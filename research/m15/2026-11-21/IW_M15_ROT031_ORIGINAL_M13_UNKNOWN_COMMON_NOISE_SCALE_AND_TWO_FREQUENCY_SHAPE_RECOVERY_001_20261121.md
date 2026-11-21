---
artifact_id: IW_M15_ROT031_ORIGINAL_M13_COMMON_UNKNOWN_SCALE_SINGLE_MODE_FALSIFIER_AND_TWO_FREQUENCY_RECOVERY_001_20261121
return_id: IW_M15_ROT031_SINGLE_FREQUENCY_CALIBRATION_NO_GO_AND_TWO_SOURCE_EXTREME_FREQUENCY_SCALE_FREE_GAUSSIAN_TEST_001_20261121
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-21
exposure: PUBLIC
class: NEW_SOURCE_CONDITIONAL_ORIGINAL_M13_BYTE_NATIVE_IV80_GLOBAL_2D_SHAPE_OPTIMALITY_AND_SCALE_FREE_CHERNOFF_BINARY_TEST
first_review: INTERNAL_NONBLIND_DIFFERENT_CELL_ORIGINAL_SOURCE; INDEPENDENT_REC_AUD_PENDING
state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_HISTORICAL_DTC0A_RUNTIME / NO_PHYSICAL_RAW_SITE_SENSOR / NO_TASK_CASCADE
---

# M15 ROT031 — A single optimal Fourier noise probe fails under unknown common gain; two extreme modes restore scale-free source discrimination

## 1. What was actually discovered, and firstness

**SOURCE-MATHEMATICAL conditional theorem and a material falsification of a silent calibration extrapolation of M15 ROT030.** With an arbitrary fitted *common* unknown positive raw spatial Gaussian noise multiplier `s`, the model families of ANY one original-M13 spatial Fourier frequency's cosine/sine observations, even with unlimited independent repetitions, are **identical** under two fixed Geeky-S12 ROT035 covariance hypotheses. Thus ROT030's beautiful, globally optimal known-scale one-frequency KL design DOES NOT imply a uniform test with unknown site-noise amplitude. A SECOND spatial frequency resolves this nuisance, providing a scale-invariant test with strictly certified finite-snapshot error guarantees. Both spatial frequencies were proven to have EXACTLY ZERO original deterministic M13 source mean for all alpha.

Priority protected: M13 FIRST original public N41 sparse B auxiliary Fourier tensor and five fixed cubic masks; Geeky-S12 ROT034 FIRST legal five-parameter exact covariance family; Geeky ROT035 FIRST two extreme near-indistinguishable legal exact rational Gaussian covariance laws A/B under six coarse masks; Geeky ROT036 FIRST an *alternative*, coordinate-swap symmetry-odd two-site independent seventh source statistic and its 40M-snapshot finite-sample bound; M15 ROT029 FIRST different-cell original source exact rational KL I1 and perfect-calibration uniform KL; M15 ROT030 FIRST source-specific global known-scale single Fourier cosine optimum and two-quadrature known-scale Bhattacharyya sample guarantee. This ROT031 does not override any firstness, does not claim new general statistical mathematical theory, and is about a DIFFERENT nuisance and observation protocol from owner ROT036's two-site probe.

ORIGINAL actual M13 unchanged 8,970-byte public source and its mathematical source `tensor_polys(41)[1]`, `calc(41,alpha=1/20)[1]`, `inner(B,B,41,0,{})` were **ACTUALLY EXECUTED** after strict byte checks: Git blob SHA1 `c6377cfbc9a0070abc34ffedc5871e719f6a4679`, full source SHA256 `cd4aad089bf68e2e6155ff048d4d812943495dcf1770c8acbf0ff8111b1deb9c`. The complete old historical `dtc0a_runtime_v0_3_1.py` was not obtained or byte-replayed. All original executable source bytes and both newly executed programs live in the user-local verified ZIP.

Original M13: https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py

Geeky ROT035 original mathematical models: https://github.com/wmakiela-tech/Nash-iw-research/blob/cb1017143615b420eadef93e7a42eb332ba1df03/research/geeky-s12/2026-11-17/IW_GEEKY_S12_ROT035_EXACT_RATIONAL_M13_SIX_MASK_COVARIANCE_KL_INDISTINGUISHABILITY_AND_SITE_AGGREGATION_INFORMATION_LOSS_001_20261117.md

Geeky ROT036 distinct two-site source probe: https://github.com/wmakiela-tech/Nash-iw-research/blob/efe4c9962811518cf068401946e09a4205d1ed91/research/geeky-s12/2026-11-19/IW_GEEKY_S12_ROT036_ORIGINAL_M13_SYMMETRY_ODD_TWO_SITE_PROBE_EXACT_INDEPENDENCE_AND_NONASYMPTOTIC_TESTING_ESCAPE_001_20261119.md

M15 ROT030 known-variance Fourier: https://github.com/wmakiela-tech/Nash-iw-research/blob/6f1681b99fc194c41354e5a65158fb6fed0addad/research/m15/2026-11-19/IW_M15_ROT030_ORIGINAL_M13_OPTIMAL_RAW_SITE_FOURIER_GAUSSIAN_LINEAR_CONTRAST_SOURCE_IV70_001_20261119.md

Full prior independent M15 ROT030 source IV70 machine certificate SHA256 `48738b3c1b5cf23163cd9144f96fbd2ae7723c4b5a64d8e5ad2dd57f50b9456f` and M15 ROT029 independent original-source exact rational KL JSON SHA256 `00b8c93da96c9c92901555fd4c2db0af63978ecf735df3945e9ff42d218dee90` are SOURCE-LOCKED as prior inputs. Main ROT031 re-executes native original M13 and independently recalculates all four spectral corner variances with *80-digit outward interval arithmetic*; no Geeky private executable or result array imported.

## 2. Exact original-source observer model

Original N=41 periodic 3D lattice M=41^3=68,921 spatial sites. Let `E_source(x;alpha)` be the deterministic B tensor-energy density as mathematically defined by original unchanged M13. Its 41 Fourier tensor B modes are supported in integer coordinate ranges x[-3,3], y[-2,2], z[-1,1]; original B-energy difference q support contains 221 lattice wavevectors. Neither `k_lo=(20,20,20)` nor `k_hi=(20,20,0)` (nor their negatives modulo 41) occurs in this finite source energy support. Consequently **BOTH full-site normalized cos and sin projections of E_source have EXACT mean zero FOR ALL alpha**; all permitted global source gain changes and common torus translations preserve their Fourier-support zeros. This is an exact source integer-support proof, NOT an interpretation of near-zero FFT numerics.

Consider entirely hypothetical additive centered RAW SITE Gaussian energy noise with conditional spatial covariance under two fixed prior legal models X=A,B:

```
Sigma_X(s) = s * beta0_X * [ I + theta_axis_X A_axis
                                + theta_face_X A_face
                                + theta_body_X A_body ],  s>0.
```

Here **ONE AND THE SAME unknown positive multiplicative site-noise variance scale `s` multiplies every spatial frequency** within a given true law. It is not separately estimated for each frequency. The independent new nuisance `s` was not part of fixed-scale M15 ROT030. A sample consists of all raw spatial site data (or the four **new** correctly measured weighted Fourier projections), which the original six coarse shell means do NOT supply. Real M13 has no authenticated physical 68,921-site energy detector or high-k Fourier instrumentation.

Legally frozen owner model A: beta0=1, theta_axis=3/25, theta_face=1/10, theta_body=2/25. Model B: beta0=99779719687217/10^14, theta_axis=316869474178226/2494492992180425, theta_face=93110637627687/997797196872170, theta_body=205860943554709/2494492992180425. Both are mathematically SPD by bounds on periodic spectral averaging operators; no actual noise measurement was supplied.

The source Fourier eigenvariance formula for a frequency k is

```
v_X(k) = beta0_X * [1 + theta_axis_X*(c1+c2+c3)/3
                       + theta_face_X*(c1*c2+c1*c3+c2*c3)/3
                       + theta_body_X*c1*c2*c3],
cj=cos(2*pi*kj/41).
```

Under each Gaussian hypothesis and for each k distinct from -k, the real normalized sine/cosine projections are independent centered N(0,s*v_X(k)). Distinct Fourier frequency planes are independent as well, since spatial covariance is stationary and circulant.

## 3. NEW negative result: one Fourier frequency admits no test under arbitrary unknown noise amplitude

If we observe ONLY the sine/cosine pair for ONE fixed Fourier mode k over n IID snapshots, its conditional law under H_A is N(0,s*v_A(k)*I_(2n)) and under H_B is N(0,s*v_B(k)*I_(2n)). Because the nuisance s ranges freely over all positive reals, the *sets of allowed probability laws coincide exactly*: for each H_A(s) one obtains the **same** H_B(s') by taking s'=s*v_A(k)/v_B(k). Therefore there is no binary test whose success is uniformly above 1/2 for equal priors over the two independently fitted nuisance values; even n→∞ does not resolve the model identity from only this frequency. This is NOT a statement that KL at fixed *known* s vanishes: ROT030's fixed-scale KL remains rigorously positive and correct.

This extends to any NUMBER of sin/cos replicates at the same spatial k because they all have the same scalar covariance. A common unknown additive spatial baseline (k=0) is independently annihilated by both nonzero spatial Fourier contrasts.

## 4. NEW positive result: global two-dimensional shape contrast and strict IV80 extremes

Choose TWO source-mean-free frequencies `k_lo=(20,20,20)` and `k_hi=(20,20,0)`. The source IV80 verifier calculates the relative eigenvariance ratios `r(k)=v_B(k)/v_A(k)`. Their strict original-source enclosures are:

- `r_min` at k_lo in `[0.97989536383370119549,0.97989536383370119550]` (displayed conservatively rounded; see full JSON for exact directed bounds);
- `r_max` at k_hi in `[1.00018700445686864031,1.00018700445686864032]`;
- `q=r_min/r_max` in `[0.97971215329458673522,0.97971215329458673524]`;
- new *shape condition number* `r_max/r_min` in `[1.02070796676063379653,1.02070796676063379655]`.

The original Fourier ratio is fractional-linear in each cosine coordinate c_j separately on cube `[-cos(pi/41),1]^3`. Thus all spectral ratio minima/maxima occur on its eight corners (four permutation classes), independently recomputed and interval-separated with M15's NEW mpmath.iv.dps80. `r_min` and `r_max` are attained at the two chosen original lattice frequencies. No float rounding decides these signs.

**Global 2D SHAPE theorem:** for any full-rank matrix U: R²→R^68921 selecting ANY TWO real linear raw-site summary coordinates, its generalized covariance-pencil eigenvalues (U^T Sigma_B U, U^T Sigma_A U) are Rayleigh quotients of the full site covariances and both lie in `[r_min,r_max]`. Thus their ratio is always <=`r_max/r_min`, achieved by the plane spanned by the two source Fourier cosine vectors above. That proves this subspace has MAXIMUM spectral variance-ratio anisotropy among ALL 2D real raw-site linear compression planes. It DOES NOT prove this plane is the globally best Bayes/minimax test across all possible 2D summaries, or that a physical sensor can record either mode. Those are separate questions.

The two frequencies have q strictly different from unity, so one shared s>0 CANNOT make the joint two-mode Gaussian covariance shapes match. They are now distinguishable, conditional on the original mathematical Gaussian model and IID snapshots.

## 5. Constructive SCALE-FREE test and nonasymptotic error proof

Within each of n independent full spatial snapshots, take FOUR real normalized noise-only readings:

```
Z_lo_cos, Z_lo_sin  at k_lo
Z_hi_cos, Z_hi_sin  at k_hi.
```

Let S_lo and S_hi be sums over n snapshots of their TWO per-mode squared quadratures. Define normalized ratio

```
T=(S_lo/v_A(k_lo))/(S_hi/v_A(k_hi)).
```

Under H_A, `T~F_(2n,2n)`; under H_B, `T~q*F_(2n,2n)`; the **unknown s cancels exactly**. Decide B if `T<sqrt(q)` and A otherwise. Since q<sqrt(q)<1, by exchangeability of two identical chi-square degrees of freedom the A and B misclassification probabilities coincide. For F=U/V with U,V independent chi-square_{2n}, Chernoff's standard Laplace bound yields

```
P(F<=a) <= [4a/(1+a)^2]^n   for 0<a<1.
```

The bound follows exactly by applying Markov to `exp[-t(U-aV)]` and minimizing at `t=(1-a)/(4a)`; no data, simulation, central-limit, or parameter approximation is used. Therefore **BOTH conditional errors**, UNIFORMLY FOR EVERY s>0, obey

```
P_A(wrong), P_B(wrong) <= H^n,
H=4*sqrt(q)/(1+sqrt(q))^2.
```

Full rigorous original-source IV80 gives `H` in `[0.99997374387537118137680,0.99997374387537118137682]`, strictly <1. Actual outward IV80 power checks certify these sufficient finite full-spatial snapshot gates, simultaneously for BOTH hypotheses and ANY common scale:

| Strict guaranteed success for each hypothesis | n snapshots | Rigorous error upper (rounded upward) |
|---|---:|---:|
| >75% | 60,000 | <0.2070 |
| >90% | 90,000 | <0.0942 |
| >95% | 120,000 | <0.0429 |
| >99% | 200,000 | <0.00525 |

These are **SUFFICIENT** (conservative) theoretical sample sizes for the TWO exact known source-law shapes and FOUR new Fourier sensor coordinates, not experimental feasibility. The fixed-amplitude 14k source ROT030 guarantee and the new unknown-amplitude 60k guarantee use DIFFERENT knowledge assumptions and may not be conflated. Allowing separate unknown s_lo and s_hi destroys even this two-frequency discrimination: BOTH 4-coordinate Gaussian law families are then identical because each mode's variance can be fitted independently. That is a second exact negative guard, not a physical claim.

## 6. Actual independent original-M13 41³ spatial source and statistical diagnostics

A SECOND genuinely separately authored Python script imports and runs original unchanged M13 source, synthesizes original nine Fourier B tensor fields by full 41×41×41 inverse FFT, constructs the original B energy at every site, verifies native original global mean k0 and evaluates ALL FOUR source high-k cosine/sine projections directly. The four energy projections are float64 near zero (`~6.46e-27`, `1.70e-26`, `1.30e-26`, `1.78e-26` in original mathematical source units), **numeric diagnostics only**: exact means are zero by M13 integer Fourier support.

Independently defines all 6+12+8 actual signed periodic 41³ site neighbor shifts and **directly applies those shifts** to all four cos/sin spatial weight functions, recomputing two separate 4×4 raw covariance matrices *without importing main IV80 spectral calculation*. Their off-diagonal elements are all <=~5e-16 in noise units, numerically confirming Gaussian independence of four modes. Diagonal variances A: `(0.9004682684983889,0.900468268498388,1.0064329065072715,1.0064329065072708)` and B: `(0.8823646815809316,0.8823646815809308,1.0066211139463277,1.0066211139463268)`. Corresponding direct q≈0.9797121532945865 overlaps IV80 within declared FLOAT tolerance (not IV inclusion).

Separate complete 68,921-mode NumPy spectral scan finds min at (20,20,20) and max at a PERMUTATION of (20,20,0), exactly as IV80 geometry predicts; an initial too-specific diagnostic incorrectly assumed the max index order had to be (20,20,0) and **FAILED** because NumPy's argmax returned (0,20,20). This was corrected to permutation-invariant checking BEFORE the final science/replay, and failed intermediate run was NOT counted PASS. The separate `scipy.stats.f` F_(2n,2n) CDF confirms exact-scale-free test conditional errors (FLOAT numerical, not rigorous source proof): n60k ~0.03794573, 90k ~0.01485364, 120k ~0.00603166, 200k ~0.00059604; each is below the strict IV80 Chernoff bound.

## 7. Actual reproducibility and falsification controls

Full self-contained USER-LOCAL ZIP contains the ORIGINAL byte-identical native M13 8970B Python; both distinct new **actually executed** IV80 and full-site numeric scientific Python programs; their complete actual output JSONs; prior independently source-verified M15 ROT029 rational and M15 ROT030 IV70 input JSONs, both source SHA-locked; actual cold-replay and EIGHT attack script and full receipt; full local scientific report and README, plus complete manifest and ZIP builder. The exact ZIP filename, byte size and SHA256 are supplied in the public handoff; the packaged README supplies reproduction commands. **No claim that public GitHub report or curated JSON equals a public Python byte mirror.**

ACTUALLY executed complete original scientific scripts in a fresh isolated Python `-I` directory, each full machine JSON result BYTE IDENTICAL to first original execution (2/2 PASS). EIGHT separate disposable adversarial controls ACTUALLY REJECTED: ORIGINAL M13 one-byte alteration against main and independent spatial scripts (2), one-byte previous source ROT030 IV70 JSON alteration (1), previous ROT029 exact rational JSON alteration (1), current strict IV80 result tampered before independent FFT (1), falsely labeling source MIN frequency `(0,0,0)` as mean-free (1), falsely identifying the MAX frequency as same as MIN (1), and falsely claiming 99% success from n=100 snapshots (1). Five source/parent SHA guards plus THREE substantive mathematical model/claim falsifiers. The initial independent numerical FFT argmax ordering assertion failure was repaired and was NOT counted in the eight successful negative tests.

## 8. Strict epistemic ceilings

Original M13 public auxiliary tensor operator ONLY; full historical dtc0a runtime bytes unavailable. Original calc has no source-native actual physical 68,921-site RAW energy recorder, high-frequency spatial projections, 6th native sensor, free common source torus translations or arbitrary log gain. Original covariance laws, their common unknown scale and n independent complete snapshots are mathematical synthetic hypotheses, with no actual experimental source noise or real time budget. Gaussian assumptions and IID are essential. This theorem does not establish a new NASH physical effect, original J3/K/TPE, physical sensor design, global alpha inversion, literature novelty or actual 60k+ measurements. The original two-model source firstness of Geeky ROT034/035 and the separate two-site symmetry-odd source firstness of Geeky ROT036 remain intact. Internal different-cell NONBLIND I1 source work only, not external blind I3, REC13/AUD3 acceptance or KN15 native BW ingest receipt; GitHub/Slack publication != owner ACK. `NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE`.

FINAL: M15_ROT031_ORIGINAL_NATIVE_M13_GIT_AND_SHA_EXECUTED_PASS / SINGLE_FREQUENCY_ANY_N_UNKNOWN_SCALE_COMPOSITE_NO_GO_PASS / SECOND_SOURCE_MEAN_FREE_FREQUENCY_ADDED_PASS / SOURCE_IV80_FOUR_CORNER_SPECTRAL_EXTREMA_STRICT_PASS / ALL_2D_REAL_LINEAR_SPATIAL_SHAPE_ANISOTROPY_MAX_BOUND_PASS / SCALE_FREE_GAUSSIAN_TWO_FREQUENCY_F_2N2N_CHERNOFF_75_90_95_99_PASS / SEPARATE_REAL_ORIGINAL_41CUBED_SOURCE_FFT_SITE_ROLL_AND_ALL_68921_SPECTRAL_NUMERIC_PASS / TWO_COMPLETE_ISOLATED_JSON_BYTE_IDENTICAL_PASS / EIGHT_NEGATIVE_MUTATIONS_REJECTED_PASS / USER_ZIP_SHA_CRC_PASS / ORIGINAL_FIRSTNESS_RETAINED / BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE.