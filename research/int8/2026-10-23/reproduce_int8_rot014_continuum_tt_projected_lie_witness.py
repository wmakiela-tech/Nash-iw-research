"""INT8 ROT014: independent FFT validation of exact continuum TT Lie bracket nonclosure.
Synthetic 3-torus; original historical DTC0a v0.3.1 runtime NOT replayed.
"""
import numpy as np

def deriv(f,axis,N):
  k=np.fft.fftfreq(N,d=1/N)
  shape=[1]*f.ndim; shape[axis]=N
  return np.fft.ifftn(1j*k.reshape(shape)*np.fft.fftn(f,axes=(0,1,2)),axes=(0,1,2)).real

def lie(C,H,N):
  T=np.zeros_like(H)
  for m in range(3):
    for i in range(3):
      for j in range(3):
        T[...,i,j]+=C[...,m]*deriv(H[...,i,j],m,N)
        T[...,i,j]+=H[...,m,j]*deriv(C[...,m],i,N)
        T[...,i,j]+=H[...,i,m]*deriv(C[...,m],j,N)
  return T

def bracket(C,D,N):
  E=np.zeros_like(C)
  for j in range(3):
    for m in range(3):
      E[...,j]+=C[...,m]*deriv(D[...,j],m,N)-D[...,m]*deriv(C[...,j],m,N)
  return E

def PTT(H,N):
  F=np.fft.fftn(H,axes=(0,1,2))
  k=np.fft.fftfreq(N,d=1/N)
  grids=np.meshgrid(k,k,k,indexing='ij')
  K=np.stack(grids,axis=-1)
  den=np.sum(K*K,axis=-1)
  inv=np.zeros_like(den); np.divide(1.,den,out=inv,where=den!=0)
  P=np.eye(3)-np.einsum('...i,...j,...->...ij',K,K,inv)
  PF=np.einsum('...ia,...ab,...bj->...ij',P,F,P)
  trace=np.einsum('...ab,...ab->...',P,F)
  TT=PF-.5*P*trace[...,None,None]
  TT[den==0]=F[den==0]-np.eye(3)*np.trace(F[den==0],axis1=-2,axis2=-1)[...,None,None]/3
  return np.fft.ifftn(TT,axes=(0,1,2)).real

def test(N):
  z=np.arange(N)*2*np.pi/N
  X,Y,Z=np.meshgrid(z,z,z,indexing='ij')
  a=np.zeros((N,N,N,3));b=a.copy();H=np.zeros((N,N,N,3,3))
  a[...,0]=np.cos(X);b[...,1]=np.cos(X)
  H[...,0,0]=np.cos(Z);H[...,1,1]=-np.cos(Z)
  hnorm=np.sqrt(np.mean(np.sum(H*H,axis=(-1,-2))))
  pH=PTT(H,N)
  KC=lie(a,lie(b,H,N),N)-lie(b,lie(a,H,N),N)-lie(bracket(a,b,N),H,N)
  KA=PTT(lie(a,PTT(lie(b,H,N),N),N)-lie(b,PTT(lie(a,H,N),N),N)-lie(bracket(a,b,N),H,N),N)
  F=np.fft.fftn(KA,axes=(0,1,2))/(N**3)
  G=np.fft.fftn(KC,axes=(0,1,2))/(N**3)
  rms=np.sqrt(np.mean(np.sum(KA*KA,axis=(-1,-2))))
  expect=np.array([[0,-1/10,0],[-1/10,0,1/5],[0,1/5,0]])/8
  print('N=',N,'pH error=',np.max(np.abs(pH-H)), 'KC max=',np.max(np.abs(KC)),'KA RMS=',rms,'KA/H=',rms/hnorm)
  print('Khat(2,0,1):',F[2,0,1], 'expected:',expect,'KChat max=',np.max(np.abs(G)))
  assert np.max(np.abs(KC))<1e-10
  assert np.max(np.abs(pH-H))<1e-12
  assert np.max(abs(F[2,0,1]-expect))<1e-12
  assert abs(rms-np.sqrt(11/160))<1e-12

if __name__=='__main__':
  for N in (9,11,17,31):test(N)
  print('PASS synthetic exact finite Fourier witness / NO PHYSICAL CLAIM')
