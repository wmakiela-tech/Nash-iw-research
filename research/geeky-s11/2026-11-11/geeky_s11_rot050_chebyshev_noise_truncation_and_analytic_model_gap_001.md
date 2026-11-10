---
artifact_id: GEEKY-S11-ROT050-CHEBYSHEV-NOISE-TRUNCATION-ANALYTIC-MODEL-GAP-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-11-11
exposure: PUBLIC
status: NUMERICALLY_REPRODUCED_CLASSICAL_INTERPOLATION_AND_EXACT_ANALYTIC_MODEL_NONIDENTIFIABILITY / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
full_local_report_sha256: 2ad0b614bda6a1a251901a723d85b5fa3bfeb914025827809d5228d6222a5888
---

# ROT050 — Two separate reference-placement objectives and analytic finite-validation blind spot

## Prior first
Geeky ROT015–017 even-grid source-compatible real TT projector B=GA. ROT027/029 averaged complete three-term Lie placement. ROT033 variable stable Ealpha. ROT034 arbitrary schedule inverse NONIDENTIFIABILITY. ROT037–038 six-level restricted six TT probe inverse/nominal sensor selection. ROT039–040 source legal negative N64 schedule and open-box interval certificate. ROT041 source-finite run-length Fourier identity. ROT042–043 all-large-N and Clarke kink guards. ROT044 global restricted-cone source-finite six-channel inversion for even N>=200000, known relative gains, inverse lower constant c=1.2e-5 (still REFEREE_PENDING). ROT045 blind sensor gains, reference correction, severe float time-knot derivative fault. ROT046–048 changing gains, sharp C2 drift interpolation, K-reference spacing, and impossibility of certifying derivative/curvature globally from finitely many adaptive samples. ROT049 **first of current paired rotations**: exact polynomial log-gain degree<=p gives K=p+1 known references necessary/sufficient for an unsampled target, with Lebesgue noise amplification. ROT050 does NOT reattribute ROT049.

New delta here: compare TWO different interpolation error objectives, and demonstrate that even globally analytic gain drift can agree with ANY FINITE set of known-profile references (including heldout) without satisfying alleged low-degree class. Standard Chebyshev monic minimax/Lagrange remainder/Lebesgue operator mathematics; no priority or novelty.

## Host and the separate noise and truncation bounds
Source is UNCHANGED retained auxiliary `deepseek_python_20260627_a87249.py`, byte SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`; historical original production `dtc0a_runtime_v0_3_1.py` unavailable. Full unmasked even periodic 3D symmetric real TT host, true projector B=GA, original complete THREE-term Lie C=(0,cos x,0), stable scalar Ealpha. Six normalized nonzero Fourier sidebands H0+, H1-, H1+, H2-, H3+, H4-. Source finite insertion mean Ω from all filter positions, fixed six known dose levels/ramp slope, six unknown positive dwell durations summing .25, unknown target common gain. z=(t,t d0,...,t d4) in original ROT044 open convex cone C.

Known-profile references each may have their OWN unknown absolute amplitude. Center the six logarithms of Y_ref/Ω_ref to remove it. Six normalized relative channel gains satisfy sum_i ell_i(s)=0. With K distinct reference times s_j and interpolation weights L_j(t), define pointwise Lebesgue amplification Lambda(t)=sum_j |L_j(t)|.

If each true ell_i is EXACT polynomial degree <=K-1, relative reference channel errors |e_ij|<=eps_ref<1 imply, for each channel,
 |ellhat_i(t)-ell_i(t)| <= Lambda(t)*(5/6)*log[(1+eps_ref)/(1-eps_ref)].
The coefficient 5/6 is the sharp centering of six unequal logarithmic measurement errors, and Lambda is the sharp worst-case interpolation amplification for one channel. Not a simultaneous six-channel attaining construction.

If the unknown drift is instead C^K and has an INDEPENDENTLY JUSTIFIED global high-derivative bound sup |ell_i^(K)|<=M, the classical Lagrange remainder is:
 |ellhat_i(t)-ell_i(t)| <= M/K! * abs(prod_j(t-s_j)) + Lambda(t)*(5/6)*log[(1+eps_ref)/(1-eps_ref)].
The PRODUCT term and LEBESGUE term are different objectives; cannot call one set of nodes universally optimal for both.

For even N>=200000, source-cone-legal z,zhat, independent bound ||F_N(z)||<=B, target relative noise eps_t, corrected residual r, with eta the previous RHS and Q=(1+eps_t)*exp(eta)-1:
 ||zhat-z||_2 <= (r + B Q)/(1.2e-5).
Only conditional use of ROT044, no empirical H/M/eps/B or global Newton basin, and d_i=z_i/t loses gain-uniform stability as t approaches zero.

## R50.1 exact classical minimax polynomial
For K=9 distinct sample nodes on [0,1] and omega_9(t)=prod_j(t-s_j), all such polynomials are MONIC. The degree-9 rescaled Chebyshev T9(2t-1) has leading coefficient 2^(2K-1), so
  min_nodes max_(t in [0,1]) |omega_9(t)| = 2^(1-2K)=2^-17=0.00000762939453125.
Achieved by NINE ROOTS t_j=(1-cos((2j+1)pi/(2K)))/2, j=0,...,K-1. Alternation at K+1 extrema proves minmax; elementary classical approximation theorem, not source physics. Endpoint reference measurements NOT required here.

Independent 85-digit implementation checks polynomial f(t)=M*t^9/9!, for which interpolation remainder equals (M/9!)*omega_9(t) IDENTICALLY and all ten alternating extrema have exactly 2^-17 magnitude in high precision.

## R50.2 different empirical noise winner
THREE DECLARED 9-node designs, target t=.0415, 70-digit mpmath Lagrange:
 DESIGN | POINTWISE Lambda_8(.0415) | grid-sampled max Lambda (1001 samples, NOT rigorous exact sup) | grid-sampled max |omega_9|
 EQUISPACED | 10.94561610 | 10.94500546 | 3.6722244e-5
 CHEB_LOBATTO (endpoints present) | 1.12889370 | 2.27472770 | 1.4970144e-5
 CHEB_ROOTS (no endpoints) | 1.84559979 | 2.36185679 | 7.62939453125e-6, also EXACT minimax.
Here CHEB_LOBATTO gives ~9.7x less adversarial reference-noise amplification than EQUISPACED for this ONE target, and less than CHEB_ROOTS. The CHEB_ROOTS design minimizes worst-case TRUNCATION product for declared bounded ninth derivative. Neither establishes CHEB_LOBATTO global minimal Lebesgue constant over all possible node sets. Empirical sampled sup not an interval certificate.

SAME legal source-FINITE six-TT Fourier map, independent correct rational time-partitioned Jacobian (NOT legacy FLOAT-KNOT derivatives), N200000,300000,1000000, synthetic reference errors eps_ref=2e-12 with per-design signs chosen to align with Lagrange weights, each reference having different unknown absolute amplitude. At N300000:
 EQ: target channel0 centered log error 3.64840129e-11, reconstructed z error 5.66766454e-7;
 LOB: 3.76282599e-12, z error 5.84467820e-8;
 ROOT: 6.15185333e-12, z error 9.55612550e-8.
These are DIFFERENT synthetic noise realizations per node scheme, not one instrument experiment. All noiseless calibrations of polynomial drift recovered at near machine precision.

## R50.3 exact finite-sample model validation impossibility EVEN IN ANALYTIC CLASS
For ANY finite distinct calibration and heldout times S={s1,..,sK} with target t not in S, choose
   P(u)=a*prod_(j=1)^K(u-s_j).
This is ENTIRE ANALYTIC and exactly zero on ALL samples, but P(t)≠0 for any nonzero a. Relative gain drift ell=(P,-P,0,0,0,0) keeps sum ell_i=0. An alternative admissible target z' exists for sufficiently small a by ROT044's open image F_N(C); two different schedule-and-drift pairs produce EXACTLY identical ALL calibration references and target observations. Numerical exact-source six-TT demonstration with K=9 and target log relative shift 2e-9 gives ||z'-z||≈5.179852e-5 and output mismatch <2e-14 at N200k/300k/1m. Existence is algebraic/topological, not proved by the floating residual.

A nonzero HELDOUT discrepancy can reject declared polynomial degree p (when external model/measurement error budgets justify rejection). Zero heldout residual, even across many additional distinct times, CANNOT prove degree p or a global bound M; increase polynomial degree to accommodate those roots. Analyticity ALONE is insufficient. This is a strong model-class guard, not a theorem against independently known finite-degree physical calibration laws.

## Actual checks and custody
Five executable paths: 3016 high precision sample-Lebesgue/Chebyshev alternation, 902 exact stdlib Fraction finite analytic zero polynomial/heldout controls, 1513 independent mpmath85 sharp interpolation remainder, 168 exact SOURCE-FINITE Fraction-time six-TT forward/noise/inverse analytic hidden polynomial checks on 3 huge N, 29 RETAINED original auxiliary literal full 3D TT/E/THREE-term Lie small-grid N12/16 controls. Total 5628/5628 actually executed typed assertions PASS (many mathematical grid tests, not independent scientific experiments). Initial prefinal development exceptions corrected before PASS. Full LOCAL Polish report SHA256 `2ad0b614bda6a1a251901a723d85b5fa3bfeb914025827809d5228d6222a5888`.

LOCAL conversation ZIP `GEEKY_S11_ROT050_CHEBYSHEV_NOISE_ANALYTIC_MODEL_GAP_REPRO_001.zip` SHA256 `73eaed2fc03e4fca1f0b3a3480212abfc895a10447fd433797132c3705de68a3`. It contains FULL ~14KB Polish report, 5 executable scripts + 5 JSON + 5 stdout, original unchanged auxiliary source, dependencies, README, manifest. Clean ZIP CRC PASS, SHA256 21/21, FIVE reruns in clean extraction, FIVE JSON and stdout BYTE IDENTICAL. This GitHub science note is a condensed source-grounded index, not a claim the local ZIP/code have been uploaded to GitHub separately.

NO historic masked h=fI/K_A, original production runtime, NCDG physical K/J3/GR/GW/PBH, apparatus noise/real derivative bound, mathematical novelty, independent referee/BW/owner canon or EXEC. NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
