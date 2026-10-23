#!/usr/bin/env python3
"""PRF11 R24 independent mesoscopic spectral/scheme comparision.
Source carrier: retained DTC verification helper SHA256 23b0ec... (NOT historical production runner).
Use: python prf11_r24_mesoscopic_dealiasing.py /mnt/data/deepseek_python_20260627_a87249.py
"""
import sys, math, hashlib, importlib.util, json
import numpy as np
EXPECTED='23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801'
E=np.eye(3);ex,ey,ez=E.T
v=(-ex+ez)/np.sqrt(2); H=(np.outer(v,v)-np.outer(ey,ey))/np.sqrt(2)
S=np.outer(ex,H@ez)+np.outer(H@ez,ex)
def P(t,k):
    k=np.asarray(k,float)
    if np.linalg.norm(k)==0: return t-np.trace(t)/3*E
    U=E-np.outer(k,k)/(k@k)
    return U@t@U-0.5*U*np.trace(U@t)

def analytic(N,m):
    h=2*math.pi/N; k=(m,0,m); n=(m+1,0,m)
    assert m+1<=(N-1)//2
    assert np.linalg.norm(P(H,k)-H)<2e-14
    d=P(H,n)-H
    e=P(S,n)-S
    cd=math.sin(m*h)/h; sq=math.sin(h)/h
    grid_coeff=(.02/np.sqrt(2))*(cd*d+sq*e)
    cont_coeff=(.02/np.sqrt(2))*(m*d+e)
    diff=grid_coeff-cont_coeff
    # mirror + conj (-n) -> physical L2 Fourier pair norm
    return dict(N=N,m=m,h=h,grid_mode_norm=float(np.sqrt(2)*np.linalg.norm(grid_coeff)),
                continuum_mode_norm=float(np.sqrt(2)*np.linalg.norm(cont_coeff)),
                mode_difference_norm=float(np.sqrt(2)*np.linalg.norm(diff)),
                error_over_h2=float(np.sqrt(2)*np.linalg.norm(diff)/h**2),
                _grid=grid_coeff,_cont=cont_coeff,_difference=diff)

def D_spectral(a,axis):
    n=a.shape[axis]
    k=np.fft.fftfreq(n)*n
    dims=[1]*a.ndim;dims[axis]=n
    return np.fft.ifft(np.fft.fft(a,axis=axis)*(1j*k.reshape(dims)),axis=axis).real

def lie_spectral(C,F):
    out=np.zeros_like(F)
    for b in range(3):
        out+=C[...,b,None,None]*D_spectral(F,b)
        for a in range(3):
            val=D_spectral(C[...,b],a)
            out[...,a,:]+=val[...,None]*F[...,b,:]
            out[...,:,a]+=val[...,None]*F[...,:,b]
    return (out+np.swapaxes(out,-1,-2))/2

def check_native(native,N,m):
    z=analytic(N,m)
    x=np.arange(N)*2*math.pi/N; X,Z=np.meshgrid(x,x,indexing='ij')
    wave=np.sqrt(2)*np.cos(m*X+m*Z)
    F=np.broadcast_to(wave[:,None,:,None,None]*H[None,None,None,:,:],(N,N,N,3,3)).copy()
    C=np.zeros((N,N,N,3))
    C[...,2]=.04*np.sin(x)[:,None,None]
    C[...,0]=.04*np.cos(x)[None,None,:]
    dx=2*math.pi/N
    PF=native.apply_P_TT(F,dx)
    discrete=native.apply_P_TT(native.apply_T(C,F,'Identity',dx,2,0.),dx)-native.apply_T(C,PF,'Identity',dx,2,0.)
    continuum=native.apply_P_TT(lie_spectral(C,F),dx)-lie_spectral(C,PF)
    diff=discrete-continuum
    idx=((m+1)%N,0,m%N)
    def coeff(t): return np.array([[np.fft.fftn(t[...,i,j])[idx]/N**3 for j in range(3)] for i in range(3)])
    a,b,c=coeff(discrete),coeff(continuum),coeff(diff)
    erra=float(np.linalg.norm(a-z['_grid'])/np.linalg.norm(z['_grid']))
    errb=float(np.linalg.norm(b-z['_cont'])/np.linalg.norm(z['_cont']))
    errc=float(np.linalg.norm(c-z['_difference'])/np.linalg.norm(z['_difference']))
    tterr=float(np.linalg.norm(PF-F)/np.linalg.norm(F))
    fullnorm=float(np.linalg.norm(diff)/N**1.5)
    assert erra<2e-11 and errb<2e-11 and errc<3e-10 and tterr<2e-12,(N,m,erra,errb,errc,tterr)
    assert fullnorm>=z['mode_difference_norm']-2e-11
    return dict(N=N,m=m,grid_coef_rel_error=erra,continuum_coef_rel_error=errb,
                difference_coef_rel_error=errc,TT_input_rel_error=tterr,
                selected_mode_difference=z['mode_difference_norm'],total_difference=fullnorm)

def main():
    limit=(.01)*(1-2*math.sqrt(2)/math.pi)
    assert abs(limit-.0009968368384289383)<1e-14
    meso=[analytic(8*m+1,m) for m in (1,2,4,8,16,32,64,128,256,512)]
    fixed=[analytic(N,2) for N in (17,31,41,81,161,321,641)]
    print('meso N,m,exact selected difference:',[(z['N'],z['m'],z['mode_difference_norm']) for z in meso])
    print('limit:',limit,'last',meso[-1]['mode_difference_norm'])
    print('fixed m=2, error/h^2:',[(z['N'],z['error_over_h2']) for z in fixed])
    assert .00099<meso[-1]['mode_difference_norm']<.001
    assert abs(fixed[-1]['error_over_h2']-.0034567)<5e-7
    if len(sys.argv)>1:
        fp=sys.argv[1]
        sha=hashlib.sha256(open(fp,'rb').read()).hexdigest(); assert sha==EXPECTED,(sha,EXPECTED)
        spec=importlib.util.spec_from_file_location('dtc_helper_prf24',fp)
        mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
        tests=[check_native(mod,N,m) for N,m in ((17,2),(33,4),(41,2))]
        print('NATIVE_CHECKS',json.dumps(tests,indent=2))
    print('PRF11_R24_NUMERIC_CONTROL_PASS; NO_DTC_PHYSICS')

if __name__=='__main__':main()