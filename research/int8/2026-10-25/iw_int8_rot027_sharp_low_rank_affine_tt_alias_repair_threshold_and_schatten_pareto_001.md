---
artifact_id: IW_INT8_ROT027_SHARP_LOW_RANK_AFFINE_TT_ALIAS_REPAIR_THRESHOLD_AND_SCHATTEN_PARETO_001_20261025
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
date: 2026-10-25
problem_id: P3_DTC0A_AFFINE_METRIC_TT_RAW_WAVEVECTOR_ALIAS_INTERFACE_001
exposure: PUBLIC_SAFE
evidence: EXACT_ECKART_YOUNG_SPECTRAL_RANK / FULL_SINGULAR_SPECTRUM / INDEPENDENT_6x6_SVD / BYTE_SHA_CHECKED_SOURCE_HELPER / CLEAN_REPRODUCTION_PASS
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# INT8 ROT027 — exact minimum rank of approximate affine TT alias repair

## Source-currentness, ownership, and subtraction

Slack #iw-dispatch source inspected Oct 25, 2026, including current M13 and Geeky-S11. MT13 FIRST proved finite affine metric-local filter E_g U_A=U_A E and reported failure of naive raw-k metric TT re-projection on folded spectra. XH-S4 owns moving York/curved metric. INT8 ROT023: exact nofold census and highband TT loss; ROT024: EXACT full operator norm and source Hs rate; ROT025: full singular values, rank of EXACT repair, Hilbert–Schmidt norm; ROT026: synthetic colored Gaussian covariance and s=3/2 threshold. M13 owns historical h=fI, KA and moving masks; PRF11 owns different Lie/TT collocation, Geeky-S11 even matched-symbol TT finite-difference. NEW narrow delta: SHARP tolerance-to-rank Pareto frontier for approximation of the ALREADY FIXED finite operator D and asymptotic extensive rank cost, NOT original phenomenon or mathematical novelty. All claims use mature finite Fourier/Eckart–Young–Mirsky host.

## Mathematical carrier

N=2m+1 ODD >=9; periodic (Z/NZ)^3, real symmetric 3x3 tensor arrays; complete unmasked 6N^3-dimensional flat input Frobenius L2 and target g-Frobenius L2. Shear A=[[1,1,0],[0,1,0],[0,0,1]], g=A^T A FLAT, U_A H(x)=A^T H(Ax mod N)A is isometric in these declared inner products.

Source E_alpha=I+alpha Σ_j(tau_ej+tau_-ej−2I), alpha=.05, Fourier multiplier e(k)=1−4alpha Σ_j sin²(pi k_j/N), e(k)>=.4>0. This is user-retained helper apply_E, SHA256 **23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801**, NOT the byte-unavailable historical production dtc0a_runtime_v0_3_1.py. Metric-transported E_g, standard source raw-wavevector Fourier TT P, and recomputed target metric raw-k P_g^raw:

    D=P_g^raw E_g U_A−U_A P E_alpha.

For source k in signed B_N with |kx+ky|<=m, D(k)=0. Otherwise ell=(kx,ky−N sign(kx+ky),kz), c_k=|k dot ell|/(|k||ell|). In the isometrically conjugated Euclidean tensor frame:

    D(k)=e(k)[Pi_ell−Pi_k].

ROT025's exact NONZERO singular values on each folded mode are:

    a_k=|e(k)| sqrt(1−c_k²), MULTIPLICITY TWO;
    b_k=|e(k)| sqrt(1−(1+c_k²)²/4), MULTIPLICITY TWO,
    with a_k>=b_k>0; remaining two singular values zero.

On source TT range (rank2 except k=0 convention) there is ONE copy of each a_k,b_k. Folded mode count M_N=N(N²−1)/4. Real Fourier conjugate ±k pairs lead to REAL total ranks, not a factor-two extra count. Source and target norm types explicit.

## Theorem 027.1 — SHARP and ATTAINED spectral error vs minimal correction rank

For epsilon>=0, among ALL REAL linear corrections C to this specified operator D (no requirement of spatial locality or low computational cost), the least possible rank attaining ||D−C||_(L2→L2(g))<=epsilon is EXACTLY

    r_epsilon(N)
       =2 sum_(k folded){1[a_k>epsilon]+1[b_k>epsilon]}.

On source TT domain the analogous exact minimum is half this number:

    r_epsilon^TT(N)
       =sum_(k folded){1[a_k>epsilon]+1[b_k>epsilon]}.

Proof: Eckart–Young sharp spectral-norm SVD truncation, retaining all singular values STRICTLY GREATER than epsilon. Orthogonal Fourier blocks make the global singular multiset the disjoint union of per-mode spectra. All symmetry-related ±k modes can be retained together, so the cutoff correction has a real representation. In particular r_0=N(N²−1) and r_0^TT=N(N²−1)/2, recovering EXACT ROT025. No claim lower bound for arbitrary redesigns of the raw projector/observable or locally supported real-space stencil.

## Theorem 027.2 — SHARP Schatten-2 accuracy-cost curve

Let s_1>=...>=s_R>0 be complete positive singular spectrum, R=N(N²−1). Among corrections rank<=r,

    min_(rank C<=r)||D−C||_HS² = Σ_(j=r+1)^R s_j².

Thus the minimum rank retaining eta∈{.50,.90,.99} of the SQUARED HS norm is the smallest r with Σ_(j<=r)s_j²>=eta Σ_(j<=R)s_j². These are algebraic Hilbert-space error measures, not fractions of physical gravitational-wave energy.

## Theorem 027.3 — non-vanishing volumetric rank density

Scale u=k/N in C=[−1/2,1/2]^3 and define folded region F={|ux+uy|>1/2}, volume 1/4; v=(ux,uy−sgn(ux+uy),uz), c(u)=|u·v|/(|u||v|), e(u)=1−4alpha Σ sin²(pi u_i), and analogs

    a(u)=|e(u)| sqrt(1−c(u)²)
    b(u)=|e(u)| sqrt(1−(1+c(u)²)²/4).

At epsilon with zero-measure threshold level sets (true for chosen epsilon=.10,.25,.50,.70, alpha=.05), Riemann sums imply

    lim_(N odd→∞) r_epsilon(N)/N³
       =2 ∫_F [1_{a(u)>epsilon}+1_{b(u)>epsilon}] d³u.

For EVERY epsilon below the positive maximum of a on the folded interior, this integral is strictly positive; hence a bounded-error correction within this contract REQUIRES rank Θ(N³), not o(N³), at fixed sufficiently small epsilon. At epsilon>=max a the trivial zero correction suffices; no stronger claim. This is a full L2 input statement, NOT a Hs unit-ball statement from ROT024.

## Exact numerical minimax, alpha=.05

Ranks for full 6N³-dimensional real tensor source; source-TT minimum is exactly half these integers.

|N|EXACT rank|r_epsilon=.25|r_epsilon=.50|r_epsilon=.70|min rank retaining 99% HS²|
|--:|--:|--:|--:|--:|--:|
|31|29760|29672|21016|1352|28967|
|33|35904|35816|25364|1636|34947|
|35|42840|42728|30284|1940|41695|
|37|50616|50484|35804|2308|49264|
|39|59280|59096|42032|2696|57698|
|41|68880|68672|48744|3140|67040|
|101|1030200|1027228|729216|46880|1002613|
|201|8120400|8097076|5746460|369712|7902883|

At epsilon=.50 roughly 70.6–70.9% of the exact correction rank must be retained across source odd grids 31–41; at epsilon=.70 only ~4.55% rank, but residual error is still about .70 compared with unrepaired ||D||op≈.79. Retaining 99% of squared HS norm demands ~97.33% of exact rank (N31 28967 of 29760; N41 67040 of 68880), exposing poor HS compressibility. Rows N9,15,63 and epsilon .10 are in standalone JSON. NOT cost or accuracy percentages of historical KA.

## Independent EXECUTED falsifiers and source readback

Main NumPy analytic wave formula enumerated all signed modes at odd N9,15,31,33,35,37,39,41,63,101,201, counted spectral strict thresholds (.10,.25,.50,.70), computed sorted HS² energy spectra and optimal capture rank. Independent direct 6x6 projector SVD on 24 random folded modes N9,15,31,41: COMPLETE ordered singular-value discrepancy max 4.44e−16. Third, independent EXHAUSTIVE real-Frobenius 6x6 SVD for EVERY folded mode N9 and N15 independently recovered r_epsilon at all four thresholds, exact rank and HS² to <1e−8 absolute. N9: rank720; N15: rank3360. Byte SHA-verified actual user helper apply_E on random symmetric arrays N9,15 agrees independent 7-point stencil; unmodified apply_P_TT retains genuine flat Fourier TT cosine carriers.

Transparent rejected preliminary controls: epsilon=.75 at N15 hit a nearly EXACT threshold equality in float, so this value was WITHDRAWN from numerical certification (final epsilon=.70 has no near equal singulars). An initial direct 6x6 basis control used sum(X@Y) instead of Frobenius sum(X*Y), causing a FAILED symmetry check; correct Frobenius-normalized basis and full matrix eigentests subsequently PASS. Neither failed control is counted as evidence of the claim.

## Local reproducibility custody

Complete 7-member zip contains FULL ~9K report, standalone NumPy reproducer, independent exhaustive direct SVD audit, complete JSON, execution log, README and SHA256SUMS. Artifact:
  iw_int8_rot027_low_rank_alias_repair_bundle.zip
SHA256 **1ad1730af6272c3cb9086436bef8805e67bea755d0af211dc3f7c2f58aeaf0c3**.
Zipfile CRC PASS, SHA256 manifest **6/6 PASS** (manifest lists six content files), TWO clean directory re-executions PASS: without helper mathematical work and independent audit PASS / source check explicitly SKIPPED; with SHA-verified unmodified helper ALL PASS, reproduced JSON BYTE IDENTICAL. Neither original helper nor its original production missing runtime is redistributed. Executable full code is in Moderator conversation ZIP; code GitHub publication NOT claimed by this report.

## STOP, cross-cell routing, no upgrade

Affine FLAT finite-torus representation only; D precisely typed, no claim true curved York, general covariant Box, physical gauge invariants J3/K, gravitational-wave energy, actual historical masked DTC0a KA or PBH interpretation. SVD optimal abstract rank is NOT a locally implementable stencil guarantee; no background independence or new math/physics novelty. Owner adoption/BW ingest/referee/Moderator EXEC pending, no new task cascade.

NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / BW_PENDING / REFEREE_PENDING.
