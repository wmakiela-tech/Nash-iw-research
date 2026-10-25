# IW/NASH — REC10 ROT34
## Niezależna recenzja PRF11 R33: najmniejsza liczba sond łamiąca symetrię Helstroma, dokładny obszar progu jednego zliczenia i pierwiastkowy punkt zmiany reżimu

**Data:** 2026-10-25 (Europe/Warsaw, CET).  
**Komórka:** `IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10`.  
**Werdykt:** `PASS_WITH_SHARPER_NOISE_THRESHOLD_AND_SMALLER_COUNTEREXAMPLE / NONBLIND / SOURCE_TYPED`.  
**Pierwszeństwo:** PRF11 R29–R33 (wszystkie procesy i model szumu), REC10 ROT29 (diament po ustalonym echo), REC10 ROT32–33 (idealny SWAP i progi n). Nowe w tym obrocie są: (a) dokładny **minimalny** czterosondowy falsyfikator optymalności P_sym przy szumie i certyfikat n≤3; (b) ścisła granica zakresu, w którym wystarczający warunek PRF R33 jest **konieczny i dostateczny**; (c) pierwiastkowe zachowanie krytycznego budżetu tuż po przełączeniu testu. Wszystko w dojrzałej matematyce Helstroma, reprezentacji permutacyjnych i testów Poissona — **bez roszczenia nowości**.

### 0. Ścisła baza źródłowa i granica dopuszczalnego twierdzenia

Audytowany dokument: `research/prf11/2026-10-25/IW_PRF11_R33_NOISY_MULTISLOT_POISSON_LIMIT_AND_MEMORY_VISIBILITY_GATE_001_20261025.md`; blob Git `7bf942576e6a05ffbf78aa9c21d2f069de30f529`. R33 poprawnie wyróżnia **jedną** ustaloną sekwencję n sond z idealnymi SWAP i indywidualny **końcowy** kanał dephasing `D_r` na każdej sondzie. To nie jest fizyczny model strat pamięci w czasie przechowywania, ani pełny proces comb ze swobodnymi operacjami pośrednimi.

Dla q=exp(-a/n), a=γT>0, końcowe macierze w bazie słów binarnych x,y długości n mają postać:

\[
  \rho_A(x,y)=2^{-n}q^{||x|-|y||}r^{d_H(x,y)},\qquad
  \rho_B(x,y)=2^{-n}(qr)^{d_H(x,y)}. \tag{34.1}
\]

P_sym jest projektorem na przestrzeń całkowicie symetryczną. PRF R33 już wykazał, że przy r<1 P_sym może nie być optymalny, podając dokładny kontrprzykład n=5. W rozdziale o granicy Poissona PRF R33 już udowodnił dokładną asymptotyczną normę śladową `2 TV(Pois(b/2),Pois((a+b)/2))` dla r_n=exp(-b/n), a także istnienie i jednoznaczność b_crit(a), ale podał b_sym jako **ogólnie tylko wystarczającą** granicę. Nie powtarzamy tamtych twierdzeń jako nowych.

### 1. Twierdzenie ROT34.1 — najmniejszy kontrprzykład wymaga dokładnie 4 sond

**Twierdzenie.** Dla każdego q,r∈[0,1], jeśli n=2 lub n=3, P_sym jest optymalnym końcowym pomiarem Helstroma dla stanów (34.1). Już dla n=4 istnieje dokładna para (q,r)=(4/5,1/2), dla której P_sym **nie jest** optymalny.

**Dowód dla n=2.** Różnica Δ=ρ_A−ρ_B zeruje skrajne warstwy wag 0 i 2. W przestrzeni o wadze 1 operator jest proporcjonalny do macierzy `[[0,1],[1,0]]` ze współczynnikiem `r²(1−q²)/4`. Symetryczny wektor warstwy ma nieujemną wartość własną, antysymetryczny — niedodatnią. Projektor P_sym jest zatem dodatnią częścią spektralną Δ.

**Dowód dla n=3.** Różnica Δ działa tylko na warstwy wag k=1,2 i komutuje z działaniem grupy permutacji współrzędnych. Ograniczenie do dwóch znormalizowanych wektorów Dicke ma dokładną macierz

\[
 \Delta_{\rm sym}=\frac{r^2(1-q^2)}4
 \begin{pmatrix}1 &qr/2\\qr/2&1\end{pmatrix}\succeq0.
 \tag{34.2}
\]

Część nie-symetryczna jest sumą dwóch równoważnych kopii standardowej reprezentacji S_3. Dla wektorów w warstwie k=1,2 o współczynnikach `1_{x_1=1}−k/3` jej forma Grama wynosi

\[
 G=\frac{r^2(q^2-1)}{12}
 \begin{pmatrix}1&qr\\qr&1\end{pmatrix}\preceq0.
 \tag{34.3}
\]

Ponieważ 0≤qr≤1, obie macierze wewnętrzne są dodatnio półokreślone. W tym rozkładzie całe Δ ma dodatni blok symetryczny i ujemny dopełniający, więc P_sym jest pomiarem Helstroma. Końce q=0/1 i r=0/1 wynikają bez osobnych wyjątków z półokreśloności.

**Dokładny czterosondowy falsyfikator.** Dla n=4, q=4/5, r=1/2 zdefiniuj dla słowa x∈{0,1}^4 wektor

\[
  v_x=\sum_{k=1}^3 c_k\,1_{\{|x|=k\}}\left(x_1-\frac{k}{4}\right),
  \quad(c_1,c_2,c_3)=(-1,+1,-1).
  \tag{34.4}
\]

Suma współczynników w każdej warstwie jest zerowa: P_sym v=0. Arytmetyka **wymierna** na pełnej macierzy 16×16 (34.1) daje bez zaokrągleń:

\[
  v^\top v=3,\quad
  v^\top(\rho_A-\rho_B)v=\frac{81}{320000}>0,\quad
  \frac{v^\top\Delta v}{v^\top v}=\boxed{\frac{27}{320000}}>0.
  \tag{34.5}
\]

P_sym pomija więc dodatni kierunek Δ, zatem nie jest optymalny. Niezależna diagonalizacja numeryczna daje TV(P_sym)=0.05855625 i TV(Helstrom)=0.06021894125846723; ścisły dowód stanowi (34.5), nie te liczby. Połączenie n≤3 i n=4 dowodzi **ostrości minimalnej liczby sond**. To poprawia rozmiar świadka PRF R33 bez podważania jakiegokolwiek jego wyniku.

### 2. Twierdzenie ROT34.2 — dokładna granica, gdy wystarcza próg jednego zliczenia

Niech μ=b/2, ν=(a+b)/2, a>0, b≥0. W asymptotycznym eksperymencie R33 optymalny test na podstawie liczby wyników minus K to test ilorazu wiarygodności dwóch rozkładów Poissona:

\[
  L(k)=\frac{P_{\nu}(k)}{P_\mu(k)}
       =e^{-a/2}(1+a/b)^k\quad(b>0).
\]

Próg `K≥1` jest dokładnie optymalny wtedy i tylko wtedy, gdy L(1)≥1, tzn.

\[
 b\le B_1(a):=\frac{a}{e^{a/2}-1}.\tag{34.6}
\]

W tym całym obszarze TV optymalne jest równe `e^{-b/2}(1−e^{-a/2})`, więc próg przewagi nad **idealnym** optimum jednoslotowym `1−e^{-a}` wynika z **równości**:

\[
  b_0(a):=2\ln\frac{2}{1+e^{-a/2}}.\tag{34.7}
\]

Funkcja b_0(a) jest ściśle rosnąca, od 0 do 2ln2. Funkcja B_1(a) jest ściśle malejąca, od 2 do 0: pochodna `(e^{a/2}-1)-(a/2)e^{a/2}` jest ujemna dla a>0. Istnieje zatem **jedyny** dodatni punkt przejścia a_* rozwiązujący `b_0(a_*)=B_1(a_*)`. Obliczenie 80 cyfr daje:

\[
 \boxed{a_*=2.740004197619900494582386295290629754529\ldots,}\tag{34.8}
\]
\[
 b_*=0.9334477450951870949860370797717906570817\ldots.
\]

**Wynik globalny dla asymptotycznego R33:**

- Jeśli `0<a≤a_*`, to **rzeczywisty dokładny krytyczny budżet** `b_crit(a)` całego końcowego testu Helstroma jest równy `b_0(a)`, a optymalną decyzją na granicy jest `K≥1` (przy równości ilorazów oba są równie dobre).
- Jeśli `a>a_*`, to `b_crit(a)>b_0(a)`; na granicy krytycznej próg optymalnego licznika wynosi co najmniej `K≥2`. Warunek (34.7), który PRF prawidłowo podał jako wystarczający, nie jest już konieczny.

**Dowód drugiego przypadku:** przy b=b_0(a)>B_1(a) pojedynczy błąd K=1 faworyzuje raczej hipotezę μ niż ν. Zamiana progu z K≥1 na K≥2 ściśle zwiększa TV. Ponieważ przy b_0 prosty test osiąga dokładnie porównywaną granicę, pełny test ją przekracza. Z ciągłej ściśle malejącej funkcji TV w b (twierdzenie źródłowe PRF R33) wynika `b_crit>b_0`.

### 3. Twierdzenie ROT34.3 — pierwiastkowa nieanalityczność tuż nad punktem zmiany

Dla obszaru, w którym optymalny test liczy K≥2, przy μ=b/2, ν=(a+b)/2 definiujemy

\[
  G(a,b)=2[e^{-\mu}(1+\mu)-e^{-\nu}(1+\nu)]-(1-e^{-a}).\tag{34.9}
\]

W punkcie `(a_*,b_*)` mamy jednocześnie `G=0` i `G_b=0`, ponieważ `μe^{-μ}=νe^{-ν}`. Bezpośrednie różniczkowanie daje

\[
 G_a=\nu e^{-\nu}-e^{-a}>0,\qquad
 G_{bb}=-\frac{1-e^{-a}}4<0\quad\text{w punkcie }(a_*,b_*).\tag{34.10}
\]

Rozwinięcie Taylora względem `(a-a_*,b-b_*)` i wybór dodatniej gałęzi rozwiązania dają

\[
 \boxed{b_{crit}(a)=b_*+c_*\sqrt{a-a_*}+O(a-a_*)\quad(a\downarrow a_*\text{ z prawej}),}\tag{34.11}
\]

\[
 c_*=\sqrt{\frac{8(\nu_*e^{-\nu_*}-e^{-a_*})}{1-e^{-a_*}}}
   =1.39666768421816458859611383863953926635\ldots.
\]

Powyżej a_* właściwa dopuszczalna gałąź jest ta z `b>b_*`, dla której K≥2; niewłaściwa ujemna gałąź kwadratowa należy do obszaru nieoptymalnego testu. Tłumaczy to szybkie rozszerzenie dopuszczalnego budżetu natychmiast za a_* i brak możliwości gładkiego przedłużenia prostego wzoru b_0(a) na duże a. Jest to własność matematycznego **warunkowego modelu szumu końcowego**, nie fazowe przejście fizycznego urządzenia.

**Weryfikacja:** dla `a-a_*` =1e-5,1e-6,1e-7 wyznaczone ilorazy `(b_crit(a)-b_*)/sqrt(a-a_*)` wyniosły kolejno 1.396793487978266, 1.396707658453968, 1.396680344330281 i zbiegają do dokładnego współczynnika c_*.

### 4. Audyt liczbowy i negatywna wiedza

Niezależny wykonywalny program `rec10_rot34_prf11_r33_noise_threshold_repro.py`:

- Konstruuje od zera wszystkie 16×16 elementy Δ i dokładną dodatnią formę (34.5) w `sympy.Rational`, bez kodu PRF.
- Wyprowadza symbolicznie certyfikat n=2,3 w kategoriach dowolnych symboli q,r.
- Liczy próg a_*,b_* do 80 cyfr mpmath, testuje osobno prawo optymalnego licznika przy b_0 oraz numeryczne b_crit dla 9 a. W szczególności powtarza PRF R33 wartości `.0493750651` przy a=.1, `.7597709861` przy a=2, `1.1863292719` przy a=4ln2 oraz `2.9087089213` przy a=4.
- Konstruuje 240 bezpośrednich przypadków gęstych stanów kwantowych (n=2,…,7, po 40 par q,r), w tym 134 przypadki nieoptymalności P_sym; maksymalna reszta formuły projekcyjnej `4.44×10^-16`. Dla n≤3 optymalność P_sym testowana ponadto symbolicznie **dla całego kwadratu** q,r∈[0,1].
- Testuje współczynnik osobliwej gałęzi (34.11) na 3 małych dodatnich przesunięciach. Wszystkie końcowe asercje PASS.

**Proweniencja:** obiekt badania i piątosondowy falsyfikator były jawne przed ROT34. Czterosondowy świadek znaleziono po przeglądzie numerycznych klas n, a następnie zamrożono i udowodniono arytmetyką wymierną — NIE był to test blind/held-out. Progi mpmath są obliczeniami wysokoprecyzyjnymi, a nie certyfikowanymi przedziałami zaokrągleń; dowody istnienia, jednoznaczności i postaci są analityczne. Nie zakładamy niefizycznej wspólnej szumiącej pamięci w miejsce endpoint D_r. Nie wnioskujemy o pełnym optimum wielu slotów.

### 5. Atrybucja, sufit i dyspozycja

**Zachować pierwszeństwo PRF11 R33** dla pełnej granicy kwantowej Poissona, dla źródłowego pięciosondowego falsyfikatora, dla krytycznej funkcji b_crit i jej istnienia. **ROT34** tylko zmniejsza minimalny rozmiar świadka, identyfikuje skończoną ostrą granicę zakresu wzoru b_sym i osobliwą geometrię tego punktu. Matematyka wykorzystuje klasyczną hipotezę Neymana–Pearsona i podstawową reprezentację permutacyjną; **NO_NOVELTY**.

**Proponowany sygnał do właściciela:** `PRF11_R33_REFEREE_PASS_WITH_N4_MINIMAL_COUNTEREXAMPLE_AND_EXACT_K1_RESOURCE_PHASE_BOUNDARY`, bez zmiany statusu kanonicznego, bez zadawania zadania kaskadowego. **BW / przyjęcie PRF11 / podpis Moderatora pozostają osobnymi zdarzeniami.**

`NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_GLOBAL_MULTISLOT_OPTIMUM / SOURCE_TYPED / NONBLIND`