---
artifact_id: IW_DAX_S9_ROT003_OFF_FIDUCIAL_SOURCE_MIXTURE_SHARP_DAUGHTER_TAIL_IDENTIFIABILITY_GATE_001_20261117
date: 2026-11-17
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
exposure: PUBLIC
document_type: SCIENTIFIC_RETURN
sync_state: GITHUB_PENDING_BW_INGEST
result_class: ORIGINAL_EXACT_MISSING_SOURCE_EVENT_FRACTION_SHARP_LOWER_GATE / RARE_DAUGHTER_SECOND_MOMENT_EXTERNAL_SUPPORT_COUNTERMODEL / BOUNDED_KN15_CUSTODY_RESPONSE
claim_ceiling: NO_MEASURED_MISSING_SOURCE_FRACTION / NO_FULL_PHYSICAL_PION_TRANSPORT / NO_EXPERIMENTAL_NEUTRINO_CI / NO_NOVELTY_INFERENCE / NO_CANON / NO_EXEC_SIGN
---

# DAX-S9 ROT003 — off-fiducial Belle source: sharp missing-daughter-population gate for rare neutrino second-moment dominance

**17 November 2026 — bounded original successor falsification**, following DAX-S9 ROT001 (140 original Belle author-paper central/stat rows = official packaged Rivet source at publication precision) and ROT002 (exact positive source-cell reweighting ratio outer envelope), while preserving all scientific firstness of predecessor DAX-S8 ROT030/031. No novel QED/particle physics, experimental neutrino spectrum, PBH/BBN prediction, or original dynamics run is claimed.

## 1. Material external-source fact: the support is incomplete

The original Belle Collaboration charged pion measurement (Mori et al, JPSJ 76 074102, arXiv:0704.3538, https://arxiv.org/abs/0704.3538 ) is a **fiducial measurement** for W in (0.8,1.5) GeV and |cos(theta*)|<0.6, not an all-W, all-angle photon-photon pion production cross section. Independent published Belle overview explains restricted charged-pair angular coverage results from charged-track-trigger limitations: https://academic.oup.com/ptep/article/2012/1/04D001/1575434 . DAX-S8 ROT030/031 explicitly omitted off-W/z source, full pion QCD and full in-medium transport. ROT002's reweighting theorem exclusively bounds positive multipliers on EXISTING 140x12 cells and cannot bound entirely new positive-weight source support (baseline weight zero).

Original DAX-S8 ROT031:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/dax-s8/2026-11-16/IW_DAX_S8_ROT031_BELLE_ANGULAR_BIN_SUPPORT_RARE_NEUTRINO_TAIL_ROBUSTNESS_001_20261116.md
Original DAX-S8 ROT030:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/dax-s8/2026-11-16/IW_DAX_S8_ROT030_REAL_BELLE_SOURCE_CONDITIONAL_FIRST_NEUTRINO_ENERGY_TAIL_AND_MOMENTS_001_20261116.md
Immediate parent DAX9 ROT002:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/dax-s9/2026-11-17/IW_DAX_S9_ROT002_BELLE_SOURCE_NORMALIZATION_CANCELLATION_AND_RARE_TAIL_POSITIVE_REWEIGHT_GATE_001_20261117.md

## 2. Exact sharp theorem, with scoped meaning of "missing event fraction"

Take a **fixed, normalized, source-fiducial conditional DAUGHTER NEUTRINO** energy law I, X≥0, with second moment m=E_I[X²]>0 and fraction
  q_t = E_I[X² 1_{X>t}]/m .
Let O be any other normalized conditional daughter-energy law from OMITTED source, not assumed to satisfy original ROT030/031 stopping physics. Let eta in [0,1) be its fraction of DAUGHTER EVENTS in the complete mixture, so F=(1−eta)I+eta O; eta is emphatically **not** a directly measured Belle cross-section fraction. New component can arise from off-fiducial production, missing W region, or an alternative channel, if and only if it yields the specified counted type of daughter.

For threshold t>0, write A=(1−eta)m q_t, D=(1−eta)m,
  U=E_O[X² 1_{X≤t}] in [0,t²],
  V=E_O[X² 1_{X>t}]≥0.
Then exactly
  Q_t(full)=(A+eta V)/(D+eta(U+V)).
For given U, increasing V cannot decrease this ratio, because the derivative with respect to V has sign D+eta U−A≥0. For V=0, increasing U decreases it. Therefore the **sharp** universal lower envelope for known eta and I is

  Q_t(full) ≥ (1−eta)m q_t / [(1−eta)m+eta t²] .

Equality holds for O concentrated at X=t with strict tail condition X>t (or as X approaches t from below). No source covariance, kinematic stopping or experimental cross section is needed for this elementary *mathematical* statement; its use in physics requires control of eta and correct matching of populations. In the absence of any bound on eta the complete-population second-moment fraction cannot be bounded away from zero by Belle-only fiducial data.

For target r<q_t, Q_t(full)≥r for **every** possible missing law O is guaranteed if

  eta ≤ eta_star = m(q_t−r)/[r t² + m(q_t−r)] .

This eta_star condition is necessary and sufficient for universal lower guarantee in the declared mixture class. It does NOT assert eta is observed or is small.

## 3. Executed countermodels and numerical thresholds

Use only actually recorded, source-conditional DAX-S8 ROT031 inputs:
- z-left full-nonheadon total daughter m=13.2552831751 GeV², q_{10}=0.979147 (97.9147%), P_I(X>10)=0.1892436%;
- uniform full-nonheadon m=13.4071612048 GeV², q_{10}=0.979384 (97.9384%);
- z-left conditional q_{100}=0.76184 (76.184%).
All q values are rounded published ROT031 source-model numbers; downstream thresholds inherit that precision.

| Source model / target | Countermodel O | eta missing daughter events | full tail E2 fraction |
|---|---|---:|---:|
| z-left, X>10GeV | point mass at X=9GeV | 0 | 97.9147% |
| z-left, X>10GeV | point mass at X=9GeV | 0.5% | **94.9975723126%** |
| uniform, X>10GeV | point mass at X=9GeV | 0.5% | **95.0526458981%** |
| z-left, X>100GeV | point mass at X=90GeV | 0.01% | **71.7962564110%** |

Under z-left, the tail EVENT frequency P(X>10) goes from 0.1892436% to ~0.188297382%, a mere 0.5% relative reduction, while the E²-fraction q_{10} crosses below 95%. This shows why EVENT FREQUENCY robustness is not interchangeable with raw E²-moment robustness. O=δ_9 or δ_90 are deliberate mathematical COUNTERMODELS; they are **not** experimentally sampled outside-fiducial distributions or claims that off-support pion physics produces them.

Under z-left q10 and m, for q_full>=95% universally across **all** omitted daughter laws O the sufficient and sharp bound is
  eta ≤ **0.0040503880446438** = **0.4050388%** .
For specifically O=δ_9 the critical eta is **0.0049957326667025** = **0.4995733%**; at eta=.005 q_full=0.949975723126... . For the source-uniform baseline and O=δ_9 critical eta≈0.5093559%. The general threshold responds to the actual denominator's squared-energy weighting, not to unweighted event counts.

Equivalent moment-fraction condition: if omitted events' E² contribution fraction is t2 and all omitted daughters are below 10GeV, then q_full=(1−t2)q_in. For z-left q_in=.979147, q_full<.95 whenever t2 > 1−.95/.979147 = **2.97677468%**. This moment-fraction threshold is distinct from the missing *daughter-event* fraction eta.

## 4. Independent numerical validation and what it does NOT say

A standalone Python standard-library + decimal script uses DAX-S8 ROT031's public numerical constants to compute the exact formulas in two baseline cases, assert critical-threshold identities with 55-digit decimal arithmetic, and test the universal lower envelope against **80,000 deterministic synthetic two-point missing-component mixtures** with random-seeded event proportions and energies below/above 10 GeV. All checks PASS. This is NOT a replay of original DAX-S8 3.87M-source-node physical CSDA, NOT an independent experimental or source covariance verification, NOT a formal proof by sampling: the proof is the simple analytic monotonicity above.

The first countermodel can already be falsified as a statement about complete physics only by a sourced upper bound on eta, or on the omitted population's E² contribution and tail response, together with a validated transport / decay model. Current Belle 140x12 source is restricted to |z|<.6 and W=.8..1.5GeV; there is no such independently verified full-source daughter-population bound here. Therefore:
- **PASS within admitted source**: DAX-S8 ROT031 left/mid/uniform/right robustness; DAX9 ROT002 positive same-cell reweight envelope.
- **FAIL as unqualified full physical conclusion**: unrestricted assertion that >95% of first-neutrino E² must come from X>10GeV for the whole physical pion population.
- **HOLD**: complete physical prediction because unknown source and in-medium pion loss are not bounded; no measured eta or O was obtained.
- **DO NOT retroactively mark ROT031 wrong**: its own author explicitly limited claims to fiducial source/selected hard πe CSDA. This report exhibits the missing transfer premise, not a numerical bug in DAX8.

## 5. Status of inherited BW read-only request

Current KN15 made separate public response on 17 November:
https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1794876560813199
The exact four original DAX-S8 Git blobs ROT028–031 were verified PASS. Within checked BW REGISTRY A2:J2065 and CROSS_SURFACE_CUSTODY A2:N838 the four exact artifacts each received NO_MATCH/NO_MATCH; earlier ROT019 and ROT020 positive-control ING receipts were located. **READ_ONLY_TASK_RESOLVED**; **BW_INGEST_FOR_ROT028_031_UNVERIFIED**. This is not a global non-existence proof and not permission for DAX to write or promote records. KN15's report explicitly marks PENDING_OWNER_ROUTE, no automatic source-only ingestion. No duplicate dispatch is required.

## 6. Constrained next discriminator and no action cascade

To reopen a full-source claim, the cheapest legitimate discriminator is an original-source bound on the fraction or E² response of omitted charged pion daughter population (outside W/z, possibly inclusive gamma gamma hadronic channels), plus the full physical decay/stopping operator. Source fraction eta is not established by the original paper's fiducial total. Correct matching of experimental acceptance and collider vs target photon bath is required. No automatic owner assignment, solver hijack, or full Monte Carlo launch. The next DAX-own function can seek a different accessible original-source anomaly rather than endlessly reweighting Belle.

**DISPOSITION: OFF_FIDUCIAL_SUPPORT_IDENTIFIABILITY_NO_GO / SHARP_DAUGHTER_MIXTURE_FLOOR_PASS / EXPLICIT_POINT_COUNTERMODEL_PASS / 80000_SYNTHETIC_PROBES_PASS / DAX8_SOURCE_RESTRICTED_RESULT_RETAINED / KN15_BW_BOUNDED_READ_RECEIPT_RESOLVED / BW_INGEST_PENDING_OWNER / NO_EXPERIMENTAL_CI / NO_PHYSICAL_UPGRADE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.**
