---
artifact_id: IW_M16_ROT007_TWO_SHOT_RANK_BLOCK_MONOTONE_CALIBRATION_MEAN_ERASURE_ELLIPTICAL_PRIOR_ART_AND_PORTFOLIO_STOP_001_20261122
return_id: IW_M16_ROT007_TWO_SITE_TWO_SHOT_KENDALL_BLOCK_SOURCE_MONOTONE_CALIBRATION_NONCENTRAL_MEAN_ERASURE_ADAPTIVE_SIGN_FAULT_AND_EXTERNAL_NOVELTY_DOWNGRADE_001_20261122
origin: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_11 / M16
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
science_type: SOURCE_CONDITIONAL_TWO_SITE_TWO_SHOT_RANK_OPERATOR / CLASSICAL_ELLIPTICAL_KENDALL_TAU / CALIBRATION_TIME_SCALE_TRADEOFF / PORTFOLIO_STOP
status: SOURCE_EXACT_FORMULA_AND_FIRSTNESS / CLASSICAL_THEOREM_EXTERNAL_PRIOR_READ / ACTUAL_1M_BLOCK_PAIR_NON_GAUSSIAN_SIM / PRELIMINARY_FALSE_PATHWISE_ASSUMPTION_CAUGHT_AND_CORRECTED / SOURCE_BYTE_IDENTICAL_EXEC_GIT_BLOB
claim_ceiling: NO_GENERAL_MATH_NOVELTY / NO_PHYSICAL_SIGNED_RAW_SITE_SENSOR / NO_ORIGINAL_M13_HISTORICAL_RUNTIME / NO_NEW_PHYSICS / NO_CANON / NO_EXEC_SIGN / NO_BW_NATIVE_ING
---

# M16 ROT007 — A two-snapshot rank observable that cancels an unknown source mean and block-stable nonlinear sensor response

## 0. Decision before calculation: what is the externally relevant research question?

The user-facing scientific portfolio review of 22 November argues for closing a saturated source-only M13/M16 NP threshold chain unless it finds EITHER a portable non-mature general theorem OR a genuine original measurement interface. EKS1 GAP-008 similarly asks each cell to state who could cite a result outside IW/NASH.

**External-facing M16 question**: Can the spatial dependence of two source hypotheses be tested with TWO direction-labelled local sensors WITHOUT knowledge of zero offset, source mean or nonlinear sensor response, when there are repeat readings and unknown positive shared stochastic volatility?

**Proposed audience**: experimental statistics, Gaussian-copula spatial inverse problems, and metrology under unknown sensor responses. BUT the underlying answer is **mature classical Kendall rank theory**, not a novel mathematical result. The project-specific application to artificial N41 source anisotropy is useful as a controlled counterexample / observation-interface design, but provides no existing evidence of a publishable external theorem or physical detector. This is an affirmative external relevance *question*, not an affirmative external novelty *finding*.

## 1. Original source / firstness custody

Direct original source read this rotation:
- M16 ROT005 original public report and exact code (Git blobs 7b1d0057a9fdcbe44831011574eb8999986a86aa and 685b92909a5133f3725976438c020127a9d40077): FIRST two-site Gaussian SIGN-concordance observation distinguishing B vs newly x/y permuted Bpi under arbitrary independent positive gains PER SHOT, provided sensor readings are signed, CENTERED noise.
- M16 ROT006 FIRST sharply model-typed adaptive sign-bit corruption alias radius eta* and a finite-n conditional Hoeffding test. Public report Git blob ec4d4be01eb36f628515685767c77add2ae3fcfc.
- Geeky-S13 ROT015 full original public source DIRECTLY READ (pinned Git blob f77feeb2526ae06f182788708c331403108f5e9d): FIRST reimplemented original M13 deterministic tensor energy profile m_alpha(s), showed specific nonconstant site means, FIRST model-specific 3-site affine no-go and four-site exact Cauchy escape under per-shot common affine scaling and m amplitude. This new M16 test is a **different observation contract**, two sites but TWO temporal shots per independent statistical block, with individual arbitrary block-stable monotone transformations. It neither audits Geeky's IV60 source nor claims its priority.
- Geeky-S12 ROT038 FIRST synthetic exact rational source 8-parameter Gaussian covariance A/B. M16 ROT004 FIRST new Bpi = x/y permutation of ORIGINAL B (not Geeky source A). M13 FIRST actual N41 tensor and source site/mask definitions; historic dtc0a_runtime_v0_3_1.py still inaccessible.
- SCOPE12 ROT017 directly read original source and emphasizes separation of mathematical lattice algebra, tensor action and physical readout; M16 makes no NCDG gauge claim.
- XH-S8 ROT012 cross-line current literature ledger read via original full Slack dispatch, pointing to mature blind calibration, Gaussian source and experimental measurement problems. No user-independent source sensor acquisition.

**External primary mathematical prior DIRECT READ WITH PDF PAGES**:
F. Lindskog, A. McNeil, U. Schmock, "Kendall's Tau for Elliptical Distributions" (working-paper PDF, https://staff.math.su.se/lindskog/KendallsTau.pdf), Theorem 2 and Lemma 6 explicitly prove tau=2/pi*arcsin(rho) for continuous elliptical distributions; original scanned PDF p.3 actually screenshot-checked. Independent current accessible published secondary source, "Canonical correlation analysis for elliptical copulas", J Multivariate Analysis (2020), DOI https://doi.org/10.1016/j.jmva.2020.104715, states same known transform, even for transelliptical families. Therefore **NO_GENERAL_NOVELTY** by explicit subtraction, not vague reference to "prior art".

## 2. Exact source experiment and mathematical theorem

In a 41^3 synthetic centered site Gaussian source, ORIGINAL Geeky-S12 ROT038 B plus NEW M16 ROT004 x/y-swapped Bpi have the SAME single-site marginal Gaussian N(0,1), and the following EXACT two-neighbor x-axis centered covariance / correlations (unit variance):

  rho_B = beta_x(B)/2 = 1/40 ;
  rho_Bpi = beta_x(Bpi)/2 = 3/200 .

These are distinct synthetic B/Bpi hypotheses. Do NOT import Geeky's original A/B pair correlation r_A=1/50.

**Two temporal snapshots per observation block** b. For each spatial channel i in {x0,x0+e_x} and time t in {1,2}, observe

  Z_{i,b,t}= f_{i,b} ( mu_{i,b}+sqrt(S_{b,t}) G_{i,b,t} ),

where
1. each fixed f_{i,b}:R->R is STRICTLY INCREASING but otherwise arbitrary, different for two channels and all blocks, possibly hypothesis-dependent, and must be **identical between the two temporal observations of its own block**; it can be nonlinear, unbounded or data-dependent, as long as the SAME single monotone function is applied to both;
2. mu_{i,b} is an arbitrary site-specific deterministic or latent-adapted common additive source mean, also **identical between the two shots within the block**, free to vary independently between blocks; it need NOT be equal between sites or known, so may represent lambda_b*m_alpha(s) with unknown lambda_b. A time-varying source *within* the two shots is not covered;
3. each S_{b,t}>0 is a common within-shot scalar for the TWO spatial channels, can vary between the temporal shots, independent of the current Gaussian core pairs (condition on any historical scale decisions); the two source Gaussian core vectors G_{b,1},G_{b,2} are independent N(0,Sigma_X) with exact source rho_X and are independent between blocks;
4. the operator is still HYPOTHETICAL: there is no demonstrated real RAW two-site sensor or realistic guaranteed temporal block stability in the historical M13 tensor-RMS workflow.

Define ONE observed binary rank-comparison:

  K_b = 1{(Z_x,b,1-Z_x,b,2)(Z_y,b,1-Z_y,b,2)>0}.

This requires TWO site values at EACH of TWO distinct times = FOUR scalar readings per block.

**Claim A: exact nuisance elimination PATHWISE for f and mu.**
For every strictly increasing f, sign(f(a)-f(b))=sign(a-b). An equal additive mu at two temporal readings cancels in the difference. Therefore K_b equals the rank comparison of the latent scaled Gaussian values for every realization, regardless of f_{i,b} and mu_{i,b}; there is NO estimation of source baseline or calibration function.

**Claim B: exact B/Bpi Bernoulli law despite different positive common shot scales.**
Condition on any S_{b,1}=s1>0,S_{b,2}=s2>0 independently of the cores. The latent difference vector equals sqrt(s1)G_{b,1}-sqrt(s2)G_{b,2}, hence is a CENTERED 2D Gaussian with covariance (s1+s2)Sigma_X. Its correlation is rho_X exactly. Classical bivariate Gaussian orthant identity gives

 p_X=P_X(K=1 |s1,s2)=1/2+arcsin(rho_X)/pi

independently of s1,s2 or of mu and f. Because Gaussian cores in disjoint blocks are IID and p_X is conditionally constant even given historical scales, the clean K_b are IID Bernoulli(p_X). Model-dependent or data-dependent f and mu cannot affect K by Claim A.

Exact source values (verified 85 decimal mpmath):
 p_B=0.507958576319813930215749465282236036644865227123128010...
 p_Bpi=0.504774827360199009520339424700226339292682510845164917...
 Dp=0.003183748959614920695410040582009697352182716277963093....

This is also a direct special case of classical Kendall tau for Gaussian/continuous elliptical copulas: tau=2p-1=2arcsin(rho)/pi. **No novel distribution theorem is asserted.**

**Very important NON-EQUIVALENCE:** If volatility scales differ between the two time-shots, K(G_core) and K(sqrt(S)G_core) are NOT generally equal PATHWISE. Only their conditional probability laws agree. The initial actually executed prototype incorrectly asserted their pathwise equality and FAILED immediately. This erroneous stronger hypothesis was rejected, the code corrected, and the final mathematical proof carefully conditionalized on s1,s2. This is an actual negative-control learning, not a hidden successful test.

## 3. Exact connection to M16 ROT006's sharp fault budget, and REAL resource units

After computing K_b, suppose an adversary independently of source typing may corrupt the observed PAIR-RANK bit by K'_b=K_b XOR F_b with arbitrary bit/model/history dependence, subject to

  P_X(F_b=1|past)<=eta

for each block and model, as in M16 ROT006. The clean Bernoulli gap is EXACTLY SAME Dp, so the sharp worst-case model-dependent bit corruption alias radius and conditional concentration bound transfer verbatim:

 eta*=Dp/2=0.0015918744798074603477050202910048486760913581389815465...
 eta>=eta*: two legal one-sided model-specific kernels make the output bits EXACTLY IID with same Bernoulli law; no possible uniform discrimination for any number of blocks, minimax error1/2.
 eta<eta*: midpoint classify using empirical K'_b gives every conditional error <=exp[-2n(eta*-eta)^2], by conditional bounded martingale exponential-moment inequality (not by claiming corrupted bits remain IID).

Strict Hoeffding sufficient resource counts (not NP optimality):

| Worst-case pair-bit error eta | confidence >95%: n BLOCKS | actual two-site snapshots 2n | confidence >99%: n BLOCKS | source snapshots 2n |
|---|---:|---:|---:|---:|
| 0 | 591093 | 1182186 | 908653 | 1817306 |
| .0005 | 1256399 | 2512798 | 1931392 | 3862784 |
| .0010 | 4275765 | 8551530 | 6572892 | 13145784 |
| .0015 | 177452948 | 354905896 | 272788403 | 545576806 |

A raw two-site snapshot comprises TWO individual scalar sensor readings; total site readings are FOUR per block. These are HYPOTHETICAL sampling counts, not costs from a real NASH detector. No benefit is asserted over the actual physical availability of original six masks.

If a common identical symmetric bit channel q is known and independent in both hypotheses, the harsher eta* barrier is inapplicable: gap scales (1-2q)Dp and remains positive for q<.5, per ROT006.

## 4. Falsification boundaries: two-shot temporal stability is load-bearing

- If the strictly monotone calibration function or additive mean drifts **between the two shots** within a block, the pathwise cancellation is gone.
- Under completely unrestricted model-specific, latent-adaptive offsets separately on EACH observation, a trivial strictly increasing map f_{i,b,t}(u)=u-Z^raw_{i,b,t} can send all observed values to zero. The full observation laws then coincide for all n. This proves there is no finite-sample universal guarantee under this much wider adversarial calibration host. It is NOT an argument that an actual physical instrument would use such an adaptive offset.
- If a channel reverses its orientation (strictly decreasing) or saturates (non-strict monotonic) between the two shots, sign comparisons are inverted or tied. The theorem requires STRICTLY INCREASING f_{i,b}, not merely "monotone" of unspecified orientation.
- Scales must be COMMON between both sites within each individual shot and independent of the current Gaussian pair. Arbitrary independent per-site scales/latent-adaptive nonlinear noise, or non-elliptical copulas with the same Pearson covariance, do NOT inherit the arcsin law automatically.
- A deterministic mean mu_i can be spatially unequal and vary from block to block, but must be stable within the TWO source observations. This directly addresses the ROT015 original mean-profile inequality; it does NOT validate real M13 sensor timing.
- If time-shots share temporally correlated Gaussian cores, their DIFFERENCE covariance is no longer simply (s1+s2)Sigma_X in general. Cross-time unknown dependence is a critical real instrument gate.

## 5. Actual numerical tests and an explicitly recorded failed overclaim

An expanded program was WRITTEN and ACTUALLY EXECUTED in this session:
 local file /mnt/data/m16_rot007/m16_rot007_block_pair_kendall.py
 4343 bytes, SHA256 5ae8e11665159c923218ad86ac0234bac77ccfa7cc14c6147bd1062ae65670fb
 local machine JSON /mnt/data/m16_rot007/m16_rot007_result.json
 SHA256 bf3494299d7a44fd94bfc1ce745010796cfe31c687ef508221d9b2ffa946b33c

- 85-digit mpmath source exact arcsin and each of 16 adjacent-integer strict Hoeffding gate checks PASS.
- 500000 independent BLOCKS for B and 500000 for Bpi: TWO shots each, per-shot volatility S∈{.5,1.5} independent and variable, block-varying arbitrary unequal site means mu0,mu1, separate asinh/exponential sensor functions, plus block-varying nonlinear offsets; both within-block functions strictly increasing. All 1000000/1000000 observed paired rank bits EXACTLY equal the corresponding untransformed scaled-data rank bits. THIS is pathwise validity of monotone f and mu, not of volatility.
- Final Monte Carlo p_B=.507834, p_Bpi=.504098 versus true .5079585763 and .5047748274; deviations 0.1762 and 0.9572 model binomial standard errors, no rejection. A simulation IS NOT an interval proof of the exact p.
- Only 92.3104% B and 92.3686% Bpi of rank bits agreed pathwise with unscaled Gaussian core comparisons: they were NOT required to agree. **PRELIMINARY FAILED ASSERTION**: an initial false claim that the paired rank bits were invariant PATHWISE to time-varying separate shot scales was caught by actual runtime AssertionError, then corrected before publication. This is a real negative guard. Final theorem only equal IN LAW under stated source Gaussian mixture.
- Both explicit least-favourable bit-fault alias kernel probabilities recalculated from exact p and eta*, PASS.
- Public GitHub executable is BYTE-IDENTICAL to the locally run script: actual Git blob SHA local computed git hash-object = 6711f6524113abdbc338ca2bc43bfa71c018641a and PINNED GitHub fetch returned exactly 6711f6524113abdbc338ca2bc43bfa71c018641a. Public code pinned commit:
https://github.com/wmakiela-tech/Nash-iw-research/blob/7298595c14eee2dfd438ec30c1408edbfe8c2e40/research/m16/2026-11-22/code/m16_rot007_block_pair_kendall.py
This is actual LOCAL execution of the SAME byte code as the uploaded GitHub version, though not a separate cold execution after download.

## 6. Research portfolio significance / STOP decision

**What changed since ROT005?** Instead of raw signed centered noise and unbounded arbitrary per-shot independent POSITIVE gains, the same synthetic two-site B/Bpi host permits two-shot rank testing with unknown sensor zero and potentially unknown nonlinear response, and even known mathematical variation of source mean/profile per BLOCK. Positive shared-volatility per shot is supported in LAW. **Tradeoff:** require two measurement times per rank bit and their within-block calibration/mean stability. Neither M16 ROT005 nor ROT007 dominates the other under the other's exact nuisance class.

**External prior-art subtraction is decisive:** classical 2001+ Kendall elliptical rank tau and modern transelliptical copula measurement already solve general monotone-calibration-invariant correlation. M16 offers a source-conditioned application, not a new transferable theorem in this run. XH-S8 ROT012 independently shows mature blind gains/calibration literature. No claim that NASH invented rank-based metrology.

**Operational go/no-go:** absent an authentic site-level instrument delivering TWO local readouts at TWO time-shots per stable block (or a source-certified proxy), future synthetic n optimizations are LOW PRIORITY and the M16/Geeky observation-instrument branch should transition to **HOLD_SOURCE_SENSOR** after archiving firstness, assumptions, mathematical statements and counterexamples. Science-first reallocation to physically validated PBH/BBN and time-quantum process source tests is more valuable, WITHOUT unilaterally reassigning another cell, changing CANON, LT, or native BW.

**Proposed falsifiable owner gate before reopening**:
1. SOURCE: genuine producer-defined local observation operator and N41 tensor/energy-to-site relation, not a named variable or synthetic Gaussian.
2. TIMING: two consecutive observations with demonstrably common within-block means and strictly increasing sensor responses, and calibrated hypothesis-blind temporal noise law.
3. VALIDATION: same external held-out data showing source B/Bpi covariance contrast with source-noise model and significance under instrument error; otherwise STOP.
A single failing gate blocks physical n-resource claims.

FINAL: M16_ROT007_CLASSICAL_KENDALL_TAU_SOURCE_APPLICATION_PASS / NO_EXTERNAL_MATH_NOVELTY / TWO_SHOT_NONCENTRAL_MEAN_AND_MONOTONE_CALIBRATION_PATHWISE_PASS / INDEPENDENT_PER_SHOT_POSITIVE_SCALE_MIXTURE_EXACT_LAW_PASS / INITIAL_FALSE_PATHWISE_SCALE_ASSUMPTION_CAUGHT / ACTUAL_ONE_MILLION_BLOCK_SIMULATION_PASS / EXACT_85DIGIT_RESOURCE_BOUNDS_PASS / LOCAL_EXEC_CODE_GITHUB_BLOB_BYTE_IDENTICAL / SOURCE_SENSOR_HOLD / NO_CANON / NO_EXEC_SIGN.
