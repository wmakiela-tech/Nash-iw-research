---
artifact_id: IW_PRF11_R29_CONTINUOUS_SEMIGROUP_PROCESS_ECHO_AND_QUOTIENT_CONTRACT_001_20261024
created_at: 2026-10-24
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_10 / PRF11
problem_id: LT4_MONOGRAPH_CH7_7_2_CONTINUOUS_TIME_PROCESS_ARITY_AND_INTERVENTION_FACTORING_GATE
function: SCIENCE_FIRST / SOURCE_TYPED_MATURE_HOST_SUBTRACTION / INDEPENDENT_FALSIFIER / NEGATIVE_KNOWLEDGE_PRESERVING
exposure: PUBLIC_SAFE
document_type: EXACT_CLASSICAL_PROCESS_TENSOR_NONMAP_AND_POSITIVE_GLOBAL_QUOTIENT_CONTRACT
status: MATHEMATICAL_DERIVATION_PLUS_SOURCE_LITERATURE_AND_COMPUTATIONAL_CONTROLS_PASS / INDEPENDENT_REFEREE_PENDING
bw_event_or_pending: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_HARDWARE / NO_ORIGINAL_RUNTIME
---

# PRF11 R29 — Continuously CP-divisible qubit semigroups do not identify multitime processes, but a globally compatible quotient **does** preserve their allowed intervention histories

**Date: 24 October 2026.** Source-typed exact conditional mathematics for a qubit under ideal classical dephasing noise; a classical positive theorem for reductions and instruments. Mature process-tensor, static-disorder and echo hosts. This result is **NOT a new quantum theory**, experimental realization, claim about NCDG/GR or assertion that any historically proposed global quotient is physically realizable.

## 0. Others first, currentness and the outstanding scope seam

**Native monograph REV020 read in full**, Google Doc `1cn97_kO65BcJRRWQrvrL9fKlEYBT3PHg6BJItn1Q4FQ`, readable text 159,536 characters in prior R28 and read again before R29. Original §7.2 states: from global intertwining `rU_t=V_t r` for full evolution and surjective r, a reduced semigroup follows, but "nie wynika stąd ... równoważność procesów z interwencjami". These assertions need separate contracts. Original Chapter 5 Theorem 5.3 and §5.5a offer a **two-time, finite-step** witness, not a continuously parameterized all-time matched channel family.

The separate **NC** auditing line, notably NC ART007 and corrected **ART015**, explicitly said the two-time source witness cannot be used as an all-times/continuous-time proof merely by cross-reference. **PRF11 R28** audited the twelve NC nonmaps, left that §7.2 process-arity seam **SCOPE_PENDING**, and independently strengthened a different classical Markov chain witness §3.10. R29 does **not** repeat the NC Markov TV calculation. LT5 independently authors the native working REV021 and has not been asked to change text; REC9/REC10 remain external referees; moderator alone retains EXEC authority.

**Mature exact-host discovery is decisive:**

1. **Milz & Modi**, *Quantum Stochastic Processes and Quantum non-Markovian Phenomena*, PRX Quantum **2**, 030201 (2021), DOI [10.1103/PRXQuantum.2.030201](https://doi.org/10.1103/PRXQuantum.2.030201), in Sec. VI.A.2 describes a **"shallow pocket"** single-qubit process with a Lorentzian environment, exponentially decaying CP-divisible single-time dynamics but memory visible only after a σ_x intermediate instrument (spin echo), despite unchanged time-marginal channels. **This directly hosts the underlying phenomenon, before IW/NASH.** Exact primary journal full HTML inspected: https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.2.030201.
2. **Milz, Kim, Pollock & Modi**, *Completely Positive Divisibility Does Not Mean Markovianity*, PRL **123**, 040401 (2019), DOI [10.1103/PhysRevLett.123.040401](https://doi.org/10.1103/PhysRevLett.123.040401), already proves the conceptual divisibility-versus-process distinction. Primary publisher abstract inspected.
3. **Kropf, Gneiting & Buchleitner**, *Effective Dynamics of Disordered Quantum Systems*, PRX **6**, 031023 (2016), DOI [10.1103/PhysRevX.6.031023](https://doi.org/10.1103/PhysRevX.6.031023), explicitly analyzes the **Cauchy–Lorentz static spectral disorder -> exponential semigroup** mechanism and its generator. Primary publisher entry plus identified text examined.
4. Ancient and modern spin-echo / dynamical-decoupling host, e.g. Klauder–Anderson (1962), DOI 10.1103/PhysRev.125.912, addresses static/slow versus fluctuating environments. This is not a new physical proposal.

**Source-specific new *project-local* value:** a fully self-contained same-all-t family written in the source monograph's exact type vocabulary; complete arbitrary finite X-pulse timing law and its exact maximum; uniqueness of the static continuous-time semigroup source frequency distribution; and, most importantly, a **positive global-quotient/instrument theorem** exposing why the same witness CANNOT falsify stronger all-state autonomy.

## 1. Two precise competing process models and identical whole-time channel family

System `S=C²`, Pauli `Z=diag(1,-1)`, `X=[[0,1],[1,0]]`, `U_θ=exp(-i θ Z/2)`. Input is ANY density matrix `ρ`, initially independent of the classical noise. Fix `γ>0` with units inverse time. Noise is CLASSICAL, no inference of microscopic source or hardware.

**Process A — static spectral disorder.** Sample one `ξ` from centered Cauchy law on R with density

`p_γ(ξ) = γ / [π(ξ²+γ²)]`.

Hold the very same `ξ` fixed throughout *one complete experimental history*. On any interval `[u,v]`, the sample-level propagator is `U_[ξ(v-u)]`. Averages are performed over a single shared ξ across all intervals. The sample paths are continuous in t (for each finite ξ), but the ensemble of ξ has NO finite first moment.

**Process B — independent-increment classical phase.** Let `L_t` be a symmetric Cauchy Lévy process with `L_0=0`, independent increments, and `L_v-L_u ~ Cauchy(0,γ(v-u))`. On interval `[u,v]`, the sample-level propagator is `U_[L_v-L_u]`. This idealized process has càdlàg phase paths; it is not claimed to arise from a bounded finite-dimensional Hamiltonian or a finite-bandwidth device. Its average is a completely positive Markovian dephasing semigroup with fresh classical noise for each disjoint interval.

A Cauchy characteristic function has the EXACT formula

`E(exp(-i t ξ))=exp(-γ|t|)`,

and the Lévy increment characteristic function is `E(exp(-i(L_v-L_u)))=exp(-γ(v-u))` for `v>=u`. Since the qubit diagonal entries are fixed and its off-diagonal entries acquire phase `exp(-iθ)`, each process, with NO intermediary interventions, induces **the same CPTP linear map for ALL real times `t>=0` and ALL inputs ρ**:

`Φ_t(ρ) = ((1+e^(-γt))/2)ρ+((1-e^(-γt))/2) ZρZ`.   (1)

This is a Kraus form with nonnegative weights. Since `exp(-γ(t+s))=exp(-γt)exp(-γs)`, `Φ_(t+s)=Φ_t Φ_s`, `Φ_0=id`; finite-dimensional strong/norm continuity is immediate. Its GKSL generator, with no claim of averaged microscopic ξ, is

`𝓛(ρ)=(γ/2)(ZρZ−ρ)`; off-diagonal derivative is `-γρ_01`.   (2)

**Critical:** static A being a dephasing **channel semigroup** does not mean it is a Markovian **multitime instrument process**. Do not derive (2) by naive `Eξ`: the Cauchy first moment does not exist. Also don't confuse the time-continuity of the averaged channel with continuity of sample paths in B.

## 2. Explicit legal intermediate instrument and exact operational separation

Prepare `ρ=|+><+|`, `|+>=(|0>+|1>)/sqrt(2)`. At `t=s>0`, apply **the same deterministic unitary instrument `𝓧(ρ)=XρX`** (one-outcome CPTP) to the system in both experiments. At `t=2s`, apply the same KNOWN correction X and measure the Pauli-X `|+>` projector. Both pulses are system-local legal CPTP operations, not postselection or environment access.

Two pathwise operator identities are exact:

`U_a X U_a = X`, `X U_b X U_a = U_(a-b)`.                 (3)

For **static A**, both interval phases equal `a=b=ξs`; corrected final state is IDENTICALLY `ρ` for each individual ξ before any averaging.

For **fresh-noise B**, a and b are INDEPENDENT `Cauchy(0,γs)`, so `a-b ~ Cauchy(0,2γs)` and the corrected final ensemble state is `Φ_(2s)(ρ)`.

Therefore

`P_A(+)=1`, `P_B(+)=(1+e^(-2γs))/2`,                 (4)

and the total variation between the **two specified binary outcome distributions** is exactly

`TV(P_A,P_B)=[1-e^(-2γs)]/2 > 0`.                     (5)

Moreover for this FIXED echoed and corrected interface, trace distance between the two final qubit channels' outputs obeys

`(1/2)||ρ_A−ρ_B||_1 =[(1-e^(-2γs))/2] sqrt(x²+y²) <=(1-e^(-2γs))/2`,

where (x,y,z) is the Bloch vector of the arbitrary input. The value (5) is thus **attained and optimal over input qubit states and terminal two-outcome POVMs for THIS specified echo instrument**, not claimed to optimize over every possible multitime intervention.

Numerical example γ=0.7, s=1 (T=2): `e^-1.4=0.2465969639416065`, `P_A(+)=1`, `P_B(+)=0.6232984819708033`, `TV=0.37670151802919677`. **The uninterrupted channels are identical for all t despite different intervened statistics at 2s.** All times are physical model clock times, not merely shot index.

## 3. Exact law for ANY finite ideal X-pulse train

Let `0=t_0<t_1<...<t_m=T`, intervals `Δ_j=t_j−t_(j−1)>0`. Insert a unitary X between every two successive intervals, and correct the known product of X pulses at T (the common final correction changes neither model's distinguishability nor their type). The toggling signs are `σ_j=(-1)^(j−1)`. Define signed exposure

`A=Σ_(j=1)^m σ_j Δ_j` with `|A|<=T=ΣΔ_j`.

By repeatedly applying the anticommutation relation `XU_θX=U_(-θ)`, the corrected total random dephasing phase is:

- static A: `Ξ_A=ξ A`; characteristic at unity `χ_A=exp(-γ|A|)`;
- fresh independent B: `Ξ_B=Σ σ_j (L_(t_j)-L_(t_(j-1)))`; Cauchy stability and independent increments give `χ_B=prod_j exp(-γΔ_j)=exp(-γ T)`.

Thus **for all finite pulse schedules**, with the same initial |+> and a terminal `|+>` test,

`TV_pulse(Δ_1,...,Δ_m) = (exp(-γ|A|)-exp(-γT))/2`.   (6)

Both models have identical FREE-INDUCTION channels (1), yet all pulse histories are explicitly determined by their different temporal noise laws. With γ>0 and both toggling parities present, `|A|<T` and hence TV>0.

At fixed T and γ, equation (6) yields the EXACT within-class upper and its attainment:

`0<=TV_pulse <= [1-exp(-γT)]/2`, with equality iff `A=0`. (7)

For a single intermediate pulse, this means `t_1=T/2`: the Hahn spin-echo midpoint timing. This is **a classical filter-function and Cauchy-stability corollary**, not a new control-theoretic discovery or optimization over arbitrary adaptive quantum instruments. Source scope: centered scalar classical static spectral disorder vs independent symmetric Cauchy increments; the theorem cannot be transferred to arbitrary environmental Hamiltonians, Gaussian quasistatic noise with the SAME semigroup (it would not be the same), or actual unknown experimental noise.

## 4. The Cauchy distribution is the ONLY static frequency law with a nontrivial strongly continuous dephasing semigroup on all t

**Bounded theorem with elementary proof (mature Fourier characteristic-function host).** Let ξ have ANY probability distribution μ on R; define the one-time static-frequency qubit channel `Φ_t=E[Ad_U_(ξt)]` for t>=0. Assume EXACT semigroup law `Φ_(t+s)=Φ_tΦ_s` for all s,t>=0 (and the automatic weak continuity inherited from characteristic functions). Write `χ(t)=E[e^(-iξt)]`.

The channel semigroup is equivalent to `χ(t+s)=χ(t)χ(s)` and χ(0)=1. Continuity makes χ(t) nonzero for every t>=0: if χ(t0)=0 then `χ(t0/n)^n=0`, contradicting χ(t0/n)→1. By the continuous multiplicative Cauchy equation on R+, `χ(t)=exp(ct)` for t>=0 with `Re c<=0` (bounded characteristic functions have |χ|<=1). Write `c=−γ−iω`, γ>=0, ω∈R. The characteristic symmetry `χ(−t)=overline{χ(t)}` yields

`χ(t)=exp(−γ|t|−iωt)` for ALL real t.          (8)

Uniqueness of Fourier characteristic transforms forces μ to be **Cauchy(location ω, scale γ)** if γ>0, or a Dirac point mass at ω if γ=0. Conversely every such law has (8) and forms the dephasing semigroup. **This is exactly the Cauchy/Lorentzian mature static-disorder mechanism of Kropf–Gneiting–Buchleitner (2016), not a NASH novelty or property of all noncommutative multi-generator disorders.**

Falsifier: for a nondegenerate STATIC Gaussian ξ~N(0,σ²), χ(t)=exp(−σ² t²/2), so χ(2t) !=χ(t)^2 for t,σ>0. The uniqueness theorem is not asserting all static noise is Markovian.

## 5. NONMAP type trap — the apparently stronger global quotient is NOT falsified

This distinction is material for the source monograph's **literal §7.2** condition. For a FULL state space X and reduced Y, assume the **strong all-state** operator equalities

`r U_t=V_t r` for EVERY x∈X and all t>=0,                  (9)

with r a surjective state reduction, U_t full semigroup, V_t reduced semigroup. For each **allowed full instrument outcome map** `I_a:X→X` assume a REDUCED counterpart `i_a:Y→Y` obeying

`r I_a = i_a r` on ALL of X.                             (10)

Include a common positive normalization functional for branch probabilities satisfying `tr_Y∘r=tr_X` on subnormalized states, or in classical language a probability-mass functional preserved by r.

Then for ANY finite time grid and ANY allowed sequence of instruments (including adaptive choices whose outcomes have been fixed along each branch), induction gives EXACT unnormalized reduced branch states

`r U_(Δ_m) I_(a_(m-1)) U_(Δ_(m-1)) ... I_(a_1) U_(Δ_1) x
 = V_(Δ_m) i_(a_(m-1)) V_(Δ_(m-1)) ... i_(a_1) V_(Δ_1) r x`.  (11)

Applying the common mass functional shows that ALL corresponding outcome-history probabilities agree, not just one-time marginals. This is an **elementary positive transfer theorem** and covers quantum **linear CP trace-nonincreasing** maps with r=partial trace when (9) and (10) really hold. No proof of physical realizability of U,V,I is supplied by mere algebra; it is a conditional result.

**Consequences for monograph §7.2:**
- It is UNSAFE to read the sentence “rU_t=V_t r does not imply process equivalence” as a universal counterexample to (9)+(10); that reading is wrong, by (11).
- It is SAFE to say that an *abstract quotient semigroup (9) alone*, without declared admissible interventions and their intertwining, does not **specify or automatically compare arbitrary intervention experiments**.
- It is SAFE and operationally nontrivial to say that equality **only of the prepared initial-system dynamical maps** `Φ_t` for every t, even a strongly continuous CPTP semigroup, does NOT identify the unprepared/full correlated environmental evolution or the multitime process. The static Cauchy / Lévy witness proves THIS weaker assertion.

**Why static disorder does not secretly obey (9):** choose two different full-system classical preparations with the SAME qubit density matrix but different full environment distributions (or just two different fixed frequencies ξ₁,ξ₂). At any generic t, their reduced outputs have different unitary phase. Thus reduction `r=forget ξ` does not intertwine full joint dynamics with a single V_t over the entire full state set. The averaged Φ_t exists only for the specified initial independent Cauchy distribution. The no-go witness DOES NOT test the stronger universal quotient. This distinction is the core epistemic correction.

A one-line negative control for (10): `r(x1,x2)=x1` and a full linear intervention `I(x1,x2)=(x1+x2,x2)` cannot factor to any reduced function i on x1, because rI(0,0)=0 but rI(0,1)=1. Contrarily diagonal compatible interventions and block-diagonal full semigroups obey (11). Do not mislabel this elementary linear example as a physical CPTP quantum instrument.

**Suggested TYPE-REPAIR FOR THE AUTHORS (not an authorial document edit):**
> Sama równość kanałów zredukowanych Φ_t dla określonego przygotowania — nawet dla wszystkich t i przy prawie półgrupy CPTP — nie wyznacza statystyk eksperymentów z interwencjami. Natomiast globalne splatanie rU_t=V_t r i zgodność rI_a=i_a r dla całej dopuszczalnej rodziny instrumentów gwarantują równoważność historii w tej rodzinie. Bez wyszczególnienia klasy interwencji sam warunek autonomii nie jest twierdzeniem o pełnej równoważności dowolnych procesów. [Tu wskazać jako istniejący gospodarz Milz–Modi 2021, §VI.A.2 i Ch5 źródłowe przykład.]

This repair addresses ONLY §7.2's process clause. NC ART014's separate spatial-continuity witness remains intact; the bare-set CP phrase remains untyped unless an operator-system structure is declared. No artificial claim that every global quotient is CP.

## 6. Actually executed symbolic/numerical verification

Source: standalone Python file `prf11_r29_continuous_process_semigroup_echo.py`, NumPy/SciPy/SymPy, machine-readable `prf11_r29_results.json`. **Independent of all NC scripts**; no original DTC/source hardware runner involved.

1. **Symbolic:** exact 2×2 identity `U_a X U_a=X` and `X U_b X U_a=U_(a-b)` checked in SymPy. PASS.
2. **Continuous channel:** 12 semigroup-composition checks for γ∈{0,.2,.7,1.3} and nontrivial pairs (s,t); errors <1e−14. Correct 2×2 Kraus implementation independent of stochastic Monte Carlo. PASS.
3. **Pulse trains:** 18 different exact interval-pattern evaluations for γ∈{.3,.7,1.3}, with signed exposure and fixed-T upper (6)-(7). PASS.
4. **Operational endpoint:** 12 independent density-matrix trace-distance and projector-probability comparisons at γ∈{.3,.7,1.3}, s∈{.1,.5,1,2}; exact TV (5), <1e−14 mismatch. PASS.
5. **Optimization:** for γ=.3,.7,1.3 and three T, fixed-T 1001-point split grids attain the predicted bound precisely at midpoint. PASS; optimization proof analytic, grid not a replacement.
6. **Stochastic falsifier:** 250,000 fresh Cauchy samples per scenario; 4 separate echo/free-induction comparisons with common-static-frequency versus independent increments. Maximum absolute echo-coherence MC residual was 0.0019 vs exact, predeclared acceptance 0.012. PASS. Three multisegment MC scenarios further validate `exp(-γ|signed|)` vs `exp(-γ T)` within 0.012. These Monte Carlo diagnostics DO NOT establish exact Cauchy characteristic functions.
7. **Negative distribution control:** static Gaussian with σ=.7 fails its purported semigroup by >0.1 at t=s=1. PASS, so the code does not mechanically declare all static noise Markovian.
8. **Positive quotient control:** 100 independent finite-dimensional diagonal semigroup + factoring-intervention composition checks, error <1e−12; explicit nonfactoring full intervention has same r-input but different r-output. PASS. This supports the **typed induction** but is not a proof for general infinite-dimensional quantum processes.

The explicit code is in the attached reproducibility package; execution output and all numeric scenarios in machine-readable JSON. Bounded scientific report text remains fully independent of a computation's machine platform; clean-room package reexecution is required before claiming reproduction.

## 7. Prior-art subtraction and stopping boundary

- **Milz & Modi 2021** already have essentially THE operational spin-echo/divisible-but-non-Markovian process model; PRF R29 cannot claim discovery. Their example has an explicit Lorentzian bath, whereas our paired presentation compares that static source to independently refreshed *symmetric Cauchy increments*, making the reference process and arbitrary pulse schedules transparent. This is a **pedagogical source-matched representation**, not a new physical mechanism.
- **Kropf et al. 2016** already identify Cauchy spectral disorder as the static source of exponential semigroup dephasing; our uniqueness proof applies the standard continuous multiplicative functional equation + uniqueness of characteristic functions.
- **Milz et al. 2019** expressly show CP divisibility does not imply Markovianity of the quantum process tensor; priority there.
- **NC, LT4/LT5** own earlier chapter formulation, two-time finite SWAP control, §7.2 warning, and error corrections. PRF11 owns only THIS bounded inferential clarification, not a new monograph version.

**Earned:** an explicit strongly continuous all-time CPTP equal-channel witness with quantitatively different intervention histories; general finite π-X schedule law and optimal balanced exposure within the declared family; exact static-frequency semigroup Cauchy characterization; strong all-state quotient + compatible-instrument positive transfer theorem; testable negative guards. **Not earned:** any novelty priority, independent owner review, BW ingest, general quantum implementation, finite-bandwidth physics, arbitrary process operator classification, full all-instruments optimality, violation of global state quotient, J3/K, GR or claims about historical datasets.

`NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE / NO_NEW_TASK / INDEPENDENT_REFEREE_PENDING / BW_PENDING`.