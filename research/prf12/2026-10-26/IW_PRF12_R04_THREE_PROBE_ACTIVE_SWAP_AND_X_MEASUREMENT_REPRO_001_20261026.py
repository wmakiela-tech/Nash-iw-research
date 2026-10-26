#!/usr/bin/env python3
"""PRF12 R04: 3 qubits, two finite SWAPs. NumPy/SciPy, source-typed and synthetic.
A: one static Cauchy xi through whole circuit. B: gamma/2(Z_S rho Z_S-rho)
during both pulses and all free intervals. Post-SWAP memory ages are physical.
Numerics are NOT a substitute for the analytic ideal-clock lemma.
"""
import numpy as np
from scipy.linalg import expm
from math import pi, atan, exp
T=1.; gamma=1.; Omega=8.; tau=pi/(2*Omega); n=8
i2=np.eye(2, dtype=complex)
Z=np.diag([1.,-1.]).astype(complex)
X=np.array([[0.,1.],[1.,0.]],complex)
bits=np.array([[(j>>2)&1,(j>>1)&1,j&1] for j in range(n)])
zs=1-2*bits[:,0]
Zs=np.kron(np.kron(Z,i2),i2)
psi=np.ones(n,complex)/np.sqrt(n)
rho0=np.outer(psi,psi.conj())
mS=bits[:,None,0]!=bits[None,:,0]
m1=bits[:,None,1]!=bits[None,:,1]
m2=bits[:,None,2]!=bits[None,:,2]
had=np.array([[1.,1.],[1.,-1.]],complex)/np.sqrt(2)
W=np.kron(np.kron(had,had),had)
XXX=np.kron(np.kron(X,X),X)
swaps=[]
for j in (1,2):
    S=np.zeros((n,n),complex)
    for k in range(n):
        v=bits[k].copy();v[0],v[j]=v[j],v[0]
        idx=4*v[0]+2*v[1]+v[2];S[idx,k]=1.
    swaps.append(S)
pulseB=[]
for S in swaps:
    L=np.empty((n*n,n*n),complex)
    for k in range(n*n):
        r=np.zeros((n,n),complex);r.ravel()[k]=1.
        h=Omega*S
        L[:,k]=(-1j*(h@r-r@h)+gamma/2*(Zs@r@Zs-r)).ravel()
    pulseB.append(expm(tau*L))
def dephase(r,mask,dt,rate):
    return r*np.where(mask,np.exp(-rate*dt),1.)
def B(fracs,kappa):
    d1,d2,d3=np.array(fracs)*(T-2*tau)
    r=dephase(rho0,mS,d1,gamma)
    r=(pulseB[0]@r.ravel()).reshape(n,n)
    r=dephase(r,mS,d2,gamma)
    r=(pulseB[1]@r.ravel()).reshape(n,n)
    r=dephase(r,mS,d3,gamma)
    return dephase(dephase(r,m1,d2+tau+d3,kappa),m2,d3,kappa)
def pulse_vector(v,xis,j):
    """Exact exp of Omega SWAP + xi Z_s/2 using disjoint 1x1,2x2 sectors."""
    freq=np.hypot(Omega,xis/2.)
    cc=np.cos(freq*tau)
    ss=np.sin(freq*tau)/freq
    out=np.empty_like(v)
    for k in range(n):
        if bits[k,0]==bits[k,j]:
            out[:,k]=np.exp(-1j*(Omega+xis*zs[k]/2.)*tau)*v[:,k]
        else:
            flip=bits[k].copy();flip[0],flip[j]=flip[j],flip[0]
            l=4*flip[0]+2*flip[1]+flip[2]
            out[:,k]=(cc-1j*xis*zs[k]*ss/2.)*v[:,k]-1j*Omega*ss*v[:,l]
    return out
def A(fracs,kappa,cut=30000.,step=.3,chunk=100000):
    d1,d2,d3=np.array(fracs)*(T-2*tau)
    size=int(np.ceil(2*cut/step));dx=2*cut/size
    rho=np.zeros((n,n),complex)
    for low in range(0,size+1,chunk):
        indexes=np.arange(low,min(size+1,low+chunk))
        xi=-cut+dx*indexes
        weights=gamma/(pi*(gamma**2+xi**2))*dx
        weights[(indexes==0)|(indexes==size)]*=.5
        v=np.repeat(psi[None,:],len(xi),axis=0)
        v*=np.exp(-.5j*xi[:,None]*zs[None,:]*d1)
        v=pulse_vector(v,xi,1)
        v*=np.exp(-.5j*xi[:,None]*zs[None,:]*d2)
        v=pulse_vector(v,xi,2)
        v*=np.exp(-.5j*xi[:,None]*zs[None,:]*d3)
        rho+=np.einsum('i,ij,ik->jk',weights,v,v.conj(),optimize=True)
    tail=2/pi*atan(gamma/cut)
    rho+=tail*rho0
    return dephase(dephase(rho,m1,d2+tau+d3,kappa),m2,d3,kappa),tail
def ideal(fracs,kappa):
    ds=np.array(fracs)*T;ts=np.cumsum(ds)
    ra=np.empty((n,n),complex);rb=np.empty((n,n),complex)
    for k in range(n):
        for l in range(n):
            diff=bits[k]-bits[l]
            aging=sum(kappa*(T-ts[j])*(diff[j]!=0) for j in range(3))
            ra[k,l]=np.exp(-gamma*abs(np.dot(ds,diff))-aging)/n
            rb[k,l]=np.exp(-gamma*np.dot(ds,np.abs(diff))-aging)/n
    return ra,rb
def metrics(ra,rb):
    D=ra-rb;D=(D+D.conj().T)/2
    hel=np.sum(abs(np.linalg.eigvalsh(D)))/2
    probs=np.real(np.diag(W@D@W.conj().T))
    full=np.sum(abs(probs))/2
    parity=abs(np.trace(XXX@D).real)/2
    or_test=abs(np.vdot(psi,D@psi).real)
    return np.array([hel,full,parity,or_test,hel-full])
def closed_form_equal_no_memory(q):
    x=exp(-q);z=1-x*x
    hel=z/2
    xfull=z*(6+9*x)/32 if x>=2/3 else 3*z/8
    parity=3*x*z/8
    x_or=3*z*(2+x)/32
    return np.array([hel,xfull,parity,x_or,hel-xfull])
if __name__=="__main__":
    print("PRF12 R04 / T",T,"gamma",gamma,"Omega",Omega,"tau",tau,"F",T-2*tau)
    exact=metrics(*ideal([1/3]*3,0.))
    closed=closed_form_equal_no_memory(gamma*T/3)
    assert np.max(abs(exact-closed))<1e-13
    print("IDEAL_ZERO_MEMORY EXACT",exact,"CLOSED_FORM",closed)
    for frac,k in [([1/3]*3,.3),([.55,.3,.15],.3),([1/3]*3,5.),([.55,.3,.15],5.)]:
        i=metrics(*ideal(frac,k))
        aa,tail=A(frac,k)
        a=metrics(aa,B(frac,k))
        assert a[4]>2*tail
        print("DATA",frac,"kappa",k,"reference",i,"ACTIVE",a,"cauchy_tail_TV_bound",tail)
    for cut,step in [(10000.,.3),(30000.,.3),(30000.,.15),(100000.,.25)]:
        aa,tail=A([1/3]*3,.3,cut,step)
        print("STRESS",cut,step,metrics(aa,B([1/3]*3,.3)),tail)
