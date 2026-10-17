# Wierność celu przy nieznanym sektorze ukrytym

## Problem i typ matematyczny

Niech \(H=X\oplus Y\) będzie przestrzenią Hilberta, \(\mathcal L\in\mathcal B(H)\) ograniczonym generatorem, \(P:H\to X\) projekcją i \(J_X,J_Y\) kanonicznymi włożeniami. Znany jest początkowy stan \(x_0\in X\), a ukryty \(y_0\in Y\) należy do kuli \(\|y_0\|\le R\). Celem jest tylko \(z(T)=Gx(T)\in Z\), gdzie \(G\in\mathcal B(X,Z)\), \(Z\) — Hilbert.

Zdefiniujmy
\[
K_T=GP e^{T\mathcal L}J_X,\qquad M_T=GP e^{T\mathcal L}J_Y.
\tag{1}
\]
Wówczas \(z(T)=K_Tx_0+M_Ty_0\). **Nieznany początkowy sektor \(y_0\)** nie jest tym samym problemem co pamięć \(Be^{tD}C\) w redukcji z dokładnie przygotowanym \(y_0=0\).

## Twierdzenie 1 — dokładny minimaksowy błąd celu

Dla każdego ustalonego \(x_0\) mamy
\[
\inf_{a(x_0)\in Z}\sup_{\|y_0\|\le R}
\|K_Tx_0+M_Ty_0-a(x_0)\|
=R\|M_T\|.
\tag{2}
\]
Optymalnym estymatorem jest \(a_*(x_0)=K_Tx_0\). Dokładna identyfikowalność celu z samego \(x_0\) dla wszystkich dopuszczalnych \(y_0\) zachodzi wtedy i tylko wtedy, gdy \(M_T=0\).

**Dowód.** Wybór \(a_*\) daje górną granicę \(R\|M_T\|\). Dla każdego innego estymatora połóżmy \(c=a(x_0)-K_Tx_0\). Ponieważ kula ukrytych przygotowań zawiera równocześnie \(y\) i \(-y\), nierówność trójkąta daje
\[
2\|M_Ty\|\le\|M_Ty-c\|+\|-M_Ty-c\|.
\]
Jeden z obu błędów ma normę co najmniej \(\|M_Ty\|\). Biorąc supremum po \(\|y\|\le R\), otrzymujemy dolne ograniczenie \(R\|M_T\|\). \(\square\)

Dla elipsoidalnego ograniczenia \(y_0=\bar y+Qv,\ \|v\|\le R\) wynik brzmi \(R\|M_TQ\|\), a estymatorem centralnym jest \(K_Tx_0+M_T\bar y\).

## Twierdzenie 2 — rząd pojawienia się wpływu ukrytego sektora

Połóżmy \(M_k=GP\mathcal L^kJ_Y\), \(k\ge0\). Mamy \(M_0=0\). Jeśli \(m\ge1\) jest najmniejszą liczbą całkowitą z \(M_m\ne0\), to
\[
M_T=\frac{T^m}{m!}M_m+O_{\mathcal B(Y,Z)}(T^{m+1}),\quad
\lim_{T\downarrow0}\frac{R\|M_T\|}{T^m}=\frac{R\|M_m\|}{m!}.
\tag{3}
\]
Jeżeli wszystkie \(M_k=0\), wtedy \(M_T=0\) dla każdego \(T\). Gdy \(\dim H=n<\infty\), wystarczy sprawdzić \(M_0,\ldots,M_{n-1}\).

**Dowód.** Szereg \(e^{T\mathcal L}=\sum_{k\ge0}T^k\mathcal L^k/k!\) zbiega w normie operatorowej. Po przemnożeniu przez \(GP,J_Y\) daje rozwinięcie i resztę w (3). Ciągłość normy operatorowej daje asymptotykę błędu minimaksowego z (2). W skończonym wymiarze twierdzenie Cayleya–Hamiltona wyraża wyższe potęgi przez pierwsze \(n\), co dowodzi ostatniej tezy. \(\square\)

**Granica:** kryterium momentowe nie przechodzi automatycznie na dowolny nieograniczony generator \(C_0\). Dla niego nie musi zachodzić analityczność w normie. To odrębna kwestia od twierdzenia o pojedynczym mnożniku spektralnym w rozdziale VII.

## Twierdzenie 3 — pełna historia i gramian obserwowalności celu

Jeśli \(Z\) jest Hilbertem, oznaczmy przez
\[
\mathscr M_T:Y\to L^2(0,T;Z),\qquad
(\mathscr M_T y)(t)=M_ty
\]
operator wpływu ukrytego stanu na całą historię obserwabli. Niech
\(\mathcal W_T=\int_0^T M_t^*M_t\,dt\); całka jest w normie operatorowej, a \(\mathcal W_T\ge0\).
Wówczas
\[
E_{\mathrm{hist}}(T)=R\|\mathscr M_T\|
=R\sqrt{\|\mathcal W_T\|}. \tag{4}
\]
Jeśli pierwszy niezerowy \(M_m\) występuje w rzędzie \(m\), to
\[
\lim_{T\downarrow0}\frac{E_{\mathrm{hist}}(T)}{T^{m+1/2}}
=\frac{R\|M_m\|}{m!\sqrt{2m+1}}. \tag{5}
\]

**Dowód.** Symetryczny argument z twierdzenia 1 działa również dla normy \(L^2\). Wykorzystując iloczyn skalarny Hilberta, mamy
\[
\|\mathscr M_T y\|_{L^2}^2=\int_0^T\langle M_t y,M_t y\rangle\,dt
=\langle y,\mathcal W_T y\rangle.
\]
Zatem \(\|\mathscr M_T\|^2=\|\mathcal W_T\|\). Rozwinięcie \(M_t=t^mM_m/m!+O(t^{m+1})\), równomierne na \([0,T]\), daje w normie operatorowej
\[
\mathcal W_T=
\frac{T^{2m+1}}{(m!)^2(2m+1)}M_m^*M_m+O(T^{2m+2}).
\]
Po wzięciu normy i pierwiastka otrzymujemy (5). \(\square\)

Dla każdej chwili \(T\) niewidoczność tylko w końcowym wyjściu oznacza \(M_T=0\). Całkowita niewidoczność na przedziale \([0,T]\) oznacza \(\mathcal W_T=0\), czyli \(M_t=0\) dla wszystkich \(t\in[0,T]\) (dzięki ciągłości). Nie są to równoważne kryteria.

## Twierdzenie 4 — odporność wniosku na perturbację generatora

Niech \(\mathcal L,\widetilde{\mathcal L}\in\mathcal B(H)\), a \(a=\max(\|\mathcal L\|,\|\widetilde{\mathcal L}\|)\). Przy stałych mapach \(P,G,J_Y\):
\[
\Big|\|GP e^{T\mathcal L}J_Y\|-\|GP e^{T\widetilde{\mathcal L}}J_Y\|\Big|
\le\|GP\|\,\|J_Y\|\,T e^{Ta}\|\mathcal L-\widetilde{\mathcal L}\|. \tag{6}
\]
Pomnożenie przez \(R\) ogranicza zmianę dokładnego błędu minimaksowego.

**Dowód.** Stosujemy tożsamość Duhamela
\[
e^{T\mathcal L}-e^{T\widetilde{\mathcal L}}
=\int_0^T e^{(T-s)\mathcal L}(\mathcal L-\widetilde{\mathcal L})e^{s\widetilde{\mathcal L}}ds,
\]
oszacowanie \(\|e^{t\mathcal L}\|\le e^{t\|\mathcal L\|}\) oraz nierówność odwrotną dla norm operatorowych
\(|\|S\|-\|T\||\le\|S-T\|\). \(\square\)

## Ścisły most z równaniem sprzężonym

Adjungowany operator
\[
M_T^*=J_Y^*e^{T\mathcal L^*}P^*G^*
\tag{7}
\]
przenosi dualny wektor celu do kierunku ukrytego przygotowania. To bezpośrednia, poprawnie typowana realizacja rachunku wrażliwości z rozdziału VI: „najgroźniejszy” ukryty stan leży w kierunku maksymalizującym normę \(M_T\), a dla jednowymiarowego \(Z\) w kierunku \(M_T^*1\) (o ile ten wektor jest niezerowy). W nieskończonym wymiarze normowy maksymalizator może nie istnieć; supremum z twierdzenia 1 nie zakłada jego osiągania.

## Przykład A. Opóźniona widzialność sektora ukrytego

Weźmy \(\dot u=v,\ \dot v=h,\ \dot h=0\), z zachowanym stanem \(x=(u,v)\), ukrytym \(y=h\) oraz celem \(u(T)\). Generator ma \(\mathcal L^3=0\), a \(M_0=M_1=0\), \(M_2=1\). Dlatego
\[
u(T)=u_0+Tv_0+\frac{T^2}{2}h_0.
\]
Dla \(|h_0|\le R\) dokładny błąd końcowej prognozy to \(RT^2/2\), a błąd całej historii w \(L^2(0,T)\) to \(RT^{5/2}/\sqrt{20}\). Przy \(R=1,T=0.4\): odpowiednio \(0.08\) oraz \(0.0226274169979695\). Ukryty sektor nie ma wpływu na wartość ani na pierwszą pochodną celu w chwili początkowej, lecz pojawia się w drugiej pochodnej.

## Przykład B. Pełna dokładność punktowa i błąd całej historii

Dla oscylatora \(\dot x=y,\ \dot y=-x\), znanego \(x_0\), nieznanego \(|y_0|\le R\) i wyjścia \(x(t)\) otrzymujemy \(M_t=\sin t\). Przy \(T=\pi\):
\[
E_{\rm end}(\pi)=0,\qquad
E_{\rm hist}(\pi)=R\sqrt{\int_0^\pi\sin^2t\,dt}
=R\sqrt{\pi/2}>0.
\]
Identyfikowalność końcowej obserwabli nie implikuje identyfikowalności trajektorii. Nie jest to kontrprzykład dla Kalmana, którego warunek obserwowalności dotyczy pełnej historii odczytów.
