#!/usr/bin/env python3
"""PRF14 ROT024: exact standalone four-character SO3 falsifier.
Restricted six-only Pauli law: all 10 ordinary Fourier coords fixed zero.
No hardware, no general process-tensor claim, no external novelty claim.
"""
import itertools,math
import sympy as s
F=s.Rational
R=s.Matrix([[-3,-2,6],[6,-3,2],[2,6,3]])/7
P=s.Matrix([[0,0,1],[1,0,0],[0,1,0]])
S=P*R;DX=s.diag(1,-1,-1)
C=s.Matrix([[0,F(9,100),F(11,100)],[F(7,100),0,F(1,10)],[F(8,100),F(12,100),0]])
V=list(itertools.product((0,1),repeat=2))
H=list(itertools.product(V,V))
chi=lambda i,v:((-1)**v[1],(-1)**(v[0]+v[1]),(-1)**v[0])[i]
D={v:s.diag(*(chi(i,v) for i in range(3))) for v in V}
OFF=[(i,j) for i in range(3) for j in range(3) if i!=j]
def law(M):
 return {(v,w):s.factor((1+sum(M[i,j]*chi(j,v)*chi(i,w) for i,j in OFF))/16) for v,w in H}
def channel(prob,U):
 T=s.zeros(3)
 for (v,w),a in prob.items():T+=a*D[w]*U*D[v]
 return T.applyfunc(s.factor)
def tv(a,b):return s.factor(sum(abs(a[z]-b[z]) for z in H)/2)
assert S.T*S==s.eye(3) and S.det()==1
pbreak=law(F(7,2)*C);punit=law(F(91,25)*C)
assert sum(pbreak.values())==sum(punit.values())==1
assert min(pbreak.values())==F(11,3200)
assert min(punit.values())==F(43,40000)
assert tv(pbreak,punit)==F(1197,80000)
U=F(26,25)*S
assert all(sum(U[i,j]**2 for j in range(3) if i!=j)==F(6084,6125) for i in range(3))
assert all(sum(U[i,j]**2 for i in range(3) if i!=j)==F(6084,6125) for j in range(3))
x01,x02,x10,x12=U[0,1],U[0,2],U[1,0],U[1,2]
gap=s.factor(abs(x02*x12)-abs(x10)*s.sqrt(1-x01*x01-x02*x02)-abs(x01)*s.sqrt(1-x10*x10-x12*x12))
assert s.simplify(gap-(F(12168,30625)-F(234,30625)*s.sqrt(205)))==0 and gap>0
k=s.symbols('k')
a,b,c,d=6*k/7,3*k/7,-3*k/7,6*k/7
Aa=c*c*(1-a*a-b*b);Bb=a*a*(1-c*c-d*d);W=b*d
quartic=s.factor((W*W-Aa-Bb)**2-4*Aa*Bb)
assert s.simplify(quartic-F(729,117649)*k**4*(k*k-1)*(81*k*k-49))==0
assert quartic.subs(k,F(26,25))>0
assert channel(pbreak,S)==DX*channel(pbreak,DX*S)
assert channel(punit,S)==DX*channel(punit,DX*S)
# Six-only positive physical unknown-gate alternative identical full 2x9
# channel entries and identical breaker source labels but different transport TV.
t=F(1,1000)
X=s.Matrix([[1,0,0],[0,(1-t*t)/(1+t*t),-2*t/(1+t*t)],[0,2*t/(1+t*t),(1-t*t)/(1+t*t)]])
Sp=P*X*R
M=s.Matrix(3,3,lambda i,j:s.factor(F(7,2)*C[i,j]*S[i,j]/Sp[i,j]) if i!=j else 0)
pother=law(M)
assert min(pother.values())>0
assert channel(pother,Sp)==channel(pbreak,S)
assert channel(pother,DX*Sp)==channel(pbreak,DX*S)
assert tv(pother,pbreak)==F(41979,50199950)>0
nu=math.ceil(2*math.log(8/.025)/.0013**2)
nb=math.ceil(2*math.log(8/.025)/.001**2)
assert (nu,nb,4*nu+nb)==(6826416,11536642,38842306)
print('PASS physical 16 Pauli laws; all six norms pass; strict two-row SO3 violation',gap)
print('PASS exact quartic; exact 18/18 CPTP channel gauge; source TV witness',tv(pother,pbreak))
print('95 percent sufficient 4*n_u+n_Bell=',4*nu+nb,'model only; no hardware')
