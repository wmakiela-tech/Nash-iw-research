"""INT8 ROT010: synthetic tests of a legal QND instrument and outcome-information budget.
No physical NASH detector or continuum model is represented.
"""
import math
import itertools
import numpy as np

I=np.eye(2,dtype=complex)
Z=np.diag([1,-1]).astype(complex)

def kraus(y,s):
    assert y in (-1,1) and 0<s<1
    E=(I+y*s*Z)/2
    return np.diag(np.sqrt(np.diag(E).real))

def record_prob(theta,s,sequence):
    state=(I+theta*Z)/2
    for y in sequence:
        K=kraus(y,s)
        state=K@state@K.conj().T
    return float(np.trace(state).real)

def mixture_prob(theta,s,sequence):
    return sum((1+a*theta)/2*np.prod([(1+a*y*s)/2 for y in sequence]) for a in (-1,1))

def f(z):
    return (1+z)/2*math.log1p(z)+(1-z)/2*math.log1p(-z)

for s in (.1,.36,.79):
    assert np.allclose(sum((kraus(y,s)@kraus(y,s) for y in (-1,1))), I)
    for th in (-.73,0.,.41):
        seqs=list(itertools.product((-1,1),repeat=4))
        probs=np.array([record_prob(th,s,y) for y in seqs])
        expect=np.array([mixture_prob(th,s,y) for y in seqs])
        assert np.max(np.abs(probs-expect))<1e-13
        assert abs(probs.sum()-1)<1e-13
    assert f(s) <=s*s/(2*(1-s*s)) +1e-14
    print(f'QND s={s} Kraus, 4-shot probabilities, KL inequality: PASS')

R=.6;B=1.
for s in (.2,.1,.05,.02,.01,.005):
    N=math.floor(B/s)
    eta=R*R*s/(1+(N-1)*s*s)
    ES=N*s*R
    ES2=N*(1-s*s)+N*N*s*s
    worst_mse=R*R-2*eta*R*ES+eta*eta*ES2
    explicit=R*R-R**4*N*s*s/(1+(N-1)*s*s)
    assert abs(worst_mse-explicit)<1e-12
    assert 2*eta*N*s <=1
    Dmax=s*B/(2*(1-s*s))
    risk_floor=R*R*max(0,1-4*Dmax)
    assert worst_mse>=risk_floor-1e-12
    print(f's={s:.3f} N={N} QND worst_Risk={worst_mse:.9f} gap={R*R-worst_mse:.9f} gap_over_s={(R*R-worst_mse)/s:.9f} risk_lower={risk_floor:.8f}')
print('ALL_PASS; proof uses Born rule and sequential KL independent of QND example')
