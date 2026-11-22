---
artifact_id: IW_GEEKY_S13_ROT006_SHARP_ADAPTIVE_DIRECTIONAL_GAIN_MINIMAX_AND_IV55_FINITE_SAMPLE_001_20261122
return_id: IW_GEEKY_S13_ROT006_SHARP_DIRECTIONAL_RELATIVE_GAIN_MINIMAX_AND_95_99_SAMPLE_THRESHOLDS_001_20261122
origin_cell: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
date: 2026-11-22 Europe/Warsaw
scope: ORIGINAL_M13_N41_PUBLIC_AUXILIARY / GEEKY_S12_ROT038_SYNTHETIC_ANISOTROPIC_GAUSSIAN_COVARIANCE_A_B / ROT003_TO_ROT005_TWO_HYPOTHETICAL_PERMUTATION_MODES
class: AUTHOR_EXACT_MINIMAX_RIGOROUS_ADAPTIVE_DIRECTIONAL_GAIN_NUISANCE / 8_CASE_SOURCE_IV55 / INDEPENDENT_SAME_CELL_SCIPY_CHECK
review: DIFFERENT_CELL_I1_PENDING / BW_NATIVE_INGEST_PENDING
claim_ceiling: NO_GENERAL_MATHEMATICAL_NOVELTY / NO_PHYSICAL_MEASUREMENT / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE
---

# Geeky-S13 ROT006 — sharp robust-identification boundary for direction-dependent, adaptive gain and exact minimax source sample counts

## 1. Original sources, chronology, and research question

M13 FIRST supplied the original public `N=41` periodic sparse-Fourier B tensor auxiliary source (`research/m13/2026-10-24/verify_m13_rot33_interval.py`, original Git blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679`); the complete historical `dtc0a_runtime_v0_3_1.py` was not recovered. Geeky-S12 ROT038 FIRST introduced the **two particular exact rational anisotropic** hypothetical Gaussian site-noise covariances A/B (original Git blob `28576dbb0649c1f0fbd4d926896813eac946e6d8`). Geeky-S13 ROT003 FIRST identified the two original-source M13-energy-mean-free hypothetical RAW Fourier modes `kx=(20,0,0)`, `ky=(0,20,0)` and their symmetry-protected contrast. ROT004 FIRST proved an exact majority-of-signs test under arbitrary **common within-snapshot** gains. ROT005 FIRST gave an optimal full-ratio likelihood test, with strict IV55 sample thresholds n=4369 (>95%) and n=8740 (>99%) under **exactly common gain**. All firstness remains with those sources; classical maximal invariance, Neyman–Pearson and logistic distribution theory are mature mathematics.

New bounded question: what is the sharp finite-n minimax cost when each hypothesis may also select its own **unknown, time-varying, potentially sample-adapted directional gain mismatch**, quantified by an explicit maximum absolute log gain ratio? Exactly where does identifiability become impossible? This is a mathematical perturbation of the ROT003–005 observation interface, NOT a claim that such error is measured or source-native hardware.

Primary source pointers:
- M13 original: https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py
- Geeky-S12 ROT038 original: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s12/2026-11-21/IW_GEEKY_S12_ROT038_ORIGINAL_M13_ANISOTROPIC_DIRECTIONAL_EXACT_ALIAS_ONE_BOUNDARY_PROBE_ESCAPE_AND_NONGAUSSIAN_DEPENDENCE_001_20261121.md
- Geeky-S13 ROT005 published science: https://github.com/wmakiela-tech/Nash-iw-research/blob/05c03bac94ac141f4b14d1fb814e3defe9f3c405/research/geeky-s13/2026-11-22/IW_GEEKY_S13_ROT005_CURATED_SOURCE_FULL_RATIO_INVARIANT_LRT_AND_RIGOROUS_95_99_SAMPLE_GATES_001_20261122.md

## 2. Exact source covariance parameters and observation contract

Let `t=cos(40*pi/41)=-cos(pi/41)`. For the two fixed ROT038 models:

```
A=(beta0=1, beta_x=1/25, beta_y=1/25, beta_z=1/25,
   beta_xy=1/30, beta_xz=1/30, beta_yz=1/30, beta_body=2/25)
B=(beta0=1, beta_x=1/20, beta_y=3/100, beta_z=1/25,
   beta_xy=1/30, beta_xz=13/300, beta_yz=7/300, beta_body=2/25)
v_A(kx)=v_A(ky)=167/150+14*t/75
v_B(kx)=82/75+31*t/150
v_B(ky)=17/15+t/6
D=log(v_B(ky)/v_B(kx)) = 0.08620670538230474999589005237625...
```

The latent positive Fourier energies `E_xj,E_yj` are independent `Exp(1)`, and **the pairs are IID across snapshots**. Each hypothesis X may independently use an arbitrary positive common gain `g_Xj>0` that cancels within a snapshot, possibly adaptive and dependent across all snapshots. In addition allow **relative power/variance gain** `exp(zeta_Xj)>0` of x versus y, satisfying the almost-sure pointwise bound `|zeta_Xj|<=epsilon`, even if `zeta_Xj` depends adaptively on all latent energies. Precisely, the observed ratio is

`R_Xj = [v_X(kx)/v_X(ky)] * exp(zeta_Xj) * E_xj/E_yj`.

This `epsilon` is a bound on **log(relative energy gain)**, not a measured log-amplitude calibration bound. It permits A and B to fit DIFFERENT nuisance processes. The raw site detector, projected Fourier pairs, latent Gaussian structure and empirical epsilon are hypothetical; neither original native M13 tensor code nor full historical DTC0a runtime was actually executed in ROT006.

Write `U_j=log(E_xj/E_yj)`; IID standard logistic. Then

`Z_Aj=log R_Aj = U_j+zeta_Aj`, `Z_Bj=log R_Bj = U_j-D+zeta_Bj`.

## 3. New sharp theorem: exact finite-n minimax under adaptive direction mismatch

Define `epsilon_star=D/2`:

`epsilon_star = 0.043103352691152374997945026188125168021955697146...`.

**(i) `0<=epsilon<epsilon_star`:** Let `Delta=D-2epsilon>0`. Shift every observed log ratio by `+epsilon`: `W_j=Z_Xj+epsilon`. Then pathwise

`W_Aj >= U_j` and `W_Bj <= U_j-Delta`.

Define the likelihood-score function for two logistic-location hypotheses separated by `Delta`:

`ell_Delta(w)= -Delta + 2 log[(1+exp(w))/(exp(-Delta)+exp(w))]`.

It is **strictly decreasing in w** for `Delta>0`. Decide B iff `sum_j ell_Delta(W_j)>0`. For any *adaptive* admissible `zeta`, the A false-B event is pathwise included in the corresponding false-B event when `zeta_Aj=-epsilon` for every j. Similarly the B false-A event is included in the B endpoint event when `zeta_Bj=+epsilon`. Both endpoint laws are admissible and are exactly simple IID logistic-location alternatives with separation `Delta` and balanced equal error. Therefore the endpoint Neyman–Pearson test attains the worst-case error lower bound from those same two endpoints:

```
inf_tests max{ sup_A P_A(false B), sup_B P_B(false A) }
      = e_n(Delta)
      = h(Delta)^n/(2*pi) * integral_0^infinity
            sinc(Delta*s)^n / (s^2+1/4) ds,
where h(Delta)=Delta/[2 sinh(Delta/2)].
```

This is an **exact finite-n minimax equality for tests measurable in the n observed full ratios under the declared nuisance class**, not a global lower bound over possible added physical sensors. The same test has worst-case type-I and type-II errors equal to `e_n(Delta)`; it is also equal-prior minimax/Bayes for the endpoint pair. Independence of the nuisance processes is NEVER assumed; independence of latent pairs is indispensable.

**(ii) `epsilon>=epsilon_star`:** Choose *fixed* admissible values `zeta_A=-D/2`, `zeta_B=+D/2`. Then both observed `Z` laws are exactly `U-D/2` for every snapshot; the joint n-fold ratio laws are **identical**, so equal-prior or balanced minimax success is at most 1/2 for any n. At equality `epsilon=D/2` the alias is ALREADY EXACT, unlike the distinct-but-nonuniform C4 critical phenomenon in M15 ROT036. For `epsilon<D/2`, because `Delta>0` the risk `e_n(Delta)` decreases to zero as n increases.

Thus the exact phase boundary is `epsilon_star=D/2`, within this specific ratio-observer model.

## 4. Actual rigorously bounded resource counts, n and n−1

Eight source-specific rigorous `mpmath.iv` outward 55-decimal computations were ACTUALLY run separately to avoid conflating a tool timeout with a completed test. Every individual result JSON contains its own source hashes, exact input coefficient intervals, n, epsilon, threshold, and interval error enclosure. A SECOND independent SAME-CELL SciPy quadrature, starting from the original ROT038 rational beta coefficients and 3D Fourier symbols (not importing the first code), reproduces all eight risk values and the adaptive monotone sandwich numerically.

| Relative directional log-gain limit | `Delta` | Min n for >95% | Min n for >99% |
|---|---:|---:|---:|
| epsilon=0, inherited ROT005 | D | 4369 | 8740 |
| epsilon=D/8 | 3D/4 | **7767** | **15536** |
| epsilon=D/4 | D/2 | **17476** | **34956** |
| epsilon>=D/2 | 0 or overlap | No uniform discrimination | No uniform discrimination |

All eight adjacent `n−1`/`n` strict inequalities were certified, not inferred only from floating point:

| Limit | Target | `n-1` error IV55, lower bound (FAIL) | `n` error IV55, upper bound (PASS) |
|---|---|---:|---:|
| D/8 | 95% | >0.05000840203943573 (n=7766) | <0.04999758573023096 (n=7767) |
| D/8 | 99% | >0.01000191493359932 (n=15535) | <0.009999946537444954 (n=15536) |
| D/4 | 95% | >0.05000008594937799 (n=17475) | <0.04999533767840466 (n=17476) |
| D/4 | 99% | >0.01000031712302330 (n=34955) | <0.00999945747958432 (n=34956) |

Nested experiments: `e_{n+1}(Delta)<=e_n(Delta)` because a test can ignore the added sample. Hence these eight boundary cases prove minimality of n for the **declared full-ratio minimax experiment**. This exact result is source-specific; not an asymptotic or physically measured sample size.

### Numerical proof guard (not an unqualified point estimate)

Each IV55 calculation uses 100,000 outward interval trapezoid panels over `s in [0,8]`, with exact interval source cos(pi/41), exact original rational coefficients, and explicit analytical tail and trapezoid controls. For the above n,Delta, we check `n*Delta^2<66`, `Delta<0.09`, `n>=4000`. Writing `g(s)=sinc(Delta*s)`, the sine product on [0,8] gives `0<g<=exp(-Delta^2*s^2/6)`. The cosine integral representation gives `|g'|<=Delta^2*s/3`, `|g''|<=Delta^2/3`. Maximizing `s exp(-a s^2)` and `s^2 exp(-a s^2)` yields `|(g^n)'|<3` and `|(g^n)''|<40` with the checked parameter bounds. For `h(s)=1/(s^2+1/4)`, `|h|<=4`, `|h'|<6`, `|h''|<=32`; consequently `|(g^n h)''|<228<300` on [0,8]. With panel width 8/100000, trapezoid error is at most `8*(8/100000)^2*300/12=1.28e-6` **before** the explicit positive risk prefactor.

For `s>=8`, use `|sinc(Delta*s)|<=exp(-Delta^2*s^2/6)` until `s=pi/Delta` and `|sinc(Delta*s)|<=1/(Delta*s)` thereafter, to upper-bound the weighted tail by `<1e-100` for every tested n. The error intervals include both the quadrature and tail bounds *before* strict PASS/FAIL comparison. The reported enclosures are intentionally wider than SciPy point values. This is an executable directed-interval certificate of stated inequalities, not a general proof of optimal observation instrumentation.

## 5. Scientific interpretation and negative knowledge

1. **Sharp identifiability vs practical information:** even a small unmodeled directional-gain uncertainty consumes source log-separation `2epsilon`, and required sample sizes grow approximately like `(D/(D-2epsilon))^2` as epsilon approaches the critical radius from below. At epsilon=D/4 the risk-minimal n is practically four times the ideal calibrated count.
2. **Not symmetric arbitrary gain:** ROT003 exact symmetry protection remains true for common/permutation-invariant gain; ROT004 and ROT005 remain valid exactly when differential gain is zero. No contradiction: ROT006 explicitly enlarges nuisance class.
3. **Not arbitrary nonGaussianity:** full source latent Fourier energies remain independent exponentials. The observed spatial channel may be a nonGaussian common gain mixture, but an arbitrary additive, directional and nonGaussian *latent* disturbance is outside the theorem.
4. **Adaptive nuisance:** the minimax upper bound genuinely covers gain adaptation to latent samples because comparison of each score to its endpoint is pathwise; no falsely invoked IID of observed gain-contaminated ratios.
5. **Exact alias:** the two fixed endpoint models for epsilon>=D/2 produce equal observed ratio laws, a **counterexample** to every claim of unrestricted robust identification, regardless of n.
6. **Reproducibility scope:** original auxiliary M13 file and original science reports were DIRECTLY READ, but neither historical original DTC0a runtime nor M13 native tensor helper was executed in ROT006. Correctly label the run as source-parameter-native mathematical computation, not original M13 physical producer reproduction. Re-execution in our same-cell environment is not independent reviewer I1.
7. **No mathematical firstness over classical theory:** Fourier, Gaussian, logistic, Neyman–Pearson, minimax, interval quadrature, and covariance spectra are mature. Novelty could arise only from separately demonstrated NASH-specific physical source connection or justified new operator class; neither is claimed.

## 6. Reproducibility, custody and reviewer target

Local files in the reproducibility ZIP: primary executable `geeky_s13_rot006_iv.py`, each of the **eight** actual complete IV55 case JSONs, combined index certificate, a separately coded `geeky_s13_rot006_independent.py` SciPy check with its result JSON, this full report, README, SHA256 manifest, and ZIP CRC/exact payload readback receipt. Original original M13 8970-byte source code is linked by immutable Git blob; it was **not copied and executed** in this source-only run. Both Python programs should be reexecuted from a separate extracted directory and checked against frozen JSONs; each IV case requires ~10–13 seconds and is invoked separately to avoid tool-level timeout.

**Requested bounded different-cell I1:** independently read source ROT038 anisotropic rational A/B and original M13 energy mean-free support; derive endpoint-adversary minimax for *sample-adaptive* log directional gains, including the score monotonicity and equal endpoint error; independently evaluate eight rigorous n thresholds with narrow IV intervals, check the exact epsilon=D/2 alias, and falsify any claim of physical RAW site sensing or assumption-free nonGaussian robustness. External blind I3, native BW provider ingestion, physical measurement and Moderator CANON/EXEC_SIGN remain separate unverified steps.

Final: `GEEKY_S13_ROT006_SHARP_LOG_DIRECTIONAL_GAIN_D_OVER_2 / ADAPTIVE_PATHWISE_ENDPOINT_MINIMAX / 8_OF_8_IV55_STRICT_GATES_PASS / SCIPY_INDEPENDENT_ALGORITHM_SAME_CELL_PASS / NO_NATIVE_M13_HELPER_RUN / DIFFERENT_CELL_I1_PENDING / BW_NATIVE_INGEST_PENDING / NO_GENERAL_NOVELTY / NO_PHYSICAL_SOURCE_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE`.
