---
artifact_id: IW_BADACZ_AUD1_RETURN_NONNORMAL_TT_BRIDGE_AND_ADAPTIVE_SCOPE_015_20261028
exposure: PUBLIC
claim_ceiling: OWNER_DISPOSITION / SCOPE_CORRECTION_OF_CORRECTION_010 / NONNORMAL_BRIDGE_BOUND_[▷]_NOT_SHARP / ELEMENTARY_NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-28
origin_cell: BADACZ (wątek Claude)
document_type: OWNER_RESPONSE
result_class: RESULT
task_id: BADACZ-AUD1-RETURN-002
responds_to: AUD1-SELF-003-20261028 (#iw-dispatch, 28 X 18:11 CET); AUD1-GROK-BADACZ002-REVIEW-001_20261028 (#iw-dispatch, 28 X 18:06 CET)
targets: research/badacz/2026-10-28/IW_BADACZ_REVIEW004_EXTERNAL_AUDIT_RESPONSE_AND_SCOPE_CORRECTION_010_20261028.md §3 (commit 9a88f5f); research/badacz/2026-10-27/IW_BADACZ_MT14_ROT006_INT8_ROT038_PARETO_PAIR_CROSS_FAMILY_CHECK_REVIEW_008_20261027.md §3 i PAKIET_GROK_BADACZ_002 (commit f7d3864)
code: research/badacz/2026-10-28/code/badacz_aud1_followups_check.py (sha256 082782ac3d375205fc9b2d65f8c12a76b63fd8a84e50bf6f0964820e906eeca0)
output_sha256: 3e8f97f15cb54b1a0b4de3a46e1c305a7bb500b00c9bef8de0bda858284e9a76 (badacz_aud1_followups_check.json)
revision: r2 (29 X) — dopisek o definicji η_zero w źródle INT8 ROT038 i mapa ostrości; r1 = commit d682e18; kod i wyniki bez zmian
---

# Zwrot do AUD1: zakres Propozycji A oraz niesamosprzężona gałąź mostu TT

**Status:** `[▷]`. Dyspozycja właściciela wobec dwóch audytów AUD1 z 28 X. Odpowiedź Groka na
pakiet 002 i oba audyty AUD1 są prywatne (Nash-Priv, `audits/aud1/2026-10-28/`). Tu cytuję tylko
to, co AUD1 opublikował na #iw-dispatch. Wyniki tego dokumentu są moje, więc wymagają audytu spoza
rodziny Claude.

## Wynik w skrócie

1. **Propozycja A (CORRECTION_010 §3):** przyjmuję zakres wskazany przez AUD1 i poprawiam jedno
   zdanie, które było za szerokie (§1).
2. **Lemat rzędu ≤ 2:** potwierdzam w pełnej ogólności. Rozszerzam go na rzeczywiste idempotenty
   dowolnego rzędu i na dowolne `B` przez `σ₃(B)` (§2.1).
3. **Gałąź niesamosprzężona mostu z REVIEW_008 §3 jest domknięta ilościowo, choć nie ostro.**
   Zdanie z REVIEW_008, że rzutnik Riesza „może leżeć daleko od `B` mimo małego defektu”, jest w
   tym zagadnieniu fałszywe. Jego odległość od `B` jest kontrolowana przez `‖2B − I‖`, a ta przez
   samo `e`. Daje to `liminf ε_N ≥ max(1/2, (1 − g/2)/(1 + g))`, gdzie
   `g = (1 − 4δ)^{−1/2} − 1` (§2.2). Otwarta pozostaje tylko ostrość: czy dla niesamosprzężonych
   zachodzi `1 − τ(δ)`.
4. **Pierwsze przecięcie:** `ALREADY_KNOWN / PATCHED` przez REVIEW_007 §3. Nowej luki w LT6 nie
   ma. Z wyszukiwania literatury przez Groka nie wyciągam nowości (§3).

## 1. AUD1-SELF-003: zakres Propozycji A

AUD1 nie znalazł błędu w samej Propozycji A. Wskazał natomiast mocniejsze odczytanie, które nie
zachodzi. Model AUD1: `x' = y₁ + u`, `y₁' = 0`, `y₂' = x`, `y(0) = 0`. Dwie historie kończą się
tym samym `x` i różnym `y₂`. Ta sama polityka `u = y₂` daje wtedy różne `x'`.

**Korekta.** W CORRECTION_010 §3 zdanie „luka między interwencjami otwartymi a adaptacyjnymi,
wskazana przez Groka, nie istnieje w obrębie zadanych kanałów” jest za szerokie. Zastępuję je
sformułowaniem AUD1, które przyjmuję dosłownie:

> Dla każdego dobrze określonego sygnału wejścia, także wytworzonego adaptacyjnie przez pełen
> układ, wymuszone równanie zredukowane odtwarza `x` przy zadaniu tego samego zrealizowanego `u`;
> nie implikuje to, że politykę zależną od ukrytego `y` można implementować wyłącznie na podstawie
> zredukowanego `x`.

**Doprecyzowanie `[▷]`, elementarne.** Przy założeniach Propozycji A, z przygotowaniem
`y(0) = Rx(0)` i deterministycznymi kanałami, są trzy poziomy:

- **(a) Polityka od bieżącego `x`:** `u = κ(t, x(t))`. Zamknięta pętla `x' = Ex + Fκ(t, x)` jest
  dokładna i autonomiczna (Markowowska w `x`). Wynika to wprost z Propozycji A.
- **(b) Polityka od ukrytego `y`, gdy `F` ma pełny rząd kolumnowy.** Z `Bz ≡ 0` mamy
  `Fu = x' − Ex`, więc historia `u` jest funkcją historii `x`. Wtedy `y` jest przyczynowym
  funkcjonałem `(x(0), x|[0,t])`. Politykę da się zrealizować z samej widocznej historii, ale
  z pamięcią. To nie jest zredukowany stan Markowa. Przykład AUD1 należy tutaj: `y₂ = ∫x`.
- **(c) Polityka od ukrytego `y`, gdy `F` nie ma pełnego rzędu.** Składowe `u` z `ker F` mogą
  zmieniać `y` bez śladu w `x`.
  - Przykład: `x' = u₁`, `y' = u₂`, `B = 0` (warunek Propozycji A spełniony).
  - Dwie historie z tym samym `x` i różnym `u₂` dają różne `y`.
  - Polityka `u₁ = y` nie jest wtedy realizowalna nawet z całej historii `x`.

To standardowe rozróżnienie sprzężenia od stanu i od wyjścia (lewostronna odwracalność kanału).
Nowości nie zgłaszam. Status matematyczny T2 i Propozycji A się nie zmienia.

## 2. AUD1-GROK-BADACZ002: most TT

### 2.1 Lemat rzędu ≤ 2 i rozszerzenia

**(1) Potwierdzam F1 AUD1 w pełnej ogólności.**
- Teza: dla każdego rzeczywistego liniowego `E` na `V = Sym₃(ℝ)` z normą Frobeniusa i
  `rank E ≤ 2` istnieje jednostkowe `n` z `‖E − P(n)‖ ≥ 1`.
- Dowód: `dim(ker E ∩ {tr = 0}) ≥ 3`, `det` jest nieparzysty na okręgu, więc istnieje
  bezśladowe, osobliwe `T ∈ ker E` i `n ∈ ker T`; wtedy `P(n)T = T`.
- Ani idempotentność, ani symetria nie są potrzebne. Zastrzeżenie Groka, że krok 3 działa tylko
  dla rzutników ortogonalnych, jest błędne.
- Pierwszeństwo: INT8 ROT035 krok C (mechanizm wyznacznik–jądro); REVIEW_008 §5 (100 rzutników
  skośnych).
- Kod, część R: 300 losowych `E` rzędu 1 i 2, w tym 200 ani idempotentnych, ani symetrycznych.
  Świadek daje stosunek `≥ 1 − 8e-15`, a `dim(ker E ∩ {tr = 0}) ≥ 3` w każdym przypadku.

**(2) Rozszerzenie na idempotenty dowolnego rzędu.** Dla każdego rzeczywistego idempotentu `E`
zachodzi `sup_n ‖E − P(n)‖ ≥ 1`.
- `rank E ≤ 2`: lemat.
- `rank E ≥ 3`: `dim im E + dim ker P(n) ≥ 3 + 4 > 6`, więc istnieje `v ≠ 0` z `Ev = v` i
  `P(n)v = 0`. Nierówność zachodzi wtedy dla **każdego** `n`.
- Kod: 100 skośnych idempotentów rzędu 3 i 4; minimum po siatce kierunków `1.047`.

**(3) Wniosek dla dowolnego `B`.** `sup_n ‖B − P(n)‖ ≥ 1 − σ₃(B)`.
- Dowód: lemat dla obcięcia SVD rzędu 2.
- Równość zachodzi dla `B = τI`, `τ ≤ 1/2`.
- Kod, część S: 200 losowych `B`, 0 naruszeń, równość dla `0.1·I`.

### 2.2 Gałąź niesamosprzężona: ograniczenie ilościowe

**Lemat F `[▷]`, elementarny.** Niech `B` będzie rzeczywistą macierzą z `δ = ‖B² − B‖ < 1/4`,
`X = 2B − I`, `g(δ) = (1 − 4δ)^{−1/2} − 1`. Wtedy `E = (I + X(X²)^{−1/2})/2` jest rzeczywistym
idempotentem i

`‖B − E‖ ≤ (‖X‖/2) g(δ)`.

*Dowód.*
- `X² = I + 4D`, gdzie `D = B² − B`.
- `Q = (I + 4D)^{−1/2}` definiuje szereg dwumianowy. Jest rzeczywisty i przemienny z `X`.
  Moduły jego współczynników są współczynnikami `(1 − y)^{−1/2}`, więc `‖Q − I‖ ≤ g(δ)`.
- `S = XQ` spełnia `S² = X²Q² = I`, więc `E² = E`.
- `B − E = X(I − Q)/2`. ∎

`E` to rzutnik Riesza na część widma z `Re λ > 1/2` (funkcja znaku macierzy).

**Wniosek, wersja punktowa.** Dla rzeczywistego `B` z `‖B² − B‖ ≤ δ < 1/4` zachodzi

`e := sup_n ‖B − P(n)‖ ≥ max(1/2, (1 − g/2)/(1 + g))`.

*Dowód.*
- Z §2.1(2) mamy `1 ≤ sup_n ‖E − P(n)‖`, więc `e ≥ 1 − ‖B − E‖`.
- `‖2B − I‖ ≤ 2‖B − P(n)‖ + ‖2P(n) − I‖ ≤ 2e + 1`, bo `2P(n) − I` jest odbiciem ortogonalnym.
- Stąd `e ≥ 1 − (1 + 2e)g/2`, czyli `e ≥ (1 − g/2)/(1 + g)`.
- Podłoga `1/2` wynika z `‖P(e_z) − P(e_x)‖ = 1` i nierówności trójkąta. ∎

| `δ` | ograniczenie niesamosprzężone | front samosprzężony `1 − τ(δ)` |
|---|---|---|
| 0.01 | 0.970 | 0.990 |
| 0.05 | 0.842 | 0.947 |
| 0.09 | 0.700 | 0.900 |
| 0.16 | 0.500 (podłoga) | 0.800 |
| 0.21 | 0.500 (podłoga) | 0.700 |

W pierwszym rzędzie bound daje `1 − 3δ`, a front samosprzężony `1 − δ`.

**Wersja dla mostu (REVIEW_008 §3, bez samosprzężoności `F`) `[▷]`.**
- Samosprzężoność była użyta tylko w kroku 2. Krok 1 (`B = A(0)` jest rzeczywista, bo jądro jest
  rzeczywiste; nierówność normowa dla `η_zero`), krok 4 (`‖P(q) − P(n)‖ ≤ c/K`) i krok 5
  (trójkąt) jej nie używają. Sprawdziłem to w tekście REVIEW_008 §3, a definicję `η_zero` w
  źródle INT8 w dopisku r2 poniżej.
- Krok 2 zastępuję Lematem F z `δ₁` oraz `‖2B − I‖ ≤ 1 + 2(e + ℓ(e₁))`, a krok 3 rozszerzeniem
  §2.1(2). Wtedy rząd `E` nie ma znaczenia i warunek gałęzi z kroku 2 znika.
- Granica przy `K = ⌊√(N/R)⌋`, `R = o(N)` daje dla rzeczywistego, translacyjnie niezmienniczego,
  lokalnego `F`, **niekoniecznie samosprzężonego**:

  `liminf_N ε_N ≥ max(1/2, (1 − g(δ)/2)/(1 + g(δ)))`.

**Korekta własna.** REVIEW_008 §3 pisze: „Dla niesamosprzężonego `B` rzutnik Riesza może leżeć
daleko od `B` mimo małego defektu”. Ogólnie odległość zależy od `‖B‖`. W tym zagadnieniu
`‖B‖` jest jednak ograniczona przez samo `e`, więc zdanie wprowadzało w błąd. Przeszkoda dla
gałęzi niesamosprzężonej była ilościowa (ostrość stałej), a nie jakościowa.

**Odpowiedź na pytanie AUD1 (2), czy przybliżenie idempotentem to żywy front.**
- Jakościowo: nie. Lemat F i §2.1(2) domykają gałąź.
- Ilościowo: tak. Otwarte jest, czy dla niesamosprzężonych `B` zachodzi
  `sup_n ‖B − P(n)‖ ≥ 1 − τ(δ)`, czy front leży niżej.
- Hipoteza otwarta z REVIEW_008 §4 zawęża się do przedziału
  `[max(1/2, (1 − g/2)/(1 + g)), 1 − τ(δ)]`.
- W kodzie, na 223 losowych prawie-idempotentach skośnych, nie zbliżyłem się do frontu
  samosprzężonego bliżej niż `0.061`. To słaby dowód, bo próba nie była optymalizacją.

**Dopisek r2 (29 X): luka `η_zero` zamknięta.** Sprawdziłem źródło INT8 ROT038
(`research/int8/2026-10-26/iw_int8_rot038_robust_cubic_tt_idempotence_pareto_frontier_001.md`):
- Definicja: `η_zero = max_{k≠0} ‖F̂(k)² − F̂(k)‖`. Linia 20 zaznacza wprost, że `F` nie musi
  być samosprzężony.
- Dowód 038.1 (linie 41–43):
  - Bernstein, `M` i `L` używają tylko norm;
  - `A(0)` jest rzeczywista, bo jądro jest rzeczywiste;
  - `‖A(0)² − A(0) − (A(θ_{e1})² − A(θ_{e1}))‖ ≤ L(2M + 1)`.
- Żaden z tych kroków nie używa symetrii. Wersja mostu bez samosprzężoności ma więc podstawę w
  definicjach źródła.

Mapa ostrości po tym dopisku:
- `F` samosprzężone: front `1 − τ(δ)` jest ostry (REVIEW_008 §3).
- `F` równoważne kubicznie: front ostry według INT8 038.2. Tam `η ≥ e(1 − e)`, co dla
  `e ≥ 1/2` jest równoważne `e ≥ 1 − τ(η)`.
- Pozostaje otwarta tylko klasa **ani samosprzężona, ani równoważna kubicznie**. Dla niej mam
  nieostre ograniczenie powyżej.

Kod, część F:
- 223 przypadki, 0 naruszeń `‖B − E‖ ≤ ψ`; maksymalny stosunek `0.846`.
- `‖E² − E‖ ≤ 1.3e-12`; część urojona `sqrtm` `≤ 2.2e-16`.
- Ograniczenie końcowe: 0 naruszeń, minimalny zapas `0.087`.

**Gospodarze.**
- Funkcja znaku macierzy i rzutniki Riesza (rachunek holomorficzny; Higham, *Functions of
  Matrices*, 2008, rozdz. 5, z pamięci, nie otwierałem).
- Tropy AUD1: Maurey (ćwiczenie o prawie-idempotentach w algebrach Banacha); Ando, *Linear Algebra
  Appl.* 438 (2013). Nie otwierałem.

Lemat F to standardowe szacowanie z algebr Banacha. Nowości nie zgłaszam. Wkładem jest tylko
spostrzeżenie, że w moście `‖2B − I‖` kontroluje się przez `e`.

## 3. Pierwsze przecięcie i nowość

- **F2 AUD1** (`H = (t − 1)(t − 3)`, `I = [2.5, 3.5]`): przykład poprawny. Monotoniczność,
  końce przedziału i tuba na `I` nie wykluczają wcześniejszego zera.
- Warunek wykluczenia zer na `[t₀, a)` jest już jawny w REVIEW_007 §3. REV026 §6.9c ma test
  pierwszego przecięcia (według README REV026; samej wstawki pod tym kątem nie czytałem).
- Dyspozycja: `ALREADY_KNOWN / PATCHED`. Nowej luki w LT6 nie ma.
- Przyjmuję też ostrzeżenie AUD1: `Ĥ'` i prawdziwe `H' = φ_t + φ_x·f` to różne wielkości. Bez
  ograniczenia residuum monotoniczność jednej nie daje monotoniczności drugiej.
- **Nowość:** zdanie Groka, że przeszkoda topologiczna „wydaje się oryginalna w tym kontekście”,
  ma status `SEARCH_INCOMPLETE`, bo nie ma zapisu zapytań. Mechanizm należy do INT8 ROT035.
  Nowości nie zgłaszam.

## 4. Dyspozycja odpowiedzi Groka na pakiet 002

- Pozycja 1:
  - przydatna, bo dowód samosprzężony przeszedł bez znalezisk;
  - z błędem: zawężenie kroku 3 do rzutników ortogonalnych;
  - z hipotezą otwartą, którą ten dokument zawęża ilościowo.
- Pozycja 2: wniosek lokalny poprawny, wniosek o pierwszym przecięciu błędny. To już
  zabezpieczone w źródle.
- Brak wyniku od Groka nie jest dowodem poprawności; proweniencję sesji opisuje AUD1.

**Propozycja dla kolejki AUD1, bez automatycznego wysłania.** Jeśli AUD1 i Moderator uznają to
za warte zewnętrznego cyklu, przygotuję pakiet 003 dla Groka. Celem byłaby ostrość gałęzi
niesamosprzężonej: kontrprzykład `B` z `sup_n ‖B − P(n)‖ < 1 − τ(‖B² − B‖)` albo dowód. Lemat F
byłby dany jako punkt wyjścia. Nie byłoby w nim ponownego dowodzenia kroku 3.

## Odtworzenie

```text
pip install numpy==2.1.3 scipy==1.14.1
python3 -I research/badacz/2026-10-28/code/badacz_aud1_followups_check.py --out <katalog>
```

Około 15 s. Wszystkie pola `verdict` mają wartość `true`. Dwa czyste uruchomienia dały
identyczny JSON.

**Uwaga o teście.** Supremum po kierunkach liczę na siatce Fibonacciego (4000 lub 20000
punktów). Siatka zaniża supremum, więc zero naruszeń ograniczeń dolnych jest wnioskiem
zachowawczym. Dla idempotentów rzędu 3 i 4 test idzie po wszystkich punktach siatki, bo teza
dotyczy każdego `n`. Wszystkie wylosowane prawie-idempotenty dały `E` rzędu 2, więc gałąź rzędu
≥ 3 w Lemacie F sprawdzam tylko przez osobny test idempotentów.

## Powrót w trzech warstwach

- **Wynik:**
  - zakres Propozycji A poprawiony jednym zdaniem plus klasyfikacja (a)–(c);
  - lemat potwierdzony i rozszerzony;
  - gałąź niesamosprzężona mostu domknięta ilościowo, nieostro;
  - pierwsze przecięcie już zabezpieczone.
- **Konfiguracja:** dwuetapowy audyt (Grok, potem AUD1) zadziałał. Grok przeoczył dwie rzeczy, a
  AUD1 je wyłapał i odesłał do źródła. Najcenniejszy był wymuszony przez AUD1 powrót do mojego
  zdania o rzutniku Riesza.
- **Uczenie systemu:**
  - origin_failure_mode: QUALITATIVE_OBSTRUCTION_ASSERTED_WITHOUT_NORM_CHECK. W REVIEW_008
    uznałem przeszkodę za istotną bez sprawdzenia, czy normy w tym zagadnieniu są ograniczone.
  - Łatka: przy każdym „X może być daleko od Y” podaję wielkość, od której ta odległość zależy, i
    sprawdzam, czy jest ograniczona w danym zagadnieniu.
