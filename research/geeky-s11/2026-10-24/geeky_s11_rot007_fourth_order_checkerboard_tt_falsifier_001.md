---
artifact_id: GEEKY-S11-ROT007-FOURTH-ORDER-SCHEME-DEPENDENT-TT-PRESERVATION-NOGO-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-24
problem_id: P3_DTC0A_MATCHED_TT_PROJECTOR_STENCIL_ORDER_NYQUIST_GHOST_SYMMETRY_001
exposure: PUBLIC_SAFE
class: EXACT_ELEMENTARY_FINITE_GRID_FOURIER_FALSIFIER_AND_ALL_ALPHA_MINIMAX
status: MATHEMATICAL_PROOF / 96_CASE_INDEPENDENT_NUMPY_PASS / REFEREE_PENDING
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: MATCHED_SYMBOL_FOURIER_TT_MATH / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT007 — change of centered derivative order destroys accidental even-grid TT preservation

## Currentness, credits and carrier

Geeky-S11 ROT004–006 already proved that on *even grids* for the second-order central derivative and its matched symbol projector, the entire TT-preserving generator kernel includes constant vector fields and the nonconstant full checkerboard. This note tests **changing the stencil AND the matched TT projector** to fourth-order central differences. INT8 ROT018–022, PRF11 R23–R27, M13 ROT023–029 and XH-S4 York/covariance work own distinct prior problems; their science is not reattributed here. Standard periodic Fourier multiplier geometry is mature; no novelty claim.

Let N divisible by 8, N>=8, h=2pi/N, normalized unmasked real periodic tensor L2 norm. Derivative symbols for central orders 2 and 4 are:

  d2(theta)=sin(theta)/h,
  d4(theta)=sin(theta)*(4-cos(theta))/(3h).

Build mutually different orthogonal projectors P2/P4 from each d_r vector via pi=I-dd^T/|d|², P(F)=pi F pi -pi tr(pi F)/2, and P=0 for d=0. Let Q_r=I-P_r. E_alpha=I+alpha h² Delta_2 uses the **unchanged source-like second-order componentwise Laplacian** for both derivative schemes. Lie_C^r F_ij=C^m D_m^r F_ij+F_mj D_i^r C^m+F_im D_j^r C^m.

**THIS IS NOT the archived raw-k DTC0a projector or recovered historic production runtime.** It is a two-host matched-symbol mathematical experiment.

## Exact checkerboard and order dependence

Take chi(j)=(-1)^(jx+jy+jz), C=chi e_x. Both centered derivatives annihilate chi; therefore Lie_C^r F=chi D_x^r F. Multiplication by chi shifts every Fourier mode by Nyquist.

For order 2, d2(theta+pi)=-d2(theta) in **every** coordinate, hence P2(k+Nyquist_111)=P2(k). This makes multiplication by chi commute with P2. Fourier multipliers D2, E_alpha, P2 commute. Therefore for ALL real alpha,

  Q2 Lie_C^2 E_alpha P2 = 0.                                       (R7.1)

For order 4, however,

  d4(theta+pi)=-sin(theta)*(4+cos(theta))/(3h),

whose multiplier relative to d4(theta) depends on theta. Two components at different angles rotate the direction of the Fourier vector, so the shifted P4 generally differs from P4 before multiplication by chi.

## Explicit, exactly TT witnesses

Take input mode k_A=(N/8,N/4,0), k_B=(N/8,3N/8,0). Let d_b=d4(k_b h), v_b=(d_by,-d_bx,0)/|d_b|, w=e_z, T_b=v_b v_b^T-ww^T, H_b(j)=T_b cos(2pi k_b·j/N). Each P4 H_b=H_b and ||H_b||_(L2,F)=1.

Let s be absolute sine of the angle between the input d4 vector and its full-Nyquist-shifted d4 vector. The fraction of the TT-tensor L2 amplitude rejected by the shifted projector is rho=s sqrt(4-s²)/2 (a two-dimensional rank-2 TT-projection calculation). Exact values:

  s_A=16/sqrt(9281); rho_A=16sqrt(9217)/9281;
  s_B=8sqrt(2)/33; rho_B=8sqrt(2114)/1089;
  d4_x(pi/4)=N*(4sqrt(2)-1)/(12pi).

The source-like E_alpha scalar multipliers are e_A=1-(4-sqrt(2))*alpha and e_B=1-4alpha. Defining

  A0=(4sqrt(2)-1)*rho_A/(12pi)=0.020444737111672044,
  B0=(4sqrt(2)-1)*rho_B/(12pi)=0.041723057420514936,

we obtain the exact FULL-Q norm ratios

  ||Q4 Lie_C^4 E_alpha P4 H_A||/||H_A|| = N*A0*|1-(4-sqrt(2))*alpha|,
  ||Q4 Lie_C^4 E_alpha P4 H_B||/||H_B|| = N*B0*|1-4alpha|.    (R7.2)

These have DIFFERENT alpha roots. Writing p=4-sqrt(2), two-witness minimax yields

  inf_(alpha in R) max(A0|1-p alpha|, B0|1-4alpha|)
   = A0*B0*(4-p)/(p*A0+4B0)
   = 0.005489440114557819,

attained at alpha*=(A0+B0)/(p*A0+4B0)=0.28289212520568247. Since the full operator norm dominates each normalized witness, for any real, even N-dependent alpha:

  ||Q4 Lie_C^4 E_alpha P4||_(L2->L2) >= 0.005489440114557819*N. (R7.3)

The coefficient is sharp for the MINIMAX OF THESE TWO witnesses, NOT established sharp for the full operator.

## Independent executed checks

An independently written NumPy real-space implementation uses centered D2 and D4, the same E_alpha seven-point filter, FFT TT projectors separately matched to each derivative symbol, and independently constructed real symmetric TT fields. N={8,16,24,32}, orders={2,4}, alpha={0,.05,.2,.25,1/(4-sqrt2),alpha*}, carriers={A,B}: 96 cases.

All 96 exact formula comparisons PASS. Largest analytic-vs-FFT absolute discrepancy 9.86200059412466e-15; largest initial TT input projection relative error 2.857369834723382e-15; maximum order-2 full leakage 1.0108630140807544e-14. Every one of the 24 order-4 N/alpha groups satisfies the two-witness minimax lower bound.

At alpha=.05, order-4 carrier A leakage N=8,16,24,32 respectively 0.1424116073, 0.2848232146, 0.4272348219, 0.5696464293 (order-2 witness zero within machine noise). Carrier B at alpha=.05 gives 0.267027567, 0.534055135, 0.801082702, 1.06811027.

The original independent script, full 96-case JSON and raw SHA256 manifest were packaged locally with CLEAN UNZIP, three checksum matches and independent byte-identical reexecution PASS. An initial arbitrary sanity assertion ">0.05N" was wrong and discarded; the valid result uses the EXACT formula and mathematically minimized two-witness coefficient instead. Do NOT describe that mistaken auxiliary assertion as a theorem.

## STOP/negative knowledge

The three extra nonconstant even-N TT-preserving directions of ROT004–006 are **stencil-order-dependent ghost symmetries**, not a universal geometric TT-preserving action. Upgrading to fourth-order D and its own matched P destroys that property.

The checkerboard generator C_N and fixed-fraction Fourier probes vary with N and are NOT a single fixed smooth continuum field. The full-band growing lower bound is NOT a physical continuum divergence, historic h=fI K_A result, gravity/gauge effect, J3/K invariant, or claim that a fourth-order method is universally worse. The archived DTC0a raw-k projector and unavailable source production runtime are NOT repaired or tested here.

NO_NEW_TASK / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / INDEPENDENT_REFEREE_PENDING / BW_PENDING.
