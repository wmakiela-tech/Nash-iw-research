#!/usr/bin/env python3
"""DAX-S7 R50: source-background + source weak-only neutron equation.

Reads ORIGINAL three thermodynamics tables using R49's pinned-blobs loader.
Does not execute Julia; excludes PBH hadron reactions. Uses high-resolution RK4
for background and exact midpoint propagation for the affine weak n<->p ODE.

Examples:
  python IW_DAX_S7_ROTATION_50_WEAK_BRANCH_SAMPLED_YN_20261024.py --selftest
  python IW_DAX_S7_ROTATION_50_WEAK_BRANCH_SAMPLED_YN_20261024.py --data-dir ./dax_s7_wuxu_source_tables --n-pre 20000 --n-evap 24000
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
from typing import Any

from IW_DAX_S7_ROTATION_49_SOURCE_BACKGROUND_TRIPLE_CROSSING_20261024 import (
    WuXuThermodynamics, MP_G, TPL_S, GAMMA, HCOEFF, T_NUC,
    SOURCE_FILES, git_blob_sha,
)

Q_MEV = 939.5654205 - 938.27208816
TAU_NEUTRON_S = 878.4


def neutron_eq(T: float) -> float:
    z = Q_MEV / T
    return 1 / (1 + math.exp(z)) if z < 700 else 0.0


def weak_advance(X: float, t0: float, t1: float, T0: float, T1: float,
                 init_temperature: float = 5.0) -> float:
    """Exact relaxation for midpoint piecewise-constant weak rates.

    For T>5 MeV, Xn is reset to instantaneous equilibrium; this is a
    controlled high-temperature approximation, NOT identical to full source
    initial integration at Tf.
    """
    if T1 >= init_temperature:
        return neutron_eq(T1)
    if T0 > init_temperature:
        f = ((math.log(init_temperature) - math.log(T0)) /
             (math.log(T1) - math.log(T0)))
        t0 += (t1-t0)*f
        T0 = init_temperature
        X = neutron_eq(init_temperature)
    Tmid = math.sqrt(T0*T1)
    z = Q_MEV/Tmid
    gamma_weak = (255/TAU_NEUTRON_S) * (12+6*z+z*z) / (z**5)
    u = math.exp(-z)
    rate = gamma_weak*(1+u) + 1/TAU_NEUTRON_S
    steady = gamma_weak*u/rate
    return steady+(X-steady)*math.exp(-rate*(t1-t0))


def simulate(tables: Any, mass_g: float = 9.6725e9,
             beta: float = 1e-17, n_pre: int = 10000,
             n_evap: int = 12000, n_post: int = 10000,
             stored_nodes: int = 10000) -> dict:
    tf = mass_g/MP_G*TPL_S/GAMMA
    nb = tables.n_bh
    tau = (mass_g/MP_G)**3 * TPL_S/(3*nb)
    Tf = math.sqrt(1/(2*tf*HCOEFF*math.sqrt(tables.g_top)))
    Lf = math.log(tables.g_top)+4*math.log(Tf)
    # Same formula as source a_end, with a_f=1.
    aend_log = (math.log(10)+math.log(tables.g_top/tables.g_rho(T_NUC))/3
                +math.log(Tf/T_NUC))
    L, A, X = Lf, 0.0, neutron_eq(Tf)
    hist: list[tuple[float,float,float,float]] = [(0.0,tf,Tf,X)]
    crossings = []
    def bg(l:float,a:float,y:float):
        temp = tables.T_from_lnrho(l)
        _, r, s = tables.thermo(temp)
        ratio0 = beta*math.exp(Lf-l-3*a)
        H = HCOEFF*math.exp(l/2)*math.sqrt(1+ratio0*y)
        c = -4+r/(3+s)
        return temp,H,ratio0,c
    def rk4(z:float,h:float,fun):
        nonlocal L,A
        d1=fun(z,L,A)
        d2=fun(z+h/2,L+h*d1[0]/2,A+h*d1[1]/2)
        d3=fun(z+h/2,L+h*d2[0]/2,A+h*d2[1]/2)
        d4=fun(z+h,L+h*d3[0],A+h*d3[1])
        L += h*(d1[0]+2*d2[0]+2*d3[0]+d4[0])/6
        A += h*(d1[1]+2*d2[1]+2*d3[1]+d4[1])/6
    def record(time:float,stage:str):
        nonlocal X
        temp=bg(L,A,0)[0]
        aa,old_time,old_temp,old_X=hist[-1]
        X=weak_advance(X,old_time,time,old_temp,temp)
        hist.append((A,time,temp,X))
        p=math.log(old_temp/T_NUC)
        q=math.log(temp/T_NUC)
        if p*q<0:
            w=p/(p-q)
            crossings.append({'time_s':old_time+w*(time-old_time),
                              'log_a':aa+w*(A-aa),
                              'Xn':old_X+w*(X-old_X),
                              'direction':'heating' if q>p else 'cooling',
                              'phase':stage})
    # First phase: x=ln(t/tf) until y=M/Mf=1/2.
    end_x=math.log((tf+tau*(1-0.5**3))/tf)
    hx=end_x/n_pre
    for i in range(n_pre):
        def f1(z,l,a):
            t=tf*math.exp(z)
            y=max(1e-40,1-(t-tf)/tau)**(1/3)
            _,H,B,C=bg(l,a,y)
            return (t*(H*C+B/(3*tau*y*y)),t*H)
        rk4(i*hx,hx,f1)
        record(tf*math.exp((i+1)*hx),'pre')
    # Second phase: independent variable remaining mass fraction y from .5 to 0.
    hy=-0.5/n_evap
    for i in range(n_evap):
        def f2(y,l,a):
            _,H,B,C=bg(l,a,y)
            return (-3*tau*y*y*H*C-B, -3*tau*y*y*H)
        rk4(0.5+i*hy,hy,f2)
        y_end=max(0.0,0.5+(i+1)*hy)
        record(tf+tau*(1-y_end**3),'evap')
    T_evap=bg(L,A,0)[0]
    # Third phase: expand after evaporation. Stop just below T_nuc.
    hpost=math.log(400/(tf+tau))/n_post
    for i in range(n_post):
        def f3(z,l,a):
            t=(tf+tau)*math.exp(z)
            _,H,_,C=bg(l,a,0)
            return (t*H*C,t*H)
        rk4(i*hpost,hpost,f3)
        record((tf+tau)*math.exp((i+1)*hpost),'post')
        if hist[-1][2]<0.060:
            break
    # Mimic source's uniform geomspace(a_f, a_end, 10000).
    hgrid=aend_log/(stored_nodes-1)
    k=0
    sampled=[]
    for i in range(stored_nodes):
        target=i*hgrid
        if target>hist[-1][0]: break
        while k+1<len(hist)-1 and hist[k+1][0]<target: k+=1
        a0,t0,T0,X0=hist[k]
        a1,t1,T1,X1=hist[k+1]
        f=(target-a0)/(a1-a0)
        temp=T0+f*(T1-T0)
        sampled.append({'log_a':target,'t_s':t0+f*(t1-t0),
                        'x':Q_MEV/temp,'Xn':X0+f*(X1-X0)})
    sampled.sort(key=lambda z:z['x'])  # source's sortperm(Q ./ T_SM_list)
    x_target=Q_MEV/T_NUC
    lo,hi=0,len(sampled)-1
    assert sampled[lo]['x']<x_target<sampled[hi]['x'], 'target not bracketed'
    while hi-lo>1:
        mid=(lo+hi)//2
        if sampled[mid]['x']<x_target:lo=mid
        else:hi=mid
    left,right=sampled[lo],sampled[hi]
    w=(x_target-left['x'])/(right['x']-left['x'])
    Xsample=left['Xn']+w*(right['Xn']-left['Xn'])
    nearest_true= [dict(c,difference_Xn=Xsample-c['Xn']) for c in crossings]
    spans=[c['log_a'] for c in crossings]
    return {
        'status':'BACKGROUND_SOURCE_EQUATIONS_WEAK_ONLY_NO_HADRONS_NO_JULIA',
        'mass_g':mass_g,'beta':beta,'T_nuc_MeV':T_NUC,
        'weak_start_T_MeV':5.0,'steps_pre':n_pre,
        'steps_evap':n_evap,'steps_post':n_post,
        'tau_evap_s':tau,'T_at_evap_MeV':T_evap,
        'crossings':nearest_true,'sparse_Xn':Xsample,
        'sparse_source_Yp_formula':2*Xsample/(1-Xsample),
        'sparse_standard_Yp_approx':2*Xsample,
        'sample_bracket':[left,right],
        'samples_actually_computed':len(sampled),
        'log_a_grid_step':hgrid,
        'crossing_log_a_span':max(spans)-min(spans) if spans else None,
        'no_samples_inside_crossing_span':(
            not any(min(spans)<s['log_a']<max(spans) for s in sampled)
            if len(spans)>1 else None),
        'source_full_Julia_run':False,
        'source_hadronic_neutron_rates_enabled':False,
        'source_background_tables_reconstructed':True,
    }


class Flat:
    g_top=10.75
    n_bh=(27/4)*g_top/(30720*math.pi)
    def g_rho(self,T):return self.g_top
    def thermo(self,T):return self.g_top,0.0,0.0
    def T_from_lnrho(self,L):return math.exp((L-math.log(self.g_top))/4)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--data-dir',type=Path)
    ap.add_argument('--selftest',action='store_true')
    ap.add_argument('--mass',type=float,default=9.6725e9)
    ap.add_argument('--beta',type=float,default=1e-17)
    ap.add_argument('--n-pre',type=int,default=10000)
    ap.add_argument('--n-evap',type=int,default=12000)
    ap.add_argument('--n-post',type=int,default=10000)
    ap.add_argument('--stored-nodes',type=int,default=10000)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    if args.selftest:
        r=simulate(Flat(),mass_g=9.6725e9,beta=0,n_pre=2000,n_evap=2000,n_post=3000)
        assert len(r['crossings'])==1,r
        assert 0<r['sparse_Xn']<.5,r
        assert not r['crossings'][0]['difference_Xn']>1e-2,r
        print('PASS constant-g no-PBH: one T_nuc crossing, 0<Xn<0.5')
        return
    if args.data_dir is None:ap.error('--data-dir is required outside --selftest')
    for fname,expected in SOURCE_FILES.items():
        path=args.data_dir/fname
        if git_blob_sha(path.read_bytes())!=expected:
            raise RuntimeError('Source blob mismatch: '+fname)
    tables=WuXuThermodynamics(args.data_dir)
    r=simulate(tables,args.mass,args.beta,args.n_pre,args.n_evap,args.n_post,args.stored_nodes)
    output=json.dumps(r,indent=2,ensure_ascii=False)
    if args.output:args.output.write_text(output+'\n',encoding='utf8')
    print(output)


if __name__=='__main__':main()
