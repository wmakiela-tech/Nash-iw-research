#!/usr/bin/env python3
"""Executed full kinetic sign-root for sym map only, source-pinned reduced 10+7D.
Exact comoving zero-th moment and Bexec linear target moment preserved; no physical claim.
"""
from __future__ import annotations
import math,json,csv,time,os
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import reproduce_high_order_moment_gate_024 as m
import reproduce_target_transfer_025 as t
P=Path(__file__).resolve().parent
start=time.time();tol=float(os.environ.get('ROT025_RTOL','3e-9'));mp='sym'
raw=m.base.load(m.old.PUB,m.old.PAP)
orig=m.mod.contexts(m.base,m.old.PUB,m.old.PAP)
eos=m.mod.eos_table();br=m.bridge.run_bridge(m.base,m.mod,raw,eos,.5,mp,conserve_from_saved=False,rtol=tol)
ctx=m.bridge.shifted_ctx(orig,br,mp)
host=m.mod.prepare_host(m.base,ctx,eos,.5,rtol=2e-10)
paper=m.old.evolve_law(ctx,eos,host,mp,law='paper',rtol=tol,conserve=False)['X_nuc']
public=m.old.evolve_law(ctx,eos,host,mp,law='public',rtol=tol,conserve=False)['X_nuc']
df=ctx['maps'][mp]
y0=np.r_[float(df.Xn.iloc[1469]),np.array([float(df[f'n_{sp}_cm3'].iloc[1469]) for sp in m.base.SPECIES])/m.base.NSCALE]
factors=np.array([.5,.5,.5,1,.5,.5])

def dyn(y,T):
    X=y[0];n=y[1:]
    D,a,b,weak=m.base.rates(X,T,baryon_scale=1.)
    c=np.sum(n*m.base.NSCALE*m.base.SIGMA_V_UNIT*((1-X)*a-X*b))
    return weak+c,D

def active(u,y,epsilon):
    T=host['pre_T'](u);logA=host['pre_lna'](u);dX,D=dyn(y,T)
    nPBH=ctx['nedge']*math.exp(-3*logA)
    src=t.source(u,0,epsilon)*factors*nPBH/m.mod.HBAR_GEV_SEC/m.base.NSCALE
    return -3*m.base.DT_EDGE*u*u*np.r_[dX,src-D*y[1:]]

def post(ti,y):
    dX,D=dyn(y,host['post_T'](ti));return np.r_[dX,-D*y[1:]]

values=[]
def f(epsilon):
    a=solve_ivp(lambda u,y:active(u,y,epsilon),(1.,m.base.U_CUT),y0,method='Radau',rtol=tol,atol=tol*1e-3,max_step=.004)
    if not a.success:raise RuntimeError(a.message)
    b=solve_ivp(post,(ctx['tcut'],host['Tnuc_time']),a.y[:,-1],method='Radau',rtol=tol,atol=tol*1e-3,max_step=2.)
    if not b.success:raise RuntimeError(b.message)
    rec={'epsilon':epsilon,'Xnuc_modified_public':float(b.y[0,-1]),'Xnuc_paper':float(paper),'paper_minus_modified':float(paper-b.y[0,-1]),'steps':len(a.t)+len(b.t)}
    values.append(rec);print('ROOT_EVAL',rec,flush=True)
    return rec['paper_minus_modified']

lo,hi=(.094,.097) if tol<3e-9 else (.0,.15)
v0=f(lo);v1=f(hi)
assert v0>0>v1,(v0,v1)
root=brentq(f,lo,hi,xtol=1e-9,rtol=1e-10)
res={'root_epsilon':root,'root_last_residual':values[-1]['paper_minus_modified'],
    'X_paper':float(paper),'X_public_original':float(public),'baseline_sym_paper_minus_public':float(paper-public),
    'executed_evaluations':values,'source_moments_preserved':{'degree_zero_both_species':True,'Bexec_target_first_derivative':True},
    'elapsed_seconds':time.time()-start,'rtol':tol,
    'guard':'REDUCED_CONDITIONAL_10COMP_PLUS_7D_NO_ORIGINAL_JULIA_NO_PHYSICAL_BBN_NO_PBH_BOUND'}
(P/('tight_sym_sign_root_025.json' if tol<3e-9 else 'sym_sign_root_025.json')).write_text(json.dumps(res,indent=2),encoding='utf-8')
with (P/('tight_sym_sign_root_025.csv' if tol<3e-9 else 'sym_sign_root_025.csv')).open('w',newline='') as fcsv:
    wr=csv.DictWriter(fcsv,fieldnames=list(values[0]));wr.writeheader();wr.writerows(values)
print('ROOT_FINAL',json.dumps({'root':root,'residual':values[-1]['paper_minus_modified'],'Xpaper':paper,'Xpub':public,'evals':len(values)}),flush=True)