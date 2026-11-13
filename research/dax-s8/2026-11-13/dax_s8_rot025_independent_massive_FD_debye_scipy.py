#!/usr/bin/env python3
"""Independently coded SciPy massive QED e+-e- static response; no mpmath.
Numerical derivative in chemical potential and Bessel fugacity; not pion drag.
"""
from pathlib import Path
import json, math
from scipy.integrate import quad
from scipy.special import expit, kv
me=0.51099895069;T=0.07818527068831995; z=me/T
alpha=1/137.035999084;e2=4*math.pi*alpha
hc=1.973269804e-11
Epi=718277.1443978552;mpi=139.57039
# Dimensionful momentum integration in MeV instead of dimensionless q.
def f(p, mu):
    return expit((mu-math.hypot(p,me))/T)
ns=quad(lambda p:p*p*f(p,0),0,5.0,epsabs=1e-13,epsrel=2e-13,limit=200)[0]/math.pi**2/hc**3
chi=2/(math.pi**2*T)*quad(lambda p:p*p*f(p,0)*(1-f(p,0)),0,5.0,epsabs=1e-13,epsrel=2e-13)[0]
mD2=e2*chi;mD=math.sqrt(mD2)
# Different numerical path via actual finite perturbation in electron charge chemical potential.
chemical_shift=1e-4*T
rhocharge=lambda mu:quad(lambda p:p*p*(f(p,mu)-f(p,-mu)),0,5.0,epsabs=1e-14,epsrel=1e-13)[0]/math.pi**2
chi_finite=rhocharge(chemical_shift)/chemical_shift
# Independent convergent fugacity expression for massive FD susceptibility.
chi_bessel=2*me**2/math.pi**2*sum((-1)**(j+1)*kv(2,j*z) for j in range(1,13))
assert abs(chi/chi_bessel-1)<1e-12
assert abs(chi_finite/chi-1)<1e-7
spacing=(3/(4*math.pi*2*ns))**(1/3)
debye=hc/mD
output={
 'status':'PASS_INDEPENDENT_DIMENSIONFUL_SCIPY_AND_CHEMICAL_DIFFERENCE',
 'n_eplus_cm3':ns,'mD2_MeV2':mD2,'mD_MeV':mD,
 'debye_length_cm':debye,'debye_length_angstrom':debye*1e8,
 'debye_sphere_total_leptons':4*math.pi/3*2*ns*debye**3,
 'plasma_coupling_alpha_hbarc_over_aT':alpha*hc/(spacing*T),
 'susceptibility_fugacity_relative_residual':chi/chi_bessel-1,
 'susceptibility_finite_difference_relative_residual':chi_finite/chi-1,
 'massless_over_true_Debye_mass_ratio':math.sqrt(e2*T*T/3)/mD,
 'e_over_M2_divT':Epi/(mpi*mpi/T),
 'limits':'Ideal static longitudinal QED charge susceptibility. No complete gauge-safe hard/soft, transverse, dynamical pion stopping calculation.'
}
Path(__file__).parent.joinpath('results_independent.json').write_text(json.dumps(output,sort_keys=True,indent=2)+'\n')
print(json.dumps(output,indent=2,sort_keys=True))
