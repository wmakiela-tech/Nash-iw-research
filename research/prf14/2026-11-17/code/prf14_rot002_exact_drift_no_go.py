#!/usr/bin/env python3
"""PRF14 ROT002: deterministic rational guards, not a hardware/physics experiment.

Source: PRF12 R34 p*= (99/100, 247/4600), delta*=0.009398133420642572.
Two C1 detector histories coincide on ALL t<=t0 and split only after t0.
"""
from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec = 60

p0 = Fraction(99, 100)
p1 = Fraction(247, 4600)  # = 3705/69000
half = Fraction(1, 2)
t0 = Fraction(1)
epsilon = Fraction(1, 100)
delta_star = Decimal('0.009398133420642572')

def smoothstep(u):
    if u <= 0:
        return Fraction(0)
    if u >= 1:
        return Fraction(1)
    return 3*u*u - 2*u*u*u

def drift(pstar, t):
    return pstar + (half-pstar)*smoothstep((t-t0)/epsilon)

def d(x):
    return Decimal(x.numerator) / Decimal(x.denominator)

# Coincidence for the entire calibration history and complete washout later.
for t in [Fraction(-1), Fraction(0), t0-Fraction(1, 1000), t0]:
    assert drift(p0,t)==p0 and drift(p1,t)==p1
for t in [t0+epsilon, t0+2*epsilon, Fraction(5)]:
    assert drift(p0,t)==half and drift(p1,t)==half
for p in [p0,p1]:
    assert drift(p,t0+epsilon/2)==(p+half)/2

# derivative of cubic ramp reaches 1.5*|delta|/epsilon at u=1/2.
nu0 = Fraction(3,2)*abs(half-p0)/epsilon
nu1 = Fraction(3,2)*abs(half-p1)/epsilon
assert d(abs(half-p0))>delta_star
assert d(abs(half-p1))>delta_star
assert nu0==Fraction(147,2) and nu1==Fraction(6159,92)

# Randomized interleaving: m uniform times, a bump on fraction w/T of window.
m=100
support_fraction=Fraction(1, 10000)
no_hit=(1-support_fraction)**m
assert no_hit>Fraction(99,100)
print('R34 original p0:',d(p0))
print('R34 original p1:',d(p1))
print('science p0=p1:',d(half))
print('max |future p - p*|:',d(abs(half-p0)),d(abs(half-p1)))
print('max |dp/dt| for epsilon=.01:',d(nu0),d(nu1))
print('P(no random reference hits support), m=100, width/T=1e-4:',d(no_hit))
print('PASS: exact rational calibration-alias and interleaving failure lower bound')
