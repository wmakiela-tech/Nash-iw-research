---
artifact_id: IW_INT8_ROT008_DTC0A_FOURIER_TT_VS_FINITE_DIFFERENCE_DIVERGENCE_SYMBOL_GAP_001_20261023
problem_id: P3_DTC0A_TT_DISCRETE_SYMBOL_COMPATIBILITY_001
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
date: 2026-10-23
document_type: EXACT_DISCRETE_SYMBOL_COUNTEREXAMPLE_AND_SOURCE_LOCAL_DIAGNOSTIC
exposure: PUBLIC
canonical_path: research/int8/2026-10-23/iw_int8_rot008_dtc0a_fourier_tt_vs_finite_difference_divergence_symbol_gap_001.md
status: ANALYTIC_PASS_AND_SYNTHETIC_HELPER_REPLICATION_PASS / HISTORICAL_DTC_RUNTIME_NOT_REBUILT / INDEPENDENT_REFEREE_PENDING
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 ROT008 — Fourier-TT projector vs central finite-difference divergence: a source-local symbol mismatch

## 0. Currentness and problem choice

Moderator-accepted science programme, 2026-10-22: P2 LT/source-host consistency and P3 typed DTC validation, with no physics claims. By 2026-10-23 Geeky-S10 had already published a stronger equivalent of INT8 ROT007's finite-dose mixed-reset Gaussian sensitivity bound. That question is covered by its owner result, so this rotation does NOT repackage that result as new. INT8 role here is scientific integration of the DTC source-local numerics and their mathematical certificate types.

M13 ROT18 had already identified moving physical masks; M13 ROT19 had already established algebraically rank-one amplitude sweeps, field-class contrasts and a NOT_IMPLEMENTED fourth-order test in v0.3.1. We do not claim these as fresh.

**Distinct problem:** The retained DTC0a helper calculates the tensor TT projection in Fourier space using raw Fourier wavevector k, while the Lie derivative and brackets differentiate sampled fields by a central finite-difference stencil. Does a nearly machine-zero **Fourier k-transversality** test imply discrete divergence with that actual stencil is nearly zero? NO, even in a single exactly resolved Fourier mode and with a perfectly functioning Fourier TT projector.

This is a *definition/commuting-operator mismatch*, not an observed failure of projector idempotence or physical tensor theory.

## 1. Source carriers and strict provenance

Inspected locally provided files:

- `deepseek_python_20260627_a87249.py`, SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`, contains `derivative(order=2)` and `apply_P_TT` with `np.fft.fftfreq(N,d=dx)`, `P=I-kk^T/|k|²`, `PHP - 0.5 P tr(PH)`. It **rejects order != 2**.
- `deepseek_python_20260627_349584.py`, SHA256 `2fd77da6b2501d957fabf8884a2625bbafedf594399e720360e83caa344938c5`, is a distinct **Phase 1b / v0.3.2-stub helper** implementing fourth-order central derivative and a separate fourth-order second derivative branch. Its existence does **not** establish that a fourth-order *historical DTC0a v0.3.1 run* occurred.
- `dtc0a_stencil_order_claim_audit_v0_3_1.csv` reports three expected NotImplementedError rows; `dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv` and associated manifests are archived outputs, not recreated in this rotation.
- Historical declared runtime `dtc0a_runtime_v0_3_1.py`, published source hash `2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084`, is **not** byte-available as that source in this context. Do not identify either helper with that historical runtime.

M13 provenance audit: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-23/IW_M13_ROT19_DTC0a_control_independence_and_field_class_001.md

This is a source-local check of available helper semantics and a standalone mathematics test. It is NOT an original-runtime replay, not a recomputation of K_A/K_B/K_C, not a continuum NCDG claim.

## 2. Exact mathematical mismatch

On a periodic cube with grid spacing h=L/N, let a nonzero Fourier mode be indexed by `m=(m1,m2,m3)`, wavevector `k=2πm/L`.

The Fourier TT projector (at k!=0) is defined using `P_k=I-kk^T/|k|²` and maps a symmetric tensor `H` to
  `TT_k(H)=P_k H P_k - (1/2)P_k tr(P_k H)`.
It satisfies `k^T TT_k(H)=0`, tracefree, symmetry, and is idempotent in its own Fourier-symbol geometry.

The **actual centered second-order derivative** uses instead the Fourier symbol
  `D_{2,h}: exp(ik x) -> i delta_2(k) exp(ikx)`,
  `delta_2(k)_i=sin(k_i h)/h`.

In general `delta_2(k)` is NOT proportional to k when |k_i| differ. So
  `k^T TT_k(H)=0`
does **not** imply
  `delta_2(k)^T TT_k(H)=0`.

For the fourth-order centered derivative **only as the v0.3.2-stub branch**, the symbol is
  `delta_4(k)_i=[8 sin(k_i h)-sin(2k_i h)]/(6h)`,
which is likewise not generally parallel to k, although it has a smaller low-frequency discrepancy.

## 3. Exact single-mode tensor witness

Choose L=2π, `k=(p,q,0)`, p,q positive unequal integers strictly below Nyquist. Define perpendicular unit vectors
  `u=(q,-p,0)/sqrt(p²+q²)`, `v=(0,0,1)`.
The real symmetric tracefree polarization tensor
  `H_0=u u^T-v v^T`
satisfies
  `tr H_0=0,  k^T H_0=0,  TT_k(H_0)=H_0`.

Let `H(x)=cos(p x+q y) H_0`, sampled on the N^3 periodic grid. This is a single *exactly represented* Fourier mode; there is no nonlinear aliasing or unresolved-frequency input in the calculation.

The second-order discrete divergence obeys
  `D_{2,h}\cdot H(x)=-sin(p x+q y) delta_2(k)^T H_0`,
with exact whole-grid RMS
  `RMS(D_{2,h}\cdot H)=||delta_2(k)^T H_0||/sqrt(2)`
  `=|q sin(p h)-p sin(q h)|/[h sqrt(2(p²+q²))]`.

The quantity is nonzero whenever `q sin(ph) != p sin(qh)`, notwithstanding exact spectral TT projection.

For fixed p,q as h->0,
  `||delta_2^T H_0|| = |p q (q²-p²)| h²/[6 sqrt(p²+q²)] + O(h⁴)`.
With centered fourth-order,
  `||delta_4^T H_0|| = |p q (q⁴-p⁴)| h⁴/[30 sqrt(p²+q²)] + O(h⁶)`.

**No uniform high-frequency implication:** choose modes with p/N and q/N approaching distinct fixed fractions in (0,1/2), e.g. (1/4,1/3). Then the relative symbol defect
  `||delta_2^T H_0||/||delta_2||`
approaches a nonzero constant
  `|b sin(2πa)-a sin(2πb)|/[sqrt(a²+b²) sqrt(sin²(2πa)+sin²(2πb))]`,
a=p/N, b=q/N. Hence the low-frequency O(h²) relation is not an operator-norm-uniform statement across the full discrete Fourier band.

These are ordinary discrete Fourier/spectral-vs-finite-difference facts, not a novel theorem family.

## 4. Synthetic checks against source-local projector geometry

A standalone NumPy program reconstructs the precise FFT projection multiplier used by the inspected order2 helper (including its zero-mode tracefree branch), and independently applies second-order or exploratory fourth-order centered differences.

| N | Fourier mode | stencil | relative TT-projection error | stencil divergence RMS | relative symbol defect |
|--:|:--|:--:|--:|--:|--:|
|31|(1,2,0)|2|5.36e-16|0.0128579429|0.0083241|
|41|(1,2,0)|2|5.59e-16|0.0073831325|0.0047321|
|31|(1,2,0)|4*|5.36e-16|0.0005228138|0.0003309|
|41|(1,2,0)|4*|5.59e-16|0.0001723783|0.0001090|
|31|(7,10,0)|2|2.65e-15|1.0289218808|0.2208640|
|41|(9,13,0)|2|2.89e-15|1.3276983609|0.2146877|
|31|(7,10,0)|4*|2.65e-15|0.9656174879|0.1506862|
|41|(9,13,0)|4*|2.89e-15|1.2071148274|0.1428779|

(*) order4 here is a synthetic finite-difference countercontrol matching the separate v0.3.2 stub symbol, NOT a successful DTC0a order4 pipeline.

All eight synthetic cases reproduce the **exact analytic RMS formula** to <1e-10 and give a TT projection reconstruction error <1e-12. In a separate source-helper-local run of `apply_P_TT` directly from `deepseek_python_20260627_a87249.py`, the same tensor modes likewise reproduced the exact analytic discrete divergence (PASS). Numerical tests corroborate, not establish, the analytical identity.

## 5. Consequences: three different TT meanings and how to test them

(A) `FOURIER_SPECTRAL_TT`: `k^T Hhat(k)=0` after `P_TT(k)`. This is the projector's *actual* stated guarantee. FFT Fourier-transversality PASS is appropriate to this definition and does not become wrong.

(B) `FINITE_DIFFERENCE_TT`: `delta_2(k)^T Hhat(k)=0`. It does NOT follow from (A). The witness shows material leakage even when (A) is at machine precision.

(C) `PHYSICAL_CONTINUUM_TT`: would require a source-valid continuum limit, field class/control, domain-consistent norms, spectral regularity, and independently typed physical transport. Neither (A) nor (B) alone establishes (C).

The **cheapest discriminating numerical test**, should DTC owners choose to run it, is to compute BOTH FFT spectral divergence `||k_i Hhat_ij||` and discrete-stencil divergence `||D_{2,h,i}H_ij||` on exactly the same frozen field/tensor/mask, with the same physical norm convention. Use at least two Fourier modes: (1,2,0) and one high-band but sub-Nyquist noncollinear pair; repeat with a fixed *physical* comparison domain and avoid the moving-mask ambiguity. This is not a request to relabel prior PASS as FAIL or to infer that K_A plateau is thereby explained.

**Repair options are type-dependent, not interchangeable**:
1. If the target complex uses *spectral* derivatives, replace relevant finite-difference Lie/connection derivatives with a consistent spectral/symbol calculus, then audit aliasing and nonlinear products. This is more than changing a projector.
2. If the target complex uses the *central difference* divergence, construct a projector using the symbol `delta_2(k)` instead of k (where `delta_2!=0`), with explicit zero-symbol and Hermitian-reality handling. This is a different discretization. In particular EVEN N has Nyquist modes with `delta_2=0` at nonzero k; it requires a declared treatment rather than pretending all nonzero k are regular.
3. A fourth-order stencil can reduce smooth low-frequency leakage to O(h⁴) but does not provide uniform all-band compatibility, and no v0.3.1 full order4 output is established by the available inputs.

This explanation is consistent with M13 ROT18 moving-mask and ROT19 control-rank findings but does not duplicate them.

## 6. External/mature-host comparison

This is standard Fourier multiplier, centered difference symbol and discrete Helmholtz/Leray projection compatibility mathematics. External host for spectral projection definition (NOT equivalence to NASH tensor model): standard Leray Fourier multiplier P=I-kk^T/|k|², e.g. the source discussion in Journal of Dynamics and Differential Equations, "The Navier–Stokes Equation with Time Quasi-Periodic External Force: Existence and Stability of Quasi-Periodic Solutions" (published 2021): https://link.springer.com/article/10.1007/s10884-021-09944-w. Spectral Leray projection under Fourier derivatives is a *different operator contract* from divergence computed with centered finite differences. No new mathematical priority asserted.

## 7. Problem-state record (MT13 one-problem-one-state)

problem_id: P3_DTC0A_TT_DISCRETE_SYMBOL_COMPATIBILITY_001
best_result: exact mathematical 1-mode counterexample and eight standalone synthetic controls.
counterresult: low-frequency leakage decreases with stencil order and h; spectral TT itself remains correct in its own k-complex.
source: inspected two 2026-06-27 helper scripts with SHA256 above, frozen CSV context, M13 ROT18–19 full reports.
owner: M13 (DTC numerical/source validation), KN11 (BW source custody), LT5 (theory integration); INT8 contributes only typed operator bridge.
independent_referee: NOT_PERFORMED.
blocker: historical original `dtc0a_runtime_v0_3_1.py` unavailable byte-exact; no owner-run matched stencil-vs-Fourier divergence pair or source-valid continuum claim.
cheapest_test: frozen tensor: Fourier k-divergence vs actual stencil D_h-divergence, same grid/mask, low and high wave modes.
decision_rule: PASS as *symbol mismatch in helper/math*; HOLD actual K_A/K_B/K_C physical implication or historical runtime claim until source and matched tests; REPAIR if downstream documentation equates Fourier TT PASS with discrete-stencil TT PASS.
no_direct_owner_task: true
canonical_path: research/int8/2026-10-23/iw_int8_rot008_dtc0a_fourier_tt_vs_finite_difference_divergence_symbol_gap_001.md
bw_ingestion_state: GITHUB_PENDING_BW_INGEST

NO_NEW_TASK_CASCADE / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
