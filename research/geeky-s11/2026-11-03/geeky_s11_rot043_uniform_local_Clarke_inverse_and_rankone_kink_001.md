---
artifact_id: GEEKY-S11-ROT043-UNIFORM-LOCAL-CLARKE-INVERSE-RANKONE-KINK-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-11-03
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
class: SOURCE_FINITE_ALL_LARGE_EVEN_N_QUANTITATIVE_LOCAL_BILIPSCHITZ_PLUS_ACTUAL_SINGLE_KINK_RANK_ONE
status: ANALYTICAL_PROOF_AND_121_EXECUTED_TYPED_CHECKS_PASS / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# ROT043 — uniform local six-TT inverse even at temporal kink nodes; actual rank-one kink falsifier

## OWN SCIENCE FIRST and classical foundations

ROT015–017: source even raw Fourier TT realcast projection defect and true B=GA. ROT027/029: averaged one-Lie insertion and divided differences. ROT033: variable stable E schedule. ROT034: arbitrary schedule nonidentifiability. ROT035–037: limited six-level six-TT inverse, exact finite grid local inverse. ROT038: nominal six-sensor fixed pool choice. ROT039–040: legal N64 opposite-ranking witness, subsequently interval-certified. ROT041: exact run-length source-finite evaluation and grid-phase reversals. ROT042 **FIRST** uniform all-N Jacobian bound C/N² and continuum singular gap, preserving kink-node exceptions. ROT043 does NOT reclaim previous discoveries. NEW: quantitative BILIPSCHITZ inequality over explicitly defined SIX-DIMENSIONAL PARAMETER BALL for ALL even N>=300000 INCLUDING kink crossings, and explicit genuine nonzero rank-one Jacobian kink at an independently selected finite grid.

Classical theorem: F. H. Clarke, On the Inverse Function Theorem, Pacific J. Math 64(1) (1976); F. Behr and G. Dolzmann, A Note on Clarke's Generalized Jacobian for the Inverse of Bi-Lipschitz Maps, JOTA 200 (2024), DOI 10.1007/s10957-023-02333-x. Mathematics is classical; no novelty claim.

**SOURCE** UNCHANGED frozen AUXILIARY deepseek_python_20260627_a87249.py, byte SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. Original historical production dtc0a_runtime_v0_3_1.py unavailable. Full unmasked even periodic flat symmetric 3D source tensors, original centered 3-term Lie C=(0,cos x,0), strict real TT B=GA, Ealpha=I+alpha h²Delta2. Not historical masked puretrace h=fI/K_A or physical NCDG.

## R43.1 exact bounded local inverse theorem

Source schedule: six KNOWN cumulative-dose levels x_j=j*.009/5, five ramp slopes v=.012, total ramp time .75; six positive plateau durations d_j sum .25, common gain t>0 UNKNOWN. Six readouts NEW ROT038 (H0+,H1−,H1+,H2−,H3+,H4−) have exact **FINITE** source Fourier one-Lie average Omega_N=(m+1)^-1 SUM_ell [PROD_(j<=ell)(1−4alpha_j S_in)][PROD_(j>ell)(1−4alpha_j S_out)] with m=round(.12N²) and alpha_j=N²[a(j/m)−a((j−1)/m)]. F_N(theta)=t*Omega_N, theta=(t,d0,...,d4), d5=.25−sum d0..4.

Center theta0: t=.8123225702365454, d0..4=(.003160219022080221,.0026756342224162114,.0022914955572644483,.0027910331414697223,.04707365145084304), exact complement d5. The OPEN Euclidean parameter ball B_rho(theta0), rho=1e−6, is entirely legal: positive d_j, gain in (0,1), all source alpha_j<1/6.

**THEOREM:** For EVERY EVEN N>=300000 and EVERY theta,eta in B_rho(theta0), 
||F_N(theta)−F_N(eta)||2 >= (7.6e−6)*||theta−eta||2.
Thus F_N is injective on the entire ball; its inverse on the image is Lipschitz with factor <=131578.948. This is a 2-POINT guarantee, stronger than a mere nonsingular Jacobian at center. Remains valid on line segments crossing any temporal mesh-knot kinks; source map is locally Lipschitz/piecewise smooth, not incorrectly C1 at all grid nodes.

**PROOF:** The R42 analytic C=320000 operator Jacobian error proof depends only on fixed A,v,beta, source bounded Fourier modes |kx|<=5, the UNIFORM inequalities |da/dd_i|<=v, TV(da/dd_i)<=10v and t<1, NOT the specific six positive d_j, so its same bound extends to all parameters in the ball, all smooth time chambers and all one-sided/Clarke Jacobians:
||J_N(theta)−J_infty(theta)||2 <320000/N².
The exact continuum map is F_infty(t,d)=t(b+W d), with constant 6x5 W; J_infty=[b+Wd | tW]. Consequently
||J_infty(theta)−J_infty(theta0)||2 <=||W||F*||theta−theta0||2.
Separate direct 100-digit experimental mpmath.iv interval computations prove ||W||F² is enclosed around 0.6603558176165688, hence ||W||F<.82, AND strict interval LDLT shows all 6 pivots of J_infty(theta0)^T J_infty(theta0)−(1.20e−5)² I positive; sigma_min J_infty(theta0)>1.20e−5. Therefore on entire ball and all even N>=300000:
||J_N(theta)−J_infty(theta0)||2 <320000/(300000²)+.82e−6=4.375556e−6.
Integrate the derivative along the segment connecting theta to eta (a.e., including kink crossings) and compare with FIXED invertible J_infty(theta0):
||F_N(theta)−F_N(eta)|| >= (1.20e−5−4.375556e−6)||theta−eta|| >7.6e−6||theta−eta||.
Direct argument gives bi-Lipschitz and confirms Clarke theorem assumptions for every generalized Jacobian. The inverse coefficient applies ONLY when both candidate parameter points are IN THE BALL; it is not a guarantee noisy unconstrained optimization stays there. At the ball scale c*rho=7.6e−12 in these synthetic normalized Omega units, and no measured noise is claimed.

## R43.2 genuinely nonsmooth source-finite TT output; rank-one jump law

Independently choose LEGAL N=32, m=123, first five plateau durations (5/123,.0207,.0309,.0404,.0503), sixth positive exact complement; gain=.8123225702365454. The ONLY internal time-knot grid coincidence is first plateau end u5=5/123. ALL alpha source filters in [0,.099903]. At that node the derivative of cumulative dose with respect to d0 jumps between 0 and −v. For any single sampled time knot u_j, source alpha_j=N²(a_j−a_(j−1)), alpha_(j+1)=N²(a_(j+1)−a_j). Therefore the exact SIX-READOUT Jacobian jump equals
Delta J=[0 | t*N²*(D_alpha_j Omega−D_alpha_(j+1)Omega) OUTER Delta g ],
where Delta g is the 5-vector of jump of derivatives of a(u_j). For a single knot, rank Delta J<=1, potentially zero. Here direct independent O(m) Fourier product derivatives give an explicitly NONZERO jump in the first plateau column:
(-.00250541784, -.00115645702, -.00366212210, -.00576311155, -.00185702413, -.00357242432);
norm ||Delta J||F=.00839344139757, rank EXACTLY 1. Three one-sided finite difference steps 1e−5/1e−6/1e−7 have jump discrepancies 1.08e−4/1.08e−5/1.08e−6 respectively. Hence ROT042's caution about temporal nondifferentiability is **material**, not merely a possible artifact. NOT claimed for every resonant N; simultaneous knots can have sums of rank-one jumps.

## Independent executed falsification / provenance

Four separate source paths:
(A) new stdlib Fraction analytic constants plus 100-digit mpmath.iv W_F norm and strict independent 6-pivot LDL: 16 typed PASS.
(B) new independent direct source-spectral O(m) alpha derivatives/one-knot exact rational time geometry/three one-sided finite differences: 13 typed PASS.
(C) new separate exact Fraction time boundaries and source-finite compressed products at N300000 (m10.8 billion) and N1000000 (m120 billion) for 30 parameter pairs in the legal ball: 62 typed PASS. Numerical stress, not proof all N, no full N³ grids.
(D) **RETAINED** ROT041 frozen full REAL 3D original auxiliary apply_E/P_TT/THREE-term Lie N12/16 30 typed PASS, max Fourier norm mismatch 2.3188e−16. Not a source-native N32 full kink run; not new independent original historical source tests.
TOTAL 121/121 executed typed PASS, **30 retained ROT041 replay**, not 121 physical experiments. One Moderator-local standalone ZIP has expanded Polish full proof, three NEW standalone runnable scripts plus retained ROT041 source test, dependency helpers, original unchanged source and ROT039 witness, four original JSON+stdout, README SHA manifest. ZIP CRC PASS, payload SHA256 18/18, four independent CLEAN extracted reruns and FOUR JSON BYTE IDENTICAL PASS. ZIP SHA256 13e05ab62735fd3833584c1957de9d1281b8562e2aab7b0ced956d790df84f56. The code/ZIP are LOCAL to user conversation, NOT claimed separately hosted on Github.

**FIREWALL:** fixed 6-level synthetic source finite TT model, local parameter ball only, all even N>=300000; no global arbitrary schedule inverse, measured noise, original historical h=fI/masked K_A, physical J3/K GR/GW/PBH, independent referee, BW/canon/EXEC, or novel mathematics. NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
