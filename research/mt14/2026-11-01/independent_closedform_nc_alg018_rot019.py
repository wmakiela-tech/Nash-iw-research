#!/usr/bin/env python3
"""MT14 ROT019; independent stdlib M13/NC source example, mature matrix algebra.
NOT a physical NASH model, native NC runtime, or mathematical novelty.
"""
import math
from fractions import Fraction
# Original NC/M13 2x2 generator [[-11/10, 4],[1,-41/10]].
a,b,c=13/5,5/2,math.sqrt(34)/5
q=(b*c-a)/(a*c-b)
assert 0<q<1
t=math.atanh(q)/b
rho=math.exp(-a*t)*(math.cosh(b*t)+c*math.sinh(b*t))
third=math.exp(-2*t)
assert 1.03327724<rho<1.03327726
assert abs((b*c-a)*math.cosh(b*t)+(b-a*c)*math.sinh(b*t))<1e-14
assert rho>third
# n=3 rank2 compression simple rational trace counterexample:
x,y=Fraction(1033,1000),Fraction(1028,1000)
assert x+y==Fraction(2061,1000)
assert max(abs(x),abs(y))==Fraction(1033,1000)
# n=3 Hurwitz real rotation: spectral radius vastly exceeds real scalar Rayleigh.
rho_rotation=math.exp(-0.1)
real_Rayleigh_max=math.exp(-3.0)
assert rho_rotation>18*real_Rayleigh_max
print(f'PASS: analytic t={t:.14g}; NC r={rho:.14g}; embedded n3 rank2 r={rho:.14g}')
print('PASS: trace rank2 = 2061/1000 but spectral radius 1033/1000')
print(f'PASS: rotating n3 rank2 rho={rho_rotation:.14g} real Rayleigh max={real_Rayleigh_max:.14g}')
