#!/usr/bin/env python3
"""M14 ROT037 -- no-dependency EXACT witness for polynomial adaptive minimax bound.
The global adaptive/Bayes argument is in the companion theorem report, not a stochastic proof by tests.
"""
from fractions import Fraction as Q
from math import prod

A=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
t=(Q(0),Q(1,4),Q(3,4),Q(1))
w=[1/prod(t[j]-t[k] for k in range(4) if k!=j) for j in range(4)]
assert w==[Q(-16,3),Q(32,3),Q(-32,3),Q(16,3)]
assert sum(abs(a) for a in w)==32
for degree in range(4):
    assert sum(w[j]*t[j]**degree for j in range(4))==int(degree==3)

# Monic Chebyshev least-favorable submodel P3(t)=T3(2t-1)/32,
# where the unknown quadratic drift exactly cancels the lower coefficients.
def P(t):return t**3-Q(3,2)*t**2+Q(9,16)*t-Q(1,32)
assert [P(z) for z in t]==[Q(-1,32),Q(1,32),Q(-1,32),Q(1,32)]
assert P(Q(1,2))==0
for a in A:
    assert all((a[0]*P(t[j]))**2==Q(1,1024) for j in range(4))

# Every orientation has the same divided-difference error variance, but
# the two experimental contracts allocate the same N=144 differently.
def contrast_variance(shots):return sum(w[j]**2/shots[j] for j in range(4))
v4=contrast_variance((6,12,12,6))
v3=contrast_variance((8,16,16,8))
assert sum((6,12,12,6))*4==sum((8,16,16,8))*3==144
assert v4==Q(256,9) and v3==Q(64,3)
# tetrahedral A^T A=4I; trace 4-axis cov = 3 v4/4.
risk4=3*v4/4
# A3 inverse has squared column norms 1/2; trace 3-axis cov = 3 v3/2.
risk3=3*v3/2
assert risk4==Q(64,3) and risk3==32 and risk3/risk4==Q(3,2)

# The least-favorable 3D prior u ~ N(0,tau^2 I), tau^2=10000.
# With Cheb allocation, the pathwise posterior precision is scalar
# prior_precision+N/(2^(2m-1))^2 for each of the 3 components.
N=144; C=32; prior_prec=Q(1,10000)
assert sum(shots*P(time)**2 for time,shots in zip(t,(6,12,12,6)))==Q(36,1024)
finite_prior_bayes=Q(3)/(prior_prec+Q(N,C*C))
assert finite_prior_bayes==Q(120000,5629)
assert risk4==Q(3*C*C,N)
print('ROT037 stdlib exact PASS: global 4-axis 64/3, 3-axis 32, ratio 3/2, P3 midpoint blind, finite Bayes limit')
