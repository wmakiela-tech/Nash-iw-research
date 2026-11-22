#!/usr/bin/env python3
"""PRF14 ROT017: independent direct 16-Pauli-history Kraus check of
two distinct proper SO(3) gates with two individually invariant source
Fourier coordinates in the SAME output row, yet all four full channels equal.
SymPy only. Restricted classical Pauli source, no hardware.
"""
from itertools import product
import sympy as s
F=s.Rational
R=s.Matrix([[-3,-2,6],[6,-3,2],[2,6,3]])/7
RB=s.Matrix([[3,2,-6],[-2,-6,-3],[-6,3,-2]])/7
P=s.Matrix([[0,0,1],[1,0,0],[0,1,0]])
L=s.Matrix([[0,1/s.sqrt(2),1/s.sqrt(2)],
            [1,0,0],[0,1/s.sqrt(2),-1/s.sqrt(2)]])
C=s.Matrix([[0,F(9,100),F(11,100)],
            [F(7,100),0,F(1,10)],
            [F(8,100),F(12,100),0]])
A=[
 s.Matrix([[0,-F(9,100),-F(11,100)],[-F(21,100),0,-F(1,15)],[-F(2,75),F(6,25),0]]),
 s.Matrix([[0,-F(9,100),-F(11,100)],[F(7,200),0,-F(3,10)],[F(4,25),-F(9,50),0]]),
 s.Matrix([[0,-F(9,100),-F(11,100)],[-F(7,150),0,F(1,20)],[-F(3,25),-F(1,25),0]]),
 s.Matrix([[0,-F(9,100),-F(11,100)],[-F(7,100),0,-F(1,10)],[F(2,25),F(3,25),0]])]
labels=list(product((0,1),repeat=2))
def signs(v):
 x,z=v
 return s.diag((-1)**z,(-1)**(x+z),(-1)**x)
def source(K):
 p={}
 for v,w in product(labels,labels):
  z=s.Integer(1)
  for i in range(3):
   for j in range(3):
    if i!=j:z+=K[i,j]*signs(v)[j,j]*signs(w)[i,i]
  p[(v,w)]=s.factor(z/16)
 return p
def channel(K,S):
 p=source(K)
 assert len(p)==16 and sum(p.values())==1 and min(p.values())>0
 T=s.zeros(3)
 for (v,w),prob in p.items():T+=prob*signs(w)*S*signs(v)
 return T.applyfunc(s.simplify),min(p.values())
def contexts(R):return R,R*P,R*P**2,L*R
assert RB.T*RB==s.eye(3) and RB.det()==1 and RB!=R
for q in range(4):
 T0,p0=channel(C,contexts(R)[q])
 T1,p1=channel(A[q],contexts(RB)[q])
 assert T0==T1 and all(T0[i,i]==0 for i in range(3))
 assert A[q][0,1]==-F(9,100) and A[q][0,2]==-F(11,100)
 print('context',q,'9/9 channel entries exact; source minimum:',p0,p1)
print('PASS: FOUR FULL CHANNELS, TWO SAME-ROW SOURCE BEACONS, TWO DISTINCT PHYSICAL GATES')
print('NOT A SINGLE INTERVENTION-INDEPENDENT COMB / NO_HARDWARE / NO_GENERAL_NOVELTY')
