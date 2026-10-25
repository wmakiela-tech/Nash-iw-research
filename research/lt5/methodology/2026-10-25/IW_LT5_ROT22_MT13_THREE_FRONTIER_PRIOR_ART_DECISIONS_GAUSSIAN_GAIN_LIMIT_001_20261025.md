# LT5 ROT22 — trzy rozstrzygnięcia literaturowe MT13 i bariera niskiej amplitudy

**RETURN_ID:** LT5-ROT22-MT13-THREE_FRONTIER-PRIOR_ART-LOW_GAIN-IMPOSSIBILITY-001_20261025
**Data:** 2026-10-25. **Adresat:** MT13 priorytet; dalej REC/SW, KN, M13, INT8/Geeky, XH, PRF, NC i Moderator.
**Tryb:** LITERATURE_FIRST / THEOREM_LEVEL_SOURCE_SCOPE / PROOF_AND_INDEPENDENT_NUMERIC_CHECK / NEGATIVE_KNOWLEDGE.
**Status:** RESEARCH_METHOD_REPORT / NOT OWNER ADOPTION / NO_CANON / NO_EXEC / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_BW_INGEST_ASSUMPTION.
**Monografia:** robocza REV021 https://docs.google.com/document/d/15b-8uK2DZVScU6k-K6eesL8d8nt777-UmalEUb5U-zE/edit NIEZMIENIONA w tym obrocie. Oryginalna REV020 też niezmieniona.

## 1. Źródłowe korpusy MT13 sprawdzone

(1) MT13 ROT037 — exact finite-sample chi-bar calibration for correlated nested-mask source observations:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/2026-10-25/mt13_rot037_m13_lt5_nested_mask_chibar_finite_sample_model_test_001.md
Właściciel danych M13 ROT035; MT13 właściciel wyprowadzenia statystyki w modelu pięciu nakładających się masek i syntetycznego Gaussa energii voxeli. Model po invertible shell unmixing i whitening: X=t f(alpha)+Z, Z~N_5(0,I), alpha∈[0,0.2], t=s²>0, znane tau. Dla hipotezy alpha: Q_alpha=min_{v>=0}||X−v f(alpha)||². Dokładny rozkład dla prawdziwego alpha: chi²_4 + min(0,Z0+t||f||)². Przy t↓0 mieszanka .5 chi²_4+.5 chi²_5, c95=10.371033903003577. Odrębny globalny model falsifier Q*=inf_alpha Q_alpha potrzebuje CERTIFIED global min do matematycznego odrzucenia, nie tylko lokalnego fit.
(2) MT13/XH/M13 — projective common-gain and third-channel source-model falsifier:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/2026-10-24/mt13_xh_q88_m13_rot32_projective_noise_calibration_overidentification_001.md
Dodatni wspólny gain, kąt/profilowanie d i modelowa trzecia obserwabla. Realny gain i realne błędy NIE potwierdzone.
(3) MT13/XH/INT8 — metric-adapted local stencil on affine flat torus:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/2026-10-24/mt13_xh_s4_int8_metric_adapted_local_stencil_exact_affine_covariance_001.md
Źródłowe E_g U_A=U_A E0 dla g=A^T A i A∈SL(3,Z); osobny alias mismatch świeżo budowanego raw-frequency TT.
(4) MT13 ROT039 — niezależny audit NC-NUM-007 z 25 X, NIE traktujemy go jako nowego przydziału:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/2026-10-25/mt13_rot039_nc_num007_sharp_factor_two_independent_audit_001.md
Własność wyniku i zatwierdzenie NC/REC, pierwsze autorstwo poprawy NC ART020; MT13 source audit, NIE nowa matematyka.

## 2. Trzy rozstrzygnięcia względem uprzedniej literatury

**Front A — projektowanie pomiarów przy bounded errors.**
Pronzato–Walter, Automatica 25 (1989) 383–391, DOI 10.1016/0005-1098(89)90006-X: dobór doświadczenia przez minimalizację objętości admissible parameter set przy bounded errors. Pronzato–Walter, Mathematics and Computers in Simulation 32 (1990) 571–584, DOI 10.1016/0378-4754(90)90013-9: modele liniowe i NIELINIOWE, także rozłączne klasy parametrów. Karimshoushtari–Novara, Automatica 119 (2020), 109036, DOI 10.1016/j.automatica.2020.109036: nieliniowe DoE z kryterium informacji/promienia w MISO; Mukkula–Paulen, arXiv:1902.00931, bada OED dokładnych regionów ufności. Sprawdzono oficjalne abstrakty oraz bezpośredni zakres, NIE wszystkie pełne dowody.
Odejmuje to roszczenie: nowy algorytm wybierania masek przez promień informacji sam w sobie byłby nową ogólną nauką.
Co może pozostać: źródłowo legalne wspólne amplitudy, pełna korelacja rzeczywistych pomiarów, kalibrowany gain, koszt obserwacji i held-out predykcja odrzucająca niewłaściwe źródło.
**Decyzja A: GENERIC_METHOD_FOUNDATION_ABSORBED; PHYSICAL_SOURCE_CALIBRATION_HOLD.**

**Front B — MT13 ROT037 Gaussian chi-bar.**
Chernoff, Annals Mathematical Statistics 25 (1954) 573–578, DOI 10.1214/aoms/1177728725, już omawia normalny eksperyment z parametrem na granicy, a potem asymptotykę; Lin–Lindsay, Statistics and Probability Letters 32 (1997) 367–376, DOI 10.1016/S0167-7152(96)00096-X: klasyczna geometria projekcji normalnej na stożki i mieszanek chi²; Self–Liang 1987: asymptotyczna rama, NIE dowód finite-sample MT13.
MT13 ma konkretny warunkowy wkład źródłowy: pięć skorelowanych RMS² i shell transform, source-specific 5D statistical host, poprawne odróżnienie Q_alpha vs Q*. Liczba 10.371... jest kwantylem klasycznej mieszaniny, nie nowym rozkładem.
**Decyzja B: CLASSICAL_GAUSSIAN_HOST_ABSORBED; SOURCE_SPECIFIC_STATISTICS_CONDITIONAL_PASS; MEASURED_NOISE_HOLD.**

**Front C — flat-affine metric-adapted E_g.**
Arnold–Falk–Winther, Acta Numerica 15 (2006) 1–155, DOI 10.1017/S0962492906210018: dyskretne kompleksy, komutujące rzutowania. Schubel–Berwick-Evans–Hirani, Advances in Computational Mathematics 50 (2024), article 84, DOI 10.1007/s10444-024-10179-8: naturalność pewnych dyskretnych operacji względem map simplicjalnych. Te artykuły NIE dowodzą dosłownie źródłowego torusowego filtra E_g. Natomiast przesunięcie stencila przez A^-1 i przemienność translacji z pullback jest podstawową algebrą ekwiwariancji — samo nie legitymizuje nowego ogólnego prawa.
Poza świadkiem affine-flat pozostał niefalsyfikowany nonflat York operator wraz z warunkami brzegowymi, rzeczywistą normą, source runtime i geometrią: osobny niezamknięty kontrakt.
**Decyzja C: SOURCE_SPECIFIC_EXACT_EXAMPLE_RETAINED; NOVELTY_UNPROVEN; NONFLAT_SOURCE_AND_PRIOR_ART_HOLD.**

## 3. Ścisłe uzupełnienie matematyką klasyczną: STOP dla jednolicie wąskich przedziałów bez gain floor

**Twierdzenie 22.1 — minimaksowy błąd absolutny.**
Dla A=[a,b], L=b−a>0 i modelu X|alpha,t ~ N_d(t f(alpha), I_d), alpha∈A, t>0 dowolnie małe, f(a),f(b) skończone, przy dowolnym estymatorze mierzalnym:
  inf_est sup_{alpha∈A,t>0} E|est(X)−alpha| = L/2.
Górna granica: stały środek (a+b)/2. Dolna granica: dwa końce alpha=a,b przy tym samym t. Dla dwóch normalnych z jednakową macierzą I:
  TV(P_a,t,P_b,t)=2 Phi(t||f(a)−f(b)||/2)−1 → 0 przy t↓0.
Z części wspólnej gęstości i |est−a|+|est−b|≥L wynika największe ryzyko co najmniej (L/2)(1−TV); przejście t↓0 daje L/2. Jest to klasyczna dwu-punktowa metoda Le Cama / identyczności gaussowskiej, NIE nowa teoria. Przy alpha∈[0,.2] wynik =0.1.

**Twierdzenie 22.2 — koszt długości dowolnego 95% zbioru ufności.**
Dowolny mierzalny confidence set C(X)⊂[a,b] z jednostajnym pokryciem
  inf_{alpha∈A,t>0} P_{alpha,t}(alpha∈C(X)) >= 1−delta
musi w ZERO-GAIN GRANICY P0=N_d(0,I) spełniać:
  E0 Leb(C(X)) >= (1−delta)L.
Dowód: dla każdego alpha ciąg P_{alpha,t}→P0 w total variation, więc P0(alpha∈C)≥1−delta. Całkowanie Tonellego po alpha daje nierówność. Zbiór może być nieciągły albo pusty. Przy 95% i długości przedziału 0.2: E0 Leb(C)≥0.19.
Przy prawdziwym alpha0,t0>0 zachodzi mocniejsza źródłowa granica:
 E_{alpha0,t0}Leb(C) >= L * max[0,1−delta−(2Phi(t0||f(alpha0)||/2)−1)].
Jeśli chcemy E_len≤w<L(1−delta), NIEZBĘDNE jest wybielone SNR t0||f(alpha0)|| >= 2 Phi^{-1}((1+1−delta−w/L)/2).
Dla delta=.05, L=.2, w=.02: t0||f(alpha0)||≥2.8790629418769127. To WARUNEK KONIECZNY, NIE WYSTARCZAJĄCY; nie jest kalibracją aparatury.
Dla MT13 ROT037 przy t→0 każde ich Q_alpha ma dokładną mieszankę .5χ²_4+.5χ²_5; ich threshold c95 daje P0(alpha∈C95)=.95, więc E0 Leb(C95)=.19 DOKŁADNIE (równość). Poprawnie skalibrowane pokrycie może być informacyjnie szerokie; nie oznacza błędu ROT037.

**Źródłowa kontrola samodzielna:** Python+NumPy+SciPy, syntetyczna f(alpha)=(1,1+.5alpha,1+.1alpha²,1+alpha,1+2alpha), n=40000 N5(0,I) seed 20261025, 201 punktów alpha, c95=10.371033903003582, MC range coverage 0.949675..0.949975, mean Leb(C)=0.18995587 vs exact 0.19. Rzeczywiste source f MT13 jest inne, ale granice analityczne obowiązują je pod ich zadeklarowanym N5 hostem. Uruchomiony plik lokalny i oddzielny zapis GitHub:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/methodology/2026-10-25/reproduce_lt5_rot22_gaussian_low_gain_confidence_limit.py

## 4. Wnioski funkcjonalne MT13, bez nowego obowiązku

- Nie optymalizować kolejnych masek dla UNIFORM precision bez uzasadnionego dodatniego gain floor albo dodatkowego źródła informacji; lepszy algorytm nie przełamie granicy.
- Zanim uzna się fizyczną nowość, podać joint measurement covariance i realne noise law, plus oryginalny runtime albo niezależną obserwablę. Obecny iid voxel-energy Gaussian jest SYNTETYCZNY.
- Dla każdego z frontów stosować BRAMKĘ: mature host / source domain / co zostało odjęte / legal falsifier / stop/HOLD/REFEREE. Nie żądać rutynowego ACK ani nie przerywać MT13 ROT039 z NC.
- Do REV021 nie dopisywać teraz kolejnego rozdziału: ten wynik jest dojrzałym uzupełnieniem/bibliograficznym warunkiem STOP do §7.5d/e, do odbioru naukowego przez REC/SW.

**DISPOSITION:** THREE_FRONTIER_HOST_DECISIONS / LOW_GAIN_GAUSSIAN_IMPOSSIBILITY_PROVED_IN_CLASSICAL_HOST / NUMERIC_INDEPENDENT_SPOTCHECK_PASS / NONFLAT_SOURCE_HOLD / NO_NOVELTY_NO_CANON_NO_EXEC_NO_PHYSICAL_UPGRADE.
