#!/usr/bin/env python3
"""Mech-S7 rotation 006: independent 7D (X plus six hadron densities)
conditional last-table-edge-to-cutoff and postsource replay, exactly controlled
M^3(t), source-native Wu-Xu 6-channel collision rates, 2x2 variants.
NOT original Julia 10D, no credible subtable hadron emission, no physical bounds.

Input 2 original actions archives with enforced SHA256 checks; SciPy/Numpy/Pandas.
"""
import argparse, hashlib, io, json, math
from pathlib import Path
from zipfile import ZipFile
import numpy as np, pandas as pd
from scipy.integrate import solve_ivp
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq

PUB='75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5'
PAP='3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e'
UPSTREAM='d395183674cace6c9906a8911bdeb7234ba4040d'
# Pinned ROT004 source-derived mass-cube rate for hot PBH and mass cutoff:
GAMMA=4.207579833788249e27 # g^3/s
M_EDGE=1e9; M_CUT=6e9*math.exp(-20); U_CUT=M_CUT/M_EDGE
DT_EDGE=M_EDGE**3/GAMMA; T_NUC=.078185270688319950 # MeV
# Wu-Xu table first two rows in natural GeV mass/rate, near 1e9 g:
M1=5.609588603804452e32; M2=6.099798045788406e32
Q1=np.array([489105.5126008581,59105.93631247951,29086.774913348447,34849.08026691193,34656.17773724596])
Q2=np.array([442306.73787501804,53467.712852971126,26311.795859614824,31504.591028094237,31328.963561830213])
SLOPES=np.log(Q2/Q1)/math.log(M2/M1)
INDEX=np.array([0,0,1,2,3,4])
SPECIES=['pi_minus','pi_plus','K_minus','K0L','pbar','nbar']
HBAR_GEV_SEC=6.582119569e-25
C_CMS=299792458e2
MBARN_CM2=1e-27
SIGMA_V_UNIT=MBARN_CM2*C_CMS
M_P_MEV=938.27208816
Q_MEV=939.5654205-M_P_MEV
TAU_N=878.4
ALPHA=1/137.035999084
ETA_B=6.1e-10
ZETA3=1.202056903159594
HBARC_MEV_CM=197.3269804e-13
NSCALE=1e16 # n_h in cm^-3, transform for numerical conditioning

def checksum(path,digest):
    b=Path(path).read_bytes();assert hashlib.sha256(b).hexdigest()==digest
    return b

def load(pub,pap):
    data={}
    with ZipFile(io.BytesIO(checksum(pub,PUB))) as z:
        for name,fn in [('public_exec','current'),('public_sym','repaired')]:
            data[name]=pd.read_csv(io.BytesIO(z.read('trajectory_'+fn+'.csv')))
    with ZipFile(io.BytesIO(checksum(pap,PAP))) as z:
        for name,fn in [('paper_exec','paper_exec'),('paper_sym','paper_sym')]:
            data[name]=pd.read_csv(io.BytesIO(z.read('trajectory_'+fn+'.csv')))
    for d in data.values():
        assert len(d)==1600 and d.source_active.iloc[1469]==1 and d.source_active.iloc[1470]==0
    return data

def coulomb(T,hadron_mass):
    ve=math.sqrt(T/hadron_mass)+math.sqrt(T/M_P_MEV)
    z=2*math.pi*ALPHA/ve
    return z/(-math.expm1(-z))

def rates(X,T):
    # Source-native temperature, baryon density, decay + scattering
    nB=ETA_B*(2*ZETA3/math.pi**2)*(T/HBARC_MEV_CM)**3
    fp=coulomb(T,139.57039); fk=coulomb(T,493.677)
    a=np.array([1.5*fp,0,31*fk,7,0,28.])
    b=np.array([0,1.7,26,7,28,0.])
    decay=np.array([1/2.6033e-8,1/2.6033e-8,8.1e7,2e7,0,0])
    loss=np.array([a[0]*(1-X),b[1]*X,
                    (34+26)*X+(31+14.5)*fk*(1-X),
                    17*X+17*(1-X),
                    28*X+37*(1-X),
                    37*X+28*(1-X)])
    D=decay+loss*nB*SIGMA_V_UNIT
    # Weak standard model rates: x=Q/T, Γ=(255/tau) polynomial / x^5
    x=Q_MEV/T; g=(255/TAU_N)*(12+6*x+x*x)/x**5
    weak=g*((1-X)*math.exp(-x)-X)-X/TAU_N
    return D,a,b,weak

def simulate(df,mapname,law,rtol,initial,with_weak=True,floor=0,temperature_variant='saved',post_memory=True,method='Radau',source_scale=1.0):
    # TRUE common background extracted from the SINGLE archived 'public_exec' cell.
    # All four 2x2 branches share it, regardless of their archived own T(t).
    time=df.t_sec.to_numpy(); temp=df.T_GeV.to_numpy()*1000
    aa=df.a.to_numpy()
    t0=float(time[0]);m0=float(df.m_PBH_g.iloc[0])
    t_edge=t0+(m0**3-M_EDGE**3)/GAMMA
    t_cut=t_edge+(M_EDGE**3-M_CUT**3)/GAMMA
    # Exact event readout for the selected PCHIP common background, not linear-in-time
    # nor Wu-Xu's archived linear-in-Q/T output interpolation.
    fT=PchipInterpolator(time,temp,extrapolate=False)
    end_idx=int(np.where(temp<T_NUC)[0][0])
    t_eval=float(brentq(lambda z:float(fT(z))-T_NUC, float(time[end_idx-1]),float(time[end_idx]),xtol=1e-12))
    assert abs(float(fT(t_eval))-T_NUC)<1e-12
    fa=PchipInterpolator(time,np.log(aa),extrapolate=False)
    nPBH0=source_scale*float(df.n_PBH_cm3.iloc[1469]); a0=float(df.a.iloc[1469])
    def nPBH(t):
        return nPBH0*math.exp(-3*(float(fa(t))-math.log(a0)))
    # Edge rates: natural GeV emitted per PBH per time, convert by HBAR, multiply by nPBH
    factor=np.ones(6) if mapname=='exec' else np.array([.5,.5,.5,1,.5,.5])
    exponent=SLOPES if law=='public' else np.full(5,-1.3)
    edge_Q=Q1[INDEX]
    expo=exponent[INDEX]
    if initial=='archive':
        y0=np.concatenate([[float(df.Xn.iloc[1469])],np.array([float(df[f'n_{sp}_cm3'].iloc[1469]) for sp in SPECIES])/NSCALE])
    elif initial=='zero':
        y0=np.concatenate([[float(df.Xn.iloc[1469])],np.zeros(6)])
    elif initial=='double':
        y0=np.concatenate([[float(df.Xn.iloc[1469])],2*np.array([float(df[f'n_{sp}_cm3'].iloc[1469]) for sp in SPECIES])/NSCALE])
    else:raise ValueError(initial)
    def dXdt(X,pop,T):
        D,a,b,weak=rates(X,T)
        converted=np.sum(pop*NSCALE*SIGMA_V_UNIT*((1-X)*a-X*b))
        return (weak if with_weak else 0)+converted,D,converted
    def rhs_u(u,y):
        # u=M/M0, so dt/du=-3*(M0^3/GAMMA)*u^2; source finite in u even as u->0
        t=t_edge+DT_EDGE*(1-u**3)
        T=float(fT(t))
        X=float(y[0]);n=y[1:]
        f,D,_=dXdt(X,n,T)
        s=edge_Q*factor*nPBH(t)/HBAR_GEV_SEC * u**expo /NSCALE
        return -3*DT_EDGE*u*u*np.concatenate([[f],s-D*n])
    sol=solve_ivp(rhs_u,(1.,U_CUT),y0,method=method,rtol=rtol,atol=rtol*1e-3,
                  max_step=.02,dense_output=True)
    if not sol.success:raise RuntimeError(str(sol.message))
    probes_u=[1.,.5,.25,.1,.05,.02,.01,.005,.001,1e-4,1e-5,U_CUT]
    probes=[{'u':float(u),'X':float(sol.sol(u)[0]),'time_after_edge_s':DT_EDGE*(1-u**3)} for u in probes_u]
    ycut=sol.y[:,-1];
    def rhs_post(t,y):
        T=float(fT(t)); X=float(y[0]);pop=y[1:]
        f,D,_=dXdt(X,pop,T)
        return np.concatenate([[f],-D*pop])
    post_init=ycut.copy()
    if not post_memory:post_init[1:]=0.
    post=solve_ivp(rhs_post,(t_cut,t_eval),post_init,method=method,rtol=rtol,atol=rtol*1e-3,
                   max_step=2.,dense_output=True)
    if not post.success:raise RuntimeError(str(post.message))
    Xend=float(post.y[0,-1])
    return {'map':mapname,'law':law,'rtol':rtol,'initial':initial,'weak':with_weak,'post_memory':post_memory,'method':method,'source_scale':source_scale,'X_at_mass_probes':probes,
      'T_edge':float(fT(t_edge)),'t_edge':t_edge,'t_cut':t_cut,'t_nuc_target':t_eval,
      'X_start':float(y0[0]),'X_cut':float(ycut[0]),'X_target':Xend,
      'F_cut_per_sec':dXdt(float(ycut[0]),ycut[1:],float(fT(t_cut)))[2],
      'edge_populations_cm3':list((y0[1:]*NSCALE).astype(float)),
      'cut_populations_cm3':list((ycut[1:]*NSCALE).astype(float)),
      'u_nfev':int(sol.nfev),'post_nfev':int(post.nfev),'u_nsteps':len(sol.t),
      'post_nsteps':len(post.t),'step_end_min_u':float(sol.t[-2]-sol.t[-1]),
      'condition':'7D conditional subedge, initial state at saved last active mass reassigned to exact table edge; no preedge repair, no Julia or source-valid emission.'}

def run(args):
    data=load(args.public_zip,args.paper_zip)
    ref=data['public_exec']
    rows=[]
    for tol in [3e-5,3e-7,3e-9]:
      for initial in ['archive','zero','double'] if tol==3e-7 else ['archive']:
        for mp in ['exec','sym']:
          # frozen cell-specific initial populations and X are copied from public 2x2 archive
          d=data['public_exec'] if mp=='exec' else data['public_sym']
          # common public_exec background, so use separate initial data in ref via selected rows
          background=ref.copy()
          for key in ['Xn']+[f'n_{sp}_cm3' for sp in SPECIES]:
              background[key]=d[key].to_numpy()
          for law in ['public','paper']:
            row=simulate(background,mp,law,tol,initial)
            rows.append(row)
            print(mp,law,'tol',tol,'init',initial,'Xcut',round(row['X_cut'],10),'Xtarget',round(row['X_target'],10),flush=True)
    out=Path(args.outdir);out.mkdir(exist_ok=True,parents=True)
    (out/'terminal_7d_results_006.json').write_text(json.dumps({'meta':{'SOURCE':UPSTREAM,'PUBLIC_ACTION_SHA256':PUB,'PAPER_ACTION_SHA256':PAP,'MODEL':'7D reduced conditional terminal mass-controlled forward problem; source UNVALIDATED below 1e9g; X initial at edge proxy; common T(t) from archived public_exec','target':'time at PCHIP background T=0.078185270688319950 MeV'},'rows':rows},indent=2))
    summ=[]
    for tol in sorted({r['rtol'] for r in rows}):
      for initial in sorted({r['initial'] for r in rows if r['rtol']==tol}):
        temp={(r['map'],r['law']):r for r in rows if r['rtol']==tol and r['initial']==initial}
        for mp in ['exec','sym']:
            a=temp[(mp,'public')];b=temp[(mp,'paper')]
            summ.append({'rtol':tol,'initial':initial,'map':mp,'Xpub_nuc':a['X_target'],
                         'Xpap_nuc':b['X_target'],'deltaX_paper_minus_public':b['X_target']-a['X_target'],
                         'Xpub_cut':a['X_cut'],'Xpap_cut':b['X_cut'],
                         'deltaX_cut':b['X_cut']-a['X_cut'],
                         'public_min_step_u':a['step_end_min_u'],'paper_min_step_u':b['step_end_min_u']})
    pd.DataFrame(summ).to_csv(out/'terminal_7d_comparisons_006.csv',index=False,float_format='%.17g')
    print('RESULT_COMPARISONS')
    for t in summ:print(t)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('public_zip');p.add_argument('paper_zip');p.add_argument('--outdir',default=str(Path(__file__).parent));run(p.parse_args())