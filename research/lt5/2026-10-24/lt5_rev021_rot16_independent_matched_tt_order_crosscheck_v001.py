"""LT5 REV021 ROT16: source-independent, 100-case symbolic Fourier/TT witness check.
Checks Geeky-S11 ROT007 exact order-2/order-4 matched TT checkerboard construction.
Not a source-helper, original production runner, full FFT or physical simulation.
"""
import numpy as np
from math import pi, sqrt

p = 4 - sqrt(2)
rhoA = 16*sqrt(9217)/9281
rhoB = 8*sqrt(2114)/1089
A0 = (4*sqrt(2)-1)*rhoA/(12*pi)
B0 = (4*sqrt(2)-1)*rhoB/(12*pi)
alpha_star = (A0+B0)/(p*A0+4*B0)
lower = A0*B0*(4-p)/(p*A0+4*B0)

def symbol(k, N, order):
    theta=2*pi*np.asarray(k)/N
    if order == 2:
        return np.sin(theta)*N/(2*pi)
    return np.sin(theta)*(4-np.cos(theta))*N/(6*pi)

def TT(T, d):
    if np.linalg.norm(d)<1e-12:
        return np.zeros((3,3))
    v=d/np.linalg.norm(d)
    P=np.eye(3)-np.outer(v,v)
    return P@T@P-0.5*P*np.trace(P@T)

count=0
for N in (8,16,24,32,64):
    for label,k in [('A',np.array([N//8,N//4,0])),
                    ('B',np.array([N//8,3*N//8,0]))]:
        for order in (2,4):
            d=symbol(k,N,order)
            v=np.array([d[1],-d[0],0.])/np.linalg.norm(d)
            z=np.array([0.,0.,1.])
            T=np.outer(v,v)-np.outer(z,z)
            assert np.linalg.norm(TT(T,d)-T,'fro') < 1e-12
            d_shift=symbol((k+N//2)%N,N,order)
            leakage=np.linalg.norm(T-TT(T,d_shift),'fro')/np.linalg.norm(T,'fro')
            pref=abs(d[0])*leakage
            target=N*(A0 if label=='A' else B0) if order==4 else 0.
            assert abs(pref-target)<2e-12
            for alpha in (0., .05, alpha_star, 1/p, .25):
                scalar=1-4*alpha*np.sum(np.sin(pi*k/N)**2)
                predicted=pref*abs(scalar)
                expected=(N*A0*abs(1-p*alpha) if label=='A'
                    else N*B0*abs(1-4*alpha)) if order==4 else 0.
                assert abs(predicted-expected)<3e-12, (N,label,order,alpha)
                count += 1
assert count==100
assert abs(A0*abs(1-p*alpha_star)-B0*abs(1-4*alpha_star))<1e-14
assert abs(lower-A0*abs(1-p*alpha_star))<1e-14
print('PASS: 100 matched-symbol TT checks N={8,16,24,32,64}; '
      f'alpha*={alpha_star:.17g}; lower={lower:.17g} * N')
