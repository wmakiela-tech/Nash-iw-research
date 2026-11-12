# IW/NASH M14 ROT044 — hidden differential timestamp jitter: exact common-mode gauge and sharp Gaussian minimax

artifact_id: IW_M14_ROT044_UNOBSERVED_DIFFERENTIAL_TIMESTAMP_JITTER_GLOBAL_MINIMAX_001_20261112
return_id: M14-ROT044-NOMINAL_SIMULTANEITY_HIDDEN_JITTER_GAUGE_AND_SHARP_LIPSCHITZ_GAUSSIAN_MINIMAX_001_20261112
date: 2026-11-12
origin: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09 / M14
exposure: PUBLIC
claim_ceiling: EXACT_CLASSICAL_STATIC_FIELD_HIDDEN_TIMESTAMP_MINIMAX / NO_MATH_NOVELTY / NO_SOURCE_NATIVE_SENSOR / NO_NASH_PHYSICS / NO_CANON / NO_EXEC_SIGN / BW_PENDING / REFEREE_PENDING

## Source / custody / precedence

XH-S5 ROT007 FIRST owns Schall, Lindner, Rottstaedt et al., *Laser-enhanced quantum sensing boosts sensitivity and dynamic range*, Nature Communications 17 (2026) 10825 (22 October 2026), https://doi.org/10.1038/s41467-026-78386-z. Reported 127 fT/sqrtHz is an author PHOTON-SHOT-NOISE LIMIT; article expressly states technical noise is significant and PSN limits are not achieved technical-noise sensitivity. No source-native time-series replay; authors do NOT certify paired signed branches, simultaneous physical NV readout, channel differential timing error, Gaussian center-fit noise, H, epsilon or sigma for this model.

OWN FIRST: ROT031 four tetrahedral axes and common mode; ROT039 exact removal of common drift only at genuinely matched actual times; ROT040 first exact **known unequal actual timestamps** fixed-slot Lipschitz minimax; ROT041–043 temporal co-time group rank and resolution. NEW ROT044 concerns **UNKNOWN actual timestamps with SAME nominal reported time**, not a reattribution of known-stagger experiments. Mathematical prior is classical linear algebra, hypercube extremality and Gaussian Bayes; NO novelty claimed.

## Frozen model (critical observability typing)

A has tetrahedral rows a0=(1,1,1), a1=(1,-1,-1), a2=(-1,1,-1), a3=(-1,-1,1), with A^T A=4I3 and A^T1=0. Target z in R3 is a STATIC field. All FOUR nominal channels are labeled timestamp 0, but true per-axis times delta_i are NOT OBSERVED, with |delta_i|<=epsilon; do not assume they share actual time. Unit observation Y_i,ell=a_i·z + h(delta_i) + independent Gaussian N(0,sigma²), total N, each unit observation equal cost. Arbitrary possibly biased estimators, and adaptive allocation of repeats among these FIXED FOUR nominal channels permitted. No new user-observed physical timestamps, other time windows, or known random law for jitter. h(t) is one unknown common scalar calibration function, either unrestricted C-infinity or externally bounded Lipschitz H.

**Distinguish common-clock offset:** if delta0=delta1=delta2=delta3, even unknown, the common h(delta) cancels by A^T; no negative claim about this case. Likewise a device that actually MEASURES all true offsets belongs to a DIFFERENT statistical experiment.

## R44.1 exact structural negative: any epsilon>0 + unrestricted common h

Choose arbitrary u in R3, q>0, hidden s=±1, field z_s=u+s q e_x, the SAME linear common h(t)=(q/epsilon)t, true unobserved times delta_i,s=−s epsilon a_i,x. Since a_i,x=±1, all offsets legal and all four means are EXACTLY a_i·u in either world. This holds at ALL repeated observations, including adaptive channel allocation. Since q can be arbitrarily large with unbounded slope, the global minimax MSE of z is **INFINITE for every epsilon>0**, despite the four channels claiming one nominal timestamp. At epsilon=0 exact four-axis common-mode cancellation from ROT039 returns, so the identification assumption has a discontinuity at zero hidden jitter. No real instrument claim.

## R44.2 exact sharp geometric bias under certified Lipschitz H

If |h(t)−h(s)|<=H|t−s|, h_i=h(delta_i) lie in an interval of range <=2H epsilon. With the four-axis projector zhat=A^T Ybar/4, systematic bias is A^T h/4. Since A^T1=0, subtract min_i h_i, normalize to q_i in [0,1]. A convex norm reaches its maximum over the 16 vertices of [0,1]^4; for subset S, ||sum_{i in S} a_i|| equals 0, sqrt3, 2, sqrt3, 0 for |S|=0,1,2,3,4. Consequently **max ||A^T h/4||=H epsilon**, so squared error floor is (H epsilon)^2. EXACT witness h(t)=Ht and true offsets (−epsilon,−epsilon,+epsilon,+epsilon) gives field bias −H epsilon e_x. Any four-vector h_i of span<=2H epsilon is realizable using some hidden delta_i in [-epsilon,epsilon] and a common affine h, so no relaxation gap.

## R44.3 exact all-estimator adaptive Gaussian minimax

When N divisible by 4:
**GLOBAL TOTAL VECTOR MSE R*=3sigma²/N + (H epsilon)^2.**
For general integer N this is a universal lower bound, NOT automatically attained.

UPPER: n_i=N/4 samples per fixed nominal axis and zhat=A^T Ybar/4, with Cov=sigma²/N I3 and sharp worst squared bias (H epsilon)^2.

LOWER for all biased/adaptive estimators: independent proper Gaussian u~N(0,tau²I3) and hidden equiprobable s=±1, v=H epsilon e_x, z_s=u+s v, h(t)=Ht, delta_i,s=−s epsilon a_i,x. Both worlds have identical all-channel conditional means a_i·u; even adaptive measurement histories cannot reveal s. Conditional posterior precision Q=tau^-2 I3+sigma^-2 sum_{ell=1}^N a_iell a_iell^T, with trQ=3tau^-2+3N/sigma² on EVERY realized adaptive history. Posterior z covariance Q^-1+vv^T gives MSE>=trQ^-1+||v||²>=3/(tau^-2+N/sigma²)+(H epsilon)^2. Let tau→infinity. Upper meets lower. This is exact sharp classical minimax with the stated **H-Lipschitz source model, equal per-channel costs and unobserved fixed-axis jitter**.

THREE-AXIS NEGATIVE: first three tetrahedral axes satisfy A3(1,1,−1)=1_3. Any free common intercept h(0) is exactly confounded with field changes along (1,1,−1); minimax risk already INFINITE at epsilon0. Four axes are essential to cancel arbitrary common intercept.

## R44.4 distinct experiment: known true timestamps

If true timestamps t_i ARE observed, sort t_i by indices i_k. Let d_k=t_i(k+1)−t_i(k)>=0 and U_k=sum_{j=k+1}^3 a_i(j). Exact deterministic worst squared BIAS of the **four-axis projector**, not a global all-estimator statistical minimax, is:
**(H²/16) max_{s0,s1,s2=±1} ||sum_{k=0}^2 s_k d_k U_k||².**
All eight vertices are attainable by piecewise-linear H-Lipschitz calibration h, because consecutive increments alone determine all Lipschitz pair constraints on a real line. Example H=1: t=(-1,-1,+1,+1) -> squared bias 1; (-1,-1/3,+1/3,+1)->5/9; (-3/2,-1/2,+1/2,+3/2)->5/4, matching ROT040's known-stagger example; exactly common t=(0,0,0,0)->0. The timing-metadata observation distinguishes this experiment from hidden-jitter R44.3.

## Reproducibility and strict stop

Moderator-local original Polish proof/report plus two genuinely separate full programs, compact public stdlib proof-witness, two reproducible JSON, README, dispatch and SHA manifest assembled in a verified ZIP. Exact stdlib Fraction **300 executed assertions** including all 16 cube vertices, global exact same-data aliases, unbounded slope, and known-time vertices. Independently mpmath **100 digits** and NumPy **20031 executed assertions**, 20000 legal randomly sampled timestamp/Lipschitz trajectories, 250000 Gaussian vector samples; at N80 sigma²0.7 H0.6 epsilon0.03, theory risk **0.026574** versus empirical **0.026562136275985585** (0.04464% relative). Monte Carlo is a numerical check, not a proof of a mathematical global minimax. Exact proof above is self-contained.

ZIP: IW_M14_ROT044_UNOBSERVED_TIMESTAMP_JITTER_SHARP_GAUSSIAN_MINIMAX_FULL_REPRO_001_20261112.zip, bytes **16071**, SHA256 **1d84e5d35a5bb19658cc8fd8dfb342823444d50ae7fef8273e2a7d3e11300d32**. ZIP CRC PASS, SHA256 payload 8/8 PASS, three independent clean extracted script reruns PASS; two result JSON BYTE IDENTICAL. Full ZIP LOCAL ONLY, not GitHub-hosted.

No source-native NV timestamps, hardware physical clock precision, calibrated H/epsilon/sigma, measured technical-noise sensitivity, validated Gaussian fitting law, fT physical gain, general math novelty, new GR/GW/PBH/NASH J3K physics, independent REC11/AUD1 verdict, BW ingest, LT adoption, canon or execution signature. NO_NOVELTY / NO_NASH_PHYSICS / NO_CANON / NO_EXEC_SIGN / BW_PENDING / REFEREE_PENDING / NO_NEW_TASK_CASCADE. POSTED != ACK.