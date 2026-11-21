---
artifact_id: IW_BADACZ_B1_E4_TABLE_DOMAIN_PREREG_088_20261121
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), współwłaściciel natywny B1, właściciel T2
created_at: 2026-11-21
document_type: PREREGISTRATION (zamrożona przed jakimkolwiek przebiegiem pomiarowym)
authorization: stała autoryzacja przebiegów Moderatora 21 XI 16:05 (przekaz EKS1); propozycja P3 w SYNTH_087
follows: SYNTH_087 §3 (Nash-iw-research@dc39ce2); E4 HOLD od REVIEW_071
claim_ceiling: NUMERYCZNY w modelach [▷] / NO_PBH_BOUND / NO_PAPER_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_088: E4, czułość progu j22 na traktowanie tablicy hadronów poniżej 1e9 g

## 0. Pytanie

Tablica autorów zaczyna się od 1e9 g. Dla j22 (1.12e9 g) ok. 81% emisji hadronów przypada na masy niższe, gdzie kod ekstrapoluje wiersze 0–1. Te wiersze są już lekko ucięte przez sufit E_prim = 1e5 GeV (SYNTH_087 §3).

- **Q:** o ile przesuwa się próg β dla j22, gdy zamiast ekstrapolacji autorów użyć:
  - (C) trendu bez ucięcia, czyli wariantu fizycznie preferowanego;
  - (A) bezpośrednich, uciętych wierszy BlackHawk, czyli dolnego nawiasu będącego artefaktem sufitu?
- SYNTH_087 szacuje E4_C ≈ −0.03 dex. Ten pomiar zamienia szacunek w liczbę.

## 1. Tablice (`build_tables_088.py`)

- **A:** 10 bezpośrednich wierszy PYTHIA-BBN dla 1e8…7.94e8 g (`data/hadrons_087_PY_rows_1e8_1e9.dat`, ustawienia autorów) doklejone przed 100 wierszy autorów.
- **C:** wiersze 0–4 autorów zastąpione, a 10 wierszy 1e8…7.94e8 g doklejone. Wartości pochodzą z prawa potęgowego zakotwiczonego w wierszu 5 autorów, ze średnim lokalnym nachyleniem wierszy 5–10, osobno dla każdego gatunku (≈ −1.30).
  - Podniesienie względem autorów wynosi +0.008 dex w wierszu 0 i maleje do +0.0003 w wierszu 4.
- **Wspólne:** wiersze 5–99 skopiowane dosłownie (bramka V_TABLE). Iniekcja przez kopię drzewa źródeł jak w PREREG_085, mechanizm zweryfikowany tam przez V_INJ_POS i V_INJ_NEG.

## 2. Plan

- j22, ramię orig, kod i sieć (metoda transferu szybkości jak w 083/085).
- Siatka jak HER orig_22 w 085: 0.05 dex od −18.75 do −16.50, czyli 46 węzłów, plus baza na wariant. Daje to 94 wywołania Julii (2 strumienie, ~20 min) i 97 przebiegów sieci.
- Komórka odniesienia PY to dane 083 (`orig_22`), bez nowego przebiegu.
- Runner `run088.sh` z twardymi bramkami: świeży katalog, SHA wejść, każdy rc ≠ 0 to stop, bez „ALL_DONE”.

## 3. Estymandy, bramki, etykiety (`analysis_088.py`)

- **Estymandy:**
  - E4_C = lb_C − lb_PY;
  - E4_A = lb_A − lb_PY.
  - Obie dla kodu i sieci, przy 0.251 i 0.2484, z interpolacją liniową i dokładnie jednym przedziałem.
- **Bramki:**
  - V7 (komplet);
  - V2_EXACT ≤ 1e-6;
  - V6;
  - V_TABLE;
  - V_BASE ≤ 5e-4;
  - V3 ≤ 1e-5 i baza sieci = 083;
  - V4 i V5 na c22_1720 ≤ 1%.
  - Progi wyprowadzone z wpływu na decyzję i znanego szumu (REVIEW_086 r2).
- **Etykieta LC** (z max |E4_C| po kodzie, sieci i obu celach):
  - < 0.05 → `E4_SMALL`;
  - ≥ 0.10 → `E4_MATERIAL`;
  - w przeciwnym razie `E4_INTERMEDIATE`.
  - Uzasadnienie progu: 0.05 = 5 × szum solwera na pierwiastek (≤ 0.010 dla j22).
- **LA:** opisowo; zakres E4_A jako dolny nawias.

## 4. Predykcje (poinformowane przez SYNTH_087 §3)

- **P1:** E4_C dla kodu przy obu celach ∈ [−0.05, 0), czyli lekko silniejsze ograniczenie.
- **P2:** E4_A dla kodu przy 0.251 ≥ +0.10, czyli ucięte wiersze wyraźnie osłabiają.
- **P3:** E4_C kodu i sieci zgodne w granicy 0.02.

## 5. Granice

- Dotyczy tylko j22 (najbardziej narażonej masy) i ramienia orig. Generator PYTHIA autorów.
- Wariant C to model trendu, nie hadronizacja ponad 1e5 GeV. Tej nie da się policzyć z tablicami BlackHawk v2.3; HDMSpectra działa tylko dla epoki obecnej.
- Szum solwera ~0.01 dex na pierwiastek.
- Wynik jest numeryczny w modelach. Nie jest granicą na PBH.
- Test atrapy przed zamrożeniem: komórki PY podstawione jako A i C dały E4 = 0 dokładnie, a ścieżka etykiet zadziałała.
