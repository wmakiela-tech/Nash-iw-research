---
artifact_id: IW_BADACZ_B1_DIR008_NATIVE_TEST_REVIEW_093_20261122
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), współwłaściciel natywny B1 (wykonawca testu cudzej predykcji)
created_at: 2026-11-22
document_type: REVIEW (wynik zamrożonej PREREG_092; predykcje EKS1 ROT014)
follows: PREREG_092 (Nash-iw-research@4babc2d)
claim_ceiling: NUMERYCZNY w modelach [▷] / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_093: DIR-008 natywnie: P1 4/6, P2 2/2, teza EKS1 nieodrzucona; wszystkie sześć stosunków leży poniżej predykcji (średnio −0.018)

**Predykcje** należą do EKS1 (ROT014). Ja jestem wykonawcą testu i nie oceniam modelu, z którego je wyprowadzono.

## 1. Przebieg

- 16 wywołań `rate_dump_081.jl` od 07:39:26 do 07:45:54; oba sterowniki zakończyły się z rc = 0.
- Tablica HER: BlackHawk HERWIG R2, SHA 590c7eb6…. Zgodność sprawdzona w `inputs_sha_092.log` i w kopii drzewa źródeł.
- **Kontrola tożsamości sterownika:** świeże PY j22 przy log β = −16 jest bitowo równe wartości z `qa_B.csv` (Y = 0.2543578436853835). PASS.
- Analizę `analysis_092.py` powtórzyłem i wynik jest bitowo identyczny (SHA d845a7ef…).

## 2. Wynik według preregistracji

**P1** (ΔX_HER/ΔX_PY, tolerancja ±0.02):

| komórka | zmierzone | EKS1 | odchylenie | ocena |
|---|---|---|---|---|
| j19, −16 | 0.9463 | 0.964 | −0.018 | PASS |
| j19, −15 | 0.9364 | 0.975 | −0.039 | FAIL |
| j22, −16 | 0.9377 | 0.964 | −0.026 | FAIL |
| j22, −15 | 0.9643 | 0.977 | −0.013 | PASS |
| j24, −16 | 0.9546 | 0.965 | −0.010 | PASS |
| j24, −15 | 0.9782 | 0.981 | −0.003 | PASS |

**P2:**

| | PY: r(−16) / r(−15) | HER: r(−16) / r(−15) | model EKS1 | ocena |
|---|---|---|---|---|
| j21: brak przecięcia | 0.942 / 0.896 | 0.910 / 0.867 | 0.93 / 0.91 | PASS |
| j22: przecięcie | 1.535 / 1.467 | 1.446 / 1.420 | 1.51 / 1.48 | PASS |

**Wynik: P1 4/6, P2 2/2.** Teza nie jest odrzucona: żaden stosunek przy −15 nie spada poniżej 0.90, a P2 nie jest odwrócone.

## 3. Diagnostyka post hoc (nierejestrowana, nie zmienia wyniku k/n)

**Metoda** (`posthoc_092.py`):

- Szum punktowy w X szacuję z gęstej siatki PY w `qa_B` (log β od −16.5 do −15.0, co 0.1 dex). Miarą jest odchylenie standardowe reszt dopasowania kwadratowego.
- Wyniki: σ_X = 7.7e−6 (j19), 2.3e−5 (j22), 3.4e−5 (j24).
- Przeniesienie na stosunek zakłada, że szum HER jest taki sam jak PY, bo tylko PY ma gęstą siatkę.

**Wyniki:**

- Oba FAIL mają z ≈ −1.8 (j19, −15) i −2.2 (j22, −16).
- Po zastąpieniu PY wartością wygładzoną j22, −16 daje 0.945 (odchylenie −0.019). j19, −15 daje 0.939 (−0.036).
- Wszystkie 6 odchyleń jest ujemnych. Średnia wynosi −0.018, χ² = 11.8 przy 6 stopniach swobody.
- Komórki jednej masy dzielą przebiegi bazowe i siatkę PY, więc χ² jest tylko orientacyjne.

**Odczyt [▷]:**

- Pojedyncze FAIL mieszczą się w ~2σ szumu solwera.
- Wspólny znak sugeruje, że model EKS1 zawyża ΔX_HER/ΔX_PY o ~0.01–0.02.
- Tolerancja ±0.02 przy j19 jest równa σ stosunku (0.021). Ta komórka nie rozstrzyga niczego w żadną stronę.

## 4. Kontekst fizyczny: punkty testu leżą na plateau nasycenia

**Położenie punktów.**

- Log β = −16 i −15 leży poza domeną skanu autorów, w obszarze nasycenia opisanym w REVIEW_072 (dla j22 i j24 od −16.7).
- We wszystkich 8 krzywych (PY i HER, j19–j24) ΔX lekko maleje od −16 do −15, o 1–5%. To ten sam spadek za plateau, co w REVIEW_072.
- P1 mierzy więc stosunek wysokości plateau, a nie przesunięcie progu β w reżimie liniowym.

**Krawędź masowa.**

- Na plateau krawędź to masa, przy której r = 1.
- Interpolacja liniowa j21–j22 przy −16 daje: PY j ≈ 21.10, HER j ≈ 21.17. HER przesuwa więc krawędź o ≈ +0.0009 dex w masie.
- Krawędź jest tak sztywna, bo wysokość plateau rośnie stromo z masą: r rośnie od 0.94 do 1.53 na 0.012 dex.
- Dla porównania progi β w domenie autorów przesuwają się o dziesiąte części dex: tablice BlackHawk +0.32…+0.37 (REVIEW_086), generatory współczesne +0.13…+0.22 (REVIEW_091).
- To potwierdza jakościowo tezę EKS1: generator przesuwa próg β, a krawędzi masowej praktycznie nie.

**Mechanizm** (czas życia PBH względem zamrożenia oddziaływań słabych) jest znany. Nowości nie ma.

## 5. Granice

- Tablica HER to historyczna tablica BlackHawk R2. Wynik nie dotyczy pary współczesnej P83/H73.
- Każda komórka to pojedynczy przebieg. Szum HER oszacowałem pośrednio, z siatki PY.
- Krawędź masowa pochodzi z interpolacji między dwiema masami odległymi o 0.012 dex, przy jednym β.
- Model EKS1 jest prywatny i go nie recenzowałem. Testuję wyłącznie jego zamrożone liczby.

## 6. Trzy warstwy

- **Wynik:** P1 4/6, P2 2/2, teza nieodrzucona. Systematyczne odchylenie −0.018 [▷]. Krawędź masowa przesuwa się o ~0.001 dex, progi β o dziesiąte części dex.
- **Konfiguracja:** właściciel solwera natywnego wykonał test zamrożonych predykcji innej komórki, z kontrolą tożsamości sterownika. Całość zajęła 7 min obliczeń. Ten wzorzec warto powtarzać.
- **Uczenie systemu:**
  - Tolerancje predykcji między komórkami trzeba wyprowadzać z σ szumu przy danym ΔX, a nie ustalać jedną stałą. To samo zapisałem w REVIEW_072 dla progu rozdzielczości.
  - W PREREG_092 zgłosiłem, że ±0.02 może być poniżej szumu dla j19, ale nie wysłałem tego EKS1 przed przebiegiem. origin_failure_mode: KNOWN_TEST_WEAKNESS_NOT_ROUTED_BEFORE_RUN.
  - Przy wyborze punktów testu warto sprawdzić, czy leżą w reżimie liniowym, czy na plateau, bo oba mierzą co innego.

## 7. Dane

- `data/analysis092.json`, `posthoc092.json`, `summary_{h,p}_orig_092.csv`, `timeline_092.log`, `inputs_sha_092.log`, `jl_{h,p}_092.log`, `rate_dumps_092_sha256.log`.
- SHA w `MANIFEST_SHA256_092.md`.
- I1 zewnętrzne: przeliczenie 6 stosunków i 8 wartości r z `summary_*_092.csv` i `qa_B.csv`.
