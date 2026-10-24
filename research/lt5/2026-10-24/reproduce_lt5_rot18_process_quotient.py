"""LT5 ROT18: independently test one PRF11 R29 echo witness and a classical full quotient.
Scoped numerical/symbolic arithmetic only, not external mathematical referee or hardware.
"""
import math
import numpy as np

rng = np.random.default_rng(20261024)
X = np.array([[0,1],[1,0]], dtype=complex)
Z = np.diag([1,-1]).astype(complex)
ket = np.ones((2,1), dtype=complex)/math.sqrt(2)
rho = ket@ket.conj().T
GAMMA=.7

def U(phi):
    return np.diag([np.exp(-0.5j*phi),np.exp(0.5j*phi)])

def channel(state,t):
    w=(1+math.exp(-GAMMA*t))/2
    return w*state+(1-w)*Z@state@Z

def echo(state,a,b):
    w=U(a)@state@U(a).conj().T
    w=X@w@X
    w=U(b)@w@U(b).conj().T
    return X@w@X

max_err=0
for a,b in [(0.1,0.4),(0.3,0.3),(-2.4,1.3)]:
    exact=U(a-b)@rho@U(a-b).conj().T
    max_err=max(max_err,float(np.max(np.abs(echo(rho,a,b)-exact))))
assert max_err < 1e-14
for s,t in [(0.1,0.3),(.5,.75),(2.,1.3)]:
    assert np.max(np.abs(channel(channel(rho,s),t)-channel(rho,t+s)))<1e-14
T=2
pb=float(np.real(np.trace(rho@channel(rho,T))))
tv=1-pb
assert abs(tv-(1-math.exp(-GAMMA*T))/2)<1e-14

# Fresh Cauchy increments, independent from the source author's code.
n=250_000
a=rng.standard_cauchy(n)*GAMMA
b=rng.standard_cauchy(n)*GAMMA
cohB=float(np.mean(np.cos(a-b)))
assert abs(cohB-math.exp(-2*GAMMA))<.012

# Positive transfer theorem: classical two-block state, reduction sums sectors.
r=np.block([np.eye(2),np.eye(2)])
M=np.diag([.6,.8])
I=np.block([[M,np.zeros((2,2))],[np.zeros((2,2)),M]])
max_transfer=0
for _ in range(100):
    full=rng.random(4)
    reduced=r@full
    for dt in (.4,.8,.2,.5):
        lam=math.exp(-.2*dt)
        full=lam*full
        reduced=lam*reduced
        full=I@full
        reduced=M@reduced
    max_transfer=max(max_transfer,float(np.max(np.abs(r@full-reduced))))
assert max_transfer<1e-14
# Same reduction, different intervention outputs: no factored i can exist.
Ibad=np.diag([.1,.5,.9,.5])
s1=np.array([1.,0.,0.,0.]);s2=np.array([0.,0.,1.,0.])
assert np.allclose(r@s1,r@s2)
assert abs((r@Ibad@s1-r@Ibad@s2)[0])>.7

# Source-valid event sampling gap arithmetic: NOT original Julia interpolant.
edge=51.09825802317032
cut=51.33592433955715
last=49.96189862690079
firstoff=52.25910204802943
ratio=(firstoff-last)/(cut-edge)
assert abs(ratio-9.665666789)<2e-8

print('PASS: echo matrix maxerr',max_err)
print('PASS: gamma=.7 T=2 experimental TV',tv)
print('PASS: independent Cauchy Monte Carlo coherence',cohB,
      'absolute deviation',abs(cohB-math.exp(-2*GAMMA)))
print('PASS: 100 full-quotient branch transfer maxerr',max_transfer)
print('PASS: source event sampled-gap/lifetime ratio',ratio)
print('LT5_ROT18_SCOPED_CONTROLS_PASS')
