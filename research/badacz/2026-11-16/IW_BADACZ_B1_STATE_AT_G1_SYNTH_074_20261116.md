---
artifact_id: IW_BADACZ_B1_STATE_AT_G1_SYNTH_074_20261116
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), współwłaściciel natywny B1
created_at: 2026-11-16
document_type: SYNTHESIS (stan B1 na bramkę G1, 20 XI; dla komórek-następców)
claim_ceiling: SYNTHESIS / NO_NEW_RESULT / NO_PAPER_ERROR_CLAIM / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# SYNTH_074: stan B1 (protokół 30-dniowy) na 16 XI 2026, 23:00

**Rola:** Badacz. Jedna strona dla komórek wracających z sukcesji. Wszystkie wyniki mają status [▷]. Wartości liczbowe pochodzą z przypiętych artefaktów; tu niczego nie przeliczam.

## 1. Decyzje Moderatora (dosłownie, czas wiadomości)

| czas | decyzja | dotyczy |
|---|---|---|
| 16 XI 00:10 | „Autoryzuję” | PREREG_066 (kalibracja natywna) |
| 16 XI 16:47 | „Myślę że oba pytania da się zrobić równolegle. Autoryzuję t1 i t2” | zakres B1: Q-A i Q-B równolegle; T1 (Mech-S9), T2 (Badacz) |
| 16 XI 16:56 | „…możecie stworzyć online most wymiany informacji” | most Badacz ↔ Mech-S9 (issue #16 + wątek #iw-dispatch) |
| 16 XI 17:39 | „Autoryzuję” | przebieg Q-A (PREREG_070) |
| 16 XI 21:12 | „tak liczy się” | drugi przebieg T1 jako techniczna powtórka |
| 16 XI 21:39 | „zgodę daję” | replika T2 z rodziny GPT (T2R, Mech-S9) |

**G1 (zamrożenie pytania):** pytania Q-A i Q-B oraz ich testy są zamrożone w PROPOSAL_068 (`07211d6`), PREREG_069 (`f1e16c0`), PREREG_070 (`fd68539`) i preregu T1 Mech-S9 (`c896351` + errata `9feb28e`). Moim zdaniem warunek G1 jest spełniony; formalne zamknięcie G1 należy do Moderatora.

## 2. Wyniki

| pytanie / test | artefakt | wynik | audyt zewnętrzny |
|---|---|---|---|
| kalibracja natywna (j22, β_max) | REVIEW_067 (`c9cd6ca`) | próg szumu solvera ≈ 1e−5 w X_n(T0); archiwum autorów odtworzone tylko statystycznie (A-STAT); ślad Mech-S9 bitowo | Mech-S9 ROT026: PASS z zastrzeżeniami |
| **Q-B / T1:** semantyka tabeli 100×5 | Mech-S9 ROT029 (`a74006b`) | **T1-GROUPED**: 25/25, maks. błąd wzgl. 7.7e−11; „per stan” odrzucone | wynik komórki GPT; recenzja REC/AUD otwarta |
| **Q-B / T2:** natywny kontur E5 vs oryginał | REVIEW_071 (`2390d0d`, r2 `2fd6ee4`) | W-PASS, ORD-PASS, TOL-STABLE; **D = +0.272…+0.301 dex** (czynnik 1.87–2.00 w β) dla 1.1–7.7e9 g | replika T2R (Mech-S9) w toku |
| **Q-A:** mapa reżimów | REVIEW_072 (`f42da5c`) | P-A1 PASS (w domenie skanu brak nasycenia), P-A2 3/3, P-A3 2/3 + 1 UNRESOLVED; poza domeną nasycenie od log₁₀β = −16.7 (j22, j24) | Mech-S9 ROT030: I1 PASS (bajtowo), z zastrzeżeniami |
| **Q-B / T3:** odjęcie stanu wiedzy | prośba do LT8 (21:35) + INPUT_073 (`01a313d`) | **otwarte**. Fakty: kod jest zgodny z tekstem; konwencja bez czynnika ½ we wszystkich wersjach; v3 (V 2026) dodaje podziękowanie za poprawkę stawek konwersji n↔p po kodzie `d395183` | wykonawca spoza autora hipotezy |

**Pomost Q-A ↔ Q-B:** kontur autorów leży w reżimie liniowym dla m ≥ 1.33e9 g, a niedobór D względem log₁₀2 jest taki sam w reżimie liniowym i pośrednim. Niedobór nie wynika więc z nieliniowości. Którą część źródła wskazuje (K⁰_L czy efekty niehadronowe), pozostaje otwarte; Mech-S9 ROT030 zastrzega, że wynik nie wskazuje akurat K⁰_L.

## 3. Co blokuje etykietę wyniku 30-dniowego

| warunek | stan | właściciel | termin |
|---|---|---|---|
| T2R: replika z rodziny GPT (R-SHIFT ≤ 0.010 dex) | zgoda jest; prereg i przebieg czekają | Mech-S9 | przed G2 (27 XI) |
| T3: znane, zamierzone czy nieznalezione | prośba wysłana, bez odpowiedzi | LT8 (zapas: XH-S6) | 27 XI |
| recenzja REC12 lub AUD2 dla T1, T2 i Q-A | nie zlecona osobno | REC12 / AUD2 | — |
| E4 (fizyczna hadronizacja poniżej 1e9 g) | HOLD | — | poza zakresem B1-Q-B |

**Możliwe etykiety dla Q-B:**
- **SOURCE-VALIDATED** (kandydat na korektę opublikowanego ograniczenia o czynnik ok. 2) przy T2R PASS, T3-NOT-FOUND i pozytywnej recenzji;
- **MATURE-APPLICATION** przy T3-KNOWN;
- **NEGATIVE** dla hipotezy podwójnego liczenia przy T3-INTENDED z uzasadnieniem, np. przekrojami uśrednionymi po grupie.

**Q-A** ma sufit REPRODUCIBILITY / MATURE-APPLICATION.

W żadnym wariancie nie ma twierdzenia o błędzie w artykule przed T3 i recenzją. Ewentualny kontakt z autorami to decyzja Moderatora.

## 4. Zapisane tryby awarii (do dziedziczenia)

- `GATE_THRESHOLD_AT_NOISE_LEVEL` (drugi raz, REVIEW_067): bramki zbieżności porównujemy ze zmierzonym szumem.
- `TOLERANCE_REPRESENTATION_PERTURBATION`: jawnie podana „wartość domyślna” nie jest wartością domyślną.
- `CONFOUND_SCOPE_UNDERSTATED_IN_SELF_REPORT`: przy samozgłoszeniu najpierw sprawdzić całą historię.
- `PARALLEL_SESSIONS_SAME_CELL_DUPLICATE_AUTHORIZED_RUN` (T1): jedna sesja uruchamia jeden przebieg; przed startem odczytać deltę mostu.
- `PARALLEL_BRIDGE_SURFACES_OPENED_WITHOUT_CHECK`: jeden most, bo zamknąłem swój wątek na rzecz issue #16.
- `CUSTODY_CLAIM_WITHOUT_RAW_BYTE_RECHECK` (zarzut manifestu, wycofany przez Mech-S9).

## Uzupełnienie r2 (17 XI 2026, ok. 02:00): zwroty komórek-następców

**Zamknięte od r1:**
- **T3:** LT9 ROT001 (`0c1e2d1`). Wynik: T3_PASS_WITH_GUARDS, T3_NOT_FOUND_BOUNDED, AUTHOR_INTENT_UNRESOLVED.
  - W sprawdzonym zakresie (JCAP, arXiv v2 i v3, repozytorium autorów: issues = 0, head `d395183`) nie ma jawnej normalizacji grupa → stan ani korekty.
  - Dojrzałe schematy n↔p dla poszczególnych gatunków są znane (Kohri–Yokoyama, Kawasaki–Kohri–Moroi).
  - Uzupełnienia: XH-S7 ROT001, PRF14 ROT001. Według PRF14 poprawka w v3 dotyczy słabych stawek n↔p (B.6), nie grupowania, więc punkt 3 INPUT_073 jest rozstrzygnięty.
- **Recenzja:** AUD3 ROT001 (issue #16, komentarz `6932357720`) daje PASS_WITH_GUARDS_SOURCE_INPUT dla T1, T2 i T3. To niezależne przeliczenie 25 stawek T1 i 232 wierszy T2; NO_PAPER_ERROR_CLAIM, NO_I3.
- **Arytmetyka T2:** Mech-S9 ROT031 (`3cd83c6`) daje I1 PASS, zgodność korzeni do 1e−14 dex, z zastrzeżeniem, że TOL-STABLE dotyczy różnicy D, a nie korzeni bezwzględnych.
- **Formalizacje warunkowe:**
  - INT10 ROT002: przeszkoda w podniesieniu 5 grup do 6 stanów przy dosłownej semantyce stanów;
  - LT9 ROT002: suma grupy pionów nie wystarcza do opisu obserwabli;
  - SCOPE12 ROT003/004 i REC13 ROT003: lokalne odwrócenia i granice obserwowalności.

  Żadna z nich nie orzeka o błędzie w artykule.

**Otwarte:**
1. **T2R (natywna replika GPT):** po zgodzie z 16 XI 21:39 nie wystartowała; jedyne przebiegi Actions to audyty źródłowe ROT031/032. Badacz zgodził się przenieść ten sam zakres 68 wywołań na jedną sesję Mech-S10. **Czeka na potwierdzenie Moderatora** (zgoda wskazywała Mech-S9).
2. **Zamiar autorów** (czy n_j w 4.7–4.8 to gęstość stanu, czy grupy, i czy ⟨σv⟩ jest uśrednione po grupie): nie da się go rozstrzygnąć obliczeniem. Możliwe drogi to dalsza lektura definicji przekrojów w źródłach cytowanych przez autorów albo pytanie do autorów. To drugie wymaga decyzji Moderatora.
3. E4 (fizyczna hadronizacja poniżej 1e9 g): HOLD, poza Q-B.

**Doprecyzowania do r1:**
- Q-A P-A1 („brak nasycenia w domenie”) dotyczy **6 natywnie badanych mas**, nie wszystkich 100 (zastrzeżenie KN15).
- TOL-STABLE w T2 to stabilność różnicy D, a nie certyfikat numeryczny korzeni (Mech-S9 ROT031).

**Ścieżka etykiety Q-B:** T1 PASS (przyjęte), T2 PASS (dwa niezależne I1 arytmetyki), T3 NOT_FOUND_BOUNDED i AUD3 PASS_WITH_GUARDS dają materialne wsparcie hipotezy jako **wyniku źródłowego warunkowego od semantyki autorów**. Brakuje natywnej repliki T2R i rozstrzygnięcia zamiaru autorów. Etykietę nadaje Moderator przy G2 (27 XI).
