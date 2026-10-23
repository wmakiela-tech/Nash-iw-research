# IW_NC_SACRIFICIAL_MEASUREMENT_AND_PROTOCOL_CEILING_009_20261018


<!-- IW_CONFORMANCE_BLOCK v1 (docs/IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md §2.7) -->
```text
artifact_id          : IW_NC_SACRIFICIAL_MEASUREMENT_AND_PROTOCOL_CEILING_009_20261018
exposure             : PUBLIC_SAFE
canonical_body_path  : research/nc/2026-10-18/IW_NC_SACRIFICIAL_MEASUREMENT_AND_PROTOCOL_CEILING_009_20261018.md
source_revision      : rozwiazywane przez `git log -- <canonical_body_path>`
bw_event_or_pending  : GITHUB_PENDING_BW_INGEST
claim_ceiling        : NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE / MODEL_AGREEMENT_IS_NOT_PROOF / SEARCH_FAILURE_IS_NOT_NOVELTY
hold                 : BRAK
```

ARTIFACT_ID: IW_NC_SACRIFICIAL_MEASUREMENT_AND_PROTOCOL_CEILING_009_20261018
KOMÓRKA: NC — zewnętrzna komórka Claude
STATUS: [▷] / EXEC_SIGN = BRAK / NO_CANON / NO_NOVELTY / NO_PHYSICAL_UPGRADE
KOD: `multi.py` sha256 5b94fb6c0e8e1f438e1c71b289ff20480a25632e531b873ca8a868279137a165
POPRZEDZA: 008, DRIVE 1yqrjkkBUy9A4xyWnAB_Ir7WYEqHius4g
**AUDYT ZEWNĘTRZNY OBOWIĄZKOWY** — całość jest moja.

---

## 0. Pytanie

Zamykając 008 napisałem: Twierdzenie 7.10 monografii mówi, że adwersarialne powtórzenia pomiaru
nie zwiększają gwarantowanej precyzji — ale tam czujnik nie oddziaływał zwrotnie, a przy reakcji
zwrotnej **każdy kolejny pomiar dokłada tłumienia**. Podejrzewałem, że istnieje optymalna
skończona liczba pomiarów i że to jest twierdzenie.

Są dwa twierdzenia, i **moje podejrzenie było w połowie błędne**.

---

## 1. Pierwszy wynik jest o modelu, nie o fizyce: reakcja zwrotna musi być RÓWNOCZESNA

Naturalnym pierwszym odruchem jest pomiar impulsowy: w chwili `t_j` odczytujemy `b_j = a y(t_j)`
i mnożymy prędkość przez `e^{−γ s}`. **Ten model jest zepsuty** i trzeba to powiedzieć, zanim
cokolwiek się na nim policzy: odczyt następuje *przed* zaburzeniem, więc wzmocnienie `a` nie jest
niczym ograniczone i `a|y(t_j)| → ∞`. Wraca dokładnie nielicencjonowane wzmocnienie z Wniosku 7.4
monografii, tylnymi drzwiami.

Reakcja zwrotna musi działać **w trakcie** odczytu. Pomiar o czasie trwania `τ` i sprzężeniu `a`,
w granicy `τ → 0` przy ustalonej **sile** `s = aτ`:

    sygnał    = y(t_j) · σ(s),     σ(s) = (1 − e^{−γs}) / γ      ← NASYCA SIĘ
    przeżywa  = y(t_j) · e^{−γs}                                  ← TŁUMI

Jeden pomiar wyciąga **najwyżej `1/γ`** sygnału i zostawia `e^{−γs}` stanu. To jest budżet
informacja–zaburzenie z jawną sumą, i dopiero on czyni pytanie dobrze postawionym.

Z Tw. 7.10 monografii (adwersarialny szum `|η_j| ≤ δ` osobno na każdy pomiar) wiąże tylko
najostrzejsze ograniczenie, więc figurą zasługi protokołu jest

    M = max_j |G_j| σ(s_j),        błąd znormalizowany = min(1, δ / (R·M)).

---

## 2. Twierdzenie 1 — sufit niezależny od protokołu

**Teza.** Przy reakcji zwrotnej o sile `γ` żaden protokół — dowolna liczba pomiarów, dowolne
czasy, dowolne siły — nie osiąga `M ≥ 1/γ`. Jeden pomiar wysyca ten kres.

**Dowód, elementarny.** Start `(x,y) = (0,1)`, więc `x² + y² = 1`. Swobodna ewolucja oscylatora
zachowuje tę sumę, a tłumienie może ją tylko zmniejszyć. Zatem `|G_j| = |y(t_j)| ≤ 1` dla każdego
`j` i każdego protokołu. Ponadto `σ(s) = (1−e^{−γs})/γ < 1/γ`. Stąd `M < 1/γ`. □

**Kontrola numeryczna**, 60 000 losowych protokołów o `k ∈ {1,2,3,4}`, czasach z `[0,6]`
i siłach z `[0.01,40]`:

| γ | sufit `1/γ` | najlepsze zmierzone `M` | `M·γ` |
|---|---|---|---|
| 0.25 | 4.000000 | 3.999800 | 0.999950 |
| 0.5 | 2.000000 | 2.000000 | 1.000000 |
| 1.0 | 1.000000 | 1.000000 | 1.000000 |
| 2.0 | 0.500000 | 0.500000 | 1.000000 |
| 4.0 | 0.250000 | 0.250000 | 1.000000 |

**Konsekwencja.** Znormalizowany błąd minimaksowy ma podłogę

    ℰ / (R|h(T)|)  ≥  γ δ / R      dla KAŻDEGO protokołu pomiarowego.

W 008 wyprowadziłem podłogę `γδ/(2RN(t_s))` dla pojedynczego pomiaru w ustalonej chwili. Tutaj
podłoga jest **niezależna od protokołu**: nie da się jej obejść ani liczbą pomiarów, ani ich
rozmieszczeniem, ani strojeniem sił. Jest funkcją wyłącznie siły reakcji zwrotnej i szumu.

To **wzmacnia Tw. 7.10 monografii**. Tam: powtórzenia nie zwiększają gwarantowanej precyzji, przy
czujniku biernym. Tutaj: powtórzenia nie zwiększają jej także przy czujniku oddziałującym
zwrotnie, **i dodatkowo istnieje bezwzględny kres, którego nie przekroczy żaden protokół**.

**Tu moje podejrzenie było błędne.** Przewidywałem „optymalną skończoną liczbę pomiarów" —
sugerując, że będzie to jakieś `k > 1`. Przy swobodnych czasach optymalne `k` wynosi **jeden**.
Zmierzone najlepsze `M` dla `k = 1, 2, 3`: 0.999635, 0.999649, 0.999657 — różnice są szumem skanu.
`origin_failure_mode: EXPECTED_AN_INTERIOR_OPTIMUM_WHERE_THE_CONSTRAINT_WAS_A_CONSERVED_BUDGET`.

---

## 3. Twierdzenie 2 — przy ograniczonych czasach pomiar OFIARNY się opłaca

Swoboda czasu była jednak w Twierdzeniu 1 kluczowa. §7.5b.5 monografii mówi wprost, że pomiary
mogą być **„dopuszczone tylko w wybranych chwilach"**. Wtedy obraz się odwraca.

Okienko `[1.40, 1.75]` wokół czasu ślepego `π/2 = 1.570796`, gdzie swobodna odpowiedź prędkości
`|cos t|` jest mała: `|cos 1.40| = 0.169967`, `|cos 1.5708| = 4·10⁻⁶`, `|cos 1.75| = 0.178246`.

    JEDEN pomiar :  M = 0.178246     (t = 1.7500, s = 20)
    DWA pomiary  :  M = 0.337909     (t₁ = 1.4000, t₂ = 1.7500, s₁ = 50, s₂ = 50)
    ZYSK         :  1.8957 ×

**Mechanizm, zmierzony osobno.** Gdyby pomiar 1 czytał, ale nie tłumił, drugi pomiar widziałby
`|G₂| = 0.178246`. Z reakcją zwrotną pomiaru 1 widzi `|G₂| = 0.337909` — **1.90 ×**. Tłumienie
prędkości sprawia, że człon pozycyjny przestaje się kasować z prędkościowym, i układ wychodzi
z martwego punktu.

**Pomiar 1 jest ofiarny w ścisłym sensie.** Jego własny wkład to `0.169967` i jest **zawsze
mniejszy** od wkładu pomiaru 2 (`0.337909`). Informację niesie drugi pomiar; pierwszy jest
wydany na zaburzenie. Zależność od siły pierwszego pomiaru:

| `s₁` | 0 | 0.5 | 1 | 2 | 4 | 8 | 20 | 50 |
|---|---|---|---|---|---|---|---|---|
| `\|G₂\|` | 0.178246 | 0.241068 | 0.279172 | 0.316301 | 0.334984 | 0.337855 | 0.337909 | 0.337909 |
| `M` | 0.178246 | 0.241068 | 0.279172 | 0.316301 | 0.334984 | 0.337855 | 0.337909 | 0.337909 |

**Pomiar ofiarny należy wykonać możliwie mocno** — `M` rośnie monotonicznie w `s₁` i nasyca się
około `s₁ ≈ 8`. To jest odwrotność intuicji „mierz delikatnie, żeby nie zaburzyć".

**Zysk zależy od ciasnoty okienka:**

| okienko | `M` (1 pomiar) | `M` (2 pomiary) | zysk |
|---|---|---|---|
| [1.50, 1.65] | 0.079121 | 0.149064 | 1.8840 |
| [1.45, 1.70] | 0.128844 | 0.245601 | **1.9062** |
| [1.40, 1.75] | 0.178246 | 0.337909 | 1.8957 |
| [1.30, 1.85] | 0.275590 | 0.503640 | 1.8275 |
| [1.10, 2.05] | 0.461073 | 0.724922 | 1.5723 |
| [0.80, 2.35] | 0.702713 | 0.851337 | 1.2115 |

Im bliżej jesteśmy przypięci do czasu ślepego, tym więcej wart jest pomiar ofiarny; przy swobodzie
czasu zysk znika, zgodnie z Twierdzeniem 1.

---

## 4. Co z tego jest warte zapisania

**Pomiar, którego własny odczyt jest prawie bezwartościowy, bywa wart wykonania — dla swojego
zaburzenia.** To odwraca standardowy odczyt reakcji zwrotnej jako czystego kosztu. W 008
pokazałem, że reakcja zwrotna *przesuwa* czas ślepy; tutaj okazuje się, że można ją **celowo
wydać**, żeby czas ślepy usunąć.

Dwa twierdzenia składają się w jedno zdanie projektowe: **liczba pomiarów nie kupuje precyzji
(Tw. 1), ale rozmieszczenie zaburzenia — tak (Tw. 2).** Budżet jest na zaburzeniu, nie na
powtórzeniach.

---

## 5. Czego nie twierdzę

1. **Ten sam model co w 008, z tymi samymi zastrzeżeniami.** Skalarny stan ukryty, oscylator,
   fenomenologiczna reakcja zwrotna typu „pomiar prędkości tłumi prędkość". Wersja kwantowa
   podlegałaby relacjom nieoznaczoności i jest **innym zadaniem**.
   `COMMON MATHEMATICS != COMMON PHYSICAL MECHANISM`.
2. **Twierdzenie 1 dowiodłem dla tego oscylatora**, korzystając z `x²+y² ≤ 1`. Dla ogólnego
   generatora sufit zależałby od tego, czy istnieje analogiczna wielkość nierosnąca. Nie
   sprawdzałem, kiedy taka istnieje — a to jest właściwe pytanie uogólniające i go **nie podjąłem**.
3. **Twierdzenie 2 jest wynikiem skanu, nie dowodem.** Mam optymalizację po siatce
   `(t₁,t₂,s₁,s₂)`; nie wyprowadziłem optymalnej pary analitycznie ani nie wykazałem, że `k = 2`
   jest optymalne wśród `k > 1` w okienku. Zysk `1.9×` jest zmierzony, nie dowiedziony jako kres.
4. **Figura zasługi `max_j` opiera się na Tw. 7.10 monografii** (adwersarialny szum z osobnym
   budżetem na pomiar). Przy innym modelu szumu — niezależnym losowym, albo ze wspólnym budżetem
   normy — figura byłaby inna i **całe Twierdzenie 1 mogłoby upaść**, bo uśrednianie zaczęłoby
   działać. To jest najpoważniejsze ograniczenie tego zwrotu i wskazuję je jako pierwsze do ataku.
5. **Nie szukałem literatury.** Kompromis informacja–zaburzenie i „pomiar jako zasób sterujący"
   to motywy znane (sterowanie przez pomiar, measurement-based feedback, zeno). **Nie twierdzę
   nowości** i spodziewam się gospodarzy, zwłaszcza dla §3.

---

KONIEC. Status [▷]. EXEC_SIGN brak.
