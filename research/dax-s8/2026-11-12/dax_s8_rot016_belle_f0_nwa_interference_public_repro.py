#!/usr/bin/env python3
"""DAX-S8 ROT016: source-fitted Belle f0 two-photon width, conditional NWA and interference.
Not Belle HEPData table replay, not full pion QCD, and not a physical PBH bound.
The full executed 65-dps original and distinct SciPy finite-width code are in the local ZIP.
"""
from mpmath import mp
import json
mp.dps=55
E=mp.mpf('1436554')
T=mp.mpf('0.07818527068831995')
M=mp.mpf('985.6')
Gamma_gg=mp.mpf('205')*mp.mpf('1e-6') # Belle fit eV -> MeV
mpi=mp.mpf('139.57039')
alpha=1/mp.mpf('137.035999084')
C=4*E*T
L=lambda y:-mp.log(-mp.expm1(-y))
H=lambda w:4*w**3*L(w*w/C)/C**2
# Point-scalar charged pion Born source model, NOT full QCD.
def born(s):
    if s<=4*mpi*mpi:return mp.mpf(0)
    b=mp.sqrt(1-4*mpi*mpi/s)
    return 2*mp.pi*alpha**2*b/s*(2-b*b-(1-b**4)*mp.atanh(b)/b)
a=4*mpi*mpi/C
K_B=mp.quad(lambda y:2*y*L(y)*born(C*y),[a,1,2,3,5,10,30,80,mp.inf])
# NWA spin-zero UNPOLARIZED resonance with B(pi+pi-)=1 reference.
K_R=4*mp.pi**2*Gamma_gg*H(M)/M**2
# Same NWA via Planck y-kernel and delta(s-M^2).
y0=M*M/C
K_R_alt=2*y0*L(y0)*8*mp.pi**2*Gamma_gg/(M*C)
assert abs(K_R-K_R_alt)<mp.mpf('1e-53')
assert abs(K_B/mp.mpf('9.0976176211836268e-10')-1)<mp.mpf('2e-16')
r=K_R/K_B
lower=(1-mp.sqrt(r))**2
upper=(1+mp.sqrt(r))**2
assert lower<1<upper
print(json.dumps({
  'status':'PASS_ORIGINAL_BELLE_FITTED_F0_NWA_AND_CONDITIONAL_CAUCHY',
  'source':'Belle Mori et al 2007, arxiv:hep-ex/0610038',
  'M_f0_MeV':'985.6','Gamma_gg_eV':'205',
  'K_Born_source':mp.nstr(K_B,30),
  'K_f0_NWA_Br1':mp.nstr(K_R,30),
  'isolated_f0_over_Born_Br1':mp.nstr(r,28),
  'Cauchy_model_min_over_Born':mp.nstr(lower,28),
  'Cauchy_model_max_over_Born':mp.nstr(upper,28),
  'boundary':'NWA and exactly two coherent amplitudes ONLY. Not full pion QCD rate or an experimental uncertainty band. HEPData/YODA numeric bytes NOT READ.'
},indent=2,sort_keys=True))
