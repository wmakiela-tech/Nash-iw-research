# IW / M13 — ROT38: przedziałowo certyfikowane minimum globalne pełnego profilu pięciu masek DTC0a

**Return ID:** `M13-ROT38-DTC0A-EXACT-FIVE-MASK-GLOBAL-ARGMIN-ALPHA0P05-001_20261025`  
**Problem:** `P3_DTC0A_TT_MASK_COMMUTATION_AND_LOCAL_RMS_TYPING_001`  
**Klasa:** `EXACT_CLASSICAL_WEIGHTED_PROFILE_GEOMETRY / SOURCE_FORMULA_OUTWARD_INTERVAL_BERNSTEIN / CASE_SPECIFIC_FULL5_GLOBAL_MINIMIZER / NEGATIVE_KNOWLEDGE_PRESERVING`.  
**Status:** `PASS` warunkowo dla zdefiniowanego modelu i jednego punktu bazowego; `NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / TPE HOLD`.

## 1. Po co ROT38 i kto ma pierwszeństwo

M13 ROT23–27 odtworzył historyczną rodzinę pomocniczego DTC0a (maski, TT, źródła, granica); ROT28–31 wykazał granice identyfikowalności ogólnych pól; ROT32–34 zbadał parametry źródłowe i pary masek; ROT35 wyprowadził kowariancję masek i transformację na rozłączne powłoki; ROT36 uzyskał **numeryczne** minima globalne dla pięciu masek, a ROT37 **ścisłe** minima dla wybranych dwóch masek i tylko dolną granicę dla pięciu masek. MT13 wcześniej wyprowadził ogólną geometrię ilorazu projekcyjnego z nieznanym wspólnym dodatnim wzmocnieniem. Żaden z tych wyników nie jest w ROT38 przypisywany sobie ponownie.

**Własny przyrost ROT38:** dla pełnych pięciu masek i trzech kanałów A/B/C, przy konkretnym `N=41`, `alpha_true=0.05`, `delta=0.01`, *cały* zbiór alternatyw `beta ∈ [0,0.04] ∪ [0.06,0.2]` został wyeliminowany na korzyść jednego punktu `beta=0.06` za pomocą **źródłowej arytmetyki przedziałowej**. Nie użyto przeszukiwania β ani optymalizatora do dowodu. Po raz pierwszy w tej serii dokładne minimum globalne dotyczy **wszystkich pięciu** historycznych masek. Dodatkowo zidentyfikowano powód, dla którego naiwny pięciomaskowy dowód monotoniczności NIE działa w kanale B.

## 2. Typ źródła, operatora i modelu szumu

- Siatka okresowa `N=41`, maski sześcienne `k=2,3,4,5,6`; liczebności `n_k=(41-2k)^3`. Są to te same zagnieżdżone obserwacje energii, nie pięć niezależnych eksperymentów.
- Znane pola i generator: `C1=(0.05 sin(x),0.05 cos(y),0)`, `C2=(0.04 cos(z),0,0.04 sin(x))`, `h=0.1 sin(x) cos(y) I`. Stały projektor Fourier TT, 2. rząd centralnego różnicowania, filtr `E_alpha=I+alpha dx² Delta_h`. `K_A` liczone na **ambient pure-trace h**, a nie na TT-restricted `P h`.
- `g_{c,k}(alpha) = RMS_mask(K_c(alpha))²`, `c∈{A,B,C}`, jest wielomianem do stopnia 4. W ROT38 **każdy współczynnik** powstaje na nowo w `mpmath.iv` 45 cyfr bezpośrednio z rzadkich tensorów Fouriera oraz przedziałowych π, sin, cos, symbolu różnicowania, filtra, projekcji i przestrzennych sum na maskach. Nie jest wczytywany z zaokrąglonego JSON ROT32.
- `Y_k=t g_{c,k}(alpha)+epsilon_k`, jedno nieznane wspólne dodatnie `t=s²`. Dla statystycznej skali z ROT35/36 zakłada się **syntetyczny** i.i.d. addytywny szum ENERGII każdego voxela o wspólnej wariancji `tau_c²` i `tau_c=0.01*g_{c,2}(0.05)`. Szum fizyczny nie został zmierzony. Monotoniczność i argmin w jednostkach nieskalowanej energii nie potrzebują gaussowskości; skala τ służy prezentacji.
- Zachowane źródło odpowiada pomocniczemu `deepseek_python_20260627_a87249.py` o SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`, ale **nie zachowano** bajtowo oryginalnego `dtc0a_runtime_v0_3_1.py`. Weryfikacja dotyczy odtworzonej rodziny, nie niedostępnego oryginału.

## 3. Algebra pięciu masek — bez numerycznego optymalizatora

Niech `n=(50653,42875,35937,29791,24389)` i `v=(7778,6938,6146,5402,24389)`. Przejście liniowe z pięciu maskowanych średnich energii `g=(g_2,...,g_6)` na pięć niezależnych średnich energii powłok `b=B g` ma postać

\[
 b_i=\frac{n_i g_i-n_{i+1}g_{i+1}}{v_i}\ (i=0,...,3),\quad b_4=g_6.
\]

Dla macierzy `W=B^T diag(v) B = Σ^{-1} tau²` profil odległości przy prawdziwym `a=b(alpha_0)` i kandydującym `b=b(beta)` wynosi

\[
 D^2(\beta)=\min_{t\ge0}\|a-tb(\beta)\|_W^2
 = \|a\|_W^2 - \frac{p(\beta)^2}{q(\beta)},
 \quad p=a^T Wb,\ q=b^T Wb.
\]

Wszystkie pięć średnich energii powłok posiada **dodatnie przedziałowe obwiednie Bernsteina** dla całego `alpha∈[0,0.2]`. Stąd `p>0`, `q>0`, a optimum amplitudy jest ściśle dodatnie.

Kluczowy wielomian pochodnej to

\[
 H(\beta) = p'(\beta)q(\beta)-\tfrac12 p(\beta)q'(\beta),
 \qquad \frac{d}{d\beta} D^2(\beta)
 = -\frac{2p(\beta)H(\beta)}{q(\beta)^2}.
\]

**Ważna kontrola niezależna od DTC0a:** tożsamość jest równoważna skończeniewymiarowej tożsamości Lagrange'a

\[
 a_2 q-p^2 = \sum_{i<j} v_i v_j(a_i b_j-a_j b_i)^2,
\]

i tożsamości na `H` w postaci sumy iloczynów wyznaczników dwuwierszowych. Skrypt wyłącznie `fractions.Fraction`, bez NumPy, sprawdza na 60 wymiernych rodzinach kwartyków każdą z trzech tożsamości wielomianowych (180/180) oraz wszystkie wpisy algebry kowariancji i macierzy odwrotnej (50/50).

## 4. Certyfikaty źródłowe znaków i globalne rozstrzygnięcie

Współczynniki wielomianu `H` zostały przeliczone z bezpośrednich przedziałowych kwartyków. Poniżej podano konserwatywne zakresy **wszystkich współczynników Bernsteina** wielomianu `H` na wskazanych przedziałach β. Są to zakresy diagnostyczne; dokładne kontrole znaku wykonano na przedziałach `mpmath.iv`, zanim dokonano konwersji do float:

| Kanał | Lewy przedział ze znakiem H>0 | Minimalna dolna granica H | Prawy przedział ze znakiem H<0 | Maksymalna górna granica H |
|---|---|---:|---|---:|
| A | [0,0.04] | +5.87969e−33 | [0.06,0.2] | −5.78093e−33 |
| B | [0.02,0.04] | +1.45992e−45 | [0.06,0.2] | −4.30205e−45 |
| C | [0,0.04] | +1.36288e−41 | [0.06,0.2] | −9.38196e−41 |

**Kanały A i C:** `H>0` na całym lewym przedziale oznacza `D²'<0`: najmniejsza wartość po lewej to `D(0.04)`. `H<0` po prawej oznacza `D²'>0`: najmniejsza wartość po prawej to `D(0.06)`. Bezpośrednia analiza przedziałowa pochodząca z operatora wykazuje `D(0.04)>D(0.06)`, więc globalny minimizer to `0.06`.

**Kanał B wymaga dodatkowego kroku:** `H_B(0)<0`; jego znak nie jest dodatni na całym `[0,0.04]`, więc nie wolno twierdzić, że odległość pięciomaskowa jest tam monotoniczna. Na `[0.02,0.04]` znak jest dodatni, zatem minimum tej części jest przy `0.04` i jest większe niż `D(0.06)`. Dla `[0,0.02]` stosujemy ostrą nierówność odwzorowania pomiarów: pełne pięć masek ma odległość profilowaną **nie mniejszą** niż para 5/6 przy tej samej kowariancji. Stosunek energii B dla 5/6 jest źródłowo i przedziałowo ściśle monotoniczny (certyfikat dodatnich współczynników Bernsteina jego pochodnej). Zatem `D_full5(alpha0,beta)≥D_pair56(alpha0,0.02)` dla wszystkich `beta∈[0,0.02]`. Dolna granica pary wynosi `1036.9450537323642 τ_B`, znacznie ponad `D_full5(0.06)=578.077188549044 τ_B`. Po prawej `H_B<0` i minimum pozostaje przy `0.06`. Dowód obejmuje wszystkie β i nie opiera się na skanowaniu.

**Wynik globalny** (`alpha0=0.05`, `Δ=0.01`, odległość w jednostkach syntetycznego τ kanału):

| Kanał | Odległość przy β=0.04 | **Ścisłe minimum przy β=0.06** | Margines lewego kandydata |
|---|---:|---:|---:|
| A | 1.457860964379738 | **1.453698716557357** | 0.004162247822381 |
| B | 694.749079786020 | **578.077188549044** | 116.671891236976 |
| C | 111.892810285676 | **109.870070948422** | 2.022739337254 |

Granice `D(0.06)` są w JSON zapisane zarówno w ludzkim formacie dziesiętnym **z zachowanymi skierowanymi krańcami**, jak i jako **dokładne dwójkowe końce przedziału**, aby float nie ukrył szerokości przedziałowej (~1e-38 w jednostkach τ).

Wynik ROT36 (numeryczny, niecertyfikowany) wyniósł odpowiednio `1.4536987165617488`, `578.0771885490373`, `109.87007094842295`, czyli zgodność z ROT38 do ≤`6.8e−12` w jednostkach τ. Jest to kontrola spójności, a nie część dowodu.

## 5. Co można, a czego nie można wnioskować

- Dla **tego jednego bazowego alpha0=0.05**, tego jednego `N=41`, pięciu sześciennych masek, zadanego modelu źródła i wspólnego dodatniego gainu: `argmin_beta D_c(alpha0,beta)=0.06` w ograniczonym zbiorze alternatyw; c∈{A,B,C}. To jest **GLOBALNY** wynik, nie lokalna informacja Fishera.
- Przy syntetycznym szumie pięciowymiarowego Gaussa promień 95% ma `sqrt(chi2_5(.95))≈3.32724`; warunek dostateczny rozłączności dwóch takich kul to `D>6.65447`. Kanały B i C spełniają go w tej rodzinie, A nie. **Nie jest to** zmierzony błąd i nie porównuje jakości fizycznych detektorów.
- Nie dowiedziono globalnego argmin **jednakowego dla wszystkich** `alpha_true∈[0,0.2]`. Nie dowiedziono żadnej własności nieznanych generatorów, niezależnych gainów, ogólnych pól TT, innych stencili, parzystych siatek, ruchomej projekcji TT czy fizycznej kowariancji. Szczególnie B ma rzeczywisty defekt monotoniczności odległości po lewej stronie.
- Oryginalny historyczny produkcyjny runner DTC0a nadal nie jest bajtowo dostępny. `mpmath.iv` zakładane jako skierowanie poprawne; to **komputerowo wspomagany dowód warunkowy dla formuł**, nie formalny system dowodzenia twierdzeń.
- Wynik nie jest dowodem nowego prawa fizyki ani nową matematyką wobec klasycznej geometrii GLS/projekcji; brak fizycznego upgrade K/J3/NCDG/TPE. Bez samodzielnej recenzji i EXEC wynik nie podlega kanonizacji.

## 6. Reprodukcja i przechowanie

Pełne archiwum zawiera ten raport, `verify_m13_rot38.py` (źródłowy przedziałowy), `verify_m13_rot38_exact_geometry.py` (niezależne Fraction), `verify_m13_rot33_interval.py` (zamrożona poprzednia biblioteka rzadkiego źródła), oryginalny zachowany helper, historyczny N41 CSV, arkusz wyników ROT36 do wyłącznie porównawczej kontroli, `IW_M13_ROT38_five_mask_exact_argmin_20261025.json`, README, logi odtwarzania i sumy SHA256.

W rozpakowanym katalogu: `python verify_m13_rot38_exact_geometry.py`, `python verify_m13_rot38.py`. Pakiet wymaga `mpmath==1.3.0`; skrypty nie potrzebują SciPy/NumPy. JSON powstaje deterministycznie. Reprodukcja powinna jawnie sprawdzić sumy SHA256 i identyczność wygenerowanego JSON.

**Gate:** `SOURCE_CONDITIONAL_FULL5_ARGMIN_PASS / NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / TPE HOLD`.