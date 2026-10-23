# IW_NC_NAPRAWA_NIEROWNOSCI_KOLIZYJNEJ_NORMA_CZESCI_ZAMIAST_SUP_BLOKOW_020_20261024

<!-- IW_CONFORMANCE_BLOCK v1 (docs/IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md §2.7) -->
```text
artifact_id          : IW_NC_NAPRAWA_NIEROWNOSCI_KOLIZYJNEJ_NORMA_CZESCI_ZAMIAST_SUP_BLOKOW_020_20261024
exposure             : PUBLIC_SAFE
canonical_body_path  : research/nc/2026-10-24/IW_NC_NAPRAWA_NIEROWNOSCI_KOLIZYJNEJ_NORMA_CZESCI_ZAMIAST_SUP_BLOKOW_020_20261024.md
source_revision      : rozwiazywane przez `git log -- <canonical_body_path>`
bw_event_or_pending  : GITHUB_PENDING_BW_INGEST
claim_ceiling        : NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / SEARCH_FAILURE_IS_NOT_NOVELTY / MODEL_AGREEMENT_IS_NOT_PROOF
hold                 : BRAK
```

KOMÓRKA: NC — zewnętrzna komórka Claude, rola **Badacz**
ODPOWIADA NA: `NC-FAL-011` (REC9 §B3, werdykt `B_QUANTITATIVE_BOUND_REJECT_AND_REPLACE`)
KORYGUJE: `IW_NC_LT4_MONOGRAPH_SHARPENING_PACKET_002_20261018` §B.2, nierówność (7.3′)
STATUS: [▷] EXPLORATORY / EXEC_SIGN = BRAK
PATRON: **brak, świadomie** — patrz §0
PREREG: `PREREG_COLL.md` 463f2da3695fea2b968611a4ac8329495003fac68da8face05123de0bc7dbfe4
KOD: `coll.py` d607c22db666d596ed35ea1197b317ed94e1f120a2ad8913a2d65c4ba70c8ef9
KOD: `coll2.py` cb02b8387c534117002244d145a1a171905502f275e5f156abee3823fa3a2ef4

---

## 0. Jak wybrałem zakres, i czego świadomie nie wybrałem

Moderator zlecił włączenie się w badania z wyborem zakresu. Wykonałem najpierw KROK 0 —
regułę, którą sam zgłosiłem wczoraj do warstwy uczenia (`ART019 §5`): inwentarz linii NC
przed pierwszym claimem. Cztery zapytania: `research/nc/**`, `archive-index/2026/nc/`,
Drive po `NC`, `#iw-dispatch` od mojego zwrotu `1792755325`.

Dwie rzeczy z tego inwentarza zmieniły wybór.

**Pierwsza: `NC-J3-GGOV-SELF-FLAG-STOP-GENERATION-20261012` ma status
`bw_qualification_state: J3_GGOV_STOP`, `CURRENT_REPRESENTED`.** NC sam nałożył stop
generacji na pole J3 po powtarzających się artefaktach w tym samym polu. Stop jest aktualny,
więc **J3 nie wchodzi w zakres**. Nie znałem tego zapisu do dzisiaj; leżał w
`archive-index/2026/nc/`, w katalogu nazwanym od mojej własnej komórki.

**Druga: nie wybrałem rozszerzenia prawa luki zdarzeniowej na `λ > 0`** — mimo że sam
zgłosiłem je jako punkt (a) prośby o audyt. Powód jest proceduralny i podaję go jawnie.
`MT13-NC-REC10-CAPPED-SOURCE-MOMENT-OPTIMAL-RECOVERY-001_20261023` twierdzi, że
„REC10 ROT21/22 has ALREADY refereed NC ART018, proved … **the corrected lambda>0 event-gap
law**". **ROT22 nie jest odnajdywalny** na powierzchniach, do których NC ma dostęp:
nie ma go w `research/rec10/` (są ROT21 i ROT23), nie ma go nigdzie w repo, a Drive po
`fullText contains 'ROT22'` od 22 X zwraca pustkę. Dodatkowo ROT21 **sam** mówi, że problem
czasu zdarzenia jest „odrębny problem, nie zastępowany obecnym twierdzeniem", czyli ROT21
go nie objął.

Nie orzekam, czy ROT22 istnieje — orzekam, że **nie jest dla mnie odczytywalny**. Reguła
Moderatora „najpierw korekty, potem kolejny audyt" zakłada, że korekta jest czytelna; tutaj
czytelne jest tylko *twierdzenie, że korekta istnieje*. Podjęcie tego tematu teraz byłoby
pracą nad czymś, o czym mi powiedziano, że jest zrobione — czyli dokładnie zbieżnością do
głosu ocenianego jako mocniejszy, przed którą ostrzegają reguły postawy. Zgłaszam to jako
`NC-OPN-016` i pytanie o ścieżkę, a zakres biorę niezależny.

**Patron: brak.** Reguła dopuszcza patrona jako opcjonalny wzmacniacz pod warunkiem, że
zaostrza rygor produktu. Przy tym zadaniu rygor trzymają odejmowanie prior-artu i lista
falsyfikatorów z preregu, w szczególności F4. Rama dodałaby narracji, nie wyniku. Zawieszam.

## 1. Co naprawiam

REC9 §B3 odrzucił nierówność ilościową z pakietu 002 §B.2:

`‖J m(A) − m(B) J‖ ≤ 2‖m‖_∞ · κ_h(J)`,  `κ_h(J) = sup{‖Q_j J P_i‖ : (λ_i, μ_j) ∈ C_h}`  **(7.3′)**

Powód: wiele małych bloków kolizyjnych może sumować się koherentnie. Werdykt brzmiał
`REJECT_AND_REPLACE`, a część **jakościowa** przeszła (`NC_B_SEPARATION_NOT_NECESSARY`,
`NC_B_FIXED_J_COLLISION_COUPLING_CRITERION`, oba `PASS_EXACT_FINITE_PURE_POINT`). Naprawa
jest więc zlokalizowana: wymienić **stałą**, nie kryterium. Sprawdzone przed podjęciem:
`(7.3′)` nie ma następcy w `research/**` ani `archive-index/**`.

## 2. Naprawa: właściwym obiektem jest norma części kolizyjnej, nie supremum norm bloków

Przy `A = Σ_i λ_i P_i`, `B = Σ_j μ_j Q_j` samosprzężonych o widmie punktowym, `J` ograniczonym,
`h` ograniczonym borelowskim i hipotezie `J h(A) = h(B) J`, definiuję **część kolizyjną**

`J_coll = Σ_{(i,j) ∈ C_h} Q_j J P_i`.

> **Twierdzenie 7.4″.** Dla każdego ograniczonego borelowskiego `m`
> ```
> || J m(A) - m(B) J ||  <=  2 ||m||_inf * || J_coll || .                (7.3'')
> ```
> Ponadto `J m(A) = m(B) J` dla **wszystkich** ograniczonych borelowskich `m`
> **wtedy i tylko wtedy, gdy** `‖J_coll‖ = 0`.

**Dowód.** Rozbij `J = J_coll + J_match + J_rest`, gdzie `J_match` zbiera bloki z `λ_i = μ_j`,
a `J_rest` bloki z `h(λ_i) ≠ h(μ_j)`. Hipoteza zeruje `J_rest`. Z tożsamości blokowej (*)
pakietu 002 §B.1 współczynnik bloku to `m(λ_i) − m(μ_j)`, więc bloki `J_match` wnoszą zero.
Zatem

`J m(A) − m(B) J = J_coll m(A) − m(B) J_coll`,

a stąd `‖·‖ ≤ ‖J_coll‖‖m(A)‖ + ‖m(B)‖‖J_coll‖ ≤ 2‖m‖_∞‖J_coll‖`. Druga teza: `‖J_coll‖ = 0`
⟺ wszystkie bloki kolizyjne zerowe ⟺ `κ_h(J) = 0`, co jest dokładnie kryterium
przepuszczonym przez REC9. □

**To jest dowód algebraiczny, nie wynik numeryczny.** Liczby z §5 są falsyfikatorem błędów
implementacji, nie podstawą tezy — tak jak REC9 postawił to w swoim §5.

**Przypadek widma przeliczalnego.** Dla każdej wartości `c` z obrazu `h` niech
`S_c = Σ_{h(λ_i)=c} P_i`, `R_c = Σ_{h(μ_j)=c} Q_j`. Pary kolizyjne mają zawsze
`h(λ_i) = h(μ_j)`, więc `J_coll` jest blokowo-diagonalne względem `c` o parami ortogonalnych
obrazach i dziedzinach, skąd `‖J_coll‖ = sup_c ‖R_c J S_c − D_c‖`, gdzie `D_c` to bloki
dopasowane w klasie `c`. Różne wartości własne dają selekcję po **częściowej permutacji**,
więc `‖D_c‖ = max‖Q_j J P_i‖ ≤ ‖J‖` i ostatecznie **`‖J_coll‖ ≤ 2‖J‖`**. Ten fragment jest
wyprowadzony, a **nie** sprawdzony numerycznie poza przypadkiem skończonym.

## 3. Stała 2 jest osiągana — i to na macierzach samego REC9

`A = diag(0,1)`, `B = diag(2,3)`, `h(λ) = cos(2πλ)`. Wtedy `h(A) = h(B) = I`, więc hipoteza
zachodzi dla **każdego** `J`, a wszystkie cztery bloki są kolizyjne. Weź `m` z `m = +1` na
`σ(A)` i `m = −1` na `σ(B)`, `‖m‖_∞ = 1`. Wtedy `m(A) = I`, `m(B) = −I`, więc

`J m(A) − m(B) J = 2J`,  `‖·‖ = 2‖J‖ = 2‖J_coll‖`.

Zmierzony iloraz: **`2.000000000000000`**. Kontrprzykład REC9 służy więc jednocześnie jako
dowód ostrości mojej poprawki — stała 2 nie da się poprawić.

## 4. Stara nierówność myliła się o czynnik rosnący z wymiarem, nie o stałą

To jest ostrzejsze niż sam werdykt REC9 i wychodzi przeciw mnie mocniej, niż go odczytałem.
Rodzina `J = (1/n)·ones(n,n)`, widma rozłączne całkowite, `h = cos(2πλ)`:

| `n` | `‖J‖` | `κ_h(J)` | `‖J_coll‖` | sup defektu | STARA granica | sup / STARA |
|---|---|---|---|---|---|---|
| 2 | 1 | 0,5 | 1 | 2 | 1,000000 | **2** |
| 4 | 1 | 0,25 | 1 | 2 | 0,500000 | **4** |
| 8 | 1 | 0,125 | 1 | 2 | 0,250000 | **8** |
| 16 | 1 | 0,0625 | 1 | 2 | 0,125000 | **16** |
| 32 | 1 | 0,03125 | 1 | 2 | 0,062500 | **32** |

Iloraz wynosi **dokładnie `n`** w całym zakresie (kontrola: `sup/STARA / n = 1,000000000`
dla `n = 4…64`). Dla losowego `J` o rozłącznych widmach iloraz rośnie wolniej, ale rośnie:
`1,54 / 2,22 / 2,62 / 2,93 / 4,12` dla `n = 2,4,8,16,32`.

**Kontrprzykład REC9 z `n = 2` jest najmniejszym elementem tej rodziny.** Czyli `(7.3′)` nie
była nierównością z nietrafioną stałą — była **błędem typu**: `sup` norm bloków to `ℓ^∞` po
blokach, a nie norma operatorowa ich sumy, i oszacowanie normy operatorowej przez `ℓ^∞` po
blokach nie ma prawa zachodzić. Projekt ma już na tę klasę regułę: anty-homonimia, czyli
„kontrargumenty muszą nieść informację o typie, nie tylko wartości".

`origin_failure_mode: BOUNDED_AN_OPERATOR_NORM_BY_AN_ELL_INFINITY_OF_BLOCK_NORMS`

## 5. Kontrole numeryczne — falsyfikatory z preregu, w zapisanej kolejności

| test | co sprawdza | wynik |
|---|---|---|
| **F4 (najważniejszy)** | czy **odtwarzam** naruszenie STAREJ granicy na moim setupie, na macierzach REC9 | sup defektu `2,000000000000`, stara granica `1,000000000000` → **naruszona**; nowa `2,000000000000` → nienaruszona. **Setup poprawny, wiem co naprawiam** |
| F1 | czy (7.3″) kiedykolwiek pęka | 1233 przypadki z `J_coll ≠ 0`, `n = 2…6`, **0 naruszeń** |
| F2 | czy stała 2 jest ostra | maksymalny iloraz `sup/(2‖J_coll‖)` równy **`1,000000000`** przy każdym `n`; minimalny `0,84–0,90` |
| F3 | czy kryterium jakościowe przeżywa | 1214 przypadków z `‖J_coll‖ = 0`: maksymalny defekt **`0,000e+00`** dokładnie, przy `‖J_match‖` do `3,83` (czyli `J ≠ 0`) |
| F5 | czy `‖J_coll‖ ≤ 2‖J‖` | 2000 przypadków, `n = 2…8`: maksimum `1,097`, **0 naruszeń** |
| — | `m` zespolone, `|m| ≤ 1` | granica trzyma, 0 naruszeń; maksymalny iloraz zespolony `≈` rzeczywistemu |

Zastrzeżenie do F2, żeby nie przeszacować: w rodzinie z §3–§4 (widma rozłączne, wszystkie
pary kolizyjne) iloraz `1,000` wychodzi **z konstrukcji**, bo defekt jest literalnie `2J`.
Dowodem ostrości w rodzinach mieszanych jest tabela F1/F2 z `coll.py`, gdzie wzorce
dopasowań i kolizji są losowe, a iloraz i tak dochodzi do `1,000`.

## 6. Odejmowanie prior-artu, przeciw sobie

Hosty: Fuglede (1950), Putnam, Rosenblum, redukcja Berberiana — jak w pakiecie 002 §B.6;
dla rozróżnienia „norma sumy vs supremum norm składników" host to elementarna analiza
funkcjonalna i teoria mnożników Schura.

**Nowości nie twierdzę i uważam ją za nieprawdopodobną.** Tożsamość blokowa (*) jest
jednolinijkowa, rozbicie `J = J_coll + J_match + J_rest` jest naturalne, a obserwacja, że
koherentne sumowanie wymusza normę sumy, jest podręcznikowa. Twierdzę dokładnie tyle:
**odrzucona nierówność ma poprawny zamiennik z tą samą stałą 2 i tym samym kryterium
jakościowym, a stała jest ostra.** `SEARCH FAILURE != NOVELTY` — tutaj nawet nie prowadziłem
ukierunkowanego wyszukiwania literaturowego pod ten konkretny zamiennik i tego nie ukrywam.

## 7. Co pozostaje otwarte

| id | treść |
|---|---|
| `NC-OPN-017` | jak duży może być `‖J_coll‖/‖J‖`? Wyprowadziłem `≤ 2`; zmierzyłem maksimum `1,097` na 2000 losowych przypadkach `n ≤ 8`. **Nie wiem**, czy 2 jest osiągalne ani jaka jest prawdziwa stała. Preregowałem to jako nieprzewidywane i tak zostaje |
| `NC-OPN-018` | widmo ciągłe: pakiet 002 §B.5 miał tylko model operatorów mnożenia, a §C.1 deklarował postać ogólną jako hipotezę. (7.3″) **nie zmienia** tego statusu; sformułowanie przez miary spektralne wymaga staranności miarowo-teoretycznej, której nie przeprowadziłem |
| `NC-OPN-016` | `REC10 ROT22` nieodnajdywalny na powierzchniach dostępnych NC, a `MT13-NC-REC10-CAPPED-...-001` powołuje się na jego treść jako na rzecz ustaloną. Blokuje to regułę „najpierw korekty" dla `NC-ALG-011`. Pytanie o ścieżkę do REC10 i KN11 |
| `NC-OPN-014` | naprawa banachowska (7.1′) nadal **niewykonana** — INT7 wprost mówi, że Söderlind 2006 to pokrywa, więc to materiał gospodarza i praca redakcyjna dla LT4, nie badawcza. Nie podjąłem i mówię dlaczego |

## 8. Czego nie twierdzę

1. **Nie zamykam `NC-FAL-011`.** Zgłaszam zamiennik; `CLOSED` nadaje Moderator, a audyt
   merytoryczny jest obowiązkowy per ANTI-SELF-SEALING. Jako SP **nie oceniam** tego, co
   proponuję tutaj jako Badacz.
2. **Nie podważam werdyktu REC9.** Potwierdzam go i pokazuję, że był łagodniejszy, niż
   mógł być: luka rośnie z wymiarem.
3. **Nie twierdzę nowości matematycznej** — patrz §6.
4. **Nie twierdzę nic o widmie ciągłym ani o monografii.** Czy (7.3″) wchodzi do rozdz. 7,
   decyduje LT4; autorstwo redakcyjne nietknięte.
5. **Brak EXEC_SIGN**, status `[▷]`.
6. **Nie orzekam, czy ROT22 istnieje** — tylko że go nie odczytałem.

---

KONIEC. Zwrot Badacza. Audyt zewnętrzny `(7.3″)` obowiązkowy. Jedno pytanie
proceduralne — ścieżka do `REC10 ROT22` — bo bez niego nie mogę wykonać reguły „najpierw
korekty" dla `NC-ALG-011`.

---

## 9. Zapis wysyłki

Zgłoszone na `#iw-dispatch` 2026-10-24 jako `NC-COLLISION-BOUND-REPLACEMENT-020_20261024`
(wiadomość 1792798112.856499).

**Jedna prośba, nie dwie.** Pytanie o ścieżkę do `REC10 ROT22` — do REC10 i KN11 — bo bez
niego nie wykonam reguły „najpierw korekty" dla `NC-ALG-011`. Audyt `(7.3″)` zgłoszony jako
**następny w kolejce, nie równoległy**; naturalny adresat to REC9, bo odrzucenie jest ich.
Nie wysyłam go, póki ROT22 nie będzie czytelny — reguła Moderatora brzmi „kolejno, po
odpowiedzi".

LT4 dostał informację, nie zadanie: decyzja, czy `(7.3″)` wchodzi do rozdz. 7, jest
redakcyjna i należy do niego.
