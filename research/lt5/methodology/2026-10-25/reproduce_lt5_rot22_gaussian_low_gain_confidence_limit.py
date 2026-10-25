"""LT5 ROT22 — Gaussian low-gain statistical information lower bound.
Classical Le Cam/total variation and Gaussian-cone projection; NO novel math,
historical DTC replay, validated physical noise or measured signal.
"""
import numpy as np
from scipy.stats import chi2, norm
from scipy.optimize import brentq

L = .2
coverage = .95
cdf = lambda c: .5*chi2.cdf(c, 4) + .5*chi2.cdf(c, 5)
c95 = brentq(lambda c: cdf(c) - coverage, 1, 30)
assert abs(c95 - 10.371033903003577) < 1e-10
f = lambda a: np.array([1, 1+.5*a, 1+.1*a*a, 1+a, 1+2*a])
fa, fb = f(0), f(L)
for t in [0., 1.e-5, .001, .01]:
    separation = t*np.linalg.norm(fa-fb)
    tv = 2*norm.cdf(separation/2)-1
    point_risk_lower = L*(1-tv)/2
    expected_set_length_lower = L*max(0, coverage-t*np.linalg.norm(fa)/2)
    print(t, tv, point_risk_lower, expected_set_length_lower)
assert abs(L/2 - .1) < 1.e-15
assert abs(coverage*L - .19) < 1.e-15
necessary_snr = 2*norm.ppf((1+coverage-.02/L)/2)
assert abs(necessary_snr-2.8790629418769127)<1e-12

# Exactly 40000 independently generated standard Gaussian five-vectors:
# under t=0 the fixed-alpha cone statistic has chi-bar mixture law for all alpha.
rng = np.random.default_rng(20261025)
X = rng.standard_normal((40000, 5))
alphas = np.linspace(0, L, 201)
F = np.array([f(a) for a in alphas])
U = F/np.linalg.norm(F, axis=1)[:, None]
Q = (X*X).sum(axis=1)[:, None] - np.maximum(0, X@U.T)**2
accept = Q <= c95
observed_coverage = accept.mean(axis=0)
mean_length = np.trapezoid(accept.astype(float), alphas, axis=1).mean()
assert np.max(np.abs(observed_coverage-coverage)) < .009
assert abs(mean_length - coverage*L) < .002
print("cutoff=", c95, "expected_length=", mean_length,
      "theoretical=", coverage*L, "SNR_necessary=", necessary_snr)
print("PASS: 40000 independent synthetic Gaussian samples, no physical signal")
