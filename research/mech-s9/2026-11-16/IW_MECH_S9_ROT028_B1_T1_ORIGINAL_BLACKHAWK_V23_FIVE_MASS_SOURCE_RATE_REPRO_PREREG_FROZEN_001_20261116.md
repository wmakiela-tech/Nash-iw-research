---
artifact_id: IW_MECH_S9_ROT028_B1_T1_ORIGINAL_BLACKHAWK_V23_FIVE_MASS_SOURCE_RATE_REPRO_PREREG_FROZEN_001_20261116
created_at: 2026-11-16
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
status: PREREG_FROZEN_BEFORE_T1_RUN
exposure: PUBLIC
scope: MODERATOR_APPROVED_T1_ONLY
approval_reference: https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1794844111499439
bridge_issue: https://github.com/wmakiela-tech/Nash-iw-research/issues/16
claim_ceiling: ORIGINAL_SOURCE_TABLE_REPRODUCTION_ONLY / NO_10D_JULIA / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# Mech-S9 ROT028 / B1 — zamrożona prerejestracja T1 (przed eksperymentem)

## 0. Uprawnienie, właściciel, firstness

Moderator 2026-11-16 16:47 CET zatwierdził T1 i T2 równolegle (przekaz Badacza: https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1794844111499439).
**T1 przyjmuje Mech-S9**: jedno odtworzenie oryginalnych pięciu szybkości hadronowych z dokładnego BlackHawk v2.3, nakładki Wu–Xu i oryginalnych parametrów notebooka, dla **pięciu z góry wybranych mas**, po którym wolno ocenić tylko source-typed bramkę T1. T2 wykonuje wyłącznie Badacz; Mech-S9 nie wykonuje nowej Julii.

Oryginalne prace i kod: Arbey–Auffinger (BlackHawk), Wu–Xu (BBN 10D i kod producenta). Pierwsze testy E5/E5b i pilota PYTHIA należą do Badacza, pierwsze pobranie oryginalnego v2.3 z pełnym SHA do MT14, pierwszy rozpakowany bezpośredni odczyt źródeł v2.3 w projekcie do Mech ROT025. Nie ma claimu nowości naukowej.

**Chronologia:** niniejsze prereg i jawne etykiety zapisane do GitHub **przed uruchomieniem T1**. Niedozwolone dopasowywanie mas, progu zgodności lub wybór wariantu tablic po obejrzeniu wyników.

## 1. Nieruchome źródła

- Oryginalny BlackHawk **v2.3 TAR** 161495983 bajty, SHA256 `dd148349304c158ed3509ea6935f2fd3d60ebe7cda4c34598aa99ea329c129a7`, URL `https://blackhawk.hepforge.org/downloader?f=blackhawk_v2.3.tar.bz2`, dokładnie według `Artifacts.toml` Wu–Xu blob `324cb54a6d2d1beca970931534345f589eb68c56`. Fail closed jeśli bajty lub SHA niezgodne.
- Autor Wu–Xu commit `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`; konkretne oryginalne nakładki `arXiv-2509.05618/external_code/BlackHawk_v2.3-hack/BlackHawk_inst.c` Git blob `f517b0a71a3c994e396600ce73cb9658e440d646`, `BlackHawk_tot.c` blob `76758e05a71688b94979b326723d02dbdf630dc5`, `src/include.h` blob `3a1eaefd6d884c864056ea45233513493794ee7e`. Dokładna metoda `prepare_BlackHawk()`: kopiuj orig tar, nakładaj te trzy pliki i wykonaj `make BlackHawk_inst.c BlackHawk_tot.c` przed budowaniem wywoływalnego `BlackHawk_inst.x`. Zachować logi kompilacji, selektor `HARDTABLES`, aktywne tablice/nagłówki i sumy SHA.
- Notebook oryginału `valid_hadrons_from_BlackHawk.ipynb` blob `8a10396ae771b17059808fc2b91235dd194cba8d`, wrapper `tool_script-BlackHawk_extension.jl` blob `16c5cb6f87dcd2e2b416b6664d3bdcb3c3c68818`; referencyjne `data/out/hadrons_from_PBH.dat` blob `06d0883a27b108692720422294ba2baacd381a64`.
- Oryginalne źródła statystyk BlackHawk C: `scripts/pythia_scripts/table_up.cc` SHA256 `262c78fc41eb8440cc123329152eabade64bd0b9b35e80f063185f1c005667b6`, `scripts/pythia_scripts/formatting.c` SHA256 `0baa942a9acfac2990f1ac03fc4f8eb56273ff8a7f922177368e4c8e6eb1d33e`. Oryginalne v2.3 PYTHIA BBN `current` i `old/` różnią się liczbowo (ROT027: 179379/625005 wierszy), więc **HARDTABLES i wybór binarnego kernela muszą być jawne**.

## 2. Pięć mas zamrożonych bez wglądu w wynik T1

**Indeksy 0-based `[0,22,49,74,99]`** w 100-wierszowej tabeli Wu–Xu; masa z tabeli przyjmowana jest jako referencyjna i kontrolowana względem wzoru `M_j=10^9(4000)^{j/99}` g. Kryterium zgodności mas przy przeliczeniu original natural unit `m[GeV]`: względny błąd `<=1e-12`, inaczej `T1-NOREPRO` / `HOLD_SOURCE` bez wyników wyjściowych.

Dokładne ustawienia oryginalnego producenta **dla każdego z tych pięciu**: `BH_number=1`, `metric=0`, `spectrum_choice=0` (monomasa), `param_number=1`, `amin=0`, `primary_only=0`, `hadronization_choice=0` (PYTHIA BBN), `Emin=5 GeV`, `Emax=1e5 GeV`, `E_number=100`, `add_DM=0` i inne zgodnie z oryginalnym konstruktorem `BlackHawkParameters()`. Nie wybierać `HERWIG`, `PYTHIA(new)`, `HDMSpectra` ani `old/` ręcznie, dopóki oryginalna ścieżka wczytywania nie rozstrzygnie wariantu. Wykonać oryginalną funkcję `BlackHawk_inst.x`, nie 10D `main-scan.jl`.

**Oryginalny operator wyjściowy**: z `instantaneous_secondary_spectra.txt` odczytać 100 energii `E_i` i pięć kolumn `pipm, Kpm, K0L, proton, neutron` w układzie źródłowym; dla każdej kolumny `f_i`:
`h = mean(log(E[i+1])-log(E[i]))`,
`R = h/2 * (2*sum(E_i*f_i) - (E_1*f_1 + E_last*f_last))`;
zgodnie dokładnie z komórką 12 oryginalnego notebooka. Konwersja `s^-1` na `GeV` jak w oryginalnym `EUval.(GeV, rate ./ NU.s)`; kod użyty do konwersji i stała muszą być źródłowo wykazane przed wydaniem PASS. Uwierzytelnić źródłową kolejność pięciu kolumn i każdą jednostkę. W razie nieweryfikowalnego operatora/jednostek stosować `T1-NOREPRO`, bez dopasowania posthoc.

## 3. Trzy werdykty zamrożone (PROPOSAL_068 §3)

Porównać **25 komórek** (5 mas × 5 kolumn) do oryginalnej tablicy Wu–Xu `hadrons_from_PBH.dat`. `K0L` jest neutralny i nie podlega połowieniu. Oryginalne grupowane ładowane kolumny: `pipm,Kpm,proton,neutron`. Nie przeskalować ich posthoc przed raportowaniem surowego wyniku.

- **T1-GROUPED**: wszystkie 25 zgadzają się względnie do `<=1e-5` z *pełnymi* obliczonymi szybkościami grupowymi: `max abs(R_model/R_author -1)<=1e-5`.
- **T1-PERSTATE**: `K0L` zgadza się bez zmian i wszystkie pozostałe 20 wartości zgadzają się po *podziale grupowego modelowego R przez 2*: `max abs((0.5*R_model)/R_author -1)<=1e-5` na 20, `abs(R_model/R_author -1)<=1e-5` na 5. (To rozstrzyga, czy tabela autorów ma pół grupy; nie udowadnia jeszcze symetrii każdego stanu).
- **T1-NOREPRO / B1-HOLD_SOURCE**: żadne z powyższych na wszystkich 25, brak aktywnego oryginalnego buildu/HARDTABLES, source replay fail, nieznany parser/jednostka, albo różnice danych, których nie da się źródłowo odróżnić. **Żadna selekcja częściowo udanych komórek nie podnosi do GROUPED/PERSTATE.**
- Jeżeli warianty mają identyczny wynik w granicach tolerancji tylko z powodu fizycznie zerowych rate, użyć `T1-NOREPRO` jako nierozstrzygający. Jeśli którakolwiek referencyjna szybkość zero/ujemna, zgłosić i stosować `T1-NOREPRO` zamiast sztucznego eps.

**Raport bezwzględny/porównawczy**: dla wszystkich 25 `M, R_author, R_reproduced, R_model/R_author`, per-channel maximum relative mismatch i maksimum globalne; SHA256 surowych outputów C, build log, original source/compiler, selected headers, JSON wynik, fail-controls. Nie zmieniać progu `1e-5` po zobaczeniu liczb. Obydwie hipotezy nie mogą naraz przejść dla dodatnich rzeczywistych wartości.

## 4. T1 granice interpretacji i bramka do Badacza

T1 jest **źródłową reprodukcją pięciu stawek** dla źródłowej grupowej tablicy BBN, nie niezależnym symulatorem reakcji BBN. Wyłącznie T1-GROUPED może być przesłanką do interpretacji T2 E5 według Q-B; brak T1/PERSTATE/NOREPRO blokuje podnoszenie wyników T2 do fizycznej korekty publikowanych konturów. Ponadto wymagany T3 (przegląd JCAP, erraty i starszej literatury) oraz I1 innej komórki. Źródło Wu–Xu `main-scan.jl` domyślny solver w jednym punkcie zbadany przez Badacza PREREG_066; wrażliwość A0/A1 przy 1e-5 w X pozostaje i uniemożliwia ogólny certyfikat błędu.

**NIE**: nie wykonujemy kolejnej Julii, nie rozszerzamy skanu mas, nie twierdzimy o nowości fizycznej ani błędzie artykułu, nie zmieniamy fizycznych równań lub źródeł, nie deklarujemy wyników BBN/PBH przed dodatkową recenzją.

## 5. Most online i rozstrzygnięcia

Rejestr B1: https://github.com/wmakiela-tech/Nash-iw-research/issues/16
Wątek Slack: https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1794844748245419

Mech-S9 publikuje `T1_PREREG_FROZEN` z linkiem do tego dokumentu, dopiero potem uruchamia jeden zatwierdzony source experiment. Badacz osobno publikuje `T2_PREREG_FROZEN` i stan T2, potwierdza `BADACZ_ACK_BRIDGE`. Żadne udostępnienie w Slack nie oznacza automatycznego odbioru przez drugą komórkę. Stop do 27 XI. Wszystkie nowe konfiguracje wymagają osobnej autoryzacji Moderatora.

Status: `MECH_S9_T1_PREREG_FROZEN / AUTHORIZATION_SCOPE_T1_ONLY / T1_NO_RUN_YET / NO_NEW_JULIA / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
