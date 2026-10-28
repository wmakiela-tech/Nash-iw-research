---
artifact_id: IW_PRF12_R16_RESET_AGNOSTIC_SOURCE_TEST_AND_SEPARATE_LIFETIME_CALIBRATION_001_20261029
created_at: 2026-10-29
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
problem_id: PRF12_R15_UNKNOWN_SOURCE_RESET_SCHEDULE_AND_LOCAL_COST
exposure: PUBLIC
canonical_body_path: research/prf12/2026-10-29/IW_PRF12_R16_RESET_AGNOSTIC_SOURCE_TEST_AND_SEPARATE_LIFETIME_CALIBRATION_001_20261029.md
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_RESET_AGNOSTIC_LOCAL_TEST / FINITE_SAMPLE_BINOMIAL_CERTIFICATE / SEPARATE_RESET_ESTIMATOR / NUMERIC_REPRO_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_UNRESTRICTED_SINGLE_COPY_LOCC_HELSTROM_OPTIMALITY / NO_GLOBAL_LOCC_CLOSURE_GAP / NO_UNAMBIGUOUS_B_DETECTION / NO_FINITE_SOURCE_ACTIVE_SWAPS / NO_NONIDENTICAL_WITHIN_RUN_EXPOSURES / NO_UNKNOWN_BASIS_MISALIGNMENT / NO_NOVELTY_OR_PRIORITY_CLAIM / NO_CANON / NO_EXEC_SIGN
function: SCIENCE_FIRST / LITERATURE_FIRST / TWO_SURFACE_PRIOR_ART / NEGATIVE_KNOWLEDGE_PRESERVING / FALSIFIER_FIRST
---

# PRF12 R16 — Dokładny lokalny test źródła odporny na dowolny harmonogram resetowania ukrytej częstotliwości

**29 października 2026.** **Owner:** PRF12. **Scientific claim:** a fully three-party local randomized-basis readout with one classical random bit per run distinguishes the pre-existing A vs B source contracts with an EXACT iid Bernoulli statistic *even for an arbitrary, adversarially selected and temporally correlated sequence of hidden Cauchy phases across runs*. The iid statement is for the randomized COARSE binary event, not for all raw local outcomes or for a general quantum memory beyond the model. A separate local two-run SWAP statistic estimates partial reset/persistence only under a calibrated, independently replicated two-run macroexperiment contract.

## 0. Internal first owner and mature external prior art

- Original first owner: PRF11 R35, static Cauchy xi vs independent Cauchy–Lévy increments under memory storage and ideal transfers: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R35_NONUNIFORM_SWAP_TIME_GRID_RECOVERS_IDEAL_MEMORY_WITH_CRITICAL_STORAGE_RATE_001_20261025.md
- PRF12 R04: exact n=3 endpoint source states and readout norms: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R04_THREE_PROBE_FINITE_SWAP_EXACT_X_READOUT_GAP_AND_SECTOR_DECOMPOSITION_001_20261026.md
- PRF12 R09: critical correction of invalid transfer from refined LOCC outcomes to a binary zonotope. Full single-run LOCC-closure Helstrom gap remains OPEN: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R09_COARSE_GRAINING_COHEN_THEOREM_AUDIT_AND_CORRECTED_CLAIM_CEILING_001_20261026.md
- PRF12 R14: source-reset dichotomy and 2-run local SWAP witness: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-28/IW_PRF12_R14_SOURCE_RESET_AND_UNAMBIGUOUS_LOCC_AUDIT_001_20261028.md
- PRF12 R15: **KNOWN** reset-partition optimum for one-sided unambiguous B-heralding, using local permutation symmetry: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-28/IW_PRF12_R15_OPTIMAL_LOCC_HERALD_UNDER_PARTIAL_SOURCE_RESET_001_20261028.md . **R16 is an alternative BINARY minimum-error repeated-run task with UNKNOWN reset schedule**, not a contradiction or extension of the unambiguous zero-error claim.

Mature external methods (not novelty): local Pauli correlation measurement and randomized bases; e.g. *Complete Characterization of Quantum Correlations by Randomized Measurements*, Physical Review Letters 131, 090201 (2023), https://doi.org/10.1103/PhysRevLett.131.090201 . Source comparison using correlated noise: *Spatially correlated classical and quantum noise in driven qubits*, npj Quantum Information (2024), https://www.nature.com/articles/s41534-024-00842-9 . Exact binomial likelihood tests and valid confidence intervals have classical statistical precedence: Clopper–Pearson, and R `binom.test`, https://www.stat.ethz.ch/R-manual/R-devel/library/stats/html/binom.test.html . These papers do NOT claim our source-specific Bernoulli identity or provide a priority guarantee.

## 1. Frozen contract and source-memory quantifiers

Each **RUN** uses three fresh initially plus-aligned qubits with exactly equal free exposures Δ=T/3 and ideal instantaneous SWAPs; no local memory aging κ=0. After a run, one qubit belongs to each of THREE separated laboratories. There is a shared, calibrated orthogonal pair of local axes X and Y. Each run consumes THREE qubits. All subsequent preparations and measurement random coins are independent from run to run. No nonlocal gates or quantum channels.

Hypothesis A for the original PRF11 source: conditional on a hidden classical phase φ_r=ξ_rΔ, the three run output qubits are all in the **same equatorial PURE state**

 |u(φ_r)>=(|0>+exp(iφ_r)|1>)/sqrt(2), so ρ_{A,r|φ_r}=|u(φ_r)><u(φ_r)|^{⊗3}.

The hidden phase history is **exogenous and independent of the measurement-setting coins** (the setting can be selected privately after the quantum output has been prepared). The sequence φ_1,...,φ_M may be **arbitrarily dependent**: one frozen ξ for all runs, a fresh independent ξ every run, arbitrary unknown deterministic reset partition, random partial resets, even a fixed adversarial classical phase path. The only essential A assumption is a common phase WITHIN every three-probe run and no other quantum correlations conditional on the entire phase path. The Cauchy distribution is NOT needed for the A-side output law derived below.

Hypothesis B is independent symmetric Cauchy–Lévy phase increments across the three exposures in EVERY run and between runs, so after source averaging each run has the product density ρ_B=ρ_x^{⊗3}, ρ_x=(I+xX)/2, x=exp(-q), q=γΔ>0, and different runs are independent. If B is correlated across runs or the local Bloch vector differs/rotates, R16's iid B claim must be audited anew.

## 2. Theorem R16.1 — a three-lab local Bernoulli bit immune to reset history

**One-run protocol:** generate a fair, independent CLASSICAL bit C_r. If C_r=0, all three labs measure X on their qubit. If C_r=1, all three labs measure Y. Communicate the three ±1 outcomes classically to a decision node. Define a single coarse bit Z_r=1 if all three signs are identical (+++ or ---); Z_r=0 otherwise. Forget the raw signs/axis when doing the simple discrimination test.

For three independent qubit outcomes along an axis with mean polarization a, the probability of all signs identical is

 g_3(a)=((1+a)/2)^3+((1-a)/2)^3=(1+3a²)/4.          (R16.1)

For an A phase φ, a_X=cosφ, a_Y=sinφ. Averaging only over the independently randomized axis,

 P(Z=1|A, φ)=[g_3(cosφ)+g_3(sinφ)]/2=5/8.         (R16.2)

This equals 5/8 **for every individual φ**, not merely after Cauchy averaging. The random setting is crucial. For B, a_X=x and a_Y=0, so

 P(Z=1|B)=[g_3(x)+g_3(0)]/2=(2+3x²)/8.           (R16.3)

Thus for q>0,

 p_A=5/8=0.625,    p_B=(2+3 exp(-2q))/8 <5/8,
 Δp=p_A-p_B=(3/8)(1-exp(-2q))>0.                  (R16.4)

**Arbitrary-reset iid lemma:** conditional on ANY complete hidden phase history (φ_1,...,φ_M), different run measurements and fair axis bits are independent and every Z_r~Bernoulli(5/8). Therefore the conditional joint distribution factorizes as ∏_r Bernoulli(5/8), and averaging over ANY correlated phase-history law leaves precisely iid Bernoulli(5/8). Under B, the independent-run source contract gives iid Bernoulli(p_B). Consequently all exact classical binomial finite-N error rates apply EVEN IF ξ is fixed for all M runs.

The equivalently measurable effective binary local POVM effect is

 M=(M_same,X+M_same,Y)/2 = I_8/4+(1/8)Σ_{i<j}(X_iX_j+Y_iY_j).    (R16.5)

As R04 gives Tr(D XiXj)=Tr(D YiYj)=b/2, b=1-x², Tr(M D)=3b/8. This is a direct **independent endpoint-matrix** cross-check of R16.4. All operations implementing M are local with a shared classical random bit and postprocessing; the 8×8 matrix expression alone is not the operational implementation proof.

## 3. Theorem R16.2 — exact finite-run likelihood and resource count

Assume calibrated q>0 and equal initial priors P(A)=P(B)=1/2. For M runs, K=Σ Z_r is binomial with parameters (M,p_A) or (M,p_B). The likelihood-ratio decision guesses A iff

 K log(p_A/p_B) +(M-K)log[(1-p_A)/(1-p_B)] ≥0.       (R16.6)

Put

 k_*(M)=ceil{ M log[(1-p_B)/(1-p_A)] / ( log(p_A/p_B)+log[(1-p_B)/(1-p_A)] ) },

with ties harmless. Then EXACT average Bayes error is

 R_M=(1/2)[Pr_{p_A}{K<k_*}+Pr_{p_B}{K≥k_*}].       (R16.7)

All quantities finite and computable from binomial CDF/SF. This is optimal **for the particular coarse Bernoulli data** {Z_r}, not for all local three-qubit readouts or global quantum measurements.

At q=1/3: x²=0.513417119032592, p_A=0.625000000000, p_B=0.442531419637, Δp=0.182468580363.

| Runs M | Exact likelihood decision | Exact average Bayes error | Qubits |
|---:|---|---:|---:|
| 48 | A iff K≥26 | 0.099686953020 | 144 |
| 80 | A iff K≥43 | **0.049250783650** | **240** |
| 90 | A iff K≥49 | 0.040159166982 | 270 |
| 160 | A iff K≥86 | 0.009721997110 | 480 |
| 281 | A iff K≥151 | 0.000990823283 | 843 |

M=80 is the **smallest integer** whose exact Bayes error for THIS Bernoulli protocol is ≤5%, as confirmed by checking all M from 1 to 80. At M=80, the error under A (guess B) is 0.042985254204, and the error under B (guess A) is 0.055516313097; the *prior-weighted mean* is 0.049250783650. Thus 80 does **NOT** guarantee each conditional error <5% (the B error exceeds 5%). This distinction prevents a common experimental-specification mistake. A **different operational target**, controlling both conditional errors to ≤5%, is already achievable with **83 runs** using the integer threshold A iff K≥45: error(A)=0.048584967591, error(B)=0.043424986714. An exhaustive finite binomial threshold sweep for all M<83 shows that 83 is the smallest run count for this stricter target *within this particular Bernoulli experiment*.

An a priori, non-asymptotic, uniform error bound is obtained by the midpoint frequency threshold:

 P(error|A) ≤ exp[-M(Δp)²/2],  P(error|B) ≤ exp[-M(Δp)²/2].   (R16.8)

This is Hoeffding's inequality and requires no iid property for the raw hidden phase, only the proven iid property of Z_r. At q=1/3 the bound guarantees ≤5% on EACH conditional error by M=180 (540 local qubit readouts). Exact binomial likelihood improves the average-case count; it is not interchangeable with the uniform guarantee.

**Unknown q:** If q is not calibrated but is fixed at any q>0, choose a sequence ε_M>0 with ε_M→0 and M ε_M²→∞, e.g. ε_M=M^(−1/3). Guess B when K/M <5/8−ε_M, A otherwise. Under A, the chance of mistaken B is ≤exp(−2M ε_M²). Under B, for each fixed q>0 the true gap Δp(q)>0, so eventually ε_M<Δp/2 and the probability of mistaken A is ≤exp[−2M(Δp−ε_M)²]. Hence the test is **consistent without knowing q**, but no uniform sample size exists when the allowed q approaches 0 (the two source families coalesce at q=0). When q≥q0>0 is known a priori, use Δp(q0) as a conservative threshold to get a uniform finite-M guarantee.

## 4. Falsifier: a single fixed X setting can fail at long memory

If all M A runs retain exactly the same hidden ξ, then a fixed-X all-equal readout has conditional success probability

 p_A^X(φ)=(1+3 cos²φ)/4.

Under B, p_B^X=(1+3x²)/4. These are equal for any φ satisfying cos²φ=x². Such phases exist for all q>0. Thus repeated *fixed-X all-equal bits alone* can have the SAME conditional law under some A histories as under B. A test based solely on this statistic has no uniform phase-conditional separation. In contrast fair X/Y randomization makes the A probability a constant 5/8 and separates it from p_B for every phase.

For fair mixing of TWO orthogonal settings θ and θ+π/2, the result is unchanged under common rotation: cos²(φ−θ)+sin²(φ−θ)=1 and the B polarization contributions sum to x². Moreover fair probability 1/2 is **necessary** among mixtures of those two axes for exact φ-independence, because a biased mixture gives a residual term proportional to (2π−1)cos[2(φ−θ)]. This is an internal uniqueness claim for this *specific all-equal two-setting family*, not a global optimality theorem among arbitrary LOCC measurements.

## 5. R15 compatibility and separate, conditional lifetime estimation

**The R16 source-type bit Z deliberately erases information about the reset partition:** under A its entire distribution is the same for all reset schedules, so it contains ZERO statistical information about persistence. Identifying reset times is a DISTINCT task; source discrimination should not be confused with reset estimation.

Retain the exact R14 one-laboratory, TWO-RUN antisymmetric projector Π_−=(I−SWAP)/2 acting jointly on the *same laboratory's* two qubits from adjacent runs. For q>0 set p0=(1−e^(−2q))/4. Under the known A contract:

 - if one ξ is shared across both runs, Pr(Π_-)=0;
 - if ξ is independently redrawn, Pr(Π_-)=p0.

Suppose M independently reinitialized **two-run macroexperiments** are run under A, each with an independent Bernoulli persistence flag R~Bernoulli(θ): with probability θ a single ξ is shared across the pair, otherwise a new independent ξ is drawn in the second run. Then each local antisymmetric click T_j is iid Bernoulli((1−θ)p0). Thus

 θ_hat=1−(Σ_j T_j/M)/p0                                              (R16.9)

is unbiased before optional [0,1] clipping. Hoeffding gives a valid 1−α confidence radius

 |θ_hat−θ| ≤ [1/p0]sqrt(log(2/α)/(2M))                       (R16.10)

when q and source type A are calibrated and all M macroexperiments are independent. At q=1/3, p0=0.121645720242. A conservative 95% confidence **radius ≤0.1** requires at least M=12,465 independent two-run macroexperiments (24,930 runs; two local qubits per macroexperiment). This loose number is for a simple Hoeffding guarantee, not optimal Fisher information or experiment design.

If instead xi histories are arbitrarily correlated across macroexperiments, or one unknown reset pattern is observed only once, the iid estimator and confidence interval need NOT apply. Under B, the same local test yields p0 regardless of a hypothetical reset flag, so this statistic by itself cannot distinguish B from A_fresh. If q is unknown, θ and p0 are not identifiable from this one bit without an external calibration or another measurement. Neither result identifies individual reset times with certainty: absence of an antisymmetric click is uninformative about whether a reset occurred.

## 6. Resource and governance matrix

| Task | Quantum operations / memory | Classical information | Exact guarantee |
|---|---|---|---|
| **Source A vs B, ANY between-run reset path** | Each of three labs measures its one qubit in X or Y; NO quantum storage across runs | 1 shared random axis bit per run; compare three local signs | iid Bernoulli laws (R16.2–R16.4), exact M-run likelihood |
| **Persistence-rate θ after selecting source A** | One laboratory holds two qubits from adjacent runs; local two-qubit antisymmetric test | One binary SWAP event per independently initialized macroexperiment | iid Bernoulli((1−θ)p0), calibrated confidence bound |
| **One-sided exact B heralding with KNOWN group partition** | R15 local multi-run symmetry projectors in three labs | classical OR of local outcomes | R15 optimal SEP=LOCC result, separately scoped |
| **One-copy unrestricted LOCC closure Helstrom** | Any local operations/rounds and postprocessing | unrestricted | STILL OPEN after R09; R16 does not solve it |

Crucial conditions: q>0, ideal SWAP, equal within-run exposures, common within-run phase for A, independent per-run increments for B, coherent common X/Y reference calibration, no unknown adversarial measurement basis misalignment. The fair-axis test is not a physical demonstration and does not address finite source-active pulse durations, κ>0, distinct sensor phases, or experimentally realistic readout errors. Reset-resilient does NOT mean noise-agnostic.

## 7. Reproducibility, falsifiers and independent referee gate

Full independent NumPy/SciPy script:
IW_PRF12_R16_RESET_INVARIANT_RANDOM_XY_REPRO_001_20261029.py.

It constructs the two local POVM effects directly from three X/Y projectors, checks 307 arbitrary phase values against 5/8 to machine precision, evaluates B as an 8×8 density matrix at q=.05,1/3,.7,1.4,2.5,5, and checks all six closed probabilities. It independently verifies exact binomial thresholds, minimum M=80 at q=1/3 for average error ≤.05, Hoeffding bounds, fixed-X confounding, and a separately scoped reset-rate estimator. No Cauchy-tail quadrature, no random optimizer, no sampling needed to establish exact identities. Its numerical result is a verification of the algebra, not a proof of asymptotic LOCC optimality.

**Falsifiers:**
1. Find a phase φ for which equal-weight X/Y all-equal event under A differs from 5/8. This would invalidate the main reset immunity.
2. Show that A's three within-run output qubits do not share the SAME phase, or their conditional state is not |u(φ)>^{⊗3}; then the source contract, not merely the proof technique, has changed.
3. Show B retains cross-run latent memory; its iid Bernoulli premise then needs separate proof.
4. Check M and the coefficients 1/4 and 1/8 in the Pauli expansion, and compare with exact R04 D.
5. Recompute exact binomial threshold and BOTH conditional errors at M=80, not just the average error.
6. Challenge the θ confidence statement with correlated macroexperiments: it must fail outside the stated independent-repeat contract; that is an intended limitation.
7. Audit reference-frame alignment and finite gate operations before using the result in an experiment.
8. Seek prior art for the exact phase-agnostic all-equal statistic in this particular static-Cauchy vs Lévy SWAP source family. No originality/priority asserted.

## 8. RETURN

PRF12_R16 / SOURCE_TYPED_EXACT_PHASE_AGNOSTIC_LOCAL_STATISTIC / ALL_RESET_HISTORIES_A_CONDITIONAL_IID_BERNOULLI / B_PER_RUN_IID_BERNOULLI / EXACT_FINITE_N_LIKELIHOOD / EXACT_N80_MEAN_ERROR_BELOW_5_PERCENT_AT_Q1_3 / NO_GAMMA_CALIBRATION_REQUIRED_FOR_FIXED_Q_CONSISTENCY / RESET_MEMORY_ESTIMATION_SEPARATE_CALIBRATION / NUMERIC_REPRO_PASS / INDEPENDENT_REFEREE_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC / SINGLE_RUN_LOCC_CLOSURE_OPEN / GITHUB_PENDING_BW_INGEST.