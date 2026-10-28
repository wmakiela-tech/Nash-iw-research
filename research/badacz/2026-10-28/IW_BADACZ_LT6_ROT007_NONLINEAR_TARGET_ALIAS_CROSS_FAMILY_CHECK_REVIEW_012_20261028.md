---
artifact_id: IW_BADACZ_LT6_ROT007_NONLINEAR_TARGET_ALIAS_CROSS_FAMILY_CHECK_REVIEW_012_20261028
exposure: PUBLIC
claim_ceiling: CROSS_FAMILY_CHECK_[▷] / PROOF_VERIFIED_LINE_BY_LINE / NUMERICAL_FALSIFICATION_ATTEMPT_NO_HIT / NOT_A_REFEREE_VERDICT / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-28
origin_cell: BADACZ (wątek Claude)
document_type: REVIEW
result_class: RESULT
task_id: BADACZ-GPT-INDEPENDENT-REVIEW-003
selection: PREREG_011, pozycja 1 (research/badacz/2026-10-28/IW_BADACZ_REVIEW_TARGET_SELECTION_UPDATE_PREREG_011_20261028.md, commit cd46c28, zatwierdzony przed lekturą celu)
target: research/lt6/2026-10-28/IW_LT6_ROT007_QUANTITATIVE_NONLINEAR_TARGET_ALIAS_001_20261028.md (autor LT6; włączony do REV026 §7.5j jako Tw. 7.16–7.17)
code: research/badacz/2026-10-28/code/lt6_rot007_ift_alias_check.py (sha256 ef21fc8dc0c6701b7ef41d64b5c95a0b68ce6d734dc4a4e10918a5d3d4ac651b)
output_sha256: 25de084c03e124605daa776b55a6f2f79932afb0eec500ba73bfbf2c5d608ca4 (lt6_rot007_ift_alias_check.json)
---

# Recenzja międzyrodzinowa LT6 ROT007: dokładne nieliniowe włókno danych z rozróżnianym celem

**Status:** `[▷]`. Sprawdzenie przez Claude'a wyniku komórki GPT. Nie jest to werdykt REC10/SW.
Kod napisałem z publicznego tekstu; skryptów autora nie czytałem.

## Wynik

**Oba twierdzenia są poprawne; nie znalazłem błędu.** Integracja w REV026 §7.5j (Tw. 7.16 i 7.17)
zgadza się z raportem. Dwie uwagi redakcyjne i jedna propozycja łącząca obie części (§3).

## 1. T007.1 — sprawdzenie krok po kroku

- `F(c) − F(0) = Ac + N(c)`, a dla `c = ±tv + A†y` mamy `A(±tv) = 0` i `AA† = I_m` (pełny rząd
  wierszowy). Stąd `F(c) = F(0) ⇔ y = −N(±tv + A†y)`. Poprawne.
- Na kuli `‖y‖ ≤ Lt²`:
  - `‖c‖ ≤ t + βLt² ≤ 5t/4` (z `βLt ≤ 1/4`), a `5t/4 ≤ R` (z `t ≤ 4R/5`);
  - `‖Φ(y)‖ ≤ (L/2)(5t/4)² = (25/32)Lt² ≤ Lt²`;
  - stała kontrakcji: `sup‖DN‖·‖A†‖ ≤ L(5t/4)β ≤ 5/16`.
  Poprawne.
- `v ∈ ker A ⊥ range A† = row A`, więc `‖c₊ − c₋‖² = 4t² + ‖A†(y₊ − y₋)‖² ≥ 4t²`. Poprawne.
- `|T(c±) − T(0) ∓ αt| ≤ Gβ‖y±‖ + (K/2)‖c±‖² ≤ (GβL + 25K/32)t² = Dt²`, a stąd
  `|T(c₊) − T(c₋)| ≥ 2|α|t − 2Dt² ≥ |α|t`. Poprawne.

## 2. T007.2 — sprawdzenie

- Weyl: `σ_m(A) ≥ s − ε_A > 0`, więc rzędy `A` i `Ã` są równe `m`.
- Dla jednostkowego `x = Aᵀλ ∈ row A` zachodzi `‖λ‖ ≤ 1/(s − ε_A)`, a
  `‖x − Ãᵀλ‖ ≤ ε_A/(s − ε_A) =: γ`.
- Przy równych wymiarach `‖P_A − P_Ã‖ = sup_{x ∈ row A, ‖x‖=1} dist(x, row Ã) ≤ γ`.
- Nierówność trójkąta: `‖(I−P_A)g‖ ≥ ‖(I−P_Ã)ĝ‖ − ε_g − γ‖ĝ‖`.

Poprawne. Gospodarz: Wedin, *Perturbation bounds in connection with the singular value
decomposition*, BIT 12 (1972) 99–111, DOI 10.1007/BF01932678 (rekord sprawdzony). Wersja autora
z `γ = ε_A/(s−ε_A)` jest odrobinę słabsza od klasycznej, ale poprawna i obliczalna z `Ã`.

## 3. Uwagi

1. **Stała w T007.1 (redakcyjna).** Dowód daje `‖y±‖ ≤ (25/32)Lt²`, ostrzej niż deklarowane
   `Lt²`. W `D` można by więc użyć `(25/32)GβL`. Twierdzenie jest poprawne bez tej zmiany.
   Numerycznie stałe są zachowawcze mniej więcej dwukrotnie (§4).
2. **Połączenie T007.2 → T007.1 (propozycja, nie poprawka).** Dla `v = (I−P_A)g/‖(I−P_A)g‖`
   zachodzi `α = dist(g, row A)`, więc prawa strona T007.2 jest **certyfikowaną dolną granicą
   `|α|`**, a nie tylko świadectwem `α ≠ 0`. Pełny obliczalny certyfikat istnienia aliasu:
   - `α_c` = prawa strona T007.2;
   - `β_c = 1/(s − ε_A)`;
   - `G_c = ‖ĝ‖ + ε_g`;
   - źródłowe `L`, `K`, `R`;
   - wtedy `t ≤ min(4R/5, 1/(4β_c L), α_c/(2D_c))` wystarcza.

   Kierunek `v` pozostaje nieznany (leży w `ker A`, nie w `ker Ã`), ale do twierdzenia o
   istnieniu nie jest potrzebny. Wąskim gardłem pozostają źródłowe `L`, `K` (hesjany mapy
   ODE), co STOP autora słusznie zaznacza.
3. **Relacja do MT14 ROT009.** Zgodna z tekstem autora. Borsuk–Ulam daje parę antypodalną o
   równych odczytach, ale nie rozróżnia celu. T007.1 daje rozróżnienie przy transwersalności
   `α ≠ 0`. Przykłady `T_flat` i `T_even` pokazują, że warunek jest dostateczny, nie konieczny.
   Sprawdzone dokładnie.

## 4. Próba falsyfikacji (seed `20261028`)

| test | wynik |
|---|---|
| przykład autora (SymPy): `F(c±) = 0`; `T(c₊) = 99/1000`, `T(c₋) = −101/1000`; założenia przy `t = 0.1` z `L = √5`, `K = 0`, `G = √1.04`, `β = 1`; `‖y‖ ≤ Lt²`; `T_flat` stały na włóknie, `T_even(c₊) = T_even(c₋)`; naiwne `±t e_z` daje `F = (t²/2, t²) ≠ 0` | wszystko zgodne |
| T007.1 na 400 losowych mapach `C²` (kwadratowa + sinusowa, certyfikowane `L`, `K`; `m ≤ 3`, `n ≤ m+3`), `t` do największej dopuszczalnej wartości, punkt stały przez kontrakcję z dowodu | 0 naruszeń; residuum `F` `≤ 3.8e-16`; krok Taylora zużywa `≤ 48%` budżetu `Dt²`; `‖y‖ ≤ 45%` `Lt²`; `|T(c₊)−T(c₋)| ≥ 1.98 |α|t` |
| T007.2 na 4000 przypadkach (połowa losowa, połowa z perturbacją wpychającą najsłabszy kierunek wierszy w `ker A`) | 0 naruszeń; minimalny zapas `0.011`; 2880 dodatnich certyfikatów |

Testy nie są przedziałowo ścisłe. To próba falsyfikacji, nie dowód.

## Czego nie sprawdziłem

- skryptu i ZIP autora;
- źródłowych `L`, `K`, `ε_A`, `ε_g` dla rzeczywistej mapy Mech (nie istnieją; zgodnie ze STOP
  autora);
- fizyki PBH/BBN.

## Odtworzenie

```text
pip install numpy==2.1.3 sympy==1.13.3
python3 research/badacz/2026-10-28/code/lt6_rot007_ift_alias_check.py --out <katalog>
```

Około 6 s. Wszystkie pola `verdict` mają wartość `true`. Dwa czyste uruchomienia dały identyczny
JSON.

`NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_CLAIM`. Audyt zewnętrzny wyniku Claude'a:
według kolejki AUD1.
