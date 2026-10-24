# IW/NASH — M13 ROT32: odzyskanie identyfikowalności w źródłowo ustalonej rodzinie DTC0a oraz jej niejednorodne uwarunkowanie

**RETURN_ID:** `M13-ROT32-DTC0A-SOURCE_MODEL_JOINT_CHANNEL_ALPHA_AMPLITUDE_IDENTIFIABILITY_WITH_AB_FOLD_AND_N2_STABILITY_GATE-001_20261024`  
**CELL:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**PROBLEM_ID:** `P3_DTC0A_TT_MASK_COMMUTATION_AND_LOCAL_RMS_TYPING_001`  
**Data:** 2026-10-24  
**Klasa:** źródłowo ograniczona *identyfikowalność strukturalna* i analiza stabilności; rachunek skończenie modowy / testy numeryczne, dokładny audyt znaków na ZAPISANYCH wielomianach dziesiętnych. **Nie** jest to walidacja fizyczna, oryginalny historyczny runtime ani rygorystyczny przedziałowy certyfikat wszystkich współczynników rzeczywistych operatorów.

## 0. Punkt wyjścia, delimitacja i wcześniejsze prawa pierwszeństwa

M13 ROT23 odtworzył 99/99 historycznych RMS poprzez alternatywny zachowany helper i zrekonstruował pełne źródłowe tensory. ROT24 dowiódł w tej implementacji `K_j(alpha)=U_j+alpha V_j+alpha² W_j`; ROT26–28 utworzyły niezależny rzadki rachunek Fouriera i asymptotykę masek. ROT29 wykazał niejednoznaczność pięciu maskowanych norm dla szerszej klasy pól; ROT30 wykazał próg 2/3 dla jednowspółrzędnych TT; ROT31 udowodnił ostrą niejednoznaczność przy paśmie 1 dla **dowolnych 3D TT**. Wynik ten pozostaje w mocy. Niniejszy ROT32 bada **inną, zdecydowanie węższą klasę**: jeden z góry zadany generator `C1,C2,h`, ustalony stencil `order=2`, `E_lin`, projektor Fourier-TT, znane `N` i `interior_k`, dwa nieznane parametry rzeczywiste `(alpha,s)` z `alpha in [0,0.2]`, `s>0` jako **JEDEN wspólny mnożnik** wszystkich residuali.

Odrębne wyniki XH-S4, INT8, Geeky-S11 i PRF11 dotyczą domeny TT, Lie/projekcji, aliasingu, koniugacji oraz dyskretyzacji; nie dowodzą ani nie zastępują tego zagadnienia identyfikowalności parametrów konkretnego generatora. Matematyczny mechanizm identyfikacji parametrycznej i baza Bernsteina to dojrzałe narzędzia, **NO_NOVELTY**.

## 1. Ścisły model i kryterium monotoniczności

Dla kanału `j in {A,B,C}`, z tego SAMEGO źródła i maski:

`K_j(alpha)=U_j+alpha V_j+alpha² W_j`.

Przy normalizacji Frobeniusa na masce `M`, energia `g_j(alpha)=RMS_M(K_j(alpha))²` jest wielomianem stopnia <=4:

`g_j = <U,U> + 2alpha<U,V> + alpha²( <V,V>+2<U,W> ) + 2alpha³<V,W> + alpha⁴<W,W>`.

Wejście o wspólnej amplitudzie `s` daje odczyty `y_A=s sqrt(g_A)`, `y_C=s sqrt(g_C)`; ich iloraz `R=y_A/y_C=sqrt(g_A/g_C)` nie zależy od `s`. Jeśli

`p(alpha)=g'_A(alpha) g_C(alpha) - g_A(alpha) g'_C(alpha)<0`, `g_A,g_C>0`

dla wszystkich `alpha in [0,1/5]`, to `R` ściśle maleje i jednoznacznie wyznacza `alpha`. Potem `s=y_A/sqrt(g_A(alpha))`. Na tej podstawie rozstrzygana jest **strukturalna identyfikowalność dwóch parametrów**, a nie rekonstrukcja pełnego nieznanego tensora ani identyfikowalność dowolnych generatorów.

### Pełny audyt znaku na całym przedziale, bez próbkowania α

Dla `N=31,33,35,37,39,41` i maski `k=3`, dodatkowo `N41,k=2..6`, zrekonstruowano przez rzadki rachunek Fouriera współczynniki wszystkich `g_A,g_B,g_C`. Wielomian `p` ma stopień najwyżej 7. Każdy jego współczynnik w bazie Bernsteina na `[0,1/5]` jest **ujemny** we wszystkich 10 konfiguracjach; po podzieleniu przez `g_A(0)g_C(0)` maksimum spośród wszystkich współczynników wynosi `−13.80016257013` (najbardziej ujemny: `−56.14905126728`). Przy pozytywnych energiach jest to globalny test znaków, a nie sprawdzenie siatki 100 punktów.

**Status matematyczny precyzyjnie:** `verify_m13_rot32_decimal.py` wykonuje audyt wyznacznika pochodnej i znaków Bernsteina dla **DZIESIĘTNYCH WSPÓŁCZYNNIKÓW ZAPISANYCH w JSON** w *dokładnej arytmetyce wymiernej*. Dla tych zapisanych wielomianów dowodzi również `|d(log R)/dalpha|>4/5` na całym `[0,1/5]` (bardziej zachowawcze niż wartości numeryczne ~3.55–7). Związanie zapisanych współczynników z rzeczywistym kodem źródłowym opiera się na wykonanym niezależnie rachunku numerycznym i porównaniach. Nie ma tu zaokrągleń skierowanych ani formalnego dowodu przedziałowego dla oryginalnych trygonometrycznych danych wejściowych, dlatego wolno mówić o **silnie numerycznie potwierdzonej** monotoniczności source-family i ścisłym twierdzeniu dla opublikowanych wielomianów, ale nie o komputerowo zweryfikowanym przedziałowo dowodzie rzeczywistej implementacji.

## 2. Historyczne źródło i odtwarzalność

Wariant `deepseek_python_20260627_a87249.py`, SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`, generuje `C1=(.05sin x,.05cos y,0)`, `C2=(.04cos z,0,.04sin x)`, `h=.1sin x cos y I`. Ten **alternatywny zachowany helper** odtwarza historyczne normy; oryginalny `dtc0a_runtime_v0_3_1.py` o deklarowanym SHA256 `2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084` nie został odzyskany. Nie utożsamiać źródeł bajtowo.

* 18 konfiguracji z historycznej tabeli siatek x trzy kanały = **54/54 PASS**; maks. błąd względny `1.69e−14`.
* Z tabeli `N41 k=2..6` pozostałe 36 wartości kanałów RMS = **36/36 PASS**; maks. błąd względny `1.44e−14`.
* Trzy dodatkowe wartości testowe alpha `0.03125, 0.113, 0.177` dla 10 par `(N,k)`, wszystkich trzech kanałów: `90/90 PASS`, maksymalna względna różnica **energii** między bezpośrednim sparsowym obliczeniem a wyliczonym wielomianem `3.29e−14`.
* Dodatkowy test **NIEZMODYFIKOWANEGO** `compute_K_C`, `compute_K_A_out`, `rms_norm` źródła dla `N31,k3,alpha=.113`: zgodność norm z wielomianem A `4.44e−16`, C `1.78e−15`.
* Odzyskanie `alpha` i jednego wspólnego `s` z historycznych par A,C: **30/30 PASS**, max `|alpha_est-alpha|=4.55e−14`, przy `s=1`. Dla każdej rzeczywistej pary `yA,yC` należącej do modelu metoda identyfikuje unikalny parametr w zdefiniowanym przedziale i dodatnią amplitudę. Dane na granicach przedziału podlegają przycięciu.

Wybrane ilorazy `A/C` dla standardowej maski `k3`:

| N | alpha=0 | alpha=.05 | alpha=.2 |
|---:|---:|---:|---:|
|31|24.73594801|17.64407375|8.62664064|
|33|27.94905692|19.92233076|9.73991474|
|35|31.32675072|22.32038284|10.91533564|
|37|34.86860032|24.83791781|12.15278838|
|39|38.57470322|27.47494993|13.45226043|
|41|42.44547018|30.23169036|14.81380093|

## 3. Niezbędna negatywna kontrola: sam iloraz A/B jest niejednoznaczny

Nie każdy wybór dwóch kanałów jest poprawnym eksperymentem identyfikacyjnym. Dla każdej historycznej `N` przy `k=3`, pochodna `A/B` jest **dodatnia przy alpha=0**, następnie zmienia znak. Przykład `N41 k3`: punkt zwrotny `alpha*=0.00071266916635`; drugi punkt `alpha2=0.00142531382798` ma `R_A/R_B(alpha2)=R_A/R_B(0)` z błędem względnym `6.22e−15` w opublikowanym wielomianie.

Po dobraniu wspólnego mnożnika `s2≈1.00010120873` oba odczyty A,B dla `(alpha2,s2)` zgadzają się z `(alpha=0,s=1)`; mimo to kanał C różni się względnie o `≈0.9991871%`. Zatem **A/B nie identyfikuje globalnie α na [0,.2]**, lecz trójka A,B,C lub para A,C rozwiązuje tę szczególną degenerację. Efekt `A/B` ma bardzo małą amplitudę około punktu zwrotnego — jego detekcja w praktyce wymaga odpowiadającej dokładności obserwacji.

## 4. Stabilność: warunkowa odzyskiwalność nie jest jednostajna w N

Przy niezależnych perturbacjach odczytów RMS A i C o ±0.5% test wszystkich 10 kombinacji `(N,k)` i alpha=.05,.1,.15 (60 testów z przeciwnymi znakami perturbacji) daje maksymalną `|delta alpha|=0.00240786842`. To **syntetyczny kontrolowany model zakłóceń**, nie estymacja rzeczywistej niepewności archiwalnego eksperymentu.

Ważniejsza jest struktura graniczna. Dla stałego `alpha`, stałego indeksu maski i tego samego skończenie modowego generatora, ROT27 ustalił `K_A RMS -> A_inf>0` oraz `K_C RMS = c(alpha)/N² + o(N^-2)` z `c(alpha)>0`. Parametryzacja `u=log s`, `alpha` ma macierz czułości dwóch ABSOLUTNYCH odczytów `yA,yC`:

`J = [[A, dA/dalpha], [C, dC/dalpha]]` przy `s=1`.

Ponieważ `dA/dalpha=O(N^-2)` oraz `dC/dalpha=Theta(N^-2)` na badanym [0,.2], a `A->A_inf>0`, najmniejsza wartość osobliwa maleje `Theta(N^-2)`. Stąd `cond_2(J)=Theta(N²)` w *bezwzględnej* skali odczytów. Dla alpha=.05, maski k3, bez dużych siatek przestrzennych:

| N | cond₂(J) | cond₂(J)/N² |
|---:|---:|---:|
|31|2.83668|0.00295180|
|41|4.80704|0.00285963|
|81|17.90971|0.00272972|
|161|69.12932|0.00266692|
|321|271.77116|0.00263751|

Zatem przy **niezależnym od N absolutnym poziomie błędu pomiaru RMS** procedura traci stabilność przy zwiększaniu rozdzielczości. Nie wynika z tego analogiczna degeneracja przy zadanej dokładności **względnej** obu kanałów; ta wymaga błędów C malejących wraz z jego amplitudą. Formalna identyfikowalność i odporność eksperymentalna to dwa osobne warunki.

## 5. Formalne warunki stosowania i ograniczenia

GO tylko pod łącznymi założeniami: dokładnie znane `N`, indeks maski, `C1,C2,h` i ich względne amplitudy, identyczne parametry `E_lin`, stencil centralny `order=2`, Fourier-TT, `alpha in [0,.2]`, **jeden** wspólny nieznany dodatni mnożnik norm A,C, dodatni `g_A,g_C`. Zmiana pola, osobne skale kanałów, nieznany stencil, wybór wyłącznie dwóch kanałów A,B, inna domena lub niekontrolowane błędy wykraczają poza wniosek. Pozostaje wcześniejsza uwaga XH-S4: wejście `h=f I` to czysty ślad, a surowy `K_A` jest diagnostyką na ambient `Sym²`, nie testem przekształceń tylko na TT.

**Falsifikatory/STOP:** naruszenie monotoniczności dla zewnętrznego źródła; szum niezależny między kanałami zamiast wspólnej amplitudy; niepasujące wartości pełnego residualu względem modelu; potrzeba powtórzenia na oryginalnym runtime (brak bajtowo identycznego); brak niezależnej oceny referee. Wynik **nie** awansuje dowodów o J3/K, grawitacji, fizycznym inwariancie ani kontinuum TT.

## 6. Replikacja i custody

`verify_m13_rot32.py`: rzadkie mody, wielomiany norm, 10 znaków Bernsteina, 54+36 RMS, 90 testów spoza węzłów, 30 inwersji, fold A/B, syntetyczne perturbacje, macierz czułości. `verify_m13_rot32_decimal.py`: niezależna dokładna arytmetyka wymierna dla **zapisanych** współczynników dziesiętnych oraz `|d log R/dalpha|>4/5` dla tych modeli. `verify_m13_rot32_native.py`: bezpośrednio niezmodyfikowany helper przy dodatkowym `alpha=.113`. `IW_M13_ROT32_alpha_amplitude_identifiability_20261024.json` zawiera wszystkie współczynniki, 10 zestawów wyników, foldy, testy błędu i dane kondycjonowania. Historyczne CSV i pierwotny helper są dołączone do samodzielnego pakietu. Sumy SHA256 / manifest dołączone. Nie zakładamy dostarczenia do BW ani akceptacji OWNER/EXEC bez odpowiedniego readback.

**STATUS:** `SOURCE_SPECIFIC_IDENTIFIABILITY_NUMERIC_PASS / DECIMAL_BERNSTEIN_EXACT_PASS / AB_NONIDENTIFIABILITY_FOLD_PASS / ABSOLUTE_NOISE_N2_ILL_CONDITIONING / NO_BYTE_EXACT_RUNTIME / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_NEW_TASK / TPE HOLD`.