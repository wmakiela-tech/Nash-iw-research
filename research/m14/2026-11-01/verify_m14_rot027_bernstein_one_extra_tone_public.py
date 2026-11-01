#!/usr/bin/env python3
"""M14 ROT027 standalone exact Bernstein repair; stdlib + sympy."""
from fractions import Fraction as F
import sympy as S
T=S.Symbol('t')
BASE=[F(q) for q in ('3/4','5/4','7/4','9/4','5')]
def determinant(M):
 M=[row[:] for row in M];out=F(1);n=len(M)
 for j in range(n):
  r=next((r for r in range(j,n) if M[r][j]),None)
  if r is None:return F(0)
  if r!=j:M[r],M[j]=M[j],M[r];out=-out
  q=M[j][j];out*=q
  for r in range(j+1,n):
   scale=M[r][j]/q
   for k in range(j+1,n):M[r][k]-=scale*M[j][k]
 return out
def minor(t):
 a=F(155+t,1000);w=[a,F(51,100),F(49,100)-a]
 e,B,v,d=F(1,25),F(-3,100),F(53,100),F(11,50)
 J=[]
 for sg in (-1,1):
  gain=F(4,5) if sg==-1 else F(6,5)
  for x in BASE+([F(11,2)] if sg==-1 else []):
   z=[x-e-sg*B-j*d for j in (-1,0,1)]
   K=[1/(q*q+v) for q in z];u=[2*q/(q*q+v)**2 for q in z];dv=[-1/(q*q+v)**2 for q in z]
   dot=lambda zz:sum((p*q for p,q in zip(w,zz)),F(0))
   f=dot(K);shift=dot(u)
   J.append([-gain*(K[0]-K[2]),-gain*(K[1]-K[2]),-gain*shift,-sg*gain*shift,-gain*dot(dv),-gain*sum((p*j*q for p,j,q in zip(w,(-1,0,1),u)),F(0))]+([F(1),-f,F(0),F(0)] if sg==-1 else [F(0),F(0),F(1),-f]))
 return determinant(J[1:])
q=[(i,minor(i)) for i in range(-3,4)]
p=S.Poly(S.interpolate([(i,S.Rational(x.numerator,x.denominator)) for i,x in q],T),T)
assert p.degree()==5
for t in (F(1,7),F(2,3)):
 assert p.eval(S.Rational(t.numerator,t.denominator))==S.Rational(minor(t))
bern=[sum(p.nth(j)*S.binomial(k,j)/S.binomial(5,j) for j in range(k+1)) for k in range(6)]
assert all(b>=bern[0]>0 for b in bern)
assert p.count_roots(0,1)==0
print('PASS M14 ROT027 exact positive degree-5 Bernstein coefficients; 11x10 full rank for all t in [0,1]')
print('minor det lower',S.N(bern[0],25))
