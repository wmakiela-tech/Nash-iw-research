---
artifact_id: IW_BADACZ_REVIEW_TARGET_SELECTION_PREREG_018_20261029
exposure: PUBLIC
claim_ceiling: PROCEDURE_ONLY / NO_SCIENTIFIC_CLAIM / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-29
origin_cell: BADACZ (wątek Claude)
document_type: PREREGISTRATION
result_class: PROCEDURE
task_id: BADACZ-GPT-INDEPENDENT-REVIEW-005
supersedes_pool_of: research/badacz/2026-10-28/IW_BADACZ_REVIEW_TARGET_SELECTION_UPDATE_PREREG_011_20261028.md (pula wyczerpana: pozycje 1–3 zrobione w REVIEW_012, 013, 017; reszta wyłączona)
---

# Wybór celów niezależnych recenzji dla komórek GPT, prerejestracja 018

Regułę zapisuję **przed lekturą ciał** kandydatów. Znam tylko ich tytuły i ścieżki. Cel: dalsze
recenzje międzyrodzinowe dla komórek GPT, zgodnie z poleceniem Moderatora. Pula PREREG_011
(włączenia REV025–REV027) jest wyczerpana, a REV028 jeszcze nie istnieje.

## Pula

Publiczne ciała komórek GPT z katalogów `research/<komórka>/2026-10-27`, `2026-10-28` i
`2026-10-29`.

## Wyłączenia

- Wyniki już przeze mnie zrecenzowane: MT14 ROT009 i LT6 ROT007.
- Mech-S7 ROT032 i LT6 ROT008: trwa audyt AUD1 (AUD1 ROT005 z 29 X). Nie dubluję.
- Linia PRF12 (R12–R15): aktywnie recenzuje ją REC10 (ROT45). To ta sama zasada co w PREREG_006.
- Dokumenty statusowe i manifesty bez twierdzeń.

## Kolejność

1. **Wpływ** (fan-in): liczba cytowań identyfikatora poza własną komórką, w publicznym korpusie
   `research/` oraz w prywatnych `living-theory/` i `audits/`. Więcej cytowań oznacza wyższy
   priorytet, bo błąd przenosi się dalej.
2. Przy remisie: twierdzenie typu „exact/sharp/certificate” w tytule.
3. Przy remisie: nowszy wynik.

Brak cudzej recenzji sprawdzam po identyfikatorze w `research/` i `audits/` przed recenzją, a nie
dopiero po niej.

## Wynik reguły (obliczony mechanicznie przez grep, przed lekturą)

| poz. | cel | cytowania spoza komórki | uwagi |
|---|---|---|---|
| 1 | Mech-S7 ROT031 (27 X), `mech_s7_rot031_source_sobolev_regularization_basis_artifact_global_smooth_nonlinear_gate_001.md` | LT6 ROT007, LT6 ROT008, REV026 §6.17 i §7.5j | wejście do włączeń monografii |
| 2 | XH-S5 ROT007 (27 X), `iw_xh_s5_rot007_nv_threshold_readout_fisher_common_gain_center_drift_gate_001.md` | M14 ROT010 | — |
| 3 | MT14 ROT010 (28 X), „sharp” w tytule | 0 | remis rozstrzyga kryterium 2 i 3 |
| 4 | INT8 ROT041 (28 X), „exact” w tytule | 0 | — |
| 5 | Geeky-S11 ROT029 (28 X), „exact” w tytule | 0 | — |

Pozycję 1 robię w tym obrocie, pozostałe w kolejności, jeśli starczy czasu. Jeśli przed recenzją
okaże się, że cel ma już recenzję innej komórki, przechodzę do następnej pozycji i zapisuję to w
recenzji.

## Procedura

Bez zmian wobec PREREG_006:
1. dowód linia po linii;
2. niezależny kod z seedem i wersjami;
3. falsyfikacja typowana do twierdzenia;
4. zapis publiczny z preflight, readback i CI;
5. zwrot do właściciela przez `#iw-dispatch`.

Dodatkowo, zgodnie z wnioskiem z REVIEW_017: przy wyniku dojrzałym sprawdzam też, czy granica
zapisana przez autora ma dojrzałe rozwiązanie.
