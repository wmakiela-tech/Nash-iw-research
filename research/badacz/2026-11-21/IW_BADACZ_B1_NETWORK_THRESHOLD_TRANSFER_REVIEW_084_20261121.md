---
artifact_id: IW_BADACZ_B1_NETWORK_THRESHOLD_TRANSFER_REVIEW_084_20261121
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), autor PREREG_083
created_at: 2026-11-21
document_type: RESULT_REVIEW (wynik przebiegu zamrożonego PREREG_083; I1 zewnętrzne WYMAGANE)
prereg: IW_BADACZ_B1_NETWORK_THRESHOLD_TRANSFER_PREREG_083_20261121 (Nash-iw-research@1d6a76c)
authorization: Moderator 21 XI 15:48 „Autoryzuję” (RUNLOG_20261121)
claim_type: NUMERYCZNY w modelach (transfer szybkości kodu Wu–Xu do PRyMordial) + INTERPRETACYJNY [▷] oddzielony; dekompozycja w §4 POST-HOC
claim_ceiling: NO_PBH_BOUND / NO_PAPER_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN; status [▷] do zewnętrznego I1
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_084: wynik PREREG_083 — `SHIFT_ANCHOR_ROBUST` + `TRANSFER_MATERIAL`

## 1. Wykonanie i bramki

- **Runner z twardymi bramkami** (świeży katalog, rc i kompletność ID):
  - Julia 116 + 112 = 228 wywołań, rc = 0 (15:49–16:36);
  - deduplikacja: 76 z 228 plików, w każdym usunięty jeden duplikat T;
  - sieć 233/233 (16:37–16:53), ALL_DONE.
- **Bramki: 7/7 PASS.**

| bramka | wynik |
|---|---|
| V1 | 60/60 pokrywających się węzłów bitowo = qa_A / t2; każdy z 8 przypadków ma ≥ 3 dopasowania |
| V2_EXACT | maks. 5.9e-9 (próg 1e-6) |
| V3 | ≤ 1.2e-6 (próg 1e-5) |
| V4 | 0.06% i 0.02% |
| V5 | 0.31% i 0.04% |
| V6 | zagęszczenie zastosowane wszędzie |
| V7 | 228/228 i 233/233 |

## 2. Wyniki (zamrożone estymandy)

**Przesunięcie ładunkowe D = lb_E5 − lb_orig [dex]:**

| j | D_code(0.251) | D_net(0.251) | D_net(0.2484, LBT) | \|ΔD_net\| między kotwicami |
|---|---|---|---|---|
| 22 | 0.279 | 0.278 | 0.265 | 0.0135 |
| 38 | 0.281 | 0.282 | 0.277 | 0.0047 |
| 62 | 0.297 | 0.298 | 0.298 | 0.0006 |
| 90 | 0.302 | 0.302 | 0.301 | 0.0004 |

**L1 = `SHIFT_ANCHOR_ROBUST`** (wszystkie ≤ 0.02 dex). Korekta normalizacji ładunkowej (orig → per stan) przesuwa próg β w pełnej sieci o +0.26…+0.30 dex, niezależnie od tego, czy celem jest 0.251, czy LBT 0.2484. Odpowiada to na zarzut PRF14 ROT007 w zakresie tego modelu.

**Progi i ich przesunięcie przez transfer, T_orig = lb_net_orig − lb_code_orig [dex]:**

| j | lb_code_orig(0.251) | lb_net_orig(0.251) | T_orig(0.251) | lb_code_orig(0.2484) | lb_net_orig(0.2484) | T_orig(0.2484) |
|---|---|---|---|---|---|---|
| 22 | −17.223 | −17.709 | **−0.486** | −17.619 | −18.209 | **−0.590** |
| 38 | −19.009 | −19.169 | −0.160 | −19.243 | −19.601 | −0.358 |
| 62 | −19.388 | −19.485 | −0.097 | −19.623 | −19.921 | −0.298 |
| 90 | −19.366 | −19.412 | −0.046 | −19.599 | −19.842 | −0.243 |

- **L2 = `TRANSFER_MATERIAL`.**
- Przy tej samej natywnej historii konwersji i linii bazowej pełnej sieci próg β Wu–Xu przesuwa się w stronę ostrzejszego ograniczenia: o 0.05–0.49 dex przy 0.251 i o 0.24–0.59 dex przy LBT.
- T_E5 różni się od T_orig o ≤ 0.02 dex (w tabeli danych).

**ρ = ΔY_net/ΔY_code (mediana węzłów, orig):** j22 1.32, j38 0.98, j62 0.81, j90 0.73. Ramiona E5 dają prawie te same wartości.

## 3. Predykcje (PREREG_083 §6; poinformowane przez REVIEW_082, ujawnione)

| predykcja | wynik | status |
|---|---|---|
| P1: T_orig(0.251, j22) < −0.15 | −0.486 | PASS |
| P2: T_orig(0.251, j62) ∈ [−0.25, 0] | −0.097 | PASS |
| P3: `SHIFT_ANCHOR_ROBUST` | tak | PASS |
| P4: T_orig(LBT) < T_orig(0.251) dla wszystkich mas | tak | PASS |

## 4. Dekompozycja T_orig — POST-HOC, opisowa [▷] (nie była w preregu)

Rozdzielam T_orig na dwie części:
- **część bazowa:** przesunięcie, jakie dałaby sama zmiana linii bazowej (0.24475 → 0.24687) przy odpowiedzi kodu;
- **część odpowiedzi:** reszta, czyli efekt ρ.

| j | cel | T_orig | bazowa | odpowiedzi |
|---|---|---|---|---|
| 22 | 0.251 | −0.486 | −0.313 | −0.173 |
| 22 | 0.2484 | −0.590 | −0.428 | −0.162 |
| 38 | 0.251 | −0.160 | −0.176 | +0.016 |
| 38 | 0.2484 | −0.358 | −0.352 | −0.006 |
| 62 | 0.251 | −0.097 | −0.186 | +0.090 |
| 62 | 0.2484 | −0.298 | −0.379 | +0.081 |
| 90 | 0.251 | −0.046 | −0.179 | +0.133 |
| 90 | 0.2484 | −0.243 | −0.380 | +0.137 |

Wnioski z dekompozycji:
- **Dominuje luka bazowa** kod vs pełna sieć (≈ 0.0021 w Y). To ilościowe potwierdzenie zastrzeżenia LT9 ROT007, AUD3 ROT004 i KN15 ROT004; pierwszeństwo należy do nich, a do rozbieżności 2X vs 2X/(1−X) do AUD1/PRF11/Mech-S8.
- Część odpowiedzi ma znak zależny od masy:
  - **zaostrza** dla j22, bo kod wygasza wczesne konwersje mocniej niż sieć;
  - **łagodzi** dla j62 i j90, bo późne konwersje kod przelicza na hel z nadmiarem. Dla j90 dochodzi jeszcze odcięcie odczytu przy T_nuc.

## 5. Granice i wrażliwość

- **Model transferu wyłącznie szybkości** (REVIEW_082 §5.3 i §8):
  - bez sprzężenia zwrotnego pionów;
  - bez tła PBH (H, ogrzewanie) w sieci;
  - jedna sieć (PRyMordial, mała);
  - dopasowanie po T;
  - bez fotodysocjacji, hadrodysocjacji i E4.
  - Dla j90 część emisji przypada przy T ≲ T_nuc, gdzie brakujące procesy mogą ważyć.
- **Wrażliwość na linię bazową sieci** (uwaga post-hoc): Y0_net = 0.24687 (PRyMordial, η = 6.1e-10, τ_n = 878.4 s) leży między Yeh (0.2467) a Bianco (0.2472 ± 0.0008).
  - Przy celu LBT budżet ΔY wynosi tylko 0.00153. Niepewność teoretyczna rzędu 0.0003–0.0008 to 20–50% tego budżetu, więc progi przy LBT są **silnie** wrażliwe na Y0 sieci.
  - Liczby z §2 są właściwe dla tej konkretnej sieci i tych parametrów, a nie dla „fizyki”.
- **Cele:** 0.251 to 2σ PDG użyte przez Wu–Xu; 0.2484 to literalne 2σ LBT 2026 (LT9 ROT007), a nie 95% CL (REC13 ROT006).
- **To nie jest granica PBH ani twierdzenie o błędzie w artykule.**

## 6. Co z tego wynika dla B1 [▷]

1. **Korekta T2 (+0.27…+0.30 dex w β) jest odporna:**
   - natywnie odtworzona (Mech-S10 T2R);
   - przenoszalna do pełnej sieci (REVIEW_082);
   - niezależna od kotwicy celu (ten przegląd);
   - stała w czterech masach j22–j90.
   Zakres: model transferu szybkości.
2. **Bezwzględne progi Wu–Xu są obciążone o 0.05–0.6 dex**, głównie przez linię bazową helu w kodzie. Kierunek: pełna sieć zaostrza ograniczenie. Wielkość zależy od Y0 sieci i celu.
3. **Następny fizyczny krok** (nie zlecam go sam):
   - niezależna sieć (LINX; PRF14 ROT007 §4) na tych samych szybkościach;
   - kontrola wrażliwości progów na Y0 sieci (η, τ_n, kompilacja szybkości);
   - tło PBH w sieci.

## 7. Audyt i proweniencja

- **I1 zewnętrzne wymagane:** REC13 lub AUD3 do danych i analizy; PRF14 do drugiej sieci. Audyt Claude nad Claude nie jest zewnętrzny.
- **Kod:** SHA-256 jak w PREREG_083 §7 (11/11 zweryfikowane przed startem).
- **Dane** (`data/`, sufiks 083):
  - podsumowania natywne;
  - wyniki sieci;
  - log deduplikacji;
  - timeline;
  - SHA-256 228 pełnych i 228 zdeduplikowanych zrzutów (1.5 GB lokalnie; natywne Y bitowo deterministyczne, V1);
  - `analysis083.json`.
- Manifest: `MANIFEST_SHA256_083.md`.
- Dekompozycja z §4 to jednorazowe przeliczenie z `analysis083.json` i podsumowań, opisane w tekście. Nie jest częścią zamrożonej analizy.
