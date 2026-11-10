---
artifact_id: IW_REC11_ROT011_MECH_S8_INT9_CD_SHARP_RANK_ONE_FIT_SE_THRESHOLD_REFEREE_001_20261110
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
date: 2026-11-10
kind: NONBLIND_INDEPENDENT_REFEREE_SOURCE_TYPED_MATH
source_first: BADACZ_REVIEW050_NATIVE_V2_FINITE_BAND_RESPONSES
prior: MECH_S8_ROT012_RANK1_FIT_SE_WITNESS; INT9_ROT008_FORWARD_TARGET_BOX
exposure: PUBLIC
source_blob: 1df29aff025755f9042628ec85752178b991d398
scope: EXACT_DECIMAL_AND_BINARY64_FRACTION_BUDGET
result_class: PASS_STRONGER_SHARP_RANK1_THRESHOLD / PASS_FORWARD_TARGET_COEXISTENCE / HOLD_NATIVE_JULIA_DOUBLE_BAND / HOLD_PHYSICAL_E4
claim_ceiling: NOMINAL_FIT_SE_RECTANGLE_AS_HYPOTHETICAL_DETERMINISTIC_BOX / NO_CONFIDENCE_COVERAGE / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
bw: GITHUB_PENDING_BW_INGEST
---

# REC11 ROT011 — sharp finite-source rank-one breakdown thresholds for Wu–Xu C/D band-response inversion

## 1. Review object and firstness

BADACZ REVIEW050 **first** measured the v2 original Wu–Xu code's model-internal finite band response `s_eff` (and its seven-point regression-fit marginal `se_s_eff`), with no physical source certification. MECH-S8 ROT012 **first** showed the C/D response columns near-collinear and supplied the explicit rank-one perturbation `C'=C+(0.002,0,0,0), D'=C'/5` with all eight individual perturbations below one reported fit SE, worst **0.9833754** pooled `Dc`, **0.7250200** direct `D2`. INT9 ROT008 **first** separated failure of C/D inverse identification from conditional robustness of the sum `C+D` under a *hypothetical* rectangular error model.

REC11 answers one strictly sharper referee question: **What is the actual minimum common multiplier rho of the reported coordinate-wise SE budgets that allows ANY 4×2 C/D matrix with rank at most one?** This was not determined by the one chosen Mech witness. This report computes an exact narrow bracket for the sharp threshold with a constructive full-four-row witness and a proof that no such witness exists below the threshold.

All input decimals were transcribed from the original **public** source, pinned:
`research/badacz/2026-11-08/data/kernel_analysis.json` Git blob SHA-1 `1df29aff025755f9042628ec85752178b991d398` at commit `11eeb1c37c21f19b2510e3bba5ae50169cbd5d79`.
Data rows `j=[22,28,34,62]`; C column `derived[j].C2`; D is separately `derived[j].Dc` (post hoc D0/D2 pooled) or `derived[j].D2` (direct k=2). Each entry uses `s_eff` and `se_s_eff`; no JLD2, Julia, unreported spectra or hidden physical data accessed. The unrelated source JSON contains four Infinity tokens and is not strict JSON as a whole: only finite selected fields enter this certificate.

## 2. Exact mathematical problem

Let `(c_j,u_j)` and `(d_j,v_j)` denote source center and positive marginal fit SE of C and D at the four j. The following is a **hypothetical deterministic** ambiguity model, NOT a frequentist confidence region:

`|c'_j-c_j| <= rho u_j`, `|d'_j-d_j| <= rho v_j` independently for every j.

Find the smallest `rho≥0` for which the two columns `c',d'` of the 4×2 matrix become proportional (or degenerate). The j22 intervals are strictly positive throughout the relevant brackets, hence any rank-one witness has `d'_j=lambda c'_j` with `lambda>0`.

Whenever `c_j-rho u_j>0`, the existence of **any** coordinate pair `c'_j,d'_j` with `d'_j=lambda c'_j` is EQUIVALENT to

`L_j(rho)=(d_j-rho v_j)/(c_j+rho u_j) <= lambda <= U_j(rho)=(d_j+rho v_j)/(c_j-rho u_j)`.

A single positive `lambda` is feasible over **all four rows** iff

`max_j L_j(rho) <= min_j U_j(rho)`.

This criterion is sufficient by intersecting intervals for `c'_j`:
`[c_j-rho u_j,c_j+rho u_j] ∩ [(d_j-rho v_j)/lambda,(d_j+rho v_j)/lambda]`. Take any point in every nonempty intersection and `d'_j=lambda c'_j`.

The earliest incompatible pair in the source is:
- **pooled Dc:** j22 lower vs **j28** upper;
- **direct D2:** j22 lower vs **j62** upper (the j62 direct D2 center is actually NEGATIVE: −0.0013523344406164428).

Let `k=28` for pooled and `k=62` for direct. The exact critical rho solves

`(d_22-rho v_22)(c_k-rho u_k)=(d_k+rho v_k)(c_22+rho u_22)`.

This is a quadratic equation with coefficients in `Q` when using the frozen JSON decimal strings. Within the relevant positive interval, the left j22 bound is strictly decreasing and upper j28/j62 bound is increasing. Thus the pair's strict separation for rho below the root PROVES no full-four-row rank-one solution. At the exact root the other two rows' lambda intervals are slack, so the root is also sufficient for all four rows. This establishes GLOBAL sharpness over the stated coordinate box (not just a local numerical optimizer).

## 3. Exact rational certificate and stronger numerical result

| source D variant | exact rational lower bracket | exact rational upper bracket | numerical critical rho | binding rows |
|---|---:|---:|---:|---|
| pooled Dc | 0.70900120 | 0.70900130 | **0.709001245689070** | 22 lower, 28 upper |
| direct D2 | 0.46669870 | 0.46669880 | **0.466698741419195** | 22 lower, 62 upper |

The verifier uses Python stdlib `Fraction` on **source decimal tokens** and independently `Fraction.from_float(float(token))` on the corresponding **exact binary64 dyadics**, confirming the signs of the two quadratic polynomials at both rational brackets, the separated incompatible pair at the lower endpoints, and **full four-row exact rank-one witnesses** at the upper endpoints.

The following entries are display-rounded; rigorous comparisons use the unrounded Fraction witness constructed from exact rational interval intersections:

| variant | j | C' | D' |
|---|---:|---:|---:|
| Dc | 22 | .3452018699026313 | .0694430483524686 |
| Dc | 28 | .1367688219337002 | .0275133037875230 |
| Dc | 34 | .0722233021397727 | .0145289081547613 |
| Dc | 62 | .0098233868114432 | .0019761362402946 |
| D2 | 22 | .3405160060682330 | .0706355242249808 |
| D2 | 28 | .1423483825923824 | .0295282819245104 |
| D2 | 34 | .0722233021397727 | .0149817650770865 |
| D2 | 62 | .0067391131182464 | .0013979395371605 |

Exact proportionality `D'_j=lambda C'_j` across all four j is guaranteed **before decimal display rounding**:
`lambda≈0.201166489544381` for pooled and `lambda≈0.207436722404253` for direct, using the upper endpoint witnesses. Max normalized changes in this constructive certificate are respectively **0.709001265** and **0.466698781**, strictly below its exact allowed upper brackets.

**Material delta from MECH-S8:** the earlier existential 0.983 / 0.725 fit-SE witnesses are valid but far from optimal. For **direct D2, less than 0.467 of each marginal reported SE is enough** to produce rank one. The source table has no deterministic full-rank robustness guarantee at the one-fit-SE scale, under either D variant. That is a stronger **mathematical fit-budget** result, not evidence of genuine singular source physics.

## 4. The positive forward combined target survives

Use each rank-one witness at j22 and the explicitly conditional INT9/Badacz A1 response law for *simultaneous doubling* C and D:
`Delta_CD=-log10(1+C'_22+D'_22)`.
For pooled `Dc`, `C'_22+D'_22≈0.4146449182550999`, `Delta_CD≈−0.15064744 dex`.
For direct `D2`, the sum `≈0.4111515302932138`, `Delta_CD≈−0.14957365 dex`.
Both sit inside INT9's separately established one-fit-SE **hypothetical** forward intervals, and far from the count-number-only `Delta≈−0.038720 dex`.

Therefore even at EXACT rank-one inverse collapse, this particular target is still well defined for each *given response vector* and remains box separated from the count-only surrogate at j22. Conversely there are no data here to infer true source band multipliers separately. The forward A1 expression is an **unexecuted joint-band forecast**: source finite single-band secants, sum-rule residuals and the observed REVIEW054 j22 finite-amplitude failure forbid upgrading A1 to an exact native two-band law.

## 5. Falsification status and guards

**PASS_MATH**: The independent exact-rational one-parameter optimality proof identifies the **sharp minimal per-coordinate nominal fit-SE radius** at which 4×2 C/D rank may be lost. Both pooled/direct source variants tested. Stronger than an arbitrary witnessed 0.983 SE.

**HOLD_STATISTICAL_COVERAGE**: A regression standard error is not an independent coordinate guarantee, joint covariance model, confidence region, physical systematic, or certified derivative uncertainty. A statistical posterior or experimental noise correlation could exclude these rank-one matrices; an unknown physical source discrepancy could exceed them. We prove a conditional deterministic geometry statement only.

**HOLD_NATIVE_JULIA**: Neither source original 10D weak-rate/hadron tables nor simultaneous C×2+D×2 perturbations were replayed. `s_eff` is a finite perturbation/secant of an adopted numerical B_exec target, not a physically validated Jacobian.

**HOLD_E4/JCAP**: No transfer to original differential hadron spectra, physical Y_P/β bounds, restored Fig.5 producer, strict ODE guarantee, or novelty. Owner Mech-S8 holds physical-source choices; Badacz holds original finite-response experiment. No automatic audit cascade or BW ingest.

### Source references
- BADACZ source: https://github.com/wmakiela-tech/Nash-iw-research/blob/11eeb1c37c21f19b2510e3bba5ae50169cbd5d79/research/badacz/2026-11-08/IW_BADACZ_WUXU_BAND_RESOLVED_HADRON_RESPONSE_KERNEL_REVIEW_050_20261108.md
- MECH-S8 prior: https://github.com/wmakiela-tech/Nash-iw-research/blob/b2ba1d79df095ec1ee19a230c30426a1796207bd/research/mech-s8/2026-11-10/IW_MECH_S8_ROT012_WUXU_E4_C_D_BAND_SOURCE_IDENTIFIABILITY_AND_ONE_SIGMA_RANK_ONE_WITNESS_001_20261110.md
- INT9 prior: https://github.com/wmakiela-tech/Nash-iw-research/blob/988ceacd4e1f2652af7654302935796c3736fff5/research/int9/2026-11-10/iw_int9_rot008_CD_forward_box_robustness_vs_source_inverse_rank1_gate_001.md

**Return:** `IW_REC11_ROT011_MECH_S8_INT9_CD_SHARP_RANK_ONE_FIT_SE_THRESHOLD_REFEREE_001_20261110`.
