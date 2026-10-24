#!/usr/bin/env python3
# IW/NASH DAX-S7 — rotation 52.
# An independent Wu–Xu source-equation reconstruction with finite-life six-channel hadrons.
# NOT the original Julia solver. Does not establish physical PBH bounds or a discovery.
# Usage:
#  python IW_DAX_S7_ROTATION_52_FULL_HISTORY_SOURCE_RECONSTRUCTION_20261025.py --source-dir ./arXiv-2509.05618/data --download --out results.json
#  python IW_DAX_S7_ROTATION_52_FULL_HISTORY_SOURCE_RECONSTRUCTION_20261025.py --selftest
from __future__ import annotations
import argparse
import hashlib
import json
import math
import urllib.request
from pathlib import Path
import numpy as np

PI=math.pi
GEV_PER_GRAM=5.609588603804452e23
HBAR_GEV_S=6.582119569e-25
HCOEFF=.20658852676118475
MPLANCK_G=2.176434e-5
TPL_S=5.391247e-44
GAMMA=1/(3*math.sqrt(3))
TAU_N=878.4
ETA_B=6.1e-10
ZETA3=1.2020569031595942
MBARN_GEV2=1/.389379338
PROTON_GEV=.93827208816
ALPHA_EM=1/137.035999084
Q_MEV=939.5654205-938.27208816
T_NUC_MEV=.07818527068831995

PUBLIC_REPO='https://raw.githubusercontent.com/Fenyutanchan/Primordial-Black-Hole/master/arXiv-2509.05618/data/'
SOURCES={
 'ext/N_around_m_e.csv':'93f2494f026c5d0587ea40fe08bb938dd9d01fa8',
 'ext/N_s_from_PDG2024.csv':'33aceb876fc36cb2486d36c690e6401d85d76b46',
 'ext/N_rho_OVER_N_s_from_PDG2024.csv':'28b0c13563d7b3bdeaee191a3a981197345d05b8',
 'out/hadrons_from_PBH.dat':'06d0883a27b108692720422294ba2baacd381a64'
}

def git_blob_sha(raw:bytes)->str:
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


def obtain_source(folder:Path,download:bool):
    for sub,expected in SOURCES.items():
        path=folder/sub
        if (not path.exists() or git_blob_sha(path.read_bytes())!=expected) and download:
            path.parent.mkdir(parents=True,exist_ok=True)
            with urllib.request.urlopen(PUBLIC_REPO+sub,timeout=30) as f: raw=f.read()
            observed=git_blob_sha(raw)
            if observed!=expected:
                raise ValueError(f'Source changed: {sub}: {observed} != {expected}')
            path.write_bytes(raw)
        if not path.exists():raise FileNotFoundError(f'Missing source {path}; use --download')
        actual=git_blob_sha(path.read_bytes())
        if actual!=expected:raise ValueError(f'Source blob mismatch: {path}: {actual} != {expected}')
    return folder


def log_interpolate(tab:np.ndarray,x:float,j:int=1,logx:bool=True):
    arr=tab[:,0]
    idx=int(np.searchsorted(arr,x,side='right'))-1
    if idx<0:return float(tab[0,j]),0.
    if idx>=len(arr)-1:return float(tab[-1,j]),0.
    d=math.log(arr[idx+1]/arr[idx]) if logx else (arr[idx+1]-arr[idx])
    slope=(float(tab[idx+1,j])-float(tab[idx,j]))/d
    diff=math.log(x/arr[idx]) if logx else (x-arr[idx])
    return float(tab[idx,j]+slope*diff),slope


class Tables:
    def __init__(self,folder:Path):
        self.low=np.loadtxt(folder/'ext/N_around_m_e.csv',delimiter=',')
        self.hs=np.loadtxt(folder/'ext/N_s_from_PDG2024.csv',delimiter=',')
        self.hr=np.loadtxt(folder/'ext/N_rho_OVER_N_s_from_PDG2024.csv',delimiter=',')
        self.emission=np.loadtxt(folder/'out/hadrons_from_PBH.dat',skiprows=1)
        self.lnemission=np.log(self.emission)
        self.gtop=float(self.hs[-1,1]*self.hr[-1,1])
        self.NBH=27*self.gtop/(4*30720*PI)
        # Source inverse interpolation: 1000 geometric T nodes from 1e-5 to 1e3 GeV.
        tg=np.geomspace(.01,1.e6,1000)
        rho=np.array([self.thermo(float(t))[0]*t**4 for t in tg])
        self.inv_lnrho=np.log(rho)
        self.inv_lnT=np.log(tg)
        assert np.all(np.diff(self.inv_lnrho)>0)

    def thermo(self,T:float):
        if T<=10:
            g,dg=log_interpolate(self.low,T,1)
            s,ds=log_interpolate(self.low,T,2)
            return g,dg/g,ds/s
        s,ds=log_interpolate(self.hs,T,1)
        q,dq=log_interpolate(self.hr,T,1)
        return s*q,ds/s+dq/q,ds/s

    def T_of_L(self,L:float):
        j=int(np.searchsorted(self.inv_lnrho,L,side='right'))-1
        j=max(0,min(len(self.inv_lnrho)-2,j))
        weight=(L-self.inv_lnrho[j])/(self.inv_lnrho[j+1]-self.inv_lnrho[j])
        return math.exp(float(self.inv_lnT[j]+weight*(self.inv_lnT[j+1]-self.inv_lnT[j])))

    def rates(self,M_g:float):
        v=math.log(M_g*GEV_PER_GRAM)
        j=int(np.searchsorted(self.lnemission[:,0],v,side='right'))-1
        j=max(0,min(len(self.lnemission)-2,j))
        w=(v-self.lnemission[j,0])/(self.lnemission[j+1,0]-self.lnemission[j,0])
        p=np.exp(self.lnemission[j,1:]*(1-w)+self.lnemission[j+1,1:]*w)
        return np.array((p[0],p[0],p[1],p[2],p[3],p[4]))


class Reconstructor:
    def __init__(self,tables:Tables,mass_g:float=9.6725e9,beta:float=1e-17):
        self.th=tables;self.M=mass_g;self.beta=beta
        self.tf=(mass_g/MPLANCK_G)*TPL_S/GAMMA
        self.tau=(mass_g/MPLANCK_G)**3*TPL_S/(3*tables.NBH)
        self.Tf=math.sqrt(1/(2*self.tf*HCOEFF*math.sqrt(tables.gtop)))
        self.Lf=math.log(tables.gtop)+4*math.log(self.Tf)
        self.npbhf=beta*(PI**2/30)*tables.gtop*(self.Tf*1e-3)**4/(mass_g*GEV_PER_GRAM)
        self.ycut=math.exp(-20)

    def background(self,L,A,y):
        T=self.th.T_of_L(L)
        g,r,s=self.th.thermo(T)
        B=self.beta*math.exp(self.Lf-L-3*A)
        H=HCOEFF*math.exp(L/2)*math.sqrt(1+B*y)
        return T,H,B,-4+r/(3+s)

    @staticmethod
    def coulomb(Tgev,mgev):
        speed=math.sqrt(Tgev/mgev)+math.sqrt(Tgev/PROTON_GEV)
        x=2*PI*ALPHA_EM/speed
        return x/(-math.expm1(-x))

    def hadron_rates(self,T_MeV,X,y,A,hadfactor:float):
        Tg=T_MeV*.001
        nb=ETA_B*2*ZETA3/PI**2*Tg**3
        q=Q_MEV/T_MeV
        weak=(255/TAU_N)*(12+6*q+q*q)/q**5
        wa=weak*math.exp(-q)
        wb=weak+1/TAU_N
        pm=1.5*MBARN_GEV2*self.coulomb(Tg,.13957039)
        pp=1.7*MBARN_GEV2
        kpn=31*MBARN_GEV2*self.coulomb(Tg,.493677)
        kpo=14.5*MBARN_GEV2*self.coulomb(Tg,.493677)
        knp=26*MBARN_GEV2
        kno=34*MBARN_GEV2
        k0pn=7*MBARN_GEV2
        k0po=10*MBARN_GEV2
        k0np=7*MBARN_GEV2
        k0no=10*MBARN_GEV2
        pbn=28*MBARN_GEV2
        pbp=37*MBARN_GEV2
        nbp=28*MBARN_GEV2
        nbn=37*MBARN_GEV2
        d=np.array((
            1/2.6033e-8+nb*pm*(1-X)/HBAR_GEV_S,
            1/2.6033e-8+nb*pp*X/HBAR_GEV_S,
            8.1e7+nb*(X*(knp+kno)+(1-X)*(kpn+kpo))/HBAR_GEV_S,
            2.e7+nb*(X*(k0np+k0no)+(1-X)*(k0pn+k0po))/HBAR_GEV_S,
            nb*(X*pbn+(1-X)*pbp)/HBAR_GEV_S,
            nb*(X*nbn+(1-X)*nbp)/HBAR_GEV_S
        ))
        src=(np.zeros(6) if y<=0 or hadfactor==0 else
             self.th.rates(self.M*y)*self.npbhf*math.exp(-3*A)*hadfactor/HBAR_GEV_S)
        plus=np.array((pm,0.,kpn,k0pn,0.,nbp))/HBAR_GEV_S
        minus=np.array((0.,pp,knp,k0np,pbn,0.))/HBAR_GEV_S
        return wa,wb,d,src,plus,minus

    @staticmethod
    def n_step(n,d,src,dt):
        z=-np.expm1(-d*dt)
        return n*(1-z)+z*src/d

    @staticmethod
    def x_step(X,wa,wb,plus,minus,n,dt):
        gain=wa+float(plus@n)
        loss=wb+float(minus@n)
        equilibrium=gain/(gain+loss)
        return equilibrium+(X-equilibrium)*math.exp(-(gain+loss)*dt)

    def run(self,nx=16000,ny=20000,npost=10000,hadfactor=1.,quasistationary=False):
        L,A=self.Lf,0.
        X=1/(1+math.exp(Q_MEV/self.Tf))
        n=np.full(6,1.e-60*2*ZETA3/PI**2*(self.Tf*.001)**3)
        tprev,prevT=self.tf,self.Tf
        targets=[10000,100,10,2,1,.5,.3,.2,.15,.1,T_NUC_MEV]
        checks=[];events=[]

        def bge(x,h,f):
            k1=f(x,L,A)
            k2=f(x+h/2,L+h*k1[0]/2,A+h*k1[1]/2)
            k3=f(x+h/2,L+h*k2[0]/2,A+h*k2[1]/2)
            k4=f(x+h,L+h*k3[0],A+h*k3[1])
            return (L+h*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6,
                    A+h*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6)

        def update(newL,newA,newt,dt,y,stage):
            nonlocal L,A,X,n,prevT,tprev
            Tm=self.th.T_of_L((L+newL)/2)
            Tnew=self.th.T_of_L(newL)
            Am=(A+newA)/2
            xold=X
            wa,wb,d,src,plus,minus=self.hadron_rates(Tm,X,y,Am,hadfactor)
            if quasistationary:
                nmid=src/d
            else:
                nmid=self.n_step(n,d,src,dt/2)
            xnew=self.x_step(X,wa,wb,plus,minus,nmid,dt)
            for _ in range(2):
                midX=(xold+xnew)/2
                wa,wb,d,src,plus,minus=self.hadron_rates(Tm,midX,y,Am,hadfactor)
                nmid=src/d if quasistationary else self.n_step(n,d,src,dt/2)
                xnew=self.x_step(xold,wa,wb,plus,minus,nmid,dt)
            nnew=n if quasistationary else self.n_step(n,d,src,dt)
            if (prevT-T_NUC_MEV)*(Tnew-T_NUC_MEV)<0:
                w=(T_NUC_MEV-prevT)/(Tnew-prevT)
                events.append(dict(time_s=tprev+w*(newt-tprev),
                    ln_a=A+w*(newA-A),Xn=xold+w*(xnew-xold),stage=stage,
                    direction='up' if Tnew>prevT else 'down'))
            while targets and Tnew<=targets[0]:
                target=targets.pop(0)
                checks.append(dict(target_MeV=target,T_MeV=Tnew,t_s=newt,
                    Xn=xnew,PBH_over_SM=self.background(newL,newA,y)[2]*y,
                    mass_PBH_g=self.M*y))
            L,A,X,n,prevT,tprev=newL,newA,xnew,nnew,Tnew,newt

        xend=math.log((self.tf+.875*self.tau)/self.tf)
        hx=xend/nx
        for i in range(nx):
            x=i*hx
            t0=self.tf*math.exp(x)
            t1=self.tf*math.exp(x+hx)
            ymid=max(1e-15,1-(.5*(t0+t1)-self.tf)/self.tau)**(1/3)
            def pre(q,l,a):
                t=self.tf*math.exp(q)
                yy=max(1e-15,1-(t-self.tf)/self.tau)**(1/3)
                T,H,B,C=self.background(l,a,yy)
                return t*(H*C+B/(3*self.tau*yy*yy)),t*H
            p=bge(x,hx,pre)
            update(*p,t1,t1-t0,ymid,'pre')

        hy=(self.ycut-.5)/ny
        for i in range(ny):
            y=.5+i*hy
            yy=.5+(i+1)*hy
            ym=(y+yy)/2
            dt=self.tau*(y**3-yy**3)
            def evaporation(z,l,a):
                T,H,B,C=self.background(l,a,z)
                return -3*self.tau*z*z*H*C-B,-3*self.tau*z*z*H
            p=bge(y,hy,evaporation)
            update(*p,self.tf+self.tau*(1-yy**3),dt,ym,'evap')

        # As the source flags evaporation, nPBH abruptly vanishes, but finite
        # antinucleon densities continue to annihilate. Advance beyond the
        # evaporation surface only until third crossing / a short guard horizon.
        tend=self.tf+self.tau*(1-self.ycut**3)
        postdt=.2/npost
        for i in range(npost):
            t=tend+i*postdt
            def post(t,l,a):
                T,H,B,C=self.background(l,a,0)
                return H*C,H
            p=bge(t,postdt,post)
            update(*p,t+postdt,postdt,0,'post')
            if len(events)>=3:break
        return dict(mass_g=self.M,beta=self.beta,steps_pre=nx,steps_evap=ny,
                    tf_s=self.tf,tau_s=self.tau,Tf_MeV=self.Tf,
                    finite_hadron_populations=not quasistationary,hadron_scale=hadfactor,
                    crossings=events,checkpoints=checks,Xn_final=X,
                    Yp_code_third=(2*events[2]['Xn']/(1-events[2]['Xn'])
                        if len(events)>=3 else None))


def selftest():
    # Identity checks independent of numerical input tables.
    assert abs(GAMMA-1/(3*math.sqrt(3)))<1e-15
    assert abs(2*0.12/(1-0.12)-.2727272727272727)<1e-14
    assert len(SOURCES)==4
    assert git_blob_sha(b'test')=='30d74d258442c7c65512eafab474568dd706c430'
    print('SELFTEST PASS (source hash utility and static identities; no source trajectory)')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-dir',type=Path,default=Path('arXiv-2509.05618/data'))
    parser.add_argument('--download',action='store_true')
    parser.add_argument('--selftest',action='store_true')
    parser.add_argument('--nx',type=int,default=16000)
    parser.add_argument('--ny',type=int,default=20000)
    parser.add_argument('--mass',type=float,default=9.6725e9)
    parser.add_argument('--beta',type=float,default=1e-17)
    parser.add_argument('--had-scale',type=float,default=1.)
    parser.add_argument('--qs',action='store_true')
    parser.add_argument('--out',type=Path)
    a=parser.parse_args()
    if a.selftest:selftest();return
    obtain_source(a.source_dir,a.download)
    r=Reconstructor(Tables(a.source_dir),a.mass,a.beta).run(
        nx=a.nx,ny=a.ny,hadfactor=a.had_scale,quasistationary=a.qs)
    txt=json.dumps(r,ensure_ascii=False,indent=2)+'\n'
    if a.out:a.out.write_text(txt,encoding='utf8')
    print(txt)


# Rotation 53: source-table beta sweep from FULL formation time, source equations.
# --beta-scan --source-dir <path> --out <csv> [--nx 16000 --ny 20000]
# No independent Julia run, PBH bound, or nuclear network.
def beta_scan53():
    import csv
    import argparse
    ap=argparse.ArgumentParser(description='DAX-S7 rotation53 source-table beta sweep (quasi-stationary hadrons).')
    ap.add_argument('--beta-scan',action='store_true')
    ap.add_argument('--source-dir',type=Path,default=Path('arXiv-2509.05618/data'))
    ap.add_argument('--download',action='store_true')
    ap.add_argument('--out',type=Path,default=Path('IW_DAX_S7_ROTATION_53_RECOMPUTED.csv'))
    ap.add_argument('--nx',type=int,default=16000)
    ap.add_argument('--ny',type=int,default=20000)
    ap.add_argument('--mass',type=float,default=9.6725e9)
    args=ap.parse_args()
    obtain_source(args.source_dir,args.download)
    th=Tables(args.source_dir)
    betas=[0,1e-22,3e-22,1e-21,2e-21,3e-21,5e-21,7e-21,1e-20,
           1.5e-20,2e-20,3e-20,5e-20,1e-19,2e-19,5e-19,1e-18,3e-18,1e-17]
    columns=['beta','neutron_Xn_first','Yp_code_2X_over_1minusX','Yp_mass_2X','n_crossings']
    rows=[]
    for beta in betas:
        result=Reconstructor(th,args.mass,beta).run(nx=args.nx,ny=args.ny,quasistationary=True)
        crossings=result['crossings']
        if not crossings:
            raise RuntimeError('No temperature crossing at beta='+str(beta))
        X=crossings[0]['Xn']
        record={'beta':beta,'neutron_Xn_first':X,'Yp_code_2X_over_1minusX':2*X/(1-X),
                'Yp_mass_2X':2*X,'n_crossings':len(crossings)}
        rows.append(record)
        print('beta=',f'{beta:.5e}','Xn=',f'{X:.9g}','crossings=',len(crossings),flush=True)
    with args.out.open('w',encoding='utf-8',newline='') as out:
        writer=csv.DictWriter(out,fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)
    print('SAVED',args.out)

if __name__=='__main__':
    import sys
    if '--beta-scan' in sys.argv:
        beta_scan53()
    else:
        main()
