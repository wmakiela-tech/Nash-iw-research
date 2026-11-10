# XH-S5 / EKS1 T1 — Schall Source Data ZIP fully inventoried: NO temporal series in supplied archive

Date: 2026-11-10
Cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
REQUEST_ID: EKS1-XH-S5-SCHALL-SOURCE-DATA-INVENTORY-T1-REMINDER-001_20261110
RETURN_ID: XH-S5-EKS1-T1-SCHALL-SOURCE-DATA-ZIP-INVENTORY-NO-TEMPORAL-SHEETS_001_20261110
GAP_ID: EKS1-GAP-001
Class: ORIGINAL_USER_SUPPLIED_PUBLISHED_SOURCE_DATA_ZIP_READ / COMPLETE_MEMBER_AND_AXES_INVENTORY / NEGATIVE_TEMPORAL_DATA_IN_THIS_ARCHIVE / NO_NEW_THEORY / NO_CANON / NO_EXEC_SIGN
prior_failures: Initial ACCESS_BLOCKED report and then publisher ARTICLE PDF receipt were NOT the Source Data; this third return supersedes binary-access limitation by direct reading actual supplied ZIP.

## Exact original source provenance and integrity
Article: Schall, Lindner, Rottstaedt et al., Laser-enhanced quantum sensing boosts sensitivity and dynamic range, Nature Communications 17:10825, 2026-10-22, https://doi.org/10.1038/s41467-026-78386-z . Article PDF p9 confirms experimental data and analytical solution in separate Source Data.
Source Data ZIP provided directly by Moderator, named 41467_2026_78386_MOESM2_ESM.zip
EXACT original bytes: 88710
SHA256: 6f6fdf9b68a4f74144ccd9269de75a299ceeb326013e96863498f96eb11fcf5e
ZIP CRC testzip PASS. 12 entries: Data/ folder plus 11 files.
Original filename and structure align with article's figures, but independent publisher-server binary hash NOT available; no falsely claimed network-origin readback. Original user ZIP preserved BYTE IDENTICAL in moderator-local evidence bundle. Seven CSV have 3283 numeric records, all consistent-width finite numeric entries. Author code was READ not executed.

## Exact source-native table inventory and Figure axes
Fig1c Data/Fig1c.csv: 200 rows, six columns, X = 3 separate MECSEL pump power (W) curves grey/green/blue; Y = corresponding Laser power (mW); pump-threshold curves.
Fig1d Data/Fig1d.csv: 200 rows, four columns, X = NV pump power green/blue (W); Y = laser power green/blue (mW).
Fig2a Data/Fig2a.csv: 600 rows, four columns, X = microwave frequency blue/red (GHz); Y = laser power blue/red (mW); ODMR frequency sweep.
Fig2b Data/Fig2b.csv: 441 rows, two columns, X = MW frequency (GHz), Y = laser power (mW); eight-resonance vector ODMR spectrum.
Fig3a Data/Fig3a.csv: 600 rows, four columns, ONE X = MW frequency (GHz); THREE Y columns = PSN sensitivity gradient fit, PSN sensitivity Eq.(1), PSN sensitivity Eq.(2) (all fT/rt(Hz)). These are inferred/derived shot-noise sensitivity LIMITS, NOT measured temporal noise PSD.
Fig3b Data/Fig3b.csv: 621 rows, two columns, X = MW frequency (GHz), Y = Laser power (mW); three-hyperfine-line source spectrum.
Fig3c Data/Fig3c.csv: 621 rows, two columns, X = MW frequency (GHz), Y = PSN sensitivity gradient fit (fT/rt(Hz)), calculated shot noise limit.
Data/Fig4.xlsx: exactly ONE sheet Tabelle1; range A1:E30; header [Reference,Source,PSN_sensitivity_limit,Dynamic_Range,Comment]; units row source literal [ft/sqrtHz,µT] (publisher physics uses fT/sqrtHz); 28 reference/device rows A3:E30. Graph axes X=PSN_sensitivity_limit, Y=Dynamic_Range µT; NOT a time series.
Data/example_script.py (2024 bytes): simple supplied Python plotting CSV/XLSX, not executed; data visualizations only on these pump/frequency/sensitivity axes.
Data/analytical_solution.txt (47101 bytes): algebraic analytic solution text, not timed observations.
Data/~$Fig4.xlsx (165 bytes): Microsoft Office lock file, no measurement-sheet content.

NO other data files/sheets or temporal axes in the supplied 11-file complete archive.

## SHA256 of ALL individual source files (no inferred paths)
Data/Fig1c.csv 730d8bc560bab1be116c74a4e72f1781de3b1d751640471c756f77e57e340f19
Data/Fig1d.csv a022c762601f39c7bdc4afe190c6354e5d2ee55a93da11e48815dcc01a79265c
Data/Fig2a.csv f6f0925fd68be13c2cd3325574886e0ed61773d1dcb6b3ed6ad49e1535e33be8
Data/Fig2b.csv 9294b9b8ed63b827883922af04a61ee26b2d32849c2fc6d52202ba771e8651f3
Data/Fig3a.csv 4fe37d27696ab39b20a348b411f92fda167df7ec8d0d4e91a6155194c8135d54
Data/Fig3b.csv 2dca0b220ce23ea7bfbae30cdc74121c2762a312e95b301b3954566083562127
Data/Fig3c.csv 542438d947ae8817b837258c1faa9a778163fdaf5c4b1145d8061dcfa94f0d47
Data/Fig4.xlsx 5dffab43170e3881118894fd34ac57617bf1f1d9e9d2f12c9e8d9d60675f6b97
Data/analytical_solution.txt 33cd77dc1165e79281fa0ac9c3f36ee35de0a8ae86603cdd1e9c5d2742092749
Data/example_script.py 4f1ea238911ed52254864b93a5d441b8462b30122bbb90015dd8deca5b25ef10
Data/~$Fig4.xlsx bea4924792fc3a4b01b7d1f45f5a6bd4aa0bbc82bc6bfa674f9ef7cdf1b5df8e

## EKS1 T1 single dispositive answer
Asked: Is there ANY Source Data worksheet/figure with time-axis, repeated timestamps, temporal trace, actual technical-noise PSD, Allan deviation or drift observations?
ANSWER: NO, within the FULLY READ supplied Source Data ZIP. Primary locators ALL 7 Data/Fig*.csv headers plus Data/Fig4.xlsx Tabelle1!A1:E30, Data/example_script.py plots; analytical_solution.txt analytic steady state. All independent variables are pump power, microwave frequency, or benchmark shot-noise limit; none time. CSV contains 3283 parameter-sweep rows, NOT time-indexed repeated measurements of fixed observable. No Allan variance or noise PSD. Source article also uses steady-state model; its dynamic master equations in article do NOT themselves constitute experimental time-series.

Strict negation scope: This is about the **supplied published Source Data ZIP**, NOT proof original authors never took time data, that other unpublished repositories have no temporal traces, or that M14 mathematical theory is false. No new experimental physics result.

EKS1's T1 acquisition+hash+figure inventory+YES/NO is now **COMPLETED**, replacing earlier ACCESS_BLOCKED status. EKS1 GAP-001 needs M14 scientific-owner disposition: M14 ROT034-035, INT9 ROT007 and KN13 ROT005 have **NO SOURCE-NATIVE EXPERIMENTAL TIME-SERIES TEST IN THIS SOURCE**; therefore physical attribution to THIS source requires explicit STOP or a different independently verified time-series source. Classical hypothetical temporal mathematics remains conditionally valid. M14 owns decision, not XH-S5. No task cascade.

## Local executable custody / replay
Moderator-local full 96617-byte evidence ZIP IW_XH_S5_EKS1_T1_SCHALL_SOURCE_DATA_EVIDENCE_REPRO_20261110.zip SHA256 81d2452c69997cba70567ed22ff17ce386989b170ddc655b5e2dff805f474c55.
Includes exact unchanged supplied original ZIP nested, 8921-byte complete Polish Markdown scientific inventory SHA256 ffe9e3a1f4b5cb5e15ef272a24a6c2992460565ac6fbf2a302572d59b7a3cc08, full JSON original-member hashes+axis/header/range detail, read-only inspect_t1_source.py using stdlib csv/zipfile and artifact_tool for XLSX, README, and SHA256 manifest. PACKAGE ZIP CRC PASS, all payload hashes PASS, fresh isolated extract + execute inspect script + compare inventory.json BYTE-IDENTICAL PASS. Original submitted source never modified.

This GitHub research report is NOT a GitHub upload of the original binary ZIP or evidence bundle; do not invent binary public GitHub custody. BW ingestion, owner M14 acknowledgement and independent publisher-server byte identity are NOT verified.

STATUS: T1_COMPLETED / ORIGINAL_SOURCE_ZIP_CRC_PASS / MEMBER_HASHED / SHEET_INVENTORY_PASS / TEMPORAL_SOURCE_DATA_NO / EKS1_GAP001_AWAIT_M14_OWNER_DISPOSITION / NO_CANON / NO_EXEC_SIGN / NO_BW_INGEST_ASSUMED.
