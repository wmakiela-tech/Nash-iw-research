---
artifact_id: IW_MECH_S8_ROT012_WUXU_E4_C_D_BAND_SOURCE_IDENTIFIABILITY_AND_ONE_SIGMA_RANK_ONE_WITNESS_001_20261110
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_07 / Mech-S8
created_at: 2026-11-10
exposure: PUBLIC
document_type: BOUNDED_SOURCE_TYPED_LINEAR_ALGEBRA_FALSIFIER
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: REVIEW050_MODEL_INTERNAL_FINITE_RESPONSE_SECANTS / NO_PHYSICAL_SOURCE_VALIDATION / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
---

# ROT012 — Niepewna rozdzielność źródłowych pasm C/D z natywnego jądra odpowiedzi REVIEW050

## Cel i firstness

Źródło fizyczne: Wu–Xu, *Primordial Black Holes Evaporating before Big Bang Nucleosynthesis*, JCAP 02 (2026) 063, DOI 10.1088/1475-7516/2026/02/063. Oryginalny kod autorów, publiczny Git commit `d395183674cace6c9906a8911bdeb7234ba4040d`, to snapshot v2 (Mech-S8 ROT007). 

Pierwszeństwo odpowiedzi w paśmie: **BADACZ REVIEW050 FIRST** (2026-11-08) wykonał prerejestrowany natywny eksperyment w kodzie autorów. Badacz opisał `s_eff` (udział w wpływie na kontur) wobec `s_num` (udział liczby hadronów), wykazując, że późne pasma C+D są nadreprezentowane względem zliczania hadronów. Obecny ROT012 NIE powtarza uruchomień Julia ani nie przypisuje sobie odkrycia czasowego jądra; wyprowadza ograniczenie **odwracania** wyników Badacza. Dane: [publiczny REVIEW050](https://github.com/wmakiela-tech/Nash-iw-research/blob/11eeb1c37c21f19b2510e3bba5ae50169cbd5d79/research/badacz/2026-11-08/IW_BADACZ_WUXU_BAND_RESOLVED_HADRON_RESPONSE_KERNEL_REVIEW_050_20261108.md), `research/badacz/2026-11-08/data/kernel_analysis.json` (Git blob SHA-1 `1df29aff025755f9042628ec85752178b991d398`). Cztery dosłowne `Infinity` w tym pliku to osobny, znany problem zgodności ze ścisłym JSON (Mech-S8 ROT010), **nie** są polami użytymi tutaj.

## Zakres źródła i matematyka

- Pasmo C: `1.06e8 ≤ M_PBH < 3e8` g. Pasmo D: `M_PBH < 1.06e8` g; `T_H ≳ 100 TeV`.
- Wektor wierszy: cztery różne początkowe masy skanu `j=[22,28,34,62]`.
- Kolumny `S_{jb}`: oryginalne REVIEW050 `derived[j][b].s_eff` dla `[A2,B2,C2,Dc]`, gdzie `Dc` jest opublikowanym po fakcie połączonym oszacowaniem `D0/D2`. `se_s_eff` to przybliżone odchylenia z 7-punktowego DOPASOWANIA linii `Y_C(log10 β)`. **NIE** są eksperymentalnymi przedziałami niepewności, certyfikowanymi granicami ODE ani oszacowaniami błędu modeli fizycznych.
- Przedłożona macierz `S` jest zbiorem **skończonych przyrostów** modelu, nie niezależnie zmierzonym dokładnym Jakobianem. Przy wspólnych perturbacjach może być nieliniowa; nawet udana reguła sumy REVIEW050 z tolerancją ±0.1 nie stanowi dowodu dokładnej superpozycji.

Cztery wiersze macierzy `S` z oryginalnego JSON (A,B,C,D), zaokrąglone dla czytelności:

| j | A | B | C | D = Dc |
|---:|---:|---:|---:|---:|
| 22 | 0.00660792 | 0.56606367 | 0.33149064 | 0.07657119 |
| 28 | 0.01889818 | 0.79250957 | 0.14403435 | 0.02417064 |
| 34 | 0.24335163 | 0.61523396 | 0.07222330 | 0.01585492 |
| 62 | 0.87498656 | 0.10057549 | 0.00982339 | 0.00144864 |

Niezależna algebra liniowa: singular values pełnego 4×4 `S`: `[1.2359945178495721, 0.856702462747416, 0.20820004049988083, 0.005170393794909517]`; jego `κ_2=239.05229792486287`. Dla 3×2 podmacierzy (C,D), wiersze `j=22,28,34`, singular values `[0.3774658456204855, 0.008150150633078149]`, `κ_2=46.31397168151777`, a znormalizowany iloczyn kolumn `0.9947863365126043`. Dla 4×2 C,D `κ_2=46.15746901811617`. Wyniki obliczono niezależnie w Wolfram Language/SVD i NumPy.

**Elementarna konsekwencja:** wartości osobliwe świadczą o **słabym uwarunkowaniu** dopasowania dwóch mnożników źródła C i D na podstawie odpowiedzi konturów, pomimo nominalnego pełnego rzędu. Nie jest to twierdzenie o prawdziwym modelu poza domeną empiryczną REVIEW050.

## Nowy falsyfikator: wprost podany kontrprzykład dokładnego rzędu 1

Dla czterech punktów `j=[22,28,34,62]`, zachowując publikowane kolumny `C,D=Dc`, zdefiniuj:

```
C  = [0.33149064037701215, 0.14403434880811905, 0.07222330213977268, 0.009823386811443235]
D  = [0.07657119271096934, 0.02417064203027118, 0.015854917529929135, 0.001448640475406825]
C' = C + [0.002, 0, 0, 0]
D' = C'/5
```

**Tożsamość algebraiczna:** kolumny `[C',D']` mają RZĄD 1, ponieważ `D'=0.2 C'` dla każdej pozycji. Odniesione do udokumentowanych `se_s_eff` wartości największe bezwzględne **indywidualnych** odchyleń wynoszą:

- `max_i |C'_i-C_i|/SE(C_i) = 0.10341905`;
- `max_i |D'_i-D_i|/SE(D_i) = 0.983375395`;
- wszystkie **osiem** zmian jest w granicach jednej **nominalnej** jednostki błędu dopasowania na każdą pozycję.

**Kluczowa kontrola bez pooling:** w miejsce opublikowanego `Dc` użyj oryginalnych *bezpośrednich* `D2` z REVIEW050 (`[0.07774904762365242, 0.027007298992924644, 0.013659990316174264, -0.0013523344406164428]`) oraz ich odpowiednich `se_s_eff`. Dokładnie ten sam `C'` i `D'=C'/5` daje `max_i |D'_i-D2_i|/SE(D2_i) = 0.725020008`. Przykład działa także **bez** łączenia `D0/D2`; dla bezpośredniego 4×2 (C,D2) `κ_2=50.63066014369092`.

Jest to matematyczny **istnieje-perturbacja** falsyfikator tezy, że na podstawie odczytanych wartości i raportowanych `SE` da się zagwarantować stabilną separację C/D. Nie oznacza, że prawdziwa macierz jest rzędu 1 ani że `SE` mają empiryczne pokrycie; jest to test odporności na *zadany numeryczny budżet*, nie dowód statystyczny.

## Lokalny prawie-niewidoczny kontrast źródeł

W liniowej aproksymacji `δ log10β_j ≈ −Σ_b S_jb δf_b/ln(10)` wystarczy ustawić `δf_C = −0.2309905119006772 δf_D`, aby dokładnie skasować odpowiedź modelu w wierszu `j=22`. Dla `δf_D=0.1` (a więc małej perturbacji) przewidziane przesunięcia **surrogatu**, nie wykonanej wspólnej symulacji Julia, to w przybliżeniu `[0, +0.0003952, +0.00003596, +0.00003563] dex` dla `j=[22,28,34,62]`. Te wielkości są małe względem typowych rozrzutów punktów dopasowania REVIEW050. Nie ekstrapolować tego wzoru do dowolnie dużych korekt ani nie stwierdzać fizycznej degeneracji.

## Dlaczego to materialne dla E4

Wcześniejsze liczenie udziałów liczby hadronów (Mech-S8 ROT006) nie uwzględniało jądra czasu; REVIEW050 (Badacz FIRST) wykazał 40.8% efektu C+D wobec 9.3% liczby przy j22. ROT012 dodaje, że nawet znając samą odpowiedź na każdy z dwóch pasm, próba **osobnego kalibrowania** niepewnych praw emisji dla C i D wyłącznie z tych konturów jest słabo uwarunkowana; nominalna rangowość nie oznacza certyfikowalnej rozdzielności. Walidacja zewnętrznego źródła hadronów powinna więc dostarczyć **niezależnych informacji spektralnych** w punktach `M≈1e9, 3e8, 1e8 g` i odpowiednich progach energii, a nie opierać się na odwracaniu kilku globalnych granic BBN.

**Zadanie falsyfikacyjne, bez automatycznej kaskady:** bezpośrednio zwalidować wysokotemperaturowe widma fragmentacji/pasmo energii oraz przynajmniej jedną wspólną perturbację C/D w natywnym kodzie Wu–Xu, jeśli źródło i zasoby będą dostępne. Warunki brzegowe: E4 nadal `SOURCE_BLOCK`; `Mech-S7 ROT035` strict epsilonODE nadal `OPEN`; historyczny producer JCAP Fig5 `OPEN`. `NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN`.

## Reprodukcja

Włączony skrypt 
`mech_s8_rot012_band_C_D_identifiability.py` (NumPy) zawiera pełną maszynową macierz i raportowane `se_s_eff`, oblicza SVD, konstrukcję rzędu 1, odchylenia w jednostkach SE, kontrolę alternatywy `D2` i przewidywania lokalnego surrogatu. Wynik: `ROT012_response_rank_certificate.json` (strict JSON, zero NaN/Infinity). Lokalny clean replay PASS; niezależna kontrola SVD Wolfram PASS. Publiczne repozytorium przechowuje raport i odrębny reproduktor; zapis + readback GitHub należy sprawdzić oddzielnie. Kod nie odpala solvera Julia ani nie odczytuje prywatnych danych.