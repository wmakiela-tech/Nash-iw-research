#!/usr/bin/env python3
"""ROT004: exact even-N matched-symbol TT-preservation kernel and oblique finite frame.
Independent full-grid numerical checks, no claim about historical original DTC runtime.
Requires NumPy. Run: python geeky_s11_rot004_even_nyquist_tt_kernel_verify.py
"""
from __future__ import annotations
import json, hashlib
from pathlib import Path
import numpy as np

EYE=np.eye(3)
PAIRS=((0,1),(0,2),(1,2))

def norm2(F):
    return float(np.mean(np.sum(np.abs(F)**2,axis=(-2,-1))))

def d1(F,j,h):
    return (np.roll(F,-1,axis=j)-np.roll(F,1,axis=j))/(2*h)

def E_alpha(F,h,alpha):
    box=sum(np.roll(F,-1,axis=j)-2*F+np.roll(F,1,axis=j) for j in range(3))
    return F+alpha*box

def lie(C,F,h):
    dC=[d1(C,i,h) for i in range(3)]
    out=sum(C[...,k,None,None]*d1(F,k,h) for k in range(3))
    for i in range(3):
      for j in range(3):
        for k in range(3):
          out[...,i,j]+= F[...,k,j]*dC[i][...,k]+F[...,i,k]*dC[j][...,k]
    return out

def P_delta(F,h):
    N=F.shape[0]
    k=np.rint(np.fft.fftfreq(N)*N).astype(int)
    d=np.sin(k*h)/h
    d[(k==0)|(np.abs(k)==N//2)]=0.
    v=np.stack(np.meshgrid(d,d,d,indexing='ij'),axis=-1)
    d2=np.einsum('...i,...i->...',v,v)
    pi=np.broadcast_to(EYE,(N,N,N,3,3)).copy()
    pi-=np.einsum('...i,...j->...ij',v,v,optimize=True)/np.where(d2==0.,1.,d2)[...,None,None]
    pi[d2==0.]=0.
    X=np.fft.fftn(F,axes=(0,1,2))
    Xp=np.einsum('...ik,...kl,...lj->...ij',pi,X,pi,optimize=True)
    tr=np.einsum('...ij,...ji->...',pi,X,optimize=True)
    Xp-=.5*pi*tr[...,None,None]
    return np.fft.ifftn(Xp,axes=(0,1,2)).real

def grid(N):
    x=2*np.pi*np.arange(N)/N
    return np.meshgrid(x,x,x,indexing='ij')

def corner_C(coeff,N):
    coords=np.indices((N,N,N))
    C=np.zeros((N,N,N,3),dtype=float)
    for mask in range(8):
        chi=np.ones((N,N,N))
        for j in range(3):
            if (mask>>j)&1: chi*=(-1.)**coords[j]
        C+=chi[...,None]*coeff[mask]
    return C

def T_oblique(a,b,sgn):
    z=next(j for j in range(3) if j not in (a,b))
    v=(EYE[a]-sgn*EYE[b])/np.sqrt(2)
    return np.outer(v,v)-np.outer(EYE[z],EYE[z])

def oblique_probe_fields(N):
    xyz=grid(N)
    for a,b in PAIRS:
      for sign in (-1,1):
        kx=xyz[a]+sign*xyz[b]
        T=T_oblique(a,b,sign)
        yield (a,b,sign,'cos'),np.cos(kx)[...,None,None]*T
        yield (a,b,sign,'sin'),np.sin(kx)[...,None,None]*T

def axial_probe_fields(N):
    xyz=grid(N)
    for a in range(3):
      b,c=[i for i in range(3) if i!=a]
      A=(np.outer(EYE[b],EYE[b])-np.outer(EYE[c],EYE[c]))/np.sqrt(3)
      B=(np.outer(EYE[b],EYE[c])+np.outer(EYE[c],EYE[b]))/np.sqrt(2)
      for T in (A,B):
        for wave in (np.cos(xyz[a]),np.sin(xyz[a])):
          yield wave[...,None,None]*T

def frame_formula(coeff,N,alpha):
    h=2*np.pi/N
    s=np.sin(h)/h
    e2=1-8*alpha*np.sin(h/2)**2
    W=0.
    for mask in range(1,7):
      for a,b in PAIRS:
        if ((mask>>a)&1)!=((mask>>b)&1):
          W += coeff[mask,a]**2+coeff[mask,b]**2
    return float(3*e2*e2*s*s*W),float(W)

def run_case(N,alpha,seed):
    h=2*np.pi/N
    rng=np.random.default_rng(seed)
    coeff=rng.normal(scale=.09,size=(8,3))
    C=corner_C(coeff,N)
    dC=max(float(np.max(np.abs(d1(C,j,h)))) for j in range(3))
    pred,W=frame_formula(coeff,N,alpha)
    observed=0.
    tt_err=0.
    axial_leak=0.
    for _,H in oblique_probe_fields(N):
        tt_err=max(tt_err,np.sqrt(norm2(P_delta(H,h)-H)/norm2(H)))
        A=lie(C,E_alpha(H,h,alpha),h)
        observed+=norm2(A-P_delta(A,h))
    # axial frame for corner C must be null too in trace, but FULL projection not necessarily
    # zero for all corner types. Record max trace.
    axial_trace=0.
    for H in axial_probe_fields(N):
        A=lie(C,E_alpha(H,h,alpha),h)
        axial_trace=max(axial_trace,float(np.max(np.abs(np.trace(A,axis1=-2,axis2=-1)))))
    # fully undetectable full checkerboard plus constant: oblique AND arbitrary TT inputs.
    only6=np.zeros_like(coeff)
    only6[0]=coeff[0]; only6[7]=coeff[7]
    C6=corner_C(only6,N)
    null_check=0.
    for H in list(axial_probe_fields(N))+[q for _,q in oblique_probe_fields(N)]:
        A=lie(C6,E_alpha(H,h,alpha),h)
        null_check=max(null_check,np.sqrt(norm2(A-P_delta(A,h))))
    # random real TT input at arbitrary bandwidth
    Hrng=rng.normal(size=(N,N,N,3,3)); Hrng=.5*(Hrng+np.swapaxes(Hrng,-1,-2))
    Hrng=P_delta(Hrng,h)
    A=lie(C6,E_alpha(Hrng,h,alpha),h)
    random_null=np.sqrt(norm2(A-P_delta(A,h)))/max(np.sqrt(norm2(Hrng)),1e-30)
    return dict(N=N,alpha=alpha,seed=seed,nonconstant_coeff_norm=float(np.linalg.norm(coeff[1:7])),
                source_gradient_max=dC,trace_axial_max=axial_trace,
                observed_frame_energy=observed,predicted_frame_energy=pred,energy_abs_err=abs(observed-pred),
                W=W,tt_input_relative_max=tt_err,
                predicted_operator_lower=np.sqrt(pred/12),
                witnessed_operator_lower=np.sqrt(observed/12),
                six_dimensional_kernel_24_probe_absolute_max=null_check,
                six_dimensional_kernel_random_relative_leak=random_null)

def main():
    cases=[(N,a,700+N*100+i) for N in (6,8,10,12) for i,a in enumerate((0.,.05,.2))]
    rows=[run_case(*case) for case in cases]
    summary={'artifact':'GEEKY_S11_ROT004_EVEN_NYQUIST_EXACT_KERNEL_AND_OBLIQUE_FRAME_001',
             'status':'executed mathematical diagnostics; no novelty/physical claim',
             'rows':rows,
             'max_energy_abs_err':max(x['energy_abs_err'] for x in rows),
             'max_relative_frame_err':max(x['energy_abs_err']/max(x['predicted_frame_energy'],1e-30) for x in rows),
             'max_tt_input_relative_err':max(x['tt_input_relative_max'] for x in rows),
             'max_kernel_24_probe_residual':max(x['six_dimensional_kernel_24_probe_absolute_max'] for x in rows),
             'max_kernel_random_relative_leak':max(x['six_dimensional_kernel_random_relative_leak'] for x in rows)}
    out=Path(__file__).with_name('geeky_s11_rot004_even_nyquist_tt_kernel_results.json')
    out.write_text(json.dumps(summary,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in summary.items() if k!='rows'},indent=2))
    print('CASES',len(rows))
    assert summary['max_relative_frame_err']<1e-10
    assert summary['max_tt_input_relative_err']<1e-10
    assert summary['max_kernel_random_relative_leak']<1e-10
    print('PASS')
if __name__=='__main__':main()
