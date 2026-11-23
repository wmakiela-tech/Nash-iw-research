---
artifact_id: IW_BADACZ_B1_NOPBH_BACKGROUND_AND_GEC_PREREG_119_20261123
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel przebiegów natywnych B1
created_at: 2026-11-23
document_type: PREREGISTRATION (zamrożona przed przebiegami)
authorization: Moderator 23 XI 09:22 („Najpierw A”); stała autoryzacja przebiegów 21 XI 16:05
answers: DAX-S10 ROT003–005, AUD3 ROT025–026, REC14 ROT006–007 (tło bez PBH); EKS1 ROT024–027, REC14 ROT002 (G_EC / G_EC+)
claim_ceiling: NUMERYCZNY w modelu kodu Wu–Xu [▷] / NO_PBH_BOUND / NO_AUTHOR_ERROR_ESTABLISHED / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_119: natywne tło bez PBH w kodzie Wu–Xu oraz bramka G_EC+(a) (normalizacja utraty masy)

## 1. Cel

**Część A: tło bez PBH.** Komórki GPT ustaliły na poziomie źródła i w modelach zredukowanych (bez natywnego kodu):
- tło w `main-scan.jl` (d395183, blob b368ba55, l. 85) ewoluuje według d ln ρ/d ln a = −4 + R′/(3+S′), a nie według postaci adiabatycznej −3(4+R′)/(3+S′), którą implikuje równanie 2.7 artykułu (a³g_sT³ = const);
- skutkiem jest formalny stosunek entropii współporuszającej 1.14678 między 10 MeV a T_nuc i stosunek czasów 1.02922 (DAX ROT002–003, I1: AUD3 ROT025–026);
- przy stałym T_nuc ΔY = Y_ad − Y_code = +0.0030704, a Y_code = 0.244893 w modelu zredukowanym (DAX ROT004, I1: REC14 ROT007).

Prośba: natywny przebieg kodu z nPBH = 0 i eksportem a, t, ρ, T, X_n oraz Q = a³g_sT³ w wybranych temperaturach. Ten PREREG wykonuje ją i testuje powyższe liczby natywnie.

**Część B: G_EC+(a).** Według EKS1 kod traci masę ok. 1.7× szybciej niż standard (τ = 407 s·(M/1e10 g)³). Moje tau_check_118 daje na natywnych zrzutach stosunek 1.709. Jeśli BlackHawk, z którego zbudowano tablice hadronowe, ma standardową normalizację, kod łączy szybkości hadronowe zgodne ze standardową emisją z szybszą utratą masy. Według REC14 ROT002 porównanie mocy w dwóch masach nie wystarcza (G_EC+). Tutaj sprawdzam:
- stosunek R(M) = f_BH(M)/f_code(M) na całej trajektorii masy, gdzie f_BH to współczynnik Page z BlackHawk v2.3 (`fM.txt`, a = 0, GeV⁴, dM/dt = −f/M²), a f_code = N_BH(T_BH)·m_Pl⁴ z definicji autorów (`tool_script-parameters.jl` l. 104–105, `main-scan.jl` l. 80);
- spójność energii widm pierwotnych 090 (wejście tablic hadronowych) z `fM.txt`.

Część (b) G_EC+, czyli budżet energii samej tablicy hadronowej, oraz STD_A nie wchodzą do tego PREREG.

## 2. Ujawnienie wiedzy przed zamrożeniem

- Nagłówek `fM.txt`: f(M_Pl) = 9.48e73 GeV⁴. Na atrapie sprawdziłem, że f ≈ 9.5e73 daje τ(1.121e9 g) ≈ 0.995 × 407·M₁₀³ s. Strona BlackHawk w P_G1 nie jest więc testem ślepym, a tau_check_118 (1.709) przesądza też stronę kodu przy dwóch masach. Nowe w P_G1 jest zachowanie R(M) w całym oknie 1 g – 1e10 g.
- Natywne Y przy β = 1e-30 z wcześniejszych przebiegów (085–094, solwer autorów) mieści się w 0.24465–0.24479.
- Pilot: przebiegi „timing_only” (code/def/j22, ad/r8/j22, ad/r9/j22) wypisały tylko czas, liczbę kroków i retcode (37.8 s / 168 kroków, 69.4 s / 7064, 102.1 s / 15165; wszystkie Success). Test dymny eksportu (code/def/j50) i trybu fcode sprawdził wyłącznie kształt i skończoność plików; pliki usunięto bez odczytu wartości.

## 3. Ramiona (`code/bg_export_119.jl`, `code/run119.sh`)

Każde ramię: β = 0 dokładnie (n_PBH = 0), kopia nietkniętego drzewa autorów (blob b368ba55 sprawdzany), łaty tekstowe stosowane dokładnie raz albo przerwanie.

| ramię | zmiana wobec kodu autorów | rola |
|---|---|---|
| code | brak (poza zwrotem obiektu rozwiązania, jak w 081) | natywne tło kodu |
| ad | l. 85: −4 + R′/(3+S′) → −3(4+R′)/(3+S′) | KONTRFAKTYCZNE tło adiabatyczne (r. 2.7) |
| solwer def | wywołanie `solve` autorów bez zmian | to, czego użył skan |
| solwer r8 / r9 | ten sam algorytm, reltol 1e-8 / 1e-9, abstol 1e-10 / 1e-11 | precyzja numeryczna, bez zmiany fizyki |
| start j22 / j62 | masa początkowa 1.121e9 / 3.494e9 g; przy β = 0 wpływa tylko na chwilę startu | replika |

Razem 12 przebiegów natywnych oraz tryb `fcode`: f_code na 1000 masach siatki `fM.txt`.

**Eksport.** Wartości w T_SM = 10, 1, 0.5, 0.25, 0.1 MeV i T_nuc = 0.0781853 MeV: η = ln a (a_f = 1), t [s], ρ [GeV⁴], T [MeV], X_n, N_s, N_ρ, Q = a³N_sT³. T_SM pochodzi z `from_ρ_to_T` autorów, a pozycję wyznacza bisekcja po η na gęstym rozwiązaniu. Do tego 3000 punktów gęstych dla T ≤ 30 MeV i Y według wzoru autorów (l. 206–211). Kod ma jedną temperaturę, więc T_ν nie istnieje i nie jest eksportowane (prośba AUD3 częściowo bezprzedmiotowa).

## 4. Bramki i predykcje (`code/analysis_119.py`, progi zamrożone w skrypcie)

Tolerancje Y nie są niższe od udokumentowanego rozrzutu natywnego Y (rozstęp 1.4e-4 przy β = 1e-30, solwer def).

**Bramki:**
- G_RUN: 12/12 przebiegów z retcode Success, wszystkie pliki obecne.
- G_AD (test łaty): |Q(T_nuc)/Q(10 MeV) − 1| ≤ 0.002 w ad/r9, obie repliki.
- G_CONV: |Y_r8 − Y_r9| ≤ 2e-5 dla code i ad, obie repliki. Przy FAIL wyniki r9 oznaczam jako ograniczone szumem.
- G_REP: |Y_r9(j22) − Y_r9(j62)| ≤ 2e-5 dla code i ad.
- P_G3 (ekstrakcja po stronie kodu): τ z f_code, ∫M²/f dM, zgodne z τ z natywnych zrzutów (tau_check_118) do 0.5%.

**Predykcje (PASS wymaga obu replik):**

| id | wielkość | odniesienie (źródło) | tolerancja |
|---|---|---|---|
| P0 | Y_code, r9 | 0.244893 (REC14 ROT007, model zredukowany) | ±2e-4 |
| P0d | Y_code, def | 0.24473 (moje przebiegi β = 1e-30) | ±2e-4 |
| P1 | Q(T_nuc)/Q(10 MeV), code r9 | 1.146782 (DAX ROT003, AUD3 ROT025) | ±0.002 |
| P2 | Δt(10 MeV → T_nuc), code/ad, r9 | 1.029223 (DAX ROT003, AUD3 ROT026) | ±0.002 |
| P3 | Y_ad − Y_code, r9 | +0.0030704 (DAX ROT004, REC14 ROT007) | ±2e-4 |
| P_G1 | R(M) = f_BH/f_code dla 1 g ≤ M ≤ 1e10 g | standard / kod ≈ 1/1.709 (EKS1 ROT025, tau_check_118) | cały zakres w [0.55, 0.62] |
| P_G2 | P_spec/P_fM dla mas 090 w [2e9, 1e11] g | 1 (spójność energii BlackHawk) | ±0.03 |

P_spec = Σ_kanały ∫E·dN/dEdt dE (trapez w ln E na siatce 090: 5–1e5 GeV, 100 punktów, 16 kanałów z grawitonem, normalizacja Dirac: 1 BH/cm³). P_fM = f_BH/M²/ħ. Okno mas wybrałem tak, by obcięcie siatki energii przy obu końcach było małe; udziały brzegowe E²Φ są raportowane.

## 5. Interpretacja (ustalona przed przebiegiem)

- P1 i P2 PASS: natywny kod odtwarza dryf entropii i zegara znaleziony na poziomie źródła. To nadal nie jest teza o błędzie granicy autorów, bo T_nuc jest kalibrowane (alias kalibracji: DAX ROT004, REC14 ROT006).
- P3 PASS: ΔY ze zredukowanego modelu potwierdzone natywnie przy stałym T_nuc. FAIL: model zredukowany pomija coś w natywnym (np. interpolację Y autorów albo `from_ρ_to_T`); wtedy raportuję różnicę.
- P0 i P0d: punkt odniesienia SBBN kodu i jego szum solwera. Różnica def − r9 mierzy błąd numeryczny skanu autorów w Y przy β = 0.
- P_G1 PASS: BlackHawk ma normalizację standardową, a kod emituje ~1.7× szybciej w całym oknie trajektorii. Przesłanka EKS1 dla STD_A trzyma się po stronie normalizacji. FAIL: raportuję R(M); STD_A trzeba by normalizować f_BH(M) zamiast 407 s.
- P_G2 PASS: widma, z których zbudowano tablice hadronowe, niosą moc BlackHawk, więc tablice odpowiadają standardowej emisji. FAIL: niespójność wewnątrz BlackHawk albo w moim całkowaniu; wtedy G_EC+ pozostaje otwarta.
- Żadna kombinacja wyników nie daje tu granicy na β ani poprawki do pracy.

## 6. Odtwarzalność

- Wejścia (SHA w `out/inputs_sha.log`): drzewo autorów d395183, `fM.txt` z BlackHawk v2.3 (tarball dd148349… = Artifacts.toml autorów), `primary_spectra_090.tsv.gz` (2026-11-21/data), zrzuty keep115 (f07f7e69…, 51611ae2…).
- Środowisko: Julia 1.12.3, `wuxu_env` jak w 081–116.
- Wyniki: `data/` z SHA w manifeście.
- Analizę sprawdziłem na atrapie (`code/dummy_119.py`; liczby dowolne, tylko formaty); przeszła mechanicznie.
