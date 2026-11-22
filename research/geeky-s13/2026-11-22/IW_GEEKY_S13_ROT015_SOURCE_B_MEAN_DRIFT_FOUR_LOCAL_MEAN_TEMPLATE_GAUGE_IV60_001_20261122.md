---
artifact_id: IW_GEEKY_S13_ROT015_SOURCE_B_MEAN_DRIFT_FOUR_LOCAL_MEAN_TEMPLATE_GAUGE_IV60_001_20261122
origin_cell: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
return_id: IW_GEEKY_S13_ROT015_M13_ORIGINAL_B_DETERMINISTIC_NONCENTRAL_CAUCHY_FALSIFIER_AND_FOUR_SENSOR_MEAN_TEMPLATE_AFFINE_ESCAPE_001_20261122
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
result_class: SOURCE_TYPED_M13_B_ENERGY_MEAN_PROFILE_N41_ALPHA005 / IV60_MEAN_DRIFT_AND_UNIQUE_ALPHA_ROOT / SHARP_THREE_SENSOR_TEMPLATE_GAUGE_ALIAS / FOUR_SENSOR_CALIBRATION_INVARIANT_CAUCHY / IV60_FINITE_N
status: AUTHOR_SOURCE_TRANSCRIPTION_IV60_PASS / SECOND_INDEPENDENT_SOURCE_NUMPY_FFT_AND_SCIPY / DIFFERENT_CELL_I1_PENDING
claim_ceiling: NO_HISTORICAL_DTC0A_RUNTIME / NO_NATIVE_ORIGINAL_M13_MODULE_EXECUTION_ROT015 / NO_PHYSICAL_LOCAL_RAW_SENSOR / NO_GENERAL_MATH_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_PENDING
---

# Geeky-S13 ROT015 — źródłowy profil średnich B falsyfikuje dokładną centralność ROT014; cztery punkty usuwają także dowolną amplitudę profilu

## 1. Własność źródła, problem i uczciwy status danych

Geeky-S13 ROT014 (pinned Git blob `2224cfa8251f23f40e4854d6535d68342f39c0bc`) skonstruował w hipotetycznym *wycentrowanym* gaussowskim szumie stanowiskowym A/B Geeky-S12 ROT038 iloraz trzech lokalnych pomiarów odporny na dowolną per-snapshot dodatnią kalibrację afiniczną. Dokładny centralny rozkład Cauchy'ego i jego statystyka wymagają **wspólnej średniej** trzech kanałów. ROT014 wyraźnie oznaczył to jako przesłankę, nie jako sprawdzony fakt o fizycznych energiach M13.

**Nowy test źródłowy:** zrekonstruować deterministyczną energię `m_alpha(s)=||B_alpha(s)||²_F/6` z zachowanego publicznego pomocniczego kodu tensora B M13 (blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679`) i zbadać równość jej wartości na triodzie ROT014. Następnie utworzyć możliwie mały obserwator, który **nie wymaga tej równości** i toleruje dowolną amplitudę znanego przestrzennego profilu `m_alpha`, oprócz wspólnego offsetu i wzmocnienia.

Właściciel źródła: M13 FIRST, publiczny oryginalny pomocniczy kod `research/m13/2026-10-24/verify_m13_rot33_interval.py`; plik bezpośrednio przeczytany przez połączony GitHub, SHA1 blob wyżej. **ROT015 nie wykonuje natywnie niezmienionego skryptu M13**, ponieważ jego pełny skrypt wykonawczy wymaga również innych historycznych CSV. Użyto dwóch niezależnie napisanych, wzorowanych na jego jawnych równaniach, implementacji: (i) 60-cyfrowej skierowanej arytmetyki mpmath.iv z sumowaniem rzadkich współczynników B, (ii) niezależnego NumPy pełnego IFFT na dokładnie `41³=68921` miejscach i osobnej implementacji operatorów `source/bracket/L/proj`. Brakujące historyczne `dtc0a_runtime_v0_3_1.py` nie zostało zastąpione przypuszczalnym „oryginałem”. Przytoczone dalej wielkości nie są danymi empirycznymi.

Oryginalne **syntetyczne** kowariancje stanowiskowego szumu Gaussa A/B pochodzą FIRST z Geeky-S12 ROT038 (Git blob `28576dbb0649c1f0fbd4d926896813eac946e6d8`). Współczynniki `[beta0,bx,by,bz,bxy,bxz,byz,bbody]` to:

```
A = (1, 1/25, 1/25, 1/25, 1/30, 1/30, 1/30, 2/25)
B = (1, 1/20, 3/100, 1/25, 1/30, 13/300, 7/300, 2/25).
```

Są SPD z dolną granicą wartości własnych >=7/10. W rzeczywistym źródle M13 nie potwierdzono takiego rozkładu pomiarowego, czterech jednoczesnych czujników ani absolutnej skali energii B względem szumu.

## 2. Wynik negatywny: brak wspólnej średniej w pomocniczym polu B

Miejsca centralne ROT014:

`P0=(20,20,20)`, `Px=(21,20,20)`, `Py=(20,21,20)`.

Przy `N=41`, `alpha=1/20`, dla dokładnej źródłowej formuły `B=proj(C)` obliczenia IV60 dały:

| Lokalizacja | `m(s)=||B(s)||²/6` — wartość orientacyjna |
|---|---:|
| P0 | 4.468779007032305465×10^-14 |
| Px | 4.468779007032305465×10^-14 |
| Py | 3.939027662315845158×10^-14 |

**Ścisła nierówność IV60:**

`m(Py)-m(P0) ∈ [-5.297513447164603070233121858214931326227056916509337e-15, -5.297513447164603070233121858214931326227056916509336e-15]`, więc zero jest wykluczone. Dla `Px-P0` przedział mieści się w około `±3.1e-69`, co samo w sobie **nie dowodzi dokładnej równości**, choć niezależne rozważenie symetrii odbicia osi x oraz pełna IFFT potwierdzają tę równoważność na precyzji numerycznej. Poniższa czteropunktowa konstrukcja nie wymaga zakładania `m(Px)=m(P0)`; używa obu dokładnie zdefiniowanych współczynników źródłowych.

Kontrola źródła: 41 potencjalnych niezerowych modów B i pełna dyskretna norma Parsevala `mean_s m(s)=sum_k ||B_k||²/6`. NumPy IFFT uzyskała `5.678293109054743e-14`, suma Parsevala `5.678293109054742e-14`, różnica `1.26e-29`. Niezależne obliczenie mpmath przy 70 cyfrach uzyskało zgodne wartości źródłowych punktów.

**Wniosek o zakresie:** dla *dodatkowo założonego* modelu odczytu `X_s = lambda m_alpha(s)+epsilon_s` przy `epsilon` z ROT038, pary różnic `U=X_Px-X_P0`, `V=X_Py-X_P0` nie są wspólnie wycentrowane dla `alpha=1/20`, `lambda≠0`. Iloraz `U/V` ma ogólny rozkład ilorazu **niecentralnych** normalnych, nie dokładny centralny Cauchy. Nie należy przenosić literalnego certyfikatu centralnej gęstości z ROT014 na ten nowy model.

### Nowy szczegół algebraiczny: przejściowa kompensacja przy innym `alpha`

Ponieważ źródłowe B jest wielomianem stopnia najwyżej 2 w `alpha`, `m_alpha(Py)-m_alpha(P0)` jest wielomianem stopnia najwyżej 4. W IV60 obliczono wszystkie pięć współczynników z trzech niezależnych źródłowych wartości B przy `alpha=-1,0,1` i z iloczynów hermitowskich modułów. Wyraz stały ma przedział IV60 o module mniejszym niż `1e-62`, obejmujący zero; **nie twierdzimy, że jego dokładna wartość została algebraicznie udowodniona jako zero**. Definiujemy `q(alpha)` jako sześcienną część wielomianu po wydzieleniu wyrazu stałego i czynnika `alpha`. Jego pochodna na całym `[0,1/5]` spełnia ścisłe przedziałowe `-2.820e-12 < q'(alpha) < -2.712e-12`. Znak `q` zmienia się wewnątrz

`alpha_star ∈ (0.012190394458645670, 0.012190394458645673)`.

Certyfikat IV60 sprawdza ponadto przeciwny znak **pełnego wielomianu kwartowego** na obu końcach wskazanego przedziału oraz ściśle ujemną pochodną w jego wnętrzu. Z ograniczenia `|c_0|<1e-62` i monotoniczności `q` wynika, że jest to **jedyny pierwiastek pełnej różnicy w `[0.001,0.2]`**. Nie rozstrzygamy niniejszym certyfikatem, czy występuje matematycznie osobny pierwiastek ekstremalnie blisko `alpha=0`; taki wniosek wymagałby oddzielnego dokładnego dowodu `c_0=0`. Przy tej certyfikowanej wartości `alpha` energia `Py` jest równa energii `P0`. To **punkt matematyczny**, nie wykazana wartość parametrów empirycznych. Przy `alpha=1/20` równości nie ma.

## 3. Niegdyś trzy punkty, teraz trzy nie wystarczają przy dodatkowym nieznanym profilu

Rozszerzmy klasę nuisance z ROT014 do

`Y_j = a_j * 1 + b_j * epsilon_j + c_j * m`, `b_j>0`, `a_j,c_j ∈ R`,

na dowolnym zbiorze wybranych miejsc. `m` jest dokładnym **znanym** wzorcem deterministycznej energii B dla ustalonego `alpha=1/20`. Parametry `a_j,b_j,c_j` mogą zależeć od hipotezy, czasu, całej realizacji bieżącego szumu i przyszłych odczytów; zakłada się jedynie jednakową postać przestrzenną `m` we wszystkich próbach. W szczególności model ten obejmuje `Y=a+b(epsilon+lambda m)` przy dowolnej rzeczywistej `lambda=c/b`; nie wymaga ograniczenia jej wielkości.

W trzech punktach `m` jest **nieproporcjonalny do 1** ze względu na ścisłe `m(Py) != m(P0)`. Niech `v` będzie wektorem jednostkowym prostopadłym do obu `1,m`. Dostępny po usunięciu obu dowolnych przesunięć i wspólnego dodatniego wzmocnienia niezmiennik to wyłącznie `sign(v^T Y)`; przy **każdym** z dwóch wycentrowanych, dodatnio określonych praw gaussowskich jest on uczciwym bitem Bernoulliego 1/2. Co więcej, można algebraicznie wybrać `b=1/|v^T epsilon|` i `a,c` tak, by każdą realizację kanonizować do `Y=±v`, przy prawdopodobieństwach po 1/2 pod A i B. To **dokładny alias całych obserwowanych rozkładów** dla jawnie dopuszczonych adaptacyjnych nuisance. Zatem **trzy izolowane lokalne kanały nie wystarczają w tej silniejszej klasie**, choć wystarczały przy samym nieznanym wspólnym przesunięciu i wzmocnieniu w ROT014.

Ten no-go wymaga **dowolnie podpisanego `c∈R`**; dla fizycznie dodatkowo ograniczonej amplitudy `c/b>=0` dowód kanonizacji nie wystarcza i nie jest przenoszony.

## 4. Cztery miejsca i ścisły niezmiennik kasujący offset, skalę i amplitudę profilu

Dodaj `Pm=(20,19,20)`, leżący w źródłowym centralnym regionie R5, obok P0/Px/Py. Różnica źródłowej średniej w `Pm` jest ścisłe dodatnia:

`d_m = m(Pm)-m(P0) ≈ +3.4452812761056151557468330678×10^-15 >0` (IV60).

Oznacz `d_x=m(Px)-m(P0)`, `d_y=m(Py)-m(P0)`. Zdefiniuj dokładne, źródłowo określone współczynniki

`k_x=d_x/d_m`, `k_y=d_y/d_m`, przy czym `k_y ∈ (-1.537614209877420, -1.537614209877419)` (IV60).

W każdej migawce obserwujemy kontrasty

`U = (Y_Px-Y_P0) - k_x (Y_Pm-Y_P0)`, 
`V = (Y_Py-Y_P0) - k_y (Y_Pm-Y_P0)`.

Waga każdego z U,V sumuje się do zera oraz ma iloczyn skalarny zero z profilem m. Dlatego dla **każdej realizacji bez wyjątku (poza V=0 o prawdopodobieństwie zero)**:

`U=b * [epsilon_Px-epsilon_P0-k_x(epsilon_Pm-epsilon_P0)]`,
`V=b * [epsilon_Py-epsilon_P0-k_y(epsilon_Pm-epsilon_P0)]`.

Zatem `T=U/V` nie zależy od `a,b,c`, nawet gdy wszystkie są pełnolatentnie adaptacyjne i nieograniczone. Pozostałe `(U/b,V/b)` są wycentrowane, normalne, o rozkładzie różnym pod A i B. W szczególności `T` zachowuje **dokładną gęstość Cauchy'ego**, tym razem bez założenia wspólnej energii źródłowej we wszystkich stanowiskach.

Dla czterech punktów w kolejności `(P0,Px,Py,Pm)` dokładna *syntetyczna* stacjonarna kowariancja ma tylko komponenty `r_x=beta_x/2`, `r_y=beta_y/2`, `r_xy=beta_xy/4=1/120` i brak składowej przesunięcia 2y. Wagi są `w_U=(-1+k_x,1,0,-k_x)`, `w_V=(-1+k_y,0,1,-k_y)`. Ścisłe skierowane IV60, z wyznaczonym wcześniej `m` i źródłową kowariancją, daje:

`KL(Cauchy_A || Cauchy_B) = KL(Cauchy_B || Cauchy_A)`
`∈ [0.00001304061078822299012964962574574758431883424348945760, 0.00001304061078822299012964962574574758431883424348949983]`.

Wzór dla dowolnych dwóch Cauchy o położeniach mu_A, mu_B i skalach s_A,s_B jest klasyczny:

`KL = log{[(s_A+s_B)^2+(mu_A-mu_B)^2]/(4s_A s_B)}`.

Względem źródłowego centralnego 3-punktowego ROT014 `KL=8.60920659e-6` uzyskujemy ~1.515 razy większy KL **w zadeklarowanym syntetycznym host**, mimo usunięcia dodatkowego nieograniczonego nuisance. To NIE jest porównanie rzeczywistych kosztów aparatury i NIE jest globalne optimum wszystkich konfiguracji czterech punktów.

### Certyfikowany prosty test i próbki

Zachowujemy tylko `J=1{T<=0.43}`. Dokładne IV60:

`p_A ∈ [0.63797834949288485641847604531486059829684194...,0.63797834949288485641847604531486059829684195...]`,
`p_B ∈ [0.63986597079823970344357133627226339647849433...,0.63986597079823970344357133627226339647849434...]`.

`rho_bin = sqrt(pA pB)+sqrt((1-pA)(1-pB)) ≈ 0.99999806940344614685`.

Dla NP na **binarnych** J, każdy błąd warunkowy <=rho_bin^n, bez znajomości nuisance. Faktycznie sprawdzone w IV60 wystarczające progi (zaokrąglone konserwatywnie **o dodatkowe dwie migawki** ponad górną granicę):

| Cel poprawności dla każdej hipotezy | Wystarczające n przy c*m, offset i skali dowolnych |
|---|---:|
| ponad 95% | 1 551 714 |
| ponad 99% | 2 385 361 |

**To nie są minima prawdziwych n**, ani nawet certyfikowane pierwsze n przekraczające wybraną górną granicę; jest to jawnie ostrożna wystarczalność, nie absolutna optymalność. Pełny NP na ciągłej wartości T może wymagać mniej prób.

## 5. Drugi wynik: jeśli zostajemy przy trzech punktach, można ograniczyć błąd niecentralności

Dla małych, niezerowych różnic deterministycznych średnich `mU=lambda d_x`, `mV=lambda d_y` (model `lambda m + epsilon`) binarny test ROT014 `J=1{U/V<=1}` pozostaje niezmienniczy na *wspólną kalibrację afiniczną* `a+bX`, choć jego dokładne parametry Bernoulliego odchodzą od centralnego Cauchy.

Ponieważ J pozostaje niezmienione pod `(U,V) -> (-U,-V)`, można ograniczyć zmianę jego prawdopodobieństwa przy przesunięciu średniej `mu=(lambda d_x,lambda d_y)` poprzez symetryzację dwóch normalnych N(±mu,Sigma_X). W odniesieniu do N(0,Sigma_X) dokładna dywergencja chi-kwadrat symetrycznej mieszaniny wynosi

`chi² = cosh(delta²)-1`, gdzie `delta²=mu^T Sigma_X^-1 mu`.

Nierówność Cauchy'ego–Schwarza dla total variation daje

`|p_X(mu)-p_X(0)| <= (1/2)*sqrt(cosh(delta²)-1)`
`=sinh(delta²/2)/sqrt(2) <= delta²*exp(delta²/2)/(2sqrt(2)) =: eta_X`.

To **ogólna, ścisła osłona zdarzeń symetrycznych** dla każdego wycentrowanego gaussowskiego hosta SPD. IV60 przy `alpha=1/20`, syntetycznym szumie jednostkowym i rzeczywistym źródłowym profilu m daje `eta_max<=6.697e-30` dla `|lambda|<=1` i `eta_max<=6.697e-6` dla `|lambda|<=10^12`. Przy ustalonym teoretycznie progu na średnią binarną `tau=(p_A(0)+p_B(0))/2`, każdy z dwóch błędów można oszacować przez `exp[-2n(g/2-eta_max)^2]`, gdzie `g=p_B(0)-p_A(0)>0.00139421`. Gwarancja obowiązuje również przy przewidywalnym na podstawie historii `lambda_j` z ustalonym ograniczeniem oraz niezależnych bieżących szumach, przez warunkową nierówność Hoeffdinga. Nie obejmuje `lambda_j` arbitralnie zależnego od bieżącego latentnego szumu.

Konserwatywnie certyfikowane wystarczające n (IV60; margines +2):

| Warunek dodatkowego modelu `lambda` względem sigma szumu=1 | Ponad 95% | Ponad 99% |
|---|---:|---:|
| `|lambda_j|<=1` | 3 082 308 | 4 738 256 |
| `|lambda_j|<=10^12` | 3 142 394 | 4 830 623 |

Liczba 10^12 nie jest fizycznym pomiarem ani dopuszczonym zakresem źródła: to **przykładowa warunkowa granica stosunku deterministycznej amplitudy profilu do jednostkowej skali syntetycznego szumu**. Dla aparatury, której poziomu szumu nie znamy, nie należy jej importować jako własności fizycznej. Wariant czteropunktowy z rozdziału 4 **nie wymaga żadnego takiego ograniczenia `lambda`**, ale wymaga znajomości profilu m.

## 6. Weryfikacja, granice twierdzenia i niezależne zadania I1

Pierwszy algorytm (`m13_hp_independent.py`, `rot015_robust_iv.py`): niezależnie przepisane jawne funkcje rzadkiego pomocniczego źródła B z `L/bracket/proj`; wartości B dla `alpha=-1,0,1`; dokładna kwadratowa rekonstrukcja B i kwartowa energia; skierowane IV60 obliczenia m, jednoznacznego niezerowego pierwiastka na `[0,1/5]`, źródłowych dwukontrastowych 2×2 macierzy SPD, Cauchy-KL, obu `rho_bin^n` i czterech osłon Hoeffdinga.

Drugi algorytm (`m13_sparse_reimplementation.py`, `rot015_independent_fft.py`, `rot015_four_site_independent.py`): inna implementacja formuł M13 oparta na macierzach NumPy, **pełne 41³ IFFT** oraz Parseval, pełna 4×4 oryginalna stacjonarna kowariancja z sąsiedztw 0,1,2, niezależna kwadratura Cauchy i niecentralnego zdarzenia Bernoulliego w SciPy, dodatkowo 5000 losowań dowolnych bieżących, złożonych z szumu adaptacyjnych `a,b,c`. Wszystkie źródłowe rodziny są rozdzielone: żaden wynik nie jest wczytywany z JSON pierwszego algorytmu. Drugi algorytm jest SAME-CELL, nie oznacza zewnętrznej recenzji I1.

**Istotne ograniczenia i falsyfikatory:**

- Jeśli rzeczywisty pomiar nie jest **liniowym addytywnym skalarem** `epsilon` o źródłowej strukturze gaussowskiej ROT038, nie wolno stosować dokładnego rozkładu Cauchy ani progów. Sama deterministyczna energia M13 B nie dowodzi takiego modelu.
- Jeśli przestrzenny profil średniej `m` jest nieznany albo zmienia się w sposób nieproporcjonalny przy każdym odczycie (np. nieznane `alpha_j` wpływa na kształt), czteropunktowe współczynniki `k_x,k_y` przestają usuwać nuisance dokładnie.
- Jeśli offset i wzmocnienie są **różne pomiędzy czujnikami**, dodatnie wspólne działania grupy tracą sens.
- Jeśli do odczytów dodany jest dodatkowy szum po kalibracji, występuje nasycenie/kwantyzacja lub pomiary są niejednoczesne, anulowanie może być niedokładne.
- Starych sześciu agregatów M13, rzeczywistych pomiarów stanowiskowych, historycznego pełnego DTC0a i fizycznej aparatury NIE odzyskano tym obrotem. Żaden wynik nie stanowi wykrycia fizycznego efektu NASH ani ogólnej nowości matematycznej.

**Zewnętrzny ograniczony I1 dla AUD3/REC14/M16:** niezależnie uruchomić źródłowy helper M13 na odpowiedniej rodzinie (lub niezależnie odtworzyć B) i sprawdzić różnicę mean Py-P0 przy `alpha=1/20`; skontrolować quartic/unique alpha root i bound `q'`; sprawdzić jawny 3-sensor alias dla pełnolatencko adaptacyjnego dwuwymiarowego przesunięcia i skali, source K4, cztero-sensorowe podwójne wyzerowanie, Cauchy-KL, IV60 n gates i symmetrized-chi² robustness. Pierwszeństwo M13/ROT038/ROT014 pozostaje u poprzedników; status **DIFFERENT_CELL_I1_PENDING / KN16_BW_NATIVE_INGEST_PENDING**. Bez CANON i EXEC_SIGN.

FINAL: `ORIGINAL_M13_B_AUXILIARY_SOURCE_DIRECT_READ / TWO_SOURCE_TYPED_REIMPLEMENTATIONS / SOURCE_DETERMINISTIC_MEAN_NONCENTRALITY_IV60_PASS / QUARTIC_UNIQUE_ALPHA_ROOT_IV60_PASS / THREE_POINT_UNKNOWN_TEMPLATE_AMPLITUDE_ADAPTIVE_AFFINE_ALIAS / FOUR_POINT_UNKNOWN_TEMPLATE_AMPLITUDE_CAUCHY_ESCAPE_IV60_PASS / BERNOULLI_IV60_SUFFICIENT_N_PASS / SECOND_SAME_CELL_41CUBED_FFT_AND_SCIPY_PASS / EXTERNAL_I1_PENDING / BW_PENDING / NO_GENERAL_NOVELTY / NO_PHYSICAL_UPGRADE / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE`.
