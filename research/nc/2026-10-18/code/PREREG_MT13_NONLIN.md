# PREREG — czy twierdzenie MT13 o równych plonach przeżywa ubytek zależny od stanu

ZAPISANE PRZED URUCHOMIENIEM KODU, KTÓRY OPISUJE. Komórka NC. 2026-10-23.
TRYB: NONBLIND wobec dowodu MT13 (przeczytałem go, zanim podszedłem do problemu — patrz zwrot 018 §1).
TRYB wobec TEGO pytania: MT13 stawia je jako otwarte i nie podaje odpowiedzi; mojej odpowiedzi
nie widziałem u nikogo.

## Przedmiot

MT13 dowodzi dla układu liniowego `n' = S − γn`, `X' = −λX + κγn`:
dwa nieujemne źródła `L¹` o równej emisji `∫S` i równej liczbie ocalałych `n(T)` dają równy
plon `X(T)` **wtedy i tylko wtedy, gdy** `w ∈ span{1, q}` p.w., gdzie
`q(s) = exp(−∫_s^T γ)` i `w(s) = ∫_s^T κγ exp(−∫_s^t γ) exp(−∫_t^T λ) dt`.

Dowód odwrotności MT13 używa dualności `L¹`/`L^∞` i przechodzi przez faktoryzację
`S ↦ (∫S, ∫qS)`. Pytanie otwarte samego MT13: czy jakiekolwiek takie twierdzenie jest
stabilne, gdy ubytek zależy od stanu (`γ = γ(n)`), tzn. gdy odwzorowanie `S ↦ n(T)`
przestaje być liniowe.

## Hipotezy — rozstrzygane PRZED zobaczeniem liczb

**H1 (kiedy przypadek zdegenerowany zachodzi).** Przy stałych `γ > 0`, `λ ≥ 0`, `κ ≠ 0`
warunek `w ∈ span{1, q}` zachodzi **dokładnie dla `λ = 0`**, i dla żadnego innego `λ`,
w szczególności NIE dla `λ = γ`.
Przewidywany mechanizm: po podstawieniu `σ = T − s` mamy `q = e^{−γσ}` oraz
`w = κγ(e^{−λσ} − e^{−γσ})/(γ−λ)`; `w ∈ span{1, e^{−γσ}}` wymaga
`e^{−λσ} ∈ span{1, e^{−γσ}}`, a trzy wykładniki o różnych indeksach są niezależne
na przedziale dodatniej długości, więc zostaje `λ ∈ {0, γ}`; w granicy `λ = γ` mamy
`w = κγσe^{−γσ}`, a `σe^{−γσ} ∉ span{1, e^{−γσ}}`, więc `λ = γ` odpada.
PRZEWIDYWANY TEST: wyznacznik `[1, q, w]` na trzech węzłach — zero tylko przy `λ = 0`.

**H2 (stabilność przy ubytku zależnym od stanu).** Dla `λ = 0` i STAŁEGO `κ`
teza przeżywa dowolny ubytek `Γ(t, n)`, także nieliniowy i zależny od stanu.
Przewidywany mechanizm: z pierwszego równania `∫Γ = ∫S − n(T) + n(0)`, a przy `λ = 0`
mamy `X(T) = X(0) + κ∫Γ`. To **bilans masy**, nie dualność: nie potrzebuje liniowości
w `S` ani istnienia `q`.
PRZEWIDYWANY TEST: dla `Γ = γ₀(1+βn)n`, `β > 0`, `λ = 0` plon `X(T)` ma być STAŁY
na jednoparametrowej rodzinie źródeł o ustalonych `∫S` i `n(T)` — z dokładnością
całkowania, nie lepiej.

**H3 (gdzie nieliniowość jednak boli).** Dla `λ > 0` plon `X(T)` ma się ZMIENIAĆ na tej
samej rodzinie, zarówno przy `β = 0`, jak i `β > 0`. Czyli nieliniowość nie tworzy
nowego przypadku zdegenerowanego w tej rodzinie.
Zastrzeżenie zapisane z góry: brak nowego przypadku W TEJ RODZINIE nie dowodzi braku
takiego przypadku w ogóle. Jeśli H3 wyjdzie, wynik brzmi „nie znalazłem", nie „nie istnieje".

## Procedura

1. Impulsy prostokątne w `A = [0, 0.7, 1.4]`, szerokość `0.1`, `T = 2`, `γ₀ = 2`, `κ = 0.1`,
   `n(0) = 0`, `X(0) = 0.1`. Źródło `S = (1,1,1) + θ·(1,−1,0) + ρ·(0,1,−1)` — oba kierunki
   mają sumę zero, więc `∫S` jest ustalone z konstrukcji.
2. Dla każdego `θ` z siatki szukam `ρ(θ)` zerującego `n(T; S) − n(T; S₀)` przez bisekcję
   na całkowanym numerycznie `n(T)`. To daje rodzinę o równej emisji I równych ocalałych.
3. Raportuję `X(T)` na tej rodzinie dla czterech przypadków: `(β, λ) ∈ {0, 1.5} × {0, 1}`.
4. Kontrola odwrotna: sprawdzam, że wszystkie wagi pozostają nieujemne; punkty z wagą
   ujemną odrzucam, bo twierdzenie MT13 dotyczy źródeł nieujemnych.
5. Kontrola całkowania: ten sam przebieg przy dwóch krokach `h` i `h/4`; rozrzut `X(T)`
   na rodzinie musi maleć jak krok, jeśli ma być artefaktem, a nie zostać stały, jeśli
   jest realny.

## Falsyfikatory

- H1 fałszywa, jeśli wyznacznik zeruje się dla jakiegoś `λ ∉ {0}` w siatce.
- H2 fałszywa, jeśli przy `λ = 0, β = 1.5` rozrzut `X(T)` NIE maleje z krokiem całkowania,
  czyli jest realny, a nie numeryczny.
- H3 fałszywa, jeśli przy `λ = 1` rozrzut maleje z krokiem (czyli plon jest faktycznie stały).

## Czego ten test nie rozstrzyga

Nie rozstrzyga pełnej odwrotności dla ubytku zależnego od stanu: nie mam charakteryzacji
„dla jakich `Γ` teza zachodzi", tylko warunek dostateczny `λ = 0` + stałe `κ`. Klasyfikacja
dla `λ > 0` pozostaje otwarta i tak ją zapiszę.
Nie nadaję statusu wyższego niż `[▷]`. Brak EXEC_SIGN. Audyt zewnętrzny obowiązkowy.
