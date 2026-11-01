---
artifact_id: IW_PRF12_R23_SOURCE_INDEX_AND_REPRO_MANIFEST_001_20261101
created_at: 2026-11-01
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: FULL_GITHUB_TEXT_READBACK_EXACT / IV_ALL_XI_CERT_RECT_AND_CORPSE_PASS / INDEPENDENT_2X2_4X4_MATRIX_PASS / ZIP_CRC_AND_MEMBER_SHA256_PASS / REFEREE_PENDING
claim_ceiling: NO_CANON / NO_EXEC / NO_NOVELTY / NO_HARDWARE / NO_GLOBAL_OPTIMAL_AXIS_OR_PULSE / ORIGINAL_3Q_LOCC_CLOSURE_OPEN
---

# PRF12 R23 — complete source, scientific status and reproducibility

**Principal finding.** For source-ON bounded-amplitude Omega_max/gamma=10 finite analysis pulses and source-static Xi throughout two freshly prepared/destructively measured shots, the X/Y/Z basis probabilities w=(.18,.20,.62) give certified **globally uniform conditional contrast >=.0513001165064** with RECTANGULAR controls; conservative both-conditional-error <5% test: 1075 pairs, decision choose A if agreements>=593, worst total physical exposure+control time gamma*T=1750.4424. For the specifically declared 3-segment conventional CORPSE pulse at the SAME drive strength, conditional contrast >=.0518135394003, conservative 1134 pairs threshold 600, worst physical time gamma*T=6890.9544. The source A may have arbitrary between-pair Xi dependence, but Xi MUST be held constant within each two-shot pair; B must have independent Levy increments. These are no statements about original passive three-qubit single-copy LOCC closure.

**Authoritative full report.** Six Markdown parts, source-preserving, GitHub fetched back and concatenated with **exact 13410-character source equality** including trailing LF:

- [R23 full report part 00](IW_PRF12_R23_FULL_PROOF_PART_00_001_20261101.md)
- [R23 full report part 01](IW_PRF12_R23_FULL_PROOF_PART_01_001_20261101.md)
- [R23 full report part 02](IW_PRF12_R23_FULL_PROOF_PART_02_001_20261101.md)
- [R23 full report part 03](IW_PRF12_R23_FULL_PROOF_PART_03_001_20261101.md)
- [R23 full report part 04](IW_PRF12_R23_FULL_PROOF_PART_04_001_20261101.md)
- [R23 full report part 05](IW_PRF12_R23_FULL_PROOF_PART_05_001_20261101.md)

**GitHub executable core:** [R23 short NumPy/SciPy source-B and binomial test](IW_PRF12_R23_GITHUB_CORE_REPRO_001_20261101.py). Its scope is intentionally narrower than the full all-Xi certification.

**Complete standalone one-file certificate (ZIP member):** `IW_PRF12_R23_WEIGHTED_FINITE_SOURCE_ON_XYZ_RECT_CORPSE_REPRO_001_20261101.py` (5890 bytes; dependencies Python3 + numpy + scipy + mpmath). Runs both interval compact grids (3501 rectangle; 8001 CORPSE), conservative Lipschitz interpolation, analytic detuning tails, B-Lindblad Taylor enclosure and exact conditional binomial thresholds. Independent `IW_PRF12_R23_INDEPENDENT_DENSITY_AUDIT_001_20261101.py` (2108 bytes) uses 2x2 unitary and 4x4 Lindblad propagation at 16 settings. Test logs and machine-readable JSON manifest included.

**Complete local reproducibility ZIP:** `PRF12_R23_reproducibility_bundle_20261101.zip`, size 13142 bytes; SHA-256 `5fa889eb3b3744855a678e1d6962128385f770ecfc409bf18a2024e486f4d7e9`. `zipfile.testzip()` PASS; all extracted members SHA-256 recheck PASS.

Member hashes:
- Full report: `5d9427aa91a33f958385857e7312da5ba261f5dde8611ad2a5f21f773678e33e` (13448 UTF-8 bytes).
- Full standalone Python: `47e18188f461a0ef5af042a535fcd558e94f6ab38e274f78aeefa5f5ff662a9d` (5890 bytes).
- Independent matrix audit: `af2dc1bc72ab3e554d89312383d94127c3743295eba1a236c014ad8081a17a46` (2108 bytes).
- Main stdout: `321029fb7910302712033d898bbc191924b58f18fe9e6638b8d066d85fda0c32` (2488 bytes).
- Independent matrix stdout: `66a5b1692a502caa47890d2e60ca59066b25cd0eafc1b458d785ca70e55a2726` (227 bytes).
- JSON member-manifest included with named checksums.

**Scientific guards.** Optimizer weights w*=(.179119,.197449,.623431) are NUMERICAL finite-grid-only; the certified rational w are independently fixed and analyzed for ALL real Xi. The CORPSE comparator is one explicit conventional 3-segment sequence with opposite middle axis; no optimization of composite parameters nor alternate shaped-pulse search. The B series remainder upper bound follows exp(8)*8^121/121!<7e-89, inflated by 1e-45 in interval. No physical detector/reset/initialization time, no finite terminal Z measurement, no misalignment, no fixed total source correlation time, no full hardware claim. Source noise ON during all prep/analysis pulses; static Xi under A not reselected inside a pair. Independent referee and BW readback pending. NO_CANON / NO_EXEC / NO_NOVELTY.

**First-owner** PRF11 R35; R20-R22. **External source** Kukita–Kiya–Kondo, Phys. Rev. A 106 042613 (2022), DOI 10.1103/PhysRevA.106.042613 for established off-resonance CORPSE family. Next R24: physically finite detector and reset, correlations within the pair, and cost-normalized optimized pulse sequence.
