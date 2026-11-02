#!/usr/bin/env python3
"""M14 ROT031 public Fraction certificate: geometry and exact triplet-spectral gauge."""
from fractions import Fraction as F
A=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def det(M):
 M=[list(map(F,r)) for r in M];out=F(1)
 for j in range(len(M)):
  k=next((k for k in range(j,len(M)) if M[k][j]),None)
  if k is None:return F(0)
  if k!=j:M[j],M[k]=M[k],M[j];out=-out
  z=M[j][j];out*=z
  for k in range(j+1,len(M)):
   t=M[k][j]/z
   for l in range(j+1,len(M)):M[k][l]-=t*M[j][l]
 return out
H=[(1,)+a for a in A]
assert det(H)==-16 and det(A[:3])==4
assert all(sum(A[i][k] for i in range(4))==0 for k in range(3))
assert all(sum(A[i][j]*A[i][k] for i in range(4))==(4 if j==k else 0) for j in range(3) for k in range(3))
e=F(287,100);b=(F(1,20),-F(1,30),F(1,40));u=F(1,100)
y=[e+dot(a,b) for a in A]
b1=tuple(b[k]+u*A[3][k] for k in range(3))
y1=[e+u+dot(a,b1) for a in A]
assert y[:3]==y1[:3] and y1[3]-y[3]==4*u
assert sum(y,F(0))/4==e
assert all(sum((A[i][k]*y[i] for i in range(4)),F(0))/4==b[k] for k in range(3))
W=((F(1,4),F(1,2),F(1,4)),(F(1,5),F(3,5),F(1,5)),(F(1,3),)*3)
D=(F(1,5),F(1,4),F(1,6));V=(F(1,2),F(3,5),F(2,3))
def spectrum(i,x,center):
 return F(4)-F(4,5)*sum((W[i][j+1]/((x-center-j*D[i])**2+V[i]) for j in (-1,0,1)),F(0))
for i in range(3):
 for k in range(31):
  x=F(k-5,5)
  assert spectrum(i,x,y[i])==spectrum(i,x,y1[i])
# Arbitrary per-orientation drift e_i can absorb any field-vector shift in four center equations.
db=(F(1,50),F(-1,70),F(1,60));ep=(F(281,100),F(288,100),F(282,100),F(289,100))
assert all(ep[i]+dot(A[i],b)==ep[i]-dot(A[i],db)+dot(A[i],tuple(b[k]+db[k] for k in range(3))) for i in range(4))
# Paired plus/minus centers with independent e_i per orientation:
assert all(((ep[i]+dot(A[i],b))-(ep[i]-dot(A[i],b)))/2==dot(A[i],b) for i in range(3))
print('M14 ROT031 PUBLIC EXACT PASS: 3-spectrum gauge, four-orientation invertibility, 3 paired-branch drift cancel')
