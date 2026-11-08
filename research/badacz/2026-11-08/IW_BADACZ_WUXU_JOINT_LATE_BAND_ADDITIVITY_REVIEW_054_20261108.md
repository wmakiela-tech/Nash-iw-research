---
artifact_id: IW_BADACZ_WUXU_JOINT_LATE_BAND_ADDITIVITY_REVIEW_054_20261108
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude)
created_at: 2026-11-08
document_type: REVIEW
preregistration: IW_BADACZ_WUXU_JOINT_LATE_BAND_ADDITIVITY_PREREG_052_20261108 (4281386, przed przebiegami)
responds_to: IW_INT9_ROT006_BAND_KERNEL_CROSS_FRONT_TRANSFER_GATE_001_20261108
code: code/wuxu_band_kernel.jl (bez zmian), code/wuxu_cd052_analysis.py
data: data/kernel_cd052.csv, data/configs_cd052.dat, data/cd052_analysis.json
claim_ceiling: MODEL_INTERNAL / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_054: A1 trzyma się przy podwojeniu późnych hadronów (błąd 0.013 dex), zawodzi przy ich usunięciu (0.053 dex, 3σ)

**Rola:** Badacz. Wykonałem natywnie tani separator zaproponowany przez INT9 ROT006 i dodałem do niego test dużej zmiany.

## Wynik (j = 22, natywny kod autorów `d395183`, tolerancja domyślna)

| konfiguracja | Δ zmierzone [dex] | A1 z osobnych pasm | tylko liczba hadronów | `s` łączne | `s_C + s_D` |
|---|---|---|---|---|---|
| CD2 (`k = 2` dla m < 3e8 g) | **−0.136 ± 0.007** | −0.149 ± 0.007 (z = 1.3) | −0.039 | 0.368 | 0.408 |
| CD0 (`k = 0` dla m < 3e8 g) | **+0.281 ± 0.007** | +0.228 ± 0.016 (z = 3.1) | +0.043 | 0.476 | 0.408 |

- Korzeń bazowy z tego samego przebiegu: `−17.2276`, wobec `−17.2197` w REVIEW_050. Dryf 0.008 dex mieści się w kontroli (≤ 0.01).

## Werdykty preregu

- **Kontrola dryfu: PASS.**
- **P1** (`Δ(CD2) ∈ [−0.174, −0.124]`): **PASS**.
- **P2** (`Δ(CD0) ∈ [+0.18, +0.28]`): **FAIL**. Wartość +0.281 leży tuż za granicą. Ważniejsze jest odchylenie od A1 o 3σ.
- **F1, F2: nie wyzwolone.**
  - Przy CD2 wynik jest daleko od przewidywania z samej liczby hadronów.
  - CD0 mieści się w szerokim przedziale `[+0.13, +0.33]`.

## Co to znaczy

- **Podwojenie późnych hadronów.** Mapa INT9 `Δ = −log10(1 + Σ(k_b−1)s_b)` przewiduje wynik z błędem 0.013 dex. Model „tylko liczba” myli się o 0.10 dex.
  - Przesłanka INT9 („C+D niosą ≈ 41% efektu przy ≈ 9% liczby”) potwierdza się wspólną zmianą obu pasm, a nie tylko sumą osobnych pomiarów.
- **Usunięcie późnych hadronów.** A1 nie działa dla dużych zmian. Efektywny udział `s` pasm C+D zależy od kierunku:
  - 0.37 przy `k = 2` (kontur przy mniejszym β);
  - 0.48 przy `k = 0` (kontur przy większym β).
- **Interpretacja `[▷]`.** Udział późnych pasm rośnie z β. Zgadza się to z nasyceniem odpowiedzi przy j = 22: lokalnie `d ln ΔY / d ln β ≈ 0.5`, podczas gdy przy j ≥ 28 jest ≈ 1. Wczesne hadrony nasycają się szybciej niż późne. Nie testowałem tego osobno.
- **Wniosek dla mostów.** Liniowa mapa pasm jest wiarygodna lokalnie, przy zmianach rzędu ×2 w kierunku większego wstrzykiwania. Przy dużych zmianach w dół, a zapewne też przy masach nasyconych, potrzebny jest natywny przebieg.
  - INT9 zapisał „Not a global A1 proof”. Ten test podaje skalę: 0.013 i 0.053 dex.
  - Tego samego zastrzeżenia nie przenoszę automatycznie na j ≥ 28, gdzie odpowiedź jest bliższa liniowej. To nie zostało tu zmierzone.

## Granice

- Wynik MODEL_INTERNAL, jedna masa (j = 22), cztery zgrubne pasma masy, mapa B_exec autorów.
- Bez fizycznej granicy PBH i bez jądra czas–energia.

## Powrót w trzech warstwach

- **Wynik:** A1 lokalnie PASS (P1), globalnie FAIL (P2, 3σ). Skala nieliniowości przy j = 22: 0.013 dex dla `k = 2` i 0.053 dex dla `k = 0`.
- **Konfiguracja:**
  - natywny przebieg trwał ok. 4 min, a zamienił propozycję INT9 w zmierzoną granicę jej stosowalności;
  - INT9 policzył przewidywanie z moich danych, a ja je natywnie przetestowałem. To jest dobry podział pracy międzyrodzinowej, choć to ja jestem autorem danych wejściowych.
- **Uczenie systemu:** `origin_failure_mode: LOCAL_LINEARITY_EXTRAPOLATED`. Mapę liniową z perturbacji ×2 łatwo stosować do usunięcia pasma (`k = 0`). Kandydat reguły `[▷]`: każda mapa A1 podaje zakres `k`, w którym została natywnie sprawdzona.
