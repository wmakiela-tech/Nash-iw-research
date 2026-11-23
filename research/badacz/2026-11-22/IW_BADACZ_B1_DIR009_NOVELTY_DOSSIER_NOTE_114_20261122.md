---
artifact_id: IW_BADACZ_B1_DIR009_NOVELTY_DOSSIER_NOTE_114_20261122
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel DIR-009 (096–111)
created_at: 2026-11-22
document_type: NOTE (żywa teczka nowości; aktualizowana w kolejnych obrotach jako r2, r3, …)
authorization: Moderator 22 XI 20:30 („Czy jest to nowość wymaga pogłębienia tematu. Uwzględnij to w dalszych obrotach”)
claim_ceiling: PROWENIENCJA I PRZEGLĄD ŹRÓDEŁ / NO_NOVELTY_ESTABLISHED (decyzja Moderatora) / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# NOTE_114: teczka nowości DIR-009 (tablice HERWIG w BlackHawk). Stan po pierwszym obrocie: nie znalazłem doniesienia o T1; dwa otwarte tropy

## 1. Co dokładnie sprawdzam

Rozdzielam trzy tezy, bo każda może mieć inny status nowości.

- **T1 (etykieta √s).** Tablice HERWIG dla epoki BBN (`hadronization_choice = 1`) wygenerowano przy √s = E′: `scripts/herwig_scripts/*/main.cpp` ustawia `LuminosityFunction:Energy = E′`, a `formatting.c` podpisuje wiersz energią E′. Manual podaje E′ jako połowę √s, a BlackHawk używa wiersza E′ dla pierwotnej o energii E′. Każda pierwotna dostaje więc krotności pierwotnej o połowę lżejszej. Dowody: REVIEW_098 (skrypty, odcisk 7.3), REVIEW_106 (Herwig 7.1.5 przy √s = E′ do 0.0097 dex), REVIEW_110 (szew 10 kanałów: √s = E′ 0/48 FAIL, √s = 2E′ 30/43 FAIL), NOTE_111 (bez zmian w v3.0).
- **T2 (binowanie).** Tablice HERWIG mają 100 przedziałów energii końcowej, a PYTHIA 500. W potoku wydajności (BlackHawk i trapez autorów Wu–Xu) daje to czynnik 1.13957 zamiast 1.025814, czyli +0.0457 dex dla części HERWIG (REVIEW_100 r2). **Status otwarty:** nie ustaliłem jeszcze, czy to wada BlackHawk, czy sposobu, w jaki potok autorów całkuje wyjście BlackHawk (pozycja O6).
- **T3 (skutek).** W natywnym modelu Wu–Xu etykieta przesuwa próg β o ~−0.08 dex, a binowanie o ~−0.05 dex. Razem to 0.61–0.68 kontrastu „tablica HERWIG wobec H73” przy j22 i 0.84–0.90 przy j62 (REVIEW_110). Teza T3 zależy od T1 i T2 i od konkretnego modelu; nie jest tezą o fizycznej granicy PBH.

Nowość wymaga odjęcia stanu wiedzy na dwóch powierzchniach: literatura i dojrzałe narzędzia (poziom twierdzeń) oraz własny dorobek projektu. „Nie znalazłem” ≠ „nie istnieje”.

## 2. Powierzchnia projektu (stan na dziś)

- EKS1 ROT017: klasa wad konwencji wyjścia BlackHawk 2.3 jest znana w literaturze (arXiv:2506.13861, dodatek A: połowa strumienia w opcji HDM; PYTHIA „w parach” wobec HDM „na cząstkę”). To inna wada niż T1.
- REC13 ROT020: DIR-009 nie spełnia bramki nowości zewnętrznej z 21 XI 15:48; to odtwarzalne, wewnętrznie prawdopodobnie pierwsze odkrycie techniczne. EKS1 ROT023 to przyjął.
- REC13 ROT021: jedno opublikowane użycie HERWIG z BlackHawk (Thoss, Burkert, Kohri 2024, MNRAS 532, 451), bez potwierdzenia wersji i wyboru tablic.
- INT10 ROT017: tablica R2 autorów to hybryda energii pierwotnych z mieszaną konwencją binowania (związek z T2).

## 3. Powierzchnia literatury: dziennik wyszukiwań (obrót 1)

Narzędzia: WebSearch (tryb standard), alphaXiv (odczyt PDF), curl do blackhawk.hepforge.org.

| # | zapytanie lub źródło | wynik istotny dla T1/T2 |
|---|---|---|
| 1 | `BlackHawk HERWIG hadronization tables center-of-mass energy primary energy convention` | Manual (arXiv:1905.04268, dodatek B.3): tablice PYTHIA i HERWIG dla energii początkowych E′, „half of the center of mass energy”, HERWIG 25–1e5 GeV. Potwierdza deklarowaną konwencję; o rozbieżności nic. |
| 2 | `BlackHawk BBN hadronization tables HERWIG PYTHIA difference primordial black hole constraints` | Wu–Xu (arXiv:2509.05618) zwraca uwagę na „minor issue” tablic PYTHIA (`Emax_init = 1e5`). Brak doniesień o T1. |
| 3 | `"BlackHawk" "Herwig" hadronization tables bug OR error OR inconsistency` | nic o BlackHawk; wyniki o modelu klastrowym Herwig. |
| 4 | alphaXiv: arXiv:2509.05618v3 (Wu–Xu), §4.1 i dodatek C | Krytyka BlackHawk dotyczy wyłącznie PYTHIA: `Emax_init`, brak `PDF:lepton = off`, `mHatMin`, progi `mMin`. Konwencję E_CM/2 stosują poprawnie we własnym PYTHIA. O HERWIG ani o √s tablic HERWIG nic. Strony 4–8, 13–14 i 17–19 nie zostały zwrócone, ale sekcja hadronizacji i dodatek C tak. |
| 5 | alphaXiv: arXiv:2405.18493 (Boccia, Iocco, Visinelli) | Nie używa wstrzykiwania hadronów (tylko termiczne); nie dotyczy. |
| 6 | `"hadronization_choice" BlackHawk HERWIG BBN primordial black hole` | Manual (opis opcji 0/1/2), Wu–Xu, arXiv:2010.04797 (krytyka ekstrapolacji przy niskich energiach), arXiv:2108.02737 (v2.0). Brak T1. |
| 7 | `BlackHawk herwig_scripts LuminosityFunction:Energy main.cpp github` | Tylko źródła ThePEG i CMSSW; brak forków ani zgłoszeń dotyczących skryptów BlackHawk. |
| 8 | `primordial black holes BlackHawk "HERWIG tables" secondary spectra comparison PYTHIA tables difference` | arXiv:2201.01265 (Isatis: niepewność widm wtórnych rzędu wielkości między kodami), 2203.14979, 2110.03333 (HERWIG jako dostępna opcja). Brak T1. |
| 9 | blackhawk.hepforge.org: `bugs_corrected_v2.1.txt` (SHA-256 2f0092c2…) | 12 pozycji v2.0 → v2.1; żadna nie dotyczy energii ani etykiety tablic HERWIG. Ekstrapolacja tablic PYTHIA/HERWIG przy niskich energiach poprawiona. |
| 10 | README v3.0 (archiwum oficjalne), historia wersji | „V2.0 – 06/08/2021 – … Corrected PYTHIA tables.” Tablice HERWIG nie są wymienione w żadnej wersji. |
| 11 | `Auffinger review "Primordial black hole constraints with Hawking radiation" arXiv`, potem alphaXiv: arXiv:2206.02672v1 (przegląd autora BlackHawk) | HERWIG wymieniony jako narzędzie „at LHC energies (E ∼ GeV−TeV)”; brak porównania PYTHIA z HERWIG i brak uwag o konwencji energii tablic. Odczytane strony 1, 4, 17–18, 24, 26, 30, 34–35, 45, 62. |
| 12 | `Bauer Rodd Webber "Dark Matter Spectra from the Electroweak to the Planck Scale" arXiv HDMSpectra` | arXiv:2007.15001 (JHEP 06 (2021) 121). Według streszczenia i wstępu porównanie dotyczy Pythia 8.2, nie tablic BlackHawk; bez pełnego odczytu. Mała szansa na T1. |

**Ciekawostka bez wpływu na T1:** Wu–Xu (v3, maj 2026) piszą, że w PYTHIA BlackHawk brakuje `PDF:lepton = off`. Lista błędów v2.1 podaje, że tablice PYTHIA liczono z tym ustawieniem. Nie rozstrzygam tego.

## 4. Stan po obrocie 1

- **T1:** w przejrzanych źródłach (manual, lista błędów v2.1, historia wersji w README v3.0, artykuł v3.0, Wu–Xu, 2506.13861, 2010.04797, 2201.01265, 2108.02737, 2207.03266, przegląd Auffingera 2206.02672) brak doniesienia. Najbliższa wiedza sąsiednia: wady konwencji wyjścia BlackHawk (2506.13861) i wady przepisu PYTHIA (Wu–Xu) to ta sama klasa (konwencje i przepisy tablic hadronizacji BlackHawk), ale nie ten sam przypadek.
- **T2:** nieustalone (O6).
- **Wniosek roboczy [▷]:** T1 to nieopisany w znalezionej literaturze przypadek znanej klasy problemów. Rozstrzygnięcie o nowości należy do Moderatora i wymaga jeszcze pozycji O1–O5.

## 5. Plan na kolejne obroty (jedna pozycja na obrót, w tej kolejności)

- **O1. Archeologia wersji.** Archiwa v1.0–v2.2 z hepforge: czy tablice HERWIG zmieniły się kiedykolwiek od v1.0, i co zmieniło „Corrected PYTHIA tables” w v2.0. Jeśli tamta poprawka to przeetykietowanie √s w PYTHIA, autorzy znali klasę dla PYTHIA i pominęli HERWIG. Wstrzymane do zwolnienia miejsca na dysku po przebiegu 112.
- **O2. Użytkownicy `hadronization_choice = 1`.** Literatura cytująca BlackHawk z HERWIG (zaczynając od Thoss i in. 2024) oraz prace porównujące PYTHIA z HERWIG w BlackHawk, które przypisują różnicę fizyce generatora.
- **O3. Przegląd Auffingera** (arXiv:2206.02672): wykonane w obrocie 1 (wiersz 11), bez T1.
- **O4. HDMSpectra** (arXiv:2007.15001): wstępnie wiersz 12; pełny odczyt tylko wtedy, gdy O2 wskaże powiązanie z tablicami BlackHawk.
- **O5. Repozytoria:** forki BlackHawk na GitHub i zgłoszenia (issues) z frazami `herwig_tables`, `hadronization_choice`, `sqrt(s)`.
- **O6. Status T2:** czy czynnik binowania wynika z BlackHawk (zmiana konwencji gęstości między tablicami 100 i 500 przedziałów), czy z całkowania przez autorów Wu–Xu. Sprawdzenie w kodzie `hadro_herwig.c` i `secondary.c` oraz w potoku R2 (085).

Każdy obrót dopisuje do tej teczki sekcję rN z dokładnymi zapytaniami i lokatorami źródeł.

## r2 (22 XI, 21:40, godzina z `date` przy zapisie): O1 wykonane. Archeologia wersji v1.0–v3.0

**Metoda.** `code/bh_versions_herwig_114.py` dla każdego oficjalnego archiwum z blackhawk.hepforge.org (`downloader?f=blackhawk_vX.tar.bz2`) liczy SHA-256 archiwum. Porównuje bajtowo tablice HERWIG i PYTHIA dla epoki BBN z v2.3 (ścieżki `src/tables/herwig_tables/` w v1.x, `src/tables/hadronization_tables/…` od v2.0) oraz przepis `scripts/herwig_scripts/up/{LEP.in, main.cpp}`. Opisowo podaje też log10 stosunku krotności π± z kolumny „up” tablicy PYTHIA do v2.3. Archiwa czytałem jako dane i po przetworzeniu usuwałem (brak miejsca). Zapis: `data/bh_versions_114/v*.json`.

| wersja | SHA-256 archiwum | tablice HERWIG = v2.3 | linia energii w `up/LEP.in` | tablice PYTHIA wobec v2.3 |
|---|---|---|---|---|
| 1.0 | 29f6ba2e… | 11/11 | `…LuminosityFunction:Energy %` | inne; π± „up”: −0.014 (5 GeV), −0.098 (99 GeV), −0.268 (1 TeV), −0.431 dex (100 TeV) |
| 1.1 | fbec25a8… | 11/11 | to samo | jak 1.0 |
| 1.2 | 57878c67… | 11/11 | to samo | jak 1.0 |
| 2.0 | 29c15f97… | 11/11 | to samo | wszystkie 11 plików zawiera znaczniki konfliktu git (`<<<<<<< HEAD` … `=======` … `>>>>>>> f93dc41 (BlackHawk v2.0)`); blok HEAD = v2.3, drugi blok = stare tablice v1.x |
| 2.1 | 8ac4bf4d… | 11/11 | to samo | 11/11 identyczne |
| 2.2 | 6ae1149f… | 11/11 | to samo | 11/11 identyczne |
| 2.3 | dd148349… | odniesienie | to samo | odniesienie |
| 3.0 | c8bf4ccc… | 11/11 | to samo | 11/11 identyczne |

`main.cpp` wstawia w miejsce `%` energię początkową wiersza E′, więc √s = E′ we wszystkich wersjach (REVIEW_098). `up/main.cpp` z v1.x–v2.2 różni się od v2.3 tylko zakomentowaniem linii `system("rm */ -rf");` (diff v2.2 wobec v2.3; SHA-256 `up/main.cpp` jest ten sam w v1.0–v2.2, 36a37d16…, a w v2.3 i v3.0 7aa6ed8e…). `LEP.in` jest identyczny we wszystkich wersjach.

**Wnioski [▷]:**
- T1 dotyczy wszystkich publicznych wydań BlackHawk od v1.0 (maj 2019) do v3.0 (czerwiec 2026). Tablice HERWIG i przepis ich generacji nigdy się nie zmieniły.
- Tablice PYTHIA autorzy poprawili w v2.0 („Corrected PYTHIA tables”). Zmiana nie jest przeetykietowaniem √s: stare tablice v1.x mają krotności niższe o −0.01…−0.43 dex, a deficyt rośnie z energią. Tablic HERWIG nie ruszono. Klasa „problemy tablic hadronizacji BlackHawk” była więc autorom znana dla PYTHIA, ale przypadek HERWIG nie został zauważony (w dostępnych źródłach).
- Dla bramki REC14 ROT001 (Thoss i in. 2024 deklarują BlackHawk 2.1): tablice HERWIG w v2.1 są bajtowo identyczne z v2.3. Ogniwo `V21_SOURCE_BYTES` jest ustalone. Nadal nieustalone pozostają `ACTUAL_AUTHOR_RUNTIME_CONFIG` (czy użyli `hadronization_choice = 1`) i skutek fizyczny.
- Uboczne: wydanie v2.0 zawierało tablice PYTHIA ze znacznikami konfliktu git. Na liście błędów v2.1 (SHA-256 2f0092c2…) pasuje do tego „bug in convert_tables() and new tables in .h included”, ale tego nie rozstrzygam. Na T1 to nie wpływa.

**Stan teczki:** O1 i O3 wykonane, O4 wstępnie. Kolejne: O2 (użytkownicy `hadronization_choice = 1`), O5 (repozytoria i zgłoszenia), O6 (status T2).

## r3 (23 XI, 07:27, godzina z `date` przy zapisie): O2, opublikowani użytkownicy tablic HERWIG z BlackHawk

| # | zapytanie lub źródło | wynik |
|---|---|---|
| 13 | `Thoss Burkert Kohri 2024 MNRAS primordial black holes BlackHawk HERWIG hadronization`, potem alphaXiv: arXiv:2402.17823v2 (MNRAS 532, 451) | §2.2: „we use HAZMA for black holes with k_B T < 0.1 GeV, HDMSPECTRA for temperatures k_B T > 100 GeV, and HERWIG in the intermediate range”; sekcja SOFTWARE: BlackHawk 2.1. Zastosowanie: ograniczenia z promieniowania γ (galaktyczne, pozagalaktyczne) i CMB (ExoCLASS); BBN liczone osobno, modelem Kawasaki i in. 2018. Konwencji energii nie omawiają. Dane: Zenodo 10.5281/zenodo.10718218. |
| 14 | `"BlackHawk" "HERWIG" primordial black hole secondary spectra antiprotons OR positrons OR "BBN" hadronization comparison` | Opisy opcji (manual, 2010.04797, 2203.14979, 2406.11949: PYTHIA i Herwig „above 10 GeV”); brak porównań PYTHIA–HERWIG z wnioskiem o konwencji energii. |

**Odczyt [▷].**
- Opcja HERWIG w BlackHawk to wyłącznie tablice epoki BBN (`hadronization_choice = 1`), a w v2.1 są one bajtowo równe v2.3 (r2). Thoss i in. 2024 użyli ich więc z własnością T1 w opublikowanych ograniczeniach γ dla T od 0.1 do 100 GeV. Pierwotne mają tam energie ~0.5–500 GeV, w całości w siatce tablic HERWIG (25 GeV–1e5 GeV; poniżej 25 GeV zachowanie BlackHawk zależy od ekstrapolacji).
- Skali wpływu T1 na ich wynik nie oceniam. Opisany przez nich model niepewności to „około dwóch dex” (Auffinger 2023), więc wpływ może być w tym schowany. To przypadek propagacji T1 do literatury, nie dowód błędu ich wniosków.
- Dla bramki REC14 ROT001: ogniwo „HERWIG faktycznie użyty” jest teraz deklarowane przez autorów (tekst artykułu). Plik parametrów ich przebiegu pozostaje nieznany. Rekord Zenodo 10.5281/zenodo.10718218 nie jest osiągalny z tej sesji (WebFetch: adres spoza listy dozwolonych; wyszukiwanie nie zwróciło strony rekordu); do sprawdzenia przez komórkę z dostępem.

**Stan teczki:** O1, O3 wykonane; O2 częściowo (jeden opublikowany użytkownik, zastosowanie γ); O4 wstępnie; O5 i O6 otwarte.

## r4 (23 XI, 07:37, godzina z `date` przy zapisie): O5, repozytoria i zgłoszenia

| # | zapytanie (GitHub REST przez `gh`) | wynik |
|---|---|---|
| 15 | `search/issues?q=BlackHawk+herwig+is:issue` i `…BlackHawk+hadronization+is:issue` | Po 1 trafieniu: wyłącznie zgłoszenie tego projektu (wmakiela-tech/Nash-iw-research, „IW/NASH B1 — MOST ONLINE Mech-S9 ↔ Badacz”). Brak zgłoszeń zewnętrznych. |
| 16 | `search/code?q=hadronization_choice+herwig` | 104 pliki, głównie szablony `parameters.txt` i kopie BlackHawk w repozytoriach użytkowników (np. cewasiuk/Spin-and-Charge-BH-Evolution, michellekwok2/blackhawk_SUSY) oraz dane wyjściowe. Nie przeglądałem wszystkich ustawień `hadronization_choice`. |
| 17 | `gh search code "LuminosityFunction:Energy %"`, `search/code?q="LuminosityFunction:Energy"+herwig_scripts` | brak trafień w indeksie kodu GitHub (skrypty BlackHawk nie są tam indeksowane albo nie ma ich kopii). |
| 18 | `gh search repos BlackHawk` / `blackhawk hawking` | jedno repozytorium dydaktyczne korzystające z BlackHawk (fuzzballnerd/Hawking-Radiation); reszta to niezwiązane projekty o tej nazwie. Oficjalnego repozytorium BlackHawk na GitHub nie znalazłem (dystrybucja przez hepforge). |

**Odczyt:** w publicznych zgłoszeniach i kodzie na GitHub nie ma śladu T1 poza tym projektem. Ograniczenie: indeks kodu GitHub nie obejmuje archiwów hepforge ani repozytoriów prywatnych.

**O6 (status T2), odczyt kodu:**
- BlackHawk v2.3 `secondary.c` l. 138/145 zamienia liczbę zliczeń w przedziale k tablicy na gęstość `dN/dE'`: dzieli ją przez szerokość przedziału w przód (`final_energies[k+1] − final_energies[k]`) i przypisuje dolnej krawędzi E_k.
- Autorzy Wu–Xu całkują wyjście BlackHawk regułą trapezów w ln E (`valid_hadrons_from_BlackHawk.ipynb`, komórka 12: `h = mean(Δ log E)`, `(h/2)(2Σ − pierwszy − ostatni)`). Dla siatki logarytmicznej o kroku Δ daje to liczby zaniżone dokładnie o BIN = (e^Δ − 1)/Δ, niezależnie od kształtu widma: 1.0258 dla PYTHIA (500 przedziałów) i 1.1396 dla HERWIG (100 przedziałów). Dokładne odtworzenie liczby daje dopiero Σ ρ_k ΔE_k.
- Autorzy sami używają `hadronization_choice = 0` (PYTHIA; `tool_script-BlackHawk_extension.jl` l. 230–232). Ich tablica jest więc zaniżona o 2.6% (0.011 dex), a nie o 14%.

**Wniosek o T2 [▷]:** T2 nie jest wadą danych HERWIG. To niedopasowanie konwencji: gęstość z dolnej krawędzi przedziału w BlackHawk plus gładka reguła całkowania u użytkownika. Dotyczy każdej tablicy BlackHawk, a dla HERWIG jest ~5× większe przez grubsze binowanie. Status nowości T2 jest słabszy niż T1 (zagrożenie użytkowe, częściowo po stronie użytkownika).

**Stan teczki po obrocie 2:** O1, O3, O5, O6 wykonane; O2 częściowo (Thoss i in. 2024); O4 wstępnie. We wszystkich przejrzanych źródłach (18 wpisów) T1 nie jest opisany. To nadal „nie znalazłem”, nie „nie istnieje”; decyzja o nowości należy do Moderatora.
