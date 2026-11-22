---
artifact_id: IW_BADACZ_B1_HERWIG_TABLE_FACTORIAL_V_ARM_PREREG_101_20261122
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel 099/100
created_at: 2026-11-22
document_type: PREREGISTRATION (zamrożona przed przebiegiem natywnym)
authorization: Moderator 22 XI 13:56 („Zatwierdzam”, ramię V i powtórzenie kontroli zapowiedziane po REVIEW_100); stała autoryzacja przebiegów 21 XI 16:05
claim_ceiling: NUMERYCZNY w modelach [▷] / NO_PBH_BOUND / NO_NOVELTY_ESTABLISHED / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_101: brakujące ramię V (domknięcie układu 2×2 etykieta × binowanie) i drugi pomiar szumu solwera

## 1. Cel

**Udziały przyczynowe.** REVIEW_100 rozłożył kontrast wzdłuż jednej ścieżki L → Sa → Ua. Mech-S10 ROT014 i INT10 ROT018 wskazali, że bez ramienia V (stara etykieta i nowe binowanie) nie ma unikalnych udziałów przyczynowych. Ramię V domyka układ 2×2: główne efekty etykiety i binowania oraz interakcja I. Dla dwóch czynników alokacja Shapleya to średnia obu ścieżek.

**Szum.** W REVIEW_100 kontrola L wobec R2 (zmiana tablicy rzędu 1e−4) przesunęła jeden pierwiastek o 0.031. „Powtórzenie kontroli” wykonuję jako ramię E = L × 1.0001: identyczne wejście dałoby wynik bitowo identyczny, bo solwer jest deterministyczny. To drugi, niezależny pomiar szumu solwera w tych samych 8 komórkach.

## 2. Tablice i przebiegi

| tablica / ramię | zawartość |
|---|---|
| **V** (`build_tables_101.py`) | Złożenie identyczne jak w 099, część HERWIG z konwencją binowania PY. Na wierszach 0–28 V/L = 0.0456707 dex (sprawdzone na próbie). Skrypt odtwarza L bitowo (G_REBUILD w `run101.sh`). |
| **E** | `hadrons_099_L.dat` × 1.0001 (`table_scale_085.py`) |
| **k** | tablica L, węzeł 22 −17.20; musi być bitowo równy 099 l22_1720 (kod i sieć) |
| **węzły** | identyczne z ramieniem l z 099 (52 na ramię) |

**Skala:** 105 przebiegów Julii (dwa procesy: k + v oraz e) i 106 PRyMordial; ~35 min.

## 3. Estymaty (`analysis_101.py`, sprawdzone na atrapie)

Pierwiastki L, Sa i Ua biorę z 099 (ten sam kod i te same węzły).

| estymata | definicja |
|---|---|
| main_label | [(r_Sa − r_L) + (r_Ua − r_V)]/2 |
| main_bin | [(r_V − r_L) + (r_Ua − r_Sa)]/2 |
| I | (r_Ua − r_Sa) − (r_V − r_L) |
| dj | r_E − r_L + log₁₀1.0001 |

## 4. Predykcje (moje, zamrożone)

Tolerancje wyprowadzam z udokumentowanego maksimum szumu: max |d_ctrl| = 0.031 w 099. To łatka z REVIEW_100.

- **Pr1:** |I| ≤ 0.04 w co najmniej 7/8 komórkach. Na poziomie tablic interakcja jest zerowa.
- **Pr2:** main_label < 0 w co najmniej 7/8.
- **Pr3:** max |dj| ≤ 0.04 i mediana |dj| ≤ 0.01.

## 5. Granice

- Ekstrapolacja ponad 5e4 GeV jak w Sa (stała). Wariant Sb nie wchodzi do układu czynnikowego.
- I i efekty główne niosą szum dwóch do czterech pierwiastków (do ~0.03 każdy w komórkach j22 code).
- Wynik dotyczy progów w modelach, nie fizycznej granicy PBH.
