artifact_id: MT13-ROT040-PRF11-R33-AGE-DEPENDENT-STORAGE-MARKED-POISSON-EXACT-001_20261025
exposure: PUBLIC
claim_ceiling: NO_MATH_NOVELTY / NO_PHYSICAL_MEMORY_DEVICE / NO_UNRESTRICTED_PROCESS_TESTER / NO_CANON / NO_EXEC / PRF11_REFEREE_AND_OWNER_PENDING / BW_PENDING
sync_state: GITHUB_PENDING_BW_INGEST

# MT13 ROT040 — PRF11 R33: continuous storage-age dephasing produces a MARKED Poisson limit, not a mere count law

DATE 2026-10-25
RETURN_ID MT13-ROT040-PRF11-R33-AGE-DEPENDENT-STORAGE-MARKED-POISSON-EXACT-001_20261025
PROBLEM_ID LT4_CH7_MULTISLOT_PROCESS_STORAGE_AGE_NOISE_AND_MARKED_VISIBILITY_001
CLASS EXACT SOURCE-CONDITIONAL FINITE-PROTOCOL THEOREMS / MATHEMATICAL CLASSICAL HOST / 21 FULL-QUANTUM 2^n MATRIX CHECKS + 8 DIRECT 2^n BITSTRING ENUMERATIONS / FULL INDEPENDENT CLEAN REPLAY.
CEILING NO_MATH_NOVELTY / NO_PHYSICAL_MEMORY_DEVICE / NO_UNRESTRICTED_PROCESS_TESTER / NO_CANON / NO_EXEC / PRF11_REFEREE_AND_OWNER_PENDING / BW_PENDING.

## Literature HOST FIRST and source priority

**PRF11 R29** FIRST devised the distinct static-common-Cauchy phase vs independent-Cauchy-increment hypotheses with identical marginal one-time dephasing channels. PRF11 R31 introduced its fixed n-probe |+> SWAP testing protocol; R32 solved perfect-memory all-n fixed-protocol terminal Helstrom; R33 FIRST studied applying a *single equal* independent endpoint dephasing D_r to EVERY final probe, and obtained the homogeneous endpoint-noise Poisson limit. R33 EXPLICITLY excludes continuous quantum storage-time dephasing. This source-specific difference is the ONLY new host intervention here.
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R33_NOISY_MULTISLOT_POISSON_LIMIT_AND_MEMORY_VISIBILITY_GATE_001_20261025.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R32_ALL_N_HELSTROM_SYMMETRY_AND_WEAK_NOISE_SAMPLE_COMPLEXITY_001_20261025.md
LT5 provided prior-art-first M0–M5 and warns NOT to reproduce earlier χ-bar, optimal recovery or PRF quantum results as novelty:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/methodology/2026-10-25/IW_LT5_TO_MT13_THEORY_FIRST_SCIENCE_FRONTIER_AND_RESEARCH_DECISION_PACKET_001_20261025.md

MATURE HOSTS: product-state Uhlmann fidelity / Fuchs–van de Graaf trace bounds, Le Cam 1960 independent Bernoulli to heterogeneous Poisson random measures (https://msp.org/pjm/1960/10-4/pjm-v10-n4-p11-s.pdf), Helstrom hypothesis testing. Explicit exponential dephasing vs STORAGE AGE occurs in quantum-memory modeling, e.g. Robertson et al. 2026 https://doi.org/10.1002/qute.202500472 . General process testing host Milz–Modi 2021 https://doi.org/10.1103/PRXQuantum.2.030201 . These cited metadata/selected source texts are NOT claimed comprehensive complete literature priority review. This is NOT a mathematical novelty claim.

## Exactly LEGAL source, state and cost contract

Total time T>0 FIXED, a=γT>0, n>=2 equal phase-exposure slots Delta=T/n. Hypothesis A draws one static Cauchy frequency PER FULL RUN; B draws independent Cauchy-Lévy increments. One system qubit is exposed each slot, ideal deterministic SWAPs move the exposed qubit to a fresh |+> protected qubit; every stored qubit experiences *independent pure dephasing semigroup at rate κ_n* for its actual WAITING TIME to final joint measurement, no intermediate adaptive instruments, no active error correction, no SWAP faults. Last system probe waits ZERO. The memory is initially uncorrelated with phase source. This is NOT R33's per-probe single uniform endpoint D_r.

For k=0,..,n−1 (age k slots, k=0 freshest), b_n=κ_n T, r_{k,n}=exp(−b_n k/n), q_n=exp(−a/n).
Source terminal matrices for binary x,y:
 rho_A(x,y)=2^−n q_n^abs(|x|−|y|) prod_{j:xj!=yj} r_j
 rho_B(x,y)=2^−n q_n^dH(x,y) prod_{j:xj!=yj} r_j.
Let σ_{r,θ}=(I+r(cosθ X+sinθ Y))/2, σ_r=σ_{r,0}, θ~Cauchy(0,a/n). Then EXACT
 rho_A=E_θ tensor_j σ_{r_j,θ},
 rho_B=tensor_j σ_{r_j q_n}, rho_ref=tensor_j σ_{r_j}.
All states are PSD trace1; the resource compared is full TERMINAL POVM distinguishability at fixed SWAP schedule, not arbitrary n-slot process tester norm. The norm is ||rho_A−rho_B||_1 =2 optimal Helstrom total-variation advantage.

## THEOREM A — FULL terminal quantum information DISAPPEARS when n κ_n T→∞

Set β_n=n b_n=n κ_n T. For ANY positive β_n→∞, with fixed a>0:
  ||rho_A^(n)−rho_B^(n)||_1→0.                  (A)
No final POVM, even a coherent collective one, can sustain nonzero distinguishability in this declared noise family.

PROOF with explicit finite-n bound. Single-qubit squared fidelity:
  F(σ_{r,θ},σ_r)=1−r² sin²(θ/2).
Tensor fidelity and trace inequality show
  ||rho_A−rho_ref||_1 <= E[min(2,sqrt(n)|θ|)]
  = ε_A(z):=z/π log(1+4/z²)+4/π arctan(z/2), z=a/sqrt(n).
The Cauchy absolute first moment is infinite; the TRUNCATION is essential. ε_A=O_a(log(n)/sqrt(n))→0.

For B vs ref, the freshest k=0 has (1−F_0)=(1−q)/2<=a/(2n). For each k>=1,
  1−F(σ_r,σ_rq) <= min(1−q, r²(1−q)²/(1−r²))
    <= min(a/n, a²/(2 b_n n k)),
using 1/(exp(2 b_n k/n)−1)<=n/(2 b_n k).
Fuchs–van de Graaf and 1−prod F_k<=sum(1−F_k) give
  ||rho_B−rho_ref||_1 <=
  2 sqrt[a/(2n)+sum_{k=1}^{n−1}min(a/n,a²/(2 b_n n k))].
For β_n>a/2, compare the decreasing summand with its integral:
  SUM <= a²/(2β_n) [1+log(2β_n/a)].
Therefore EXACT FINITE-N QUANTUM BOUND:
  ||rho_A−rho_B||_1 <=
  ε_A(a/sqrt(n)) +
  2 sqrt{ a/(2n)+(a²/(2β_n))[1+log(2β_n/a)] }.      (A5)
When β_n→∞ the right side→0 EVEN if β_n/log(n) does not grow. For κT=.8 held fixed and n=10^6 this UPPER BOUND, NOT a full matrix simulation, is 0.01163844336445446. For all constant κ>0 and fixed T, convergence is O(sqrt(log n/n)).

## THEOREM B — CRITICAL lifetime yields a MARKED INHOMOGENEOUS Poisson experiment

If β_n=n κ_n T→β finite ≥0, then the binary X-basis outcomes of the reference rho_ref and rho_B form independent, age-indexed Bernoulli arrays:
 p0(k)=(1−r_k)/2 ~ (β(k/n))/(2n),
 p1(k)=(1−r_k q_n)/2 ~ ((β(k/n)+a))/(2n).
The limiting hypotheses are INHOMOGENEOUS POISSON POINT PROCESSES on marked probe age x∈[0,1] with intensity laws
   λ0(x)=β x/2,   λ1(x)=(β x+a)/2.                    (B1)
Their full experimental TV, not merely COUNT TV, is:
  lim_n ||rho_A−rho_B||_1 = 2 TV(PPP(λ0),PPP(λ1))>0 (a>0). (B2)
Furthermore individual NONENTANGLED final X measurements of each probe, retaining each probe's AGE LABEL, achieve this full final-POVM asymptotic bound. For β=0, λ0=0 and λ1=a/2; B2 recovers PRF11 ideal R32 limit 2(1−exp(−a/2)).

PROOF and TYPE GUARD: A approaches rho_ref in trace via ε_A→0. B and rho_ref are COMMUTING X-product states; their optimal quantum trace distance is exactly 2 TV of all AGE-LABELED Bernoulli bitstrings. For β_n→β, max p=O(1/n), sum p_i²=O(1/n); Le Cam individual-bin Poisson coupling is O(sum p_i²). To avoid the FALSE assertion that DISCRETE grid point configurations converge in total variation to CONTINUOUS point locations (they do not), apply uniform independent JITTER ONLY INSIDE EACH KNOWN BIN. Bin identity is exactly recoverable from a jittered point, so hypothesis TV remains UNCHANGED; the resulting piecewise-constant PPP intensities n p_i converge in L1 to λ_h, and Poisson coupling yields convergence of TV of the TWO experiments. Triangle inequality from rho_A-rho_ref finishes.

**STRICT NONMAP:** The Poisson COUNT means are Λ0=β/4, Λ1=β/4+a/2, but
  2 TV(Pois(Λ0),Pois(Λ1))
is only the distance after DISCARDING individual age labels, NOT generally the full B2 distance. Preliminary MT13 draft incorrectly claimed that count limit as full trace. Before archive it was REJECTED by an age-labeled likelihood test and independently corrected. Retain this correction as source-negative knowledge, not a superficial numerical adjustment.

## Exact a=1, β=2 EXAMPLE: marked process genuinely outperforms total count

Then λ0(x)=x, λ1(x)=x+1/2, Λ0=.5, Λ1=1.
The exact log-likelihood ratio for observed marked points x1,..,xK is
 L=−1/2+sum_i log(1+1/(2 xi)).
Optimal test:
 K=0 ⇒ A;
 K>=2 ⇒ B, since L >= −.5+2log(1.5) >0;
 K=1 ⇒ B exactly if x1<x*=.5/(exp(.5)−1)=0.7707470412683991.
Integrating K>=2 and K=1,x<x* exactly gives
 TV_marked =
  1.5exp(−.5)−2exp(−1)
  +exp(−1)(x*²/2+x*/2)−exp(−.5)x*²/2
 =0.24492260493265583.
Thus FULL LIMIT TRACE NORM = 0.48984520986531166.

By comparison Poisson COUNT-ONLY trace norm =
  2TV(Pois(.5),Pois(1))=0.47730243708238224;
loss of 0.01254277278292942 from discarding age labels. At n=10000 the exact finite Bernoulli age-labeled optimal likelihood calculation gives trace norm 0.48983604460397134, converging to the analytic value. This is the CORRECTED source typed distinction. At β=2 the corresponding R33 UNIFORM endpoint model with b=1 has only unmarked Poisson COUNT; same mean visibility expenditure but different shape means unequal information.

## Reproducibility and source-host scientific routing

Local ACTUALLY EXECUTED:
- 21 full n-qubit density-matrix cases (n=2..8 × ideal, fixed-rate .8 and critical β=2), build entire 2^n×2^n rho_A,B, check positive, trace1, compare exact Helstrom eigenvalues and upper bound A5; ALL PASS. No 2^10000 matrix claim.
- independent second Python enumerates EVERY one of 2^n CLASSICAL X-basis age-labelled output patterns for n=2,4,6,8,10,12,14,16, compares full age-marked and count-only optimal likelihood; eight direct PASS; age label advantage seen from n>=8;
- high n=100,400,1000,3000,10000 exact likelihood-positive-region for age-marked Bernoulli outcomes, verifies K>=2 always B for this a,β; n=10000 0.48983604460397134, source analytic 0.48984520986531166;
- bound A5 for n up to 10^6; does not claim quantum matrix computation there.
- source error self-audit: initial JSON writer accidentally serialized PosixPath, fixed; wrong preliminary unmarked-Poisson-as-full-limit claim corrected BEFORE GitHub report by independent bitstring enumeration and above exact likelihood.

Moderator FULL self-contained report+2 independent Python+JSON+SHA manifest+README ZIP:
 MT13_20261025_ROT040_PRF11_storage_age_marked_poisson_repro.zip
 SHA256 862b8c6b3e7358e4ddedbd01052d6da8404b19f3f2889caff83124d3736f1323.
CLEAN directory unzip CRC/SHA PASS; extracted original results JSON deleted, source Python re-executed INSIDE clean directory, exact regenerated JSON BYTE-BY-BYTE identical; independently rerun all-bitstring verifier PASS.
Full polished 16.6KB Polish theorem/provenance report also in this ZIP and conversation.

## Decisions and STOP
PRF11 R33: bounded source-local extension from uniform r endpoint noise to physically motivated DIFFERENT stored ages. Its one-line endpoint budget != a real storage lifetime; new threshold is β_n=nκ_nT, and full limit retains MARKS. PRF owns question and decisions, no attribution transfer or no-critic referee.
LT5 Ch7: history sufficiency vs count sufficient statistic, legal intervention/cost/time, full measurement versus compressed statistic — direct source-scoped science candidate only at LT author's discretion, no REV021 edit.
NC ART020/NC-NUM-007 prior audit RECEIVED PASS from external independent NC 2026-10-25 10:01 CET; per NC-033 only first backlog audit was done, others not started. No task cascade.
This is NOT a quantum hardware model verified against decoherence data, NO n-slot full comb optimum, no active correction, non-Markov bath, control noise, source gravity, physical NASH J3/K, BBH/PBH, quantum gravity, canonical adoption or EXEC.
STATE BOUNDED_THEOREM_PROPOSED / MATHEMATICAL_TESTED / HISTORICAL_PRF_OWNER_REVIEW_PENDING / REFEREE_PENDING / BW_PENDING / NO_MATH_NOVELTY / NO_CANON / NO_EXEC.