#!/usr/bin/env python3
"""PRF11 R23: TT projection vs Lie derivatives, positive continuum/negative grid comparison.

Run: python reproduce_prf11_r23_tt_commutator_host_and_alias.py path/to/deepseek_python_20260627_a87249.py
Optional source path: omit it for analytical Fourier source-compliant test only.
The verified retained DTC helper, when supplied, must have SHA256 below. Its
native TT, Lie, centered derivative and E_alpha are used on entire REAL grids.
This is NOT historical production dtc0a_runtime_v0_3_1.py.
Requires numpy.
"""
import hashlib
import importlib.util
import math
import sys
import numpy as np

VERIFIER_SHA = "23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801"
E=np.eye(3)
ex,ey,ez=E.T

def ptt(H,k):
    k=np.asarray(k,float)
    if np.dot(k,k)==0:
        return H-np.trace(H)/3*E
    U=E-np.outer(k,k)/np.dot(k,k)
    return U@H@U-.5*U*np.sum(U*H)

def h_probe():
    v=np.array([-1.,0.,2.])/math.sqrt(5)
    return (np.outer(v,v)-np.outer(ey,ey))/math.sqrt(2)

def exact_mode(M,alpha=0.):
    N=4*M+1; K=2*M; dx=2*math.pi/N
    k=np.array([K,0,M]); n=np.array([-K,0,M])
    H=h_probe()
    assert np.linalg.norm(ptt(H,k)-H)<1e-13
    S=np.outer(ex,H@ez)+np.outer(H@ez,ex)
    dk=math.sin(M*dx)/dx
    dq=math.sin(dx)/dx
    A=ptt(dk*H+dq*S,n)-(dk*H+dq*S)
    ea=1-4*alpha*(math.sin(K*dx/2)**2+math.sin(M*dx/2)**2)
    # h(x)=sqrt(2) cos(Kx+Mz) H, C_z=0.04 sin(x):
    # selected complex FFT output coefficient at n=(-K,0,M)
    coef=(.02/math.sqrt(2))*ea*A
    norm=math.sqrt(2)*np.linalg.norm(coef)
    Qnorm=np.linalg.norm(H-ptt(H,n))
    assert abs(Qnorm-4*math.sqrt(21)/25)<1e-13
    lower=.02*abs(ea)*max(0,dk*Qnorm-2*dq)
    assert norm+1e-13>=lower
    return dict(N=N,K=K,M=M,alpha=alpha,ealpha=ea,
                exact_mode_L2_norm=norm,lower=lower,coef=coef)

def native_check(native,M,alpha):
    s=exact_mode(M,alpha);N=s["N"];K=s["K"];dx=2*math.pi/N
    x=np.arange(N)*dx; X,Z=np.meshgrid(x,x,indexing="ij")
    wave=math.sqrt(2)*np.cos(K*X+M*Z)
    H=np.broadcast_to(wave[:,None,:,None,None]*h_probe()[None,None,None,:,:],
                      (N,N,N,3,3)).copy()
    C=np.zeros((N,N,N,3))
    # FULL original retained source C2, both components:
    C[...,2]=.04*np.sin(x)[:,None,None]
    C[...,0]=.04*np.cos(x)[None,None,:]
    PH=native.apply_P_TT(H,dx)
    mode="Identity" if alpha==0 else "E_lin"
    c=native.apply_P_TT(native.apply_T(C,H,mode,dx,2,alpha),dx)\
      -native.apply_T(C,PH,mode,dx,2,alpha)
    n=(-K%N,0,M%N)
    actual=np.array([[np.fft.fftn(c[...,i,j])[n]/N**3 for j in range(3)]
                     for i in range(3)])
    relative=np.linalg.norm(actual-s["coef"])/np.linalg.norm(s["coef"])
    inp=np.linalg.norm(PH-H)/np.linalg.norm(H)
    assert relative<1e-11 and inp<1e-11,(N,alpha,relative,inp)
    print("NATIVE",N,alpha,"rel Fourier error",relative,
          "TT input error",inp,"full output norm",np.linalg.norm(c)/N**1.5)

def continuum_symbol_sanity():
    # Fourier algebra block from proof: for each q,k, the fixed-source term
    # is order-zero even when k is arbitrarily large without folding.
    q=np.array([1.,0.,0.])
    for k in ([0,0,0],[1,2,3],[50,20,10],[100,100,0],[-1,0,0]):
        k=np.array(k,float);n=k+q
        for H in (h_probe(),(np.outer(ex,ex)+np.outer(ey,ey))/math.sqrt(2)):
            S=np.outer(ex,H@ez)+np.outer(H@ez,ex)
            Pk=ptt(H,k)
            SPk=np.outer(ex,Pk@ez)+np.outer(Pk@ez,ex)
            out=np.dot(k,ez)*(ptt(H,n)-ptt(H,k))+ptt(S,n)-SPk
            assert np.linalg.norm(out)<=20*np.linalg.norm(H)+1e-13

def main():
    continuum_symbol_sanity()
    print("N alpha exact_mode_L2_norm lower filter_ealpha")
    for M in (1,2,4,10,20,60,120):
        for alpha in ((0,.05,.2) if M in (4,10,60) else (0,)):
            a=exact_mode(M,alpha)
            print(a["N"],alpha,a["exact_mode_L2_norm"],a["lower"],a["ealpha"])
    if len(sys.argv)>1:
        path=sys.argv[1]
        sha=hashlib.sha256(open(path,"rb").read()).hexdigest()
        assert sha==VERIFIER_SHA,(sha,VERIFIER_SHA)
        spec=importlib.util.spec_from_file_location("dtc_verifier_r23",path)
        native=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(native)
        for M in (2,4,10):
            for alpha in ((0,.05,.2) if M in (4,10) else (0,)):
                native_check(native,M,alpha)
        print("SOURCE_HELPER_SHA256_AND_NATIVE_COMPARISON_PASS")
    print("EXACT_FOURIER_ANALYSIS_PASS; NO_J3_K_PHYSICS_OR_BYTE_EXACT_PRODUCTION_RUN")

if __name__=="__main__":
    main()
