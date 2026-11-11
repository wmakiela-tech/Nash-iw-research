---
artifact_id: IW_MECH_S8_ROT017_WUXU_RATE_TABLE_LOO_AND_FLAT_JET_EXTRAPOLATION_GUARD_001_20261111
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_07 / Mech-S8
date: 2026-11-11
exposure: PUBLIC_SAFE
worktype: ORIGINAL_AUTHOR_SOURCE_TABLE_100_ROW_WITHIN_SUPPORT_NUMERICAL_CHECK_AND_CINFINITY_BELOW_EDGE_FALSIFIER
original_author_commit: d395183674cace6c9906a8911bdeb7234ba4040d
owner_prior: Wu–Xu JCAP 2026; Badacz REVIEW038/042/043/050/054/057; Mech-S7 ROT036/037 C2 edge jets; MT14 ROT021/022/023; Mech-S8 ROT003/015/016
status: EXECUTED_WOLFRAM_ALL100_LOO + EXECUTED_PYTHON_SOURCE_EXACT_FIRST12 + MATH_EXACT_FLAT_MODIFIER
claim_ceiling: TABLE_INTERNAL_CONSISTENCY_NOT_GENERATOR_TRUTH / HYPOTHETICAL_EXTRAPOLATION_MODELS_ONLY / E4_SOURCE_BLOCK / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
---

# Mech-S8 ROT017 — Native Wu–Xu five-rate table: very small within-grid log interpolation error does not justify subedge extrapolation

## Source-first and firstness

Original source: [Wu–Xu public pinned v2 generator-rate table](https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/data/out/hadrons_from_PBH.dat) Git blob SHA-1 `06d0883a27b108692720422294ba2baacd381a64`, raw file SHA-256 **`25411c26cb24b08058be6dffe01e3c6cc668c91de963438a91c4aac0a38199df`**, 11,535 bytes; **100 original numerical rows**, five positive rate columns. Mass grid is 1e9 to 4e12 grams, logarithmically spaced. Source commit d395183 is **2025-12-30 / arXiv v2**, *not* the May-2026 v3 manuscript.

No Wu–Xu / BlackHawk / PYTHIA runtime was executed here. The *rate table is an original frozen output*, not a new spectrum generator measurement. Earlier owner prior, especially Mech-S7 ROT036/037 exact C2 edge-jet conditional tests and Mech-S8 ROT003 v2 paper/source exponent discrepancy, already addressed the left edge. ROT017 adds the concrete **entire-100-row leave-one-out self-consistency audit** and the **smooth-to-all-orders subedge multiplier** that exactly preserves all tabulated values and the edge jet. This construction is mature approximation mathematics, with no physics/novelty claim.

Badacz REVIEW043/T1 previously established full-charge aggregation of `pipm`, `Kpm`, `proton`, `neutron` table columns and source-to-ODE charge interface mismatch *under actual PYTHIA convention*. MT14 ROT021/022/023 independently audited historical generator evidence. **ROT017 does not re-claim that issue as newly discovered**. Badacz REVIEW054 already ran the native simultaneous C×2+D×2 case, and REVIEW057 already measured heavy-end post-nucleosynthesis hadron counts; neither must be re-requested.

## 1. Direct native table: 100-row interior LOO

For each species and each interior row i=2..99 (98 tests), predict the withheld log-rate at x_i=log(M_i) by the unique line through its two immediate neighbor table rows. Compute epsilon_i=exp(pred_log_rate−observed_log_rate)−1. This tests only **smooth sampling** of the *existing generated table*. Every positive table rate is preserved; no external source, spectrum or ODE is tested.

All five species share a maximum-LOO position **row 86 (1-based, M≈1.2378777884e12 g)**, well above the relevant first left-boundary rows. Independent implementation via near-geometric midpoint log-rate, (the grid is nearly logarithmically uniform) (since mass grid is log uniform), agreed with exact-x interpolation to within **1.27×10⁻¹² percentage point**. This is a mathematical cross-check of the same table, not independent BlackHawk data.

## 2. Tested alternative below-edge exponents

Let p_k be the ordinary-least-squares slope estimate *in log-rate vs log-mass*, using the FIRST k table rows, k∈{2,3,4,5,8,12}; then define an **anchored** comparison model

R_k(M)=R_1 [M/M_1]^(-p_k), M_1=1e9 g,

with all k models sharing the exact observed R_1. **Important:** the p_k are OLS slopes, but the anchored intercept is NOT the OLS intercept for k>2. These anchored powers are deliberate competing model assumptions; they do not each exactly interpolate every k point. They illustrate model-window dependence and are NOT certified alternatives with the same within-table accuracy.

| Hadron group | max LOO inside 100 rows | median | p₂ original below-edge code | p₁₂ window slope | R₁₂/R₂ at 3e8 g | R₁₂/R₂ at 1e8 g |
|---|---:|---:|---:|---:|---:|---:|
| π± | 0.2321% | 0.0176% | 1.200486 | 1.284777 | +10.68% | +21.42% |
| K± | 0.2177% | 0.0167% | 1.196651 | 1.279737 | +10.52% | +21.08% |
| K⁰L | 0.2180% | 0.0175% | 1.196805 | 1.280112 | +10.55% | +21.15% |
| p/p̄ | 0.2393% | 0.0177% | 1.204291 | 1.289823 | +10.85% | +21.77% |
| n/n̄ | 0.2378% | 0.0180% | 1.204763 | 1.290402 | +10.86% | +21.80% |

The five rate ratios at 1e8g differ +21.08…+21.80% solely as a consequence of changing the slope window while anchoring at the first rate. The k=12 ANCHORED power does not match all first12 rows closely: its largest residual over those 12 author values is 1.235%–1.292% (depending on species), distinctly larger than the full-table LOO test. This mismatch is precisely why section 3 gives a separate, exactly data-matching nonunique extension. This is not a physical source-error estimate, a correction to the JCAP PBH bound, an uncertainty interval, or evidence that k=12 is the correct choice.

## 3. Stronger exact-grid witness: C∞ flat multiplier

To isolate the *data insufficiency* independently of whether the anchored k=12 power is a good global fit, define R_ref(M) as the ORIGINAL piecewise log-linear interpolation of **all 100** rate points, using the first pair below the edge, exactly as `tool_script-hadrons_from_PBH.jl` prescribes.

Let m₀=1e9g, t=log(m₀/M)/log(10), and define the standard flat cutoff

w(t)=0 for t≤0; w(t)=1 for t≥1; 0<t<1: w(t)=exp(−1/t)/(exp(−1/t)+exp(−1/(1−t))).

For any c>0, define

**R_alt(M)=R_ref(M) × [1+(c−1)w(t)].**

**Exact proof:** for every tabulated mass M≥m₀, t≤0, so w=0 exactly and R_alt=R_ref; all 100 table values agree *by definition*. w is C∞ and **flat to every derivative order at t=0**. Therefore, as M approaches m₀ from below, the factor and all of its derivatives equal those of unity: it leaves the entire local edge jet of the original log-linear/power extension unchanged. At M=m₀/10, w=1, so R_alt/R_ref=c. c may be any strictly positive value; without restricting the below-edge source class, even all exact table values plus all edge derivatives do **not** determine the extension.

Choosing c for each hadron equal to the anchored 12-vs-2 ratio above gives **exactly the +21% contrast** with **exact equality of all 100 source-table values**. This is much stronger, as an information-theoretic obstruction, than the window-slope numerical comparison alone. Note R_ref is piecewise log-linear and has derivative changes at interior knots; the *multiplier* is C∞ and its flat edge ensures equality of the local edge jet, but this does not convert the entire 100-knot interpolant into a globally C∞ function. The construction is **mathematical**, not a Hawking/PYTHIA-mechanistic proposal. It is positive, but need not obey energy conservation, analytic continuation, physical greybody asymptotics, or QCD fragmentation. No positive lower bound on the missing hadron flux is inferred.

The Python numerical checker applied the multiplier to **all 12 available exact-source offline snapshot rows (60 source rates)**, with maximum relative floating-point discrepancy ≤9×10⁻¹⁶. The analytical 100-row equality holds without needing the other 88 rows because the multiplier is exactly 1 for all M≥m₀.

## 4. Reproducibility provenance and negative knowledge

- **Full-table science check executed** with Wolfram Language on original pinned 100-row public text, raw SHA256 verified, five × 98 withheld predictions. Independently repeated per-row comparisons using the geometric midpoint of neighboring log-rate values. Detailed full-table summary is in `mech_s8_rot017_cross_method_results.json` tagged `WOLFRAM_FULL100`, not a local Python full-source replay.
- **Independent Python offline check executed** on the first 12 original rows, individually copied and **byte-for-byte matched to the upstream exact 13-line text** using independent Wolfram raw `FileHash`. Exact 12-row SHA-256 `0a81af204bbfe2ced214b3edaaf31bcd52354d4b1934adb67571e726d9d26ac3`. Python 3 standard library, no Internet needed.
- **Full 100-row Python repro available but NOT EXECUTED in the offline container**: run `python mech_s8_rot017_author_table_edge_loo.py --download` on a networked machine, or `--input` with the frozen original 11,535 byte file. Both modes enforce original full-source SHA before returning data. The local ZIP contains only the **exact first12 excerpt**, not a reconstructed or invented 100-row data file.
- **Independent official BlackHawk v2.3 source-table admission remains OPEN**. MT14 ROT021 previously pinned official archive 161,495,983 bytes SHA256 `dd148349...` but did not extract production tables. This turn re-confirmed a full byte hash in one Wolfram transfer, while subsequent transfer/extraction attempts failed (including incomplete SSL transfer); no actual official v2.3 table contents were admitted.
- **Historical JCAP Fig5 executable↔source identity OPEN**; RATE grid self-consistency does not imply good physical spectra, faithful secondary hadronization, charge correctness, 10D Julia numerical convergence, ODE error certificate or physical PBH Y_P/beta bounds.
- Original charge semantic issues first owned by Badacz REVIEW043, native A1 failure first Badacz REVIEW054 and independent AUD1/REC11. No new task cascade. `BW_INGEST_PENDING / REFEREE_NOT_SIGNED / NO_CANON / NO_EXEC_SIGN`.

## 5. Scientific action

Existing rate table is internally smooth, but the table provides no empirical information for M<1e9g. **Priority remains direct BlackHawk/PYTHIA BBN secondary hadron spectra at M~1e9,3e8,1e8 g** with pinned executable/tables, primary→secondary map and kinetic/thermalization transport validity. Additional fitted power laws, without new source physics, cannot settle E4.

**Outcome:** `ROT017_ORIGINAL_TABLE_INTERIOR_LOO_PASS / CINF_BELOW_EDGE_DATA_NULLSPACE_PASS / SOURCE_VALIDATION_E4_HOLD / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN`.
