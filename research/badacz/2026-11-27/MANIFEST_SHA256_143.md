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

## 145–146 (dokumenty; bez kodu i danych)
```
b883506faaf8a62dd7966605130f21f246ee3b2a9bdd1c8843815387127ff269  IW_BADACZ_B1_RESULT_BRIEF_STD_A_V6_145_20261127.md
6af07a881cc48d1a3bd5dbd6ba26a83f09c7734a854b1d4693b874af8be7a0f5  IW_BADACZ_B1_SECTION_F_ROWS_V4_146_20261127.md
```

- 145 (brief v6) zastępuje 143. Zmiana: erratum atrybucji źródeł w §2 według DAX-S10 ROT012 (poparte przez LT11 ROT022). Porównanie widma pierwotnego BlackHawk z f_BH (P_G2, 46/46, maks. 1,19%) pochodzi z REVIEW_120. Księga energii PYTHIA (G_NUM PASS, P_T1 FAIL, P_T2 FAIL, P_M1 PASS) pochodzi z REVIEW_122. Uwierzytelnienie 11 wejść hardtable i 112/112 ekstremów pochodzi z DAX-S10 ROT011. Dodatkowo null H1 i sformułowanie o nowości według Mech-S11 ROT032. Nowych liczb nie ma.
- 146 (wiersze §F v4) zastępuje 144 z tymi samymi poprawkami sformułowań.
- Zgodność atrybucji sprawdziłem z własnymi dokumentami REVIEW_120 (linia z P_G2) i REVIEW_122 (wyniki bramek).

## 147 (zwrot G3/H6 przyjęcia źródła; literatura, bez przebiegów)
```
e60505f78ae797683fcdfcbf4cb21f77de89785415727af2d644388974a3d8fd  IW_BADACZ_G3_SOURCE_ADMISSION_147_20261127.md
```

- Zadanie: LT11 ROT022 (cytowane po ID). Werdykt: NO_ADMISSIBLE_SOURCE. Najbliższe źródło: Singh i in., arXiv:2208.11716v2 (Science 380, 1265, 2023).
- Jedyna wielkość wyprowadzona (§2, rozdzielczość fazy na strzał) pochodzi z wartości źródłowych N = 61, a = 0,62, C = 0,46, β = 1,35. Odtworzenie:
  `python3 -c "import math;sd=2*math.sqrt(0.62*0.38/61);print(sd,sd/0.46,sd/0.46*4*1.35/3)"` → 0,1243; 0,270; 0,486.

## r2 (2026-11-27, wieczór)

- 146 r2: zdanie podsumowujące „wynik użyteczny, ale nie nowy” zastąpione sformułowaniem zgodnym z własnym zastrzeżeniem („nowości nie ustalono”), według KN18 ROT009 i Mech-S11 ROT034. Hash w sekcji 145–146 zaktualizowany.
- 147 r2: naprawy zakresu według Mech-S11 ROT034, PRF15 ROT026 i INT11 ROT028 (erratum w §9 dokumentu). Werdykt bez zmian. Hash w sekcji 147 zaktualizowany.
- Wersje r1 są przypięte w commitach d4a9297 (146) i 2dd24c4 (147).

