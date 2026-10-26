---
artifact_id: IW_BADACZ_LT6_ROT003_TRANSFER_CERTIFICATE_CROSS_FAMILY_CHECK_REVIEW_005_20261026
exposure: PUBLIC
claim_ceiling: CROSS_FAMILY_CHECK_[▷] / PROOF_VERIFIED_LINE_BY_LINE / NUMERICAL_FALSIFICATION_ATTEMPT_NO_HIT / NOT_A_REFEREE_VERDICT / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-26
origin_cell: BADACZ (wątek Claude)
document_type: REVIEW
result_class: RESULT
task_id: BADACZ-FRONT-WEAKEST-POINT-001
target: research/lt6/2026-10-26/IW_LT6_ROT003_VARIABLE_OPERATOR_TARGET_TRANSFER_CERTIFICATE_001_20261026.md (autor LT6; dodatek do roboczej monografii, ostatni zatwierdzający recenzent: brak)
selection: najnowszy dodatek do monografii z jawną nierównością i bez recenzji innej komórki w publicznym korpusie; reguła zadeklarowana w tym pliku po przeczytaniu streszczenia ze Slacka, a przed sprawdzeniem
code: research/badacz/2026-10-26/code/lt6_rot003_sandwich_check.py (sha256 70df32fdae9be0a6236d32e484f32b37fedacc28573914f5e11702baed1caf01)
---

# Recenzja międzyrodzinowa LT6 ROT003: certyfikat przeniesienia celu między tłami

**Status:** `[▷]`. Sprawdzenie przez Claude'a wyniku komórki GPT. Nie jest to werdykt REC10/SW.

## Wynik

Wszystkie cztery twierdzenia notatki są poprawne przy założeniach podanych przez autora:
górna i dolna nierówność kanapkowa, dualne LP, certyfikat na siatce oraz kontrprzykład utraty
rzędu. Nie znalazłem błędu. Jest to elementarna, dojrzała matematyka; autor też nie zgłasza
nowości.

**Dowód sprawdzony krok po kroku.** Oznaczam `K_θ(δ) = {c : ‖c‖∞ ≤ 1, |A_θ c| ≤ δ}`.

- **Górna nierówność.** Z Höldera dla każdego wiersza
  `|(A₀c)_j| ≤ |(A_θc)_j| + ‖(A_θ−A₀)_j‖₁ ‖c‖∞ ≤ δ_j + η_j`, więc `K_θ(δ) ⊂ K₀(δ+η)`.
  Zachodzi też `|g_θ·c| ≤ |g₀·c| + ρ`.
- **Dolna nierówność.** Przy `δ ≥ η` symetrycznie `K₀(δ−η) ⊂ K_θ(δ)`, a
  `|g_θ·c| ≥ |g₀·c| − ρ`.
- **Siatka.** Każde `θ` leży w odległości `≤ h` od węzła, więc `η_j = hL_{A,j}` i `ρ = hL_g`.
  Dolna granica supremum jest trywialna, bo węzły należą do przedziału.
- **Dualność LP.** Dual `min_λ ‖g − Aᵀλ‖₁ + Σ δ_j|λ_j|` zachodzi z silną dualnością, bo
  `c = 0` jest dopuszczalne.

**Próba falsyfikacji numerycznej** (seed `20261026`, scipy HiGHS):

| test | wynik |
|---|---|
| U i L na 300 losowych instancjach (`n ≤ 6`, `m ≤ 4`, perturbacje wierszy dokładnie w normie `ℓ₁ ≤ η`) | 0 naruszeń; minimalny zapas U `0.0107`, L `0.0038` |
| zgodność primal–dual | maksymalna różnica `2.0e-13` |
| 40 liniowych rodzin teł, 6 węzłów, `h = 0.1`, gęsta kontrola 401 punktów | 0 naruszeń |
| przykład utraty rzędu (`ε = 1e-6`) | `B = 0, 1, 1` dokładnie jak w notatce |

Test na siatce sprawdza tylko konieczny warunek górnej granicy: maksimum na gęstej siatce nie
jest supremum, więc dowodem pozostaje argument analityczny.

## Czego nie sprawdziłem

Liczbowego przedziału przykładu autora, `[0.0545782160631, 0.0578728703144]`. Dane wejściowe
(`A₀`, `g₀`, `E`, `v`) są tylko w prywatnym archiwum, a autor sam zaznacza, że to obliczenie LP w
arytmetyce zmiennoprzecinkowej, nie dowód przedziałowy.

Zgadzam się z ostrzeżeniem autora: siatka bez udowodnionych stałych Lipschitza nie daje górnej
granicy globalnej. Z tego wynika jedna uwaga. W zastosowaniu do Front B stałe `L_A` i `L_g`
muszą wynikać ze źródła, a nie z próbkowania. Inaczej certyfikat jest tylko warunkowy.

## Odtworzenie

```text
pip install numpy==2.1.3 scipy==1.14.1
python3 research/badacz/2026-10-26/code/lt6_rot003_sandwich_check.py --out <katalog>
```

Około 15 s. Wszystkie pola `verdict` mają wartość `true`. Status: `AUTHOR_REPRODUCED`.

`NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_CLAIM`. Audyt zewnętrzny wyniku
Claude'a: Grok.
