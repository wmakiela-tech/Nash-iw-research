# Dokładne powiązanie błędu celu z pamięcią i nieznanym przygotowaniem

## 1. Nośniki i dwie odrębne drogi wpływu sektora ukrytego

Niech \(X,Y,Z\) będą przestrzeniami Banacha. Operatory \(A:D(A)\subseteq X\to X\) i \(D:D(D)\subseteq Y\to Y\) generują silnie ciągłe półgrupy \(S_A(t)\) i \(S_D(t)\). Zakładamy **ograniczone** sprzężenia \(B\in\mathcal B(Y,X)\), \(C\in\mathcal B(X,Y)\) i obserwację \(G\in\mathcal B(X,Z)\). Na \(H=X\oplus Y\) operator blokowy
\[
\mathcal L=\begin{pmatrix}A&B\\C&D\end{pmatrix},\quad D(\mathcal L)=D(A)\oplus D(D)
\]
generuje półgrupę \(S(t)\) na mocy twierdzenia o ograniczonym zaburzeniu generatora.

Niech \(P:H\to X\) będzie projekcją, a \(J_X,J_Y\) włożeniami. Dla znanego \(x_0\) i ukrytego \(y_0\) dokładny odczyt wynosi
\[
z(t)=G P S(t)(J_Xx_0+J_Yy_0).
\]
Zdefiniujmy operator **widzialności nieznanego przygotowania**
\[
M(t):=G P S(t)J_Y\in\mathcal B(Y,Z)
\]
i operator **pamięci wygenerowanej przez układ**, \(K(t):=B S_D(t)C\in\mathcal B(X)\). Samo utożsamienie \(M(t)\) z \(K(t)\) jest błędem typu: mają różne dziedziny i przeciwdziedziny. Można jednak wyprowadzić dokładną relację.

## 2. Twierdzenie: jedną odpowiedzią na ukryte przygotowanie kontroluje się także błąd modelu bez pamięci

**Twierdzenie A (tożsamość odpowiedzi celowej).** Dla wszystkich \(t\ge0\), \(x_0\in X\), \(y_0\in Y\) mamy dokładnie
\[
\boxed{
z(t)=G S_A(t)x_0+M(t)y_0
+\int_0^t M(t-s)\,C S_A(s)x_0\,ds.}
\tag{A}
\]
Całka jest silną całką Bochnera w \(Z\). W szczególności przy przygotowanym \(y_0=0\) błąd obserwabli modelu bez pamięci jest równy
\[
q(t,x_0):=z(t)-G S_A(t)x_0
=\int_0^t M(t-s)\,C S_A(s)x_0\,ds.
\tag{B}
\]

*Dowód.* Określmy drugi generator
\[
\mathcal L_0=\begin{pmatrix}A&B\\0&D\end{pmatrix}
\]
o tej samej dziedzinie, co \(\mathcal L\). Różnica \(\mathcal L-\mathcal L_0=J_Y C P\) jest ograniczona. Oba operatory generują półgrupy \(S(t)\), \(S_0(t)\). Wzór Duhamela dla ograniczonego zaburzenia daje
\[
S(t)-S_0(t)
=\int_0^t S(t-s)J_Y C P S_0(s)\,ds.
\]
Dla przygotowania \(J_Xx_0\) mamy \(S_0(s)J_Xx_0=J_X S_A(s)x_0\), ponieważ ukryty blok nie jest wzbudzany, gdy \(C=0\) i \(y_0=0\). Po przemnożeniu przez \(GP\) otrzymujemy (B). Dodając niezależny składnik \(GP S(t)J_Yy_0=M(t)y_0\), dostajemy (A). \(\square\)

Twierdzenie jest prawdziwe również dla **nieograniczonych** \(A,D\), o ile generują półgrupy \(C_0\) i sprzężenia \(B,C\) są ograniczone. Nie zakłada analityczności operatorowo-wartościowej funkcji \(M(t)\), a więc nie stosuje momentowego argumentu wyłącznie dla ograniczonych generatorów.

## 3. Konsekwencje dla wierności celu

**Wniosek A.1 (wierność wszystkich czasów).** Jeżeli \(M(t)=0\) dla wszystkich \(t\ge0\), wtedy dla każdego \(x_0\) i dowolnego \(y_0\)
\[
G P S(t)(J_Xx_0+J_Yy_0)=G S_A(t)x_0.
\]
Zatem nieznany stan ukryty jest niewidoczny dla celu, a całe sprzężenie zwrotne pamięci jest dla tego celu równie niewidoczne. NIE oznacza to, że jądro \(K(t)=B S_D(t)C\) jest zerowe jako operator na \(X\).

**Wniosek A.2 (jedna chwila nie wystarczy).** Z samego \(M(T)=0\) dla wybranego \(T\) nie wynika \(q(T,x_0)=0\). We wzorze (B) występują wszystkie wcześniejsze \(M(T-s)\), nie tylko \(M(T)\). Analogicznie \(q(T,x_0)=0\) nie oznacza \(M(T)=0\). Dwa kryteria wierności odpowiadają odrębnym kanałom informacji.

**Wniosek A.3 (ilościowy błąd pamięci).** Dla każdego \(t,x_0\)
\[
\|q(t,x_0)\|
\le \int_0^t\|M(t-s)\|\,\|C S_A(s)x_0\|\,ds.
\tag{C}
\]
Jeśli \(\|M(u)\|\le\delta\) na \([0,t]\), to
\[
\|q(t,x_0)\|
\le\delta\,\|C\|\int_0^t\|S_A(s)x_0\|\,ds.
\tag{D}
\]
Oznacza to, że **jedno oszacowanie operatora odpowiedzi na nieznany stan ukryty**, pochodzące z poprzedniej analizy minimaksowej, kontroluje także błąd pamięci w wybranym celu. Bez kontroli całej historii \(M(u)\) takiego wniosku nie ma.

## 4. Dokładna suma dwóch źródeł błędu dla celu skalarnego

Niech \(Z=\mathbb R\) lub \(\mathbb C\), \(Y\) przestrzenią Hilberta, a nieznane przygotowanie spełnia \(\|y_0\|\le R\). Model bez pamięci i bez ukrytego przygotowania przewiduje \(a_{\rm bare}(t)=G S_A(t)x_0\).

**Twierdzenie B (skalarna separacja błędu deterministycznego i niepewności).**
\[
\sup_{\|y_0\|\le R}|z(t)-a_{\rm bare}(t)|
=|q(t,x_0)|+R\|M(t)\|.
\tag{E}
\]
Jeżeli natomiast dopuszczamy dokładną poprawkę deterministyczną \(q\) w przewidywaniu, najlepszy możliwy błąd minimaksowy w klasie estymatorów zależnych jedynie od \(x_0\) jest równy \(R\|M(t)\|\).

*Dowód.* Na mocy (A) błąd to \(q+M(t)y_0\). Obraz kuli \(\|y_0\|\le R\) pod skalarnym funkcjonałem liniowym \(M(t)\) jest dyskiem/promieniem o promieniu \(R\|M(t)\|\) w sensie supremum. Kierunek fazy można wybrać tak, aby wektor \(M(t)y_0\) miał ten sam argument co \(q\), co daje równość w (E). Druga teza to minimaks na symetrycznej kuli: centralny estymator \(a_{\rm bare}+q\) jest optymalny, ponieważ każda inna wartość jest co najmniej o tyle samo odległa od jednej z pary przeciwnych realizacji. \(\square\)

W ogólnym Hilbertowskim \(Z\) tożsamość sumy modułów nie jest prawdziwa bez dalszych warunków o geometrycznej zgodności kierunków. Zawsze zachodzą oszacowania
\[
\max\{\|q\|,R\|M(t)\|\}
\le \sup_{\|y_0\|\le R}\|q+M(t)y_0\|
\le\|q\|+R\|M(t)\|.
\]
Dolna granica wynika z symetrii kuli i nierówności dla pary \(\pm y_0\).
