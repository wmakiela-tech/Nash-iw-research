---
artifact_id: IW_PRF12_R32_REPRODUCIBILITY_AND_CUSTODY_MANIFEST_001_20261108
created_at: 2026-11-08
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
exposure: PUBLIC
sync_state: GITHUB_READBACK_PENDING / BW_INGEST_PENDING
status: ALL_XI_7001_INTERVAL_PASS / EXACT_INTEGER_BETA_ENDPOINTS_PASS / EXACT_INTEGER_BINOMIAL_TAILS_PASS / INDEPENDENT_2X2_4X4_PASS / FRESH_ZIP_REPLAY_PASS / REFEREE_PENDING
claim_ceiling: NO_CANON / NO_EXEC / NO_NOVELTY / NO_HARDWARE / ORIGINAL_SINGLE_COPY_THREE_QUBIT_LOCC_CLOSURE_OPEN
---

# PRF12 R32 — source and reproducibility manifest

**Primary full scientific report:** [R32 complete proof](IW_PRF12_R32_ANYTIME_REFERENCE_CS_COUPLED_DETECTOR_GLOBAL_XI_001_20261108.md). Exact GitHub report blob SHA-1: 0b68cbc315ddda342a03a8fd4916df7e1dacc43d; matches the complete local original, 20,497 UTF-8 bytes; source SHA-256: 6e3a1e314bebebb8110cac7d49e81951889b10618fcb8136b85540e82e338b48. Initial commit: 8ee97c3f60a40198bd8b9aee8298307a1c5eb7c9.

**[Compact executable GitHub core](IW_PRF12_R32_GITHUB_COMPACT_EXACT_INTEGER_AND_ANYTIME_CS_REPRO_001_20261108.py)**: independent pure-integer validity checks for four Beta-mixture confidence-sequence endpoints and exact rational binomial tails. It deliberately does not rerun the full all-real-Xi quantum calculations.

**Full conversation artifact:** PRF12_R32_reproducibility_bundle_20261108.zip; **21,393 bytes**, SHA-256 **a02886dbce14542439e59e47d80d72ae405306d4be436df082a48f7180e4e1b3**. Contains 11 members, ZIP CRC PASS, re-extracted bytewise SHA-256 of all members PASS. Inside the ZIP, IW_PRF12_R32_LOCAL_REPRO_MANIFEST_001_20261108.json enumerates every file with its exact SHA-256 and bytes.

Key archived member hashes:
- Full standalone all-Xi NumPy/SciPy/mpmath.iv Python: dbe8737b3bdd73fcdd2d64d5b95995a712f1beb117bd7d86a0322dd323ebd1d5.
- Rational integer Beta-mixture endpoint verifier: 673d28190edb1c461d3e2a5a8deba82036f01a01d6c04e0b3e08c710a2804800.
- Rational integer binomial-tail verifier: d2cb85fdd7bf8197eac74914eada222ec6203098893541d88bb8dadc7da5e81b.
- Independent 2x2 static-A unitary / 4x4 source-B Lindblad matrix audit: 0737eab39d32bd1319588c6d353b61fadcc0098a0585b1f66113a7fe5d1b7459.
- Two complete full-run JSON files, exact endpoint/binomial logs and independent matrix log are included and hashed by the internal JSON registry.

**Clean ZIP extraction replay:** all two full 7001-node source-A mpmath.iv programs and 120-term source-B Lindblad runs exactly reproduce the archived JSON output, including N=1725, decision K>=502 (uniform Beta mixtures), and N=1670,K>=486 (Beta shapes chosen IN ADVANCE). Exact integer witnesses independently confirm 99% joint anytime calibration coverage and both exact science binomial errors <.04. Separate 2x2/4x4 quantum audit agrees with the Bloch source at 12 Xi fixtures to max 1.11e-15. Tested NumPy/SciPy/mpmath dependencies.

**Mathematical result and source contract:** time-uniform Beta–Bernoulli mixture confidence sequences allow adaptive allocation, inspection and stopping of BOTH reference streams with at most .01 total loss of confidence for stationary conditionally Bernoulli detector probabilities p0,p1. Source-state m has detector mean u=(1+m)p0+(1−m)p1−1: c=p0−p1 and d=p0+p1−1 are COUPLED, not independently selectable. Exact quadratic reference interpolation and reset-floor calculus, global Xi 7001-node interval plus analytic tails, and all-source-B p0,p1 corners yield:
- Uniform prior, synthetic references: P_A>=.31025956350447254, P_B<=.2718432247428817; safe a=.31022,b=.27188; N=1725, K>=502.
- Prespecified Beta(9900,100) and Beta(540,9460), SAME synthetic references: P_A>=.3105770618514484, P_B<=.2715349916038667; safe a=.31054,b=.27157; N=1670, K>=486.
- In each case the conditional science error <=.04, plus <=.01 reference calibration failure => familywise wrong-declaration probability <=.05 per source.

**Invariants and negative knowledge:** all numbers from SYNTHETIC reference counts (46000,45540,69000,3705), not device data. Calibration prior parameters must be fixed before observing CURRENT reference data; no post-selection of Beta shapes. Detector must remain stationary, reference shots conditionally Bernoulli, source-A Xi fixed within intact pairs, source-B independent increments during source-on pulses, reset survival conditioned on current hidden Xi/private axis and other hazard variables, private randomization and detector errors conditionally independent. Drift, adversarial latent Xi targeting, incorrectly repeated fixed-time CP intervals and unrestricted 12-category optimality NOT certified. Original passive three-probe single-copy asymptotic LOCC closure remains OPEN. External independent referee, BW ingestion and hardware verification pending. NO_CANON / NO_EXEC / NO_NOVELTY.


## PRF12 R33 — separate nonstationary-detector successor, 2026-11-08

R32's Beta-mixture confidence sequences remain CORRECT **only for stationary reference probabilities** p0,p1 and are NOT reinterpreted as drift-valid. PRF12 R33 explicitly permits time-varying p0(t),p1(t), but ONLY with an exogenous PATHWISE Lipschitz rate nu_i and conditionally Bernoulli, predictable, nonanticipative reference sampling. R33 applies conditional martingale Hoeffding bounds for the average of **changing conditional reference means**, with alpha_cal=.01 spent by epoch index 1/[j(j+1)]: the number of COMPLETED predeclared-size reference epochs can be adaptively selected; **not** unrestricted within-epoch reference stopping. A new source-type perturbation theorem derives exact signed-quartet sensitivity S=.59514, transferring R31's all-real-Xi source bounds A0=.3106993896688963 and B0=.27161358975207756 at a VALID comparator detector to each time-varying detector with deviations delta: pA>=A0-2S delta, pB<=B0+2S delta. Positive certified gap if delta<.0164187418.

R33 provides one **SYNTHETIC** physically ordered two-epoch reference/science schedule, with nu_i=1e-8 per gamma time ASSUMED, not inferred: each epoch 46000+69000 reference shots interleaved and 4750 science pairs; delta_max=.00934218415, safe a=.2995,b=.2828, 9500 source pairs K>=2765, independent exact INTEGER binomial error A<=.03497646 and B<=.03826513, plus global reference failure <=.01. Total reads 249000, wall gamma*T=40369.0260 — the drift-validity gain is EXPENSIVE, and R32's stationary cost is not directly comparable. An explicit new NO-GO shows unrestricted detector drift can set p0=p1=.5 during science, making all A/B recorded quartet laws EXACTLY equal despite arbitrarily good earlier reference calibrations. Hence calibration observations alone cannot supply an omitted drift-rate contract. R33 report and complete CRC/SHA256 ZIP, with included **clean-replayed original R31 full all-Xi Python**, are indexed at: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-08/IW_PRF12_R33_REPRODUCIBILITY_AND_CUSTODY_MANIFEST_001_20261108.md . R32 remains controlling for a STATIONARY detector; independent scientific referee and BW ingest pending. NO_CANON / NO_EXEC / NO_NOVELTY / ORIGINAL_3Q_LOCC_CLOSURE_OPEN.
