---
artifact_id: GEEKY-S11-ROT049-POLYNOMIAL-CHANNEL-GAIN-DRIFT-IDENTIFIABILITY-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-11-11
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
class: RESTRICTED_POLYNOMIAL_GAIN_DRIFT_EXACT_IDENTIFIABILITY_THRESHOLD_AND_FINITE_SOURCE_NOISE_GATE
status: 1084_TYPED_CHECKS_PASS / CLEAN_REPLAY_PASS / EXTERNAL_REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# ROT049 — Exact q+1-reference identifiability of polynomial six-channel gain drift; Lebesgue-noise guard

## Scientific lineage; no new-math claim

Geeky ROT015–017: genuine compatible even-grid real TT B=GA versus defective raw-realcast TT. ROT027/029: exact uniform one-Lie insertion and finite Fourier kernels. ROT033: nonstationary stable filter sequences. ROT034: arbitrary-schedule inverse noninjectivity. ROT037: exact source finite six-TT restricted local inverse. ROT038–040: nominal sensor design and interval-certified nonrobustness. ROT041: exact run-length compression. ROT042/043: all-large-N bounds and nonsmooth kinks. ROT044 FIRST global bi-Lipschitz restricted six-level finite source map given known six-channel relative gains, lower constant c=1.2e−5 at every even N>=200000. ROT045: six-channel unknown relative gain gauge, stationary reference, and serious float-knot Jacobian defect. ROT046: TWO bracketing references cannot identify unrestricted drift, sharp conditional curvature bound. ROT047: K-ref spacing/noise limits and C² blind spot. ROT048: known-target bracketing and no finite deterministic adaptive certificate of unrestricted smooth drift curvature. ROT049 does NOT reassign past findings. New narrowly scoped mathematical host is finite-dimensional POLYNOMIAL relative log-channel gain drift of KNOWN maximum degree q. Classical polynomial interpolation, not a claimed novel theorem.

Prior art: Berrut and Trefethen, Barycentric Lagrange Interpolation, SIAM Review 46(3), 501–517 (2004), DOI 10.1137/S0036144502417715; Higham, The numerical stability of barycentric Lagrange interpolation, IMA Journal of Numerical Analysis 24(4), 547–556 (2004), DOI 10.1093/imanum/24.4.547. Their standard barycentric and Lebesgue conditioning analyses underlie our terminology and nullspace arguments.

## Source / model boundary

Frozen unchanged auxiliary deepseek_python_20260627_a87249.py BYTE SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. Historic production dtc0a_runtime_v0_3_1.py bytes NOT available. Host: flat unmasked periodic even N³ real symmetric TT with true B=GA, full THREE-TERM centered Lie C=(0,cos x,0), source scalar Ealpha=I+alpha h² Delta2. Six scalar sidebands H0+,H1−,H1+,H2−,H3+,H4−, known six dose levels xj=j*.009/5 and five ramp velocity .012; six positive plateau lengths d_j total .25 and common unknown gain t. z=(t,t d0,...,t d4) in open convex restricted cone C. ROT044 says ||F_N(z)−F_N(z')||2 > c ||z−z'||2, c=1.2e−5, for ALL even N>=200000, GIVEN known relative gain normalization. Not original historic masked h=fI K_A, GR/GW/PBH/NCDG J3/K physics.

## R49.1 Exactly K=q+1 reference times identify degree≤q relative log gains

Let six positive unknown relative gains g_i(s)=exp(ell_i(s)), normalized SUM_i ell_i(s)=0. Assume as EXTERNAL model condition EACH ell_i(s) is exactly a polynomial of degree ≤q, q known. Reference j at distinct known time s_j has known six-level dwell profile d_ref,j and UNKNOWN separate positive absolute gain t_ref,j:
Y_ij=t_ref,j Omega_N,i(d_ref,j) exp(ell_i(s_j)).
All Omega reference sidebands positive in considered source host. Form R_ij=log(Y_ij/Omega_N,i(d_ref,j)); center each reference across six channels:
E_ij=R_ij−(1/6)SUM_k R_kj=ell_i(s_j),
which eliminates even independently varying t_ref,j.

If K=q+1 distinct nodes, unique Lagrange interpolation
ell_i(tau)=SUM_j L_j(tau) E_ij,
L_j(tau)=PROD_(k≠j)(tau−s_k)/(s_j−s_k).
A nonzero polynomial of degree ≤q cannot vanish at q+1 distinct nodes. Hence all relative channel gains at the target are uniquely recovered exactly under the class model; source target can then be globally uniquely inverted by ROT044 for even N>=200000. For q=0, one stationary reference as ROT045.

SHARP NECESSITY at K≤q and target tau NOT among references: P(s)=a PROD_(j=1)^K(s−s_j) is degree K≤q, zero at ALL K references and nonzero at tau. ell(s)=(P(s),−P(s),0,0,0,0) is centered, gives positive gains and can be arbitrarily small. As F_N(C) is OPEN (continuous injective map of an open subset of R6, from ROT044), for sufficiently small a there exists a different legal z' exactly satisfying F_N(z')=diag(exp(ell(tau)))F_N(z). The stationary-gain alternative (z',ell=0) gives exactly the same K reference observations and the same target six-data. Numerical residuals only demonstrate, not prove, algebraic/topological equality. Thus K=q+1 is MINIMAL for structural identification across unobserved target times under this polynomial class.

## R49.2 Sharp pointwise log-calibration amplification by Lebesgue function

Define lambda_q(tau)=SUM_j |L_j(tau)|. If each raw relative reference measurement error |delta_ij|<=eps_ref<1, log errors lie in [L,U]=[log(1−eps_ref),log(1+eps_ref)]. Six-channel centering has sharp single-coordinate error E=(5/6)(U−L) (prior ROT047). Interpolation yields
max_i |ellhat_i(tau)−ell_i(tau)| <= eta=lambda_q(tau)*(5/6)*log[(1+eps_ref)/(1−eps_ref)].
This is SHARP for a chosen channel, with admissible per-reference noise signs matching each Lagrange coefficient. This need not be simultaneously saturated by all six channels.

With target relative error |delta_target_i|<=eps_target, corrected relative data mismatch q_noise=(1+eps_target)*exp(eta)−1. If true z and reconstructed zhat belong to the legal restricted cone, corrected source residual r and ||F_N(z)||<=B imply
||zhat−z||₂ <= [r+q_noise*B]/(1.2e−5),
for all even N>=200000 as a conditional consequence of ROT044. No real gain noise/B estimate; no unbounded-gain-uniform dwell d reconstruction as t→0.

CONCRETE q=12, K=13, target tau=4879/5000=0.9758: two SPECIFIC node layouts, j0..12:
(a) equidistant s_j=j/12, lambda=89.324209191805;
(b) Chebyshev–Lobatto s_j=[1−cos(j pi/12)]/2, lambda=1.520626597533.
Pointwise worst-case amplification factor differs by approximately 58.74. Independent 110-digit direct Lagrange and separate barycentric float64 agree. No claim that these nodes are globally optimal among all placements, noise laws or target times; 101-point grid inspections are NOT global interval certificates.

SOURCE FINITE at N200000/300000/1000000, exact Fraction time knots and independently corrected fraction Jacobian (not ROT041 float-knot), synthetic six relative log polynomials of exact degree ≤12, independently unknown absolute reference gains, target actual t=1.07. Both 13-ref schemes recover noiseless target z with error <2e−8. Under separate worst-sign relative reference noise |delta|=1e−12, at N300000:
equidistant ||zhat−z||=2.31288254e−6, conditional bound=1.24630107e−5;
Chebyshev–Lobatto error=3.93735761e−8, conditional bound=2.12204120e−7.
These are different sign arrangements adapted to the two layouts but identical worst-case per-reading noise budget; no actual instrument data or all-noise averages.

## R49.3 Extra reference detects some model mismatch, never certifies assumed class

If K=q+1 reference readings fit degree≤q, a further known-profile reference at a distinct time can REFUTE the degree bound if discrepancy exceeds allowed uncertainty. For example out-of-class degree q+1 P(s)=a PROD_(j=0)^q(s−s_j) hides at all first K but not at the additional heldout sample. Conversely a degree q+2 polynomial may vanish even at all K+1 samples and differ at some other target. Likewise smooth C-infinity hidden drifts from ROT048. Finitely many perfect references cannot prove an unrestricted physical gain history is polynomial. The proof of recoverability is strictly conditional on externally justified finite-dimensional class, not certification of that class from those same references.

## Executed falsification / custody

(1) rot049_exact_degree_threshold.py: 183 stdlib Fraction typed checks, monomials/centered six-channel polynomial nullspace and sharp six-channel noise expression.
(2) rot049_highprecision_lebesgue.py: 237 independent 110-digit mpmath direct Lagrange, worst-sign noise and finite grid-scan checks (NOT certified global maxima).
(3) rot049_source_finite_poly_calibration.py: 133 direct source finite inverse/ref calibration tests over N200k/300k/1m, q12, both node schemes, independently varying unknown absolute ref gains; exact rational source temporal knots.
(4) rot049_degree_insufficient_source_falsifier.py: 418 exact rational polynomial nullspace checks at q=3,6,12 and alternative legal source finite schedule pairs producing identical references and targets to numerical tolerance; exact existence via open image.
(5) rot049_heldout_degree_falsification.py: 84 exact Fraction tests of heldout detection vs more hidden degree.
(6) rot044_literal_aux_source_gain.py: 29 RETAINED/REPLAYED literal frozen original helper full 3D real N12/16 B/E/THREE-term Lie checks; not new experiment, max spectral discrepancy ~2.69644e−16.
TOTAL 1084/1084 actually executed assertions, including 29 inherited controls and many repetitive exact arithmetics, NOT 1084 independent science experiments.

Complete user-conversation LOCAL ZIP GEEKY_S11_ROT049_POLYNOMIAL_GAIN_DRIFT_INTERPOLATION_REPRO_001.zip, SHA256 dc1bd7b1c4bc9c11c44df7adba0d2cb7ad71cb90d1ab09d80c80376643b71d66. Includes full 13KB Polish theorem/proof, five new and one retained executable scripts, dependency helper cores, frozen original source, six JSON results and six stdout logs, README and SHA manifest. CLEAN ZIP CRC PASS, payload SHA256 25/25, ALL SIX independently rerun in clean extraction and ALL SIX JSON AND STDOUT BYTE IDENTICAL PASS. Local ZIP/scripts NOT individually hosted on GitHub.

NO original historic masked K_A, NCDG J3/K/GR/GW/PBH, independent referee/BW/owner adoption, CANON/EXEC, nor math priority. NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
