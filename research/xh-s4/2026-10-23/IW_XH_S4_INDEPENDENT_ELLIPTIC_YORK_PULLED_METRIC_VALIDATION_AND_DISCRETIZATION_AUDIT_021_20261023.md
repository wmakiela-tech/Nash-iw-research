# XH-S4 — obrót 021: independent metric-defined York projection versus fixed-background TT, elliptic solver and alias-control

RETURN_ID: XH-S4-YORK-PROJECTOR-NONLINEAR-SHEAR-INDEPENDENT-ELLIPTIC-VALIDATION-021_20261023
DATE: 2026-10-23
ORIGIN_CELL: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03 / XH-S4
CLASS: MAY–OCT 2026 SOURCE-HOST SCIENTIFIC FOLLOWUP / EXACT GEOMETRY / TWO INDEPENDENT NUMERIC REALIZATIONS / NEW QUESTIONS Q46–Q50
GUARDS: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_NASH_UPGRADE / NO_NCDG_BACKGROUND-INDEPENDENCE / NO_K_J3_INVARIANT / NO_BW_INGESTION / NO_TASKS_TO_OTHER_CELLS
SCIENCE STATUS: FINITE NUMERIC REPRODUCTION VERIFIED; NOT A NONZERO-RIEMANN CURVED GEOMETRY TEST; NO FINITE-N-UNIFORM THEOREM.

## 1. Motivation and prior correction

XH017: the Fourier TT projector has a spatial tail, obstructing an unchecked finite-small-range pseudospectral theorem transfer.
XH018: exact inserted projector defect `K_A−K_B=P L2 Q L1 h−P L1 Q L2 h`.
XH019: the standard input is pure trace h=fI, Ph=0; spectral derivatives make K_C vanish at alpha0 but K_A persists.
XH020: naturality (P_{phi^*g}(phi^*h)=phi^*(P_gh)) implies ((D_gP)[Lie_Cg]=[Lie_C,P_g]), and test P+epsilon[Lie,P] agreed to O(epsilon²). That was a *constructed first-order algebraic conjugation*, NOT independently solved metric York projection.
XH021 addresses this precise gap with a real independent York elliptic problem in a NONCONSTANT metric and an exact independent analytical pullback comparison.

## 2. Original source literature and precise relation

- Ogurol/Boybeyi/Tekin (2026 Aug2), *Perturbative Analytical Construction of Bowen–York Initial Data for Binary Black Holes up to Third Order in Spin and Linear Momentum*, Fortschritte der Physik, DOI https://doi.org/10.1002/prop.70136, primary full open https://onlinelibrary.wiley.com/doi/full/10.1002/prop.70136 . Section 4 Eqs (23)-(24) explicitly implements conformal TT decomposition (A^{ij}=A^{ij}_{TT}+(L W)^{ij}), with covariant derivative of conformal metric and L vector conformal Killing operator. Paper specializes conformally flat/maximal vacuum initial data; NOT an exact theorem about DTC0a transport commutators.
- Frederik De Ceuster, Tjonnie G.-F. Li (2026 Sep9), *A Differentiable Parametric Model of Binary-Black-Hole Initial Data: I. Conformally flat Bowen–York punctures*, arXiv:2609.10173v1, full https://arxiv.org/html/2609.10173v1 . Distinguishes CHECKED DISCRETE elliptic constraint residual <=1e-10 in row-equilibrated norm from external validation against TwoPunctures and constraint verification on INDEPENDENT evolution grid. Our simple York GMRES test is neither their code nor their physics, but exactly shares the important validation-level distinction.
- Mature prior art York 1971 PRL DOI https://doi.org/10.1103/PhysRevLett.26.1656, and numerical-relativity initial-data review https://link.springer.com/article/10.12942/lrr-2000-5 (outside May range, cited as foundational). This is NOT new mathematical geometry invented by NASH.

## 3. Independent constant sheared torus: P_g constructed DIRECTLY from g, not transported P

Let (phi_s(x,y,z)=(x+s y,y,z)) on (T^3), integer s=1 or 2 so mapping is a true torus automorphism.
(J=Dphi=egin{pmatrix}1&s&0\\0&1&0\\0&0&1end{pmatrix});
(g_s=J^T J) constant positive flat but not Euclidean-coordinate identity.
For each Fourier mode k != 0 define (q^i=g^{ij}k_j), (k_g^2=k_i q^i):
 (Pi_i^{\,a}=\delta_i^a-k_i q^a/k_g^2),
 (Pi_{ij}=g_{ij}-k_i k_j/k_g^2),
 (Pi^{ab}=g^{ab}-q^a q^b/k_g^2).
Define (P_g(h)_{ij}=Pi_i^{\,a}Pi_j^{\,b}h_{ab} - 1/2 \Pi_{ij}\Pi^{ab}h_{ab}); k=0 use (h-\mathrm{tr}_g h\,g/3).
This is a metric-dependent Fourier York projector on flat constant-anisotropic torus. Original P_delta and new P_g computed independently. Discrete pullback h'(x)=J^T h(phi(x))J is exact grid index permutation for integer s; low-band frequencies chosen to avoid aliasing under shear.
Check (P_{g_s}(\phi_s^*h)=\phi_s^*(P_\delta h)) independently, as well as g-trace, g-divergence, idempotence.
NUMBERS:
 N13,s1 RMS exact equivariance error 2.4433636317e-17, fixed Euclidean projector error 0.03559874764.
 N17,s1 RMS exact equivariance error 2.3651260784e-17, fixed error 0.03559874764.
 N25,s1 RMS exact equivariance error 2.3294183150e-17, fixed error 0.03559874764.
 N17,s2 exact RMS error 7.5896926318e-17, fixed error 0.07195217611.
For pure trace h=f delta with projected pullback h'=f(phi)g_s, P_g h' norm ~0 while fixed Euclidean P_delta produces 0.01190238 RMS for shear1. Demonstrates fixed-projector artifact even when geometry intrinsically flat and no numerical-resolution issue.

## 4. Fully nonconstant metric: INDEPENDENT elliptic York solve (not prior 020 algebraic P+t[L,P])

Now (phi_a(x,y,z)=(x+a\sin y,y,z)). (g_a=J^TJ) depends on y:
 g_xx=1, g_xy=a cos y, g_yy=1+a² cos²y, g_zz=1, det g=1;
 inverse g^xx=1+a² cos²y, g^xy=-a cos y,g^yy=1;
 sole nonzero Christoffel (Gamma^x_{yy}=-a\sin y).
This is NONCONSTANT COORDINATE METRIC yet intrinsically FLAT: pure diffeomorphism of flat torus. Do not mislabel as spacetime with nonzero Riemann curvature.

Given arbitrary smooth nontrivial 3x3 symmetric covariant h formed of trigonometric harmonics, compute its pulled-back tensor h'=J^T h(phi(x))J. Instead of transporting flat projector to compute candidate, first INDEPENDENTLY solve York vector equation with Fourier pseudospectral covariant derivatives on g_a:
 H = h' - (tr_g h'/3)g;
 (L_g W)_ij = ∇_i W_j+∇_j W_i - (2/3)g_ij ∇^k W_k;
 ∇^i(L_g W)_ij = ∇^i H_ij;
 P_g^elliptic h'=H-L_g W.
GMRES from zero, relative stopping tolerance 1e-10, no arbitrary penalty; vector W may have conformal Killing zero-mode gauge, but projected TT defined independently and equation solved at declared tolerances. Trace and divergence measured in metric g, not flat delta. Only AFTER solve compare against exact analytical reference (phi_a^*P_\delta h) produced from the independent flat projector and Fourier x interpolation. Reference is NOT used in GMRES or equation RHS.

RESULTS:
N9,a.12: GMRES final reported relative residual 5.1703e-11, covariant divergence max 1.53e-11, TT trace max 7.81e-17, York vs exact reference RMS 1.727633615e-6, frozen Euclidean P_delta error 0.003898491.
N13,a.12: residual 5.8212e-11, covariance compare RMS 5.213592498e-10, fixed P_delta error 0.003898491.
N17,a.12: residual 4.3187e-11, covariance compare RMS 4.046725244e-13, fixed P_delta error 0.003898491.
N13,a.25: residual 6.3803e-11, covariance compare RMS 2.050699763e-8, fixed P_delta error 0.008121362.
N17,a.25: residual 5.9683e-11, covariance compare RMS 1.102567200e-11, fixed P_delta error 0.008121362.
For N17,a=.12, (mathrm{tr}_g(P_g h')) max about 1.0e-16, (mathrm{div}_g(P_g h')) max 1.42e-11; idempotence was separately verified in constant-metric experiment. All 5 GMRES returned success code zero. Fourier differentiation and products employ NO de-aliasing; this is a collocation toy, not a continuum error bound.
Trace-only h'=f(phi) g is killed exactly by TRUE P_g because its tracefree part H=0, while use of fixed delta projector gives RMS 0.0006925473 (a=.12) or 0.001440902 (a=.25). This is independent of vector solve because tracefree H is analytically zero; treat as supplemental check not reproduction of elliptic solve on nontrivial input.
The geometry itself is flat, so this test establishes coordinate covariance for the type of fields and smooth diffeomorphism, not general covariance under nonlinear changes of physical metric.

## 5. Material numerical negative finding: solver PASS does NOT certify geometric discretization error
ALL 5 GMRES internal relative residuals near 4e-11–6e-11, but RMS external reference errors vary from 1.7e-6 (N9) down to 4e-13 (N17) for same a=.12. Larger Fourier grid resolves nonlinear mode sidebands created by sin(y) and reduces alias/collocation error, whereas Krylov solver already solved each discrete equation to similar tolerance. This is the same logical guard highlighted by De Ceuster/Li Sep2026: solver residual != independent solution validation.
The external reference is a specially solvable flat-pullback host, not an arbitrary curved metric. Errors quoted use unweighted coordinate Frobenius/6 RMS for comparability; geometric orthogonality is relative to L²(g), with detg=1 here. Do not pass off these arbitrary-output-norm magnitudes as curvature or gravity observables.

## 6. New XH research questions and typed relations
Q46 / P0: For which classes of diffeomorphisms and source tensor bandlimits does actual metric-dependent York projection commute with pullback to a numerically certified tolerance? Falsifier: mismatched Pdelta in constant integer shear produces errors 0.0356–0.07195 even at high N; true Pg errors <=1e-16 for low-band exact integer shear.
Q47 / P0: Does solving the curved (nonconstant-coefficient) York elliptic equation restore the same relation independently of the operator conjugation heuristic? YES for this flat-intrinsic but y-dependent g_a family, with N17 external error ~4e-13 and GMRES solver residual 4e-11 at a=.12. Not proven general.
Q48 / P0: What *external* reference or across-grid certificate is necessary to distinguish Krylov algebraic convergence from the true projector error? N9 a=.12 internal 5e-11, external 1.7e-6. Design multi-grid alias-aware and separate code numerical validation, source 2609.10173 cross-code precedent. This is a concrete numerical falsifier of inference “tiny algebraic residual -> tiny exact geometry error”.
Q49 / P0: Can NASH replace componentwise E_lin with a metric-natural tensor operator E_g, and what boundary/zero-mode conventions are required so that P_g E_g transforms legally? Current E_lin finite flat-coordinate Laplacian has NO defined covariant ∇/Box source; moving P alone cannot establish full NASH spacetime or physical covariance. Test transported E_g and phi*E_g consistency before promoting any claim.
Q50 / P1: How to distinguish coordinate-induced TT artifacts (Riemann(g)=0 for these shears) from genuine curvature/background content? Require nonzero-curvature metric family, relevant geometric operator, Riemann scalar/invariant control, and source-defined gauge/observable. Current work only coordinate artifacts, NOT real gravitational-wave production.
Typed link: York original geometry (1971) -> Ogurol2026 covariant CTT mathematical host -> De Ceuster/Li2026 independent elliptic solver validation -> current finite Torus test (exactly admissible toy) -> DTC fixed flat P (DIFFERENT HOST: target not yet covariant). No auto physical interpretation, no canon and no cross-cell tasks.

## 7. Reproducibility + local code attestations
Two independently implemented scripts:
- xh_s4_021_york_constant_shear.py (sha256 3602afd49df9ad22336bd375ac6e50cdea45434af78fa2caa5b6ff6a6bb069b2), NumPy-only metric Fourier projector with no transported-operator shortcut. results JSON sha256 36911085b52bc6db80533c6c57ca36511cdcfffc89f3308683aa6aa41cd33cd3.
- xh_s4_021_curved_york_elliptic.py (sha256 3d5b6c1ae3a114caafa7d6fdf8b9f501da542e9c470102878dd11680a79e7912), SciPy GMRES on full nonconstant-metric vector equation; reference pullback computed separately after solve. results JSON sha256 27e6428b4eb0cc244efb4fe8b626b9c1a2bcc7e30403f45b98651dd132c0ad01.
These local SHA256 apply to the frozen files before any later report edits. GitHub custody and independent replay/CRC pass require separate checks; don't claim unless actually verified. Runtime source NASH DTC0a byte-for-byte not imported into 021; 021 is mathematical York consistency test not a production run.

EVIDENCE_SUMMARY: TWO_INDEPENDENT_PROJECTION_REALIZATIONS / ONE_METRIC-PDE_SOLVER / SOURCE-MAP_NO_NEW_THEOREM / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_CLAIM.
