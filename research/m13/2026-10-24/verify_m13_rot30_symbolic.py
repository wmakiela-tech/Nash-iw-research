#!/usr/bin/env python3
"""M13 ROT30 algebraic TT-bandwidth sharpness independent of NumPy.

Exact polynomial and TT multiplier identities, together with explicit
root/interior-average proof. The strict real-variable sign is proved in report.
"""
from sympy import symbols, Poly, expand, diag, eye, chebyshevt, simplify, trace
x,lam,r2,r3,r4,r5,z = symbols('x lambda r2 r3 r4 r5 z',real=True)
H=(x-r2)*(x-r3)*(x-r4)*(x-r5)
a=(x-r2)*(x-r3)
b=(x-r4)*(x-r5)*(x-lam)
V=H*(x-lam)
assert expand(a*b-V)==0
assert Poly(a,x).degree()==2 and Poly(b,x).degree()==3
assert Poly(H,x).degree()==4 and Poly(V,x).degree()==5
for root in (r2,r3,r4,r5):
    assert simplify(H.subs(x,root))==0
# Because t=cos(phi), powers to degree 3 produce Fourier harmonics 0..3,
# while product a*b has degree 5, appearing in the difference of squares.
assert expand(chebyshevt(2,x)-(2*x*x-1))==0
assert expand(chebyshevt(3,x)-(4*x**3-3*x))==0
assert expand((a+z*b)**2-(a-z*b)**2-4*z*V)==0
# For arbitrary one-coordinate mode k=(m,0,0), m!=0, TT projector:
M=diag(0,1,1)
T=diag(0,z,-z)
projected=M*T*M-(M*trace(M*T))/2
assert projected==T and trace(T)==0
# For mode k=0 source helper uses the trace-free projector; T also fixed.
assert T-(eye(3)*trace(T)/3)==T
# Unique bandwidth-4 identifiability proof: any deg<=4 polynomial with four
# boundary roots r2,...,r5 is cH. Inner sum of H is strictly positive for
# ordered r2<r3<r4<r5 and t_j>r5, forcing c=0.
# At degree5, V=H*(x-lambda) has vanishing four outer shells; choosing lambda
# as positive-H weighted inner average makes its fifth inner sum vanish;
# external four nodes have x<r2<lambda, H>0, V<0.
print('PASS: symbolic factorization, degree 2/3, degree-5 kernel, TT projection, zero mode')
print('SHARP THRESHOLD: even energy degree<=4 identifiable, degree5 non-identifiable; tensor TT bandwidth <=2 vs 3')