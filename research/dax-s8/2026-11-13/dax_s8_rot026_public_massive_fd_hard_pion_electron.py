#!/usr/bin/env python3
"""DAX-S8 ROT026 PUBLIC finite-Q² vacuum Born pion/e± hard-transfer model.
Requires numpy. Source-frozen representative Eπ from Belle/Rivet ROT020 and
ideal massive e± FD number density from ROT024; no full medium stopping.
"""
import json, math
import numpy as np
from numpy.polynomial.legendre import leggauss
A=1/137.035999084;M=.13957039;m=.00051099895069
T=.00007818527068831995;E=718.2771443978551975
p=math.sqrt(E**2-M*M);v=p/E
n_pair=4.9953665820687041e26 # cm^-3, inherited ROT024
hbarc=.00000000000001973269804 # GeV cm
q2lo=.001;q2hi=.010
qnode,qweight=leggauss(80);anode,aweight=leggauss(60)
q=16*(1+qnode);eps=np.hypot(q*T,m)
fermion=np.exp(-eps/T)/(1+np.exp(-eps/T))
weights=16*qweight*q*q*fermion
weights=weights/np.sum(weights)
rate=loss=0.
for qi,ei,wi in zip(q,eps,weights):
    ki=qi*T
    for mu,wa in zip(anode,aweight):
        s=M*M+m*m+2*(E*ei-p*ki*mu)
        lam=(s-(M+m)**2)*(s-(M-m)**2)
        upper=min(q2hi,lam/s)
        if upper<=q2lo:continue
        a=s-M*M-m*m;b=s-m*m
        flux=math.sqrt(lam)/(2*p*ei)
        ds=4*math.pi*A*A/lam*(a*a*(1/q2lo-1/upper)-b*math.log(upper/q2lo))
        gain_per_q2=((E+ei)*(s+m*m-M*M)-2*s*ei)/lam
        dg=4*math.pi*A*A/lam*gain_per_q2*(a*a*math.log(upper/q2lo)-b*(upper-q2lo))
        rate+=wi*wa/2*flux*ds
        loss+=wi*wa/2*flux*dg
rate_cm=rate*n_pair*hbarc*hbarc
loss_cm=loss*n_pair*hbarc*hbarc
assert abs(loss_cm-0.23581945614011515)<1e-12
print(json.dumps({'status':'PASS_DEFINED_ONE_PHOTON_VACUUM_TREE_HARD_SLICE_ONLY',
  'n_eplus_eminus_cm3':n_pair,'Q2_window_GeV2':[q2lo,q2hi],
  'pion_lab_E_GeV':E,'incident_elastic_events_per_cm':rate_cm,
  'mean_transfer_per_scatter_GeV':loss/rate,
  'local_hard_sector_loss_GeV_per_cm':loss_cm,
  'local_hard_sector_loss_length_m':E/loss_cm/100,
  'scope':'NOT full gauge-safe finite-T pion stopping, no pion cascade, neutrinos or BBN result; pion form factor F_pi=1 idealized.'},indent=2,sort_keys=True))
