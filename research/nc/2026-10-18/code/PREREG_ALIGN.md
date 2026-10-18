# PREREJESTRACJA — czy sufit 1/gamma jest o REAKCJI ZWROTNEJ, czy o JEJ WSPOLOSIOWOSCI

ZAPISANE I ZAHASZOWANE PRZED URUCHOMIENIEM `l2c.py`.
Poprzedza: `PREREG_L2.md` sha256 5399acbcf0c908009dbb6cfadca2df82ce42902fca2ce4f843f622ae619fb591,
`l2.py` sha256 205d51c30e47ae036f30290b374202f62fb94443e9f8b21b7309b7585a051464,
`l2b.py` sha256 74e27c701491dc8bd76f44c51db7960cca5760553b92c4729b7add3b8619ced3.

## 0. Skad pytanie

Zmierzona tozsamosc (l2.py L2, 112547 pomiarow, nadmiar < 3.4e-16):

    (gamma c_j)^2 = [A_j^2 - A_{j+1}^2] * tanh(gamma s_j / 2)

bierze sie z tego, ze czujnik TLUMI TE SAMA kwadrature, ktora CZYTA. Oba czlony sa
wtedy proporcjonalne do `y_j^2` i `y_j^2` sie skraca. To zalozenie jest w modelu
ART008/ART009 ukryte i nigdzie go nie testowalem.

## 1. Model uogolniony

Stan `v = (x,y)`, ewolucja swobodna to obrot. Czujnik ma dwa kierunki w plaszczyznie
fazowej, nie jeden:

- kierunek ODCZYTU `e = (sin th, cos th)` — sygnal to `(v . e) * sigma(s)`;
- kierunek REAKCJI ZWROTNEJ `d = (sin(th+phi), cos(th+phi))` — skladowa wzdluz `d`
  mnozy sie przez `u = e^{-gamma s}`, skladowa prostopadla zostaje nietknieta.

`phi` to NIEWSPOLOSIOWOSC. ART008/ART009 to wylacznie `phi = 0`, `th = 0`.

Wtedy `A_{j+1}^2 = A_j^2 - (v.d)^2 (1-u^2)`, a `gamma c_j = (v.e)(1-u)`. Przy `phi = 0`
licznik i mianownik dziela ten sam czynnik i dostajemy tozsamosc. Przy `phi != 0` nie.

## 2. Predykcje

- **A1.** Przy `phi = pi/2` sufit UPADA i `||c||_2` jest NIEOGRANICZONE. Mechanizm:
  mozna mierzyc w chwilach, w ktorych `v . d = 0`, wtedy ubytek amplitudy jest ZEROWY,
  a sygnal `|v . e| = A` jest maksymalny. Swobodna ewolucja zeruje `v . d` dwa razy na
  okres, wiec taki protokol da sie powtarzac w nieskonczonosc. Przewiduje
  `gamma ||c||_2 = sqrt(k) * sigma(s) * gamma` rosnace jak `sqrt(k)` bez kresu.
- **A2.** Przy `phi = 0` sufit `gamma ||c||_2 <= 1` zachodzi dla KAZDEGO `th`, nie tylko
  `th = 0` — bo dowod korzysta tylko z wspolosiowosci, nie z wyboru kwadratury.
- **A3.** Posrednie `phi`: przewiduje monotoniczny wzrost supremum od 1 przy `phi = 0`
  do nieskonczonosci przy `phi -> pi/2`. Zgaduje rozbieznosc typu `1/|cos phi|` i to jest
  zgadniecie, nie wyprowadzenie — sprawdzam je, zeby zobaczyc, czy sie myle.
- **A4.** Przy `phi = pi/2` i ustalonym BUDZECIE calkowitym `S` optymalne `k` NIE jest 1
  (odwrotnie niz w tabeli N4), bo splitowanie nic nie kosztuje.

## 3. Co to by znaczylo, gdyby A1 byla prawdziwa

Twierdzenie 1 z ART009 nie jest twierdzeniem o reakcji zwrotnej. Jest twierdzeniem
o reakcji zwrotnej WSPOLOSIOWEJ z odczytem. Nazwa i sformulowanie w ART009 sa wtedy
za szerokie i trzeba je zwezic. To byloby obalenie zakresu wlasnego wyniku, nie jego
tresci.

## 4. Czego to nie rozstrzyga

`phi = pi/2` z TLUMIENIEM nie jest modelem kwantowym. Kwantowa reakcja zwrotna przy
pomiarze jednej kwadratury to SZUM na sprzezonej, nie tlumienie jej. Szum podnosi
`A^2` zamiast je obnizac i psuje przyszle odczyty innym kanalem. Tego NIE modeluje
i nie bede z tego wnosil o przypadku kwantowym.
`COMMON MATHEMATICS != COMMON PHYSICAL MECHANISM`. Status `[▷]`, EXEC_SIGN brak.
