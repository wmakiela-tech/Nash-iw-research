---
artifact_id: IW_PRF12_R34_VARIANCE_ADAPTIVE_NONSTATIONARY_REFERENCE_ANYTIME_CERTIFICATE_001_20261110
created_at: 2026-11-10
owner: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
source_type: NEW_THEORETICAL_COMPOSITION_WITH_INHERITED_R31_QUANTUM_CERTIFICATE_AND_R33_DRIFT_MODEL
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: PROOF_OF_WITHIN_EPOCH_ANYTIME_EMPIRICAL_BERNSTEIN / SYNTHETIC_RESOURCE_WITNESS / 70_DIGIT_ENDPOINT_CHECK / INTEGER_BINOMIAL_TAIL / INDEPENDENT_MATRIX_AND_COUNTEREXAMPLE_AUDIT / REFEREE_PENDING
claim_ceiling: NO_PHYSICAL_DRIFT_RATE_MEASUREMENT / NO_DETECTOR_JOINT_ERROR_IDENTIFICATION / NO_GLOBAL_QUANTUM_OPTIMALITY / NO_CANON / NO_EXEC / NO_NOVELTY / ORIGINAL_SINGLE_COPY_3Q_LOCC_CLOSURE_OPEN
---

# PRF12 R34 — Nonstationary variance-adaptive reference e-processes with **within-epoch optional stopping**

Date: 2026-11-10. Function: PRF12. **Scientific result:** under the R33 exogenous Lipschitz-detector-drift and conditional-Bernoulli-reference contract, an empirical-Bernstein nonnegative supermartingale remains valid even if the *conditional mean itself varies in time*. Inverting finitely many predictable betting factors provides simultaneous confidence bounds at **every reference sample number inside every epoch**, including adaptive choices of which reference to measure and when to stop. A two-epoch fully synthetic numerical witness keeps R33's source scientific decision **N=9500/K>=2765** and source-error budget, while reducing reference reads from 230000 to **46055**; this last saving is a fixture outcome, **not a universal bound on stopping-time resources**.

## 0. Source map, mature host subtraction, and hard guards

**Parent R31**: [full certified source-A all-Xi quantum witness](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-03/IW_PRF12_R31_NINE_CLASS_COMPOSITE_E_OPTIMALITY_BRACKET_AND_FIXED_N_1666_001_20261103.md), reproduced in this bundle via its unchanged original 7001-node Python implementation. It supplies the reference-detector-comparator source probability inequalities

\[
A_0=0.3106993896688963,\qquad B_0=0.27161358975207756
\]

under the R25 current-hidden-Xi/axis-conditioned exogenous source reset hazard, finite source-ON rectangular controls, 2 fresh sequential qubit shots with common Xi in intact pairs, and independent Cauchy–Lévy source B increments. Between-pair Xi may be arbitrarily dependent. The reference physical detector is specified through `p*= (0.99, 3705/69000)`, which lies in R31's originally certified finite-CP set. The R31 source theorem is **inherited and independently replayed, not re-derived as a novel all-real-Xi result in R34**.

**Parent R33**: [bounded detector drift and epochwise Hoeffding certificate](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-08/IW_PRF12_R33_DRIFT_INTERLEAVED_LOCAL_REFERENCES_AND_NONIID_SOURCE_GUARD_001_20261108.md). Its detector perturbation constant is exactly

\[
S=0.18(1)+0.20(1)+0.62(0.347)=0.59514.
\]

If BOTH shots' detector reference probabilities differ from `p*` by at most `delta`, then their signed-quartet-coin success probabilities differ by at most `2*S*delta`. Hence any detector trajectory with `delta` everywhere in the science window obeys

\[
\Pr_A(Y=1\mid\text{admissible full past})\ge A_0-2S\delta,
\qquad\Pr_B(Y=1\mid\text{admissible full past})\le B_0+2S\delta. \tag{34.1}
\]

The **source** remains exactly R33's quantum and hazard model; detector drift is confined to the effective terminal Z readout. The two recorded shot outcomes must be conditionally independent GIVEN complete latent histories with their own correctly calibrated conditional means; the additional scoring coin is private and independent. Detector drift, reference sampling and score selection must not anticipate future B Lévy increments. The drift rate is **a supplied pathwise bound**, not learned from this sample.

External mature hosts (no novelty claim): Howard–Ramdas–McAuliffe–Sekhon, *Time-uniform, nonparametric, nonasymptotic confidence sequences*, *Annals of Statistics* 49 (2021), DOI `10.1214/20-AOS1991`; Waudby-Smith–Ramdas, *Estimating means of bounded random variables by betting*, *JRSS B* 86 (2024), DOI `10.1093/jrsssb/qkad009`. In particular, betting processes designed for a **constant** conditional mean must NOT be casually reused for varying means. R34 uses a different centered nonstationary supermartingale and a pathwise drift relocation.

## 1. Theorem R34.1 — empirical-Bernstein supermartingale for varying conditional means

Consider a reference stream sampled at predictably selected times `tau_k`, with `X_k` in `{0,1}`. Conditional on a filtration that includes all hazard-relevant variables and observed past,

\[
p_k:=\mathbb E[X_k\mid\mathcal F_{k-1}]\in[0,1],
\]

and **the values `p_k` need NOT be identical**. Let `q_k` be any `[0,1]`-valued predictor measurable before `X_k` is revealed, and let `V_n = sum_{k<=n}(X_k-q_k)^2`. For `lambda` in `(0,1)`, define

\[
\psi(\lambda)=-\log(1-\lambda)-\lambda,
\qquad
M_n^\pm(\lambda)=\exp\left(\pm\lambda\sum_{k\le n}(X_k-p_k)-\psi(\lambda)V_n\right). \tag{34.2}
\]

**Claim:** Both `M_n^+` and `M_n^-` are nonnegative supermartingales starting at 1, even when the `p_k` vary arbitrarily and the arm-selection/timestamps are predictable. (When the reference arm is not selected, take the multiplicative factor 1 on that global step.)

**Proof without stationarity:** for `|x|<=1` and `0<lambda<1`,

\[
\log(1+\lambda x)\ge\lambda x-\psi(\lambda)x^2. \tag{34.3}
\]

For `x<0` this follows termwise from the series of `-log(1-lambda|x|)` with `|x|^k <=|x|^2`, `k>=2`; for `x>=0` it follows from `log(1+y)>=y-y^2/2` and `psi(lambda)>=lambda^2/2`. With `x=X_k-q_k`, (34.3) gives

\[
e^{\lambda(X_k-p_k)-\psi(\lambda)(X_k-q_k)^2}
\le e^{\lambda(q_k-p_k)}\,[1+\lambda(X_k-q_k)].
\]

Taking conditional expectation gives at most `e^{lambda(q_k-p_k)}[1+lambda(p_k-q_k)]<=1`, because `1+z<=e^z` and the bracket is positive. For the negative process apply the same argument to `1-X_k,1-p_k,1-q_k`; the squared residual is unchanged. Therefore no independent-and-identically-distributed hypothesis or fixed sampling horizon is needed. QED.

**Fatal predictability guard:** if `q_k` is chosen after looking at `X_k`, this proof fails. For a fair Bernoulli reference `p_k=1/2`, setting `q_k=X_k` makes `V_n=0` and produces one-step *expected* alleged factor `cosh(lambda/2)>1`. This is an explicit falsifier, not merely a technicality.

## 2. Theorem R34.2 — joint confidence sequence at EVERY within-epoch sample size

Predeclare a nonempty finite grid `Lambda subset (0,1)`. For epoch index `j=1,2,...`, allocate failure budget `alpha_j=alpha/[j(j+1)]`. Split it across TWO reference arms, TWO signs and `|Lambda|` lambda values. Ville plus union bound gives **simultaneously for every completed epoch, arm and individual sample number `n>=1`**:

\[
\left|\widehat p_{i,j,n}-\frac1n\sum_{k=1}^n p_i(\tau_{i,j,k})\right|
\le r_{i,j,n}:=
\min_{\lambda\in\Lambda}
\frac{\log[4|\Lambda|j(j+1)/\alpha]+\psi(\lambda)V_{i,j,n}}
{\lambda n}. \tag{34.4}
\]

The global simultaneous coverage is at least `1-alpha`. The minimum over the lambda grid is legitimate precisely because **all** its candidate supermartingales were paid for in the error budget.

Now additionally assume an **exogenous pathwise detector drift rate**:

\[
|p_i(t)-p_i(s)|\le\nu_i|t-s|\quad\text{for all relevant }s,t. \tag{34.5}
\]

For any future science time `t`, even when the reference sample size `n` and epoch start time were selected from previous data,

\[
|p_i(t)-p_i^*|\le
|\widehat p_{i,j,n}-p_i^*|+r_{i,j,n}
+\frac{\nu_i}{n}\sum_{k=1}^n|t-\tau_{i,j,k}|. \tag{34.6}
\]

Equation (34.6) follows from (34.4), a triangle inequality, and (34.5), with **no assumption of stationarity**. As all reference shots in our example precede that epoch's science shots, the last time term is largest at the PREDECLARED science-window endpoint. Hence it is sufficient to use that endpoint in the stopping condition. This result permits adaptively selecting the reference arm, stopping INSIDE a reference epoch, and repeating the same process for an adaptively chosen number of epochs, paying alpha only once through the telescoping sum.

**Scope limits:** reference observations must have the asserted conditional means even when the sensor/source state is included in the filtration; each predictor and arm choice must be predictable. A zero-drift or sufficiently slow-drift condition is NOT inferred from (34.4). If the target science window is dynamically revised, the true physical endpoints must be re-evaluated through (34.6). Reusing an ordinary fixed-time Clopper–Pearson interval at optional stopping remains invalid.

## 3. R34.3 — preserve the R33 non-iid source test after arbitrary within-epoch stopping

Maintain R33's science plan: two epochs, 4750 science pairs in each, total `N=9500`, each pair duration `gamma*T_pair = 1.8283185307179588`. One reference read consumes `gamma*t_ref = .1`. Keep the conservative scientific bounds

\[
a=0.2995,\qquad b=0.2828.
\]

Using (34.1), these bounds hold whenever each detector arm's deviation from its predeclared certified nominal comparator is at most

\[
\boxed{\delta_* = \min\left\{\frac{A_0-a}{2S},\frac{b-B_0}{2S}\right\} = 0.009398133420642572.} \tag{34.7}
\]

The **predeclared stopping rule** is: before requesting any additional reference outcome, compute (34.6) at the end of the planned 4750-pair science window for both references; if both values are <= delta_*, STOP the reference block, then run that science block. Otherwise sample the reference with the larger current error budget; its predicted Bernoulli success probability is the predictable Laplace-type running mean `(K_i+50*p_i*)/(n_i+50)`. If certification does not succeed within the stated maximum acquisition budget, **ABSTAIN** rather than declare a source. A science epoch may also be omitted if the stated source/hardware contract fails.

On the joint confidence event, the R33 signed-quartet bit is a genuine Bernoulli variable obeying the **conditional** inequalities `P_A(Y=1|past)>=a`, `P_B(Y=1|past)<=b`. The arbitrary dependence of Xi BETWEEN pairs remains allowed. Thus the original N=9500,K>=2765 exact rational binomial domination theorem is unchanged:

- A false B under source A <= 0.03497645807537827;
- A false A under source B <= 0.03826512503260073;
- adding reference confidence failure <=.01 yields per-source wrong-declaration bounds <=.0449764581 and <=.0482651251, respectively, strictly below 5%.

Crucially, this proof does NOT condition naively on the future event of good calibration: stop each composite-null source test in the mathematical argument immediately before the first true-parameter reference confidence failure and pay that failure event separately by alpha. This is the same error-accounting principle as R33 but with NEW within-epoch-anytime reference coverage.

## 4. Fully specified reproducible SYNTHETIC two-epoch witness

All numbers in this section are SIMULATED. The detector was not physically measured. Predeclare prior-independent nominal comparator `p0*=.99`, `p1*=3705/69000`, random seed 20261110, lambda grid

`Lambda=(.06,.085,.12,.17,.24,.34,.48,.68)`, total reference alpha `.01`, exponent grid via (34.4), and a synthetic detector drift trajectory for the entire experiment:

\[
p_0(t)=.99+3\cdot10^{-5}\sin(t/4000),\qquad
p_1(t)=3705/69000+2.5\cdot10^{-5}\cos(t/3800). \tag{34.8}
\]

For `t` in units `gamma*time`, the exact derivative bounds are `7.5e-9` and `<6.58e-9`, respectively, so (34.5) holds for the externally declared `nu0=nu1=1e-8`. Reference readout events are drawn from independent Bernoulli distributions with these **changing** conditional probabilities. The reference arm sampled next is selected **only from past observations** using the rule of Section 3. The science bit distributions are NOT simulated to establish the statistical guarantee; the inherited R31 source bounds and exact rational binomial tails supply it.

| Epoch | n0 | n1 | positives K0/K1 | Maximum certified detector delta | Stop time gamma*t (before science) |
|---|---:|---:|---|---:|---:|
| 1 | 3372 | 18923 | 3339 / 1054 | .009395380206 | 2229.5000 |
| 2 | 4573 | 19187 | 4535 / 1061 | .009395045678 | 13290.0130 |

The detailed components of both deltas are saved in `R34_main_stdout.json`. A SECOND independent 70-decimal `mpmath` evaluation from the archived trajectories checks all four stopped endpoints, with the narrowest positive slack `2.753214675e-6` to (34.7); it is a high-precision cross-check of the stored floating-point synthetic data, not fully formal arithmetic verification of every sampled floating-point time.

This leads to:

| Resource | R33 (fixed-n nonstationary reference) | R34 (this synthetic adaptive stop) |
|---|---:|---:|
| Reference reads | 230000 | **46055** |
| Science pairs | 9500 | **9500** |
| All single-sensor reads | 249000 | **65055** |
| Total gamma-scaled wall time | 40369.02604 | **21974.52604** |

For this single reproducible synthetic draw, the reference burden drops by **79.98%**, total sensor readings by **73.87%**, and total modelled clock time by **45.57%**. These savings are NOT a theorem uniform in random measurement outcomes. The reference counts of R33 and R34 are different synthetic samples under different predeclared acquisition rules. An exploratory 12-seed sensitivity audit (same detector and rule, different synthetic random outcomes) gives observed reference counts from **33370** to **60888** (median 38707.5); this is NOT a confidence interval or a guarantee of future resource savings. A difficult or non-invertible detector can force ABSTAIN at the stated budget cap.

For further contrast, the R33 fixed-size Hoeffding reference certificate and its naive within-block repeated use are distinct objects: old fixed-size intervals cannot be used at R34's data-dependent stop, and a variance-BLIND time-uniform Hoeffding route remains substantially wider at the observed per-arm sample sizes. R34's gain comes from observed low residual variance for reference probabilities near 0.99 and 0.054, not from falsely reintroducing stationarity.

## 5. R34.4 — independent falsifiers and generality limits

**Falsifier F1: post-outcome forecast.** As in Section 1, choosing `q_k=X_k` after the measurement would make `V_n=0` even for fair `p=.5` and the process's expected one-step factor `cosh(lambda/2)>1`. The formula only holds for predictable forecasts. A separate independent checker verifies the correct e-factor expectation against 200000 random triples `(p,q,lambda)` and this precise invalid counterexample.

**Falsifier F2: calibration marginal does NOT certify independence of paired science readouts.** Two detectors can have identical calibrated one-shot probabilities `p0(t),p1(t)` but different science joint laws because a shared readout latch correlates the two results. At Z-axis recorded marginal `P(+)=1/2`, the R31 score `alpha_Z=.347,beta_Z=.018` has iid-shot expectation `(.347+.018)/4=.09125`; a perfectly shared latent latch with P(++ )=P(-- )=.5 instead has expectation `(.347+.018)/2=.1825`: difference `.09125`, larger than the entire inherited source contrast. Thus the R34 reference CS and correct drift control do NOT, by themselves, justify the quantum-to-recorded pair factorisation. Conditional shot-readout independence is a separate device-model assumption that needs its own test.

**Falsifier F3: unrestricted drift.** As in R33, one may perfectly calibrate a detector at reference times but make `p0(t)=p1(t)=.5` for each science shot when no pathwise drift restriction is imposed; A and B then have identical recorded four-category laws, so no source discriminator can be uniformly successful.

**Falsifier F4: anticipating future B noise or source-selective latent hazard.** Conditioning on future source-B increments, or only imposing a marginal no-reset rate that selects favorable Xi, invalidates the inherited per-pair source contrast. R34 does not weaken these source requirements; detector calibration cannot repair a changed source class.

The secondary numerical audit uses independent 2x2 unitary A and 4x4 Lindblad B evolution at nine Xi fixture values; its purpose is reproduction of the quantum-to-detector formula, **not** a new all-real-Xi proof. The ORIGINAL R31 7001-node mpmath.iv source certificate and R33 main drift calculation were both extracted verbatim from the earlier ZIP and actually re-executed; their JSON outputs matched the original archived outputs exactly. The R34 full statistical result and its source dependencies remain bounded by the R31/R33 assumptions.

## 6. Reproducibility and governance

The R34 ZIP includes: the complete current report, a full adaptive drift-reference Python reproducer, an independent e-factor and matrix-falsifier audit, a high-precision stopped-endpoint verifier, exact deterministic original R31/R33 parent runnable sources, all JSON/log outputs, a 12-seed resource variability record, and a member SHA-256 registry. Standard Python + NumPy + SciPy + mpmath for the entire suite. Full current and independent programs do not import each other; the source A/B global theorem is separately replayed from the original R31 first-owner program.

Scientific custody: independent scientific REFEREE not yet complete; no physical detector characterization; BW ingestion unverified. No novelty/priority claim relative to mature martingale confidence-sequence theory. The original three-qubit passive single-copy asymptotic LOCC closure remains OPEN. In the particular declared one-sensor source-ON instrument, we have an **anytime within-epoch empirical-Bernstein calibration theorem** and one favorable synthetic resource outcome, NOT an experimentally demonstrated source discriminator.

**RETURN:** PRF12_R34 / NONSTATIONARY_PREDICTABLE_EMPIRICAL_BERNSTEIN_E_SUPERMARTINGALE / WITHIN_EPOCH_ANYTIME_CALIBRATION / LATENT_XI_CONDITIONAL_SOURCE_GUARD / SYNTHETIC_NREF46055_NSCI9500 / EXACT_INTEGER_BINOMIAL_PASS / 70_DIGIT_ENDPOINT_CHECK / ORIGINAL_R31_R33_CLEAN_REPLAY_PASS / INDEPENDENT_READOUT_CORRELATION_AND_NONPREDICTABILITY_FALSIFIERS / REFEREE_PENDING / NO_CANON / NO_EXEC / NO_NOVELTY / BW_INGEST_PENDING / ORIGINAL_3Q_LOCC_CLOSURE_OPEN.

**R35 target:** conditional dependence diagnostics for paired readout outcomes, supported either by new pairwise device controls or a source-independent calibration reference, plus empirical control of the external Lipschitz drift bound. Improve the calibration/resource envelope only where this additional validation preserves a **global** source contrast.
