---
artifact_id: GEEKY-S11-ROT004-EVEN-NYQUIST-TT-KERNEL-OBLIQUE-FRAME-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-24
problem_id: P3_DTC0A_EVEN_N_MATCHED_TT_PRESERVATION_KERNEL_AND_FINITE_FALSIFIER_001
class: EXACT_EVEN_GRID_PDELTA_TT_PRESERVATION_CLASSIFICATION_WITH_12_OBLIQUE_PROBES
exposure: PUBLIC
status: PROOF_AND_INDEPENDENT_NUMPY_PASS / INDEPENDENT_REFEREE_PENDING
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: MATURE_CENTERED_SYMBOL_FOURIER_HOST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT004: exact even-N TT-preservation kernel, not constant-field rigidity

## Currentness and subtraction
ROT002 (Geeky-S11) proved the 12 axial TT trace-strain frame on odd grids. ROT003 showed a checkerboard field on even grids with all 12 full-Q axial outputs vanishing but oblique TT leakage positive; it left even-grid complete detection open. This rotation completes the *correctly typed matched-centered-symbol* even-grid classification. It is distinct from INT8 ROT020 full-band shear-invariant-filter distance, PRF11 R25 Sobolev collocation, M13 ROT027 historic pure-trace mask asymptotics, and XH-S4 curved-metric York/Noether operator work. This result is a finite-grid mature Fourier multiplier calculation; no priority, physical or theorem novelty asserted.

## Source-style mathematical carrier
N even >=6, h=2pi/N, three-dimensional periodic grid. Central derivative D_jF(n)=(F(n+e_j)-F(n-e_j))/(2h). E_alpha=I+alpha*h²*Delta_h, componentwise 7-point centered Laplacian. Lie derivative on symmetric covariant rank-two tensors:
(L_C F)_ij=C^m D_m F_ij+F_mj D_i C^m+F_im D_j C^m.

Define delta_j(k)=sin(2pi k_j/N)/h with Nyquist zeros exactly zero. Define P_delta(k)=pi F pi-(pi/2)tr(pi F), pi=I-delta delta^T/|delta|², at delta!=0; set P_delta=0 at delta=0, including eight corners. Q_delta=I-P_delta. This is a real self-adjoint idempotent *matched-centered-symbol* TT projector; NOT the original historic raw-wavevector DTC0a projector. Work throughout in unmasked full-grid Frobenius L2.
Let e1=1-4alpha sin²(pi/N), e2=1-8alpha sin²(pi/N), s=sin(2pi/N)/(2pi/N). Assume e1*e2 != 0.

## Theorem R4.1 — exact six-dimensional preservation family
Q_delta L_C E_alpha P_delta = 0 on every symmetric tensor
IF AND ONLY IF
C(jx,jy,jz)=a+b*(-1)^(jx+jy+jz), a,b in R³.

Thus preservation kernel dimension is 6, including 3 nonconstant full-checkerboard directions; it is NOT merely constant generators. In contrast ker dev sym(D C) has dimension 24 at even N: 3 coefficients at each of eight Fourier Nyquist corners.

## Step A: axial trace reduction (ROT002 theorem reused)
The 12 real axis-polarised first-harmonic TT test fields of ROT002 obey the exact identity
sum_12 ||tr(L_C E_alpha H)||² = 4 e1² ||dev sym(D C)||².
For every TT output P_delta F the trace is zero, so complete preservation implies dev sym(D C)=0. At every Fourier mode where delta(k)!=0, the three-dimensional algebraic map c->dev sym(delta(k) tensor c) is injective; therefore C has Fourier support *only* on the eight corner characters chi_m(j)=(-1)^(m_x*jx+m_y*jy+m_z*jz), m in {0,1}³. Write C=sum_m chi_m c_m, c_m in R³. ROT002's first 12 probes thus leave exactly 24 possible real coefficients on even N. They are necessary, not sufficient, TT-preservation tests.

## Step B: twelve oblique exact TT carriers
For each coordinate pair (a,b)=(x,y),(x,z),(y,z), each sign sigma=+1,-1, and both phases cos(x_a+sigma*x_b), sin(x_a+sigma*x_b), let c be the third coordinate, v=(e_a-sigma*e_b)/sqrt(2), T_ab^sigma=vv^T-e_c e_c^T, and H=T_ab^sigma times the chosen phase. These are 12 exactly TT real fields, with sum of their squared full-grid L2 Frobenius norms equal to 12.

For corner-supported C the central derivative of C is identically zero, so L_C H=C dot D H. At input k=e_a+sigma e_b the eigenvalue for E is e2, and the transport scalar Fourier multiplier is i*s*(c_m,a+sigma*c_m,b). Multiplication by chi_m shifts its output Fourier mode by Nyquist in the flagged coordinates. If m_a=m_b, the output centered symbol remains parallel to the input, so Q_delta leakage is zero. If m_a!=m_b, the new centered symbol points along v, and the fixed input polarisation has ||T||²_F=2 and ||P_out T||²_F=1/2, yielding ||Q_out T||²_F=3/2.

Parseval orthogonality across corner modes, cos/sin energy pairing and the two signs yield the EXACT identity, valid for every corner-supported C:
F_obl(C):=sum_(12 oblique H) ||Q_delta L_C E_alpha H||²
=3*e2²*s²*W(C),
W(C)=sum_(m in {0,1}³) sum_(a<b with m_a!=m_b) (|c_m,a|²+|c_m,b|²).
The terms at m=000 and m=111 have zero weight. For each of the six other m, exactly two pairs cross; if i is its lone minority-parity coordinate, W_m=2|c_m,i|²+sum_(j!=i)|c_m,j|²>0 for c_m!=0. Hence F_obl(C)=0 iff c_m=0 for all six proper Nyquist corners. In addition:
||Q_delta L_C E_alpha P_delta||_(L2->L2) >= |e2*s|/2*sqrt(W(C))
for any corner-supported C. This is a rigorous nonsharp lower bound.

## Step C: full-checkerboard sufficiency
Let chi_111=(-1)^(jx+jy+jz). Then D chi_111=0. Multiplication by chi_111 shifts *all three* Fourier coordinates by Nyquist. The centered symbol delta(k+(N/2,N/2,N/2))=-delta(k), including zero-symbol corners, so P_delta at those two modes is exactly identical. Thus multiplication by chi_111 commutes with P_delta. Constant-coefficient D, scalar E_alpha and P_delta are Fourier multipliers and commute; hence Q_delta L_(a+b chi_111) E_alpha P_delta=0 for all TT inputs. This completes the iff.

## Finite detection contract
For any vector field C, first test the 12 axial TT traces; if any is nonzero, full preservation fails. If all vanish, C is a corner Fourier combination; test the 12 oblique full-Q outputs. Their sum vanishes precisely for a+b chi_111. All 24 tests zero IF AND ONLY IF the whole operator truly preserves the P_delta-TT subspace. A nonconstant b chi_111 is a genuine PRESERVER, not a false negative. No TT-preservation probe suite can detect it as a failure.

## Executed numerical evidence
Independent standalone NumPy reproducer: complete source-style Lie tensor, centered derivative, E_alpha and 3D Fourier P_delta; 12 parameter cases N=6,8,10,12 crossed with alpha=0,.05,.2. Random real corner coefficients test the exact oblique frame, and a+b chi_111 null controls cover all 24 probes and a random broad-band TT field.
max abs identity gap 2.220446049250313e-16;
max relative identity gap 5.410302628312901e-16;
max relative TT-input projection mismatch 6.40622700963014e-16;
max absolute 24-probe null 1.4442657385410197e-16;
max relative broad-band TT null 1.922441615854644e-16.
The executed code and row-level JSON are preserved in the standalone local ZIP package (not claimed to be original DTC production runner). SHA256: code 4cceef9c9c12b0c909d0523b2b82de609949da0d744433c5b9dd01021b0588a4; JSON d48da17dedde6b4b3728de16ac5c30357f8f1d7e0a3798a99b10d6f1eee8b392. Clean extraction and rerun PASS.

## Guards / negative knowledge
- This projector P_delta is NOT the archived raw-k P_TT; the historical v0.3.1 even-N projector validation failure is NOT repaired and must not be reinterpreted.
- Even-N χ_111 changes at grid frequency when N changes; no fixed-smooth continuum or physical-gauge claim.
- The theorem requires e1 and e2 nonzero; no assertion beyond this carrier or zero-corner convention.
- STOP generic even-N 'whole TT preservation iff C constant'. The mathematically correct preservation family is 6D.
- No historical h=fI KA, K/J3 invariant, cosmology, GR or BBN inference; no claim of novelty, owner uptake, referee PASS, BW ingest or EXEC.

NO_NEW_TASK / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / INDEPENDENT_REFEREE_PENDING / BW_PENDING.
