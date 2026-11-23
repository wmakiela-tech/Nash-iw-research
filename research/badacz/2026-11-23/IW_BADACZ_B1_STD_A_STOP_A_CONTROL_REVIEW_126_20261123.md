---
artifact_id: IW_BADACZ_B1_STD_A_STOP_A_CONTROL_REVIEW_126_20261123
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel przebiegów natywnych B1
created_at: 2026-11-23
document_type: REVIEW (wynik PREREG_125, commit e346be4)
answers: REC14 ROT011/ROT014 (STOP A), EKS1 ROT028 (IDEA-A)
claim_ceiling: NUMERYCZNY w modelu kodu Wu–Xu [▷] / MODEL_CONDITIONAL / NO_PBH_BOUND / NO_AUTHOR_ERROR_ESTABLISHED / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_126: kontrola STOP A dla STD_A (kontynuacja q_h poniżej 1e9 g)

## 1. Wynik zgodny z prerejestracją

- Bramki G_TAB i G_RUN: PASS. Run: 18/18 procesów (22:54–23:06), bez przerw.
- Predykcje: 3/3 PASS.
- Powtórka analizy bitowo identyczna. Dane: `data/run125/` (tablice w gzip).

**Pierwiastki Y_code = 0.251 (log10 β) dla różnych kontynuacji poniżej 1e9 g:**

| kontynuacja (s, α) | base j22 | std j22 | **Δ(j22)** | base j62 | std j62 | **Δ(j62)** | std j20 |
|---|---|---|---|---|---|---|---|
| m10 (−1.0, 0) | −17.111 | −18.541 | −1.430 | −19.379 | −19.631 | −0.252 | −18.294 |
| kod (~−1.20, ~0.2; run123) | −17.225 | −18.609 | −1.384 | −19.389 | −19.633 | −0.244 | −18.369 |
| m13 (−1.3, 0.3) | −17.266 | −18.648 | −1.382 | −19.395 | −19.636 | −0.241 | −18.416 |
| m15 (−1.5, 0.5) | −17.388 | −18.728 | −1.340 | −19.398 | −19.637 | −0.239 | −18.494 |

Base przy j20 nie ma pierwiastka w [−21, −16] przy żadnej kontynuacji.

- **P_A1 PASS.** Δ(j22) mieści się w −1.430…−1.340, czyli w ±0.05 od kodu (tolerancja ±0.15).
- **P_A2 PASS.** Δ(j62) mieści się w −0.252…−0.239.
- **P_A3 PASS.** Pierwiastek std przy j20 istnieje dla każdego s (−18.29…−18.49).

**Raportowane bez progu.**
- Bezwzględny próg base przy j22 zależy od kontynuacji: rozstęp 0.28 dex (−17.11…−17.39). Przy j62 rozstęp wynosi 0.02 dex.
- α_PY = 0.305–0.317: lokalny wykładnik krotności hadronów w tablicach PYTHIA BlackHawk przy E′ = 1e4–1e5 GeV, dla kwarków u, d, s, c, b i gluonów.
  - Fizycznie umotywowana kontynuacja to więc s ≈ −1.31. Zgadza się z receptą artykułu (T^1.3), a nie z nachyleniem wierszy 0–1 tablicy, którego używa kod (−1.20).
  - W tej kontynuacji próg base przy j22 jest o 0.041 dex niższy niż w kodzie. To zgadza się z REVIEW_117: tam −0.061 dla tablicy Sc, z przewidywaniem, że dla tablicy autorów efekt będzie mniejszy.

## 2. Odczyt [▷]

- **Przesunięcie STD_A jest odporne na kształt kontynuacji.** W przedziale α ∈ [0, 0.5] zmienia się o ≤ 0.09 dex przy j22, podczas gdy bezwzględny próg przesuwa się o 0.28 dex. Zmiana kontynuacji przesuwa oba ramiona podobnie, a przesunięcie pochodzi z czasu życia.
- **Część STOP A dotycząca nachylenia jest zamknięta dla przesunięcia, nie dla progu bezwzględnego.**
- **Otwarte zostaje:**
  - normalizacja przy 1e9 g (obcięcie E′ ≤ 1e5 GeV, ~4% mocy, efekt rzędu 0.02 dex);
  - założenie jednego α dla dżetów powyżej 100 TeV, bez bezpośredniej hadronizacji;
  - G_DEP;
  - STOP B (trzy mapy Y_P);
  - brak sieci PRyMordial.

## 3. Ocena konfiguracji i uczenie systemu

- Bez pilotów i bez przerw. Cały przebieg trwał 12 min i zmieścił się w jednej turze; zastosowałem łatkę z REVIEW_124.
- Przedział α jest uzasadniony fizycznie (stały ułamek energii w hadronach), a nie arbitralny. Zmierzone α_PY leży w jego środku.
- Nowych trybów awarii brak.
- **origin_observation.** Recepta artykułu (T^1.3) ma poparcie w skalowaniu krotności PYTHIA; ekstrapolacja kodu ma je słabsze. Wpływ na próg base jest mały (0.04 dex przy j22).

## 4. Dalej (decyzja Moderatora)

1. Ramię sieciowe PRyMordial dla STD_A przy j22 i j62 (STOP B).
2. IDEA-C (Thoss 2024, HERWIG przy ~1e11–1e14 g).
3. I1 spoza rodziny Claude dla REVIEW_124/126.
