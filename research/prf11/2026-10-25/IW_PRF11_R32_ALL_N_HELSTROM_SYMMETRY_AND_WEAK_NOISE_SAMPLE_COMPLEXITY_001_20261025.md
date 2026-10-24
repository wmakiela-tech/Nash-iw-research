---
artifact_id: IW_PRF11_R32_ALL_N_HELSTROM_SYMMETRY_AND_WEAK_NOISE_SAMPLE_COMPLEXITY_001_20261025
created_at: 2026-10-25
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_10 / PRF11
problem_id: LT4_CH7_MULTISLOT_PROCESS_SYMMETRIC_SWAP_ALL_N_TERMINAL_HELSTROM_AND_RESOURCE_SCALING
exposure: PUBLIC_SAFE
canonical_body_path: research/prf11/2026-10-25/IW_PRF11_R32_ALL_N_HELSTROM_SYMMETRY_AND_WEAK_NOISE_SAMPLE_COMPLEXITY_001_20261025.md
function: FUNCTION_FIRST / OTHERS_FIRST / EXACT_PROOF_FIRST / MATURE_HOST_SUBTRACTION / FINITE_SOURCE_TYPED_OPERATIONAL_TEST
status: EXACT_ALL_N_ANALYTIC_PROOF / INDEPENDENT_MATRIX_AND_RATIONAL_TESTS_PASS / INDEPENDENT_REFEREE_PENDING
bw_event_or_pending: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE / NO_GLOBAL_MULTISLOT_OPTIMALITY / NO_NEW_OWNER_TASK
---

# PRF11 R32 — All-n Helstrom optimality of the symmetry test, a covariance proof and weak-dephasing memory cost

**Date:** 25 October 2026. **Character:** mathematical source-frozen, nonblind continuation; no new quantum hardware or physical implementation. Exact claim: an unrestricted **final collective POVM optimum after ONE FIXED n-probe equal-time SWAP strategy**, not optimization among all n−1-slot quantum strategies.

## 0. Others first, currentness and prior-art subtraction

The following completed sources were read *before* this mathematical derivation:

1. [PRF11 R29](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-24/IW_PRF11_R29_CONTINUOUS_SEMIGROUP_PROCESS_ECHO_AND_QUOTIENT_CONTRACT_001_20261024.md): static Cauchy per complete run vs independent Cauchy phase increments, sharing **every** one-time CPTP semigroup, different intervention histories. Ownership stays R29.
2. [PRF11 R30](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-24/IW_PRF11_R30_FULL_ONE_SLOT_TESTER_NORM_CAUCHY_PROCESS_MEMORY_001_20261024.md): exact supremum over **all** one-slot quantum-memory testers `D_1,opt(T)=1−exp(−γT)`. Ownership stays R30.
3. [PRF11 R31, Git blob f599be09235cb6abd38ec1636e09d2f6213ef0a3](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R31_MULTISLOT_SYMMETRY_MEMORY_PROCESS_NONMAP_001_20261025.md): specifies n-probe SWAP strategy, *achievable* permutation-symmetric test distance `2(1−S_n(q))`, exact n=4,q=1/2 Helstrom certificate, `S_n→exp(−γT/2)` and existence of a finite n beating the one-slot optimum at any γT>0.
4. **REC10 ROT32, independent referee of R31**, [full source](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/rec10/2026-10-25/IW_REC10_ROT32_PRF11_FOURPROBE_SHARP_THRESHOLD_HELSTROM_REFEREE_20261025.md): `PASS_WITH_ALL_PARAMETER_HELSTROM_EXTENSION`; proves P_sym Helstrom for **all q∈[0,1] at n=4** (also n=2,3), exactly n=4 advantage iff `γT>2 ln(7/3)`. These are REC10's results; do not repeat them as R32 discoveries. This referee is for R31, NOT an independent referee of the present R32 all-n extension.
5. [LT5 ROT18](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/2026-10-24/lt5_rev021_rot18_global_quotient_process_arity_source_event_and_target_identifiability_001.md) and LT5 native REV021/ROT20 already integrate prior source-typed process/quotient and one-slot interpretation. No native monograph edits by PRF.
6. Quantum binary state discrimination/positive spectral projection is standard Helstrom–Holevo mathematics; a modern synopsis is *An invitation to the sample complexity of quantum hypothesis testing*, npj Quantum Information (2025), https://www.nature.com/articles/s41534-025-00980-8. The covariance/conditional-variance trick below is elementary mature probability and tensor-product positive kernels, not priority-certified mathematical novelty. The particular organization as a process-local all-n sharp theorem is a project-level result, not a claim no such lemma appears in earlier literature.

**Scientific opening after REC10:** `n=2,3,4` P_sym proven optimal, but `n>=5` lacked a uniform proof. R31 gave the limiting `2(1−e^(−γT/2))` for an achievable test, not the exact *terminal Helstrom* limit of the fixed SWAP output states. R31 asserted existence of some n beating one slot, but did not determine **weak-dephasing resource scaling** of the first successful n.

## 1. Precisely frozen model and resource accounting

Fix γ,T>0, a=γT, integer n≥2, equal exposure ∆=T/n and q=exp(−a/n). One live system qubit S and n−1 protected private-memory qubits, each initialized as |+>. Deterministic ideal SWAP at times ∆,2∆,...,(n−1)∆ loads an already exposed probe into protected storage and exposes the next fresh |+> probe. Same inaccessible environment across the WHOLE run: in alternative A sample one static ξ∼Cauchy(0,γ) ONCE; in alternative B independent symmetric Cauchy–Lévy phase increments over all disjoint intervals. No tester reads ξ; SWAP does not reset the environment. After the n-th interval perform one joint arbitrary POVM on all probes. No restriction on the final POVM, but the intermediate control sequence is held fixed as prescribed.

The full terminal states on `(C²)^⊗n` in computational-word basis `x,y in {0,1}^n` are the R31 source-owned identities

```
ρ_A(x,y) = 2^{-n} q^{||x|-|y||};
ρ_B(x,y) = 2^{-n} q^{d_H(x,y)} = ((I+qX)/2)^{⊗n}(x,y).
```

Both are trace-one positive. Let `P_sym` be the orthogonal projector onto totally permutation-symmetric qubits. `p_±=(1±q)/2` and

```
S_n(q) = Σ_{k=0}^n p_+^{n-k} p_-^k;
TV_sym = 1−S_n(q),   achieved trace norm D_sym=2(1−S_n(q)).
```

The source state's support identity `P_sym ρ_A = ρ_A` and the invariance `[P_sym, ρ_B]=0` are immediate from the common-static-frequency phase product and iid probes respectively. What remains is the *inequality* `(P_sym (ρ_A−ρ_B) P_sym) ⪰ 0` **for every n,q**.

## 2. Theorem R32.1 — all-n exact terminal Helstrom, proof by conditional covariance

**Theorem.** For every integer `n≥2` and every real `q∈[0,1]`, the above `P_sym` is a valid Helstrom-optimal binary POVM element for distinguishing the terminal states of this fixed strategy at equal prior probability. In particular

\[
\boxed{\|\rho_A-\rho_B\|_1=2(1-S_n(q))}
\]

and `P_success,n = 1/2 + (1−S_n(q))/2 = 1−S_n(q)/2`. A final measurement ancilla and arbitrary final quantum processing cannot improve this optimum, by ordinary quantum data processing. At `q=1` both states coincide and any measurement ties; at `q=0` the formula is understood by continuity, or directly by PSD covariance with identity kernel.

**Proof.** For `k=0,...,n`, write the normalized binary Dicke vector

```
|D_k> = C(n,k)^{-1/2} Σ_{|x|=k} |x>,
```

and define `c_k=C(n,k)`, `F_kk=sqrt(c_k/2^n)>0`. In this orthonormal symmetric basis, the compressed state difference has EXACT entries

\[
\langle D_k|(\rho_A-\rho_B)|D_l\rangle
 =F_{kk}(K_{kl}-H_{kl})F_{ll},                 \tag{32.1}
\]

where

```
K_kl = q^{|k−l|};
H_kl = [C(n,k)C(n,l)]^{-1} Σ_{|x|=k,|y|=l} q^{d_H(x,y)}.
```

We establish `K−H ⪰0` without evaluating any eigenvalue.

Let `Ω={0,1}^n` and `C_xy=q^{d_H(x,y)}`. It is PSD for `|q|≤1`, because `C` is the n-fold tensor product of the positive 2×2 kernel `[[1,q],[q,1]]`. Therefore there exists a finite centered real Gaussian random field `G_x`, indexed by `x∈Ω`, with covariance `E[G_x G_y]=C_xy` (allowing degeneracy at q=0 or 1).

Independently sample one UNIFORM random coordinate permutation π∈S_n. Let `x_k^π` be the binary word with ones in the **first k positions of π** and zeros elsewhere; `x_0^π=0`, `x_n^π=1`. The important geometric identity is

\[
d_H(x_k^\pi,x_l^\pi)=|k-l|\quad\text{for ONE SHARED permutation }\pi.\tag{32.2}
\]

Define the layer mean `\bar G_k=E_π[G_{x_k^π}]=(1/c_k) Σ_{|x|=k}G_x`. By the shared-permutation path identity and independent Gaussian/permutation averaging,

\[
E_{G,\pi}[G_{x_k^π}G_{x_l^π}]=K_{kl},\qquad
E_G[\bar G_k\bar G_l]=H_{kl}.\tag{32.3}
\]

The conditional cross terms of `G_{x_k^π}−\bar G_k` vanish after averaging π at each fixed G. Thus

\[
\boxed{K_{kl}-H_{kl}
=E_{G,\pi}[(G_{x_k^\pi}-\bar G_k)(G_{x_l^\pi}-\bar G_l)]}.\tag{32.4}
\]

For any real `v∈R^{n+1}`, `vᵀ(K−H)v=E[(Σ_k v_k(G_{x_k^π}−\bar G_k))²]≥0`. The matrix is symmetric real, hence PSD on the complexification too. Congruence through positive diagonal `F` in (32.1) proves `P_sym(ρ_A−ρ_B)P_sym⪰0`.

Since `P_sym ρ_A=ρ_A` and `ρ_B` COMMUTES with `P_sym`, the operator difference is block diagonal:

```
ρ_A−ρ_B = [ Δ_sym ⪰0    0;
             0         −ρ_B|_(Sym⊥) ⪯0 ].
```

According to the binary Helstrom spectral theorem, P_sym is an optimal acceptance projector (it can include zero eigenspaces). Finally `tr(P_sym ρ_A)=1`, `tr(P_sym ρ_B)=S_n(q)`; trace difference on the positive sector equals `1−S_n`, on the negative sector its opposite, so the trace norm is `2(1−S_n)`. **QED.**

**General mature-host lemma exposed by the proof:** If `C_xy=f(d_H(x,y))` is *any PSD Hamming-radial kernel* on `{0,1}^n`, then the `n+1` by `n+1` covariance difference `f(|k−l|)−mean_{|x|=k,|y|=l}f(d_H(x,y))` is PSD by exactly the same shared-permutation conditional variance proof. The present quantum claim requires the SPECIFIC source-state identification with `f(r)=q^r`; positivity of arbitrary kernels does not automatically manufacture quantum process states or a physical channel.

## 3. Consequence R32.2 — exact asymptotic terminal Helstrom norm, no residual POVM gap

Let `a=γT>0` be fixed and `q_n=e^(−a/n)`, `r_n=(1−q_n)/(1+q_n)=tanh(a/(2n))`. Exact geometric rearrangement (already source-owned R31) gives

\[
S_n(q_n)=p_{+,n}^{n}\frac{1-r_n^{n+1}}{1-r_n},\qquad
p_{+,n}=e^{-a/(2n)}\cosh(a/(2n)).\tag{32.5}
\]

Then `p_{+,n}^n→e^(−a/2)`, `r_n→0`, and `r_n^{n+1}→0`. With NEW exact all-n Helstrom equality, the limiting **full best final measurement for the fixed SWAP protocol** is therefore

\[
\boxed{\lim_{n\to\infty}\|\rho_A^{(n)}-\rho_B^{(n)}\|_1
=2(1-e^{-a/2}).}\tag{32.6}
\]

R31's old *achievable lower bound* is now the proven *exact terminal-measurement optimum* for every finite n and in the limit. This does NOT imply an upper bound on arbitrary other n−1-slot strategies.

## 4. Consequence R32.3 — weak-noise first successful probe count, exact scaling 4/a

For `a>0`, define

\[
n_{\min}(a):=\min\{n\ge2:2[1-S_n(e^{-a/n})]>1-e^{-a}\},\tag{32.7}
\]

where the right side is the proven best **ONE-slot ALL-tester** distance at the same total T (PRF R30). R31 established this set is nonempty for every a>0. REC10 established precise n4 threshold and negative n2/n3 within the SWAP family. We obtain a quantitatively new **weak-dephasing exact leading constant**:

\[
\boxed{\lim_{a\downarrow0} a\, n_{\min}(a)=4.}\tag{32.8}
\]

**Proof with uniform remainder and no assumed monotonicity in n.** Rewrite the test `S_n < (1+e^{-a})/2` as

\[
\frac{S_n}{e^{-a/2}} <\cosh(a/2).
\]

Using (32.5), `n log(cosh(a/2n))=O(a²/n)` for `n≥2`, `r_n=a/(2n)+O(a³/n³)` and `Σ_{k=0}^n r_n^k=1+r_n+O(r_n²)` uniformly as `a↓0`, we get **uniform in all n≥2**:

\[
S_n(e^{-a/n})/e^{-a/2}=1+\frac{a}{2n}+O(a^2/n).\tag{32.9}
\]

Also `cosh(a/2)=1+a²/8+O(a⁴)`, so

\[
S_n/e^{-a/2}-\cosh(a/2)
=\frac{a}{2n}-\frac{a^2}{8}+O(a^2/n+a^4).\tag{32.10}
\]

For every `ε∈(0,4)`, on **all** integers `2≤n≤(4−ε)/a`, the first two terms are positive and dominate the remainder: `a²/n` is only O(a) relative to `a/n`, and `a⁴` is o(a²). Hence no such n beats one slot for sufficiently small a. At `n=ceil((4+ε)/a)`, the same formula gives a strictly negative difference for sufficiently small a, hence THAT n beats one slot. Consequently `(4−ε)/a < n_min(a) ≤ceil((4+ε)/a)` for small a. Let ε↓0: (32.8). **No monotonicity of S_n over all integer n was presumed or proved. QED.**

**Useful explicit sufficient nonasymptotic budget.** For `n≥a`, log cosh(x)≤x²/2 and `r_n=tanh(a/(2n))≤a/(2n)≤1/2` yield

\[
S_n \le e^{-a/2}\,\frac{\exp(a^2/(8n))}{1-a/(2n)}
\le e^{-a/2}\exp[(a+a^2/8)/n].\tag{32.11}
\]

Therefore the easily audited condition

\[
\boxed{n\ge \max\{2,a\},\quad n>\frac{a+a^2/8}{\log\cosh(a/2)}}\tag{32.12}
\]

is sufficient (not claimed necessary or sharp at finite a) for `D_n> D_1`. As `a↓0`, this conservative upper budget scales as `8/a`, whereas the TRUE leading threshold is `4/a`.

**Exact-in-class, approximate-implementation table from deterministic high-precision double arithmetic:**

| a=γT | n_min | Ideal SWAP slots | a*n_min | Conservative sufficient integer from (32.12) |
|---:|---:|---:|---:|---:|
| .01 | 402 | 401 | 4.02 | 802 |
| .02 | 202 | 201 | 4.04 | 402 |
| .05 | 82 | 81 | 4.10 | 162 |
| .1 | 42 | 41 | 4.20 | 82 |
| .2 | 22 | 21 | 4.40 | 42 |
| .5 | 10 | 9 | 5.00 | 18 |
| 1 | 6 | 5 | 6.00 | 10 |
| 1.5 | 5 | 4 | 7.50 | 7 |
| 2 | 4 | 3 | 8.00 | 6 |
| 4 ln 2 | 4 | 3 | ≈11.09 | 5 |

For `a` sufficiently small, the number of *memory qubits* and active ideal SWAP slots in this carrier is n−1, hence both also scale `4/a`. This is an ideal resource-count statement, not wall-clock or experimental feasibility. Subtlety: since n_min is a *minimum over n*, values in this table do not assert global monotonicity of the advantage for all larger n. Program scanned all smaller integers for each point.

## 5. Independent executable controls, failures, and evidence tiers

Standalone **new R32** script `reproduce_prf11_r32.py` builds the complete terminal matrices without importing PRF11/REC10 scripts. It performs:

1. **49/49** matrix checks for n=2,...,8 and q∈{0,.05,.25,.5,.8,.97,1}: full `ρ_A,ρ_B`, `P_sym`, Dicke compression PSD, `S_n`, symmetry support, and for n≤6 the full 2^n ×2^n eigenvalue trace norm versus `2(1−S_n)`. Max trace/Helstrom discrepancy **4.44×10^-16**; max independent covariance congruence discrepancy **7.88×10^-16**; all compressed eigenvalues ≥−2×10^-13 (reported min 0 on the grid). Analytic proof is independent of finite eigensolvers.
2. Independent **exact SymPy rational q=1/2,n=5** calculation of the unnormalized 6×6 Dicke Gram Δ_sym: four strictly positive exact algebraic eigenvalues and two zeros. `S_5=91/256`, `||ρ_A−ρ_B||_1=165/128`. The q=1/2,n=4 rational REC10/R31 control remains `S_4=121/256`, `D4=135/128`, excess `15/128`, all exact.
3. Direct deterministic scan of first successful n for a∈{.01,.02,.05,.1,.2,.5,1,1.5,2,4ln2}; compares each finite-n nonasymptotic sufficient budget and the n−1 failure check; **10/10 PASS**.
4. Fixed-a n=100,1,000,10,000,100,000 convergence checks for a∈{.1,.5,2,4}; exactly matches limiting direction and bounded errors; **4/4 PASS**.
5. `q=0`/`q=1` edge controls are included in the 49 matrix grid.

The local saved JSON is deterministic with sorted keys; SHA256 file manifest and clean-extraction rerun must be archived beside this report. The report's mathematical certification rests on the covariance proof and uniform expansions, **not** on numerical agreement or a source-dependent floating optimum. The exploration was **nonblind**: R31/REC10 sources were read before R32; the all-n covariance argument was constructed after low-n eigensolver checks, not pre-registered as a held-out theorem. No contrary controls were deleted. All independently verified Python checks reported after completed run.

## 6. Claim ceiling and source-return disposition

**Earned:** for the EXACT fixed equal-time n-probe SWAP experiment with common-static-Cauchy versus independent-increment-Cauchy alternatives, the all-n simple symmetric-space test is an optimal final binary state measurement; exact trace norm at every finite n, optimal fixed-protocol limit, true leading low-a resource cost 4/a, explicit finite-n sufficient resource count; a separate general classical positive-kernel covariance lemma.

**Not earned:** optimality of this input/SWAP control over ALL n−1-slot testers; any conclusion about adaptive feedback multi-slot quantum combs; any source equivalence with NC ART029's classical damping sensor / BAE or QND physics; claims about real tested quantum devices, phase-noise calibration or finite-quality memory; gravitational J3/K, DTC0a invariance, BBN, PBH or new physics; novelty of Helstrom theory, Markov kernels or conditional variance; independent referee acceptance of THIS R32 or inclusion in native LT5 / BW / EXEC.

**Status:** MATHEMATICAL_ANALYTIC_PASS / INDEPENDENT_MATRIX_RATIONAL_TESTS_PASS / CLEAN_REPRO_PENDING_UNTIL_VERIFIED / GITHUB_WRITE_PENDING_UNTIL_READBACK / REFEREE_PENDING / GITHUB_PENDING_BW_INGEST / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE / NO_NEW_TASK.
