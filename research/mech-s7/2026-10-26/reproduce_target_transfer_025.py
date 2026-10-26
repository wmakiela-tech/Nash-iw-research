#!/usr/bin/env python3
"""Mech-S7 ROT025: cross-map non-transfer of a target-calibrated source moment.

Baseline and conditional dynamics from ROT024, original pinned Wu-Xu archived states.
No original Julia source-valid 10D, no physical PBH or BBN interpretation.
"""
from __future__ import annotations
import argparse,csv,json,math,sys
from pathlib import Path
from scipy.linalg import null_space
from numpy.polynomial.legendre import leggauss
import numpy as np
import reproduce_high_order_moment_gate_024 as m
ROOT=Path(__file__).resolve().parent

# Source comoving moments 0..degree, and one Bexec target moment (i.e. G_exec dot coeff = 0).
# Select normalized null vector from projection of independent Bsym gradient.
def select(degree):
    A=np.vstack([m.M[:degree+1],m.G[0:1]])
    A=A/np.linalg.norm(A,axis=1,keepdims=True)
    N=null_space(A, rcond=1e-13)
    if N.shape[1] < 1: raise ValueError('zero nullspace')
    v=N@(N.T@m.G[1]);norm=np.max(np.abs(v))
    if norm<1e-14:raise ValueError('no cross-target separation')
    v=v/norm
    if m.G[1]@v<0:v=-v
    return v, A, N

DEGREES=(0,2)
CO={j:select(j)[0] for j in DEGREES}

def shape(u,k):
    z=math.log(u)
    for i,(lo,hi) in enumerate(m.BINS):
        if lo<u<hi:return float(CO[k][i]*m.bumpz(z,lo,hi))
    return 0.

def source(u,k,epsilon):
    q=np.array(m.old.source_rates(u,'public','native',.05),dtype=float)
    f=shape(u,k)
    if f!=0.:
        d=epsilon*(q[4]+q[5])*f
        q[4]+=d; q[5]-=d
    if min(q[4],q[5])<=0:raise ValueError('negative antinucleon channel')
    return q

# Target source moment in source-logratio units; exact linearized prediction.
def summary(k):
    c,A,N=select(k)
    return {'matched_log_moments':list(range(k+1)),
            'Bexec_target_moment_matched':True,
            'null_dim':N.shape[1],
            'coeff':c.tolist(),
            'relative_constraint_residual':float(np.linalg.norm(A@c)),
            'source_sum_exact_algebraically':True,
            'linear_Bexec_derivative':float(m.G[0]@c),
            'linear_Bsym_derivative':float(m.G[1]@c),
            'moment_condition':float(np.linalg.cond(A))}

def independent_integral(k):
    c=CO[k]
    XX,WW=leggauss(256)
    per=[]
    for j in range(k+1):
        pieces=[]
        for i,(lo,hi) in enumerate(m.BINS):
            l,h=math.log(lo),math.log(hi)
            z=(h+l)/2+(h-l)/2*XX; weights=(h-l)/2*WW;u=np.exp(z)
            b=np.sin(np.pi*(z-l)/(h-l))**4
            Qsum=m.SQ[0]*u**m.SL[0]+m.SQ[1]*u**m.SL[1]
            pieces.append(float(np.sum(weights*u**3*Qsum*b*c[i]*z**j)))
        per.append({'k':k,'j':j,'residual':sum(pieces),'normalized_residual':float(abs(sum(pieces))/sum(map(abs,pieces)))})
    return per

def run_case(maps,rtol,amp,outprefix='main',degrees=DEGREES,epsilons=None):
    m.source=source
    outputs=[]
    for mp in maps:
        degree_amps={k:(epsilons if epsilons is not None else [-amp,0.,amp]) for k in degrees}
        outputs.extend(m.run_map(mp,degree_amps,rtol))
    # annotate
    for r in outputs:
        mp=r['map'];k=r['moment_degree'];baseline=next(x for x in outputs if x['map']==mp and x['moment_degree']==k and x['epsilon']==0.)
        r['dXnuc']=r['Xnuc']-baseline['Xnuc']
        r['dXcut']=r['Xcut']-baseline['Xcut']
        r['adjoint_prediction']=r['epsilon']*float(m.G[0 if mp=='exec' else 1]@CO[k])
        r['nonlinear_residual']=r['dXnuc']-r['adjoint_prediction']
        r['paper_minus_source']=float(0.4009449678284942-r['Xnuc']) if mp=='exec' else None
    with (ROOT/f'{outprefix}_target_transfer_025.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(outputs[0]));w.writeheader();w.writerows(outputs)
    return outputs

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--amp',type=float,default=.15)
    ap.add_argument('--rtol',type=float,default=3e-9)
    ap.add_argument('--maps',default='exec,sym');ap.add_argument('--outprefix',default='main');ap.add_argument('--degrees',default='0,2');ap.add_argument('--epsilons',default='')
    args=ap.parse_args();maps=args.maps.split(',');degrees=[int(k) for k in args.degrees.split(',')]
    meta={'artifact_id':'MECH-S7-ROT025-TARGET-WEIGHTED-SOURCE-MOMENT-CROSS-MAP-NONTRANSFER-001',
        'source_commit':m.base.UPSTREAM,'source_kernel_from':'ROT021 source-target adjoint, CSV',
        'family':'7 compact sin^4 windows 7e7..9.2e8g; Qp+n constant pointwise; null moments 0..k and Bexec target gradient',
        'amplitude':args.amp,'rtol':args.rtol,'coefficients':[summary(k) for k in degrees],
        'independent_moment_check':[r for k in degrees for r in independent_integral(k)],
        'source_warning':'All below 1e9g source continuations conditional, not Hawking validated'}
    epsilons=[float(x) for x in args.epsilons.split(',')] if args.epsilons else None
    results=run_case(maps,args.rtol,args.amp,args.outprefix,degrees=degrees,epsilons=epsilons)
    meta['cases']=results
    (ROOT/f'{args.outprefix}_target_transfer_025.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
    print('RESULT',json.dumps({'coefficients':meta['coefficients'],'independent_moments':meta['independent_moment_check'],
                                 'responses':[{'map':x['map'],'k':x['moment_degree'],'eps':x['epsilon'],'dX':x['dXnuc'],'adj':x['adjoint_prediction'],'nonlinear':x['nonlinear_residual']} for x in results]},indent=2),flush=True)

if __name__=='__main__':main()