#!/usr/bin/env python3
"""Public minimal source-free INT8-044 exact SymPy certificate; standalone."""
import sympy as S
from itertools import product

a,b,c,z=S.symbols('a b c z', positive=True, real=True)
W=(a/c+c/a)/2
p=(a+b*z)/(1+z); pi=(1/a+z/b)/(1+z)
q=(c+b*z)/(1+z); qi=(1/c+z/b)/(1+z)
Fplus=((p*p+c*c)*(pi*pi+c**-2))/4
Fminus=((a*a+q*q)*(a**-2+qi*qi))/4
hplus=S.factor(-S.diff(Fplus,z).subs(z,0)/(2*W))
hminus=S.factor(-S.diff(Fminus,z).subs(z,0)/(2*W))
assert S.simplify(hplus-(a-b)*(a*b-c*c)/(2*a*b*c))==0
assert S.simplify(hminus-(a*a-b*c)*(b-c)/(2*a*b*c))==0
print('EXACT HESSIAN PASS',hplus,hminus)

A=S.Matrix([[1,1,0],[0,1,1],[0,0,1]])
D=A*A.T
assert D.det()==1 and (D-S.eye(3)).det()==-1
n=0
for k in product(range(-7,8),repeat=3):
 if k==(0,0,0) or next((v for v in k if v!=0),1)<0:continue
 x=S.Matrix(k); y=x.cross(D*x)
 assert y!=S.zeros(3,1) and y.dot(y)>=1
 n+=1
print('EXACT INTEGER CROSS PASS',n,'half-grid nonzero directions at N=15')
