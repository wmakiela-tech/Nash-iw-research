---
artifact_id: IW_MECH_S9_ROT017_WUXU_PUBLISHED_M13_VS_ORIGINAL_JULIA_LOGLOG_NATIVE_CLOCK_RATE_CONTRAST_SOURCE_HISTORY_001_20261113
created_at: 2026-11-13
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
document_type: SOURCE_ORIGINAL_AUTHOR_CODE_V1_V2_PAPER_EXTRAPOLATION_AND_EXISTING_NATIVE_MASS_CLOCK_AUDIT
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
scientific_status: ORIGINAL_V1_V2_SOURCE_HISTORY_100_OF_100_4COL_PASS / PUBLISHED_RATE_FORMULA_AND_CODE_DIFFERENT / NATIVE_CLOCK_5CHANNEL_REPRO_PASS / NO_NEW_JULIA / B1_NATIVE_X_HOLD_AUTH
claim_ceiling: PAPER_VS_CODE_EMISSION_RATES_FROZEN_NATIVE_CLOCK_ONLY / NOT_COUPLED_XN_YCODE / NOT_PBH_BBN_BOUND / NOT_INDEPENDENT_PYTHIA_GENERATOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# ROT017 — author paper versus author Julia 10D input: native-clock constrained hadron emission contrast

## 0. Original author firstness, prior research and paper verification

**Original scientific firstness** belongs to Quan-feng Wu and Xun-Jie Xu, *Primordial black holes evaporating before Big Bang nucleosynthesis*, JCAP 02 (2026) 063, DOI `10.1088/1475-7516/2026/02/063`. Its Section 4.1 equation (4.4) specifies secondary multiplicity `N(E) ∝ E^0.3`; equation (4.5) specifies high-energy analytical hadron emission `R_h ∝ T_BH^1.3 ∝ M^-1.3`, matched by rescaling to the BlackHawk table at `M=1e9 g` and used below that edge. The paper EXPLICITLY recognizes the BlackHawk v2.3/PYTHIA `Emax_init=100000 GeV` limitation, and this is the authors' own prescription. It would be a FALSE novelty/criticism to state no below-edge source prescription exists.

Source copy available in publisher https://doi.org/10.1088/1475-7516/2026/02/063 and public arXiv https://arxiv.org/pdf/2509.05618, original formula (4.5) directly rechecked in text. This does not authenticate which Julia snapshot actually produced the journal's Fig.5.

Research FIRSTNESS: LT8 ROT018 FIRST identified the PAPER M^-1.3 versus public code first-two-table loglog M^-1.2 discrepancy and completed 85-digit/SciPy analytic mass-integrated emitted-count comparison; LT8 ROT019 FIRST corrected the historical-v1 claim. PRF13 ROT017 FIRST established sub-table mass emission count dominance. Mech-S9 ROT012/013 FIRST executed one original author 10D Julia 10000-sample j22 RAW hadron six-species history and ROT015 first mapped the 1e9 g crossing into native time. **This ROT017 adds a separate finite native mass-time-axis emission-rate comparison** anchored at the first table node, not an original discovery of the two prescriptions or an ODE solution after changing one.

## 1. Exact original v1/v2 file history — verified original code, not inference

Frozen author repository `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`:
- archived v1 `arXiv-2509.05618/arXiv-2509.05618v1/data/out/mesons_from_PBH.dat` Git blob `1cfc5eac427bd71aa984e630ac939188848b3952`; v1 meson driver `tool_script-mesons_from_PBH.jl` blob `d9b9b15adaf8e500c67f1d1f1f531ccf26002b35`.
- newer public v2 `arXiv-2509.05618/data/out/hadrons_from_PBH.dat` blob `06d0883a27b108692720422294ba2baacd381a64`; original v2 code `tool_script-hadrons_from_PBH.jl` blob `cc73432910f872d526113ce59b6204f38d0766a9`.
- Both 100-row original files were fetched DIRECTLY, and the first FOUR numeric tokens of EVERY row (mass, π, K, K0L) were compared as strings: **0 mismatches among 400 token pairs**. v2 adds proton and neutron tables. Both source drivers explicitly use `LinearInterpolation(log.(rate),log.(mass);extrapolation=ExtrapolationType.Linear)`. Below the first node 1e9 g, **the same first-two-node secant extrapolation was already present in archived v1**, not a v2-only change. The approximation printed in the journal and the extrapolation in this public source remain different; unknown if intentional in final producing build.

Original first two v2 source data rows, preserved inside the executable:
```
M[GeV]                   pi±              K±             K0L             proton        neutron
5.609588603804452e32     489105.5126008581  59105.93631247951 29086.774913348447 34849.08026691193 34656.17773724596
6.099798045788406e32     442306.73787501804 53467.712852971126 26311.795859614824 31504.591028094237 31328.963561830213
```

Code slopes `p_i = log(R2_i/R1_i) / log(M2/M1)`, and paper `p_paper=-1.3`. Both use exactly SAME R1 value at original first table node. Hence the native-clock **instantaneous source rate** ratio below first node is `Rpaper/Rcode=(M/M0)^(-1.3-p_i)`, independent of unknown absolute unit conversion.

## 2. Distinct actually executed native-clock result, NO new Julia

Real Mech-S9 original Julia 10D author `magic()` source run `43436800793`, artifact `14045176436`, immutable ZIP SHA256 `71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486`, 10000-row native output `author_native_raw_hadron_history_10000.csv` SHA256 `45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1`. Native j22, `beta=10^-16.9974609375≈1.005863531e-17`, **+0.586% OUTSIDE original source beta scan top 1e-17**, but valid original `magic()` function input (Mech-S9 ROT014 first domain diagnostic).

We read original native source mass/time series, 10000 ordered snapshots; original first node `M0=1e9 g` between original saved samples 8383/8384; linear sampled crossing estimate `t_node≈0.09731184823146294s`; last live PBH sample8544 `t≈0.334927351810113s, M≈1.44891220526512e8 g`. First zero PBH row8545 is a **phase cutoff** and excluded. The finite source area under each of five original *per-PBH hadron production rates* is calculated only along this frozen original `M(t)` from first table-node crossing to last live PBH, no full 10D alternate solve. That time/mass trajectory is held identical under both alternate formula evaluations, so this is a source-condition **rate-exposure counterfactual**, not a self-consistent modified output nor physical uncertainty.

| Five author rate channels | p_code (v1/v2 native) | Paper/code rate ratio at last live M | Increase in ∫R_h(Mnative(t))dt vs code, TRAPEZOID | Same PCHIP |
|---|---:|---:|---:|---:|
| Charged pions | −1.2004856256 | 1.211960 | +5.319587% | +5.239828% |
| Charged kaons | −1.1966513505 | 1.220970 | +5.525618% | +5.442877% |
| Long neutral kaons | −1.1968048413 | 1.220609 | +5.517369% | +5.434747% |
| Protons | −1.2042914285 | 1.203083 | +5.115161% | +5.038369% |
| Neutrons | −1.2047630640 | 1.201987 | +5.089833% | +5.013409% |

These finite saved-clock integrations give **PCHIP +5.0134…+5.4429%**, trapezoid **+5.0898…+5.5256%**; all ratios positive. The larger spread of left/right rectangular quadratures (for pion +4.7636…+5.8443%; Kcharged +4.9486…+6.0705%) exposes source sampling/integration sensitivity; *neither methods nor spread certify actual Julia ODE errors*. Source paper versus code instantaneous rates near the last sampled PBH-active mass differ by approx +20.2…+22.1%, larger than their native finite time-integrated partial production difference. This is NOT a claim about final whole-history emitted counts to zero mass: LT8 ROT018 first completed a separate mass-integral calculation to author stop cutoff; our source clock terminates at last live sample and is therefore a different endpoint and mathematical object.

## 3. Exact reproducibility and negative knowledge

New actually executed Python3 **stdlib-only** program:
`research/mech-s9/2026-11-13/code/mech_s9_rot017_paper_vs_code_native_clock.py`, original local exact SHA256 `e670f3db1005b2ab33eca6f1b21d1fea975bf7a4ae7ec11919fcf4ae6c2a02e9`, Git blob **`95ec201562ad66d7516395a3761080b02c217342`**, public source create commit `15581af7e80a9a12d1dd95c0211244f3a2405e1c`. This Git source blob was fetched via connector and independently checked **BYTE-IDENTICAL** with `git hash-object` of the ACTUALLY executed local program, 5895 bytes. No code implementation difference between model and published reproducer.

Actual original data ZIP is **included UNMODIFIED** in user conversation local self-contained package (its original GitHub Actions artifact stays immutable). Full produced JSON `mech_s9_rot017_paper_vs_code_native_clock.json` SHA256 `323e09e522882252823e0d428a398e88649c317e1341f06b2b3f0a051d5ed2d1`. User-local full reproduction package ZIP SHA256 `fbeb67606171992ac907058aa8c18fd977daff4e43f04cdc1502fb5ce0bc2d5d`, includes original author native ZIP, new executed source, exact JSON, README and 4 payload SHA256 manifest. Package ZIP CRC PASS, 4/4 manifest SHA checks PASS; clean isolated standard-library script execution reproduced JSON **BYTE-IDENTICALLY PASS**. Mutation of even one original source ZIP byte caused pinned SHA gate REJECTION before output, PASS negative test. The whole ZIP is conversation-local only, NOT claimed GitHub or BW archived.

## 4. 30-day B1 decision and limitations

Moderator-approved 2026-11-13..12-13 30-day research mandate has an original-science question and explicit `§E` per-*new-Julia-run* authorization. Badacz and Mech-S9 original native B1 coowners ACKED. INT9 ROT026 first integrated current source-domain, original `q=Q/T` typed output and B1 target freeze blocker. LT8 ROT018/019 first recommended one finite B1 test of original CODE low-mass extrapolation versus AUTHOR PAPER M^-1.3 at same first node, with **primary original X_n(T0)** using original LINEAR Q/T operator; secondary `Y_code=2X/(1-X)` not physical helium. Their recommendation was four fresh native calls (two source prescriptions × default and tightened ODE tolerance) only **after** precise Moderator authorization and preregistration; **no authorization receipt was found and no Julia run in this ROT017 was conducted**. The native-rate test here is NOT a substitute for those source-legal target and covariance/uncertainty comparisons.

Critically, published author analytical rate exponent is NOT a physically independent alternative generator, so two-author-prescriptions B1 would test **source prescription implementation sensitivity**, not necessarily physical hadronization uncertainty. Need original independent E4 BlackHawk/PYTHIA/HERWIG source generator data to infer physical robust helium or PBH constraint. The historical published Fig5 producing code/Manifest unknown; science novelty beyond authors and mature ODE / kinetics NOT demonstrated. A small source-rate model change cannot be promoted to `B1-ORIGINAL-SCIENCE-PASS` solely because numerically nonzero.

**DISPOSITION**: `ROT017_AUTHOR_PAPER_VS_CODE_SOURCE_RATE_DIFFERENCE_PASS / NATIVE_CLOCK_FIVE_CHANNEL_PARTIAL_INJECTION_CONTRAST_PASS / NO_NEW_JULIA / B1_TEST_FROZEN_NOT_YET / MODERATOR_PER_RUN_AUTH_PENDING / B1_SOURCE_PHYSICAL_UNCERTAINTY_HOLD / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE`. GitHub content readback pending separate check; GitHub source/report are not BW ingestion.
