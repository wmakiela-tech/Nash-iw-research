"""LT5 ROT21: independent textbook-host witness, not a novel theorem.
Tests zero-state input/output equivalence versus hidden-state target recovery.
"""
import numpy as np
A=np.diag([0.5,2.0])
B=np.array([1.0,0.0])
C=np.array([1.0,0.0])
a,b,c=0.5,1.0,1.0
def full_run(x,us):
    obs=[]
    for u in us:
        obs.append(float(C@x))
        x=A@x+B*u
    obs.append(float(C@x))
    return np.array(obs),x
def reduced_run(x,us):
    obs=[]
    for u in us:
        obs.append(float(c*x))
        x=a*x+b*u
    obs.append(float(c*x))
    return np.array(obs),float(x)
us=np.array([0.7,-0.2,1.0,0.5])
x1=.31
N=len(us)
for hidden in (-1.,-.7,0.,.6,1.):
    y,final_x=full_run(np.array([x1,hidden]),us)
    yr,final_r=reduced_run(x1,us)
    assert np.max(np.abs(y-yr))<1.e-14
    assert abs(final_x[0]-final_r)<1.e-14
    assert abs(final_x[1]-(2**N)*hidden)<1.e-14
R0=1.
risk_no_sensor=(2**N)*R0
assert risk_no_sensor==16.
eta=.125
risk_new_sensor=(2**N)*min(R0,eta)
assert risk_new_sensor==2.
controllability=np.column_stack((B,A@B))
observability=np.vstack((C,C@A))
assert np.linalg.matrix_rank(controllability)==1
assert np.linalg.matrix_rank(observability)==1
assert max(abs(np.linalg.eigvals(A)))==2.
print("PASS: input/output-equivalent full and reduced LTI systems")
print("PASS: controllability and observability rank 1 < 2")
print("PASS: hidden-state target cannot be inferred from manifest data")
print("PASS: scalar target radius before sensor",risk_no_sensor,"after sensor",risk_new_sensor)
print("CEILING: mature systems-theory / optimal-recovery textbook host, not novelty")
