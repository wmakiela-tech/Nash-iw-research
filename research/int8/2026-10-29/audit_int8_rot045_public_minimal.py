#!/usr/bin/env python3
"""INT8 ROT045: independent exact SymPy Krylov cubic/counterexample gate."""
import sympy as s
from itertools import product
x,y,z,t,a,b,c=s.symbols('x y z t a b c')
u=s.Matrix([x,y,z]); E=s.diag(a,b,c)
K=s.factor(s.det(s.Matrix.hstack(u,E*u,E*E*u)))
V=(a-b)*(a-c)*(b-c)*x*y*z
assert s.simplify(K*K-V*V)==0
A={
 'mix':[[1,1,0],[0,1,1],[0,0,1]],
 'strong':[[1,2,0],[0,1,1],[0,0,1]],
 'extra':[[1,1,2],[0,1,1],[0,0,1]],
 'rational_control':[[1,0,-1],[0,1,2],[0,0,1]]}
counts={}
for name,matrix in A.items():
 D=s.Matrix(matrix)*s.Matrix(matrix).T
 p=s.Poly(D.charpoly(t).as_expr(),t)
 irr=p.is_irreducible
 assert irr==((D-s.eye(3)).det()!=0)
 f=s.Poly(s.det(s.Matrix.hstack(u,D*u,D*D*u)),x,y,z)
 terms=[(mon,int(co)) for mon,co in f.terms()]
 zero=0;tested=0
 for q in product(range(-7,8),repeat=3):
  if q==(0,0,0) or next((j for j in q if j),1)<0:continue
  d=sum(co*q[0]**mon[0]*q[1]**mon[1]*q[2]**mon[2] for mon,co in terms)
  if d==0:zero+=1
  if irr: assert d!=0
  tested+=1
 if not irr:assert zero>0
 counts[name]=(tested,zero,str(p.discriminant()))
assert counts['mix'][2]=='49'
print('EXACT_KRYLOV_PASS',counts)
