#!/usr/bin/env python3
"""Geeky-S11 ROT006: all-real-alpha filter-tuning adversarial two-band proof verification.
Dependency: geeky_s11_rot005_quantitative_tt_distance_verify.py (public Github, same folder).
The host is the matched-centered-symbol even-grid projector, not historic DTC raw-k.
"""
import json
import math
from pathlib import Path
import numpy as np
from geeky_s11_rot005_quantitative_tt_distance_verify import (
    EYE, PAIRS, d1, E_alpha, lie, P_delta, norm2_tensor, norm2_vector,
    norm2_scalar, corners)


def q_probes(N,q,oblique=False):
    x=np.meshgrid(*([2*np.pi*np.arange(N)/N]*3),indexing='ij')
    probes=[]
    if not oblique:
        for a in range(3):
            b,c=[i for i in range(3) if i!=a]
            mats=[(np.outer(EYE[b],EYE[b])-np.outer(EYE[c],EYE[c]))/np.sqrt(3),
                  (np.outer(EYE[b],EYE[c])+np.outer(EYE[c],EYE[b]))/np.sqrt(2)]
            for M in mats:
                for f in (np.cos(q*x[a]),np.sin(q*x[a])):
                    probes.append(f[...,None,None]*M)
    else:
        for a,b in PAIRS:
            c=next(i for i in range(3) if i not in (a,b))
            for sigma in (-1,1):
                v=(EYE[a]-sigma*EYE[b])/np.sqrt(2)
                T=np.outer(v,v)-np.outer(EYE[c],EYE[c])
                for f in (np.cos(q*(x[a]+sigma*x[b])),np.sin(q*(x[a]+sigma*x[b]))):
                    probes.append(f[...,None,None]*T)
    return probes


def run():
    rows=[]
    for N in (6,8,10,12):
        h=2*np.pi/N
        sq=lambda q:np.sin(q*h)/h
        a=np.sin(np.pi/N)**2;b=np.sin(2*np.pi/N)**2
        rho=(b-a)/(a+b)
        tests={
            'zero':0.,'native_005':.05,'native_02':.2,
            'axial_q1_zero':1/(4*a), 'axial_q2_zero':1/(4*b),
            'oblique_q1_zero':1/(8*a),'oblique_q2_zero':1/(8*b),
            'axial_minimax':1/(2*(a+b)),'oblique_minimax':1/(4*(a+b)),
        }
        probes_a={q:q_probes(N,q) for q in (1,2)}
        probes_b={q:q_probes(N,q,True) for q in (1,2)}
        # random spatially rough C plus near-kernel and exact kernel controls
        gen=np.random.default_rng(20261024+N)
        noise=gen.normal(scale=.11,size=(N,N,N,3))
        jj=np.indices((N,N,N))
        chi=(-1.)**(jj[0]+jj[1]+jj[2])
        kernel=np.array([.10,-.08,.04])+chi[...,None]*np.array([.08,.13,-.07])
        cases={'generic':kernel+noise,'near_kernel':kernel+1e-3*noise,'kernel':kernel}
        for tag,alpha in tests.items():
            ea={q:1-4*alpha*np.sin(q*np.pi/N)**2 for q in (1,2)}
            eb={q:1-8*alpha*np.sin(q*np.pi/N)**2 for q in (1,2)}
            qa=max((1,2),key=lambda q:abs(ea[q]))
            qb=max((1,2),key=lambda q:abs(eb[q])*sq(q))
            ca=np.sqrt(2/3)*sq(1)*abs(ea[qa])
            cb=np.sqrt(3)*sq(qb)*abs(eb[qb])
            const=min(ca,cb)/np.sqrt(17)
            universal=sq(1)*rho*np.sqrt(2/51)
            assert const+1e-12>=universal,(N,tag,const,universal)
            for kind,C in cases.items():
                coeff,chars=corners(C)
                corner=np.zeros_like(C)
                for m in range(8):corner+=chars[m][...,None]*coeff[m]
                proper=np.zeros_like(C)
                for m in range(1,7):proper+=chars[m][...,None]*coeff[m]
                noncorner=C-corner
                dist2=norm2_vector(noncorner)+norm2_vector(proper)
                D=np.array([d1(C[...,k],j,h) for j in range(3) for k in range(3)]).reshape(3,3,N,N,N)
                S=.5*(D+D.transpose(1,0,2,3,4))
                S=np.moveaxis(S,(0,1),(-2,-1))
                S-=np.trace(S,axis1=-2,axis2=-1)[...,None,None]*EYE/3
                axial_pred=4*ea[qa]**2*norm2_tensor(S)
                W=0.
                for m in range(8):
                    for i,j in PAIRS:
                        if ((m>>i)&1)!=((m>>j)&1):W+=coeff[m,i]**2+coeff[m,j]**2
                oblique_corner_pred=3*eb[qb]**2*sq(qb)**2*W
                atr=0.;obo=0.;inp_mismatch=0.
                for H in probes_a[qa]:
                    inp_mismatch=max(inp_mismatch,math.sqrt(norm2_tensor(H-P_delta(H,h)))/max(1e-15,math.sqrt(norm2_tensor(H))))
                    A=lie(C,E_alpha(H,alpha),h)
                    atr+=norm2_scalar(np.trace(A,axis1=-2,axis2=-1))
                for H in probes_b[qb]:
                    inp_mismatch=max(inp_mismatch,math.sqrt(norm2_tensor(H-P_delta(H,h)))/max(1e-15,math.sqrt(norm2_tensor(H))))
                    A=lie(C,E_alpha(H,alpha),h)
                    obo+=norm2_tensor(A-P_delta(A,h))
                bound=(const**2)*dist2
                witnessed=(atr/3+obo)/17
                # 24-probe aggregate provides lower bound on the true op norm.
                assert atr+3e-10>=axial_pred and abs(atr-axial_pred)<1e-10
                assert obo+3e-10>=oblique_corner_pred
                assert witnessed+3e-10>=bound
                assert inp_mismatch<1e-12
                rows.append(dict(N=N,alpha=alpha,alpha_label=tag,kind=kind,
                                 axial_q=qa,oblique_q=qb,
                                 e_axial=ea[qa],e_oblique=eb[qb],
                                 alpha_independent_floor=universal,
                                 adaptive_constant=const,
                                 L2_distance=np.sqrt(dist2),
                                 axial_trace_energy=atr,axial_trace_pred=axial_pred,
                                 oblique_energy=obo,oblique_corner_pred=oblique_corner_pred,
                                 empirical_24probe_lower=np.sqrt(witnessed),
                                 certificate_lower=const*np.sqrt(dist2),
                                 TT_probe_rel_err=inp_mismatch,
                                 pass_all=True))
            print(f'N={N:2d} {tag:20s} alpha={alpha:11.5g}, bands a{qa}/o{qb}, constant={const:.6g} >= alpha-uniform {universal:.6g}')
    summ=dict(artifact='GEEKY_S11_ROT006_ALL_ALPHA_EVEN_GRID_TT_RIGIDITY_AND_UNIFORM_COERCIVITY_001',
              status='MATHEMATICAL_NUMERIC_PASS_NOT_HISTORICAL_OR_PHYSICAL',
              number_of_cases=len(rows),
              max_abs_axial_frame_error=max(abs(r['axial_trace_energy']-r['axial_trace_pred']) for r in rows),
              maximum_oblique_corner_energy_overshoot=max(r['oblique_corner_pred']-r['oblique_energy'] for r in rows),
              max_TT_input_error=max(r['TT_probe_rel_err'] for r in rows),
              minimum_observed_lower_bound_margin=min(r['empirical_24probe_lower']-r['certificate_lower'] for r in rows),
              cases=rows)
    path=Path(__file__).with_name('geeky_s11_rot006_all_alpha_two_band_results.json')
    path.write_text(json.dumps(summ,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in summ.items() if k!='cases'},indent=2))
    assert len(rows)==4*9*3
if __name__=='__main__':run()
