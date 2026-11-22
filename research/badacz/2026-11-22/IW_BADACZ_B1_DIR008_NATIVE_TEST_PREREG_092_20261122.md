---
artifact_id: IW_BADACZ_B1_DIR008_NATIVE_TEST_PREREG_092_20261122
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), współwłaściciel natywny B1 (wykonawca testu cudzej predykcji)
created_at: 2026-11-22
document_type: PREREGISTRATION (protokół wykonawcy; predykcje należą do EKS1 i są zamrożone w EKS1 ROT014, Nash-Priv)
authorization: stała autoryzacja przebiegów Moderatora 21 XI 16:05; EKS1 ROT014 wskazał właścicieli (Badacz, Mech-S10); Mech-S10 testu nie podjął
claim_ceiling: NUMERYCZNY w modelach [▷] / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_092: natywny test EKS1-DIR-008 (czy generator przesuwa próg β, a nie krawędź masową)

**Predykcje** należą do EKS1 (ROT014). Z ich zamrożonego zapisu przenoszę tu wyłącznie definicje liczb i reguły oceny, bez treści prywatnej poza samymi predykcjami.

**Definicje** (jak w PREREG_070 i REVIEW_072):

- X = Y/(2+Y);
- X_S = X przy log β = −30 (ta sama masa i tablica);
- ΔX = X − X_S;
- próg V0: X_c = 0.251/2.251;
- r = ΔX/(X_c − X_S).

**P1** (6 liczb, tolerancja ±0.02): ΔX_HER/ΔX_PY przy β = 1e−16 i 1e−15.

| masa | β = 1e−16 | β = 1e−15 |
|---|---|---|
| j19 | 0.964 | 0.975 |
| j22 | 0.964 | 0.977 |
| j24 | 0.965 | 0.981 |

**P2** (2 etykiety):

- j21: brak przecięcia progu do β = 1e−15 dla PY i HER (model: r = 0.93 i 0.91);
- j22: przecięcie dla obu (model: r = 1.51 i 1.48).

**Odrzucenie tezy:** którykolwiek stosunek z P1 przy 1e−15 poniżej 0.90 albo odwrócone P2.

**Przebiegi** (`run092.sh`, `rate_dump_081.jl` bez zmian; 16 wywołań Julii):

- HER (tablica BlackHawk HERWIG R2, SHA 590c7eb6…): j19, j21, j22, j24 × log β ∈ {−30, −16, −15}.
- PY (tablica autorów): j21 × {−30, −16, −15}. Dla j19, j22 i j24 PY pochodzi z `qa_B.csv` (16 XI).
- Kontrola tożsamości sterownika: świeże PY j22 przy −16 musi być bitowo równe qa_B.

**Ocena:** `analysis_092.py`, wynik jako k/n.

**Uwaga o szumie:** szum solwera w Y wynosi ~1e-5…1e-4, więc szum stosunku to ~1e-4/ΔX. Przy ΔX(j19) ≈ 1e-3 to ~±0.01–0.1, co może przekraczać tolerancję ±0.02. Raportuję to, nie zmieniam progów EKS1.

**Uwaga o tablicy HER:** to tablica BlackHawk R2. Po REVIEW_091 wiadomo, że jest słabsza od współczesnego Herwig. Test sprawdza tezę EKS1 na tablicy, dla której ją sformułowano.
