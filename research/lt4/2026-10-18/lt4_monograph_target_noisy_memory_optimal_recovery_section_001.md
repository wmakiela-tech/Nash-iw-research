# 7.5b. Nieznane przygotowanie, ograniczony błąd pomiaru i informacja wystarczająca dla celu

## 7.5b.1. Wspólny nośnik dynamiki i pomiaru

Niech \(X,Y\) będą rzeczywistymi przestrzeniami Hilberta, a dla zapewnienia dokładnego twierdzenia minimaksowego niech w tej sekcji przestrzeń przygotowań \(Y=\mathbb R^n\) będzie skończenie wymiarowa. Niech \(\mathcal L\) będzie blokowym generatorem z §7.5a, \(S(t)=e^{t\mathcal L}\) jego legalną półgrupą, a \(P\) projekcją na obserwowany sektor. Dla **skalarnego** celu \(G:X\to\mathbb R\) mamy z twierdzenia 7.6
\[
z(T)=a_T(x_0)+q_T(x_0)+m_T^\top y_0,\quad
m_T:=M(T)^*1,\quad M(T)=GPS(T)J_Y. \tag{7.9}
\]
Przygotowanie \(y_0\) pozostaje nieznane, ale należy do znanej kuli \(\|y_0\|\le R\), \(R>0\). Poprawka \(q_T\) jest tutaj **znana** dla danego \(x_0\) i modelu; gdy jest nieznana, należy ją oszacować osobno. Po pomiarze
\[
b=C y_0+\eta,\qquad \|\eta\|\le\delta,\qquad
C:\mathbb R^n\to\mathbb R^p, \quad\delta\ge0, \tag{7.10}
\]
szukamy estymatora \(\hat z(b)=a_T+q_T+\varphi(b)\). Ryzyko ma charakter deterministycznego błędu najgorszego przypadku, a nie wariancji względem rozkładu szumu.

**Twierdzenie 7.9 (dokładne ryzyko skalarnego celu przy ograniczonym szumie).**
W przestrzeniach euklidesowych i przy dowolnych regułach \(\varphi:\mathbb R^p\to\mathbb R\) zachodzi
\[
\begin{split}
\mathcal E(C,m_T;R,\delta)
&:=\inf_\varphi\sup_{\|y\|\le R,\|\eta\|\le\delta}
  |m_T^\top y-\varphi(Cy+\eta)|\\
&=\max_{\|v\|\le R,\ \|Cv\|\le\delta}|m_T^\top v|\\
&=\min_{w\in\mathbb R^p}
  \bigl[R\|m_T-C^\top w\|+\delta\|w\|\bigr].
\end{split} \tag{7.11}
\]
Optymalny estymator może być liniowy: \(\varphi_*(b)=w_*^\top b\).

*Dowód.* Niech \(v\) spełnia oba ograniczenia. Legalne pary \((y,\eta)=(v,-Cv)\) i \((-v,Cv)\) dają identyczny pomiar \(b=0\), a cele \(m_T^\top v\) i \(-m_T^\top v\). Jeden estymator po pomiarze \(b=0\) popełnia błąd nie mniejszy niż \(|m_T^\top v|\); to daje dolne oszacowanie przez maksimum w (7.11).

Dla dowolnego \(w\) estymator liniowy ma błąd
\[
|(m_T-C^\top w)^\top y-w^\top\eta|
\le R\|m_T-C^\top w\|+\delta\|w\|.
\]
Stąd uzyskujemy górne oszacowanie przez infimum. Aby wykazać równość, rozważmy funkcję
\(F(v,w)=(m_T-C^\top w)^\top v+\delta\|w\|\)
na zwartej wypukłej kuli \(\|v\|\le R\) i wypukłej \(\mathbb R^p\). Dla ustalonego \(w\) jest ona liniowa w \(v\), dla ustalonego \(v\) wypukła i ciągła w \(w\). Skończenie wymiarowa postać minimaksu wypukłego daje
\[
\sup_{\|v\|\le R}\inf_w F(v,w)
=\inf_w\sup_{\|v\|\le R}F(v,w).
\]
Wewnętrzne \(\inf_w[\delta\|w\|-(Cv)^\top w]\) wynosi \(0\), gdy \(\|Cv\|\le\delta\), i \(-\infty\) w pozostałym przypadku. Po prawej \(\sup_{\|v\|\le R}F=R\|m_T-C^\top w\|+\delta\|w\|\). Wykorzystujemy symetrię zbioru dopuszczalnych \(v\), aby zastąpić funkcjonał liniowy jego wartością bezwzględną. Minimum po \(w\) jest osiągane: gdy \(\delta>0\), funkcja jest koercywna, a przy \(\delta=0\) jest to problem rzutowania \(m_T\) na domknięty obraz \(C^\top\). \(\square\)

## 7.5b.2. Informacja wystarczająca, koszt dokładności i legalność aparatury

**Wniosek 7.2 (dokładne odtwarzanie, brak szumu).** Przy \(\delta=0\)
\[
\mathcal E(C,m_T;R,0)=R\|P_{\ker C}m_T\|.
\]
Błąd znika dokładnie wtedy, gdy \(\ker C\subseteq\ker m_T^\top\). Odtworzenie całego stanu ukrytego nie jest konieczne: wystarcza dostęp do ilorazu rozróżniającego wybrany cel.

**Wniosek 7.3 (nieusuwalny szum przy stałej aparaturze).** Dla \(\delta>0\), \(R>0\) i \(m_T\ne0\) mamy \(\mathcal E(C,m_T;R,\delta)>0\), nawet gdy \(C\) jest różnowartościowa. Wystarczy wybrać odpowiednio mały niezerowy \(v\) równoległy do \(m_T\), aby \(\|Cv\|\le\delta\).

**Wniosek 7.4 (niebezpieczeństwo nieograniczonego wzmocnienia).** Dla \(Y=W=\mathbb R\), \(m_T=1\), \(C_a y=ay\) i \(R=1\) dostajemy \(\mathcal E(C_a,1;1,\delta)=\min(1,\delta/|a|)\) dla \(a\ne0\). Jeśli dozwalamy \(a\to\infty\) bez zmiany kosztu energii, kalibracji i poziomu szumu, matematyczna „poprawa pomiaru” wynika z nielicencjonowanego wzmocnienia urządzenia. Porównywanie konstrukcji czujników wymaga zatem oddzielnego, fizycznego kontraktu dostępnych \(C\).

**Twierdzenie 7.10 (adwersarialne powtórzenia nie zwiększają gwarantowanej precyzji).** Załóżmy, że \(k\) pomiarów ma postać \(b_j=Cy+\eta_j\), a przeciwnik może niezależnie wybierać dowolne \(\|\eta_j\|\le\delta\), bez wspólnego ograniczenia ich całkowitej energii. Dokładny minimaksowy błąd estymacji skalarnego \(m_T^\top y\) z pełnej krotki \((b_1,\ldots,b_k)\) jest równy błędowi z jednego pomiaru (7.11).

*Dowód.* Estymator pomijający wyniki \(b_2,\ldots,b_k\) daje nie większe ryzyko niż \(\mathcal E(C,m_T;R,\delta)\). Dla dolnego oszacowania wybierzmy \(v\) spełniające \(\|v\|\le R\), \(\|Cv\|\le\delta\). Dwa stany \(v,-v\) i szumy odpowiednio \(\eta_j=-Cv\) i \(+Cv\) przy każdym \(j\) dają tę samą krotkę zer, więc żaden estymator nie pokona dolnej granicy z twierdzenia 7.9. \(\square\)

Powtarzanie pomiarów zmniejsza niepewność w innym modelu, np. przy niezależnym, wycentrowanym szumie losowym albo przy jednym *wspólnym* budżecie normy złożonego szumu. Żaden z tych modeli nie wynika z jednostkowego ograniczenia \(\|\eta_j\|\le\delta\).

## 7.5b.3. Dostępny pomiar historii a geometria celu

W fizycznym modelu pełna aparatura mierzy zwykle liniowe obserwable stanów w chwilach \(t_1,\ldots,t_k\). Przy znanym przygotowaniu sektora obserwowanego \(x_0\), legalnym liniowym czujniku \(H:X\to\mathbb R^d\) oraz niezależnych błędach modelu i pomiaru należy najpierw oddzielić deterministyczny wkład:
\[
b_j=H P S(t_j)(J_Xx_0+J_Yy_0)+\eta_j
=a_j(x_0)+q_j(x_0)+C_j y_0+\eta_j,
\quad C_j=HP S(t_j)J_Y. \tag{7.12}
\]
Po dokładnym odjęciu **znanych** \(a_j+q_j\) i zestawieniu portów otrzymujemy \(b= C_{\mathcal I}y_0+\eta\). Jeśli zadeklarowany jest *wspólny* budżet \(\|\eta\|\le\delta\), a celem jest \(m_T^\top y_0\), stosujemy wprost (7.11) z \(C_{\mathcal I}\). Jeśli szumy mają oddzielne ograniczenia, zbiór błędów jest iloczynem kul i jego funkcja wspierająca, a nie automatycznie norma euklidesowa \(\delta\|w\|\), wchodzi do formuły dualnej.

**Twierdzenie 7.11 (wystarczalność pomiaru historii dla celu przy braku szumu).** Niech
\[
\mathcal W_{\mathcal I}= C_{\mathcal I}^\top C_{\mathcal I}
=\sum_{j=1}^k C_j^\top C_j.
\]
Przy \(\delta=0\) błąd minimaksowy skalarnego celu końcowego jest równy
\[
R\bigl\|P_{\ker\mathcal W_{\mathcal I}}m_T\bigr\|.
\]
Zanika dokładnie wtedy, gdy \(m_T\) należy do obrazu \(C_{\mathcal I}^\top\). Warunek ten jest słabszy od obserwowalności całego \(y_0\), wymagającej \(\ker \mathcal W_{\mathcal I}=\{0\}\).

*Dowód.* Zachodzi \(\langle \mathcal W_{\mathcal I}v,v\rangle=\sum_j\|C_jv\|^2\), więc \(\ker \mathcal W_{\mathcal I}=\ker C_{\mathcal I}\). Stosujemy wniosek 7.2 oraz w skończonym wymiarze \((\ker C_{\mathcal I})^\perp=\operatorname{ran} C_{\mathcal I}^\top\). \(\square\)

To standardowy wynik z liniowej obserwowalności i odtwarzania funkcjonału, ujęty tu w języku operatora \(M(T)\) z §7.5a. Nie należy bez dowodu przenosić go na nieliniowe przygotowania, nieograniczone porty Hilberta ani dowolne procesy kwantowe z interwencjami.

## 7.5b.4. Oscylator jako falsyfikator źle wybranego czasu pomiaru

Dla oscylatora z §7.5a mamy
\(x(t)=x_0\cos t+y_0\sin t\).
Po dokładnym odjęciu znanego wkładu \(x_0\cos t_s\) jeden skalarny pomiar w chwili \(t_s\) zwraca
\[
b=(\sin t_s)y_0+\eta,\qquad |\eta|\le\delta.
\]
Cel końcowy to wkład ukrytego przygotowania \(z_T^{\rm hidden}=(\sin T)y_0\). Przy \(|y_0|\le R\) wzór (7.11) redukuje się do **ścisłej** zależności
\[
\mathcal E_{T,t_s}
=|\sin T|\min\!\left(R,\frac{\delta}{|\sin t_s|}\right)
\quad\text{dla }\sin t_s\ne0, \tag{7.13}
\]
zaś dla \(\sin t_s=0\) ryzyko wynosi \(R|\sin T|\). W chwili \(t_s=\pi/2\) obserwacja jest maksymalnie czuła na \(y_0\), natomiast w chwilach \(t_s\in\pi\mathbb Z\) nie wnosi żadnej informacji o przygotowaniu ukrytym. Jeśli \(T=\pi\), ukryta niepewność celu znika bez pomiaru, ale błąd **surowej prognozy bez pamięci** może być równy \(-2x_0\), jak dowiedziono w §7.5a. Nie wolno mieszać tych dwóch błędów.

Ten przykład wskazuje trzy różne obiekty projektowe: funkcję celu końcowego, prawidłowy czas pomiaru oraz prawo szumu. Dla fizycznej realizacji konieczny byłby także kontrakt kosztu uzyskania danej obserwabli i wpływu pomiaru na dalszą ewolucję.

## 7.5b.5. Obszar rzeczywiście otwarty

Dotychczasowe twierdzenia są znanym rachunkiem *optimal recovery* po zastosowaniu do konkretnego operatora pamięci \(M(T)\). Potencjalnie badawczy problem powstaje dopiero dla **fizycznie ograniczonej rodziny obserwacji**, kiedy czujniki oddziałują zwrotnie na układ, pomiary są dopuszczone tylko w wybranych chwilach, a ich koszt i zakłócenia są sprzężone z dynamiką. Wtedy nie wolno zakładać arbitralnej macierzy \(C\), niezmienionej półgrupy \(S(t)\) ani niezależności szumu od sygnału.

Precyzyjny problem brzmi: dla zadanej klasy interwencji \(\mathfrak I\), przygotowań \(K\), funkcjonału celu \(Q_T\) i prawa pomiaru \(P_{\mathcal I}(\cdot\mid y_0)\) wyznaczyć minimalny błąd najgorszego przypadku, a następnie wykazać, kiedy optymalny protokół można zastąpić czujnikiem liniowym niezmieniającym dynamiki. Twierdzenie 7.9 daje **klasę odniesienia do falsyfikacji**; nie daje wyniku dla całej \(\mathfrak I\).

### Literatura

C. A. Micchelli, T. J. Rivlin, *A Survey of Optimal Recovery*, w: *Optimal Estimation in Approximation Theory* (1977), DOI 10.1007/978-1-4684-2388-4_1.

M. Ettehad, S. Foucart, *Instances of Computational Optimal Recovery: Dealing with Observation Errors*, *SIAM/ASA Journal on Uncertainty Quantification* **9** (2021), 1438–1456, DOI 10.1137/20M1328476.

S. Foucart, *Instances of Computational Optimal Recovery: Refined Approximability Models*, *Journal of Complexity* **62** (2021), 101503, DOI 10.1016/j.jco.2020.101503.

Twierdzenia 7.9–7.11 są kwalifikowanymi zastosowaniami klasycznej analizy wypukłej, geometrii przestrzeni Hilberta i teorii obserwowalności do nośnika pamięci z §7.5a. Ich formalna poprawność nie ustanawia oryginalności naukowej całego mechanizmu ani nowej fizyki; szczególny wkład dalszej pracy wymaga znalezienia i dowiedzenia nowych, fizycznie ograniczonych warunków dopuszczalnego pomiaru.