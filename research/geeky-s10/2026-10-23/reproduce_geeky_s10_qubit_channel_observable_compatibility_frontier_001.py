import math
import numpy as np

I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.array([[1,0],[0,-1]],complex)

def frontier(a,t):
    return 0.5*((1-a)+math.sqrt((1+a)**2-4*t*t))

def threshold_instrument(s):
    a=1-s
    u=math.sqrt(a)
    p0=(1+a+2*u)/4
    p1=(1+a-2*u)/4
    q=s/4
    Kp=[(math.sqrt(p0)*I+math.sqrt(p1)*X)/math.sqrt(2),
        math.sqrt(q/2)*(Y-1j*Z)]
    Km=[(math.sqrt(p0)*I-math.sqrt(p1)*X)/math.sqrt(2),
        math.sqrt(q/2)*(Y+1j*Z)]
    return Kp,Km,a,u

def effect(Ks):
    return sum(K.conj().T@K for K in Ks)

def channel(Kp,Km,A):
    return sum(K@A@K.conj().T for K in Kp+Km)

for s in [0.1,0.3,0.7]:
    Kp,Km,a,t=threshold_instrument(s)
    assert np.linalg.norm(effect(Kp)-(I+s*X)/2)<1e-12
    assert np.linalg.norm(effect(Km)-(I-s*X)/2)<1e-12
    assert np.linalg.norm(channel(Kp,Km,X)-a*X)<1e-12
    assert np.linalg.norm(channel(Kp,Km,Y)-t*Y)<1e-12
    assert np.linalg.norm(channel(Kp,Km,Z)-t*Z)<1e-12
    assert abs(frontier(a,t)-s)<1e-12

    t_near=1-s/2
    assert abs(frontier(a,t_near)-s/2)<1e-12

print("PASS")
