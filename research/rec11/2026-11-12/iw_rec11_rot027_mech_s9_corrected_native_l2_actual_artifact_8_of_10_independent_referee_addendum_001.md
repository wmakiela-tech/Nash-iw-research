---
artifact_id: IW_REC11_ROT027_MECHS9_ROT008_ACTUAL_INDEPENDENT_NATIVE_L2_SOURCE_ATTESTATION_001_20261112
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
date: 2026-11-12
kind: I1_NONBLIND_ACTUAL_BINARY_GITHUB_ACTIONS_NUMERICAL_SOURCE_REFEREE
source_firstness: MECH_S9_ROT008_OWNS_REPAIRED_L2_NATIVE_RUN / BADACZ_REVIEW053_OWNS_ORIGINAL_REFERENCE
source_run: 43310359194
source_artifact: 13986347698
status: EXECUTION_PASS / SIX_ROOTS_EXIST / 8_OF_10_PREDECLARED_COMPARISON_PASS / TWO_J22_V2_CRITERIA_FAIL
claim_ceiling: SOURCE_NUMERICAL_NONBLIND / NO_INDEPENDENT_ODE_SOLVER / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# REC11 ROT027 source addendum — real Mech-S9 independent L2 Julia run completed but 2/10 reference comparisons FAIL

## Original execution and priority

Mech-S9 FIRST fixed the source-relative include loader from failed ROT007 in ROT008, then executed the unchanged original Wu–Xu `magic()` through a separate GPT-authored observation and adaptive bisection driver, not the original Badacz driver. Badacz REVIEW053 FIRST produced owner reference roots. REC11 independently downloaded the completed original source archive and verified it, without creating or executing a new Julia ODE. This record updates the formerly correct `IN_PROGRESS` status on earlier REC11 and Mech-S9 reports; historical messages should not be silently rewritten.

Original [corrected Actions run 43310359194](https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43310359194) completed SUCCESS at **2026-11-12 21:41:56 UTC**, all steps PASS including source hash pin, Julia1.12.3, native adaptive L2, comparator and artifact upload. Run workflow head `9e2ee03c342a56b6f57efb2e69292a829a0be2d4`; original corrected GPT L2 driver `mech_s9_rot008_independent_native_L2_FIXED_INCLUDE.jl` Git blob `5ca59bd911bbd12e4bb2b3deca9fbd3fa4ed0506`. Original Wu–Xu author commit `d395183674cace6c9906a8911bdeb7234ba4040d`, original main-scan.jl unchanged.

**ACTUALLY DOWNLOADED** original GitHub artifact ID **13986347698** named `mech-s9-rot008-wuxu-native-independent-gpt-L2-FIXED`, ZIP size **22,179 bytes**, SHA256 **88913fd22b95efd37d26d69e036f9e05a99f7bb411faa5c996deeb1aebc0b461**, matching GitHub provider digest. Archive ZIP CRC PASS; all **15/15** internally recorded file SHA256 PASS; 16 members including manifest, native stdout/stderr, source points and six roots. Note two JSON files (`L2_REFERENCE_COMPARISON_STDOUT` and `independent_L2_vs_badacz_REFERENCE.json`) have the SAME parsed JSON but different key ordering — byte comparison is NOT asserted.

## Six actual roots, independent source-file arithmetic

The real `independent_L2_raw_calls.csv` contains **57 different** (j,log10beta) original-source PBH calls, 30 at j22 and 27 at j62, plus **two** SBBN calibration runs recorded in `NATIVE_L2_STDOUT`. All six rows of `independent_L2_roots.csv` have a strictly signed negative/positive final residual bracket; each root equals the bracket midpoint (half-width 0.0001953125 dex before eight-place CSV rounding). Independent read rechecks `Yc_author=2X_T0/(1-X_T0)` to within **2.23e-16** across all 57 points.

| j | criterion | New L2 root log10beta | Badacz quadratic original | signed difference L2−owner | tolerance | result |
|---|---|---:|---:|---:|---:|---|
| 22 | V0 | -17.2240234375 | -17.215113933232 | -0.008909504268 | 0.02 | PASS |
| 22 | V1 | -17.1373046875 | -17.140129424510 | +0.002824737010 | 0.02 | PASS |
| 22 | V2 | -16.9974609375 | -17.020870078768 | **+0.023409141268** | 0.02 | **FAIL** |
| 62 | V0 | -19.3919921875 | -19.389434029919 | -0.002558157581 | 0.01 | PASS |
| 62 | V1 | -19.3564453125 | -19.355223416240 | -0.001221896260 | 0.01 | PASS |
| 62 | V2 | -19.3044921875 | -19.302014840944 | -0.002477346556 | 0.01 | PASS |

Two additional comparisons per mass are target-specific ROOT DIFFERENCES (`V1−V0` and `V2−V0`) with tolerance **0.02 dex**, not independent roots. All three at j62 PASS (two shifts, three roots), and j22 shift `V1−V0` PASS, but j22 shift `V2−V0`:
- New L2: **0.226562500000 dex**.
- Badacz original quadratic: **0.194243854464 dex**.
- Difference: **+0.032318645536 dex**, greater than 0.02 → **FAIL**.

Therefore **8/10 PASS, 2/10 FAIL**, both `j22/V2` or its dependent shift. The two failed criteria are algebraically related, not two independent physical anomalies. The owner post-run comparison JSON itself flags `all_within_predeclared_windows=false`; the workflow is still green because the script's successful execution does not assert complete parity. This is the same execution/validation distinction AUD1 previously emphasized.

## Independent source checks and remaining falsification gates

REC11 independently used Python standard library `zipfile,hashlib,csv,json` (not owner numeric comparator implementation) to verify provider ZIP SHA, CRC, 15 file SHA entries, all 57 unique raw coordinates, two mass groups, all 6 bracket sign constraints, all 6 root-midpoint identities, all 10 reference comparisons and the precise two failed selectors. It also checked `Yc_author` from the printed X0 values, no source-native ODE rerun. Original provider artifact + actual executed independent source verifier + exact JSON + stdout + README preserved in separate 6-member LOCAL attestation ZIP, `IW_REC11_ROT027_MECHS9_NATIVE_L2_ACTUAL_8_OF_10_COMPARE_ATTESTATION_001_20261112.zip`, SHA256 `bd42ba80ef073061090ce806bf081923204ac8ef44ac415b01ee86fcb5d9d2ab`; CRC PASS, SHA5/5 PASS, clean extracted replay reproduces JSON and stdout byte-identically. Local ZIP is NOT claimed stored in GitHub.

**Scientific HOLD:** A bisection half-width is an *algorithmic* bracket width, not a physical uncertainty in root position. Mech-S9 ROT009 first computed a very small local j22 V2 source response slope `~0.004012/dex` such that a response perturbation `1e-4` may shift the root by `~0.0249 dex`. Current L2 j22 V2 source sign bracket is not by itself solver-stability validation or proof of uniqueness under native adaptive source noise. E4 hadron spectra, original manuscript-vs-executable physical model, JCAP published Fig5 production build and SBBN inter-mass calibration mismatch remain HOLD. Badacz original L1 source 53/53 exact-digit match remains PASS; no physical bound, no broader NASH novelty. This is an **external independent archive/source arithmetic referee**, not new model discovery.

**RETURN_ID:** IW_REC11_ROT027_MECHS9_ROT008_ACTUAL_INDEPENDENT_NATIVE_L2_SOURCE_ATTESTATION_001_20261112.

**FINAL:** `PASS_NATIVE_L2_EXECUTION / PASS_ACTUAL_ARCHIVE_PROVENANCE_15_OF_15 / PASS_SIX_SOURCE_SIGNED_BRACKETS / FAIL_COMPLETE_EKS1_ROOT_PARITY_2_OF_10 / HOLD_NATIVE_SOLVER_NUMERIC_UNCERTAINTY / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
