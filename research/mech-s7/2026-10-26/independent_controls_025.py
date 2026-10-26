#!/usr/bin/env python3
"""Independent high-quadrature moment, positivity, pair sum, edge controls for ROT025."""
import csv, json
from pathlib import Path
import numpy as np
import reproduce_target_transfer_025 as t
D=Path(__file__).resolve().parent
out=[]
for k in t.DEGREES:
    q=t.independent_integral(k)
    u=np.geomspace(t.m.BINS[0][0], t.m.BINS[-1][1], 4001)
    worst_pair=0; smallest_fraction=1; max_abs_shape=0
    for eps in [-.15,.15]:
      for mass in u:
        qp,qn=t.m.SQ*mass**t.m.SL
        pair=qp+qn
        f=t.shape(mass,k)
        p1=qp+eps*pair*f;n1=qn-eps*pair*f
        worst_pair=max(worst_pair,abs(p1+n1-pair)/pair)
        smallest_fraction=min(smallest_fraction,p1/pair,n1/pair)
        max_abs_shape=max(max_abs_shape,abs(f))
    out.append({'k':k,'constraint_2norm':t.summary(k)['relative_constraint_residual'],
        'first_moment_max_relres_256':max(r['normalized_residual'] for r in q),
        'pointwise_pair_relative_residual':worst_pair,'min_channel_fraction_of_sum':smallest_fraction,
        'max_abs_shape':max_abs_shape,
        'linear_exec_response':t.summary(k)['linear_Bexec_derivative'],
        'linear_sym_response':t.summary(k)['linear_Bsym_derivative'],
        'coefficients':t.summary(k)['coeff'],
        'unmodified_at_edge': all(t.shape(v,k)==0 for v in (.921,.95,1.,1.01))})
    print('CONTROL',out[-1],flush=True)
(D/'independent_controls_025.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
with (D/'independent_controls_025.csv').open('w',newline='') as f:
    q=[{k:v for k,v in p.items() if k!='coefficients'} for p in out]
    w=csv.DictWriter(f,fieldnames=list(q[0]));w.writeheader();w.writerows(q)
if max(x['first_moment_max_relres_256'] for x in out)>1e-12:raise SystemExit('MOMENT_CHECK_FAIL')
if min(x['min_channel_fraction_of_sum'] for x in out)<=0:raise SystemExit('POSITIVITY_FAIL')
if max(abs(x['linear_exec_response']) for x in out)>1e-12:raise SystemExit('EXEC_TARGET_NULL_FAIL')
print('CONTROLS_PASS')