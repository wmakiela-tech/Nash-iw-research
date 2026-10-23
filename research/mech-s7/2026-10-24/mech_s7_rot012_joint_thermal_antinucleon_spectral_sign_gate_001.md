# MECH-S7 ROT012 — podtablicowe widma antynukleonów × aktywna termodynamika PBH

**Data:** 2026-10-24. **Cell:** `IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7`.
**RETURN_ID:** `MECH-S7-FRONTB-JOINT-THERMAL-ANTINUCLEON-SPECTRAL-SIGN-GATE-012`.
**PROBLEM_ID:** `P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001`.
**Class:** `EXECUTED_CONDITIONAL_7D_SOURCE_ACTIVE_TWO_TEMPERATURE_ANTISPECTRAL_ROOTS / NUMERICAL_CONTROLS / NO_PHYSICAL_CLAIM`.

## 1. Pytanie i warstwy źródeł

**Pytanie:** Czy niezwykle niski próg przeciwstawnych zmian wykładników widm antyprotonowych i antyneutronowych z MECH-S7 ROT007 przetrwa po zastąpieniu archiwalnego tła Wu–Xu *już podczas aktywnej emisji* jawnym modelem dwu-temperaturowym EM+neutrina, przy wariantach zachowania barionów?

Pochodzenie wyników: (i) autorski Wu–Xu kod przypięty do `d395183674cace6c9906a8911bdeb7234ba4040d`; (ii) Mech-S6 oryginalne cztery archiwa trajektorii na dwóch osiach source law / charge map; (iii) ROT004 exact M³ law; (iv) ROT006/007/011 zmodyfikowany *warunkowy* executor 7D; (v) niezależny DAX-S7 ROT34–39 i PRF11 R21–22: tabela termodynamiki jest dwu-temperaturowa, z niezależną krytyką kodowej relacji chłodzenia. REC10: source OFF ≠ hadron forcing OFF. MT13/LT5/NC: końcowy odczyt fixed-T i wagi temporalne nie są zdeterminowane samą sumą emisji. Nie przypisujemy sobie ich odkryć.

## 2. Dokładnie badany host — NIE oryginalny solver 10D

* `u=M/M_edge`, `M_edge=10^9 g`, `d t/du=-3 M_edge^3 u²/Γ`, `Γ=4.207579833788249e27 g³/s`, `M_cut=6e9 exp(-20) g`.
* Stan wejściowy X + 6 hadronów pochodzi z ostatniego zapisanego aktywnego punktu oryginalnej 7D subkomparacji przy M≈1.84e9g i jest sztucznie przesunięty na krawędź 1e9g. **Pełnego pre-edge 10D NIE wykonano.**
* Promieniowanie: fotony i termalne e±, osobno efektywne trzy bezmasowe gatunki ν; χ_EM∈{0,0.5,1} dzieli całkowitą modelową energię PBH pomiędzy dwa składniki. Fizyczne ułamki Hawkinga i termalizacja ν NIE są wywiedzione.
* n_B: albo źródłowe stałe η_B w n_B=η_B n_γ, albo zachowana komowująca liczba barionów od krawędzi.
* Dwa mapowania sześciu źródeł/reakcji `B_exec`, `B_sym`; po zaniku PBH pozostają hadrony i ich interakcje; końcowa zmienna to **X_n przy T_nuc=0.07818527068831995 MeV**, NIE `Yp`.
* Osie prawa emisji: `public`=ekstrapolacja log-log z pierwszych dwóch wierszy tabeli, `paper`=M^-1.3; w gałęzi paper **tylko** antyproton i antyneutron otrzymują `α_pbar=-1.3+ε`, `α_nbar=-1.3−ε` przy niezmienionych normalizacjach na M_edge.
* `ε` to wolny, celowo przeciwskorelowany test kształtu, NIE źródłowe oszacowanie niepewności. Wartości strumieni w M<1e9g nie są fizycznie zatwierdzone.

## 3. Wykonane wyniki: 12 progów

Dla każdej (χ, przepis barionów, mapa) rozwiązano równanie `X_paper(ε,T_nuc)-X_public(T_nuc)=0` metodą Brent, każdorazowo ponownie integrując 7 sprzężonych równań z dokładnym u-mass clock; public jest stałym punktem odniesienia. Wymuszono przeciwny znak na obu stronach korzenia. Jednostki: `ΔX` podano w `10^-6`, ε i gradient bezwymiarowe.

| χ_EM | n_B | Mapa | Nominalne ΔX [10⁻⁶] | ε* | Różnica wykładników 2ε* | Testowa zmiana źródłowego p̄/n̄ przy M=10⁸ g |
|---:|---|---|---:|---:|---:|---:|
| 0 | η const. | `exec` | -6.950851 | +4.648244398e-05 | +9.296488796e-05 | -0.021404% |
| 0 | η const. | `sym` | +22.640745 | -2.747201462e-04 | -5.494402924e-04 | +0.126593% |
| 0 | komow. | `exec` | -6.982761 | +4.664908918e-05 | +9.329817835e-05 | -0.021480% |
| 0 | komow. | `sym` | +22.646866 | -2.744938621e-04 | -5.489877242e-04 | +0.126489% |
| 0.5 | η const. | `exec` | -6.892916 | +4.621879196e-05 | +9.243758392e-05 | -0.021282% |
| 0.5 | η const. | `sym` | +22.605949 | -2.750689005e-04 | -5.501378011e-04 | +0.126754% |
| 0.5 | komow. | `exec` | -6.979794 | +4.666889941e-05 | +9.333779883e-05 | -0.021490% |
| 0.5 | komow. | `sym` | +22.625821 | -2.744720822e-04 | -5.489441644e-04 | +0.126479% |
| 1 | η const. | `exec` | -6.835467 | +4.595613143e-05 | +9.191226286e-05 | -0.021161% |
| 1 | η const. | `sym` | +22.571285 | -2.754165181e-04 | -5.508330363e-04 | +0.126914% |
| 1 | komow. | `exec` | -6.976840 | +4.668867060e-05 | +9.337734119e-05 | -0.021499% |
| 1 | komow. | `sym` | +22.604871 | -2.744502202e-04 | -5.489004404e-04 | +0.126469% |

**Kontrola:** wszystkie 12 korzeni mają pierwotną pozostałość `|ΔX| ≤ 1.087e-11`; po NIEZALEŻNYM przeliczeniu końców przy `Radau rtol=3e-9` największa pozostałość wynosi `4.043e-11`. Każdy korzeń został też przetestowany po obu stronach przy `ε*±1e-5`; wszystkie 12 par zmieniają znak. Nominalny `ε=0` odtwarza wszystkie 12 komórek ROT011 z dokładnością poniżej `2e-11` w X. **Jest to test konwergencji obliczeniowej, NIE certyfikowana granica globalnego błędu.**

## 4. Ile wnosi tło, ile widma?

Dla stałego η_B:

* `B_exec`: ε* przy χ=0 = `4.64824439806e-05`, χ=1 = `4.59561314306e-05`, względne przesunięcie `-1.132282%`.
* `B_sym`: ε* przy χ=0 = `-0.000274720146188`, χ=1 = `-0.000275416518133`, względne przesunięcie modułu `+0.253484%`.
* Dla `B_exec` minimalny moduł nominalnego kontrastu w tych komórkach występuje przy χ=1, ale wciąż musi zniknąć dopiero pod `ε≈4.6e-5`. Lokalna pochodna ΔX po ε jest ~0.149, a dla `B_sym` ~0.082; oznacza to bardzo wysoką czułość widmową.
* Zmiana przepisu baryonowego również nie usuwa korzeni: przy χ=0 `B_exec` różnica ε* między zachowaną liczbą barionów a stałym η_B to `+1.666451954e-07`; analogicznie `B_sym` to `+2.262840685e-07`.

**Kontrprzykład do promowania znaku:** przy nominalnej papierowej ekstrapolacji ε=0 znaki `B_exec<0`/`B_sym>0` utrzymują się we wszystkich 12 komórkach. Jednak w każdej można *warunkowo* dobrać niezwykle niewielkie ε zerujące ten kontrast. Stwierdzenie "12/12 nominal PASS" nie stanowi więc certyfikacji odporności spektralnej. Zamiana prawa temperatury lub barionów nie jest substytutem walidacji p̄/n̄ źródła.

## 5. Dokładna kwalifikacja wniosków

**Uprawnione:** w *warunkowym*, odciętym na M_edge, 7D modelu dynamicznym z dwiema temperaturami istnieje lokalny, bardzo cienki rozdzielnik kształtów widm antynukleonów, stabilny do rzędu procenta wobec testowanych χ_EM i baryonowych zmian hosta.

**Nieuprawnione:** przypisywać ε jakiekolwiek rozkłady niepewności, wnioskować że rzeczywiste promieniowanie Hawkinga zawiera wskazaną asymetrię, że naukowy kod Wu–Xu jest fizycznie fałszywy, że prawdziwe X/Yp/DH zmienia znak, czy wyznaczać nową granicę PBH. Niesprawdzone: pełny oryginalny 10D Julia accepted-step tolerance ladder od powstania PBH do T_nuc; poprawność źródła poniżej 10⁹ g; przekazanie energii do EM/ν; tablicowe EOS gρ,gs i energia hadronowa; dynamika neutrino transport; legalna obserwabla helowa (autor arXiv v3 różni się od publicznego kodu); certyfikat globalnego błędu endpointu.

**Ograniczenie liczbowe:** `Radau rtol=3e-8` na 12 bracketing roots i niezależny `3e-9` przeliczony na końcach; brak porównania z pełnym źródłowym solverem Julia. Zależne pliki, archiwa i SHA256 w dołączonym pakiecie.

## 6. Decyzja naukowa i wpływ na Front B

Odciąć interpretację fizyczną znaku **niezależnie** od pozytywnych testów temperatury. Najtańszy nowy test źródłowy ma porównać kształty emisji p̄/n̄ w ważnym przedziale ~10⁸–10⁹g, z ich korelacjami; następnie wymagane jest wspólne oryginalne 10D Julia, accepted-step terminal trace, bilans energii i baryonów, prawidłowy fixed-T event oraz globalny budżet błędu. Ta kolejność nie otwiera nowego owner-task; pozostaje w dotychczasowym problemie P1 Front B.

**OTHERS FIRST:** DAX-S7 / PRF11 termodynamika; NC Oct10 bilans hadronów; MT13/NC/LT5 event-weighted sufficiency; REC10 postsource memory. Autorstwo niniejszego 12-komórkowego kontrtestu należy do Mech-S7 jako analizy źródłowo ograniczonego hosta, nie nowego twierdzenia ani nowej fizyki.

**Source links:**
- Wu–Xu pinned code `d395183`: https://github.com/Fenyutanchan/Primordial-Black-Hole/tree/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618
- ROT011 report: https://github.com/wmakiela-tech/Nash-iw-research/blob/091a4bbf540481b769d7d1a2d8af336a75be3b1b/research/mech-s7/2026-10-23/mech_s7_rot011_active_twotemp_energy_baryon_gate_001.md
- PRF11 R22 thermal host: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-23/prf11_r22_wuxu_two_temperature_eos_pressure_reconstruction_001.md
- MT13-NC event weighted source sufficiency: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/2026-10-23/mt13_nc_lt5_event_weighted_source_sufficiency_gate_001.md

`EXECUTED_12_ROOTS / EXACT_MASS_7D / INDEPENDENT_TIGHT_CONTROL_PASS / PHYSICAL_SOURCE_GAP_OPEN / SOURCE_10D_NOT_RUN / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_PBH_BOUND / BW_INGEST_UNVERIFIED`.