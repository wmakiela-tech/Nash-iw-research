# IW / M13 — ROT31: ostra granica pięciu masek w pełnej 3D przestrzeni TT — nieidentyfikowalność już dla pasma 1

**RETURN_ID:** `M13-ROT31-3D-TT-ONE-BAND-FIVE-MASK-NONMAP-001_20261024`  
**CELL:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**DATE:** 2026-10-24  
**PROBLEM_ID:** `P3_DTC0A_TT_MASK_COMMUTATION_AND_LOCAL_RMS_TYPING_001`  
**CLASS:** exact finite-dimensional cyclotomic/modular rank certificate + genuine low-band TT tensors + source-helper numerical RMS/TT replay. **Mature host linear algebra, no novelty and no physical claim.**  
**STOP:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / ORIGINAL_RUNTIME_BYTE_EXACT_UNAVAILABLE / NO_NEW_TASK / TPE HOLD`.

## 0. Subtraction i znaczenie

ROT29 udowodnił nieidentyfikowalność pełnosieciowego RMS z pięciu masek nawet dla gładkiej niskopasmowej **gęstości energii**; sam pierwiastek tej gęstości nie musiał być skończenie pasmowy. ROT30 dostarczył oryginalne pola TT zależne wyłącznie od jednej współrzędnej i ostry próg: do stopnia 2 jednoznaczność, od stopnia 3 niejednoznaczność, **wyłącznie w tej jednowymiarowej podklasie**. ROT31 rozstrzyga, że taki próg nie obowiązuje po dopuszczeniu pełnej trójwymiarowej przestrzeni modów TT. Tu *sam tensor* jest pasmowy, dokładnie TT, a pięć pomiarów nadal nie określa jego normy pełnej.

Równoległe ustalenia INT8/Geeky-S11/PRF11/XH-S4 dotyczą nielokalności projekcji, transportu i komutatorów oraz różnych stencili. Nie są niniejszą nieidentyfikowalnością maskowanego pomiaru; nie przypisujemy sobie ich wcześniejszych wyników.

## 1. Ścisłe twierdzenie, zakres i minimalność

Pracujemy na okresowej siatce `N=41`, `L=2π`, z dokładnie tymi pięcioma wewnętrznymi sześcianami `Ω_k={k,...,40−k}^3`, `k=2,3,4,5,6`. Dla rzeczywistego symetrycznego tensora TT definiujemy `R_k(T)^2 = [6 |Ω_k|]^{-1} Σ_{x∈Ω_k} ||T(x)||_F^2`; pełne RMS to `R_0`. TT oznacza dokładnie zerowy ślad i dywergencję Fouriera, względem *stałego płaskiego projektora* `P_TT` z zachowanego helpera.

**Twierdzenie ROT31.1.** W klasie rzeczywistych tensorów TT, których niezerowe mody Fouriera spełniają `|m_x|,|m_y|,|m_z| ≤ 1`, istnieją `T_+`, `T_-` o identycznych pięciu wartościach `R_k(T_+)=R_k(T_-)` dla `k=2,...,6`, ale z `R_0(T_+)≠R_0(T_-)`. Dla pasma 0 (wyłącznie stały tensor bezśladowy) `R_0=R_k` dla każdej maski. Zatem dokładny próg jednoznaczności w *ogólnej* klasie wymienionych pasm to **0/1**. Nie znaczy to, że każda składowa TT lub każdy generator DTC ma taką niejednoznaczność.

### Dowód przez sześć modów i niezerowy minor w ciele skończonym

Przyjmij współrzędne centrowane `r=(j_x−20,j_y−20,j_z−20)`, `θ=2π/41`. Moduł fali `k` i symetryczny tensor `A` określają kosinusowy mod TT

`b_{k,A}(r)=cos(θ k·r) Π_k(A)`, 

z `P_k=I−kkᵀ/(k·k)` i `Π_k(A)=P_k A P_k−(1/2)P_k tr(P_k A)`. Dla `k≠0`, macierz `Π_k(A)` jest symetryczna, bezśladowa i poprzeczna. Wystarczą następujące **sześć** różnych fal:

```
k0=(-1,-1,0)
k1=(-1,-1,-1)
k2=(0,0,-1)
k3=(-1,1,-1)
k4=(-1,0,1)
k5=(-1,1,0)
```

Weź `A=diag(0,1,−1)`, `B0=Π_k0(A)` i `B_i=Π_ki(B0)` dla `i>0`. Niech `u(r)=b_{k0,A}(r)=cos(θ k0·r) B0`, `b_i(r)=cos(θ k_i·r) B_i`. Zdefiniuj `D_{s,i}=〈u,b_i〉_{Ω_s}` dla `s=0,2,3,4,5,6`, gdzie iloczyn Frobeniusa jest **uśredniony** po węzłach maski (normalizacja przez 6 jest wspólnym dodatnim czynnikiem, nieistotnym dla rzędu). Każdą komórkę `D` oblicza się dokładnie z

`〈cos(k·r),cos(l·r)〉_{Ω_s} = [∏_a d_{n_s}(k_a−l_a)+∏_a d_{n_s}(k_a+l_a)]/2`, 

`d_n(q)=(1/n) Σ_{j=−(n−1)/2}^{(n−1)/2} ζ^{qj}`, `ζ=exp(2πi/41)`, `n_s=41−2s`.

Te liczby należą do ciała cyklotomicznego `Q(ζ_41)`, a polaryzacje `B_i` są wymierne. Aby **ściśle** wykazać niezerowość wyznacznika, stosujemy homomorfizm redukcji do `F_821`, w którym `159^41 ≡ 1 (mod 821)` i `159≠1`. Ponieważ 41 jest pierwsze, 159 jest pierwotnym pierwiastkiem 41. stopnia, a `Φ_41(159) ≡0`. Wszystkie mianowniki (2,3, `n_s^3` itd.) są odwracalne modulo 821. Niezależny program czysto całkowity `verify_m13_rot31_exact.py` otrzymuje macierz:

```
      b0  b1  b2  b3  b4  b5
s=0   565   0   0   0   0   0
s=2   706 236 130 337 278  86
s=3    37 283 478 568 425 644
s=4   737 367 255 506 372 643
s=5   585 647  19 192 488 297
s=6    78  57 803 300 153 146
```

Wyniki dokładne: **`det(D_6x6) ≡247 (mod 821) ≠0`**, a wyznacznik podmacierzy masek i kolumn `b1,...,b5` to **`804 (mod 821) ≠0`**. Gdyby wyznacznik pierwotny był zerem w `Q(ζ_41)`, jego obraz przy poprawnej redukcji też byłby zerem; otrzymana niezerowość jest więc certyfikatem **ścisłym, a nie szacunkiem floating-point**.

Można zatem rozwiązać jednoznacznie pięć równań `Σ_{i=1}^5 c_i D_{s,i}=−D_{s,0}` dla `s=2,...,6`, ustawić `v=b0+Σ c_i b_i` i otrzymać `〈u,v〉_{Ω_s}=0` dla pięciu masek. Dla pełnej siatki kosinusy różnych fal są ortogonalne, więc `〈u,v〉_{Ω_0}=〈u,u〉_{Ω_0}>0`. Niech `T_±=u±v`: dokładnie

`R_s(T_+)²−R_s(T_-)² = (4/6)〈u,v〉_{Ω_s}=0`, `s=2,...,6`,

natomiast `R_0(T_+)²−R_0(T_-)²=(4/6)〈u,u〉_{Ω_0}>0`. Dowód zakończony. Wszystkie składniki mają 3D pasmo współrzędnych najwyżej 1 i należą do TT. Dla pasma 0 stała gęstość energii implikuje równość wszystkich RMS.

## 2. Wersja liczbowa lepiej uwarunkowana i kontrola w niezmodyfikowanym helperze

Niezależnie od sześciomodowego dowodu wybrano pełną bazę 26 rzeczywistych kosinusowych tensorów TT (po 2 niezależne polaryzacje dla 13 par `k,−k` w kostce `[-1,1]^3\{0}`). Nie użyto modów zerowych ani sin; kosinusy są centrowane na środku siatki. Baza ma tożsamościową macierz Grama dla pełnej siatki. Dla pięciu masek policzono dokładne analitycznie elementy macierzy Grama ze znormalizowanych sum Dirichleta. Algorytm o ustalonym ziarnie `20261024` wybiera `u`, a przez SVD konstruuje `v` ortogonalny do pięciu wektorów pomiarowych. Wybór najlepszy spośród 2000 kandydatów jest wyłącznie **kondycjonowaniem numerycznego przykładu**. Rygorystyczny dowód nie opiera się na SVD.

```
                  T_plus            T_minus
mask k=2      0.566664575126     0.566664575126
mask k=3      0.561571127609     0.561571127609
mask k=4      0.556875456197     0.556875456197
mask k=5      0.552795509056     0.552795509057
mask k=6      0.549585776196     0.549585776196
full k=0      0.578130912039     0.576568569393
```

Największy bezwzględny odstęp maskowanych RMS: `2.23×10^−14`. Globalna względna różnica RMS: `0.002706059318803925 = 0.2706059%`. Oryginalne, **niezmodyfikowane** funkcje pomocnicze `rms_norm` oraz `apply_P_TT` ze skryptu `deepseek_python_20260627_a87249.py` SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801` zostały wywołane bezpośrednio. Względny błąd `||P_TT T−T||_F/||T||_F` wyniósł `3.4237×10^−16` i `3.6429×10^−16` odpowiednio dla `T_plus` i `T_minus`. Tym samym oba pola są istotnie Fourier-TT na całej siatce.

Pełne wektory współczynników 26-modowych i polaryzacje znajdują się w dołączonym JSON, co eliminuje konieczność ponownego przeszukiwania losowych kandydatów. Skrypt sam regeneruje wynik i sprawdza równość. Dokładna konstrukcja sześciomodowa oraz stabilniejszy 26-modowy przykład to **dwa różne kontrmodele**, spełniające to samo ograniczenie pasma.

## 3. Zmiana decyzji naukowej, granice i najtańszy falsyfikator

**EARNED:** (i) ostry próg `0/1` dla opisanej *ogólnej trójwymiarowej* klasy Fourier-TT na N41 i pięciu maskach; (ii) pełna domena RMS nie jest funkcją pięciu pomiarów na tej klasie; (iii) realny przykład w zachowanym helperze TT przy masce i normalizacji DTC0a; (iv) dowód algebraiczny niezależny od niestabilności SVD; (v) ROT30 `2/3` nadal obowiązuje w swojej węższej jednowspółrzędnej podklasie.

**NOT EARNED:** niejednoznaczność w ściśle ograniczonej rodzinie residuali generowanych przez ustalone `C1,C2,h,alpha` (ROT23–27 pozwala dla tej rodziny odtworzyć pełny tensor), jakakolwiek własność fizycznej geometrii/gravitacji, dowód na odmienność historycznych pól przy tym samym skanie, czy generalizacja na nieznane normy / inne maski / wszystkie N bez osobnego dowodu. Brak bajtowo tożsamego historycznego `dtc0a_runtime_v0_3_1.py`, jego manifest SHA256 `2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084`. Zachowany alternatywny helper odtwarza historyczne normy według ROT23, ale nie jest oryginalnym runtime'em. `P_TT` przyjęty względem ustalonej euklidesowej metryki, nie geometrycznie transportowanego projektora.

**Cheapest check:** uruchom oba dołączone programy w pustym katalogu z helperem: exact modular certificate jest niezależny od NumPy, a numeric verifier wywołuje pełny oryginalny `apply_P_TT`. Ponieważ zagadnienie dotyczy **identyfikowalności**, nie prosimy Moderatora o nowy eksperyment fizyczny.

**Owner:** MT13; **custody:** KN11 / BW jeżeli później potwierdzi zapis; **referee:** niezależny REC10/SW niepotwierdzony. Nie stwierdzamy BW ingestion, owner acceptance ani EXEC. `NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / TPE HOLD`.