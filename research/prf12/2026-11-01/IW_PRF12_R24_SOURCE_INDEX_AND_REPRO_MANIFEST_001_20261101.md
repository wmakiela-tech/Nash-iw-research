---
artifact_id: IW_PRF12_R24_SOURCE_INDEX_AND_REPRO_MANIFEST_001_20261101
created_at: 2026-11-01
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: SOURCE_READBACK_PASS / NUMPY_SCIPY_REPRO_PASS / INDEPENDENT_DENSITY_MATRIX_AND_ASSIGNMENT_PASS / ZIP_CRC_AND_SHA256_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_CANON / NO_EXEC / NO_NOVELTY / NO_REAL_DETECTOR_T1_MODEL / ORIGINAL_SINGLE_COPY_3Q_LOCC_GAP_OPEN
---

# PRF12 R24 — indeks pełnego raportu, kontraktów i sum kontrolnych

**Wynik:** R23 rectangle X/Y/Z weights (.18,.20,.62), Omega/gamma=10, Delta*gamma=.5, conservative pA>=.576 and pB<=.526, upgraded with finite Z-only QND detector wait gamma*t_d=.05, reset wait gamma*t_r=.05, independently calibrated symmetric label errors eta and a conditional Poisson bound on within-pair static-Xi persistence. Exact label contraction: (1-2eta)^2. Source-A shot-boundary-reset lower floor .31 has an analytic ALL-real-Xi proof; arbitrary within-shot jumps require fallback floor 0. For eta=.01 and lambda/gamma=.02, a>=.5536611975, b<=.5249704, 3277 pairs and K>=1768 guarantee both errors <.05; worst total gamma*T<=5991.3998. Conditional probability restrictions matter; independent or uncorrelated Xi across pairs are NOT assumed. The source detector is only QND dwell + ideal Z projector + classical assignment flips, not full hardware.

**Pełny raport naukowy:** siedem części GitHub. Po pełnym pobraniu i sklejeniu: EXACT **14,715-character content equality** z oryginalnym lokalnym dokumentem (wliczając końcowy LF).

- [Pełny raport R24, część 00](IW_PRF12_R24_FULL_PROOF_PART_00_001_20261101.md)
- [Pełny raport R24, część 01](IW_PRF12_R24_FULL_PROOF_PART_01_001_20261101.md)
- [Pełny raport R24, część 02](IW_PRF12_R24_FULL_PROOF_PART_02_001_20261101.md)
- [Pełny raport R24, część 03](IW_PRF12_R24_FULL_PROOF_PART_03_001_20261101.md)
- [Pełny raport R24, część 04](IW_PRF12_R24_FULL_PROOF_PART_04_001_20261101.md)
- [Pełny raport R24, część 05](IW_PRF12_R24_FULL_PROOF_PART_05_001_20261101.md)
- [Pełny raport R24, część 06](IW_PRF12_R24_FULL_PROOF_PART_06_001_20261101.md)

**Kod GitHub:** [R24 core standalone NumPy/SciPy](IW_PRF12_R24_GITHUB_CORE_REPRO_001_20261101.py). Rozszerzony jeden plik oraz niezależny audyt 2x2 / 4x4 są w ZIP.

**Pełny lokalny pakiet ZIP:** `PRF12_R24_reproducibility_bundle_20261101.zip`, 13,840 bytes. SHA-256: `eec873115e0460fee2a1d66cdb3cf60953cc0803354d15bdcabc2b9ad9c7250f`. Six members, CRC PASS, re-extracted member hashes PASS.

Member SHA-256:
- Full report: `5840a29347932051b0de71045c47c47187b6dd9e975a1fe6eb61046327117183`.
- Full main Python: `3455618c2e7b5c53038f14b6aa60dcd64b43a68575a70b17eb34a11415dcdb98`.
- Independent 2x2/4x4 audit: `d7d6ff394fe88616ab3722d35aca88eb089d0a09bb86ebc5386dc4e50bf0b87a`.
- Main log: `5edcf5b5e0cc4be9693a676877555c239d9a5fc41a733672aa90d5849d98e578`.
- Independent log: `3073edc7e0b17e07d458b9145142c73b85a3fe3c3174405522c34bec6a1861e7`.
- Machine-readable member-hash JSON inside archive.

**First owner:** PRF11 R35 / PRF12 R23. External mature references: IBM Quantum documentation for measurement assignment matrices; classical conditional Bernoulli stochastic domination and martingale concentration. There is NO hardware device measurement, no complete finite detector dynamics, no external referee readback, no BW ingestion verification, no physical source lifetime identification, no original three-qubit LOCC gap theorem. NO_CANON / NO_EXEC.


## PRF12 R25 continuation (2026-11-02) — calibration vs source-class identifiability

R25 strengthens R24's detector contract by adding **terminal-idle zero-temperature T1 amplitude damping** and **asymmetric assignment** eta_+=Pr(+->−), eta_−=Pr(−->+). For m=ideal pre-detector Z expectation, the recorded mean is c*m+d, c=exp(−Gamma1*t_d)*(1−eta_+−eta_−), d=(1−exp(−Gamma1*t_d))*(1−eta_+−eta_−)+(eta_−−eta_+). A two-shot **calibrated SCORE** Y=[1+((R1−d)(R2−d))/c²]/2 exactly recovers the R23 ideal pre-detector pair-correlation mean under independent detectors. Unlike R24's raw same-bit event, Y is generally **NOT Bernoulli**; one must use a bounded-increment martingale test, not R24's exact binomial tails. For eta_+=.01,eta_−=.03,Gamma1/gamma=.5,t_d gamma=.05, and conditional lambda/gamma=.02 with mid-shot source resets allowed, the conservative Hoeffding sufficient count is N=9516 (worst gamma*time 17398.28) versus N=11039 with conservative calibration uncertainties delta_c=delta_d=.0005. Independent 2x2/4x4/Kraus code and source-typed report: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-02/IW_PRF12_R25_REPRODUCIBILITY_AND_CUSTODY_MANIFEST_001_20261102.md .

**Independent material negative finding:** without a lower bound on the lifetime of static xi, the broadened source A_h redrawing independent Cauchy(0,gamma) frequency every h is EXACTLY stroboscopically indistinguishable from B Cauchy-Lévy for all controls AT cell boundaries; under deterministic bounded piecewise-constant noncommuting drive, their channels converge in diamond as O(h log(1/h)). A_h breaks R24's original within-pair-static A hypothesis, so this is a SOURCE-CLASS IDENTIFIABILITY BOUNDARY, not a logical contradiction of R23/R24 or original passive three-probe LOCC closure result. Full single-copy LOCC closure remains OPEN. Independent referee and BW ingest pending; NO_CANON / NO_EXEC / NO_NOVELTY.
