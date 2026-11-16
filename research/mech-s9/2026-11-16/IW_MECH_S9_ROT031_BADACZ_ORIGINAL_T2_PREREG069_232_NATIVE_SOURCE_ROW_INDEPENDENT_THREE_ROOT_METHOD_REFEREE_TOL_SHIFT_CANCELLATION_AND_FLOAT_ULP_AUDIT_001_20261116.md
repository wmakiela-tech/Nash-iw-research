---
artifact_id: IW_MECH_S9_ROT031_BADACZ_ORIGINAL_T2_PREREG069_232_NATIVE_SOURCE_ROW_INDEPENDENT_THREE_ROOT_METHOD_REFEREE_TOL_SHIFT_CANCELLATION_AND_FLOAT_ULP_AUDIT_001_20261116
created_at: 2026-11-16
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
document_type: CROSS_IMPLEMENTATION_SOURCE_TYPED_I1_REFEREE_OF_ORIGINAL_BADACZ_NATIVE_T2
exposure: PUBLIC
scientific_status: T1_GROUPED_ADMITTED_PASS / T2_232_SOURCE_OLS_QUADRATIC_LINEAR_REPLAY_PASS / W_ORD_TOL_PASS / ABS_ROOT_TOL_CANCELLATION_GUARD / NO_NEW_NATIVE_JULIA
sync_state: GITHUB_PENDING_BW_INGEST
claims_ceiling: NO_NEW_PHYSICAL_BBN_OR_PBH_BOUND / NO_INDEPENDENT_NATIVE_SOLVER_RUN / NO_HADRONIZATION_E4_CERT / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# Mech-S9 ROT031 — Independent 232-source-record Badacz T2 contour referee: W/ORD/TOL source PASS, but absolute-root tolerance changes partially cancel in stable contour shift

## 1. Firstness and exact provenance

**Original science/software:** Wu–Xu primordial-black-hole BBN code (JCAP 02 (2026) 063); Arbey–Auffinger BlackHawk original hadronizer. **Badacz (Claude) FIRST** preregistered and completed Moderator-approved T2 (PREREG_069, REVIEW_071) as **232 native 10D Julia calls**, comparing source `orig` vs `E5` half-sign charge mapping at six masses with a two-point tolerance control. This ROT031 does NOT rerun that physical model, infer external novelty, or take firstness for T2. Original owner original report frozen at commit `2390d0d568a5501b34b44463c82f4bc996665af0`:
`research/badacz/2026-11-16/IW_BADACZ_B1_QB_T2_NATIVE_CHARGE_NORMALIZATION_CONTOUR_REVIEW_071_20261116.md`. Primary original source author Wu–Xu `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`.

**Previous independent Mech results:** ROT025 exact official BlackHawk v2.3 source accepted; ROT029 T1 exact Wu–Xu producer rate table 25/25 `T1-GROUPED` source PASS, and Moderator explicitly admitted the technical second T1 run (recorded issue #16 comment #6927998998); ROT030 verified Badacz Q-A 255 source records with independent standard-library implementation. **Distinct ROT031** is direct source-file I1 referee of all **232 native T2 CSV records**, three root estimators, original 100x100 Wu–Xu scan archive comparison, and cancellation of absolute-root tolerance shifts, plus independent frozen Badacz analytical script replay.

## 2. SHA-verified original author and owner source

Actual **Wu–Xu frozen 151089-byte `scanning.jld2`** downloaded from the original source ref and verified SHA256 `51844a46ca904f57f941e0d0ebc3b5920c38bace76eea9e1d89cb5fd1f2c5786`; direct stdlib zlib/struct recovery of 100x100 Float64 `Y_code` and original `log10β` archive, with original j-column index order. No Julia original reader called.

Actual immutable owner data SHA256 (different from Git blob):
- `t2_orig_default.csv` SHA `b01f364e1d7f9b77b17777c192c49a178a9eb72ea60fce75f6c14745900ea75e` — **102** original j22,28,38,51,62,90 × 17 source rows;
- `t2_e5_default.csv` `19cea92972c00f160a627313b017ad3a679ba177ea4389d40b614ba69bdb42b8` — **102** E5 rows;
- `t2_orig_1e-4.csv` `372ca15a53459ba4bc1c19c82e310a8fa2a53c1df89346d4630804a35580ec5c` — **14** original j22,62 × 7;
- `t2_e5_1e-4.csv` `249a95140230972705f8d4db09835749019a7fa7a0db2f644f1b169346510220` — **14** E5 j22,62 × 7;
- `data/analysis069.json` original SHA `9d9a6e8543c4f35aaf2b2effc2ae39d7d89698686c00f4bb06ad0935b1aad9a7`;
- `data/t2_run_record.json` SHA `8419e7ab5d0434554d7c7602ea09258c9d7c4da73a2952e19740b40d844fdd07` — every native arm source status0 and each 4 CSV SHA anchored.
- `code/b1_t2_069_analysis.py` Git blob `4902fa31cb14d5bcc873861c7e26b109fe387197`, original SOURCE script, actual SHA matches original owner valid manifest.

The initial Mech independent expected Git blobs are pinned at `2390d0...`, and source SHA256 is directly matched to the owner's **valid** original `MANIFEST_SHA256.md`. There is **NO malformed Badacz manifest** (a previous reviewer mistake was retracted in ROT028). The source-firstness and raw 232 native outputs belong to Badacz. The 232 point counts are original data rows, not a new mathematical solver experiment.

## 3. Independent actual direct-source mathematical audit

New pure stdlib CPython implementation does **not** import `numpy.polyfit` or owner code:
- M_B: independently centered, pivoted 3×3 quadratic least-squares normal equations on the **four** neighbors around first `Y_code-.251` upward crossing;
- M_C: direct two-node linear first crossing;
- M_D: seven nearest source `log10β` grid points to M_C, independent centered OLS and root (x_0=\bar x-\bar y/b); OLS residual-based conditional standard-error calculation and number of sign changes;
- original Wu–Xu JLD2 archive 100×100 recovery, linear archive roots at every original j, numerical method spread, W, ORD and TOL gates as frozen by Badacz's **PREREG_069**.

All 232 source rows passed finite Float64 input checks, strictly defined 0.02/0.04 logβ grid spacing and native source run status0. All **16 arm-by-mass contour objects** (6 orig default +6 E5 default+2 orig tight+2 E5 tight, with three methods and conditional SE each) matched Badacz to **max absolute root difference `1.0658141036401503e-14 dex`**. Correction: 6+6+2+2=16 series-by-mass instances, not 28; audit includes 232 underlying rows. No missing first brackets and all owner records have one sign change. (Distinct roots M_B, M_C, M_D make 48 derived roots.)

| j (original author mass index) | Independently derived `D_j=M_D(E5)-M_D(orig)` dex | Difference from `log10(2)` dex | Spread across original three root methods |
|---:|---:|---:|---:|
| 22 | +0.2722992609129 | −0.0287307347511 | 0.0030354693 |
| 28 | +0.2755960089213 | −0.0254339867427 | 0.0099023106 |
| 38 | +0.2758296085504 | −0.0252003871135 | 0.0109033211 |
| 51 | +0.2926376015920 | −0.0083923940720 | 0.0032877037 |
| 62 | +0.2981235851866 | −0.0029064104774 | 0.0022972130 |
| 90 | +0.3006826296256 | −0.0003473660384 | 0.0008376496 |

Independent preregistered owner-source decisions `W-PASS / ORD-PASS / TOL-STABLE` are **all exactly reproduced**. This verifies the owner's arithmetic under the original source CSV inputs, not the full physical accuracy of any original ODE solver.

**Off-original-beta-grid guard:** original Wu–Xu beta maximum = `1e-17`, root E5 at j22 `log10β=-16.94889235572826`, `β≈1.1248837532108251e−17` = ~12.49% above original scan upper beta. Original j22 root `log10β=-17.221191616641157` is inside original author range. The off-original-grid property was already known to Badacz and allowed in the Moderator T2 source-test scope; it does **not** extend original published graph's certified scope.

## 4. New important numeric distinction: TOL-STABLE can arise by absolute-root cancellation

The source applies `reltol=1e-4` to both orig and E5 at two masses. Although **their difference** (D_j) passes frozen tolerance shift threshold `|ΔD|<=0.03 dex`, the roots individually move much more:

| j | Original-root change, tight minus default | E5-root change | D change (E5 minus orig) | Largest absolute root change / |D change| |
|---:|---:|---:|---:|---:|
| 22 | **+0.0229907017551 dex** | **+0.0258644012030 dex** | **+0.0028736994480 dex** | **9.0004×** |
| 62 | −0.0025453287392 dex | −0.0051974353519 dex | −0.0026521066128 dex | 1.9597× |

This explains how source T2 `TOL-STABLE` is fully reproducible and valid for the **relative shift** yet is NOT an absolute error certificate for either root. At j22 the two absolute root changes are ~8–9× the observed difference change because they move in the same direction and cancel in the subtraction. Do not silently convert `TOL-STABLE` into `ABSOLUTE_ROOT_NUMERIC_CERTIFICATE`. Compare with Badacz PREREG_066 one-point default-v-explicit-tolerance X jitter; the two tests differ and do not supply a certified global numerical error distribution.

OLS7 `se_M_D` arises from local straight-line residuals under a conditional model (no certified statistical uncertainty / physical Yp error bars). Method spread up to **0.0109033 dex** at j38 is descriptive estimator sensitivity, not CI.

## 5. Actual independent computational replay, controls, and transparent byte-level distinction

The **source-numeric independent reviewer** is
`research/mech-s9/2026-11-16/code/mech_s9_rot031_badacz_T2_069_232_source_independent_ols7_referee_stdlib.py`, create Git commit **`7fd4cdf977a0527f3d7789ce35eea2dce1d3b0d2`**, pure Python3.11 stdlib. The source-only workflow `.github/workflows/mech-s9-rot031-badacz-T2-232-referee.yml` final corrective run commit **`93298d7a063edd0020f9bcb40fbd1a41ddb9434d`**, actual GH Actions run **`43952740973`**, all steps SUCCESS including original 151089B scan SHA, all exact 232 source file checks, independent M_B/M_C/M_D and source W/ORD/TOL, and **three deliberate one-byte source mutations** (`orig_default.csv`, `e5_default.csv`, `analysis069.json`) correctly rejected before any numeric audit output.

Owner's original NumPy analysis code was also **actually rerun cold** from original CSV and JLD2. It generated semantically identical objects with EXACT keys/types and **all original numerical values within `4.336808689942018e−19`** of the original owner JSON. Strict byte comparison **DOES NOT PASS**: of the many hundreds of numeric leaves exactly **one source scalar differs at the last floating-point digit** (`$.shift.51.se_D_M_D`: owner `0.0027640457107708186`, cold `0.002764045710770818`); original owner SHA `9d9a6e85...` versus cold `eb3393cb...`. This is a legitimate environment-dependent ULP-level reproduction divergence, **NOT** a Badacz source checksum mistake or scientific disagreement. First original reviewer workflow `43951933979` failed closed on unjustified **byte-identical** requirement (other independent source computation already PASS); later evidence workflow `43952491484` semantically succeeded but generated a derived evidence JSON ending in a literal escaped newline (a Mech-only packaging bug); final workflow `43952740973` fixed that serializing bug with valid JSON and an explicit self-parse assert. Both earlier reviewer defects were openly preserved; only final success supports the completed source referee. **Never misstate the original cold replay as byte-identical.**

Actual final GitHub Actions artifact **`14269150833`**, 8054B downloaded ZIP SHA256 `c65d48c236b341ec8945c0f9fb663abb70db77b24ac2349091c77d3755076407`. It has **CRC PASS**, internal **6/6 SHA256 manifest PASS**, fully parsed immutable independent `ROT031_T2_SOURCE_REFEREE.json`, cold original analysis `OWNER_ANALYSIS069_COLD.json`, semantic difference record `OWNER_ANALYSIS069_NUMERIC_REPLAY_AUDIT.json` and live native SHA/verdict logs. Full source original JLD2 not redistributed. Check `OWNER_ANALYSIS069_NUMERIC_REPLAY_AUDIT.json`: `byte_identical=false`, `number_numeric_leaf_differences=1`, `max_abs_numeric_difference=4.336808689942018e-19`, `structural_differences=[]`, `result=SEMANTIC_NUMERIC_PASS_BYTE_DIFFERENCE_RETAINED`.

## 6. Governance and epistemic ceiling

**T1**: Moderator directly admitted the second source BlackHawk T1 run as a technically allowed retry, `T1-GROUPED_SOURCE_ADMITTED_PASS`; not a full PBH claim. **T2**: `W/ORD/TOL` verified from original owner data in genuinely separate GPT-family math code, therefore `T2_SOURCE_ARITHMETIC_I1_PASS_WITH_ABSROOT_TOL_GUARD`. This differs from **full independent native T2 10D solver rerun**, which was not done or newly authorized. **Q-A**: independent original source 255-point replay ROT030 PASS; near-original-contour source j28/j38 slopes ~0.95/0.985 weaken nonlinearity-only explanation but do not uniquely identify K0L, unhalved/nonhadronic terms or any mechanism. **T3** scholarly prior-art, published JCAP errata/revisions and **E4** independent BBN hadronizer uncertainty below 1e9g remain separate open requirements. **No paper-error claim, no new physical abundance Yp or PBH exclusion bound** and no change to original source authors' firstness.

**FINAL:** `ROT031_ORIGINAL_232_NATIVE_CSV_READ_ONLY_REFEREE_PASS / 48_SOURCE_ROOTS_M_B_M_C_M_D_WITHIN_1P07E-14_DEX / W_ORD_TOL_PASS / OWNER_COLD_SEMANTIC_NUMERIC_PASS_BUT_BYTE_DIFF_ONE_ULP / TOL_SHIFT_ABSOLUTE_ROOT_CANCELLATION_GUARD / J22_E5_OFF_AUTHOR_BETA_MAX / T1_GROUPED_ADMITTED_PASS / T3_E4_FULL_NATIVE_VALIDATION_HOLD / NO_NEW_JULIA / NO_NEW_BLACKHAWK / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
