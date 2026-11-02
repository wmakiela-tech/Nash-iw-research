# XH-S5 ROT018: original verified UTe2 tetracritical phase-boundary data, exact crosschecks and extrapolation limits

artifact_id: IW_XH_S5_ROT018_UTE2_PRIMARY_DATA_PHASE_BOUNDARY_20261102
return_id: XH-S5-ROT018-UTE2-TETRACRITICAL-PRIMARY-DATA-CROSS-FIGURE-EXTRAPOLATION-GATE_20261102
date: 2026-11-02
cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
exposure: PUBLIC
claim_ceiling: VERIFIED_BYTE_IDENTICAL_AUTHOR_CSV / EXACT_RATIONAL_AND_INDEPENDENT_SCIPY_NUMPY_REPLAY / NO_RAW_ULTRASOUND_TRACE_ANALYSIS / NO_NOVELTY / NO_NASH_PHYSICAL / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST

## Original source and priority
Kamat, Dans, Saha, Kokovin, Paglione, Schmalian, Ramshaw, "Thermodynamic demonstration of tetracriticality and multicomponent superconductivity in UTe2", Nature Physics, PUBLISHED 30 Oct 2026, DOI https://doi.org/10.1038/s41567-026-03504-z . SOURCE experiment reports the ultrasound-derived extra phase boundary which resolves the thermodynamically forbidden apparent triple point and supports two-component superconductivity. We did NOT replay their raw acoustic c11/c33/c55 traces, the jump in velocity or full thermodynamics; no independent order-parameter identification. The author paper owns all physical discovery priority; mature phenomenology Sigrist-Ueda RMP63:239 (1991), DOI10.1103/RevModPhys.63.239. Regression/LOOCV classical. No scientific novelty claimed.

## Strong positive provenance: real original-author data
Six authentic UTF-8 CSV files copied byte-identically from authors' GitHub repository source commit 908bb84e64c20411b14013c0bca43554731f7774 dated 2026-09-09:
https://github.com/CHiLL-Ramshaw/manuscripts-supporting_data/tree/908bb84e64c20411b14013c0bca43554731f7774/2026_UTe2_Tetracriticality .
Exact Git blob SHA1 (SHA1 of Git blob header plus source bytes, checked against repository):
fig2_Tc1.csv : 62cdfe70a50ec6500eb13208f78f7564319af924
fig2_Tc2.csv : 600525e0e0ff9246c1aac7e43b5ac5851db39835
fig2_Tc2_star.csv : ea1bd418fdb4e3bd90f8e07369a30b682d8b59bb
fig3_Tc1_infield.csv : 9ec50e45f68299a6d89bd6ac7ede125137a87e86
fig3_Tc2_infield.csv : 24ceb39ca588c9f5a0ab5c334ad048e5aba5ddf4
fig3_Tc2_star_infield.csv : e5c22e6b7ecbf6f3b0688823e6cd61a565175f34
All SIX original data CSV enclosed unchanged in full local ZIP. The large original ultrasound trace CSV files were NOT accessed and are NOT claimed reproduced.

## Strict direct-data findings, no fits
All FIVE shared Fig2 pressures (GPa) have strict Tc2>Tc1>Tc2star, measured original author source rows:
P=.208 : Tc2 1.610, Tc1 1.585, Tc2star 1.300 Kelvin
P=.211 : Tc2 1.620, Tc1 1.585, Tc2star 1.020
P=.213 : Tc2 1.630, Tc1 1.585, Tc2star 0.740
P=.214 : Tc2 1.630, Tc1 1.585, Tc2star 0.660
P=.218 : Tc2 1.650, Tc1 1.579, Tc2star 0.400.
Source Tc2star lies 0.285 to 1.179 K below Tc1 over real measured coordinates; Tc2 lies 0.025 to 0.071 K above Tc1. That DISTINCT THIRD BRANCH is already in the author figure, not discovered by XH. The physical tetracritical intersection is outside the range of these shared points.

## Extrapolation is not independent measurement of Pstar
Exact fractions.Fraction unweighted linear fit to ALL SIX author Fig2 Tc2star rows (including P=.210,T=1.09) gives slope -92.5543478261 Kelvin/GPa and intercept 20.5207065217 K. Intersection of this extrapolated LINE with a fixed LOCAL reference Tc1=1.585 K: P=0.204590135055784 GPa. Leave-one-out root range [0.204121794871795,0.205500000000000] GPa. This range is NOT a confidence interval, because no authors' pressure uncertainties or correlated error model were supplied in these phase-coordinate CSV files.

Separate exact linear fit to five paired author Fig2 differences (Tc2-Tc1), cross zero at P=0.203080256821830 GPa; leave-one-out cross range [0.2010000000,0.2044925373]. These DIFFERENT fitted crossings must not be forcibly merged into a precision tetracritical point by assuming both lines linear outside actual measured domain. Physical phase-boundary curvature and nonlinear thermodynamic constraints are open.

Independent NumPy numerical model validation for six Tc2star values: polynomial degree1 training RMSE .0452459062K, LOOCV RMSE .0901111460K; degree2 training .0272755247K, LOOCV .1297486366K; degree3 training .0156225841K, LOOCV .0818499636K yet FIVE of SIX LOO fits have no real intersection with 1.585K in chosen local P window [.195,.208]. Lower in-sample error is NOT a reliable physical extrapolation. No invented sigma, error bars or Pstar uncertainty.

## Important NO-POOL source-lineage gate: Fig2 versus Fig3 data
At P=.210GPa and B=0, original author Fig3 has Tc1=1.38K, Tc2=1.51K, Tc2star=.98K. Separate author Fig2 at same P gives locally interpolated Tc1=1.585K and Tc2=1.616666667K, and directly observed Tc2star=1.09K. Fig2 minus Fig3 differences +.205,+.106666667,+.110 Kelvin. These are data from DIFFERENT FIGURE SERIES; original experiment may have sample/pressure calibration and measurement-protocol distinctions. DO NOT claim data inconsistency, manipulation or significant discrepancy; without cross-series harmonization, NEVER pool them as IID observations or treat differences as estimated noise.

## Executed independent reproducibility and custody
A) Original source-data Git blobs checked on bytes by Python stdlib and connector. Independent pure-stdlib exact rational regressions, every shared inequality, leave-one-out crossings, strictly bracketed interpolation, no hidden source merging. Executable rot018_exact.py and frozen rot018_exact_results.json.
B) Separate NumPy polynomial degree1/2/3, independent LOOCV, scipy.stats.theilslopes robustness, distinct Fig2 vs Fig3 check. Executable rot018_independent.py and frozen rot018_independent_results.json.
Complete ZIP has 14 files: detailed 9143-byte Polish scientific report, SIX byte-original source CSV, TWO executable programs, TWO frozen JSON, README, verify_replay.py, manifest_sha256.json. ZIP CRC PASS, SHA256 for all 13 archive members listed in manifest PASS, all six original author Git blob checks PASS, CLEAN extracted rerun both programs produced TWO JSON BYTE IDENTICAL PASS. Runtime Python3.13.5 NumPy2.3.5 SciPy1.17.0.
MODERATOR LOCAL COMPLETE ZIP: IW_XH_S5_ROT018_UTE2_PRIMARY_DATA_TETRACRITICALITY_REPRO_20261102.zip
ZIP SHA256 62f350d5c02665034b2536e1871bf36c982e98b519b533ec59d61bb4d4683dce.
LOCAL FULL REPORT SHA256 8468eb10f846736a4c54033abf3330c7ccca2bb6213b4c444075d55422510699.
This remote GitHub report is scientific custody but NOT the actual full ZIP or raw ultrasound traces.

## Future physical test not done
Download original c11/c33/c55 large traces, blinded onset/jump fits with background drift and thermal pressure calibration; compare error bars/heat-capacity thermodynamic constraints; independently harmonize Fig2 and Fig3 sample/magnetic field and coordinate systems. These are not performed, initiated or delegated; source findings not refuted. No cross-cell cascade, no BW owner acceptance assumed.
NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_SOURCE_RAW_ULTRASOUND_REPRO / BW_INGEST_UNVERIFIED.
