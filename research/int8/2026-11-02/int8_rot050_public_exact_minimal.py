#!/usr/bin/env python3
"""INT8-050 minimal source-free exact rank-3 kernel and norm certificate."""
import sympy as S
s1,s2,u,v,w,e=S.symbols('s1 s2 u v w e',real=True)
a=S.Matrix([1,2,0]);b=S.Matrix([2,-1,0]);z=S.Matrix([0,0,1]);sa=S.Matrix([s1,s2,0]);sb=S.Matrix([s2,-s1,0]);U=S.Matrix([u,v,w])
def sym(p,q):return p*q.T+q*p.T
def TT(H,k):
 Q=S.eye(3)-k*k.T/(k.dot(k))
 return S.simplify(Q*H*Q-S.trace(Q*H)*Q/2)
Ta=TT(sym(U,sa),a);Tb=TT(sym(U,sb),b)
H=S.simplify(sym(Tb*z,sa)-sym(Ta*z,sb))
d=2*s1-s2;t=(s1+2*s2)/5;p=7*s1-s2;q=s1+7*s2
np_=S.Matrix([1,-3,0])/S.sqrt(10);nm=S.Matrix([3,1,0])/S.sqrt(10)
W=lambda n:n*n.T-z*z.T
V=lambda n:n*z.T+z*n.T
coef=-e*d*t*w/2
bp=e*d*S.sqrt(10)*(p*u-q*v)/100
bm=e*d*S.sqrt(10)*(q*u+p*v)/100
assert S.simplify(e*TT(H,a+b)/2-coef*W(np_)-bp*V(np_))==S.zeros(3)
assert S.simplify(e*TT(H,a-b)/2-coef*W(nm)-bm*V(nm))==S.zeros(3)
assert S.simplify(2*coef**2+bp**2+bm**2-e**2*d**2*(t**2*w**2/2+(s1**2+s2**2)*(u**2+v**2)/20))==0
M=S.Matrix([coef,bp,bm]).jacobian([u,v,w]);det=S.factor(M.det())
assert S.simplify(det+e**3*(s1+2*s2)*(2*s1-s2)**3*(s1**2+s2**2)/200)==0
print('EXACT_SOURCE_FREE_PASS kernel=(S_xz,S_yz,S_zz)=0, rank3; determinant:',det)
