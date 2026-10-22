"""INT8 ROT008: source-local Fourier TT vs central-difference divergence mismatch.
Synthetic NumPy-only reproduction. NOT a v0.3.1 DTC original runtime replay.
"""
import numpy as np

def ptt_like_inspected_helper(H, dx):
    n=H.shape[0]
    F=np.fft.fftn(H,axes=(0,1,2))
    k1,k2,k3=np.meshgrid(*([np.fft.fftfreq(n,d=dx)]*3),indexing="ij")
    k=np.stack((k1,k2,k3),axis=-1)
    k_sq=np.sum(k*k,axis=-1)
    denom=np.where(k_sq==0,1.,k_sq)
    P=np.eye(3)[None,None,None,:,:]-np.einsum("...i,...j->...ij",k,k)/denom[...,None,None]
    TT=P@F@P-0.5*P*np.einsum("...ij,...ij->...",P,F)[...,None,None]
    at_zero=k_sq==0
    TT[at_zero]=F[at_zero]-np.trace(F[at_zero],axis1=-2,axis2=-1)[...,None,None]*np.eye(3)/3
    X=np.fft.ifftn(TT,axes=(0,1,2)).real
    return (X+np.swapaxes(X,-1,-2))/2

def diff(x,axis,dx,order):
    if order==2:
        return (np.roll(x,-1,axis)-np.roll(x,1,axis))/(2*dx)
    if order==4:
        return (-np.roll(x,-2,axis)+8*np.roll(x,-1,axis)
                -8*np.roll(x,1,axis)+np.roll(x,2,axis))/(12*dx)
    raise ValueError("order 2 or 4")

def check(n,p,q,order):
    dx=2*np.pi/n
    u=np.array([q,-p,0.],dtype=float);u/=np.linalg.norm(u)
    v=np.array([0.,0.,1.])
    H0=np.outer(u,u)-np.outer(v,v)
    t=np.arange(n)
    x,y,z=np.meshgrid(t,t,t,indexing="ij")
    H=np.cos(2*np.pi*(p*x+q*y)/n)[...,None,None]*H0
    TT=ptt_like_inspected_helper(H,dx)
    err=np.linalg.norm(TT-H)/np.linalg.norm(H)
    div=np.zeros((n,n,n,3))
    for i in range(3):
        for j in range(3):
            div[...,j]+=diff(TT[...,i,j],i,dx,order)
    rms=np.sqrt(np.mean(np.sum(div*div,axis=-1)))
    angles=2*np.pi*np.array([p,q])/n
    symbol=(np.sin(angles)/dx if order==2 else
            (8*np.sin(angles)-np.sin(2*angles))/(6*dx))
    dh=np.array([symbol[0],symbol[1],0.])
    predicted=np.linalg.norm(dh@H0)/np.sqrt(2)
    rel=np.linalg.norm(dh@H0)/np.linalg.norm(dh)
    assert np.linalg.norm(np.array([p,q,0.])@H0)<1e-13
    assert err<1e-12
    assert abs(rms-predicted)<1e-10
    assert rms>0
    return err,rms,predicted,rel

if __name__=="__main__":
    for n,p,q in ((31,1,2),(41,1,2),(31,7,10),(41,9,13)):
        for order in (2,4):
            err,rms,pred,rel=check(n,p,q,order)
            print(f"N={n}, wave=({p},{q},0), stencil={order}, TTerror={err:.3e}, D_h_RMS={rms:.10f}, analytic={pred:.10f}, rel_symbol={rel:.7f}")
    print("PASS: Fourier-TT projector does not enforce central-difference transversality.")
