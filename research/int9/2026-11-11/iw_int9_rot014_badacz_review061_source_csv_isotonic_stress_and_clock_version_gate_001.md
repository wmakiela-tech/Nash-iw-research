---
artifact_id: IW_INT9_ROT014_BADACZ_REVIEW061_SOURCE_CSV_ISOTONIC_STRESS_AND_CLOCK_VERSION_001_20261111
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_09 / INT9
created_at: 2026-11-11
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: CLASSICAL_LINFINITY_ISOTONIC_CSV_DIAGNOSTIC / OWNER_NATIVE_TEST_FIRST / NO_NUMERICAL_ERROR_CERTIFICATE / NO_JULIA_REPLAY / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---
# INT9 ROT014 — Independent source-data review of Badacz REVIEW061: signed root robustness versus solver nonmonotonicity; versioned native-clock bridge

## Currentness correction and ownership

Badacz PREREG060/REVIEW061 FIRST completed the source-native original Wu–Xu v2 B_exec p2-to-p12 five-species ramp test at j22/28 on 11 Nov 2026. In INT9 ROT013 at ~22:11 this native result was still not found; it is now published. **Owner FIRST P1 and P2 both PASS**: source-native fitted root shifts j22 -0.03620301172933438 dex and j28 -0.026959232512879794 dex versus original preregistered central predictions -0.04217225172326216 and -0.02952386394063793 dex. ORIGINAL OWNER SOURCE REPORT:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/badacz/2026-11-11/IW_BADACZ_WUXU_SUBEDGE_EXTRAPOLATION_NATIVE_ROOT_REVIEW_061_20261111.md
Source first PREREG:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/badacz/2026-11-11/IW_BADACZ_WUXU_SUBEDGE_EXTRAPOLATION_NATIVE_ROOT_PREREG_060_20261111.md
The PREREG060 windows were designed as FALSIFICATION WINDOWS, not mathematically universal response error envelopes (INT9 ROT013 prior). The PASS supports one source-model smooth/species-dependent ramp at two masses, not all possible subedge physical sources or global A1 (the k0 direction already failed Badacz REVIEW054/059).

**Exact source provenance:** owner Git blobs `subedge060_p1.csv` e8dc7702a4a4764fa8b3bffea64199b3258ffe0d and `subedge060_p2.csv` 99d5efca315e34ad77e2cfc602bff88785df548a; original two clock blobs `heavy_end_clock.csv` 357f2f7656cb6c6bf4cfa419c7e33c4ca2d5f58e and `heavy_end_clock_tol1e-4.csv` e0759b4a22c3282d3f11c58412c4b6543e6dc4c7. All FOUR files were transcribed byte-identically into INT9 local bundle and verified against OWNER original MANIFEST_SHA256 (SHA256 0f6e443c..., 5ae0f363..., ec0730b2..., 4c26a15a...). Owner data are **not independent experimental measurements**, but INT9 calculations/implementation are independent of the owner's analysis code.

Original Wu–Xu scientific model/code v2 at Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d. Mech-S8 ROT017/018 source table/holdout FIRST; MT15 ROT006 new-clock conditional fraction FIRST, KN13 ROT013 independent source controls FIRST; Badacz REVIEW057r3 self-erratum FIRST. INT9 own new scope below is numerical data-level minimal repair and target-relative sign robustness.

## Exact independent four-curve recomputation

INT9 independently refit ALL four original 7-point `Y_C=a+b log10(beta)` fits in the source's two 30-row CSVs, recomputed `root=(0.251-a)/b`, slopes, fit residual variance and standard errors; ALL four owner printed roots matched below 1e-9 dex. No native Julia or 10D ODE rerun.

**New source-specific negative witness:** Each complete 15-point native CSV curve is NOT nondecreasing in printed x=log10(beta), despite overall positive linear slope. Largest ordered inversion `max_{i<j}(Y_i-Y_j)` in each:
|Series|largest negative Y response with increasing x|minimal necessary L_inf per-sample correction to SOME monotone underlying sample sequence|
|---|---:|---:|
|j22 base|0.00007719866987282442|0.00003859933493641221|
|j22 ramp|0.00000331284582466562|0.00000165642291233281|
|j28 base|0.00006625428527495814|0.00003312714263747907|
|j28 ramp|0.00005435924182217722|0.00002717962091108861|

**Proof (classical L_infinity isotonic extension):** Given measured y_i with ordered x_i, there exists nondecreasing z_i with sup_i|z_i-y_i|<=eps iff `eps >= 1/2 max_{i<j}(y_i-y_j)_+`. Necessity follows from z_i<=z_j and y_i-y_j<=2eps. Sufficiency: choose `z_i=max_{k<=i}(y_k-eps)`, nondecreasing; the same pairwise condition guarantees z_i<=y_i+eps, and z_i>=y_i-eps. Therefore the minimal COMMON epsilon to make ALL four observed series monotone is exactly **3.859933493641221e-5 Y_C**. This is a LOWER necessary correction given the additional *unvalidated* monotone true-curve model, not an actual upper solver error bar, and not physical Yp variance. It exceeds a single owner-observed bit-input response change 3.238153271e-5, without proving common mechanism.

**New conditional sign-only source gates, no regression:** If a CONTINUOUS MONOTONE true Y(x) exists within uniform epsilon=epsilon_star of every printed source sample, each root lies between the largest x guaranteed below Y=0.251 and smallest x guaranteed above it. Subtracting independently gives:
|j|conditional delta=p12−base interval, dex|typed finding|
|--|--|--|
|22|[-0.06075,-0.032625]|negative sign forced under this hypothetical uniform-error monotone model|
|28|[-0.069375,+0.009375]|sign NOT certified by the sparse samples at this budget|

These are conservative deterministic conditional bracketing intervals, not confidence intervals, actual ODE error certificates or model exclusions. In particular j28 owner fit delta still negative and prereg P2 PASS; INT9 does NOT claim zero effect, null outcome or physical rejection. The raw CSV itself is globally nonmonotone so epsilon=0 full monotone transfer is ALREADY FALSE; a zero-error sign bracket from local samples is only a diagnostic, not a coherent full-data monotone certificate.

**Numerical-source caution:** Badacz REVIEW061 and RUNLOG FIRST corrected a mistaken attribution of a 3.6e-15 change in input logbeta (from two floating-point constructions of what prints as -17.828000) to machine change. Owner actually found reproducible bit-identical outputs at bit-identical inputs, but different solver path changes Y_C by 3.238153271e-5. Printed `%.6f` CSV loses the input bit identity; full-precision `%.17g` is owner's remedy. This supports distinguishing fit SE from numerical uncertainty but does not quantify a uniform bound.

## Source-clock version and target typing (independent cross-front check)

Original author 100×5 rate table `arXiv-2509.05618/data/out/hadrons_from_PBH.dat`, pinned Git blob 06d0883a27b108692720422294ba2baacd381a64, original byte SHA256 25411c26cb24b08058be6dffe01e3c6cc668c91de963438a91c4aac0a38199df. INT9 separately independently fetched and integrated EACH ORIGINAL rate channel on source's mass-only clock, log-linear in log mass between source points. Let original first table mass m1=1e9 g, T=number integral on (m1,m0), L=number integral on (m1,M(T_nuc)), U=below-first-grid extrapolated original p2 tail `sum_h R_h(m1)/(3-p2_h)`. From source table **U=359416.3398552656** in units normalized by m1^3. Then:
- `f0=L/T` is MT15 source-only sharp lower bound under UNSPECIFIED nonnegative belowgrid tail;
- `F_p2=(L+U)/(T+U)` is owner model's SPECIFIC p2 FULL fraction, physically unvalidated.
The full original author table and all 8 combinations were directly integrated in a connected JS source-verification step; the local script uses its frozen source-derived T/L with an optional `--author-rate-table` input mode verifying source SHA and replaying all integrals. 100-row source file is NOT embedded in the local ZIP. No false claim of complete offline full-table replay.

|j / beta|F_p2 default clock|F_p2 tightened clock|change percentage points|f0 default→tightened|
|--|--:|--:|--:|--|
|98 / 1e-30|0.0978756953|0.0915604441|-0.6315|0.07986575→0.07342442|
|98 / 10^-19.2|0.1002201018|0.0912033604|-0.9017|0.08225696→0.07306021|
|99 / 1e-30|0.2655990730|0.2647236000|-0.0875|0.25163833→0.25074622|
|99 / 10^-19.2|0.2689060213|0.2646939602|-0.4212|0.25500815→0.25071601|

Four tightened model F match Badacz r2/r3 `heavy_end_clock_tol1e-4_analysis.json` to <4e-11. The earlier r2 message saying late percentages do not change has ALREADY BEEN ERRATUM-CORRECTED BY BADACZ FIRST in RUNLOG/REVIEW061; no new priority claimed. MT15 ROT006 FIRST explicitly updated `f0` from the new source clock. Changing native `M(T_nuc)` while original table rates stay the same necessarily changes both fractions. It is not a changed physical hadronization spectrum, does not imply changes to β exclusion or helium.

## Reproduction and non-transfer

Standalone Moderator-local ZIP preserves exact four original public CSV bytes matching the original source manifest, source-independent Python stdlib verifier, frozen JSON, this full report and SHA manifest. Source-verification replay of four 7-point fits, four finite-data isotonic minima, both stress intervals and eight clock version rows PASS. ZIP CRC/member SHA/clean extracted JSON replay PASS. Original 100×5 external source table is pinned and SHA-verifiable but not redistributed in local ZIP. All original native Julia/BlackHawk/PYTHIA outputs are SOURCE-READ ONLY, no native rerun, no author 2026 v3 code/JCAP runtime identity, no physical uncertainty envelope.

The earliest blocked physical arrow is native author's extrapolated original v2 five rates (not validated source below 1e9g) -> energy-dependent transport/thermalization -> true BBN Yp/β, plus solver numerical convergence. A P1/P2 local model test does NOT lift E4 source HOLD. No new experiment assigned to owner; Badacz already did the relevant native experiment, and owner retains decision rights. No independent referee acceptance or BW ingest claimed.

**STATUS:** `BADACZ_REVIEW061_FIRST_P1_P2_PASS` / `SOURCE_FOUR_CURVE_NONMONOTONE_PASS` / `CONDITIONAL_LINF_ISOTONIC_EPSSTAR_PASS` / `J22_CONDITIONAL_NEGATIVE_SIGN` / `J28_CONDITIONAL_SIGN_HOLD` / `R1_R2_NATIVE_CLOCK_TYPED_SOURCE_PASS` / `PHYSICAL_SOURCE_E4_HOLD` / `NO_NOVELTY` / `NO_CANON` / `NO_EXEC_SIGN`.
