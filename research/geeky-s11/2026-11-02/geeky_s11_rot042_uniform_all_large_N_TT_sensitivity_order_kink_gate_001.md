---
artifact_id: GEEKY-S11-ROT042-UNIFORM-ALL-LARGE-N-TT-SENSITIVITY-ORDER-KINK-GATE-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-11-02
problem_id: P3_DTC0A_SOURCE_FINITE_GRID_PHASE_UNIFORM_ALL_N_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: ANALYTICAL_ALL_LARGE_N_BOUND_PLUS_DIRECTED_INTERVAL_CONTINUUM_GAP_176_TYPED_CHECKS_PASS
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / REFEREE_PENDING / BW_PENDING
---

# ROT042 — every sufficiently large even grid favors ROT038 channels on the FIXED ROT039 adverse schedule

## FIRST own scientific lineage

ROT015–017 first corrected even-grid auxiliary realcast raw-k TT projection to genuine real-compatible B=GA. ROT027/029 first gave exact uniformly inserted one-Lie average and finite Fourier divided differences. ROT033 first variable-alpha schedule. ROT034–037 restricted schedule inverse and exact source-finite local Jacobian. ROT038 first nominal six-TT finite-pool sensor selection. ROT039 FIRST legal adverse N64 case, ROT040 FIRST OPEN 6D interval-certification of its local nonrobustness. ROT041 FIRST compressed run-length exact-by-algebra source-finite insertion/Jacobian and observed nonmonotonic grid ranking. ROT042 does NOT reattribute these discoveries; it replaces the ROT041 22-grid numerical convergence observation by an analytic UNIFORM ALL-N Jacobian error certificate and an independently interval-certified continuum singular-value GAP. Mature Euler product/total variation/Weyl inequalities, NO priority/novelty.

Source: unchanged auxiliary deepseek_python_20260627_a87249.py ACTUAL SHA256 23b0ec865263c5688682425af9d4c1f9dcb9f1d582a0f2f33d99c642c176f801, true even-N real TT B=GA, flat unmasked periodic N³ symmetric tensors, source centered THREE-TERM Lie C=(0,cos x,0), stable source Ealpha=I+alpha h²Delta2. Original historical production dtc0a_runtime_v0_3_1.py BYTES UNAVAILABLE; no masked historical h=fI K_A or NCDG physics.

## Precise fixed-host theorem

The SINGLE fixed LEGAL ROT039 adverse profile: total dose A=.009, ramp velocity v=.012, beta=m/N² asymptotically .12, six known dose levels x_j=jA/5. First five strictly positive dwell durations are exact decimal rationals (.003160219022080221,.0026756342224162114,.0022914955572644483,.0027910331414697223,.04707365145084304); d5=.25-sum_first5; fixed unknown-to-inverse but actual gain t=.8123225702365454. For any even N set m=nearest_integer(.12N²) and source sampled alpha_j=N²[a(j/m)-a((j-1)/m)]∈[0,1/6]. OLD TT six sidebands H2−,H2+,H3−,H3+,H4−,H4+. NEW H0+,H1−,H1+,H2−,H3+,H4−. Their EXACT SOURCE-FINITE scalar insertion means Omega_N=(m+1)^−1 sum_ell prod_(j<=ell)(1-4alpha_j Si) prod_(j>ell)(1-4alpha_j So); Jacobian J_N=[Omega,t d_(d0..4)Omega] (six rows per set), away from time-grid kink parameter chambers.

NEW R42.1: for EVERY EVEN N>=64 at smooth parameter-chamber point,
||J_N^OLD-J_inf^OLD||_2 < 320000/N², ||J_N^NEW-J_inf^NEW||_2 < 320000/N².
The same bound applies to one-sided neighboring Jacobians and their Clarke convex hull at mesh-knot coincidences. J_inf is INDEPENDENT classical continuous schedule moment Jacobian (from ROT034–036), NOT a fitted limit.

PROOF AUDIT with conservative EXACT RATIONAL constants: for used carrier/sidebands |kx|<=5, with lambda_N(k)=4N²[sin²(pi*kx/N)+sin²(pi/N)] and Lambda=4pi²(kx²+1), elementary sin bound/π<3.142 give lambda_N<=Lambda<1027 and |lambda_N-Lambda|<82000/N². For N>=64, m>=.119N², each positive low-band Euler factor q=1-lambda_N Delta a, with Delta a<=v/m, has lambda_N Delta a<1/20. Therefore -log(1-x)-x<=x²/[2(1-1/20)] and product-to-exponential value error <=lambda_max² A v/[2m(1-1/20)]. Each dose derivative g_i(t)=∂a/∂d_i has sup <=v=.012 and TV<=10v=.12. Differentiating source finite log product yields derivative deviation <=2 lambda_max v*value_error +lambda_max² v TV/[m(1-1/20)]. Normalized m+1-point quadrature has value error <=[TV(f)+2sup|f|]/m; apply to exponential profile (TV<=2 lambda_max A), to derivative (TV<=2lambda_max[10v+2lambda_max v A]). Replacing lambda_N by Lambda adds at most A*82000/N² in value and (2*82000*v+2lambda_max*v*A*82000)/N² in derivative. Exact Fraction bounds: EVERY Omega coordinate error <1415/N², EVERY dwell derivative coordinate error <52326/N². Fixed gain t<1 and 6x6 Frobenius => each ||J_N-J_inf||_2 <6*52326/N²<320000/N². Proof is analytic for all N, not exhaustive computation of all N.

NEW R42.2: independent 95-digit experimental directed mpmath.iv interval of CONTINUUM matrix with original exact rational dwell/gain: strict interval LDL^T of J_infNEW^T J_infNEW−(1.20e−5)²I has all SIX positive lower pivots, hence sigma_min(J_infNEW)>1.20e−5. An explicit declared rational right vector gives interval Rayleigh quotient for OLD <=9.20956e−13 <(1.10e−6)², hence sigma_min(J_infOLD)<1.10e−6. Continuum gap >1.09e−5. For EVERY EVEN N>=300000, 2*320000/N² <=7.11112e−6 <1.09e−5; Weyl inequality yields STRICT sigma_min(J_NNEW)>sigma_min(J_NOLD). Also holds for each choice of one-sided/Clarke generalized Jacobian at a kink, but classical differentiability itself is not asserted there. N0=300000 is CONSERVATIVE, not minimal. Interval backend experimental, not formal proof assistant, independent referee pending.

NEW R42.3 NONSMOOTH GRID-KNOT GUARD: because all source dwell times are exact rational decimals and each ramp length is exactly 3/20, LCM of rational time-knot denominators is L0=10^19. Thus for every k>=1, even N=10*L0*k, m=12*L0²*k², EVERY source ramp/plateau knot is exactly on a discrete mesh time sample. The sampled cumulative-dose function has distinct one-sided derivatives there; a classical time-sampling Jacobian cannot be assumed without checking possible output cancellation. R42.1 controls all branchwise derivative limits (Clarke convex hull), not a fabricated unconditional C1 assertion for these exceptional N.

EXECUTED 5 paths: (1) 15 Fraction checks of analytic upper constants; (2) 8 independent 95-digit interval LDL/Rayleigh; (3) 64 exact Fraction knot resonance and legal geometry checks; (4) 59 independently implemented Fraction-source-knot run-length blocks vs ORIGINAL full O(m) product/derivative at N<=1024 plus N300000 (m=10.8 billion) and N1000000 (m=120 billion), 21 blocks each, source finite J ratios NEW/OLD 13.005660 and 13.005657 numeric; (5) 30/30 explicitly REPLAYED ROT041 UNCHANGED literal helper source FULL real 3D N12/16 apply_E/P_TT/three-term Lie (max modal error 2.319e−16). TOTAL 176/176 typed PASS, of which 30 are old reproducibility controls, not new independent experiments. NO full physical N³ computation for huge N; mathematical symbol proof only.

Local Moderator ZIP complete Polish proof (~12KB), original four new scripts, one retained source-native test, two helpers, one legal ROT039 witness JSON, five original JSON/five stdout, unchanged frozen helper, README and SHA manifest: CRC PASS, SHA256 21/21, FIVE clean reruns reproduce FIVE JSON BYTE IDENTICAL. ZIP SHA256 471b511b34d8716bc1d027b7f23572302972ac56285e6c71f92198d561c19531. Code/ZIP LOCAL to user conversation, NOT separately hosted on GitHub.

Claim ceiling strictly this FIXED synthetic legal source host, no all-schedule robustness, no global inverse, no original production/masked h=fI K_A, no physical J3/K/GR/GW/PBH, independent referee, BW, canon or EXEC. NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
