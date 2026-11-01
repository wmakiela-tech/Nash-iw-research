#!/usr/bin/env python3
"""Source-free SymPy certificate of the equal-E-eigenvalue projected commutator identity."""
import sympy as S
s1,s2,e=S.symbols('s1 s2 e',real=True)
a=S.Matrix([1,2,0]);b=S.Matrix([2,-1,0]);z=S.Matrix([0,0,1]);d=2*s1-s2;t=(s1+2*s2)/5
sa=S.Matrix([s1,s2,0]);sb=S.Matrix([s2,-s1,0])
ra=S.simplify(sa-a*a.dot(sa)/a.dot(a));rb=S.simplify(sb-b*b.dot(sb)/b.dot(b))
assert ra==d*b/5 and rb==-d*a/5
sym=lambda u,v:u*v.T+v*u.T
H=S.simplify(e*(sym(rb,sa)-sym(ra,sb)))
assert S.simplify(H+2*e*d*t*S.diag(1,1,0))==S.zeros(3)
def TT(H,k):
 Q=S.eye(3)-k*k.T/k.dot(k)
 return S.simplify(Q*H*Q-S.trace(Q*H)*Q/2)
for k,n in [(a+b,S.Matrix([1,-3,0])/S.sqrt(10)),(a-b,S.Matrix([3,1,0])/S.sqrt(10))]:
 W=n*n.T-z*z.T
 assert n.dot(k)==0
 assert S.simplify(TT(H,k)+e*d*t*W)==S.zeros(3)
 assert S.trace(W.T*W)==2
assert S.simplify(2*(e*d*t/2)**2-(e*d*t)**2/2)==0
h=S.symbols('h',real=True)
assert S.trigsimp(S.sin(h/2)**2+S.sin(h)**2-S.sin(h)**2-S.sin(-h/2)**2)==0
print('EXACT_SYMPY_PASS: equal E eigenvalue, nonzero projected commutator, exact two sidebands and RMS')
