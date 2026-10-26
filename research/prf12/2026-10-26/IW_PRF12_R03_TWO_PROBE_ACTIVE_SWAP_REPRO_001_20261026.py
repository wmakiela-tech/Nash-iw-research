#!/usr/bin/env python3
"""PRF12 R03 independent rerun of the two-probe model; NOT a physical device test.
Requirements: Python 3, numpy, scipy. gamma,T,kappa are fixed synthetic model values.
A: one hidden Cauchy xi held across the entire sequence (including SWAP).
B: Markovian dephasing gamma/2 (Z rho Z-rho) throughout.
Finite Cauchy integration tail is replaced by a positive reference state, with
rigorous <=2*tail_mass trace norm difference and numeric quadrature refinement.
"""
import numpy as np
from scipy.linalg import expm
from math import pi,exp,atan,log
T=1.; GAMMA=1.; OMEGA=8.; TAU=pi/(2*OMEGA)
Z=np.diag([1.,1.,-1.,-1.]).astype(complex)
ZM=np.diag([1.,-1.,1.,-1.]).astype(complex)
SWAP=np.eye(4,dtype=complex)[[0,2,1,3]]
psi0=np.ones(4,complex)/2
R0=np.outer(psi0,psi0.conj())
sbits=np.array([0,0,1,1]); mbits=np.array([0,1,0,1])
sflip=sbits[:,None]!=sbits[None,:]
mflip=mbits[:,None]!=mbits[None,:]
X=np.array([[0.,1.],[1.,0.]])
XX=np.kron(X,X)
def dephase(rho,dt,mask,rate):
    return rho*np.where(mask,np.exp(-rate*dt),1.)
def b_pulse(rho):
    H=OMEGA*SWAP
    L=np.empty((16,16),complex)
    for j in range(16):
        e=np.zeros((4,4),complex);e.flat[j]=1.
        L[:,j]=(-1j*(H@e-e@H)+GAMMA/2*(Z@e@Z-e)).ravel()
    return (expm(TAU*L)@rho.ravel()).reshape(4,4)
def B(p,kappa):
    d1=p*(T-TAU);d2=(1-p)*(T-TAU)
    r=dephase(R0,d1,sflip,GAMMA)
    r=b_pulse(r)
    return dephase(dephase(r,d2,sflip,GAMMA),d2,mflip,kappa)
def A(p,kappa,xi_max=100000.,step=.2,chunk=100000):
    d1=p*(T-TAU);d2=(1-p)*(T-TAU)
    N=round(2*xi_max/step);step=2*xi_max/N
    r=np.zeros((4,4),complex)
    for first in range(0,N+1,chunk):
        inds=np.arange(first,min(N+1,first+chunk))
        xi=-xi_max+step*inds
        weights=(GAMMA/pi)/(GAMMA**2+xi**2)*step
        weights*=np.where((inds==0)|(inds==N),.5,1.)
        phase=np.exp(-.5j*xi*d1)
        p0=np.empty((len(xi),4),complex)
        p0[:,0]=p0[:,1]=.5*phase
        p0[:,2]=p0[:,3]=.5*np.conj(phase)
        w=np.hypot(OMEGA,xi/2)
        c=np.cos(w*TAU);s=np.sin(w*TAU)/w
        v=np.empty_like(p0)
        v[:,0]=np.exp(-1j*TAU*(OMEGA+xi/2))*p0[:,0]
        v[:,3]=np.exp(-1j*TAU*(OMEGA-xi/2))*p0[:,3]
        v[:,1]=(c-1j*xi*s/2)*p0[:,1]-1j*OMEGA*s*p0[:,2]
        v[:,2]=-1j*OMEGA*s*p0[:,1]+(c+1j*xi*s/2)*p0[:,2]
        phase2=np.exp(-.5j*xi*d2)
        v[:,0]*=phase2;v[:,1]*=phase2
        v[:,2]*=np.conj(phase2);v[:,3]*=np.conj(phase2)
        r+=np.einsum('n,ni,nj->ij',weights,v,v.conj())
    tail=2/pi*atan(GAMMA/xi_max)
    r+=tail*R0
    return dephase(r,d2,mflip,kappa),tail
def ref(p,kappa):
    d1=p*(T-TAU); d2=(1-p)*(T-TAU)
    rA=np.empty((4,4),complex);rB=np.empty((4,4),complex)
    for i in range(4):
        for j in range(4):
            ds=sbits[i]-sbits[j]; dm=mbits[i]-mbits[j]
            fac=exp(-kappa*d2) if dm else 1.
            rA[i,j]=fac*exp(-GAMMA*abs(d1*dm+d2*ds))/4
            rB[i,j]=fac*exp(-GAMMA*(d1*abs(dm)+d2*abs(ds)))/4
    return rA,rB
def tv(rA,rB):
    D=(rA-rB); D=(D+D.conj().T)/2
    hel=np.abs(np.linalg.eigvalsh(D)).sum()/2
    parity=abs(np.real(np.trace(XX@D)))/2
    x_or=abs(np.real(np.vdot(psi0,D@psi0)))
    others=np.array(D,copy=True);others[1,2]=others[2,1]=0.
    return hel,parity,x_or,np.max(np.abs(others))
def cref(p,kappa):
    d1=p*(T-TAU);d2=(1-p)*(T-TAU)
    return exp(-kappa*d2)/4*(exp(-GAMMA*abs(d1-d2))-exp(-GAMMA*(d1+d2)))
def pstar(kappa):
    F=T-TAU
    kcrit=2*GAMMA/(1-exp(-GAMMA*F))
    return .5 if kappa<=kcrit else 1-log(kappa/(kappa-2*GAMMA))/(2*GAMMA*F)
def main():
    print('parameters T,gamma,Omega,tau:',T,GAMMA,OMEGA,TAU)
    F=T-TAU
    print('critical_kappa:',2*GAMMA/(1-exp(-GAMMA*F)))
    for kappa in [.3,3.,5.,10.]:
        p=pstar(kappa)
        rA,rB=ref(p,kappa)
        print('REF',kappa,'p*',p,'TV',tv(rA,rB)[0],'analytic c',cref(p,kappa))
    for kappa,p in [(.3,.5),(5.,.5),(5.,.682184202),(5.,.8),(5.,.9)]:
        b=B(p,kappa)
        a,tail=A(p,kappa)
        print('ACTIVE',kappa,p,'TV_H,TV_parity,TV_XOR,other_max',tv(a,b),'tail_mass',tail)
    for bound,step in [(10000.,.2),(10000.,.1),(100000.,.2),(100000.,.1)]:
        a,tail=A(.5,.3,xi_max=bound,step=step)
        print('TRUNCATION',bound,step,'TV',tv(a,B(.5,.3))[0],'tail_bound_TV',tail)
if __name__=='__main__':main()
