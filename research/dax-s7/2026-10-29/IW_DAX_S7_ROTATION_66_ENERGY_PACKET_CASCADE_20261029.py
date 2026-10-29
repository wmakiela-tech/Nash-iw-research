#!/usr/bin/env python3
"""DAX-S7 R66: conditional, energy-weighted electromagnetic branching test.

Independent gamma-gamma Breit-Wheeler opacity + Jones/Blumenthal-Gould
isotropic inverse-Compton differential kernel on a fixed blackbody Tgamma.
The correct angular average has 1/2. Monte Carlo follows a RANDOM UNIT
OF CARRIED ENERGY down the branching tree (size-biased sampling).
It stops at E <= E_cut (default 0.1 GeV), which is NOT deposition or heating.
Pair energy split is a deliberately EXTERNAL PROXY (equal, beta(2,2),
or 0.1/0.9). No pair-production differential kernel, plasma collective
processes, EM cascades with other channels, kinetic feedback, full BlackHawk
spectra, or any PBH constraint is claimed.

Dependencies: numpy, scipy. Entrypoint --quick or full; --out.
"""
from __future__ import annotations
import argparse, csv, json, hashlib, math, pathlib, time
import numpy as np
from scipy.special import roots_legendre

SIGMA_T=6.6524587321e-25; C=2.99792458e10
HC=1.973269804e-11; ME=0.51099895; TNUC=.07818527068831995

def sigma_bw(E, eps, a):
    # E,eps MeV; a=1-cos(theta), pair threshold E eps a > 2 me^2.
    with np.errstate(divide='ignore',invalid='ignore',over='ignore'):
        u=2*ME**2/(E*eps*a)
        v=(u>0)&(u<1)
        q=np.where(v,u,1.)
        b=np.sqrt(1-q)
        L=2*np.log1p(b)-np.log(q)
        s=(3/16)*SIGMA_T*q*((3-(1-q)**2)*L-2*b*(1+q))
    return np.where(v,np.maximum(s,0),0)

class BWC:
    def __init__(self,n=105):
        zz,w=roots_legendre(n)
        self.x=21*(zz+1);self.wx=21*w
        self.a=zz+1;self.wa=w/2 # essential isotropic angular factor
        self.wn=self.wx*self.x**2/np.expm1(self.x)
    def calc(self,E_GeV,T=TNUC):
        E=E_GeV*1e3
        ss=sigma_bw(E,T*self.x[:,None],self.a[None,:])
        val=C*(T/HC)**3/math.pi**2 * np.dot(self.wn,ss@(self.a*self.wa))
        return float(val)

class BG:
    def __init__(self,nx=88,nq=115):
        zx,wx=roots_legendre(nx)
        self.x=20*(zx+1);self.wx=20*wx
        self.wphot=self.wx*self.x/np.expm1(self.x)
        self.zq,self.wq=roots_legendre(nq)
    def calc(self,E_GeV,T=TNUC,dist=False):
        gamma=E_GeV*1e3/ME
        if gamma<100:raise ValueError('IC ultra-relativistic kernel use requires gamma >=100')
        qLower=-max(44.,np.log(4*gamma*T*self.x[-1]/ME)+19.)
        logq=qLower*(1-self.zq)/2
        q=np.exp(logq)
        wlog=self.wq*(-qLower)/2
        G=(4*gamma*T/ME)*self.x[:,None]
        z=G*q[None,:]
        k=2*q[None,:]*logq[None,:]+(1+2*q[None,:])*(1-q[None,:])+z*z*(1-q[None,:])/(2*(1+z))
        np.maximum(k,0,out=k)
        frac=z/(1+z)
        jac=E_GeV*1e3*z/(1+z)**2
        weight=self.wphot[:,None]*wlog[None,:]*k*jac
        pref=3*SIGMA_T*C/(4*gamma**2)*(T/HC)**3/math.pi**2/T
        total=float(np.sum(weight));rate=pref*total
        if not dist:return float(rate),float(np.sum(weight*frac)/total)
        f=frac.flatten();w=weight.flatten()
        inds=np.argsort(f);f=f[inds];w=w[inds]
        cum=np.cumsum(w);cum/=cum[-1]
        return float(rate),float(np.sum(weight*frac)/total),f,cum

class Tables:
    def __init__(self,nquad=105,ngrid=125,T=TNUC,cut=.1,emax=1e12):
        self.cut=cut;self.emax=emax;self.T=T
        self.E=np.geomspace(cut,emax,ngrid)
        self.logE=np.log(self.E);self.logE0=self.logE[0];self.inv_dlog=(ngrid-1)/(self.logE[-1]-self.logE[0])
        bw=BWC(nquad);bg=BG(max(60,nquad-10),nquad)
        self.bw=np.array([bw.calc(E,T) for E in self.E]);self.ic=np.empty(ngrid)
        self.fc=[];self.cdf=[];self.mean=[]
        for i,E in enumerate(self.E):
            rate,mean,f,cdf=bg.calc(E,T,dist=True)
            self.ic[i]=rate;self.mean.append(mean)
            # replace ~10000 quadrature nodes by a 1024 quantile table,
            # preserving the cumulative distribution of scattering output f.
            grid=(np.arange(1024)+.5)/1024
            self.fc.append(np.interp(grid,cdf,f))
        self.fc=np.asarray(self.fc);self.mean=np.asarray(self.mean)
        self.logBW=np.log(self.bw);self.logIC=np.log(self.ic)
    def sample(self, E,which,rng):
        # rate geometric interpolation, f distribution nearest tabulated bin.
        le=math.log(E)
        z=(le-self.logE0)*self.inv_dlog
        i=max(0,min(len(self.E)-2,int(z)))
        t=z-i
        rates=self.logBW if which=='photon' else self.logIC
        rate=math.exp((1-t)*rates[i]+t*rates[i+1])
        if which=='photon':return rate,None
        closest=i if t<.5 else i+1
        f=self.fc[closest,rng.integers(len(self.fc[closest]))]
        return rate,float(f)


def cascade(tables,E0,kind,split,ntrials,seed,cut=.1,maxevents=700):
    rng=np.random.default_rng(seed)
    durations=np.empty(ntrials);counts=np.empty(ntrials,dtype=int)
    stepsBW=np.empty(ntrials,dtype=int);stepsIC=np.empty(ntrials,dtype=int)
    unresolved=0
    for i in range(ntrials):
        E=E0;part=kind;tm=0;bwct=0;icct=0
        for j in range(maxevents):
            if E <=cut:break
            rate,f=tables.sample(E,part,rng)
            tm+=rng.exponential()/rate
            if part=='photon':
                bwct+=1
                # pair-production spectrum NOT determined here; stress-test split.
                if split=='equal':z=.5
                elif split=='asymmetric':z=.1
                elif split=='beta22':z=rng.beta(2,2)
                else:raise ValueError(split)
                E*=z if rng.random()<z else (1-z)
                part='electron'
            else:
                icct+=1
                if rng.random()<f:
                    E*=f;part='photon'
                else:E*=(1-f)
        else:unresolved+=1
        durations[i]=tm;counts[i]=j;stepsBW[i]=bwct;stepsIC[i]=icct
    return {'initial_kind':kind,'pair_energy_split_proxy':split,'E0_GeV':E0,'Ecut_GeV':cut,
            'ntrials':ntrials,'unresolved':unresolved,'mean_s':float(np.mean(durations)),
            'median_s':float(np.median(durations)),'p90_s':float(np.quantile(durations,.9)),
            'p99_s':float(np.quantile(durations,.99)),
            'p999_s':float(np.quantile(durations,.999)),
            'upper_95p_for_frac_over_0p003s':float((np.sum(durations>.003)+1.96**2/2+1.96*np.sqrt(np.sum(durations>.003)*(1-np.sum(durations>.003)/ntrials)+1.96**2/4))/(ntrials+1.96**2)),
            'max_s':float(np.max(durations)),
            'frac_over_0p003s':float(np.mean(durations>.003)),
            'frac_over_0p05s':float(np.mean(durations>.05)),
            'mean_events':float(np.mean(counts)),'mean_bw':float(np.mean(stepsBW)),
            'mean_ic':float(np.mean(stepsIC))}

def main():
    p=argparse.ArgumentParser();p.add_argument('--out',default='.')
    p.add_argument('--quick',action='store_true');p.add_argument('--seed',type=int,default=66129)
    p.add_argument('--cut',type=float,default=.1,help='Energy carrier STOP threshold GeV, not deposition')
    p.add_argument('--ntrials',type=int,default=None);p.add_argument('--nquad',type=int,default=None)
    a=p.parse_args();out=pathlib.Path(a.out);out.mkdir(exist_ok=True,parents=True)
    quick=a.quick
    n= a.nquad or (85 if quick else 130);nt=a.ntrials or (250 if quick else 1600)
    start=time.perf_counter()
    tab=Tables(n,100 if quick else 160,cut=a.cut)
    assert np.all(tab.bw>0) and np.all(tab.ic>0)
    cases=[];energies=[1e3,1e6,1e9,1e12]
    for E in energies:
        for kind in ['photon','electron']:
            for split in ['equal','beta22','asymmetric']:
                row=cascade(tab,E,kind,split,nt,a.seed+int(math.log10(E))*100+len(cases),cut=a.cut)
                cases.append(row)
                print('E',E,'kind',kind,'split',split,'median',row['median_s'],'p99',row['p99_s'],'mean_event',row['mean_events'],flush=True)
    columns=list(cases[0]);cp=out/'IW_DAX_S7_R66_ENERGY_WEIGHTED_CASCADE_PATHS_20261029.csv'
    with cp.open('w',newline='',encoding='utf8') as f:
        writer=csv.DictWriter(f,fieldnames=columns);writer.writeheader();writer.writerows(cases)
    samples=[{'E_GeV':float(E),'BW_s':float(1/bw),'IC_s':float(1/ic),'IC_mean_frac_out':float(f)} for E,bw,ic,f in zip(tab.E,tab.bw,tab.ic,tab.mean)]
    sp=out/'IW_DAX_S7_R66_BW_BG_LOGGRID_RATES_20261029.csv'
    with sp.open('w',newline='',encoding='utf8') as f:
        writer=csv.DictWriter(f,fieldnames=list(samples[0]));writer.writeheader();writer.writerows(samples)
    # Required sanity: high energy interaction times remain compatible with R65.
    ref={1e3:(1.62945e-10,2.89301e-10),1e6:(1.02942e-7,1.90639e-7)}
    for E,(bt,it) in ref.items():
        i=np.searchsorted(tab.E,E);e0,e1=tab.E[i-1:i+1]
        b=math.exp(np.interp(math.log(E),np.log(tab.E),np.log(tab.bw)))
        ic=math.exp(np.interp(math.log(E),np.log(tab.E),np.log(tab.ic)))
        assert abs(1/b/bt-1)<.03,(E,'BW',1/b,bt)
        assert abs(1/ic/it-1)<.03,(E,'IC',1/ic,it)
    result={'rotation':66,'name':'Energy-weighted branching proxy for sub-GeV EM transport',
            'physical_status':'PROXY_NOT_DEPOSITION','source':'BW isotropic exact total + BG ultrarelativistic differential IC',
            'T_MeV':TNUC,'Ecut_GeV':tab.cut,'pair_distribution':'equal or fixed .1/.9 or beta(2,2) unvalidated proxy',
            'number_of_paths_per_case':nt,'nquad':n,'ngrid':len(tab.E),'repro_seed':a.seed,
            'elapsed_seconds':time.perf_counter()-start,
            'limits':['Crossing 0.1 GeV not thermal heating or energy deposition','No pair differential cross section',
                      'No synchrotron, BH, weak channels, photon injection feedback, expansion',
                      'No physical Hawking source spectrum','No low-energy IC kernel below gamma=100','No PBH bound'],
            'cases':cases}
    (out/'IW_DAX_S7_R66_CASCADE_NUMERICAL_SUMMARY_20261029.json').write_text(json.dumps(result,indent=2),encoding='utf8')
    print('DONE',len(cases),'cases',result['elapsed_seconds'],'sec')
if __name__=='__main__':main()
