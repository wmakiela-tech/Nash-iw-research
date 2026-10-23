#!/usr/bin/env python3
"""Geeky-S11 ROT001: fixed smooth TT leakage corollary; independent Fourier and optional retained helper verification.
Standalone: numpy only. No historical production runtime is asserted.
"""
import argparse
import importlib.util
import json
import math
import os
from pathlib import Path
import numpy as np


def get_test(N):
    x = np.arange(N) * (2*np.pi/N)
    xx, yy, zz = np.meshgrid(x, x, x, indexing='ij')
    C = np.zeros((N,N,N,3), float)
    C[...,0] = np.sin(xx)
    H = np.zeros((N,N,N,3,3),float)
    H[...,0,0] = np.cos(zz)
    H[...,1,1] = -np.cos(zz)
    return C,H,xx,zz


def source_lie_closed(N,alpha):
    C,H,xx,zz=get_test(N)
    h = 2*np.pi/N
    sigma = math.sin(h)/h
    filt = 1-4*alpha*math.sin(h/2)**2
    L = np.zeros_like(H)
    L[...,0,0] = 2*sigma*filt*np.cos(xx)*np.cos(zz)
    return C,H,L


def projector_fourier(H):
    N=H.shape[0]
    h=2*np.pi/N
    k=np.fft.fftfreq(N, d=h)*2*np.pi
    K=np.stack(np.meshgrid(k,k,k,indexing='ij'),-1)
    k2=(K*K).sum(-1)
    inv=np.zeros_like(k2)
    np.divide(1.0,k2,where=k2>0,out=inv)
    PT=np.eye(3)-np.einsum('...i,...j,...->...ij',K,K,inv)
    A=np.fft.fftn(H,axes=(0,1,2))
    pap=np.einsum('...ia,...ab,...bj->...ij',PT,A,PT,optimize=True)
    tr=np.einsum('...ij,...ij->...',PT,A,optimize=True)
    proj=pap-0.5*PT*tr[...,None,None]
    zero=k2==0
    if np.any(zero):
        A0=A[zero]
        proj[zero]=A0-(np.trace(A0,axis1=-2,axis2=-1)/3)[:,None,None]*np.eye(3)
    return np.fft.ifftn(proj,axes=(0,1,2)).real


def rms(a):
    return float(np.sqrt(np.mean(np.sum(a*a,axis=(-1,-2)))))


def run(N,alpha,helper=None):
    C,H,L=source_lie_closed(N,alpha)
    P_H=projector_fourier(H)
    Q_L=L-projector_fourier(L)
    ratio=rms(Q_L)/rms(H)
    h=2*np.pi/N
    formula=(math.sin(h)/h)*(1-4*alpha*math.sin(h/2)**2)*math.sqrt(7/8)
    assert abs(rms(H)-1)<1e-12
    assert rms(P_H-H)<1e-12
    assert abs(ratio-abs(formula))<1e-11, (ratio,formula)
    result=dict(N=N, alpha=alpha, q=1, exact_formula=abs(formula), independent_FFT=ratio, delta=abs(ratio-abs(formula)), TT_input_err=rms(P_H-H))
    if helper is not None:
        dx=2*np.pi/N
        EH=helper.apply_E(H,'E_lin',dx,2,alpha)
        Lh=helper.lie_derivative_tensor(C,EH,dx,2)
        Ph=helper.apply_P_TT(H,dx)
        Qh=Lh-helper.apply_P_TT(Lh,dx)
        r_helper=rms(Qh)/rms(H)
        result.update(source_helper_ratio=r_helper, source_helper_diff=abs(r_helper-abs(formula)), Lie_tensor_err=rms(Lh-L), helper_TT_err=rms(Ph-H))
        assert abs(r_helper-abs(formula))<2e-11
        assert rms(Lh-L)<2e-11
    return result


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--helper',default=None,help='Optional retained DTC helper source file')
    p.add_argument('--json',default=None)
    args=p.parse_args()
    helper=None
    if args.helper:
        spec=importlib.util.spec_from_file_location('retained_dtc_helper',args.helper)
        helper=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(helper)
    rows=[]
    for N in (7,9,17,31):
        for alpha in (0.0,0.05,0.2):
            rows.append(run(N,alpha,helper if (N in (9,17,31) and alpha==0.05) else None))
    summary={
        'status':'EXACT_COROLLARY_FROM_INT8_ROT016_EQ_2_3 / INDEPENDENT_FOURIER_VERIFIED / OPTIONAL_RETAINED_HELPER_VERIFIED',
        'fixed_field':'H=diag(1,-1,0)cos(z)',
        'fixed_transport':'C=(sin(x),0,0)',
        'limit_any_fixed_alpha':math.sqrt(7/8),
        'normalized_Hs_to_L2_limit_formula':'sqrt(7/8)*2^(-s/2) for each fixed finite s>=0',
        'witness_source':'retained helper supplied by user, not the byte-exact historical production file',
        'rows':rows
    }
    print(json.dumps(summary,indent=2))
    if args.json:
        Path(args.json).write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':main()
