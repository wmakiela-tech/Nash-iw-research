"""XH-S4/019: independently compare central and FFT spectral derivatives in frozen DTC0a.
Requires adjacent xh_s4_dtc0a_projection_leakage_018_selfcontained.py.
Computes no physical observables or continuum invariants.
"""
import json
import numpy as np
from pathlib import Path
import importlib.util
S=importlib.util.spec_from_file_location('s18',Path(__file__).with_name('xh_s4_dtc0a_projection_leakage_018_selfcontained.py'))
m=importlib.util.module_from_spec(S);S.loader.exec_module(m)

def derivatives(h,dx,kind):
    if kind=='central':return [m.derivative(h,i,dx) for i in range(3)]
    N=h.shape[0];k=2*np.pi*np.fft.fftfreq(N,d=dx)
    F=np.fft.fftn(h,axes=(0,1,2))
    out=[]
    for ax in range(3):
        shape=[1]*h.ndim;shape[ax]=N
        out.append(np.fft.ifftn(1j*k.reshape(shape)*F,axes=(0,1,2)).real)
    return out

def lie(C,h,dx,kind):
    dH=derivatives(h,dx,kind);dC=derivatives(C,dx,kind)
    J=np.stack(dC,axis=-2)
    return sum(C[...,i,None,None]*dH[i] for i in range(3))+np.einsum('...ik,...kj->...ij',J,h,optimize=True)+np.einsum('...ik,...jk->...ij',h,J,optimize=True)

def bracket(A,B,dx,kind):
    a=derivatives(A,dx,kind);b=derivatives(B,dx,kind)
    return sum(A[...,i,None]*b[i]-B[...,i,None]*a[i] for i in range(3))

def one(N,alpha,kind):
    dx=2*np.pi/N;s=slice(3,N-3);C1,C2,h,X,Y,Z=m.smooth(N)
    P=lambda g:m.tt(g,dx)
    L=lambda C,g:lie(C,m.E_lin(g,dx,alpha),dx,kind)
    b=bracket(C1,C2,dx,kind)
    a1=L(C1,h);a2=L(C2,h)
    kc=L(C1,a2)-L(C2,a1)-L(b,h)
    ka=P(L(C1,P(a2)))-P(L(C2,P(a1)))-P(L(b,h))
    hTT=np.zeros_like(h)
    hTT[...,0,1]=.1*np.sin(X+Z)*np.cos(Y);hTT[...,1,0]=hTT[...,0,1]
    hTT[...,0,2]=.075*np.cos(2*Y-Z);hTT[...,2,0]=hTT[...,0,2]
    hTT[...,1,2]=.05*np.sin(2*X+Y);hTT[...,2,1]=hTT[...,1,2]
    hTT=P(hTT);hTT*=m.rms(h)/m.rms(hTT)
    t1=L(C1,hTT);t2=L(C2,hTT)
    tkc=L(C1,t2)-L(C2,t1)-L(b,hTT)
    tka=P(L(C1,P(t2)))-P(L(C2,P(t1)))-P(L(b,hTT))
    return dict(N=N,alpha=alpha,derivative=kind,KC_mask=m.rms(kc,s),KB_mask=m.rms(P(kc),s),KA_mask=m.rms(ka,s),TT_KC_mask=m.rms(tkc,s),TT_KA_mask=m.rms(tka,s))

if __name__=='__main__':
    data=[one(n,a,k) for n,a,k in [(17,0,'central'),(17,0,'spectral'),(31,0,'central'),(31,0,'spectral'),(31,.05,'central'),(31,.05,'spectral'),(31,.2,'spectral')]]
    Path(__file__).with_name('xh_s4_dtc0a_derivative_crosscheck_019_results.json').write_text(json.dumps(data,indent=2))
    for row in data:print(row)
