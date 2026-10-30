#!/usr/bin/env python3
"""M14 ROT023: exact rational four/five-tone Jacobian rank checks (stdlib)."""
from fractions import Fraction as F
v=F(1,2);d=F(1,5);w=(F(1,4),F(1,2),F(1,4));e=F(1,100);B=F(1,50)
def K(t):return 1/(t*t+v)
def Ku(t):return 2*t/(t*t+v)**2
def Kv(t):return -1/(t*t+v)**2
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def J(tones):
 out=[]
 for s in (-1,1):
  u=e+s*B; f=[]
  for x,y in zip(tones[:-1],tones[1:]):
   t=[x-u-j*d for j in (-1,0,1)];t2=[y-u-j*d for j in (-1,0,1)]
   a=[K(x)-K(y) for x,y in zip(t,t2)]
   b=[Ku(x)-Ku(y) for x,y in zip(t,t2)]
   c=[Kv(x)-Kv(y) for x,y in zip(t,t2)]
   z=dot(w,a);assert z>0
   f.append([(a[0]-a[2])/z,(a[1]-a[2])/z,dot(w,b)/z,dot(w,c)/z,(-w[0]*b[0]+w[2]*b[2])/z])
  for a,b in zip(f[:-1],f[1:]):
   q=[x-y for x,y in zip(a,b)]
   out.append([q[0],q[1],q[2],s*q[2],q[3],q[4]])
 return out
def det(a):
 a=[list(r) for r in a];ans=F(1);n=len(a)
 for j in range(n):
  p=next((i for i in range(j,n) if a[i][j]),None)
  if p is None:return F(0)
  if p!=j:a[j],a[p]=a[p],a[j];ans=-ans
  z=a[j][j];ans*=z
  for i in range(j+1,n):
   t=a[i][j]/z
   for k in range(j,n):a[i][k]-=t*a[j][k]
 return ans
def solve(a,b):
 a=[list(r)+[t] for r,t in zip(a,b)];n=len(a)
 for j in range(n):
  p=next(i for i in range(j,n) if a[i][j]);a[j],a[p]=a[p],a[j]
  t=a[j][j];a[j]=[x/t for x in a[j]]
  for i in range(n):
   if i!=j:
    t=a[i][j];a[i]=[x-t*y for x,y in zip(a[i],a[j])]
 return [r[-1] for r in a]
a=J(tuple(map(F,(1,2,3,4))))
A=[r[:4] for r in a]
assert det(A)>0
width_tangent=solve(A,[-r[4] for r in a]);assert width_tangent[3]!=0
splitting_tangent=solve(A,[-r[5] for r in a]);assert splitting_tangent[3]!=0
z=J(tuple(map(F,(1,2,3,4,5))))
assert det(z)!=0
assert det([r[:5] for r in z[:5]])!=0
zalt=J(tuple(map(F,('0.85','1.35','2.25','3.55','3.95'))))
assert det(zalt)!=0
print('PASS: exact 4-tone field-width alias tangent and 5-tone 6x6 full rank')
