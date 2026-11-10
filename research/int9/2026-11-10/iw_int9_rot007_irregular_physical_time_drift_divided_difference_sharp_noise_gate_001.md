---
artifact_id: IW_INT9_ROT007_IRREGULAR_TIME_POLYNOMIAL_DRIFT_M14_XH_SPIDER_001_20261110
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_09 / INT9
date: 2026-11-10
exposure: PUBLIC_SAFE
claim_ceiling: CLASSICAL_CONDITIONAL_RETYPE_ONLY / NO_REAL_NV_TIMESTAMPS / NO_OU_TRANSFER / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---
# INT9 ROT007 — time-polynomial drift retyping and sharp irregular-grid noise gate

## Original source order
Schall et al., *Laser-enhanced quantum sensing boosts sensitivity and dynamic range*, Nature Communications 17:10825 (2026-10-22), DOI https://doi.org/10.1038/s41467-026-78386-z, first real NV source. Original paper does NOT demonstrate the hypothetical paired four-tetrahedron real-time drift contract here. M14 ROT034 FIRST supplies the **source model with equally spaced samples and degree-p drift in sample INDEX k**, full result https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m14/2026-11-08/iw_m14_rot034_temporal_polynomial_nv_drift_field_difference_maximal_invariant_sharp_error_001.md ; Git blob 331c1cc20b4d3d2bf3ff77afb8e70ea318a015bf. Smith et al., *Estimating the resilience of non-stationary systems*, Nature Communications 17:11286 (2026-11-06), DOI https://doi.org/10.1038/s41467-026-78489-7, and XH-S5 ROT024 https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s5/2026-11-08/iw_xh_s5_rot024_smith2026_resilience_measurement_noise_irregular_sampling_domain_gate_001.md, first own resilience/OU irregular sampling source and noise warning. Neither is the same physical model.

**STRICT TYPE GATE:** this INT9 result is valid only AFTER REPLACING M14 original eta_i(k)=polynomial_in_sample_INDEX with a NEW AND DIFFERENT assumption eta_i(t)=polynomial_in_PHYSICAL_TIME. With uneven sampling these contracts are not equivalent; do not transfer the M14 theorem silently. Ordinary divided differences are classical mathematics, no novelty claimed.

## Exact source-conditional theorem
Hypothetical four axes A rows (+++),(+--),(-+-),(--+), with A^T A=4I3, A^T 1=0. At p+2 distinct physical timestamps t0<...<tm, m=p+1, observe g_i(tj)=a_i dot b(tj)+eta_i(tj)+xi_ij where eta_i is any polynomial of PHYSICAL t degree <=p and |xi_ij|<=delta is independently established. Put h=(tm-t0)/m and
    alpha_j = (m! h^m)/product_{ell!=j}(t_j-t_ell),
    D_t f = sum_j alpha_j f(tj).
Lagrange interpolation gives sum_j alpha_j*tj^r=0 (r=0..p), hence D_t eta=0 and D_t g=A D_t b + D_t xi. In the noiseless case D_t b=A3^{-1} D_t g[1:3] from 3 axes; from 4 axes D_t b=A^T D_t g/4 and sum_i D_t g_i=0. This target is the normalized top interpolation divided difference, NOT absolute field or field velocity. For equal steps the weights reduce to (-1)^(m-j)*binom(m,j), exactly M14's index Delta^m.

Polynomial physical-time gauges b'=b+h(t), eta_i'=eta_i-a_i dot h, deg h<=p, leave full observations identical. Conversely on minimal p+2 timestamps, equal source readings imply the difference in field samples lies on a polynomial of t degree<=p. Thus this D_t b is complete at this stated quotient level, not a full field time-history inverse.

## Sharp deterministic error
The sharp per-channel bound is kappa_t=delta*sum_j |alpha_j|; any chosen +/-kappa_t appears from legitimate raw errors xi_ij=+/-delta sign(alpha_j). The four channels' post-difference noise cover the full cube [-kappa_t,kappa_t]^4. Source M14 tetrahedral proof therefore carries over **only via this exact cube-identification**, with worst-case Euclidean four-axis radius kappa_t and three-axis radius sqrt(3)*kappa_t, per minimal window; no multitime stochastic independence or NV device noise claim.

## Two-way exact counterexample and sharp schedule ratio
At p=1, physical times (0,1/2,2), total span T=2:
    time-typed normalized alpha=(2,-8/3,2/3), sum |alpha|=16/3;
    original INDEX difference coefficients=(1,-2,1).
For physical-time drift eta(t)=t, INDEX difference gives 1 (spurious nonzero field curvature), while correct time-divided difference gives 0. REVERSE: for original M14 lawful index drift eta(k)=k, INDEX difference gives 0 but time-divided difference gives -4/3 (spurious signal). This disproves both untyped transfers.

For equal-time grid (0,1,2) under same T and error delta: alpha=(1,-2,1), sum |alpha|=4. Irregular middle time 1/2 therefore raises the sharp radius by (16/3)/4=4/3 (33.333%). With delta=.01, radii are .04 and .053333... . General middle x in (0,2): sum |alpha| = 4/[x(2-x)], minimized at x=1 and divergent as x approaches either endpoint. The result is exact, not a real NV experimental estimate.

## Evidence, limits, custody
Independent INT9 Python 3 standard-library fractions.Fraction with seed 20261110: 705 grouped exact checks of polynomial annihilation for p0..3 over 5 rational grids, Lagrange-product versus separately written recursive Newton divided difference for 40 arbitrary rational sequences each, 15 multi-axis random field/gauge source checks per grid, all 4-axis noise cube corners, dual contract falsifiers. No author NV hardware, Smith OU regression, physical quantum experiment or M14 original code was rerun. Local full report SHA256 b482be6b4f5221a599057262a30f4992cd7a6bda91583c815bcca84175360a13; local standalone 6-member ZIP SHA256 93ba1eff69c065c71e54c99a5a9dacb2688131790e0c2e0b596dda99498f4c72. ZIP CRC, five member SHA256 and clean deterministic replay PASS; local bytes are NOT asserted as remotely hosted on GitHub.

Owner gate if scientifically needed: actual irregular physical timestamps, actual verified model variable (index versus t), independent delta and paired-center extraction are required. Do not infer real 127fT/sqrtHz performance, force XH climate OU estimator into polynomial model, or substitute PRF12 Lipschitz-drift calibration. No automatic owner task, BW ingestion, referee pass or physical new result.

STATUS: INDEX_TO_TIME_RETYPE_REQUIRED / EXACT_DIVIDED_DIFFERENCE_PASS / SHARP_NOISE_RATIO_4_OVER_3 / TWO_WAY_NONMAP / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / GITHUB_PENDING_BW_INGEST.
