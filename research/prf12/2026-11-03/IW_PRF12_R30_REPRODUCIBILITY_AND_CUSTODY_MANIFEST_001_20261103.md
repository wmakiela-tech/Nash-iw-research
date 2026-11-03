---
artifact_id: IW_PRF12_R30_REPRODUCIBILITY_AND_CUSTODY_MANIFEST_001_20261103
created_at: 2026-11-03
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: FULL_REPORT_BYTE_IDENTICAL_GIT_READBACK_PASS / 7001_NODE_MPMATH_IV_PASS / ANALYTIC_SECOND_DERIVATIVE_PASS / CP_QUADRATIC_CORNER_AND_RESET_PASS / B_LINDBLAD_PASS / INDEPENDENT_2X2_4X4_AUDIT_PASS / ZIP_CRC_MEMBER_SHA256_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_FULL_12_ALPHABET_MINIMAX / NO_HARDWARE / NO_NOVELTY / NO_CANON / NO_EXEC / ORIGINAL_3Q_SINGLE_COPY_LOCC_CLOSURE_OPEN
---

# PRF12 R30 — exact source, reproducibility and claim ceiling

**[Full scientific report](IW_PRF12_R30_CP_QUADRATIC_AND_SECOND_DERIVATIVE_GLOBAL_CERTIFICATE_001_20261103.md)**. GitHub report is **byte-identical** with the original UTF-8 local report, verified by Git blob SHA-1 \`f53371e795cd85b97085aec1653210705893ee3d\` after complete readback. Full report original local SHA-256: \`e2759115d30ec608d0ab75c3c2009eb928783277280452a36ddf72b116aa895c\` (15669 bytes). Initial commit \`617d5418678e689b77e2a826b49d7bf940c3d898\`.

**[Short standalone GitHub reproducer](IW_PRF12_R30_SHORT_CP_SECOND_DERIVATIVE_BINOMIAL_REPRO_001_20261103.py)**: demonstrates CP nuisance rectangle, exact quadratic penalty, analytic reset floor, second-derivative interpolation penalty, N=1682 exact binomial tails and full-outcome e-factor algebra. This short mirror assumes the global phase-node and B-channel lower/upper results separately verified by the FULL Python code. Do not represent it as a fresh phase simulation.

**Full local executable + independent audit bundle:** \`PRF12_R30_reproducibility_bundle_20261103.zip\`, 17656 bytes. Archive SHA-256:
\`99d8c79e6ec64e372c087fadee847eb5bc4a9020e0569e146c08314b3b87d624\`.

Archive contains 6 members including a JSON checksum registry; full ZIP CRC \`testzip()\` PASS, extracted bytes for all members SHA-256 PASS. Members:

- Main full single-file Python \`IW_PRF12_R30_SECOND_DERIVATIVE_CP_CORNER_REPRO_001_20261103.py\`, SHA-256 \`6e816a3563369e7db39c69f8c7c76d73aae27888a435c465207247b98c350182\` (9636 bytes).
- Full report, SHA-256 \`e2759115d30ec608d0ab75c3c2009eb928783277280452a36ddf72b116aa895c\`.
- Independent 2x2 A-unitary + 4x4 B-Lindblad reproducibility audit \`IW_PRF12_R30_INDEPENDENT_UNITARY_AND_LINDBLAD_AUDIT_001_20261103.py\`, SHA-256 \`ea631fc6e382db3082b54a3d2d0ed62b94745f29ff91af313b2a04c27c699c82\` (3832 bytes).
- Main full-run JSON stdout \`IW_PRF12_R30_REPRO_STDOUT_001_20261103.json\`, SHA-256 \`abe4af484fd20b7656c3343742ac9107fd206a3de62e0d687606dc539012b053\`.
- Independent audit JSON stdout \`IW_PRF12_R30_INDEPENDENT_STDOUT_001_20261103.json\`, SHA-256 \`4eff2dcf54a12b1865f741df4e2468062b613a1d13e00819a0528105b860ebd9\`.
- Machine-readable member integrity registry \`IW_PRF12_R30_REPRO_MANIFEST_001_20261103.json\` SHA-256 \`8fc32ad219feadfd131915f269dac6c6e40d899f7ae0ccfbbcfda98174e7f256\`.

**Reproducible theorem:**
- synthetic reference calibration counts (46000,45540,69000,3705), CP success >=.99, source B independent Levy process, source A static within intact pair and arbitrarily dependent between pairs; no-reset survival hazard conditioned on CURRENT Xi, PRIVATE axis and other source-relevant latents, or an independent Poisson clock;
- same R28 source-active rectangular physical pulse with Omega/gamma=10, gamma*Delta=.5, R28 axes and signed-to-bit randomised score;
- all-real-Xi certification: 7001 mpmath.iv compact source-A nodes, exact four-corner CP quadratic correction, analytic Duhamel SECOND derivative interpolation O(h²), old R23/R28 far-detuning analytic tail lemma;
- conditional source-A P(Y=1)>=.30953728591436, source-B P(Y=1)<=.27066120169916;
- safe a=.3095,b=.2707: **1682** science pairs, decision A iff K>=488, conditional science error A=.03989654588613 and B=.03940977664157, plus <=.01 reference calibration failure. Original R28 2251: reduction by 569, 25.28%; same 115000 synthetic reference readings, total sensor readings 118364, modelled gamma wall clock 14575.2318;
- deterministic full 12-category e-factors from R29 with stronger margins: certified log-drift A>=.00425814627, B>=.00423169916 per pair, as opposed to R29 .00318882953/.00317983082. This does **NOT** imply a smaller expected stopping time in every experimental sequence.

**Validation:** independent 2x2/4x4 source A/B evolution at 9 Xi values, CP-corner quadratic bounds over a dense interior nuisance grid, source-B generator, reset-floor numeric search and exact binomial tails. No naive iid assumption for Xi.

**Scientific limitations:** stronger certificate is based on improved mathematical enclosure, **NOT** a new physical operation nor full optimisation over all twelve category-specific e-factors. Scalar SciPy beta quantile inversion is outward buffered and cross-checked via binomial tails, not fully formally directed-rounded; full quantum compact-grid calculation does use mpmath.iv with separate analytic interpolation. Device data and physical hardware confirmation absent. Independent scientific referee, BW ingestion, publication novelty and original single-copy 3-party unrestricted LOCC-closure result remain UNCONFIRMED/OPEN. NO_CANON / NO_EXEC.

External mature theory: [Safe testing, Grünwald–de Heide–Koolen, JRSS B 86 (2024)](https://doi.org/10.1093/jrsssb/qkae011); Duhamel and linear interpolation error are standard analysis; Clopper–Pearson exact binomial reference interval method is mature. No novelty/priority claim.

**R31 target:** full 12-category composite-null e-factor optimization with a rigorous all-real-Xi and calibration-rectangle constraint (not only 701-point LP) or time-uniform robust detector calibration from actual data. Do not interpret any design-only grid optimum as an all-Xi theorem.


## PRF12 R31 later owner uplift — 2026-11-03: N1666 and bounded 9-category certificate optimum

R30's all-real-Xi second-derivative, CP-corner calibration enclosure and certified fixed-N 1682 test remain VALID. PRF12 R31 retains identical finite source-ON rectangular quantum instrument, source A static Xi within intact two-shot pairs (arbitrary dependent Xi across pairs), source B independent Levy-Lindblad increments, CP SYNTHETIC 115000 reference readouts, and Xi-/axis-conditioned exogenous reset hazard. It changes ONLY the postmeasurement signed-quartet coin to rational probability triples:
  X(++,.943; mixed,0; --,1), Y(++,.907; mixed,0; --,1), Z(++,.347; mixed,0; --,.018).
A new independent 7001-node source-A interval/analytic tail and exact CP quadratic/reset-floor audit establishes p_A(Y=1)>=.3106993896688963, p_B(Y=1)<=.27161358975207756. With safe a=.31068,b=.27164, exact conditional non-iid binomial stochastic tails certify **N=1666, K>=485**, each science-error <.04, plus <=.01 CP calibration failure. Total single readouts 118332 and modeled gamma time 14545.9787, versus R30 N1682, reads 118364/time 14575.2318.

**Separate structural theorem:** exchangeability/swap closure of both composite one-pair null/alternative families permits exact 12→9 symmetrization WITHOUT worsening e-validity or maximin expected log evidence growth for any positive single-pair factor (not all adaptive histories). R31 constructs a **nine-support nonnegative multiplier interval DUAL** which shows upper <.039155288096258 on the optimum of the precisely DECOMPOSED conservative one-pair affine-score certification objective; rational score lower >=.039085799916819 is within 0.178% of THIS restricted optimum. This is NOT full multinomial/quantum minimax or global fixed-clock optimality. GitHub full science and reproducibility ZIP: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-03/IW_PRF12_R31_REPRODUCIBILITY_AND_CUSTODY_MANIFEST_001_20261103.md . R30 N1682 remains correct as a prior certificate; R31 N1666 supersedes it only for the specified source, weights, calibration, and postmeasurement score. No CANON/EXEC/novelty; original 3-qubit single-copy LOCC closure OPEN, referee/BW ingest PENDING.
