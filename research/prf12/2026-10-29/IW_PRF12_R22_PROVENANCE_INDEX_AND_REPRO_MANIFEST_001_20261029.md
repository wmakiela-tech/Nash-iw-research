---
artifact_id: IW_PRF12_R22_PROVENANCE_INDEX_AND_REPRO_MANIFEST_001_20261029
created_at: 2026-10-29
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: FULL_GITHUB_TEXT_READBACK_PASS / MP_IV_3501_GRID_PASS / ANALYTIC_FAR_DETUNING_PASS / DENSITY_MATRIX_PASS / ZIP_CRC_PASS / MEMBER_SHA256_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_FINITE_TERMINAL_DETECTOR / NO_HARDWARE / NO_NOVELTY / NO_CANON / NO_EXEC / ORIGINAL_SINGLE_COPY_LOCC_GAP_OPEN
---

# PRF12 R22 — full source index, executable verification, and checksum custody

**Executive theorem:** Fixed source-ON rectangular controls (gamma=1, Omega_max=10, free Delta=.5), two sequential fresh sensor preparations with the SAME static A xi within each pair, one uniformly random common axis X/Y/Z, finite source-ON Y preparation and finite source-ON X/Y analysis pulses plus ideal terminal Z projectors: **p_A(same | xi)>=.5753 FOR ALL xi IN R**, versus source B with independent Levy increments in all stages **p_B(same)<=.5460**, giving a verified strict contrast >=.0293. The test achieves errors <=.045656 and <=.044206 respectively with 3,300 pairs and agreement-count decision threshold 1,851, even for arbitrarily correlated exogenous xi across pairs. Not a claim of fixed-duration detector/reset implementation; not a result for original three-qubit LOCC closure.

**Full scientific body:** Seven ordered parts; GitHub full fetch and EXACT string reassembly with the terminal newline agrees with the local complete source of **17,945 characters / 18,176 UTF-8 bytes**.

- [Part 00 — complete source segment](IW_PRF12_R22_FULL_PROOF_PART_00_001_20261029.md)
- [Part 01 — complete source segment](IW_PRF12_R22_FULL_PROOF_PART_01_001_20261029.md)
- [Part 02 — complete source segment](IW_PRF12_R22_FULL_PROOF_PART_02_001_20261029.md)
- [Part 03 — complete source segment](IW_PRF12_R22_FULL_PROOF_PART_03_001_20261029.md)
- [Part 04 — complete source segment](IW_PRF12_R22_FULL_PROOF_PART_04_001_20261029.md)
- [Part 05 — complete source segment](IW_PRF12_R22_FULL_PROOF_PART_05_001_20261029.md)
- [Part 06 — complete source segment](IW_PRF12_R22_FULL_PROOF_PART_06_001_20261029.md)

**GitHub compact runnable core:** [R22 finite XYZ interval grid and independent B numerical reproduction](IW_PRF12_R22_SOURCE_ON_XYZ_INTERVAL_REPRO_001_20261029.py). This shorter mirror DOES NOT implement the full B Taylor interval remainder or independent density-matrix audit; those are in the complete ZIP full runner.

**Full local conversation reproducibility archive:** `PRF12_R22_reproducibility_bundle_20261029.zip`
SHA-256 `8183fd7d971d7a2253403e681fa251dd0e87956e613794eeb3ddb0b7625f98ff` (14,763 bytes); ZIP CRC PASS and all extracted member hashes individually verified.

SHA-256 of complete members:
- Full report: `731e591eb757e4b2a286d9f7e53679df22e308f8bda5379d4ca63e8648f0a09d`.
- Full standalone Python: `0db6b32f23fa359bd656103e4b72f67de6dfcde57c398af4c394660344416108`.
- Independent 2×2/4×4 density audit: `d9b0f7263a35ffdd027ab423c50ce61065bb872a647ed8d2851eb1c9a7f27a75`.
- Main execution stdout: `ad3c8b6fb2597e9e0b4a30189859801e8b60090410748339deeb5ac45bed92f8`.
- Density-audit stdout: `5c060b7ecc3142d179e5bde77e608dcbcb4981b717a5bfa9f27f3bc8acf2cc4c`.

Member hash registry is also inside the ZIP as `IW_PRF12_R22_REPRO_MANIFEST_001_20261029.json`. Full code dependencies Python3, mpmath, NumPy, SciPy.

Review caveat: mpmath.iv directed interval arithmetic for 3501 compact grid values, explicit analytic Duhamel bound L<.815, analytic off-resonant amplitude bound for |xi|>=35, rigorous B Bloch Taylor remainder <1.1e-72 per gate with inflated interval, independent 2×2/4×4 check. No independent referee or BW ingestion verified. No physical real-device verification and no formal proof-assistant reimplementation. External mature sources: Kukita et al. PRA 106 042613 (2022), randomized purity review Physics Reports (2024).

**REVIEW REQUEST:** audit the source-ON analysis axis signs, the globally quantified xi and private fair-axis timing, interval rounding/remainder, binomial stochastic domination with between-pair dependency, and missing detector/reset duration. NO_CANON / NO_EXEC.
