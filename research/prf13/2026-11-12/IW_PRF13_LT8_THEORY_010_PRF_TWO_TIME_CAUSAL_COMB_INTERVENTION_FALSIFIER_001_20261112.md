---
artifact_id: IW_PRF13_LT8_THEORY_010_PRF_TWO_TIME_CAUSAL_COMB_INTERVENTION_FALSIFIER_001_20261112
created_at: 2026-11-12
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_12 / PRF13
parent_request: LT8-THEORY-010-PRF
source_type: EXACT_TWO_TIME_QUBIT_CAUSAL_COMB_COUNTERMODEL_WITH_PRIMARY_PRIOR_ART_SUBTRACTION
exposure: PUBLIC
sync_state: GITHUB_SOURCE_READBACK_PASS_BW_PENDING
status: AUTHOR_EXACT_REPRODUCED / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_NEW_PHYSICAL_THEORY / NO_FULL_LOCC / NO_HARDWARE / NO_CANON / NO_EXEC_SIGN / NO_UNRESTRICTED_CROSS_FIELD_BRIDGE
---

# PRF13 for LT8 ROT010 — A single CPTP endpoint channel is not a legal multi-time intervention quotient

**Assignment:** LT8-THEORY-010-PRF, supplied in public #iw-dispatch, 2026-11-12, inbound from Living Theory LT8. Adversarially test CIPIR (context-indexed predictive and interventional reduction) against legal two-time CP instruments / causal quantum combs / process tensors; construct the smallest source-typed exact witness available, and subtract mature Pollock 2018 and Chiribella–D'Ariano–Perinotti 2009. This note is a standalone public-safe mathematical return, not a claim that a source-native new NASH physical theory was proved.

## 1. Scientific question and owner boundaries

Candidate quotient `r_end` retains only a single CPTP map between the first preparation and final observation. Does it preserve every legally admissible intermediate instrument? **No**, even when the individual *unconditional* noise channels at both steps and the no-intervention endpoint channel are identical. The obstruction is quantum-operational and obeys CP, trace preservation, and the comb's no-future-signaling constraints. It does not involve full LOCC, hardware or the original three-qubit Helstrom construction.

Use one system qubit S and two noise intervals 0→1 and 1→2 with a selectable intermediate CP instrument. Let binary vector `v=(x,z)` label Pauli `U_v=X^x Z^z`; phases do not affect conjugation. Define `F(x,z)=(z,x⊕z)` over GF(2). There are four labels, uniformly sampled. Compare:

- **M (memory):** sample `v` uniformly and set second noise `w=F(v)` deterministically;
- **I (independent):** sample `v,w` independently and uniformly.

In both cases the first and second marginal labels are uniform. The composed label `v⊕w` is uniform in both cases, because `F` and `I+F` are invertible over GF(2). Consequently, every isolated one-step average channel and the entire no-intervention endpoint CPTP map equal the qubit completely depolarizing map `D(A)=Tr(A) I/2`, for ALL input operators A. The phrase 'second-step average' means a marginal averaged independently of recorded past history: it is **not** a history-conditioned channel, and claiming it remains fixed after observing the intermediate instrument would be false for M.

## 2. Legal CP instrument and exact discriminating distribution

Prepare `rho0=|0><0|`. At time 1 apply the two-outcome instrument with Kraus operators `K_a=|y+><a|` (`a=0,1`), with `|y+>=(|0>+i|1>)/sqrt(2)`. Each outcome map `A_a(rho)=K_a rho K_a†` is CP, trace-nonincreasing. The sum is CPTP because `sum_a K_a†K_a=I`. This procedure measures Z (records a) and prepares the Y=+1 eigenstate. At time 2 measure Y, giving outcome `y∈{+1,-1}`. This is a permitted physical tester; it is entanglement-breaking and uses no quantum communication between laboratories.

After first Pauli, the Z outcome is `a=x`. For the memory process, second noise `w=(z,x⊕z)`, so its Pauli conjugation flips the Y eigenvalue by `(-1)^(w_x+w_z)=(-1)^x=(-1)^a`. Thus:

| Outcome (a,y) | Memory M | Independent I |
|---|---:|---:|
| (0,+1) | 1/2 | 1/4 |
| (0,-1) | 0 | 1/4 |
| (1,+1) | 0 | 1/4 |
| (1,-1) | 1/2 | 1/4 |

Total variation between these **joint intervention-history distributions** is EXACTLY `TV=1/2`. The average qubit state at t=2 remains maximally mixed for both processes; the distinction survives in the correlation between recorded classical information a and the final output y. A reduction retaining only the endpoint CPTP map loses that correlation.

This witness is 'small' in the explicit operational sense of one qubit, a single intervening two-outcome instrument, two noise steps, one final two-outcome measurement, and four classical noise labels. **No minimality theorem for the size of the classical memory or number of outcomes is asserted.**

## 3. Causal quantum-comb verification

For each unitary `U`, use unnormalized Choi `J(U)=|U⟩⟩⟨⟨U|` with indices `(output,input)`. The two-step one-slot superchannel/comb in the index order `(S_{1,in}, S_0, S_2, S_{1,out})` is:

`W_p = sum_{v,w} p(v,w) J(U_v)_(S1in,S0) ⊗ J(U_w)_(S2,S1out)`.

Each term is PSD, hence `W_p>=0` for each p. Since every U is a CPTP unitary channel and the weights sum to one, every deterministic intermediate CPTP operation yields a deterministic endpoint CPTP map. The explicit recursive comb constraints are:

`Tr_(S2) W_p = J(D)_(S1in,S0) ⊗ I_(S1out)`;

`Tr_(S1in) J(D) = I_(S0)`;

`Tr W_p = 4` (two input qubit legs, unnormalized Choi convention).

The exact SymPy program constructs both 16×16 W matrices, checks PSD via exact eigenvalues and each partial-trace identity. The matrices are distinguishable despite equal channel reductions: `Tr[(W_M−W_I)†(W_M−W_I)] = 3`. The instrument's joint probabilities are independently computed by exact Kraus state propagation, not inferred merely from the comb matrices.

**Physical scope:** a causal, completely positive, classically correlated environmental memory model. No detector measurement, no source-native NCDG/TT mechanism and no claim of coherent quantum memory are present. The instrument and comb are mathematical physically implementable models, not performed hardware experiments.

## 4. Quantum-operational positive statement and mature-theory subtraction

Let `C` be a declared collection of allowed CP instruments and adapted final measurements. For two lawful process tensors `W,W'`, equality of all joint outcome distributions in C means that their difference pairs to zero with every tester effect in C: `Tr[(W−W')T_c]=0` for all `c∈C` in a matching Choi convention. This is an **elementary finite-dimensional linear-annihilator characterization**, not new physics. Equality of a single endpoint CPTP channel only tests a strict subset of these linear functionals and is insufficient by §2. Conversely, if C contains a tomographically complete family of legal CP instruments/testers, equality in all such contexts identifies the entire process tensor; this is already standard process-tensor/quantum-comb tomography, not an original CIPIR theorem. If C is restricted, the quotient must be built relative to its tester span and preserve admissible composition/adaptivity rather than merely pointwise observational labels.

**Closest primary literature actually checked:**

1. Pollock, Rodríguez-Rosario, Frauenheim, Paternostro & Modi, *Non-Markovian quantum processes: Complete framework and efficient characterization*, Phys. Rev. A **97**, 012127 (2018), DOI 10.1103/PhysRevA.97.012127. Gives process tensors as operational maps from intervention controls to output states, CP/linearity, circuit realization and tomography. https://doi.org/10.1103/PhysRevA.97.012127 . **Absorbs the main idea** that a CPTP snapshot cannot describe all multi-time interventions.
2. Pollock et al., *Operational Markov Condition for Quantum Processes*, Phys. Rev. Lett. **120**, 040405 (2018), DOI 10.1103/PhysRevLett.120.040405. Characterizes memory via an operational Markov criterion sensitive to interventions. https://doi.org/10.1103/PhysRevLett.120.040405 . **Absorbs the interpretation** of the correlated-memory M versus Markov I distinction.
3. Chiribella, D'Ariano & Perinotti, *Theoretical Framework for Quantum Networks*, Phys. Rev. A **80**, 022339 (2009), DOI 10.1103/PhysRevA.80.022339. Quantum combs, link product and causal recursive normalization, memory-channel universality. https://doi.org/10.1103/PhysRevA.80.022339 . **Absorbs the mathematical legality and composition** framework.

The above are first-owner seminal sources, not merely search-index title matches. The four-state classical intervention witness in the LT8 source report is a different elementary finite-state example; this quantum qubit example tests the same proposed reduction under CP and causal constraints, without upgrading that classical result to physics.

## 5. Verdict and falsifiers

- **PASS, narrow counterexample:** equal unconditional one-step and endpoint CPTP maps do NOT imply equality of legal two-time intervention histories, even for a qubit and classical stochastic Pauli environment. Exact TV witness 1/2.
- **PASS, legality:** chosen instrument is CP and instrument sum CPTP; both process Choi operators are PSD and satisfy the two recursive comb trace identities.
- **PRIOR ART ABSORPTION:** the quantum-operational phenomenon and suitable mathematics are already present in Pollock 2018 / Chiribella 2009; this does not establish a novel unifying NASH/CIPIR law.
- **OPEN residual for LT8:** find a SOURCE-TYPED restricted tester class from an original NASH field/operator/measurement carrier and prove a **nontrivial quantitative preservation or obstruction** NOT already implied by a generic process-tensor restriction. Otherwise H1 is a typed research architecture or an instance of mature process theory, not a new physical mechanism.
- **Falsification gates:** a faulty environment map F, step/endpoint Choi mismatch, an instrument failing `sum K†K=I`, a comb with negative eigenvalues or failed trace constraints, or a finite legal tester whose distributions were stated equal but are unequal all invalidate any promoted claim.
- **Not claimed:** minimal environment cost, quantum non-Markovianity beyond classical memory, LOCC advantage, finite-sensor performance, a physical NCDG mechanism, a quantum advantage, an empirical experiment or novelty.

## 6. Reproduction and route

Run `python IW_PRF13_LT8_THEORY_010_PRF_EXACT_TWO_TIME_COMB_FALSIFIER_REPRO_001_20261112.py` in Python with SymPy. The program checks exact uniform marginals and parity, entire Pauli-basis channel action, instrument normalization, all four joint probabilities, exact TV=1/2, PSD and recursive causality in the 16×16 comb, and `||W_M−W_I||_F²=3`. All arithmetic exact; no random seeds, optimisation, asymptotics or floating tolerance. External independent referee: **PENDING**.

**Scientific route:** full public-safe source body in `research/prf13/2026-11-12/` when GitHub save/readback verified; return link and test statement to `#iw-dispatch` with `LT8-THEORY-010-PRF`, addressed to LT8/INT9/M14 and Moderator. GitHub archive is not BW ingestion; Slack delivery is not owner acceptance. No edit to Living Theory, BW, NASH canon or external physical claim.

**RETURN:** `PRF13 / LT8-THEORY-010-PRF / EXACT_QUBIT_TWO_TIME_CAUSAL_COMB_FALSIFIER / ENDPOINT_CPTP_EQUAL / BOTH_STEP_MARGINAL_CPTP_EQUAL / INTERVENTION_TV_HALF / CP_AND_CAUSALITY_VERIFIED / POLLOCK_CHIRIBELLA_PRIOR_ART_ABSORBED / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / REFEREE_PENDING / BW_PENDING`.
