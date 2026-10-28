---
artifact_id: IW_PRF12_R14_SOURCE_RESET_AND_UNAMBIGUOUS_LOCC_AUDIT_001_20261028
created_at: 2026-10-28
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
problem_id: PRF12_R13_ORTHOGONAL_MIXED_PAIR_AND_FULL_LOCC_CLOSURE_OPEN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_SOURCE_TYPED_SUPPORT_THEOREM / UNAMBIGUOUS_SEP_NO_GO / TWO_RUN_RESET_DICHOTOMY / KERNEL_FILTER_NEGATIVE_KNOWLEDGE / NUMERIC_AND_SYMBOLIC_REPRO_PASS / REFEREE_PENDING
claim_ceiling: NO_FULL_SINGLE_COPY_LOCC_CLOSURE_GAP / NO_PHYSICAL_IMPLEMENTATION / NO_PRIOR_ART_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# PRF12 R14 — Nośnik symetryczny, bezbłędne świadectwo źródła i fundamentalny wpływ resetowania Cauchy'ego

**Data:** 28 października 2026. **Funkcja:** PRF12, następca PRF11. **Wynik naukowy:** oryginalna para źródeł Cauchy-vs-Lévy posiada subtelnie inną strukturę operacyjną niż pomocnicza ortogonalna para P/2-vs-Q/4 z R13. Dla pojedynczego przebiegu B można jednoznacznie potwierdzić pomiarem globalnym, ale nie separowalnym. Przy wielu niezależnie *resetowanych* przebiegach zakaz separowalnego bezbłędnego świadectwa B nadal obowiązuje dla każdej skończonej liczby kopii, choć zwykła lokalna klasyfikacja uzyskuje błąd malejący wykładniczo. Jeśli natomiast jedna zmienna ξ jest wspólna dla dwóch przebiegów, JUŻ LOKALNY pomiar antysymetryczny na dwóch kubitach jednego laboratorium daje bezbłędne świadectwo B z dodatnim prawdopodobieństwem. To jest rozróżnienie kontraktów źródła, a nie obejście twierdzenia dla niezależnych bloków.

## 0. Pierwszeństwo, zewnętrzne metody i oddzielenie zadań

**Pierwszy właściciel i kontekst:** PRF11 R35 (static common Cauchy ξ kontra independent Cauchy–Lévy increments w protokole SWAP); PRF12 R04 (trzy próbki i dokładne końcowe macierze), R05/R11/R12 (separowalny optymalny pomiar Helstroma mimo braku globalnego LOCC-no-go), R06 (zakaz dokładnego finite-round LOCC dla oryginalnych n=3 stanów), R09 (wycofanie R07 o domknięciu LOCC wskutek coarse-graining), R13 (redukowanie *minimum-error binary* do pomocniczych stanów ortogonalnych P/2 i Q/4 oraz kernel bridge). Kluczowy raport R13: `IW_PRF12_R13_RESEARCH_REPORT_001_20261028.md`; publiczny indeks: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-28/IW_PRF12_R13_SCIENCE_STATUS_001_20261028.md .

**Mature external prior art:** (i) Helstrom, *Quantum Detection and Estimation Theory* (1976); (ii) Feng–Duan–Ying, *Unambiguous discrimination between mixed quantum states*, PRA 70, 012308 (2004), https://doi.org/10.1103/PhysRevA.70.012308 ; (iii) Parthasarathy/generic completely entangled subspaces, see *Generic local distinguishability and completely entangled subspaces*, J. Phys. A 41, 375305 (2008), https://doi.org/10.1088/1751-8113/41/37/375305 ; (iv) Filippov–Ziman, *Probability-based comparison of quantum states*, PRA 85, 062301 (2012), https://doi.org/10.1103/PhysRevA.85.062301 ; (v) Kleinmann–Kampermann–Bruß, *Asymptotically perfect discrimination in the LOCC paradigm*, PRA 84, 042326 (2011), https://doi.org/10.1103/PhysRevA.84.042326 ; (vi) Cohen, *Local approximation of multipartite quantum measurements*, PRA 105, 022207 (2022), https://doi.org/10.1103/PhysRevA.105.022207 . Unambiguous state comparison, SWAP tests, support criteria and polynomial nonzero arguments are mature methods. R14 gives only source-typed algebra, no external discovery priority.

**Three DIFFERENT operational questions:**
1. *One-copy, binary, minimum-error*, with arbitrary number of LOCC rounds: does the full LOCC closure attain global Helstrom? **STILL OPEN** since R09. R14 does not claim an answer.
2. *One-sided unambiguous B detection*, allowing an inconclusive outcome: exact zero false positive A. Not equivalent to binary minimum error. R14 proves a separable obstruction in the physical original A/B states.
3. *Repeated blocks*: the joint density depends decisively on whether static ξ is freshly redrawn each block or persists across blocks. Number of copies is NOT number of LOCC rounds on a single copy.

## 1. Frozen single-block contract, support and global unambiguous optimum

Exactly three equal free exposures Δ=T/3 with ideal instantaneous SWAPs, initial |+>³, κ=0, q=γΔ>0, x=e^(−q)∈(0,1). For an equatorial spinor |u(z)>=(|0>+z|1>)/sqrt(2) and z=e^{−iξΔ}, model A is a continuous positive-weight mixture of |u(z)>^{⊗3} across ξ~Cauchy(0,γ). Its support is EXACTLY the symmetric subspace Sym³(C²), rank 4: the four monomials 1,z,z²,z³ are independent over the circle and the Cauchy phase density is everywhere positive. Write S for its projector, Q=I−S for the rank-four nonsymmetric projector. This Q equals the previous negative spectral projector in R04/R13. Model B has the FULL-RANK density

ρ_B=ρ_1^{⊗3}, ρ_1=(I+xX)/2,

with positive single-qubit eigenvalues (1±x)/2.

**Theorem R14.1.** An event E≥0 is an unambiguous certificate of B only if Tr(Eρ_A)=0, which since ρ_A is positive definite ON S forces E=QEQ. For unrestricted global effects, E=Q maximizes Tr(Eρ_B) among 0≤E≤I, so

p^{global}_{B-only}=Tr(Qρ_B)=(1−x²)/2.

Independent group-theoretic derivation: S=(1/6)∑_{π∈S3} U_π, so Tr(Sρ_1^{⊗3})=[1+3Tr(ρ_1²)+2Tr(ρ_1³)]/6=(1+x²)/2. Therefore Tr(Qρ_B)=1−(1+x²)/2=(1−x²)/2. Since Q is also the negative Helstrom support, binary decision B on Q and A otherwise attains the EXACT global endpoint Helstrom TV=(1−x²)/2. These are distinct decision metrics: the same global measurement is one-sided unambiguous and minimum-error optimal.

There is NO unambiguous global A event, since ρ_B is full rank and Tr(Eρ_B)=0 with E≥0 forces E=0.

## 2. Theorem R14.2 — no separable unambiguous B outcome on ONE copy

The nonsymmetric subspace Q=Sym³(C²)^{perp} contains NO nonzero fully product vector. For any nonzero three-qubit product ket |a>⊗|b>⊗|c>, its overlap with |u(z)>^{⊗3} is proportional to the nonzero polynomial

f_a(z) f_b(z) f_c(z), where f_a(z)=<a|0>+z<a|1>, etc.

C[z] is an integral domain, so this product cannot vanish for every |z|=1. Therefore no product vector is orthogonal to S. If E≥0 is SEPARABLE then E is a finite sum of nonnegative rank-one product projectors (decompose every local positive factor spectrally). Tr(Eρ_A)=0 and positivity force EACH nonzero product vector to belong to Q, impossible. Thus E=0. In particular LOCC, as a subset of separable POVMs, cannot yield an unambiguous B outcome on one copy. This does NOT contradict the R11 SEP9 construction attaining binary Helstrom with NONZERO false B positives; unambiguous detection and minimum-error optimality are different tasks.

## 3. Theorem R14.3 — finite independent reset blocks preserve the no-unambiguous-SEP result

Suppose m whole experimental BLOCKS are independently prepared, **including A's hidden ξ resampled independently before each block**. Under A the joint support is S^{⊗m}; under B, (ρ_1^{⊗3})^{⊗m} is full rank. Three spatially distinct labs now each hold m qubits (one from every block); a local operation within one lab may entangle its OWN m qubits. We allow arbitrary positive product effects across the THREE 2^m-dimensional labs.

A general nonzero vector of laboratory L has components a_{b1...bm}. Its overlap with the local orbit |u(z1)>⊗...⊗|u(zm)> is a nonzero MULTIAFFINE polynomial f_L(z1,...,zm) whose coefficients are the components of a (up to harmless conjugation and normalization). For an overall product |a>_L1⊗|b>_L2⊗|c>_L3, overlap with the original-source orbit ∏_{j=1}^m |u(z_j)>^{⊗3} is f_a(z) f_b(z) f_c(z) times a strictly nonzero normalization factor. All three polynomials are nonzero; the polynomial ring C[z1,...,zm] is an integral domain. The product cannot vanish on the entire m-torus of phases, where the static Cauchy measure has strictly positive joint density. Thus NO nonzero product ket across the three multi-qubit labs lies in the kernel of ρ_A^{⊗m}; no separable positive B-certificate can exist for ANY FINITE m.

**Quantifier is essential:** this theorem does NOT cover m shots with a common ξ across shots, nor correlated redraws, nor nonlocal quantum communication. In the independent-block regime the unrestricted global B-only success on m blocks is

p^{global}_{B-only,m}=1−[(1+x²)/2]^m,

by measuring the orthogonal complement of S^{⊗m}. LOCC remains unable to produce any finite-m event with ZERO false A probability, although ordinary finite-error classification may be successful.

## 4. Theorem R14.4 — source reset produces an EXACT two-run local SWAP-test bifurcation

Take TWO whole runs of identical duration Δ, with one output qubit from each run kept in the SAME laboratory. The laboratory performs the antisymmetric local two-qubit test Π_-=(I−SWAP)/2; this operation is LOCAL relative to the three-laboratory partition even though it is jointly entangling within one lab.

**Model A_same:** a SINGLE ξ persists across both complete runs. Conditioned on ξ, the two local qubits are |u(z)>⊗|u(z)>; the antisymmetric projector annihilates them for every ξ, so p_-(A_same)=0.

**Model A_fresh:** before EACH run an independent ξ is drawn. A single laboratory's two qubits are in ρ_1⊗ρ_1, so p_-(A_fresh)=(1−Trρ_1²)/2=(1−x²)/4.

**Model B_independent:** for independent Lévy increments between runs the local two-qubit state is also ρ_1⊗ρ_1 and p_-(B)=(1−x²)/4.

Consequently

p_-(A_same)=0 < p_-(B)=(1−x²)/4=p_-(A_fresh).

For q=1/3, B-only LOCAL conclusive probability under A_same is 0.121645720241852 per pair of runs. The identical local test does NOT distinguish A_fresh from B. This is the precise source-typing answer to why R14.3 cannot be applied when one ξ persists across blocks. It also does not assert that the whole A_fresh and B hypotheses are indistinguishable by more informative three-qubit measurements—their cross-lab joint states are distinguishable (PRF11/R04). Only the local two-copy antisymmetry statistic coincides.

## 5. R13 kernel bridge is algebraically valid but informationally sterile on its diagonal segment

For auxiliary orthogonal σ_P=P/2 and σ_Q=Q/4, P positive and Q negative support of R04, let F_r=diag(1,r)^{⊗3}. Then exactly

Tr(F_r σ_P)=Tr(F_r σ_Q)=(r+r²)/2.

This filter does not alter the likelihood ratio at all, and its probability under EITHER hypothesis tends to zero as r→0. At r=0 F=|000><000| lies in the common kernel; R13's continuous extension to a negative product ray exists as operator geometry but is NOT itself an LOCC protocol. The failure of the necessary no-product-vector precondition in Kleinmann–Kampermann–Bruß (2011), Proposition 1, is explicit: ker σ_P ∩ ker σ_Q=K contains |000> and |111>. Projecting to P⊕Q first would be nonlocal and would silently change the LOCC task.

Extra exact nonlinear identity: for a strictly positive Hermitian local H=[[a,z],[conj(z),b]],

Tr(H^{⊗3}σ_P)=(a+b)(ab/2+|z|²),
Tr(H^{⊗3}σ_Q)=(a+b)(ab−|z|²)/2,

so the likelihood contrast equals (3/2)(a+b)|z|². Diagonal H has zero contrast; the offdiagonal coherence appears only quadratically. This is an EXACT source-pair identity, not a protocol/POVM implementation or a quantitative LOCC no-go.

## 6. Multiple independent copies: exponential approximate success DOES coexist with finite-m unambiguous impossibility

For the auxiliary pair σ_P,σ_Q, measure local X independently on all three qubits. Two outcomes (+++),(---) occur with total probability 3/4 under P and 0 under Q. The other six outcomes have per-outcome probabilities 1/24 under P and 1/6 under Q. On m independent copies, the classical Bayes decision is P iff at least one all-aligned outcome appears, Q otherwise. Exactly

p_err^{(m),X}(σ_P,σ_Q)= (1/2)4^{-m}.

This is the optimum FOR THIS FIXED X-TRANSCRIPT, not for arbitrary cross-copy LOCC or global operations. Eg m=1,2,3,5 give 1/8,1/32,1/128,1/2048. The COPY asymptotic reaches zero, while the SINGLE-COPY arbitrarily-many-ROUNDS asymptotic remains OPEN.

One-shot **two-sided unambiguous auxiliary** LOCC also exists: choose local X bases with prob λ and locally rotated trine bases (phases 0,2π/3,4π/3) with prob 1−λ. In the X setup, aligned signs herald P with probability 3/4 under P and 0 under Q; in the trine setup, aligned signs herald Q with probability 3/8 under Q and 0 under P. Choosing λ=1/3 balances both conclusive probabilities to 1/4, producing a classical erasure channel with erasure 3/4 for either class. This applies to the artificial σ_P/σ_Q pair—not to physical original ρ_A/ρ_B, because the latter has nonzero weight in kernel K.

For ORIGINAL A_fresh vs B with independently reset complete blocks, all-X measurement on each block has four Hamming-weight classes k=0,1,2,3 with multiplicities C(3,k). Denote x=e^{-q}. Per-individual-outcome probabilities:

A_k = [(1+x)(x²+5x+10), (1−x²)(2+x), (1−x²)(2−x), (1−x)(x²−5x+10)]_k /32,
B_k = [(1+x)^3, (1−x)(1+x)^2, (1−x)^2(1+x), (1−x)^3]_k /8.

Because A_k != B_k for q>0, Bhattacharyya coefficient C(q)=Σ_{k=0}^3 C(3,k) sqrt(A_k B_k) is STRICTLY less than one. On m independently **re-drawn** whole blocks, classical minimum error under X measurement has standard upper bound

p_err^{(m),X}(ρ_A,ρ_B) <= (1/2) [C(q)]^m.

Numerical q=1/3 gives C=0.9566684243079806. This only proves asymptotic statistical consistency with growing number of independent blocks; it is NOT the LOCC closure question on a SINGLE block. It FAILS as an iid assertion if A holds one common ξ across the whole repeated sequence. R14.4 handles that distinct contract separately.

## 7. Reproducibility, falsifiers and honest closure status

Self-contained Python 3 + NumPy + SymPy code: `IW_PRF12_R14_KERNEL_HERALD_AND_MULTICOPY_REPRO_001_20261028.py` in the same directory. Checks exactly: P/Q matrices, diagonal kernel-filter identity, full symbolic H^{⊗3} contrast, 8 local X outcomes, aligned trine herald under auxiliary pair, exact m-copy classical error for m=1..6, complete original-source X probability polynomials, positivity/normalization, Qρ_A=0 and Tr(Qρ_B)=(1−x²)/2, ρ_A rank4 and ρ_B rank8 for q=.05,1/3,1,3, and the 2-shot local antisymmetric source-reset dichotomy. Symbolic multiaffine integral-domain proof is in §3; code prints but does not pretend numerical sampling proves it.

**Independent referee priorities:** check the scope of the unit-circle orbit of static Cauchy, the polynomial proof for arbitrary m LOCAL entangled vectors, the true positive-definite support on Sym³, the local two-output SWAP measurement assumption, and the irrelevance of Kleinmann Prop.1 because K contains product vectors. Most important: do NOT replace R14's finite-m *unambiguous* no-go with a positive single-copy asymptotic *minimum-error* LOCC gap; the latter is still not proved.

**Status:** `EXACT_SOURCE_SUPPORT / GLOBAL_B_ONLY_OPTIMUM / ANY_FINITE_FRESH_BLOCK_SEPARABLE_UNAMBIGUOUS_NO_GO / TWO_RUN_COMMON_XI_LOCAL_ANTISYMMETRIC_WITNESS / AUX_M_COPY_X_ERROR_EXACT / SOURCE_RESET_CRITICAL / LOCAL_SYMBOLIC_AND_NUMERIC_REPRO_PASS / INDEPENDENT_REFEREE_PENDING / NO_FULL_LOCC_CLOSURE_GAP / NO_NOVELTY / NO_CANON / NO_EXEC / GITHUB_PENDING_BW_INGEST`.

## Subsequent owner result — PRF12 R15 (2026-10-28)

R15 strengthens the R14 **single-laboratory, two-run** antisymmetric B-only witness into an **EXACT optimal SEP and three-lab LOCC B-only herald** for any fixed known partition of runs into hidden-Xi-sharing reset groups. For group sizes m_j, set h_m=sum_{k=0}^m p_+^{m-k}p_-^k, p_+=(1+e^{-q})/2, p_-=(1-e^{-q})/2. Then optimum one-sided unambiguous conditional success under B is 1-(product_j h_mj)^3 for LOCC/SEP and 1-product_j h_(3*mj) for GLOBAL. Proof uses multivariate polynomial integral-domain factorization and includes arbitrary fine-grained separable leaves; it does not infer single-copy LOCC Helstrom closure non-approximability. At q=1/3, one shared Xi for two runs: three-lab LOCC optimum 0.322344191560 vs R14 one-lab witness 0.121645720242, and global 0.521242588284. Source: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-28/IW_PRF12_R15_OPTIMAL_LOCC_HERALD_UNDER_PARTIAL_SOURCE_RESET_001_20261028.md . Reviewer pending, no canon/EXEC, BW ingestion pending.
