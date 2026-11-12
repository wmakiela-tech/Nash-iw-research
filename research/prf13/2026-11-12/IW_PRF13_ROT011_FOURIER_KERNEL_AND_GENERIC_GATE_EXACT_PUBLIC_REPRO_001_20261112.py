#!/usr/bin/env python3
"""ROT011 exact six-dimensional Pauli-comb ordinary-channel fiber and one-gate recovery."""
import sympy as s
from itertools import product
I=s.I;E=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-I],[I,0]]);Z=s.diag(1,-1)
P=[X,Y,Z];G=list(product((0,1),repeat=2));pairs=list(product(G,G))
U={v:X**v[0]*Z**v[1] for v in G}
ch={'0':lambda v:1,'X':lambda v:(-1)**v[1],'Y':lambda v:(-1)**(v[0]+v[1]),'Z':lambda v:(-1)**v[0]}
nonzero=['X','Y','Z']
cons=[]
for v in G:cons.append([int(u==v) for (u,w) in pairs])
for w in G:cons.append([int(z==w) for (u,z) in pairs])
for d in G:cons.append([int((u[0]^w[0],u[1]^w[1])==d) for (u,w) in pairs])
A=s.Matrix(cons)
assert A.shape==(12,16) and A.rank()==10 and 16-A.rank()==6
V=(E-I*(X+Y+2*Z))/s.sqrt(7)
assert s.simplify(V.H*V-E)==s.zeros(2)
R=s.Matrix(3,3,lambda i,j:s.simplify(s.trace(P[i]*V*P[j]*V.H)/2))
assert R==s.Matrix([[-3,-2,6],[6,-3,2],[2,6,3]])/7
assert all(R[i,j]!=0 for i in range(3) for j in range(3) if i!=j)
assert R*R.T==s.eye(3)
basis=[]
for a in nonzero:
 for b in nonzero:
  if a==b:continue
  dp=s.Matrix([s.Rational(ch[a](v)*ch[b](w),16) for v,w in pairs])
  assert A*dp==s.zeros(12,1)
  basis.append(dp)
  p={z:s.Rational(1,16)+dp[k] for k,z in enumerate(pairs)}
  assert all(pr>=0 for pr in p.values()) and sum(p.values())==1
  i=nonzero.index(b);j=nonzero.index(a)
  for ii,O in enumerate(P):
   for jj,Q in enumerate(P):
    T=s.simplify(sum((pr*s.trace(O*U[w]*V*U[v]*Q*U[v].H*V.H*U[w].H)/2
                      for (v,w),pr in p.items())))
    assert T==(R[i,j] if (ii,jj)==(i,j) else 0)
assert s.Matrix.hstack(*basis).rank()==6
g2=list(product((0,1),repeat=2))
L=[]
for v in (0,1):L.append([int(a==v) for a,b in g2])
for w in (0,1):L.append([int(b==w) for a,b in g2])
for t in (0,1):L.append([int((a^b)==t) for a,b in g2])
assert s.Matrix(L).rank()==4
print('PASS: marginal/idle rank 10, hidden six basis states, generic rotation, 6 Pauli testers, size-2 no-go')
