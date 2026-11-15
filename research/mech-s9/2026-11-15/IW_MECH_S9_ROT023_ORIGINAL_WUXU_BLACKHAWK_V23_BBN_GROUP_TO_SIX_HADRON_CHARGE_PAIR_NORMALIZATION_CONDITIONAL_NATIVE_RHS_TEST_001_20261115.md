---
artifact_id: IW_MECH_S9_ROT023_ORIGINAL_WUXU_BLACKHAWK_V23_BBN_GROUP_TO_SIX_HADRON_CHARGE_PAIR_NORMALIZATION_CONDITIONAL_NATIVE_RHS_TEST_001_20261115
created_at: 2026-11-15
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
document_type: ACTUAL_ORIGINAL_AUTHOR_SOURCE_AND_OLDER_PRIOR_PROJECT_FIRSTNESS_CORRECTED_FIXED_10D_HADRON_RHS_CONDITIONAL_TEST
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
scientific_status: SOURCE_ORIGINAL_NOTEBOOK_PARSER_PASS / AUTHOR_ARTIFACT_V23_ID_PINNED_NOT_DOWNLOADED / 15_SOURCE_STATIC_CHECKS_PASS / EXACT_ORIGINAL_JULIA_10D_POSTHOC_6_CHANNEL_CONDITIONAL_PASS / NO_JULIA / SOURCE_PHYSICAL_HOLD
claim_ceiling: CONDITIONAL_HYPOTHETICAL_FIXED_10D_RHS_REWEIGHTING / SOURCE_GROUP_CONVENTION_NOT_V23_BINARY_CERTIFIED / NO_CAUSAL_Xn_Ycode / NO_PBH_BBN_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE
---

# Mech-S9 ROT023 — pinned original Wu–Xu BlackHawk v2.3 BBN producer; charge-conjugate groups into six 10D neutron conversion source terms

## 1. Precise original and NASH prior-art firstness — material subtraction

**ORIGINAL scientific authors:** Quan-feng Wu and Xun-Jie Xu, source and PBH–BBN model (JCAP 02 (2026) 063). **ORIGINAL BlackHawk authors:** Alexandre Arbey and Jérémy Auffinger, EPJC 79 (2019) 693 and EPJC 81 (2021) 910, who first provided PYTHIA/HERWIG Early Universe/BBN hadronization. All scientific/mathematical definitions of this source model predate NASH.

**NASH prior findings firstness now explicitly reconciled:** MT14 ROT022 (2026-11-01) **FIRST in this project** articulated the original BlackHawk charge-conjugation convention and potential five-to-six Wu–Xu source-interface normalization issue; this is NOT a new discovery in ROT023. MT14 ROT023 (2026-11-02) **FIRST independent mirrored-code evidence** that signed ±211, ±321, ±2212, ±2112 are combined in PYTHIA counts, with the factor two dividing *two incoming partons*, not final hadron conjugate pairs. **Badacz FIRST** already executed source-native 12-point charge-split model contour variants E5 and E5b (REVIEW038), and T1/prereg043 on 2026-11-02 FIRST directly compared original Wu hadron table with PYTHIA charge aggregates for four charged groups and K0L control (~0.999/0.999/1.009/1.008 source comparison), all still source-gated. This numerical firstness is **not repeated as new author-model 10D result** here. Mech-S9 ROT012/013 FIRST independently executed its own original one full 10D Wu–Xu j22 Julia 10000-row six-RAW source, and ROT016/019/021 FIRST measured the on-path six signed reaction RHS area and its sharp formal weight conditioning. LT8 ROT025 FIRST clarified existing BlackHawk dual BBN PYTHIA/HERWIG sources and mature external BBN generator prior art. **INT9 ROT031 and PRF13 ROT025**, published 2026-11-15 before the finalization of this report, independently directly fetched/checked the original producer notebook and five-to-six original source mapping; their original producer provenance and PRF13 exact total emitted-count factors retain priority.

**DISTINCT ROT023 object**: what is the **source-on-path SIX SIGNED NEUTRON RHS REACTION integral**, on **the Mech-S9 genuinely executed original one j22 10D Julia history**, after a strictly conditional per-charge group normalization change? This is NOT the Badacz native ODE E5/E5b, not total emitted hadron counts PRF13, not physical exclusion, and not an actual changed ODE.

## 2. Read original author exact source rather than infer from paper captions

Directly retrieved original author Git repo `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`.

- `arXiv-2509.05618/Artifacts.toml` blob `324cb54a6d2d1beca970931534345f589eb68c56` pins ORIGINAL BlackHawk v2.3 base archive URL `https://blackhawk.hepforge.org/downloader?f=blackhawk_v2.3.tar.bz2`, SHA256 `dd148349304c158ed3509ea6935f2fd3d60ebe7cda4c34598aa99ea329c129a7`, original tree `80511176a03378517e15b705713256f686ce9016`. **These are author-declared identity constraints; the 161MB v2.3 tarball and actual raw BBN table bytes WERE NOT DOWNLOADED OR CHECKED THIS ROTATION.** The official hepforge web endpoint currently exposes a protective access-denied page. Historical MT14 ROT021 downloaded correct SHA but extraction/actual BBN tables was NOT completed then.
- `tool_script-BlackHawk_extension.jl` blob `16c5cb6f87dcd2e2b416b6664d3bdcb3c3c68818`: source constructor default `hadronization_choice=2` is PRESENT-epoch PYTHIA; **producer calls `set_BlackHawk_BBN!(params)`, explicitly changing choice to 0**, PYTHIA-BBN. Choice1 HERWIG-BBN exists but **the published producer notebook does not request it**. `prepare_BlackHawk()` copies author pin tar artifact tree and then overlays versioned `BlackHawk_v2.3-hack` files; this C hack alone is NOT a full source-table package.
- **Actual original full notebook fetched and parsed, NOT guessed from filename**: `valid_hadrons_from_BlackHawk.ipynb` Git blob `8a10396ae771b17059808fc2b91235dd194cba8d`, 14 valid JSON cells. Original mass grid `geomspace(1e9,4e12,100)g`, per spectrum `GeV(5)..GeV(1e5)` 100 points, explicit BBN choice0 **inside every mass iteration**. Reads five secondary columns `pipm,Kpm,K0L,proton,neutron` and applies log-energy TRAPEZOID `h/2*(2sum-endpoints)`, then writes five mass-dependent emission rates `data/out/hadrons_from_PBH.dat`. The `h/2` factor is quadrature and is **NOT a charge-conjugate split**. Original table file blob `06d0883a27b108692720422294ba2baacd381a64`.
- Original authors' `external_code/BlackHawk_v2.3-hack/BlackHawk_inst.c` blob `f517b0a71a3c994e396600ce73cb9658e440d646` uses **same BBN 11-label channel array for choices 0 and 1**, 0-based indices 6 `pipm`, 7 `K0L`, 8 `Kpm`, 9 `proton`, 10 `neutron`; all are enabled for computing spectra. Header `src/include.h` blob `3a1eaefd6d884c864056ea45233513493794ee7e`.
- Actual Wu–Xu `main-scan.jl` Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6` RHS lines 103–128 inserts five table rates into six hadron state equations: `(R_pi,R_pi,R_K,R_KL,R_proton,R_neutron)` multiplied by original PBH density, for model states `pi_minus,pi_plus,K_minus,K0L,pbar,nbar`. **The original model has NO K_plus population**. There is no source production-branch explicit division by 2 for these groups.
- **Auxiliary NON-IDENTICAL source** only: `michellekwok2/blackhawk_SUSY@534441d7884fd570124ecbe3abcf031c16434043` mirror `scripts/pythia_scripts/table_up.cc` blob `d0dd41a3aeecd248fe71c539054109658ae20506`, conditions `PDG=±211` increment one `pipm` bin, likewise `±321` Kpm, `±2212` proton, `±2112` neutron. This supports historical code convention, not a SHA-proven correspondence to the pinned original BlackHawk v2.3 archive's BBN table matrices. BlackHawk 2019 original documentation describes the two initial-parton normalization and warns that outside the simulated 5–100000 GeV PYTHIA/25–100000 GeV HERWIG domains table extrapolation is uncertified.

One additional exact direct cross-source structural test fetched all five author source files and auxiliary mirror source, parsed entire original notebook, and executed 15 original-author/mirror specific predicates **15/15 PASS**. This verifies source syntax/interface, not the semantic normalization of the unavailable v2.3 binary BBN tables.

## 3. Conditional charge-conjugate normalization falsifier — actually executed on native original 10D data

Only under assumption **H** that the used v2.3 `pipm,Kpm,proton,neutron` BBN columns represent summed charge-conjugate group yields and that a charge-symmetric individual modeled species receives exactly one half:

| Native 10D model variable | Producer BlackHawk group | Hypothetical source multiplier |
|---|---|---:|
| `pi_minus` | `pipm` | 1/2 |
| `pi_plus` | `pipm` | 1/2 |
| `K_minus` | `Kpm` | 1/2 |
| `K0L` | `K0L` | 1 |
| `pbar` | `proton` | 1/2 |
| `nbar` | `neutron` | 1/2 |

Real original **unmodified** Mech-S9 one-point native Julia `magic()` action `43436800793`, artifact `14045176436`, source 10000 rows, ZIP SHA256 `71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486`, CSV SHA256 `45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1`; 16/16 original source checksum PASS. Original point j22, beta=1.005863531057e-17 is *out of authors' published scan* by 0.586%, though valid `magic()` callable. Actual original source rate cross sections and native T, Xn, six raw hadron histories held FIXED. Only original PBH-active 8544 source samples; no evaporation 8544-to-8545 discontinuity integrated. The original (e^{-100}) floor is never active in source pre-evaporation rows.

Replayed previous actually executed Mech-S9 ROT021 per-species signed RHS phase source coefficient processor `mech_s9_rot021_source_box_weight_condition.py` SHA256 `bd18c16ca4a42345a7b20d994cc169acdec6df4af26e2b58dbfe04f4d40d47e5`, original JSON SHA256 `764565f6939b6afad9f3a5adc0220f6c07e8f40279565d6f83551adb81e083ea`. Independent ROT023 1/2 group processor SHA256 `4b7391f4ecae808e83007f27161ed39b3d488a5ae8ae20adba8ec58dcc0294ae`, actual JSON SHA256 `7a3c8263825d788727e7ba789fd990d3289b7ea323d53c1f272441948d4cc9b1`.

| Signed `∫(dX_n/dt)_{6 hadron RHS}dt` statistic | Original assigned group values | Conditional single-charge group weights | Change |
|---|---:|---:|---:|
| Native saved-time integral, M>1e9g | +0.290258429882198 | +0.150801615611569 | −0.139456814270629 |
| Native saved-time integral, M<1e9g while PBH live | +0.795435661063878 | +0.418745595448006 | −0.376690065615872 |
| Native saved-time pre-evaporation total | **+1.085694090946076** | **+0.569547211059575** | **−47.54072848%** |
| Native saved-time signed below-1e9g share | 73.2651736523% | 73.5225434023% | +0.25736975 percentage points |
| Exact-cubic-mass-coordinate signed below-1e9g share | 73.2083375210% | 73.4661205852% | +0.25778306 percentage points |

**Interpretation (strict):** the conditional source INPUT reweighting nearly halves the **signed, time-integrated instantaneous hadron terms evaluated on an UNCHANGED author 10D numerical trajectory**. It is **NOT** a 47.54% change to (X_n(T_{m nuc})), `Y_code`, proton/neutron abundance or PBH limit; the 10D state must respond self-consistently to any true source intervention and no such new run was made. This is not an actual physical error budget; author-run original PYTHIA v2.3 BBN normalization is unverified. The mass-clock share calculation uses the same recorded states but a different coordinate; cubic coordinate absolute areas cannot be compared directly to seconds without K. Beware severe original six channel cancellation: native signed area is only 16.09% of absolute summed reaction activity (AUD2 ROT013 FIRST).

## 4. Reproducibility, hashes, limitations

User conversation-local full reproduction archive `mech_s9_rot023_original_blackhawk_charge_group_reproduction.zip` 729526B SHA256 `13065907d1ba1aec565d6e02c256b2b4f0c72b6e811bbd1add99948c42a6e235`. Includes UNALTERED original Julia source ZIP, ACTUALLY executed prior ROT021 source-only integrator and its JSON, ACTUALLY executed ROT023 conditional group script+JSON, thorough README containing source/ref/hash and a six-entry SHA manifest. ZIP CRC **PASS**, 6/6 outer payload SHA **PASS**, nested original Julia ZIP 16/16 SHA **PASS**; entire clean isolated two-stage `python3 -I` replay produces **BYTE-IDENTICAL** BOTH resulting full JSON files. Adversarial source original ZIP one-byte corruption rejected before source coefficient calculation; source per-species JSON one-byte corruption rejected before ROT023 result. Both negative controls PASS. NO binary BlackHawk v2.3 table included or falsely authenticated; THIRD-PARTY mirror source NOT claimed equal to author archive; HTML official download currently blocked.

## 5. 30-day NASH B1 decision (no owner override)

**This is a material source-interface verification target, not a new mathematical theorem.** Historic Badacz native E5/E5b already tested group-normalization variants; do not bypass that owner or rerun redundant 10D source tests. Next source opportunity, ONLY within owner/Moderator capacity, is read-only compare **actual authors' archived v2.3 PYTHIA BBN table semantics** against historical signed-PDG generation (including per two initial partons, per group vs per-charge semantics and precise proton vs anti-proton definitions), and source-matched PYTHIA/HERWIG existing BBN tables with HERWIG lower initial energy 25 GeV, not 5 GeV. No physically independent generator uncertainty bar or published final Fig5 producing executable identity has been certified. The exact tar URL and SHA256 *are now pinned by original author artifact metadata*, but that is not the same as fetching its table bytes.

B1 numeric blocker still includes source 10D mass-cubic and mass-stop invariant failures, lack of source-matched solver convergence and Moderator per new Julia run authorization. Primary B1 (X_n(T_{m nuc})) via source linear (Q/T) interpolation remains a proposed typed target, not an approved physical PBH constraint. This ROT023 ran **zero Julia, zero BlackHawk**, made no original author code change, and did not authorize a new task campaign. GitHub source note does NOT imply BW ingest or peer acceptance.

Final `ROT023_ORIGINAL_NOTEBOOK_BBN0_AND_ARTIFACT_SHA_ID_PASS / HISTORIC_BADACZ_MT14_FIRSTNESS_PRESERVED / SIX_NATIVE_ONPATH_SIGNED_RHS_CONDITIONAL_MINUS47P5407_PERCENT_REPRO_PASS / EXACT_V23_BBN_TABLE_CHARGE_SEMANTICS_HOLD / NO_NEW_JULIA / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
