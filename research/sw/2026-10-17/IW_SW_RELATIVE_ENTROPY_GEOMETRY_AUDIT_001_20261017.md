# Relative entropy, flux and geometry: contracts, obstructions and a perturbation-order test

artifact_id: IW_SW_RELATIVE_ENTROPY_GEOMETRY_AUDIT_001_20261017  
origin_cell: IW_SCIENCE_WORK_01 / SW  
as_of: 2026-10-17  
exposure: PUBLIC  
archive_mode: PUBLIC_ARTIFACT  
bw_ingestion_event_id: NOT_YET_INGESTED  
sync_state: GITHUB_PENDING_BW_INGEST  
status: AUTHOR_CHECKED / INDEPENDENT_REVIEW_PENDING  
claim_ceiling: CONDITIONAL_HOST_RECONSTRUCTION_AND_EXACT_SCOPE_TESTS; NO_NOVELTY; NO_CANON; NO_EXEC_SIGN

This is a bounded research audit, not a referee verdict on the entirety of any paper. The analytical tests below are SW's own reconstruction; their components have mature mathematical hosts. The independent NC analysis was not read before freezing this report. Public content consists of original analysis, brief source descriptions and bibliographic references; private manuscript and coordination records are excluded.

## 1. Decision

**Admit the relative-entropy/flux construction as a conditional case study. Do not promote it to a general derivation of geometry from information. Narrow the proposed AdS3 application to a linear functional until its perturbative interpretation is resolved.**

There are three different questions: whether a relative entropy is defined, whether it equals a geometric modular-energy functional, and whether a geometric response follows. Passing the first does not pass the other two.

The most material additional result of this audit is an interval-local diffeomorphism test. In the vacuum Bañados orbit, with fixed boundary endpoints and regulator, a nontrivial smooth interior excitation can have positive relative entropy at order epsilon squared while its exact RT geodesic-length difference is zero. This kills the **exact/leading-nonzero length-difference promotion**, not the algebraic identity obtained by feeding the stress profile into the first metric variation. Section 5 supplies the proof and explains why these statements coexist.

### Source versions and short dispositions

| Source | Version examined | Source-specific content and disposition |
| --- | --- | --- |
| Dorau–Much [DM] | arXiv:2510.24491v3; PRL 136, 091602 (2026) | Coherent scalar excitations on a horizon give a modular relative-entropy/weighted-flux relation. The metric response uses an area ansatz; the gravitational normalization requires a further area-entropy identification. Accept with explicit assumptions. |
| Dorau–Much–Verch [DMV] | arXiv:2603.13029v2, 30 September 2026 | The corrected Corollary 3.7 and Theorem 3.10 matter: formal associativity, finite-order localization, and a quotient symplectic construction are the relevant contracts. Corollary 5.2 gives a nonnegative order-theta-squared mixed-derivative contribution. No strict all-orders or cross-model monotonicity promotion. |
| Much–Dorau–Sangaletti–Verch [MDSV] | arXiv:2606.27915v1 | Equations (24)–(32) match an interval Schwarzian functional to a first metric variation. Their use as a nonzero approximation to the actual RT-length difference needs the order audit in section 5. |

## 2. Reconstructed theorem contract

The following is a **sufficient conditional contract**, assembled from the horizon/modular literature and the Jacobson argument [A, U, BW, C, L, CGP, KPV, J95]. It is not a new theorem or a claim that all hypotheses have been constructed simultaneously for every curved background.

Let a four-dimensional Lorentzian spacetime admit the declared local null-horizon construction. On each appropriate horizon algebra choose a faithful reference state with the required geometric modular flow and an admissible coherent excitation. Use a conserved stress tensor in one fixed renormalization prescription. Suppose the local relative-entropy/area equality holds with one constant coefficient for a sufficiently localizing family of patches and every null direction. Impose local equilibrium and control the terms discarded in Raychaudhuri's equation. Then the resulting null equation, together with conservation, has Einstein form, with a cosmological integration constant, at the retained order.

### Assumption ledger

| Gate | Required object or condition | What fails without it |
| --- | --- | --- |
| A1 | Legal globally hyperbolic neighborhood, null hypersurface, affine parameter and transverse measure | No well-typed horizon restriction or flux integral. |
| A2 | Declared Weyl/von Neumann algebra and coherent test data in the actual support/regularity class | A finite matrix formula does not define the horizon quantity. |
| A3 | Hadamard/quasifree reference where required; cyclic and separating representation; modular generator domain | Relative entropy may be infinite; a formal logarithm is insufficient. |
| A4 | A theorem identifying modular flow with the selected dilation/boost, including the scaling-limit scope | An arbitrary modular Hamiltonian is not local physical energy. |
| A5 | Coherent displacement and the correct ordered pair of states | Generic changes of state contain an entropy-change term. |
| A6 | One conserved, renormalized target stress tensor; reference subtraction explicitly recorded | A state-difference calculation is not automatically the absolute source of a new spacetime. |
| A7 | Constant entropy-area coefficient, with an independently declared metric/area response | Quantum distinguishability alone does not determine area. |
| A8 | Affine Raychaudhuri equation, vanishing initial expansion/shear to required order, hypersurface orthogonality | Extra optical terms or boundary data remain. |
| A9 | Localizing test family and all null directions at each point | One weighted moment or one null contraction does not determine a tensor. |
| A10 | Conservation, contracted Bianchi identity and compatible approximation order | The scalar trace completion and constant cosmological term do not follow. |
| A11 | A calibrated area coefficient and consistent units | The numerical gravitational coupling remains an input. |
| A12 | Error estimates and a reference-background prescription before promotion to a full coupled problem | No existence, uniqueness, backreaction or physical-stability theorem follows. |

### Calculation with distinct affine and Killing generators

Set c = k_B = 1 and retain hbar. Let lambda be negative on the past horizon, k = d/dlambda its affine null generator, and chi = -kappa lambda k the approximate boost generator. Do not use the same symbol for k and chi. Define

\[
 I_T=\int_H(-\lambda)T_{ab}k^ak^b\,d\lambda\,dA,
 \qquad \delta Q=\kappa I_T,
 \qquad D_{\rm coh}=\frac{2\pi}{\hbar}I_T=\beta\delta Q.
\]

Here beta = 2pi/(hbar kappa); normalization of the boost cancels. In the coherent free-field calculation the excitation contribution is quadratic in the classical displacement. Its extension to a generic state is not licensed [C, CGP].

Introduce the **additional response condition** D_coh = eta delta A. Linearized focusing with the declared boundary condition gives delta A = integral(-lambda) R_kk. Equality for all legal local tests yields

\[
 R_{ab}k^ak^b=\alpha T_{ab}k^ak^b,
 \qquad \alpha=\frac{2\pi}{\hbar\eta}.
\]

For every null k, the symmetric tensor E = R - alpha T must be proportional to g. To see this in an orthonormal frame, test k=(1,n), |n|=1, and k=(1,-n). Their difference forces E_0i=0; the remaining quadratic form is constant on the spatial unit sphere, so E_ij=-E_00 delta_ij. Conservation then gives

\[
 G_{ab}+\Lambda g_{ab}=\alpha T_{ab}.
\]

Choosing eta = 1/(4G hbar) fixes alpha = 8pi G. This fixes a normalization through an assumption; it does not measure or derive G. The local-to-tensor step is the mature Jacobson mechanism [J95].

For the coherent calculation, Delta T = expectation(T)_excited - expectation(T)_reference on the **same** background is especially clean: state-independent renormalization ambiguities cancel. Turning this into an absolute semiclassical equation additionally requires a reference solution and a renormalization scheme. Curvature counterterms cannot in general all be hidden in Lambda. This audit does not solve that coupled construction.

The area ansatz in [DM, equations (19)–(20)] selects the required area response; Raychaudhuri supplies its curvature interpretation. The argument is explanatory as a conditional equivalence/consistency construction. Calling it a derivation from quantum information alone would suppress A7–A12. The source itself invokes consistency across local horizons; A9 is a required retained assumption, not a newly discovered omission.

## 3. Cheap exact falsifiers of stronger statements

**One horizon does not fix the field equation.** In signature (-+++), take k=(1,1,0,0) and E=diag(0,0,1,0). Then E_kk=0 but E is not proportional to the metric. Likewise h(lambda)=lambda+2/3 on [-1,0] is nonzero although integral(-lambda)h(lambda) dlambda=0. These separate tensor identification from one successful flux comparison.

**An area bound is not an area equation.** Replacing equality by D <= eta delta A can yield a null inequality, not the vanishing of E_kk. Pointwise, T=0 and R_ab=t_a t_b with t=(1,0,0,0) give strictly positive R_kk for every nonzero null k while R is not proportional to g. This is an algebraic obstruction to the inference, not a proposed global gravitational solution.

**Distinguishability is not entanglement deficit.** For sigma=diag(3/4,1/4) and rho=X sigma X, the von Neumann entropy is unchanged but D(rho||sigma)=(log 3)/2>0. The identity

\[
 D(\rho\Vert\sigma)=\Delta\langle-\log\sigma\rangle-\Delta S
\]

explains the distinction [C, JLMS]. A local unitary preserves the regulated reduced-state spectrum. For continuum type-III algebras use relative modular theory rather than a nonexistent finite density-matrix entropy. No general entanglement-loss interpretation follows from positivity of D.

**Ordering matters.** With omega_U(A)=omega(U* A U), D(omega||omega_U) involves U* Omega, whereas the reverse order involves U Omega [H, P]. Weyl quadratic displacement formulas can hide this distinction. Virasoro formulas require checking the inverse diffeomorphism. The quadratic obstruction below is unchanged by epsilon -> -epsilon and therefore does not rely on choosing the favorable orientation.

## 4. Deformation: admissible information and remaining gaps

Keep the finite-order symplectic quotient and its KMS/reference-state assumptions explicit [DMV, Definitions 4.1–4.5]. The perturbative product does not supply a strict nonperturbative algebra on the original compact-support class. Nor does a formal state definition alone discharge every analytic existence/domain requirement needed in a new application.

Our interpretation of the second-order quadratic form is:

* Sensitivity depends on the chosen excitation and angular derivatives. A vanishing derivative removes this coefficient only where that excitation is legal. A globally angle-independent mode is not a nonzero compactly supported function in a single open angular chart.
* Increasing angular frequency can increase the derivative coefficient. A small parameter is therefore not a uniform small-error statement over all smooth excitations; a controlled Sobolev/spectral class and remainder bound are needed.
* A positive even coefficient neither identifies the sign of the deformation parameter nor establishes monotonicity at finite deformation.
* Comparing two numbers obtained from different deformed algebras is a parameterized diagnostic. It is not the data-processing inequality without an actual state/channel or algebra-transport map.

The useful surviving problem is to specify that common experiment or transport, including the state and reference state. It is not enough to identify two parameters because both occur in descriptions called nonlocal.

## 5. AdS3 discriminator: exact length versus first metric variation

### Precisely delimited test

Use a unitary chiral sector with c>0, the vacuum Bañados orbit, one chiral boundary diffeomorphism, the same boundary interval I=(-1,1), fixed endpoint regulators, and sufficiently small smooth deformations to stay on the vacuum-connected extremal-geodesic branch. This tests a **pure-gravity holographic realization**, conditional on that dictionary; it does not assert that an arbitrary chiral net has a semiclassical gravity dual.

Choose any nonzero real g in C_c^infinity((-1/2,1/2)), for example

\[
 g(u)=\begin{cases}\exp[-1/(1-4u^2)],&|u|<1/2,\\0,&|u|\geq1/2.\end{cases}
\]

Let f_epsilon=Exp(epsilon g) be its flow. It equals the identity in neighborhoods of both endpoints, with endpoint derivatives one. It defines an interval-local Virasoro unitary in the standard host [H, P].

### Exact geometric side

The endpoint transformation law for a vacuum descendant [R, equation (14)] gives, in the one-chiral sector,

\[
 \frac{\Delta L_{\rm RT}}{4G}
 =\frac{c}{12}\log\!\frac{[f_\epsilon(1)-f_\epsilon(-1)]^2}
 {4 f_\epsilon'(1)f_\epsilon'(-1)}=0.
\]

Both the cutoff rescaling and endpoint displacement vanish here. This concerns the actual renormalized length difference; it is not obtained by truncating the metric integrand on the original path. Local isometry to AdS does not remove boundary-graviton charges in general, but endpoint identity suffices for this length statement.

### Relative-entropy side and independent expansion

The bounded-interval Schwarzian formula, with the appropriate ordered pair/inverse convention [P, section 5], has no endpoint terms in this example. Write w(u)=(1-u^2)/2. Its positive quadratic coefficient is

\[
 D_\epsilon=\frac{c\epsilon^2}{24}Q[g]+O(\epsilon^3),
 \qquad Q[g]=\int_{-1}^1\{w(g'')^2-(g')^2\}\,du.
\]

Here is a direct derivation of the coefficient. For f=u+epsilon g+epsilon^2 h+O(epsilon^3),

\[
 \{f,u\}=\epsilon g'''+\epsilon^2[h'''-g'g'''-\tfrac32(g'')^2]+O(\epsilon^3).
\]

All boundary jets vanish. Since w'''=0, the g''' and h''' moments vanish. Integration by parts gives

\[
 \int w[-g'g'''-\tfrac32(g'')^2]=-\tfrac12 Q[g].
\]

The flow has h=gg'/2, which therefore does not change the coefficient. For support in (-a,a), the Dirichlet Poincare inequality applied to g' gives

\[
 Q[g]\geq\left[\frac{(1-a^2)\pi^2}{8a^2}-1\right]\int(g')^2.
\]

At a=1/2 the bracket is 3pi^2/8-1>0. Thus every nonzero such smooth bump has D_epsilon>0 for sufficiently small nonzero epsilon, while the exact length difference above is zero. The same positive Hessian applies to the reversed state order.

### What this does and does not falsify

Let h_epsilon=epsilon h1+epsilon^2 h2+... be the metric family. For the extremal-length functional L,

\[
 L(g_0+h_\epsilon)-L(g_0)
 =L'[\epsilon h_1+\epsilon^2 h_2]
   +\tfrac12\epsilon^2 L''[h_1,h_1]+O(\epsilon^3).
\]

In this example L'[h1]=0. Evaluating the first derivative on the **full** source profile can retain L'[epsilon^2 h2], but the discarded Hessian/path term is of the same order and cancels it in the exact length. Therefore an O(h^2) absolute remainder is insufficient to establish a nonzero leading relative-entropy/length correspondence when D itself starts at O(epsilon^2).

The functional matching in [MDSV] can survive as a first-metric-variation identity. The statement that it controls the actual length difference through its first nonzero order fails this test. A linear-order assertion along the state family is merely 0=0 here. **Disposition: NARROW; no blanket retraction claim.**

The appropriate mature comparison at quadratic order is relative-entropy Hessian versus canonical energy, including gravitational and surface contributions [LV]. Absence of local propagating gravitons in three dimensions does not justify dropping boundary/symplectic contributions. FLM/JLMS are separate, regime-dependent statements [FLM, JLMS], not a way to identify relative entropy with area alone.

### Reproducible algebra checks

The accompanying standard-library script performs 12 exact checks. For the C3 zero-extension of (1-4u^2)^4 on [-1/2,1/2], it obtains Q=65536/455 and Q/24=8192/1365. This polynomial is only an exact integration control; the C-infinity admissible example is established by the analytical inequality above. The code is not a CFT, metric or geodesic solver and is not independent peer review.

Reproduction entrypoint: `runtime/sw/2026-10-17/relative_entropy_exact_checks.py`. Run it with Python 3.12 and compare stdout with `research/sw/2026-10-17/relative_entropy_exact_results.json`. The manifest is `manifests/reproduction/sw/2026-10-17/relative_entropy_geometry_audit.json`.

## 6. Genealogy and subtraction

| Host | Contribution used here | Boundary retained |
| --- | --- | --- |
| Araki [A]; Uhlmann [U] | Relative entropy beyond commuting probabilities; modular/operator formulation. | Finiteness and representation domains remain substantive. |
| Bisognano–Wichmann [BW]; Casini [C] | Geometric modular generator in the wedge; distinguishability/energy/entropy budget. | No arbitrary-region or arbitrary-state local-energy formula. |
| Longo [L]; Casini–Grillo–Pontello [CGP]; Hollands [H]; Panebianco [P] | Coherent Weyl and Virasoro calculations; bounded-interval and ordered-pair control. | Weyl coherence and Virasoro coherence are different constructions. |
| Kurpicz–Pinamonti–Verch [KPV] | Horizon scaling-limit and entropy/area genealogy. | Its dynamical spherical setting is not every local horizon. |
| Jacobson [J95, J16] | Local horizon equation of state; later small-ball entanglement-equilibrium route. | The two routes have different equilibrium/state assumptions; neither removes the area input by nomenclature. |
| Ryu–Takayanagi [RT]; Roberts [R] | Extremal geometry and transformed endpoints. | Holographic dictionary, regulator and branch must be fixed. |
| Faulkner et al. [FGHMR]; FLM; JLMS | Entanglement constraints, quantum corrections, bulk/boundary modular structure. | Linearized/semiclassical orders, code subspace and bulk terms cannot be erased. |
| Lashkari–Van Raamsdonk [LV] | Quadratic relative entropy and canonical energy. | Full gravitational symplectic/boundary accounting is required. |
| Faulkner–Hollands–Swingle–Wang [FHSW] | Recovery controlled by relative-entropy loss for general von Neumann subalgebras. | Requires an actual algebra inclusion/reference-state contract. |

This is a selected, dependency-driven genealogy, not a systematic review proving exhaustiveness or novelty. The 2026 work is useful as source-specific synthesis and deformation analysis. The task for IW is to exhibit legal objects and maps and to preserve perturbation order; vocabulary alone contributes no theorem.

## 7. Ranked implementation options

| Rank / use | Types, domains and maps | Falsifier or kill criterion | Ceiling / residual |
| --- | --- | --- | --- |
| 1. Book case and host atlas | Horizon algebra, reference/excited state, geometric modular generator, conserved flux, area response and all-null completion as separate edges. Sources: J95, C, CGP, DM. | A missing state/domain/area/normalization edge blocks the corresponding conclusion. | Mature host; conditional scientific case. Owner chooses placement. |
| 2. Operational information budget | A fixed physical state pair and one common CPTP measurement/restriction map: D(classical outcomes) <= D(quantum states). For algebraic generalization use actual inclusions and FHSW. | Different preparations, references or testers on the two sides; missing support/finite-D conditions. | Standard data processing/recovery. Residual: constructing the source-native experiment, not reproving DPI. |
| 3. Bounded deformation comparison | Finite-order symplectic carriers; a specified symplectic transport inducing a Weyl *-map, transported reference states and modular dynamics, or a common measurement experiment. | A numerical entropy comparison without such a map; nonuniform high-frequency remainder; illegal zero mode. | Parameter-sensitive diagnostic only. Residual: well-posed transport and controlled remainder for the chosen class. |
| 4. AdS example after order repair | Fixed vacuum orbit, interval, regulator, diffeomorphism convention; distinguish L'[h] from Delta L and from canonical energy. Sources: P, R, LV. | Interior compact flow in section 5. | Current actual-length promotion fails. Retain the obstruction and first-variation identity; independent review pending. |
| 5. Empirical theory discrimination | Two physical models mapped to probability laws for the same preparation and instrument; nuisance parameters and accessible statistics declared. | Identical outcome laws, inaccessible modular observables or differing instruments. | Classical/quantum distinguishability of the declared models; no mediator attribution or gravity test from a horizon formula alone. |

### Exact nonmaps and the current research language

* **Reduction/identifiability/process:** a scalar relative entropy is not a point-separating family and does not determine multi-time statistics. Add legal preparations and intervention testers before discussing process equivalence. A successful scalar witness can establish failure of a stronger equivalence; its agreement does not establish that equivalence.
* **QRF:** finite-dimensional Umegaki entropy belongs to the broader operator-algebraic family. A change of frame preserves D when it transports the algebra and both states by the same isomorphism. That is a valid structural connection. It does not embed the existing finite-spin experiment into a horizon net or identify its pinching reference with a KMS state. A fixed reference/pinching operation and a co-transformed one answer different questions [P, Lemma 3].
* **TC-E1:** a channel's ability to transmit quantum information or generate entanglement is different from the relative entropy of two horizon states. A shared experimental likelihood family could connect the discrimination questions, but would not by itself locate the mediator carrying the information.
* **NCDG/DTC:** a unary form factor E(Box) and a bilinear star product have different types. A compression defect K/J3 is not a state pair. A bridge would require a legal state algebra and positive states built from the specific model; an explicit parameter/carrier map; compatible dynamics/reference modular data; a renormalized stress prescription; and a common measurable output. None is supplied by the shared word 'nonlocal'.

An information-loss/recovery atlas can make the field coherent by keeping these typed edges visible. It should not demand one physical mechanism for every occurrence of a similar mathematical functional.

## 8. Proved / conditional / unresolved

**Established in this audit:** the elementary one-moment and one-null counterexamples; the conditional null-to-tensor argument; the smooth compact-flow order discriminator using stated CFT and geometric host formulas; 12 exact algebra controls.

**Source-supported, not independently reconstructed in full:** the modular/coherent-state theorems, finite-order deformed symplectic/KMS construction, holographic dictionaries and recovery theorem. Reading their statements or selected derivations does not certify every analytic hypothesis.

**Unresolved:** independent review of the AdS interpretation, any complete nonlinear backreacted existence theorem, uniform deformation remainders on a declared function class, physical state/algebra maps for NCDG/DTC, empirical implementation and any novelty assessment.

The minimal next scientific action is an independent check of section 5 against the exact endpoint formula and the state/metric parameter expansion. That lies within this bounded audit. No additional research campaign, automatic manuscript edit or physical promotion is authorized by this report.

## References

Bibliographic data are also exported in `relative_entropy_sources.bib`; retrieval depth and limitations are recorded separately.

* [DM] P. Dorau, A. Much, *From Quantum Relative Entropy to the Semiclassical Einstein Equations*, PRL 136, 091602 (2026). [doi:10.1103/lmq8-nsty](https://doi.org/10.1103/lmq8-nsty), [v3](https://arxiv.org/html/2510.24491v3), equations (10)–(28).
* [DMV] P. Dorau, A. Much, R. Verch, *Noncommutative QFT and Relative Entropy on Axisymmetric Bifurcate Killing Horizons*, [2603.13029v2](https://arxiv.org/html/2603.13029v2), sections 3–5.
* [MDSV] A. Much, P. Dorau, L. Sangaletti, R. Verch, *A UV-Finite Ryu-Takayanagi Relation from Relative Entropy in AdS3/CFT2*, [2606.27915v1](https://arxiv.org/html/2606.27915v1), equations (7)–(9), (24)–(38).
* [A] H. Araki, *Relative Entropy of States of von Neumann Algebras*, Publ. RIMS 11, 809–833 (1976). [Publisher](https://ems.press/journals/prims/articles/2800).
* [U] A. Uhlmann, *Relative entropy and the Wigner-Yanase-Dyson-Lieb concavity in an interpolation theory*, CMP 54, 21–32 (1977). [doi:10.1007/BF01609834](https://doi.org/10.1007/BF01609834).
* [BW] J. J. Bisognano, E. H. Wichmann, *On the duality condition for a Hermitian scalar field*, JMP 16, 985 (1975). Primary locator: [DM], reference 37; publisher retrieval failed in this pass. The geometric modular statement is corroborated in [C, H].
* [J95] T. Jacobson, *Thermodynamics of Spacetime: The Einstein Equation of State* (1995). [gr-qc/9504004v2](https://arxiv.org/html/gr-qc/9504004v2).
* [J16] T. Jacobson, *Entanglement Equilibrium and the Einstein Equation*, PRL 116, 201101 (2016). [1505.04753](https://arxiv.org/abs/1505.04753).
* [C] H. Casini, *Relative entropy and the Bekenstein bound* (2008). [0804.2182v3](https://arxiv.org/html/0804.2182v3).
* [L] R. Longo, *Entropy of Coherent Excitations* (2019). [1901.02366](https://arxiv.org/abs/1901.02366).
* [CGP] H. Casini, S. Grillo, D. Pontello, *Relative entropy for coherent states from Araki formula* (2019). [1903.00109](https://arxiv.org/abs/1903.00109).
* [H] S. Hollands, *Relative entropy for coherent states in chiral CFT*, LMP 110, 713–733 (2020). [1903.07508v2](https://arxiv.org/pdf/1903.07508v2), equations (3.22)–(4.32).
* [P] L. Panebianco, *A formula for the relative entropy in chiral CFT* (2020). [1911.10136v3](https://arxiv.org/html/1911.10136v3), Lemma 3 and section 5.
* [KPV] F. Kurpicz, N. Pinamonti, R. Verch, *Temperature and entropy-area relation of quantum matter near spherically symmetric outer trapping horizons* (2021). [2102.11547v2](https://arxiv.org/abs/2102.11547v2).
* [RT] S. Ryu, T. Takayanagi, *Holographic Derivation of Entanglement Entropy from the anti–de Sitter Space/Conformal Field Theory Correspondence*, PRL 96, 181602 (2006). [doi:10.1103/PhysRevLett.96.181602](https://doi.org/10.1103/PhysRevLett.96.181602).
* [R] M. M. Roberts, *Time evolution of entanglement entropy from a pulse* (2012). [1204.1982v1](https://arxiv.org/html/1204.1982v1), equations (13)–(16).
* [FGHMR] T. Faulkner, M. Guica, T. Hartman, R. C. Myers, M. Van Raamsdonk, *Gravitation from Entanglement in Holographic CFTs* (2014). [1312.7856](https://arxiv.org/abs/1312.7856).
* [FLM] T. Faulkner, A. Lewkowycz, J. Maldacena, *Quantum corrections to holographic entanglement entropy* (2013). [1307.2892](https://arxiv.org/abs/1307.2892).
* [JLMS] D. L. Jafferis, A. Lewkowycz, J. Maldacena, S. J. Suh, *Relative entropy equals bulk relative entropy* (2016). [1512.06431](https://arxiv.org/abs/1512.06431), sections 1–2.
* [LV] N. Lashkari, M. Van Raamsdonk, *Canonical Energy is Quantum Fisher Information* (2016). [1508.00897v2](https://arxiv.org/html/1508.00897v2), sections 1–2.
* [FHSW] T. Faulkner, S. Hollands, B. Swingle, Y. Wang, *Approximate recovery and relative entropy I: general von Neumann subalgebras* (2020/2021). [2006.08002v1](https://arxiv.org/abs/2006.08002v1).
