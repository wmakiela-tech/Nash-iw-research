# MT13 — Deterministic bounded-noise target recovery and measurement-gain legality

**RETURN_ID:** MT13-ROTATION-NOISY-TARGET-RECOVERY-001_20261018  
**DATE:** 2026-10-18  
**CELL:** MT13 / scientific programme owner  
**RESULT CLASS:** exact real finite-dimensional minimax, source-typed experimental-design guard, mature-host subtraction  
**CEILING:** FOUNDATION / NO_NOVELTY / NO_CANON / NO_EXEC / NO_PHYSICAL_TRANSFER.

## 1. Source-native motivation and separation

LT4, *Hidden-state target minimax/Gramian*:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt4/2026-10-17/lt4_hidden_state_target_minimax_gramian_001.md
proves the no-measurement worst-case target error R||M_T|| for a ball of hidden preparations.

MT13, *Optimal exact rank-k sensors*:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/20261018_hidden_state_target_optimal_sensors_singular_values.md
proves E_k=R sigma_(k+1)(M_T) when arbitrary k exact noiseless linear measurements of hidden state are allowed.

PRF11 foundation report:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-18/IW_PRF11_FOUNDATION_IDENTIFIABILITY_DECISION_MEMORY_REPORT_001_20261018.md
distinguishes full-law identifiability from finite-sample risk and target-relative information.

**This rotation changes ONE load-bearing assumption: noiseless linear measurement -> deterministically bounded measurement error.** It does not assert laboratory realizability.

## 2. Exact minimax theorem (real scalar target)

Let Y=R^n and W=R^p with Euclidean norms, R>0, delta>=0, a known linear measurement matrix C: Y->W and target vector m in Y. Nature chooses hidden state y and measurement error eta subject to ||y||<=R and ||eta||<=delta. The instrument returns z=Cy+eta. A deterministic reconstruction rule phi:W->R attempts to estimate m^T y; a known baseline can be added back afterward.

Define worst-case minimax error
E(C,m;R,delta)=inf_phi sup_{||y||<=R, ||eta||<=delta} |m^T y-phi(Cy+eta)|.

**Exact identity:**
E = max_{||v||<=R, ||Cv||<=delta} |m^T v|
  = min_{w in R^p} [R||m-C^T w|| + delta||w||].               (1)

An optimal recovery rule can be chosen LINEAR: phi(z)=w_*^T z, with w_* minimizing (1). Nonlinear algorithms cannot improve its worst-case error under this contract.

**Proof (indistinguishable pair):** For any v satisfying ||v||<=R and ||Cv||<=delta, the two legal preparations (y,eta)=(v,-Cv) and (-v,+Cv) both produce z=0 while their scalar targets are opposite. Every phi therefore incurs worst-case error at least |m^T v|; maximize over v.

**Duality and upper bound:** Any w yields
|m^T y-w^T(Cy+eta)| <= R||m-C^T w||+delta||w||.
For equality of the infimum and constrained maximum, use finite-dimensional convex minimax:
max_{||v||<=R,||Cv||<=delta} m^Tv
 = max_{||v||<=R} inf_w [(m-C^Tw)^Tv + delta||w||]
 = inf_w max_{||v||<=R} [(m-C^Tw)^Tv + delta||w||]
 = inf_w [R||m-C^Tw||+delta||w||].
The first inf_w gives 0 from the constraint when ||Cv||<=delta and minus infinity otherwise. The swap is licensed by the compact convex state ball, convex w-domain and convex-concave continuous payoff. Central symmetry permits replacing m^Tv by |m^Tv|. Minima are attained in finite dimension (for delta=0, minimize distance to closed ran(C^T)). QED.

## 3. Sharp legal-access and precision consequences

- Exact observation limit: delta=0 gives E=R||P_ker(C) m||. Thus this scalar result reduces to the previous exact noiseless target-risk gate.
- Nonzero noise: for m!=0, R>0, delta>0, E>0 for every fixed finite C. A small nonzero v aligned with m is legal and can be hidden within positive noise. Even full-rank C does not restore exact minimax recovery.
- If m is orthogonal to ran C^T then E=R||m||: measurements cannot constrain any part of target uncertainty. If m lies in ran C^T, noise can still prevent exact recovery.
- On a scalar target measured through one normalized sensor C=m^T/||m||, E=||m|| min(R,delta). Improvement depends on sensor precision, not only number of observed directions.
- **Gain degeneracy:** If C is freely rescaled to aC without an accompanying gain/noise/energy contract, its effective input uncertainty delta/a shrinks artificially. For scalar C=1,m=1,R=1,delta=0.2, E(a)=min(1,0.2/a). Hence unconstrained 'optimal noisy sensor' comparisons are ill posed.
- **Adversarial repeats do not automatically help:** If n repeats return z_i=Cy+eta_i with every ||eta_i||<=delta and no joint noise budget, an adversary may use eta_1=...=eta_n=-Cv for the same pair +/-v. The minimax error is exactly the same as one measurement: use first observation for upper bound, common-noise pair for lower bound. Independent stochastic mean-zero noise is a DIFFERENT contract and may allow averaging.
- If a joint Euclidean bound applies to concatenated noise (instead of each repeat separately), the effective common-perturbation budget can scale as delta/sqrt(n). Always specify noise geometry.

## 4. Fully solved two-dimensional witness

Take n=2, m=(1,1), C=(1,0), R=1. Unobserved target risk is sqrt(2); noiseless C leaves risk 1. For 0<=delta<=1/sqrt(2),

E(delta)=delta+sqrt(1-delta^2).

For delta>=1/sqrt(2), E(delta)=sqrt(2). This follows by optimizing v1+sqrt(1-v1^2) over 0<=v1<=min(delta,1), subject to ||v||<=1. For delta=0.2, E=1.179795897113271. The optimal linear recovery weight is w*=1-delta/sqrt(1-delta^2)=0.795875854768 for 0<delta<1/sqrt(2), and 0 above threshold.

Seven numerical primal-vs-dual-vs-closed checks were performed for delta in {0,0.1,0.2,0.5,1/sqrt(2),0.9,1}; all discrepancies were below 2e-8 (grid primal and golden-section dual). Sensor gains 1,10,100 give the artificially improving scalar errors 0.2,0.02,0.002 at unchanged external noise budget. These are classical toy computations, NOT data.

## 5. Mature host and subtraction

The basic result is **established optimal-recovery theory**, not NASH mathematical novelty. Literature anchors:
- C. A. Micchelli and T. J. Rivlin, *A survey of optimal recovery*, in *Optimal Estimation in Approximation Theory* (1977): classical worst-case recovery and indistinguishable-input geometry (see also Golomb–Weinberger 1959).
- D. L. Donoho, *Statistical Estimation and Optimal Recovery*, *Annals of Statistics* (1994): deterministic-noise recovery versus statistical risk, radius of information.
- *Instances of computational optimal recovery: Refined approximability models*, *Journal of Complexity* (2020), DOI 10.1016/j.jco.2020.101503: explicitly discusses optimal recovery of linear functionals with bounded observation errors and coefficient objective of residual dual norm plus noise dual norm.
- *Worst case tractability of linear problems in the presence of noise: Linear information*, *Journal of Complexity* (2023): deterministic bounded versus Gaussian noise, information precision costs.

The contribution here is **project-local typing**: replacing the idealized rank-only sensor claim with the exact precision/access/cost admission object. The theorem is not proposed as new.

## 6. Programme placement and negative knowledge

For any claim that k measurements improve fidelity in LT4/PRF11, freeze target m or M_T, hidden preparation class/radius, legal observation channel C, norm of C and its calibration, deterministic/stochastic noise model and joint-vs-per-sample noise budget, intervention meaning, and actual endpoint/history/decision loss. In this theorem the output is a real scalar endpoint target, not a vector or quantum instrument. For vector targets, an indiscriminate scalar half-diameter argument can fail and a separate Chebyshev-radius theorem is needed. Gaussian confidence/error bars cannot be copied from this deterministic adversarial model. A measurement cannot be called physically legal solely because an arbitrary linear functional exists mathematically.

**No change:** REV020 active authored head, P2 current, P3 host-atlas fallback, TPE HOLD, true surplus NONE; LT4 author/integration, KN/BW custody, Moderator EXEC. No new tasks and no Front B or NCDG physical upgrade.
