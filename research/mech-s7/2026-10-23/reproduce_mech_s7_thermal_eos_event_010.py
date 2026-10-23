#!/usr/bin/env python3
"""MECH-S7 ROT010 conditional post-evap background swap: source-native 7D
terminal hadron+neutron X states from ROT006/009, a two-temperature ideal
photon+e±+free-streaming massless neutrino thermal EOS; radiation-only
adiabatic post-source T(t), optional comoving baryon conservation.
SOURCE_LIMIT: not source-authorized original 10D runtime, no PBH hadron source below table,
no helium/deuterium/published PBH bound. The micro host is ideal instantaneous-decoupling,
not realistic precision neutrino transport. No new theorem/novelty claimed.
"""
import math, json, csv, hashlib, importlib.util, argparse
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.interpolate import PchipInterpolator
from scipy.integrate import solve_ivp, cumulative_trapezoid

PI=math.pi
M_e=0.51099895000 # MeV
HBAR_GEV_SEC=6.582119569e-25
MPL_GEV=1.220890e19
TNUC=.07818527068831995

def micro_coefficients(T, quad=100):
    """Dimensionless rho/T^4, pressure/T^4, photon+e± and 3 massless neutrinos.
    Photon/e subsystem entropy conserved separately, neutrino Tnu inferred from
    instantaneous relativistic decoupling g_s(em)=5.5 (NOT measured decoupling)."""
    T=np.asarray(T,float)
    z,w=leggauss(quad); z=(z+1)*22.5; w=w*22.5
    e=np.sqrt(z[None,:]**2+(M_e/T[:,None])**2)
    ferm=np.exp(-e)/(1+np.exp(-e)) # exact Fermi-Dirac 1/(exp(e)+1)
    rho_e=4/(2*PI**2)*np.sum(w[None,:]*(z[None,:]**2*e)*ferm,axis=1)
    p_e=4/(6*PI**2)*np.sum(w[None,:]*(z[None,:]**4/e)*ferm,axis=1)
    rho_g=PI**2/15; p_g=rho_g/3
    gsem=45/(2*PI**2)*(rho_e+p_e+rho_g+p_g)
    ratio=(gsem/5.5)**(1/3)
    rho_nu=PI**2/30*5.25*ratio**4
    rho_total=rho_e+rho_g+rho_nu
    p_total=p_e+p_g+rho_nu/3
    return {'gsem':gsem,'grho':rho_total*30/PI**2,'w':p_total/rho_total,'Tnu_over_Tgamma':ratio,'rho_e':rho_e,'p_e':p_e}

def build_micro(Tcut,ntab=1200,quad=120,anchor_H_factor=1.):
    # Pre-tabulate exact ideal integrals on logarithmic grid; avoid any low-T
    # nonrelativistic approximation in electron pressure/enthalpy.
    TL=np.geomspace(.065,.18,ntab)
    D=micro_coefficients(TL,quad)
    lnTL=np.log(TL)
    gs=PchipInterpolator(lnTL,D['gsem'],extrapolate=False)
    rho=PchipInterpolator(lnTL,D['grho'],extrapolate=False)
    w=PchipInterpolator(lnTL,D['w'],extrapolate=False)
    rnu=PchipInterpolator(lnTL,D['Tnu_over_Tgamma'],extrapolate=False)
    # H(T) = sqrt(8*pi/3 / M_pl^2 * rho) ; M_pl is unreduced.
    # 1.660539... sqrt(g_rho) (T/1000 GeV)^2 / M_pl * (1/hbar GeV/s)
    hcoef=1.66053906660*(1/HBAR_GEV_SEC)/MPL_GEV/1e6
    def getH(T):return anchor_H_factor*hcoef*(T*T)*np.sqrt(rho(np.log(T)))
    x=np.linspace(0,math.log(Tcut/TNUC),6000)
    TT=Tcut*np.exp(-x)
    ln= np.log(TT)
    s=gs.derivative()(ln)/gs(ln)
    H=getH(TT)
    dt_dx=(3+s)/(3*H)
    tt=cumulative_trapezoid(dt_dx,x,initial=0)
    Tfun=PchipInterpolator(tt,TT,extrapolate=False)
    return {'T':lambda t, tcut: float(Tfun(min(max(t-tcut,0.),float(tt[-1])))),
            'gs':lambda T:float(gs(math.log(T))),
            'rho':lambda T:float(rho(math.log(T))),
            'w':lambda T:float(w(math.log(T))),
            'rnu':lambda T:float(rnu(math.log(T))),
            'duration':float(tt[-1]),'H_cut':float(getH(Tcut)),
            'max_EOS_derivative':float(np.max(abs(s))),
            'ntab':ntab,'quad':quad}

def load_base(path):
    spec=importlib.util.spec_from_file_location('mech006baseline',str(path)); base=importlib.util.module_from_spec(spec); spec.loader.exec_module(base)
    return base

def prepare(base,public,paper,rtol=3e-9):
    raw=base.load(public,paper)
    ref=raw['public_exec']
    initial_by_map={}
    for mp in ('exec','sym'):
        d=ref.copy()
        chosen=raw['public_exec'] if mp=='exec' else raw['public_sym']
        for key in ['Xn']+[f'n_{sp}_cm3' for sp in base.SPECIES]:d[key]=chosen[key].to_numpy()
        initial_by_map[mp]=d
    fTbase=PchipInterpolator(ref.t_sec.to_numpy(),1000*ref.T_GeV.to_numpy(),extrapolate=False)
    cells={}
    for mp in ('exec','sym'):
        for law in ('public','paper'):
            r=base.simulate(initial_by_map[mp],mp,law,rtol,'archive')
            cells[(mp,law)]=r
    tcut=cells[('exec','public')]['t_cut']; Tcut=float(fTbase(tcut))
    return cells,tcut,Tcut,fTbase

def post_once(base,entry,tcut,Tcut,thermo,mode,method='Radau',rtol=3e-9,conserve=False):
    if mode=='archive':
        Tfun=lambda t:float(thermo['Tbase'](t))
        tend=float(thermo['tend_base'])
    elif mode=='micro':
        Tfun=lambda t: thermo['micro']['T'](t,tcut)
        tend=tcut+thermo['micro']['duration']
    else: raise ValueError(mode)
    y0=np.r_[entry['X_cut'],np.array(entry['cut_populations_cm3'])/base.NSCALE]
    def rhs(t,y):
        temp=Tfun(t)
        baryon_factor=thermo['micro']['gs'](temp)/thermo['micro']['gs'](Tcut) if conserve else 1.
        D,a,b,weak=base.rates(y[0],temp,baryon_scale=baryon_factor)
        conv=np.dot(y[1:],(1-y[0])*a-y[0]*b)*base.NSCALE*base.SIGMA_V_UNIT
        return np.r_[weak+conv,-D*y[1:]]
    sol=solve_ivp(rhs,(tcut,tend),y0,method=method,rtol=rtol,atol=rtol*1e-3,max_step=2)
    if not sol.success:raise RuntimeError(sol.message)
    return {'X_target':float(sol.y[0,-1]),'target_time_s':tend,'T_target':float(Tfun(tend)),
            'nfev':sol.nfev,'steps':len(sol.t), 'nB_ratio_relative_constant_eta':thermo['micro']['gs'](TNUC)/thermo['micro']['gs'](Tcut) if conserve else 1., 'eos_mode':mode,'comoving_baryons':conserve,'rtol':rtol,'method':method}

def main():
    a=argparse.ArgumentParser()
    a.add_argument('--base',default='/mnt/data/mech_s7_rotation_009/source_7d_clock_baryon_stress_009.py')
    a.add_argument('--public',default='/mnt/data/mech_s6_public_2x2_raw.zip')
    a.add_argument('--paper',default='/mnt/data/mech_s6_paper_2x2_raw.zip')
    a.add_argument('--outdir',default='/mnt/data/mech_s7_rotation_010')
    args=a.parse_args()
    out=Path(args.outdir);out.mkdir(exist_ok=True,parents=True)
    base=load_base(Path(args.base));cells,tcut,Tcut,fTbase=prepare(base,args.public,args.paper)
    tvec=base.load(args.public,args.paper)['public_exec'].t_sec.to_numpy()
    idt=np.flatnonzero(1000*base.load(args.public,args.paper)['public_exec'].T_GeV.to_numpy()<TNUC)[0]
    from scipy.optimize import brentq
    tb=float(brentq(lambda t:fTbase(t)-TNUC,float(tvec[idt-1]),float(tvec[idt])))
    micro=build_micro(Tcut)
    thermo={'micro':micro,'Tbase':fTbase,'tend_base':tb}
    Tpoints=[Tcut,.12,.10,TNUC]
    eostable=[]
    for T in Tpoints:
        v=micro_coefficients(np.array([T]))
        eostable.append({'T_MeV':T,'gsem':float(v['gsem'][0]),'grho':float(v['grho'][0]),'w':float(v['w'][0]),'Tnu_to_Tgamma':float(v['Tnu_over_Tgamma'][0])})
    combos=[('archive',False),('archive',True),('micro',False),('micro',True)]
    data=[]
    for mode,conserve in combos:
      for mp in ('exec','sym'):
        row={'eos_mode':mode,'comoving_baryons':conserve,'map':mp}
        for law in ('public','paper'):
          k=post_once(base,cells[(mp,law)],tcut,Tcut,thermo,mode,conserve=conserve)
          row['X_'+law]=k['X_target'];row['t_target_s']=k['target_time_s'];row['T_target']=k['T_target'];row['nB_ratio_vs_const_eta']=k['nB_ratio_relative_constant_eta'];row['nfev_'+law]=k['nfev'];row['steps_'+law]=k['steps']
        row['deltaX']=row['X_paper']-row['X_public'];data.append(row)
        print(f'{mode:8s} nBcons={conserve} {mp:4s} deltaX={row["deltaX"]:+.12e} Xpub={row["X_public"]:.9f} tTarget={row["t_target_s"]:.4f}',flush=True)
    # split factorial effects of thermal host and conserved nB for the fixed map.
    facts=[]
    for mp in ('exec','sym'):
        v={(r['eos_mode'],r['comoving_baryons']):r['deltaX'] for r in data if r['map']==mp}
        inter=v['micro',True]-v['micro',False]-v['archive',True]+v['archive',False]
        facts.append({'map':mp,'nominal':v['archive',False], 'thermal_at_const_eta':v['micro',False]-v['archive',False], 'nB_at_archive':v['archive',True]-v['archive',False], 'mixed_interaction':inter,'full_micro_cons':v['micro',True]})
    # test refinement of EOS quadrature and thermal table (not full ODE error certificate)
    refinements=[]
    for ntab,quad in [(300,80),(600,100),(1200,120),(2400,160)]:
        m=build_micro(Tcut,ntab,quad)
        refinements.append({'ntab':ntab,'quad':quad,'target_duration_s':m['duration'],'gsem_nuc':m['gs'](TNUC),'Tnu_over_Tgamma_0p1':m['rnu'](.1)})
    manifest={'description':'Conditional Mech-S7 ROT010 thermodynamic host replacement post PBH source cutoff only; archived 7D terminal states, source spectra UNVALIDATED below 1e9g.',
        'upstream_repo':'Fenyutanchan/Primordial-Black-Hole','upstream_commit':base.UPSTREAM,
        'original_archive_sha256':{'public':base.PUB,'paper':base.PAP},
        'source_eos':'ideal thermal Fermi-Dirac electrons/positrons + photons + separately cooled 3 massless neutrinos; instantaneous relativistic decoupling at g_s,em=5.5',
        'cross_cell_credit':'DAX-S7 ROT34-39 initial source cooling anomaly; PRF11 R21/R22 thermal table and micro reconstruction; MECH 7D earlier ROT006-009','limits':['postsource change only','source-active 7D same archived T(t)','constant eta and conserved baryons modelled alternatives','no 10D original Julia','no physical BBN/Yp/DH/PBH bound']}
    with open(out/'thermal_eos_2x2_010.csv','w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(data[0]));writer.writeheader();writer.writerows(data)
    with open(out/'thermal_eos_factored_010.csv','w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(facts[0]));writer.writeheader();writer.writerows(facts)
    (out/'thermal_eos_010.json').write_text(json.dumps({'manifest':manifest,'t_cut':tcut,'T_cut_MeV':Tcut,'baseline_tnuc':tb,'micro_tnuc':tcut+micro['duration'],'eos_table':eostable,'results':data,'factorial':facts,'thermal_grid_controls':refinements},indent=2))
    print('THERMAL_REFINEMENT',refinements)
    print('FACTORS',facts)

if __name__=='__main__':main()