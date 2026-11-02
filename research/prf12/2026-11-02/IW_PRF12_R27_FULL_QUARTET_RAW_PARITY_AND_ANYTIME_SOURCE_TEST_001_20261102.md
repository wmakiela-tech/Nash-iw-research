---
artifact_id: IW_PRF12_R27_FULL_QUARTET_RAW_PARITY_AND_ANYTIME_SOURCE_TEST_001_20261102
created_at: 2026-11-02
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_QUARTET_LAW / ALL_REAL_XI_INTERVAL_LOWER_BOUND / CONDITIONAL_RESET_HAZARD / FINITE_CP_CALIBRATION / NONIID_BINOMIAL_DOMINATION / ANYTIME_E_PROCESS / NUMERIC_INDEPENDENT_MATRIX_REPRO_PASS / REFEREE_PENDING
claim_ceiling: NO_FULL_MULTINOMIAL_MINIMAX_OPTIMALITY / NO_EMPIRICAL_CALIBRATION / NO_FORMAL_CP_INTERVAL_ENDPOINT_PROOF / NO_HARDWARE / NO_CANON / NO_EXEC / NO_NOVELTY / ORIGINAL_SINGLE_COPY_3Q_LOCC_CLOSURE_OPEN
---

# PRF12 R27 — All-four-outcome audit: calibrate raw parity rather than invert the detector; an exact non-iid binomial and anytime test

**Data:** 2026-11-02. **Lineage:** PRF11 R35; PRF12 R23 finite source-ON rectangular Y preparation + X/Y analysis and direct Z readout; R24 conditional source reset survival, R25 affine T1/asymmetric detector, R26 two-reference Clopper–Pearson calibration and corrected bounded score. **Thesis:** the four recorded pair outcomes \\(R_1,R_2\\) may contain information beyond one bit, but their direct **raw agreement** Z=1[R1=R2] already admits a much sharper **certified, parameter-calibrated conditional Bernoulli test** than R26's conservative corrected-score Hoeffding test in this EXACT physical source model. We do not claim full multinomial optimality or any result on the original 3-qubit LOCC closure gap.

## 0. Source maps, external host subtraction and quantifiers

Primary first-owner R26: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-02/IW_PRF12_R26_FINITE_REFERENCE_CALIBRATION_AND_IDENTIFIABILITY_001_20261102.md . R23 complete interval source: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-01/IW_PRF12_R23_SOURCE_INDEX_AND_REPRO_MANIFEST_001_20261101.md . R25 corrected hidden-state conditional hazard: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-02/IW_PRF12_R25_AFFINE_T1_AND_FAST_RESET_IDENTIFIABILITY_LIMIT_001_20261102.md .

Mature external hosts: Clopper–Pearson exact intervals, https://doi.org/10.1093/biomet/26.4.404 ; optional-stopping-safe e-values/supermartingales, Grünwald–de Heide–Koolen (2024), https://doi.org/10.1093/jrsssb/qkae011 ; randomized measurement and purity methods, https://doi.org/10.1016/j.physrep.2024.09.009 . Neither raw parity, binomial stochastic domination, interval arithmetic nor e-processes are claimed as original methodology. Source-specific assembly warrants independent referee review.

Freeze **all R23/R26 hardware and source contracts**: gamma=1 units, Omega_max/gamma=10, free Delta=.5, source active during all rectangular Y preparation and X/Y analysis pulses, direct ideal Z endpoint followed by T1 detector dwell td=.05/gamma and sensor reset tr=.05/gamma, source A single static hidden xi THROUGHOUT both shots of every intact pair, A xi can have ARBITRARY dependence BETWEEN pairs; source B independent symmetric Levy dephasing in each stage and each run. Random private common axis J per pair with fixed w=(.18,.20,.62) for (X,Y,Z). A source reset may occur at ANY point in the pair, but its no-reset survival lower bound s=exp(-lambda L), L*gamma=1.7783185307179588, lambda/gamma=.02 MUST hold **conditional on the actual latent xi, prior history, private axis and variables governing hazard**, e.g. an exogenous Poisson reset clock. Readout labels must be independent across the two shots conditional on their ideal physical readout means; reference calibration is independent and detector remains stationary.

## 1. Theorem R27.1 — the entire conditional four-category likelihood is a quadratic polynomial

For selected J=j, let m_j(xi)∈[-1,1] denote the Z mean BEFORE detector, computed by R23's exact source-active finite controls. Under source A and no reset the two shots have the identical m_j(xi). Under B they have identical fixed mu_j, each from a continuous source-active Lindblad channel. A single recorded sign R∈{+1,-1} has mean z=c*m+d with effective T1/assignment calibration c=p0-p1 and d=p0+p1-1 (R25/R26). Conditional on xi,J the two recorded shots are independent and identically distributed. Hence the complete ordered quartet is EXACT:

  P(++|j,xi)=(1+z_j)^2/4,
  P(+-|j,xi)=P(-+|j,xi)=(1-z_j^2)/4,
  P(--|j,xi)=(1-z_j)^2/4,       z_j=c*m_j(xi)+d.    (R27.1)

For B use z_B,j=c*mu_j+d. Thus the signed one-shot mean and the raw parity are the two freely varying quantities in the four-category model under conditional exchangeability:

  P(++)-P(--)=z_j;   P(same|j,xi)=(1+z_j^2)/2.      (R27.2)

The R26 corrected product Yhat estimates a PRE-DETECTOR quadratic using division by the measured c^2. Instead retain directly the raw binary observation Z=1[R1=R2]. Under intact A and independent B shots,

  p_A^raw(xi;c,d)=1/2+1/2 sum_j w_j (c*m_j(xi)+d)^2,
  p_B^raw(c,d)=1/2+1/2 sum_j w_j(c*mu_j+d)^2.       (R27.3)

These are genuine Bernoulli probabilities, even if the latent hidden xi has an arbitrary BETWEEN-pair history. The conditional means, not an assumed iid marginal distribution, determine error bounds.

**Information warning:** (R27.1) shows that the quartet also exposes the signed marginal z_j. It has NOT been proved that this signed information fails to improve minimax efficiency for the actual source-A family. In a deliberately SIGN-SYMMETRIZED restricted experiment, a fresh fair coin F∈{±1} is multiplied onto BOTH recorded signs. Then ++ and -- become equiprobable, as do +- and -+, so the entire resulting four-outcome distribution depends only on raw parity. Within THIS restricted invariant data class, parity is sufficient; this does NOT establish unrestricted four-outcome sufficiency or full nuisance-robust likelihood optimality.

## 2. Theorem R27.2 — known finite calibration data imply an ALL-XI strict source gap

Use the SAME synthetic fixed-n R26 reference record, not real data:

 (n0,K0,n1,K1)=(46000,45540,69000,3705),  delta_cal=.01.

Two independent two-sided CP confidence intervals with individual tail level alpha=.005 give (conservatively outward-buffered 1e-12 for numerical beta quantiles):

 p0 in [0.9886260251098791, 0.9912535947691880],
 p1 in [0.05131577713212541,0.05614809544764209];
 c in [0.932477929662237, 0.939937817637063],
 d in [0.039941802242004,0.047401690216830].       (R27.4)

Joint confidence at least 99% follows from Clopper–Pearson + Bonferroni given fixed-size iid reference measurements. The full code evaluates the beta quantiles with SciPy, enlarges them by 1e-12 and checks tail inequalities using a separate binomial implementation. **This does not constitute a formal, directed-rounding certificate for the CP endpoints**; the robust source gap has large slack compared with the buffer, and an independent referee should verify the quoted endpoints in fully certified arithmetic.

With these entire c,d rectangles, compute R27.3 for ALL xi. R23's exact unitary model uses finite Y preparation of length t=pi/20, free phase xi*Delta with Delta=.5, finite -Y pulse before X outcome, +X pulse before Y outcome, and direct Z for the third axis. The three m_j are calculated independently of the detector model by 3D Bloch rotation Rodrigues matrices, enclosed by mpmath.iv (dps=40) at 7001 Xi grid nodes covering [-35,35] with interval parameter boxes c,d. The smallest LOWER NODE boundary is 0.5703921702934973 at xi≈-3.96.

For any xi, |partial_xi m_j(xi)| ≤ T_shot=Delta+2t=.81415926535898, by the usual Duhamel/unitary observable perturbation argument. Since |c*m_j+d| ≤ c_max+d_max, the raw-agreement Lipschitz constant is bounded by

  L_raw = c_max(c_max+d_max)(Delta+2t) ≤0.75557052648.

Grid spacing h=.01 gives the INTER-NODE subtraction L_raw*h/2<0.003777853. Hence

  min_{|xi|≤35, (c,d) in CP rectangle} p_A^raw(xi;c,d)
    ≥0.5666143176611008.                              (R27.5)

For |xi|≥35, the R23 rectangle off-resonant spin-flip bound is f=Omega^2/(xi^2+Omega^2)≤100/1325,

  m_X,m_Y≥1-8f>0,   m_Z≥1-2f>0.

Since c,d>0 throughout the interval, monotonic squaring gives the INDEPENDENT tail lower bound

  p_A^raw ≥ 0.5+0.5[(wX+wY)(c_min*(1-8f)+d_min)^2
                    +wZ(c_min*(1-2f)+d_min)^2]
           ≥0.7462661897728924.                      (R27.6)

By the same continuous Levy-B 3x3 generator used in R23, an interval Taylor propagator with 120 terms gives mu≈(0.5219734435,0.00231335785,0.04809737885). Substituting the CP interval yields

  p_B^raw ≤0.5289568525891072,                     (R27.7)

where a 1e-12 conservative buffer also covers the many-orders-smaller Taylor truncation. Source-specific conditional A no-reset probability is uniformly at least 0.56661431766; no Cauchy prior on a persistent xi is required for this part.

## 3. Theorem R27.3 — reset in the middle of shots and non-iid exact BINOMIAL domination

If A resets at any point in the pair, its two pre-detector Z means could be arbitrary m1,m2∈[-1,1]. Their recorded means each lie in [d-c,d+c]. The minimum possible PRODUCT of the two recorded means is d^2-c^2 (since 0<d<c). Therefore the raw same bit under reset always satisfies

  p_A^raw(reset)≥(1+d^2-c^2)/2 ≥ (1-c_max^2)/2
                        ≥0.05825844948783809.          (R27.8)

Let s=exp(-.02*1.7783185307179588)=0.9650586805668616 be the conditional hidden-state AND private-axis no-reset survival lower bound. By R27.5-8,

  p_A^raw(pair agreement | full prior, latent variables) 
       ≥ s*0.5666143176611008+(1-s)*0.05825844948783809
       ≥0.5488516928855485.

Thus choose safe rounded constants, for EVERY allowed history and on the joint CP-coverage event,

  a=0.548 ≤ Pr_A(Z_j=1|past),
  b=0.529 ≥ Pr_B(Z_j=1|past),   a>b.           (R27.9)

The inequalities are SOURCE-CONTRACT CONDITIONAL, not claims that Z_j are iid under A. A sequential coupling with independent uniforms or supermartingale stochastic dominance gives

  Pr_A(Σ_{j=1}^N Z_j <k) ≤ BinomCDF(k-1;N,a),
  Pr_B(Σ Z_j ≥k) ≤ BinomSF(k-1;N,b).             (R27.10)

At N=8497 and k=4576, the exact tails are ≤.039054431737654514 and ≤.03989507697069841. Both are less than delta_test=.04. Calibration failure has probability at most delta_cal=.01, so each hypothesis' WRONG-CONCLUSION probability is at most .05. No model of iid Xi is needed. This is an improvement over R26's deliberately conservative Hoeffding bound for a bounded, *non-Bernoulli* calibrated score: R27 uses a raw **Bernoulli** statistic for which sharp binomial stochastic bounds are permitted.

This conclusion does not guarantee successful calibration on all samples: if the actual reference counts fail to certify a>b, ABSTAIN. The actual sample numbers are the old SYNTHETIC record; an experimental result needs real counts and live detector calibration.

## 4. Theorem R27.4 — anytime-valid testing WITHOUT optional stopping of reference calibration

Still fix the reference calibration samples BEFORE science; after observing them, determine safe a>b on the CP coverage event. For each subsequent pair write Z_i∈{0,1}. Define

  M_n^A=product_i (a/b)^{Z_i} ((1-a)/(1-b))^{1-Z_i},
  M_n^B=product_i (b/a)^{Z_i} ((1-b)/(1-a))^{1-Z_i}=1/M_n^A.   (R27.11)

Under SOURCE B, for every allowed history E[M_n^A/M_{n-1}^A|past]≤1 because p_i^B≤b and a>b. Thus M_n^A is a nonnegative test supermartingale. Under SOURCE A, M_n^B is likewise a nonnegative supermartingale because p_i^A≥a. Ville's inequality implies that declaring A when M_n^A≥1/delta_test, or B when M_n^B≥1/delta_test, at ANY data-dependent stopping time has respective wrong-declaration probability at most delta_test on the calibration-coverage event. Adding delta_cal gives the same unconditional per-hypothesis 5% bound with the given delta allocation. A finite-sample maximum-stopping schedule may also be imposed.

This is **not** an anytime-valid Clopper–Pearson calibration: the 115000 reference measurements remain fixed-size. If calibration itself is stopped adaptively, R26's fixed-n CP intervals MUST be replaced with a suitable confidence sequence. E-processes for composite nulls and safe testing are well-developed externally; no new e-value methodology is claimed. Under the maintained strict conditional gap, a correct-side crossing occurs almost surely as N→infinity, conditional on successful calibration; no claim of specific expected stopping time or finite deadline is made.

## 5. Resource comparison and precise limitations

The same inherited nominal setting (synthetic CP calibration reference, lambda/gamma=.02 with reset within shots, source-ON pulses, c,d detector) gives:

| Protocol | calibration reads | scientific pairs | total single-shot reads | nominal clock gamma*T |
|---|---:|---:|---:|---:|
| R26 calibrated bounded-score Hoeffding | 115000 | 49215 | 213430 | 101480.6965 |
| R27 directly calibrated raw parity, exact binomial | 115000 | **8497** | **131994** | **27035.2226** |

Physical clock only uses inherited ILLUSTRATIVE reference-readout cost gamma*t_cal=.1 and worst science-pair gamma*T_pair=1.8283185307. It is NOT a hardware budget including accurately characterized reference state preparations, possible switching overhead, drift, or source calibration. Savings: about 82.7% scientific pairs, 38.2% total sensor readings, 73.4% illustrative experiment clock. These are comparisons against R26's specified conservative method, not universal quantum-optimality claims.

The FULL four-outcome model R27.1 is retained and is potentially more informative than raw parity, including outcome sign and axis. R27 did **NOT** optimize over general four-category scores, unknown Xi distributions, adversarial per-pair phase trajectories or full multinomial composite likelihoods. It does not treat correlated detector errors, unknown reference preparation, detector drift, an uncalibrated physical Z detector, axis errors, source-reset hazard depending on latent Xi, rapid piecewise-Cauchy A_h that violates original static-within-pair contract, or original single-copy three-probe LOCC closure. R25's fast-reset nonidentifiability remains a strict negative guard.

## 6. Independent repro, precision caveat and next falsifiers

**Main one-file runnable** reconstructs R23's source-A finite Bloch unitaries as rigorous-style mpmath.iv interval operations, source-B via 120-term interval Taylor generator, 7001 phase nodes on [-35,35], Duhamel inter-node bound, exact off-resonant far-tail bound, interval CP calibration rectangle, conditional reset lower bound and exact SciPy binomial tails, with a complete JSON transcript. **Second independent executable** uses source-A 2x2 matrix exponentials and source-B 4x4 Lindblad superoperators, checks 10 fixed xi, verifies all FOUR ordered outcomes, tests the null test-supermartingale factors on 202 extreme conditional probabilities, and independently checks binomial decision thresholds. Both scripts execute PASS.

**Important arithmetic distinction:** the quantum compact-grid enclosures are evaluated in mpmath.iv interval arithmetic and all far-detuning bounds are analytic; source-B Taylor remainder is bounded by standard convergent norm series. CP interval quantiles and final binomial CDF/SF are evaluated using SciPy floating-point with explicit 1e-12 outward CP shifts, checked against independently implemented binomial tails. We have **not** performed fully directed-rounding interval certification for the Beta CDF inversion or every special-function evaluation. The numerical safety margin (~8.5e-4 from chosen a) is large compared to the 1e-12 CP buffers; nonetheless a strict formal all-layer proof would certify those scalar probability functions with interval arithmetic too.

**Priority R28:** use the extra signed/axis labels of the 4 categories to optimize a *genuinely robust* conditional e-variable or linear score over the actual compact convex hull of Xi-indexed laws, including detector (c,d) confidence rectangles and quantified source resets; contrast any improvement against the R27 sign-symmetrized parity-only baseline. Independently audit time-uniform reference calibration under real device drift and finite reference preparation, without crossing these contracts.

RETURN: PRF12_R27 / COMPLETE_QUARTET_LAW / RAW_PARITY_NO_DEBIAS / CP_RECTANGLE_ALL_XI_INTERVAL / MIDSHOT_RESET_FLOOR / CONDITIONAL_BERNOULLI_BINOMIAL_STOCHASTIC_DOMINATION / OPTIONAL_STOPPING_SAFE_SOURCE_EPROCESS / INDEPENDENT_2X2_4X4_PASS / REFEREE_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC / ORIGINAL_SINGLE_COPY_3Q_LOCC_CLOSURE_OPEN / GITHUB_PENDING_BW_INGEST.
