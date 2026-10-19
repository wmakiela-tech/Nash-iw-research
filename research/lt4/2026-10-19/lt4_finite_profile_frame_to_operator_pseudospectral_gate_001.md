# Od błędu profilowego do normy operatorowej: ostry warunek ramy i granica transportu pseudospektralnego

**Status:** rozdział IV monografii — materiał pogłębiający; twierdzenia z dowodami; matematyka gospodarzy: teoria ram skończenie wymiarowych, normy Hilberta–Schmidta i perturbacje pseudospektralne. **Nie deklaruje nowości matematycznej ani wierności konkretnego instrumentu DTC.**

## 1. Typ problemu

Niech \(H_N,Z_N\) będą skończenie wymiarowymi przestrzeniami Hilberta, a \(E_N\in\mathcal B(H_N,Z_N)\) będzie **liniowym** operatorem błędu: na przykład różnicą dwóch **poprawnie przeniesionych na jeden nośnik** dyskretnych operatorów rozwiązań. Testujemy \(E_N\) na wektorach \(v_{N,1},\ldots,v_{N,m_N}\).

Dla skrótu pomijamy indeks \(N\). Niech \(U=\operatorname{span}\{v_i\}\subset H\), \(P_U\) będzie projekcją ortogonalną oraz
\[
S:U\to U,\quad
S u=\sum_{i=1}^m\langle u,v_i\rangle v_i
\]
operatorem ramy na \(U\). Niech \(\alpha=\lambda_{\min}(S|_U)>0\) — najmniejsza wartość własna ramy na rzeczywiście testowanym podprzestrzennym nośniku. Definiujemy profilowy błąd RMS
\[
r=\left(\frac1m\sum_{i=1}^m\|E v_i\|^2\right)^{1/2}. \tag{1}
\]
Hipoteza kluczowa brzmi: normy i iloczyny skalarne, względem których liczymy \(r,\alpha,\|E\|\), muszą być **tą samą metryką**. Przeliczenie między ważonymi normami wymaga oddzielnej, jednostajnie kontrolowanej równoważności norm.

## 2. Twierdzenie o ostrym odzyskiwaniu normy z ramy

**Twierdzenie 1 (profilowa kontrola operatorowa na testowanym nośniku).** W powyższych warunkach:
\[
\boxed{\;\|EP_U\|_{\mathrm{op}}
\le\left(\frac{\sum_{i=1}^m\|Ev_i\|^2}{\alpha}\right)^{1/2}
=\sqrt{\frac m\alpha}\,r.\;} \tag{2}
\]
W szczególności jeśli \(U=H\), prawa strona kontroluje pełną normę \(\|E\|\).

*Dowód.* Niech \(S=\sum_i |v_i\rangle\langle v_i|\) na \(U\), a \(E_U=E|_U\). Ponieważ \(S\ge\alpha I_U\),
\[
\sum_i\|Ev_i\|^2
=\operatorname{tr}_U(E_U^*E_U S)
\ge\alpha\operatorname{tr}_U(E_U^*E_U)
=\alpha\|E_U\|_{\mathrm{HS}}^2
\ge\alpha\|E_U\|_{\mathrm{op}}^2.
\]
Równość \(\|EP_U\|=\|E_U\|\) kończy dowód. \(\square\)

**Ostrość stałej \(1/\sqrt{\alpha}\).** Jeżeli \(u\in U\) jest jednostkowym wektorem własnym \(S\) do \(\alpha\), a \(w\in Z\) jest jednostkowy, weźmy \(E x=\langle x,u\rangle w\). Wtedy \(\|E_U\|=1\) i \(\sum_i\|Ev_i\|^2=\langle Su,u\rangle=\alpha\). Równość zachodzi w (2). To dowodzi optymalności oszacowania dla zadanej ramy.

**Wniosek 1 (konieczny kontrakt wymiarowy dla ciągu testów).** Jeśli \(U_N=H_N\) i
\[
\sqrt{m_N/\alpha_N}\,r_N\longrightarrow0,
\]
to \(\|E_N\|_{\mathrm{op}}\to0\). Samo \(r_N\to0\) **nie wystarcza**, o ile \(\sqrt{m_N/\alpha_N}\) może rosnąć bez kontroli.

## 3. Dwa falsyfikatory złego wnioskowania

**Przykład A (niewidzialny kierunek ortogonalny).** Jeśli \(U\ne H\), wybierzmy jednostkowy \(w\in U^\perp\) i \(E x=L\langle x,w\rangle z\), gdzie \(z\in Z\) jest jednostkowy. Wtedy \(Ev_i=0\) dla wszystkich profili, czyli \(r=0\), lecz \(\|E\|=L\) może być dowolnie duża. Nie istnieje uniwersalne oszacowanie \(\|E\|\le C r\) dla prób nieobejmujących całego deklarowanego nośnika.

**Przykład B (zanik RMS mimo pełnej ramy).** Na \(H_N=\mathbb C^N\) weźmy profile kanoniczne \(v_i=e_i\), \(i=1,\ldots,N\), oraz \(E_N=|e_1\rangle\langle e_1|\). Mamy \(\alpha_N=1\), \(m_N=N\), a dokładnie
\[
r_N=N^{-1/2}\to0,\qquad \|E_N\|_{\mathrm{op}}=1. \tag{3}
\]
Rodzina testów obejmuje cały nośnik dla każdego \(N\), lecz **średni** profilowy RMS spada, ponieważ błędny jest tylko jeden kierunek. W (2) zachodzi równość, więc czynnik \(\sqrt N\) nie może być usunięty bez dodatkowej informacji.

Wniosek fizyczno-obliczeniowy: jeśli profilowy RMS używa normalizacji przez liczbę przypadków testowych i ich liczba rośnie, nie wolno bez renormalizacji ogłaszać jednostajnej wierności operatorowej.

## 4. Niewytestowana część nośnika i pełna norma

**Twierdzenie 2 (jawna kara za sektory nietestowane).** Jeśli znamy dodatkową niezależnie uzasadnioną granicę
\[
\|E(I-P_U)\|\le\eta,
\]
to
\[
\boxed{\;\|E\|\le \sqrt{m/\alpha}\,r+\eta.\;} \tag{4}
\]

*Dowód.* Rozkład \(E=EP_U+E(I-P_U)\) i nierówność trójkąta wraz z Twierdzeniem 1. \(\square\)

Dla operatorów działających na przestrzeniach różnej geometrii przed zastosowaniem (4) trzeba zdefiniować poprawny wspólny nośnik i mapy identyfikacji. Zbieżność na sztucznie dobranej, wąskiej podprzestrzeni nie daje \(\eta\) dla jej dopełnienia.

## 5. Przeniesienie do pseudospektrów — wyłącznie przy pełnej normie

Niech \(A_N,B_N\in\mathcal B(H_N)\) będą kwadratowymi macierzami na **tym samym** skończenie wymiarowym Hilbercie. Definiujemy otwarte \(\varepsilon\)-pseudospektrum jako
\[
\sigma_\varepsilon(A)=\{z\in\mathbb C:s_{\min}(zI-A)<\varepsilon\}.
\]
Ta definicja obejmuje widmo; przy \(\varepsilon>0\) jest równoważna wersji normy resolwenty.

**Twierdzenie 3 (warunkowy transport pseudospektralny).** Dla \(\delta=\|A_N-B_N\|\) i każdego \(\varepsilon>0\),
\[
\sigma_\varepsilon(A_N)\subset
\sigma_{\varepsilon+\delta}(B_N),
\qquad
\sigma_\varepsilon(B_N)\subset
\sigma_{\varepsilon+\delta}(A_N). \tag{5}
\]
Jeżeli \(E_N=A_N-B_N\), a profile dają ramę jak wyżej, wystarczy jawny kontrakt \(\delta\le\sqrt{m_N/\alpha_N}\,r_N+\eta_N\).

*Dowód.* Dla każdego jednostkowego \(u\),
\(\|(zI-B_N)u\|\le\|(zI-A_N)u\|+\delta\).
Po wzięciu infimum otrzymujemy \(s_{\min}(zI-B_N)\le s_{\min}(zI-A_N)+\delta\). Gdy \(z\in\sigma_\varepsilon(A_N)\), prawa strona jest mniejsza od \(\varepsilon+\delta\). Druga inkluzja jest symetryczna. \(\square\)

Nie wynika z (5) zbieżność widm jako zbiorów z samych obserwacji profili. Dla nie-normalnych operatorów obiektem stabilnym normowo jest tu pseudospektrum **przy zdefiniowanej tolerancji**, nie dowolnie oznaczone pojedyncze wartości własne.

## 6. Związek z aktualną literaturą i prawidłowy zakres

Boffi, Hu, Liang i Zerbinati (arXiv:2610.01501, 1 października 2026), *Finite element exterior calculus for spectra and pseudospectra of advection-diffusion of differential forms*, wyprowadzają wyniki dla schematów FEEC na właściwych przestrzeniach form różniczkowych. Kontrola zbieżności operatorów rozwiązań opiera się tam na stabilności, regularności, projekcjach komutujących i poprawnych warunkach brzegowych. Ich twierdzenia o pseudospektrach korzystają z **normy operatorowej**, nie z małego błędu wybranych pól testowych.

Wyniki (2)–(5) określają dokładnie, kiedy skończona diagnostyka liniowej mapy błędu może dostarczyć normy wymaganej do prostego twierdzenia pseudospektralnego. Nie ustanawiają mostu pomiędzy dowolną diagnostyką RMS a FEEC, bo dla prawdziwego modelu trzeba jeszcze spełnić kontrakt: liniowość badanego operatora błędu, pełność nośnika, zgodność norm, kontrola \(\eta_N\), odpowiednia identyfikacja przestrzeni dyskretnej z ciągłą i — dla rozwiązań różniczkowych — wymogi dziedzinowe i brzegowe.

W szczególności **defekt K_A zmierzony na kilku polach TT nie jest automatycznie liniową mapą operatorową na przestrzeni Hilberta o tych hipotezach**. Bez sprawdzenia tego faktu nie wolno nazywać (2) certyfikatem obiektu DTC.

Dojrzali gospodarze: teoria ram w skończonym wymiarze, normy Hilberta–Schmidta, nierówności śladowe, perturbacja pseudospektralna Trefethena–Embree. Oryginalność twierdzeń 1–3: **nieustalona i mało prawdopodobna jako samodzielna nowa matematyka**. Ich wartością dla monografii jest ilościowy, typowany kontrakt pomiędzy błędem obserwacyjnym i twierdzeniem operatorowym oraz ostre falsyfikatory nielegalnego transferu.

**Bibliografia:** D. Boffi, K. Hu, Y. Liang, U. Zerbinati, arXiv:2610.01501 (2026); L. N. Trefethen, *Pseudospectra of Linear Operators*, SIAM Review 39 (1997), 383–406, DOI 10.1137/S0036144595295284; O. Christensen, *An Introduction to Frames and Riesz Bases*, 2nd ed., Birkhäuser 2016.

**Rozstrzygnięcie redakcyjne:** kandydat do rozwinięcia §4.11 (granice dyskretyzacji), nie samodzielny nowy rozdział. Niezależna recenzja SW/INT i source-native porównanie FEEC pozostają wymagane przed jakimkolwiek claim upgrade.
