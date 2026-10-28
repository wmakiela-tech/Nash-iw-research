import numpy as np
from math import exp,pi,sqrt
from itertools import product
I=np.eye(8,dtype=complex);w=(I[1]+I[2]+I[4])/sqrt(3);v=(I[3]+I[5]+I[6])/sqrt(3)
P=np.outer(w,w)+np.outer(v,v);K=np.outer(I[0],I[0])+np.outer(I[7],I[7]);Q=I-P-K
bits=np.array(list(product((0,1),repeat=3)));o=np.exp(2j*pi/3)
def kron(a,b,c):return np.kron(np.kron(a,b),c)
def e(z):return np.array([1,z])/sqrt(1+abs(z)**2)
def D(q):
 d=bits[:,None,:]-bits[None,:,:]
 return (np.exp(-q*abs(d.sum(2)))-np.exp(-q*abs(d).sum(2)))/8
def F(t):
 if t<=1:
  a=np.diag([1,1-t]);return kron(a,a,a)
 z=t-1;v=kron(e(z),e(o*z),e(o*o*z));return exp(-z)*np.outer(v,v.conj())
rng=np.random.default_rng(28)
for q in [.05,1/3,.7,1.6,2.5]:
 x=exp(-q);b=1-x*x
 for _ in range(30):
  a=rng.normal(size=(8,8))+1j*rng.normal(size=(8,8));h=a.conj().T@a;E=h/np.linalg.eigvalsh(h).max()
  err=np.trace((I-E)@P).real/4+np.trace(E@Q).real/8
  gap=b/2-np.trace(E@D(q)).real
  assert b*(1-x)*err<gap+1e-12< b*(1+x)*err+1e-12
trace=[]
for t in np.linspace(0,2,201):
 m=F(t);trace.append(np.trace(m).real)
 assert np.linalg.eigvalsh(m).min()>-1e-12 and np.linalg.norm(P@m@Q)<1e-12
assert max(np.diff(trace))<1e-12
print('PASS: regret/error sandwich, kernel product path, 201 checkpoints')
print('NO full LOCC closure-gap assertion')
