#!/usr/bin/env python3
"""Geeky-S11 ROT008: two fourth-order centered stencils, opposite Nyquist-TT symmetry.
Stand-alone NumPy checkerboard exact Fourier probes, broad-band TT control, and symbolic moment assertions.
DOES NOT test historic original raw-k DTC0a runtime.
"""
import json
from pathlib import Path
import numpy as np

OUT = Path('/mnt/data/geeky_s11_rot008_stencil_parity_results.json')
STENCILS = {
    'order2_R1': {1: 1.},
    'order4_R2_standard': {1: 4./3., 2: -1./6.},
    'order4_R3_odd_steps': {1: 9./8., 3: -1./24.},
}

def der(F, axis, h, weights):
    return sum(a*(np.roll(F,-r,axis=axis)-np.roll(F,r,axis=axis))/(2*h)
               for r,a in weights.items())

def sym(k,N,h,weights):
    theta=2*np.pi*k/N
    result=sum(a*np.sin(r*theta) for r,a in weights.items())/h
    # Force exact zeros of antisymmetric real periodic derivative at k=0, Nyquist
    result=np.asarray(result).copy()
    result[(np.asarray(k)==0)|(np.abs(np.asarray(k))==N//2)]=0.
    return result

def proj_tt(F,N,weights):
    h=2*np.pi/N
    k=np.rint(np.fft.fftfreq(N)*N).astype(int)
    dk=sym(k,N,h,weights)
    d=np.stack(np.meshgrid(dk,dk,dk,indexing='ij'),axis=-1)
    d2=np.einsum('...i,...i->...',d,d)
    pi=np.broadcast_to(np.eye(3),(N,N,N,3,3)).copy()
    pi-=np.einsum('...i,...j->...ij',d,d)/np.where(d2==0,1,d2)[...,None,None]
    pi[d2==0]=0
    FF=np.fft.fftn(F,axes=(0,1,2))
    PP=np.einsum('...ik,...kl,...lj->...ij',pi,FF,pi,optimize=True)
    tr=np.einsum('...ij,...ji->...',pi,FF,optimize=True)
    PP-=.5*pi*tr[...,None,None]
    result=np.fft.ifftn(PP,axes=(0,1,2))
    return result.real,float(np.max(np.abs(result.imag)))

def norm(F):
    return float(np.sqrt(np.mean(np.sum(F*F,axis=(-2,-1)))))

def LchiE(H,chi,N,weights,alpha):
    h=2*np.pi/N
    EH=H+alpha*sum(np.roll(H,-1,axis=a)-2*H+np.roll(H,1,axis=a) for a in range(3))
    return chi[...,None,None]*der(EH,0,h,weights)

def rho_analytic(N,weights,alpha,kx,ky):
    h=2*np.pi/N
    # first differential symbol at input; shifted delta at output
    dx=float(sym(np.array([kx]),N,h,weights)[0]);dy=float(sym(np.array([ky]),N,h,weights)[0])
    ux=float(sym(np.array([kx-N//2]),N,h,weights)[0]);uy=float(sym(np.array([ky-N//2]),N,h,weights)[0])
    cross=abs(dx*uy-dy*ux)/(np.hypot(dx,dy)*np.hypot(ux,uy))
    rho=cross*np.sqrt(4-cross**2)/2
    e=1-4*alpha*(np.sin(np.pi*kx/N)**2+np.sin(np.pi*ky/N)**2)
    return abs(dx*e)*rho,cross,e,dx,dy

def main():
    # Fourth-order derivative, equivalence of two consistency moment constraints.
    moments={}
    for name,w in STENCILS.items():
        m1=sum(r*a for r,a in w.items());m3=sum(r**3*a for r,a in w.items())
        moments[name]=dict(m1=m1,m3=m3,radius=max(w),odd_shifts_only=all(r%2==1 for r in w))
        assert abs(m1-1)<1e-14
        if 'order4' in name:assert abs(m3)<1e-14
        else:assert abs(m3-1)<1e-14
    roots=(0.,.05,.2,.25,1/(4-np.sqrt(2)))
    rows=[];broad=[]
    for N in (8,16,24,32):
        h=2*np.pi/N
        j=np.arange(N)
        x,y,z=np.meshgrid(h*j,h*j,h*j,indexing='ij')
        chi=(-1.)**(j[:,None,None]+j[None,:,None]+j[None,None,:])
        for name,w in STENCILS.items():
            # All stencils must annihilate the checkerboard, by antisymmetry.
            assert np.max(abs(der(chi,0,h,w)))==0
            for alpha in roots:
                for carrier,ky in (('A',N//4),('B',3*N//8)):
                    kx=N//8
                    dx=float(sym(np.array([kx]),N,h,w)[0]);dy=float(sym(np.array([ky]),N,h,w)[0])
                    v=np.array([dy,-dx,0.])/np.hypot(dx,dy)
                    T=np.outer(v,v)-np.diag([0.,0.,1.])
                    H=np.cos(kx*x+ky*y)[...,None,None]*T
                    PH,imag_H=proj_tt(H,N,w)
                    LH=LchiE(H,chi,N,w,alpha)
                    PL,imag_L=proj_tt(LH,N,w)
                    actual=norm(LH-PL)/norm(H)
                    predicted,cross,e,_,_=rho_analytic(N,w,alpha,kx,ky)
                    err=abs(actual-predicted)
                    assert err<3e-12,(N,name,alpha,carrier,actual,predicted,err)
                    TT=norm(H-PH)/norm(H)
                    assert TT<4e-13,(N,name,carrier,TT)
                    if name!='order4_R2_standard':assert actual<4e-12,(N,name,alpha,carrier,actual)
                    rows.append(dict(N=N,stencil=name,alpha=float(alpha),carrier=carrier,
                                     leakage=actual,formula=predicted,absolute_formula_error=err,
                                     TT_input_error=TT,angle_sine=cross,filter=e,
                                     projector_imag_max=max(imag_H,imag_L)))
            # One broad-band random TT test for BOTH odd-step stencils and the even-step stencil.
            rng=np.random.default_rng(1000+N)
            X=rng.standard_normal((N,N,N,3,3))
            X=(X+X.swapaxes(-1,-2))/2
            H,_=proj_tt(X,N,w)
            L=LchiE(H,chi,N,w,.05)
            P,_=proj_tt(L,N,w)
            val=norm(L-P)/norm(H)
            if name!='order4_R2_standard':assert val<5e-12,(N,name,val)
            broad.append(dict(N=N,stencil=name,leakage=val))
    # Finite mode two-carrier exact minimax from ROT007, against the even-step stencil:
    rt2=np.sqrt(2)
    rhoA=16*np.sqrt(9217)/9281
    rhoB=8*np.sqrt(2114)/1089
    A=(4*rt2-1)*rhoA/(12*np.pi)
    B=(4*rt2-1)*rhoB/(12*np.pi)
    p=4-rt2
    alpha_star=(A+B)/(p*A+4*B)
    floor=A*B*rt2/(p*A+4*B)
    for N in (8,16,24,32):
        for alpha in roots:
            leak=max(r['leakage'] for r in rows if r['N']==N and r['stencil']=='order4_R2_standard' and r['alpha']==alpha)
            assert leak+2e-12>=floor*N
    res=dict(artifact_id='GEEKY-S11-ROT008-FOURTH_ORDER_SAME_ACCURACY_DIFFERENT_NYQUIST_TT_PRESERVATION',
             status='PASS',cases=len(rows),N=[8,16,24,32],alpha=list(roots),
             stencils=STENCILS,moment_checks=moments,
             max_exact_formula_error=max(r['absolute_formula_error'] for r in rows),
             max_tt_input_error=max(r['TT_input_error'] for r in rows),
             max_odd_shift_checkerboard_leak=max(r['leakage'] for r in rows if r['stencil']=='order4_R3_odd_steps'),
             broad_band_controls=broad,alpha_tuned_all_compatible_lower_per_N=floor,
             evenstep_best_witness_alpha=alpha_star,rows=rows)
    OUT.write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n')
    print('PASS',json.dumps({k:v for k,v in res.items() if k!='rows'},indent=2))
    return res
if __name__=='__main__':main()
