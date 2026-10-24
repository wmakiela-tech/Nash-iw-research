#!/usr/bin/env python3
"""Source-free Fraction witness to the algebra used by ROT38.
Checks nested covariance -> shell diagonalization, weighted Cauchy-Binet,
and derivative polynomial identity for deterministic rational polynomial probes.
The symbolic expansion is stated in ROT38 report; numeric source interval is separate.
"""
from fractions import Fraction as F
import random

N=41; ks=(2,3,4,5,6)
n=[(N-2*k)**3 for k in ks]
v=[n[i]-n[i+1] for i in range(4)]+[n[-1]]
M=[[F(int(i==j)) for j in range(5)] for i in range(5)]
for i in range(4):
 M[i][i]=F(n[i],v[i]);M[i][i+1]=-F(n[i+1],v[i])
W=[[sum((M[k][i]*v[k]*M[k][j] for k in range(5)),F(0)) for j in range(5)] for i in range(5)]
S=[[F(1,n[min(i,j)]) for j in range(5)] for i in range(5)]
# Check W=Sigma^-1 (Sigma covariance normalized by variance tau²).
SW=[[sum((S[i][k]*W[k][j] for k in range(5)),F(0)) for j in range(5)] for i in range(5)]
assert all(SW[i][j]==F(int(i==j)) for i in range(5) for j in range(5))
MSMT=[[sum((M[i][k]*S[k][l]*M[j][l] for k in range(5) for l in range(5)),F(0)) for j in range(5)] for i in range(5)]
assert all(MSMT[i][j]==F(int(i==j),v[i]) for i in range(5) for j in range(5))

def mul(a,b):
 r=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):r[i+j]+=x*y
 return r

def add(a,b):return [(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(max(len(a),len(b)))]
def sub(a,b):return add(a,[-x for x in b])
def der(a):return [a[i]*i for i in range(1,len(a))]
def scale(a,c):return [x*c for x in a]
def pdot(a,b,weights):
 r=[F(0)]
 for i in range(len(a)):
  r=add(r,scale(mul(a[i],b[i]),weights[i]))
 return r

def sample(rng):return F(rng.randint(1,31),rng.randint(1,7))
rng=random.Random(20261025)
for it in range(60):
 # positive quartic component probes as scale*(1+x+x²/...), no physical interpretation
 amp=[sample(rng) for _ in range(5)]
 pol=[[amp[i]*F(rng.randint(1,8),j+2) for j in range(5)] for i in range(5)]
 alpha=F(it%19,100)
 a=[sum((pol[i][j]*alpha**j for j in range(5)),F(0)) for i in range(5)]
 ap=[[c] for c in a]
 p=pdot(ap,pol,v)
 q=pdot(pol,pol,v)
 H=sub(mul(der(p),q),scale(mul(p,der(q)),F(1,2)))
 wedge_H=[F(0)]
 wedge_D=[F(0)]
 for i in range(5):
  for j in range(i+1,5):
   A=sub(scale(pol[j],a[i]),scale(pol[i],a[j]))
   B=sub(mul(der(pol[i]),pol[j]),mul(der(pol[j]),pol[i]))
   wedge_H=add(wedge_H,scale(mul(A,B),v[i]*v[j]))
   wedge_D=add(wedge_D,scale(mul(A,A),v[i]*v[j]))
 assert len(H)==len(wedge_H) and H==wedge_H,('H',it)
 # Weighted Lagrange identity: ||a||²||b||² -(a·b)² = sum wedges².
 a2=pdot(ap,ap,v)[0]
 assert sub(scale(q,a2),mul(p,p))==wedge_D,('distance',it)
 # Along polynomial source, exact derivative: (D²)'=−2pH/q².
 qprime=der(q)
 dnum=sub(mul(der(wedge_D),q),mul(wedge_D,qprime))
 assert dnum==scale(mul(mul(p,H),[F(1)]),-2),('derivative',it)
print('ROT38_EXACT_SHELL_COVARIANCE_25/25 / INVERSE_25/25 / THREE_POLYNOMIAL_IDENTITIES_60x3_PASS')