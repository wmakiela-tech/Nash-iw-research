---
artifact_id: IW_PRF12_R27_REPRODUCIBILITY_AND_CUSTODY_MANIFEST_001_20261102
created_at: 2026-11-02
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: FULL_REPORT_BYTEWISE_GIT_READBACK_PASS / ALL_XI_IV_TAIL_PASS / CP_NUMERIC_OUTWARD_BUFFER_PASS / EXACT_NONIID_BINOMIAL_PASS / INDEPENDENT_2X2_4X4_PASS / ZIP_CRC_AND_SHA256_PASS / REFEREE_PENDING
claim_ceiling: NO_FULL_MULTINOMIAL_OPTIMALITY / NO_EMPIRICAL_DATA / NO_FULL_CP_ROUNDING_CERT / NO_CANON / NO_EXEC / NO_NOVELTY / ORIGINAL_SINGLE_COPY_3Q_LOCC_GAP_OPEN
---

# PRF12 R27 — full science source and reproducibility custody

**[Full scientific report R27](IW_PRF12_R27_FULL_QUARTET_RAW_PARITY_AND_ANYTIME_SOURCE_TEST_001_20261102.md)**.

Local exact report Git blob SHA-1 \`3bc3e571db0ef9147a90a9a2b45fd26c728e5b3d\`, confirmed by independent GitHub full fetch after initial report commit \`97068628969b9c332317018643f0f1e10dc91fb5\`.

**[Short GitHub runnable](IW_PRF12_R27_GITHUB_RAW_PARITY_AND_ANYTIME_CORE_001_20261102.py)** (SciPy): verifies CP rectangle, threshold 8497/4576 and anytime e-process one-step null inequality. It uses previously certified conditional source bounds, rather than reconstructing them.

**Full local archive** \`PRF12_R27_reproducibility_bundle_20261102.zip\`, size **15321 bytes**, SHA-256:
\`8efad16cbac30422cac1b983dfd19c96331abcebeea0ac04d98d2f2d1849fb15\`.
ZIP CRC \`testzip()\` PASS and full re-extracted bytewise SHA-256 comparison PASS for all five source members; separate JSON manifest member included.

Source members and SHA-256:
- report (16750 bytes): \`92938a5ff1a4c2eba6d7a9484de965a94dbba2455f394cb29e35d87cc759b46e\`.
- all-real-Xi mpmath.iv / NumPy / SciPy independent one-file executable (6322 bytes), \`IW_PRF12_R27_RAW_FOUR_OUTCOME_ROBUST_CALIBRATED_REPRO_001_20261102.py\`: \`76b9dab18a2fb8b5a190614370b87536a7b3ac0d275290d3259fa66b41f4642d\`.
- independent 2x2 A and 4x4 B + quartet/e-process test (2497 bytes): \`af135bfc1a787d359d941fb250395e4c45feedfa61c1840e256ef203b9b850ba\`.
- full main JSON stdout (1691 bytes): \`04994d5b61c9c475f241d201757b9df81cb4350b9194a6ca2397f368553e4f33\`.
- independent stdout (648 bytes): \`afa14fb6039b346d5ef02e0638a9a79e63df1aab71c58281ebfe43e34359f69d\`.

**Core reproduction:** same SYNTHETIC reference counts as R26: (46000,45540,69000,3705), 99% joint CP rectangles c∈[.932477929662,.939937817637], d∈[.039941802242,.047401690217]. The source-A mpmath.iv compact grid has 7001 nodes [-35,35]; independent global Lipschitz interpolation ≤.00378, analytic far-detuning tail for |Xi|≥35. Conservative A-noreset lower .5666143, B upper .5289569. Conditional exogenous hidden-Xi hazard lambda/gamma=.02 over L*gamma=1.7783 yields pA>=.5488516 including arbitrary mid-shot reset behavior, allowing safe pA>=.548, pB<=.529. Exact Bernoulli non-iid binomial-stochastic tails at N=8497,K>=4576: source-A false B ≤.03905443, source-B false A ≤.03989508. Cal failure at most .01 => per-hypothesis total wrong <=.05. This is NOT an iid claim for Xi.

**Arithmetic limitation:** true IV enclosure for quantum compact grid and large-detuning analytic control; numerical CP quantiles and final binomial tails via SciPy with outward 1e-12 beta buffers and independent SciPy binomial-tail checks. Scalar CP inversion is NOT fully certified with directed rounding across all special functions. External referee could provide that extra layer. No empirical device or input data; no claim full four-outcome minimax optimization.

**Additional scientific contribution:** sequential test supermartingales M^A and M^B permit optional stopping AFTER fixed-size calibration without loss of respective error bounds; do not claim optional-stopping-safe reference calibration. Previous R26 source and its R25 conditional hazard restrictions remain controlling. BW ingestion and independent referee pending. NO_CANON / NO_EXEC / NO_NOVELTY. Next R28: optimize robust signed-axis four-category statistic with proper composite nuisance constraints.


## Subsequent PRF12 R28 upgrade — signed-quartet randomized binary score (2026-11-02)

R27's full quartet law and carefully source-typed calibration/hazard assumptions remain controlling. R28 shows that the R27 RAW AGREEMENT bit (same sign, without distinguishing ++ from --) is not information-optimal for this particular calibrated source-control family. With the SAME finite source-active pulse hardware, weights (wX,wY,wZ)=(.18,.20,.62), SYNTHETIC reference counts (46000,45540,69000,3705), 99% fixed-N CP rectangle, Xi-conditioned survival hazard lambda/gamma=.02 and arbitrary Xi correlation BETWEEN pairs, R28 chooses an implementable additional private random bit Y after observing the signs: on (++), output 1 with probabilities (alphaX,alphaY,alphaZ)=(.94,.88,.36); on (--), with (betaX,betaY,betaZ)=(1,.96,.02); mixed outcomes always yield 0. This uses signs while producing a GENUINE binary Bernoulli result. An independent 7001-node mpmath.iv all-Xi compact enclosure plus analytic far-tail bound, all-CP-rectangle source-B estimate and four-corner mid-shot reset floor give conditional pA(Y=1)>=.30587825, pB(Y=1)<=.27186815. Safe a=.3055,b=.2720 and exact non-iid Bernoulli binomial domination permit **2251 science pairs, choose A iff K>=650**, with conditional test errors <.04 and total wrong-declaration bound <.05 including calibration-failure reserve .01. The same 115000 synthetic calibration reads now imply **119502 total sensor readouts**, versus R27 131994; gamma-time modeled 15615.5450 vs R27 27035.2226. A finite-grid 12-outcome LP only supplied candidate scoring coefficients; R28 does **NOT prove full 12-category global minimax optimality**. Independent matrix audit and ZIP SHA256: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-02/IW_PRF12_R28_REPRODUCIBILITY_AND_CUSTODY_MANIFEST_001_20261102.md . R25 Xi-conditioned hazard guard and fixed-size CP data remain REQUIRED; no empirical hardware, no CANON/EXEC/novelty, no single-copy 3Q LOCC closure claim. Independent referee and BW ingest pending.
