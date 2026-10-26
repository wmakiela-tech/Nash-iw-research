artifact_id: MECH-S7-FRONTB-BASIS-ENLARGEMENT-FINITE-OBSERVATION-NULLSPACE-030_20261026
exposure: PUBLIC
claim_ceiling: EXECUTED_CONDITIONAL_FINITE_SOURCE_BASIS_NULLSPACE_AND_NONLINEAR_COUNTERCHECK
sync_state: GITHUB_PENDING_BW_INGEST

# Mech-S7 ROT030 — finite observation nullspace reappears on enlarging the antinucleon source basis

**Date:** 2026-10-26. **Cell:** IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7. **Return:** MECH-S7-FRONTB-SOURCE-BASIS-DIMENSION-AND-NONLINEAR-C2-GATE-030_20261026.

**Scientific claim ceiling:** rigorous 11-variable/9-functional linear dimension bound; actual executed numerical conditional source-inspired bridge plus 7D kinetics for a particular smooth synthetic source. **Not** source-validated Hawking hadrons below 1e9 g, original Wu–Xu Julia 10D, genuine BBN Yp/DH, PBH bounds, novelty, canonical adoption or EXEC.

## 1. Upstream and prior-work subtraction

Original upstream source: Fenyutanchan/Primordial-Black-Hole pinned commit `d395183674cace6c9906a8911bdeb7234ba4040d`; `arXiv-2509.05618/main-scan.jl` at blob `b368ba55d5a493f7bc185909730f7fe5691f10d6` and original `data/out/hadrons_from_PBH.dat` at blob `06d0883a27b108692720422294ba2baacd381a64`. Hadron-rate table has **no** calibrated mass nodes below `1e9 g`. The public implementation extrapolates separate hadronic rate columns log-linearly below the first tabulated mass node. There is no original Julia 10D execution in this rotation.

Dependencies carried forward: ROT013 corrected source-active preedge 10-component bridge; ROT020 pair-sum-conserving sign falsifier; ROT021 final-Xn adjoint mass kernel; ROT023–024 individual antinucleon moment matching; ROT026–027 target- and host-dependent source sufficiency failure; ROT028 numerical six-host/full-rank **seven-bin** test and better-conditioned nonlinear heldout response; ROT029 kernel-error stability and uncertainty warning. Finite rank/nullity and target-relative sufficiency are **mature elementary linear algebra and inverse-problem host**, not novel mathematical claims (cross-cell MT/NC/PRF/LT prior art).

**Precise correction:** ROT028's `rank 4 of 4`, and hence lack of common exact linear null in its moment-constrained seven-bin parameterization, **must not be generalized to smooth source functions outside that finite space**. This rotation verifies a separate larger admissible source space.

## 2. Construction and exact statement

Set `u=M/(1e9 g)`, log mass `z=ln u`; support within `7e7 <= M <= 9.2e8 g`. Split logarithmically into eleven disjoint intervals `[u_i,u_(i+1)]`. Each basis function is `phi_i(z)=sin^4(pi*(z-z_i)/(z_(i+1)-z_i))` on its own interval, zero outside. Functions are nonnegative, C^3 across interval endpoints, with untouched source rates and jets at the upstream `1e9 g` boundary.

For coefficients c_i and any allowed amplitude epsilon, redistribute source rates:

`Qpbar_new=Qpbar_native+epsilon*(Qpbar_native+Qnbar_native)*h(z)`;
`Qnbar_new=Qnbar_native-epsilon*(Qpbar_native+Qnbar_native)*h(z)`;
`h(z)=sum_i c_i*phi_i(z)`.

Pointwise pair sum is **identical** for every mass. The original source rates for all other species are unchanged. For each antinucleon, constrain three comoving source moments `L_j(h)=integral u^3 (Qpbar+Qnbar) h(z) z^j dz=0`, j=0,1,2. Add six final-Xn first-order target constraints for `chi_EM=0.25,0.5,0.75` by two reaction maps (`B_exec`,`B_sym`), supplied by ROT021/028 actual forward/backward adjoints.

There are **nine scalar linear functionals on eleven coefficients**, so rank-nullity guarantees `dim ker >= 2`, regardless of conditioning or functional independence. The numerical 9×11 sampled matrix yielded a two-dimensional SVD nullspace with normalized maximum residual 6.418e-17. This **is not** a global exact nonlinear kinetic invariance theorem. The *particular coefficient vector* is chosen deterministically by projecting a fixed trigonometric vector onto the sampled nullspace; no held-out chi0/chi1 targets participated in selection.

Its nine nonzero singular values under row normalization are `2.855e+00, 9.057e-01, 1.701e-01, 6.945e-03, 9.409e-04, 1.496e-06, 5.668e-08, 3.142e-11, 1.846e-11`. The two smallest are approximately `3.14e-11` and `1.85e-11`, so the numerical rank `9` is not an independently physically certifiable source-rank finding. **The rigorous claim is dim null >= 2**, not that all nine physical derivatives are independent.

Independent Gauss256/source and tighter-rtol ROT028 host kernels checked: maximal relative source and adjoint constraint discrepancy `6.376e-12` (the latter depends on the discretely sampled, interpolated kernel, not certified continuous adjoints). The exact sum holds algebraically; in 20001-point Float64 control relative numerical pair-sum residual max `2.22e-16`; minimum individual source channel share `0.3512 >0` at epsilon ±0.15.

## 3. Executed conditional ODE tests: 30 baseline/amplitude solves

The same original source-active preedge bridge followed by seven hadronic/neutron variables to a fixed nucleosynthesis temperature. χEM values `(0, 0.25, 0.5, 0.75, 1)`; both `B_exec/B_sym`; epsilon `0, +0.15, -0.15`. For ±0.15 the following table lists maximum abs target changes and even second-order parts (mean of ± responses):

| chi EM | Map | max abs Delta Xnuc | even (Delta Xplus + Delta Xminus)/2 |
|---:|:---:|---:|---:|
| 0.00 | `exec` | 6.228051e-11 | -6.206824e-11 |
| 0.00 | `sym` | 2.441386e-11 | -2.413209e-11 |
| 0.25 | `exec` | 6.375622e-11 | -6.301012e-11 |
| 0.25 | `sym` | 2.458866e-11 | -2.455114e-11 |
| 0.50 | `exec` | 6.221390e-11 | -6.184289e-11 |
| 0.50 | `sym` | 2.447403e-11 | -2.426895e-11 |
| 0.75 | `exec` | 6.069723e-11 | -6.041845e-11 |
| 0.75 | `sym` | 2.464168e-11 | -2.440909e-11 |
| 1.00 | `exec` | 6.128081e-11 | -6.088835e-11 |
| 1.00 | `sym` | 2.409278e-11 | -2.408529e-11 |

The six fitted host backgrounds are χ=`.25,.5,.75` across both maps. The `0,1` rows are completely held out at source-direction construction. **The reported nonzero response is allowed by second and higher orders in epsilon**. Vanishing of the linear functional does not imply equality of finite-amplitude trajectories; cut-time Xn changes are not necessarily small even when final Xn changes are.

## 4. Heldout comparison against ROT028 with no source-amplitude shrinkage

Compare against ROT028's robust seven-window direction at the **same epsilon ±0.15**. The seven-window function has comoving source-weighted RMS `0.131893`; new eleven-window direction `0.147888` (12.13% larger). Maximum |ln((Qp/Qn)_new/(Qp/Qn)_native)| at this amplitude is `0.6186` versus old `0.6195`; source reallocation is **not vanishingly small**. Thus any improvement in final-Xn contrast does not follow merely from using a smaller perturbation under these reported source metrics.

| Heldout chi EM | Map | Improvement in maximum abs Delta Xnuc, old/new | even-response factor epsilon .15/.075 | max abs tight-rtol Delta discrepancy |
|---:|:---:|---:|---:|---:|
| 0% | `exec` | 4.117× | 3.950× | 9.051e-13 |
| 0% | `sym` | 5.619× | 3.882× | 9.922e-13 |
| 100% | `exec` | 3.816× | 3.997× | 3.164e-13 |
| 100% | `sym` | 6.175× | 4.003× | 1.477e-13 |

The factor close to `4` under amplitude halving supports quadratic dominance for the tested range; not an exact or globally certified second-order Taylor theorem. New heldout response remains nonzero; at chi=0, exec max `6.2281e-11`; at chi=1, sym max `2.4093e-11`. The base/tight-rtol differences are `1e-12` or smaller. Target differences far below physical modeling systematics are **not physical precision claims**.

## 5. Kernel-error and nonlinear-higher-order limits

ROT029 warned that an ill-conditioned observation matrix can give unreliable directional detail under model error. Here using independent Gauss256/`tight` ROT028 χ.25/.75 adjoint kernels in place of base kernels rotates this particular projected source direction **3.85834 degrees**. New direction nevertheless gave comparably small heldout nonlinear residuals after complete fresh χ=0/1, map exec/sym Radau ODE. But no error bound for physical source gradients M<1e9g is available. There is **no validated orientation of the exact physical near-null** from this work.

The two-dimensional null space is defined for a **finite matrix assembled from stored/interpolated adjoint kernels**. It is not a closed-form null for exact 10D Wu–Xu kinetics. In an infinite-dimensional smooth-source class, finitely many linear observations cannot uniquely identify the full source; this generality is elementary, and its interpretation may be limited by physically admissible source constraints (positivity alone does not validate arbitrary spectra).

## 6. Independent reproducibility/integrity

Executed default Radau rtol `3e-9`, and an independent set of twelve heldout ODE states at `3e-10` for χ=0/1 and both maps. Executed twelve more at epsilon `±0.075` and four cases times three states using an alternative direction from tighter adjoints. Clean isolated replay of chi0/Bexec three states with raw input-only dependencies produced **exactly identical stored Xnuc, Xcut, dXnuc, dXcut and accepted step counts**. Replay diagnostic: `{"replay": "PASS", "case": "chi0 Bexec eps 0,+0.15,-0.15", "max_abs_difference": 0.0, "n": 3, "solver": "3.13.5"}`.

Executable scripts in attached ZIP: `build_multibin_null_030.py`, `test_multibin_ode_030.py`, `source_size_and_tolerance_030.py`, `tight_kernel_direction_030.py`, `verify_clean_replay_030.py`. It additionally preserves source-active bridge, early EOS and source host dependencies and both raw Mech-S6 archives. `README_REPRODUCE_030.md` gives complete commands. CSV/JSON outputs and SHA256 manifest included.

## 7. Claim gates and next decisive test

- `FINITE_11_BASIS_9_LINEAR_FUNCTIONALS_NULL_DIM_GE_2 = EXACT_LINEAR_ALGEBRA`
- `ELEVEN_BIN_POSITIVE_C3_SOURCES_MOMENTS0_2_AND_PAIR_SUM = VERIFIED_CONDITIONALLY`
- `FIVE_BACKGROUNDS_TWO_MAPS_30_BASE_ODE_STATES = EXECUTED`
- `TWO_UNSEEN_BACKGROUNDS_AND_TIGHT_RTOL = EXECUTED`
- `NONLINEAR_XNUC_EXACT_INVARIANCE = FALSE`
- `ROW_RANK_9_PHYSICALLY_CERTIFIED = FALSE`
- `ORIGINAL_JULIA_10D = NOT_EXECUTED`
- `SOURCE_VALID_BELOW_1E9G = OPEN`
- `BW_INGEST = GITHUB_PENDING_BW_INGEST`
- `NO_PHYSICAL_Yp_DH_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`

**Science decision:** the ROT028 no-common-null conclusion is explicitly **basis-relative**. ROT030 falsifies a basis-independent extension and exhibits an exact finite-linear-observation null with a small nonzero, mostly quadratic conditional neutron response. Neither the linear null nor the small target residual is a physically admitted PBH emission result. The logically decisive forward path is source-admissible subedge spectra, then accepted-step original 10D Julia event/kinetic and full target sensitivity validation with a declared source/host uncertainty budget. No new cross-cell task cascade is created.


## Executable attachment: `build_multibin_null_030.py` (complete source)

```python
#!/usr/bin/env python3
"""Mech-S7 ROT030: matrix source-target information gate, not author-native physical PBH.
Builds exactly 3 comoving source moments + 6 linear response constraints
for a 11-window smooth positive antinucleon source family.
"""
import csv,json,math
from pathlib import Path
import numpy as np
from scipy.linalg import null_space
from scipy.interpolate import PchipInterpolator
from numpy.polynomial.legendre import leggauss
import reproduce_high_order_moment_gate_024 as m
ROOT=Path(__file__).resolve().parent
NWIN=11
EDGES=np.geomspace(.07,.92,NWIN+1)
BINS=list(zip(EDGES[:-1], EDGES[1:]))
TARG=[(chi,mp) for chi in (.25,.5,.75) for mp in ('exec','sym')]
XX,WW=leggauss(144)

def datasets(tight=False):
    d={}
    k=m.K
    for chi,mp in TARG:
        if chi==.5:
            z=np.asarray(k['logu']); w=np.asarray(k['Kln_'+mp]);
        else:
            fn=f'host_kernel_{mp}_chi{int(chi*100):02d}_'+('tight_' if tight else '')+'028.csv'
            z,w=np.loadtxt(ROOT/fn,skiprows=1,delimiter=',').T
        d[(chi,mp)]=PchipInterpolator(z,w,extrapolate=False)
    return d

def mat(nodes=144,tight=False):
    if nodes!=144:x,w=leggauss(nodes)
    else:x,w=XX,WW
    ker=datasets(tight)
    mom=np.zeros((3,NWIN)); obs=np.zeros((6,NWIN))
    for i,(lo,hi) in enumerate(BINS):
        al,ah=np.log(lo),np.log(hi); zz=.5*(al+ah)+.5*(ah-al)*x; uu=np.exp(zz)
        w0=w*.5*(ah-al); B=np.sin(np.pi*(zz-al)/(ah-al))**4
        qp=m.SQ[0]*uu**m.SL[0]; qn=m.SQ[1]*uu**m.SL[1]
        sm=qp+qn
        for j in range(3):mom[j,i]=np.dot(w0,uu**3*sm*B*(zz**j))
        for j,host in enumerate(TARG):obs[j,i]=np.dot(w0,ker[host](zz)*sm*sm/(qp*qn)*B)
    return mom,obs

def canonical(A):
    A=A/np.linalg.norm(A,axis=1,keepdims=True)
    U,s,Vh=np.linalg.svd(A,full_matrices=True)
    # uncorrelated target shape: project a fixed broad-window real probe into nullspace
    N=Vh[len(s):].T
    cand=np.cos(1.17*np.arange(NWIN))+.31*np.sin(2.69*np.arange(NWIN))
    cc=N@(N.T@cand)
    cc=cc/np.max(np.abs(cc))
    if cc[1]<0:cc=-cc
    return cc,A,s,Vh,N

def main():
    mom,obs=mat(); A0=np.vstack([mom,obs]); c,A,s,vh,N=canonical(A0)
    z0=np.array([7,16,30,60,120,160,220,240,270,310,340],float)
    assert np.linalg.norm(A@c)<1e-9
    mass=[]
    for i,(lo,hi) in enumerate(BINS):
        mass.append([float(lo*1e9),float(hi*1e9)])
    vals={'name':'Mech-S7 ROT030','source_kind':'CONDITIONAL_KINETICS_NOT_HAWKING_VALIDATED','upstream_commit':'d395183674cace6c9906a8911bdeb7234ba4040d',
        'windows':NWIN,'bins_mass_g':mass,'constraints':['comoving_pbar/nbar_zeroth','first','second']+[f'adjoint_chi{chi}_{mp}' for chi,mp in TARG],
        'target_covariates':TARG,'coefficients':c.tolist(),'row_norms':np.linalg.norm(A0,axis=1).tolist(),'singular_values':s.tolist(),'singular_cond':float(s[0]/s[-1]),'exact_null_dim':NWIN-len(s),'numeric_rank_relative_1e-8':int((s/s[0]>1e-8).sum()),
        'singular_null_max':float(np.max(np.abs(A@c))),'null_basis':N.tolist(), 'software':'Pchip kernels, Gauss144 basis'}
    (ROOT/'multibin_null_030.json').write_text(json.dumps(vals,indent=2))
    with (ROOT/'constraint_matrix_030.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['constraint']+[f'bin{i:02}' for i in range(NWIN)]+['dot_coefficient','norm']);
        for name,row in zip(vals['constraints'],A0):w.writerow([name,*map(float,row),float(row@c),np.linalg.norm(row)])
    # new independently discretized Gauss256 incl tight host adjoint rows
    mom2,obs2=mat(256,True);A2=np.vstack([mom2,obs2]);err=[]
    for i,(name,r) in enumerate(zip(vals['constraints'],A2)):
        rr=float(r@c)/max(float(np.sum(np.abs(r*c))),1e-100)
        err.append({'constraint':name,'relative_residual_independent':rr,'absolute_residual':float(r@c)})
    with (ROOT/'independent_null_controls_030.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(err[0]));w.writeheader();w.writerows(err)
    print(json.dumps({'singular_values':s.tolist(),'dim_null':N.shape,'max_normalized_primary_residual':float(np.max(np.abs(A@c))),'independent':err,'coef':c.tolist()},indent=2))
if __name__=='__main__':main()

```


## Executable attachment: `test_multibin_ode_030.py` (complete source)

```python
#!/usr/bin/env python3
"""Mech-S7 ROT030; conditional nonlinear 7D kinetics, not Julia 10D/physical PBH."""
import argparse,csv,json,math,time
from pathlib import Path
import numpy as np
import reproduce_high_order_moment_gate_024 as m
import build_multibin_null_030 as g
P=Path(__file__).resolve().parent
C=np.array(json.loads((P/'multibin_null_030.json').read_text())['coefficients'])
def signed_bump(u):
 if not g.EDGES[0]<u<g.EDGES[-1]:return 0.
 i=int(np.searchsorted(g.EDGES,u,side='right')-1);i=max(0,min(len(C)-1,i))
 z=math.log(u);a,b=math.log(g.EDGES[i]),math.log(g.EDGES[i+1]);return C[i]*math.sin(math.pi*(z-a)/(b-a))**4
def new_source(u,k,eps):
 q=np.asarray(m.old.source_rates(u,'public','native',.05),float)
 d=eps*(q[4]+q[5])*signed_bump(u)
 q[4]+=d;q[5]-=d
 if min(q[4:6])<=0:raise ValueError('NONPOSITIVE')
 return q
def run_case(chi,mp,eps,rtol):
 br,host,src=m.bridge.run_bridge,m.mod.prepare_host,m.source
 def new_bridge(*args,**kwargs):
  args=list(args);assert args[4]==.5;args[4]=chi;return br(*args,**kwargs)
 def new_host(*args,**kwargs):
  args=list(args);assert args[3]==.5;args[3]=chi;return host(*args,**kwargs)
 m.bridge.run_bridge=new_bridge;m.mod.prepare_host=new_host;m.source=new_source
 try: rows=m.run_map(mp,{2:eps},rtol)
 finally:m.bridge.run_bridge=br;m.mod.prepare_host=host;m.source=src
 baseline=next(x for x in rows if x['epsilon']==0.)
 for r in rows:
  r.update(chi_EM=chi,dXnuc=float(r['Xnuc']-baseline['Xnuc']),dXcut=float(r['Xcut']-baseline['Xcut']),predicted_linear=0.)
 return rows
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--chis',default='.5');ap.add_argument('--maps',default='exec,sym');ap.add_argument('--amp',type=float,default=.15);ap.add_argument('--rtol',type=float,default=3e-9);ap.add_argument('--prefix',default='multibin_ode_030');opt=ap.parse_args();arr=[]
 for chi in map(float,opt.chis.split(',')):
  for mp in opt.maps.split(','):
   start=time.time();rows=run_case(chi,mp,[0,opt.amp,-opt.amp],opt.rtol);arr.extend(rows)
   print('RESULT',chi,mp,[(r['epsilon'],r['dXnuc'],r['dXcut']) for r in rows], 'time',round(time.time()-start,2),flush=True)
   with (P/f'{opt.prefix}.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(arr[0]));w.writeheader();w.writerows(arr)
 (P/f'{opt.prefix}.json').write_text(json.dumps({'settings':vars(opt),'rows':arr,'NOT_JULIA10D':True,'NOT_PHYSICALLY_VALIDATED':True},indent=2))
if __name__=='__main__':main()

```