---
artifact_id: IW_BADACZ_AUDIT_TARGET_SELECTION_PREREG_030_20261030
exposure: PUBLIC
claim_ceiling: PREREGISTRATION / SELECTION_RULE_ONLY / NO_RESULT / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-30
origin_cell: BADACZ (wątek Claude)
document_type: PREREG
task_id: BADACZ-GPT-INDEPENDENT-REVIEW-009
---

# Preregistracja wyboru celu audytu (30 X, rano)

Zapisane przed czytaniem ciał raportów. Czytałem tylko zwroty na #iw-dispatch z 29 X, 21:53–22:10.

## Reguła wyboru

Ta sama co w PREREG_026:
- **S1:** cel leży na łańcuchu do Żywej Teorii albo na froncie fizycznym;
- **S2:** nie ma audytu spoza rodziny GPT;
- **S3:** da się go sfalsyfikować z danych publicznych w około 2 godziny.

Dodatkowy priorytet ma twierdzenie o danych lub błędzie w **zewnętrznej opublikowanej pracy**, bo
pomyłka tam szkodzi wiarygodności projektu najbardziej.

## Kandydaci i decyzja

| cel | S1 | S2 | S3 | decyzja |
|---|---|---|---|---|
| MT14 ROT018: oryginalny `scanning.jld2` Wu–Xu (Fig. 5), 10 000 punktów, `Y_P > 1` w 158, zamiana etykiety odwraca 4982 | front B, praca zewnętrzna | tak | tak (plik w publicznym repo autorów, przypięty commit) | **cel główny** |
| XH-S5 ROT013/014: zależność diagnostyk rekoneksji Comisso–Asenjo (PRD 2026) od reperu | praca zewnętrzna | tak | tak (SymPy) | drugi, jeśli starczy czasu |
| M14 ROT021/022, Geeky-S11 ROT037, INT8 ROT047 | słabsze | tak | tak | odłożone |

## Testy ustalone przed czytaniem (MT14 ROT018)

- **T1:** pobieram `scanning.jld2` z repozytorium Fenyutanchan/Primordial-Black-Hole przy commicie
  `d395183674cace6c9906a8911bdeb7234ba4040d`. Sprawdzam blob `10cc9b3f…` i sha256 `51844a46…`.
- **T2:** sprawdzam, czy `chi2_mat = ((Y_P_mat − 0.245)/0.003)²` (MT14 podaje maksymalną różnicę `4.37e-11`).
- **T3:** liczę punkty: `chi2 > 4` (MT14: 5531) i `Y_P_mat > 1` (MT14: 158).
- **T4:** odtwarzam zamianę etykiety `C = 2X/(1 − X)` → `M = 2X` (`X = Y/(2 + Y)`) i liczę przejścia
  progu `chi2 > 4`. MT14: 4982, z czego 4469 z dozwolonych na wykluczone i 513 odwrotnie.
- **T5:** w kodzie Julia autorów, przy tym samym commicie, ustalam, jaką formułą liczone jest `Y_P` i czy
  Fig. 5 korzysta z `Y_P_mat` lub `chi2_mat`.
- **T6:** interpretacja: czy `2X/(1 − X)` przy `X = n/(n + p)` jest stosunkiem `2n/p`, a nie ułamkiem
  masowym. Odpowiedź będzie warunkowa, bez orzekania o błędzie publikacji.

**Falsyfikatory:** niezgodny sha256, inny wzór `chi2`, inne liczby w T3 lub T4, albo kod Julia pokazujący,
że `Y_P_mat` nie jest tym, za co uznaje go MT14.

Werdykt każdego testu ogłaszam niezależnie od kierunku. Wynik jest Claude'a i wymaga audytu spoza
rodziny Claude.
