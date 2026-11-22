#!/usr/bin/env python3
"""PRF14 ROT022 compact SymPy source: two Bell projectors fully reveal a fixed
joint classical Pauli label p(v,w) in THAT breaker protocol, but fail to
transport to a separate unitary protocol without a contextual source premise.
No actual quantum device; full executed originals in local ROT022 ZIP.
"""
import itertools, math
import sympy as s
f=s.Rational
V=list(itertools.product((0,1),repeat=2))
H=list(itertools.product(V,V))
ket0=s.Matrix([1,0]);ket1=s.Matrix([0,1]);I=s.eye(2)
X=s.Matrix([[0,1],[1,0]]); Z=s.diag(1,-1)
bell0=(s.kronecker_product(ket0,ket0)+s.kronecker_product(ket1,ket1))/s.sqrt(2)
b=[s.kronecker_product(X**x*Z**z,I)*bell0 for x,z in V]
Gram=s.Matrix(4,4,lambda a,c:(b[a].T.conjugate()*b[c])[0])
assert Gram==s.eye(4)
assert s.kronecker_product(Gram,Gram)==s.eye(16)
chi=lambda i,v:((-1)**v[1],(-1)**(v[0]+v[1]),(-1)**v[0])[i]
S={v:s.diag(*(chi(i,v) for i in range(3))) for v in V}
R=s.Matrix([[-3,-2,6],[6,-3,2],[2,6,3]])/7
L=s.Matrix([[0,1/s.sqrt(2),1/s.sqrt(2)],[1,0,0],[0,1/s.sqrt(2),-1/s.sqrt(2)]])
C=s.Matrix([[0,f(9,100),f(11,100)],[f(7,100),0,f(1,10)],[f(8,100),f(12,100),0]])
off=[(i,j) for i in range(3) for j in range(3) if i!=j]
def law(B):
 return {(v,w):s.factor((1+sum(B[i,j]*chi(j,v)*chi(i,w) for i,j in off))/16) for v,w in H}
def channel(p,U):
 A=s.zeros(3)
 for (v,w),pr in p.items():A+=pr*S[w]*U*S[v]
 return A.applyfunc(s.factor)
def tv(a,b):return sum(abs(a[z]-b[z]) for z in H)/2
unif={z:f(1,16) for z in H}
plus={(v,w):f(1,16)*(1+f(99,100)*chi(0,v)) for v,w in H}
minus={(v,w):f(1,16)*(1-f(99,100)*chi(0,v)) for v,w in H}
assert min(plus.values())==min(minus.values())==f(1,1600)
assert tv(plus,minus)==f(99,100)
assert channel(plus,R)==channel(minus,L*R)==s.zeros(3)
# Two worlds have identical UNIT terminal channels and BREAK Bell labels
# (both BREAK laws uniform); nevertheless unit source pair TV is 0 versus .99.
assert channel(unif,R)==channel(unif,L*R)==s.zeros(3)
# Stronger original PRF13 SIX-only source: 10 ordinary Fourier chars remain zero.
p0=law(C)
t=f(1,1000)
U=s.Matrix([[1,0,0],[0,(1-t*t)/(1+t*t),-2*t/(1+t*t)],
            [0,2*t/(1+t*t),(1-t*t)/(1+t*t)]])
assert U.T*U==s.eye(3) and U.det()==1
newlaws=[]
for Q0,Q1 in [(R,U*R),(L*R,L*U*R)]:
 J=s.zeros(3)
 for i,j in off:J[i,j]=s.factor(C[i,j]*Q0[i,j]/Q1[i,j])
 pj=law(J)
 assert sum(pj.values())==1 and min(pj.values())>0
 assert channel(pj,Q1)==channel(p0,Q0)
 for i in range(3):
  assert sum(p*chi(i,v) for (v,w),p in pj.items())==0
  assert sum(p*chi(i,w) for (v,w),p in pj.items())==0
  assert sum(p*chi(i,v)*chi(i,w) for (v,w),p in pj.items())==0
 newlaws.append(pj)
assert tv(newlaws[0],newlaws[1])>0
# 16-category distribution-free joint Hoeffding; no Gaussian asymptotics.
r=.022
n=math.ceil(2*math.log(2*(2**16-2)/.05)/r**2)
assert n==61072 and 2*(2**16-2)*math.exp(-n*r*r/2)<.05
# Two-data-stream 95% tester-transport falsifier resources.
eta=.0075; rr=.011
nu=math.ceil(2*math.log(4/.025)/eta**2)
nb=math.ceil(2*math.log(2*(2**16-2)/.025)/rr**2)
assert (nu,nb,2*(nu+nb))==(180451,255742,872386)
margin=(.1*(6/7-.001)-2*(2*eta+.0005))/2-(2*rr+4*.001)
assert margin>.0013
print('PASS exact 4x4 and 16x16 Bell error-label measurement maps')
print('PASS two-world arbitrary Pauli unitary source TV .99 unidentifiable')
print('PASS six-only source alternate exact full terminal channels and nonzero TV')
print('PASS 95% paired breaker 122144 trials; 95% hybrid 872386 runs')
print('NO UNRESTRICTED PROCESS TENSOR / NO HARDWARE / NO EXTERNAL NOVELTY')
