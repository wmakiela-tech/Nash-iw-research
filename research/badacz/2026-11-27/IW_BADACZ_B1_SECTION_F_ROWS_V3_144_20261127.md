---
artifact_id: IW_BADACZ_B1_SECTION_F_ROWS_V3_144_20261127
supersedes: IW_BADACZ_B1_SECTION_F_ROWS_V2_142_20261126
referee: REC15 ROT015 (zakres: §F wymaga B1, B2 i C1; pytanie pierwotne a zawężone); naprawy środowiska i zakresu s: Mech-S11 ROT028; v3: REC15 ROT019, Mech-S11 ROT029/031, KN18 ROT004
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel B1
created_at: 2026-11-27
document_type: SECTION_F_B1_ROWS (wiersze B1 do artefaktu §F; artefakt całościowy obejmuje B1, B2 i C1 i nie należy do Badacza; protokół 30-dniowy IW_NASH_30_DAY_EXTERNAL_RESULT_DECISION_PROTOCOL_001_20261113, §F; termin 13 XII)
decision_basis: Moderator 25 XI 14:57 („tak przyjmuję”): STD_A jako główny brief B1, Q-B jako sekcja warunkowa
claim_ceiling: PROPOSAL / labels and CLOSED are Moderator decisions / NO_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# §F, wiersze B1 (projekt v2 na 13 XII)

**Pytanie pierwotne B1 (§B protokołu):** czy źródłowo legalny opis historii hadronów rozróżnia reżim liniowy, pośredni i nasycenia, albo daje węższe ograniczenie błędu redukcji niż najbliższy gospodarz ODE.
- Linia Badacza na to pytanie **nie odpowiedziała**.
- Za zgodą Moderatora zastąpiły je pytania węższe: Q-B (G1, 16 XI) oraz STD_A (25 XI).
- Proponowana etykieta dla pytania pierwotnego: **B1-HOLD_SOURCE**.
- Natywne historie sześciu hadronów istnieją, ale tylko w jednym zamrożonym punkcie j22 (Mech-S9 ROT013, 13 XI; BW ING-20261113-0055; odnalezienie i archiwum: KN18 ROT004/006, Mech-S11 ROT031). Pojedynczy punkt nie rozróżnia reżimów. Surowe n_h to nie to samo co użyty RHS, a zamrożona historia nie jest legalną trajektorią kontrfaktyczną. Etykieta HOLD_SOURCE pozostaje.

Tabela niżej dotyczy wyłącznie pytań zawężonych.

| pole | STD_A (wynik główny) | Q-B (sekcja warunkowa) |
|---|---|---|
| dokładne pytanie | O ile przesuwa się próg β(M) w publicznym kodzie Wu–Xu, gdy zegar parowania (geometryczna optyka, Eq. 2.10) zrównać z normalizacją widm greybody (BlackHawk f(M)), przy niezmienionym źródle hadronów? | O ile przesuwa się próg, gdy grupową stawkę hadronów rozdzielić na stany ładunkowe zamiast wstrzykiwać ją do każdego stanu? |
| źródło niezmienne | Wu–Xu d395183, `main-scan.jl` l. 80; BlackHawk v2.3 `fM.txt`; arXiv:2509.05618v3 | to samo; `hadrons_from_PBH.dat`; tablice BBN PYTHIA |
| data zamrożenia | PREREG_123 (40c6423, 23 XI) | G1: PROPOSAL_068 / PREREG_069 (16 XI) |
| pierwszeństwo | kierunek EKS1 (DIR-010); pomiar natywny Badacz (REVIEW_120–126) | E5 Badacz (31 X); grupowanie Mech-S9 |
| prereg | PREREG_123, PREREG_125, DRAFT_127 §3 (H2) | PREREG_069, T1 Mech-S9 |
| wykonywalność | natywna Julia; upstream Project bez przypiętej wersji (NaturalUnits rev main), więc użyto przypiętego, zarchiwizowanego Manifestu Mech-S11, identycznego dla H1 i H2 (Mech-S11 ROT028) | natywna Julia, T2R Mech-S10 |
| dane | research/badacz/2026-11-23, research/mech-s11/2026-11-25 | research/badacz/2026-11-16 |
| poprawność | Δ(j22) = −1.384 i Δ(j62) = −0.244 dex; pierwiastki std przy 9.45e8–1.08e9 g, gdzie base nie ma pierwiastka w siatce; wynik odporny na kontynuację źródła w trzech testowanych wartościach s ∈ {−1.5, −1.3, −1.0}; zaburzenia wyjścia o ε = 1e−4 zachowują znaki we wszystkich 86 punktach i zmieniają Δ o mniej niż 0.02314 / 0.01540 dex (Mech-S11 ROT028; czułość wyjścia, nie granica błędu solvera) | +0.272…+0.301 dex w 6 masach; po przeniesieniu na sieć +0.26…+0.30 |
| niepewność | szum pierwiastków 0.001–0.021 dex; progi bezwzględne objęte STOP A (źródło poniżej 1e9 g), STOP B (mapa Y_P), G_DEP | przesunięcie względne odporne; progi bezwzględne nie (SYNTH_087) |
| dojrzały gospodarz | Page 1976; MacGibbon 1991; Baldes et al. 2020, dod. A (czynnik ok. 2); Cheek et al. 2022; Boccia et al. 2025 (zegar greybody, bez hadronów) | Reno–Seckel 1988; Bianco et al. 2026 (wydajności per stan) |
| niezależne I1/I3 | H1: Mech-S11 ROT009 (natywnie, 56/56) + AUD4 ROT007 i REC15 ROT011 PASS. H2: Mech-S11 ROT012, 3/3 punktowo i 2/3 przedziały. Brief v2: REC15 ROT012 | T2R Mech-S10, 68/68 bitowo; semantyka (T3) OPEN |
| ważny null | H1: replika innej rodziny różna o > 0.03 dex przy j16, j22 lub j62 (nie wystąpił); H2: co najmniej 2 z 3 przewidywań punktowych poza przedziałem (nie wystąpił, 0/3); normalizacja q zgodna z geometryczną optyką (sprzeczna z Fig. 2 autorów) | T3: konwencja grupowa zamierzona razem z przekrojami grupowymi, a więc spójna |
| rzeczywista nowa informacja | W modelu autorów przesunięcie jest przewidywalne: przeskalowanie zegara M′ = 1.198·M oraz czynnik R^c w β, gdzie c ≈ 0.92 wynika z tablicy źródła (minimax ciągły: pierwszy M17 ROT002; replay REC15 ROT014). Wyjaśnia to dużą wartość Δ przy stromej ścianie. | W kodzie siedzi konwencja czynnika 2 warta ok. +0.3 dex; jej status zależy od semantyki |
| alternatywne wyjaśnienie | świadome przybliżenie autorów; wtedy niespójność zegara i widm pozostaje, ale wymaga ich potwierdzenia | konwencja odziedziczona po Kohri 2001 z przekrojami grupowymi |
| produkt | brief v5 (IW_BADACZ_B1_RESULT_BRIEF_STD_A_V5_143_20261127), poziom modelu | sekcja 6 briefu |
| decyzja i stop | **Proponowana etykieta: B1-SOURCE-VALIDATED-MATURE-APPLICATION**, z zakresem: przesunięcie i mechanizm w modelu kodu. ORIGINAL-SCIENCE nie wchodzi w grę, bo dojrzały gospodarz zna czynnik. Nowości nie wykazano, co nie jest wykazaniem jej braku; etykieta „mature application” nie dowodzi jednak braku nowości. STOP A pozostaje HOLD (test generatora niedopuszczalny, REVIEW_132). Do 13 XII żadnych dalszych przebiegów B1. | **B1-HOLD_SOURCE** dla interpretacji, **B1-REPRODUCIBILITY-ONLY** dla pomiaru. T3 nie da się zamknąć bez autorów (kontakt wstrzymany). |

**Propozycja tylko dla B1** (nie decyzja całościowa §F, która obejmuje też B2 i C1): pytania zawężone dają wynik użyteczny, ale nie nowy. Zachowujemy wkład odtwarzalnościowy i wstrzymujemy wydatki na twierdzenia teoretyczne w B1. Z wieloetapowej weryfikacji opisowej nie wynika żadna przyczynowa przewaga metody NASH; to pytanie należy do C1. Etykiety, zamknięcie i EXEC_SIGN należą do Moderatora.

**Otwarte do 13 XII (bez przebiegów):** odczyt BW przez KN18 oraz scalenie wierszy B1 z B2 i C1 w jeden artefakt przez Moderatora lub wyznaczoną komórkę.

NO_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
