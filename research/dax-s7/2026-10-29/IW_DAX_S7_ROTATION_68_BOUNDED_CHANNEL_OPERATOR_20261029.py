#!/usr/bin/env python3
"""DAX-S7 R68: bounded BW+DPP+muon gamma operators, with TPP diagnostics.

R67 single-pair Breit-Wheeler and Jones/Blumenthal-Gould inverse Compton
kernels are reused unchanged (including isotropic 1/2 angular factor).
Additional gamma-gamma -> e+e-e+e- channel uses ONLY published high-s
TOTAL cross section (asymptote), NOT an exact four-lepton differential law.
DPP final-state energy allocations are explicitly synthetic Dirichlet or
leading-spectator uncertainty controls. Gamma-gamma -> mu+mu- uses full
Breit-Wheeler total cross section with m_e replaced by m_mu; a muon event
is recorded as an UNRESOLVED branch, not as fully deposited neutrino energy.
The TPP electron+photon -> e+e+e- is inspected via high-s TOTAL cross
section, and *not* treated as an electron energy-loss kernel.

One energy-biased lineage is NOT a complete cascade, below-cut energy is
NOT thermal energy, and NO physical f_EM or PBH bound is inferred.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, math, pathlib, subprocess, sys
from functools import lru_cache
import numpy as np
from scipy.special import roots_legendre

HERE=pathlib.Path(__file__).resolve().parent
DEFAULT_R67=HERE.parent/'dax67'/'IW_DAX_S7_ROTATION_67_EXACT_DIFFERENTIAL_BW_CASCADE_20261029.py'
# The frozen R67 code is bundled alongside this R68 script in releases.
FROZEN_R67=HERE/'R67_FROZEN_EXACT_DIFFERENTIAL_BW_CASCADE_20261029.py'
REF=FROZEN_R67 if FROZEN_R67.exists() else DEFAULT_R67
import importlib.util
spec=importlib.util.spec_from_file_location('dax67_68',REF)
r67=importlib.util.module_from_spec(spec)
spec.loader.exec_module(r67)
C=r67.C; HC=r67.HC; ME=r67.ME; SIGMA_T=r67.SIGMA_T; TNUC=r67.TNUC
ALPHA=1/137.035999084
MMU=105.6583755
ZETA3=1.202056903159594
SIGMA_DPP_ASYMPTOTIC=(ALPHA**4/(36*math.pi)*(175*ZETA3-38)*(HC/ME)**2)
SIGMA_ELECTRON_TPP_PREF=ALPHA*(3*SIGMA_T/(8*math.pi)) # alpha * r_e^2


def sigma_lepton_pair(E_mev,eps,a,m_lepton):
    """Unpolarized two-photon Breit-Wheeler total cross section, in cm^2."""
    E=np.asarray(E_mev)
    with np.errstate(divide='ignore',invalid='ignore',over='ignore'):
        u=2*m_lepton**2/(E*eps*a)
        valid=(u>0)&(u<1)
        q=np.where(valid,u,1.)
        beta=np.sqrt(1-q)
        L=2*np.log1p(beta)-np.log(q)
        s=(3/16)*SIGMA_T*(ME/m_lepton)**2*q*((3-(1-q)**2)*L-2*beta*(1+q))
    return np.where(valid,np.maximum(s,0),0)


class PhotonicRates:
    def __init__(self,nquad=112,T=TNUC):
        self.nquad=nquad;self.T=T
        a,wa=roots_legendre(nquad);x,wx=roots_legendre(nquad)
        self.a=a+1;self.wa=wa/2
        self.x=(x+1)*21.;self.wx=wx*21.
        self.wph=self.wx*self.x**2/np.expm1(self.x)
        self.pref=C*(T/HC)**3/math.pi**2
        self.ndensity=2*ZETA3/math.pi**2*(T/HC)**3
        self.rate_dpp=C*self.ndensity*SIGMA_DPP_ASYMPTOTIC
    def lepton(self,E_GeV,lepton_mass):
        E=E_GeV*1000
        ss=sigma_lepton_pair(E,self.T*self.x[:,None],self.a[None,:],lepton_mass)
        return self.pref*float(np.dot(self.wph,ss@(self.a*self.wa)))
    def tpp_asymptotic_event(self,E_GeV):
        # electron+blackbody-photon high-s asymptotic approximation.
        # k=E_e*eps*(1-cos theta)/me^2. Rate is ONLY meaningful if
        # log branch valid, k≫10^4; this is not a kinetic energy LOSS rate.
        if E_GeV<100:
            # Below this point an increasingly tiny Wien-tail slice of the
            # bath meets k>1e4: the high-s approximation is not a useful
            # physical model for the full thermal event rate.
            return math.nan
        k=E_GeV*1000*self.T*self.x[:,None]*self.a[None,:]/ME**2
        term=(28/9)*np.log(np.maximum(2*k,1e-300))-218/27
        sig=np.where(k>1e4,np.maximum(term,0)*SIGMA_ELECTRON_TPP_PREF,0.)
        total=self.pref*float(np.dot(self.wph,sig@(self.a*self.wa)))
        return total


def draw_four_fractions(rng,kernel):
    if kernel=='equal4': return np.full(4,.25)
    if kernel=='dirichlet_a0p15':return rng.dirichlet([.15]*4)
    if kernel=='dirichlet_a1':return rng.dirichlet([1]*4)
    if kernel=='dirichlet_a4':return rng.dirichlet([4]*4)
    if kernel=='leading95':
        # Deterministic 95/5 leading + three 1.67% spectators; random order.
        f=np.array([.95,.05/3,.05/3,.05/3]);rng.shuffle(f);return f
    raise ValueError(kernel)


def second_moment_analytic(kernel):
    if kernel=='equal4':return .25
    if kernel=='leading95':return .95**2+(.05**2)/3
    al={'dirichlet_a0p15':.15,'dirichlet_a1':1,'dirichlet_a4':4}.get(kernel)
    return (al+1)/(4*al+1)


class JointTable:
    def __init__(self,nquad=80,ngrid=130,cut=.1,emax=1e12):
        self.original=r67.BWTables(nquad=nquad,ngrid=ngrid,cut=cut,emax=emax)
        self.rate=PhotonicRates(nquad)
        self.mu=np.array([self.rate.lepton(E,MMU) for E in self.original.E])
        self.logE=self.original.logE
        self.cut=cut
    def mu_rate(self,E):
        le=math.log(E)
        return float(np.interp(le,self.logE,self.mu)) if E<=self.original.E[-1] else float(self.mu[-1])
    def gamma_rates(self,E):
        bw,_=self.original.sample(E,'photon',np.random.default_rng(0))
        return bw,self.rate.rate_dpp,self.mu_rate(E)


def lineage(table,E0,kernel,seed,ntrials,enable_dpp=True,enable_mu=True,cut=.1,maxevents=1200):
    rng=np.random.default_rng(seed)
    records=[]
    for j in range(ntrials):
        E=float(E0);part='photon'; t=0.;nbw=ndpp=nmu=nic=0;event_count=0
        flag='unresolved_limit'
        while event_count <maxevents:
            if E<=cut:
                flag='below_cut_not_deposition';break
            event_count+=1
            if part=='photon':
                bw,_=table.original.sample(E,'photon',rng)
                dpp=table.rate.rate_dpp if enable_dpp else 0.
                mu=table.mu_rate(E) if enable_mu else 0.
                rate=bw+dpp+mu
                t+=rng.exponential()/rate
                draw=rng.random()*rate
                if draw<bw:
                    nbw+=1
                    f=table.original.physical_bw.sample_pair(E,rng)
                    E*=f if rng.random()<f else 1-f
                    part='electron'
                elif draw<bw+dpp:
                    ndpp+=1
                    fractions=draw_four_fractions(rng,kernel)
                    assert np.isclose(sum(fractions),1.,rtol=1e-13)
                    idx=rng.choice(4,p=fractions)
                    E*=fractions[idx]
                    part='electron'
                else:
                    nmu+=1
                    flag='muon_opportunity_not_neutrino_deposition'
                    break
            else:
                ic,f=table.original.sample(E,'electron',rng)
                if ic<=0: raise ValueError('nonpositive IC')
                t+=rng.exponential()/ic
                nic+=1
                if rng.random()<f:
                    E*=f;part='photon'
                else:
                    E*=1-f
        records.append((t,flag,nbw,ndpp,nmu,nic,event_count,E))
    a=np.array([v[0] for v in records])
    flags=[v[1] for v in records]
    cols=np.array([[v[i] for v in records] for i in (2,3,4,5,6,7)],dtype=float)
    return {
        'E0_GeV':E0,'ntrials':ntrials,'dpp_kernel':kernel,'enable_dpp':int(enable_dpp),
        'enable_muon':int(enable_mu),'n_unresolved':sum(v=='unresolved_limit' for v in flags),
        'energy_biased_muon_opportunity_fraction':flags.count('muon_opportunity_not_neutrino_deposition')/ntrials,
        'energy_biased_below_cut_fraction':flags.count('below_cut_not_deposition')/ntrials,
        'median_exit_s':float(np.median(a)), 'p90_exit_s':float(np.quantile(a,.9)),
        'median_exit_s_given_below_cut':float(np.median(a[np.array(flags)=='below_cut_not_deposition'])) if flags.count('below_cut_not_deposition') else math.nan,
        'frac_exit_time_over_0p003_s':float(np.mean(a>.003)),
        'frac_exit_time_over_0p05_s':float(np.mean(a>.05)),
        'mean_bw_events':float(np.mean(cols[0])), 'mean_dpp_events':float(np.mean(cols[1])),
        'mean_muon_events':float(np.mean(cols[2])), 'mean_ic_events':float(np.mean(cols[3])),
        'mean_total_events':float(np.mean(cols[4])),
        'dpp_f2_theoretical':second_moment_analytic(kernel),
    }


def write_rows(file,rows):
    with file.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]))
        w.writeheader();w.writerows(rows)


def selftest():
    assert abs(SIGMA_DPP_ASYMPTOTIC/6.444337088351144e-30-1)<1e-12
    for kernel in ['equal4','dirichlet_a0p15','dirichlet_a1','dirichlet_a4','leading95']:
        rng=np.random.default_rng(42)
        v=np.array([draw_four_fractions(rng,kernel) for _ in range(20000)])
        assert np.all(v>=0) and np.max(np.abs(v.sum(axis=1)-1))<1e-14
        measured=np.mean((v*v).sum(axis=1))
        assert abs(measured-second_moment_analytic(kernel))<.008,(kernel,measured,second_moment_analytic(kernel))
    for ml in [ME,MMU]:
        E=1e7
        r=PhotonicRates(112).lepton(E,ml)
        assert r>0 and np.isfinite(r)
    assert PhotonicRates(112).lepton(1,MMU)<1e-3
    print('SELFTEST PASS')


def main():
    pa=argparse.ArgumentParser()
    pa.add_argument('--out',type=pathlib.Path,default=HERE)
    pa.add_argument('--nquad',type=int,default=88)
    pa.add_argument('--ngrid',type=int,default=130)
    pa.add_argument('--ntrials',type=int,default=600)
    pa.add_argument('--seed',type=int,default=681029)
    pa.add_argument('--quick',action='store_true')
    pa.add_argument('--selftest',action='store_true')
    args=pa.parse_args()
    selftest()
    if args.selftest:return
    args.out.mkdir(parents=True,exist_ok=True)
    if args.quick:args.nquad=54;args.ngrid=85;args.ntrials=150
    Q=PhotonicRates(args.nquad)
    # Separate lepton rate × quadrature convergence.
    pcon=[]
    for E in [1,10,100,1000,2240,1e4,1e6,1e9,1e12]:
        vals=[]
        for n in [max(64,args.nquad//2),args.nquad,max(136,args.nquad*2)]:
            q=PhotonicRates(n)
            vals.append((q.lepton(E,ME),q.lepton(E,MMU),q.rate_dpp,q.tpp_asymptotic_event(E)))
        bw,mu,dpp,tpp=vals[-1]
        pcon.append({'E_GeV':E,'BW_rate_s_inv':bw,'DPP_rate_asymptotic_s_inv':dpp,
                     'muon_pair_rate_s_inv':mu, 'muon_fraction_of_gamma3_channel_events':mu/(bw+dpp+mu),
                     'DPP_fraction_of_gamma3_channel_events':dpp/(bw+dpp+mu),
                     'TPP_event_rate_asymptotic_s_inv_for_electron':tpp,
                     'max_rel_spread_BW_grid':(max(v[0] for v in vals)-min(v[0] for v in vals))/bw,
                     'max_rel_spread_muon_grid':((max(v[1] for v in vals)-min(v[1] for v in vals))/mu) if mu else 0.0,
                     'max_rel_spread_TPP_grid':((max(v[3] for v in vals)-min(v[3] for v in vals))/tpp) if np.isfinite(tpp) and tpp>0 else math.nan})
    write_rows(args.out/'IW_DAX_S7_R68_CHANNEL_RATE_HIERARCHY_20261029.csv',pcon)
    tab=JointTable(args.nquad,args.ngrid)
    runs=[]
    for E in [1e3,1e6,1e9,1e12]:
        for k in ['equal4','dirichlet_a0p15','dirichlet_a1','dirichlet_a4','leading95']:
            v=lineage(tab,E,k,args.seed+int(math.log10(E))*87+['equal4','dirichlet_a0p15','dirichlet_a1','dirichlet_a4','leading95'].index(k)*300,
                      args.ntrials,True,True)
            runs.append(v)
            print('E',E,'kernel',k,'pMuon',v['energy_biased_muon_opportunity_fraction'],'medExit',v['median_exit_s'],'p90',v['p90_exit_s'],flush=True)
        for dpp,mu,k in [(0,0,'equal4'),(1,0,'dirichlet_a1'),(0,1,'equal4')]:
            v=lineage(tab,E,k,args.seed+int(math.log10(E))*87+900+100*dpp+10*mu,args.ntrials,bool(dpp),bool(mu))
            runs.append(v)
    write_rows(args.out/'IW_DAX_S7_R68_BOUNDED_DPP_MUON_LINEAGE_MATRIX_20261029.csv',runs)
    # Independent conditional probabilities of DPP 4-lepton energy-biased branch.
    m=[]
    for k in ['equal4','dirichlet_a0p15','dirichlet_a1','dirichlet_a4','leading95']:
        rng=np.random.default_rng(33129)
        vs=np.array([draw_four_fractions(rng,k) for _ in range(20000)])
        m.append({'kernel':k,'sum_fraction_max_abs_err':float(np.max(np.abs(vs.sum(axis=1)-1))),
                  'event_mean_sum_squared_energy_fractions':float(np.mean(np.sum(vs*vs,axis=1))),
                  'theoretical_mean_sum_squared_energy_fractions':second_moment_analytic(k),
                  'absolute_difference':float(abs(np.mean(np.sum(vs*vs,axis=1))-second_moment_analytic(k)))})
    write_rows(args.out/'IW_DAX_S7_R68_DPP_FOUR_LEPTON_FRACTION_CONTROLS_20261029.csv',m)
    print('SUCCESS',len(pcon),'rate rows',len(runs),'runs')

if __name__=='__main__':main()
