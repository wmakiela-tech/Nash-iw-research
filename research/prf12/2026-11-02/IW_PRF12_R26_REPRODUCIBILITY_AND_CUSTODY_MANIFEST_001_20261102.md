---
artifact_id: IW_PRF12_R26_REPRODUCIBILITY_AND_CUSTODY_MANIFEST_001_20261102
created_at: 2026-11-02
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: FULL_REPORT_BYTEWISE_GIT_READBACK_PASS / CP_EXACT_COVERAGE_CHECK_PASS / KRAUS_INDEPENDENT_PASS / ZIP_CRC_AND_SHA256_PASS / REFEREE_PENDING
claim_ceiling: NO_REAL_CALIBRATION_DATA / NO_GUARANTEE_OF_CONCLUSIVE_OUTPUT / NO_HARDWARE / NO_NOVELTY / NO_CANON / NO_EXEC / ORIGINAL_SINGLE_COPY_3Q_LOCC_CLOSURE_OPEN
---

# PRF12 R26 — scientific readback and reproducibility custody

**[Main scientific report](IW_PRF12_R26_FINITE_REFERENCE_CALIBRATION_AND_IDENTIFIABILITY_001_20261102.md)**. GitHub body blob verified against byte-identical local UTF-8 source, SHA-1:
\`690c993e1276450c74238f33411b1a2ad1c980cd\`.
Full report local SHA-256: \`8c6f50f23b9cc8c91d1d398c6d00660193b62faea4c58b774db82a4f0acb3042\`. Initial GitHub report commit: \`524bc6e3a6a51f027c3108ce607e7cbea847516c\`.

**[GitHub short runnable NumPy/SciPy code](IW_PRF12_R26_FINITE_CALIBRATION_CORE_REPRO_001_20261102.py)**, verified blob SHA-1: \`97d0695e2ec8800a565bd243a614b196758dc0fc\`. It demonstrates exact CP intervals, the finite-source comparison and structural microscopic nonidentifiability; it does NOT implement the full independent Kraus audit or synthetic grid optimization.

**Full local reproducibility archive:** \`PRF12_R26_reproducibility_bundle_20261102.zip\`, 14,053 bytes, SHA-256:
\`b9c32c2bcd2b8454fa0832cb3f8f7867c41ca6b30d25bd9d942bd7c7a02e11ad\`.
Archive has 6 members, ZIP \`testzip()\` CRC: PASS, extraction and bytewise SHA-256 check for EACH member: PASS.

Full archive members / SHA-256:
- \`IW_PRF12_R26_FINITE_REFERENCE_CALIBRATION_AND_IDENTIFIABILITY_001_20261102.md\` — \`8c6f50f23b9cc8c91d1d398c6d00660193b62faea4c58b774db82a4f0acb3042\`.
- \`IW_PRF12_R26_FINITE_CALIBRATION_AND_SHOT_ALLOCATION_REPRO_001_20261102.py\` — \`e3818a4dd76baa369ab312ef9d6cc3a7475c247246b3b8a00d9a21dd6da2536a\`.
- \`IW_PRF12_R26_INDEPENDENT_KRAUS_AND_BINOMIAL_AUDIT_001_20261102.py\` — \`0419d53016722b6166602e6e796aa1943d479763a15b7f4bd17ff0c3a26d4f1f\`.
- \`IW_PRF12_R26_REPRO_STDOUT_001_20261102.txt\` — \`5bdb850d7987ce84792c948b25f7ff8930359c05edd8d00cf26291a2d5faefb8\`.
- \`IW_PRF12_R26_INDEPENDENT_AUDIT_STDOUT_001_20261102.txt\` — \`1af1a31d59e180c7672cb24ff0d7ac479a7467ce127574be26e607d3caaa7d0d\`.
- \`IW_PRF12_R26_LOCAL_REPRO_MANIFEST_001_20261102.json\` — \`58349e2042203f20933aafccc799c8f6162200463203be487ac26421c4a5ea41\`.

**Executions:** 101 Kraus input m checks, CP exact binomial inversion (n=3,5,8,12, all k), small-n exact coverage, end-to-end two-error score and interval corner checks, plus a coarse calibration split/total-cost grid. Python 3 + scipy + numpy. No independent scientific referee attestation; independent NUMERICAL implementation is not a substitute for independent scientific review.

**Critical source typing:** All large-count calibration examples are SYNTHETIC counts derived from an explicitly declared nominal detector. They are not experimental measurements, do not by themselves imply the instrument has passed calibration, and do not guarantee a conclusive decision at any particular n0,n1. The actual fixed-size calibration data must yield a confidence interval excluding c=0 and a positive certified gap, or the protocol declares ABSTAIN. The familywise wrong-conclusion probability (≤.01+.04=.05) includes calibration failure for either source; it is not a guarantee about probability of conclusive output. Science source must satisfy the full R25 latent-Xi-conditioned hazard or independent Poisson reset clock. The fast-refresh Cauchy indistinguishability of R25 remains unchanged.

**First owners:** PRF11 R35, PRF12 R23–R25. **External mature foundations:** Clopper–Pearson 1934 DOI 10.1093/biomet/26.4.404; IBM Quantum assignment calibration, https://quantum.cloud.ibm.com/learning/en/courses/tools-for-quantum-advantage/error-mitigation . No CANON / EXEC; BW ingestion pending. Next R27: conditional *full-pair multinomial* likelihood with finite detector nuisance confidence sets, compare against corrected bounded score without falsely assuming iid hidden Xi.


## PRF12 R27 continuation and R26 conservative-score efficiency correction (2026-11-02)

R26's finite calibration of the affine detector c,d and its **non-Bernoulli debiased pair score** are mathematically valid under the original conditional source contract, but its Hoeffding shot cost of 49215 scientific pairs for the SYNTHETIC reference counts (46000,45540,69000,3705) is **not** an efficiency lower bound. R27 reconstructs the complete four-category recorded outcome likelihood conditional on each hidden Xi and the private X/Y/Z axis, then retains the RAW agreement indicator Z=1[R1=R2] rather than inverting c². With the same R26 99% Clopper–Pearson calibration confidence rectangle, the same full R23 source-active rectangular pulse physics, R25 Xi-conditioned exogenous source-reset hazard lambda/gamma=.02, an all-real-Xi mpmath.iv compact-enclosure plus analytic far-tail bound gives safe conditional pA(Z=1)>=.548 and pB(Z=1)<=.529. R27 then invokes exact **non-iid conditional Bernoulli binomial stochastic domination** (NOT a falsely assumed iid Xi) to certify 8497 scientific pairs, choose A if K>=4576, each test error <.04 and total wrong conclusion per source <.05 including <=.01 calibration error. Total shots shrink from R26's 213430 to 131994 with the SAME synthetic 115000 calibration reads. A pair of **composite-null e-processes** additionally supports optional stopping of the science sequence after fixed-n calibration, NOT adaptive stopping of CP reference calibration.

R27 does NOT prove that four-outcome multinomial data add no information: the signed marginal and axis may further improve robust tests, R28 open. Scalar Beta quantiles are SciPy outward buffered 1e-12 and checked with separate binomial tails, not full machine-certified interval inversion. Full theory, runnable interval code and SHA256 reproducibility package: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-02/IW_PRF12_R27_REPRODUCIBILITY_AND_CUSTODY_MANIFEST_001_20261102.md . Independent referee and BW ingest pending, NO_CANON / NO_EXEC / NO_NOVELTY / ORIGINAL_3Q_LOCC_CLOSURE_OPEN.
