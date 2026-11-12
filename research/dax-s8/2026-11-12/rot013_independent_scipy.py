#!/usr/bin/env python3
"""DAX-S8 ROT013 independent direct Eq21 angular integration using SciPy.
Does not import exact-primitive script; not a QCD amplitude or data fit.
"""
from scipy.integrate import quad
from math import sqrt,pi,atanh,log,expm1
import json
from pathlib import Path
E=1436554.0;T=.07818527068831995;mp=139.57039;alpha=1/137.035999084
C=4*E*T
y0=4*mp*mp/C;y1=800**2/C;y2=1500**2/C

def dsdz(s,z):
    if s<=4*mp*mp:return 0.
    b=sqrt(1-4*mp*mp/s);B=b*b
    k=((1-B)/(1-B*z*z))**2 + (B*(1-z*z)/(1-B*z*z))**2
    return pi*alpha*alpha*b/s*k

def dtheta(s,zlim):
    # Integrate original angular formula, NOT closed source primitive.
    return 2*quad(lambda z:dsdz(s,z),0,zlim,epsabs=1e-22,epsrel=4e-11,limit=200)[0]

def f(y,zlim):
    if y<=y0:return 0.
    return 2*y*(-log(-expm1(-y)))*dtheta(C*y,zlim)*1e12

def K(a,b,zlim):
    pts=[a]+[v for v in [0.3,0.5,1.0,1.5,2,3,4,5,8,12,18,30] if a<v<b]+[b]
    return sum(quad(lambda y:f(y,zlim),lo,hi,epsabs=3e-10,epsrel=1e-9,limit=200)[0] for lo,hi in zip(pts,pts[1:]))/1e12
allrate=K(y0,120,1.0)
left=K(y0,y1,1.0)
mid=K(y1,y2,1.0)
right=K(y2,120,1.0)
fid=K(y1,y2,0.6)
assert abs((left+mid+right)/allrate-1)<1e-7
assert abs(allrate/9.0976176211836268e-10-1)<3e-7
res={
 'status':'PASS_INDEPENDENT_2D_EQ21_INTEGRATION',
 'method':'scipy 1D Planck-energy convolution over independently numerically integrated original Eq21 pion scattering angle',
 'K_all':allrate,'K_below_0p8':left,'K_W0p8_to_1p5':mid,'K_above_1p5':right,
 'K_Belle_fiducial':fid,
 'fraction_below_0p8':left/allrate,
 'fraction_W0p8_to_1p5':mid/allrate,
 'fraction_above_1p5':right/allrate,
 'fraction_Belle_fiducial':fid/allrate,
 'scope':'Model-derived Born only, not Belle physical data or full QCD rate.'}
print(json.dumps(res,indent=2,sort_keys=True))
(Path(__file__).parent/'results_scipy.json').write_text(json.dumps(res,indent=2,sort_keys=True)+'\n')
