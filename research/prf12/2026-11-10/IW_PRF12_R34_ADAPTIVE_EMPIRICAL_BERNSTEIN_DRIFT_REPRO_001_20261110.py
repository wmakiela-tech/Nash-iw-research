#!/usr/bin/env python3
"""PRF12 R34. Adaptive within-epoch reference stopping for a drifting Bernoulli detector.

MAIN: self-contained statistical proof witness with predeclared finite lambda grid,
nonstationary conditional-mean E-Bernstein e-process, physically ordered timestamps,
source-A/B transfer from PREVIOUSLY CERTIFIED R31 all-real-Xi comparator, exact
integer binomial tails, and a strictly synthetic, reproducible drift path.

NOT a hardware calibration. NO_CANON/EXEC/NOVELTY; 3q original LOCC remains OPEN.
Python 3, NumPy. Optional SciPy only for double-checking binomial results.
"""
import json, math, argparse, hashlib
from pathlib import Path
import numpy as np

A0 = 0.3106993896688963
B0 = 0.27161358975207756
S = .18*1 + .20*1 + .62*.347
PSTAR = (.99, 3705/69000)
NU = 1e-8
REF_TIME = .1
PAIR_TIME = 1.8283185307179588
SCI_PER_EPOCH = 4750
ALPHA_CAL = .01
LAMBDA_GRID = (.06,.085,.12,.17,.24,.34,.48,.68)
PSI = tuple(-math.log1p(-x)-x for x in LAMBDA_GRID)
ALPHA_SCI = .04
A_SAFE, B_SAFE = .2995, .2828
N_SCI, K_THRESHOLD = 9500, 2765
TOLERANCE = min((A0-A_SAFE)/(2*S),(B_SAFE-B0)/(2*S))
SYNTHETIC_SEED = 20261110  # predeclared fixture only, NOT a measured sample

def true_synthetic_p(arm, gamma_t):
    # Rates: 3e-5/4000=7.5e-9, 2.5e-5/3800=6.579e-9 < NU
    if arm==0:
        return PSTAR[0] + 3e-5*math.sin(gamma_t/4000)
    return PSTAR[1] + 2.5e-5*math.cos(gamma_t/3800)

def reference_radius(n, observed_V, epoch):
    if n==0:return math.inf
    L=math.log(4*len(LAMBDA_GRID)*epoch*(epoch+1)/ALPHA_CAL)
    return min((L+psi*observed_V)/(lam*n)
               for lam,psi in zip(LAMBDA_GRID,PSI))

def exact_cdf(n,k,p_num,p_den):
    assert 0<=k<n and 0<p_num<p_den
    term=pow(p_den-p_num,n);total=term
    for i in range(k):
        term,rem=divmod(term*(n-i)*p_num,(i+1)*(p_den-p_num))
        assert rem==0
        total+=term
    return total,pow(p_den,n)

def exact_binomial_cert():
    # Rational safe bounds .2995=599/2000, .2828=707/2500.
    FA,DA=exact_cdf(N_SCI,K_THRESHOLD-1,599,2000)
    CB,DB=exact_cdf(N_SCI,K_THRESHOLD-1,707,2500)
    assert 25*FA<DA and 25*(DB-CB)<DB
    return {'N':N_SCI,'K':K_THRESHOLD,
            'false_B_under_A':FA/DA,'false_A_under_B':(DB-CB)/DB,
            'per_hypothesis_total_including_calibration':
            [FA/DA+ALPHA_CAL,(DB-CB)/DB+ALPHA_CAL],
            'exact_integer_4_percent_checks':'PASS'}

def run(seed=SYNTHETIC_SEED, verbose=False):
    rng=np.random.default_rng(seed)
    now=0.0
    epochs=[]
    for epoch in (1,2):
        n=[0,0];k=[0,0]; V=[0.,0.];time_sum=[0.,0.]
        max_ref=150000
        def status(arm,science_end):
            if n[arm]==0:
                return {'delta':math.inf,'radius':math.inf,'bias':math.inf,'drift':math.inf}
            rad=reference_radius(n[arm],V[arm],epoch)
            deviation=abs(k[arm]/n[arm]-PSTAR[arm])
            # All reference timestamps precede science; science_end is max future timestamp.
            drift=NU*(science_end-time_sum[arm]/n[arm])
            return {'delta':rad+deviation+drift, 'radius':rad,
                    'bias':deviation, 'drift':drift}
        for step in range(max_ref):
            science_end=now+SCI_PER_EPOCH*PAIR_TIME
            s=[status(i,science_end) for i in range(2)]
            if max(v['delta'] for v in s)<=TOLERANCE:
                # Crucial: these are calculated BEFORE any next outcome.
                result={
                    'epoch':epoch,'ref_counts':n[:],'ref_positive_counts':k[:],
                    'ref_reads':sum(n),'ref_radius':[v['radius'] for v in s],
                    'empirical_deviation':[v['bias'] for v in s],
                    'Lipschitz_time_budget':[v['drift'] for v in s],
                    'effective_delta':[v['delta'] for v in s],
                    'max_delta':max(v['delta'] for v in s),
                    'stopping_time_reference_gamma':now,
                    'science_end_gamma':science_end,
                    'science_pairs':SCI_PER_EPOCH,
                    'alpha_epoch':ALPHA_CAL/(epoch*(epoch+1)),
                    'observed_quadratic_V':V[:],
                }
                # True synthetic path verifies within the statistical guarantee
                # as a fixture, NOT a certificate of typical performance.
                tchecks=np.linspace(now,science_end,51)
                result['fixture_true_max_detector_deviation']=max(
                    abs(true_synthetic_p(i,float(t))-PSTAR[i])
                    for i in range(2) for t in tchecks)
                assert result['fixture_true_max_detector_deviation']<result['max_delta']
                assert result['max_delta']<=TOLERANCE
                epochs.append(result)
                now=science_end
                break
            # Predictable arm allocation: sample the arm with the worse current
            # certified error budget, using no future/current unobserved result.
            arm=1 if s[1]['delta']>s[0]['delta'] else 0
            q=(k[arm]+50*PSTAR[arm])/(n[arm]+50)
            midpoint=now+REF_TIME/2
            x=int(rng.random()<true_synthetic_p(arm,midpoint))
            V[arm]+=(x-q)**2
            n[arm]+=1;k[arm]+=x;time_sum[arm]+=midpoint
            now+=REF_TIME
        else:
            raise RuntimeError('calibration ABSTAIN: no finite successful stopping at cap')
    exact=exact_binomial_cert()
    ref_readouts=sum(x['ref_reads'] for x in epochs)
    refs_fixed_R33=230000
    out={
      'rotation':'PRF12_R34','timestamp':'2026-11-10',
      'model':'pathwise Lipschitz nonstationary p0(t), p1(t), R31 inherited all-Xi source',
      'synthetic_seed':seed,'synthetic_only':True,
      'lambda_grid':LAMBDA_GRID,'predictor':'sequential Laplace pseudo-count 50, predictable',
      'nu_per_gamma_time':NU,'alpha_cal':ALPHA_CAL,
      'tolerance_to_preserve_R33_a_b':TOLERANCE,
      'source_score_sensitivity_S':S,
      'reference_epochs':epochs,
      'source_test':exact,
      'total_reference_reads':ref_readouts,
      'total_science_pairs':N_SCI,
      'total_single_sensor_reads':ref_readouts+2*N_SCI,
      'total_wall_gamma':now,
      'fixed_R33_reference_reads':refs_fixed_R33,
      'fixed_R33_total_reads':249000,
      'fixed_R33_wall_gamma':40369.02604182061,
      'percent_reduction_ref_reads':100*(1-ref_readouts/refs_fixed_R33),
      'percent_reduction_all_reads':100*(1-(ref_readouts+19000)/249000),
      'percent_reduction_wall_gamma':100*(1-now/40369.02604182061),
      'claim_ceiling':'SYNTHETIC_ONLY / STATIONARITY_NOT_ASSUMED / EXOGENOUS_NU / SOURCE_R31_INHERITED / CONDITIONAL_DETECTOR_INDEPENDENCE / NO_CANON / NO_EXEC / NO_ORIGINAL_3Q_LOCC_CLOSURE'
    }
    assert len(epochs)==2
    assert max(x['max_delta'] for x in epochs)<TOLERANCE
    assert now<40369.02604182061
    if verbose: print(json.dumps(out,indent=2))
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--seed',type=int,default=SYNTHETIC_SEED)
    p.add_argument('--output')
    opts=p.parse_args()
    result=run(opts.seed)
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if opts.output:Path(opts.output).write_text(text)
    else:print(text,end='')
