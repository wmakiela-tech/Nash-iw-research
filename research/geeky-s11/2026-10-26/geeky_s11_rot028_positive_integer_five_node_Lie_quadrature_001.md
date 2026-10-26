---
artifact_id: GEEKY-S11-ROT028-POSITIVE-INTEGER-FIVE-NODE-LIE-PLACEMENT-MOMENT-MATCH-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-26
problem_id: P3_DTC0A_INTEGER_SOURCE_FILTER_LIE_INSERTION_EXPENSIVE_UNIFORM_MEAN_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
class: EXACT_POSITIVE_INTEGER_FIVE_NODE_QUADRATURE_DEGREE5
status: MATHEMATICAL_PROOF_3710_TYPED_CONTROLS_PASS / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT028: source-legal positive integer Lie-insertion quadrature

## Own and external prior art

Geeky ROT015-017 FIRST source helper even-N raw-k realcast versus correct B=GA; ROT021-023 fixed-smooth TT memory carriers; ROT024-025 gain-alpha identifiability and repeated E; ROT026 FIRST filter placement effect; ROT027 FIRST exact uniform all-(m+1)-insertions Duhamel mean and its logarithmic-mean diffusion limit. Current result does NOT reclaim those prior findings. M14 historical masked puretrace h=fI/K_A, INT8 geometric TT and PRF12 process memory are distinct. This is a constrained moment-matching application of classical Gaussian quadrature (NIST DLMF §3.5, https://dlmf.nist.gov/3.5 ; SIAM News Townsend 2015). NO mathematical novelty or priority claim.

Archived and UNCHANGED auxiliary source deepseek_python_20260627_a87249.py SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. Original historic production dtc0a_runtime_v0_3_1.py not available. On even N^3, full unmasked real tensors, source 3-term centered Lie L with fixed C=(0,cos x,0), strict orthogonal real raw-TT B=GA, T=BLB and scalar E=I+alpha*h^2*Delta2 (full-grid nonexpansive iff 0<=alpha<=1/6). Crucial: for alpha>1/12, E has NEGATIVE high-frequency multipliers, even though contractive; fractional E powers would NOT be a source-legal globally real implementation. All positions in our schemes are INTEGER and use only ordinary powers of retained E.

## Exact discrete measure and positive 3- and <=5-node rules

For even m>=2, define original ROT027 average
U_m=(1/(m+1)) SUM_(ell=0)^m E^(m-ell) T E^ell.

Let X=ell-m/2 for the discrete uniform distribution ell=0,...,m. Its exact moments are odd moments 1,3,5 equal zero, v=E[X^2]=m(m+2)/12 and mu4=E[X^4]=m(m+2)*(3m^2+6m-4)/240.

THREE-node optional positive rule: j=ceil(sqrt(v)), center ell=m/2 weight 1-v/j^2, symmetric ell=m/2+/-j weight v/(2j^2) each. Integer indices all valid. All moments through degree 3 agree exactly with uniform, at most THREE Lie evaluations.

FIVE-node main rule: rho^2=mu4/v=(3m^2+6m-4)/20. Set r0=floor(sqrt(rho^2)), r1=ceil(sqrt(rho^2)); when r0<r1 set paired masses
u0=(v*r1^2-mu4)/(r0^2*(r1^2-r0^2)),
u1=(mu4-v*r0^2)/(r1^2*(r1^2-r0^2)).
Assign u0/2 to each integer insertion at m/2+/-r0, u1/2 at m/2+/-r1, and center mass 1-u0-u1. If r0=r1, use paired total mass v/r0^2 and center 1-v/r0^2. All masses nonnegative and sum 1 for EVERY even m>=2. Proof: r0^2<=mu4/v<=r1^2 gives paired positivity. For m>=10, r0^2>=v, whence u0+u1<=v/r0^2<=1; verify m=2,4,6,8 directly with exact fractions. Furthermore r1<=m/2, so all insertion indices are allowed. By construction centered moments 2 and 4 agree, odd centered moments vanish by symmetry and total mass is 1. Thus **EVERY moment degree 0..5 matches EXACTLY**. The rule needs at most FIVE source Lie insertions, independently of m. This is NOT an exact identity U_m=Q5 for general exponential symbols.

## Rigorous sixth-order bound (positive LOW-band Fourier factors)

For a,b>0, set G=(ab)^(m/2), z=log(b/a), delta=m*z. Both the full sum and the positive moment-matched Q5 are expectations of G exp(z X) with |X|<=m/2. Taylor's theorem and equality of moments up to degree 5 give the rigorous (nonsharp) scalar bound

abs(U_m(a,b)-Q5_m(a,b)) <= G*exp(abs(delta)/2)*(abs(delta)/2)^6/360.

Three-point moment matching analogously gives a fourth-order bound. These are low-band POSITIVE-a,b statements, not uniform high-frequency full-grid operator-error theorems; globally stable E may have negative multipliers.

## Continuous heat-time limit with fixed smooth real TT test carriers

Take m even with m/N^2->beta>0, fixed alpha in (0,1/6]. For fixed low Fourier band j, retained E symbol q_j=1-4alpha[sin^2(pi j/N)+sin^2(pi/N)] satisfies q_j^m->d_j=exp[-4pi^2*alpha*beta*(j^2+1)]>0. On sideband j=p+/-1 of H_p=T_p cos(px+y), p2/3, with the previously established exact TT coefficients (p2:71/200,31/40; p3:261/680,141/200), the exact uniform mean tends to L(A,B)=(A-B)/(log A-log B), A=d_j, B=d_p.

Writing delta=log(A/B), G=sqrt(AB):
uniform/G=sinh(delta/2)/(delta/2).
midpoint/G=1; leading difference delta^2/24.
3-node integer/G -> cosh(delta/(2sqrt(3))); leading uniform-minus-3-node difference delta^4/4320.
5-node integer/G -> 4/9+(5/9)*cosh(sqrt(3/20)*delta); leading uniform-minus-5-node difference delta^6/2016000.
This is the standard 2- and 3-point Gaussian quadrature LIMIT, attained through exact *finite integer* insertion positions.

At beta=.02, input-normalized errors relative to U for (H2 alpha.05, H3 alpha.05, H2 alpha1/6, H3 alpha1/6):
midpoint [5.82742924e-4, 1.11356696e-3, 3.98499692e-3, 5.30068030e-3];
3-node [9.77799023e-8, 3.55803728e-7, 6.38900737e-6, 1.58198463e-5];
5-node [7.80410463e-12, 5.21181777e-11, 5.42160764e-9, 2.24749686e-8].
C and H_p fixed smooth independent of grid. At alpha=0, E=I and all variants coincide exactly.

## Executed independently, strict scientific scope

(A) New Python Fourier/moment program, 198 N/p/alpha/beta combinations N12...4096, actual source q, independent exact finite uniform checks when feasible and asymptotic values: 1088 typed PASS.
(B) Independent full N^3 real source-native unmodified apply_E, full 3-term lie_derivative_tensor, source apply_P_TT plus explicit strict reality guard B; 32 cases N12/16 with m2/4/6/8, both TT carriers and alpha0/.05/1/6: 288 typed PASS, max norm discrepancy 1.492e-16. Local preliminary pointwise test was corrected to the proper GLOBAL scalar orthogonality before archival, rerun passed.
(C) Independent Python stdlib Fraction-only 3x3 TT polarization and positive weights/moments all even m2..512, exact two-symbol samples: 2334 typed PASS. TOTAL **3710/3710**; these are typed tests, NOT physical datasets.

Complete long mathematical report, THREE runnable Python programs, THREE executed JSON, unmodified auxiliary source, README, SHA256 manifest in Moderator-local reproducibility ZIP GEEKY_S11_ROT028_POSITIVE_INTEGER_FIVE_NODE_LIE_QUADRATURE_REPRO_001.zip; ZIP SHA256 e8ece668eaed5f32b8f91f3d78373193e1d17bb619e9c4558d085e770078eda6; CLEAN unzip ZIP CRC PASS, all 9/9 content SHA PASS, three clean script reruns produced byte-identical 3 JSON PASS. Source and reproducer code are NOT asserted to be GitHub-hosted by publication of this text record alone.

Cost guarantee is at most FIVE source Lie calls vs m+1, NOT constant TOTAL applications of E, FFT, memory or experiment setup. No claims about original historical h=fI/masked K_A, production runtime, J3/K, GR/GW/PBH, independent referee, BW ingestion, authorial adoption, canon or EXEC. NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
