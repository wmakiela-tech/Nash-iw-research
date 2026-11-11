---
artifact_id: IW_BADACZ_WUXU_HEAVY_END_NATIVE_CLOCK_REVIEW_057_20261111
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude)
created_at: 2026-11-11
document_type: REVIEW
preregistration: IW_BADACZ_WUXU_HEAVY_END_NATIVE_CLOCK_PREREG_056_20261111 (bdc8906, 00:03:26, przed przebiegiem)
responds_to: IW_MT14_ROT026_WUXU_THERMAL_EVENT_CLOCK_TNUC_MASS_THRESHOLD_001_20261103
code: code/wuxu_heavy_end_clock_record.jl, code/wuxu_heavy_end_clock_analysis.py
data: data/heavy_end_clock.csv, data/heavy_end_clock_analysis.json, data/heavy_end_clock_tol1e-4.csv (post hoc, r2), data/RUNLOG.md, data/MANIFEST_SHA256.md
revision: r2 (11 XI) — dodana diagnostyka tolerancji (pkt 3); werdykty preregu bez zmian; r1 = 5b5521e
claim_ceiling: MODEL_INTERNAL_RECORD / NO_PBH_BOUND / NO_OWNER_DISPOSITION / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_057: zegar MT14 zgadza się z natywnym do 0.006 s (j = 97–99); przy ciężkim końcu 58–66% hadronów pada po T1, a 10–27% po T_nuc, poza obserwablą kodu

**Rola:** Badacz. Zapis natywny, o który MT14 ROT026 prosił jako o rozstrzygający. Właściciel Fig. 5 i E4 (Mech-S8) bez zmian.

## 1. Natywny zapis (tolerancja domyślna; β = 1e−30 / β = 10^−19.2)

| j | M0 [g] | t(T0) [s] | t(T1) [s] | M(T0) natywnie [g] | M(T0) z zegara MT14 [g] | odchylenie M | τ efektywne − τ | hadrony po T1 | hadrony po T0 |
|---|---|---|---|---|---|---|---|---|---|
| 62 | 3.494e9 | 215.077 / 214.904 | 123.54 / 123.42 | wyparowała (t_ev ≈ 10.2 s) | wyparowała | — | — | 0 | 0 |
| 97 | 9.447e9 | 214.962 / 214.966 | 123.52 / 123.52 | wyparowała (t_ev ≈ 201.4 s) | wyparowała | — | — | 58% | 0 |
| 98 | 9.720e9 | 214.965 / 214.956 | 123.52 / 123.52 | 2.489e9 / 2.523e9 | 2.398e9 | +3.8% / +5.1% | +0.18% / +0.25% | 62% | 10% |
| 99 | 1.000e10 | 214.971 / 214.967 | 123.52 / 123.52 | 4.580e9 / 4.613e9 | 4.571e9 | +0.20% / +0.93% | +0.06% / +0.30% | 66% | 27% |

- **Zegar odniesienia.** MT14 ROT026 daje `t(T0) = 214.9675 s`. W tabeli „odchylenie M” liczę względem `M0(1 − t_native/τ)^{1/3}`; liczby MT14 różnią się od tego o ≤ 0.03%.
- **„τ efektywne”** to czas życia, który odtwarza natywne `M(T0)` przy prawie `M³ ∝ (τ − t)`.
- **Udziały hadronów** to liczba hadronów z tabeli autorów, emitowanych po T1 (0.0997 MeV) albo po T0 (`T_nuc`), przy natywnym `M(T)`.
- **Rozdzielczość `t_ev`.** `magic()` zapisuje 10 000 punktów geometrycznie w a, więc `t_ev` ma rozdzielczość ≈ 0.9% i jest obciążony w górę. Wartości `t(T)` i `M(T)` są interpolowane w log T i tego obciążenia nie mają.

## 2. Werdykty preregu

- **P1 (zegar termiczny, okno ±1 s): PASS.** Natywne `t(T0)` przy β = 1e−30 wynosi 214.962–214.971 s dla j = 97–99, czyli 0.006 s od MT14, oraz 215.077 s dla j = 62 (+0.11 s).
  - Zredukowany zegar MT14 (bez PBH, z kotwicą `t(10 MeV)`) odtwarza więc natywny z dokładnością ≤ 0.05%.
  - Różnica przy j = 62 jest zgodna z rozrzutem ścieżki solvera (pkt 3).
- **P2 (prawo masy, okno 2%): FAIL** przy j = 98: +3.8% przy β = 1e−30 i +5.1% przy 10^−19.2. Przy j = 99 PASS: +0.20% i +0.93%.
  - Przyczyna to wzmocnienie blisko końca parowania. Względny błąd masy wynosi `(t/τ)/(3(1 − t/τ))` razy względny błąd czasu życia, czyli ×21.9 dla j = 98 i ×3.2 dla j = 99.
  - Wyrażone jako czas życia, natywne punkty odchylają się od `τ = 0.2376664 s·(M0/1e9)³` o +0.06…+0.30%.
  - Okno 2% na masę było więc źle dobrane dla masy tak bliskiej progu: przy j = 98 nie rozróżnia odchylenia czasu życia o 0.1%. Werdykt zostaje FAIL.
- **P3 (klasyfikacja): PASS.** j = 62 i 97 wyparowują przed `T_nuc` (`t_ev` ≈ 10.2 i 201.4 s), a j = 98 i 99 nie. Próg MT14 (9.67e9 g) się potwierdza.
- **P4 (sprzężenie zwrotne PBH, okno 0.1 s): FAIL** przy j = 62: −0.17 s. Dla j = 97–99 PASS: |Δt| ≤ 0.009 s.
  - Przy j = 62 zawyżona jest wartość bazowa (+0.11 s wobec pozostałych mas), więc różnica pokazuje rozrzut solvera, a nie sprzężenie zwrotne.
  - Okno 0.1 s było niespójne z oknem P1 (±1 s), które sam ustawiłem z powodu tolerancji solvera.

## 3. Diagnostyka tolerancji (post hoc, poza preregiem; r2)

- **Przebiegi.**
  - `reltol = 1e−6` przerwałem po 32 min bez ukończenia pierwszego punktu.
  - Wykonałem te same rekordy przy `reltol = 1e−4`, `abstol = 1e−7` (j = 62, 98, 99 × oba β), czyli przy tolerancji N1 z REVIEW_050.

| j | β | t(T0) [s] (Δ wobec MT14) | M(T0) [g] | odchylenie M | τ_eff − τ |
|---|---|---|---|---|---|
| 62 | 1e−30 | 214.854 (−0.113) | wyparowała | — | — |
| 62 | 10^−19.2 | 215.000 (+0.033) | wyparowała | — | — |
| 98 | 1e−30 | 214.964 (−0.003) | 2.3949e9 | −0.15% | −0.007% |
| 98 | 10^−19.2 | 214.963 (−0.005) | 2.3895e9 | −0.39% | −0.018% |
| 99 | 1e−30 | 214.963 (−0.005) | 4.5712e9 | 0.00% | −0.001% |
| 99 | 10^−19.2 | 214.961 (−0.006) | 4.5709e9 | −0.01% | −0.004% |

- **Odczyt.**
  - Przy ostrzejszej tolerancji prawo masy `τ ∝ M³` zgadza się z natywnym do ≤ 0.02% w czasie życia (masa przy j = 98: −0.15% zamiast +3.8%). FAIL P2 przy tolerancji domyślnej był więc szumem solvera, wzmocnionym ×22 blisko końca parowania. Kod autorów nie ma innego prawa masy.
  - Dla j = 98 i 99 `t(T0)` zgadza się z MT14 do 0.006 s, a efekt β na zegar wynosi ≤ 0.002 s.
  - Przy j = 62 `t(T0)` skacze o ±0.1 s także przy `1e−4`. Znak „sprzężenia” odwraca się (−0.17 s domyślnie, +0.15 s przy `1e−4`), więc to rozrzut solvera dla masy wyparowującej wcześnie, nie efekt PBH.
- **Werdykty preregu (P2, P4 FAIL) zostają**, bo dotyczą przebiegu zarejestrowanego.
- **Uboczny wniosek dla wszystkich natywnych przebiegów przy domyślnej tolerancji:** wielkości bliskie osobliwości (koniec parowania) mają szum rzędu procentów, a `t(T0)` dla wczesnych mas rzędu 0.1 s.

## 4. Co z tego wynika

1. **Zegar MT14 ROT026 jest natywnie potwierdzony.**
   - `t(T_nuc)` zgadza się z natywnym do ≤ 0.05%, a prawo masy `τ ∝ M³` do ≤ 0.3% w czasie życia przy tolerancji domyślnej i do ≤ 0.02% przy `1e−4` (pkt 3).
   - Klasyfikacja „j = 98, 99 nie wyparowały przy T_nuc” zachodzi.
   - To było sprawdzenie, które MT14 nazwał rozstrzygającym. Wynik nie wymaga korekty progu 9.67e9 g.
2. **Na ciężkim końcu obserwabla kodu pomija część wstrzykiwania.** `magic()` czyta X przy `T_nuc`, a przy j = 98 i 99 po `T_nuc` pada odpowiednio 10% i 27% liczby hadronów.
   - To fakt o modelu (MODEL_INTERNAL), nie błąd kodu: po rozpoczęciu nukleosyntezy hadrony działają innymi kanałami (fotodysocjacja i hadrodysocjacja lekkich jąder), których ten model nie zawiera.
   - Kontur Y_P przy M0 ≥ 9.67e9 g opiera się więc na niepełnej historii wstrzykiwania. Nie oceniam, czy i jak zmienia to fizyczną granicę.
3. **Uzupełnienie REVIEW_053.** Wariant V1 (punkt celu przy T1 = 0.0997 MeV) pomija przy j = 97–99 hadrony emitowane po T1, czyli 58–66% całej liczby. Stąd jego rozjazd z V2 przy 1e10 g (+0.34 wobec +0.085 dex).
   - `[▷]` Jeśli właściciel przyjmie poprawkę wzoru Y_P, na ciężkim końcu V2 jest mniej zależny od wyboru chwili celu niż V1. To uwaga do decyzji Mech-S8, nie rozstrzygnięcie.

## 5. Granice i odtworzenie

- Wynik MODEL_INTERNAL, w kodzie v2 i przy mapie B_exec autorów.
- Bez fizycznej granicy PBH, bez tożsamości Fig. 5 i bez E4.
- Udziały hadronów dotyczą liczby z tabeli autorów, nie wagi odpowiedzi konturu (por. jądro pasm z REVIEW_050).

```text
julia --project=<env> code/wuxu_heavy_end_clock_record.jl <arXiv-2509.05618 @ d395183> data/heavy_end_clock.csv 62,97,98,99 -30,-19.2
BADACZ_TOL=1e-4:1e-7 julia --project=<env> code/wuxu_heavy_end_clock_record.jl <…> data/heavy_end_clock_tol1e-4.csv 62,98,99 -30,-19.2   # post hoc (r2)
python3 -I code/wuxu_heavy_end_clock_analysis.py --csv data/heavy_end_clock.csv --table <…>/data/out/hadrons_from_PBH.dat --out data/heavy_end_clock_analysis.json
```

## 6. Powrót w trzech warstwach

- **Wynik:**
  - zegar MT14 jest potwierdzony natywnie (P1, P3 PASS);
  - P2 i P4 FAIL przez źle dobrane okna (wzmocnienie ×22 przy j = 98; rozrzut solvera przy j = 62). Diagnostyka r2 przy `1e−4` potwierdza, że to szum: masa −0.15% i τ_eff ≤ 0.02%;
  - przy ciężkim końcu 10–27% hadronów pada po `T_nuc`, poza obserwablą kodu.
- **Konfiguracja:**
  - komórka teorii (MT14) przewidziała, a natywny przebieg (Badacz) rozstrzygnął w ≈ 2 minuty obliczeń;
  - to wzorzec R1 z OW §9a: test zamiast kolejnego STOP.
- **Uczenie systemu:**
  - `origin_failure_mode: WINDOW_WITHOUT_SENSITIVITY_MAP`: okna preregu ustawiałem dla wielkości końcowej (M, t), nie licząc ich wzmocnienia względem parametru (τ). Łatka: okno na wielkość pochodną przeliczać przez jej czułość. Przy wielkościach bliskich osobliwości (koniec parowania) testować parametr (τ_eff), nie wynik.
  - Moje okna P1 i P4 były wzajemnie niespójne (±1 s wobec 0.1 s przy tym samym solverze).
