---
artifact_id: IW_GEEKY_S13_ROT001_N41_FULLFIELD_CINFTY_AXIAL_CALIBRATION_ALIAS_001_20261122
origin_cell: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
date: 2026-11-22 Europe/Warsaw
program: IW/NASH / P3 / source M13 Fourier B N41
class: ORIGINAL_SOURCE_CONDITIONAL_FINITE_GRID_CYCLOTOMIC_INTERPOLATION_GAUSSIAN_FULLFIELD_ALIAS
status: AUTHOR_MATHEMATICAL_PROOF / LOCAL_EXECUTED_INDEPENDENT_SITE_ROLL_VS_FFT_NUMERIC_DIAGNOSTIC_PASS / DIFFERENT_CELL_I1_PENDING
source_scope: ORIGINAL_M13_N41_GRID_AND_GEEKY_ROT035_SYNTHETIC_ISOTROPIC_STATIONARY_NOISE_PAIR
source_execution: ORIGINAL_M13_HELPER_NOT_EXECUTED_IN_THIS_ROTATION
sync: LOCAL_VERIFIED / GITHUB_AND_BW_PENDING_UNTIL_ACTUAL_WRITE_ACK
claim_ceiling: NO_GENERAL_NOVELTY / NO_PHYSICAL_SENSORS / NO_HISTORICAL_FULL_DTC0A_RUNTIME / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE
---

# Geeky-S13 ROT001 — Full-field exact Gaussian indistinguishability under unrestricted smooth *axial-only* spectral calibration on the original N=41 M13 lattice

## 0. Science-first question, source firstness and currentness

Prior M15 ROT035: five original-source high-frequency, mean-free Fourier pairs distinguish two fixed Geeky ROT035 hypothetical Gaussian stationary site-noise hypotheses against separately fitted arbitrary C4 log spectral calibration `phi_X(a)`, **provided the known bound** `||phi_X''''||_infinity <= L < 7.2115097831082...`; at the threshold a five-pair exact alias exists. M15 ROT036 (2026-11-22 10:47 CET, after ROT035) added an unbounded face-diagonal slope, falsified transfer of that five-mode result, and found a six-mode Peano-kernel threshold `Lstar≈15.84944` for that DIFFERENT calibrated observer; at equality no exact C4 alias, but lack of uniform finite-N separation. Those are M15's original source results and not claimed here.

NEW bounded *far-consequence* question: if there is **no numerical regularity bound at all**, but the log calibration is still `C-infinity` and depends **only on the axial one-number symbol `a(k)`**, does access to the *entire* original M13 41^3 site field guarantee that distinct isotropic stationary Gaussian covariance hypotheses remain distinguishable? Source-scoped answer: **NO**. This no-go holds even for an arbitrarily large number of repeated full site recordings because the two composite model families contain **exactly the same full 68,921-dimensional Gaussian law**. The original field's deterministic mean is kept fixed and identical between hypotheses.

This is a source-specific consequence of *standard* prime cyclotomic irreducibility, finite-node interpolation and Gaussian covariance diagonalization; **no claim of novelty in general algebra, statistics, nonparametric inverse problems, or physics**.

Original source priority preserved: M13 first authored original N=41 B sparse Fourier/TT auxiliary source, 41 tensor modes, five fixed observation windows `k=2..6`, and mathematical full-domain `k=0`. Original source helper, public Git blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679`, SHA256 previously certified by M15 `cd4aad089bf68e2e6155ff048d4d812943495dcf1770c8acbf0ff8111b1deb9c`; original B25 data blob `a6f50fbe5904e580e84c87ee87c5ad043cdec5d0`. ROT001 read the actual original Git source and reused the source's **N=41 mathematical setting**, but **did not import or execute the original M13 helper**, did not recover the full historical `dtc0a_runtime_v0_3_1.py`, and did not reproduce an original physical simulation. The model-noise hypotheses and hypothetical raw full-site observer belong first to Geeky-S12 ROT035, not M13 physical hardware.

Upstream source documents:
- M13 actual source: https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py
- Geeky-S12 ROT035 two original-source conditional rational Gaussian covariance witnesses: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s12/2026-11-17/IW_GEEKY_S12_ROT035_EXACT_RATIONAL_M13_SIX_MASK_COVARIANCE_KL_INDISTINGUISHABILITY_AND_SITE_AGGREGATION_INFORMATION_LOSS_001_20261117.md
- M15 ROT035 actual original source published math: https://github.com/wmakiela-tech/Nash-iw-research/blob/965d7fbb00334c1c34e7a92d059720ff75c24e88/research/m15/2026-11-22/IW_M15_ROT035_ORIGINAL_M13_SHARP_C4_SMOOTH_SPECTRAL_CALIBRATION_ROBUSTNESS_RADIUS_001_20261122.md
- M15 ROT036, explicitly newer: https://github.com/wmakiela-tech/Nash-iw-research/blob/050447888d17c4dfe712ed1bf5260306c77dfe05/research/m15/2026-11-22/IW_M15_ROT036_ORIGINAL_M13_FACE_ANISOTROPY_C4_SHARP_PEANO_SOURCE_FALSIFIER_001_20261122.md

## 1. Exact declared mathematical model

Let `G=(Z/41Z)^3`, |G|=41^3=68,921. At each spatial site observe an original M13 fixed energy-mean `mu(s)` plus hypothetical additive zero-mean *stationary Gaussian* site noise. Two fixed source-hypothesis covariance spectra A and B are exactly those introduced by Geeky ROT035 and used by M15 ROT035/036.

For `k in G`, let `c_j=cos(2*pi*k_j/41)`, and define

```
a(k)=(c_x+c_y+c_z)/3,
f(k)=(c_x*c_y+c_x*c_z+c_y*c_z)/3,
h(k)=c_x*c_y*c_z.

v_X(k) = beta0_X * (1 + theta_axial_X*a(k)
                         + theta_face_X*f(k)
                         + theta_body_X*h(k)).
```

Exact rational source parameters:

```
A beta0=1, theta_axial=3/25, theta_face=1/10, theta_body=2/25.
B beta0=99779719687217/100000000000000,
  theta_axial=316869474178226/2494492992180425,
  theta_face=93110637627687/997797196872170,
  theta_body=205860943554709/2494492992180425.
```

`v_A`, `v_B` are strictly positive at all modes: analytically `beta0_X*(1-sum(theta_X))>0` for the stipulated positive weights; A lower bound `0.7`, B bound approximately `0.695594392151309`. Both source site covariance matrices are symmetric positive definite. The identical mean `mu` is unaffected by the declared noise covariance.

**NEW more adversarial model class:** Candidate X may independently fit any real `phi_X∈C^infinity(R)` (not necessarily polynomial and with no specified size or derivative bound) as a function only of `a`:

```
V_X(k;phi_X) = v_X(k) * exp(phi_X(a(k))).
```

`phi_A` and `phi_B` need not coincide. This calibration preserves a positive, real and even Fourier spectral covariance, hence real SPD Gaussian site covariance, but generally induces *arbitrarily nonlocal* spatial noise; it is **not** an actual M13 source-native site/noise mechanism. It is NOT the M15 bounded `||phi''''||<=L` class and not a physical detector calibration.

## 2. Lemma: axial symbol `a` labels exactly 1771 distinct unordered frequency triples

Each coordinate `k_j mod 41` has a unique *absolute frequency class* `u_j=min(k_j mod 41, 41-(k_j mod 41)) in {0,...,20}`. Distinct sorted triples `(u_x,u_y,u_z)` have distinct exact sums of their three cosines.

**Proof, not a floating-point inference.** Let `zeta=exp(2*pi*i/41)` be a primitive root. Suppose two triples have equal cosine sums. Let integer `d_j` be the difference in multiplicity of class `j=0,...,20`; thus `sum_(j=0..20) d_j=0`. Equality of sums gives

```
P(zeta) = 2*d_0 + sum_(j=1..20) d_j*(zeta^j+zeta^(41-j)) = 0.
```

`P∈Z[X]`, degree at most 40. Because 41 is prime, its cyclotomic polynomial is the **irreducible** `Phi_41(X)=1+X+...+X^40` of degree 40. Hence `P(X)=q*Phi_41(X)` for some rational `q`. Compare coefficients: `2*d_0=q` and `d_j=q` for each `j>=1`. Therefore `0=sum_j d_j=d_0+20*(2*d_0)=41*d_0`, so all `d_j=0`. The sorted triples are equal. QED.

The number of unordered triples drawn with repetition from 21 coordinate classes is `C(21+3-1,3)=C(23,3)=1771`. Each triple stands for signed and permuted frequencies; their combined orbit sizes exactly sum to `41^3=68921`.

**Material arithmetic dependence:** The uniqueness result is tied to the *prime* modulus N=41 and the precise sum-of-cosines axis symbol, rather than to generic cubic grids or continuous Fourier space.

## 3. Full-field indistinguishability theorem and constructive C-infinity witness

**THEOREM (source-scoped).** For the two fixed original Geeky ROT035 isotropic source noise spectra above, there exist two separately permitted smooth axial-only log-calibrations `phi_A, phi_B ∈ C^infinity(R)` such that

```
V_A(k;phi_A) = V_B(k;phi_B)     for EVERY k∈(Z/41Z)^3.
```

Consequently the entire **68,921-dimensional Gaussian spatial noise distributions** coincide exactly, and with their common original deterministic M13 mean, the complete **full RAW-site Gaussian observation distributions** coincide. Every measurable derived observation, including all old masks, all local probes, all Fourier modes and any nonlinear statistics, therefore has identical law under the two composite hypotheses. For every number n of IID complete spatial snapshots the equal-prior maximum binary accuracy for these two indistinguishable members is **exactly 1/2**. There is no uniformly successful test over this unrestricted composite calibration class, independent of n.

**Proof/construction.** Enumerate the `1771` sorted triple representatives indexed `j`, with unique real axial nodes `a_j`, and define finite real values

```
d_j = log[v_A(k_j)/v_B(k_j)].
```

The isotropic spectral functions `v_A/v_B` are symmetric in coordinate permutations and sign reversals, so **all modes sharing the same `a_j` have the same d_j**. Set `phi_A(a)=0`. Let `Delta_min=min_(i != j)|a_i-a_j|>0`, and `r=Delta_min/3`. Define a standard `C^infinity` compact bump

```
b(u) = exp(1-1/(1-u^2))   if |u|<1;
       0                    if |u|>=1.
```

Then `b(0)=1` and its derivatives of all orders vanish at the support boundary. Because the 1771 open support intervals `(a_j-r,a_j+r)` are disjoint, the finite sum

```
phi_B(a) = sum_(j=1..1771) d_j * b((a-a_j)/r)
```

is a globally smooth, real-valued function and satisfies `phi_B(a_j)=d_j` **exactly** for every source frequency orbit. Therefore for any source mode `k` with `a(k)=a_j`,

```
v_B(k)*exp(phi_B(a(k)))
     = v_B(k)*exp(log(v_A(k)/v_B(k)))
     = v_A(k) = v_A(k)*exp(phi_A(a(k))).
```

All real Fourier eigenvariances agree. The two covariance matrices, related to these spectra by invertible discrete Fourier conjugation, are exactly identical. Their means agree by hypothesis, so their centered multivariate Gaussian laws agree. Tensor powers preserve the equality. QED.

An alternative purely algebraic construction is the unique interpolating polynomial `p(a)` of degree at most 1770 through the same `(a_j,d_j)` nodes. This also belongs to `C^infinity`; its actual evaluation could be ill-conditioned and is **not needed** for the exact theorem. The compact-bump construction is explicit and avoids an unproved numerically stable degree-1770 interpolation claim.

**No contradiction with M15:** The bump functions have some finite but potentially enormous fourth-derivative sup norm; no bound such as 3 or 7.21151 is asserted or satisfied. Source M15 ROT035/036 legitimately prove positive discrimination under a known *small enough* bound. Structural `C^infinity` regularity alone, without a numerical bound, is insufficient on this finite prime torus.

## 4. Actually executed independent numerical and falsification controls

A newly authored, standalone Python executable uses the exact source rational A/B parameters and numpy/mpmath; does NOT import M15's code or original M13 tensor helper:

1. `itertools.combinations_with_replacement(0..20,3)` gives **1771** orbit representatives, and exact integer orbit multiplicities sum **68,921**.
2. `mpmath` 65-decimal precision yields a strictly positive *diagnostic* minimal `a` spacing `0.0000039624113735067002482884409871204`, for nearest representative triples `(2,15,19)` and `(5,13,20)`; chosen global bump support radius `0.0000013208037911689000827628136623735`. Positivity is rigorously established by the cyclotomic lemma, not by a numerical threshold.
3. Interpolation evaluation at 1771 representative nodes gives zero residual at mpmath precision by exact bump identity; explicit off-grid midpoint bump tests check disjoint supports.
4. Construct all 68,921 source full-grid Fourier spectral variances; matching under `phi_B` yields maximum relative variance discrepancy **2.1628015595158026e-16** in binary64; maximum log variance difference **1.6653345369377348e-16**.
5. **Independent numerical operator route:** implement all signed 6 axial, 12 face and 8 body nearest-neighbor periodic shift averages directly on random `41^3` spatial arrays, independently compare to the Fourier multiplier formula. Relative L2 discrepancy `4.46e-16` for A and `4.50e-16` for B. This verifies the declared site-noise spectral formula but is not a reexecution of M13 tensor physics.
6. **Upstream positive-threshold control:** independently recompute M15 ROT035's five-mode C4 sharp `Lstar=12D/M4` from original 5 wavevectors using 75-digit mpmath; result `7.2115097831082245653848767183562579`, agreeing with the source M15 strict interval. It is a float/high-precision consistency check, NOT our interval proof and not firstness claimed by Geeky-S13.
7. **Out-of-source negative geometry test:** repeat the axis collision thought experiment at *composite* `N=40`. Two distinct cosine triples `(1,0,-1)` from indices `(0,10,20)` and `(0,0,0)` from `(10,10,10)` have exactly the same `a=0` but different `f=-1/3` versus `f=0`; the original A/B variance ratios differ by a relative `0.00229946...`. A single *axial-only* calibration **cannot** equalize both N40 modes. This explicitly falsifies an illegitimate claim that the proof holds for any integer N. `N=40` is NOT source-native M13 and the check is a deliberate counterfactual.
8. All base source `v_A(k)` and `v_B(k)` are positive; measured full-grid minimum spectral variances around `0.9004682685` for A and `0.8823646816` for B (higher than the simple analytical lower bounds).

All statements labeled numeric rely on executed local Python; no false claim of independent other-cell verification. The exact mathematical claim relies on the displayed cyclotomic/interpolation proof.

## 5. Protected interpretations, negative knowledge, transfer decisions

- The result is **not** `NASH K/J3/TPE/GW/GR` identifiability, original M13 global alpha inversion, actual cosmological evidence, a real hardware noise measurement, or a new detector proposal.
- The unrestricted smooth calibration is an extremely broad, generally *nonlocal* mathematical perturbation, not native to M13's short-range stationary covariance family or a measured laboratory transfer function. No absolute amplitude/derivative bounds are inferred.
- If `phi_A=phi_B` is required (shared physical calibration), this particular alias construction is NOT available; source variances A/B are different. If a validated quantitative `||phi''''||<=L` bound is imposed, M15 ROT035/036 positive results can survive. If a causal/local finite-neighbor calibration is imposed, revalidate from that class rather than extrapolating from ROT001.
- `C^infinity` is not itself an information restriction on a FINITE grid when derivatives and amplitudes are unrestricted; high-degree or narrow smooth interpolators can mimic arbitrary finite data. This is a mature interpolation phenomenon, **not general mathematics novelty**.
- The N=41 cyclotomic injectivity is not a claim about arbitrary composite N or the continuum. Counter-control N40 above demonstrates a real geometry distinction.
- The model A/B covariance and all raw local/Fourier observations are source-derived synthetic mathematical hypotheses, not original six physical energy instruments. Source M13 fixed five masks plus mathematical global `k0` are not six native physical detectors.
- No original M13 helper execution this rotation; original Git source and M15 published rational parameters actually read before calculation. Historical full DTC0a runtime unavailable. Neither source scientific priority nor M15's proof priority is reassigned.
- **Different-cell referee I1 pending**, external I3 pending, KN15 BW owner ingestion unverified, no `CANON`, no `EXEC_SIGN`, no claimed owner ACK. GitHub file readback and Slack, if later issued, are transport only.

## 6. Next falsifier / proposed scientific boundary

The scientifically relevant next question is NOT adding a seventh mode under unconstrained C-infinity calibration; ROT001 proves that cannot help even with the complete 41^3 field. Instead require a defensible observation/calibration contract and test at least one of: known small `C4` radius, shared across-hypothesis calibration, locality/finite-range transfer, stable bounded polynomial degree, or a second physical observable whose response cannot be eliminated by the same nuisance.

A different-cell referee should independently verify the **exact** cyclotomic proof (particularly the coefficient relation and the `sum_j d_j=0` step), the count of 1771 orbit classes and 68921 signed ordered modes, the fact that A/B ratios are constant on each orbit, the smooth bump supports, and the covariance-law implication. The referee must also check the negative controls: N40 counterexample, M15 five-mode `Lstar`, and same-calibration boundary. `STOP` if the actual source observer or allowed calibration class is narrower than stated, or if an accidental same-a collision with different ratio is found on N41.

## 7. Mature prior art and provenance

- Standard prime cyclotomic polynomial irreducibility, `Phi_p=1+X+...+X^(p-1)`, see Cambridge number field lecture notes, §8, https://www.dpmms.cam.ac.uk/~jat58/nfl2019/Number_Fields_web.pdf . This external source was located, not treated as proof of novelty.
- Standard finite real interpolation / smooth compact bumps and covariance diagonalization of stationary Gaussian periodic fields. These are mature methods; no claimed original general theorem.
- Actual companion files in this rotation: `geeky_s13_rot001_fullfield_axial_calibration_alias.py` and `IW_GEEKY_S13_ROT001_FULLFIELD_CINFTY_ALIAS_CERT_001_20261122.json`, with independent SHA256/manifest in local archive. Exact source parameters embedded, no private Project data included.

**FINAL:** `SOURCE_SPECIFIC_CYCLOTOMIC_INJECTIVITY_ANALYTIC_PASS / SOURCE_1771_ORBITS_68921_MULTIPLICITY_PASS / EXPLICIT_CINFTY_FULL_41CUBED_GAUSSIAN_ALIAS_MATHEMATICAL_PASS / FULL_FFT_VS_SPATIAL_SITE_OPERATOR_NUMERIC_PASS / FIVE_MODE_LSTAR_UPSTREAM_CONTROL_PASS / N40_COUNTERFACTUAL_FAIL_CLOSED_PASS / ORIGINAL_M13_HELPER_NOT_EXECUTED / DIFFERENT_CELL_I1_PENDING / BW_PENDING / NO_GENERAL_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE`.