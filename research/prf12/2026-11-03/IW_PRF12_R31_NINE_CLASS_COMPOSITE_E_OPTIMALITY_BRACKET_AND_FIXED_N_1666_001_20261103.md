---
artifact_id: IW_PRF12_R31_NINE_CLASS_COMPOSITE_E_OPTIMALITY_BRACKET_AND_FIXED_N_1666_001_20261103
created_at: 2026-11-03
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: SOURCE_TYPED_EXACT_E_FACTOR_SYMMETRIZATION / 7001_IV_ALL_REAL_XI_PASS / INDEPENDENT_2X2_4X4_PASS / FINITE_SUPPORT_DUAL_IV_PASS / FIXED_N_1666_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_UNRESTRICTED_ALL_HISTORY_TEST_OPTIMALITY / NO_GLOBAL_QUANTUM_MEASUREMENT_OPTIMALITY / NO_EMPIRICAL_DATA / NO_NOVELTY_OR_PRIORITY / NO_CANON / NO_EXEC / ORIGINAL_3Q_SINGLE_COPY_LOCC_CLOSURE_OPEN
---

# PRF12 R31 — Exact nine-class reduction for composite e-factors; a nearly tight certified affine-source contrast bracket

**Owner result, 3 November 2026.** R31 delivers two independent theoretical advances relative to R30: (1) exact extension of the R29 12-to-9 symmetrization from linear worst-case mean contrasts to positive composite-null e-factors **under a maximin expected-log-growth objective**, and (2) a fully declared rational nine-category postmeasurement score with an all-real-Xi mathematical certificate requiring **1666** rather than R30's 1682 source pairs for a fixed-N decision. An interval-valued nine-multiplier finite-source dual witness supplies an upper bound on the optimal contrast of a precisely defined conservative affine-source certification functional. The candidate scores at least 99.82% of that restricted optimum. This is NOT global minimax optimality across arbitrary quantum measurement, source-memory policies or nonlinear multirun tests.

## 0. Evidence and mature prior art

First physical source owner PRF11 R35: common static Cauchy Xi during intact runs versus independently incremented symmetric Cauchy–Lévy process. Nearest mathematical sources PRF12 R23 finite source-active rectangular sensor controls, R24/R25 exogenous Xi-conditioned reset hazard, R26 fixed-n Clopper–Pearson affine-detector calibration, R28 signed quartet randomized score, R29 Rao–Blackwell e-processes, and R30 all-real-Xi quadratic nuisance / second-derivative bounds. Readable source indices:
- R28 https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-02/IW_PRF12_R28_SIGNED_QUARTET_GLOBAL_XI_AND_NONIID_CERTIFICATE_001_20261102.md
- R29 https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-03/IW_PRF12_R29_DETERMINISTIC_TWELVE_CATEGORY_E_PROCESS_AND_NINE_CLASS_SYMMETRY_001_20261103.md
- R30 https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-03/IW_PRF12_R30_CP_QUADRATIC_AND_SECOND_DERIVATIVE_GLOBAL_CERTIFICATE_001_20261103.md

External mature hosts: Grünwald, de Heide and Koolen, *Safe testing*, JRSS B 86 (2024), DOI 10.1093/jrsssb/qkae011; Koolen and Grünwald, *Log-optimal anytime-valid E-values*, Int. J. Approx. Reason. 141 (2022), DOI 10.1016/j.ijar.2021.09.010; Hao and Grünwald, *E-values for exponential families: The general case*, Bernoulli 32 (2026), DOI 10.3150/26-bej1981; Clopper–Pearson fixed-reference interval method (1934). Conditional e-values, group symmetrization, quadratic interpolation and LP duality are standard mathematics. The narrow model-specific calculations below are NO novelty/priority claim.

## 1. Unchanged quantum and detector contract

Within each two-shot *intact* pair, one hidden Cauchy frequency Xi is CONSTANT through both sequential sensor preparations, exposures and measurements. Between pairs it may be arbitrarily correlated or even identical forever. A broken pair may have arbitrary two detector-input means m_1,m_2 in [-1,1], but conditional probability of remaining intact is at least s=exp(-lambda L)=0.9650586805668616 **even after conditioning on CURRENT Xi, privately selected measurement axis, complete relevant latent variables and observed history**, or an independent exogenous Poisson reset clock supplies the same lower bound. A mere marginal survival guarantee is insufficient.

B is an independent-increment symmetric Cauchy–Lévy source with the correct continuous Lindblad generator during every driven and free segment. The sensor is freshly prepared twice, and each shot uses finite source-ON rectangular pulses with Omega_max/gamma=10, gamma Delta=.5; X and Y analysis pulses of length pi/(20 gamma) and direct Z readout. The common axis J is private and independently drawn with probabilities w=(.18,.20,.62). The terminal idle T1 and asymmetric independent assignment errors are represented only by stable effective affine mean u=c m+d.

Fixed-size, INDEPENDENT synthetic reference counts (n0,k0,n1,k1)=(46000,45540,69000,3705) give joint 99%-coverage Clopper–Pearson rectangle expanded outward to
c in [.932477929562237,.939937817737063],
d in [.039941802142004,.047401690316830].
These are NOT experimental data. Individual CP beta quantiles use SciPy with outward scalar buffers, independently checked via binomial inversion; a fully directed-rounded special-function formalization is NOT claimed. If real calibration does not produce an invertible positive-gap rectangle, the procedure must ABSTAIN.

Observables z=(j,r1,r2) comprise 3 axes times 4 ordered pairs of signs. Conditional intact pair with identical mean u_j=c m_j(Xi)+d:
P_j(r1,r2|Xi)=w_j(1+r1 u_j)(1+r2 u_j)/4.
For broken pairs, replace u_j by independently specified u1,u2 and retain the same product-form conditional independent shot model. Only this declared one-sensor experiment is addressed; the original passive three-probe three-party single-copy asymptotic LOCC gap remains OPEN.

## 2. Theorem R31.1 — exact 12-to-9 reduction for positive composite e-factors

Let the experiment's family P0 (null) and P1 (alternative) be each closed under the transposition S of the two results inside any fixed axis, including reset trajectories. This holds for the intact two-shot laws (which are exchangeable) and for R29's broken-pair uncertainty square (m1,m2) in [-1,1]^2, provided the conditional hazard contract is not time-asymmetric. For any positive single-pair e-factor g(j,r1,r2)>0 define

  g_sym(z)=[g(z)+g(Sz)]/2.

For all P in P0, E_P g_sym=[E_P g+E_(S P)g]/2 <=sup_(Q in P0) E_Q g. Thus if g is uniformly e-valid, g_sym remains uniformly e-valid. For any Q in P1, concavity of log implies
  E_Q log g_sym >= [E_Q log g+E_(S Q)log g]/2
                 >= inf_(Q' in P1) E_(Q') log g.

Therefore restricting each one-pair positive e-factor to g(j,+,-)=g(j,-,+) can NEVER worsen its maximin expected-log-growth criterion under the stated symmetric composite families. Exactly NINE parameters remain: per axis ++, mixed, --. The same proof works with source A and source B interchanged as null and alternative.

**Ceiling:** this is a ONE-PAIR e-factor maximin result, not a proof that every adaptive multirun history-dependent 12-category test can be replaced with a nine-category one. If the reset hazard, detector, preparation or treatment of shot order is asymmetric, the group-invariance premise fails. Do not discard the original time-stamped twelve-category data from science storage.

## 3. Restricted certificate functional for R31.2 — exact objective being bounded

For any pointwise nine-category coin score f in [0,1]^9, with original fixed axis weights w, define the source-typed CONSERVATIVE certification functional

  L(f)=s * inf_(Xi in R, (c,d) in CP) E_A,intact f
      +(1-s) * sum_(j=X,Y,Z) w_j inf_(m1,m2 in [-1,1],(c,d) in CP)
                           E_A,reset[f|j]
      - sup_((c,d) in CP) E_B f.                         (R31.1)

The first two terms may minimize over SEPARATE choices of detector nuisance parameters. This decomposition is deliberately more conservative than a full likelihood calculation using the same fixed physical c,d across all cases. The linear source-reset floor also permits the most adverse within-pair jumps; it is not a Cauchy-shape prior on broken shots. Thus a LOWER bound on L(f) is a legal sufficient conditional A-versus-B contrast certificate, but the supremum of L is NOT the global statistical or quantum optimum.

Since L is concave in f, a scenario relaxation obtained by restricting Xi, CP and reset nuisance variables to FINITELY many allowed values yields an UPPER bound on sup_f L(f): infimums over subsets can only increase and supremums over subsets can only decrease this objective. R29 exact affine symmetrization applies to (R31.1), hence the bound covers ALL TWELVE-COEFFICIENT linear pointwise scores, provided the source family remains swap-closed.

## 4. Theorem R31.2 — reproducible rational test and ALL-REAL-Xi lower bound

A finite-grid LP with 701 Xi nodes on [-35,35], four CP corners and the four reset mean extremities is DESIGN-ONLY. The numerical LP candidate is
 f_X=(.94253641,0,1), f_Y=(.90689684,0,1), f_Z=(.34712054,0,.01827027).
Freeze instead the exact decimal-rational source score

| Axis | f(++) | f(mixed) | f(--) |
|---|---:|---:|---:|
| X | 0.943 | 0 | 1.000 |
| Y | 0.907 | 0 | 1.000 |
| Z | 0.347 | 0 | 0.018 |

Implementation: after observing the axis and two signs, toss an independent private coin with probability f(z) and record one Bernoulli bit Y. The only new resource versus R30 is changed classical randomization; NO changes of sensor/control source.

Let F_j(u)=[alpha_j(1+u)^2+beta_j(1-u)^2]/4. For fixed Xi this is quadratic in nuisance c,d, so averaging FOUR corner values can exceed the value at an arbitrary CP interior point by at most

  H_CP <=sum_j w_j(alpha_j+beta_j) *[(c_U-c_L)^2+(d_U-d_L)^2]/16
       =0.000006660283811603181 (outward inflated).       (R31.2)

At 7001 directed mpmath.iv nodes Xi in [-35,35], spacing h=.01, the minimum of the four source-A corner scores is >=.32081795261915746 (near Xi=-4.32). The known source-on unitary Duhamel bound on m'_j,m''_j yields for the score

  |d²/dXi² E_A f|<=M2=.5813110901631865,

and the linear interpolation shortfall between neighboring nodes is at most M2*h²/8 = .000007266388627039832. Hence

  min_(|Xi|<=35,CP) E_A,intact f >=.32080402594671886.    (R31.3)

For |Xi|>=35, an independent rectangular off-resonant spin-flip amplitude estimate supplies >=.38804378238408166; this tail bound is strictly higher. The A guarantee in (R31.3) holds on the ENTIRE real Xi axis, not merely the finite grid or under a Cauchy average.

For an arbitrarily broken pair the two detector-input means lie in [-1,1]. Each signed score is bilinear in them; its minimum is attained at one of four mean corners. For fixed equal-sign corners its CP dependence is a one-dimensional convex quadratic; for opposite-sign corners it decreases with c and has an explicit clipped d-minimizer. This yields (outward buffers included):
  r_X>=.05623468220154122,
  r_Y>=.05441647202405015,
  r_Z>=.01711250089754987,
  sum_j w_j r_j >=.03161528775756837.               (R31.4)

NOTE: the CP minimizer of the Z reset floor lies at an INTERIOR d value; treating only the four CP corners as sufficient would produce an invalid LOWER bound. The independent matrix/nuisance audit explicitly checks this. Conversely, the fixed source B total score is convex in c,d, so its maximum on the CP rectangle is at a corner. Direct 120-term interval Lindblad propagation plus an independent 4x4 audit yield

  sup_CP E_B f <=.27161358975207756.                    (R31.5)

With s conservatively rounded DOWN to .9650586805658616, (R31.3–5) prove

  inf history E_A[Y=1|past] >=.3106993896688963,
  sup history E_B[Y=1|past] <=.27161358975207756.     (R31.6)

This source-A statement requires the R25 LATENT-Xi-conditioned lower survival guarantee, not merely a marginal Poisson rate inferred after selection bias.

## 5. Theorem R31.3 — EXACT fixed-N non-iid test with both errors <5%

Choose transparent weaker thresholds a=.31068 and b=.27164. The added private output coin makes Y a genuine Bernoulli observation. For arbitrary BETWEEN-pair Xi dependence preserving the full source contract, E_A[Y_n|full relevant past]>=a and E_B[Y_n|full relevant past]<=b. Apply conditional stochastic domination by Binomial(N,a) and Binomial(N,b), NOT an assumption that the hidden Xi process is iid.

For N=1666 declare A iff K=sum Y_n>=485. Exact binomial tails:

  P_A(wrong B|successful CP calibration)
    <= BinomCDF(484;1666,.31068)=.03927014418496993;
  P_B(wrong A|successful CP calibration)
    <= BinomSF(484;1666,.27164)=.039949982056578834.

Add <=.01 joint CP-reference failure to get per-hypothesis total wrong declaration <=.05. All 115000 reference measurements are SYNTHETIC; an actual device run must repeat fixed-size calibration and may return ABSTAIN.

Relative to R30 N1682, R31 saves 16 science pairs (0.95%), 32 sensor readouts and gamma-scaled worst-case modeled source/calibration wall time 29.2531; relative to R28 N2251, R31 saves 585 pairs. With the same 115000 synthetic reference readings R31 total individual reads =118332 and gamma*wall clock=14545.97867218. This is a modest physical resource uplift; most cost remains the finite detector calibration.

The deterministic coin-free full-category e-factor theorem R29 still applies with the stronger R31 bounds a,b:
 G_A(z)=(1-a)/(1-b)+[a/b-(1-a)/(1-b)] f(z),
 G_B(z)=(1-b)/(1-a)+[b/a-(1-b)/(1-a)] f(z).
They are safe opposite-composite-null e-factors and produce certified source-uniform log-drift lower bounds >=.0043000858571 under A and >=.0042732646732 under B. They do NOT inherit the Binomial(N=1666) fixed-N tails without actually generating the private coin Y.

## 6. Theorem R31.4 — independent FINITE-SUPPORT dual upper certificate

Take the 701-node source-phase finite relaxation from Section 3. Introduce scalar auxiliary variables A0, r_X,r_Y,r_Z and B0 (each in [0,1]) constrained by:
 A0 <= P_A,intact(f;Xi_i,c_l,d_l) at each sampled Xi_i and four CP corners;
 r_j <= P_A,reset(f|j;m1,m2,c_l,d_l) at each chosen mean corner and CP corner;
 B0 >= P_B(f;c_l,d_l) at four CP corners.
Maximize s A0 +(1-s)sum_j w_j r_j−B0 over 0<=f<=1. This is a RELAXATION (hence UPPER bound) of max L(f), not a finite-grid lower certificate.

A nominal SciPy/HiGHS LP produces U≈.0391552880962453. The LP solution alone is NOT treated as mathematical evidence. Instead provide an explicit **nine-support nonnegative multiplier vector** for nine of the 2856 inequalities (indices refer to the fully documented row-generation order):

| Scenario row index | Nonnegative multiplier |
|---:|---:|
| 352 | 0.59865630037427 |
| 1008 | 0.19866360804043 |
| 1094 | 0.03268637935457 |
| 1199 | 0.13505239279759 |
| 2813 | 0.00628943749796 |
| 2833 | 0.00698826388663 |
| 2844 | 0.00510105283038 |
| 2845 | 0.01656256521816 |
| 2855 | 1.00000000000000 |

Write the relaxation in maximizing form max c^T x subject to A x<=0, 0<=x<=1 with 14 decision variables (nine scores, A0, three reset floors, B0). For ANY nonnegative multipliers lambda, weak duality directly yields

  c^T x <=sum_(k=1)^14 max{0, c_k−(A^T lambda)_k}.       (R31.7)

This does **not** require exact LP dual optimality or KKT stationarity. Evaluating just the nine selected rows with 45-decimal mpmath.iv directed intervals, the original 8-dimensional unitary source A, CP endpoint bounds, analytic reset-corner probabilities and 120-term controlled Lindblad source B, inflating B series remainder by 1e−40, gives the INDEPENDENT result

  sup_(all 12 pointwise scores) L(f)
      <= sup_(9 symmetric scores) L(f)
      <= 0.039155288096258 < **0.039156**.             (R31.8)

Our rational test lower bound from (R31.6) equals
 L(f_R31) >=.3106993896688963−.27161358975207756
          =0.03908579991681876.

Combining the independent primal and finite-support dual certificates:
  0.03908579991681876 <= max_f L(f) <0.039156,
or relative to the MORE PRECISE computed upper .039155288096258,
  L(f_R31) / max_f L(f) >=0.9982253.

**Exactly scoped interpretation:** the rational candidate achieves at least 99.82% of the mathematically defined conservative, independent-nuisance, one-pair **affine-source contrast functional L**. This is NOT an optimum of the full physical experiment under a shared detector c,d, not of expected log evidence for all e-factors, not of total experiment time or of LOCC. The dual computation is independent of R31's 7001-node global LOWER proof; it only uses nine physically allowable FINITE support sources to certify the UPPER. Scalar CP quantile rounding remains inherited from R26; the interval dual itself is checked from its given endpoints.

## 7. Independent checks, negative knowledge and governance

Full R31 local reproducibility consists of:
- one self-contained Python3+NumPy+SciPy+mpmath.iv 7001-node directed source-A proof, exact nuisance quadratic interpolation, global analytic detuning tail, exact reset-floor minimization, source B 120-term Lindblad, conditional binomial tails, and full-outcome e-factors;
- a second short Python implementation of the FINITE-SUPPORT interval-dual bound using only the complete first module's source model, WITHOUT trusting SciPy LP optimizer status;
- independent from both: a 2x2 complex unitary source-A and 4x4 continuous Lindblad source-B audit for nine Xi controls, plus dense nuisance tests. This audit caught and prevented a FALSE corner-only reset-floor shortcut for axis Z;
- separate 701-phase grid exploratory linear program, whose optimum is DESIGN-ONLY and whose frozen coefficients are subsequently audited by the independent global source proof;
- full stdout logs, hashes and a checksum manifest. The full bundle is exported as ZIP and all members are validated by exact SHA-256 and CRC.

Limits:
1. No new quantum controls, source or detector model, experimental data, external scientific referee, novelty or priority claim;
2. Source A still holds Xi fixed within an intact pair; the hazard must be conditional on current Xi/private axis, not merely past observations; source B increments remain independent;
3. CP beta special-function numerical inversion has outward buffers and independent binomial checks, not a certified arbitrary-precision interval implementation;
4. The 99.82% statement concerns the restricted L functional (conservative decomposition of CP and reset uncertainties), not an unrestricted minimax information projection or time-optimal device;
5. The 12-to-9 LOG-e theorem requires shot-swap closure of BOTH composite source families; source reset directional asymmetry, drift or history-dependent control can violate it;
6. A full two-sided all-alphabet test optimizing arbitrary positive e-factors for the true *joint* composite nuisance family remains open. An even shorter fixed-N test using all outcome data without the private coin is not established;
7. Original three-party single-copy unrestricted LOCC asymptotic closure issue from R09 remains OPEN. No mathematical result above transfers to it.

**Status:** PRF12_R31 / EXACT_12_TO_9_COMPOSITE_E_GROWTH_SYMMETRIZATION / RATIONAL_NINE_CATEGORY_SOURCE_CERTIFICATE / 7001_INTERVAL_ALL_XI_PASS / INDEPENDENT_NINE_SUPPORT_DUAL_UPPER_PASS / RESTRICTED_AFFINE_OBJECTIVE_99P82_PERCENT / FIXED_NONIID_N1666_K485 / INDEPENDENT_MATRIX_PASS / SOURCE_RESET_GUARDS_PRESERVED / REFEREE_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC / BW_INGEST_PENDING / ORIGINAL_3Q_LOCC_CLOSURE_OPEN.

**R32 target:** go beyond the L affine-certification objective: build real source-adapted, detector-nuisance composite-null e-factor optimization with exact all-real-Xi (including calibration), or obtain an anytime-valid finite-reference calibration confidence sequence with optional stopping that does not forfeit the source-wise error budget.
