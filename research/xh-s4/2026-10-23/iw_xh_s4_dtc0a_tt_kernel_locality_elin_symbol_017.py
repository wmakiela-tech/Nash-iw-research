"""XH-S4 017: finite-grid TT nonlocality lower bounds and E_lin Fourier symbols.
This is a verification of the published-to-project applicability gate, NOT a DTC0a physical or continuum result.
"""
import json
import numpy as np

def tt_impulse(N):
    k1=np.fft.fftfreq(N,d=1/N)
    k=np.stack(np.meshgrid(k1,k1,k1,indexing='ij'),axis=-1)
    k2=np.sum(k*k,axis=-1)
    inv=np.divide(1.,k2,out=np.zeros_like(k2,dtype=float),where=k2>0)
    P=np.eye(3)-k[..., :,None]*k[...,None,:]*inv[...,None,None]
    T=P[..., :,0,None]*P[...,None,0,:]-.5*P*P[...,0,0,None,None]
    T[0,0,0]=np.diag([2/3,-1/3,-1/3])
    out=np.fft.ifftn(T,axes=(0,1,2))
    assert np.max(abs(out.imag))<1e-12
    return out.real

def direct_tt_impulse(N):
    h=np.zeros((N,N,N,3,3))
    h[0,0,0,0,0]=1
    H=np.fft.fftn(h,axes=(0,1,2))
    out=np.zeros_like(H)
    a=np.fft.fftfreq(N,d=2*np.pi/N)
    for x in range(N):
      for y in range(N):
       for z in range(N):
        k=np.array([a[x],a[y],a[z]])
        k2=np.sum(k*k)
        if k2==0:
            out[x,y,z]=H[x,y,z]-np.trace(H[x,y,z])/3*np.eye(3)
        else:
            p=np.eye(3)-np.outer(k,k)/k2
            out[x,y,z]=p@H[x,y,z]@p-.5*p*np.sum(p*H[x,y,z])
    return np.fft.ifftn(out,axes=(0,1,2)).real

def tail_stats(N):
    h=tt_impulse(N)
    i=np.arange(N); r=np.minimum(i,N-i)
    R=np.maximum.reduce(np.broadcast_arrays(r[:,None,None],r[None,:,None],r[None,None,:]))
    E=np.sum(h*h,axis=(-1,-2))
    result={'N':N,'projected_impulse_norm':float(np.sqrt(E.sum())),'radii':{}}
    for m in [0,1,2,3,4,6,8]:
        if m<N//2:
            tail=float(E[R>m].sum())
            result['radii'][m]={'relative_energy_tail':tail/float(E.sum()),
                    'minimum_operator_norm_error_for_m_local_approx':np.sqrt(tail)}
    return result

def elin_stats(N,alpha):
    kd=2*np.pi*np.fft.fftfreq(N)
    si=np.sin(kd/2)**2
    s=si[:,None,None]+si[None,:,None]+si[None,None,:]
    lam=1-4*alpha*s
    a=np.abs(lam)
    return {'N':N,'alpha':alpha,'lambda_min':float(lam.min()),'lambda_max':float(lam.max()),
            'negative_fraction':float(np.mean(lam<0)),'min_abs_lambda':float(a.min()),
            'condition_number_if_inverse_used':float(a.max()/a.min())}

def main():
    checks={N:float(np.max(abs(tt_impulse(N)-direct_tt_impulse(N)))) for N in [7,9]}
    assert all(v<1e-12 for v in checks.values())
    data={'scope':'periodic odd N, 3D symmetric Frobenius norm; unit tensor delta input; no continuum theorem',
          'independent_fft_agreement':checks,
          'TT':[tail_stats(N) for N in [17,31,41]],
          'E_lin':[elin_stats(N,a) for N in [31,41] for a in [0,.05,.2]]}
    print(json.dumps(data,indent=2))

if __name__=='__main__': main()
