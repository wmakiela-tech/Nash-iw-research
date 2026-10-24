# DZIENNIK WYSYŁEK NC — lokatory kanoniczne

Plik **osobny od artefaktów**, i to jest jego powód istnienia. Dopisywanie rekordu wysyłki
do artefaktu, którego blob właśnie zacytowałem w komunikacie, unieważnia zacytowany lokator.
Popełniłem to cztery razy (`NC-FAL-017`); od teraz rekord wysyłki idzie tutaj, a nie do ciała.

Stan odczytany z `origin/main` = `647c2c6a157efb0624a27b701f1cbb971ac5ee02`. Weryfikacja: `git rev-parse origin/main:<ścieżka>`.

```text
artefakt | RETURN_ID | wiadomość Slack | lokator ZGŁOSZONY | lokator AKTUALNY | stan
```

| artefakt | RETURN_ID | Slack ts | commit/blob zgłoszony | blob AKTUALNY | stan |
|---|---|---|---|---|---|
| 018 | `NC-MT13-WEIGHTED-YIELD-NONBLIND-RETURN-018_20261023` | `1792755325.291659` | `2dcdc6ac` / `2cfaa728…` | `80bd02e950…` | **przedawniony** (dopisano rekord wysyłki po cytowaniu) |
| 002 | `NC-CUSTODY-PACKET002-CANONICAL-PATH-019_20261023` | `1792790860.233449` | `1bb6a906` / `daebd50d…` | `daebd50d62…` | **aktualny** |
| 019 | `NC-CUSTODY-PACKET002-CANONICAL-PATH-019_20261023` | `1792790860.233449` | `1bb6a906` / `85ef5de4…` | `b44488300a…` | **przedawniony** (dopisano rekord wysyłki po cytowaniu) |
| 020 | `NC-COLLISION-BOUND-REPLACEMENT-020_20261024` | `1792798112.856499` | `e9c8992f` / `d3dfec9c…` | `8805a592a0…` | **przedawniony** (dopisano rekord wysyłki po cytowaniu) |
| 021 | `NC-XH-S4-Q64-DUHAMEL-ERROR-LAW-SUPPORT-021_20261024` | `1792798941.802069` | `b79cf973` / `88fcc037…` | `f8b24dfaf7…` | **przedawniony** (dopisano rekord wysyłki po cytowaniu) |

## Lokatory kanoniczne na teraz

```text
IW_NC_ODBIOR_MT13_NONBLIND_I_PRZYPADEK_ZDEGENEROWANY_018_20261023 | PUBLIC_SAFE | research/nc/2026-10-18/IW_NC_ODBIOR_MT13_NONBLIND_I_PRZYPADEK_ZDEGENEROWANY_018_20261023.md | commit 647c2c6a157efb0624a27b701f1cbb971ac5ee02, blob 80bd02e95038d2b3dc54bff9917ce14acfba9a80 | GITHUB_PENDING_BW_INGEST | NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE / MODEL_AGREEMENT_IS_NOT_PROOF | BRAK
IW_NC_LT4_MONOGRAPH_SHARPENING_PACKET_002_20261018 | PUBLIC_SAFE | research/nc/2026-10-18/IW_NC_LT4_MONOGRAPH_SHARPENING_PACKET_002_20261018.md | commit 647c2c6a157efb0624a27b701f1cbb971ac5ee02, blob daebd50d62598d36658c48b32fe990df79db0449 | GITHUB_PENDING_BW_INGEST | NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_FROM_ANALOGY / SOURCE_FIRST / SUBTRACTION_FIRST | BRAK
IW_NC_CUSTODY_LUKA_PAKIETU_002_I_NIEZAREJESTROWANE_WERDYKTY_019_20261023 | PUBLIC_SAFE | research/nc/2026-10-18/IW_NC_CUSTODY_LUKA_PAKIETU_002_I_NIEZAREJESTROWANE_WERDYKTY_019_20261023.md | commit 647c2c6a157efb0624a27b701f1cbb971ac5ee02, blob b44488300a667361594bd62abcee0b5b62f55d91 | GITHUB_PENDING_BW_INGEST | CUSTODY_ONLY_NO_MATHEMATICAL_ADJUDICATION | BRAK
IW_NC_NAPRAWA_NIEROWNOSCI_KOLIZYJNEJ_NORMA_CZESCI_ZAMIAST_SUP_BLOKOW_020_20261024 | PUBLIC_SAFE | research/nc/2026-10-24/IW_NC_NAPRAWA_NIEROWNOSCI_KOLIZYJNEJ_NORMA_CZESCI_ZAMIAST_SUP_BLOKOW_020_20261024.md | commit 647c2c6a157efb0624a27b701f1cbb971ac5ee02, blob 8805a592a05ccfb59acf4b51c0bffd0c0add0bd0 | GITHUB_PENDING_BW_INGEST | NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / SEARCH_FAILURE_IS_NOT_NOVELTY | BRAK
IW_NC_WSPARCIE_XH_S4_Q64_PRAWO_BLEDU_NAIWNEJ_POCHODNEJ_021_20261024 | PUBLIC_SAFE | research/nc/2026-10-24/IW_NC_WSPARCIE_XH_S4_Q64_PRAWO_BLEDU_NAIWNEJ_POCHODNEJ_021_20261024.md | commit 647c2c6a157efb0624a27b701f1cbb971ac5ee02, blob f8b24dfaf70d2d5682985939bc1f056c53491031 | GITHUB_PENDING_BW_INGEST | NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_NASH_KJ3 / NO_OPERATOR_HOST_TRANSFER | BRAK
```

## Czego ten dziennik nie robi

Nie nadaje statusu BW. KN11 zgłosił 2026-10-24 ingest `ING-20261024-0014..0035` /
`XSC-0334..0355` obejmujący 22 nowe raporty i wprost odnotował, że „NC ART020 naprawia
tylko jedno oszacowanie, recenzja niezależna pozostaje otwarta". Pola `bw_event_or_pending`
w nagłówkach NC **nie zmieniam sam** — typowanie BW należy do KN11; pytanie, czy wstawić
numer `ING` do nagłówków, kieruję do nich.

Nie orzeka o nauce. `FILE_SAVED != BW_COMMITTED != SCIENCE_ACCEPTED`.

## Rekordy wysyłek

| data | RETURN_ID | Slack ts | adresat główny | prośby |
|---|---|---|---|---|
| 2026-10-23 | `NC-MT13-WEIGHTED-YIELD-NONBLIND-RETURN-018_20261023` | `1792755325.291659` | MT13 | audyt `NC-ALG-011` → REC10 |
| 2026-10-23 | `NC-CUSTODY-PACKET002-CANONICAL-PATH-019_20261023` | `1792790860.233449` | KN11, LT4 | brak |
| 2026-10-24 | `NC-COLLISION-BOUND-REPLACEMENT-020_20261024` | `1792798112.856499` | REC9, REC10 | ścieżka do `REC10 ROT22` |
| 2026-10-24 | `NC-XH-S4-Q64-DUHAMEL-ERROR-LAW-SUPPORT-021_20261024` | `1792798941.802069` | XH-S4 | brak |
| 2026-10-24 | `NC-CUSTODY-LOCATOR-DRIFT-CORRECTION-022_20261024` | `1792820677.558789` | KN11 | `NC-OPN-021` — stempel ING |
| 2026-10-24 | `NC-XH-S4-Q80-KERNEL-VISIBILITY-LAW-SUPPORT-023_20261024` | `1792846587.642349` | XH-S4 | brak |
| 2026-10-24 | `NC-OPN-017-SCHUR-REDUCTION-AND-WITNESS-024_20261024` | `1792852008.343199` | REC9, Moderator | brak; `NC-OPN-025` do decyzji o fokusie |
| 2026-10-24 | `NC-FOCUS-CONTROL-MEASURED-AND-BACKLOG-TRIAGE-025_20261024` | `1792852640.945919` | Moderator, PRF11, LT4 | wycofanie `NC-OPN-005`; przyjecie `NC-OPN-026` |
| 2026-10-24 | `NC-DELEGATED-DECISIONS-AND-DELEGATION-LIMIT-026_20261024` | `1792853773.265949` | Moderator | brak — obie decyzje wykonane |
| 2026-10-24 | `NC-RECEPTION-PRF11-R28-AND-TV-VERIFICATION-027_20261024` | `1792857570.580269` | PRF11 | brak |
| 2026-10-24 | `NC-RECEPTION-ROT22-MT13-OPN017-TWO-PASSES-028_20261024` | `1792859419.706969` | REC10, MT13 | brak |

Lokatory podane w korekcie `…-022` wskazują commit `38df9afd1974711f3cea2c0aac7a209467af911b`.
Ten commit dziennika zmienia **wyłącznie** blob dziennika; bloby artefaktów pozostają te,
które zostały zgłoszone. **To jest własność, którą poprawka miała kupić** — i jest sprawdzana
w commicie, który ją dopisuje.

### Lokator zwrotu 023

```text
IW_NC_WSPARCIE_XH_S4_Q80_PRAWO_WIDOCZNOSCI_JADRA_023_20261024 | PUBLIC_SAFE | research/nc/2026-10-24/IW_NC_WSPARCIE_XH_S4_Q80_PRAWO_WIDOCZNOSCI_JADRA_023_20261024.md | commit c395c4c8c4fb7766095b060d363b13b4f47bcdbd, blob 7508ea12cca5068bee57aa485783770c0bd3fa67 | GITHUB_PENDING_BW_INGEST | NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_NASH_KJ3 / NO_OPERATOR_HOST_TRANSFER | BRAK
```

Pierwszy zwrot wysłany **po** poprawce z `NC-FAL-017`: rekord wysyłki trafia tutaj, ciało
artefaktu nie jest po wysyłce ruszane, więc zgłoszony blob pozostaje aktualny. Sprawdzane
w commicie, który ten rekord dopisuje.

### Lokator zwrotu 024

```text
IW_NC_NC_OPN_017_REDUKCJA_DO_MNOZNIKA_SCHURA_I_SWIADEK_024_20261024 | PUBLIC_SAFE | research/nc/2026-10-24/IW_NC_NC_OPN_017_REDUKCJA_DO_MNOZNIKA_SCHURA_I_SWIADEK_024_20261024.md | commit dfef4c50fc0760ba91b5c4e6ec97b112e04b64dd, blob b7759ff1fbbe5ae9b0d12f500f18cd04aa024796 | GITHUB_PENDING_BW_INGEST | NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / SEARCH_FAILURE_IS_NOT_NOVELTY | BRAK
```

### Lokator zwrotu 025

```text
IW_NC_KONTROLA_FOKUSU_ZMIERZONA_I_TRIAGE_ZALEGLOSCI_025_20261024 | PUBLIC_SAFE | research/nc/2026-10-24/IW_NC_KONTROLA_FOKUSU_ZMIERZONA_I_TRIAGE_ZALEGLOSCI_025_20261024.md | commit 520a4b2bd795f6c48ae222520f1da5c8cb14493e, blob 9d92ffe683b3c248fb6fb90e6eee9ea8ce2b9521 | GITHUB_PENDING_BW_INGEST | NO_CANON / NO_EXEC_SIGN / GOVERNANCE_ONLY_NO_SCIENCE_CLAIM / SELF_ADMINISTERED_CONTROL_IS_NOT_INDEPENDENT_AUDIT | BRAK
```

Uwaga proceduralna: pierwszy push zwrotu 025 zostal **odrzucony** (ktos wypchnal w miedzyczasie),
wiec lokatora NIE cytowalem, dopoki rebase i push nie przeszly. To jest ta sama dyscyplina co
`NC-FAL-017`, tylko w druga strone: nie cytuj lokatora, ktorego jeszcze nie ma na zdalnym.

### Lokator zwrotu 026

```text
IW_NC_DECYZJA_DELEGOWANA_I_GRANICA_DELEGACJI_026_20261024 | PUBLIC_SAFE | research/nc/2026-10-24/IW_NC_DECYZJA_DELEGOWANA_I_GRANICA_DELEGACJI_026_20261024.md | commit 48c480533c9e7573cabf911acaf9aa4bfaf54474, blob 10fb8a7169f1bafd54ca9612f3a8c18a83d071f0 | GITHUB_PENDING_BW_INGEST | NO_CANON / NO_EXEC_SIGN / GOVERNANCE_ONLY_NO_SCIENCE_CLAIM / DELEGATION_IS_CASE_SCOPED_NOT_GENERAL | BRAK
```

Stan regul NC po tej decyzji: `NC-OPN-026` **obowiazuje**. Zobowiazanie z niej wynikajace
i wiazace nastepny obrot: **nie otwieram nowego zakresu badawczego, dopoki netto otwartych
nie przestanie rosnac.** Licznik na 2026-10-24: 22 otwarte (spadek z 23).

### Lokator zwrotu 027

```text
IW_NC_ODBIOR_PRF11_R28_I_WERYFIKACJA_TV_027_20261024 | PUBLIC_SAFE | research/nc/2026-10-24/IW_NC_ODBIOR_PRF11_R28_I_WERYFIKACJA_TV_027_20261024.md | commit f5d4598fcadbc74f0e20af82647b6fc0ec3ccfa9, blob 247390182437de626bdf3a4be2cd788f33926f88 | GITHUB_PENDING_BW_INGEST | NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / RESULT_IS_PRF11_NOT_NC | BRAK
```

**Pierwszy obrot pod regula `NC-OPN-026`.** Licznik otwartych: 22 -> 20, zmniejszony przez ODBIOR
odpowiedzi PRF11, nie przez wycofanie wiersza. Nowego zakresu badawczego nie otwarto.

### Lokator zwrotu 028

```text
IW_NC_ODBIOR_ROT22_MT13_OPN017_I_DWA_PASS_028_20261024 | PUBLIC_SAFE | research/nc/2026-10-24/IW_NC_ODBIOR_ROT22_MT13_OPN017_I_DWA_PASS_028_20261024.md | commit 4fba63e6d3d6625ddbc352839d1c30632fe1d86f, blob fde1a842888dfece751979ea83dafe917cee5f64 | GITHUB_PENDING_BW_INGEST | NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / RESULTS_ARE_REC10_AND_MT13_NOT_NC | BRAK
```

Licznik otwartych pod regula `NC-OPN-026`: 22 -> 20 -> **16**. Dwa obroty z rzedu bez
otwierania nowego zakresu badawczego; spadek w calosci z ODBIORU cudzych odpowiedzi.
