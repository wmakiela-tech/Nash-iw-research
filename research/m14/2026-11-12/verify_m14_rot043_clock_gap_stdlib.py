#!/usr/bin/env python3
"""ROT043 exact integer-shot m=1 clock-gap certificates, pure Python stdlib.
Analytical compactness/nonattainment proof lives in scientific report.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb, ceil

A=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))

def inverse(M):
 n=len(M);a=[list(map(Q,M[i]))+[Q(int(i==j)) for j in range(n)] for i in range(n)]
 for j in range(n):
  k=next(k for k in range(j,n) if a[k][j]);a[j],a[k]=a[k],a[j]
  p=a[j][j];a[j]=[v/p for v in a[j]]
  for k in range(n):
   if k==j:continue
   fac=a[k][j];a[k]=[a[k][u]-fac*a[j][u] for u in range(2*n)]
 return [row[n:] for row in a]

def check(r,delta):
 m=1;N=240;C=Q(2);B=comb(4,r);alpha=1-(B-1)*delta
 groups=list(combinations(range(4),r))
 data=[]
 for g,G in enumerate(groups):
  for j,tbase in enumerate((0,1)):
   t=Q(g)*delta+alpha*tbase
   data.append((t,G))
 ts=sorted(t for t,_ in data)
 assert all(v-u>=delta for u,v in zip(ts,ts[1:]))
 mat=[[Q(0) for _ in range(6)] for _ in range(6)]
 for t,G in data:
  means=[sum(A[i][k] for i in G)/Q(r) for k in range(3)]
  for i in G:
   a=[Q(A[i][k])-means[k] for k in range(3)]
   x=a+[t*v for v in a]
   for j in range(6):
    for k in range(6):mat[j][k]+=10*x[j]*x[k]
 inv=inverse(mat)
 risk=sum(inv[i][i] for i in range(3,6))
 bound=Q(9*r,4*(r-1))*C*C/N
 q=ceil(Q(3*(m+1),r-1))-(m+1)
 gamma=2*delta-delta*delta
 gap_lower=Q(9)*C*C/(Q(4*N*(r-1),r)-4*q*gamma)
 upper=bound/alpha**(2*m)
 assert bound<gap_lower<risk<upper
 return bound,gap_lower,risk,upper

for r in (2,3):
 out=check(r,Q(1,100))
 print('r=',r,'delta=1/100',' | '.join(str(x)+' = '+format(float(x),'.12f') for x in out))
 assert (out[0]==Q(3,40) if r==2 else out[0]==Q(9,160))
print('ROT043 EXACT STDLIB PASS: positive integer-shot clock-resolution gap, exact full Gaussian quotient, strict constructive upper')
