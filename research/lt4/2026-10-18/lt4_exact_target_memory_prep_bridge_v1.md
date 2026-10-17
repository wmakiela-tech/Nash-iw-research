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

## 5. Rozstrzygające kontrprzykłady

**Przykład 1 (jedna chwila dokładna dla przygotowania, pamięć nadal widoczna).**
Dla \(X=Y=\mathbb R\), \(A=D=0\), \(B=1\), \(C=-1\), \(G=1\) mamy generator oscylatora
\[
\mathcal L=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
Stąd \(M(t)=\sin t\), a dla \(x_0=1,y_0=0\) rzeczywisty cel to \(z(t)=\cos t\), model bez pamięci zaś przewiduje \(1\). Wzór (B) daje dokładnie
\[
q(t,1)=-\int_0^t\sin(t-s)\,ds=\cos t-1.
\]
W chwili \(t=\pi\) mamy \(M(\pi)=0\), ale \(q(\pi,1)=-2\). Oznacza to zerowy błąd z nieznajomości **początkowego** \(y_0\), a jednocześnie maksymalny błąd pominięcia **pamięci** w określonej chwili. Dla skalarnych ukrytych danych o promieniu \(R\) błąd surowego modelu jest wtedy dokładnie \(2\).

**Przykład 2 (jądro pamięci niezerowe, lecz niewidoczne dla celu).**
Weźmy \(X=\mathbb R^2\), \(Y=\mathbb R\), \(A=0\), \(D=0\), \(B y=(0,y)\), \(C(x_1,x_2)=x_2\), \(G(x_1,x_2)=x_1\). Wtedy
\[
K(t)=BC=
\begin{pmatrix}0&0\\0&1\end{pmatrix}\ne0,
\]
lecz \(M(t)=0\) dla każdego \(t\), ponieważ sektor \(x_1\) nie jest sprzężony z sektorem ukrytym. Mimo niezerowej pamięci w dynamice \(x_2\), obserwabla \(x_1\) jest dokładnie opisana równaniem bez pamięci. Nie ma sprzeczności: cel nie rozdziela wszystkich stanów \(X\).

**Przykład 3 (brak pamięci przy silnej zależności od przygotowania).**
Dla \(X=Y=\mathbb R\), \(A=D=C=0\), \(B=1\) mamy \(K(t)=0\), lecz \(M(t)=t\), więc \(z(t)=x_0+t y_0\). Przy \(y_0=0\) model bez pamięci jest dokładny dla wszystkich chwil; przy nieznanym \(y_0\) nie jest. Wniosek odwrotny do A.1 jest zatem fałszywy.

## 6. Z próbek czasowych do ilościowego certyfikatu, z normą generatora

Załóżmy dodatkowo, że **pełny** generator \(\mathcal L\) jest ograniczony. Niech \(T>0\), \(\ell=\|\mathcal L\|\), \(K_G=\|GP\|\,\|J_Y\|\). Wówczas \(M(t)\) jest różniczkowalne w normie operatorowej i
\[
\sup_{0\le t\le T}\|M'(t)\|
\le K_G\ell e^{T\ell}=:L_*.
\tag{F}
\]

**Twierdzenie C (skończony certyfikat trajektorii przy kontrolowanej szybkości).**
Niech węzły \(0=t_0<t_1<\dots<t_N=T\) mają maksymalny odstęp \(h\). Jeśli uzyskano wiarygodne oszacowania **norm operatorów**
\(\|M(t_j)\|\le \varepsilon\) dla wszystkich \(j\), to
\[
\sup_{0\le t\le T}\|M(t)\|
\le \varepsilon+\tfrac12 h L_*=:\delta_{\rm grid},
\tag{G}
\]
\[
\left\|\int_0^T M(t)^*M(t)\,dt\right\|^{1/2}
\le \sqrt{T}\,\delta_{\rm grid},
\tag{H}
\]
oraz dla przygotowanego \(y_0=0\)
\[
\|G P S(T)J_Xx_0-G e^{TA}x_0\|
\le \delta_{\rm grid}\,\|C\|\int_0^T\|e^{sA}x_0\|\,ds.
\tag{I}
\]
Dla skalarnej obserwabli \(G\) i ukrytego przygotowania \(\|y_0\|\le R\), ryzyko surowego modelu bez pamięci jest dodatkowo ograniczone przez prawą stronę (I) powiększoną o \(R\varepsilon\), ponieważ \(T\) jest próbkowanym węzłem.

*Dowód.* Wzór \(M'(t)=GP\mathcal L e^{t\mathcal L}J_Y\) i \(\|e^{t\mathcal L}\|\le e^{t\ell}\) dają (F). Każdy \(t\in[0,T]\) jest odległy od pewnego węzła \(t_j\) o co najwyżej \(h/2\). Twierdzenie o wartości średniej w normie operatorowej daje
\(\|M(t)\|\le\|M(t_j)\|+L_*|t-t_j|\le\delta_{\rm grid}\).
Stąd (H) przez oszacowanie kwadratowej całki, a (I) przez dokładny wzór (B). Ostatni wniosek wynika ze skalarnej równości (E) i \(\|M(T)\|\le\varepsilon\). \(\square\)

**Zakres.** Twierdzenie C NIE mówi, że skończone testy dokładnie zerowych wartości bez znajomości generatora potwierdzają zerowanie całego \(M(t)\). Daje certyfikat **przy znanej normowej stałej szybkości** i kontroli pełnych operatorów \(M(t_j)\), a nie jednego wyniku pomiarowego na nieznanym \(y_0\). Dla ogólnych generatorów \(C_0\) operatorowa pochodna może nie istnieć; wtedy należy osobno wykazać odpowiedni moduł ciągłości na klasie badanych danych. W szczególności nie narusza to kontrprzykładu translacyjnego z rozdziału I, gdzie wszystkie pochodne w zerze mogą znikać mimo późniejszej niezerowej pamięci.
