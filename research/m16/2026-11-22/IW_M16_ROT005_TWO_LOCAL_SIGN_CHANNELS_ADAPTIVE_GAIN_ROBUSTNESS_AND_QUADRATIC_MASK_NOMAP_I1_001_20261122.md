---
artifact_id: IW_M16_ROT005_TWO_LOCAL_SIGN_CHANNELS_ADAPTIVE_GAIN_ROBUSTNESS_AND_QUADRATIC_MASK_NOMAP_I1_001_20261122
return_id: IW_M16_ROT005_TWO_SITE_SIGN_ARCSINE_CALIBRATION_INVARIANT_ALTERNATIVE_AND_ROT012_QUADRATIC_MASK_ORBIT_NOMAP_001_20261122
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_11 / M16
created_at: 2026-11-22
exposure: PUBLIC
science_class: SOURCE_CONDITIONAL_EXACT_TWO_SITE_GAUSSIAN_SIGN_INVARIANT_AND_FULL_SUPPORT_QUADRATIC_OBSERVER_NO_MAP
status: SOURCE_ANALYTIC_PASS / EXECUTED_MPMATH90_NUMPY_FULL_41CUBED_SYNTHETIC_TESTS / NO_OUTSIDE_I3
sync_state: PUBLIC_SOURCE_GITHUB / BW_INGEST_NOT_VERIFIED
claim_ceiling: NO_GENERAL_MATHEMATICAL_NOVELTY / NO_REAL_SITE_SENSOR / NO_REAL_IID_NOISE / NO_HISTORICAL_DTC0A / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE
---

# M16 ROT005 — minimal two signed-site statistical contrast, and direct no-map for cubic quadratic masks

## 0. Target, currentness and prior work retained

Moderator-directed research program asks for external relevance and an actual observation interface, not indefinite synthetic NP sample-count shaving. An adjacent same-day Geeky-S13 ROT012 directly establishes that the ORIGINAL M13 six cubic aggregate outputs (unmasked k=0 and five masks k=2..6) cannot reconstruct the FOUR hypothetical Fourier powers, using an exact positive pair with equal source geometric masks but Fourier ratios 1 and 9, plus a Gaussian sine-mode conditional argument for LINEAR source mask noise. ROT012 was DIRECTLY READ at source Git blob 16ea5df956eb51ff9b010f2e97e5845f4d614a7b:
https://github.com/wmakiela-tech/Nash-iw-research/blob/7d895f8b62a5058109e557ea0e3f4521849c469b/research/geeky-s13/2026-11-22/IW_GEEKY_S13_ROT012_ORIGINAL_M13_SIX_MASK_FOURIER_OBSERVABILITY_NOGO_001_20261122.md

Firstness: M13 original five TT tensor RMS and source geometry FIRST. M13 ROT29/ROT31 FIRST various exact non-identifiability witnesses. Geeky-S12 ROT038 FIRST source exact rational synthetic anisotropic Gaussian 8-neighbor covariance models A/B, old-nine LINEAR observer full-law alias and new boundary contrast Z3. Geeky-S13 ROT007 FIRST direction-times-radius gain-invariant four-mode contrast; ROT009 exact NP; ROT010 first author IV75 n thresholds; ROT011 N>=17 source-geometric portability; ROT012 first six-original-mask-to-Fourier exact positive field nonrecoverability. M16 ROT004 FIRST a DIFFERENT quadratic scalar noise-only mask-law orbit alias comparing original source B versus its x/y permuted sibling Bpi, Git blob 2e2b1194a96b7001a66887aea7fb60cdf9fe40c5. Nothing in this ROT005 transfers priority of those results.

**New bounded question**: Can ONE additional tiny, direction-labelled local SIGN measurement class, requiring just TWO centered site values rather than four full Fourier powers, distinguish source B from Bpi under completely unknown, even data-adaptive POSITIVE gains? What is a valid finite-n guarantee? Can the previous mask-Fourier no-map be stated also for the NONLINEAR quadratic scalar site-noise masks without incorrectly using ROT012's independence proof for LINEAR regional Gaussian averages?

The answers are mathematical and source-conditional, not real instrument engineering. Classical Gaussian orthant probability / arcsin identity is mature: e.g. peer-reviewed reference https://link.springer.com/article/10.1007/s11336-020-09730-5 ; no external novelty claim.

## 1. Two exact rational synthetic site-noise hypotheses

Work on the ORIGINAL N=41 periodic cube, 41^3=68921 sites, with the exact synthetic Gaussian covariance family FIRST in ROT038:

 Sigma_beta = beta0 I + beta_x (T_x+T_-x)/2
            + beta_y (T_y+T_-y)/2 + beta_z (T_z+T_-z)/2
            + beta_xy A_xy + beta_xz A_xz + beta_yz A_yz + beta_body A_body.

Original ROT038 B source coefficients ordered (beta0,betax,betay,betaz,betaxy,betaxz,betayz,betabody) are exactly

 B=(1,1/20,3/100,1/25,1/30,13/300,7/300,2/25).

M16 ROT004's NEW legal x/y permuted hypothesis is

 Bpi=(1,3/100,1/20,1/25,1/30,7/300,13/300,2/25).

Both neighbor weights sum EXACTLY to 3/10; all periodic eigenvalues satisfy >=7/10, so both centered site Gaussian laws are nondegenerate and have everywhere strictly positive densities in full R^68921. These are NOT the original ROT038 comparison pair A vs B. Nothing here asserts that the noise covariance has ever been observed in a physical device.

Fix ONE source site v and its adjacent site v+e_x. Let X0=X(v), X1=X(v+e_x). Their marginal variances are both beta0=1. At displacement e_x the seven other normalized one-step neighbor operators have zero kernel value (N41 prevents coordinate aliasing). Hence exactly

 Corr_B(X0,X1)=Cov_B(X0,X1)=beta_x(B)/2 =1/40,
 Corr_Bpi(X0,X1)=beta_x(Bpi)/2=3/200.

This is source-exact rational, not a fitted parameter.

## 2. Two-site sign-concordance discriminates and cancels arbitrary positive per-channel gain

Define a single Bernoulli readout

 Y_j = 1{ tilde_X_0,j * tilde_X_1,j > 0 }.

The two noisy centered signed readouts may be transformed by independently varying positive calibrations

 tilde_X_0,j=g_0,j(X,history,hypothesis) X_0,j,
 tilde_X_1,j=g_1,j(X,history,hypothesis) X_1,j,

with EACH g>0 a.s., no scale bound, and arbitrary adaptivity to all latent site noise, previous shots and hypothesis. Pathwise

 1{tilde_X_0 tilde_X_1>0}=1{X_0 X_1>0}

for every nonzero pair. Gaussian zero probability ensures no tie. Therefore the resulting Y_j remain IID Bernoulli across IID latent GAUSSIAN FULL-SITE snapshots even though gains may be arbitrarily correlated, adaptive, and different between hypotheses. The reading consumes only TWO signed centered site values, not 2 Fourier energy channels or a full 41^3-site snapshot.

For centered bivariate unit-variance Gaussian correlation rho, classical exactly proven orthant identity

 Pr(X0>0,X1>0)=1/4+arcsin(rho)/(2*pi)

gives

  Pr(Y=1)=1/2+arcsin(rho)/pi.

Thus EXACT:

 p_B = 1/2+arcsin(1/40)/pi
     =0.5079585763198139302157494652822360...,

 p_Bpi=1/2+arcsin(3/200)/pi
     =0.5047748273601990095203394247002263...,

 delta_p = p_B-p_Bpi
     =0.00318374895961492069541004058200969735... >0.

This establishes genuine source-model identifiability with only two signed site measurements: the two Bernoulli source laws differ. It is weak information; NOT a precise measurement guarantee or evidence for real detectors.

**One-site standalone no-go:** Under both hypotheses a single original centered raw site has exactly Gaussian N(0,1) law; all single-site tests without other channels have equal-prior optimal success 1/2. Thus TWO is minimum in the specific design class of standalone RAW signed site values. This is NOT a theorem that adding ONE site to the EXISTING six old masks can never help, and is not a minimum over all other observations/instruments.

**Critical physical caveat:** sign requires access to the SIGN of a *centered additive-noise residual*, not to nonnegative total site ENERGY or squared RMS. If the instrument adds unknown offsets, unknown nonzero source means or saturations BEFORE taking signs, invariance and the exact probabilities may fail. The positive gain cancellation only applies to multiplicative positive scaling of those centered signed quantities. Gaussianity and IID source snapshots remain unverified.

## 3. Explicit source-conditional conservative finite-n guarantee

Observe IID Y_1..Y_n under the exact model and set threshold

 t=(p_B+p_Bpi)/2=0.50636670184000646986804444499123118797...

Decide B if empirical mean Y >t, else Bpi. In either model the true Bernoulli expectation is at distance delta_p/2 from t. Hoeffding's bounded-independent-variable inequality supplies for EACH conditional error

  P(error) <= exp[-2n*(delta_p/2)^2]=exp[-n*delta_p^2/2].

Therefore a sufficient condition for strict >1-alpha accuracy under each hypothesis is

 n > 2 log(1/alpha)/delta_p^2.

90-digit mpmath actual evaluation, with analytic formula exact before decimal reporting:

| Target | lower real sufficient bound | first INTEGER n satisfying this CONSERVATIVE bound | guaranteed error upper |
|---|---:|---:|---:|
| error <0.05 | 591092.381369051785... | **591093** | 0.0499998432351820... |
| error <0.01 | 908652.964711067318... | **908653** | 0.00999999821151163... |

This is the first n satisfying THIS EXACT HOEFFDING UPPER BOUND, not a claim of first n for the actual binomial test nor any NP-optimal test. It is deliberately expensive in repeated snapshots because delta_p is small. A completely specified binomial likelihood could give better sample numbers, but optimizing them absent a genuine site-sign detector is not scientifically justified.

An arbitrary positive per-site gain does NOT require a correction term in this sign-only finite-n guarantee. Nonpositive gains or additive offsets destroy the pathwise argument. The test is not robust to arbitrary non-Gaussian latent law with only a covariance specified.

## 4. Strong direct no-map for QUADRATIC cubic-mask site-noise readings

ROT012 proved an exact source six-mask no-map for positive SCALAR FIELDS' LINEAR means and a Gaussian SIN-CHANNEL independence result for LINEAR region averages; DO NOT silently extend that statistical independence proof to NONLINEAR mask energies. M16 ROT004 separately addressed the new QUADRATIC-noise mask law.

We now make a **stronger full-support almost-sure theorem** in the ROT004 quadratic mask host. Let

 M_k(x)=|Omega_k|^-1 sum_{v in Omega_k} x(v)^2,  k=2..6,
 M_0(x)=41^-3 sum_v x(v)^2,

with Omega_k the original M13 cube masks. Each M_k is axis-swap EVEN: M(Ux)=M(x) for spatial x/y permutation U. The raw four-mode Fourier power cross ratio C(x)>0, defined almost everywhere where the four Fourier coefficients are nonzero, is axis-swap ODD in the multiplicative sense:

 C(Ux)=1/C(x).

**Theorem:** Under EITHER source B or Bpi nondegenerate centered stationary Gaussian site field, there exists NO measurable function g such that C(X)=g(M(X)) almost surely. This includes ALL SIX quadratic masks (full and k2..6), not merely the five masked ones. In fact it holds for any full-dimensional field probability measure P such that P and its axis-swapped pushforward U_*P are equivalent and C is not almost surely 1.

**Proof.** Each strict-SPD Gaussian field law P has positive Lebesgue density on the entire finite-dimensional R^68921. Its axis-swapped pushforward U_*P also has such a positive density; therefore P and U_*P are mutually absolutely continuous. Suppose C(x)=g(M(x)) for P-almost every x. By equivalence, this SAME relation holds U_*P-almost everywhere as well. Consequently, for P-almost every x,

 C(Ux)=g(M(Ux))=g(M(x))=C(x).

But C(Ux)=1/C(x) by definition. Hence C(x)=1 P-a.s., contradicted by full support and nonconstancy of C: there exist open sets of fields where C is well-defined and !=1, as shown by explicit exact source mode amplitudes below. QED.

**Independent strictly positive constructed witness** reusing Geeky ROT012's F2 with proper firstness attribution:

 F(u)=1+(1/25)[(3/2)cos(2pi20 u_x/41)+(1/2)cos(2pi20 u_y/41)
              + cos(2pi7 u_x/41)+ cos(2pi7 u_y/41)].

F>=21/25>0, and Fpi=U F is equally positive. For SIX QUADRATIC masks M_k(F)=M_k(Fpi) PATHWISE because geometry is invariant, but by orthogonality of the N41 DFT:

 C(F)=9, C(Fpi)=1/9 EXACTLY.

This is not ROT012's original F1 vs F2 **LINEAR** mask comparison. It is a different pair F2 vs swapped F2 that works for QUADRATIC masks, and supports the full-support almost-sure no-map above. Numeric grid actual check: all six mean-square mask differences 0 at binary64 and FFT C≈9.000000000000004 and 0.11111111111111165. The two source fields are NOT original M13 deterministic tensor solutions.

**Important distinction from source observation:** none of these arguments implies that actual deterministic M13 tensor residual samples are Gaussian site scalar fields. Their five masked tensor squared norms are genuinely different measurement functions; no historical M13 native DTC0a telemetry, real noise-centering, or instrumental access to X(v) has been established.

## 5. Actual reproducibility and external literature sanity

An independently authored Python executable, source model formulas as exact Fraction, mpmath 90 decimal digits, NumPy FFT on all 68921 sites, was ACTUALLY run locally, with outputs:

- exact rational SPD coefficient sums B=Bpi=3/10 and neighbor correlations 1/40,3/200 PASS;
- bivariate Gaussian same-sign arcsin formula independently verified by 90-digit direct numerical 1D integration of standard-normal pdf/CDF; both deviations <1e-55;
- both strict Hoeffding neighboring-integer gates PASS;
- 100000 randomly sampled pairs with separate nonlinear positive data-dependent gains: sign product pathwise identical in all 100000/100000;
- 41^3 deterministic strictly positive field F and axis swap: six quadratic masked energies exactly identical to numerical precision; Fourier power ratios 9 and 1/9;
- full-support almost-sure proof is mathematical, NOT inferred from a finite Monte Carlo.

Source repository executable file:
research/m16/2026-11-22/code/m16_rot005_two_site_signed_arcsine_and_quadratic_mask_nomap.py

GitHub code commit 71d0b09d3e890b0fdf7772a8e2258a92031b01a7 (created and to be read back); the executed local script is a separate, formula-identical version. Do NOT claim cold executing GitHub blob verbatim or hashes of machine JSON not actually uploaded. Source-matched local program stdout verified in the running environment.

Prior external classical source used for the normal orthant identity: https://link.springer.com/article/10.1007/s11336-020-09730-5 ; this does NOT support a novel NASH mathematical theorem or any physical sensor. Source model rational coefficients originate solely in Geeky-S12 ROT038, not in this external classical reference.

## 6. Decision and STOP

**Source-conditional exact math:** two local *signed centered* Gaussian site readings separate the NEW B vs Bpi axis-permutation models, even with arbitrary hypothesis-dependent/adaptive POSITIVE multipliers per channel. A single standalone site cannot. The Bernoulli Hoeffding sufficient n 591093/908653 are not sharp and are not physical experiment resource commitments.

**Separate, stronger no-map:** under source SPD Gaussian law, even all SIX QUADRATIC cubic mask energies cannot recover the four-Fourier power contrast almost surely; new proof uses orbit invariance + mutual absolute continuity, NOT the linear-mask Gaussian sine independence from ROT012. Distinct original firstness retained.

**Material next decision:** Is any actual signed/centered two-site channel (or a source-typed boundary contrast) available, and what nuisance class is defensible empirically? If not, all these are conditional statistical experiment design models; no external novelty gate or hardware benefit has been passed. We do NOT launch another unassigned audit, BW ingestion, CANON or EXEC_SIGN process.

FINAL: M16_ROT005_SOURCE_RATIONAL_B_BPI_PASS / TWO_SIGNED_LOCAL_SITE_GAUSSIAN_ARCSIN_EXACT / INDEPENDENT_MPMATH_GAUSSIAN_QUADRATURE_PASS / ADAPTIVE_POSITIVE_GAIN_PATHWISE_PASS / CONSERVATIVE_HOEFFDING_591093_908653_PASS / FULL_SUPPORT_SIX_QUADRATIC_MASK_FOURIER_C_NOMAP_ANALYTIC / FULL_N41CUBED_POSITIVE_ORBIT_WITNESS_PASS / NO_HARDWARE / NO_M13_HISTORICAL_RUNTIME / NO_GENERAL_NOVELTY / NO_CANON / NO_EXEC_SIGN.
