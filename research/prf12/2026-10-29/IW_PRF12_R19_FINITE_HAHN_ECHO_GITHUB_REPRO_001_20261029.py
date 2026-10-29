#!/usr/bin/env python3
"""R19 standalone: controlled one-sensor finite Hahn echo, source-active.
A static Cauchy xi (arbitrarily dependent across runs, Cauchy marginals);
B Levy Lindblad gamma/2 (AdZ-Id) through square X pi pulse.
No original 3-probe SWAP LOCC gap inference. Requires NumPy+SciPy.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.stats import binom
I=np.eye(2,dtype=complex);X=np.array([[0,1],[1,0]],complex)
Z=np.diag([1,-1]).astype(complex)
plus=np.array([1,1],complex)/math.sqrt(2)
minus=np.array([1,-1],complex)/math.sqrt(2)
def pA(xi,tau,T=1):
 delta=(T-tau)/2;u=xi*tau;h=math.hypot(math.pi,u)
 v=math.cos(h/2)*math.sin(xi*delta)+u/h*math.sin(h/2)*math.cos(xi*delta)
 return v*v
def A_matrix(xi,tau,T=1):
 d=(T-tau)/2
 f=expm(-.5j*xi*d*Z);g=expm(-.5j*(math.pi*X+xi*tau*Z))
 return abs(np.vdot(minus,f@g@f@plus))**2
def pB(gamma,T=1):return (1-math.exp(-gamma*T))/2
def B_matrix(gamma,tau,T=1):
 rho=np.outer(plus,plus.conj()).reshape(4,order='F')
 deph=gamma/2*(np.kron(Z,Z)-np.eye(4))
 H=math.pi*X/(2*tau)
 L=-1j*(np.kron(I,H)-np.kron(H.T,I))+deph
 f=expm((T-tau)/2*deph)
 rho=f@expm(tau*L)@f@rho
 return float(np.vdot(minus,rho.reshape(2,2,order='F')@minus).real)
def risk(gamma,T,tau,N,tail):
 M=gamma/math.tan(math.pi*tail/2)
 u=M*tau
 eps=min(1.,(u/math.pi+u*u/(4*math.pi))**2)
 false=min(1.,N*tail+1-(1-eps)**N)
 missed=(1-pB(gamma,T))**N
 return false,missed,eps,M,math.pi*T/tau
def main():
 rng=np.random.default_rng(19)
 for tau in (.0001,.0008,.01,.1,.4):
  for xi in list(rng.uniform(-100,100,50))+[-1e5,0,1e5]:
   assert abs(pA(xi,tau)-A_matrix(xi,tau))<2e-10
  for gamma in (.1,1,2):
   assert abs(pB(gamma)-B_matrix(gamma,tau))<5e-13
 false,missed,eps,M,control=risk(1,1,.0008,8,.004)
 assert abs(false-.04590461130210699)<1e-12
 assert abs(missed-.04787872899240723)<1e-12
 assert false<.05 and missed<.05
 print('N8 both conditional errors PASS',false,missed,'cutoff',M,'control Omega*T',control)
 C=(2/math.pi**2+1/math.pi**3)**2
 for N in (8,20,50,100,1000):
  false,missed,*_=risk(1,1,N**-3,N,N**-2)
  assert false<=(1+C)/N+1e-12
  print('N',N,'false upper',false,'missed',missed)
 for k in (100000,1000000):
  assert pA((2*k+1)*math.pi,.0008)>.99
 print('R19 source-typed formulas and nonuniformity PASS; no LOCC closure result')
if __name__=='__main__':main()
