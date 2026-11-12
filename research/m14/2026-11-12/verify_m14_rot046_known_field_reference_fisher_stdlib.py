#!/usr/bin/env python3
"""ROT046 exact known-reference 3/4-axis full raw nuisance Fisher, stdlib only."""
from fractions import Fraction as Q
A=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))

def dot(x,y):return sum(a*b for a,b in zip(x,y))
def inv(matrix):
 n=len(matrix);M=[[Q(x) for x in matrix[i]]+[Q(int(i==j)) for j in range(n)] for i in range(n)]
 for j in range(n):
  pivot=next(k for k in range(j,n) if M[k][j])
  M[j],M[pivot]=M[pivot],M[j]
  val=M[j][j];M[j]=[x/val for x in M[j]]
  for k in range(n):
   if k==j:continue
   factor=M[k][j];M[k]=[M[k][q]-factor*M[j][q] for q in range(2*n)]
 return [x[n:] for x in M]
N=1200;sig2=Q(1);D=Q(1,50)
for r in (3,4):
 K=3+r;n=Q(N,2*r);I=[[Q(0) for j in range(K)] for i in range(K)]
 for i in range(r):
  onehot=[int(i==k) for k in range(r)]
  for x in (list(A[i])+onehot,[0,0,0]+onehot):
   for a in range(K):
    for b in range(K):I[a][b]+=n*Q(x[a])*x[b]/sig2
 C=inv(I);var=sum(C[j][j] for j in range(3))
 assert var==(Q(12,N) if r==4 else Q(18,N))
 floor=(D*D if r==4 else 3*D*D)
 assert var+floor==(Q(13,1250) if r==4 else Q(81,5000))
 print('r=',r,'exact nuisance profiled field variance=',var,'risk with drift=',var+floor)
# Comparative known-reference criterion, all per-run costs inside SAME N.
H_eps=Q(1,10)
assert Q(9)/(H_eps*H_eps-D*D)==Q(1875,2)
assert Q(3,N)+H_eps*H_eps==Q(1,80)
print('ROT046 STDLIB PASS: full raw reference Fisher, 3/4 axes, two-protocol crossover N>937.5')
