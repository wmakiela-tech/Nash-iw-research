#!/usr/bin/env python3
"""PRF13 ROT010: exact Pauli-comb control and tester optimum. SymPy only."""
import sympy as s
from itertools import product
I=s.I;E=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-I],[I,0]]);Z=s.diag(1,-1)
H=(X+Z)/s.sqrt(2);S=s.diag(1,I);V=S*H
G=list(product((0,1),repeat=2));U={v:X**v[0]*Z**v[1] for v in G}
F=lambda v:(v[1],v[0]^v[1])
P={(v,w):(s.Rational(1,4) if w==F(v) else s.S.Zero) for v in G for w in G}
Q={(v,w):s.Rational(1,16) for v in G for w in G}
assert len(set(F(v) for v in G))==4
assert len(set((v[0]^F(v)[0],v[1]^F(v)[1]) for v in G))==4
assert s.simplify(V.H*V-E)==s.zeros(2)
for v in G:
    A=U[F(v)]*V*U[v];lam=s.simplify((V.H*A)[0,0])
    assert s.simplify(A-lam*V)==s.zeros(2)
    assert s.simplify(lam*s.conjugate(lam))==1
ket=s.Matrix([1,0]);rho=ket*ket.H
def out(p,C):
    return s.simplify(sum((pr*U[w]*C*U[v]*rho*U[v].H*C.H*U[w].H for (v,w),pr in p.items()),s.zeros(2)))
assert out(P,E)==out(Q,E)==E/2
assert out(P,V)==V*rho*V.H
assert out(Q,V)==E/2
M=(E+Y)/2
p1=s.simplify(s.trace(M*out(P,V)))
p0=s.simplify(s.trace(M*out(Q,V)))
assert p1==1 and p0==s.Rational(1,2)
assert abs(p1-p0)==s.Rational(1,2)
phi=s.Matrix([1,0,0,1])/s.sqrt(2)
B={v:s.kronecker_product(U[v],E)*phi for v in G}
for v in G:
    for w in G:assert s.simplify((B[v].H*B[w])[0]-int(v==w))==0
assert sum((b*b.H for b in B.values()),s.zeros(4))==s.eye(4)
tv=sum(abs(P[k]-Q[k]) for k in P)/2
assert tv==s.Rational(3,4)
assert (1+tv)/2==s.Rational(7,8)
print('PASS: all three uncontrolled channels equal, Clifford echo TV=1/2; Bell adaptive tester optimal TV=3/4; success=7/8')
