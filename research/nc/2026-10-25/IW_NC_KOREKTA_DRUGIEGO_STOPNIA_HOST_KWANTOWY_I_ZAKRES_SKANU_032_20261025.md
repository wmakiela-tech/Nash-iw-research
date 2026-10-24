# IW / NC — KOREKTA DRUGIEGO STOPNIA: wycofanie hosta kwantowego i zakres skanu z 18 X

**Artefakt:** `IW_NC_KOREKTA_DRUGIEGO_STOPNIA_HOST_KWANTOWY_I_ZAKRES_SKANU_032_20261025`
**Rola:** Badacz (autokorekta). **Data:** 2026-10-25. **Autor:** NC.
**Koryguje:** ART029 par. 4 (claim **fizyczny**, wycofany) oraz ART031 par. 3 i par. 5
(korekta byla niepelna). **Nie zmienia** T1, T1a, T2, swiadka geometrycznego, falsyfikacji H-A.

**SUFIT CLAIMU: NO_CANON / NO_EXEC_SIGN / AUDYT ZEWNETRZNY OBOWIAZKOWY.**
Zlozone z wlasnej inicjatywy, przed jakimkolwiek audytem zewnetrznym, w ciagu dwoch godzin
od ART031 — czyli ART031 sam byl niepelnym odejmowaniem wobec wlasnej komorki.

---

## 1. Najpowazniejsze: wycofuje claim fizyczny z ART029 par. 4

ART029 par. 4 orzekl, ze konfiguracja maksymalizujaca (`e` prostopadle do `d`, `u -> 0`) **jest**
znana konfiguracja **back-action evading / QND**, i podal jako dojrzalego hosta eksperyment
optomechaniczny (arXiv:1608.06152v2), cytujac jego zdanie o kwadraturze *"dynamically decoupled
from the measured quadrature"*.

**Moja wlasna preregestracja z 18 X 2026 (`PREREG_ALIGN.md`, par. 4) tego zabrania, z podana
przyczyna:**

> *"`phi = pi/2` z TLUMIENIEM nie jest modelem kwantowym. Kwantowa reakcja zwrotna przy pomiarze
> jednej kwadratury to SZUM na sprzezonej, nie tlumienie jej. Szum podnosi `A^2` zamiast je
> obnizac i psuje przyszle odczyty innym kanalem. Tego NIE modeluje i nie bede z tego wnosil
> o przypadku kwantowym. `COMMON MATHEMATICS != COMMON PHYSICAL MECHANISM`."*

Przyczyna jest merytoryczna, nie formalna. W naszym modelu `D_d(u) = I - (1-u)dd^T` jest
**dyssypacja**: back-action **obniza** `A^2`, i dlatego `d` prostopadle do stanu daje pomiar
"zerokosztowy". W kwantowym BAE back-action to **szum** na sprzezonej kwadraturze: podnosi
wariancje, a nie obniza amplitude. Zbieznosc jest w **algebrze rozdzielenia kierunkow**, nie w
mechanizmie. Dlatego BAE/QND **nie jest hostem** tego wyniku.

**Co wycofuje:** zdanie z ART029 par. 4, ze to *jest* konfiguracja BAE/QND, oraz podanie
arXiv:1608.06152v2 jako dojrzalego hosta.
**Co zostaje:** analogia **strukturalna** — w obu przypadkach kierunek odczytu jest odsprzezony
od kierunku odbierajacego back-action — jawnie oznaczona jako analogia, bez przenoszenia
wnioskow fizycznych w zadna strone.
**Typ claimu:** to byl claim **interpretacyjny/fizyczny**, nie numeryczny. Poprawna liczba
(`sqrt(m)`) nie autoryzowala interpretacji. Zasada projektu zadziala przeciw mnie dokladnie tam,
gdzie jest napisana.

Odwrotny skutek, ktorego nie wolno mi potraktowac jako pocieszenia: skoro BAE nie jest hostem,
to tresc par. 4 **nie jest cudza** — jest **moja z 18 X** (par. 2). Oba ustalenia obowiazuja
jednoczesnie i zadne z nich nie jest dla mnie korzystne.

## 2. `PREREG_ALIGN` preregestrowal strukture dzisiejszych par. 1, 4 i 5

`PREREG_ALIGN.md` (18 X) zawiera:

- **A1** — przy `phi = pi/2` sufit upada i `||c||_2` jest **nieograniczone**; przewidywane
  `sqrt(k)` bez kresu, z mechanizmem (mierzyc gdy `v . d = 0`, ubytek zerowy, sygnal maksymalny).
  **To jest dzisiejszy warunek osiagania T1.**
- **A2** — przy `phi = 0` sufit `gamma||c||_2 <= 1` dla **kazdego** `th`. **To jest dzisiejszy
  test P3** (`1.000000000`).
- **A3** — posrednie `phi`: monotoniczny wzrost od 1 do nieskonczonosci, **ze zgadnieciem**
  `1/|cos phi|`, jawnie oznaczonym jako zgadniecie. **To jest dzisiejsza tabela V5**; zgadniecie
  A3 padlo, a prawdziwa postac `sqrt(k)|sin phi|sigma(s)` jest w `l2d.py` z tego samego dnia.
- **par. 3** — *"Twierdzenie 1 z ART009 nie jest twierdzeniem o reakcji zwrotnej. Jest
  twierdzeniem o reakcji zwrotnej WSPOLOSIOWEJ z odczytem. Nazwa i sformulowanie w ART009 sa
  wtedy za szerokie i trzeba je zwezic."* **To jest dzisiejszy par. 1 i par. 2 ART029** —
  diagnoza, ze F5 pochodzi z tozsamosci waznej tylko przy `e = d`, i ze `NC-OPN-002` byl zle
  postawiony, bo nie ustalal relacji `e`–`d`.

**Konsekwencja dla `NC-FAL-022`: podnosze wage tego bledu.** Zapisalem go jako "preregestrowalem
falsyfikator z tozsamosci bez sprawdzenia jej zakresu". Falszywie lagodnie. Zakres **byl
sprawdzony i zapisany** szesc dni wczesniej, moja wlasna reka, wraz z wnioskiem, ze
sformulowanie trzeba zwezic. Nie przeoczylem dziedziny — **zignorowalem wlasna dokumentacje**.

## 3. `NC-NUM-001`: brak zakresu parametryzacji

Wiersz mowi: *"280000 losowych protokolow, 0 naruszen `gamma||c||_2 <= 1` przy `mu_2 <= 0`;
maksimum 1.000000000"*. Sprawdzone w kodzie: `l2.py` nie zawiera `phi` **ani razu**, a dynamika to

```python
c.append(y*(1.0-u)/gam)   # odczyt skladowej y
y = y*u                   # tlumienie skladowej y
```

Odczyt i back-action po **tej samej osi** — `e = d` jest zahardkodowane, nie losowane. Ewolucja
swobodna jest obrotem, czyli **jeden** generator z `mu_2 = 0`. Zatem "280000 losowych protokolow"
to losowania **czasow i sil** przy `e = d` na jednym generatorze.

Wiersz czyta sie jako poparcie sufitu `1` **w modelu**. W modelu ze swobodnymi `(e,d)` sufit
wynosi `sqrt(m)`, co pokazuje `l2d.py` **w tym samym katalogu z tego samego dnia**. Maksimum
**dokladnie** `1.000000000` z 280 tysiecy losowan nie jest podpisem granicy — jest podpisem
zawezonej parametryzacji.

**Nie wycofuje liczby** (jest poprawna i rowna dzisiejszemu P3). Dopisuje **zakres**: wynik
dotyczy przypadku wspolosiowego na jednym generatorze, nie modelu.

Rodzina: `NC-FAL-018` (maksimum z przeszukiwania podane tam, gdzie pytano o kres), z dodatkiem —
tu **parametryzacja z konstrukcji wykluczala** konfiguracje naruszajaca, a kod, ktory ja
znajdowal, lezal obok.

`NC-NUM-003` sprawdzone tym samym trybem: `gen4.py` tez nie ma `phi`, czyli "lamie sufit w 12/12
generatorow z `mu_2 > 0`" uzyskano **przy `e = d`**. To wiersz **mocniejszy**, niz mu
przypisywalem, i spojny z dzisiejszym V5 (przy silnym `mu_2 > 0` kat nie rzadzi). Bez korekty.

## 4. ART031 byl niepelny — i to obala regule, ktora w nim zaproponowalem

ART031 par. 5 proponowal: preregestracja niekompletna, dopoki nie zawiera wyniku przejscia po
**`CLAIM_ROWS_NC`**. Niewystarczajace, co pokazalem **sam, w ciagu dwoch godzin**: przeszedlem po
rejestrze i nadal przeoczylem `PREREG_ALIGN.md` oraz `l2.py`/`l2d.py`, czyli najwazniejsza czesc —
w tym caveat, ktory zakazywal claimu fizycznego.

**Poprawiona propozycja (`NC-OPN-027`, wersja 2).** Przejscie po wlasnym dorobku obejmuje trzy
powierzchnie, nie jedna: (a) `CLAIM_ROWS_NC`, (b) **wszystkie wlasne preregestracje**,
(c) **katalog kodu** z dat, w ktorych pracowalem nad ta sama wielkoscia. Wynik — trafienia albo
jawne "brak trafien" **per powierzchnia** — wpisany przed uruchomieniem kodu. Egzekwowalne z
zewnatrz: pliki sa publiczne, brak sekcji widac bez pytania mnie o cokolwiek.

`origin_failure_mode: PATCHED_A_PRIOR_ART_RULE_WITH_THE_NARROWEST_SURFACE_THAT_WOULD_HAVE_CAUGHT_THE_LAST_MISS`
— ta sama wada co poprawka KROK 0 po ART018: poprawka skrojona do ostatniego objawu, nie do
mechanizmu. **Dwa razy z rzedu.** To jest wlasciwy wzorzec do zapisania, nie pojedyncze pominiecia.

## 5. Co po trzech korektach zostaje z ART029 jako nowe

1. **T1** jako nierownosc dla kazdego `G` z `mu_2 <= 0` (wiersze z 18 X: jeden generator,
   `e = d` albo brak przeplywu; T1 obejmuje dowolny przeplyw kontraktujacy, przez Dahlquista).
2. **T1a** — warunek osiagania, izometria kontra przeplyw scisle kontraktujacy, deficyt liniowy
   w szerokosci okna. `A1` przewidywalo nieograniczonosc, nie warunek osiagania.
3. **Rezim `mu_2 > 0`: tempo i mechanizm** — redukcja rangi 1, `rho = w^T e^{G*Delta} w`, dowod
   progu T2, jawny swiadek geometryczny, falsyfikacja H-A. `NC-NUM-003` dawal **fakt lamania**
   przy `e = d`, bez tempa i mechanizmu.

Nowe **nie** sa: par. 4 w calosci (moje z 18 X, a przy tym z wycofanym hostem kwantowym),
prawo kata z par. 5 (`NC-ALG-005`, `A3`), prog empiryczny (`NC-NUM-003`), diagnoza zakresu
tozsamosci z par. 1–2 (`PREREG_ALIGN` par. 3).

## 6. Czego NIE robie

- Nie zmieniam zadnej liczby w ART029, ART030 ani ART031.
- Nie wycofuje `NC-NUM-001` ani `NC-NUM-003` — dopisuje zakres do pierwszego.
- Nie twierdze, ze analogia strukturalna do BAE jest bezwartosciowa; twierdze, ze **nie jest
  hostem** i nie uprawnia wnioskow fizycznych.
- Nie podnosze ani nie obnizam statusu zadnego wiersza; `CLOSED` nadaje Moderator.
- Nie przyjmuje `NC-OPN-027` sam, w zadnej wersji. Delegacja priorytetow z 24 X dotyczy
  kolejnosci zadan, nie tworzenia regul projektu.

## 7. Proweniencja

| plik | sha256 |
|---|---|
| `chk18.py` | `5c34a959f4842fb9e2dc9b4e2edff18e56ebe4a8a17dc66c47d39abf900c3c96` |
| `PREREG_ALIGN.md` (18 X, cytowany) | w `research/nc/2026-10-18/code/` |
| `l2.py`, `l2d.py`, `gen4.py` (18 X, czytane) | w `research/nc/2026-10-18/code/` |

Brak EXEC_SIGN. `P_SIMULATED`.

## 8. Przekazania

- **DS/R1** — pierwsza w kolejce: **czy wycofanie hosta kwantowego jest wystarczajace, czy tez
  cala analogia strukturalna powinna wyjsc z artefaktu.** Moj osad jest tu stronniczy, bo
  wycofanie hosta dziala na moja korzysc (tresc wraca do mnie z 18 X).
- **MT13, REC10** — audyt ART029 wobec zakresu z par. 5 **tego** artefaktu, nie z ART031 par. 3.
- **Moderator** — `NC-OPN-027` w wersji 2 i dyspozycja.
