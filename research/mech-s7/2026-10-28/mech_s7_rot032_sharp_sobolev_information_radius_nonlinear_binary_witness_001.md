artifact_id: MECH-S7-FRONTB-SHARP-SOBOLEV-INFORMATION-RADIUS-NONLINEAR-BINARY-WITNESS-032_20261028
exposure: PUBLIC
claim_ceiling: EXECUTED_CONDITIONAL_FINITE_SOURCE_GALERKIN_SHARP_LINEAR_RADIUS_AND_ACTUAL_NONLINEAR_TWO_SOURCE_MINIMAX_WITNESS_NO_PHYSICAL_ADMISSION
sync_state: GITHUB_PENDING_BW_INGEST
return_id: MECH-S7-FRONTB-SHARP-SOBOLEV-INFORMATION-RADIUS-NONLINEAR-BINARY-WITNESS-032_20261028
owner_cell: IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7
problem_id: P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001
source_lock: Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d
status: EXECUTED_CONDITIONAL_SCIENTIFIC_TEST_NO_EXEC

# Mech-S7 ROT032 — Sharp finite-basis H² source-information radius and nonlinear binary witness

**28 października 2026.** Owner/autor obliczeń: Mech-S7, `IW_MECH_LINEAGE_001_SUCCESSOR_06`. **SCOPE:** syntetyczne, dodatnie kontynuacje widm pbar/nbar poniżej krawędzi tabeli Wu–Xu; poprawiony preedge transport z ROT013 i **warunkowa** kinetyka 7D po krawędzi; NIE oryginalny author-native solver Julia10D; NIE źródłowo uprawniona emisja hadronów M<1e9g; NIE Yp/DH/ograniczenie PBH. Wszystkie cyfry i funkcjonały dotyczą tej klasy.

## 1. Co jest nowe względem dojrzałej teorii i własnych obrotów

Odejmowanie prior art: wzór Riesz/Cauchy–Schwarz na normę funkcjonału ograniczonego do jądra skończonych momentów, kwadratowa metryka Sobolewa oraz dwupunktowa granica minimaksowa to klasyczne konstrukcje, **bez roszczeń do nowego twierdzenia**. Własne Mech ROT021 wyznaczyło funkcję adjoint końcowego Xn; ROT023–024 wykazały, że wiele momentów nie wystarcza; ROT025–029 rozdzieliły przenoszalność między mapami i tłami od błędu operatora; ROT030 rozszerzył bazę; ROT031 wykazał artefakt regularizacji sin⁴ i zbudował globalne C³ źródło o małej odpowiedzi Xn. ROT032 **nie powtarza** poszukiwania dowolnego prawie zerowego kierunku: oblicza **najgorszy** możliwy kierunek przy dokładnie tym samym budżecie krzywizny i następnie sprawdza oba jego znaki w faktycznych równaniach kinetycznych.

Źródło upstream: `Fenyutanchan/Primordial-Black-Hole`, git commit `d395183674cace6c9906a8911bdeb7234ba4040d`, surowe cztery gałęzie archiwalne Mech-S6. Tabela autora `arXiv-2509.05618/data/out/hadrons_from_PBH.dat` ma dane tylko dla M≥1e9 g; wszystkie sztuczne zmiany w tym raporcie obejmują M∈[7e7,9.2e8]g. Wykorzystany warunkowy model z ROT013/020/021/024/031 nie zatwierdza tej ekstrapolacji fizycznie.

## 2. Zadanie matematyczne: kontrola momentów i krzywizny, nie tylko wybranego kierunku

Niech `u=M/1e9g`, `z=ln u`, `L=ln(0.92/0.07)` i `x=2(z-zmid)/L∈[-1,1]`. Użyto dokładnie rodziny 11 globalnych bazowych funkcji C³ z ROT031,

`phi_j(z) = (1-x²)^4 P_j(x)`, `j=0,...,10`, zero poza nośnikiem.

`f(z)=sum c_j phi_j(z)` określa **bezwzględną** zmianę udziałów w sumie źródeł antynukleonowych:

`Qp'(u) = Qp(u) + [Qp(u)+Qn(u)] f(ln u)` oraz
`Qn'(u) = Qn(u) - [Qp(u)+Qn(u)] f(ln u)`.

Zatem `Qp'+Qn'=Qp+Qn` **algebraicznie w każdym M**; przy końcach nośnika f i pochodne do 3. rzędu zanikają. Wymuszono trzy komowujące momenty każdego gatunku, `C c=0`, tj.

`∫_{ln .07}^{ln .92} u³ [Qp(u)+Qn(u)] z^j f(z) dz=0`, `j=0,1,2`.

Wspólna bezwymiarowa metryka gładkości dla zmian *udziału źródła* to norma pół-Sobolewa `||f''||_L²(dz) = [∫|d²f/dz²|² dz]^{1/2}`. Budżet `R=11.435960696834389` dobrano jako **dokładnie normę H²** kształtu `0.15*f_ROT031`, bez sztucznego ułatwiania problemu poprzez dopuszczenie mniej gładkich źródeł.

Każda z dwóch map `m∈{B_exec,B_sym}` ma w nominalnym tle χ_EM=.5 liniową odpowiedź `ell_m(c) = b_m^T c`, gdzie b pochodzi z wcześniej wykonanego target adjoint i jawnie interpolowanych danych na z, a source-rate Jacobian = `(Qp+Qn)²/(Qp Qn)`. Mierzona wielkość to odchylenie końcowego Xn przy stałym T_nuc.

Zapiszmy `G2_ij=∫phi_i'' phi_j'' dz`, `Z` — kolumnową bazę jądra `C`, `H=ZᵀG2 Z`, `g=Zᵀb`. W skończonej przestrzeni o dodatnio określonym H:

`sup_{Cc=0, cᵀG2c≤R²} |bᵀc| = R sqrt[gᵀH^{-1}g]`.

Osiągnięty kierunek ma współczynniki

`c* = R·Z·H^{-1}g / sqrt[gᵀH^{-1}g]`.

Jest to **ostre** zdanie dla danego 11-wymiarowego podmodelu, zadanego interpolowanego operatora i zadanego kwadratowego ograniczenia (wartość liczbowa podlega kwadraturze). Nie jest to górny limit dla wszystkich funkcji C³, wszystkich widm fizycznych ani dla nieliniowego układu. Zerowanie momentów jest numeryczne, nie arbitralnie dokładne po zastosowaniu niezależnej kwadratury.

## 3. OSTRE wyniki liniowe i niezależny audyt prymalne–dualne

| Target (χ_EM=.5) | R | Wartość liniowego supremum | Reszta dualna w pierwotnej kwadraturze | Test H² |
|---|---:|---:|---:|---:|
| `B_exec` | 11.4359606968 | **5.72547461749e−4** | 4.71e−17 | ||f''||=R |
| `B_sym` | 11.4359606968 | **2.16589567135e−4** | -8.94e−19 | ||f''||=R |

Przy niezależnej kwadraturze **1536-punktowej** wyniki supremum różniły się względnie o `4.79e-10` dla `B_exec`, `3.75e-9` dla `B_sym`. Niezależne reszty trzech momentów mierzone jako `|∫δQ z^j u³ dz|/∫|δQ z^j u³|dz` wyniosły maksymalnie `1.171e−12` (`exec`) oraz `8.701e−14` (`sym`). Te ostatnie liczby, a nie tylko reszty macierzy projektującej (~1e−15), stanowią granicę kontrolowanej dokładności równych momentów.

W rodzinie 10,11,13,15 globalnych modów, przy identycznym R, liniowy supremum `B_exec` odpowiednio `5.6979e−4`, `5.7255e−4`, `5.9944e−4`, `6.1808e−4`: 11-wymiarowej wartości **nie** wolno uważać za granicę dla dowolnie bogatych widm. To nie błąd spójności — poszerzenie przestrzeni daje potencjalnie większy supremum.

**Dodatniość nie jest tylko obserwacją w węzłach:** dla obu kierunków i obu znaków użyto 200001 równych próbek x∈[-1,1], bazowa frakcja Qp/(Qp+Qn) jest jawną logistyką w x. Dla wielomianu p stopnia 18 zastosowano nierówność Markowa `||p'||∞ ≤18² ||p||∞` wraz z oszacowaniem pełnego supremum z gęstej siatki; po dodaniu pochodnej frakcji bazowej konserwatywne dolne oszacowanie udziału każdego gatunku **pomiędzy próbkami** wyniosło `0.02223405` (`exec`) i `0.03409358` (`sym`). Są to dodatnie marginesy dla przyjętych liczbowych współczynników, nie formalny certyfikat arytmetyki przedziałowej wszystkich parametrów źródłowych.

## 4. Rzeczywiście wykonana nieliniowa kinetyka — dwa znaki źródła

Wykorzystano źródło `public` z podmienionym względnym udziałem pbar/nbar, przy zachowanej sumie punktowej; papierową gałąź, wszystkie pozostałe kanały, mapy, gospodarkę energii, momenty oraz tło χ_EM=.5 pozostawiono bez zmian. Źródła `+c*` i `−c*` mają **te same momenty w wyżej zmierzonej dokładności**, taką samą sumę funkcji emisji Qp+Qn, tę samą normę H² i te same dane na granicy tabeli. Różni się wyłącznie rozkład emisji pomiędzy dwa gatunki w funkcji masy. Warunkowe preedge10 + subedge/postsource7D zostały ponownie zintegrowane `Radau rtol=3e−9`, z osobną kontrolą `3e−10` przy słabszej amplitudzie.

| Mapa | Xnuc (bez perturbacji) | Xnuc (+pełna amplituda) | Xnuc (−pełna amplituda) | Przedział wyników |
|---|---:|---:|---:|---:|
| `B_exec` | 0.400959518965593 | 0.401532078747270 | 0.400386812623339 | **1.14526612393e−3** |
| `B_sym` | 0.400084966167165 | 0.400301539601712 | 0.399868355214440 | **4.33184387272e−4** |

Z **nierówności trójkąta** dla wspólnego przewidywania `yhat` i dwóch możliwych stanów `y+`, `y−` wynika `max(|yhat−y+|,|yhat−y−|) ≥ |y+−y−|/2`. Dla każdej metody, która zna wyłącznie trzy momenty każdego gatunku, całkowitą funkcję Qp+Qn, normę H², pozostałe dane modelu i z góry zadany budżet R, ale nie zna rozdziału kanałów, istnieje na tej *konkretnej dwuźródłowej parze* wymuszony maksymalny błąd:

* `B_exec ≥ **5.72633061966e−4**`;
* `B_sym ≥ **2.16592193636e−4**`.

Wartość ta jest ścisłym ograniczeniem typu two-point dla danych **wykonanych numerycznie**; nie jest górnym błędem solvera, nie jest zdaniem o dostępnych rzeczywistych danych emisji hadronowej i nie obejmuje pełnego zbioru historii kosmologicznych.

**Kontrola reżimu liniowego i dokładności:** przy 20% budżetu R, `B_exec`: ΔXn(+0.2)=`+1.14507245070e−4`, ΔXn(−0.2)=`−1.145131085998e−4` wobec liniowych ±`1.14509492350e−4`. `B_sym`: ΔXn(+0.2)=`+4.33171842932e−5`, ΔXn(−0.2)=`−4.33186850169e−5` wobec ±`4.33179134270e−5`. Przy `rtol=3e−10` największa różnica kontrastu ΔXnuc dla sześciu odpowiednich stanów to `5.680e−13` (`exec`) i `1.074e−13` (`sym`). W pełnym budżecie R różnica z liniowym wynikiem wynosi odpowiednio ~1.6e−7 i ~2.1e−8 dla najbardziej odchylonego znaku; nie deklarujemy uniform-nieliniowego bound z liniowej metody.

**Kontrafaktyczny wniosek dla ROT031:** kształt dobrany jako „prawie niewidoczny” miał dla χ=.5 rzeczywistą odpowiedź nieliniową ~3.5e−10 `exec`/~1.1e−10 `sym`, mimo identycznego R. Odpowiedź przeciwnego, target-worst-case kształtu jest w tym samym syntetycznym modelu około sześciu rzędów większa. Pojedyncza demonstracja bardzo gładkiej ścieżki źródła z małym Xn nie jest gwarancją **jednostajnej** wystarczalności statystyk momentowych.

## 5. Granice uwarunkowania, błędu operatora i statusu fizycznego

Wartość liczbowa supremum jest liczona przy **ustalonej**, interpolowanej funkcji adjoint: zmiana operatora `ell→ell+δell` zmienia normę ograniczonego funkcjonału nie więcej niż `R ||δell||_{(H²,ker C)*}`, co wynika z nierówności trójkąta. W ROT029 nie uzyskano niezależnej, fizycznej granicy błędu operatora; dlatego nie certyfikujemy realnego źródła ani prawdziwej kosmologicznej przewidywalności. Kontrola dwóch kwadratur jest kontrolą numeryczną **wewnątrz** tego warunkowego operatora.

Dodatkowe ograniczenie: w praktycznym pomiarze samo źródło może być opisane przez inne statystyki (np. pełne widmo czy niezależne dane gatunkowe), których obecne zadanie celowo nie udostępnia. Binary minimax twierdzi tylko brak wystarczalności *określonego* podsumowania, nie niemożność rekonstrukcji z innych źródeł.

STOP: `PINNED_AUTHOR_SOURCE` / `ORIGINAL_JULIA_10D_NOT_EXECUTED` / `PHYSICAL_HADRON_Q_BELOW_1e9G_NOT_VALIDATED` / `NO_PHYSICAL_Yp_DH` / `NO_PBH_BOUND` / `NO_CANON` / `NO_EXEC_SIGN` / `NO_NOVELTY` / `BW_PENDING`.

## 6. Reprodukowanie, dowody zapisu

`compute_sobolev_information_radius_032.py` buduje przy stałym R macierze momentów, G2 i funkcjonały adjoint; wyznacza dokładną dualną formułę i kierunki dla n=10,11,13,15. `independent_primal_dual_checks_032.py` niezależnie całkuje funkcjonały/momenty na 1536 węzłach i sprawdza **międzywęzłową** dodatniość nierównością Markowa. `test_adversarial_sobolev_ode_032.py` wykonuje pełną warunkową integrację kinet. przy χ=.5, mapach exec/sym i amplitudach {0,±.2}/{0,±1}, kontrola {0,±.2} z rtol3e−10. `finish_sobolev_audit_032.py` scala wyniki i dwupunktową dolną granicę.

**Czyste odtworzenie:** niezależna kwadratura kontrolna daje identyczne bajty CSV; w osobnym katalogu trzy stany `B_exec` przy ε∈{0,±.2} odtworzyły 8 niezależnych pól (Xnuc,Xcut,ΔXnuc,ΔXcut,liczby kroków, przewidywany wynik i reszta) bez różnicy binarnej w odczycie float.

Archiwum `MECH_S7_ROTATION_032_REPRODUCIBILITY_20261028.zip` zawiera oryginalne archiwa 4 gałęzi Wu–Xu z Mech-S6, komplet modułów zależnych ROT031/013/020/024/030, wszystkie wykonane skrypty i wyniki 032, logi, raport, manifest SHA256. Wymaga `python3`, `numpy`, `scipy`; nie wymaga prywatnego dostępu do Drive/Slack/GitHub do odtworzenia *warunkowej* kinetyki. `GITHUB_PUBLICATION != BW_INGEST != INDEPENDENT_REFEREE_PASS != OWNER_ADOPTION != EXEC`. Żadna ingestia BW nie została potwierdzona.