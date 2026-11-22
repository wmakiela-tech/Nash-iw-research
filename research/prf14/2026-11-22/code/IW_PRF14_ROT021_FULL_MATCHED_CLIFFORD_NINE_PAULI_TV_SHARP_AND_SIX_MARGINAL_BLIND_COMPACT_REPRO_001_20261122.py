#!/usr/bin/env python3
"""PRF14 ROT021 exact compact SymPy reproducer.
Two physically distinct post-target Cliffords, matched FULL three-output Pauli
frame, source-TV Frobenius sharp witness and arbitrary-source blindness.
Full native executed scientific and binomial code supplied in ROT021 ZIP.
"""
import itertools
import sympy as s
F=s.Rational
R=s.Matrix([[-3,-2,6],[6,-3,2],[2,6,3]])/7
P=s.Matrix([[0,0,1],[1,0,0],[0,1,0]])
D=s.diag(1,-1,-1);B=D*P
C=s.Matrix([[0,F(9,100),F(11,100)],
            [F(7,100),0,F(1,10)],
            [F(8,100),F(12,100),0]])
vset=list(itertools.product((0,1),repeat=2))
h=list(itertools.product(vset,vset))
sig=lambda v:s.diag((-1)**v[1],(-1)**(v[0]+v[1]),(-1)**v[0])
def source(U):
 return {(v,w):s.factor((1+sum(U[i,j]*sig(v)[j,j]*sig(w)[i,i]
         for i in range(3) for j in range(3) if i!=j))/16) for v,w in h}
def TV(a,b):return s.factor(sum(abs(a[k]-b[k]) for k in h)/2)
def Ch(p,M):
 T=s.zeros(3)
 for (v,w),z in p.items():T+=z*sig(w)*M*sig(v)
 return T.applyfunc(s.factor)
assert all(X.T*X==s.eye(3) and X.det()==1 for X in (R,P,D,B))
assert D**2==s.eye(3) and B==D*P and B!=P
p=source(C);assert min(p.values())==F(73,1600)
assert Ch(p,P*R)==D*Ch(p,B*R)
Z=C.copy();Z[0,1]+=F(1,10)
pz=source(Z)
E=(D*Ch(pz,B*R)-Ch(p,P*R)).applyfunc(s.factor)
assert TV(p,pz)==F(1,20)
assert E==s.Matrix([[0,F(3,35),0],[0,0,0],[0,0,0]])
# Exact SO3 Frobenius diameter sharpness via two full-support sources.
u=F(1,100)
p0={k:(1-u if k==(vset[0],vset[0]) else 0)+u/16 for k in h}
p1={k:(1-u if k==(vset[0],(1,0)) else 0)+u/16 for k in h}
assert TV(p0,p1)==1-u and min(p0.values())==u/16
W=D*Ch(p1,B*R)-Ch(p0,P*R)
assert s.factor(sum(W[i,j]**2 for i in range(3) for j in range(3)))==8*(1-u)**2
# Opposite first-error marginal ±0.99, second error completely random:
pm={(v,w):(1+F(99,100)*sig(v)[0,0])/16 for v,w in h}
pn={(v,w):(1-F(99,100)*sig(v)[0,0])/16 for v,w in h}
assert TV(pm,pn)==F(99,100)
assert Ch(pm,P*R)==Ch(pn,P*R)==s.zeros(3)
# Full normalized Fourier map to 9 cross coefficients has six-dimensional null.
M=s.Matrix([[1]*16]+[[sig(v)[j,j]*sig(w)[i,i] for v,w in h]
                     for i in range(3) for j in range(3)])
assert M.shape==(10,16) and M.rank()==10
# Independently enumerate original INT10 (different-cell FIRSTNESS!) 64
# sign vertices of six-character inverse Fourier source TV norm 9/8.
six=[(i,j) for i in range(3) for j in range(3) if i!=j]
w=[[sig(v)[j,j]*sig(z)[i,i] for i,j in six] for v,z in h]
vals=[sum(abs(sum(row[k]*bits[k] for k in range(6))) for row in w)
      for bits in itertools.product((-1,1),repeat=6)]
assert vals.count(36)==32 and vals.count(24)==32
print('PASS SO3 Clifford physicality, 9/9 full-frame match')
print('PASS sharp Frobenius 2 sqrt(2) TV bound, full source support')
print('PASS full 16-way source blindness TV=0.99, Fourier 6D kernel')
print('PASS INT10-first 9/8 six-coordinate inverse norm, independent replay')
print('NO HARDWARE; NO GENERAL PROCESS TENSOR; NO EXTERNAL NOVELTY')
