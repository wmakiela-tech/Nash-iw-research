---
artifact_id: IW_BADACZ_WUXU_A1_TWO_DIRECTION_SOLVER_ROBUSTNESS_REVIEW_059_20261111
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude)
created_at: 2026-11-11
document_type: REVIEW
preregistration: IW_BADACZ_WUXU_A1_TWO_DIRECTION_SOLVER_ROBUSTNESS_PREREG_058_20261111 (3559a17, przed przebiegiem)
responds_to: REVIEW_054 (własny); AUD1 ROT035; REC11 ROT012; INT9 ROT011; KN13 ROT009; Mech-S8 ROT015
code: research/badacz/2026-11-08/code/wuxu_band_kernel.jl (bez zmian, BADACZ_TOL=1e-4:1e-7); code/wuxu_a1tol058_analysis.py
data: data/kernel_a1tol058.csv, data/configs_a1tol058.dat, data/a1tol058_analysis.json, data/RUNLOG.md, data/MANIFEST_SHA256.md
claim_ceiling: MODEL_INTERNAL / SELF_FALSIFICATION_TEST / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_059: złamanie A1 w obu kierunkach przy j = 22 przetrwało ostrzejszą tolerancję (G = 1.880; prereg: odporne)

**Rola:** Badacz. Testowałem własny wynik z REVIEW_054. Kilka komórek przyjęło go już za ustalony, a jego σ obejmowało tylko błąd dopasowania, bez szumu solvera.

## Wynik (j = 22, `reltol = 1e−4`, `abstol = 1e−7`; Δ względem bazy z tego samego przebiegu)

| wielkość | tolerancja domyślna (REVIEW_054) | `1e−4` (ten przebieg) |
|---|---|---|
| korzeń bazowy | −17.2276 ± 0.0048 | −17.2095 ± 0.0017 |
| Δ₂ (C+D ×2) | −0.1360 | −0.1362 |
| Δ₀ (C+D ×0) | +0.2810 | +0.2910 |
| `s` przy k = 2 / k = 0 | 0.368 / 0.476 | 0.369 / 0.488 |
| `G = 10^(−Δ₂) + 10^(−Δ₀)` (A1: 2) | 1.8914 | **1.8801** |
| `G` w sześcianie ±1 SE dopasowania | [1.850, 1.934] | [1.864, 1.896] |
| minimalny wspólny budżet korzeni `d*` (REC11 ROT012) | 0.0121 dex | 0.0134 dex |
| rozrzut punktów wokół prostej (σ_resid) | 6–9e−5 | 2.5–4.7e−5 |

- **Werdykt preregu: R (złamanie A1 odporne), bo `G_t = 1.880 ≤ 1.95`.** Przy ostrzejszej tolerancji odchylenie od A1 nawet nieco rośnie, a rozrzut punktów maleje mniej więcej trzykrotnie.
- **Przesunięcie korzeni przy zmianie tolerancji.** Wszystkie trzy przesuwają się w tę samą stronę: +0.018 (baza), +0.018 (CD2) i +0.028 (CD0) dex. To zgodne z REVIEW_047 (+0.025 przy j = 22).
  - Δ₂ się nie zmienia, Δ₀ rośnie o 0.010 dex.
  - Szum solvera jest więc w dużej części wspólny dla konfiguracji przy tej samej masie i skraca się w różnicach. Wyjaśnia to, dlaczego dryf bazy między przebiegami (0.008 dex) nie przełożył się na G.

## Co to znaczy

- Wnioski AUD1 ROT035, REC11 ROT012, KN13 ROT009, INT9 ROT011 i Mech-S8 ROT015 („nie przedłużać liniowego pudełka A1 na k = 0”) zostają w mocy także po uwzględnieniu numeryki solvera.
- Lokalna stosowalność A1 przy k = 2 też się utrzymuje: Δ₂ jest stabilne, a od przewidywania A1 (−0.149) dzieli je 0.013 dex.
- Zastrzeżenie z PREREG_058 było zasadne jako pytanie, ale odpowiedź jest negatywna dla hipotezy szumu. Nie było potrzeby niczego odwoływać.

## Granice

- Jedna masa (j = 22).
- Tolerancja `1e−4` nie jest certyfikatem błędu ODE.
- Wynik MODEL_INTERNAL, bez fizycznej granicy PBH i bez E4.

## Powrót w trzech warstwach

- **Wynik:** A1 przy k = 0 zawodzi także przy `reltol = 1e−4` (G = 1.880). REVIEW_054 utrzymany.
- **Konfiguracja:**
  - pięć komórek oparło się na moim wyniku, mając w ręku tylko σ dopasowania;
  - test odporności numerycznej kosztował ok. 28 min na jednym rdzeniu i zamyka tę lukę.
- **Uczenie systemu:**
  - `origin_failure_mode: FIT_SE_AS_TOTAL_UNCERTAINTY` (moje, w REVIEW_054): podałem „3σ” z błędu dopasowania 7 punktów, bez szumu ścieżki solvera.
  - Łatka: przy wynikach natywnych podawać osobno σ dopasowania i rozrzut między tolerancjami. Istotność liczyć z sumy, albo z różnic przy wspólnej bazie, jeśli szum jest skorelowany.
