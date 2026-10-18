# PREREJESTRACJA — atak na Twierdzenie 1 z ART009 przez zmianę modelu szumu

ZAPISANE I ZAHASZOWANE PRZED URUCHOMIENIEM `l2.py`.

## 0. Co jest atakowane

ART009 (sha256 577617b58c05bed8a0aa34323a9e0378bdd30b8f312bf83368bea309f597630e,
commit 2058fd3) Twierdzenie 1: przy reakcji zwrotnej o sile `gamma` zaden protokol
pomiarowy nie osiaga `M >= 1/gamma`, gdzie `M = max_j |c_j|`, `c_j = y(t_j) sigma(s_j)`.

W ART009 par. 5 punkt 4 zapisalem WLASNA PREDYKCJE:

> "Figura zaslugi max_j opiera sie na Tw. 7.10 monografii (adwersarialny szum
> z osobnym budzetem na pomiar). Przy innym modelu szumu — niezaleznym losowym,
> albo ze wspolnym budzetem normy — figura bylaby inna i CALE TWIERDZENIE 1
> MOGLOBY UPASC, bo usrednianie zaczeloby dzialac."

To jest predykcja do rozstrzygniecia. **Przewidywalem, ze sufit upadnie.**

## 1. Dlaczego figura zaslugi sie zmienia

Model obserwacji jest liniowy w ukrytym `y0`:  `b_j = y0 c_j + eta_j`.

- szum adwersarialny per pomiar, `|eta_j| <= delta`: wiaze najostrzejsze ograniczenie,
  figura = `||c||_inf`;
- szum niezalezny gaussowski `eta_j ~ N(0, delta^2)`: informacja Fishera o `y0` wynosi
  `sum_j c_j^2 / delta^2`, odchylenie estymatora `delta / ||c||_2`, figura = `||c||_2`;
- szum adwersarialny ze WSPOLNYM budzetem `||eta||_2 <= delta`: zbior zgodnych `y0` ma
  promien `delta / ||c||_2`, figura = `||c||_2`.

Dwa ostatnie modele daja te sama figure. Dla `k` pomiarow o rownym wzmocnieniu
`||c||_2 = sqrt(k) ||c||_inf`, wiec usrednianie MOZE kupic czynnik `sqrt(k)` —
i dokladnie dlatego przewidywalem upadek sufitu.

## 2. Wyprowadzenie zrobione przed kodem (do sprawdzenia numerycznie)

Oznaczenia: stan przed pomiarem `j` to `(x_j, y_j)`, amplituda `A_j^2 = x_j^2 + y_j^2`;
`u_j = e^{-gamma s_j} w (0,1]`; `sigma(s_j) = (1-u_j)/gamma`. Pomiar mnozy `y` przez `u_j`,
nie rusza `x`. Ewolucja swobodna zachowuje `A^2`.

    A_{j+1}^2 = x_j^2 + y_j^2 u_j^2 = A_j^2 - y_j^2 (1 - u_j^2)

    (gamma c_j)^2 = y_j^2 (1-u_j)^2 = [A_j^2 - A_{j+1}^2] * (1-u_j)/(1+u_j)

a poniewaz `(1-u)/(1+u) <= 1` na `u w [0,1]`:

    (gamma c_j)^2 <= A_j^2 - A_{j+1}^2          (*)   TERMWISE
    gamma^2 ||c||_2^2 <= A_1^2 - A_{k+1}^2 <= 1  (**)  PO ZSUMOWANIU

czyli `||c||_2 <= 1/gamma`. **TEN SAM SUFIT.** Rownosc wymaga `u_j -> 0` (pomiar
nieskonczenie silny), co wymusza `k = 1`.

Mechanizm: kwadrat wzmocnienia jest zawsze mniejszy od ubytku kwadratu amplitudy, wiec
informacja Fishera jest placona z ZACHOWANEGO budzetu. Zysk `sqrt(k)` z usredniania
jest dokladnie zjadany przez koszt amplitudowy wielu pomiarow.

## 3. Predykcje do testu (rozstrzygaja miedzy par. 1 a par. 2)

- **P1.** `gamma ||c||_2 <= 1` dla KAZDEGO protokolu. Skan losowy nie znajdzie naruszenia.
  Jesli znajdzie — wyprowadzenie (**) jest falszywe i sufit upada zgodnie z ART009 par.5.4.
- **P2.** Nierownosc termwise (*) zachodzi dla kazdego pomiaru osobno.
- **P3.** Optimum `||c||_2` osiaga sie przy `k = 1`, silnym pomiarze w antywezle predkosci.
  Wiele slabych pomiarow NIE bije jednego silnego.
- **P4.** `sup gamma ||c||_2 = 1` jest wysycane: skan dojdzie do 1 z dokladnoscia skanu.
- **P5.** Podloga bledu znormalizowanego `delta/(R ||c||_2) >= gamma delta / R` — ta sama
  co w ART009, mimo innej figury zaslugi.
- **P6 (osobne, o Tw. 2 z ART009).** W oknie wokol czasu slepego pomiar ofiarny dawal
  zysk 1.9x w normie `inf`. Przy figurze `||c||_2` przewiduje zysk **WIEKSZY niz 1.9x**,
  bo oba pomiary wnosza do sumy kwadratow, a w normie `inf` liczyl sie tylko drugi.

## 4. Czego ten test nie rozstrzyga

Model pozostaje ten sam co ART008/009: oscylator, skalarny stan ukryty, fenomenologiczna
reakcja zwrotna "pomiar predkosci tlumi predkosc". Wersja kwantowa to inne zadanie.
`COMMON MATHEMATICS != COMMON PHYSICAL MECHANISM`. Nie szukalem literatury; nie twierdze
nowosci. Status wyniku: `[▷]`, EXEC_SIGN brak, audyt zewnetrzny obowiazkowy.
