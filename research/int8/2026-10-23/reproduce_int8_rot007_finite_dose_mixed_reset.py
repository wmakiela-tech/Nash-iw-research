"""INT8 ROT007: exact scalar Fisher/state-noise split and frozen-history heterogeneous check.
PUBLIC synthetic mathematical controls, not source-valid device models.
Requires numpy, scipy.
"""
import math
import numpy as np
from scipy.linalg import expm

def scalar_exact(s: float, B: float = 1.0, sigma: float = .3):
    N = math.floor(B / s)
    fisher = N * s**2 / sigma**2
    state_var = sigma**2 * (1.0 - (1.0-s)**(2*N)) / (s*(2-s))
    return N, fisher, state_var

for s in (.1, .02, .005, .001):
    N,I,V = scalar_exact(s)
    print(f"s={s:.4g}, N={N}, I={I:.10g}, VarPost={V:.10g}")
    assert abs(I-N*s*s/.09) < 1e-12
    assert V > 0
    target_limit = .09*(1-math.exp(-2.0))/2
    if s <= .005:
        assert abs(s*V-target_limit) < .001

rng = np.random.default_rng(23010)
G = np.array([[-.6,1.],[-.4,-.3]], dtype=float)
v = np.array([.8,-.6], dtype=float)
n = 52
T = 1.5
eps = .025
times = np.sort(rng.uniform(0,T,n))
ss = rng.uniform(0,eps,n)
alphas = rng.uniform(0,1,n)
es = rng.normal(size=(n,2))
ds = rng.normal(size=(n,2))
es /= np.linalg.norm(es,axis=1)[:,None]
ds /= np.linalg.norm(ds,axis=1)[:,None]
zpath = rng.normal(0,.2,n)

def frozen_history_means(theta):
    x = theta*v.copy()
    tprev = 0.0
    out = []
    for t,s,alpha,e,d,z in zip(times,ss,alphas,es,ds,zpath):
        x = expm(G*(t-tprev)) @ x
        tprev = t
        out.append(float(s*(e@x)))
        x = x-d*((1-alpha)*s*(e@x)+alpha*z)
    return np.array(out)

m0 = frozen_history_means(0.)
c = (frozen_history_means(1.25)-m0)/1.25
aff_err = np.max(np.abs(frozen_history_means(-.5)-m0+.5*c))
mu_plus = max(0.,float(np.linalg.eigvalsh((G+G.T)/2).max()))
dose = float(ss.sum())
bound = eps*dose*math.exp(2*mu_plus*T+2*dose)*float(v@v)
actual = float(c@c)
print(f"frozen affine residual={aff_err:.3e}, sensitivity energy={actual:.10g}, ceiling={bound:.10g}")
assert aff_err < 1e-12
assert actual <= bound
print("PASS: conditional-parameter-sensitivity and fixed-dose Fisher controls")
