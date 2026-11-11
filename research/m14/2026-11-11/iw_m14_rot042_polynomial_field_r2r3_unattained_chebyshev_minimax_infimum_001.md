# M14 ROT042 — polynomial-field r2/r3 sharp but UNATTAINED temporal minimax infimum

artifact_id: IW_M14_ROT042_POLYNOMIAL_FIELD_GROUP_CAPACITY_UNATTAINED_CHEBYSHEV_INFIMUM_001_20261111
return_id: M14-ROT042-POLYNOMIAL_FIELD_PAIR_TRIPLE_FINITE_TIME_NONATTAINED_MINIMAX_AND_CHEB_CLUSTER_001_20261111
date: 2026-11-11
origin: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09 / M14
exposure: PUBLIC
claim_ceiling: EXACT_CLASSICAL_NONADAPTIVE_FINITE_CALENDAR_GAUSSIAN_GLOBAL_INFIMUM / PROVEN_NONATTAINMENT / NO_NOVELTY / NO_NATIVE_NV_DATA / NO_NASH_PHYSICS / NO_CANON / NO_EXEC_SIGN / BW_PENDING / REFEREE_PENDING

## FIRST sources and prior ownership

XH-S5 ROT007 FIRST owns the original external source: Schall, Lindner, Rottstaedt et al., Laser-enhanced quantum sensing boosts sensitivity and dynamic range, Nature Communications 17 (2026) 10825, published Oct 22 2026, DOI https://doi.org/10.1038/s41467-026-78386-z . The paper's 127 fT/sqrtHz is a PHOTON-SHOT-NOISE sensitivity LIMIT, not achieved technical-noise sensitivity. Source does not establish actual paired signed NV branches, homogeneous Gaussian centroid errors, arbitrary smooth common temporal drift or time-group resource costs; NO original sensor-native time-series replay. M14 ROT040 FIRST finite co-time rank and minimum timestamp group numbers for degree-m vector fields, ROT041 FIRST global static m=0 group-size 2/3/4 Gaussian minimax and co-time graph. ROT035-039 own earlier time-Chebyshev, resource Fisher, exact common and smooth calibration cases. ROT042 changes the target to nonstatic polynomial field with r2/r3 co-time capacity. General math is classical Chebyshev polynomial regression design, NIST DLMF 18.38(i) https://dlmf.nist.gov/18.38 ; general mathematical novelty NOT claimed.

## Frozen conditional model

Tetrahedral axes a0=(1,1,1), a1=(1,-1,-1), a2=(-1,1,-1), a3=(-1,-1,1), A^T A=4I3. Field b(t)=sum_{j=0}^{m-1} b_j t^j + z t^m on [0,L], m>=1; all vector lower coefficients unknown, target z shared across time-node designs. A **FINITE PREDECLARED NONADAPTIVE CALENDAR** has distinct exact timestamps t_k, and only a subset S_k of at most r=2 or r=3 axes is read at each timestamp. At time t_k, every observed axis shares an unknown scalar h(t_k), where h belongs to C-infinity on [0,L] but is UNBOUNDED in values and derivatives. Any finite values of h(t_k) are jointly legal via smooth polynomial interpolation. Raw independent Gaussian Y=a_i dot b(t_k)+h(t_k)+Normal(0,sigma²), uniform cost per unit shot, total N. Any estimator including biased. Nonlinear physical sensor response, nonpolynomial b, adaptive selection of NEW timestamps and timing jitter are NOT included.

## R42.1 exact global infimum; strict nonattainment for EVERY finite identifiable design

Let C_m=2^(2m−1)/L^m and r in {2,3}. Over legal finite calendars and all estimators and exposures:
**inf_{calendar,estimator} sup_{b,h} E||zhat-z||² = [9r/(4(r−1))] sigma² C_m²/N.**
The infimum equality is proven for continuous exposure allocations and integer N divisible by 24m. For other integer N only the universal LOWER BOUND is certified, not equality.

LOWER and all-estimator proof: P_m(t)=T_m(2t/L−1)/C_m is monic with sup|P_m|=1/C_m. Legal subfamily b_u(t)=u P_m(t), target z=u. After profiling unrestricted h(t_k), Gaussian effective FI_u is J=sum_k P_m(t_k)^2 F_k,
F_k=sigma^-2[sum_i n_ki ai ai^T−(sum_i n_ki ai)(sum_i n_ki ai)^T/n_k].
Tetrahedral Gram ai dot aj=−1 for i!=j implies tr F_k=4(n_k−sum n_ki²/n_k)/sigma²<=4n_k(r−1)/(r sigma²).
Consequently tr J<=4N(r−1)/(r sigma² C_m²), tr J^-1>=9/tr J >= [9r/(4(r−1))] sigma² C_m²/N; if J singular risk diverges. Proper Gaussian priors on u and the finitely many smooth-interpolable h_k, followed by diffuse limits, extend this bound to ALL estimators (biased included), not only CRLB-unbiased ones.

NONATTAINMENT: |P_m| attains 1/C_m at precisely m+1 separate Chebyshev-Lobatto extrema. Yet full identification of z from co-time contrast data with group size r<=3 requires at least ceil(3(m+1)/(r−1))>m+1 INFORMATIVE separate group timestamps (ROT040 exact contrast rank). Hence some positive-cost informative session necessarily lies away from a Chebyshev extremum where |P_m|<1/C_m; then tr J is STRICTLY below the universal maximum, making the minimax risk STRICTLY GREATER than the infimum at every finite identifiable calendar. A rank-deficient calendar has exact arbitrarily large field aliases and INFINITE risk. There is NO uniform positive gap across all calendars.

## R42.2 LEGAL near-optimal construction and exact asymptotic upper

Let B=binom(4,r)=6 for pairs or 4 for triples, and enumerate all B subsets G_g of exactly r distinct axes. Let ideal Cheb times tau_j=L/2(1−cos(j*pi/m)), j=0..m. For epsilon sufficiently small set alpha=1−(B−1)epsilon/L and choose distinct timestamp grid:
**t_gj=g*epsilon+alpha*tau_j.**
Every one of B(m+1) timestamps is different and in [0,L], and only G_g is measured at time t_gj. The unknown common h is NOT equated across near timestamps.

Within group g, divided-difference top-coefficient weights scale lambda_gj=alpha^(−m)lambda_star_j, sum|lambda_star|=C_m. Give each axis in group/time n_gji=(N/(B*r))*|lambda_star_j|/C_m unit shots; Cheb endpoint share 1/(2m) and interior share 1/m. B*r=12 for either r, so integer counts for N divisible by 24m.

Taking a separate time-divided difference for EACH axis of EACH group yields d_gi=ai dot z+q_g+noise, where q_g=sum lambda_gj h(t_gj) is a FREE group-specific scalar. Across axes within group independent Gaussian noise has variance v_g=B*r*sigma²*C_m²/(N alpha^(2m)). After profiling q_g independently and combining ALL B groups, the constructed GLS has isotropic FI=4(r−1)N alpha^(2m)/(3r sigma² C_m²) I3 and EXACT risk:
**R_construct(epsilon)=R_inf/[1−(B−1)epsilon/L]^(2m).**
The FULL RAW GLS may additionally use common lower polynomial coefficients across groups, so rigorously
**R_inf < R_full_raw_GLS(epsilon) <= R_construct(epsilon)**,
and R_full_raw_GLS tends to R_inf as epsilon tends to zero from above. At epsilon=0 different r-subsets would coalesce at the SAME timestamp, thereby exceeding the r-axis hardware capacity; this limit is NOT an allowed finite schedule. No common drift regularity is inferred from near times.

## Exact m1 comparison and independently reproduced polynomial cases

Set m=1,L=1,N=240,sigma²=1; exactly 10 unit Gaussian observations per raw channel, fixed equal resource. r4 fully simultaneous Cheb optimum from ROT037 is .05. For r3 (all 4 triples, each at 2 own times, 8 distinct sessions / 24 channel averages), infimum **9/160=.05625**; full RAW Gaussian GLS risk at epsilon=.01 **.059756726669589**, epsilon=.001 **.056588787640386**, constructive upper epsilon=.001 .056589024847864. For r2 (all 6 pairs, each 2 own times, 12 distinct sessions /24 channel averages), infimum **3/40=.075**; full RAW risk at epsilon=.01 **.083048831578411**, epsilon=.001 **.075755216379256**, constructive upper epsilon=.001 .075755662735790. Both raw models include all six field coefficients plus free separate h_k in EVERY session.

10 SymPy EXACT RATIONAL tests of full field profiled FI for m1,m2,m3 with r2/r3 validate strict sandwiches, 121 assertions. Independently full RAW regression including ALL h_k columns uses mpmath95+NumPy; 6 high-precision comparisons agree with rational results at RELATIVE <1e-70; 500 randomized legal resource/calendar tests respect lower bound; 120000 synthetic Gaussian MC observations with LARGE NONPOLYNOMIAL common h validate resulting MSE with max relative error 0.4853%. Numerical experiments validate but do NOT prove global theory. Third independent pure-stdlib Fraction script reproduces exact m1 r2/r3 positive-gap and Cheb-near-limits.

Local full ZIP, 20,630 bytes, SHA256 0947f01f1be73ac289011f0ae02591c904971dc4736273d59047c6349ba07d72; payload SHA256 8/8 PASS, ZIP CRC PASS; all 3 scripts cleanly rerun after extraction; scientific JSON regenerated BYTE IDENTICAL 2/2. Full original Polish report, independent executables, original JSON, README, dispatch, SHA manifest. ZIP is LOCAL ONLY (not GitHub-hosted).

## STRICT interpretation / STOP

No source-native NV time data, actual independent Gaussian center noise, instrument grouping timing feasibility, real H or sigma/fT, physical photon measurements, nonpolynomial vector field, adaptively chosen future NEW timestamps, new NASH J3K GR/GW/PBH result, novelty, independent REC11/AUD1 referee verdict, BW ingest, LT adoption, canon or EXEC signature. POSTED != ACK. **NO_NOVELTY / NO_NASH_PHYSICS / NO_CANON / NO_EXEC_SIGN / BW_PENDING / REFEREE_PENDING / NO_NEW_TASK_CASCADE.**