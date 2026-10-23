#!/usr/bin/env python3
"""PRF11 R25. Sharp Sobolev threshold for TT/source-centered collocation consistency.

Requires numpy; for --native optional exact retained DTC helper alongside this file.
Original helper expected sha256: 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801.
NO physical J3/K or original production-runtime inference.
"""
import argparse
import hashlib
import importlib.util
import math
from pathlib import Path
import numpy as np

E = np.eye(3)
ex, ey, ez = E.T
v = np.array([-1.,0.,2.])/math.sqrt(5.)
H = (np.outer(v,v)-np.outer(ey,ey))/math.sqrt(2.)
S = np.outer(ex,H@ez)+np.outer(H@ez,ex)


def ptt(t, k):
    k=np.asarray(k,float)
    kn2=float(k@k)
    if kn2==0:
        return t-E*np.trace(t)/3.
    U=E-np.outer(k,k)/kn2
    return U@t@U-.5*U*np.trace(U@t)


def folded_l2_mode(N,alpha=0.):
    assert (N-1)%4==0 and N>=9
    m=(N-1)//4; K=2*m; dx=2*math.pi/N
    k=np.array([K,0,m]); n=np.array([-K,0,m])
    assert np.linalg.norm(ptt(H,k)-H)<3e-14
    st=np.sin(m*dx)/dx*H+np.sin(dx)/dx*S
    filt=1-4*alpha*(np.sin(K*dx/2)**2+np.sin(m*dx/2)**2)
    coef=(.02/math.sqrt(2))*filt*(ptt(st,n)-st)
    # +n and -n Fourier coefficients, input sqrt(2) cos(kx) H
    output=math.sqrt(2)*np.linalg.norm(coef)
    return dict(N=N,m=m,k_norm=math.sqrt(K*K+m*m),L2=output,coef=coef,alpha=alpha)


def fixed_lowband_l2_error(N):
    """Source C2 no-fold finite-mode central-vs-spectral, k=(2,0,2)."""
    assert N>=9 and N%2==1
    h=2*math.pi/N
    # Uses a different exact normalized TT polarization from PRF11 R24
    u=np.array([-1.,0.,1.])/math.sqrt(2)
    G=(np.outer(u,u)-np.outer(ey,ey))/math.sqrt(2)
    S0=np.outer(ex,G@ez)+np.outer(G@ez,ex)
    n=(3,0,2)
    eG=ptt(G,n)-G
    eS=ptt(S0,n)-S0
    return .02*np.linalg.norm((np.sin(2*h)/h-2)*eG+(np.sin(h)/h-1)*eS)


def run_numeric():
    lim_per_N=.02*(4*math.sqrt(21)/25)/(2*math.pi)
    lim_s1=lim_per_N*4/math.sqrt(5)
    assert abs(lim_per_N-.002333886636624)<2e-13
    print('fold limiting L2/N',lim_per_N,'H1-normalized limiting lower',lim_s1)
    print('N folded_L2 folded_H1 folded_H2 folded_H3 folded_L2/N')
    for N in (9,17,41,81,161,401,801,1601):
        z=folded_l2_mode(N)
        L=z['L2']; k=z['k_norm']
        vals=[L/(1+k*k)**(s/2) for s in (0,1,2,3)]
        print(N,*[f'{x:.10g}' for x in vals],f'{L/N:.10g}')
        assert L>=0
    print('fixed input (k=(2,0,2)) lower/h²; exact symbolic limit sqrt(727)/7800')
    target=math.sqrt(727)/7800
    for N in (17,33,41,81,161,321,641):
        d=fixed_lowband_l2_error(N); ratio=d/(2*math.pi/N)**2
        print('N',N,'ratio',ratio)
        assert abs(ratio-target)<.04
    assert abs(fixed_lowband_l2_error(641)/(2*math.pi/641)**2-target)<5e-7
    print('ANALYTICAL_FOURIER_SCALING_AND_SHARP_FIXED_MODE_PASS')


def native_check(path):
    b=Path(path).read_bytes()
    sha=hashlib.sha256(b).hexdigest()
    assert sha=='23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801',sha
    spec=importlib.util.spec_from_file_location('retained_DTC_helper_r25',path)
    helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
    for N in (9,17,41):
        z=folded_l2_mode(N);m=z['m'];K=2*m;dx=2*math.pi/N
        x=np.arange(N)*dx;X,Z=np.meshgrid(x,x,indexing='ij')
        wave=math.sqrt(2)*np.cos(K*X+m*Z)
        F=np.broadcast_to(wave[:,None,:,None,None]*H[None,None,None,:,:],(N,N,N,3,3)).copy()
        C=np.zeros((N,N,N,3));C[...,2]=.04*np.sin(x)[:,None,None];C[...,0]=.04*np.cos(x)[None,None,:]
        PF=helper.apply_P_TT(F,dx)
        discrete=helper.apply_P_TT(helper.apply_T(C,F,'Identity',dx,2,0.),dx)-helper.apply_T(C,PF,'Identity',dx,2,0.)
        idx=((-K)%N,0,m%N)
        num=np.zeros((3,3),complex)
        for a in range(3):
            for b in range(3):
                num[a,b]=np.fft.fftn(discrete[...,a,b])[idx]/N**3
        err=np.linalg.norm(num-z['coef'])/np.linalg.norm(z['coef'])
        tt_err=np.linalg.norm(PF-F)/np.linalg.norm(F)
        assert err<5e-12 and tt_err<5e-12,(N,err,tt_err)
        print('NATIVE_SOURCE_HELPER_PASS',N,err,tt_err)
    print('NATIVE_DTC_HELPER_SHA256_AND_SELECTED_FOLDED_MODE_PASS')


def main():
    p=argparse.ArgumentParser();p.add_argument('--native',type=str,default='')
    args=p.parse_args();run_numeric()
    if args.native:native_check(args.native)
    print('PRF11_R25_ALL_AVAILABLE_CHECKS_PASS')


if __name__=='__main__':main()
