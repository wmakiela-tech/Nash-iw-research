---
artifact_id: IW_MECH_S8_ROT003_WUXU_PAPER_VS_MAIN_SCAN_SUBEDGE_SOURCE_LAW_DISCREPANCY_GATE_001_20261102
created_at: 2026-11-02
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_07 / Mech-S8
artifact_type: BOUNDED_SOURCE_NATIVE_FALSIFIER_RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: MAIN_SCAN_SOURCE_METHOD_DIFFERENCE_ONLY / NO_FIG5_PROVENANCE / NO_BBN / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
---

# Mech-S8 ROT003 — paper's subedge 1.3 law versus shipped main-scan log-linear extrapolation

**Result:** `SOURCE_METHOD_DIVERGENCE_CONFIRMED_FOR_PINNED_MAIN_SCAN / E4_HOLD / FIG5_SOURCE_LINEAGE_OPEN`.

## Pinning and scope

* Paper: Wu & Xu, *Primordial black holes evaporating before big bang nucleosynthesis*, JCAP 02 (2026) 063, DOI https://doi.org/10.1088/1475-7516/2026/02/063, §4.1, eq.(4.5) and paragraph after it. The authors **already explicitly know** BlackHawk's 100 TeV restriction and state that below `M=1e9g` they use an analytical `T_H^1.3` law, rescaled to the BlackHawk rate at `1e9g`, whereas above this floor they use BlackHawk. Do not misrepresent the energy cap as unnoticed by the authors.
* Original author repository `Fenyutanchan/Primordial-Black-Hole`, frozen commit `d395183674cace6c9906a8911bdeb7234ba4040d`.
* Original `arXiv-2509.05618/tool_script-hadrons_from_PBH.jl` Git blob `cc73432910f872d526113ce59b6204f38d0766a9`: five `LinearInterpolation(log.(rates), log.(masses); extrapolation=ExtrapolationType.Linear)` calls, without an `if m<1e9g` analytical branch. Under a standard linear extrapolation of log-log data, the first pair of source table rows determines the below-floor power.
* `arXiv-2509.05618/main-scan.jl` Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`: `@everywhere include("tool_script-hadrons_from_PBH.jl")` at line 37; calls `dN_over_dt_π/K/K⁰ᴸ/proton/neutron` at lines 103–107. No extra method selection at those call sites.
* Original table `arXiv-2509.05618/data/out/hadrons_from_PBH.dat` Git blob `06d0883a27b108692720422294ba2baacd381a64`. First two masses in table's GeV units: `5.609588603804452e32` (M~1e9g), `6.099798045788406e32`; first two values for five rates were directly read via GitHub connector and embedded in the reproducibility script.
* Author `arXiv-2509.05618/main.ipynb` Git blob `171c4a29e414860d724c817641896628f35982b0` was NOT read: its detailed contents, Fig.5 code lineage and published beta-bound lineage remain **OPEN**. The present result does not establish a paper error, nor that the public main-scan code generated any particular published figure.

## Executed source-derived calculation

Let `M0=1e9g`, `R_j(M0)` be the boundary rate and `M1` the next table mass. The **paper's stated calibrated analytic law** is `R_paper(M)=R(M0)*(M0/M)^1.3` for `M<M0`. The shipped `main-scan` path instead evaluates `R_scan(M)=R(M0)*(M0/M)^p_j`, with `p_j=-log(R(M1)/R(M0))/log(M1/M0)` from log-linear extrapolation.

| Integrated hadronic source (aggregate) | `p_j` from original table | scan/paper at `3e8g` | scan/paper at `1e8g` |
|---|---:|---:|---:|
| pi± | 1.200486 | 0.8871 | 0.7952 |
| K± | 1.196651 | 0.8830 | 0.7882 |
| K0L | 1.196805 | 0.8832 | 0.7885 |
| p+pbar | 1.204291 | 0.8912 | 0.8022 |
| n+nbar | 1.204763 | 0.8917 | 0.8031 |

Thus the public scan source is **~19.7–21.2% below** the boundary-normalized paper analytic function at `1e8g` for each instantaneous aggregate rate. The two functions also differ **~10.8–11.7%** at `3e8g`. This is a **source-algorithm identity check**, NOT a percentage change in PBH mass loss, physical hadron emission error, neutron fraction, Yp, D/H, or beta bound.

## Custody / actual owner gate

**Owner decision needed before claiming "Wu–Xu reproduced":** distinguish and explicitly label source functions `paper_eq4p5_calibrated`, `main_scan_loglinear_first_interval`, `source_native_generator_replayed`. Do not erase their provenance or promote one into the other. Next bounded falsifier: recover `main.ipynb` body and identify the *actual* Fig.5 generation pathway; then evaluate a source-correct native paired run if independently warranted, while preserving charge-state, primary energy support, greybody, numerical strict-error, and target validation gates.

**Status:** `MAIN_SCAN_METHOD_DIVERGENCE_PASS / FIG5_SOURCE_LINEAGE_OPEN / SOURCE_VALIDATION_OPEN / PBH_DE_DYNAMIC_ACCURACY_OPEN / PBH_Yp_DH_TARGET_VALIDATION_OPEN / HOLD/SOURCE_BLOCK / NO PBH BOUND / NO CANON / NO EXEC_SIGN`.

## Reproducer and local long form

Public runnable standard-library script: [mech_s8_rot003_public_compact_paper_code_subedge_gate.py](mech_s8_rot003_public_compact_paper_code_subedge_gate.py). Local extended artifact and independent JSON/manifest SHA-256 additionally produced in this conversation: `IW_MECH_S8_ROT003_WUXU_PAPER_VS_MAIN_SCAN_SUBEDGE_SOURCE_LAW_DISCREPANCY_GATE_001_20261102.md`, `mech_s8_rot003_paper_code_subedge_exponent_gate.py`, `mech_s8_rot003_paper_code_subedge_exponent_gate.json`, `IW_MECH_S8_ROT003_MANIFEST_20261102.json`. Public report is a concise custody edition, not byte-identical to the local longer report. The program uses **two pinned source table rows**; it does not re-execute Julia/PYTHIA/BlackHawk. `sync_state=GITHUB_PENDING_BW_INGEST`, not evidence of BW ingestion, REC/AUD peer audit, or LT adoption.
