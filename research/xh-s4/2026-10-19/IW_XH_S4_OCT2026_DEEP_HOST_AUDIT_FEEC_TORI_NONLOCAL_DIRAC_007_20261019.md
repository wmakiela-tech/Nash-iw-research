# XH-S4 — October 2026 deep source/host audit: FEEC pseudospectra, noncommutative tori, nonlocal Dirac
DATE: 2026-10-19
RETURN_ID: XH-S4-OCT2026-DEEP-HOST-AUDIT-FEEC-TORI-DIRAC-007
CELL: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03 / XH-S4
READ_MODE: FULL_ARXIV_HTML_SECTIONS (NOT JUST ABSTRACT), 3 ORIGINAL PREPRINTS
AUTHORITY: EXTERNAL_THEOREM_AND_HYPOTHESIS_EXTRACTION_ONLY / NO_EXEC / NO_CANON / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO NEW TASKS
REVIEW_STATE: SOURCE_TEXT_READ / PROOFS_NOT_INDEPENDENTLY_FORMALIZED_OR_REFEREED / NO CODE REPRODUCTION
PREDECESSOR: https://github.com/wmakiela-tech/Nash-iw-research/blob/89dacddfdbde11bfc9255ce4a8a0ae62323475e9/research/xh-s4/2026-10-18/IW_XH_S4_OCTOBER_2026_SCIENTIFIC_LITERATURE_NASH_SOURCE_MAP_006_20261018.md

## A. FEEC / advection-diffusion / pseudospectra
PRIMARY: Boffi, Hu, Liang, Zerbinati, arXiv:2610.01501v1, 1 October 2026.
HTML: https://arxiv.org/html/2610.01501v1

OBJECT. Complex-valued differential k-forms on bounded polyhedral Lipschitz Ω⊂R^n, de Rham/Hodge complex. Closed complexes (closed range). s-regularity with s>1/2 (Sec 2, eq 2.3). Conforming FEEC dual de Rham subcomplex; Assumption 2.2 bounded commuting cochain projections tilde_pi_h with d tilde_pi_h=tilde_pi_h d, plus approximation ||u-tilde_pi_h u||_{L2} ≤ C h^t |u|_{H^t} for 1/2<t≤1. Discrete harmonic forms controlled by projection and approximation (Lemma 2.3). Field u bounded; further ν/coercivity conditions for full advection-diffusion source operator. Important: physically motivated periodic-cube experiments do not erase formal domain/boundary assumptions.

THEOREM 3.5 (bounded S,T on COMMON Hilbert space X): for ε>0 and η=||T-S||_{L(X)}, sigma_ε(T) ⊆ sigma_{ε+η}(S), and reverse inclusion with S,T swapped. It is a known Kato/Trefethen-Embree-type stability estimate adapted to pseudospectra, NOT newly invented here.
COROLLARY 3.6: ||T_n-T||_{operator}→0 implies mutual ε-vs-δ pseudospectrum containment for any 0<δ<ε, n sufficiently large.
THEOREM 4.6: for half-Hodge solution operator, ||T-T_h||_{L(L2,H*Λ)}→0.
THEOREM 5.3: for full-Hodge system, under u∈L∞ and ν≥4ε+(1/2)||u||∞+ε^-1||u||∞²+1>0, ||T-T_h||_{L(L2,L2)}→0.
In Sec 3 they make a shifted inverse solution operator relation to unbounded L_u; don't transport finite bounded T statement to unbounded L_u without shifted resolvent/hypotheses and space projections.

HOST RELEVANCE:
- Hilbert-complex continuum+numerical bridge: appropriate complex, boundary, commuting cochain projector, harmonic approximation, norm convergence of solution operators.
- DTC0a nonnormal projected transport A_C: motivates pseudospectral certification, BUT native FFT/TT projected tensor discretization is not demonstrated to be a conforming discrete de Rham complex with the above commuting projection, nor is a common-space ||T_N-T||_op bound established.
- A profile RMS(K_A h0) is a pointwise witness, NOT ||M_A||_op, and odd-N stable plateau is not FEEC pseudospectral convergence.

EXACT NEGATIVE TEST / MY ALGEBRA (not source paper):
Take X=C², M_L=diag(0,L), unit h0=(1,0). Then ||M_L h0||=0 for every L>0, while ||M_L||_op=L can be arbitrarily large. So a single zero residual is consistent with unbounded operator norm; pointwise profile checks cannot certify Theorem 3.5's η. This is an elementary illustrative counterexample, not a new NASH result.

CITATION: https://arxiv.org/html/2610.01501v1 sections 2,3 (Thm 3.5, Cor 3.6), 4 (Thm 4.6), 5 (Thm 5.3).

## B. Spectral truncations for noncommutative tori
PRIMARY: Bhatt, Guin, Sharma, arXiv:2610.01132v1, 1 October 2026.
HTML: https://arxiv.org/html/2610.01132v1

OBJECT: A_Theta noncommutative n-torus n≥2 with canonical spectral triple (A_Theta,H,D), its finite cutoff P_R and finite-dimensional operator system E_R; study compact state spaces equipped with Connes metric. Target is GH convergence of metric STATE SPACES, not operator graph-norm convergence, spectrum of arbitrary A_C, or physical field observables.

DEF 2.3: C1-approximate order isomorphism consists of maps rho_R:E→E_R, sigma_R:E_R→E, each positive, unital, norm contractive and Lipschitz seminorm contractive, and two round-trip defects bounded:
||e - sigma_R rho_R(e)||≤γ_R ||[D,e]||;
||T - rho_R sigma_R(T)||≤γ_R ||[D_R,T]||;
γ_R→0.
Sec 3 constructs rho_R(a)=P_R^0 pi_tau(a) P_R^0 and sigma_R(T)=(1/N_R) Σ_{λν∈Λ_R} T_{λν} e_λ e_ν*.
Proposition 3.6 says compositions are Fourier multipliers F_{m_R} on A_Theta / entry multipliers S_{m_R} on E_R; underlying cocycle phases cancel.
Proposition 3.7 shows rho unital completely positive C1-contractive; Lemma 3.9 plus followups sigma positive/contractive.
THEOREM 4.18: state metric spaces (S(E_R),d_E_R) converge in GH to (S(A_Theta),d_A_Theta) as R→∞.

HOST RELEVANCE: NASH finite-N / continuum currentness guard. If aspiring to state-space geometric convergence, must specify state-space object, Lipschitz Dirac seminorm, cutoff maps BOTH ways and round-trip bounds. An orthogonal projector P_TT and finite matrix spectra are not by themselves a C1 approximate order isomorphism. DTC TT projected tensor fields are not shown to form unital operator systems with CP reconstruction or Connes metric. Nor does GH convergence imply K/J3 covariance residual convergence. No theorem import to DTC as-is.

CITATION https://arxiv.org/html/2610.01132v1 def 2.3, prop 3.6/3.7, thm 4.18.

## C. Nonlocal covariant Dirac / de Sitter
PRIMARY: Porfírio & da Silva, arXiv:2610.06390v1, 5 October 2026.
HTML: https://arxiv.org/html/2610.06390v1

OBJECT: spin-1/2 curved-spacetime action S=∫√-g [i barPsi slash-nabla f(slash-nabla) Psi - m barPsi Psi]. Explicit covariant spin connection and tetrads; entire analytic f of FIRST-ORDER covariant Dirac operator. Free squared equation [slash-nabla² f(slash-nabla)²+m²]Psi=0, with their sign conventions slash-nabla²=Box−R/4 (Lichnerowicz). Entire zero-free f=e^g does NOT rule out zeros/poles of the FULL massive kinetic operator i slash-nabla f(slash-nabla)-m.

BEHAVIOR: on local eigenmodes i slash-nabla Psi_M=M Psi_M, branch condition M f(-iM)=m. Two exponential models use Lambert-W roots:
- Model I: M_n=-i Λ W_n(i m/Λ), principal root complex at finite Λ, no standard real-mass physical sector.
- Model II: M_n=-Λ W_n(-m/Λ). For 0<m/Λ<1/e, two real branches, n=0 with 0<M_0<Λ giving positive pole residue; n=-1 with M_{-1}>Λ giving negative residue/ghostlike; others complex. At m/Λ=1/e roots collide and simple-pole analysis fails.
In presence of U(1) gauge, squared operator acquires sigma^{μν}F_{μν} spin-field term; scalar-like separated decomposition is NOT directly legal in interaction; analysis perturbative with |λ|/Λ,e|A|/Λ,e|F|/Λ² ≪1 in fixed gauge.
Results for open chart de Sitter and Bunch-Davies vacuum/entropy are background- and physical-branch-dependent. No generic physically ghost-free theorem for arbitrary exponential form factor.

HOST RELEVANCE:
- Essential NCDG/LT gate: covariantize BEFORE applying nonlocal function, choose correct tensor/spinor bundle, define domain and operator spectrum, then check full kinetic-pole/residue positivity, not merely zero-free f.
- Curvature/spin/gauge commutator explicitly changes square of Dirac operator; NOT valid to substitute flat Box by curved scalar Box without representation/domain checks.
- This is a DIFFERENT spinor first-order f(slash-nabla) theory, not a theorem for NASH E(Box) tensor, K/J3 invariant, NCDG background dependence, or empirically verified gravity.
- In NASH functional-multiplier Hilbert cohomology question, invertibility/domain of f(Delta) and resulting differential/cohomology remain separate mathematical issues from physical pole structure.

CITATION https://arxiv.org/html/2610.06390v1 sec II (eq 4–11, 19–24), III (eq 31), IV.3 (Table 1, Lambert W branches).

## Three incompatible notions of finite approximation
A. FEEC approximates compact solution operators in OPERATOR NORM with commuting COMPLEX structure, yielding pseudospectral control.
B. Truncated quantum tori approximate METRIC STATE SPACES via positive two-way maps and round-trip Lipschitz bounds, yielding GH convergence.
C. Finite DTC FFT/TT profile evidence currently supports declared numerical residual diagnostics, not A or B.
Avoid conflation 'all are finite-N convergence'.

## Decision / claim ceilings
FEEC source-native applicability: HIGH as design of missing numerical certification, direct theorem import to current DTC = HOLD (commuting projections/norm convergence not shown).
Noncommutative torus: MODERATE as precise negative guard for geometry convergence, no direct DTC residual host.
Dirac nonlocal: HIGH physics-type firewall for curved background and full kinetic-pole physical-branch selection, no physical NCDG result.
HYPOTHESES READ != PROOF CHECKED. No automated researcher delegation, no canon modification, no published new-NASH claim, no PBH endpoint.

AUDIT PROVENANCE: official arXiv HTML versions v1; previously harvested overview 006 linked above. All mathematical equations quoted/paraphrased source-specifically. No PDFs required for this reading.
