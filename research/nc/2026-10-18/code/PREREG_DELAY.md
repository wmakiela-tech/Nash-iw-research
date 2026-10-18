# PREREJESTRACJA — falsyfikator momentowy w klasie nieograniczonej (NC, 2026-10-18)

Zapisane PRZED uruchomieniem kodu. Cel: uniemożliwić dopasowanie odczytu do wyniku.

## Konstrukcja (analityczna, dokładna)
X = Y = L^2(0,1). A = D = d/dxi, dziedzina {f in H^1 : f(1)=0} — generator nilpotentnej
poolgrupy lewych przesunieć (S(t)f)(xi)=f(xi+t), S(t)=0 dla t>=1. NIEOGRANICZONY, C_0.
G f = <f,g>, g = bump na [0,eps].        G w B(X,C), ||G|| = ||g||
B y = <y,u> beta, beta = bump na [1-eps,1] w X, u = bump na [0,eps] w Y.   B w B(Y,X)
C x = <x,v> gamma, gamma = bump na [1-eps,1] w Y, v = bump na [0,eps] w X.  C w B(X,Y)
Wszystkie bumpy >= 0, C_c^inf w otwartych przedzialach, wiec w D(A^k), D(D^k) dla kazdego k.

## P1 (dowod analityczny: rozlaczne nosniki)
Wszystkie momenty widzialnosci M_k = G P L^k J_Y znikaja, bo kazda sciezka z Y do X konczy
sie A^j B, a G A^j beta = int g beta^{(j)} = 0 przy supp g = [0,eps] rozlacznym z supp beta.
Wszystkie momenty pamieci B D^k C = <.,v> <D^k gamma, u> beta = 0 z tego samego powodu.
PRZEWIDYWANIE NUMERYCZNE: w dyskretyzacji N komorek pierwszy niezerowy moment
wystepuje przy m_N = (liczba komorek odleglosci nosnikow), czyli m_N ~ N*t_0, gdzie
t_0 = dist(supp g, supp beta). Zatem m_N -> inf i staly R||M_m||/m! z Tw. 2 degeneruje.

## P2
||K(t)|| = 0 dla t < t_0 i > 0 dla t > t_0 (t_0 = odleglosc nosnikow), przy wszystkich
momentach zerowych. Onset = czas transportu.

## P3 (ostrosc)
max_t ||K(t)|| = ||B|| ||C|| — gorne ograniczenie ||B|| ||S_D(t)|| ||C|| jest OSIAGANE
(rownosc Cauchy-Schwarza, gdy przesuniete gamma pokrywa sie z u). Czyli: zerowanie
WSZYSTKICH momentow nie daje ZADNEJ informacji o rozmiarze pamieci w klasie nieograniczonej.
PRZEWIDYWANIE: iloraz max_t ||K(t)|| / (||B|| ||C||) -> 1 przy N -> inf.

## P4 (kontrola wlasna — moze wyjsc FALSE)
Tozsamosc A LT4 (wzor B: q(t,x0) = int_0^t M(t-s) C S_A(s) x0 ds) zachodzi w tej samej
dyskretyzacji z bledem rzedu dyskretyzacji. Jesli nie — defekt jest u mnie albo u LT4.

## P5 (kontrola wlasna)
Dla celu skalarnego: E_hist(T)^2 = R^2 lambda_max(W_T) oraz int_0^T E_end(t)^2 dt
= R^2 tr(W_T). Zatem E_hist(T) <= sqrt(int E_end^2) <= sqrt(r) E_hist(T), r = rank W_T.
Rownosc po lewej WTEDY I TYLKO WTEDY, gdy najgorszy kierunek ukryty nie obraca sie w czasie.
PRZEWIDYWANIE: prawa nierownosc jest ostra — istnieje uklad z ilorazem dazacym do sqrt(r).

## Zakazy
Nie wolno: podnosic statusu bez EXEC_SIGN; twierdzic nowosci matematycznej (mechanizm
nilpotentnej poolgrupy przesunieć jest material gospodarza — Engel-Nagel); pisac tekstu
interpretacyjnego w print (regula z 12 X).
