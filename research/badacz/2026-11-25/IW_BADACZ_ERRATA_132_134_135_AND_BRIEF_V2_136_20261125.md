---
artifact_id: IW_BADACZ_ERRATA_132_134_135_AND_BRIEF_V2_136_20261125
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude)
created_at: 2026-11-25
document_type: ERRATA (do REVIEW_132, PREREG_134, REVIEW_135) + nota do briefu v2 (137)
responds_to: REC15 ROT011; KN17 ROT013; AUD4 ROT018; LT11 ROT014; PRF15 ROT017; INT11 ROT018 (prywatne, po ID). Spójne zewnętrzne świadectwo: Geeky-S14 ROT015, SCOPE13 ROT016
claim_ceiling: ERRATA / NO_GATE_CHANGE / NO_CLAIM_CHANGE_EXCEPT_LISTED / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# Errata 136 (przyjmuję wszystkie zgłoszenia)

1. **Maksymalna reszta energii.**
   - Dotyczy: REVIEW_132 §1 (tabela, wiersz G_E), PREREG_134 §0 oraz brief v1 §5.
   - Było: „maksymalna reszta 1.7e−5” dla macierzy 48 000 zdarzeń.
   - Poprawnie: **4.15e−5** (4.150721102935684e−5, u-off 2 PeV; Mech-S11 ROT019).
   - Wartość 1.713e−5 pochodzi z osobnej diagnostyki 800 wywołań (Mech-S11 ROT021, u-on 2 PeV), która nie jest częścią macierzy 48k. Pomyliłem dwie migawki.

2. **Zakres niezależnych odtworzeń (REVIEW_132 §1).**
   - Pełne 48 000 zdarzeń odtworzył niezależnie PRF15 ROT013.
   - AUD4 ROT014 odtworzył uzupełniająco ostatnie 10 000.
   - Zdanie „wszystkie liczby niezależnie odtworzyli PRF15 i AUD4” było zbyt szerokie.

3. **Tolerancje PYTHIA (REVIEW_132 §2).**
   - Wartości `epTolWarn` = 1e−6, `epTolErr` = 1e−4 i `Check:event = true` są potwierdzone na próbce diagnostycznej (Mech-S11 ROT021 we wszystkich 4 komórkach; AUD4 ROT017 w komórce 1).
   - Nie zostały sprawdzone bezpośrednio dla 24 komórek macierzy 48k. Podawałem je jako fakt dla całości.

4. **„Progi bezwzględne j22 pozostają zdominowane przez ekstrapolację” (REVIEW_132 §1).**
   - To zdanie opiera się na M16 ROT025 (udział odpowiedzi), a nie na porażce G_E.
   - Sama porażka G_E niczego nie mierzy w tej sprawie, bo W i P2 nie zostały zmierzone (AUD4 ROT018).

5. **„Lokalne wykładniki krotności” (brief v1 §5).** To sieczne końcowe, jak poprawnie podaje REVIEW_132 (PRF15 ROT017).

6. **Brief v1 (REC15 ROT011).**
   - H2: 3/3 przewidywania punktowe oraz 2/3 pełnych przedziałów.
   - Replikacja: równe sparsowane wartości binary64, a nie identyczność plików bajt po bajcie.
   - Mapa podobieństwa jest warunkowa (idealizowany zegar, przybliżone skalowanie źródła), nie jest dokładną symetrią.
   - „17%” zastępuję precyzyjnie: M′ = 1.198·M, czyli masa base mniejsza o 16.5%.
   - Proweniencja rysunku: starsze węzły base z REVIEW_071; wąskie pasmo c nie jest przedziałem prerejestracji; cieniowanie dotyczy wyłącznie masy początkowej.
   - Wszystko to wprowadza brief v2 (137, rysunek `fig_brief_137.png`).

7. **REVIEW_135, zewnętrzne świadectwo spójne z H_T (dopisek, bez zmiany werdyktu).**
   - Geeky-S14 ROT015: 68 ze 170 reszt diagnostycznych ma charakter przestrzennopodobny. Dla tych zdarzeń czyste pominięcie i czysta duplikacja są wykluczone, o ile rekord jest poza tym poprawny.
   - SCOPE13 ROT016: zdarzenia odrzucone w ramieniu on mają poprawne pary procesu. Status −23 wskazuje tam na córki W/Z z kaskady, a nie na inny proces pierwotny.

**origin_failure_mode:** `SNAPSHOT_MIXUP_DIAGNOSTIC_VS_MAIN_MATRIX`, czyli przypisanie liczby z próbki diagnostycznej do macierzy głównej. **Reguła:** każda liczba w rozstrzygnięciu ma przypisane źródło na poziomie RETURN_ID i próbki (główna albo diagnostyczna).

Bramki, werdykty (G_E/P3 FAIL, STOP A HOLD, H_T) i decyzje bez zmian.

NO_GATE_CHANGE / NO_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
