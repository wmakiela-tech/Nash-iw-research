# IW / M14 ROT040 — finite temporal overlap rank, minimal groups, and sharp sequential Lipschitz risk

artifact_id: IW_M14_ROT040_SYNCHRONIZATION_OVERLAP_RANK_AND_SEQUENTIAL_LIPSCHITZ_MINIMAX_001_20261111
return_id: M14-ROT040-TIME_OVERLAP_MINIMAL_GROUPS_UNBOUNDED_COMMON_GAUGE_AND_SHARP_LIPSCHITZ_SEQUENTIAL_MINIMAX_001_20261111
date: 2026-11-11
cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09 / M14
exposure: PUBLIC
claim_ceiling: EXACT_CLASSICAL_CONDITIONAL_FINITE_DESIGN_AND_GAUSSIAN_MINIMAX / NO_NOVELTY / NO_NATIVE_NV_DATA / NO_NASH_PHYSICS / NO_CANON / NO_EXEC_SIGN / BW_PENDING / REFEREE_PENDING

## External source and prior owners

XH-S5 ROT007 FIRST owns Schall, Lindner, Rottstaedt et al, Laser-enhanced quantum sensing boosts sensitivity and dynamic range, Nature Communications 17:10825, published 2026-10-22, DOI https://doi.org/10.1038/s41467-026-78386-z . Real paper reports NV vector orientations; a separate diamond sample resolves 14N triplet. Its 127 fT/sqrtHz is photon-shot-noise fundamental sensitivity LIMIT, not achieved technical-noise sensitivity. It does NOT certify real simultaneous signed-branch centers, temporal scheduling, calibration Lipschitz constants, readout Gaussian noise or equal shot cost. No author's actual time series replay. Mathematics is conditional and classical.

M14 first precedence: ROT031 tetrahedral axes/common-mode geometry; ROT034 temporal polynomial quotient; ROT035 Chebyshev time nodes and fixed equal-shots Gaussian falsifier; ROT036 optimized resources; ROT037 global adaptive Gaussian minimax for polynomial field; ROT038 orientation-specific smooth calibration floor; **ROT039** FIRST common arbitrary spatial drift removed EXACTLY under four-axis matched-time readout. ROT040 tests and repairs the additional hidden requirement of temporal overlap, and gives exact multi-time recovery / sharp sequential penalty. No new general mathematical novelty.

## Frozen synthetic design

Four axis vectors a0=(1,1,1), a1=(1,-1,-1), a2=(-1,1,-1), a3=(-1,-1,1). A^T A=4I3, A^T 1=0. Polynomial vector field b(t)=sum_{q=0}^{m} b_q t^q for m>=1, z=b_m. Finite K distinct exact timestamps t_k, and at time t_k only group S_k of at most r orientations is read; same-time group has ONE arbitrary common scalar h(t_k), where h belongs to C-infinity with UNBOUNDED derivative and amplitude. Y_ik=a_i dot b(t_k)+h(t_k)+noise. No identification by pretending h(t_k)=h(t_l) at different times.

## R40.1 — necessary and sufficient contrast rank for z

For each timestamp group choose base axis i0 and form the |S_k|-1 contrasts Y_i-Y_i0. Construct D with row blocks [(a_i-a_i0)^T * t_k^q] for q=0,...,m, total 3(m+1) columns.

The following conditions are EQUIVALENT: (i) full vector polynomial b uniquely identified noise-free, (ii) highest field coefficient z=b_m uniquely identified, (iii) rank D=3(m+1).

Proof: full rank recovers coefficients. For any polynomial difference db(t) in ker D, all a_i dot db(t_k) share a common scalar within their group; interpolate dh(t_k)=minus that scalar by a polynomial of degree <=K-1. Then h+dh is a legal smooth common drift and every FINITE observed mean agrees between two distinct fields. Most importantly, if db has degree d<=m, then t^(m-d) db is also in ker D and has NONZERO highest coefficient. Thus any nonzero rank defect aliases z, with arbitrary scalar magnitude, implying INFINITE global minimax risk (even when measurements have Gaussian noise) without derivative bounds on h. This is a result for FINITE time slots, NOT a theorem for continuous time-series access.

In particular with completely distinct axis timestamps, |S_k|=1, D has no nonzero rows. Any finite number of fully asynchronous singleton observations can be masked by one perfectly smooth interpolating h, no matter how small (nonzero) the physical staggering is. C-infinity/analytic h without a quantitative bound does not fix the finite-observation gauge.

## R40.2 — EXACT SHARP minimal coincident-time groups

If each timestamp can read at most r orientations (r=2,3,4), the **minimum number of distinct timestamps for unique b and z** is

K_min(r,m) = ceil(3*(m+1)/(r-1)).

NECESSITY: one group has at most r-1 independent common-drift-free contrasts; 3(m+1) free field coefficients require K(r-1)>=3(m+1), and by R40.1 no lower-rank design can even identify z.

SUFFICIENCY FOR ANY DISTINCT TIMES, constructively, write n=m+1:
- r=4: use all four axes on n distinct timestamps; each group gives 3 independent field coordinates; interpolate the degree<=m vector field.
- r=2: use n distinct timestamps of pair (0,1), another n of (0,2), and another n of (0,3): the three difference vectors form an invertible basis, and each scalar polynomial has n zeros if the contrast vanishes.
- r=3: use K=ceil(3n/2) timestamp groups observing triples, omitting respectively axes 0,1,2. For n even n=2q take q groups of each omitted axis; for n odd n=2q+1 take q+1,q+1,q. The vectors a0,a1,a2 span R3. Write any zero-contrast db(t)=c0(t)a0+c1(t)a1+c2(t)a2, each c polynomial deg<=n-1. A triple omitting axis j forces the other TWO c-polynomials zero at that timestamp (all other a_i dot a_j equal -1). Each c_l has at least K-number_omitting_l >=n distinct roots, so all c_l identically zero. This certifies full rank for all m and every distinct grid, NOT a generic random rank claim.
- r=1: zero contrasts, no finite design suffices.

Examples: m=1: K_min r4=2, r3=3, r2=6; m=2: 3,5,9; m=3:4,6,12; m=4:5,8,15.

## R40.3 — explicit 3-triple recovery without EVER four simultaneous axes

m=1, L=1; times t=(0,1/2,1); groups S0=(1,2,3), S1=(0,2,3), S2=(0,1,3). The full 6x6 rational contrast matrix D for coefficients (b0_x,b0_y,b0_z,z_x,z_y,z_z) has EXACT determinant +64. Thus the full field is recovered with arbitrary smooth common drift and no four-way simultaneous observation.

With q independent identical Gaussian shots per each of the 9 original axis-time slots, variance sigma²/q per averaged raw slot, note each pair of same-time contrasts shares the same base noise and is CORRELATED. Using the exact 6x6 inverse, the slope z covariance is

Cov(z_hat)=(sigma²/q)*[[11/4,0,9/4],[0,5/4,0],[9/4,0,11/4]],
trace Cov=27 sigma²/(4q).

For N=9q=72, q=8, this design's trace risk is 27sigma²/32; against the previous ROT037 matched four-axis, two-time resource-optimized risk 12sigma²/N=sigma²/6 at the SAME budget, the ratio is exactly 81/16=5.0625. This is the cost of THIS explicit three-triple design, NOT a lower bound on all three-axis schedules.

## R40.4 — SEPARATE constant-field four-slot sharp Lipschitz minimax

Different target: static field b(t)=z (m=0), four sequential NONSIMULTANEOUS slots t_i=i*Delta for axes i=0..3 respectively, Delta>0. Unknown h is common globally and H-Lipschitz, so |h(t)-h(s)|<=H|t-s|. At each fixed slot only its assigned axis is measurable, repeated n_i times with independent equal-cost Gaussian variance sigma² per elemental sample; total N. Resource allocation can adapt among THESE FOUR FIXED SLOTS, but NO extra timestamps or different axis in another slot.

The 3x3 successive-axis difference matrix D_s has rows a_{i+1}-a_i and EXACT determinant -16; from successive observed means d, compatible z form the EXACT parallelepiped |d-D_s z|<=H Delta coordinatewise. Each vector of three bounded increments is realized by a legal piecewise-linear h. Its Euclidean minimax Chebyshev radius is

rho = sqrt(5)/2 * H*Delta, squared rho²=(5/4)*H²*Delta².

The center D_s^-1 d equals A^T Y /4. Exact worst-case witness is fully smooth LINEAR h_+(t)=H(t-3Delta/2) and h_-(t)=-h_+(t), paired with fields u+v and u-v for v=H Delta*(1,1/2,0), respectively: all four SLOT observations have exactly the SAME conditional means a_i dot u, while targets differ by 2v and ||v||²=5 H²Delta²/4.

With total N divisible by 4, the **GLOBAL (all adaptive allocation, including biased estimators) Gaussian minimax risk** for this restricted slot protocol is EXACTLY

R_seq* = 3sigma²/N + (5/4) H²Delta².

UPPER: equal n_i=N/4, estimator A^T averagedY/4, trace variance 3sigma²/N and sharp worst squared bias 5H²Delta²/4. LOWER: proper prior u~N(0,tau² I3), independent sign s, (z_s=u+s v, h_s=-s H(t-3Delta/2)); every measurement is independent of s. Adaptively realized Gaussian posterior precision Q=tau^-2 I3+sigma^-2 sum a_i a_i^T; traceQ <=3tau^-2+3N/sigma². Trace inverse >=9/traceQ, so diffuse prior gives risk floor 3sigma²/N PLUS unobservable ||v||². Equal allocation attains it; no overclaim for arbitrary extra times/axes. N nondivisible 4: formula is a lower bound, not automatically attained.

This sharp static result differs from high-degree polynomial-field temporal minimax ROT037–039; it does not claim universal superiority of synchrony under all field/drift/noise physical laws.

## Repro and audit

Moderator-local full ZIP: IW_M14_ROT040_TIME_OVERLAP_GAUGE_THREE_AXIS_RECOVERY_SEQUENTIAL_LIPSCHITZ_FULL_REPRO_001_20261111.zip, 19,646 bytes, SHA256 61403b7967ecea1914c6599b1c4bfb64be333aa6ef95257b8e8c4c15aefa14b5. ZIP CRC PASS, payload SHA manifest 8/8 PASS. Two distinct independent full Python exact/numeric scripts rerun from clean archive regenerate each JSON BYTE IDENTICALLY; public pure-stdlib exact script PASS.

Exact SymPy Fraction-style 147 assertions: all full-rank constructive r2/r3/r4 for n=1..8, determinant64, exact correlated Gaussian contrast covariance, 12 distinct-slot analytical smooth aliases at m0..3, sharp bounded slot bias, positive/negative full witness. Independent mpmath90+NumPy 5945 assertions: 500 random full field/different common h recoveries at high precision, 4000 random Lipschitz increments, 1440 asynchronous interpolation alias evaluations, two independent 120000-trial Gaussian MC risk checks. MC measured 0.8441196564 against exact 0.84375 for triple-groups N72, and 0.0235903474 against exact 0.023625 for sequential slots N40/H0.75/Delta0.04/sigma²0.3. Numerical tests do NOT prove universal theorem; exact algebra and Bayes lower are proof.

STRICT SCIENTIFIC STOP: no original Schall synchronous timestamp acquisition or raw center data, no hardware certified H/sigma/gamma, photon statistics, timing jitter or calibration, no actual fT gain, no novel mathematical result or new GR/GW/PBH/NASH J3K physical claim, no external referee acceptance, no BW ingest, no LT adoption. POSTED != ACK. NO_NOVELTY / NO_NASH_PHYSICS / NO_CANON / NO_EXEC_SIGN / BW_PENDING / REFEREE_PENDING / NO_NEW_TASK_CASCADE.