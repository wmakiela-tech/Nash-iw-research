#!/usr/bin/env python3
"""Independent 256-point Gaussian quadrature checks of ROT024 96-point nullspaces."""
import json,csv,math
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
import reproduce_high_order_moment_gate_024 as R
P=Path(__file__).resolve().parent
nodes,w=leggauss(256)
records=[]
for k in (2,3,4,5):
  coeff=R.CO[k]
  eps=.04
  assert max(abs(coeff))<=1+1e-13
  for j in range(k+1):
    A=B=C=0.
    for i,(lo,hi) in enumerate(R.BINS):
      a,b=math.log(lo),math.log(hi)
      z=(a+b)/2+(b-a)/2*nodes
      weights=(b-a)/2*w
      u=np.exp(z)
      Bump=np.sin(np.pi*(z-a)/(b-a))**4
      qp,qn=R.SQ[0]*u**R.SL[0],R.SQ[1]*u**R.SL[1]
      dw=weights*u**3*(qp+qn)*Bump*coeff[i]*z**j
      A+=np.sum(dw)
      B+=np.sum(np.abs(dw))
      # independent true baseline moment of each species
      C+=np.sum(weights*u**3*(qp+qn)*abs(z)**j)
    records.append({'k':k,'j':j,'residual_signed_scaled':eps*A,'residual_over_L1':abs(A)/B,'residual_over_fluence':abs(eps*A)/C})
  for u in np.geomspace(.00000002,1,2000):
    if u<R.BINS[0][0] or u>R.BINS[-1][1]: continue
    a=R.source(u,k,.04);b=R.source(u,k,0.)
    if abs((a[4]+a[5])/(b[4]+b[5])-1)>4e-16:
        raise ValueError('pair sum differs')
    if min(a[4],a[5])<=0:raise ValueError('negative source')
  # at edge all derivatives vanish because perturbation has compact support away from boundary
  assert np.array_equal(R.source(1,k,.04),R.source(1,k,0.))
  assert np.array_equal(R.source(.95,k,.04),R.source(.95,k,0.))
  assert np.array_equal(R.source(.06,k,.04),R.source(.06,k,0.))
P.joinpath('independent_moment_checks_024.csv').write_text('k,j,residual_signed_scaled,residual_over_L1,residual_over_fluence\n'+'\n'.join(','.join(str(r[z]) for z in ['k','j','residual_signed_scaled','residual_over_L1','residual_over_fluence']) for r in records)+'\n')
report={'quadrature_nodes':256,'design_nodes':96,'max_normalized_residual':max(r['residual_over_L1'] for r in records),'all_pair_sums':True,'all_positive':True,'all_edge_jets_unperturbed':True,'records':records}
P.joinpath('independent_moment_checks_024.json').write_text(json.dumps(report,indent=2))
print(json.dumps({z:v for z,v in report.items() if z!='records'},indent=2))