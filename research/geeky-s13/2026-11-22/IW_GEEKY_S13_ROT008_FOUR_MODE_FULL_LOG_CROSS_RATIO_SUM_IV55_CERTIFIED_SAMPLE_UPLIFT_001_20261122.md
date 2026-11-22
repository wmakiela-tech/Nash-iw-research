---
artifact_id: IW_GEEKY_S13_ROT008_FOUR_MODE_FULL_LOG_CROSS_RATIO_SUM_IV55_CERTIFIED_SAMPLE_UPLIFT_001_20261122
return_id: IW_GEEKY_S13_ROT008_ROT038_FOUR_MODE_SEPARABLE_GAIN_FULL_LOG_CROSS_RATIO_SIMPSON_IV55_RISK_AND_NP_CEILING_001_20261122
origin: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
science_class: SOURCE_TYPED_SYNTHETIC_M13_N41_ANISOTROPIC_GAUSSIAN_A_B / SOURCE_FIRST_FOUR_MODE_SUM_LOG_INVARIANT_TEST / ANALYTIC_FINITE_N_RISK / IV55_CERTIFIED_IMPROVED_SAMPLE_GATES
status: AUTHOR_MATH_EXECUTED_IV55_SIX_FINITE_N_CERTIFICATES / SAME_CELL_INDEPENDENT_SCIPY / DIFFERENT_CELL_I1_PENDING
source_execution: M13_ORIGINAL_AUXILIARY_SOURCE_READ_PRIOR_ROTATION_NOT_NATIVE_EXECUTED_NOW / HISTORICAL_FULL_DTC0A_RUNTIME_MISSING
claim_ceiling: NO_GENERAL_MATHEMATICS_NOVELTY / NO_PHYSICAL_RAW_SITE_MEASUREMENT / NO_CANON / NO_EXEC_SIGN / BW_PENDING
---

# Geeky-S13 ROT008: more efficient four-mode calibration-invariant test, rigorous finite-sample error by Fourier inversion

## 0. Source-native question, priority, result

Geeky-S13 ROT007 showed that four HYPOTHETICAL mean-free RAW-site Fourier energies in the original M13 N41 periodic grid allow an exactly calibration-independent cross ratio for original Geeky-S12 ROT038 *anisotropic* synthetic Gaussian site-noise hypotheses A/B, provided the nuisance gain factorizes into a direction factor times a radial factor separately for every snapshot. ROT007 discarded all but a 1-bit decision per snapshot and its exact majority test first passed >95% at **20,557** IID hypothetical snapshots and >99% at **41,121**. Does retaining the actual continuous value improve the source-conditional mathematical resource bound while preserving **unbounded, arbitrary, adaptive, snapshot-varying, candidate-specific** direction×radius gains?

**AUTHOR THEOREM: YES.** The elementary full-log-cross-ratio *sample-sum test* (which is NOT the optimal full-information NP test) yields strictly certified >95% at **n=15,029** and >99% at **n=30,063**, with opposite verdicts at the immediate preceding integers **15,028** and **30,062** respectively. The six complete actually executed IV55 certificates also cover n=16,000 and n=32,000 as generously sufficient safety gates. Improvement at these four endpoints: ~26.89% and ~26.89% fewer whole hypothetical RAW-site snapshots than ROT007's one-bit test. We **do not** claim the first possible n for the full-log sum test, full-invariant LRT or all source observers; proving two adjacent crossings does not establish all-n monotonicity for this particular non-NP sample-sum rule.

**Scientific firstness maintained:** original M13 first public N41 sparse B tensor/Fourier auxiliary, hash Git blob SHA1 `c6377cfbc9a0070abc34ffedc5871e719f6a4679`; Geeky-S12 ROT038 FIRST exact rational SPD ANISOTROPIC site Gaussian A/B (blob `28576dbb0649c1f0fbd4d926896813eac946e6d8`) and original nine-coarse-observation alias; Geeky-S13 ROT003 FIRST two directional modes, ROT004 shared-volatility ratio and sign, ROT005 full two-mode NP, ROT006 directional-gain sharp radius, ROT007 FOUR-mode rank-3 separable calibration invariant and one-bit first-n gate (blob `ce97cdabfa887ffb1029c98715f6fdc836875c18`). M15 ROT041 FIRST an entirely **different** six-mode five-nuisance-degree group for DIFFERENT isotropic ROT035 A/B. Neither two source A/B pairs nor group firstness are conflated. Logistic convolution, Fourier inversion, composite Simpson, Euler product, likelihood-ratio theory are standard mathematics, NOT claimed as general mathematical novelty.

## 1. Exact original-source algebra and nuisance group

Using source order `(beta0,beta_x,beta_y,beta_z,beta_xy,beta_xz,beta_yz,beta_body)`:

`A=(1,1/25,1/25,1/25,1/30,1/30,1/30,2/25)`;
`B=(1,1/20,3/100,1/25,1/30,13/300,7/300,2/25)`.

Both have strictly positive periodic 41³ spatial Fourier variances at least 7/10, because sum of the seven nonidentity positive neighbor-operator coefficients equals 3/10. At axial frequency `j` and `c_j=cos(2πj/41)`:

`v_A(x,j)=v_A(y,j)=167/150+(14/75)c_j`;
`v_B(x,j)=82/75+(31/150)c_j`;
`v_B(y,j)=17/15+c_j/6`.

The chosen original-source Fourier modes are `xH=(20,0,0), yH=(0,20,0), xL=(7,0,0), yL=(0,7,0)`. According to independent prior M15 original-source native support checks, the deterministic M13 B-energy has Fourier differences supported in the signed box `[-6,6]×[-4,4]×[-2,2]`; all four chosen modes and conjugates are outside. Thus the original-source energy means **of these hypothetical extra modes** vanish. The M13 historical full `dtc0a_runtime_v0_3_1.py` remains missing; ROT008 does **not** newly execute the original M13 tensor producer, acquire RAW recordings or check actual sensors.

For each sample t, each of the 4 observed squared Fourier mode magnitudes is postulated as

`P_{d,r,t}=G_{d,t} H_{r,t} v_X(d,r) E_{d,r,t}`, where X=A or B, d=x/y, r=H/L, and the latent E variables are independent unit exponentials, IID four-vectors across t. The factors `G_x,G_y,H_H,H_L>0` can be ANY positive unbounded functions of time, hypothesis, all underlying latent variables, and past/future: no independence, calibration standard deviation or derivative constraint is postulated. Their only real restriction is exact MULTIPLICATIVE separability into direction×radius *within each snapshot*.

Exactly, pathwise:

`C_t=(P_xH P_yL)/(P_yH P_xL) = q_X (E_xH E_yL)/(E_yH E_xL)`.

The four loggain columns have rank 3 with annihilator `(1,-1,-1,1)`; `Z_t=log C_t` is their maximal invariant over strictly positive energy vectors. Source exact

`q_A=1, q_B=exp(-Delta)`;
`Delta=log[v_B(x,7)/v_B(y,7)]-log[v_B(x,20)/v_B(y,20)]`
`     =0.06883323430559849760294690989001727861304...>0`.

Under A, `Z_t=W_t=L_{1,t}+L_{2,t}` with independent standard logistic `L` obtained from logarithms of exponential ratios. Under B, `Z_t=W_t-Delta`. Because the nuisance cancels pathwise *before* taking a distribution, the observed `Z_t` retain these IID laws even under fully adaptive shared gain factors, including nonGaussian marginal observed four-channel energies.

## 2. Two distinct full-value tests: optimal NP and computable sample-sum

The CDF of `W=L1+L2` is `F_W(w)=e^w(e^w-1-w)/(e^w-1)^2`, interpreted continuously as 1/2 at zero. Differentiating yields the exact even density

`f_W(w)=[w*coth(w/2)-2]/[4*sinh(w/2)^2]` for `w≠0`, with `f_W(0)=1/6`.

The convolution of two standard logistic densities is strictly logconcave. The **Neyman–Pearson** equal-prior likelihood ratio for the *complete sequence of maximal invariants* `(Z_1,...,Z_n)` therefore selects B iff

`sum_{t=1}^n [log f_W(Z_t+Delta)-log f_W(Z_t)] > 0`.

The individual score is nonlinear and bounded, approaching `+Delta` and `−Delta` at negative and positive infinities. This LRT is optimal among tests based on these entire `n` cross ratios for the two fixed source hypotheses and exactly stated nuisance group. **It is not equivalent for n≥3 to a test on the sum `Σ Z_t`; ROT008 does NOT present its exact finite-n optimal threshold.** The score and density are an exact analytical characterization for independent review, not a claim of a new general NP theorem.

For a tractable, powerful **but not globally optimal** four-mode invariant rule define `S_n=Σ_t Z_t`. By symmetry of W, the test

`Decide B iff S_n < -n*Delta/2`

has exactly equal type I and type II errors. Its risk is

`e_n=P_A(Σ W_t < -n*Delta/2)=P(Σ W_t > n*Delta/2)`.

Each logistic characteristic function is `φ_L(s)=πs/sinh(πs)`, and there are 2n independent logistics in ΣW. Gil–Pelaez/Fourier inversion gives, exactly,

`e_n = 1/2 - (1/π)∫_0^∞ [sin((n Delta/2)t)/t] [πt/sinh(πt)]^(2n) dt`.

After `u=√n*t`, put `a_n=√n*Delta/2` and `g_n(u)=[(πu/√n)/sinh(πu/√n)]^(2n)`. Then

`e_n = 1/2 - (1/π)∫_0^∞ [sin(a_n u)/u] g_n(u) du`.

The integrand at u=0 has continuous extension `a_n`. It is not replaced by a normal approximation. Finite-n risk is **exactly** independent of all allowed nuisance gains under the retained Gaussian latent model.

## 3. NEW actual directed-IV55 computational certificate with analytical error control

We independently computed 6 cases `n=15028,15029,30062,30063,16000,32000` from the **original exact rational ROT038 source coefficients and interval cosines**, using 55-digit outward `mpmath.iv` arithmetic. Composite Simpson quadrature has 4,000 equal panels on `[0,8]`, length `h=8/4000=1/500`, which is an even number of panels. The following strictly deterministic remainder bound is proved for **all these n** (n≥15,000, n≤32,000 and source `0<Delta<0.07`). No derivative is estimated by sampling:

1. Euler's product `sinh(πt)/(πt)=∏_{m≥1}(1+t²/m²)` gives `log g_n(u)=-2n Σ_{m≥1} log(1+u²/(nm²))`.
2. On `0≤u≤8`, `log(1+x)≥x−x²/2` yields
   `g_n(u)≤exp[-(π²/3)u²+ζ(4)u⁴/n]≤exp(-3u²)`.
3. Let `A=2π²/3`. Elementary differentiation of Euler's product and complex conjugate factor bounds yield
   `|(log g)'|≤A u`, `|(log g)''|≤A`,
   `|(log g)'''|≤8ζ(3)/√n<0.08`,
   `|(log g)''''|≤24ζ(4)/n<0.002`.
4. Applying the product derivative identities and maxima of `u^k exp(-3u²)` yields **uniform**
   `|g'|<2, |g''|<12, |g'''|<60, |g''''|<500`.
   Since `sin(a_n u)/u=∫_0^{a_n} cos(vu)dv`, for k=0..4 its kth derivative has absolute value at most `a_n^(k+1)/(k+1)`; `a_n<7` throughout. Leibniz then yields for `H(u)=[sin(a_n u)/u]g_n(u)`:
   `|H''''(u)|<7·500+4·(49/2)·60+6·(343/3)·12+4·(2401/4)·2+16807/5 < 30,000`.
5. The composite Simpson error obeys
   `|E_S| < (8/180)*(1/500)^4*30,000 < 2.134×10^-8`.
6. For **every u≥8** the Euler product implies `g_n(u)≤(1+u²/n)^(-2n)`. Split `[8,√n]` and `[√n,∞]`. On the first interval `g_n≤exp(-u²)` because `log(1+x)≥x/2` for 0≤x≤1. Hence
   `∫_8^∞ |sin(a_n u)| g_n(u)du/u < e^-64/128 + 2^(-2n)/(2n-1) < 2×10^-30`.
7. The risk conversion divides the total integral error by π. The new code uses the uniform, outward-rounded padding `±8×10^-9` for each risk, strictly exceeding the combined two analytic error bounds. It retains interval uncertainty in the exact irrational source `Delta` and numerical quadrature terms. There is no Monte Carlo randomness in certification.

**Complete machine certificates (summarized, all intervals strictly on one side of the decision boundaries):**

| n | Rigorous lower risk bound | Rigorous upper risk bound | Judgment |
|---:|---:|---:|---|
| 15,028 | 0.05000487996028 | 0.05000489596029 | **NOT >95%** |
| **15,029** | **0.04999923585533** | **0.04999925185534** | **>95%** |
| 30,062 | 0.01000037123796 | 0.01000038723798 | **NOT >99%** |
| **30,063** | **0.00999934003225** | **0.00999935603227** | **>99%** |
| 16,000 | 0.04483274803464 | 0.04483276403466 | **>95%** |
| 32,000 | 0.00819421811396 | 0.00819423411397 | **>99%** |

The lower/upper values displayed above are shortened decimals of the machine-cert intervals, rounded conservatively for readability. **These are six exact finite-n rigorous risk gates for ONE fixed simple sample-sum rule**; the NP-invariant test may be strictly better for n≥3. No statement of minimal n over all test classes, other possible non-monotone n or actual experimental measurements follows from the four adjacent n checks. Relative to ROT007's **different** one-bit decision rule under **the same exact four-mode nuisance group**, the improvements are `(20557−15029)/20557≈26.89%` and `(41121−30063)/41121≈26.89%` fewer hypothetical RAW snapshots to reach those levels with the stated rule.

## 4. Independent same-cell program and negative knowledge

A second algorithm independently rebuilds the original exact ROT038 8-coefficient spectra from **all 8 directional Fourier operator terms**, obtains `Delta` in ordinary SciPy/NumPy arithmetic, differentiates the CDF to verify `f_W(0)=1/6`, integrates Fisher information for `f_W` and numerically evaluates the **same exact characteristic-function integral by independently implemented SciPy QUAD**. All six resulting point risks lie inside the IV55 bounds. Its supplementary Fisher location information is approximately `I_W≈0.15710461599` per complete log-cross-ratio, a **numerical diagnostic**, not an exact certified information radius or finite-n optimum. The heuristic normal/Fisher approximation to the full NP 95% sample gate `n≈14,539` is not accepted as a rigorous sample threshold.

**Falsifiers explicitly retained:**

- `G_{d,r}` **nonseparable** four arbitrary gains introduce a fourth independent log-energy direction; the rank-3 cross-ratio invariant disappears and exact A/B alias can be constructed. More measured channels cannot by themselves rule out this nuisance.
- Directional or radial **additive noise**, saturation and frequency leakage do not cancel from cross ratios; ROT008 does not model them.
- Without standardized **latent IID Gaussian** Fourier coefficients (equivalently independent unit exponentials after squaring), the exact logistic-sum density and certified sample probabilities may fail, even if observed site covariances are unchanged.
- A one-bit sign under the same four-mode contract still has its exact ROT007 n thresholds; the new test improves conditional resource needs only by preserving a fuller statistic, not by altering the source spectra or assuming a smaller nuisance class.
- The finite-sample **NP** likelihood is not the score used for the strictly certified 15,029 and 30,063 thresholds; no claim of NP-optimal n is permitted.
- All source Fourier detectors are HYPOTHETICAL, not original fixed five coarse masks, and the original full historical DTC0a runtime has not been recovered. No NASH physical J3/K/GR/TPE/GW claim.

## 5. Provenance, reproducibility and bounded outside I1 request

The bundle contains (i) new original-source-typed standalone Python IV55 reproducer including six cases and complete JSON; (ii) independently written NumPy/SciPy script and complete JSON; (iii) executable guard+receipt for all original-source identity, interval containment, sample gate and fail-closed mutation tests; (iv) this report and README; (v) frozen previous ROT007 original-source-scoped report as predecessor with SHA256; (vi) SHA256 payload manifest and reproducibility ZIP. Sources were directly inspected; parameters are not a claim that we ran the original M13 historical tensor producer.

Independence limits: two algorithms in **the same Geeky-S13 cell** are not different-cell independent I1; a separate REC13/AUD3 I1 on ROT008 is still required. The latest fetched M15 ROT041 belongs to separate isotropic Gaussian A/B (ROT035) and uses six-mode five-parameter nuisance, so no duplication of its firstness is inferred.

**Specific I1 demand:** independently verify the exact logistic-sum density and NP loglikelihood; check the characteristic-function inversion and π normalization; audit *every link* in the global fourth-derivative bound, Simpson remainder and Euler-product tail; reconstruct original rational source `Delta`; independently verify IV55 enclosures at n=15028/15029/30062/30063; falsify the source contract with permitted adaptive separable gains or exhibit an overlooked latent dependence; do not confuse 15,029/30,063 sample-sum gates with minimal invariant NP sample sizes or measured physical sensors.

STATE: `SOURCE_TYPED_N41_ANISOTROPIC_ROT038_RATIONAL / FOUR_MODE_SEPARABLE_UNBOUNDED_GAIN / FULL_LOG_SUM_TEST / IV55_SIX_FINITE_N_RISK_PASS / RIGOROUS_SIMPSON_4TH_AND_EULER_TAIL_PASS / SAME_CELL_INDEPENDENT_SCIPY_PASS / DIFFERENT_CELL_I1_PENDING / BW_PENDING / NO_GENERAL_NOVELTY / NO_PHYSICAL_RAW_SENSOR / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE`.
