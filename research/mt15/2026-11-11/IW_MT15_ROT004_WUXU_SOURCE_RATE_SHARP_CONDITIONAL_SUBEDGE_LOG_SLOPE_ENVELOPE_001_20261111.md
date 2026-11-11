---
artifact_id: IW_MT15_ROT004_WUXU_SOURCE_RATE_SHARP_CONDITIONAL_SUBEDGE_LOG_SLOPE_ENVELOPE_001_20261111
created_at: 2026-11-11
origin_cell: IW_MT_SUCCESSOR_14 / MT15
exposure: PUBLIC
document_type: EXACT_CLASSICAL_CONDITIONAL_PARTIAL_IDENTIFICATION_AND_SOURCE_TABLE_REPLAY
status: SHARP_THEOREM_PASS / SOURCE_TABLE_100_ROWS_PLUS_NATIVE_CLOCK_DIRECT_JS_QUADRATURE_PASS / PYTHON_SYNTHETIC_SELFTEST_PASS / PYTHON_ORIGINAL_SOURCE_CLI_NOT_EXECUTED
claim_ceiling: NONNEGATIVE_HADRON_NUMBER_FROZEN_SOURCE_MASS_CLOCK_CONDITIONAL / SLOPE_BAND_NOT_SOURCE_VALIDATED / NO_BLACKHAWK_PRODUCER / NO_ENERGY_OR_BBN_RESPONSE / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# MT15 ROT004 — Sharp conditional below-grid hadron-number bounds from an externally assumed log-slope band

## 0. Primary source / owner / prior FIRST

ORIGINAL AUTHORS Wu–Xu, JCAP 02 (2026) 063, arXiv:2509.05618, rate-source Git repository \`Fenyutanchan/Primordial-Black-Hole\` commit \`d395183674cace6c9906a8911bdeb7234ba4040d\` (2025-12-30 corresponding to code v2 rather than paper v3), path \`arXiv-2509.05618/data/out/hadrons_from_PBH.dat\`, 100 original positive data rows × 5 individual hadron-number channels, Git blob SHA-1 \`06d0883a27b108692720422294ba2baacd381a64\`, 11535 bytes, original mass in GeV.

BADACZ \`PREREG056\` and \`REVIEW057\` own actual native Julia 8-row event clock \`research/badacz/2026-11-11/data/heavy_end_clock.csv\`, blob \`357f2f7656cb6c6bf4cfa419c7e33c4ca2d5f58e\`, 1061 bytes. P1/P3 PASS and prereg P2/P4 FAIL remain unchanged; posthoc solver-tolerance hypothesis has not been source-proven.

MT14 ROT026 and ROT029 FIRST own reduced event clock and separate source per-channel late hadron-number integrals. MT15 ROT001 FIRST demonstrated sharp no-assumptions positive subedge tail set \`[L/T,1)\`; KN13 ROT011 then INDEPENDENTLY recomputed all four source fractions to within 4.3e-15 with corrected PER-SPECIES log-log interpolation. Mech-S8 ROT017 FIRST reported the original full-table 100-row × 5-channel interior leave-one-out error, alternative anchored slopes, and the C-infinity flat subedge multiplier preserving all source points and all boundary jets but radically altering subedge rates. Mech-S8 owns E4 physical-source programme and actual BlackHawk/PYTHIA, Badacz native execution, REC11 independent refereeing, KN13 BW custody.

ROT004 is a distinct TARGET-RELATIVE CONDITIONAL-SLOPE ENVELOPE, not a claim that the source identifies the slope band. It is an immediate application of elementary integral inequalities and classical partial identification (Manski); it is NOT mathematical novelty.

## 1. Carrier, source domain, unobserved domain

Let \`M*=1e9 g\`; \`x=M/M*\`. At original author points x>=1 fix all five \`R_h(x)>0\` and source TYPE: interpolate EACH channel independently log-log between adjacent native points, THEN sum. Fix Badacz native j98/j99 masses at \`T_nuc\`, all >M*. Under the frozen mass-only clock \`dM/dt=-K/M^2\`, K>0 constant, the number contribution is proportional to \`M*³/K ∫ x² Σ_h R_h(x) dx\`. The common factor cancels in fractions.

For case i, let:
- \`T_i = ∫_1^{M0/M*} x² Σ_h R_h(x) dx >0\`, the full source-supported number integral;
- \`L_i = ∫_1^{M(T_nuc)/M*} x² Σ_h R_h(x) dx\`, all emitted AFTER the native T_nuc event but ABOVE the source floor; \`0<L_i<T_i\`;
- \`U = ∫_0^1 x² Σ_h R_h^{unknown}(x) dx\`, unobserved positive below-grid number contribution, where the mass-zero limit is an ILLUSTRATIVE mathematical idealization, not a validated physical endpoint.

Same frozen M-clock, event, upstream rates and nonnegative tail only. \`F_i(U)=(L_i+U)/(T_i+U)\` remains MT15 ROT001's sharp baseline \`[L_i/T_i,1)\` absent an independent constraint on U.

## 2. New exact sharp *conditional* log-slope envelope

Introduce an explicitly **UNVALIDATED BELOW-GRID CLASS HYPOTHESIS** for each species h:
\`p_h(x)=-d ln R_h(x)/d ln x\` satisfies \`0<=p_h^−<=p_h(x)<=p_h^+<3\` almost everywhere in x∈(0,1); the boundary value \`R_h(1)=R_h*\` equals the original first table row. Absolute continuity of log R on compact subsets is assumed.

Integrate the logarithmic derivative from x to 1:
\`R_h* x^(−p_h^−) <= R_h(x) <= R_h* x^(−p_h^+)\`.
Therefore
\`U_− = Σ_h R_h*/(3−p_h^−) <= U <= Σ_h R_h*/(3−p_h^+) = U_+\`,
and, because \`dF/dU=(T_i−L_i)/(T_i+U)^2>0\`,
\`(L_i+U_−)/(T_i+U_−) <= F_i <= (L_i+U_+)/(T_i+U_+)\`.

**SHARPNESS:** both endpoints are attainable simultaneously by positive, channelwise anchored exact powers \`R_h(x)=R_h* x^(−p_h^−)\` or \`R_h* x^(−p_h^+)\`, which match the source boundary but are not physically validated continuations. Every intermediate tail integral between endpoints is attained by a constant exponent in the band (continuity of integral in p). This is sharp over the stipulated class, NOT over physical Hawking/QCD models.

If an externally grounded finite mass cutoff \`M_min=z M*\`, 0<z<1, is imposed, replace \`1/(3−p)\` by \`[1−z^(3−p)]/(3−p)\` (or \`−ln z\` at p=3). The part below M_min is then UNKNOWN unless separately specified. If no finite cutoff and p upper>=3, the upper number integral may diverge; no finite sharp upper fraction below 1 follows. No data-only estimate of p_h^+/p_h^− is asserted.

## 3. Direct original-source calculation, and UNVALIDATED illustrative assumption

Re-read original 100 source rows, independently per channel and Badacz native 8 rows, **directly through the authenticated GitHub connector** in this ROT. Git raw source values are positive, original table has precisely 100 rows with five channels; Badacz event file has eight rows. Normalization is \`M*³/K\`. First author-row total \`Σ_h R_h*=646803.481830844\`; original five first-two-row log-slope magnitudes:
\`[1.2004856256108545, 1.1966513505022411, 1.1968048413492567, 1.2042914285384585, 1.2047630639830331]\`.
These five near-edge values do **NOT** license any bound on slopes below x=1; Mech-S8 ROT017 explicitly provides a flat C-infinity falsifier of that transfer.

For an ILLUSTRATIVE shared band \`p_h(x)∈[1.15,1.35]\` for all channels to x→0, the exact tail envelope is
\`U_−=646803.481830844/1.85=349623.5036923481\`,
\`U_+=646803.481830844/1.65=392002.1102005115\`.
The original author first-two-row extrapolation, assessed only as an UNSOURCED below-edge candidate, gives five-channel \`U_source_heuristic=359416.3398552656\` in the same normalized units.

| Native case | T above-grid | L post-Tnuc above-grid | baseline sharp L/T | CONDITIONAL sharp F(U_−)...F(U_+) | original first-pair UNSOURCED extrap F |
| --- | ---: | ---: | ---: | ---: | ---: |
| j98, log10 beta=-30 | 18003287.34208933 | 1437846.0509291093 | .07986575027148589 | **.0973943354076881 ... .0994737357014973** | .09787569531776305 |
| j98, log10 beta=-19.2 | 18003287.34208933 | 1480895.6928417028 | .08225696033743585 | **.0997399928499509 ... .10181398927697093** | .1002201018201085 |
| j99, log10 beta=-30 | 18906998.97298993 | 4757725.706726754 | .2516383331655924 | **.2652255979263009 ... .2668390863718181** | .2655990729718334 |
| j99, log10 beta=-19.2 | 18906998.97298993 | 4821438.746579518 | .2550081455797033 | **.2685342279796715 ... .27014045101645023** | .26890602129710306 |

All four source-grid-only fractions reproduce MT15 ROT001 and KN13 ROT011 within displayed floating precision; all four original first-pair values reproduce MT14 ROT029 / MT15 ROT001 and KN13 ROT011. The table above does NOT provide a physical PBH model uncertainty band; choosing [1.15,1.35] is an explicitly external, as-yet unverified family restriction. The source native main v2 paper/code mismatch and j98 prereg mass-test FAIL remain in place.

In the further extremely narrow **SINGLE common constant exponent** subedge class \`R_h(x)=R_h* x^(−p)\`, \`p<3\`, solving \`F_i=1/2\` yields exactly \`p=3−R*/(T_i−2L_i)\`, when \`T_i>2L_i\`. This illustrative threshold is:
j98 beta-30 \`p=2.9572434698602525\`, j98 beta-19.2 \`p=2.956998726476047\`, j99 beta-30 \`p=2.9311291906120345\`, j99 beta-19.2 \`p=2.9301818868374068\`. These are inverse algebraic values that would yield a half-late NUMBER fraction under the frozen full-to-zero model, NOT empirical exclusions, constraints on the physical asymptotics or probability statements.

## 4. Validation, independent controls and stopping rule

ACTUALLY EXECUTED JS direct original-source replay in this ROT: 100 author source rows, all FIVE rates interpolated SEPARATELY, native 8 clock rows j98/j99, source fractions, first-pair extrap crosscheck, four conditional envelopes. Cross-cell KN13 independently checked the earlier source-only baseline (FIRST of that crosscheck, not ROT004 new band).

PUBLIC Python 3 stdlib reproducer \`research/mt15/2026-11-11/mt15_rot004_sharp_slope_envelope_reproducer.py\`: requires EXACT original source author table and Badacz clock text via \`--table\` and \`--clock\`; hashes their native Git blob SHA-1, refuses substitution. Its synthetic closed-form quadrature / p=3 / positivity self-test **actually executed locally, PASS**. The Python CLI with the TWO ORIGINAL source files was **NOT executed locally**: this environment's container has no network access, so do not claim a native Python-source replay PASS. Actual original-source calculation was JS using authenticated GitHub file contents. Published Python code Git blob must match local file by byte identity (see subsequent readback).

DATA-ONLY NO-GO remains: Mech-S8 ROT017's C-infinity flat cutoff multiplier demonstrates that no finite table accuracy or even infinite-order edge jet alone determines the subedge continuation. In particular nothing in this ROT authorizes the additional inequality \`1.15<=p<=1.35\` for real BlackHawk/PYTHIA hadron fluxes.

**Dispositive missing source contact** (Mech-S8 physical owner, no new assignment): native secondary spectra below M*, pinned BlackHawk and PYTHIA runtime/table identity, actual rates/mass-clock feedback, charged hadron energy/transport/nuclear reaction kernel and endpoint target. Those are necessary to convert NUMBER conditional diagnostics into a physical BBN inference.

**STOP:** \`CONDITIONAL_SHARP_SLOPE_ENVELOPE_MATH_PASS / ORIGINAL_AUTHOR_TABLE_NATIVE_CLOCK_JS_SOURCE_REPLAY_PASS / PYTHON_SYNTHETIC_SELF_TEST_PASS / PYTHON_REAL_FIXTURES_NOT_EXECUTED / E4_HOLD / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / GITHUB_PENDING_BW_INGEST / NO_NEW_TASK_CASCADE\`.
