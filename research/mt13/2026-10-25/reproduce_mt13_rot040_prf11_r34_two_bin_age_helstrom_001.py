#!/usr/bin/env python3
"""MT13 ROT040 PRF11 R34 age-labelled Poisson: source-local exact compressed decisions.
Standalone NumPy/SciPy; NOT quantum hardware. Full finite-n shared Cauchy
reproduction, JSON, and independent 16K-point integration in Moderator ZIP.
"""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.stats import poisson
from scipy.integrate import quad

a=4*math.log(2)
c=math.exp(-a/2)
baseline=(1-math.exp(-a))/2

def count_tv(beta):
    return math.exp(-beta/4)*(1+beta/4)-math.exp(-beta/4-a/2)*(1+beta/4+a/2)

def two_bin_tv(beta):
    return math.exp(-beta/4)*((1-c)*(1+3*beta/16)-a*c/4)

def full_age_tv(beta):
    assert 2*a/3<=beta<=a
    return count_tv(beta)+math.exp(-beta/4)*(a*c)**2/(4*beta*(1-c))

def enum_exact_two_bins(beta,K=30):
    muA=(beta/16,3*beta/16)
    muB=(muA[0]+a/4,muA[1]+a/4)
    ks=np.arange(K)
    p=np.outer(poisson.pmf(ks,muA[0]),poisson.pmf(ks,muA[1]))
    q=np.outer(poisson.pmf(ks,muB[0]),poisson.pmf(ks,muB[1]))
    # Exact NP test in the analytically proved parameter interval
    rule=(ks[:,None]+ks[None,:]>=2)|((ks[:,None]==1)&(ks[None,:]==0))
    assert 4*a/9<beta<4*a/3
    assert np.array_equal(rule,q>p)
    tv=.5*np.abs(p-q).sum()
    assert abs(tv-two_bin_tv(beta))<2e-14
    assert abs((q-p)[rule].sum()-tv)<2e-14

beta_count=brentq(lambda b:count_tv(b)-baseline,2,3,xtol=2e-14)
beta_2=brentq(lambda b:two_bin_tv(b)-baseline,3,3.2,xtol=2e-14)
assert 2*a/3<beta_count<a<beta_2<4*a/3
for b in (beta_count,beta_2,2.,2.8):
    enum_exact_two_bins(b)
cut=a*c/(beta_count*(1-c))
assert .3<cut<.5
# Full labelled optimum: K>=2 always B for beta_count<=a;
# K=1 favours B iff age u<cut. Janossy quadrature verifies equality.
signed=lambda u: math.exp(-beta_count/4)/2*(a*c-beta_count*(1-c)*u)
gain=quad(signed,0,cut,epsabs=1e-14)[0]
assert abs(full_age_tv(beta_count)-count_tv(beta_count)-gain)<2e-14
gainhalf=math.exp(-beta_count/4)/2*(a*c/2-beta_count*(1-c)/8)
assert abs(two_bin_tv(beta_count)-count_tv(beta_count)-gainhalf)<2e-14
# At beta_2 full age STRICTLY better: age cut is WITHIN young half.
u2=a*c/(beta_2*(1-c))
strict=math.exp(-beta_2/4)*beta_2*(1-c)/4*(.5-u2)**2
assert 0<u2<.5 and strict>.01
assert full_age_tv(beta_count)>two_bin_tv(beta_count)>baseline
print("PRF11 R34 FIRST source; MT13 two-bin local sufficiency, NOT novelty")
print("count critical beta",beta_count,"two-bin critical beta",beta_2)
print("noise budget improvement",beta_2/beta_count-1)
print("at beta_count: count",baseline,"two-bin",two_bin_tv(beta_count),
      "full exact",full_age_tv(beta_count),"optimal one-bit age cut",cut)
print("2-bin preserved labelled gain fraction",
      gainhalf/(full_age_tv(beta_count)-baseline))
print("additional full-age TV at beta_2 at least",strict)
print("PASS exact NP sign on full 30x30 two-bin Poisson enumeration and Janossy quadrature")
