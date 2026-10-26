---
artifact_id: GEEKY-S11-ROT027-UNIFORM-LIE-INSERTION-LOGARITHMIC-MEAN-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-26
problem_id: P3_DTC0A_STABLE_E_FILTER_LIE_INSERTION_PLACEMENT_UNCERTAINTY_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
class: EXACT_DISCRETE_FRECHET_DERIVATIVE_DIFFUSION_LOGMEAN_AND_MIDPOINT_BIAS
status: EXACT_PROOF_2290_EXECUTED_TYPED_CHECKS_PASS / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT027: average over all Lie-insertion positions and logarithmic mean

## Own/external prior art and typing

Geeky ROT015–017 FIRST established even-grid auxiliary source raw-k realcast non-idempotence and the strict orthogonal real raw-TT projection B=GA; ROT021–023 fixed smooth TT memory carriers; ROT024 single-E gain-alpha identification cost; ROT025 m~N² stable repeated source E before transport; ROT026 FIRST established nonzero pre/post transport placement bias. This ROT027 investigates the DISTINCT question of the average of ALL positions and the quality of symmetric insertion; no owner displacement. M14 owns historic source puretrace masked h=fI KA, INT8 geometric TT, PRF12 quantum process memory. Classical operator product derivative, Duhamel and arithmetic-logarithmic-geometric mean inequality are mature; e.g. N. Higham, Functions of Matrices (SIAM 2008); https://mathworld.wolfram.com/Arithmetic-Logarithmic-GeometricMeanInequality.html. No priority or mathematical novelty.

The only original source used is unchanged auxiliary deepseek_python_20260627_a87249.py SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801, NOT original unavailable historic production dtc0a_runtime_v0_3_1.py. Even N>=12, full unmasked real symmetric tensor Fourier, source central stencil, three-term Lie L with fixed smooth C=(0,cos x,0), compatible real orthogonal TT B=GA, source E=I+alpha h²Delta_2; 0<=alpha<=1/6 makes E full-3D-grid nonexpansive. E commutes with B, but not with BLB.

## Exact algebraic finite product and source TT sidebands

Write T=BLB. For even m>=2:
U_m=(1/(m+1)) SUM_(ell=0)^m E^(m-ell) T E^ell,
S_m=E^(m/2) T E^(m/2),
A_m=(E^m T+T E^m)/2.
By the product rule, U_m is EXACTLY
d/d_eps [(E+eps*T/(m+1))^(m+1)] at eps=0.
Thus U is a reference for one defined first-order product perturbation, not a unique or physical transport law.

For p=2,3, use fixed smooth exactly B-TT input
H_p=T_p cos(px+y),
T_p=(3/10)(zz - v_p v_p^T/(p²+1)), v_p=(-1,p,0),
||T_p||_F²=9/50.
Full three-term source Lie produces ONLY TT projected Fourier sidebands p+1 and p-1 (frequency y=1). Let d_N=sin(2pi/N)/(2pi/N), q_j=1-4alpha[sin²(pi j/N)+sin²(pi/N)].
Independently verified exact rational polarization coefficients:
p2 c+=71/200 c-=31/40;
p3 c+=261/680 c-=141/200.

For each sideband with a=q_(p+/-1), b=q_p, U_m multiplies Lie-sideband coefficient by
u_m(a,b)=(1/(m+1)) SUM_(ell=0)^m a^(m-ell)b^ell
        =(a^(m+1)-b^(m+1))/[(m+1)(a-b)] (a!=b),
with u_m(a,a)=a^m.
Symmetric placement gives g_m=(ab)^(m/2), endpoint average gives e_m=(a^m+b^m)/2.
For alpha>0, m even>=2 and these low sidebands, q>0 and a!=b, and EXACT strict inequalities hold:
g_m(a,b)<u_m(a,b)<e_m(a,b).
At alpha=0 they coincide (NO all-alpha positive floor). Exact normalized TT output difference:
|| (U_m-S_m) H_p ||/||H_p|| =
d_N * sqrt[ c+²(u_m(q_(p+1),q_p)-g_m(q_(p+1),q_p))²
           + c-²(u_m(q_(p-1),q_p)-g_m(q_(p-1),q_p))² ].
Replace u-g by e-u for endpoint-average error.
Proof: pair terms of the finite sum using AM-GM for lower inequality; convexity in integer insertion position for upper inequality. Identity u_m/g_m=sinh((m+1)z/2)/[(m+1)sinh(z/2)] for z=ln(a/b).

## Continuous diffusion-time limit and strict symmetric bias

For m_N=2ceil(beta*N²/2), fixed beta>0 and alpha>0 stable, q_j^m -> d_j=exp[-4pi²alpha beta(j²+1)]. Hence
u_m(q_j,q_p) -> L(d_j,d_p)=(d_j-d_p)/(log d_j-log d_p), the CLASSICAL logarithmic mean;
g_m -> sqrt(d_j*d_p), e_m -> (d_j+d_p)/2.
All sideband differences are NONZERO for alpha beta>0. Write z=ln(d_j/d_p); relative scalar symmetric bias (L-G)/G=z²/24+O(z^4), endpoint-mean bias (A-L)/G=z²/12+O(z^4). Symmetry removes first-order endpoint placement error but NOT the second-order one. Fixed smooth C AND H_p across N: no Nyquist-carrier cheating.

Beta=.02 continuum input-normalized norm of U-S and A-U, respectively:
p2 alpha=.05: .0005827429243, .0011658869501;
p3 alpha=.05: .0011135669619, .0022286508917;
p2 alpha=1/6: .0039849969164, .0079955364093;
p3 alpha=1/6: .0053006802967, .0106692890730.

OBSERVABLE: original-carrier <H_p,(U-S)H_p> =0 EXACT; matched projected TT sidebands S_(p,s) have signed scalar -(d_N/2)[u_m(q_(p+s),q_p)-g_m(...)], strictly negative at alpha>0 for both s. A false negative from original-carrier scalar is NOT commutation.

## Execution and custody

Three independently authored standalone programs:
(1) Fourier symbol, exact finite sums/stable expm1 and continuum limits N12..8192, 360 parameter sets: 2166/2166 checks PASS.
(2) ORIGINAL UNCHANGED SOURCE HELPER REAL FULL 3D, N12, p2/3, alpha0/.05/1/6, m2/4, literal ALL ell=0..m insertion positions with original E, Lie, raw TT and separate strict guard B: 74/74 PASS; largest numeric disagreement 9.020562075e-17. A broader source-native sweep timed out and is NOT included.
(3) Python stdlib Fraction rational TT 3x3 and exact 2x2 dual-number product derivative: 50/50 PASS.
Total 2290/2290 executed typed controls PASS.

Complete expanded ~12KB proof+3 source scripts+3 actual JSON+unchanged original helper+README+3 stdout and manifest are in the single Moderator-local user-conversation ZIP GEEKY_S11_ROT027_DUHAMEL_LOGMEAN_SYMMETRIC_LIE_REPRO_001.zip. ZIP SHA256 e33d47914d0fd57e104b552c92a13c48251fd54a42469512ae2a1bac5bfe1bbe. Independent clean extraction CRC PASS, content SHA256 12/12, delete and run all 3 scripts and obtain three BYTE-IDENTICAL original JSON PASS. ZIP/code NOT separately uploaded to GitHub.

STRICT: newly specified insertion experiment, NOT original historical single-E/masked K_A experiment, no original production-byte reproduction, J3/K physical invariant, GR/GW/PBH/BBN, noise calibration, independent referee, BW, owner or EXEC sign. No new task cascade. NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
