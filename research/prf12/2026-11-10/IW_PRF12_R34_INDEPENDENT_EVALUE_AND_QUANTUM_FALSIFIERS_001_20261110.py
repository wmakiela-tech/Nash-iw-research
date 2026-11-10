#!/usr/bin/env python3
"""Independent R34 audit: test-martingale factor checks and quantum detector law.
Does not import the main R34 runner. A/B ALL-Xi certificates rely on the
separately archived and rerun original R31 source proof. Python numpy/scipy.
"""
import json, math
import numpy as np
from scipy.linalg import expm

# Independent nonstationary reference e-process one-step check using exact
# Bernoulli expectation over both possible current results.
rng=np.random.default_rng(991234)
max_overshoot=-1e100
for _ in range(200000):
    p=float(rng.random());q=float(rng.random());lam=float(rng.uniform(1e-5,.899))
    psi=-math.log1p(-lam)-lam
    test=(1-p)*math.exp(lam*(0-p)-psi*q*q) + p*math.exp(lam*(1-p)-psi*(1-q)**2)
    test_minus=(1-p)*math.exp(-lam*(0-p)-psi*q*q) + p*math.exp(-lam*(1-p)-psi*(1-q)**2)
    max_overshoot=max(max_overshoot,test-1,test_minus-1)
    assert test<=1+3e-14 and test_minus<=1+3e-14

# Malicious nonpredictable forecast q=X makes V_n identically 0; at true
# stationary p=1/2 the expected factor becomes cosh(lam/2)>1, NOT an e-factor.
lam=.68
bad_expected_factor=math.cosh(lam/2)
assert bad_expected_factor>1.05

# Source A independently computed from complex 2x2 unitaries.
I=np.eye(2,dtype=complex); X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.diag([1.,-1.]).astype(complex)
ket0=np.array([1.,0.],complex); tp=math.pi/20
w=np.array([.18,.20,.62]); alpha=np.array([.943,.907,.347]);beta=np.array([1.,1.,.018])
def ma(xi):
    state=expm(-.5j*(10*Y+xi*Z)*tp)@ket0
    state=expm(-.5j*xi*Z*.5)@state
    tx=expm(-.5j*(-10*Y+xi*Z)*tp)@state
    ty=expm(-.5j*(10*X+xi*Z)*tp)@state
    return np.array([np.vdot(tx,Z@tx).real,np.vdot(ty,Z@ty).real,np.vdot(state,Z@state).real])
def lb(H):
    return -1j*(np.kron(I,H)-np.kron(H.T,I))+.5*(np.kron(Z,Z)-np.eye(4))
def mb():
    density=np.outer(ket0,ket0.conj()).reshape(4,order='F')
    density=expm(tp*lb(5*Y))@density
    density=expm(.5*lb(np.zeros((2,2),complex)))@density
    mz=np.trace(density.reshape(2,2,order='F')@Z).real
    def read(h):return float(np.trace((expm(tp*lb(h))@density).reshape(2,2,order='F')@Z).real)
    return np.array([read(-5*Y),read(5*X),mz])
MB=mb();assert np.max(np.abs(MB-np.array([.5219734434954134,.00231335785212866,.04809737884883814])))<1e-12

def q(m,p0,p1):return (1+m)*p0/2+(1-m)*p1/2
def f(x,y,j):return alpha[j]*x*y+beta[j]*(1-x)*(1-y)
pref=(.99,3705/69000)
fixture=[]
for xi in [-35.,-17.4,-4.32,-1.,0.,1.2,3.14,12.,35.]:
    mz=ma(xi)
    score=float(sum(w[j]*f(q(mz[j],*pref),q(mz[j],*pref),j) for j in range(3)))
    fixture.append({'xi':xi,'source_score':score})
# Independently audit the 2S*delta perturbation for two unequal shot detectors.
S=float(sum(w*np.maximum(alpha,beta)))
assert abs(S-.59514)<1e-14
min_margin=1e100
for mm in [MB,*[ma(x) for x in (-35.,-4.32,0.,12.,35.)]]:
    for _ in range(10000):
        d=rng.uniform(-.012,.012,size=(2,2))
        q0=np.array([q(m,*pref) for m in mm])
        q1=np.array([q(m,*(np.array(pref)+d[0])) for m in mm])
        q2=np.array([q(m,*(np.array(pref)+d[1])) for m in mm])
        actual=float(sum(w[j]*f(q1[j],q2[j],j) for j in range(3)))
        ideal=float(sum(w[j]*f(q0[j],q0[j],j) for j in range(3)))
        bound=S*(max(abs(d[0]))+max(abs(d[1])))
        min_margin=min(min_margin,bound-abs(actual-ideal))
        assert actual-ideal<=bound+1e-13 and ideal-actual<=bound+1e-13

# Even perfect one-shot reference calibration does NOT guarantee conditional
# INDEPENDENCE of two science readouts. Shared latent latching yields same
# single-shot marginals q=.5 but completely different joint quartet law.
qhalf=.5; j=2
score_iid=f(qhalf,qhalf,j)
score_latched=alpha[j]*qhalf+beta[j]*(1-qhalf)
assert abs(score_iid-.09125)<.01 and abs(score_latched-score_iid)>.09
# Under unconstrained detector p0(t)=p1(t)=.5, the single-shot score cannot
# distinguish any source state, even when source A/B channel differs.
no_go_score=sum(w[j]*f(.5,.5,j) for j in range(3))

print(json.dumps({'audit':'PASS',
 'independent_one_step_EB_trials':200000,
 'largest_one_step_supermartingale_overshoot':max_overshoot,
 'after_outcome_predictor_q_equals_X_EXPECTATION_gt_one':bad_expected_factor,
 'source_B_independent_4x4':MB.tolist(),
 'source_A_2x2_control_fixture':fixture,
 'score_lipschitz_S':S,'minimum_drift_test_slack':min_margin,
 'correlated_detector_same_marginals_counterexample':{
    'joint_independent_score_Z':score_iid,'joint_shared_latch_score_Z':score_latched,
    'difference':score_latched-score_iid},
 'unrestricted_drift_source_blind_score':no_go_score,
 'scope':'only fixtures; all-Xi R31 independently rerun, not re-proved in this script; no hardware'},
 indent=2,sort_keys=True))
