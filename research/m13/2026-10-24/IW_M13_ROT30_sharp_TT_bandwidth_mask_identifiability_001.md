# IW/NASH — M13 ROT30: ostry próg pasma TT dla identyfikowalności pełnego RMS z pięciu masek

**RETURN_ID:** `M13-ROT30-SHARP-TT-TENSOR-BANDWIDTH-2-VS-3-FIVE-MASK-IDENTIFIABILITY-001_20261024`  
**CELL:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**DATE:** `2026-10-24`; **PROBLEM_ID:** `P3_DTC0A_TT_MASK_COMMUTATION_AND_LOCAL_RMS_TYPING_001`.  
**CLASS:** exact elementary Fourier/Chebyshev moment theorem + sharp constructive source-native low-band TT nonmap + numerical mask/projector controls. **NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / TPE HOLD**.

## 0. Dlaczego ten obrót i pierwszeństwo innych wyników

ROT28 obliczył poprawkę geometryczną RMS za pomocą kilku masek. ROT29 ustalił ostry limit minimaksowy `L1=7` dla kasowania dwóch rzędów przy pięciu maskach i skonstruował niejednoznaczność pełnej normy dla dwóch **dodatnich gęstości energii o paśmie <=5**, wykorzystując tensory `T_xx=sqrt(6F)`. Tam **tensorowi** nie przypisywano skończonego pasma ani własności TT. ROT30 usuwa właśnie te dwie luki: kontrprzykład składa się z autentycznych, rzeczywistych, symetrycznych tensorów **TT o paśmie <=3**; równocześnie wykazuje **dodatni ostry próg jednoznaczności <=2** w tym samym precyzyjnie określonym hoście. Jest to rozszerzenie strukturalne konstruktora ROT29, nie roszczenie pierwszeństwa dla klasycznej teorii momentów.

XH-S4 ROT019 i INT8 ROT014/015 uprzednio rozdzieliły ambient versus TT-restricted Lie, projekcyjne niezamknięcie i aliasing; Geeky-S11, PRF11 i INT8 kontynuują oddzielne badania operatorowych i Sobolevowskich granic. ROT30 **nie** twierdzi, że jego pola realizują historyczne `K_A`, ani nie koryguje wniosku ROT26 o wybranym pełnym generatorze.

## 1. Twierdzenie ROT30.1: dokładny ostry próg 2 versus 3

Ustalmy nieparzyste `N >= 13`, siatkę okresową `x_j=2πj/N`, `c=(N−1)/2` oraz pięć przestrzennych masek `k=2,3,4,5,6`: `j=k,...,N−k−1` dla każdej z trzech osi. Rozważmy realne, symetryczne pola tensorowe `T(x)`, **niezależne od y,z**, z wyrazami Fouriera `|m_x|<=B`. Każdemu polu przyporządkujmy normy `R_k` dokładnie jak w zachowanym DTC0a `rms_norm` (globalny Frobenius symetrycznego tensora, wagi 2 dla pozadiagonalnych, dzielenie przez `6(N−2k)^3`).

**(a) Jednoznaczność dla B<=2.** Jeżeli dwa takie pola (w szczególności pola TT) mają identyczne pięć maskowanych RMS, to mają identyczny RMS pełnej siatki. Nie zakłada się, że same pola są równe. Dowód dotyczy wyłącznie pełnej normy.

**(b) Niejednoznaczność już przy B=3 w klasie dokładnie TT.** Dla każdej powyższej nieparzystej siatki istnieją dwa realne, symetryczne, śladowo zerowe, transwersalne pola `T_+` i `T_-` z `|m_x|<=3`, dla których `R_k(T_+)=R_k(T_-)` dla wszystkich pięciu k, ale `R_0(T_+) != R_0(T_-)`. Jest to więc **ostry próg pasma tensorowego 2/3 w zadanej klasie**. Żadne twierdzenie o wielowymiarowych niezależnych polach, innym N, innej masce lub o historycznej przestrzeni residuali `K` nie wynika stąd automatycznie.

### Dowód (a): ranga pięciu obserwacji w klasie pasma energii <=4

Gęstość energii `e(x)=|T(x)|_F²/6` jest rzeczywistym wielomianem trygonometrycznym stopnia <=`2B<=4`. Każda maska jest symetryczna względem indeksu `c`; części sinusowe gęstości dają sumę zero zarówno na wszystkich pięciu maskach, jak i na pełnej siatce. Pozostaje zatem część parzysta `p(t_j)` stopnia <=4, gdzie `t_j=cos(2π(j−c)/N)`.

Załóżmy, że różnica dwóch takich energii ma pięć zerowych **średnich** na maskach. Wówczas również pięć odpowiednich sum jest zerowych. Odjęcie sum dla sąsiednich k wymusza `2p(t_k)=0` dla `k=2,3,4,5`, bo obcięte pary węzłów mają te same `t_k`. Wartości `t_2<t_3<t_4<t_5` są różne; zatem wielomian `deg p<=4` ma postać `p(t)=A H(t)`, `H(t)=prod_{k=2}^5(t−t_k)`. W pozostałej masce k6 zachodzi `t_j>t_5`, więc **każdy** `H(t_j)>0`. Jej suma jest równa zero tylko wtedy, gdy `A=0`. To dowodzi wstrzykiwalności pomiaru na parzystych gęstościach energii stopnia <=4, a tym samym tożsamości pełnych średnich energii i norm.

### Dowód (b): jawna rodzina dwóch rzeczywistych tensorów TT o paśmie <=3

Przy powyższych `t_j`, `H`, zdefiniujmy

`lambda = [sum_{j=6}^{N−7} H(t_j)t_j]/[sum_{j=6}^{N−7} H(t_j)]`.

Mianownik jest dodatni, a `lambda > t_5`. Rozłóżmy `H(t)(t−lambda)` na dwa czynniki:

`a(t)=(t−t_2)(t−t_3)` — wielomian stopnia 2,

`b(t)=(t−t_4)(t−t_5)(t−lambda)` — wielomian stopnia 3.

Dla dowolnego `epsilon>0` niech `f_±(x_j)=a(t_j)±epsilon b(t_j)`. Ponieważ `t=cos(phase)`, `f_+` i `f_-` są **same wielomianami trygonometrycznymi o paśmie <=3**. Ustalmy pojedynczą, rzeczywistą polaryzację:

`T_±(x_j,y,z) = sqrt(3) f_±(x_j) diag(0,1,-1)`.

Ich ślad to zero. Dla niezerowego modu Fouriera `k=(k_x,0,0)`, macierz projektora poprzecznego to `diag(0,1,1)` i standardowy źródłowy `P_TT` zostawia `T_±` bez zmian, ponieważ są już transwersalne i bezśladowe. Mod zerowy też jest bezśladowy i zostaje zachowany przez źródłową regułę zero-mode. Pola są zatem **dokładnie TT** na płaskim torusie.

Ze źródłowej normalizacji `|T|_F²/6=f²` mamy

`R_k(T_+)²−R_k(T_-)² = 4 epsilon * mean_{j=k,...,N−k−1} a(t_j)b(t_j)`.

Ale `ab=H(t)(t−lambda)`. Dla k6 średnia iloczynu znika **z definicji lambda**. Każda z czterech zewnętrznych, kolejno zdejmowanych par węzłów jest pierwiastkiem `H` przy k2..5, więc średnia tego iloczynu znika na **wszystkich pięciu** maskach. Na pełnej siatce zostają natomiast cztery zewnętrzne węzły `j=0,1,N−2,N−1`, dla których `t_j<t_2<lambda`, `H(t_j)>0`, a więc `H(t_j)(t_j−lambda)<0`. W konsekwencji średnia pełna iloczynu jest **ściśle ujemna**, a pełne kwadraty RMS — i normy — się różnią. QED.

Ta konstrukcja jest nieliniowością normy dwóch **różnych** pełnych pól TT, nie skutkiem błędu projekcji TT, aliasingu stencilu, niespójności odpowiedzi historycznego źródła czy różnicy norm przy zmianie k dla *tego samego* tensora.

## 2. Weryfikacja w prawdziwych funkcjach zachowanego helpera — N=41

Kod źródłowy: `deepseek_python_20260627_a87249.py`, SHA256 `23b0ec865263c5688682425af9d4c1f9dcb9f1d582a0f2f33d99c642c176f801`. Użyto niezmodyfikowanych `rms_norm` i `apply_P_TT`. Jako amplitudę względną wybrano `epsilon=sqrt(mean(a²)/mean(b²))=5.98752788663385`, a `lambda=0.82268310396438`; ten wybór **nie** jest wymagany w dowodzie.

| k | RMS(T+) | RMS(T−) |
|--:|--:|--:|
| 2 | 2.73591798978687 | 2.73591798978686 |
| 3 | 2.81113445659128 | 2.81113445659128 |
| 4 | 2.89475647224451 | 2.89475647224450 |
| 5 | 2.98667426671591 | 2.98667426671591 |
| 6 | 3.08791711674240 | 3.08791711674240 |
| 0 (pełna) | **2.60926254179164** | **2.60968630224903** |

W pięciu maskach maksymalna bezwzględna różnica RMS wynosi `4.44e−15`, ale dla całej siatki `0.00042376045739445`, czyli względnie `0.01623930297%`. Projekcja przez niezmodyfikowany `apply_P_TT` daje `||PT_+−T_+||/||T_+||=3.97e−16` oraz `||PT_-−T_-||/||T_-||=5.08e−16`. FFT pól wykazuje brak modów `|m_x|>3` do błędu <`3e−14`.

**Dodatkowe kontrole nieparzystych siatek** `N=13,15,17,21,31,41,61`: w każdej 5/5 masek numerycznie równe, pełne RMS nierówne, macierz obserwacji stopnia 4 pełnego rzędu. Przykładowe globalne różnice RMS: N13 `0.417708`, N31 `0.00592975`, N41 `0.000423760`, N61 `0.00000968939`. To potwierdza konstrukcję, nie jest dowodem granicy fizycznej N→∞.

## 3. Stabilność dodatniego przypadku B<=2 — informacja to nie precyzja

Dla N41 macierz obserwacji gęstości energii w bazie `cos(m phase)`, `m=0,..,4`, ma rozmiar 5x5 i liczbę uwarunkowania `cond_2 ≈ 37 343.84`. Dokładny w tej modelowej klasie liniowy estymator **pełnego kwadratu RMS** ze wszystkich pięciu maskowanych kwadratów RMS ma wagi (kolejno k2..6):

`w ≈ (+6.7533960199, −11.9408396532, +9.0593418773, −3.3886875418, +0.5167892978)`,

`sum|w| ≈ 31.65905439`.

Jest jednoznaczny w klasie dokładnej rekonstrukcji składowych parzystych pasma energii <=4; przy niezależnie ograniczonych zaburzeniach każdego **kwadratu** maskowanej normy przez ε wzmacnia błąd deterministycznie najwyżej `31.659... ε`. Jest to większe od minimaksowego `L1=7` z ROT29, ale ROT29 żądał tylko asymptotycznego usunięcia dwóch pierwszych członów maski, a nie dokładnego odtworzenia każdej gęstości Fouriera stopnia 4. Są to **różne wymagania i klasy gwarancji**.

Bezpośrednia kontrola: 12 niezależnych syntetycznych realnych pól TT z wielomianami x-pasmowymi stopnia <=2 (również z sinusami) ma błąd odzyskanego pełnego **RMS²** poniżej `1.1e−14`. Natomiast dla pary TT z pasmem 3 każdy estymator oparty tylko na pięciu normach musi zwrócić tę samą wartość, mimo różnych rzeczywistych pełnych RMS. To jest ograniczenie danych, nie awaria algorytmu.

## 4. Relacja do historii projektu i granice claimu

**EARNED:** ostra identyfikowalność globalnego RMS dla realnych symetrycznych pól zależnych tylko od x o paśmie tensorowym <=2; jawny nonmap przy paśmie 3 już w pełni TT; siedem numerycznych odd-N kontroli; źródłowy bezpośredni TT PASS dla N41; odzyskiwalność dokładna o koszcie L1≈31.66 dla B<=2.

**NOT EARNED:** że analogiczny próg obowiązuje bez zmian dla pełnej trójwymiarowej klasy pól DTC0a, że konkretne historyczne `K_A` ma dwa możliwe wyniki z jednego generatora, że tensorowe pola realizują `K_A` dla historycznych `C1,C2,h`, że teoretyczny próg jest stabilną metodą dla niedokładnych CSV, że zachodzi nowe zjawisko fizyczne, lub że byte-exact oryginalny `dtc0a_runtime_v0_3_1.py` został odnaleziony. Ostatni plik nadal nie jest dostępny pomimo deklaracji SHA256 `2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084` w manifestach.

**Następna tania decyzja (warunkowa, bez tworzenia zadania):** jeśli rozważa się estymację pełnej normy z pięciu RMS bez pełnego generatora, nie należy opierać się na samej deklaracji 'smooth/TT/low-band'; potrzebny jest *jawny limit pasma energii* i budżet błędu kwadratów pomiarów. Pełny tensor źródłowy pozostaje mocniejszą informacją niż dowolne pięć jego norm.

**Original-source inputs:** zachowany helper, zamrożona tabela masek `dtc0a_mask_sensitivity_N41_v0_3_1.csv` SHA256 `4dc228e1edab9fefc219118b5ba465b817d86a934cfee4d5ae563657e3bd5f91` (nie służy do wytworzenia świadków) i pełny raport ROT29 jako bezpośredni punkt porównania. **Code:** `verify_m13_rot30.py` (NumPy+oryginalny helper) i `verify_m13_rot30_symbolic.py` (niezależne tożsamości SymPy). Maszynowe wyniki zawiera `IW_M13_ROT30_TT_bandwidth_identifiability_20261024.json`. Priorytet źródłowy: raport ROT29 / XH-S4 / INT8 / klasyczna trygonometryczna algebra rzutów i problem momentowy; **NO_NOVELTY**.

**Source/owner custody:** autonomiczny wynik M13; MT13 programme; KN11 BW; REC10 referee. Brak osobnego potwierdzonego referee pass, owner acceptance, BW ingest i EXEC. **NO_NEW_TASK / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / TPE HOLD**.

**ROUTE_TAGS:** `IWTO_MT13 IWTO_KN11 IWTO_INT8 IWTO_XH_S4 IWTO_REC10 IWTO_LT5 IWTO_SW IWTO_MODERATOR`.