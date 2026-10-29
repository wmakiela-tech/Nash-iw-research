---
artifact_id: IW_PRF12_R17_REPRODUCIBILITY_MANIFEST_001_20261029
date: 2026-10-29
origin_cell: PRF12
sync_state: GITHUB_PENDING_BW_INGEST
status: GITHUB_READBACK_PASS / CONTAINER_REPRO_PASS / ZIP_CRC_PASS / SHA256_EXTRACTED_MEMBERS_PASS / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC / SINGLE_RUN_FULL_LOCC_CLOSURE_OPEN
---

# PRF12 R17 — Complete custody and reproducibility manifest

Report: `IW_PRF12_R17_SOURCE_ACTIVE_SWAP_STORAGE_AND_AXIS_ROBUSTNESS_001_20261029.md`
Full NumPy/SciPy reproducer (ZIP member): `IW_PRF12_R17_SOURCE_ACTIVE_SWAP_STORAGE_AND_AXIS_ROBUSTNESS_REPRO_001_20261029.py`
Shorter standalone GitHub mirror reproducer: `IW_PRF12_R17_SOURCE_ACTIVE_SWAP_STORAGE_AND_AXIS_ROBUSTNESS_REPRO_001_20261029.py` (same name, abbreviated code; **not byte-identical to ZIP full code**).
Full execution log in ZIP: `IW_PRF12_R17_RUN_LOG_001_20261029.txt`.
JSON member hashes in ZIP: `IW_PRF12_R17_REPRO_MANIFEST_001_20261029.json`.

Local ZIP path: `PRF12_R17_reproducibility_bundle_20261029.zip`.
ZIP SHA-256: `e081f65a49a99216ae537d19f833a89e4fd76290eef71c6b249ef3218b8508c0`.
Report SHA-256: `1dd9b591512b82186cce65b6993a854053332a8eba89d862df955e29f07b60e9`.
Full Python SHA-256: `f5fcf27e0612d74e81a14f99f09cb64d66a5f3fc0eef5a5bb4921d51242a7874`.
Run log SHA-256: `6baef9f3346ba27b64679aa4643d7b8015562630dcc955313d6d855ee24cee87`.
GitHub report blob SHA (verified byte-identical to local report, terminal newline preserved): `76d7cbc7b5ace9799d38cc3ef584207426500ceb`.

Checks:
1. Direct NumPy exact source matrix equalities for four memory κ configurations, four q values, 30 random hidden phases each.
2. Direct 8x8 arbitrary common phase/axis mismatch identity for five epsilon values, six phases each.
3. Cauchy clipped-moment analytic formula separately checked against quadrature.
4. Two-qubit source-active finite-SWAP exact Hamiltonian diagonalization and independent B controlled Lindbladian exponential vs Duhamel bounds.
5. Memory-only exact minimum equal-prior average N=119 and both-condition N=121.
6. Analytic confidence numbers at tail δ=.01 and .05 checked.
7. Archive `zipfile.testzip()` and full extracted-byte SHA-256 for all four members PASS.

Important distinctions: one-run Cauchy average does NOT imply iid runs under persistent Xi; finite pulses use T_phys=T_free+2τ, not an impossible free-time equality; positive contrast bounds do not establish all-protocol optimality. Reviewer pending, no BW ingestion readback.
