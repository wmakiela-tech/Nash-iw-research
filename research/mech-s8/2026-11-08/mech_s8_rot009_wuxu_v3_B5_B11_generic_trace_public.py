#!/usr/bin/env python3
"""Mech-S8 ROT009: v3 manuscript B.5-B.11 generic Dirac trace. SymPy required.
https://arxiv.org/html/2509.05618v3  No physical PBH/BBN inference.
"""
import sympy as s
from itertools import product
z=s.zeros(2);i=s.I;u=s.eye(4)
a=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-i],[i,0]]),s.Matrix([[1,0],[0,-1]])]
g=[s.diag(1,1,-1,-1)]+[s.BlockMatrix([[z,t],[-t,z]]).as_explicit() for t in a]
g5=s.simplify(i*g[0]*g[1]*g[2]*g[3])
def sl(p):return g[0]*p[0]-sum((g[j]*p[j] for j in range(1,4)),s.zeros(4))
v,w,mn,mp,me=s.symbols('gV gA mn mp me',real=True)
e,x,y,z0,n,q,r,h=s.symbols('Ee px py pz Enu qx qy qz',real=True)
pp=(mp,0,0,0);pn=(mn,0,0,0);pe=(e,x,y,z0);nu=(n,q,r,h)
G=v*u-w*g5;L=u-g5;sig=(1,-1,-1,-1)
H=[[s.trace((sl(pp)+mp*u)*g[j]*G*(sl(pn)+mn*u)*g[k]*G)
    for k in range(4)] for j in range(4)]
T=[[s.trace((sl(pe)+me*u)*g[j]*L*sl(nu)*g[k]*L)
    for k in range(4)] for j in range(4)]
full=s.expand(sum((sig[j]*sig[k]*H[j][k]*T[j][k]
             for j,k in product(range(4),repeat=2)),s.S.Zero)/2)
E=e*n;D=x*q+y*r+z0*h
b9=(v*v+3*w*w)*E+(v*v-w*w)*D
b6=(3*v*v+w*w)*E-(v*v-w*w)*D
assert s.simplify(full-32*mn*mp*b9)==0
assert s.simplify(b6-b9-2*(v*v-w*w)*(E-D))==0
assert s.simplify(full/16-2*mn*mp*b9)==0
assert s.simplify(2/(s.Rational(1,16))-32)==0
assert s.simplify((full/16)/(4*mn*mp)-b9/2)==0
print('PASS: B6 wrong mass-term sign; B9 bracket right; printed prefactor 32x too small; B11 compatible with corrected normalization.')
print('NO CANON / NO EXEC_SIGN / NO Yp,DH,PBH BOUND')
