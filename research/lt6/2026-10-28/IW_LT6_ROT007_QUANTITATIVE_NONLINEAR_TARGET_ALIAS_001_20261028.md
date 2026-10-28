---
artifact_id: IW_LT6_ROT007_QUANTITATIVE_NONLINEAR_TARGET_ALIAS_001_20261028
created_at: 2026-10-28
origin_cell: IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_04 / LT6
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: SOURCE_TYPED_CLASSICAL_QUANTITATIVE_IFT / CONSTRUCTIVE_TARGET_ALIAS / SYNTHETIC_REPRO_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_MATHEMATICAL_NOVELTY / NO_CANON / NO_EXEC / NO_PHYSICAL_PBH_BBN / NO_NATIVE_WUXU_JULIA10D
---

# LT6 ROT007: exact nonlinear data alias with different target — local certificate

**Prior owners and subtraction.** Mech-S7 [ROT030](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s7/2026-10-26/mech_s7_rot030_basis_enlargement_finite_observation_nullspace_nonlinear_gate_001.md) FIRST enlarged the positive, sum-preserving antinucleon source family from 7 to 11 bins, retaining three exact source moments and six conditional X_nuc targets. [MT14 ROT009](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt14/2026-10-27/iw_mt14_rot009_frontb_borsuk_ulam_exact_nonlinear_source_alias_001.md) FIRST used classical Borsuk–Ulam to guarantee, subject to continuity and positivity, an antipodal source pair with exactly the same six **full nonlinear** readouts for each small radius. Critically, this does **NOT** establish variation in a seventh heldout target. Mech-S7 [ROT031](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s7/2026-10-27/mech_s7_rot031_source_sobolev_regularization_basis_artifact_global_smooth_nonlinear_gate_001.md) compares bases and finds an extremely ill-conditioned 9×11 operator; higher smoothness did not automatically improve target accuracy.

## T007.1: constructive exact nonlinear target-varying fiber (classical IFT)
Let F:B_R(0)⊂R^n→R^m, T:B_R(0)→R be C², n>m, A=DF(0) full row rank, β=1/σ_m(A), ||D²F||≤L, ||D²T||≤K, G=||DT(0)||. Assume a unit v∈ker A has α=DT(0)v≠0. Set D=GβL+25K/32. For t>0 with t≤4R/5, βLt≤1/4 and Dt≤|α|/2, there exist TWO EXACT sources

    c±(t)= ±t v + A† y±(t),   ||y±(t)||≤Lt²

satisfying

    F(c+)=F(c−)=F(0)  EXACTLY,
    ||c+−c−||₂ ≥ 2t,
    |T(c+)−T(c−)| ≥ |α|t >0.

**Proof.** N(c)=F(c)−F(0)−Ac satisfies ||N(c)||≤(L/2)||c||² and ||DN(c)||≤L||c||. Solve y=−N(±tv+A†y) by Banach contraction on ||y||≤Lt²: ||c||≤5t/4, self-map norm ≤(25/32)Lt², contraction constant ≤(5/4)βLt≤5/16. Thus F(c±)=F(0). Orthogonality of ker A and range(A†) gives the source distance. Taylor's theorem gives |T(c±)−T(0)∓αt|≤[GβL+25K/32]t²; subtract and use Dt≤|α|/2. This is a **source-typed application of mature quantitative implicit-function / contraction theory**. No novelty priority.

If the source parameter ball is mapped injectively into strictly positive and moment-conserving physical source functions, the two constructed points are also distinct legal sources. Admissibility cannot be presumed from the abstract theorem.

## T007.2: certifying transversality when gradients have bounded error
Suppose computed Ã,ĝ have **certified source-valid** ||A−Ã||₂≤ε_A, ||g−ĝ||₂≤ε_g, g=DT(0), and s=σ_m(Ã)>ε_A. Then

    dist(g,row A) ≥ ||(I−P_row Ã) ĝ||₂ − ε_g
                      − [ε_A/(s−ε_A)] ||ĝ||₂.

**Proof.** Weyl gives σ_m(A)≥s−ε_A. For unit x∈row A write x=Aᵀλ with ||λ||≤1/(s−ε_A), giving dist(x,row Ã)≤ε_A/(s−ε_A). The equal-dimensional projector-gap identity and triangle inequality yield the claim. A **positive lower bound** gives a unit v∈ker A with α≠0, permitting T007.1. This is a classical Wedin/sinTheta-style bound, not a novelty claim.

**STOP:** Mech ROT030–031 extremely small singular values (~1e−11 and ~2.79e−13 in distinct matrices). No physically verified ε_A or ε_g currently exists for subtabulated hadron sources. Solver variants, MC stress and a small finite LP gap do not certify the real Jacobian, let alone original Julia 10D.

## Independent examples and checks
F(x,y,z)=(x+z²/2,y+z²), T(x,y,z)=z+0.2x. Exact fibers c±=(-t²/2,−t²,±t) have F(c±)=(0,0); at t=.1, T(c+)=.099 and T(c−)=−.101, target difference .2 versus certified lower bound .1. The naive first-order null ±t e_z does NOT have identical finite F; one must solve for second-order corrections.

**Necessary warning:** T_flat=F_1+F_2 is constant on every fiber, so MT14's antipodal alias need not differ in that target. With T_even=z² the first derivative criterion fails although each fiber point differs from T(0) at order t²: the transverse-gradient condition is sufficient, not necessary.

**Reproduction:** local self-contained NumPy code checked four exact fiber amplitudes and 100 independently generated controlled-Hessian quadratic C² cases; all tests PASS. A separate perturbative-gradient toy had s=1, ε_A=√.0005 and ε_g=.01, with positive certified transverse lower ≈.9644255. This synthetic numerical value is not a real Mech-source error bound.

**Independent corrective source:** [Badacz REVIEW007](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/badacz/2026-10-27/IW_BADACZ_LT6_ROT004_EVENT_CERTIFICATE_CROSS_FAMILY_CHECK_REVIEW_007_20261027.md) independently verified LT6 ROT004 but correctly noted its true-event m,F require computable tube bounds, first-crossing isolation and explicit monotonicity for piecewise-C1 numerical guards. Also distinguished the special event-manifold Q bound (.00591) from the general (.0179). REV026 §6.9c preserves this reviewer's priority; NOT a new LT6 theorem or a REC10/SW verdict.

**Mature literature:** classical constant rank (Stanford Math 215B Th44), Banach contraction (Cornell CS4220 27 Mar 2026), Wedin singular subspaces (Yuxin Chen, Spectral Methods §2.4.2). No claim to new mathematics, physics, PBH/BBN/Yp/DH, BW ingest, EXEC or canon.

**Verified working book:** [REV026 native Docs](https://docs.google.com/document/d/1ZBkboLN9t-rf07V3ZB1PKfoTuYheumC4w5eSM_PD5WE/edit) and [REV026 exact GitHub incremental paragraph mirror](https://github.com/wmakiela-tech/Nash-Priv/blob/main/living-theory/2026-10-28/REV026/README.md). Complete local report, exact scripts, JSON, SHA in Moderator's ZIP. Storage/readback != independent referee != physical validation.
