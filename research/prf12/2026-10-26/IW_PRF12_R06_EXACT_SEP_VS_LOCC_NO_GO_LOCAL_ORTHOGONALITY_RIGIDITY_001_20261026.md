---
artifact_id: IW_PRF12_R06_EXACT_SEP_VS_LOCC_NO_GO_LOCAL_ORTHOGONALITY_RIGIDITY_001_20261026
created_at: 2026-10-26
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
problem_id: PRF12_R05_SEP28_IMPLIES_LOCC_QUERY
exposure: PUBLIC
canonical_body_path: research/prf12/2026-10-26/IW_PRF12_R06_EXACT_SEP_VS_LOCC_NO_GO_LOCAL_ORTHOGONALITY_RIGIDITY_001_20261026.md
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_SOURCE_TYPED_LOCAL_NO_GO_PROOF / INDEPENDENT_NUMERIC_MATRIX_CHECK_PASS / ONE_WAY_BOUNDARY_WITNESS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_GENERAL_LOCC_QUANTITATIVE_GAP / NO_LOCC_CLOSURE_EXCLUSION / NO_PHYSICAL_HARDWARE / NO_NOVELTY_OR_PRIORITY_CLAIM / NO_FINITE_PULSE_EXTENSION / NO_FULL_HANDOFF_PACKET_READBACK
function: SCIENCE_FIRST / FOUNDATION_FIRST / TWO_SURFACE_PRIOR_ART / NEGATIVE_KNOWLEDGE_PRESERVING / FALSIFIER_FIRST
---

# PRF12 R06 — Separator SEP/LOCC: niemożliwość dokładnego osiągnięcia Helstroma przez skończony LOCC dla zamrożonego trójkubitowego modelu

**26 October 2026; owner PRF12.** Status: własny ścisły argument dla syntetycznej rodziny R04/R05, numeryczne odtworzenie macierzy na 8D i 28 efektów, brak niezależnego review. **Werdykt:** oddzielne laboratoria trzech kubitów + tylko local operations and classical communication (LOCC), bez wspólnego splątania i bez kanału kwantowego, NIE zrealizują dokładnego endpoint Helstrom tej rodziny w żadnym skończonym protokole. Tymczasem istnieje dokładny 28-elementowy separowalny POVM z R05. Argument jest source-specific i należy do dojrzałej rodziny technik *orthogonality-preserving local measurements*, nie jest twierdzeniem o nowości gatunku.

## 0. History / host subtraction / external precedents

INTERNAL:
- PRF11 R29–R35: first owner static hidden Cauchy ξ vs Cauchy–Lévy increments and ideal SWAP source contract. PRF11 R35: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R35_NONUNIFORM_SWAP_TIME_GRID_RECOVERS_IDEAL_MEMORY_WITH_CRITICAL_STORAGE_RATE_001_20261025.md
- PRF12 R01: clock/error boundary: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R01_CLOCK_BUDGET_GATE_ERRORS_AND_TWO_TIER_SCHEDULE_001_20261026.md
- PRF12 R02: source-active finite-duration SWAP Hamiltonian/Lindblad: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R02_FINITE_DURATION_SWAP_CAUCHY_ACTIVE_PULSES_AND_RESOURCE_GATE_001_20261026.md
- PRF12 R03: n=2 local X parity achieves endpoint Helstrom: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R03_FINITE_TWO_PROBE_SWAP_CAUCHY_SECTOR_PARITY_HELSTROM_001_20261026.md
- PRF12 R04: exact n=3 sector block and strict loss of full X: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R04_THREE_PROBE_FINITE_SWAP_EXACT_X_READOUT_GAP_AND_SECTOR_DECOMPOSITION_001_20261026.md
- PRF12 R05: explicit 28 rank-one PRODUCT POVM attaining the n=3 ideal endpoint Helstrom but NOT shown LOCC: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R05_SEPARABLE_HELSTROM_POVM_PRODUCT_BASES_AND_ONE_CNOT_RESOURCE_AUDIT_001_20261026.md

MATURE EXTERNAL PRECEDENTS:
- S. M. Cohen, *When a quantum measurement can be implemented locally, and when it cannot*, Phys. Rev. A 84, 052322 (2011), https://doi.org/10.1103/PhysRevA.84.052322; SEP may be strictly beyond finite-round LOCC.
- S. M. Cohen, *Local quantum protocols for separable measurements with many parties*, Phys. Rev. A 87, 052135 (2013), https://doi.org/10.1103/PhysRevA.87.052135; multiparty measurement trees and finite-round obstructions.
- S. M. Cohen, *Extended necessary condition for LOCC: Tight bound for all measurements*, Phys. Rev. A 91, 062125 (2015), https://doi.org/10.1103/PhysRevA.91.062125; analytic necessary conditions and SEP–LOCC separations.
- S. M. Cohen, *General approach to quantum channel impossibility by LOCC*, Phys. Rev. Lett. 118, 020501 (2017), https://doi.org/10.1103/PhysRevLett.118.020501; related linear-equation impossibility, potentially infinite-round distinctions.
- Duan, Xin, Ying, *Locally indistinguishable subspaces spanned by three-qubit unextendible product bases*, Phys. Rev. A 81, 032329 (2010), https://doi.org/10.1103/PhysRevA.81.032329; locally indistinguishable subspaces on three qubits, DIFFERENT source problem.
- *Strong quantum nonlocality without entanglement in every (n−1)-partition*, accessible PMC, https://pmc.ncbi.nlm.nih.gov/articles/PMC11732064/; recent local orthogonality-preservation discussions.
- *Entangled measurement for W states*, Science Advances (2025), https://doi.org/10.1126/sciadv.adx4180; W-state measurements in different experimental setting, not a prior proof for our binary Cauchy/Lévy family.

PRIOR-ART SUBTRACTION: orthogonality preserving POVMs, locally irreducible sets/subspaces, W-state algebra and SEP≠LOCC are established. The report's local contribution is a fully explicit, unusually short certificate for the particular PRF11-sourced R04/R05 discrimination pair and an extra one-way restricted benchmark. No independent priority search establishes scientific novelty.

## 1. Model and spectral contract: exactly the one used in R04/R05

Only n=3, strictly positive γT, ideal instantaneous SWAP, equal exposures Δ1=Δ2=Δ3=T/3, κ=0; input |+>^{⊗3}. A is ONE static hidden ξ~Cauchy(0,γ) for all exposure intervals, B is independent Cauchy–Lévy increments. Put q=γT/3>0, x=e^(−q)∈(0,1), b=1−x², a=xb.

PRF12 R04 matrix difference D=ρ_A−ρ_B has support exclusively on one- and two-excitation sectors; in the 3+3 complementary ordering:

 D_(N1,N2)=(1/8)*[[b(J3−I3), a I3],[a I3,b(J3−I3)]],

zero on |000>,|111>. Define normalized symmetric W state and its bit complement:

 |W>=(|001>+|010>+|100>)/√3,
 |Wbar>=(|110>+|101>+|011>)/√3.

The **strictly positive spectral subspace** is P=span{|W>,|Wbar>} (rank 2). The **strictly negative spectral subspace** Q is the two-dimensional standard-representation complement of W in weight 1 PLUS the analogous standard complement of Wbar in weight 2 (total rank 4). The zero subspace K=span{|000>,|111>} has rank 2.

Nonzero eigenvalues:
  positive b(2+x)/8, b(2−x)/8;
  negative −b(1+x)/8 twice, −b(1−x)/8 twice.
All signs are STRICT for every q>0. Hence:

 TV_Hel=0.5||D||1=b/2=(1−e^(−2q))/2.           (R06.1)

The 28-product-effect POVM from R05 has binary aggregate

 E_+ = P_P + (1/3)P_K,
 E_- = P_Q + (2/3)P_K,                         (R06.2)

and **saturates** TV_Hel for every q>0. It is a mathematical SEP POVM and is not assumed to have any LOCC implementation.

## 2. Orthogonality-preserving first local step: necessary for any exact LOCC Helstrom readout

Let {E_+,E_-} be ANY binary POVM attaining Helstrom for the states ρ_A,ρ_B at equal priors. After choosing the favorable labeling, equality in the variational formula forces E_+ to act as identity on P and zero on Q, E_- as zero on P and identity on Q. Freedom on the kernel K does not help. Therefore the same measurement would perfectly distinguish any state with support in P from any state with support in Q. This is a stronger test pair than the original nonorthogonal mixed states but is NECESSARILY solved if original endpoint Helstrom is attained.

Suppose the FIRST quantum instrument operation in a finite-round LOCC tree is applied locally on one qubit. For any fine-grained first outcome μ with Kraus map M_μ on that qubit, define positive local effect \(F_\mu=M_\mu^\dagger M_\mu\). If later stages are to distinguish all states in P from all states in Q perfectly conditioned on μ, then (strict preservation of support orthogonality)

  \(\langle p | (F_\mu\otimes I\otimes I)|q\rangle=0\)
  for EVERY p∈P and q∈Q.                             (R06.3)

If (R06.3) failed, the conditional images of some p and q would not be orthogonal and deterministic exact downstream discrimination would be impossible. Refining any multikraus outcome is allowed and cannot rescue this condition.

### Two explicit orthogonality witnesses — no free local measurement

Consider qubit 1, and write the most general local Hermitian positive effect:

 \(F=\begin{pmatrix}\alpha&z\\z^*&\delta\end{pmatrix}.\)

Choose two **orthonormal-to-W negative vectors**:

 \(|u\rangle=(2|100\rangle-|010\rangle-|001\rangle)/\sqrt6\in Q,\)
 \(|v\rangle=(2|011\rangle-|101\rangle-|110\rangle)/\sqrt6\in Q.\)

Direct three-qubit inner products give

 \(\langle W|F_1|u\rangle={2(\delta-\alpha)\over\sqrt{18}},\)     (R06.4)
 \(\langle W|F_1|v\rangle={-2z\over\sqrt{18}}.\)                    (R06.5)

Therefore (R06.3) enforces δ=α and z=0, equivalently

 \(\boxed{F_\mu=\alpha_\mu I_2\quad\text{for EVERY admissible first local outcome.}}\) (R06.6)

As P and Q are invariant under permutations of the three qubits, the argument applies identically whichever party attempts to start LOCC. **No party has a nontrivial orthogonality-preserving local first step.**

### Rigidity beyond the first node

A Kraus operator on a 2D qubit satisfying \(M^\dagger M=\alpha I\) is \(\sqrt{\alpha}\,U\) for a unitary U (or zero). Thus such a first operation reveals no information about the input and only performs a known local unitary, perhaps with a private classical random label. Undoing any known local unitary is free in LOCC; after the first node the same rigid P/Q geometry recurs. A finite LOCC tree with at least one informative leaf must have a first informative operation along some branch. R06.6 excludes that operation by induction.

\[
\boxed{\mathrm{TV}_{\rm LOCC,\ finite\ exact}<\mathrm{TV}_{\rm Hel}\quad\text{for every single finite-round LOCC protocol}.}\tag{R06.7}
\]

**Care with the strict quantifier:** R06.7 means every individually chosen finite-round LOCC POVM is strictly suboptimal. It does NOT prove existence of any **uniform constant** gap to the supremum over all finite-round protocols; this supremum could conceivably approach Helstrom. We did not establish whether this measurement is in the closure of LOCC, or whether any strictly positive resource cost is necessary in the limit of approximation. For standard countable-round exact LOCC with only classical transcripts and no nonlocal resource, the same first-informative-outcome obstruction suggests nonimplementability, but the formal theorem and auditable claim ceiling here are the **finite-round** case; infinite-round conventions require separate analysis.

Local ancillas initially product with each lab, shared classical randomness, local unitaries, and arbitrarily many (finite) classical communications do not change (R06.6). Shared *entanglement*, quantum channel transmission, pre-merged laboratories, or nonlocal gate resources are NOT covered.

## 3. Independent 8×8 and rank/Pauli basis verifier

Each single-qubit Hermitian effect has Pauli decomposition \(F=tI+xX+yY+zZ\) with REAL x,y,z. The previous two witnesses constrain z=0 and x−iy=0, hence x=y=0. Independent NumPy projection on the full positive/negative spectral subspaces finds for every party j=1,2,3:

 singular values of \(F\mapsto P_P F_j P_Q\) on basis (I,Z,X,Y):
   1.3333333333, 0.6666666667, 0.6666666667, <5×10^(−16).

The only null direction is local I; the scalar-effect condition is therefore EXACT, not dependent on q, κ, or finite-sample fitting (within the frozen ideal κ=0 family, q>0).

The source-independent SEP28 construction from R05 is also rechecked in the same code:
- 4 product rank-one + effects, 24 product rank-one − effects, all PSD.
- Max closure matrix entry |ΣE−I| = 4.44×10^(−16).
- Max error |E_+−P_P−P_K/3|=2.78×10^(−16).
- For q=0.05,1/3,0.7,1.4 the exact SEP witness matches TV_Hel ≤1×10^(−15).

This independently guards against accidentally proving a LOCC no-go for a POVM that was not separable in the first place.

## 4. Quantitative one-way benchmark with a RESTRICTED two-laboratory resource

Separate from three-party LOCC, allow party A (qubit 1) to measure X projectively, send its result to a *merged* B+C laboratory, and permit B+C to perform an arbitrary collective two-qubit endpoint Helstrom POVM conditioned on A. This is a **two-block A|BC** protocol, not LOCC among THREE separated qubits; do not relabel it as a three-party LOCC upper bound.

Writing x=e^(−q) and b=1−x², a direct 4×4 conditional diagonalization gives:

 \(\boxed{\mathrm{TV}_{A:X;\,BC:\mathrm{joint}}=
 {b\over32}[4+2x+\sqrt{x^2+4x+20}+\sqrt{x^2-4x+20}].}\)  (R06.8)

For q=1/3:

| Measurement/resource | TV |
|---|---:|
| three fully local X outcomes (R04) | 0.189292628451 |
| FIRST A measure X, THEN BC **joint Helstrom** (R06.8) | 0.220014079553 |
| SEP28 R05 (abstract separable POVM) | 0.243291440484 |
| unrestricted endpoint Helstrom | 0.243291440484 |

This demonstrates a partial intermediate resource ladder, not a theorem about all bipartition LOCC or all separable projectors. In particular, 0.220014 is neither a certified maximum over all A first bases nor over all three-party LOCC.

For q=.05,.7,1.4 the independent numerical conditional-state calculation matches formula (R06.8) to machine precision. Both source states are computed by the exact R04 static-Cauchy vs Lévy matrix entries, no active-pulse extrapolation.

## 5. Falsifiers, boundary conditions and independent referee

F1: If any local positive non-scalar F has \(P_P F_j P_Q=0\) for this exact P/Q, R06 no-go falls. Matrices in §3 and explicit witnesses §2 provide an easily independent falsification path.

F2: If kernel K=span(000,111) allowed to accept mistaken signs on positive/negative subspaces without affecting Helstrom, the equality argument would fail; it does NOT, because D has STRICT nonzero eigenvalues on P/Q for q>0. Freedom is only on K.

F3: If a fully specified finite LOCC tree with pre-shared classical randomness and NO quantum nonlocal resource can exactly realize binary effects attaining TV_Hel, R06 is false. Such a tree must violate (R06.3) somewhere; the contradiction is testable.

F4: If individual local operations have multiple Kraus labels, refine them at the first step; deterministic exact distinguishability of two orthogonal subspaces remains necessary on each nonzero fine-grained branch.

F5: q→0 annihilates signal; q=0 gives D=0 and no distinguishability obstruction. Do NOT state q≥0 theorem; strict q>0 is essential.

F6: Source-active finite pulses and κ>0 (R04/R05 numerics) change eigenvectors and possibly null space. R06 proof is NOT automatically valid there, although candidate numerical gaps exist; source typed scope remains κ=0/ideal instantaneous equal exposures.

F7: No globally positive gap \(\inf_{\mathrm{finite\ LOCC}}(\mathrm{TV}_H-\mathrm{TV})>0\) established, no exclusion of \(\overline{\mathrm{LOCC}}\) closure, and no operational lower bound in ebits, CNOT count or communication cost. It would be invalid to infer experimental entangling hardware requirements solely from SEP≠LOCC.

F8: The result concerns endpoint binary discrimination under a fixed n=3 SWAP protocol, not the process-tensor norm over arbitrary adaptive controls, not physical Cauchy device realization, not NCDG K/J3, not LT canon and not an EXEC claim.

**Referee priority:**
1. Independently reconstruct eigenprojectors P/Q/K for PRF11 source states at n=3 equal Δ, κ=0.
2. Check E_+ Helstrom equality and its forced complete support/zero support on P/Q.
3. Verify explicit inner products R06.4–R06.5, in particular z orientation; avoid complex-conjugation convention error.
4. Audit LOCC first-node condition for arbitrary local ancillas and fine-grained Kraus maps.
5. Investigate quantitative approximate LOCC, LOCC closure and maximal A|BC protocol; current no-go is only exact finite-round.
6. Investigate source-active finite-duration robustness, where spectral subspaces may differ.

## 6. Fully reproducible custody and status

Code (Python 3, NumPy, no private data):
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R06_SEP_NOT_EXACT_LOCC_LOCAL_RIGIDITY_REPRO_001_20261026.py

This includes source-state matrix, P/Q/K, all three local Pauli linear maps, full SEP28 reconstruction, positive/negative support audit, and restricted one-way 4×4 analytic formula. It was executed locally before upload: local-map singular values (4/3,2/3,2/3,0) for all three parties, closure 4.44e−16, equality Helstrom for q=.05,1/3,.7,1.4, and restricted A-X/BC-joint TV=0.2200140795526928 at q=1/3.

**No BW readback**; GitHub scientific body committed with source code. State-based PRF12 limited succession inherited: full prior ZIP is not present/read. Do not silently declare new canonical claim, device observation, novelty, LOCC approximation lower bound or referee PASS.

## 7. RETURN

PRF12_R06 / EXACT_LOCAL_ORTHOGONALITY_RIGIDITY / FINITE_ROUND_EXACT_LOCC_NO_GO / SEP28_EXACT_HELSTROM_SOURCE_TYPED / FULL_3_PARTY_PAULI_MATRIX_CHECK_PASS / RESTRICTED_A_X_BC_JOINT_FORMULA / EXTERNAL_PRIOR_ART_SUBTRACTION / INDEPENDENT_REFEREE_PENDING / NO_GENERAL_QUANT_GAP / LOCC_CLOSURE_OPEN / SOURCE_ACTIVE_EXTENSION_OPEN / NO_NOVELTY / NO_CANON / NO_EXEC / GITHUB_PENDING_BW_INGEST / PRF12_SUCCESSION_PACKET_UNREAD.
