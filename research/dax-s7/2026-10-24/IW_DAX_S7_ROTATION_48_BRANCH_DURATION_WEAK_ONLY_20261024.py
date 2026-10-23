"""DAX-S7 rotation 48: three-branch durations and neutron weak+decay sensitivity.

Independent surrogate built on rotation 47, NOT Wu--Xu's full Julia executor.
Radiation-dominated, constant-g background with PBH injection; exactly integrated
mass evaporation and comoving-energy injection. Only weak neutron conversions
and free neutron decay; all PBH-hadron exchange terms EXCLUDED.

Run: python IW_DAX_S7_ROTATION_48_BRANCH_DURATION_WEAK_ONLY_20261024.py
Dependencies: numpy, scipy.
"""
import csv
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, minimize_scalar
from scipy.special import beta as beta_func, betainc

OUT = Path(__file__).resolve().parent
MPL_G = 2.176434e-5
TPL_S = 5.391247e-44
GAMMA = 1/(3*math.sqrt(3))
G_RHO_BH_EXTRAP = 104.86508083893959
N_BH = 27*G_RHO_BH_EXTRAP/(4*30720*math.pi)
T_NUC = .07818527068831995
Q_MEV = 939.5654205-938.27208816
TAU_NEUTRON = 878.4
F0 = float(beta_func(1/3,3/2)/3)
CLOCKS = {'g_constant': 205.2044342176343,
          'g_variable_adiabatic_clock': 208.85253295051325,
          'g_variable_code_clock': 214.95558106551593}
BETAS = [1e-17,1e-18,1e-19,1e-20]


def F(y):
    return F0 * (1-float(betainc(1/3,3/2,y*y*y)))


def pb_params(M,b):
    tf=M/MPL_G*TPL_S/GAMMA
    tau=(M/MPL_G)**3*TPL_S/(3*N_BH)
    return tf,tau,b*math.sqrt(tau/tf)


def extrema(M,b):
    tf,tau,eps=pb_params(M,b)
    def injection(y):
        return 2*eps/3*(1-y**3)**1.5/(y*y*(1+eps*F(y)))
    ym=brentq(lambda y:injection(y)-4,1e-9,.9,xtol=1e-15)
    tmin=tau*(1-ym**3)
    lo=tau/math.sqrt(1+eps*F0)
    hi=tmin/math.sqrt(1+eps*F(ym))
    return dict(tf=tf,tau=tau,eps=eps,ym=ym,tmin=tmin,lo=lo,hi=hi)


def window(M,b,tref):
    d=extrema(M,b)
    return d['lo']<tref<d['hi']


def mass_limits(b,tref):
    left=brentq(lambda M: extrema(M,b)['hi']-tref,8.5e9,1e10,xtol=1e-3)
    right=brentq(lambda M: extrema(M,b)['lo']-tref,8.5e9,1e10,xtol=1e-3)
    return left,right


def crossings(M,b,tref):
    d=extrema(M,b)
    if not (d['lo']<tref<d['hi']):
        raise ValueError('Parameters outside three-crossing interval')
    tau,eps,ym=d['tau'],d['eps'],d['ym']
    def q(y):
        return (tref/(tau*(1-y**3)))**2*(1+eps*F(y))
    y1=brentq(lambda y:q(y)-1,ym,.999999999,xtol=1e-14)
    y2=brentq(lambda y:q(y)-1,1e-15,ym,xtol=1e-14)
    t1=tau*(1-y1**3)
    t2=tau*(1-y2**3)
    t3=tref*math.sqrt(1+eps*F0)
    assert t1<d['tmin']<t2<=tau<t3, (M,b,tref,ym,y1,y2,t1,d['tmin'],t2,tau,t3)
    return d,dict(t1=t1,t2=t2,t3=t3,span=t3-t1)


def temp(t,tref,tau,eps):
    if t<tau:
        y=max(0,1-t/tau)**(1/3)
        q=(tref/t)**2*(1+eps*F(y))
    else:
        q=(tref/t)**2*(1+eps*F0)
    return T_NUC*q**.25


def weak_rhs(t,x,tref,tau,eps):
    T=temp(t,tref,tau,eps)
    q=Q_MEV/T
    gamma=255/TAU_NEUTRON*(12+6*q+q*q)/q**5
    return -gamma*(x-(1-x)*math.exp(-q))-x/TAU_NEUTRON


def neutron_test(M,b,tref):
    d,c=crossings(M,b,tref)
    vals={}
    for x0 in [0.,.11,1.]:
        sol=solve_ivp(lambda t,x:[weak_rhs(t,x[0],tref,d['tau'],d['eps'])],
            (c['t1'],c['t3']),[x0],rtol=2e-12,atol=1e-14,dense_output=True,
            max_step=max(.000001,c['span']/80))
        assert sol.success
        values=[float(sol.sol(t)[0]) for t in (c['t1'],c['t2'],c['t3'])]
        vals[str(x0)]={'X_at_crossings':values,'X_delta':values[2]-values[0]}
    # Rigorous conditional absolute weak+decay drift bound for X in [0,1].
    # Tmax is at third crossing or local maximum at PBH exhaustion.
    Tmax=max(T_NUC,temp(d['tau'],tref,d['tau'],d['eps']))
    q=Q_MEV/Tmax
    rate=255/TAU_NEUTRON*(12+6*q+q*q)/q**5
    D=(rate*(1+math.exp(-q))+1/TAU_NEUTRON)*c['span']
    return d,c,vals,D,Tmax


def main():
    lines=[]
    for clock,tref in CLOCKS.items():
        for b in BETAS:
            ml,mr=mass_limits(b,tref)
            def span(frac):
                M=ml+(mr-ml)*frac
                return crossings(M,b,tref)[1]['span']
            opt=minimize_scalar(lambda f:-span(f),bounds=(1e-6,1-1e-6),
                method='bounded',options={'xatol':2e-11})
            fopt=float(opt.x)
            Mopt=ml+(mr-ml)*fopt
            d,c,vals,bound,Tmax=neutron_test(Mopt,b,tref)
            center=neutron_test((ml+mr)/2,b,tref)
            edge=extrema(mr,b)
            def edge_first_cross_eq(y):
                return (1+edge['eps']*F(y))-(1+edge['eps']*F0)*(1-y**3)**2
            y_edge=brentq(edge_first_cross_eq,edge['ym'],.5,xtol=1e-14)
            edge_limit_span_s=edge['tau']*y_edge**3
            assert abs(edge_limit_span_s-c['span']) < max(1e-6,edge_limit_span_s*.00001)
            leading=(2/3)*(d['eps']/6)**1.5
            row=dict(clock=clock,reference_time_s=tref,beta=b,
              mass_lo_g=ml,mass_hi_g=mr,mass_width_g=mr-ml,
              relative_width=(mr-ml)/ml,
              approx_relative_width=(2/3)*(d['eps']/6)**1.5,
              asymptotic_ratio=((mr-ml)/ml)/leading,
              M_max_span_g=Mopt,mass_frac_in_window=fopt,
              tau_evap_s=d['tau'],eps=d['eps'],t_cross1_s=c['t1'],
              t_cross2_s=c['t2'],t_cross3_s=c['t3'],
              max_span_s=c['span'],edge_limit_span_s=edge_limit_span_s,
              edge_y_first_cross=y_edge,
              center_span_s=center[1]['span'],
              X0_011_last_minus_first=vals['0.11']['X_delta'],
              Ystd_011_last_minus_first=2*vals['0.11']['X_delta'],
              Ycode_011_last_minus_first=2*vals['0.11']['X_delta']/
                ((1-vals['0.11']['X_at_crossings'][0])*(1-vals['0.11']['X_at_crossings'][2])),
              X0_0_last_minus_first=vals['0.0']['X_delta'],
              X0_1_last_minus_first=vals['1.0']['X_delta'],
              absolute_weak_only_X_bound=bound,
              max_temperature_MeV=Tmax)
            lines.append(row)
            print(f'{clock:25s} beta={b:.0e} Mwidth={mr-ml:10.3f}g '
                  f'span={c["span"]:.9f}s  dX(0.11)={vals["0.11"]["X_delta"]:.4e}')
    output_csv=OUT/'IW_DAX_S7_ROTATION_48_BRANCH_DURATION_WEAK_ONLY_20261024.csv'
    with output_csv.open('w',newline='',encoding='utf-8') as fh:
        w=csv.DictWriter(fh,fieldnames=list(lines[0]));w.writeheader();w.writerows(lines)
    groups={}
    for clock in CLOCKS:
        rr=[r for r in lines if r['clock']==clock]
        groups[clock]={
            'max_beta_1e_17':next(r for r in rr if r['beta']==1e-17),
            'mass_width_scaling_beta_1e17_to_1e20':[
                (r['beta'],r['mass_width_g']) for r in rr],
            'log_log_exponent':float(np.polyfit(
                np.log10([r['beta'] for r in rr]),
                np.log10([r['mass_width_g'] for r in rr]),1)[0])}
    summary=dict(status='ANALYTICAL_SURROGATE_WITH_WEAK_ONLY_ODE_NOT_FULL_JULIA',
        cross_model='radiation_dominated_constant_g_background_plus_PBH',
        weak_model='Wu-Xu weak rates and neutron decay only, zero PBH hadrons',
        complete_source_grid_triple_crossing_from_rotation47=0,
        tested_calibrations=groups,
        epistemic=['NO_CANON','NO_EXEC_SIGN','NO_PHYSICAL_UPGRADE','NO_PBH_BOUND'],
        source_script='IW_DAX_S7_ROTATION_47_REHEATING_GRID_SURROGATE_20261023.py',
        data_csv=output_csv.name)
    summary_path=OUT/'IW_DAX_S7_ROTATION_48_BRANCH_DURATION_WEAK_ONLY_20261024.json'
    summary_path.write_text(json.dumps(summary,indent=2,ensure_ascii=False),encoding='utf-8')
    print('saved',output_csv.name,summary_path.name)

if __name__=='__main__':main()
