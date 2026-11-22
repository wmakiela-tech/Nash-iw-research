---
artifact_id: IW_BADACZ_B1_J22_RESIDUAL_VINTAGE_VS_PROCESSING_PREREG_112_20261122
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel 099–110
created_at: 2026-11-22
document_type: PREREGISTRATION (zamrożona przed przebiegami)
authorization: Moderator 22 XI 20:30 („Akceptuję następny krok”); stała autoryzacja przebiegów 21 XI 16:05
claim_ceiling: NUMERYCZNY w modelach [▷] / NO_PBH_BOUND / NO_NOVELTY_ESTABLISHED / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_112: rozdzielenie reszty przy j22 na rocznik generatora (7.1.5 → 7.3) i obróbkę tablic BlackHawk, pełną tablicą z własnego Herwig 7.1.5

## 1. Cel

**Problem.** Po zamknięciu etykiety √s (REVIEW_110) w kontraście H73 względem L zostaje reszta r_H73 − r_U: −0.063…−0.076 dex w 3/4 komórkach j22 (−0.087 w komórce j22 code 0.251) i −0.013…−0.023 przy j62 (REVIEW_110 r2). Ta reszta łączy dwa różne źródła:
- rocznik generatora: Herwig 7.1.5 (rocznik tablic BlackHawk, REVIEW_106) wobec 7.3 (tablica H73 z 090);
- obróbkę: skrypty i zliczanie BlackHawk, siatkę 100 węzłów z interpolacją liniową, próg łączenia z PYTHIA (12.5 GeV wobec ELO 25–200 GeV), obsługę higgsa.

**Rozwiązanie.** Tablica W powstaje dokładnie jak H73 w 090 (ten sam przepis `mult_herwig`, te same energie, zdarzenia i ziarna, ten sam fold i ELO), ale z Herwig 7.1.5. Tablica V to Sc z REVIEW_110 z konwencją binowania PY. Ścieżka L → Sc → V → W → H73 daje:
- bin_c = r_V − r_c (binowanie na Sc),
- proc = r_W − r_V (obróbka przy stałym roczniku 7.1.5),
- vint = r_H73 − r_W (rocznik przy stałym przepisie i foldzie).

Domknięcie: (r_c − r_l) + bin_c + proc + vint = total(099) = r_H73 − r_l.

## 2. Przebiegi (`run112.sh`)

**MC.** Herwig 7.1.5, √s = 2E, `mult_herwig_097.py` (fizyka identyczna z `mult_herwig_090.py` i `090r.py`, którymi powstało H73), energie, liczby zdarzeń i ziarna z PREREG_090 (`requested.json`; 25…1e5 GeV, 2000/1000/500 zdarzeń, ziarna 90001–90011), 11 kanałów łącznie z higgsem. Każde wywołanie Herwig z limitem 1500 s.
- **Zadeklarowane przed przebiegiem:** top bez E = 1e5 GeV (w 7.1.5 √s = 2e5 pada, REVIEW_110 DEV-2). Krotność topu powyżej 51 200 GeV jest przycięta (`interp_loglog`). Ten sam zabieg po stronie 7.3 (tablica H73t) zmienia wydajności o ≤ 0.0013 dex w wierszach 0–28 (próba na sucho, niżej).
- Pilot higgsa w 7.1.5 (100 i 1e5 GeV, po 100 zdarzeń): PASS, K0S i hiperony nieobecne.

**Tablice** (`build_tables_112.py`): W, V, kontrolne H73 i Sc (muszą być bitowo równe `hadrons_090_H73.dat` i `hadrons_109_Sc.dat`) oraz opisowe H73t.
- Bramki: G_MC (każda żądana energia: rc 0, liczba zdarzeń zgodna, |⟨E_final/√s⟩ − 1| ≤ 1e−3, brak K0S i hiperonów), G_STAT (błąd statystyczny W ≤ 1% w wierszach 0–28), G_REBUILD_H73, G_REBUILD_SC, G_FINITE.

**Natywnie.** Ramiona w (W) i v (V) w węzłach 099/109, j22 i j62 w osobnych procesach. Kontrola k: tablica Sa, węzeł 22 −17.20, musi być bitowo równa 099 s22_1720. PRyMordial dla każdego węzła i net_base. Analiza jest wywoływana w skrypcie przebiegu z rzeczywistymi ścieżkami (łatka z REVIEW_110). Czas: ~1 h.

## 3. Analiza (`analysis_112.py`, sprawdzona na atrapie)

- Pierwiastki w i v: interpolacja liniowa, dokładnie jeden przedział. r_l, r_HERBH, r_H73 z `analysis099.json`; r_c z `analysis109.json`.
- Bramki: G_TABLES, G_COMPLETE, G_V2, G_DRIVER, G_BASE (|Y_base − Y_base_l(099)| ≤ 5e−4 dla w i v przy obu masach).
- Estymaty w każdej komórce: bin_c, proc, vint oraz domknięcie (musi wynosić 0 do błędu zaokrąglenia).

**Próba na sucho (przed zamrożeniem; ujawniam, co widziałem).** Budowę tablic sprawdziłem z danymi 7.3 podstawionymi jako atrapa W. Obie odbudowy są bitowo równe, a bramki przechodzą. Widziałem przy tym stosunki tablic V/H73 w wierszach 0–28: piony +0.02…+0.04 dex, kaony −0.15…−0.21, nukleony −0.03…+0.02. To są istniejące tablice (klasa znana z 098/099); W z 7.1.5 nie było policzone. Test analizy na atrapie (ramiona w i v zastąpione ramieniem c z 109) wykrył błąd mojego wzoru na domknięcie, poprawiony przed zamrożeniem, oraz błąd w REVIEW_110 §3 (REVIEW_110 r2).

## 4. Predykcje (moje, zamrożone)

Tolerancje ≥ 0.03, czyli nie poniżej udokumentowanego maksimum zmienności pojedynczego pierwiastka.

- **Pr1:** |proc| ≤ 0.03 w co najmniej 6/8 komórkach. Uzasadnienie: tablice BlackHawk odtwarzają 7.1.5 do 0.0097 dex dla kwarka u w 6 węzłach (REVIEW_106) i do 0.022 dex dla 10 kanałów przy 1e5 GeV (REVIEW_110).
- **Pr2:** vint ≤ −0.03 w co najmniej 3/4 komórkach j22 (reszta przy j22 to głównie rocznik).
- **Pr3:** |vint| ≤ 0.03 w co najmniej 3/4 komórkach j62.
- **Pr4:** |bin_c − d_bin(099)| ≤ 0.03 we wszystkich 8 komórkach (krok binowania przenosi się z Sa na Sc).

## 5. Granice

- Przepis MC (proces twardy z `LEP.in` BlackHawk, zliczanie z HepMC) jest wspólny dla W i H73. vint mierzy więc rocznik i strojenie domyślne łącznie, bez rozdzielenia.
- proc łączy kilka czynników (próg łączenia z PYTHIA, siatkę, higgsa, skrypty BlackHawk) i ich nie rozdziela.
- Pojedyncze przebiegi; szum pojedynczego pierwiastka do ~0.03.
- Wynik dotyczy progów w modelach, nie fizycznej granicy PBH.
