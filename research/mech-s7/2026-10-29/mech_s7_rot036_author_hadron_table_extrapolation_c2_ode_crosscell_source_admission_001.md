artifact_id: MECH-S7-FRONTB-AUTHOR-EXTRAPOLATION-GATE-AND-CROSSCELL-SOURCE-ADMISSION-036_20261029
exposure: PUBLIC
claim_ceiling: SOURCE_PINNED_CODE_AUDIT_AND_EXECUTED_CONDITIONAL_POSTEDGE_7D_SENSITIVITY_ONLY / AUTHOR_NATIVE_10D_NOT_EXECUTED / PHYSICAL_SUBEDGE_SPECTRUM_UNVALIDATED / NO_Yp_DH_PBH_BOUND / NO_MATHEMATICAL_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
result_class: SCIENTIFIC_SOURCE_AUDIT / THREE_BACKGROUND_TWO_MAP_NONLINEAR_ODE_REPLAY / C2_EDGE_CONTROL / NO_PHYSICAL_ADMISSION
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7
problem_id: P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001
rotation: ROT036
created_at: 2026-10-29
owner_response: CONTINUES_ROT035_AND_MT14_ROT013

# Mech-S7 ROT036 — Źródłowa brama ekstrapolacji hadronów Wu–Xu; test C² i kontrole międzykomórkowe

## I. Wynik i jego granice

**Wynik źródłowy:** przypięty kod Wu–Xu rzeczywiście PRZEDŁUŻA emisję poniżej dolnej masy tablicowej, a nie pozostawia jej niezdefiniowanej. Służy temu `DataInterpolations.LinearInterpolation(log Q,log M; extrapolation=ExtrapolationType.Linear)`. Tablica 100×6 `hadrons_from_PBH.dat` obejmuje od 1e9 do 4e12 gramów (pierwsza masa 5.609588603804452e32 GeV, ostatnia 2.243835441521781e36 GeV). Przy masach mniejszych niż 1e9 g kod stosuje potęgowe przedłużenie z nachyleniem wyznaczanym z PIERWSZYCH DWÓCH wierszy. Jest to **fakt o algorytmie autora**; nie jest niezależnym potwierdzeniem fizycznej poprawności podprogowych widm Hawkinga. Skrypt skanowania autorów rozpoczyna zakres początkowych mas od `6e8 g`, a więc sam kod uruchamia się również w obszarze poniżej tabeli.

**Nowy test warunkowy:** zmiana wyłącznie nachylenia przedłużenia na regresję logarytmiczną z pierwszych OŚMIU rzeczywistych wierszy źródłowej tablicy, z zachowaniem wartości emisji na granicy 1e9g, daje w naszej odziedziczonej kinetyce 10-składnikowego mostu przedkrawędziowego i 7D po krawędzi różnice końcowego Xnuc rzędu 1.7–2.4e-5. Są one stabilne po zmianie tła chi_EM=0,.5,1 i po zaostrzeniu tolerancji Radau. Osobna próba `C²` zachowująca na granicy wartość i dwie pierwsze pochodne podtrzymuje ten efekt. Alternatywna regresja oraz wygładzenie są **syntetycznymi scenariuszami błędu modelu**, nie szacowanym błędem fizycznym i nie rekomendowaną zmianą wzorów autorów.

**STOP:** oryginalny program Julia 10D nie został wykonany: `julia` nie jest dostępna w aktualnym środowisku. Testy wykonano w reprodukowanym warunkowym solverze Mech-S7 10-comp preedge + 7D post-edge, z odziedziczonymi danymi archiwalnymi. Nie potwierdzono widma pochodzącego z zewnętrznego, niezależnego generatora emisji <1e9g. Wyniki nie są wielkością Yp, D/H ani kosmologicznym ograniczeniem PBH. Nie ma nowego twierdzenia matematycznego ani EXEC.

## II. Źródła i sprawdzona proweniencja

Repozytorium autora: `Fenyutanchan/Primordial-Black-Hole`; ścisły commit `d395183674cace6c9906a8911bdeb7234ba4040d`.

1. `arXiv-2509.05618/main-scan.jl`, blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`: źródłowy 10D RHS w `evolution_system!`, `AutoTsit5(Rosenbrock23())`, przejście do helu oznaczane `Yₚ` obliczane przez źródłową formułę `2*Xₙ_nuc/(1-Xₙ_nuc)`. Osobna walidacja interpretacji tej zmiennej wykracza poza obecny obrót.
2. `arXiv-2509.05618/tool_script-hadrons_from_PBH.jl`, blob `cc73432910f872d526113ce59b6204f38d0766a9`: wszystkie pięć kanałów tablicy ładowane przez liniową interpolację w `log Q,log M` z `ExtrapolationType.Linear`.
3. `arXiv-2509.05618/data/out/hadrons_from_PBH.dat`, blob `06d0883a27b108692720422294ba2baacd381a64`: źródłowa tabela 100 wierszy, 6 kolumn; pierwsze osiem wierszy przepisano jawnie do `author_table_first8_pinned_036.tsv` i porównano ze współczynnikami używanymi przez Mech-S7. Ten ośmiowierszowy plik NIE jest pełną tablicą autora i ma własny SHA256 w `QA_ROT036.json`.
4. `arXiv-2509.05618/main-scan-parameters.jl`, blob `53faee65beda383348580c28d0424188da69b660`: zakres mas początkowych `6e8 ... 1e10 g`.
5. `arXiv-2509.05618/README.md`, blob `ea52003db19307c07b4164fd4144483752d21a32`: autorzy deklarują Julia 1.12.3, `NaturalUnits` i pakiety numeryczne; uruchomienie pełnego skanu ma kosztowny profil wieloprocesowy.

Źródła online:
- https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/tool_script-hadrons_from_PBH.jl
- https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl
- https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan-parameters.jl
- https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/data/out/hadrons_from_PBH.dat

Poniższe opisy wyraźnie rozróżniają FAKT O KODZIE AUTORA od NASZEGO TESTU warunkowego i jego założeń.

## III. Metoda i ścisłe rozróżnienie modeli

W źródłowej tabeli `M1=1e9g` oznaczmy `u=M/M1`, `z=ln(u)`, `Q1_j` wartość pierwszego wiersza. **Autor:** dla `0<u<1`,

`Q_j^native(u)=Q1_j*u^(s2_j)`, `s2_j = [ln(Q2_j)-ln(Q1_j)]/[ln(M2)-ln(M1)]`.

**Test regresji:** `s8_j` otrzymuje się z MNK (`ln(Q_i/Q1)` względem `ln(M_i/M1)`) dla 8 pierwszych próbek i swobodnego wyrazu, po czym **celowo zakotwicza** się krzywą do oryginalnego `Q1_j`:

`Q_j^trial(u)=Q1_j*u^(s8_j)`. Nie przenosimy wyrazu wolnego regresji — zapewniamy identyczne Q przy u=1; zmieniamy nachylenie, więc pierwszy pochodny jet na brzegu nie jest dopasowany. To test stresowy, NIE fizycznie uprzywilejowana regresja.

**Kontrola eliminująca zarzut niezgodności pochodnych:** dla `w=.15` i `r(z)=1-exp[-(z/w)^2]`:

`Q_j^C2(u)=Q1_j*exp[s2_j*z+(s8_j-s2_j)*z*r(z)]`.

Ponieważ `z*r(z)=z³/w²+O(z⁵)`, na u=1 wartość, pierwsza i druga pochodna względem logmasy są zgodne z oryginalną kontynuacją. Zmienia się dopiero trzecia i wyższe. Nie jest to prawo fizyczne, a jedynie kontrola artefaktu krawędziowego.

Dla każdego z trzech przepisów historia do krawędzi tabeli jest identyczna (odziedziczony most Mech ROT013). Potem zmienia się **pięć kanałów hadronowych na raz**, zgodnie ze źródłową tablicą: piony, kaony ładowane, K0L, pbar, nbar. W przeciwieństwie do ROT020–035 NIE zachowujemy tu punktowej sumy pbar+nbar ani momentów; celem jest kontrola wrażliwości na łączną normę źródłowego błędu, nie świadek informacyjnej nierozróżnialności. Nie należy mieszać claim ceilings obu grup eksperymentów.

Baza Mech-S7: odziedziczone surowe dwa archiwa S6, poprawiona geometria mostu ROT013, warunkowa termika o `chi_EM ∈ {0,0.5,1}` i `eta-constant`, dwa warianty mapy reakcji `B_exec/B_sym`. Aktywna ewolucja po krawędzi oraz zanik hadronów po źródle z solvera SciPy Radau `rtol=3e-9`, `atol=rtol*1e-3` (dla ostrzejszego kontrolnego `rtol=3e-10`). Nie wykonano autorskiego `AutoTsit5(Rosenbrock23())`.

## IV. Dane i obliczenia

### IV.1 Wszystkie pięć kanałów: kontrola tabeli i nachyleń

| Kanał | `s2` (autor) | `s8` (test) | `Q_trial/Q_native` przy `M=7e7 g` | `Q_trial/Q_native` przy `M≈12.37 g` |
|---|---:|---:|---:|---:|
| naładowane piony | -1.200486 | -1.270924 | 1.2060 | 3.6058 |
| naładowane kaony | -1.196651 | -1.266333 | 1.2036 | 3.5565 |
| K0L | -1.196805 | -1.266512 | 1.2037 | 3.5581 |
| proton / antyproton | -1.204291 | -1.275581 | 1.2087 | 3.6622 |
| neutron / antyneutron | -1.204763 | -1.276094 | 1.2089 | 3.6649 |

Przy `M=.92e9g` względna zmiana wynosi jedynie 0.58–0.60%; przy `M=7e7g` 20.4–20.9%. Wartości przy ≈12.37g są **bardzo daleką ekstrapolacją**, nie niezależnie sprawdzoną tabelą Hawkinga.

### IV.2 Pełne porównanie nieliniowe — 3 tła × 2 mapy

| `chi_EM` | mapa | `Xnuc(native)` | `Xnuc(s8 trial)` | `trial-native` |
|---:|---|---:|---:|---:|
| 0.0 | exec | 0.401587336118 | 0.401604692221 | +1.73561029e-5 |
| 0.0 | sym | 0.400713370329 | 0.400737228509 | +2.38581797e-5 |
| 0.5 | exec | 0.400959518962 | 0.400976847544 | +1.73285824e-5 |
| 0.5 | sym | 0.400084966241 | 0.400108745370 | +2.37791290e-5 |
| 1.0 | exec | 0.400335638616 | 0.400352939883 | +1.73012673e-5 |
| 1.0 | sym | 0.399460510003 | 0.399484210873 | +2.37008701e-5 |

Każda wartość `Xnuc` jest wynikiem pełnej warunkowej 7D integracji po odziedziczonym 10-komponentowym moście do krawędzi; nie jest autorskim rozwiązaniem Julia 10D. Dane z `heldout_and_tight_036.csv`.

### IV.3 Ograniczenie błędu z kontroli numerycznych i replay

- Ostrzejszy Radau przy `chi=.5`: różnica w kontraście trial-native `2.8588e-14` (exec) i `2.5602e-13` (sym). Nie są to rygorystyczne majoranty całkowitego błędu ODE.
- W odrębnym replay `replay_source_extrapolation_036.py` ponownie obliczono 6 porównań dla 3 teł i 2 map, na podstawie **zapisanych tylko pierwszych 8 wierszy** oryginalnego pliku. Max absolutna różnica kontrastów od odziedziczonej siatki `1.921e-12`; w teście użyto innej metody implementacji źródła i nadpisano jedynie funkcję `source_rates` po przejściu do podtablicowego sektora. Pliki `independent_replay_036.csv`, `independent_heldout_replay_036.csv`, `QA_ROT036.json`.
- Dodatkowe źródło `C²`, `w=.15` przy chi=.5, daje `trial-native` `+1.700370822e-5` (exec) oraz `+2.320312220e-5` (sym), zamiast `+1.732858213e-5` / `+2.377912971e-5` dla surowej regresji. Zatem efekt NIE jest zdominowany przez sztuczną zmianę nachylenia dokładnie w punkcie brzegowym. To nadal scenariusz arbitralnie wygładzonej ekstrapolacji.
- Kontrola źródła w `verify_rotation_036.py` weryfikuje znane `s2` z bazy Mech, pięć `s8`, tablicowe ilorazy oraz sześć niezależnych replay i cztery wartości tight-vs-base; końcowy wynik zapisany do JSON.

### IV.4 Granice porównań

Wcześniejszy kontrast `paper-public` Mech ROT020/021 w mapie `B_exec` wynosił około `-1.46e-5`, a w `B_sym` około `+1.13e-5`. Test alternatywnego źródłowego nachylenia daje różnice od tych liczb porównywalne lub większe. Nie wolno z tego wnioskować, że rzeczywisty błąd Wu–Xu jest co najmniej tak duży ani że te kontrasty można dodać liniowo. W szczególności zmiana nachylenia obejmuje 5 kanałów naraz, a wcześniejsze eksperymenty miały inny cel i różne przestrzenie dozwolonych źródeł.

## V. Stan naukowy projektu — źródła międzykomórkowe (stan 29.10.2026)

1. **AUD1 / LT6 / Badacz**: AUD1 SELF002 wykazał, że niemal równe kwadraturowe momenty nie oznaczają tożsamych danych dla idealnego obserwatora. Mech ROT035 wykonał owner repair przez bazę Gegenbauera (źródłowy pomysł Badacza, korekta teorii LT6): symbolem dokładne 24 zera, a pełna kinetyka z niezerowym kontrastem; nadal osobna brama solvera. Badacz doc025 v2 (przedziałowy defekt i bootstrap na całych kawałkach) dotyczy wyłącznie syntetycznego modelu o strukturze Mech i oczekuje audytu; NIE uznajemy go za certyfikat naszych źródłowych trajektorii.
2. **MT14 ROT013**: programme architect zidentyfikował odrębne błędy SYSTEMATYCZNE modelu źródłowego i STATYSTYCZNE odczytu. Niniejszy ROT036 daje fizycznie niezwalidowany scenariusz systematycznego odchylenia źródła, którego nie redukuje zwiększanie liczby odczytów przy stałym modelu. Nie tworzymy z tego pomiarowej granicy PBH.
3. **KN12 / SYSS5**: GitHub/Slack receipt nie oznacza automatycznie ingestii BW. Proweniencja wejściowej tabeli, commit autora, SHA i brak native Julia run pozostają jawne.
4. **XH-S5 / PRF12 / LT6**: źródłowa zgodność mechanizmu emitowania i transportu przed przyjęciem dowolnego ograniczenia fizycznego pozostaje warunkiem przyszłej pracy. Materiał z nowych publikacji i pozostałych frontów może wskazać procedury kontroli błędu, lecz nie dostarczył jeszcze prawomocnego widma hadronowego poniżej 1e9g dla tej implementacji.

Wybrane dowody międzykomórkowe:
- https://github.com/wmakiela-tech/Nash-iw-research/blob/73723c6340655187c6127ac694891a8b5b77e68f/research/mech-s7/2026-10-29/mech_s7_rot035_crosscell_exact_moment_nonlinear_witness_owner_aud1_disposition_001.md
- https://github.com/wmakiela-tech/Nash-iw-research/blob/5f36f4a11e45436d7b7a1e3ecfbb751957554d90/research/mt14/2026-10-29/iw_mt14_rot013_scientific_programme_alignment_and_model_error_transfer_gate_001.md
- https://github.com/wmakiela-tech/Nash-iw-research/blob/58ca45d9bd5ef36c13f7ced2b0372d0199596529/research/badacz/2026-10-29/IW_BADACZ_MECH7D_RIGOROUS_SOLVER_BOUND_V2_AFTER_AUD1_ROT009_025_20261029.md
- https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt6/2026-10-29/IW_LT6_ROT009_EXACT_H_MOMENT_REPAIR_TARGET_PERSISTENCE_001_20261029.md

## VI. Decyzja naukowa i następna brama

`AUTHOR_LINEAR_LOGLOG_EXTRAPOLATION_BELOW_TABLE = SOURCE_CODE_VERIFIED`

`AUTHOR_TABLE_FIRST_ROW_MASS_1e9g = SOURCE_TABLE_VERIFIED`

`AUTHOR_SCAN_MIN_6e8g_BELOW_TABLE = SOURCE_CODE_VERIFIED`

`EIGHT_POINT_ALT_SOURCE_STRESS = NUMERIC_ODE_PASS_6/6`

`C2_EDGE_MATCHED_STRESS = NUMERIC_ODE_PASS_2/2`

`INDEPENDENT_SIX_CASE_REPLAY = PASS_WITH_MAX_2e-12_CONTRAST_DIFFERENCE`

`TIGHT_RADAU_DIFF = SMALL_BUT_NOT_A_RIGOROUS_ERROR_CERTIFICATE`

`JULIA_1_12_NATIVE_10D = NOT_EXECUTED`

`AUTHOR_BELOW_EDGE_EMISSION_PHYSICAL_VALIDATION = OPEN`

`BW_INGEST = PENDING`

`NO_PHYSICAL_Yp_DH_PBH_BOUND / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY`

**Werdykt:** bazowa implementacja źródła jest algorytmicznie zidentyfikowana. Główna nierozwiązana kwestia nie brzmi już „czy autorzy mają ekstrapolację?”, tylko „jaka jest niepewność i dziedzina ważności ekstrapolowanej produkcji hadronów?”. Dwie techniczne bramy pozostają osobne: (A) odtworzenie oryginalnego solvera Julia i porównanie na parametrach źródłowych; (B) niezależne źródłowe uzasadnienie emisji i jej błędu modelu, zwłaszcza w dziedzinie M<1e9g. W obrocie 036 nie twierdzę, że zrealizowano A lub B.

Kolejne prace na Front B powinny priorytetowo szukać oryginalnego generatora tabeli i sprawdzać jego dziedzinę masowo-energetyczną, zestaw parametrów pełnego solvera oraz minimalny niezależny błąd źródłowy. Syntetyczne projektowanie dodatkowych momentów nie zastąpi tych działań.