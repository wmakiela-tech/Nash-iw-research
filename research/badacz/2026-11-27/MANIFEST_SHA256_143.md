---
artifact_id: IW_BADACZ_MANIFEST_SHA256_143_20261127
exposure: PUBLIC
document_type: MANIFEST
claim_ceiling: CUSTODY_ONLY
sync_state: GITHUB_PENDING_BW_INGEST
---

# MANIFEST SHA-256 (Badacz, 2026-11-27)

## 143–144 (dokumenty; bez kodu i danych)
```
e236c77c2233911d723c9f984e378071aceba1271e84ab5fdff6a440a6204fd7  IW_BADACZ_B1_RESULT_BRIEF_STD_A_V5_143_20261127.md
765f7805508b56de94e7739c1bd794dc159570c446143fad2965afa971e6ae9a  IW_BADACZ_B1_SECTION_F_ROWS_V3_144_20261127.md
```

## Zakres i odtworzenie

- 143 to brief B1 v5. Zastępuje v4 (2026-11-26/IW_BADACZ_B1_RESULT_BRIEF_STD_A_V4_141_20261126.md). Zmienia wyłącznie sformułowania i lokatory według REC15 ROT019, Mech-S11 ROT029/031 i KN18 ROT004/006/007. Nie zawiera nowych liczb z obliczeń.
- 144 to wiersze B1 artefaktu §F, v3. Zastępuje v2 r2 (2026-11-26/IW_BADACZ_B1_SECTION_F_ROWS_V2_142_20261126.md).
- Liczby w obu dokumentach pochodzą z artefaktów wymienionych w MANIFEST_SHA256_116 (2026-11-23), MANIFEST_SHA256_128 (2026-11-25) i MANIFEST_SHA256_138 (2026-11-26) oraz z raportów Mech-S11 w research/mech-s11/.
- Surowe dane natywne są w kapsułach Mech-S11 ROT029 (STD_A, SHA256 02c3f86b…) oraz w prywatnym archiwum KN18 ROT006/007 (historia j22 i 10 ZIP STOP A). Artefakty Actions wygasają 2027-02-23.
- Weryfikacja: `sha256sum` obu plików i porównanie z blokiem powyżej.

## Nota proceduralna

Pierwszy push tego katalogu (commit 7c80736) nastąpił mimo FAIL kontroli `SOURCE_BODY_TOO_SHORT` dla tego manifestu. Wywołanie kontroli przez `| tail -1` maskowało kod wyjścia. Ta wersja uzupełnia treść manifestu.

origin_failure_mode: `CHECK_EXIT_CODE_MASKED_BY_PIPE`. Reguła: kontrole przed push uruchamiam z `set -o pipefail` albo bez potoku, a push następuje tylko przy kodzie 0.
