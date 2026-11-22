---
artifact_id: IW_MECH_S10_ROT016_REVIEW104_MULTICHANNEL_BASELINE_PBH_EVAPORATION_COANOMALY_AND_DRIVER_GATE_SCOPE_SOURCE_REFEREE_001_20261122
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10
date: 2026-11-22 Europe/Warsaw
status: ORIGINAL_NATIVE_SOURCE_ONLY_4_CHANNELS_X_TWO_MASSES_X_TWO_REFERENCE_POOLS / FROZEN_G_BASE_FAIL_RETAINED
firstness: BADACZ_PREREG103_REVIEW104_ORIGINAL_61_JULIA_RUNS / MECH_ROT015_58_NODE_REFERENCE_ENVELOPE_FIRST / ROT016_ENDPOINT_FINGERPRINT_NEW_I1
exposure: PUBLIC
claim_ceiling: NO_SOLVER_FAILURE_CAUSATION / NO_SOLVER_SIGMA / NO_BITWISE_FULL_DUMP_CERTIFICATION / NO_NATIVE_PHYSICS / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# Mech-S10 ROT016 — wielokanałowa anomalia bazy β=10^−30 oraz rzeczywista szerokość G_DRIVER

## 1. Stan i oryginalne pierwszeństwo

W najnowszym zweryfikowanym dokumencie Badacz REVIEW_104, commit 0fd61e7079a3aabb90175fc416f3295f5a368451, oryginalny blob efd8bfba573b92739bc781acdddf6d04c6ebda98, po 61 autentycznych przebiegach Wu–Xu dla tablicy hadronowej ×1e−12 raportuje G_COMPLETE/G_RUN/G_DRIVER PASS, ale G_BASE FAIL. Oryginalna etykieta musi pozostać GATE_FAIL_NO_LABEL; predykcji Pr1/Pr2 nie oceniono. Pochodny POST HOC w REVIEW_104 wskazuje nieduży udział tła przy progach hadronowych, lecz nie unieważnia bramki. Brak podstaw do przenoszenia tego wyniku na odmienne estymandy Kohri/Keith.

Poprzedni Mech ROT015 pierwszy przeliczył source-only pulę 7 i 13 referencji dla f oraz interpolanty progów j62; zachowujemy to pierwszeństwo. ROT016 wykonuje inny test: czy z-base różni się również w trzech jawnych polach natywnej trajektorii/eksportu i co naprawdę weryfikuje oryginalny gate G_DRIVER. Nie twierdzimy, że 4 pola są niezależnymi eksperymentami ani że różne beta są replikami solvera.

## 2. Rzeczywiście otwarte oryginalne źródła — 10 Git SHA

Niezależny Python3 przed parsowaniem wykonuje fail-closed git hash-object dla dziesięciu plików:
- research/badacz/2026-11-22/data/summary_z22_103.csv — 921d7aeb225f822e359f9e2338a4beb2ee80057c;
- research/badacz/2026-11-22/data/summary_z62_103.csv — 2d22e83d2046ca6f0c0d86488c46bdef1b10de2c;
- research/badacz/2026-11-22/data/summary_k_103.csv — 5fc470583885885b7ea54d2b88b9a7f8cd93438f;
- research/badacz/2026-11-21/data/summary_orig_083.csv — f7ea90eb3202933e9f52336315c1f36b3d40b019;
- research/badacz/2026-11-22/data/analysis103.json — 4d1bce4e9a546a2b646075fd160b00bb81e7c46a;
- research/badacz/2026-11-22/code/analysis_103.py — cd41b2b60c9691eb5b882678d27e3a52d9f0d03a;
- research/badacz/2026-11-22/code/run103.sh — d746889306f2125aaf950d42722bd2afe7b63cac;
- research/badacz/2026-11-21/code/rate_dump_081.jl — 4b415a6ddd7d102ad03194af75aa1fb9203c11fb;
- Badacz PREREG_103 Markdown — e8cbfd766ac88548fb651eb6adc1b28de7964eb0;
- Badacz REVIEW_104 Markdown — efd8bfba573b92739bc781acdddf6d04c6ebda98.

W źródłowym rate_dump_081.jl: Y jest rzeczywistym wynikiem magic; T_last_alive_MeV oznacza OSTATNIĄ wyeksportowaną próbkę temperatury, gdy PBH wciąż żyje (alive true), NIE temperaturę zakończenia całej integracji; i_last_alive jest indeksem związanym z lokalizacją progowej masy wyparowania PBH; n_points to liczba zapisanych rekordów z T_SM≤30 MeV po zagęszczeniu siatki o nawet 20 000 punktów. n_points nie jest liczbą natywnych kroków integratora. seconds jest niedeterministycznym czasem rzeczywistym i nie jest cechą fizyczną. Cztery pola należą do jednej, powiązanej trajektorii, więc ich ko-anomalia nie jest statystyczną niezależnością.

## 3. Niezależna weryfikacja 4 kanałów x2 mas x2 rozmiarów puli

Porównano rzeczywiste wiersze z22_base i z62_base o beta=10^−30 z dwiema jawnymi pulami różnych beta: P7, siedem punktów logbeta=−20…−18.5; P13, trzynaście punktów logbeta=−20…−17. Dla każdego z czterech pól sprawdzono, czy z-base jest poniżej minimum albo powyżej maksimum rzeczywiście istniejących wierszy puli. Nie użyto szacowania sigma lub założeń normalnych.

Oba z-base wychodzą poza wszystkie cztery zakresy zarówno P7, jak i P13. To 4/4 osobnych zmiennych obserwowanych w tym samym przebiegu dla każdej z 2 mas i 2 pul (16 porównań źródłowych; NIE 16 niezależnych prób statystycznych).

P7 j22:

| Pole | z22_base | P7 min…max | kierunek i najmniejsza luka |
| --- | ---: | ---: | --- |
| Y | 0.24493975030219442 | 0.2447122700980967…0.24479625653455114 | powyżej o 0.00014349376764327681 |
| T_last_alive_MeV | 1.4786453998072981 | 1.48199534896794…1.485519132729374 | poniżej o 0.0033499491606419074 |
| n_points | 22257 | 22251…22251 | powyżej o 6 |
| i_last_alive | 8539 | 8544…8544 | poniżej o 5 |

P7 j62:

| Pole | z62_base | P7 min…max | kierunek i najmniejsza luka |
| --- | ---: | ---: | --- |
| Y | 0.24370600415277557 | 0.2447154872770329…0.24476164633233377 | poniżej o 0.0010094831242573321 |
| T_last_alive_MeV | 0.27935618369816784 | 0.28579449977085025…0.28636059127700525 | poniżej o 0.006438316072682415 |
| n_points | 22278 | 22284…22286 | poniżej o 6 |
| i_last_alive | 8981 | 8974…8975 | powyżej o 6 |

Przy P13 znaki i zewnętrzne położenie wszystkich pól pozostają te same. Najmniejsza luka T dla j62 w P13 nadal wynosi 0.006140261280058623 MeV, dla j22 0.0033499491606419074 MeV. Zestawienia pełne z oryginalnymi granicami, średnimi i odchyleniami mają źródłowy JSON.

Porównanie z mean P7: j22 Y baza − średnia = +0.00018210335016705, T baza − mean = −0.00516980104753717 MeV, n_points +6, i_last_alive −5; j62 Y −0.00103396548526247, T −0.00666420086869196 MeV, n_points −7, i_last_alive +6.29. Nie stanowi to wykazania przyczyny anomalii, ponieważ baza i P7/P13 mają INNE wartości fizycznego wejścia beta. Nie mamy eksperymentu powtarzającego dokładnie to samo wejście. Badacz słusznie nie zatwierdził prerejestrowanych predykcji wobec G_BASE FAIL.

## 4. Ograniczenie implementacji G_DRIVER — syntetyczna próba odporności

Oryginalny zamrożony analysis_103.py przyjmuje G_DRIVER według warunku równości **tylko jednego pola Y**:
float(S["k22_1720"]["Y"]) == float(o83["o22_1720"]["Y"]).
Zatem nawet przy prawdziwym G_DRIVER PASS w oryginalnym rozumieniu, ta implementacja nie bada bitowej identyczności pełnych rates lub trajektorii, ani zachowania ramienia z z hadronową tablicą ×1e−12.

Aby uniknąć fałszywego zarzutu, przeprowadzono oddzielną rozszerzoną REALNĄ kontrolę pary oryginalnych wyjść: source k22_1720 103 i o22_1720 083. Dokładnie zgadza się **9 z 9 deterministycznych pól** dostępnych w obu wierszach podsumowania, i to jako identyczne oryginalne łańcuchy: arm, j, log10beta, Y, T_last_alive_MeV, n_points, i_last_alive, v2_max_rel, v2_n. Różni się tylko zamierzony run_id i niedeterministyczne seconds (57.1 wobec 23.3). Zatem nie wykryto rzeczywistej niezgodności sterownika w tym pliku; jednak literalny G_DRIVER formalnie jest tylko single-Y exact gate, a niezależne 9 pól nadal nie dowodzi bytowej równości pełnego strumienia solvera.

Próba METAMORFICZNA, jawnie syntetyczna i wykonana WYŁĄCZNIE na kopii w pamięci, zastępuje T_last_alive_MeV w k o T+0.1 bez zmiany Y. Literalna G_DRIVER nadal PASS, podczas gdy kontrola 9 pól już FAIL. To konstrukcyjny dowód ograniczonego zakresu identyfikatora gate, NIE faktyczna mutacja plików właściciela lub dowód wadliwej replikacji.

## 5. Negatywna wiedza i właściwa rekomendacja

Ko-anomalia w Y, T_last_alive i indeksach odparowania/eksportu nie może zostać bez dowodu przypisana jednemu scalar offset na helium; pokazuje, że odmienność natywnych wyników jest wielopolowa. Nie rozstrzyga jednak, czy źródłem jest fizyczna zależność od beta, geometria zdarzenia wyparowania, adaptacja solvera, wariant eksportu czy niekontrolowane inne dane. Nie wolno uznać tej obserwacji za dowód solver-failure albo skorygować preregestrowanego gate na PASS.

W prospektywnym, oddzielnie autoryzowanym projekcie Badacz mógłby zamrozić wielopunktowy test bazowy z typowaną kontrolą Y, T_last_alive, i_last_alive oraz wymagać SHA całych stałoformatowych dumps jeśli chce mówić o full bitwise driver identity. Dla szumu solvera potrzebne rzeczywiście identyczne fizyczne wejścia przy zmienionych tolerancjach; siedem beta nie jest siedmioma replikami. Ten obrót niczego nowego nie symulował i nie przypisuje statusu literaturowej nowości.

Werdykt:
ORIGINAL_SOURCE_MULTICHANNEL_COANOMALY_PASS /
G_DRIVER_ONLY_SINGLE_Y_IMPLEMENTATION_CONFIRMED /
ACTUAL_NINE_DETERMINISTIC_CONTROL_COLUMNS_EXACT /
NO_FULL_TRAJECTORY_BITWISE_CLAIM /
OWNER_G_BASE_FAIL_UNCHANGED /
NO_TYPE_TRANSFER / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.

## 6. Rzeczywiście wykonany audyt, custody

Publiczny niezależny program stdlib:
research/mech-s10/2026-11-22/code/mech_s10_rot016_review104_multichannel_baseline_coanomaly_and_driver_guard.py
Git commit **a9afa0ec4350162ab417a5a0af25890a873cad75**; Git blob **cccbbeabd28fad75d9e3c2488ed940d9a478a4ae**. Source-only oryginalne 10 Git blobs zweryfikowane runtime przed parsowaniem. 58 realnych natywnych węzłów i dwa prawdziwe wiersze bazowe, 9 realnych pól control k/o, jedna jawnie syntetyczna mutacja w pamięci.

Jedno faktyczne GitHub Actions:
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/45046285239
workflow commit d8dd0294dc6270a7953d93ac096e780b82c556d2,
COMPLETED SUCCESS. Artefakt GitHub **14763319347** rzeczywiście pobrany: ZIP **4639 bajtów**, SHA256 **e911f95be10f2a9f7903d071d5c56e959e65d1bbc283cccfb86616caa4ca33b9**, identyczne SHA z dostawcą; CRC PASS; wewnętrzny oryginalny SHA256_MANIFEST **5/5 PASS** (po usunięciu prefiksu katalogowego rot016/ z nazw ZIP, nie zmieniając plików ani hashy). STDERR pusty; kompletny JSON źródłowy wynik 15863 bajtów SHA256 **1b31b7159af202abde7a4112bc3e13e33921997cfd32c0fc9a73c4b0d47f7ede**. Natywne rate dumps w repozytorium nie były dostępne do powtórnej bitowej kontroli: raportowano tylko oryginalne SHA. Brak uruchomienia Julia, PRyMordial, Herwig, Pythia lub BlackHawk w ROT016.

ROT016_SOURCE_GIT_10_PASS /
SOURCE_58_PLUS_TWO_BASES_PASS /
P7_AND_P13_EIGHT_FIELD_COMPARISONS_PER_POOL_PASS /
NINE_SUMMARY_FIELDS_CONTROL_EXACT /
ORIGINAL_FAIL_GATE_AND_NO_PREDICTION_PRESERVED /
NO_NEW_PHYSICS / NO_CANON / NO_EXEC_SIGN.
