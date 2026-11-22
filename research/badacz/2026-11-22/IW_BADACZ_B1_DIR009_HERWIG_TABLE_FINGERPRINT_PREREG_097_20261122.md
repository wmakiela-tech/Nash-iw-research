---
artifact_id: IW_BADACZ_B1_DIR009_HERWIG_TABLE_FINGERPRINT_PREREG_097_20261122
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude); EKS1-DIR-009, krok 1, działaniem własnym
created_at: 2026-11-22
document_type: PREREGISTRATION (zamrożona przed przebiegami produkcyjnymi)
authorization: Moderator 22 XI 11:36 („nie pytamy autorów; wiedzę uzyskujemy samodzielnie, w szczególności przez analizę innej literatury i samodzielne działania”); stała autoryzacja przebiegów 21 XI 16:05
claim_ceiling: DEFINICYJNY (kod) / NUMERYCZNY [▷] / NO_NOVELTY_ESTABLISHED / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_097: odcisk tablic HERWIG z BlackHawk v2.3: konwencja √s i wersja Herwig

## 1. Ustalenia przed preregistracją (jawnie: widziane przed zamrożeniem)

**Kod.**

- `scripts/herwig_scripts/*/main.cpp` zastępuje `%` w `LEP.in` wartością `initial_energies[i]` (E′). W efekcie zapisuje `LuminosityFunction:Energy = E′`. W Herwig ta wielkość to √s: nasze przebiegi 090 z Energy = 2E dają ⟨E_final⟩ = Energy.
- `formatting.c` dzieli liczby zliczeń przez 2, czyli „na pierwotny”, i podpisuje wiersz energią E′.
- Manual (arXiv:1905.04268, B.3) definiuje E′ jako połowę √s.
- Jeśli tablice powstały zgodnie z tym skryptem, wiersz E′ odpowiada pierwotnym o energii E′/2.

**Dane tablic.**

- Najwyższy niezerowy węzeł energii π± leży konsekwentnie tuż przy E′/2: 12.9 przy E′ = 25, 774 przy 1649, 4.64e4 przy 1e5 (plus pojedyncze zdarzenie 5e−6 w węźle 5.99e4).
- Wpisy tablic to liczby zliczeń na przedział: suma × 2 daje krotności zdarzeniowe. Odczyt jako gęstość daje wartości bez sensu.

**Opisowe porównanie z danymi 090 (H73 przy √s = 2E):**

| odczyt | BH-HER/H73 dla π | dla K± |
|---|---|---|
| BH(E′ = E), czyli odczyt nominalny | 0.79–0.87 | 0.48–0.72 |
| BH(E′ = 2E) | 1.02–1.08 | 0.93 → 0.61, spada z energią |

**Archiwum nie jest spójne:**

- `formatting.c` mapuje przedziały histogramu ln(E/E_wiązki) ∈ [−10, 0] indeksem na absolutną siatkę 1e−6–1e5 GeV. Tymczasem tablice mają fizyczną oś energii.
- Analiza Rivet rezerwuje 12 gatunków (z π⁰), a `formatting.c` czyta 11.
- Archiwalny zestaw skryptów nie jest więc w całości tym, którym wygenerowano tablice. Wniosek o √s opieram na danych (punkt końcowy, krotności), a kod tylko go wspiera.

**Literatura.**

- Herwig 7.2 (arXiv:1912.06509, XII 2019) wprowadził zmiany produkcji dziwności i nowe strojenie hadronizacji.
- Tablice HERWIG opisuje już manual v1.0 (V 2019).
- Doniesienia o √s = E′ w tablicach BlackHawk nie znalazłem. To nie znaczy, że go nie ma; sprawdzenie należy do XH-S7.

## 2. Przebiegi (`run097.sh`, `mult_herwig_097.py`)

- Pierwotny: kwark u, przepis `LEP.in` BlackHawk (e⁺e⁻ → uū, bez ISR).
- 6 węzłów tablicy: indeksy 0, 20, 40, 60, 80, 99, czyli 25–1e5 GeV. 2000 zdarzeń na węzeł.
- Ramiona:

| ramię | generator | √s |
|---|---|---|
| H72_f1 | Herwig 7.2.0 | E′ |
| H73_f1 | Herwig 7.3.0 | E′ |
| H73_f2 | Herwig 7.3.0 | 2E′ |

Domyślne strojenia, conda-forge. Pilot z Herwig 7.2 przy 25 GeV (300 zdarzeń) potwierdził działanie i domknięcie energii.

## 3. Analiza (`analysis_097.py`)

- **Miara:** L = log₁₀(N_BH/N_MC) dla π±, K±, K0L, p i n.
- **Bramki:**
  - G_MC: rc = 0, ⟨E_final/√s⟩ w 1e−3;
  - G_NODES: energie MC = węzły tablicy z dokładnością 1e−5.
- **Etykieta L_SQRTS:** `SQRTS_EQ_E`, jeśli max|L_π| dla H73_f1 jest mniejsze niż dla H73_f2 i nie większe niż 0.04. Symetrycznie `SQRTS_EQ_2E`, w przeciwnym razie `UNRESOLVED`.
- **Etykieta L_VER:**
  - `MATCH_v`, jeśli wszystkie 30 wartości |L| ≤ 0.04 dla wersji v;
  - `NO_MATCH_PRE_72_CANDIDATE`, jeśli obie wersje chybiają, a L_K spada o co najmniej 0.10 dex od najniższego do najwyższego węzła;
  - w pozostałych przypadkach `NO_MATCH`.
- Analizę sprawdziłem na atrapie.

## 4. Predykcje (moje, zamrożone)

- **Pr1:** `SQRTS_EQ_E`. To nie jest predykcja ślepa, bo dane opisowe z §1 już ją sugerują. Test dodaje porównanie jabłka do jabłek w tych samych węzłach.
- **Pr2:** `NO_MATCH_PRE_72_CANDIDATE`. Uzasadnienie: tablice istnieją od V 2019, czyli przed 7.2.

## 5. Granice

- Odcisk dotyczy tylko kwarku u.
- Herwig 7.0 i 7.1 nie są dostępne w conda. Gdyby wyszło `PRE_72_CANDIDATE`, następnym krokiem jest budowa 7.1 ze źródeł (hepforge jest osiągalny).
- Wynik nie jest jeszcze oceną wpływu na próg PBH. Ten wymaga osobnego przebiegu natywnego z tablicą BH-HER o poprawionej osi energii.
