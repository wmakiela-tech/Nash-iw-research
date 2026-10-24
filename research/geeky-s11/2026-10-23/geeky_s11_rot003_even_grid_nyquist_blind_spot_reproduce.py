#!/usr/bin/env python3
"""Geeky-S11 ROT003: centered-symbol TT projector and even-grid Nyquist blind spot.
Requires numpy. No historical production DTC runner or physical claim is implied.
"""
from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np

AXES = np.eye(3)


def derivatives(F, h):
    return [(np.roll(F, -1, axis=j) - np.roll(F, 1, axis=j))/(2*h) for j in range(3)]


def apply_E(F, h, alpha):
    box = sum((np.roll(F,-1,axis=j)-2*F+np.roll(F,1,axis=j))/h**2 for j in range(3))
    return F + alpha*h*h*box


def lie_tensor(C,F,h):
    out = np.zeros_like(F)
    dF = derivatives(F,h)
    dC = derivatives(C,h)
    for k in range(3):
        out += C[...,k,None,None]*dF[k]
        for i in range(3):
            for j in range(3):
                out[...,i,j] += F[...,k,j]*dC[i][...,k] if k < 3 and i < 3 else 0
                out[...,i,j] += F[...,i,k]*dC[j][...,k] if k < 3 and j < 3 else 0
    return out


def centered_TT_projector(N):
    h=2*np.pi/N
    ki=np.rint(np.fft.fftfreq(N)*N).astype(int)
    d=np.sin(ki*h)/h
    d[(ki==0)|(np.abs(ki)==N//2)]=0.0
    vector=np.stack(np.meshgrid(d,d,d,indexing='ij'),axis=-1)
    d2=np.sum(vector*vector,axis=-1)
    pi=np.broadcast_to(np.eye(3),(N,N,N,3,3)).copy()
    pi -= np.einsum('...i,...j->...ij',vector,vector)/np.where(d2==0.,1.,d2)[...,None,None]
    pi[d2==0]=0

    def project(F):
        ft=np.fft.fftn(F,axes=(0,1,2))
        fp=np.einsum('...ik,...kl,...lj->...ij',pi,ft,pi,optimize=True)
        tr=np.einsum('...ij,...ji->...',pi,ft,optimize=True)
        fp -= (1/2)*pi*tr[...,None,None]
        x=np.fft.ifftn(fp,axes=(0,1,2))
        return x.real,float(np.max(abs(x.imag)))
    return project


def norm(F):
    return float(np.sqrt(np.mean(np.sum(F*F,axis=(-2,-1)))))


def test(N,alpha,constant=False):
    assert N >= 6 and N%2==0
    h=2*np.pi/N
    coord=np.arange(N)*h
    x,y,z=np.meshgrid(coord,coord,coord,indexing='ij')
    C=np.zeros((N,N,N,3),dtype=float)
    C[...,0]=1.0 if constant else ((-1.)**np.arange(N))[:,None,None]
    project=centered_TT_projector(N)
    v=np.array([1.,-1.,0])/np.sqrt(2)
    w=np.array([0.,0.,1.])
    T=np.outer(v,v)-np.outer(w,w)
    H=np.cos(x+y)[...,None,None]*T
    pH,imH=project(H)
    LH=lie_tensor(C,apply_E(H,h,alpha),h)
    pLH,imLH=project(LH)
    Q=LH-pLH
    measured=norm(Q)/norm(H)
    expected=0.0 if constant else math.sqrt(3)/2*abs(math.sin(h)/h)*abs(1-8*alpha*math.sin(h/2)**2)

    axprobes=[]
    for axis in range(3):
        b,c=[i for i in range(3) if i!=axis]
        A=(np.outer(AXES[b],AXES[b])-np.outer(AXES[c],AXES[c]))/math.sqrt(3)
        B=(np.outer(AXES[b],AXES[c])+np.outer(AXES[c],AXES[b]))/math.sqrt(2)
        phasecoord=[x,y,z][axis]
        for name,M in [('A',A),('B',B)]:
            for phase,fun in [('c',np.cos),('s',np.sin)]:
                G=fun(phasecoord)[...,None,None]*M
                pG,imG=project(G)
                LG=lie_tensor(C,apply_E(G,h,alpha),h)
                pLG,imLG=project(LG)
                axprobes.append({'probe':f'{name}{axis}{phase}', 'rel_TT_input_err':norm(G-pG)/norm(G),
                                 'rel_Q_output':norm(LG-pLG)/norm(G),'imag_max':max(imG,imLG)})
    max_checker_deriv=max(float(np.max(abs(v))) for v in derivatives(C,h))
    return {'N':N,'alpha':alpha,'constant':constant,
            'oblique_witness_measured':measured,'oblique_witness_expected':expected,
            'oblique_abs_gap':abs(measured-expected),'oblique_TT_input_rel_err':norm(H-pH)/norm(H),
            'oblique_output_trace_max':float(np.max(abs(np.trace(LH,axis1=-2,axis2=-1)))),
            'max_checkerboard_centered_grad':max_checker_deriv,
            'max_axial_probe_TT_error':max(t['rel_TT_input_err'] for t in axprobes),
            'max_axial_probe_output_leak':max(t['rel_Q_output'] for t in axprobes),
            'max_projector_imag':max([imH,imLH]+[t['imag_max'] for t in axprobes]),
            'axial_probes':axprobes}


def main():
    cases=[test(N,a) for N in (8,12,20,32) for a in (0.,.05,.2)]
    cases.append(test(12,.05,constant=True))
    summary={'artifact_id':'GEEKY-S11-ROT003-EVEN-NYQUIST-AXIAL-PROBE-BLIND-SPOT-001',
             'class':'EXACT EVEN-GRID CENTERED-SYMBOL TT COUNTEREXAMPLE / NO PHYSICAL CLAIM',
             'cases':cases,
             'case_count':len(cases),
             'max_oblique_abs_gap':max(t['oblique_abs_gap'] for t in cases),
             'max_axial_probe_output_leak':max(t['max_axial_probe_output_leak'] for t in cases),
             'max_axial_probe_TT_error':max(t['max_axial_probe_TT_error'] for t in cases),
             'max_centered_grad':max(t['max_checkerboard_centered_grad'] for t in cases),
             'max_projector_imag':max(t['max_projector_imag'] for t in cases),
             'all_expected_leakage_positive_nonconstant':all(t['oblique_witness_measured']>0.5 for t in cases if not t['constant'])}
    (Path(__file__).resolve().parent/'geeky_s11_rot003_even_grid_nyquist_results.json').write_text(json.dumps(summary,indent=2)+'\n')
    assert summary['max_oblique_abs_gap'] < 1e-12
    assert summary['max_axial_probe_output_leak'] < 1e-12
    assert summary['max_axial_probe_TT_error'] < 1e-12
    assert summary['max_centered_grad'] == 0.0
    assert summary['all_expected_leakage_positive_nonconstant']
    print(json.dumps({k:v for k,v in summary.items() if k!='cases'},indent=2))
    for r in cases:
        print('N',r['N'],'alpha',r['alpha'],'constant',r['constant'],'oblique',round(r['oblique_witness_measured'],12),'axial_max',format(r['max_axial_probe_output_leak'],'.2e'))

if __name__=='__main__':main()
