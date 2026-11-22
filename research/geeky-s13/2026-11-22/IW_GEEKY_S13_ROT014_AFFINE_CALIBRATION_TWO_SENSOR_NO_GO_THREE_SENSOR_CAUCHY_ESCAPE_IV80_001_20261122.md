---
artifact_id: IW_GEEKY_S13_ROT014_AFFINE_CALIBRATION_TWO_SENSOR_NO_GO_THREE_SENSOR_CAUCHY_ESCAPE_IV80_001_20261122
origin_cell: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
return_id: IW_GEEKY_S13_ROT014_ORIGINAL_M13_ROT038_THREE_LOCAL_AFFINE_GAIN_INVARIANT_CAUCHY_AND_TWO_LOCAL_NO_GO_001_20261122
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
result_class: SOURCE_TYPED_N41_SYNTHETIC_ANISOTROPIC_GAUSSIAN_THREE_LOCAL_SENSOR_AFFINE_NUISANCE_MINIMALITY_AND_IV80_FINITE_N
status: AUTHOR_EXACT_RATIONAL_SOURCE_THEOREM / PRIMARY_IV80 / INDEPENDENT_SAME_CELL_SPATIAL_FFT_AND_SCIPY / COLD_REPRO_PASS_3_JSON_BYTE_IDENTICAL / DIFFERENT_CELL_I1_PENDING
claim_ceiling: NO_GENERAL_MATHEMATICAL_NOVELTY / NO_ORIGINAL_M13_PHYSICAL_SENSOR / NO_HISTORICAL_FULL_DTC0A / NO_CANON / NO_EXEC_SIGN / BW_PENDING
---

# Geeky-S13 ROT014 — dwa surowe punkty nie wystarczają przy nieznanej kalibracji afinicznej; trzy lokalne punkty przywracają dokładną informację Cauchy’ego

## 0. Pytanie i rygor zakresu

Geeky-S13 ROT013 pierwszy źródłowo wyczerpująco wykazał, że dołączenie JEDNEGO dowolnego surowego punktu do sześciu starych liniowych masek M13 niesie przy A/B bardzo niewiele informacji (maksymalnie KL~4.94423557252e-8 na niezależną migawkę), a DWA sąsiednie punkty przy ZNANEJ normalizacji gaussowskiej dają KL~1.25204875693e-5 i wystarczające n=957177 dla >95% ze znanego współczynnika Bhattacharyyi. ROT012 pierwszy udowodnił nieodtwarzalność czteromodowego kontrastu Fouriera z samych sześciu masek. ROT007–011 wcześniej zajmowały się zupełnie inną grupą kierunkowo-promieniowych kalibracji czterech modów.

**NOWE pytanie:** co przetrwa, kiedy w każdej pojedynczej migawce WSZYSTKIE lokalne czujniki mają wspólne, zupełnie nieznane i dowolnie zależne od danych **przesunięcie i dodatnie wzmocnienie** `Y_i=a_j+b_j X_i`, `a_j∈R`, `b_j>0`? Jest to model wspólnej kalibracji AFINICZNEJ, silniejszy od czysto multiplikatywnego modelu ROT013 i różny od źródłowej 2×2 grupy ROT007. W takim modelu dla DWÓCH izolowanych punktów źródłowe hipotezy są nierozróżnialne w sensie minimax (dokładny alias pełnego prawa można wymusić adaptacyjnym wyborem kalibracji). TRZY lokalne punkty o geometrii narożnika przywracają informację o anizotropii: pojedynczy iloraz dwóch różnic jest niezmienniczy na KAŻDĄ wspólną kalibrację afiniczną, a jego prawo ma dokładny, różny pod A/B rozkład Cauchy’ego.

**KRYTYCZNA GRANICA:** wynik dotyczy idealnych, jednocześnie odczytywanych trzech **wycentrowanych skalarów gaussowskiego szumu stanowiskowego** lub skalarów mających wspólną, usuwalną średnią. Nie jest to operator pierwotnych pięciu kwadratowych średnich energii tensora TT, nieznanej heterogenicznej deterministycznej energii M13 ani autentycznej aparatury NASH. Nie ustalono rzeczywistej procedury odejmowania różnych średnich stanowiskowych przy nieznanym b; bez wspólnej średniej dokładna gęstość Cauchy’ego NIE OBOWIĄZUJE.

### Pierwszeństwo i źródła bezpośrednio sprawdzone

- M13 FIRST: niezmieniony publiczny pomocniczy kod Fouriera `research/m13/2026-10-24/verify_m13_rot33_interval.py` o Git blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679`, bezpośrednio pobrany/odczytany w ROT014 poprzez zintegrowany GitHub; **nie wykonano historycznego pełnego producenta DTC0a ani oryginalnego M13 `tensor_polys` w ROT014**.
- Geeky-S12 ROT038 FIRST: dokładne racjonalne A/B dla anizotropowego stacjonarnego szumu Gaussa oraz sześciu/dziewięciu obserwatorów pełny alias: Git blob `28576dbb0649c1f0fbd4d926896813eac946e6d8`, również bezpośrednio odczytany w ROT014. Dodatkowa oryginalna kalibracja z ROT038 `beta_cal_raw=1/2500` to INNY parametr; nie jest utożsamiana z niniejszym `a_j,b_j` i nie wpływa na sam iloraz trzech pomiarów.
- Geeky-S13 ROT012 FIRST: konstrukcyjny no-go odtworzenia 4FFT z sześciu starych masek, Git blob `16ea5df956eb51ff9b010f2e97e5845f4d614a7b`.
- Geeky-S13 ROT013 FIRST: pełny skan 68,921 możliwych pozycji jednego dodatkowego surowego odczytu i źródłowy dwupunktowy kontrprzykład przy znanej skali: Git blob `41e98d801152e0a47c491107767406537e4cf335`.
- M16 ROT004 dotyczy INNEGO kwadratowego obserwatora B/Bpi (swapped covariance), nie jest dowodem liniowego eksperymentu ROT014.

Logika klas ilorazowych grupy afinicznej, prawo ilorazu skorelowanych normalnych, KL Cauchy’ego i test hipotez/Bhattacharyya są matematyką klasyczną: bez roszczeń do nowego ogólnego twierdzenia. Własny wynik jest **ściśle źródłową aplikacją do konkretnej racjonalnej geometrii/szumu ROT038**.

## 1. Dokładne źródło i narożna geometria trzech sond

Torus `N=41`, okresowy indeks `Z_41³`. Używam rzeczywistych lokalizacji centralnego starego regionu M13:

`P0=(20,20,20)`, `Px=(21,20,20)`, `Py=(20,21,20)`.

Obie syntetyczne, dodatnio określone, stacjonarne kowariancje szumu mają współczynniki w porządku `(beta0, beta_x, beta_y, beta_z, beta_xy, beta_xz, beta_yz, beta_body)`:

`A=(1,1/25,1/25,1/25,1/30,1/30,1/30,2/25)`;
`B=(1,1/20,3/100,1/25,1/30,13/300,7/300,2/25)`.

`A_x` oznacza ŚREDNIĄ z dwóch punktów ±x, `A_y` analogicznie, `A_xy` średnią z czterech ±x±y. Zatem korelacje jednostkowych skalarów na triodzie są dokładnie

`r_Ax=1/50`, `r_Ay=1/50`, `r_Axy=1/120`;
`r_Bx=1/40`, `r_By=3/200`, `r_Bxy=1/120`.

Obie macierze pełnej siatki pozostają SPD z prostą analityczną dolną granicą widma `>=7/10`. Nie mylić normalizowanego operatora axial ± (współczynnik beta/2 na SĄSIEDZIE) z współczynnikiem beta na każdej krawędzi.

Dla `U=Xx-X0` i `V=Xy-X0`, których wspólna średnia wynosi zero:

`u=Var(U)=2(1-rx)`, `v=Var(V)=2(1-ry)`, `w=Cov(U,V)=1-rx-ry+rxy`.

Pod **A**: `u_A=v_A=49/25`, `w_A=581/600`.

Pod **B**: `u_B=39/20`, `v_B=197/100`, `w_B=581/600`.

To w pełni racjonalne SPD 2×2 kowariancje; ich zmiana NIE jest tylko wspólnym przemnożeniem przez dodatnią liczbę, więc pozostaje widoczna po ilorazowaniu skali.

## 2. Dokładny dwu-punktowy no-go przy dowolnej kalibracji afinicznej

Weź DWA surowe stanowiskowe odczyty o identycznej znanej lub wspólnej średniej pod A i B, jednostkowych wariancjach i korelacjach `r_A=1/50`, `r_B=1/40`. Pełne gaussowskie prawa 2D są różne przy znanej kalibracji (ROT013); nie wolno przenosić tej rozróżnialności przy nowej grupie nuisance.

Dla każdego stanu `(X1,X2)` o `X1≠X2` dodatnia grupa afiniczna `Y_i=a+b X_i`, `b>0` może przeprowadzić parę do kanonicznej `(-1/2,+1/2)` lub `(+1/2,-1/2)`, według znaku różnicy. Konstrukcja jawna: `b=1/|X2-X1|`, `a=-(X1+X2)/(2|X2-X1|)`. Jest DOZWOLONA przy naszej deklaracji, że nuisance może adaptować się do całej realizacji latentnej. Ponieważ pod OBU modelami `(X1,X2)` są wymienne, mają równe średnie i ciągłą gęstość, `Pr(X1<X2)=Pr(X1>X2)=1/2`. Zatem po tej adaptacyjnej kalibracji **całe rozkłady obserwowanej pary są identyczne A i B**: po 1/2 na obu punktach kanonicznych. W szczególności przy dowolnej liczbie niezależnych próbek minimax przy równych wagach osiąga najwyżej sukces 1/2, bo przeciwnik może zawsze wybrać tę ścieżkę nuisance.

To no-go ma ścisłą klasę: dwa odczyty, per-snapshot dowolny adaptacyjny COMMON affine transform, wspólna średnia i jednakowe marginalne wariancje; nie stosuje się automatycznie do dwóch punktów przy znanym a, znanym b, nieadaptacyjnym nuisance ani do eksperymentu zawierającego stare sześć niezależnie dostępnych agregatów.

## 3. Trzy-punktowy iloraz, grupa nuisance i dokładne prawo Cauchy’ego

Dla dowolnego wspólnego `a_j∈R,b_j>0` (również modelowo, czasowo i **latentnie adaptacyjnych**) i dowolnej realizacji z `V_j≠0` zachodzi dokładnie:

`T_j=(Yx_j-Y0_j)/(Yy_j-Y0_j)=(Xx_j-X0_j)/(Xy_j-X0_j)=U_j/V_j`.

`T` jest niezmiennikiem; przy restrykcji `b>0` *pełnym matematycznym maksymalnym niezmiennikiem* jest para `(T, sign(V))`. Drugi składnik jest jednocześnie uczciwą monetą i niezależny od `T` pod KAŻDYM z dwóch wycentrowanych normalnych modeli (symetria `(U,V) -> (-U,-V)`). W tym konkretnym eksperymencie **T jest statystycznie wystarczający wśród wszystkich dodatnio-afinicznie niezmienniczych testów**. Nie utożsamiamy go z maksymalnym niezmiennikiem geometrycznym przy b>0.

Dla każdej dodatniej 2×2 macierzy kowariancji `(u,w;w,v)` iloraz dwóch wycentrowanych skorelowanych normalnych ma dokładnie gęstość

`f_T(t)=sqrt(uv-w²)/(pi*(v*t²-2*w*t+u))`

czyli standardowy rozkład Cauchy’ego z położeniem `mu=w/v` i skalą `s=sqrt(uv-w²)/v`. Pod A oraz B:

`mu_A=581/1176≈0.494047619047619`, `s_A≈0.8694348452376283`;
`mu_B=581/1182≈0.491539763113367`, `s_B≈0.8650065762839584`.

Te dwie rodziny są ściśle odmienne. Ich źródłowo dokładna dywergencja Cauchy’ego jest symetryczna i ma zamknięty wzór, bez integracji numerycznej:

`KL(A||B)=KL(B||A)=log( ((s_A+s_B)^2+(mu_A-mu_B)^2)/(4 s_A s_B) )`

`=0.00000860920659056062856794333458490835...`.

Zapisano rzeczywiście wykonane, skierowane przedziały IV80 zarówno dla źródłowych parametrów, jak i pełnego KL. Pierwszy model nie pozostaje w pełni nierozróżnialny przy tej strukturze niezależnie od dowolnej adaptacyjnej kalibracji, ponieważ dla KAŻDEJ jej realizacji `T` ma wyżej określone prawo.

### Konstrukcja źródłowa niezależności od sześciu dawnych masek

W każdym z trzech powyższych punktów i we WSZYSTKICH ich 26 sąsiedztwach jednokrokowych źródłowej kowariancji znajdujemy się w centralnym regionie M13 `R5=I6`, |R5|=24389; żaden sąsiad nie należy do R0..R4. Każdy z trzech punktów ma zatem ten sam dokładny wektor kowariancji ze STARYMI średnimi regionowymi:

`Cov_X(M_r,X_i)=0` przy r=0,...,4;
`Cov_X(M_5,X_i)= (beta0+sum_{seven} beta)/24389 = 13/(10*24389)` pod obiema A/B.

W konsekwencji `Cov_X(M_r,U)=Cov_X(M_r,V)=0` dla wszystkich r i obu X. W JEDNYM wspólnym wycentrowanym gaussowskim modelu `U,V` są niezależne od wszystkich sześciu starych średnich `M`. Jest to źródłowo dokładna własność lokalności; dodatkowy wcześniejszy niezależny parametr kalibracji pełnej średniej z ROT038 nie zmienia zer tych kowariancji. Nie twierdzimy, że przed-kalibracyjna niezależność utrzymuje się dla wszystkich obserwowanych danych po zastosowaniu nieliniowo adaptacyjnych a_j,b_j.

## 4. Ścisłe zasoby dla jednej niezmienniczej obserwacji binarnej

Dopuszczalny, bardzo prosty test zachowuje tylko `J_j=1{T_j≤1}`. Otrzymujemy dokładnie:

`p_X=Pr_X(J=1)=1/2+(1/pi)atan((1-mu_X)/s_X)`.

Z wykonanych IV80:

`p_A≈0.66775841986290844804`;
`p_B≈0.66915263143178603792`;
`p_B-p_A≈0.00139421156887758988003 >0`.

Ponieważ każdy T_j skraca swoją własną, nawet adaptacyjną kalibrację, `J_1,..,J_n` są IID Bernoulli(p_X) jeśli latentne trójki gaussowskie są IID między migawkami. Standardowy test NP dla `n` obserwacji binarnych ma iloraz wiarygodności `L_n`. Z nierówności Markowa (dla każdego X osobno!) `P_A(L_n≥1)≤E_A sqrt(L_n)=rho_bin^n`, `P_B(L_n<1)≤E_B(1/sqrt(L_n))=rho_bin^n`, gdzie

`rho_bin=sqrt(p_A p_B)+sqrt((1-p_A)(1-p_B))≈0.999998903639386`.

Dla docelowego błędu <5% na KAŻDĄ hipotezę: pierwsza n spełniająca **TYLKO tę rygorystyczną nierówność wystarczającą** wynosi **2,732,432**, a przy `n-1` prawa strona jest jeszcze powyżej 5%. Dla <1%: **4,200,414**. Mamy również osobno proste wystarczające progi z Hoeffdinga `n≥3,082,306` (95%) i `n≥4,738,254` (99%). Także te progi są otrzymane z 80-cyfrowej skierowanej arytmetyki, z kontrolą bezpośredniego poprzednika.

Nie twierdzimy, że n=2,732,432 lub 4,200,414 jest minimalnym n optymalnego testu na **pełnej wartości T**: NP na pełnym Cauchym może być lepszy od NP na binarnym `J`. Co więcej, dla każdej z dwóch liczb stwierdzamy FIRST *dla danej nierówności* `rho_bin^n<alpha`, NIE first dla rzeczywistego błędu testu binarnego.

Z porównania informacji per snapshot wynika `KL_triadu≈8.6092e-6`; jest to około 174 razy KL najlepszego JEDNEGO nowego punktu+6 oryginalnych agregatów w ROT013, lecz eksperymenty należą do RÓŻNYCH klas nuisance i mają różne koszty obserwacji. Nierówności zasobowe nie powinny być bezpośrednio interpretowane jako koszt aparatury.

## 5. Reprodukcja, kontrole negatywne, decyzje naukowe

Dwa autorskie algorytmy napisane oddzielnie:

1. `rot014_primary_iv.py`: tylko dokładne rational `Fraction` i skierowana `mpmath.iv.dps=80`; wylicza pełne rational 3x3/2x2 source, Cauchy KL, prawdopodobieństwa testu `T≤1`, afiniczną invariance tożsamość, obie pierwsze granice Bhattacharyyi/Hoeffdinga wraz z n−1. Bez symulacji.
2. `rot014_independent_spatial.py`: osobny przestrzenny 41³ kernel ze wszystkimi 26 kierunkowymi przesunięciami, niezależny FFT widma, dokładna geometria sąsiadów wszystkich trzech punktów względem R0..R5, osobno SciPy QUAD oryginalnej gęstości Cauchy’ego i niezależny liczbowy wzór KL, numeryczny test adaptacyjnych kalibracji zależnych od latentnych realizacji. Nie importuje programu 1.

Kontrole: wszystkie osiem współczynników każdego źródłowego modelu, A/B SPD, dokładna geometryczna niezależność triadu od 6 masek, zamiana osi x/y (źródłowo kierunkowa), odrzucenie fałszywej tezy o dwupunktowej odporności na nieznany offset, niezależna zmiana parametrów Cauchy’ego, dokładne testy korupcji danych przy przeliczonym manifest SHA256. Dokładne wyniki, kody, replay i manifest znajdują się w pakiecie (status całej reprodukcji należy ustalić wyłącznie z wykonanego receipt). Wyniki numeryczne SciPy nie są „różną komórką” ani zewnętrznym I1.

### Warunki falsyfikujące przeniesienie na aparaturę

- **Różne deterministyczne średnie stanowiskowe** lub surowa energia będąca nieliniową funkcją normalnych składowych: iloraz różnic nie musi mieć rozkładu Cauchy’ego.
- **Kalibracje osobne dla każdego z trzech czujników**, nawet multiplikatywne, nie skracają się przez dwie różnice.
- **Szum dodany po kalibracji**, saturacja, kwantyzacja, dryft względnego położenia bądź niejednoczesność odczytów: mogą złamać ścisłą symetrię.
- **Brak IID latentnych trójek** w czasie, nawet jeżeli rozkład pojedynczej trójki jest poprawny: nie można użyć Bernoulliego/Bhattacharyyi w zadeklarowanej postaci.
- Sześć oryginalnych średnich M13, historyczne dane DTC0a, właściwa aparatura, surowe lokalne pomiary i procedura kalibracji **nie zostały źródłowo empirycznie ustalone**.

### I1 bounded scope i status

Wniosek do niezależnych recenzentów AUD3/REC13/M16: (a) niezależnie sprawdzić kanonizację i dwupunktowy dokładny alias przy adversarial affine, (b) zrekonstruować geometrycznie dokładne `u,v,w` trzech punktów ze źródłowego ROT038 z poprawnymi czynnikami normalizacji 2/4, (c) wyprowadzić pełne maksymalne niezmienniki grupy `b>0` i statystyczną marginalność dodatkowego bitu orientacji, (d) sprawdzić całkę Cauchy-KL i IV80 n> thresholds, (e) sfalsyfikować lokalne `Cov(M,U)=Cov(M,V)=0` w źródłowych maskach M13. Żaden I1 samego ROT014 nie został jeszcze uzyskany; nie domniemujemy niezależnej akceptacji ani wpisu do BW.

**FINAL:** `SOURCE_N41_ROT038_SYNTHETIC_ANISOTROPIC_GAUSSIAN / 2_SENSOR_ADAPTIVE_AFFINE_FULL_LAW_ALIAS / 3_SENSOR_CAUCHY_RATIO_AFFINE_GAIN_INVARIANT / IV80_KL_AND_BHATTACHARYYA_FINITE_N / EXACT_LOCAL_MASK_ORTHOGONALITY / SECOND_SAME_CELL_SPATIAL_FFT_AND_SCIPY / EXTERNAL_I1_PENDING / BW_PENDING / NO_GENERAL_NOVELTY / NO_PHYSICAL_UPGRADE / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE`.
