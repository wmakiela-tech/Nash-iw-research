# Mech-S7 ROT022 — complete executed Python source and reproduction protocol

This file contains **all three executed ROT022 scripts verbatim**. To reproduce: save each fenced section as the named `.py` file in one directory with the documented ROT021/020/013 dependency files and original Wu-Xu trajectory ZIPs, then run in numeric order with Python+NumPy+SciPy. Full set of dependencies and exactly pinned raw archives are included in the local reproducibility ZIP. Source below `M=1e9g` remains physically unvalidated; no original Julia 10D run.

Report: `research/mech-s7/2026-10-25/mech_s7_rot022_postsource_state_memory_and_reaction_budget_001.md`.

## 1. `reproduce_postsource_memory_partition_022.py`
SHA256 `692f1f53289f689c074c1ebd24299d2b224cdb046791dfd452c336beb51241b3`

```python
#!/usr/bin/env python3
"""MECH-S7 ROT022: exact nonlinear post-evaporation state-swap decomposition.
Source-conditioned preedge ten-component replay + seven-dimensional late dynamics;
pointwise exact Qpbar+Qnbar conservation. No source-valid PBH physics claim.
Requires pinned original Wu-Xu archives and ROT013/020 dependency scripts.
"""
import csv,json,math,itertools,time,hashlib
from pathlib import Path
from math import factorial
import numpy as np
from scipy.integrate import solve_ivp
import reproduce_joint_c2_ratio_020 as prev
ROOT=Path(__file__).resolve().parent
base,bridge,mod=prev.base,prev.bridge,prev.mod

def run_one(mp='exec',chi=.5,conserve=False,rtol=3e-9,shape='sumflat',lmbd=.05):
    begin=time.time()
    raw=base.load(prev.PUB,prev.PAP)
    orig=mod.contexts(base,prev.PUB,prev.PAP)
    eos=mod.eos_table()
    bridged=bridge.run_bridge(base,mod,raw,eos,chi,mp,conserve_from_saved=conserve,rtol=rtol)
    ctx=bridge.shifted_ctx(orig,bridged,mp)
    host=mod.prepare_host(base,ctx,eos,chi,rtol=2e-10)
    df=ctx['maps'][mp]
    yy0=np.r_[float(df.Xn.iloc[1469]),np.array([float(df[f'n_{sp}_cm3'].iloc[1469]) for sp in base.SPECIES])/base.NSCALE]
    factors=np.ones(6) if mp=='exec' else np.array([.5,.5,.5,1,.5,.5])
    Tedge=ctx['Tedge']
    def kin(y,T,ln_a):
        scale=(Tedge/T)**3*math.exp(-3*ln_a) if conserve else 1.
        X=y[0];n=y[1:]
        D,aa,bb,weak=base.rates(X,T,baryon_scale=scale)
        dx=weak+np.dot(n,base.NSCALE*base.SIGMA_V_UNIT*((1-X)*aa-X*bb))
        return dx,D
    def src(u,y,kind):
        T=host['pre_T'](u); ln_a=host['pre_lna'](u)
        dx,D=kin(y,T,ln_a)
        nPBH=ctx['nedge']*math.exp(-3*ln_a)
        qq=prev.source_rates(u,'public',kind,lmbd)
        source=qq*factors*nPBH/mod.HBAR_GEV_SEC/base.NSCALE
        return -3*base.DT_EDGE*u*u*np.r_[dx,source-D*y[1:]]
    cut={}
    for kind in ['native',shape]:
        r=solve_ivp(lambda u,y:src(u,y,kind),(1.,base.U_CUT),yy0,method='Radau',rtol=rtol,atol=rtol*1e-3,max_step=.01)
        assert r.success,r.message
        cut[kind]=r.y[:,-1].copy()
    def post(t,y,no_hadrons=False):
        T=host['post_T'](t); ln_a=host['post_lna'](t)
        if no_hadrons:
            X=y[0]
            D,aa,bb,weak=base.rates(X,T,baryon_scale=1.)
            return np.r_[weak,np.zeros(6)]
        dx,D=kin(y,T,ln_a)
        return np.r_[dx,-D*y[1:]]
    def after(y, no_hadrons=False):
        r=solve_ivp(lambda t,y:post(t,y,no_hadrons),(ctx['tcut'],host['Tnuc_time']),y,method='Radau',rtol=rtol,atol=rtol*1e-3,max_step=2.)
        assert r.success,r.message
        return float(r.y[0,-1])
    # Two-factor exact Shapley of finite change in the cutoff state, not a causal ontology.
    nat,alt=cut['native'],cut[shape]
    full_nat=after(nat);full_alt=after(alt)
    Xonly_n=after(np.r_[alt[0],nat[1:]])
    Honly_n=after(np.r_[nat[0],alt[1:]])
    exX=.5*((Xonly_n-full_nat)+(full_alt-Honly_n))
    exH=.5*((Honly_n-full_nat)+(full_alt-Xonly_n))
    assert abs(exX+exH-(full_alt-full_nat))<1e-14
    # 4 factor fully coupled postsource: X, mesons (4), pbar, nbar
    groups=[[0],[1,2,3,4],[5],[6]]
    vals={}
    for mask in range(16):
        y=nat.copy()
        for g,inds in enumerate(groups):
            if mask>>g&1: y[inds]=alt[inds]
        vals[mask]=after(y)
    shapley=[]
    N=len(groups)
    for g in range(N):
        v=0.
        for mask in range(1<<N):
            if mask>>g&1: continue
            k=int(mask.bit_count())
            v+=factorial(k)*factorial(N-k-1)/factorial(N)*(vals[mask|(1<<g)]-vals[mask])
        shapley.append(v)
    assert abs(sum(shapley)-(full_alt-full_nat))<1e-13,(sum(shapley),full_alt-full_nat)
    no_memory_nat=after(nat,no_hadrons=True);no_memory_alt=after(alt,no_hadrons=True)
    result={'map':mp,'chi_EM':chi,'baryons':'comoving' if conserve else 'constant_eta','rtol':rtol,'source_mode':shape,'lambda':lmbd,
        'source_definition':'PUBLIC native vs modified pbar/nbar pointwise-exact-sum, all other Q and host fixed',
        'Xn_source_off_baseline':float(nat[0]),'Xn_source_off_modified':float(alt[0]),'delta_Xn_source_off':float(alt[0]-nat[0]),
        'Xn_Tnuc_baseline':full_nat,'Xn_Tnuc_modified':full_alt,'delta_Xn_Tnuc':full_alt-full_nat,
        'Xnuc_hybrid_X_modified_hadrons_native':Xonly_n,'Xnuc_hybrid_X_native_hadrons_modified':Honly_n,
        'two_group_shapley_X_cut':exX,'two_group_shapley_hadron_memory':exH,
        'two_group_share_X_cut':exX/(full_alt-full_nat),'two_group_share_hadron_memory':exH/(full_alt-full_nat),
        'four_group_shapley_labels':['X_cut','mesons_4','pbar','nbar'],
        'four_group_shapley':shapley,
        'postsource_nohadron_delta_X':no_memory_alt-no_memory_nat,
        'source_off_state_native':nat.tolist(),'source_off_state_modified':alt.tolist(),
        'state_cut_delta':(alt-nat).tolist(),'postsource_4factor_cells':{str(m):x for m,x in vals.items()},
        'postsource_time_s':host['Tnuc_time']-ctx['tcut'],'runtime_s':time.time()-begin,
        'guard':'not source-original Julia; no PBH bound; source unsupported below 1e9g'}
    print('RESULT',mp,'dX_cut',result['delta_Xn_source_off'],'dX_nuc',result['delta_Xn_Tnuc'],
          'shapley_X',exX,'shapley_hadrons',exH,'4group',shapley,'dt',round(result['runtime_s'],1),flush=True)
    return result

def main():
    cases=[]
    for mp in ['exec','sym']:
        cases.append(run_one(mp))
    (ROOT/'postsource_memory_partition_022.json').write_text(json.dumps({'cases':cases,'source_commit':base.UPSTREAM,'previous_kernel_source':'ROT021','claim_ceiling':'CONDITIONAL_MODEL_ONLY'},indent=2))
    with (ROOT/'postsource_memory_partition_022.csv').open('w',newline='') as f:
        fieldnames=['map','delta_Xn_source_off','delta_Xn_Tnuc','two_group_shapley_X_cut','two_group_shapley_hadron_memory','two_group_share_X_cut','two_group_share_hadron_memory','postsource_nohadron_delta_X','pbar_shapley','nbar_shapley','mesons_shapley']
        w=csv.DictWriter(f,fieldnames=fieldnames);w.writeheader()
        for c in cases:
            w.writerow({**{k:c.get(k) for k in fieldnames},'pbar_shapley':c['four_group_shapley'][2],'nbar_shapley':c['four_group_shapley'][3],'mesons_shapley':c['four_group_shapley'][1]})
if __name__=='__main__':main()
```

## 2. `verify_postsource_weak_hadron_budget_022.py`
SHA256 `13a1a9b63553207cbf784691ccc43bf59ae11edabd406a3d8dddb8362d6e39e9`

```python
#!/usr/bin/env python3
"""Independent FToC check: X_nuc-X_cut=integral(weak+decay)+integral(hadron scattering).
Two source trajectories share host, and pair sum of pbar+nbar source is preserved.
"""
import math,json,csv
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
import reproduce_postsource_memory_partition_022 as mem
prev,base,bridge,mod=mem.prev,mem.base,mem.bridge,mem.mod
P=Path(__file__).resolve().parent
R=json.loads((P/'postsource_memory_partition_022.json').read_text())
res=[]
raw=base.load(prev.PUB,prev.PAP); orig=mod.contexts(base,prev.PUB,prev.PAP);eos=mod.eos_table()
for c in R['cases']:
    mp=c['map'];chi=c['chi_EM'];conserve=c['baryons']=='comoving'
    br=bridge.run_bridge(base,mod,raw,eos,chi,mp,conserve_from_saved=conserve,rtol=c['rtol'])
    ctx=bridge.shifted_ctx(orig,br,mp)
    host=mod.prepare_host(base,ctx,eos,chi,rtol=2e-10)
    cutT=ctx['Tedge']
    def rhs(t,y):
        X=float(y[0]);ns=y[1:7]
        T=host['post_T'](t);a=host['post_lna'](t)
        baryon=(cutT/T)**3*math.exp(-3*a) if conserve else 1.
        D,aa,bb,weak=base.rates(X,T,baryon_scale=baryon)
        hadr=np.dot(ns,base.NSCALE*base.SIGMA_V_UNIT*((1-X)*aa-X*bb))
        return np.r_[weak+hadr,-D*ns,weak,hadr]
    rows=[]
    for kind in ['native','sumflat']:
        init=np.array(c['source_off_state_native'] if kind=='native' else c['source_off_state_modified'])
        start=np.r_[init,[0.,0.]]
        sol=solve_ivp(rhs,(ctx['tcut'],host['Tnuc_time']),start,method='Radau',rtol=3e-9,atol=3e-12,max_step=2.)
        assert sol.success
        yf=sol.y[:,-1]
        assert abs((yf[0]-init[0])-(yf[7]+yf[8]))<2e-12
        rows.append({'kind':kind,'X_cut':init[0],'X_nuc':float(yf[0]),'weak_integral':float(yf[7]),'hadron_integral':float(yf[8]),'steps':len(sol.t),'identity_error':(yf[0]-init[0])-(yf[7]+yf[8])})
    dX=rows[1]['X_nuc']-rows[0]['X_nuc']
    dw=rows[1]['weak_integral']-rows[0]['weak_integral'];dh=rows[1]['hadron_integral']-rows[0]['hadron_integral'];dcut=rows[1]['X_cut']-rows[0]['X_cut']
    assert abs(dX-(dcut+dw+dh))<3e-12
    assert abs(dX-c['delta_Xn_Tnuc'])<2e-10
    row={'map':mp,'dX_cut':dcut,'dI_weak':dw,'dI_hadron':dh,'dX_nuc':dX,'sum_error':dX-(dcut+dw+dh),'early_target_error':dX-c['delta_Xn_Tnuc'],'source_runs':rows}
    print('BUDGET',mp,row['dX_cut'],row['dI_weak'],row['dI_hadron'],row['dX_nuc'],row['sum_error'],flush=True)
    res.append(row)
(P/'postsource_fundamental_theorem_022.json').write_text(json.dumps({'cases':res,'guard':'conditional source perturbation; postsource weak vs hadron contributions, not physical causal identification'},indent=2))
with (P/'postsource_fundamental_theorem_022.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['map','dX_cut','dI_weak','dI_hadron','dX_nuc','sum_error','early_target_error']);w.writeheader();w.writerows({k:v for k,v in c.items() if k in w.fieldnames} for c in res)
```

## 3. `verify_cut_adjoint_and_controls_022.py`
SHA256 `00a99dcc85ec743c6e04216d8ced33513a8b00cee03ff070a75ca53221bd9aca`

```python
#!/usr/bin/env python3
"""Validate ROT022 nonlinear cutoff-state Shapley against ROT021 source-target cutoff adjoint,
and summarize independent thermo/baryon controls with explicit replay tolerances.
"""
import json, csv, pathlib, math
P=pathlib.Path(__file__).resolve().parent
main=json.loads((P/'postsource_memory_partition_022.json').read_text())['cases']
adj=json.loads((P/'causal_kernel_021.json').read_text())['cases']
extra=[]
for label,filename in [('chi_0_comoving','postsource_memory_thermal_chi0_022.json'),('chi_1_comoving','postsource_memory_thermal_chi1_022.json')]:
 for case in json.loads((P/filename).read_text()):extra.append({**case,'control':label})
results=[]
for c,a in zip(main,adj):
 assert c['map']==a['map']
 lam=a['adjoint_cut']; deltas=c['state_cut_delta']
 direct=lam[0]*deltas[0]
 memory=sum(x*y for x,y in zip(lam[1:],deltas[1:]))
 full=direct+memory
 assert abs(full-c['delta_Xn_Tnuc'])<5e-11
 assert abs(direct-c['two_group_shapley_X_cut'])<8e-12
 assert abs(memory-c['two_group_shapley_hadron_memory'])<8e-12
 data={
 'map':c['map'],'adjoint_X_cut_factor':lam[0],
 'linear_adjoint_direct':direct,'linear_adjoint_population_memory':memory,'linear_total':full,
 'full_nonlinear_total':c['delta_Xn_Tnuc'],'linear_vs_nonlinear':full-c['delta_Xn_Tnuc'],
 'nonlinear_shapley_direct':c['two_group_shapley_X_cut'],'nonlinear_shapley_memory':c['two_group_shapley_hadron_memory'],
 'mesons_4group':c['four_group_shapley'][1],
 'pbar_memory_4group':c['four_group_shapley'][2],
 'nbar_memory_4group':c['four_group_shapley'][3],
 }
 results.append(data)
rows=[]
for case in [*main,*extra]:
 rows.append({'map':case['map'],'chi_EM':case['chi_EM'],'baryons':case['baryons'],'rtol':case['rtol'],
 'delta_X_cut':case['delta_Xn_source_off'],'delta_X_nuc':case['delta_Xn_Tnuc'],
 'shapley_X_cut':case['two_group_shapley_X_cut'],'shapley_populations':case['two_group_shapley_hadron_memory'],
 'population_memory_pct':100*case['two_group_share_hadron_memory'],
 'cut_X_pct':100*case['two_group_share_X_cut'],
 'pbar_four_shapley':case['four_group_shapley'][2],
 'nbar_four_shapley':case['four_group_shapley'][3]})
assert len(rows)==6
assert all(2.2<r['population_memory_pct']<2.8 for r in rows)
(P/'postsource_state_adjoint_audit_022.json').write_text(json.dumps({'nominal_adjoint':results,'six_thermal_baryon_cases':rows,'interpretation':'Shapley state swaps and cutoff adjoint are alternative model-specific parameterizations of post-evap sensitivity'},indent=2))
with (P/'postsource_state_robustness_022.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
for r in results:print('ADJOINT',r['map'],r['linear_total'],r['linear_vs_nonlinear'],r['linear_adjoint_direct'],r['linear_adjoint_population_memory'])
for r in rows:print('ROBUSTNESS',r['map'],r['chi_EM'],r['baryons'],r['population_memory_pct'])
```