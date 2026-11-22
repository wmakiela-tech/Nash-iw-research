---
artifact_id: IW_GEEKY_S13_ROT004_TIMEVARYING_COMMON_VOLATILITY_EXACT_SIGN_TEST_AND_BETA_BINOMIAL_RESOURCE_IDENTITY_001_20261122
return_id: IW_GEEKY_S13_ROT004_ROT038_ANISOTROPIC_TWO_FOURIER_MODE_ARBITRARY_TIMEVARYING_COMMON_VOLATILITY_SIGN_TEST_EXACT_SAMPLE_GATES_001_20261122
origin_cell: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
date: 2026-11-22 Europe/Warsaw
source_scope: ORIGINAL_PUBLIC_M13_N41_AUXILIARY_PLUS_GEEKY_S12_ROT038_EXACT_ANISOTROPIC_SYNTHETIC_GAUSSIAN_COVARIANCES_PLUS_GEEKY_S13_ROT003_PERMUTATION_INVARIANT_FOURIER_MODES
result_class: SOURCE_CONDITIONAL_EXACT_TIMEVARYING_COMMON_SCALE_INVARIANT_SIGN_TEST / FINITE_BINOMIAL_RESOURCE_GATES / NON_GAUSSIAN_SHARED_VOLATILITY_REPAIR / POOLED_F_TEST_COUNTEREXAMPLE
status: AUTHOR_SOURCE_RATIONAL_ALGEBRA_AND_MPMATH_IV85_FINITE_SAMPLE_CHECKS_PLUS_INDEPENDENT_SAME_CELL_SCIPY / EXTERNAL_DIFFERENT_CELL_I1_PENDING
claim_ceiling: NO_GENERAL_NOVELTY / NO_NATIVE_RAW_SITE_SENSOR / NO_HISTORICAL_DTC0A_RUNTIME / NO_PHYSICAL_UPGRADE / NO_CANON / NO_EXEC_SIGN / BW_PENDING
---

# Geeky-S13 ROT004 — pathwise robust two-Fourier-mode discrimination under arbitrary time-varying shared gain; exact binomial sample gates and pooled-F failure

## 0. Problem, firstness, and new return

**Scientific target.** ROT003, based on the **original rational, strictly SPD, anisotropic synthetic Gaussian RAW-site noise hypotheses A/B** from Geeky-S12 ROT038, found a permutation-related optimal two-frequency witness on the original N=41 periodic source grid: `kx=(20,0,0)`, `ky=(0,20,0)`. Every arbitrary *permutation-invariant* spectral calibration is equal on the pair. The Gaussian IID calculation in ROT003 used pooling of energies over snapshots; it gave a valid but conservative 45,000-snapshot sufficiency gate. ROT038, however, exhibited a shared-volatility non-Gaussian scale mixture that breaks unconditional Gaussian independence. Can we find an exact **finite-n, per-snapshot calibration-invariant test** that remains valid under arbitrary unmeasured, potentially severe time variation in the *common within-snapshot gain*, including such non-Gaussian mixtures?

**ANSWER / AUTHOR PASS:** Yes, for an explicitly bounded **latent Gaussian plus a *common positive multiplicative scale*** family, including arbitrarily varying, dependent or sample-adapted shared scale. Instead of summing Fourier powers before taking a ratio, take a ratio **inside each snapshot**, then retain one binary sign relative to an exact threshold. Shared scale cancels **pathwise**, and the resulting signs are IID Bernoulli with source-fixed parameters regardless of the joint law of the shared gains. The 95% and 99% per-hypothesis **exact sufficient and minimal sample counts for this binary majority test** are 5,825 and 11,653, respectively; 85-decimal directed-interval checks strictly bracket each 95% and 99% crossing. These are *hypothetical complete RAW-site snapshots or equivalent two direct Fourier channels*, not measured data.

A second source-specific mathematical identity establishes an exact resource correspondence for this pair: **the error of the robust sign test with `2m-1` independent observations equals the error of the Gaussian fixed-gain pooled F-ratio test with `m` independent observations.** This is a comparison of two **specified tests**, NOT a universal information-theoretic lower bound for all robustness-preserving tests.

**Scientific priority and custody.** M13 FIRST original public N=41 sparse B-tensor source, unchanged original Git blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679`; the historical complete `dtc0a_runtime_v0_3_1.py` still unavailable. Geeky-S12 ROT038 FIRST the two anisotropic source-legal Gaussian site-noise A/B and the original six-plus-three nine-observer exact alias, plus nonGaussian dependence warning. Geeky-S13 ROT003 FIRST the permutation-invariant optimal Fourier pair and its Gaussian 45k sufficient test. Geeky-S13 ROT001 and ROT002 use a **different isotropic source A/B pair** and are NOT superseded. M15 ROT035–038 and AUD3 work with their own C4/C5 Gaussian-source and calibration contracts; ROT004 is not an amendment to their priority. Beta-prime, F, binomial/regularized-beta, invariance and scale-mixture calculus are standard mathematics; do **not** claim any general theorem or physical mechanism is novel.

Source documents, directly consulted:
- Original public M13 auxiliary: https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py
- Geeky-S12 ROT038: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s12/2026-11-21/IW_GEEKY_S12_ROT038_ORIGINAL_M13_ANISOTROPIC_DIRECTIONAL_EXACT_ALIAS_ONE_BOUNDARY_PROBE_ESCAPE_AND_NONGAUSSIAN_DEPENDENCE_001_20261121.md
- Geeky-S13 ROT003, SOURCE firstness: https://github.com/wmakiela-tech/Nash-iw-research/blob/e28c11e38cd97f3fda52c5cf882df99e034f22bd/research/geeky-s13/2026-11-22/IW_GEEKY_S13_ROT003_PERMUTATION_INVARIANT_ANISOTROPIC_FOURIER_ESCAPE_001_20261122.md
- Background identity (not a firstness source): https://stats.libretexts.org/Bookshelves/Probability_Theory/Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/05%3A_Special_Distributions/5.18%3A_The_Beta_Prime_Distribution and https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.betainc.html.

## 1. Original exact source parameters and fixed two-mode witness

The original anisotropic ROT038 A/B normalized covariance operators on the periodic 41³ RAW-site lattice are linear combinations of identity, three ±one-step axial, three ±one-step face diagonal, and ±one-step body diagonal averaging operators. With coefficient order `(beta0,beta_x,beta_y,beta_z,beta_xy,beta_xz,beta_yz,beta_body)`:

- `A=(1,1/25,1/25,1/25,1/30,1/30,1/30,2/25)`;
- `B=(1,1/20,3/100,1/25,1/30,13/300,7/300,2/25)`.

All seven neighboring coefficients are nonnegative and sum exactly `3/10` in either model. Every spatial eigenvariance is >= `7/10 > 0` by the operator norm bound. Neither these Gaussian laws nor the two RAW-site Fourier observations were part of authenticated physical M13 instrumentation.

Let `t=cos(40π/41)=-cos(π/41)` and source frequencies `kx=(20,0,0)`, `ky=(0,20,0)`. Exact rational source reduction gives:

```
v_A(kx) = v_A(ky) = 167/150 + (14/75)*t,
v_B(kx) = 82/75 + (31/150)*t,
v_B(ky) = 17/15 + t/6,
v_B(ky)-v_B(kx) = (1-t)/25 > 0.
```

Define `r_A=1`, `r_B=v_B(kx)/v_B(ky)=exp(-D)`, where actual source D is

`D=0.0862067053823047499958900523762503360439...`,
`r_B=0.9174045791555125245852005885283940...`.

The modes are permutation-related, so any *permutation-invariant* within-snapshot spectral response gives exactly the SAME positive gain for both modes, even if it is unknown, source-hypothesis-specific, unbounded and changes between snapshots. Their original deterministic N41 B-energy Fourier means vanish by the previously independently source-native M15 verified Fourier support (signed energy difference support within `[-6,6]×[-4,4]×[-2,2]`). This ROT004 did **not** reexecute M13 native `tensor_polys` or authenticate 41³ RAW recording; previous source support results are cited, not claimed newly re-derived.

## 2. Larger volatility family and exact cancellation theorem

For each hypothetical snapshot `t=1,...,n`, let `E_{x,t},E_{y,t}` be independent Exp(1) variables obtained from squared magnitudes of independent unit-variance circular complex Gaussian *latent* Fourier modes. Assume these **latent pairs are IID across t**. For the source X∈{A,B}, allow arbitrary positive random/calibration gains `g_{X,t}>0`, the SAME for BOTH permutation-related modes *within that snapshot*, possibly unbounded, varying between snapshots, mutually dependent, and even functions of the latent variables. Set the **observable Fourier energies**

`P_{x,t}=g_{X,t} v_X(kx) E_{x,t}`, `P_{y,t}=g_{X,t} v_X(ky) E_{y,t}`.

Hence for **every sample path**, not just in expectation,

`R_t=P_{x,t}/P_{y,t}=r_X E_{x,t}/E_{y,t}`.

This ratio has density `f_X(r)=r_X/(r_X+r)^2` on positive real r and is iid across t, whatever the positive common gains do. **No conditional independence or Gaussianity is asserted for the observed joint pair** `(P_x,P_y)` after marginalizing a random common scale; only the explicitly postulated *latent standardized Gaussian* structure is needed for the exact distribution of `R_t`. The ratio's log has the familiar shifted logistic law.

The concrete ROT038 nonGaussian shared-volatility witness `g_t=S_t` with independent `S_t∈{1/2,3/2}` (each with probability 1/2) fits this family: `E[S_t]=1` preserves each source Gaussian base-site covariance after multiplication of raw site amplitudes by `sqrt(S_t)`, but `Var(S_t)=1/4` produces nonzero fourth-order cross dependence. Thus ROT038's warning that zero covariance DOES NOT IMPLY independence is **preserved**, while the new per-snapshot ratio statistic is rigorously valid for THIS DECLARED subclass of nonGaussian observations. Unrestricted nonGaussian site laws do **not** automatically satisfy this theorem.

## 3. Exact finite-n majority-of-ratios test

Set `theta=sqrt(r_B)=exp(-D/2)=0.95781239246290425...`. For each snapshot record just the one bit

`Y_t = 1{R_t < theta}`.

From the ratio of independent exponentials, `Pr(E_x/E_y<z)=z/(1+z)` for z>0. Consequently

`p_A=Pr_A(Y_t=1)=theta/(1+theta)=0.4892258298855631800784550938963529...`,
`p_B=Pr_B(Y_t=1)=1/(1+theta)=1-p_A`.

With odd n, define `K=sum Y_t` and decide **B iff `K >= (n+1)/2`**. These are the Bayes optimal and balanced minimax decisions **among tests of the n binary signs with equal priors**. Type-I and type-II errors coincide exactly:

`e_n = Pr[Binomial(n,p_A) >= (n+1)/2]`.

For n=2m-1, `e_n = I_{p_A}(m,m)`. The exact point-value gates at 100 digits, supplemented by 85-decimal *outward interval sums for the 95% and 99% thresholds*, are:

| Per-hypothesis correct classification | First sufficient odd n for sign-majority | Source-model conditional error at n | Error at previous odd n-2 |
|---|---:|---:|---:|
| >90% | 3,537 | 0.0999604417679 | 0.100024037180 |
| >95% | **5,825** | **0.0499985953797** | **0.0500277249998** |
| >99% | **11,653** | **0.00999746178321** | **0.01000278276093** |
| >99.9% | 20,561 | 0.000999987619416 | 0.00100049379136 |

For p_A<1/2, `e_{2m-1}-e_{2m+1} = C(2m-1,m-1) p_A^m (1-p_A)^m (1-2p_A) > 0`, so strict checks at n and n-2 certify minimality over odd n. For even n the balanced test with randomized 50/50 tie has the EXACT same error as at n−1; therefore the displayed odd numbers also give minimal total n **for this binary-sign majority family**. The 90% and 99.9% values are high-precision point computation plus independent SciPy checks; the **95% and 99% comparisons against their nearest predecessors are additionally certified by full directed IV85 recurrence**. This is not a claim that such sample counts are physically available.

## 4. Exact 2m−1-to-m resource identity with fixed-gain pooling

If the gain is constant through all snapshots, the source-Gaussian original ROT003 pooled-power statistic `Sx/Sy` (sums of 2n real cosine/sine squares) has `F_{2m,2m}` under A, and `r_B * F_{2m,2m}` under B. The equal-error decision threshold is the same `theta=sqrt(r_B)`. Since

`Pr(F_{2m,2m} < theta) = I_{theta/(1+theta)}(m,m) = Pr(Bin(2m-1,p_A) >= m)`, 

**the error of the *specified* pooled fixed-gain test after m snapshots is EXACTLY EQUAL to the error of the robust one-bit-per-snapshot sign test after 2m−1 snapshots**. In this instance:

- >95% at m=**2,913** fixed-gain pooled observations versus n=**5,825** common-gain-varying robust sign observations;
- >99% at m=**5,827** versus n=**11,653**;
- >99.9% at m=**10,281** versus n=**20,561**.

This exact identity follows from classical regularized-beta/F/binomial identities, not a new probability law. It is an experimentally meaningful *conditional resource comparison* in source-typed mathematical terms. It does NOT prove every possible test under arbitrary gain requires nearly double the observations; in particular retaining the FULL ratios rather than one bit can recover information.

## 5. Strict falsification of the original pooled F claim under arbitrary varying gains

For each fixed n≥2, take a permitted **positive shared gain sequence** with `g_1=M`, `g_2=...=g_n=1` and M→∞. Then the pooled statistic becomes

`(M v_x E_{x,1}+Σ_{t>1}v_x E_{x,t})/(M v_y E_{y,1}+Σ_{t>1}v_y E_{y,t}) → r_X E_{x,1}/E_{y,1}` almost surely.

Thus the old pooled ratio at threshold theta has, for EACH source hypothesis, limiting *misclassification probability* `p_A≈0.48922582988556`, regardless of how many total snapshots n there are. The unqualified old `F_{2n,2n}` probability certificate is FALSE over the expanded arbitrary-gain nuisance family. The robust sign test remains binomial because each ratio cancels the gain before aggregating.

This is a deliberately adversarial mathematical nuisance sequence, not a claim that M13 physical calibration behaves so extremely or that every nonGaussian noise law is of this form. Shared scale mixture can also violate the pooled F law without this extreme example. The original ROT003 fixed-gain gaussian guarantee remains valid **in its declared scope**.

Other failure modes and strict boundaries:

1. If gain is frequency-direction-specific (`g_x,t != g_y,t`), an A fit with `g_x/g_y = r_B` and a B fit with `g_x/g_y = 1` makes both *entire observed ratio laws* the same. A shared gain assumption is indispensable.
2. Additive noise or a common additive offset does NOT algebraically cancel from energy ratios; no corresponding robustness claim.
3. For arbitrary nonGaussian latent energies, including correlated or degenerate latent pairs, the ratios need not have the beta-prime/logistic law. The independent latent Gaussian or equivalent Exp(1) radial structure is indispensable.
4. A single snapshot is not guaranteed accurate: the equal-prior binary test succeeds only `1-p_A≈0.51077417`. Finite-n improvement requires IID latent pairs; gain independence across time is *not* necessary.
5. This two-mode RAW Fourier acquisition is hypothetical, not among the original five fixed M13 cube masks plus mathematical global mean; neither original historical complete DTC0a code nor actual N41³ site-level apparatus has been recovered.

## 6. Actual reproducibility, independent numerical implementation and acceptance ceiling

New PRIMARY source-typed Python independently reconstitutes exact source rational anisotropic coefficients of ROT038 and exact line spectra; verifies source SPD and analytic difference `(1−t)/25`; obtains D, r_B, theta and p with 100-digit mpmath point arithmetic plus directed 85-decimal `mpmath.iv` intervals; computes **binomial tails by independent positive-term recurrences**, not depending on normal approximation or opaque incomplete-beta library; and establishes **nonoverlapping 95%/99% error-threshold intervals** both before and after each claimed minimal odd n. Four different finite resource gates are computed; the 90% and 99.9% gates are point-precision checks, not falsely claimed IV85.

A NEW SECOND independently written SciPy+NumPy referee (no imports from primary source) reconstructs ROT038 source coefficients and pair spectra, computes binomial survival probabilities, F CDF and regularized beta CDF, checks the exact identities at all four resource gates, and simulates **synthetic** independent exponential latents under wildly varying shared gains (`exp(linspace(-15,15,2000))`), verifying that *every sign-bit event is identical* with/without shared gain. A separate deterministic gain-dominance fixture explicitly falsifies pooled-F transfer. This is an algorithmically independent **SAME-CELL** numerical control, not different-cell I1 review nor a real observed experiment.

Both original-source reports have been directly read with authorized connected GitHub access. This ROT004 does **not** claim byte-exact reproduction of the missing historical DTC0a producer or execution of the M13 native Fourier source module. Actual new code, complete deterministic result JSONs, cold Python -I replay receipts, explicit adversarial mutation fixtures, README and SHA256 manifest are included in the user-local ZIP. Only the scientific report is to be placed in the public GitHub source repo; unless separate code files are in fact posted and byte-read back, they must not be called a public code mirror. GitHub/Slack delivery is not scientific owner acknowledgement.

**Review request for an independent different-cell I1:** Independently derive ROT038 rational Bx/By and the latent two-mode exponential-normalization step; verify cancellation even for adaptively correlated `g_t`; verify `p_B=1-p_A`; certify the very narrow 95% n=5825 threshold using rigorous binomial bounds, verify n=5823 fails, derive the `I_p(m,m)` / `F_(2m,2m)` / `Bin(2m−1,p)` exact identity, find any counterexample under the declared common-scale latent Gaussian assumptions, and check the extreme shared-gain pooled-F failure. DO NOT import ROT004 author report as an independent computation without declaring exposure. Separate actual original-M13 source-native run and instrument/physical characterization remain outside the current scope.

**Final ceiling:** `SOURCE_TYPED_EXACT_LATENT_GAUSSIAN_SHARED_GAIN_SIGN_THEOREM / SOURCE_IV85_95_AND_99_MINIMA_PASS / SAME_CELL_INDEPENDENT_SCIPY_BETA_F_BINOMIAL_PASS / EXACT_SPECIFIED_TEST_2M_MINUS_1_VS_M_RESOURCE_IDENTITY_PASS / SHARED_VOLATILITY_MIXTURE_REPAIR_PASS / POOLED_F_ARBITRARY_GAIN_FAIL / ORIGINAL_M13_NATIVE_NOT_EXECUTED / NO_PHYSICAL_RAW_SITE_SENSOR / DIFFERENT_CELL_I1_PENDING / BW_PENDING / NO_GENERAL_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE`.
