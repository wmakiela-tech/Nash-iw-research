#!/usr/bin/env python3
"""Public M14 ROT021 stand-alone Fraction interval certificate + exact positive alias."""
from fractions import Fraction as F
v=F(1,2);d=F(1,5)
def K(z):return 1/(z*z+v)
def box(a,b,l,r):
 def term(x):
  lo=F(x)-r;hi=F(x)-l
  return 2*lo/(hi*hi+v),2*hi/(lo*lo+v)
 p,q=term(a),term(b)
 return -2/(a+b-2*r)+p[0]+q[0],-2/(a+b-2*l)+p[1]+q[1]
for i in range(35):
 l=-F(7,20)+F(i,50);r=l+F(1,50)
 assert box(1,2,l,r)[0]>F(137,100)
 assert box(2,3,l,r)[1]<F(129,100)

def solve(A,b):
 r=[list(row)+[v] for row,v in zip(A,b)]
 for k in range(len(r)):
  j=next(j for j in range(k,len(r)) if r[j][k]);r[j],r[k]=r[k],r[j]
  t=r[k][k];r[k]=[v/t for v in r[k]]
  for i in range(len(r)):
   if i!=k:
    t=r[i][k];r[i]=[u-t*v for u,v in zip(r[i],r[k])]
 return [row[-1] for row in r]
tones=[F(1),F(2),F(3)];w0=[F(7,40),F(7,20),F(7,40)]
base=[sum((w*K(x-j*d) for j,w in zip((-1,0,1),w0)),F(0)) for x in tones]
for s in (-1,+1):
 a=[[K(x-s*F(1,20)-j*d) for j in (-1,0,1)] for x in tones]
 w1=solve(a,base)
 assert all(w>0 for w in w1) and sum(w1)/v<F(3)
 assert [sum((w*K(x-s*F(1,20)-j*d) for j,w in zip((-1,0,1),w1)),F(0)) for x in tones]==base
print('M14 ROT021 PASS: 35 rational boxes and exact six-channel positive alias without common shape')
