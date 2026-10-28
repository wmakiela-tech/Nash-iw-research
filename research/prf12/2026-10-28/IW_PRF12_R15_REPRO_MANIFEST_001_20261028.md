---
artifact_id: IW_PRF12_R15_REPRO_MANIFEST_001_20261028
created_at: 2026-10-28
origin_cell: PRF12
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: NUMPY_36_FIXTURES_PASS / ZIP_CRC_PASS / SHA256_MEMBER_READBACK_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_SINGLE_COPY_MINERROR_LOCC_CLOSURE_GAP / NO_NOVELTY
---

# R15 — reproducibility manifest and custody

Scientific report:
IW_PRF12_R15_OPTIMAL_LOCC_HERALD_UNDER_PARTIAL_SOURCE_RESET_001_20261028.md

Standalone NumPy reproducible source:
IW_PRF12_R15_RESET_PARTITION_SEP_OPTIMAL_HERALD_REPRO_001_20261028.py

Full local run transcript:
IW_PRF12_R15_REPRO_STDOUT_001_20261028.txt

Complete local archive:
PRF12_R15_reproducibility_bundle_20261028.zip

All 3 files were included together with JSON manifest in the ZIP, verified via Python zipfile.testzip, followed by full extracted byte SHA-256 comparisons: PASS.

Local source SHA-256: fa9050b993ed106a719ec9e6bc22fee353895c573e21f16b12c51a484e018499
Local report SHA-256: c131ddc66aab05c707acce11af1b42f986635c68a09e36842eff4e9b9551247c
Local stdout SHA-256: 02f668f349554e86a3c08240472b26997ced5c1f51b7348b908700d43afda6e7
ZIP SHA-256: eed05dd7f23f0d3dbbcbd12ca9f57a674370f4223ed6e8642e1487292ae8e7f1

Numerical sanity checks: 4 values of q multiplied by 9 source-reset partitions = 36 independent fixture combinations; direct local traces, subset global traces with 3r<=9, source-orbit local permutation symmetry, positivity and independent B herald probabilities all PASS.

Mathematical result: for known reset partition G with lengths m_j, three-lab separable and LOCC maximum of unambiguous B-only success is 1-(product h_mj)^3. Unrestricted joint measurement maximum is 1-product h_3mj. This is conditional on B and is a ONE-SIDED unambiguous statistic, not the minimum-error Helstrom/LOCC-closure problem on one copy. Initial source PRF11 R35, nearest first owner PRF12 R14. No independent referee review or BW readback yet.
