"""INT8 ROT016: standalone independent Fourier-TT check of a source-stencil theorem.
Optional direct original helper run: DTC0A_HELPER_PATH=/path/to/deepseek_python_20260627_a87249.py
No historic v0.3.1 executor or NASH physical claim.
"""
import os, importlib.util
import numpy as np

def rms(a):
 return np.sqrt(np.mean(np.sum(a*a,axis=(-2,-1))))

def PTT(H):
 N=H.shape[0]
 F=np.fft.fftn(H,axes=(0,1,2))
 q=np.fft.fftfreq(N,d=1/N)
 k=np.stack(np.meshgrid(q,q,q,indexing='ij'),axis=-1)
 n2=np.sum(k*k,axis=-1)
 inv=np.divide(1.,n2,out=np.zeros_like(n2),where=n2>0)
 P=np.eye(3)-np.einsum('...i,...j,...->...ij',k,k,inv)
 T=np.einsum('...ia,...ab,...bj->...ij',P,F,P)
 T-=.5*P*np.einsum('...ab,...ab->...',P,F)[...,None,None]
 T[n2==0]=F[n2==0]-np.eye(3)*np.trace(F[n2==0],axis1=-2,axis2=-1)[...,None,None]/3
 return np.fft.ifftn(T,axes=(0,1,2)).real

def test(N,alpha,src=None):
 dx=2*np.pi/N;q=(N-1)//2
 z=np.arange(N)*dx
 X,Y,Z=np.meshgrid(z,z,z,indexing='ij')
 H=np.zeros((N,N,N,3,3))
 H[...,0,0]=np.cos(q*Z);H[...,1,1]=-np.cos(q*Z)
 C=np.zeros((N,N,N,3));C[...,0]=np.sin(X)
 sig=np.sin(dx)/dx
 ef=1-4*alpha*np.sin(q*dx/2)**2
 A=np.zeros_like(H);A[...,0,0]=2*sig*ef*np.cos(X)*np.cos(q*Z)
 if src is None:
  PT=PTT
 else:
  PT=lambda a:src.apply_P_TT(a,dx)
  actual=src.lie_derivative_tensor(C,src.apply_E(H,'E_lin',dx,order=2,alpha=alpha),dx,order=2)
  assert np.max(abs(actual-A))<1e-10
 actualnorm=rms(A-PT(A))/rms(H)
 formula=abs(sig*ef)*np.sqrt(1-.5*(q*q/(1+q*q))**2)
 assert abs(actualnorm-formula)<1e-10
 assert rms(PT(H)-H)<1e-10
 return actualnorm,formula

for N in (9,17,31,41):
 for a in (0,.05,.2):
  observed,formula=test(N,a)
  print('N',N,'alpha',a,'obs',f'{observed:.12f}','formula',f'{formula:.12f}')
helper=os.environ.get('DTC0A_HELPER_PATH','')
if helper:
 spec=importlib.util.spec_from_file_location('retained_dtc0a_helper',helper)
 src=importlib.util.module_from_spec(spec);spec.loader.exec_module(src)
 for N in (9,17,31):
  print('DIRECT RETAINED HELPER',N,test(N,.05,src))
print('N>=7 uniform alpha=.05 L2 lower >=',
      .8*(np.sin(2*np.pi/7)/(2*np.pi/7))/np.sqrt(2))
print('PASS / SYNTHETIC SOURCE-CARRIER ONLY')
