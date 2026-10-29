---
artifact_id: IW_PRF12_R20_REPRODUCIBILITY_MANIFEST_001_20261029
created_at: 2026-10-29
origin_cell: PRF12
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: LOCAL_REPRO_PASS / ZIP_CRC_PASS / BYTEWISE_SHA256_PASS / GITHUB_REPORT_BLOB_PARITY_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC / NO_FINITE_PREP_READOUT_DRIVE_PROOF / NO_ORIGINAL_SINGLE_COPY_LOCC_CLOSURE_GAP
---

# PRF12 R20 — reproducibility manifest and source custody

Main scientific report: IW_PRF12_R20_FIXED_DRIVE_RAMSEY_PAIR_PHASE_INVARIANT_SOURCE_DISCRIMINATION_001_20261029.md

GitHub shorter runnable core script: IW_PRF12_R20_RAMSEY_PAIR_CORE_REPRO_001_20261029.py

Full local independent NumPy/SciPy script (5280 bytes), complete run log, R19 fixed-Omega comparison script, full scientific report and JSON member hash manifest are preserved in conversation archive: PRF12_R20_reproducibility_bundle_20261029.zip.

ZIP SHA-256: `98e0a8f9ac267cee87a1b944dcf16e0b3bee06a4379d6f67941b49fde8ed06d4` (13,269 bytes), four study members plus one manifest; ZIP CRC PASS and each extracted member SHA-256 recheck PASS.

Scientific report SHA-256: `786b4b0e4b89b94201f7105485a869d27cd6bdeebaa9d41184a71897336efd8a` (16219 bytes). Its GitHub blob SHA is `7583f064640370efb4a548788e14e043239b7d0c`, independently computed locally via git hash-object and verified by GitHub fetch.

Full local Python SHA-256: `209543d2f202453270b2a1b6672b4f0fa0831566dbf8ed83d9006caa7069aadc`.
Bounded-echo R19 comparison Python SHA-256: `654809a0b290f1bcc0ef4340e4785c78f517070e30a0636809fa6154787c4c91`.
Full run log SHA-256: `0514d476830e1e3cae11e0f087d500a2fe24e83ce4781bd74a85319d00428717`.

Tests: 307 static phases times 3 rotated orthogonal-axis pairs; 7 values q; direct two-qubit 4×4 density matrices; exact U(1)-twirled Helstrom eigenvalues; exact finite-sample binomial tails; q=.579,N=80; numerical homogeneous Chernoff/time maximizer; all-phase relative-axis-skew and independent visibility tests; counterexample unequal Ramsey durations; R19 prior sufficient eight-run bounded-echo error comparison over eight fixed Omega*T values.

**Non-transfer boundaries:** R20 requires one and the SAME static hidden source frequency during two Ramsey shots within each pair; it allows arbitrary source reset dependence only BETWEEN pairs. Preparation/readout assumed ideal, not a complete fixed-Omega physical implementation. There is no driven echo π pulse or SWAP during the source exposures. Source B needs independent increments across shots. R20 no proof of original three-qubit asymptotic LOCC gap.

Independent scientific referee and BW readback pending. NO_CANON / NO_EXEC.
