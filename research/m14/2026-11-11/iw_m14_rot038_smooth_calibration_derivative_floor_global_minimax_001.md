# M14 ROT038 — ostry globalny minimaks przy nieznanym gladkim dryfcie kalibracji

artifact_id: IW_M14_ROT038_SMOOTH_CALIBRATION_ADAPTIVE_SHARP_MINIMAX_001_20261111
return_id: M14-ROT038-SMOOTH_CALIBRATION_DERIVATIVE_FLOOR_FOUR_VS_THREE_AXIS_GLOBAL_MINIMAX_001_20261111
date: 2026-11-11
cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09 / M14
exposure: PUBLIC
ceiling: EXACT_CLASSICAL_CONDITIONAL_ADAPTIVE_GAUSSIAN_MINIMAX / NO_NOVELTY / NO_NATIVE_SENSOR_DATA / NO_NASH_PHYSICS / NO_CANON / NO_EXEC_SIGN / BW_PENDING / REFEREE_PENDING

## Source typing and precedence

XH-S5 ROT007 FIRST owns the external source: Schall, Lindner, Rottstaedt et al., *Laser-enhanced quantum sensing boosts sensitivity and dynamic range*, Nature Communications 17 (2026) 10825, published 22 Oct 2026, DOI https://doi.org/10.1038/s41467-026-78386-z . The source reports actual NV vector magnetometry, but does **not** validate these hypothetical paired +/− branch centers, C^m orientation calibration stability, independent homoscedastic Gaussian centroid noise, same shot cost, time scheduling or any value H, sigma, gamma. Source 127 fT/sqrtHz is a PHOTON SHOT NOISE LIMIT, not achieved technical-noise sensitivity; no original raw sensor time-series replay.

M14 owners PRIOR: ROT031–033 4-axis gauge and bounded calibration, ROT034 exact polynomial temporal quotient, ROT035 Chebyshev L∞ time nodes and fixed-equal-shot Gaussian falsifier, ROT036 resource optimized Fisher, **ROT037 FIRST GLOBAL ADAPTIVE MINIMAX for exact polynomial nuisance degree<=p**. NEW ROT038: smooth nuisance with NONZERO mth derivative budget H, and SHARP additive irreducible error floor, not a claim of new general mathematics.

## Exact mathematical contract

Let m=p+1>=1, time t in [0,L], L>0. Three or four tetrahedral rows a_i of A = ((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)); A^T A=4I3. Field b(t)=z*t^m + vector polynomial of degree<=m−1; unknown target is SAME z for all schedules. Independent orientation-specific nuisance eta_i in C^m([0,L]) has absolutely bounded mth derivative sup|eta_i^(m)|<=H; lower derivatives and nuisance values UNBOUNDED. Each adaptively chosen time/orientation gives independent Y=a_i dot b(t)+eta_i(t)+Normal(0,sigma²) with uniform cost. Total count N, arbitrary nonanticipating adaptive schedule and any estimator incl biased. Fractional exposures with sigma²/n are continuous relaxation. Set C=2^(2m−1)/L^m, eps=H/m!.

**THEOREM R38.1 EXACT GLOBAL MINIMAX TOTAL VECTOR MSE:**

FOUR AXES: R4* = 3 sigma² C²/N + eps².
THREE AXES: R3* = (9/2) sigma² C²/N + 3 eps².

Equality for continuous exposure allocations and INTEGER N divisible respectively by 8m or 6m. For other integer N these formulas are lower bounds, with rounding gap potentially nonzero. For H=0 the statements reduce EXACTLY to ROT037. The mth-derivative calibration floor does not vanish as N grows; it is 3x bigger in 3-axis than 4-axis squared-risk limit.

## Upper bound — robust Chebyshev construction

Choose t_j=L(1−cos(j pi/m))/2 for j=0,...,m, lambda_j=1/prod_{k!=j}(t_j−t_k), S=sum|lambda_j|=C. Saturated exposure allocation n_ij=N|lambda_j|/(rC) for r=3 or 4 orientations. Per-axis quotient y_i=sum_j lambda_j averaged Y_{i,j} gives y_i=a_i dot z+rho_i+Gaussian noise. Generalized divided-difference mean value theorem for any eta_i in C^m yields rho_i=eta_i^(m)(xi_i)/m! and |rho_i|<=eps, INDEPENDENT of node times. Four-axis zhat=A^T y/4 has variance trace 3 sigma² C²/N and systematic squared bias ||A^T rho/4||²=(1/4)||rho||²−(1/16)(sum rho_i)²<=eps². The bound is sharp with parity-zero rho=eps*(1,1,-1,-1). First three axes zhat=A3^{-1} y has noise trace (9/2) sigma² C²/N and sharp squared bias max_{|rho_i|<=eps}||A3^{-1}rho||²=3eps², achieved at rho=(eps,eps,eps). Gaussian zero-mean noise makes variance+bias² EXACTLY additive.

## Lower bound — source-legal all-time two-world alias + adaptive Gaussian Bayes

Define monic P_m(t)=T_m(2t/L−1)/C with sup|P_m|=1/C and P_m−t^m of degree <=m−1. Select hidden s in {−1,+1} equally, independent u~Normal(0,tau² I3). For r=4 take v=eps*(1,0,0); for r=3 take v=eps*(1,1,-1). In each legal world set
b_(u,s)(t)=(u+s v)t^m,
eta_(i,u,s)(t)=(a_i dot u)*(P_m(t)−t^m) − s*(a_i dot v)*t^m.
All nuisance satisfies |eta_i^(m)|=m!|a_i dot v|<=H. **Exactly for EVERY t, axis, parameter and s:**
a_i dot b_(u,s)(t)+eta_(i,u,s)(t)=(a_i dot u) P_m(t).
Thus observation distributions, including the FULL ADAPTIVE HISTORY, are independent of s, whereas true z=u+s v differs by 2v. Any estimator's conditional posterior squared error is >= tr(Q^{-1})+||v||², where, even for adaptive sampling,
Q=tau^-2 I3 +sigma^-2 sum_{readings r} P_m(t_r)^2 a_{i_r}a_{i_r}^T.
For FOUR axes, tr Q <=3tau^-2 +3N/(sigma² C²), and tr Q^{-1}>=9/tr Q, giving Bayes risk >=3/(tau^-2+N/(sigma² C²))+eps². Let tau→infinity for the EXACT matching global lower bound.

For THREE axes use pathwise Loewner Q <=tau^-2 I +(1/(sigma² C²)) A3^T diag(n1,n2,n3) A3. Trace inverse convex in allocation n and invariant under permutations since A3 A3^T=4I3−11^T. Jensen implies equal n_i=N/3 is best; tr (A3^T A3)^-1=3/2, and tau→infinity yields (9/2)sigma² C²/N +3eps². The matching constructions above establish SHARPNESS even for overcomplete extra times, adaptivity and biased estimators. Without any mth derivative restriction H, same continuous gauge with arbitrary v shows exact NONIDENTIFIABILITY and INFINITE global minimax risk.

## Exact witness and reproducibility

For m=3, p=2, L=1, N=144, sigma²=1, H=3/5: C=32, eps=1/10. Four axes Cheb times (0,1/4,3/4,1), shots per axis (6,12,12,6), exact variance trace=64/3, squared calibration bias floor=1/100, **R4*=6403/300 ≈ 21.34333**. Three axes, shots per axis (8,16,16,8): noise trace=32, squared calibration floor=3/100, **R3*=3203/100 =32.03**. Two distinct signed field worlds have IDENTICAL measured functions for ALL t, and exact synthetic positive triple-Lorentz spectra in all eight branch channels.

Moderator-local full Polish theorem ZIP: IW_M14_ROT038_SMOOTH_DRIFT_DERIVATIVE_BOUND_ADAPTIVE_MINIMAX_FULL_REPRO_001_20261111.zip; SHA256 **de857a7da459a5ba4c887db64af17f9837de77bd6170f14f4457503f0c586284**; 14,468 bytes. ZIP CRC PASS, 7/7 payload SHA256 PASS, two independent clean isolated Python replay result JSON BYTE IDENTICAL, third pure-stdlib exact replay PASS. Exact SymPy: **264** tests incl 168 positive complete three-Lorentz evaluations. Independent mpmath95 and NumPy: 63 high precision Cheb, 900 nonpolynomial smooth calibration perturbations with analytic derivative bound, 1200 all-time world comparisons, 150000 Gaussian Monte Carlo samples PER 3/4 geometry (empirical MSE 21.28712, 31.88653). Numerical checks are NOT proof of globality; Bayes construction above is.

STRICT STOP: no original time-resolved NV sensor data, validated H/gamma/sigma/noise law, physical sensitivity fT, novel physical theory, NASH J3/K/GR/GW/PBH bridge, global nonlinear Lorentz physical inverse, mathematical novelty, external referee return, BW ingestion, LT adoption or canon/execution. NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_PENDING / REFEREE_PENDING / NO_NEW_TASK_CASCADE.