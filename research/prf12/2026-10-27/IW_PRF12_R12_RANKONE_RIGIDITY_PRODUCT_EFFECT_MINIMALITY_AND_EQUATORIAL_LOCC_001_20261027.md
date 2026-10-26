---
artifact_id: IW_PRF12_R12_RANKONE_RIGIDITY_PRODUCT_EFFECT_MINIMALITY_AND_EQUATORIAL_LOCC_001_20261027
created_at: 2026-10-27
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
problem_id: PRF12_R11_GENERAL_PRODUCT_PSD_MINIMALITY_AND_REFINED_LOCC_BOUNDARY
exposure: PUBLIC
canonical_body_path: research/prf12/2026-10-27/IW_PRF12_R12_RANKONE_RIGIDITY_PRODUCT_EFFECT_MINIMALITY_AND_EQUATORIAL_LOCC_001_20261027.md
sync_state: GITHUB_PENDING_BW_INGEST
status: LOCAL_EXACT_PRODUCT_PSD_RANK_RIGIDITY_PROOF / R11_MINIMALITY_EXTENDED / FIXED_EIGHT_PRODUCT_OUTCOME_POSITIVE_GAP_EXISTENCE / EXACT_EQUATORIAL_FEEDFORWARD_FORMULA / REPRO_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_FULL_LOCC_CLOSURE_GAP / NO_FINITE_PULSE_TRANSFER / NO_GLOBAL_ONEWAY_OPTIMALITY / NO_NUMERICAL_LOWER_BOUND_FOR_EIGHT_PRODUCT_OUTCOME_GAP / NO_NOVELTY_CLAIM / NO_PHYSICAL_DEVICE / NO_CANON / NO_EXEC
---

# PRF12 R12 — Exact rank-one rigidity for optimal PRODUCT effects, robust eight-outcome exclusion, and improved equatorial adaptive LOCC witnesses

**Data:** 27.10.2026. **Funkcja:** PRF12. **Mode:** independently rerun the R11 fixture, then separately extend its rank-one product minimality and search for a constructive readout witness without inferring unrestricted LOCC properties. **Independent referee:** PENDING.

## 0. First-owner source map, mature host and anti-self-sealing guard

- PRF11 R35 owns the original frozen static common Cauchy vs independent Cauchy–Lévy process distinction and ideal SWAP state formula: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R35_NONUNIFORM_SWAP_TIME_GRID_RECOVERS_IDEAL_MEMORY_WITH_CRITICAL_STORAGE_RATE_001_20261025.md .
- PRF12 R04 owns the exact n=3 endpoint difference, positive/negative spectral supports and loss of fixed local X: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R04_THREE_PROBE_FINITE_SWAP_EXACT_X_READOUT_GAP_AND_SECTOR_DECOMPOSITION_001_20261026.md .
- PRF12 R05, R10, R11 constructed successively 28, 10 and **9** positive rank-one PRODUCT effects attaining the same exact Helstrom value. R11: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R11_NINE_EFFECT_PRODUCT_SIMPLEX_MINIMAL_HELSTROM_REFINEMENT_001_20261026.md .
- PRF12 R06: exact finite-round three-party LOCC local first-node no-go, not extended in R12 to asymptotic closure.
- PRF12 R07's overstrong closure LOCC claim explicitly withdrawn by R09 due to an invalid replacement of the **refined full POVM** by a **coarse-grained binary decision pair**. Audit: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R09_COARSE_GRAINING_COHEN_THEOREM_AUDIT_AND_CORRECTED_CLAIM_CEILING_001_20261026.md .
- PRF12 R08 owns first exact adaptive local X→conditional X/Y→last-qubit Helstrom witness at q=1/3: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R08_EXACT_ADAPTIVE_LOCC_WITNESS_AND_DELTA_UPPER_BRACKET_001_20261026.md .
- Mature external hosts (no priority claims): Helstrom's optimal binary endpoint state test (1976); Welch/equiangular frames; Fickus, Jasper, King & Mixon, *Equiangular tight frames that contain regular simplices*, LAA 555 (2018), DOI https://doi.org/10.1016/j.laa.2018.06.004 ; Cohen, *Local approximation of multipartite quantum measurements*, PRA 105, 022207 (2022), DOI https://doi.org/10.1103/PhysRevA.105.022207 ; Kleinmann, Kampermann, Bruß, *Asymptotically perfect discrimination in the local-operation-and-classical-communication paradigm*, PRA 84, 042326 (2011), DOI https://doi.org/10.1103/PhysRevA.84.042326 ; Cohen, *Local approximation for perfect discrimination of quantum states*, PRA 107, 012401 (2023) and erratum PRA 108, 029902. These are external literature starting points and NOT a license to port their asymptotic theorems without checking outcome refinements and source assumptions.

## 1. Frozen exact mathematical fixture

Exactly n=3, equal ideal exposures T/3 with two instantaneous SWAP operations, input |+>^3, storage κ=0. Hypothesis A is ONE static Cauchy(0,γ) frequency shared over three exposures; B is independent increments of a symmetric Cauchy–Lévy source. Put q=γT/3>0, x=e^(−q), b=1−x², a=xb. The 8×8 endpoint difference is

 D_{u,v}(q)=1/8 [ exp(−q|Σ_j(u_j−v_j)|) − exp(−q Σ_j|u_j−v_j|) ].

Positive spectral projector P spans
 W=(|001>+|010>+|100>)/sqrt(3),
 Wbar=(|110>+|101>+|011>)/sqrt(3).

Q denotes the rank-four strictly negative spectral projector, K the rank-two kernel on 000 and 111. P+Q+K=I. D has STRICT nonzero eigenvalues on P and Q for every q>0. Hence exact endpoint binary Helstrom distinguishability is

 TV_Hel(q) = (1/2)||D(q)||_1 = b/2.                  (R12.1)

An exactly optimal full POVM with positive operators {F_l} may include any number of outcomes followed by a deterministic/randomized classical A/B decision. A nonzero fine effect assigned to A must have support contained in Q-perp=P⊕K; a nonzero fine effect assigned to B must be supported within P-perp=Q⊕K. If a fine effect is randomized across A/B, both nonzero labeled parts must be supported in kernel K. This is a consequence of positivity and strict signs in D, not a choice of a particular nine-effect implementation.

## 2. Theorem R12.1 — every optimal PRODUCT effect is automatically rank one

**Claim.** Let F=A⊗B⊗C≥0 be any nonzero product PSD effect in an exactly Helstrom-optimal fine-grained POVM. Then rank(F)=1. This remains true if we initially allow rank(A),rank(B),rank(C)∈{1,2} without restricting rank one.

**Proof.** The range of a product PSD operator is the tensor product of the factor ranges. If rank(F)>1, at least one local positive factor has full two-dimensional range. By party permutation, its range therefore contains the entire product slice

 S_bc = C²⊗span{|b>}⊗span{|c>}

for some nonzero qubit vectors |b>,|c> chosen from the other two ranges.

**A-labeled branch:** Q-perp=P⊕K is exactly the FULLY SYMMETRIC cube Sym³(C²), dimension 4. All nonzero product vectors in Sym³ are of the form |u>^{⊗3}, up to local scalars. S_bc cannot be contained in Sym³: |0,b,c> and |1,b,c> would both be fully symmetric nonzero product kets, forcing b and c to be proportional to |0> and |1> simultaneously. Contradiction.

**B-labeled branch:** P-perp={|W>,|Wbar>}^perp. If S_bc⊂P-perp, the inner products of |a,b,c> with W and Wbar vanish for BOTH independent choices |a>=|0>,|1>. Writing b=(b0,b1), c=(c0,c1), this requires

 b0*c0=0,   b1*c1=0,   b0*c1+b1*c0=0.

These three conditions say every coefficient of the polynomial

 (b0+b1*t)(c0+c1*t)

vanishes. C[t] is an integral domain, so either b=0 or c=0, contradicting the chosen nonzero vectors. Thus S_bc is not a subspace of P-perp.

**Kernel-only randomized branch:** K is a subspace of BOTH Q-perp and P-perp, so it is likewise incapable of containing any S_bc.

All cases exclude rank(F)>1; hence rank(F)=1. QED.

This is source-specific algebra for three qubits, not a general theorem about all product POVMs.

## 3. Theorem R12.2 — R11 minimality extends to ALL individual positive PRODUCT effects

R11 constructed nine explicit normalized product kets from ninth roots of unity, with pairwise |<v_i,v_j>|=1/8 and sum of weighted effects (8/9)|v_i><v_i|=I_8. Three positive-label outcomes sum to P+(2/3)|g><g| with g=(000+111)/sqrt(2), and six negative-label outcomes complete the measurement; TV=Helstrom for every q>0.

R11 originally proved N≥9 **assuming rank-one product effects**. By R12.1 every nonzero product effect in ANY EXACT Helstrom-optimal product-effect POVM is necessarily rank one. R11's remaining argument therefore applies without a rank hypothesis:

- Completeness in d=8 needs at least N=8 nonzero rank-one effects.
- If N=8, the weighted product rays are an orthonormal PRODUCT basis (square isometry is unitary).
- Any A-labeled ray must belong to Sym³(C²), hence is |u>^3. At most TWO such vectors can be mutually orthogonal on a qubit: <u³|v³>=<u|v>³.
- But P (rank 2) is not the span of only two symmetric product cubes, because P contains NO nonzero product ket at all: the |000> and |111> amplitudes of |u³> vanish only if u=0. Therefore at least THREE A-labeled product rays are necessary for exact Helstrom saturation.
- Contradiction if N=8; N≥9. The R11 construction attains 9.

\[
 \boxed{N_{\min}^{\rm individual\ PRODUCT\ PSD\ effects}=9
  \quad \text{for this exact endpoint source pair}.}     \tag{R12.2}
\]

**Strict scope**: "nine minimum" is about the count of fine-grained **individual product** effects, not the count of aggregated SEPARABLE effects (two suffice), local unitary gates, ancillary product degrees of freedom, arbitrary LOCC protocols, or device cost. No SEP/LOCC equivalence assumed.

**Finite-outcome corollary, with quantified caution.** Let C_8 be the set of all three-party POVMs with at most eight nonzero *individual positive product* effects, arbitrary allowed ranks, and arbitrary classical labeling A/B. It is a compact subset of finite-dimensional POVMs: write each nonzero product effect as t ρ1⊗ρ2⊗ρ3 with 0≤t≤8 and each ρj a one-qubit density matrix; pad zero effects as needed and impose the closed sum-to-I condition. R12.2 excludes equality with Helstrom everywhere on C_8, and the TV functional is continuous. Therefore for every fixed q>0,

 \[
 \boxed{\delta_{\rm PRODUCT,\le8}(q)
  := TV_H(q)-\max_{{\cal M}\in C_8}TV_{\cal M}(q) >0.}    \tag{R12.3}
 \]

No explicit numerical lower bound on this restricted gap is claimed. Since arbitrary LOCC may have MANY MORE than eight refined outcomes, R12.3 **does not imply** a positive gap for unrestricted/closure(LOCC). This avoids exactly the coarse-graining mistake documented in R09.

## 4. New exact formula: arbitrary equatorial sequential X–Y local projective readout

Now a separate constructive task. Three labs Alice, Bob, Charlie each hold one output qubit. Alice measures

 X(α)=cosα X + sinα Y,

obtains s=±1 and communicates it. Bob measures X(β_s) with β_+ or β_- selected by s and communicates t=±1. Charlie, holding only the last qubit, applies an optimal 2×2 Helstrom decision conditional on (s,t). Exactly EIGHT fine-grained rank-one product outcomes result, with no nonlocal gates or shared entanglement.

The Pauli expansion of the source difference is verified directly from the 8×8 D:

 D=(b/16) Σ_{j<k}(X_jX_k+Y_jY_k)
   +(a/32)(3X1X2X3+X1Y2Y3+Y1X2Y3+Y1Y2X3).             (R12.4)

Let cα=cosα, sα=sinα, cβ=cosβ_s, sβ=sinβ_s. After outcomes (s,t), the UNNORMALIZED signed conditional difference on Charlie is

 \[
 D_C^{s,t}=u_{s,t} I+v^x_{s,t} X+v^y_{s,t} Y, \tag{R12.5}
 \]
where
 u_{s,t}=(b/16) s t cos(α−β_s),
 v^x_{s,t}=(b/16)(s cosα+t cosβ_s)
          +(a/32)s t(3 cosα cosβ_s+sinα sinβ_s),
 v^y_{s,t}=(b/16)(s sinα+t sinβ_s)
          +(a/32)s t(cosα sinβ_s+sinα cosβ_s).

For a Hermitian 2×2 operator uI+vx X+vy Y, its trace norm is 2max(|u|,sqrt(vx²+vy²)). Hence the EXACT source-typed TV for this physically implementable one-way LOCC family is

 \[
 \boxed{TV_{\rm eq,1way}(q;\alpha,\beta_+,\beta_-)
 =\sum_{s,t=\pm1}\max\{|u_{s,t}|,\sqrt{(v^x_{s,t})^2+(v^y_{s,t})^2}\}.} \tag{R12.6}
 \]

R08 is the special case α=0, β_+=0, β_-=π/2. No global optimum over the three angles is claimed. Because D has only X/Y Pauli components on the first two parties, local projective axes with a Z component act for this signed-difference objective like a classical noisy version of the corresponding equatorial projective result. Thus restricting to the equator incurs no gain loss in this particular sequential projective family, but this says NOTHING about general local unsharp POVM or unlimited LOCC rounds.

## 5. New explicit finite-round witnesses for stronger phase signal

The analytic formula (R12.6) agrees with independent direct 8×8 source-matrix partial traces and four conditional 2×2 diagonalizations for all tested settings at machine accuracy (<6×10^-17).

Choose two SIMPLE, fully specified settings:

- At q=1.6: α=π/2, β_+=π/2−0.1, β_-=π/2+0.1.
- At q=2.5: α=π/2, β_+=π/2−0.04, β_-=π/2+0.04.

| q | unrestricted Helstrom | full fixed X | R08 fixed X→X/Y adaptive | R12 explicit equatorial adaptive |
|---:|---:|---:|---:|---:|
| 1/3 | 0.243291440484 | 0.189292628451 | 0.198464903476 | 0.198464903476 (R08 settings) |
| 1.6 | 0.479618898011 | 0.359714173508 | 0.359252615391 | **0.360920877083** |
| 2.5 | 0.496631026500 | 0.372473269875 | 0.365900341505 | **0.372681895172** |

At q=1.6, the R12 witness increases TV vs X by 0.001206703575; at q=2.5 by 0.000208625296. The margins are analytically reproducible via (R12.6), without Cauchy-tail quadrature or stochastic simulation. They do not certify a global optimum, nor an LOCC closure gap. R08 is still a better choice at q=1/3.

One may always choose a priori the BEST of the three explicit allowed LOCC strategies, giving an honest improvement in the achievable lower witness

 \[
 TV_{\rm LOCC}(q)\ge
 \max\bigl\{TV_X(q),TV_{\rm R08}(q),
 TV_{\rm eq,1way}(q;\pi/2,\pi/2-\theta,\pi/2+\theta)\bigr\}
 \]
for any chosen θ, e.g., θ=.1 or .04. This is an ACHIEVABILITY lower bound, not a prohibition of other LOCC protocols.

## 6. Reproducibility and review gates

Runnable independent code, Python 3 + NumPy:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-27/IW_PRF12_R12_PRODUCT_RANK_RIGIDITY_AND_EQUATORIAL_LOCC_REPRO_001_20261027.py

- Rebuilds R11's fixed nine ninth-root product kets; checks all 36 overlaps and frame closure.
- Rebuilds the source D(q) independently for q=.05,1/3,.7,1.4,3, checks SEP9=Helstrom.
- Computes three-party one-way readout by DIRECT 8×8 contraction with local Pauli projectors and by INDEPENDENT closed formula (R12.6), including new q=1.6 and q=2.5 witnesses.
- Rank-one rigidity is proved algebraically in §2 (polynomial integral-domain lemma); the program prints this critical condition but does NOT pretend Monte Carlo proves it.

**Independent referee tasks:** verify product-slice lemma for both positive and negative spectral supports, handle probabilistic labels and kernel, verify all eight-product compactness quantifiers, check Pauli expansion coefficients, signs of Y, conditional TV factors, and the absence of overreach to LOCC closure. Verify external source context and no public-novelty claim.

**Not solved:** explicit numeric lower bound on δ_PRODUCT,≤8(q), optimization of equatorial family, arbitrary adaptive POVMs, full LOCC/closure gap, source-active finite SWAP with fixed κ and hardware. No NCDG K/J3 physical interpretation, canon, EXEC or verified BW ingestion.

## 7. RETURN

PRF12_R12 / SOURCE_TYPED_PRODUCT_PSD_RANKONE_RIGIDITY_PROVEN_LOCAL / R11_NINE_OUTCOME_MINIMALITY_STRENGTHENED / FIXED_EIGHT_PRODUCT_OUTCOME_STRICT_GAP_EXISTENTIAL / EXACT_THREE_ANGLE_EQUATORIAL_LOCC_FORMULA / NEW_Q1_6_Q2_5_LOCC_WITNESSES / TWO_INDEPENDENT_MATRIX_ROUTES_PASS / REFEREE_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC / FULL_LOCC_CLOSURE_GAP_OPEN / GITHUB_PENDING_BW_INGEST.
