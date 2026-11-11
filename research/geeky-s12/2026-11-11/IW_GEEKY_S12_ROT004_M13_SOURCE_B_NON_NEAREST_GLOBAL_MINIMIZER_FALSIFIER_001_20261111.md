---
artifact_id: IW_GEEKY_S12_ROT004_M13_SOURCE_B_NON_NEAREST_GLOBAL_MINIMIZER_FALSIFIER_001_20261111
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
created_at: 2026-11-11
exposure: PUBLIC
result_class: SOURCE_TYPED_EXACT_RATIONAL_INTERVAL_COUNTEREXAMPLE_AND_ANTI_REDISCOVERY
science_status: DIRECT_FROZEN_COEFFICIENT_MATHEMATICAL_FALSIFIER_PASS / INDEPENDENT_REFEREE_PENDING / OWNER_ADOPTION_PENDING
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: N41_FUNCTIONALLY_MATCHED_AUXILIARY_SOURCE_AND_M13_DIRECTED_INTERVAL_INPUT_ONLY / NO_HISTORIC_RUNTIME_IDENTITY / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT004 — strict source-coefficient falsifier of universal nearest-delta minimization, channel B

## 0. Decisive scientific return

**Question left OPEN by M13 ROT40:** For N41, five nested masks k=2..6, exact source-matched stencil2 and Fourier-TT generator, and a single unknown positive energy gain, does channel-B profiled distance D_B(alpha,beta) always attain its GLOBAL minimum over separation |beta-alpha|>=delta at one of the two *nearest* admissible points beta=alpha±delta, for ALL alpha and delta?

**ANSWER: NO, for M13's frozen source-coefficient model.** Choose exact rational parameters:

    alpha=39/1000=0.039; delta=7/200=0.035;
    nearest admissible beta_L=alpha-delta=1/250=0.004;
    nearest admissible beta_R=alpha+delta=37/500=0.074.

The strictly INTERIOR admissible witness beta_*=1/1000=0.001 satisfies |beta_*-alpha|=0.038>delta and BOTH source-certified STRICT inequalities:

    D_B²(.039,.001) < D_B²(.039,.004);
    D_B²(.039,.001) < D_B²(.039,.074).

Thus NEITHER closest admissible beta is a GLOBAL minimizer. This does NOT assert that beta_* itself is the global argmin. It is a negative result for the universal ALL-DELTA conjecture on B only. It does NOT refute M13's narrower B numerical observation for delta=.01 (which remains OPEN) or M13's certified A/C universal-all-delta radial results.

## 1. Priority, source and mature mathematics

**M13 firstness:** ROT32/33 established source-parameter geometry, ROT34 monotone/folding channel classes, ROT35 disjoint shell covariance, ROT36 numerical global separation, ROT37–39 certified selected delta endpoints, ROT40 proved universal A/C radial nearest-delta theorems by 2D Bernstein certificates. Crucially M13 ROT40 FIRST exhibited an actual B radial monotonicity counterexample (alpha=.05,beta=0), but explicitly did NOT upgrade it to a failure of global nearest-delta minimization. Its B delta=.01 dense scan found no counterexample and is NOT overturned.

Owner report:
https://github.com/wmakiela-tech/Nash-iw-research/blob/27188018c1dbbcee81d391ceb8ba5c55237cff7e/research/m13/2026-10-26/IW_M13_ROT40_universal_AC_radial_mask_global_argmin_001.md
Owner dispatch:
https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1793021293483809
M14 source successor:
https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1793027627068589

**Immutable input:** the original M13 outward-rounded interval coefficient table direct_B.json, Git blob SHA-1 a6f50fbe5904e580e84c87ee87c5ad043cdec5d0, publicly accessible:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json

These 25 interval coefficients are for the functionally matched auxiliary N41 centered stencil-2 Fourier-TT model with C1=(.05sin x,.05cos y,0), C2=(.04cos z,0,.04sin x), ambient pure-trace h=.1sin x cos y I, and E_alpha=I+alpha grid_h² Delta_2. The exact historical producer dtc0a_runtime_v0_3_1.py (published historical SHA256 2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084) has NOT been recovered byte-identically. ROT004 does not run or claim such a historic source. M13's initial interval coefficient generation is inherited, NOT regenerated independently by ROT004. The NEW strict inequalities are independently verified from those source intervals.

**Mature mathematical host:** projective least-squares fitting with common positive gain, Gram/wedge determinant identity and exact rational interval arithmetic. No mathematical novelty is asserted.

## 2. Precisely typed shell profile and positive nuisance fit

At N=41 the five nested interior cubes and shell sizes are:

    mask k:      2      3      4      5      6
    cube n:   50653  42875  35937  29791  24389
    shell w:   7778   6938   6146   5402  24389.

For each mask k, original directed interval coefficients define g_k(alpha)=RMS_mask(K_B(alpha))², a polynomial of degree <=4. The disjoint shell average energy polynomials are:

    s_i(alpha)=[n_i*g_i(alpha)-n_(i+1)*g_(i+1)(alpha)]/w_i, i=2..5;
    s_6(alpha)=g_6(alpha).

Let a_i=s_i(alpha), b_i=s_i(beta), W=diag(w_i). At all four tested beta values (0, .001, .004, .074) every shell-energy interval has strictly positive lower endpoint; therefore the common energy nuisance gain t minimizing ||a-t b||_W² over t>0 lies strictly inside the positive domain.

Write p=sum_i w_i a_i b_i>0, q=sum_i w_i b_i²>0. The algebraically exact profiled squared distance is

    D_B²(alpha,beta)
    =sum_i w_i a_i² - p²/q
    =[sum_(i<j) w_i*w_j*(a_i*b_j-a_j*b_i)²]
      /[sum_i w_i*b_i²].

The latter WEDGE identity avoids cancellation and is used for proof. W corresponds to M13's specific synthetic i.i.d. voxel ENERGY covariance host, not to an actual measured instrument covariance. A different mask/gain/noise model is OUTSIDE this theorem.

## 3. Rational interval proof and numbers

Read every original M13 lower/upper finite decimal endpoint as an EXACT rational (arbitrary-length BigInt numerator and denominator), without double rounding. Propagate using exact rational intervals through:
(1) all 25 quartic coefficients;
(2) all 25 shell polynomial coefficients and positive weights;
(3) Horner evaluations at alpha=39/1000 and the four exact rational betas;
(4) wedge differences, sign-safe interval squaring, finite sums and strictly positive denominator division.

The exact integer cross-products certify all FOUR tests:

    upper D²(.039,.001) < lower D²(.039,.004) : PASS
    upper D²(.039,.001) < lower D²(.039,.074) : PASS
    upper D²(.039,0)    < lower D²(.039,.004) : PASS
    upper D²(.039,0)    < lower D²(.039,.074) : PASS

Readable approximate values in original squared-energy units multiplied by 10^24 (NOT used for proofs):

| beta | role | 10^24 D_B² |
|---:|---|---:|
| 0 | supplemental domain-end witness | 0.801179843405898 |
| 0.001 | **strictly interior, farther, decisive witness** | **0.817576334733301** |
| 0.004 | left nearest admissible endpoint | 0.847761514126208 |
| 0.074 | right nearest admissible endpoint | 0.879415119792045 |

The certified strictly POSITIVE lower margins of nearest-boundary lower minus farther-interior upper, also multiplied by 10^24, are approximately:
- left: +0.0301851793929069;
- right: +0.0618387850587440.

No floating point is used in positivity comparisons; exact BigInt rational cross-multiplication decides the signs. The positive gaps exceed original coefficient interval widths by an enormous margin.

The proof is elementary: beta_*=.001 is legal and farther because |.039-.001|=.038>.035. If either beta=.004 or .074 globally minimized D² over legal betas, its value would be <= D²(.039,.001). Both strict opposite inequalities are established, so neither nearest beta can globally minimize. This does NOT identify the unknown global minimizer.

## 4. Reproducer and executed scope

Public self-contained stdlib Node.js verification program (remote immutable source Git blob SHA fetch with byte-level identity check, or pass the same direct_B.json file locally):
https://github.com/wmakiela-tech/Nash-iw-research/blob/5a4655324943e1cef8ea5b8d56c8bbcc0b4fdfed/research/geeky-s12/2026-11-11/iw_geeky_s12_rot004_m13_B_source_interval_counterexample.js

Invocation:

    node iw_geeky_s12_rot004_m13_B_source_interval_counterexample.js

The source table is not silently changed: exact Git blob SHA a6f50fbe5904e580e84c87ee87c5ad043cdec5d0 must match. An offline execution passes the original file as an argument. The report's exact rational interval algorithm was ACTUALLY executed directly against connected GitHub source content in the author's V8 execution tool; all strict inequalities were PASS. A separately implemented floating shell/wedge scan found the initial candidate and independently checked numerical scales, but that scan is NOT the proof. The published JS file has pinned GitHub create+full readback PASS; a second independent execution of the published bytes is not claimed.

## 5. Exact claims changed and preserved

**FALSIFIED:** universal ALL-(alpha,delta) source-model B nearest-delta GLOBAL argmin assertion.

**NOT FALSIFIED / STILL OPEN:** the specific B delta=.01 global boundary hypothesis and M13's 401x4001-point observation for that delta.

**RETAINED PASS:** M13 source-certified A/C universal radial proofs; its B radial counterexample firstness; M13 and MT13 attribution of the nuisance projective geometry; conventional exact Gram algebra.

**HOLD:** absent historical producer byte identity, other N, other masks, different covariance or independent gains per mask, physical NASH J3/K/GR/GW/TPE, independent referee, owner adoption.

**Research lesson:** when radial monotonicity fails, proving nearest endpoints from two-endpoint comparison or dense numerical grid is not valid; an explicit interior beta may dominate both nearest candidates. For any claimed positive B minimax theorem now restrict (alpha domain, delta, mask/noise/gain class) and demand a real global certificate rather than assuming universal reduction. Do not extrapolate this witness to delta=.01.

**REOPEN_IF:** M14 source owner or REC11 referee challenges coefficient lineage, exact interval arithmetic, or the declared W profile; alternatively a source-authorized narrower delta=.01 theorem is sought. No unnecessary new general mathematical campaigns.

## 6. Custody

PUBLIC scientific primary is this report; source verifier has its own pinned file and exact readback. Original B intervals stay in M13's published source, not duplicated under a new firstness identity. No confidential source data released. GitHub storage != Slack delivery != ACK != KN13 BW ingest != independent mathematical referee != owner adoption != canonical or EXEC status. If routed, Slack link will be reported separately. BW is GITHUB_PENDING_BW_INGEST, not a fabricated source event. NO_NEW_TASK_CASCADE.

**FINAL:** B_ALL_DELTA_UNIVERSAL_NEAREST_BOUNDARY_FAIL / EXACT_FARTHER_INTERIOR_WITNESS_PASS / M13_A_C_PASS_RETAINED / B_DELTA0P01_OPEN / M13_FROZEN_INTERVALS_NOT_HISTORIC_RUNTIME / SOURCE_OWNER_ADOPTION_PENDING / REFEREE_PENDING / BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
