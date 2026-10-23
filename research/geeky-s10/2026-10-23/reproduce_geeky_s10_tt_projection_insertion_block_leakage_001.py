import math
import numpy as np

def der(f,axis,dx):
    return (np.roll(f,-1,axis=axis)-np.roll(f,1,axis=axis))/(2*dx)

def E(h,a):
    return h+a*sum(np.roll(h,1,axis=i)+np.roll(h,-1,axis=i)-2*h for i in range(3))

def lie(C,h,dx):
    DC=np.stack([np.stack([der(C[...,k],i,dx) for k in range(3)],-1) for i in range(3)],-2)
    return (sum(C[...,k,None,None]*der(h,k,dx) for k in range(3))
            +np.einsum('...ik,...kj->...ij',DC,h)
            +np.einsum('...ik,...jk->...ij',h,DC))

def Ptt(h,dx):
    N=h.shape[0]
    k=2*np.pi*np.fft.fftfreq(N,d=dx)
    K=np.stack(np.meshgrid(k,k,k,indexing='ij'),-1)
    s=np.sum(K*K,-1)
    inv=np.divide(1.,s,out=np.zeros_like(s),where=s>1e-30)
    P=np.eye(3)-np.einsum('...i,...j,...->...ij',K,K,inv)
    H=np.fft.fftn(h,axes=(0,1,2))
    Y=np.einsum('...ia,...ab,...bj->...ij',P,H,P)
    Y-=.5*P*np.einsum('...ij,...ij->...',P,H)[...,None,None]
    Y[0,0,0]=H[0,0,0]-np.trace(H[0,0,0])/3*np.eye(3)
    y=np.fft.ifftn(Y,axes=(0,1,2)).real
    return .5*(y+np.swapaxes(y,-1,-2))

def rms(A):
    return float(np.sqrt(np.mean(np.sum(A*A,axis=(-2,-1))/6)))

def run(N,alpha=.05):
    dx=2*np.pi/N
    X,Y,Z=np.meshgrid(np.arange(N)*dx,np.arange(N)*dx,np.arange(N)*dx,indexing='ij')
    C1=np.zeros((N,N,N,3)); C2=np.zeros_like(C1)
    C1[...,0]=.05*np.sin(X); C1[...,1]=.05*np.cos(Y)
    C2[...,0]=.04*np.cos(Z); C2[...,2]=.04*np.sin(X)

    href=np.zeros((N,N,N,3,3))
    f=.1*np.sin(X)*np.cos(Y)
    for i in range(3): href[...,i,i]=f

    h=np.zeros_like(href)
    h[...,0,1]=.1*np.sin(X+Z)*np.cos(Y); h[...,1,0]=h[...,0,1]
    h[...,0,2]=.075*np.cos(2*Y-Z); h[...,2,0]=h[...,0,2]
    h[...,1,2]=.05*np.sin(2*X+Y); h[...,2,1]=h[...,1,2]
    h=Ptt(h,dx)
    h*=rms(href)/rms(h)

    L=lambda C,u: lie(C,E(u,alpha),dx)
    L1=L(C1,h); L2=L(C2,h)
    KB=Ptt(L(C1,L2)-L(C2,L1),dx)

    KA=Ptt(L(C1,Ptt(L2,dx)),dx)-Ptt(L(C2,Ptt(L1,dx)),dx)
    Delta=KA-KB
    ratio=rms(Delta)/rms(h)
    lower=math.sqrt(ratio/2)
    return N,rms(h),rms(Delta),ratio,lower

for N in (9,17,31):
    row=run(N)
    print("N=%d h=%.15e Delta=%.15e ratio=%.15e lower=%.15e"%row)

print("PASS")
