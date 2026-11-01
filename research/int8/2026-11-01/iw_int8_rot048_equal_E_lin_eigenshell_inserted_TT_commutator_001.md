---
artifact_id: IW_INT8_ROT048_EQUAL_FILTER_EIGENSHELL_INSERTED_TT_NONCLOSURE_001_20261101
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_SOURCE_OPERATOR_COMPATIBILITY_AND_GAUGE_TYPE_GATE_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_SOURCE_TYPED_AUXILIARY_E_LIN_EIGENSHELL_INSERTED_TT_NONCLOSURE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# INT8 ROT048 — exact inserted RAW-k TT commutator survives equal E_lin eigenvalues

Date 2026-11-01. Mathematical SOURCE-DIRECT audit of the retained original auxiliary DTC0a helper. No original historical masked production K_A, physical GR/J3/K, canon or EXEC is inferred. BW ING, independent referee and original source owner adoption remain PENDING.

## Previous owners FIRST, mature mathematical host

MT13 FIRST correct affine E_g and naive target folded RAW-k alias. INT8 ROT016 FIRST source Q Lie E P leakage on TT input, ROT046 FIRST single projected_T(C,I) central derivative/raw-k TT symbol mismatch, ROT047 FIRST commuting two-z-shear unfiltered Identity K_C=K_B=0 but K_A_out nonzero. THIS ROT048 ONLY extends to GENERAL unwrapped two-mode symbol formulas and a separate witness with EXACTLY EQUAL E_lin eigenvalues at nonzero alpha. M13/M14 first historic h=fI and masked K_A; Geeky-S11 even RAW casting; PRF other Lie, XH curved York remain separate. Mature host Hyman and Shashkov, The Orthogonal Decomposition Theorems for Mimetic Finite Difference Methods, SIAM J Numerical Analysis 36 (1999) 788-818, DOI 10.1137/S0036142996314044, addresses compatible discrete operators; it does NOT claim these source-specific witnesses. NO general math novelty.

## Exact original source and definitions

Original user-retained auxiliary source deepseek_python_20260627_a87249.py has SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. Functions literally executed on full grids: derivative, lie_derivative_tensor, apply_E, apply_P_TT, lie_bracket, compute_K_C, compute_K_B, compute_K_A_out. The historical complete dtc0a_runtime_v0_3_1.py is BYTE-UNAVAILABLE and masked historical K_A is NOT run. Odd N grid, spatial h=2pi/N, centered second-order derivative with source Fourier wavevector s_N(k)_j=sin(h k_j)/h, while original source rank2 TT_k on k!=0 uses RAW signed k. Input H=I3 constant puretrace. Source vector fields C_a=e_z sin(a dot x), C_b=e_z sin(b dot x), a,b nonzero signed 2D integer wavevectors, zero z dependence, unwrapped nonzero signed Fourier sidebands a+b and a-b. E_mode is Identity or E_lin with real alpha; source E_lin eigenvalue e_alpha(k)=1-4alpha sum_j sin²(h k_j/2). E(I3)=I3 exactly.

Use sym(u,v)=u tensor v+v tensor u and source r_a=(I-aa^T/|a|²)s_N(a), r_b=(I-bb^T/|b|²)s_N(b). Put e_a=e_alpha(a),e_b=e_alpha(b), or 1 in Identity.

## T048.1 — universal EXACT two-sideband source-auxiliary identity

The SOURCE bracket of these two z-shears is identically zero, because both have only z-component and no z dependence. Their unprojected source commutator on constant input H=I is exactly
  K_C=(e_b-e_a) sym(s_a,s_b) cos(a dot x)cos(b dot x).
Thus K_B=P_raw K_C. The projected-between-Lie source auxiliary K_A_out uses the EXACT entire-tensor intermediate coefficient
  H_AB=e_b sym(r_b,s_a)-e_a sym(r_a,s_b)
and obeys the all-nodes Fourier identity
  K_A_out(x)=1/2 sum_(sigma=+,-) cos((a+sigma b) dot x) TT_(a+sigma b)(H_AB).

For each sideband k_sigma=a+sigma b in the xy-plane, let n_sigma=J k_sigma/|k_sigma| in the xy-plane, J(x,y)=(-y,x). Define
  delta_sigma=e_b(n_sigma dot r_b)(n_sigma dot s_a)
              -e_a(n_sigma dot r_a)(n_sigma dot s_b).
Then TT_(k_sigma)(H_AB)=delta_sigma (n_sigma tensor n_sigma-e_z tensor e_z), and the FULL GRID Frobenius RMS exactly equals
  sqrt(delta_plus²+delta_minus²)/2.
For genuinely distinct nonzero signed Fourier sidebands, K_A_out=0 IFF both delta terms are zero. These are exact identities, not merely a norm fit, and remain valid in the mentioned no-wrap contract.

## T048.2 — exact equal-eigenshell E_lin witness distinct from ROT047

Set a=(1,2),b=(2,-1). They are perpendicular and have same E_lin spectral factor:
  e_a=e_b=e=1-4alpha(sin²(h/2)+sin²h).
For odd N>=7 and stable alpha in [0,1/6], e>0. Put x=sin(h)/h, y=sin(2h)/h,
  d=2x-y=2sin(h)(1-cos h)/h>0,
  t=(x+2y)/5>0.
Then r_a=d b/5, r_b=-d a/5, s_a=t a+d b/5, s_b=t b-d a/5. Exactly
  H_AB=-2e d t diag(1,1,0).
The source K_C and K_B are ZERO even for E_lin, because e_a=e_b, whereas K_A_out is NOT ZERO.

Signed sidebands k_plus=(3,1), k_minus=(-1,3), both within the signed cube for ALL odd N>=7. Let n_plus=(1,-3,0)/sqrt10, n_minus=(3,1,0)/sqrt10 and W_sigma=n_sigma tensor n_sigma-e_z tensor e_z. Full entire-grid tensor equality:
  K_A_out(x)=-(e d t/2) [
    cos((3,1) dot x) W_plus + cos((-1,3) dot x) W_minus].
The source-original unmasked full-grid Frobenius RMS is exactly:
  ||K_A_out||_RMS=e d t/sqrt2
     =e (2x-y)(x+2y)/(5 sqrt2)>0.
For each fixed alpha (Identity or E_lin) N² times this RMS tends to 2sqrt2 pi²=27.9154567985555... because e->1, d~h², t->1. This is ONLY a two-fixed-smooth-mode asymptotic, not a global frequency-uniform operator result.

Source-native sample alpha=.05:
| N | Identity K_A RMS | E_lin K_A RMS | K_C and K_B E_lin |
|---:|---:|---:|---|
| 7 | 0.282294372013 | 0.237154623087 | 0 exact |
| 9 | 0.227987654379 | 0.203813955148 | 0 exact |
| 11 | 0.175581199794 | 0.162529696937 | 0 exact |
| 15 | 0.107306378337 | 0.102828226321 | 0 exact |
| 21 | 0.058809710651 | 0.057526550867 | 0 exact |
| 31 | 0.028087170976 | 0.027802051792 | 0 exact |

Important negative controls: a=(1,2),b=(2,1) also has equal E eigenvalues but K_A=0: equal eigenvalues alone are NOT sufficient for leakage. Collinear a=(1,2),b=(2,4) with Identity has K_A=0 despite individual source projection leakage; for E_lin with unequal e factors, this distinction disappears. Original ROT047 pair a=(1,2),b=(1,1) with E_lin nonzero alpha has K_C, K_B, K_A ALL nonzero, so cannot support an exclusive projector-insertion attribution. Replacing raw TT_k with hypothetical centered-symbol TT_s would change original science object and is NOT done.

## Executed code, falsification, and custody

A. MAIN standalone NumPy on full original helper with byte SHA verification: 15 ACTUAL native cases with full-grid tensor fields, original compute_K_A_out, compute_K_B, compute_K_C and bracket: 12 principal source cases N=7,9,11,15,21,31 × Identity/E_lin(alpha=.05) plus 3 controlled input families, entire tensor field relative/infinity discrepancy <2e-11 on UNROUNDED arrays, all PASS. General no-wrap pair formula 2208 checked integer pairs a,b in [-3,3]² at N31; 48 equal-E nonzero KA and 96 collinear Identity KA-zero cases; mathematical scalar N up to 6401 but NOT full native N³ there.

B. INDEPENDENT source-FREE audit with SymPy+Fraction, no NumPy and no DTC0a source import: 12 symbolic equal-eigenvalue tensor identities, 4512 exact rational two-sideband projector checks (4204 nonzero, 308 zero), independently 176 complete exact SymPy 3x3 tensor spot checks, ALL PASS. Initial exploratory exact script incorrectly asserted raw, differently factored but equivalent expressions equal; fixed the audit to compare symbolic simplified differences and reran. Initial expensive all-SymPy clean replays timed out; changed only test implementation to exact fractions plus independent 176 full SymPy tensor checks, preserving all 4512 cases; reran all. Neither problem was a substantive mathematical counterexample.

Moderator-local full 8-member ZIP iw_int8_rot048_equal_filter_eigenshell_projected_commutator_bundle.zip SHA256 459379d9063b681c1cfcc2c84d8760656d6ab9ec695a80ce8c29958976c73332. ZIP CRC PASS, SHA256 7/7 payload PASS. CLEAN_A and CLEAN_B: both standalone JSON byte-identical with original SHA-pinned user helper. CLEAN_C: exact JSON byte-identical, main mathematics equal, source explicitly SOURCE_SKIPPED_NO_HELPER. Full Polish original report, full runnable NumPy original helper audit, full independent exact script, both JSON, README, RUNLOG, SHA256SUMS. Actual original helper not redistributed. Public report and frozen original bundle are distinct surfaces; publication of separately runnable files must be verified independently.

## Strict hard STOP
Only original AUXILIARY unmasked compute_K_A_out, second-order centered derivative, odd N>=7, fixed H=I, two z-independent shear fields, E_lin or Identity. Not original historical production masked K_A, not all h=fI controls or observational noise, not even-N raw-cast, curved York, GR gauge closure, physical J3/K, Noether, GW energy, experimental gravity. NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE; BW ING, independent referee and owner uptake UNCONFIRMED. No new task cascade.
