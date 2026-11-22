#!/usr/bin/env python3
"""ROT015 short independent exact symbolic witness (SymPy required).
Four *control-conditioned*, separately causal classical Pauli sources, not
one intervention-independent process comb. No quantum hardware.
"""
import itertools,math
import sympy as S
R=S.Matrix([[-3,-2,6],[6,-3,2],[2,6,3]])/7
P=S.Matrix([[0,0,1],[1,0,0],[0,1,0]])
L=S.Matrix([[0,1/S.sqrt(2),1/S.sqrt(2)],
            [1,0,0],[0,1/S.sqrt(2),-1/S.sqrt(2)]])
C=S.Matrix([[0,S.Rational(9,100),S.Rational(11,100)],
            [S.Rational(7,100),0,S.Rational(10,100)],
            [S.Rational(8,100),S.Rational(12,100),0]])
DS=((1,1,1),(-1,-1,1),(-1,1,-1),(1,-1,-1))
G=list(itertools.product((0,1),repeat=2))
chi=lambda i,v:((-1)**v[1],(-1)**(v[0]+v[1]),(-1)**v[0])[i]
SIX=[(i,j) for i in range(3) for j in range(3) if i!=j]
def prob(K):
 return [S.factor((1+sum(K[i,j]*chi(j,v)*chi(i,w)
          for i,j in SIX))/16) for v in G for w in G]
def tv(a,b):return S.factor(sum(abs(x-y) for x,y in zip(a,b))/2)
assert all(X.T*X==S.eye(3) and X.det()==1 for X in (R,P,L))
assert P**3==S.eye(3)
ops=[]
for i,j in enumerate((1,2,1)):
 for t in range(3):ops.append((i,j,t))
ops.extend(((0,2,0),(1,0,0),(2,0,1)))
assert len(ops)==12
ref=[S.factor(C[i,j]*(R*P**t)[i,j]) for i,j,t in ops]
ref.append(S.factor(C[0,1]*(L*R)[0,1]))
for idx,d in enumerate(DS):
 D=S.diag(*d);RR=D*R;CC=D*C
 q=prob(CC)
 assert sum(q)==1 and min(q)==S.Rational(73,1600)
 assert [S.factor(CC[i,j]*(RR*P**t)[i,j]) for i,j,t in ops]==ref[:12]
 needed=S.factor(ref[-1]/(L*RR)[0,1]);change=S.factor(needed-CC[0,1])
 CCleft=CC.copy();CCleft[0,1]=needed
 qq=prob(CCleft)
 assert min(qq)>0 and sum(qq)==1
 assert S.simplify(CCleft[0,1]*(L*RR)[0,1]-ref[-1])==0
 assert tv(q,qq)==abs(change)/2
 assert tv(q,qq)==(S.Rational(0),S.Rational(3,50),
                    S.Rational(3,100),S.Rational(9,100))[idx]
 print('world',idx,'source-TV spoof',tv(q,qq),'min legal p',min(qq))
ctx={0:[],1:[],2:[],3:[(0,1)]}
for i,j,t in ops:ctx[t].append((i,j))
assert [len(set(ctx[t])) for t in range(4)]==[5,4,3,1]
assert sum(6-len(set(ctx[t])) for t in range(4))==11
print('24 conditional Fourier parameters - rank 13 = nullity 11')
# One small legal intervention-only source drift (context I) is invisible.
pert=C.copy();pert[2,0]+=S.Rational(1,1000)
assert min(prob(pert))>0 and tv(prob(C),prob(pert))==S.Rational(1,2000)
assert all((pert if t==0 else C)[i,j]*(R*P**t)[i,j]==C[i,j]*(R*P**t)[i,j]
           for i,j,t in ops)
print('invisible intervention-specific p change TV 0.0005: PASS')
# AUD3's earlier interval eta=.008 (source firstness AUD3) + PRF14 ROT014
# calibrated source-TV bias: e=stat+mu+2TV=0.00799 < 0.008.
assert S.Rational(6,1000)+S.Rational(39,100000)+2*S.Rational(8,10000)==S.Rational(799,100000)
n=math.ceil(2*math.log(520)/(.006**2))
assert n==347435 and 13*n==4516655
print('conditional 95% Hoeffding (given independent AUD3 box):',13*n,'shots')
print('EXACT ROT015 SOURCE TEST PASS / NO_HARDWARE / NO_NOVELTY')
