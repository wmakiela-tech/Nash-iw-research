---
artifact_id: IW_BADACZ_B1_J22_INTERIOR_INTERACTION_SIX_PROBE_REVIEW_108_20261122
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel 083/084
created_at: 2026-11-22
document_type: REVIEW (wynik zamrożonej PREREG_107)
follows: PREREG_107 (Nash-iw-research@60f3e0d)
claim_ceiling: NUMERYCZNY w modelach [▷] / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_108: sześć sond SCOPE12 i AUD3 daje BRACKET_FAIL (1/3 ważne). Przy 0.002 dex solwer zmienia Y o 5–10e−5, czyli 4–7 razy więcej niż nachylenie; Pr1 PASS

## 1. Przebieg

- **Przebiegi:** 7 przebiegów Julii (18:36:11–18:38:49) i 8 PRyMordial, ALL_DONE 18:39:36.
- **Bramki 4/4 PASS:**
  - G_DRIVER: o22_1730 bitowo równe 083 w kodzie i w sieci; net_base bitowo równe;
  - G_COMPLETE, G_RUN, G_V2.
- Analizę powtórzyłem i wynik jest bitowo identyczny (SHA 6184014d…).

## 2. Wynik według preregistracji: `BRACKET_FAIL`, Pr1 PASS

| przedział | sondy (log β) | Y − Y* (dolna, górna) | dY zmierzone | dY z nachylenia |
|---|---|---|---|---|
| CODE_orig | −17.340625 / −17.338625 | −1.13e−4 / −1.44e−5 | +9.8e−5 | ~1.4e−5 |
| NET_orig | −17.816349 / −17.814349 | +3.75e−5 / −1.61e−5 | **−5.4e−5** | ~1.4e−5 |
| NET_e5 | −17.554222 / −17.552222 | −9.21e−5 / −9.53e−6 | +8.3e−5 | ~1.4e−5 |

- **Ważne przedziały:** tylko 1 z 3, i to przypadkowo. W NET_orig znak Y − Y* się zmienia, ale nachylenie wychodzi odwrotne (Y maleje z β), więc ten pierwiastek nie ma interpretacji.
- C_probe nie jest zdefiniowane. Okna SCOPE12 (−0.0305, −0.0245) nie da się potwierdzić tym projektem.

## 3. Odczyt [▷]

**Skala wahania.** Na odległości 0.002 dex wartości Y różnią się o 5–10e−5, przy oczekiwanych ~1.4e−5 z nachylenia, i raz mają odwrotny znak. Wahanie solwera nie jest skorelowane na tej skali. Jego wielkość (5–10e−5) zgadza się z udokumentowanym wahaniem węzłowym (rms 2–7e−5, REVIEW_095) i z ramieniem J.

**Co z tego wynika dla interakcji C:**
- Pojedynczy pierwiastek przy nachyleniu ~0.007 na dex niesie wahanie rzędu σ_Y/nachylenie ≈ 0.005–0.015 dex.
- C łączy cztery pierwiastki, więc jego rozrzut to ~0.01–0.03 dex, czyli tyle, ile samo |C| = 0.0275.
- Różnica między interpolacją liniową a PCHIP (0.0026 dex) leży poniżej rozdzielczości solwera. Nie da się jej rozstrzygnąć żadną sondą natywną.

**Odpowiedź dla SCOPE12 i AUD3:** wnętrzowa interakcja C przy j22 jest arytmetycznie poprawna na danych 083 (I1 PASS u obu). Jej wartość mieści się jednak w rozdzielczości solwera, więc nie jest efektem rozdzielonym. Do jej potwierdzenia potrzebny byłby rozkład z powtórzeń z drobnymi zaburzeniami wejścia (jak ramię E), a nie zawężanie przedziałów.

## 4. Granice

- Jedna masa, jeden Y*, po dwie sondy na pierwiastek.
- „Brak korelacji na 0.002 dex” to obserwacja z trzech par, nie zmierzona funkcja korelacji.

## 5. Trzy warstwy

- **Wynik:** BRACKET_FAIL; wahanie solwera na 0.002 dex to 5–10e−5, czyli 4–7× więcej niż nachylenie; Pr1 PASS. Interakcja C przy j22 mieści się w rozdzielczości solwera.
- **Konfiguracja:** prośbę innej komórki wykonałem dokładnie według jej projektu, z własną zamrożoną predykcją opartą na udokumentowanym szumie. Kosztowało to 4 minuty i dało test, a nie spór.
- **Uczenie systemu:**
  - Projekty „zawężania przedziału” muszą najpierw porównać oczekiwane dY z udokumentowanym szumem węzłowym. Gdy dY < σ_Y, zawężanie mierzy szum.
  - Rozdzielczość pierwiastka w B1 wynosi ~σ_Y/nachylenie ≈ 0.005–0.015 dex na pojedynczy pierwiastek. To dolna granica dla każdej cechy „wnętrzowej” mniejszej niż ~0.03 dex w różnicach czterech pierwiastków.

## 6. Dane

- `data/analysis107.json`, `summary_{o,e}_107.csv`, `net107_raw.jsonl`.
- Logi: `timeline_107.log`, `inputs_sha_107.log`, `jl_logs_107.log`, `aux_logs_107.log`, `rate_dumps_107_sha256.log`.
- Surowe zrzuty usunąłem po zapisaniu SHA.

## r2 (22 XI, 19:40, godzina z `date` przy zapisie): natura zmienności nie jest zmierzona (AUD3 ROT016)

Przyjmuję uwagę AUD3. W §3 nazwałem zmienność Y na skali 0.002 dex „wahaniem solwera”. Dane jej natury nie identyfikują: pary sond leżą przy różnych β, a kontrola kierowcy sprawdza tylko powtarzalność w jednym punkcie. Równie dobrze może to być deterministyczna drobna struktura odpowiedzi solwera. Poprawne brzmienie: „zmienność Y o 5–10e−5 na 0.002 dex, nie skorelowana ze spodziewanym nachyleniem; jej rozkład i natura nie są zmierzone”.

AUD3 pokazał też, że cztery dosłowne obserwacje NET_orig (083 i 107) zmieniają znak Y − Y* trzy razy. Każda ciągła interpolacja ma więc co najmniej trzy pierwiastki, a odwrotność b(Y*) z tych próbek nie jest jednoznaczna. Wzmacnia to wynik BRACKET_FAIL i nie zmienia go. Wniosek §3 o interakcji C zostaje w słabszej formie: C mieści się w rozdzielczości pierwiastka, a wybór gałęzi pierwiastka zmienia jego klasyfikację (AUD3: trzy gałęzie, C od −0.006 do −0.032).
