---
artifact_id: IW_MECH_S9_ROT015_ORIGINAL_WUXU_NATIVE_RATE_TABLE_NODE_TIME_GATE_AND_B1_SOURCE_INPUT_HOLD_001_20261113
created_at: 2026-11-13
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
document_type: FROZEN_ORIGINAL_AUTHOR_NATIVE_OUTPUT_SOURCE_TIMING_GATE
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: SINGLE_FROZEN_AUTHOR_10D_MODEL_SOURCE_DIAGNOSTIC / NO_NEW_NATIVE_RUN / NO_PHYSICAL_BBN_PBH_BOUND / NO_HADRON_SOURCE_UNCERTAINTY_CLAIM / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# Mech-S9 ROT015 — native original-source hadron rate-table boundary on actual j22 trajectory

## Source and precedence

Original Wu–Xu source code: `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`, original `main-scan.jl` blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`. The authors originally supplied rate table `arXiv-2509.05618/data/out/hadrons_from_PBH.dat` Git blob `06d0883a27b108692720422294ba2baacd381a64`; **first native tabulated PBH mass** `5.609588603804452e32 GeV`, corresponding to approximately `1e9 g`. Original interpolator `tool_script-hadrons_from_PBH.jl` blob `cc73432910f872d526113ce59b6204f38d0766a9`: five channel rates used with a log-log interpolation and explicit `ExtrapolationType.Linear`; this is a model *extrapolation* below the lowest data node. Original `main-scan-parameters.jl` blob `53faee65beda383348580c28d0424188da69b660` sets `beta_max=1e-17`.

**PRIOR FINDINGS FIRST**: PRF13 ROT017 first quantified source extrapolation dominating the model hadron *number* count below the first tabulated node; LT8 ROT017 independently recalculated approx `81.36–81.44%` for five hadron channels in the j22 original source approximation. This ROT015 does NOT reassign those findings. LT8 first identified raw-vs-effective hadron floor in source; Mech-S9 ROT012/013 first executed one original native j22 10D 10000-point six raw history; INT9/MT15/REC11/AUD2 separately audited and analyzed on-path weak comparator. No causal physical novelty inferred.

## Distinct new measurement: *when* the real original native 10D code enters extrapolation regime

No new Julia calls. Use the **original exact recorded output** from pre-existing Mech-S9 source-native Actions run `43436800793`, artifact `14045176436`, original untouched ZIP SHA256 `71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486`, original 10000-row source CSV `author_native_raw_hadron_history_10000.csv` SHA256 `45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1`. The original source run is j22 (`M_ini=1.12117445647096e9 g`, `log10 beta=-16.9974609375`), and source state is not a final historical JCAP Figure 5 producer identity.

The original source mass time series crosses 1e9g **between original saved ONE-based rows 8383 and 8384**, while PBH remains active:

| Actual source row | M_PBH (g) | source time (s) | T_SM (MeV) | Xn |
|---|---:|---:|---:|---:|
| 8383 | 1,000,140,439.8666 | .0972118115885253 | 2.75822367709356 | .398100115476821 |
| 8384 | 999,087,914.133578 | .0979615356055445 | 2.74765550972953 | .397900874762395 |
| 8544, last sampled PBH-active | 144,891,220.526512 | .334927351810113 | 1.48824851749403 | .47097045071722 |
| 8545, first sampled PBH-zero | original sentinel mass 1.47268711730633 | .33751037021169 | 1.48260941885709 | .472697125696049 |

Linear interpolation ONLY between saved source rows 8383–8384 estimates crossing `t≈.09731184823146293 s`, `T≈2.75681355288638 MeV` and `Xn≈.398073530531221`; **these are NOT certified exact continuous event location**, and original Julia ODE error remains unquantified. The extrapolation window between this sampled crossing estimate and first recorded zero-PBH time lasts about `.240198521980227 s`, **71.1677456990646%** of the modeled pre-zero output-time interval (`t≈.33751037 s`), not a duration certified in the continuum.

The observed decrement in mass between *initial native mass and LAST saved PBH-active sample* has about **87.5881863%** below the first table node. The mathematical FULL-EVAPORATION mass decrement to ideal zero has **89.1921854%** below that node. This latter figure is a **limit relying on zero final PBH mass**, NOT the fraction resolved by the final saved live-mass sample; a large model mass decline occurs between rows 8544 and 8545, where the source sets nPBH to zero. Keep these denominators distinct.

The source-recorded neutron fraction changes from approximately `.39807353` at the table-node crossing to `.47269713` at first sampled PBH-zero, a descriptive **+0.07462360** change. **DO NOT** attribute this change to subgrid hadron emission: source neutron fraction is driven by weak SM background, neutron decay, hadron conversions, and source dynamics simultaneously. The native 10D record is ONE factual trajectory, no counterfactual control.

The same original source beta `1.0058635310570255e-17` is **0.5863531057% ABOVE original scan beta_max=1e-17**, i.e. an original `magic()` callable out-of-grid point, NOT a published beta scan node. This material domain fact was first registered by Mech-S9 ROT014; no novelty firstness claim here.

## Reproduction and negative tests

Executed new standalone standard-library Python checker directly on the original 713794-byte source native ZIP, reading the archived CSV (not retyping trajectory values). Checks: ZIP CRC; outer immutable SHA256; 16/16 original archived per-member SHA256 manifest; exact upstream main-source SHA256 and one original `magic()` call metadata; all 10000 time-ordered records; actual PBH zero switch; first mass-node sign crossing and linear saved-sample interpolation; table/subgrid time fraction and DISTINCT mass decrement denominators; beta bound. Positive clean replay produces byte-identical JSON PASS. Deliberately modified single raw ZIP CSV byte (with outer ZIP re-created) rejected before numerical calculations, PASS negative control.

Exact locally executed script `mech_s9_rot015_native_first_table_node_gate.py` SHA256 `6748ab5460dc67362a62a8e95147e8eeb7d20d888105b6661ee7b6b23eef9efd`, JSON SHA256 `c52ecd97a57958267d3857f5a9869e59b8c2edfdb4726e97d88ad4a14c997c23`. Conversation-local *self-contained* reproduction ZIP includes original source artifact, exact script, JSON, README, four SHA256 manifest entries, checksum `a84d1a2c80b08d82bcedc5e13203a3f8350e4edcf47db12cb13ddb88421ba2fa`; CRC PASS, 4/4 outer file SHA PASS, original 16/16 internal SHA PASS, isolated clean replay byte-identical JSON PASS. The ZIP is a **conversation-local artifact**, not claimed stored in GitHub or BW. Original author native source ZIP is preserved via GitHub Actions as cited.

## 30-day B1 decision / stop gate

Current date 2026-11-13. Read Moderator-accepted B1/C1 30-day protocol `IW_NASH_30_DAY_EXTERNAL_RESULT_DECISION_PROTOCOL_001_20261113` pinned private `ffc0d011706617aeb38ea90abd62f40626353fad`. Mech-S9 ROT014 already ACKed co-owner native source, Badacz ACKed separately; proposed primary B1 endpoint `X_n(T_nuc)`, secondary `Y_code=2X/(1-X)` as code observable NOT physical helium, but Moderator+INT9 have NOT yet frozen a test intervention or source-anchored subgrid generator uncertainty class. **No specific approval for additional Julia runs** found; NONE executed in ROT015.

Recommended narrow B1 direction: only a nontrivial physically and source-verified hadron-generator uncertainty/intervention below 1e9g, with source provenance for the perturbation and original 10D endpoint+solver tolerance controls, can credibly test whether subgrid production drives a stable outcome beyond mature ODE theory. Without independent generator data/uncertainty, arbitrary ±25% or similarly chosen hadron emission factors are mathematical counterfactuals, not physically calibrated uncertainties, and would NOT meet scientific novelty gate. Under current evidence B1 is `SOURCE_NATIVE_REPRODUCIBILITY_PASS / INPUT_HADRONIZATION_UNCERTAINTY_HOLD / PHYSICAL_PBH_CLAIM_HOLD`. Ask Moderator to freeze or explicitly HOLD; do not initiate an open-ended mass-grid scan or task cascade.

**Strict ceiling:** native 10D source timing diagnostic only; published final paper generator identity and E4 BlackHawk/PYTHIA provenance unverified; raw/effective numerical floor correction is tiny for j22 in existing native source, but no physical claim from that. NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE.
