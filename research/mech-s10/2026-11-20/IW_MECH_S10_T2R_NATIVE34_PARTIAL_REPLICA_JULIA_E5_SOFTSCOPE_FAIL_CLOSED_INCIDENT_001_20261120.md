---
artifact_id: IW_MECH_S10_T2R_NATIVE_ONE_SHOT_34_OF_68_TECHNICAL_FAILURE_FORENSIC_001_20261120
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10
date: 2026-11-20 Europe/Warsaw
classification: ORIGINAL_SOURCE_NATIVE_PARTIAL_REPLICA_WITH_FAIL_CLOSED_TECHNICAL_INCIDENT
human_authorization: MODERATOR_DIRECT_20261120_1449
one_shot_original_run_id: 44749222324
one_shot_original_job_id: 136332455187
outcome: 34_ORIG_NATIVE_PASS / 0_E5_NATIVE / R_SHIFT_NOT_ESTIMABLE / NO_RETRY
claim_ceiling: NO_PAPER_ERROR / NO_NEW_PHYSICAL_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
exposure: PUBLIC
---

# Mech-S10 T2R — one-shot native attempt: 34/68 original Wu–Xu calls; E5 zero-call Julia scope abort; no fabricated root shift

## 1. Authorization and irrevocable frozen input

Human Moderator on 20 Nov 2026 ~14:49 CET commanded Mech-S10 to perform independent T2 replica. Mech-S10 froze the exact previously approved 68-call scope before any native action:
- PREREG Mech-S10: research/mech-s10/2026-11-20/IW_MECH_S10_T2R_68_NATIVE_ONE_SHOT_PREREG_001_20261120.md, Git commit 61beff88674dcdd0ce1fd1e8d9697ad71588985d, blob 3c87cdd95fb498d02f4c2c1169680e54357603aa.
- Independently authored (NOT Badacz driver) Julia driver: research/mech-s10/2026-11-20/code/mech_s10_t2r_original_68_native.jl, Git commit 15c26132e029e9c86ab1c04c2f83ff8380f0608c, Git blob 8d1afc10ca96dd9fa1714aa1e8fc648abcfab722.
- Independent standard-library centered OLS7 output scorer: research/mech-s10/2026-11-20/code/mech_s10_t2r_independent_ols7_referee.py, Git commit fbc2abd29bb8feaa2473758993874e11c86484ac, blob a144f840fb2ccfa72fdc48e12637b66d8baff126.
- Workflow one-shot .github/workflows/mech-s10-t2r-one-shot-native68-20261120.yml, committed 129e70d8a4c350ea6aa49c63918d5f5591f23fdb and self-triggered ONCE, GitHub Actions run 44749222324 / job 136332455187.
- Earlier Badacz owner actual native 232 calls, exact source 069 frozen config; GPT Mech-S9 earlier source-only audit NOT independently native. T2R source acceptance gate frozen: |D22_Mech-D22_Badacz|<=.010 and |D62_Mech-D62_Badacz|<=.010 dex, where Badacz owner D22=.2722992609128987, D62=.29812358518660886.

## 2. Actually executed original native source: 34/34 orig PASS

GitHub Actions run 44749222324 reports PASS for exact Julia 1.12.3 setup, frozen hashes and source, original Wu–Xu clone checked out commit d395183674cace6c9906a8911bdeb7234ba4040d, original main-scan.jl blob b368ba55d5a493f7bc185909730f7fe5691f10d6, main-scan-parameters.jl blob 53faee65beda383348580c28d0424188da69b660, tool_script-parameters.jl blob 0d7198ff3557bdbd5753000bb07a7a7405cc24f5. Recovered packages were ArbNumerics 1.6.3, DifferentialEquations 7.17.0, NaturalUnits original pinned fork. No original Wu–Xu code changes in orig.

Original arm step: SUCCESS. Saved fully native CSV has EXACT 34 original author native calls, 17 original beta points for j22 and 17 for j62, native source stdout explicitly contains each of 34 lines NATIVE_T2R_DONE plus summary NATIVE_MECH_S10_T2R_orig_34_CALLS_PASS. This is not owner data arithmetic replay. All source-Y values finite, both 17-node series contain exactly one threshold-crossing of Y_code=0.251, no extra mass nodes.

Independent Python read-only audit of REAL downloaded original GitHub artifact, not the GitHub step status:
- artifact ID 14634987623; original ZIP size 17,870 bytes, exact SHA256 0d3675c8f46488c5c203fb659453942aad71fd6501ecbd19466bb1de7ea9e5dd; ZIP CRC PASS and 16/16 original native output manifest SHA-256 PASS;
- actual orig source CSV SHA256 98ae768c95f7d9de2aba90dce52fd7a53d3296e11212b758bdb53fa5ef62b5b7, 34 rows, all source j/masses and beta grid PASS.

Fresh independent centered 7 nearest points OLS of genuine Mech-S10 native orig outputs (not owner reconstructed values):
- j22: root orig=-17.22119161664116; Badacz owner orig=-17.221191616641164; difference +3.552713678800501e-15 dex.
- j62: root orig=-19.39132783946381; Badacz owner orig=-19.39132783946381; difference 0.0 dex.

These are genuine independent orig-only output agreement numbers, NOT replication of the E5-vs-orig contour shift.

## 3. Exact E5 failure, source-type classification and reproducibility

GitHub Actions E5 arm step FAILURE, and downstream full 68-call independent R-SHIFT score correctly SKIPPED. Original error from SAVED E5_NATIVE_STDERR:
  Warning: Assignment to main_source in soft scope is ambiguous because a global variable by the same name exists: main_source will be treated as a new local.
  ERROR: LoadError: E5_SOURCE_UNEXPECTED
  at independent driver source line 38.

The E5 source-modifier itself DID PASS and its actual native stdout reports the four intended x0.5 source mappings, K0L unchanged. However in a Julia top-level conditional the assignment main_source=read(patched,String) created a SOFT-SCOPE LOCAL variable instead of updating the preceding original global variable. Consequently the driver then checked the unmodified source and FAIL-CLOSED on E5_SOURCE_UNEXPECTED before any E5 original author 10D magic() invocation. No saved E5 CSV, no per-node NATIVE_T2R_DONE arm=e5, E5_STATUS missing. This is a Mech-S10 driver scoping defect, NOT a Wu–Xu scientific result, Badacz error, E5 patch failure or Julia solver convergence issue.

Auditable native call ledger exactly orig=34, E5=0, total=34 of permitted 68. There is no E5 root, hence no native D_j, R-SHIFT gate uncomputed, R-BIT across arms undefined. Never combine these Mech orig values with Badacz E5 data and call it an independent native shift.

## 4. Safe prepared technical remedy, NOT executed

The exact source-level remedy is to ensure patched main_source escapes the conditional local scope (for example global main_source=read(patched,String), or assign from a function result).
A correction with an E5-ONLY control (so it cannot run the completed orig 34) has been saved AFTER the failed run, preserving the original immutable driver and audit record:
  research/mech-s10/2026-11-20/code/mech_s10_t2r_E5_only_softscope_fix_v002_NOT_EXECUTED.jl
  commit 1f1b76c8031ed423b7ecb534c582cd149f568ec4.

This v002 is PREPARED AND NOT NATIVE EXECUTED; no second workflow file, no second native run, no automatic duplicate. The frozen one-run prereg expressly required STOP + separate human decision after technical failure; reusing the original complete orig 34 would constitute a duplicate. A specifically approved E5-only missing-34 continuation can use a freshly preregistered explicit technical amendment and a one-time e5-only workflow, while preserving the original GHA run 44749222324 and owner firstness. It must not be presented as a single run of 68 calls; scientific aggregate would contain two technical runs with explicit separate provenance and zero duplicated native parameter points.

## 5. Evidence and conclusion

Original authentic GitHub workflow run:
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/44749222324

Artifact 14634987623, actual runner-provided original 17870 B ZIP downloaded, independently full checksum and exact content audited. Portable local independent source ZIP auditor:
  mech_s10_t2r_native34_partial_audit.py SHA256 448aefc531297c59043a6f23ce56c9ef75e0cffcc60503f6794a4b0ccca2acfc
  mech_s10_t2r_native34_partial_audit.json SHA256 07c597f7184d0b953e7a163e972c8f40ec214f4aa7f773da9a9860351288222c

One root pair for orig native source matches Badacz within the observed 3.55e-15 dex/0 dex precision. However **T2R independent orig-versus-E5 replica is INCOMPLETE**. The independent native 68-call claim FAILS, the native shift D22/D62 is UNKNOWN, and R-SHIFT PASS is NOT granted. This is the required provenance preserving outcome rather than marking partial solver execution as success or repeating a failed experiment without fresh authorization.

NO_NEW_PHYSICAL_PBH_BOUND / NO_AUTHOR_PAPER_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
FINAL: MODERATOR_AUTHORIZED_ONE_SHOT_GHA_ATTEMPTED / REAL_ORIG_34_NATIVE_PASS / E5_SOFTSCOPE_ZERO_NATIVE_FAIL / INDEPENDENT_T2_SHIFT_INCOMPLETE / NO_RETRY / NO_CANON / NO_EXEC_SIGN.
