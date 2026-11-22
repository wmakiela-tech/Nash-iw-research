---
artifact_id: IW_REC14_ROT001_THOSS2024_BLACKHAWK21_HERWIG_USE_V23_EXPOSURE_SOURCE_VERSION_REFEREE_001_20261122
date: 2026-11-22
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_13 / REC14
exposure: PUBLIC
document_type: REVIEW
mode: PLANNED_NONBLIND_SUCCESSOR_FIRST_FUNCTIONAL_ROTATION / CLAIM_LOCAL_SOURCE_REFEREE / ONE_PUBLISHED_PRIMARY_ARTICLE / NO_NATIVE_SIMULATION
status: SOURCE_TEXT_VERSION_MISMATCH_PASS / SPECIFIC_V23_CHOICE1_USE_NOT_ESTABLISHED / PUBLISHED_PHYSICAL_IMPACT_HOLD
claim_ceiling: NO_EXTERNAL_NOVELTY_ESTABLISHED / NO_PHYSICAL_PBH_BOUND / NO_AUTHOR_ERROR_CLAIM / NO_I3 / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REC14 ROT001 — Thoss, Burkert & Kohri 2024: which BlackHawk version actually appears in the published HERWIG application?

## 0. Freeze: exact claim to test

Target proposition `P`: The published 2024 Thoss–Burkert–Kohri calculation is demonstrated in the original article to have used the **BlackHawk v2.3 HERWIG hadronization_choice=1 archived tables** implicated by an independently investigated source-variable labeling mismatch.

This is a **source-provenance question**. Do not substitute the broader and true proposition `Q`: "The 2024 paper cites BlackHawk and uses HERWIG for a middle energy regime."

One primary article is the bounded test. No author email, code execution, raw tarball extraction, or cosmological fitting was authorized or performed by REC14 here.

## 1. Primary source actually opened

V. Thoss, A. Burkert, K. Kohri, *Breakdown of Hawking Evaporation opens new Mass Window for Primordial Black Holes as Dark Matter Candidate*, **MNRAS 532** (2024), 451–459, DOI: 10.1093/mnras/stae1098.

Original publisher full HTML opened 2026-11-22:
https://academic.oup.com/mnras/article/532/1/451/7656972
arXiv record: https://arxiv.org/abs/2402.17823
Supplementary numerical-result archive (inventory only, not a reconstructed producer environment): https://zenodo.org/records/10718218

Primary publisher HTML §2.2 ("Secondary emission") states that, for their computation, they use HERWIG in the intermediate temperature regime, HAZMA below 0.1 GeV, and HDMSpectra above 100 GeV, with BlackHawk spectra as part of the model.

Crucially, the article's explicit **SOFTWARE** section enumerates **"blackhawk 2.1"** (together with exoclass, class, Montepython, Julia, matplotlib). This is positive original evidence of the *declared software version*; it differs from the version 2.3 whose exact archived table identity was checked separately in IW/NASH.

In this article's inspected HTML, no explicit runtime value of `hadronization_choice=1`, BlackHawk-v2.3 table member hash, exact runtime command, or archival code-produced secondary spectrum was found. This bounded observation is not a proof that such original inputs do not exist elsewhere.

## 2. Referee outcome — different propositions, different ceilings

- `Q` = "Thoss et al. 2024 use HERWIG for some secondary spectra": **SOURCE-TEXT PASS**.
- `P_version` = "The published software inventory declares BlackHawk 2.3": **FAIL_AS_STATED** — the inventory explicitly names **BlackHawk 2.1**.
- `P_bytes` = "This 2024 paper demonstrably consumed the exact BlackHawk v2.3 table bytes affected by the v2.3/v3.0 source convention problem": **NOT ESTABLISHED / HOLD**, because producer version and byte-level provenance are not pinned to the disputed catalog.
- `P_choice` = "The article proves its actual input specifically set `hadronization_choice=1`": **NOT ESTABLISHED / HOLD** based on opened published text. Mention of HERWIG does not in itself identify the entire BlackHawk invocation or kernel data provenance.
- `P_physics` = "Correcting a source labeling mismatch changes the paper's reported physical PBH constraints": **NOT ESTABLISHED / HOLD**. No source-native corrected-input rerun nor source-binned outcome sensitivity exists in this referee rotation.

This does **not** prove the older BlackHawk 2.1 catalog is free of the same energy-index mismatch. A different release number also does not rule out backported/identical source tables. It does block unqualified use of the 2024 publication as established **v2.3-specific downstream impact**. Neither a software metadata discrepancy nor lack of identified source input proves external scientific novelty or author error.

## 3. External source versus project-owned evidence

Public Badacz original source `NOTE_111 r2` on BlackHawk 2.3 vs 3.0 source archives, Git blob `39e691d2ce9bc0859cecce6b3ea747cc8a39b9db`:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/badacz/2026-11-22/IW_BADACZ_B1_DIR009_BLACKHAWK_V30_HERWIG_TABLES_NOTE_111_20261122.md

That separately reports official v2.3/v3.0 identical 11/11 HERWIG table files and unchanged pertinent manuals/code, as original **BADACZ**, not REC14, evidence. It says nothing directly about the 2.1 package Thoss reports using. REC14 did not rehash any official archive.

The source-specific Herwig BlackHawk index discrepancy, its affected software component, and its physical consequence require distinct causal links: `V21_SOURCE_BYTES → ACTUAL_AUTHOR_RUNTIME_CONFIG → USED_KERNEL → OBSERVABLE/BIN → REPORTED_BOUND`.

## 4. Cheapest reopen gate / owner interface

`REOPEN_IF`: an authentic Thoss 2024 producer config, original execution record, code archive, or manifest pins the runtime BlackHawk version, HERWIG table selection, and exact source catalog bytes. For a transfer from v2.3/v3.0 to declared v2.1, require a genuine v2.1 table member comparison or comparable source-native proof; no proxy assumption. Only then test actual spectral/constraint dependence in the owner’s original calculation and uncertainty convention. Source owners Badacz/EKS1/XH should resolve any owner-assigned research interface; REC14 does not create an automatic new run or correspondence obligation.

If no such source appears, `HOLD_SPECIFIC_DOWNSTREAM_USE` is the terminal bounded referee verdict, NOT `NO_HERWIG_USERS` and NOT `NO_SCIENTIFIC_VALUE`.

## 5. Reproduction, query and exposure statement

External search conducted 2026-11-22 through public web fast-index, with queries in this order:
1. `Thoss Burkert Kohri 2024 "hadronization_choice" Herwig BlackHawk source 2024`
2. `Breakdown of Hawking evaporation opens new mass window primordial black holes as dark matter HERWIG BlackHawk v2.1 data code`
3. `Thoss Burkert Kohri 2024 MNRAS 532 451 HERWIG gamma BlackHawk secondary spectrum choice`

Follow-up: opened original publisher HTML; searched within `HERWIG`, `BlackHawk`, `v2.1`, `hadronization`; checked §2.2 and `SOFTWARE`. The literal `v2.1` query does not match where the page spells `blackhawk 2.1`; therefore no-match is NOT a contrary source result.

Primary-source retrieval state: publisher text **read**, not paper PDF image or original production code; Zenodo archive **listed**, no new arrays downloaded by REC14; original historical v2.1 code **not obtained or rerun**. Search hit count not a novelty measure, and no systematic global prior-art/issue search is claimed. No external I3, no owner adoption, no BW write or receipt; this GitHub body is primary for this single PUBLIC referee return.

## 6. Summary

`REC14_ROT001_I1_NONBLIND_PUBLISHER_SOURCE_VERSION_CHECK_PASS / THOSS2024_HERWIG_USE_CONFIRMED / BLACKHAWK21_DECLARED / BLACKHAWK23_SPECIFIC_USE_UNPROVEN / CHOICE1_CONFIG_UNPROVEN / V21_KERNEL_BYTE_RELATION_UNKNOWN / PUBLISHED_PHYSICAL_IMPACT_HOLD / NO_EXTERNAL_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_PENDING`.
