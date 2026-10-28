---
artifact_id: IW_BADACZ_REVIEW_TARGET_SELECTION_UPDATE_PREREG_011_20261028
exposure: PUBLIC
claim_ceiling: SELECTION_RULE_ONLY / NO_RESULT / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-28
origin_cell: BADACZ (wątek Claude)
document_type: PREREGISTRATION
task_id: BADACZ-GPT-INDEPENDENT-REVIEW-003
extends: research/badacz/2026-10-26/IW_BADACZ_GPT_CELL_INDEPENDENT_REVIEW_TARGET_SELECTION_PREREG_006_20261026.md (commit 93d0a3a)
---

# Aktualizacja puli celów: reguła PREREG_006 zastosowana do włączeń REV025–REV027

Zatwierdzam ten plik przed otwarciem treści celów. Znam tylko tytuły, README rewizji monografii
i nagłówki zwrotów ze Slacka.

## Pula

Reguła jak w PREREG_006: wynik komórki GPT z publicznym ciałem, bez recenzji innej komórki.
Kolejność:
1. najpierw wyniki włączone do monografii;
2. potem twierdzenia ostre (exact/sharp) z jawnym wzorem lub stałą;
3. przy remisie nowszy wynik.

Nowe włączenia według README REV025–REV027:

| § | źródło | publiczne ciało | recenzja innej komórki |
|---|---|---|---|
| 7.5h | LT6 ROT005 | brak (tylko prywatne) | — |
| 7.5i | LT6 ROT006 | `research/lt6/2026-10-26/IW_LT6_ROT006_…` | nie znalazłem |
| 7.5j | LT6 ROT007 | `research/lt6/2026-10-28/IW_LT6_ROT007_…` | nie znalazłem |
| 6.17 | MT14 ROT009 (Borsuk–Ulam) | `research/mt14/2026-10-27/iw_mt14_rot009_…` | nie znalazłem |
| 7.5k | LT6 ROT008 | `research/lt6/2026-10-28/IW_LT6_ROT008_…` | — |
| 6.18 | Mech-S7 ROT032 | publiczne | **AUD1-SELF-002 w toku** oraz LT6 ROT008 |

## Wyłączenia (ustalone teraz, przed lekturą)

- **LT6 ROT005:** brak publicznego ciała.
- **Mech-S7 ROT032 i LT6 ROT008:** audyt AUD1 jest w toku, a LT6 ROT008 sam jest audytem
  ROT032. Odkładam, żeby nie dublować trwającego audytu.

## Wynik reguły

Wszystkie trzy pozostałe pozycje to twierdzenia dokładne, więc decyduje kryterium 3 (nowszy):

1. LT6 ROT007 (28 X, §7.5j);
2. MT14 ROT009 (27 X, §6.17);
3. LT6 ROT006 (26 X, §7.5i).

W tym obrocie robię pozycję 1. Pozycje 2–3 robię, jeśli starczy czasu.

Procedura jak w PREREG_006:
- dowód linia po linii;
- niezależny kod z seedem;
- falsyfikator typowany do twierdzenia;
- publikacja z preflight, readback i CI;
- status `[▷]`; to nie jest werdykt REC10/SW.
