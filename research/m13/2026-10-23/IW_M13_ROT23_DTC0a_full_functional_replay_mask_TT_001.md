# IW / M13 — ROT23: pełna rekonstrukcja numeryczna DTC0a i rozkład maskowanego kanału TT na rzeczywistym polu odtworzonym funkcjonalnie

**RETURN_ID:** `M13-ROT23-ODDN-DTC0A-FUNCTIONAL-REPLAY-AND-SOURCE-TYPED-TT-OUTSIDE-INPUT-SPLIT-001_20261023`  
**CELL:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**DATA:** 2026-10-23  
**KLASA:** **99/99 źródłowo-tabelarycznych norm RMS odtworzonych poprzez przeliczenie generatorów i operatorów** z zachowanego alternatywnego skryptu + analiza liniowa pełnego odtworzonego pola `K_C`. **Nie** jest to bajtowe odtworzenie zaginionego pierwotnego runtime ani niezależny eksperyment fizyczny.  
**STATUS:** `HELPER_FUNCTIONAL_REPLAY_PASS / FROZEN_RMS_MATCH_PASS / NOT_BYTE_EXACT_SOURCE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / TPE HOLD`.

## 0. Stan źródeł i jedno materialne rozstrzygnięcie

W ROT18–22 znane były: ruchoma dziedzina maskowanego RMS; wymuszona jednorodność skalowania; nieidentyfikowalność tensorowego współczynnika `alpha²` z trzech norm; matematyczny nonmap `MP(I−M)` i ostre ograniczenie `||MP(I−M)||≤1/2`. **Nie było** jednak obliczonego wkładu spoza maski dla pełnych tensorów należących do tej samej rodziny, której normy historycznie zaraportowano. ROT23 uzupełnia tę lukę.

Dwa dostępne skrypty mają różne, jawne zawartości i hashe:

* **Wariant pasujący:** `deepseek_python_20260627_a87249.py`, SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`. Funkcja `generate_smooth_fields` tworzy dwa wektory trigonometryczne, tensor `h` z diagonalną strukturą `h_ii=0.1 sin(x)cos(y)` i zerowe `h_xy`; dla `order=2` implementuje różnicowanie centralne, `E_lin`, pochodną Liego, bracket i FFT TT.
* **Wariant niepasujący:** `deepseek_python_20260627_349584.py`, SHA256 `2fd77da6b2501d957fabf8884a2625bbafedf594399e720360e83caa344938c5`. Wprowadza dodatkowo `h_xy=h_yx=0.02 sin(z)`; w zakresie użytym w eksperymencie operatorowe instrukcje `order=2` odpowiadają pierwszemu skryptowi. Pozostałe odgałęzienia, w tym niezrealizowany historycznie czwarty stencil, nie są tu testowane.
* **Pierwotny historyczny plik deklarowany przez manifesty:** `dtc0a_runtime_v0_3_1.py`, SHA256 `2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084`. Brak kopii o tym hashu. Zgodność outputu **nie jest dowodem identyczności kodu, konfiguracji wszystkich pomocniczych flag czy bitowej reprezentacji pól**.

Tabela `dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv`, SHA256 `1ed5dec5797ed1bc0ae9c4a924e1f18ef0a118f5602be99f03c953fd532cd66e`; piętnaście rekordów tabeli maskowej `dtc0a_mask_sensitivity_N41_v0_3_1.csv`, SHA256 `4dc228e1edab9fefc219118b5ba465b817d86a934cfee4d5ae563657e3bd5f91`. Danych wejściowych nie zmieniano.

## 1. Zakres pełnego ponownego obliczenia i niezależne kontrole

Dla `L=2π`, `N∈{31,33,35,37,39,41}`, `α∈{0,0.05,0.2}`, `order=2`, `E_mode=E_lin`, `interior_k=3` skrypt `verify_m13_rot23.py`:

1. generuje `C1,C2,h` przez `a87249.py` osobno dla każdej N;
2. liczy **pełny tensor** `K_C`, a następnie `K_B=P_TT K_C` i **pełny** `K_A` z oryginalnych formuł zagnieżdżenia;
3. stosuje `rms_norm` do wskazanej maski, a łącznie 54 normy porównuje ze źródłowymi CSV;
4. rozszerza na wszystkie k=2,..,6 przy N41 i trzech alpha — dodatkowe 45 wartości;
5. kontroluje osobno bez modyfikacji kodu `apply_P_TT` i `compute_K_A_out` na N31, alpha=.05. Do przyspieszenia wielokrotnego testu maskowego implementacja widmowego TT jest wektoryzowana, ale **jawnie sprawdzona względem niezmienionego TT**.

**Wynik:** 54/54 + 45/45 = **99/99** norm odtworzonych; maksymalny błąd względny serii N31..41: **4.441e-16**, a maskowej: **4.441e-16**. Bezpośrednie `compute_K_A_out` przy pełnej oryginalnej implementacji TT i ta sama ścieżka z TT wektoryzowanym dały względny błąd tensorowy **4.663e-16**. Kontrola TT na N11 dała **9.877e-16**.

**Negatywna kontrola rozróżniająca warianty:** po dodaniu do `h` nowego shear `0.02 sin(z)` dla N31 alpha=.05, względem źródłowych norm `K_C`, `K_B`, `K_A` dostajemy odpowiednio **+0.045864%**, **+0.288603%**, **-1.375350%**. Nie wolno mieszać tych dwóch wariantów pola pod wspólną etykietą bez sprawdzenia definicji `generate_smooth_fields`.

## 2. Ścisły rozkład źródła wnętrze/zewnętrze

Dla stałego N, α i maski M definiujemy Q=I−M, P=P_TT. Wewnątrz maski zachodzi **dokładnie**

`M K_B = M P(M K_C) + M P(Q K_C) =: v_in + v_out`.

Norma RMS tych tensorów odpowiada stałemu iloczynowi Hilberta (symetryczne tensory z wagą 2 dla elementów pozadiagonalnych), więc

`||M K_B||_RMS² = ||v_in||_RMS² + ||v_out||_RMS² + 2 ||v_in||_RMS ||v_out||_RMS cosθ`.

Jest to superpozycja po **projekcji** wyliczonego już K_C, nie oddzielny eksperyment z dwoma fizycznymi pobudzeniami. Definiowany stosunek `||v_out||_RMS / ||M K_B||_RMS` NIE jest frakcją energii / niezależnie addytywną składową błędu. Dopuszcza wartości powyżej 1, jeżeli człony się znoszą; w poniższych 18 punktach ma wartości 0.603877–0.963257, a cosθ jest ujemny w każdym punkcie (−0.575219..−0.413477).

| N | α | K_C RMS | K_B RMS | K_A RMS | ||v_in|| RMS | ||v_out|| RMS | ||v_out||/||M K_B|| | cosθ |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 31 | 0.0 | 1.531588665e-06 | 3.000263961e-07 | 3.788529759e-05 | 3.364415382e-07 | 2.890024629e-07 | 0.963257 | -0.548683 |
| 31 | 0.05 | 2.133723145e-06 | 4.436200376e-07 | 3.764756853e-05 | 5.270581923e-07 | 3.930288809e-07 | 0.885958 | -0.568343 |
| 31 | 0.2 | 4.282922729e-06 | 1.335067326e-06 | 3.694723526e-05 | 1.438136188e-06 | 8.549468402e-07 | 0.640377 | -0.413477 |
| 41 | 0.0 | 9.072566953e-07 | 1.679064034e-07 | 3.850893701e-05 | 1.906499651e-07 | 1.573369351e-07 | 0.937051 | -0.548564 |
| 41 | 0.05 | 1.269282746e-06 | 2.527820074e-07 | 3.837256295e-05 | 3.046911263e-07 | 2.163275438e-07 | 0.855787 | -0.574511 |
| 41 | 0.2 | 2.562985512e-06 | 7.786456420e-07 | 3.796755716e-05 | 8.521716097e-07 | 4.702059193e-07 | 0.603877 | -0.425511 |

Przykład N31 α=.05 (ścisłe wartości w JSON): `K_B= 4.436200375564e-07`, `v_in=5.270581923129e-07`, `v_out=3.930288809468e-07`, `cosθ=-0.56834259`. Człony **częściowo się znoszą**, a pominięcie Q K_C przed TT usuwa człon o normie `88.596%` normy istniejącego wyjścia.

## 3. Zmiana maski bez zmiany obliczonego tensora

Dla `N=41, alpha=.05` poniższe liczby otrzymano z **jednego i tego samego pełnego** pola K_C, zmieniając jedynie operator przestrzennego obcięcia M. Każdy przypadek odpowiada zapisanej tabeli czułości maski:

| k | K_B RMS maskowany | ||v_out|| RMS | ||v_out||/||M K_B|| | cosθ |
|---:|---:|---:|---:|---:|
| 2 | 2.475290034e-07 | 1.883070124e-07 | 0.760747 | -0.543810 |
| 3 | 2.527820074e-07 | 2.163275438e-07 | 0.855787 | -0.574511 |
| 4 | 2.577580879e-07 | 2.295137559e-07 | 0.890423 | -0.570506 |
| 5 | 2.615575019e-07 | 2.322755158e-07 | 0.888048 | -0.543798 |
| 6 | 2.632383568e-07 | 2.257305043e-07 | 0.857514 | -0.492961 |

Różnice między k są spowodowane zmianą przestrzennego okna i podziału pola przed nielokalną projekcją. Nie dają wprost estymatora zbieżności na stałej domenie fizycznej (ROT18); nie izolują też częstotliwości / kątów dyfuzji operatora (INT8 ROT008).

## 4. Jak wynik zmienia status ROT18–22

* **Status poprawiony:** z `FROZEN_CSV_POSTPROCESS + SYNTHETIC_HELPER_TEST` do `99/99 SOURCE-HELPER-FUNCTIONAL NUMERICAL REPLAY` dla **konkretnej** rodziny generatorów i diagnostyk, przy dokładnie jawnych parametrach oraz alternatywnym kodzie.
* **Przeciek jest realny w odtworzonej rodzinie:** `MPQ K_C !=0` w 18/18 konfiguracji, a wkład ma mierzalną normę i ujemny iloczyn skalarny z kanałem wejściowym w masce. Zamyka lokalny brak danych dla tego modelu funkcjonalnego.
* **Wynik nie jest ogólnym wyjaśnieniem plateau K_A:** `K_A` wykorzystuje **zagnieżdżoną kompresję** i nie redukuje się do jednej projekcji `P K_C`; stąd nie można utożsamiać z jej mechanizmem wykazanego terminu spoza maski w `K_B`.
* **ROT22:** ogólna ostra granica `||MPQ||≤1/2` pozostaje prawdziwa. Efektywna wartość `||MPQ K_C||/||Q K_C||` w przeliczonych konfiguracjach wynosi od 0.132193 do 0.170080, czyli poniżej tej granicy; w tym scenariuszu ekstremalne podprzestrzenie z ROT22 **nie** są osiągane przez konkretne K_C.
* **ROT20:** zgodność trzech norm na trzech α nie określa tensorowych współczynników z samych **CSV**, lecz udana rekonstrukcja pełnego generatora i operatorów pozwala wyliczyć więcej niż same trzy normy. Nie jest to logiczna sprzeczność; uzupełniono model.
* **INT8/KN11:** symbol projekcji Fouriera vs dyskretnych pochodnych i kompresja komutatorów to odrębne problemy. Zbieżność numerów nie rozstrzyga ich uniwersalnie ani nie nadaje endpointowi statusu fizycznego.

## 5. Kryteria PASS / STOP, własność naukowa i pochodzenie

**PROBLEM_ID:** `P3_DTC0A_TT_MASK_COMMUTATION_AND_LOCAL_RMS_TYPING_001` (rozszerzenie istniejącego problemu z ROT21/22, bez zakładania nowej gałęzi BW).  
**PASS:** 99/99 historycznych RMS; 18/18 dokładnych dekompozycji pełnego maskowanego wyniku; 18/18 przeciwnie ukierunkowanych wektorowych wkładów; natywny/widektorowy P_TT tensorowo zgodny.  
**HOLD:** brak bajtowo tożsamego oryginalnego `dtc0a_runtime_v0_3_1.py`, brak niezależnego SRC referee, brak dowodu fizycznej interpretacji J3/K lub extrapolacji continuum.  
**Właściciel:** MT13 program; KN11 custody BW; M13 lokalna analiza — bez samowolnego OWNER_ADOPTION/EXEC.  
**Falsyfikatorem wersji pól:** dodanie shear i stwierdzony brak zgodności historycznych norm.

**Źródła:** oba `deepseek_python_20260627_*.py`, dwa zachowane CSV, manifest. Skrypt i JSON są pełnym lokalnym odtwarzalnym nośnikiem; `verify_m13_rot23.py` oblicza wszystkie deklarowane tabele bez korzystania z gotowych tensorów. Źródłowy `P_TT` wywołano bezpośrednio jako kontrolę. Brak źródłowo zweryfikowanego pierwotnego runnera pozostaje jawnym ograniczeniem.

**ROUTE_TAGS:** `IWTO_MT13 IWTO_KN11 IWTO_INT8 IWTO_REC10 IWTO_LT5 IWTO_SW IWTO_MODERATOR`.  
**STOP:** `NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / TPE HOLD`.