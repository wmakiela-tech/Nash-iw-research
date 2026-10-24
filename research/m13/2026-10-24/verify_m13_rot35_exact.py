#!/usr/bin/env python3
"""Independent standard library Fraction certificate for nested cube covariance and shell means."""
from fractions import Fraction as F
N=41
ks=range(2,7)
n=[(N-2*k)**3 for k in ks]
v=[n[i]-n[i+1] for i in range(4)]+[n[4]]
M=5
S=[[F(1,n[min(i,j)]) for j in range(M)] for i in range(M)]
B=[[F(0) for j in range(M)] for i in range(M)]
for i in range(4): B[i][i]=F(n[i],v[i]);B[i][i+1]=-F(n[i+1],v[i])
B[4][4]=F(1)
def mul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def transpose(A):return list(map(list,zip(*A)))
BSBT=mul(mul(B,S),transpose(B))
assert all(BSBT[i][j]==(F(1,v[i]) if i==j else 0) for i in range(M) for j in range(M))
# Exact invertibility, closed form covariance of nested means
assert sum(v)==n[0]
assert all(v_i>0 for v_i in v)
print('EXACT_INTEGER_SHELL_COUNTS:',v)
print('COV12_EXACT',S[0][1],'; CORR12² exact',F(n[1],n[0]))
print('COV26_EXACT',S[0][4],'; CORR26² exact',F(n[4],n[0]))
print('DIAGONAL_SHELL_COVARIANCE_PROVED_25_OF_25')
# Identity: shell summation weights reconstruct each old mask mean
for k in range(M):
 W=[F(v[i],n[k]) if i>=k else F(0) for i in range(M)]
 for z in range(M):
  assert sum(W[i]*B[i][z] for i in range(M))==(1 if z==k else 0)
print('MASKS_FROM_SHELLS_EXACT_25_OF_25')