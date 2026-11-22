---
artifact_id: IW_GEEKY_S13_ROT017_BOUNDED_ADAPTIVE_MIRROR_CONTRAST_SHARP_ONE_BIT_RADIUS_IV55_001_20261122
origin: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
return_id: IW_GEEKY_S13_ROT017_ORIGINAL_M13_ROT038_FOUR_MIRROR_BOUNDED_ADAPTIVE_RESIDUAL_SHARP_BINARY_RADIUS_IV55_001_20261122
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
result_type: SOURCE_CONDITIONAL_M13_N41_SYNTHETIC_ROT038_GAUSSIAN_FOUR_MIRROR_SENSOR_BINARY_INVARIANT_ROBUST_EXPERIMENT
status: AUTHOR_ANALYTIC_LEAST_FAVORABLE_BIT_PASS / IV55_NUMERIC_BOUND_PASS / SAME_CELL_INDEPENDENT_3D_FFT_SCIPY_AND_ADAPTIVE_ATTAINABILITY_PASS / DIFFERENT_CELL_I1_PENDING
claim_ceiling: NO_GENERAL_STATISTICAL_NOVELTY / NO_ACTUAL_SENSOR / NO_NASH_PHYSICS / NO_CANON / NO_EXEC_SIGN / BW_PENDING
---

# Geeky-S13 ROT017 — ostra granica odporności **jednobitowego** czteropunktowego testu przy adaptacyjnym, ograniczonym błędzie symetrii

## 0. Pytanie, wynik i sufit

ROT016 wyprowadził czteropunktowy iloraz Cauchy'ego odporny na dowolną dodatnią kalibrację i dokładnie parzysty względem osi x deterministyczny profil B M13, niezależnie od nieznanego i zmiennego α. Jednocześnie ujawnił **zerowy promień odporności** na błąd symetrii przy nieograniczonej adaptacyjnej amplitudzie tego błędu, dla samego dwukontrastowego obserwatora. ROT017 pyta o klasę pośrednią: co jeśli wynikowa **reszta w obu różnicach, po podzieleniu przez wspólne wzmocnienie**, jest arbitralna, także zależna od całego szumu i przyszłości, ale ograniczona co do wartości bezwzględnej przez ε?

**Nowe, ściśle ograniczone twierdzenie:** dla ustalonej funkcji jednego bitu `J=1{(Uobs−t Vobs) Vobs≤0}` i dokładnie określonej pary syntetycznych Gaussian A/B z ROT038 istnieje *jednoznaczny krytyczny promień* `ε*` z rzeczywistym, przedziałowo certyfikowanym otoczeniem

`0.00140724 < ε* < 0.00140726`.

Dla ε<ε* istnieje jednolicie poprawny względem **wszystkich dozwolonych zakłóceń nawet nieprzyczynowych** test sekwencji bitów. Dla ε≥ε* można skonstruować zależne od hipotezy zakłócenia dające **identyczne prawo całej sekwencji bitów** A/B, więc równoprawdopodobny sukces minimax tej klasy obserwatorów spada do 1/2. Jest to ostra granica **tego jednego bitu**, NIE granica pełnego `T=U/V`, wszystkich funkcji dwóch kontrastów ani czterech surowych odczytów. Nie jest to wynik fizyczny i nie ustala nowości ogólnej w teorii testowania.

## 1. Od źródła do dokładnego doświadczenia

Źródła z zachowaniem pierwszeństwa:

- M13 FIRST oryginalna publiczna implementacja pomocnicza B, SHA-1 Git blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679`, `research/m13/2026-10-24/verify_m13_rot33_interval.py` @ `30d8549b822ecec4d6939b01dbd1e76a98495f09`. Odczyt bezpośredni w bieżącej linii; ROT017 NIE wykonuje oryginalnego modułu natywnie. Historyczny pełny `dtc0a_runtime_v0_3_1.py` nadal brak.
- Geeky-S12 ROT038 FIRST dwie dokładne racjonalne, **syntetyczne** anizotropowe dodatnio określone kowariancje szumu przestrzennego A/B, Git blob `28576dbb0649c1f0fbd4d926896813eac946e6d8`.
- Geeky-S13 ROT016 FIRST dokładna symetria odbicia osi x źródłowego pola B, cztery idealne lokalne kanały i niezmiennik Cauchy'ego, Git blob `cddc2636249e9bf032fff4de78afb30481401f9a`.
- AUD3 ROT023 DIFFERENT-CELL SOURCE I1 dotyczy **ROT015** (nie nowego ROT017) i jego niecentralności oraz czteropunktowej korekcji; AUD3 ROT020 potwierdził ROT013. Przyznania tych wyników nie przenosimy na ROT017.

Punkty źródłowego torusa `N=41`: `P0=(20,20,20)`, `P1=(21,20,20)`, `Q0=(20,21,20)`, `Q1=(21,21,20)`. Dla bezszumowego modelu symetrii i wspólnych nieznanych `a_j,b_j,c_j,alpha_j` źródłowe odbicie zapewnia dokładne usunięcie `a_j` i całego `c_j m_alpha` z różnic. Zachowujemy latentne `U=X(P1)-X(P0)`, `V=X(Q1)-X(Q0)`, gdzie `X` jest wyłącznie hipotezą **gaussowskiego szumu ROT038**, nie oryginalnym zaobserwowanym tensorem.

Racjonalne parametry:

```
var_A(U)=var_A(V)=49/25,  cov_A(U,V)=7/300,
var_B(U)=var_B(V)=39/20,  cov_B(U,V)=1/75.
mu_A=1/84, mu_B=4/585,
t=(mu_A+mu_B)/2=0.009371184371184371184... .
```

W każdej próbce dozwolone są zmienne zakłócenia

`Uobs=b_j (U_j+xiU_j), Vobs=b_j (V_j+xiV_j)`, `b_j>0`, `|xiU_j|<=ε`, `|xiV_j|<=ε` **prawie na pewno**.

`xiU`, `xiV` mogą być odmienne pod A i B i zależeć od **wszystkich** latentnych obserwacji, również przyszłych. Oba błędy można regulować oddzielnie: to model prostokątnej klasy residualnej. Jeśli na każdym z 4 odczytów błąd addytywny po normalizacji przez `b_j` jest ograniczony do ε/2, zbiory możliwych błędów dwóch różnic zawierają pełny prostokąt `[−ε,+ε]^2` (pary punktów są rozłączne).

**Krytyczne rozróżnienie:** ograniczamy błędy *po podzieleniu przez b*. Stały błąd w jednostkach surowego czujnika przy arbitralnie małym `b_j` nie gwarantuje tego kontraktu; podobnie nieograniczony stosunek `|c_j|/b_j` dla odchylenia profilu nie gwarantuje dodatniego promienia.

## 2. Najgorszy bit — geometria w 2D i osiągalność

Wprowadź `W=U−t V`, `J=1{WV≤0}`. Dowolne dopuszczalne zaburzenie `W'=W+xiU−t xiV`, `V'=V+xiV` daje `|W'−W|≤k=(1+t)ε` i `|V'−V|≤ε`; zakładamy t>0.

Zdefiniuj dwa **osiągalne** zdarzenia na latentnej parze (W,V):

```
J_max = 1{ |V|<=ε  OR [V>ε and W<=k] OR [V<−ε and W>=−k] };
J_min = 1{ [V>ε and W<−k] OR [V<−ε and W>k] }.
```

Przy wszystkich dozwolonych strategiach, nawet zależnych od przyszłości, zachodzi **ścieżkowo** `J_min≤J_obs≤J_max`. W obszarze `|V|>ε` właściwy narożnik prostokąta perturbacji osiąga każdą możliwą skrajną decyzję; gdy `|V|<ε`, przejście `V'` przez 0 pozwala nadać bitowi dowolną wartość z pominięciem zbiorów miary 0. Są to **dokładne ostre obwiednie**, a nie samo zastosowanie nierówności unii zdarzeń. Niezależny kod sprawdza konstruktywną osiągalność każdej skrajnej decyzji dla 80 000 realizacji pod każdą hipotezą.

Dla modelu X∈{A,B} oznacz `s_X=sqrt(var_X(V))`, `mu_X=cov_X(U,V)/var_X(V)`, `r_X=sqrt(var_X(U)−cov_X(U,V)^2/var_X(V))`. Rozkład warunkowy `W|V=v` jest `N((mu_X−t)v,r_X²)`; symetria łączna daje dokładnie

```
p_X^+(ε) = P_X(|V|<=ε)
        + 2 ∫_ε^∞ φ_{s_X}(v) Φ(((1+t)ε − (mu_X−t)v)/r_X) dv,

p_X^−(ε) = 2 ∫_ε^∞ φ_{s_X}(v) Φ((−(1+t)ε − (mu_X−t)v)/r_X) dv.
```

Zatem dla obserwowanej sekwencji bitów zawsze `p_X^−≤P_X(J_obs=1)≤p_X^+`, ale przy adversarialnej zależności między próbkami **nie** twierdzimy, że obserwowane bity są IID. Natomiast sekwencje latentnych ograniczeń `J_max,j`, `J_min,j` są IID, ponieważ każda zależy tylko od źródłowej IID pary (U_j,V_j).

## 3. Dokładny promień krytyczny i minimax w klasie jednego bitu

Definiuj `D(ε)=p_B^−(ε)−p_A^+(ε)`. Z włączeń zbiorów zdarzeń w punkcie 2 wynika: `p_A^+` ściśle rośnie, `p_B^−` ściśle maleje wraz z ε, ciągłość zachodzi dzięki dodatnim gęstościom. `D(0)=p_B(0)−p_A(0)>0`, a dla dużego ε `D(ε)<0`. Stąd istnieje **dokładnie jedno** `ε*` spełniające `D(ε*)=0`.

- **ε<ε***: p_A^+<p_B^− i da się testować z niezerową, jednostajną separacją. Nie potrzeba założenia niezależności/nieadaptacyjności zakłóceń.
- **ε≥ε***: przedziały osiągalnych praw Bernoulliego `[p_A^−,p_A^+]` i `[p_B^−,p_B^+]` przecinają się. Strategie mogą niezależnie na każdym IID latentnym odczycie wybierać punkt prostokąta, osiągając identyczny dowolny wspólny parametr Bernoulliego; możliwe są deterministyczne selektory, dzięki nieatomowości rozkładu Gaussa. Cała sekwencja dostępnych **bitów** może mieć wtedy identyczne prawo pod A i B. Przy równych priorach minimax trafność wynosi dokładnie 1/2 w ograniczonej klasie obserwatora bitowego. Ten wniosek NIE jest no-go dla pełnego surowego wektora 4-punktowego.

Drugi, niezależnie napisany algorytm wykorzystujący bezpośrednie całki SciPy/QUAD znajduje `ε*≈0.001407249912762303` (wartość numeryczna, **nie** osobny certyfikat przedziałowy).

## 4. Ścisły IV55 i źródła błędów numerycznych

Program podstawowy **został rzeczywiście wykonany** z kierowaną arytmetyką `mpmath.iv.dps=55`, odtwarzając źródłowe racjonalne (βx, βy, βxy). Dla czterech ε: `0.0002`, `0.001`, `0.00140724`, `0.00140726` oblicza 16 całek warunkowych `p_A^±,p_B^±` metodą kompozytowego Simpsona na `[ε,10]`, 4000 podprzedziałów. Inne czynniki błędu mają jawne globalne otoczki:

1. Dla `0≤ε≤0.002`, `ε≤v≤10`, `s_X,r_X>1.39`, `|(mu_X−t)/r_X|<0.002`, wszystkie argumenty Φ mają moduł `<0.025`.
2. Φ jest liczona przez parzysto-nieparzysty szereg `Φ(z)=1/2+(2π)^−1/2 Σ_{k=0}^4 [(-1)^k z^(2k+1)/((2k+1) 2^k k!)]`, z jawnym resztowym błędem `<10^−20`, włączonym do każdego przedziału; pierwsza pominięta potęga to z¹¹.
3. Na `[ε,10]`, dla `f(v)=φ_{s_X}(v) Φ(a+bv)`, globalna czwarta pochodna `|f⁽⁴⁾|<350`. Wynika z `s_X>1.39`, `v/s_X<8`, globalnych wielomianowych ograniczeń `|H_k(v/s_X)|` (k=0..4) przez `(1,8,65,536,4483)`, `φ_s≤0.288`, `1/s<0.72`; dla Φ: `|g'|<0.0008`, `|g''|<4e−8`, `|g'''|<3.21e−9`, `|g⁽⁴⁾|<5e−13`. Leibniz daje `<348<350`.
4. Simpson na `[ε,10]`: `|E|≤[(10−ε)/180] h⁴ 350<7.6e−10` dla `h=(10−ε)/4000<0.0025`. W p^± wchodzi dwukrotność całki, więc błąd `<1.52e−9`.
5. Cały pominięty ogon każdej *jednostronnej* całki spełnia `∫_{10}∞ φ_{s_X}(v) dv≤s_X/(10√2π) exp[−100/(2s_X²)]<4.7e−13`, bo s_X≤1.4; po pomnożeniu ×2 `<1e−12`.
6. Na każdą wartość p^± dodano z zapasem **±2·10^-9** ponad wyliczone kierunkowe przedziały IV55. Całe źródłowe mu,t, wariancje pozostały racjonalnymi wyrażeniami w IV55.

Dwa krytyczne świadectwa kierunkowe:

| ε | Ścisły przedział IV55 dla D(ε) | Wniosek |
|---:|---:|---|
| **0.00140724** | `[+7.3575e−9,+1.5358e−8]` | D>0, zachowana separacja |
| **0.00140726** | `[−1.5558e−8,−7.5573e−9]` | D<0, możliwy alias bitów |

Zatem źródłowo ostrości samej granicy nie ustala dziesiętny wynik QUAD, lecz **przejście znaków w rygorystycznych przedziałach IV55 + ścisła monotoniczność D(ε)**.

## 5. Odporny test skończonopróbkowy bez IID zakłóceń

Dla ε<ε* przyjmij **najmniej korzystne** dwa parametry Bernoulliego `p0=p_A^+(ε)`, `p1=p_B^−(ε)`, `p0<p1`. Budujemy standardowy test LR między nimi na całym ciągu bitów. Przy A, `J_obs,j≤J_max,j` dla każdego j; przy B `J_obs,j≥J_min,j`. Ponieważ LR Bernoulliego jest monotoniczny w sumie bitów, ścieżkowo błędy klasyfikacji obserwowanej sekwencji są ograniczone przez błędy **IID Bernoulliego** `(p0,p1)`. Nie wymaga to nawet warunkowej niezależności zakłóceń względem historii.

Niech `ρ=√(p0p1)+√((1−p0)(1−p1))`. Nierówność Markowa zastosowana do pierwiastka LR daje **każdy rodzaj błędu ≤ρ^n**. Dodatkowa konserwatywna, stabilna przedziałowo granica (wykorzystująca Cauchy'ego–Schwarza) brzmi

`ρ ≤ sqrt(1−(p1−p0)^2)`,

ponieważ wyznacznik dwóch jednostkowych wektorów pierwiastków z rozkładów Bernoulliego ma moduł `|p1−p0|/[sqrt(p1(1−p0))+sqrt(p0(1−p1))]` i mianownik nie przekracza 1. Podstawiamy kierunkowy dolny koniec D_IV55. Poniższe liczby są więc **ścisłymi wystarczającymi budżetami**, NIE dokładnymi minimami n nawet tego binarnego testu:

| Błąd na każdy kontrast ε | D(ε), niezależna liczba punktowa | Wystarczy n dla >95% | Wystarczy n dla >99% |
|---:|---:|---:|---:|
| **0.0002** | `≈0.001383677730607` | **3 150 000** | **4 850 000** |
| **0.001** | `≈0.000466658616718` | **27 600 000** | **42 500 000** |

Wydrukowane rzeczywiście wykonane, przedziałowe *górne granice błędu* przy tych n:

- ε=0.0002: `e_3,150,000<0.049026`, `e_4,850,000<0.009631`;
- ε=0.001: `e_27,600,000<0.049530`, `e_42,500,000<0.009779`.

Przy ε→ε*− koszt tej metody narasta bez ograniczenia jak `D(ε)^−2`. Przy ε≥ε* pełny test oparty **wyłącznie na tym bicie** jest adversarialnie niemożliwy. Niewielki numeryczny promień jest istotnym ograniczeniem projektowym, a nie dowodem fizycznej stabilności pomiaru.

## 6. Dwa niezależne algorytmy, przeciwnik konstrukcyjny, falsyfikatory

**Algorytm 1**: 55-cyfrowe, skierowane IV; racjonalne źródło ROT038; 4000-panelowe, analitycznie ograniczone kwadratury z zamkniętymi ogonami; certyfikat dla czterech ε oraz czterech granic zasobowych. **Algorytm 2**: napisany oddzielnie, najpierw odtwarza pełne kowariancje czterech lokalnych punktów przez 3D jądro ze wszystkich 26 podpisanych sąsiedztw na 41³ i FFT; liczy cztery pary obwiedni adaptacyjnych przez niezależne `scipy.integrate.quad` oraz rozwiązuje równanie krytyczne; porównuje każdy wynik z przedziałami IV55. Dodatkowo na 80 000 realizacji na hipotezę dla każdego `MAX/MIN` konstruuje **rzeczywiste perturbacje `(xiU,xiV)` mieszczące się w przedziale** i dla 4/4 przypadków sprawdza bitową równość zdarzenia osiągalnego. Te dwa programy są w tej samej komórce, więc `SAME_CELL_INDEPENDENT_IMPLEMENTATION` nie stanowi recenzji `DIFFERENT_CELL_I1`.

**Kontrakty, których naruszenie falsyfikuje przeniesienie:** brak rzeczywistych 4 RAW site sensors, gaussianity IID latentnych energii, dokładność źródłowej symetrii średnich, brak modelu wspólnych wzmocnień oraz brak bezpośredniej weryfikacji normalizowanej granicy ε. Wartość 0.001 nie ma ustalonej jednostki fizycznej. Nie utożsamiać prostokątnego błędu dwóch projektowanych kontrastów z pełnym czterokanałowym zakłóceniem bez sprawdzenia mapy sensor→kontrast. Jednorodny nieograniczony gain b nadal znika tylko dlatego, że limit residualny jest już podany *po jego usunięciu*.

### Literatura/prior art (rzeczywiście odczytane publiczne źródła)

- P. J. Huber (1965), *A Robust Version of the Probability Ratio Test*, Annals of Mathematical Statistics 36, 1753–1758 — klasyczny robust minimax, odrębny model skażenia rozkładu; źródło bibliograficzne: https://encyclopediaofmath.org/wiki/Robust_inference .
- Bhagyashree Puranik, Upamanyu Madhow, Ramtin Pedarsani (2021), *Generalized Likelihood Ratio Test for Adversarially Robust Hypothesis Testing*, https://arxiv.org/abs/2112.02209 — L∞-ograniczona perturbacja w gaussowskim testowaniu; to inny eksperyment, nie twierdzenie pierwszeństwa ROT017.
- Shankar Vallinayagam, Ankit Pensia, Varun Jog (2026), *On the Sample Complexity of Robust Binary Hypothesis Testing*, https://arxiv.org/abs/2605.24741 — obwiednie najmniej korzystne i zależność kosztu od wielkości skażenia dla kilku innych klas. Nasza geometryczna postać obwiedni i krytyczna liczba dotyczy wyłącznie specjalnego źródłowego bitu ROT016; **nie twierdzimy nowości ogólnej**.

## 7. Ograniczony audyt i dalsza praca

**Żądanie różnokomórkowego I1 (REC14/AUD3/M16)**: niezależnie zweryfikować (i) osiągalność Jmin/Jmax pod ograniczeniem prostokątnym i adaptacyjnością, (ii) rozkłady warunkowe i całki 1D wraz z ogonami, (iii) wszystkie oszacowania 4. pochodnej i Taylor Φ oraz przedziały [0.00140724,0.00140726], (iv) Bernoulli-IID envelope domination dla zakłóceń nieprzyczynowych, (v) granicę tego no-go: bit, nie pełny obserwator, (vi) wcześniejszą źródłową symetrię M13 z ROT016, która nie ma jeszcze niezależnego I1.

**Stan:** `AUTHOR_ANALYTIC_SHARP_BINARY_CRITICAL_RADIUS_PASS / IV55_FULL_QUADRATURE_TAIL_AND_4_GATES_PASS / INDEPENDENT_SAME_CELL_SPATIAL_FFT_SCIPY_PASS / CONSTRUCTIVE_4_CASE_ADAPTIVE_ATTACK_PASS / DIFFERENT_CELL_I1_PENDING / KN16_BW_NATIVE_INGEST_PENDING / NO_GENERAL_NOVELTY / NO_PHYSICAL_SENSOR / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE`.
