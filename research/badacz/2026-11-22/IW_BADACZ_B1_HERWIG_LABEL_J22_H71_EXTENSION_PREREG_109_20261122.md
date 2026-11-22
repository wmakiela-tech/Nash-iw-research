---
artifact_id: IW_BADACZ_B1_HERWIG_LABEL_J22_H71_EXTENSION_PREREG_109_20261122
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel 099–106
created_at: 2026-11-22
document_type: PREREGISTRATION (zamrożona przed przebiegami)
authorization: obrót „O” Moderatora 22 XI 18:33; krok zapowiedziany po REVIEW_106; stała autoryzacja przebiegów 21 XI 16:05
claim_ceiling: NUMERYCZNY w modelach [▷] / NO_PBH_BOUND / NO_NOVELTY_ESTABLISHED / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_109: zamknięcie pomiarem niejednoznaczności etykiety √s przy j22. Brakujący zakres pierwotnych 5e4–1e5 GeV z Herwig 7.1.5

## 1. Cel

**Problem.** REVIEW_100 i 102 zostawiły wpływ etykiety √s przy j22 nieoznaczony: −0.01…−0.03 dex z wariantem Sa (ekstrapolacja stała) i −0.05…−0.08 z wariantem Sb (kształt H73). Po przeetykietowaniu tablica HERWIG z BlackHawk nie ma danych dla pierwotnych powyżej 5e4 GeV. REVIEW_106 ustalił, że rocznik tablic to Herwig 7.1.5.

**Rozwiązanie.**
- Generuję brakujący zakres tym samym rocznikiem, przy poprawnym √s = 2E, i buduję tablicę Sc.
- Mierzę natywnie jej próg względem L, Sa i Sb z 099.
- Szew (A) przy E = 5e4 sprawdza przepisy wszystkich 10 kanałów. Dotąd zweryfikowany był tylko kwark u.

## 2. Przebiegi (`run109.sh`)

**MC.**
- Herwig 7.1.5, √s = 2E, E ∈ {5e4, 7.07e4, 1e5} GeV, 2000 zdarzeń.
- Kanały: up, down, strange, charm, bottom, top, gluon, W±, Z0, τ.
- Pilot przy 500 GeV PASS dla kanałów gluon, W±, Z0, top i τ.

**Tablica Sc** (`build_tables_109.py`):
- do 5e4 GeV jak Sa (wiersze przeetykietowane, higgs bez zmiany);
- ponad 5e4 GeV krotności 7.1.5 (log-log) dla 10 kanałów; stała dla fotonu, elektronu i mionu;
- konwencja binowania jak w Sa.

Skrypt odtwarza Sa bitowo (G_REBUILD; sprawdzone na próbie z atrapą MC).

**Natywnie.** Ramię c (Sc) w węzłach 099: j22 i j62 w osobnych procesach. Kontrola k: tablica Sa, węzeł 22 −17.20, musi być bitowo równa 099 s22_1720. Czas: ~40 min.

## 3. Analiza (`analysis_109.py`, sprawdzona na atrapie)

**(A) Szew:**
- porównanie 7.1.5 przy E = 5e4 (√s = 1e5) z wierszem E′ = 1e5 tablicy, dla 10 kanałów × 5 gatunków;
- tolerancja max(0.04, 4·se); komórki z mniej niż 20 zliczonymi cząstkami w MC raportuję, ale ich nie bramkuję;
- etykieta SEAM_PASS albo SEAM_FAIL.

**(B) Bramki:** G_MC, G_TABLES, G_COMPLETE, G_V2, G_DRIVER, G_BASE.

**Estymaty w każdej komórce:** d_label_c = r_c − r_l oraz r_c − r_s i r_c − r_b.

## 4. Predykcje (moje, zamrożone)

Tolerancje ≥ 0.03, czyli nie poniżej udokumentowanego maksimum zmienności pojedynczego pierwiastka (REVIEW_100–108).

- **Pr1:** SEAM_PASS.
- **Pr2:** |r_c − r_s| ≤ 0.03 we wszystkich 4 komórkach j62 (zakres 5e4–1e5 GeV nie ma tam znaczenia).
- **Pr3:** r_c ∈ [min(r_s, r_b) − 0.03, max(r_s, r_b) + 0.03] w co najmniej 3/4 komórek j22.

## 5. Granice

- Pierwotne > 1e5 GeV nie wchodzą do żadnej tablicy (siatka autorów).
- Szew sprawdza przepisy tylko przy jednej energii.
- Wynik dotyczy progów w modelach, nie fizycznej granicy PBH.
