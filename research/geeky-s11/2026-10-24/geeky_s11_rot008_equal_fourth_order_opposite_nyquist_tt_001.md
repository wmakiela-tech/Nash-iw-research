---
artifact_id: GEEKY-S11-ROT008-EQUAL-FOURTH-ORDER-OPPOSITE-NYQUIST-TT-PRESERVATION-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-24
problem_id: P3_DTC0A_STENCIL_PARITY_VS_TT_PRESERVATION_AND_LOCALITY_001
class: EXACT_PERIODIC_FOURIER_COUNTERMODEL / FOURTH_ORDER_STENCIL_PARITY_AND_MINIMUM_RADIUS
exposure: PUBLIC_SAFE
status: PROOF_AND_INDEPENDENT_120_CASE_NUMPY_PASS / REFEREE_PENDING
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: MATURE_FOURIER_TT_HOST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT008 — Equal fourth-order accuracy, opposite checkerboard TT symmetry

## Scientific question / source subtraction
Geeky-S11 ROT004-006 established the full-checkerboard TT-preserving generator for the centered **second-order**, matched-symbol projector. ROT007 showed that this generator fails for the standard **fourth-order** centered derivative and its distinct matched projector. Does fourth-order accuracy itself remove checkerboard ghost preservation? **No.** An equally fourth-order accurate but odd-offset-only centered stencil retains the full-checkerboard symmetry for all real scalar filter alpha. This is an algebraic, host-typed countermodel, NOT a reason to prefer a ghost-preserving stencil in physical computations.

Prior owners distinct: INT8 ROT018-022 (scalar filter shear equivariance), PRF11 R23-R27 (source *raw-k* collocation/alias/Sobolev), XH-S4 (moving York and curved tensor operators), M13 (historical h=fI masked source). Mature finite difference moment and interpolation host, e.g. https://tobydriscoll.net/fnc-julia/localapprox/finitediffs.html. No novelty claim.

## Defined mathematical host
Even periodic N-grid in three coordinates (numerics N=8,16,24,32), spacing h=2pi/N; translation-invariant centered finite difference
D_a f(j)=sum_(r>=1) a_r [f(j+r)-f(j-r)]/(2h)
with symbol d_a(theta)=sum_r a_r sin(r theta)/h.

For each stencil construct its OWN orthogonal, real, matched-symbol Fourier TT projector P_a via delta_a(k)=(d_a(k_x h),d_a(k_y h),d_a(k_z h)), pi=I-delta delta^T/|delta|²,
P_a F=pi F pi -pi tr(pi F)/2 for delta!=0, and P_a=0 at delta=0. Q_a=I-P_a. This is mathematically different from historical DTC0a RAW-k P_TT whose even-N validity failed. Operator is source-style Lie derivative of symmetric covariant rank2:
(L_C^a F)_ij = C^m D^a_m F_ij + F_mj D^a_i C^m + F_im D^a_j C^m.
Scalar componentwise E_alpha=I+alpha h² Delta_(2), same seven-point *second-order* difference Laplacian for all stencils. Full-grid unmasked normalized Frobenius L2.

## R8.1 — Constructive same-order opposite symmetry
Standard order4 radius2 a1=4/3, a2=-1/6, symbol
d_std(theta)=sin(theta)(4-cos(theta))/(3h).

Odd-offset order4 radius3 a1=9/8, a3=-1/24, symbol
d_odd(theta)=[(9/8)sin(theta)-(1/24)sin(3theta)]/h
=sin(theta)(1+sin²(theta)/6)/h.

Both satisfy the fourth-order Taylor conditions sum_r r*a_r=1 and sum_r r³*a_r=0.
Standard sum_r r^5 a_r=-4 -> leading truncation -(1/30) h^4 f^(5).
Odd-only sum_r r^5 a_r=-9 -> leading truncation -(3/40) h^4 f^(5), coefficient 9/4 times greater.
Odd-only requires radius3 rather than radius2, and is NOT uniformly more accurate just because of preserved symmetry.

Take chi(j)=(-1)^(j_x+j_y+j_z), generator C=chi*b for arbitrary constant b in R³. Every antisymmetric centered derivative annihilates chi, hence L_C^a F=chi b·D_a F.

For ANY odd-offset-only stencil, d_a(theta+pi)=-d_a(theta). Thus delta_a(k+Nyquist*(1,1,1))=-delta_a(k), including exact zero-symbol modes; because P_a depends on delta only through its direction up to sign, P_a is identical before and after checkerboard shift. Consequently multiplication by chi COMMUTES WITH P_a. Since b·D_a and E_alpha commute with P_a as Fourier multipliers, the ENTIRE P_a-TT range is invariant under L_C^a E_alpha for EVERY real alpha:
Q_odd L_(chi*b)^odd E_alpha P_odd=0.              [R8.1]
Constants also preserve TT. In particular at N divisible by8 both central order2 and odd-only central order4 admit the six-dimensional family K6={a+b chi} of TT-preserving generators.

For standard fourth-order stencil:
d_std(theta+pi)=-sin(theta)(4+cos(theta))/(3h)
and d_std(theta+pi)+d_std(theta)=-sin(2theta)/(3h),
which is not zero globally. Explicit exactly TT carriers from ROT007 at k_A=(N/8,N/4,0), k_B=(N/8,3N/8,0), b=e_x, have positive projector leakage. The EXACT 2-carrier all-alpha minimax of ROT007 remains:
||Q_std L_(chi*e_x)^std E_alpha P_std||_(L2->L2)
>= 0.005489440114557819 N, for every alpha∈R and N divisible by 8. [R8.2]
This constant is sharp for the TWO-CARRIER minimax only, not for full operator norm. Since generator chi_N and carriers vary with N, NOT a fixed-smooth continuum source claim.

## R8.3 — Sharp radius tradeoff inside centered explicit stencils
The fourth-order Taylor conditions sum_r r*a_r=1 and sum_r r³*a_r=0 are both necessary. For only odd-offset support at radius<=2, the sole variable is a1, and conditions require a1=1 and a1=0 simultaneously. Hence radius2 cannot achieve fourth-order AND checkerboard anti-periodicity using purely odd offsets. Radius3 with a1,a3 solves the two linear equations uniquely as (9/8,-1/24). This is a *sharp support-radius* claim in the family of explicit centered translation-invariant difference stencils only; not a claim about general compact, staggered or implicit operators.

## Conditional full-kernel classification for odd-only order4
d_odd(theta)=sin(theta)(1+sin²(theta)/6) has zeros exactly at 0,pi. So its vector conformal strain kernel on even grids is 24-dimensional (8 Fourier corners times 3 vector components). The axial 12-TT-probe trace identity of ROT002 still holds with s_odd=sin(h)(1+sin²(h)/6)/h; conditional on e1=1-4alpha sin²(pi/N)!=0 it confines TT-preserving C to the eight corners. The oblique 12-TT probe frame of ROT004 also holds with s_odd; conditional on e2=1-8alpha sin²(pi/N)!=0, it eliminates the six *proper* Nyquist corners. Thus for e1*e2!=0, the ENTIRE TT-preserving generator kernel for this odd-step fourth-order projector host equals K6={a+b chi}. At exceptional alpha where e1 or e2 vanish, R8.1 sufficiency for K6 still holds, but this note DOES NOT claim that a complete iff has been proved for those special values.

## Independent executed source-type checks
Independent standalone NumPy repro computes *direct physical-space centered differences*, the same scalar E_alpha, and a separate 3D Fourier TT projector matched to each stencil. Test sizes N=8,16,24,32, three stencils (2nd radius1, standard4 radius2, odd-only4 radius3), five alphas 0,.05,.2,.25,1/(4-sqrt2), two exact TT carriers =120 comparisons. Plus 12 *random broadband* tensor TT tests (four N times three stencils). All 120 direct-FFT analytic-formula comparisons PASS; maximum abs error 1.0721278301600827e-14, maximum normalized TT input projection error 2.870349843956195e-15. Maximum 4th-order odd-offset observed witness leakage 1.1176594387784612e-14. Broadband N32, alpha=.05: standard4 leakage 0.6698797745753129, odd4 leakage 1.1581775257263966e-15. Same fourth-order consistency moment checks PASS.

CLEAN ZIP local execution: original self-contained Python, 120-row JSON, full report, SHA256 manifest; ZIP CRC PASS, 3/3 source hashes PASS, clean Python re-execute PASS, JSON byte-equal. This GitHub report is a science record; uploaded Python/JSON provenance must be independently checked before they are called GitHub-custodied.

## Scope / STOP
This proves **formal consistency order DOES NOT determine Nyquist ghost TT symmetry**. Parity of explicit first-derivative support and matched TT symbol matter. Other stencil families may behave differently. Preserving checkerboard TT is not physically desirable. No result upgrades historic raw-k DTC0a (even-N failure), metric covariance/moving York, physical gauge invariance, K/J3, GR, or general continuum behavior; high-frequency checkerboard is grid-dependent. No novelty/EXEC/BW/referee/owner adoption claimed.

NO_NEW_TASK / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / REFEREE_PENDING / BW_PENDING.
