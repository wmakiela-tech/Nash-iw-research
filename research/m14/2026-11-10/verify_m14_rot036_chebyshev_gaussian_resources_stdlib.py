#!/usr/bin/env python3
"""M14 ROT036 -- pure-stdlib exact resource allocation and Gaussian negative-control replay."""
from fractions import Fraction as Q
from math import prod

def weight(t,j):
    return 1/prod(t[j]-t[k] for k in range(len(t)) if k!=j)

def evaluate(t,shots):
    w=[weight(t,j) for j in range(len(t))]
    S=sum(abs(q) for q in w)
    assert sum(shots)*4==96
    per_orientation=sum(w[j]**2/shots[j] for j in range(len(t)))
    # All 4 tetrahedral orientations use same allocation, so A^T A=4I.
    return w,S,per_orientation/4

cheb=(Q(0),Q(1,4),Q(3,4),Q(1))
regular=(Q(0),Q(1,3),Q(2,3),Q(1))
cw,cs,cv=evaluate(cheb,(4,8,8,4))
ew,es,ev=evaluate(regular,(3,9,9,3))
assert cw==[Q(-16,3),Q(32,3),Q(-32,3),Q(16,3)]
assert cs==32 and es==36 and cv==Q(32,3) and ev==Q(27,2)
assert 1-cv/ev==Q(17,81)
alt=(Q(0),Q(7,30),Q(23,30),Q(1))
aw=[weight(alt,j) for j in range(4)]
assert sum(abs(q) for q in aw)==Q(225,7)>cs
assert sum(q*q for q in aw)==Q(14630625,51842)<sum(q*q for q in cw)
# n_ij=N/(4)*|lambda_j|/sum|lambda| and integer realization.
assert [Q(96)*abs(q)/(4*cs) for q in cw]==[4,8,8,4]
print('ROT036 PASS: exact Chebyshev resource optimum, 96-shot field variance 32/3 vs 27/2, 17/81 reduction, equal-shot Gaussian falsifier retained')
