#!/usr/bin/env python3
"""PRF14 ROT016: four complete qubit channels indistinguishable for
stationary C,R and context-specific C'_q,R' (known P,L). SymPy only.
Source-restricted physical Pauli histories; no hardware or general comb claim.
"""
import itertools,math
import sympy as s
R=s.Matrix([[-3,-2,6],[6,-3,2],[2,6,3]])/7
P=s.Matrix([[0,0,1],[1,0,0],[0,1,0]])
L=s.Matrix([[0,1/s.sqrt(2),1/s.sqrt(2)],
            [1,0,0],[0,1/s.sqrt(2),-1/s.sqrt(2)]])
C=s.Matrix([[0,s.Rational(9,100),s.Rational(11,100)],
            [s.Rational(7,100),0,s.Rational(1,10)],
            [s.Rational(8,100),s.Rational(12,100),0]])
SIX=[(i,j) for i in range(3) for j in range(3) if i!=j]
G=list(itertools.product((0,1),repeat=2))
chi=lambda i,v:((-1)**v[1],(-1)**(v[0]+v[1]),(-1)**v[0])[i]
D={v:s.diag(*(chi(i,v) for i in range(3))) for v in G}
def law(K):return {(v,w):s.factor((1+sum(K[i,j]*chi(j,v)*chi(i,w)
                    for i,j in SIX))/16) for v in G for w in G}
def channel(K,M):
    T=s.zeros(3)
    for (v,w),p in law(K).items():T+=p*D[w]*M*D[v]
    return T.applyfunc(s.simplify)
def contexts(B):return (B,B*P,B*P**2,L*B)
assert all(Q.T*Q==s.eye(3) and Q.det()==1 for Q in (R,P,L))
assert P**3==s.eye(3)
t=s.Rational(1,1000)
x=(1-t*t)/(1+t*t);y=2*t/(1+t*t)
U=s.Matrix([[1,0,0],[0,x,-y],[0,y,x]])
assert U.T*U==s.eye(3) and U.det()==1
Rp=U*R;A=contexts(R);B=contexts(Rp)
kappa=min((abs(A[q][i,j]) for q in range(4) for i,j in SIX),
          key=lambda v:float(v))
assert kappa==s.Rational(2,7)
p0=law(C);alt=[]
for q in range(4):
    K=s.zeros(3)
    for i,j in SIX:K[i,j]=s.factor(C[i,j]*A[q][i,j]/B[q][i,j])
    pk=law(K)
    assert min(pk.values())>0 and sum(pk.values())==1
    assert channel(K,B[q])==channel(C,A[q])
    assert all(channel(K,B[q])[i,i]==0 for i in range(3))
    alt.append((K,pk))
assert len(set(tuple(str(K[i,j]) for i,j in SIX) for K,pk in alt))>1
# Nonconstant across contexts even for arbitrarily small angle t:
z=s.symbols('z',real=True)
V=s.Matrix([[1,0,0],[0,(1-z*z)/(1+z*z),-2*z/(1+z*z)],
            [0,2*z/(1+z*z),(1-z*z)/(1+z*z)]])
V0=contexts(V*R)
derivative=s.factor(s.diff(C[0,1]*A[3][0,1]/V0[3][0,1]-
                   C[0,1]*A[0][0,1]/V0[0][0,1],z).subs(z,0))
assert derivative==s.Rational(27,50)
# 13 original scalar probes leave 11 of 24 Fourier directions unseen.
initial=[(q,i,j) for i,j in [(0,1),(1,2),(2,1)] for q in range(3)]
initial += [(0,0,2),(0,1,0),(1,2,0),(3,0,1)]
assert len(initial)==13 and len(set(initial))==13
missing=[(q,i,j) for q in range(4) for i,j in SIX if (q,i,j) not in initial]
assert len(missing)==11
# Independently calibrated target rotation: 3 local SO3 entries are anchors.
O=(s.Matrix([[0,0,0],[0,0,-1],[0,1,0]]),
   s.Matrix([[0,0,1],[0,0,0],[-1,0,0]]),
   s.Matrix([[0,-1,0],[1,0,0],[0,0,0]]))
anchors=((1,2),(2,0),(2,2))
J=s.Matrix(3,3,lambda r,k:(O[k]*R)[anchors[r][0],anchors[r][1]])
assert J.det()==-s.Rational(36,49)
# Source TV bound with externally calibrated known R, all 24 experiments:
eta=.000018;xi=.0008
assert 12*eta/float(kappa)<xi
n=math.ceil(2*math.log(48/.05)/eta**2)
assert n==42388477065 and 24*n==1017323449560
print('PASS: exact 36/36 full Kraus Pauli channel entries for two physical worlds')
print('minimum known-R coefficient pivot',kappa)
print('initial 13/24 rank; 11 extra known-R source settings')
print('unknown-R smooth 3D fiber; derivative',derivative)
print('3 externally calibrated gate anchors local Jacobian determinant',J.det())
print('known-R conditional 95pct TV<=.0008 upper sufficient shots',24*n)
print('NO HARDWARE / NO GENERAL PROCESS TENSOR / NO EXTERNAL NOVELTY')
