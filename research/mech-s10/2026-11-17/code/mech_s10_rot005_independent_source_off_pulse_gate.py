#!/usr/bin/env python3
"""Independent exact + numerical control of the Mech-S10 ROT004 source-off pion tail.

Frozen original Wu-Xu SOURCE constants (public commit d395183, Git blob main
b368ba55d5a493f7bc185909730f7fe5691f10d6 and parameters
0d7198ff3557bdbd5753000bb07a7a7405cc24f5), independently read
through GitHub connector; full upstream file contents not mounted here.

No Julia/BlackHawk/PBH trajectories, no physical Yp/beta result.
"""
import json
import math
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from sympy import symbols, factor, simplify, sqrt, log, diff, exp

C=299792458.0
HBAR=1.054571817e-34
E=1.602176634e-19
MBARN=1e-31
M_PI=139.57039
M_P=938.27208816
ETA=6.1e-10
ALPHA=1/137.035999084
TAU=2.6033e-8
GAMMA=1/TAU
ZETA3=1.2020569031595942854

def author_coeffs(T_MeV, X):
    z=2*math.pi*ALPHA/(math.sqrt(T_MeV/M_PI)+math.sqrt(T_MeV/M_P))
    Fc=z/(-math.expm1(-z))
    n_B=ETA*(2*ZETA3/math.pi**2)*(T_MeV*1e6*E/(HBAR*C))**3
    a=(1-X)*n_B*(1.5*Fc)*MBARN*C/GAMMA
    b=X*n_B*1.7*MBARN*C/GAMMA
    assert Fc>1 and a>0 and b>0
    return a,b,Fc,n_B

def post_integral(a,b,L):
    """gamma*integral P/(S/nB), with L in tau and steady only if L=inf."""
    aa=a/(1+a)**2
    bb=b/(1+b)**2
    if math.isinf(L): return aa-bb
    return aa*(-math.expm1(-(1+a)*L))-bb*(-math.expm1(-(1+b)*L))

def source_on_peak_L(a,b):
    assert a>b>0
    return math.log(a*(1+b)/(b*(1+a)))/(a-b)

def root_L(a,b):
    assert a>b>0 and a*b>1
    m=source_on_peak_L(a,b)
    assert post_integral(a,b,m)>0
    hi=m+1
    while post_integral(a,b,hi)>0: hi=2*hi
    return brentq(lambda L:post_integral(a,b,L),m,hi,xtol=1e-14)

def numeric_full_tail_RK(a,b,L,limit=32):
    """Numerically independently solve charged densities and integral, not formula-fit."""
    if math.isinf(L):
        m0=1/(1+a);p0=1/(1+b)
    else:
        m0=-math.expm1(-(1+a)*L)/(1+a)
        p0=-math.expm1(-(1+b)*L)/(1+b)
    def rhs(t,y):
        return [-(1+a)*y[0],-(1+b)*y[1],a*y[0]-b*y[1]]
    sol=solve_ivp(rhs,(0,limit),[m0,p0,0.],method='DOP853',rtol=2e-13,atol=2e-15)
    assert sol.success
    return sol.y[2,-1],max(abs(sol.y[0,-1]),abs(sol.y[1,-1]))

def max_tail_flip_ab_ratio(T):
    """Maximum AB/gamma^2 over 0<X<1 occurs exactly at X=1/2."""
    a,b,_,_=author_coeffs(T,0.5)
    return a*b

def temperature_critical():
    r=brentq(lambda T:max_tail_flip_ab_ratio(T)-1,1.,10.,xtol=1e-13)
    assert max_tail_flip_ab_ratio(r)<1+1e-12
    assert max_tail_flip_ab_ratio(1.)<1 and max_tail_flip_ab_ratio(10.)>1
    # Exact original Fc(T)=x/(1-exp(-x)), x=k/sqrt(T); derivative dlogFc/dlogT
    # equals -0.5*(1-x/(exp(x)-1)), strictly between -0.5 and 0.
    # Hence T^6*Fc(T) increases strictly for any T>0.
    return r

def x_interval_with_tail_flip(T):
    r=max_tail_flip_ab_ratio(T)
    if r<=1:return None
    x0=(1-math.sqrt(1-1/r))/2
    fc=author_coeffs(T,.5)[2]
    xstar=1.5*fc/(1.5*fc+1.7)
    return {'X_min':x0,'X_max':1-x0,'Xstar_positive_to_negative':xstar,
            'X_window_initial_positive_to_integral_negative':[x0,xstar],
            'X_window_initial_negative_to_integral_positive':[xstar,1-x0]}

def symbolic_audit():
    A,B,G,L=symbols('A B G L', positive=True)
    identity=A/(G+A)**2-B/(G+B)**2-(A-B)*(G**2-A*B)/((G+A)**2*(G+B)**2)
    assert simplify(identity)==0
    Jpulse=A/(G+A)**2*(1-exp(-(G+A)*L))-B/(G+B)**2*(1-exp(-(G+B)*L))
    poststeady=A/(G+A)*exp(-(G+A)*L)-B/(G+B)*exp(-(G+B)*L)
    assert simplify(diff(Jpulse,L)-poststeady)==0
    y=symbols('y',real=True)
    finite_equation=factor(8*(1-y**3)-9*(1-y**2))
    assert simplify(finite_equation+(y-1)*(8*y*y-y-1))==0
    special=float(-log((1+sqrt(33))/16))
    return {'tail_sign_factor_exact': True,'finite_pulse_factorization_exact':True,'duration_derivative_equals_steady_post_stop_RHS_exact':True,'ideal_Lcrit_over_tau':special}

def main():
    symbols_check=symbolic_audit()
    examples=[]
    for name,a,b,L in [('ideal_steady',2.,1.,math.inf),
                         ('ideal_short_pulse',2.,1.,.4),
                         ('ideal_long_pulse',2.,1.,1.3)]:
        closed=post_integral(a,b,L)
        numeric,tail=numeric_full_tail_RK(a,b,L)
        assert math.isclose(closed,numeric,rel_tol=2e-11,abs_tol=4e-12), (name,closed,numeric)
        examples.append({'name':name,'a':a,'b':b,'L_over_tau':L if math.isfinite(L) else 'infinite',
                         'signed_tail_closed':closed,'signed_tail_solved':numeric,'tail_residual_n':tail})
    Tc=temperature_critical()
    assert math.isclose(Tc,4.294807511761707,rel_tol=1e-12)
    assert x_interval_with_tail_flip(1.) is None
    interval5=x_interval_with_tail_flip(5.)
    assert interval5['X_min']<.30<interval5['Xstar_positive_to_negative']
    a,b,fc,n_B=author_coeffs(5.,0.30)
    sharp=root_L(a,b)
    at_peak=source_on_peak_L(a,b)
    steady=post_integral(a,b,math.inf)
    assert a>b>0 and a*b>1 and steady<0
    assert post_integral(a,b,sharp*.7)>0 and post_integral(a,b,sharp*1.5)<0
    val,tail=numeric_full_tail_RK(a,b,math.inf)
    assert math.isclose(steady,val,rel_tol=1e-10,abs_tol=5e-12)
    # Same original source, different X can lead to no negative finite-pulse area
    a2,b2,fc2,n_B2=author_coeffs(1.,.15)
    assert a2>b2>0 and a2*b2<1 and post_integral(a2,b2,math.inf)>0
    for L in (1e-4,.4,1.,10.,100.,math.inf):
        assert post_integral(a2,b2,L)>0
    output={
      'status':'LOCAL_FORMULAS_INDEPENDENT_PYTHON_EXECUTED_SOURCE_CONSTANTS_CHECKED_SEPARATELY',
      'upstream_source_commit':'d395183674cace6c9906a8911bdeb7234ba4040d',
      'upstream_source_blobs':{'main':'b368ba55d5a493f7bc185909730f7fe5691f10d6','params':'0d7198ff3557bdbd5753000bb07a7a7405cc24f5'},
      'provenance':'Original author files read through GitHub connector; this script does not hash full original files; it is an independent mathematical source-constant reproduction only',
      'symbolic':symbols_check,
      'new_necessary_temperature_gate':{
        'Tcritical_MeV':Tc,
        'necessary_for_any_X':'T > Tcritical, because maximum of X(1-X) at X=1/2',
        'max_AB_over_gamma_squared_T1':max_tail_flip_ab_ratio(1.),
        'max_AB_over_gamma_squared_T5':max_tail_flip_ab_ratio(5.),
        'allowed_X_intervals_T5':interval5,
        'proof_monotonicity':'T^6 Fc(T) strictly increasing; dlog Fc/dlogT in (-0.5,0)',
        'scope':'ONLY_FIXED_T_X_NB_SOURCE_PULSE_AND_LOCAL_CAPTURE_RATES'
      },
      'ideal_examples':examples,
      'ideal_steady_cross_over_tau':source_on_peak_L(2.,1.),
      'ideal_Lcrit_from_root_solve':root_L(2.,1.),
      'T5_X0p30':{'Fc':fc,'nB_mminus3':n_B,'a_A_over_gamma':a,'b_B_over_gamma':b,
                 'a_times_b':a*b,'steady_post_integral_over_S_tau_over_nB':steady,
                 'peak_L_over_tau':at_peak,'critical_on_duration_L_over_tau':sharp,
                 'critical_L_seconds':sharp*TAU,
                 'steady_numeric_post_integral':val,'numeric_late_pion_density_max':tail,
                 'short_pulse_area':post_integral(a,b,sharp*.7),'long_pulse_area':post_integral(a,b,sharp*1.5)},
      'T1_X0p15':{'a_A_over_gamma':a2,'b_B_over_gamma':b2,'a_times_b':a2*b2,
                 'steady_post_integral_over_S_tau_over_nB':post_integral(a2,b2,math.inf)},
      'execution_scope':'NO_JULIA_NO_BLACKHAWK_NO_10D_NO_PBH_BOUND_NO_CLAIM_OF_AUTHOR_ERROR'
    }
    print(json.dumps(output,indent=2,sort_keys=True,allow_nan=False))

if __name__=='__main__':main()
