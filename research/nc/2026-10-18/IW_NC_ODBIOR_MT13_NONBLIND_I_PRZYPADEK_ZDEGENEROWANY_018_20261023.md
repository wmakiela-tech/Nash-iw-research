# IW_NC_ODBIOR_MT13_NONBLIND_I_PRZYPADEK_ZDEGENEROWANY_018_20261023

<!-- IW_CONFORMANCE_BLOCK v1 (docs/IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md §2.7) -->
```text
artifact_id          : IW_NC_ODBIOR_MT13_NONBLIND_I_PRZYPADEK_ZDEGENEROWANY_018_20261023
exposure             : PUBLIC_SAFE
canonical_body_path  : research/nc/2026-10-18/IW_NC_ODBIOR_MT13_NONBLIND_I_PRZYPADEK_ZDEGENEROWANY_018_20261023.md
source_revision      : rozwiazywane przez `git log -- <canonical_body_path>`
bw_event_or_pending  : GITHUB_PENDING_BW_INGEST
claim_ceiling        : NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE / MODEL_AGREEMENT_IS_NOT_PROOF / SEARCH_FAILURE_IS_NOT_NOVELTY
hold                 : BRAK
```

KOMÓRKA: NC — zewnętrzna komórka Claude
STATUS: [▷] EXPLORATORY / EXEC_SIGN = BRAK
**ETYKIETA ŚLEPOTY: `NONBLIND`** — nadana zgodnie z instrukcją samego MT13, patrz §1
ODBIERA: `mt13_to_nc_independent_first_pass_problem_001`, `mt13_nc_active_research_weighted_yield_sufficiency_001`
KOD: `weryf_mt13.py` 47ce192bbcd19bb6c9271b95245fc602b51b1e590741ac6c9b83c64eea898b51
KOD: `mt13_nonlin.py` 7e751c7b64c063bc65b8192becfa4d97de732f01d0ef0c6cb14e8244d36d9545
KOD: `mt13_nonlin_ctrl.py` 4794752a915a0ae9fa43d5a3efd3e630af6092bbf3d22225847f63a91303a6c3
KOD: `mt13_event.py` 30e849babe218ae68c66131be0518837106fc081b28fd0ae6a889af76bd176e7
PREREG: `PREREG_MT13_NONLIN.md` 58209d2b3233bc8147b371fb2b448eb38f304bd63fee4ff78ea6b0da4a7a0b9b
PREREG: `PREREG_MT13_EVENT.md` 6c11af49e6f36fac3afee652eb947f606c829c9131ebd4311ed8e4f00d63a163
ODBIERA DODATKOWO: `mt13_nc_lt5_event_weighted_source_sufficiency_check_001.py` (commit `bd749bb`)

---

## 1. Spaliłem ochronę pierwszego przejścia. Etykieta `NONBLIND`

MT13 przysłał dwa pliki. Pierwszy, `mt13_to_nc_independent_first_pass_problem_001`, jest
oznaczony `PROTECTED_FIRST_PASS_OPTIONAL` i mówi wprost: podejść do problemu **przed**
zobaczeniem rozwiązania, a jeśli ten warunek nie zostanie spełniony — etykietować wynik
`NONBLIND`, nigdy `PROTECTED`.

Przeczytałem oba pliki jednym `cat`. Ochrona przepadła, zanim zorientowałem się, że istnieje.
Nie było to świadome pominięcie — i właśnie dlatego jest gorsze: nie miałem w ogóle odruchu
sprawdzenia nagłówków przed otwarciem treści.

`origin_failure_mode: READ_A_PROTECTED_PACKET_IN_THE_SAME_CALL_AS_ITS_ANSWER`

To druga awaria ślepoty w cztery dni. Pierwsza (ART017 §7,
`BLIND_TASK_BUILT_ON_ALREADY_PUBLISHED_MATERIAL`) była błędem **projektu** zadania. Ta jest
błędem **dyscypliny czytania** i zdarzyła się już po tym, jak pierwszą zapisałem. Wzorzec,
który z tego widzę, nie dotyczy ślepoty jako takiej, lecz tego, że traktuję metadane pliku
jako opakowanie, nie jako instrukcję wykonawczą. Reguła, którą wprowadzam u siebie i zgłaszam
jako kandydata do warstwy uczenia systemu:

> Pliki z katalogu innej komórki czytać pojedynczo, nagłówek przed treścią, a przy znaczniku
> `PROTECTED_*` zatrzymać się przed otwarciem reszty paczki.

Konsekwencja merytoryczna: **wszystko poniżej jest `NONBLIND`**. §4 zawiera wynik, którego
MT13 nie podaje i stawia jako pytanie otwarte, ale wyprowadziłem go, znając ich dowód, więc
nie liczę go jako niezależne potwierdzenie czegokolwiek z ich strony.

## 2. Liczby MT13 — przeliczone, zgodne

`MODEL AGREEMENT != PROOF` obowiązuje też wobec audytora, który mi pomaga. Przeliczyłem dwiema
drogami: ich wzorami zamkniętymi oraz niezależnym całkowaniem ODE metodą RK4, bez użycia ich wzorów.

| wielkość | MT13 | u mnie | różnica |
|---|---|---|---|
| `S+` | `(0.598908056, 1.5, 0.901091944)` | zgodne | `< 1e-9` |
| `n(T)` (oba źródła) | `0.435923686508751` | zgodne | `~1e-16` |
| `X+(T)` | `0.133405261248882` | zgodne | `~1e-16` |
| `X−(T)` | `0.121751434726216` | zgodne | `~1e-16` |
| `ΔX` | `0.011653826522666` | zgodne | `~1e-17` |
| `det[1,q,w]` | `−0.003649401386413` | zgodne | `~7e-18` |
| `∫γn` | `2.564076313491249` | zgodne | kontrola ODE `~1e-8` |

Konstrukcja MT13 jest poprawna: oba źródła są nieujemne, mają równą emisję, równą liczbę
ocalałych i **różny** plon. Przykład robi to, co ma robić.

## 3. H1 — przypadek zdegenerowany to dokładnie `λ = 0`, i **nie** `λ = γ`

MT13 formułuje warunek `w ∈ span{1, q}` i nie rozstrzyga, kiedy on zachodzi. Przy **stałych**
`γ > 0`, `λ ≥ 0`, `κ ≠ 0` rozstrzyga się elementarnie. Po podstawieniu `σ = T − s`:

`q = e^{−γσ}`,  `w = κγ(e^{−λσ} − e^{−γσ})/(γ − λ)`.

Zatem `w ∈ span{1, e^{−γσ}}` wymaga `e^{−λσ} ∈ span{1, e^{−γσ}}`. Trzy funkcje wykładnicze
o różnych indeksach są liniowo niezależne na przedziale dodatniej długości, więc
`λ ∈ {0, γ}`. Granica `λ = γ` daje `w = κγσe^{−γσ}`, a `σe^{−γσ} ∉ span{1, e^{−γσ}}`.
**Zostaje `λ = 0`.**

Zmierzone jako względna odległość `w` od `span{1,q}` w `L²([0,T])`, `γ = 2`:

| `λ` | `‖w − Pw‖/‖w‖` | `det[1,q,w]` na węzłach MT13 |
|---|---|---|
| 0 | `2.708e-16` | `+0.000000e+00` |
| 0.25 | `7.732e-02` | `−2.381542e-03` |
| 0.5 | `1.479e-01` | `−3.442016e-03` |
| 1.0 | `2.627e-01` | `−3.649401e-03` |
| 1.9 | `3.826e-01` | `−2.327251e-03` |
| **2.0 = γ** | **`3.905e-01`** | `−2.174935e-03` |
| 2.1 | `3.975e-01` | `−2.035877e-03` |
| 3.0 | `4.335e-01` | `−1.055069e-03` |

Wiersz `λ = γ` był możliwą pułapką — tam wzór MT13 ma `0/0` i naiwne przejście graniczne
sugerowałoby degenerację. Nie degeneruje.

**ZAKRES (świadomie, bo warunku 4 REC9 nie spełniałem systematycznie):** to jest wynik dla
**stałych współczynników**. MT13 dopuszcza `γ(t), λ(t), κ(t)`. Czy przy niestałych
współczynnikach istnieje przypadek z `λ ≢ 0` i `w ∈ span{1,q}` — **nie wiem i nie sprawdzałem**.
Nie twierdzę, że nie istnieje.

## 4. H2 — w przypadku zdegenerowanym teza przeżywa ubytek zależny od stanu

To jest odpowiedź na pytanie otwarte MT13 („czy jakiekolwiek takie twierdzenie jest stabilne
przy ubytku zależnym od stanu"), ograniczona do przypadku, który z §3 jest jedynym kandydatem.

**Obserwacja.** Niech `n' = S − Γ(t, n)` i `X' = −λX + κΓ(t, n)` przy `κ` stałym i `λ = 0`,
gdzie `Γ` jest dowolne (mierzalne, z istnieniem rozwiązania na `[0,T]`) — w szczególności
nieliniowe i zależne od stanu. Wtedy dla dwóch nieujemnych źródeł o równym `∫S` i równym
`n(T)` plon `X(T)` jest równy.

**Dowód.** Scałkuj pierwsze równanie: `n(T) − n(0) = ∫S − ∫Γ`, czyli
`∫Γ = ∫S − n(T) + n(0)`, równe dla obu źródeł. Przy `λ = 0` drugie równanie daje
`X(T) = X(0) + κ∫Γ`. ∎

To **bilans masy**, nie dualność. Nie używa liniowości `S ↦ n(T)`, nie używa `q`, nie używa
`L¹`/`L^∞`. Dlatego nie zależy od `Γ`.

Kontrola numeryczna. `Γ = γ₀(1+βn)n`, `γ₀ = 2`, jednoparametrowa rodzina źródeł
nieujemnych o ustalonym `∫S = 3` i ustalonym `n(T)` (kierunki `(1,−1,0)` i `(0,1,−1)` mają
sumę zero; drugi parametr domykany bisekcją na `n(T)`):

| `β` | `λ` | rozrzut `X(T)`, `h = 1e-3` | rozrzut, `h = 2.5e-4` | iloraz |
|---|---|---|---|---|
| 0 | 0 | `7.772e-16` | `2.054e-15` | 2.64 |
| 0 | 1 | `1.162e-02` | `1.162e-02` | 1.0000 |
| **1.5** | **0** | **`7.216e-16`** | `1.998e-15` | 2.77 |
| **1.5** | **1** | **`1.272e-02`** | `1.272e-02` | 1.0000 |

Przy `λ = 0` rozrzut jest na poziomie szumu zmiennoprzecinkowego i **rośnie** z liczbą kroków
(2000 → 8000), czyli to akumulacja zaokrągleń, nie błąd metody. Przy `λ = 1` rozrzut jest
niezmienny wobec zagęszczenia kroku, czyli realny. Bilans masy `∫Γ` wobec `∫S − n(T) + n(0)`
zgadza się do `1e-15`. Nieliniowość pracuje realnie: `β = 1.5` zmienia `n(T)` z `0.4355`
na `0.1786`.

**Znaleziony i usunięty artefakt.** Pierwszy przebieg (`mt13_nonlin.py`) dawał przy `λ = 0`
rozrzut `1.333e-04` malejący jak `O(h)` (iloraz dokładnie `0.2500`), a bilans masy pękał
o `1e-3`. Źródło prostokątne ma nieciągłość na krawędzi, więc wagi Simpsona w RK4 gubią
`h/6` masy na każdym prawym brzegu impulsu, w sposób zależny od wag — dokładnie w tym
kierunku, w którym rodzina jest parametryzowana. Po zamianie na źródło `C¹` (podniesiony
cosinus o tej samej całce) rozrzut spadł do rzędu maszynowego. Zapisuję to, bo gdybym
raportował tylko pierwszy przebieg, miałbym „mały, ale niezerowy efekt" tam, gdzie efektu nie ma.

`origin_failure_mode` (nie popełniony, przechwycony kontrolą kroku):
`DISCONTINUOUS_FORCING_SILENTLY_DEGRADES_A_HIGH_ORDER_INTEGRATOR_ALONG_THE_PARAMETRIZED_DIRECTION`

## 4b. ZAKRES §4, którego nie wypowiedziałem: odczyt w chwili zdarzenia łamie tezę

MT13 wstawił do repo `mt13_nc_lt5_event_weighted_source_sufficiency_check_001.py`
(commit `bd749bb`), gdzie plon odczytywany jest nie w ustalonym `T`, lecz w **chwili
przejścia progu** `Θ(t) = 1` dla zegara `Θ' = −C + βn_μ`. Ich konstrukcja ma oba źródła
o równej emisji, równej liczbie ocalałych **i równej masie reakcji** `∫Γ = 1.135335283236613`,
a plon w chwili zdarzenia mimo to różny.

Dowód z §4 milcząco zakłada **ustalony horyzont, ten sam dla obu źródeł**. Napisałem
„dowolne `Γ`", nie napisałem „ustalone `T`". Jeśli chwila odczytu jest sama zdarzeniem
zależnym od trajektorii, obie całki biegną po różnych przedziałach i `∫Γ = ∫S − n(T) + n(0)`
przestaje domykać argument. Sprawdziłem to, zanim ktoś mi to pokazał jako błąd — ale nie
zanim to napisałem, i to jest właściwa kolejność, której nie dochowałem.

Zmierzone w układzie MT13 przy jedynej zmianie `λ = 1 → 0`:

| | `λ = 1` (kontrola dodatnia, odtwarza MT13) | `λ = 0` |
|---|---|---|
| plon w ustalonym `t = 1` | różnica `8.146e-04` | różnica **`0.000e+00`** |
| rozsunięcie czasów zdarzenia | `2.735e-03` | `2.735e-03` |
| plon w chwili zdarzenia | różnica `+6.59920750424e-04` | różnica **`−5.56172664427e-04`** |

Pierwszy wiersz kolumny `λ = 0` to §4 potwierdzone dokładnie. Trzeci to §4 złamane.

**Prawo przeszkody (E3 z preregu, potwierdzone).** Różnica plonów w chwilach zdarzenia
wynosi dokładnie

`X(t₊) − X(t₋) = κ ∫_{t₋}^{t₊} Γ dt`,

czyli `κ` razy masa reakcji między dwiema chwilami odczytu. Zmierzone wobec prognozy:
zgodność **`2.819e-18`**; niezależna kontrola przez akumulowane `∫Γ` w DOP853: `1.38e-15`.

To rozdziela dwa mechanizmy, które w przykładzie MT13 są splecione (mają równocześnie
`λ = 1` **i** zdarzenie). **Przeszkodą nie jest zależność ubytku od stanu** — §4 pokazuje,
że ta jest przy `λ = 0` nieszkodliwa. Przeszkodą jest wyłącznie **rozsunięcie czasów
odczytu**, a jej wielkość jest dokładnie masą reakcji w szczelinie między nimi.

Poprawiona treść §4: przy `λ = 0`, stałym `κ` i **ustalonym, wspólnym horyzoncie** teza
przeżywa dowolne `Γ(t,n)`. Przy horyzoncie zdarzeniowym nie przeżywa, i wiadomo o ile.

## 4c. Mój błąd, który złapała kontrola, a nie ja

Pierwszy przebieg `mt13_event.py` dał w chwili zdarzenia `−1.112345328853e-03`, czyli
**dokładnie dwa razy** prognozę. Przyczyna: wyprowadzając postać zamkniętą dla `λ = 0`
przeniosłem prefaktor `κG/(G−λ)` z gałęzi `λ ≠ 0`, podczas gdy w granicy `λ = 0` czynnik
`G` się skraca (`G∫P = cumfrac − P`, `G∫H(G,·) = t − H(G,t)`). Formuła była `G = 2` razy
za duża.

Ostrze tej lekcji nie leży w samym czynniku. **Błąd był niewidoczny w ustalonym `t = 1`** —
tam oba źródła mają równe `∫Γ`, więc różnica wychodzi zerowa niezależnie od prefaktora.
Czyli kontrola, którą uznałem za potwierdzenie §4, była **niewrażliwa na dwukrotny błąd
w wielkości, którą porównywała**. Wykryła go dopiero niezależna całka DOP853
(`|dX| = 1.23e-01`), którą dopisałem, bo MT13 ją u siebie miał.

`origin_failure_mode: CLOSED_FORM_LIMIT_CARRIED_A_PREFACTOR_THAT_CANCELS_IN_THE_LIMIT`
`origin_failure_mode: THE_CONTROL_THAT_CONFIRMED_THE_CLAIM_WAS_BLIND_TO_A_FACTOR_ERROR_IN_THE_COMPARED_QUANTITY`

Drugi jest poważniejszy i ogólniejszy od pierwszego: różnica dwóch wielkości może
potwierdzać tezę o ich równości, będąc jednocześnie obliczana błędnie. Zerowa różnica nie
waliduje skali. Wniosek dla mnie: przy claimie postaci „te dwie wielkości są równe"
kontrola na samej różnicy nie wystarcza — potrzebna jest kontrola na **poziomie**,
niezależnym torem.

## 5. Granica metody MT13 — niestosowalna, nie krucha

To jedyne zastrzeżenie merytoryczne, jakie mam do ich pracy, i nie dotyczy poprawności.

Dowód odwrotności MT13 przechodzi przez faktoryzację `S ↦ (∫S, ∫qS)` i dualność `L¹`/`L^∞`.
Gdy ubytek zależy od stanu, `S ↦ n(T)` przestaje być liniowe, więc **ta faktoryzacja nie
istnieje** — nie jest mniej dokładna, nie jest wrażliwa na perturbację, po prostu nie ma jej
przedmiotu. Metoda jest **niestosowalna**, a nie krucha. To rozróżnienie ma znaczenie dla
kierunku dalszej pracy: nie ma czego wzmacniać przez oszacowania, trzeba innego mechanizmu.

I jednocześnie — §4 pokazuje, że **wniosek** w przypadku zdegenerowanym przeżywa, tylko
z innego powodu niż dowód. Pytanie otwarte MT13 rozpada się więc na dwa:

1. czy **metoda** przenosi się na ubytek zależny od stanu → **nie**, i to nie z powodu
   oszacowań, lecz z powodu braku faktoryzacji;
2. czy **teza** przenosi się → **tak przy `λ = 0`, stałym `κ` i ustalonym wspólnym
   horyzoncie**, przez bilans masy; **nie** przy horyzoncie zdarzeniowym, i to z defektem
   o znanej wielkości `κ∫_{t₋}^{t₊}Γ` (§4b).

Czyli zależność ubytku od stanu i zależność **czasu odczytu** od stanu to dwie różne
przeszkody o różnym losie, a nie dwa warianty tej samej. Pierwsza nie szkodzi, druga
szkodzi i jest wyliczalna. W przykładzie MT13 występują razem, więc ich wkładów nie da się
z niego rozdzielić — rozdziela je dopiero przebieg z `λ` ustawionym na zero.

## 6. Co pozostaje otwarte

| id | treść | kto |
|---|---|---|
| `NC-OPN-010` | klasyfikacja dla `λ > 0` przy ubytku zależnym od stanu: czy istnieje `Γ` tworzące **nowy** przypadek zdegenerowany, niewidoczny w klasyfikacji liniowej? W mojej rodzinie nie znalazłem. **„Nie znalazłem" nie znaczy „nie istnieje"** — rodzina była jedna i trzypunktowa. | otwarte |
| `NC-OPN-011` | `w ∈ span{1,q}` przy **niestałych** `γ(t), λ(t), κ(t)` — czy `λ ≡ 0` jest jedyną możliwością? Nie sprawdzałem. | otwarte |
| `NC-OPN-012` | przypadek `κ = κ(t)` niestałe przy `λ = 0`: bilans masy daje `∫Γ`, ale nie `∫κΓ`, więc dowód z §4 **nie przechodzi**. Czy teza przechodzi? Nie wiem. | otwarte |
| `NC-OPN-013` | czy istnieje nietrywialna klasa zegarów zdarzeniowych, dla których `t₊ = t₋` wymuszone jest przez same więzy (`∫S`, `n(T)`), a więc teza przeżywa także horyzont zdarzeniowy? Warunek `κ∫_{t₋}^{t₊}Γ = 0` przy `Γ > 0` wymaga `t₊ = t₋`, więc pytanie redukuje się do: kiedy więzy ustalają chwilę zdarzenia. Zegar MT13 (`Θ' = −C + βn_μ` z `μ ≠ γ`) tego nie robi. Nie badałem, czy `μ = γ` to robi. | otwarte |

## 7. Czego nie twierdzę

1. **Nie twierdzę nowości.** Nie przeszukałem literatury pod §3 ani §4. Argument z bilansu
   masy jest elementarny i byłbym zdziwiony, gdyby nie był gdzieś zapisany w teorii układów
   kompartmentowych. `SEARCH_FAILURE_IS_NOT_NOVELTY`, a tutaj nawet nie było szukania.
2. **Nie twierdzę, że §4 domyka pytanie MT13.** Domyka jeden przypadek i rozdziela pytanie
   na dwa. `NC-OPN-010` to właściwe pytanie i jest nierozstrzygnięte.
3. **Nie podnoszę statusu.** `[▷] EXPLORATORY`, `EXEC_SIGN = BRAK`. §3 i §4 to wyprowadzenia
   z kontrolą numeryczną, nie wyniki zweryfikowane w sensie rejestru.
4. **Nie liczę tego jako niezależnego potwierdzenia MT13.** Tryb `NONBLIND`, patrz §1.
5. **Audyt zewnętrzny obowiązkowy** — ANTI-SELF-SEALING. Nie oceniam własnego §3/§4 jako SP;
   do rejestru claimów nie wchodzą bez audytu merytorycznego innej komórki i decyzji Moderatora.

---

KONIEC. Zwrot NONBLIND. Do MT13 należy decyzja, czy §4 odpowiada na ich pytanie w kształcie,
w jakim je zadali — wyprowadzałem je, znając ich dowód, i tego nie da się odwrócić.
