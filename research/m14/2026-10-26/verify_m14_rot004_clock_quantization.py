#!/usr/bin/env python3
"""M14 ROT004 standard-library numeric control; mathematical proof in Markdown."""
import math, cmath, json
A,B=.75,1.25
Z=(math.exp(2*B)-math.exp(2*A))/2-(B-A)
def expint(c,l,r):
    return complex(r-l) if abs(c)<1e-13 else (cmath.exp(c*r)-cmath.exp(c*l))/c
def h1(w,l=A,r=B):
    return 2*(expint(1+1j*w,l,r)-expint(-1+1j*w,l,r))/Z
def h2(w,l=A,r=B):
    return 8*(expint(2j*w,l,r)-expint(-2+2j*w,l,r))/Z
def quad(f,l,r,n=20000):
    assert n%2==0
    h=(r-l)/n
    total=f(l)+f(r)
    for k in range(1,n):
        total+=(4 if k%2 else 2)*f(l+h*k)
    return total*h/3
def q1(w,l=A,r=B):
    return quad(lambda t:2/Z*(math.exp(t)-math.exp(-t))*cmath.exp(1j*w*t),l,r)
def q2(w,l=A,r=B):
    return quad(lambda t:8/Z*(1-math.exp(-2*t))*cmath.exp(2j*w*t),l,r)
def pmass(l,r):
    return ((math.exp(2*r)-math.exp(2*l))/2-(r-l))/Z
def rcov(l,r):
    return 4*((r-l)-(math.exp(-2*l)-math.exp(-2*r))/2)/(Z*pmass(l,r))
bins=[(A,.9),(.9,1.07),(1.07,B)]
for w in (0,1.5,21,177):
    assert abs(h1(w)-q1(w))<2e-8
    assert abs(h2(w)-q2(w))<2e-8
assert abs(sum(pmass(*x) for x in bins)-1)<1e-13
rad=rcov(A,B)
assert abs(rad-quad(lambda t:4*(1-math.exp(-2*t))/Z,A,B))<2e-11
assert abs(sum(pmass(*x)*rcov(*x) for x in bins)-rad)<1e-13
assert all(rcov(*x)>0 for x in bins)
for w in (200,2000,20000):
    for l,r in bins:
        assert abs(h1(w,l,r))<=4*(math.exp(r)-math.exp(-r))/(Z*w)*(1+1e-12)
res={'return_id':'M14_ROT004_CLOCK_QUANTIZATION_TV_COLLAPSE_001_20261026',
     'status':'PASS_STANDARD_LIBRARY_NUMERIC_CHECKS_NOT_THEOREM_PROVER',
     'Z':Z, 'radial_covariance_independent_of_omega':rad,
     'bin_stats':[{'bin':x,'prob':pmass(*x),'radial_cov':rcov(*x)} for x in bins],
     'harmonic_trend':[{'omega':w,'abs_h1':abs(h1(w)),'abs_h2':abs(h2(w)),
              'bin_abs_h1':[abs(h1(w,*x))/pmass(*x) for x in bins]} for w in (0,2,20,200,2000,20000)],
     'proof':'SEE_PAIRED_REPORT','BW_INGEST':'UNVERIFIED',
     'no_novelty':True,'no_physics':True}
print(json.dumps(res,indent=2,ensure_ascii=False))
