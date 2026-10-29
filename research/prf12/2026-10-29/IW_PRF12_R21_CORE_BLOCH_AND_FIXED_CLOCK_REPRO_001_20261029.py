#!/usr/bin/env python3
"""PRF12 R21 core, numpy scipy; full independent density audit in ZIP.
A static xi during BOTH shots; B independent Levy noise. No original LOCC gap.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.stats import binom
from scipy.optimize import brentq,minimize_scalar
z=np.array([0.,0.,1.]);y=np.array([0.,1.,0.]);x=np.array([1.,0.,0.])
D=np.diag([1.,1.,0.])
def cross(v):return np.array([[0,-v[2],v[1]],[v[2],0,-v[0]],[-v[1],v[0],0.]])
def step(v,xi,axis,drive,t,src):
 m=cross(xi*z+drive*axis) if src=='A' else cross(drive*axis)-D
 return expm(t*m)@v
def active(q,omega,xi=0,src='A'):
 t=math.pi/(2*omega);r=step(z,xi,y,omega,t,src)
 r=step(r,xi,z,0,q,src)
 xx=step(r,xi,y,-omega,t,src)[2]
 yy=step(r,xi,x,omega,t,src)[2]
 return .5+(xx**2+yy**2)/4
def purity(q,omega,idle=.05):
 t=math.pi/(2*omega);r=step(z,0,y,omega,t,'B')
 r=step(r,0,z,0,q+idle,'B')
 return 2/3,.5+float(r@r)/6
def counts(a,b):
 u=math.log(a/b);v=math.log((1-b)/(1-a))
 for n in range(1,600):
  k=math.ceil(n*v/(u+v)-1e-12)
  ea=binom.cdf(k-1,n,a);eb=binom.sf(k-1,n,b)
  if max(ea,eb)<.05:return n
def chernoff(q):
 a=.75;b=.5+math.exp(-2*q)/4
 v=minimize_scalar(lambda s:a**s*b**(1-s)+(1-a)**s*(1-b)**(1-s),bounds=(0,1),method='bounded')
 return -math.log(v.fun)
b=active(.5,10,src='B')
xi=brentq(lambda t:active(.5,10,t)-b,23.,24.)
assert abs(xi-23.496399049865)<1e-9 and abs(active(.5,10,xi)-b)<1e-12
a,bp=purity(.5,10)
assert abs(bp-.5479181432778)<1e-12 and counts(a,bp)==185
h=math.pi/10+.1
opt=minimize_scalar(lambda q:-chernoff(q)/(2*(q+h)),bounds=(.05,5),method='bounded')
q=opt.x;N=counts(.75,.5+math.exp(-2*q)/4)
assert abs(q-.8982531)<1e-5 and N==56
print('SOURCE-ON XY finite-pulse scalar indistinguishability xi=',xi,'pB=',b)
print('SOURCE-ON finite prep; IDEAL direct XYZ:',a,bp,'N_both',185)
print('SOURCE-GATED source OFF during pulse overhead q*= ',q,'N_both=',N,'gamma*T=',2*N*(q+h))
print('PASS; finite source-on basis-setting NOT certified phase invariant')
