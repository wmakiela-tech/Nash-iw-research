---
artifact_id: IW_MT15_ROT007_WUXU_NODE_MONOTONE_LATE_NUMBER_SHARP_INTEGRAL_BOUND_001_20261111
created_at: 2026-11-11
origin_cell: IW_MT_SUCCESSOR_14 / MT15
document_type: ORIGINAL_SOURCE_TYPED_CLASSICAL_SHARP_PARTIAL_IDENTIFICATION
exposure: PUBLIC
status: SOURCE100_FIVE_RATE_BOTH_NATIVE_CLOCK_VERSIONS_JS_PASS / EXACT_MATH_PROOF / SYNTHETIC_STEP1600_PASS / LOCAL_PYTHON_SYNTHETIC_STEP250_PASS
claim_ceiling: NODE_ONLY_MONOTONE_RATE_INTERPOLANTS_FIXED_MASS_CLOCK / NO_HAWKING_GENERATOR_TRUTH / NO_Yp_OR_BBN_RESPONSE / NO_PHYSICAL_PBH_BOUND / NO_MATHEMATICAL_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# MT15 ROT007 — Sharp late hadron-number integral bounds from original 100-node monotonicity alone

## Sources, scientific priority and previous results

Original physics: Wu–Xu, JCAP 02 (2026) 063, arXiv:2509.05618. Frozen author public Git code v2 Fenyutanchan/Primordial-Black-Hole commit d395183674cace6c9906a8911bdeb7234ba4040d, original data/out/hadrons_from_PBH.dat Git blob 06d0883a27b108692720422294ba2baacd381a64. Exactly 100 source mass rows and FIVE positive hadron total-number rate groups. The code v2 is NOT presumed byte-identical to the paper v3 execution. Mech-S8 owns physical E4 and complete original BlackHawk/PYTHIA provenance.

Native events FIRST Badacz REVIEW057 r1, default 8-row clock blob 357f2f7656cb6c6bf4cfa419c7e33c4ca2d5f58e; REVIEW057 r2 posthoc reltol=1e-4 6-row clock blob e0759b4a22c3282d3f11c58412c4b6543e6dc4c7. Original owner prereg P1/P3 PASS and P2/P4 FAIL not overwritten. Badacz REVIEW059 separately verified native A1 failure at j22. These are MODEL_INTERNAL rows, not observational constraints.

Prior research FIRST: MT14 ROT029 original five-channel log-log source quadratures; MT15 ROT001 sharp conditional arbitrary nonnegative subedge number tail; MT15 ROT004 illustrative but UNVALIDATED below-edge log-slope p-band; MT15 ROT006 posthoc clock numeric sensitivity; KN13 ROT011/013 independent source-rate/clock reviews. Mech-S8 ROT017 original all-100 LOO and C-infinity below-edge nonuniqueness; AUD1 ROT038 FIRST strict monotonicity of all 495 adjacent source transitions and C-infinity positive decreasing INTERGRID countermodels. Mech-S8 ROT018 FIRST 2,225 known-data masked h-step backtests (different problem and observable). INT9 ROT012/013 own energy/linear target gates. No mathematical novelty beyond mature classical Darboux integration, Stieltjes step mixtures and linear-fractional optimization.

NEW TARGET: Fix all original source nodes and native event masses. Change only the unknown functions BETWEEN these nodes under positivity and monotonic decrease as mass increases, not the source author code's prescribed log-log interpolant. What are mathematically SHARP partial-identification bounds for the above-grid late NUMBER fraction?

## Typed theorem: exact monotone node-only sharp inf and sup

Source masses in grams M_i, with Mstar=M_0=1e9 g. Normalize x=M/Mstar and the original five channel rates R_h(x). Assumptions: at each original node the rates equal original source values, all node-to-node values satisfy R_{h,i}>R_{h,i+1}>0; on every cell [x_i,x_{i+1}] each hypothetical interpolating R_h(x) is positive and nonincreasing with x. No bound on derivatives, curvature or slope; arbitrarily narrow smooth strictly decreasing transitions permitted.

Freeze native event t=M(Tnuc)/Mstar and initial mass m=M_init/Mstar, with 1<t<m<x_99. Mass-only carrier dM/dt_phys=-K/M^2, K>0, common K cancels. Define:
L = integral_[1,t] x^2 sum_h R_h(x) dx (post-event late count);
E = integral_[t,m] x^2 sum_h R_h(x) dx (earlier count);
F = L/(L+E). No subedge M<Mstar source included at this stage.

For any cell [x_i,x_i+1] cropped to [a,b]=intersection with [1,m], let U_i=sum_h R_{h,i} (high LEFT-node rate), V_i=sum_h R_{h,i+1} (low RIGHT-node rate), and W(a,b)=(b^3-a^3)/3.

Define sums for full cells strictly BELOW the event (a late cell):
Llo=sum_late V_i W(a,b), Lhi=sum_late U_i W(a,b).
For full cells strictly ABOVE the event (an early cell):
Elo=sum_early V_i W(a,b), Ehi=sum_early U_i W(a,b).

One source cell straddles t for each of the 8 actual native cases. For it write U,V and Wl=W(a,t), We=W(t,b). Then the exact sharp global extrema are:

  f_v = (Llo+V Wl)/(Llo+V Wl+Ehi+V We).
  f_u = (Llo+U Wl)/(Llo+U Wl+Ehi+U We).
  inf_F = min(f_v,f_u).
  sup_F = (Lhi+U Wl)/(Lhi+U Wl+Elo+V We).

The extrema are attained in the closure by increasingly steep smooth strictly decreasing node-matching profiles; they need not be attained by a continuously differentiable interpolant with bounded derivative.

Proof: Fraction F strictly increases with L and strictly decreases with E. On a cell entirely late, choose the lower node rate V for infimum and upper U for supremum; on an early cell the reverse. In the crossing cell, represent each nonincreasing profile as a Stieltjes mixture of steps from its left endpoint value u to right endpoint value v. For an elementary step at s<t the crossing EARLY count is fixed v We and LATE count grows as s increases, so F increases. For a step at s>t the crossing LATE count is fixed u Wl and EARLY count grows as s increases, so F decreases. Therefore upper F uses a step at s=t (u late/v early), while lower F uses a step immediately at a or immediately at b (all v or all u in the cell interior). The five species have the same crossing-cell Wl and We, so for the lower endpoint their combined crossing contribution depends only on aggregate interior rate R in [V,U]. The linear-fractional F is monotone in R, attaining its infimum at one of V,U. Independent cell extrema can be approximated simultaneously by narrow C-infinity transitions preserving every node value, and dominated convergence transfers them to the integrals. QED. This is classical monotone moment optimization; novelty is not established or claimed.

If t equals a source node exactly the crossing-cell case is absent; use separate noncrossing sums. None of the eight actual owner clocks requires this degeneracy.

## Executed original 100x5 source data and both native event clocks

Rows: SOURCE author 100x5, exact original Git blob 06d0883; strict adjacent rate monotonicity 495/495 PASS. The eight numerical cases came from both frozen native Badacz clocks. Each reported interval concerns ONLY above-1e9g number; the author code's specific FIVE-SEPARATELY-interpolated log-log fraction is inside it.

| Clock | j | log10 beta | Exact inf F | Exact sup F | Actual author-code log-log F |
| --- | --- | --- | --- | --- | --- |
| DEFAULT | 98 | -30 | 0.07222391761949264 | 0.08825020889783335 | 0.07986575027148587 |
| DEFAULT | 98 | -19.2 | 0.07449636815991842 | 0.09091835714696901 | 0.08225696033743583 |
| DEFAULT | 99 | -30 | 0.23225058693607797 | 0.27305319613862095 | 0.25163833316559240 |
| DEFAULT | 99 | -19.2 | 0.23559900229534267 | 0.27649142307639790 | 0.25500814557970330 |
| POSTHOC 1e-4 | 98 | -30 | 0.06630529157881943 | 0.08107111610413598 | 0.07342442178903677 |
| POSTHOC 1e-4 | 98 | -19.2 | 0.06597953333073808 | 0.08067567025003687 | 0.07306020931817923 |
| POSTHOC 1e-4 | 99 | -30 | 0.23136945985774476 | 0.27214801531166016 | 0.25074621764347693 |
| POSTHOC 1e-4 | 99 | -19.2 | 0.23133966771645330 | 0.27211740681913676 | 0.25071601442815517 |

Event crossing grid cells numbered from 1 at Mstar: j98 crosses 11 or 12 according to mass and clock, j99 crosses cell 19. Each author log-log fraction is STRICTLY inside its independent node-monotone range.

Two-clock FINITE-SCENARIO envelope, not a certified solver-error band: beta -30 j98 [0.06630529,0.08825021], j99 [0.23136946,0.27305320]; beta -19.2 j98 [0.06597953,0.09091836], j99 [0.23133967,0.27649142]. This does NOT cover other unknown tolerances or physical mass trajectories.

A separate arbitrary below-grid nonnegative hadron NUMBER tail Z>=0, all after Tnuc, changes full ratio to (L+Z)/(L+E+Z), strictly increasing with Z. Therefore the sharp node-only source-supported INF above is also a mathematical lower bound when arbitrary nonnegative tail is added under the FROZEN clock; but the global SUP for unrestricted finite Z is 1 (not attained). Do NOT misinterpret the above-grid upper fractions as total observable or physical error bars.

The monotone-class interval widths are about 1.47–1.64 percentage points for j98 and ~4.08–4.09 percentage points for j99, larger than the between-run shifts of the log-log reference. This is worst-case **SOURCE-CLASS width**, not measured or validated real generator error.

## Actual controls and reproducibility limitations

1. Executed direct authenticated GitHub JS 100 original author rows, five separately preserved source-rate channels, 8 default/posthoc native j98/j99 event inputs, EXACT independent weighted x^2 cell quadratures. Confirmed source original per-channel log-log outputs inside ALL 8 monotone sharp intervals. All 495 node rate transitions positive and strictly decreasing.
2. An independent source-anchored JS finite-step checker sampled 200 choices of 99x5 step locations and computed each of eight late/early mass integrals with a different step-weighted algorithm: 1,600/1,600 hypothetical monotone ratios within certified analytic bounds. These finite checks are NOT a proof; the proof is above.
3. Local expanded Python stdlib reproducer at /mnt/data/mt15_rot007_monotone_table_integral_bounds.py, SHA256 1bfc185e6426faefe3a63106411ad4a08e5b8c6ccc74e528bd27184fc024ab8c, source-blob hash locking; its SYNTHETIC 250-step unit selftest actually executed and PASS. Original source fixtures not mounted locally, so Python original-source CLI was NOT executed; original source data WERE executed via GitHub JS tool. No false Python-native pass.
4. Public compact source-locked Python stdlib reproducer in same research directory: mt15_rot007_monotone_table_integral_bounds_public.py, Git blob 66d73ef9d63ca90a4f2c7d3155ae949ff7922b7c, full exact GitHub readback PASS. NOT the byte-identical version of the longer local self-tested Python script. Full original runtime Python replay NOT CLAIMED.
5. Public eight-case JSON file mt15_rot007_monotone_node_source_results.json, Git blob bd8af5686fe18709a2e3c60a4efac7d07943c01a, full exact GitHub readback PASS.

## Negative knowledge, source contact and execution gate

Author source v2 actually FIXES log-log interpolation; this theorem concerns counterfactual positive nonincreasing continuations sharing all original node values, not a diagnosed numerical error of author code. Monotonicity between nodes is itself a MODEL-CLASS restriction, not proven for unseen physical BlackHawk/PYTHIA generator output. Even the strictly positive lower fraction is model-number-only and frozen mass-clock conditional, NOT a late nuclear response or physical Yp correction.

Mech-S8 owns physical E4 and author generator-source closure; Badacz owns actual Julia, native source clocks and PREREG060 ramp. INT9 owns target-response theory; REC11/AUD1 external scoped reviews; KN13 source custody. No task reassignment or automatic new execution from this note. No verified full-spectrum energy/charge/BBN transfer, no physical PBH beta bound, no CANON or EXEC_SIGN.

END: EXACT_CLASSICAL_NODE_MONOTONE_SHARP_FRACTION / DIRECT_AUTHOR_AND_BOTH_CLOCKS_JS_PASS / 1600_MONOTONE_STEP_CONTROLS_PASS / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / GITHUB_PENDING_BW_INGEST / NO_NEW_TASK_CASCADE.
