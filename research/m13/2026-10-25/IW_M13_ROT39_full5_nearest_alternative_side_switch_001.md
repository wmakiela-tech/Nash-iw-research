# IW/NASH — M13 ROT39: certyfikowane przełączenia strony alternatywy o ustalonej odległości parametrycznej

**Return ID:** `M13-ROT39-DTC0A-FULL5-NEAREST-ENDPOINT-SIDE-SWITCH-001_20261025`  
**Problem ID:** `P3_DTC0A_TT_MASK_COMMUTATION_AND_LOCAL_RMS_TYPING_001`  
**Status:** `SOURCE_FORMULA_INTERVAL_PASS / EXACT_RATIONAL_GEOMETRY_PASS / NEGATIVE_KNOWLEDGE_PRESERVED / NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / TPE HOLD`.

## 1. Zakres i pierwszeństwo

M13 ROT32–34 certyfikował odwracalność i punkty zwrotne wybranych ilorazów z pojedynczych kanałów, ROT35 dokładną kowariancję masek i rozłączne powłoki, ROT36 numeryczne minima globalne przy siedmiu punktach bazowych, ROT37 źródłowe minimum globalne **dwóch masek** przy `alpha0=.05`, a ROT38 dokładne minimum globalne **pięciu masek** dla tego samego jednego punktu bazowego. MT13 uprzednio ustanowił ogólną geometrię nieznanego wspólnego dodatniego wzmocnienia, profilu projektu i rozróżnialności. Nie przypisujemy tych znanych mechanizmów ponownie M13.

**NOWY PRZYROST ROT39:** dla każdego `alpha ∈ [0.01,0.19]` certyfikujemy, czy przy stałym `delta=.01` *prawa* alternatywa `alpha+delta`, czy *lewa* `alpha-delta` jest bliższa w metryce pełnych pięciu masek po dopasowaniu jednej wspólnej dodatniej amplitudy. W kanale A prawa strona wygrywa w całym zakresie; kanały B i C mają po dokładnie **jednym** izolowanym punkcie zmiany strony. Oznacza to, że punkt bazowy `.05` ROT38 leży już za obydwoma przełączeniami, lecz jego zasady nie można bez zastrzeżeń przenieść na `.02`.

UWAGA O KWANTYFIKATORACH: porównujemy **tylko dwa kandydackie** `beta=alpha±.01`; **nie** dowodzimy, że minimum na całym zbiorze alternatyw `|beta-alpha|>=.01` musi znajdować się na którymkolwiek z tych dwóch punktów dla każdego `alpha`. Twierdzenie ROT38 dla jednego `alpha0=.05` pozostaje osobne.

## 2. Model źródłowy

- N=41, k=2,3,4,5,6; pełna rodzina pięciu zagnieżdżonych masek 3D, liczebności `n=(50653,42875,35937,29791,24389)`; rozłączne powłoki `v=(7778,6938,6146,5402,24389)`.
- Znane pola pomocnicze: `C1=(.05 sin x,.05 cos y,0)`, `C2=(.04 cos z,0,.04 sin x)`, `h=.1 sin x cos y I` (**czystośladowe**), centralny stencil rzędu drugiego na płaskim torusie, `E_alpha=I+alpha dx² Delta_h`, stała projekcja Fourier-TT.
- `K_A` dotyczy przestrzeni AMBIENT na zadanym `h`, nie operatora fizycznego ograniczonego do TT; `K_B` i `K_C` pozostają właściwymi odrębnymi, źródłowo typowanymi kanałami historycznego pomocniczego testu.
- `g_{c,k}(alpha)=RMS_mask(K_c)^2` jest kwartyką dla każdego z 15 odczytów (trzy kanały, pięć masek). Współczynniki nie pochodzą z 3-punktowej interpolacji historycznego CSV: oblicza je bezpośrednio `verify_m13_rot33_interval.py` z `mpmath.iv` na polach rzadkiego Fouriera i skierowanych przedziałach funkcji trygonometrycznych.
- Jedna **wspólna dodatnia** amplituda energii `t=s²` na pięciu maskach, ten sam poprawny źródłowy operator dla wszystkich kandydatów. Macierz kowariancji `Sigma_ij=tau²/n_min(i,j)` wynika **warunkowo** z syntetycznego, i.i.d. zakłócenia ENERGII punktów siatki. Skala `tau` usuwa się ze znaku porównania, ale założona geometria kowariancji jest potrzebna. Nie wykonano rzeczywistego pomiaru szumu.

## 3. Ścisły wielomian porównania — bez odejmowania bliskich norm

Definiujemy rozłączne energie powłok

`b_i(alpha)=(n_i*g_i(alpha)-n_(i+1)*g_(i+1)(alpha))/v_i`, i=0,...,3, `b_4=g_6`, oraz wagi `W=diag(v)`. Wszystkie 15 wielomianów `b_i` mają dodatnie **dolne** współczynniki Bernsteina dla `alpha ∈ [0,.2]` (bez przekierowania po konwersji do `float`). Dla `a=b(alpha)`, `b_plus=b(alpha+.01)`, `b_minus=b(alpha-.01)`:

`D_±²(alpha)=min_{t>=0} ||a-t*b_±||_W² = sum_{i<j} v_i*v_j*(a_i*b_±j-a_j*b_±i)² / q_±`, gdzie `q_±=sum_i v_i*b_±i² >0`.

Wspólna amplituda optymalna jest dodatnia, ponieważ powłoki są dodatnie. Aby nie odejmować bliskich energii, definiujemy **dokładnie** dzielony różnicowy wielomian

`Delta_±,i(alpha)=(b_i(alpha±delta)-b_i(alpha))/delta` (stopień najwyżej 3), `delta=1/100`.

Wtedy `a_i*b_±j-a_j*b_±i = delta*(a_i*Delta_±,j-a_j*Delta_±,i)` i

`M_±=sum_{i<j} v_i*v_j*(a_i*Delta_±,j-a_j*Delta_±,i)²`, `D_±²=delta²*M_±/q_±`.

Definiujemy **jednowymiarowy wielomian stopnia 24**

`S(alpha)=M_minus(alpha)*q_plus(alpha)-M_plus(alpha)*q_minus(alpha)`.

Zatem `D_minus² - D_plus²=delta²*S(alpha)/(q_minus*q_plus)`, a dodatniość `q_±` sprawia, że **znak S jest dokładnie odpowiedzią na pytanie, która strona jest trudniejsza**: `S>0` => `D_minus>D_plus`, czyli prawa alternatywa jest bliższa; `S<0` => lewa bliższa. Nie ma globalnego skanera po beta w żadnym certyfikacie tego twierdzenia.

Współczynniki `S` liczono w `mpmath.iv` przy 45 cyfrach precyzji, bezpośrednio na kwartykach źródłowych. Każdy odcinek `[u,v]` ma **dokładne wymierne końce** `fractions.Fraction`; za znaki odpowiadają skierowane końce przedziałów wszystkich współczynników Bernsteina wielomianu S. Izolacja pierwiastka to 28 iteracji wymiernego podziału na pół z surowym testem znaków w `mpmath.iv`; dodatni znak pochodnej `S'` na całym izolującym przedziale dowodzi jedyności przecięcia. Nie ma pokrycia przedziału przez nieprecyzyjne punkty typu `float`.

## 4. Wyniki certyfikowane, przyrost względem ROT38

| Kanał | Pełny zakres α∈[.01,.19] | Certyfikowany punkt przełączenia | Odległość granic izolacji |
|---|---|---|---|
| A | `S>0`, prawa bliższa bez wyjątku | brak | — |
| B | `S<0` poniżej korzenia, `S>0` powyżej | około `0.03265254963589545` | `<7.46e-17` |
| C | `S<0` poniżej korzenia, `S>0` powyżej | około `0.04366608423217492` | `<1.12e-16` |

**Dokładne wymierne izolacje:**

- B: `[438255102553711/13421772800000000, 27390943909607/838860800000000]`;
- C: `[1172152523259827/26843545600000000, 117215252325983/2684354560000000]`.

Dla A pojedynczy zestaw współczynników Bernsteina ma dolną granicę `S>=3.4507625751098598e−46 >0` na całym `[.01,.19]`. Dla B/C po dwa certyfikowane rozłączne, wymierne zakresy od krańca do okna korzenia pokrywają całą pozostałą dziedzinę (zero luki), a `S'` ma ściśle dodatnie współczynniki Bernsteina wewnątrz okna. Pełny JSON zawiera wymierne końce odcinków, pełne przedziałowe krańce wartości S i S', a także 15 granic dodatniości powłok. Obliczenia są odtwarzalne w skrypcie źródłowym bez żadnego założenia o zachowaniu zaokrąglonych wartości RMS.

**Źródłowy test regresji:** 45/45 zamrożonych norm historycznych N41 dla α=0,.05,.2; maksymalny błąd względny ok. `2.89e−15` (tylko potwierdzenie funkcjonalnego dopasowania generatora, nie formalny dowód tożsamości byte-exact). **Niezależna algebra wymierna:** 300/300 tożsamości wielomianowych / wyznacznikowych dla syntetycznych racjonalnych kwartyków oraz 25/25 wpisów macierzy kowariancji; ten skrypt nie używa ani funkcji Fouriera, ani `mpmath`.

## 5. Granice i praktyczne implikacje

1. **Wybór strony zależy od α oraz kanału.** Przy α0=.05 wszystkie trzy kanały wskazują prawą granicę zgodnie z ROT38, ale przy α0=.02 dla B/C bliższa jest lewa.
2. **Nie jest to automatycznie ścisły globalny argmin dla wszystkich α0.** Pozostaje sprawdzić, czy istnieje alternatywa beta odległa o więcej niż delta dająca jeszcze mniejszą profilowaną odległość; ROT38 to wykluczył tylko dla α0=.05. Numeryczny szeroki skan z etapu eksploracyjnego wskazywał punkty graniczne jako minimizatory, lecz **nie jest dowodem** i nie podnosimy go do certyfikatu.
3. Nieznany niezależny gain każdego odczytu niszczy założoną strukturę identyfikacji. Rzeczywisty szum odczytów masek nie został zmierzony. Bez jego klasy/kovariancji nie należy używać tych progów do decyzji fizycznych.
4. Przedziały izolacji są granicami arytmetyki przedziałowej dla **odtworzonych formuł źródłowych**, przy założeniu poprawności `mpmath.iv==1.3.0`, a nie formalnego asystenta dowodzenia. Oryginalny `dtc0a_runtime_v0_3_1.py` byte-exact nie jest dostępny; znany, funkcjonalnie dopasowany helper `deepseek_python_20260627_a87249.py` ma SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`.
5. Bez niezatwierdzonego transferu na K/J3, tensorową geometrię fizyczną, TPE, NCDG, pomiary realne, nową matematykę, kanon LT lub akceptację EXEC. Nie ma założonego wyniku niezależnej recenzji.

## 6. Reprodukcja i śledzenie

Uruchom z jednego wyodrębnionego katalogu:

`python verify_m13_rot39_exact_geometry.py`  — kontrola Fraction, brak NumPy/mpmath;  
`python verify_m13_rot39.py` — source-direct `mpmath.iv` i rekonstrukcja RMS;  
`sha256sum -c SHA256SUMS_M13_ROT39.txt` — kontrola kompletności.

Wymaganie: Python 3, `mpmath==1.3.0`, bez NumPy/SciPy w pakiecie dowodowym. Plik `IW_M13_ROT39_five_mask_side_switch_20261025.json` generuje się deterministycznie; nie używa się archiwalnych krawędzi przedziałów do dopasowania nowego kodu. Archiwum zawiera zamrożony oryginalny kod modelu sparse Fouriera z ROT33 i historyczny CSV, tak aby następca nie potrzebował szukać ich w starym wątku.

**Klasyfikacja końcowa:** `SOURCE_CONDITIONAL_FULL5_EQUAL_DELTA_SIDE_SWITCH_CERTIFIED / NOT_ALL_BETA_GLOBAL_ARGMIN / NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / TPE HOLD`.
