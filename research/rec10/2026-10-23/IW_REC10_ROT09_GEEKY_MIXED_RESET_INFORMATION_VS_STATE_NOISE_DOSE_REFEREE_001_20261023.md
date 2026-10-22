# REC10 ROT09 — Geeky-S10 mixed reset: information collapse versus growing stochastic state disturbance

artifact_id: IW_REC10_ROT09_GEEKY_MIXED_RESET_INFORMATION_VS_STATE_NOISE_DOSE_REFEREE_001_20261023
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10
date: 2026-10-23
document_type: INDEPENDENT_SCIENTIFIC_REFEREE
problem_id: P2-WEAK-RESET-RESOURCE-DOSING-001
exposure: PUBLIC
canonical_path: research/rec10/2026-10-23/IW_REC10_ROT09_GEEKY_MIXED_RESET_INFORMATION_VS_STATE_NOISE_DOSE_REFEREE_001_20261023.md
bw_ingestion_event_id: PENDING
result: PASS_WITH_STRENGTHENING / MATURE_GAUSSIAN_AR1_HOST
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_NEW_TASK

## Sources and scope

Primary reviewed source: research/geeky-s10/2026-10-23/geeky_s10_mixed_reset_total_dose_collapse_without_common_storage_001.md (observed blob c0c04728834bc93e0ad17ca34829f4b709ef7b0b), and its independent numerical sanity script (blob 797d82692ae572ecb656b74406ad8634548df0c6). Comparison source INT8 ROT006: research/int8/2026-10-22/iw_int8_oblique_reset_damping_dwell_and_total_strength_budget_bridge_001.md (blob e160f9d33d292dd26d6e1a3ec9cb13380134a21a).

The Geeky-S10 source theorem
  sum c_j² <= epsilon B E² exp(2 mu_+ T + 2DEK)||v||²
is VERIFIED from the prefix semigroup/reset operator norm and sum s_j² <= epsilon sum s_j, for deterministic finite horizon, bounded readout/reset vectors and total observation dose B=sum s_j, conditional state dose K=sum (1-alpha_j)s_j. Under a COMMON theta-independent causal policy with iid Gaussian innovations, sequential likelihood and Fisher bounds are correctly scoped. At raw alpha=1, K=0 and scalar e=d=1,G=0 saturates the bound. This result reuses mature norm-product/Grönwall and Gaussian experiment hosts; novelty is NOT inferred.

## Independent exact separating witness: finite dose and vanishing Fisher, but divergent state disturbance

Set n=1, G=0, e=d=1, scalar theta=x0 in [-R,R]. Choose fixed strength s=epsilon in (0,1), fixed noise-mixing alpha in [0,1], and N integer shots, all within any chosen finite T. Let independent observed-noise innovations eta_j ~ N(0,sigma²), sigma>0; no other state noise. Declared mixed readout/reset:
  Z_j = s x_j^- + eta_j,
  x_j^+ = x_j^- - [(1-alpha)s x_j^- + alpha Z_j]
        = (1-s)x_j^- - alpha eta_j.
No physical detector is asserted.

By induction, actual terminal state is
  x_N = (1-s)^N theta - alpha sum_(j=1)^N (1-s)^(N-j) eta_j.
Therefore EXACTLY:
  E_theta x_N = (1-s)^N theta,
  Var_theta x_N = alpha² sigma² [1-(1-s)^(2N)]/(2s-s²).

But conditional on the same observed history h=(Z_1,...,Z_(j-1)), the state obeys
  x_j^-= (1-kappa s)^(j-1) theta
       - alpha sum_(k<j) (1-kappa s)^(j-1-k) Z_k,
  kappa=1-alpha.
Hence conditional coefficient c_j=s(1-kappa s)^(j-1), and subtracting the known history-dependent offset gives iid Gaussian innovations with parameter mean theta*c_j. Consequently the WHOLE observation experiment has exact Fisher:
  I_N(theta)
    = (s²/sigma²) sum_(j=0)^(N-1)(1-kappa s)^(2j).
If kappa>0 this equals
  (s²/sigma²)[1-(1-kappa s)^(2N)]/[1-(1-kappa s)²];
if kappa=0 (raw endpoint), it equals N s²/sigma².
In either case I_N <= N s²/sigma² = s B/sigma² with B=N s.

Fix B>0 and choose s=B/N, N->infinity. Then
  E x_N -> exp(-B)theta (ORDER-ONE mean state damping);
  I_N=O(s)->0 (NO-INFORMATION experiment at fixed sigma);
  Var x_N ~ [alpha² sigma²/(2s)](1-exp(-2B)).
Thus for EVERY FIXED alpha>0 the unconditional state variance DIVERGES as 1/s, despite bounded total measurement strength and vanishing information about theta. For every fixed target M, P_theta(|x_N|>M)->1, uniformly for theta in [-R,R] when alpha>0 fixed.

New exact scaling separator if alpha=alpha_s=s^p (p>=0):
  Var x_N ~ [sigma²/2](1-exp(-2B))*s^(2p-1).
So p<1/2 => divergent state variance; p=1/2 => finite nonzero variance; p>1/2 => noise-driven variance vanishes. At p=0 alpha=1 gives the raw endpoint. This is a standard AR(1)/Gaussian calculation, not a novel physical phase law. The conditional Fisher collapse O(s) holds throughout these cases.

## Independent reproducibility checks

For B=1, sigma²=1 and N=1/s:
  s=.1, N=10: raw alpha=1 variance 4.62328077, Fisher 0.1;
  s=.02, N=50: variance 21.90354657, Fisher 0.02;
  s=.005, N=200: variance 86.75107339, Fisher 0.005;
  s=.001, N=1000: variance 432.61634547, Fisher 0.001.
In the alpha_s=s^(1/2) critical scaling, corresponding state variances are .46232808, .43807093, .43375537, .43261635, approaching (1-exp(-2))/2=.4323323584. All figures follow direct geometric sums, not simulations of the source apparatus.

## Referee disposition

PASS for Geeky-S10 source theorem and its exact scalar sharpness; no contradiction.
STRENGTHENED NONMAP: finite total observation strength and vanishing statistical information DOES NOT imply vanishing actual state disturbance when unscaled measurement noise is physically fed into state reset.
More sharply, actual mean state damping is O(1), while state variance may be O(1/epsilon); therefore treating the statistical-information bound as a measurement-backaction, operational-safety, or physical weak-disturbance theorem is ILLEGAL.
Parameter-conditioned information and unconditional stochastic state trajectories are different mathematical objects. Adaptation, correlated Gaussian noise without innovation contract, quantum CP instruments, or physical energy cost are NOT derived from this witness.
This is within mature discrete-time linear Gaussian AR(1) / Kalman-state and sequential experiment theory. It is a source-typed falsifier for false inference, not new theory.
No extra owner tasks. STOP until changed physical source contract or independently validated noise-scaling/shot-rate rule. BW ingestion and owner acceptance not implied by GitHub storage.
