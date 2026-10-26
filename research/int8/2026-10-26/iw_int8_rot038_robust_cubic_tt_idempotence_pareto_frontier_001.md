---
artifact_id: IW_INT8_ROT038_ROBUST_CUBIC_TT_IDEMPOTENCE_PARETO_FRONTIER_001_20261026
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_SOURCE_TYPED_MEAN_ZERO_TT_LOCALITY_AND_STABILIZER_INTERFACE_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_FINITE_APPROXIMATE_IDEMPOTENCE_CERTIFICATE_AND_SHARP_ASYMPTOTIC_PARETO / SOURCE_TYPED / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 ROT038 — robust cubic TT locality: sharp asymptotic approximate-idempotence Pareto frontier

## Source precedence and closest mathematical host
The 2026-10-26 current #iw-dispatch was read before publication; no conflicting INT8 priority was received. MT13 FIRST established exact metric-transported affine E_g and the original naive raw-target-k TT alias fault. INT8 ROT023–028 ALREADY study source TT alias/norm; ROT029–032 universal ONE fixed metric-independent operator commutant; ROT033 FIRST in INT8 constructed metric-indexed flat integer-grid P_g via 24 proper signed-cube stabilizer; ROT034 full zero-mode SOURCE rank5 finite full support; ROT035 mean-zero sublinear-radius gap; ROT036 onsite local subunit error without cubic invariance; ROT037 FIRST exact finite radius NO-GO for meanzero TT when idempotent AND 24-cube equivariant. ROT038 changes ONLY exact F²=F to controlled APPROXIMATE idempotence. No science credit transferred. M14 historic h=fI masked KA, Geeky-S11 even RAW realcast, PRF12 projected Lie, XH curved York owners remain separate.

Classical EXTERNAL mathematics: finite group multiplicity-free representation 1+2+3 of Sym²(R³) under 24 proper cube rotations, Fourier diagonalization, Bernstein derivative inequality for trigonometric polynomials. V. Totik, "Bernstein-type inequalities", Journal of Approximation Theory 164 (2012), 1390–1401, DOI 10.1016/j.jat.2012.03.002. No mathematics or physics novelty asserted; these ingredients are mature.

## Precisely typed host
ODD N>=3, grid G_N=(Z/NZ)^3; full REAL Sym²(R³) fields. L2 meanzero carrier H_N^0 includes ALL tensor polarizations at every k!=0, excludes k=0 for approximation. Original unchanged retained helper deepseek_python_20260627_a87249.py SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801 gives P_N(k) rank2 orthogonal raw-signed-k TT for ALL k!=0; original rank5 at zero is NOT used in the approximation error, nor inferred on meanzero. Historical full production dtc0a_runtime_v0_3_1.py is byte-unavailable; original masked KA not run.

F is ANY real translation-invariant operator with arbitrary MATRIX-COUPLED 6x6 kernel supported in signed cube radius R, commuting with the 24 proper signed-coordinate cube rotations (ROT033 seed condition). F need NOT be selfadjoint, positive or idempotent. This is H-stabilizer compatibility, NOT one same fixed operator under all integer shears (ROT029 has different assumptions).

Define
  epsilon=|| (F-P_N) restricted to meanzero ||_(L2->L2)
         =max_(k!=0)||Fhat(k)-P_N(k)||_2.
  eta_full=||F²-F||_(full L2->L2)=max_(ALL k)||Fhat(k)²-Fhat(k)||_2.
  eta_zero=||(F²-F) restricted to meanzero||=max_(k!=0)||Fhat(k)²-Fhat(k)||_2.
Distinguish full vs meanzero defect.

## THEOREM 038.1 — explicit FINITE N certificate

Assume epsilon<=e<1 and 5*pi*R/N<1. Set
  M=(1+e)/(1-5*pi*R/N),
  L=(2*pi*R/N)*M,
  a=e+L.
If a<1/2 then no such F exists. If 1/2<=a<1:
  eta_full >= a(1-a);
  eta_zero >= max{0,a(1-a)-L*(2*M+1)}.
For a>=1 the certificate supplies no positive bound, not to be extrapolated.

PROOF, complete:
Let A(theta)=sum_(d in [-R,R]^3) K_F(d)e^(i d.theta), matrix trigonometric polynomial. For scalar matrix elements of A, Bernstein gives |partial_i A|_op<=R sup_theta||A||_op. Any torus angle is within L1 angular distance <=5*pi/N of SOME NONZERO Fourier grid frequency (if closest is k0 choose adjacent nonzero). On k!=0, ||Fhat(k)||<=1+e. Thus, if 5*pi*R/N<1, M_global=sup||A||<=M, and ||A(theta_e1)-A(0)||<=L for theta_e1=2*pi*(1,0,0)/N.

Cubic invariance implies A(0) commutes with all 24 real symmetric tensor congruence actions. The real Sym² fiber is multiplicity-free under the cube group: scalar trace 1, diagonal traceless D of dimension2, offdiagonal O of dimension3. Therefore A(0)|D=b I_D with b REAL, even though A need not be selfadjoint. Original source TT along k=e1 acts in D as orthogonal rank-one P_x|D, accepting v=diag(0,1,-1) and rejecting w=diag(-2,1,1). Bound ||A(0)-P_x||<=e+L=a therefore gives |b|<=a and |1-b|<=a. For a<1/2 contradiction. For 1/2<=a<1 b in [1-a,a] subset (0,1); its scalar idempotency defect obeys b(1-b)>=a(1-a), and eta_full>=|b²-b|. For eta_zero, compare A(0)^2-A(0) with A(theta_e1)^2-A(theta_e1). Their difference norm <=||A(0)-A(theta_e1)|| (||A(0)||+||A(theta_e1)||+1) <=L*(2*M+1). QED. This argument NEVER uses P_N(0); only the candidate polynomial's A(0).

## THEOREM 038.2 — EXACT asymptotically sharp Pareto frontier, including meanzero defect

For every FIXED e in [1/2,1), every odd N->infinity, and every integer radius sequence R_N=o(N):
  lim_N inf_{radius<=R_N, cube-equivariant, epsilon<=e} eta_full = e(1-e),
  lim_N inf_{radius<=R_N, cube-equivariant, epsilon<=e} eta_zero = e(1-e).

LOWER: apply T038.1 as R/N->0, so a->e, L->0; both eta >=e(1-e)-o(1).

CONSTRUCTIVE UPPER, valid already at EACH finite N and radius ZERO:
  Q=I6-Ptrace is the onsite rank5 ORTHOGONAL tracefree tensor projection.
  F_e=(1-e) Q.
It commutes with all 24 cube rotations and translations. At EVERY k!=0 source TT P_N(k) is an orthogonal subprojection of Q. Thus F_e-P has eigenvalues -e on TT, 1-e on the other tracefree polarizations, zero on trace. For e>=1/2, epsilon(F_e)=e EXACTLY. F_e²-F_e=-e(1-e)Q, hence eta_full=eta_zero=e(1-e) EXACTLY, with no source-specific asymptotic approximation.

At e=1 zero F yields defect0; e<1/2 is asymptotically infeasible for sublinear radius (already INT8 ROT035). For R=0 the exact minimax value e(1-e) holds at EVERY odd N due to T038.1 with L=0, NOT just in the limit. This is a sharp filter-design TRADEOFF, not a physical quantum/gravitational projector.

Sample exact e: .5=>.25; .6=>.24; .8=>.16; .9=>.09. Example finite FORMULA evaluation only (NOT a N^3 simulation) N=10001 R=1 e=.6: M=1.602516976082, L=.001006790433, full eta lower .239797628286; meanzero eta lower .235564040334, onsite upper .24. For e=.5 the finite full lower .249999109117 and upper .25. For e=.8 full lower .159319133586 and upper .16. All source-scoped.

## Independent actually executed controls and negative knowledge
MAIN STANDALONE NumPy script:
 - 30 cubic-equivariant tracefree-scalar stencil constructions: 18 onsite e=.5/.6/.8 at N3,5,9,15,31,41 and 12 radius-one symbols lambda(k)Q=cQ+t*sum_i(cos(2*pi*k_i/N)-1)Q at N9,15,31,41, two signs and three parameter choices;
 - on ALL nonzero k for those tested finite N, exact scalar eigenvalue error and defect computed; the source P_N(k) is a subprojection of Q for k!=0, not an assumed physical field;
 - 63 analytical finite-radius Bernstein certificates across N31,41,101,401,1001,10001,1000001, R0/1/3 and e=.5/.6/.8; N>41 here ONLY formula evaluation, not huge lattice execution;
 - direct 6x6 symmetric tensor projectors at 4 directions and five tracefree witness scalings;
 - SHA-verified literal ORIGINAL helper apply_P_TT on TWELVE independent cosine inputs at N5,9,15: true TT diagonal, TT yz, traceless longitudinal, pure trace; projector and onsite idempotency .24/0 checks PASS, original helper unchanged. No original runtime, no historical K_A.

SECOND COMPLETELY INDEPENDENT SOURCE-FREE SymPy exact-rational audit:
 - 24 proper cube rotations, 864 rational commutator equations on arbitrary 6x6 fiber endomorphism, matrix rank33 and commutant dimension3, exact invariant projectors dimensions1+2+3;
 - rank2 x-axis TT, rank1 compression on diagonal traceless D, explicit accepted/rejected tensors;
 - rational onsite epsilon e=1/2,3/5,4/5,9/10; F_e²-F_e = -e(1-e)Q and exact output eigenvalues;
 - exact polynomial factorization b(1-b)-a(1-a)=(a-b)(a+b-1).

NEGATIVE KNOWLEDGE: first SymPy run FAILED due to incorrect SIGN inside the last symbolic factorization ASSERT, NOT to a defect of the stated inequality. Corrected that assertion, reran the complete exact audit, PASS. The FIRST FAILED run is not passed off as certified.

## Repro custody
Moderator-local complete 8-member ZIP:
  iw_int8_rot038_robust_idempotency_frontier_repro_bundle.zip
 SHA256 **b672e25edfa0e465d0d6ee76ac10c220515cd8d8e570c6ccd5742cb7fd314bb1**
Contains full 10.5KB Polish report, two standalone executed Python programs, two frozen JSON results, README, runlog, SHA256SUMS. ZIP CRC PASS, SHA256 7/7 payloads PASS. Two clean extracted replays:
- with original SHA-checked helper, both JSON files BYTE IDENTICAL to archive.
- helper absent, exact audit JSON BYTE IDENTICAL; numerical math equal and source status explicitly SOURCE_SKIPPED_NO_HELPER.
Original source helper not redistributed. Neither standalone Python file is falsely claimed separately uploaded to GitHub.

## Epistemic STOP
All theorems are FINITE ODD flat raw-k TT DTC0a, full real Sym² but meanzero L2 approximation, 24 cube stabilizer, translation invariant matrix-valued stencil, idempotence norm. No even-N realcast, no original production runtime, no h=fI historical masked KA, no arbitrary curved York, no Lorentzian Box, no Noether/GR gauge, no J3/K physics and no empirical discovery. Source-owner acceptance, independent referee, BW ingest and Moderator EXEC are unverified and PENDING. No new task cascade.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
