---
artifact_id: GEEKY-S11-ROT041-EXACT-RUNLENGTH-TT-SCHEDULE-GRID-PHASE-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-11-02
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_ALGEBRAIC_BLOCK_IDENTITY / SOURCE_TYPED_NUMERICAL_VALIDATION_127276_PASS / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# ROT041 — exact run-length source-finite TT insertion mean, grid-phase reversal of probe ranking

## Science lineage and custody

ROT015–017 first source even-grid realcast raw-k TT pathology and genuine compatible orthogonal B=GA; ROT027 first uniform one-Lie insertion; ROT029 exact divided differences for one E; ROT033 variable-alpha exact insertion; ROT034–037 variable schedule inverse and local source-finite six-sensor Jacobian; ROT038 first nominal 25-pool six-sensor optimum; ROT039 FIRST legal N64 adverse schedule producing nominal probe NONROBUSTNESS; ROT040 FIRST rigorous directed interval six-dimensional open neighborhood for that adverse case. ROT041 DOES NOT take ownership of that witness or interval result. It evaluates the SAME exact finite source schedule with a new block algorithm and distinguishes finite-grid failure from large-grid limit. All relevant geometry is classical Fourier analysis/finite geometric sums and differentiation, NO claim of mathematical novelty.

Source: unchanged retained AUXILIARY deepseek_python_20260627_a87249.py; actual BYTE-verified SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. Historic production dtc0a_runtime_v0_3_1.py UNAVAILABLE. Full unmasked periodic even N³ symmetric TT, source centered 3-term Lie C=(0,cos x,0), strict compatible B=GA, scalar source Ealpha=I+alpha h²Delta2. Only low-band q_in,q_out>0 in this algorithm, NOT a high-band negative-E black-box solver, historic masked h=fI K_A or physics.

## R41.1 — exact run-length block identity, including analytic Jacobian

Same restricted ramp/plateau model ROT037–040: six known cumulative dose levels x_j=j*.009/5, five ramp speeds v=.012, six positive plateau durations sum .25, unknown common gain t. m=round(.12N²), source legal alpha_j=N²[a_d(j/m)-a_d((j-1)/m)] in [0,1/6].

For each TT sideband (p,s), set Si=sin²(pi p/N)+sin²(pi/N), So=sin²(pi(p+s)/N)+sin²(pi/N). Define qi,j=1−4alpha_j Si, qo,j=1−4alpha_j So, r_j=qi,j/qo,j. Original exact source-finite uniformly averaged one-Lie insertion:
Omega=(m+1)^−1 SUM_(ell=0)^m PROD_(j<=ell)qi,j PROD_(j>ell)qo,j
= [PROD_(j=1)^m qo,j]/(m+1) [1+SUM_(ell=1)^m PROD_(j=1)^ell r_j].
For any consecutive run L with identical alpha (so identical r,qo), define G_L(r)=SUM_(k=1)^L r^k (standard geometric sum, G_L(1)=L). If accumulated prior ratio R, partial sum S, out product Q, exact updates:
 S'=S+R G_L(r), R'=R*r^L, Q'=Q*qo^L.
For the specified piecewise-linear accumulated-dose family, all temporal cells completely INSIDE a plateau or ramp have alpha=0 or alpha=N²*v/m, respectively, hence ZERO derivative w.r.t plateau durations in the fixed knot chamber. At time-grid cells intersecting ramp boundaries, alpha and its exact five first partials come from source-sampled dose. For such one-step blocks:
 dlog r=−4(Si−So)/(qi qo)*dalpha,
 dlog Q=−4 So/qo*dalpha,
 dR' = r*dR+R*r*dlog r,
 dS'=dS+dR'.
Ultimately dOmega=Q/(m+1)[dS+S*dlogQ], source Jacobian J=[Omega,t*dOmega/dd0..4].
This is an ALGEBRAIC identity (not a numerical quadrature). Implementation uses log1p/expm1/powers to reduce cancellation. It is floating point, NOT bit-exact or constant bit complexity. Complexity O(number_of_runs * number_of_readouts * 5) instead of O(m * number_of_readouts * 5), when the number of ramps/plateaux is fixed. In witness profile observed 19–22 runs across N64..16384; N16384 means m=32,212,255 source filters, without iterating over all positions.

## R41.2 — confirmed nonmonotonic finite-grid ranking of ONE fixed legal ROT039/040 witness

OLD six TT: H2-,H2+,H3-,H3+,H4-,H4+.
NEW six TT: H0+,H1-,H1+,H2-,H3+,H4-.

EXACT finite mathematical mapping evaluated by block algorithm; numerical SVD of its exact-source Jacobian:

N=56 m376 NEW/OLD sigma_min ratio 28.20 (NEW wins);
N=64 m492 ratio .09017 (OLD wins, ROT040 interval certificate already established);
N=72 m622 ratio 9.03 (NEW wins);
N=128 m1966 ratio 7.88;
N=512 m31457 ratio 12.72;
N=1024 m125829 ratio 12.94;
N=2048 m503316 ratio 13.00;
N=4096 m2013266 ratio 13.01;
N=16384 m32212255 ratio 13.01.
This is not an all-N monotonicity theorem; NEW remains NOT globally parameter-robust, as ROT040 proved. Both the plateau durations AND gain are fixed across this N scan; the sampled ramp/cell phase and source finite Fourier symbols change with N.

## R41.3 independent continuum Jacobian and source-finite residual gate

The same fixed low-band schedule has the classical ROT034–036 continuum affine moment limit Omega_inf=exp(−4pi² Kout A)[(expm1(lambda A)/(lambda v))+SUM_(j=0)^5 d_j exp(lambda x_j)] where lambda=4pi²(Kout−Kin). J_inf=[Omega_inf | gain*W] with W_ij=exp(−4pi² Kout_i A)[exp(lambda_i x_j)−exp(lambda_i x5)] (j0..4). For the same ROT039 adverse profile, sigma_min(J_infOLD)=9.596640619e−7, sigma_min(J_infNEW)=1.248106181e−5, gap=1.152139775e−5.

At EACH assessed N, Weyl gives sufficient condition: deltaOLD_N+deltaNEW_N<gap, where delta=||J_N−J_inf||2, implying sigma_minNEW_N>sigma_minOLD_N. The NUMERICALLY COMPUTED residual sum first satisfies this inequality at N2048 among 22 tested sizes, with sum/gap≈.8995; N4096 ≈.1105 and N16384≈.0076. These are float64 a posteriori diagnostics, NOT independently interval-certified residuals and NOT a theorem that every N>=2048 is ordered. At N64 the absolute J_N−J_inf distances (~.0033 and .0030) are orders above the singular gap. This supports the source finite-grid sampling explanation, NOT a precise physical resonance.

## Independent actually executed controls and clean replay

(A) 50 source legal profiles/configurations including independent random d: compare block Jacobian to ORIGINAL ROT039 explicit source finite product-and-derivative loops, N12..1024 and 12 channels: 289 typed PASS, max absolute J difference 9.77995e−13.
(B) independent stdlib Fraction exact rational schedule piece intersections: 42,264 temporal cells on eight N, 126808 typed PASS, max alpha floating difference 2.70437e−13, algebraic derivatives EXACT rational; NOT exact sine values.
(C) literal UNCHANGED AUXILIARY original full real 3D source apply_P_TT, three-term Lie and apply_E at ALL m+1 positions for N12/16 TT p=0/1/2: 30 typed PASS, max Fourier relative diff 2.31880e−16. NOT full native N64 m492.
(D) independent analytic continuum Jacobian and 22-grid source finite comparisons N24..16384: 149 typed PASS. Total **127276/127276** typed PASS; overwhelming majority are Fraction geometry cell checks, not separate physical experiments.

Single user/Moderator LOCAL ZIP contains expanded Polish report, 4 runnable tests, two helper source implementations, FOUR JSON, FOUR logs, ROT039 witness JSON, unmodified original auxiliary, README and manifest. ZIP SHA256 8c202406fe7774a7d86e30618f3eb2e82f4a8f19cbad9b618739a3da4388d622. Zip CRC PASS, content SHA256 18/18, clean unpack and ALL FOUR independent reruns produce FOUR JSON byte-for-byte identical. Local ZIP/source NOT separately published on GitHub.

IMPORTANT CUSTODY: initial ROT041 development script transposed two digits in pasted auxiliary source checksum and failed its CHECK, then was FIXED before PASS. Direct filesystem checksum and prior ROT039/ROT040 science reports, including pinned ROT040 GitHub note, agree with the correct above source hash. No evidence of corrupt ROT039/040 report/source, no changing frozen auxiliary bytes. All-N source geometry/historic production/bw referee beyond scope.

NO historical masked K_A, original production DTC, source h=fI, NCDG physical J3/K/GR/GW/PBH, independent referee, BW/owner adoption, canon or EXEC. NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
