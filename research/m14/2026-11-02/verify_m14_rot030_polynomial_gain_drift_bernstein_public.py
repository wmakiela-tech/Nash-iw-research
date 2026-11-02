#!/usr/bin/env python3
"""M14 ROT030 public reproducible exact Jacobian/Bernstein certificate, synthetic."""
from fractions import Fraction as F
import sympy as s
T=s.Symbol('t')
BASE=tuple(map(F,('3/4','5/4','7/4','9/4','5')))
EXTRA=tuple(map(F,('11/2','6','13/2','7')))
def det(M):
 M=[list(r) for r in M];v=F(1);n=len(M)
 for j in range(n):
  z=next((k for k in range(j,n) if M[k][j]),None)
  if z is None:return F(0)
  if j!=z:M[j],M[z]=M[z],M[j];v=-v
  d=M[j][j];v*=d
  for i in range(j+1,n):
   q=M[i][j]/d
   for k in range(j+1,n):M[i][k]-=q*M[j][k]
 return v
def value(t):
 w=(F(155+t,1000),F(51,100),F(335-t,1000))
 e,B,v,d=F(1,25),F(-3,100),F(53,100),F(11,50)
 J=[];M=[]
 for sg in (-1,1):
  beta,g=(F(31,10),F(4,5)) if sg==-1 else (F(29,10),F(6,5))
  for x in BASE+(EXTRA if sg==-1 else ()):
   z=[x-e-sg*B-j*d for j in (-1,0,1)]
   k=[1/(zz*zz+v) for zz in z]
   du=[2*zz/(zz*zz+v)**2 for zz in z]
   dv=[-1/(zz*zz+v)**2 for zz in z]
   dot=lambda a:sum((q*y for q,y in zip(w,a)),F(0))
   f=dot(k);shift=dot(du)
   J.append([-g*(k[0]-k[2]),-g*(k[1]-k[2]),-g*shift,-sg*g*shift,
       -g*dot(dv),-g*sum((q*j*y for q,j,y in zip(w,(-1,0,1),du)),F(0))]
       +([F(1),-f,F(0),F(0)] if sg==-1 else [F(0),F(0),F(1),-f]))
   M.append(beta-g*f)
 assert min(w)>0 and min(M)>0
 old=[J[i] for i in (1,2,3,4,9,10,11,12,13)]
 H=[[F(1),M[5+i],(EXTRA[i]-6)*M[5+i]] for i in range(4)]
 cof=[(-1)**i*det([h for j,h in enumerate(H) if j!=i]) for i in range(4)]
 assert all(sum(cof[i]*H[i][j] for i in range(4))==0 for j in range(3))
 q=[sum(cof[i]*J[5+i][j] for i in range(4)) for j in range(10)]
 D=det(old+[q]);C=det(H[:3])
 if t==0:
  full=[r+[F(0)]*3 for r in old]+[J[i]+H[i-5] for i in range(5,9)]
  assert det(full) in (D,-D)
 return D,C
def rat(x):return s.Rational(x.numerator,x.denominator)
def P(which):
 a=s.Poly(s.interpolate([(i,rat(value(i)[which])) for i in range(-6,7)],T),T,domain=s.QQ)
 for t in (F(1,7),F(2,3),F(5,11)):assert a.eval(rat(t))==rat(value(t)[which])
 return a
def bern(a):
 n=a.degree()
 return [sum(a.nth(j)*s.binomial(i,j)/s.binomial(n,j) for j in range(i+1)) for i in range(n+1)]
D=P(0);Q=P(1);d=bern(D);q=bern(Q)
assert D.degree()==7 and Q.degree()==2
assert all(x<=d[0]<0 for x in d)
assert all(x>=q[-1]>0 for x in q)
assert D.count_roots(0,1)==0 and Q.count_roots(0,1)==0
print('M14 ROT030 EXACT PASS: 3 extra channels absorbed by 3 affine-drift nuisances; 4 give 13x13 uniform rank')
print('Bernstein D upper',s.N(d[0],18),'calibration Q lower',s.N(q[-1],18))
