#!/usr/bin/env python3
"""DAX-S8 ROT014: exact universal R68 W-kernel peak and 5MeV H envelope.
No Belle raw numeric rows or physical hadronic QCD amplitude are used.
"""
import json
import mpmath as mp
mp.mp.dps=65
E=mp.mpf('1436554')
T=mp.mpf('0.07818527068831995')
C=4*E*T
def L(y):
    return -mp.log(-mp.expm1(-y))
def H(W):
    return W**3/(4*E**2*T**2)*L(W**2/C)
def f(y):
    return 3*L(y)-2*y/mp.expm1(y)
y0=mp.findroot(f,(mp.mpf(1),mp.mpf(2)))
W0=mp.sqrt(C*y0)
assert abs(f(y0))<mp.mpf('1e-60')
assert W0<800
bin_ratios=[]
for i in range(140):
    lo=mp.mpf(800+5*i)
    hi=lo+5
    assert H(lo)>H(hi)>0
    bin_ratios.append(H(lo)/H(hi))
maximum=max(bin_ratios)
assert mp.mpf('1.0237')<maximum<mp.mpf('1.0238')
# Constant-sigma threshold test of exact incoming-angle/Planck reduction.
m_pi=mp.mpf('139.57039')
a=(2*m_pi)**2/C
original=mp.quad(lambda x: x*x/mp.expm1(x)*(1-(a/x)**2),[a,1,3,10,40,mp.inf])
reduced=mp.quad(lambda z:2*z*L(z),[a,1,3,10,40,mp.inf])
assert abs(original-reduced)<mp.mpf('1e-59')
print(json.dumps({
 'status':'PASS_ANALYTIC_PLANCK_W_MODE_AND_BIN_ENVELOPE',
 'W_mode_MeV':mp.nstr(W0,52),
 'mode_dimensionless_y':mp.nstr(y0,52),
 'H_800_over_H_peak':mp.nstr(H(800)/H(W0),30),
 'max_5MeV_H_left_to_right':mp.nstr(maximum,34),
 'constant_sigma_flux_check':mp.nstr(reduced,35),
 'scope':'Kernel per LINEAR dW; real Belle Table 1 numeric rows inaccessible; a point-sampled cross section is NOT a bin area; NO physical pion rate.'
},indent=2,sort_keys=True))
