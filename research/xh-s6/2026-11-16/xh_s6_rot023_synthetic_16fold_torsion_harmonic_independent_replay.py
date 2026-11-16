#!/usr/bin/env python3
"""ROT023 synthetic 16-point ring 16th torque harmonic standalone replay.

Original scientific host: An et al., Nat. Commun. (2026)
https://doi.org/10.1038/s41467-026-78187-4 .
The geometry below is INVENTED, not the authors' experiment or alpha bound.
"""
import json, math
import numpy as np

G=6.67e-11
m=7.6e-6
K=16
D=(.654,1.554)
R_LIST=(1.,2.,3.)

def phase_data(radius_mm,gap_mm,phases=8192):
    psi=np.arange(phases)*2*np.pi/phases
    angle=psi[:,None]+np.arange(K)[None,:]*2*np.pi/K
    r=radius_mm*.001
    d=gap_mm*.001
    s=np.sqrt(d*d+2*r*r*(1-np.cos(angle)))
    force=G*m*m*r*r*np.sin(angle)/s**3
    sin16=np.sin(K*psi)
    bnewton=2*np.mean(np.sum(force,axis=1)*sin16)
    return (s,force,sin16,bnewton)

def Q(r,gap,lam,pre):
    s,force,sin16,bnewton=pre
    u=s/(lam*.001)
    b=2*np.mean(np.sum(force*(1+u)*np.exp(-u),axis=1)*sin16)
    return b/bnewton

def maximize(fn):
    a,b=math.log(.05),math.log(20)
    g=(math.sqrt(5)-1)/2
    x=b-g*(b-a);y=a+g*(b-a);fx=fn(math.exp(x));fy=fn(math.exp(y))
    for _ in range(65):
        if fx>fy:
            b,y,fy=y,x,fx;x=b-g*(b-a);fx=fn(math.exp(x))
        else:
            a,x,fx=x,y,fy;y=a+g*(b-a);fy=fn(math.exp(y))
    return math.exp((a+b)/2)

def main():
    expected=((.196783,.356025),(.262065,.309346),(.315920,.293834))
    report=[]
    for r,(want_l,want_c) in zip(R_LIST,expected):
        pair=[phase_data(r,d) for d in D]
        contrast=lambda lam:Q(r,D[0],lam,pair[0])-Q(r,D[1],lam,pair[1])
        L=maximize(contrast);value=contrast(L)
        assert abs(L-want_l)<2e-5 and abs(value-want_c)<2e-5,(r,L,value)
        assert pair[0][3]>0 and pair[1][3]>0
        report.append({'artificial_radius_mm':r,'lambda_shape_max_mm':L,'contrast_peak':value,
                       'model':'synthetic_16fold_classical_torque_NOT_original_apparatus'})
    print(json.dumps({'ROT023_INDEPENDENT_NUMERIC_REPLAY':'PASS','results':report,
                      'source_original_experiment_data_used':False,
                      'NO_NASH_BRIDGE':True},sort_keys=True))
if __name__=='__main__':main()
