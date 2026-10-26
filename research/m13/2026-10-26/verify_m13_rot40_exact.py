#!/usr/bin/env python3
"""ROT40: source-independent exact Fraction polynomial and GLS geometry checks.
Confirms the universal divisibility H=(beta-alpha)Q and its sign logic;
NOT a proof that historical source coefficients are exactly rational.
"""
from fractions import Fraction as F
from random import Random
rng=Random(401026); N=41;ks=range(2,7);n=[(N-2*k)**3 for k in ks];w=[n[i]-n[i+1] for i in range(4)]+[n[-1]]

def add(x,y):
 z=dict(x)
 for k,v in y.items():z[k]=z.get(k,F(0))+v
 return {k:v for k,v in z.items() if v}
def mul(x,y):
 z={}
 for (i,j),v in x.items():
  for (k,l),u in y.items():z[i+k,j+l]=z.get((i+k,j+l),F(0))+v*u
 return {k:v for k,v in z.items() if v}
def sc(x,t):return {k:v*t for k,v in x.items()}
def db(x):return {(i,j-1):v*j for (i,j),v in x.items() if j>0}
def ea(x,a,b):return sum((v*a**i*b**j for (i,j),v in x.items()),F(0))
def ev(p,x):return sum((c*x**i for i,c in enumerate(p)),F(0))

def polyproof(shell):
 p={};q={}
 for i in range(5):
  a={(j,0):c for j,c in enumerate(shell[i])}
  b={(0,j):c for j,c in enumerate(shell[i])}
  p=add(p,sc(mul(a,b),w[i]));q=add(q,sc(mul(b,b),w[i]))
 H=add(sc(mul(db(p),q),2),sc(mul(p,db(q)),-1))
 degree=max(j for i,j in H);Q=[{} for _ in range(degree)]
 Q[-1]={i:v for (i,j),v in H.items() if j==degree}
 for j in range(degree-1,0,-1):
  coeff={i:v for (i,k),v in H.items() if k==j};shift={i+1:v for i,v in Q[j].items()}
  Q[j-1]={i:coeff.get(i,F(0))+shift.get(i,F(0)) for i in set(coeff)|set(shift)}
 q2={(i,j):v for j,t in enumerate(Q) for i,v in t.items() if v}
 H2=mul(q2,{(0,1):F(1),(1,0):F(-1)})
 assert {k:v for k,v in H.items() if v}=={k:v for k,v in H2.items() if v},'factor identity'
 return H,p,q

def verify():
 tests=0
 for trial in range(40):
  # Positive sample quartics, source free and deterministic.
  shell=[[F(rng.randint(20,90),17)] + [F(rng.randint(-2,4),51) for i in range(4)] for k in range(5)]
  H,p,q=polyproof(shell)
  for al,be in [(F(0),F(0)),(F(1,20),F(0)),(F(1,20),F(3,25)),(F(1,10),F(9,100)),(F(1,5),F(0))]:
   aval=[ev(s,al) for s in shell];bval=[ev(s,be) for s in shell];bp=[sum((j*s[j]*be**(j-1) for j in range(1,5)),F(0)) for s in shell]
   pp=sum((w[i]*aval[i]*bval[i] for i in range(5)),F(0));qq=sum((w[i]*bval[i]**2 for i in range(5)),F(0))
   pp1=sum((w[i]*aval[i]*bp[i] for i in range(5)),F(0));qq1=2*sum((w[i]*bval[i]*bp[i] for i in range(5)),F(0))
   assert ea(p,al,be)==pp and ea(q,al,be)==qq
   assert ea(H,al,be)==2*pp1*qq-pp*qq1
   d2=sum((w[i]*aval[i]**2 for i in range(5)),F(0))-pp**2/qq
   wedge=sum((w[i]*w[j]*(aval[i]*bval[j]-aval[j]*bval[i])**2 for i in range(5) for j in range(i+1,5)))/qq
   assert d2==wedge,'exact projection wedge'
   derivative=-pp*(2*pp1*qq-pp*qq1)/qq**2
   assert derivative==-pp*ea(H,al,be)/qq**2
   tests+=1
 print('ROT40 INDEPENDENT EXACT Fraction PASS',tests,'geometry cases +',40,'coefficient factorizations')
if __name__=='__main__':verify()