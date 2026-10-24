#!/usr/bin/env python3
"""ROT32 exact rational-Bernstein sign audit for PUBLISHED DECIMAL polynomial coefficients.
DO NOT confuse sign proof for decimal snapshots with rigorously enclosed
transcendental Fourier coefficients of the original physical/source model.
"""
import json,math
from pathlib import Path
from fractions import Fraction as F
P=Path(__file__).resolve().parent
D=json.loads((P/'IW_M13_ROT32_alpha_amplitude_identifiability_20261024.json').read_text())
assert len(D['cases'])==10

def conv(a,b):
 z=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]+=x*y
 return z

def poly_sub(a,b):
 n=max(len(a),len(b));return [(a[i] if i<len(a) else F(0))-(b[i] if i<len(b) else F(0)) for i in range(n)]

def diff(a):return [i*a[i] for i in range(1,len(a))]

def eval_poly(a,x):return sum(v*x**i for i,v in enumerate(a))

def bernstein(a):
 n=len(a)-1;return [sum(a[j]*F(1,5)**j*F(math.comb(k,j),math.comb(n,j)) for j in range(k+1)) for k in range(n+1)]

for case in D['cases']:
 G={k:[F(str(v)) for v in vals] for k,vals in case['G_quartic_squared_RMS'].items()}
 assert all(len(v)==5 for v in G.values())
 p=poly_sub(conv(diff(G['A']),G['C']),conv(G['A'],diff(G['C'])))
 B=bernstein(p)
 assert len(B)==8 and all(b<0 for b in B),(case['N'],case['mask_k'])
 upper_A=max(bernstein(G['A']));upper_C=max(bernstein(G['C']))
 assert upper_A>0 and upper_C>0
 lower_abs_log=-max(B)/(2*upper_A*upper_C)
 assert lower_abs_log>F(4,5),(case['N'],case['mask_k'],float(lower_abs_log))
 # direct values at alpha=0 and 1/5 for A/C strictly ordered
 assert G['A'][0]*eval_poly(G['C'],F(1,5)) > eval_poly(G['A'],F(1,5))*G['C'][0]
 # k3 A/B noninjectivity: derivative positive at alpha0,
 # derivative negative by 0.005, and ratio crosses original value
 if case['mask_k']==3:
  d=poly_sub(conv(diff(G['A']),G['B']),conv(G['A'],diff(G['B'])))
  assert eval_poly(d,F(0))>0 and eval_poly(d,F(1,200))<0
  h=lambda x: eval_poly(G['A'],x)*G['B'][0]-G['A'][0]*eval_poly(G['B'],x)
  assert h(F(1,100000))>0 and h(F(1,100))<0
 print('DECIMAL_BERNSTEIN_PASS',case['N'],case['mask_k'],'margin normalized',float(max(B)/(G['A'][0]*G['C'][0])))
print('ALL_10_DECIMAL_MODELS_PROVEN_IN_EXACT_RATIONAL_ARITHMETIC',len(D['cases']))