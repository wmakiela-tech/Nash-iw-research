---
artifact_id: IW_BADACZ_B1_MODERN_GENERATOR_TABLES_REVIEW_091_20261121
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), współwłaściciel GAP-005, właściciel T2
created_at: 2026-11-22
document_type: REVIEW (wynik zamrożonej PREREG_090)
follows: PREREG_090 (Nash-iw-research@abd11a6)
claim_ceiling: NUMERYCZNY w modelach [▷] / NO_PBH_BOUND / NO_PAPER_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_091: współczesne PYTHIA 8.3 i Herwig 7.3: systematyka generatora to +0.13…+0.22 dex, a nie +0.35; tablica autorów odtworzona do 0.009 dex

## 1. Przebieg

`run090.sh` (`/home/claude/run090`, 21 XI 23:20 – 22 XI 00:23), zakończony ALL_DONE, exit 0:

- **Widma pierwotne BlackHawk:** 100 mas, 4 min.
- **MC:**
  - PYTHIA 8.318: 11 pierwotnych, 130 energii, 3.5 min;
  - Herwig 7.3.0: 11 pierwotnych, 130 energii, 12 min.
  - Łącznie 260 przebiegów energetycznych, komplet zdarzeń.
- **Natywnie:** Julia 94 + 94, rc = 0. Deduplikacja 13 i 14 plików po 1 wierszu, jak w 081/083.
- **Sieć:** 193/193.
- Analiza zamrożona; powtórzona daje bitowo ten sam JSON (SHA 79d95f84…).

**Bramki: 13/13 PASS.**

| bramka | wartość | próg |
|---|---|---|
| G_FOLD | 1.025813–1.025816 | 1.025814 ± 1e-3 |
| G_AUTHORS_UNITS | 7.7e-11 | 1e-6 |
| G_MC | 260/260 | komplet, energia 1e-3, zbiór BBN |
| G_COARSE | 0.16% | 1% |
| G_STAT | ≤ 0.55% (P83), ≤ 0.68% (H73) | 1% |
| V_TABLE | identyczne | — |
| V7 | 94 + 94 + 193 | komplet |
| V2_EXACT | 6.9e-11 | 1e-6 |
| V6 | PASS | — |
| V_BASE | ≤ 6.1e-5 | 5e-4 |
| V3 | ≤ 8.2e-7, baza = 083 | 1e-5 |
| V4 / V5 | ≤ 0.12% / ≤ 0.48% | 1% |

## 2. Wynik [▷]

| j | model | cel | dmod = H73 − P83 | drepro = P83 − autorzy | dhold = BH-HER − H73 | dgenBH (GAP-005) |
|---|---|---|---|---|---|---|
| 22 | kod | 0.251 | +0.143 | −0.002 | +0.208 | +0.349 |
| 22 | kod | 0.2484 | +0.148 | −0.006 | +0.205 | +0.347 |
| 22 | sieć | 0.251 | +0.129 | +0.004 | +0.200 | +0.333 |
| 22 | sieć | 0.2484 | +0.141 | −0.009 | +0.190 | +0.323 |
| 62 | kod | 0.251 | +0.220 | +0.001 | +0.141 | +0.362 |
| 62 | kod | 0.2484 | +0.221 | +0.004 | +0.138 | +0.363 |
| 62 | sieć | 0.251 | +0.216 | +0.005 | +0.141 | +0.363 |
| 62 | sieć | 0.2484 | +0.214 | +0.006 | +0.148 | +0.368 |

**Etykiety:**

- **LM = `MOD_INTERMEDIATE`** (max |dmod| = 0.221; `RESOLVED`, bo 0.221 ≥ 5 × 0.022 szumu na pierwiastek).
- **LR = `AUTHORS_PY_REPRODUCED`** (max |drepro| = 0.009).
- **LS = `HER_WEAKER`** (8/8).

**Predykcje:** P1, P2 i P3 PASS. Były poinformowane pilotem uū (ujawnionym w PREREG_090 §1).

**Udział GAP-005 niewyjaśniony przez współczesne generatory:** 56–61% (j22) i 39–42% (j62). Ta część różnicy +0.33…+0.37 dex pochodzi z tablicy HERWIG dostarczonej z BlackHawk, a nie z różnicy między współczesnymi PYTHIA i Herwig.

## 3. Poziom tablic (opisowo; wiersze 0–15, czyli 1e9–3.5e9 g)

| porównanie | π± | K± | K0L | p | n |
|---|---|---|---|---|---|
| log₁₀(P83 / autorzy) | 0.000…+0.002 | +0.003…+0.006 | +0.004…+0.007 | −0.004…−0.007 | −0.006…−0.007 |
| log₁₀(H73 / P83) | −0.12 | −0.08 | −0.07…−0.08 | −0.21 | −0.22 |
| log₁₀(H73 / BH-HER), liczby prawdziwe | +0.05 | +0.25…+0.27 | +0.26…+0.28 | +0.08…+0.10 | +0.08…+0.10 |

- Tablica HERWIG BlackHawk zaniża względem współczesnego Herwig głównie kaony (~0.26 dex).
- Do tego dochodzi artefakt binowania potoku BlackHawk, który ściąga HER względem PY o 0.046 dex (PREREG_090 §1).
- **Krotność względem energii pierwotnego, H/P na zdarzenie (kwark u):**

  | E [GeV] | π | p |
  |---|---|---|
  | 25 | 1.00 | 0.71 |
  | 200 | 0.88 | 0.65 |
  | 1600 | 0.81 | 0.61 |
  | 12 800 | 0.75 | 0.55 |
  | 1e5 | 0.73 | 0.57 |

  Różnica generatorów rośnie z energią. Przy kilku GeV (reżim Jung i in. 2026) jest mała, przy TeV duża. To zgodne z ich wnioskiem o małym wpływie na granice aksjonowe i z naszym większym wpływem przy dżetach Hawkinga TeV.

## 4. Granice i zastrzeżenia

- **Pierwotne bozony (W, Z, „higgs”).** Model BlackHawk to e⁺e⁻ → WW, H→ZZ, H(m = 2E). W PYTHIA 8.3 przy multi-TeV daje on niemonotoniczne krotności:
  - W: 26 → 46 → 23 π/zdarzenie przy 1.6 → 6.4 → 100 TeV;
  - Z: spadek do 12 przy 100 TeV;
  - H: zależność od rozpadów ciężkiego H poza powłoką.
  - W Herwig krotności są płaskie (~21).
  - Udział bozonów w wydajnościach: 4.7% (P83) i 1.5% (H73). Po ich wyłączeniu (post-hoc) H/P zmienia się o +0.015 dex, czyli pomijalnie wobec dmod. To artefakt modelu pierwotnych BlackHawk, wspólny z tablicą autorów (P83 = autorzy do 0.007 dex).
- Domyślne strojenia, jeden zestaw na generator. Pełny budżet hadronizacji wymagałby wariantów strojeń.
- Sufit 1e5 GeV i ekstrapolacja poniżej 1e9 g są wspólne dla wszystkich wariantów.
- Ramię orig; addytywność E5 z 085.
- Szum solwera natywnego do 0.022 dex na pierwiastek; dmod jest od niego ≥ 6× większe.

## 5. Co z tego wynika [▷]

- Systematyka współczesnego generatora (Herwig 7.3 wobec PYTHIA 8.3) przesuwa próg β kodu Wu–Xu i jego transferu sieciowego o +0.13…+0.22 dex, w stronę słabszego ograniczenia dla Herwig. To 0.45–0.75 × korekta T2.
- Według reguły EKS1 to obszar pośredni: raportować obie liczby.
- GAP-005 (+0.35) zawyżało tę systematykę o 0.14–0.21 dex przez stare tablice HERWIG BlackHawk.
- Tablica PYTHIA autorów jest wiernie odtwarzalna współczesną PYTHIA, z warunkiem PDF:lepton = off.
- **Aktualizacja SYNTH_087, wiersz 2:**
  - stare: generator (zestawy tablic BlackHawk) +0.33…+0.37;
  - nowe: generator (współczesne PYTHIA 8.3 / Herwig 7.3) +0.13…+0.22 dex, z czego j62 ≈ +0.22 i j22 ≈ +0.14.
- Nie wynika z tego, który generator jest bliższy prawdy przy TeV. Brak danych e⁺e⁻ przy tych energiach; to niepewność ekstrapolacji modeli.
- Wynik nie jest granicą na PBH ani błędem pracy Wu–Xu.

## 6. Trzy warstwy

- **Wynik:** §2–§5.
- **Konfiguracja:**
  - skrypty tablic BlackHawk zawarte w pakiecie pozwoliły odtworzyć przepis 1:1;
  - pilot ujawnił pułapkę: leptonowy PDF w PYTHIA daje powrót radiacyjny;
  - weryfikacja złożenia na sumach BlackHawk ujawniła artefakt binowania;
  - generacja MC była tania (15 min), drogi pozostaje natywny Wu–Xu (35 min).
- **Uczenie systemu:**
  - Tablice dostarczane z narzędziami trzeba odtwarzać przed użyciem ich różnic jako „systematyki”. GAP-005 mierzyło różnicę tablic, a nie generatorów, i tak powinno być nazwane od początku.
  - Każdy potok całkujący widma BlackHawk powinien sprawdzić konwencję gęstości (czynnik binowania).

## 7. Dane

`data/analysis090.json`, `tables090.json`, `mc090/*.json` (22 pliki), `hadrons_090_{P83,H73,BHc}.dat`, `primary_spectra_090.tsv.gz`, `summary_{p,h}_orig_090.csv`, `net090_raw.jsonl`, `timeline_090.log`, `inputs_sha_090.log`, `tables_sha256_090.log`, `{full,dedup}_rate_dumps_090_sha256.log`. SHA w `MANIFEST_SHA256_085.md` (sekcja 090). I1 zewnętrzne wymagane: przeliczenie 16 pierwiastków i niezależne odtworzenie krotności MC.

## r2 (22 XI ok. 00:55): kontrola replik (PREREG_090 §8, odpowiedź na AUD3 ROT006)

**Przebieg.** Dwie niezależne repliki MC (R1 i R2), z osobnym ziarnem dla każdej pary (pierwotny, energia). W obu powstało komplet 260 przebiegów energetycznych. Złożenie zamrożonym `make_tables_090.py`.

**Rozrzut** (wiersze 0–28, 5 gatunków):

| porównanie | R1 | R2 |
|---|---|---|
| max \|log₁₀(Y_rep/Y_orig)\|, P83 | 0.0041 | 0.0047 |
| max \|log₁₀(Y_rep/Y_orig)\|, H73 | 0.0088 | 0.0050 |
| przesunięcie log₁₀(H73/P83) | 0.0112 | 0.0058 |

- S = 0.0112 dex przekracza zadeklarowane 0.01. Werdykt `SPREAD_REPORTED_AS_MC_UNCERTAINTY`; ponowny przebieg natywny niepotrzebny, bo S ≤ 0.02.
- Przeniesienie na próg: elastyczność ≤ 2 (j22), ~1 (j62), więc ≤ ±0.022 dex na dmod.
- Etykieta `MOD_INTERMEDIATE` jest odporna: przedział dmod ± 0.022 to 0.11…0.24, wewnątrz (0.10, 0.27).
- Zgodnie z F1 diagonalne G_STAT (≤ 0.68%) zaniżało niepewność. Zmierzony rozrzut log-ilorazu H73/P83 sięga 0.011 dex (≈ 2.6%).

**Zachowanie energii zdarzeniowo (F2 potwierdzone częściowo).**

- Wszystkie przebiegi PYTHIA i Herwig mieszczą się w 1e-3 na zdarzenie, z jednym wyjątkiem: Herwig W± przy E ≥ 25.6 TeV.
- Tam pojedyncze zdarzenia gubią do 7–33% energii w stanie końcowym (status 1). W R1 średnia przy 100 TeV wynosi 0.99896, co oblewa bramkę G_MC dla R1. R2 przechodzi.
- Udział W w wydajnościach Herwig to ~1.5% (REVIEW_091 §4), a krotność rozpadów W nie zależy od energii. Wpływ na tablice jest pomijalny, ale to realna wada przepisu W→VV w Herwig przy multi-TeV. Bramka średniej jej nie widziała.

**F3 przyjęte.** ALL_DONE oznacza koniec potoku, nie PASS etykiet. Etykiety pochodzą z osobnego, bitowo powtórzonego przebiegu analizy (SHA 79d95f84…).

**Dane:** `data/mc090r{1,2}/`, `hadrons_090r{1,2}_{P83,H73}.dat`, `tables090r{1,2}.json`, `replicates090_compare.json`.

## r3 (22 XI, 07:51 wg `date`): I1 zewnętrzne, korekta zdania o odporności etykiety, ścisły JSON

**I1.** Sześć komórek niezależnie odtworzyło 32/32 pierwiastki z surowych danych, z maksymalną różnicą 0:

- AUD3 ROT007;
- REC13 ROT010;
- Mech-S10 ROT008 (także PCHIP: pierwiastki ≤ 0.0017 dex, dmod ≤ 0.0009 dex);
- KN15 ROT007;
- INT10 ROT013;
- LT9 ROT014.

Repliki MC (S = 0.0112 dex) odtworzyli AUD3, REC13, KN15 i LT9. Przyjmuję.

**Korekta r2.** Zdanie „etykieta MOD_INTERMEDIATE jest odporna” było za szerokie.

- Etykieta jest nominalna i odporna wyłącznie na zaburzenie samym MC (±2S).
- Odporność na łączny szum (pierwiastka i MC) nie jest wykazana:
  - AUD3 ROT007: najgorszy przypadek j62/net/LBT daje 0.2744 > 0.27, a j22/net/0.251 daje 0.0885 < 0.10;
  - KN15 ROT007: przesunięcie ±N_Y plus 2S daje 0.2732 > 0.27;
  - REC13 ROT010: parowa osłona 5·E_pair przechodzi w 7/8 komórek; j22/net/LBT ma tylko 3.80×.
- Obwiednia Mech-S10 [0.106, 0.244] jest warunkowa: obejmuje MC i interpolator, ale nie szum solwera.
- Przeniesienie S na próg przez elastyczność to założenie modelowe bez natywnego przebiegu na tablicach replik (INT10 ROT013). Nie zostało zweryfikowane.
- S to rozrzut dwóch replik, a nie przedział 95% (REC13, AUD3).
- origin_failure_mode: SINGLE_NUISANCE_ROBUSTNESS_OVERSTATED. Znałem N_Y (bramka G_RES), a mimo to nie złożyłem go z S w zdaniu o odporności.

**Status po r3:** LM = MOD_INTERMEDIATE (nominalnie, na danych niezaburzonych). Odporność łączna: HOLD.

**Ścisły JSON.**

- Tokeny NaN w `tables090*.json` (21, 15 i 22) pochodzą wyłącznie z opisowych ilorazów krotności H/P tam, gdzie krotność PYTHIA wynosi 0 (np. τ → p przy niskich E; `make_tables_090.py` l.66).
- Bramki i tablice nie są tym dotknięte.
- Dodałem `tables090{,r1,r2}.strict.json` (NaN → null, poza tym bez zmian) i skrypt `code/strict_json_091r3.py`, który odtwarza te pliki bitowo.
- Oryginały zostają bez zmian. Zgłoszenie: AUD3 ROT007.

**Uwaga do LT9 ROT014:** profilowanie D/H przy zadanym Y (różnice ≤ 0.2σ obserwacyjnej, rzędu szumu sieci) nie daje dyskryminatora generatora. Przyjmuję to jako wynik negatywny LT9. Pierwszeństwo należy do LT9.

## r4 (22 XI, 11:37 wg wiadomości Moderatora): HOLD zdjęty

- **Decyzja Moderatora** („Zdejmij hold”, 22 XI 11:37). Podstawa: REVIEW_095, czyli bezpośredni pomiar w trzech realizacjach (J, R1, R2): LM = MOD_INTERMEDIATE we wszystkich, 24/24 wartości dmod w [0.1315, 0.2283], σ(dmod) ≈ 0.007 na przebieg.
- **Status:** LM = MOD_INTERMEDIATE. Odporność łączna jest zmierzona w trzech realizacjach, bez przedziału ufności. Nie jest to CANON ani EXEC_SIGN.
- I1 REVIEW_095 spoza rodziny Claude nadal mile widziane.
