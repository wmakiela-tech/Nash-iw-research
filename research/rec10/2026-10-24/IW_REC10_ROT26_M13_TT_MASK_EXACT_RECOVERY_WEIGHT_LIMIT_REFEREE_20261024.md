# IW/NASH — REC10 ROT26
## Pięć masek DTC0a: ostra identyfikowalność M13 i wymierna granica wag odzysku globalnego RMS

**Date:** 2026-10-24 16:26+02:00 (start of audit)  
**Cell:** `IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10`  
**Problem:** `P3_DTC0A_TT_MASK_COMMUTATION_AND_LOCAL_RMS_TYPING_001`  
**Source:** M13 ROT30, `research/m13/2026-10-24/IW_M13_ROT30_sharp_TT_bandwidth_mask_identifiability_001.md`, blob `315e3a0d80d435e31827774a9135f1dd9774db55`; prior M13 ROT29 plus REC10 ROT24.  
**Verdict:** `PASS_WITH_ASYMPTOTIC_STABILITY_STRENGTHENING / NONBLIND`  
**Guards:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_TASK_CASCADE / BW_PENDING`.

## 1. Chronologia i zakres

M13 ROT29 skonstruował nierozróżnialne **gęstości energii** o paśmie stopnia 5 przy pięciu maskach k=2..6. REC10 ROT24 niezależnie wykazał, że przy jednowymiarowej gęstości energii o paśmie ≤4 pomiary pozwalają dokładnie odzyskać pełną średnią, i podał wagi N41 oraz dwa różne modele błędów. Następnie M13 ROT30 zaostrzył zakres: dla **pól tensorowych TT** o paśmie tensora B≤2 zachodzi pozytywny wynik, podczas gdy przy B=3 istnieje jawna nierozróżnialna para pól rzeczywiście TT; źródłowy `rms_norm` i `apply_P_TT` to potwierdzają. Niniejszy audyt nie przypisuje REC10 pierwszeństwa tych źródłowych twierdzeń ani konstrukcji nieidentyfikowalności.

**Nowa, wąska delta ROT26:** dokładna wymierna granica i pierwszy wyraz asymptotyki jednoznacznych wag pięciomaskowego odzysku, oraz rozdzielenie uwarunkowania **funkcjonału globalnej średniej** od uwarunkowania rekonstrukcji całego wektora współczynników energii.

Zakres: nieparzyste N≥13, periodyczne x_j=2πj/N, pola T(x) niezależne od y,z, identyczne tensorowe źródło na każdej masce, `R_k²=mean_{j=k}^{N-k-1} ||T(x_j)||_F²/6`, k=2,3,4,5,6. Gęstość energii `F(x)=||T||_F²/6` ma harmoniczne |p|≤4. Dla pól tensorowych stopnia ≤2 ten warunek zachodzi automatycznie. Dane `R_k` nie muszą mieć podpisanego modelu szumu; oszacowanie błędu odnosi się do ich **kwadratów**.

## 2. Dokładna macierz obserwacji bez regresji

Niech c=(N−1)/2, θ=2π/N, z_j=θ(j−c). Podstawmy

`F(z)=a_0+sum_{p=1}^4 (a_p cos(pz)+b_p sin(pz))`.

Średnie sinusów znikają na każdej symetrycznej masce, jak i na pełnym okresie. Zatem `g_k=R_k²= Σ_{p=0}^4 A_{k,p} a_p` i `g_0=a_0`, gdzie **dokładnie**

`A_{k,0}=1`,

`A_{k,p}=(-1)^(p+1) sin(2π p k/N)/[(N−2k)sin(π p/N)]` dla p=1,2,3,4.

Dowód: suma kosinusów na pełnej siatce znika, usunięto po k kolejnych węzłów z każdej strony; `2Σ_{j=0}^{k−1}cos((j+1/2)t)=sin(k t)/sin(t/2)`. Wykorzystano dokładną parzystość przesunięcia c.

Wektor dokładnych wag w(N) spełnia `A(N)^T w=e_0` i jest jednoznaczny dla wszystkich zadanych nieparzystych N≥13 (M13/REC10 range result). `a_0=Σ_k w_k g_k`.

## 3. Nowe twierdzenie 26.1: wymierna granica wag i pierwszy rząd

**Twierdzenie.** Przy N→∞ po nieparzystych N, pięć dokładnych wag ma rozwinięcie

`w_k(N)=w_k^(∞)(1−2k/N)+O(N^−2)`, k=2..6,

przy

`(w_2∞,w_3∞,w_4∞,w_5∞,w_6∞)=(99/14,−88/7,66/7,−24/7,1/2)`.

W konsekwencji:

`Σ_k |w_k(N)| = 33 − 1536/(7N) + O(N^−2)`.

**Dowód.** Warunki `Σw=1` oraz cztery równości `Σ_k w_k sin(p k θ)/(N−2k)=0` są dokładne. Zdefiniuj `u_k=w_k/(1−2k/N)`, t=1/N. Wtedy `Σu_k sin(2πp k t)=0`, p=1,2,3,4, i `Σ_k(1−2kt)u_k=1`. Dla t≠0 zastosuj do czterech równań odwracalną liniową eliminację współczynników dla różnych p w bazie `{p,p³,p⁵,p⁷}`. Macierz `(p^{2j+1})_{p=1..4,j=0..3}` jest odwracalna. Po podzieleniu odpowiednich wierszy przez niezerowe potęgi t, nowe cztery warunki analityczne przy t=0 przyjmują postać

`Σ_k k u_k=Σ_k k³u_k=Σ_k k⁵u_k=Σ_k k⁷u_k=0`.

Pozostałe wyrazy są parzystymi analitycznymi poprawkami rzędu O(t²), ponieważ sin jest funkcją nieparzystą. Wraz z `Σu_k=1` graniczna macierz jest odwracalna: jej cztery ostatnie wiersze to `(k,k³,k⁵,k⁷)`, a pierwszy jest jedynką. Bezpośrednia wymierna inwersja daje podany wektor u∞. Co ważne `Σ_k k u_k∞=0`; liniowy człon warunku normalizacyjnego `−2tΣku` więc również znika. Z analitycznej odwracalności układu i twierdzenia o funkcji uwikłanej wynika `u_k(t)=u_k∞+O(t²)` (brak członu liniowego). Zatem `w_k=(1−2kt)u_k∞+O(t²)`.

Żaden składnik w∞ nie jest zerowy, więc znaki wag dla dużych N są stałe. Suma modułów jest `Σ|w∞|=33`; ponadto `Σ k|w∞|=768/7`, co daje wskazaną poprawkę `−(2/N)(768/7)`. QED.

**Sens liczb:** `L1=33` to graniczne, ostre w modelu pięciu niezależnie ograniczonych błędów **kwadratów norm** wzmocnienie odzysku globalnej średniej energii. Nie oznacza ogólnego uwarunkowania wyznaczania całego `F` z danych ani rzeczywistych błędów historycznych DTC0a.

## 4. Niezależny test i źródłowy falsyfikator

Samodzielny skrypt `IW_REC10_ROT26_FIVE_MASK_WEIGHT_LIMIT_REPRO_20261024.py` wykorzystuje:
- wysoką precyzję `mpmath` i **dokładny analityczny** wzór A(N), bez dopasowania do danych M13;
- wymierną inwersję `sympy` granicznych pięciu równań;
- 100 niezależnych dodatnich lub nieujemnych energii postaci `F=f²`, `f` rzeczywisty trygonometryczny stopnia≤2, realizowanych przez dokładnie TT tensor `sqrt(3) f diag(0,1,-1)`;
- niezmodyfikowane funkcje oryginalnego **retained helpera**, którego plik sprawdzono SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`, z `apply_P_TT` i `rms_norm` dla N41;
- kontrolę ujemną M13 z TT tensorami `T_±=sqrt(3)[a(t) ±epsilon b(t)]diag(0,1,-1)` o paśmie 3.

| N | Σ|w(N)| | N*(33−Σ|w|) |
|---:|---:|---:|
|13|117.95096306|−1104.36252|
|31|32.99643189|0.11061146|
|41|31.65905439|54.97877001|
|101|31.51383089|150.10307997|
|401|32.49826267|201.19667075|
|1601|32.86583356|214.80047701|
|3201|32.93217482|217.10838745|
|N→∞|33|1536/7 ≈ 219.42857143|

Przy małych siatkach poprawki wyższego rzędu dominują, więc wzrost/zmniejszanie `L1` nie musi być monotoniczne. Maksymalny błąd odtworzenia `R_0²` w 100 polach TT przy N41 wyniósł `5.11e−15`. Bezpośredni helper dał błąd pełnego `R_0²` `6.66e−16`, dokładnie TT błąd względny `5.43e−16`. Para stopnia 3 ma wszystkie pięć maskowanych RMS identyczne w granicach błędu maszynowego, zaś pełne różnią się o `4.237604573944509e−4`. Zatem nie tylko udowodniono asymptotykę, lecz odtworzono **oba kierunki ostrego progu** M13 w tej samej realizacji.

Wiersze N>41 to algebra i obliczenia macierzy 5x5, **nie** pełne 3D symulacje siatkowe o takim rozmiarze.

## 5. Granice i dyspozycja

- **Wcześniejsze:** M13 ROT29/30 pozytywność i kontrprzykład źródłowy, REC10 ROT24 jednowymiarowy stopień 4 i N41 wagi. ROT26 dodaje wymierną granicę i rozwinięcie wag; nie wywodzi od nowa ani nie zawłaszcza progu TT.
- **Mature host:** dokładne sumy trygonometryczne, wielomiany Czebyszewa, graniczne momenty sinusowe, stabilność odwracania macierzy, normy funkcjonałów odczytu.
- **Nie rozszerzać:** nie ma tu tezy dla ogólnych pól 3D, masek o fizycznie stałym promieniu, alternatywnego projektora zależnego od metryki, widm innych niż niskie, rzeczywistego historycznego `K_A` i jego oryginalnego byte-exact runnera, zbieżności fizycznej J3/K ani danych pomiarowych.
- `GITHUB_SAVED` i `SLACK_ROUTED` muszą mieć potwierdzony odczyt; samo stworzenie lokalnego pakietu to custody, nie BW ingestion. Kanon/EXEC pozostają poza REC10.

**Final:** `PASS_WITH_ASYMPTOTIC_STABILITY_STRENGTHENING / SOURCE_HELPER_REPRO_PASS / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / BW_PENDING`.