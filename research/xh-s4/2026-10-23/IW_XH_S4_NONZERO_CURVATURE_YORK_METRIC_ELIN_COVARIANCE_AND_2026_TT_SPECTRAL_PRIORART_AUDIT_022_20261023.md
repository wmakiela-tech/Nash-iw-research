# XH-S4 — obrót 022: niezerowa krzywizna, niezależny projektor Yorka i oddzielna kowariancja operatora E

RETURN_ID: XH-S4-OCT2026-NONFLAT-YORK-ELIN-GEOMETRIC-COVARIANCE-022_20261023
DATE: 2026-10-23
CELL: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03 / XH-S4
SCIENCE WINDOW: 2026-05-01—2026-10-23
RESULT_CLASS: INDEPENDENT_MANUFACTURED_SOLUTION_ELLIPTIC_YORK / NONZERO_RIEMANN_CURVATURE / DTC_FLAT_STENCIL_COVARIANCE_FALSIFIER / 2026_FOUNDATIONS / FIVE_QUESTIONS
GUARDS: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_NCDG_INTERPRETATION / NO_K_J3_INVARIANT / NO_BW_INGESTION / NO_NEW_OWNER_TASKS / NO_CONTINUUM_UNIFORM_CLAIM
REPRODUCTION: Actual local Python scripts and frozen JSON packaged in IW_XH_S4_022_NONFLAT_YORK_AND_OPERATOR_COVARIANCE_REPRO.zip. ZIP CRC, clean-directory execution of BOTH scripts and byte SHA-256 equality of JSON outputs PASS. The actual source code is inside ZIP, not claimed GitHub synced.

## 1. Why this test matters

Previous XH021 tested metric-dependent York P_g for phi^*delta with coordinate-dependent coefficients but Riemann(g)=0; thus a change of coordinate cannot distinguish intrinsic curvature effects. New Q51 compares an ACTUALLY CURVED conformal metric to the proper York projector with an analytically known, covariantly transverse-traceless manufactured field; independent solution is computed by vector elliptic York equation, not by transporting a flat projector. Separately Q52 checks source E_lin: even a correct P_g does NOT fix the coordinate dependence of an unrelated componentwise E_lin.

## 2. Exact mathematical host and TT conformal scaling

M=T^3, x,y,z periodic with period 2pi, g_ij=e^{2u(y)} delta_ij, u(y)=epsilon cos y. For n=3, scalar curvature
 R_g=e^{-2u}(-4 Delta_delta u -2|grad_delta u|^2)
    = e^{-2epsilon cos y}(4epsilon cos y−2epsilon² sin²y).
For epsilon≠0 this is NOT identically zero; the metric is not a diffeomorphic coordinate rewrite of delta. Numeric grid epsilon=.12: scalar R sampled from −.5986 to +.37758 at N17, RMS=.35682; epsilon=.25: from −1.6138 to +.60653, RMS=.86093. Therefore test has nonzero intrinsic curvature, unlike XH021.

Let Tflat=P_delta Hflat be a nontrivial symmetric flat Fourier TT field, with tr_delta(Tflat)=div_delta(Tflat)=0. Standard n-dimensional conformal law for a **covariant** rank-2 TT tensor gives
   T_g=e^{(2−n)u} Tflat=e^{-u}Tflat  (n=3).
Then tr_g(T_g)=0, div_g(T_g)=e^{-3u} div_delta(Tflat)=0. This is a traditional conformal covariance fact / York source tool, not a new theorem.

Select INDEPENDENT smooth covector W0 and scalar f, and manufacture an arbitrary nontrivial input
    h = T_g + (L_g W0) + f g,
    (L_g W)_ij = nabla_i W_j+nabla_j W_i − (2/3)g_ij nabla^k W_k.
From h alone form H=h−(tr_g h/3)g, then INDEPENDENTLY solve elliptic equation
     nabla^i(L_g W)_ij = nabla^i H_ij
with pseudospectral covariant derivatives and SciPy GMRES, x0=0, rtol=3e−10. Reconstruct York P_g h=H−L_g W. Only AFTER the solve compare to independently manufactured T_g. The Krylov solver is not supplied T_g or W0. It is supplied H and g; construction of manufactured input means recovery consistency is expected if code is correct, but solver and analytic reference are separately implemented.

Conformal Christoffels Γ^k_ij=delta^k_i u_j+delta^k_j u_i−delta_ij u^k; implementation uses full Gamma tensor, not XH021 shear-specialized connection. All code local in the ZIP. Gamma, g inverse, divergence, longitudinal operator, independent Tflat Fourier TT source directly inspectable.

## 3. Independently executed numerical evidence

All cases GMRES success info=0; global coordinate Frobenius tensor RMS /6 used for comparison (NOT intrinsic g-weighted norm). No dealiasing applied to pointwise products; manufactured T_g divergence improves with grid resolving its y sidebands. The corresponding g-traces were ≲1.1e−16; elliptic projected divergence max generally 7e−11 to 8e−11 for epsilon≠0.

| N | ε | manufactured T_g div max | York-vs-known TT RMS | wrong P_delta-vs-known TT RMS |
| 9  | .12 | 4.182e−6 | 3.223386868e−7 | 2.200893992e−3 |
| 13 | .12 | 1.085e−9 | 5.848126946e−11 | 2.200893983e−3 |
| 17 | .12 | 1.214e−13 | 1.579393248e−11 | 2.200893983e−3 |
| 13 | .25 | 5.610e−8 | 2.241506680e−9 | 4.611907930e−3 |
| 17 | .25 | 2.717e−11 | 2.533510708e−11 | 4.611907930e−3 |

Control epsilon0 N9: zero R, no nonflat error; the recovered TT error ≈1.0454e−12 and naive P_delta on same field reproduces Tflat ≈2.07e−17. This pins the metric dependence.
At epsilon=.12 N17 the improvement over wrong-flat projector for this ONE manufactured input is ~1.4e8× in chosen numerical norm. This numerical comparison is not a universal bound on ||P_g-P_delta|| or curvature sensitivity.
NB source host is a spatial Riemannian 3-torus, NOT a full Lorentzian spacetime, GR constraint solution, or NCDG physical background.

## 4. Independent E_lin NATURALITY FALSIFIER, tested under constant integer torus shear

Use diffeomorphism phi(x,y,z)=(x+y,y,z), with Jacobian M and flat pullback metric g=M^T M, still constant; no Christoffels. For any covariant tensor h let phi*h=M^T h(phi(x))M. Frozen DTC-style componentwise periodic central 3D stencil
   E_flat^(center)=I+alpha dx² Δ_h
does NOT generally intertwine with coordinate shear:
 E_flat^(center)(phi*h) − phi*(E_flat^(center)h) ≠0,
since its Fourier symbol depends on the coordinate sum sin²(k_i dx/2), not the transformed metric.

By contrast, for constant metric g define the (spectral) Laplace-Beltrami component tensor operator
   E_g^(spec)=I+alpha dx² (g^{ij}∂_i∂_j) 
(the Christoffel symbols vanish in this constant metric). For low-band Fourier fields and exact integer-grid shear,
 E_(phi*g)^(spec)(phi*h)=phi*(E_delta^(spec)h)
to numerical precision. This is NOT identical to using the original central stencil even in delta metric: that discretization difference was separately measured and remains O(dx²).

| N | alpha | naive central intertwining defect RMS | metric spectral intertwining defect RMS |
| 13 | .05 | 8.266499303e−4 | 3.595702e−17 |
| 17 | .05 | 4.873397066e−4 | 3.764554e−17 |
| 25 | .05 | 2.267315047e−4 | 3.575178e−17 |
| 17 | .20 | 1.949358827e−3 | 4.556737e−17 |

N17 alpha0: the naive identity operator commutes exactly with pullback; both defects are ≤4e−17.
N17 alpha.05, comparison *metric spectral* vs pulled *source central stencil* gives ≈1.16442e−5, not zero: DO NOT falsely claim the central source is numerically the same as the covariant spectral operator.
Thus a legally metric-dependent P_g and a source coordinate-centered E_flat are SEPARATE mathematical obligations. A fully curved tensor E_g would require connection/curvature terms and possibly a Lichnerowicz rather than Bochner choice; NOT IMPLEMENTED for the varying-curvature conformal metric.

## 5. Source-native new 2026 papers and prior-art subtraction

A. Sergey Stepanov, *Spectral Properties of the Chen-Nagano Gauge on Einstein Manifolds*, arXiv:2605.25723v1, posted May25, https://arxiv.org/abs/2605.25723 . ORIGINAL ARXIV ABSTRACT VERIFIED; full HTML unavailable. In its Einstein metric host, the Chen-Nagano gauge permits coupled trace/tracefree modes unlike Berger-Ebin TT, and the source claims under pinching that certain deformations become TT; it links Lichnerowicz tensor operator with shifted scalar spectrum. SOURCE LIMIT: not an imported theorem about arbitrary non-Einstein conformal torus g_epsilon. It motivates explicitly *fixing the gauge class and trace definition* before promoting a source trace->TT residual.

B. Anass Nifa, *Scalar and tensor eigenvalue bounds for conformally Kähler Einstein four-manifolds*, preprint v1 dated Sept1 2026, author primary https://anassnifa.com/papers/scalar-tensor-eigenvalues/ , record DOI 10.5281/zenodo.22851442. Full abstract and source bibliography verified; 31-page full PDF NOT read. In a 4D compact Einstein and conformally Kähler host, source claims tensor bound λ_m^TT≤(4Λ/3)(1−ρ^{-3}) for m=b2^- >0, ρ= max s_K/min s_K, with a strict inequality if conformal factor nonconstant, and CLW two TT eigenvalues below 7Λ/6. DIFFERENT 4D Einstein host from current 3D arbitrary conformal, NOT spectral proof for our projected finite operator. Motivates Q54 measuring curvature-aware spectral restrictions only when legal.

C. July14 2026 Oxford IMRN *Metric-uniform spectral inequality for the Laplacian operator on manifolds with bounded sectional curvature*, https://academic.oup.com/imrn/article/2026/14/rnag158/8733970 . Primary ABSTRACT: L2 full-vs-thick-subset inequality for scalar spectral projector with constants depending on curvature bounds and cutoff. DIFFERENT scalar Laplacian host, NOT a norm certificate for TT projector or DTC mask; informs Q55 that domain/curvature/observation coverage affect legal spectral control.

D. Mature York/CTT foundational theory: York PRL 26 1656 (1971) https://doi.org/10.1103/PhysRevLett.26.1656 . Ogurol/Boybeyi/Tekin Aug2 2026 DOI 10.1002/prop.70136 used CTT in specifically conformally flat maximal slice; do NOT call current conformal nonzero curvature experiment their model or assert its novelty.

E. IMPORTANT chronology: Bochniak/Dąbrowski/Sitarz/Zalecki *On Geometric Spectral Functionals*, SIGMA 22 035, originally online **April14 2026** https://sigma-journal.com/2026/035/ , hence OUTSIDE requested May1 date window; relevant prior art for source metric/scalar curvature/Einstein spectral functionals, NOT a new post-May discovery. The named spectral functionals require Dirac/Laplace type hosts and Wodzicki residue; unrelated to raw TT RMS in our finite torus. Explicitly subtract mature geometry before novelty.

## 6. Original XH scientific questions and exact discriminators

Q51 P0 **Does independently solved York recovery persist with intrinsic nonzero Riemann curvature?** YES for this explicitly manufactured 3D torus conformal metric with R≠0, bandlimited input and periodic boundary, error table above. NOT universally. Cheapest next falsifier outside conformally flat host: a metric with nonzero Cotton tensor / nonconformal-flat geometry, and independent reference/orthogonality certificate, not yet solved.

Q52 P0 **Can P_g be geometrically correct while coordinate-source E_lin remains non-natural?** YES: constant shear E_flat-vs-pulled target differs 4.87e−4 at N17 alpha.05 whereas metric spectral intertwining ≈3.8e−17. Exact host distinction: central and spectral DIFFER; do not use this to claim full E_g for variable metric.

Q53 P0 **Which geometric E_g is the intended mathematical realization—connection Bochner ∇*∇, Lichnerowicz Δ_L=∇*∇+curvature, covariant tensor wave box, or another?** These differ, including curvature couplings, signature/domain and time causality. Each candidate requires own source mathematical target, norm, sign, boundary and if Lorentzian, retarded prescription. No source license for physical background independence without declared covariant ∇/□.

Q54 P1 **When is TT vs a different gauge (Chen-Nagano) informative for source physical target?** Need identical background geometry, gauge-fixing, trace and boundary domain; Stepanov source result Einstein host does not transfer to our g.

Q55 P0 **Does small residual of elliptic GMRES certify geometric target error?** NO: at same epsilon=.12 N9 manufactured TT divergence 4e−6 and output error 3.22e−7 vs GMRES ~3e−10, whereas N13 error 5.85e−11 and N17 1.58e−11. Use multi-N + source manufactured solution, residual, independent trace/div and q-mode leakage. Relevant numerical literature De Ceuster/Li arXiv:2609.10173, known from report021.
Owners/moderator may select future effort; no tasks assigned now.

## 7. Reproduction and custody
LOCAL immutable initial code and outputs:
- xh_s4_022_nonflat_conformal_york.py, plus result JSON
- xh_s4_022_elin_naturality.py, plus result JSON
- 021 trusted tt_constant_metric helper copied self-contained into ZIP
- README + MANIFEST_022 JSON with all SHA256.
ZIP /mnt/data/IW_XH_S4_022_NONFLAT_YORK_AND_OPERATOR_COVARIANCE_REPRO.zip
Archive SHA256 e48fe19a007cea19b998ba13f401635ea9c441bd760f5b2dc89474e7e9021a10.
Clean extract in new directory, run both entrypoints (exit 0), verify JSON sha matches originals:
York JSON 05732e56a3bc2bd76420b1596b513220b203fa12a9f2117c64d0bd196be0ff11
E_naturality JSON cb26c0faee7fd702f3b7796345c89496cee0bc2e6a901c8e8386daaa838b3d07.
GitHub readback and Slack dissemination must be independently verified; not implied by local archive check. Data SHA might be environment-specific due floating reductions; declared local platform replay byte-identical.

NEGATIVE_KNOWLEDGE: Curved 3D Riemannian metric is not full Lorentzian NCDG gravity; recovery from manufactured input does not prove arbitrary-field operator convergence or curvature dynamics; static metric spectral E is not a retarded □; TT gauge is not universal; no K/J3 invariant, BW ingestion or discovery.
