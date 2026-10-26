#!/usr/bin/env python3
"""PRF12 R07 independent 8x8 checks for exact n=3 equal-grid Cauchy-vs-Levy pair.
Not a numerical simulation of asymptotic LOCC or a quantitative gap bound.
The path necessity used in the analytic proof is Cohen, PRA 105 022207 (2022).
"""
import numpy as np
from itertools import product
from math import exp,sqrt

bits=np.array(list(product((0,1),repeat=3)))
I=np.eye(8,dtype=complex)
w=(I[1]+I[2]+I[4])/sqrt(3)
wb=(I[3]+I[5]+I[6])/sqrt(3)
P=np.outer(w,w.conj())+np.outer(wb,wb.conj())
PK=np.zeros((8,8),complex);PK[0,0]=PK[7,7]=1.
Q=I-P-PK

def source_difference(q):
    diff=bits[:,None,:]-bits[None,:,:]
    return (np.exp(-q*np.abs(diff.sum(axis=-1)))
           -np.exp(-q*np.abs(diff).sum(axis=-1)))/8

def kernel_contraction(a,b,z=0):
    K=np.zeros((8,8),complex)
    K[0,0]=a;K[7,7]=b;K[0,7]=z;K[7,0]=np.conj(z)
    k=K[np.ix_([0,7],[0,7])]
    assert np.linalg.eigvalsh(k).min()>=-1e-12
    assert np.linalg.eigvalsh(np.eye(2)-k).min()>=-1e-12
    return K

def realignment_first_vs_rest(F):
    return F.reshape(2,4,2,4).transpose(0,2,1,3).reshape(4,16)

def main():
    for q in (.05,1/3,.7,1.4):
        D=source_difference(q)
        x=exp(-q);b=1-x*x
        predicted=np.sort(np.array([0.,0.,b*(2+x)/8,b*(2-x)/8,
           -b*(1-x)/8,-b*(1-x)/8,-b*(1+x)/8,-b*(1+x)/8]))
        eig=np.linalg.eigvalsh(D)
        assert np.max(abs(eig-predicted))<2e-14
        assert np.linalg.norm(P@D@Q)<1e-14
        assert abs(abs(eig).sum()/2-b/2)<1e-14
        print('q',q,'Helstrom',(1-exp(-2*q))/2,
              'spectral_error',np.max(abs(eig-predicted)))
    for name,K in (('K0',kernel_contraction(0,0)),
                   ('Kmid',kernel_contraction(.5,.5)),
                   ('Kcomplex',kernel_contraction(.25,.75,.2+.1j)),
                   ('Kfull',kernel_contraction(1,1))):
        Ep=P+K
        Em=I-Ep
        assert np.linalg.eigvalsh(Ep).min()>-1e-12
        assert np.linalg.eigvalsh(Em).min()>-1e-12
        assert np.linalg.norm(P@Ep-P)<1e-12
        assert np.linalg.norm(Q@Ep)<1e-12
        for u,v in ((.8,.5),(.99,.98),(.8,.8)):
            F=u*Ep+v*Em
            assert np.linalg.eigvalsh(F).min()>0
            assert abs(F[0,1])<1e-12
            assert abs(F[1,2]-(u-v)/3)<1e-12
            singular=np.linalg.svd(realignment_first_vs_rest(F),
                                   compute_uv=False)
            if u!=v: assert singular[1]>1e-5
            else: assert singular[1]<1e-12
            print('kernel',name,'u',u,'v',v,'nearest_onebit',F[0,1],
                  'two_bit',F[1,2],'second_product_Schmidt',singular[1])
    q=1/3
    x=exp(-q);b=1-x*x
    hel=b/2;tvX=b*(6+9*x)/32
    print('q=1/3 Helstrom',hel,'Xfull_LOCC_lower',tvX,
          'proven_delta_interval:(0,',hel-tvX,']')
if __name__=='__main__':main()
