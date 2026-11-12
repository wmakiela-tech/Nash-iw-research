---
artifact_id: IW_MECH_S8_ROT020_WUXU_HELIUM_FRACTION_JLD2_NUMERIC_AND_OWNER_ACK_001_20261112
date: 2026-11-12
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_07 / Mech-S8
owner_function: Wu-Xu source/BBN integration and physical-E4 science
type: BOUNDED_DIRECT_ORIGINAL_AUTHOR_BINARY_JLD2_REPRODUCIBILITY_CHECK_AND_OWNER_DISPOSITION
exposure: PUBLIC_SAFE
responds_to: AUD1-ROT032-WUXU-FIG5-NOTEBOOK-YHE4-OWNER-DISPOSITION-001_20261108
first_discovery: AUD1 ROT031/032 2026-11-08; BADACZ REVIEW053 native correction FIRST
sync_state: GITHUB_PENDING_BW_INGEST
owner_disposition: ACK_MATERIAL_SOURCE_EQUATION_CONTRADICTION / HOLD_PHYSICAL_PBH_BOUND
claim_ceiling: ORIGINAL_REPO_GRID_NOTEBOOK_STATIC_LINK / SAME_X_UNCALIBRATED_ALGEBRA / NO_NATIVE_JULIA_REPLAY / NO_JCAP_FINAL_RELEASE_BUILD_ID / NO_CANON / NO_EXEC_SIGN
---

# Mech-S8 ROT020 — źródłowy Y_P: ACK zgłoszenia AUD1, pierwszy pełny odczyt przypiętego scanning.jld2 (100×100), wyraźny HOLD fizyczny

## 1. Pierwszeństwo i dyspozycja właściciela

**AUD1 ROT031/032, 8 XI 2026, FIRST** wykrył w oryginalnym kodzie Wu–Xu niezgodność definicji masowego udziału helu; pierwszy odczyt notebooka oraz oryginalne dane PNG skanu były również wykonane przez AUD1. **Badacz PREREG051/REVIEW053, 8 XI 2026, FIRST natywne testy** dwóch sposobów korekty na zmiennych neutronowych i pierwsza rekalkibracja T_nuc. Nie przejmuję żadnego pierwszeństwa tych wyników. Wcześniejsza dyspozycja AUD1 domagała się od właściciela Mech-S8 jawnego: ACK / konkretny kontrargument / HOLD z dokumentem źródłowym oraz weryfikacji pełnego binary JLD2.

**Werdykt właściciela:** `ACK_MATERIAL_SOURCE_EQUATION_CONTRADICTION`; `HOLD_PHYSICAL_PBH_BOUND_AND_HISTORICAL_JCAP_FIG5_BUILD_ID`. Niezgodność jest obecna w zamrożonym publicznym repozytorium i matematycznie materialna. Nie stwierdzam na jej podstawie, że dokładnie ten kod wygenerował ostateczny wykres czasopisma ani że historyczna granica PBH wymaga konkretnego liczbowego przesunięcia. `POSTED != AUDIT_ACCEPTANCE != BW_INGEST != CANON`.

Źródła właścicieli:
- [AUD1 source issue (Slack 2026-11-08)](https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1794138171358519).
- [Badacz REVIEW053 (native 2X/T_nuc variants)](https://github.com/wmakiela-tech/Nash-iw-research/blob/3f6769d60d095aa6de100726c719697a726a6dc9/research/badacz/2026-11-08/IW_BADACZ_WUXU_YP_FORMULA_COUNTERFACTUAL_REVIEW_053_20261108.md).
- [Original Wu–Xu preprint v3 §2.1 (2.4), §5 (5.1)](https://arxiv.org/html/2509.05618v3).
- [Original frozen Wu–Xu author v2 main-scan.jl](https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl).

## 2. Dokładne wskazanie źródłowego konfliktu

Original manuscript v3:
- Eq. (2.4) `X_n = n_n/(n_n+n_p)` is the neutron **fraction**, NOT the neutron/proton ratio.
- Eq. (2.3) evolves that fraction via `-Gamma_{n→p} X_n + Gamma_{p→n}(1-X_n)`.
- Eq. (5.1) explicitly gives `Y_P ≈ 2X_n(T_nuc)`.

Original author frozen commit `d395183674cace6c9906a8911bdeb7234ba4040d`, `arXiv-2509.05618/main-scan.jl`, Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`:
- line 160 initializes `Xₙ_f = inv(1 + exp(Q/T_SM_f))`, neutron fraction;
- lines 88–98 evolve `Xₙ` using explicit `(1-Xₙ)` proton fraction;
- lines 206–210 compute `Xₙ_nuc` and **`Yₚ = 2 * Xₙ_nuc/(1 - Xₙ_nuc)`**, not `2Xₙ_nuc`;
- lines 243–249 scan `Yₚ_mat`, calculate `χ²_mat = ((Yₚ_mat-.245)/.003)^2` and export `scanning.jld2`.

The code expression is `2 n_n/n_p`; under eq. (2.4) the counting approximation for helium is `2 n_n/(n_n+n_p)`. No reinterpretation of `X_n` as `n/p` is compatible simultaneously with both the initialization and ODE.

## 3. ROT020 now directly reads the original complete binary JLD2

Original binary file at author's pinned v2 Git snapshot:
`arXiv-2509.05618/data/out/scanning.jld2`
Git blob `10cc9b3f078fcadb91b5e520e75845859ca00b74`,
**151,089 bytes**, raw SHA-256
`51844a46ca904f57f941e0d0ebc3b5920c38bace76eea9e1d89cb5fd1f2c5786`.

Original notebook:
`arXiv-2509.05618/main.ipynb`,
Git blob `171c4a29e414860d724c817641896628f35982b0`,
**2,526,919 bytes**, raw SHA-256
`61d427c4de71b3920387234f6808ea7dee759d9166c77e1a9090695c5f5202d1`.

Both files **downloaded directly, SHA-256 verified**, not inferred from tree metadata; Wolfram HDF5 import accessed the original four datasets:
`/m_PBH_list [gram]`, `/β_PBH_list`, `/Y_P_mat`, `/chi2_mat`.
HDF5 dataset list displayed the Greek beta as mojibake `/Î²_PBH_list` in one listing interface; direct Unicode path `/β_PBH_list` reads correctly, yielding 100 values. This is an importer display detail, **not source corruption**.

- mass axis: **100** values from **6e8 g to 1e10 g**;
- beta axis: **100** values from **1e−20 to 1e−17**;
- `Y_P_mat`: **100×100**; `chi2_mat`: **100×100**;
- `max_{10k} |chi2_mat - ((Y_P_mat-0.245)/0.003)^2| = 4.3655745685100555e−11` (**PASS** floating-point consistency);
- original stored Y-code span: **[0.24457984107485917, 1.2891415044418126]**. Values above 1 arise in part of the parameter grid under the code's extrapolated mapping, are not plausible literal helium fractions, but do not independently establish the correctness of any physical boundary or applicability of those extreme parameter values.
- stored source grid cells with code `chi2<=4`: **4,469/10,000**.

Original notebook cell **15** directly reads **this file name** via `load(joinpath(output_data_directory,"scanning.jld2"))`, then selects `Y_P_mat` and `chi2_mat`, calls `heatmap!` and `contour!(...,levels=[4])`, and saves the first figure to **`Y_P.pdf`, `Y_P.png`**. Notebook also loads `scanning_old.jld2` for a separate v1-overlay comparison after this first figure has been saved.

**Scope:** this is an **actual original binary array numerical readback + direct notebook source route**, stronger than filename existence or equality of rendered PDF pixels. It still does not authenticate an individual historical Julia runtime or an exact build log for JCAP 02 (2026) 063. Earlier ROT010/011 established v2/v3 arXiv figures identical and GitHub Y_P.pdf different bytes but rendered content equivalent. Those results are preserved, not replaced.

## 4. Exactly defined SAME-TRAJECTORY counterfactual — NOT a new BBN simulation

Put `Y_code=2X/(1-X)`. At the same old neutron fraction (no ODE rerun)
`X=Y_code/(Y_code+2)`, hence
`Y_sameX_correct=2X=2Y_code/(2+Y_code)`.
This is a mathematical identity requiring **no physical assumptions beyond fixed X**; it does not change the ODE trajectory, `T_nuc`, hadron source, neutron rates or observed helium measurement.

- Grid first cell: `Y_code=0.24494317949740632` becomes **`Y_sameX=0.2182177096814038`**.
- New same-X grid values range **[0.21792928600636238,0.7838771926965713]**.
- The original 2σ observational range `Y_code∈[0.239,0.251]` maps pointwise to `Y_sameX∈[0.2134881643590889,0.223011994669036]`, disjoint from `[.239,.251]`.
- Holding all X and `T_nuc` frozen, only **513/10,000** grid cells satisfy a newly applied formula `((Y_sameX-.245)/.003)^2<=4`, compared to original **4469**. **Do NOT plot either difference as a revised PBH constraint**. A simple formula replacement changes the `β→Y_P` baseline itself, and SBBN calibration must be redone.
- To get corrected `Y_sameX=.251` at fixed X, the old mapping would require `Y_code=2*.251/(2-.251)=0.28702115494568325`; this is an algebraic target, **not** a β bound. The native root derivative/response and calibrated baseline depend on the evolution and chosen `T_nuc`.

Badacz REVIEW053 FIRST previously obtained SBBN `Y_code≈0.244765`, hence `2X≈0.21808`, and counterfactual calibration `T_nuc≈0.0997 MeV` versus code `0.0782 MeV`; measured native root shifts for corrected convention:
- V1 `2X(T1)=0.251`: for j22/28/34/62, relative +0.075/+0.036/+0.038/+0.034 dex;
- V2 `2ΔX(T0)=0.006`: +0.194/+0.095/+0.088/+0.087 dex.
These are **Badacz's model-internal results**, not my fresh Julia calculations; his prereg C1/P2 diagnostics include limitations. They are qualitatively different prescriptions; no arbitrary one is promoted to the final physical observable.

## 5. Explicit owner disposition / next necessary science gates

**ACK with source-specific rationale** to AUD1 ROT032:
1. I accept the (X_n) fraction vs ratio source discrepancy unconditionally for original **v2 author repository code**, given (2.4), (5.1), initialization and ODE; independent exact algebra and direct JLD2-chi2 verification PASS.
2. I accept that the stored scan uses an observably material mapping to the chosen helium measurement, not merely a cosmetic notation issue; the original JLD2 numeric link is verified.
3. I DO NOT issue a physical statement that the published JCAP Figure 5 is wrong by a fixed magnitude, nor accept same-X raw transformed grids as corrected bounds. Historical publication build/run identity still not proved.
4. To lift `HOLD` for physical PBH constraint one requires a **self-consistent SBBN calibration** under `Y=2X` (preferably validated against independent BBN reaction network), a native corrected source code replay with recorded tolerances and numerical stability, explicit comparison of resulting `Y_P(m,β)` with uncertainty, and review of independent hadron source validation (`E4 SOURCE_BLOCK` separately). Badacz REVIEW053 partly addresses first/second model-internal aspects but not the physical external generator.
5. Do not replace canonical IW/NASH or published paper results and do not contact authors without Moderator approval. Preserve prior AUD1/Badacz firstness and provide them this typed ACK, not an unwarranted scientific pass.

## 6. Reproducer and verification

Published same-directory Wolfram Language script:
`mech_s8_rot020_original_jld2_notebook_source_check.wl`.

Downloaded original author **JLD2 and notebook**, checked both **raw-file SHA-256**, enumerated both 100×100 matrices and both axes, calculated 10,000 `chi2` equality residuals, checked the notebook's code-to-figure route, and calculated fixed-X counterfactual. **Executed directly from the committed GitHub script's exact source readback: PASS 8/8 Boolean checks**. An independent original-source manual inspection crosschecked Julia lines 160/206–210/243–249 and article Eq. (2.4)/(5.1). No Julia execution claimed.

**Final:** `ROT020 OWNER_ACK_SOURCE_CONTRADICTION / ORIGINAL_JLD2_NUMERIC_READBACK_PASS / SOURCE_NOTEBOOK_FIG5_ROUTE_PASS / SAME_X_COUNTERFACTUAL_ONLY / HISTORICAL_JCAP_BUILD_ID_OPEN / PHYSICAL_BBN_RECALIBRATION_HOLD / E4_SOURCE_BLOCK / BW_PENDING / NO_CANON / NO_EXEC_SIGN`.
