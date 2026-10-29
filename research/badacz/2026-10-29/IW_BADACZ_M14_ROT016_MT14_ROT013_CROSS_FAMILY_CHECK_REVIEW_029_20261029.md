---
artifact_id: IW_BADACZ_M14_ROT016_MT14_ROT013_CROSS_FAMILY_CHECK_REVIEW_029_20261029
exposure: PUBLIC
claim_ceiling: CROSS_FAMILY_CHECK_[▷] / EXACT_SYMBOLIC_REPRODUCTION / NOT_A_REFEREE_VERDICT / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_CLAIM
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-29
origin_cell: BADACZ (wątek Claude)
document_type: REVIEW
result_class: RESULT
task_id: BADACZ-GPT-INDEPENDENT-REVIEW-008
targets: M14 ROT016 (research/m14/2026-10-29/iw_m14_rot016_unknown_center_five_tone_fisher_fold_six_tone_repair_001.md, commit 9d45f27); MT14 ROT013 (research/mt14/2026-10-29/iw_mt14_rot013_scientific_programme_alignment_and_model_error_transfer_gate_001.md, commit 5f36f4a), tylko bramka ε*
code: research/badacz/2026-10-29/code/m14_rot016_mt14_rot013_exact_checks.py (sha256 87310a716f992c4aa7e3365874cc7aac360fe76736cdfbeec28d95a29b679313)
output_sha256: 7f613157d92e61cd50086ae2d50cc37ffd1e1f37552900fe767b55201606887a
---

# Sprawdzenie międzyrodzinowe M14 ROT016 i bramki ε* z MT14 ROT013

**Status:** `[▷]`. Claude sprawdza wyniki komórek GPT. To nie jest werdykt REC10/SW. M14 ROT016 nie ma
publicznego kodu (zapis kodu do GitHub był zablokowany), więc model odtworzyłem wyłącznie z treści
raportu.

## Wynik

**M14 ROT016: wszystkie twierdzenia odtworzone dokładnie.** Nie znalazłem rozbieżności.

| twierdzenie M14 | mój wynik |
|---|---|
| Minor `O12 = U(1)Q(2) − U(2)Q(1)` ma czynnik `d³ g P(d²)` | licznik równy `−2048·d³·g·P(d²)`; mianownik `81·Π(2d² ± 8d + 9)²(2d² ± 4d + 3)²`, dodatni (wyróżniki ujemne) |
| Minor `O13` ma czynnik `d³ g T(d²)` | licznik równy `−8192·d³·g·T(d²)` |
| `gcd(P, T) = 1` | potwierdzone |
| Dokładnie jeden pierwiastek `P` na `z ∈ (0, 1)` | `z = 0.088575776253157`, czyli `d★ = 0.29761682790654983`; przedział wymierny `(0.29761682, 0.29761684)` potwierdzony; ograniczenie `P′ ≤ −1804` poprawne |
| Wyznacznik bloku parzystego 3×3 | równy podanemu wzorowi tożsamościowo |
| `lim_{d→0} I_eff/d⁴ = 12544/399466485` | `d = 1e-5` daje `3.1401883376e-5` wobec `3.1401883440e-5`; zbieżność `O(d²)` |
| `I_eff5(d★) = 0` | `|I_eff5| < 1e-40` (60 cyfr) |
| `I_eff6(d★) = 2.23563461214e-8` | zgodne do 12 cyfr |
| `I_eff7(d★) = 7.83201427065e-8` | zgodne do 12 cyfr |

Uwaga do formy: bloki parzysty i nieparzysty rozdzielają się dzięki symetrii tonów `±x` w punkcie
bazowym `u = q = 0`, `a = g/2`. Wszystkie wnioski są więc lokalne, co M14 sam zaznacza. Uwag
merytorycznych nie mam.

**MT14 ROT013, bramka ε*: poprawna, a z REVIEW_027 da się ją zaostrzyć.**

- **Kryterium.** Warunek `d > 2ε` dla niezależnych kul wokół wersorów pozostaje poprawny także przy
  profilowanym dodatnim wzmocnieniu, czyli gdy porównujemy stożki, a nie punkty. Stożek nad
  `B(u, ε)` ma półkąt `arcsin ε`, a `d = 2 sin(θ/2)`. Stożki się przecinają wtedy i tylko wtedy, gdy
  `θ/2 ≤ arcsin ε`, czyli `d ≤ 2ε`. Wniosek MT14 nie zależy więc od tego, czy obserwacja jest
  normalizowana.
- **Liczby.** `(0.0011034044962, 0.0011072495216)` odtworzone z przedziału ROT012.
- **Zaostrzenie** z REVIEW_027 (`m_B ∈ [4.90375906e-6, 4.9037590616144e-6]` na przedziałach źródła M13):
  **`ε* ∈ [0.00110722232091, 0.00110722232110]`**, czyli względnie `1.6e-10`. Dla zakresu
  `0.11034–0.11073%` z ROT013 oznacza to, że cała szerokość tego zakresu pochodzi z luźnego dolnego
  ograniczenia ROT012. Wartość rzeczywista leży tuż przy jego górnym końcu: `0.1107222%`. Dotyczy to
  realizacji źródła M13. Dla pudełek MT14 `C ± 1e-8` mam tylko `m_B ≥ 4.89e-6`.

## Czego nie sprawdziłem

- Skryptów M14 (lokalne u Moderatora) ani 105 kontroli różnic skończonych.
- Części fizycznej i relacji do urządzenia Schall NV. M14 słusznie zaznacza, że jej nie ma.
- Pozostałych części MT14 ROT013 (mapy programu, decyzji właścicieli).

## Literatura i dorobek projektu

- **Zewnętrzna:** informacja Fishera dla Poissona z uzupełnieniem Schura; algorytm Euklidesa dla `gcd`
  wielomianów; geometria stożków nad kulami.
- **Własna:** M14 ROT013–016, XH-S5 ROT007, moje REVIEW_020 (zero Fishera w XH ROT007), MT14
  ROT012/013 i moje REVIEW_027.
- Nowości nie zgłaszam.

## Odtworzenie

```text
pip install sympy==1.13.3 mpmath==1.3.0
python3 -I research/badacz/2026-10-29/code/m14_rot016_mt14_rot013_exact_checks.py --out <plik.json>
```

Około 1 minuty. Dwa przebiegi dały identyczny JSON. Wszystkie `verdicts` mają wartość `true`.

## Powrót w trzech warstwach

- **Wynik:** M14 ROT016 odtworzony dokładnie, bez rozbieżności. Bramka ε* z MT14 ROT013 jest
  poprawna; po zaostrzeniu `ε* = 0.1107222%` dla źródła M13.
- **Konfiguracja:** raport M14 był na tyle kompletny, że model dało się odtworzyć bez kodu. Wzorzec
  wart powtarzania: jawny kontrakt modelu w raporcie publicznym.
- **Uczenie systemu:** nic nowego. Gdy przedział jest luźny po jednej stronie, propagacja do wielkości
  pochodnych dziedziczy luz; warto podawać, która strona jest ostra.

Wynik jest Claude'a, więc wymaga audytu spoza rodziny Claude.
