---
artifact_id: IW_INT8_ROT014_EXACT_CONTINUUM_TT_PROJECTION_LIE_COMMUTATOR_NONCLOSURE_FINITE_FOURIER_WITNESS_001_20261023
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
date: 2026-10-23
problem_id: P3_DTC0A_TT_TARGET_DOMAIN_AND_PROJECTED_LIE_REPRESENTATION_001
document_type: EXACT_FOURIER_ANALYTIC_COUNTEREXAMPLE_AND_INDEPENDENT_GRID_REPRODUCTION
exposure: PUBLIC
canonical_path: research/int8/2026-10-23/iw_int8_rot014_exact_continuum_tt_projection_lie_commutator_nonclosure_finite_fourier_witness_001.md
status: EXACT_RATIONAL_FOURIER_COEFFICIENTS_AND_SPECTRAL_NUMERIC_PASS / HISTORICAL_RUNNER_UNAVAILABLE / REFEREE_PENDING
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: MATURE_HOST_SPECIALIZATION / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_J3_K_INVARIANT
---

# INT8 ROT014 — exact nonzero projected Lie commutator on an initial TT tensor, even with continuum/spectral derivatives

## 0. Why this is a distinct science iteration

Currentness refresh: as of 2026-10-23:
- INT8 ROT013 isolated a central-difference Leibniz violation as a genuine source of UNPROJECTED K_C on selected E=I pure-trace fields; that deliberately had K_A=K_B≈0 and was NOT a causal explanation for archived K_A.
- XH-S4 ROT019 already numerically controlled *the actual frozen smooth project-field source*: replacing central derivatives by exact FFT spectral derivatives when alpha=0 makes K_C≈0 while K_A stays about 3.84158e-5 (pure trace input) or 3.32154e-5 (a distinct nonzero TT test). At alpha=.05, E != I can separately affect the closure residual. This observation belongs to XH-S4, NOT a new INT8 numerical discovery:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s4/2026-10-23/IW_XH_S4_DTC0A_TT_DOMAIN_SPECTRAL_DERIVATIVE_AND_COMMUTATOR_HOST_AUDIT_019_20261023.md
- XH-S4 ROT018 gave the exact source-operator identity K_A-K_B=P L2 Q L1-P L1 Q L2, and demonstrated initial benchmark h=fI is PURE TRACE, not a TT input:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s4/2026-10-23/IW_XH_S4_DTC0A_PROJECTION_INSERTION_TRACE_INPUT_AND_STENCIL_HOST_AUDIT_018_20261023.md
- Geeky-S10 gave the exact P/Q BLOCK identity and TT-sector bound ||(K_A-K_B)P|| <= 2||[P,L1]||||[P,L2]||; this is prior source material:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s10/2026-10-23/geeky_s10_tt_projection_insertion_block_leakage_theorem_001.md
- M13 ROT023 functionally recreated 99/99 archive RMS values using retained helper and explicitly did NOT recover byte-exact historical runtime or physical K/J3. No owner ingestion, review or physical upgrade follows:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-23/IW_M13_ROT23_DTC0a_full_functional_replay_mask_TT_001.md

**Distinct narrower delta**: prove a fully explicit CLOSED-FORM Fourier counterexample, with exact rational coefficients and exact nonzero RMS, in which the INPUT is genuinely TT, the derivative is the CONTINUUM differential operator (or spectrally exact for all resolved modes), and the UNPROJECTED Lie representation identity holds EXACTLY. The full computed failure is *solely* the intermediate fixed TT projection. This removes trace-input, stencil truncation, moving mask, and E_lin as explanations for this particular witness. It is a mature algebraic fact about non-invariant subspaces, not NASH gravity or a novel physical anomaly.

## 1. Model, operators and nonphysical boundary

Flat periodic 3-torus T³=(R/2piZ)³ with coordinates (x,y,z). Real smooth symmetric covariant rank-two tensors H_ij. Fix a background Euclidean metric solely to define the global Fourier TT orthogonal projector P. For nonzero Fourier mode k, write
  P_k=I-kk^T/|k|²,
  Pi_k(H)=P_k H P_k-(1/2)P_k tr(P_k H).
At zero mode use the retained helper's tracefree convention; no output mode in the witness has k=0.

For vector field C define the classical covariant tensor Lie derivative
  (L_C H)_ij=C^m partial_m H_ij + H_mj partial_i C^m + H_im partial_j C^m.
Bracket [C1,C2]^i=C1^m partial_m C2^i-C2^m partial_m C1^i.

Let E=Identity (alpha=0, no E_lin insertion). Define:
  K_C = [L_C1,L_C2]H - L_[C1,C2]H,
  K_B = P K_C,
  K_A = P L_C1 P L_C2 H - P L_C2 P L_C1 H - P L_[C1,C2]H.

As classical differential geometry requires, [L_C1,L_C2]=L_[C1,C2] on ALL smooth covariant tensors, so K_C=K_B=0 exactly, before numerical discretization.

With Q=I-P and the above exact continuum closure:
  K_A=P L_C2 Q L_C1 H - P L_C1 Q L_C2 H. (1.1)
This is XH-S4/Geeky prior algebra specialized to E=I. The new work supplies a minimal exact NONZERO, initially TT witness.

This uses a FIXED Euclidean background projection, not an equivariantly transported projector or covariant gauge-invariant gravity observable. Source readback does not authorize any such interpretation.

## 2. All-smooth real low-band witness

Set
  C1=(cos x,0,0),
  C2=(0,cos x,0),
  H=diag(1,-1,0) cos z.                              (2.1)

For every Fourier mode k=±(0,0,1) of H: H is symmetric, tracefree, k^i H_ij=0. Therefore
  P H=H exactly.                                  (2.2)
In contrast to the historical DTC standard puretrace input, this test is in the ACTUAL TT input subspace.

All products and brackets contain only x-frequencies -2,0,2 and z-frequencies ±1, so a spectral derivative and Fourier projector on any odd N≥7 grid reproduce the continuum function without aliasing. No high-band assumption, moving mask or domain mismatch occurs in the test.

## 3. Explicit one-mode tensor calculation

For complex plane waves
  C(x)=a exp(i p·x), H(x)=H0 exp(i q·x),
the Fourier amplitude of the covariant Lie action at p+q is
  T_{p,a;q}(H0)=i[(a·q)H0+p(H0 a)^T+(H0 a)p^T].    (3.1)
This is a direct substitution into the source tensor Lie formula; no generalized-geometry theorem.

For two plane-wave vector fields with (p,a) and (r,b), the bracket has Fourier amplitude at p+r
  i[(a·r)b-(b·p)a].                                (3.2)

Choose
  q=e_z, H0=diag(1,-1,0),
  p=r=e_x, a=e_x, b=e_y.                           (3.3)

Use (3.1) twice with projector at the actual intermediate wavevectors, and (3.2) in the bracket channel. For the THREE unmixed complex input waves of unit amplitude, the output coefficient at k=(2,0,1) is exactly
  M=[[0,-1/10,0],[-1/10,0,1/5],[0,1/5,0]].     (3.4)
The continuous unprojected closure coefficient at the same mode vanishes.

In the REAL cosine witness (2.1), each of the three positive-frequency input coefficients is 1/2, so
  K_A_hat(2,0,1)=M/8
  =[[0,-1/80,0],[-1/80,0,1/40],[0,1/40,0]].     (3.5)

For the other nonzero Fourier coefficients, all EXACT rational entries are:
  at k=(0,0,±1):
    K_A_hat=[[0,1/8,0],[1/8,0,0],[0,0,0]];
  at k=(±2,0,+1):
    K_A_hat=[[0,-1/80,0],[-1/80,0,1/40],[0,1/40,0]];
  at k=(±2,0,-1):
    K_A_hat=[[0,-1/80,0],[-1/80,0,-1/40],[0,-1/40,0]].
No other Fourier coefficients occur. These exact expressions were derived by elementary sympy rational matrix arithmetic and checked by an independently implemented FFT tensor-Lie calculation.

Parseval, using the full unweighted spatial mean of tensor Frobenius squares, yields
  mean_x ||K_A(x)||_F²
    =2*(1/32)+4*(1/640)
    =11/160.                                        (3.6)
Thus
  RMS_F(K_A)=sqrt(11/160)=0.262202212042537..., (3.7)
while
  RMS_F(H)=1
and
  K_C=K_B=0 exactly.

The RMS is WHOLE-PERIODIC GRID and NOT masked, not divided by sqrt(6), not source-normalized to historical h. No numerical scalar from this artificial witness may be compared directly with archived 3.76e-5 K_A.

## 4. Independent actual spectral finite-grid test

A separate NumPy source-style tensor Lie implementation uses FFT differentiation in all three coordinates, a vectorized Fourier Pi_k on all rank-2 symmetric tensor components, and the exact vector-field Lie bracket. It does NOT use the sympy rational-mode code to compute the result, except for comparing the predicted known rational Fourier target.

Results:
| odd N | max |P H - H| | max |K_C| | RMS_F(K_A) | max error in K_A_hat(2,0,1) |
|--:|--:|--:|--:|--:|
| 9 |3.33e-16|2.22e-15|.2622022120425375|3.45e-17|
|11 |2.22e-16|4.16e-15|.2622022120425380|2.86e-17|
|17 |3.33e-16|1.21e-14|.2622022120425377|2.21e-17|
|31 |4.44e-16|2.50e-14|.2622022120425376|2.85e-17|

All computed projected components match expected exact Parseval/RMS and Fourier coefficient, while every unprojected Lie commutator residual is at floating point roundoff. The phase-space norm is independent of N after mode resolution; this is not a finite-stencil convergence test.

## 5. Precise interpretation and cheapest source discriminator

The fixed globally defined TT subspace is NOT invariant under general variable-coordinate Lie transports. Compressing an exact Lie algebra action onto a non-invariant subspace, while re-inserting P after each operation, need not define a representation. Accordingly,
  UNPROJECTED_CONTINUUM_LIE_CLOSURE = TRUE
and simultaneously
  INTERMEDIATE_FIXED_TT_PROJECTED_CLOSURE = FALSE
can hold, even on an initial TT tensor and with exact Fourier differentiation.

That is a legitimate mathematical counterexample; it does NOT establish that a physical graviton gauge sector, general covariance, or an authentic NASH invariant fails. One would need to specify a dynamically transported TT decomposition, connection/background, actual physical field domain, and source-valid target before such a question has a meaning.

In relation to the archived DTC0a data:
- XH-S4 ROT019 ALREADY found the spectral derivative replacement made K_C~0 but K_A finite at alpha=0 in its source fields. The present exact low-mode witness establishes this phenomenon in algebra with a known continuum value and genuine TT initial state, not just in a floating-point smooth testcase.
- XH-S4 ROT018's source-driven K_A excess from projector insertion remains the relevant owner result; this is a simpler explanatory countermodel, NOT a quantitative reconstruction of the original plateau.
- INT8 ROT013 central difference Leibniz error is an independent mechanism that can produce K_C when source derivatives are central; it vanishes identically in THIS spectral test.
- INT8 ROT008/012 k-versus-delta projection mismatch is absent because all transport derivatives in THIS witness use the spectral i*k symbol.
- M13 ROT023 reproduced 99/99 archival RMS with the helper, and the historical runtime remains BYTE-UNAVAILABLE; this new witness makes no original-executor claim.

Cheapest falsifier for a contrary claim:
  For one actual submitted projected-Lie physical claim, precisely define whether fixed flat Fourier TT is intended to represent a true invariant Lie module. If yes, (2.1)-(3.7) disprove that mathematical statement. If instead P must transform with background and frame, this countermodel is the wrong carrier; explicit moving-P law is required before comparison.

## 6. One problem / one state, owner and custody

problem_id: P3_DTC0A_TT_TARGET_DOMAIN_AND_PROJECTED_LIE_REPRESENTATION_001
best_result: exact all-rational spectral coefficient and sharp nonzero continuum RMS on a genuinely TT input, with analytic K_C=0 and independent spectral FFT checks.
prior_hosts: elementary compression non-representation of Lie algebra actions, Fourier TT/Leray projectors, XH-S4 ROT018/019 source operator identities and prior actual spectral tests, Geeky-S10 block leakage theorem.
counterresult: no continuum operator closure defect if the TT subspace is invariant under the selected fields, but current source variable C does not guarantee invariance; mathematical K_A here survives continuum but has no physical invariant semantics.
owner: LT5 for abstract theory chapter, M13 for DTC numerics, KN11 source/BW; INT8 only independent scientific integration.
independent_referee: NOT_PERFORMED.
blocker: source-validated physical tensor space and background-equivariant P missing; original archived code bytes missing; no legitimate continuum physical observable, interpretation or execution.
cheapest_test: verify exact Fourier data (2.1)-(3.7) in existing source-defined operator interface, with spectral derivatives and alpha=0 only; classify the target as fixed-P abstract representation, not physical NCDG.
decision: PASS exact mathematical counterexample; STOP any inference that this K_A must be a discretization error; HOLD all physical J3/K and historical executor claims.
canonical_path: research/int8/2026-10-23/iw_int8_rot014_exact_continuum_tt_projection_lie_commutator_nonclosure_finite_fourier_witness_001.md
bw: GITHUB_PENDING_BW_INGEST
no_new_owner_task: true

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_TASK_CASCADE.
