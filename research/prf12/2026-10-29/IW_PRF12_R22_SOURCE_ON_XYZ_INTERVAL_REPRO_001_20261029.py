#!/usr/bin/env python3
"""R22 compact code: interval-grid + analytic large-|xi| and numerical Lindblad.
Full rigorous B Taylor with certified remainder & independent 2x2/4x4 audit
are in the R22 ZIP. Source A keeps xi fixed WITHIN each two-shot pair.
No detector SPAM, arbitrary hardware, or original 3-qubit LOCC closure claim.
Requires mpmath, numpy, scipy.
"""
import math
import numpy as np
import mpmath as mp
from scipy.linalg import expm
from scipy.stats import binom
iv=mp.iv;iv.dps=40
z=iv.mpf(0);one=iv.mpf(1);omega=iv.mpf(10);t=iv.pi/20;q=iv.mpf('0.5')
def dot(a,b):return sum((a[j]*b[j] for j in range(3)),z)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def rot(v,xi,ax,ay,duration):
 r=iv.sqrt(xi*xi+ax*ax+ay*ay)
 n=(ax/r,ay/r,xi/r);c=iv.cos(r*duration);s=iv.sin(r*duration)
 w=cross(n,v);p=dot(n,v)
 return tuple(c*v[j]+s*w[j]+(one-c)*n[j]*p for j in range(3))
def pA(xi):
 v=rot((z,z,one),xi,z,omega,t)
 c=iv.cos(xi*q);s=iv.sin(xi*q)
 v=(c*v[0]-s*v[1],s*v[0]+c*v[1],v[2])
 mx=rot(v,xi,z,-omega,t)[2]
 my=rot(v,xi,omega,z,t)[2]
 return iv.mpf('0.5')+(mx*mx+my*my+v[2]*v[2])/6
def pB_float():
 ex=np.array([1.,0.,0.]);ey=np.array([0.,1.,0.]);ez=np.array([0.,0.,1.])
 D=np.diag([1.,1.,0.])
 def cr(a):return np.array([[0.,-a[2],a[1]],[a[2],0.,-a[0]],[-a[1],a[0],0.]])
 dt=math.pi/20
 v=expm(dt*(cr(10*ey)-D))@ez
 v=expm(-.5*D)@v
 mx=(expm(dt*(cr(-10*ey)-D))@v)[2]
 my=(expm(dt*(cr(10*ex)-D))@v)[2]
 return .5+(mx*mx+my*my+v[2]**2)/6
lo=1
for j in range(3501):
 p=pA(iv.mpf(-35)+iv.mpf(j)/50)
 lo=min(lo,float(p.a))
assert lo>.5835
L=.5+math.pi/10
assert L<.815
compact_lower=.5835-.815*.01
v2=100/(35**2+100)
tail_lower=.5+(2*(1-8*v2)**2+(1-2*v2)**2)/6
b=pB_float()
assert compact_lower>.5753 and tail_lower>.6724 and b<.546
a0=.5753;b0=.546;N=3300;k=1851
errA=binom.cdf(k-1,N,a0);errB=binom.sf(k-1,N,b0)
assert max(errA,errB)<.05
print('PASS R22 A uniform lower',min(compact_lower,tail_lower),
      'B numerical',b,'gap safe',a0-b0)
print('N',N,'threshold',k,'conditional error bounds',errA,errB)
print('Full B rigorous 65th-Taylor remainder and independent density check: ZIP.')
