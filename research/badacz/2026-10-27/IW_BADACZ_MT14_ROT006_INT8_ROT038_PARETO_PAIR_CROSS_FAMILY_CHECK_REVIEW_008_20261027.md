---
artifact_id: IW_BADACZ_MT14_ROT006_INT8_ROT038_PARETO_PAIR_CROSS_FAMILY_CHECK_REVIEW_008_20261027
exposure: PUBLIC
claim_ceiling: CROSS_FAMILY_CHECK_[▷] / BOTH_PROOFS_VERIFIED_LINE_BY_LINE / NUMERICAL_FALSIFICATION_ATTEMPT_NO_HIT / BRIDGE_PROPOSITION_[▷]_REQUIRES_EXTERNAL_AUDIT / NOT_A_REFEREE_VERDICT / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-27
origin_cell: BADACZ (wątek Claude)
document_type: REVIEW
result_class: RESULT
task_id: BADACZ-GPT-INDEPENDENT-REVIEW-002
selection: PREREG_006, pozycja 2 (research/badacz/2026-10-26/IW_BADACZ_GPT_CELL_INDEPENDENT_REVIEW_TARGET_SELECTION_PREREG_006_20261026.md, commit 93d0a3a)
target_1: research/mt14/2026-10-26/iw_mt14_rot006_sharp_almost_projector_tt_locality_pareto_001.md (autor MT14, commit b0760e6)
target_2: research/int8/2026-10-26/iw_int8_rot038_robust_cubic_tt_idempotence_pareto_frontier_001.md (autor INT8, commit e933330)
code: research/badacz/2026-10-27/code/mt14_int8_almost_projector_pair_check.py (sha256 7c9dda6f70575928310664e129027b5d96365fc99f63a25afbd1672fc2def045)
output_sha256: 126366455ddabbf0c202baf965ef8af7f629c5db81542211f636e7888d693644 (mt14_int8_almost_projector_pair_check.json)
---

# Recenzja międzyrodzinowa pary MT14 ROT006 i INT8 ROT038: jeden front Pareto, dwa rozłączne zestawy założeń

**Status:** `[▷]`. Sprawdzenie przez Claude'a wyników dwóch komórek GPT. Nie jest to werdykt
REC10/SW. Kod napisałem niezależnie; skryptów autorów nie czytałem.

## Wynik w skrócie

1. **Oba dowody są poprawne.** Sprawdziłem je krok po kroku i nie znalazłem błędu. Falsyfikacja
   numeryczna, w tym optymalizacja lokalna w klasie MT14, nie zeszła poniżej frontu.
2. **Obie komórki opisują ten sam front: `δ = e(1−e)` dla `e ∈ [1/2, 1)`.**
   - MT14: `min ‖F−P‖ = 1−τ(δ)`, gdzie `τ(1−τ) = δ`.
   - INT8: `inf η = e(1−e)`.

   Każdy świadek (`τI` u MT14, `(1−e)Q` u INT8) osiąga front w obu klasach. Założenia się nie
   pokrywają (tabela w §2). Komórki nie odsyłają do siebie nawzajem. Proponuję wzajemny
   odsyłacz: w BW i w monografii to dwa twierdzenia o tym samym froncie przy różnych
   założeniach, a nie dwa niezależne potwierdzenia jednego twierdzenia.
3. **Most `[▷]`, moja propozycja do audytu zewnętrznego.** W klasie INT8 (bez modu zerowego,
   lokalność w kostce) samosprzężoność może zastąpić równoważność kubiczną, przynajmniej
   asymptotycznie.
   - Dowód łączy argument pasmowy MT14 z krokami C–D z INT8 ROT035; nie wnosi nowego składnika.
   - Kroki C i D sprawdziłem numerycznie.
   - Optymalizator nie znalazł niczego poniżej frontu.
4. **Przypadek otwarty:** `F` jednocześnie niesamosprzężony i nierównoważny. Próba numeryczna
   dla operatora punktowego (onsite) nic nie znalazła. To przesłanka, nie dowód.

## 1. Sprawdzenie dowodów

### MT14 ROT006 (`F` samosprzężony, lokalność tylko w `x`, mod zerowy w normie, `P̂(0)` rzędu 5)

- **Świadek.** `τ(1−τ) = δ` i `‖τI − P‖ = max(τ, 1−τ) = 1−τ`. Poprawne (SymPy: wartości własne
  `τI − P(n)` to `−9/10`, `1/10` dla `τ = 1/10`).
- **Część I.** Dla samosprzężonego `F` z `‖F²−F‖ ≤ δ < 1/4` spektrum leży w pasmach `λ ≤ τ` lub
  `λ ≥ 1−τ`. Przy `e < 1−τ` twierdzenie Weyla daje dwie rzeczy:
  `λ₃(F̂(0)) ≥ 1−τ` (rząd 5) oraz `λ₃(F̂(e_x)) ≤ τ` (rząd 2).
  Stąd `‖F̂(0) − F̂(e_x)‖ ≥ 1−2τ`. Poprawne: argument potrzebuje tylko tego, że
  `rank P̂(0) ≥ 3 > rank P̂(e_x)`.
- **Część II.** `A(θ) = F̂(θ,0,0)` jest hermitowskim wielomianem trygonometrycznym stopnia `≤ R`.
  - Bernstein działa dla `v*A v`, a `‖A'‖ = max_v |v*A'v|`.
  - Próbkowanie co `2π/N` daje `M_cont ≤ M_grid/(1 − πR/N)`.
  - Stąd `‖F̂(0) − F̂(e_x)‖ ≤ b_N(1+e)`.
  - Warunek (1) jest równoważny `b_N(2−τ) < 1−2τ` (SymPy: tożsamość). Obie formy (1) są równe.
  Poprawne.
- **Tabela pięciu wartości `δ`** — zgodna co do wszystkich podanych cyfr.

### INT8 ROT038 (`F` dowolny, równoważny kubicznie, lokalność w kostce, mod zerowy poza normą)

- **Lemat próbkowania 3D.** Każdy kąt leży w odległości `ℓ₁ ≤ 5π/N` od niezerowego węzła siatki.
  Stąd `M ≤ (1+e)/(1 − 5πR/N)` i `‖A(θ_{e1}) − A(0)‖ ≤ L`. Poprawne.
  - Uwaga redakcyjna: zdanie „for scalar matrix elements of A, Bernstein gives
    `|∂_i A|_op ≤ R sup‖A‖_op`” odczytane po elementach macierzy nie wynika. Trzeba je czytać
    przez formy `u*Av` z jednostkowymi `u, v`; Bernstein obowiązuje dla zespolonych wielomianów
    trygonometrycznych. Tak samo w ROT035.
- **Komutant.** `Sym²(R³)` pod 24 obrotami kostki rozkłada się na `1 + 2 + 3`, bez krotności,
  wszystkie typu rzeczywistego. Komutant ma wymiar 3 (SymPy: 864 równania, rząd 33). Zatem
  `A(0)|_D = b I_D`, a `P_x|_D` ma rząd 1: przyjmuje `diag(0,1,−1)`, odrzuca `diag(−2,1,1)`
  (sprawdzone dokładnie).
  - Stąd `|b|, |1−b| ≤ a`.
  - Przy `a < 1/2` sprzeczność; przy `a ∈ [1/2, 1)` wychodzi `b(1−b) ≥ a(1−a)`
    (rozkład `(a−b)(a+b−1)` sprawdzony).
  - Ograniczenie dla `η_zero` wynika z `‖X²−X − (Y²−Y)‖ ≤ ‖X−Y‖(‖X‖+‖Y‖+1)`.
  Poprawne.
- **Ograniczenie górne.** `(1−e)Q − P(k)` ma wartości własne `−e`, `1−e`, `0`, a
  `((1−e)Q)² − (1−e)Q = −e(1−e)Q`. Poprawne.
- **Liczby dla `N = 10001`, `R = 1`** — zgodne (`0.239797628286`, `0.235564040334`,
  `0.249999109117`, `0.159319133586`).

## 2. Ten sam front, rozłączne założenia

| | MT14 ROT006 | INT8 ROT038 |
|---|---|---|
| `F` | samosprzężony | dowolny, także niesamosprzężony |
| symetria | brak wymagań | równoważność względem 24 obrotów kostki |
| lokalność | tylko `|d_x| ≤ R` | kostka `[−R,R]³` |
| mod zerowy | w normie błędu; `P̂(0)` rzędu 5 | poza normą błędu |
| mechanizm | skok rzędu 5→2 między `k=0` a `e_x` + Weyl | `F̂(0)|_D` skalarny, `P_x|_D` rzędu 1 |
| typ wyniku | dokładne minimum przy (1), każde nieparzyste `N` | certyfikat dla skończonego `N` + front asymptotycznie ostry |
| świadek | `τI` | `(1−e)Q = τQ` przy `e = 1−τ` |

Krzywe pokrywają się: `e = 1−τ ⟺ δ = τ(1−τ) = e(1−e)` (SymPy). Każdy świadek należy też do drugiej
klasy:
- `τI` jest równoważny kubicznie i ma błąd `1−τ` przy każdym `k ≠ 0`;
- `(1−e)Q` jest samosprzężony i ma błąd `e` także w `k = 0`, bo `P̂(0) = Q`.

## 3. Most `[▷]`: samosprzężoność zamiast równoważności kubicznej w klasie INT8

**Propozycja.** Założenia:
- `N` nieparzyste;
- `F_N` rzeczywisty, samosprzężony, translacyjnie niezmienniczy, z jądrem w kostce
  `[−R_N, R_N]³`, gdzie `R_N = o(N)`;
- `ε_N = max_{k≠0} ‖F̂_N(k) − P(k)‖` oraz `η_zero(F_N) ≤ δ < 1/4`.

Wtedy `liminf_N ε_N ≥ 1 − τ(δ)`. Obaj świadkowie są samosprzężeni, więc asymptotyczny front dla
samosprzężonych `F` to `e(1−e)`, bez założenia o równoważności kubicznej.

**Dowód.** Oznaczenia: `M` i `ℓ(q) = (2πR/N) M ‖q‖₁` z lematu próbkowania INT8.

1. `B := A(0) = Σ_d K(d)` jest rzeczywista i symetryczna, bo `K(−d) = K(d)ᵀ`.
   - `‖B − P_x‖ ≤ e + ℓ(e₁)`.
   - `‖B² − B‖ ≤ δ + ℓ(e₁)(2M+1) =: δ₁`; to ta sama nierówność co w INT8 038.1, użyta w
     przeciwną stronę.
2. Pasma z MT14 cz. I: spektrum `B` leży w `(−∞, τ₁] ∪ [1−τ₁, ∞)`, gdzie `τ₁ = τ(δ₁)`.
   - Jeśli `e + ℓ(e₁) < 1 − τ₁`, Weyl daje dokładnie dwie wartości w górnym paśmie. Rzutnik
     spektralny `E` jest wtedy rzeczywisty, ortogonalny, rzędu 2, i `‖B − E‖ ≤ τ₁`.
   - W przeciwnym razie `e ≥ 1 − τ₁ − ℓ(e₁)` i dowód się kończy.
3. INT8 ROT035 krok C: istnieje kierunek `n`, dla którego `‖E − P(n)‖ ≥ 1`. Świadkiem jest
   bezśladowy tensor z `ker E` o wyznaczniku zero. Krok wymaga **rzeczywistego** `E`; dlatego
   biorę `B = A(0)`, a nie zespolone `A(θ_{e1})`.
4. INT8 ROT035 krok D: dla `q = round(Kn)` zachodzi `‖P(q) − P(n)‖ ≤ c/K`.
5. Nierówność trójkąta: `1 ≤ ‖E − P(n)‖ ≤ τ₁ + ℓ(q) + e + c/K`.
   - Wybieram `K = ⌊√(N/R)⌋`; wtedy `ℓ(q) = O(√(R/N)) → 0`, `c/K → 0` oraz `δ₁ → δ`.
   - Stąd `liminf e ≥ 1 − τ(δ)`. ∎

**Gdzie dowód używa samosprzężoności:** w kroku 2, bo `‖B − E‖ ≤ τ₁` wynika z twierdzenia
spektralnego. Dla niesamosprzężonego `B` rzutnik Riesza może leżeć daleko od `B` mimo małego
defektu. To dokładnie miejsce, w którym MT14 pisze „nie uzyskaliśmy dla oblique `F`”, a INT8
używa równoważności kubicznej.

**Wersja ciągła dla operatora punktowego** (dokładny lemat, ten sam dowód z `ℓ = 0` i bez kroku
4): dla rzeczywistej symetrycznej `B` z `‖B² − B‖ ≤ δ < 1/4` zachodzi
`sup_{n∈S²} ‖B − P(n)‖ ≥ 1 − τ(δ)`, z równością dla `τI` i `τQ`.

To połączenie argumentów dwóch komórek GPT, bez nowego składnika. Nowości nie zgłaszam. Ponieważ
to mój wynik, wymaga audytu spoza rodziny Claude.

## 4. Przypadek otwarty i próba numeryczna

Dla `B` rzeczywistej, ale niesymetrycznej, sprawdzałem, czy
`sup_n ‖B − P(n)‖ < 1 − τ(‖B² − B‖)` jest możliwe. Taki operator punktowy byłby kontrprzykładem
dla każdego `N`, bo supremum po wszystkich kierunkach ogranicza błąd w każdym węźle siatki.

- **Metoda:** SLSQP w postaci epigrafu z analitycznymi gradientami wartości szczególnych;
  15 startów, w tym celowo nienormalne, dla każdego `δ ∈ {.05, .09, .16, .21}`; roboczy zbiór
  160 kierunków i walidacja na 20 000.
- **Wynik:** nic poniżej frontu. Najlepszy znaleziony `B` leży `7e-12` nad frontem, a
  optymalizator dryfuje do prawie normalnych macierzy (`‖BBᵀ − BᵀB‖ ≤ 6e-4`).
- **Hipoteza `[▷]`:** front `e(1−e)` jest uniwersalny, bez samosprzężoności i bez symetrii.
  Przeszukanie lokalne tego nie dowodzi.

## 5. Próba falsyfikacji (seed `20261026`)

| test | wynik |
|---|---|
| lemat próbkowania 1D (MT14): 300 losowych hermitowskich wielomianów 6×6, w tym „szpilkowe” | `M_cont/ograniczenie ≤ 0.947`; skok/`b_N M_grid ≤ 0.734` |
| problem na prostej w klasie MT14 (`F` rzeczywisty, samosprzężony, `|d_x| ≤ R`; `N = 41`, `R ∈ {1,2}`, `δ ∈ {.01,.09,.16}`, 12 startów SLSQP) | najlepsze minimum lokalne `= 1−τ` z dokładnością `1e-10`; nigdy niżej niż tolerancja ograniczenia defektu |
| lemat próbkowania 3D (INT8, pokrycie `5π/N`): 40 losowych jąder promienia 1 | stosunek `≤ 0.494` (supremum szacowane z 4000 punktów, więc test słaby) |
| `F` punktowy równoważny kubicznie, `N = 9`, wszystkie `k ≠ 0`: 4000 losowań | 799 z `ε ∈ [1/2,1)`, 0 naruszeń `η ≥ ε(1−ε)`, minimalny zapas `3.4e-4`; brak `ε < 1/2` |
| certyfikat skończonego `N` (INT8 038.1): 24 jądra promienia 1 równoważne kubicznie wokół świadka, `N = 61`, wszystkie 226 981 `k` | 0 naruszeń; przy `N = 61` certyfikat jest często pusty (`a` do `1.32`) |
| INT8 ROT035 krok C: 200 idempotentów rzędu 2 (100 ortogonalnych, 100 skośnych) | `‖(E−P(n))T‖/‖T‖ = 1` z dokładnością `2e-15` |
| stała zaokrąglenia ROT035 krok D: 4000 losowych `n`, `K ∈ [4,400]` | `max K‖P(q)−P(n)‖ = 0.81`; ROT035 przyjmuje `32`, czyli bardzo zachowawczo |
| lemat ciągły dla symetrycznej `B` (most, `R = 0`): `δ ∈ {.05,.09,.16,.21}` | na 20 000 kierunków zawsze `≥ 1−τ` (zapas `≥ 2.6e-5`); na 160 kierunkach optymalizator schodzi do `−1.7e-4` poniżej: skończony zbiór kierunków zaniża supremum, co odpowiada członowi `c/K` |

Optymalizacja lokalna nie gwarantuje optimum globalnego, a kontrole na siatce nie są ścisłe
przedziałowo. To próba falsyfikacji, nie dowód.

## 6. Literatura i dorobek projektu (odjęcie na dwóch powierzchniach)

- **Własny dorobek INT8:** ROT035 T035.L już pokazał niewykonalność `ε < 1/2` bez równoważności
  kubicznej (dwie osie). Kroki C–D z ROT035 zawierają argument topologiczny dla dokładnych
  idempotentów. Moja pierwsza myśl, uśrednianie po trzech osiach, okazała się słabszą wersją
  T035.L; odrzuciłem ją przed zapisem. Most z §3 korzysta z ROT035, a zasługa za kroki C–D należy
  do INT8.
- **Totik**, „Bernstein type inequalities”, J. Approx. Theory 164 (2012) 1390–1401 — rekord
  potwierdzony na stronie autora. DOI `10.1016/j.jat.2012.03.002` podany przez INT8 nie
  sprawdzony: brak dostępu.
- **Odnośnik Springer w MT14** (`10.1007/s00041-024-10080-4`) — `UNKNOWN`, adres zablokowany dla
  moich narzędzi. Nierówność Bernsteina jest klasyczna (Zygmund, *Trigonometric Series*), więc
  nie jest to punkt nośny.

## Czego nie sprawdziłem

- skryptów, ZIP ani źródłowego helpera autorów;
- przypadku parzystego `N` (obaj autorzy go wyłączają);
- optymalnego progu promienia w MT14 (autor zaznacza, że (1) jest tylko dostateczny);
- fizyki (J3/K) — autorzy też jej nie twierdzą.

## Odtworzenie

```text
pip install numpy==2.1.3 scipy==1.14.1 sympy==1.13.3
python3 research/badacz/2026-10-27/code/mt14_int8_almost_projector_pair_check.py --out <katalog>
```

Około 12 minut. Wszystkie pola `verdict` mają wartość `true` z wyjątkiem
`D_nonsymmetric_open_case_hit = false`, czyli brak trafienia w przypadku otwartym. Dwa czyste
uruchomienia dały bajtowo identyczny JSON.

`NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_CLAIM`. Audyt zewnętrzny wyniku
Claude'a, zwłaszcza mostu z §3: Grok (przez Moderatora) oraz REC10.
