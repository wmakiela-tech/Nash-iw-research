---
artifact_id: IW_GEEKY_S12_ROT001_TRANSPORT_REACHABLE_ELIN_GROWTH_FALSIFIER_001_20261111
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
date: 2026-11-11
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_FINITE_SCALAR_AUXILIARY_FOURIER_FALSIFIER / NO_TENSOR_TT_INFERENCE / NO_HISTORIC_PRODUCER / NO_PHYSICAL_UPGRADE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
science_status: AUTHOR_DERIVED_EXACT_PROOF_WITH_STDLIB_NUMERIC_CHECK / REFEREE_PENDING / OWNER_ADOPTION_PENDING
---

# Geeky-S12 ROT001 — stable starting modes do not imply stable transport-reachable modes

## 0. One-question return

**Question.** If the source-like 3D filter E_alpha=I+alpha*h^2*Delta_2 damps every Fourier mode of the initial field, can a *norm-preserving* source-distinct transport transfer that field into an E-amplified spectral band?

**Answer in a declared scalar auxiliary toy:** YES. At N=7, alpha=1/5, a real divergence-free centered-difference advection field has a nonzero unstable Fourier component after exactly five Lie-generator applications. For the norm-preserving group exp(tL), that component is nonzero for sufficiently small nonzero t, so repeated post-transport filtering E^m causes unbounded L2 amplification. This is an exact finite-dimensional mathematical counterexample to a GENERAL source-support-to-transport-support stability inference, **NOT** a counterexample to the original DTC0a (0,cos x,0) tensor source, its TT projection, its historic masks, or physical NCDG.

**Practical decision changed:** distinguish initial-source spectral support from the transport-invariant *reachable spectral support*. An all-mode E failure does NOT itself disprove source-native restricted contraction; conversely source-only E tests do NOT certify arbitrary transport insertions.

## 1. Source and mature-host subtraction before the new question

**Internal firstness.** INT9 ROT009 (2026-11-10), source-authoritative public report [INT9 spectral threshold](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/int9/2026-11-10/iw_int9_rot009_dtc0a_elin_alpha020_global_l2_noncontraction_and_historic_source_gate_001.md) FIRST proves for the separate literal auxiliary helper E_lin:
q_alpha(k)=1-4alpha*sum_{j=1}^3 sin^2(pi*k_j/N).
For historical odd N=31..41, alpha=0.2 is globally noncontractive, but low Fourier modes are attenuated. INT9 ROT010 separately studies source-*reachable* contraction: this report does NOT rename either result as its discovery. Geeky-S11 ROT015-023 FIRST developed genuine even-grid B=GA and two-step projected Lie leakage; ROT027-034 investigated filtered insertion/order; S11 ROT044 inverse is restricted; ROT050 interpolation/analytic model limits. Geeky-S10 and XH previously identified projection insertion block leakage. None is a physical or canonical output by inheritance.

**External mature hosts checked** (search performed 2026-11-11): classical von Neumann/Fourier multiplier stability; variable-coefficient spectral filtering and noncommuting time splitting, including *Spectral Methods for Hyperbolic Problems* (2001; https://doi.org/10.1016/S0377-0427(00)00510-0), Christon–Voth–Martinez *Generalized Fourier Analyses of Semi-Discretizations of the Advection-Diffusion Equation* (Sandia 2002, https://www.sandia.gov/research/publications/details/generalized-fourier-analyses-of-semi-discretizations-of-the-advection-diffu-2002-11-01/), and Ostermann–Schratz *Stability of Exponential Operator Splitting Methods for Noncontractive Semigroups* (SIAM JNA 2013; https://doi.org/10.1137/110846580). Orthogonal projection/hidden-mode transfer is also classical in Mori–Zwanzig reduced dynamics (e.g. https://doi.org/10.1098/rspa.2017.0385). This is an elementary exact finite example in a mature mathematical setting. **No novelty inference.**

The original auxiliary source uses three-term tensor Lie action, original E_lin, and source-specific C=(0,cos x,0); historical masked producer bytes not recovered. Here E is symbol-matched but the transport is a declared *different scalar toy*. Neither the origin nor projected full K_A is claimed to have been rerun.

## 2. Precisely typed finite toy

Let H be real grid fields on (Z/7Z)^3, h=2*pi/7, with normalized counting L2 norm and complex discrete Fourier basis e_k(n)=exp(2*pi*i*k·n/7). Let D_j be the second-order periodic centered first difference:
D_j f(n)=[f(n+e_j)-f(n-e_j)]/(2h).
Let Delta_2=sum_j [f(n+e_j)-2f(n)+f(n-e_j)]/h^2.
Set E=I+(h^2/5)Delta_2, diagonal in Fourier with q(k)=1-(4/5)*sum_j sin^2(pi*k_j/7).

Choose **different, real divergence-free** transport velocity
C(n)=(cos(x_z),cos(x_x),cos(x_y))
and L=M_cos(z) D_x + M_cos(x) D_y + M_cos(y) D_z.
C_j is independent of its differentiated coordinate x_j; hence M_Cj commutes with D_j, and D_j*=-D_j. Consequently **L*=-L** exactly in normalized discrete L2, and U(t)=exp(tL) preserves norm for every real t.

Choose real f(n)=cos(x_x+x_y+x_z). Its only Fourier modes are ±(1,1,1), coefficient 1/2 each, and q(1,1,1)=0.5481877622304803, so ||E^m f||=0.5481877622304803^m ||f||.

## 3. Exact theorem — first escape at transport depth 5

For the above toy define the expanding mode set S+={k: |q(k)|>1}. Then:

1. No Fourier component of L^r f lies in S+ for r=0,1,2,3,4.
2. The coefficient of L^5 f at k*=(3,3,2) is NONZERO; its source is the initial positive Fourier mode, via 30 distinct orderings of two +x, two +y and one +z shifts.
3. q(k*)=-1.009783467904461, so ||E^m L^5 f|| diverges as m→infinity. In particular
||E^m L^5 f|| >= sqrt(2)*|hat(L^5f)(k*)|*|q(k*)|^m.
4. Since U(t) is exactly norm preserving and the analytic function t↦hat(U(t)f)(k*) has its FIRST nonzero Taylor derivative at order 5, it is nonzero for every sufficiently small t≠0. Thus even a NORM-PRESERVING finite transport step can access an E-amplified mode: ||E^m U(t)f||→infinity as m→infinity.

**Proof of (1).** A multiplication by each cosine shifts one Fourier index by ±1 (cyclic coordinates), with coefficient i*sin(2*pi*k_j/7)/(2h). On the seven-grid, sin²(pi*k/7) for absolute frequencies 0,1,2,3 equals 0, approximately .1883,.6113,.9505. The inequality sum>5/2 requires at least two absolute frequencies 3 and the remaining absolute frequency at least 2 (the least unstable multiset is (3,3,2)). From either all-1 or all-minus-1 starting corner, graph distance in one-coordinate steps to such a multiset is at least 2+2+1=5. Therefore r<=4 cannot reach S+.

**Proof of (2).** At five steps k* can be reached from +(1,1,1) only by positive coordinate increments (2,2,1); the negative starting mode cannot reach k* in five steps. Exactly 5!/(2!2!1!)=30 such paths exist. Along all these minimal paths, the relevant centered derivative frequency is in {1,2,3}, whose sin(2*pi*k/7) is strictly positive. Their complex phases are all i^5 and their positive magnitudes cannot cancel. The coefficient lower bound, including initial 1/2 and cosine factors, is
|hat(L^5 f)(k*)| >= 15*[sin(6*pi/7)/(2h)]^5 > 0.
Proofs (3)-(4) follow from Parseval and the convergent exponential series; lower-order Taylor coefficients for k* vanish by (1), fifth is nonzero. Note: no conclusion is asserted for every t; isolated zeros at other t are not excluded.

## 4. Independently executable arithmetic; not a proof substitute

The public stdlib reproducer uses exact finite Fourier support updates, explicit mode bookkeeping and analytic noncancellation assertions:
[Geeky-S12 ROT001 public reproducer](https://github.com/wmakiela-tech/Nash-iw-research/blob/a7378e79f0af4e4e4eee73bcb52c0ce5343f634f/research/geeky-s12/2026-11-11/iw_geeky_s12_rot001_transport_reachable_elin_growth_reproducer.py).

Local author run of a detailed stdlib variant produced:
- First support overlap with S+: r=5 (r<5: zero), mode coefficient |hat(L^5f)(3,3,2)|=0.2503579527911263.
- Elementary analytic amplitude lower bound 0.012370834869317617.
- ||L^5f||=8.407228111993478.
- For m=100,500,1000 respectively ||E^m L^5f|| ≈1.623538661785051,79.75632016614303,10372.733007476741.
- At t=0.5 a 32-term *numerical* Taylor check gives ||U(t)f||=0.7071067811865476 vs ||f||=0.7071067811865475 and |hat(U(t)f)(k*)|≈6.218002877194475e-05. Exact skew-adjointness and nonzero Taylor coefficient, not this numerical check, establish the theorem.
- Assertions passed for the local source-dependent implementation. Published GitHub script is a separately stored compact re-expression; its content readback was checked, but independent source-level rerun of the published bytes is NOT claimed here.

Mathematical source rule: a Fourier graph edge says only *possible* coupling; cancellation can still prevent a specific mode from appearing. The explicit 30-path same-phase proof, not graph reachability alone, licenses the positive witness.

## 5. Crucial negative source control

For the source-style **single** scalar transport C_src=(0,cos x,0), L_src=cos(x)D_y, only k_x changes; k_y and k_z remain exactly fixed. For the same f, the E-relevant invariant frequency fibre has k_y=k_z=±1. It therefore remains inside the |q|<=1 band, although E on the FULL 3D Fourier space is noncontractive. The maximum |q| on this fixed scalar fibre is:
- N=7: 0.6987918414869868
- N=31: 0.9836239530019956
- N=41: 0.9906243390242788

This is a **positive restricted stability example** and an important falsifier of the careless inference: "E globally unstable, so every source-reachable composition unstable." Source C_src and the NEW divergence-free C are different objects. For the source-like three-term tensor Lie, the x-only dependence also preserves transverse Fourier indices, but component mixing, TT B, and masks require fresh owner-specific tests; these scalar fibre numbers are not such tests.

## 6. What changes, kill test, and stop/reopen

**New candidate diagnostic:** TRANSPORT_REACHABILITY_SPECTRAL_GATE. Given a declaration of (source field spectral support, exact transport generators, E Fourier multiplier, projection/mask, legal operator order), compute the smallest invariant frequency carrier under all admitted transport steps and classify whether it intersects {|q|>1}. If no intersection and E is normal Fourier-diagonal, E is contractive on that carrier. If intersection exists, prove a NONZERO observed coefficient rather than just graph reachability, before claiming amplified output.

**Falsifier:** A projection/symmetry cancels every potentially expanding mode in the *actual legal* transport word, or the actual source transport preserves a stable invariant fibre. Such a result kills the proposed transfer from THIS toy to THAT source, even though the toy theorem survives.

**STOP:** Do not infer instability of literal historical full K_A, original masked h=fI, E at alpha=.2 in a physical model, or a general projector/gauge/L∞ failure. Do not turn this toy into an unrequested runtime campaign.

**REOPEN_IF:** A current source owner M14/INT9/KN13 or a scientific reviewer specifies a legal exact tensor/TT operator word whose initial source and transport-reachable spectral carrier cross the |q|>1 boundary, including an actual noncancelled output and exact producer identity if historical transfer is intended.

## 7. Custody, provenance and status

Chosen legal public scientific path: research/geeky-s12/2026-11-11/IW_GEEKY_S12_ROT001_TRANSPORT_REACHABLE_ELIN_GROWTH_FALSIFIER_001_20261111.md. Public compact code in the same directory. No private notebook/Drive locators or protected source bytes have been released.

GITHUB PUBLIC SCIENCE PRIMARY / source-local author proof + check; BW not edited here; GITHUB_PENDING_BW_INGEST (no event fabricated); independent referee pending; owner adoption pending; no task cascade or physical transfer. Delivery/receipt are separate from GitHub storage and will be reported separately.

**Final:** EXACT SCALAR AUXILIARY TRANSPORT-REACHABILITY COUNTEREXAMPLE PASS / SOURCE-SINGLE-C FIBRE STABILITY POSITIVE / HISTORIC TENSOR TT TRANSFER HOLD / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
