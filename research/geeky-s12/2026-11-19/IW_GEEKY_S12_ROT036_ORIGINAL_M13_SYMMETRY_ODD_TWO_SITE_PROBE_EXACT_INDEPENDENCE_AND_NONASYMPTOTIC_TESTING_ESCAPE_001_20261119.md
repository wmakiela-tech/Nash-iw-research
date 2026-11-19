---
artifact_id: IW_GEEKY_S12_ROT036_ORIGINAL_M13_SYMMETRY_ODD_TWO_SITE_PROBE_EXACT_INDEPENDENCE_AND_NONASYMPTOTIC_TESTING_ESCAPE_001_20261119
date: 2026-11-19
origin: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
exposure: PUBLIC
original_source: M13_PUBLIC_ORIGINAL_B_N41_GIT_BLOBS_BYTE_VERIFIED_AND_ACTUALLY_NATIVE_EXECUTED
science_status: AUTHOR_EXACT_RATIONAL_TWO_SITE_SYMMETRY_ODD_GAUSSIAN_INDEPENDENCE_AND_FINITE_SAMPLE_HYPOTHESIS_BOUNDS_PASS / SAME_CELL_SEPARATE_FULL_N41_CUBED_SPATIAL_FFT_PASS / DIFFERENT_CELL_I1_PENDING
prior_source: ROT034_EXACT_RANK5_COVARIANCE_TOMOGRAPHY_AND_ROT035_TWO_LEGAL_GAUSSIAN_MODELS_SHA_LOCKED
sync_status: GITHUB_PENDING_NATIVE_BW_INGEST
claim_ceiling: HYPOTHETICAL_TWO_RAW_SITE_SENSORS_AND_40M_INDEPENDENT_GAUSSIAN_NOISE_REPEATS / NOT_HISTORICAL_DTC0A / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT036 — one symmetry-odd two-site Gaussian probe provably independent of six M13 shell means, but sufficient to escape ROT035 finite-sample indistinguishability

## 0. Priority, actual original source and review status

M13 FIRST immutable public original N41 B Fourier/TT sparse 41-mode operator and FIVE fixed cubic observation masks k2..6. ORIGINAL M13 Python 8,970 bytes, Git blob SHA1 c6377cfbc9a0070abc34ffedc5871e719f6a4679; ORIGINAL B25 coefficients 7,501 bytes, Git blob SHA1 a6f50fbe5904e580e84c87ee87c5ad043cdec5d0. This rotation verifies both Git blobs byte-for-byte BEFORE source import and ACTUALLY imports UNMODIFIED M13, executes tensor_polys(41)[B] and all original five inner(k=2..6) plus native unmasked inner(k=0) at alpha=1/20, outward mpmath.iv.dps40, with strictly positive old and full source energy. This does not authenticate any historical independent hardware energy sensor or producer.
Original source:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py

Geeky ROT034 FIRST exact 5-parameter linear covariance tomography from the original six disjoint masks, with rank5 and 16 exact falsifying constraints, and demonstrated severe boundary near-singularity. Geeky ROT035 FIRST exhibited TWO explicit distinct *admissible EXACT rational Gaussian covariance site-noise models* A/B with SAME actual source mean and SAME KNOWN RAW global-calibration variance, full SIX aggregated mask observation KL<8.550e-18 and even ONE hypothetical raw SITE noise marginal KL>1e-6. Both prior complete original source-result JSON files are SHA256-locked as mathematical inputs. ROT034 and ROT035 different-cell independent I1 still NOT verified at this source inspection.
ROT035:
https://github.com/wmakiela-tech/Nash-iw-research/blob/cb1017143615b420eadef93e7a42eb332ba1df03/research/geeky-s12/2026-11-17/IW_GEEKY_S12_ROT035_EXACT_RATIONAL_M13_SIX_MASK_COVARIANCE_KL_INDISTINGUISHABILITY_AND_SITE_AGGREGATION_INFORMATION_LOSS_001_20261117.md

M15 ROT028 independently ORIGINAL-NATIVE M13 I1 reviewed prior Geeky ROT033 FACE12 unique source Fisher minimum, and M15 FIRST supplied its own baseline-recrossover source IV55. AUD3 ROT002 independently verified prior face integer graph and classical Schur identities but its separate full-source IV55 replay HOLD. Neither is a new I1 of ROT036.
M15 primary prior:
https://github.com/wmakiela-tech/Nash-iw-research/blob/6e6e3f272eb287ad6f6219a3b8e733202428108d/research/m15/2026-11-17/IW_M15_ROT028_ORIGINAL_M13_FACE12_SOURCE_I1_AND_NEW_FISHER_BASELINE_RECROSS_IV55_001_20261117.md

NEW ROT036 science target: Can we identify a SINGLE ADDITIONAL scalar from the originally defined site geometry which is mathematically independent of ALL six aggregated means under BOTH ROT035 source-admissible site-noise models, yet restores significant finite-sample statistical discrimination? The new result is NOT data processing from the existing six means; it explicitly posits an additional two-site readout that is NOT known to exist physically.

## 1. Exact original mask and group symmetry

The original periodic N41 lattice has 41³=68,921 sites. In the original region order outer + five fixed k2..6 cubic shells, the exact occupancy vector is (18268,7778,6938,6146,5402,24389). All six ORIGINAL masks are invariant under exchanging the first two lattice coordinates x,y.

Select precise original coordinates a=(9,19,20) and b=(19,9,20), exchanged by this coordinate permutation. Both lie in the SAME original region label5, the inner k6 cube; their periodic coordinate-distance vector is (10,10,0), so they are NOT sites joined by any single one-step axial6, face12, or body8 displacement.

The mathematical NEW observation is the signed RAW energy-density contrast

 **Z = E(a) − E(b).**

The original B tensor field is not assumed coordinate-permutation invariant; indeed the independent original-source FFT found its deterministic ENERGY means E_M13(a)−E_M13(b) generally NONZERO. The following exact independence is of the NOISE COVARIANCE and original mask averages, conditional on the original source fixed mean, NOT of the deterministic M13 signal itself.

ROT035 source-defined stationary site error is centered Gaussian with covariance beta0 I+beta_ax A_ax+beta_face A_face+beta_body A_body. The A matrices average the 6,12,8 single-step periodic shifts, respectively. ALL FOUR covariance generators commute with the lattice coordinate-swap permutation, and ALL original six region indicator vectors are invariant. The signed point contrast delta_a−delta_b is ANTI-invariant. Hence, algebraically for every original region j and EVERY beta in the allowed source covariance family,

 Cov(Z,mean_j) = (delta_a−delta_b)^T Sigma_site (indicator_j/w_j) = **0**.

The main source verifier additionally ACTUALLY checks exactly all SIX original region-neighborhood membership counts of a and b for each identity, axial, face, body type (all 6x4 differences ZERO), in addition to proving source permutation symmetry, and recomputes all THREE full original 6x6 integer E neighbor matrices to compare with source SHA-pinned ROT034. The independent random global sixth calibration noise is independent of RAW site noise and thus does not alter zero cross covariance.

**GAUSSIAN INDEPENDENCE**: Under BOTH ROT035 admissible model A and model B (indeed the whole declared isotropic Gaussian family), the signed raw-site error contrast Z is jointly Gaussian with the six aggregated region mean error readings, and their covariance vector is exactly zero. Thus Z is STATISTICALLY INDEPENDENT of all six original mean observations in both models. This conclusion does not follow from zero covariance for arbitrary non-Gaussian noise.

Original source sites a,b are not adjacent under ANY three one-step covariance operators; their Gaussian site-noise cross covariance is exactly ZERO. Hence

 Var_A(Z) = 2 beta0_A = **2**,
 Var_B(Z) = 2 beta0_B = **2*(99779719687217/100000000000000)**,

where the exact ratio q=beta0_B/beta0_A=99779719687217/100000000000000 differs from unity. BOTH models have exactly the same source M13 mean and identical raw independent calibration variance beta_cal=1/2500.

This yields a new independent factor of the seven-variate Gaussian law: **KL(six old means+Z) = KL(six old means) + KL(Z)**. The additional one-contrast marginal KL has the SAME exact lower as the ROT035 one-site KL, at least (1−q)^2/4 ≈**1.2130854049944e−6 >1e−6**, versus KL(old six) <8.550e−18. The extra information is NEW, not hidden inside a deterministic re-expression of six existing signals; any function of only the original six cannot beat ROT035 testing bound by data processing.

## 2. Same-snapshot-count nonasymptotic explicit testing theorem with unknown common source mean

Assume a mathematical experiment of **n=40,000,000** independent snapshots of the SAME FIXED M13 source field state, with Gaussian RAW SITE ENERGY noise independently redrawn at every snapshot, from either model A or B. This is a wholly SYNTHETIC hypothetical sampling experiment, NOT a proposed physical schedule.

Let Z_t be one differential site readout per snapshot. Its deterministic original source mean mu = E_M13(a)−E_M13(b) may be UNKNOWN and NONZERO, but is stable across samples under both hypotheses. Pair temporally consecutive independent samples and form Y_i=Z_(2i)−Z_(2i−1), i=1,...,m=n/2=20,000,000. This removes mu exactly and gives m independent centered Gaussian samples with raw variances:

 Var_A(Y_i)=4, Var_B(Y_i)=4q.

The hypothesis-discriminating likelihood-ratio statistic, with equal prior odds, is fully explicit and requires NO estimation of mu:
 log(p_A/p_B)=(m/2)log(q) + (sum_i Y_i²/8)*(1/q−1);
 decide A iff log(p_A/p_B)>0.

For two centered Gaussians with variance ratio q, the exact HELLINGER AFFINITY rho obeys

 rho^4 = 4q/(1+q)^2 = 1−z,
 z = (1−q)^2/(1+q)^2.

The original source EXACT rational verifier establishes **z>1/1000000** by exact rational cross multiplication, no numerical eigenvalue. Thus for m=20,000,000 independent paired differences,

 rho^m = (1−z)^(m/4) <= exp(−m*z/4) < exp(−5).

By the classical Bhattacharyya bound on optimal equal-prior binary Gaussian decision error,

 **P_error,Bayes < 0.5 exp(−5) ≈0.0033689735**,
 **P_correct,Bayes >1−0.5 exp(−5)=0.9966310265004573**, i.e. **>99.66310265%**.

This lower bound on optimal test success is a constructive binary testing claim; the explicit likelihood-ratio test above attains the Bayes optimum for the declared simple Gaussian hypotheses. Pairing cancels an UNKNOWN fixed source mean (but not arbitrary source drift).

At the IDENTICAL n=40,000,000 hypothetical independent snapshots, if one observes ONLY the previous SIX mean energy channels, the ROT035 EXACT rational upper KL remains. IID product KL plus Pinsker give for every possible equal-prior binary six-means-only decision rule:

 TV(P_A^n,P_B^n)<=sqrt(n KL_six_upper/2)<1.30762766e−5,
 **P_correct,six-only <0.500006538138288**, i.e. **<50.00065381383%**.

The enormous discrepancy concerns THESE TWO synthetic Gaussian source models and this single specified sample count. No empirical 40-million-readout technology, covariance, clock, temporal independence or site detector was demonstrated. If the source state varies across pairs or errors are correlated between snapshots, the proof requires modification.

## 3. Two different actual original-source algorithms

**Original source / exact geometry verifier**: source-lock unchanged M13 8970B Python and 7501B B25 Git SHA1 blobs, prior complete actual ROT034 and ROT035 original result JSON SHA256s, all BEFORE scientific import. ACTUALLY calls unchanged M13 tensor_polys(41), native inner(k2..6) and native full k0 at mpmath.iv40. Enumerates original full 41³ source cube regions, recomputes all three full E matrices, exact 6x4 equality of neighbor membership counts for a and b. Uses previous EXACT RATIONAL model fractions and constructs exact q,z, proof of contrast variance and independence and 40M Pinsker/Bhattacharyya binary experiment.

Original actual new script SHA256 **833a6daa8d0cc92ee96b25dca6ea83dd6c873aeecaf07aa4296b0740ccc6ce9f**; complete new exact result JSON SHA256 **ef6b0f5bfb8e3fed2472022b537dbba8c1ce54aeefd0c16cdf4ce3a22376553f**.

**Independently programmed full-source spatial verifier**: does NOT import primary exact-geometry script or any source integer E graph; builds six ORIGINAL full-site mask-indicator FFTs and a signed two-site delta FFT. Independently aggregates original 41³ site AXIAL/FACE/BODY spectral power and directly constructs each original full 7×7 noise covariance including independent outer calibration. For BOTH A/B the six cross covariance entries |Cov(Z,old_j)| are smaller than ~4.3e−20 in declared units, and Var(Z)=2 beta0 to binary64 precision. It independently imports ORIGINAL M13 helper and builds full original 41 complex 3×3 B Fourier tensor field in N41³ physical space by 3D inverse FFT, verifying original full k0 inner relative difference ~1.1e−16. The deterministic original B signal energy contrast at a,b is NONZERO (~1.2673e−13), confirming NO accidental assumption of source-field permutation symmetry. Independent scalar numerical KL of Z≈**1.2166571730115e−6**, above the strict rational lower.

Independently programmed spatial Python SHA256 **52bbfdff9ffc5a345f6b47de38519f10409ced1dbf8874760c4daa18225e04ea**, full spatial JSON SHA256 **3458a8415f754d4234b7183b0d2b0fd38f8656446000859c844db4963b4935**. Spatial checks are SAME-CELL numerical diagnostics, NOT an external different-cell I1 referee.

## 4. Source integrity and fully executed replay

Full USER self-contained executable archive:
 **Geeky_S12_ROT036_symmetry_odd_two_site_probe_finite_sample_escape.zip**,
 **47,570 bytes**, SHA256 **ea0b80241c89c22a70da654deb3fee178fb6dc36834c84dcc536615a47a2c319**.

16 archive entries, 15 manifest SHA256 payload files. ZIP CRC PASS; exact member byte readback 16/16 PASS; all 15/15 manifest SHA256 checks PASS. Archive contains BOTH ORIGINAL M13 source files, previous ROT034 and ROT035 exact science evidence and source scripts, new primary exact and separately programmed spatial Python, both complete result JSONs, actual clean replay/tamper controller and receipt, full README and SHA manifest. New replay receipt SHA256 **10c584af6601f2d5b125cc04db3d2b0fd38f8656446000859c844db4963b4935**.

ACTUALLY re-executed BOTH entire new science programs in separate fresh Python -I temporary directories with original frozen source bytes; BOTH resulting COMPLETE JSON files BYTE IDENTICAL: **2/2 PASS**. EIGHT separately mutated disposable source input files, original M13 Python, original B25, prior ROT034/ROT035 source result, new current primary result as applicable, all rejected with SOURCE_IDENTITY_MISMATCH BEFORE original M13 import: **8/8 FAIL CLOSED PASS**, source originals untouched.

Original runnable source code and complete exact rational results are IN THE USER ZIP. Public GitHub science report and curated machine JSON are separate publication events, NOT a false claim that executable Python bytes were mirrored into public GitHub.

## 5. Material limitations, prior firstness and different-cell reviewer

This is the public auxiliary M13 B N41 mathematical source only, NOT the unavailable exact complete historical dtc0a_runtime_v0_3_1.py. A real physical RAW pointwise energy detector pair, original simultaneous seventh observer, 40-million independent repeats, site-noise Gaussian distribution, calibration and common field state constancy have NOT been authenticated. This is NOT a conclusion about actual six-channel NASH observability or physical device improvements, and NOT a proof of global alpha source inversion. Prior field translations/free gain of local inverse work remain hypothetical and non-native original M13 inputs.

Classical cubic-group covariance symmetry, Gaussian independence and Hellinger/Bhattacharyya/Pinsker two-hypothesis bounds are mature methods, no general mathematical novelty claim. Original M13 FIRST. Geeky ROT034 FIRST exact source five-parameter covariance tomography. Geeky ROT035 FIRST exact rational near-indistinguishable covariance pair. NEW ROT036 FIRST within this source chain a source-mask odd two-site readout with exact Gaussian independence from SIX original means and strong finite-sample two-hypothesis testing advantage at the SAME snapshot budget. This is AUTHOR same-cell science, new different-cell M15/REC13/AUD3 I1 PENDING. KN15 native BW ingest and M15 owner CANON/EXEC_SIGN NOT verified. GitHub posting, Slack dispatch and same-cell Python replay are NOT different-cell scientific acceptance or source owner signing.

Bounded reviewer: independently original-source reconstruct mask coordinate-swap and x/y two-site positions, prove four basis generator covariance inner products zero for six original windows, verify variance 2 beta0 for both ROT035 rational models and unchanged raw sixth calibration, verify z>1e−6 exact rational and both 40-million-snapshot Pinsker/Bhattacharyya optimal accuracy inequalities; critically preserve source signal ≠ symmetric, unknown-stable-mean temporal pairing, and NO physical seventh sensor claim. Failure on any component should be documented as mathematical falsification, not a task cascade.

FINAL:
 ORIGINAL_M13_ORIGINAL_NATIVE_SOURCE_REEXECUTED_PASS /
 ORIGINAL_SOURCE_SIX_MASK_COORDINATE_PERMUTATION_EXACT_NOISE_INDEPENDENCE_PASS /
 TWO_NONADJACENT_SOURCE_SITE_PROBE_VARIANCE_2BETA0_AND_NEW_KL_LOWER_PASS /
 SAME_40M_HYPOTHETICAL_SNAPSHOT_N_BAYES_GREATER_99p663_PERCENT_VS_OLD_SIX_LESS_50p000654_PERCENT_PASS /
 DIFFERENT_OBSERVATION_ALGORITHM_FULL_41CUBED_SPATIAL_FFT_PASS /
 TWO_COMPLETE_BYTE_IDENTICAL_COLD_REPLAYS_AND_EIGHT_FAILCLOSED_SOURCE_ATTACKS_PASS /
 USER_ZIP_CRC_16OF16_BYTES_15OF15_SHA_PASS /
 ROT036_EXTERNAL_I1_PENDING / BW_PENDING /
 NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
