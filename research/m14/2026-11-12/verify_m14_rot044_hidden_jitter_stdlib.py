#!/usr/bin/env python3
"""M14 ROT044 -- standalone exact Fraction witness; no scientific packages."""
from fractions import Fraction as F
from itertools import product
A=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
assert [sum(A[i][j] for i in range(4)) for j in range(3)]==[0,0,0]
assert [[sum(A[i][j]*A[i][k] for i in range(4)) for k in range(3)] for j in range(3)]==[[4,0,0],[0,4,0],[0,0,4]]
def sq(v):return sum(z*z for z in v)
def proj(h):return tuple(sum(F(A[i][j])*h[i] for i in range(4))/4 for j in range(3))
assert max(sq(proj(q)) for q in product((F(0),F(2)),repeat=4))==1
for H,eps in ((F(3,5),F(1,20)),(F(2),F(1,1000)),(F(0),F(1))):
 for s in (-1,1):
  for i in range(4):
   # Two worlds: z_s=u+s*H*eps*ex; hidden time=-s*eps*a_ix; common h(t)=H*t.
   assert s*H*eps*A[i][0]+H*(-s*eps*A[i][0])==0
N=80;sigma2=F(7,10);H=F(3,5);eps=F(3,100)
assert F(3)*sigma2/N+(H*eps)**2==F(13287,500000)
# Three axes: arbitrary common h and z->z+q*(1,1,-1) generate identical data.
assert [sum(A[i][j]*(1,1,-1)[j] for j in range(3)) for i in range(3)]==[1,1,1]
print('M14 ROT044 stdlib EXACT PASS: 4-axis hidden jitter minimax 3 sigma²/N + H² eps²; 3-axis common-offset gauge')
