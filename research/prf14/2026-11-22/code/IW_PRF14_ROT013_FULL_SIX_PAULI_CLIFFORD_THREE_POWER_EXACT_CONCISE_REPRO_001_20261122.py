#!/usr/bin/env python3
"""PRF14 ROT013 public concise exact source and finite-N reproducibility.
All six offdiagonal Fourier coefficients independent, not row-flat.
SymPy required; concise source is separately published from the full
actually-executed local 1000-trial NumPy/SymPy original program.
"""
import itertools, math
import sympy as S

R=S.Matrix([[-3,-2,6],[6,-3,2],[2,6,3]])/7
P=S.Matrix([[0,0,1],[1,0,0],[0,1,0]])
L=S.Matrix([[0,1/S.sqrt(2),1/S.sqrt(2)],
            [1,0,0],[0,1/S.sqrt(2),-1/S.sqrt(2)]])
C=S.Matrix([[0,S.Rational(9,100),S.Rational(11,100)],
            [S.Rational(7,100),0,S.Rational(10,100)],
            [S.Rational(8,100),S.Rational(12,100),0]])
ds=((1,1,1),(-1,-1,1),(-1,1,-1),(1,-1,-1))
js=(1,2,1)
others=(2,0,0)
extra_t=(0,0,1)
assert all(A.T*A==S.eye(3) and A.det()==1 for A in (R,P,L))
assert P**3==S.eye(3)
assert sum(abs(C[i,j]) for i in range(3) for j in range(3))==S.Rational(57,100)
assert all(C[i,js[i]]!=C[i,others[i]] for i in range(3))
G=list(itertools.product((0,1),repeat=2))
def chi(i,v):return ((-1)**v[1],(-1)**(v[0]+v[1]),(-1)**v[0])[i]
def probs(d):
    return [S.factor((1+sum(d[i]*C[i,j]*chi(j,v)*chi(i,w)
         for i in range(3) for j in range(3) if i!=j))/16)
         for v in G for w in G]
for d in ds:
    pp=probs(d)
    assert min(pp)==S.Rational(73,1600) and max(pp)==S.Rational(157,1600)
    assert sum(pp)==1
    for k in range(3):
        for f in (lambda v,w:chi(k,v), lambda v,w:chi(k,w),
                  lambda v,w:chi(k,v)*chi(k,w)):
            assert sum(p*f(v,w) for p,(v,w) in
                       zip(pp,itertools.product(G,G)))==0

ops=[(i,js[i],t) for i in range(3) for t in range(3)]
ops += [(i,others[i],extra_t[i]) for i in range(3)]
assert len(ops)==12
allworld=[]
for d in ds:
    D=S.diag(*d);rd=D*R
    means=[S.factor(d[i]*C[i,j]*(rd*P**t)[i,j]) for i,j,t in ops]
    means.append(S.factor(d[0]*C[0,1]*(L*rd)[0,1]))
    allworld.append(means)
assert all(z[:12]==allworld[0][:12] for z in allworld)
third=[z[-1] for z in allworld]
assert third==[27*S.sqrt(2)/1400,-81*S.sqrt(2)/1400,
               81*S.sqrt(2)/1400,-27*S.sqrt(2)/1400]
gap=min(abs(a-b) for i,a in enumerate(third) for b in third[i+1:])
assert gap==27*S.sqrt(2)/700

eta=S.Rational(7,2000)
a=(S.Rational(9,100),S.Rational(1,10),S.Rational(3,25))
rho=[2*S.sqrt(3)*eta/x for x in a]
Eg=(rho[1]+rho[2])/S.sqrt(2)
Gmax=9/(7*S.sqrt(2))
Ea=S.sqrt(3)*eta
Epred=S.factor(Ea*(Gmax+Eg)+a[0]*Eg)
margin=S.factor(gap-2*(Epred+eta))
assert margin>0
assert all(rho[i]<R[i,2] for i in range(3))
eb=[S.factor((eta+abs(C[i,others[i]])*rho[i])/(S.Rational(6,7)-rho[i]))
    for i in range(3)]
prob_err=S.factor((3*Ea+sum(eb))/16)
assert prob_err<S.Rational(73,1600)
n=math.ceil(2*math.log(26/.05)/float(eta)**2)
assert n==1021034 and 13*n==13273442
print("ROT013 PASS: 6 independent source coordinates, 4 physical worlds")
print("12 exact common Pauli means:", allworld[0][:12])
print("4 distinct left means:",third,"gap:",gap)
print("row L2 bounds:",[float(x) for x in rho])
print("six Fourier max-error:",max(float(Ea),*(float(x) for x in eb)))
print("max p error:",float(prob_err))
print("95pc all-13 settings sufficient total shots:",13*n)
print("deterministic candidate separation margin:",float(margin))
print("NOT a hardware experiment; known gates/SPAM, source-fixed certificate.")
