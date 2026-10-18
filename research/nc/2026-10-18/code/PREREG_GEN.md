# PREREJESTRACJA — uogolnienie ksiegowania na dowolny generator

ZAPISANE I ZAHASZOWANE PRZED URUCHOMIENIEM `gen.py`.
Poprzedza: ART010 (GitHub commit 1e5f6c3, Drive 1p9sB1Q3x0D41vZk3RSEhwuUOy0nCk7aX),
`PREREG_ALIGN.md` 1c075b7afe970e4b3e246b63f655608c4a522348761359b72ad4cc3a755491ad.

## 0. Co jest otwarte

ART010 par. 6 punkt 2: "Dla ogolnego generatora sufit zalezalby od istnienia wielkosci
nierosnacej pelniacej role A^2; NIE ZBADALEM, kiedy taka istnieje — i to jest wlasciwe
pytanie uogolniajace." Podejmuje je.

## 1. Model

`v' = G v` zamiast oscylatora. Czujnik: czyta `(v . e)` z `sigma(s)`, tlumi skladowa
wzdluz tego samego `e` przez `u = e^{-gamma s}` (wspolosiowosc, `phi = 0`, bo przypadek
`phi != 0` jest juz rozstrzygniety w ART010 par. 3).

W oscylatorze dzialaly trzy fakty: ewolucja swobodna zachowywala `|v|^2`; pomiar obnizal
`|v|^2` o `(v.e)^2(1-u^2)`; wzmocnienie wynosilo `(v.e)(1-u)`. Dla ogolnego `G` pierwszy
fakt wymaga **certyfikatu Lapunowa**: `P > 0` z `G^T P + P G <= 0`, czyli `mu_P(G) <= 0`
— logarytmiczna norma w metryce `P` niedodatnia. To jest dokladnie wielkosc, o ktora
rozbil sie moj wniosek z 2026-10-17: kontrprzykad M13 (`A = [[-11/10,4],[1,-41/10]]`,
`mu_2 = +0.3155 > 0` mimo malejacej masy) pokazal, ze `P = I` bywa zlym wyborem,
a wazona dziala — zmierzylem tam `cond(W) = 2`.

## 2. Wyprowadzenie zrobione przed kodem

`Q(v) = v^T P v`. Pomiar: `v -> v - (1-u)(v.e) e`. Niech `p = e^T P e`, `m = e^T P v`.

    dQ = 2 (gamma c) m - (gamma c)^2 p,     gdzie gamma c = (v.e)(1-u)

Czlon liniowy w `gamma c` ma znak `m`, wiec **pomiar moze podniesc Q**. Kluczowy warunek:

**`e` jest wektorem wlasnym `P`**, `P e = p e`. Wtedy `m = p (v.e)` i wszystko sie sklada:

    (gamma c_j)^2 = dQ_j * tanh(gamma s_j / 2) / p
    gamma^2 ||c||_2^2 <= Q(v_0) / p <= lambda_max(P) / p

czyli przy `|v_0| = 1`

    gamma ||c||_2  <=  sqrt( lambda_max(P) / (e^T P e) )  <=  sqrt( cond(P) )

Przy `P = I` (G skosnie symetryczne) to jest dokladnie sufit `1` z ART010.

## 3. Predykcje

- **G1.** Przy `P e = p e` nierownosc `gamma||c||_2 <= sqrt(lambda_max(P)/p)` zachodzi dla
  kazdego protokolu. Skan losowy po `G`, czasach i silach nie znajdzie naruszenia.
- **G2.** Tozsamosc `(gamma c_j)^2 = dQ_j tanh(gamma s_j/2)/p` zachodzi **termwise**,
  do precyzji maszynowej, przy `P e = p e`.
- **G3.** Sufit jest **ciasny** dla par `(G, e)` obserwowalnych — skan dojdzie do
  `sqrt(lambda_max(P)/p)`. Dla nieobserwowalnych bedzie ostro nizej.
- **G4.** Gdy `e` NIE jest wektorem wlasnym `P`, sufit **znika**, nie degraduje sie.
  Mechanizm przewidywany: mozna dobrac stan z `m` przeciwnego znaku do `(v.e)`, wtedy
  `dQ < 0` i pomiar **podnosi** `Q`. To jest pompa, a nie koszt. Przyklad do sprawdzenia:
  `P = [[1,0.9],[0.9,1]]`, `v = (1,-1)`, `Q = 0.2`; wytlumienie pierwszej wspolrzednej
  do zera daje `v' = (0,-1)`, `Q = 1`. Wzrost pieciokrotny.
  Przewiduje `gamma||c||_2` rosnace z `k` bez kresu, tak jak przy `phi != 0` w ART010.
- **G5.** Gdy certyfikatu NIE MA (`G` ma wartosc wlasna o dodatniej czesci rzeczywistej,
  albo jest defektywny na granicy stabilnosci, np. klatka Jordana `[[0,1],[0,0]]`), sufitu
  nie ma nawet przy jednym pomiarze: sama ewolucja swobodna pompuje `(v.e)`.
- **G6.** Na kontrprzykladzie M13 (`A` wyzej, `cond(W) = 2`) sufit wynosi
  `sqrt(lambda_max(W)/(e^T W e))`, a nie `1`. Dla `e` = wektor wlasny `W` o najwiekszej
  wartosci wlasnej daje to dokladnie `1`; dla tego o najmniejszej — `sqrt(2) = 1.4142`.
  Sprawdzam obie.

## 4. Czego to nie rozstrzyga

Nadal model fenomenologiczny, nadal `phi = 0`, nadal klasyczny. Przypadek kwantowy
(reakcja zwrotna jako **szum** na kwadraturze sprzezonej, nie tlumienie) pozostaje poza
zakresem i nic o nim nie wnosze. `COMMON MATHEMATICS != COMMON PHYSICAL MECHANISM`.
Nie szukalem literatury; `mu_P(G) <= 0` to standardowa nierownosc Lapunowa i spodziewam
sie gospodarzy. `SEARCH FAILURE != NOVELTY`. Status `[▷]`, EXEC_SIGN brak,
audyt zewnetrzny obowiazkowy.
