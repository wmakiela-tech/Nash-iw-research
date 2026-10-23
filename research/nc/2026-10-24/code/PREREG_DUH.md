# PREREG — wsparcie XH-S4 Q64: dokładna formuła błędu naiwnego różniczkowania i jak zły może być

ZAPISANE PRZED URUCHOMIENIEM KODU, KTÓRY OPISUJE. Komórka NC, rola **Badacz**. 2026-10-24.
Tryb: **wsparcie, nie przejęcie.** Pytanie Q64 i konstrukcja 3×3 należą do XH-S4
(`XH-S4-OFFSHELL-BIANCHI-DUHAMEL-NOETHER-024`). Autorstwo pytania ich.

KROK 0 wykonany: `research/xh-s4/**` (obroty 017–025), `archive-index/**`, grep po
`Duhamel|Frechet|expm_frechet` w `research/**`. Wynik: **nikt nie ma formuły błędu ani
oszacowania przez komutator**; XH-S4 025 wprost mówi, że wątek Duhamela nie był rozwijany
(przeszli do Q70–Q76 o przyczynowości i stanie).

## Co XH-S4 ma, i czego tam brakuje

Mają **jeden punkt**: `D = [[-2,1,1],[1,-2,1],[1,1,-2]]`, `B = diag(b)`, `A = BD`,
`δA = diag(δb)D`, `b = [.15,.30,.42]`, `δb = [.01,−.018,.012]`:

`‖[A,δA]‖ = 0.040626336286`, `‖Dexp(A)[δA]‖ = 0.032470731485`,
`‖e^A δA − Dexp‖ = 0.013382194757`, **błąd względny 41,2131%**;
kontrola przemienna `b = .2I`: komutator zero, błąd `~6,5e-18`.

Brakuje trzech rzeczy, i to one są przedmiotem tego preregu: **formuły** błędu, jego
**oszacowania**, i odpowiedzi na pytanie **jak zły może być**. Bez tego trzeciego Q64 brzmi
jak „41% to dużo", a nie jak warunek wykonalności.

## Hipotezy

**P1 — dokładna tożsamość błędu.** Dla macierzy `A`, `E`:

`e^A E − Dexp(A)[E] = ∫₀¹ (1−u) · e^{(1−u)A} [E, A] e^{uA} du`

Przewidywane wyprowadzenie: `Dexp(A)[E] = ∫₀¹ e^{sA}E e^{(1−s)A}ds`, więc różnica
`= ∫₀¹ e^{sA}[E, e^{(1−s)A}]ds`; dalej `[E, e^{tA}] = ∫₀^t e^{(t−u)A}[E,A]e^{uA}du`
(rozwiązanie `F' = [E,A]e^{tA} + AF`, `F(0)=0`); po podstawieniu `e^{sA}e^{(1−s−u)A} = e^{(1−u)A}`
i zamianie kolejności całkowania zostaje waga `(1−u)`.
PRZEWIDYWANY TEST: zgodność z numeryczną kwadraturą do `~1e-12`.

**P2 — oszacowanie przez komutator.** Z P1 natychmiast
`‖e^A E − Dexp(A)[E]‖ ≤ ½ ‖[A,E]‖ · e^{μ₂(A)}`,
gdzie `μ₂(A) = λ_max((A+Aᵀ)/2)` to norma logarytmiczna. W szczególności przy `μ₂(A) ≤ 0`
**`‖błąd‖ ≤ ½‖[A,E]‖`**.
PRZEWIDYWANY TEST na liczbach XH-S4: `½·0.040626336286 = 0.020313168`, a błąd to
`0.013382195`, czyli iloraz `≈ 0.659`. Przewiduję, że **oszacowanie trzyma**. Osobno
sprawdzam znak `μ₂(A)` dla ich `A = BD` — tego nie przewiduję, bo `BD` nie jest symetryczne.

**P3 — jak zły może być błąd: nie 41%, lecz nieskończony.** Twierdzę, że istnieje `A`, dla
którego **prawdziwa pochodna znika, a naiwna nie**. Przewidywany świadek:
`A = π·[[0,−1],[1,0]]` (wartości własne `±iπ`). W bazie własnej pochodna Frécheta ma wpisy
pozadiagonalne `(e^{λ_i}−e^{λ_j})/(λ_i−λ_j)`; tu `(e^{iπ}−e^{−iπ})/(2iπ) = 0`. Zatem
`Dexp(A)` **zeruje** składową pozadiagonalną, podczas gdy `e^A E = −E ≠ 0`.
PRZEWIDYWANY TEST: `‖Dexp(A)[E]‖ ≈ 0` do rzędu maszynowego przy `‖e^A E‖ = ‖E‖`, oraz
błąd względny → ∞ przy `θ → π` w rodzinie `A = θ·[[0,−1],[1,0]]`.

Mechanizm nazwany: `Dexp(A)` jest nieodwracalna dokładnie wtedy, gdy dwie wartości własne
`A` różnią się o niezerową całkowitą wielokrotność `2πi` — klasyczny warunek z teorii
funkcji macierzowych. Dla `A` o **widmie rzeczywistym** rezonans jest nieosiągalny, więc
błąd względny pozostaje skończony.

**P4 — warunek typowany dla ich hosta, bez transferu.** Jeśli `A_C = B(C)□` ma widmo
rzeczywiste, rezonans z P3 jest **nieosiągalny** i Q64 pozostaje poprawką ilościową.
Staje się osiągalny, gdy argument form faktora nabiera części urojonych. **Nie twierdzę
transferu**: ich własny link typowany #3 mówi „SAME ALGEBRAIC DERIVATIVE, DIFFERENT FIELD,
CAUSAL AND UNBOUNDED-OPERATOR HOST", i to zastrzeżenie przyjmuję.

## Falsyfikatory

- **F1 — KONTROLA NA MOIM SETUPIE, PIERWSZA.** Muszę **odtworzyć wszystkie pięć liczb
  XH-S4** z ich danymi. Jeśli nie odtworzę, zły jest mój setup, **a nie ich wynik**,
  i wstrzymuję całość, bo nie wiem, co wspieram.
- **F2.** P1 fałszywa, jeśli kwadratura różni się od `e^AE − Dexp(A)[E]` o więcej niż `1e-10`.
- **F3.** P2 fałszywa, jeśli którykolwiek przypadek daje `‖błąd‖ > ½‖[A,E]‖e^{μ₂(A)} + tol`.
- **F4.** P3 fałszywa, jeśli przy `θ = π` norma `Dexp(A)[E]` nie spada do rzędu maszynowego
  albo jeśli błąd względny nie rośnie przy `θ → π`.
- **F5.** Jeśli dla `A` o widmie **rzeczywistym** znajdę nieograniczony błąd względny,
  to mechanizm z P3 jest źle nazwany.

## Czego nie robię

Nie liczę nic w grawitacji, nie buduję `T`, nie dotykam `□` ani NASH `E_g`, nie orzekam
o Q62, Q63, Q65–Q68. Nie twierdzę nowości: tożsamość Duhamela, pochodna Frécheta `exp`
i warunek `2πi` to dojrzała teoria funkcji macierzowych (Higham). Wkładem jest wyłącznie
**złożenie tego w odpowiedź na Q64 z oszacowaniem i świadkiem granicznym**.

Status docelowy `[▷]`. Brak EXEC_SIGN. Audyt zewnętrzny obowiązkowy. **Autorstwo Q64
i konstrukcji 3×3 pozostaje przy XH-S4**; to zwrot wspierający, nie konkurencyjny.
