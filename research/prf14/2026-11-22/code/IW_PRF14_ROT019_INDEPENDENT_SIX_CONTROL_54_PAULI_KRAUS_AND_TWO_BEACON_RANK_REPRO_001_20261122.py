#!/usr/bin/env python3
"""Independent 16-label Pauli-Kraus verification of ROT019 54 channel elements.
No import from owner main script; separately derive row mixing, physicality,
unknown-gate alias and two independent left-null Jacobian covectors.
"""
import itertools
import sympy as s
F=s.Rational
R=s.Matrix([[-3,-2,6],[6,-3,2],[2,6,3]])/7
P=s.Matrix([[0,0,1],[1,0,0],[0,1,0]])
L=s.Matrix([[0,1/s.sqrt(2),1/s.sqrt(2)],[1,0,0],[0,1/s.sqrt(2),-1/s.sqrt(2)]])
Q=s.Matrix([[-F(4,5),0,F(3,5)],[F(3,5),0,F(4,5)],[0,1,0]])
C=s.Matrix([[0,F(9,100),F(11,100)],[F(7,100),0,F(1,10)],[F(8,100),F(12,100),0]])
V=list(itertools.product([0,1],[0,1]));non_diag=[(i,j) for i in range(3) for j in range(3) if i!=j]
Sigma=lambda v:s.diag((-1)**v[1],(-1)**(v[0]+v[1]),(-1)**v[0])
sigma={v:Sigma(v) for v in V}
def prob(Z):
 return {(v,w):s.factor((s.Integer(1)+sum(Z[i,j]*sigma[v][j,j]*sigma[w][i,i] for i,j in non_diag))/16) for v,w in itertools.product(V,V)}
def KrausTransfer(Z,M):
 W=s.zeros(3)
 pp=prob(Z)
 assert min(pp.values())>0 and sum(pp.values())==1
 for (v,w),pr in pp.items():W+=pr*sigma[w]*M*sigma[v]
 return W.applyfunc(s.factor)
def controls(T):return [T,T*P,T*P*P,L*T,P*P*T,Q*T]
assert all(K.T*K==s.eye(3) and K.det()==1 for K in [R,P,L,Q])
A=controls(R)
rot=F(1,1000)
U=s.Matrix([[1,0,0],[0,(1-rot**2)/(1+rot**2),-2*rot/(1+rot**2)],[0,2*rot/(1+rot**2),(1-rot**2)/(1+rot**2)]])
assert U.T*U==s.eye(3) and U.det()==1
B=controls(U*R)
new=[]
for k in range(6):
 Z=s.zeros(3)
 for i,j in non_diag:Z[i,j]=s.factor(C[i,j]*A[k][i,j]/B[k][i,j])
 assert min(prob(Z).values())>0
 a=KrausTransfer(C,A[k]);b=KrausTransfer(Z,B[k])
 assert a==b
 assert a==s.Matrix(3,3,lambda i,j:s.factor(C[i,j]*A[k][i,j]) if i!=j else 0)
 assert all(a[i,i]==0 for i in range(3))
 new.append(Z)
 print('context',k,'FULL 9 CPTP transfer entries equal; minp alternative',min(prob(Z).values()))
assert any(new[k][1,2]!=new[0][1,2] for k in range(1,6))
# Analytic source drift pair with closure independence
null=[F(1,10)*x[1,2] for x in A]
assert null==[F(1,35),F(3,35),-F(3,70),F(3,35),F(3,70),F(3,35)]
def H(t):return s.factor(t[3]**2+t[4]**2-t[1]**2-t[2]**2)
def G(t):return s.factor(t[5]-F(3,5)*t[3]-F(4,5)*t[4])
assert H(null)==0 and G(null)==0
v=null.copy();v[5]*=2
assert H(v)==0 and G(v)==F(3,35)
v=null.copy();v[3]*=2;v[5]*=F(8,5)
assert H(v)==F(27,1225) and G(v)==0
# All 6 contexts generated from common single SO3 gate: 6x4 derivative has rank 4,
# two specified gradients give independent left annihilators.
rotgens=[s.Matrix([[0,0,0],[0,0,-1],[0,1,0]]),s.Matrix([[0,0,1],[0,0,0],[-1,0,0]]),s.Matrix([[0,-1,0],[1,0,0],[0,0,0]])]
JJ=s.Matrix(6,4,lambda q,k:A[q][1,2] if k==0 else F(1,10)*controls(rotgens[k-1]*R)[q][1,2])
assert JJ.rank()==4
jH=s.Matrix([[0,-2*null[1],-2*null[2],2*null[3],2*null[4],0]])
jG=s.Matrix([[0,0,0,-F(3,5),-F(4,5),1]])
assert jH*JJ==s.zeros(1,4) and jG*JJ==s.zeros(1,4) and s.Matrix.vstack(jH,jG).rank()==2
print('PASS 6x9=54 exact physically CPTP Bloch transfer entries; Jacobian rank4 and 2 independent closures')
print('NEW_CONTROL_Q_NEEDS_KNOWN_NON_CLIFFORD_GATE ; EXACT_SOURCE_NOT_HARDWARE')
