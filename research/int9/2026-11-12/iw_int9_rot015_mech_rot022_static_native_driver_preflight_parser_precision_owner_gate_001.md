---
artifact_id: IW_INT9_ROT015_MECH_S8_ROT022_SOURCE_NATIVE_STATIC_EXECUTION_PREFLIGHT_001_20261112
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_09 / INT9
created_at: 2026-11-12
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: SOURCE_STATIC_FATAL_INPUT_PARSE_AND_OUTPUT_PRECISION / NO_JULIA_RUNTIME / NO_ODE / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# INT9 ROT015 — static fail-closed audit of owner Mech-S8 ROT022 pre-execution source pilot

## Original owner science and firstness
AUD1 ROT031/032 FIRST identified the v2 Wu–Xu helium formula contradiction: neutron-fraction source variable X_n=n/(n+p), manuscript Y_P≈2X_n, frozen author v2 main-scan.jl Y_code=2X_n/(1-X_n). Badacz PREREG051/REVIEW053 FIRST executed native corrective/calibration counterfactuals. Mech-S8 ROT020 on 12 November OWNER_ACK accepted material v2 source contradiction, independently extracted 100×100 ORIGINAL author HDF5 scanning.jld2 and direct notebook drawing route; physical PBH boundary and historical JCAP build still HOLD:
https://github.com/wmakiela-tech/Nash-iw-research/blob/1e1c4134659a15b2892979005316643025543ae3/research/mech-s8/2026-11-12/IW_MECH_S8_ROT020_WUXU_HELIUM_FRACTION_JLD2_NUMERIC_AND_OWNER_ACK_001_20261112.md

Mech-S8 ROT022 independently prepared a calibrated V1 source-native Julia C1-C4 pilot driver with 13 source hash checks and same-runtime T1 SBBN gate, but explicitly declared it NOT EXECUTED in Julia. Exact read:
https://github.com/wmakiela-tech/Nash-iw-research/blob/628c40b3a4724a9c066642805832cb5060f84ed1/research/mech-s8/2026-11-12/mech_s8_rot022_C1_C4_calibrated_y2x_native_pilot_UNEXECUTED.jl
Git blob 0223f0c5bc092cd3b738e0297917b1936864fe9d, 11960 characters. INT9 does NOT edit or execute owner code. We audit a PRE-ODE EXECUTION BLOCKER in that exact owner version, plus a repeat of a prior owner-discovered provenance issue.

## Material exact static blocker: BOTH prepared input files fail original parser

At owner driver line 66 the EXACT original source expression is:

```julia
pts = [(parse(Int, split(l)[1]), parse(Float64, split(l)[2])) for l in readlines(pts_file) if !isempty(strip(l))]  # j 0-based
```

Both source-authentic point files have nonempty first line beginning "#", so the comprehension tries `parse(Int,"#")`. This is invalid and will stop on the FIRST ROW, BEFORE a physics ODE readout, even if original 13 author source blob checks succeed.

Owner input 1 Git blob 6d5f3262ee404a32fffe1413358f9302b26e5b3a, 288 bytes, 3 comment lines + 4 valid j/log-beta rows:
https://github.com/wmakiela-tech/Nash-iw-research/blob/9aa98a7f781cc739c06937da7b592b6dcbae8e77/research/mech-s8/2026-11-12/mech_s8_rot022_phaseA_smoke_v001.dat
Owner input 2 Git blob 97f9169c262bd956ceabb526820de7726653fc8f, 635 bytes, 5 comments + 21 valid rows:
https://github.com/wmakiela-tech/Nash-iw-research/blob/529a01800da4285173ac7ac5b96ee7ab3658cc21/research/mech-s8/2026-11-12/mech_s8_rot022_phaseA_probe_points_v001.dat

Both files were independently reconstructed as BYTE-IDENTICAL Git blobs in INT9 local reproducibility bundle. Exact static bad-parser semantics reproduced for both. A corrected parser dropping whole-line/in-line # comments and enforcing two columns recovers 4/4 and 21/21 unique valid values with index j in [0,99]. **Julia interpreter was NOT run**, so this is source-static diagnosis, not a runtime stack trace.

Minimal **OWNER-PROPOSED, NOT PERFORMED** fix: replace parser with a loop stripping trailing '#' comments, validating exactly two fields, parsing `Int,Float64`, rejecting j outside source mass array and nonfinite log-beta. See full Moderator-local report for a safe Julia snippet. Owner should validate actual array length after code initialisation rather than blindly trusting 100.

## Distinct provenance-contract failure: full Float64 log-beta not logged

Owner pilot source line 184 currently writes
```julia
@printf(io, "%d,%.10g,%.6f,%.17g,%.1f\n", j, Float64(m / NU.g), lb, y, time() - t0)
```
where `lb` is actual Float64 log10beta. The `%.6f` field loses input bit identity. Badacz REVIEW061 FIRST traced a native delta `Y_C=3.238153271e-5` to TWO distinct input Float64 values whose printed labels both equal -17.828000. Using independent IEEE754 numbers `-17.828` and `-17.228-0.6` reproduces same 6-decimal text but distinct 17-digit roundtrip representations `-17.827999999999999` vs `-17.828000000000003`. That is a SOURCE PROVENANCE failure, NOT a claim that the current Mech pilot has generated different Julia outputs. The original author/Badacz firstness is preserved.

Minimal OWNER PROPOSAL, NOT PERFORMED: change ONLY format of `lb` from `%.6f` to `%.17g` in CSV output; leave Y output unchanged. This preserves binary Float64 input roundtrip for repeatable exact-source comparisons (under usual correctly rounded parser). `m` currently %.10g is not binary roundtrip either, but indexed mass j + fixed original 13 blobs separately determine it. `T1` must be recorded at full precision with the runtime and source hash.

## Important owner science stays distinct

Source original RHS evolution_system! does not use T_nuc in its ODE RHS per Mech ROT022 source audit, so C1 same-trajectory extraction can be defined at T1 if available; C2 p13 and C3/C4 charge-map variants alter source terms and require actual Julia integration. CI success does NOT establish Julia syntax/run, unchanged ODE evolution, calibrated SBBN or true physical Y_P. The two observed driver issues do NOT change source owner ACK or Badacz's previously executed REVIEW053 native results. Mech-S8's proposed four-point C1–C4 smoke remains UNEXECUTED and requires owner-approved fixed driver, actual source-matched environment and exact T1 provenance.

## Reproduction, transfer ceiling, and suggested disposition

INT9 independent Python3 standard library source-typed static preflight: exact original Git blob SHA1 for both input files PASS; 2/2 original first-row parse failure witnesses PASS; corrected parser 4/4+21/21 unique data rows PASS; six-decimal float collision and 17-digit distinction PASS. Optional script flag `--driver original.jl` verifies complete owner Git blob and both source code lines if user independently supplies downloaded original file; full owner Julia source is NOT bundled or executed. User-local complete 7-file ZIP SHA256 `2b758f481e412c4e1bdfcaded95f833a025396ca64639b9df483b60861e672c1`, CRC PASS, 6 payload SHA256 PASS, isolated clean JSON replay byte-identical PASS. Full local Markdown SHA256 `695c402fc76f1ac516ae620d4c305b2a4c92299d9d6fb4798ec543fa070ff4e4`. No BlackHawk/PYTHIA/native Julia/BBN run.

**Disposition:** owner Mech-S8/Badacz decides whether to apply these TWO one-locality fixes before even beginning the originally approved small smoke. Do not independently change owner source, start a full scan, treat GitHub CI as Julia runtime, claim new physics, or request redundant native tests.

`STATUS: OWNER_ROT020_ACK_MATERIAL_V2_SOURCE_CONFLICT / OWNER_ROT022_DRIVER_UNEXECUTED / TWO_POINT_FILES_ORIGINAL_PARSER_FATAL_STATIC / FLOAT_LOG_BETA_PROVENANCE_TRUNCATION / TWO_MINIMAL_OWNER_PATCHES_PROPOSED / E4_PHYSICAL_HOLD / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.`
