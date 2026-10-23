#!/usr/bin/env python3
"""MECH-S7 ROT011. Event-anchored, conditional, source-ACTIVE two-temperature
ideal gas background (photons, e+- thermal equilibrium; separately tracked
3 neutrino species). PBH energy Q= -n_PBH dM/dt allocated χ to EM and 1-χ to
an EFFECTIVE fully thermalized neutrino bath, just a stress carrier.
Mass is exact: M^3=M_edge^3-Γ(t-t_edge). Initial edge state inherited from
archived source-native 7D executor, not a corrected 10D prehistory.
Compares nB(T)=eta n_gamma with comoving nB anchored at M=1e9g.
Not source-valid emission below 1e9g, not full Wu-Xu Julia 10D, no physical
BBN helium/deuterium/constraint. ν deposition χ is NOT source specified.
"""
import argparse, csv, importlib.util, json, math, hashlib, sys
from pathlib import Path
from scipy.integrate import solve_ivp, cumulative_trapezoid
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq
import numpy as np

PI=math.pi
G_CGS=6.67430e-8
C_CGS=2.99792458e10
A_RAD=7.5657e-15
K_PER_MEV=1.160451812e10
PHOTON_RHOC=(PI*PI/15)
HBAR_GEV_SEC=6.582119569e-25
TNUC=.07818527068831995
# numerically independently computed neutrino mass equivalent rho in photons units
# at temperature T_nu: coefficient ratio (7/8)*3=2.625, yes photon 2 d.o.f. ν effective =5.25 vs 2.
NU_TO_GAMMA=5.25/2


def module(path):
    spec=importlib.util.spec_from_file_location('mech_base_011',str(path))
    b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b);return b

def eos_table(tmax=.18, tmin=.073, n=1600, quad=130):
    """Use independently evaluated ideal gas from ROT010, including derivative."""
    root=Path(__file__).parents[1]/'mech_s7_rotation_010'/'reproduce_mech_s7_thermal_eos_event_010.py'
    if not root.is_file(): root=Path('/mnt/data/mech_s7_rotation_010/reproduce_mech_s7_thermal_eos_event_010.py')
    m=module(root)
    temps=np.geomspace(tmin,tmax,n)
    z,w=np.polynomial.legendre.leggauss(quad);z=(z+1)*22.5;w=w*22.5
    e=np.sqrt(z[None,:]**2+(m.M_e/temps[:,None])**2)
    ferm=np.exp(-e)/(1+np.exp(-e))
    rho_e=4/(2*PI**2)*np.sum(w[None,:]*z[None,:]**2*e*ferm,axis=1)
    p_e=4/(6*PI**2)*np.sum(w[None,:]*z[None,:]**4/e*ferm,axis=1)
    em_rho=rho_e+PI*PI/15
    em_p=p_e+PI*PI/45
    gs=45/(2*PI**2)*(em_rho+em_p)
    lr=np.log(temps)
    rem=PchipInterpolator(lr,em_rho)
    pem=PchipInterpolator(lr,em_p)
    gsint=PchipInterpolator(lr,gs)
    photonref=A_RAD*(K_PER_MEV**4)/C_CGS**2 # mass equiv at 1 MeV in g/cm3
    unit=photonref/PHOTON_RHOC
    return {'rho':lambda t:unit*t**4*float(rem(math.log(t))),'P':lambda t:unit*t**4*float(pem(math.log(t))),
            'd_rho_dT':lambda t:unit*t**3*(4*float(rem(math.log(t)))+float(rem.derivative()(math.log(t)))),
            'gs':lambda t:float(gsint(math.log(t))),
            's':lambda t:float(gsint.derivative()(math.log(t)))/float(gsint(math.log(t))),
            'neutrino_rho':lambda t:photonref*NU_TO_GAMMA*t**4,
            'Tnu_from_rho':lambda r:(r/(photonref*NU_TO_GAMMA))**.25,
            'range':[tmin,tmax],'em_ref_gcm3':unit,'quad':quad,'table_points':n}

def contexts(base, pub, pap):
    raw=base.load(pub,pap)
    ref=raw['public_exec']
    ts=ref.t_sec.to_numpy();T=1000*ref.T_GeV.to_numpy();a=ref.a.to_numpy()
    t0=float(ts[0]);mass0=float(ref.m_PBH_g.iloc[0]);tedge=t0+(mass0**3-base.M_EDGE**3)/base.GAMMA
    tc=tedge+(base.M_EDGE**3-base.M_CUT**3)/base.GAMMA
    fT=PchipInterpolator(ts,T);fa=PchipInterpolator(ts,np.log(a));fn=PchipInterpolator(ts,np.log(ref.n_PBH_cm3.to_numpy()+1e-300))
    Tedge=float(fT(tedge));aedge=math.exp(float(fa(tedge)))
    i=1469; nedge=float(ref.n_PBH_cm3.iloc[i])*math.exp(-3*(float(fa(tedge))-math.log(float(a[i]))))
    mp={}
    for name in ['exec','sym']:
        d=ref.copy();r=raw['public_exec'] if name=='exec' else raw['public_sym']
        for key in ['Xn']+[f'n_{sp}_cm3' for sp in base.SPECIES]: d[key]=r[key].to_numpy()
        mp[name]=d
    return {'ref':ref,'fT':fT,'fa':fa,'tedge':tedge,'tcut':tc,'Tedge':Tedge,'aedge':aedge,'nedge':nedge,'maps':mp,
            'nPBH_mass_edge_gcm3':nedge*base.M_EDGE}

def prepare_host(base, ctx, eos, chi=1., rtol=2e-10):
    assert 0<=chi<=1
    T0=ctx['Tedge']; nPBH0=ctx['nedge']; rho_em0=eos['rho'](T0)
    Tnu0=T0*(eos['gs'](T0)/5.5)**(1/3)
    rnu0=eos['neutrino_rho'](Tnu0)
    dt=base.DT_EDGE; m0=base.M_EDGE
    def fields(u,y):
        T,lr,lnrnu=y
        nPBH=nPBH0*math.exp(-3*lr)
        rnu=math.exp(lnrnu)
        rpbh=nPBH*m0*u
        rem=eos['rho'](T); pem=eos['P'](T)
        H=math.sqrt(8*PI*G_CGS/3*(rem+rnu+rpbh))
        dudt=-1/(3*dt*u*u)
        Q=nPBH*m0*(-dudt) # mass-energy equivalent g/cm3/s
        return H,rem,pem,rnu,rpbh,Q,nPBH
    def rhs(u,y):
        T,lr,lnrnu=y
        H,rem,pem,rnu,rpbh,Q,nPBH=fields(u,y)
        dtdu=-3*dt*u*u
        dTemdt=(-3*H*(rem+pem)+chi*Q)/eos['d_rho_dT'](T)
        drnu_dt=(-4*H*rnu+(1-chi)*Q)
        return np.array([dTemdt*dtdu,H*dtdu,drnu_dt/rnu*dtdu])
    U=float(base.U_CUT)
    sol=solve_ivp(rhs,(1.,U),[T0,0.,math.log(rnu0)],method='DOP853',rtol=rtol,atol=[1e-13,1e-12,1e-12],dense_output=True,max_step=.004)
    if not sol.success:raise RuntimeError('Host: '+sol.message)
    Ts=sol.y[0];lnas=sol.y[1]; rnu=np.exp(sol.y[2]);us=sol.t
    if min(Ts)<eos['range'][0] or max(Ts)>eos['range'][1]:raise RuntimeError('EOS host outside table range')
    # Event-integrated conservation (mass equivalent energy plus pressure)
    # geometric average dt integral, no assumption of adiabaticity for injected EM.
    uu=np.linspace(1,U,1200)
    TT,logA,lnrn=sol.sol(uu)
    rpb=nPBH0*np.exp(-3*logA)*m0*uu
    rem=np.array([eos['rho'](float(x)) for x in TT]);p_em=np.array([eos['P'](float(x)) for x in TT]);rv=np.exp(lnrn)
    H=np.sqrt(8*PI*G_CGS/3*(rem+rv+rpb))
    denergy_du=-(3*H*(rem+p_em+4*rv/3+rpb))*(-3*dt*uu*uu)
    # Check full total derivative including source-via-mass: should equal sum dE/du.
    cons=(rem[-1]+rv[-1]+rpb[-1])-(rem[0]+rv[0]+rpb[0]) - float(np.trapezoid(denergy_du,uu))
    rel_cons=cons/max(1,rem[0]+rv[0]+rpb[0])
    Tcut=float(sol.y[0,-1]); lr_cut=float(sol.y[1,-1]);rnu_cut=math.exp(float(sol.y[2,-1]))
    # Adiabatic photons+e, neutrino scaling after source off; do not re-assume Tnu(T) from ultrarelativistic anchor.
    x=np.linspace(0,math.log(Tcut/TNUC),6500)
    temp=Tcut*np.exp(-x)
    gs0=eos['gs'](Tcut)
    gs=np.array([eos['gs'](float(z)) for z in temp])
    loga=lr_cut+x+np.log(gs0/gs)/3
    rnuc=rnu_cut*np.exp(-4*(loga-lr_cut))
    rp=np.array([eos['rho'](float(z)) for z in temp]); HH=np.sqrt(8*PI*G_CGS/3*(rp+rnuc))
    s=np.array([eos['s'](float(z)) for z in temp]);dt_dx=(3+s)/(3*HH)
    time_after=cumulative_trapezoid(dt_dx,x,initial=0.)
    tp=ctx['tcut']+time_after
    T_post=PchipInterpolator(tp,temp,extrapolate=False)
    a_post=PchipInterpolator(tp,loga,extrapolate=False)
    return {'chi':chi,'u_sol':sol,'pre_T':lambda u:float(sol.sol(float(u))[0]),
            'pre_lna':lambda u:float(sol.sol(float(u))[1]),
            'Tcut':Tcut,'Tnuc_time':float(tp[-1]),'lna_cut':lr_cut,'rho_nu_cut':rnu_cut,
            'post_T':lambda t:float(T_post(min(max(t,float(tp[0])),float(tp[-1])))),
            'post_lna':lambda t:float(a_post(min(max(t,float(tp[0])),float(tp[-1])))),
            'cons_integral_mass_residual_gcm3':float(cons),'cons_integral_relative':float(rel_cons),
            'PBH_to_radiation_at_edge':ctx['nPBH_mass_edge_gcm3']/(rho_em0+rnu0),
            'rho_em_edge':rho_em0,'rho_nu_edge':rnu0,'rho_PBH_edge':ctx['nPBH_mass_edge_gcm3'],
            'rho_em_cut':eos['rho'](Tcut),'rho_nu_cut':rnu_cut,
            'post_em_entropy_ratio_final':float(gs[-1]*TNUC**3*math.exp(3*(loga[-1]-lr_cut))/(gs0*Tcut**3)),
            'cut_effective_nu_ratio':eos['Tnu_from_rho'](rnu_cut)/Tcut,
            'solver_nfev':sol.nfev,'solver_steps':len(sol.t)}

def evolve(base,ctx,eos,host,mapname,law,conserve=False,rtol=3e-8,method='Radau'):
    df=ctx['maps'][mapname]
    x0=float(df.Xn.iloc[1469]); n0=np.array([float(df[f'n_{sp}_cm3'].iloc[1469]) for sp in base.SPECIES])/base.NSCALE
    y0=np.r_[x0,n0]
    factors=np.ones(6) if mapname=='exec' else np.array([.5,.5,.5,1,.5,.5])
    slopes=base.SLOPES[base.INDEX] if law=='public' else np.full(6,-1.3)
    q1=base.Q1[base.INDEX];M0=base.M_EDGE
    tE=ctx['Tedge']
    def baryon_factor(T,lr):
        return (tE/T)**3*math.exp(-3*lr) if conserve else 1.
    def collision(t,y,T,lr):
        X=y[0];ns=y[1:]
        D,aa,bb,weak=base.rates(X,T,baryon_scale=baryon_factor(T,lr))
        conv=np.sum(ns*base.NSCALE*base.SIGMA_V_UNIT*((1-X)*aa-X*bb))
        return weak+conv,D
    def rhs_mass(u,y):
        T=host['pre_T'](u);lna=host['pre_lna'](u)
        f,D=collision(None,y,T,lna)
        nPBH=ctx['nedge']*math.exp(-3*lna)
        source=q1*factors*nPBH/HBAR_GEV_SEC*u**slopes/base.NSCALE
        return -3*base.DT_EDGE*u*u*np.r_[f,source-D*y[1:]]
    pre=solve_ivp(rhs_mass,(1.,base.U_CUT),y0,method=method,rtol=rtol,atol=rtol*1e-3,max_step=.01)
    if not pre.success: raise RuntimeError('7D pre '+pre.message)
    ycut=pre.y[:,-1]
    def rhs_post(t,y):
        T=host['post_T'](t);lna=host['post_lna'](t)
        f,D=collision(t,y,T,lna)
        return np.r_[f,-D*y[1:]]
    post=solve_ivp(rhs_post,(ctx['tcut'],host['Tnuc_time']),ycut,method=method,rtol=rtol,atol=rtol*1e-3,max_step=2.)
    if not post.success:raise RuntimeError('7D post '+post.message)
    return {'map':mapname,'law':law,'chi':host['chi'],'baryon_prescription':'comoving-from-edge' if conserve else 'eta-constant',
            'Xedge':float(y0[0]),'Xcut':float(ycut[0]),'X_nuc':float(post.y[0,-1]),
            'nfev_active':pre.nfev,'nfev_post':post.nfev,'nstep_active':len(pre.t),'nstep_post':len(post.t),
            'max_pre_X':float(max(pre.y[0])),'min_pre_X':float(min(pre.y[0]))}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--base',default='/mnt/data/mech_s7_rotation_009/source_7d_clock_baryon_stress_009.py')
    p.add_argument('--pub',default='/mnt/data/mech_s7_rotation_010/mech_s6_public_2x2_raw.zip')
    p.add_argument('--pap',default='/mnt/data/mech_s7_rotation_010/mech_s6_paper_2x2_raw.zip')
    p.add_argument('--out',default='/mnt/data/mech_s7_rotation_011')
    p.add_argument('--rtol',type=float,default=3e-8)
    p.add_argument('--host-rtol',type=float,default=2e-10)
    p.add_argument('--chis',default='0,0.5,1')
    a=p.parse_args();out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    base=module(Path(a.base));ctx=contexts(base,a.pub,a.pap);eos=eos_table()
    print('EDGE',ctx['tedge'],ctx['tcut'],ctx['Tedge'],ctx['nedge'],'sourcePBH_rho',ctx['nPBH_mass_edge_gcm3'],flush=True)
    hosts=[prepare_host(base,ctx,eos,float(z),a.host_rtol) for z in a.chis.split(',')]
    cases=[];hr=[]
    for host in hosts:
        hr.append({k:val for k,val in host.items() if not callable(val) and k!='u_sol'})
        print('HOST',host['chi'],'Tcut',host['Tcut'],'nuc_t',host['Tnuc_time'],'energy_rel_resid',host['cons_integral_relative'],flush=True)
        for conserve in (False,True):
            for mp in ('exec','sym'):
                runs=[]
                for law in ('public','paper'):
                    r=evolve(base,ctx,eos,host,mp,law,conserve,a.rtol)
                    cases.append(r);runs.append(r)
                print('CELL',host['chi'],conserve,mp,'deltaX',runs[1]['X_nuc']-runs[0]['X_nuc'],'Xpublic',runs[0]['X_nuc'],flush=True)
    rows=[]
    for host in hosts:
        for conserve in (False,True):
            for mp in ('exec','sym'):
                p0=next(z for z in cases if z['chi']==host['chi'] and z['baryon_prescription']==('comoving-from-edge' if conserve else 'eta-constant') and z['map']==mp and z['law']=='public')
                p1=next(z for z in cases if z['chi']==host['chi'] and z['baryon_prescription']==('comoving-from-edge' if conserve else 'eta-constant') and z['map']==mp and z['law']=='paper')
                rows.append({'chi_EM':host['chi'],'conserved_baryons':conserve,'map':mp,'deltaX_target':p1['X_nuc']-p0['X_nuc'], 'X_public':p0['X_nuc'],'X_paper':p1['X_nuc'],'X_cut_public':p0['Xcut'],'X_cut_paper':p1['Xcut'],'T_cut_MeV':host['Tcut'],'t_nuc_s':host['Tnuc_time'],'rhoPBH_edge_over_rhorad':host['PBH_to_radiation_at_edge']})
    with (out/'active_micro_2x2_011.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    (out/'active_micro_011.json').write_text(json.dumps({'upstream_commit':base.UPSTREAM,'source_hash_public':base.PUB,'source_hash_paper':base.PAP,
         'provenance_and_limits':'Full old 10D from t_formation to 1e9g NOT repeated; archived 7D edge states reused and mass exact on subedge, all hadron spectra extrap below 1e9g NOT physically supported. χ fraction is intentional conditional source-independent stress; neutrino heating modeled thermal, physical license absent.',
         'eos_ideal':'separately T_gamma,Tnu, Fermi-Dirac e+- pressure, instantaneous early ν decoupling, cgs Friedmann sourced by radiation and PBH mass',
         'source_migration':'exact source-on rho injection from PBH mass loss and nPBH dilution; valid only for assumed thermalisation channel',
         'edge':{k:v for k,v in ctx.items() if k in ('tedge','tcut','Tedge','aedge','nedge','nPBH_mass_edge_gcm3')},
         'hosts':hr,'cells':cases,'comparisons':rows},indent=2))
    print('TOTAL_CELLS',len(cases))
if __name__=='__main__':main()