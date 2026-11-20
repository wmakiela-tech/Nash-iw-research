---
artifact_id: IW_BADACZ_B1_RESPONSE_GAIN_PREREG_077_20261120
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel natywny B1 (współwłaściciel), autor propozycji
created_at: 2026-11-20
document_type: PREREGISTRATION (zamrożona przed jakimkolwiek przebiegiem pomiarowym)
authorization: Moderator 20 XI 14:50 „autoryzuję przygotowanie preregistracji” — dotyczy PRZYGOTOWANIA. Uruchomienie wymaga osobnej zgody Moderatora (wpis w RUNLOG).
proposal_source: SYNTH_076 §4.2 (Nash-iw-research@0d3e410)
firstness: rozbieżność paper-vs-code 2X vs 2X/(1−X): AUD1/PRF11/Mech-S8. Niezidentyfikowane wzmocnienie k: INT10 ROT007, PRF14 ROT006, KN15 ROT004, AUD3 ROT004, LT9 ROT007. Ten prereg niczego z tego nie przejmuje; mierzy brakującą wielkość.
claim_ceiling: NUMERYCZNY (kontrolowany pomiar odpowiedzi liniowej) / NO_PBH_BOUND / NO_PAPER_ERROR / NO_NOVELTY (funkcja odpowiedzi BBN to dojrzałe narzędzie) / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_077: wzmocnienie odpowiedzi helu na zaburzenie frakcji neutronów — kod Wu–Xu kontra pełna sieć BBN

## 0. Pytanie i znaczenie

Każde fizyczne odczytanie wyników B1 blokuje dziś niezidentyfikowane odwzorowanie obserwabli kodu na fizyczne Y_p. Dotyczy to T2 (+0.27…+0.30 dex), rekastu LBT 2026 (LT9 ROT007) oraz Q-A.

W kodzie autorów Y_C = 2X/(1−X) przy T_nuc = 0.0782 MeV, a baza wynosi 0.2447. Pełna sieć SBBN daje 0.2467–0.2472. Różnica bazowa jest znana; nieznane pozostaje **wzmocnienie**, czyli o ile zmienia się hel na jednostkę zaburzenia neutronów.

Pytanie pomiarowe: **jak końcowy hel odpowiada na natychmiastowy transfer frakcji barionów p↔n przy temperaturze T_p?** Odpowiedź mierzę w kodzie Wu–Xu i w publicznym kodzie z pełną siecią, a potem porównuję oba wzmocnienia w funkcji T_p.

Znaczenie dla decyzji:
- Jeśli R jest stałe, różnice Y_C przenoszą się na fizyczne Y_p jednym czynnikiem.
- Jeśli R zależy od T_p, przeniesienie wymaga splotu z historią źródła. To byłby osobny, następny prereg.

## 1. Definicje (definicja przed liczbą)

- **Kick (fluencja A, ułamek przeniesiony w chwili t_k):**
  - sign = +1 (p→n): Y_n += A·Y_p, Y_p −= A·Y_p;
  - sign = −1 (n→p): Y_p += A·Y_n, Y_n −= A·Y_n.
  - Liczba barionów jest zachowana. t_k = t(T_p) według **własnej** relacji t(T) każdego kodu.
- **T_p:**
  - w NET jest to temperatura fotonów T_γ (interpolator t_of_T PRyMordial);
  - w CODE jest to T_SM = from_ρ_to_T(ρ_SM), dokładnie jak w `evolution_system!` autorów (jedna temperatura plazmy SM).
  - Różnica definicji jest strukturalna i wchodzi do porównania jawnie, nie jest korygowana.
- **NET:** PRyMordial (vallima/PRyMordial @725d8a8, `PRyM_main.py` SHA-256 98f0724f…). Ustawienia:
  - mała sieć 12 reakcji (przeznaczona do Y_p i D/H);
  - domyślne flagi poza: η₀ = 6.1e-10 (dopasowane do η_B Wu–Xu), verbose off, julia off;
  - τ_n = 878.4 s (identyczne z Wu–Xu).
  - Y := YP_BBN (res[4], 4·Y_He4).
- **CODE:** zamrożony kod autorów (d395183, `main-scan.jl` blob b368ba55), masa j22, β = 1e-30 (PBH praktycznie wyłączone; ten sam wiersz co qa_A).
  - Y := (last ∘ magic), tj. 2X/(1−X) przy T_nuc.
  - Kick realizuje `ContinuousCallback` na T_SM(u) − T_p, z affect! na u[4] = log X.
- **Wzmocnienia:**
  - G_net(T_p) = (Y₊ − Y₋) / (A·(Y_n + Y_p)_przed kickiem). Przy zachowaniu barionów i linii wzmocnienie nie zależy od X(t_k).
  - G_code(T_p) = (Y₊ − Y₋) / A, bo X + (1−X) = 1.
  - **R(T_p) = G_code / G_net**, tylko tam, gdzie |G_net| ≥ 0.05.
- **Linia bazowa:** offset Y0_code − Y0_net jest raportowany i nie wchodzi do R.

## 2. Zamrożony kod (`research/badacz/2026-11-20/code/`)

| plik | SHA-256 |
|---|---|
| `prym_kick_patch_077.py` | 7d9e5f07146b73b25c923d17e310fffd0065fc2cb92cdc8b500dc06ce8d571fa |
| `net_gain_077.py` | b38e2a0c92f6d613620b2d63fd754dcd6e899e5d46737d8d3610f6bf56bec051 |
| `run_net_077.py` | 8f1ecbfcb6ef2128c4c3eda7abc4fb319bdc6c14c3a2fba2c84c95a0640001c5 |
| `code_gain_077.jl` | 63ff1866cf630ad6307485843ecd8aacc4594a934721b3364d9e756740fbc9a9 |
| `analysis_077.py` | f5f56e9490a48d4adeed7238cbd662fc1ae9ebe1ee3508b7e3053d59360565fe |
| `run077.sh` | d75a3b70ffd839a789ebe496dda55a09d26f83d9702667e64cb4f8937ec7e9b7 |
| `cfg077_code_default.dat` | 943e11ab1f2ba3e05899758f8607a229d3c9d9a3e290afe1e720a6f4f36d86a9 |
| `cfg077_code_1e-4.dat` | 15b3753bd3431451b98768178dfff4da71823a682c8e60799814cfe33675d682 |

**Łatka PRyMordial.** Skrypt sprawdza SHA źródła i kopiuje repo do katalogu roboczego (PRyM czyta tablice z cwd). Potem:
- dodaje helper `_iw077_solve`;
- wystawia interpolator t_of_T;
- kieruje pięć wywołań `solve_ivp` sieci n/p przez helper: HT, MT ×2, LT ×2.

Bez kicku i przy tol_scale = 1 helper woła `solve_ivp` z oryginalnymi argumentami. SHA wyniku łatki: cd607965eb71…6fd0.

**Licencja.** PRyMordial jest na GPLv3. Nie redystrybuuję go: publikuję wyłącznie skrypt łatki.

## 3. Plan przebiegów (zamrożony)

- **Siatka T_p [MeV], 18 punktów:** 3.0, 2.0, 1.5, 1.2, 0.8, 0.6, 0.45, 0.35, 0.25, 0.18, 0.13, 0.105, 0.095, 0.088, 0.082, 0.075, 0.068, 0.06.
  - Granice er PRyMordial (1.0 i 0.1 MeV) są celowo omijane.
  - Zbiór rdzeniowy C (do etykiet): 2.0 … 0.105 (11 punktów).
  - Punkty 0.095–0.06 są opisowe: tam wypada odczyt T_nuc kodu.
- **Fluencje:** A = 2e-3 (główna) i 1e-3 (liniowość), oba znaki, w obu ramionach.
- **NET, 87 przebiegów:**
  - baza oraz baza w dużej sieci;
  - 18 × 2 A × 2 znaki;
  - kontrola tolerancji (rtol, atol × 1e-2) przy T_p ∈ {1.5, 0.45, 0.18, 0.105}, plus baza;
  - kontrola dużej sieci (63 reakcje) przy T_p ∈ {0.45, 0.13}.
  - Każdy przebieg w świeżym podprocesie, 2 równoległe.
- **CODE, 110 przebiegów Julii:**
  - tol domyślna: baza + 18 × 2 A × 2 znaki = 73;
  - tol 1e-4 (reltol = 1e-4, abstol = 1e-7, jak A3/T2): baza + 18 × 2 znaki (A = 2e-3) = 37.
  - Dwa procesy równolegle.
- **Szacowany czas:**
  - NET ≈ 5–10 min;
  - CODE ≈ 30 min (≈ 30 s na wywołanie, jak w qa_A) plus ewentualna kompilacja.
  - Koszt wyłącznie CPU w tym kontenerze.

## 4. Bramki (zamrożone)

- **V0_NET_BASELINE:** Y0_net ∈ [0.2460, 0.2480].
- **V2_KICK_APPLIED:**
  - każdy przebieg z kickiem zastosował go dokładnie raz;
  - stan przed kickiem jest identyczny w parze ± (|Δ| ≤ 1e-12).
- **V3_CODE_ZERO:** baza CODE (callback = nothing) odtwarza natywny wiersz qa_A (j22, log10β = −30) Y = 0.24474916002311889 z |Δ| ≤ 1e-15.
- **V4_LIN:** |G(A = 1e-3) / G(A = 2e-3) − 1| ≤ 0.03 w każdym ramieniu przy każdym T_p, gdzie |G| ≥ 0.05.
- **V5_TOL:**
  - NET: |G(tol × 1e-2) / G − 1| ≤ 0.01;
  - CODE: |G(1e-4) / G(default) − 1| ≤ 0.03 (tam, gdzie |G| ≥ 0.05).
- T_p, które nie przejdą V2, V4 lub V5, wypadają ze zbioru rdzeniowego; raportuję je.
- Niepowodzenie V0 lub V3 blokuje etykietę (`GATE_FAIL_NO_LABEL`).

## 5. Etykiety i znaczenie decyzyjne (zamrożone)

Na zbiorze rdzeniowym po bramkach:

| etykieta | warunek | znaczenie |
|---|---|---|
| `GAIN_MATCH` | wszystkie \|R − 1\| ≤ 0.05 | wzmocnienie kodu zgodne z siecią; zostaje sam offset bazowy |
| `GAIN_CONSTANT_OFFSET` | nie MATCH i max R / min R ≤ 1.05 | ΔY_net ≈ ΔY_code / r, r = mediana R (dla małych zaburzeń w zakresie rdzenia) |
| `GAIN_T_DEPENDENT` | pozostałe | przeniesienie wymaga splotu ΔY_net = ∫ G_net(t)·s(t) dt z natywnym źródłem s(t); następny prereg, nie ten |
| `INSUFFICIENT` | mniej niż 5 punktów rdzeniowych | brak etykiety |

**Żadna etykieta nie jest granicą PBH.** `GAIN_CONSTANT_OFFSET` daje tylko czynnik przeniesienia dla odpowiedzi liniowej.

## 6. Predykcje Badacza [▷] (zamrożone; ich porażka nie unieważnia pomiaru)

- **P1 (mechanizm):** R(0.25), R(0.18), R(0.13) leżą każde w [1.10, 1.45].
  - Hipoteza: po wymrożeniu oddziaływań słabych różnicę dominuje odwzorowanie 2X/(1−X), czyli czynnik 1/(1−X_nuc)² ≈ 1.26 przy X_nuc ≈ 0.109.
- **P2:** wczesne kicki są wymazywane przez równowagę słabą. |G(3.0)| < 0.1·|G(0.25)| w obu ramionach.
- **P3:**
  - G_code przy T_p ∈ {0.075, 0.068, 0.06} ma |G| < 1e-3, bo kick wypada po odczycie T_nuc kodu;
  - G_net(0.075) > 0.5, bo sieć nadal przerabia późne neutrony.

## 7. Ujawnienie przed zamrożeniem

Przed zamrożeniem wykonałem dwa przebiegi PRyMordial, oba **bez zaburzenia**:
1. Smoke test instalacji z domyślnymi ustawieniami (η₀ = 6.10459e-10): YP_BBN = 0.2468816718011093, N_eff = 3.04439, około 8 s.
2. Ten sam przebieg na kopii po łatce, bez kicku: wynik bitowo identyczny, 0.2468816718011093. To potwierdza neutralność łatki.

Ponadto:
- Żaden przebieg z kickiem nie został wykonany.
- Żadnego przebiegu Julii nie wykonałem. Driver `code_gain_077.jl` jest nieprzetestowany.
- Błąd techniczny drivera przed uzyskaniem danych (składnia, API callbacku) poprawiam jako odnotowane odchylenie, bez oglądania wyników. Zmiana definicji, siatki lub bramek wymaga nowego prereg.

## 8. Granice

- Odpowiedź liniowa na idealizowany kick na tle SBBN. Nie obejmuje:
  - zmiany ekspansji ani entropii od PBH (przy β ~ 1e-18 rzędu 1e-4 względnie);
  - fotodysocjacji ani hadrodysocjacji;
  - historii źródła.
- Jedna sieć (PRyMordial, mała sieć) z kontrolą dużej sieci w dwóch punktach. Zależność od kompilacji szybkości reakcji jądrowych nie jest badana.
- Różnice strukturalne kodów są częścią mierzonego G, a nie korektą. Należą do nich:
  - jedna temperatura plazmy SM w kodzie;
  - stałe η_B przed anihilacją e±;
  - przybliżone szybkości słabe 255/τ_n·(12 + 6x + x²)/x⁵.
- To pomiar w modelu; sufit NO_PBH_BOUND / NO_PAPER_ERROR.

## 9. Audyt i niezależność

Jestem autorem propozycji, więc audyt Claude nad Claude nie jest zewnętrzny. Po przebiegu poproszę o I1 komórkę spoza rodziny Claude (REC13 lub AUD3; opcjonalnie XH-S7). Najcenniejszy test: odtworzyć G_net w 2–3 punktach **innym kodem sieci**, np. LINX (arXiv:2408.14538) lub AlterBBN.

Zapis wyników: dane surowe, analiza (`analysis077.json`), manifest SHA-256 i REVIEW_078 w `research/badacz/2026-11-20/`, z odczytem zwrotnym i zwrotem na #iw-dispatch.
