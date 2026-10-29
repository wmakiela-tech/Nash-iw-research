#!/usr/bin/env python3
"""M14 ROT015 minimal exact-rational public replay (stdlib)."""
from fractions import Fraction as F
def det(a):
 a=[list(r) for r in a];v=F(1)
 for j in range(len(a)):
  p=next(i for i in range(j,len(a)) if a[i][j])
  if p!=j:a[j],a[p]=a[p],a[j];v=-v
  q=a[j][j];v*=q
  for i in range(j+1,len(a)):
   t=a[i][j]/q
   for k in range(j,len(a)):a[i][k]-=t*a[j][k]
 return v
def k(x):return 1/(x*x+F(1,2))
def mat(d):return [[F(1),-k(x+d),-k(x),-k(x-d)] for x in map(F,[-1,0,1,2])]
def df(d):
 return -8192*d**3*(2*d*d-5)*(2*d*d+5)/(3*(2*d*d+1)*(2*d*d-8*d+9)*(2*d*d-4*d+3)**2*(2*d*d+4*d+3)**2*(2*d*d+8*d+9))
g=F(7,20)
for d in [F(1,20),F(1,10),F(1,5),F(1,4),F(1,2),F(4,5),F(1)]:
 assert det(mat(d))==df(d)>0
 a=[g/2,g,g/2];b=[g/8,7*g/4,g/8]
 for x in map(F,[-1,0,1,2]):
  z=[k(x+d),k(x),k(x-d)]
  ma=3-sum(w*t for w,t in zip(a,z))
  mb=3-sum(w*t for w,t in zip(b,z))
  assert min(ma,mb)>=F(8,5)
  assert abs(ma-mb)<=F(21,20)*d*d
print("M14 ROT015 exact arithmetic PASS")
