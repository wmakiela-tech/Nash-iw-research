import math
import numpy as np

def run(q=2.0, kappa=0.5, s=1e-3, c=2.0):
    r = kappa*s
    Q1 = np.array([[1-r,0],[q*r,1.0]])
    Q2 = np.array([[1.0,q*r],[0,1-r]])
    B = Q2 @ Q1
    W = np.array([[1+q*q*r*r,q*r],[q*r,1.0]])
    vals, vecs = np.linalg.eig(B)
    i = int(np.argmax(vals.real))
    lam = float(vals[i].real)
    v = vecs[:,i].real
    v = v/np.linalg.norm(v)
    A = float(v @ W @ v)
    Btarget = c*math.log(1/s)
    M = max(1, int(round(Btarget/(2*s))))
    Btot = 2*M*s
    exact = s*s*A*(lam**(2*M)-1)/(lam*lam-1)
    asym = s/(2*(q-1)*kappa)*(math.exp((q-1)*kappa*Btot)-1)
    return exact, asym, exact/asym, Btot

if __name__ == "__main__":
    for c in [1.5,2.0,2.5]:
        for s in [1e-2,5e-3,2e-3,1e-3]:
            print(c, s, run(s=s,c=c))
    s=1e-3
    M=5000
    Btot=2*M*s
    print("raw", M*s*s, 0.5*s*Btot)
