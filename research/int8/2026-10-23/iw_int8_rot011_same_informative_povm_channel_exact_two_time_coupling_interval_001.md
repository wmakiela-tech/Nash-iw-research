---
artifact_id: IW_INT8_ROT011_SAME_INFORMATIVE_POVM_CHANNEL_EXACT_TWO_TIME_COUPLING_INTERVAL_001_20261023
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P2_LT5_G2_INSTRUMENT_MULTITIME_IDENTIFICATION_001
date: 2026-10-23
document_type: EXACT_RESTRICTED_INSTRUMENT_FAMILY_CLASSIFICATION_AND_CAUSAL_TEST
exposure: PUBLIC
canonical_path: research/int8/2026-10-23/iw_int8_rot011_same_informative_povm_channel_exact_two_time_coupling_interval_001.md
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
status: ANALYTICALLY_DERIVED_AND_FINITE_MATRIX_CHECKED / INDEPENDENT_REFEREE_PENDING
claim_ceiling: MATURE_HOST_SPECIALIZATION / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# INT8 ROT011 — Same informative POVM and same full CPTP channel leave a sharp interval of two-shot histories and causal targets

## 0. Function, currentness, original hosts and subtraction

Moderator-accepted programme and LT5 2026-10-23 manuscript impact audit prioritize correctly typed quantum instruments, terminal targets and temporal histories. Direct LT5 G2 question: does a classical reset/readout consequence possess a legal CP instrument and how much of the multitime process is identified by its one-step data?

Already known; do NOT claim as new:
- LT5 ROT06: naive classical full Bloch reset Q_s=diag(1-s,1,1) non-CP; diamond nearest CPTP channel distance s/2.
- LT5 ROT07: two instruments with identical full CPTP marginal and same **input-INDEPENDENT** POVM, but different flagged-error recovery and diamond gap 4p(1-p).
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/2026-10-23/lt5_same_channel_same_povm_distinct_instrument_exact_causal_recovery_001.md
- INT8 ROT009: restricted input family, same scalar mean and nonselective reset can be achieved by legal Kraus operations, but selective trajectory differs.
- INT8 ROT010: weak OUTCOME-ONLY records become parameter-independent under a bound on total measurement contrast; not a statement about retained state.
- Geeky-S10 2026-10-23 derived exact Pauli channel–POVM compatibility and separately the affine-one-copy multitime nonmap, including the fact that classical independent noisy readouts have nonlinear theta dependence at two shots. These claims are prior.
- PRF11 R18: noisy-syndrome correction risk with same full channel/POVM; prior mature-host result.

**Material narrowly-scoped delta here:** In a simple **input-INFORMATIVE** POVM with fixed same-strength longitudinal damping, classify the ENTIRE allowed two-time correlation interval within a specifically declared Z-diagonal measure-and-prepare qubit instrument class, compute exact two-shot TV and flagged-instrument diamond distances, and give a direct postrecord feedforward target test. This is an exact finite classical coupling specialized to legal CP operations. No general quantum novelty is asserted.

Mature hosts: Davies–Lewis instruments; process tensor / sequential quantum operation representation, e.g. *Quantum Stochastic Processes and Quantum non-Markovian Phenomena*, PRX Quantum 2 030201 (2021), DOI 10.1103/PRXQuantum.2.030201, https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.2.030201; binary Fréchet–Hoeffding coupling bounds, see https://link.springer.com/article/10.1186/2195-5832-1-14. We do not invoke any fresh physical quantum source.

## 1. Carrier and exact legal instrument

Fix 0<s<1 and write a=1-s. Input is a SINGLE qubit. Label Z eigenstates |z>, z∈{±1}. For theta in [-1,1], define rho_theta=(I+theta Z)/2. We also describe operations on arbitrary qubit inputs.

For each z, choose a probability coupling on the PAIR (record y, prepared output eigenvalue w), both in {±1}, with fixed two marginal expectations:
  E[y|z]=s z,
  E[w|z]=a z.
A Z-flip-symmetric 1-parameter family of joint couplings is
  p_C(y,w|z) = [1+y s z+w a z+y w C]/4.           (1.1)

**Theorem 1 (exact valid range in this family).**
For BOTH possible input eigenvalues z and ALL y,w, p_C(y,w|z)>=0 iff
  0 <= C <= Cmax(s):=1-|s-a|=2 min(s,1-s).     (1.2)
Proof: For binary variables with means m1=s z,m2=a z and cross moment C, the four outcomes have masses (1+y m1+w m2+yw C)/4. Their nonnegativity is equivalent to
  -1+|m1+m2| <= C <= 1-|m1-m2|.
Here s+a=1, yielding [0,1-|s-a|]. Both endpoints and every convex intermediate coupling are attained. QED.

Construct four or eight (zero branches permitted) explicit Kraus operators:
  K_(y,w,z) = sqrt(p_C(y,w|z)) |w><z|.          (1.3)
The OUTCOME-indexed instrument operations are
  I_y^C(rho)=sum_{z,w} K_(y,w,z) rho K_(y,w,z)^dag.     (1.4)
Every branch is CP. Trace normalization:
  sum_{y,z,w} K^dag K
   =sum_z [sum_{y,w} p_C(y,w|z)] |z><z|=I.
Thus sum_y I_y^C is CPTP on ALL single-qubit states, including entangled extensions.

For EVERY C in (1.2), the entire POVM effects agree:
  (I_y^C)^*(I)=E_y=(I+y s Z)/2.                (1.5)
Therefore Pr(Y=y|rho_theta)=(1+y s theta)/2 and E[Y]=s theta.

For EVERY C, the entire nonselective CPTP channel agrees:
  Lambda_s(rho)
    =sum_z <z|rho|z> [I+a z Z]/2,             (1.6)
or, on any Bloch vector,
  (r_x,r_y,r_z) -> (0,0,a r_z).               (1.7)
This is a **stronger equality** than one-component output matching: both instruments have the EXACT SAME full CP map and full POVM. It is an entanglement-breaking channel, not the full naive non-CP classical Q_s. On rho_theta the terminal Z mean matches the classical scalar reset (1-s)theta.

Note a physically costly sharp Z dephasing/repreparation is built into this mathematical family. A small s controls the reported POVM contrast but does not make the **full** instrument a weakly disturbing operation: for all s, transverse coherences are erased. No weak hardware cost or noninvasiveness follows.

## 2. Theorem 2: exact two-shot outcome joint laws differ

Apply the SAME I^C instrument twice successively, with no interposed unitary, to the SAME rho_theta. Let Y1,Y2∈{±1} be the recorded results, and W1 the (unobserved) prepared Z-eigenstate after shot 1.

Conditional on W1=w, the second result has mean E[Y2|w]=s w. Hence
  E[Y1|theta]=s theta,
  E[Y2|theta]=s a theta,
  E[Y1 Y2|theta]=s E[Y1 W1|theta]=s C.         (2.1)

The EXACT joint probability table is
  P_C(Y1=y1,Y2=y2|theta)
     =[1+y1 s theta+y2 s a theta+y1 y2 s C]/4. (2.2)

Therefore, for all theta and any two admissible couplings C,D:
  TV(P_C^(2)(.;theta),P_D^(2)(.;theta))
       =s |C-D|/2.                            (2.3)
This is achieved on FOUR ordinary binary readout probabilities and does not require measuring a terminal qubit.

The exact attainable family interval for the two-shot mixed moment is
  0 <= E[Y1Y2] <= 2s min(s,1-s).               (2.4)

Covariance is
  Cov(Y1,Y2|theta)=s C-s² a theta².           (2.5)
In particular the **mixed moment** E[Y1Y2], rather than covariance, is the cleaner theta-independent identifier for C. For C=0 and theta!=0, covariance is NEGATIVE, even though E[Y1Y2]=0; do not confuse them.

For example s=.4,a=.6,C0=0,C1=.8:
  E[Y1Y2]: 0 vs .32,
  two-shot TV: .16.
Both instruments are fully legal CP, have exactly the same POVM E_y and nonselective channel Lambda_s.

## 3. Theorem 3: exact flagged instrument distance

The difference between first-shot operations is independent of the INPUT state except through its trace:
  (I_y^C-I_y^D)(rho)
      = y(C-D)/4 * Z * Tr rho.                 (3.1)
Define flagged quantum channels
  hat I^C(rho)=sum_y |y><y| tensor I_y^C(rho).
Then
  (hat I^C-hat I^D)(rho)
    =[(C-D)/4] (|+><+|-|-><-|) tensor Z * Tr rho. (3.2)

For arbitrary reference system R, replacing Tr rho by Tr_A rho_AR in (3.2) yields a tensor product of this fixed Hermitian flag×qubit operator with the retained reference state. The complete trace norm is the fixed operator's trace norm, and the bound is attained on any input state. Therefore
  ||hat I^C-hat I^D||_diamond = |C-D|.         (3.3)

For the endpoints, the gap is 2min(s,1-s), e.g. .8 at s=.4. This contrasts with outcome-only two-shot TV=.16: the joint FLAG+TERMINAL-QUBIT observation has stronger access to the C-dependent correlation. Both are type-specific distances; one must not identify them.

## 4. Exact causal postrecord target

After the first measurement with outcome y, apply a FREE-DESCRIBED conditional Pauli bit flip X only when y=-1, i.e.
  R_y=id for y=+1,
  R_y=Ad_X for y=-1.
This is a valid outcome-conditioned CPTP feedforward, available only AFTER the record is read and BEFORE measuring terminal Z.

It maps the post-shot eigenvalue w to y w. Therefore the terminal target
  E[Z_after_feedback|rho_theta]
     =E[Y W]=C                                  (4.1)
for EVERY theta in [-1,1], while WITHOUT feedback,
  E[Z_before_feedback]=a theta                 (4.2)
is identical across C.

Thus exactly the same first-shot POVM and the same full averaged channel permit different causal postrecord terminal Z targets, ranging from zero to 2min(s,1-s) in this specified class. For s=.4, the two instrument endpoints produce target 0 vs .8, despite same POVM, same first-step channel and same initial input family.

This is NOT a state-recovery theorem: it deliberately prepares a Z-biased state and can erase input information. The conditional operation can consume work; its physical hardware cost is not specified. It is an elementary legal causal-target discriminator, NOT a new quantum error-correction principle.

## 5. Comparison with INT8 ROT010 and other hosts

ROT010 bounded the information about INITIAL parameter theta available from a sequence of near-fair weak binary OUTCOME bits when sum strength<=B; it did not distinguish different theta-INDEPENDENT instrument couplings in the retained quantum state. Here (2.2) can depend on C, but for two fixed s-shots, both result laws are O(s²)-close in TV, entirely consistent with outcome-only weak-information collapse as s->0. If two instruments have distinct unknown model indices, their input theta and model C are different estimation targets.

LT5 ROT07 supplied earlier SAME channel + SAME POVM but flag uninformative about initial input. The present witness makes the POVM genuinely input-sensitive and fixes a nontrivial matched longitudinal attenuation while showing the **exact finite interval**, two-time TV and causal-terminal target. We do not claim the general instrument nonuniqueness was discovered here.

Geeky-S10 QND/Lüders nonmap and one-copy affine-probability theorem do not contradict (2.2): every P_C history is AFFINE in theta. The differences between the instruments enter the theta-independent coefficient y1y2 s C, not a theta² term. This explicit compatibility with Geeky's general one-copy affine theorem is a diagnostic check.

PRF11 target-risk/flagged-error result concerns optimum correction diamond under a different error carrier; here target is simply E[Z_after_feedback], not correction loss. Need source-specific target and intervention timing before declaring equivalence.

We make NO transfer to a source-certified measurement apparatus, time/energy budget, NASH physical PBH/NCDG/J3/K, or beyond-Born physical theory.

## 6. Synthetic reproducibility and exact numeric table

The accompanying NumPy test:
- explicitly builds all K_(y,w,z), checks CP-by-Kraus and sum K^dag K=I;
- checks full E_y and Lambda_s on coherent and diagonal inputs and exact two-shot joint law;
- checks C=0, Cmax and intermediate C;
- checks C-dependent causal feedforward target and a fixed-C theta-independent difference;
- verifies flagged-instrument trace-norm witness on a qubit input and analytic diamond formula (3.3).
All analytic identities are elementary algebra. Finite matrix tests are sanity checks, not independent referee acceptance.

| s | a=1-s | C_max | max 2-shot E[Y1Y2] | endpoint 2-shot TV | flagged diamond |
|---:|---:|---:|---:|---:|---:|
| .2 | .8 | .4 | .08 | .04 | .4 |
| .4 | .6 | .8 | .32 | .16 | .8 |
| .5 | .5 | 1.0 | .5 | .25 | 1.0 |
| .8 | .2 | .4 | .32 | .16 | .4 |

## 7. One problem, one state

problem_id: P2_LT5_G2_INSTRUMENT_MULTITIME_IDENTIFICATION_001
best_result: all-C exact CP realization with same informative POVM and full nonselective channel, sharp two-time moment/TV interval and postrecord target interval.
prior_source: LT5 ROT07 general informative-status-independent flag instrument nonuniqueness and diamond norm; Geeky-S10 ROT010-11 one-copy QND/affine history; INT8 ROT009-010; mature binary Frechet couplings/process instruments.
independent_referee: PENDING.
owner: LT5 chapter 5; PRF11 decision theory; Geeky-S10 legal reset source. INT8 reports typed integrator witness only.
blocker: no source-calibrated NASH CP instrument, physical energy/time/bandwidth costs, terminal controller or source-admissible future readout.
cheapest_discriminator: on legal realized instrument, measure joint (Y1,Y2) or (Y1,Z_out), not merely one-shot POVM effects or nonselective channel; compare with the exact C interval while controlling initial state and physical intervention timing.
decision: PASS as conditional legal qubit operations and mature-host coupling computation; HOLD physical implementation and source-original equivalence.
canonical_path: research/int8/2026-10-23/iw_int8_rot011_same_informative_povm_channel_exact_two_time_coupling_interval_001.md
bw_state: GITHUB_PENDING_BW_INGEST
no_new_task_cascade: true.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
