---
artifact_id: IW_DAX_S9_ROT025_BORN_ZERO_NEUTRAL_NONZERO_I2_PROJECTION_AND_CROSS_MODEL_TRANSFER_HOLD_001_20261122
date: 2026-11-22
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
exposure: PUBLIC
sync_state: GITHUB_REPORT_ONLY_PENDING_BW_INGEST
claim_ceiling: NO_AUTHOR_FIT_REEXEC / NO_EXPERIMENTAL_CI / NO_NEUTRINO_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX9 ROT025 — Neutral direct-Born zero does not imply I=2 zero

Original source-first mathematical and reproducible model-sensitivity audit, 22 Nov 2026. This is standard isospin physics and a source-model scope falsifier, NOT novel particle physics nor rejection of a separate 2022 published fit.

## Direct primary-source contact

1. Dai & Pennington, Phys Rev D90,036004 (2014), DOI 10.1103/PhysRevD.90.036004, ORIGINAL author 61-page PDF text actually read https://misportal.jlab.org/sti/publications/12980/attachments/9416/1404.7524v2.pdf . Original Eq(5) explicitly gives orthogonal physical charged/neutral-to-I0/I2 amplitude rotation, Eq(7) interference-free SUM over matched charge channels, Eq(9) hadronic unitarity constraints, Eq(27) fitted alpha coupling-function functional form. Actual fitted numeric alpha coefficients, hadron T data and complex author Solution-I full amplitudes were NOT OBTAINED; author plots and pole tables do not enable literal numerical replay. The original PDF web screenshot attempt returned cache miss; no author native PDF bytes or visual page verified.
2. Surovtsev et al, Particles 5 (2022) 210–224 DOI 10.3390/particles5030019, original open-access full paper text actually read https://inspirehep.net/files/6753cb5dfe873785aacfbf9eb5b2fff0 . Authors explicitly OMIT I2 in neutral-only rescattering, partly motivating this by zero direct neutral Born and absence of I2 meson resonances. Source Eqs(11),(12) retain only F00(I0) and F22(I0); symbolic couplings Eq(13), no sourced simultaneous BOTH charged and neutral S,D0,D2 I0/I2 fit. Author numerical fit values and native complex amplitude arrays were NOT OBTAINED. PDF screenshot cache miss, visual/byte audit NOT claimed. This paper is not experimentally falsified by another model's numerical rates.
3. Klevansky/Lemmer/Beygi EPJA61 49 (2025) DOI 10.1140/epja/s10050-025-01524-6 original equations (28),(65),(83) source replayed in DAX9 ROT012; exact predecessor source Python verify_coherent_born_fsi.py authenticated SHA256 60774900f007d1e1ef8a9c463168c9deee8aa065589ce89f98926e097e14633d. 2025 model is NOT Dai Solution I and ROT019 found 17–21 degree phase differences relative to independently sourced Roy/GKPY.

## Exact charge-to-isospin counterexample

Use normalized symmetric charge basis (C,N) and isospin basis (A0,A2). Dai source Eq(5) up to harmless overall sign: U=[[-sqrt(2/3), -sqrt(1/3)],[-sqrt(1/3), +sqrt(2/3)]], orthogonal U^T U=I. A DIRECT scalar-QED charge Born vector (A_C,A_N)=(B,0), arbitrary nonzero complex B, transforms into A0=-sqrt(2/3) B and A2=-sqrt(1/3) B. Therefore A2/A0=1/sqrt2, with isospin-2 component fraction |A2|^2/(|A0|^2+|A2|^2)=**1/3**. Both nonzero isospin components CANCEL in the neutral direct-Born projection. Artificial deletion of I2 while holding I0 Born fixed generates a SPURIOUS nonzero neutral direct Born amplitude +sqrt(2)/3 B. Hence neutral direct Born=0 does not imply I2=0. This demonstrates the proposed implication is invalid AS ALGEBRA, although an explicitly fitted neutral-only physical approximation may still be useful for other dynamical reasons. No novelty claim; it follows standard isospin projection.

## Actual original 2025 model, conditional neutral J00 I2-delete numeric falsifier

Neutral original Eq65/83 amplitude proportional to C0+C2, C0=Jpi*T0_pi_pi/3+JK*T0_K_pi/sqrt6, C2=-Jpi*T2_pi_pi/3. For source-frozen 2025 model (MPI=.140,MK=.496,FPI=.093,cutoff=1.351GeV), the conditional neutral J00 cross-section ratio full(I0+I2)/I0-only is |1+C2/C0|^2, BOTH amplitudes coherent. No experimental fitted result; no separate Surovtsev 2022 numeric fit.

| W GeV | full / I0 only |
|---:|---:|
| .35 | 1.409758 |
| .40 | 1.357624 |
| .54 | 1.140681 |
| .65 | .957046 |
| .80 | .717161 |
| .85 | **.673820** |
| .87 | .712949 |
| .89 | .927678 |
| .90 | 1.255021 |
| .91 | **1.977748** |
| .93 | **3.708836** |
| .95 | 2.115352 |
| .98 | 1.114215 |

Interference sign depends on W; deletion of I2 cannot be interpreted as removing an always-positive contribution. Using SAME original R68 H(W) Egamma=1436.554 GeV, T=.00007818527068831995 GeV, and source chiral J00 model, fold ratios K(full)/K(I0-only): [.35,.54] 1.253926; [.54,.80] .961413; [.80,.90] .716375; [.90,.95] **2.610561**; [.85,.95] **1.462270**; [.95,.98] 1.386794. These ratios are NOT physical full pion source/neutrino/BBN rates or model fit to Belle/MarkII.

## Reproducibility and anti-overclaim

Actual executing original Python from predecessor ROT012 (source SHA pinned) plus original new verify_rot025_isospin_scope.py and separate standard-library-only independent_check_rot025.py. Tests: Eq(5) general COMPLEX Born isospin inversion and I2-delete negative control PASS; original 2025 Eq83 neutral amplitude reconstruction 5/5; 13/13 amplitude-level source ratio identity PASS; independent 65-digit mpmath versus binary64 hadronic/photo loops seven W max rel **5.50911e-15**; SciPy adaptive vs 180-node independent NumPy Legendre quadrature six bands times two models max rel <3e-15. TWO fresh isolated clean directory replays each regenerate frozen original JSON+2 CSV **3/3 BYTE IDENTICAL PASS**. Local complete archive CRC PASS and **13/13 member payload SHA PASS**, 14 ZIP members including manifest.

Local original full detailed 11.5K science report and executable archive attached to originating chat: DAX9_ROT025_Neutral_Born_Zero_Nonzero_I2_Source_CrossModel_Gate_Repro.zip, ZIP SHA256 **8fc0be0b8db28a94e42204e4697978e60235743c38ac4a1dd6702f66bbd70eb0**. THIS GitHub Markdown is TEXT SCIENCE REPORT ONLY, NOT uploaded ZIP, original PDFs, or author full numeric fits. No BW ingestion, I3, owner signoff.

DECISION: original 2014 author's coupled-channel I0/I2 fitted Solution I numerics remain ACCESS HOLD; 2022 published neutral-only I0 S+D2 formulas are not a substitute for joint both-channel I0/I2 S+D0+D2 fitted amplitudes. Do not replace source-specific 2022 fit with 2025 model, do not infer new experimental tension, and do not resume arbitrary Belle angular-box scans. Next material source gate: obtain independent numeric genuine coupled-channel real/complex partial-wave coefficient arrays or undertake explicitly marked new joint fit with source-level covariance.

RETURN: ORIGINAL_2014_2022_PRIMARY_SCOPE_READ_PASS / NEUTRAL_BORN_ZERO_NOT_I2_ZERO_EXACT_PASS / INDEPENDENT_2025_NEUTRAL_I2_OMISSION_SENSITIVITY_PASS / HIGH_PRECISION_AND_QUADRATURE_PASS / AUTHOR_SOL_I_AND_2022_FIT_NATIVE_NUMERICS_HOLD / NO_EXPERIMENTAL_CI / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.