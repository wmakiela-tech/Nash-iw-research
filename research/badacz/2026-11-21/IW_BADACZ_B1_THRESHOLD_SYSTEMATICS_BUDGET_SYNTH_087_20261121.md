---
artifact_id: IW_BADACZ_B1_THRESHOLD_SYSTEMATICS_BUDGET_SYNTH_087_20261121
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), współwłaściciel natywny B1, właściciel T2
created_at: 2026-11-21
document_type: SYNTEZA etapu (budżet osi systematycznych progu β) + diagnostyka tablicowa E4 (opisowa, post-hoc)
follows: REVIEW_086 (Nash-iw-research@66be234)
integrates: REVIEW_071, REVIEW_082, REVIEW_084, REVIEW_086 (Badacz); LT9 ROT010 (metoda przesunięcia bazy, tu przeliczona na danych publicznych); EKS1-GAP-005; G1_FREEZE_PROPOSAL_068; Mech-S9 ROT031
claim_ceiling: NUMERYCZNY w modelach / opisowy [▷]; E4 = OSZACOWANIE tablicowe, nie pomiar progu / NO_PBH_BOUND / NO_PAPER_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# SYNTH_087: budżet osi systematycznych progu β Wu–Xu dla j22 i j62 po GAP-005

## 0. Po co

GAP-005 zamyka etap B1. Zbieram w jednej tabeli wszystko, co zmierzono dla progu β przy j22 (1.12e9 g) i j62 (3.49e9 g), żeby było widać trzy rzeczy: co dominuje, które twierdzenie jest odporne i co mierzyć dalej. Liczby z wcześniejszych artefaktów są przepisane, a nie przeliczone, z dwoma wyjątkami: wiersz 4 (przesunięcie bazy) i wiersz 7 (E4) liczy `code/budget_087.py` na danych publicznych.

## 1. Tabela (dex w log₁₀β; znak + oznacza słabsze ograniczenie)

| # | oś | j22 @0.251 | j22 @LBT | j62 @0.251 | j62 @LBT | źródło | status |
|---|---|---|---|---|---|---|---|
| 1 | korekta T2/E5, D (code / net) | +0.279 / +0.278 | +0.283 / +0.265 | +0.297 / +0.298 | +0.297 / +0.298 | 084, 086 | zmierzone |
| 2 | generator: HERWIG − PYTHIA (net, orig) | +0.333 | +0.323 | +0.363 | +0.368 | 086 | zmierzone (2 zestawy tablic BlackHawk) |
| 3 | transfer do pełnej sieci, T_orig | −0.486 | −0.590 | −0.097 | −0.298 | 084 | zmierzone (transfer szybkości, PRyMordial) |
| 3a | z tego luka bazowa (post-hoc) | −0.313 | −0.428 | −0.186 | −0.379 | 084 §4 | opisowe |
| 3b | z tego odpowiedź (post-hoc) | −0.173 | −0.162 | +0.090 | +0.081 | 084 §4 | opisowe |
| 4 | baza sieci ±0.0005 (ilustracyjnie, nie σ), rozpiętość lb_net_orig | 0.139 | 0.321 | 0.106 | 0.294 | metoda LT9 ROT010; tu przeliczone | opisowe |
| 5 | tolerancja solwera natywnego (domyślna → 1e-4), dryf korzenia orig | +0.023 | — | −0.003 | — | 071 | zmierzone tylko przy 0.251, kod |
| 6 | szum solwera natywnego na pierwiastek (N_Y / nachylenie) | ≤ 0.005 | ≤ 0.010 | ≤ 0.003 | ≤ 0.009 | 086 | zmierzone |
| 7 | domena tablicy < 1e9 g (E4), trend bez ucięcia | ≈ −0.03 | ≈ −0.03 | ≈ −0.005 | ≈ −0.005 | §3 niżej | OSZACOWANIE |
| 8 | sieć niezależna od PRyMordial, tło PBH w sieci, hadro- i fotodysocjacja, kowariancja teoria/obserwacja, warianty strojenia generatorów | ? | ? | ? | ? | — | niezmierzone |

Przesunięcie bazy ±0.0005 (wiersz 4) ruszyło D_net o ≤ 0.012 dex i Δ_gen o ≤ 0.014 dex we wszystkich komórkach. Rozpiętość 0.321 dex dla j22 przy LBT zgadza się z liczbą LT9 ROT010 (0.3213); arytmetyka jest wspólna, pierwszeństwo należy do LT9.

## 2. Co jest odporne, a co nie [▷]

- **Odporne (twierdzenie względne):** korekta T2/E5 przesuwa próg o +0.27…+0.30 dex. Jest:
  - addytywna względem generatora (|I| ≤ 0.016, w granicy szumu ~0.02);
  - przenaszalna do pełnej sieci (|D_net − D_code| ≤ 0.02, zgodne z zerem w szumie natywnym);
  - stabilna pod przesunięciem bazy ±0.0005 (≤ 0.012);
  - stabilna pod tolerancją (≤ 0.003, REVIEW_071).
- **Nieodporne (położenie bezwzględne progu):**
  - wybór generatora przesuwa próg o +0.33…+0.37;
  - przejście do pełnej sieci z jej bazą o −0.10…−0.59;
  - przy LBT sama baza sieci ±0.0005 to ±0.15 dex.
  - Żadne twierdzenie o bezwzględnej granicy β nie jest uprawnione, ani „Wu–Xu za silne o X”, ani „za słabe o Y”.
- **Konsekwencja redakcyjna:** jedyna liczba B1 gotowa do wyjścia poza projekt (po I1 i ocenie nowości) to zdanie względne o D wraz z jego granicami. Musi mu towarzyszyć zdanie o generatorze i o sieci, w tym samym miejscu.

## 3. E4: domena tablicy poniżej 1e9 g (diagnostyka tablicowa, bez przebiegu progu)

- **Fakt kodu.** Tablica autorów zaczyna się od 1e9 g. Poniżej kod ekstrapoluje liniowo w (log m, log Y) z wierszy 0–1, z nachyleniem −1.20 dla π.
- **Waga emisji.** Przy dN/dt ∝ m^−1.2 i dt ∝ m² dm ułamek hadronów emitowanych poniżej m* wynosi (m*/m₀)^1.8:
  - dla j22: 81% poniżej 1e9 g i 23% poniżej 5e8 g;
  - dla j62: 10.5% poniżej 1e9 g.
  - Próg j22 zależy więc głównie od ekstrapolacji autorów.
- **Bezpośrednie wiersze BlackHawk** (PYTHIA-BBN, ustawienia autorów, 11 mas 1e8–1e9 g, `data/hadrons_087_PY_rows_1e8_1e9.dat`, 37 s) w porównaniu z ekstrapolacją, log₁₀:

  | m [g] | log₁₀(bezpośrednie/ekstrapolacja) |
  |---|---|
  | 7.9e8 | −0.014 |
  | 6.3e8 | −0.073 |
  | 5.0e8 | −0.209 |
  | 4.0e8 | −0.421 |
  | 2.0e8 | −1.21 |
  | 1.0e8 | −2.04 |

  To artefakt sufitu E_prim ≤ 1e5 GeV (Wu–Xu sami go zauważają). Przy T_H ≥ 10 TeV coraz większa część pierwotnych wypada ponad sufit i daje zero hadronów. Bezpośrednie wiersze są więc ścisłym dolnym ograniczeniem, nie lepszym modelem.
- **Nachylenie lokalne tablicy autorów:**

  | wiersz | T_H [TeV] | nachylenie |
  |---|---|---|
  | 0 | 10.6 | −1.200 |
  | 1 | | −1.239 |
  | 2 | | −1.266 |
  | 3 | | −1.281 |
  | 5–10 | 7.0–4.6 | −1.295…−1.302 |
  | 20 | 2.0 | −1.311 |

  Spłaszczenie przy wierszach 0–3 to ten sam sufit. Wiersz 0 jest sam ucięty o ok. −0.008 dex (oszacowanie z kontynuacji wierszy 5–10).
- **Oszacowanie [▷].** Kontynuacja bez ucięcia (nachylenie ≈ −1.30) daje wydajności wyższe od ekstrapolacji autorów o ≈ 0.01 dex przy 1e9 g, ≈ 0.04 przy 5e8 i ≈ 0.08 przy 2e8.
  - Ważone emisją j22 to ok. +0.02…+0.03 dex w wydajnościach.
  - Czułość j22 z GAP-005 to ok. −1.1 dex progu na 1 dex wydajności (HER: −0.22…−0.38 dex wydajności → +0.35 dex progu).
  - Wynik: **≈ −0.03 dex dla j22 i ≈ −0.005 dla j62.** Ekstrapolacja autorów jest więc lepszym z dwóch dostępnych wyborów, a jej błąd jest mały na tle wierszy 1–3.
- **Status:** oszacowanie, nie pomiar. Pomiar to tani przebieg natywny j22 z tablicą rozszerzoną poniżej 1e9 g wierszami „trend bez ucięcia” zamiast ekstrapolacji autorów, z kontrolą „bezpośrednie (ucięte)” jako dolnym nawiasem. Proponuję go poniżej jako P3.

## 4. Kolejność dalszych pomiarów (propozycja)

- **P1. Sieć niezależna od PRyMordial**, zadanie PRF14 (LINX). Dotyka największej osi, wierszy 3 i 4, przy j22 do 0.6 dex.
- **P2. Fizyczna niepewność bazy sieci** w miejsce ilustracyjnego ±0.0005: τ_n, η, kompilacje szybkości jądrowych, poprawki słabe w PRyMordial. Mogę to zrobić sam na istniejących szybkościach 083/085 bez nowej Julii (sama sieć, ok. 15 min na wariant).
- **P3. E4 natywnie dla j22**, jak w §3. Tanie, ok. 20 min. Zamieni oszacowanie ≈ −0.03 w pomiar.
- **P4. Tło PBH w sieci** (rozszerzanie i grzanie), dziś poza transferem szybkości. Właściciel do ustalenia.
- **I1 zewnętrzne** dla REVIEW_078–086 i niezależna weryfikacja tablic HERWIG (Mech-S10) wciąż otwarte.

## 5. Zastrzeżenia

- To synteza wyników jednej komórki (Claude) plus jedna przeliczona metoda LT9. Nie jest zewnętrznym audytem.
- Wiersze 3a, 3b, 4 i 7 są opisowe albo szacunkowe. Wiersz 4 nie jest niepewnością statystyczną.
- Liczby wierszy 1–3, 5 i 6 pochodzą z zamrożonych analiz, wiersza 4 z `code/budget_087.py` (`data/budget087.json`).

## r2 (21 XI ok. 22:41): wiersz 7 zmierzony dla j22

REVIEW_089 (PREREG_088) dało E4_C = −0.05…−0.08 dex dla j22 (kod i sieć, oba cele; `E4_INTERMEDIATE`), a nie ≈ −0.03 jak w oszacowaniu z §3. Oszacowanie ważone liczbą hadronów zaniżało wpływ późnej emisji. Dolny nawias, czyli bezpośrednie wiersze BlackHawk ucięte sufitem, wynosi +0.37…+0.59 dex. Dla j62 wiersz 7 pozostaje oszacowaniem (≈ −0.01).

## r3 (22 XI ok. 00:30): wiersz 2 zaktualizowany (REVIEW_091)

Generator mierzony współczesnymi PYTHIA 8.318 i Herwig 7.3.0, według przepisu tablic BlackHawk, daje +0.13…+0.15 dex dla j22 i +0.21…+0.22 dex dla j62 (kod i sieć, oba cele; `MOD_INTERMEDIATE`, HERWIG słabszy). To miejsce +0.33…+0.37 z GAP-005. Różnica 0.14–0.21 dex wynika z tablicy HERWIG dostarczonej z BlackHawk (w tym 0.046 dex w wydajnościach to artefakt binowania). Tablica autorów (PYTHIA) odtworzona do 0.009 dex.
