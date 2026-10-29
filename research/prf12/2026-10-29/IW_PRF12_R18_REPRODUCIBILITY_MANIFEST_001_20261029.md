---
artifact_id: IW_PRF12_R18_REPRODUCIBILITY_MANIFEST_001_20261029
created_at: 2026-10-29
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: RUN_PASS / GITHUB_READBACK_PENDING / ZIP_CRC_PASS / ZIP_SHA256_MEMBER_READBACK_PASS / REFEREE_PENDING
claim_ceiling: NO_CANON / NO_EXEC / NO_FORMAL_FLOAT_INTERVAL_CERTIFICATION / NO_SINGLE_COPY_LOCC_CLOSURE_RESULT / NO_NOVELTY
---

# PRF12 R18 — exact custody and source manifest

Full scientific report, source contract, algebraic error enclosure and limits:
IW_PRF12_R18_FULL_THREE_QUBIT_ACTIVE_SWAP_DYNAMICS_CAUCHY_TAIL_CERTIFICATE_001_20261029.md

GitHub compact independent runnable source (NumPy + SciPy):
IW_PRF12_R18_DIRECT_ACTIVE_SWAP_SHORT_REPRO_001_20261029.py

**Full** standalone Python source (12,153 bytes) with complete test suite, full stdout, scientific summary and machine-readable manifest are packaged in the conversation attachment:
PRF12_R18_reproducibility_bundle_20261029.zip

Exact archive SHA-256:
\`ef2a0138cbcd2bb22b329e4b6a26edce99c6c5f5b0395fdc119982922172ab7a\`

Member file hashes:
- Full Python code \`b356f1dc2cf4d80acce3d274c9601892d9a281839cc0be6c3b00fefd9126c992\` (12153 bytes)
- stdout log \`ceb43bec401e8bea37cc942aa23b23aef187180d5fa531406288f1362dd0bf4d\` (5417 bytes)
- science summary \`9eec6c25165e9e76a10ec38caf99f647bad4537c0690ad44da91a020c53206ac\` (2406 bytes)
- JSON manifest inside ZIP lists the 3 complete member hashes.

Archive integrity: \`zipfile.testzip()\` PASS, and all extracted member SHA-256 hashes matched. The full script was executed with
\`python IW_PRF12_R18_FULL_ACTIVE_SWAP_DYNAMICS_REPRO_001_20261029.py --checks --certificate --witness --fixed-clock --grids 144 288 576\`.
No stochastic Monte Carlo or fitted parameters were used in source A integration. Full A is conditional 8x8 unitary followed by a **deterministic** Cauchy integral; B uses 64x64 Lindblad expm. Independent matrix expm, ODE and memory dephasing controls PASS.

Scope: the analytic error **of the Cauchy integral** is controlled by source-tail mass and an explicit Duhamel Lipschitz bound. Floating-point evaluations of conditional amplitudes and matrix exponential are numerically cross-checked, **not formally interval-certified**. The reported lower contrasts have large numerical safety margins. Some Gauss–Legendre values are only stable to about 1e−4; treat them as approximate. Do not conflate average contrast with phase-uniform discrimination under a shared persistent hidden Xi. Independent referee pending; no BW readback.

External mature foundations: Lindblad equation and Markovian pure dephasing, https://www.nature.com/articles/s41534-019-0189-0 ; quasi-static vs white-noise distinction, https://qopt.readthedocs.io/en/latest/examples/t2_markovian_noise.html ; internal first-owner PRF11 R35 and R02/R16/R17.
