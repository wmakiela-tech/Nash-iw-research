---
artifact_id: IW_BADACZ_B1_RESPONSE_GAIN_REVIEW_078_20261120
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), autor PREREG_077
created_at: 2026-11-20
document_type: RESULT_REVIEW (wynik przebiegu zamrożonego PREREG_077; I1 zewnętrzne WYMAGANE)
prereg: IW_BADACZ_B1_RESPONSE_GAIN_PREREG_077_20261120 (Nash-iw-research@0140c0e)
authorization: Moderator 20 XI 15:20 „Masz zgodę” (RUNLOG_20261120)
claim_type: NUMERYCZNY w modelu (odpowiedź liniowa dwóch kodów na kontrolowany kick) + INTERPRETACYJNY [▷] oznaczony osobno
claim_ceiling: NO_PBH_BOUND / NO_PAPER_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN; status [▷] do zewnętrznego I1
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_078: wynik PREREG_077 — `GAIN_T_DEPENDENT`

## 1. Wynik w skrócie

- **Bramki:**
  - V0 (baza NET 0.246874): PASS.
  - V2 (każdy kick zastosowany dokładnie raz, identyczny stan przed kickiem w parach ±): PASS 18/18.
  - V3 (baza CODE = natywny wiersz qa_A j22, log10β = −30): PASS bitowo (0.24474916002311889).
- **Zbiór rdzeniowy:** 8 z 11 punktów (0.8 … 0.105 MeV). Wypadają 2.0, 1.5 i 1.2 MeV, z powodów opisanych w §3.
- **Etykieta (reguła zamrożona): `GAIN_T_DEPENDENT`.** R rośnie monotonicznie z temperaturą kicku: od 1.064 przy 0.8 MeV do 1.285 przy 0.105 MeV (max/min = 1.21 > 1.05).
- **Predykcje:** P1, P2 i P3 przeszły (§4). Ponieważ etykieta brzmi T_DEPENDENT, przeniesienie Y_C → Y_p wymaga splotu z historią źródła, zgodnie z §5 preregu. Ten pomiar go nie daje.

## 2. Dane (A = 2e-3; G = ΔY_końcowe / ΔY_n przy T_p)

| T_p [MeV] | G_net | G_code | R = G_code/G_net | X_net(T_p) | X_code(T_p) | rdzeń |
|---|---|---|---|---|---|---|
| 3.0 | −0.0002 | −0.0000 | — | 0.396 | 0.395 | nie (\|G\| < 0.05) |
| 2.0 | 0.0018 | −0.0052 | — | 0.350 | 0.349 | nie (\|G\| < 0.05) |
| 1.5 | 0.0549 | 0.1320 | (2.40) | 0.312 | 0.310 | nie (V4/V5 CODE, V5 NET) |
| 1.2 | 0.2489 | 0.2434 | (0.98) | 0.282 | 0.279 | nie (V4/V5 CODE) |
| 0.8 | 0.8024 | 0.8538 | **1.064** | 0.232 | 0.227 | tak |
| 0.6 | 1.1128 | 1.2416 | **1.116** | 0.205 | 0.199 | tak |
| 0.45 | 1.3035 | 1.5030 | **1.153** | 0.187 | 0.178 | tak |
| 0.35 | 1.4030 | 1.6559 | **1.180** | 0.176 | 0.165 | tak |
| 0.25 | 1.4857 | 1.8003 | **1.212** | 0.167 | 0.153 | tak |
| 0.18 | 1.5489 | 1.9192 | **1.239** | 0.160 | 0.143 | tak |
| 0.13 | 1.6264 | 2.0627 | **1.268** | 0.153 | 0.133 | tak |
| 0.105 | 1.7143 | 2.2027 | **1.285** | 0.145 | 0.125 | tak |
| 0.095 | 1.7694 | 2.2905 | 1.295 | 0.140 | 0.120 | opisowy |
| 0.088 | 1.8230 | 2.3708 | 1.301 | 0.136 | 0.116 | opisowy |
| 0.082 | 1.8769 | 2.4575 | 1.309 | 0.131 | 0.112 | opisowy |
| 0.075 | 1.9504 | **0.0000** | — | 0.106 | 0.106 | opisowy |
| 0.068 | 1.9759 | **0.0000** | — | 0.010 | 0.100 | opisowy |
| 0.06 | 1.9673 | **0.0000** | — | 0.000 | 0.090 | opisowy |

**Kontrole:**
- Liniowość (A = 1e-3 vs 2e-3) w rdzeniu:
  - NET ≤ 1.4% (maksimum przy 0.8 MeV, poza nim ≤ 0.7%). Rozrzut ±1% traktuję jako szum numeryczny PRyMordial przy ΔY ~ 1e-3; bramka V4 wynosi 3%.
  - CODE ≤ 0.07%.
- Tolerancja:
  - NET (rtol, atol × 1e-2) przy 0.45, 0.18 i 0.105: ≤ 0.2%;
  - CODE (1e-4 vs default) w rdzeniu: ≤ 0.02%.
- Duża sieć (63 reakcje) przy 0.45 i 0.13: odchylenie ≤ 0.09%.
- Offset bazowy Y0_code − Y0_net = −0.00212.

Pełny wynik: `data/analysis077.json`; dane surowe w `data/`.

## 3. Odchylenia i ograniczenia wykonania

- **DEV-1 (techniczne, tylko ramię tol = 1e-4).**
  - Zamrożony driver (`ContinuousCallback`) przerwał się przy pierwszym kicku z błędem DiffEq „Current interpolant only works between tprev and t”. Ramię tol = default (73/73) przeszło bez błędu.
  - Próby (a) RightRootFind i (b) tolerancje typu ArbFloat nie usunęły błędu.
  - Próba (c) `code_gain_077_dev1.jl` zadziałała. Kick ma tę samą definicję (natychmiastowy, przy T_SM = T_p), ale jest umieszczany przez `PresetTimeCallback` w η_p, interpolowanym z przebiegu bazowego tej samej tolerancji. Przy β = 1e-30 T_SM(η) nie zależy od X.
  - Błąd położenia |T_kick/T_p − 1|: w rdzeniu 9e-7 … 3.3e-5; maksymalnie 3.8e-4 w punktach opisowych przy niskich T.
  - W próbach nie oglądałem Y. Ramię 1e-4 służy wyłącznie bramce V5.
- **Przerwanie przez restart środowiska.** Przebieg DEV-1 został przerwany po 33/37 wierszach. Ponowiłem go w całości; 33/33 wspólne wiersze są **bitowo identyczne**, co daje dodatkową kontrolę powtarzalności.
- **T_p ≥ 1.2 MeV.** G jest tam małe (kick w dużej mierze wymazuje równowaga słaba; P2), a G_code przy tol default jest zdominowane szumem solvera (np. 1.5 MeV: 0.132 przy A = 2e-3 vs 0.039 przy A = 1e-3). **R nie jest tam wyznaczone.** To ważne, bo właśnie tam wypada epoka parowania j22 (T ≈ 1.5 MeV, Mech-S10 ROT006).

## 4. Predykcje Badacza (zamrożone w PREREG_077 §6)

- **P1:** R(0.25), R(0.18), R(0.13) ∈ [1.10, 1.45]. Otrzymano 1.212, 1.239, 1.268: **PASS**.
- **P2:** wczesne kicki wymazane. G(3.0) / G(0.25) wynosi −1.7e-4 (NET) i ≈ −1e-13 (CODE): **PASS**.
- **P3:** G_code = 0 poniżej T_nuc kodu (0.0782 MeV), G_net(0.075) > 0.5. Otrzymano 0, 0, 0 oraz 1.95: **PASS**.

Zgodność predykcji z wynikiem nie jest dowodem mechanizmu. To przewidywania tego samego autora, który projektował pomiar, więc I1 jest zewnętrzne.

## 5. Interpretacja [▷] (oddzielona od liczb; do I1)

1. **Kod przeszacowuje odpowiedź helu na to samo zaburzenie neutronów o 6–31%, tym więcej, im później zaburzenie powstaje** (R od 1.06 przy 0.8 MeV do 1.31 przy 0.082 MeV). Hipoteza rozkładu:
   - **Późno** (kick po wymrożeniu): R ≈ 1.29–1.31 odpowiada odwzorowaniu Y_C = 2X/(1−X), dla którego dY/dX = 2/(1−X)² ≈ 2.5, wobec pełnej sieci, gdzie późny neutron daje ≈ 2. To P1.
   - **Wcześnie** R maleje do ~1.06. Kod szybciej wymazuje wczesny kick niż sieć; prawdopodobnie przybliżone szybkości słabe 255/τ_n·(12 + 6x + x²)/x⁵ wobec pełnych szybkości PRyMordial. Tego nie testowałem.
2. **Ślepota na późne wstrzyknięcia.** Y_C odczytuje X przy T_nuc = 0.0782 MeV, więc konwersje p↔n później nie wpływają na wynik kodu. W pełnej sieci późny neutron nadal daje G ≈ 1.95–1.98 aż do 0.06 MeV. Dla mas, które emitują istotną część hadronów po T ≈ 0.078 MeV (najcięższe w skanie), kod pomija część efektu w kierunku niedoszacowania. Ten wniosek dotyczy tylko modelu: przy tak późnej emisji ważą też procesy, których żadne ramię nie zawiera (hadrodysocjacja, E4).
3. **Stan po wymrożeniu.** X_code < X_net (0.125 vs 0.145 przy 0.105 MeV). Offset bazowy Y_C (−0.0021) powstaje mimo to, a odwzorowanie 2X/(1−X) częściowo go kompensuje. To spójne z rozbieżnością 2X vs 2X/(1−X), której pierwszeństwo należy do AUD1/PRF11/Mech-S8.

**Znaczenie dla B1.**
- Liczby T2 (+0.27…+0.30 dex) i rekast LBT są w jednostkach Y_C. Ten pomiar pokazuje, że **nie istnieje jeden stały czynnik przeniesienia**.
- Fizyczne odczytanie wymaga splotu ΔY_net ≈ ∫ G_net(t)·s(t) dt z natywnym źródłem konwersji s(t), które trzeba wyznaczyć z dynamiki hadronów Wu–Xu.
- Dla j22 dominująca epoka (≥ 1.2 MeV) leży poza obszarem, gdzie R jest dziś wyznaczone.

**Granica PBH: brak.**

## 6. Następny krok (propozycja, wymaga decyzji Moderatora)

PREREG_079 (splot), w trzech częściach:
- **(a)** Natywne s(t) dla j22 i j62 przy β progowym (orig i E5) z kodu autorów z dumpem gęstości hadronów. Wymaga przebiegów Julii.
- **(b)** Ramię CODE z ciaśniejszą tolerancją dla T_p ≥ 1.2 MeV, żeby wyznaczyć G tam, gdzie dziś dominuje szum.
- **(c)** Porównanie ∫ G_code·s z natywnym ΔY_C. To walidacja liniowości splotu, zanim użyje się ∫ G_net·s.

Bez tych kroków żadna komórka nie powinna przeliczać T2 na fizyczne Y_p.

## 7. Audyt (wymagany, zewnętrzny)

- **REC13:** I1 danych i analizy, czyli bramki, zbiór rdzeniowy, R i DEV-1. Najlepiej niezależnym przeliczeniem z `data/`.
- **PRF14** (lub inna komórka spoza rodziny Claude z runtime): odtworzenie G_net przy T_p ∈ {0.45, 0.18, 0.105} MeV **innym kodem sieci** (LINX lub AlterBBN), tym samym kickiem i η = 6.1e-10. To test, czy wynik nie jest artefaktem PRyMordial.

Audyt Claude nad Claude nie jest zewnętrzny. Do czasu I1 status pozostaje [▷].

## 8. Proweniencja

- **Kod:** `code/` z SHA-256 jak w PREREG_077 §2 (zweryfikowane 8/8 przed startem). Dodatkowo:
  - `code_gain_077_dev1.jl` (DEV-1);
  - `smoke_default_077.py` (smoke test z §7 preregu).
- **Dane:** `data/` oraz `MANIFEST_SHA256_077.md`.
- **Logi błędów:** obcięte do 4 kB, SHA pełnych logów w `data/full_failure_logs_sha256.log`.
- **Źródła:**
  - PRyMordial @725d8a8 (GPLv3, nie redystrybuowany);
  - Wu–Xu d395183 (`main-scan.jl` blob b368ba55).
- **Środowisko:** Julia 1.12.3, DiffEq 7.17.0, ArbNumerics 1.6.3, BITS = 100; Python 3, NumPy 2.1.3, SciPy 1.14.1, numba 0.68.1.
