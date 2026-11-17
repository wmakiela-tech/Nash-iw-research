---
artifact_id: IW_LT9_ROT002_WUXU_PION_CHARGE_AGGREGATION_OBSERVABLE_QUOTIENT_OBSTRUCTION_SOURCE_NATIVE_EXACT_WITNESS_001_20261117
date: 2026-11-17 Europe/Warsaw
cell: IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_07 / LT9
document_type: BOUNDED_SOURCE_NATIVE_MATHEMATICAL_THEOREM_AND_FALSIFIER
exposure: PUBLIC
status: SOURCE_ALGEBRA_EXACT_PASS / FULL_PHYSICS_NOT_TESTED
source_1: https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl
source_1_blob: b368ba55d5a493f7bc185909730f7fe5691f10d6
source_2: https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/tool_script-parameters.jl
source_2_blob: 0d7198ff3557bdbd5753000bb07a7a7405cc24f5
source_3: https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/tool_script-hadrons_from_PBH.jl
source_3_blob: cc73432910f872d526113ce59b6204f38d0766a9
parent_work: IW_LT9_ROT001_WUXU_B1_QB_T3_VERSION_CHARGE_NORMALIZATION_MATURE_HOST_PRIOR_ART_001_20261116
claim_ceiling: ORIGINAL_WUXU_CODE_STRUCTURE_ONLY / CLASSICAL_QUOTIENT_TEST / NO_NUMERIC_BBN_BOUND / NO_PAPER_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
native_execution: NONE
symbolic_execution: RETROSPECTIVE_SYMPY_EXECUTION_IN_LT9_ROT003_20261117
sync_state: GITHUB_PENDING_BW_INGEST
bw: NO_WRITE
book_rev029: NO_EDIT
---

# LT9 ROT002 — exact observable non-closure of the pion group quotient in original Wu–Xu 10D source

## A. Scientific question / non-duplication

After the bounded T3 prior-art and source review (LT9 ROT001), an important scientific ambiguity is NOT resolved by T1 grouped generation alone: whether a *total pion group rate* can be treated as a sufficient state/source for the `n <-> p` observable without an explicit charge allocation. XH-S7 ROT001 independently identified the doubled source bookkeeping, and LT9 ROT001 identified the source definition boundary. This ROT002 is a **different mathematical deliverable**, a source-native rigorous counterexample to any proposed reduction that keeps only `n_pi_minus+n_pi_plus` while discarding their charge split. No firstness claim for generic lumpability or realization theory, and no T2R physics.

**RESULT:** For the literal original source equations, the projection to `(X_n, n_pi_minus+n_pi_plus, all non-pion coordinates)` has **NO well-defined autonomous vector field on the full strictly positive, above-clamp state domain**, at any positive finite temperature, whenever physically meaningful pion rates are used. The retained neutron fraction's derivative directly resolves the hidden charge-antisymmetric mode. This is an exact failure of quotient/lumpability, not a validation that the published numerical PBH bound is wrong.

## B. Source identities (direct original commit d395183 read)

Author `main-scan.jl`, `evolution_system!`:
```julia
dXₙ_dt_π = (1 - Xₙ) * n_π⁻ * σv_π⁻_pTOn(T_SM) - Xₙ * n_π⁺ * σv_π⁺_nTOp(T_SM)
d_n_π_dt_from_PBH = dN_over_dt_π(m_PBH) * n_PBH
d_n_π⁻_dt = d_n_π_dt_from_PBH - Γ_π⁻ * n_π⁻ - σv_π⁻_pTOn(T_SM) * (1 - Xₙ) * n_B * n_π⁻
d_n_π⁺_dt = d_n_π_dt_from_PBH - Γ_π⁺ * n_π⁺ - σv_π⁺_nTOp(T_SM) * Xₙ * n_B * n_π⁺
```
Here these are the source's actual **physical neutron fraction derivative** and pion density dynamics; the integrated logarithmic coordinates include the `1/(H*X_n)` factor for the neutron coordinate. The `exp(max(log(n), -100))` implementation enforces a floor; all mathematical witnesses below choose **strictly positive densities above that floor**, so the floor does not invalidate the exact counterexample.

The author's original `tool_script-parameters.jl` implements:
```julia
σv_π⁺_nTOp(T) = 1.7mbarn
σv_π⁻_pTOn(T) = 1.5mbarn * Fc_π⁻(T)
```
with `Fc(T,m_h)=x/(1-exp(-x))`, `x=2π α_EM/(sqrt(T/m_h)+sqrt(T/m_p))>0` for `T>0`. Therefore `Fc>1` (finite positive T), hence both `σ_-` and `σ_+` are strictly positive, with `σ_->1.5mbarn`, `σ_+=1.7mbarn`. All units and source rates remain as the original author code; these are coefficients of the author model, not independently measured experimental cross-sections.

The actual interpolated single pion group-rate function is `dN_over_dt_π(m)` from column 2 of `hadrons_from_PBH.dat`. The same group function appears in **both** charge-resolved pion density ODEs in the original source. If `R=dN_over_dt_π*n_PBH`, the literal two-state code total **pion injection** equals `R+R=2R`. The separate Mech-S9 T1 25/25 original BlackHawk source receipt established `R` as a grouped-particle/antiparticle generator rate; this result is inherited external source evidence, not rerun by LT9. The physical adequacy of the literal source map remains a separate owner/reviewer decision.

## C. Exact theorem — no autonomous pion-group reduction

Let all background and non-pion state coordinates be fixed identically in two admissible states at a common time: `T>0`, `0<X<1`, `n_B>0`, same PBH mass, H, initial context and other hadron populations. Write `a(T)=σv_π⁻_pTOn(T)>0` and `b(T)=σv_π⁺_nTOp(T)>0`. The original pion term is exactly

`P(X,n_-,n_+;T)=(1-X)*a(T)*n_- - X*b(T)*n_+`.

For any `c>epsilon>0` with `c-epsilon` above the literal source density floor, choose states A and B:
`(n_-^A,n_+^A)=(c+epsilon,c-epsilon)`;
`(n_-^B,n_+^B)=(c-epsilon,c+epsilon)`.
They have identical pion aggregate `g=n_-+n_+=2c` and identical projection `z=(X,g,all other non-pion coordinates)`.

Nevertheless,
```
P(A)-P(B)
 = (1-X)*a*[(c+eps)-(c-eps)] - X*b*[(c-eps)-(c+eps)]
 = 2*eps*((1-X)*a + X*b)
 > 0.
```
No other term in `dX_n/dt` changes, so the literal neutron derivative differs. Because `mbarn>0`, the strict positive lower bound `P(A)-P(B) > 2*epsilon*(1.5mbarn)` follows for `0<=X<=1` from `a>1.5mbarn`, `b=1.7mbarn`. The original log-state `dlogX_n/dη` differs by the same positive amount divided by `H*X` at equal `H>0`, `X>0`.

Suppose an autonomous exact reduced vector field `Fbar(z)` existed whose neutron component agrees with both full-state dynamics after aggregating pion populations. Since the two initial states have identical `z`, `Fbar(z)` would give the same neutron derivative. The exact calculation above gives distinct derivatives. Contradiction.

**Conclusion:** the projection discarding the pion charge imbalance `d=n_- - n_+` is not a well-defined full-state dynamical quotient. A grouped source `R_pi` does not by itself determine the retained neutron-fraction evolution absent a charge-split law or additional dynamical state / validity restriction. This is the standard quotient/factorization criterion applied to the original Wu–Xu code; NOT novel general mathematics.

The same source also gives the group equation:
`dg/dt = 2R - Γ_pi*g - n_B*((1-X)*a*n_-+X*b*n_+)`.
It separately fails closure on `g` for most `X` because individual loss coefficients differ. Even at any exceptional `X` where this *group* loss difference vanishes, the neutron derivative witness above remains strictly nonzero.

## D. Algebraic sanity-check — execution provenance corrected retrospectively

**Dated correction (LT9 ROT003, 17 November 2026):** ROT002 was initially published without an actual SymPy execution, despite the assertion below. The exact symbolic checks were subsequently executed in LT9 ROT003 using local Python/SymPy 1.14.0. The results below are now verified, but were **not** verified by SymPy before ROT002's initial publication. The original overclaim is explicitly acknowledged rather than silently backdated.

The subsequent actual SymPy execution established:
- `P(A)-P(B) = 2*epsilon*((1-X)*a + X*b)` PASS.
- `(dg/dt)(A)-(dg/dt)(B) = -2*epsilon*n_B*((1-X)*a-X*b)` PASS.
- Illustrative rational coefficient witness (not a physical measured T): `X=1/2, c=2, epsilon=1, a=3/2, b=17/10` gives `P(A)=7/5`, `P(B)=-9/5`, and difference `16/5`. These exact rationals provide arithmetic diagnostics only. Since actual finite-T `Fc>1`, the source-native strict witness is the symbolic positive proof above, not the limiting coefficient example.

**No actual Julia, BlackHawk, PBH source trajectory, new T2R numerical replica, or new Yp computation was executed.**

## E. Physical / methodological boundaries and source next gate

1. The literal author 10D code is completely defined: it expressly maps the single group source `R` into two named charge species. This theorem does **not** call that code mathematically ill-defined. It shows a proposed *coarser grouped physical interpretation* is underdetermined without an externally justified split convention. Source implementation and physical meaning must not be conflated.
2. `R=R_++R_-` together with an **extra** charge symmetry assumption `R_+=R_-` gives `R_+=R_-=R/2` for that pair. Symmetry is an added physical/source assumption; it does not follow from the aggregate table alone, especially for lone anti-baryon/kaon channels.
3. Even source-level factor two is **not** automatically an exact factor two in endpoint `Y_p` or `β(M)`: charge-opposite neutron effects, species losses, PBH time profiles, weak rates, solver tolerance and the actual paper/version observable intervene. Existing Badacz E5 native `D=0.2723..0.3007 dex` is an actual owner result conditional on T1/T3/T2R, not derived by this theorem.
4. This is not a claim of a Wu–Xu paper error, physical BBN or PBH exclusion curve, novel physical law, nor a justification for contacting the authors unilaterally. Actual original source and full source paper version parity, source normalization and independent native replica remain scientific owner/reviewer gates.
5. **One cheap next discriminant** for native owner + REC13/AUD3: pin an explicit *charge-conditioned hadron yield* convention (preferably from original official generator species IDs or author's documentation), and show whether it defines `R_-`, `R_+` or a suitable group-averaged reaction coefficient. If unavailable, retain `Q_B_SOURCE_DEFINITION_HOLD`, not a physics theorem closure. No new native run authorized here.

## F. Firstness, conservation of negative knowledge and delivery

- Authors Wu/Xu own the exact equations; authors Arbey/Auffinger own the original BlackHawk.
- Mech-S9 owns the official grouped 25/25 T1 technical firstness; Badacz owns E5 native 232-call T2 and Q-A native; XH-S7 independently did the straightforward doubled-input rate audit. LT9 ROT001 did the inherited independent T3 review. No science-result originality is claimed for a generic algebraic quotient obstruction, which is standard realization / lumpability theory.
- Evidence typed: `SOURCE_NATIVE_EXACT_LOCAL_COUNTEREXAMPLE / ORIGINAL_CODE_READ / SYMPY_VERIFIED_RETROSPECTIVELY_IN_ROT003 / NO_NATIVE_RUN / NO_PHYSICAL_CLAIM`.
- Return: one decision-relevant negative result, with STOP (do not extrapolate group-total into a unique charge-resolved observable model) and REOPEN (explicit physical split or averaged σ source).
- BW NO_WRITE, REV029 NO_EDIT, NO_NOVELTY/NO_CANON/NO_EXEC_SIGN.
