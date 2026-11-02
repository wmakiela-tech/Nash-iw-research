# XH-S5 ROT020 — UTe2: actual original ultrasound c11 rows, pressure-specific Tc2star cooling-contrast control

artifact_id: IW_XH_S5_ROT020_UTE2_RAW_C11_TRANSITION_CONTRAST_20261103
return_id: XH-S5-ROT020-UTE2-ORIGINAL-RAW-C11-CONTRAST-001-20261103
cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
date: 2026-11-03
exposure: PUBLIC
claim_ceiling: ORIGINAL_AUTHOR_TRACE_READ_AND_GIT_BLOB_PROVENANCE / DERIVED_AGGREGATE_OFFLINE_REPLAY_ONLY / NO_RAW_OFFLINE_REPLAY / NO_INDEPENDENT_SECOND_ORDER_THERMODYNAMICS / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST

## Source author ownership and prior science
Sahas Kamat, Jared Dans, Shanta Saha, Artem D. Kokovin, Johnpierre Paglione, Jörg Schmalian and B. J. Ramshaw, "Thermodynamic demonstration of tetracriticality and multicomponent superconductivity in UTe2", Nature Physics, PUBLISHED 30 Oct 2026, DOI https://doi.org/10.1038/s41567-026-03504-z . Authors document original thermodynamic ultrasound evidence of pressure-dependent extra phase boundary Tc2star, upward change of velocity upon cooling and a tetracritical point. Do NOT ascribe the discovery to XH. Related independent Sept2026 high-field UTe2 PRL Vališka et al 137:126003 DOI 10.1103/1l46-jbm6 is distinct P/B/T geometry, not our data.

Original authors public source repo pinned COMMIT 908bb84e64c20411b14013c0bca43554731f7774:
https://github.com/CHiLL-Ramshaw/manuscripts-supporting_data/tree/908bb84e64c20411b14013c0bca43554731f7774/2026_UTe2_Tetracriticality .

## Verified full original traces actually read; source versus frozen derivatives
Through connected authenticated Github fetch_file the following FOUR COMPLETE, non-synthetic Fig2 c11 raw files were ACTUALLY READ and parsed, total 22,112 numerical rows, with Git source blob identity:
0.211 GPa: fig2_c11_0pt211GPa.csv, 5557 rows, blob 58bbfff19b680b94cbdda92c1145d31f16682ce4.
0.213 GPa: fig2_c11_0pt213GPa.csv, 5828 rows, blob eee5a437d22b92b703ebb1649e7676fb9b13c583.
0.218 GPa: fig2_c11_0pt218GPa.csv, 3676 rows, blob fb84dbda637e7335cf73b98276c4a80d27765045.
0.250 GPa: fig2_c11_0pt25GPa.csv, 7051 rows, blob 937baf6de41441dc1d9d934ea324658769576cc5.
Original header: T in K, dc/c in units of 1e-5. The independent original small source Fig2 Tc2star CSV (77 bytes, author Git blob ea1bd418fdb4e3bd90f8e07369a30b682d8b59bb) IS bundled in local ZIP unmodified.

IMPORTANT CUSTODY LIMIT: full 22,112 original raw rows were READ through Github connected tool, but were NOT copied into Moderator-local ZIP because container external DNS is disabled. Local ZIP includes exact pinned commit/source Git hashes, frozen SOURCE-DERIVED window statistics and one genuine small original CSV. Offline clean extracted replay checks derivations from frozen aggregates, NOT full original trace reprocessing. An independently executable OPTIONAL network raw-download-and-recompute script is supplied, verifies actual Git blob SHA and redoes all raw window contrasts if a network exists; it was not clean-executed in the isolated container. Do NOT assert raw offline replay PASS.

## Controlled descriptive primary-signal test
Predefined source transition reference: Tc2star(P=.211)=1.02K, Tc2star(.213)=.74K, Tc2star(.218)=.40K. Control .250 GPa has NO source annotated Tc2star; reference .74K is chosen only to compare a similar temperature background. For each source tstar, take window center tstar-h and tstar+h with +/- .01K T bandwidth, h in {.04,.05,.06,.07,.08}K. Contrast D=(mean lower-T c11 - mean higher-T c11), unit 1e-5. Positive D corresponds to sound-velocity rise on cooling. At h=.05:
P=.211: lower n40 mean -6.182168049592499, upper n42 mean -24.61735334287114, D=+18.4351852933;
P=.213: lower n41 mean -6.8905632310682075, upper n40 mean -24.955526223242664, D=+18.0649629922;
P=.218: lower n48 mean +12.258974931271176, upper n13 mean +3.339137258199571, D=+8.9198376731;
P=.250 CONTROL at T=.74: lower n64 mean -26.35329225879991, upper n63 mean -26.41329308045073, D=+.06000082165.

All five tested h contrasts positive for 3 annotated transition traces, actual ranges: .211 [15.9096546,23.8340054], .213 [15.3536008,23.5762407], .218 [7.3097547,13.0650034]. Control .250 only [.0224157,.0600008]. Per-control magnitude ratios at h=.05 ~307.249,301.079,148.662, descriptive only, not standardized effect sizes because different pressures/samples.

Robustness using raw rows directly at h=.05:
P=.211 difference of medians +18.530427985; 10pct trimmed +18.45536814;
P=.213 medians +18.091810400; trimmed +18.08803256;
P=.218 medians +8.965375189; trimmed +8.940260989;
P=.250 medians +.059556861; trimmed +.058878125.
Agreement supports sign stability, does NOT estimate independent physical uncertainty. Temperature-adjacent rows are correlated and under an unknown apparatus/pressure background; hence no p-values or unjustified CIs.

## Reproduction contract, immutable hashes
Complete local report 6825 bytes; offline pure-Python independent source-aggregate scripts rot020_summary_analysis.py, rot020_independent.py; original small source CSV; source_derived_windows.json; two frozen derived JSON; online raw download/check script rot020_source_fetch.py; README, independent replay verifier, SHA manifest.
Local complete Moderator ZIP IW_XH_S5_ROT020_UTE2_RAW_C11_SOURCE_CONTRAST_REPRO_20261103.zip
SHA256 1fc3bf3ddd101ad2749a5d50f8983b4098d36faec1e73f20e344f9f804ee5269.
Full report SHA256 0980a0841f98d6fba4d8833d19e768862553f3c0691d59fb0861db996f65ff70.
ZIP 11 members, CRC PASS, 10 content member SHA256 PASS, fresh clean extraction both OFFLINE aggregate scripts JSON BYTE IDENTICAL PASS. This remote report is NOT full ZIP. Do not confuse original source trace analysis executed through connector with fully locally re-executed source-trace extraction.

Scientific verdict: source's real ultrasonic data exhibit pressure-dependent strong positive cooling contrasts at author annotated Tc2star windows compared with a descriptive unmatched-pressure control. This is a primary-data sign check, NOT independent proof of a jump discontinuity, transition order, pressure calibration accuracy, raw phase classification or novel evidence. To prove physical order independently requires raw heating-cooling/calibration and error-aware ultrasound background fits. No author data licensed redistribution of whole raw files, no cross-cell tasks, no BW/REFEREE/OWNER/EXEC adoption.
NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_INGEST_UNVERIFIED.
