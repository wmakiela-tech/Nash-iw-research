---
artifact_id: IW_BADACZ_B1_STOPA_GENERATOR_EXTENSION_REVIEW_132_20261125
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel PREREG_129
created_at: 2026-11-25
document_type: REVIEW (rozstrzygnięcie PREREG_129 + A1 według zamrożonych reguł)
inputs: Mech-S11 ROT019, ROT021 (public, research/mech-s11/2026-11-25); PRF15 ROT011–014; AUD4 ROT013, ROT014; REC15 ROT007, ROT008; SCOPE13 ROT012, ROT013; INT11 ROT014; LT11 ROT010 (prywatne raporty cytuję po ID)
claim_ceiling: NEGATIVE_GATE / STOP_A_HOLD / NO_GATE_CHANGE / NO_RETRY / NO_PBH_BOUND / NO_AUTHOR_ERROR / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_132: wynik PREREG_129. Bramka energii FAIL, więc test nie jest dopuszczalny, a STOP A zostaje HOLD

**Rola:** Badacz. Rozstrzygam według reguł zamrożonych w PREREG_129 (15a4761) i A1 (a11d503). Nie zmieniam bramek ani tolerancji i niczego nie powtarzam.

## 1. Wynik według bramek
Mech-S11 wygenerował 48 000 zaakceptowanych zdarzeń w 24 komórkach. Użył PYTHIA 8.318.3 przez wiązanie Python, a nie PYTHIA8.jl ze skryptów autorów. To odstępstwo od §1 PREREG_129 Mech-S11 zamroził i opisał przed wygenerowaniem pierwszego zdarzenia, po nieudanej instalacji. Wszystkie liczby niezależnie odtworzyli z surowych archiwów PRF15 ROT013 i AUD4 ROT014.

| bramka / predykcja | wynik |
|---|---|
| G_Q (ładunek w każdym zdarzeniu) | PASS, 48 000/48 000 |
| G_QS (symetria ±) | PASS, 96/96 |
| **G_E** (\|ΣE − 2E′\|/2E′ ≤ 1e−6) | **FAIL** w 11/24 komórkach; 2726 zdarzeń, w tym 1374 z niedoborem i 1352 z nadmiarem; maksymalna reszta 1.7e−5 |
| G_OVL, G_COV, Δ_src, kryterium łączne A1 | nie mierzone: G_E blokuje splot |
| P1 (α_π w [0.22, 0.34]) | wynik tylko opisowy, nie PASS: u-off 0.285 ± 0.005, g-off 0.288 ± 0.003 (sieczne 1e5–2e6 GeV); bramka energii w węźle końcowym nie przeszła |
| P2 (Δ_src) | nie zmierzone |
| P3 (G_E, G_Q i G_QS przechodzą) | **FAIL** |

**Decyzja (PREREG_129 §4, A1):** test nie jest dopuszczalny. STOP A pozostaje w HOLD.
- Progi bezwzględne j22 pozostają zdominowane przez ekstrapolację.
- Nie twierdzę, że STD_A został sfalsyfikowany: przesunięcie Δ było odporne na kształt kontynuacji (REVIEW_126).

## 2. Co wiadomo o przyczynie (diagnostyka po teście; status nie zmienia się)
- **Gdzie powstaje rozjazd.** Sumy energii na poziomie procesu twardego są dokładnie nominalne. Rozjazd pojawia się dopiero w pełnym rekordzie zdarzenia, czyli po hadronizacji i rozpadach. Zaokrąglenie przy sumowaniu jest wykluczone (Mech-S11 ROT021, 800 zdarzeń, 3.26 mln cząstek).
- **Ostrzeżenia samego PYTHIA.** Natywne wyjście generatora zawiera komunikaty „energy-momentum not quite conserved” w 15/24 komórkach (wszystkich 11 z FAIL i 4 z PASS). W wielu komórkach są też błędy i ponowienia na etapie hadronizacji, w tym przy 1–2 PeV (SCOPE13 ROT013, AUD4 ROT014). Komunikaty nie są powiązane z numerami zdarzeń.
- **Tolerancje generatora.** Generator działa z `epTolWarn` = 1e−6 i `epTolErr` = 1e−4, więc moja bramka leżała na progu ostrzeżenia generatora. Dyskusja dopuszczalności i dokładności dla tej wersji pozostaje jednak otwarta (AUD4 ROT013).
- **Ramię weakShower-on.** Wszystkie 4196 odrzuconych zdarzeń to u-on, a 144 zdarzenia mają 4 lub 6 rekordów twardych. Filtr autorów (status −23 tylko z u/ū) wchodzi w interakcję z emisją W/Z, co daje selekcję w ramieniu on (REC15 ROT007, SCOPE13 ROT012). Systematyki weakShower nie da się więc zidentyfikować czysto.

**Wniosek fizyczny [▷], ostrożny.** Przy E′ ≥ 1 PeV ten generator w tej konfiguracji sam sygnalizuje problemy z kinematyką rekordu. Przedłużenie tablic autorów powyżej 1e5 GeV nie jest więc „tanim i czystym” źródłem fizycznym, za jakie uznałem je w TRIAGE_128 („TAK, z istniejących zasobów”). Korekta: zasoby istnieją, ale ich zachowanie przy PeV wymaga osobnej walidacji generatora, która wykracza poza B1.

## 3. Konsekwencje dla B1
- Brief B1 nie twierdzi nic o progach bezwzględnych, więc negatyw nie blokuje produktu. Do briefu v1 STOP A wchodzi jako otwarta bramka z tym testem jako dowodem.
- **Pruning:** do 13 XII nie proponuję w B1 kolejnych przebiegów generatora. To zgodne z AUD4 ROT014 i LT11 ROT010.
- Ewentualną diagnostykę generatora przy PeV (powiązanie numerów zdarzeń z kontrolerem, analiza genealogii na istniejących rekordach według Mech-S11 ROT021) zostawiam jako zadanie poza B1, do decyzji Moderatora.

## 4. Uczenie systemu
1. **`GATE_THRESHOLD_NOT_ANCHORED_TO_TOOL_TOLERANCE_AND_DECISION_RELEVANCE`.** Ustawiłem G_E na 1e−6, czyli na progu ostrzeżenia generatora. Nie powiązałem go ani z udokumentowanym progiem błędu, ani z wielkością decyzyjną (0.03 dex w liczebnościach).
   - **Reguła:** bramka numeryczna generatora zawiera (a) udokumentowane tolerancje narzędzia, sprawdzone dla użytej wersji, oraz (b) uzasadnienie wpływu na wielkość decyzyjną.
   - Nie twierdzę, że luźniejsza bramka by przeszła, bo generator sam zgłasza błędy.
2. **`NEW_ARM_NOT_CHECKED_AGAINST_INHERITED_SELECTION_FILTER`.** Ramię weakShower-on nie zostało sprawdzone z filtrem −23 autorów, choć ten filtr czytałem.
   - **Reguła:** każde nowe ramię konfiguracji przechodzi przed zamrożeniem techniczny pilot (odsetek odrzuceń, liczność rekordów twardych), ślepy wobec wielkości fizycznych.
3. **Korekta TRIAGE_128 §1.** „Blokerem jest koszt i autoryzacja, nie brak źródła” było zbyt optymistyczne. Blokerem okazała się także walidacja generatora przy PeV.

NO_GATE_CHANGE / NO_RETRY / NO_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
