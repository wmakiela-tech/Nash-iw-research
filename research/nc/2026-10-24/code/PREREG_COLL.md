# PREREG — naprawa odrzuconej nierówności (7.3′): właściwym obiektem jest norma części kolizyjnej

ZAPISANE PRZED URUCHOMIENIEM KODU, KTÓRY OPISUJE. Komórka NC, rola **Badacz**. 2026-10-24.
Zakres wybrany po KROKU 0 (inwentarz linii NC: `research/nc/**`, `archive-index/2026/nc/`,
Drive po `NC`, `#iw-dispatch` od mojego zwrotu 1792755325).

PATRON: **brak, świadomie.** Reguła dopuszcza patrona jako opcjonalny wzmacniacz, pod
warunkiem że zaostrza rygor produktu. Tu rygor trzymają odejmowanie prior-artu i lista
falsyfikatorów poniżej; dodatkowa rama dodałaby narracji, nie wyniku. Zawieszam.

## Co naprawiam i dlaczego to należy do NC

`NC-FAL-011`. REC9 §B3 odrzucił nierówność ilościową z pakietu 002 §B.2:

`‖J m(A) − m(B) J‖ ≤ 2‖m‖_∞ · κ_h(J)`,  gdzie `κ_h(J) = sup{‖Q_j J P_i‖ : (λ_i, μ_j) ∈ C_h}`

Powód odrzucenia: **wiele małych bloków kolizyjnych może sumować się koherentnie** do
operatora o normie znacznie większej niż supremum norm bloków. Kontrprzykład REC9:
`A = diag(0,1)`, `B = diag(2,3)`, `h(λ) = cos(2πλ)` dają `h(A) = h(B) = I`, więc hipoteza
`J h(A) = h(B) J` zachodzi dla **każdego** `J`; dla `J = ½[[1,1],[1,1]]` jest `‖J‖ = 1`,
a każdy blok `Q_j J P_i` ma normę `½`.

Werdykt REC9 brzmi `B_QUANTITATIVE_BOUND_REJECT_AND_REPLACE`. Część **jakościowa** przeszła
(`NC_B_SEPARATION_NOT_NECESSARY`, `NC_B_FIXED_J_COLLISION_COUPLING_CRITERION` — oba
`PASS_EXACT_FINITE_PURE_POINT`). Naprawa jest więc precyzyjnie zlokalizowana: wymienić
**stałą**, nie kryterium. Sprawdzone przed podjęciem: `(7.3′)` nie ma następcy w
`research/**` ani `archive-index/**`; linia zbioru kolizji jest wyłącznie NC.

## Hipotezy

**H1 (właściwy obiekt).** Supremum norm bloków jest złym obiektem; właściwym jest norma
**całej części kolizyjnej**. Definiuję

`J_coll = Σ_{(i,j) ∈ C_h} Q_j J P_i`

i twierdzę, że przy hipotezie `J h(A) = h(B) J` dla każdego ograniczonego borelowskiego `m`

`‖J m(A) − m(B) J‖ ≤ 2‖m‖_∞ · ‖J_coll‖`.   **(7.3″)**

Przewidywany mechanizm: rozbij `J = J_coll + J_match + J_rest`, gdzie `J_match` to bloki
z `λ_i = μ_j`, a `J_rest` to bloki z `h(λ_i) ≠ h(μ_j)`. Hipoteza zeruje `J_rest`; bloki
`J_match` mają współczynnik `m(λ_i) − m(μ_j) = 0`. Zostaje
`J m(A) − m(B) J = J_coll m(A) − m(B) J_coll`, a stąd nierówność trójkąta.

**H2 (kryterium jakościowe nietknięte).** `‖J_coll‖ = 0 ⟺ κ_h(J) = 0`, więc wymiana stałej
**nie rusza** części, którą REC9 przepuścił. To jest warunek, który naprawa musi spełnić,
żeby była naprawą, a nie nowym twierdzeniem.

**H3 (stała 2 jest osiągana).** Istnieje świadek z ilorazem
`‖J m(A) − m(B) J‖ / (‖m‖_∞ ‖J_coll‖)` równym **dokładnie 2**. Przewidywana konstrukcja:
**macierze samego REC9** z `m` przyjmującym `+1` na widmie `A` i `−1` na widmie `B`; wtedy
`m(A) = I`, `m(B) = −I`, więc `J m(A) − m(B) J = 2J`. Jeśli to wyjdzie, kontrprzykład REC9
służy jednocześnie jako dowód ostrości mojej poprawki.

**H4 (relacja do `‖J‖`).** `‖J_coll‖ ≤ 2‖J‖` zawsze, bo `J_coll = J − J_match` przy
zerowym `J_rest`, a `J_match` jest selekcją po **częściowej permutacji** (różne wartości
własne, więc każde `i` pasuje do najwyżej jednego `j`), skąd `‖J_match‖ = max ‖Q_j J P_i‖ ≤ ‖J‖`.
Pytanie ilościowe, którego **nie przewiduję**: jak duże może być `‖J_coll‖/‖J‖`. Zapisuję
jako otwarte, nie jako tezę.

## Falsyfikatory — rozstrzygane PRZED interpretacją

- **F1.** (7.3″) fałszywa, jeśli którykolwiek losowy przypadek daje
  `‖J m(A) − m(B) J‖ > 2‖m‖_∞‖J_coll‖ + tol`.
- **F2.** H3 fałszywa, jeśli maksymalny zmierzony iloraz nie dochodzi do 2; wtedy stała nie
  jest ostra i trzeba szukać prawdziwej.
- **F3.** H2 fałszywa, jeśli istnieje przypadek z `‖J_coll‖ = 0` i niezerowym defektem
  splatania dla jakiegoś `m`. To by przeczyło `PASS` REC9, więc byłby to wynik przeciw
  **obu** nam i wymagałby zatrzymania.
- **F4 — KONTROLA NA MOIM SETUPIE, nie na REC9.** Muszę **odtworzyć** naruszenie **starej**
  nierówności w moim własnym kodzie, na macierzach REC9. Jeśli tego nie odtworzę, to mój
  setup jest zły, **a nie ich kontrprzykład** — i wtedy wstrzymuję całą naprawę, bo nie
  wiem, co naprawiam. Ten falsyfikator jest ważniejszy od F1.
- **F5.** H4 fałszywa, jeśli znajdę `‖J_coll‖ > 2‖J‖`.

## Procedura

1. Macierze diagonalne `A`, `B` o zadanych widmach (projektory `P_i`, `Q_j` = jednostkowe
   bloki), `J` losowe rzeczywiste i zespolone, `n` od 2 do 8.
2. `h` dobrane tak, by **wymusić kolizje**: `h = cos(2πλ)` na widmach całkowitych albo
   `h` sklejające zadane pary. Hipoteza `J h(A) = h(B) J` nakładana przez **zerowanie**
   bloków niekolizyjnych i niepasujących — czyli konstrukcyjnie, nie przez odrzucanie prób.
3. Dla każdego przypadku: maksymalizacja defektu po `m` z `‖m‖_∞ ≤ 1`. Przy skończonym widmie
   `m` to wektor wartości na widmach, więc maksymalizuję po wierzchołkach `{±1}^(#widm)`
   — **wyczerpująco**, nie losowo, dopóki liczba wierzchołków na to pozwala.
4. Osobno: dokładny świadek z H3 wypisany jawnie i policzony.
5. Kontrola F4 na macierzach REC9 przed czymkolwiek innym.

## Czego ten test nie rozstrzyga

Nie dotyka widma ciągłego (pakiet 002 §B.5 miał tam tylko model operatorów mnożenia, a §C.1
deklarował ogólną postać jako hipotezę — ten status się nie zmienia). Nie dotyka przypadku
nieskończonego widma punktowego, gdzie `J_coll` wymaga kontroli zbieżności. Nie twierdzę
nowości: przestrzeń hostów to mnożniki Schura i Fuglede–Putnam–Rosenblum, a sama tożsamość
blokowa (*) jest jednolinijkowa. `SEARCH FAILURE != NOVELTY`.

Status docelowy `[▷]`. Brak EXEC_SIGN. **Audyt zewnętrzny obowiązkowy** — ANTI-SELF-SEALING;
jako SP nie oceniam merytorycznie tego, co proponuję jako Badacz.
