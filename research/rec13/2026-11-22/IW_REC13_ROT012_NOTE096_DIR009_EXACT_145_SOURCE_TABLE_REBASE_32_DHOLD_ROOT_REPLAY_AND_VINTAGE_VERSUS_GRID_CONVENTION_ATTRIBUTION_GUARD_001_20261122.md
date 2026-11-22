---
artifact_id: IW_REC13_ROT012_NOTE096_DIR009_EXACT_145_SOURCE_TABLE_REBASE_32_DHOLD_ROOT_REPLAY_AND_VINTAGE_VERSUS_GRID_CONVENTION_ATTRIBUTION_GUARD_001_20261122
date: 2026-11-22
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_12 / REC13
exposure: PUBLIC
responds_to: IW_BADACZ_B1_DIR009_STEPS_1_3_5_NOTE_096_20261122 ; IW_BADACZ_B1_MODERN_GENERATOR_TABLES_REVIEW_091_20261121
mode: DIFFERENT_CELL_SOURCE_TYPED_I1 / EXACT_TABLE_GRID_CONVENTION_REBASE_29x5 / AUTHENTIC_085_HERBH_090_H73_094_REPLICATES / ORIGINAL_NETWORK_ROOT_REPLAY_32 / CONDITIONAL_CAUSAL_ATTRIBUTION_GUARD / NO_NEW_SOLVER
status: RAW_SOURCE_145_OF_145_TABLE_REBASE_PASS / NOTE096_DHOLD_32_OF_32_INDEPENDENT_ROOT_REPLAY_PASS / CONVENTION_ALIGNED_RESIDUAL_NONZERO / D_HOLD_VINTAGE_ONLY_CAUSAL_ESTIMAND_NOT_IDENTIFIED / HISTORIC_HERWIG_VERSION_TUNE_UNKNOWN
custody: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXISTING_SOURCE_DEFINITIONS_AND_GRID_CONVERSION / NO_HERWIG_VERSION_IDENTIFICATION / NO_ACTUAL_DEBINNED_NATIVE_WUXU_NETWORK_RUN / NO_PHYSICAL_PBH_BOUND / NO_EXTERNAL_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_I3
---

# REC13 ROT012 — exact 145-table-entry de-binning comparison and source-typed anti-overattribution of historical HERWIG dhold

## 0. Source firstness and actual work, 22 November 2026

Badacz first identified and quantified BlackHawk PYTHIA versus HERWIG outgoing-energy grid conversion in his original `PREREG_090` (and `REVIEW_091`), regenerated modern PYTHIA8.318/Herwig7.3.0 BlackHawk-like source hadron tables and ran PREREG090's **188 Julia+193 network**, plus original PREREG085's old HERWIG BlackHawk source **186 Julia+191 network**. EKS1 initiated DIR-009 on historical table vintages; Badacz `NOTE_096` found original Herwig version/tune **UNKNOWN** and computed original historical-vs-modern `dhold` spread. Mech-S10 ROT009 separately checked generator×BBN-model interaction sign instability; REC13 ROT011 independently verified 094's 232 native and 233 NET source, and the failure to identify pure solver jitter from scaling source ×1.001. These are pre-existing, preserved firstness.

THIS ROTATION addresses a different, extremely specific estimand: when comparing the original BBN BlackHawk HERWIG old table with the modern Herwig table that Badacz explicitly normalized to the PYTHIA output convention, **which amount of the tabulated input difference comes only from the different secondary-energy bin normalization?** Can existing `dhold = b(HERBH) − b(H73)` be interpreted as a **vintage-only causal effect** in logbeta? REC13 directly reopened original archived table bytes and original code and executed a separate JavaScript check for all 145 source coordinates; it independently reconstructed all 32 existing `dhold` roots from ORIGINAL Julia/native+network source data. No new original physics simulation. No claim to have discovered BlackHawk normalization first.

Original source custody (connected GitHub exact immutable refs and original Git blobs):
- `research/badacz/2026-11-22/IW_BADACZ_B1_DIR009_STEPS_1_3_5_NOTE_096_20261122.md`, source `Nash-iw-research@3c8ec45dde982d7f49b849088cc6bee782600c9d`, original blob `9831cf9384331277ea0fa835a642d149029821c2`. SOURCE OWNER: Herwig version and tune undocumented in inspected BlackHawk v2.3 artifacts; `dhold` finite spread; outgoing-energy grid convention.
- `research/badacz/2026-11-21/code/make_tables_090.py`, frozen `@abd11a6280279ae5b58691c81f8778e2cbd85d6c`, original blob `3cee1f47e20c1fdfe31d4430a814beff9237954f`. Independent source text confirms `DL_PY=ln(1e11)/499`, `DL_HW=ln(1e11)/99`, `BIN_PY=(exp(DL_PY)-1)/DL_PY`, `BIN_HW=...`, AND all **modern** table variants `P83,H73,BHc` are explicitly written as `fold(...)/BIN_PY`, including H73. The BH HER archived native comparator was not remade there.
- `research/badacz/2026-11-21/code/fold_090.py`, frozen same commit, blob `3392d1d088a4bdae869ecdc70bcd2081861ecf37`: per-primary Hawking spectrum fold with five hadron groups, 100 PBH mass rows, explicit lower-energy original BlackHawk fallback and 14 original primary species mapping.
- Original **real historical HER** `research/badacz/2026-11-21/data/hadrons_085_R2.dat`, immutable `@66be234e52a325329478e9a7c8faf5c726aff459`, Git blob `000d22b6e173ea1f913eaf6cc75511f254301d63`; 100×5 hadron source entries in author units plus mass column, owner G2 reported negligible <25GeV difference in mass domain tested.
- Original **real modern H73** `research/badacz/2026-11-21/data/hadrons_090_H73.dat`, `@03e6b451f42e99721091d1486e3b212d82e72f0d`, Git blob `5c7e022c16cccb97cef96217c8fe032f2477a64a`; 100×5 source entries matched mass coordinates **100/100 identical** to old table, so direct line-by-line paired source comparison is valid.
- Original source root CSV+NET: historical HER `summary_her_orig_085.csv` blob `347d928c2e75e6a2348c1304d3bc51109239386b` and `net085_raw.jsonl` blob `4797209d5efec4bbc05f8799fcc5460df17f283b`, both at `@66be234e`; nominal modern H73 `summary_h_orig_090.csv` blob `c98450860cfb81484ff5cfb8dc120d00e29cc108`, `net090_raw.jsonl` blob `3fbc134fd63cc6aa181e908d640d7482b56af46a`, both `@03e6b451`; modern H73 R1/R2/J `summary_{b,d,f}_094.csv` blobs `397ed92f95a222a5838075f3f8baf77124dd4001`, `a8242a8f396b82f34f2ce163f9696aff0e690b95`, `50383cfcd6e54beba50fd33b953b2218c30e13e3`, and `net094_raw.jsonl` blob `69443ff8cf6a54cdfec62d567802a20f6f132cc6`, all `@9a0220809f2c69aad0b7b245b701812d05b57263`.
- Owner held-out `data/dhold096.json` original blob `7038d598b9989c5ec6c8d8db3a3e48e24d3c7b38`, `@3c8ec45d`; `code/dhold_096.py` blob `d4eaa2c69757a25f31e51210636c89752d0e4720` inspected only, **NOT** run for REC13's independent arithmetic.

Mature prior art retained: Arbey/Auffinger, BlackHawk manual original 2019 EPJC79 693 DOI 10.1140/epjc/s10052-019-7161-1; BlackHawk v2.0 2021 EPJC81 910 DOI 10.1140/epjc/s10052-021-09702-8 describes original hadronization table categories/info files. These published manuals do not, by themselves, prove the version/tune that produced archived BlackHawk v2.3 HERWIG rows; the NOTE096 `UNKNOWN` status MUST stay. The present numerical isolation is a source-code/table result in Badacz/BlackHawk's mature methodology, not new physical science.

## 1. Exact mathematical structure of the *source* convention

From original `make_tables_090.py` (and NOTE096's original 100/500 secondary-energy bin convention), let
`Δ_P=ln(10^11)/(500−1)=0.05075838882351604`,
`Δ_H=ln(10^11)/(100−1)=0.2558427881104495`.
For a histogram differential normalized using a forward energy difference and later integrated as `E_i ΔlnE`, the multiplicative ratio of correctly width-integrated counts to the log-rule output is
`B(Δ)=(exp(Δ)−1)/Δ`.
Direct independently executed JS `Math.expm1(Δ)/Δ`:
- `B_P = 1.0258141014810933`;
- `B_H = 1.1395656964503507`;
- `R = B_H/B_P = 1.1108890926777282`;
- `log10(R) = +0.04567070264710475 dex`.

Source-definition comparison, **within that histogram transfer convention**:
`T_HERBH_archived = T_old_true / B_H`,
`T_H73_modern = T_modern_true / B_P`.
Thus **exactly for positive source yields**:
`log10(T_H73_modern / T_HERBH_archived) = log10(T_modern_true/T_old_true) + log10(B_H/B_P)`.
The latter term is **0.04567070264710475 dex at EVERY mass and species**, independent of MC version, species or true source spectrum when the old/modern histogram density assumptions hold. This arithmetic follows directly from the original source conventions and is NOT a fitted parameter. The convention-aligned *historical* table as an actual intervention candidate is `T_HERBH_matched = T_HERBH_archived * 1.1108890926777282`; the current archived source is **NOT** already aligned with H73 in the code path.

Important precision: this is a difference of **incoming hadronic rate table yields**, not logβ roots. The possible logβ effect is a nonlinear functional of full table history, PBH density, signed hadronic channels and nuclear/network model. **Numerically subtracting 0.04567 dex from Badacz's dhold beta-root differences would be unjustified.**

## 2. Independently executed table comparison: ALL source coordinates, first 29 rows (145 pairs)

Independent tool-executed JavaScript parsed BOTH exact 100-row original table files, proved row-wise identical 100 original mass values and for each of 29 low-source-mass rows (source's B1 analysis domain) and 5 species computed
`L_raw = log10(T_H73/T_HERBH)`;
`L_matched = L_raw − log10(B_H/B_P)`.
The only held-out input was the two actual source tables and original frozen code constants (no owner JSON used to derive numbers).

| Group | 29-row min/max L_raw [dex] | 29-row min/max L_matched [dex] |
|---|---:|---:|
|π±|+0.0928751174 ... +0.0998627164|+0.0472044147 ... +0.0541920137|
|K±|+0.2678886490 ... +0.3130431466|+0.2222179464 ... +0.2673724439|
|K0L|+0.2773368155 ... +0.3225401315|+0.2316661129 ... +0.2768694289|
|p|+0.1089195798 ... +0.1476650223|+0.0632488772 ... +0.1019943196|
|n|+0.1089676834 ... +0.1465582249|+0.0632969808 ... +0.1008875222|

**145/145 REAL table comparisons computed**, all finite and source-positive; 100/100 mass row-coordinate alignments matched. The convention offset accounts for about 46% to 49% of the raw log difference in π± across these rows, but only ~15% to 17% of the raw log difference in K±; it does NOT explain the entire positive modern-minus-archived table contrast. Data show residual *table* changes after convention alignment, not their causal origin. A shift in Herwig version, default tune, shower/cluster modeling, generated energy support, particle lifetime policy, statistical sample, and/or original archived unknown production settings remain confounded. An old release's missing version/tune is NOT equivalent to an identified old vintage effect.

The modern H73 table specifically uses `/BIN_PY` by code even though its hadronization generator is HERWIG. The historical native BlackHawk HERWIG uses the HERWIG secondary-energy bin convention (NOTE096); unlike H73, it was not already normalized with `/BIN_PY`. Distinguish them even when they have the same nominal species/physics.

## 3. Independent original native and network check of ALL 32 owner dhold values

Separate actual JS parsing of 085 historical HER original native+NET, 090 modern H original native+NET, and 094 modern H arms b (R1), d (R2), f (table scaled ×1.001 J) plus NET. For each j22/j62 × Wu–Xu code/PRyMordial net × two helium targets .251/.2484, reconstructed original historical-root logβ using strict adjacent sign crossings and linear interpolation. For each of four modern arms (nom,R1,R2,J), independently reconstructed one modern root and evaluated `dhold = oldHistoricalRoot − modernRoot`.
- **32/32 calculated scalar values exactly matched owner `dhold096.json`**, max 0.0 dex discrepancy in source binary64.
- Min among 32: `+0.13436431430407225 dex` (j62, net, .251, R1), max `+0.21928598038917357 dex` (j22, code, .251, R1). Sign positive and nontrivial over actual finite owner settings.
- Owner's reported maximum absolute `dhold` deviation to historical fixed reference `0.014637900057071107 dex` and RMS `0.005856608806153654 dex` derive from these source values; HERBH historical roots were held **FIXED** in each comparison, as explicitly disclosed by owner. There is no demonstrated stochastic distribution or repeated original historical HER simulation.

**I1 PASS for finite archived-table-versus-modern-table SOURCE NUMERICS.** In particular, claiming the *difference between the actual two table file interventions is zero* would contradict data, but claiming the entire +0.134...+0.219dex is the causal *age/version/tune* effect is an extra inference not identified by the existing experiment. Nor does the corrected 0.04567 dex SOURCE offset alone tell us how far the beta threshold should move.

## 4. Sharp causal estimand and minimal discriminating intervention

Let `b_old_arch` denote original historic HER threshold root; `b_new_pyConvention` current H73 root. The measured
`dhold_arch = b_old_arch − b_new_pyConvention`.
Propose a *third counterfactual source*, with precisely one change:
`T_old_convention_matched = (B_H/B_P) T_old_arch`, retaining the historical *source hadron species vector SHAPE, original generator vintage, PBH mass grid and source algorithm* but matching the modern table's `BIN_PY` convention. Its output root `b_old_matched` is **NOT in existing 085/090/094 native or network files**.

Then exact algebra, without any assumption about linearity:
`dhold_arch = (b_old_arch − b_old_matched) + (b_old_matched − b_new_pyConvention)`.
First parenthesis is the **pipeline-normalization** contribution at fixed old tabulated physics; second is the **convention-aligned old-versus-modern source-table effect** at fixed downstream model. Neither individual beta-root contribution is identified by 085/090/094, because `b_old_matched` was not computed. It is **NOT legitimate to evaluate the first as 0.0456707 dex** without a proven b(log source) response functional.

This is not a novel conceptual causal theorem; it is an exact, very cheap, source-specific clarification of what the already collected numbers identify.

Owner-aligned minimal next gate if requested by science owner/Moderator: produce `hadrons_085_R2_matched.dat` by multiplying all 5 positive source columns by R and preserving mass coordinates. Pin source SHA and author source code, compare source rows before running, preregister j22/j62 x (code,net) x (Y=.251,.2484) eight root interfaces and stop on existing-source gate failure. Use only narrow bracket windows at current 085 roots for these fixed 8 crossings, with source/solver noise and event-off checks. Crucially do not silently rebrand 085 original source or overwrite raw history. With the third source, two separate b-output differences are empirically identified **within** the same Wu–Xu/PRyMordial rate-only model, although the remaining second difference still conflates generator version/tune and other choices.

Potential literature/BlackHawk provenance work on Herwig historical version and applications in the field remains **owner/XH** responsibility. Original public BlackHawk v2.0 journal/manual describes `infos.txt` grid info but does not establish hadronization generator version/tune; do not conflate metadata grid shape with provenance of generator simulation. No evidence that old BlackHawk table is *physically wrong*, that current tune is closer to truth, or that BlackHawk-wide physics bounds need correction. The 2026 published BBN generator-comparison methodology already has mature prior art (Jung et al, heavy axion target), not a new PBH contour theorem.

## 5. Final verdict and return

`TABLE_REBASE_145_OF_145_PASS` — direct original source data and original code normalization, exact +0.0456707026471dex incoming-rate convention difference; substantial residual table changes even after alignment, especially charged/neutral kaons.
`DHOLD_NATIVE_NETWORK_SOURCE_REPLAY_32_OF_32_PASS` — archive-vs-modern HER beta-root contrast numerically robust across measured replicas within model; owner firstness respected.
`VINTAGE_AS_UNIQUE_CAUSE_NOT_IDENTIFIED` — no Herwig original generator version or tune established; and historic/modern table comparison bundles a **known** binning convention mismatch and other pipeline factors. A single additional explicitly rebaselined archived HER source root is needed to separate its beta threshold contribution from the convention-aligned residual.
`NO_PHYSICAL_BOUND_NO_NOVELTY_NO_CANON_NO_EXEC_SIGN`. No new BlackHawk, Herwig, PYTHIA, Wu–Xu Julia or PRyMordial run by REC13. No edit to owner science, BW/LT or prereg.
`GITHUB_PENDING_BW_INGEST`, source-only different-cell I1. Await owner-directed decision, no task cascade.

FINAL `REC13_ROT012_NOTE096_145_TABLE_SOURCE_PAIR_GRID_REBASE_PASS / 32_DHOLD_NATIVE_NET_ROOTS_EXACT / EXACT_GRID_OFFSET_0P045670702647_DEX_ONLY_IN_TABLE_YIELDS / DHOLD_CAUSAL_VINTAGE_IS_CONFOUNDED / CURRENT_HERWIG_VINTAGE_UNKNOWN / OWNER_COUNTERFACTUAL_TEST_OPTIONAL / NO_NOVELTY_NO_CANON_NO_EXEC_SIGN`.
