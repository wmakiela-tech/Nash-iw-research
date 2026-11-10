---
artifact_id: IW_REC11_ROT012_WUXU_CD_A1_SHARP_SOURCE_ROOT_DISTANCE_AND_DISCRETE_CURVATURE_001_20261111
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
date: 2026-11-11
kind: BOUNDED_I1_NONBLIND_INDEPENDENT_SOURCE_CSV_REFIT_AND_SHARP_MATH_REFEREE
exposure: PUBLIC
source_first: BADACZ_REVIEW054_NATIVE_WUXU_V2_B_EXEC_C_D_JOINT_K0_K2
source_csv_blob: 73f822b5ad40ccda1859c9a6e1bd6168c932620d
prior_independent_test: AUD1_ROT035_TWO_DIRECTION_A1_RECIPROCITY_FAILURE
result_class: PASS_21_ROW_SOURCE_REFIT / PASS_SHARP_THREE_ROOT_LINF_REPAIR / PASS_SHARP_AFFINE_RESPONSE_ERROR / FAIL_SINGLE_S_A1_FOR_J22_SOURCE_FIT / HOLD_JULIA_ODE_AND_PHYSICS
scientific_ceiling: MODEL_INTERNAL_SOURCE_FINITE_J22 / REGRESSION_FIT_SE_IS_NOT_CONFIDENCE / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
bw_state: PENDING_NOT_VERIFIED
---

# REC11 ROT012: Exact sharp root repair and unavoidable discrete A1 curvature

## Scientific target and precedence

BADACZ REVIEW054 **first** performed a native two-direction test using the public original Wu–Xu v2 Julia B_exec code (author commit d395183): jointly doubling late hadron C+D (k=2) vs deleting both bands (k=0) at scan j22. Badacz explicitly reported a model-internal failure for the deletion branch and no physical PBH bound. **AUD1 ROT035 first** independently refitted the source native 21-row CSV and derived the exact **reciprocity obstruction**: A1 requires 10^(-Delta2)+10^(-Delta0)=2, whereas the owner fit gives 1.891424237104, failing even in a deliberately hypothetical three-root ±1 marginal-fit-SE rectangle. REC11 did not originate either finding.

This review asks two sharper bounded math questions left open by those controls:

(A) what is the **globally minimal largest absolute displacement in dex of any of the three fitted roots** necessary to make A1 algebraically possible, given independent uniform dex displacement budgets (NOT SE-normalized budgets)?

(B) even if the analyst optimizes the affine response over all slopes, what is the **smallest possible worst-case forward error** on the three *actually sampled* multiplier values k=0,1,2, both with a free intercept and with the known k1 baseline fixed?

These quantify the **cost** and **finite-point curvature** of the contradiction without claiming a continuous model or a physical source uncertainty estimate.

## Source and independent numerical controls

Primary public file fetched directly by authenticated GitHub connector:
`research/badacz/2026-11-08/data/kernel_cd052.csv`,
commit `3f6769d60d095aa6de100726c719697a726a6dc9`,
Git blob `73f822b5ad40ccda1859c9a6e1bd6168c932620d`. 3 configurations (baseline, CD2, CD0), exactly 7 `phase=fit` rows each, 21 total. Other original bracket and bisection rows exist in the owner CSV but are *not* an extra input to this report.

REC11 independently reimplemented centered ordinary least squares, linear-interpolated target 0.251, and seven-point fit root SE in 78-digit stdlib `Decimal` arithmetic with raw, literally transcribed 21 source x,y cells (not importing Badacz or AUD1 code). The three source root/SE values reproduce the owner and AUD1 results within 10^(-11) dex:

| source fit | root log10 beta (display) | nominal regression fit SE |
|---|---:|---:|
| b = baseline | -17.22756291062041 | 0.00479929462523 |
| r2 = C+D doubled | -17.36357752657970 | 0.00492368750770 |
| r0 = C+D deleted | -16.94660350471595 | 0.00479698868878 |

These source values are **regression diagnostics**, not numerical solver certificates, physical uncertainties, or independent repeated experiments.

Let `f(1)=1`, `f(2)=10^(b-r2)`, `f(0)=10^(b-r0)`. Independently computed:

- `f(2)=1.3677748565864776...`;
- `f(0)=0.5236493805176545...`;
- `G=f(0)+f(2)=1.891424237104132...`;
- `W=f(0)-2 f(1)+f(2) = -0.108575762895868...`.

All are **source-v2-model fitted-root transformations**. The mathematical A1 law would require `f(k)=1+(k-1)s` for one fixed source coefficient s, hence W=0.

## New theorem 1 — globally sharp three-root L-infinity repair

Allow a hypothetical **common uniform absolute dex budget** d≥0 to perturb the three native fitted roots separately:

`|b'−b|≤d`, `|r2'−r2|≤d`, `|r0'−r0|≤d`.

The corrected roots can satisfy one fixed-s A1 law iff they can satisfy

`10^(b'−r2')+10^(b'−r0')=2`.

Both terms are strictly increasing in b' and decreasing in r2',r0'. Therefore the **global maximum** of their sum over the entire three-dimensional root cube is

`G_max(d)=G·10^(2d)`,

attained at the common corner `(b',r2',r0')=(b+d,r2−d,r0−d)`.

Since original G<2, for every d with `G·10^(2d)<2` no feasible A1 reconciliation exists. At the unique sharp value

`d* = 1/2·log10(2/G)`,

the same corner attains the A1 identity exactly. Thus, with **no convex approximation or optimizer assumption**,

**SHARP `d*=0.01212052289405356...` dex.**

This is the minimal possible `max(|b'-b|,|r2'-r2|,|r0'-r0|)` compatible with A1, conditional solely on the three deterministic fitted roots as input. At that corner one common `s≈0.446290926969` works exactly.

REC11 **rigorously certified the numerical bracket** `0.0121205228 < d* < 0.0121205230` by stdlib `Fraction` only. The proof encloses ln10 by convergent positive rational atanh series for `ln10=3ln2+ln(5/4)` and each exponential by its rational 100th Taylor polynomial with symmetric Lagrange remainder; rational interval products prove `G·10^(2d)<2` at the lower endpoint and `>2` at the upper endpoint. No floating-point optimization or unbounded numerical rounding is used for this bracket.

If **baseline b is kept exactly fixed** while r2 and r0 each may shift by at most d, the minimal d instead is `log10(2/G)=0.0242410457881...` dex. This is a separate source contract (not a claimed physical fact).

## New theorem 2 — sharp minimum finite-point affine response error

Consider the three-point vector `f=(f0,1,f2)` at k=0,1,2. Every affine function `g(k)=a+bk` has zero second difference, so for residuals `e_j=f(j)-g(j)`,

`W=e0−2e1+e2`.

By the triangle inequality, `|W|≤4 max_j|e_j|`. The bound is **sharp** by choosing the residual pattern `(W/4,-W/4,W/4)`; then the subtracted g has vanishing second difference and hence is affine. Therefore

`inf_{g affine} max_{j=0,1,2}|f(j)−g(j)|=|W|/4 = 0.027143940723966975...`.

For A1's **physically typed known baseline** `g(1)=f(1)=1`, the middle residual is 0, so `|W|≤2 max(|e0|,|e2|)`, and it is sharp by choosing endpoint residuals `e0=e2=W/2`. Thus

`inf_{g affine, g(1)=1} max(|f0−g(0)|,|f2−g(2)|)=|W|/2 = 0.05428788144793395...`.

These are FINITE-POINT least-favorable approximation identities, not claims about derivative curvature between samples, or physical error for unsampled k.

## Additional root-fit-SE budget control

Take the owner reported nominal SE of each of b,r2,r0 and place an **explicitly hypothetical independent coordinate box** of ±1 FIT SE around each source root. The maximum possible G in that box is

`G_1SE_max = 10^((b+eB)-(r2−e2)) + 10^((b+eB)-(r0−e0))`
`=1.934090797610986...<2`.

For EVERY three-root perturbation within this purely deterministic fit-SE box, the anchored affine response minimax error remains at least

`(2−G_1SE_max)/2 = 0.032954601194506994...`.

This is a **robust conditional math bound** and directly sharp as a uniform lower bound under that box's worst case. FIT SEs are not validated joint uncertainty sets, confidence intervals, physical systematics, or guarantees of Julia ODE/discretization accuracy. No "sigma" significance or real physical exclusion follows.

## Compatibility and nontransfer

- `PASS` source CSV 21-fit re-derivation and exact rational d* bracket.
- `PASS` exact sharp three-root root-space minimal correction.
- `PASS` exact finite-point anchored/unanchored best-affine residual.
- `PASS_WITH_GUARD` robust nominal one-FIT-SE hypothetical box lower bound.
- `FAIL` SINGLE-S A1 for BOTH directions on the fitted source-v2-model roots, coherently with Badacz REVIEW054 and AUD1 ROT035.
- `HOLD` original Julia ODE continuous β-root error, physically valid fragmentation spectra E4, true uncertainty covariance/certification, historic JCAP Fig5, v3 execution, helium calibration, source physical PBH limits, BW owner receipt.

This audit does **not** refute INT9 ROT008's explicitly **conditional** one-direction forward sum box at k=2 or REC11 ROT011's conditional inverse-rank mathematics. It sharpens WHY neither can simply be promoted to source-native global A1 for k=0. There is no new theorem novelty claim: the algebra follows classical 3-point affine Chebyshev approximation and monotonic exponentials.

## Reproducible artifact

The independently executed standalone stdlib script `verify_rec11_rot012_A1_sharp_root_and_curvature.py` retains the literal 21 public input fit rows and generates a stable `results_rec11_rot012.json`. Source fit, rigorous rational bracket, affine minimax residual witnesses, and independent one-SE box monotonicity all PASS.

Local complete ZIP `IW_REC11_ROT012_A1_SHARP_ROOT_REPAIR_REPRO_001_20261111.zip`: SHA256 `772daa4381889e65bb38fc6e7a693d807098b3520b106361c0be70e8f173d261`. ZIP CRC PASS, 4/4 SHA-manifest members PASS, isolated clean re-execution produces JSON and stdout byte-identical PASS. The ZIP is local conversation material; not falsely claimed as hosted in GitHub.

Source references:
- Badacz REVIEW054 original: https://github.com/wmakiela-tech/Nash-iw-research/blob/3f6769d60d095aa6de100726c719697a726a6dc9/research/badacz/2026-11-08/IW_BADACZ_WUXU_JOINT_LATE_BAND_ADDITIVITY_REVIEW_054_20261108.md
- Original Badacz CSV: https://github.com/wmakiela-tech/Nash-iw-research/blob/3f6769d60d095aa6de100726c719697a726a6dc9/research/badacz/2026-11-08/data/kernel_cd052.csv
- AUD1 ROT035 source-aware original referee, private: https://github.com/wmakiela-tech/Nash-Priv/blob/52d26653387c2efc6b203aa071786019d0da78ee/audits/aud1/2026-11-10/IW_AUD1_ROT035_WUXU_BADACZ_REVIEW054_A1_TWO_DIRECTION_RECIPROCITY_AND_INT9_FORWARD_BOX_FALSIFIER_001.md
- INT9 ROT008 owner conditional A1 forward: https://github.com/wmakiela-tech/Nash-iw-research/blob/988ceacd4e1f2652af7654302935796c3736fff5/research/int9/2026-11-10/iw_int9_rot008_CD_forward_box_robustness_vs_source_inverse_rank1_gate_001.md

RETURN_ID: `IW_REC11_ROT012_WUXU_CD_A1_SHARP_SOURCE_ROOT_DISTANCE_AND_DISCRETE_CURVATURE_001_20261111`.
