---
artifact_id: IW_M15_ROT004_GEOMETRIC_DECAY_AR1_ENVELOPE_SHARP_MINIMAX_001_20261113
return_id: IW_M15_ROT004_GEOMETRIC_DECAY_TEMPORAL_CORRELATION_ALL_ESTIMATOR_SHARP_MINIMAX_AND_LAG1_FAIL_001_20261113
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-13
exposure: PUBLIC
result_class: EXACT_CLASSICAL_CONDITIONAL_GAUSSIAN_MINIMAX / ANTI_REDISCOVERY / SOURCE_ADMISSION
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_NATIVE_SENSOR_TIMESERIES / NO_NASH_PHYSICAL_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE / NO_NEW_TASK_CASCADE
---

# M15 ROT004 — exact Gaussian minimax restoration of 1/m with geometric temporal covariance envelope

## 0. Material decision, source firstness, currentness

**Question:** M15 ROT003 allowed bounded but nondecaying temporal correlation |K_kl| <= kappa and obtained a sharp positive replication-error floor sigma²*kappa. Can we establish a SHARP ALL-ESTIMATOR robust finite-m risk when ALL-lag correlations instead decay geometrically, and determine whether knowing only the first lag suffices?

**Result:** For the separable Gaussian covariance contract below, m complete simultaneous four-channel groups, N=4m, and 0<=rho<1, if the UNKNOWN cross-group K obeys the FULL all-pairs bound |K_kl| <= rho^|k-l|, then

    R*(m,rho)=sigma²(1+rho)/[m(1-rho)+2rho].           (R4.1)

For every fixed rho<1, R*(m,rho) tends to 0 at rate 1/m, with asymptotic inflation (1+rho)/(1-rho) relative to the independent-group worst-case. In contrast, a lag-one-only bound allows an equicorrelated K and a nonzero floor. Thus the source-admission distinction is full lag DECAY, not a fitted single lag correlation coefficient.

**Prior and firstness**: M14 ROT031 first tetrahedral geometry; M14 ROT039 first independent-noise exact all-estimator four-axis Gaussian minimax (original public Git blob 80e678005d4a0edd0c6299d8b582e0199f464a8f); M14 ROT041 first independent-noise group-size co-time graph/minimax (blob 357d823e604fabfc86b9fc3573743aa126001250). M15 ROT001 source-to-temporal static negative; ROT002 unknown within-group covariance (sharp 4sigma²/N); ROT003 nondecaying cross-group correlation (sharp sigma²[kappa+(1-kappa)/m]), original https://github.com/wmakiela-tech/Nash-iw-research/blob/4c120405dbb66e769ab1cbd864b5eca70a82b9e7/research/m15/2026-11-12/iw_m15_rot003_separable_spatiotemporal_correlation_sharp_minimax_replication_floor_001.md . No reinterpretation of M14 original conditional results.

Empirical original source FIRST: Schall, Lindner, Rottstaedt et al., Laser-enhanced quantum sensing boosts sensitivity and dynamic range, Nature Communications 17 (2026), 10825, DOI https://doi.org/10.1038/s41467-026-78386-z . XH-S5 FIRST inventoried the original user-supplied Schall companion ZIP: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s5/2026-11-10/iw_xh_s5_eks1_t1_schall_original_source_data_zip_complete_inventory_temporal_no_003.md . That archive did not contain a true-time four-channel repeated noise record; no claim about all external possible source data. The authors' photon-shot-noise sensitivity is a calculated LIMIT, not achieved technical-noise measurement. This result is SYNTHETIC CLASSICAL MODEL, NOT detector reconstruction.

Closest mature established statistical hosts (none confer novelty): (a) NIST Engineering Statistics Handbook, Autocorrelation: https://itl.nist.gov/div898/handbook/eda/section3/eda35c.htm ; (b) Spatial Statistics lecture notes, GLS correlated constant mean and AR(1): https://zhouyuzhen.github.io/Spatial_Statistics_Lecture_Notes/intro.html ; (c) NIST Zhang 2008, Allan Variance of Time Series Models of Measurement Data: https://www.nist.gov/publications/allan-variance-time-series-models-measurement-data ; (d) Hermans et al. Estimation in AR(1) Models, https://documentserver.uhasselt.be/bitstream/1942/25871/1/Estimation%20in%20AR%281%29%20models.pdf , whose established AR(1) constant-mean GLS variance formula matches the scalar R4.1 host. No exhaustive novelty search and absolutely NO novelty claim.

## 1. Frozen mathematical observation contract

Four tetrahedral axes are a0=(1,1,1), a1=(1,-1,-1), a2=(-1,1,-1), a3=(-1,-1,1), with the 4x3 matrix A of these rows and Gram A^T A=4 I3, A^T 1_4=0, A A^T=4I4-1_4 1_4^T.

Unknown CONSTANT z in unrestricted R3. For m predeclared true-co-time four-channel complete groups, observe

    Y_k = A z + h_k 1_4 + eps_k, k=1..m, N=4m.

Every real h_k is unrestricted, deterministic and can vary independently across groups. Centered Gaussian eps has full SEPARABLE 4m covariance

    Cov(eps_ki,eps_lj) = sigma² K_kl C_ij,

where known sigma²>0 is every single-channel marginal error variance. Unknown spatial C=C^T PSD with diag C=1 (entire elliptope); unknown temporal K=K^T PSD with diag K=1 and FULL all-lag envelope

    |K_kl| <= rho^|k-l|, for k!=l, fixed known 0<=rho<1.     (1)

Singular C admitted; strictly positive approximation gives same supremum. No assumption of K=AR(1) is imposed: actual K may be ANY admissible PSD correlation. The AR(1) matrix is only a worst-case witness. Covariance must be separable; this is NOT a theorem for an arbitrary nonseparable block covariance. All estimators, biased and nonlinear, allowed; fixed schedule and m. No nonconstant z, heteroscedasticity, arbitrary new adaptive groups, unknown rho/axes/shot variance, or real optical Poisson model. Loss is total Euclidean vector squared error.

## 2. Attaining the uniform upper bound with nonnegative GLS weights

Set P=I4-11^T/4 and define per-session field contrast w_k=A^T Y_k/4; it annihilates h_k identically and E w_k=z. Let m=1 have weight a1=1. For m>=2 define

    d=m-(m-2)rho=m(1-rho)+2rho,
    a1=am=1/d,
    ak=(1-rho)/d for 2<=k<=m-1.                     (2)

All weights nonnegative and sum to one. Define z_hat=sum_k ak w_k. Its covariance and risk factorize:

    Cov(z_hat)=(sigma²/16)*(a^T K a)*A^T C A;
    R(z_hat;K,C)=sigma² (a^T K a) [1-(1_4^T C1_4)/16]. (3)

The second bracket is <=1 because C PSD. Critically, since EVERY ak>=0 and K_kl <= rho^|k-l| entrywise, for the AR(1) correlation matrix Qrho with entries Qrho_kl=rho^|k-l|,

    a^T K a <= a^T Qrho a.                             (4)

DO NOT infer K <= Qrho in PSD/Loewner order; only the weighted entrywise quadratic inequality is used.

For 0<=rho<1, Qrho is positive definite (m>=2) and its inverse is the well-known AR(1) tridiagonal precision matrix: endpoint diagonals 1/(1-rho²), inner diagonals (1+rho²)/(1-rho²), and immediate offdiagonals -rho/(1-rho²). Hence

    Qrho^-1 1 = (1/(1+rho))*(1,1-rho,...,1-rho,1)^T,
    1^T Qrho^-1 1 = d/(1+rho),
    a=Qrho^-1 1/(1^T Qrho^-1 1),
    a^T Qrho a = (1+rho)/d.                            (5)

m=1 separately yields a=1 and exact same closed formula R*=sigma².

Equations (3)-(5) give an attainable UNIFORM upper bound sigma²(1+rho)/d for EVERY unknown admissible K,C,z,h.

## 3. Matching lower bound for ALL estimators, including biased/nonlinear

Choose the legal least-favorable spatial correlation Cstar=(4/3)(I4-11^T/4), with diag Cstar=1, spatial offdiag -1/3, PSD rank 3; and temporal Kstar=Qrho. Both belong to the declared full nuisance classes and simultaneously attain equality above.

The complete raw observation Y_k is invertibly reconstructed from w_k=A^T Y_k/4 and s_k=1^T Y_k/4 via Y_k=A w_k+1_4 s_k. Under Cstar the spatial common mode is noise-free: s_k=h_k; restrict the legal submodel to h_k=0. Then all raw z-information is exactly in

    w_k=z+eta_k, Cov(vec eta)=(sigma²/3) Qrho tensor I3. (6)

A proper Gaussian prior z~N3(0,tau² I3) yields posterior vector covariance

    V_tau=[tau^-2+(3/sigma²)1^T Qrho^-1 1]^-1 I3
         =[tau^-2+3d/(sigma²(1+rho))]^-1 I3.          (7)

The Bayes integrated MSE of ANY estimator is at least tr(V_tau). Sending tau to infinity produces a global minimax lower sigma²(1+rho)/d. This matches the upper estimator. The argument uses a legal restricted Gaussian location experiment and a PROPER PRIOR LIMIT, not merely a Cramer-Rao or BLUE-only claim.

For strictly PD C, take C_eps=(1-eps)Cstar+eps I4 (0<eps<1), fix h=0, K=Qrho and let eps decrease to zero. The Gaussian location Bayes lower bound varies continuously and approaches the same value. The robust supremum is unchanged.

## 4. Exact countercontrols, finite sample and source-admission hinge

m=4, rho=1/2, sigma²=1:
- sharp robust R*=1/2, with endpoint-biased weights a=(1/3,1/6,1/6,1/3);
- ordinary uniform temporal mean under Qrho,Cstar produces 33/64=0.515625 (strictly worse);
- ROT003 WEAKER uniform all-pairs kappa=1/2 gave 5/8=0.625;
- rho=0 in the present contract gives sigma²/m=1/4 (ROT002). Original M14 independent CHANNELS also reduces factor 3/4 to 3/(4m)=3/16, different stronger assumptions.

m=100,rho=1/2: new sharp R*=1/34=0.02941176 sigma²; old ROT003 nondecaying kappa=1/2 permits R*=0.505 sigma². As m grows, the relative variance penalty compared to independently distributed worst-case groups tends to 3 at rho=1/2, but the absolute worst-case variance still tends to zero.

**FALSIFIER F4.1 — lag-one-only bound insufficient.** For m>=3 and any 0<rho<1, let K_lag1=(1-rho)I+rho 11^T. This is PSD with diag1; ALL adjacent lag-one correlations equal rho, yet lag-two correlation rho>rho², so the full geometric-envelope model is violated. The original ROT003 sharp risk under the wider lag-one-only class has nonzero sigma² rho floor as m grows. One measured lag-one correlation estimate (even precisely known) CANNOT silently be converted to an all-lag envelope.

**NEGATIVE CONTROL F4.2 — spatially common noise.** For C=11^T the contrast covariance A^T C A=0 and z_hat error is zero for every K (including a long-memory K), despite nonzero per-channel marginal sigma². The theorem is a WORST-CASE over C, not a claim that all correlated noises harm field reconstruction.

Boundary rho approaching 1: R* tends to sigma². At exactly rho=1, all-completely-correlated temporal K=11^T is allowed, and no replication gain can be guaranteed; the above inverse-matrix proof is for rho<1. Time-lag envelope rho<1 must be justified by source, not guessed.

## 5. Reproducer / evidential audit

Original exact stdlib Python Fraction reproducer genuinely executed locally on 2026-11-13: **305 counted assertion gates PASS** across m=1,2,3,4,5,7,10 and rho=0,1/5,1/2,3/4,9/10, complete rational Qrho inverse computed by independent generic Gauss-Jordan elimination, exact GLS weights/precision, full tetrahedral covariance Gram, independent vs perfectly common spatial noise controls, lag-one-only negative K controls, exact 33/64 versus 1/2 m4 comparison. These are 305 checked assertions, NOT 305 independent proofs; the analytic all-estimator lower proof is §3.

Exact original executed Python source local SHA256 34fc159332007b2e191793de90b965c7f2301bde879bd6573e681736b3896f1b, local Git blob cfbea9f8dbcfb14dcb8ad8414675270df1fb252f. Published GitHub original BYTE-IDENTICAL with full pinned readback PASS: commit 98353d1bd6fba040ad5e338770625d5707b5c570, blob cfbea9f8dbcfb14dcb8ad8414675270df1fb252f:
https://github.com/wmakiela-tech/Nash-iw-research/blob/98353d1bd6fba040ad5e338770625d5707b5c570/research/m15/2026-11-13/verify_m15_rot004_ar1_envelope_minimax.py

Actual locally executed deterministic machine JSON 10,621 bytes, SHA256 2957347306b2d5b85ee92ea2c34b6c4a44e176c5ae36febf59e84e594c314f29; LOCAL ONLY unless separately published. No independent REC11/AUD2 referee or native Schall time-series reanalysis has been performed.

Currentness separate inbound: 2026-11-13 ~13:42 CET #iw-dispatch tagged M15 in Geeky-S12 ROT013 original source B quartic coefficient interval robustness: https://github.com/wmakiela-tech/Nash-iw-research/blob/49fb59ee7c9aa5f967455c4a9969579fbd755fea/research/geeky-s12/2026-11-13/IW_GEEKY_S12_ROT013_SOURCE_B_QUARTIC_COEFFICIENT_ROBUST_PHASE_GATE_001_20261113.md . This original author computation states nearest result positive for eps<=1e-7 and full positive+negative witness for eps<=1e-8 within specified 25-dimensional independent coefficient box. M15 READ its original report, but this ROT004 does NOT rerun the BigInt certifier or APPROVE the theorem: REC11/AUD2 external referee pending, M13/Geeky firstness preserved, no BW authority assumed.

## 6. Stop, source admission, status

Without source-native verified same-sample synchronized four-channel repeated contrast measurements, an actual tested covariance or rigorously justified full lag decay mechanism, true-time grouping, known technical sigma² and validated separability, NONE of these formulae is a physical claim on Schall's original optical instrument. A Gaussian AR(1) fit is not a nonprobabilistic proof of a full upper bound; finite-sample uncertainty and provenance must be tracked separately.

REOPEN only after credible original time-lag source sufficient to validate a statistical full-envelope/risk model, or independently proven noise physical law; XH-S6 source ownership, KN13 BW event custody, M15 math only. No new tasks/cascade/EXEC.
Final: ROT004_EXACT_MATH_PASS / SOURCE_FIRST / REPRO_305_EXACT_GATES_PASS / GITHUB_SCRIPT_BYTE_EXACT_READBACK / GITHUB_PENDING_BW_INGEST / EXTERNAL_REFEREE_PENDING / NO_NOVELTY / NO_NASH_PHYSICAL_CLAIM / NO_CANON / NO_EXEC_SIGN.
