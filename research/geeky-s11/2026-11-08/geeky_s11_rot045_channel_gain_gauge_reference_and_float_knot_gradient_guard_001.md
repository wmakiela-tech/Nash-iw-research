---
artifact_id: GEEKY-S11-ROT045-CHANNEL-GAIN-GAUGE-KNOWN-REFERENCE-AND-FLOAT-KNOT-GUARD-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-11-08
exposure: PUBLIC
science_status: EXACT_ALGEBRAIC_GAUGE_AND_REFERENCE_GATE / FINITE_SOURCE_NUMERICAL_FALSIFIER_OF_FLOAT_KNOT_JACOBIAN / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# ROT045 — Nieznana kalibracja sześciu kanałów niszczy identyfikowalność; jedna znana referencja ją przywraca. Osobny falsyfikator gradientu na wielkich siatkach.

## 0. Poprzedni dorobek i dokładny typ źródła

ROT015–017: wadliwy `realcast` surowego surowego projektera Fourier–TT dla parzystego N, źródłowo zgodny rzeczywisty B=GA. ROT027/029: dokładny uśredniony operator pojedynczego Liego i przejścia Fourierowskie. ROT033: zmienne stabilne filtry. ROT034: ograniczenie identyfikowalności dowolnego harmonogramu z dwóch sond. ROT035–036: model sześciopoziomowy w granicy dyfuzyjnej i bramka nieznanego wspólnego wzmocnienia. ROT037: lokalne źródłowo dyskretne odwracanie sześciu sond. ROT038: nominalny dobór sześciu pasm. ROT039–040: udowodniona przedziałowo nieodporność doboru na zmianę harmonogramu przy N64. ROT041: pierwsza dokładna algebraicznie kompresja filtrów po stałych blokach. ROT042: jednostajne oszacowanie błędu Jacobianu w stosunku do modelu granicznego i bramka załamań. ROT043: lokalna dwupunktowa odwrotność i rzeczywisty skok Jacobianu. **ROT044 FIRST**: globalna bi-Lipschitzowość całej ograniczonej sześciopoziomowej rodziny w zmiennych `z=(t,t*d0,...,t*d4)` dla parzystych N>=200000, POD ZAŁOŻENIEM ZNANYCH NORMALIZACJI sześciu kanałów.

ROT045 nie przypisuje sobie tych wyników. Nowa granica: nieznane **niezależne względne kalibracje** sześciu pasm TT niszczą tę odwracalność nawet przy nieskończenie dokładnych obserwacjach. Nowa bramka dodatnia: jeden znany harmonogram referencyjny wystarcza do kalibracji względnej. Nowy niezależny falsyfikator wykonawczy: stary algorytm zmiennoprzecinkowych granic ramp może obliczyć poprawne wartości operatora, a błędny Jacobian przy dużym N.

**Korpus pomocniczy**: zachowany niezmieniony `deepseek_python_20260627_a87249.py`, SHA256 bajtów `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`. Oryginalny historyczny produkcyjny `dtc0a_runtime_v0_3_1.py` jest niedostępny. Model pełnej niezamaskowanej parzystej siatki okresowej N³, rzeczywiste TT B=GA, oryginalna trzyczłonowa Liego C=(0,cos x,0), stabilne Ealpha. Nie ma żadnego przeniesienia na maskowany historyczny h=fI K_A ani interpretację fizyczną NCDG.

Klasyczne mature host: bilinear inverse problems, group/gauge ambiguities w blind gain and phase calibration (Li, Lee, Bresler, IEEE Transactions on Information Theory 63, 822–842, 2017, DOI 10.1109/TIT.2016.2637933); Balzano i Nowak, Blind Calibration of Sensor Networks, IPSN 2007 DOI 10.1145/1236360.1236372; teoria otwartości homeomorfizmów (Brouwer invariance of domain). Są to źródła kontekstu, **nie** dowód poniższych szczególnych wzorów ani podstawa roszczenia o nowość.

## 1. Zakres i oznaczenia: sześć kanałów

Znane skumulowane poziomy dawki x_j=j*.009/5 dla j=0..5, znane pięć ramp o szybkości v=.012, sześć dodatnich czasów plateau d_j o sumie D=.25; nieznane dodatnie t. Dopuszczalne z=(t,t*d0,..,t*d4) tworzą otwarty wypukły stożek C={z0>0,z_i>0,sum_(i1..5) z_i<D*z0}. Dla N parzystego m=round(.12N²), alpha_j=N²[a_d(j/m)-a_d((j-1)/m)] w [0,1/6].

Sześć odczytów źródłowych ROT038: S={(0,+),(1,-),(1,+),(2,-),(3,+),(4,-)}; źródłowy dokładny symbol jednego uśrednionego Liego to

`Omega_i(d)=(m+1)^-1 * sum_(ell=0)^m [prod_(j<=ell)(1-4 alpha_j S_in,i)]*[prod_(j>ell)(1-4 alpha_j S_out,i)]`.

Prawidłowo znormalizowane wyjście `F_N(z)=t*Omega_N(d)`. Dla N>=200000 wszystkie sześć Omega_i jest ściśle dodatnich; wynika to bezpośrednio z dodatniości niskoczęstotliwościowych q_j i liczb dodatnich w sumie. ROT044 udowodnił globalnie na C:

`||F_N(z)-F_N(z')||_2 > c||z-z'||_2`, c=1.20e-5, wszystkie różne dopuszczalne z,z' oraz wszystkie parzyste N>=200000.

To twierdzenie zakłada **znaną kalibrację względną** i nie rozstrzyga odwracania, jeśli każdy odczyt jest mnożony przez dodatkowe nieznane `g_i>0`.

## 2. R45.1 — dokładna symetria kalibracyjna dla jednej obserwacji

Przy osobnych nieznanych wzmocnieniach obserwujemy `Y=diag(g) F_N(z)`. Dodatnia wspólna skala g jest nierozróżnialna od t, dlatego bez utraty ogólności wybieramy normalizację `prod_(i=1)^6 g_i=1`. Jest to **konwencja**, nie zmierzona kalibracja.

Niech z' dowolnie blisko z, z'≠z, i obie konfiguracje należą do C. Wyznacz sześć dodatnich liczb `r_i=F_N(z)_i/F_N(z')_i` i ich średnią geometryczną `a=(prod_i r_i)^(1/6)>0`. Ponieważ F_N jest jednorodna stopnia 1 w z, `F_N(a z')=a F_N(z')`. Nowe względne wzmocnienia `g_i'=g_i*r_i/a` spełniają:

- `prod_i g_i'=1`;
- `diag(g') F_N(a z') = diag(g) F_N(z)` **DOKŁADNIE**;
- gdy z'→z, g'→g i a z'→z.

Nowy harmonogram jest różny przy odpowiednio wybranym kierunku zmian plateau; nie jest to wyłącznie przesunięcie wspólnej amplitudy. Nie istnieje dodatni próg tolerancji nieznanej kalibracji, poniżej którego automatycznie odzyskuje się **strukturalną** jednoznaczność z jednej sześciokanałowej obserwacji. To nie znaczy, że każda faktyczna niepewność prowadzi do równie dużego błędu; mówi o braku matematycznej injektywności.

## 3. R45.2 — skończenie wiele ślepych powtórzeń nie usuwa swobody

Załóż skończone k obserwacji z tym samym nieznanym znormalizowanym wektorem g, ale z osobno nieznanymi z^(r)∈C (łącznie z ich wspólnymi amplitudami t_r). Dane `Y^(r)=diag(g)F_N(z^(r))`.

Dla N>=200000, F_N jest ciągłą injekcją z otwartej dziedziny C⊂R^6 do R^6 (ROT044); z klasycznego twierdzenia Brouwera o niezmienniczości dziedziny `F_N(C)` jest otwarty i F_N ma ciągłą odwrotność na obrazie. Wybierz dowolny wektor h>0 o `prod h_i=1`, h≠1, dostatecznie bliski 1. Dla **każdego** r wektor `diag(h)^-1 F_N(z^(r))` pozostaje w otwartym obrazie F_N(C) po wystarczającym zmniejszeniu perturbacji. Dla skończonej liczby r wystarcza wspólna dodatnia tolerancja. Definiujemy więc

`z'^(r)=F_N^-1(diag(h)^-1 F_N(z^(r)))`, `g'=g*h`.

Wtedy `diag(g')F_N(z'^(r))=Y^(r)` dla wszystkich powtórzeń, choć g'≠g i z'^(r)≠z^(r). Jest to dokładny **pięciowymiarowy lokalny gauge** kalibracji względnej w modelu bez ograniczeń sprzęgających harmonogramy pomiędzy powtórzeniami. Dodatkowe przesłanki, takie jak wspólne znane czasy, struktury podprzestrzenne lub obserwacje nadmiarowe, mogą zmienić identyfikowalność i NIE są wykluczone tym twierdzeniem.

## 4. R45.3 — jeden znany harmonogram referencyjny odzyskuje względne wzmocnienia

Niech znany będzie jeden referencyjny profil d_ref, mierzone dla niego sześć odczytów `Y_i_ref=t_ref*g_i*Omega_N,i(d_ref)`, przy nieznanym t_ref>0 i NIEZMIENNYCH g_i w dalszych pomiarach. Wszystkie Omega_ref,i>0, więc

`r_i=Y_ref,i/Omega_ref,i`, `t_ref=(prod_i r_i)^(1/6)`, `g_i=r_i/t_ref`.

Te wzory **dokładnie** wyznaczają znormalizowane g. W pomiarze docelowym korygujemy `Y_i/g_i=F_N,i(z)`, a następnie korzystamy z ROT044: z jest globalnie jedyne w C dla wszystkich parzystych N>=200000. Nie trzeba znać referencyjnego t_ref wcześniej; otrzymuje się je ze średniej geometrycznej. Nie ma gwarancji bez założenia tej samej kalibracji g pomiędzy referencją a pomiarem docelowym.

### Oszacowanie błędu referencji

Jeśli pomiar referencyjny ma relatywne zaburzenia `Y_ref,i^obs=Y_ref,i(1+e_i)`, |e_i|<=epsilon<1, definiujemy `H=(prod_i(1+e_i))^(1/6)`. Wtedy `g_hat_i/g_i=(1+e_i)/H` i niezależnie od nieznanej skali t:

`max_i |g_hat_i/g_i-1| <= 2 epsilon/(1-epsilon)`.

Przy bezszumowym pomiarze docelowym korekcja za pomocą g_hat daje odchylenie obserwacji o normie co najwyżej `[2 epsilon/(1-epsilon)] ||F_N(z)||_2`. Dla dowolnego znalezionego kandydata z_hat∈C o residualu r wobec skorygowanych danych, twierdzenie ROT044 daje

`||z_hat-z||_2 <= [r + 2 epsilon/(1-epsilon) * ||F_N(z)||_2] / (1.2e-5)`.

To syntetyczny deterministyczny bound w z, nie ocena aparatury ani jednostajny bound na same d przy t→0. Jeżeli algorytm nie znajduje kandydata wewnątrz C, z tej nierówności nie wynika wykonalność rekonstrukcji.

## 5. R45.4 — jawne źródłowo dyskretne odczyty, nie tylko analiza continuum

Niezależna implementacja z **dokładnymi ułamkami wymiernymi granic czasu** dla pełnego źródłowego iloczynu filtrów (nie przybliżenia cieplnego) została porównana z algorytmem symbolu i jego analyticznym Jacobianem.

- N=200000, zmiana wektora z o normę 0.001 w kierunku najmniejszej wartości singularnej macierzy granicznej, zmiana sześciu względnych kalibracji nie większa niż `8.32200146e-7`; sześć **dokładnie modelowo tych samych** obserwacji odtworzonych numerycznie z błędem max `5.56e-17`.
- Cztery różne nieznane historie (i amplitudy) na N=200000 z **tymi samymi sześcioma względnymi gain** o max odchyleniu rzędu `6e-9`; niezależne numeryczne odwrócenie odpowiednio przeskalowanych źródłowych odczytów daje parametry z zmianą normy od `1.30e-5` do `1.85e-5` i resztą poniżej `1e-15`.
- Referencja z nieznanym t_ref=1.37, względnymi wzmocnieniami rzędu kilku promili: wszystkie względne g i wszystkie testowane docelowe z odzyskano numerycznie przy N=200000/300000/1000000. Po dodaniu syntetycznego błędu referencji epsilon=1e-9 błąd z wyniósł około `2.14e-5`, wobec konserwatywnej gwarancji `1.67e-4`.

Testy te **nie** są pełnym wykonaniem programu źródłowego na siatce 200000³; są realizacją dokładnego matematycznie symbolu wywiedzionego z zachowanego pomocniczego kodu na sześciu niskich modach. Dosłowny kod TT wykonano niezależnie na N12/16 (test dziedziczony ROT044).

## 6. R45.5 — krytyczny falsyfikator wykonawczy `FM_FLOAT_KNOT_JACOBIAN_FALSE_SINGULAR`

Niezależny program wskazał **rzeczywisty błąd NUMERYCZNEGO Jacobianu** w odziedziczonej implementacji `rot041_compressed_core.py`, korzystającej z floatowych granic ramp. Model źródłowy i jego dokładne iloczyny matematyczne nie ulegają zmianie. Na ustalonym legalnym profilu `d=(.042013279,.041233731,.040822091,.045112967,.040733239)`, t=1.07:

| N | min singular J zmiennoprzecinkowy ROT041 | min singular J z dokładnymi granicami `Fraction` | max błąd Jacobianu |
|---:|---:|---:|---:|
| 200000 | 1.2148042e-5 | 1.5364662e-5 | .496369 |
| 300000 | 1.6507101e-18 | 1.5364662e-5 | .076223 |
| 1000000 | 2.1386710e-20 | 1.5364662e-5 | .596136 |

**Natomiast wartości samych sześciu funkcji obserwacji** obliczone dwoma metodami są zgodne do około `4.5e-16`, a niezależny Fraction-forward zgadza się z Fraction-Jacobian forward do `2.3e-16`.

Poprawne `Fraction` pochodne spełniają dla N=200000,300000,1000000 oszacowanie ROT044 w stosunku do niezależnej continuum M: odpowiednio `3.57e-10`, `1.59e-10`, `8.51e-11` wobec granic `3e-6`, `1.333e-6`, `1.2e-7`.

**Kwalifikacja**: jest to falsyfikacja **własności numerycznej implementacji gradientu** dla dużych siatek, NIE matematyczna falsyfikacja twierdzenia ROT044. Reproduktor ma osobne porównanie: (i) stary float core, (ii) niezależny Fraction-knots Jacobian, (iii) niezależny Fraction-knots forward, (iv) graniczna M. Wynik wymaga odseparowania starszej funkcji pochodnych od bezwarunkowych certyfikatów wielkich N. Nie propagować fałszywej osobliwości jako własności źródła.

## 7. Kontrole, niezależność i sufit

Sześć wykonalnych ścieżek:

1. `rot045_exact_fraction_gauge.py` — 362/362 dokładne racjonalne analogi gauge i znanej referencji; **nie** oblicza dokładnie eksponent trygonometrycznych.
2. `rot045_highprecision_continuum.py` — 41/41 kontroli 110-cyfrowej granicznej M, sześciu ślepych profili, referencji i szumu; arytmetyka wysokiej precyzji jako weryfikacja, nie ścisły certyfikat przedziałowy nowego twierdzenia.
3. `rot045_source_finite_gauge.py` — 66/66 niezależna źródłowa formuła z wymiernymi granicami, jedno- i wielokrotna gauge oraz lokalne odwracanie.
4. `rot045_reference_calibration.py` — 34/34 testy rzeczywistej matematycznej dyskretnej formuły dla trzech dużych N i znanej referencji, dodatkowo syntetyczne zaburzenia.
5. `rot045_largeN_gradient_guard.py` — 23/23 falsyfikacja numerycznego Jacobianu starego float-core kontra niezależny Fraction-core i Forward.
6. `rot044_literal_aux_source_gain.py` — **29/29 ODZIEDZICZONE ROT044** źródłowe dosłowne pełne TT N12/16, sprawdzające bazową geometrię i Lie; nie są to nowe historyczne dane, ich maksymalna względna rozbieżność `2.69644e−16`.

**RAZEM 555/555 rzeczywiście wykonanych typowanych kontroli PASS, w tym 29 odziedziczonych**. Nie jest to 555 niezależnych fizycznych eksperymentów. Pierwsza próba wykonania wysokoprecyzyjnego programu zatrzymała się na błędnym indeksowaniu wyniku SVD; pierwsza próba testu korekcji przy N300000 wykryła fałszywie osobliwy float Jacobian; obie poprawiono **przed** końcowym wynikiem, a sam fałszywy Jacobian zachowano w osobnym reproduktorze. Zamrożone źródło bez zmian.

ARCHIWUM: kompletna polska treść, sześć skryptów testowych, sześć wyników JSON i logów, trzy zachowane/reprodukowane moduły źródłowe, nowy Fraction-Jacobian, README, manifest SHA256. Szczegóły w manifeście/replay. Publiczny raport naukowy GitHub zawiera powyższą treść; skrypty/ZIP są lokalne w rozmowie Moderatora, chyba że niezależnie zapisano je w repozytorium. Niezależny referee oraz BW niepotwierdzone.

**FIREWALL**: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_NEW_TASK. Nie orzekać o historycznym maskowanym K_A, J3/K, GR/GW/PBH, skuteczności empirycznej aparatury, ani o identyfikowalności dowolnych harmonogramów bez referencji.