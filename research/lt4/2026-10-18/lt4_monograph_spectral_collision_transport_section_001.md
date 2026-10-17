# 7.8.2. Transport spektralny przy mnożniku nierozdzielającym: rola sprzężeń między włóknami

Rozdział 7.8.1 wykazał, że **wystarczającym** warunkiem transportu całego borelowskiego rachunku funkcyjnego jest splatanie jednego mnożnika rozdzielającego oba widma. Nie jest to jednak warunek konieczny dla *ustalonego* splatacza \(J\): operator \(J\) może nie łączyć tych sektorów, które dany mnożnik utożsamia.

Niech \(H_1,H_2\) będą skończenie wymiarowymi zespolonymi przestrzeniami Hilberta i niech
\[
 A=\sum_{i=1}^r\lambda_i P_i,\quad
 B=\sum_{j=1}^s\mu_j Q_j
\]
będą samosprzężone, gdzie \(\lambda_i\) i \(\mu_j\) są parami różnymi wartościami własnymi w obrębie odpowiedniego operatora, a \(P_i,Q_j\) ich projekcjami spektralnymi. Operator \(J:H_1\to H_2\) jest ograniczony (automatycznie w skończonym wymiarze). Dla każdego ograniczonego mnożnika borelowskiego \(f\)
\[
 Q_j[Jf(A)-f(B)J]P_i
 =[f(\lambda_i)-f(\mu_j)]\,Q_jJP_i. \tag{7.14}
\]

**Twierdzenie 7.12 (dokładny test kolizji dla ustalonego splatacza).** Załóżmy, że \(Jh(A)=h(B)J\) dla danej funkcji borelowskiej \(h\). Zdefiniujmy *operator kolizji*
\[
J_{\mathrm{col}}
=\sum_{\substack{\lambda_i\ne\mu_j\\ h(\lambda_i)=h(\mu_j)}}Q_jJP_i. \tag{7.15}
\]
Wtedy dla dowolnej ograniczonej funkcji borelowskiej \(m\)
\[
Jm(A)-m(B)J
=J_{\mathrm{col}}m(A)-m(B)J_{\mathrm{col}}, \tag{7.16}
\]
oraz
\[
\|Jm(A)-m(B)J\|
\le2\|m\|_\infty\|J_{\mathrm{col}}\|. \tag{7.17}
\]
Ponadto
\[
Jm(A)=m(B)J\quad\text{dla wszystkich ograniczonych borelowskich }m
\quad\Longleftrightarrow\quad J_{\mathrm{col}}=0. \tag{7.18}
\]

*Dowód.* Projekcja \(Q_j\) z lewej i \(P_i\) z prawej w równości \(Jh(A)=h(B)J\) daje
\([h(\lambda_i)-h(\mu_j)]Q_jJP_i=0\).
Stąd bloki \(Q_jJP_i\) mogą być niezerowe tylko wtedy, gdy wartości \(h\) są równe. Dla \(\lambda_i=\mu_j\) każdy mnożnik \(m\) przyjmuje tę samą wartość i blok defektu w (7.14) znika. Zatem wszystkie niezerowe bloki defektu należą do części (7.15), co daje (7.16); nierówność (7.17) wynika z dwóch zastosowań nierówności operatorowej.

Jeżeli \(J_{\mathrm{col}}=0\), równość (7.16) zeruje defekt każdego \(m\). Odwrotnie, gdy defekt każdego \(m\) znika, wybieramy dla ustalonej pary różnych wartości \(\lambda_i\ne\mu_j\) borelowski wskaźnik jednoelementowego zbioru \(\{\lambda_i\}\). Wówczas (7.14) wymusza \(Q_jJP_i=0\). Dotyczy to wszystkich składników (7.15), więc \(J_{\mathrm{col}}=0\). \(\square\)

Wniosek: różnowartościowość \(h\) na połączeniu widm jest warunkiem wystarczającym *niezależnym od \(J\)*; dla jednego konkretnego \(J\) mocniejszy jest dokładny test zerowania sprzężeń przez kolizje różnych wartości własnych. Nie istnieje tu sprzeczność z twierdzeniem 7.4.

**Kontrprzykład 7.4 (niedozwolone zastąpienie normy sumy największym blokiem).**
Weźmy
\(A=\operatorname{diag}(0,1)\), \(B=\operatorname{diag}(2,3)\),
\(h(\lambda)=\cos(2\pi\lambda)\) i
\(J=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}\).
Mamy \(h(A)=h(B)=I\). Wszystkie cztery bloki kolizyjne \(Q_jJP_i\) mają normę \(1/2\), lecz \(\|J_{\mathrm{col}}\|=\|J\|=1\). Jeśli \(m(0)=m(1)=1\), \(m(2)=m(3)=-1\), to \(\|m\|_\infty=1\) i
\[
\|Jm(A)-m(B)J\|=2,
\]
co osiąga oszacowanie (7.17). Fałszywa byłaby nierówność
\(\|Jm(A)-m(B)J\|\le2\|m\|_\infty\max_{i,j}\|Q_jJP_i\|\),
która dawałaby \(2\le1\).

Twierdzenie 7.12 dotyczy skończonego czystopunktowego widma. Nie rozszerzamy bez dowodu sumy (7.15) na ciągłe widmo i dowolne mierzalne jądra \(J\). W ogólnym przypadku samosprzężonym bezpieczne kryterium pełnego transportu pozostaje sformułowane przez projekcje spektralne: \(JE_A(\Omega)=E_B(\Omega)J\) dla każdego zbioru borelowskiego \(\Omega\). Twierdzenie nie transportuje automatycznie różniczkowania kompleksu Hilberta ani przestrzeni brzegów; do tego pozostaje potrzebny osobny kontrakt z twierdzenia 7.5.