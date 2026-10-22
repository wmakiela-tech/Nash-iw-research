# XH-S4 — Research questions and cross-paper links, October 2026 (rotation 012)

RETURN_ID: XH-S4-OCT2026-QUESTIONS-LINKS-012_20261022

DATE: 2026-10-22; ROLE: external science source intake; NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_TASK_DISPATCH / BW_NOT_ASSUMED.

STANDARD: each source result -> research question -> typed literature links -> competing models -> measurable discriminator -> precise scope, evidence and blocking assumptions.



## Q1 / P0 / hidden-state identifiability and predictive memory

Source: Jiang, Andreou, Chen, arXiv:2610.22286v1, Oct15, https://arxiv.org/html/2610.22286v1. Defines model-conditioned fingerprint I_M(t,tau)=KL(p_M(Y_t|X_[0,t+tau]) || p_M(Y_t|X_[0,t])). Its trajectory average is conditional mutual information, though per-realization I need not increase monotonically with tau. Models sharing mean/variance/decorrelation can yield different fingerprints.

LINKS: PRF11 target-relative history / support-vs-law vs realization https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-18/IW_PRF11_FOUNDATION_IDENTIFIABILITY_DECISION_MEMORY_REPORT_001_20261018.md (direct host of observation semantics); Zhou/Koehler partial-measurement PEM-MHE arXiv:2610.16559v1 (complementary estimator); DALI 2610.02104 (distinct likelihood-geometry test).

QUESTION: does a different model-conditioned hidden fingerprint predict a genuinely different held-out observation law or intervention response, or only different latent semantics?

EXACT CONTROL (XH derivation, not source claim): Same observed X_t iid fair binary in both models. Model A Y_t=X_t => filter and smoother both point mass, I_A(t,1)=0. Model B hidden Y_t iid fair drives X_(t+1)=Y_t, with independent X_0 => filter Bernoulli(1/2), smoother point mass, I_B(t,1)=ln2. Full observable laws X identical. Consequently fingerprint difference alone cannot discriminate true model using passive X data. Fast test: compare future observed held-out distributions, then optional added observable or intervention. Falsifies automatic identification from different fingerprints. Same observed X law is a strict nonidentifiability obstruction.



## Q2 / P0 / DTC0a finite-N: alias vs projection vs operator norm

FEEC 2610.01501v1 establishes, on a same Hilbert space for bounded S,T, epsilon-pseudospectrum perturbation inclusion with delta=||T-S||_op. Poisson-GENERIC 2610.05570v2 has alias-free band-dependent discrete Jacobi, not generic full grid. Sparse leading-eigenvector paper 2610.14620v1 shows submatrix selection may drop target direction completely. EDGES: complementary numerical falsifiers, DIFFERENT actual operator hosts.

QUESTION: Is DTC0a K_A finite-N plateau invariant under admissible de-aliasing and projector/field-mask controls? H_alias (shrinks after de-alias); H_proj (sensitive to TT or field mask); H_state (RMS test field unrepresentative); H_stable (persists controls). Freeze N=31..41 odd grid, alpha, field/source class and normalization; crossed perturbation checks. Pseudospectral theorem only after common-space operator norm UPPER BOUND: single field RMS is insufficient. No continuum or K/J3 physical claim.



## Q3 / P0 / gravitational nonlocality and causal response

Matsui Oct19 2610.25994v1 https://arxiv.org/html/2610.25994v1: tree-level Lorentz-invariant Gaussian universal LINEAR conserved-source mediator. Visibility P, difference-source radiation/decoherence D and retarded conditional response C jointly give positive Kallen-Lehmann mass-shell weights and prevent gravity becoming universally weaker than Newtonian. Source notes STATIC bound is prior art; new P/D/C decomposition distinguishes prescriptions. Dirac 2610.06390 pole/residue branches and RR gravity 2610.20720 retarded Box^-1/homogeneous data are complementary PRESCRIPTION lessons but NONMAP field classes.

QUESTION: for a future explicitly defined Lorentzian NASH E(Box) candidate, does its physical source/response fit all Matsui hypotheses, and if yes which P/D/C fails under UV softening? H_in: legal on-shell kernel plus UV weakening entails violating P/D/C; H_out: representation/linearity/universality assumptions not met. First discriminator analytical kernel + source support + on-shell noise and commutator audit, not near-term interferometer signal. NO direct physical NASH inference.



## Q4 / P0 / BBN/PBH posterior shifts under crossed source systematics

B-mesogenesis 2610.03455v1, Phi-decay b-bar-b hadronic BBN source and Yp+D/H; differs from PBH Hawking donor. DALI 2610.02104v1 shows same data mismatch magnitude but distinct directions and nonlinear/nonadditive posterior shifts. Wu-Xu repository source scan uses Yp chi2=((Yp-.245)/.003)^2, with unresolved per-charge Q->R, below-table rates and exact execution provenance (XH 001-004, 008).

QUESTION: after legally freezing the PBH source+reaction map, do independent changes to charge split, subedge extrapolation and reaction calibration interact nonadditively in Yp,D/H and beta posterior? Test crossed 2x2 perturbations and interaction O_11-O_10-O_01+O_00, then recompute joint likelihood. BLOCKED until executable source, reaction inputs and observational covariance verified; NO numeric bound transfer.



## Q5 / P0 / scientific custody of wrong higher-level hypotheses

Maestro 2610.25920v1 replans proof DAG and removes no-longer-relevant formally proved lemmas; LeanPRM 2610.17697v2 predicts wrong steps but is NOT Lean at inference; Bolzano 2610.09769v2 uses LLM verifier with risk of durable mistaken lemmas; Fried 2610.22281v1 and pinned blawton/fried-conj-lean expose gap between conditional Lean resolvent theorem (16 hypotheses) and actual geometry/existential claim.

QUESTION: can a research state retain valid local lemmas yet retract all unsupported downstream claims across successor handoffs? Test a synthetic wrong parent with valid child lemmas, original NL versus formal statement mismatch, and audit-dependent demotion. Compare full immutable assumption ledger vs summary-only transfer; measure false acceptance and lost valid lemmas. This is an IW methodology QUESTION, not an assigned task nor an asserted new theorem.



## Q6 / P1 / metrological QFI versus useful task information

Nguyen/Soh 2610.14454v1 QFI upper bound with five link efficiencies for a fixed-rank refitted linear readout; published Oct19 EPJC Krylov-QFI DOI 10.1140/epjc/s10052-026-16434-0 (original arXiv February 2026) describes QFI Krylov-level truncations. Linked to PRF11 target-relative sufficiency and decision risks, but not identical host.

QUESTION: can finite Krylov truncation preserve almost all total quantum Fisher information while accessible classical FI or a fixed task's held-out decision value collapses? Control state, parameter direction, measurement dictionary, readout and K; compare QFI, accessible FI, task loss. Do not equate quantum resource amount and practical observability.



## Priority / acceptance

P0 Q1 exact nonidentifiability guard; Q2 finite grid falsifier; Q3 physical-host assumption audit; Q4 BBN crossed-systematics question subject to provenance; Q5 assumption dependency and correct status. P1 Q6. Literature-result statements, cross-paper inferences and XH-authored questions are not interchangeable. Source-only report: GitHub save is not owner acceptance, BW ingestion or EXEC.