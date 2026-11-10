#!/usr/bin/env python3
"""M14 ROT035: small exact rational replay, Python stdlib only.

This certifies selected rational instances and algebraic Chebyshev norm
formulas; the universal minimax proof appears in the accompanying report.
"""
from fractions import Fraction as Q
from math import factorial

def barycentric(x):
    return [1/prod(x[j]-x[k] for k in range(len(x)) if k!=j) for j in range(len(x))]

def prod(xs):
    y=Q(1)
    for x in xs:y*=x
    return y

def norm1(w):return sum(abs(v) for v in w)
def norm2_sq(w):return sum(v*v for v in w)
def dot(x,y):return sum(a*b for a,b in zip(x,y))

def verify(m,x):
    w=barycentric(x)
    assert [dot(w,[v**q for v in x]) for q in range(m+1)] == [Q(0)]*m+[Q(1)]
    return w

for m in range(1,9):
    L1_equal=Q(2**m*m**m,factorial(m))
    L1_cheb=Q(2**(2*m-1))
    assert L1_equal>=L1_cheb
    print('m',m,'equal_error_factor',L1_equal,'Chebyshev_minimax_factor',L1_cheb,'ratio',L1_equal/L1_cheb)

m=3
xe=[Q(0),Q(1,3),Q(2,3),Q(1)]
xc=[Q(0),Q(1,4),Q(3,4),Q(1)]
xa=[Q(0),Q(7,30),Q(23,30),Q(1)]
we,wc,wa=[verify(m,v) for v in (xe,xc,xa)]
assert norm1(we)==36 and norm1(wc)==32
assert wc==[Q(-16,3),Q(32,3),Q(-32,3),Q(16,3)]
assert norm1(wa)==Q(225,7)>norm1(wc)
assert norm2_sq(wa)==Q(14630625,51842)<Q(2560,9)==norm2_sq(wc)
assert norm2_sq(wc)-norm2_sq(wa)==Q(1039895,466578)>0

# Complete minimal-window raw-data alias: construct time errors and a
# degree m-1 calibration via Newton-free exact solve on first m timestamps.
A=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))

def interp_at_first_m(x,ys,at):
    total=Q(0)
    for j in range(m):
        ell=prod((at-x[k])/(x[j]-x[k]) for k in range(m) if k!=j)
        total+=ys[j]*ell
    return total

def witness(axis_count,base):
    delta=Q(1,100);kappa=32*delta
    for sign in (-1,1):
        z=[sign*kappa*u for u in base]
        for axis in A[:axis_count]:
            field=dot(axis,z)
            assert abs(field)<=kappa
            xi=[-field/norm1(wc)*(1 if w>0 else -1) for w in wc]
            assert max(abs(v) for v in xi)<=delta
            eta_points=[-field*x**m-n for x,n in zip(xc,xi)]
            # A degree <=m-1 interpolation also fits the final timestamp.
            assert interp_at_first_m(xc,eta_points,xc[m])==eta_points[m]
            assert all(field*x**m+e+n==0 for x,e,n in zip(xc,eta_points,xi))
    return True

assert witness(4,(1,0,0))
assert witness(3,(1,1,-1))
print('PASS: exact Chebyshev m3 sharp raw-data two-world aliases (3 and 4 axes)')
print('PASS: strict rational Gaussian-variance falsifier',norm2_sq(wc)-norm2_sq(wa))
print('ROT035_EXACT_STDLIB_PASS')
