#!/usr/bin/env python3
"""Public M14 ROT022: exact 3-tone same-shape field-value alias (stdlib)."""
from fractions import Fraction as F
D,V=F(1,5),F(1,2)
xs=list(map(F,[1,2,3,4]));w=[F(1,4),F(1,2),F(1,4)]
e=F(1,100);b0=F(1,50);b1=F(201,10000)
def K(z):return 1/(z*z+V)
def f(x,u,w):return sum((a*K(x-u-j*D) for a,j in zip(w,(-1,0,1))),F(0))
def dif(u,w,i):return f(xs[i],u,w)-f(xs[i+1],u,w)
def R(u,w):return dif(u,w,0)/dif(u,w,1)
def C(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
rows=[]
for s in (-1,+1):
  r=R(e+s*b0,w);u=e+s*b1
  rows.append([K(xs[0]-u-j*D)-K(xs[1]-u-j*D)-r*(K(xs[1]-u-j*D)-K(xs[2]-u-j*D)) for j in (-1,0,1)])
q=C(*rows);ww=[a/sum(q) for a in q]
assert min(ww)>0 and sum(ww)==1 and ww!=w
for s,beta,gain in [(-1,F(31,10),F(4,5)),(+1,F(29,10),F(6,5))]:
  u0=e+s*b0;u1=e+s*b1
  old=[beta-gain*f(x,u0,w) for x in xs]
  gg=gain*dif(u0,w,0)/dif(u1,ww,0)
  bb=old[0]+gg*f(xs[0],u1,ww)
  new=[bb-gg*f(x,u1,ww) for x in xs]
  assert gg>0 and bb-gg/V>0
  assert old[:3]==new[:3] and old[3]!=new[3]
print('PASS: exact six-channel full Poisson alias; fourth-tone heldout nonzero')
