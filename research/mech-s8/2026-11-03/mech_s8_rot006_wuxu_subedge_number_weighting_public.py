#!/usr/bin/env python3
"""Mech-S8 ROT006: Wu-Xu conditional hadron NUMBER emission weighting.
Python 3 standard library. NOT BlackHawk/Julia/BBN, NO physical bound.
Upstream pinned d395183674cace6c9906a8911bdeb7234ba4040d;
table Git blob 06d0883a27b108692720422294ba2baacd381a64.
Paper JCAP 02(2026)063 section 4.1: T_H^1.3; shipped v3 scan
tool_script-hadrons_from_PBH.jl uses log-linear first-interval slope.
"""
import json,math
NAMES=['pions_pm','kaons_pm','K0L','proton_antiproton','neutron_antineutron']
R=[
 [5.609588603804452e32,489105.5126008581,59105.93631247951,29086.774913348447,34849.08026691193,34656.17773724596],
 [6.099798045788406e32,442306.73787501804,53467.712852971126,26311.795859614824,31504.591028094237,31328.963561830213]]
x100=1.057261195158e8/1e9
def numfactor(p,x): return (1-x**(3-p))/(3-p)
def simpson(p,n=4096):
 def f(t):return 4*t**(4*(3-p)-1) if t else 0.
 h=1/n
 return h/3*(f(0)+f(1)+4*sum(f(k*h) for k in range(1,n,2))
     +2*sum(f(k*h) for k in range(2,n-1,2)))
out=[]
for j,name in enumerate(NAMES,1):
 p=-math.log(R[1][j]/R[0][j])/math.log(R[1][0]/R[0][0])
 exact=numfactor(p,0)
 check=simpson(p)
 assert abs(check-exact)<3e-12
 out.append(dict(channel=name,p_code=p,
   paper_over_code_total_subedge_number=exact**-1/1.7,
   paper_relative_increase_total_subedge_number=(3-p)/1.7-1,
   scan_over_paper_before_100tev_mass=numfactor(p,x100)/numfactor(1.3,x100),
   scan_number_fraction_after_100tev_mass=x100**(3-p),
   paper_number_fraction_after_100tev_mass=x100**1.7,
   independent_simpson_abs_err=abs(check-exact)))
print(json.dumps(dict(source='WuXu d395183 pinned first 2 rows',
 assumption='dM/dt=-K/M^2, rate boundary-matched M^-p, formal M_end->0',
 claim='CONDITIONAL_HADRON_NUMBER_ONLY/NO_BBN/NO_PBH_BOUND/NO_CANON/NO_EXEC_SIGN',
 results=out),indent=2))
