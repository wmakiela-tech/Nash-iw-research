---
artifact_id: IW_BADACZ_B1_SUBGRID_EXTRAPOLATION_NATIVE_CHECK_PREREG_116_20261123
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel 099–115
created_at: 2026-11-23
document_type: PREREGISTRATION (zamrożona przed przebiegami)
authorization: Moderator 23 XI 07:11 („Kontynuuj”); stała autoryzacja przebiegów 21 XI 16:05
answers: Mech-S10 ROT021/ROT022 (ekstrapolacja Wu–Xu poniżej 1e9 g); REVIEW_110 r3
claim_ceiling: NUMERYCZNY w modelach [▷] / NO_PBH_BOUND / NO_NOVELTY_ESTABLISHED / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_116: natywny pomiar kanału ekstrapolacji poniżej 1e9 g (warianty topu, recepta z artykułu, ramię kalibracyjne) i test przybliżenia ekspozycyjnego D

## 1. Cel

**Fakty wyjściowe.**
- Kod Wu–Xu (d395183, `tool_script-hadrons_from_PBH.jl`) ekstrapoluje szybkości hadronowe poniżej najniższego wiersza tablicy (1e9 g) liniowo w log–log z wierszy 0–1.
- Przy j22 (1.121e9 g) na ten reżim przypada ~49% całkowanej konwersji n↔p wywołanej hadronami, przy j62 (3.494e9 g) ~7% (REVIEW_110 r3, `posthoc_115`).
- Artykuł (arXiv:2509.05618, równania 4.4–4.5) opisuje dla M < 1e9 g skalowanie analityczne T^1.3 (szybkość ∝ M^−1.3) kalibrowane przy 1e9 g. Kod używa nachylenia wierszy 0–1 tablicy, ~−1.16…−1.21 dla Sc.

**Pytania.**
- (a) Czy skrajne warianty przyciętego topu (×0, ×3) przesuwają próg natywnie, gdy wliczyć ekstrapolację (Mech-S10 ROT022)?
- (b) Ile zmienia próg recepta z artykułu wobec ekstrapolacji kodu?
- (c) Czy D, czyli tanie przybliżenie ekspozycyjne z `posthoc_115`, przewiduje natywne przesunięcie progu? Test na silnym ramieniu kalibracyjnym.

## 2. Ramiona (`build_tables_116.py`, `run116.sh`)

Bazą jest tablica Sc z PREREG_109, odbudowana najpierw bitowo (G_REBUILD_SC).

| ramię | zmiana względem Sc | masy |
|---|---|---|
| x0 | segment topu E > 7.07e4 GeV ×0 | j22 |
| x3 | ten sam segment ×3 | j22 |
| p13 | 20 wierszy dopisanych poniżej 1e9 g (M0·10^(−k/2), k = 1…20) z szybkością ∝ M^−1.3 od wiersza 0; wiersze ≥ 1e9 g bez zmian | j22, j62 |
| s15 | jak p13, ale z wykładnikiem −1.5 (ramię kalibracyjne: silna, znana zmiana wyłącznie w ekstrapolacji) | j22, j62 |

- Kontrola k: tablica Sa, węzeł 22 −17.20, bitowo równa 099 s22_1720.
- Węzły: siatka 099/109. Dla s15 rozszerzona do −18.70 (j22) i −20.30 (j62), bo przewidywane przesunięcie wychodzi poza siatkę.
- Po każdym przebiegu Julia surowy zrzut jest haszowany, deduplikowany i usuwany (miejsce na dysku; zgoda Moderatora z 22 XI).

## 3. Przybliżenie D (policzone przed przebiegiem, `tables116.json`)

D to zmiana (w dex) całkowanej konwersji n↔p wywołanej hadronami w zrzucie natywnym ramienia w z 112 (węzły w22_1740 i w62_1940). Każdy gatunek jest ważony swoimi członami zrzutu. M(t) = max(M_init(1 − t/τ)^(1/3), M_init·e^−20). Stosunki szybkości liczę interpolacją kodu, łącznie z ekstrapolacją.

| ramię | D przy j22 | D przy j62 |
|---|---|---|
| x0 | −0.0093 | — |
| x3 | +0.0219 | — |
| p13 | +0.0177 | +0.0074 |
| s15 | +0.3070 | +0.2096 |

## 4. Analiza (`analysis_116.py`, sprawdzona na atrapie)

- Bramki: G_TABLES, G_COMPLETE, G_V2, G_DRIVER, G_BASE (|Y_base − Y_base_l(099)| ≤ 5e−4).
- Pierwiastki: interpolacja liniowa, dokładnie jeden przedział. dr = r_ramię − r_c (r_c z `analysis109.json`); średnia z 4 komórek (code/net × Y* 0.251/0.2484).
- Etykiety: GATE_FAIL_NO_LABEL, NOT_BRACKETED (dla pary ramię–masa), MEASURED.

## 5. Predykcje (moje, zamrożone)

Dla każdej pary ramię–masa: średnie dr ∈ [min(−0.8D, −1.5D) − 0.03, max(−0.8D, −1.5D) + 0.03].

- Zakres c = −dr/D ∈ [0.8, 1.5] pochodzi z kalibracji binowania: jednorodna zmiana tablicy o 0.0457 dex dała bin_c od −0.040 do −0.066 (REVIEW_113).
- Margines 0.03 to udokumentowane maksimum zmienności pojedynczego pierwiastka.

| para | przedział średniego dr | charakter testu |
|---|---|---|
| x0\|22 | [−0.023, +0.044] | słaby (efekt mniejszy niż szum) |
| x3\|22 | [−0.063, +0.012] | słaby |
| p13\|22 | [−0.057, +0.016] | słaby |
| p13\|62 | [−0.041, +0.024] | słaby |
| s15\|22 | [−0.491, −0.216] | **silny: test przybliżenia D** |
| s15\|62 | [−0.344, −0.138] | **silny** |

Opisowo raportuję też c_hat = −średnie dr / D.

**Ryzyko jawne.** D waży konwersje równo w czasie i pomija wymywanie przy T > ~1.8 MeV. W s15 przyrost wypada pod koniec życia PBH, więc c może wyjść poza [0.8, 1.5]. To jest właśnie testowane.

## 6. Granice

- Ramiona p13 i s15 zmieniają tylko reżim poniżej 1e9 g. Nie są fizyczną hadronizacją przy M < 1e9 g (tablice BlackHawk nie sięgają tam energii pierwotnych).
- x0 i x3 to skrajne nawiasy, nie realistyczne warianty (realistyczna kontynuacja nachylenia: D ≤ 0.0003).
- Pojedyncze przebiegi; szum pojedynczego pierwiastka do ~0.03.
- Wynik dotyczy progów w natywnym modelu Wu–Xu, nie fizycznej granicy PBH.
