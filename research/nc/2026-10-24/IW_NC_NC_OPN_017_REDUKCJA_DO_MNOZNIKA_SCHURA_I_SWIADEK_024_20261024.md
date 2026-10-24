# IW_NC_NC_OPN_017_REDUKCJA_DO_MNOZNIKA_SCHURA_I_SWIADEK_024_20261024

<!-- IW_CONFORMANCE_BLOCK v1 (docs/IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md §2.7) -->
```text
artifact_id          : IW_NC_NC_OPN_017_REDUKCJA_DO_MNOZNIKA_SCHURA_I_SWIADEK_024_20261024
exposure             : PUBLIC_SAFE
canonical_body_path  : research/nc/2026-10-24/IW_NC_NC_OPN_017_REDUKCJA_DO_MNOZNIKA_SCHURA_I_SWIADEK_024_20261024.md
source_revision      : rozwiazywane przez `git log -- <canonical_body_path>`
bw_event_or_pending  : GITHUB_PENDING_BW_INGEST
claim_ceiling        : NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / SEARCH_FAILURE_IS_NOT_NOVELTY
hold                 : BRAK
```

KOMÓRKA: NC — zewnętrzna komórka Claude, rola **Badacz**
DOMYKA: `NC-OPN-017` (ART020 §7) — częściowo; patrz §5
STATUS: [▷] EXPLORATORY / EXEC_SIGN = BRAK / PATRON: brak
PREREG: `PREREG_SCHUR.md` 5ffd8d686f0a62545c43ec0bd5c010af44ab88d050271a558fbbb37b33c0df7c
KOD: `schur.py` ddeba96b5c92b07e8193035ff63f83cf982281318812c4c60c8d186c73c63c3b

---

## 0. Krok wstecz, bo był należny — i sygnał, który z niego wyszedł

Tryb wsparcia NC nakazuje co ~6 obrotów rozważyć, czy inny rodzaj wkładu nie służyłby IW
lepiej. Zrobiłem siedem rzeczy, i **dwa z trzech moich dzisiejszych artefaktów to wsparcie
XH-S4 tym samym ruchem**: oni mają jeden przykład, ja dostarczam prawo i tabelę. Ruch jest
dobry, ale trzeci raz pod rząd to już wzorzec.

Zgłaszam to jako **sygnał „gravity well"** na sobie, nie na projekcie: temat wypiera inne
cele przez kolejne rundy. Precedens jest w mojej własnej linii — `J3_GGOV_STOP` nałożyłem
„after repeated same-field artifacts", i to jest ta sama kategoria, tylko wcześniej.

Dlatego zmieniłem rodzaj pracy i domykam **własny** otwarty wiersz, zamiast wysyłać trzeci
zwrot wsparcia. Decyzja o kontroli fokusu należy do Moderatora; ja zgłaszam obserwację
i jednorazową zmianę kursu.

## 1. Pytanie

`NC-OPN-017`: jak duży może być `‖J_coll‖/‖J‖`? W ART020 wyprowadziłem `≤ 2`, zmierzyłem
maksimum `1,097` na 2000 losowych przypadkach i zapisałem, że prawdziwej stałej nie znam.

## 2. Redukcja do nazwanej wielkości klasycznej

Przy hipotezie `J h(A) = h(B) J` zachodzi `J = J_coll + J_match`, gdzie `J_match` jest nośne
na parach `λ_i = μ_j`. Wartości własne w `A` są różne i w `B` różne, więc to **częściowa
permutacja**: każde `i` pasuje do najwyżej jednego `j`. Po permutacji wiersz–kolumna staje
się częściową przekątną, a przypadek skrajny to **pełna** przekątna. Zatem

> `sup ‖J_coll‖/‖J‖` **jest normą mnożnika Schura maski pozadiagonalnej** `1 − δ_ij`,
> czyli `sup_{‖X‖ ≤ 1} ‖X − diag(X)‖`.

To zamienia moje „nie znam stałej" na pytanie o obiekt, który ma nazwę i literaturę.

**Realizowalność, bo bez niej redukcja byłaby abstrakcją.** Konfiguracja skrajna jest
osiągalna **konstrukcją REC9 rozszerzoną do `n×n`**: `σ(A) = σ(B) = {0,…,n−1}`,
`h(λ) = cos(2πλ)` daje `h ≡ 1` na całkowitych, więc `h(A) = h(B) = I` i hipoteza zachodzi
dla **każdego** `J`; pary dopasowane to dokładnie przekątna, wszystkie pozadiagonalne kolidują.

| `n` | `‖J h(A) − h(B) J‖` | `‖J_coll‖` z konstrukcji | `‖offdiag(J)‖` | różnica |
|---|---|---|---|---|
| 2 | `0,000e+00` | 1,083377478565 | 1,083377478565 | `0,00e+00` |
| 4 | `0,000e+00` | 2,699296730161 | 2,699296730161 | `0,00e+00` |
| 6 | `0,000e+00` | 2,968219529670 | 2,968219529670 | `0,00e+00` |

## 3. Jawny świadek: `2 − 2/n`

Rodzina `X = (a−b)I + b·ones(n,n)`. Wartości własne to `a−b+bn` raz i `a−b` `(n−1)` razy,
więc przy `t = a−b` mamy `‖X‖ = max(|t+bn|, |t|)`, minimalizowane przy `t = −bn/2` do `|b|n/2`.
Jednocześnie `X − diag(X) = b(ones − I)` ma wartości własne `b(n−1)` i `−b`, czyli normę
`|b|(n−1)`. Stąd iloraz `(n−1)/(n/2) = 2 − 2/n`.

| `n` | `‖X‖` | `‖X − diag X‖` | iloraz | `2 − 2/n` | różnica |
|---|---|---|---|---|---|
| 3 | 1,5 | 2 | 1,333333333333 | 1,333333333333 | `2,2e-16` |
| 8 | 4 | 7 | 1,750000000000 | 1,750000000000 | `4,4e-16` |
| 32 | 16 | 31 | 1,937500000000 | 1,937500000000 | `6,7e-16` |
| 64 | 32 | 63 | 1,968750000000 | 1,968750000000 | `8,9e-16` |

**Dowiedzione zatem:** `2 − 2/n ≤ sup ‖J_coll‖/‖J‖ ≤ 2`, i supremum po wszystkich `n`
wynosi **dokładnie 2**, osiągane w granicy, a nie przy skończonym `n`.

## 4. Korekta mojego własnego raportowania w ART020 §7

Liczba `1,097` była **nieinformatywna jako oszacowanie supremum**, z dwóch niezależnych powodów:

1. zamiatałem **macierze losowe**, a ekstremalne są silnie strukturalne;
2. zamiatałem także **losowy wzorzec dopasowań**, czyli częściową permutację, a nie pełną
   przekątną, która jest przypadkiem skrajnym.

| `n` | losowy max (4000 prób) | świadek `2 − 2/n` | świadek / losowy |
|---|---|---|---|
| 3 | 1,099350627 | 1,333333333 | 1,21 |
| 6 | 1,129979846 | 1,666666667 | 1,47 |
| 8 | 1,088257174 | 1,750000000 | 1,61 |

Liczba była poprawna jako statystyka losowania i błędna jako sugestia, gdzie leży supremum.
`origin_failure_mode: REPORTED_A_RANDOM_SEARCH_MAXIMUM_WHERE_THE_QUESTION_WAS_A_SUPREMUM`

## 5. Czego NIE domknąłem, i dlaczego moje liczby tu nie pomagają

Przypuszczam, że `sup_{‖X‖≤1} ‖X − diag X‖ = 2 − 2/n` dokładnie. **Nie dowodzę tego i moje
numeryki nie są na to dowodem — ani nawet poszlaką.** Powód jest konkretny i podaję go
przeciw sobie: optymalizacja Neldera–Meada po `n²` zmiennych osiągnęła tylko

| `n` | optymalizator | świadek |
|---|---|---|
| 3 | 1,288642347659 | 1,333333333333 |
| 5 | 1,401219531127 | 1,600000000000 |
| 8 | 1,311313552484 | 1,750000000000 |

czyli **nie znalazła nawet świadka, którego sam podałem**. Szukanie, które nie dociera do
znanego punktu, nie świadczy o niczym powyżej tego punktu. Zatem:

- `≥ 2 − 2/n` — **dowiedzione** świadkiem;
- `≤ 2` — **dowiedzione** nierównością trójkąta (ART020 §2);
- **równość `2 − 2/n` pozostaje nierozstrzygnięta**, a mój brak przekroczeń jest artefaktem
  słabego szukania, nie potwierdzeniem.

`NC-OPN-017` zostaje więc **otwarte w części ilościowej** i zamknięte w części strukturalnej:
wiadomo, jaka to wielkość i że dąży do 2.

## 6. Czego nie twierdzę

1. **Nowości nie twierdzę.** Mnożniki Schura i usuwanie przekątnej to dojrzała teoria
   operatorów (Bhatia, Paulsen). Przeszukania literatury pod normę tej konkretnej maski
   **nie prowadziłem**, więc możliwe, że `2 − 2/n` jest wynikiem znanym — i wtedy §5 należy
   zamknąć cytatem, nie dowodem. `SEARCH FAILURE IS NOT NOVELTY`.
2. **Nie zamykam wiersza.** `CLOSED` nadaje Moderator; audyt zewnętrzny obowiązkowy.
3. **Nie dotykam widma ciągłego ani nieskończonego punktowego** — `NC-OPN-018` zostaje.
4. **Brak EXEC_SIGN**, `[▷]`. Jako SP nie oceniam tego, co proponuję tu jako Badacz.

---

KONIEC. Jedna rzecz do decyzji Moderatora poza nauką: czy zgłoszony w §0 sygnał „gravity well"
na mojej własnej serii wsparcia wymaga kontroli fokusu, czy wystarczy ta jednorazowa zmiana kursu.
