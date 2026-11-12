#!/usr/bin/env python3
"""DAX-S8 ROT013. Exact angular primitive + high precision Planck-rate integrals.
Only point-scalar charged-pion Born; Belle W and angle fiducial support.
No experimental cross-section numeric rows imported. Not a physical cross-section bound.
"""
import json
from pathlib import Path
import mpmath as mp
mp.mp.dps=48
M=mp.mpf('139.57039');E=mp.mpf('1436554');T=mp.mpf('0.07818527068831995')
alpha=1/mp.mpf('137.035999084');C=4*E*T
low=2*M; wmin=mp.mpf(800); wmax=mp.mpf(1500); zfid=mp.mpf('0.6')

def angle_primitive(beta,z):
    b2=beta*beta
    # Integral_0^z [(1-b²)^2+b^4*(1-x²)^2]/(1-b²*x²)^2 dx.
    # This is equivalent to source dσ/dΩ of Klevansky et al Eq.21.
    if beta==0: return z
    return z + (1-b2)**2*z/(1-b2*z*z) - (1-b2*b2)*mp.atanh(beta*z)/beta

def born(s,z=mp.mpf(1)):
    if s<=4*M*M:return mp.mpf(0)
    beta=mp.sqrt(1-4*M*M/s)
    return 2*mp.pi*alpha*alpha*beta/s *angle_primitive(beta,z)

def kern(y,z=mp.mpf(1)):
    return 2*y*(-mp.log(-mp.expm1(-y)))*born(C*y,z)

def integration(y1,y2,z=mp.mpf(1)):
    # Split at fixed W scales, avoid branch and slow near-threshold quadrature.
    cuts=sorted(set([y1,y2]+[mp.mpf(v)*mp.mpf(v)/C for v in
       ['300','350','450','600','800','1000','1200','1500','2000','3000'] if y1<mp.mpf(v)*mp.mpf(v)/C<y2]+[mp.mpf(t) for t in [1,2,3,5,10,25,60] if y1<t<y2]))
    return sum((mp.quad(lambda y:kern(y,z),[a,b]) for a,b in zip(cuts,cuts[1:])),mp.mpf(0))

y0=4*M*M/C
ya=wmin*wmin/C; yb=wmax*wmax/C
# The y>120 Planck tail is negligible in declared precision; verify upper bound separately.
ymax=mp.mpf(120)
allrate=integration(y0,ymax)
lowrate=integration(y0,ya)
midrate=integration(ya,yb)
highrate=integration(yb,ymax)
fidrate=integration(ya,yb,zfid)
assert mp.almosteq(allrate,lowrate+midrate+highrate,rel_eps=mp.mpf('1e-35'))
assert fidrate<midrate<allrate
# Pointwise identity verified independently by differentiating closed primitive.
for w in [300,400,644,800,1000,1500,3000]:
 s=mp.mpf(w)**2
 be=mp.sqrt(1-4*M*M/s)
 b2=be*be
 z=mp.mpf('0.37')
 source = ((1-b2)/(1-b2*z*z))**2+(b2*(1-z*z)/(1-b2*z*z))**2
 assert abs(mp.diff(lambda t: angle_primitive(be,t),z)-source) < mp.mpf('1e-43')
# Analytic lower/upper bound of tail neglected after y=120:
# sigma_Born <= 4*pi*alpha^2/s crude bound from I(1)<=2 and beta<=1;
# -log(1-exp(-y)) <= exp(-y)/(1-exp(-120)), integration from 120.
# With s=C*y, kernel <= [8*pi*alpha^2/C]*exp(-y)/(1-exp(-120)).
error_upper=(8*mp.pi*alpha*alpha/C)*mp.exp(-ymax)/(1-mp.exp(-ymax))
assert error_upper<mp.mpf('1e-55')
props={
 'status':'PASS_EXACT_ANGULAR_PRIMITIVE_AND_PLANCK_COVERAGE',
 'model':'Klevansky_Lemmer_Beygi_2025_point_scalar_charged_pion_Born',
 'R68_E_gamma_MeV':mp.nstr(E,50), 'R68_T_gamma_MeV':mp.nstr(T,50),
 'm_pi_MeV':mp.nstr(M,50),
 'Belle_W_GeV':['0.8','1.5'], 'Belle_abs_cos_theta_max':'0.6',
 'rate_total':mp.nstr(allrate,42),
 'rate_below_Belle_0.8GeV':mp.nstr(lowrate,42),
 'rate_in_Belle_energy_only':mp.nstr(midrate,42),
 'rate_above_Belle_1.5GeV':mp.nstr(highrate,42),
 'rate_in_Belle_energy_and_angular':mp.nstr(fidrate,42),
 'fraction_below_0.8':mp.nstr(lowrate/allrate,38),
 'fraction_0.8_to_1.5_inclusive_angle':mp.nstr(midrate/allrate,38),
 'fraction_above_1.5':mp.nstr(highrate/allrate,38),
 'fraction_Belle_joint_fiducial':mp.nstr(fidrate/allrate,38),
 'fraction_outside_Belle_joint_fiducial':mp.nstr(1-fidrate/allrate,38),
 'fraction_Belle_angular_given_energy':mp.nstr(fidrate/midrate,38),
 'ratio_total_over_fiducial_Born':mp.nstr(allrate/fidrate,38),
 'tail_y120_absolute_upper':mp.nstr(error_upper,20),
 'source_data_status':'Belle HEPData DOI and tables located, raw table numerical payload NOT OPENED',
 'limits':'Born SOURCE MODEL COVERAGE ONLY; no measured physical rate, FSI, full hadronic channel, neutrino yield, deposition, PBH/BBN bound'
}
print(json.dumps(props,indent=2,ensure_ascii=False,sort_keys=True))
if __name__=='__main__':
 (Path(__file__).parent/'results_exact.json').write_text(json.dumps(props,indent=2,ensure_ascii=False,sort_keys=True)+'\n')
