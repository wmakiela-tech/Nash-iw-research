---
artifact_id: IW_M16_ROT003_RAW_FOURIER_MINIMAX_COMPLETENESS_AND_GEEKY_ROT010_IV75_TAIL_PARTIAL_I1_001_20261122
return_id: IW_M16_ROT003_FOUR_RAW_POWERS_STRICT_MINIMAX_COMPLETENESS_AND_GEEKY_S13_ROT010_INFINITE_TAIL_PARTIAL_I1_001_20261122
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_11 / M16
created_at: 2026-11-22
exposure: PUBLIC
result_class: SOURCE_CONDITIONAL_EXACT_FULL_RAW_FOUR_POWER_MINIMAX_PROOF_AND_DIFFERENT_CELL_BOUNDED_INTERVAL_TAIL_I1
status: M16_ANALYTIC_PROOF_AND_EXECUTED_NUMERIC_WITNESS_PASS / ROT010_PARTIAL_I1_ONLY
sync_state: GITHUB_SOURCE_ONLY_BW_UNVERIFIED
claim_ceiling: NO_FULL_ROT010_IV75_I1 / NO_REAL_FOURIER_SENSORS / NO_GENERAL_MATH_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE
---

# M16 ROT003 — four RAW power minimax equality and bounded independent ROT010 infinite-tail referee

## 0. Sources and firstness

Original firstness belongs strictly to:
- M13 original N41 sparse Fourier/tensor helper (public Git blob c6377cfbc9a0070abc34ffedc5871e719f6a4679; NOT executed here); historical complete dtc0a_runtime_v0_3_1.py not recovered.
- Geeky-S12 ROT038 FIRST synthetic rational anisotropic Gaussian A/B (original Git blob 28576dbb0649c1f0fbd4d926896813eac946e6d8).
- Geeky-S13 ROT006 FIRST two-mode sharp adaptive directional gain minimax (blob 814bc6eeaf131a818066de5dbeaa0ffcf532f45c).
- Geeky-S13 ROT007 FIRST four-mode direction-times-radius separable-gain maximal invariant (blob ce97cdabfa887ffb1029c98715f6fdc836875c18).
- Geeky-S13 ROT009 FIRST full four-mode exact Neyman–Pearson test and symmetric-tilt risk formula (blob 14fbe78c6371bbed80bf5b4febc0de69f4120e4c).
- M16 ROT001 FIRST different-cell proof of STRICT n monotonicity of ROT009's NP risk, blob 457b3cb02d8f69d64b1b9eddc279f5c041b89f93.
- M16 ROT002 FIRST applied ROT006's endpoint minimax method to **bounded nonseparable four-mode power calibration interaction** and obtained EXACT optimal risk among tests using Z=log cross ratio; blob 87aa54864315e21654f9acb0628ed4897d99425c.
- **Geeky-S13 ROT010 FIRST original SOURCE-CONDITIONAL IV75 claimed certified 14,539/29,083 sharp sample gates**, Git blob 69a07892ec0574b5ecd3ac8abae9b78b607e5a31, original report opened and read entirely:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/d49588de62ad78ce8bdb7bc458065decf369548c/research/geeky-s13/2026-11-22/IW_GEEKY_S13_ROT010_SHARP_FOUR_MODE_NP_IV75_SAMPLE_CERTIFICATE_001_20261122.md.

This M16 rotation does NOT recreate ROT010's IV75 32-point quadrature/4000-panel certificates. It performs only a clearly marked **PARTIAL independent I1 for its source parameter and CF infinite tail**, plus an exact mathematical strengthening of M16 ROT002. No claim to original NP threshold firstness or a full independent IV I1.

## 1. Raw four-power minimax extension: statement

The RAW Fourier power vector has four positive components in order (x20,y20,x7,y7). Denote its logarithm by Y in R^4 and set the cross vector w=(1,-1,-1,1), with w·w=4. Let fixed source log spectra a_X=log(v_X) in R^4, and IID standard exponential source energies E_j with e_j=log E_j componentwise. The raw power model is

  Y^X_j = a_X+e_j+k_X,j(e_j,history,X),

where k_X,j=log(K_X,j) is the strictly positive multiplicative power gain in log coordinates. The gain can depend on hypothesis X, sample and all latent energies as expressly allowed by ROT007/ROT002. Only its **interaction** w·k_X,j is bounded pathwise:

  |w·k_X,j|<=epsilon  almost surely, every j.

The exact source contrast is w·a_A=0 and w·a_B=-Delta, with

  Delta=log[(v_B(x7)/v_B(y7))/(v_B(x20)/v_B(y20))]
       =0.06883323430559849760294690989001727861304...>0.

Then the RAW statistic Z_j=w·Y_j is exactly W_j+theta_A,j under A, W_j-Delta+theta_B,j under B, with W_j=w·e_j distributed as sum of two independent standard logistic variables.

Write R_n^RAW(epsilon)=inf over ALL measurable, possibly randomized classifiers of the WHOLE sequence Y_1..Y_n of the maximum of the two worst-case conditional errors, sup separately over ALL admissible nuisance maps under A and B.

**Theorem RAW (new source-qualified strengthening of ROT002):**
For every integer n>=1,

  R_n^RAW(epsilon)=e_n^NP(Delta-2epsilon),  0<=epsilon<Delta/2;
  R_n^RAW(epsilon)=1/2,                    epsilon>=Delta/2.

Here e_n^NP(d) is ordinary symmetric NP Bayes risk for location family f_W(t) vs f_W(t+d) as defined in Geeky-S13 ROT009. Hence the previously reported four-mode minimax theorem is not merely optimal in the Z-measurable subclass: under the EXACT exceptionally permissive data-adaptive gain contract it is optimal among ALL tests of four observed raw powers. This does NOT assert minimax over additional raw site readings, real amplitudes/phases, unknown noise, hardware, or a more restrictive independent-gain family.

## 2. Complete proof by a RAW canonical gauge slice

**Upper bound.** M16 ROT002 proves by pathwise score monotonicity that the endpoint NP classifier on Z alone has each worst-case conditional error at most e_n^NP(d), d=Delta-2epsilon>0. Since any Z-based classifier is also a RAW classifier,

  R_n^RAW(epsilon)<=e_n^NP(d).

**Lower bound, requiring a legal explicit adversary.** Fix any constant admissible interaction eta_X satisfying |eta_X|<=epsilon, possibly different under each hypothesis. For each hidden exponential vector e and its latent source log powers T_X=a_X+e, define the scalar z_X=w·T_X+eta_X and the observed raw log powers

  Y_X := (z_X/4) w.

Choose the data-adaptive log gain

  k_X(e) := Y_X - T_X.

It is allowed: all its four components are real and the observed K=exp(k) is positive; it depends measurably on e and X, and satisfies EXACTLY

  w·k_X = (w·w/4) z_X - w·T_X = eta_X.

If eta_X=0 the gain k_X lies in the three-dimensional annihilator of w, i.e. exactly the log-direction-by-radius separable gain subspace. For eta_X nonzero it has exactly the permitted nonseparable cross interaction, while the other three gain degrees remain unrestricted.

Crucially the ENTIRE observed four-power vector is now a deterministic injective transform of ONE scalar z_X: exp(Y_X)=exp(w z_X/4). No non-invariant raw amplitude can help classify X for these admissible nuisance processes.

For 0<=epsilon<Delta/2 take eta_A=-epsilon and eta_B=+epsilon. The two raw observation distributions are exactly injective transforms of Z_A=W-epsilon and Z_B=W-Delta+epsilon, IID across snapshots since e_j are IID. Their separation is d=Delta-2epsilon. Against this embedded two-simple-hypothesis endpoint subexperiment, every RAW classifier has maximal conditional error >= equal-prior NP Bayes risk e_n^NP(d). This proves lower bound matching the Z-based upper bound.

For epsilon>=Delta/2 take eta_A=-Delta/2 and eta_B=+Delta/2. Then in the SAME canonical gauge slice under a shared-E coupling both RAW log vectors are literally

  Y_A = Y_B = [w·e-Delta/2] w/4,

so all four observed powers have EXACTLY THE SAME joint law for EVERY n, and a fair coin is minimax. Note the proof here is stronger than ROT002's stated Z-only alias: it constructs equal entire four-power distributions. QED.

**Severe scope warning:** the adversary explicitly accesses the latent e and selects hypothesis-specific gains. Removing either such freedom or restricting separable gains to fixed calibration over snapshots can materially improve RAW discrimination; this theorem cannot be applied to that different experiment. It shows the mathematical consequence of a very broad nuisance class, NOT unavoidable loss in any real instrument.

## 3. PARTIAL independent Geeky ROT010 IV75 referee: infinite characteristic-function tail

ROT010 writes e_n=(1/(2pi))∫_0^infinity A(t)^n/(t²+1/4)dt with A(t)=rho psi(t), rho<=1, and f the logistic-convolution density. It claims a uniform |psi(t)|<=0.998272 for t>=8 and consequent risk tail <2.4e-13 for n>=14538. This segment is directly re-derived below, without reusing the author's IV code.

For standard logistic q(x)=1/[4cosh²(x/2)], (log q)''(x)=-(1/2)sech²(x/2)>=-1/2. The convolution f=q*q can be rewritten f(x)=∫q(u+x/2)q(u-x/2)du. Second logarithmic differentiation gives

  (log f)''(x) = E[(log q)''(u+x/2)/4+(log q)''(u-x/2)/4] + Var(V_x(u)) >=-1/4,

where V_x(u) is the x-derivative of the inside logarithmic density and the expectation/variance use the normalized positive integrand. The upper bound (log f)''<=0 follows from standard convolution preservation of log-concavity. Hence for centered score ell(y)=log[f(y+Delta/2)/f(y-Delta/2)]:

  -Delta/4 <= ell'(y) <=0, so |ell'(y)|<0.01725 when Delta<0.069.

The tilted sampling density is h(y)=sqrt(f(y-Delta/2)f(y+Delta/2))/rho with rho<=1. Since f is even and decreasing for positive y, on y∈[-2,2],

  h(y)>=f(2+Delta/2)>0.11.

The original source inequality ell(2)<-0.024 plus symmetry and strict monotonicity implies the score takes every value of [-0.024,0.024] at some y in [-2,2]. Therefore the *pushforward* score density under h is at least 0.11/0.01725>6 on that score interval. The score law contains the uniform[-0.024,0.024] distribution as a mixture component of mass at least m=6*(0.048)=0.288.

Consequently |psi(t)|<=1-0.288+0.288 |sinc(0.024 t)|. For t>=8, u=0.024t>=0.192; on [0.192,pi], sin(u)/u is decreasing and sin(0.192)/0.192<0.994; for u>=pi, |sin(u)/u|<=1/u<=1/pi<0.994. Hence for ALL real t>=8,

  |psi(t)|<=0.712+0.288*(0.994)=0.998272.

Since rho<=1 and ∫_8^infinity dt/(t²+1/4) <=1/8, for n>=14538:

  |tail contribution to e_n| <=(0.998272)^n/(16*pi)
                   <= (0.998272)^14538/(16*pi)
                   = approx 2.39382725341078124277e-13
                   < 2.4e-13.

This bound is GLOBAL over ALL t>=8; it does not rely on the false assumption psi(t)>=0 outside the truncated outer quadrature.

**Actually executed independent interval computations:** mpmath.iv 80-digit with exact rational source spectral coefficients and interval cos/log/exp confirms
- Delta within [0.06883323430559849760294690989001727861304162229302232973778953079330830713407330132788, 0.06883323430559849760294690989001727861304162229302232973778953079330830713407331924962];
- f(2+Delta/2) within [0.1118749799196487198858612044053526840571976738692293865000768213520689980714517879754, 0.1118749799196487198858612044053526840571976738692293865000768213520689980714517956185];
- ell(2) within [-0.02562539748709120822129623930678487702352915117948342857265719720690080145375409036287, -0.02562539748709120822129623930678487702352915117948342857265719720690080145375395730056].
All strict conditions PASS, as does outward bound on tail.

**PARTIAL I1 verdict:** ANALYTIC SCORE DENSITY MINORIZATION / 80DPS SOURCE-INTERVAL KEY VALUES / ENTIRE t>=8 FOURIER TAIL PASS. This is NOT review of analytic complex-strip quadrature, all 32 Gauss root sign brackets, 180 inner panels, 4000 outer Simpson panels or interval JSON. The author's four original adjacent threshold IV75 inequalities remain AUTHOR_CERTIFIED / DIFFERENT_CELL_FULL_IV_I1_PENDING. M16 ROT001 monotonicity proof continues to stand independently.

## 4. Actually executed RAW gauge witness, reproducibility and error handling

New different-cell program (NumPy plus mpmath), 600 independent latent four-energy vectors; coupling the same E under A and B for verification, while leaving source draws independent within each hypothesis:
- epsilon/Delta = 0, 1/4, 1/2;
- in all three cases computed cross-interaction w·logK matches admissible eta to double precision;
- at epsilon/Delta=1/2 all four RAW LOG energies under A and B coincide to max absolute difference 8.88e-16, rather than only matching the scalar cross ratio;
- at epsilon/Delta=0 the constructed gains lie in the exact separable subspace;
- independent interval tail test PASS at 80 decimal precision.

The first attempt at a purely binary64 RAW numerical witness rejected an overly strict *absolute observed power* tolerance 5e-15 because exp(Y) can amplify tiny relative/log discrepancies at large values. The scientifically appropriate log-relative criterion <5e-14 was substituted, without altering any model formulas, source parameters, random seed, or proof. All cases rerun PASS. This computational correction is documented instead of silently retroactively counting the first attempt as PASS.

**Source program:** research/m16/2026-11-22/code/m16_rot003_raw_fourier_minimax_and_rot010_tail_audit.py, public Git commit 75b41662b38eaba457ae5f6cef4cc0c4f0656695. The full original script has been executed in the local environment with final JSON output; a finite code check is NOT a substitute for the exact analytic proof.

## 5. Disposition and STOP

**M16 ROT003 direct result:** FULL_RAW_FOUR_POWER_MINIMAX_EQUIVALENCE_PASS_ANALYTIC under the exact sample-adapted, model-dependent gain class. This strengthens the statement of the scope of M16 ROT002 and, at epsilon=0, establishes a RAW-four-energy minimax interpretation of Geeky-S13 ROT009/010's invariant NP sample experiment (conditional on original synthetic source model and permitted gains).

**ROT010 review:** INFINITE_TAIL_PARTIAL_I1_PASS; FULL_QUADRATURE_IV75_I1_HOLD. The owner FIRST IV75 theorem remains sourced and unaltered; no independent verification of the 32 Gauss root/weight certificate or the 4 finite-n risk intervals is claimed by this review.

**NEXT MATERIAL GATE:** evidence supporting an actual 4-mode RAW sensor model and measured (non)separable gain interaction class. With no empirical anchor, stop further arbitrary synthetic n-shaving, refrain from cross-cell task cascades, BW write/ING ID, novelty, physical NASH, CANON or EXEC_SIGN claims.

FINAL: M16_ROT003_ANALYTIC_FULL_RAW_MINIMAX_PASS / SOURCE_GAUGE_WITNESS_EXECUTED / ROT010_CF_TAIL_PARTIAL_IV_I1_PASS / FULL_IV75_THRESHOLD_I1_HOLD / GITHUB_READBACK_TO_VERIFY / BW_UNVERIFIED / NO_NOVELTY / NO_PHYSICAL_SENSOR / NO_CANON / NO_EXEC_SIGN.
