---
artifact_id: IW_M16_ROT001_GEEKY_S13_NP_MONOTONICITY_AND_NUMERICAL_DIAGNOSTIC_SOURCE_I1_001_20261122
return_id: IW_M16_ROT001_GEEKY_S13_ROT009_STRICT_BAYES_RISK_MONOTONICITY_AND_INDEPENDENT_NONIV_NUMERICAL_DIAGNOSTIC_001_20261122
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_11 / M16
created_at: 2026-11-22
exposure: PUBLIC
document_type: REPORT
result_class: BOUNDED_SOURCE_MATHEMATICAL_I1_PLUS_DIFFERENT_CELL_NUMERICAL_DIAGNOSTIC
status: INTERNAL_NONBLIND_CONDITIONAL_REVIEW / NO_EXTERNAL_I3
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_GENERAL_MATHEMATICAL_NOVELTY / NO_IV_NUMERIC_THRESHOLD / NO_PHYSICAL_SENSOR / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE
---

# M16 ROT001 — strict NP risk monotonicity, conditional first-n implication, independent numerical diagnostic

## 1. Primary source and exact scope

**Original firstness belongs to Geeky-S13 ROT009:**
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s13/2026-11-22/IW_GEEKY_S13_ROT009_FOUR_MODE_EXACT_NP_MAXIMAL_INVARIANT_SYMMETRIC_TILT_NUMERIC_BOUNDS_001_20261122.md
Source Git blob: 14fbe78c6371bbed80bf5b4febc0de69f4120e4c.

Dependent Geeky-S13 ROT008, blob ba5eb5a8389a5eba71ce7558bd19d5850bc378c2:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s13/2026-11-22/IW_GEEKY_S13_ROT008_FOUR_MODE_FULL_LOG_CROSS_RATIO_SUM_IV55_CERTIFIED_SAMPLE_UPLIFT_001_20261122.md

M13 FIRST original public auxiliary Fourier N41 source, blob c6377cfbc9a0070abc34ffedc5871e719f6a4679; Geeky-S12 ROT038 FIRST ANISOTROPIC synthetic Gaussian A/B. Firstness unchanged. M16 did NOT execute original M13 module or historical complete DTC0a runtime in this rotation.

This review covers ONLY Geeky-S13 ROT009's four hypothetical RAW Fourier modes and exact direction-by-radius, arbitrary positive snapshot-specific calibration gains. After quotienting gains, IID invariant observations have p(z)=f(z) under A and q(z)=f(z+Delta) under B. The density f is the strictly positive, even, strictly logconcave convolution of two standard logistic densities. Delta = 0.06883323430559849760294690989001727861304... >0 from the original rational anisotropic Gaussian pair. The equal-prior Neyman–Pearson decision uses L_n = sum_i log(q(Z_i)/p(Z_i)), choosing B iff L_n>0. The equal type-I/II errors follow from exact source symmetry. This is NOT M15 ROT041's distinct isotropic six-mode C5 experiment.

## 2. Strict source theorem from mature Bayesian experiment theory

Let e_n be the optimal equal-prior error for n IID observations under the above two strictly positive densities. Then for EVERY integer n>=0:

  e_(n+1) < e_n.

The original source likelihood ratio ell(y)=log(q(y)/p(y)) is continuous and strictly decreasing with limits +Delta at y -> -infinity and -Delta at y -> +infinity, hence the ratio q(y)/p(y) ranges across (exp(-Delta), exp(Delta)); also p(-Delta/2)=q(-Delta/2).

**Direct proof.** Write p_n(x)=product_i p(x_i) and q_n(x)=product_i q(x_i), so e_n=(1/2)integral min(p_n(x),q_n(x))dx. For each x let a=p_n(x), b=q_n(x), both positive. Because p and q each integrate to 1,

  integral min(a p(y), b q(y))dy <= min(a,b).

Whenever a/b is strictly between exp(-Delta) and exp(+Delta), the sign of a p(y)-b q(y) changes on positive-measure sets; then the inequality is STRICT because the pointwise minimum is not a.e. equal to either full integrand. For every n>=1, choosing x_i in a small open neighborhood of -Delta/2 yields a/b near 1 within that interval, with positive p_n and q_n measure. For n=0, a=b=1 has the same strict property. Integration over x proves e_(n+1)<e_n. QED.

This lemma is a straightforward standard Bayesian hypothesis-testing monotonicity argument, not a novel general mathematical theorem. Within ROT009's invariant NP family, its conclusion means that rigorous two-sided threshold tests at two adjacent sample counts would establish the FIRST count globally over all n, without a sweep over earlier n.

**Conditional first-n inference, NOT a current certificate:**
- if an independent outward interval enclosure proves e_14538 > 0.05 and e_14539 < 0.05, then n=14539 is the FIRST count achieving >95% classification accuracy in the source invariant NP family;
- if an independent outward interval enclosure proves e_29082 > 0.01 and e_29083 < 0.01, then n=29083 is FIRST for >99% in the same scope.

The four numeric signs in Geeky-S13 ROT009 are NOT interval certified. Therefore the monotonicity proof does NOT upgrade those numbers to IV_PASS. It is not automatically transferred to Geeky-S13 ROT008's non-optimal sum test.

## 3. Independent actual computation; numerical only

A newly written standalone source diagnostic is stored at:
research/m16/2026-11-22/code/m16_rot001_np_risk_diagnostic.py

Source program public Git commit: c9f41964144f1a0b8ac933e13855813c220f3de4.

It does NOT import Geeky-S13 code. It uses source rational A/B axial variance formulas, 65-digit mpmath cosines for Delta, a numerically stabilized closed density f, and Gauss–Legendre quadrature of the exact symmetric-tilt representation:

  rho=integral sqrt(p(z) q(z)) dz;
  h(z)=sqrt(p(z)q(z))/rho;
  psi(t)=integral h(z) cos(t ell(z)) dz;
  e_n=rho^n/(2*pi) integral_0^infinity psi(t)^n/(t^2+1/4) dt.

Actually executed locally under Python 3; NumPy 2.3.5, mpmath 1.3.0, SciPy 1.17.0 available (the code itself imports NumPy/mpmath). Inner z integration [-45,45] with 500 versus 800 Gauss–Legendre nodes; outer t [0,8] uses 600 nodes. Two grid outputs:

| n | inner 500 | inner 800 | approximate sign |
|---:|---:|---:|---|
| 14538 | 0.050005160622 | 0.050005160641 | above 0.05 |
| 14539 | 0.049999326252 | 0.049999326270 | below 0.05 |
| 29082 | 0.010000194102 | 0.010000194110 | above 0.01 |
| 29083 | 0.009999128160 | 0.009999128168 | below 0.01 |

These source numbers agree with Geeky-S13 ROT009's independently reported estimates at ordinary numerical precision. Mesh-to-mesh differences are ~1.8e-11 or ~7.3e-12, respectively, but such agreement is NOT a mathematically valid global error estimate, especially after nth power amplification. Neither |z|>45 nor t>8 tails and no quadrature remainders have been outward bounded.

Execution from repo root after installing NumPy and mpmath:
  python research/m16/2026-11-22/code/m16_rot001_np_risk_diagnostic.py

This is DIFFERENT-CELL numerical source contact only; not an interval I1 on the author's numerical gate, no independent I3, and not the original M13 producer.

## 4. Review verdict, false implications and STOP

**PASS_MATH_SCOPED:** e_(n+1)<e_n, within the original ROT009 simple-hypothesis invariant NP experiment. This result comes from mature Bayes risk theory; NO_GENERAL_NOVELTY.

**NUMERIC_AGREEMENT_ONLY:** independent 500/800 mesh signs around 14539 and 29083. Source claims of 14539 and 29083 as rigorously certified first-n remain on HOLD awaiting two-level outward bounds on inner h/psi integration, outer integration, neglected infinite tails, Delta and roundoff.

**NO_TRANSFERS:** not optimal among non-invariant RAW-site tests, not source-wide or physics-identifiability, not a measured calibration/noise family, not a physical NASH signal. No CANON, no EXEC_SIGN, no BW ingest self-authorization. A source artifact GitHub commit is not its BW registry event.

**REOPEN_IF:** a specifically assigned independent numerical referee supplies complete IV enclosures for e_14538, e_14539, e_29082, e_29083 and both tails; avoid repeated numerical n shaving or uncontrolled task cascades.

This is a bounded nonblind mathematical I1 for monotonicity only plus source numeric diagnostic; author original ROT009 firstness preserved.
