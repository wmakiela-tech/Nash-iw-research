---
artifact_id: IW_GEEKY_S13_ROT020_UNKNOWN_ETA_COMMON_Q_REFERENCE_SHARP_ALIAS_TWO_SENTINEL_IV75_001_20261123
return_id: IW_GEEKY_S13_ROT020_UNKNOWN_CONTAMINATION_FRACTION_REFERENCE_Q_SHARP_LIKELIHOOD_RATIO_ALIAS_TWO_SOURCE_SENTINELS_001_20261123
origin: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
date: 2026-11-23 Europe/Warsaw
exposure: PUBLIC
scope: ORIGINAL_M13_N41_FOUR_MIRROR_GEOMETRY_PLUS_ROT038_SYNTHETIC_GAUSSIAN_A_B_CAUCHY_OUTPUT / HYPOTHETICAL_SEPARATE_FAULT_ONLY_REFERENCE
status: AUTHOR_EXACT_ANALYTIC_SOURCE_PROOF / OUTWARD_IV75_NUMERICS / INDEPENDENT_SAME_CELL_SCIPY_AND_SYMBOLIC_SOURCE_WITNESSES / COLD_REPLAY / DIFFERENT_CELL_I1_PENDING
claim_ceiling: NO_GENERAL_MATH_NOVELTY / NO_REAL_FAULT_ONLY_REFERENCE / NO_NATIVE_ORIGINAL_M13_EXECUTION_THIS_ROTATION / NO_HISTORICAL_FULL_DTC0A_RUNTIME / NO_PHYSICAL_SENSOR / NO_CANON / NO_EXEC_SIGN / BW_PENDING
---

# Geeky-S13 ROT020 — ostry alias przy nieznanym udziale skażenia pomimo referencji Q; dwa źródłowe przedziały przywracają identyfikowalność poniżej progu

## 0. Pytanie, odpowiedź i pierwszeństwo

**Pytanie:** ROT019 naprawił nieznany wspólny rozkład awarii Q za pomocą niezależnych obserwacji z Q, ale założył ZNANY udział η. Czy samo nieograniczone zwiększanie liczby odczytów z Q wystarcza, jeśli także η jest nieznane? **Nie:** przy horyzoncie `η∈[l,h]` istnieje dokładny FULL-LAW alias *obu rozkładów łącznych* `(R,Q)`, jeśli i tylko jeśli

`h >= 1 - (1-l)/M`, `M=sup(f_B/f_A)=sup(f_A/f_B)=sqrt(350455)/589 ≈1.0050804730048334266`.

Dla l=0 ostry próg `h*=1−589/sqrt(350455)≈0.0050547922691648936630` (0.505479%). Alias osiąga jawna **ta sama gładka gęstość Q w obu światach**, lecz różne udziały η. Nie ma sprzeczności z ROT019: tam η było znane, tu η jest parametrem zakłócającym zmieniającym się między dopuszczalnymi alternatywnymi światami. Jeżeli nakazuje się zewnętrznie tę SAMĄ NUMERYCZNĄ wartość η w obu porównywanych światach, taka swoboda znika — ale to już wiedza o η wykraczająca poza obecny kontrakt.

Drugi wynik: poniżej ostrego progu, przy `η∈[0,0.004]`, istnieją **dwa jawne pojedyncze zdarzenia** `E_minus`, `E_plus`, które wraz z odczytami referencyjnymi Q dają jednostajny test przy dowolnym kształcie Q, z IV75 certyfikatem źródłowego odstępu i skończonej próby. Jeden starszy bit NP z ROT018/019 traci natomiast identyfikowalność już przy `η≈0.00322094227355140079`, mimo że cały rozkład nadal ją zachowuje do `h*`.

**Pierwszeństwo zachowane:** M13 pierwszy publiczny pomocniczy tensor B (Git blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679`); Geeky-S12 ROT038 pierwszy dokładny racjonalny syntetyczny anizotropowy model szumu A/B (blob `28576dbb0649c1f0fbd4d926896813eac946e6d8`); Geeky-S13 ROT016 pierwszy oryginalno-geometryczny czteropunktowy iloraz Cauchy'ego i symetria odbicia (blob `cddc2636249e9bf032fff4de78afb30481401f9a`); Geeky-S13 ROT017 pierwszy zakres jednego bitu dla ograniczonych błędów AMPLITUDY (blob `90b7a9f6fafbc3a46d9aaed01d8223bcf0ff1a43`); ROT018 pierwszy pełny TV i dwa ostre promienie różnych modeli skażenia (blob `a7c4d7514fc1aa17a0b49c1c0a73d772ca8cf4ff`); ROT019 pierwszy tutaj audyt nieznanego Q przy **znanym η** i bitowej referencji (blob `b3b0eaf5389adf6fe1831d68b8aa29ad9fa699f7`). W niniejszym obrocie bezpośrednio odczytano kompletne przypięte raporty ROT018/ROT019 przez połączony GitHub. Oryginalny moduł M13 NIE był wykonany natywnie. HISTORYCZNY pełny DTC0a runtime pozostaje niedostępny. Nie deklarujemy nowości ogólnej.

Zewnętrzne źródła (rzeczywiście znalezione i sprawdzone na powierzchni wyszukiwarki): Blanchard i Scott, *Decontamination of Mutually Contaminated Models*, PMLR 2014, https://proceedings.mlr.press/v33/blanchard14.pdf ; Zhu et al., *Mixture Proportion Estimation Beyond Irreducibility*, ICML/PMLR 2023, https://proceedings.mlr.press/v202/zhu23c.html ; Sanderson i Scott, *Class Proportion Estimation*, PMLR 2014, https://proceedings.mlr.press/v33/sanderson14.pdf. Teoria identyfikowalności proporcji mieszanin, irredukowalności i ilorazów gęstości jest DOJRZAŁYM HOSTEM, nie odkryciem ogólnego narzędzia w ROT020.

## 1. Kontrakt eksperymentu i ścisłe parametry Cauchy'ego

Cztery IDEALNE równoczesne odczyty na oryginalnym torusie 41³ w punktach `P0=(20,20,20),P1=(21,20,20),Q0=(20,21,20),Q1=(21,21,20)` z ROT016 oraz syntetyczne gaussowskie kowariancje ROT038 dają niezmiennik T=U/V, usuwający wspólny offset i dodatnią skalę przy źródłowo dokładnym odbiciu średniej energii. To postulowany eksperyment, NIE dostępne dane z oryginalnych sześciu masek M13.

`P_A = Cauchy(a=1/84, s_A=sqrt(1-a²))`;
`P_B = Cauchy(b=4/585, s_B=sqrt(1-b²))`;
`f_X(t)=s_X/[pi(t²−2μ_X t+1)]` na całej prostej rzeczywistej. Pod A/B czyste T są IID, z czego nie wynika prawdziwość IID danych rzeczywistej aparatury.

Główne odczyty `Y_1,...,Y_n IID~R_(X,η,Q)=(1−η)P_X+η Q`; obserwacje referencyjne `Z_1,...,Z_m IID~Q` niezależne od Y, z tym SAMYM Q; udział η nieznany, ale ograniczony do `[l,h]`, gdzie `0<=l<=h<1`. W obrębie konkretnego świata η,Q są stałe, ale wartości parametrów zakłócających MOGĄ BYĆ INNE w dwóch możliwych światach statystycznych X=A oraz X=B. Skażenie egzogeniczne: decyzja o wyborze gałęzi Q nie jest funkcją aktualnego czystego T. Referencja mierzy rzeczywiście Q, nie próbę zanieczyszczoną nowym, innym rozkładem.

## 2. Ostry alias pełnego prawa ŁĄCZNEGO `(R,Q)` i jego warunek konieczny

Niech `L(t)=f_B(t)/f_A(t)=[s_B/s_A]*(t²−2a t+1)/(t²−2b t+1)`. Dokładne różniczkowanie daje

`L'(t)=[2 s_B/s_A]*(b−a)*(1−t²)/(t²−2b t+1)²`.

Ponieważ `a>b>0`, maksimum `L` występuje w `t=−1`, minimum w `t=+1`. Dzięki `s_X²=1−μ_X²` otrzymujemy analitycznie:

`max L = max(1/L) = M = sqrt{[(1+a)(1−b)]/[(1−a)(1+b)]} = sqrt(350455)/589`.

Załóżmy, że dwa możliwe światy `(A,η_A,Q)` i `(B,η_B,Q)` mają identyczne prawo referencji Q i identyczne prawo pracy R. Jeśli `η_A=η_B<1`, równość wymaga `P_A=P_B` — sprzeczność. Jeśli `η_B>η_A`, równość gęstości wymusza

`(1−η_A) f_A(t) − (1−η_B) f_B(t) = (η_B−η_A)q(t) >=0`

prawie wszędzie; brak składowej osobliwej Q jest konieczny, bo różnica lewa ma tylko część absolutnie ciągłą. W punkcie `t=-1` wynika `(1−η_A)/(1−η_B) >=M` (ciągłość i dodatnie otoczenie dają warunek także dla równości a.e.). Maksymalny możliwy iloraz w `[l,h]` to `(1−l)/(1−h)`. Zatem konieczne `h>=1−(1−l)/M`. Dla gałęzi `η_A>η_B` używamy zamiast tego `t=+1` i `max(f_A/f_B)=M`, co daje identyczny warunek.

### Konstrukcyjna osiągalność

Dla każdego `l<1`, wybierz

`η_A=l`, `η_B=h_c(l)=1−(1−l)/M=l+(1−l)(1−1/M)`;

`q_*(t)=[f_A(t)−f_B(t)/M]/[1−1/M]`.

Ta SAMA gęstość `q_*` działa dla wszystkich dolnych końców l. Jest nieujemna w każdym t z definicji M, całkuje się do 1, a w punkcie t=−1 ma dokładne zero drugiego rzędu:

`q_*(t)=C*(t+1)²/[pi*h_*(t²−2a t+1)(t²−2b t+1)]`,

`h_*=1−1/M`, `C=s_A−s_B/M>0`.

Bezpośrednie podstawienie:

`(1−l)P_A+l Q_* = (1−h_c(l))P_B+h_c(l)Q_*`.

Obie hipotezy mają więc IDENTYCZNE rozkłady robocze i identyczne referencyjne Q*. Dla dowolnej liczby n i m ich pełne joint laws są takie same: przy równych priors błąd minimax 50%. Dla `h>h_c(l)` można nadal przyjąć `η_B=h_c(l)` z dozwolonego przedziału. **Warunek jest konieczny i wystarczający.** Nie używamy sztucznego atomu Diraca; świadek jest gładką i normalizowaną gęstością.

Dokładne ekstremum `M=sqrt(350455)/589` potwierdził oddzielny program SYMPY bez danych liczbowych z programu IV. Program IV75 podaje

`h_* ∈ [0.005054792269164893663023825620710761726592836604780385340947368031120317501887348, 0.0050547922691648936630238256207107617265928366047803853409473680311203175031309562]`.

## 3. Dlaczego dotychczasowy JEDEN bit zawodny jest przed progiem pełnego prawa

Źródłowy bit `J_E=1{T∈E}` ROT018/019, gdzie E to dwa ogony wyznaczone równaniem fA=fB, ma `p_A≈0.4991934655311292`, `p_B≈0.5008065344688708`, `δ=p_B−p_A≈0.00161306893774156`. Nawet gdy Q jest referencyjnie ZNANE, dla `Q(E)=1`, `η_A=δ/(1−p_A)`, `η_B=0` mamy identyczne Bernoulli work pB i identyczne reference Bernoulli q=1. Ostry świadek aliasu TEGO BITU:

`h_bit = δ/(1−p_A)≈0.00322094227355140079118` = 0.322094%.

**Wniosek:** dla `0.322094%<=h<0.505479%` jeden dawny bit może być nieinformatywny, podczas gdy PEŁNY rozkład nadal rozróżnia A/B przy wspólnym referencyjnym Q. To nowy dla tej linii ilościowy NEGATIVE CONTROL przeciw pomyleniu informacji bitowej z pełnodystrybucyjną. Nie twierdzimy, że dowolny pojedynczy możliwy bit zawodzi w tej całej strefie.

## 4. Konstruktywny, jednostajny test DWÓCH zdarzeń przy η<=0.004

Niech `l=0`, `h=1/250=0.004 < h_*`, `κ=(1−l)/(1−h)=1/(0.996)`. Wybierz dwa źródłowe optymalne *dla dwóch przeciwnych kierunków* zdarzenia:

`E_-={t: f_B(t)/f_A(t)>κ}`;
`E_+={t: f_A(t)/f_B(t)>κ}`.

To dwa ROZŁĄCZNE ograniczone przedziały (ponieważ κ>1):

`E_-≈(-2.0529929048447786444, -0.4870937437923621812)`;
`E_+≈(0.4942090846757708811, 2.0234350824531211804)`.

Każdy przedział otrzymujemy z dokładnego kwadratu `(s_B−κ s_A)(t²+1)+2(κ s_A b−s_B a)t=0` lub analogicznego po odwróceniu A/B. Obliczamy jego masę z dokładnego Cauchy CDF, nie z obcięcia ogonów. Zewnętrznie skierowana IV75 daje oba dodatnie odstępy

`γ_-=(1−h)P_B(E_−)−(1−l)P_A(E_−)>0`;
`γ_+=(1−h)P_A(E_+)−(1−l)P_B(E_+)>0`,

`γ = min(γ_-,γ_+)∈[0.00014668409539958040277040982999839026423711992869689597708351942709939336480324195,0.0001466840953995804027704098299983902642371199286968959770835194270993937865591695]`.

**Dlaczego dwa zdarzenia wystarczają dla KAŻDEGO Q:** jeśli porównywane dopuszczalne udziały spełniają `η_B>=η_A`, na E_- zachodzi

`R_B(E_−)−R_A(E_−)=(1−η_B)P_B(E_−)−(1−η_A)P_A(E_−)+(η_B−η_A)Q(E_−)>=γ_-`.

Jeśli `η_A>=η_B`, na E_+ mamy `R_A(E_+)−R_B(E_+)>=γ_+`. Przynajmniej jedno z dwóch źródłowych zdarzeń oddziela każde dwie kompozytowe hipotezy od siebie o co najmniej γ, przy tym SAMYM referencyjnym Q. Ten dowód obejmuje również dokładnie równe eta. Zależy wyłącznie od ilorazu gęstości i nieujemności Q(E), nie od kształtu awarii.

### Jawny test i koszt

Z n roboczych i m referencyjnych próbek zbierz dwie częstości `rhat=(mean 1_E-(Y),mean 1_E+(Y))` oraz `qhat` analogicznie dla Z. Dla każdej hipotezy X minimalizuj po jednej nieznanej liczbie η z `[0,h]`:

`d_X=min_{η∈[0,h]} ||rhat-[(1−η)p_X+η qhat]||_∞`,

z `p_X=(P_X(E_-),P_X(E_+))` dokładnie znanym z czystego Cauchy. Wybierz X o mniejszym d_X (ties dowolnie). Jeśli odchylenia obu częstości głównych mają moduł ≤a, a obu referencyjnych ≤b, to `d_true<=a+h b`, zaś `d_false>=γ-(a+h b)`. Wystarczy zatem `2(a+h b)<γ`.

Hoeffding + suma czterech dwustronnych zdarzeń daje `P(error) <= 4 exp(-2 n a²)+4 exp(-2 m b²)` dla KAŻDEGO Q i eta∈[0,h]. Wybierz `K=ln(8/α_err)`, `a=sqrt(K/(2n))`, `b=sqrt(K/(2m))`; wtedy łączny błąd ≤α_err, o ile `γ-2(a+h b)>0`. Program IV75 certyfikuje STRICT oba następujące dodatnie marginesy:

| Cel na każdą hipotezę | n robocze | m fault-only | γ-2(a+h b), IV75 — wartość przybliżona |
|---|---:|---:|---:|
| >95% | **496,000,000** | **12,500,000** | `+2.57190932914e−8` |
| >99% | **654,000,000** | **16,500,000** | `+1.07172992125e−7` |

To NIE minima n,m. Są to bardzo konserwatywne gwarancje prostej metody dwuzdarzeniowej, o znacznie większym koszcie niż w ROT019 przy ZNANYM eta. W obrębie tego akurat oszacowania Hoefdding–union i równych kosztów orientacyjna alokacja ciągła ma `m/n≈h^(2/3)=0.0251984`; NIE przenosimy automatycznie alokacji `m/n=eta` z ROT019, bo kontrakt testu i jego granice są inne. Dane rzeczywistego czujnika NASH, tryb Q i skalowalność takiej próby NIE zostały wykazane.

## 5. Trzy faktycznie wykonane, różne sprawdzenia

1. `rot020_primary_iv75.py`: oryginalne RATIONAL a,b, kierunkowy `mpmath.iv` z `iv.dps=75`, dokładny `M`, przedział h*, kwadratowe E±, Cauchy CDF, oba źródłowe odstępy γ, poprzedni jedno-bitowy alias wyliczony OD NOWA z rootów ROT018, cztery nierówności skończeniepróbkowe (dwa cele x n/m). Wynik `ROT020_PRIMARY_IV75.json`.
2. `rot020_independent_scipy.py`: osobna implementacja NUMPY+SciPy, wyznacza ekstremum z gęstości, dwa wydarzenia poprzez `brentq`, wszystkie masy przez osobne całkowanie `scipy.integrate.quad`, skonstruowaną gładką gęstość q_*, jej całkę na R oraz bezpośredni residual równania mieszaniny na gęstej siatce. To numeryczna DIAGNOSTYKA samej komórki, NIE nowy rygorystyczny IV i NIE different-cell I1.
3. `rot020_symbolic_witness.py`: całkowicie niezależna arytmetyka algebraiczna SYMPY, która w symbolach potwierdza `M=sqrt(350455)/589`, dokładną pochodną ilorazu, wyłączenie `(t+1)²`, podwójne zero gładkiego Q oraz identity całej mieszaniny z dowolnym l∈[0,1). Wynik `ROT020_SYMBOLIC_WITNESS.json`.

Dodatkowo archiwum przenośne zawiera 2 wcześniej naprawdę odczytane raporty źródłowe ROT016/019, niezależny kontroler integralności i pięć celowo sfałszowanych zestawów danych z przeliczonymi sumami w testach negatywnych. Same kontrole autorskie NIE są niezależnym I1.

## 6. Granice wniosków i zlecenie niezależnego I1

- Wyniki odnoszą się do **HIPOTETYCZNEGO** czteropunktowego RAW eksperymentu z syntetyczną kowariancją gaussowską ROT038 i dokładną symetrią M13 B; nie są stwierdzeniem o oryginalnych sześciu agregatach ani aparaturze fizycznej.
- Obecność czterech jednoczesnych czujników RAW oraz oddzielnego niezależnego trybu obserwacji fault-only Q nadal jest NIEPOTWIERDZONA. Założenie IID i stałego η w jednej realizacji również wymaga walidacji.
- Referencja Q jest WSPÓLNA w obu porównywanych światach; nie wolno zastępować dowodu aliasu konstrukcją Q_A≠Q_B z ROT019, bo tu dajemy mocniejszy kontrprzykład Q_A=Q_B=Q_*.
- Próg h* nie jest prawdopodobieństwem pojedynczej podmiany warunkowanej aktualną wartością, a założenie gałęzi skażenia egzogenicznego nie obejmuje ROT018 TV-postselection.
- Przy niezależnym zewnętrznym certyfikacie η (np. przedział `[l,h]`), porównuj jego szerokość ze źródłową ścisłą granicą `h−l<(1−l)h*`. Błędna estymacja η może przywrócić alias.
- Nie ma deklaracji, że dwie wybrane sentinel-biny są globalnie optymalne ani że wzrost do ~508 mln obserwacji jest wykonalny.
- Priorytet niezależnego AUD3/REC14/M16 I1: sprawdzenie `M=√350455/589`, ostrych kwantyfikatorów Q wspólny i η różne, gładkiego `q_*`, dwóch ekstremów zdarzeń E±, źródłowego IV75 γ, granic 2(a+h b)<γ oraz fałszywego wniosku „jeden bit zawsze wystarczy”.

**Sufit:** `AUTHOR_EXACT_ANALYTIC_ALIAS_PASS / AUTHOR_SYMPY_TANGENT_Q_PASS / IV75_TWO_EVENT_SOURCE_PASS / SAME_CELL_SCIPY_PASS / EXTERNAL_DIFFERENT_CELL_I1_PENDING / BW_INGEST_PENDING / NO_GENERAL_NOVELTY / NO_PHYSICAL_UPGRADE / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE`.
