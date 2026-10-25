# IW / NC — ODBIÓR red-teamu Groka: degradacja T2 i redukcja rangi tylko dla n=2

**Artefakt:** `IW_NC_ODBIOR_GROK_DEGRADACJA_T2_I_RANGA_TYLKO_N2_033_20261025`
**Rola:** Badacz (odbiór audytu zewnętrznego + własna korekta pochodna). **Data:** 2026-10-25.
**Koryguje:** ART029 (status T2; zakres redukcji rangi), ART031 §3 i ART032 §5 (lista „co zostaje
jako nowe"), ART030 §1 (redakcja). **Nie zmienia** T1, T1a, falsyfikacji H-A, świadka
geometrycznego, ani żadnej liczby.

**SUFIT CLAIMU: NO_CANON / NO_EXEC_SIGN / brak claimu nowości / audyt zewnętrzny nadal otwarty.**

---

## 1. Trafienie Groka — przyjęte, i sprawdzone zanim przyjęte

Grok (lateralny red-team, pakiet samowystarczalny przez Moderatora) zgłosił jedno trafienie
materialne: **T2 jest przedstawione jako „próg" o wadze porównywalnej z T1, a jest niemal
tautologią definicji normy logarytmicznej.**

Nie przyjąłem tego na słowo — konformizm wobec uczestnika ocenianego jako silniejszy jest
udokumentowanym trybem awarii modeli, a zgoda modeli nie jest dowodem. Sprawdziłem argument:

- kierunek `μ₂ ≤ 0 ⟹ sup wᵀe^{tG}w ≤ 1` to klasyczna konsekwencja `‖e^{tG}‖ ≤ 1`;
- kierunek odwrotny to `e^{tG} = I + tG + O(t²)` i **definicja** `μ₂` jako maksimum ilorazu
  Rayleigha części hermitowskiej.

To jest dwie linie, z których jedna jest definicją. **Grok ma rację.** Numeryczne sprawdzenie na
dziewięciu macierzach, w tym na trójce rozdzielającej `±0.05`, jest poprawną higieną i nie
podnosi faktu do rangi progu, który trzeba było odkryć.

**Co robię.** T2 **degradowane** z twierdzenia do elementarnego pomostu; usunięte z listy „co
zostaje jako nowe" w ART031 §3 i ART032 §5. Zachowuję tabelę dziewięciu macierzy jako kontrolę
spójności, jawnie jako higienę, nie jako wynik.

**Typ claimu:** interpretacyjny/redakcyjny — zgodnie z klasyfikacją Groka. To **trzecie**
wystąpienie tego samego gatunku u mnie w ciągu doby (po `NC-FAL-024`, gdzie poprawne `√m` nie
autoryzowało identyfikacji fizycznej). Poprawna równoważność nie autoryzuje interpretacji.

**Gdzie treść faktycznie leży.** Nietrywialne jest **nie** „sup Rayleigha > 1 ⟺ μ₂ > 0", lecz to,
że tempo wzrostu funkcjonału na pomiar **równa się** `sup_{Δ,w} wᵀe^{GΔ}w`. T2 jest trywialnym
pomostem od tej treści do kryterium `μ₂`. Bez tego rozdzielenia zdanie „próg dychotomii to
dokładnie `μ₂ = 0`" brzmi jak odkrycie, że wielkość zdefiniowana przez `μ₂` ma próg w `μ₂ = 0`.

## 2. Korekta pochodna, której Grok nie zgłosił jako błędu — moja

W nagłówku swojej oceny Grok napisał *„Redukcja rangi 1 + ρ = wᵀe^{GΔ}w **(n=2)**"* i uzasadnił:
*„W wymiarze 2 rzut Π ma rangę 1, więc P też; jedyna niezerowa wartość własna = ślad."*
Nie zgłosił tego jako trafienia. **Jest nim.**

`Π = I − ddᵀ` w wymiarze `n` ma rangę **`n − 1`**, nie 1. ART029 §6 mówi: *„cykl okresowy
`P = e^{GΔ}Π` ma **rang 1**"* — bez lokalnego zastrzeżenia wymiaru, jako **mechanizm**.
To prawda wyłącznie przy `n = 2`.

Sprawdzone (`rank.py`, sha256 `0c66392a8733976d3ad03166910986f8466dd2ed893b4cc7cf441b9bf230526c`):

| `n` | `rank(Π)` | `rank(P)` | `ρ(P)` | `|tr(P)|` | `ρ = tr`? |
|---|---|---|---|---|---|
| 2 | 1 | 1 | 0.899412 | 0.899412 | **tak** |
| 3 | 2 | 2 | 1.033199 | 2.061191 | nie |
| 4 | 3 | 3 | 2.141833 | 3.522155 | nie |
| 6 | 5 | 5 | 3.006937 | 5.164834 | nie |

Przy `n = 3` ślad jest dwukrotnie większy od `ρ`. Wzór jest tam **fałszywy**, nie tylko
niesprawdzony.

**Pytanie, które skierowałem do MT13, było źle postawione.** Zapytałem, *„czy redukcja rangi 1
przenosi się na `n > 2`"*. Nie o to należy pytać: przy `n > 2` `d_⊥` **nie jest kierunkiem**,
lecz podprzestrzenią wymiaru `n − 1`, więc nie ma czego przenosić — formuła śladowa nie ma tam
sensu. Poprawne pytanie: **co zastępuje formułę śladową, gdy `rank(Π) = n − 1 > 1`** — czy tempo
jest wtedy `sup` po `(n−1)`-wymiarowych podprzestrzeniach, i czy ma postać wariacyjną.

Poprawiam sformułowanie zadania w kolejce MT13 (pozycja 3, `NC-ALG-018`) **bez wyprzedzania
kolejki** — ich pozycja 2 to `NC-NUM-011`.

## 3. Korekta redakcyjna w ART030, którą ujawniło czytanie Groka

Grok odnotował: *„Wzorzec »wspólne dla każdego λ« oznacza zgodność między źródłami przy każdym
ustalonym λ, nie niezależność od λ"* — i rozstrzygnął to poprawnie przez postać zamkniętą i F2.
Rozstrzygnął, bo **musiał**; zdanie było dwuznaczne.

ART030 §1 pisze, że `X(T) = κΓ₀(1−e^{−λT})/λ` *„jest wspólne dla każdego `λ > 0`"*. Wzór
oczywiście zależy od `λ`; „wspólne" miało znaczyć „wspólne **dla porównywanych źródeł**".
Zdanie zawężone: **przy każdym ustalonym `λ > 0` wszystkie źródła utrzymujące nasycenie dają to
samo `X(T)`; sama wartość zależy od `λ`.** Projekt ma regułę anty-homonimii i to jest jej
przypadek — nie błąd rachunku, lecz claim, który trzeba było odczytać dwa razy.

## 4. Co zostaje jako nowe po czterech redukcjach

1. **T1** — nierówność `λ_max(W) ≤ m` dla każdego `G` z `μ₂ ≤ 0`, każdych `(e,d)`, czasów i sił.
   Dowód korzysta wyłącznie z podadditywności `λ_max` na składnikach PSD i z `‖e^{Gt}‖ ≤ 1`,
   więc jest **wymiarowo ogólny**. Grok sprawdził i uznał za czyste. To najmocniejsza część.
2. **T1a** — warunek osiągania z deficytem liniowym w `h`.
3. **Falsyfikacja H-A** jawną konstrukcją (`m = 2` daje `493.76 > M(G) = 36.79`). Kontrprzykład
   potrzebuje jednego wymiaru, więc `n = 2` wystarcza.
4. **Redukcja rangi 1 i `ρ = wᵀe^{GΔ}w` — wyłącznie `n = 2`**, odtąd jawnie.

**Usunięte z listy:** T2 (§1). **Zawężone:** punkt 4 (§2).

Czego to nie zmienia: żadnej liczby w 029, 030, 031, 032. Odpowiedź na `NC-OPN-002` stoi —
ciasna stała nie istnieje — ale **mechanizm** po stronie `μ₂ > 0` jest faktem o `2×2`, a nie
mechanizmem ogólnym, i tak go teraz zapisuję.

## 5. Ocena samego red-teamu

Grok podał też granicę swojego poszukiwania: pakiet zawierał pełny ART029 i ART030, cytaty z
preregestracji i z 18 X, ale **nie** pełny tekst ART031/032 ani kodu, więc *„nie znalazłem poza
T2 nie jest dowodem nieistnienia poza dostarczonym materiałem"*. To właściwe zastrzeżenie i jest
to ograniczenie **mojego** pakietu, nie jego pracy. Przy następnym zleceniu lateralnym dołożę
pełne teksty korekt i istotne fragmenty kodu.

Odnotowuję też, że najcenniejsza część jego odpowiedzi była w **nawiasie** przy rzeczy uznanej za
czystą, nie na liście trafień. Czyli: przy odbiorze red-teamu trzeba czytać także to, co audytor
uznał za poprawne, bo kwalifikatory, które tam stawia, mogą być trafieniami, których sam nie
zgłasza. To wzorzec operacyjny, nie komplement.

## 6. Czego NIE robię

- Nie wycofuję T2 jako **fałszywego** — jest prawdziwe. Degradowane jest jego **znaczenie**.
- Nie obniżam ani nie podnoszę statusu żadnego wiersza; `CLOSED` i `EXEC_SIGN` są ludzkie.
- Nie wyprzedzam kolejek z dyspozycji 033.
- Nie twierdzę, że po tych czterech redukcjach lista z §4 jest już stabilna. Trzy redukcje
  przyszły z trzech różnych powierzchni w ciągu czternastu godzin.

## 7. Proweniencja

| plik | sha256 |
|---|---|
| `rank.py` | `0c66392a8733976d3ad03166910986f8466dd2ed893b4cc7cf441b9bf230526c` |
| `PAKIET_GROK_NC_029_032_v1.md` | w `research/nc/2026-10-25/` |

Brak EXEC_SIGN. `P_SIMULATED`.

## 8. Przekazania

- **MT13** — poprawione sformułowanie `NC-ALG-018` (ich pozycja 3): nie „czy przenosi się na
  `n > 2`", lecz **co zastępuje formułę śladową przy `rank(Π) = n − 1 > 1`**.
- **DS/R1** — ich pozycja 1 (`NC-ALG-021`) bez zmian; przy okazji informacja, że T2 jest
  degradowane, więc nie ma sensu atakować go jako twierdzenia.
- **Grok** — podziękowanie merytoryczne: trafienie przyjęte, plus to z nawiasu, którego nie
  zgłosił. Następny pakiet będzie pełniejszy.
- **Moderator** — dyspozycja; `NC-OPN-027` nadal otwarte, teraz jako powierzchnia bramki LT5.
