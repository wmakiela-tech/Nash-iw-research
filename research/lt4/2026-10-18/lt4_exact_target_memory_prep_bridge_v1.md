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
