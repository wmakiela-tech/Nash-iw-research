#!/usr/bin/env python3
"""DAX-S8 ROT012: source-typed 4-channel Born-pion first-event test.
Requires Python>=3.10, mpmath>=1.3.0. Not a physical hadronic rate.
"""
import mpmath as m
import json
m.mp.dps=48
E=m.mpf('1436554');T=m.mpf('0.07818527068831995')
a=1/m.mpf('137.035999084')
me=m.mpf('0.51099895'); mm=m.mpf('105.6583755')
mp=m.mpf('139.57039'); C=4*E*T
dpp0=a**4*(175*m.zeta(3)-38)/(36*m.pi*me**2)
def bw(s,mass):
    b=m.sqrt(1-4*mass**2/s)
    return 2*m.pi*a*a/s*((3-b**4)*2*m.atanh(b)-2*b*(2-b**2))
def piborn(s):
    if s<=4*mp**2: return m.mpf('0')
    b=m.sqrt(1-4*mp**2/s)
    return 2*m.pi*a*a*b/s*(2-b*b-(1-b**4)*m.atanh(b)/b)
def integral(fn,mass):
    y0=4*mass*mass/C
    pts=[y0]+[m.mpf(z) for z in (1,3,10,30,80) if z>y0]
    return m.quad(lambda y:2*y*(-m.log(-m.expm1(-y)))*fn(C*y),pts)
R_e=integral(lambda s:bw(s,me),me)
R_mu=integral(lambda s:bw(s,mm),mm)
R_pi=integral(piborn,mp)
R_dpp=integral(lambda s:dpp0,2*me)
p3=R_mu/(R_e+R_mu+R_dpp)
p4=R_mu/(R_e+R_mu+R_dpp+R_pi)
assert m.mpf('.08649')<p3<m.mpf('.08650')
assert m.mpf('.08577')<p4<m.mpf('.08579')
assert m.mpf('.0964')<R_pi/R_mu<m.mpf('.0965')
print(json.dumps({
 'status':'PASS_CONDITIONAL_SOURCE_MODEL',
 'kernel_BW_e':m.nstr(R_e,29),
 'kernel_BW_mu':m.nstr(R_mu,29),
 'kernel_DPP_asymptotic':m.nstr(R_dpp,29),
 'kernel_charged_pion_Born':m.nstr(R_pi,29),
 'P_first_mu_3channel':m.nstr(p3,29),
 'P_first_mu_4channel_Born':m.nstr(p4,29),
 'relative_drop':m.nstr(1-p4/p3,29),
 'pion_Born_to_muon_BW_ratio':m.nstr(R_pi/R_mu,29),
 'scope':'Not full pion QCD, SM completeness, final muon/neutrino yield, or PBH/BBN'
},indent=2,sort_keys=True))
