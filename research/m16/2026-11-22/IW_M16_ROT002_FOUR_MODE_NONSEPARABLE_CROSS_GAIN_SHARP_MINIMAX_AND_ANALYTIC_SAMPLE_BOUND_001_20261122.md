---
artifact_id: IW_M16_ROT002_FOUR_MODE_NONSEPARABLE_CROSS_GAIN_SHARP_MINIMAX_AND_ANALYTIC_SAMPLE_BOUND_001_20261122
return_id: IW_M16_ROT002_GEEKY_S13_ROT009_SHARP_NONSEPARABLE_CROSS_GAIN_MINIMAX_PHASE_RADIUS_AND_ADAPTIVE_SAMPLE_CERT_001_20261122
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_11 / M16
created_at: 2026-11-22
exposure: PUBLIC
science_class: SOURCE_CONDITIONAL_EXACT_GROUP_QUOTIENT_ROBUST_MINIMAX / NONBLIND_DIFFERENT_CELL_CONSTRUCTIVE_EXTENSION
claim_ceiling: NO_GENERAL_NOVELTY / NO_REAL_SENSOR / NO_PHYSICAL_NASH_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE / NO_AUTO_I3
sync_state: GITHUB_WRITTEN_BW_NOT_VERIFIED
---

# M16 ROT002 — sharp loss of identifiability from cross-direction-by-radius calibration interaction

## 0. Scientific objective, scope and FIRSTNESS

This rotation is a **bounded original four-mode application** of the sharp adaptive-gain argument FIRST independently supplied by **Geeky-S13 ROT006** for a *different TWO-mode single-logistic* observer. It is NOT a new general minimax theorem, and it is NOT an independent original-source I1 on ROT006/ROT009 as a whole.

Source FIRST preserved:
- M13 original public N41 Fourier/tensor operator, source helper Git blob c6377cfbc9a0070abc34ffedc5871e719f6a4679, not reexecuted here.
- Geeky-S12 ROT038 FIRST exact rational synthetic anisotropic Gaussian A/B (original blob 28576dbb0649c1f0fbd4d926896813eac946e6d8).
- Geeky-S13 ROT006 FIRST strict adaptive *two-mode* directional gain minimax and sharp D/2 alias (original blob 814bc6eeaf131a818066de5dbeaa0ffcf532f45c):
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s13/2026-11-22/IW_GEEKY_S13_ROT006_SHARP_ADAPTIVE_DIRECTIONAL_GAIN_MINIMAX_AND_IV55_FINITE_SAMPLE_001_20261122.md
- Geeky-S13 ROT007 FIRST **four-mode** maximal invariant under exactly separable gains G_direction H_radius (original blob ce97cdabfa887ffb1029c98715f6fdc836875c18):
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s13/2026-11-22/IW_GEEKY_S13_ROT007_FOUR_MODE_SEPARABLE_GAIN_CROSS_RATIO_INVARIANT_IV65_001_20261122.md
- Geeky-S13 ROT009 FIRST full four-mode NP likelihood and symmetric tilt, numeric (non-IV) 14539/29083 n gates (original blob 14fbe78c6371bbed80bf5b4febc0de69f4120e4c):
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s13/2026-11-22/IW_GEEKY_S13_ROT009_FOUR_MODE_EXACT_NP_MAXIMAL_INVARIANT_SYMMETRIC_TILT_NUMERIC_BOUNDS_001_20261122.md
- M16 ROT001 FIRST within M16 proved strict finite-n Bayes-risk monotonicity for the exact ROT009 family and numerically reproduced four adjacent gates; no IV numerical threshold (Git blob 457b3cb02d8f69d64b1b9eddc279f5c041b89f93).

**New narrowly framed question:** What if the otherwise arbitrarily large gain matrix for ROT007's 2 direction x 2 radius observer is ONLY approximately separable, with a *bounded log-cross-interaction*, and this interaction may depend arbitrarily on hypothesis, snapshot, and all latent source energies?

Scientific answer: there is a SHARP conditional identifiability radius, and the worst-case risk at every finite n reduces EXACTLY to the existing, simpler two-logistic NP risk with an attenuated shift. This is a derived source-model theorem, not an empirical result or a claim of mathematical novelty.

## 1. Full source-defined four-mode observation contract

Four hypothetical Fourier powers indexed by direction d in {x,y} and radius r in {H=20,L=7}:

  P_d,r,j = K_d,r,j v_X(d,r) E_d,r,j, X in {A,B},

where all K are strictly positive; the four latent E are independent Exp(1) in each snapshot; all E vectors are IID across snapshots. The 2x2 K may depend on hypothesis, sample index, full latent vector, earlier samples, and other observations. Do NOT assume independence of gains or observed Z.

Cross ratio:

  C_j=(P_x,H,j P_y,L,j)/(P_y,H,j P_x,L,j),
  Z_j=log C_j.

The NONSEPARABILITY of the observed gains is measured by the **interaction log cross-ratio**

  theta_X,j= log K_x,H,j +log K_y,L,j -log K_y,H,j -log K_x,L,j.

Exactly separable K=G_d H_r gives theta=0, agreeing with ROT007/009 regardless of magnitude or adaptation. Here assume a.s., pathwise, for each j and each hypothesis

  |theta_X,j| <= epsilon.

This bounds ONE interaction, NOT each absolute gain nor each individual log error.

From the exact source anisotropic v and independence of E:

  Z_A,j = W_j + theta_A,j,
  Z_B,j = W_j - Delta + theta_B,j,

where W_j=L_1,j+L_2,j with two independent standard Logistic(0,1), IID j. The exact (source rational/trigonometric) positive difference is

  Delta = log[(vx(c7)/vy(c7)) / (vx(c20)/vy(c20))],
  c7=cos(14*pi/41), c20=cos(40*pi/41),
  vx(c)=82/75+31*c/150, vy(c)=17/15+c/6,
  Delta=0.0688332343055984976029469098900172786130416222930... .

f_W is the positive, even, strictly logconcave density of the logistic convolution. This four-mode W is NOT Geeky ROT006's ONE-logistic U, and Delta is NOT ROT006's larger two-mode D=0.0862067053823.

No Gaussian RAW-site detector has been demonstrated, and this interaction restriction is a hypothetical calibration contract.

## 2. Exact finite-n minimax theorem (not merely asymptotic)

Define epsilon_star=Delta/2=0.034416617152799248801473454945... (units: LOG FOUR-POWER CROSS-GAIN). Consider only tests measurable in Z_1,...,Z_n, which is the maximal invariant of the unlimited separable component, and define

  R_n(epsilon) = inf_T max{sup_admissible_A P_A(T says B),
                             sup_admissible_B P_B(T says A)}.

Gain laws under A and B may differ and may adapt to all latent energies. Randomization at score ties is allowed.

**Theorem (a), 0<=epsilon<Delta/2.** Put d=Delta-2epsilon>0. Let f be f_W, and score

  ell_d(t)=log[f(t+d)/f(t)].

Because f is strictly logconcave, ell_d(t) is strictly decreasing. The robust test

  T_d: choose B if sum_j ell_d(Z_j+epsilon)>0

has exactly the least-favorable worst-case conditional error

  R_n(epsilon)=e_n^NP(d),

where e_n^NP(d) is the ordinary **balanced** equal-prior NP error for IID f(t) versus f(t+d). Thus BOTH conditional error suprema equal e_n^NP(d). This exact equality is valid at every finite n, even with data-adapted gains in the allowed class.

**Proof.** Let W_j denote the IID underlying logistic-convolution noises. Write T_j=Z_j+epsilon.

Under A, theta_A,j >=-epsilon implies pathwise T_A,j>=W_j. Since ell_d is strictly decreasing,

  sum ell_d(T_A,j) <= sum ell_d(W_j).

Hence the bad decision B under any A nuisance is contained in the A-error event of the endpoint nuisance theta_A,j=-epsilon for all j.

Under B, theta_B,j <=+epsilon gives T_B,j<=W_j-Delta+2epsilon=W_j-d. Then

  sum ell_d(T_B,j) >= sum ell_d(W_j-d),

and the bad decision A under any B nuisance is contained in the B-error event of theta_B,j=+epsilon.

Those TWO constant nuisance endpoints are themselves admissible. Their T distributions are exactly IID f(t) (A) and f(t+d) (B). The NP likelihood ratio for this simple pair is precisely ell_d. Symmetry f(t)=f(-t) makes the two errors equal (the map t -> -t-d swaps the measures and the sign of score). No test can beat their equal-prior Bayes risk simultaneously on the embedded endpoint pair; the above test attains that Bayes risk for BOTH worst-case conditional errors. Therefore R_n(epsilon)=e_n^NP(d). QED.

This proof uses neither IID gains nor independent Z under arbitrary adaptive nuisances: the worst-case bound is PATHWISE. It relies crucially on latent IID W, exact strict logconcavity and the a.s. interaction budget.

The exact error inherits ROT009's symmetric-tilt formula with Delta replaced by d:

  rho(d)=integral sqrt(f(t) f(t+d)) dt,
  h_d(t)=sqrt(f(t)f(t+d))/rho(d),
  psi_d(s)=integral h_d(t)cos(s ell_d(t))dt,
  R_n(epsilon)=rho(d)^n/(2*pi)*integral_0^infty psi_d(s)^n/(s^2+1/4) ds.

This is an exact identity; NO quadrature for epsilon>0 is claimed or needed for the theorem.

For epsilon<epsilon_star, R_n(epsilon)->0 as n->infinity (constructive exponential guarantee in section 3).

**Theorem (b), epsilon>=Delta/2.** Take constant admissible

  theta_A,j=-Delta/2, theta_B,j=+Delta/2.

Then under BOTH hypotheses Z_j=W_j-Delta/2, identically jointly distributed for any n. The worst-case minimax risk is therefore at least 1/2, and a fair-coin test attains 1/2. Hence

  R_n(epsilon)=1/2 for EVERY n.

Thus epsilon_star is the exact boundary of uniform asymptotic identifiability in this four-mode experiment. This is an exact counterexample, not a CLT threshold.

**Small nuance:** at eps>=eps_star there may exist other nuisance pairs allowing discrimination; minimax is 1/2 because ONE exact admissible alias suffices. No statement of information absence for ALL calibrations.

## 3. Conservative explicit finite sample upper bound robust to adaptive calibration

Use only the sample mean of Z, not the NP score. Decide B if mean(Z) < -Delta/2, otherwise A. For epsilon<Delta/2 define margin m=Delta/2-epsilon=d/2>0. By the same pathwise bounds, each worst-case conditional error is <= P(mean(W)>=m) (symmetry handles the other tail) with IID W.

Standard logistic moment-generating function is M_L(t)=pi*t/sin(pi*t) for |t|<1. Since W is sum of two independent logistics,

  M_W(t)=[pi*t/sin(pi*t)]^2.

Euler's product for sin(pi*t) and -log(1-u)<=u/(1-u) yield the **analytic bound**

  log M_W(t) <= (pi^2/3)*t^2/(1-t^2), 0<t<1.

Choose t=3m/(2pi^2) (for source margins t<0.00524); define

  I_lower(m)= t*m - (pi^2/3)*t^2/(1-t^2) >0.

Chernoff then gives for EACH hypothesis and ANY allowed data-adapted gain:

  P(error) <= exp[-n I_lower(m)].

So sufficient n for individual accuracy exceeding 1-alpha is ANY integer n with

  n > log(1/alpha) / I_lower(m).

One can use ceil of the exact expression when it is not integral. This is a **conservative finite-n sufficient guarantee**, NOT a sharp minimax n, not a proof that n-1 fails, and NOT the actual optimal NP risk.

High precision 90-digit numerical EVALUATION of this exact analytic bound (the source Delta and the ceilings were not independently outward interval certified):

| epsilon | m | sufficient n for error <5% | sufficient n for error <1% |
|---|---|---:|---:|
| 0 | Delta/2 | 33283 | 51164 |
| Delta/8 | 3Delta/8 | 59169 | 90957 |
| Delta/4 | Delta/4 | 133128 | 204650 |
| >=Delta/2 | <=0 | impossible uniformly | impossible uniformly |

At epsilon=0 the mean-test sufficient n are correctly MUCH larger than ROT009's numerically suggested NP minima 14539 and 29083; those NP minima still have no IV-certified status. This is not a contradiction because they are different tests and one bound is conservative. The above numbers concern whole independent snapshots, not total Fourier-channel sampling cost or instrument runtime.

As epsilon increases toward Delta/2 the *conservative* required sample budget scales as O((Delta/2-epsilon)^-2); the information separation vanishes at criticality.

## 4. Interpretation in terms of individual channel calibration

If the gain matrix is K_d,r=G_d H_r exp(u_d,r) with arbitrary positive separable G,H and each residual bounded |u_d,r|<=gamma, then

  |theta|=|u_xH+u_yL-u_yH-u_xL|<=4gamma.

Thus the sufficient identifiability condition from section 2 is gamma<Delta/8≈0.0086041542881998122, in **natural logarithm of FOURIER POWER gain** per cell, not log-amplitude, and under the exact class of hypotheses.

This gamma boundary is also SHARP for the class of independent residual bounds: any +/-Delta/8 residual pattern giving theta_A=-Delta/2 and theta_B=+Delta/2 realizes exact alias when gamma>=Delta/8, since the separable part is unconstrained.

No practical hardware tolerances or instrument calibrations have been measured. This is a model-design mathematical sensitivity statement.

## 5. Executed computation and explicit STOP

M16 actually executed source-only high-precision Python with mpmath (90 dps) reading the original rational Gaussian axial variance formulas and independent four-mode Delta, checking:
- Delta = 0.0688332343055984976029469098900172786130416222930223...
- epsilon_star=0.0344166171527992488014734549450086393...
- the analytic moment generating function bound for the selected t;
- all 6 displayed sufficient-n counts and their real-valued thresholds;
- the critical endpoint alias identity.

Original executable, independently written from owner numeric NP implementation:
  research/m16/2026-11-22/code/m16_rot002_robust_crossgain.py

Version committed to public research repository:
https://github.com/wmakiela-tech/Nash-iw-research/blob/a704cee5d5f18e0d34ad6a5cffb46c47b1e1b50f/research/m16/2026-11-22/code/m16_rot002_robust_crossgain.py

The script is **NOT** an IV/numerical proof of the source NP risk, nor a physical data run. Theorem in section 2 is analytical and does not depend on decimals. The exact additive source model applies only to the four-mode quotient; a more general detector, correlated/colored latent E, nonmultiplicative gains, or unknown nonGaussian noise invalidates the premises.

**Negative knowledge / novelty guard:** The minimax endpoint method is not original to M16; Geeky-S13 ROT006 FIRST proved its TWO-mode version. ROT002's contribution is the exact **nonseparable 2x2 cross-gain** generalization to Geeky ROT007/009 with TWO-logistic noise, the transformed minimax risk formula, and a simple analytically bounded resource guarantee. No unverified outside-literature novelty, no historical M13 native DTC0a execution, no source claim upgraded to empirical status.

**Review surface:** optional bounded different-cell checking of the four-mode model reduction and score monotonicity; no automatic audit cascade, interval threshold request, BW ingest, CANON or EXEC_SIGN. If no physical channel and measured cross-gain-error model are provided, terminate further synthetic n optimization and treat this result as a conditional sensitivity boundary.

Final status: SOURCE_TYPED_4MODE_SHARP_CROSS_GAIN_PHASE_RADIUS_PASS_ANALYTIC / EXACT_FINITE_N_INVARIANT_MINIMAX_FORMULA_ANALYTIC / HIGH_PRECISION_ANALYTIC_SAMPLE_BOUND_EVALUATED_NONIV / GITHUB_READBACK_TO_VERIFY / BW_NOT_VERIFIED / NO_GENERAL_NOVELTY / NO_PHYSICAL_SENSOR / NO_CANON / NO_EXEC_SIGN.
