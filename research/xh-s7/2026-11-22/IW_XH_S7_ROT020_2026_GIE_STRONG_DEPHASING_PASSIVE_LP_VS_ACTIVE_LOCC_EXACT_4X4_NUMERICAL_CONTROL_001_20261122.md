---
artifact_id: IW_XH_S7_ROT020_2026_GIE_STRONG_DEPHASING_PASSIVE_LP_VS_ACTIVE_LOCC_EXACT_4X4_NUMERICAL_CONTROL_001_20261122
date: 2026-11-22
cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_06 / XH-S7
exposure: PUBLIC
role: EXTERNAL_PRIMARY_SCIENCE_HARVEST / NOV2026_ORIGINAL_THEORETICAL_PHYSICS / INDEPENDENT_FALSIFIABILITY_TEST
scientific_mode: ORIGINAL_PRIMARY_SOURCE_READ / TWO_SURFACE_PRIOR_ART / NEGATIVE_KNOWLEDGE / PHYSICAL_HYPOTHESIS_CLASS_TYPED / INDEPENDENT_4X4_MATRIX_REPLAY
status: SOURCE_ARXIV_V2_TEXT_READ / ORIGINAL_PDF_SCREENSHOT_CACHE_MISS / PYTHON_NUMPY_ACTUALLY_EXECUTED_PASS / DIRECT_PPT_MATRIX_AND_CLOSEST_PASSIVE_TRACE_DISTANCE_PASS / ACTIVE_FEEDBACK_WITNESS_MATCH_EXECUTED_PASS / NO_LAB_DATA
claim_ceiling: MATHEMATICAL_MODEL_ONLY / CLASSICAL_LP_REJECTION_NOT_ALL_LOCC / NOT_DEVICE_INDEPENDENT / NO_GRAVITATIONAL_OBSERVATION / NO_NASH_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync: GITHUB_PENDING_BW_INGEST
---

# XH-S7 ROT020 — Quantum gravity conditional-phase test without final entanglement: exact passive LP gap and an explicit active-LOCC negative control

Execution date 22 November 2026; one-letter O autonomous external rotation. Standing user preference: original SCIENCE FIRST and external literature first, not repetitive NASH internal status reports. Research was triggered by recent specialist 2026 quantum-gravity research, not by an existing internal physics programme run. The external source is ONLY a theoretical preprint; no gravitationally-induced entanglement was experimentally detected.

## 0. Primary source access, date, source typing and previous prior art

Tianfeng Feng and Vlatko Vedral, **"Testing non-classical gravitational phase dynamics under strong dephasing"**, arXiv:2611.12229, v1 submitted **9 November 2026**, v2 revised **10 November 2026**.
Original arxiv landing https://arxiv.org/abs/2611.12229
Accessible original source v2 technical PDF https://arxiv.cnoctave.top/pdf/2611.12229
Full original primary author PDF **web-extracted TEXT ACTUALLY READ** including source Eqs 1–5, 9–15, 20–24, Theorem 1, partial-transpose criterion, Section IV active diagonal-PPT class, appendix proof and author explicit experimental calibration caveats; screen page 0 and 4 called per PDF inspection requirement but returned CACHE MISS. DO NOT claim figures themselves independently visually inspected or supplementary experimental bytes downloaded. The paper is PREPRINT, not an experimental result or a verified independent referee-certified global physical conclusion.

Motivation: standard two-path BMV phase setup with fixed local dephasing may be final-state separable for all t while one specifically quantified measurement differs from a **passive path-local stochastic phase mediator**. Active measurement-and-feedback classical mediator can also generate conditional phase-like correlations with a disturbance cost, so the hypothesis class is THE critical physical information.

**Two-surface prior art, subtracting novelty**:
A) 2017 Bose et al PRL 119 240401, DOI https://doi.org/10.1103/PhysRevLett.119.240401 and Marletto & Vedral PRL 119 240402, DOI https://doi.org/10.1103/PhysRevLett.119.240402: BMV gravitationally induced entanglement witness and LOCC assumptions.
B) Crucial contemporary closest 2024 published **Lami, Pedernales, Plenio**, "Testing the Quantumness of Gravity without Entanglement", Physical Review X **14 021022 (1 May 2024)** DOI https://doi.org/10.1103/PhysRevX.14.021022, and first arxiv:2302.03075 Feb 2023, already showed LOCC-simulation inequality and nonclassical-gravity detectability without final entanglement. Feng/Vedral do NOT invent nonentangling gravity tests or general LOCC separation. Their 2026 original *distinct contribution* is exact finite-time passive stochastic LOCAL-PHASE comparison for a specific dephased two-path BMV geometry, and separate bounds for broader diagonal PPT active feedback class, with explicit operational witness/cost and noise-time optimization. Earlier Pedernales/Plenio 2021 arXiv:2111.04570 classical measurement feedback construction explicitly warns that interferometric revival alone does not universally refute classical mediation.
A complete unrestricted-LOCC physical conclusion is not obtained from their passive class and not obtained by XH.

## 1. Original physical model, not NASH physical assumptions

Original author Eq(1): two identical masses m, arm center separation L, branch separation d (L>d). Four distances R00=R11=L, R01=L+d, R10=L-d. After removing LOCAL and global phases, the inter-body conditional ZZ strength is:
 Gamma_g = (G*m^2/(4*hbar)) * [1/(L-d) + 1/(L+d) - 2/L] >0,
 U_Theta = exp(i*Theta*Z_A*Z_B), Theta=Gamma_g*tau.
Source notes this fixed geometry ignores actual trajectories during splitting/recombination; a realistic hold would require integrating phases over paths.

Author Eq(2): local environmental Markovian pure dephasing gamma sum_j (Z_j*rho*Z_j-rho). Each local coherence retains r=exp(-2gamma*tau). The environment dephasing r is assumed independently measured AND fixed identically in quantum target and candidate classic simulators, not a knob that a classic mediator is allowed to appropriate.

Target input |++>, resulting 4×4 complex density matrix sigma1 given explicitly as author Eq(3), verified by direct construction of U*rho0*U^dag and independent Hamming-distance phase-damping factor r per differing qubit.
Author Eqs(4)–(5): the POSSIBLY NEGATIVE partial-transpose eigenvalue is (1-r²-2r*abs(sin(2Theta)))/4; output separable iff 1-r²>=2r*abs(sin2Theta). Source correctly calls it the "potentially negative" eigenvalue, not necessarily the NUMERICALLY LOWEST eigenvalue when r<<1.

Author Theorem 1: passive local-phase family C_LP mixtures of LOCAL diagonal unitaries with shared randomness (but without active measurement conditional feedback or path transfer), fixed external D_r. Its EXACT minimum trace distance to quantum target on |++> is g_LP=r*abs(sin2Theta)/2. Optimal passive channel at selected t C_star=cos²Theta I + sin²Theta Ad_{Z_A Z_B}; source phase witness W_B=-Z_A Y_B, expectation target r sin2Theta and expectation every passive C_LP zero. Witness lower bound and constructed channel upper bound coincide. This model-specific EXACT characterization is authored by Feng/Vedral; XH independent check not original theorem firstness.

## 2. ACTUAL independent Python execution on primary physical parameters — matrices, spectra and trace norm

Original author low-visibility illustration Eq(23)/Fig2:
 m=1e-14 kg, L=40e-6 m, d=10e-6 m, tau=1 s, local r=0.1 (illustrative **NOT observed**).
G=6.67430e-11 SI, hbar=1.054571817e-34 SI.
Actual Python3 + NumPy code created and RUN locally (code and receipt SHA below), constructs full 4×4 Hermitian density matrices using Kronecker operators not just scalar substituting authored rate equation. Generates local completely-positive dephasing by r^HammingDistance across computational-path basis; calculates eigenvalues of the partial transpose and exact trace norm D(a,b)=||a-b||_1/2.

Executed:
Gamma_g=**0.052740994752628306 s^-1**, Theta=0.052740994752628306 rad; agrees author approximate 0.052741 rad.
Effective gamma from r=0.1,tau=1: **1.1512925464970227 s^-1**, gamma/Gamma_g≈21.829, deep strongly dephased.
rho_target eigs=**0.202500, 0.247500, 0.247500, 0.302500**.
rho_target^PT eigs=**0.20277790343611046, 0.2422356754192728, 0.2527643245807271, 0.30222209656388943**.
All ≥0 so two-qubit state SEPARABLE by Peres-Horodecki; the author Eq(4) branch equals **0.24223567541927282**, which is NOT the globally smallest PPT eigenvalue **0.2027779** at this r. No source author mistake; they say "potentially negative", correctly. Code checks membership in eigenspectrum rather than misasserting minimum.
Full sigma source Eq(3) matrix error <=1.4e-16, consistent with numerical precision.

Independently realize source claimed nearest passive C_star on original input and same dephasing:
D(quantum, passive_best)=**0.005264324580727185**;
predicted r/2 sin(2Theta)=**0.005264324580727186**;
witness expectation quantum W_B=**0.010528649161454367**;
passive_best W_B=0.
This is independent actual matrix computation and explicit saturation of passive class LP lower bound. The class-wide lower bound follows analytically from the witness being zero for EVERY passive local diagonal unitary product on |++> and convex shared random mixtures; source proof independently understood, but not a numerical exhaustive search over infinite models.

No microscopic gravitational sensor data or actual environmental visibilities measured. This is mathematical simulation based on authors' hypothetical experiment.

## 3. NEW independent explicit FALSIFIER NEGATIVE CONTROL: active classical LOCC can reproduce a single witness

Define allowed active protocol with local measurement and ONE classical bit:
(1) perform a projective Z_A path measurement with Kraus P0, P1 on Alice;
(2) send outcome i ∈{0,1} to Bob by classical communication;
(3) Bob applies U_i=exp(±iTheta Z_B) conditional on outcome i;
(4) retain unselected combined ensemble and apply SAME external D_r noise to both qubits as in the quantum target. The two full-system Kraus are M0=P0⊗U0 and M1=P1⊗U1. This is mathematically CPTP population-preserving active one-way LOCC. NOTE: its projective which-path measurement itself destroys Alice coherence, so NOT an LP random-phase channel.

XH EXPLICITLY CONSTRUCTED THESE KRAUS in Python and evaluated:
 W_B(target)=**+0.010528649161454367**;
 W_B(active one-way LOCC)=**+0.010528649161454367** exact to machine precision;
 W_B(best passive LP)=**0**.
BUT single-qubit coherence X_A:
 <X_A>_target=**0.09944419312777894**;
 <X_A>_active=**0**.
And full-state trace distance D(target, active) =**0.05**.

Thus a single nonzero W_B **by itself distinguishes the quantum target from passive LP** but DOES NOT exclude classical feedback / active LOCC in this simple demonstration. More multi-observable or full trace-distance channel discrimination is required; the paper explicitly states this in §VI around Eqs(23)–(24), so XH does NOT claim original refutation, new firstness or an uncovered author error. The concrete constructed LOCC is an operational negative control against a possible stronger misleading publicity claim.

Cannot infer that all active LOCC can reproduce the ENTIRE quantum model: our active example cannot, and we did NOT optimize over the paper's diagonal-PPT class or arbitrary feedback combs. Nor can we assert that the paper's passive LP exactly represents all admissible classical gravitational theories. In original authors' words their assumptions are source mechanisms and calibrations, not device independence.

## 4. Noise-time tradeoff and sample complexity, independently recomputed

In original source §§V–VI:
 g_LP(t)=(1/2)exp(-2gamma*t)*abs(sin(2Gamma_g*t)).
At original gamma=1.15129/s, independent exact scalar optimum:
 t_opt=atan(Gamma_g/gamma)/(2Gamma_g)=**0.4339910634862081 seconds**,
 r(t_opt)=**0.3681365487410755**,
 g_LP(t_opt)=**0.008423378997091297**,
 W_B(t_opt)=0.016846757994182594.
The optimized gap is about 1.60× the 1-second gap but depends on the SAME assumed environmental gamma calibration and feasibility of shorter interferometer hold.

At tau=1s, a ±1 observable W with mean S=0.010528649... has a formal iid detection threshold N>=25/S²=**225525.004510... independent recorded events** for nominal 5 sigma under authors' approximations; integer ceil **225526**. If using round human numbers ~226 thousand or 2.3e5, not 49 bit messages and not NASH simulation samples. This excludes detector losses, multiple testing, calibrated systematics, common drifts, apparatus noise and tests of active feedback models. At tau_opt, ideal threshold N>=**88087** (ceil of 88086.09) assuming same readout and time dependence.
This exposes a sharper practical limit: to claim passive LP exclusion on source author's exact trace-distance measure at 1 s, model mismatch / calibration additive error in trace distance must be **strictly less than 0.00526432**; the hypothetical inequalities are of form max(0,g_LP-epsilon_model) with independently justified per-class premise. This is NOT an experimental claim that r must have calibration absolute error <0.005264 and not a measurement uncertainty prescription without a sensor model.

### Additional executed scope
Original script evaluated 36 grid points gamma/Gamma_g in {0,0.1,0.5,1,2,5,10,20,40} and scaled hold Gamma_g*t in {0.2,1,3,10}; all cases gamma/Gamma_g>=1 had nonnegative partial transpose minimal eigenvalues. This is a bounded numerical spot check of the source inequality; analytic all-time proof remains the author's bound using arcsinh etc. No numerical experiment can prove PPT for continuum of all t.

## 5. Reproducibility and technical custody

ACTUAL Python code created and EXECUTED, output genuine container files:
- /mnt/data/xh_s7_rot020_locc_phase_test.py, **5,814 bytes**, SHA-256 **ce87413adfa8ad022880305ef7db422f7b0cb2732e2641332ad111e137c3df23**.
- /mnt/data/xh_s7_rot020_locc_phase_receipt.json, **8,599 bytes**, SHA-256 **7175b3b6aec914480d1749ecd39b9dd4f25d80d3fea83b5ddd377c3e3f90df64**.
Source imported NumPy and Python stdlib; no author code, no author data CSV or instrument data claimed. Independent author source Eq3 matrix, 4×4 Pauli, Kraus channels and randomized? NO random samples used (sweep deterministic). The script initially failed a too-strong local assertion that author Eq(4)'s potentially-negative eigenvalue was ALWAYS the smallest; this was CORRECTED after inspecting exact 4×4 PT spectrum, and passed. Important negative knowledge: "potentially negative" branch need not be minimum in all PPT regimes. The final source verified author Eq4 branch belongs to exact eigen-spectrum; no allegation of source error.

Arxiv original PDF textual content directly inspected, PDF screenshot requested but cache miss. Web sources do not establish independent peer-review journal publication of 2026 work. Firstness of LOCC non-entanglement test belongs at least to Lami et al 2023/2024, BMV test to 2017; only v2's particular passive LP exact gap + active diagonal PPT comparison is its new theoretical contribution.

## 6. Research outcome and implications for NASH

The most useful concrete source-native external science result is a **model hierarchy** with explicitly different prediction tests:
- Q: fixed noisy two-qubit quantum ZZ conditional-phase (author model);
- C1: passive classical path-local random phase, can share arbitrary random phases but no measurement of paths or active feedback; witness W=0 and full-state gap exactly positive;
- C2: active local measurement + classical communication + conditional phase, can match W alone but not full state in concrete example;
- C3: authors' broader population-preserving diagonal-PPT class with optimized discriminant, not independently solved by XH;
- C4: arbitrary classical gravity theories, non-diagonal LOCC or unrestricted experimental nuisances: NOT excluded by this single source theorem or XH computation.

No conclusion that a laboratory observation of W≠0 confirms gravity quantization without excluding other ZAZB interactions, adaptive feedback, non-gravitational couplings and calibration bias. The environmental dephasing must be independently characterized and same across hypothesis tests. This is compatible with author-source caution, not novel NASH physics.

NASH potential relevance is epistemic and conditional only: distinguish "same observable under different physical model classes" from "same complete quantum channel", and distinguish testable restriction on an adversarial classical model from a universal assertion. No direct bridge to NASH GMACH/J/K/DTC, no new NASH gravity model, no controlled B1 runs authorized, no automated canonical promotion, no external scientist contact. Github published report != BW receipt, independent mathematical referee or NASH theory acceptance.

ROT020 RESULT:
SOURCE_ARXIV_2611_12229_V2_TEXT_READ_PASS /
PPT_SEPARABLE_STATE_NUMERIC_PASS /
EXACT_CLOSEST_PASSIVE_LP_GAP_0P00526432_NUMERIC_PASS /
WITNESS_0P01052865_NUMERIC_PASS /
ACTIVE_LOCC_CONSTRUCTIVE_SINGLE_WITNESS_COUNTEREXAMPLE_PASS /
FULL_ACTIVE_VS_QUANTUM_STATE_DISTANCE_0P05 /
OPT_TAU_0P43399_AND_CALIBRATION_BOUND_CHECK /
EXPERIMENTAL_SOURCE_DATA_NONE /
NO_NASH_NOVELTY / NO_CANON / NO_EXEC_SIGN.
