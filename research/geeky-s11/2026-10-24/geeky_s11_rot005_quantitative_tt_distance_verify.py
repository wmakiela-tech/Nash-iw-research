#!/usr/bin/env python3
"""ROT005 independent quantitative frame verification; NumPy-only.

The fixed projector is the *matched centered-symbol* Fourier TT P_delta on even grids.
This is not the archived raw-wavevector historical DTC0a TT projector.
"""
from __future__ import annotations
import json
import math
import numpy as np
from pathlib import Path

EYE=np.eye(3)
PAIRS=((0,1),(0,2),(1,2))

def d1(F,j,h):
    return (np.roll(F,-1,axis=j)-np.roll(F,1,axis=j))/(2*h)

def E_alpha(F,a):
    return F+a*sum(np.roll(F,-1,axis=j)-2*F+np.roll(F,1,axis=j) for j in range(3))

def lie(C,F,h):
    dC=[d1(C,i,h) for i in range(3)]
    A=sum(C[...,k,None,None]*d1(F,k,h) for k in range(3))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                A[...,i,j]+=F[...,k,j]*dC[i][...,k]+F[...,i,k]*dC[j][...,k]
    return A

def norm2_tensor(F):
    return float(np.mean(np.sum(np.abs(F)**2,axis=(-2,-1))))

def norm2_vector(F):
    return float(np.mean(np.sum(np.abs(F)**2,axis=-1)))

def norm2_scalar(F):
    return float(np.mean(np.abs(F)**2))

def P_delta(F,h):
    N=F.shape[0]
    k=np.rint(np.fft.fftfreq(N)*N).astype(int)
    d=np.sin(k*h)/h
    d[(k==0)|(np.abs(k)==N//2)]=0
    v=np.stack(np.meshgrid(d,d,d,indexing='ij'),axis=-1)
    v2=np.einsum('...i,...i->...',v,v)
    pi=np.broadcast_to(EYE,(N,N,N,3,3)).copy()
    pi-=v[..., :,None]*v[...,None,:]/np.where(v2==0,1,v2)[...,None,None]
    pi[v2==0]=0
    X=np.fft.fftn(F,axes=(0,1,2))
    Z=np.einsum('...ik,...kl,...lj->...ij',pi,X,pi,optimize=True)
    t=np.einsum('...ij,...ji->...',pi,X,optimize=True)
    Z-=0.5*pi*t[...,None,None]
    return np.fft.ifftn(Z,axes=(0,1,2)).real

def probe_sets(N):
    coords=np.meshgrid(*([2*np.pi*np.arange(N)/N]*3),indexing='ij')
    axial=[]
    for a in range(3):
        b,c=[i for i in range(3) if i!=a]
        mats=[(np.outer(EYE[b],EYE[b])-np.outer(EYE[c],EYE[c]))/np.sqrt(3),
              (np.outer(EYE[b],EYE[c])+np.outer(EYE[c],EYE[b]))/np.sqrt(2)]
        for T in mats:
            for f in (np.cos(coords[a]),np.sin(coords[a])):
                axial.append(f[...,None,None]*T)
    oblique=[]
    for a,b in PAIRS:
        c=next(i for i in range(3) if i not in (a,b))
        for sigma in (-1,1):
            v=(EYE[a]-sigma*EYE[b])/np.sqrt(2)
            T=np.outer(v,v)-np.outer(EYE[c],EYE[c])
            for f in (np.cos(coords[a]+sigma*coords[b]),np.sin(coords[a]+sigma*coords[b])):
                oblique.append(f[...,None,None]*T)
    return axial,oblique

def corners(C):
    N=C.shape[0]
    js=np.indices((N,N,N))
    chi=[]; coeff=[]
    for m in range(8):
        z=np.ones((N,N,N))
        for j in range(3):
            if (m>>j)&1: z*=(-1.)**js[j]
        chi.append(z)
        coeff.append(np.mean(C*z[...,None],axis=(0,1,2)))
    return np.array(coeff),chi

def runs():
    rows=[]
    for N in (6,8,10,12):
        h=2*np.pi/N; s=np.sin(h)/h
        axial,oblique=probe_sets(N)
        for alpha in (0.,.05,.2):
            for kind in ('generic','almost_kernel','kernel'):
                rng=np.random.default_rng(13000+N*1000+round(1000*alpha)+{'generic':1,'almost_kernel':2,'kernel':3}[kind])
                js=np.indices((N,N,N))
                chi111=(-1.)**(js[0]+js[1]+js[2])
                C=rng.normal(scale=.12,size=(N,N,N,3))
                a=np.array((0.08,-0.11,0.13));b=np.array((0.23,-0.05,0.17))
                if kind=='generic':
                    C=C+a+b*chi111[...,None]
                elif kind=='almost_kernel':
                    C=a+b*chi111[...,None]+.0001*C
                else:
                    C=a+b*chi111[...,None]
                coeff,chi=corners(C)
                target=coeff[0]+chi[7][...,None]*coeff[7]
                Chat=np.fft.fftn(C,axes=(0,1,2))/(N**3)
                Chat[0,0,0]=0
                Chat[N//2,N//2,N//2]=0
                dist2=float(np.sum(np.abs(Chat)**2))
                assert abs(dist2-norm2_vector(C-target))<1e-11
                S=np.zeros((N,N,N,3,3))
                for i in range(3):
                    for j in range(3):
                        S[...,i,j]=0.5*(d1(C[...,j],i,h)+d1(C[...,i],j,h))
                S0=S-np.trace(S,axis1=-2,axis2=-1)[...,None,None]*EYE/3
                sn2=norm2_tensor(S0)
                W=0.
                for m in range(8):
                    for i,j in PAIRS:
                        if ((m>>i)&1)!=((m>>j)&1):
                            W+=coeff[m,i]**2+coeff[m,j]**2
                e1=1-4*alpha*np.sin(np.pi/N)**2
                e2=1-8*alpha*np.sin(np.pi/N)**2
                axial_trace=sum(norm2_scalar(np.trace(lie(C,E_alpha(H,alpha),h),axis1=-2,axis2=-1)) for H in axial)
                oblique_energy=0.
                for H in oblique:
                    A=lie(C,E_alpha(H,alpha),h)
                    oblique_energy+=norm2_tensor(A-P_delta(A,h))
                exact_ax=4*e1*e1*sn2
                exact_corner_ob=3*e2*e2*s*s*W
                frame_lower=axial_trace/3+oblique_energy
                tight_lower=exact_ax/3+exact_corner_ob
                coercivity=s*s/17*min((2/3)*e1*e1,3*e2*e2)*dist2
                op_witness=frame_lower/17
                # Need not evaluate gigantic full operator matrix; weighted average of 24 probes bounds it.
                rows.append(dict(N=N,alpha=alpha,case=kind,dist2=dist2,axial_trace=axial_trace,
                  predicted_axial_trace=exact_ax,oblique_energy=oblique_energy,corner_component_lower=exact_corner_ob,
                  frame_lower=frame_lower,tight_lower=tight_lower,coercivity_square=coercivity,
                  operator_witness_square=op_witness,pass_bound=bool(frame_lower+3e-12>=tight_lower and op_witness+3e-12>=coercivity)))
                print(f'N{N:2d} a{alpha:.2f} {kind:13s} dist {math.sqrt(dist2):.4g} '
                      f'frame {math.sqrt(op_witness):.4g} certificate {math.sqrt(coercivity):.4g} '
                      f'corner ≤ob {exact_corner_ob:.5g}≤{oblique_energy:.5g}')
    summ={ 'artifact':'GEEKY_S11_ROT005_UNIFORM_EVEN_N_TT_DISTANCE_COERCIVITY_001',
      'status':'executed mathematical tests; not physical inference; no novelty',
      'case_count':len(rows),
      'maximum_axial_frame_abs_error':max(abs(r['axial_trace']-r['predicted_axial_trace']) for r in rows),
      'maximum_oblique_corner_overshoot':max(r['corner_component_lower']-r['oblique_energy'] for r in rows),
      'minimum_coercivity_margin':min(r['operator_witness_square']-r['coercivity_square'] for r in rows),
      'all_pass':all(r['pass_bound'] for r in rows),
      'rows':rows}
    Path(__file__).with_name('geeky_s11_rot005_even_tt_distance_results.json').write_text(json.dumps(summ,indent=2)+'\n')
    assert summ['all_pass']
    assert summ['maximum_axial_frame_abs_error']<1e-10
    assert summ['maximum_oblique_corner_overshoot']<1e-10
    print('STATUS PASS',json.dumps({k:v for k,v in summ.items() if k!='rows'},indent=2))
if __name__=='__main__': runs()
