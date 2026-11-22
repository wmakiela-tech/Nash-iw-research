#!/usr/bin/env python3
"""PRF14 ROT018 compact reproducibility of exact five-control Pauli beacon
closure, legal source violation, 4-setting 95% Hoeffding bounds and the
full five-context conditional-source gauge. SymPy required. No hardware.
"""
import itertools, math
import sympy as s
f=s.Rational
R=s.Matrix([[-3,-2,6],[6,-3,2],[2,6,3]])/7
P=s.Matrix([[0,0,1],[1,0,0],[0,1,0]])
L=s.Matrix([[0,1/s.sqrt(2),1/s.sqrt(2)],[1,0,0],[0,1/s.sqrt(2),-1/s.sqrt(2)]])
C=s.Matrix([[0,f(9,100),f(11,100)],[f(7,100),0,f(1,10)],[f(8,100),f(12,100),0]])
S=lambda RR:(RR,RR*P,RR*P**2,L*RR,P**2*RR)
basis=list(itertools.product((0,1),repeat=2))
chi=lambda i,v:((-1)**v[1],(-1)**(v[0]+v[1]),(-1)**v[0])[i]
D={v:s.diag(*(chi(i,v) for i in range(3))) for v in basis}
def probs(B):
 return [s.factor((1+sum(B[i,j]*chi(j,v)*chi(i,w)
          for i in range(3) for j in range(3) if i!=j))/16)
          for v in basis for w in basis]
def fullchannel(B,U):
 z=s.zeros(3)
 for p,(v,w) in zip(probs(B),itertools.product(basis,basis)):z+=p*D[w]*U*D[v]
 return z.applyfunc(s.simplify)
def h(v):return s.factor(v[3]**2+v[4]**2-v[1]**2-v[2]**2)
assert all(z.T*z==s.eye(3) and z.det()==1 for z in (R,P,L))
assert P**3==s.eye(3)
A=S(R)
y=[s.factor(C[1,2]*z[1,2]) for z in A]
assert y==[f(1,35),f(3,35),-f(3,70),f(3,35),f(3,70)]
assert h(y)==0
for U in A:assert fullchannel(C,U)==s.Matrix(3,3,lambda i,j:C[i,j]*U[i,j])
drift=C.copy();drift[1,2]=f(1,5)
assert min(probs(drift))==f(63,1600)
assert sum(probs(drift))==1
assert sum(abs(a-b) for a,b in zip(probs(drift),probs(C)))/2==f(1,20)
yd=y.copy();yd[3]=f(6,35)
assert h(yd)==f(27,1225)
eta=f(27,2000); trueabs=sum(abs(yd[q]) for q in (1,2,3,4))
assert trueabs==f(12,35)
assert h(yd)-4*eta*trueabs-16*eta**2==f(7479,12250000)>0
n=math.ceil(2*math.log(8/.05)/float(eta)**2)
assert n==55695
# Physical calibration bound assumes known actual controls within SO3 opnorm .001,
# preparation/meas/bias error <=.00005 each, and source max |C| <=.2.
mu=f(55,100000); stat=f(13,1000);e=stat+mu
assert h(yd)-4*e*trueabs-16*e**2>0
ncal=math.ceil(2*math.log(8/.05)/float(stat)**2)
assert ncal==60062
# Exact physical 5-channel nonidentification with varied source in all contexts.
t=f(1,1000)
U=s.Matrix([[1,0,0],[0,(1-t*t)/(1+t*t),-2*t/(1+t*t)],
            [0,2*t/(1+t*t),(1-t*t)/(1+t*t)]])
assert U.T*U==s.eye(3) and U.det()==1
Alt=S(U*R)
sources=[]
for q in range(5):
 B=s.Matrix(3,3,lambda i,j:s.factor(C[i,j]*A[q][i,j]/Alt[q][i,j])
            if i!=j else 0)
 assert min(probs(B))>0 and sum(probs(B))==1
 assert fullchannel(B,Alt[q])==fullchannel(C,A[q])
 sources.append(B)
assert len(set(str(B[1,2]) for B in sources))>1
print('PASS exact 5-control beacon SO3 quadratic closure')
print('PASS strictly positive intervention dependent source TV=1/20')
print('PASS 45/45 full physical Bloch channel equalities without beacon')
print('95pc sufficient ideal 4-setting shots:',4*n)
print('95pc sufficient bounded calibrated 4-setting shots:',4*ncal)
print('NO GENERAL QUANTUM COMB / NO HARDWARE / NO EXTERNAL NOVELTY')
