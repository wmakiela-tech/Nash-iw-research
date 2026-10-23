# IW_NC_LT4_FOUR_MISSING_WITNESSES_006_20261018


<!-- IW_CONFORMANCE_BLOCK v1 (docs/IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md §2.7) -->
```text
artifact_id          : IW_NC_LT4_FOUR_MISSING_WITNESSES_006_20261018
exposure             : PUBLIC_SAFE
canonical_body_path  : research/nc/2026-10-18/IW_NC_LT4_FOUR_MISSING_WITNESSES_006_20261018.md
source_revision      : rozwiazywane przez `git log -- <canonical_body_path>`
bw_event_or_pending  : GITHUB_PENDING_BW_INGEST
claim_ceiling        : NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE / MODEL_AGREEMENT_IS_NOT_PROOF / SEARCH_FAILURE_IS_NOT_NOVELTY
hold                 : BRAK
```

ARTIFACT_ID: IW_NC_LT4_FOUR_MISSING_WITNESSES_006_20261018
KOMÓRKA: NC — zewnętrzna komórka Claude
OBIEKT: monografia, DRIVE 1cn97_kO65BcJRRWQrvrL9fKlEYBT3PHg6BJItn1Q4FQ
POPRZEDZA: 005 (audyt warstwy non-mapów), DRIVE 1q9csyp4dBTYoZiA9kNmBL-lr0O7iFghB
STATUS: [▷] / EXEC_SIGN = BRAK / NO_CANON / NO_NOVELTY / SOURCE_FIRST
KOD: `holes.py` sha256 a20b843fa9fa812f426e2ac819da4e14f09ed0fbf55919fab58992f4cc760d76
AUTORSTWO I DECYZJA O WŁĄCZENIU: LT4.
**AUDYT ZEWNĘTRZNY OBOWIĄZKOWY** per ANTI-SELF-SEALING — wszystkie cztery konstrukcje są moje.

---

## 0. Co to jest

Audyt 005 znalazł w monografii **dwanaście non-mapów bez świadka**. Zamiast je zostawić jako
listę, konstruuję świadków. Poniżej **cztery z dwunastu**, każdy zweryfikowany.

Nie twierdzę nowości matematycznej dla żadnego. Trzy są elementarne. Czwarty (§1.10) stoi na
klasycznej nieoznaczoności problemu momentów Stieltjesa i jest podręcznikowy w swojej części
źródłowej — nowy jest tylko sposób, w jaki domyka zdanie monografii.

---

## 1. §1.10 — „Nie wystarczy domagać się analityczności tylko dla `t > 0`"

**To jest najważniejszy z czterech**, bo monografia stawia tę granicę jawnie i zostawia ją bez
świadka, a jej własne Twierdzenie 8 jej nie pokrywa: tamtejsze `K` jest nośnikowo zwarte w `t`,
więc nie jest analityczne. Potrzeba świadka, w którym `K` **jest** analityczne na `(0,∞)`.

**Konstrukcja.** `Y = L²(0,∞)`, `D` = mnożenie przez `−λ` (samosprzężone, generuje półgrupę
kontrakcji `C₀`). Niech

    f(x) = exp(−(ln x)²/2) / (x√(2π))        (gęstość lognormalna)
    g(x) = f(x) · sin(2π ln x)

i połóżmy `c(x) = |g(x)|^{1/2}`, `b(x) = sgn(g(x))|g(x)|^{1/2}`, czyli `b·c = g`. Wtedy
`C: ℝ → Y`, `Cα = αc`, oraz `B: Y → ℝ`, `By = ∫by`, są **ograniczone**, bo `∫|g| < ∞`;
zmierzone `‖B‖ = ‖C‖ = 0.797884561`.

**Momenty znikają — dowód, nie numeryka.** Podstawienie `x = e^u` daje `g(x)dx = w(u)sin(2πu)du`
z `w` gęstością `N(0,1)`, więc dla `U ~ N(0,1)`

    ∫ x^k g(x) dx = E[e^{kU} sin(2πU)] = Im E[e^{(k+2πi)U}] = Im e^{(k+2πi)²/2}
                  = e^{(k²−4π²)/2} · sin(2πk) = 0   dla każdego całkowitego k ≥ 0.

Zatem `B D^k C = (−1)^k ∫x^k g dx = 0` dla każdego `k`. Dziedziny: `λ^k c ∈ L²` wymaga
`∫x^{2k}|g| < ∞`, co zachodzi (zmierzone: `4.70e+00`, `1.90e+03`, `4.18e+07`, `5.03e+13` dla
k=1..4), więc `ran C ⊂ ⋂_k D(D^k)` i wszystkie momenty istnieją jako operatory ograniczone.

**A jednak `K ≢ 0`.** `K(t) = ∫e^{−xt}g(x)dx` jest transformatą Laplace'a niezerowej miary
znakowanej, więc nie znika tożsamościowo (injektywność transformaty). Zmierzone, dwiema
niezależnymi parametryzacjami zgodnymi do **11 cyfr znaczących**:

| t | K(t) |
|---|---|
| 0.25 | `+8.494625717906e-07` |
| 0.50 | `−6.649378925222e-06` |
| 1.00 | `+2.636590987127e-05` |
| 2.00 | `−5.938476146366e-05` |
| 4.00 | `+8.152203988058e-05` |
| 8.00 | `−7.017116724974e-05` |

`max|K|` na `[0.1, 20]` wynosi `8.153e-05`; znak zmienia się wielokrotnie, co wyklucza odczyt
„to szum kwadratury". Zgodność obu parametryzacji: `1.3e-09` … `1.1e-11` względnie.

**Analityczność i spłaszczenie w zerze.** `K` jest holomorficzna na `{Re t > 0}` (różniczkowanie
pod całką; `x^k e^{−xt}|g|` całkowalne). Jednocześnie
`K^{(k)}(t) = ∫(−x)^k e^{−xt} g dx → (−1)^k ∫x^k g dx = 0` przy `t → 0⁺` (zbieżność majoryzowana).
Zmierzone dla k = 0,1,2,3 przy t = 1, 0.1, 0.01, 0.001:

| k | t=1.0 | t=0.1 | t=0.01 | t=0.001 |
|---|---|---|---|---|
| 0 | `+2.64e-05` | `−4.06e-08` | `+6.08e-14` | `+5.54e-16` |
| 1 | `+2.87e-05` | `−1.20e-06` | `−1.63e-11` | `+1.09e-16` |
| 2 | `−5.07e-04` | `+4.57e-05` | `−5.61e-08` | `+1.56e-13` |
| 3 | `−6.38e-04` | `+5.37e-03` | `−4.96e-05` | `+1.03e-09` |

**Teza świadka.** Istnieje układ blokowy z ograniczonymi `B`, `C` i samosprzężonym `D`
generującym półgrupę kontrakcji, w którym `K(t) = Be^{tD}C` jest **holomorficzna na całej otwartej
prawej półpłaszczyźnie**, wszystkie jej pochodne przedłużają się ciągle do `t = 0⁺` z wartością
dokładnie zero, a mimo to `K ≢ 0`. Zatem żądanie analityczności dla `t > 0` nie przywraca
kryterium momentowego — brakującym składnikiem jest jednoznaczność rozwinięcia **w zerze**,
dokładnie jak mówi tekst, i teraz jest na to świadek.

**Prior art, przeciw sobie.** Nieoznaczoność lognormalnego problemu momentów jest klasyczna
(Stieltjes; rodzina `f(x)(1 + ε sin(2π ln x))` o identycznych momentach). Wkładem jest wyłącznie
przeniesienie jej na nośnik `Be^{tD}C` i zauważenie, że daje świadka mocniejszego niż
Twierdzenie 8. **NO_NOVELTY.**

---

## 2. §7.8 — „splatanie rachunku funkcyjnego nie daje splatania różniczek"

Monografia stwierdza, że Twierdzenia 7.4 i 7.5 rozdzielają dwa wymagania i że „pierwsze nie daje
drugiego", bez świadka. INT7 analizował te kontrakty; świadek poniżej jest minimalny.

**Konstrukcja.** Jeden kompleks dwustopniowy, `H⁰ = H¹ = ℂ²`, `d = diag(1,2)`. Wtedy
`Δ⁰ = d*d = diag(1,4)` i `Δ¹ = dd* = diag(1,4)`, oba o **widmie prostym**, więc operator
przemienny z całym rachunkiem funkcyjnym jest dokładnie operatorem diagonalnym. Biorę
`J₀ = diag(1,1)`, `J₁ = diag(1,2)`.

**Splatanie spektralne zachodzi dla każdego ograniczonego mnożnika borelowskiego**: zmierzony
maksymalny defekt `‖J_k f(Δ^k) − f(Δ^k)J_k‖` po 2000 losowych mnożnikach wynosi **`0.000e+00`**.

**Splatanie łańcuchowe zawodzi**: `dJ₀ = diag(1,2)`, `J₁d = diag(1,4)`, czyli
`‖dJ₀ − J₁d‖ = 2.000000`.

Świadek jest mocniejszy, niż wymaga teza, bo oba laplasjany są **identyczne** — splatanie
spektralne zachodzi w najsilniejszej możliwej postaci, a mimo to różniczka się nie przenosi.

---

## 3. §3.10 — „równość zbiorów trajektorii nie musi oznaczać równości praw na historiach"

**Konstrukcja.** Dwa łańcuchy Markowa na `{0,1}`, start jednostajny:
`P₁ = [[1/2,1/2],[1/2,1/2]]`, `P₂ = [[2/3,1/3],[1/3,2/3]]`.

**Ten sam nośnik:** każda z `2^{n+1}` historii ma dodatnie prawdopodobieństwo w obu układach
(sprawdzone równością zbiorów nośników dla n ≤ 18; minimalne prawdopodobieństwa przy n = 10
wynoszą `4.883e-04` i `8.468e-06`).

**Różne prawa:** odległość całkowitego wahania między prawami historii:

| n | 1 | 2 | 4 | 6 | 10 | 14 | 18 |
|---|---|---|---|---|---|---|---|
| TV | 0.166667 | 0.194444 | 0.280093 | 0.336634 | 0.409919 | 0.477832 | 0.536399 |

Świadek jest kompletny już przy `n = 1` (TV = 1/6 > 0). **Nie wykazałem, że TV → 1** — rośnie
monotonicznie do 0.536 przy n = 18 i dalej nie liczyłem; granica wynika z dodatniej dywergencji
na krok, której nie policzyłem. Zapisuję to jako niezrobione, nie jako wynik.

---

## 4. §1.7 — redukcja jądra względem celu nie daje minimalności zamkniętej odpowiedzi

Tekst mówi, że redukcja przez `(D, C, τB)` „nie oznacza jeszcze minimalności całej zamkniętej
odpowiedzi `x₀ ↦ τx(t)`, w której uczestniczy także `A`". Świadek pokazuje mocniejszą rzecz:
taka redukcja **zmienia** `τx(t)`.

**Konstrukcja.** `X = Y = ℝ²`, `τ = (1,0)`,

    A = [[0,1],[0,0]]      (x₂ → x₁)
    B = [[0,0],[1,0]]      (mod ukryty 1 → x₂)
    C = [[1,0],[0,0]]      (x₁ wzbudza mod 1)
    D = diag(−0.3, −5.0)

Wtedy `τB = (0,0)`, więc jądro ważone celem znika tożsamościowo: zmierzone `τBD^kC = [[0,0]]`
dokładnie dla k = 0,1,2,3. Minimalną realizacją funkcji zerowej jest sektor **zerowymiarowy**,
więc redukcja oparta na `(D, C, τB)` usuwa cały sektor ukryty.

**A jednak cel to widzi**, bo `B ≠ 0` wprowadza mod do `x₂`, a `A` przenosi `x₂` do `x₁ = τx`:

| t | `τx(t)` pełne | `τx(t)` po redukcji | różnica |
|---|---|---|---|
| 0.5 | 1.020095749284 | 1.000000000000 | `2.01e-02` |
| 1.0 | 1.156159488982 | 1.000000000000 | `1.56e-01` |
| 2.0 | 2.231537673295 | 1.000000000000 | `1.23e+00` |
| 4.0 | 13.749338068084 | 1.000000000000 | `1.27e+01` |

Przy `t = 4` redukcja, która zachowuje jądro ważone celem **dokładnie**, myli się o czynnik 13.7.

Mechanizm jest tym samym, co w Kontrprzykładzie 3 rozdziału 1 (`ker τ` nie jest `A`-niezmiennicze),
zastosowanym do pytania o minimalność — co jest argumentem za umieszczeniem świadka przy §1.7
i odesłaniem do Kontrprzykładu 3, a nie za nowym obiektem.

---

## 5. Stan dwunastki po tym zwrocie

Zamknięte świadkiem: **§1.10, §7.8, §3.10, §1.7** — cztery.
Pozostaje osiem, z czego:
- **§5.2** (stałe `σ_E`) — gospodarz istnieje w literaturze, do zacytowania, nie do konstruowania;
- **§3.6** (minimalność przybliżona w nieskończonym wymiarze) — kandydat na gospodarza, nie szukałem;
- §2.8, §2.9, §3.5, §4.7, §5.10, §7.2 — sześć bez znanego mi świadka, z czego §2.9 i §3.5 są
  bliźniacze, a §7.2 zawiera **trzy** nieimplikacje w jednym zdaniu.

---

## 6. Czego nie twierdzę

1. **Nowości matematycznej — nigdzie.** §1.10 stoi na klasycznej nieoznaczoności Stieltjesa;
   §7.8, §3.10, §1.7 są elementarne.
2. **Nie przedowodziłem §1.10 w pełnym rygorze funkcjonalnoanalitycznym.** Holomorficzność na
   `Re t > 0` i przejście graniczne pochodnych uzasadniłem różniczkowaniem pod całką i zbieżnością
   majoryzowaną, ale nie wypisałem obu argumentów formalnie. To rutynowe i to jest luka.
3. **TV → 1 w §3.10 nie zostało wykazane**, zob. §3.
4. **Czy te świadki są warte umieszczenia w tekście, osądza LT4.** Świadek poprawny może być
   zbyt ciężki na przypis.
5. **Wszystkie cztery konstrukcje są moje**, więc żadnej nie mogę sobie wystawić. Audyt zewnętrzny
   obowiązkowy: §1 do DS (to jedyny nietrywialny), §2–§4 do kogokolwiek z dostępem do dwóch linii
   rachunku.
6. Nie dotykałem niczego opartego na moich wynikach J3 — nadal `[▷]`, w audycie zewnętrznym.

---

KONIEC. Status [▷]. EXEC_SIGN brak.
