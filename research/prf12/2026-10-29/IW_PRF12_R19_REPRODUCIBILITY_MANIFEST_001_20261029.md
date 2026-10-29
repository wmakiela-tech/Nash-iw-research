---
artifact_id: IW_PRF12_R19_REPRODUCIBILITY_MANIFEST_001_20261029
created_at: 2026-10-29
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: LOCAL_REPRO_PASS / ZIP_CRC_PASS / BYTEWISE_MEMBER_SHA256_PASS / GITHUB_READBACK_PENDING / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_CANON / NO_EXEC / NO_NOVELTY / NO_FIXED_DRIVE_CONSISTENCY / NO_UNRESTRICTED_SINGLE_COPY_LOCC_CLOSURE_RESULT
---

# PRF12 R19 — reproducibility and custody manifest

**Full authoritative science report**: IW_PRF12_R19_FINITE_HAHN_ECHO_RESET_ROBUST_CERTIFIED_SOURCE_DISCRIMINATION_001_20261029.md, in the same GitHub directory.

**GitHub compact runnable reproducer** (NumPy/SciPy): IW_PRF12_R19_FINITE_HAHN_ECHO_GITHUB_REPRO_001_20261029.py. This is a deliberately shorter standalone version and NOT byte-identical with the full local executable.

**Full local conversation archive**: PRF12_R19_reproducibility_bundle_20261029.zip. Contains:
- IW_PRF12_R19_FINITE_HAHN_ECHO_REPRO_001_20261029.py (full executable, 5715 bytes), SHA-256: \`5780006a2d7eca5eefd1ef00d2f8888422c16ef5b8b8979a50e2da189b044748\`;
- IW_PRF12_R19_LOCAL_SCIENCE_REPORT_001_20261029.md (4905 bytes), SHA-256: \`28f5208f42ff1b4ce5b151895893ec0df824f6bcc84f0f2a6491a29d33f32ddd\`;
- IW_PRF12_R19_REPRO_LOG_001_20261029.txt (1973 bytes), SHA-256: \`da12bb46cbdd680fcfe95d4e3597d496d9f53c39fa2f45c0463aa6a5986826e1\`;
- IW_PRF12_R19_REPRO_MANIFEST_001_20261029.json, containing all above per-member SHA-256 values.

ZIP SHA-256: \`087814f56b106e94dcf549c96a8579477242acf91a0e499d5191fdd4c29628ed\`. Archive 7,233 bytes; \`zipfile.testzip()\` PASS and extracted member SHA-256 checks PASS.

Reproduction:
- 435 exact source-A spinor pulse probabilities checked independently against 2x2 unitary matrix exponentials;
- 15 exact source-B probabilities checked against the 4x4 Lindblad superoperator;
- 8-run at gamma*T_phys=1, tau/T_phys=.0008, tail=.004: A false-B upper bound .045904611302107 and exact B missed .047878728992407;
- 6 pulse-width/quantile tradeoff computations, sufficient frontier tau/T≈.000910418;
- far-tail fixed-Xi examples falsifying any all-Xi finite-width guarantee;
- 5 N values of tau_N=T/N^3, tail_N=N^-2 source-reset-history agnostic asymptotic consistency.

**Source contract**: one qubit, ONE finite X-axis Hahn echo pulse, no SWAP; A static xi throughout each run but arbitrary inter-run dependence of Cauchy-marginal draws; B independent Cauchy–Lévy increments throughout free and driven intervals. This is an additional controlled-source experiment, NOT the original fixed three-probe LOCC measurement. Arbitrary worst-case xi is excluded from the distributional guarantee. No finite-power asymptotic conclusion; Ω_N scales as N³.

REFEREE_PENDING; BW ingestion unconfirmed; NO_CANON / NO_EXEC.
