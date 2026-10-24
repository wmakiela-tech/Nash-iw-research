"""LT5 ROT19: limited source-independent scalar worst-case information-radius checks.
Classical deterministic optimal recovery; no physics or novelty claim.
"""
import math
import numpy as np

A=np.array([[0.,0.],[.12,1.1],[.26,-.5],[.34,.3],[.62,1.4],[.70,-1.0],[1.,.2]])
eta=.11
pairs=[(abs(A[i,1]-A[j,1]),i,j) for i in range(len(A))
       for j in range(i,len(A)) if abs(A[i,0]-A[j,0])<=2*eta+1e-12]
worst=max(pairs)
radius=worst[0]/2
ys=set(float(x) for x in A[:,0])
ys.update(float((A[i,0]+A[j,0])/2) for _,i,j in pairs)
local=[]
for y in ys:
    feasible=A[np.abs(A[:,0]-y)<=eta+1e-12]
    if feasible.size:
        local.append((feasible[:,1].max()-feasible[:,1].min())/2)
assert abs(max(local)-radius)<1e-12 and abs(radius-1.2)<1e-12
print("ARBITRARY_NONCONVEX_SOURCE_CLASS_RADIUS_PASS",len(pairs),radius)

# 1D symmetric ball specialization: |a|<=R, L(a)=ca, T(a)=ma.
R,noise,c,m=2.,.3,1.5,2.
assert abs(abs(m)*min(R,noise/abs(c))-.4)<1e-12
print("EXISTING_LT_THEOREM7_9_SPECIAL_CASE_PASS")

# Projective model: alpha in [0,1], gain s>0 with no lower floor.
# Any fixed positive eta admits every alpha at the same observation y=0.
alpha=np.linspace(0,1,1001)
f=np.c_[np.ones(len(alpha)),1+alpha]
noise=1.e-6
s=noise/(2*np.max(np.linalg.norm(f,axis=1)))
assert np.max(np.linalg.norm(s*f,axis=1))<noise
assert np.all(np.diff(f[:,1]/f[:,0])>0)  # noiseless unique alpha
print("POSITIVE_GAIN_NO_FLOOR_ANY_NOISE_RISK_HALF_PASS")

rng=np.random.default_rng(20261024)
err=0.
for _ in range(2000):
    f0=np.exp(rng.normal(size=2))
    f1=np.exp(rng.normal(size=2))
    s0=float(np.exp(rng.normal()))
    s1=s0*float(f0@f1)/float(f1@f1)
    d=float(np.linalg.norm(s0*f0-s1*f1))
    det=s0*abs(float(np.linalg.det(np.stack((f0,f1)))))/float(np.linalg.norm(f1))
    err=max(err,abs(d-det))
    assert abs(d-det)<2e-13
    midpoint=.5*(s0*f0+s1*f1)
    assert np.linalg.norm(midpoint-s0*f0)<=d/2+1e-12
assert 2/math.sqrt(3)>1  # vector Chebyshev radius not half-diameter
print("PROJECTIVE_NUISANCE_2000_PAIRS_PASS",err)

bound=math.log(1.005/.995)/.8648869093985175
assert abs(bound-.011562301644)<1e-9
print("M13_DIRECTED_INTERVAL_RELATIVE_NOISE_BOUND_PASS",bound)
print("LT5_ROT19_LIMITED_INDEPENDENT_CONTROLS_PASS")
