\[
\operatorname{Tr}[\Pi_\pm\mathcal D_{Z,t_d}(\rho)]
 =\operatorname{Tr}[\Pi_\pm\rho].\tag{R24.1}
\]

W szczególności w modelu D opóźnienie detekcji może być dowolnie długie **matematycznie bez wpływu na prawdopodobieństwo**; zwiększa jednak czas, a więc ryzyko resetu ξ. Nie przenosić tego na T1, leakage, rzeczywistą integrację wzmacniacza, błędy kalibracji i chwilowe sterowanie poprzeczne.

Niech U_i∈{±1} będzie bezbłędnym wynikiem i,j=1,2 przy wspólnej osi, a C_i niezależnym losowym znakiem z Pr(C_i=−1)=η. Zapisany wynik to R_i=C_i U_i; więc E[R_1R_2]=(1−2η)^2 E[U_1U_2]. Otrzymujemy dla dowolnej dynamiki stanów (również po zmianie ξ między strzałami):

\[
\boxed{p_\eta(\mathrm{same})=\tfrac12+(1-2\eta)^2[p_0(\mathrm{same})-\tfrac12].}\tag{R24.2}
\]

Stąd rozróżniający kontrast pod jednakową, skalibrowaną η kurczy się dokładnie o c_η=(1−2η)². **Nie** zachodzi w tej postaci dla niesymetrycznej macierzy pomyłek, dryfu η zależnego od ξ, czy korelacji pomyłek między odczytami.

## 3. Twierdzenie R24.2 — kontrola dwóch różnych ξ: nowe ograniczenie przy resetach TYLKO między odczytami

Rozważ dwa kompletne odczyty ze stałymi, lecz możliwie RÓŻNYMI częstotliwościami ξ_1,ξ_2. Niech m_j(ξ) oznacza idealny średni znak wyniku dla j=X,Y,Z po właściwym pulsie i ekspozycji. Z prywatnym wspólnym losowaniem osi i warunkową niezależnością dwóch świeżych stanów:

\[
p_A(\mathrm{same}\mid\xi_1,\xi_2)=\tfrac12+\tfrac12\sum_{j=X,Y,Z} w_j m_j(\xi_1)m_j(\xi_2).
\tag{R24.3}
\]

Dla prostokątnego źródłowo aktywnego Y przygotowania z Ω=10, tπ/2=π/(2Ω), Z odczytywane bez obrotu, obliczamy dokładnie

\[
m_Z(\xi)=\frac{u^2+\cos[(\pi/2)\sqrt{1+u^2}]}{1+u^2},\qquad u=\xi/\Omega.
\tag{R24.4}
\]

**Globalny dowód m_Z(ξ)≥0:** dla u²≥1 licznik ≥u²−1≥0. Dla u²≤1, z θ=(π/2)(√(1+u²)−1)≥0, mamy cos(π/2+θ)=−sinθ≥−θ≥−πu²/4. Zatem licznik ≥(1−π/4)u²≥0. Nie używamy numerycznego skanowania. Ponieważ |m_X|≤1, |m_Y|≤1 i m_Z(ξ_1)m_Z(ξ_2)≥0, z wag X=.18,Y=.20,Z=.62 wynika

\[
\boxed{p_A(\mathrm{same}\mid\xi_1,\xi_2)\ge\frac{1-w_X-w_Y}{2}=0.31.}
\tag{R24.5}
\]

To **nowa, dystrybucyjnie wolna** podłoga przy resetowaniu źródła *wyłącznie pomiędzy całymi odczytami*, a nie w środku źródłowo aktywnego impulsu, swobodnej ekspozycji czy analizy. Gdy ξ może skoczyć w środku odczytu, stosujemy tylko bezpieczną podłogę 0, a nie 0.31.

## 4. Twierdzenie R24.3 — warunkowy hazard Poissona i skończone prawdopodobieństwa obu błędów

Czas fizyczny pojedynczego strzału z najdłuższą analizą to Δ+2tπ/2+t_d. Czas od początku pierwszego przygotowania do końca drugiej detekcji (z resetem sensora między nimi) ogranicza z góry

