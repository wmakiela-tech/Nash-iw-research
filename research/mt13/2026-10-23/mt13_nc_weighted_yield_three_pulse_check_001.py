#!/usr/bin/env python3
"""MT13/NC synthetic nonnegative 3-pulse target insufficiency test.
Standard library only; NO PBH physical/BBN solver execution.
"""
from math import exp,expm1
T=2.;g=2.;lam=1.;k=.1;dt=.1
starts=(0.,.7,1.4)
def u(rate,start): return exp(-rate*(T-start))*expm1(rate*dt)/(rate*dt)
q=[u(g,a) for a in starts]
w=[k*g/(g-lam)*(u(lam,a)-u(g,a)) for a in starts]
c=[q[1]-q[2],q[2]-q[0],q[0]-q[1]]
maxnorm=max(map(abs,c))
c=[z/maxnorm for z in c]
sp=[1+z/2 for z in c];sm=[1-z/2 for z in c]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def metrics(s):return (sum(s),dot(q,s),sum(s)-dot(q,s),.1*exp(-lam*T)+dot(w,s))
a=metrics(sp);b=metrics(sm)
assert min(sp)>0 and min(sm)>0
assert max(abs(a[j]-b[j]) for j in range(3))<2e-14
assert abs(a[3]-b[3])>1e-3
assert all(0<z[3]<1 for z in (a,b))
# Three source moments not rank-two:
det=(q[1]-q[0])*(w[2]-w[0])-(q[2]-q[0])*(w[1]-w[0])
assert abs(det)>1e-4
print('positive source weights:',sp,sm)
print('emission, survivors, reactions, X(T) PLUS:',a)
print('emission, survivors, reactions, X(T) MINUS:',b)
print('different terminal X:',a[3]-b[3])
print('three moment determinant:',det)
print('PASS exact integral-formula test: equal E,n(T),integrated reactions, different X(T)')
