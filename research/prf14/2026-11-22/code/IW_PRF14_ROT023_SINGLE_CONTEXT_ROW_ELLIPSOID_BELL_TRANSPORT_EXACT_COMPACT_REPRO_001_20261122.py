#!/usr/bin/env python3
"""PRF14 ROT023 concise symbolic reproduction. Full executed source,
physical SO3/Bloch/POVM multinomial simulations and manifest are in
prf14_rot023_reproducibility_bundle.zip. Uses SymPy only.
"""
import itertools, math
import sympy as s
from scipy.optimize import brentq
f=s.Rational
V=list(itertools.product((0,1),repeat=2))
H=list(itertools.product(V,V))
R=s.Matrix([[-3,-2,6],[6,-3,2],[2,6,3]])/7
P=s.Matrix([[0,0,1],[1,0,0],[0,1,0]])
DX=s.diag(1,-1,-1)
C=s.Matrix([[0,f(9,100),f(11,100)],
            [f(7,100),0,f(1,10)],
            [f(8,100),f(12,100),0]])
chi=lambda i,v:((-1)**v[1],(-1)**(v[0]+v[1]),(-1)**v[0])[i]
D={v:s.diag(*(chi(i,v) for i in range(3))) for v in V}
def p(K):
    return {(v,w):s.factor((1+sum(K[i,j]*chi(j,v)*chi(i,w)
            for i in range(3) for j in range(3) if i!=j))/16) for v,w in H}
def TV(a,b):return s.factor(sum(abs(a[h]-b[h]) for h in H)/2)
def T(a,S):
    M=s.zeros(3)
    for (v,w),z in a.items():M+=z*D[w]*S*D[v]
    return M.applyfunc(s.factor)
assert all(A.T*A==s.eye(3) and A.det()==1 for A in (R,P,DX))
source_break=p(C);source_unit=p(f(8,5)*C)
assert min(source_break.values())==f(73,1600)
assert min(source_unit.values())==f(71,2000)
assert TV(source_break,source_unit)==f(513,8000)
S=P*R
cj=[C[0,j] for j in (1,2)]
aj=[s.factor(f(8,5)*C[0,j]*S[0,j]) for j in (1,2)]
assert cj==[f(9,100),f(11,100)]
assert aj==[f(108,875),f(66,875)]
assert sum((a/c)**2 for a,c in zip(aj,cj))==f(576,245)
assert T(source_unit,S)==DX*T(source_unit,DX*S)
root=brentq(lambda z:sum((float(a)/(float(c)+2*z))**2 for a,c in zip(aj,cj))-1,0,.2)
assert .02498<root<float(TV(source_break,source_unit))
# Distinct proper target gate with strictly positive alternative UNIT source,
# but EXACT same all 2*9 full UNIT channel entries and same BREAK Bell data.
t=f(1,1000)
U=s.Matrix([[1,0,0],[0,(1-t*t)/(1+t*t),-2*t/(1+t*t)],
            [0,2*t/(1+t*t),(1-t*t)/(1+t*t)]])
assert U.T*U==s.eye(3) and U.det()==1
Sp=P*U*R
Cp=s.Matrix(3,3,lambda i,j:s.factor(C[i,j]*S[i,j]/Sp[i,j]) if i!=j else 0)
hidden=p(Cp)
assert min(hidden.values())>0
assert TV(hidden,source_break)==f(5997,25099975)
assert T(hidden,Sp)==T(source_break,S)
assert T(hidden,DX*Sp)==T(source_break,DX*S)
# Separate n-shot allocation: two UNIT +/-1 means, one two-Bell 16-label
# sample from which two source Fourier characters are computed.
etau=.010;etab=.009;alpha=.025
nu=math.ceil(2*math.log(4/alpha)/etau**2)
nb=math.ceil(2*math.log(4/alpha)/etab**2)
assert (nu,nb,2*nu+nb)==(101504,125313,328321)
ea=etau+.00015;ec=etab+2*.001
alt_power=sum(((1.6*float(cj[j])*(float(S[0,j+1])-.001)-2*ea)
               /(float(cj[j])+2*ec))**2 for j in range(2))
assert alt_power>1
print('PASS physical sources, row SO3 contradiction 576/245, TV 513/8000')
print('PASS alternate 2x9 full channel invisible gate/source alias')
print('PASS 95pct 328321-runs finite-shot allocation, model-only')
print('Exact-data gate-free TV lower:',root)
print('NO_HARDWARE / NO_GENERAL_PROCESS_TENSOR / NO_EXTERNAL_NOVELTY')
