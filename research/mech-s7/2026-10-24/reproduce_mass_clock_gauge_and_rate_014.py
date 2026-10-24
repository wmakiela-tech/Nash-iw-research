#!/usr/bin/env python3
"""MECH-S7 ROT014: source-informed conditional preedge bridge clock-gauge and rate-stress controls.

Distinguishes a consistent translation of absolute clock labels from a perturbation
of the PBH cubic mass-loss rate. THIS IS NOT the original Julia 10D solver.
Requires ROT013 archive files adjacent and two original source archive ZIPs.
"""
from pathlib import Path
import importlib.util, json, csv, math, time, copy
import numpy as np
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parent

def mod(path,name):
    sp=importlib.util.spec_from_file_location(name,str(path))
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
bridge=mod(ROOT/'edge_bridge_013.py','bridge14')
base=bridge.base=bridge.module(bridge.BASE,'base14')
model=bridge.host_wrapper_setup(bridge.module(bridge.SCRIPT,'mori14'))
raw=base.load(bridge.PUB,bridge.PAP)
orig=model.contexts(base,bridge.PUB,bridge.PAP)
eos=model.eos_table()
G0=base.GAMMA;E0=base.DT_EDGE
M0=float(raw['public_exec'].iloc[1469].m_PBH_g)
t0=float(raw['public_exec'].iloc[1469].t_sec)
tglobal=float(orig['tedge'])
tlast=t0+(M0**3-base.M_EDGE**3)/G0
CLOCK_DRIFT=tlast-tglobal
assert abs(CLOCK_DRIFT-0.0984049264)<1e-6

# Tolerance: tight state differences expected < 1e-10 on X values when clock fully translated.
rows=[]; roots=[]; provenance=[]
chi=.5
start=time.time()
def run_case(gamma_ratio,whichmap,clockshift=0.,tol=3e-8):
    b=bridge.run_bridge(base,model,raw,eos,chi,whichmap,False,rtol=tol)
    b['t_edge_direct'] += clockshift
    ctx=bridge.shifted_ctx(orig,b,whichmap)
    host=model.prepare_host(base,ctx,eos,chi,rtol=2e-10)
    results={}
    for law in ('public','paper'):
        r=model.evolve(base,ctx,eos,host,whichmap,law,conserve=False,rtol=tol)
        results[law]=r
    return b,ctx,host,results

for scale in (1.,.99,1.01):
    base.GAMMA=G0*scale
    base.DT_EDGE=base.M_EDGE**3/base.GAMMA
    for mp in ('exec','sym'):
        br,ctx,host,r=run_case(scale,mp)
        d=r['paper']['X_nuc']-r['public']['X_nuc']
        row={'gamma_ratio':scale,'map':mp,'clock_variant':'last-row-absolute','clock_shift_s':0.,
             't_edge_s':ctx['tedge'],'t_nuc_s':host['Tnuc_time'],'T_edge_MeV':br['Tedge'],
             'X_edge':br['Xedge'],'X_public':r['public']['X_nuc'],'X_paper':r['paper']['X_nuc'],
             'deltaX':d,'bridge_steps':br['steps']}
        rows.append(row)
        print('RATE',scale,mp,'deltaX',d,'Xedge',br['Xedge'],'tedge',ctx['tedge'],'time',round(time.time()-start,1),flush=True)
        if scale==1.:
            # Clock translation shifts both the end of the PBH bridge and every event
            # in host/kinetics. No new physics should result.
            for shift in (-CLOCK_DRIFT,CLOCK_DRIFT):
                br2,ctx2,h2,r2=run_case(scale,mp,shift)
                d2=r2['paper']['X_nuc']-r2['public']['X_nuc']
                rows.append({'gamma_ratio':scale,'map':mp,'clock_variant':'consistent-translation',
                      'clock_shift_s':shift,'t_edge_s':ctx2['tedge'],'t_nuc_s':h2['Tnuc_time'],
                      'T_edge_MeV':br2['Tedge'],'X_edge':br2['Xedge'],
                      'X_public':r2['public']['X_nuc'],'X_paper':r2['paper']['X_nuc'],
                      'deltaX':d2,'bridge_steps':br2['steps']})
                print('TRANSLATE',mp,'dt',shift,'ΔX_abs_error',d2-d,'X_public_error',r2['public']['X_nuc']-r['public']['X_nuc'],flush=True)
    # orig is internally anchored with initial m6e9 mass, but for altered gamma
    # this is not an internally consistent initial-to-last archived trajectory.
base.GAMMA=G0;base.DT_EDGE=E0

# The clock translation invariance of any paper-vs-public spectral root follows
# from the identical autonomous shifted trajectory equations. Historical
# ROT013 spectral roots are read from pinned archived JSON separately in report.

out={'clock_translation_s':CLOCK_DRIFT,'mass_rate_g3_s':G0,'upstream_source':'Wu-Xu d395183674cace6c9906a8911bdeb7234ba4040d',
     'source_archive_csv_numbering':'CSV i begins 1, iloc zero-indexed; last active iloc1469 (i=1470)',
     'crossing_absolute_formation_anchor_s':tglobal,'crossing_last_saved_anchor_s':tlast,
     'results':rows,'spectral_roots':roots,
     'limitations':'conditional synthetic preedge bridge + 7D, no native 10D Julia; gamma variation is artificial stress not physical uncertainty; anchor shift is a time-origin gauge only when all times and histories moved jointly'}
(ROOT/'mass_clock_rate_014.json').write_text(json.dumps(out,indent=2,ensure_ascii=False))
with (ROOT/'mass_clock_rate_014.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
print('DONE',len(rows),round(time.time()-start,1),flush=True)