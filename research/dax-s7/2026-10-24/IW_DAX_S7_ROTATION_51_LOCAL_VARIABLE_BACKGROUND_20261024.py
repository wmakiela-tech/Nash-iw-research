#!/usr/bin/env python3
"""IW/NASH DAX-S7 R51: local six-hadron source model on variable Wu-Xu background.
NOT a full trajectory or source Julia executor. Fixes T(t), a(t), n_PBH(t)
locally across an off-grid three-crossing episode. Initial X and hadrons are
conditional. Source T and emission rows are pinned to public repository blobs;
source log-log hadron rates extrapolate below data minimum. No physical upgrade.
"""
from __future__ import annotations
import math,json,argparse,csv
from pathlib import Path
PI=math.pi
T_NUC=.07818527068831995
MF=9.6725e9; BETA=1e-17
TAU=215.07211197892192
TF=1.244985657155457e-28
T_FIRST=215.05755469059486
A_FIRST=35.071137473435506
Tf=43213506455750.82
Gtop=104.86508083893959
Hcoeff=.20658852676118475
GEV_PER_G=5.609588603804452e23
HBAR=6.582119569e-25
MBARN=1/.389379338
ETA_B=6.1e-10
ZETA3=1.2020569031595942
Q_MEV=939.5654205-938.27208816
TAU_NEUTRON=878.4
TABLE_T=[
(.07693854731117557,3.696531948491963,4.218257755908624),
(.07741705290394023,3.7062823924876476,4.227322244180149),
(.07789760667108417,3.7162163534675137,4.236557985651205),
(.07838021198792086,3.726334503700429,4.245965594027054),
(.0788648721066034,3.73663755492681,4.25554571134569),
(.0793515822897443,3.7471277438535253,4.265300275999974)]
TABLE_H=[
(5.609588603804452e32,489105.5126008581,59105.93631247951,29086.774913348447,34849.08026691193,34656.17773724596),
(6.099798045788406e32,442306.73787501804,53467.712852971126,26311.795859614824,31504.591028094237,31328.963561830213)]
H_EXP=[math.log(TABLE_H[1][j]/TABLE_H[0][j])/math.log(TABLE_H[1][0]/TABLE_H[0][0]) for j in range(1,6)]
LN_TABLE=[(math.log(T),g,s) for T,g,s in TABLE_T]

def gs(T):
    x=math.log(T)
    if not LN_TABLE[0][0]<=x<=LN_TABLE[-1][0]:
        raise ValueError('T outside embedded local source table: '+str(T))
    for i in range(len(LN_TABLE)-1):
        a,b=LN_TABLE[i:i+2]
        if a[0]<=x<=b[0]:
            u=(x-a[0])/(b[0]-a[0]); g=a[1]+u*(b[1]-a[1]); s=a[2]+u*(b[2]-a[2]);
            return g,(b[1]-a[1])/(b[0]-a[0])/g,(b[2]-a[2])/(b[0]-a[0])/s
    raise AssertionError

# Exact corresponding *two inverse interpolation knots*, at T=(0.01 MeV)*geomspace(1,1e8,1000).
# This is the source's independent 1000-node log-rho -> log-T inverse locally.
INV=[]
for i in (111,112):
    TT=.01*math.exp(i*math.log(1e8)/999)
    g=gs(TT)[0];INV.append((math.log(g)+4*math.log(TT),math.log(TT)))

def T_of_L(L):
    u=(L-INV[0][0])/(INV[1][0]-INV[0][0]);return math.exp(INV[0][1]+u*(INV[1][1]-INV[0][1]))

def L_of_T(T):
    x=math.log(T);u=(x-INV[0][1])/(INV[1][1]-INV[0][1]);return INV[0][0]+u*(INV[1][0]-INV[0][0])

L_FIRST=L_of_T(T_NUC)
LF=math.log(Gtop)+4*math.log(Tf)


def fc(T,mass):
    v=math.sqrt(T/mass)+math.sqrt(T/.93827208816)
    x=2*PI/137.035999084/v
    return x/(-math.expm1(-x))


def sxs(T):
    return (1.5*MBARN*fc(T,.13957039),1.7*MBARN,
            31*MBARN*fc(T,.493677),14.5*MBARN*fc(T,.493677),
            26*MBARN,34*MBARN,7*MBARN,10*MBARN,7*MBARN,10*MBARN,
            28*MBARN,37*MBARN,28*MBARN,37*MBARN)


def emission(y):
    val=MF*GEV_PER_G*y/TABLE_H[0][0]
    e=[TABLE_H[0][j]*val**H_EXP[j-1] for j in range(1,6)]
    return (e[0],e[0],e[1],e[2],e[3],e[4])


def background(L,A,y):
    TT=T_of_L(L);g,r,s=gs(TT)
    B=BETA*math.exp(LF-L-3*A)
    H=Hcoeff*math.exp(L/2)*math.sqrt(1+B*y)
    C=-4+r/(3+s)
    return TT,H,B,C


def neutron(T,X,n):
    nB=ETA_B*2*ZETA3/PI**2*(T*.001)**3
    sx=sxs(T*.001)
    pm,pp,kpn,kpo,knp,kno,k0pn,k0po,k0np,k0no,pbn,pbp,nbp,nbn=sx
    x=Q_MEV/T
    gam=255/TAU_NEUTRON*(12+6*x+x*x)/x**5
    weak=-gam*(X-(1-X)*math.exp(-x))-X/TAU_NEUTRON
    plus=(1-X)*(n[0]*pm+n[2]*kpn+n[3]*k0pn+n[5]*nbp)/HBAR
    minus=X*(n[1]*pp+n[2]*knp+n[3]*k0np+n[4]*pbn)/HBAR
    return weak+plus-minus,weak,plus-minus


def hadrons_D(T,X):
    nB=ETA_B*2*ZETA3/PI**2*(T*.001)**3
    pm,pp,kpn,kpo,knp,kno,k0pn,k0po,k0np,k0no,pbn,pbp,nbp,nbn=sxs(T*.001)
    fac=nB/HBAR
    return [1/2.6033e-8+(1-X)*pm*fac,1/2.6033e-8+X*pp*fac,
        8.1e7+(X*(knp+kno)+(1-X)*(kpn+kpo))*fac,
        2e7+(X*(k0np+k0no)+(1-X)*(k0pn+k0po))*fac,
        (X*pbn+(1-X)*pbp)*fac,((1-X)*nbp+X*nbn)*fac]


def hadrons_S(y,A):
    # n_PBH = n_PBH,f * (a_f/a)^3, as source code, physical units GeV^3
    rho_f=PI**2/30*Gtop*(Tf*.001)**4
    nPBHf=BETA*rho_f/(MF*GEV_PER_G)
    nPBH=nPBHf*math.exp(-3*A)
    return [nPBH*z/HBAR for z in emission(y)] if y>0 else [0.]*6


def evolve_n(n,D,S,dt):
    return [math.exp(-D[j]*dt)*n[j]+(-math.expm1(-D[j]*dt))*S[j]/D[j] for j in range(6)]


def local(nsteps=12000,xfirst=.11,scale_had=1,initial_hadron_factor=1.,a_first=A_FIRST):
    yfirst=((TF+TAU-T_FIRST)/TAU)**(1/3)
    if abs(T_FIRST-(TF+TAU*(1-yfirst**3)))>1e-9: raise AssertionError
    y=yfirst;A=a_first;L=L_FIRST;X=xfirst
    Tin,H,B,C=background(L,A,y)
    n=[a*scale_had*initial_hadron_factor/b for a,b in zip(hadrons_S(y,A),hadrons_D(Tin,X))]
    events=[{'t':T_FIRST,'ln_a':A,'X':X,'direction':'down','phase':'initial'}]
    # Hadron and X integrator strang/exp method, background RK4 in remaining mass y.
    def b_rhs(yy,l,a):
        T,H,B,C=background(l,a,yy)
        return -3*TAU*yy*yy*H*C-B,-3*TAU*yy*yy*H
    def bg_step(y,h,L,A):
        p=b_rhs(y,L,A);q=b_rhs(y+h/2,L+p[0]*h/2,A+p[1]*h/2)
        k=b_rhs(y+h/2,L+q[0]*h/2,A+q[1]*h/2);r=b_rhs(y+h,L+k[0]*h,A+k[1]*h)
        return L+h/6*(p[0]+2*q[0]+2*k[0]+r[0]),A+h/6*(p[1]+2*q[1]+2*k[1]+r[1])
    h=-yfirst/nsteps
    maxT=T_NUC;minT=T_NUC
    for i in range(nsteps):
        ynew=max(0.,y+h);ymid=(y+ynew)/2;dt=TAU*(y**3-ynew**3)
        Lnew,Anew=bg_step(y,ynew-y,L,A)
        Tnew=T_of_L(Lnew)
        Tmid=T_of_L((L+Lnew)/2)
        S=[v*scale_had for v in hadrons_S(ymid,(A+Anew)/2)]
        D=hadrons_D(Tmid,X)
        nmid=evolve_n(n,D,S,dt/2)
        xmid=X+dt/2*neutron(Tmid,X,nmid)[0]
        Dmid=hadrons_D(Tmid,xmid)
        nmid=evolve_n(n,Dmid,S,dt/2)
        xnew=X+dt*neutron(Tmid,xmid,nmid)[0]
        nnew=evolve_n(n,Dmid,S,dt)
        if (Tin-T_NUC)*(Tnew-T_NUC)<0:
            theta=(T_NUC-Tin)/(Tnew-Tin)
            t=TF+TAU*(1-y**3)+theta*dt
            events.append({'t':t,'ln_a':A+(Anew-A)*theta,'X':X+(xnew-X)*theta,'direction':'up' if Tnew>Tin else 'down','phase':'evap'})
        maxT=max(maxT,Tnew);minT=min(minT,Tnew)
        y=ynew;L=Lnew;A=Anew;X=xnew;n=nnew;Tin=Tnew
    tev=TF+TAU;Xe=X;T_evap=Tin
    # Post evaporative crossing, keep finite antinucleon decay/annihilation; no source.
    postdt=.0000015
    t=tev
    while Tin>T_NUC or len(events)<3:
        dt=postdt
        Tb,H,B,C=background(L,A,0.)
        k1=H*C; q1=H
        Tm,Hm,Bm,Cm=background(L+k1*dt/2,A+q1*dt/2,0.)
        Lnew=L+dt*Hm*Cm;Anew=A+dt*Hm
        Tnew=T_of_L(Lnew)
        D=hadrons_D(Tm,X)
        nmid=evolve_n(n,D,[0]*6,dt/2)
        xmid=X+dt/2*neutron(Tm,X,nmid)[0]
        Dm=hadrons_D(Tm,xmid)
        nmid=evolve_n(n,Dm,[0]*6,dt/2)
        xnew=X+dt*neutron(Tm,xmid,nmid)[0]
        nnew=evolve_n(n,Dm,[0]*6,dt)
        if (Tin-T_NUC)*(Tnew-T_NUC)<0:
            theta=(T_NUC-Tin)/(Tnew-Tin)
            events.append({'t':t+theta*dt,'ln_a':A+(Anew-A)*theta,'X':X+(xnew-X)*theta,'direction':'up' if Tnew>Tin else 'down','phase':'post'})
        t+=dt;L=Lnew;A=Anew;X=xnew;n=nnew;Tin=Tnew
        if t>tev+.25: break
    return {'steps':nsteps,'X_first':xfirst,'scaled_emission':scale_had,'initial_hadron_factor':initial_hadron_factor,'a_first':a_first,'events':events,'X_at_evap':Xe,'T_at_evap':T_evap,'T_min_before_evap':minT,'T_max_before_evap':maxT,'delta_X':events[-1]['X']-events[0]['X'] if len(events)>=3 else None,'T_start':T_of_L(L_FIRST),'y_first':yfirst,'nPBH_scale_end':math.exp(-3*(A-a_first))}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--steps',type=int,default=12000)
    parser.add_argument('--selftest',action='store_true')
    parser.add_argument('--suite-prefix',type=Path,help='Write reproduction matrix CSV and summary JSON')
    parser.add_argument('--xfirst',type=float,default=.11)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=local(args.steps,args.xfirst)
    if args.suite_prefix is not None:
        suite=[]
        for n in (3000,6000,12000,24000,48000):
            suite.append(('convergence',n,local(n,.11)))
        for x in (.08,.11,.2,.4,.6,.8):
            suite.append(('X_initial',x,local(12000,x)))
        for k in (0,.1,.25,.5,1,1.5,2):
            suite.append(('emission_scale',k,local(12000,.11,k)))
        for k in (0,.25,.5,1,2,5):
            suite.append(('initial_hadron_factor',k,local(12000,.11,1,k)))
        for k in (-.0002,-.0001,-.00002,0,.00002,.0001,.0002):
            suite.append(('A_initial_offset',k,local(12000,.11,1,1,A_FIRST+k)))
        fields=('group','test_value','steps','X_initial','scale_emission','initial_hadron_factor','A_initial','crossing_count','t2_s','t3_s','X2','X3','delta_X','T_evap_MeV','PBH_number_dilution_factor')
        csvfile=args.suite_prefix.with_suffix('.csv')
        with csvfile.open('w',newline='',encoding='utf-8') as ff:
            w=csv.DictWriter(ff,fieldnames=fields);w.writeheader()
            for group,p,r in suite:
                events=r['events']
                w.writerow(dict(group=group,test_value=p,steps=r['steps'],X_initial=r['X_first'],scale_emission=r['scaled_emission'],initial_hadron_factor=r['initial_hadron_factor'],A_initial=r['a_first'],crossing_count=len(events),t2_s=events[1]['t'] if len(events)>1 else '',t3_s=events[2]['t'] if len(events)>2 else '',X2=events[1]['X'] if len(events)>1 else '',X3=events[2]['X'] if len(events)>2 else '',delta_X=r['delta_X'],T_evap_MeV=r['T_at_evap'],PBH_number_dilution_factor=r['nPBH_scale_end']))
        metadata=dict(status='LOCAL_SOURCE_EQUATION_MATCHED_NOT_FULL_JULIA',source='Fenyutanchan/Primordial-Black-Hole',source_background='main-scan.jl plus N_around_m_e.csv',source_emission='data/out/hadrons_from_PBH.dat, below-table loglog EXTRAPOLATION',background_ref='DAX-S7 rotation 49 first crossing coordinates',source_blobs=dict(background='b368ba55d5a493f7bc185909730f7fe5691f10d6',thermo='93f2494f026c5d0587ea40fe08bb938dd9d01fa8',emission='06d0883a27b108692720422294ba2baacd381a64'),mass_g=MF,beta=BETA,Tn_MeV=T_NUC,first_crossing_s=T_FIRST,conditional_Xn_first=.11,base=local(12000,.11),num_suite_rows=len(suite),series=[dict(group=g,value=v,output=r) for g,v,r in suite])
        jsonfile=args.suite_prefix.with_suffix('.json')
        jsonfile.write_text(json.dumps(metadata,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
        print('SUITE PASS',len(suite),'tests',csvfile,jsonfile)
    if args.selftest:
        assert len(result['events']) == 3, result
        assert abs(result['delta_X'] - 0.0019265303330826544) < 1e-7, result
        assert abs(result['T_start'] - T_NUC) < 1e-12, result
        print('SELF-CHECK PASS: three crossings / hadron X / inverse-T knot alignment')
    if args.output: args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
