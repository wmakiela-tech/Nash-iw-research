---
artifact_id: IW_BADACZ_B1_MODERN_GENERATOR_TABLES_PREREG_090_20261121
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), współwłaściciel GAP-005, właściciel T2
created_at: 2026-11-21
document_type: PREREGISTRATION (zamrożona przed produkcyjnymi przebiegami MC i natywnymi; pilot ujawniony w §1)
authorization: Moderator 21 XI 22:59 (dosłownie): „Tak, przygotuj i przeprowadz” — odpowiedź na pytanie o test tablic BBN generowanych współczesnymi PYTHIA 8.3 i Herwig 7.3
follows: REVIEW_086 r4 (Nash-iw-research@65ab08a), REVIEW_089
claim_ceiling: NUMERYCZNY w modelach [▷] / NO_PBH_BOUND / NO_PAPER_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_090: tablice BBN hadronów ze współczesnych PYTHIA 8.3 i Herwig 7.3: czy wynik GAP-005 to systematyka generatora, czy artefakt tablic BlackHawk?

## 0. Pytanie

GAP-005 (REVIEW_086) zmierzyło Δ = +0.33…+0.37 dex między tablicami BBN BlackHawk v2.3 HERWIG i PYTHIA. Mechanicznie dojrzała praca Jung i in. (PRD 2026) znajduje dla współczesnych PYTHIA 8.306 i Herwig 7.3.0 wpływ rzędu kilku procent.

- **Q1:** jaka jest różnica progu β, gdy obie tablice wygenerować od nowa współczesnymi generatorami według przepisu BlackHawk?
- **Q2:** czy współczesna PYTHIA odtwarza tablicę autorów (PYTHIA BlackHawk)?
- **Q3:** jak daleko tablica HERWIG BlackHawk jest od współczesnego Herwig?

## 1. Stan przed zamrożeniem (wejścia i pilot; ujawnione, bo informują predykcje)

**Środowisko:**

- PYTHIA 8.318 (PyPI `pythia8mc` 8.318.3).
- Herwig 7.3.0 i ThePEG 2.3.0 (conda-forge, build `h2aa1e36_2`).
- Zestawy PDF CT14lo i CT14nlo, potrzebne tylko do inicjalizacji repozytorium Herwig; w e⁺e⁻ PDF są wyłączone. Pobrane z lhapdfsets (CERN); SHA w runnerze.

**Przepis BlackHawk.** Skrypty z pakietu: `scripts/pythia_scripts/table_*.cc`, `scripts/herwig_scripts/*/LEP.in`.

- e⁺e⁻ przy √s = 2E.
- PYTHIA: ISR off, procesy per pierwotny:
  - Z*→qq̄ dla kwarków;
  - H→gg, ZZ, ττ dla g, Z, τ;
  - H (wszystkie rozpady) dla higgs;
  - WW;
  - tt̄.
- Herwig: MEee2gZ2qq, MEee2Higgs2SM (Gluon/All), MEee2VV (WW/ZZ), MEee2gZ2ll (Tau); e± NoPDF.
- Tablica podaje liczbę na pierwotny, czyli na zdarzenie / 2, z wyjątkiem higgs.
- Zbiór stabilny (τ > 1e-8 s): π±, K±, K0L, μ, n. W obu generatorach K0S i hiperony się rozpadają; sprawdzone na domyślnych flagach PYTHIA i w pilocie Herwig.

**Pilot (tylko uū, ≤ 300 zdarzeń, wybrane energie):**

- PYTHIA 8.318 z domyślnym leptonowym PDF daje przy wysokim √s „powrót radiacyjny” na Z i zaniżoną krotność.
- Z `PDF:lepton = off` odtwarza tablicę PYTHIA BlackHawk. π± na zdarzenie przy √s = 91/200/600/2k/6k/20k/200k GeV:

  | źródło | 91 | 200 | 600 | 2k | 6k | 20k | 200k |
  |---|---|---|---|---|---|---|---|
  | PYTHIA 8.318 | 16.3 | 22.9 | 36.3 | 53.4 | 75.8 | 122 | 237 |
  | BH PY | 16.4 | 22.4 | 34.5 | 53.2 | 77.9 | 116 | 235 |

  Dlatego w PYTHIA przyjmuję `PDF:lepton = off`. Fizycznie pierwotny o energii E nie ma powrotu radiacyjnego.
- Herwig 7.3 (NoPDF), π± przy √s = 200…200k:

  | źródło | 200 | 600 | 2k | 6k | 20k | 200k |
  |---|---|---|---|---|---|---|
  | Herwig 7.3 | 21.2 | 29.9 | 44.5 | 64.1 | 93.9 | 176 |
  | BH HER | 17.6 | 25.8 | 37.9 | 53.5 | 78.6 | 153 |

  K± i K0L z Herwig 7.3 są ~1.5–2 × wyższe niż w tablicy BH HER.

**Artefakt potoku BlackHawk (nowe, ścisłe [▷]).**

- Moje złożenie tablicy BlackHawk PYTHIA z widmami pierwotnymi BlackHawk daje dokładnie 1.025814 × sumy BlackHawk całkowane jak u autorów, stale we wszystkich wierszach i gatunkach. Dla HERWIG ten współczynnik wynosi 1.1395–1.1397.
- Wartości te to Δ/(e^Δ − 1)⁻¹ dla logarytmicznej siatki energii wtórnych: 500 przedziałów dla PY, 100 dla HER. BlackHawk zamienia liczby w przedziałach na gęstość różnicą w przód, a całka trapezowa w ln E′ autorów zaniża sumę.
- Skutek: 0.046 dex z różnicy wydajności HER/PY w GAP-005 to artefakt binowania. Tablica autorów (PY) jest zaniżona o 1.1%.

**Ograniczenia techniczne:**

- Procesy PYTHIA przez H przy `PDF:lepton = off` wymagają √s ≥ 200 GeV.
- MC startuje więc od E = 100 GeV dla g, H, τ, W, Z i od 200 GeV dla t; dla kwarków u, d, s, c, b od 25 GeV.
- Poniżej tych progów oraz dla fotonu, e i μ (znikoma produkcja hadronów) we wszystkich wariantach używana jest tablica BH PYTHIA, wspólna i jawna.
- Przy T_H ≥ 1 TeV udział E < 100 GeV jest ~1e-4.

## 2. MC (zamrożone: `mc_spec_090.py`)

- **Pierwotne:** 11 hadronowych (g, H, W, Z, τ, u, d, s, c, b, t).
- **Energie:** 25, 50, 100, 200, 400, 800, 1600, 3200, 6400, 12 800, 25 600, 51 200, 100 000 GeV (od progów z §1).
- **Liczba zdarzeń:** 2000 dla E ≤ 800, 1000 do 6400, 500 powyżej.
- **Ziarno:** 90001 + indeks pierwotnego.
- **Skrypty:** `mult_pythia_090.py` i `mult_herwig_090.py` liczą π±, K±, K0L, p, n na zdarzenie (średnia i błąd standardowy) oraz sprawdzają brak K0S i hiperonów i zachowanie energii.

## 3. Tablice (`fold_090.py`, `make_tables_090.py`)

- **Wzór:** S_h(M) = Σ_i ∫ dE Φ_i(E; M) n_{i→h}(E), gdzie Φ to widma pierwotne BlackHawk (ustawienia autorów, `primary_spectra_090.jl`).
- **Interpolacja n:** log-log między węzłami MC.
- **Konwencja:** tablica wariantu = S / 1.025814 × ħ, czyli konwencja potoku BlackHawk-PYTHIA autorów. Porównanie z tablicą autorów jest wtedy jabłka do jabłek, a w różnicy H73 − P83 czynnik się znosi.
- **Warianty:** P83 (PYTHIA 8.3), H73 (Herwig 7.3), BHc (kontrola rzadkiej siatki).
- **Bramki** (wiersze 0–28, 5 gatunków; STOP przy porażce):
  - G_FOLD: złożenie / sumy BlackHawk = 1.025814 ± 1e-3;
  - G_AUTHORS_UNITS ≤ 1e-6;
  - G_COARSE ≤ 1%;
  - G_STAT: błąd statystyczny MC ≤ 1%;
  - G_MC: komplet energii, zachowanie energii 1e-3, zbiór stabilny BBN.

## 4. Pomiar natywny i sieć

- j22 i j62, ramię orig (addytywność E5 wykazana w 085). Siatki jak HER orig w 085 (46 węzłów), plus bazy.
- Wywołania: 188 Julii (2 strumienie), 193 przebiegi sieci (metoda 083/085).
- Iniekcja przez kopię drzewa źródeł (V_TABLE: plik identyczny).
- Bramki jak w 088: V7, V2_EXACT ≤ 1e-6, V6, V_BASE ≤ 5e-4, V3 (zero sieci i baza = 083), V4/V5 na p22_1720 i p62_1940 ≤ 1%.
- Runner `run090.sh` z twardymi bramkami.

## 5. Estymandy i etykiety (`analysis_090.py`)

- **Estymandy:**
  - dmod = lb_H73 − lb_P83;
  - drepro = lb_P83 − lb_PYBH;
  - dhold = lb_HERBH − lb_H73;
  - dgenBH = lb_HERBH − lb_PYBH (z 085);
  - udział (dgenBH − dmod)/dgenBH.
- **Etykiety** (8 komórek: j × model × cel):
  - **LM:** max |dmod| < 0.10 → `MOD_SMALL`; ≥ 0.27 → `MOD_COMPARABLE`; w przeciwnym razie `MOD_INTERMEDIATE`. Do tego flaga rozdzielczości: max |dmod| ≥ 5 × max szumu pierwiastka.
  - **LR:** max |drepro| ≤ 0.05 → `AUTHORS_PY_REPRODUCED`.
  - **LS:** znak dmod.

## 6. Predykcje (poinformowane pilotem z §1)

- **P1:** `AUTHORS_PY_REPRODUCED`.
- **P2:** wszystkie 8 dmod ∈ (0, 0.25), czyli HERWIG nadal osłabia, ale wyraźnie mniej niż +0.33…+0.37.
- **P3:** wszystkie 8 dhold ≥ +0.10, czyli tablica BH HER jest słabsza od współczesnego Herwig.

## 7. Granice

- Domyślne strojenia (PYTHIA Monash, Herwig 7.3 default); jeden zestaw na generator, bez wariantów strojenia.
- „Higgs” jako pierwotny modelowany jak w BlackHawk: s-kanałowe H o masie 2E, w obu generatorach.
- Brak hadronizacji ponad 1e5 GeV; sufit wspólny dla wszystkich wariantów, por. REVIEW_089.
- Wkład hadronów od γ, e i μ wspólny (BH PY).
- Ramię E5 pominięte.
- Wynik numeryczny w modelach; nie jest granicą na PBH.
- Przed zamrożeniem przetestowałem budowę tablic na atrapie (wartości BH jako „MC”: P83 = autorzy do 0.04%) i analizę (dmod = dgenBH, drepro = 0).
