# IW / M13 — ROT20: identyfikowalność kwadratowego składnika `E_lin` z norm RMS DTC0a

**RETURN_ID:** `M13-ROT20-DTC0A-ALPHA-NORM-IDENTIFIABILITY-AND-QUARTIC-CERTIFICATE-001_20261023`  
**CELL:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**DATE:** 2026-10-23  
**CLASS:** exact algebraic source-helper theorem + full frozen-CSV postprocessing + constructed non-identifiability witnesses; **no original-runner replay**.  
**STATE:** `EXACT_CONDITIONAL_HELPER_MATH / 18_TRIPLETS_VERIFIED / RUNTIME_BYTE_EXACT_MISSING / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / TPE HOLD`.

## 0. Związek ze stanem nauki, a nie drugi raport o plateau

ROT18 wykazał problem ruchomego obszaru maski RMS w refinacji siatki. ROT19 oddzielił 14 wymuszonych algebraicznie testów amplitudy od kontrastów klasy pól. Obecna praca bada **inny, ortogonalny limit wnioskowania**: trzy zapisane wartości norm przy `alpha=0,.05,.2` NIE identyfikują składnika dwukrotnego działania `E_lin` w tensorze residualu. Nie obalamy samych danych ani obserwowanego plateau `K_A` — rozdzielamy skan norm od skanu tensorów.

MT13 w raporcie programowym z 22 X 2026 utrzymuje DTC/NCDG jako pojedynczy poprawnie typowany obszar walidacji (`P3`, M13/KN11), z zakazem awansu claims bez źródła i niezależnej recenzji. Obecny obrót nie zastępuje MECH-S7/MT13/KN11/REC10.

**Źródła pierwotne tego audytu:** `dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv` (18 wierszy: sześć N × trzy alpha), manifest `dtc0a_oddN_sparse_convergence_N31_to_N41_manifest.json` (`stencil_order=2`, `E_mode=E_lin`, `interior_k=3`), oraz retained helper `deepseek_python_20260627_349584.py`. Manifest deklaruje nieudostępniony bajtowo historyczny `dtc0a_runtime_v0_3_1.py` z SHA256 `2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084`. Skript helper NIE jest tożsamy z historycznym runtime.

## 1. Dokładna algebra — dwa zastosowania `E_lin`, wielomian tensorowy stopnia najwyżej 2

Dla jednej ustalonej siatki N, `dx=L/N`, jednego pola tensorowego h i wektorowych generatorów C1,C2 oraz ustalonego `order`, definiujemy `S_N=dx² Delta_N`. Zachowany `apply_E` realizuje dokładnie

`E_alpha=I+alpha*S_N`.

Niech `L_i` oznacza liniowy (w tensorze) dyskretny operator `lie_derivative_tensor(C_i, .)`, `L_[1,2]` zaś analogiczny operator dla dyskretnego komutatora generatorów. Ustalamy `T_i(alpha)=L_i E_alpha`; `P` to stały liniowy projektor TT. Historyczny helper definiuje

`K_C(alpha)=[T_1(alpha),T_2(alpha)]h - L_[1,2] E_alpha h`,  
`K_B(alpha)=P K_C(alpha)`,  
`K_A(alpha)=[P T_1(alpha),P T_2(alpha)]h - P L_[1,2] E_alpha h`, gdzie symbol ostatniego komutatora oznacza dokładnie zagnieżdżone wywołania `projected_T` w helperze, nie nowe abstrakcyjne twierdzenie o reprezentacji.

Każde wyrażenie zawiera **co najwyżej dwa czynniki `E_alpha`**: dlatego dla `j∈{A,B,C}` istnieją tensory U_j,V_j,W_j (zależne od N, pól, maski i wszystkich pozostałych operatorów, ale NIE od alpha), takie że

`K_j(alpha)=U_j+alpha V_j+alpha² W_j`.  **(ROT20.1)**

Przykładowo `W_C=(L_1 S_N L_2 S_N-L_2 S_N L_1 S_N)h`, `W_B=P W_C`, a w torze projektowanym `W_A=(P L_1 S_N P L_2 S_N-P L_2 S_N P L_1 S_N)h`. Obowiązuje wyłącznie dokładnie zadeklarowany kontrakt helpera z jedną stałą maską i bez przeliczenia pól wraz z alpha.

Kod RMS sumuje moduły kwadratów sześciu niezależnych komponentów symetrycznego tensora, z mnożnikiem 2 dla składowych pozadiagonalnych i stałym mianownikiem `6*n_nodes`. Stanowi więc **stałą normę Hilbertowską** na tensorach po tej samej masce. Stąd

`g_j(alpha)=||K_j(alpha)||_RMS²`

jest wielomianem w alpha stopnia **co najwyżej 4**, którego współczynnik przy `alpha⁴` jest dokładnie `||W_j||_RMS²` (nieujemny).

## 2. Co dają wyłącznie trzy wartości norm: dwa przeciwne dokładne modele

Niech na jednej siatce `a=0.05`, `b=0.2`, `t=a/b=1/4`; niech `r0=||K(0)||`, `ra=||K(a)||`, `rb=||K(b)||`. Przy założeniu **afinicznego wektorowego** residualu (W=0) konieczne i wystarczające do istnienia dwóch wektorów `u,v` w R² o normach `r0,rb`, aby `||(1-t)u+t v||=ra`, są nierówności

`|(1-t)r0-t rb| <= ra <= (1-t)r0+t rb`.  **(ROT20.2)**

Są to dokładnie granice trójkąta. Bez założenia afiniczności, nie wymusza się ich a priori, lecz można je wykorzystać jako **falsyfikator** hipotezy W=0 dla dostępnych samych norm.

**Weryfikacja CSV:** wszystkie **18 z 18** trójek (`N=31..41` co 2 × `K_A,K_B,K_C`) spełnia ROT20.2 ściśle. Istnieje dla każdej trójki *dokładna* trajektoria afiniczna `K_aff(alpha)=(1-alpha/b)u+(alpha/b)v`, z `W_aff=0`, której normy w alpha=0,a,b pokrywają wartości zapisane.

Jednocześnie te same trzy normy zawsze wyznaczają interpolacyjny **wielomian skalarny** `q(alpha)=r0+c1 alpha+c2 alpha²`; przy wektorze jednostkowym e tensor `K_quad(alpha)=q(alpha)e` ma te same trzy normy w punktach pomiarowych. Dla wszystkich 18 trójek `c2!=0`: istnieje więc również konstrukcja z `W_quad=c2 e !=0`. Przykładowe `q(alpha)` pozostają dodatnie na badanym odcinku alpha∈[0,.2], lecz wystarczają już wartości w trzech punktach.

W szczególności przy N=31 w kanale K_A:

`r0=3.788529759260593e-5`,  
`ra=3.764756853208360e-5`,  
`rb=3.694723525796834e-5`.

Trajektoria afiniczna z `||u||=r0`, `||v||=rb` i kątem u-v **około 1.73977°** odtwarza te trzy normy oraz ma dokładnie `W=0`. To *hipotetyczna* geometria wektorów, nie zmierzony kąt rzeczywistych residuali. Równocześnie skalarna trajektoria

`q(alpha)=3.788529759260593e-5 - 4.77600438953e-6 alpha + 4.28463581724e-7 alpha²`

odtwarza je dokładnie z niezerowym składnikiem W. Ten sam dwoisty świadek istnieje we wszystkich 18 trójkach; pełne liczby w JSON.

**Dodatkowa ostra granica informacyjna.** Z interpolacji Lagrange'a

`W = 100 K(0) -(400/3) K(.05) +(100/3) K(.2)`.

Dla dowolnych wektorów residualu o danych trzech normach twierdzenie o sumie wektorów daje górny limit

`||W|| <= 100 r0 + (400/3)ra +(100/3)rb`.

Jest on osiągalny przez kollinearne dobranie znaków (`K(0),K(.2)` zgodnie, `K(.05)` przeciwnie), podczas gdy minimum `||W||=0` jest osiągalne przez powyższą konstrukcję afiniczną, bo wszystkie trójki spełniają ROT20.2. Dla N31 K_A ostre granice wynikające **tylko z trzech norm** są

`0 <= ||W_A||_RMS <= 1.0039780072e-2`,

czyli górna granica ok. **265×||K_A(0)||**, mimo zmian norm K_A poniżej 2.5% na alpha=0→.2. Tak szeroki przedział nie znaczy, że rzeczywisty W ma duży moduł: pokazuje, jak wiele informacji tensorowej utracono przez raportowanie samych norm.

**Granica konstrukcji:** te dwa wymyślone profile Hilbertowskie NIE zostały okazane jako obrazy konkretnych pól C1,C2,h i operatora P_TT historycznego programu. Jest to dowód nieidentyfikowalności na podstawie samych trzech norm **w klasie residuali wektorowych stopnia ≤2**. Nie jest to niezależna rekonstrukcja oryginalnego przebiegu.

## 3. Dokładny rozstrzygający certyfikat z pięciu norm, bez dostępu do pól

Dla `alpha_k=alpha0+k δ`, `k=0..4` na **identycznych** N/polach/operatorach/masce i bez zmiany definicji RMS:

`Δ_δ^4 g(alpha0) = g(alpha0+4δ)-4g(alpha0+3δ)+6g(alpha0+2δ)-4g(alpha0+δ)+g(alpha0)`.  

Ponieważ `g(alpha)` ma stopień najwyżej 4, rachunek różnic skończonych daje dokładnie

`Δ_δ^4 g(alpha0)=24 δ^4 ||W||_RMS² >= 0`.  **(ROT20.3)**

Jest to **dokładny certyfikat tensorowego składnika kwadratowego** mimo obserwowania tylko norm. Obustronna równość działa nawet dla alpha0 != 0. Jeśli wartość jest dodatnia, wiadomo `W !=0`; jeśli jest dokładnie zero, `W=0` w tej zadeklarowanej klasie. Wynik ujemny oznacza niespełnienie kontraktu (lub niedokładności/niestabilność numeryczną), nie ujemny „fizyczny współczynnik”.

**Stabilność liczbowa:** operator czwartej różnicy odejmuje podobne liczby; na rzeczywistych danych przy małym δ może silnie wzmacniać błąd zaokrąglenia i fluktuacje. `ROT20.3` dotyczy arytmetyki dokładnej; praktyczna kwalifikacja wymaga wiarygodnej granicy błędu przy ustalonym protokole i powtórzeń. Nie twierdzimy, że pięć odpowiednich historycznych wyników jest obecnie zapisanych: w bieżącym zamrożonym skanie istnieją tylko **trzy** wartości alpha na każdej siatce.

**Niezależna kontrola algebraiczna:** w osobnym **syntetycznym** trójwymiarowym modelu z wymiernymi macierzami `P,L1,L2,S,L_bracket` wyznaczono `K_A,K_B,K_C` z dwukrotnym `E_alpha` i dokładnymi liczbami wymiernymi (`fractions.Fraction`). Dla wszystkich trzech `W != 0` i `Δ^4 g=24δ^4||W||²` **dokładnie**. To test tożsamości i stopnia, nie walidacja dyskretnego pola historycznego DTC0a.

## 4. Decyzja naukowa (jeden problem, jeden stan)

**PROBLEM_ID:** `DTC0A_E_ALPHA_SECOND_INSERTION_IDENTIFIABILITY`.  
**Best existing fact:** operator pomocniczy podwójnie używa `E_lin`; tensor residualu jest zatem co najwyżej kwadratowy w alpha. Zamrożone trzy normy na N nie określają W.  
**Countermodel:** 18× świadek afiniczny `W=0` i 18× świadek kwadratowy `W!=0`, te same trzy normy RMS, oba modele syntetyczne.  
**Source:** frozen odd-N CSV + manifest + helper `deepseek_python_20260627_349584.py`, nie historyczny runtime.  
**Referee:** niezależny audyt ROT20 **nieotrzymany**.  
**Exact mathematical discriminator:** pięć równoodległych alpha norm daje czwarte różnicowanie kwadratów, tożsamość ROT20.3; w obecnych zamrożonych danych nie ma takiego pięciopunktowego certyfikatu.  
**Claim decision:** `PASS_HELPER_ALGEBRA + PASS_FROZEN_CSV_OBSERVABILITY_COUNTERMODEL / HOLD_RUNNER_SOURCE_BINDING / HOLD_PHYSICAL_ENDPOINT`.

W szczególności mała zmiana `K_A_RMS` między alpha=0 a .2 NIE dowodzi małej normy `W_A` ani braku zakłócenia tensorowego; duża zmiana `K_C_RMS` NIE dowodzi, że jego drugi współczynnik W_C jest niezerowy. Aby rozróżnić, potrzebne są legalne dane innego typu. Nie przekazujemy Moderatorowi nowego zadania ani nie imputujemy brakujących obserwacji.

## 5. Pochodzenie, kontrola, obieg

- Skrypt read-only `verify_m13_rot20.py`: **18/18** warunków zgodności z afinicznym profilem; **18/18** niezerowych skalarnych współczynników modelu kwadratowego; ścisły syntetyczny certyfikat `A,B,C` na liczbach wymiernych: **3/3 PASS**.
- Zamrożona tabela wejściowa: `dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv`, SHA256 `1ed5dec5797ed1bc0ae9c4a924e1f18ef0a118f5602be99f03c953fd532cd66e`.
- Skrypt SHA256 `70b33692b5af45485a2c67731bf8b78d3faee8d4622d99776544dc6f7934f12f`.
- JSON machine summary `IW_M13_ROT20_alpha_identifiability_summary_20261023.json`, SHA256 `5bac701241b77aac9bcfdb4c0526d0ff2c3b31833de7a2a5a8360323ff110081`.
- Hist. runner hash deklarowany w manifestach `2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084`, źródło nieudostępnione i nieprzebudowane. Zachowane `RUNNER_NOT_REBUILT` z ROT18–19.

**ROUTE_TAGS:** `IWTO_MT13 IWTO_MECH_S7 IWTO_LT5 IWTO_REC10 IWTO_KN11 IWTO_INT8 IWTO_SW IWTO_MODERATOR`.  
**STOP:** `NO_NEW_TASK / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / TPE HOLD`.
