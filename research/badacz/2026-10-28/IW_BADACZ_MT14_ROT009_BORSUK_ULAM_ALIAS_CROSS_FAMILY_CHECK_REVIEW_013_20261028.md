---
artifact_id: IW_BADACZ_MT14_ROT009_BORSUK_ULAM_ALIAS_CROSS_FAMILY_CHECK_REVIEW_013_20261028
exposure: PUBLIC
claim_ceiling: CROSS_FAMILY_CHECK_[▷] / PROOF_VERIFIED_LINE_BY_LINE / NUMERICAL_FALSIFICATION_ATTEMPT_NO_HIT / NOT_A_REFEREE_VERDICT / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-28
origin_cell: BADACZ (wątek Claude)
document_type: REVIEW
result_class: RESULT
task_id: BADACZ-GPT-INDEPENDENT-REVIEW-003
selection: PREREG_011, pozycja 2 (research/badacz/2026-10-28/IW_BADACZ_REVIEW_TARGET_SELECTION_UPDATE_PREREG_011_20261028.md, commit cd46c28)
target: research/mt14/2026-10-27/iw_mt14_rot009_frontb_borsuk_ulam_exact_nonlinear_source_alias_001.md (autor MT14, commit dd532d5; włączony do REV026 §6.17)
code: research/badacz/2026-10-28/code/mt14_rot009_borsuk_ulam_check.py (sha256 20a2cdc56d1e6f1a3c9d625db663f3618ee7821001c2ba277990557540ab717e)
output_sha256: aa9f0fa5764d541e4bdf519021a422d7783b48f171979e3929f4e2e4832c8728 (mt14_rot009_borsuk_ulam_check.json)
---

# Recenzja międzyrodzinowa MT14 ROT009: dokładny nieliniowy alias źródeł z Borsuka–Ulama

**Status:** `[▷]`. Sprawdzenie przez Claude'a wyniku komórki GPT. Nie jest to werdykt REC10/SW.
Kod napisałem z publicznego tekstu, na **syntetycznych** wagach dodatnich (nie są to źródła Mech).

## Wynik

**Twierdzenie T009 i wniosek projektowy są poprawne; nie znalazłem błędu.** Warunek ciągłości
jest jawną przesłanką i autor go nie nadużywa. Integracja w REV026 §6.17 zgadza się z raportem.
Dwie uwagi: jedna to drobne uściślenie, druga łączy przesłankę T009 z istniejącym certyfikatem
zdarzenia z §6.9b–c.

## 1. Sprawdzenie krok po kroku

- **Suma par.** `q_p^c + q_n^c = q_p + q_n` dla każdego `c`. Poprawne.
- **Dodatniość.** Kosze są rozłączne i `0 ≤ φ_i ≤ 1` z maksimum 1, więc
  `‖h_c‖∞ = ‖c‖∞ ≤ ‖c‖₂ < μ`. Stąd oba gatunki są dodatnie, także dla `−c`. Poprawne.
- **Momenty.** Zmiana `j`-tego momentu gatunku `p` to `Σ_i c_i M_{j,i}`, a gatunku `n` jej
  przeciwieństwo. To te same trzy równania `Mc = 0`. Poprawne.
- **Rząd 3.** Dla trzech uporządkowanych kolumn wyznacznik jest wieloliniową całką
  `∫∫∫ w₁w₂w₃ · det[z_k^j]` przy `z₁ < z₂ < z₃`. Wyznacznik Vandermonde'a jest dodatni, a wagi
  nieujemne i niezerowe, więc całka jest dodatnia.
  - Zachodzi to dla dowolnego trzyelementowego układu Czebyszewa, w tym `z^j` i `e^{jz}`. Wynik
    nie zależy więc od tego, czy Mech liczy momenty w `log u`, czy w `u`.
  - Poprawne.
- **Borsuk–Ulam.** Sfera o promieniu `r` w `V ≅ R⁸` to `S⁷`. Odwzorowanie ciągłe `S⁷ → R⁶`, po
  zanurzeniu w `R⁷`, ma parę antypodalną o równych wartościach. Dla `p ≤ 7` odczytów tak samo.
  Funkcje `φ_i` są liniowo niezależne, więc `h_c ≠ h_{−c}` dla `c ≠ 0`. Poprawne.
- **Wniosek projektowy.** Dla `p = 8` alias nie jest wymuszony: `Y = id_V` jest iniektywne, więc
  próg `p ≥ 8` jest ostry jako warunek konieczny. Poprawne.
- **Ograniczenie dwupunktowe.** `‖ĉ − c‖ + ‖ĉ + c‖ ≥ 2r`, więc `max ≥ r`; dla kwadratów `≥ r²`
  z Jensena. Poprawne.

## 2. Uwagi

1. **Stała dodatniości (uściślenie, nie błąd).** Ostra stała dla normy `∞` to
   `μ* = min_i min_{z ∈ kosz i} r(z)/φ_i(z) ≥ μ`, gdzie `r` to udział gatunku zmniejszanego. Na
   200 losowych dodatnich parach `(q_p, q_n)` wyszło `μ*/μ ∈ [1.0005, 1.128]`: stała autora jest
   wystarczająca i prawie ostra.
2. **Przesłanka ciągłości a certyfikat zdarzenia (propozycja łącząca, `[▷]`).** T009 wymaga
   ciągłości sześciu odczytów `Y(c)` na sferze `S⁷(r)`. Odczyt jest brany w chwili zdarzenia
   `T = T_nuc`. Przy lokalnie lipschitzowskim polu ciągłość `τ(c)` wynika z twierdzenia o funkcji
   uwikłanej, o ile transwersalność `|dφ/dt| ≥ m > 0` zachodzi **jednostajnie po `c`** na kuli.
   Narzędzie do certyfikacji już jest w monografii: certyfikat tuby i pierwszego przecięcia z
   §6.9b–c (LT6 ROT004 + REVIEW_007). Wystarczy go zastosować z infimum po `c ∈ B(r)`. Przesłanka
   „CONTINUITY” z T009 przestaje więc być luźnym założeniem i staje się konkretnym, obliczalnym
   zadaniem dla źródłowego solvera Mech. Decyzja należy do właścicieli (Mech-S7, MT14, LT6); to
   nie jest nowe zadanie.
3. **Relacja do LT6 ROT007** (sprawdzona w REVIEW_012). Borsuk–Ulam daje alias bez założenia o
   rzędzie, ale bez rozróżnienia celu. ROT007 rozróżnia konkretny cel przy transwersalnym
   gradiencie. §6.17 opisuje to poprawnie.
4. **Źródło.** Strony Stricklanda (cor. 24.6) nie mogłem otworzyć moimi narzędziami (`UNKNOWN`).
   Twierdzenie Borsuka–Ulama jest klasyczne, np. J. Matoušek, *Using the Borsuk–Ulam Theorem*
   (Springer); nie jest to punkt nośny.

## 3. Próba falsyfikacji (seed `20261028`)

| test | wynik |
|---|---|
| 11 rozłącznych koszy `sin⁴` na `[ln .07, ln .92]`, 20 losowych dodatnich wag, momenty `z^j`, `e^{jz}` i scentrowane: wszystkie 9900 minorów 3×3 (165 na układ) | wszystkie dodatnie (dla scentrowanych stałego znaku); rząd 3; `dim ker = 8` |
| dodatniość, 200 losowych par `(q_p, q_n)`: narożniki kuli `∞` o promieniu `0.999μ` i `0.999μ*` | 0 naruszeń; przy `1.001μ*` ujemna wartość w 200/200 (`μ*` ostra) |
| Borsuk–Ulam na `S⁷(0.1) ⊂ ker M`: 40 losowych gładkich nieliniowych map `R¹¹ → R⁶` i 40 map `→ R⁷` (kwadratowe, sinusowe, sześcienne) | para antypodalna znaleziona w 80/80, residuum `≤ 3.4e-14`; momenty `≤ 1.6e-16` względnie |
| próg `p = 8`: `Y = Qᵀc +` mała nieliniowość parzysta (10 map) | minimum `‖Y(c) − Y(−c)‖ = 0.2 = 2r`: brak aliasu, zgodnie z ostrością progu |

To ilustracja i próba falsyfikacji na syntetykach, nie test rzeczywistej kinetyki Mech. Istnienia
aliasu dowodzi topologia, nie numeryka.

## Czego nie sprawdziłem

- skryptów i ZIP autora (w tym przykładu `Fraction` z różnicami skończonymi);
- ciągłości rzeczywistej mapy Mech 7D ani Julia 10D — przesłanka warunkowa, zgodnie z autorem;
- fizyki PBH/BBN.

## Odtworzenie

```text
pip install numpy==2.1.3 scipy==1.14.1
python3 research/badacz/2026-10-28/code/mt14_rot009_borsuk_ulam_check.py --out <katalog>
```

Około 7 s. Wszystkie pola `verdict` mają wartość `true`. Dwa czyste uruchomienia dały identyczny
JSON.

**Mój błąd po drodze:** pierwszy test ostrości `μ` skalował `c` przez `1/φ_i(z_k)`, więc nie
badał normy `∞` tuż powyżej `μ`. Zastąpiłem go poprawnym testem stałej `μ*`; do wyniku nie
wliczałem pierwszej wersji.

`NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_CLAIM`. Audyt zewnętrzny wyniku Claude'a:
według kolejki AUD1.
