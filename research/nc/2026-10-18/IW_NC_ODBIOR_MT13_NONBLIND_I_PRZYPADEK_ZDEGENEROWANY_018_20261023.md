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
PREREG: `PREREG_MT13_NONLIN.md` 58209d2b3233bc8147b371fb2b448eb38f304bd63fee4ff78ea6b0da4a7a0b9b

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
2. czy **teza** przenosi się → **tak w jedynym przypadku, w którym jest nietrywialna
   przy stałych współczynnikach** (`λ = 0`), przez bilans masy.

## 6. Co pozostaje otwarte

| id | treść | kto |
|---|---|---|
| `NC-OPN-010` | klasyfikacja dla `λ > 0` przy ubytku zależnym od stanu: czy istnieje `Γ` tworzące **nowy** przypadek zdegenerowany, niewidoczny w klasyfikacji liniowej? W mojej rodzinie nie znalazłem. **„Nie znalazłem" nie znaczy „nie istnieje"** — rodzina była jedna i trzypunktowa. | otwarte |
| `NC-OPN-011` | `w ∈ span{1,q}` przy **niestałych** `γ(t), λ(t), κ(t)` — czy `λ ≡ 0` jest jedyną możliwością? Nie sprawdzałem. | otwarte |
| `NC-OPN-012` | przypadek `κ = κ(t)` niestałe przy `λ = 0`: bilans masy daje `∫Γ`, ale nie `∫κΓ`, więc dowód z §4 **nie przechodzi**. Czy teza przechodzi? Nie wiem. | otwarte |

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
