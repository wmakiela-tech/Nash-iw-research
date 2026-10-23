# IW / M13 — ROT28: dwumaskowa redukcja błędu RMS i ścisła energia koncentrycznych powłok

**RETURN_ID:** `M13-ROT28-DTC0A-TWO-MASK-BIAS-CANCELLATION-AND-FROZEN-SHELL-ENERGY-001_20261023`  
**CELL:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**DATE:** 2026-10-23  
**PROBLEM_ID:** `P3_DTC0A_TT_MASK_COMMUTATION_AND_LOCAL_RMS_TYPING_001` (ciąg dalszy ROT18, ROT23–27, bez nowej gałęzi)  
**CLASS:** dokładna tożsamość geometryczna dla maskowanych norm + źródłowe 45 historycznych wartości N41 i 9 kontrolek z tabeli siatek + niezależna ścisła wymierna asymptotyka po korekcie.  
**STATUS:** `EXACT_CONDITIONAL_MASK_DEBIAS / 45_FROZEN_MASK_VALUES_PASS / 9_GRID_VALUES_PASS / 36_SHELL_ENERGIES_POSITIVE / SYMPY_RATIONAL_COEFFICIENT_PASS / NOT_ORIGINAL_RUNNER / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / TPE HOLD`.

## 0. Rzeczywisty przyrost względem istniejącego korpusu

ROT18 wykazał zmianę **fizycznego obszaru** maski `interior_k=3` podczas refinacji. ROT21–23 zidentyfikowały nielokalność projekcji TT w masce i odtworzyły pełne tensory z zachowanego wariantu kodu odpowiadającego 99/99 historycznym RMS. ROT26 obliczył granicę globalnego `K_A`, a ROT27 dokładny człon pierwszego rzędu `1/N` w jego maskowanej normie, odróżniając go od operatorowego `N^-2`. XH-S4 ROT019 i INT8 ROT014/015/016 posiadają odrębne pierwszeństwo dla testu czystego śladu, TT-komutatora i bezaliasowości. Geeky-S11, PRF11 kontynuują niezależne oceny TT. **ROT28 nie podaje ich twierdzeń pod nową nazwą.**

Nowe rozstrzygnięcie jest *operacyjne i kontrolowane na zapisanej tabeli*: z **dwóch masek na jednej siatce** można anulować geometryczny składnik `1/N` w **kwadracie** RMS, bez zmiany stencilu i bez pełnych tensorów. Dane `N=41,k=2..6` pozwalają to sprawdzić źródłowo. Z tych samych historycznych liczb można dokładnie odczytać energię powłok zagnieżdżonych masek. Niezależny SymPy daje **ścisły**, wymierny współczynnik błędu poprawionej normy `K_A` na poziomie `N^-2`.

## 1. Twierdzenie geometryczne: korekta z dwóch masek

Niech `M_k` wybiera kostkę indeksów `k...N-k-1` w każdej osi. Dla *tego samego* pełnego pola tensorowego `T_N` określmy `g_k(N)=R_k(N)^2`, gdzie `R_k` to RMS z normalizacją `6(N-2k)^3`. Niech `g_0` będzie kwadratem RMS pełnej siatki.

Jeżeli gęstość energii `F_N(x)=||T_N(x)||_F²/6` jest okresowa i ma jednostajnie ograniczone pierwsze dwie pochodne (w używanej skończenie pasmowej rodzinie tak jest), a `k_a,k_b` to stałe dodatnie liczby całkowite, to suma obciętych węzłów i mianownik dają:

`g_k(N)=g_0(N) + (2k/N)(3 g_0(N)-S_x(N)-S_y(N)-S_z(N)) + O(k²/N²)`.

`S_j(N)` to średnia energii na płaszczyźnie `x_j=0` pełnego pola przy **tej samej siatce**, a nie parametr dopasowany do istniejącej tabeli. Stąd **bez znajomości `S_j`**:

`ĝ_0(N) := (k_b g_{k_a}(N)-k_a g_{k_b}(N))/(k_b-k_a) = g_0(N)+O(N^-2)`.

Dla historycznie dostępnych dwóch masek `k_a=2,k_b=3`:

`ĝ_0 = 3R_2²−2R_3²`, `R̂_0=sqrt(ĝ_0)` pod warunkiem `ĝ_0≥0`.

**Dowód.** Wiodąca energia w każdej z sześciu obciętych ścian to `2k S_j/N`. Przecięcia dwóch pasów mają objętość `O(k²/N²)`, podobnie jak korekta drugiego rzędu od odwrotności `(1−2k/N)^3`. Cała średnia to zatem wyrażenie afiniczne w `k/N` z błędem kwadratowym. Kombinacja `k_b*g_{k_a}−k_a*g_{k_b}` anuluje jej wiodący współczynnik dokładnie. Warunki stałości `N`, pól, `alpha`, `P_TT`, stencilu i definicji RMS są krytyczne: NIE wolno odejmować norm z różnych N czy pól. Ten prosty rodzaj ekstrapolacji jest klasyczny (Richardson / boundary quadrature), nie rości nowości.

## 2. Wymierny, *ostry dla tej rodziny* drugi współczynnik po korekcie

Dla continuum granicznego `A_∞(x)` z ROT26 definiujemy:

`G = mean(F) = 5917501/3499200000000000`,  `F=||A_∞||_F²/6`, `A_∞=sqrt(G)=4.1122999754697787e-5`.

Płaszczyznowe średnie `S_x,S_y,S_z` są z ROT27. Nowy rachunek dokładny parowania współczynników Fouriera na **przecięciach dwóch płaszczyzn** dał:

| Linia przecięcia | Wymierna wartość średniej `T_ij` |
|:--|:--|
| `x=y=0` (średnia po z) | `27135931/9841500000000000` |
| `x=z=0` (średnia po y) | `154107797/52488000000000000` |
| `y=z=0` (średnia po x) | `134706859/39366000000000000` |

Rozwinięcie unormowanego kwadratu RMS w ustalonej masce ma postać

`g_k = g_0 + k A_1/N + (k A_{2,lin}+k² A_{2,quad})/N² + O_α(N^-3)`.

Terminy `A_{2,lin}` zawierają pochodne gęstości na płaszczyznach, lecz są **również anulowane** przez powyższe dwupunktowe odejmowanie. Współczynnik kwadratowy w k:

`A_{2,quad} = 24G−12(S_x+S_y+S_z)+4(T_xy+T_xz+T_yz) = −333001/246037500000000`.

Stąd dla `k=2,3`:

`ĝ_0−g_0 = −6 A_{2,quad}/N² + O_α(N^-3)`

oraz, po wyciągnięciu pierwiastka,

**`lim_{N→∞} N² (R̂_0/R_0 −1)=42624128/17752503=2.401020746201254`**.

Dokładność jest tu **rodzinna, nie uniwersalna**: współczynnik dotyczy źródłowego pola `h=.1sin(x)cos(y) I`, podanych `C1,C2`, niezmiennego Fouriera P_TT i stałego `alpha`. Dzięki limitowi `E=I`, wiodąca poprawka nie zależy od stałej alpha. Wynik nie wymaga regresji i NIE jest twierdzeniem o innym polu ani dowodem nowej fizyki.

## 3. Bezpośrednia kontrola na historycznym N=41, trzy alpha i trzy kanały

15 źródłowych rekordów `dtc0a_mask_sensitivity_N41_v0_3_1.csv` zawiera trzy RMS każdy, razem **45/45** wartości. Odtworzono je ponownie z pełnej rodziny modów na N41, z maksymalnym względnym błędem `1.45e-14`; dodatkowe 9 porównań z `dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv` również `PASS`.

W tabeli podajemy procentowy błąd normy w stosunku do **niezależnie obliczonej z pełnego tensora normy globalnej przy tym samym N**, a nie do continuum `A_∞`:

| alpha | kanał | historyczne `k=3` | korekta `k=2,3` | poprawa |
|---:|:--:|---:|---:|---:|
| 0 | A | −5.6162% | −0.8761% | tak |
| 0 | B | +6.1096% | −1.6086% | tak |
| 0 | C | −18.5080% | −4.9641% | tak |
| .05 | A | **−5.6264%** | **−0.8737%** | **6.44×** mniejszy błąd bezwzględny |
| .05 | B | +6.0809% | −0.6791% | tak |
| .05 | C | −17.1928% | −4.5501% | tak |
| .2 | A | −5.6555% | −0.8667% | tak |
| .2 | B | +1.4653% | −0.2149% | tak |
| .2 | C | −13.8029% | −3.3387% | tak |

Zatem **9/9 testów na historycznej tabeli masek** daje mniejszy błąd bezwzględny wobec pełnosieciowego RMS. Współczynniki dla alpha=.05, kanał A: `R_3=3.8372562954249065e-5`, `R̂_0=sqrt(3R_2²−2R_3²)=4.030501279657465e-5`, rzeczywista globalna norma `4.0660276474467215e-5`.

### Jak wygląda dalszy trend N? (tylko model rzadki)

Korekta `k2,3` z niezależnego rachunku modów daje `N²(R̂_0/R_0−1)` dla `K_A` przy alpha=.05: `−14.6875` (N41), `−2.0323` (N201), `+0.11994` (N401), `+1.47425` (N1001), `+1.93536` (N2001), `+2.30753` (N10001), dążąc do dokładnego **`+2.40102`**. Zmiana znaku nie obala rzędu `N^-2`: odpowiednio duże człony następnego rzędu są istotne, gdy N=31–41. Wiersze N>41 to **ewaluacja skończonej liczby modów**, nie uruchomienia dawnego programu na dużych trójwymiarowych siatkach.

W szczególności sama procedura korekty na N41 nadal nie wyznacza granicy continuum bez dodatkowych założeń o stencilu i rodzinie źródeł.

## 4. Dokładna energia powłok z N41 CSV bez pełnych tensorów

Dla zagnieżdżonych kostek `D_k ⊃ D_{k+1}` o liczbach węzłów `n_k=(N−2k)^3` można rozdzielić energię na maskowaną kostkę wewnętrzną i usuwaną **powłokę indeksową**, używając tylko historycznych RMS:

`R_shell(k→k+1)² = [n_k R_k²−n_{k+1} R_{k+1}²]/[n_k−n_{k+1}]`.

To **ścisła tożsamość** dla niezmienionych tensorów i identycznej metryki RMS. Dla 3 alpha × 3 kanały × 4 powłoki otrzymano **36/36 dodatnich gęstości energii**. W alpha=.05 stosunek RMS powłoki `k2→k3` do RMS kostki wewnętrznej `k3` wynosi: `K_A=1.10641`, `K_B=0.85566`, `K_C=1.30899`.

Wszystkie trzy kanały mają odmienne profile przestrzenne i nie można utożsamiać wzrostu/spadku z oszacowaniem „przecieku fizycznego przy granicy”. Jest to wewnętrzna powłoka **wybranej kostki indeksowej na siatce okresowej**, nie rzeczywista granica fizyczna ani rozkład energii całej pełnej siatki.

## 5. Stabilność i zakres stosowalności

Korekta dwumaskowa dla kwadratów RMS ma wagi `(3,−2)` i sumę modułów wag **5**; jeżeli wejściowe `R_k²` mają niepewności absolutne ≤ε, niepewność poprawionej **energii średniej** może wynieść 5ε. Dopasowywanie wielomianu po kolejnych k daje większe sumy modułów wag: maski `(2,3,4)` → 17; `(2,3,4,5)` → 49; `(2,3,4,5,6)` → 129. Wyższy rząd nie jest automatycznie lepszy przy szumie, zaokrągleniach ani przy małym N. Jeżeli `ĝ_0<0`, pierwiastek nie istnieje jako rzeczywista estymata i należy oznaczyć `FAIL/STOP`, zamiast obcinać na zero.

Warunki krytyczne: obie maski obliczone na **jednym i tym samym pełnym polu** i tej samej siatce; te same `alpha`, pole, stencil, FFT `P_TT`, wagi sześciu symetrycznych komponentów, mianowniki. Nie używać `R_2` z jednego N i `R_3` z innego ani norm z dwóch przebiegów zmieniających pole. Brak dwóch masek nie uprawnia do odtworzenia pełnej normy z samego `R_3`. Źródło zapisane (CSV) nie zawiera rzeczywistych tensorów; niezależny pełnosieciowy `R_0` to walidacja pomocnicza z funkcjonalnie dopasowanego wariantu, a nie pomiar produkcyjny.

Wzory nie implikują, że `K_A` jest fizyczne, że zachodzi kowariancja tła, że znika niezgodność symbolu różnicowego INT8, ani że naprawiono nieidentyfikowalność TT-restricted w teście czystego śladu (XH019). Operator `dtc0a_runtime_v0_3_1.py` o manifestowym SHA256 `2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084` nadal nie jest dostępny bajtowo. Bez niezależnego referee i BW ingest / owner adoption nie ma zmiany claim ceiling.

## 6. Pochodzenie, testy, kryteria decyzji

- Wykonawczy audyt: `verify_m13_rot28.py` (54 porównań RMS w N41: 45 maskowych + 9 grid, z czego 9 wartości mogą się pokrywać logicznie przy k3; niezależne tabele, nie osobne eksperymenty), plus 36 tożsamości powłok, 9 testów poprawy błędu, ekstrapolacje do N=10001.
- Niezależne wyprowadzenie symboliczne: `verify_m13_rot28_exact.py` z dokładnymi `G,S_j,T_ij` i współczynnikiem wymiernym `42624128/17752503`.
- Surowe historyczne `dtc0a_mask_sensitivity_N41_v0_3_1.csv` i `dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv` pozostają nienaruszone. Wariant źródłowo dopasowany `deepseek_python_20260627_a87249.py`. Zależności splotowe i asymptotyczne `verify_m13_rot26.py`, `verify_m13_rot26_exact.py`, `verify_m13_rot27.py` są dołączone.
- JSON `IW_M13_ROT28_mask_extrapolation_and_shells_20261023.json`: dziewięć przypadków N41 × trzy kanały, 36 powłok, 27 dodatkowych ewaluacji dużych N oraz pełne porównania ekstrakcji; gotowy ZIP z manifestem sum SHA256.

**Jedna decyzja:** `PASS_SOURCE_FROZEN_MASK_45/45 + PASS_EXACT_RATIONAL_FIRST_ORDER_CANCELLATION + PASS_SOURCE_FAMILY_9/9_NUMERIC_GAIN`, ale `HOLD_UNIVERSAL_QUALITY / HOLD_HISTORICAL_RUNNER_IDENTITY / HOLD_PHYSICAL_ENDPOINT / HOLD_REFEREE / HOLD_BW_INGEST`.

**ROUTE_TAGS:** `IWTO_MT13 IWTO_KN11 IWTO_INT8 IWTO_XH_S4 IWTO_REC10 IWTO_LT5 IWTO_SW IWTO_MODERATOR`.  
**STOP:** `NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / TPE HOLD`.