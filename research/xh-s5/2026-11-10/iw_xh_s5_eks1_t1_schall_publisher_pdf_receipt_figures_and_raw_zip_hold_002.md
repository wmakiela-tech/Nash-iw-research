# XH-S5 — Schall Source Data T1, receipt of published PDF, ZIP still missing
Date: 2026-11-10
Cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
RESPONDS_TO: EKS1-XH-S5-SCHALL-SOURCE-DATA-INVENTORY-T1-REMINDER-001_20261110
REPLACES_NO_PRIOR_RECORD: This is an ADDENDUM to previous ACCESS_BLOCKED report, not T1 closure.
CLAIM_CEILING: DIRECT_USER_PDF_READ / ARTICLE_FIGURE_AXIS_INVENTORY_ONLY / NO_ORIGINAL_SOURCE_DATA_ZIP / NO_TIMESERIES_NEGATION / NO_CANON / NO_EXEC_SIGN

## Source receipt
Full 12-page user-supplied **published ARTICLE** Schall et al., *Laser-enhanced quantum sensing boosts sensitivity and dynamic range*, Nature Communications 17:10825 (22 Oct 2026), DOI https://doi.org/10.1038/s41467-026-78386-z; filename s41467-026-78386-z.pdf; byte size **1,181,170**, SHA256 **a4244e1243b2b337c3ad703172aed1b2b3527d3bea5dda1e9dc70f0c5d29f072**. PyMuPDF scanned attachment count: **zero**. PDF provides DOI and bibliography URLs but **no binary Source Data and no direct exact Source Data ZIP href**. PDF hash is not original Source Data hash.

## Figures — published PDF only, NOT ZIP members
- p.2 Fig1c: x MECSEL pump power W, y laser output power mW; theory and microwave resonance condition. Fig1d: x NV pump power W, y laser output power mW.
- p.3 Fig2a: x microwave frequency GHz, y laser power mW for 2 pump settings; Fig2b x microwave frequency GHz, y laser power mW for 8 ODMR resonances (4 NV orientation families).
- p.4 Fig3a: x microwave frequency GHz, y calculated PSN sensitivity LIMIT fT/sqrtHz; Fig3b x microwave frequency GHz, y laser power mW, triple hyperfine fitting; Fig3c x microwave frequency GHz, y calculated PSN sensitivity LIMIT fT/sqrtHz.
- p.5 Fig4: x sensitivity limit fT/sqrtHz; y intrinsic dynamic range microT; device benchmark.
- p.7 Fig5: state-transition diagram, NO plotted time axis. p.8 Tables1/2: model rates and fit parameters; NO time-series axes.

PDF pp.3,7–8: experimental cw-ODMR frequency scans at fixed continuously pumped setup. Although rate EOMs have derivatives, authors **solve only the steady-state d/dt=0** (p.8). A Ramsey sequence is mentioned to measure T2* ~200 ns (p.6); no raw Ramsey time series is presented in paper figures. Thus **NO PAPER-FIGURE TIME-AXIS** from displayed figures. Does NOT establish absence of time-varying raw data in the UNOPENED ZIP.

PDF p.9 'Data availability' affirmatively identifies SEPARATE Source Data with experimental data AND analytical solution. The Nature web version identifies **Source Data (download ZIP)**. PDF main text explicitly says real measured technical noise is much worse than calculated PSN limits (pp.4,6); 1160 fT/sqrtHz at ±280 microT and 127/<400 fT/sqrtHz at ±40 microT are different setups (pp.4,5), not achieved real sensitivities.

## EKS1 T1 strict fields
Original ZIP exact filename UNKNOWN; original bytes UNKNOWN; original SHA256 UNKNOWN; actual entries/sheets/column axes UNKNOWN; any time series / PSD / Allan deviation / drift in actual original ZIP **UNKNOWN (NEITHER YES NOR NO)**. Container outbound DNS to Nature/PMC/EuropePMC unavailable. Publisher archive URL not determined from embedded PDF links. User uploaded ARTICLE, not data archive.

STATUS: EKS1_T1_PARTIAL_ARTICLE_SOURCE_RECEIPT / ORIGINAL_SOURCE_DATA_ARCHIVE_ACCESS_BLOCKED / NO_RAW_ZIP_YES_NO_VERDICT / M14_TEMPORAL_BRANCH_OWNER_DECISION_PENDING / BW_INGEST_UNVERIFIED / NO_CANON / NO_EXEC_SIGN.

Full local 4998-byte manuscript report: IW_XH_S5_EKS1_T1_SCHALL_PDF_RECEIPT_AND_FIGURE_AXIS_INVENTORY_20261110.md, SHA256 8d65c825054567432639af98a5cb099e35ab90dbc711062242b3044639d452ef (REPORT hash, not published source archive).
