# XH-S4 — rotation 020: metric-dependent York projection, covariance and reproducibility repair
RETURN_ID: XH-S4-20261023-GEOMETRIC-COVARIANCE-TT-MOVING-PROJECTION-REPRO-AUDIT-020
DATE: 2026-10-23
CELL: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03 / XH-S4
RESULT: SOURCE-PRIOR-ART-SUBTRACTION / EXACT NATURALITY IDENTITY / TWO-FIELD FINITE FIRST-ORDER TEST / VERIFIED 019 PACKET / REPRO INTERFACE REPAIR
GUARDS: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_KJ3 / NO_NCDG_BACKGROUND_INDEPENDENCE / NO_CONTINUUM / NO_BW_INGESTION / NO_NEW_OWNER_TASKS.

## 1. Main theorem is standard geometric naturality, not an NASH discovery
For a compact boundaryless Riemannian manifold (M,g) with a well-defined orthogonal York decomposition, let P_g select the divergence-free and trace-free covariant rank-2 symmetric tensors in L2(g). Under a smooth diffeomorphism phi, carrying BOTH the metric and tensor, naturality is
  P_(phi*g)(phi*h) = phi*(P_g h).
Here phi* denotes pullback and preserves the appropriate **metric-changing** tensor Hilbert norms; for boundaries, zero modes and conformal Killing vectors extra domain/gauge choices must be fixed.
For flow phi_t of C and h_t=phi_t*h, differentiate t=0:
  (D_g P)[Lie_C g] h + P_g (Lie_C h) = Lie_C(P_g h),
thus
  (D_g P)[Lie_C g]h = [Lie_C,P_g]h.
For a pure trace h=f g, P_g(fg)=0 and Lie_C(fg) = (C·grad f)g + f Lie_C g, so
  (D_g P)[Lie_Cg](f g) = -P_g[f Lie_Cg].
The fixed-metric projected trace->TT source is canceled by the first-order **metric-dependent moving projection**. This does NOT state the code's K_A vanishes; the code fixes flat P and introduces E_lin, whose componentwise finite difference formula has no proved tensorial naturality with a moving metric.

## 2. Numerical experiment and exact error semantics
Using original **verified ZIP version** of XH018 source (user attachment IW_XH_S4_019_reproducibility_packet.zip), N=17 odd 3-torus, smooth source fields C1,C2 and h=f*I, central finite Lie:
  P_eps^(1) = P + eps [Lie_C,P],  h_eps^(1)=h+eps Lie_C h.
This is an **algebraic first-order conjugate projector**, not an independently computed curved York P_(g_t); P_eps^(1)^2=P_eps^(1)+O(eps²).
It obeys identically
  P_eps^(1) h_eps^(1) = P h + eps Lie_C(P h) + eps² [Lie_C,P](Lie_C h).
For the standard pure trace h, P h=0.

Computed unweighted global Frobenius/6 RMS:
C1, eps 0.1: fixed projection of moving field 1.995084382e-5, moving-projector defect 3.868651162e-7;
C1, eps 0.05: fixed 9.975421911e-6, moving error 9.671627904e-8;
C1, eps 0.025: fixed 4.987710955e-6, moving error 2.417906976e-8.
C2, eps 0.1: fixed 5.888410054e-5, moving error 2.959860418e-7;
C2, eps 0.05: fixed 2.944205027e-5, moving error 7.399651045e-8;
C2, eps 0.025: fixed 1.472102513e-5, moving error 1.849912761e-8.
Halving epsilon divides moving error by ~4 while fixed-projector trace contamination divides by ~2. The per-field [Lie,P] h + P Lie h error for pure trace was <=1.6e-35 in this finite setting; this is algebraic since P h=0. Projected FIRST stage h=fI is entirely trace-modulated tensorial strain: P(Lie_C h)=P[f(D_i C_j+D_j C_i)], while projected scalar advection vanishes to machine accuracy. Source archive XH019 had same first-stage result at N31 alpha=.05.

For a separate normalized nonzero TT input h_TT (global RMS 0.03535534), on N17, ||Q Lie_C1 h_TT||=0.00130238331315546 and ||Q Lie_C2 h_TT||=0.00133975508769834, matching ||[Lie_C,P]h_TT|| numerically. These are **single input** responses and not operator norm certificates.

## 3. Why the observed curvature is not automatically physical curvature
For source operators L_i=Lie_Ci◦E and P=P_TT fixed, XH018-019 derived exactly
  K_A-K_B = P L_2 (I-P) L_1 h - P L_1 (I-P) L_2 h.
For h=P h and source algebra with E=I and spectral no-alias differentiation, the above is a projected-connection obstruction from intermediate excursions out of the fixed TT subspace. It is analogous to second fundamental form / projected connection curvature in established subbundle geometry. It is NOT proof that physical spacetime curvature or NASH J3/K must be nonzero, nor a proof fixed flat TT projection should be covariant under arbitrary non-isometric diffeomorphism.
For E_lin=I+alpha dx²Δ_h on components, moving P alone does not establish full naturality. One would separately require a properly defined geometric E_g and E_(phi*g)(phi*h)=phi*(E_g h), with operator domain, inverse/retarded prescription if any, and metric dynamics declared.
Finite centered derivative does not reproduce exact continuum Leibniz for general modes; FFT spectral at N31 alpha=0 reduces source K_C to ~1.6e-18 while K_A remains ~3.84e-5 for trace input (XH019). Different residual types and test domains must not be merged.

## 4. 2026 original external science sources — actual content and nonmaps
[1] Leyla Ogurol, Tore Boybeyi, Bayram Tekin, "Perturbative Analytical Construction of Bowen–York Initial Data for Binary Black Holes up to Third Order in Spin and Linear Momentum", Fortschritte der Physik 74 e70136, FIRST PUBLISHED August 2 2026. Full open text https://onlinelibrary.wiley.com/doi/full/10.1002/prop.70136 . Sec4 uses conformal metric, conformal covariant derivatives, York tensor split A=A_TT+(L W), and exact vacuum momentum constraints. Host: GR black-hole initial constraints, not a DTC representation theorem.
[2] Trey Cole and David Vanderbilt, "Exact expression for the Berry connection in the projection gauge", Physical Review B 113,245106, June 1 2026, https://doi.org/10.1103/jh1y-x9nz . APS primary ABSTRACT read; projected Bloch-state gauge and Berry connection need coherent transport of subspace/frames; not the curved York projector. No full theorem assumptions independently audited.
[3] Ramesh Radhakrishnan et al., "Where are linearized gauge invariants encoded for plane waves in linearized gravity", EPJC 86 article1183, October19 2026. Full open article https://doi.org/10.1140/epjc/s10052-026-16355-y : Bardeen TT plane waves on fixed Minkowski vs NP/Cartan-Karlhede and translation Killing invariants; **explicitly flat linearized host only**. Its gauge-invariance conclusion does not license arbitrary curved/background NASH physical gauge claims.
[4] Marius Oancea, Thomas Mieling, Giandomenico Palumbo, "Quantum geometric tensors from sub-bundle geometry", Quantum 10 1965, Jan14 2026, https://quantum-journal.org/papers/q-2026-01-14-1965/ ; EARLIER PRIOR ART (original preprint March2025, outside requested new May date filter) showing projected connection, shape operator and generalized Gauss–Codazzi–Mainardi. Useful to subtract any apparent novelty of projected curvature mechanisms from NASH. DIFFERENT physics host.

## 5. New testable questions and stop rules
Q41 P0: Is intended transport fixed-background TT, or a moving metric-dependent subspace? Competing H_fixed vs H_moving, with distinct geometric and domain semantics. Test explicit original target statement and tensor reference metric before claims.
Q42 P0: Can an **independent** elliptic solver evaluate true P_(g_t) for pulled-back non-flat metric g_t and check P_(g_t)(phi_t*h)=phi_t*(P_g h) in matched L2(g_t) norm? NOT DONE. Current algebraic P+t[L,P] is a first order consistency test only.
Q43 P0: Can E_g be made natural simultaneously with P_g under the same pullback? If not, which source-level finite stencil/zero-mode assumption fails? Need compare E_(phi*g)(phi*h) vs phi*(E_g h) and source tensor norm. NOT DONE.
Q44 P1: Under source-native projected connection conditions, which blocks P L Q / Q L P produce geometric curvature vs discretization curvature? Requires ideal underlying Lie representation (check K_C first), operator bounds and source-target semantical alignment, not a physical J3 invariant.
Q45 P0: Does GitHub readback PASS imply executable reproducibility? NO. Historic GitHub019 self-contained script referenced m.derivative/m.smooth/m.E_lin/m.tt while paired GitHub018 used m.der/m.Ptt/m.E and no smooth, so its initial GitHub version was incompatible even though both blobs read back. VERIFIED original 019 ZIP (extracted and both scripts executed in clean directory; numbers match). In this rotation GitHub019 Python script patched with a compatibility adapter, new commit ebefab7059d67d122f0273e7077168ab587db905, blob31bfd5c76e6305f6dc12aace78b04bf91fc47182; readback must be distinguished from independently rerunning exact post-patch remote bytes. Original GitHub commit preserved. New ZIP20 contains the **ACTUALLY EXECUTED** 018 base, 019 scripts/JSON, 020 script/JSON and this analysis.
STOP: no BW ingestion, no canon/EXEC, no continuum limit or physics upgrade, no inference of metric background independence absent actual covariant ∇/□.

## 6. Rerun protocol
Download verified ZIP20, extract; in xh_s4_020_bundle run:
  python xh_s4_dtc0a_derivative_crosscheck_019.py
  python xh_s4_dtc0a_trace_sector_and_spectral_control_019.py
  python xh_s4_020_moving_projector_covariance.py
Last writes xh_s4_020_moving_projector_covariance_results.json. Tests include exact trace/strain cancellation, epsilon quartering, nonzero TT norm identity; all pass in frozen local environment. A separate README or manifest gives full SHA256 and exact source bytes inside ZIP. The source file is self contained **relative to the included 018 base**; no Python networking required.
