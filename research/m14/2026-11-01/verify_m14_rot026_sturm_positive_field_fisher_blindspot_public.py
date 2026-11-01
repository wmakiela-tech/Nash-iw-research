#!/usr/bin/env python3
"""Public exact M14 ROT026 Sturm certificate; requires sympy, no source data."""
from fractions import Fraction as F
import sympy as s
T=s.symbols('t')
SETS={
 'winner':tuple(map(F,('3/4','5/4','7/4','9/4','5'))),
 'old':tuple(map(F,('1','2','3','4','5'))),
 'alternative':tuple(map(F,('17/20','27/20','9/4','71/20','79/20')))}
def jac(a,tones):
 c,e,B,v,d=F(51,100),F(1,25),F(-3,100),F(53,100),F(11,50)
 w=(a,c,1-a-c);assert min(w)>0
 rows=[]
 for sg,baseline,gain in ((-1,F(31,10),F(4,5)),(1,F(29,10),F(6,5))):
  for x in tones:
   z=[x-e-sg*B-j*d for j in (-1,0,1)]
   k=[1/(q*q+v) for q in z]
   u=[2*q/(q*q+v)**2 for q in z]
   vv=[-1/(q*q+v)**2 for q in z]
   dot=lambda a:sum((r*q for r,q in zip(w,a)),F(0))
   f=dot(k);der=dot(u)
   assert baseline-gain*f>0
   rows.append([-gain*(k[0]-k[2]),-gain*(k[1]-k[2]),-gain*der,-sg*gain*der,
     -gain*dot(vv),-gain*sum((r*j*q for r,j,q in zip(w,(-1,0,1),u)),F(0))]
     +([F(1),-f,F(0),F(0)] if sg==-1 else [F(0),F(0),F(1),-f]))
 return rows
def det(rows):
 a=[list(q) for q in rows];out=F(1);n=len(a)
 for j in range(n):
  p=next((i for i in range(j,n) if a[i][j]),None)
  if p is None:return F(0)
  if p!=j:a[p],a[j]=a[j],a[p];out=-out
  pivot=a[j][j];out*=pivot
  for i in range(j+1,n):
   fac=a[i][j]/pivot
   for h in range(j+1,n):a[i][h]-=fac*a[j][h]
 return out
def poly(tones,nuis=False):
 pairs=[]
 for x in range(-3,4):
  a=F(155+x,1000);J=jac(a,tones)
  if nuis:J=[[v for i,v in enumerate(row) if i!=3] for row in J[:9]]
  q=det(J);pairs.append((x,s.Rational(q.numerator,q.denominator)))
 return s.Poly(s.interpolate(pairs,T),T,domain=s.QQ)
P=poly(SETS['winner']);Q=poly(SETS['winner'],True)
R=poly(SETS['old']);S=poly(SETS['alternative'])
assert [p.degree() for p in (P,Q,R,S)]==[5,4,5,5]
assert [int(p.count_roots(0,1)) for p in (P,Q,R,S)]==[1,0,0,0]
assert all(s.gcd(P,q).degree()==0 for q in (Q,R,S))
assert P.eval(s.Rational(2794,10000))<0<P.eval(s.Rational(2795,10000))
print('PASS M14 ROT026: exact first-order field-Fisher zero at one positive-source weight; 9 nuisance independent')
