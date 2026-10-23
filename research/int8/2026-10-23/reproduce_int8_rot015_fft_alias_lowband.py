"""INT8 ROT015. Standalone NumPy spectral-alias and frozen source-field no-alias tests."""
import numpy as np

def d(v,axis,N):
 k=np.fft.fftfreq(N,d=1/N);shape=[1]*v.ndim;shape[axis]=N
 return np.fft.ifftn(np.fft.fftn(v,axes=(0,1,2))*(1j*k.reshape(shape)),axes=(0,1,2)).real

def lie(C,H,N):
 out=np.zeros_like(H)
 for i in range(3):
  for j in range(3):
   for m in range(3):
    out[...,i,j]+=C[...,m]*d(H[...,i,j],m,N)
    out[...,i,j]+=H[...,m,j]*d(C[...,m],i,N)
    out[...,i,j]+=H[...,i,m]*d(C[...,m],j,N)
 return out

def bracket(C,D,N):
 out=np.zeros_like(C)
 for j in range(3):
  for m in range(3):
   out[...,j]+=C[...,m]*d(D[...,j],m,N)-D[...,m]*d(C[...,j],m,N)
 return out

for N in (31,41,47,61):
 x=np.arange(N)*2*np.pi/N
 diff=lambda f:d(f[:,None,None],0,N)[:,0,0]
 f=np.sin(10*x);g=np.cos(13*x)
 kc=2*(f*diff(diff(g))-g*diff(diff(f))-diff(f*diff(g)-g*diff(f)))
 expected=3*N*np.sin((N-23)*x) if (N-1)//2<23 else np.zeros(N)
 assert np.max(np.abs(kc-expected))<1e-10
 print("high-band",N,np.sqrt(np.mean(kc**2)))

for N in (9,17,31):
 x=np.arange(N)*2*np.pi/N
 X,Y,Z=np.meshgrid(x,x,x,indexing="ij")
 C=np.zeros((N,N,N,3));D=C.copy();H=np.zeros((N,N,N,3,3))
 C[...,0]=.05*np.sin(X);C[...,1]=.05*np.cos(Y)
 D[...,0]=.04*np.cos(Z);D[...,2]=.04*np.sin(X)
 for j in range(3):H[...,j,j]=.1*np.sin(X)*np.cos(Y)
 A=lie(C,lie(D,H,N),N);B=lie(D,lie(C,H,N),N);E=lie(bracket(C,D,N),H,N)
 k=np.fft.fftfreq(N,d=1/N);a,b,c=np.meshgrid(k,k,k,indexing="ij")
 outside=(abs(a)>3)|(abs(b)>2)|(abs(c)>1)
 tail=max(np.max(abs(np.fft.fftn(v,axes=(0,1,2))[outside]))/N**3 for v in (A,B,E))
 resid=np.max(abs(A-B-E))
 assert resid<1e-12 and tail<1e-12
 print("source low-band",N,resid,tail)
print("ALL_PASS; not historical DTC0a production runtime")
