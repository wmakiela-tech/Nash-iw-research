#!/usr/bin/env python3
"""PRF12 R20 NumPy+SciPy core. Full extended code in R20 ZIP.
Same static xi through two sequential Ramsey shots, no mid-pair reset.
No finite-time preparation/readout or original single-copy LOCC claim.
"""
import math
import numpy as np
from scipy.stats import binom
from scipy.optimize import minimize_scalar
I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
eye=np.eye(4,dtype=complex)
J=np.kron(X,X)+np.kron(Y,Y)
E=eye/2+J/4
assert np.max(abs(np.linalg.eigvalsh(E)-[0,.5,.5,1]))<1e-13
def rho(p,v=1):
 return (I+v*(math.cos(p)*X+math.sin(p)*Y))/2
for phi in np.linspace(-50,50,307):
 assert abs(np.trace(E@np.kron(rho(phi),rho(phi))).real-.75)<1e-13
for q in (.05,1/3,.5,.579,1,3):
 x=math.exp(-q)
 b=np.trace(E@np.kron(rho(0,x),rho(0,x))).real
 assert abs(b-(.5+x*x/4))<1e-13
 A=eye/4+J/8
 B=eye/4+x*x*J/8
 D=A-B
 assert abs(np.abs(np.linalg.eigvalsh(D)).sum()/2-(1-x*x)/4)<1e-13
 assert abs(np.trace(E@D).real-(1-x*x)/4)<1e-13
def err(n,q):
 a=.75;b=.5+math.exp(-2*q)/4
 k=math.ceil(n*math.log((1-b)/(1-a))/
      (math.log(a/b)+math.log((1-b)/(1-a)))-1e-12)
 ea=binom.cdf(k-1,n,a);eb=binom.sf(k-1,n,b)
 return k,(ea+eb)/2,ea,eb
assert err(94,.5)[1]<.05 and err(93,.5)[1]>.05
assert max(err(97,.5)[2:])<.05 and max(err(96,.5)[2:])>.05
assert max(err(80,.579)[2:])<.05
q=.5;e=.02
margin=((1-math.exp(-2*q))-(1+math.exp(-2*q))*abs(math.sin(e)))/4
assert margin>.151
n=math.ceil(2*math.log(20)/margin**2)
assert n==263
def C(q):
 a=.75;b=.5+math.exp(-2*q)/4
 y=minimize_scalar(lambda s:a**s*b**(1-s)+(1-a)**s*(1-b)**(1-s),
                   bounds=(0,1),method='bounded')
 return -math.log(y.fun)
v=minimize_scalar(lambda q:-C(q)/(2*q),bounds=(.02,4),method='bounded')
assert abs(v.x-.589513)<2e-5
print('PASS 307 phase checks, U1-twirl Helstrom, exact binomial samples')
print('N94 at q=.5',err(94,.5),'N97',err(97,.5))
print('N80 at q=.579',err(80,.579),'Chernoff q*',v.x)
print('Relative-axis error epsilon=.02 Hoeffding certificate N',n)
