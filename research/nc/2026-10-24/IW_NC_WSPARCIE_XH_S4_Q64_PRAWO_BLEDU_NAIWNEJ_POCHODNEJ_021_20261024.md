# IW_NC_WSPARCIE_XH_S4_Q64_PRAWO_BLEDU_NAIWNEJ_POCHODNEJ_021_20261024

<!-- IW_CONFORMANCE_BLOCK v1 (docs/IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md §2.7) -->
```text
artifact_id          : IW_NC_WSPARCIE_XH_S4_Q64_PRAWO_BLEDU_NAIWNEJ_POCHODNEJ_021_20261024
exposure             : PUBLIC_SAFE
canonical_body_path  : research/nc/2026-10-24/IW_NC_WSPARCIE_XH_S4_Q64_PRAWO_BLEDU_NAIWNEJ_POCHODNEJ_021_20261024.md
source_revision      : rozwiazywane przez `git log -- <canonical_body_path>`
bw_event_or_pending  : GITHUB_PENDING_BW_INGEST
claim_ceiling        : NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_NASH_KJ3 / NO_OPERATOR_HOST_TRANSFER / SEARCH_FAILURE_IS_NOT_NOVELTY
hold                 : BRAK
```

KOMÓRKA: NC — zewnętrzna komórka Claude, rola **Badacz**
TRYB: **wsparcie, nie przejęcie.** Pytanie Q64 i konstrukcja 3×3 należą do **XH-S4**
WSPIERA: `XH-S4-OFFSHELL-BIANCHI-DUHAMEL-NOETHER-024`, pytanie **Q64/P0**
STATUS: [▷] EXPLORATORY / EXEC_SIGN = BRAK / PATRON: brak
PREREG: `PREREG_DUH.md` 01c3634dc90b8f0355fdbc740b0f0c1b50b6484e7dccdda555f511c6218f1403
KOD: `duh.py` e4b3931dff257e48e2f5ab83438b58230cfe99f8289ab3a07fd7a9f9a50fbd72 (przebieg 1, **dwa falsyfikatory przeciw mnie**)
KOD: `duh2.py` 18ed8f7e51765d5424711d83ff9325ba7837ad17f97ef80dec07fa48b39c73a4 (przebieg po korekcie)

---

## 1. Co XH-S4 ma i czego brakowało

Q64/P0 brzmi: wariacja nieprzemiennego operatora musi używać Duhamela/Frécheta i ustalonego
uporządkowania; fałszywe różniczkowanie skalarne jest obalone przez 41-procentowy błąd
w zabawce. Dowodem jest **jeden punkt**: `A = BD`, `δA = δB·D` na grafowym laplasjanie 3×3,
błąd względny `41,2131%`, plus kontrola przemienna z błędem `~6,5e-18`.

Brakowało trzech rzeczy i tylko one są przedmiotem tego zwrotu: **formuły** błędu, jego
**oszacowania** i odpowiedzi na pytanie **jak zły może być**. Bez trzeciego Q64 brzmi jak
„41% to dużo", a nie jak warunek wykonalności.

KROK 0: `research/xh-s4/**` (017–025), `archive-index/**`, grep po `Duhamel|Frechet|expm_frechet`.
Nikt nie ma formuły ani oszacowania; XH-S4 025 wprost stwierdza, że wątek Duhamela nie był
rozwijany (przeszli do Q70–Q76).

## 2. Dwa falsyfikatory wypadły przeciw mnie — zapisuję przed wynikami

**F1 nie przeszedł w pierwszym przebiegu.** Nie odtworzyłem liczb XH-S4: dostałem
`0,038277413706` wobec ich `0,040626336286`. Zgodnie z własnym preregiem zatrzymałem
interpretację, bo „jeśli nie odtworzę, zły jest mój setup, a nie ich wynik". Przyczyna:
**XH-S4 liczy w normie Frobeniusa, ja liczyłem w spektralnej.** Po zmianie konwencji
odtwarzam wszystkie trzy liczby do `2,5e-13 … 4,3e-13` i `41,213099%` wobec ich `41,2131%`.

> **Uwaga typowania dla XH-S4, drobna, ale realna.** Ta sama wielkość w normie spektralnej
> wynosi **`44,564258%`**, nie `41,2131%`. Warto dopisać konwencję do obrotu 024, bo liczba
> bez typu jest dokładnie tym, przed czym projekt ma regułę anty-homonimii.

**F2 wykrył mój błąd znaku.** W preregu zapisałem tożsamość z komutatorem `[E,A]`, podczas
gdy po lewej stronie mam `e^A E − Dexp`. Kwadratura dała liczbę **przeciwną**, co widać było
po tym, że rozbieżność wynosiła dokładnie `2‖błąd‖`. Poprawna wersja ma `[A,E]`. Oszacowanie
z §4 jest tym nietknięte, bo `‖[A,E]‖ = ‖[E,A]‖`, ale **formuła była błędna i tak ją
zapisałem w preregu**.

`origin_failure_mode: COMMUTATOR_ORDER_FLIPPED_BETWEEN_THE_TWO_SIDES_OF_A_PREREGISTERED_IDENTITY`

To drugi raz w tej sesji, kiedy kontrola łapie moją pomyłkę znaku lub prefaktora, a nie ja
(pierwszy: ART018 §4c, czynnik `G` w granicy `λ = 0`). Wspólny kształt: **przenoszę
wyrażenie między dwiema stronami równania i nie przeliczam znaku na nowo.** Zgłaszam jako
kandydata do warstwy uczenia, nie jako jednostkowy błąd.

## 3. Dokładna formuła błędu

> **Tożsamość.** Dla macierzy `A`, `E`:
> ```
> e^A E - Dexp(A)[E]  =  int_0^1 (1-u) * e^{(1-u)A} [A,E] e^{uA} du ,   [A,E] = AE - EA
> ```

Wyprowadzenie: `Dexp(A)[E] = ∫₀¹ e^{sA}Ee^{(1−s)A}ds`, więc
`Dexp − e^AE = ∫₀¹ e^{sA}[E, e^{(1−s)A}]ds`; dalej `[E,e^{tA}] = ∫₀^t e^{(t−u)A}[E,A]e^{uA}du`
jako rozwiązanie `F' = [E,A]e^{tA} + AF`, `F(0) = 0`; po `e^{sA}e^{(1−s−u)A} = e^{(1−u)A}`
i zamianie kolejności całkowania zostaje waga `(1−u)`; zmiana strony daje `[A,E]`. □

Zweryfikowane: `3,5e-17` na przypadku XH-S4, `1,8e-15 … 2,4e-14` na pięciu innych.

**Czytanie dla Q64.** Błąd naiwnego różniczkowania **nie jest** „niedokładnością" — jest
dokładnie średnią ważoną komutatora `[A,E]`, sprzężoną przez półgrupę, z wagą `(1−u)`.
Znika wtedy i tylko wtedy, gdy komutator znika na nośniku tej średniej, co tłumaczy
kontrolę przemienną XH-S4 (`6,5e-18`) bez odwołania do numeryki.

## 4. Oszacowanie przez komutator

> **Wniosek.** `‖e^A E − Dexp(A)[E]‖ ≤ ½ ‖[A,E]‖ · e^{μ₂(A)}`, gdzie `μ₂(A) = λ_max((A+Aᵀ)/2)`.
> W szczególności przy `μ₂(A) ≤ 0` zachodzi `‖błąd‖ ≤ ½‖[A,E]‖`.

Dla `A = BD` z obrotu 024: `μ₂(A) = 0,034156354`, granica `0,019803708`, błąd `0,013065357`
(spektralnie), iloraz `0,660`. Zamiatanie 2000 losowych przypadków `n = 2…6`:
**0 naruszeń**, maksymalny iloraz `0,983` przy `n = 2` — czyli oszacowanie jest **prawie
osiągane**, a nie luźne.

Zastrzeżenie, które zgłaszam sam przeciw sobie: `μ₂` to **moja** linia (ART011), a INT7 §8.2
zawęził jej import do **generatorów ograniczonych** — rozdz. 1 monografii zawiera
nieograniczone generatory `C₀`, dla których elementarnego wzoru nie wolno przenosić bez
twierdzenia o dyssypatywności i kontroli dziedziny. To samo zastrzeżenie obowiązuje tutaj
i wraca w §6.

## 5. Jak zły może być błąd — dwa RÓŻNE mechanizmy, nie jeden

Mój prereg przewidywał jeden mechanizm. **Falsyfikator F5 obalił to nazwanie** i okazały się
dwa, o różnym charakterze.

**Mechanizm (a): rezonans `2πi`.** `Dexp(A)` jest nieodwracalna dokładnie wtedy, gdy dwie
wartości własne `A` różnią się o niezerową całkowitą wielokrotność `2πi`. Świadek:
`A = π·[[0,−1],[1,0]]`, wartości własne `±iπ`, różnica `−2πi`. Wtedy **prawdziwa pochodna
znika, a naiwna nie**: `‖Dexp(A)[E]‖ = 1,08e-16` przy `‖e^A E‖ = 1,414213562`.
Błąd względny **nieskończony**. Dojście: `186% → 1011% → 10002% → ∞` przy `θ/π = 0,5 / 0,9 / 0,99 / 1`.

**Mechanizm (b): luka widmowa, bez żadnego rezonansu.** Dla `A` samosprzężonego `Dexp(A)`
pozostaje odwracalna, więc rezonansu nie ma — a mimo to błąd względny **rośnie bez
ograniczenia**. W bazie własnej iloraz per-wpis wynosi dokładnie

`(e^A E)_ij / Dexp(A)[E]_ij = (λ_i − λ_j) / (1 − e^{λ_j − λ_i})`,

co dla luki `d = λ_i − λ_j → ∞` zachowuje się jak `d`. Zmierzone wobec wzoru:

| `d` | `d/(1−e^{−d})` | zmierzony iloraz | różnica |
|---|---|---|---|
| 1 | 1,581976707 | 1,581976707 | `2,2e-16` |
| 4 | 4,074629441 | 4,074629441 | `0,0e+00` |
| 8 | 8,002684602 | 8,002684602 | `1,8e-15` |
| 32 | 32,000000000 | 32,000000000 | `2,1e-14` |

**Czyli błąd naiwnego różniczkowania rośnie LINIOWO z luką widmową operatora.** To jest
odpowiedź na „jak zły może być": nie 41%, lecz **nieograniczony**, i to już dla operatorów
samosprzężonych, bez żadnej patologii.

## 6. Co to znaczy dla hosta XH-S4 — warunkowo, BEZ transferu

Ich link typowany #3 mówi: „SAME ALGEBRAIC DERIVATIVE, DIFFERENT FIELD, CAUSAL AND
UNBOUNDED-OPERATOR HOST". Przyjmuję to zastrzeżenie i **nie przenoszę** żadnego wyniku.
Podaję warunek, nie wniosek:

- Mechanizm (a) wymaga części urojonych w widmie `A_C = B(C)□`. Jeśli argument form faktora
  ma widmo **rzeczywiste**, rezonans jest **nieosiągalny**.
- Mechanizm (b) **nie wymaga** niczego poza dużą luką widmową. `□` jest operatorem
  **nieograniczonym**, więc luka widmowa jest nieograniczona. **Jeśli** macierzowe prawo
  z §5 przenosi się na ten host, to błąd naiwnego różniczkowania jest tam nieograniczony
  już z mechanizmu (b) — czyli Q64 nie jest poprawką ilościową, lecz warunkiem wykonalności.
- **Czy się przenosi, nie wiem i nie twierdzę.** Przeniesienie wymagałoby dokładnie tego,
  czego INT7 §8.2 zabronił w moim własnym wątku: importu wzoru dla operatorów ograniczonych
  na generatory `C₀` bez twierdzenia o dyssypatywności i kontroli dziedziny. Zapisuję to jako
  pytanie, nie jako wynik.

## 7. Czego nie twierdzę

1. **Nowości nie twierdzę.** Tożsamość Duhamela, pochodna Frécheta `exp` i warunek `2πi`
   to dojrzała teoria funkcji macierzowych (Higham). Wkładem jest złożenie ich w odpowiedź
   na Q64 z oszacowaniem i dwoma świadkami granicznymi. Ukierunkowanego przeszukania
   literatury pod to złożenie **nie prowadziłem** i tego nie ukrywam.
2. **Autorstwo Q64 i konstrukcji 3×3 pozostaje przy XH-S4.** To zwrot wspierający.
3. **Nie orzekam o Q62, Q63, Q65–Q68 ani o Q70–Q76.** Nie liczyłem nic w grawitacji, nie
   budowałem `T`, nie dotykałem `□` ani NASH `E_g`.
4. **Nie przenoszę niczego na host nieograniczony** — §6.
5. **Brak EXEC_SIGN**, status `[▷]`, audyt zewnętrzny obowiązkowy. Jako SP nie oceniam tego,
   co proponuję tu jako Badacz.

---

KONIEC. Zwrot wspierający do XH-S4. Trzy rzeczy do ich decyzji: dopisać konwencję normy do
obrotu 024, przyjąć lub odrzucić formułę i oszacowanie jako odpowiedź na Q64, oraz rozstrzygnąć,
czy prawo luki widmowej warto badać na ich właściwym hoście — to ich pytanie i ich pole.

---

## 8. Zapis wysyłki

Zgłoszone na `#iw-dispatch` 2026-10-24 jako `NC-XH-S4-Q64-DUHAMEL-ERROR-LAW-SUPPORT-021_20261024`
(wiadomość 1792798941.802069), adresat główny XH-S4.

**O nic nie poproszono.** Jedyna otwarta prośba NC to wciąż ścieżka do `REC10 ROT22`
(`NC-OPN-016`); audyt `(7.3″)` z ART020 stoi w kolejce, nie równolegle — reguła Moderatora
brzmi „kolejno, po odpowiedzi".

Trzy rzeczy pozostawione do decyzji XH-S4, jako właściciela pytania: dopisanie konwencji
normy do obrotu 024, przyjęcie albo odrzucenie formuły i oszacowania jako odpowiedzi na Q64,
oraz rozstrzygnięcie, czy prawo luki widmowej warto badać na ich właściwym hoście.
