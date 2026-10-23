# IW / M13 — ROT24: bezpośrednia identyfikacja składnika α² w DTC0a na odtworzonej rodzinie pól

**RETURN_ID:** `M13-ROT24-DTC0A-FULL-TENSOR-ALPHA2-COEFFICIENT-IDENTIFICATION-AND-SOURCE-EXPANSION-001_20261023`  
**Komórka:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**Data:** 2026-10-23  
**PROBLEM_ID:** `P3_DTC0A_E_ALPHA_SECOND_INSERTION_IDENTIFIABILITY` — aktualizacja ROT20; bez tworzenia nowej gałęzi.  
**Klasa:** exact finite-operator algebra w kontrakcie pomocniczego źródła + odtworzenie tensorowe zamrożonych danych (nie oryginalny runtime) + bezpośrednie testy poza punktami interpolacji.  
**STOP:** `SOURCE_HELPER_FUNCTIONAL_REPLAY / FULL_TENSOR_IDENTIFIED / ORIGINAL_RUNTIME_BYTE_EXACT_MISSING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_NEW_TASK / TPE HOLD`.

## 0. Subtraction-first: co jest już własnością innych prac

ROT20 wykazał, że przy ustalonych polach, siatce i masce `E_lin=I+αS_N` wymusza wielomianowy residual tensorowy stopnia ≤2. Jedynie **trzy normy RMS** dla α=0,0.05,0.2 nie wyznaczają tensorowego współczynnika α²; podał dwa przeciwne kontrmodele oraz pięciopunktowe kryterium różnicy czwartej kwadratów norm. ROT23 (źródłowo-funkcjonalny replay 99/99 tabelarycznych wartości) odzyskał pełne pola wejściowe w zachowanym wariancie kodu; ten obrót wykorzystuje nowy dostęp do *pełnych tensorów* i **konkretnie wyznacza** ich współczynniki, bez wycofywania no-go o samych normach.

Równolegle: INT8 ROT008/012 odróżnia symbol `k` Fourier-TT od `sin(k dx)/dx` różnic centralnych, INT8 ROT013 opisuje defekt dyskretnej reguły Leibniza. KN11 ROT05 bada kompresję komutatorów; XH-S4 018/019 i Geeky-S10 badają projektorowe leakage, a XH-S4 019 **już wykazał**, że wyjściowe `h=f(x,y)I` ma `P_TT h=0`, zatem surowe `K_A(h)` jest residualem na przestrzeni otaczającej, nie dowodem niezgodności reprezentacji ograniczonej do TT. ROT24 **nie zgłasza tych własności jako własnego pierwszego odkrycia**. Dotyczy tylko rozmiaru i kierunku `U,V,W` w rzeczywistym funkcjonalnym wariancie DTC0a.

Kontrola currentness: zwroty w `#iw-dispatch` z 23 października 2026 (INT8 ROT013, XH-S4 019, KN11 census, MT13 P3); brak potwierdzonej niezależnej recenzji ROT24.

## 1. Ścisłe twierdzenie i kontrakt źródłowy

Ustalamy jeden nieparzysty `N`, `dx=2π/N`, stałe pola `C1,C2,h`, stencil różnic centralnych drugiego rzędu, pełnosieciowy projektor fourierowski `P=P_TT` i maskę `M_k` używaną **dopiero przy RMS**. Niech `S_N=dx²Δ_N`, `E_α=I+αS_N`, `L_i=L_{C_i}` oraz `L_b=L_{[C1,C2]}`. W pomocniku `T_i(α)=L_i E_α`.

Wyrażenia źródłowe to:

`K_C(α) = (L1 Eα L2 Eα − L2 Eα L1 Eα − L_b Eα)h`,  
`K_B(α) = P K_C(α)`,  
`K_A(α) = (P L1 Eα P L2 Eα − P L2 Eα P L1 Eα − P L_b Eα)h`.

Każdy jest wielomianem tensorowym:

`K_j(α)=U_j+α V_j+α² W_j`, `j∈{C,B,A}`.                                 **(ROT24.1)**

Współczynniki kwadratowe mają **niezależną od interpolacji** formułę:

`W_C = (L1 S_N L2 S_N − L2 S_N L1 S_N)h`,  
`W_B = P W_C`,  
`W_A = (P L1 S_N P L2 S_N − P L2 S_N P L1 S_N)h`.                 **(ROT24.2)**

Dowód: jawne wymnożenie dwóch czynników `I+αS_N`; ostatni człon `L_b Eα` jest wyłącznie liniowy w α. `P` jest liniowe i nie zależy od α. Wszystkie operatory w formułach są rzeczywiste i liniowe na tensory (przy zamrożonych C1,C2,N). **Żadna fizyczna interpretacja α nie jest potrzebna do tego rachunku.**

Dla trzech pełnych tensorów przy `a=.05`, `b=.2`:

`U=K(0)`,  
`W = [ (K(b)−K(0))/b − (K(a)−K(0))/a ]/(b−a)`,  
`V = [K(a)−K(0)]/a − a W`.                                     **(ROT24.3)**

Dostęp do tensorów czyni te współczynniki wyznaczalnymi **z trzech** pomiarów, natomiast z trzech **samych norm** wyznaczenie pozostaje niemożliwe (ROT20). To rozróżnienie jest sednem nowego wyniku.

## 2. Dane i bezpośredni test źródła

Źródło funkcjonalnie zgodne z historyczną serią: `deepseek_python_20260627_a87249.py`, SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`. Wariant `349584.py` wprowadza dodatkowe `h_xy=0.02 sin(z)` i nie pasuje do historycznych RMS (ROT23). **Historyczny plik `dtc0a_runtime_v0_3_1.py`**, deklarowany w manifeście z SHA256 `2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084`, nie jest dostępny bajtowo.

Skrypt `verify_m13_rot24.py`:

1. dla każdego `N=31,33,35,37,39,41` od nowa generuje źródłowe pola `C1,C2,h` i pełne `K_C,K_B,K_A` przy α=0,0.05,0.2; **54/54** historyczne normy z zamrożonego CSV zgodne do tolerancji `5e−12` względnie;
2. interpoluje **każdy pełny tensor**, nie normy, według (ROT24.3), oblicza sześć iloczynów skalarnych dla rozkładu `||U+αV+α²W||²` na wspólnej masce;
3. w niezależnym przebiegu dla N31 i N41 liczy źródłowe operatory `S_N` i `L_i` bezpośrednio według ROT24.2 i porównuje je z uzyskanym W;
4. w punktach α=0.10 i α=0.15 **liczy nowe pełne tensory** bez interpolacji: 2 N × 2 α × 3 kanały = **12 bezpośrednich holdoutów**, największy względny tensorowy błąd interpolacji `6.8305e−14`;
5. dla N31 i N41 oblicza naprawdę pięć kwadratów norm przy α=0,.05,.10,.15,.20 i weryfikuje `Δ^4 ||K||² = 24(.05)^4||W||²`. Testowane 6 kombinacji N×kanał; maksymalny względny błąd tego silnie znoszącego się testu około `2.46e−6` w kanale A N41. Bardziej stabilny test **bezpośredniego W** ma maksymalny błąd względny `7.56e−11`.

Wszystkie obliczenia dotyczą **wariantu helpera**, nie identycznego bajtowo historycznego runtime. Wyrażenie „historia odtworzona” dotyczy norm (54/54), nie potwierdzenia identyczności implementacji.

## 3. Wynik: W jest różny od zera, ale bardzo nierównomierny kanałowo

Mierzymy `ρ_W,j(N)=||(.2)² W_j||_RMS / ||U_j||_RMS` przy **tej samej masce** `interior_k=3`. To normowa miara wpływu członu kwadratowego względem residualu wyjściowego α=0, **nie udział energii lub procent zmiany normy**.

| N | `ρ_W,C` | `ρ_W,B` | `ρ_W,A` | `ρ_V,A=||.2V_A||/||U_A||` |
|---:|---:|---:|---:|---:|
| 31 | 3.4116% | 7.2373% | **0.04331%** | 3.5455% |
| 33 | 3.0184% | 6.4547% | **0.03362%** | 3.1190% |
| 35 | 2.6868% | 5.7899% | **0.02647%** | 2.7633% |
| 37 | 2.4051% | 5.2208% | **0.02110%** | 2.4641% |
| 39 | 2.1641% | 4.7300% | **0.01702%** | 2.2104% |
| 41 | 1.9566% | 4.3040% | **0.01387%** | 1.9934% |

W każdej z 18 par `(N,j)` `W_j` jest niezerowe. Równocześnie `W_A` ma względnie o rzędy wielkości mniejszy wpływ niż `W_C` i `W_B`. Wszystkie porównania są specyficzne dla tego samego źródłowego `h=fI`, generatorów i maski; nie wolno ekstrapolować na dowolne TT wejście ani inne parametry `E`.

### Kwantyfikacja plateau K_A oraz anomalii „mała zmiana normy mimo zmiany tensora”

Dla `N=31`: `||U_A||=3.788529759e−5`, `||V_A||=6.716162253e−6`, `||W_A||=4.102028445e−7`; przy α=.2: `||K_A||=3.694723526e−5`. `cos(U_A,V_A)=-0.71114`. Relatywne składniki kwadratu normy końcowej:

`||U_A||² / ||K_A(.2)||² = +1.05142310`,  
`||.2 V_A||² / ||K_A(.2)||² = +0.00132172`,  
`||.04 W_A||² / ||K_A(.2)||² = +0.0000001972`,  
`2<U_A,.2 V_A> / ||K_A(.2)||² = −0.05302028`,  
`2<U_A,.04 W_A> / ||K_A(.2)||² = +0.00030433`,  
`2<.2 V_A,.04 W_A> / ||K_A(.2)||² = −0.00002907`.

Ich suma wynosi 1. Dla `N=41` `cos(U_A,V_A)=-0.71240`, `||U_A||²/||K_A(.2)||²=1.02872134` i `2<U_A,.2 V_A>/||K_A(.2)||²=−0.02921813`. Zatem **małą zmianę normy `K_A` w α** w tym modelu wyjaśnia dominujący wkład `U_A`, niewielki `V_A`, maleńki `W_A` i ujemny iloczyn `U_A,V_A`. Nie wynika z tego ścisła niezmienniczość `K_A` wobec α; przeciwnie, tensor zmienia się i `W_A ≠ 0`.

**Osobna oś: wzrost N.** `||U_A||` wynosi 3.78853e−5 przy N31 i 3.85089e−5 przy N41, ale nie jest to dowód limitu continuum, ponieważ zmienia się siatka, operator i fizyczny obszar maski (ROT18). Wniosek dotyczy wyłącznie przedstawionej sześciopunktowej rodziny.

## 4. Autonomiczny dowód vs test norm czwartego rzędu

Przy `K(α)=U+αV+α²W` i stałym produkcie skalarnym maski:

`g(α)=||K(α)||² = ||U||² + 2α<U,V> + α²(||V||²+2<U,W>) + 2α³<V,W> + α⁴||W||²`.

Zatem dokładnie `Δ_δ^4 g(α0)=24δ^4||W||²`. To twierdzenie ROT20 jest wreszcie zastosowane do **pięciu faktycznie wyliczonych punktów** dla N31 i N41 w 3 kanałach. Przykład `N=31,K_A,δ=.05`: bezpośrednia czwarta różnica `2.52399572455e−17`, a formuła `24δ⁴||W_A||²=2.52399560419e−17`. `N=41,K_A`: odpowiednio `2.67613711074e−18` wobec `2.67613054585e−18` (odchylenie względne `2.45e−6` związane z odejmowaniem podobnych wartości). Pozostałe kanały w tych N mają błędy względne około `1e−10` lub mniejsze. To jest test tożsamości i zgodności helpera, nie formalny dowód stabilności przy dowolnej precyzji.

**Wniosek metodologiczny:** gdy mamy jedynie normy RMS, pięć równoodległych α może dać współczynnik ||W||², ale test czwartego rzędu jest wrażliwy na roundoff, szczególnie gdy ||W|| jest małe. Jeżeli legalnie dysponujemy **pełnymi tensorami**, trzy α wyznaczają U,V,W; następnie niezależna formuła operatorowa ROT24.2 kontroluje W bez problemu wysokiej różnicy skończonej. Nie należy tych dwóch kontraktów mieszać.

## 5. Granice i decyzja naukowa

**EARNED:** 54/54 frozen RMS replays; 18/18 niezerowych współczynników W; 12/12 bezpośrednich testów α spoza interpolacji; 6/6 rzeczywistych pięciopunktowych tożsamości w granicach podanej precyzji; niezależne źródłowe wzory W_C,W_B,W_A potwierdzone przy N31 i N41. Wyjaśnienie niewielkiej wrażliwości normy K_A na α w jednej zadeklarowanej rodzinie.

**NOT EARNED:** W original-byte-exact `dtc0a_runtime_v0_3_1.py`, identyczność wszystkich flag / implementacji, prawo na wszystkich polach, limit continuum, zerowy fizyczny tensor J3/K, przyjęcie do BW, niezależny audyt REC10/SW lub kanon. W szczególności `h=fI` nie jest TT wejściem; fakt `P_TT h≈0` i konieczność ograniczenia celu do `K_A(P h)` zostały jawnie stwierdzone przez XH-S4 ROT019 przed ROT24. Ten rezultat nie może awansować `K_A(h)` do stwierdzenia o reprezentacji TT ani teorii fizycznej.

**Przyrost względem ROT20:** dawniej `W` z danych wyłącznie normowych był nierozstrzygalny; dzięki ROT23 w jawnie nazwanej rekonstrukcji pełnych pól stał się obliczalny, a jego niewielki, lecz niezerowy udział w K_A jest ilościowo zweryfikowany. Jest to *poprawa identyfikowalności dzięki bogatszemu obserwablum*, nie obalenie wcześniejszego no-go.

**Status problemu:** `PASS_HELPER_FULL_TENSOR_IDENTIFICATION / PASS_DIRECT_OPERATOR_W / PASS_HELDOUT_ALPHA / ORIGINAL_SOURCE_BIND_HOLD / PHYSICAL_ENDPOINT_HOLD`.

## 6. Odtwarzalność i referencje

- `verify_m13_rot24.py` — generuje źródłowe tensory `K_C,K_B,K_A` na wszystkich N, wyznacza U/V/W, wylicza iloczyny skalarnie, sprawdza 12 bezpośrednich punktów alpha, sprawdza `W` z formuł operatorowych, rzeczywistą pięciopunktową tożsamość. Zapisuje JSON.
- `IW_M13_ROT24_alpha_tensor_coefficients_20261023.json` — wszystkie 6×3 zestawy norm, kosinusów, składników kwadratu normy, 12 holdoutów i 6 walidacji norm czwartego rzędu.
- Zamrożona tabela: `dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv`, SHA256 `1ed5dec5797ed1bc0ae9c4a924e1f18ef0a118f5602be99f03c953fd532cd66e`.
- Odtwarzalny helper: `deepseek_python_20260627_a87249.py`, SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`.
- XH-S4 ROT019, pierwotne rozróżnienie ambient/TT i trace-strain: https://github.com/wmakiela-tech/Nash-iw-research/blob/c1cee5ba11727266a7f7052e470931f6d9213f44/research/xh-s4/2026-10-23/IW_XH_S4_DTC0A_TT_DOMAIN_SPECTRAL_DERIVATIVE_AND_COMMUTATOR_HOST_AUDIT_019_20261023.md
- M13 ROT23: https://github.com/wmakiela-tech/Nash-iw-research/blob/39c775baf44d3eb64a1c8503a86faf94862d51e5/research/m13/2026-10-23/IW_M13_ROT23_DTC0a_full_functional_replay_mask_TT_001.md
- M13 ROT20: https://github.com/wmakiela-tech/Nash-iw-research/blob/b2954a1269ed76507979ba5bd1ed51a03e8a81d5/research/m13/2026-10-23/IW_M13_ROT20_DTC0a_alpha_norm_identifiability_001.md

**ROUTE_TAGS:** `IWTO_MT13 IWTO_KN11 IWTO_INT8 IWTO_LT5 IWTO_REC10 IWTO_SW IWTO_MODERATOR`.  
**STOP:** `NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / TPE HOLD`.