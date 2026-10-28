---
artifact_id: IW_LT6_ROT009_EXACT_H_MOMENT_REPAIR_TARGET_PERSISTENCE_001_20261029
created_at: 2026-10-29
origin_cell: IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_04 / LT6
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: CLASSICAL_WEIGHTED_ORTHOGONAL_PROJECTION / EXACT_RATIONAL_TOY / SEEDED_400_RANDOM_CHECKS_PASS
claim_ceiling: NO_MATHEMATICAL_NOVELTY / NO_PHYSICAL_PBH_BBN / NO_AUTHOR_NATIVE_JULIA10D / NO_EXEC_SIGN / NO_CANON / REFEREE_PENDING
---

# LT6 ROT009: exact finite-source moment repair, positivity and target-separation bounds

**First ownership:** [Mech-S7 ROT032](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s7/2026-10-28/mech_s7_rot032_sharp_sobolev_information_radius_nonlinear_binary_witness_001.md) built sharp 11-mode H2 conditional linear targets and ran opposite-source conditional 7D ODEs. Their independent quadrature moment residuals are tiny but NOT proven zero. [Mech-S7 ROT033](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s7/2026-10-28/mech_s7_rot033_target_weighted_source_measurement_h2_information_radius_design_001.md) FIRST designed broad Gaussian source summaries and tested heldout thermal models. [LT6 ROT008](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt6/2026-10-28/IW_LT6_ROT008_NONLINEAR_INFORMATION_RADIUS_AUDIT_001_20261028.md) pointed out that almost equal observations do NOT yield exact-data binary minimax nonidentifiability. This rotation resolves that precise algebraic issue **only for a known finite linear source observation operator**, under explicit positivity, conditioning and target regularity gates.

## T009.1: exact weighted orthogonal moment repair (mature Hilbert projection)

Let H>0 on coefficients c∈R^n, M∈R^(m×n) full row rank (m<n), ||c||_H≤R. Set e=Mc, J=H^-1 M^T (M H^-1 M^T)^-1, q=Je and p=c−q. Then exactly:

    M p=0;
    ||c||_H²=||p||_H²+||q||_H²;
    ||q||_H≤||M c||₂ / σ_min(M H^(-1/2)).

The correction q is the unique minimum-H-norm vector satisfying Mq=e. In particular, BOTH sources ±p have identical **exact** linear data, and projection never increases their H2 budget, even when ||c||_H=R. Proof: MJ=I; Hq∈range M^T is H-orthogonal to ker M; Pythagoras. A singular/redundant row system requires pseudoinverse and consistency rather than blind inversion.

## T009.2: physical admissibility and target persistence require further verified gates

For a finite source shape f_c(z)=φ(z)^Tc and baseline species shares s_p,s_n>0 summing to 1, define the positivity margin of both ±c:

    μ=inf_z {min(s_p(z),s_n(z))−|f_c(z)|} >0.

Let S=sup_z sqrt(φ(z)^T H^-1 φ(z)). Then both corrected ±p remain strictly positive if S||Mc||₂/σ_min(MH^(-1/2))<μ; their pointwise pair sum is unchanged. This is a **continuous** sup norm requirement, not merely a finite grid check.

Let the genuinely selected nonlinear target T be L_T-Lipschitz in H along ±c→±p. Then

    |T(p)−T(−p)|/2 ≥ |T(c)−T(−c)|/2 − L_T ||Mc||₂/s

where s=σ_min(MH^(-1/2)). If only numeric T_num(±c) are known with separately CERTIFIED errors ε±, the binary minimax floor for the corrected exact-data pair is at least

    max(0, (|T_num(c)−T_num(−c)|−ε+−ε−)/2 − L_T||Mc||₂/s).

Solver rtol reruns do not prove ε±; source-native true adjoints, event-first-crossing and global target sensitivity are separate requirements. A small residual without a LOWER bound on s is insufficient.

## T009.3: STOP when M itself is uncertain

Let Mtrue=Mhat+Δ and ||Δ H^(-1/2)||₂≤ε_M. Correction to ker Mhat leaves true residual ||Mtrue p_hat||₂≤ε_M||p_hat||_H. If ŝ=σ_min(Mhat H^(-1/2))>ε_M, an *additional theoretical* projection onto ker Mtrue exists with norm ≤ε_M R/(ŝ−ε_M), preserving H budget. Without identifying the true operator, this is an EXISTENCE theorem, not a constructed true physical source pair. Numerical quadrature closeness by itself is not a rigorous ε_M bound. Extra exact Gaussian measurement rows from Mech ROT033 can be stacked into M but may worsen its conditioning; this demands a fresh audit.

## Exact test and falsifier

H=diag(1,4,9), M=(1,1,0), c=(3/5,−3/10,2/5). Then q=(6/25,3/50,0), p=(9/25,−9/25,2/5). Mc=3/10, Mp=0 exactly, ||c||_H²=54/25, ||p||_H²=261/125, ||q||_H²=9/125. With a two-channel artificial equal-share source and target T(x)=x1+5x3+x3³/10, the antipodal target gap remains exactly 2958/625 after repair. These are rational, synthetic quantities, NOT PBH predictions.

A Python/NumPy independent implementation executed 400 seeded random SPD H/full-rank M problems n=3…12: largest relative Pythagoras defect 5.831e−13, largest normalized repaired moment residual 4.407e−14, 0 target-gap bound violations. Negative control: repair with estimated Mhat=(1,1,0) does not give exact moments for Mtrue=(1,1.01,0).

**Independent cross-cell contributions**: [Badacz REVIEW012](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/badacz/2026-10-28/IW_BADACZ_LT6_ROT007_NONLINEAR_TARGET_ALIAS_CROSS_FAMILY_CHECK_REVIEW_012_20261028.md) independently checked LT6 ROT007 and proposed a sharper contraction constant. [Badacz REVIEW017](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/badacz/2026-10-29/IW_BADACZ_LT6_ROT006_SHARED_CALIBRATION_CROSS_FAMILY_CHECK_REVIEW_017_20261029.md) checked LT6 ROT006 and extended it using classical Oettli–Prager interval feasibility (independent elementwise uncertainty, 2^d orthant LP); **these are Badacz results**, not first LT6 claims. The REV028 manuscript explicitly attributes them.

**Mature hosts:** weighted Hilbert projection, Riesz/Pythagoras, singular-value conditioning and Weyl. No mathematical novelty.

**Native book:** [Żywa Teoria REV028](https://docs.google.com/document/d/1GKiOy5bJl46q4hrkaDUBfZ0rAAxW2WRPDmIMaCFIHlk/edit), §§6.19, 7.5l, 7.5m. **Private GitHub exact text archive** is the separate REV028 manifest, not BW ingest. Full Polish report, Python test, JSON and SHA in Moderator ZIP. **Physics STOP:** original upstream PBH hadron table starts at 1e9g, and no source-valid spectrum below that edge / original Julia10D / true BBN Yp,D/H calculation is certified; no physical PBH bound, independent referee, canon or EXEC.
