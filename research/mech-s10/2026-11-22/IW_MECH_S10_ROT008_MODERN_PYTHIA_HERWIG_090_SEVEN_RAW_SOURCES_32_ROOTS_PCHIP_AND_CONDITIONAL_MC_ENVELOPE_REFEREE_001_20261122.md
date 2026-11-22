---
artifact_id: IW_MECH_S10_ROT008_MODERN_PYTHIA_HERWIG_090_SEVEN_RAW_SOURCES_32_ROOTS_PCHIP_AND_CONDITIONAL_MC_ENVELOPE_REFEREE_001_20261122
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10
date: 2026-11-22 Europe/Warsaw
mode: SEVEN_ORIGINAL_NATIVE_AND_NETWORK_SOURCE_FILES / INDEPENDENT_STDLIB_PYTHON_GIT_BLOB_SHA_GATED_REEXECUTION / NO_NEW_SOLVER
owner_firstness: BADACZ REVIEW_091 PREREG_090 188_JULIA_193_PRYMORDIAL_260_MC / AUD3 PRERUN MC_SEED_AND_ENERGY_AUDIT / BADACZ R2 INDEPENDENT_MC_REPLICATES
exposure: PUBLIC
status: 32_OF_32_RAW_LINEAR_ROOTS_OWNER_EXACT / 32_OF_32_PCHIP_ALTERNATE / 8_GENERATOR_EFFECTS_STABLE / CONDITIONAL_MC_ENVELOPE_LABEL_STABLE
claim_ceiling: NUMERICAL_IN_FROZEN_MODELS_ONLY / NOT_MC_95PCT_CI / NO_PHYSICAL_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# Mech-S10 ROT008 — niezależny audyt dwóch interpolatorów i konserwatywnej klasyfikacji systematyki generatorów dla Badacz REVIEW_091

## 0. Data-currentness, firstness, no duplicate science

Mech-S10 previous ROT007 alerted Badacz to event-source interpolation aliasing and a Bash fail-open structure in frozen PREREG_079. On 21 Nov, Badacz independently performed 079: GATE_FAIL_NO_LABEL owing to underresolved event (V5 j22 ~10.1%). 081 then used native Wu–Xu original dense around-source-off samples and matching log floor, reached all-six-gates PASS, V5 j22 0.23%, j62 0.19%; event warning from earlier ROT007 is CLOSED at level of the owner-source validation, NOT a currently unresolved 079 error. Badacz subsequently completed 083 native 228 + network 233 for four mass indices, and 085 BlackHawk v2.3 table-set generator control. ROT008 neither repeats these nor makes an independent science-firstness claim.

Latest original Badacz REVIEW_091, Git blob b451f21a1620c3e6b01eadeb3e180e69cbcbadd3, 22 Nov 2026, supersedes a naive "generator difference = BlackHawk provided table-set difference" reading. Badacz original performed modern PYTHIA 8.318 and Herwig 7.3.0 with BlackHawk author recipe, MC 260 energy-channel jobs, native original Wu–Xu Julia 94+94 calls, network 193/193. 13/13 gates PASSED. Modern-generator dmod=H73-P83 ranges +0.129 to +0.221 dex rather than old provided-table difference +0.323 to +0.368. Author PYTHIA table root matched to ~0.009 dex. Subsequent owner MC independent seed replicates found maximum per-table ratio spread S=0.0112 dex and one Herwig high-energy W event-level energy-leak exception; owner reports an illustrative threshold spread |delta dmod| <=0.022 dex, not formal certainty. These facts are the owner's first result.

ROT008 is an independent narrow source referee for **interpolation and label sensitivity**, not a new generator or full network run, and does NOT copy/interpolate final owner roots as inputs.

## 1. Seven original source files, exact immutable Git blob identities

All seven files were ACTUALLY FETCHED via live GitHub repository and processed, not only read from an owner summary; independent source-only script validates every exact git hash-object before using it:

| original source file under research/badacz/2026-11-21/data/ | Git SHA-1 blob |
| --- | --- |
| summary_orig_083.csv | f7ea90eb3202933e9f52336315c1f36b3d40b019 |
| net083_raw.jsonl | 05f6f93eb4f53a95f5ad6fbe38609557bae04465 |
| summary_her_orig_085.csv | 347d928c2e75e6a2348c1304d3bc51109239386b |
| net085_raw.jsonl | 4797209d5efec4bbc05f8799fcc5460df17f283b |
| summary_p_orig_090.csv | 737eaccea9e8152d4f39bdfeb026577dc1744c6f |
| summary_h_orig_090.csv | c98450860cfb81484ff5cfb8dc120d00e29cc108 |
| net090_raw.jsonl | 3fbc134fd63cc6aa181e908d640d7482b56af46a |

Files contain actual ORIGINAL frozen author Julia scalar outputs and genuine PRyMordial source network results; references original Badacz owner runs. No new Julia, BlackHawk, Herwig, PYTHIA, PRyMordial or physical solver was executed by Mech-S10 ROT008. The independent script reads raw original-rate/network pairs by run ID, explicitly requires 0<= network rc and nonmissing YP_BBN for each matched source row, sorts by numerical logbeta and selects original native beta nodes; it handles **different grids** 083 vs 085/090. It does NOT import Badacz analysis_090.py nor use analysis090.json as input.

Separate owner analysis090.json blob 2bae2cb7505e340ec6fe0db107be3070e8bd8923 was opened ONLY FOR FINAL EQUALITY VERIFICATION. Read-only value check: all **32/32** separately recalculated strictly linear 0.251/0.2484 roots EXACTLY match owner values at JavaScript/Python double precision (max |delta| 0). Owner estimation firstness unchanged.

## 2. Independent alternative PCHIP experiment — reproducible third-party algorithm

Four physically distinct input yield table sets:
- PYBH: original Wu–Xu/BlackHawk author PYTHIA table, Badacz 083.
- HERBH: old Herwig BlackHawk provided table, Badacz 085.
- P83: newly generated PYTHIA 8.318 table, Badacz 090.
- H73: newly generated Herwig 7.3.0 table, Badacz 090.

Two source mass indices j22/j62, two observable models original author code Y_C vs PRyMordial network YP_BBN, two targets 0.251/0.2484 ⇒ **4 × 2 × 2 × 2 = 32** root problems. For each full recorded source series, locate ONE threshold crossing in its native logbeta grid, compute original bracket-based linear root, then compute an **independent piecewise cubic Hermite, Fritsch-Carlson/SciPy-style PCHIP** local root using adjacent first derivatives from neighboring original source records, harmonic means on sign-concordant secants and endpoint slope limiters. The PCHIP interpolant is shape-preserving, and 72-step bisection restricts each root to its ORIGINAL source-grid bracket. All 32 cases bracketed exactly once; no extrapolation outside scan.

From **actual independently executed GHA Python3 stdlib**:
- maximum |PCHIP root minus linear root| among all 32 individual roots = **0.0016572786298425513 dex**;
- maximum |[H73-P83] PCHIP minus [H73-P83] linear| among all eight generator shifts = **0.0008760250764758837 dex**;
- original owner 32 linear roots = **32/32 source-exact PASS**, owner source file analysis090.json was NOT used by the actual independent PCHIP program.

Eight independent generator effects:

| mass | observable | helium threshold | linear dmod dex | PCHIP dmod dex | PCHIP-linear dex |
| --- | --- | --- | ---: | ---: | ---: |
| j22 | code | 0.251 | +0.142702684666 | +0.142950648931 | +0.000247964265 |
| j22 | code | 0.2484 | +0.148178909503 | +0.148829237347 | +0.000650327844 |
| j22 | net | 0.251 | +0.128971100425 | +0.128891612532 | -0.000079487892 |
| j22 | net | 0.2484 | +0.141432520161 | +0.142308545238 | +0.000876025076 |
| j62 | code | 0.251 | +0.219748963290 | +0.219998891461 | +0.000249928171 |
| j62 | code | 0.2484 | +0.221188098983 | +0.220891711449 | -0.000296387534 |
| j62 | net | 0.251 | +0.216135878450 | +0.215913576807 | -0.000222301643 |
| j62 | net | 0.2484 | +0.214246092103 | +0.213674906300 | -0.000571185803 |

Separate strict identity enforced on all eight cases and BOTH interpolators:
dgenBH ≡ dmod + drepro + dhold (algebraic telescoping of four same-source roots); max machine discrepancy <1e-12. This identity is not scientific novelty and does not prove those terms are statistically independent.

## 3. Joint conditional envelope: shape-preserving interpolation plus existing owner's MC spread

Badacz 091 r2 measured largest replicate-to-original **yield ratio log-spread S=0.0112 dex**, and bounded its effect on generator dmod illustratively by **2*S=±0.0224 dex** using a locally bounded estimated mass-j22 root elasticity. This is empirical transfer of MC uncertainty, NOT a formal probabilistic 95% interval, certified independent random draws or a rigorous worst-case theorem. Code 091's original G_STAT diagonal covariance gate had been qualified by later owner independent MC replicas.

A deliberately conservative **conditional arithmetic combination** of maximum observed interpolation method spread on ANY of 8 dmod with assumed MC envelope:
linear generator dmod range [0.12897110042450777,0.2211880989833972] dex;
max |delta interpolation|=0.0008760250764758837;
optional ±0.0224 MC envelope;
therefore total combined dmod range
**[0.10569507534803188,0.24446412405987308] dex**.
It is strictly within both preregistered LM classification boundaries (0.10 and 0.27), so the 8-cell **MOD_INTERMEDIATE** label is robust under THIS COMPOSITE FINITE-DATA ENVELOPE. It also stays within the original P2 0<dmod<0.25 range, conditional on 2S bound.

CAUTION: 0.0224 itself is not a proven all-sources error interval, nor does finite 2-seed MC provide a confidence level or protect against generator tuning, invalid Herwig W high-energy events, cosmic reheat, QCD/hadron transport or physical source semantics. No physical constraint or error bar for PBH abundance is certified. Net-minus-code dmod differences in original linear results are j22: -0.01373 (target0.251), -0.00675(target0.2484), j62: -0.00361 and -0.00694 dex; all below assumed 0.0224 MC transfer envelope, so this finite source evidence cannot distinguish an actual model-dependent generator-interaction at the uncertainty ceiling.

## 4. Execution proof, negative knowledge, currentness, custody

Standalone independently implemented Python3 source referee:
research/mech-s10/2026-11-22/code/mech_s10_rot008_modern_generator_pchip_raw_referee.py
Git commit **47bba53bf159d663b9cbe759b2647e3623710dff**, blob **47ddfc026ad4fac5de3ac4300bae5b1e46b9ba5b**. Parent first version had an overly strict >=40-grid-points check; that would exclude original **083's 28-node** j22/j62 frozen source series. It was corrected BEFORE executing GHA to >=20, preserving distinct 083 vs 085/090 source-grid requirements. No post hoc result-based numerical parameter choice.

One-shot source-only GitHub Actions workflow commit **47141d54e236ba6fe011c5b15569528e4ace0a84**, run **44994444431**, job **137122329638**. Source reader and 32-root checker actually completed **SUCCESS**, no Julia/network/native generator. Authentic immutable artifact **14743347010** downloaded, original ZIP **4198 bytes**, SHA256 **841f5daff6061fcd9ce7d4e5d86a1d12679f84273b271f8cebb604852c65a739**, provider digest same, ZIP CRC PASS, original 4/4 internal SHA-256 PASS. Original raw result JSON SHA256 **73bf76b7ce85baba54e849108f982971c1d87be1f23ae6ec11fae7bf995ca9c1**, original runner stdout SHA256 **877a749f9737eb90da908aac689103dc4bc83a97c4c6a813f3a5630893f24577**; independent container readback of actual downloaded bytes verified 32 roots, 8 cases, gate and checksum. Native owner 090 data and synthetic PCHIP were not changed.

**No new human-authorized physics run required**; computational work was source-only and bounded. No scientific owner sign-off assumed from GitHub/Slack dispatch; subsequent Badacz/REC13/AUD3/Moderator appraisal is separate. If review identifies a material time-varying event, MC construction or physical transfer defect, revisit source interface in owners' bounded processes, not by silently promoting this PCHIP stability result.

FINAL:
ROT008_SEVEN_ORIGINAL_RAW_GIT_SHA_PASS / INDEPENDENT_32_LINEAR_ROOTS_OWNER_EXACT_PASS / 32_ALTERNATIVE_PCHIP_CROSSINGS_PASS / 8_GENERATOR_DELTAS_PCHIP_MAX_0P000876_DEX / CONDITIONAL_MC_PLUS_INTERP_MOD_INTERMEDIATE_STABLE / SOURCE_ONLY_GHA_44994444431_SUCCESS / NO_NATIVE_JULIA / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
