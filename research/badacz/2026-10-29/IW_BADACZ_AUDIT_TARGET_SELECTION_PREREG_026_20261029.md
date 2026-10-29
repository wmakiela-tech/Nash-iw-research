---
artifact_id: IW_BADACZ_AUDIT_TARGET_SELECTION_PREREG_026_20261029
exposure: PUBLIC
claim_ceiling: PREREGISTRATION / SELECTION_RULE_ONLY / NO_RESULT / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-29
origin_cell: BADACZ (wątek Claude)
document_type: PREREG
task_id: BADACZ-GPT-INDEPENDENT-REVIEW-007
---

# Preregistracja wyboru celu audytu (obrót 29 X, wieczór)

Zapisane przed czytaniem ciał raportów. Czytałem tylko zwroty na #iw-dispatch z 29 X, 13:38–13:58.

## Reguła wyboru

Cel musi spełniać trzy warunki:
- **S1:** leży na łańcuchu do Żywej Teorii albo ma sufit „CERTIFIED” lub „EXACT”;
- **S2:** nie ma jeszcze audytu spoza rodziny GPT; nie widzę też audytu AUD1 ani REC10;
- **S3:** da się go sfalsyfikować moim niezależnym kodem z danych publicznych w ciągu około 2 godzin.

## Kandydaci i decyzja

| cel | S1 | S2 | S3 | decyzja |
|---|---|---|---|---|
| MT14 ROT012 (dokładny przedział `m_B`, zasób gaussowski) | tak (`SOURCE_CONDITIONAL_CERTIFIED`) | tak | tak (`research/m13/2026-10-26/direct_B.json` jest publiczny) | **cel główny** |
| Mech-S7 ROT034 (promień przy dwóch pomiarach z ograniczonym szumem) | tak (zasila LT §6.19) | tak | częściowo: wzór i tabela tak, przebiegi ODE nie (ZIP lokalny u Moderatora) | **cel drugi**, w zakresie wzoru, tabeli i logiki |
| pozostałe (M14 ROT014/015, Geeky-S11 ROT032/033, XH-S5 ROT008/009, INT8 ROT041/042) | słabsze | tak | nie sprawdzałem | odłożone |

## Testy ustalone przed czytaniem

**MT14 ROT012**
- **C1:** `ρ²(0.20, 0.19)` liczę na 60 cyfrach z punktów środkowych przedziałów źródła i z obu końców. Falsyfikator: wartość dla punktu środkowego poza `(4.903744074886575e-6, 4.903774041472931e-6)`.
- **C2:** globalne przeszukanie `α ∈ [0, 0.2]`, `|α − β| ≥ 0.01`, siatka plus lokalne doprecyzowanie. Falsyfikator: jakakolwiek para z `ρ² < 4.87e-6` przy współczynnikach z pudełek.
- **C3:** wzór Bayesa `P = Φ(√(n·SNR²·ρ²)/2)` i próg 371074: postać zamknięta plus Monte Carlo.
- **C4:** analiza słowna, czy „warunek konieczny” jest poprawny przy nieznanym wzmocnieniu i ograniczeniu `t > 0`.

**Mech-S7 ROT034**
- **C5:** wzór dualny na promień, sprawdzany na losowych instancjach skończenie wymiarowych (prymal wypukły kontra dual), łącznie z `δ = 0` i przypadkami zdegenerowanymi.
- **C6:** zakres dwupunktowego dolnego ograniczenia (Le Cam): co wolno z niego wnioskować.
- **C7:** wewnętrzna zgodność tabeli: wiersz „jeden pomiar” z wzoru `η·cos θ + sin θ·√(1 − η²)`; wiersz „dwa pomiary” z macierzy Grama odtworzonej z liczb w raporcie, o ile raport je podaje.
- **C8:** zgodność nieliniowej połowy luki z liniowym nośnikiem względem nieznanego błędu solvera.

Werdykt każdego testu ogłaszam niezależnie od kierunku. Wynik jest Claude'a i wymaga audytu spoza rodziny Claude.
