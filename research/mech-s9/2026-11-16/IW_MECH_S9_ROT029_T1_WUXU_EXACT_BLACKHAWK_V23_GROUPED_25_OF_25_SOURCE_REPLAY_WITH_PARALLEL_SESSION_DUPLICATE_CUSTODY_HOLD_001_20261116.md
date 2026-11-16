---
artifact_id: IW_MECH_S9_ROT029_T1_WUXU_EXACT_BLACKHAWK_V23_GROUPED_25_OF_25_SOURCE_REPLAY_WITH_PARALLEL_SESSION_DUPLICATE_CUSTODY_HOLD_001_20261116
created_at: 2026-11-16
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
document_type: ORIGINAL_SOURCE_GENERATOR_T1_CUSTODY_INCIDENT_AND_READ_ONLY_INDEPENDENT_EVIDENCE_REFEREE
exposure: PUBLIC
state: T1_GROUPED_SOURCE_25_OF_25_ADMITTED_PASS / SECOND_RUN_ACCEPTED_AS_TECHNICAL_RETRY_BY_MODERATOR / HISTORICAL_DUPLICATE_DISCLOSED / T2_T3_E4_PHYSICAL_GATES_HOLD
claim_ceiling: NO_PHYSICAL_PBH_BBN_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_THIRD_T1_RUN / NO_NEW_JULIA
---

# ROT029 — T1-GROUPED 25/25 source PASS, duplicate-session incident preserved, Moderator admission received in ROT030

> **DATED GOVERNANCE ADDENDUM — 2026-11-16, ROT030 (supersedes only prior custody HOLD):** Moderator subsequently stated directly to Mech-S9: **„Decyzja była o dopuszeniu”**. Therefore the second source workflow (GitHub Actions `43911520867`) is **admitted** as a technical retry of the first interrupted 100-primary-vs-500-secondary parser execution (`43911170672`). Previous status `MODERATOR_CUSTODY_DECISION_PENDING` is **CLOSED**. This is a controlling Moderator decision relayed in the conversation; no invented timestamp, signature, or separate authorization artifact is claimed. The two overlapping runs, exact source/executable hashes, parser failure, initial session coordination failure, and original prereg remain in full documented history below. Evidence: [bridge issue #16, admission record](https://github.com/wmakiela-tech/Nash-iw-research/issues/16#issuecomment-6927998998); [Slack relay](https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1794860096229409). **Current source result:** `T1-GROUPED_SOURCE_ADMITTED_PASS`, 25/25 rates, max relative mismatch `7.734157758676474e-11`, versus prereg `1e-5`; `T1-PERSTATE` fails (50%). **Not promoted:** physical error in publication, PBH bound, B1 full Q-B claim, T3 prior art/errata, E4 hadronizer uncertainty, independent GPT-family T2 review. NO_NEW_JULIA / NO_THIRD_T1_RUN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.

## Historic ROT029 report (preserved with its as-of-publication pending disposition)



## Firstness and previous science

Original scientific and code firstness: Arbey and Auffinger (BlackHawk v2.3), Wu and Xu (BBN model, published five-channel rate table and original overlay and producer notebook). MT14 first SHA-downloaded official v2.3 on November 1 (extraction blocked), Mech-S9 ROT025 first directly extracted genuine full original tar and 15 original BBN tables, ROT027 first proved current-versus-old PYTHIA numerical difference over all five sources. Badacz first performed separate B1 E5/E5b and native source variants and owned T2 original Julia test, which finished in REVIEW_071 with owner W-PASS, ORD-PASS, TOL-STABLE and 0.272–0.301 dex root shifts. **No firstness of the native BBN result, physical PBH bounds or new hadronization methods is claimed here.**

Controlling Moderator decision transmitted 2026-11-16 16:47 CET approved T1 (Mech-S9 original source five-mass reconstruction) and T2 (Badacz Julia) as *separate defined tests*. Mech T1 prereg was frozen BEFORE BOTH workflows at original commit `c896351e537d79c401eee9a36a80cfac3a47f19d`, original body Git blob `720320a3f24b63a3fa8482dcfb8413a28db5598e`. It fixes original mass-grid indices zero-based `[0,22,49,74,99]`, five groups `pipm,Kpm,K0L,proton,neutron`, original official v2.3 PYTHIA BBN choice0, 100 **PRIMARY** energies [5,100000] GeV, 25 comparisons to `hadrons_from_PBH.dat`, strict max absolute RELATIVE difference `1e-5`, hypotheses grouped or divided-by-two four charged/nucleon groups, and `T1-GROUPED/T1-PERSTATE/T1-NOREPRO`. A source-faithful explicit **PRE-EXEC** erratum at commit `9feb28e014f0256490cfd72ee10ac009580ab782` corrects the parser's conflation of primary `E_number=100` with PYTHIA BBN SECONDARY output table `nb_fin_en=500` without changing any mass, group, hypothesis or gate. Its status before second run is source-checkable.

## Material procedural incident — ALL run attempts preserved

There were unexpectedly **TWO overlapping GitHub Actions original-source T1 workflows initiated from parallel Mech-S9 chat sessions**, despite only one source test authorized. This is not to be hidden or reinterpreted as an independent replication:

| Property | FIRST original run | SECOND overlapping run |
|---|---|---|
| Workflow run ID | `43911170672` | `43911520867` |
| GitHub head commit | `45a1ea1647a857e53d667cf4536f1a2e23fb5603` | `6b3aed8f569c020363bae1e5cc0b3ce250ad3a9a` |
| Start UTC | `2026-11-16T16:46:23Z` | `2026-11-16T16:48:17Z` |
| Workflow conclusion | GitHub job SUCCESS | GitHub job SUCCESS |
| Actual C source calls | One initial mass `j=0`, then Python parser aborted | FIVE exact predefined masses `j=[0,22,49,74,99]` completed |
| Scientific workflow result | `T1-NOREPRO` **because runner erroneously asserted 100 output rows, actual source returned 500**, no 25-cell verdict | `T1-GROUPED` on 25 source cells |
| GHA output artifact ID | `14247857006` | `14249230100` |
| Actual downloaded immutable artifact ZIP SHA256 | `e08930dd72f855a8d9bbc1d1b036d97a80f397ef35ab7bc384dea1c8cac620f1` | `4f6d3cbd0b58f455bdc60935177e78f24da51de1d1b7b05929c953f60ea8142b` |
| Compiled original author patched `BlackHawk_inst.x` SHA256 | `17da5c5bd9d2958c18ee2c31e1f8236b12be69902795c23e947d8da70eded221` | **exact same SHA256** |

FIRST run `43911170672` produced `T1_SOURCE_COMPARE_RESULT.json` with error `AssertionError: ('unexpected source E_number', 500)` in parser, although original BlackHawk C returned normally on first mass and its log explicitly shows loading `./src/tables/hadronization_tables/pythia_tables/pipm.txt` and corresponding current `Kpm/proton/neutron`, source output `instantaneous_secondary_spectra.txt`. It is NOT valid to report this first result as a scientific rejection of either group-normalization hypothesis. It failed at the representation layer and had NO full 25-cell scientific conclusion.

SECOND run `43911520867` completed with exact same original compiled executable source identity, the same five prereg masses and hypotheses, after source-faithful correcting secondary 500 energy nodes before execution. However the SECOND launch was NOT preceded by an independently identified, second explicit Moderator run authorization; the parallel Mech-S9 instance failed to detect the first already underway. This is a **process custody violation / potential unauthorized duplicate**; the workflow succeeded before the issue was discovered, and no tool could un-execute it. Mech will NOT silently ratify this run or treat first+second as independent confirmatory replication. It preserves both source artifacts, reports the scope overrun, and requests the Moderator to decide explicitly whether the second run may be accepted as a *technical retry of the first prematurely aborted T1* under the original scope or should remain quarantined from governance. **No THIRD run authorized or planned.**

## Source authenticity and independent quantitative result in SECOND run

The second workflow original BlackHawk `v2.3.tar.bz2` has exactly 161495983 bytes and SHA256 `dd148349304c158ed3509ea6935f2fd3d60ebe7cda4c34598aa99ea329c129a7`, **directly equal Wu–Xu frozen `Artifacts.toml` blob `324cb54a...`**. All THREE original Wu–Xu overlay Git blobs match the frozen author commit `d395183674cace6c9906a8911bdeb7234ba4040d`: `BlackHawk_inst.c` `f517b0a7...`, `BlackHawk_tot.c` `76758e05...`, `src/include.h` `3a1eaefd...`. Actual compiled `BlackHawk_inst.x` SHA256 `17da5c5bd9d2958c18ee2c31e1f8236b12be69902795c23e947d8da70eded221` equals first runner's binary (a material independent build-identity match).

Original overlay `//#define HARDTABLES` is COMMENTED; relevant Makefile has no `-DHARDTABLES` flag. The original readout is from current `src/tables/hadronization_tables/pythia_tables/` raw BBN tables, NOT `old/` and not present-epoch `pythia(new)`. For example current `pipm.txt` SHA256 `603f8b1a53efe316b4378da9a6242c1a1b3be026c17fbdaa917cb07f13850ac4` and archival `old/pipm.txt` `39306be56e4feeeb361c23983e64b7c4f193c60be4ffa7211b745275cad679fa` are distinct, while author reference `hadrons_from_PBH.dat` is exact Git blob `06d0883a27b108692720422294ba2baacd381a64`.

Mass points actually generated (gram units using original first table mass as source unit anchor): `j0=1e9`, `j22=6.316227669701322e9`, `j49=6.06509731409678e10`, `j74=4.9254836571028394e11`, `j99=4.0000000000000005e12`. Each C source output has **500** secondary energy values and the exact five expected columns, generated with original PYTHIA BBN choice0, original 100 primary energies and specified mass.

Original Wu–Xu notebook source `valid_hadrons_from_BlackHawk.ipynb` Git blob `8a10396ae771b17059808fc2b91235dd194cba8d` defines `h = mean(diff(log E_secondary))`, and five rates via `h*(sum(E_secondary*dN/dtdE)-0.5*(first+last))` with conversion `NU.s` to GeV. Second run used `hbar=6.582119569e-25 GeV s` and produced a uniform near-one constant ratio, likely due only to a minute unit constant difference but exact cause not separately certified.

**All 25 source ratios** `R_reproduced_group / R_original_author` are approximately `0.999999999922658` for every one of five source groups and five masses, with maximum preregistered relative group mismatch **`7.734157758676474e-11`**. Group hypothesis is far inside `1e-5`; per-final-sign/antistate alternative (divide `pipm,Kpm,proton,neutron` by 2, `K0L` unchanged) has maximum relative mismatch **`0.5000000000386708`** (50%). Within exact frozen numeric test definitions SECOND workflow returns **`T1-GROUPED`**.

This is direct strongly corroborating source evidence that **Wu–Xu published five-column rate table stores BlackHawk original charge-aggregated GROUPED rates**, not half-perstate rates, consistent with original v2.3 PYTHIA signed PDG counters. It raises a material interpretation question because original `main-scan.jl` injects full `R_pi` into BOTH `pi-` and `pi+` 10D species; one `Kpm` group feeds `K-`, and similarly proton and neutron groups feed only anti-p/n. However actual impact on final BBN Yp/PBH exclusion is not measured by this T1-only code reproduction and Badacz T2 remains conditional. No assertion of a physical factor-of-two error in final published contours, no physical independent generator uncertainty, no article novelty or canon.

## Independent local source-output verification (NO third provider execution)

Actual downloaded second GitHub artifact ZIP `mech_s9_rot029_DUPLICATE_QUARANTINED_T1_evidence.zip` SHA256 **`4f6d3cbd0b58f455bdc60935177e78f24da51de1d1b7b05929c953f60ea8142b`**; ZIP CRC PASS; **24/24 nested GHA manifest SHA PASS**. For all five actual C-produced `instantaneous_secondary_spectra.txt` files individually SHA-pinned by its machine JSON, independent newly authored Python stdlib numeric referee re-parsed 500x11 source samples, checked strictly increasing energy, regenerated all 25 log-energy trapezoid integrals independently from the generated JSON, and confirmed **25/25 source rates to <1e-14 relative** against original processor; max group relative diff `7.734157758676474e-11`, max perstate diff `0.5000000000386708`. No BlackHawk, Julia or any other original physics code was called during this referee step.

Actually executed independent referee `mech_s9_rot029_independent_source_output_referee.py` SHA256 **`ad871ea63b51bb61f53bce53c3f80180b8eadca1ee16909d0e66272462f92aed`**, actual full 25-row result `mech_s9_rot029_independent_referee.json` SHA256 **`af5a133bc880af2d59d8551cc7a68ba87907e90a25bfbd7f75a289077e5e91a1`**. User-conversation-local evidence package `mech_s9_rot029_T1_grouped_source_PASS_PROCEDURAL_HOLD_evidence.zip` SHA256 **`e8c52e9f4c78621b08121b6674ccaf0ce27419daa7ddd3baa17f058d581c0317`**, includes both immutable first and second Actions artifact ZIPs, new independent referee source+JSON, README and 5 SHA manifest; outer CRC and 5/5 SHA checks PASS. No original 161MB tar redistributed.

## Governance and next owner decision

**Scientific source status:** `T1-GROUPED_SOURCE_REPLAY_25_OF_25_PASS` on SECOND runner, with 25-cell relative max `7.734e-11`. **Formal custody status:** `HOLD_DUPLICATE_SECOND_RUN_PENDING_MODERATOR_DISPOSITION`. In B1 project governance do NOT promote this to T1 release, T2 physical Yp/PBH contour correction, or independent replication until Moderator acknowledges and explicitly decides whether this technical retry was within original approved T1 or is excluded.

Specific contemporaneous Slack incident disclosure: https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1794848181053449?thread_ts=1794844748.245419&cid=C0BV1J3SYLT . Shared Github issue #16 https://github.com/wmakiela-tech/Nash-iw-research/issues/16 to be updated; request to Moderator as CUSTODY_DECISION_REQUIRED, not ask for extra run. Badacz already ACKed bridge and completed independently authorized T2 REVIEW_071, while later Q-A is separately approved, outside T1.

The intrinsic typed scientific conclusion about source grouped rates does not automatically resolve T3 scholarly prior-art, physical hadronization uncertainties, or native 10D reference-sensitivity (Badacz PREREG_066). Do not call this published PBH exclusion corrected without separate science and independent referee.

**HISTORICAL FINAL (prior to ROT030 decision; see controlling addendum above):** `ROT029_ORIGINAL_AUTHOR_V23_5MASS_25CELL_GROUPED_SOURCE_PASS / T1_PERSTATE_REJECTED / PARALLEL_SESSIONS_TWO_WORKFLOWS_DISCLOSED / FIRST_SOURCE_PARSER_500VS100_FAIL / SECOND_SOURCE_CONDITIONAL_PASS / MODERATOR_CUSTODY_DECISION_HOLD [SUPERSEDED BY MODERATOR_ADMITTED_PASS] / BADACZ_T2_OWNER_RESULT_CONDITIONAL / NO_THIRD_T1 / NO_JULIA / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / GITHUB_PENDING_BW_INGEST`.
