---
artifact_id: IW_PRF12_R08_EXACT_ADAPTIVE_LOCC_WITNESS_AND_DELTA_UPPER_BRACKET_001_20261026
created_at: 2026-10-26
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
problem_id: PRF12_R07_UNKNOWN_NUMERICAL_LOCC_GAP
exposure: PUBLIC
canonical_body_path: research/prf12/2026-10-26/IW_PRF12_R08_EXACT_ADAPTIVE_LOCC_WITNESS_AND_DELTA_UPPER_BRACKET_001_20261026.md
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_SOURCE_TYPED_ANALYTIC_SEQUENTIAL_LOCC_WITNESS / INDEPENDENT_8X8_CHECK_PASS / REFEREE_PENDING
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_QUANTITATIVE_POSITIVE_LOWER_BOUND_ON_LOCC_GAP / NO_GLOBAL_LOCC_OPTIMUM / NO_FINITE_PULSE_CLAIM / NO_NOVELTY_CLAIM / NO_FULL_SUCCESSION_ZIP_READBACK
function: SCIENCE_FIRST / FOUNDATION_FIRST / TWO_SURFACE_PRIOR_ART / NEGATIVE_KNOWLEDGE / FALSIFIER_FIRST
---

# PRF12 R08 — Dokładny adaptacyjny trójstronny LOCC bez CNOT i ostrzejszy przedział nieznanej luki

**Właściciel:** PRF12. **Data:** 26.10.2026. **Główny wynik:** w n=3, idealne SWAP, równe ekspozycje i κ=0, prosty skończony trójstronny LOCC osiąga TV=0.198464903476238 przy q=1/3 BEZ żadnych bramek splątujących. Jest to dokładnie wynik wcześniej obserwowany w R05 dla świadectwa używającego jednego CNOT. Daje mocniejszy górny kres dodatniej luki LOCC z R07, ale nie jej dodatni dolny kres.

## 0. Source map, first owner, prior-art subtraction

- PRF11 R35 (oryginalny kontrakt static Cauchy vs independent Cauchy–Lévy i SWAP): https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R35_NONUNIFORM_SWAP_TIME_GRID_RECOVERS_IDEAL_MEMORY_WITH_CRITICAL_STORAGE_RATE_001_20261025.md .
- PRF12 R04 (dokładne n=3 stany, strata pełnego odczytu X): https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R04_THREE_PROBE_FINITE_SWAP_EXACT_X_READOUT_GAP_AND_SECTOR_DECOMPOSITION_001_20261026.md .
- PRF12 R05 (28-elementowy separowalny POVM, dokładny Helstrom; ponadto jeden CNOT i lokalny odczyt TV≈0.198464903476): https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R05_SEPARABLE_HELSTROM_POVM_PRODUCT_BASES_AND_ONE_CNOT_RESOURCE_AUDIT_001_20261026.md .
- PRF12 R06 (finite-round exact LOCC no-go): https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R06_EXACT_SEP_VS_LOCC_NO_GO_LOCAL_ORTHOGONALITY_RIGIDITY_001_20261026.md .
- PRF12 R07 (Cohen-theorem-dependent strictly positive gap for closure LOCC; number δ unknown): https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R07_POSITIVE_ASYMPTOTIC_LOCC_GAP_VIA_ZONOTOPE_PRODUCT_PATH_OBSTRUCTION_001_20261026.md .

**Dojrzałe zewnętrzne metody:** Helstrom (1976), Quantum Detection and Estimation Theory. Croke, Barnett, Weir, *Optimal sequential measurements for bipartite state discrimination*, PRA 95 052308 (2017), https://doi.org/10.1103/PhysRevA.95.052308 . Higgins et al., *Multiple-copy state discrimination: Thinking globally, acting locally*, PRA 83 052314 (2011), https://doi.org/10.1103/PhysRevA.83.052314 (inny model źródła). Cohen, *Local approximation of multipartite quantum measurements*, PRA 105 022207 (2022), https://doi.org/10.1103/PhysRevA.105.022207 , Theorem 1: własność closure LOCC wykorzystana przez R07. *Structure of quantum measurements implementable with one round of classical communication* (2026), https://pubmed.ncbi.nlm.nih.gov/41806397/ (adaptacja i kierunek wiadomości, odmienny eksperyment). Nie rościmy ogólnej nowości lub publikacyjnego pierwszeństwa dla adaptacyjnych lokalnych testów.

## 1. Source-typed, unchanged n=3 ideal endpoint pair

Trzy świeże kubity |+> i idealne chwilowe SWAP między trzema równymi ekspozycjami T/3, bez starzenia pamięci (κ=0). Hipoteza A: **jedno wspólne** ukryte ξ~Cauchy(0,γ) przez cały eksperyment. Hipoteza B: **niezależne** przyrosty Cauchy–Lévy. Po zakończeniu trzy kubity są w trzech fizycznie odseparowanych laboratoriach A/B/C. Dla q=γT/3>0, x=e^(−q), b=1−x², a=xb, różnica końcowych stanów ma formę

 D(s,t)=1/8[exp(−q|Σ_j(s_j−t_j)|)−exp(−q Σ_j|s_j−t_j|)], s,t∈{0,1}³.

Unrestricted endpoint Helstrom: V_H=b/2. Full fixed X on all qubits (R04) yields V_X=b(6+9x)/32 for x≥2/3 and 3b/8 for x≤2/3.

Z R07: δ(q)=V_H−sup_LOCC V_LOCC >0 przy q>0, w wąskim modelu trzech odseparowanych laboratoriów. R08 NIE udowadnia ponownie koniecznego twierdzenia Cohena ani nie liczy tego supremum.

## 2. Constructive theorem R08.1: finite-round, THREE-PARTY LOCC

1. Alice measures X on qubit 1 and broadcasts s=±1 to Bob.
2. If s=+, Bob measures X on qubit 2; if s=−, Bob measures Y on qubit 2. He broadcasts t=±1 to Charlie.
3. Charlie uses only qubit 3 and performs the **one-qubit conditional Helstrom decision** for the pair of unnormalized conditional states given (s,t). No BC joint measurement or CNOT occurs.

This is a valid protocol with only **two classical feed-forward messages** and local qubit observables. Charlie’s final eigenbasis is explicitly recoverable from the 2×2 matrices below.

### Exact Pauli decomposition

Writing X_i, Y_i for tensor factors and omitting identities on unused factors:

 D=(b/16) Σ_{i<j}(X_i X_j+Y_i Y_j)
   +(a/32)(3 X_1 X_2 X_3 +X_1Y_2Y_3+Y_1X_2Y_3+Y_1Y_2X_3).     (R08.1)

All matrix entries checked against the original R04 Cauchy characteristic-function definition. Project Alice and Bob as in this protocol. The four **unnormalized signed 2×2 differences on Charlie** are

 D_C^{++}=(b/16) I +(b/8+3a/32) X,                            (R08.2)
 D_C^{+-}=−(b/16) I−(3a/32) X,                              (R08.3)
 D_C^{−t}=−(b/16) X+t(b/16−a/32) Y, t=±1.                  (R08.4)

Charlie measures along their Bloch vectors and assigns decisions by the signs of the resulting eigenvalues. In particular, when D_C^{+-} has both eigenvalues negative (x≤2/3), Charlie can simply guess B on that branch.

Because the norm of a 2×2 Hermitian uI+v·σ equals 2 max(|u|,||v||), a strict closed formula follows:

 V_adapt(q) = 1/2 Σ_{s,t}||D_C^{s,t}||_1
 = **(b/32)[4+3x+max(2,3x)+2 sqrt(4+(2−x)²)]**.             (R08.5)

For x≥2/3 it simplifies to b[4+6x+2sqrt(4+(2−x)²)]/32;
for x≤2/3 to b[6+3x+2sqrt(4+(2−x)²)]/32.

This is an exact **LOCC-achievable witness**, not an optimum over all LOCC. No random Cauchy sampling, numerical tail truncation, infinite time or finite-gate extrapolation are required to prove it.

## 3. Main numerical resource correction at q=1/3

At q=1/3, x≈0.71653131057:

| End readout | Exact TV |
|---|---:|
| Full global Helstrom | 0.243291440483704 |
| Fixed full local X, R04 | 0.189292628450799 |
| Finite-round adaptive X→(X/Y)→local Helstrom, R08 | **0.198464903476238** |
| R05 one-CNOT + tuned local readout witness | ≈0.198464903476 |
| R05 abstract 28-effect SEP POVM | 0.243291440483704 |

The TWO protocols with identical TV need not implement the same POVM or be equivalent under a local circuit. But the equality **falsifies any claim that a CNOT is necessary for the performance gain of that selected R05 witness**. It does NOT falsify R07 no-go for exactly attaining 0.243291... under all separated-party LOCC.

Adaptive gain over full fixed X:
 ΔV=0.009172275025439. Fraction of the original Helstrom-vs-X gap recovered: 0.169860681747 or ≈17%.

**Quantitative gap bracket:** since this LOCC witness is achievable and R07 yields strict positivity,

 0 < δ(1/3) ≤ 0.243291440483704−0.198464903476238
             = **0.044826537007466**.                              (R08.6)

Previous valid R07 upper bound using X only was δ≤0.053998812032905. Our result improves this **UPPER** bound. We have NOT produced a numerical strictly POSITIVE **LOWER** bound on δ. Treating 0.0448265 as such would be a severe reversal of quantifiers.

## 4. For which q does THIS adaptive protocol beat full X?

Compare the two exact expressions. For x≥2/3, adaptive−X has sign equal to
 2 sqrt(4+(2−x)²)−(2+3x),
whose nonnegative-side square reduces to 5x²+28x−28<0.
For x≤2/3, sign equals
 2 sqrt(4+(2−x)²)+3x−6,
reducing to 5x²−20x+4<0.

Combining admissible roots gives exactly

 V_adapt(q)>V_X(q)
 iff **2−4sqrt(5)/5 < e^(−q) < (−14+4sqrt(21))/5**,
 equivalently **0.143800446808 < q < 1.555207250836**.        (R08.7)

Else the adaptive test may be strictly worse, so the participant can always choose whichever of the two is better, giving a globally valid witness

 V_LOCC(q)≥max{V_X(q),V_adapt(q)},                              (R08.8)
 0<δ(q)≤(1−e^(−2q))/2−max{V_X(q),V_adapt(q)}.                 (R08.9)

The lower strict inequality is contingent on review of R07 and Cohen's 2022 theorem. The explicit right bound is standalone from the finite LOCC construction.

Selected independent direct matrix calculation:

| q | V_H | V_X | V_adapt |
|---:|---:|---:|---:|
| 0.10 | 0.090634623461 | 0.080118383054 | 0.079245560438 |
| 1/3 | 0.243291440484 | 0.189292628451 | 0.198464903476 |
| 0.80 | 0.399051741003 | 0.299288805752 | 0.309500576971 |
| 1.00 | 0.432332358382 | 0.324249268786 | 0.331450643207 |
| 1.50 | 0.475106465816 | 0.356329849362 | 0.356923853095 |
| 2.00 | 0.490842180556 | 0.368131635417 | 0.364291324240 |

The advantage of this particular feed-forward protocol is NOT universal, and q→0 makes all distinguishability vanish.

## 5. Independent reproducibility

Standalone artifact:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R08_ADAPTIVE_THREE_PARTY_LOCC_EXACT_REPRO_001_20261026.py .

Python 3 + NumPy only. Rebuilds D(q) directly, projects first two qubits under X→conditional X/Y, diagonalizes four Charlie-only 2×2 matrices, and checks equality with all analytic expressions above and global Helstrom plus full X. Tested at q=.01,.05,.1,1/3,.8,1,1.5,2,5; maximum observed discrepancy ≲2.3×10^−16. No fitting, no random seed, no Cauchy tail integration, no previous-R04 code dependency.

## 6. Negative knowledge, review gate, and cross-cell correction

- **The central R07 request remains UNRESOLVED:** produce explicit positive numerical lower δ(q)>c>0. R08 improves only its upper bound by exhibiting a better LOCC algorithm. This is valuable positive engineering and a falsifier of R05 hardware necessity rhetoric, but not a solution to quantitative LOCC impossibility.
- R05's **one-CNOT witness** remains a valid numerical strategy; however its score is reached with ZERO entangling gates. Avoid representing its reported improvement as evidence that an entangling gate is necessary.
- This measurement is three-party LOCC with two classical messages. Contrast with R06's A:X then **joint BC** readout at TV 0.220014079553 — that result IS NOT a three-separated-lab LOCC witness.
- No claim that R08 is optimal among local projective adaptive strategies, unsharp POVMs, arbitrary finite rounds or closure LOCC. Exploratory six-angle optimization for first A and conditional B returned the same peak around q=1/3, but that is not an optimization certificate.
- κ=0, instantaneous SWAPs, equal times only. R04/R05 finite-duration source-active pulse experiments with nonzero κ are **not** covered. No physical implementation or empirical device claim.
- Source typing, no fixed κ asymptotic recovery, no NCDG K/J3 interpretation, no novelty, no BW-sync claim, no canon and no EXEC_SIGN.
- Referee: rederive Pauli expansion R08.1; check all four Charlie matrices and TV normalization; check comparison interval roots; assess whether Charlie's conditional choices are implementable by X/Y plane one-qubit observables or constant guessing; verify that R05 equality refers to scores, not identical POVMs.
- Best next work R09: rigorous **positive numerical lower δ** using quantitative restrictions stronger than SEP/PPT (which attain Helstrom via R05), e.g., finite precision product-path stability with a certified inequality, or a direct general LOCC relaxation. A bound for only fixed local bases or a fixed number of rounds is not enough.

**Ready to transmit internally (scientific correction):** PRF12_R08 proves an exact fully local, two-message adaptive protocol X→(X/Y)→single-qubit Helstrom with TV=0.198464903476 at q=1/3, identical in score to R05's CNOT witness. The CNOT is unnecessary for THAT witness advantage. R07's unknown asymptotic LOCC gap δ stays >0 under its conditions, while its numeric UPPER bound tightens to 0.044826537007466; no positive numeric lower δ was found. Independent referee still pending.

## 7. RETURN

PRF12_R08 / EXACT_ADAPTIVE_THREE_PARTY_LOCC_WITNESS / CLOSED_FORM_ALL_Q / EXACT_FEED_FORWARD_WIN_WINDOW / R05_CNOT_RESOURCE_NECESSITY_FALSIFIED_AT_WITNESS_SCORE / R07_GAP_UPPER_BOUND_TIGHTENED / NO_NUMERIC_POSITIVE_LOCC_GAP_LOWER_BOUND / INDEPENDENT_8X8_REPRODUCTION_PASS / REVIEW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC / GITHUB_PENDING_BW_INGEST / PRF12_SUCCESSION_ZIP_UNREAD.
