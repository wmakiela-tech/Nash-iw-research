---
artifact_id: IW_PRF11_R13_ADAPTIVE_WEAK_SENSOR_LECAM_INFORMATION_MINIMAX_COLLAPSE_001_20261021
title: "PRF11 R13 — weak reset sensing, adaptive Gaussian experiments, Le Cam and sharp minimax-loss collapse"
created_at: 2026-10-21
as_of: 2026-10-21
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_10 / PRF11
function: SCIENCE_FIRST / OTHER_CELLS_FIRST / FOUNDATION_RECONSTRUCTION / CROSS_FAMILY_PRIOR_ART_SUBTRACTION
document_type: REPORT
task_id: IW_PRF11_R13_WEAK_SENSOR_STATISTICAL_COMPARISON_001_20261021
exposure: PUBLIC
status: DRAFT / REQUIRES_INDEPENDENT_REVIEW
primary_location: GitHub research/prf11/2026-10-21/IW_PRF11_R13_ADAPTIVE_WEAK_SENSOR_LECAM_INFORMATION_MINIMAX_COLLAPSE_001_20261021.md
content_identity: VERIFY_GITHUB_BLOB_AND_COMMIT_BY_READBACK
provenance: public NASH GitHub source bodies + externally verified publisher/journal metadata + full independent analytic derivation
derived_from:
  - IW_PRF11_R12_ADAPTIVE_GAUSSIAN_SENSOR_BUDGET_KL_FISHER_VANTREES_MINIMAX_001_20261019
  - GEEKY-S10-INT8-WEAK-MEASUREMENT-ACCUMULATION-CEILING-001
  - IW_INT8_WEAK_PROTOCOL_QUOTIENT_IDENTIFICATION_VS_BOUNDED_ACTUATION_BRIDGE_001_20261021
supersedes: []
stale_if: legal readout/reset/noise semantics change; project owner updates a cited theorem; peer review changes claim ceiling
acceptance_owner: mathematical referee / source owners Geeky-S10, INT8, LT5, SW; Moderator holds EXEC
return_path: canonical GitHub file; bounded Slack science dispatch if successfully sent
claim_ceiling: EXACT_CONDITIONAL_MATURE_HOST_COROLLARY / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC / NO_PHYSICAL_UPGRADE
cross_surface_sync: GITHUB_PENDING_BW_INGEST
---

# PRF11 R13 — When do arbitrarily many weak observations carry asymptotically zero *statistical* information?

## 0. Others' results before own derivation: current 2026-10-21 source map

Read full current public sources before selecting the question:

**LT5** distinguishes two *noninterchangeable* controller resources:
1. operator-gain bound ||F||<=kappa for static linear feedback, giving an exact constrained optimal-recovery objective;
2. hard actuator-amplitude bound ||u(b)||<=Umax, for which a different exact scalar minimax decomposition holds for centrally symmetric compact convex uncertainties and arbitrary measurable policies.
Sources:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/2026-10-20/lt5_target_information_vs_actuation_bounded_feedback_exact_gate_001.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/2026-10-21/lt5_scalar_target_amplitude_limited_output_feedback_minimax_decomposition_001.md

**REC10** independently audited LT5 turn-1 in its declared linear-gain class, PASS_WITH_GUARDS, not a general verdict about turn-2 amplitude-limited nonlinear policies:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/rec10/2026-10-21/IW_REC10_ROT03_LT5_INFORMATION_VS_ACTUATION_EXACT_GATE_REFEREE_001_20261021.md

**INT8** shows that one finite fixed-sensor reset protocol can noiselessly separate the observable quotient while inversion gain diverges as measurement strength vanishes. This is an exact classical *fixed-sample* statement, not yet a growing-sample stochastic asymptotic:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/int8/2026-10-21/iw_int8_weak_protocol_quotient_identification_vs_bounded_actuation_bridge_001.md

**Geeky-S10**, *two* 2026-10-21 returns:
- exact fixed-time triangular factorization C_s=s(I+sH)^(-1)M, so deterministic co-axial resets preserve the passive sample rank and kernel while transforming *noise geometry*;
- an arbitrary-FINITE-number-of-weak-shots quadratic-storage bound, uniform over times and N: if P>=0, Pe=e and G^TP+PG<=0, then Σ b_j² <=[epsilon/(2-epsilon)] x0^TPx0 for all strengths 0<=s_j<=epsilon<1. In the scalar G=0 example the constant is attained in the supremum over finite N.
Sources:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s10/2026-10-21/geeky_s10_fixed_time_reset_passive_sample_triangular_equivalence_001.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s10/2026-10-21/geeky_s10_int8_weak_measurement_accumulation_ceiling_001.md

**R12 PRF11** already identified a conditional single-preparation Gaussian observation model and basic KL/Fisher/van Trees bridge, but used the older O(1) sensitivity ceiling. R13 re-evaluates this question using the newly established **O(epsilon) weak-record energy bound**, including *arbitrary N and adaptive selection* under an explicit common observation-law contract:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-19/IW_PRF11_R12_ADAPTIVE_GAUSSIAN_SENSOR_BUDGET_KL_FISHER_VANTREES_MINIMAX_001_20261019.md

The R12 dispatch has no verified recipient reply in its original thread. No BW ingestion/acceptance has been inferred from lack of reply. Currentness is based on full public GitHub primary text and bounded public dispatch reads.

## 1. Question after mature foundation subtraction

Old question: "Does one tiny nonzero sensor strength preserve noiseless identifiability?" INT8+Geeky already answer this for the model.

More incisive typed question: **With ONE physical preparation, arbitrary many causally chosen weak reset measurements, and independent fixed-variance Gaussian readout noise, does the entire statistical experiment retain nonzero decision information as per-shot strength epsilon→0?**

The external mathematical hosts are:
- Willems (1972) dissipation/available storage;
- Cover–Thomas (2006) relative entropy, mutual information, data processing, Gaussian channels;
- Torgersen (1991) comparison/deficiency of statistical experiments;
- Tsybakov (2009) minimax testing and estimation inequalities;
- adaptive experiment inference literature, which requires preserving conditional likelihood instead of assuming nonadaptive iid data.

All component theorems are mature. The conditional assembly below is not a novelty claim or physical transfer.

## 2. Full LEGAL hypothetical Gaussian model

Dimension n finite, fixed known unit sensor vector e in R^n, fixed known real matrix G. Let the original hidden preparation be x0=theta v for fixed known v in R^n and unknown scalar theta∈[-R,R], R>0. Assume 0<epsilon<1.

Free evolution between measurements is x'=Gx. At measurement j, the controller selects, **before** observing the j-th noise, a nonnegative waiting time tau_j and strength s_j∈[0,epsilon]. Both may be measurable functions of the earlier measured outcomes Z_1,...,Z_(j-1) and independent public seed U. The same functions and seed law are used under every theta; policies do NOT know theta.

Define premeasurement state x_j^-, ideal normalized signal b_j=s_j e^T x_j^- and deterministic reset x_j^+=Q_(s_j)x_j^- where Q_s=I-s ee^T. The observed scalar is

  Z_j=b_j+eta_j,   eta_j iid N(0,sigma²), sigma>0 FIXED independent of epsilon, time, signal and earlier history.

Critically, eta_j does NOT instantaneously alter x_j^+; the only measurement-induced state change is Q_s. Past noisy outcomes may influence LATER choices of tau and s, but for a frozen past history the map from x0 to x_j^- remains linear.

Assume an ellipsoidal certificate:

  P=P^T>=0,   Pe=e,   G^T P+P G<=0.                      (H)

Take an arbitrary chosen finite N, possibly depending on epsilon and unbounded as epsilon→0. Each epsilon experiment may have its own policy and N. Gaussian innovation likelihoods are well defined. The full dataset includes the seed if observed and choices/actions when logged; actions are generated by the common policy rule.

This is a *new conditional observation-law contract*, NOT an accepted physical law of NC's classical backaction, and still less a quantum instrument.

## 3. Pathwise energy of the sensitivity under *adaptive* selection

Fix a complete admissible hypothetical past outcome history h. Freeze all selected times/strengths to the numbers prescribed by the shared policy on that history. Then x_j^-(theta;h)=theta x_j^-(v;h). The conditional Gaussian observation mean is

  mu_j(theta;h)=theta c_j(h),
  c_j(h)=s_j(h) e^T x_j^-(v;h).

Although c_j(h) depends on the observed past, at the same frozen h it does NOT depend separately on theta. For each such h, Geeky-S10's deterministic storage telescope applies to the trajectory starting from v, including the chosen actions. Therefore:

  Σ_{j=1}^N c_j(h)²
     <= alpha_v(epsilon)
     := [epsilon/(2-epsilon)] v^T P v.                 (1)

This is a bound **on every frozen policy path**, not only an expected-value bound. It holds for any chosen finite N/timing, even when the choices were generated adaptively. The proof is the single-shot identity

  (s e^T x)^2
  = [s/(2-s)] [x^TPx-(Q_sx)^TP(Q_sx)]

followed by nonincrease of x^TPx during free evolution. Do not equate this to a theorem about truly outcome-dependent STATE RESET maps; that is a different source type.

## 4. Exact sequential KL and Fisher: all finite adaptive protocols

Let P_theta^pi be the joint law of the recorded sequence for a fixed admissible policy pi, and let P_0^pi denote the law for zero initial amplitude. At a common frozen history the two next-observation conditional laws are Gaussians N(theta*c_j(h),sigma²) and N(theta'*c_j(h),sigma²). The sequential KL chain rule yields exactly:

  D_KL(P_theta^pi || P_theta'^pi)
    = (theta-theta')²/(2sigma²)
      E_theta^pi Σ c_j(H_(j-1))²
    <= (theta-theta')² alpha_v/(2sigma²).             (2)

The same observable policy seed contributes zero relative entropy because its law is common to the parameter values. Adaptivity is LEGAL here because history is frozen in the conditional comparison.

The likelihood score is a Gaussian martingale transform, giving Fisher information:

  I_pi(theta)
    = sigma^(-2) E_theta^pi Σ c_j(H_(j-1))²
    <= alpha_v/sigma².                                (3)

All the bounds are independent of N. Under (H), alpha_v=O(epsilon) as epsilon→0.

## 5. EXPERIMENT LEVEL: near equivalence to a no-information experiment

Define the parameter-independent experiment F_pi on the SAME observable data space by Q_theta=P_0^pi for all theta. For theta∈[-R,R], equation (2) gives

  D_KL(P_theta^pi || P_0^pi) <= theta² alpha_v/(2sigma²).

Pinsker, using TV(P,Q)=sup_A|P(A)-Q(A)|, gives

  TV(P_theta^pi,P_0^pi)
    <= min{1, |theta| sqrt(alpha_v)/(2sigma)}.       (4)

By using the identity comparison kernel in one direction and an input-ignoring kernel simulating P_0^pi in the other, the Le Cam experiment distance (max of the two deficiencies) obeys

  Delta(E_pi,F_pi)
    <= min{1, R sqrt(alpha_v)/(2sigma)}
    = O(sqrt(epsilon)).                               (5)

The two experiments may have different and epsilon-dependent observation lengths, but for EACH epsilon the matching no-information experiment is built on the same measurable record space, including logged choices. The bound is uniform across all admitted policies and arbitrary finite N, so the sequence of full statistical experiments becomes asymptotically indistinguishable from a parameter-free experiment as epsilon↓0.

No statement here implies hidden states are identical, the noiseless row space collapses for fixed nonzero epsilon, or physical quantum experiments become equivalent.

## 6. SHARPER decision consequence: worst-case squared error collapses at O(epsilon), not merely O(sqrt epsilon)

Let

  J_pi := inf_{all measurable estimators theta_hat}
          sup_{|theta|<=R}
          E_theta^pi[(theta_hat-theta)²].

The zero estimator shows J_pi<=R². We derive a matching FIRST-ORDER lower bound, uniformly over all admitted pi, even with arbitrarily large finite N.

Take a two-point prior Theta∈{-R,+R}, each with probability 1/2. Write M=(P_+R^pi+P_-R^pi)/2 and t(z)=E[Theta|z]/R in [-1,1]. The optimal Bayes squared-error risk is

  BayesRisk = R²[1-E_M t(Z)²].                        (6)

Let I(Theta;Z) denote mutual information for this two-point prior. The binary posterior relative entropy obeys

  D_KL(Posterior(Theta|z) || Uniform{-R,+R})
    >= t(z)²/2                                      (7)

by binary Pinsker. Averaging gives E_M t²<=2 I(Theta;Z).

The standard information-radius identity, with fixed reference P_0^pi, gives exactly

  I(Theta;Z)
  = [D_KL(P_+R^pi||P_0^pi)+D_KL(P_-R^pi||P_0^pi)]/2
    - D_KL(M||P_0^pi)
  <= R² alpha_v/(2sigma²).                            (8)

Combining (6)-(8), and noting minimax risk >= Bayes risk,

  R² [1 - R² alpha_v/sigma²]_+
      <= J_pi <= R².                                  (9)

As epsilon→0, J_pi→R², **uniformly over every admitted adaptive policy and every finite N**, including N=N(epsilon)→infinity.

This bound applies to arbitrary BIASED estimators. It has a more informative epsilon→0 limit than plugging I_pi=O(epsilon) into a cosine-prior van Trees bound, which would approach R²/pi² rather than the exact no-information minimax R². This is a source-matched comparison of mature statistical techniques, not a new information inequality.

More generally, for a fixed target tau(theta)=a theta, the squared-error scales by a², provided the target does NOT itself change with the policy. A policy-dependent physical terminal target is a different problem and cannot be substituted silently.

## 7. EXACT toy controls and RATE SHARPNESS

Take scalar n=1, G=0, e=1, P=1, v=1. Choose all strengths s∈(0,1), zero waits, and N measurements on the SAME preparation. Then

  x_j^-=(1-s)^(j-1) theta,
  c_j=s(1-s)^(j-1),

and exactly

  S_N := Σ c_j²
      = [s/(2-s)] [1-(1-s)^(2N)].                     (10)

For independent Gaussian noise variance sigma², the complete sample has Fisher information S_N/sigma²; the matched linear-shrinkage estimator

  theta_hat
    = [R²/(sigma²+R² S_N)] Σ_j c_j Z_j

has exact worst-parameter MSE

  R² sigma²/(sigma²+R² S_N).                           (11)

As N→infinity over finite protocols, S_N↗s/(2-s), Geeky's bound is sharp. We can choose N(s)↑infinity so that (1-s)^(2N(s))=o(1). Thus the *best achievable risk improvement* is at least

  R² - R² sigma²/(sigma²+R² S_N(s))
    = (R⁴/sigma²) [s/(2-s)] + O(s²),

whereas (9) upper-bounds improvement by

  R²-J_pi <= (R⁴/sigma²) [s/(2-s)].

Thus the O(s) minimax-information-loss rate and even its leading coefficient are SHARP in this scalar classical subclass. We do not claim the shrinkage rule is finite-s minimax exact (only its proved risk upper bound is needed).

Reproduction table for R=1, sigma²=1/4, and N large enough that S_N≈s/(2-s):

s         S_infty        lower_minimax_MSE   shrinkage_upper_MSE
0.1       0.0526315789   0.7894736842        0.8260869565
0.01      0.0050251256   0.9798994975        0.9802955665
0.001     0.0005002501   0.9979989995        0.9980029955

The shrinkage upper values are for a limit of finite protocols (not proof that an infinite zero-time experimental schedule is physically admissible).

## 8. CRITICAL negative control: noise can scale with strength

The result is **not** a universal 'weak measurement destroys all information' statement. The fixed absolute innovation variance sigma²>0 is load-bearing.

Retain the SAME scalar deterministic readouts (10), but let each independent readout have variance sigma²(s)=sigma_0² s^p, p>=0. For an arbitrarily long finite protocol approaching S_infty, total Fisher information is

  I_s = S_infty/sigma²(s)
      = s^(1-p)/[sigma_0²(2-s)].

Then:
- p<1: I_s→0 (statistical collapse);
- p=1: I_s→1/(2sigma_0²) (nonzero finite information);
- p>1: I_s→infinity (arbitrarily strong information in the bare mathematical model).

This is a **conditional statistical thought experiment**, NOT a physical claim that an actual detector achieves any selected noise exponent. In particular, if measurement time, total intensity, available power, thermal disturbance, shot noise or quantum backaction is constrained, the admissible sigma²(s), number of shots and legal time horizon must be derived from that source first.

Similarly, unlimited fresh independent preparations replace one initial state by N separate resources and are OUTSIDE the one-preparation dissipation budget.

## 9. Relation to INT8, LT5 and prior R12, with STOP

- Geeky-S10's O(sqrt epsilon) record norm bound and INT8's exact noiseless quotient separation remain mathematically compatible. Noise-level statistical information goes to zero, despite algebraically nonzero rank for every epsilon>0.
- With fixed-variance Gaussian innovations, even arbitrary adaptive schedules with N(epsilon)→infinity cannot rescue nontrivial scalar-estimation advantage under the stated common P-storage.
- For bounded **operator gain**, Geeky's existing LT5 cross-application shows at most O(sqrt epsilon) guaranteed deterministic target improvement. R13's O(epsilon) concerns **Gaussian minimax squared error of the ORIGINAL fixed scalar preparation**, not the same controller/loss object.
- Hard-amplitude actuator limits from LT5 turn-2 are another distinct action class, not automatically covered.
- The full experiment bound (5) is an outcome-law comparison for a single declared parametric measurement model. It is not quantum process-tensor equality, a microcarrier equality or a result about actual DTC/PBH observables.
- The R12 Young (2026) augmented van Trees application is not refuted; (9) offers a sharper small-signal limit via an older two-point Bayes/information-radius argument.

No new project gate or front is opened. A possible source-native question remaining after this mature-host subtraction is: **what actual source-admitted noise-resource scaling and readout backaction are compatible with a physical sensor?** Without that contract, a general weak-measurement physics theorem is not earned.

## 10. Reproducible literature/host log, source hierarchy and provenance

Date: 2026-10-21. Public research-source access: full GitHub bodies listed in §0 and full prior R12 body. Latest Slack #iw-dispatch checked; no reply in original R12 thread, which is "UNKNOWN receipt", not scientific rejection.

External targeted (not exhaustive) search, with literal example queries:
- "Le Cam deficiency statistical experiments same parameter-independent distribution upper bound sup total variation loss decision theory"
- "mutual information upper bound KL to reference distribution average prior identity information radius posterior mean binary risk Pinsker"
- "adaptive sequential experiments KL chain rule Gaussian predictable measurements feedback"
- "Tsybakov Introduction to Nonparametric Estimation 2009 testing minimax methods KL inequalities pdf"
- "Willems dissipative dynamical systems part I storage function 1972 supply rate"
- "Cover Thomas Elements of Information Theory second edition mutual information relative entropy chain rule publisher Wiley"
- "Lattimore Szepesvari Bandit Algorithms Cambridge 2020 divergence decomposition adaptive experiments lemma"
- "Bayesian minimax information theoretic lower bound squared error mutual information binary prior posterior variance bound"

Verified reputable host records:
- J.C. Willems, "Dissipative Dynamical Systems Part I: General Theory", *Arch. Rational Mech. Anal.* 45:321–351 (1972), DOI 10.1007/BF00276493, publisher abstract inspected, plus author-hosted PDF retrieved as a text excerpt of storage/supply definitions; not a full theorem-level rederivation from the entire paper. https://doi.org/10.1007/BF00276493
- T.M. Cover & J.A. Thomas, *Elements of Information Theory*, 2nd ed., Wiley (2006), DOI 10.1002/047174882X; publisher Ch. 2 overview confirms chain rules and data-processing; entire monograph not read. https://doi.org/10.1002/047174882X.ch2
- E. Torgersen, *Comparison of Statistical Experiments*, Cambridge UP (1991), DOI 10.1017/CBO9780511666353; Cambridge preface/TOC read, not full proofs. https://doi.org/10.1017/CBO9780511666353
- A.B. Tsybakov, *Introduction to Nonparametric Estimation*, Springer (2009), DOI 10.1007/b13794; publisher TOC and minimax chapter scope read, not full chapter proof. https://doi.org/10.1007/b13794
- J. Hadad et al., "Demystifying Inference After Adaptive Experiments", *Annual Review of Statistics and Its Application* 12:407–423 (2025), DOI 10.1146/annurev-statistics-040522-015431; publisher abstract read, context only (not a proof of this source result). https://doi.org/10.1146/annurev-statistics-040522-015431

Primary algebra of §§3-8 is self-contained and checkable without reliance on a thin abstract theorem transfer. Reproduction of numerical table requires only (10)-(11) and elementary arithmetic; source software / physical data NOT_USED. No full literature citation-chain exhaustion, systematic-review completion, external peer-review or physical source validation claimed.

## 11. Frozen outcome / status

RESULT: EXACT_CONDITIONAL_STATISTICAL_BRIDGE / PRIOR_ART_ABSORPTION / QUANTIFIER_CHECK.
NEGATIVE_KNOWLEDGE:
  NOISELESS_RANK != STOCHASTIC_INFORMATION_AT_FIXED_NOISE;
  N_UNBOUNDED != FREE_NEW_PREPARATIONS;
  COMMON_STORAGE != COMMON_GAUSSIAN_NOISE_MODEL;
  UNIFORM_NOISY_LECAM_COLLAPSE != PHYSICAL_QUANTUM_PROCESS_STATEMENT;
  WEAK_ELLIPSOIDAL_CEILING != NONQUADRATIC_AVAILABLE_STORAGE_CEILING.

NO_CANON / NO_EXEC / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE.
GitHub content persistence/readback and Slack delivery must be independently verified; BW ingestion/recipient acceptance remain separate unknown states.
