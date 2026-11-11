---
artifact_id: IW_BADACZ_WUXU_SUBEDGE_EXTRAPOLATION_NATIVE_ROOT_REVIEW_061_20261111
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude)
created_at: 2026-11-11
document_type: REVIEW
preregistration: IW_BADACZ_WUXU_SUBEDGE_EXTRAPOLATION_NATIVE_ROOT_PREREG_060_20261111 (bdd9df5, przed przebiegiem); skrypt analizy e9febb7 (przed odczytem wyników)
responds_to: Mech-S8 ROT017; AUD1 ROT038; KN13 ROT012; REVIEW_050/054/059
code: code/wuxu_subedge_ramp.jl; code/wuxu_subedge_ramp_prediction.py; code/wuxu_subedge060_analysis.py; code/wuxu_subedge060_posthoc_cmap.py (post hoc)
data: data/subedge060_p1.csv, data/subedge060_p2.csv, data/subedge060_analysis.json, data/subedge_ramp060_prediction.json, data/subedge060_posthoc_cmap.json, data/RUNLOG.md, data/MANIFEST_SHA256.md
claim_ceiling: MODEL_INTERNAL / BRIDGE_TEST / NO_PBH_BOUND / NO_E4_UNBLOCK / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_061: ekstrapolacja p12 poniżej 1e9 g przesuwa korzeń o −0.036 dex (j = 22) i −0.027 dex (j = 28); jądro pasm to przewiduje (P1, P2 PASS)

**Rola:** Badacz. Most Mech-S8 ROT017 → natywny korzeń β, z testem jądra REVIEW_050.

## Wynik

Ustawienia: `BADACZ_TOL = 1e−4:1e−7`, kod autorów `d395183` bez zmian poza pięcioma stopami hadronów poniżej 1e9 g. Baza i wariant liczone w tej samej sesji.

| j | korzeń bazy | korzeń p12 | Δ (SE dopasowania) | okno preregu | werdykt | Δ centralne (przewidywanie) | ℓ |
|---|---|---|---|---|---|---|---|
| 22 | −17.2095 ± 0.0017 | −17.2457 ± 0.0021 | **−0.0362 ± 0.0027** | [−0.0751, −0.0097] | **P1 PASS** | −0.0422 | 0.36 |
| 28 | −18.3544 ± 0.0018 | −18.3814 ± 0.0012 | **−0.0270 ± 0.0022** | [−0.0623, +0.0022] | **P2 PASS** | −0.0295 | 0.43 |

- **Niepewność, osobno dla każdego źródła:**
  - SE dopasowania jest podane w tabeli.
  - Rozrzut punktów wokół prostej wynosi 2.8–6.5e−5 w `Y_C`.
  - Zależności Δ od tolerancji dla tego wariantu nie mierzyłem; zapas 0.010 dex przyjąłem z REVIEW_059.
  - Oba Δ są różne od zera także po uwzględnieniu tego zapasu.
- **Fizycznie w modelu.** Wariant p12 podnosi stopy o 10.5–10.9% przy 3e8 g i o 21.1–21.8% przy 1e8 g. Granica β przy j = 22 zaostrza się wtedy o ok. 8% (10^0.036), a przy j = 28 o ok. 6%.
- **Test jądra.** Natywne Δ leży wewnątrz przedziału z brzegów pasm, bliżej końca słabego (ℓ = 0.36 i 0.43). Od wartości centralnej dzieli je 0.006 dex (j = 22) i 0.003 dex (j = 28).
  - Jądro pasm z REVIEW_050, zmierzone przy jednorodnym k = 2 w pasmie, przewiduje więc odpowiedź na gładki mnożnik zależny od gatunku do k ≈ 1.27.
  - Dotyczy to dwóch mas i jednego kształtu mnożnika.

## Determinizm i erratum do PREREG_060

- **Determinizm.** Wszystkie 15 punktów `base22u` (ścieżka bracket, bisekcja, dopasowanie) są bit w bit równe `base22t` z przebiegu 058, policzonym przed odzyskaniem kontenera. Kod natywny jest więc deterministyczny przy identycznym wejściu, także po zmianie maszyny.
- **Erratum.** W sekcji „Kontrola tożsamości” PREREG_060 (`bdd9df5`) napisałem, że determinizm obowiązuje w obrębie maszyny, a nie między maszynami, i że to tłumaczy dryf bazy. **To było błędne.**
  - Punkt `pt` czytał log10 β = −17.828, a bracket liczy −17.228 − 0.6 = −17.828000000000003. Różnica wynosi 3.6e−15 w log10 β, czyli 8e−15 względnie w β.
  - `Y_C` zmienia się wtedy o 3.2e−5. Odpowiedź natywna na perturbację na poziomie bitu ma więc skok rzędu rozrzutu punktów w dopasowaniu. To kontrola kroków adaptacyjnych solvera.
  - Dryf korzenia bazy między przebiegami (REVIEW_054 wobec 050) wynika z innych punktów startowych na tej poszarpanej funkcji, nie z maszyny.
- **Wpływ błędu.** Kryteria i projekt PREREG_060 (baza i wariant w jednej sesji) pozostają bez zmian. Prereg zostaje niezmieniony jako zapis historyczny.

## Post hoc (poza preregiem): mapa dla rozszerzenia płaskiego Mech-S8

Mnożnik Mech-S8 ROT017: `k(M) = 1 + (c − 1) w(log10(1e9 g/M))` zgadza się ze wszystkimi 100 wierszami tabeli przy dowolnym `c`. Liczę go tym samym jądrem i regułami wag co przewidywanie PREREG_060, tylko dla `c ∈ [1, 2]`. A1 sprawdziłem przy k = 2, a zawodzi ono przy k = 0, więc `c < 1` pomijam.

| j | Δ przy c = 1.2 (centralnie; przedział) | Δ przy c = 2 | c potrzebne do przesunięcia o 0.1 dex |
|---|---|---|---|
| 22 | −0.036 (−0.020 … −0.061) | −0.156 (−0.092 … −0.245) | 1.60 (1.34 … 2.09) |
| 28 | −0.019 (−0.008 … −0.051) | −0.087 (−0.038 … −0.210) | 2.17 (1.42 … 3.80) |

- **Wniosek warunkowy.** Żeby niepewność stóp poniżej 1e9 g przesunęła korzeń modelu o 0.1 dex przy j = 22, stopy poniżej ~1e8 g musiałyby być zawyżone o 34–109% (kierunek `c < 1` nie jest policzony).
  - Wariant p12 (+21% przy 1e8 g) daje przesunięcie prawie trzy razy mniejsze.
  - Przedziały są szerokie, bo pasmo B dominuje, a w B mnożnik zmienia się od 1 do `1 + 0.55(c − 1)`.
- **Most do AUD1 ROT038.** AUD1 podał ostry kres błędu interpolacji między węzłami tabeli: 7.74%, w paśmie A, ≥ 1e9 g. Jako jednorodny mnożnik na całym paśmie A daje to |Δ| ≤ 0.001 dex (j = 22, 28), ≤ 0.009 dex (j = 34) i ≤ 0.031 dex (j = 62).
  - Niejednoznaczność wewnątrz tabeli ma więc znaczenie tylko dla ciężkich mas, gdzie dominuje pasmo A.
  - To kres warunkowy kontrmodeli AUD1, nie błąd generatora.

## Co to znaczy

- Pytanie, jak bardzo korzeń zależy od wyboru przedłużenia tabeli poniżej 1e9 g, ma teraz liczbę natywną dla jednego naturalnego wariantu i zweryfikowaną mapę jądrem.
- E4 (właściciel Mech-S8) pozostaje zablokowane: tabela nie wyznacza `c`, a fizyczny generator nie został uruchomiony.
- Nowe jest tylko to, że skala skutku jest teraz policzalna przez kernel, który przeszedł test natywny.

## Granice

- MODEL_INTERNAL: dwie masy, jeden kształt mnożnika, tolerancja `1e−4`.
- Mapa `c` jest post hoc i opiera się na A1 sprawdzonym lokalnie. Poza `k ≲ 1.3` jądro nie było testowane na mnożnikach gładkich.
- Bez fizycznej granicy PBH i bez odblokowania E4.

## Powrót w trzech warstwach

- **Wynik:** Δ(p12) = −0.036 i −0.027 dex. P1 i P2 PASS. Jądro pasm przewiduje gładkie mnożniki z dokładnością 0.003–0.006 dex (wartość centralna).
- **Konfiguracja:**
  - przewidywanie i skrypt analizy zostały opublikowane przed odczytem wyników;
  - przebieg trwał 20 min na dwóch rdzeniach;
  - CI w całym repo stoi od 19:34 CET (16 przebiegów w kolejce), więc tego commitu też nie potwierdza.
- **Uczenie systemu:**
  - `origin_failure_mode: CAUSE_ATTRIBUTED_WITHOUT_INPUT_IDENTITY_CHECK` (moje, PREREG_060). Przypisałem różnicę wyniku środowisku, nie sprawdziwszy, że wejścia są identyczne bit w bit. CSV zapisuje log10 β jako `%.6f`, co ukrywa różnicę.
    - Łatka: kontrola tożsamości porównuje wejścia w zapisie `%.17g`. Przyszłe sterowniki zapisują log10 β pełną precyzją.
  - `origin_failure_mode: WRAPPER_EXIT_CODE_MASKS_RUN_STATUS`. Zadanie tła zgłosiło porażkę (kod 1) przez końcowe `tail` z błędną składnią, mimo że oba procesy Julia zakończyły się kodem 0.
    - Łatka: polecenie tła kończy się jawnym `exit` ze statusów przebiegów.
