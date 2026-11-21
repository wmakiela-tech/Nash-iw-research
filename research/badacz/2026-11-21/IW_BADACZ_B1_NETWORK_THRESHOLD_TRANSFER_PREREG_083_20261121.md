---
artifact_id: IW_BADACZ_B1_NETWORK_THRESHOLD_TRANSFER_PREREG_083_20261121
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), współwłaściciel natywny B1, właściciel T2
created_at: 2026-11-21
document_type: PREREGISTRATION (zamrożona przed jakimkolwiek przebiegiem pomiarowym)
authorization: przygotowanie w ramach kierunku Moderatora 21 XI 12:41 („prowadź swoje badania naukowe”). Uruchomienie wymaga osobnej zgody Moderatora (przebiegi Julii).
follows: REVIEW_082 r2 (`SHIFT_TRANSFERS` przy kotwicy kodu 0.251; Nash-iw-research@65fd67b)
responds_to: PRF14 ROT007 (kotwica 0.251 ≠ cel LBT), KN15 ROT004 / AUD3 ROT004 / LT9 ROT007 (luka bazowa kod vs pełna sieć), REC13 ROT007 i Mech-S10 ROT007 (runner fail-open)
claim_ceiling: NUMERYCZNY w modelach (transfer szybkości) / NO_PBH_BOUND / NO_PAPER_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_083: progi β w pełnej sieci dla rzeczywistych celów helowych (0.251 i LBT 0.2484) i odporność przesunięcia ładunkowego na kotwicę

## 0. Pytania

- **Q1 (kotwica).** PREREG_081 pokazał przenoszalność D przy poziomie efektu, który odpowiada progowi kodu 0.251. PRF14 słusznie zauważył, że z tego nie wynika przenoszalność przy celu LBT 2026 (Y_p ≤ 0.2484). Pytanie: czy D_net jest takie samo przy obu celach, w pełnej sieci z jej własną linią bazową?
- **Q2 (próg).** Jak przesuwa się sam próg β z kodu Wu–Xu, gdy jego natywna historia konwersji przechodzi przez pełną sieć z jej linią bazową (0.24687 zamiast 0.2447)?
  - To pierwszy w projekcie bezpośredni pomiar łączący luki bazowej (AUD3, LT9, KN15) z niezidentyfikowanym wzmocnieniem (INT10, PRF14), bez swobodnego parametru.
  - Mieści się nadal w modelu transferu wyłącznie szybkości.

## 1. Metoda (bez zmian względem PREREG_081)

- **Eksport natywny:** `rate_dump_081.jl` (bez zmian; V2_EXACT i zagęszczenie przy śmierci PBH).
- **Deduplikacja:** `dedupe_rates_081.py`, teraz zaplanowana z góry.
- **Sieć:** PRyMordial z hakiem 079 (`net_rate_079.py` bez zmian), η = 6.1e-10, τ_n = 878.4 s, mała sieć.
- **Nowe: runner z twardymi bramkami** (`run083.sh`, `run_net_083.py`). Przyjmuję w ten sposób zarzut REC13 ROT007 i Mech-S10 ROT007:
  - świeży katalog roboczy wymagany (odmowa, jeśli istnieje);
  - rc ≠ 0 Julii, porażka deduplikacji, niekompletne ID lub porażka sieci oznaczają stop z rc ≠ 0 i brak „ALL_DONE”;
  - odmowa nadpisania wyników.

## 2. Plan (zamrożony; `gen_cfg_083.py` → `cfg083_*.dat`, `grid083.json`)

- **Masy:** j ∈ {22, 38, 62, 90}. To lekka, pośrednia, ciężka i parująca blisko T_nuc kodu.
- **Siatka:** ramiona orig i E5. Wielokrotności 0.05 dex od ⌊(root − 1.20)/0.05⌋ do ⌈(root + 0.10)/0.05⌉, gdzie root to pierwiastek T2 M_D. Daje to 28 węzłów na (masę, ramię).
- **Bazy:** log β = −30 dla czterech mas.
- **Łącznie:** 228 wywołań Julii i 229 + 4 przebiegi sieci. Szacunek: ~1 h CPU.
- **Przypadki V4/V5:** węzły orig najbliższe pierwiastkom T2 dla j22 i j62 (o22_1720, o62_1940).

## 3. Wielkości (cele Y* ∈ {0.251, 0.2484}, każdy model z własną linią bazową)

- **Pierwiastki** (liniowo w log β między węzłami obejmującymi poziom; wymagane dokładnie jedno przecięcie):
  - lb_code_{arm}(Y*): log β, przy którym natywne Y_C = Y*;
  - lb_net_{arm}(Y*): log β, przy którym Y_net z transferu = Y*.
- **Przesunięcia ładunkowe:** D_code(Y*) = lb_code_E5 − lb_code_orig oraz D_net(Y*) = lb_net_E5 − lb_net_orig.
- **Przesunięcie progu przez transfer:** T_orig(Y*) = lb_net_orig − lb_code_orig, analogicznie T_E5.
- **Dodatkowo** ρ dla każdego węzła.

## 4. Bramki (progi a priori ponad szumem; reguła z REVIEW_080)

| bramka | warunek |
|---|---|
| V1 | natywne Y = owner qa_A / t2 dla węzłów pokrywających się, \|Δ\| ≤ 1e-12, co najmniej 1 dopasowanie na (masę, ramię); bazy wobec qa_A |
| V2_EXACT | ≤ 1e-6 |
| V3 | \|Y_net(szybkości bazowe) − Y0_net\| ≤ 1e-5 |
| V4 | tol × 1e-2 zmienia ΔY_net o ≤ 1% |
| V5 | stride 2 zmienia ΔY_net o ≤ 1% |
| V6 | zagęszczenie zastosowane |
| **V7 (nowa)** | komplet 228 natywnych ID i 233 ID sieci, wszystkie rc = 0 |

## 5. Etykiety (zamrożone)

- **L1, odporność przesunięcia ładunkowego na kotwicę:**
  - `SHIFT_ANCHOR_ROBUST`, jeśli |D_net(0.2484) − D_net(0.251)| ≤ 0.02 dex dla wszystkich 4 mas;
  - inaczej `SHIFT_ANCHOR_DEPENDENT`.
- **L2, przeniesienie progu:**
  - `TRANSFER_MATERIAL`, jeśli |T_orig(0.251)| > 0.05 dex dla którejkolwiek masy;
  - inaczej `TRANSFER_SMALL`.
- Brak przecięcia w którymkolwiek szeregu: `NOT_BRACKETED`. Porażka bramki: `GATE_FAIL_NO_LABEL`.
- **Żadna etykieta nie jest granicą PBH.** Nawet `TRANSFER_MATERIAL` mówi tylko, że próg kodu Wu–Xu nie przenosi się bez zmian do pełnej sieci w modelu transferu szybkości.

## 6. Predykcje Badacza [▷] (poinformowane przez REVIEW_082; ujawnione)

- **P1:** T_orig(0.251, j22) < −0.15 dex. Rachunek: sieć potrzebuje ΔY = 0.00413, a kod 0.00625; przy ρ ≈ 1.32 daje to około −0.3 dex.
- **P2:** T_orig(0.251, j62) ∈ [−0.25, 0].
- **P3:** `SHIFT_ANCHOR_ROBUST`.
- **P4:** T_orig(0.2484) < T_orig(0.251) dla wszystkich mas, bo przy celu LBT relatywna luka bazowa waży więcej.

## 7. Zamrożony kod (`research/badacz/2026-11-21/code/`)

| plik | SHA-256 |
|---|---|
| `gen_cfg_083.py` | 0dc7f3eca3dd839ad2267cafb07ee49e45c228a7cd1c9e804f74692acb6be2f6 |
| `cfg083_orig.dat` | c7847ba01ce345f31df2b9ff35efb0e9014837270deece1e6aaa8f1bd43d8a30 |
| `cfg083_e5.dat` | 9e96bb8b94b7c47bd97d17b1fc3e5d42c696c832429d89fdc3ec252ceb72a646 |
| `grid083.json` | dd27037afb98ee29dcd30724fa90002dea93d6b6b9ad53125e47d4933b6d6b24 |
| `run083.sh` | 29d65a1e31ca2de47dec4f0c2dbf3850e955c4ca344abe04de04186ff561db05 |
| `run_net_083.py` | cef93454e94ae75a53f227ffe3ef1a2f5aa36838315182fbfb710c44c4f91421 |
| `analysis_083.py` | 2a5b0b390de107c7e1efb0724ec605c16918c57720474ea2d934e6edf2ea661b |
| `rate_dump_081.jl` (bez zmian) | fbbce938b7b798a18500d16d9795acfb958dc66e40ed73e7715fb57a03d0e0ee |
| `dedupe_rates_081.py` (bez zmian) | 10a24000e3026f437e24b10c272953b80ae559fa9fb30807ef6c3c2266a8b6de |
| `net_rate_079.py`, `prym_rate_patch_079.py` (bez zmian) | 866f90fc… / 93989e68… |

## 8. Ujawnienie i granice

- **Ujawnienie:** przed zamrożeniem nie było żadnego nowego przebiegu. Do zaprojektowania siatki użyłem wyłącznie pierwiastków T2 oraz istniejących wierszy qa_A.
- **Granice jak w REVIEW_082 §5.3 i §8:**
  - transfer wyłącznie szybkości;
  - bez sprzężenia zwrotnego pionów;
  - bez tła PBH w sieci;
  - jedna sieć;
  - bez fotodysocjacji, hadrodysocjacji i E4.
- Dla j90 część emisji przypada po T_nuc kodu, a zatem w erze, w której te nieobecne procesy mogą ważyć.
- Cel 0.2484 to literalne 2σ LBT 2026 (LT9 ROT007), a nie fizyczny 95% CL (REC13 ROT006).
- **I1 zewnętrzne wymagane.**
