#!/usr/bin/env python3
"""PRF12 R18 compact independent reproduction: S,M1,M2 two active SWAPs.
Static A Cauchy integrated deterministically; B continuous Lindblad ON the
gate, not independent finite B-phase. Memory parking local dephasing exact.
Python 3, numpy, scipy. NOT all-run iid nor a full LOCC-optimality claim.
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.linalg import expm
i=np.eye(2,dtype=complex);x=np.array([[0,1],[1,0]],complex)
y=np.array([[0,-1j],[1j,0]],complex);z=np.diag([1,-1])
I=np.eye(8,dtype=complex)
bits=np.array([[int(t) for t in f'{j:03b}'] for j in range(8)])
def k(a,b,c):return np.kron(np.kron(a,b),c)
Z=k(z,i,i)
def sw(t):
 r=np.zeros((8,8),complex)
 for j,b in enumerate(bits):
  a=b.copy();a[0],a[t]=a[t],a[0]
  r[4*a[0]+2*a[1]+a[2],j]=1
 return r
S=(sw(1),sw(2))
def same(a):
 return k(*([(i+a)/2]*3))+k(*([(i-a)/2]*3))
e=.02
angle=math.pi/2+e
E=(same(x)+same(math.cos(angle)*x+math.sin(angle)*y))/2
psi0=np.ones(8,dtype=complex)/math.sqrt(8)
rho0=np.outer(psi0,psi0.conj())
L0=[-1j*(np.kron(math.pi/2*s,I)-np.kron(I,(math.pi/2*s).T)) for s in S]
Lz=(np.kron(Z,Z)-np.eye(64))/2
def memory(rho,kT,t):
 m1=math.exp(-kT*(2/3+t));m2=math.exp(-kT/3)
 return rho*np.where(bits[:,None,1]!=bits[None,:,1],m1,1)*np.where(bits[:,None,2]!=bits[None,:,2],m2,1)
def pa_xi(xi,t,kT):
 ph=xi/3;diag=np.exp(-.5j*ph*(1-2*bits[:,0]))
 v=diag*psi0
 for s in S:
  H=(math.pi/2)*s+(xi*t/2)*Z
  w,u=np.linalg.eigh(H)
  v=(u*np.exp(-1j*w))@u.conj().T@v
  v=diag*v
 return np.trace(E@memory(np.outer(v,v.conj()),kT,t)).real
def pb(t,q,kT):
 rho=rho0*np.where(bits[:,None,0]!=bits[None,:,0],math.exp(-q),1)
 for L in L0:
  rho=(expm(L+3*q*t*Lz)@rho.reshape(-1)).reshape(8,8)
  rho=rho*np.where(bits[:,None,0]!=bits[None,:,0],math.exp(-q),1)
 return float(np.trace(E@memory(rho,kT,t)).real)
def approx(t,q=1/3,kT=.3,n=576):
 v,w=leggauss(n)
 return sum(weight*pa_xi(3*q*math.tan(math.pi*node/2),t,kT)/2 for node,weight in zip(v,w))
def lower_bound(t,q=1/3,kT=.3,c=20,N=2000):
 # Bound |pa(xi)-pa(xi')|<=Tphys*|xi-xi'| by Duhamel.
 gamma=3*q
 edges=np.linspace(-c*gamma,c*gamma,N+1)
 w=np.diff(np.arctan(edges/gamma))/math.pi
 mids=(edges[1:]+edges[:-1])/2
 v=sum(weight*pa_xi(xi,t,kT) for xi,weight in zip(mids,w))
 error=(1+2*t)*(edges[1]-edges[0])*w.sum()/2
 return v-error,v+error+(1-w.sum())
def main():
 for t in (.001,.01,.05,.15,.3,1.):
  b=pb(t,1/3,.3)
  a=approx(t)
  low,high=lower_bound(t)
  assert low>b+.09
  print('tau/Tfree',t,'pA approx',a,'pB',b,
        'contrast approx',a-b,'positive contrast lower',low-b)
 # Countersequence at fixed q=1/3, kappa*Tfree=.3.
 for n in (10,100,300):
  xi=6*math.pi*n;t=4/xi
  a=pa_xi(xi,t,.3);b=pb(t,1/3,.3)
  assert a<b
  print('persistent xi counterexample n',n,'tau',t,'pAxi',a,'pB',b)
 print('No uniform source-A phase guarantee for any finite source-active SWAP.')
if __name__=='__main__':main()
