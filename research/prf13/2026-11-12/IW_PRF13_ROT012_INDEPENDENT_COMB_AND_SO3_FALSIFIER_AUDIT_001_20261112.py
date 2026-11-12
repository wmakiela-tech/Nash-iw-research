#!/usr/bin/env python3
"""Independent numerical audit of ROT012: 16x16 causal Choi comb and random SO(3).
Sampling is falsification only; the global minimax theorem is proved analytically.
"""
from itertools import product
import numpy as np
from numpy.linalg import eigvalsh

X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.diag([1,-1]).astype(complex)
I=np.eye(2,dtype=complex)
G=list(product((0,1),repeat=2))
U={v:np.linalg.matrix_power(X,v[0])@np.linalg.matrix_power(Z,v[1]) for v in G}
char={"X":lambda v: (-1)**v[1],"Y":lambda v:(-1)**(v[0]+v[1]),"Z":lambda v:(-1)**v[0]}
coeffs={("X","Y"):.1,("X","Z"):-1/12,("Y","X"):1/15,("Y","Z"):-.05,("Z","X"):1/30,("Z","Y"):-.025}
p={(v,w):(1+sum(c*char[a](v)*char[b](w) for (a,b),c in coeffs.items()))/16 for v in G for w in G}
assert min(p.values())>0 and abs(sum(p.values())-1)<1e-14

def J(M):
    z=M.reshape(4)
    return np.outer(z,z.conj())
W=sum((prob*np.kron(J(U[v]),J(U[w])) for (v,w),prob in p.items()),np.zeros((16,16),dtype=complex))
assert np.max(np.abs(W-W.conj().T))<1e-14
assert min(eigvalsh(W))>-1e-13
assert abs(np.trace(W)-4)<1e-13
T=np.trace(W.reshape((2,)*8),axis1=2,axis2=6).reshape(8,8)
Jdep=np.eye(4,dtype=complex)/2
assert np.max(np.abs(T-np.kron(Jdep,I)))<1e-13
assert np.max(np.abs(np.trace(Jdep.reshape(2,2,2,2),axis1=0,axis2=2)-I))<1e-13
print('PASS independent 16x16 mixed Pauli process comb PSD and causal trace identities')

# Explicit input/state evolution in 2x2 for all six active settings.
V=-1j*(X+Y+Z)/np.sqrt(3)
assert np.max(np.abs(V.conj().T@V-I))<1e-14
P={'X':X,'Y':Y,'Z':Z}
for (a,b),c in coeffs.items():
    rho=(I+P[a])/2
    evolved=sum((prob*U[w]@V@U[v]@rho@U[v].conj().T@V.conj().T@U[w].conj().T
                 for (v,w),prob in p.items()),np.zeros((2,2),dtype=complex))
    mean=np.trace(P[b]@evolved)
    assert abs(mean-2*c/3)<1e-13 and abs(mean.imag)<1e-13
print('PASS independent 2x2 six offdiagonal physical settings')

# Random quaternion samples only FALSIFY globally valid upper bound if > 2/3.
rng=np.random.default_rng(20261112)
q=rng.normal(size=(100000,4));q/=np.linalg.norm(q,axis=1)[:,None]
a,b,c,d=q.T
R=np.empty((len(q),3,3))
R[:,0,0]=1-2*(c*c+d*d);R[:,0,1]=2*(b*c-a*d);R[:,0,2]=2*(b*d+a*c)
R[:,1,0]=2*(b*c+a*d);R[:,1,1]=1-2*(b*b+d*d);R[:,1,2]=2*(c*d-a*b)
R[:,2,0]=2*(b*d-a*c);R[:,2,1]=2*(c*d+a*b);R[:,2,2]=1-2*(b*b+c*c)
off=np.abs(R[:,np.array([0,0,1,1,2,2]),np.array([1,2,0,2,0,1])])
best=float(np.max(np.min(off,axis=1)))
assert best<=2/3+1e-12
assert np.max(np.abs(R[:100]@np.swapaxes(R[:100],1,2)-np.eye(3)))<1e-13
print('PASS 100000 seeded SO3 attempted counterexamples; max min_offdiag =',best)
print('AUDIT_PASS numerical only; exact optimum proof uses cofactor contradiction')
