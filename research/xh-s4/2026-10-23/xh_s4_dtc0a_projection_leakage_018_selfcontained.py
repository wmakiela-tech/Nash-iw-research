"""XH-S4/018: standalone finite periodic operator check, NumPy only.
Reconstructed definitions from user-provided DTC0a verification source SHA256
23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801.
Finite-grid source-host test; NOT a continuum or physical theorem.
"""
import json
import sys
import numpy as np

def der(f, axis, dx):
    return (np.roll(f,-1,axis=axis)-np.roll(f,1,axis=axis))/(2*dx)

def bracket(A,B,dx):
    return np.stack([sum(A[...,m]*der(B[...,k],m,dx)-B[...,m]*der(A[...,k],m,dx)
                         for m in range(3)) for k in range(3)],axis=-1)

def E(h,alpha):
    return h+alpha*sum(np.roll(h,1,axis=a)+np.roll(h,-1,axis=a)-2*h for a in range(3))

def lie(C,h,dx):
    Dh=np.stack([np.stack([der(C[...,k],i,dx) for k in range(3)],axis=-1)
                 for i in range(3)],axis=-2)
    return (sum(C[...,k,None,None]*der(h,k,dx) for k in range(3))
        +np.einsum('...ik,...kj->...ij',Dh,h,optimize=True)
        +np.einsum('...ik,...jk->...ij',h,Dh,optimize=True))

def Ptt(h,dx,mode='k'):
    N=h.shape[0]
    k=2*np.pi*np.fft.fftfreq(N,d=dx)
    if mode=='sin':k=np.sin(k*dx)/dx
    K=np.stack(np.meshgrid(k,k,k,indexing='ij'),axis=-1)
    sq=np.sum(K*K,axis=-1)
    inv=np.divide(1.,sq,out=np.zeros_like(sq),where=sq>1e-30)
    P=np.eye(3)-np.einsum('...i,...j,...->...ij',K,K,inv)
    H=np.fft.fftn(h,axes=(0,1,2))
    Y=np.einsum('...ia,...ab,...bj->...ij',P,H,P,optimize=True)
    Y-=.5*P*np.einsum('...ij,...ij->...',P,H)[...,None,None]
    Y[0,0,0]=H[0,0,0]-np.trace(H[0,0,0])/3*np.eye(3)
    y=np.fft.ifftn(Y,axes=(0,1,2)).real
    return .5*(y+np.swapaxes(y,-1,-2))

def rms(A,s=None):
    if s is not None:A=A[s,s,s]
    return float(np.sqrt(np.mean(np.sum(A*A,axis=(-2,-1))/6)))

def one(N,alpha):
    dx=2*np.pi/N; s=slice(3,N-3)
    X,Y,Z=np.meshgrid(np.arange(N)*dx,np.arange(N)*dx,np.arange(N)*dx,indexing='ij')
    C1=np.zeros((N,N,N,3));C2=C1.copy()
    C1[...,0]=.05*np.sin(X);C1[...,1]=.05*np.cos(Y)
    C2[...,0]=.04*np.cos(Z);C2[...,2]=.04*np.sin(X)
    h=np.zeros((N,N,N,3,3))
    f=.1*np.sin(X)*np.cos(Y)
    for i in range(3):h[...,i,i]=f
    Q=lambda u:u-Ptt(u,dx)
    L=lambda C,u:lie(C,E(u,alpha),dx)
    B=bracket(C1,C2,dx)
    L1=L(C1,h);L2=L(C2,h)
    Kc=L(C1,L2)-L(C2,L1)-L(B,h)
    Kb=Ptt(Kc,dx)
    Ka=Ptt(L(C1,Ptt(L2,dx)),dx)-Ptt(L(C2,Ptt(L1,dx)),dx)-Ptt(L(B,h),dx)
    D=Ptt(L(C2,Q(L1)),dx)-Ptt(L(C1,Q(L2)),dx)
    test=np.zeros_like(h)
    test[...,0,1]=.2*np.sin(2*X+Z);test[...,1,0]=test[...,0,1]
    test[...,0,0]=.1*np.cos(X+Y)
    test[...,2,2]=.07*np.sin(2*Z-X)
    constant=np.zeros_like(C1);constant[...,0]=.05;constant[...,1]=-.03
    hTT=np.zeros_like(h)
    hTT[...,0,1]=.1*np.sin(X+Z)*np.cos(Y);hTT[...,1,0]=hTT[...,0,1]
    hTT[...,0,2]=.075*np.cos(2*Y-Z);hTT[...,2,0]=hTT[...,0,2]
    hTT[...,1,2]=.05*np.sin(2*X+Y);hTT[...,2,1]=hTT[...,1,2]
    hTT=Ptt(hTT,dx);hTT*=rms(h)/rms(hTT)
    def KA(u,mode='k'):
        p=lambda t:Ptt(t,dx,mode)
        return p(L(C1,p(L(C2,u))))-p(L(C2,p(L(C1,u))))-p(L(B,u))
    result=dict(N=N,alpha=alpha,
        original_h_global_RMS=rms(h),
        original_h_TT_global_RMS=rms(Ptt(h,dx)),
        alternative_hTT_global_RMS=rms(hTT),
        K_C_mask_RMS=rms(Kc,s),K_B_mask_RMS=rms(Kb,s),
        K_A_mask_RMS=rms(Ka,s),KA_minus_KB_mask_RMS=rms(Ka-Kb,s),
        algebra_identity_error_RMS=rms(Ka-Kb-D,s),
        P_E_commutator_probe_RMS=rms(Ptt(E(test,alpha),dx)-E(Ptt(test,dx),alpha)),
        P_L_constant_probe_RMS=rms(Ptt(L(constant,test),dx)-L(constant,Ptt(test,dx))),
        P_L_variable_probe_RMS=rms(Ptt(L(C1,test),dx)-L(C1,Ptt(test,dx))),
        K_A_discrete_k_trace_input_mask_RMS=rms(KA(h,'sin'),s),
        K_A_nonzero_TT_input_mask_RMS=rms(KA(hTT),s),
        K_A_nonzero_TT_discrete_k_mask_RMS=rms(KA(hTT,'sin'),s))
    assert result['original_h_TT_global_RMS']<1e-12
    assert result['algebra_identity_error_RMS']<1e-12
    assert result['P_E_commutator_probe_RMS']<1e-12
    assert result['P_L_constant_probe_RMS']<1e-12
    return result

if __name__=='__main__':
    runs=[one(n,a) for n in (9,17,31) for a in (0.,.05,.2)]
    if len(sys.argv)>1:
        with open(sys.argv[1],'w') as fp:json.dump(runs,fp,indent=2)
    for r in runs:
        print(r['N'],r['alpha'],r['K_A_mask_RMS'],r['K_B_mask_RMS'],
              r['algebra_identity_error_RMS'])
