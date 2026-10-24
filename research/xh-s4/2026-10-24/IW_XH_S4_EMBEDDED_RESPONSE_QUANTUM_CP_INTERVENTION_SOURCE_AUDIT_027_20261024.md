# XH-S4 — obrót 027: pełny stan ukryty, response theory, kwantowa CP i interwencje
RETURN_ID: XH-S4-20261024-EMBEDDED-RESPONSE-CP-DIVISIBILITY-CROSS-PROTOCOL-027
DATE: 2026-10-24
CELL: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03 / XH-S4
SOURCE_WINDOW: May 1–October 24, 2026
CLASS: SIX+ PRIMARY 2026 SCIENCE SOURCES / EXACT CLASSICAL-QUANTUM FINITE CONTROLS / Q85–Q92
CLAIM_CEILING: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_NASH_KJ3 / NO_BW_INGESTION / NO_NEW_OWNER_TASK / NO_QG_MEM_MECHANISM.
Definitions, exact numerical values and executable Python are present additionally in locally clean-replayed ZIP IW_XH_S4_027_REPRODUCIBILITY.zip (SHA256 e5a1956c67ce76043b6819f1a1426d81ab93df7639a9799526c644b5de7ddf4c).

## 1. Scientific leap from XH026
Memory **realization**, predictive sufficiency, and positivity admissibility (XH026) have a further operational axis: the adequacy of **intervention response and multi-time data**. Accurate stationary marginal p(x) or one passive response point can mispredict interventional susceptibility. Quantum dynamical maps from t0 may all be CP while intermediate maps are not CP. A history-of-states CPNS model differs in scope from a process tensor with arbitrary history of controls. These are different tests, not one theorem.

## 2. New and current SOURCE-NATIVE paper atlas, exact dates and limits
A. Charlotte Bäcker, Valentin Link, Walter T. Strunz, *Verifying quantum memory in the dynamics of spin-boson models*, Phys Rev Research 8 023106 published MAY 4 2026, DOI https://doi.org/10.1103/5bfc-znkj .
Primary APS abstract: two criteria for genuinely quantum memory, one using dynamical maps and another requiring a single-intervention process tensor; numerically exact MPO influence functional simulated spin-boson and coupled two-spin-boson hosts, quench and correlated stationary system+bath preparations. Authors find intervention access often detects quantum memory in low-temperature regimes where map-only diagnosis is weaker; maps sometimes detect resonant low-time effects. Do NOT equate CP-indivisibility with source's stronger quantum-memory witness. Full equations/PDF not audited.

B. Serhii Kryhin and Vivishek Sudhir, *Completely-positive non-signalling non-Markovian dynamics*, arxiv 2605.03197v2 MAY 6 (original MAY 4) 2026, FULL https://arxiv.org/html/2605.03197 . Authors axiomatize discrete history-of-**states** maps under complete positivity, trace preservation and non-signalling, derive a continuous-time memory-GKSL form:
 d rho(t)/dt = L[rho(t)] + int_(t0)^t dt' sum_a (R_a† rho(t')R_a − (1/2){R_a R_a†,rho(t)}).
The jump term acts on PAST rho(t'), the anticommutator on PRESENT rho(t): this temporal asymmetry is load-bearing for their axiom class. Boundedness/integrability restrictions matter; unbounded operator converse not established. Their class is narrower than **all** quantum process tensors with freely varied interventions; no NASH quantum-memory theorem. They discuss multi-time measurement correlations. Claimed PSD class: integrable power spectra under source assumptions.

C. Antonio Sannia, Ricard Ravell Rodríguez, Gian Luca Giorgi, Roberta Zambrini, *Non-Markovianity and memory enhancement in quantum reservoir computing*, npj Quantum Information 12 111 published MAY 8 2026, https://www.nature.com/articles/s41534-026-01257-4 . In specified QRC reservoir benchmark, past information under Markov evolution decays exponentially; auxiliary qubits/partial SWAP retain information and can help selected prediction tasks. NOT general 'all Markov memory useless', no physics evidence for NASH.

D. Jonathan Keeling, E. Miles Stoudenmire, Mari-Carmen Bañuls, David R. Reichman, *Process Tensor Approaches to Non-Markovian Quantum Dynamics*, Phys Rev X 16 020502 published JUNE 22 2026, DOI https://doi.org/10.1103/1ncg-11hz . Perspective/review of process tensor interventions and efficient tensor-network algorithms; not new empirical measurement or proof of every model's scaling.

E. Rémi Goerlich, Antoine Tartar, Yael Roichman, Igor M. Sokolov, *Fluctuation-response relation for a nonequilibrium system with resolved Markovian embedding*, Phys Rev E 114 014138 published JULY 20 2026 DOI https://doi.org/10.1103/kldw-kftz . **Physical experiment**: optically confined colloidal particle in controlled colored noise, respond to confinement STIFFNESS perturbation. Reduced steady-state equilibrium-like response relation fails; in full Markov embedding a particular conjugate observable gives the quantitative response. Publisher abstract verified; XH numerical 43% discrepancy is our own independent OU toy, NOT source's measurement. Do not transplant colloid to metric memory.

F. E. K. Jaradat, M. Noman et al., *Operational Signatures of Non-Markovian Memory: Entanglement Revivals and Multi-Time Metrology in a Qubit Pseudomode Channel*, Annalen der Physik 538 e70249 FIRST JULY 24 2026, DOI https://doi.org/10.1002/andp.70249 . Qubit+cavity pseudomode, CP-divisibility test/intermediate Choi, restricted trace-distance backflow proxy, entanglement revival and time-budgeted detuning QFI. Abstract explicitly disclaims optimized BLP from restricted proxy and assumes zero reset-time cost. No resource-theory proof; full model equations not audited.

G. Ridha Horchani, *Coherence-selective non-Markovian qubit dynamics*, Quantum Information Processing 25 308 SEPTEMBER 2026 DOI https://doi.org/10.1007/s11128-026-05336-5 . Source university abstract: constrained broadband+finite-linewidth oscillatory kernel; exact 4D auxiliary realization and Routh-Hurwitz poles, CP checked separately via |G(t)|<=1, free-induction Ramsey and controlled Hahn echo. Synthetic cross-protocol failure for fitted one-component kernels. Full paper not audited.

SOURCE-TYPED EDGE: Bäcker (memory witness on intervention tensor) != Kryhin (history-of-states CPNS) != Jaradat (CP-divisibility/backflow proxy) != Sannia (task predictive memory) != Goerlich (actual nonequilibrium response) != Horchani (echo protocol). No automatic equivalence.

## 3. XH independently reproduced control 1: colored-noise OU, hidden state changes stiffness response
Synthetic 2-state SDE:
 dx=(-k x+eta+f)dt,
 d eta=−gamma eta dt + sqrt(2 gamma sigma²) dW;
 k=1, gamma=3, sigma²=1. Drift A=[[-1,1],[0,-3]], noise Q=diag(0,6).
Exact stationary covariance AC+CA^T+Q=0:
 C=[[1/4,1/4],[1/4,1]], inverse C^-1=[[16/3,-4/3],[-4/3,4/3]].
Perturb stiffness k by delta k: change drift F=(-x,0). Full steady Gaussian conjugate observable (Agarwal response) B_full=−div(F p)/p=1−x(C^-1 [x,eta])_x. A reduced p(x)-only score B_x=1−x²/Cxx.

Analytic causal stationary Cxx(t)= (3/8)e^-t − (1/8)e^-3t. Full linear response of x² to instantaneous stiffness:
 R_full(t)=E[x(t)^2 B_full(0)] = −2 Cxx(t)e^-t.
Reduced surrogate response: R_x(t)=−2 Cxx(t)^2/Cxx(0).
At t=1: full −0.0969225527053, reduced −0.138825308497, relative error 0.43233235838 (43.23%). Additive force response full e^-1=.36787944 vs reduced .52692563, but experimental paper changes stiffness not force.
Independently checked with finite pulse of delta k=.001 during dt=.0001, propagated covariance via separately perturbed continuous-time Lyapunov solution: finite-pulse R=-0.0969317792698 at t=1, differs from analytic impulse by 9.23e−6 (finite duration). Residual stationary Lyapunov <5e−15. No claim actual colloid data or calibration reproduced.
FALSIFIER: equal stationary p(x) or low one-time trajectory metric does not guarantee equal susceptibility; compare experimentally measurable response to changes in stiffness/forcing, and source-conjugate variables.

## 4. XH independently reproduced control 2: CPTP t0->t does not imply CP divisible
Qubit phase damping with G(t)=exp[−a(1−cos t)], a=.8, |G(t)|<=1. Each map Phi_t(rho)=p(t)rho+(1-p(t)) Zrho Z, p=(1+G)/2 is CPTP. Its normalized Choi spectrum: (1+G)/2, (1−G)/2, 0,0.
At s=pi, t=2pi, intermediate dephasing factor G(t)/G(s)=exp(1.6)=4.953032424395116, Choi min eigenvalue (1−factor)/2=−1.976516212197558. Not CP. Instantaneous decay rate −d log G/dt=a sin t negative in part of period. The family is compatible with quantum channels from fixed t0 but NOT CP-divisible; this *does not by itself prove necessary genuinely quantum environmental memory* in sense of Bäcker process tensor. Completely independent toy, not Jaradat pseudomode or Kryhin history-of-states source model.

## 5. XH independently reproduced control 3: one-time free agreement vs controlled echo
Static Gaussian frequency disorder sigma=1 has free coherence G_s(T)=exp(−sigma² T²/2). White Markov dephasing gamma=.5 gives G_M(T)=exp(−gamma T). At T=1 both equal exp(−.5)=0.6065306597126334; IDEAL Hahn echo perfectly refocuses the quasi-static source G_s,echo=1, but Markov dephasing remains 0.6065306597126334. One matched point is NOT equivalence of entire free curves. The result is an exact methodological toy of cross-protocol prediction, not a replication of Horchani. Assumes perfect instantaneous toggles and no pulse/reset cost.

## 6. New questions Q85–Q92, competing hypotheses and cheap discriminators
Q85 P0: Is the conjugate observable for an intended response defined on full Markov embedding or only a reduced marginal? OU stiffness test supplies exact 43.23% error for the latter.
Q86 P0: Can distinct latent auxiliary realizations sharing passive predictions be separated by a controlled, recorded intervention on a physical variable? Define action and actual source/observable response.
Q87 P0: distinguish CPTP from fixed beginning, intermediate CP-divisibility and TRUE quantum-memory criteria requiring controlled tensor process. The dephasing toy splits first two; Bäcker source splits last.
Q88 P0: Are measurements with a single intervention/initial system-bath correlations actually accessible or only zero-intervention maps? Bäcker intervention tensor vs Kryhin history-of-states maps have DIFFERENT host assumptions.
Q89 P0: Does an independent Ramsey-vs-echo or perturbation/response experiment falsify a fitted effective memory kernel? One-time free matching counterexample PASS.
Q90 P1: Are quantum-memory task gains robust at equal use count, reset-time, control and observation budgets? Jaradat source explicitly assumes fresh baths with no reset-time cost.
Q91 P0: What is precise CPNS vs process tensor mathematical target and whether NASH really needs quantum CP at all? Classical metric memory has no automatic quantum-channel interpretation.
Q92 P1: Does QRC prediction improvement measure physical admissibility, kernel uniqueness, or just target-relative information retention? Sannia QRC only supports task-specific prediction.
No tasks assigned to other cells; Moderator retains final EXEC. No physical NASH, K/J3, gravity dynamics, false cosmology/pseudomode extrapolation.

## 7. Repro and custody
Local source xh_s4_027_embedding_CP_process_controls.py, local result xh_s4_027_results.json and full Markdown report plus MANIFEST_027.json and README, all inside IW_XH_S4_027_REPRODUCIBILITY.zip.
Clean isolated temporary directory: unzip, CRC PASS, run NumPy/SciPy source exit0, new JSON byte-identical SHA256 4ba10bb13b896766245de897ca6f77b5fa6d55149b8c73030493ed2832d897f7, manifest verification PASS. ZIP SHA256 e5a1956c67ce76043b6819f1a1426d81ab93df7639a9799526c644b5de7ddf4c.
Repo receipt and Slack dispatch require SEPARATE confirmations. Full local report is in ZIP, not assumed in BW.
