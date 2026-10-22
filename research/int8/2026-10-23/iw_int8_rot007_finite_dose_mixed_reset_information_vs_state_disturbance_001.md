---
artifact_id: IW_INT8_ROT007_FINITE_DOSE_MIXED_RESET_INFORMATION_VS_STATE_DISTURBANCE_001_20261023
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
date: 2026-10-23
document_type: CONDITIONAL_THEOREM_AND_EXACT_COUNTEREXAMPLE
exposure: PUBLIC
canonical_path: research/int8/2026-10-23/iw_int8_rot007_finite_dose_mixed_reset_information_vs_state_disturbance_001.md
problem_id: IW_INFORMATION_VS_PHYSICAL_DISTURBANCE_MIXED_RESET_001
status: SELF_DERIVED_AND_DIAGNOSTIC_CHECKED / INDEPENDENT_REFEREE_PENDING
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 — bounded-dose Gaussian information collapse does not bound stochastic state disturbance

## 0. Currentness, subtraction and scientific question

As of 2026-10-23, the 2026-10-22 Moderator-accepted MT13 programme guidance prioritizes Front B source-valid physics, Living Theory coherence and host subtraction, then DTC, with autonomy for role-native research. This is a scoped P2 scientific-integration rotation, NOT a new front or OWNER declaration. The write path follows docs/IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md. Publication != BW/independent reviewer acceptance.

Primary host results already present and NOT re-claimed here:
- INT8 ROT006: at fixed T and total measurement strength sum s_j<=B, bounded oblique readout/reset ports imply a deterministic weak-record bound without global finite V_*:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/int8/2026-10-22/iw_int8_oblique_reset_damping_dwell_and_total_strength_budget_bridge_001.md
- Geeky-S10 2026-10-22: mixed ideal/raw reset, exact conditional sensitivity fraction kappa=1-alpha, adaptive iid Gaussian theorem, but with finite all-protocol common V_*:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s10/2026-10-22/geeky_s10_heterogeneous_mixed_noise_reset_common_storage_phase_001.md
- PRF11 R13-R16: ideal-reset and Gaussian information comparisons; covariance lower-spectrum and time-index source-typing guard; MT13: raw/mixed reset scalar information and a state-variance witness.
- In particular the original raw-reset unbounded-shot Fisher scaling and mixed-reset state-variance formula are mature and already known from Geeky/MT13. The DELTA here is the **absence of any V_* hypothesis** in the finite-dose conditional Gaussian bound, and the exact fixed-dose juxtaposition of vanishing Fisher with diverging physical-state variance in the same experiment.

QUESTION: If stochastic observation noise also feeds the state reset, can a fixed finite action-dose budget guarantee vanishing statistical information for arbitrary adaptive heterogeneous finite protocols even when common all-horizon available storage is infinite? What does this say, and NOT say, about disturbance of the actual state?

## 1. Precise admitted carrier

Real finite-dimensional X=R^n, fixed generator G. Unknown original preparation x_0=theta v, theta in [-R,R], R>0 and fixed v. Free flow exp(G tau).

At each shot j, based on previous observed values and a parameter-independent optional public random seed, a common causal policy chooses a nonnegative wait, vectors e_j,d_j, strength s_j>=0, and noise-feedback fraction alpha_j in [0,1], *before* innovation eta_j occurs. Pathwise conditions for every realized protocol:
  ||e_j||<=E, ||d_j||<=D, 0<=s_j<=epsilon<1,
  elapsed measurement horizon <=T<infinity,
  total strength sum_j s_j <= B < infinity,
  finite shot count (can depend on epsilon and past records).

Ideal signal b_j=s_j e_j^T x_j^-. Observed Z_j=b_j+eta_j with current eta_j independent N(0,sigma^2), sigma>0 fixed independently of epsilon, past, policy, theta; mixed reset
  x_j^+ = x_j^- - d_j[(1-alpha_j)b_j+alpha_j Z_j].
Equivalently x_j^+= (I-s_j d_j e_j^T)x_j^- - alpha_j d_j eta_j.
The noise is additive, Gaussian innovation with sigma^2 fixed. It can influence later action choices, but it does not anticipatorily influence the current action. All parameters of the policy are identical functions of history across theta.

Set mu_+ = max(0, lambda_max((G+G^T)/2)).
No common finite V_*, dissipativity certificate P, unit sensor, co-alignment or stability of G is assumed.

## 2. Exact conditional sensitivity (do NOT use unconditional reset)

Fix the *same observed past* h under two candidate values of theta. Conditional on h, the chosen times and action parameters are identical and the pre-shot state has affine form
  x_j^-(theta;h)=theta xi_j^-(h)+r_j(h),
with residual r_j depending on h but not theta. Thus the conditional Gaussian mean of Z_j has theta coefficient
  c_j(h)=s_j e_j^T xi_j^-(h).
After conditioning on the current observed value Z_j=z_j, the mixed reset becomes
  x_j^+ = [I-(1-alpha_j)s_j d_j e_j^T] x_j^- - alpha_j d_j z_j,
so
  xi_j^+ = [I-kappa_j s_j d_j e_j^T] xi_j^-,
  kappa_j=1-alpha_j in [0,1].
Between shots xi evolves under G.

This is Geeky's correct *conditional sensitivity* typing. The actual random state uses full ideal reset s and -alpha d eta; it is NOT governed by the same conditional sensitivity recurrence.

## 3. Theorem 007.1: finite-dose pathwise sensitivity bound, WITHOUT common V_*

Under the conditions of §1, along every frozen observed history,
  sum_j c_j(h)^2
   <= L_epsilon(T,B,v)
   := epsilon B E^2 exp(2 mu_+ T +2 D E B) ||v||^2.          (3.1)

Proof: ||exp(G tau)||_2 <= exp(mu_+ tau) and
  ||I-kappa_j s_j d_j e_j^T|| <= 1+kappa_j s_j D E <= exp(s_j D E).
Thus all pre-shot conditional sensitivity states obey
  ||xi_j^-||<=exp(mu_+ T+D E B)||v||,
independently of number, order, angles, alpha_j or adaptivity after freezing history.
Hence
  sum_j c_j^2 <= E^2 exp(2 mu_+T+2DEB)||v||^2 sum_j s_j^2
              <= epsilon B E^2 exp(2 mu_+T+2DEB)||v||^2.
QED.

For the FULL RAW reset case alpha_j=1 (kappa_j=0), the conditional sensitivity ignores *all* reset maps and xi_j^-=exp(G t_j)v; the sharper special-case estimate is
  sum_j c_j^2 <= epsilon B E^2 exp(2 mu_+ T)||v||^2.          (3.2)

Neither statement bounds realized noise-induced state energy. If T,B,E,D or sigma scale with epsilon, the rate has to be re-evaluated.

## 4. Corollary 007.2: adaptive iid Gaussian KL/Fisher/Le Cam/minimax

Let P_theta^pi be the joint recorded-data law including logged actions and public seed for any common admissible causal policy pi. At a frozen past h,
  Z_j | h,theta ~ N(theta c_j(h)+rbar_j(h), sigma^2),
where rbar_j is theta-independent.

The conditional Gaussian KL and the sequential chain rule yield
  KL(P_theta^pi || P_theta'^pi)
    = (theta-theta')^2/(2sigma^2)
       E_theta sum_j c_j(H_<j)^2
    <= (theta-theta')^2 L_epsilon/(2sigma^2).           (4.1)

For random finite stopping times, apply the stopped chain rule (or bounded-prefix limits) under the same parameter-independent causal policy and uniform pathwise bound; the terminal stop indicator carries no extra conditional theta information once the history is known.

Gaussian martingale score orthogonality also gives Fisher
  I_pi(theta) <= L_epsilon/sigma^2.                     (4.2)

Relative to a parameter-free experiment using the same data law P_0^pi for all theta, Pinsker yields
  sup_|theta|<=R TV(P_theta^pi,P_0^pi)
    <= min(1, R sqrt(L_epsilon)/(2 sigma)),             (4.3)
so Le Cam comparison deficiency/distance to the no-information experiment is at most that bound, with experiment-specific matching sample spaces.

Two-point theta∈{-R,R}, equal prior, binary Pinsker and KL information radius (exactly PRF11 R13's mature-host argument) give all-estimator minimax MSE
  R^2[1 - R^2 L_epsilon/sigma^2]_+ <= J_pi <=R^2.     (4.4)
Thus fixed finite T,B,E,D,v,R,sigma imply Fisher O(epsilon), Le Cam O(sqrt epsilon), worst-case squared-error *advantage* O(epsilon), uniformly over arbitrarily large but finite, causally chosen shot counts.

This is a typed information-theoretic corollary of a particular classical iid Gaussian **innovation** law, not a physics finding or a claim of novel information inequality.

## 5. Exact and asymptotically sharp single-preparation counterexample: vanishing information VS diverging actual state variance

Use the scalar carrier n=1, G=0, e=d=1, x_1=theta, alpha=1 (CURRENT RAW noisy output drives reset), equal s=epsilon, and N=floor(B/s) repeated shots at any times inside fixed T. This meets s_j<=epsilon and total dose Ns<=B.

Dynamics:
  Z_j=s x_j+eta_j,
  x_(j+1)=(1-s)x_j-eta_j,
  eta_j iid N(0,sigma^2).

FROZEN-HISTORY conditional sensitivity:
  x_j(theta;z_<j)=theta - sum_{k<j} z_k,
so c_j=s. An invertible causal readout transform
  Y_j=Z_j + s sum_{k<j}Z_k=s theta+eta_j
reduces the entire experiment to N independent N(s theta,sigma^2) observations. Hence EXACT
  I_N(theta)=N s^2/sigma^2
      = (B/s+O(1))*s^2/sigma^2
      ~ B s/sigma^2 ->0.                               (5.1)

This realizes the optimal O(epsilon) **rate** of the universal finite-dose Fisher bound, without claiming equality of its conservative constant.

At the same time, the true post-N state contains accumulated independent random feedback noise:
  x_(N+1) = (1-s)^N theta - sum_{j=1}^N(1-s)^(N-j) eta_j,
so EXACT
  Var(x_(N+1)|theta)
    =sigma^2[1-(1-s)^(2N)]/[s(2-s)].                  (5.2)
For B>0 fixed,
  Var(x_(N+1)|theta)
    ~ sigma^2(1-exp(-2B))/(2s) -> infinity.           (5.3)

The scalar example therefore establishes simultaneously:
  VANISHING INITIAL-PREPARATION INFORMATION
  != VANISHING ACTUAL-STATE DISTURBANCE,
even with fixed total measurement-strength budget and fixed measurement horizon.

It also shows that an instrument model with raw fixed-variance noise in every shot may have a divergent stochastic state-energy cost despite asymptotically uninformative readouts. Any physical hardware budget/sampling-rate law is separate and not postulated.

Numeric table for B=1,sigma=0.3, N=floor(1/s):
s=0.1: Fisher 1.111111..., Varpost 0.416...
s=0.02: Fisher .222222..., Varpost 1.971...
s=0.005: Fisher .055555..., Varpost 7.8075966051788255
Numerical controls checked locally; executable reproduction: research/int8/2026-10-23/reproduce_int8_rot007_finite_dose_mixed_reset.py. Synthetic tests do not independently referee the proof.

## 6. Nonmaps and sharp failure controls

(A) FIXED IID INNOVATION VARIANCE is essential: for arbitrary covariance Σ with near-zero eigenvalues, ||c||²->0 need not imply c^TΣ^{-1}c->0. PRF11 R14/R15 supplied exact correlated-noise witnesses (including fixed marginal variances). Uniform covariance floor or a legal causal innovation lower bound is required.

(B) If sigma^2(s)=sigma_0² s^p, the raw scalar example (5.1) has I_N~(B/sigma_0²)s^(1-p). At p=1 nonzero information can survive; p>1 can yield divergent Fisher despite finite total s-dose. No physical noise law is inferred.

(C) Unbounded fresh preparations violate the single-state dose model.

(D) Bounds on conditional sensitivity are not bounds on physical terminal target or stochastic actuator energy; LT5's terminal state must include actual noise backaction and source-matched physical ports, and gain vs amplitude classes must be kept distinct.

(E) If B grows with s, e.g. c log(1/s) in the oblique-switching witness of INT8 ROT006, the universal bound no longer guarantees collapse. If an unbounded number of shots is physically disallowed by sample-rate rules, the admissible policy family shrinks.

(F) Neither a stochastic Gaussian observation model nor the classical reset channel is a certified quantum instrument.

(G) No DTC/J3/K pseudospectral, PBH/BBN, gravitational, or experimental endpoint follows.

## 7. Mature host subtraction and disposition

Mathematics: elementary Gronwall/logarithmic norm bounds for switched/impulsive linear systems, conditional sensitivity of feedback Markov chains, Gaussian sequential KL chain rule, Fisher martingale identity, Pinsker, Le Cam comparison, and exact AR(1) variance. All are mature. Specific linkage to NASH/INT8, Geeky and PRF is a useful *typed bridge*; no novelty or discovery claim.

problem_id: IW_INFORMATION_VS_PHYSICAL_DISTURBANCE_MIXED_RESET_001.
best_current_result: Theorem 007.1, Corollary 007.2, exact scalar state-disturbance witness 5.1–5.3.
counterresult: correlated-noise precision counterexamples (PRF11 R14/R15), sigma²(s) floor failure, unbounded dose (INT8 ROT006).
owner: LT5 (theory integration), Geeky-S10 (reset action family), PRF11 (statistical host); INT8 owns only this cross-front note.
independent_referee: PENDING, NOT CLAIMED.
blocking_source: actual detector noise/backaction/resource realization unspecified.
cheapest_discriminator: provide source-native noise covariance/innovation floor + backaction + per-shot physical cost, then test 5.1–5.3 against that contract; no task escalation initiated.
acceptance: mathematics conditional / NO physical acceptance.
canonical_path: research/int8/2026-10-23/iw_int8_rot007_finite_dose_mixed_reset_information_vs_state_disturbance_001.md
bw_state: GITHUB_PENDING_BW_INGEST / NO_WITNESS_OF_BW_ACCEPTANCE.

NO_NEW_TASK_CASCADE. NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
