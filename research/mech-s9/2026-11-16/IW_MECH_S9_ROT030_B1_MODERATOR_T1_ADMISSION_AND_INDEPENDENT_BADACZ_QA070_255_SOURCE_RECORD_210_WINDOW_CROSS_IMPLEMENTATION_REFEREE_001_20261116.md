---
artifact_id: IW_MECH_S9_ROT030_B1_MODERATOR_T1_ADMISSION_AND_INDEPENDENT_BADACZ_QA070_255_SOURCE_RECORD_210_WINDOW_CROSS_IMPLEMENTATION_REFEREE_001_20261116
created_at: 2026-11-16
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
document_type: B1_GOVERNANCE_ADMISSION_RELAY_AND_READ_ONLY_INDEPENDENT_GPT_FAMILY_SOURCE_REFEREE_OF_BADACZ_QA070
exposure: PUBLIC
status: T1_GROUPED_ADMITTED_PASS_BY_MODERATOR / QA070_OWNER_REPRO_PASS_INTERNAL_CROSS_FAMILY_I1 / T2_T3_E4_PHYSICS_GATES_SEPARATE
claims_ceiling: NO_NEW_JULIA_NO_NEW_BLACKHAWK / NO_PBH_BOUND / NO_PAPER_ERROR_CLAIM / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# ROT030 — Formal T1 admission by Moderator, plus different-implementation audit of Badacz Q-A PREREG_070 native 255-row regime-map result

## 1. Formal Moderator source-custody decision: previous T1 HOLD superseded

**DECISION DELIVERED DIRECTLY BY MODERATOR:** In the current 16 Nov Mech-S9 conversation Moderator explicitly clarified `„Decyzja była o dopuszeniu”`. The meaning is to **ADMIT** the overlapping second source T1 workflow `43911520867` as a technical retry following source-parser mismatch in first `43911170672`; earlier `T1_MODERATOR_CUSTODY_DECISION_PENDING` is CLOSED. Do not fabricate a separate signed Moderator artifact or retrospective timestamp. The original overlap breach remains in historical records for prevention of duplicate same-cell experiments; admission does not erase it.

- First original BlackHawk v2.3 j0 execution `43911170672`: BlackHawk source exit0 but incorrect Mech parser 100 PRIMARY vs actual 500 SECONDARY grid, no 25-cell source comparison.
- Second original source execution `43911520867`: full frozen 5 mass indices `[0,22,49,74,99]`, 25/25 PYTHIA BBN current original source rate groups matches Wu–Xu frozen rates; max relative mismatch `7.734157758676474e-11` vs prereg threshold `1e-5`; `T1-PERSTATE` alternative has 50% mismatch. Original `BlackHawk_inst.x` same binary SHA `17da5c5bd9d2958c18ee2c31e1f8236b12be69902795c23e947d8da70eded221` in both jobs; original v2.3 tar SHA `dd148349304c158ed3509ea6935f2fd3d60ebe7cda4c34598aa99ea329c129a7`; original Wu–Xu package overlay frozen `d395183...`.
- **New formal typed status**: `T1-GROUPED_SOURCE_ADMITTED_PASS`, not `T1_PENDING_MODERATOR`. The direct decision was recorded and linked at [B1 joint issue #16, comment #6927998998](https://github.com/wmakiela-tech/Nash-iw-research/issues/16#issuecomment-6927998998) and [Slack source bridge](https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1794860096229409). ROT029 report has a dated controlling update [commit b53ece4](https://github.com/wmakiela-tech/Nash-iw-research/commit/b53ece4d56872ae7f3fc801710391a4e9776a12b).
- Absolutely no third source-provider T1 run or native Julia authorized by this custody admission; T3 literature prior-art / author errata, E4 independent hadronization below first mass-grid node and separate external I1 BBN T2 numerical review remain unresolved.

## 2. Priority, original native authors and source custody

Original scientists: **Quan-feng Wu and Xun-Jie Xu** original PBH–BBN `main-scan.jl` and original source model; **Arbey and Auffinger** original BlackHawk. **Badacz (Claude) FIRST** preregistered and actually ran Q-A PREREG_070 in two source native Julia batches (192 in-domain +63 OFF-SCAN =255 calls), approved separately by Moderator 2026-11-16 17:39 CET. Owner first final report [REVIEW_072 at source commit f42da5c](https://github.com/wmakiela-tech/Nash-iw-research/blob/f42da5ca89227ce2a1b72664a747a4d593e18853/research/badacz/2026-11-16/IW_BADACZ_B1_QA_NATIVE_REGIME_MAP_REVIEW_072_20261116.md) and prereg [PREREG_070](https://github.com/wmakiela-tech/Nash-iw-research/blob/f42da5ca89227ce2a1b72664a747a4d593e18853/research/badacz/2026-11-16/IW_BADACZ_B1_QA_NATIVE_REGIME_MAP_PREREG_070_20261116.md). Underlying hypothesis of linear-to-intermediate-to-saturation response and original archive exploration first belongs to EKS1 ROT011 and mature literature (e.g. astro-ph/9908160), not Badacz or this referee. Badacz FIRST ran separate Q-B T2 contours in REVIEW_071 with conditional 0.272–0.301 dex original-to-E5 shift and W/ORD/TOL PASS; those are NOT re-executed here.

**DISTINCT Mech-S9 ROT030 first:** independent STANDARD-LIBRARY-ONLY, different implementation (no owner analytical code imported) to read the actually recorded 255 ORIGINAL native result rows from `data/qa_A.csv`, `data/qa_B.csv`; compare every 5-point log-beta OLS `X_n` and `Y_code` slope, each conditional `sigma_s`, resolution test `min_5 ΔQ≥1e-3`, every label and prereg hypothesis against Badacz `analysis070.json`; secondly run original Badacz Python source code COLD on the exact source CSV to demand byte-identical owner JSON output; third reject altered source CSV and owner analysis as negative controls. **NO new native Julia or BlackHawk run.**

Actual input exact SHA256, obtained from Badacz original GitHub sources `f42da5c` and checked by the independent source runner:
- `data/qa_A.csv` **`0d7922b78ffe07dd85bbc462324dbf1d9ae6a4fdcc3040d0cf643a08af3f9d56`**, 192 native source rows, baseline plus β[-20,-17] grid for masses j22,28,38,51,62,90;
- `data/qa_B.csv` **`7b25eb8728d0f4c449631ca0035d96ef6ed820d5b4a3b8f2014497a8e6d083cd`**, 63 source rows, baseline plus β[-16.9,-15] OFF-SCAN for j19,22,24;
- `data/analysis070.json` **`72c0925bbf0f9ba3f39b09edab4a63003db0fac9492ccb22575325a95d3f5db4`**, owner frozen output, independently matched fields;
- `code/b1_qa_070_analysis.py` **`1a9d5aafeca14a4c2729572157b6463dc4926c5c526f999116dcbb223487f1f7`**, original frozen numpy polyfit source, NOT imported by independent stdlib checker;
- `data/qa_run_record.json` **`1ed1a26abb8874784fcc5c04297a03cf151ba3f4e1f8ca9714ddd50e2317cade`**, both owner job statuses 0, csv SHA equality;
- Every one of these original 64-char hashes also appears unaltered inside original owner `data/MANIFEST_SHA256.md`. **NO damaged manifest claim:** previous ROT026 reviewer mistake of a truncated SHA expectation was formally retracted; original Badacz manifests PASS.

## 3. All 210 local source windows, predictions, and non-vacuity

There are **162 internal five-node windows** in grid A = 6×(31−4), and **48** in grid B = 3×(20−4); **210 distinct source windows**, with **420 separately checked X and Y slopes and conditional sigma-s measurements**, all independently matched to original owner slopes, labels, resolutions and `dQ` at stringent Float64 tolerances. Each OLS is implemented as centered `Σ(x−x̄)(lnΔQ−mean)/Σ(x−x̄)²` by Python `math.fsum`; NOT numpy polyfit, with `x=lnβ` and `X=Y/(2+Y)`. Both native grid CSVs have full expected node counts and no missing or duplicated β nodes.

| Frozen owner prediction | Independent source-calc result | Note |
|---|---|---|
| P-A1: no resolvable in-domain X SATURATION | **PASS** | Nonvacuous: 5,14,21,23,24,24 resolved X nodes respectively for j22,28,38,51,62,90 |
| P-A2: Y slope at logβ -17.2 in [.35,.70] | **PASS 3/3** | j22 .42026756; j28 .45214101; j38 .46146091 |
| P-A3: Y slope at logβ -18.2 in [.75,1.05] | **PASS 2/3, j22 UNRESOLVED** | j22 .90390422 is point-estimated but window has a subthreshold ΔY; j28 .92373907; j38 .92765927 |
| B: first resolvable SATURATION outside original β scan | **j22,j24: -16.7; j19: no label** | j19 response plateau exists visually at ΔX~7e−4 but below *frozen* 1e−3 resolution threshold |

These gate values are source-deterministic *under the owner resolution/noise assumptions*. No adaptive raising/lowering threshold to recover any specific sample, and no claim of statistical coverage or physical BBN bound. Actual B scan up to β1e−15, 2 orders above original author maximum.

**Independent connection to Badacz T2 original root grid**: nearest source Q-A 5-node local `s_X` to T2 ORIGINAL contour is j22 `0.4191047389` at logβ−17.2 (intermediate), j28 `0.9483477855` at −18.4 (linear), j38 `0.9848071196` at −19 (linear), j51 `0.9855468164`, j62 `0.9973277568`, j90 `0.9883872085`. T2 owner reports 0.2756 dex (j28) and 0.2758 dex (j38) as opposed to `log10(2)≈0.30103` — deficits ~.0254/.0252 dex even with near-linear ORIGINAL regime at root. This **falsifies the simplistic claim that the shift deficit MUST come exclusively from original response saturation/nonlinearity at the contour**, but does **NOT uniquely establish** the K0L channel, untouched nonhadronic background effects, other source terms, nonlinear E5 branch or their mixture. Strictly root-local slope is not a proof of global linearity or of derivative on the modified E5 branch.

**Structural mathematical audit:** original notebook observable `Y_code=2X/(1-X)` is a deterministic monotonic rational transformation, so 
`ΔY_code = 2 ΔX / [(1-X)(1-X_SBBN)]` exactly. Verified on all source observations to Float64 relative algebra residual `4.012346010995316e-12` (finite decimal/float conditioning). The X and Y slopes are **NOT independent physical confirmations** even though both can be useful descriptive views and different finite differences. Neither `Y_code` nor its reference scan is a physically validated helium abundance Yp.

**Noise interpretation guard:** Badacz assumes a transferable `σ_X=1.4e−5` obtained from **ONE** original run default-vs-explicit nominal tolerance comparison, not a cross-mass independently measured statistical standard deviation. `σ_s` is computed by first-order propagation of assumed constant independent source errors across five nodes. Numeric `σ_s` recomputation PASS is a reproduction of this **conditional model**, NOT certification of unbiased noise distribution, confidence intervals or universal resolver thresholds; j22 P-A3 must stay UNRESOLVED even though center's slope .9039 falls in theoretical range. No additional source calls authorized for our audit.

## 4. Actual independent executed reproducibility and adversarial source safety

Original independent source reviewer published at GitHub path `research/mech-s9/2026-11-16/code/mech_s9_rot030_qa_prereg070_independent_stdlib_referee.py`, original create commit **`6f9c478932eecc3c0c6bff0b7594318dfd81bba2`**. Dedicated no-native-physics Github Actions workflow `.github/workflows/mech-s9-rot030-qa-070-independent-referee.yml`, create commit **`ad0387ac8ec1154684a0558648ee000a295e5667`**.

**Actual completed Actions** `43948329975`, **all steps SUCCESS**:
1. source SHA256 of 5 original files and owner 64-char manifest evidence PASS; 255 original CSV rows exact, independent all 210 five-node windows × X/Y slopes and first-order sigma-s under owner assumptions PASS;
2. clean CPython3.11 + frozen NumPy2.1.3 owner original analyzer *reran* on original CSVs, `cmp` **BYTE IDENTICAL** to original owner `analysis070.json`, original owner source SHA **`72c0925bbf0f9ba3f39b09edab4a63003db0fac9492ccb22575325a95d3f5db4`**;
3. intentional one-byte changes separately to owner `qa_A.csv`, `qa_B.csv`, `analysis070.json` each independently **REJECTED** before numerical result and no partial output, negative fixtures **3/3 PASS**;
4. complete GitHub Actions evidence artifact **`14266395478`**, ZIP actual 19474 B SHA256 **`13fda706a1cff95f05a4ae636f88955ef35e4647fc6b3ff27c9f5da7b7a63045`**, directly downloaded, opened as actual ZIP and CRC PASS, own **6/6 inner SHA256 manifest PASS**, exact independent result JSON SHA256 **`4de2fb63c64cdf6b817258d3c7020af14c51a76c2b55c3beaab70a6fc35c38db`** fully read. Generated evidence contains derived numeric output and cold owner analysis but *not* original native Julia CSV input duplicates. This is internal cross-family **read-only DIFFERENT IMPLEMENTATION I1**, not a native independent solver re-execution.
5. Exact original source author Wu–Xu and original Badacz firstness preserved; not an independent published-article replication or external peer review.

## 5. Acceptance and next decision

- **T1 now released at source layer** by directly reported Moderator admission; 25/25 grouped rates match exactly original v2.3 producer table. The earlier procedural HOLD cannot be reinstated absent a new explicit decision. No third T1 run.
- **Q-A** is **SOURCE_REPRODUCIBILITY_PASS with explicitly conditional noise model and OFF-SCAN scope**. Native Badacz source labels are correct under frozen thresholds; Q-A source test does not prove which physical term causes the T2 contour-shift deficit or establish an independent physical PBH constraint.
- **T2** remains Badacz native conditional result; external different-family solver and literature review T3, E4 hadronization uncertainty validation are distinct remaining gates. Any full physical claim needs explicit Moderator scientific acceptance and separate scientific provenance.

**FINAL:** `ROT030_MODERATOR_T1_ADMITTED_PASS / Q_A_ORIGINAL_255_SOURCE_ROWS_210_WINS_INDEPENDENT_STDLIB_PASS / OWNER_QA070_BYTE_IDENTICAL_COLD_PASS / 3_FAIL_CLOSED_MUTATION_CONTROLS_PASS / Q_A_CONDITIONAL_NOISE_OFFSCAN_HOLD / T2_T3_E4_PHYSICS_SEPARATE / NO_NEW_JULIA / NO_NEW_BLACKHAWK / NO_NOVELTY / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN / GITHUB_PENDING_BW_INGEST`.
