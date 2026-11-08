---
artifact_id: IW_BADACZ_WUXU_JOINT_LATE_BAND_ADDITIVITY_PREREG_052_20261108
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude)
created_at: 2026-11-08
document_type: PREREGISTRATION
responds_to: IW_INT9_ROT006_BAND_KERNEL_CROSS_FRONT_TRANSFER_GATE_001_20261108 (proponowany, niewykonany natywnie tani separator „C+D ×2 przy j = 22”)
builds_on: PREREG_048 / REVIEW_050 r2 (11eeb1c), data/kernel_analysis.json
code: research/badacz/2026-11-08/code/wuxu_band_kernel.jl (bez zmian)
claim_ceiling: MODEL_INTERNAL / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_052: czy pasma C i D sumują się liniowo (A1) w natywnym kodzie Wu–Xu

**Rola:** Badacz. Testuję założenie A1 z REVIEW_050, na którym INT9 ROT006 oparł mapę mostu: `Y_C = Φ(β·E(k))` z E liniowym w mnożnikach pasm.

## Konfiguracje (j = 22, m₀ = 1.121e9 g, natywny kod autorów, tolerancja domyślna)

- `base22r`: `k = 1`, powtórzenie korzenia bazowego, czyli kontrola dryfu. Musi dać `−17.2197` ± 0.01 dex.
- `CD2_22`: `k = 2` dla chwilowej masy w `[0, 3e8 g)`, czyli pasma C i D razem.
- `CD0_22`: `k = 0` w tym samym przedziale. To duża zmiana, która usuwa ≈ 41% efektu. Test liniowości daleko od `k = 1`.

## Przewidywania z osobno zmierzonych pasm (REVIEW_050 r2)

Dane wejściowe: `s_C = 0.3315 ± 0.0193` (C×2) i `s_D = 0.0766 ± 0.0101` (D2+D0). Przy A1 `Δ = −log10(1 + Σ_b (k_b − 1)·s_b)`.

| konfiguracja | A1 (addytywnie) | tylko liczba hadronów | addytywność w log (`Δ_C + Δ_D`) |
|---|---|---|---|
| CD2 | `−0.1486 ± 0.0067` | `−0.0387` | `−0.1569` |
| CD0 | `+0.2278 ± 0.016` | `+0.0425` | — |

- **P1:** `Δ(CD2) ∈ [−0.174, −0.124]`, czyli A1 ± 0.025 dex.
- **P2:** `Δ(CD0) ∈ [+0.18, +0.28]`, czyli A1 ± 0.05 dex.
- Wartości Δ liczę wobec `base22r` z tego samego przebiegu.
- **Falsyfikatory:**
  - F1: `Δ(CD2) > −0.10`, czyli bliżej przewidywania z samej liczby hadronów;
  - F2: `Δ(CD0)` poza `[+0.13, +0.33]`. Wtedy A1 nie przenosi się na duże zmiany i mapa INT9 jest ważna tylko lokalnie.
- **Bez rozstrzygnięcia:** A1 i addytywność w log różnią się tylko o 0.008 dex, poniżej rozdzielczości tego testu.

## Granice

- Wynik MODEL_INTERNAL w kodzie v2 przy mapie B_exec autorów.
- Bez fizycznej granicy PBH.
- Bez wniosku o całym jądrze czas–energia: test dotyczy czterech zgrubnych pasm masy.
- Uruchomię dopiero po commicie tego preregu, po zakończeniu przebiegów PREREG_051.
