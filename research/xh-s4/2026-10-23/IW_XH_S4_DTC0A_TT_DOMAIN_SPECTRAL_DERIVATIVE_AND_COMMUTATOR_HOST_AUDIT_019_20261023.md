# XH-S4 / obrót 019 — kontrakt domeny TT i rozdzielenie błędów dyskretyzacji od projekcji

RETURN_ID: XH-S4-DTC0A-TT-DOMAIN-SPECTRAL-LEIBNIZ-COMMUTATOR-Q36-Q40-019_20261023
DATE: 2026-10-23
CELL: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03 / XH-S4
CLASS: EXACT_FINITE_ALGEBRA + INDEPENDENT_NUMPY_DIAGNOSTICS + MAY_OCT_2026_PRIOR_ART + RESEARCH_QUESTIONS
CLAIM_CEILING: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_KJ3 / NO_DTC_CONTINUUM / BW_NOT_ASSUMED / NO_NEW_TASKS

## Grounded user source + replication
Original user DTC verification source `deepseek_python_20260627_a87249.py` SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801` and independently reconstructed XH018 `xh_s4_dtc0a_projection_leakage_018_selfcontained.py` SHA256 `534c1e548b4175de4b3929a8a8b82ce85098afa4cc39be36f4c3ffe26251826f`. Run N17/31 odd periodic 3D, centered vs FFT spectral derivatives, E_lin=I+alpha dx² Delta_h, Fourier P_TT at nonzero k (zero k tracefree), same frozen source smooth C1,C2. Standard h=.1 sin x cos y * I, alternate h_TT=P H normalized to exactly same global RMS; interior mask slice(3,N-3), Frobenius/6 RMS. No NASH production physics claim.

Full local report byte hash verified; source local `IW_XH_S4_DTC0A_DOMAIN_CONTRACT_SPECTRAL_DERIVATIVE_AND_COMMUTATOR_PRIORART_019_20261023.md` with full exact proof, data, and links. Independent TWO NumPy scripts and JSON arrays, local SHA256:
- `xh_s4_dtc0a_trace_sector_and_spectral_control_019.py`: 7c2f9d4a66648c3ee514695b44428de6ac0b82072ef2ee56c4bf2add713e15aa
- `xh_s4_dtc0a_trace_sector_and_spectral_control_019_results.json`: fe027a82b032551195a94a4e80e0c3b3826c17df925aa6982a6b47f1075b1745
- `xh_s4_dtc0a_derivative_crosscheck_019.py`: ccd0ee930daca5200e8bbb8babac13527dfc7a13dc15f6466839d63f4392529f
- `xh_s4_dtc0a_derivative_crosscheck_019_results.json`: a9060a4604d563f3a957c18821af4b08f621470bad1534861c7455d159f5a1cf
The scripts import the PREVIOUS frozen XH018 NumPy definitions and are not physically independent from the shared source formula; they DO independently compute current metrics and FFT derivatives. No independent theorem proof from literature or continuum bound.

## A. Exact input-domain distinction, NOT a new physical invariant
Let P=P_TT, Q=I-P, L_i=Lie_{C_i}∘E, b=[C1,C2].
Source ambient diagnostic:
  K_A(h)=P L_1 P L_2 h - P L_2 P L_1 h - P L_b h.
Genuinely TT-restricted expression:
  R_TT(h)=P L_1 P L_2 P h - P L_2 P L_1 P h - P L_b P h = K_A(P h).
Therefore K_A(h)=R_TT(h)+K_A(Q h) for EVERY h. Original h=f I is PURE TRACE: P h=0 EXACTLY. Original raw trace K_A cannot be read as evaluation of TT-restricted representation; R_TT(h)=0 identically, raw K_A(h) can be nonzero, and in this case is.
At N31 alpha .05:
 ||h||global RMS=.0353553390593, ||P h||≈7.77e-34,
 ||K_A(h)||masked=3.76475685320836e-5,
 ||R_TT(h)||masked≈1.97e-36.
Independent nonzero TT input, same global RMS: ||K_A(h_TT)||=3.22347203162382e-5; ||R_TT(h_TT)-K_A(h_TT)||≈1.18e-19. Thus REAL nonzero residual also exists on one proper TT input, but that finding is SEPARATE evidence.

## B. Which Lie term creates the TT component from original fI?
For componentwise scalar E and g=E f,
  Lie_C (g I) = (C·D g) I + g (D_i C_j + D_j C_i).
Since P(phi I)=0 on each lattice Fourier mode, algebraically
  P Lie_C E(f I) = P[g (D_i C_j+D_j C_i)].
Thus projected ADVECTION contribution is EXACT ZERO on trace input: this first-stage TT is wholly produced by multiplied tensor STRAIN. At N31 alpha .05:
 ||P L_C1 h||glob=2.01899447455e-4 and ||P L_C2 h||glob=5.95897971469e-4;
 ||P advection_C1||glob=6.21e-20, ||P advection_C2||glob=1.19e-19;
 ||P strain_C1||glob=2.01899447455e-4, C2=5.95897971469e-4.
At constant h=.1I, frozen axis-aligned single-mode C and k-based P kill also the pure strain output, so K_A≈2.30e-20 while K_C≈1.45e-6 on N31 alpha .05. This special cancellation need not hold for arbitrary vector fields, non-axis-aligned discrete q vectors or boundary conditions. For TT-initial input advection and strain BOTH contribute (no identical mechanism).

## C. Spectral derivative discrimination of discretization error
Alpha0 implies E=Identity. For smooth low-band fields and FFT differentiation (no aliasing in tested harmonics), [Lie_C1,Lie_C2]h−Lie_[C1,C2]h and thus K_C approximately vanish to machine precision, but K_A DOES NOT. Full independently computed table:

| N | α | D | KC(mask) puretrace | KB(mask) puretrace | KA(mask) puretrace | KC(mask) nonzero TT | KA(mask) nonzero TT |
|--:|--:|:--|--:|--:|--:|--:|--:|
| 17 | 0 | central | 5.25484e-6 | 1.01123e-6 | 3.77585e-5 | 1.10731e-5 | 3.21685e-5 |
| 17 | 0 | spectral | 5.03314e-19 | 6.99025e-20 | 3.95834e-5 | 8.18657e-19 | 3.27572e-5 |
| 31 | 0 | central | 1.53159e-6 | 3.00026e-7 | 3.78853e-5 | 3.59789e-6 | 3.28334e-5 |
| 31 | 0 | spectral | 1.62390e-18 | 1.79494e-19 | 3.84158e-5 | 2.05642e-18 | 3.32154e-5 |
| 31 | .05 | central | 2.13372e-6 | 4.43620e-7 | 3.76476e-5 | 4.66890e-6 | 3.22347e-5 |
| 31 | .05 | spectral | 8.19927e-7 | 3.38265e-7 | 3.81759e-5 | 1.85154e-6 | 3.25412e-5 |
| 31 | .20 | spectral | 3.23926e-6 | 1.33637e-6 | 3.74692e-5 | 7.18774e-6 | 3.08290e-5 |

At alpha0 spectral, independent two input classes show K_C≈0 BUT K_A≈3–4e-5. Therefore failure of central Leibniz is not dominant cause of large K_A in this frozen source setup. At nonzero alpha, E(k) varies by k and does NOT commute with variable Lie_C, even though P and E commute exactly, so K_C can remain nonzero even with spectral derivative. For an arbitrary high-band h, the current no-dealias FFT derivative need not reproduce exact Leibniz; do not overgeneralize to all N/fields.

## D. Retained 018 insertion identity and operator bound
For ANY h:
  K_A-K_B = P L_2 Q L_1 h - P L_1 Q L_2 h.
For h=Ph:
  ||K_A-K_B|| ≤ (||P L_2 Q|| ||Q L_1 P|| + ||P L_1 Q|| ||Q L_2 P||) ||h||.
No admissible continuum/finite-N-uniform UPPER control of these four blocks yet established. Observed RMS on one input is not an operator norm proof. This is exact operator bookkeeping, not a new theorem or invariant.

## E. External May–October literature, typed relation and nonmaps
1. Qianyuan Zhang and Kai Yan, arXiv 2605.05654v1 MAY7, original https://arxiv.org/html/2605.05654. Theorem 1.1 gives paraproduct and dyadic [v,Delta_j]·∇f estimates in Besov and Triebel-Lizorkin classes, with p,q,s, regularity and divergence conditions. SAME BROAD COMMUTATOR QUESTION, DIFFERENT scalar dyadic operator; not a tensor P_TT Lie theorem. Regularity/commutator technical prior-art donor for Q39.
2. Tuomas Hytönen, arXiv 2609.30961v1 SEP25, original https://arxiv.org/html/2609.30961. Commutator [T,b] of singular integral and multiplication, weak Schatten/singular-value asymptotics; Connes quantized calculus, critical norm bounds. Source has matrix-symbol/nonlocal multiplier analogies but full first-order Lie + tensor stretching and k=0 must be separately derived. NO claim this directly bounds K_A or TT commutator.
3. Radhakrishnan et al., EPJC 86 1183 published OCT19 2026, DOI https://doi.org/10.1140/epjc/s10052-026-16355-y. Bardeen/NP/Cartan-Karlhede gauge-invariant plane-wave analysis under specified linearized GR host; does NOT promote our finite projected trace input to gauge-invariant gravitational-wave observable. Type label PHYSICAL_NONMAP.
Background crosslinks: Wittig Aug finite-range cert needs finite host and TT tails obstruct naive host; Boffi et al FEEC Oct pseudospectra needs same norm host; Brué et al July scalar transport estimates remain distinct mathematical object.

## F. New questions and discriminators
Q36 / P0: WHICH target is intended—ambient full Sym² K_A(h), or TT-restricted R_TT(h)? Input target type decides interpretation. Current pure-trace dataset cannot alone establish nonzero TT-sector defect. Separate TT test shows it exists for one smooth h_TT.
Q37 / P0: If P_TT is defined relative to FIXED background Euclidean metric, what changes if one transports metric/projector covariantly with a non-isometric C? Competing H_fixedProjection vs H_covariantlyMovingReference; first declare background and consistent gauge, calculate transformed TT decomposition; no presumed physical solution.
Q38 / P0: Which part of K_C comes from discrete Leibniz error vs E_lin nonidentity? Controlled alpha0 spectral eliminates K_C but not K_A; alpha .05 spectral KC survives. Extend alpha and Fourier band while preserving de-aliasing.
Q39 / P1: Can source-native Sobolev/Littlewood-Paley commutator estimates bound P L_C Q and Q L_C P under declared tensor geometry, field regularity, zero mode and frequency support? Test Fourier kernel P(k)-P(l) on paired modes with explicit lower-frequency cutoff; no automatic full-theorem transfer.
Q40 / P1: When is nonzero fixed P_TT projection a physically gauge-invariant radiative observable? Needs a declared perturbative gravity/gauge/measurement host and independent source calibration; current DTC data lack one.

## Outcome and limitations
Source equations and compact projection proof EXACT on finite host, 7 derivative-crosscheck combinations and 2 domain-contract controls independently reproduced against source definitions and earlier 018. DTC production, full source theorem from literature, continuum, experimental physics, and physical K/J3 NOT adjudicated. Scientific priority Q36/Q38 (domain contract and discretization separation), then Q39 mathematical upper estimates, Q37/Q40 theoretical/physical host specification.
NO_CANON / NO_EXEC_SIGN / NO_NEW_OWNER_TASK / BW_NOT_ASSUMED.
