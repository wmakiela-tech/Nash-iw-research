---
artifact_id: IW_BADACZ_WUXU_REVIEW053_J22_ROOT_METHOD_TOLERANCE_PREREG_064_20261113
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude)
created_at: 2026-11-13
document_type: PREREGISTRATION
responds_to: EKS1 ROT010 (test rozstrzygający dla właściciela REVIEW_053); KN13 ROT022 i Mech-S9 ROT007–009 (natywna replika GPT: L1 53/53, L2 8/10, dwa FAIL przy j = 22 V2); REC11 ROT025/027
code: code/wuxu_yp_formula_counterfactual_tol.jl (kopia sterownika REVIEW_053 z przełącznikiem BADACZ_TOL; ścieżka domyślna bez zmian)
claim_ceiling: MODEL_INTERNAL / SELF_FALSIFICATION_TEST / NO_PBH_BOUND / NO_E4_UNBLOCK / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_064: czy rozbieżność L2 przy j = 22 (V2) to szarpanie funkcji przy tolerancji domyślnej

**Rola:** Badacz, właściciel REVIEW_053.

## Powód

- **Wyniki repliki zewnętrznej (GPT).**
  - L1, czyli moja siatka REVIEW_053: zgodność co do cyfry w 53/53 punktach.
  - L2, adaptacyjna bisekcja: 8/10 kryteriów. Oba FAIL dotyczą j = 22 V2: korzeń −16.9975 wobec mojego −17.0209 i przesunięcie V2 − V0 = 0.2266 wobec 0.1942.
- **Hipoteza EKS1 ROT010.** To szarpanie funkcji autorów przy tolerancji domyślnej, a nie różnica implementacji. Na tych samych danych różne metody dają korzeń V2 od −17.017 do −16.986.
- **Dlaczego j = 22 V2 jest czułe.** V2 to ten sam natywny `Y_code(T0)` co V0, tylko przy progu 0.25235 zamiast 0.251. Różnica V2 − V0 zależy więc od nachylenia i krzywizny jednej funkcji między dwoma progami, a to właśnie psuje szarpanie.

## Przebieg

Sterownik `code/wuxu_yp_formula_counterfactual_tol.jl` to sterownik REVIEW_053 z jedną zmianą (przełącznik tolerancji, jak w REVIEW_050/059). Kod autorów `d395183`. Kalibracja SBBN (j = 22 i j = 62) w każdym procesie, w tej samej tolerancji.

| proces | tolerancja | punkty |
|---|---|---|
| 1 | `1e−4:1e−7` | siatka REVIEW_053 `g22` (9 punktów, −17.369678 … −16.769678, krok 0.075) oraz siatka gęsta, połowa A (16 punktów) |
| 2 | `1e−4:1e−7` | siatka gęsta, połowa B (15 punktów); razem 31 punktów od −17.40 do −16.80 z krokiem 0.02 |
| 3 | domyślna | ta sama siatka gęsta, 31 punktów |

Wartości log10 β to liczby zaokrąglone do 6 miejsc. Wydruk `%.6f` odtwarza więc bity wejścia (łatka z REVIEW_061).

## Metody korzenia (każda dla V0, V1, V2 i przesunięć V1 − V0, V2 − V0)

- **M_A:** metoda REVIEW_053 (kwadratowa przez 4 punkty wokół pierwszej zmiany znaku) na siatce `g22`.
- **M_B:** ta sama metoda na siatce gęstej.
- **M_C:** interpolacja liniowa między dwoma punktami gęstymi, które otaczają zmianę znaku (odpowiednik bisekcji).
- **M_D:** lokalna prosta OLS przez 7 punktów gęstych najbliższych zmianie znaku.

Progi: V0 `Y_code − 0.251`, V1 `2X(T1) − 0.251`, V2 `2X(T0) − 2X0s − 0.006`. `X0s` i `T1` biorę z kalibracji SBBN tego samego procesu.

## Kryteria (zapisane przed przebiegiem)

Niech `S` oznacza rozrzut (maksimum minus minimum) metod M_A–M_D przy `1e−4`.

- **J1 (wyjaśnienie szarpaniem utrzymane):** `S(V2) ≤ 0.010` i `S(V2 − V0) ≤ 0.010` dex. Wtedy:
  - podaję wartości `1e−4` jako aktualne dla j = 22;
  - wartości REVIEW_053 (tolerancja domyślna) zostają jako historyczne, a „8 z 10” w L2 się nie zmienia;
  - trzecia cyfra przesunięcia V2 przy j = 22 to szum metody przy tolerancji domyślnej.
- **J0 (wyjaśnienie obalone):** `S(V2) ≥ 0.020` albo `S(V2 − V0) ≥ 0.020` dex. Czułość na metodę zostaje także przy `1e−4`, czyli to nie tylko szarpanie, lecz krzywizna lub inna przyczyna. Przesunięcie V2 przy j = 22 jest wtedy nieoznaczone na poziomie 0.02 dex, co zgłaszam komórkom, które go użyły (SYNTH_055, EKS1, Mech-S9, KN13).
- **Pomiędzy:** wynik nierozstrzygnięty.
- **Bez okna:**
  - `S` przy tolerancji domyślnej (proces 3) wobec `S` przy `1e−4`;
  - rozrzut wokół gładkiego trendu (kwadrat przez wszystkie 31 punktów) przy obu tolerancjach;
  - wartości `1e−4` wobec REVIEW_053 i wobec L2;
  - ponowna kalibracja SBBN: T1 i X0s przy `1e−4` wobec `0.099688851247` i `0.109037947009`.

## Uczciwość i granice

- Nie znam żadnego punktu `1e−4` przy j = 22 w okolicy korzeni V1 i V2 (około −17.14 i −17.0).
- Znam REVIEW_059: `1e−4` przy j = 22 w sterowniku pasm, korzeń V0 −17.2095. Jego punkty leżą jednak w pobliżu −17.21 (dopasowanie ±0.09) oraz w dwóch punktach bracketu, −17.828 i −16.628. β jest tam budowane inaczej (`ArbFloat(10)^ArbFloat(lb)`).
- Znam też liczby L1 i L2.
- Jedna masa (j = 22). Wynik MODEL_INTERNAL, bez granicy PBH i bez E4.
- To moja samokontrola, nie audyt zewnętrzny. Replika GPT pozostaje odniesieniem zewnętrznym.
