# M14 ROT036 — Gaussian resource allocation restores Chebyshev global E-optimality

artifact_id: IW_M14_ROT036_RESOURCE_ALLOCATED_GAUSSIAN_CHEBYSHEV_E_OPTIMALITY_001_20261110
return_id: M14-ROT036-CHEBYSHEV_LOBATTO_GAUSSIAN_RESOURCE_ALLOCATION_GLOBAL_FIELD_E_OPTIMALITY_001_20261110
date: 2026-11-10
origin: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09 / M14
exposure: PUBLIC
ceiling: EXACT_CLASSICAL_SATURATED_GAUSSIAN_DESIGN / NO_NOVELTY / NO_REAL_NV_SENSOR_DATA / NO_NASH_PHYSICS / NO_CANON / NO_EXEC_SIGN / BW_PENDING / REFEREE_PENDING

## Source provenance and own prior

**XH-S5 ROT007** first owns Schall, Lindner, Rottstaedt et al., *Laser-enhanced quantum sensing boosts sensitivity and dynamic range*, Nature Communications **17**, 10825 (published October 22, 2026), DOI https://doi.org/10.1038/s41467-026-78386-z . Actual four NV orientations and separate 14N triplet source do NOT validate paired signed sensor branches, polynomial orientation drift, equal-variance Gaussian center measurements, independent technical noise or this experiment's budget. Source photon-shot-noise sensitivity figures are **limits**, not measured technical-noise device figures. Never claim original source-data reproduction. M14 ROT031–033 first handled four-axis gauge and bounded orientation drift; ROT034 proved maximal time differences for polynomial calibration; **ROT035** first proved Chebyshev-Lobatto minmax time-node choice under bounded center error and gave an exact **counterexample to fixed-equal-shots Gaussian optimality**. The new ROT036 calculation conditions on *optimizable* replication/exposure allocations, not an overturn of that counterexample. Classical polynomial interpolation, Cauchy–Schwarz, and Gaussian Cramer–Rao; no mathematical novelty claimed.

## Frozen model / target typing

Four axes are rows of A=( (1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1) ); A^T A=4I, ||a_i||²=3. At exactly m+1 distinct times 0=t0<...<tm=L, m=p+1, hypothetically observe g_{ij}=a_i·b(t_j)+eta_i(t_j)+xi_{ij}. Each unknown eta_i is *independent arbitrary polynomial of degree <=m-1*. New independent Gaussian assumption: variance(xi_ij)=sigma²/n_ij, strictly positive exposures n_ij, sum over i,j n_ij=N, constant elemental sigma² and equal costs across all axes/times. Model is an abstract Gaussian mean observation, NOT photon counts or actual NV centroid error. Fractional n is resource relaxation; integer-shot statement is separate.

Let lambda_j=1/product_{k!=j}(t_j-t_k), S=sum_j |lambda_j|, z=sum_j lambda_j b(t_j). Since sum lambda_j t_j^r=0 for 0<=r<m, each orientation quotient y_i=sum_j lambda_j g_ij=a_i·z+epsilon_i eliminates the arbitrary eta_i exactly. Variance v_i=sigma² sum_j lambda_j²/n_ij, independent over orientations. The remaining m directions of raw data per orientation are unconstrained polynomial nuisance and supply NO extra information on z: this is the exact profile, not an estimator-only simplification. Profiled Fisher for the 3-vector z is I_z=sum_i a_i a_i^T / v_i; GLS attains Cov(z_hat)=I_z^{-1}. All globally unbiased regular procedures obey this CRLB in the saturated Gaussian location model.

**Critical comparability gate:** if b(t) is arbitrary, z depends on chosen node set; node optimization then compares variance of different functionals, not precision for a fixed field physical property. If b(t) is polynomial degree <=m on [0,L], z is its common t^m coefficient for every node design. No absolute field, lower polynomial modes or real frequency-to-fT inference follows.

## R36.1 — exact sharp global Gaussian E-optimal design

Denote total exposure on orientation i by n_i=sum_j n_ij. Cauchy–Schwarz gives
v_i/sigma²=sum_j lambda_j²/n_ij >= (sum_j |lambda_j|)²/n_i = S²/n_i,
with equality iff n_ij=n_i |lambda_j|/S. Since ||a_i||²=3,
tr(I_z)=3 sum_i 1/v_i <= 3N/(sigma² S²).
Therefore lambda_min(I_z)<=N/(sigma² S²), and **for every unbiased regular z estimator**
lambda_max(Cov(z_hat)) >= sigma² S²/N.

**SHARP:** choose n_ij = N |lambda_j|/(4S) for every i,j. Then v_i=4sigma² S²/N; I_z=N I_3/(sigma² S²). The GLS estimator z_hat=A^T y/4 attains *isotropic* Cov(z_hat)=sigma² S² I_3/N. Thus the optimal worst-direction variance **for fixed times** is exactly sigma² S²/N. This is a *global Fisher bound over allocations and unbiased estimators*, not just a good plug-in estimate.

From ROT035 / Chebyshev extremal polynomial T_m(2t/L-1): S >= 2^(2m-1)/L^m, with equality **only** at Chebyshev-Lobatto times t_j=(L/2)(1-cos(j*pi/m)). Hence over all legal minimal-window schedules and all continuous exposure allocations:
**min max_{||u||=1} Var(u·z_hat)= sigma² 2^(4m-2)/(N L^(2m)).**
The unique optimal times and balanced exposures achieve it. For Chebyshev nodes, relative absolute lambda weights are 1/(2m) at each endpoint, 1/m at each interior point. **INTEGER SHARP AT N MULTIPLE OF 8m:** each of four orientations gets n_i,end=N/(8m) shots at each endpoint and n_i,interior=N/(4m) at each interior node. At other integer N, continuous expression is a bound, not automatically attained.

## Exact rational m=3 / L=1 / total N=96

| Choice | t | per-orientation shot allocation | S | (Cov z_hat)_{aa} |
| --- | --- | --- | --- | --- |
| Chebyshev-Lobatto | 0,1/4,3/4,1 | 4,8,8,4 | 32 | 32/3 sigma² |
| Equispaced | 0,1/3,2/3,1 | 3,9,9,3 | 36 | 27/2 sigma² |

Both 3x3 covariances are isotropic. The Chebyshev scheme improves variance by exactly 17/81 = 20.987654... percent at **equal N**.

**Preserved negative control from ROT035:** when *each of 16 channels must receive exactly 6 shots*, variance of the simple balanced estimator is sigma² (sum_j lambda_j²)/24. Chebyshev gives sum_j lambda_j²=2560/9. Non-Chebyshev alternative times (0,7/30,23/30,1) give 14630625/51842 <2560/9, therefore win **when shots per channel are locked equal**, but have S=225/7>32 and **lose under reallocation**. No contradiction. Do not substitute real Poisson photon resource statistics for this homogeneous abstract Gaussian model.

## Independent reproducibility and limitations

Moderator-local full ZIP: IW_M14_ROT036_GAUSSIAN_RESOURCE_ALLOCATION_CHEBYSHEV_GLOBAL_E_OPTIMALITY_REPRO_001_20261110.zip, SHA256 d4454f84ad555b21298fb5ae8535e0f3c4411c852e4469b738346b13734481eb, 8 payloads (report, README, two full independent scientific scripts, one compact public stdlib replay, 2 JSON results, manifest); CRC PASS, 8/8 payload SHA PASS, TWO isolated independent JSON regenerations BYTE IDENTICAL, compact exact public Python script PASS.

Pure stdlib Fraction full matrix 3x3 exact Fisher inverse: both covariances, 17/81 gain, 12 integer-realizable m=1..12 counts PASS. Independent mpmath105 + NumPy: m=1..12 Chebyshev sum verification relative error ~1e-106, 1680 randomized time sets, 5000 randomized strictly positive exposure allocations all uphold global lower bound; **full raw 16-observation / 15-parameter Gaussian Fisher**, independently of quotient, matches the quotient Fisher covariance within 1.51e-12. Gaussian Monte Carlo 100000 trials per design reproduces expected three-dimensional covariance diagonals within 0.42%. Random sampling is not a global proof; the analytic argument above is.

NOT PROVEN: original author's sensor paired branches, actual technical-noise or photon shot distributions, correlated drifts or realistic per-time detection costs, more than m+1 times, arbitrary vector-field history invariant across node sets, Poisson optical Fisher, physical sensor fT/sqrtHz uplift, GR/GW/PBH or NASH J3/K physics, full Lorentz inverse, novelty, independent referee acceptance, BW ingest, canon or execution sign. Source publication / dispatch != custody acceptance. NO_NEW_TASK_CASCADE.