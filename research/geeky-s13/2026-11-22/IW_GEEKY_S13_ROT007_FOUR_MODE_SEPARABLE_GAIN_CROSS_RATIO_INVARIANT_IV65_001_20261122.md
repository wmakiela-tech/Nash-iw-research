---
artifact_id: IW_GEEKY_S13_ROT007_FOUR_MODE_SEPARABLE_GAIN_CROSS_RATIO_INVARIANT_IV65_001_20261122
return_id: IW_GEEKY_S13_ROT007_ORIGINAL_M13_ROT038_FOUR_MODE_DIRECTION_RADIUS_SEPARABLE_CALIBRATION_FREE_CROSS_RATIO_001_20261122
origin_cell: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
scientific_class: ORIGINAL_M13_N41_SOURCE_CONDITIONAL_ROT038_FIXED_ANISOTROPIC_GAUSSIAN_PAIR / FOUR_RAW_FOURIER_MODES / EXACT_RANK3_GAIN_GROUP / CROSS_RATIO_MAXIMAL_INVARIANT / BINOMIAL_IV65
status: AUTHOR_PROOF_AND_EXECUTED_IV65_PLUS_INDEPENDENT_FULL_N41CUBED_SPATIAL_SOURCE_MATH_REFEREE / DIFFERENT_CELL_I1_PENDING
source_access: ORIGINAL_M13_HELPER_AND_ROT038_REPORT_READ / ORIGINAL_M13_HELPER_NOT_EXECUTED_THIS_ROTATION / FULL_HISTORICAL_DTC0A_MISSING
claim_ceiling: NO_PHYSICAL_SITE_SENSOR / NO_NEW_PHYSICAL_NASH_CLAIM / NO_GENERAL_MATH_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_PENDING
---

# Geeky-S13 ROT007 — czteromodowy niezmiennik przy nieograniczonej, ale rozdzielnej kalibracji kierunku i częstotliwości

## 0. Pytanie, pochodzenie i wynik

Po ROT003–005 i ROT006 krytycznym ograniczeniem dwóch modów `kx=(20,0,0)`, `ky=(0,20,0)` okazał się nieznany, *osobny* współczynnik kierunkowy: jeśli jego logarytm może mieć odchyłkę `epsilon >= D/2`, hipotezy A/B stają się dokładnie nierozróżnialne dla rozkładu dwóch ilorazów. Zamiast zakładać fizycznie nieuzasadniony mały limit `epsilon`, pytamy, czy **dodatkowy promień częstotliwości** pozwala wyeliminować całe nieznane wzmocnienie kierunkowe na drodze algebraicznej.

**WYNIK, ściśle warunkowy:** Dla oryginalnej periodycznej siatki N=41 i **dwóch dokładnie określonych anizotropowych sztucznych hipotez szumu gaussowskiego A/B pierwszych w Geeky-S12 ROT038**, cztery hipotetyczne niezależne odczyty zespolonych modów Fouriera w każdym pełnym pomiarze dostarczają maksymalny niezmiennik dla trójwymiarowej grupy nieznanych wzmocnień rozdzielnych na kierunek i promień. Wzmocnienia mogą być nieograniczone, różne pod A/B, dowolnie zależne od czasu i nawet adaptacyjne do ukrytych wartości losowych. Mimo to rozkłady niezmiennika pod A i B pozostają różne o ściśle dodatnie przesunięcie `Delta=0.0688332343055984976...`. Zatem możliwa jest jednostajna statystyczna dyskryminacja A/B **bez ograniczania rozmiaru wzmocnień**, jeżeli zachodzi dokładna **rozdzielność mnożnikowa**.

Co nie należy do wyniku: dowolna kalibracja zależna nieseparowalnie od kierunku i promienia, arbitralny niestrukturalny szum niegaussowski, rzeczywista aparatura RAW-site, cała przestrzeń fizyczna NASH, globalna optymalność wszystkich dozwolonych czteromodowych schematów, ogólna nowość matematyczna lub zewnętrzna I1.

### Pierwszeństwo i sprawdzone źródła

- M13 FIRST oryginalne publiczne pomocnicze operatory Fourier–tensor N41, Git blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679`; historyczny pełny `dtc0a_runtime_v0_3_1.py` nadal niedostępny. Ten obrót **nie wykonywał** oryginalnego modułu M13.
- Geeky-S12 ROT038 FIRST *anizotropowe* dokładne racjonalne A/B szumu RAW-site i dziewięcioobserwacyjny pełny alias; Git blob `28576dbb0649c1f0fbd4d926896813eac946e6d8`: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s12/2026-11-21/IW_GEEKY_S12_ROT038_ORIGINAL_M13_ANISOTROPIC_DIRECTIONAL_EXACT_ALIAS_ONE_BOUNDARY_PROBE_ESCAPE_AND_NONGAUSSIAN_DEPENDENCE_001_20261121.md.
- Geeky-S13 ROT003 FIRST dwu-kierunkowa para na promieniu `20` i source-conditional optymalność par permutacyjnych; ROT004 FIRST wspólne wzmocnienie i test binarny; ROT005 FIRST optymalny pełny iloraz; ROT006 FIRST ścisłe `epsilon*=D/2` dla dwumodowego błędu kierunkowego. Raport ROT006: https://github.com/wmakiela-tech/Nash-iw-research/blob/339e76e97b35e0cf6f1e4a875c4d8fdaad0625a1/research/geeky-s13/2026-11-22/IW_GEEKY_S13_ROT006_SHARP_ADAPTIVE_DIRECTIONAL_GAIN_MINIMAX_AND_IV55_FINITE_SAMPLE_001_20261122.md.
- M15 ROT041 FIRST *inna* sześciomodowa, pięcioparametrowa grupa kalibracji dla **innej izotropowej pary A/B ROT035**, maksymalny niezmiennik i log-Gamma test: https://github.com/wmakiela-tech/Nash-iw-research/blob/5877526b1228237fcafb9e2a433db88e8b305e5d/research/m15/2026-11-22/IW_M15_ROT041_ORIGINAL_M13_MAXIMAL_INVARIANT_MINIMAX_GAMMA_SOURCE_IV110_001_20261122.md. Zachowuje pełne pierwszeństwo M15; tu inna hipoteza i inna grupa. Również ROT001/002 Geeky używały *izotropowej*, a nie obecnej anizotropowej pary A/B.

Opracowanie jest zastosowaniem klasycznej analizy niezmienników grupowych, różnicy różnic, rozkładów logistycznych i dwumianowych do dokładnego, ograniczonego obiektu źródłowego; **bez claimu nowości ogólnej**.

## 1. Dokładny model źródła i dobór czterech modów

Dla kosinusów `cx=cos(2*pi*kx/41)` itd. i ośmiu współczynników sąsiedztwa model ma dokładnie widmo:

`v_X(k)=beta0 + beta_x cx + beta_y cy + beta_z cz + beta_xy cx cy + beta_xz cx cz + beta_yz cy cz + beta_body cx cy cz`.

W kolejności `(beta0,beta_x,beta_y,beta_z,beta_xy,beta_xz,beta_yz,beta_body)`:

- `A=(1,1/25,1/25,1/25,1/30,1/30,1/30,2/25)`;
- `B=(1,1/20,3/100,1/25,1/30,13/300,7/300,2/25)`.

Oba modele mają dodatnio określony operator: `v_X(k)>=1-3/10=7/10` dla całego N41³. Gdy `c=cos(2*pi*j/41)`, dokładne racjonalne redukcje to

`v_A(x,j)=v_A(y,j)=167/150+(14/75)c`, 

`v_B(x,j)=82/75+(31/150)c`,  `v_B(y,j)=17/15+c/6`.

`v_B(y,j)-v_B(x,j)=(1-c)/25` oraz `d/dc log(v_B(x,j)/v_B(y,j))=(13/250)/(v_B(x,j)v_B(y,j))>0`.

Niech `d(j)=log(v_B(x,j)/v_B(y,j))`. Na `j=1,...,20` symbol `c(j)` ściśle maleje, więc `d(j)` też ściśle maleje. Dla klasy `j∈{7,...,20}`, gdzie zarówno `(j,0,0)` jak `(0,j,0)` leżą poza ograniczonym nośnikiem źródłowej energii M13 `[-6,6]x[-4,4]x[-2,2]` weryfikowanym wcześniej źródłowo przez M15, **największa różnica d(j_low)-d(j_high)** występuje przy `j_low=7`, `j_high=20`. Twierdzenie o optymalności dotyczy *wyłącznie tej osiowej, dwupromieniowej klasy*, nie wszystkich modów czy kosztów statystycznych.

Wybór:

`k_xH=(20,0,0), k_yH=(0,20,0), k_xL=(7,0,0), k_yL=(0,7,0)`.

Dla A ilorazy kierunkowe na obu promieniach są równe 1. Dla B:

`d(20)=-0.086206705382304749995890052376...`;
`d(7)=-0.017373471076706252392943142486...`;
`Delta=d(7)-d(20)=0.0688332343055984976029469098900172786130416...>0`.

**Źródłowy warunek zerowej średniej:** oryginalne M13 B-energy Fourier różnice mają nośnik w `[-6,6]x[-4,4]x[-2,2]` według zweryfikowanych upstream obliczeń M15. Każdy z czterech modów i jego sprzężony mod ujemny leży poza tym nośnikiem. Jest to warunek dla *hipotetycznych obserwacji surowych site Fourier*, nie instrument M13. W ROT007 nośnika nie przeliczano przez wykonanie oryginalnego tensor-polys.

## 2. Dokładna redukcja grupowa: eliminacja dowolnych wzmocnień kierunku i promienia

Przyjmijmy, że w każdej hipotetycznej obserwacji `t=1..n`, dla hipotezy X∈{A,B}, cztery kwadraty amplitud zespolonych modów można zapisać:

`P_{d,r,t}=G_{d,t} H_{r,t} v_X(d,r) E_{d,r,t}`,

przy kierunku `d∈{x,y}`, promieniu `r∈{H=20,L=7}`, **ściśle dodatnich** (możliwie nieograniczonych) mnożnikach `G_x,G_y,H_H,H_L` i czterech niezależnych jednostkowych `Exp(1)` energiach `E`. Ukryte cztery `E` w obrębie obserwacji są niezależne, a wektory czterech `E` są IID między obserwacjami. Mnożniki mogą zależeć od wszystkich `E`, historii, t i hipotezy X; ich rozkładu **nie** zakładamy.

Definiujemy *wewnątrz każdej obserwacji* dokładny kontrast:

`C_t=(P_xH,t P_yL,t)/(P_yH,t P_xL,t)`.

**Zanik ścieżkowy:** wszystkie czynniki `G_x,G_y,H_H,H_L` skracają się *identycznie* przed wnioskowaniem probabilistycznym. Zostaje

`C_t=q_X (E_xH E_yL)/(E_yH E_xL)`, z `q_A=1`, `q_B=exp(-Delta)<1`.

W logarytmach czynników obserwacyjnych grupa mnożnikowa generuje wektory: `G_x:(1,0,1,0)`, `G_y:(0,1,0,1)`, `H_H:(1,1,0,0)`, `H_L:(0,0,1,1)`. Ich rząd wynosi **3** (jedna relacja liniowa), a przestrzeń anihilatora jest rozpięta przez `(1,-1,-1,1)`. Dlatego `log C` jest **maksymalnym niezmiennikiem** na dodatniej czterowymiarowej przestrzeni energii dla tej grupy. Nie zakładamy, że grupa została zmierzona lub fizycznie wyznaczona.

Dokładne prawo: niech `L=log(E_1/E_2)` dla niezależnych Exp(1). Wtedy L ma logistyczną gęstość `f_L(u)=e^u/(1+e^u)^2`. W tym eksperymencie `Z_t=log C_t` ma pod A rozkład `W=L_1+L_2`, pod B rozkład `W-Delta`, gdzie `L_1,L_2` są niezależne logistyczne. Dla dowolnego rzeczywistego `w`:

`F_W(w)=e^w(e^w-1-w)/(e^w-1)^2`, z ciągłym przedłużeniem `F_W(0)=1/2`.

Można to sprawdzić bez tablic rozkładów: jeśli `U=logistic(L_1)` jest jednostajna na (0,1), to `F_W(w)=int_0^1 exp(w)(1-u)/[u+exp(w)(1-u)] du`. Pochodna w zerze wynosi `f_W(0)=1/6`; gęstość jest symetryczna i logarytmicznie wklęsła jako splot gęstości logistycznych.

## 3. Jednostajny test: certyfikat kosztu próbkowania i jego wyraźny sufit

Najprostszy test: `Y_t=1{Z_t < -Delta/2}`. Wtedy:

`p_A=F_W(-Delta/2)=0.49426412361275686384628944472164...<1/2`;
`p_B=1-p_A=0.50573587638724313615371055527836...`.

Dla nieparzystego n orzekamy B wtedy i tylko wtedy, gdy `sum_t Y_t >=(n+1)/2`. Oba błędy są równe dokładnie:

`e_n=Pr[Binomial(n,p_A)>n/2]=I_{p_A}((n+1)/2,(n+1)/2)`.

Ponieważ **C_t** jest niezależne od wszystkich mnożników w modelu, `Y_t` są IID, nawet jeżeli mnożniki zmieniają się arbitralnie i adaptacyjnie. Przy `p_A<1/2`, błędy monotonicznie spadają pomiędzy kolejnymi nieparzystymi n; losowanie przy remisie dla parzystych n daje dokładnie błąd poprzedniego nieparzystego n. Rygorystyczne, wykonane przez program nowe **mpmath.iv 65-digit outward** sumowanie dodatnich dwumianowych składników certyfikuje:

| Cel (trafność dla każdej hipotezy) | n poprzednie (NIE) | n pierwsze (TAK) | Ścisłe przedziały błędu e_n |
|---|---:|---:|---|
| >95% | 20555 | **20557** | prev `[0.05000748679967719..., 0.05000748679967720...]`; first `[0.04999923399579210..., 0.04999923399579211...]` |
| >99% | 41119 | **41121** | prev `[0.01000095332054383..., 0.01000095332054384...]`; first `[0.009999445482993015..., 0.009999445482993016...]` |

Te liczby są **minimalne w ściśle zadanej klasie testów jednobitowej większości z czteromodowego ilorazu**, NIE wśród wszystkich testów wykorzystujących pełne `Z_t`. Pełny test Neymana–Pearsona wykorzystujący gęstość `f_W(z+Delta)/f_W(z)` może być skuteczniejszy; jego dokładny koszt pozostaje otwarty. Nie porównuj bezpośrednio kosztu czterech kanałów z dwiema sondami w ROT005 jako kosztu tego samego kontraktu kalibracji: klasy dopuszczalnych błędów są różne.

Wynik ma charakter **czysto matematycznego warunku**: liczby 20557 i 41121 dotyczą hipotetycznych niezależnych pełnych obrazów RAW-site N41³ lub bezpośrednich odczytów czterech modów, nie wykonanych pomiarów ani sprawdzonych wymagań aparatury.

## 4. Próby falsyfikacji i nierozwiązane pułapki

1. **Fałszywe rozszerzenie na dowolną kierunkowo-częstotliwościową kalibrację:** jeśli dozwolone są niezależne cztery mnożniki `G_{d,r}` bez faktoryzacji, można wybrać `G_{x,H,A}/G_{x,H,B}=q_B` przy pozostałych odpowiednio dostrojonych i uzyskać dokładnie wspólny rozkład `C` pod A i B. Sama liczba czterech modów nie ratuje identyfikowalności.
2. **Jedna para kierunkowa z arbitralnym wzmocnieniem osi:** przy tylko jednym promieniu `G_x/G_y` jest niezidentyfikowanym dodatnim mnożnikiem, który dokładnie maskuje źródłowe `v_B(x)/v_B(y)`; ROT006 poprawnie wykrył tę granicę.
3. **Cztery latenty niegaussowskie:** z niezależności warunkowej energii i ich rozkładów Exp(1) wynikają dwie składowe logistyczne. Dowolne niegaussowskie pary mogą zmienić `p_A`; brak prawa do uniwersalnego twierdzenia bez tego założenia.
4. **Nieliniowe lub addytywne błędy:** kontrast z ilorazu mocy nie usuwa addytywnych offsetów, saturacji czy wzajemnego przenikania kanałów.
5. **Ograniczenie promienia `j>=7`:** pozwala nie opierać się na podtrzymanej bez nowego wykonania źródła hipotezie zera średniej przy mniej odległych modach. Nie udowodniono optymalności po wszystkich możliwych przestrzennych modach.
6. **Nieobserwowalność czterech modów:** M13 oryginalnie dostarczył matematykę tensorów i pięciu masek; cztery RAW-site sondy są pomocnicze, hipotetyczne.

## 5. Materiał wykonawczy i kontrola źródłowości

Program pierwotny oblicza dokładne racjonalne współczynniki, wyznacza `Delta` w wysokiej precyzji i z **arytmetyką skierowaną 65 cyfr**, sprawdza wszystkie 14 legalnych promieni j7..20, cztery sąsiadujące wartości dwumianowego błędu dodatnią rekurencją oraz ich ścisłą pozycję względem progów 5% i 1%. **Pierwotna próba uruchomienia kodu początkowo została odrzucona przez limit długości konwersji int→str Python 3.13 (4300 cyfr), nie przez błąd matematyczny; podniesiono wyłącznie limit wyjściowy `sys.set_int_max_str_digits`, bez zmiany współczynników i formuł.** Nie nazywamy tej przerwanej próby PASS.

Drugi program, napisany niezależnie, nie importuje pierwszego, odtwarza **pełen periodyczny operator kowariancji N41³ przez 6 axial + 12 face + 8 body oryginalnych przesunięć sąsiedztwa** i weryfikuje wartości własne na wszystkich czterech rzeczywistych falach sinusoidalnych, a także oblicza `p_A` niezależną kwadraturą SciPy i cztery błędy `scipy.stats.binom.sf`. Dodatkowo testuje ścieżkowe skasowanie adaptacyjnych współczynników kierunkowych i radialnych na 5000 syntetycznych zestawach. Jest to **same-cell independent-algorithm**, nie niezależna recenzja I1 i nie wykonanie natywnego `tensor_polys` M13.

Pliki pakietu: program pierwotny i jego pełny JSON, program niezależny i JSON, ten raport, README, replay z kontrolami negatywnymi, potwierdzenie przebiegu i manifest SHA256. Każdy eksperyment jest na danych modelowych i nie korzysta z prywatnego fizycznego odczytu. Opublikowanie raportu w GH/Slack nie jest statusem CANON ani ACK przez właściciela.

## 6. Recenzja zewnętrzna i status

**Prośba o ograniczony, nieślepy I1 do REC13/AUD3:** (a) sprawdzić source exact rational spectra i SPD oraz niepowtarzanie pierwszeństwa M15; (b) dowieść rzędu 3 grupy i maksymalności `log C`; (c) odtworzyć monotoniczność `d(j)` i źródłowy warunek mean-free dla czterech modów; (d) niezależnie wyprowadzić logistyczny splot i jego CDF; (e) przeliczyć cztery przedziałowe granice n, w szczególności bardzo wąskie `n=20557`; (f) spróbować złamać tezę przez dozwolone adaptacyjne czynniki o postaci `G_d H_r`; (g) odróżnić ograniczenia ściśle rozdzielnego modelu od rzeczywistej aparatury.

**Sufit:** `AUTHOR_SOURCE_TYPED_MATH / N41_SPATIAL_FFT_SITE_OPERATOR_SAME_CELL_PASS / IV65_FOUR_BINOMIAL_GATES_PASS / EXTERNAL_DIFFERENT_CELL_I1_PENDING / NATIVE_BW_INGEST_PENDING / NO_PHYSICAL_FOUR_MODE_SENSOR / NO_GENERAL_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE`.
