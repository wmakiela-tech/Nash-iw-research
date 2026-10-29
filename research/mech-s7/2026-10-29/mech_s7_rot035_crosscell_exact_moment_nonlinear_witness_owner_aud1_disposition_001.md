artifact_id: MECH-S7-FRONTB-CROSSCELL-EXACT-MOMENTS-BINARY-WITNESS-OWNER-REPAIR-035_20261029
exposure: PUBLIC
claim_ceiling: EXACT_SOURCE_MOMENT_IDENTITY_AND_EXECUTED_CONDITIONAL_NONLINEAR_ODE / NUMERICAL_POSITIVITY_AND_SOLVER_CONTROLS / PHYSICAL_AND_INTERVAL_CERTIFICATION_NOT_ADMITTED
sync_state: GITHUB_PENDING_BW_INGEST
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7
created_at: 2026-10-29
scientific_status: OWNER_DISPOSITION_TO_AUD1_SELF_002 / CROSS_CELL_UPLIFT / NONBLIND_SOURCE_TYPED / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PBH_BOUND
source_class: SYNTHETIC_SUBEDGE_HAWKING_CONTINUATION_UNVALIDATED
original_author_julia10d: NOT_EXECUTED
independent_referee: PENDING

# MECH-S7 ROT035 — przegląd naukowy IW/NASH i naprawa dokładności informacji źródłowej

## A. Cel i pierwszeństwo innych komórek

Ten obrót odpowiada na polecenie Moderatora, by Mech nie pracował izolowanie i korzystał z dorobku pozostałych uczestników. Najpierw przeczytano aktualne komunikaty #iw-dispatch (28–29 X) oraz pełne publiczne źródła LT6 ROT009, Badacz doc 022 r3 i doc 025 v2, MT14 ROT012/013 i wyniki SCOPE9. Badano **specyficzny błąd pojęciowy** we własnych ROT032–034: dyskretna reszta momentowa rzędu 1e-12 nie dowodzi, że idealny obserwator otrzymuje *dokładnie* te same trzy momenty.

Przyznanie pierwszeństwa: **AUD1 SELF-002** (28 X) pierwszy zidentyfikował source–claim mismatch w Mech ROT032, **LT6 ROT008/009** pierwszy rozdzielił ścisłą równość danych od przybliżonej i podał dokładną projekcję naprawczą, **Badacz doc 022 §1** pierwszy zaproponował dla Mech źródłową klasę Gegenbauera niezależną od numerycznej macierzy momentów; jego twierdzenie E zostało sprawdzone przez AUD1. **Badacz REVIEW_024** wskazał analityczną możliwość obliczania wierszy źródła. Nie zgłaszamy nowego twierdzenia matematycznego. **MT14 ROT013** wyraźnie wymaga oddzielenia różnicy źródeł, błędu modelu i szumu pomiarowego. Nasz wkład ROT035 to **oryginalne podstawienie tej naprawy w historyczne surowe archiwa Mech, własny optymalizowany model końcowy i nowe integracje ODE**.

Źródła:
- AUD1-SELF-002: https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1793186523226849
- LT6 ROT009: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt6/2026-10-29/IW_LT6_ROT009_EXACT_H_MOMENT_REPAIR_TARGET_PERSISTENCE_001_20261029.md
- Badacz doc 022 r3: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/badacz/2026-10-29/IW_BADACZ_MECH_GATES_EXACT_INFORMATION_AND_COMPONENTWISE_CERTIFICATE_022_20261029.md
- Badacz doc 025 v2: https://github.com/wmakiela-tech/Nash-iw-research/blob/58ca45d9bd5ef36c13f7ced2b0372d0199596529/research/badacz/2026-10-29/IW_BADACZ_MECH7D_RIGOROUS_SOLVER_BOUND_V2_AFTER_AUD1_ROT009_025_20261029.md
- MT14 ROT013: https://github.com/wmakiela-tech/Nash-iw-research/blob/5f36f4a11e45436d7b7a1e3ecfbb751957554d90/research/mt14/2026-10-29/iw_mt14_rot013_scientific_programme_alignment_and_model_error_transfer_gate_001.md
- SCOPE9, 29 X: https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1793278681920889

## B. Dokładna konstrukcja zachowująca momenty

Wstawiamy `u=M/1e9g`, `z=ln u`, `z∈[ln .07, ln .92]`, `x=2(z-ZM)/L∈[-1,1]`, `L=ln(.92/.07)`. Źródłowy czas masowy implikuje dla łącznej *komowującej emisji* wagę `u³`. Nie zmieniamy postaci innych czterech hadronów ani tła termicznego.

Nie perturbujemy udziału `Qp/(Qp+Qn)` jako wielomianu. Zgodnie z Badaczem perturbujemy samo źródło, wybierając:

    k(x) = (1−x²)^4 Σ_{ℓ=3}^{10} a_ℓ C_ℓ^(9/2)(x),
    Qp^±(u) = Qp_native(u) ± k(x)/u³,
    Qn^±(u) = Qn_native(u) ∓ k(x)/u³.

Współczynniki `a` mogą być dowolnymi liczbami rzeczywistymi, także zapisanymi liczbami dziesiętnymi. `C_ℓ^(9/2)` są klasycznymi wielomianami Gegenbauera ortogonalnymi dla wagi `(1−x²)^4`. Dla `j=0,1,2`,  `∫_{−1}^1 x^j (1−x²)^4 C_ℓ^(9/2)(x)dx=0` **tożsamościowo**; zatem `∫u³ δQp z^j dz =0` i `∫u³ δQn z^j dz=0` dla obu ±, *niezależnie od wyjściowego Q_native*. Suma `Qp^±+Qn^±=Qp_native+Qn_native` zachowana **punktowo i dokładnie z definicji**, zaś wszystkie pochodne perturbacji do 3. rzędu znikają na końcach wsparcia. W symbolicznym niezależnym rachunku `sympy` sprawdzono dokładnie 8×3=24 tożsamości zerowania. Kwadratura SciPy jest tylko dodatkową kontrolą (relatywne reszty momentów ≤2.5e−16).

Dla porównania z ROT032 trzymamy ten sam budżet normy krzywizny *udziału* `h(z)=δQp/(Qp+Qn)`, `||h''||_L2 ≤ R=11.435960696834389`. Baza źródłowa składa się z 8 niezależnych kierunków (ℓ3…ℓ10). Matrycę H² liczymy bez aproksymacji pochodnych przez siatkę: dla `b=u³(Qp+Qn)`, `h=k/b`, `A=b'/b`, `A'=(b''b−b'²)/b²`, zachodzi `h''=(k''−2A k'+(A²−A')k)/b`. Wiersze funkcji sprzężonych Mech ROT021, ROT028 są traktowane jako **numeryczne, warunkowe** (nie fizyczne), a Riesz/Schur są matematycznymi narzędziami do wyznaczenia kierunków.

W tej nowej klasie o dokładnych momentach ostre promienie liniowe przy χEM=.5:

| Mapa | ROT032 dawna klasa: momenty numerycznie | ROT035 dokładna klasa Gegenbauera |
|---|---:|---:|
| B_exec | 5.72547462e-4 | 5.39487481e-4 |
| B_sym | 2.16589567e-4 | 2.00192865e-4 |

Uwaga: są to promienie **różnych skończeniewymiarowych klas**, obydwie w tej samej deklarowanej normie H². Mniejszy promień nie jest monotoniczną konsekwencją ścisłości; jest efektem zmiany bazy/klasy.

## C. Nowy faktycznie wykonany nieliniowy eksperyment: dokładne momenty

Wzięto kierunki Riesz maksymalizujące odpowiedź, skalowane dla **obu znaków** tak, aby pozostały dodatnie: 0.716026… budżetu H² dla B_exec, 0.730510… dla B_sym. Kody z tego pakietu rzeczywiście wywołują oryginalne archiwa Mech-S6, naprawiony 10-składnikowy preedge ROT013 i warunkową kinetykę 7D po krawędzi (Radau, `rtol=3e−9`, χEM=.5, stałe η). NIE wykonano źródłowego oryginalnego Julia 10D.

| mapa | Xnuc(+) | Xnuc(−) | połowa luki nieliniowej | liniowe przewidywanie dodatniej amplitudy |
|---|---:|---:|---:|---:|
| B_exec | 0.4013457986033065 | 0.4005731717792495 | **3.86313412028e−4** | 3.86287241782e−4 |
| B_sym | 0.4002312008516105 | 0.39993871354707966 | **1.46243652265e−4** | 1.46242790973e−4 |

Zaostrzenie `rtol` do `3e−10`: największa zmiana stanu końcowego 3.34e−11 (exec), 3.34e−12 (sym), dużo mniejsza niż luka. **To kontrola zbieżności, nie ścisły dowód błędu solvera**. Dla dokładnie określonego funkcjonału na *rzeczywistym rozwiązaniu ODE* dwupunktowy argument minimaksowy jest ważny dzięki dokładnie tej samej informacji. Podane **liczbowe wartości luki** mają jednak status numeryczny, do rygorystycznej dolnej granicy należy dodać niezależnie potwierdzone `ε_ODE(+)`, `ε_ODE(−)` i użyć `(gap_num−ε_+−ε_−)/2`. Tego ostatniego certyfikatu w ROT035 NIE ma.

## D. Dwa dodatkowe **niedokładne** pomiary — test odpowiedzi ROT034 w naprawionej klasie

Zachowano **dokładnie** trzy pierwotne momenty każdego gatunku oraz punktowo sumę źródła. Dodano dwa ważone pomiary `∫u³ Qp(u) w_i(logu)dlogu`, z wagami Gaussa o centrach `M1=8.32396936244e8 g, σ1=1`, `M2=4.77318736294e8g, σ2=.65`, znanymi z Mech ROT033. Założono **hipotetyczny** osobny błąd każdego odczytu `δ_i=η R ||a_i||_{H^−1}`, `η=.01`; wspólny raportowany odczyt może być **dokładnym punktem środkowym** dwóch odpowiedzi ±. Inaczej niż momenty 0…2 te odczyty NIE są deklarowane idealnie identyczne: wystarcza, że oba mieszczą się w *zadeklarowanych przedziałach niepewności*. Błąd 1% to frakcja max źródłowego zakresu pomiaru, nie rzeczywista dokładność instrumentu.

Nowa numeryczna analiza convex dual daje dla sześciu targetów z chiEM=.25,.5,.75 `max_2_weight_radius/original_no_weight_radius=0.0282560` przy `η=.01`, wobec 0.0283973 w starej klasie ROT034. W nowej klasie, χEM=.5:

| mapa | nowy promień liniowy 2 pomiary, η=.01 | maks. zmierzona różnica/2 z ODE dla ± | wymaganie obu pomiarów |
|---|---:|---:|---|
| B_exec | 1.33289801e−5 | **1.31287552213e−5** | odchylenie <0.985 δ_i |
| B_sym | 5.64892008e−6 | **5.56423334816e−6** | odchylenie <0.9851 δ_i |

Kierunki świadków zredukowano do `0.985` swojego H² promienia dla zapasu dodatniości i tolerancji. Wyniki: pełne ODE dla obu map, `ε=0,±1`, `rtol=3e−9` plus ponowne trzy stany przy `3e−10`. Maksymalne różnice wyników między tymi tolerancjami ≤3.34e−11. Cztery niezależne testy przybliżonej równości momentów SciPy `quad`: największa względna reszta ~2.5e−16, ale gwarancja momentów pozostaje SYMBOLICZNA, nie kwadraturowa. Dwa pomiary świadków oceniono niezależną 1536-punktową kwadraturą: obydwa <0.9851 własnej `δ_i`.

## E. Dodatniość i niezależne kontrole

**We wszystkich czterech świadkach** (dwie mapy × kierunek czystych momentów/noisy) sprawdzono konserwatywną obwiednię wielomianową: 128 podprzedziałów `x∈[-1,1]`; na każdym maksimum `|k(x)|` ograniczano od góry z bezwzględnych współczynników Bernsteina stopnia 18; dolny limit `u³ Q_species` otrzymywano przez minimum na obu końcach przy mocowym źródle. Najmniejszy względny zapas `1−bound_k/lower_u3Q` z wysokoprecyzyjnego `mpmath` był 0.274260 (czysty exec), 0.274706 (czysty sym), 0.346847 (noisy exec), 0.416081 (noisy sym). To konserwatywne NUMERYCZNE kontrole w zadeklarowanej klasie, nie formalna maszynowa arytmetyka przedziałowa dla fizyki PBH.

Kontrola źródła podkrawędziowego: użyte native `Qp,Qn=SQ*u**SL` są identyczne z implementacją `source_rates(u,'public','native',...)` w sprawdzonych czterech punktach; nie poprawia to fizycznej wiarygodności ekstrapolacji. Źródła są dodatnie i takie same poza `M∈(7e7,9.2e8)g`; na krawędzi zanikają wszystkie derywacje do 3. rzędu.

Przenoszenie statusu: dokładność momentów **PASS jako ścisła algebra konstrukcyjna**; wartości końcowe **EXECUTED_CONDITIONAL_NUMERIC**; ścisłe wartości minimaksowe dla realnego rozwiązania **HOLD bez niezależnego εODE**; weryfikacja `Badacz doc025 v2` **PENDING AUD1**; źródło fizyczne poniżej 1e9g i oryginalne Julia10D **NOT VALIDATED**.

## F. Przegląd projektu na 29 października i wykorzystanie wyników

Źródłowy przegląd z ostatnich komunikatów i publicznych raportów (nie pełna historyczna inwentaryzacja prywatnych BW):

- **P1 / Front B:** Mech-S7 ROT020–034 ma liczne wykonane testy warunkowego źródła i 7D, ale za wcześnie na PBH/BBN. Najistotniejsze teraz LT6 ROT009, AUD1 SELF-002 i Badacz doc 022/025 — dokładna informacja, niezależny błąd solvera i kryteria fizycznej dopuszczalności. Materiał Badacz v1 z `certified_*` NIE był poprawnym certyfikatem, co AUD1 wykazał; v2 jest nowy, wciąż bez niezależnego PASS i bez przełożenia na nasze trajektorie. MT14 ROT013 nakazuje oddzielić błąd systematyczny modelu od szumu instrumentu.
- **P3 DTC0A / N41:** M13 oryginalne B pięciu masek; MT14 ROT011 rygorystyczne najbliższe granice **wyłącznie δ=.01**, ROT012 ilościowa źródłowo-warunkowa separacja statystyczna; INT8 ROT041/042 dokładne normy pomocniczych projektorów TT i geometrię transportu, Geeky-S11 ROT032/033 źródłowo-typowane stabilność i warianty parametru α. Wszystkie te prace klasyczne i modelowo określone; brak fizycznego J3/K lub GR. 
- **Living Theory / SCOPE9 / PRF / REC:** LT6 REV028 i ROT009 rozwijają strukturę dowodową; SCOPE9 CROSSCELL SYNTHESIS 010 proponuje cztery odrębne osie: dokładne włókna obserwacyjne, promień błędu targetu, legalny eksperyment i reprezentacyjnie właściwą normę. REC10/SW/AUD1 są warstwami kontroli — nie utożsamiać własnego audytu lub recenzji z niezależnym acceptance.
- **XH-S5 / zewnętrzne zakotwiczenie:** ROT008 używa pracy grafenowej Nature 2026 do dodatniego *syntetycznego* modelu pamięci; ROT009 używa świeżej propozycji interferometrii neutronowej do eksperymentu przełączania masy z nieidentyfikowalnością dryfu kwadratowego. Nie są to powtórzenia pełnych eksperymentów źródłowych. M14 niezależnie analizuje identyfikowalność czujników NV i Yukawę przy jawnych klasach obserwacji. 
- **Custody:** SYSS5 wdrożył wymagane pola `artifact_id/exposure/claim_ceiling/sync_state`. KN12 poszukuje oryginalnych skryptów NC N=21, ponieważ jawne metadane siatki `L=3,N=21,dx=.15` są niespójne z `np.linspace(-L,L,N)` (dla N21 byłoby dx=.30); to przykład, że źródłowa proweniencja liczb jest równie ważna jak dowód. GitHub ≠ ingest BW, brak oczekiwanego naturalnego awansu statusów.

Wybrane źródła uzupełniające:
- MT14 ROT012 https://github.com/wmakiela-tech/Nash-iw-research/blob/a0322c3c7dba2f7752d20229f2e0e8d028ea1f22/research/mt14/2026-10-29/iw_mt14_rot012_B_source_interval_global_statistical_separation_gaussian_resource_001.md
- MT14 ROT013 https://github.com/wmakiela-tech/Nash-iw-research/blob/5f36f4a11e45436d7b7a1e3ecfbb751957554d90/research/mt14/2026-10-29/iw_mt14_rot013_scientific_programme_alignment_and_model_error_transfer_gate_001.md
- INT8 ROT042 https://github.com/wmakiela-tech/Nash-iw-research/blob/e828e6752b26bc706b11060a832c79361dd16d2c/research/int8/2026-10-29/iw_int8_rot042_general_unimodular_tt_norm_finite_grid_attainment_001.md
- XH-S5 ROT008 https://github.com/wmakiela-tech/Nash-iw-research/blob/fc299de436fcf30b5bb87e19323741093ee4f099/research/xh-s5/2026-10-29/iw_xh_s5_rot008_graphene_relaxation_kernel_exact_dc_and_complex_phasor_null_001.md
- XH-S5 ROT009 https://github.com/wmakiela-tech/Nash-iw-research/blob/262ffca299c30b44c0b4a395f5e57d2db29cadc2/research/xh-s5/2026-10-29/iw_xh_s5_rot009_neutron_pgmi_quadratic_drift_switching_design_001.md
- SCOPE9 https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1793278681920889
- KN12 provenance https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1793055428202839

## G. Owner disposition wobec AUD1 SELF-002 i korekta wcześniejszych claims

**AUD1 finding ACCEPT.** ROT032 różnice momentów ~1e−12 nie uzasadniały ścisłego minimaksu dla idealnych dokładnych wejść; wcześniejsze sformułowania tak interpretowane są **RETRACTED AS A STRICT CERTIFICATION**. Sam liniowy wynik Riesz przy faktycznie przyjętej numerycznie zdefiniowanej przestrzeni nie zostaje automatycznie unieważniony; konkluzja o *ścisłej* równości analitycznych danych wymaga naprawy. ROT033 „dokładne pomiary Gaussa” dotyczyły projekcji obliczonych numerycznie, więc ścisłą równość idealną uznajemy za nieudowodnioną. ROT034 dwa **niedokładne** pomiary z zadanymi tolerancjami mają sens operacyjny, ale oryginalne trzy momenty nie zostały tam formalnie równe — nowy ROT035 daje wykonany zamiennik tej luki. Nie modyfikujemy ani nie fabrykujemy historycznych surowych wyników.

Obecna poprawa:
1. Dokładnie równe trzy momenty (dla wskazanej nowej klasy Gegenbauera) — `EXACT_MATH_BY_IDENTITY`.
2. Dodatniość — konserwatywne kontrole Bernsteina dla 4 źródeł, zastrzeżenie końcowej arytmetyki o ograniczonej precyzji.
3. Niezerowa odpowiedź nieliniowa — `EXECUTED_NUMERIC_ODE`, dwie mapy, dwa warianty obserwacji, 24 trajektorie nominal/tight łącznie.
4. Rygorystycznie certyfikowany błąd numeryczny dla tych konkretnych Mech trajektorii — `OPEN`; doc025 Badacza ma model syntetyczny i oczekuje audytu.
5. Fizyczna poprawność przedłużenia widma, oryginalna Julia10D, Yp, D/H i ograniczenia PBH — `OPEN/NOT_EXECUTED`.

Zwrócić do AUD1 jako właściciel: **OWNER_REPAIR_EXECUTED_WITH_CLAIM_NARROWING / INDEPENDENT_REVIEW_PENDING**; nie nadawać `AUDIT_PASS`, `EXEC_SIGN`, `CANON` ani `BW_ING`.

## H. Odtwarzalność

Nowe oryginalne skrypty: `exact_moment_gegamma_repair_035.py` (Sympy exact 24 zeros, H2/target and source), `execute_exact_witness_035.py` (conditional ODE), `exact_moment_noisy_two_weights_035.py` (finite H2 bounded measurement dual), `execute_exact_noisy_witness_035.py` (conditional ODE), `independent_source_controls_035.py` (separate Gauss/quad and polynomial Bernstein). Dependencies SciPy, NumPy, SymPy, mpmath, pandas (inherited Mech-S7), Python stdlib; full pinned raw archives Mech-S6 plus dependent codes/repro input json/csv stored in self-contained ZIP. Run in unzipped root; root contains inherited Mech-S7 scripts and `mech_s7_rotation_009/`, `mech_s7_rotation_010/`. New results in `*_035.json`, `*_035.csv`, `*.log`. All scripts executed with Python 3.13, NumPy 2.3.5, SciPy 1.17.0, Sympy 1.14.0. No source-provided Julia10D solver executed.

`NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_Yp_DH / NO_PBH_BOUND / BW_PENDING`.