#!/usr/bin/env python3
"""M14 ROT029: public exact Bernstein certificate, synthetic Poisson 3-line class.
Requires sympy; standard library handles all exact 12x12 determinants."""
from fractions import Fraction as F
import sympy as S
T=S.symbols("t")
X=tuple(map(F,("3/4","5/4","7/4","9/4","5")))
def determinant(A):
 A=[r[:] for r in A];ans=F(1);n=len(A)
 for j in range(n):
  p=next((i for i in range(j,n) if A[i][j]),None)
  if p is None:return F(0)
  if p!=j:A[p],A[j]=A[j],A[p];ans=-ans
  z=A[j][j];ans*=z
  for i in range(j+1,n):
   h=A[i][j]/z
   for k in range(j+1,n):A[i][k]-=h*A[j][k]
 return ans
def witness(t):
 a=(F(155)+t)/1000;w=(a,F(51,100),F(49,100)-a)
 e,B,v,d=F(1,25),F(-3,100),F(53,100),F(11,50)
 J=[];means=[]
 for sg in (-1,1):
  beta,g=(F(31,10),F(4,5)) if sg==-1 else (F(29,10),F(6,5))
  for x in X+((F(11,2),F(6),F(13,2)) if sg==-1 else ()):
   z=[x-e-sg*B-j*d for j in (-1,0,1)]
   k=[1/(q*q+v) for q in z]
   u=[2*q/(q*q+v)**2 for q in z]
   qv=[-1/(q*q+v)**2 for q in z]
   dot=lambda vec:sum((p*y for p,y in zip(w,vec)),F(0))
   f=dot(k);h=dot(u)
   J.append([-g*(k[0]-k[2]),-g*(k[1]-k[2]),-g*h,-sg*g*h,
      -g*dot(qv),-g*sum((p*j*y for p,j,y in zip(w,(-1,0,1),u)),F(0))]
      +([F(1),-f,F(0),F(0)] if sg==-1 else [F(0),F(0),F(1),-f]))
   means.append(beta-g*f)
 assert min(w)>0 and min(means)>0 and len(J)==13
 old=[J[i] for i in (1,2,3,4,8,9,10,11,12)]
 y1,y2,y3=means[5:8]
 q=[(y2-y1)*J[7][i]-(y3-y1)*J[6][i]+(y3-y2)*J[5][i] for i in range(10)]
 D=determinant(old+[q])
 full=[r+[F(0),F(0)] for r in old]+[J[i]+[F(1),means[i]] for i in (5,6,7)]
 assert determinant(full)==D
 return D
rat=lambda x:S.Rational(x.numerator,x.denominator)
P=S.Poly(S.interpolate([(i,rat(witness(F(i)))) for i in range(-5,6)],T),T,domain=S.QQ)
assert P.degree()==6
for t in (F(1,7),F(2,3),F(5,11)):
 assert P.eval(rat(t))==rat(witness(t))
b=[sum(P.nth(j)*S.binomial(k,j)/S.binomial(6,j) for j in range(k+1)) for k in range(7)]
assert all(z<=b[0]<0 for z in b)
assert P.count_roots(0,1)==0
print("M14 ROT029 EXACT PASS: all seven Bernstein coefficients negative; 13x12 full rank over t in [0,1]")
print("uniform determinant abs lower",S.N(-b[0],20))
