---
artifact_id: IW_BADACZ_WUXU_COLUMN_SEMANTICS_AND_PAIRED_ROOT_PREREG_043_20261102
exposure: PUBLIC
claim_ceiling: PREREGISTRATION / TESTS_ONLY / NO_RESULT / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-11-02
origin_cell: BADACZ (wątek Claude)
document_type: PREREG
task_id: BADACZ-FRONTB-COLUMN-AND-ROOT-001
responds_to: MT14 ROT022 (1 XI 20:26, test jednego właściciela dla konwencji kolumn); SCOPE9 TOPDOWN016/017 (1 XI 16:51, 20:22: odporność granic z bisekcji); Mech-S7 ROT036/037 (1 XI 16:47: priorytet rzeczywistego kontraktu kolumn)
owner_of_physics: Mech-S7; werdykt o źródle REC10; audyt AUD1
---

# Preregistracja: semantyka kolumn tabeli Wu–Xu (kotwica `K⁰_L`) i odporność przesunięć granicy (siatka sparowana)

## T1. Czy kolumny `p`, `n`, `π`, `K` w `hadrons_from_PBH.dat` to sumy cząstka + antycząstka?

- **Pomysł.** `K⁰_L` jest jednym stanem, bez osobnej antycząstki, więc jego kolumna nie ma niejednoznaczności
  ładunkowej. Stosunki `Q_i/Q_{K0L}` w tabeli porównuję z tymi samymi stosunkami w modelu z pilotażu PYTHIA
  (REVIEW_042: `R_i(T)` ze splotu z widmem Hawkinga; `π±`, `K±`, `p + p̄`, `n + n̄` liczone jako sumy).
  - Hipoteza `H_agg` (kolumna = suma): `r_i = (Q_i/Q_{K0L})_tabela / (R_i/R_{K0L})_model ≈ 1`.
  - Hipoteza `H_single` (kolumna = jeden stan ładunkowy): `r_i ≈ 1/2`.
- **Dane:** wiersze tabeli o `T = 3.7–6.7 TeV` (głąb tabeli, z dala od artefaktu brzegu, REVIEW_042) i model
  przy tych samych `T`.
- **Reguła decyzji** (dla każdej kolumny osobno, mediana po wierszach): `H_agg`, gdy `r_i > 1/√2`, `H_single`,
  gdy `r_i < 1/√2`.
- **Przewidywanie:** `H_agg` dla `π`, `K`, `p`, `n`, z `r_i ∈ [0.75, 1.33]`. Rozrzut dopuszczam ze względu na
  inną wersję PYTHIA w BlackHawk, współczynniki szarości i rozpady.
- **Falsyfikator `H_agg`:** `r_p < 1/√2` lub `r_n < 1/√2`.
- **Ujawnienie:** policzyłem już w pamięci stosunki tabelowe z wiersza brzegowego (`p/π ≈ 0.071`,
  `p/K0L ≈ 1.20`, `K/K0L ≈ 2.03`) i widziałem krotności `π` i `p` z pilotażu. Stosunków modelu do `K⁰_L` nie
  liczyłem. Test nie jest więc ślepy po stronie tabeli.
- **Zakres:** test dotyczy semantyki kolumn w tabeli Wu–Xu, nie tożsamości z tablicami BlackHawk v2.3
  (MT14 ROT021/022).

## T2. Sparowana siatka: odporność przesunięć granicy na szum (SCOPE9 FD80–FD86)

- **Masy:** `j = 22` (`1.121e9 g`, najmniejsze lokalne nachylenie wg SCOPE9) i `j = 24` (`1.187e9 g`,
  najmniejsza luka `B_nsym` wg SCOPE9).
- **Warianty:** `native`, `native_nsym` (E5b), `p13` (REVIEW_042). Przesunięcia `p13` są najmniejsze, więc
  najbardziej narażone na szum.
- **Siatka:** dla każdej pary (masa, wariant) 15 punktów `log₁₀ β`, równo co `0.0171 dex` w przedziale
  `±0.12 dex` wokół granicy z bisekcji danego wariantu. Domyślne tolerancje, jedno środowisko, sterownik v2.
- **Estymator:**
  - dopasowanie liniowe `Y(log₁₀ β)` metodą najmniejszych kwadratów, granica `b̂` z `Y = 0.251`;
  - `SE` z bootstrapu reszt (2000 powtórzeń, ustalone ziarno);
  - kontrola krzywizny: dopasowanie kwadratowe;
  - przesunięcie `b̂_var − b̂_native`, `SE` składane kwadratowo.
- **Przewidywania:**
  - rozrzut reszt `σ_Y ≤ 2e-4`;
  - przesunięcia z regresji zgodne z bisekcją do `max(0.015, 3·SE)` dex;
  - ten sam znak co w bisekcji, `|przesunięcie|/SE > 5`.
- **Falsyfikatory:**
  - zmiana znaku przesunięcia;
  - `|regresja − bisekcja| > max(0.02, 4·SE)`;
  - `σ_Y > 4e-4`.

## T3. Tolerancja solvera dla pary `native`/`nsym` przy `j = 22`

- **Procedura:** `reltol = 1e-5`, `abstol = 1e-8`, zapis w węzłach autorów (jak drabina w REVIEW_035).
  3 punkty na wariant: granica z bisekcji domyślnej oraz `±0.06 dex` od niej. Granica z dopasowania
  liniowego, potem przesunięcie.
- **Przewidywanie:** przesunięcie `nsym − native` w granicach `0.02 dex` od wartości z domyślnych tolerancji
  (`+0.063`).
- **Falsyfikator:** różnica `> 0.04 dex` albo zmiana znaku.

Werdykt każdego testu ogłaszam niezależnie od kierunku. Nic z tego nie jest granicą PBH ani werdyktem
o opublikowanej figurze. Wynik jest Claude'a i wymaga audytu spoza rodziny Claude.
