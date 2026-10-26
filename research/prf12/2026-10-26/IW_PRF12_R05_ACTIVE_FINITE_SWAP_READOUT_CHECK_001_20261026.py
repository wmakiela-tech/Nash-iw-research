#!/usr/bin/env python3
"""PRF12 R05 finite-pulse readout check; requires adjacent R04 reproduction source.
Neither the product-basis search nor separable POVM establishes LOCC optimality.
"""
import argparse,importlib.util
from pathlib import Path
from math import pi
import numpy as np
from scipy.optimize import differential_evolution
parser=argparse.ArgumentParser()
parser.add_argument('--cut',type=float,default=30000.)
parser.add_argument('--step',type=float,default=.3)
parser.add_argument('--search',action='store_true')
args=parser.parse_args()
src=Path(__file__).with_name('IW_PRF12_R04_THREE_PROBE_ACTIVE_SWAP_AND_X_MEASUREMENT_REPRO_001_20261026.py')
if not src.exists():
    raise FileNotFoundError('R04 Python source required in same directory: '+str(src))
spec=importlib.util.spec_from_file_location('prf12_r04',str(src))
r04=importlib.util.module_from_spec(spec);spec.loader.exec_module(r04)
bits=r04.bits
W=(bits.sum(axis=1)==1).astype(float)/np.sqrt(3)
Wb=(bits.sum(axis=1)==2).astype(float)/np.sqrt(3)
P0=np.zeros((8,8));P0[0,0]=P0[7,7]=1
Eplus=np.outer(W,W)+np.outer(Wb,Wb)+P0/3
def local(theta,phi):
    c,s=np.cos(theta/2),np.sin(theta/2);z=np.exp(1j*phi)
    return np.array(((c,-z.conjugate()*s),(z*s,c)))
def product_tv(D,angles):
    U=np.kron(np.kron(local(*angles[:2]),local(*angles[2:4])),local(*angles[4:6]))
    return np.abs(np.diag(U.conj().T@D@U).real).sum()/2
for fr,k in (([1/3]*3,.3),([1/3]*3,5.),([.55,.30,.15],.3),([.55,.30,.15],5.)):
    A,tail=r04.A(fr,k,cut=args.cut,step=args.step)
    B=r04.B(fr,k)
    D=(A-B+(A-B).conj().T)/2
    hel=np.abs(np.linalg.eigvalsh(D)).sum()/2
    x=r04.metrics(A,B)[1]
    sep=abs(np.trace(Eplus@D))
    print('CONFIG',fr,'kappa',k,'TV_H',hel,'TV_X',x,
          'TV_SEP28',sep,'Cauchy_tail_TV_bound',tail,flush=True)
    if args.search:
        out=differential_evolution(lambda p:-product_tv(D,p),
           [(0,pi),(0,2*pi)]*3,seed=42,maxiter=150,popsize=9,tol=1e-9)
        print('UNCERTIFIED_PRODUCT',-out.fun,out.x,flush=True)
