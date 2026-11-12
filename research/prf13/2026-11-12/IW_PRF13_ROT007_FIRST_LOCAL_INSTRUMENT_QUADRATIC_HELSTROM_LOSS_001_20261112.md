---
artifact_id: IW_PRF13_ROT007_FIRST_LOCAL_INSTRUMENT_QUADRATIC_HELSTROM_LOSS_001_20261112
created_at: 2026-11-12
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_12 / PRF13
source_type: SOURCE_NATIVE_EXACT_THREE_QUBIT_SPECTRAL_COUPLING_AND_GENERALIZED_FIDELITY_THEOREM
exposure: PUBLIC
sync_state: GITHUB_BODY_BLOB_READBACK_PASS_BW_INGEST_PENDING
status: EXACT_SOURCE_TYPED_FIRST_LOCAL_MEASUREMENT_LOSS / CONDITIONAL_REENTRY_INCLUDED / AUTHOR_REPRODUCED / EXTERNAL_REFEREE_PENDING
claim_ceiling: NO_FULL_LOCC_POSITIVE_UNIFORM_GAP / NO_ASYMPTOTIC_LOCC_CLOSURE / NO_FINITE_PULSE_OR_HARDWARE / NO_NOVELTY_OR_PRIORITY / NO_CANON / NO_EXEC_SIGN
---

# PRF13 ROT007 — Quadratic unavoidable loss in first local measurement, even if the first party re-enters and ALL three qubits are subsequently reunited

**12 November 2026 / PRF13**. This rotation attacks the precise *re-entry* obstruction remaining after PRF13 ROT006. It provides a **quantitative, source-specific first-informative-measurement theorem**. Its bound survives arbitrary later quantum operations, including an artificially strengthened continuation in which all three qubits may be globally measured after the first local instrument. It therefore applies, in particular, to arbitrary subsequent LOCC with the first party revisiting the protocol. **It does NOT give a positive gap uniform over all full LOCC protocols or their closure**, because the first measurement can have arbitrarily small strength. This ceiling is a theorem necessity, not a procedural disclaimer.

## 0. Provenance, literature and R09 negative-knowledge guard

Frozen original source: PRF12 R04, exact three-qubit endpoint matrix, `research/prf12/2026-10-26/IW_PRF12_R04_THREE_PROBE_FINITE_SWAP_EXACT_X_READOUT_GAP_AND_SECTOR_DECOMPOSITION_001_20261026.md`, public https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R04_THREE_PROBE_FINITE_SWAP_EXACT_X_READOUT_GAP_AND_SECTOR_DECOMPOSITION_001_20261026.md. Original model from PRF11 R35: one static hidden Cauchy frequency versus independent symmetric Cauchy-Lévy increments. Source qubits are in three separated laboratories after equal ideal exposures with instantaneous SWAP and storage kappa=0.

R06 finite-round exact LOCC obstruction: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R06_EXACT_SEP_VS_LOCC_NO_GO_LOCAL_ORTHOGONALITY_RIGIDITY_001_20261026.md. **R09 critical owner correction**: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R09_COARSE_GRAINING_COHEN_THEOREM_AUDIT_AND_CORRECTED_CLAIM_CEILING_001_20261026.md: R07's positive closure(LOCC) gap was WITHDRAWN due to mistaken application of Cohen's POVM path theorem after coarse-graining. R12 explicit 9-product-effect Helstrom-achieving SEP measurement is source-native and does not imply LOCC: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-27/IW_PRF12_R12_RANKONE_RIGIDITY_PRODUCT_EFFECT_MINIMALITY_AND_EQUATORIAL_LOCC_001_20261027.md. PRF13 ROT006 exact one-way first-party-measurement quantitative gap: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf13/2026-11-11/IW_PRF13_ROT006_ONE_SHOT_A_TO_BC_QUANTITATIVE_LOCC_RESTRICTION_001_20261111.md.

Mature **external** hosts: Fuchs-van de Graaf fidelity versus trace norm for normalized states and its direct unequal-trace purification variant; e.g. https://learning.quantum.ibm.com/course/general-formulation-of-quantum-information/purifications-and-fidelity . Instrument polar decomposition and trace-norm data processing are textbook quantum information. Relevant recovery/equality characterizations: Jenčová, *Recoverability of quantum channels via hypothesis testing*, 2024, https://doi.org/10.1007/s11005-024-01775-2 . Cohen, *Local approximation of multipartite quantum measurements*, PRA 105 (2022), https://doi.org/10.1103/PhysRevA.105.022207; Cohen's later instrument extension, arXiv:2310.05362, https://arxiv.org/abs/2310.05362 . No priority search supports novelty/firstness. The present contribution is an explicit algebraic bound for this fixed PRF12 source pair.

## 1. Frozen endpoint and first-instrument contract

Let `q=gamma*T/3>0`, `x=exp(-q)` in `(0,1)` and `b=1-x^2`. Put `D=rho_A-rho_B`. For computational strings `u,v` in `{0,1}^3`,

`D[u,v]=(x^{|sum_k(u_k-v_k)|}-x^{sum_k|u_k-v_k|})/8`.

Define normalized `W=(001+010+100)/sqrt(3)` and `Wbar=(110+101+011)/sqrt(3)`. Let `P=|W><W|+|Wbar><Wbar|`, `K=|000><000|+|111><111|` and `Q=I-P-K`. The spectral positive/negative parts of `D` are `D_+=PDP>=0`, `D_-=-QDQ>=0`, with `D=D_+-D_-` and `Tr(D_++D_-)=b`. There are two strictly positive and four strictly negative nonzero eigenvalues for each `q>0`; the minimum nonzero absolute eigenvalue is `mu=b(1-x)/8`. Therefore

`TV_Hel=(1/2)||D||_1=b/2`.

Alice (or, by exact party permutation symmetry, any first laboratory) performs **an arbitrary local quantum instrument** with publicly available classical outcomes `i` and associated qubit POVM effects `E_i`. Local ancillas and outcome-dependent local postmeasurement operations are allowed; no pre-shared entanglement or prior quantum transfer. After this first instrument, we allow the most generous continuation: the entire post-instrument state of all three labs (including Alice's retained output/ancilla) is brought together for **one global optimum test**, conditional on `i`. This is strictly at least as powerful as an actual later LOCC where Alice can return. The theorem holds for every finite or measurable-outcome POVM with the indicated second moment; infinite sums interpreted as integrals.

Write each effect in Bloch form `E_i=alpha_i(I+r_i · sigma)` with `alpha_i>=0`, `||r_i||<=1`; completeness implies `sum_i alpha_i=1` and `sum_i alpha_i r_i=0`. Define `S2=sum_i alpha_i||r_i||^2` in `[0,1]`, the squared mean informative strength of the classical first measurement. `S2=0` iff every nonzero effect is proportional to the identity (classical outcome independent of the Alice input).

## 2. Theorem ROT007.1 — effect-aware first-step information-loss certificate

Define the actual achievable TV after the announced first instrument and any global continuation as `TV_after`. For `a_i=Tr[(D_++D_-) E_i]`, `z_i=Tr[D_+ (E_i tensor I_BC) D_- (E_i tensor I_BC)]`, with tensor products implicit, one has

`TV_Hel-TV_after >= (1/2) sum_i (a_i - sqrt(a_i^2-4*z_i)) >= sum_i (z_i/a_i)`;

for `a_i=0`, the corresponding summand is zero, and all radicands are nonnegative.

More explicitly, in this R04 source pair and for `E_i=alpha_i(I+r_i·sigma)`:

`a_i = b*alpha_i*(1+(x/3)*r_ix)`,  (7.1)

`z_i = (b^2*alpha_i^2/144)*[(2-x^2)*r_ix^2 +(2+x^2)*r_iy^2 +4*(2+x^2)*r_iz^2]`.  (7.2)

Thus the **effect-aware lower bound** is

`TV_Hel-TV_after >= (b/144) * sum_i alpha_i * [ (2-x^2)*r_ix^2+(2+x^2)*r_iy^2+4*(2+x^2)*r_iz^2 ] / [1+(x/3)*r_ix]`.  (7.3)

In particular, since `0<x<1`, `2-x^2>0`, and `1+(x/3)*r_ix <=1+x/3`, the following is valid without any restriction `x in [0.7,0.75]`:

`TV_Hel-TV_after >= C(x)*S2`,

`C(x)=(1-x^2)*(2-x^2)/(144*(1+x/3)) >0`.  (7.4)

**Interpretation.** Every first POVM with nontrivial locally informative effects (`S2>0`) creates a positive, quantitatively controlled loss that no later joint quantum measurement can reverse. The inequality is about the **first instrument on the original source triple**, or the equivalent first informative instrument preceded only by distinguishability-preserving local isometries; it is not a uniform gap for arbitrary fully adaptive LOCC sequences with first-effect strengths tending to zero.

### Proof, Part A: general instrument to Lüders upper envelope

For each classical outcome `i`, the completely positive trace-decreasing Alice operation has effect `E_i`. Its Stinespring operator `V_i` satisfies `V_i† V_i=E_i`; polar decomposition gives `V_i=U_i sqrt(E_i)` for a partial isometry `U_i`, with the environment and any discarded degrees of freedom handled by a subsequent channel. Consequently, for **either** hypothesis and for their signed difference D, data processing gives

`||instrument_i(D)||_1 <= ||(sqrt(E_i) tensor I_BC) D (sqrt(E_i) tensor I_BC)||_1`.

Hence `TV_after <=(1/2) sum_i||A_i-B_i||_1`, with `A_i=sqrt(E_i) D_+ sqrt(E_i)`, `B_i=sqrt(E_i)D_-sqrt(E_i)` (tensor identities implicit). They are PSD. Set `a_i=Tr(A_i+B_i)` and `z_i=Tr(A_i B_i)=Tr[D_+ E_i D_- E_i]>=0`.

### Proof, Part B: source-independent overlap loss

For arbitrary unnormalized PSD A,B with `T=Tr A+Tr B`, choose optimal Uhlmann purifications with inner product `F=||sqrt A sqrt B||_1`. Trace-norm contractivity under partial trace and the exact trace norm of two rank-one pure operators yield

`||A-B||_1 <=sqrt(T^2-4F^2) <=sqrt(T^2-4Tr(AB))`.

Here `F^2>=||sqrt A sqrt B||_2^2=Tr(AB)`. Since `0<=4Tr(AB)<=T^2`, scalar concavity of the square root gives `(T-sqrt(T^2-4TrAB))/2 >=TrAB/T`. Applied to each outcome, this proves both inequalities in the theorem. This argument depends on the **fine-grained announced instrument outcomes**, not the two final A/B guesses, so the R09 coarse-graining mistake is absent.

### Proof, Part C: exact source-specialized 3Q algebra

Let `sigma_{k,A}=sigma_k tensor I_4`. Direct exact multiplication of the source matrix and its positive and negative spectral projectors yields

`Tr[(D_++D_-) sigma_{X,A}]=b*x/3`,
`Tr[(D_++D_-) sigma_{Y,A}]=Tr[(D_++D_-) sigma_{Z,A}]=0`,

and real quadratic cross-coefficients vanish in the Hermitian 3x3 matrix `H_{jk}=Tr[D_+ sigma_{j,A} D_- sigma_{k,A}]`:

`H_xx=b^2*(2-x^2)/144`,
`H_yy=b^2*(2+x^2)/144`,
`H_zz=b^2*(2+x^2)/36`,
`Re(H_jk)=0` for `j!=k`.

In fact `H_yz=-H_zy` is purely imaginary, as checked symbolically and listed in the reproduced stdout. Since `P D_- =0`, scalar terms and scalar-vector terms cancel in `Tr(D_+ E_i D_- E_i)`. The formulas (7.1)–(7.2) follow. Substituting them into `sum z_i/a_i` proves (7.3)–(7.4). QED.

## 3. ROT007.2 — binary unsharp measurement and the asymptotic obstruction

For the first two-outcome qubit POVM `E_±=(I±eta n·sigma)/2` with `eta in (0,1]`, `||n||=1`, the effective informative strength is `S2=eta^2`. Formula (7.3) specializes to the **stronger direction-sensitive bound**

`loss >= [b*eta^2/(144)]*[(2-x^2)*n_x^2+(2+x^2)*n_y^2+4*(2+x^2)*n_z^2] / [1-(x*eta*n_x/3)^2]`.

For the particular q=1/3, `x=exp(-1/3)=0.716531310573789...`, `TV_Hel=0.243291440483704...`, and the universal constant

`C=0.00405477648697132...`.

As `eta -> 0`, `sqrt(E_±) -> I/sqrt(2)`; the flagged Lüders instrument converges to the undisturbed input with an irrelevant fair coin, hence the true globally optimal distinguishability AFTER this first instrument tends to `TV_Hel`. This is an explicit **falsifier of any attempted fixed uniform gap based only on the existence of a nonzero first informative local step**. Any asymptotically optimal sequence of protocols that starts with an informative POVM acting on the source triple must have first-step strengths `S2 -> 0` (since `S2 <= total_error/C`). The existence/nonexistence of such an asymptotically LOCC-Helstrom sequence is still OPEN.

**Diagnostic values for n=(1,0,0) with the specified Lüders instrument at q=1/3**, recomputed by direct 8x8 matrix square roots and trace norms:

| eta | actual global loss after first instrument | theorem guaranteed loss (weaker universal) |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0.001 | 0.00000001339529665 | 0.00000000405477649 |
| 0.01 | 0.00000133957176635 | 0.00000040547764870 |
| 0.1 | 0.00013438036484120 | 0.00004054776486971 |
| 0.5 | 0.00365169198252316 | 0.00101369412174283 |
| 1 | 0.02327736093101118 | 0.00405477648697132 |

These are calculations for **actual global continuation**, not LOCC optimum. Their purpose is an independent consistency witness for the loss bound and small-eta vanishing, not a claim that the bound is tight.

## 4. Falsifiers, limitations and empirical obligations

F1: Any x in (0,1), any legal qubit POVM and quantum instrument with a violation of the exact effect-aware inequality (7.3) invalidates ROT007.

F2: Wrong source spectral projectors P/Q, a different hidden process, different durations or source-active finite pulses invalidate this source-specific calculation. Rebuild source D and H for the new model.

F3: Initial shared entanglement with Alice's measuring apparatus/BC or prior quantum transfer violates the first-local-input contract. Asymptotic LOCC often uses arbitrarily weak instruments: a uniform first-step informative strength cannot be assumed.

F4: **If the first POVM is trivial** (all E_i proportional to I), S2=0 and the theorem makes no strict-loss statement; an outcome-independent disturbance may still reduce TV, but is not certified by (7.4). More generally it does not directly turn into a finite-round proof with arbitrary preliminary operations without their source-typed analysis.

F5: The theorem quantifies the first local POVM and even grants full global readout after it. It is a necessary information-loss condition, not an optimization of all LOCC trees, not an asymptotic positive lower bound, and not a theorem about the R31 sensor with real-time calibration.

F6: No independent external referee, no global LOCC closure theorem, no hardware or novelty inference, no BW or Living Theory adoption.

## 5. Reproduction and exact-source-to-code trace

Standalone script: `IW_PRF13_ROT007_FIRST_LOCAL_MEASUREMENT_INFORMATION_LOSS_REPRO_001_20261112.py`. Python3 + SymPy + NumPy. It constructs the source D twice (positive/negative supports from W, Wbar, Q, K and the original characteristic-function 8x8 matrix), verifies `D=D_+-D_-`, all symbolic H coefficient identities for arbitrary real symbolic x, and evaluates 2500 pseudorandom fully valid `±` Bloch-effect POVM families with 2–10 outcomes. Each diagnostic random instrument uses the actual Lüders square root E and directly tests the trace-norm gain/loss against both the exact effect-aware bound and the weaker C*S2 floor; maximal T/z algebra discrepancy is under 5e-16 at q=1/3. A second sweep of weak two-outcome X measurements checks the vanishing-loss obstruction.

Author output: `ROT007_author_exact_symbolic_and_random_20261112.log`; bytecode compile PASS. These are **same-cell** checks and do not replace an adversarial external referee. Mathematical proof is contained above and uses only identities plus mature trace/fidelity inequalities.

**RETURN:** PRF13_ROT007 / SOURCE_NATIVE_EXACT_3Q_FIRST_INFORMATIVE_MEASUREMENT_LOSS / ANY_LATER_QUANTUM_REENTRY_PERMITTED / PSD_OVERLAP_FIDELITY_BOUND / EFFECT_AWARE_7P3 / UNIVERSAL_QUADRATIC_C_X_S2 / EXACT_SYMBOLIC_H_AND_2500_RANDOM_POVMS_PASS / WEAK_MEASUREMENT_UNIFORM_GAP_OBSTRUCTION / FULL_LOCC_CLOSURE_OPEN / EXTERNAL_REFEREE_PENDING / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / BW_PENDING.
