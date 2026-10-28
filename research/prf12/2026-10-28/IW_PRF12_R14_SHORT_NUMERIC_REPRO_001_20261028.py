#!/usr/bin/env python3
"""PRF12 R14: short independent n=3 source-support and source-reset check.
numpy required. Full SymPy proof/reproducer in R14 ZIP; NO closure LOCC claim.
"""
import numpy as np
from itertools import product
from math import exp
bits=np.array(list(product((0,1),repeat=3)))
I=np.eye(8)
S=np.zeros((8,8))
for k in range(4):
 ids=[j for j,v in enumerate(bits) if sum(v)==k]
 for a in ids:
  for b in ids:S[a,b]=1/len(ids)
Q=I-S
P=np.zeros((8,8))
for k in (1,2):
 ids=[j for j,v in enumerate(bits) if sum(v)==k]
 for a in ids:
  for b in ids:P[a,b]=1/3
K=S-P
X=np.array([[0,1],[1,0]])
swap=np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
anti=(np.eye(4)-swap)/2
for q in (.05,1/3,1,3):
 x=exp(-q)
 A=np.empty((8,8));B=np.empty((8,8))
 for i in range(8):
  for j in range(8):
   d=bits[i]-bits[j]
   A[i,j]=x**abs(sum(d))/8
   B[i,j]=x**sum(abs(d))/8
 rho=(np.eye(2)+x*X)/2
 assert np.linalg.norm(Q@A)<1e-12
 assert np.linalg.eigvalsh(B).min()>0
 assert abs(np.trace(Q@B)-(1-x*x)/2)<1e-12
 assert abs(np.trace(anti@np.kron(rho,rho))-(1-x*x)/4)<1e-12
 r=.37
 f=np.kron(np.kron(np.diag([1,r]),np.diag([1,r])),np.diag([1,r]))
 assert abs(np.trace(f@P/2)-(r+r*r)/2)<1e-12
 assert abs(np.trace(f@(I-P-K)/4)-(r+r*r)/2)<1e-12
 print('q',q,'global B-only',(1-x*x)/2,'local 2-run shared-xi B-only',(1-x*x)/4)
print('PASS. Fresh xi per run differs from one xi across runs. Full LOCC closure OPEN.')
