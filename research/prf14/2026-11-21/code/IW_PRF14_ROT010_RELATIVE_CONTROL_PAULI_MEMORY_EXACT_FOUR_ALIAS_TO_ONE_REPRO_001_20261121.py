#!/usr/bin/env python3
"""PRF14 ROT010: source-restricted exact legal Pauli comb, 4->1 control gauge.
Requires SymPy. This does NOT validate SPAM or physical two-time hardware.
"""
import itertools, math
import sympy as S

R=S.Matrix([[-3,-2,6],[6,-3,2],[2,6,3]])/7
WR=S.Matrix([[-1,2,2],[2,-1,2],[2,2,-1]])/3
r=S.sqrt(2)
WL=S.Matrix([[0,1/r,1/r],[1,0,0],[0,1/r,-1/r]])
SIGNS=((1,1,1),(-1,-1,1),(-1,1,-1),(1,-1,-1))
c=S.Rational(1,10)
chi=lambda i,v:((-1)**v[1],(-1)**(v[0]+v[1]),(-1)**v[0])[i]
states=list(itertools.product(range(2),repeat=2))
def corr(d):
    return S.Matrix(3,3,lambda i,j:S.Integer(0) if i==j else c*d[i])
def probs(d):
    C=corr(d)
    return [S.factor((1+sum(C[i,j]*chi(j,v)*chi(i,w) for i in range(3)
          for j in range(3) if i!=j))/16) for v in states for w in states]
def read(M,d):
    return S.matrix_multiply_elementwise(M,corr(d))
def same(A,B):
    return all(S.simplify(A[i,j]-B[i,j])==0 for i in range(3)
               for j in range(3) if i!=j)
for M in (R,WR,WL):
    assert S.simplify(M.T*M)==S.eye(3) and S.simplify(M.det())==1
T0=read(R,SIGNS[0]); T1=read(R*WR,SIGNS[0]); T2=read(WL*R,SIGNS[0])
recover=[]
for i in range(3):
    js=[j for j in range(3) if j!=i]
    q={j:S.factor(T1[i,j]/T0[i,j]) for j in js}
    A=S.Matrix([[WR[k,j]-(q[j] if k==j else 0) for k in range(3)] for j in js])
    assert A.rank()==2 and len(A.nullspace())==1
    v=A.nullspace()[0]
    v=S.simplify(v/S.sqrt((v.T*v)[0]))
    assert all(S.simplify(v[j]-R[i,j])==0 for j in range(3))
    recover.append(q)
means=[]
for sign in SIGNS:
    D=S.diag(*sign)
    assert (D*R).det()==1
    P=probs(sign)
    assert sum(P)==1 and min(P)==S.Rational(1,20)
    # All ordinary channels / their Pauli Fourier diagonal equal zero.
    for i in range(3):
        assert sum(P[k]*chi(i,v) for k,(v,w) in
                   enumerate(itertools.product(states,states)))==0
        assert sum(P[k]*chi(i,w) for k,(v,w) in
                   enumerate(itertools.product(states,states)))==0
        assert sum(P[k]*chi(i,v)*chi(i,w) for k,(v,w) in
                   enumerate(itertools.product(states,states)))==0
    assert same(read(D*R,sign),T0)
    assert same(read(D*R*WR,sign),T1)
    means.append(S.simplify(read(WL*D*R,sign)[0,1]))
assert len(set(means))==4
gap=min(S.simplify(abs(a-b)) for i,a in enumerate(means)
        for b in means[i+1:])
assert S.simplify(gap-3/(35*S.sqrt(2)))==0
# Global maximin over left-control SO3 for the fixed Pauli X<-Y probe:
# Four candidates have c*(A+-B+-C), B=-3*w_y/7,C=6*w_z/7.
# Max nearest-neighbor gap attained at w_x=0,w_y=w_z=1/sqrt(2).
other_branch=S.simplify(2*c*6/(7*S.sqrt(17)))
assert gap>other_branch
conditional_shots=math.ceil((8/float(gap**2))*math.log(40))
assert conditional_shots==8034
print("PASS: exact legal SO3, 16 positive p each, 2-gate 4-alias / 3-gate unique")
print("right-control ratios",recover)
print("third single Pauli X<-Y four exact means",means)
print("single-probe globally optimal gap",gap,"=",float(gap))
print("95% stage-3-only Hoeffding shots IF stage-1/2 means exact:",conditional_shots)
