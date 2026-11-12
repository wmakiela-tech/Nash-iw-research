---
artifact_id: IW_REC11_ROT023_M14_ROT046_ASYMMETRIC_REFERENCE_COST_EXACT_MINIMAX_REFEREE_001_20261112
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
date: 2026-11-12
exposure: PUBLIC
review_class: I1_NONBLIND_INDEPENDENT_CLASSICAL_GAUSSIAN_MATH_COST_EXTENSION
source_firstness: M14_ROT046_KNOWN_FIELD_REFERENCE_GAUSSIAN_MINIMAX
claim_ceiling: SYNTHETIC_REFERENCE_TWO_SESSION_STABLE_BETA_PLUS_BOX_D / NO_NATIVE_NV / NO_NOVELTY / NO_PHYSICAL_GAIN / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REC11 ROT023 — Independent M14 ROT046 referee: sharp Gaussian minimax for unequal target/reference sample costs

## Source, firstness, and scientific ceiling

M14 ROT046 **FIRST** proved exact all-estimator Gaussian minimax for a known-field reference, arbitrary stable per-channel calibration offsets and possible independent bounded run mismatch, in the unit-cost model. REC11 independently audited that result and derives the following **different-cost** theorem using the same source-typed Gaussian assumptions; no claim of new fundamental mathematics.

Original owner primary note was directly read and source-pinned: public GitHub commit `1688dd3aa32c2a6d5b7f9116f0e51996cfbc6e51`, Git blob `b8c042961a8e771a328bc2b95c0b1f401721e809`:
https://github.com/wmakiela-tech/Nash-iw-research/blob/1688dd3aa32c2a6d5b7f9116f0e51996cfbc6e51/research/m14/2026-11-12/iw_m14_rot046_known_field_reference_calibration_stability_and_optimal_resource_001.md

External actual source Schall et al, *Laser-enhanced quantum sensing boosts sensitivity and dynamic range*, Nat Commun **17** (2026), 10825, DOI 10.1038/s41467-026-78386-z, published October 22 2026. Authors explicitly distinguish photon-shot-noise **limit** from real achieved sensitivity with technical noise. The original article does NOT demonstrate this synthetic two-session reference, an actual stable calibration offset, Gaussian equal-variance shot model, measured c_T/c_R cost, D or Hε.

## Exact mathematical model

r=4 tetrahedral axes `a1=(1,1,1), a2=(1,-1,-1), a3=(-1,1,-1), a4=(-1,-1,1)` (r=3 uses first three). Unknown target z∈R³ and KNOWN externally anchored reference z_ref∈R³. Each channel has arbitrary unbounded β_i shared between target/ref sessions, plus target mismatch |d_i|≤D:
`T_ij=a_i.z+β_i+d_i+ε_ij`, `R_ij=a_i.z_ref+β_i+ε'_ij`, with mutually independent centered Gaussian variances σ² per elemental shot. Target shot cost c_T>0; reference shot cost c_R>0, common across all channels. Total deterministic continuous cost budget B=Σ_i(c_T n_iT+c_R n_iR). Adaptive repetitions within those r channel types and any estimator including biased allowed. Integer realizations subject to divisibility.

Let `C=(sqrt(c_T)+sqrt(c_R))²`.

**SHARP GLOBAL SQUARED EUCLIDEAN MINIMAX risks:**

- **four axes:** `R4*=3σ² C/B+D²`;
- **first three axes:** `R3*=(9/2)σ² C/B+3D²`.

The exact optimal per-channel spend is `b_i=B/r` and **shot count ratio** `n_iT/n_iR=sqrt(c_R/c_T)`. This reduces to M14's original unit-cost formulas `12σ²/B+D²` and `18σ²/B+3D²` when c_T=c_R=1.

### Upper bound and variance allocation

Subtract reference means and add known `a_i.z_ref`, getting `X_i=a_i.z+d_i+ε_i`, independent `var(ε_i)=σ²(1/n_iT+1/n_iR)=σ²/q_i`, where `q_i=n_iT n_iR/(n_iT+n_iR)`.

The resource Cauchy inequality

`(c_T n_iT+c_R n_iR)(1/n_iT+1/n_iR) >= C`

is equality iff `n_iT/n_iR=sqrt(c_R/c_T)`; thus `q_i<=b_i/C`. The Gaussian profiled Fisher is `I=σ^-2 Σ_i q_i a_i a_i^T`.

For r4, `A4^T A4=4I3`, `tr I=3Σq_i/σ²<=3B/(Cσ²)`; hence by `tr I^-1>=9/trI`, the noise risk is >=`3σ²C/B`, reached by equal b_i and optimal T/R ratio. For r3, `A3` invertible with each column of `A3^-1` squared norm `1/2`, so `tr I^-1=(σ²/2)Σ1/q_i>=(σ² C/2)Σ1/b_i>=(9σ² C)/(2B)`, attained at b_i=B/3 with optimal T/R split.

The exact worst squared bias of equal optimal estimates is `max_|d|<=D ||A4^T d/4||²=D²` and `max_|d|<=D ||A3^-1 d||²=3D²`. These are PSD convex functions maximized at signed cube vertices; 16/8 vertices independently enumerated.

### Matching lower bound INCLUDING biased/adaptive

The original M14 diffuse Gaussian Bayes prior method on the target and nuisance β yields the profiled resource-bound noise floors for any procedure and nonanticipating sequential adaptive repeats. For the mismatch add hidden sign S=±1, `z_S=u+Sv`, `d_i,S=-S a_i.v`. Choose `v=D e1` for four axes (all projections have magnitude D), or `v=D(1,1,-1)` for first three (all projections D). Both target and reference raw likelihoods are **identical for S**, so its squared error `||v||²` is an unavoidable additive D² or 3D² to the diffuse-u noise risk. Positive upper construction matches the lower bound. No physics is deduced.

## New conditional experimental budget crossover

Compare four-axis reference `R_ref=3σ² C/B+D²` with M14 ROT044's DIFFERENT source-unverified direct hidden-jitter protocol, now with per-shot target cost c_T:
`R_direct=3σ² c_T/B+(H ε)²`.

**Reference wins iff** `D<Hε` **and**
`B > 3σ² [C-c_T]/[(H ε)²-D²]`.
No crossover if D≥Hε; if c_T=c_R=1 the owner unit-cost result `B>9σ²/[(Hε)²−D²]` is recovered. This comparison requires separate validation of both mutually distinct nuisance/noise contracts before any real-world decision.

**Exact integer-feasible example** c_T=1,c_R=4,σ²=1,D=1/20,Hε=1/10,B=3600: C=9 and optimal T/R shots ratio 2:1. Four axes each use nT=300,nR=150 for cost 900 per axis; R_ref4=27/3600+1/400=**1/100=.0100**. First three each use nT=400,nR=200, R_ref3=81/7200+3/400=**.01875**. Direct four-axis at same cost R_direct=3/3600+1/100=**13/1200=.010833333...**. Crossover **B>3200**, all exact.

## Independent executed tests / custody / limits

Independent LOCAL pure stdlib Python Fraction script (not imported from M14) ACTUALLY EXECUTED: exact tetrahedron Gram and inverse, 24 signed cube vertices, 56 positive rational shot cost inequality tests, exact two integer-feasible full design risks and exact crossover. Deterministic JSON/stdout are reproducible. Local six-member ZIP `IW_REC11_ROT023_M14_REFERENCE_ASYMMETRIC_COST_MINIMAX_REPRO_001_20261112.zip` SHA256 **b1a0e9223f57699dc6c1f5f40442bb8be10faf2d7ccd0375e27c10f6175ea141**; archive CRC PASS, SHA five payload members PASS, isolated extraction and replay JSON/stdout BYTE IDENTICAL PASS. Local ZIP not represented as uploaded to GitHub.

No actual sensor calibration reference, real NV per-shot costs/correlations, Gaussian technical noise proof, native timing, fT/√Hz gain, physical PBH/GR/GW/J3K inference, mathematical novelty, prior-art global survey or CANON/EXEC. No owner M14/AUD1 approval or BW science receipt established by reporting.

RETURN_ID: `IW_REC11_ROT023_M14_ROT046_ASYMMETRIC_REFERENCE_COST_EXACT_MINIMAX_REFEREE_001_20261112`.
FINAL `PASS_M14_ROT046_SCOPED / PASS_ASYMMETRIC_COST_ALL_ESTIMATOR_MINIMAX / PASS_EXACT_COST_CROSSOVER / HOLD_NV_NATIVE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
