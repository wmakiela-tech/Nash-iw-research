---
artifact_id: IW_PRF12_R24_FINITE_READOUT_RESET_AND_SOURCE_LIFETIME_CERTIFICATE_001_20261101
created_at: 2026-11-01
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
problem_id: PRF12_R23_FINITE_READOUT_RESET_AND_CORRELATION_LIFETIME
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_QND_Z_IDLE_AND_ASSIGNMENT_CONTRACTION / SHOT_BOUNDARY_RESET_FLOOR / POISSON_PERSISTENCE_SUFFICIENT_CERTIFICATE / STOCHASTIC_DOMINATION_BINOMIAL / INDEPENDENT_BLOCH_CHECK_PASS / REFEREE_PENDING
claim_ceiling: NO_FULL_FINITE_DETECTOR_DEVICE_CERT / NO_NON_QND_DETECTION_MODEL / NO_SOURCE_RESET_RATE_IDENTIFICATION / NO_NOVELTY / NO_CANON / NO_EXEC / ORIGINAL_3Q_LOCC_CLOSURE_OPEN
---

# PRF12 R24 — skończony odczyt, reset sensora i ograniczona trwałość źródła w certyfikacie R23

**Data:** 1 XI 2026. **Status naukowy:** twierdzenia źródłowo warunkowe, niezależna kontrola analityczna i numeryczna; brak niezależnej recenzji. W odróżnieniu od R23 nie poszukuje się nowych wag ani impulsów. Nową zmienną jest **czas fizyczny wymagany dla kolejnego odczytu**, błędy klasycznej etykiety ± i zmiana źródła A **w obrębie pary**.

## 0. Source typed prior art, first owner i zakres

Pierwszy właściciel źródła: PRF11 R35; stan wejściowy: PRF12 R22 i R23, których kontrakt jest udokumentowany w [R23 source index](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-01/IW_PRF12_R23_SOURCE_INDEX_AND_REPRO_MANIFEST_001_20261101.md). Nie powtarzamy całego dowodu R23: **używamy dokładnie jego oddzielnie certyfikowanych granic** dla impulsu prostokątnego i wag X=.18, Y=.20, Z=.62:

\[
\forall\xi\in\mathbb R:\quad p_A(\mathrm{same}\mid\xi)\ge a_0=0.576,
\qquad p_B(\mathrm{same})\le b_0=0.526.
\tag{R24.baseline}
\]

Stałe są zaokrąglonymi *konserwatywnymi* punktami R23, a nie wartościami optymalnymi. R23 podaje dla B bezpośrednio około .5252387409109164, zaś dolną kontrolę A 0.576539... . Brak nowej niezależnej reprodukcji całej siatki przedziałowej R23 nie pozwala udawać, że R24 jest jej zamiennikiem.

