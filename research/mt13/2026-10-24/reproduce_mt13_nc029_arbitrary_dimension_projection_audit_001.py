#!/usr/bin/env python3
"""MT13 NC-OPN-002 independent concise 3D/4D, spectral and resource tests.
Needs NumPy/SciPy. Source-native NC ART029 code NOT executed here.
"""
import numpy as np
from scipy.linalg import expm
from numpy.linalg import eigvalsh, eigvals, norm

def mu2(g): return eigvalsh((g+g.T)/2)[-1]
def witness(g,dt):
    m=expm(g*dt)
    _,v=np.linalg.eigh((g+g.T)/2);w=v[:,-1]
    a=w@m@w; r=m@w-a*w
    if norm(r)<1e-13:
        z=np.eye(len(w))[:,np.argmin(abs(w))]
        r=z-(w@z)*w
    d=r/norm(r);p=np.eye(len(w))-np.outer(d,d)
    assert abs(w@d)<1e-12 and norm(p@m@w-a*w)<1e-10
    assert a>1
    D=np.eye(len(w))-(1-np.exp(-20))*np.outer(d,d)
    assert max(abs(eigvals(m@D)))>1
    z=w.copy()
    for k in range(8):
        assert abs(w@z-a**k)<5e-7
        z=m@p@z
    return a

G3=np.array([[-1.,12.,1.],[0.,-1.,8.],[0.,0.,-1.]])
G4=np.array([[-1.,4.,0.,0.],[0.,-1.,5.,0.],[0.,0.,-1.,3.],[0.,0.,0.,-1.]])
a3,a4=witness(G3,.12),witness(G4,.2)
assert abs(a3-1.8284805958103003)<1e-12
assert abs(a4-1.5028145397507875)<1e-12

G=np.array([[-.1,-np.pi/2,0.],[np.pi/2,-.1,0.],[0.,0.,-1.]])
m=expm(G)
spec=eigvals(m[:2,:2]);real_num=eigvalsh((m+m.T)/2)[-1]
assert abs(max(abs(spec))-np.exp(-.1))<1e-12
assert abs(real_num-np.exp(-1))<1e-12
assert max(abs(spec))>real_num

# NC ART029 T1a local counterexample: isometry without Gramian saturation.
e=np.array([1.,0.]);P=np.diag([1.,0.]);R=np.array([[0.,-1.],[1.,0.]])
W=np.outer(e,e)+np.outer(P@R.T@e,P@R.T@e)
assert abs(eigvalsh(W)[-1]-1)<1e-13  # below m=2

# Original NC Jordan separator: closed optimum of positive real Rayleigh.
opt=.98;rstar=50*np.exp(-opt)
assert abs(rstar-18.765554942569977)<1e-12

# LT5 target nonmap: growing largest eigenvalue, Gramian exactly rank ONE.
Ghid=np.array([[-1.,100.,0.],[0.,-1.,0.],[0.,0.,-2.]])
w=np.array([1.,1.,0.])/np.sqrt(2);d=np.array([1.,-1.,0.])/np.sqrt(2)
m=expm(Ghid*opt);p=np.eye(3)-np.outer(d,d)
a=w@m@w; L=np.eye(3); W=np.zeros((3,3))
for k in range(6):
    z=L.T@w;W+=np.outer(z,z)
    L=m@p@L
v=sum(a**(2*k) for k in range(6))
assert norm(W-v*np.outer(w,w))/v<1e-12
assert v>5e12 and abs(W[2,2])<1e-14

# Resource guard: fixed total T, arbitrary five contraction impulses.
rng=np.random.default_rng(20261024)
for trial in range(300):
    n=3+trial%2
    g=rng.normal(size=(n,n))*.6-np.eye(n)*(trial%3)/2
    e=rng.normal(size=n);e/=norm(e)
    d=rng.normal(size=n);d/=norm(d)
    T=1.4;ts=np.sort(rng.uniform(0,T,5));u=rng.uniform(0,1,5)
    L=expm(g*ts[0]); W=np.zeros((n,n))
    for j in range(5):
        z=(1-u[j])*(L.T@e);W+=np.outer(z,z)
        if j<4:
            D=np.eye(n)-(1-u[j])*np.outer(d,d)
            L=expm(g*(ts[j+1]-ts[j]))@D@L
    assert np.sqrt(eigvalsh(W)[-1])<=np.sqrt(5)*np.exp(max(mu2(g),0)*T)+1e-10
print('PASS NC029 n3/n4 witness; compression; NC T1a; LT5 hidden-target; 300 horizon controls')
