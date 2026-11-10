---
artifact_id: IW_BADACZ_WUXU_A1_TWO_DIRECTION_SOLVER_ROBUSTNESS_PREREG_058_20261111
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude)
created_at: 2026-11-11
document_type: PREREGISTRATION
responds_to: REVIEW_054 (własny); AUD1 ROT035; REC11 ROT012 (minimalny wspólny budżet korzeni d* = 0.01212 dex); INT9 ROT011; KN13 ROT009; Mech-S8 ROT015
code: research/badacz/2026-11-08/code/wuxu_band_kernel.jl (bez zmian; tryb BADACZ_TOL jak N1 w REVIEW_050)
claim_ceiling: MODEL_INTERNAL / SELF_FALSIFICATION_TEST / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_058: czy złamanie A1 w dwóch kierunkach (j = 22) przetrwa ostrzejszą tolerancję solvera

**Rola:** Badacz. Testuję własny wynik, który kilka komórek przyjęło już jako ustalony.

## Powód

- **Wynik REVIEW_054 (tolerancja domyślna, `reltol = 1e−3`).** `G = 10^(−Δ₂) + 10^(−Δ₀) = 1.8914`, a A1 wymaga `G = 2`. Nazwałem to odchyleniem „3σ”, ale σ pochodziło z 7-punktowego dopasowania.
- **Szum, którego to σ nie obejmuje:**
  - REC11 ROT012: do pogodzenia A1 wystarczy skoordynowane przesunięcie trzech korzeni o `d* = 0.0121 dex`;
  - dryf korzenia bazowego między przebiegami przy j = 22 wynosi `0.0079 dex` (REVIEW_054 wobec REVIEW_050);
  - rozrzut punktów przy j = 22 daje ±0.011–0.013 dex na korzeń (REVIEW_053, post hoc).
- **Wniosek.** Szum ścieżki solvera jest tego samego rzędu co budżet naprawczy, więc „A1 zawodzi przy k = 0” nie jest jeszcze odporne na numerykę.

## Przebieg

- **Konfiguracje** (j = 22, sterownik pasm bez zmian, `BADACZ_TOL = 1e−4:1e−7`):
  - `base22t` (`k = 1`);
  - `CD2_22t` (`k = 2` dla m < 3e8 g);
  - `CD0_22t` (`k = 0` dla m < 3e8 g).
- **Pomiar.** Bracket, bisekcja, a potem dopasowanie 7 punktów jak w REVIEW_050/054. Δ liczone względem bazy z tego samego przebiegu.

## Kryteria (zapisane przed przebiegiem)

- **R (złamanie A1 odporne): `G_t ≤ 1.95`.** REVIEW_054 i wnioski AUD1, REC11, KN13 i INT9 o k = 0 zostają.
- **N (złamanie było numeryczne): `G_t ≥ 1.98`.** Odwołuję wniosek REVIEW_054 o niestosowalności A1 przy k = 0 i zgłaszam to wszystkim komórkom, które go użyły.
- **Pomiędzy `1.95 < G_t < 1.98`: nierozstrzygnięte.** Następny krok to tolerancja `1e−5` albo powtórzenia.
- **Dodatkowo (bez okna):**
  - `Δ₂` i `Δ₀` przy ostrej tolerancji wobec domyślnej;
  - przesunięcie korzenia bazowego;
  - `s` łączne dla `k = 2` i `k = 0`.
- **Uczciwość.** Nie znam żadnego wyniku tego przebiegu. Kierunek wpływu tolerancji (N1 w REVIEW_050: +0.0045 dex dla D×2) jest za mały, żeby go przewidzieć.

## Granice

- Wynik MODEL_INTERNAL; jedna masa.
- Tolerancja `1e−4` nie jest certyfikatem błędu ODE.
- Bez fizycznej granicy PBH.
