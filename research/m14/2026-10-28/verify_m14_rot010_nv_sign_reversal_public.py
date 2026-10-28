#!/usr/bin/env python3
"""M14 ROT010: public standalone synthetic NV ratio and Fisher checks."""
from fractions import Fraction as Q
C,a=Q(97,100),Q(1,2)
f0=1-C/(1+4*a*a)
fp=8*C*a/(1+4*a*a)**2
assert f0==Q(103,200) and fp==Q(97,100)
q=fp*fp/f0
assert q==Q(9409,5150)
Jp,Jm=4000*q,6000*q
J=4*Jp*Jm/(Jp+Jm)
assert J==Q(1806528,103)
assert 4*(5000*q)*(5000*q)/(10000*q)==Q(1881800,103)
def f(x):return 1-.97/(1+4*x*x)
def df(x):return 8*.97*x/(1+4*x*x)**2
def R(u):return f(.5+u)/f(.5-u)
def invert(v):
    assert R(-.5)<v<R(.5)
    l,r=-.5,.5
    for _ in range(75):
        m=(l+r)/2
        if R(m)>v:r=m
        else:l=m
    return (l+r)/2
def mus(g,u):return [g*f(.5+u)/2,g*f(.5-u)/2]
N1,N2=4000,6000
e,delta=.11,.07
up,um=e+delta,e-delta
m1,m2=mus(N1,up),mus(N2,um)
v1,v2=invert(m1[0]/m1[1]),invert(m2[0]/m2[1])
assert abs((v1-v2)/2-delta)<1e-14 and abs((v1+v2)/2-e)<1e-14
assert abs(2*m1[1]/f(.5-v1)-N1)<1e-9
assert abs(2*m2[1]/f(.5-v2)-N2)<1e-9
for k in range(1,100):
    u=-.5+k/100
    assert df(.5+u)/f(.5+u)+df(.5-u)/f(.5-u)>0
# Outside |u|<0.5 the ratio has an exact distant alternative.
target=R(.2);l,r=.5,100.
assert R(l)>target>R(r)
for _ in range(80):
    m=(l+r)/2
    if R(m)>target:l=m
    else:r=m
uf=(l+r)/2
mf=mus(2*mus(N1,.2)[1]/f(.5-uf),uf)
assert .5<uf<1 and max(abs(x-y) for x,y in zip(mf,mus(N1,.2)))<1e-9
# Unknown gain AND additive background can hide nearby nonzero shifts.
orig=[x+1000 for x in mus(4000,.16)]
g1=2*(orig[0]-orig[1])/(f(.5+.17)-f(.5-.17))
b1=orig[0]-g1*f(.5+.17)/2
assert g1>0 and b1>0
assert max(abs(x-(v+b1)) for x,v in zip(orig,mus(g1,.17)))<1e-9
print('PASS','J=',J,'Ieff_ratio=',float(J/(10000*q)),
      'u_remote=',uf,'global_alias_gap=',R(uf)-target,
      'gain_offset=',g1,b1)
