# XH-S4 — obrót 023: Bochner/Lichnerowicz, analityczny kontrprzykład TT i granice stabilności widmowej

RETURN_ID: XH-S4-20261023-NONEINSTEIN-TT-BOCHNER-LICH-EXACT-COUNTEREXAMPLE-023
DATE: 2026-10-23
CELL: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03 / XH-S4
SCIENTIFIC WINDOW: May 1–October 23, 2026 plus mature mathematical prior art.
RESULT CLASS: EXACT SYMBOLIC COUNTEREXAMPLE / TWO INDEPENDENT FINITE NUMERICAL VALIDATIONS / 2026 THEOREM HOST-SUBTRACTION / NEW RESEARCH QUESTIONS
GUARDS: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_PRIORITY / NO_NCDG_PHYSICAL_UPGRADE / NO_K_J3_INVARIANT / NO_BW_INGESTION / NO_NEW_OWNER_TASK / NO_CONTINUUM_UNIFORM_CONVERGENCE.
SOURCE DISTINCTION: XH exact symbolic and NumPy results are independently produced; academic sources are prior-art host constraints, not claimed authors of this explicit toy calculation.

## 0. Previous state and target
Report 022 verified a proper York elliptic projection for a NON-EINSTEIN conformal metric g=e^{2u(y)}delta with nonzero scalar curvature, and separately showed a DTC-style componentwise E_lin does not intertwine with torus shear while a metric spectral operator does. Thus Q53 remained unresolved: which tensor operator E_g can preserve geometric naturality, and does such naturality imply that the **TT-subspace is invariant**? The latter is a DISTINCT proposition.

## 1. Exact host and convention
Take the flat-topology Riemannian three-torus T³ with 2π-periodic coordinates (x,y,z), u(y)=eps cos y and g_ij=e^{2u}delta_ij. Scalar curvature R=e^{-2u}(-4u''-2(u')²). For eps≠0, the metric is intrinsically curved; its Ricci eigenvalues are distinct and it is generally NOT EINSTEIN.
Let Δ_B h=∇*∇h=−g^{pm}∇_p∇_m h (positive rough operator on Euclidean Fourier modes) and use the source standard symmetric-covariant-rank-2 Lichnerowicz convention
  (Δ_Lh)_ij=(Δ_Bh)_ij+Ric_i^a h_aj+Ric_j^a h_ia−2 R_{i a j b}h^{ab}.
Riemann sign chosen so g^{ij}R_{i a j b}=Ric_ab. The two operators are both geometric/natural at the CONTINUUM tensorial-definition level. Their curvature terms differ. Avoid the convention-free sign of 'Lichnerowicz eigenvalue'; some literature defines −Δ_L or an Einstein operator shifted by 2Λ.

## 2. CLOSED-FORM EXACT COUNTEREXAMPLE
Consider ANY smooth periodic u(y), any real a,b, and covariant symmetric field
  h=e^{−u(y)} diag(a,b,−a−b).
This is EXACT TT: tr_g h=0 and ∇^i h_ij=0 everywhere, because e^{(2−n)u} with n=3 preserves divergence-free and trace-free for covariant rank-2 tensors and the flat diagonal reference is TT.
Direct SymPy symbolic tensor differentiation of Γ^k_ij, ∇h, second covariant derivative, Ric and 3D Riemann contraction yields:
  tr_g(Δ_B h)=0,  tr_g(Δ_L h)=0,
  ∇^i(Δ_B h)_{iy}=−3 b e^{−5u}(2u'u''−u'''),
  ∇^i(Δ_L h)_{iy}=+3 b e^{−5u}(2u'u''−u'''),
and x,z divergence components vanish.
For u=eps cos y:
  2u'u''−u'''=eps sin y (2eps cos y−1).
For 0<abs(eps)<1/2 and b≠0 the divergences are nonzero at generic y, even though h is exactly TT on the input. Yet for b=0 BOTH outputs preserve TT. Thus an apparent successful one-TT-state test does not establish invariant full TT subspace. Source-only non-Einstein host; no NASH theorem.

## 3. Numeric reproduction using full independent tensorial covariant operators
NumPy FFT implementation on N³ periodic grid:
- Γ from conformal metric; first and second covariant derivatives include derivatives on tensor and derivative index, so no omission of Γ^q_{pm};
- analytical Ric components Ric_xx=Ric_zz=−u''−(u')², Ric_yy=−2u''; scalar cross-check with conformal curvature;
- 3D Riemann contraction calculated independently from Ric, scalar and g; verified tr_g(R°h)=Ric_ab h^{ab} at each node and ∆_L trace cancellation;
- source h_TT=e^{−u}P_delta Hflat from previous verified 022 source and diagonal special cases.
Table global coordinate-component divergence RMS, no interior mask:
N9 eps0: input div ≈1.1e−16; div Δ_B≈6.67e−16; div Δ_L≈6.67e−16.
N13 eps .12: input div max 1.085e−9; div Δ_B RMS .015821513; div Δ_L .008203771.
N17 eps .12: input div max 1.214e−13; div Δ_B .015821514; div Δ_L .008203770.
N17 eps .25: input div max 2.717e−11; div Δ_B .053174293; div Δ_L .025510552.
The output tr_g was ~1e−15 for both; apparent TT non-preservation is in divergence, not trace. The error persists against grid refinement while input div tends to zero.
ANALYTIC crosscheck for diagonal (a,b)=(1,−2), N17 eps .12: max discrepancy between the exact -3b e^-5u(2u'u''−u''') formula and computed ∇·Δ_B is 4.3164e−10, and computed ∇·Δ_L opposite-sign formula 4.3229e−10. At N25 both discrepancies ≈8e−13. This is a strongly validated exact identity, not an inferred continuum result from finite N alone.

## 4. A tempting scalar curvature tuning succeeds only on one chosen field
Define a family A_theta=Δ_B+theta(Δ_L−Δ_B), where theta=0 means Bochner, theta=1 means Lichnerowicz. For the diagonal TT family above,
  ∇^i(A_theta h)_{iy}=(2theta−1)*3 b e^{-5u}(2u'u''−u'''),
so theta=.5 REMOVES divergence for ALL diagonal TT of this particular form. This does NOT turn A_.5 into a universal TT-preserving tensor Laplacian.
INDEPENDENT full grid N17 eps .12:
- for h=e^-u diag(1,−2,1), ||div A0 h||=.344447148, theta=.5 ->1.45e−13, theta=1 ->.344447148; least squares theta*=.5000000.
- for independent multi-harmonic h=e^-u P_delta(Hflat), ||div A0 h||=.015821514, theta=.5 ->.006360300, theta=1 ->.008203770; best single theta*=.693289619 with residual STILL .004771334 >0.
Thus NO single theta from this simple one-parameter mix preserves even these two TT examples simultaneously. This is a concrete target-relative counterexample, not a theorem about every possible curvature-dependent tensor differential operator.

## 5. Recent 2026 primary theorem/host audit and existing mathematics
A. Guillaume Verger, *Instability of Böhm’s Einstein metrics*, arXiv:2608.25865v1, submitted AUG 26 2026, FULL HTML source https://arxiv.org/html/2608.25865v1. In named high-dimensional Böhm Einstein metric families on spheres/products with 5≤dim≤9, the COUNT of negative TT Lichnerowicz eigenvalues diverges along an Einstein metric sequence approaching cone limit. Crucial separate questions: (i) is TT a well-defined invariant operator domain? (ii) how large/sign is its spectrum? (iii) which physical perturbative problem, if any, does that spectrum govern? Einstein status and legal TT eigenspaces do not imply positivity/stability. Source theorem CONDITIONAL to Böhm family/sequence and chosen Lich sign; our non-Einstein 3-torus is NOT its host.
B. Anass Nifa, *Negative Lichnerowicz modes on Einstein warped products and spheres*, author manuscript August31 revised Sep2 2026, primary abstract https://anassnifa.com/papers/negative-lichnerowicz-modes/ ; full PDF was NOT read. Claims at least one negative TT mode for nonhomogeneous compact Böhm metrics and certain positive Einstein warped products, with divergence penalty preserving negative TT index. Source status PREPRINT, author ABSTRACT only, may overlap with Verger, no independent priority novelty claim.
C. Mature prior art (not new 2026 discoveries): Schwahn *Stability of Einstein metrics on symmetric spaces of compact type*, 2021/2022 source https://link.springer.com/article/10.1007/s10455-021-09810-4 ; Einstein TT-Lichnerowicz eigenproblem and Δ_L≥2E stability criterion in that variational convention. Cross-source comparison MUST reconcile operator sign/curvature shift before saying 'negative eigenvalue' equals 'physical instability'.
D. March 2008 original *Stress-energy tensors and the Lichnerowicz Laplacian*, https://doi.org/10.1016/j.geomphys.2008.05.008 : commutation with divergence under PARALLEL RICCI (∇Ric=0) for a specified Lichnerowicz calculus, not arbitrary non-Einstein metric. This is mature explanation for host restrictions, not XH new discovery.

## 6. Typed research questions Q56–Q61, falsifiers and stop rules
Q56 P0: Does chosen geometric tensor operator preserve TT as a WHOLE SUBSPACE on chosen metric? One counterexample b≠0 answers no for both raw Δ_B/Δ_L on this metric; testing one b=0 field gives a false PASS. Require operators/domains and source-specific trace/div certificate.
Q57 P0: Can a universal scalar combination of curvature terms cure leakage? Diagonal theta=.5 exactly cures, but multi-harmonic optimum theta=.6932896 leaves residual .00477; this falsifies universal solution WITHIN the limited one-parameter A_theta FAMILY for chosen metric/inputs. More elaborate geometric operators remain open.
Q58 P0: Will a compressed form E_g^TT=P_g E_g P_g cure leakage by construction? Yes in a properly defined bounded-domain/projector host, but it CHANGES OPERATOR, often introduces global/nonlocal projection, can modify the commutator and does not imply positivity, causal Lorentzian response, or project physical invariance. Distinguish *trivially projected output* from *intrinsic invariant subspace*.
Q59 P0: If E_g preserves TT on EINSTEIN host, does that imply spectral/variational or physical stability? NO: Verger 2026 exhibits increasingly many negative TT eigenvalues for its specified Einstein/Böhm family. A proper physical stability mapping to Lorentzian wave source must be stated and checked separately.
Q60 P1: What field family and frequency/metric class suffice to certify the entire TT operator restriction rather than a few favorable probes? Need upper bound on ||(I−P_g)E_gP_g|| (possibly Sobolev H^s→H^{s−2}, unbounded operator domains handled), not just finite TT input RMS. Demonstrated exact diagonal b=0 PASS/b=-2 FAIL and different h multi-harm.
Q61 P0: Can the intended NASH E_g be specified as Bochner/Lichnerowicz/metric wave □, plus curvature correction, causal prescription, boundary/zero-mode and gauge class, and compared to DTC flat E_lin at g=δ? Source E_lin is discrete componentwise *smoothing* I+alpha dx²Δcenter; none of our Δ_B or Δ_L calculations is yet a physically selected E_g or full DTC re-execution.
Claim ceiling remains mathematical host/research questions; no new K/J3 invariant, physical NCDG, BW acceptance or auto owner tasks.

## 7. Reproduction and trust
Artifacts freeze three scripts / two JSON / README plus dependency source scripts. Exact local ZIP:
 /mnt/data/IW_XH_S4_023_REPRODUCIBILITY.zip
SHA256 5873a01274daac85038619cc386e67a65fff1eabb5e60419294465513f100aaf.
- xh_s4_023_symbolic_diagonal.py SHA256 a5a53abeab6183145bdade002fbc3d51a19b79a7e73b5fe9e51b35c641d168dd: pure SymPy exact symbolic tensor calculus with general u(y);
- xh_s4_023_rough_lichnerowicz_tt.py SHA256 a14acff9624d90d131107c2ec1e95e5b6f2434ef52d1509f8e0475d14561ec78: NumPy operator code + exact formula numerical crosscheck, N9/13/17 manufactured TT and diagonal/multiharm theta tests;
- xh_s4_023_rough_lichnerowicz_tt_results.json SHA256 fe4c19495dac572f4573f1a084ac9d4ac83aaa4317f1444be1e03a1611a410f3;
- xh_s4_023_additional_falsifier_results.json SHA256 8b048b9998b889906f11f7d8cdc1adcaed8c211f58ca550ace33ddf774817ad3;
- manifest verifies all dependency bytes.
ZIP CRC test passed and clean independent temporary-directory unzip, execution of BOTH entrypoints and recomputation of JSON hash check passed. This is actual executable reproducibility, not only blob readback. GitHub custody of this report and Slack dispatch need independently verified receipts; must not assume from local ZIP.

FINAL STATUS: EXACT_SYMBOLIC_NON_EINSTEIN_TT_COUNTEREXAMPLE / MULTIFIELD_MIXTURE_NO_GO / CLEAN_REPRO_PASS / SOURCE_LEVEL 2026 THEOREM AUDIT / NO_CANON / NO_EXEC_SIGN.
