"""LT5 ROT20. Independent exact-geometry controls for common gain,
componentwise relative and additive errors; mature optimal recovery host.
No historical DTC runtime or physical calibration validation.
"""
import numpy as np

def gain_interval(alpha, y, eta, rel, minimum, maximum, f):
    z=np.asarray(f(alpha),dtype=float)
    y=np.asarray(y,dtype=float)
    eta=np.asarray(eta,dtype=float)
    rel=np.asarray(rel,dtype=float)
    assert np.all(z>0) and np.all(rel<1) and maximum>=minimum>0
    lo=max(minimum,np.max((y-eta)/(z*(1+rel))))
    hi=min(maximum,np.min((y+eta)/(z*(1-rel))))
    return lo,hi,lo<=hi+1e-12

def pair_compatible(f0,f1,s0,s1,eta,rel):
    u=s0*np.asarray(f0);v=s1*np.asarray(f1)
    return bool(np.all(abs(u-v)<=rel*(u+v)+2*eta+1e-12))

rng=np.random.default_rng(20261024)
f=lambda a:np.array([1.,1+a,1+.3*a*a])
for i in range(2000):
    a,b=rng.uniform(0,.2,2)
    s,t=rng.uniform(.25,3,2)
    eta=np.array([.02,.015,.03])
    rel=np.array([.01,.005,.02])
    u=s*f(a);v=t*f(b)
    lo=np.maximum(u*(1-rel)-eta,v*(1-rel)-eta)
    hi=np.minimum(u*(1+rel)+eta,v*(1+rel)+eta)
    expected=bool(np.all(lo<=hi+1e-12))
    assert pair_compatible(f(a),f(b),s,t,eta,rel)==expected
    if expected:
        obs=.5*(lo+hi)
        assert gain_interval(a,obs,eta,rel,.25,3.,f)[2]
        assert gain_interval(b,obs,eta,rel,.25,3.,f)[2]
print("PASS: 2000 mixed-noise two-source rectangles")

eps=.005
A=.2
Q=((1+eps)/(1-eps))**2
R=.5*min(A,(1+A)*(1-1/Q))
assert abs(R-.011880894037276019)<1e-13
aa=(1+A)/Q-1;bb=A
assert abs((1+bb)/(1+aa)-Q)<1e-14
assert pair_compatible([1,1+aa],[1,1+bb],1/(1-eps),1/(1+eps),np.zeros(2),np.repeat(eps,2))
print("PASS: exact global relative-only risk",R)

g=lambda a:np.array([1.,1+a])
lo,hi,valid=gain_interval(.06,[1.,1.065],[.005,.005],[.005,.005],.5,2.,g)
assert valid and lo<=1<=hi
for aa in np.linspace(0,.2,101):
    assert np.all(np.abs(1e-11*g(aa))<1e-8)
print("PASS: vanishing gain + any absolute noise risk",A/2)

logerr=np.log((1+eps)/(1-eps))
r33=logerr/.8648869093985175
r34=logerr/.056593174
assert abs(r33-.011562301644)<1e-9 and abs(r34-.17670)<5e-5
print("PASS: M13 ROT33/34 two distinct relative inverse bounds",r33,r34)
print("LT5_ROT20_MIXED_NOISE_INFORMATION_RADIUS_SCOPED_PASS")
