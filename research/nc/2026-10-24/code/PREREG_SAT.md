# PREREG — NC-OPN-010: czy przy lambda>0 i ubytku zaleznym od stanu istnieje NOWY przypadek zdegenerowany

**Data:** 2026-10-24. **Autor:** NC, rola Badacz. **Wiersz:** `NC-OPN-010` (2026-10-23).
Preregestracja zapisana PRZED uruchomieniem kodu. Status wyjsciowy wiersza: *"W badanej rodzinie
(trzy impulsy, Gamma=gamma0(1+beta n)n) nie znalazlem. 'Nie znalazlem' nie znaczy 'nie istnieje'
— rodzina byla jedna i trzypunktowa."*

## Model

```
n' = S(t) - Gamma(n),      n(0) = n0
X' = -lambda X + kappa Gamma(n),   X(0) = 0
X(T) = kappa * int_0^T e^{-lambda(T-t)} Gamma(n(t)) dt
```

Bilans masy: `int_0^T Gamma(n) = int_0^T S - [n(T) - n0]`.

Klasyfikacja MT13 (Tw. o rownych plonach) orzeka rownosc `X(T)` przy rownych `int S` i `n(T)`
**wtedy i tylko wtedy, gdy `w in span{1,q}`** — czyli warunek na **wage**. REC10 ROT21 doprecyzowal
wersje z niestalymi wspolczynnikami.

## Hipoteza (H-SAT)

Istnieje mechanizm degeneracji **nieobjety** klasyfikacja na wadze, bo dziala przez **zawezenie
zbioru dopuszczalnego**, nie przez wage. Jesli kinetyka jest **nasycona** na calym osiaganym
zakresie `n`, tj. `Gamma(n(t)) = Gamma_0` stale dla `t in [0,T]`, to bilans masy ustala nie tylko
calke `int Gamma`, lecz **caly profil**: `Gamma_0 = (int S - Delta n)/T`. Wtedy

```
X(T) = kappa * Gamma_0 * (1 - e^{-lambda T}) / lambda
```

jest wspolne dla **kazdego** `lambda > 0`, mimo ze waga `e^{-lambda(T-t)}` NIE jest stala i
`w` NIE lezy w `span{1,q}`.

Jesli H-SAT sie potwierdzi, odpowiedz na `NC-OPN-010` jest **TAK**, a klasyfikacja MT13 jest
kompletna tylko przy ustalonym zbiorze dopuszczalnych profili — czego jej sformulowanie nie mowi.

## Falsyfikatory — kolejnosc obowiazujaca

**F1 (KONTROLA, PIERWSZA).** Przy `lambda > 0` i `Gamma(n) = gamma n` (liniowe, NIEnasycone) dwa
zrodla o rownych `int S` i rownym `n(T)` musza dac **ROZNE** `X(T)`. Jesli dadza rowne, to moj
uklad testowy albo integrator jest zly i **wstrzymuje wszystkie wnioski** — bo MT13 orzeka, ze
przy `lambda > 0` rownosc nie zachodzi.

**F2.** Przy nasyceniu (`n(t) >= n_s` przez cale `[0,T]`, `Gamma` dokladnie stale na `[n_s, inf)`)
dwa takie zrodla musza dac `X(T)` **ROWNE** do tolerancji integratora (`< 1e-10` relatywnie).
Jesli nie — H-SAT pada.

**F3 (ANTY-ARTEFAKT).** Zrodlo, przy ktorym `n` **wychodzi** ponizej `n_s`, musi dac `X(T)`
**ROZNE** od przypadku nasyconego. Jesli i tu wyjdzie rowne, zgodnosc z F2 nie pochodzi z
nasycenia, lecz z tego, ze moje zrodla sa zbyt podobne — i H-SAT nie jest wykazana.

**F4.** Zgodnosc z F2 musi zachodzic dla **kilku** `lambda > 0` (0.1, 0.5, 1, 3), a wspolna wartosc
musi zgadzac sie z postacia zamknieta `kappa*Gamma_0*(1-e^{-lambda T})/lambda` do `< 1e-10`.
Zgodnosc liczb bez zgodnosci z postacia zamknieta = nie rozumiem, co licze.

**F5.** Bilans masy `int Gamma = int S - Delta n` musi zachodzic do tolerancji integratora w
KAZDYM przebiegu. To kontrola samego integratora, niezalezna od hipotezy.

**F6.** Zrodla musza byc `C^1` (podniesiony cosinus). Zrodla prostokatne daja artefakt kwadratury
`O(h)` — udokumentowany blad wlasny z ART018 par.4b. Sprawdzam zbieznosc przy zageszczaniu siatki.

## Czego ten test NIE rozstrzygnie

- Nie rozstrzygnie, czy nasycenie jest **jedynym** takim mechanizmem.
- Nie rozstrzygnie nic o przypadku, w ktorym `n` dotyka `n_s` stycznie.
- Wszystko numeryczne, `P_SIMULATED`, bez EXEC_SIGN.
- Czesc analityczna (postac zamknieta) jest trywialna PO przyjeciu `Gamma = Gamma_0`; cala
  zawartosc hipotezy lezy w tym, ze bilans masy **wymusza** `Gamma_0`, a nie w rachunku calki.

## Odejmowanie stanu wiedzy — do wykonania PRZED zlozeniem

Nasycona kinetyka zerowego rzedu (`Gamma` niezalezne od `n` powyzej progu) to **kinetyka
Michaelisa-Menten w rezimie nasycenia** — material dojrzaly i z pewnoscia cudzy. Przed zlozeniem
sprawdzam, czy wniosek o **niezaleznosci plonu wazonego od profilu zrodla przy kinetyce zerowego
rzedu** jest juz w literaturze farmakokinetycznej / reaktorowej (AUC przy zerowym rzedzie).
Jesli tak — zglaszam wylacznie, ze **nasza** klasyfikacja tego nie obejmuje, bez claimu nowosci.
