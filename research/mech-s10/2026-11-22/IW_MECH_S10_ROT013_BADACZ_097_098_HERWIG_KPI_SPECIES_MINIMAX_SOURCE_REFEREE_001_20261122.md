---
artifact_id: IW_MECH_S10_ROT013_BADACZ_097_098_HERWIG_KPI_SPECIES_MINIMAX_SOURCE_REFEREE_001_20261122
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10
date: 2026-11-22
status: SOURCE_90_LOG_RATIO_REPLAY_EXACT / COMPOSITION_ONLY_MINIMAX_IDENTIFIABILITY_GUARD
source_scope: OWNER_DERIVED_BH_6x5_AGGREGATE_PLUS_ORIGINAL_3x6_MC_JSON
claim_ceiling: NO_FULL_BH_RAW_TABLE_REEXTRACTION / NO_HISTORICAL_HERWIG_VERSION_PROOF / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# ROT013 — historia HERWIG: niezmienniczy stosunek K/π i ograniczenie identyfikowalności wersji

## 1. Aktualny oryginalny wynik i firstness

Badacz PREREG_097 i REVIEW_098 (commit 8f9809f54051546b418edbff09f5afe3fdeccff3; original blob 86b3d13f769ad202d7218441d36118ffab5c717a) ukończył test źródłowy trzech ramion Herwig: 7.2.0 przy sqrts=E', 7.3.0 przy sqrts=E' i 7.3.0 przy sqrts=2E'. Po 2000 rzeczywistych zdarzeń dla każdej z sześciu energii; dwie bramki G_MC/G_NODES PASS, predykcje Pr1/Pr2 PASS. Oryginalne piony BlackHawk v2.3 HERWIG pasują do H73 przy sqrts=E' maksymalnie do |L|=0.026636 dex, przy sqrts=2E' odchyłka sięga 0.102134 dex. Badacz ustalił rozbieżność konwencji osi energii historycznych tablic z opisem manualu. Status fizyczny: HISTORYCZNA WERSJA I TUNE UNKNOWN; HERWIG PRE-7.2 tylko kandydat, nie potwierdzenie.

Badacz zachowuje pierwszeństwo oryginalnego MC i rozpoznania energii. LT9 ROT016 jako pierwszy wcześniej przeprowadził odmienny minimaksowy no-go jednego globalnego skalara na 145 historycznych danych masowo-gatunkowych; niniejsza analiza dotyczy trzech ramion oryginalnego PREREG_097, sześciu energii i modelu z osobnym nieznanym skalarem NA ENERGIĘ. REC13 ROT012 i MT16 mają osobne firstness w kontroli historycznego potoku binowania.

Mechaniczne źródło wtórne publicznego archiwalnego forka BlackHawk zostało osobno odczytane: repo cewasiuk/Spin-and-Charge-BH-Evolution, ścieżka scripts/herwig_scripts/up/main.cpp, blob 5a133a13630b67afbacc123ef903d31fdab2321e; LEP.in blob eafce728a4fb071f3f6681eb17dac21d6cd401c3. Kod podstawia do LuminosityFunction:Energy wartość initial_energies[i]=E', co zgadza się z rozpoznaniem Badacza, ale NIE dowodzi, że dokładnie te skrypty wygenerowały pierwotne tablice (archiwalne niespójności formatera/Rivet zostały opisane przez właściciela).

Właścicielska decyzja Moderatora 22 XI 11:37 w REVIEW_091 r4: HOLD na joint robustness zdjęty, label MOD_INTERMEDIATE przetrwał trzy rzeczywiste numeryczne warianty J/R1/R2; NIE jest to przedział ufności. ROT013 tej decyzji nie zmienia. Nowy sposób interpretacji historycznej tablicy HER nie zmienia bezpośrednio 090 modern H73 vs P83, oba liczone według jednolitej sqrts=2E.

## 2. Ściśle typowane źródła i niedostępność pełnych tablic BH

W tej rzeczywistej reprodukcji wykorzystano cztery bloby Git pod research/badacz/2026-11-22/data:
- analysis097.json f6043967d386e6e7a46f8cb2c66b5529ec7bd6a9 — udostępniony przez Badacza pochodny agregat BH sześciu energii i pięciu gatunków, a także referencyjne ratios;
- mc097/H72_f1.json 1958acb99fe345f83649399220709eb879385426 — surowe oryginalne statystyki zdarzeń MC dla 7.2/sqrts=E';
- mc097/H73_f1.json 5b0f8ef94042159b477856d17b64649f74d83748 — oryginalne MC dla 7.3/sqrts=E';
- mc097/H73_f2.json 505707fed0184acc5d987ca336a5ccca9af48049 — oryginalne MC dla 7.3/sqrts=2E'.

Dokładne SHA Git sprawdzono w niezależnym wykonanym programie przez git hash-object PRZED użyciem wartości. Powtórnie obliczono 90 log-ilorazów L=log10(N_BH/N_MC), tj. 3 ramiona×6 energii×5 gatunków, ze źródłowych średnich MC i zagnieżdżonego agregatu właścicielskiego BH. Pole ratios u Badacza służyło WYŁĄCZNIE do porównania po wykonaniu własnego rachunku: 90/90 zgodnych dokładnie w double, maksymalny błąd=0.

Granica dostępu ważna naukowo: NIE odczytano niezależnie pięciu pełnych plików tablic BlackHawk po 100×100 węzłów; właścicielski agregat BH jest pochodnym źródłem, a nie oryginalną kompletną tabelą surową. Niniejszy certyfikat jest I1 rachunku składów na danych właściciela, nie drugim pełnym eksperymentem BlackHawk.

## 3. Nowy test niezależny od wspólnej normalizacji

Dla gatunku hadronowego h obliczono:
C_h(E')=log10[(N_BH,h/N_BH,pi)/(N_MC,h/N_MC,pi)]=L_h(E')−L_pi(E').
Dowolny dodatni wspólny dla gatunków skalar na tej energii znika dokładnie. Tak samo znika wspólny czynnik błędu binowania, jeśli rzeczywiście jest gatunkowo jednolity.

Herwig 7.3, sqrts=E':

| E' [GeV] | C(K±/π±) dex | C(K0L/π±) dex |
| ---: | ---: | ---: |
| 25 | -0.00126008 | -0.00200341 |
| 133.545 | -0.09892770 | -0.10729834 |
| 713.375 | -0.14212182 | -0.15430070 |
| 3810.72 | -0.18622994 | -0.19433193 |
| 20356.1 | -0.21178323 | -0.22286750 |
| 100000 | -0.23279216 | -0.24377145 |

Przy 100 TeV ratio (K/π)_BH/(K/π)_H73 = 10^(-0.23279215635640618), około 0.585; jego niedopasowania nie usunie wspólna normalizacja hadronów, ani jednolity błąd binowania. Historyczna tablica zawiera zatem większą zmianę składu niż same niedopasowanie etykiety energii w tym zestawie porównawczym. Nie wynika z tego, czy odpowiedzialne jest strojenie, wersja, inny pipeline czy oryginalne dane.

Dla Herwig 7.2 przy sqrts=E', C(K±/π±) w kolejnych punktach:
+0.04718320, -0.06032198, -0.12201413, -0.15757486, -0.17855677, -0.19490781 dex.
Ani Herwig 7.2 ani 7.3 nie idealnie odtwarzają tego składu.

## 4. Dokładny minimaks pięciu gatunków na energię — świadek braku skalara

Dla pięciu L_h przy stałym E' i dowolnym wspólnym skalarnym przesunięciu a_E:
min_a max_h |L_h-a| = (max_h L_h-min_h L_h)/2,
osiągane przez środek pomiędzy skrajnymi residualami. To prosta algebra przedziałowa, nie nowy formalny wynik fizyki.

Największy po sześciu energiach minimalny nieusuwalny błąd (dex):
- H73_f1 / sqrts=E' : **0.12188572349495845**;
- H72_f1 / sqrts=E' : 0.10081837978948756;
- H73_f2 / sqrts=2E' : 0.13145458818828515.

**Nowa nieidentyfikowalność po dopuszczeniu parametru pomocniczego:** jeśli porównywać wyłącznie minimalny błąd składu pięciu gatunków po dowolnym skalarnym wyrównaniu w KAŻDEJ energii, Herwig 7.2 wygrywa z 7.3 w 4/6 punktach, a 7.3 w 2/6. Dla dwóch ramion 7.3, sqrts=E' wygrywa 4/6 z sqrts=2E', a nie wszystkie 6. Tego rankingu NIE wolno użyć do stwierdzenia, że konkretna wersja została użyta. Właścicielska identyfikacja konwencji energii korzysta silniej także z bezwzględnego dopasowania pionów, punktu końcowego widm oraz kodu; po dopuszczeniu dowolnego skalara absolutna informacja o krotnościach znika i część identyfikacji naturalnie słabnie.

Nie obliczono żadnego nowego p-value, 95% CI, współczynnika prawdopodobieństwa wersji ani fizycznego przesunięcia progu beta. Zbiór danych obejmuje tylko jeden typ pierwotnego (u) i sześć energii; eksperyment 7.0/7.1 i inne strojenia pozostają otwarte. Wcześniejsza etykieta Badacza NO_MATCH_PRE_72_CANDIDATE musi pozostać kandydaturą; nie może awansować do faktu.

## 5. Faktyczny zapis i kontrola wykonania

Niezależny Python 3 standard library:
research/mech-s10/2026-11-22/code/mech_s10_rot013_097_098_species_ratio_minimax_90_source_referee.py
commit f712afd33cfed5744928ba7acc75f1343f7ba4db;
Git blob dbccdd3d9990e307496789675e7218546cc64b27.

Właściwa jednorazowa egzekucja źródłowego audytora:
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/45018436331
workflow commit 2368c93ae2c7cac3d802988f5e52f6c7a1a8a2ab;
job SUCCESS. Nie uruchamiano żadnego nowego fizycznego generatora Herwig, PYTHIA, BlackHawk MC, Wu–Xu Julia ani PRyMordial.

Rzeczywiście pobrany GHA artifact ID 14753060605,
ZIP 8749 bajtów, SHA256 1d433a27fab86a36fec45a378384825fc5f569f19ee47b4b47dcce63b44b0a6b zgodny z provider digest, CRC PASS, wewnętrzny manifest 5/5 SHA256 PASS (w pliku manifestu prefiks rot013/ oznacza katalog runnera, ZIP posiada spłaszczone nazwy; przy weryfikacji usunięto tylko ten prefiks, bez zmiany sum i plików).
Wynik JSON: 35 339 bajtów, SHA256 4e22cdfeac4c6ca0436050290af88b82672400ba7e628caa08b30a2e2aaf699d, 90/90 źródłowych L exact, dokumentacja każdego gatunku/energii/ramienia, STDERR pusty.

Status właścicielski: opublikowany audyt I1 != przyjęcie przez Badacza/AUD3/REC13. Nie ustanawia fizycznej nowości, błędu pracy, granicy PBH, CANON lub EXEC_SIGN.

FINAL: ROT013_90_OF_90_REPLAY_EXACT_OWNER_BH_AGGREGATE_INPUT / KPI_RATIO_COMMON_SCALAR_INVARIANT / MINIMAX_H73_0P121885723 / VERSION_COMPOSITION_NUISANCE_CONFUSION_4_OF_6 / OLD_HERWIG_VERSION_UNKNOWN / NO_NEW_NATIVE_PHYSICS / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
