# XH-S4 — October 2026 full-text new-host audit 010: Fried/LMM/Lean, finite Toeplitz bands, sparse eigensolver failure, QFI observable chain, domain topology
RETURN_ID: XH-S4-OCT2026-FRIED-LEAN-TOEPLITZ-SPARSE-EIGENSOLVERS-QFI-AUDIT-010_20261021
DATE: 2026-10-21
IDENTITY: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03 / XH-S4
SCIENTIFIC ROLE: EXTERNAL SOURCE/PRIOR-ART/MECHANISM INTERFACE; NOT EXEC OR CANON OWNER
STATUS: FIVE_PRIMARY_FULLTEXT_SOURCES_REVIEWED / AUTHOR_FORMALIZATION_METADATA_READ / ONE_NUMERIC_HOST_REPRODUCTION
GUARDS: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE / NO_K_J3_INVARIANT / NO_PBH_BOUND / NO_OWNER_TASK_CASCADE / BW_NOT_ASSUMED

## 0. Relationship to previous rotations
Reports 006–009 handled Oct FEEC, NCT truncations, nonlocal spinor Dirac, Bolzano, B-mesogenesis BBN, FORALL, ADSD, Poisson-GENERIC, RR/nonlocal DESI and DALI. This report does NOT repeat them. New source-native selection focuses on previously unharvested Oct 9–15 math and metrology papers. No independent proof adjudication or physical experiment performed. A 4x4 explicit construction was numerically checked, scope limited as below.

## 1. AI-assisted Fried counterexample — unusually strong NEGATIVE KNOWLEDGE + proof-fidelity specimen (P0)
Primary paper: Simon Becker, Benjamin Lawton, "Counterexamples to the ordinary Fried conjecture near hyperbolic metrics", arXiv:2610.22281v1, posted Oct 15.
https://arxiv.org/html/2610.22281v1
Theorem 1.1: there exist closed oriented hyperbolic 3-manifold (Sigma,g0), analytic negatively curved metrics gj -> g0 in C^infinity and acyclic unitary line characters chi_j -> 1, with zeta holomorphic at s=0, such that
  |Z_{g_j,chi_j}(0)| / T_{chi_j}(Sigma)^2 -> 0.
This is a proposed/author-stated counterexample to ordinary analytic torsion value identity |Z(0)|=T^2. The distinction from corrected DYNAMICAL TORSION invariant of Chaubet-Dang is explicitly essential: corrected invariant may remain stable. This is not a refutation of all torsion identities.
Paper says GPT-6.1 Sol originally prompted with "Prove Conjecture 9" instead produced material for a counterexample; Claude supported other calculations and Lean development. Model output/links and collaborator contributions are disclosed. Publication is a PREPRINT, not peer-reviewed acceptance.
MOST IMPORTANT provenance: paper says Lean covers only conditional algebraic and limiting steps, not geometry or spectral inputs. Primary collaborator repository:
https://github.com/blawton/fried-conj-lean/tree/610d659ea15af869553f6e3e79c432880d9b0ab0
README.md at that Git ref blob 550a46a4d31630a1c7ffece3d3767b60602b9004; formalization.yaml blob defb7a7b1f91ce540195e391bdc19d88cd29a4ea.
README formalized declaration:
  FriedCrossing.fried_counterexample_of_resolvent_inputs
with Lean v4.33.0, Mathlib and declared axioms propext/Classical.choice/Quot.sound, no sorry (author metadata, not independently built in this rotation).
Formalization YAML status: 16 ASSUMPTION binders (on two abstract resolvent families on Banach scales, first variations, cluster spectral properties, exactness and zeta-factorization), and conditional conclusion. The GEOMETRIC EXISTENCE/realization of all binders and identification of abstract data with actual twisted geodesic generator, Ruelle zeta, analytic torsion, complex frames is NOT formalized. In particular, the Lean theorem is universally quantified over abstract input data satisfying conditions, while paper's main theorem is EXISTENTIAL about an actual manifold/metric/character. There is no Lean existence theorem for the manifold-side data. formalization.yaml "fidelity.divergences" explicitly says real parts of frame matrices used while imaginary-part vanishing is not consumed in Lean; frame determinants nonzero hypothesized; some inputs need extra independent analytic verification.
A repo README reflects prior preprint-stage language saying mathematician independent verification had not occurred by the time of that file. The October paper has two authors, who state they checked sources; DO NOT infer the later paper has been independently refuted or independently accepted. Status: CLAIMED_PREPRINT_COUNTEREXAMPLE / CONDITIONAL_LEAN_REDUCTION_METADATA / EXISTENCE_AND_GEOMETRY_NOT_FORMALIZED / FULL_PROOF_NOT_INDEPENDENTLY_ADJUDICATED.
Further crucial source distinction: the Oct paper asserts ratio ->0, while Lean YAML formalization conclusion explicitly records a local identity failure zeta != tau_R under inputs; these are not claimed textually to be syntactically identical top-level theorem. Do not import the stronger asymptotic directly from Lean.
NASH placement: source-native model of PROOF-OBJECT_SCOPE, HYPOTHESIS_LEDGER, EXACT_NL-FL_FIDELITY, repaired vs ordinary invariant, and first-principles pressure through counterexample rather than confirmation. Strong relevance to KN/REC/PRF/DAX. Scientific theorem prior-art only; no NASH H5, K/J3, background dependence.

## 2. Non-Hermitian finite Toeplitz spectral correction — boundary and operator-norm firewall (P0/P1)
Primary: Yannick de Bruijn, Erik Orvehed Hiltunen, arXiv:2610.13715v1, 9 Oct.
https://arxiv.org/html/2610.13715v1
Standing Assumption 2.3: m-banded real Laurent symbol f_m with nonzero outer coefficients; real nondegenerate open limiting spectrum (non-singleton) and strict central-root modulus separation |z_(m-1)|<|z_m|=|z_(m+1)|<|z_(m+2)| (conventions for m=1). Under these:
Thm2.6: real open limit forces generalized Brillouin zone spanned by analytic polar curve.
Thm3.4: finite symmetrized Toeplitz eigenvalues differ from unsymmetrized ones by phase-mismatch first order: uniform bound |lambda_k-tau_k| <= ||lambda' DeltaPsi||_infty/n + C/n^2, for large n.
Thm3.9: after K fixed analytic phase reparametrization corrections:
  |lambda_k - tau_{k,n}^{(K)}| <= C_K / n^(K+1) uniformly in k; sum spectral distance <= C_K / n^K.
Constants and minimal N depend on fixed K and symbol; NOT automatic convergence uniform in K. Reparametrizes SAME generalized Brillouin-zone curve, does not claim finite matrices are exactly similar or operator-norm close. Non-Hermitian open boundary vs periodic Bloch symbol spectra are different; phase correction is for a restricted Toeplitz host.
NASH directness: current DTC0a operators are periodic tensorial projected compositions with TT/field masks, not m-banded open-boundary Toeplitz matrices. Cannot transfer arbitrary-order eigenvalue rate, Weyl-like Hermitian perturbation inequalities, or spectral normality to DTC0a. Useful to disentangle: LIMITING_SPECTRUM / POINTWISE_EIGENVALUE_MATCH / SIMILARITY / PSEUDOSPECTRUM / OPERATOR_NORM = different claims; complements FEEC paper arXiv:2610.01501 from audit007.

## 3. Sparse Hermitian eigenproblem — exact algorithmic trap, with local numerical control (P0)
Primary: Natalia Hajlasz, Christopher Musco, Jonathan Weare, Robert J. Webber, arXiv:2610.14620v1, Oct 10.
https://arxiv.org/html/2610.14620v1
Positive results: Proposition1 eigenVALUE estimation dimension-independent for Hermitian row/column s-sparse A given sparse initial vector with nonzero leading overlap; retained sparsified power method Thm1 eigenVECTOR convergence additionally requires compressible leading eigenvector, oversampling and relative spectral-gap controls. Not every sparse algorithm and not arbitrary nonnormal projected operator.
Negative result: Proposition2 gives real symmetric TRIdiagonal 4x4 A with relative eigenvalue gap r in (0,1) and initial squared overlap delta in (0, 2(1-r)^3/((1+r)^2(2-r))) such that adaptive SUBMATRIX selection loses all target-eigenvector overlap in the first iteration and never regains it. This does NOT contradict positive sparse power guarantee: different algorithm. The selected submatrix can produce locally monotonically improving Rayleigh quotient but destroy global leading direction.
INDEPENDENT LOCAL NUMERIC INSTANCE from paper Sec 6 (algorithmically reconstructed in isolated numpy; no edited source): choose r=0.2, q=0.25, delta=0.1 and alpha=((1+q)^2*(2-q)/(2*(1-q)^3))*delta = 0.3240740740740741. Let
 c=sqrt((3-q)/(3+3*q)), s=sqrt(4*q/(3+3*q)), d=sqrt((1-q^2)/2), R=[[c,-s],[s,c]], C=R diag(1-q,(q-1)/2) R^T;
 A=[[C11,C12,0,0],[C21,C22,d,0],[0,d,q,0],[0,0,0,1-r]]
 and x0=[sqrt(alpha),0,0,sqrt(1-alpha)].
Independent numpy eigensolve (double precision):
 A≈[[0.45,0.497493719,0,0],[0.497493719,-0.075,0.684653197,0],[0,0.684653197,0.25,0],[0,0,0,0.8]]
 eig(A)=[-0.75,0.375,0.8,1.0];
 |<v_top,x0>|^2 ≈0.09999999999999994.
 First active set S1={1,2,4}; restricted eigensystem values [-0.375,0.75,0.8], winning unit eigenvector x1=e4; |<v_top,x1>|=0. Hence all subsequent selections retain e4 and never return the leading direction. Reproduced an EXPLICIT INSTANCE only, not full proof for all gaps/overlaps or DTC.
NASH directness: finite-Krylov/sparse compression/target-sufficiency pipelines need a target-direction retention certificate or a legal bias/bound; small selected local residual or monotonically improving local objective is insufficient. Not a PBH, physics, J3/K, NCDG or continuum theorem.

## 4. Quantum Fisher / trained readout — response budget vs usable observation (P1 high)
Primary: Phi Hung Nguyen, Daniel Soh, arXiv:2610.14454v1, Oct 10.
https://arxiv.org/html/2610.14454v1
Different source from Oct19 EPJC Krylov-QFI paper in audit008. This paper addresses QFI-aware training of quantum reservoir models for one task under fixed measured feature dictionary and retrained LINEAR readout.
Eq 2: L(theta,u)=min_w 1/2||y-X(theta,u)w||^2, w*=X^+ y, residual r=y-Xw*. On neighbourhood of FIXED MATRIX RANK, X^T r=0 and envelope theorem Eq3 D_v L=-r^T X_v w*.
Eq 7 gives chain of first-order response inequalities across classical-feature derivative and Fisher: ell_0 <= ell_perp <= ||X_v w*||/||w*|| <= ||X_v||2 <= ||X_v||F <= B_C(v) <= B_Q(v).
Eq 9 factorizes achieved slope:
  |D_v L| = ||r|| ||w*|| B_Q(v) product_{k=1}^5 eta_k(v)
with each 0<=eta_k<=1, linked to measurement info accessibility, features, readout, novelty beyond span X, and task alignment; when a denominator is zero treat on support as authors specify.
Corollary1: if v^T F_Q(t) v=0 for all observed samples t, NO choice of measurement/readout/target produces first-order loss gradient in v, for the declared state family. CONVERSE requires compatible observable accessing the SLD, not automatic task success.
Authors show the symmetry (J,h,tau)->(lambda J,lambda h,tau/lambda) leaves their Ising output invariant, v_sym proportional to (J,h,-tau) and QFI vanishes along it. QFI zero means no accessible FIRST-ORDER direction under this model, not fundamental all-experiments impossibility.
Numerical claims authors: on selected Mackey–Glass task JC reservoir 4–30 trained weights, held-out advantage vs matched echo-state network 25–69% and QFI-aware stage gain up to 51%. This is task/feature/model/budget dependent, not universal quantum computational advantage, and no independent experimental physics verification in this rotation.
NASH: PRF11 identifiability / measurement target / state-geometry vs readout geometry; flags that GENERATOR_ASYMMETRY_RESOURCE, QFI, CLASSICAL_FI, and held-out predictive utility are distinct quantities. Pair with Oct19 Krylov QFI hierarchy and 2026-03 KST prior art. No direct NASH physics.

## 5. Geometry/PDE convergence — ambient domain convergence does NOT guarantee operator convergence (P1)
Primary: F. Francesconi, J. Karatson, B. Lados, J. Rowlett, arXiv:2610.14946v1, Oct10.
https://arxiv.org/html/2610.14946v1
Nonsymmetric elliptic convection-diffusion -div(G grad u)+w.grad u=f with uniformly SPD G, divergence-free C1 drift w, Dirichlet boundary. GMRES/GCR residual bounds on S_h-weighted inner product tied to eigenvalues of positive elliptic operator/Laplacian.
Continuity under domain deformations when appropriate Hausdorff->gamma/Mosco convergence criteria: convex, uniformly Lipschitz, or planar bounded number of complementary connected components. Counterexample Ex3.23 "Ball Pit": D=(-1,1)^2, Sigma={0}x[-1/2,1/2]; Omega_k=D minus k tiny discs of radii e^(-k^2) with centers dense on Sigma. Domains converge geometrically in Hausdorff topology to Omega=D\Sigma but removed holes have capacity tending zero, so H_0^1(Omega_k) Mosco converges to H_0^1(D) != H_0^1(D\Sigma). Consequently Laplace eigenvalues / solver residual convergence do NOT automatically follow the naive limit domain. Contrasts Koch snowflake where continuity survives.
Mathematical host: need domain topology/capacity and norm/weighted inner product, not just mesh or geometric closeness; source-specific. This is conceptually relevant to masked grid geometry in NCDG, not automatically our discrete TT mask or Banach/Hilbert realization. Contrasts FEEC perturbation control which presupposes valid same-space operator comparison.

## 6. Host separation / result-level ranking
P0 governance and mathematical claim control: Fried explicit NL existential vs Lean conditional theorem. Exact proof-fidelity blocker and anti-self-sealing material. Import as negative-knowledge/source archive only.
P0 algorithmic negative control: sparse submatrix selection explicit 4x4 falsifier, useful for target-sensitive truncation tests; local numeric reproduction completed.
P1 boundary/spectrum distinctness: Toeplitz/GBZ pointwise corrections under restrictive symbol assumptions, NOT DTC.
P1 QFI vs task usable information: zero QFI impossibility plus product of five link factors; not automatic "quantum advantage for NASH".
P1 topology-aware nonnormal PDE: domain capacity and Mosco input to solver convergence, not arbitrary masked-grid result.

## 7. Source and version integrity
- arXiv 2610.22281 posted Oct15, 2610.13715 Oct09, 2610.14620 Oct10, 2610.14454 Oct10, 2610.14946 Oct10.
- Fried collaborator metadata anchored at immutable Git ref 610d659ea15af869553f6e3e79c432880d9b0ab0, not conflated with full paper peer review or full Lean manifold formalization.
- All papers preprints: proof claims source-native, NOT independently adjudicated.
- All source results are independent of NASH; borrowing a HOST does not certify project applicability. No claim on finite-to-continuum K/J3, BW acceptance, physical PBH/BBN, discovered physics, or author priority.

## 8. Computational reproduction script (NumPy) and expected semantics
```python
import numpy as np
r, q, delta = 0.2, 0.25, 0.10
alpha = ((1+q)**2 * (2-q) / (2*(1-q)**3)) * delta
c = np.sqrt((3-q)/(3+3*q)); s = np.sqrt(4*q/(3+3*q))
d = np.sqrt((1-q*q)/2)
R = np.array([[c,-s],[s,c]])
C = R @ np.diag([1-q,(q-1)/2]) @ R.T
A = np.zeros((4,4))
A[:2,:2] = C; A[1,2] = A[2,1] = d; A[2,2] = q; A[3,3] = 1-r
eig, V = np.linalg.eigh(A)
v_top = V[:,-1]
x0 = np.array([np.sqrt(alpha),0,0,np.sqrt(1-alpha)])
S = [0,1,3]  # zero-based first active set {1,2,4}
e_sub,U_sub = np.linalg.eigh(A[np.ix_(S,S)])
x1 = np.zeros(4); x1[S]=U_sub[:,-1]
assert np.allclose(eig,[-.75,.375,.8,1])
assert np.isclose(abs(v_top@x0)**2,.1)
assert np.isclose(abs(v_top@x1),0,atol=1e-14)
print(eig, abs(v_top@x0)**2, x1, abs(v_top@x1))
```
VALIDATION_SCOPE: explicit finite-dimensional counterexample only, independent numeric recomputation of author's parametric recipe. Not a claim about exact floating operations, full theorem proof, higher dimensions or empirical use.

FINAL: SCIENTIFIC_INTAKE_AND_NEGATIVE_KNOWLEDGE_ONLY / NO_EXEC / NO_CANON / BW_NOT_CONFIRMED.
