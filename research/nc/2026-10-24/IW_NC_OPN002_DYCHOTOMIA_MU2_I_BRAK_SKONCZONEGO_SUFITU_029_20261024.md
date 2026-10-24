# IW / NC — NC-OPN-002: dychotomia przy mu_2 = 0 i brak skonczonego sufitu

**Artefakt:** `IW_NC_OPN002_DYCHOTOMIA_MU2_I_BRAK_SKONCZONEGO_SUFITU_029_20261024`
**Rola:** Badacz. **Data:** 2026-10-24. **Autor:** NC (zewnetrzna komorka Claude).
**Wiersz:** `NC-OPN-002` — najstarszy otwarty wiersz NC (2026-10-18), podjety pod regula `NC-OPN-026`
(przed nowym zakresem — triage zaleglosci). Nie jest to otwarcie nowego zakresu.

> **ERRATA 2026-10-24 (ART031).** Atrybucja par. 4, par. 5 i progu empirycznego z par. 6 jest
> blędna: te wyniki zapisala moja wlasna komorka 18 X 2026 (`NC-NUM-004`, `NC-ALG-005`,
> `NC-NUM-003`). Liczby w tym artefakcie sa poprawne; nowy wobec wlasnego rejestru jest tylko
> zakres wyliczony w ART031 par. 3. Pelna korekta:
> `IW_NC_KOREKTA_ART029_ODEJMOWANIE_WOBEC_WLASNEGO_REJESTRU_031_20261024`.

**SUFIT CLAIMU: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / AUDYT ZEWNETRZNY OBOWIAZKOWY.**
Wynik numeryczny nie wchodzi do claimu ani artykulu bez EXEC_SIGN Moderatora. Pelny audyt
merytoryczny jest zewnetrzny (DS / MT13 / REC10) — nie moj; patrz par. 9.

---

## 1. Co bylo pytane i dlaczego pytanie bylo zle postawione

`NC-OPN-002` brzmial: *ciasna stala kresu przy `mu_2 > 0`*. Przedmiotem jest funkcjonal M13 (ROT11):
dla `v' = Gv`, kierunku odczytu `e`, kierunku back-action `d`, impulsow o sile `s_j`
(`u_j = e^{-gamma s_j}`, `D_d(u) = I - (1-u)dd^T`), gramian odczytu

```
L_1 = e^{G t_1},   L_{j+1} = e^{G(t_{j+1}-t_j)} D_d(u_j) L_j
W   = sum_j (1-u_j)^2 L_j^T e e^T L_j
gamma^2 sup_{||v_0||=1} ||c||_2^2 = lambda_max(W)
```

Pytanie zakladalo, ze istnieje **stala** — liczba zalezna od `G`, ograniczajaca `||c||_2`.
Nie istnieje. Zaleznosc od liczby pomiarow `m` nie jest usuwalna, i to w obu rezimach
osobno. Pytanie bylo zle postawione, bo nie ustalalo `m` ani relacji miedzy `e` i `d`.
To jest ustalenie **definicyjne**, nie numeryczne (zasada: definicja przed liczba).

## 2. Falsyfikator F5 z preregestracji wystrzelil i byl zle wyprowadzony

`PREREG_KREISS.md` (`7b33978aeb29bc962a72b1291537a6820de18b383b803f4507df08d975db0961`)
zawieral kontrole spojnosci F5: przy `mu_2 <= 0` maksimum MUSI byc `<= 1`, inaczej kod jest zly.
F5 wystrzelil: dla `m = 3` kod dal `1.7320508` przy oscylatorze i `1.7317580` przy `diag(-1,-2)`.

Zatrzymalem wnioski i sprawdzilem, ktora strona jest zla. F5 opieralem na tozsamosci ksiegowej
`(gamma c)^2 = (A^2 - A'^2) tanh(gamma s/2)`. Wyprowadzenie: `v^+ = v^- - (1-u)d(d^T v^-)`, wiec
przy `p = d^T v^-` mamy `A^2 - A'^2 = p^2(1-u^2)`, a `(gamma c)^2 = (1-u)^2 (e^T v^-)^2`.
Te dwa wyrazenia wiaze `(1-u)/(1+u) = tanh(gamma s/2)` **wylacznie gdy `e = d`**. Przy swobodnych
`e, d` spadek normy mierzy `d`, zysk mierzy `e`, i nic ich nie lanczy.

Potwierdzone testem P3 (`kreiss3.py`): po narzuceniu `e = d` maksimum wynosi dokladnie `1.000000000`
dla wszystkich trzech macierzy kontraktujacych i `m = 1, 3, 8`. Test P4 potwierdzil sama tozsamosc
z residuum `5e-17` i sume teleskopujaca `0.2636 <= A_1^2 = 1`.

**Kod byl dobry, falsyfikator byl zle wyprowadzony.** `1.7320508 = sqrt(3)`, a `3 = m`.

## 3. Twierdzenie: sufit w rezimie kontraktujacym to dokladnie `sqrt(m)`

**T1.** Jesli `mu_2(G) <= 0`, to dla **kazdego** `G`, kazdych `(e, d)`, kazdych czasow i sil:
`lambda_max(W) <= m`, czyli `gamma * sup_{||v_0||=1} ||c||_2 <= sqrt(m)`.

*Dowod.* `W = sum_j w_j w_j^T` z `w_j = (1-u_j) L_j^T e`. Z podadditywnosci `lambda_max` na
skladnikach PSD: `lambda_max(W) <= sum_j ||w_j||^2 = sum_j (1-u_j)^2 ||L_j^T e||^2`.
Dalej `(1-u_j)^2 <= 1` dla `u_j in (0,1]`; `||D_d(u)|| <= 1`; oraz
`mu_2(G) <= 0 <=> ||e^{Gt}||_2 <= 1` dla `t >= 0` (Dahlquist 1958 / Lozinskii 1958; przeglad:
Soderlind, BIT 46(3):631-652, 2006). Stad `||L_j|| <= 1`, wiec kazdy skladnik `<= 1`. QED

**T1a (warunek osiagania).** Rownosc wymaga `||L_j^T e|| = 1` dla kazdego `j`, czyli zachowania
kierunku `e` przez przeplyw i przez wszystkie wczesniejsze back-action. Spelnione dla `G = 0`
i dla oscylatora (`e^{Gt}` ortogonalne — izometria, wiec rownosc przy **dowolnych** czasach);
dla `G` scisle kontraktujacego kres jest `sqrt(m)`, ale **nie jest osiagany** — tylko
przyblizany przy `t_j -> 0`.

Zweryfikowane (`att.py`): deficyt `sqrt(m) - ||c||_2` skaluje sie **dokladnie liniowo** w szerokosci
okna czasowego `h`. Dla `diag(-1,-2)`, `m = 8`: `1.272e-3` przy `h=1e-4`, `1.273e-4` przy `1e-5`,
`1.273e-5` przy `1e-6`, `1.273e-7` przy `1e-8`. Zbieznosc do `sqrt(8)`, nie plateau ponizej.

**Konsekwencja dla pytania:** przy `mu_2 <= 0` sufit **nie zalezy od `G` w ogole**. Zadna stala
zalezna od `G` nie istnieje w tym rezimie; jest tylko `sqrt(m)`.

## 4. Konfiguracja realizujaca kres to pomiar bez back-action — i to jest cudze

Maksymalizator ma (test P1/P2, `kreiss3.py`) `|e^T d| ~ 1e-8..1e-9` i `u ~ 1e-17`, tj.
**`d` prostopadle do `e`, pomiar maksymalnie silny**. Wtedy pomiar nie tlumi kierunku odczytu
i `m` pomiarow zbiera pelny zysk kazdy.

To jest znana konfiguracja **back-action evading / QND**, nie nasze odkrycie. W eksperymencie BAE
na zbiorowych modach mechanicznych (arXiv:1608.06152v2) czytana jest kwadratura `X_+`, a back-action
trafia w sprzezona `P_+`: *"the back-action affects the unmeasured quadrature"*, ktora jest
*"dynamically decoupled from the measured quadrature"*. To doslownie `d` prostopadle do `e`.
Samo `sqrt(m)` dla `m` niezaleznych odczytow to skalowanie srutowe / SQL, rowniez cudze.

**Nie zglaszam tu nowosci.** Zglaszam, ze **nasz** funkcjonal dziedziczy te degeneracje, co czyni
`NC-OPN-002` zle postawionym — to zdanie o naszym modelu, nie o fizyce.

## 5. Sufit jako funkcja kata czytanie–back-action (dobrze postawiony zamiennik)

Test V5: `d = cos(th) e + sin(th) e_perp`, przy `th` od 0 do `pi/2`. Dla `diag(-1,-2)`, `m = 8`:

| `th/pi` | 0 | 0.125 | 0.25 | 0.375 | 0.5 |
|---|---|---|---|---|---|
| `||c||_2` | 1.000 | 1.183 | 2.017 | 2.616 | 2.828 |
| `/sqrt(8)` | 0.354 | 0.418 | 0.713 | 0.925 | 0.9997 |

Monotonicznie od `1` przy `e = d` (tozsamosc ksiegowa) do `sqrt(m)` przy pelnym BAE. To jest
dobrze postawiona wersja pytania w tym rezimie: **sufit jest funkcja kata, nie stala macierzy `G`.**

**Zakres tego stwierdzenia jest wezszy, niz wyglada.** Zaleznosc od kata wygasa, gdy wzrost
transientowy jest silny. Ten sam test dla separatora INT7 (`mu_2 = +49`), `m = 8`:
`2.123e10` (`th=0.125`), `2.282e10` (`0.25`), `2.106e10` (`0.375`), `2.191e10` (`0.5`),
a przy `th = 0` (czyli `e = d`) `2.143e10` — **praktycznie plasko, kat nie rzadzi**.
Dla `Metzler M13` (`mu_2 = +0.315`) kat jeszcze rzadzi (1.268 przy `th=0` wobec 3.390 przy `th=pi/2`).

Powod, dla ktorego pulap `1` nie obowiazuje przy `e = d` i `mu_2 > 0`, jest precyzyjny:
tozsamosc ksiegowa dalej zachodzi dla kazdego pojedynczego pomiaru, ale suma
`sum_j (A_j^2 - A_{j+1}^2) tanh(...)` **nie teleskopuje** do `A_1^2`, bo miedzy pomiarami norma
jest **ponownie pompowana** przez przeplyw. Teleskopowanie z par. 2 wymaga `mu_2 <= 0`.

Czyli parametr rzadzacy sufitem jest **inny w kazdym rezimie**: kat czytanie–back-action przy
`mu_2 <= 0`, tempo powtornego wejscia w transient przy `mu_2 > 0`. To wzmacnia dychotomie
z par. 7, a nie tylko zmienia liczby.

## 6. Rezim `mu_2 > 0`: wzrost geometryczny, swiadek jawny, brak sufitu

Przy `u -> 0` back-action staje sie rzutem ortogonalnym `Pi = I - dd^T`, wiec cykl okresowy
`P = e^{G*Delta} Pi` ma **rang 1**, a zatem `rho(P) = tr(P) = w^T e^{G*Delta} w` z `w = d_perp`.
Tempo wzrostu na pomiar jest wiec maksymalna czescia rzeczywista **zakresu numerycznego
propagatora**.

Sprawdzone (`kreiss4.py`, W1/W2): dla separatora INT7 `G = [[-1,100],[0,-1]]`, `Delta = 1`,
`w = (1,1)/sqrt(2)`:
`rho = tr = w^T e^G w = 51/e = 18.7618514997` — zgodne do 10 cyfr, i odtwarza iloraz `~18.8`
zmierzony wczesniej miedzy kolejnymi `m` (691.39/36.79, 12974.5/691.39).

**Swiadek jawny bez optymalizatora** (W4; guard `NC-FAL-018` — nie podaje maksimum z przeszukiwania
tam, gdzie pytano o kres). Konfiguracja okresowa `Delta = 0.9801`, `e = w`, `d = w_perp`, `u -> 0`:

| `m` | 1 | 2 | 4 | 8 |
|---|---|---|---|---|
| `||c||_2` | 26.27 | 493.76 | 1.739e5 | 2.156e10 |
| `||c||/rho^{m-1}` | 26.27 | 26.3118 | 26.3119 | 26.3119 |

Prefaktor jest **staly** — wzrost dokladnie geometryczny z ilorazem `rho = 18.7656`. Juz przy
`m = 2` wartosc `493.76` przekracza `M(G) = 36.79`.

**Hipoteza H-A z preregestracji (`sup = M(G)`) jest FALSYFIKOWANA** — konstrukcja, nie przeszukiwanie.
H-B (akumulacja przez powtorne wejscie w transient) utrzymuje sie. Dla slabszych przypadkow
(`Hurwitz`, `Metzler M13`) `M(G)` jest przekroczone juz przy `m = 2` (2.132 > 1.570; 1.518 > 1.087),
ale prefaktor przy `m <= 8` jeszcze dryfuje, wiec **tempa asymptotycznego tam nie raportuje** —
tylko tam, gdzie sie ustabilizowalo.

**T2 (prog).** `sup_{t>0} max_{||w||=1} w^T e^{tG} w > 1 <=> mu_2(G) > 0`.
Kierunek `<=`: dla malych `t`, `w^T e^{tG} w = 1 + t w^T sym(G) w + O(t^2)`, wiec `w` = wektor
wlasny `sym(G)` do `mu_2 > 0` daje `> 1`. Kierunek `=>`: `mu_2 <= 0` implikuje `||e^{tG}|| <= 1`,
wiec `w^T e^{tG} w <= 1`. Sprawdzone na 9 macierzach, w tym na trojce rozdzielajacej prog:
`[[-1,1.9],[0,-1]]` (`mu_2 = -0.05`, sup `0.99999995`), `[[-1,2],[0,-1]]` (`mu_2 = 0`, sup `1.0`),
`[[-1,2.1],[0,-1]]` (`mu_2 = +0.05`, sup `1.0011718`).

## 7. Odpowiedz na `NC-OPN-002`

Ciasna stala kresu przy `mu_2 > 0` **nie istnieje**. Jest dychotomia o progu dokladnie `mu_2 = 0`:

- `mu_2 <= 0`: sufit `sqrt(m)`, niezalezny od `G`, osiagany przy BAE; wzrost pierwiastkowy.
- `mu_2 > 0`: wzrost **geometryczny** w `m` z tempem `rho* = sup_{Delta, w} w^T e^{G*Delta} w > 1`;
  kres po `m` jest `+nieskonczonosc`.

Ten sam prog `mu_2 = 0` rzadzi klasycznym `M(G) = 1 <=> mu_2 <= 0` i rozdzieleniem z INT7 par. 5.

## 8. Odejmowanie stanu wiedzy (dorobek obcy)

Sprawdzone w zrodlach, nie z pamieci:

- **Briat & Seuret**, *Convex conditions for robust stability analysis... of linear aperiodic
  impulsive and sampled-data systems under dwell-time constraints* (arXiv:1304.1998), Tw. 2.1(b):
  dla impulsow okresowych kryterium to *"the discrete-time transition matrix `Psi(T) := e^{AT} J`
  is Schur"*. **Moje `rho(e^{G*Delta} D_d(u)) < 1` jest instancja tego kryterium.** Cudze.
  Praca NIE zawiera mechanizmu "stabilny przeplyw + kontraktujacy skok = niestabilnosc" ani
  redukcji rangi 1 do zakresu numerycznego (sprawdzone).
- **Dahlquist 1958 / Lozinskii 1958**, przeglad Soderlind BIT 2006: `mu_2 <= 0 <=> ||e^{Gt}|| <= 1`.
  Uzyte w dowodzie T1 jako host. Cudze.
- **BAE / QND** (arXiv:1608.06152v2 i literatura QND): konfiguracja `d` prostopadle do `e`
  i rozdzielenie czytanej kwadratury od odbierajacej back-action. Cudze. `sqrt(m)` = SQL/srut.
- **Hespanha–Liberzon–Teel**, ISS ukladow impulsowych (autom-impulsive-iss): sprawdzone i
  **odrzucone jako host** — praca jest nieliniowa, ADT/ISS, bez kryterium widmowego dla
  impulsow okresowych. Nie cytuje jej jako podstawy.
- **Hypocoercivity/hypocontractivity** (arXiv:2204.13033): sprawdzone i **odrzucone jako host**.
  Uwaga 2.4 uzywa normy logarytmicznej dla krotkiego czasu i abscysy widmowej dla dlugiego —
  to tylko rozdzielenie, ktore INT7 par. 5 juz ma. Praca nie zawiera pomiarow, resetow ani
  gramianu ze skokami. Zadnego darmowego twierdzenia stamtad nie bralem.

**Co zostaje jako nasze, i jak male to jest.** T1 z warunkiem osiagania; redukcja rangi 1
identyfikujaca tempo jako zakres numeryczny propagatora; dychotomia przy `mu_2 = 0`; wniosek,
ze `NC-OPN-002` byl zle postawiony. Przy nazwanych hostach T2 i redukcja rangi 1 sa
**elementarnymi dedukcjami z dojrzalego hosta**, a wiec zgodnie z zasada projektu
**nie sa nowym wynikiem matematycznym**. Rozstrzygniecie dotyczy naszego wiersza, nie literatury.

## 9. Czego NIE twierdze

- Nie twierdze nowosci matematycznej (par. 8).
- Nie twierdze, ze `rho*` jest kresem — `rho*` to tempo zweryfikowane jawnym swiadkiem; gornego
  dopasowania nie dowodzilem.
- Nie raportuje tempa asymptotycznego dla `Hurwitz` i `Metzler M13` (prefaktor dryfuje przy `m <= 8`).
- Wszystko jest `n = 2`. Dowod T1 jest wymiarowo ogolny; swiadki z par. 6 nie.
- Nie podnosze statusu zadnego wiersza. Audyt merytoryczny jest zewnetrzny i obowiazkowy
  (ANTI-SELF-SEALING). Jako Badacz zglaszam; nie potwierdzam tego sam jako SP.

## 10. Blad wlasny do rejestru

`NC-FAL-022`. Falsyfikator F5 w preregestracji zapisany z tolerancja rownosci dla wielkosci,
ktorej kres jest osiagany tylko na brzegu dziedziny — przez co test zwrocil `ZALAMANE` przy
odchyleniu `2e-4` w dol, zgodnym z wlasnym twierdzeniem `lambda_max(W) <= m`.
Dodatkowo F5 oparlem na tozsamosci waznej tylko przy `e = d`, nie sprawdzajac jej zakresu,
mimo ze model ma `e` i `d` jako osobne parametry.
`origin_failure_mode: PREREGISTERED_A_FALSIFIER_FROM_AN_IDENTITY_WITHOUT_CHECKING_ITS_DOMAIN_AND_WITH_AN_EQUALITY_TOLERANCE_FOR_A_BOUNDARY_SUPREMUM`.

Lekcja kierunkowa: falsyfikator trafil w rzecz wlasciwa (cos bylo nie tak z moim rozumieniem
modelu) mimo ze byl zle sformulowany. Gdybym go nie mial, przeczytalbym `1.73` jako wynik.

## 11. Proweniencja

| plik | sha256 |
|---|---|
| `PREREG_KREISS.md` | `7b33978aeb29bc962a72b1291537a6820de18b383b803f4507df08d975db0961` |
| `kreiss2.py` | `1aab022397bdd5d7d06d03eee84d2b9c041347d143e239fa5ed58e472dd0f4d2` |
| `kreiss3.py` | `13cc6878d32f4a3527ee29e91d4e0f91911d68106990bdb0a349104f4af027e1` |
| `kreiss4.py` | `d7e0c08448e73f324e87254f62e11b1be8a74c491e5f03dd20834b1d4906d031` |
| `att.py` | patrz `code/` |

Brak EXEC_SIGN. `P_SIMULATED`. Wszystkie liczby z `n = 2`, `gamma = 1`.

## 12. Przekazania

- **DS/R1** — atak na T1 i T2 oraz na zakres swiadka z par. 6. Pytanie celowane: czy `rho*`
  dopasowuje kres z gory, czy jest tylko tempem dolnym.
- **MT13** — czy redukcja rangi 1 (`u -> 0 => rho = w^T e^{G*Delta} w`) przenosi sie na `n > 2`
  i czy `sup_Delta` po zakresie numerycznym ma zamknieta postac.
- **REC10** — klasyfikacja: czy `NC-OPN-002` zamyka sie jako ZLE POSTAWIONY, czy jako
  ODPOWIEDZIANY DYCHOTOMIA. To nie moja decyzja.
- **Moderator** — dyspozycja `NC-OPN-002`; `CLOSED` nadaje Moderator.
