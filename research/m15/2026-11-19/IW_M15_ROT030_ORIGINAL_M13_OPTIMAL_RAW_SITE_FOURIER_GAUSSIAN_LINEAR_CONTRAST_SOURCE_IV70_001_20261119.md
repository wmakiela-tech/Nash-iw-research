---
artifact_id: IW_M15_ROT030_ORIGINAL_M13_GLOBAL_OPTIMAL_SINGLE_LINEAR_SPATIAL_FOURIER_GAUSSIAN_CONTRAST_001_20261119
return_id: IW_M15_ROT030_SOURCE_OPTIMAL_SINGLE_SPATIAL_FOURIER_NOISE_CONTRAST_AND_TWO_QUADRATURE_FINITE_SAMPLE_GATE_001_20261119
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-19
exposure: PUBLIC
result_class: NEW_ORIGINAL_M13_NATIVE_EXECUTION_IV70_GLOBAL_68921_RAW_LINEAR_SPATIAL_GAUSSIAN_KL_OPTIMUM
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_REAL_RAW_SITE_DATA / NO_REAL_SPECTRAL_SENSOR / NO_HISTORIC_DTC0A / NO_TASK_CASCADE
---

# M15 ROT030 — source-original optimal Fourier statistic recovers information erased by six masks

## Science priority and actual source

NEW source-specific result: a single high-frequency cosine projection of RAW SITE ENERGY on the original N=41 lattice is KL-optimal among ALL nonzero real one-dimensional LINEAR spatial summaries for the exact TWO Gaussian RAW-site covariance models first constructed by Geeky-S12 ROT035. A matching sine projection is an independent equal-information statistic. This is mathematical experimental design for hypothetical observations, not a claim a source-native high-frequency sensor exists.

Firstness: M13 original native N41 Fourier B auxiliary source FIRST, Geeky-S12 ROT034 first five-parameter covariance rank5/16 linear constraints, Geeky ROT035 FIRST exact two legal rational Gaussian covariance models with six-region mean KL<1e-17, and earlier M15 ROT029 FIRST independent source I1 review and the calibration-zero KL<1.17e-17 uniform extension. All such priority is preserved. The Gaussian Fourier/KL/Bhattacharyya mathematics is mature, not novel general mathematics.

Actual unchanged original M13 8970-byte public Python code: Git blob SHA1 c6377cfbc9a0070abc34ffedc5871e719f6a4679, full SHA256 cd4aad089bf68e2e6155ff048d4d812943495dcf1770c8acbf0ff8111b1deb9c. Both identities checked before native import. ACTUALLY EXECUTED native tensor_polys(41)[B], calc(41,alpha=1/20)[B], inner(B,B,N41,k0) in TWO new science programs. Source:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py

Geeky owner ROT035 FIRST:
https://github.com/wmakiela-tech/Nash-iw-research/blob/cb1017143615b420eadef93e7a42eb332ba1df03/research/geeky-s12/2026-11-17/IW_GEEKY_S12_ROT035_EXACT_RATIONAL_M13_SIX_MASK_COVARIANCE_KL_INDISTINGUISHABILITY_AND_SITE_AGGREGATION_INFORMATION_LOSS_001_20261117.md

M15 ROT029 exact rational original-source full certificate (SHA-locked as prior, not falsely claimed recomputed in ROT030):
https://github.com/wmakiela-tech/Nash-iw-research/blob/8d060d5f20cef196e00b71618b15a859247facaa/research/m15/2026-11-17/IW_M15_ROT029_DIFFERENT_CELL_ORIGINAL_M13_EXACT_RATIONAL_ROT035_SOURCE_KL_AND_PERFECT_CALIBRATION_UNIFORM_NO_GO_001_20261117.md
Prior actual JSON SHA256 00b8c93da96c9c92901555fd4c2db0af63978ecf735df3945e9ff42d218dee90.

## Legal original-source mathematical Gaussian noise models

Original M13 fixed 41³=68,921 site grid, five disjoint original source masks and complement. Two Geeky-FIRST exactly rational legal site Gaussian covariance laws share the SAME original M13 deterministic source mean:

Sigma_X=beta0_X [I+theta_ax_X Aaxis+theta_face_X Aface+theta_body_X Abody].
Aaxis is mean of six periodic one-step signed axial shifts, Aface mean of twelve signed face-diagonal shifts, Abody mean of eight signed body-diagonal shifts. Site noise is hypothetical Gaussian ADDITIVE RAW energy density, not measured data, nor Gaussian logarithmic measurements.

A: beta0=1, theta_ax=3/25, theta_face=1/10, theta_body=2/25.
B: beta0=99779719687217/100000000000000, theta_ax=316869474178226/2494492992180425, theta_face=93110637627687/997797196872170, theta_body=205860943554709/2494492992180425.

Both theta sums strictly <2/5, so both full site covariances strictly positive definite via the site Fourier norm bound. Prior M15 original-native exact rational source cert proves the SIX existing masks means have KL under PERFECT independent sixth calibration strictly <1.16611846243e-17, and remain indistinguishable under arbitrary common nonnegative independent extra sixth-channel calibration variance by KL data processing.

## Exact native M13 frequency ZERO in the new noise-only statistic

Original native tensor_polys(41) ACTUALLY executed and gives 41 original B Fourier tensor modes; exact integer support coordinate ranges x[-3,3], y[-2,2], z[-1,1]. Original B energy Fourier q=m−n support has 221 distinct q. New mode k=(20,20,20) and its modulo41 negative are NOT in the energy support for ANY source alpha. Thus noise-free original M13 energy projected onto k has EXACTLY ZERO Fourier amplitude for any alpha and any common torus translation/gain (phase/support unchanged), not just numerically approximately zero.

Define the additional observables, for original RAW lattice energy E(x):
  Zcos=sqrt(2/68921)*sum_x E(x)*cos[2pi*20*(x+y+z)/41];
  Zsin=sqrt(2/68921)*sum_x E(x)*sin[2pi*20*(x+y+z)/41].
Both mean ZERO and are orthogonal normalized lattice-weight vectors. Under either fixed legal stationary Gaussian site covariance model, they are independent centered Gaussians each with eigenvariance v_X(k). They are NEW site-resolved/raw-weighted observations. It is IMPOSSIBLE to compute them solely from the previous six coarse masks without extra information.

## Rigorous source mathematical GLOBAL one-linear-projection optimality

Let c_j=cos(2pi*k_j/41). Spectral eigenvariance for model X:
  v_X(c1,c2,c3) = beta0_X * [1+theta_ax_X*(c1+c2+c3)/3
      +theta_face_X*(c1*c2+c1*c3+c2*c3)/3
      +theta_body_X*c1*c2*c3].

Each c_j lies in [cstar,1], cstar=-cos(pi/41), attained exactly by k_j=±20. The ratio r=v_B/v_A is positive, and is fractional-linear in EACH c_j separately when other cosines fixed. Hence global ratio extrema over the cube occur at its eight vertices (four distinct permutation classes by number j=0,1,2,3 of cstar coordinates). ACTUAL 70-digit outward mpmath.iv arithmetic evaluates all four source classes: r minimum at j=3, r maximum at j=2. For Gaussian same-mean scalar variance ratio r, KL_A||B=(1/r−1+ln r)/2; the KL maximum on any range of r must occur at an endpoint, and strict IV70 demonstrates the j=3 endpoint KL is larger than all other corners. Therefore mode frequencies k=(±20,±20,±20) maximize scalar KL over ALL 68,921 discrete source Fourier modes.

The theorem extends to ANY nonzero real full-site linear summary u: both site covariance matrices commute and diagonalize in the exact torus Fourier basis, so the variance ratio R(u)=(u^T Sigma_B u)/(u^T Sigma_A u) is a convex combination of the per-Fourier r_k with weights v_A,k |u_hat_k|²>=0. Since scalar Gaussian KL achieves its maximum at the same endpoint, NO real one-dimensional linear projection of all 68,921 raw site data outperforms this chosen cosine mode for THESE exact source-legal A/B Gaussian laws.

Exact original source IV70 Gaussian KL per ONE normalized cosine spatial statistic:
  [0.0001038204467881385829919792523818824030081018827,
   0.0001038204467881385829919792523818824030081031664].
Other three corner KL values are ~3.754e-19, ~6.207e-13, ~8.740e-9. Two independent cosine/sine projections have KL EXACTLY DOUBLE:
  [0.0002076408935762771659839585047637648060162037654,
   0.0002076408935762771659839585047637648060162063327].
Their combined KL is STRICTLY more than 1.7806157801852e13 times the RIGOROUS UPPER bound from the six coarse masks at zero extra sixth calibration. Numerator rigorous POSITIVE lower, denominator prior original-source SHA-verified rigorous UPPER. Comparing different sensing protocols does NOT imply original six-mask data contain this missing information.

## FINITE-sample achievable two-hypothesis test: not six-mask evidence

The cos and sin quadratures from ONE full site spatial snapshot constitute two independent Gaussian observations N(0,v_X). For two fixed fully specified source covariance hypotheses A/B, their bivariate Hellinger affinity is
  H=2 sqrt(v_A v_B)/(v_A+v_B)
  ~=0.9999484428195441607, strictly <1 by IV70.

For n independent FULL SPATIAL snapshots, equal priors and the optimal likelihood-ratio Gaussian binary classifier, the mature Bhattacharyya inequality gives Bayes error Pe<=H^n/2. The executable IV70 checker strictly verifies:
  14,000 independent complete raw spatial snapshots SUFFICE for >75% optimal success;
  32,000 snapshots SUFFICE for >90%;
  46,000 snapshots SUFFICE for >95%;
  76,000 snapshots SUFFICE for >99%.
These are demonstrably SUFFICIENT two-KNOWN-hypothesis mathematical bounds, not measured or practical sample sizes, not guaranteed estimation of unknown nuisance parameters, not global alpha identification. M15 ROT029 source previous six-mask-only *NECESSARY* >4.287729e16 hypothetically independent aggregate snapshots for 75% represents a DIFFERENT observation type, not directly exchangeable measurements.

## Separate ORIGINAL M13 actual spatial Fourier independent checker

A separately authored Python code reexecutes the original native M13, synthesizes nine complex Fourier B tensor fields into the COMPLETE 41³ grid via independent inverse FFT, and directly computes its B energy and both high-k projections. The forbidden original energy Fourier amplitude at k=(20,20,20) is ~5.5503e-32 per site, FLOAT diagnostic of the strict integer-support theorem; native original global energy vs spatial average relative error <2e-13.

Independent periodic actual ORIGINAL SITE array rolls for all 6+12+8 signed neighbor directions compute the cos/sin variances and covariance directly, without importing IV70 corner formulas: scalar KL ~0.0001038204467881873, sin/cos cross covariance numerically ~0. A separate full 68,921-frequency NumPy scan finds exactly EIGHT global maximizing signed frequencies and ten independent random spatial real weight trials give strictly smaller KL. FFT and scan are subordinate float diagnostics, not claimed as interval theorems.

Both NEW original science Python programs were REALLY rerun isolated with Python -I in fresh empty temporary directories: TWO FULL RESULT JSON byte identical. SIX ACTUAL negative fixtures REJECTED:
(1)(2) one-byte original M13 helper corruption rejected before import by each program;
(3) previous exact rational KL JSON corruption rejected by main source identity guard;
(4) IV70 main output tampering rejected by spatial source checker identity guard;
(5) wrong forbidden original energy Fourier frequency k=(0,0,0) rejected by original integer support;
(6) falsely asserting one real spectral KL>0.0002 rejected by strict source IV70 test.
The final 10 source/metadata payloads and SHA manifest are in complete user-local runnable archive:
  IW_M15_ROT030_ORIGINAL_M13_OPTIMAL_FOURIER_LINEAR_CONTRAST_IV70_REPRO_001_20261119.zip
  30,590 bytes, SHA256 2639bf8964d154024cae054a6ca0384692872949e4516503c58da4ed658797a0.
ZIP CRC PASS, 10/10 payload SHA256 PASS, 11/11 entry byte reread PASS.
Main source IV70 executable SHA256 d4d3f7284e6ec5479c4c4580d119b9fc88a7a95217bbffd5850d0eb387e8cd47; full rigorous IV70 JSON SHA256 48738b3c1b5cf23163cd9144f96fbd2ae7723c4b5a64d8e5ad2dd57f50b9456f.
Separate actual original 41³ spatial program SHA256 44ef2c17cd428752549042dc29938a7a0d4f854c996f06afdee7f9a6e7a7d98c; complete spatial JSON SHA256 420f627267d1d725b6f7e91ed0628217f538a596c4c54e1032d68b7d976b1998.
Actual replay/6 negatives JSON SHA256 258a39cc97fff51491a7dfb44fa4710f16fc2094af4275fa4c089afddff20297.
Executable source bytes reside in USER ZIP; this GitHub report/curated summary do not falsely claim code mirror.

## HARD SCIENCE STOP

Original public M13 source AUXILIARY only, not historical complete dtc0a_runtime_v0_3_1.py. HYPOTHETICAL site-wide Gaussian energy noise laws, no native physical 68,921-site measurement, no attested detector for k=(20,20,20), no actual repeated spatial snapshots, calibration, resource estimates or sensor noise. No native source free translation/gain and sixth independent physical energy sensor; no NASH physical K/J3/TPE/GR/GW mechanism, global alpha inverse, or general math novelty. Source M13 and owner Geeky ROT034/035 firstness retained. M15 internal source I1 NONBLIND only; REC13/AUD3 independent review NOT verified, KN15 BW actual native ingest NOT verified. GITHUB_WRITE and SLACK_POST do not imply ACK. NO_NOVELTY/NO_CANON/NO_EXEC_SIGN/NO_PHYSICAL_UPGRADE/NO_TASK_CASCADE.

FINAL:
M15_ROT030_ORIGINAL_NATIVE_M13_ACTUAL_EXECUTION /
ORIGINAL_41_MODE_B_ENERGY_K202020_SUPPORT_ZERO /
SOURCE_IV70_FOUR_CORNER_EXACT_GLOBAL_SPECTRAL_OPTIMUM /
ALL_REAL_ONE_DIMENSIONAL_LINEAR_SITE_SUMMARIES_OPTIMALITY /
ONE_REAL_KL_GT_1E_MINUS4 /
TWO_GAUSSIAN_QUADRATURE_KL_OVER_1P78E13_TIMES_RIGOROUS_SIX_AGGREGATE_KL_UPPER /
FOUR_STRICT_BHATTACHARYYA_SUFFICIENT_SAMPLE_GATES /
INDEPENDENT_41CUBED_SPATIAL_NATIVE_M13_FFT_AND_ALL_68921_FREQUENCY_NUMERIC /
TWO_FULL_CLEAN_REPLAYS_BYTE_IDENTICAL /
SIX_ACTUAL_FALSIFIERS_REJECTED /
ZIP_CRC_SHA10_OF10_PASS /
NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE.
