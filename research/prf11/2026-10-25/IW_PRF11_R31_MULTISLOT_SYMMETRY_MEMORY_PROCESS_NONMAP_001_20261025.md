---
artifact_id: IW_PRF11_R31_MULTISLOT_SYMMETRY_MEMORY_PROCESS_NONMAP_001_20261025
created_at: 2026-10-25
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_10 / PRF11
problem_id: LT4_CH7_MULTISLOT_PROCESS_TESTER_RESOURCE_VS_R30_ONE_SLOT_OPTIMALITY
exposure: PUBLIC_SAFE
canonical_body_path: research/prf11/2026-10-25/IW_PRF11_R31_MULTISLOT_SYMMETRY_MEMORY_PROCESS_NONMAP_001_20261025.md
bw_event_or_pending: GITHUB_PENDING_BW_INGEST
status: EXACT_RATIONAL_MATHEMATICS_AND_CLEAN_REPRODUCTION_PASS / REFEREE_PENDING
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE / NO_UNRESTRICTED_MULTISLOT_OPTIMUM_CLAIM / NO_NEW_OWNER_TASK
---

# PRF11 R31 — Three coherent SWAP slots beat the exact one-slot tester bound

**Date:** 25 October 2026. **Function:** source-first, others-first, nonblind mathematical falsifier, mature-host subtraction. This report is a standalone scientific proof. A separate locally attached ZIP contains an expanded explanatory report (17,809 UTF-8 bytes), full source code, machine-readable JSON, README and SHA manifest. The GitHub text is an independently formatted complete proof, NOT claimed to be byte-identical to the local expanded report.

## 0. Previous scientific ownership and precise gap

**PRF11 R29** constructed two processes sharing every one-time strongly continuous CPTP dephasing channel: (A) a frequency xi drawn once per whole run from symmetric Cauchy(0,gamma), and (B) symmetric Cauchy Levy independent phase increments. Their multi-time intervention laws differ. Original pinned source: https://github.com/wmakiela-tech/Nash-iw-research/blob/3199a28e2fff9f6f4a1a262f0d0708d81ba97145/research/prf11/2026-10-24/IW_PRF11_R29_CONTINUOUS_SEMIGROUP_PROCESS_ECHO_AND_QUOTIENT_CONTRACT_001_20261024.md

**REC10 ROT29** independently proved the diamond norm and timing tolerance for a FIXED echo pulse sequence, with PASS_WITH_SHARP_DIAMOND_AND_TIMING_GUARD: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/rec10/2026-10-24/IW_REC10_ROT29_PRF11_CONTINUOUS_PROCESS_ECHO_DIAMOND_TIMING_REFEREE_20261024.md

**PRF11 R30** proved exact optimal distinguishability among ALL instruments acting jointly on a qubit plus any finite-dimensional private quantum memory, but with **exactly ONE active intermediate time slot**. At two intervals s,t the optimum unnormalized output trace norm distance is exp(-gamma*abs(s-t))-exp(-gamma*(s+t)), and optimizing over s+t=T gives the theorem

    D_one_slot_opt(T)=1-exp(-gamma*T).                        (R31.0)

This is still valid. R31 does NOT falsify R30, but falsifies transfer of (R31.0) to THREE active slots. R30 source Git blob efac40c8e4db5d7451174041ecf886aed88db0ce: https://github.com/wmakiela-tech/Nash-iw-research/blob/2ca01509d410a0abce479d8f6c90a99480ef493d/research/prf11/2026-10-24/IW_PRF11_R30_FULL_ONE_SLOT_TESTER_NORM_CAUCHY_PROCESS_MEMORY_001_20261024.md

**LT5** has integrated previous process-vs-single-time source-typed logic into the native seven-chapter WORKING REV021, with original REV020 unchanged. Authorial adoption of R31 is not presumed.

## 1. Legal source and explicit quantum resource

Fix total T>0 and n>=2 equal subintervals Delta=T/n. Initially n qubits are available in |+>=(|0>+|1>)/sqrt(2): one phase-exposed system S, n-1 noiseless private memory qubits. At the n-1 intermediate times apply deterministic SWAP between S and the next fresh |+> private qubit; the old phase-bearing state remains coherently stored without additional exposure to noise. At the end measure all n qubits jointly. The environment is NOT reset between subintervals and the tester cannot read xi.

Hypothesis A: SINGLE static xi~Cauchy(0,gamma) persists across all n subintervals in one run. Hypothesis B: each disjoint subinterval has INDEPENDENT symmetric Cauchy phase increment with scale gamma*Delta. Without interventions BOTH give the identical all-time one-qubit channel D_exp(-gamma t). Ideal protected quantum storage and instantaneous swaps are mathematical resources, NOT actual hardware performance claims.

Let q=exp(-gamma*T/n). With psi_theta=(|0>+exp(i theta)|1>)/sqrt(2), final states are

    rho_A = E_xi [ |psi_(xi Delta)><psi_(xi Delta)|^(tensor n) ],
    rho_B = rho_q^(tensor n), rho_q=(I+qX)/2.               (R31.1)

For computational words x,y in {0,1}^n, with word Hamming weights |x|,|y| and Hamming distance d_H(x,y), Cauchy characteristic-function integration yields the complete exact matrix entries

    (rho_A)xy = 2^(-n) q^(abs(|x|-|y|)),
    (rho_B)xy = 2^(-n) q^(d_H(x,y)).                        (R31.2)

These are proper trace-one positive matrices with source and target precisely specified.

## 2. Theorem R31.1 — exact n-probe permutation-symmetry test

Let P_sym project onto the totally permutation-symmetric space Sym^n(C^2), of dimension n+1; let p_plus=(1+q)/2 and p_minus=(1-q)/2. Then:

    Prob_A(P_sym)=1,
    Prob_B(P_sym)=S_n(q)=sum_(k=0)^n p_plus^(n-k)*p_minus^k
                           =(p_plus^(n+1)-p_minus^(n+1))/(p_plus-p_minus).     (R31.3)

The exact binary-outcome TV distance of the test (P_sym,I-P_sym) is

    TV_sym = 1-S_n(q).                                      (R31.4)

Therefore the UNRESTRICTED optimal distance over n-1-slot testers (with full quantum memory) obeys the achievable lower bound

    D_multislot_opt(T,n-1) >= 2*(1-S_n(exp(-gamma*T/n))).     (R31.5)

PROOF: For EVERY fixed xi the vector psi_(xi Delta)^(tensor n) is permutation-symmetric, and its mixture rho_A remains wholly inside Sym^n. For B, diagonalize rho_q in the X eigenbasis |+>,|->. Each word with k minus entries has weight p_plus^(n-k)*p_minus^k. The NORMALIZED Dicke superposition of the C(n,k) equal-weight words is a single unit vector with exactly that expectation value; the binomial multiplicity cancels under normalization. Sum k=0,...,n to obtain S_n. The two outcomes are A:(1,0) and B:(S_n,1-S_n), so their TV is 1-S_n. A binary classical output trace distance equals twice its TV, proving the operational lower bound. QED.

Negative falsifier: re-drawing xi INDEPENDENTLY after every SWAP would change A into rho_q^(tensor n)=rho_B, making TV_sym=0. Here the noise environment remains one static xi for the entire run; a fresh system qubit is not a fresh noise environment.

## 3. Theorem R31.2 — 16x16 rational certificate, three slots > every one-slot tester

Choose n=4, i.e. exactly THREE intermediate SWAP slots, and gamma*T=4 ln(2), so q=1/2. Then p_plus=3/4, p_minus=1/4. Substituting into (R31.3) gives EXACTLY

    S_4(1/2)=sum_(k=0)^4 (3/4)^(4-k)*(1/4)^k
             =(3^5-1)/(2*4^4)=121/256.
    TV_sym=135/256.
    Achievable output trace distance >=135/128.            (R31.6)

At the SAME T the already proved OPTIMUM among ALL R30 ONE-SLOT strategies is

    D_one_slot_opt=1-e^(-gamma*T)=1-1/16=15/16=120/128.

Thus

    D_three_slot_opt >=135/128 > 15/16 =D_one_slot_opt,
    STRICT witnessed excess >=15/128.                      (R31.7)

This is a source-frozen EXACT finite-dimensional inequality. It does NOT establish three slots as globally minimal, nor an optimum over every possible three-slot quantum tester.

The fixed four-probe SWAP protocol admits an even stronger EXACT Helstrom certificate: define Delta=rho_A-rho_B from the 16x16 rational matrices (R31.2). SymPy rational eigendecomposition gives positive eigenvalues +75/256,+33/256,+27/256 (once each), zeros (twice), and negative eigenvalues -27/256 (multiplicity 3), -9/256 (multiplicity 5), -3/256 (multiplicity 3). Each eigenvalue and multiplicity was verified against the characteristic polynomial in exact arithmetic.

Independently, P_sym*rho_A=rho_A; [P_sym,rho_B]=0. On the symmetric subspace, Delta has exactly three positive and two zero eigenvalues. On its orthogonal complement Delta=-rho_B<=0. Therefore the simple two-outcome P_sym measurement is an EXACT optimal Helstrom projector for the FIXED four-probe SWAP protocol:

    ||rho_A-rho_B||_1 =135/128 (exact).                      (R31.8)

For equal prior hypothesis probabilities,

    Success_four_probe =1/2+(135/128)/4=391/512,
    Success_opt_one_slot =1/2+(15/16)/4=47/64=376/512,
    strict decision gain =15/512.                           (R31.9)

Two useful readout controls: measuring all qubits in the original computational Z basis gives TV=0. Measuring them INDIVIDUALLY in X basis gives classical output L1 norm=375/512, LESS than both coherent symmetry L1=135/128 and the one-slot norm 15/16 for these exact selected readouts. No general no-LOCC theorem is claimed.

## 4. Theorem R31.3 — fixed-time arbitrary-resource lower limit

Fix a=gamma*T>0 independent of n, q_n=e^(-a/n). Then

    p_plus,n=(1+q_n)/2 =1-a/(2n)+O(1/n^2),
    p_minus,n=(1-q_n)/2=a/(2n)+O(1/n^2).

The exact geometric sum (R31.3) can be rewritten as

    S_n=p_plus,n^n * [1-(p_minus,n/p_plus,n)^(n+1)] /
                       [1-p_minus,n/p_plus,n].

Since p_plus,n^n->e^(-a/2) and p_minus,n/p_plus,n->0,

    S_n(e^(-a/n)) -> e^(-a/2),
    TV_sym(n,T) -> 1-e^(-gamma*T/2),                         (R31.10)
    achieved output trace norm -> 2*(1-e^(-gamma*T/2)).

Compare with the FULL optimum one-slot bound 1-e^(-gamma*T):

    2*(1-e^(-a/2))-(1-e^(-a))
      =(1-e^(-a/2))^2 >0 for EVERY a>0.                     (R31.11)

So for every positive fixed gamma*T some finite n already gives a witness exceeding the BEST one-slot tester. An exact finite-n sufficient check is

    S_n(e^(-a/n)) < (1+e^(-a))/2.                           (R31.12)

At n=4,a=4ln2, S4=121/256 and RHS=136/256. This yields strict advantage with finite 3-slot memory and is NOT an assertion that unlimited intervention slots are physically cost-free.

The limit in (R31.10) is the LIMIT OF THE EXPLICIT SYMMETRIC-SPACE MEASUREMENT, not the claimed optimal unrestricted quantum multi-slot process norm. R30 is still correct within its stipulated one-slot class.

## 5. Source-code independent reproduction and nonblind provenance

One standalone Python script reproduce_prf11_r31.py uses SymPy and NumPy without importing prior PRF11, REC10, LT5 or NC scripts. It constructs the FULL exact 16x16 density matrices from (R31.2), rational P_sym with entries 1/C(n,k) on equal-weight word pairs, exact trace/multiplication/commutation, rational characteristic-polynomial spectrum, both sign blocks and output trace norm. It also runs 35 independent full-matrix tests (n=2,...,6 and seven total-time a values), four high-n closed-form limiting tests up to n=100000, q=0 and q=1 boundary controls, and separate local X/Z readout controls.

FULL independent local complete packet:
IW_PRF11_R31_MULTISLOT_SYMMETRY_MEMORY_FULL_REPRODUCTION_001_20261025.zip

ZIP SHA256: 3279bfb8ef4495c961a9840f79269208cbf021b77bd4a330809d6ee1a0e316a9

ZIP contains expanded complete explanatory report (17809 UTF-8 bytes; SHA256 c79a83f19527fbc887bc4d28489dc99ec191e57717208420914668c3102396fc), executable Python, deterministic output JSON, README, SHA256 manifest. Verified CRC PASS, four manifest hashes PASS, clean-directory execution PASS, JSON BYTE-FOR-BYTE regeneration PASS. Uploaded GitHub REPORT alone does NOT imply the binary ZIP or scripts were also stored in GitHub.

**Nonblind honesty:** selection of the n=4,q=1/2 rational witness followed exploratory floating-point scans within this same rotation. It was NOT a blind/preregistered discovery. The final algebraic rational proof remains sound irrespective of the selection process.

## 6. Mature-host subtraction, anti-overclaim and status

Existing hosts: Cauchy stable dephasing, quantum channel memory-assisted testing (Chiribella-D'Ariano-Perinotti PRL 101,180501, 2008, DOI https://doi.org/10.1103/PhysRevLett.101.180501), process tensor/quantum non-Markovianity (Milz-Modi PRX Quantum 2,030201, 2021, DOI https://doi.org/10.1103/PRXQuantum.2.030201), standard Hilbert-space symmetric/Dicke representations, Helstrom quantum binary discrimination. This is a bounded source-local construction with no claim of new mathematical phenomenon or priority over literature.

Critical nonmaps:
- SAME_ONE_TIME_ALL_T_CPTP != SAME_MULTITIME_INSTRUMENT_RESPONSE.
- BEST_ONE_SLOT != BEST_THREE_SLOTS. Our result **does not contradict R30**.
- ONE_STATIC_FREQUENCY_PER_COMPLETE_RUN != FRESH_INDEPENDENT_FREQUENCY_EACH_SLOT.
- FIXED_SWAPS_FINAL_HELSTROM_OPTIMUM != UNIVERSAL_THREE_SLOT_STRATEGY_OPTIMUM.
- IDEAL_NOISELESS_QUANTUM_MEMORY_RESOURCE != CERTIFIED_LAB_HARDWARE.
- CORRECT_MODEL_MATH != INDEPENDENT_REFEREE / OWNER_ADOPTION / BW_INGEST / MODERATOR_EXEC.

STATUS: MATHEMATICAL_RATIONAL_PASS / SOURCE_CODE_CLEAN_REPRO_PASS / GITHUB_RETRIEVAL_PENDING_UNTIL_VERIFIED / INDEPENDENT_REFEREE_PENDING / GITHUB_PENDING_BW_INGEST / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE / NO_NEW_OWNER_TASK.
