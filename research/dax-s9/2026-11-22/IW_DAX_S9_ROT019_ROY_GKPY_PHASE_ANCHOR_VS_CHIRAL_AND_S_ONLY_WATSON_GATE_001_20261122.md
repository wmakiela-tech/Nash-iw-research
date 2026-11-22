---
artifact_id: IW_DAX_S9_ROT019_ROY_GKPY_PHASE_ANCHOR_VS_CHIRAL_AND_S_ONLY_WATSON_GATE_001_20261122
date: 2026-11-22
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NEW_PHYSICS / NO_EXPERIMENTAL_CI / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX9 ROT019 — independent Roy/GKPY elastic phase anchor versus chiral 2025 and pure-S Watson

Original-source original-mathematics audit, 22 Nov 2026. NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.

**Primary published references actually inspected:** García-Martín et al., PRD83 (2011) 074004, arXiv:1102.2183v2 original PDF **Table XII page 34 visually verified**; source rows W (850,880,910,940) MeV: δ^0_0 = (93.5±1.8,99.7±2.2,108.8±3.4,122.7±7.0) degrees; δ^2_0=(-20.2±1.2,-21.2±1.3,-22.1±1.4,-22.9±1.5). Comparison original equations Klevansky/Lemmer/Beygi EPJA61 49 (2025), DOI10.1140/epja/s10050-025-01524-6, on-shell 2-channel hadron T model from DAX9 ROT010 (not the 2011 paper's fitted T).

**Independently executed** NumPy vs mpmath70 phase checks, two-source SHA, original true source input reexecution PASS: 2025 model δ^0_0 at 850,880,910,940 MeV =112.76214,117.80101,126.02964,143.49006 degrees, systematically +19.262,+18.101,+17.230,+20.790 degrees above Roy/GKPY central values. Model I2 phases -25.566,-27.040,-28.513,-29.981 degrees versus Roy/GKPY -20.2,-21.2,-22.1,-22.9 degrees. Exact unitary S matrix is thus not empirical phase-fit validation. No profile over model parameter or correlated source phase uncertainties; no formal model rejection CI.

**Hypothetical single-S Watson necessary ratio test:** from normalized charge/isospin rotation AC=√(2/3)A0+√(1/3)A2, AN=√(1/3)A0−√(2/3)A2, real freely signed production coefficient aI and phase δI from original Roy/GKPY, minimum neutral/charged ratio is rmin=(1−√(1+8cos²Δ)/3)/(1+√(1+8cos²Δ)/3), Δ=δ00−δ02. Across common original Belle charged/neutral source W centers .85,.87,.89,.91,.93GeV: measured source central N/C=.0678454,.0819748,.0971096,.1042412,.1255664; Roy-centre S-only rmin=.329169,.282129,.229680,.175403,.109801. Therefore 4/5 central values violate the SOURCE-CONDITIONAL pure-S necessary condition; 3/5 still do under an artificially permissive phase envelope using paper-printed phase margins and 20MeV W bin. **THE OBSERVED ORIGINAL BELLE CROSS-SECTIONS ARE FULL S+D0+D2+, NOT ISOLATED S WAVE; these tests DO NOT reject Watson or full photoproduction or Belle measurements.** This is a bounded hypothesis veto only.

Genuine original openSUSE packaged **SECONDARY** Rivet Belle charged source SHA256 28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403 and neutral source SHA256 65ed96b71a3e03e5528c406c336aa07277bff3fd9cf1c6b9596a708f14c573dd, original primary HEPData exports HTTP403 NOT HELD. Same corrected/positive source weighting as ROT018 (W .84–.94 GeV, 12 angular bins z0..0.6); no experimental covariance.

Original **local full report** and Python replayer with actual source bytes, source rows, JSON, two CSV, manifest in originating DAX9 chat archive DAX9_ROT019_Roy_GKPY_Phases_Chiral_Watson_Pure_S_Gate_Repro.zip SHA256 **fc67b5ba4761ba7eda43ee7a28af4877b4ebb192d55f799abf916086fa3e83b7**. ZIP CRC PASS, 13/13 member SHA PASS, two isolated clean-directory execution replays 2×3/3 outputs byte-identical PASS. GitHub report is text only, no executable stored in repo. Next analytical extension ROT020 explicitly adds arbitrary residual amplitude rather than pretending total source is pure S. NO_BW_WRITE / NO_I3 / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.