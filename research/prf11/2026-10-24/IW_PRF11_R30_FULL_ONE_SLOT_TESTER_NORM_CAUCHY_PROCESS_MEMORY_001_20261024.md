---
artifact_id: IW_PRF11_R30_FULL_ONE_SLOT_TESTER_NORM_CAUCHY_PROCESS_MEMORY_001_20261024
created_at: 2026-10-24
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_10 / PRF11
problem_id: LT4_CH7_PROCESS_VS_SEMIGROUP_FULL_ONE_SLOT_INTERVENTION_TESTER_NORM
exposure: PUBLIC_SAFE
canonical_body_path: research/prf11/2026-10-24/IW_PRF11_R30_FULL_ONE_SLOT_TESTER_NORM_CAUCHY_PROCESS_MEMORY_001_20261024.md
source_revision: resolve from GitHub commit after completed write
bw_event_or_pending: GITHUB_PENDING_BW_INGEST
function: SOURCE_FIRST / OTHERS_FIRST / FALSIFICATION_FIRST / MATURE_HOST_SUBTRACTION / TARGET_RELATIVE_TESTER
status: ANALYTIC_ONE_SLOT_PROOF_PLUS_INDEPENDENT_NUMERIC_CONTROL / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE / NO_UNRESTRICTED_MULTISLOT_CLAIM / NO_NEW_OWNER_TASK
---

# PRF11 R30 — Exact one-slot quantum tester norm for two indistinguishable dephasing semigroups

**Date 2026-10-24.** Nonblind functional continuation of PRF11 R29 and REC10 ROT29; model-specific mathematical tightening. **Neither the phenomenon of CP-divisible non-Markovian processes nor comb/tester distinguishability is a new result of IW/NASH.** All claims concern an exactly specified mathematical qubit noise model with one active intermediate time, not a calibrated physical device or new quantum gravity.

## 0. Currentness, attribution and STOP

Read source [PRF11 R29](https://github.com/wmakiela-tech/Nash-iw-research/blob/3199a28e2fff9f6f4a1a262f0d0708d81ba97145/research/prf11/2026-10-24/IW_PRF11_R29_CONTINUOUS_SEMIGROUP_PROCESS_ECHO_AND_QUOTIENT_CONTRACT_001_20261024.md), [REC10 ROT29](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/rec10/2026-10-24/IW_REC10_ROT29_PRF11_CONTINUOUS_PROCESS_ECHO_DIAMOND_TIMING_REFEREE_20261024.md) and [LT5 ROT18](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/2026-10-24/lt5_rev021_rot18_global_quotient_process_arity_source_event_and_target_identifiability_001.md) BEFORE derivation. REC10 independently refereed R29 with `PASS_WITH_SHARP_DIAMOND_AND_TIMING_GUARD` and proved `||D_u−D_v||_diamond=u−v` for a **FIXED** ideal X-pulse schedule plus exact timing tolerance; LT5 genuinely integrated the typed semigroup/intervention distinction into native working REV021, with source REV020 unaffected. PRF11 R30 does not reclaim their work.

Mature external hosts inspected:
- Simon Milz and Kavan Modi, *Quantum Stochastic Processes and Quantum non-Markovian Phenomena*, PRX Quantum **2**, 030201 (2021), DOI [10.1103/PRXQuantum.2.030201](https://doi.org/10.1103/PRXQuantum.2.030201), especially shallow-pocket/dephasing model and the need for intervention-based criteria.
- Guilherme Zambon, *Process tensor distinguishability measures*, Physical Review A **110**, 042210 (2024), DOI [10.1103/PhysRevA.110.042210](https://doi.org/10.1103/PhysRevA.110.042210). Generalized comb divergences and physically meaningful tester optimizations are mature; a bare Choi-state distance is NOT automatically the full operational distance.
- Paulina Lewandowska, Łukasz Pawela, Zbigniew Puchała, *Strategies for single-shot discrimination of process matrices*, Scientific Reports **13**, 3046 (2023), DOI [10.1038/s41598-023-30191-0](https://doi.org/10.1038/s41598-023-30191-0), established comb tester/strategy framework.
- Prior NC and LT5 monograph bridge: [NC ART015](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-18/IW_NC_KOREKTY_PO_AUDYTACH_INT7_REC9_015_20261019.md) corrects two-time-vs-continuous-time inference; R29 previously established global quotient+instrument positive theorem; R30 does not attack it.

Scientific question left by REC10: is intermediate X actually optimal when a tester can use a **general** CP instrument on the qubit, record outcomes, entangle the input with quantum memory, act JOINTLY on system+memory at the intermediate time, and measure everything jointly at the end? This is strictly stronger than fixed-X channel diamond norm, but strictly weaker than unrestricted multitime (multiple distinct intervention slots) process norm.

## 1. Process carriers and resource contract

S=C² with Pauli Z=diag(1,-1), X=|0><1|+|1><0|. One experiment at times 0,s,s+t, s,t>0. Environment is prepared independently of tester input and is never directly accessible. Two alternatives:

**A (static disorder):** One frequency ξ~Cauchy(0,γ) is sampled ONCE for the whole run; over interval u, the phase unitary is exp[-i ξuZ/2]. A tester intervention acts on S and its *own* quantum memory, never on ξ.

**B (independent increments):** The phase process has independent Cauchy increments, scale γu in length u. Unitary random phases on successive intervals are independent; same one-interval channel.

Both have for all u>=0 and for every qubit density matrix rho the same CPTP dephasing semigroup

    Phi_u(rho) = D_{exp(-gamma*u)}(rho)
               = ((1+exp(-gamma*u))/2)*rho
                 + ((1-exp(-gamma*u))/2)*Z rho Z.

The R29 one-slot nonmap uses two s=t intervals and intermediate X. This is a claim on reduced channels under a FIXED preparation, not global factorization on every full S+environment state.

**Allowed tester:** choose ANY finite memory Hilbert space R and initial state rho_SR (arbitrarily entangled), independent of ξ; allow a single intervention at time s given by any instrument `{I_a}` on S⊗R, branches completely positive and trace-nonincreasing, sum trace preserving. Kraus operators `K_{aµ}:S⊗R→S⊗R'_a` may change the memory dimension. Record the outcome a as a classical orthogonal flag. Finally, after the second noisy interval of length t, use ANY outcome-dependent joint quantum measurement on S⊗R'_a. All test operations must be the SAME under A and B; they cannot directly consult ξ or an environment record. No conditioning on a rare postselection success to redefine the prior/payoff. A single slot means one time s, though arbitrary operations can be part of the instrument at that time.

Define the **operational output trace-norm strategy distinguishability** with NO factor 1/2:

    D_1slot(s,t) = sup_{rho_SR, {I_a}} Σ_a ||sigma^A_a−sigma^B_a||_1,

where sigma_a are unnormalized output branch states before terminal measurement, so sum_a tr(sigma_a)=1 for both models. For equiprobable alternatives, classical maximum-TV of final outcome laws equals D_1slot/2 and Helstrom success equals 1/2+D_1slot/4. This explicit normalization removes terminology ambiguity; no claim is made about another author's different convention for normalized process-comb norms.

## 2. Theorem R30.1 — exact unrestricted **one-slot** operational distance

**THEOREM.** For γ>0 and s,t>0, in the above FULL allowed tester class (including quantum memory and a joint intermediate instrument),

    D_1slot(s,t) = δ(s,t)
                := exp[−γ|s−t|]−exp[−γ(s+t)].                     (30.1)

The supremum is ATTAINED by the simplest tester: choose R one-dimensional, prepare |+>, apply the deterministic bit flip X at s, and perform an appropriate final X-basis measurement. Neither a stored entangled quantum memory, an outcome flag, nor a joint intermediate memory interaction can improve the ONE-SLOT distinguishing advantage beyond this value. In particular

    P_success,opt = 1/2 + δ(s,t)/4,
    TV_terminal,opt = δ(s,t)/2.                                  (30.2)

At fixed T=s+t, the unique interior optimum timing is s=t=T/2, yielding δ_max=1−exp(−γT). At either s=0 or t=0, δ=0 (by continuous extension). These equal-time statements also follow from REC10's ideal-X witness; **new** is the UPPER bound over *all allowed one-slot quantum testers*.

### Proof step 1 — all 16 coefficient pairs, only opposite coherence survives

Let z_0=+1,z_1=−1. For input matrix unit E_ij and output unit E_kl, define a=(z_i−z_j)/2 and b=(z_k−z_l)/2 in {-1,0,1}. The static disorder coefficient is E[e^{-i ξ(sa+tb)}]=exp[−γ|sa+tb|]; independent increment coefficient exp[−γ(s|a|+t|b|)]. Their difference vanishes unless a=-b=+/-1, in which case it equals δ(s,t). Thus the two models differ ONLY when an intermediate intervention converts the input qubit coherence E_01 into the output E_10 or vice versa. Diagonal input/output and sign-preserving coherence are indistinguishable between models under this two-interval observation contract.

### Proof step 2 — exact block form with arbitrary quantum memory and classical flags

Write the arbitrary input state in the qubit Z basis, with operator-valued memory blocks:

    rho_SR = [[A, B], [B†, D]],

A,D>=0, tr(A)+tr(D)=1. For each outcome a and Kraus index µ decompose the INTERVENTION block operators (mapping R→R'_a):

    U_{aµ} = <1|K_{aµ}|0>,
    V_{aµ} = <0|K_{aµ}|1>.

Let the cross-coherence conversion map on the memory be

    T_a(B) = Σ_µ U_{aµ} B V_{aµ}†.

The unnormalized BRANCH output difference between process A and process B is then exactly

    sigma^A_a−sigma^B_a
       = δ(s,t) * [[0, T_a(B)†], [T_a(B), 0]],                  (30.3)

in the final system qubit blocks. Each difference has trace zero. For a matrix [[0,T†],[T,0]], its trace norm is 2||T||_1. Since flags a are mutually orthogonal,

    Σ_a ||sigma^A_a−sigma^B_a||_1
        = 2δ(s,t) Σ_a ||T_a(B)||_1.                           (30.4)

This equation is exact even when the tester's initial S and R were ENTANGLED, even when the instrument couples S and R, and even when the outcome-dependent output-memory spaces differ.

### Proof step 3 — two-sided Kraus column contraction and positive block bound

The joint instrument is complete: `Σ_{aµ} K_{aµ}†K_{aµ}=I_{S⊗R}`. Taking its input-(S=0) and input-(S=1) diagonal compressions gives

    Σ_{aµ} U_{aµ}†U_{aµ} <= I_R,
    Σ_{aµ} V_{aµ}†V_{aµ} <= I_R.                               (30.5)

For every trace-class B and all finitely many outcomes a, **two-sided trace-ideal Cauchy–Schwarz** yields

    Σ_a ||Σ_µ U_{aµ} B V_{aµ}†||_1 <= ||B||_1.                (30.6)

Self-contained proof: choose dual test operators H_a on R'_a with ||H_a||_infty<=1. Then

    |Σ_a tr[H_a T_a(B)]|
      = |tr[(Σ_{aµ} V_{aµ}† H_a U_{aµ}) B]|
      <= ||Σ V† H U||_infty ||B||_1
      <= ||B||_1.

The last bound follows by forming tall block-column contractions U=(U_{aµ}) and V=(V_{aµ}), so `Σ V† H_a U=V† diag(H_a) U` with each operator factor norm<=1. Maximizing the real dual traces, including independent phase choices across outcomes, establishes (30.6).

Moreover positivity of rho_SR gives **||B||_1<=1/2**: for a pure state |ψ>=|0>⊗u+|1>⊗v, B=|u><v| and ||B||_1=||u||·||v||<=1/2; every mixed state is a convex combination of pure states and the trace norm is convex. Combining (30.4)-(30.6):

    Σ_a ||sigma^A_a−sigma^B_a||_1
      <= 2δ ||B||_1 <= δ.                                   (30.7)

This is an unconditional, uniform bound for every allowed tester, no finite-rank enumeration or SDP required.

### Proof step 4 — attainment and scope

Input rho_S=|+><+|, memory R=C, intermediate K=X. Then B=1/2, U=<1|X|0>=1, V=<0|X|1>=1, and T(B)=1/2. Hence branch trace distance from (30.4) is 2δ*(1/2)=δ, reaching (30.7). Final appropriate X-basis Helstrom measurement gives TV=δ/2. The theorem is proved.

**FIREWALL:** this is exactly a ONE-SLOT tester supremum for two specified processes. An instrument interacting directly with ξ, multiple intervention times, an additional feedforward slot in the second interval, time-dependent adaptive environment sensing, selective conditional comparison, or another noise law changes the test class, and (30.1) is NOT asserted for any of those. A global quotient compatible with all legal instruments remains process-preserving under R29's positive theorem; no contradiction.

## 3. Theorem R30.2 — a complete exact formula for arbitrary system-only flagged instruments

If an instrument acts on qubit S **only**, with Kraus K_{aµ}:C²→C², set

    b_a := Σ_µ (K_{aµ})_{10} overline[(K_{aµ})_{01}].

Then the flagged difference channel on the qubit is

    (D_A^I−D_B^I)_a(rho)
      = δ [ b_a rho_{01} E_{10} + conj(b_a) rho_{10} E_{01}].   (30.8)

For each branch the diamond norm of its Hermiticity-preserving linear map is exactly δ|b_a|: it is δ|b_a| times a phase-conjugated unitary bit flip composed with the offdiagonal projection `(id−Ad_Z)/2`, which has diamond norm 1, with lower bound already attained at |+>. Consequently for the channel outputting all classical flags,

    ||D_A^{I,flag}−D_B^{I,flag}||_diamond
      = δ Σ_a |b_a| <= δ.                                    (30.9)

(The general theorem above yields the upper bound, and |+> gives the exact lower bound simultaneously for ALL flag outcomes.) Forgetting the classical flag gives instead

    ||D_A^{I,unflag}−D_B^{I,unflag}||_diamond
      = δ |Σ_a b_a| <= δ Σ_a |b_a|.                            (30.10)

This is an exact **instrument-dependent** resource quantity: `Σ|b_a|` is the amount of coherence-sign inversion the chosen instrument can pass to the post-intervention interval, not a universal memory monotone. It is basis Z and one-slot-model typed. Formulae (30.9)-(30.10) do not generalize blindly to joint quantum-memory instruments, where b_a is not a scalar and (30.4) is the correct carrier.

### Flag loss witness — equal probabilities, total loss of distinguishing power

Take two outcomes with Kraus `K_0=X/√2`, `K_1=ZX/√2`, summing to a TP instrument. Then `b_0=1/2`, `b_1=−1/2`.

    Flag recorded:  ||D_A−D_B||diamond = δ(|b_0|+|b_1|)=δ.
    Flag discarded: ||D_A−D_B||diamond = δ|b_0+b_1|=0.

Both outcomes have probability 1/2 under EITHER model. Thus classical side information about which physically allowed intervention occurred can be essential, even though the same *unconditional* instrument mixture is completely blind to process memory. This is a sharp elementary source-typed witness, not a new memory physics discovery.

Other exact controls: `I` and Z-basis projective measurement have `b=0`; full `X` has |b|=1; the unitary `exp(−i(π/4)X)` has |b|=1/2, hence exactly half the allowed flagged distance.

## 4. Source-typed mature-host subtraction

The general *physical phenomenon* that one-time CPTP semigroups can arise from a non-Markovian multi-time process is mature Milz–Modi 2021 / shallow pocket and Cauchy dephasing; the idea of spin echo and dephasing correlation is mature. The **mathematical technique** is standard CP Kraus completeness, Schatten trace ideal duality, and tester/comb operational discrimination, see Zambon 2024 and Lewandowska–Pawela–Puchała 2023. REC10 ROT29 already proved the sharp diamond formula in the much narrower fixed deterministic pulse class and the precise timing budget. PRF11 R30 adds a **self-contained model-specific one-slot optimality proof** that admits arbitrary initial entangled memory, arbitrary joint system+memory intermediate instrument and classical outcomes, then reads out both systems. That extra quantifier is the earned project-local clarification; its mathematical priority relative to all process-norm literature has NOT been established.

An apparent "full quantum process norm" claim requires naming exactly how many time slots and what ancillary communication is allowed. The present norm is defined operationally in §1 to avoid illegitimate Choi/strategy/diamond norm identifications. **We did not optimize multiple distinct intervention times.**

## 5. Reproducibility and anti-self-sealing

**Pre-registration BEFORE S-only numerical tests**: `PRF11_R30_PREREG_20261024.md` (SHA256 `734902e8045988c1023c25390918dc094748976c472518a9895851f3eadf8fa8`), initially restricted to intermediate system-only instruments. It explicitly excluded general joint tester claims at first. S-only proof and controls suggested a **stronger** formula; the joint-memory case is thus an explicitly **NONBLIND extension** rather than a fake blind first-pass derivation.

**Second, honest extension prereg BEFORE joint numerical tests**: `PRF11_R30_EXTENSION_PREREG_20261024.md` (SHA256 `e69d08bfbc95de60d6481efa4cd39b014ef45b2da681e013beae95a62be3984b`). It freezes the stronger formula and test cases F8-F12, without claiming independence from the earlier derivation.

Executable programs, executed here independently of the PRF11 R29 and REC10 numerical scripts:

- `reproduce_prf11_r30_flagged_instrument.py` SHA256 `cb83b7ce08afba851b3d20bdd16333dd972ee9f6e1030fa93d82b2e31d6bb728`; 175 random source-legal qubit-only CPTP instruments, **1,536** direct random 2-interval characteristic-function versus cross-block operator checks (ancilla dimensions 1,2,3); maximum complex coefficient discrepancy `1.5516e-17`; max CP-completeness error `1.33e-15`; zero bound violations. The full selected X, X/ZX with flag and forgotten flag, X rotations and Z measurement exact controls all PASS. Distinct `flag_diamond` vs `unflag_diamond` values in attached JSON.
- `reproduce_prf11_r30_joint_tester_extension.py` SHA256 `7d4485685964311a8344aa8992f6fc29ccf10dcf27b800db7935938d3391e927`; **200** random TP joint qubit+memory instruments with memory input/output sizes 1–4 and 16 input/output-size pairs, **1,186** direct characteristic-function versus coherent-block checks on pure AND mixed joint states. Largest complex discrepancy `2.776e-17`; max TP residual `4.663e-15`; zero trace-norm bound violations; deterministic X and entangled Bell+X both attain `δ=0.7534030360583935`, while Bell+SWAP gives zero. These are not SDP calculations and do not replace the general proof.
- `prf11_r30_flagged_instrument_results.json` SHA256 `db2a62eff3a59fe9bf55a8c815ab48fd33bc0fa7f9fe4e103edf2133bfeb1db5`.
- `prf11_r30_joint_tester_results.json` SHA256 `88bb48f9ee514785aa56b67a9ae8a9bb5e6ded99a2d7cb3959b1c038989d170a`.

**One initial computational failure and repair are disclosed:** the FIRST joint test-script run tried to normalize stacked Ginibre Kraus matrices with insufficient total output rank when input memory dimension exceeded output support (e.g., d_in=4,d_out=1, only two Kraus); the Gram operator was singular, `L**-1/2` produced invalid floating values and asserted completeness failed. This was a *generator rank-contract bug*, NOT falsification of the theorem. The script was fixed to use 5/7/9/11 Kraus operators, guaranteeing enough stacked output rows; a separate explicit trace-preservation assertion then passed all 200 instruments. The prereg files were NOT edited.

The supplementary archive has independent SHA-256 manifest for all contained source code, the two immutable preregs, numeric outputs, and this report; clean extraction, recomputation and byte-identical JSON comparisons must be performed and logged **before** completion is claimed. GitHub source report publication does NOT by itself prove supplementary code was written to GitHub, nor BW ingestion. External independent referee remains pending for new universal one-slot optimality claim.

## 6. Immediate useful implications and exact boundaries

1. **Quantifier upgrade over REC10:** ancilla, intermediate quantum memory manipulation, general CP instruments, and adaptive outcome-flagged final POVMs do not improve a ONE-SLOT observation above the simple Hahn-echo witness for this exact source model.
2. **Type of intervention matters:** only `E01 → E10` and its conjugate are detectable at a fixed two-interval source law; an instrument with no coherence inversion cannot witness this specific process difference, even if it is a valid quantum instrument.
3. **Recording interventions matters:** distinguishability after discarding the outcome record may collapse to zero despite maximal flagged tester advantage. Thus 'instrument law with records' and 'unconditional CPTP map' are distinct observable contracts.
4. **Global quotient compatibility remains a positive theorem**, not a casualty of this counterexample. Microscopic state accessibility/ancilla legality and factorization of source-level instruments have to be stated separately.
5. **STOP:** no multi-intervention comb norm, environment access, hardware validation, physical NCDG/PBH result, canon promotion, mathematical priority or blanket instrument independent physical effect. These are explicit separate conjectural targets, not implicit conclusions.

**Status:** MATHEMATICAL_ANALYTIC_PASS / DIRECT_SOURCE_ALGEBRA_CONTROL_PASS / PREREG_SCOPE_PRESERVED / NONBLIND_EXTENSION_DISCLOSED / INDEPENDENT_REFEREE_PENDING / GITHUB_PENDING_BW_INGEST / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE / NO_NEW_OWNER_TASK.