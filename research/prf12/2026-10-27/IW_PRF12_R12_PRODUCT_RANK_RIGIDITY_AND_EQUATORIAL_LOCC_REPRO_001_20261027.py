#!/usr/bin/env python3
"""PRF12 R12; exact n=3 ideal Cauchy-vs-Levy endpoint, kappa=0.
Independent SEP9 and three-party equatorial adaptive LOCC witness checks.
Not a certification of a general LOCC discrimination gap. Requires numpy.
"""
import numpy as np
from math import pi,exp,sqrt
from itertools import product
bits=np.array(list(product((0,1),repeat=3)),dtype=int)
I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
eta=np.exp(2j*pi/9)
triples=[(0,0,0),(3,3,3),(6,6,6),(1,4,7),(4,7,1),(7,1,4),(5,2,8),(8,5,2),(2,8,5)]
def state(exps):
    v=np.array([1.],complex)
    for t in exps:v=np.kron(v,np.array([1,eta**t],complex)/sqrt(2))
    return v
def D(q):
    d=bits[:,None,:]-bits[None,:,:]
    return (np.exp(-q*np.abs(d.sum(2)))-np.exp(-q*np.abs(d).sum(2)))/8
def proj(phi,s):
    return (I+s*(np.cos(phi)*X+np.sin(phi)*Y))/2
def tv_direct(q,alpha,betap,betam):
    state=D(q).reshape((2,)*6);value=0.
    for s in (+1,-1):
        pa=proj(alpha,s)
        for t in (+1,-1):
            pb=proj(betap if s==1 else betam,t)
            c=np.einsum('abcABC,Aa,Bb->cC',state,pa,pb)
            value+=np.abs(np.linalg.eigvalsh(c)).sum()/2
    return float(value)
def tv_closed(q,alpha,betap,betam):
    x=exp(-q);b=1-x*x;a=x*b
    ca,sa=np.cos(alpha),np.sin(alpha);result=0.
    for s in (+1,-1):
        beta=betap if s==1 else betam
        cb,sb=np.cos(beta),np.sin(beta)
        for t in (+1,-1):
            u=b*s*t*np.cos(alpha-beta)/16
            vx=b*(s*ca+t*cb)/16+a*s*t*(3*ca*cb+sa*sb)/32
            vy=b*(s*sa+t*sb)/16+a*s*t*(ca*sb+sa*cb)/32
            result+=max(abs(u),np.hypot(vx,vy))
    return float(result)
def fixed_x(q):
    x=exp(-q);b=1-x*x
    return b*(6+9*x)/32 if x>=2/3 else 3*b/8
def r08(q):
    x=exp(-q);b=1-x*x
    return b*(4+3*x+max(2,3*x)+2*sqrt(4+(2-x)**2))/32
def main():
    v=np.column_stack([state(row) for row in triples])
    g=v.conj().T@v
    assert np.max(abs(abs(g[np.triu_indices(9,1)])-1/8))<5e-14
    assert np.max(abs((8/9)*v@v.conj().T-np.eye(8)))<5e-14
    for q in (.05,1/3,.7,1.4,3):
        d=D(q);h=np.abs(np.linalg.eigvalsh(d)).sum()/2
        p=(8/9)*v[:,:3]@v[:,:3].conj().T
        assert abs(h-(1-exp(-2*q))/2)<5e-14
        assert abs(np.trace(p@d).real-h)<5e-14
    print('SEP9 frame and Helstrom checks PASS')
    for q,ang in ((1/3,(0,0,pi/2)),
                  (1.6,(pi/2,pi/2-.1,pi/2+.1)),
                  (2.5,(pi/2,pi/2-.04,pi/2+.04)),
                  (.7,(.44,.32,1.1))):
        z=tv_direct(q,*ang)
        assert abs(z-tv_closed(q,*ang))<5e-14
        print('q',q,'hel',(1-exp(-2*q))/2,
              'X',fixed_x(q),'R08',r08(q),'R12',z)
    print('Rank-one rigidity proof: coefficients of')
    print('(b0+b1*t)*(c0+c1*t) vanish only if b or c=zero.')
    print('Full LOCC closure gap still OPEN.')
if __name__=='__main__':main()
