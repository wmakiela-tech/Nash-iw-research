---
artifact_id: IW_BADACZ_AUDIT_TESTS_PREREG_032_XH_S5_ROT013_014_20261030
exposure: PUBLIC
claim_ceiling: PREREGISTRATION / TESTS_ONLY / NO_RESULT / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-30
origin_cell: BADACZ (wątek Claude)
document_type: PREREG
task_id: BADACZ-GPT-INDEPENDENT-REVIEW-010
selection: cel drugi z PREREG_030 (commit 1a33bb3)
---

# Testy dla XH-S5 ROT013/014, ustalone przed czytaniem ciał raportów

Znam tylko zwroty XH-S5 na #iw-dispatch (29 X, 21:54 i 22:00). Twierdzenie: diagnostyki z Comisso &
Asenjo, Phys. Rev. D 114, 084095 (2026), arXiv:2609.25241 (równania 28 i 31), zależą od wyboru reperu
lokalnego Lorentza przy tej samej płaskiej metryce i tym samym obserwatorze.

## Testy

- **X1:** oba korepery (kontrolny `α = 0` i aktywny) dają metrykę `diag(−1, 1, 1, 1)` (SymPy, dokładnie).
- **X2:** `F¹ = de¹` w `t = 0`, w początku układu: `F_ty = 2/5`, `F_xz = 7/10`, wyznacznik `49/625`,
  rząd 4.
- **X3:** `∫_{−1}^{1} exp(1 − 1/(1 − y²)) dy = 1.2069003224378765`, a całka typu Eq. 31 wzdłuż
  `x = z = 0` wynosi `0.4 · C = 0.48276…`.
- **X4 (ROT014):** z `α = κ h(t) f(y)` i `h(t) = t f(t)` reper aktywny pokrywa się z kontrolnym w `t = 0`
  i dla `|t| ≥ 1`, a całka wynosi `|κ| C`, czyli nie jest ograniczona.
- **X5 (rozstrzygający):** odczytuję w źródle (arXiv:2609.25241), z czego zbudowane są Eq. 28 i 31.
  - Jeśli są budowane z `de^a` przy dowolnym reperze (teleparalelizm „czystego reperu”, bez połączenia
    spinowego), kontrprzykład XH jest trafny.
  - Jeśli używają kowariantnej torsji `T^a = de^a + ω^a_b ∧ e^b` z połączeniem spinowym transformującym
    się razem z reperem albo jawnie ustalają klasę reperów, to obrót reperu przy `ω = 0` nie jest
    dopuszczalną transformacją, a kontrprzykład trafia w model słomiany.
- **X6:** czy XH-S5 przypisuje autorom coś, czego ci nie twierdzą (sprawdzam cytaty).

**Falsyfikatory:** inna metryka, inne `F¹`, inna całka albo X5 w drugim wariancie.

Werdykt każdego testu ogłaszam niezależnie od kierunku. Wynik jest Claude'a i wymaga audytu spoza
rodziny Claude.
