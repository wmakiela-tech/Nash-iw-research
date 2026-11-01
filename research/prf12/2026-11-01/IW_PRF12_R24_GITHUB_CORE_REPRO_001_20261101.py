#!/usr/bin/env python3
"""R24 independent NumPy/SciPy core. Full script and 2x2/4x4 audit in ZIP.
Inherits R23 globally certified source-ON rectangle pA>=.576, pB<=.526;
ideal Z-QND measurement wait, symmetric independent label flips.
"""
import math
import numpy as np
from scipy.stats import binom
w=(.18,.20,.62);omega=10.;tp=math.pi/(2*omega)
td=tr=.05;Delta=.5
span=2*(Delta+2*tp+td)+tr
wall=2*(Delta+2*tp+td+tr)
def mz(xi):
 u=xi/omega
 return (u*u+math.cos(math.pi/2*math.sqrt(1+u*u)))/(1+u*u)
for xi in np.linspace(-500,500,20001):assert mz(xi)>-3e-15
floor=(1-w[0]-w[1])/2
assert abs(floor-.31)<1e-14
def bound(eta,lam,f=0):
 s=math.exp(-lam*span); c=(1-2*eta)**2
 return .5+c*(s*.576+(1-s)*f-.5),.5+c*(.526-.5)
def sample(a,b):
 if a<=b:return None
 v=math.log(a/b);u=math.log((1-b)/(1-a))
 for n in range(1,30000):
  k=math.ceil(n*u/(u+v)-1e-12)
  ea=binom.cdf(k-1,n,a);eb=binom.sf(k-1,n,b)
  if max(ea,eb)<.05:return n,k,ea,eb
 raise ValueError('N threshold exceeded')
for eta,lam,f,n0 in [(0,0,0,1075),(.01,0,0,1170),(.01,.01,0,1835),
(.01,.02,0,3277),(.01,.04,0,26775),(.01,.04,.31,2907)]:
 a,b=bound(eta,lam,f);n,k,ea,eb=sample(a,b)
 assert n==n0
 print('eta',eta,'lambda/gamma',lam,'floor',f,'A>=',a,'B<=',b,
       'N',n,'K',k,'errors<=',(ea,eb),'wall_gammaT<=',n*wall)
print('R24 PASS; no full continuous readout or three-probe LOCC claim')
