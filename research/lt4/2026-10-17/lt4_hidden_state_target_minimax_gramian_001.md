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
