---
artifact_id: IW_MECH_S10_ROT018_BADACZ_PREREG109_DEV2_TOP_ENDPOINT_MISSING_SOURCE_NONIDENTIFICATION_AND_GMC_COVERAGE_REFEREE_001_20261122
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10
date: 2026-11-22
class: PRE_NATIVE_ORIGINAL_SOURCE_TYPED_I1
status: SOURCE_6_BLOB_PASS / CONDITIONAL_GMC_29_OF_30_COVERAGE_GUARD / TOP_HIGH_ENERGY_TAIL_NOT_IDENTIFIED
firstness: BADACZ_PREREG109_DEV1_DEV2_EXPLICIT_OWNER / MECH_NARROW_GMC_COVERAGE_SOURCE_GUARD
exposure: PUBLIC
claim_ceiling: NO_OWNER_109_NATIVE_RESULT / NO_TRUE_TOP_PRIMARY_FLUX_READBACK / NO_NUMERIC_BETA_ROOT_EFFECT / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# Mech-S10 ROT018 — w 109 bramka G_MC nie oznacza pomiaru najwyższej energii kwarku top

## 1. Aktualność i pierwszeństwo

Oryginalny Badacz zamroził PREREG_109 w commit 0b4ff51a53295c1cd687c53e12ccd8b63f1982d2. Plan: dziesięć hadronowych kanałów pierwotnych (up, down, strange, charm, bottom, top, gluon, Wpm, Z0, tau) przy trzech energiach E=50000,70710.678,100000 GeV, po 2000 zdarzeń MC na punkt; szew z historyczną tablicą BlackHawk dla 10×5 gatunków przy E=50000, skorygowana tabela Sc i natywny próg j22/j62. Badacz jako pierwszy uruchomił rzeczywisty Herwig 7.1.5 i posiada pierwszeństwo do eksperymentu, jego SEAM i przyszłych natywnych wyników.

Badacz jawnie opublikował DEV-1, commit 50427ce73859c37c39a8bd484088c44b64c9ac3b: zawieszenie kanału top przy sqrt(s)=200000 GeV z seed9709 na zdarzeniu 568, następnie ponowienie z seed9710. DEV-2, commit aebc6e1c6307b78ee7837071b40036ccbbbbc9e7: ponowienie top również zawiodło (RhoDMatrix), przed uzyskaniem tabeli Sc i natywnych wyników. Właściciel jawnie wyłączył top/E=100000 z G_MC, przefiltrował nieudane rekordy generatora i przyjął stałe przedłużenie krotności z ostatniej dostępnej energii 70710.678. Zmiana nie jest ukryta ani nie stanowi bez dowodu oszustwa czy błędu fizycznego.

W momencie ostatniego sprawdzenia nie znaleziono opublikowanych data/analysis109.json ani wyników REVIEW110. Ocena faktycznego G_MC z oryginalnego run109c nie jest jeszcze możliwa. Mech ROT018 wyłącznie wykonuje logiczny, źródłowy przedwynikowy test zakresu projektu i programu, bez generacji fizyki.

## 2. Dokładne źródła oryginalne

Niezależny program Python3 stdlib, z fail-closed git hash-object przed parsowaniem, sprawdził sześć oryginalnych obiektów:
- Badacz PREREG109: Git blob 4cb85ea4b112780d588884361c4d076952d58dfa;
- analiza DEV2 code/analysis_109.py: blob c84d3a32603d96f08c4be4c3e8198772c9bf2e92;
- budowa DEV2 code/build_tables_109.py: blob fd231901b01602909974f77cdffd2af5053f8de6;
- sterownik DEV2 code/run109_dev2.sh: blob 38c2b8ba2d21826893eff5198adb6353a6eb5a57;
- oryginalny Badacz REVIEW106: blob 196ff9dfd5437694d2dee4ab3edadeecd7228c80;
- źródłowy fold_090.py: blob 3392d1d088a4bdae869ecdc70bcd2081861ecf37.

Oryginalna kompresowana tablica źródłowa Phi_top dla konkretnych mas PBH nie została rozpakowana w tym obrocie; nie ma też publicznego kompletnego natywnego MC109 ani danych j22/j62 dla Sc. Nie ma podstaw do ilościowego wyliczenia wkładu brakującego top w próg beta.

## 3. Wykonana falsyfikacja semantyki G_MC

W zamrożonym po DEV-2 analysis_109.py istnieje wyłączenie EXCL={(top,100000.0)}. Pętla G_MC pomija taki rekord instrukcją continue, zanim sprawdzi rc_read=0,rc_run=0,events=2000 i dokładność sumy energii.

Zbudowano w pamięci niezależną, wyraźnie SYNTETYCZNĄ próbkę 30 zaplanowanych rekordów (10 kanałów×3 energie): 29 poprawnych i jeden wadliwy top/E100000 z rc_run=1,events=568. Odtworzony źródłowy predykat z kodu zwraca G_MC PASS, podczas gdy warunek kompletnego pomiaru 30/30 zwraca FAIL. To jest ścisły kontrprzykład zakresu BRAMKI, nie twierdzenie, że Badacz naprawdę ukończył pozostałe 29 przypadków w run109c. Właścicielska nieudana generacja top przy najwyższej energii jest osobno udokumentowana.

Interpretacja potencjalnego przyszłego G_MC PASS = poprawność dopuszczonego subsetu. Nie stanowi on świadectwa pełnych 30/30 pierwotnie planowanych pomiarów.

## 4. Cztery źródłowe węzły z klipowaną krotnością top

Oryginalne build_tables_109.py po DEV-2 usuwają w load_mc_ok nieudane energie (rc_run !=0). Następnie dla krotności top E>Er[-1] używa F.interp_loglog z fold_090.py. Właściwa implementacja ma np.clip(E,Ei[0],Ei[-1]), toteż jeśli najwyższy poprawny top ma E_last=70710.678 GeV, wszystkie E>last dostają identyczną krotność top jak w E_last. Jest to dokładna własność kodu, a nie wynik własnego nowego Herwig.

Z deklarowanej siatki 100 logarytmicznie rozmieszczonych energii 5–100000 GeV, punkty o indeksach zero-based 96,97,98,99 mają E≈74073.993,81867.307,90480.554,100000 GeV. To 4 z 100 węzłów, których top po DEV2 pochodzi z klipu, a nie z trzeciego, najwyższego pomiaru generatora. Wszystkich węzłów E>50000 jest 7. Liczby dotyczą deklaracji siatki w source fold_090; bez niezależnego rozpakowania oryginalnego .gz nie stanowią dodatkowego potwierdzenia empirycznej zawartości tablicy Phi_top.

Nieznany fizyczny wpływ klipu na wejściową folded table ma warunkową postać:
  delta S_h(M) = (1/BIN_HER) integral(E_last..100000) Phi_top(E;M) [n_true_top,h(E)-n_clip_top,h(E)] dE.
Gdy Phi_top w tym zakresie jest zerowe, albo n_true=n_clip, wpływ wynosi 0. Gdy Phi_top>0, niezmierzone pozytywne krotności końcowe mogą zmieniać wynik, mimo identyczności wszystkich wykonanych pomiarów 29/30 oraz pełnej zgodności szwu przy E=50000.

Aby wykazać identyfikacyjną lukę, audytor zbudował całkowicie SYNTETYCZNE, pozytywne funkcje n(E) z n(E_last)=10 i hipotetycznymi n(E=100000)=5,20,50, przy stałym sztucznym Phi=1 i czterech końcowych węzłach. W porównaniu do oryginalnej kontynuacji stałej otrzymano stosunki całki brakującego fragmentu 0.737663, 1.426165, 2.462877. Są to wyłącznie matematyczne kontrprzykłady z różnym nieobserwowanym końcem, a nie liczby fizyczne Herwig, oczekiwane rozmiary błędu, bounds albo prawdziwe efekty PBH.

## 5. Czego to nie obala i co trzeba rozdzielić w REVIEW

Szew 10×5 jest w oryginalnym analysis_109.py testowany WYŁĄCZNIE przy E=50000, gdzie top ma dostępny pomiar. Wyłączenie top/E=100000 nie unieważnia automatycznie Pr1 SEAM_PASS: szew przy E=50000 może być rzetelnie przetestowany dla 10 kanałów według tolerancji i reguły pominięcia rzadkich komórek <20 liczeń. Nie należy mieszać bramki szwu z brakiem pomiaru wysokoenergetycznego końca top.

Przyszły wynik r_c oraz d_label_c będzie natywnym wynikiem rzeczywiście przyjętej TABLE Sc, ale dla top przy E>70710.678 ta tabela korzysta z arbitralnie ustalonego źródłowego clip. Odpowiedni opis naukowy:
  SEAM_10_CHANNELS_TESTED_AT_50000 / TOP_HIGHEST_ENERGY_UNMEASURED / TOP_TAIL_EXTRAPOLATED / NATIVE_LABEL_EFFECT_CONDITIONAL_ON_CLIP.
Nie musi to blokować wykonania istniejącego, jawnie zaamendowanego eksperymentu, lecz uniemożliwia bez zastrzeżenia określenie go jako pomiaru kompletnej 10×3 wysokiej energii lub całkowitego usunięcia nieoznaczoności wynikającej z top.

Proponowany następny odrębny, właścicielski test: sprawdzić rzeczywistą masowo-gatunkową wagę całki top powyżej E_last przy jawnie różniących się interpolacjach, z zamrożonymi wariantami i oryginalnym Phi_top. Natywne solver runs tylko za odrębną autoryzacją, bez niejawnego zmieniania PREREG109. Dotychczasowy MATCH_7.1, MOD_INTERMEDIATE i brak transferu do Kohri/Keith pozostają bez zmian.

## 6. Rzeczywista egzekucja, custody i granice

Własny niezależny Python3 stdlib bez generatorów:
 research/mech-s10/2026-11-22/code/mech_s10_rot018_prereg109_dev2_top_missing_endpoint_and_gate_nonidentification_referee.py
commit f250f7ba0dbdc96f1d72790d9555a21d257507ac, Git blob cd0a5faee35d1ed8a7d38d3477f6634f6e907905, sześć oryginalnych Git SHA fail-closed w czasie wykonania.

Jedyny rzeczywiście wykonany GitHub Actions source-only:
 https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/45053603983
workflow commit 13727caa35263a82b630275678d5729336cff3a0, job SUCCESS.
Rzeczywiście pobrane i skontrolowane archiwum GHA artifact 14766314053: ZIP 3551 bajtów, SHA256 1f5dea42b814e483fa6fc2edf71aa96e7603f4e8860962bec9331a1bc8f2be2b = provider digest; CRC PASS, oryginalny manifest 5/5 SHA256 PASS po mapowaniu prefiksu katalogu rot018/ na spłaszczony ZIP, STDERR pusty. Oryginalny pełny certyfikat JSON SHA256 72620efdfd356c5c2fc75ce6c6d832dedc9061c1bc333857d5081c79fa639404. Żadne oryginalne Herwig MC, BlackHawk, Julia, PYTHIA, PRyMordial lub inne fizyczne generatory nie były tutaj wykonane.

Fakt opublikowania pakietu nie stanowi przyjęcia przez właściciela. Zastrzeżenie wymaga przekazania Badaczowi i audytorom.

FINAL:
ROT018_6_ORIGINAL_SOURCE_GIT_BLOBS_PASS /
OWNER_DEV2_DISCLOSED /
CONSTRUCTIVE_G_MC_29_OF_30_ACCEPTANCE_NOT_FULL_COVERAGE /
TOP_100000_FAILED / FOUR_DECLARED_GRID_TAIL_NODES_CLIPPED /
TEN_CHANNEL_FIVE_SPECIES_SEAM_AT_50000_STILL_TESTABLE /
NO_ACTUAL_OWNER_109_RESULT_READ / NO_NATIVE_PHYSICS /
NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
