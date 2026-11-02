---
artifact_id: IW_PRF12_R28_SIGNED_QUARTET_GLOBAL_XI_AND_NONIID_CERTIFICATE_001_20261102
created_at: 2026-11-02
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_SIGNED_QUARTET_STOCHASTIC_BIT / ALL_REAL_XI_INTERVAL_TAIL_PASS / FINITE_CP_CONFIDENCE / NONIID_BINOMIAL_PASS / INDEPENDENT_DENSITY_AUDIT_PASS / REFEREE_PENDING
claim_ceiling: NO_UNRESTRICTED_MULTINOMIAL_OPTIMALITY / NO_EMPIRICAL_HARDWARE / NO_PRIORITY / NO_CANON / NO_EXEC / ORIGINAL_SINGLE_COPY_THREE_QUBIT_LOCC_CLOSURE_OPEN
---

# PRF12 R28 — Signed quartet source test with robust finite calibration and non-iid source dynamics

**Main result (2026-11-02).** R27 used a coarse single bit that records equality of two destructive sensor readouts. R28 retains the SAME physical source-on rectangular pulse model, the SAME axis weights, the SAME SYNTHETIC finite calibration and the SAME hidden-Xi survival contract, but uses the two agreement SIGNS separately. A private classical coin maps each observed (axis, two signs) quartet to a new binary result. A globally all-real-Xi and detector-calibration-robust lower bound allows **2251 science pairs** with each science error <4%, versus R27's **8497 science pairs** with the same target. Total single-sensor readouts (calibration included): **119502** versus R27 **131994**. This is a constructive SUFFICIENT comparison, NOT optimization over the entire multinomial experiment.

## 0. Source contract and mature-host subtraction

Internal lineages: PRF11 R35 source A static Cauchy within intact runs versus source B independent-increment Cauchy-Lévy; PRF12 R23 finite Y preparation, free sensing, finite X/Y analysis and terminal Z projectors with \Omega_max/\gamma=10, \gamma\Delta=.5, (w_X,w_Y,w_Z)=(.18,.20,.62); R24/R25 finite detector and exogenous mid-shot source-reset hazard; R26 finite fixed-size Clopper-Pearson calibration; R27 full quartet conditional law and non-iid raw parity.

As in R27, A's hidden Xi stays identically fixed during BOTH fresh preparations and readouts inside each *intact* two-shot pair. Between pairs Xi may be arbitrarily dependent, even constant through all pairs. A source reset MAY occur during the pair; its no-reset probability must be at least s=exp(-\lambda L) **conditionally on the CURRENT hidden Xi, the privately selected axis, and all hazard-relevant latent variables**, or come from an independent exogenous Poisson clock. Merely conditioning on prior observed events is insufficient (R25 owner correction). \lambda/\gamma=.02, \gamma L=1.7783185307179588, s=.9650586805668616. In reset intervals, each pre-detector Bloch Z mean may vary arbitrarily in [-1,1], but fresh sensor readout results and independently generated private coins are conditionally independent given the full exogenous latent trajectory.

Source B still uses the finite source-ACTIVE Lindblad generator \gamma(Ad_Z-I)/2 during ALL pulses and free intervals; do not approximate it by static frequency for a pulse.

Known mature hosts: randomised Pauli measurements and nonlinear functionals (Physics Reports 1095, 2024, doi:10.1016/j.physrep.2024.09.009); exact fixed-size binomial confidence intervals Clopper-Pearson (1934); robust composite hypothesis and classical randomised binary decision rules. NO novelty or first-publication claim.

## 1. R28.1 — Exact signed quartet and implementable new Bernoulli bit

Let axis j be picked privately with weights (.18,.20,.62) for X,Y,Z. For either source, conditional on a shared Bloch mean m_j of each of two freshly re-prepared shots, the recorded detector mean is u_j=c*m_j+d, and

  P_j(r1,r2 | u_j) = (1+r1*u_j)(1+r2*u_j)/4,
  r1,r2 in {+1,-1}.

Here effective c,d already include R25's terminal T1 and asymmetric label assignment, assumed stable across the two shots and independent across readouts conditional on their latent trajectories.

When the observed signs are (++), generate private binary Y=1 with probability alpha_j; when (--), generate Y=1 with probability beta_j; on (+-) or (-+), generate Y=0. This produces a TRUE Bernoulli output; merely treating an expected score as a Bernoulli sample without the coin would be invalid.

| Axis j | alpha_j for ++ | beta_j for -- | mixed outcomes |
|---|---:|---:|---:|
| X | 0.94 | 1.00 | 0 |
| Y | 0.88 | 0.96 | 0 |
| Z | 0.36 | 0.02 | 0 |

Thus for intact source A, or for each independent source B shot pair,

  F_j(u) = [alpha_j(1+u)^2+beta_j(1-u)^2]/4.              (R28.1)

Unlike R27's raw parity (alpha=beta=1), R28 uses the sign of an agreement. No new quantum drive, preparation, memory or entanglement is needed; the additional resource is a private classical coin and retaining the two signed outcomes.

A finite-grid nominal 12-coefficient linear programme gave a design separation ≈.04142, but the coefficients displayed above are deliberately simplified RATIONAL design values; no claim that the finite-grid LP optimum is globally attainable or globally optimal under all Xi and calibration sets. The SCIENTIFIC theorem below rests on independently quantifying those fixed rational coefficients.

## 2. R28.2 — Real-axis bound with finite CP detector calibration

R26's explicitly SYNTHETIC counts (n0,K0,n1,K1)=(46000,45540,69000,3705) yield two separate exact two-sided CP intervals at individual failure probability .005, i.e. simultaneous coverage >=.99. For effective detector parameters,

 c in [.932477929662237,.939937817637063],
 d in [.039941802242004,.047401690216830],

where numerical beta quantiles are inflated outward by 1e-12 and independently checked with binomial tails. The CP beta inversion is NOT itself fully formal directed-rounding software.

Source B Bloch Z means from the finite source-active X/Y rectangular Lindblad evolution:

  m_B=(.5219734434954134,.00231335785212866,.04809737884883814),

and robustly maximizing the new signed score over the CP rectangle with an outward 1e-12 margin yields

  p_B(Y=1) <= 0.271868146204745.                          (R28.2)

For a fixed static Xi, take finite Y state preparation, free Z evolution of duration .5/gamma and finite X/Y analysis pulses of duration pi/(20 gamma) with source STILL active. With a 7001-node mpmath.iv directed interval source-A evaluation on Xi ∈[-35,35] at .01 spacing, the smallest certified node score is

  min_node >=.31813254074121566  (near Xi=-4.10).

Node checking ALONE does not certify a continuum. By Duhamel the output Bloch coordinate satisfies |dm_j/dXi|<=T_shot=.5+pi/10 and the derivative of F_j with respect to m_j has absolute value at most c_hi max(alpha_j,beta_j). The weighted total score therefore has Lipschitz bound

  L<=.455482206255474.

The maximum distance to a node is .005, so the compact interval certificate is

  p_A(Y=1|Xi, intact)>=.3158551297099383 for |Xi|<=35.

For |Xi|>=35, a source-active rectangular pulse has off-resonant spin-flip amplitude at most Omega/sqrt(Xi^2+Omega^2). Let f<=100/(35^2+100), then m_AX,m_AY >=1-8f and m_AZ>=1-2f; these bounds are derived via amplitude addition for up to two finite pulses. Every F_j is convex in u_j and its minimizer lies BELOW the permitted positive tail interval, giving the independent analytic tail certificate

  p_A(Y=1|Xi,intact)>=.3911654505439207 for |Xi|>=35.

Combining compact interval and unbounded tails yields the **ALL REAL Xi** no-reset bound

  p_A(Y=1|Xi,intact)>=.3158551297099383.                (R28.3)

No integration over the Cauchy prior is used in this A certificate; it applies even to persistent adversarially chosen static Xi so long as the reset/sampling contract holds. Intervals certify the main compact quantum dependence. Outward scalar buffers and independent numerical matrix checks are not a fully machine-formal proof of floating-point special functions.

## 3. R28.3 — Arbitrary intra-pair source jumps, with conditional survival

If a reset happens within a pair, let the ideal detector means of two shots be m1,m2∈[-1,1] with u1=c*m1+d, u2=c*m2+d. For the new Bernoulli bit,

  G_j(u1,u2)=alpha_j(1+u1)(1+u2)/4+
             beta_j(1-u1)(1-u2)/4.                       (R28.4)

The two-shot score is BILINEAR in m1,m2. Its minimum on the square [-1,1]^2 is attained at one of the four corners (m1,m2)∈{±1}². Evaluating all four with the full CP c,d rectangle gives conservative source-reset floors

  r_X>=.05232020886947945,
  r_Y>=.04912280145267879,
  r_Z>=.01787181488996674.

The weighted floor is r>=.03032272311882144. With conditional survival s=.9650586805668616, the source-A mean is bounded, EVEN with arbitrary dependence among Xi values between pairs, by

  p_A(Y=1|full relevant past)
    >= s*.3158551297099383 +(1-s)*.03032272311882144
    >= **.30587825068272534**.                          (R28.5)

The survival assumption must hold at the latent level, including the chosen axis and Xi; it cannot be inferred from marginal or observable-past survival alone. The different shots are conditionally independent given complete trajectories and private randomness. If the detector drifts, if resets target current Xi without the conditional bound, or if cross-shot correlated measurement errors occur, this theorem does NOT apply.

## 4. R28.4 — Non-iid exact binomial and anytime errors

Take conservative transparent limits a=.3055 and b=.2720, which are respectively below (R28.5) and above (R28.2). The pair outcome Y is genuinely Bernoulli by the additional independent coin. For every pair under source A, conditional on all previous measurements and latent history allowed by the contract, Pr(Y=1)>=a. Under B, conditional Pr(Y=1)<=b. Thus arbitrary NON-IID hidden Xi does not prevent binomial stochastic domination of the accumulated count K_N.

For N=2251, choose source A iff K_N>=650. Exact binomial tails certify

  Pr_A(declare B | successful calibration)
    <= BinomCDF(649;2251,.3055)=.03976608161349547,

  Pr_B(declare A | successful calibration)
    <= BinomSF(649;2251,.272)=.039543061132522324.

Adding the <=.01 calibration confidence failure to the <=.04 scientific decision error bounds gives each source a familywise wrong-declaration limit <=.05. This is NOT a guarantee of conclusive calibration for arbitrary count data. The example counts are SYNTHETIC, NOT experimental.

For optional stopping of the SCIENCE series after FIXED-SIZE calibration define

  M_n^A=(a/b)^{K_n}[(1-a)/(1-b)]^{n-K_n},
  M_n^B=(b/a)^{K_n}[(1-b)/(1-a)]^{n-K_n}.

The first is a nonnegative supermartingale under composite B-null p<=b, the second under composite A-null p>=a. Threshold 25 bounds the respective probability of a false crossing by at most .04, and the CP failure budget retains the total .05. This does NOT justify optionally stopping reference calibration; an anytime-valid calibration set is a separate research task.

## 5. Reproducibility, clock comparison, and negative knowledge

| Same source and detector model | R27 raw parity | R28 signed Bernoulli |
|---|---:|---:|
| Synthetic CP calibration reads | 115000 | 115000 |
| Science pairs | 8497 | **2251** |
| Science sensor readouts | 16994 | 4502 |
| All sensor readouts | 131994 | **119502** |
| Total gamma*wall time (reference read=.1/gamma) | 27035.2226 | **15615.5450** |

The net reduction is 73.51% of science pairs, 9.46% of all readouts and 42.24% of this explicitly modeled wall time. This does NOT establish a global minimax test or a real hardware speedup.

Reproducibility within conversation ZIP contains:
- full standalone NumPy+SciPy+mpmath.iv 7001-point interval/analytic-tail proof and exact binomial threshold;
- independent 2x2 complex A matrix evolution and 4x4 Lindblad B evolution, reconstructing the quartet probabilities for nine hidden Xi values;
- separate exploratory finite-grid linear programme, explicitly DESIGN-ONLY;
- output logs and SHA256 member manifest.
The shortened public GitHub mirror may cover only the quantitative core; the ZIP carries the full standalone certificate.

**Claim guard:** NO_CANON, NO_EXEC, NO priority/novelty, NO full four-category minimax optimality, NO physical detector data, NO result about the unrestricted single-copy three-qubit LOCC closure (still OPEN following R09 correction), and BW ingest plus independent referee still PENDING.

**Next R29:** optimize over signed-axis multicategory test processes with a proper composite-null confidence set; improve confidence sets for detector nuisance parameters using an empirical all-outcome calibration and conditional e-processes, without assuming iid Xi or resetting source inside an intact pair.
