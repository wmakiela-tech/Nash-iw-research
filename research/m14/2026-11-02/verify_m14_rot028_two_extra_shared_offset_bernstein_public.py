#!/usr/bin/env python3
"""M14 ROT028 public Fraction/SymPy certificate; synthetic source, no hardware claims."""
from fractions import Fraction as F
import sympy as S
t=S.symbols('t')
xs=tuple(map(F,('3/4','5/4','7/4','9/4','5')))
def det(A):
 A=[list(q) for q in A];out=F(1)
 for j in range(len(A)):
  p=next((p for p in range(j,len(A)) if A[p][j]),None)
  if p is None:return F(0)
  if j!=p:A[j],A[p]=A[p],A[j];out=-out
  pivot=A[j][j];out*=pivot
  for k in range(j+1,len(A)):
   q=A[k][j]/pivot
   for m in range(j+1,len(A)):A[k][m]-=q*A[j][m]
 return out
def minor(x):
 a=(F(155)+x)/1000;w=(a,F(51,100),F(49,100)-a)
 e,B,v,d=F(1,25),F(-3,100),F(53,100),F(11,50)
 assert min(w)>0
 rows=[]
 for sg in (-1,1):
  gain=F(4,5) if sg==-1 else F(6,5)
  for tone in xs+((F(11,2),F(6)) if sg==-1 else ()):
   z=[tone-e-sg*B-j*d for j in (-1,0,1)]
   k=[1/(zz*zz+v) for zz in z]
   u=[2*zz/(zz*zz+v)**2 for zz in z]
   q=[-1/(zz*zz+v)**2 for zz in z]
   dot=lambda arr:sum((ww*y for ww,y in zip(w,arr)),F(0))
   f=dot(k);du=dot(u)
   rows.append([-gain*(k[0]-k[2]),-gain*(k[1]-k[2]),-gain*du,-sg*gain*du,-gain*dot(q),-gain*sum((ww*j*uu for ww,j,uu in zip(w,(-1,0,1),u)),F(0))]+([F(1),-f,F(0),F(0)] if sg==-1 else [F(0),F(0),F(1),-f]))
 nine=[r for i,r in enumerate(rows) if i in (1,2,3,4,7,8,9,10,11)]
 dif=[p-q for p,q in zip(rows[6],rows[5])]
 return det(nine+[dif])
points=[(j,minor(F(j))) for j in range(-3,4)]
p=S.Poly(S.interpolate([(x,S.Rational(y.numerator,y.denominator)) for x,y in points],t),t)
assert p.degree()==5
for u in (F(1,7),F(2,3)):
 assert p.eval(S.Rational(u.numerator,u.denominator))==S.Rational(minor(u).numerator,minor(u).denominator)
b=[sum(p.nth(j)*S.binomial(k,j)/S.binomial(5,j) for j in range(k+1)) for k in range(6)]
assert all(q<=b[0]<0 for q in b)
assert p.count_roots(0,1)==0
print('M14 ROT028 EXACT PASS: two shared-offset extra Poisson readings give uniformly nonzero 11x11 Jacobian minor')
print('abs determinant lower',S.N(-b[0],23))
