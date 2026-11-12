---
artifact_id: IW_MECH_S9_ROT008_NATIVE_GPT_L2_INCIDENT_ORIGINAL_SOURCE_PRESERVATION_AND_FIXED_RETRY_001_20261112
created_at: 2026-11-12
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
document_type: ORIGINAL_SOURCE_NATIVE_EXECUTION_ERRATUM_AND_RETRY
claim_ceiling: VERIFIED_L2_WRAPPER_PATH_FAILURE_BEFORE_MODEL / FIXED_RETRY_NATIVE_RUNNING / NO_L2_NUMERIC_RESULT_AT_REPORT_CUTOFF / NONBLIND / NO_PHYSICAL_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# Mech-S9 ROT008 — native L2 incident, falsification of wrapper capability assertion and exact repaired source path

## FIRSTNESS / SOURCE IDENTITY

- Original Wu–Xu source author repo `Fenyutanchan/Primordial-Black-Hole`, exact git commit `d395183674cace6c9906a8911bdeb7234ba4040d`; original `arXiv-2509.05618/main-scan.jl` blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`, unmodified all runs.
- Badacz (Claude) FIRST native scientific results REVIEW053 (2026-11-08). EKS1 FIRST found forgotten remote Julia executor in Mech-S6 lineage and supplied strict L1→independent L2→Grok order. L2 classification is `NONBLIND` because Badacz's V0/V1/V2 roots informed coarse search brackets; no independent physics novelty claim.
- Mech-S9 ROT006 original Badacz driver L1 all 53 of 53 native result digit outputs identical to owner, source archive `13983688155` digest `sha256:2120d9c103e948db112ae3b4846d7b9003e469d1daa83c5c92318c9c39789603`, 17-file ZIP native original contents. This is a source-level original-model numerical replica, NOT paper publication build ID.

## Incident: first Mech-S9 autonomous native L2 exact log

Initial GPT-authored native Julia L2 driver created at public commit `2d1adbbe33925190e203931412fb238adc98a1ff`, path `research/mech-s9/2026-11-12/mech_s9_rot007_independent_native_L2.jl`, Git blob `f44cb0babdb931e936e04883d3a1e75f7e1e273b`. Real native GitHub Actions run `43308493869`, job `131497974547` ended `failure` after preflight and package freeze PASS.

Actual direct job stdout+uploaded artifact (id `13985551662`, ZIP SHA256 `e997107d25b49556242f3bc63335fa9e1228ee251ccc8372ac4055ce02f047c6`) were downloaded and examined. Preserved `NATIVE_L2_STDERR` reports at line 26:

```
ERROR: LoadError: SystemError: opening file ".../research/mech-s9/2026-11-12/main-scan-parameters.jl": No such file or directory
Stacktrace:
 ... include ... mech_s9_rot007_independent_native_L2.jl:26
```

Root cause: `include("main-scan-parameters.jl")` inside GPT driver is resolved relative to **the including source file path**, not the temporary `cd(author_dir)` context. This is `FM_INDEPENDENT_DRIVER_INCLUDE_BASEDIR`, not a failure in Wu–Xu 10D solver. The initial L2 did **not execute a single native PBH `magic()` evaluation**; no native L2 Yp, root or scientific difference can be inferred. Preserve original failed source unchanged and failed archived logs for audit.

## Precisely bounded one-issue source repair, no original author modification

The corrected GPT independent driver is separate:
`research/mech-s9/2026-11-12/mech_s9_rot008_independent_native_L2_FIXED_INCLUDE.jl`
at public commit `3d69cfc72fb31fe03e6719f2ea835830ffbb880c`, blob `5ca59bd911bbd12e4bb2b3deca9fbd3fa4ed0506`.

Change the single path binding:
```julia
# WRONG: searches directory of GPT script
include("main-scan-parameters.jl")
# CORRECT: original author file accessed via frozen author source dir
include(joinpath(author_dir, "main-scan-parameters.jl"))
```
Remaining changes are explanatory comment-only, original author's prefix `main-scan.jl` bytes and original `main-scan-parameters.jl` bytes unchanged. No numerical model, target contours, beta anchors, bisection algorithm or source mass grid changed.

Actual corrected workflow `.github/workflows/mech-s9-wuxu-native-independent-l2-rot008-fixed-include.yml`, commit `9e2ee03c342a56b6f57efb2e69292a829a0be2d4`, Git blob `a1d474d8358c8abbaea4490ac928a2a8e47cd2da`, readback PASS. Triggered native run:
`https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43310359194`.
Latest observed GitHub job: source check PASS, original frozen Julia dependencies PASS; native adaptive root computation **IN PROGRESS**. Run result not yet available at the writing cut, **NO L2 PASS CLAIM**. Independent Python post-run comparison is `mech_s9_rot007_L2_referee_comparison_stdlib.py`, executed only after Julia roots are recorded, with owner original reference only as post-run comparison.

## Source-number and bracket controls independent of failed L2

L1 original actual 53-point native CSV was decoded and examined locally:
- All 8 adjacent per-case source response slopes for each of `j22/j62 × V0/V1/V2` are positive (48/48 slope segments). One negative→nonnegative crossing per sampled 9-point case.
- This is a **discrete sample property only**, not a proof of continuous monotonicity of native `magic()`, physical Yp, or uniqueness between knots.
- Independently applied PCHIP vs linear numerical source-root extraction on real L1 data, differences in dex:
  - j22 V0 +0.000360880, V1 +0.000463381, V2 +0.000072419.
  - j62 V0 +0.000483593, V1 +0.001452715, V2 +0.001312273.
- PCHIP checks do NOT constitute an independent Julia L2 or new PBH bound. Native original solver adaptivity at j22 has larger previously observed source uncertainty (Badacz), so bisection bracket widths alone are not physical error bars.

## Strict claim ceiling

Source original model path and BBN/entropy physical compatibility concerns from Mech-S9 ROT001–004 remain unclosed. No independent L2 numerical verdict until successful GitHub workflow and independently retrieved `independent_L2_roots.csv` + reference JSON + job logs. The final published Wu–Xu JCAP run producer is not identity-verified, source E4 hadron production and physical beta bounds OPEN, no original source equation modifications and NO 100×100 full grid.
No BW ingestion claimed; `GITHUB_PENDING_BW_INGEST` is a mandatory metadata state, not a receipt. REC11/AUD1 referee remains independent.
