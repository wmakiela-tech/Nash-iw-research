# Mech-S7 ROT020 — executed scripts and exact source-dependency contract

Companion to `mech_s7_rot020_c2_matched_antinucleon_ratio_dynamic_sign_falsifier_001.md`. Both code listings were actually executed; the exact runnable `.py` and all four dependency modules plus the two SHA-pinned archival ZIPs reside in `MECH_S7_ROTATION_020_REPRODUCIBILITY_20261025.zip`. No native Julia 10D run was executed.

## 1. Main ODE source-shape controller: `reproduce_joint_c2_ratio_020.py`

```python
#!/usr/bin/env python3
"""MECH-S7 ROT020: executed conditional bridged 10+7-variable Wu-Xu source-shape control.
All controls agree through 1e9g; below edge conserve the geometric mean Qp*Qn,
change ONLY log(Qp/Qn) via a positive C^2-at-edge continuation.
IMPORTANT: this is a conditional ODE experiment, not a source-valid PBH calculation.
Reproduction: run in the same directory as the extracted ROT013 dependencies.
"""
import sys,math,json,csv,hashlib,importlib.util,time, argparse
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
P=Path(__file__).resolve().parent

def module(path,name):
    spec=importlib.util.spec_from_file_location(name,str(path))
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
base=module(P/'mech_s7_rotation_009/source_7d_clock_baryon_stress_009.py','base_rot020')
bridge=module(P/'edge_bridge_013.py','bridge_rot020')
bridge.base=base
mod=bridge.host_wrapper_setup(module(P/'active_source_antispectral_012.py','source_rot020'))
PUB=P/'mech_s6_public_2x2_raw.zip';PAP=P/'mech_s6_paper_2x2_raw.zip'
S_EDGE=float(base.SLOPES[3]-base.SLOPES[4])  # source log ratio exponent pbar/nbar
# Index 3 and 4 of 5 source groups correspond to pbar and nbar: verify against source first two rows
S_TABLE=math.log((bridge.A[1,4]/bridge.A[1,5])/(bridge.A[0,4]/bridge.A[0,5]))/math.log(bridge.A[1,0]/bridge.A[0,0])
assert abs(S_TABLE-S_EDGE)<2e-14, (S_TABLE,S_EDGE)

def log_shape(u,kind,lmbd):
    """Difference from native log(Qp/Qn) at subedge normalized u=M/1e9g."""
    z=math.log(u)
    if kind=='native':return 0.
    if kind in ('flat','sumflat'): return S_TABLE*(lmbd*math.tanh(z/lmbd)-z)
    if kind=='reversed':return S_TABLE*(-lmbd*math.tanh(z/lmbd)-z) # same VALUE but derivative changes: forbidden C1; not used.
    if kind=='curved':
        # cubic flat term: zero at z=0 together with first two derivatives. Positive rate under exponentiation.
        return S_TABLE*lmbd*(z/lmbd)**3/(1+(z/lmbd)**4)
    raise ValueError(kind)

def source_rates(u,law,kind,lmbd,epsilon=0.0):
    factors=np.ones(6)
    slopes=np.array(base.SLOPES[base.INDEX] if law=='public' else np.full(6,-1.3),dtype=float,copy=True)
    if law=='paper':slopes[4]+=epsilon;slopes[5]-=epsilon
    values=np.array(base.Q1[base.INDEX],float)*u**slopes
    if law=='public':
       logdelta=log_shape(u,kind,lmbd)
       if kind=='sumflat':
           total=values[4]+values[5]
           ratio=(values[4]/values[5])*math.exp(logdelta)
           values[4]=total*ratio/(1+ratio)
           values[5]=total/(1+ratio)
       else:
           values[4]*=math.exp(.5*logdelta)
           values[5]*=math.exp(-.5*logdelta)
    return values

def evolve_law(ctx,eos,host,mp,law='public',kind='native',lmbd=.05,epsilon=0.,rtol=3e-8,conserve=False):
    df=ctx['maps'][mp]
    X0=float(df.Xn.iloc[1469]);npop=np.array([float(df[f'n_{sp}_cm3'].iloc[1469]) for sp in base.SPECIES])/base.NSCALE
    y0=np.r_[X0,npop]
    factors=np.ones(6) if mp=='exec' else np.array([.5,.5,.5,1,.5,.5])
    Tedge=ctx['Tedge']
    def derivative(y,T,logA):
        X=y[0]; pops=y[1:]
        baryon_factor=(Tedge/T)**3*math.exp(-3*logA) if conserve else 1.
        D,aa,bb,weak=base.rates(X,T,baryon_scale=baryon_factor)
        conv=np.sum(pops*base.NSCALE*base.SIGMA_V_UNIT*((1-X)*aa-X*bb))
        return weak+conv,D
    def active(u,y):
        T=host['pre_T'](u);logA=host['pre_lna'](u)
        f,D=derivative(y,T,logA)
        nPBH=ctx['nedge']*math.exp(-3*logA)
        source=source_rates(u,law,kind,lmbd,epsilon)*factors*nPBH/mod.HBAR_GEV_SEC/base.NSCALE
        return -3*base.DT_EDGE*u*u*np.r_[f,source-D*y[1:]]
    a=solve_ivp(active,(1.,base.U_CUT),y0,method='Radau',rtol=rtol,atol=rtol*1e-3,max_step=.01)
    if not a.success:raise RuntimeError('Active: '+a.message)
    def post(t,y):
        f,D=derivative(y,host['post_T'](t),host['post_lna'](t))
        return np.r_[f,-D*y[1:]]
    b=solve_ivp(post,(ctx['tcut'],host['Tnuc_time']),a.y[:,-1],method='Radau',rtol=rtol,atol=rtol*1e-3,max_step=2.)
    if not b.success:raise RuntimeError('Post: '+b.message)
    return {'X_edge':X0,'X_cut':float(a.y[0,-1]),'X_nuc':float(b.y[0,-1]),'nfev':a.nfev+b.nfev,'steps':len(a.t)+len(b.t)}

def main():
    p=argparse.ArgumentParser();p.add_argument('--rtol',type=float,default=3e-8);p.add_argument('--out',default=str(P));p.add_argument('--chis',default='0.5');p.add_argument('--models',default='native,flat:.05,flat:.2,curved:.05');p.add_argument('--baryons',default='eta');args=p.parse_args()
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    raw=base.load(PUB,PAP);orig=mod.contexts(base,PUB,PAP);eos=mod.eos_table()
    mods=[]
    for z in args.models.split(','):
        if ':' in z:
            typ,lmbd=z.split(':');mods.append((typ,float(lmbd)))
        else:mods.append((z,.05))
    records=[];state=[];start=time.time()
    for chi in map(float,args.chis.split(',')):
      for conserve in [x=='comoving' for x in args.baryons.split(',')]:
        for mp in ('exec','sym'):
            br=bridge.run_bridge(base,mod,raw,eos,chi,mp,conserve,rtol=args.rtol)
            state.append(br)
            ctx=bridge.shifted_ctx(orig,br,mp)
            host=mod.prepare_host(base,ctx,eos,chi,rtol=2e-10)
            paper=evolve_law(ctx,eos,host,mp,law='paper',rtol=args.rtol,conserve=conserve)
            reference=evolve_law(ctx,eos,host,mp,law='public',rtol=args.rtol,conserve=conserve)
            print('BASELINE',chi,conserve,mp,'reference',paper['X_nuc']-reference['X_nuc'],flush=True)
            for kind,lmbd in mods:
                res=reference if kind=='native' else evolve_law(ctx,eos,host,mp,law='public',kind=kind,lmbd=lmbd,rtol=args.rtol,conserve=conserve)
                row=dict(chi=chi,baryon='comoving' if conserve else 'eta',mp=mp,kind=kind,lmbd=lmbd,X_paper=paper['X_nuc'],X_public=res['X_nuc'],delta_X=paper['X_nuc']-res['X_nuc'],delta_public_vs_native=res['X_nuc']-reference['X_nuc'],Xcut_public=res['X_cut'],steps=res['steps'])
                records.append(row)
                print('CASE',mp,chi,row['baryon'],kind,lmbd,'delta',row['delta_X'],'shift',row['delta_public_vs_native'],'elapsed',round(time.time()-start,2),flush=True)
    with (out/'matched_edge_7d_kinetics_020.csv').open('w',newline='') as f:
      w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader();w.writerows(records)
    md=[]
    for kind,lmbd in mods:
        for u in [1,0.5,0.2,0.1,0.01,base.U_CUT]:
            d=log_shape(u,kind,lmbd)
            native=source_rates(u,'public','native',lmbd)
            changed=source_rates(u,'public',kind,lmbd)
            p_factor=changed[4]/native[4];n_factor=changed[5]/native[5]
            sum_factor=(changed[4]+changed[5])/(native[4]+native[5])
            product_factor=(changed[4]*changed[5])/(native[4]*native[5])
            md.append({'kind':kind,'lambda':lmbd,'u':u,
                'native_ratio_change_pct':100*(u**S_TABLE-1),
                'new_ratio_change_pct':100*(math.exp(S_TABLE*math.log(u)+d)-1),
                'log_delta_vs_native':d,'p_factor':p_factor,'n_factor':n_factor,
                'sum_factor':sum_factor,'product_factor':product_factor})
    with (out/'matched_edge_source_witness_020.csv').open('w',newline='') as f:
      w=csv.DictWriter(f,fieldnames=list(md[0]));w.writeheader();w.writerows(md)
    assert all(abs(r['product_factor']-1)<1e-13 for r in md if r['kind']!='sumflat')
    assert all(abs(r['sum_factor']-1)<1e-14 for r in md if r['kind']=='sumflat')
    # Exact analytic C2 edge jet: delta(z)=S*(lambda*tanh(z/lambda)-z).
    # First and second edge derivatives vanish, third derivative -2*S/lambda^2.
    assert abs(log_shape(1.0,'flat',.05))<1e-16
    result={'source_commit':base.UPSTREAM,'source_table_blob':'06d0883a27b108692720422294ba2baacd381a64','rot013_edge_state_inheritance':'same archive last-active row; no original Julia','source_ratio_slope':S_TABLE,'rtol':args.rtol,'rows':records,'bridge':state,'models':mods}
    (out/'matched_edge_dynamics_020.json').write_text(json.dumps(result,indent=2))
    print('DONE',len(records),round(time.time()-start,1),flush=True)
if __name__=='__main__':main()

```

## 2. Nominal ratio saturation root finder: `find_c2_saturation_threshold_020.py`

```python
#!/usr/bin/env python3
"""MECH-S7 ROT020: find one parameter root in C2-matched below-edge ratio family.
No source-valid below-edge emission or original Julia 10D claimed.
"""
from pathlib import Path
import json,time,math,csv,argparse
from scipy.optimize import brentq
import reproduce_joint_c2_ratio_020 as m
P=Path(__file__).resolve().parent

def main():
  ap=argparse.ArgumentParser();ap.add_argument('--rtol',type=float,default=3e-8);ap.add_argument('--out',default=str(P));ap.add_argument('--kind',choices=('flat','sumflat'),default='flat');a=ap.parse_args()
  out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
  raw=m.base.load(m.PUB,m.PAP);orig=m.mod.contexts(m.base,m.PUB,m.PAP);eos=m.mod.eos_table()
  br=m.bridge.run_bridge(m.base,m.mod,raw,eos,.5,'exec',False,rtol=a.rtol)
  ctx=m.bridge.shifted_ctx(orig,br,'exec')
  host=m.mod.prepare_host(m.base,ctx,eos,.5,rtol=2e-10)
  xpap=m.evolve_law(ctx,eos,host,'exec','paper',rtol=a.rtol)['X_nuc']
  native=m.evolve_law(ctx,eos,host,'exec','public',kind='native',rtol=a.rtol)['X_nuc']
  rows=[]
  def residual(lbd):
    x=m.evolve_law(ctx,eos,host,'exec','public',kind=a.kind,lmbd=lbd,rtol=a.rtol)['X_nuc']
    v=xpap-x
    rows.append({'lmbd':lbd,'X_public':x,'X_paper':xpap,'delta_X':v})
    print('LAMBDA',lbd,'delta',v,flush=True)
    return v
  small=residual(.2);large=residual(5.)
  if small*large>=0:raise RuntimeError('No bracket for the root')
  root=brentq(residual,.2,5.,xtol=3e-9,rtol=3e-9)
  zero=residual(root)
  for u in [.5,.2,.1,.01]:
    print('RATIO_ROOT',u,'pct',100*(math.exp(m.S_TABLE*math.log(u)+m.log_shape(u,a.kind,root))-1),flush=True)
  with (out/f'c2_ratio_{a.kind}_saturation_root_history_020.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
  result={'critical_lambda':root,'postroot_residual':zero,'baseline_delta':xpap-native,'endpoint':xpap,'rtol':a.rtol,'calls':len(rows),'edge_table_slope':m.S_TABLE,'kind':a.kind}
  (out/f'c2_ratio_{a.kind}_saturation_root_020.json').write_text(json.dumps(result,indent=2))
  print('RESULT',result,flush=True)
if __name__=='__main__':main()

```

## Reproducibility commands

```bash
python reproduce_joint_c2_ratio_020.py --chis 0,0.5,1 --baryons eta,comoving --models native,flat:.05,sumflat:.05 --out sumcontrols
python find_c2_saturation_threshold_020.py --kind sumflat --rtol 3e-9 --out .
```

**Guards:** NO_ORIGINAL_JULIA_10D / NO_SOURCE_VALID_E2B / NO_Yp_DH / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY.