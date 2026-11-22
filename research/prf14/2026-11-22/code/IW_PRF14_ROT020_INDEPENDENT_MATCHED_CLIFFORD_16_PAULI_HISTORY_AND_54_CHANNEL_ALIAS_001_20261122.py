#!/usr/bin/env python3
"""Independent direct Pauli-history test of ROT020 matched Clifford readout and
full six-context physical alias. No imports from main owner implementation.
"""
import itertools
import sympy as sp
R=sp.Matrix([[-3,-2,6],[6,-3,2],[2,6,3]])/7
P=sp.Matrix([[0,0,1],[1,0,0],[0,1,0]])
L=sp.Matrix([[0,1/sp.sqrt(2),1/sp.sqrt(2)],[1,0,0],[0,1/sp.sqrt(2),-1/sp.sqrt(2)]])
B=sp.Matrix([[0,1,0],[1,0,0],[0,0,-1]])
F=sp.Rational
C=sp.Matrix([[0,F(9,100),F(11,100)],[F(7,100),0,F(1,10)],[F(8,100),F(12,100),0]])
vs=list(itertools.product((0,1),repeat=2))
sgn={v:sp.diag((-1)**v[1],(-1)**(v[0]+v[1]),(-1)**v[0]) for v in vs}
OFF=[(i,j) for i in range(3) for j in range(3) if i!=j]
def pp(K):
 vals={}
 for v,w in itertools.product(vs,vs):
  coeff=sp.Integer(1)
  for i,j in OFF: coeff+=K[i,j]*sgn[v][j,j]*sgn[w][i,i]
  vals[(v,w)]=sp.factor(coeff/16)
 return vals
def physical_transfer(K,S):
 p=pp(K)
 assert sum(p.values())==1 and min(p.values())>0
 T=sp.zeros(3)
 for (v,w),pr in p.items():T+=pr*sgn[w]*S*sgn[v]
 return T.applyfunc(sp.factor)
source_bigger=C.copy();source_bigger[1,2]=F(1,5)
assert pp(source_bigger)!=pp(C)
assert sum(abs(pp(source_bigger)[k]-pp(C)[k]) for k in pp(C))/2==F(1,20)
assert all(K.T*K==sp.eye(3) and K.det()==1 for K in (R,P,L,B))
assert P!=B and P!=L and B!=L
# distinct physical channels under stationary source, same tested observable Y-from-Z:
channels=[physical_transfer(C,K*R) for K in (L,P,B)]
assert all(T[1,2]==F(3,35) for T in channels)
assert all(T!=channels[0] for T in channels[1:])
for i in range(3):
 for j in range(3):
  assert (physical_transfer(C,P*R)[i,j]-physical_transfer(C,B*R)[i,j])==(channels[1][i,j]-channels[2][i,j])
assert physical_transfer(source_bigger,P*R)[1,2]==F(6,35)
# Proper alternative target R' with all six independently adjusted context-dependent sources.
t=F(1,1000)
X=sp.Matrix([[1,0,0],[0,(1-t*t)/(1+t*t),-2*t/(1+t*t)],[0,2*t/(1+t*t),(1-t*t)/(1+t*t)]])
assert X.det()==1 and X.T*X==sp.eye(3) and X!=sp.eye(3)
cs=lambda U:(U,U*P,U*P**2,L*U,P**2*U,P*U)
a=cs(R);b=cs(X*R)
changes=[]
for k in range(6):
 alt=sp.zeros(3)
 for i,j in OFF:
  assert b[k][i,j]!=0
  alt[i,j]=sp.factor(C[i,j]*a[k][i,j]/b[k][i,j])
 A=physical_transfer(C,a[k]);B2=physical_transfer(alt,b[k]);
 assert A==B2
 assert all(A[i,i]==0 for i in range(3))
 changes.append(alt)
 print('context',k,'9/9 COMPLETE Pauli Kraus channel elements equal, min source p',min(pp(alt).values()))
assert len(set(sp.factor(z[1,2]) for z in changes))>1
print('PASS: distinct physical controls with SAME targeted Pauli expectation; full 54/54 opposite physical sources/gates indistinguishable')
print('NO REAL QUANTUM HARDWARE / NO GENERAL QUANTUM COMB')
