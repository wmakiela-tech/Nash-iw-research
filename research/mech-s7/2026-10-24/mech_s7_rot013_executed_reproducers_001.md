# ROT013 — kompletne skrypty źródłowe


Pliki pomocnicze i wymagane oryginalne archiwa znajdują się w pakiecie ZIP. Źródło Wu–Xu: przypięty commit `d395183674cace6c9906a8911bdeb7234ba4040d`.


## `edge_bridge_013.py`

```python

#!/usr/bin/env python3
"""MECH-S7 ROT013. Source-tabulated M=1.8366e9 to 1e9g bridge, followed by
ROT011/012 7D source-active conditional micro EOS and fixed-T readout.
This is a REDUCED synthetic transfer, not original 10D Julia or physical BBN.
Wu-Xu pinned original hadron table first 8 rows Git blob 06d088..., source first-table
mass 1e9g. The loglinear above-edge Q interpolation is exact code prescription.
Source-active thermal model is hypothetical chi fraction, not Hawking species BR.
"""
from pathlib import Path
import sys,importlib.util, math, json, csv, argparse, hashlib
import numpy as np
from scipy.integrate import solve_ivp

ROOT=Path(__file__).resolve().parent if (Path(__file__).resolve().parent/'active_source_antispectral_012.py').exists() else Path('/mnt/data/mech_s7_rotation_012')
SCRIPT=ROOT/'active_source_antispectral_012.py'
BASE=ROOT/'mech_s7_rotation_009/source_7d_clock_baryon_stress_009.py'
PUB=ROOT/'mech_s6_public_2x2_raw.zip'
PAP=ROOT/'mech_s6_paper_2x2_raw.zip'

# Exact columns extracted via source-pinned GitHub fetch_file, SHA(blob):
# 06d0883a27b108692720422294ba2baacd381a64, original 100-row table.
SOURCE8='''
5.609588603804452e32 489105.5126008581 59105.93631247951 29086.774913348447 34849.08026691193 34656.17773724596
6.099798045788406e32 442306.73787501804 53467.712852971126 26311.795859614824 31504.591028094237 31328.963561830213
6.632845798026921e32 398690.1598495927 48211.730108163305 23725.176936555476 28387.973269731203 28228.650640502765
7.212475404948756e32 358559.19536496664 43374.63741563819 21344.783627377088 25521.031717558253 25376.846686105455
7.842757550984395e32 322060.72296048724 38974.46193231208 19179.30370937906 22914.14992967101 22783.765726686597
8.528118648601441e32 289050.62442306214 34993.890879347164 17220.15976305694 20557.039300656503 20439.153412336287
9.273371924584742e32 259332.04736516144 31409.435724546158 15455.783823623013 18435.545939209584 18328.895469639596
1.008375122287719e33 232613.7291020198 28185.93864132649 13868.975338526008 16528.826829228834 16432.30301047628
1.0964947761375425e33 208619.52808866516 25290.27823804905 12443.514823508669 14817.06284452867 14729.692480456592
'''
A=np.loadtxt(SOURCE8.splitlines())
TABLE_MASS=A[:,0]/A[0,0]*1e9
assert np.all(np.diff(TABLE_MASS)>0) and np.isclose(TABLE_MASS[0],1e9)

def Qtab(mass):
    z=np.log(float(mass))
    assert TABLE_MASS[0]*(1-1e-12)<=mass<=TABLE_MASS[-1]*(1+1e-12),mass
    return np.array([math.exp(float(np.interp(z,np.log(TABLE_MASS),np.log(A[:,j])))) for j in range(1,6)])

def module(path,name):
    spec=importlib.util.spec_from_file_location(name,str(path));v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v);return v

def run_bridge(base,mod,raw,eos,chi,mp,conserve_from_saved=False,rtol=3e-8):
    r=raw['public_exec'].iloc[1469];rmap=raw['public_'+mp].iloc[1469]
    m0=float(r.m_PBH_g);T0=float(r.T_GeV)*1000
    t0=float(r.t_sec);a0=float(r.a);nPBH0=float(r.n_PBH_cm3)
    uend=base.M_EDGE/m0; dt0=m0**3/base.GAMMA
    x0=float(rmap.Xn);n0=np.array([float(rmap[f'n_{sp}_cm3']) for sp in base.SPECIES])/base.NSCALE
    rnu0=eos['neutrino_rho'](T0*(eos['gs'](T0)/5.5)**(1/3))
    fields=lambda y,u:None
    ifactor=np.ones(6) if mp=='exec' else np.array([.5,.5,.5,1,.5,.5])
    def RHS(u,y):
        T,lr,lnrnu,X=*y[:4],
        npop=y[4:]
        nPBH=nPBH0*math.exp(-3*lr)
        rnu=math.exp(lnrnu)
        rpbh=nPBH*m0*u
        rem=eos['rho'](T); pem=eos['P'](T)
        H=math.sqrt(8*math.pi*mod.G_CGS/3*(rem+rnu+rpbh))
        dudu=-1/(3*dt0*u*u)
        Q=nPBH*m0*(-dudu)
        dTdt=(-3*H*(rem+pem)+chi*Q)/eos['d_rho_dT'](T)
        drnudt=-4*H*rnu+(1-chi)*Q
        factor=(T0/T)**3*math.exp(-3*lr) if conserve_from_saved else 1.
        D,aa,bb,weak=base.rates(X,T,baryon_scale=factor)
        conv=np.sum(npop*base.NSCALE*base.SIGMA_V_UNIT*((1-X)*aa-X*bb))
        source=Qtab(m0*u)[base.INDEX]*ifactor*nPBH/base.HBAR_GEV_SEC/base.NSCALE
        dtdu=-3*dt0*u*u
        return dtdu*np.r_[dTdt,H,drnudt/rnu,weak+conv,source-D*npop]
    y0=np.r_[T0,0.,math.log(rnu0),x0,n0]
    sol=solve_ivp(RHS,(1.,uend),y0,method='Radau',rtol=rtol,atol=[1e-11,1e-11,1e-11,rtol*1e-3,*([rtol*1e-3]*6)],max_step=.01)
    if not sol.success:raise RuntimeError(sol.message)
    y=sol.y[:,-1]
    # exact source table supported edge: smooth at uend, no inserted extrapolation above table.
    fstart=Qtab(m0)[base.INDEX]
    fedge=Qtab(base.M_EDGE)[base.INDEX]
    return {'T0':T0,'m0':m0,'t0':t0,'nPBH0':nPBH0,'chi':chi,'map':mp,'conserve_from_saved':conserve_from_saved,
        't_edge_direct':t0+dt0*(1-uend**3),'t_edge_absolute':t0+(m0**3-base.M_EDGE**3)/base.GAMMA,
        'Tedge':float(y[0]),'lnaedge':float(y[1]),'rnu_edge':math.exp(float(y[2])),
        'Xedge':float(y[3]),'nedge':nPBH0*math.exp(-3*float(y[1])),
        'nedge_pop_cm3':list((y[4:]*base.NSCALE).astype(float)),
        'saved_pop_cm3':list((n0*base.NSCALE).astype(float)),
        'nfev':sol.nfev,'steps':len(sol.t),'source_start_rates':list(fstart),'source_edge_rates':list(fedge)}

def shifted_ctx(orig, b, mp):
    d=orig.copy();d['tedge']=b['t_edge_direct'];d['tcut']=b['t_edge_direct'] + (base.M_EDGE**3-base.M_CUT**3)/base.GAMMA
    d['Tedge']=b['Tedge'];d['nedge']=b['nedge'];d['rnu_override']=b['rnu_edge']
    # only field maps may be mutated; archive source arrays untouched.
    d['maps']={name: f.copy(deep=True) for name,f in orig['maps'].items()}
    frame=d['maps'][mp];ix=1469;frame.at[ix,'Xn']=b['Xedge']
    for k,name in enumerate(base.SPECIES):frame.at[ix,f'n_{name}_cm3']=b['nedge_pop_cm3'][k]
    return d

def host_wrapper_setup(mod):
    # source-code-local substitution to carry preedge physical neutrino density through
    # source-on t>=edge ODE, rather than silently resetting the neutrino bath at edge.
    original=mod.prepare_host.__code__
    # avoid unsafe runtime function patching by loading a verified alternate local source file.
    src=SCRIPT.read_text();needle="rnu0=eos['neutrino_rho'](Tnu0)"
    assert src.count(needle)==1
    dest=Path(__file__).parent/'active_micro_bridge_013.py'
    dest.write_text(src.replace(needle,"rnu0=ctx.get('rnu_override',eos['neutrino_rho'](Tnu0))"))
    return module(dest,'modbridge013')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',default=str(Path(__file__).parent));ap.add_argument('--rtol',type=float,default=3e-8)
    ap.add_argument('--chis',default='0.5');ap.add_argument('--baryons',default='eta');args=ap.parse_args()
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    global base;base=module(BASE,'base_013')
    mod=host_wrapper_setup(module(SCRIPT,'origmod_013'))
    orig=mod.contexts(base,PUB,PAP);raw=base.load(PUB,PAP);eos=mod.eos_table()
    rows=[];bridges=[];t=__import__('time').time()
    for chi in map(float,args.chis.split(',')):
      for conserve in [x=='comoving' for x in args.baryons.split(',')]:
       for mp in ['exec','sym']:
        br=run_bridge(base,mod,raw,eos,chi,mp,conserve,rtol=args.rtol)
        bridges.append(br);ctx=shifted_ctx(orig,br,mp)
        h=mod.prepare_host(base,ctx,eos,chi,rtol=2e-10)
        h0=mod.prepare_host(base,orig,eos,chi,rtol=2e-10)
        for mode,ct,hst in [('transplant',orig,h0),('supported_bridge',ctx,h)]:
            res=[]
            for law in ('public','paper'):
                v=mod.evolve(base,ct,eos,hst,mp,law,conserve=conserve,rtol=args.rtol)
                res.append(v)
            row={'chi_EM':chi,'baryon':'comoving' if conserve else 'eta','map':mp,'mode':mode,
                 'X_public':res[0]['X_nuc'],'X_paper':res[1]['X_nuc'],
                 'deltaX':res[1]['X_nuc']-res[0]['X_nuc'],
                 'Tedge':ct['Tedge'],'t_edge':ct['tedge'],'Tcut':hst['Tcut'],'t_nuc':hst['Tnuc_time'],
                 'Xedge':res[0]['Xedge'],'Xcut_public':res[0]['Xcut']}
            rows.append(row)
        transplant=rows[-2];transport=rows[-1]
        print('COMPARE',chi,conserve,mp,'deltaX base',transplant['deltaX'],'transport',transport['deltaX'],'ratio',transport['deltaX']/transplant['deltaX'],'Xedge old',transplant['Xedge'],'new',transport['Xedge'],'step',br['steps'],'elapsed',round(__import__('time').time()-t,1),flush=True)
    with (out/'supported_bridge_vs_transplant_013.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
    with (out/'bridge_edge_states_013.json').open('w') as f:json.dump({'results':bridges,'source_commit':base.UPSTREAM,'table_blob':'06d0883a27b108692720422294ba2baacd381a64','source_rows':SOURCE8.strip().splitlines()},f,indent=2)
    print('DONE',len(rows),len(bridges),flush=True)
if __name__=='__main__':main()


```

## `edge_bridge_ablation_013.py`

```python

#!/usr/bin/env python3
"""ROT013 conditional separation: correct edge population vs correct background/time/temperature."""
from pathlib import Path
import importlib.util,csv,json
P=Path(__file__).parent
s=importlib.util.spec_from_file_location('rot013',P/'edge_bridge_013.py');b=importlib.util.module_from_spec(s);s.loader.exec_module(b)
b.base=b.module(b.BASE,'baseabl013'); m=b.host_wrapper_setup(b.module(b.SCRIPT,'modpreabl013'))
raw=b.base.load(b.PUB,b.PAP);orig=m.contexts(b.base,b.PUB,b.PAP);eos=m.eos_table();out=[];models=[]
for mp in ('exec','sym'):
 bridge=b.run_bridge(b.base,m,raw,eos,.5,mp,False,rtol=3e-8)
 full=b.shifted_ctx(orig,bridge,mp)
 state=orig.copy();state['maps']={k:v.copy(deep=True) for k,v in orig['maps'].items()};state['maps'][mp]=full['maps'][mp]
 background=full.copy();background['maps']=orig['maps']
 for label,ctx in [('raw_transplant',orig),('state_transport_only',state),('host_mass_clock_only',background),('both_corrected',full)]:
   host=m.prepare_host(b.base,ctx,eos,.5,rtol=2e-10)
   runs={law:m.evolve(b.base,ctx,eos,host,mp,law,False,rtol=3e-8) for law in ('public','paper')}
   row={'map':mp,'mode':label,'deltaX':runs['paper']['X_nuc']-runs['public']['X_nuc'],'Xpublic':runs['public']['X_nuc'],
   'Xpaper':runs['paper']['X_nuc'],'Xcutpub':runs['public']['Xcut'],'Tedge':ctx['Tedge'],'tedge':ctx['tedge'],'t_nuc':host['Tnuc_time']}
   out.append(row);print(row,flush=True)
with (P/'bridge_state_background_ablation_013.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=out[0]);w.writeheader();w.writerows(out)


```

## `spectral_bridge_roots_013.py`

```python

#!/usr/bin/env python3
"""MECH-S7 ROT013: edge state transport changes antispectral index kill roots."""
import importlib.util,json,math,sys,csv
from pathlib import Path
from scipy.optimize import brentq
from time import perf_counter
here=Path(__file__).parent
spec=importlib.util.spec_from_file_location('bridge',here/'edge_bridge_013.py');b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
b.base=b.module(b.BASE,'base_roots_013'); mod=b.host_wrapper_setup(b.module(b.SCRIPT,'mod_prev_013'))
raw=b.base.load(b.PUB,b.PAP);orig=mod.contexts(b.base,b.PUB,b.PAP);eos=mod.eos_table()
chi=.5;h_0=mod.prepare_host(b.base,orig,eos,chi,rtol=2e-10)
start=perf_counter();res=[]
for mp in ('exec','sym'):
  br=b.run_bridge(b.base,mod,raw,eos,chi,mp,False,rtol=3e-8)
  ctx=b.shifted_ctx(orig,br,mp);h=mod.prepare_host(b.base,ctx,eos,chi,rtol=2e-10)
  xpub=mod.evolve(b.base,ctx,eos,h,mp,'public',conserve=False,rtol=3e-8)['X_nuc']
  def f(epsilon,tol=3e-8):return mod.evolve(b.base,ctx,eos,h,mp,'paper',conserve=False,rtol=tol,anti_epsilon=epsilon)['X_nuc']-xpub
  l,r=(-.002,.002);fl=f(l);fr=f(r)
  print('BRACKET',mp,fl,fr,flush=True)
  root=brentq(f,l,r,xtol=2e-9,rtol=9e-9,maxiter=35)
  nominal=f(0);err=f(root)
  tightpub=mod.evolve(b.base,ctx,eos,h,mp,'public',conserve=False,rtol=3e-9)['X_nuc']
  tightpaper=mod.evolve(b.base,ctx,eos,h,mp,'paper',conserve=False,rtol=3e-9,anti_epsilon=root)['X_nuc']
  res.append({'chi_EM':chi,'map':mp,'epsilon_kill_root':root,'nominal_deltaX':nominal,'root_residual':err,'tight_root_residual':tightpaper-tightpub,'root_slope_separation':2*root,'relative_source_ratio_at_M1e8':math.exp(2*root*math.log(.1))-1,'Xedge_transport':br['Xedge'],'nPBH_edge':br['nedge']})
  print('ROOT',mp,res[-1],'elapsed',perf_counter()-start,flush=True)
with (here/'bridge_spectral_roots_013.json').open('w') as f:json.dump(res,f,indent=2)
with (here/'bridge_spectral_roots_013.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=res[0]);w.writeheader();w.writerows(res)


```