---
artifact_id: IW_PRF12_R07_POSITIVE_ASYMPTOTIC_LOCC_GAP_VIA_ZONOTOPE_PRODUCT_PATH_OBSTRUCTION_001_20261026
created_at: 2026-10-26
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
problem_id: PRF12_R06_FINITE_LOCC_NO_GO_VS_LOCC_CLOSURE
exposure: PUBLIC
canonical_body_path: research/prf12/2026-10-26/IW_PRF12_R07_POSITIVE_ASYMPTOTIC_LOCC_GAP_VIA_ZONOTOPE_PRODUCT_PATH_OBSTRUCTION_001_20261026.md
sync_state: GITHUB_PENDING_BW_INGEST
status: CORRECTION_REQUIRED_DUE_TO_COARSE_GRAINING_INVALIDATION / SCIENTIFIC_POSITIVE_LOCC_GAP_CLAIM_NOT_PROVED
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NUMERICAL_LOCC_GAP_LOWER_BOUND / NO_OPTIMAL_LOCC_VALUE / NO_EBIT_COST / NO_FINITE_SWAP_TRANSFER / NO_PHYSICAL_DEVICE / NO_NOVELTY_OR_PRIORITY_CLAIM / NO_FULL_SUCCESSION_PACKET_READBACK
function: SCIENCE_FIRST / LITERATURE_FIRST / TWO_SURFACE_PRIOR_ART / NEGATIVE_KNOWLEDGE / FALSIFIER_FIRST
---

> **CRITICAL CORRECTION / CLAIM WITHDRAWN — PRF12 R09 AUDIT, 2026-10-26.** R07's application of Cohen (2022) Theorem 1 to the **binary decision effects** E_+=P+K and E_-=I-E_+ is invalid without a refinement-preserving argument. LOCC may measure a fine-grained PRODUCT-effect POVM and classically coarse-grain many leaves into a NONPRODUCT binary effect (e.g. two local Z measurements with an even-parity decision). Absence of non-scalar product operators from the BINARY DECISION zonotope thus does not establish nonmembership of the operational discrimination protocol in closure(LOCC). The R07 claim \`delta(q)>0\` for all three-party LOCC/closure **is NOT ESTABLISHED by this report and MUST NOT be cited as proved.** Its algebraic lemmas about the binary-effect zonotope remain valid only as statements for THAT restricted geometric object. R06's direct finite-round exact local-orthogonality argument and R05's 28-effect SEP construction are separate and not refuted by this correction. See PRF12 R09 audit at \`research/prf12/2026-10-26/IW_PRF12_R09_COARSE_GRAINING_COHEN_THEOREM_AUDIT_AND_CORRECTED_CLAIM_CEILING_001_20261026.md\`.


# PRF12 R07 — Ściśle dodatnia luka asymptotycznego LOCC w trzypróbkowej rodzinie Cauchy–Lévy

**Właściciel/funkcja:** PRF12, obrót R07 26.10.2026. **Najistotniejsza korekta granicy R06:** nie tylko żaden skończony LOCC nie uzyskuje dokładnie Helstroma — jego granica nie leży nawet w topologicznym domknięciu trójstronnego LOCC. Dowód korzysta z dojrzałego, ZEWNETRZNEGO twierdzenia o ścieżkach produktowych Cohena (2022); nowa jest tylko konkretna algebra oparta na modelu PRF11/R04/R05. **Ścisłość wyniku:** dodatnia luka istnieje; jej liczbowej dolnej granicy nie wyprowadzono.

## 0. First owner / nowy priorytet literaturowy / no novelty claim

**Repozytorium, pierwszeństwo i ograniczenia:**
- PRF11 R35 (first owner): https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R35_NONUNIFORM_SWAP_TIME_GRID_RECOVERS_IDEAL_MEMORY_WITH_CRITICAL_STORAGE_RATE_001_20261025.md — correlated static Cauchy vs independent Cauchy–Lévy in an ideal SWAP program.
- PRF12 R01: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R01_CLOCK_BUDGET_GATE_ERRORS_AND_TWO_TIER_SCHEDULE_001_20261026.md — clock/resource constraint.
- PRF12 R02: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R02_FINITE_DURATION_SWAP_CAUCHY_ACTIVE_PULSES_AND_RESOURCE_GATE_001_20261026.md — source active during finite SWAP.
- PRF12 R03: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R03_FINITE_TWO_PROBE_SWAP_CAUCHY_SECTOR_PARITY_HELSTROM_001_20261026.md — two-probe parity sufficiency.
- PRF12 R04: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R04_THREE_PROBE_FINITE_SWAP_EXACT_X_READOUT_GAP_AND_SECTOR_DECOMPOSITION_001_20261026.md — exact three-probe Helstrom vs full local X.
- PRF12 R05: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R05_SEPARABLE_HELSTROM_POVM_PRODUCT_BASES_AND_ONE_CNOT_RESOURCE_AUDIT_001_20261026.md — explicit *separable* 28-product-effect POVM attaining Helstrom.
- PRF12 R06: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R06_EXACT_SEP_VS_LOCC_NO_GO_LOCAL_ORTHOGONALITY_RIGIDITY_001_20261026.md — exact finite-round LOCC obstruction, LOCC closure explicitly left OPEN in R06.

**Mature external hosts — foundational, essential for R07 proof:**
1. S. M. Cohen, **Local approximation of multipartite quantum measurements**, *Phys. Rev. A* **105**, 022207 (14 February 2022), DOI https://doi.org/10.1103/PhysRevA.105.022207 ; full theorem available as https://arxiv.org/html/1912.02330v2 ; **Theorem 1** establishes a necessary condition for membership of a POVM in the closure of LOCC: for *each effect* E_j a continuous *trace-monotonic* product-operator path from I to a nonzero point of (0,E_j] within the POVM's zonotope Z={Σ_j c_j E_j, 0≤c_j≤1}. This is **not** a theorem discovered by PRF12.
2. Kleinmann, Kampermann, Bruß, **Asymptotically perfect discrimination in the local-operation-and-classical-communication paradigm**, *Phys. Rev. A* **84**, 042326 (2011), DOI https://doi.org/10.1103/PhysRevA.84.042326 — earlier necessary criteria for *asymptotic* perfect discrimination.
3. S. M. Cohen, **Local approximation for perfect discrimination of quantum states**, *Phys. Rev. A* **107**, 012401 (2023), DOI https://doi.org/10.1103/PhysRevA.107.012401, WITH ERRATUM *PRA* 108, 029902 (2023). Its pure-state error bounds are different from the present mixed-state Helstrom optimization, and were NOT silently assumed.
4. S. M. Cohen, **Structure of LOCC: finite versus infinite rounds**, *Phys. Rev. A* **91**, 042106 (2015), https://doi.org/10.1103/PhysRevA.91.042106 — the distinction between nonattainment and no approximation; why R06 alone was insufficient.
5. S. M. Cohen, **General Approach to Quantum Channel Impossibility by LOCC**, *Phys. Rev. Lett.* **118**, 020501 (2017), https://doi.org/10.1103/PhysRevLett.118.020501 — channel-implementation constraints, not substituted for the 2022 POVM closure theorem.

**External prior-art subtraction:** geometric zonotopes, monotone product paths, quantum nonlocality without entanglement, LOCC vs SEP and "asymptotic LOCC may fail" are ALL mature phenomena. R07 is a source-specific application to the established PRF11 triple Cauchy/Lévy pair, not a novelty or publication-priority claim.

## 1. Exact frozen problem, unchanged from R04–R06

Exactly n=3, equal free exposure times Δ1=Δ2=Δ3=T/3, *ideal instantaneous* SWAPs, κ=0, input |+>⊗3. Hypothesis A is one global hidden ξ~Cauchy(0,γ), hypothesis B independent Cauchy–Lévy increments; no other coherent controls. Fix q=γT/3>0, x=e^(−q)∈(0,1), b=1−x², a=xb. D(q)=ρ_A−ρ_B has computational-basis elements

 \(D(q)_{s,t}=8^{-1}[\exp(-q|\sum_j(s_j-t_j)|)-\exp(-q\sum_j|s_j-t_j|)]\).

As derived in R04, the spectral decomposition has:
- positive space P=span\{|W>,|Wbar>\}, with |W>=(|001>+|010>+|100>)/sqrt(3), |Wbar>=(|110>+|101>+|011>)/sqrt(3);
- negative space Q=two standard representations in Hamming-weight 1 and 2, total rank 4;
- kernel K0=span\{|000>,|111>\}, rank 2.

Positive eigenvalues b(2±x)/8, four negative eigenvalues −b(1±x)/8 each with multiplicity 2, and two zero eigenvalues. All *nonzero* eigenvalues remain strictly separated from 0 for every fixed q>0. Denote corresponding projectors P,Q,K0, with P+Q+K0=I.

Unrestricted endpoint Helstrom distinguishability:

 \(\mathrm{TV}_H(q)=\tfrac12\|D(q)\|_1=b/2=(1-e^{-2q})/2.\)   (R07.1)

The three qubits are assumed to reside in physically isolated laboratories when LOCC is discussed; if all can be jointly measured in one lab, the LOCC restriction is irrelevant.

## 2. All possible exact Helstrom binary POVMs, INCLUDING arbitrary kernel freedom

Let E be the effect associated with guessing hypothesis A after any quantum measurement plus classical decision (the other effect I−E guesses B). At equal priors, \(\mathrm{TV}_E=|\mathrm{Tr}(E D(q))|\), with orientation E→I−E chosen to make it nonnegative.

Equality \(\mathrm{Tr}(E D)=\mathrm{Tr}(D_+)=b/2\), 0≤E≤I, forces, since every eigenvalue on P/Q is strictly signed:
 
 E restricted to P = I_P, E restricted to Q=0.

PSD of E and I−E additionally forbids off-block coherences between P/Q and K0: if E|p>=|p> and E|q>=0 for all p∈P,q∈Q, then E must be block diagonal in P⊕Q⊕K0. Consequently **every** Helstrom-optimal binary effect has the full family

 \(\boxed{E_+ =P+K,\quad E_-=I-E_+=Q+(K_0-K),\quad 0\le K\le K_0.}\) (R07.2)

Here K may be ANY 2×2 Hermitian PSD contraction *on* span(000,111), including nonreal offdiagonal entry |000><111|. The argument below does not choose K=K0/3 or assume a special result label. This quantifier is crucial for proving a gap in optimal SUCCESS PROBABILITY, not merely an obstruction for one fixed R05 POVM.

## 3. Lemma R07.1 — product-operator rigidity in the ENTIRE binary zonotope

For arbitrary K as (R07.2), define two-outcome zonotope:

 \({\cal Z}_K=\{\alpha E_+ +\beta E_-:0\le\alpha,\beta\le1\}\)
 \(\qquad =\{\beta I+(\alpha-\beta)(P+K):0\le\alpha,\beta\le1\}.\)    (R07.3)

**Lemma:** every **strictly positive definite** operator \(F\in{\cal Z}_K\) that is a positive three-party product \(F=A\otimes B\otimes C\), A,B,C≥0, is a scalar multiple of the identity.

**Elementary exact proof, independent of q and K.** Every operator F from (R07.3) has ZERO offdiagonal matrix entries between any two computational bitstrings differing in exactly ONE bit. Why: P contains nonzero offdiagonal elements only between distinct weight-1 strings or distinct weight-2 strings, which differ in precisely TWO bits; K is supported in the 000/111 block and may couple only strings differing in THREE bits. I is diagonal.

Now suppose F=A⊗B⊗C is **positive definite**. Then A,B,C can be taken positive definite. Consider e.g.

 \(\langle 000|F|100\rangle=A_{01} B_{00} C_{00}=0.\)

B_00,C_00>0, hence A_01=0. Similarly \(\langle000|F|010\rangle=0\) forces B_01=0, and \(\langle000|F|001\rangle=0\) forces C_01=0. Each local factor is Hermitian, therefore ALL factors are DIAGONAL, so F is diagonal.

But the weight-1 pair 001 and 010 has
 \(\langle001|F|010\rangle=(\alpha-\beta)\langle001|P|010\rangle=(\alpha-\beta)/3.\)
Because F is diagonal, \(\alpha=\beta\), yielding \(F=\beta I\). QED.

Notice that the proof allows full arbitrary K (complex coherences |000><111|), all 0≤α,β≤1, all q>0; it is not merely a perturbative derivative argument.

**Numerical falsifiers:** For four K choices (zero, K0/2, generic complex kernel contraction, full K0), direct 8×8 sampling of positive definite F with (α,β)=(.8,.5),(.99,.98) gives F[000,001]=0 and F[001,010]=(α−β)/3, plus second operator Schmidt singular value across 1|23 >0; equal α=β gives second singular value ≤1.4e−16. This only sanity-checks the algebra, not a numeric exhaustive proof.

## 4. Theorem R07.2 — NO Helstrom-optimal binary POVM is in closure(LOCC)

Cohen 2022, Theorem 1 (essential external theorem): if POVM \({\cal M}=\{E_+,E_-\}\) lies in topological closure of LOCC, then each outcome effect E_j admits a continuous path \(\Pi:[0,1]\to{\cal Z}_{\cal M}\) consisting exclusively of positive product operators, starting at \(\Pi(0)=I\), ending at \(\Pi(1)=\lambda E_j\) for SOME \(\lambda>0\), and having a non-increasing trace \(\operatorname{Tr}\Pi(t)\). Here \(E_j\) is the WHOLE binary effect after outcome coarse-graining, not each refined leaf separately.

Assume by contradiction a closure(LOCC) realization of any Helstrom-optimal binary POVM. Its E+=P+K obeys (R07.2). Consider Cohen's product path from I to \(\lambda E_+\) inside \({\cal Z}_K\).

By Lemma R07.1, every FULL-RANK point on this path must be scalar \(c(t)I\). Starting from I, if the continuous path ever reaches a rank-deficient point then, at its first such point, continuity forces it to be \(0\): it is a limit of positive scalar multiples of I, and only \(0\) is a singular scalar operator. At 0 the non-increasing trace condition prevents the path from reaching any later nonzero positive endpoint. Therefore the path can never reach rank deficiency.

But the target \(\lambda E_+\), λ>0, is RANK-DEFICIENT because it vanishes on the four-dimensional Q. Contradiction.

\[
 \boxed{\forall q>0,\;\forall\,0\le K\le K_0:\quad
 \{P+K,Q+(K_0-K)\}\notin\overline{\mathrm{LOCC}}_{A|B|C}.}\tag{R07.4}
\]

This is a **strictly stronger conclusion** than R06 finite-round impossibility; both rely on a *fixed n=3 endpoint* and the stated operational split. It is a rigorous mathematical COROLLARY OF Cohen's established theorem AND the exact source-specific R07.1 lemma, not a standalone newly discovered generic LOCC-closure theorem.

## 5. Theorem R07.3 — strictly positive performance gap, although not numerically known

Define \({\cal B}_{\rm LOCC}\) as the two-outcome LOCC discrimination POVMs for the three physically separated parties, with unrestricted FINITE classical communication rounds, no prior entanglement/quantum channel and no other nonlocal resource. Its operator-norm/finite-dimensional closure \(\overline{{\cal B}_{\rm LOCC}}\) is a CLOSED subset of the COMPACT set of binary effects \(0\le E\le I\). Therefore it is compact.

The endpoint TV functional \(E\mapsto |\mathrm{Tr}(E D(q))|\) is CONTINUOUS and achieves a maximum on the compact closure. Suppose the supremum over LOCC were Helstrom. Then some limit point E* in that closure would be Helstrom-optimal. By (R07.2) it would equal P+K or its complementary orientation for some K. By R07.2 this is forbidden from closure(LOCC), contradiction.

Consequently there exists a **strictly positive but quantitatively UNKNOWN** number \(\delta(q)>0\), at each q>0, such that

 \(\boxed{\sup_{\rm LOCC}\mathrm{TV}(q)
 =\mathrm{TV}_{H}(q)-\delta(q)<\mathrm{TV}_{H}(q).}\)     (R07.5)

In the exact R04/R05 source family:
- SEP28 has \(\mathrm{TV}_{\rm SEP}=\mathrm{TV}_H\) exactly.
- LOCC cannot even approach it arbitrarily.
- q=1/3: \(\mathrm{TV}_H=0.243291440483704\).
- Local X full readout is an admissible LOCC protocol: \(\mathrm{TV}_X=0.189292628450799\).
- Thus, using that explicit LOCC witness, \(\boxed{0<\delta(1/3)\le0.053998812032905}\). The right side is an **upper bound on the unknown gap**, NOT an attained optimum or a lower bound.
- For any compact q range [q0,q1] with 0<q0≤q1<∞, the continuous maximal LOCC value and R07.5 imply a positive minimum gap over that range. It cannot be stated uniformly for all q>0 without qualification because the signal itself vanishes at q→0.

**Perturbation corollary (qualitative only):** for another binary traceless state difference D' on the same three-qubit space with \(\|D'-D(q)\|_1=\eta\), both the Helstrom and LOCC values change by at most η/2, so the LOCC performance gap remains at least δ(q)−η. No explicit δ(q) is known; this is NOT evidence that the source-active finite-duration SWAP experiments R04/R05 lie inside that neighborhood. It does not certify experimental implementation or robust hardware bounds.

## 6. Numeric independent checks and reproducible source

The independent R07 verifier computes n=3 exact A/B states DIRECTLY from the Cauchy characteristic functions, forms P/Q/kernel WITHOUT importing previous R06 code, and checks:

- q=0.05,1/3,.7,1.4: predicted D eigenvalues, Helstrom TV = (1−e^(−2q))/2 and P D Q=0 agree to 1e−14 or better;
- four kernel contractions K: K=0, K=K0/2, non-diagonal complex K, K=K0;
- zonotope points (α,β)=(.8,.5),(.99,.98),(.8,.8): all are positive definite, single-bit matrix element zero, two-bit element exactly (α−β)/3; operator-Schmidt second singular value >0 if α≠β and ~1e−16 if α=β.

Source:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R07_ASYMPTOTIC_LOCC_ZONOTOPE_RIGIDITY_REPRO_001_20261026.py

Environment Python 3, numpy; run file directly. The code is an **algebraic verifier**, NOT a numerical simulation of infinite-round LOCC, proof of Cohen's theorem, or a quantitative estimate of δ. The essential asymptotic inference is theorem-based, not extrapolated from finite-round simulation.

## 7. Falsifiers and independent referee

1. **Check exact Cohen theorem** in https://arxiv.org/html/1912.02330v2 , Theorem 1, including definition of monotonic *trace* and nonzero endpoint λE_j, zonotope of *the binary coarse-grained effects*, not merely each rank-one SEP leaf. Without the published theorem R06 does not by itself prove R07.
2. Confirm any Helstrom-optimal binary decision has precisely E+=P+K (or complement) with K allowed to have COMPLEX coherence between |000>,|111>, all PSD 0≤K≤I_K; no missing cross-term mixing under positivity/equality.
3. Check every element of Z_K has zero computational *single-bit-flip* coherences, while P has <001|P|010>=1/3. Recheck argument for positive definite 2×2 local product factors, which is valid for 3 remote qubits with arbitrary local ancillas already absorbed into effective effects.
4. Audit the "first loss of rank" topological/monotonic argument. If one constructs a nonzero continuous trace-monotone positive-product path from I to λ(P+K) lying inside Z_K, R07 claim is falsified.
5. Audit that binary classical postprocessing of any LOCC measurement is LOCC, and that finite-dimensional binary POVM compactness applies even if number of refined outcomes/LOCC rounds is unrestricted.
6. **No numeric positive lower bound on δ(q)**. Compactness proves existence only; 0.053998812 at q=1/3 is an *upper* bound from an X protocol. A subsequent work could derive a certified lower bound using quantitative stability of product paths and Cohen's proof.
7. Results do NOT address finite active pulses, κ>0, non-equal exposure times, arbitrary joint laboratories, hardware realization, generalized process-tensor norm, shared prior entanglement, CNOT-gate cost, or physical resource rates.
8. Do not promote R07 into NCDG gravity, physical interpretation, NOVELTY, CANON, EXEC, or synchronized BW without an owner-approved readback.

## 8. RETURN

PRF12_R07 / FIRST_OWNER_PRF11_CAUCHY_SWAP / COHEN_2022_THEOREM_1_EXTERNAL_LOAD_BEARING / ALL_HELSTROM_POVMS_KERNEL_COMPLETE / FULL_RANK_BINARY_ZONOTOPE_PRODUCT_RIGIDITY / NOT_IN_CLOSURE_LOCC / STRICT_EXISTENTIAL_ASYMPTOTIC_LOCC_PERFORMANCE_GAP / DELTA_NUMERIC_UNKNOWN / INDEPENDENT_N3_MATRIX_CHECKS_PASS / REFEREE_PENDING / NO_EXEC / NO_CANON / NO_NOVELTY / GITHUB_PENDING_BW_INGEST / PRF12_SUCCESSION_PACKET_UNREAD.
