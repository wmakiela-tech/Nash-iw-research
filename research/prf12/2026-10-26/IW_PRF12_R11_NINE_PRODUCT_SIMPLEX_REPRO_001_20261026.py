#!/usr/bin/env python3
"""PRF12 R11: 9 rank-one product effects attain endpoint Helstrom in frozen ideal n=3 Cauchy/Lévy SWAP model. NumPy only; no LOCC inference."""
import numpy as np
from itertools import product
from math import pi,sqrt,exp
z=np.exp(2j*pi/9);w=z**3; I=np.eye(8,dtype=complex)
cyc=((0,1,2),(1,2,0),(2,0,1))
anti=((0,2,1),(1,0,2),(2,1,0))
rows=[(3*k,)*3 for k in range(3)]
rows += [tuple(1+3*j for j in p) for p in cyc]
rows += [tuple((5+3*j)%9 for j in p) for p in anti]
def vec(exponents):
 v=np.array([1.],complex)
 for i in exponents: v=np.kron(v,np.array([1.,z**i])/sqrt(2))
 return v
V=np.column_stack([vec(row) for row in rows])
G=V.conj().T@V
off=np.abs(G[np.triu_indices(9,k=1)])
assert np.max(abs(off-1/8))<3e-15
assert np.max(abs((8/9)*V@V.conj().T-I))<1e-13
val=np.linalg.eigvalsh(G)
assert abs(val[0])<1e-13 and np.max(abs(val[1:]-9/8))<1e-13
W=(I[1]+I[2]+I[4])/sqrt(3)
B=(I[3]+I[5]+I[6])/sqrt(3)
P=np.outer(W,W.conj())+np.outer(B,B.conj())
h=(I[0]+I[7])/sqrt(2)
E=(8/9)*V[:,:3]@V[:,:3].conj().T
assert np.max(abs(E-P-(2/3)*np.outer(h,h.conj())))<1e-13
bits=np.array(list(product((0,1),repeat=3)))
for q in (.05,1/3,.7,1.4,3):
 d=bits[:,None,:]-bits[None,:,:]
 D=(np.exp(-q*np.abs(d.sum(2)))-np.exp(-q*np.abs(d).sum(2)))/8
 hel=np.abs(np.linalg.eigvalsh(D)).sum()/2
 sep=np.trace(E@D).real
 expected=(1-exp(-2*q))/2
 assert abs(hel-expected)<1e-13 and abs(sep-expected)<1e-13
 print('q',q,'Helstrom',hel,'SEP9',sep)
print('Gram 36 pairs mod=1/8; tight-frame identity; Eplus spectral support: PASS')
print('MINIMALITY 9: proof uses rank >=8, 8 effects is orthonormal product basis, but at least 3 positive symmetric product vectors are needed and at most 2 can be mutually orthogonal.')
print('Scope: minimum NUMBER among rank-one product-effect exact POVMs only; no global LOCC gap.')
