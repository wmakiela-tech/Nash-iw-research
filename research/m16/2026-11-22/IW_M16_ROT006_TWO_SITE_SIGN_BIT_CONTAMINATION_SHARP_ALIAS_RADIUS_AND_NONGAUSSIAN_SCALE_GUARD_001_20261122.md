---
artifact_id: IW_M16_ROT006_TWO_SITE_SIGN_BIT_CONTAMINATION_SHARP_ALIAS_RADIUS_AND_NONGAUSSIAN_SCALE_GUARD_001_20261122
return_id: IW_M16_ROT006_TWO_SITE_SIGN_BERNOULLI_ADAPTIVE_FAULT_SHARP_PHASE_BOUNDARY_AND_NON_GAUSSIAN_VOLATILITY_SURVIVAL_001_20261122
origin: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_11 / M16
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
result_class: SOURCE_CONDITIONAL_BERNOULLI_ADVERSARIAL_CONDITIONAL_BIT_FAULT_SHARP_ALIAS_AND_ROBUST_FINITE_N
scientific_status: ANALYTIC_MINIMAX_IDENTIFIABILITY_PHASE_PASS / MPMATH100_DIRECT_SOURCE_EXEC / IV80_6_NEIGHBORING_GATES_PASS / NONGAUSSIAN_200K_SIGN_COUPLING_PASS
sync_state: PUBLIC_GITHUB_SOURCE_ONLY_BW_NATIVE_UNVERIFIED
claim_ceiling: NO_NEW_GENERAL_MATHEMATICAL_THEOREM / NO_HISTORICAL_DTC0A_RUNTIME / NO_REAL_SIGNED_SITE_SENSOR / NO_PHYSICAL_NASH_INFERENCE / NO_CANON / NO_EXEC_SIGN / NO_UNASSIGNED_TASK_CASCADE
---

# M16 ROT006 — sharp adversarial sign-bit fault identifiability boundary and scale-mixture survival

## 0. Relevance, actual sources reopened, source firstness

This turn audits M16 ROT005's largest genuine measurement vulnerability: the instrument must supply TWO signed, CENTERED latent Gaussian site values, not only nonnegative squared energy. Even if every positive per-channel multiplicative gain cancels in a sign test, sign decision errors, offsets, and nonGaussian site volatility are unmodeled.

The following original sources were DIRECTLY READ this rotation:
1. **M16 ROT005** full original report Git blob 7b1d0057a9fdcbe44831011574eb8999986a86aa and full public exact code blob 685b92909a5133f3725976438c020127a9d40077. Its FIRST result was the two-site sign-concordance Gaussian orthant law for new B versus Bpi and unbounded adaptive positive gain invariance; its two conservative sufficient n were 591093/908653.
2. **Geeky-S13 ROT013** full source Git blob 41e98d801152e0a47c491107767406537e4cf335 (pinned commit c7da358f2620e45fdc860ce86428c97d0ca80688). FIRST its exhaustive 104-class one-RAW-site information audit and original ROT038 **A/B** pair two adjacent raw Gaussian-value Hellinger bound n957177. Do NOT merge with this distinct **B/Bpi sign-ONLY** comparison.
3. Underlying **Geeky-S12 ROT038** FIRST synthetic anisotropic site covariance A and B, blob 28576dbb0649c1f0fbd4d926896813eac946e6d8. M16 ROT004 FIRST hypothesis Bpi as exactly axis-permuted source B; M13 FIRST original spatial N41 geometry.

Relevant mature prior art, background rather than source claims:
- Chen, Gao, Ren, *A General Decision Theory for Huber's epsilon-Contamination Model* (2015), https://arxiv.org/abs/1511.04144 .
- Vallinayagam, Pensia, Jog, *On the Sample Complexity of Robust Binary Hypothesis Testing* (May 2026), https://arxiv.org/abs/2605.24741 . This compares Huber/additive, subtractive and TV contamination and their adaptive variants. **The present sign-flip channel is a specifically defined transition kernel and is not silently identified with Huber's mixture family.**
- Normal scale-mixture and elliptical sign/orthant invariance are well-established (e.g. https://www.mdpi.com/2227-9091/8/4/103 and https://pmc.ncbi.nlm.nih.gov/articles/PMC7839949/). No first-principles general novelty claimed.

## 1. Full source-conditional contract

N41 original 68921-site periodic geometry; two source-hypothesis centered Gaussian site-noise laws from ROT038 B and M16 ROT004 Bpi. Both are SPD (eigenvalues >=7/10), beta0=1. An ideal pair of adjacent x-axis signed site values has within-snapshot Pearson correlations

 rho_B = (beta_x(B)/2) = 1/40;
 rho_Bpi = (beta_x(Bpi)/2) = 3/200.

The signed **pair-concordance bit** is Y_j=1{G_0,j G_1,j>0}, for IID source Gaussian cores G_j under hypothesis X. Under BOTH models, a single scalar signed site marginal is identical N(0,1); only their correlation differs. The classical bivariate Gaussian orthant identity gives exactly

 p_B = P_B(Y=1)=1/2+arcsin(1/40)/pi
     = 0.5079585763198139302157494652822360366448652271231280...
 p_Bpi = P_Bpi(Y=1)=1/2+arcsin(3/200)/pi
       = 0.5047748273601990095203394247002263392926825108451649...
 Dp=p_B-p_Bpi
    =0.00318374895961492069541004058200969735218271627796309...>0.

ANY positive, separately and arbitrarily gain-controlled readings g0_j G0_j and g1_j G1_j, even with gains depending on latent observations, the true model, entire shot and all preceding shots, yield the SAME Y_j pathwise. The Gaussian core IID across snapshots makes the clean Y_j IID in the exact source model.

**New sign-bit fault model**: after sign extraction, observe tildeY_j=Y_j XOR F_j. F_j may depend on Y_j, latent current noise, hypothesis, previous observations, arbitrary extra randomness and earlier faults. Let H_(j-1) be the entire prior history; for EACH shot j and each hypothesis X require the predictive per-shot guarantee

  P_X(F_j=1 | H_(j-1)) <= eta a.s.

This is NOT a deterministic maximum number of flips in n shots, NOT a bound on aggregate fraction only, NOT arbitrary analog additive error, and NOT a symmetric common binary channel. The conditional formulation matters because it yields a finite-n martingale concentration guarantee. The adversary can be model-specific and deliberately flip opposite bit values in the two hypotheses.

Define inf over all randomized tests using tildeY_1...tildeY_n of the maximum of the two worst-case conditional errors over this exactly bounded fault class, denoted R_n^sign(eta).

## 2. Exact, SHARP uniform-identifiability phase boundary

**Theorem.** Let eta_star=Dp/2:

  eta_star =
     [arcsin(1/40)-arcsin(3/200)]/(2*pi)
   = 0.00159187447980746034770502029100484867609135813898154653294816...
   = 0.15918744798074603477... PERCENT of PAIR-CONCORDANCE bit readings.

(i) For eta>=eta_star, R_n^sign(eta)=1/2 for ALL finite n. The hypotheses can be made ENTIRELY observationally identical, not merely asymptotically close.

**Constructive proof.** Let pbar=(p_B+p_Bpi)/2. Under B, flip ONLY clean ones Y=1 to zero with conditional probability a=eta_star/p_B; leave clean zero intact. Under Bpi, flip ONLY clean zeros Y=0 to one with conditional probability b=eta_star/(1-p_Bpi); leave clean one intact. The per-shot unconditional and history-conditional probabilities of a flip are exactly p_B*a=eta_star under B and (1-p_Bpi)*b=eta_star under Bpi. Such kernel probabilities are strictly <1; use independent randomization across j. The resulting observed sequences are IID Bernoulli(pbar) under BOTH hypotheses, hence exactly identical laws. Every test has maximum conditional error >=1/2 for this legal pair of faults; a fair coin attains 1/2. QED.

Numerical checked alias-kernel conditional rates:
 a = 0.0031338667246070988941... when B clean bit is one;
 b = 0.0032144458071910260984... when Bpi clean bit is zero.

**Nuance:** the threshold is the supremum over HYPOTHESIS-DEPENDENT, bit-VALUE-TARGETED faults. At eta_star only ~0.159% of outputs change on average under each hypothesis, not 0.159% of each raw channel's independent sign. Two simultaneous raw sign errors can cancel in the pair-concordance bit.

(ii) For 0<=eta<eta_star the hypotheses are uniformly asymptotically identifiable, even under HISTORY-ADAPTIVE conditional faults. Define the midpoint

  t=(p_B+p_Bpi)/2

and the classifier "declare B iff (1/n)sum_j tildeY_j>t". Every admissible fault mechanism obeys

  E_B[tildeY_j | H_(j-1)] >= p_B-eta = t+(eta_star-eta);
  E_Bpi[tildeY_j | H_(j-1)] <= p_Bpi+eta = t-(eta_star-eta).

Indeed clean Y_j is independent of past, and
 |E[tildeY_j-Y_j |past]| <= P(F_j=1|past) <=eta.
With bounded observed bits, the conditional Hoeffding exponential-moment lemma gives for both tails

  sup_X,legalFaults P_X(error)
       <= exp[-2n(eta_star-eta)^2]
       = exp[-n(Dp-2eta)^2/2].

The proof uses a super/submartingale exponential bound and does NOT assume tildeY_j IID under arbitrary adaptive faults. For every eta<eta_star this tends to zero exponentially. QED.

Hence eta_star is the exact boundary for uniform *asymptotic* identifiability and exact no-information minimax risk at and beyond it. The displayed exponent is a **CONSERVATIVE SUFFICIENT finite-n guarantee for the midpoint test**, not the globally minimax risk or its exact sample threshold below eta_star.

## 3. Reproducible conservative resource consequence

Sufficient n for each hypothesis with strict error <alpha is any natural integer satisfying

 n > log(1/alpha) / [2(eta_star-eta)^2] 
   = 2 log(1/alpha) / (Dp-2eta)^2.

Actual 100-digit mpmath eval of exact rational/arcsine source and strict neighboring-integer inequalities:

| Allowed worst-case conditional bit-flip probability eta | sufficient n error<5% | sufficient n error<1% |
|---:|---:|---:|
| 0 | 591093 | 908653 |
| 0.0001 (0.01%) | 672990 | 1034550 |
| 0.0005 (0.05%) | 1256399 | 1931392 |
| 0.0010 (0.10%) | 4275765 | 6572892 |
| 0.0015 (0.15%) | 177452948 | 272788403 |
| eta>=eta_star | **UNIFORM IDENTIFIABILITY IMPOSSIBLE** | **UNIFORM IDENTIFIABILITY IMPOSSIBLE** |

These huge counts describe PAIRS of hypothetical signed centered site readings across IID Gaussian-core snapshots, not full N41³ raw-site data costs, sensor execution, or real NASH physics.

A second 80-decimal *directed mpmath.iv interval* check used exact identity asin(x)=atan2(x,sqrt(1-x^2)) for positive x and verified strict neighboring-integer thresholds at eta=0, 0.0010, 0.0015 for BOTH alpha. Other rows have 100-digit high-precision neighboring checks but were not independently directed-interval replayed. The eta_star source interval was explicitly outward-bounded:

 [0.001591874479807460347705020291004848676091358138981546532948163854057932823515153115551,
  0.001591874479807460347705020291004848676091358138981546532948163854057932823515154169771].

## 4. Falsifier of an overly broad engineering interpretation: common BSC vs adversarial bit corruption

If the sign bit is instead passed through the SAME hypothesis-BLIND independent symmetric binary channel with bit-flip probability q under BOTH B and Bpi, then exactly

 p'_X = q+(1-2q)p_X,
 p'_B-p'_Bpi=(1-2q)Dp.

For EVERY q<1/2 the pair remains statistically identifiable; the adverse eta_star=.1592% phase transition DOES NOT APPLY to this strictly narrower shared symmetric mechanism. A known fixed q yields the conservative midpoint Hoeffding numbers:

| q shared symmetric bit channel | sufficient n >95% | sufficient n >99% |
|---:|---:|---:|
| 0 | 591093 | 908653 |
| 0.01 | 615465 | 946120 |
| 0.10 | 923582 | 1419771 |
| 0.49 | 1477730954 | 2271632412 |

Only q=1/2 gives the fully erased Bernoulli bit in this class. These are not strict rates for an unknown hypothesis-specific physical error law. **Therefore eta_star is NOT a universal required detector bit accuracy:** it is a no-go boundary under a worst-case very wide fault model. A valid instrument statement needs the actual error TRANSITION KERNEL and its time dependence.

## 5. Survival under nonGaussian positive shared volatility (not arbitrary nonGaussianity)

Let independently sampled across time Gaussian cores G_j have precisely original B/Bpi 2x2 correlation. Define observed two readings

  X_0,j = sqrt(S_j)*g_0,j*G_0,j,
  X_1,j = sqrt(S_j)*g_1,j*G_1,j,

with S_j>0 a.s. (possibly fluctuating nonGaussian shared scale) and separate positive g_ij arbitrarily dependent on current latent and historical variables. Then, EXACTLY PATHWISE,

  1{X_0,j X_1,j>0} =1{G_0,j G_1,j>0}

for EVERY realization. Even if S_j is time-adaptive or correlated across j, clean sign bits remain IID as long as Gaussian **CORE pairs** G_j are IID. The robust sign theorem and eta bounds survive this declared class. The whole X field can be nonGaussian and exhibit common-volatility fourth-moment dependence.

**Specific source-aligned independent nonGaussian control:** take IID S_j with P(S=1/2)=P(S=3/2)=1/2 and independent G_j; E[S]=1, E[S²]=5/4. Cov(X0,X1)=Cov(G0,G1)=rho is UNCHANGED, but
  Cov(X0²,X1²)=E[S²]*(1+2rho²)-1 =1/4+(5/2)rho²
rather than Gaussian 2rho². Thus the site noise is genuinely nonGaussian with shared volatility while sign probabilities remain EXACTLY those of ROT005. This is a mathematical controlled class, not a claim of measured astrophysical volatility or physical noise tails. Source Geeky-S12 ROT038 already FIRST used the same two-point global S=1/2,3/2 scale-mixture to falsify Gaussian independence of old linear mask probes; current sign-survival is a DIFFERENT application and firstness is not appropriated.

What is NOT implied: robustness to arbitrary nonGaussian noise having only the same covariance (there exist radically different sign copulas), unknown nonzero means or offsets before sign, zero or negative gain, clipping, time-correlated Gaussian cores, or arbitrary analog additive perturbations. An analog readout error must first be *proven* to imply a bound on the PAIR BIT FLIP, before applying this theorem.

## 6. Actual calculations and provenance limits

New expanded local actually executed source:
  m16_rot006_sign_bit_fault_radius.py
  Python script SHA256: 4895187fc0983eb18100f2f67db7c6d92a88a7d11c10d974bc945326fb1f5022.
  Full result JSON SHA256: c7397685eee2dd0800a29bcbda6672e76575df2da7b83524b03cc462bbf528ff.

Execution: exact source Fractions for correlations; 100-digit mpmath arcsines and strict 10 neighboring-threshold checks; explicit two hypothesis-wise alias kernels; 200000 actual synthetic bivariate Gaussian draws with independent 2-point positive scale-mixture and separately adapted gains all pair signs unchanged exactly; 80-digit outward-directed IV bracket for eta_star and SIX neighboring gates. The actual calculations were run in the session's local Python runtime, and both expanded script/JSON kept as LOCAL data artifacts. This does not claim a physical test or that the shorter public GitHub code was itself cold rerun after upload.

Public reproducible compact code at:
  research/m16/2026-11-22/code/m16_rot006_sign_bit_fault_radius.py
  Git commit 2316a673758cb8f88c169b45519cc288fc2d2ad3.

The short public file contains the same exact source formulas, legal alias tests, the full count table and additional IV80 guards; its Git blob is a DISTINCT representation from the locally executed expanded 100-digit script and is NOT assigned its local SHA256. We require a post-upload actual GitHub fetch before claiming GitHub full readback.

## 7. Decision / scientific stop

**Earned within declared synthetic host:** a SHARP fault radius for the Bernoulli sign experiment under model-specific value-targeted bit corruption; exponential finite-n Hoeffding survival under adaptive conditional contamination below threshold; positive per-channel gain and arbitrary positive shared-volatility robustness given IID Gaussian cores; strict different interpretation for a shared BSC. Source-specific contribution, classical statistics methods, not new general mathematics.

**Not earned:** real NASH source covariance, availability of two centered signed site readings, analog-to-bit fault budgets, general nonGaussian distribution-free inference, sample optimality, hardware shot feasibility, any other source transfer. Full independent different-cell I1 and BW native ingestion unverified, no CANON/EXEC_SIGN.

**Recommended next MATERIAL gate (NOT automatic task cascade):** documented signed-site observer / analog comparator with a measured or independently justified bit transition kernel and Gaussian-core temporal IID validity. If the only actual available data remain M13 masked tensor RMS, STOP: the whole signed-local Gaussian noise family is a useful mathematical counterexperiment but not an available instrument.

FINAL: M16_ROT006_SHARP_MODEL_DEPENDENT_CONDITIONAL_BIT_FAULT_RADIUS_PASS / ADAPTIVE_MARTINGALE_HOEFFDING_PASS / INDEPENDENT_GAUSSIAN_SCALE_MIXTURE_SIGN_INVARIANCE_PASS / IV80_6_CHECKS_PASS / SYMMETRIC_BSC_DIFFERENT_PHASE_REVIEW_PASS / PUBLIC_REPO_READBACK_TO_VERIFY / BW_UNVERIFIED / NO_GENERAL_NOVELTY / NO_PHYSICAL_SITE_SENSOR / NO_CANON / NO_EXEC_SIGN.
