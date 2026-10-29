#!/usr/bin/env python3
"""DAX-S7 R67: differential Breit-Wheeler pair angular Monte Carlo with R66 controls.

Independent gamma-gamma Breit-Wheeler opacity + Jones/Blumenthal-Gould
isotropic inverse-Compton differential kernel on a fixed blackbody Tgamma.
The correct angular average has 1/2. Monte Carlo follows a RANDOM UNIT
OF CARRIED ENERGY down the branching tree (size-biased sampling).
It stops at E <= E_cut (default 0.1 GeV), which is NOT deposition or heating.
Pair energy split controls: external proxies (equal, beta(2,2),
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


# SOURCE for d sigma/d Omega (unpolarized):
# Drebot et al., Phys. Rev. Accel. Beams 20, 043402 (2017), Eq. (1)
# DOI: 10.1103/PhysRevAccelBeams.20.043402
# d sigma/d Omega = (r_e^2 beta / s_bar) *
# [1+2 beta^2 sin^2(theta)-beta^4(1+sin^4(theta))] /
# (1-beta^2 cos^2(theta))^2; s_bar=s/(m_e^2).
# The equivalent [1 - beta^4 cos^4(theta)
# +2 beta^2(1-beta^2)sin^2(theta)] numerator is manifestly positive.
# Analytical transformed variable t = atanh(beta |cos(theta_CM)|):
#   d sigma/dt (both signs) = 3 sigma_T q /8 * F(t;q)
#   F(t;q) = 2+2q-sech^2(t)-2 q^2 cosh^2(t)
#           = 1+z^2 + 2q*(1-q-z^2)/(1-z^2), z=tanh(t), q=1-beta^2.
#   t_max = asinh(beta/sqrt(q))
# Integral equals exact total BW sigma = (3 sigma_T q/16)*
#   ((3-beta^4)*2*tmax - 2 beta*(2-beta^2)).

class BWDifferential:
    """Sample physical target Planck photon and exact CM lepton angle.

    Class returns pair energy fractions relative to Ehard + epsilon. The
    subsequent cascade follows fractions of HARD energy; background epsilon
    is neglected in that ledger, a relative O(epsilon/Ehard) approximation.
    """
    def __init__(self, energies_GeV, T=TNUC, nquad=88):
        self.T = T
        self.E=np.asarray(energies_GeV)
        nodes, weights=roots_legendre(nquad)
        self.x=21*(nodes+1)
        self.wx=21*weights
        self.a=1+nodes
        self.wa=weights/2  # R65 corrected isotropic angular average
        self.wn=self.wx*self.x**2/np.expm1(self.x)
        self.cdfs=[]
        self.rates=[]
        self.cond=[]
        for e in self.E:
            cs=sigma_bw(e*1000,T*self.x[:,None],self.a[None,:])
            prob=(self.wn[:,None]*self.a[None,:]*self.wa[None,:]*cs).ravel()
            total=float(np.sum(prob));assert total>0
            self.rates.append(C*(T/HC)**3/math.pi**2*total)
            cdf=np.cumsum(prob/total)
            cdf[-1]=1.
            self.cdfs.append(cdf)
        self.logE=np.log(self.E)
        self.logRates=np.log(self.rates)

    def sample_pair(self, E_GeV, rng):
        E=float(E_GeV)*1e3  # MeV
        l=math.log(E_GeV)
        j=int(np.searchsorted(self.logE,l,side='right'))
        j=max(1,min(j,len(self.E)-1))
        i=j-1;w=min(1.,max(0.,(l-self.logE[i])/(self.logE[j]-self.logE[i])))
        # Conditional quadrature weights are tabulated on the energy grid.
        # A mix of neighboring tables approximates the target distribution.
        # Near the pair threshold a node valid at the adjacent energy may be
        # kinematically closed at E_actual: reject it (never evolve with q>=1).
        for attempt in range(1000):
            node=j if rng.random()<w else i
            cdf=self.cdfs[node]
            index=int(np.searchsorted(cdf,rng.random(),side='left'))
            k,ia=divmod(index,len(self.a))
            eps=float(self.T*self.x[k]);angle=float(self.a[ia])
            q=2*ME*ME/(E*eps*angle)
            if 0<q<1: break
        else:
            raise RuntimeError('no valid Breit-Wheeler target at actual energy')
        beta=math.sqrt(1-q)
        tmax=math.asinh(beta/math.sqrt(q))
        # Rejection with uniform log-endpoint coordinate; efficiency >=~1/2.
        # Explicit transformed kernel avoids under-resolving forward CM peaks.
        for trial in range(1000):
            t=rng.random()*tmax
            z=math.tanh(t)
            sech2=1/math.cosh(t)**2
            f=2-sech2+2*q*max(0,1-q/sech2)
            if rng.random()*(2+2*q)<=f: break
        else:raise RuntimeError('BW angle rejection failure')
        mu=(z/beta)*(1 if rng.random()>.5 else -1)
        # CM boost axis differs from incident hard photon axis; use exact
        # two-photon kinematics and uniform azimuth around hard photon.
        stotal=2*E*eps*angle
        total=E+eps
        P=math.sqrt(max(0,total*total-stotal))
        cosalpha=min(1.,max(-1.,(E-eps)/P))
        sinalpha=math.sqrt(max(0.,1-cosalpha*cosalpha))
        phi=2*math.pi*rng.random()
        muBoost=cosalpha*mu+sinalpha*math.sqrt(max(0.,1-mu*mu))*math.cos(phi)
        B=P/total
        frac=.5*(1+B*beta*muBoost)
        if not 0<=frac<=1:raise AssertionError(('out of range pair fraction',frac))
        return frac

    @staticmethod
    def angular_norm(q):
        beta=math.sqrt(1-q)
        t=math.asinh(beta/math.sqrt(q))
        # Stable F integral; beta term avoids overflow of sinh(t) cosh(t).
        Int=(2+2*q-q*q)*t-beta*(1+q)
        sig=3*SIGMA_T*q/8*Int
        # sigma_bw uses q=1-beta^2, stable L=2log(1+beta)-log(q)
        expected=3*SIGMA_T*q/16*((3-beta**4)*(2*math.log1p(beta)-math.log(q))-2*beta*(2-beta*beta))
        return sig,expected


class BWTables(Tables):
    def __init__(self,nquad=88,ngrid=130,T=TNUC,cut=.1,emax=1e12):
        super().__init__(nquad,ngrid,T,cut,emax)
        self.physical_bw=BWDifferential(self.E,T,nquad)
        assert np.max(np.abs(np.asarray(self.physical_bw.rates)/self.bw-1))<1e-12


def cascade67(tables,E0,kind,split,ntrials,seed,cut=.1,maxevents=700):
    rng=np.random.default_rng(seed)
    durations=np.empty(ntrials)
    ns=np.empty(ntrials,dtype=int)
    nbw=np.empty(ntrials,dtype=int)
    nic=np.empty(ntrials,dtype=int)
    unresolved=0
    for it in range(ntrials):
        E=float(E0);part=kind;tm=0;countBW=countIC=0
        for j in range(maxevents):
            if E<=cut:break
            rate,frac=tables.sample(E,part,rng)
            tm+=rng.exponential()/rate
            if part=='photon':
                countBW+=1
                if split=='exact_bw':z=tables.physical_bw.sample_pair(E,rng)
                elif split=='equal':z=.5
                elif split=='asymmetric':z=.1
                elif split=='beta22':z=rng.beta(2,2)
                else:raise ValueError(split)
                # Energy-biased one-branch lineage; NOT a fully branching
                # cascade. This estimator samples a unit of HARD energy.
                E*=z if rng.random()<z else (1-z)
                part='electron'
            else:
                countIC+=1
                if rng.random()<frac:
                    E*=frac;part='photon'
                else:E*=1-frac
        else:unresolved+=1
        durations[it]=tm
        ns[it]=j
        nbw[it]=countBW
        nic[it]=countIC
    return {'initial_kind':kind,'pair_energy_split':split,'E0_GeV':E0,'Ecut_GeV':cut,
       'ntrials':ntrials,'unresolved':unresolved,
       'mean_s':float(np.mean(durations)),'median_s':float(np.median(durations)),
       'p90_s':float(np.quantile(durations,.90)),'p99_s':float(np.quantile(durations,.99)),
       'frac_over_0p003s':float(np.mean(durations>.003)),'frac_over_0p05s':float(np.mean(durations>.05)),
       'mean_events':float(np.mean(ns)), 'mean_bw':float(np.mean(nbw)),'mean_ic':float(np.mean(nic))}


def main():
    p=argparse.ArgumentParser();p.add_argument('--out',default='.')
    p.add_argument('--quick',action='store_true')
    p.add_argument('--seed',type=int,default=671029)
    p.add_argument('--cut',type=float,default=.1)
    p.add_argument('--nquad',type=int,default=None)
    p.add_argument('--ngrid',type=int,default=None)
    p.add_argument('--ntrials',type=int,default=None)
    args=p.parse_args();out=pathlib.Path(args.out);out.mkdir(parents=True,exist_ok=True)
    n=args.nquad or (66 if args.quick else 112)
    ne=args.ngrid or (94 if args.quick else 150)
    nt=args.ntrials or (150 if args.quick else 1500)
    start=time.perf_counter()
    for q in [1e-2,.1,.25,.5,.75,.99,.9999999,1e-12]:
        s,ref=BWDifferential.angular_norm(q)
        assert abs(s/ref-1)<1e-10,(q,s,ref)
    tab=BWTables(nquad=n,ngrid=ne,cut=args.cut)
    assert np.all(tab.bw>0) and np.all(tab.ic>0)
    stats=[]
    for E0 in [1e3,1e6,1e9,1e12]:
        for kind in ['photon','electron']:
            for split in ['exact_bw','equal','beta22','asymmetric']:
                thisSeed=args.seed+int(math.log10(E0))*100+(['exact_bw','equal','beta22','asymmetric'].index(split))*11+(kind=='electron')
                v=cascade67(tab,E0,kind,split,nt,thisSeed,cut=args.cut)
                stats.append(v)
                print(f'E {E0:.0e} {kind} {split:12s}: med={v["median_s"]:.5g}, p90={v["p90_s"]:.5g}',flush=True)
    filename=out/'IW_DAX_S7_R67_EXACT_BW_VS_R66_PROXIES_20261029.csv'
    with filename.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(stats[0]));writer.writeheader();writer.writerows(stats)
    # Pair fraction check. Use a separate RNG for a reproducible test.
    pairStats=[]
    nP=10000 if args.quick else 30000
    for E0 in [1e3,1e6,1e9,1e12]:
        rng=np.random.default_rng(args.seed+int(math.log10(E0))*23)
        f=np.array([tab.physical_bw.sample_pair(E0,rng) for _ in range(nP)])
        en=f*f+(1-f)*(1-f)
        pairStats.append({'E_GeV':E0,'nsamples':nP,'mean_frac':float(np.mean(f)),
                          'mean_energy_bias_frac':float(np.mean(en)),
                          'quantile_01':float(np.quantile(f,.01)),
                          'quantile_10':float(np.quantile(f,.10)),
                          'quantile_25':float(np.quantile(f,.25)),
                          'quantile_75':float(np.quantile(f,.75)),
                          'quantile_90':float(np.quantile(f,.90)),
                          'quantile_99':float(np.quantile(f,.99))})
    filename=out/'IW_DAX_S7_R67_DIFFERENTIAL_BW_PAIR_FRACTIONS_20261029.csv'
    with filename.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(pairStats[0]));writer.writeheader();writer.writerows(pairStats)
    shape=[]
    for q in np.geomspace(1e-13,.99,17):
        s,ref=BWDifferential.angular_norm(q)
        shape.append({'q_1_minus_beta2':q,'sigma_from_differential_cm2':s,'sigma_total_reference_cm2':ref,'relative_diff':s/ref-1})
    filename=out/'IW_DAX_S7_R67_DIFFERENTIAL_TO_TOTAL_QED_IDENTITY_20261029.csv'
    with filename.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(shape[0]));writer.writeheader();writer.writerows(shape)
    meta={'rotation':67,'status':'QED_DIFFERENTIAL_BW_PASS_BUT_CASCADE_PROXY_NOT_FULL_DEPOSITION',
          'source':'Drebot et al 2017 Phys Rev Accel Beams 20 043402 Eq 1',
          'original_baseline':'DAX-S7 R66 reference kernel and energy-weighted lineage',
          'T_MeV':TNUC,'seed':args.seed,'nquad':n,'ngrid':ne,'ntrials_per_case':nt,
          'n_pair_kinematic_samples_per_energy':nP,'cut_GeV':args.cut,'run_seconds':time.perf_counter()-start,
          'nuclear_status':'No Julia, no BlackHawk, no physical PBH bounds',
          'limitations':['CM Breit-Wheeler exact tree-level unpolarized, isotropic Planck target',
               'Event target quadrature x and 1-cos theta conditional on pair production',
               'Physical pair angle in CM and boost to lab, sampled with uniform azimuth',
               'IC remains ultrarelativistic Jones/Blumenthal-Gould',
               'One randomly energy-weighted branch, not full cascade; no plasma feedback',
               'Neglect tiny target photon energy in hard-injection branch bookkeeping',
               'At 0.1 GeV cutoff branching STOP not thermal heating',
               'No other energy losses, redshift, background evolution, or secondary species'],
          'pair_stats':pairStats,'case_count':len(stats)}
    (out/'IW_DAX_S7_R67_COMPUTATION_MANIFEST_20261029.json').write_text(json.dumps(meta,indent=2),encoding='utf8')
    print('SUCCESS',len(stats),'cases',nP*4,'pair samples',meta['run_seconds'],'seconds')

if __name__=='__main__':main()
