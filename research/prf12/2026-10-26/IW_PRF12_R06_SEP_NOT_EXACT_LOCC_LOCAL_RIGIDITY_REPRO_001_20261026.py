#!/usr/bin/env python3
"""PRF12 R06 exact n=3 Cauchy/Lévy SEP-versus-LOCC obstruction.
Requires only NumPy. No hardware or approximate LOCC optimum claim.
"""
import numpy as np
from itertools import permutations, product
from math import pi,exp,sqrt
from numpy.linalg import eigvalsh
bits=np.array(list(product((0,1),repeat=3)))
eye=np.eye(8,dtype=complex);eye2=np.eye(2,dtype=complex)
ket=lambda s:eye[int(s,2)]
w=(ket('001')+ket('010')+ket('100'))/sqrt(3)
wb=(ket('110')+ket('101')+ket('011'))/sqrt(3)
q1=(2*ket('100')-ket('001')-ket('010'))/sqrt(6)
q2=(2*ket('011')-ket('101')-ket('110'))/sqrt(6)
pplus=np.outer(w,w.conj())+np.outer(wb,wb.conj())
pzero=np.outer(ket('000'),ket('000'))+np.outer(ket('111'),ket('111'))
pminus=eye-pplus-pzero

def D(q):
    diff=bits[:,None,:]-bits[None,:,:]
    return (np.exp(-q*abs(diff.sum(axis=-1)))-np.exp(-q*abs(diff).sum(axis=-1)))/8

def local_effect_on_party(e,j):
    ops=[eye2]*3
    ops[j]=e
    return np.kron(np.kron(ops[0],ops[1]),ops[2])

def sep_effects():
    def equator(phi):return np.array([1,np.exp(1j*phi)])/sqrt(2)
    epos=np.zeros((8,8),complex);eneg=np.zeros_like(epos);effects=[]
    for phi in (0,pi/2,pi,3*pi/2):
        v=np.kron(np.kron(equator(phi),equator(phi)),equator(phi))
        e=2/3*np.outer(v,v.conj());epos+=e;effects.append(e)
        for alpha in permutations((0,2*pi/3,4*pi/3)):
            z=np.kron(np.kron(equator(phi+alpha[0]),equator(phi+alpha[1])),equator(phi+alpha[2]))
            e=2/9*np.outer(z,z.conj());eneg+=e;effects.append(e)
    return epos,eneg,effects

def one_first_X_BC_joint(q):
    d=D(q)
    plus=np.array([1.,1.])/sqrt(2);minus=np.array([1.,-1.])/sqrt(2)
    def block(v):
        K=np.kron(v.conj().reshape(1,2),np.eye(4))
        return K@d@K.conj().T
    val=0.5*sum(sum(abs(eigvalsh(block(v)))) for v in (plus,minus))
    x=exp(-q);b=1-x*x
    closed=b/32*(4+2*x+sqrt(x*x+4*x+20)+sqrt(x*x-4*x+20))
    return val,closed

if __name__=='__main__':
    P=(eye2,np.diag([1.,-1.]),np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]))
    A=np.array([[np.vdot(w,local_effect_on_party(op,0)@qq) for op in P] for qq in (q1,q2)])
    print('Orthogonality local coefficient rows q1,q2; columns I,Z,X,Y:\n',A)
    assert abs(A[0,1])>0.9 and abs(A[1,2])>0.4 and abs(A[1,3])>0.4
    assert np.max(abs(A[:,0]))<1e-12
    for party in range(3):
        K=np.column_stack([(pplus@local_effect_on_party(op,party)@pminus).ravel() for op in P])
        singular=np.linalg.svd(K,compute_uv=False)
        print('Party',party,'singular spectrum(I,Z,X,Y)',singular)
        assert singular[0]>1 and singular[1]>.6 and singular[2]>.6 and singular[3]<1e-12
    epos,eneg,effects=sep_effects()
    assert len(effects)==28
    eps=max(abs(epos+eneg-eye).ravel())
    err=max(abs(epos-pplus-pzero/3).ravel())
    assert max(eps,err)<2e-14
    print('SEP28 completeness error',eps,'spectral effect error',err)
    for q in (.05,1/3,.7,1.4):
        d=D(q)
        h=.5*sum(abs(eigvalsh(d)))
        v=abs(np.trace(epos@d))
        first,closed=one_first_X_BC_joint(q)
        assert abs(h-(1-exp(-2*q))/2)<1e-13
        assert abs(v-h)<1e-13 and abs(first-closed)<1e-13
        print('q',q,'Helstrom',h,'SEP28',v,'A-X-then-BC-JOINT',first,'analytic',closed)
