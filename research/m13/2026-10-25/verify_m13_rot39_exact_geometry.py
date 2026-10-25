#!/usr/bin/env python3
"""Source-free exact rational algebra: compare shifted-shell wedge profile polynomial.
Does not verify source reconstruction, directed intervals, or root isolation.
"""
from fractions import Fraction as F
from math import comb

def add(a,b):
 return [(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(max(len(a),len(b)))]
def mul(a,b):
 out=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def scale(a,k):return [x*k for x in a]
def sub(a,b):return add(a,scale(b,-1))
def shift(a,t):
 out=[F(0)]*len(a)
 for i,x in enumerate(a):
  for j in range(i+1):out[j]+=x*comb(i,j)*t**(i-j)
 return out
def pe(a,t):return sum((x*t**i for i,x in enumerate(a)),F(0))
def abs_cross(a,b,w):
 return sum((w[i]*w[j]*(a[i]*b[j]-a[j]*b[i])**2 for i in range(5) for j in range(i+1,5)),F(0))

N=41;n=[(N-2*k)**3 for k in range(2,7)];v=[n[i]-n[i+1] for i in range(4)]+[n[4]]
# covariance inverse shell map: B maps 5 masked averages to 5 disjoint shells.
B=[[F(0) for _ in range(5)] for _ in range(5)]
for i in range(4):B[i][i]=F(n[i],v[i]);B[i][i+1]=F(-n[i+1],v[i])
B[4][4]=F(1)
Sigma=[[F(1,n[min(i,j)]) for j in range(5)] for i in range(5)]
D=[[sum((B[i][k]*Sigma[k][l]*B[j][l] for k in range(5) for l in range(5)),F(0)) for j in range(5)] for i in range(5)]
assert all(D[i][j]==(F(1,v[i]) if i==j else F(0)) for i in range(5) for j in range(5))
checks=0;dd=F(1,100)
for seed in range(1,21):
 # positive polynomials for a∈[0,0.2], source-free rational coefficient examples
 a=[[F(1+i+seed,3)+F((i+2)*seed,11)*F(k+1,24)*F(1,seed+1) for k in range(5)] for i in range(5)]
 shifted=[ [shift(p,sg*dd) for p in a] for sg in (-1,1)]
 def numerator(z):
  num=[F(0)]
  for i in range(5):
   for j in range(i+1,5):
    di=scale(sub(z[i],a[i]),1/dd);dj=scale(sub(z[j],a[j]),1/dd)
    c=sub(mul(a[i],dj),mul(a[j],di))
    num=add(num,scale(mul(c,c),v[i]*v[j]))
  return num
 def q(z):
  x=[F(0)]
  for i in range(5):x=add(x,scale(mul(z[i],z[i]),v[i]))
  return x
 nm,np=numerator(shifted[0]),numerator(shifted[1]);qm,qp=q(shifted[0]),q(shifted[1]);S=sub(mul(nm,qp),mul(np,qm))
 for x in [F(1,100),F(3,100),F(1,20),F(1,10),F(19,100)]:
  y=[pe(p,x) for p in a]
  bm=[pe(p,x-dd) for p in a];bp=[pe(p,x+dd) for p in a]
  n_m=abs_cross(y,bm,v);n_p=abs_cross(y,bp,v)
  assert n_m==dd*dd*pe(nm,x)
  assert n_p==dd*dd*pe(np,x)
  direct=n_m/pe(qm,x)-n_p/pe(qp,x)
  certified=dd*dd*pe(S,x)/(pe(qm,x)*pe(qp,x))
  assert direct==certified
  checks+=3
print('ROT39 EXACT SOURCE-FREE RATIONAL GEOMETRY PASS',checks,'identities + 25 exact covariance components')
