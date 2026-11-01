artifact_id: MECH-S7-ROT037-LOGTABLE-FIT-WINDOW-C2-EDGE-SOURCE-TRANSFER-GATE-20261101
exposure: PUBLIC
claim_ceiling: EXECUTED_CONDITIONAL_REDUCED_SOURCE_EXTRAPOLATION_FIT_WINDOW_AND_C2_JET_TEST / ORIGINAL_JULIA_RUN_BY_OTHER_CELLS_NOT_REPLAYED_HERE / NO_PHYSICAL_HAWKING_OR_BBN_BOUND / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY
sync_state: GITHUB_PENDING_BW_INGEST
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7
rotation: ROT037
document_date: 2026-11-01
problem_id: P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001

# Mech-S7 ROT037 — zakres dopasowania ekstrapolacji, C² na brzegu i kinetyka neutronowa

## I. Rozróżnienie testów i pierwszeństwa

Autorzy Wu–Xu (pin `d395183674cace6c9906a8911bdeb7234ba4040d`) implementują potęgowe przedłużenie 5 źródłowych kanałów od pierwszych dwóch wierszy `hadrons_from_PBH.dat` poniżej 10^9g, przez `ExtrapolationType.Linear` po log-log. Mech-S7 ROT036 pierwszy w tej linii przeprowadził alternatywny test 8-point OLS w redukowanym modelu. Badacz niezależnie uruchomił oryginalny Julia 10D w NASH (31 X 2026) i skanował wpływ prawa subedge na kontur ograniczeń, a w pilotażu PYTHIA sformułował hipotezę artefaktu ostatnich wierszy. Pierwszeństwo source-native interpretacji/PYTHIA należy do Badacza; jego wnioski nie są tu niezależnie recenzowane. Przyjmujemy status REVIEW_PENDING. Nasz niezależny przyrost: wrażliwość na **procedurę** regresji, dokładny C² edge-jet matched falsifier, kontrola trzech teł i tightened conditional ODE.

Źródło: `arXiv-2509.05618/tool_script-hadrons_from_PBH.jl`, blob `cc73432910f872d526113ce59b6204f38d0766a9`; tabela `06d0883a27b108692720422294ba2baacd381a64`. Mech ROT013 code tabulates 9 original near-edge rows in its pinned `edge_bridge_013.py`. Nie twierdzimy, że 9 wierszy ujmuje wszystkie 100 oryginalnych punktów.

## II. Dwa różne estymatory pochodnej źródła

Niech z_i=ln(M_i/M_edge), y_i=ln(Q_i/Q_edge), i=0..n-1, z_0=y_0=0. Autorzy używają s_native=y_1/z_1. Porównania:

* `free_intercept`: nachylenie s_OLS z regresji y_i=a+s z_i (wyraz wolny dopasowany swobodnie), następnie wymuszenie Q(M_edge)=Q_edge przez nadpisanie a=0 w przedłużeniu. Krawędź jest C0, ale generalnie nie C1.
* `edge_constrained`: estymator s_C=(Σ_i z_i y_i)/(Σ_i z_i²); wymaga wartości brzegowej już podczas dopasowania. Te same źródłowe punkty, inna procedura.

Oba są hipotetyczne poniżej 10^9g, zgodne z wartością Qedge; **żaden nie jest oryginalnym algorytmem** (poza n=2).

Warunkowy Mech ROT013 preedge + 7D eta-constant, chi_EM=0.5, źródło od M1=10^9g do stop mass ~12.37 g, B_exec i B_sym; wynik z `fit_window_kinetic_037.csv`:

| Pierwsze n wierszy / fit | ΔXnuc B_exec | ΔXnuc B_sym |
|---|---:|---:|
| 2: native | 0 | 0 |
| 3: free_intercept | +3.18306679e-6 | +5.55294131e-6 |
| 5: free_intercept | +8.86153540e-6 | +1.43554219e-5 |
| 8: free_intercept | +1.73285823e-5 | +2.37791305e-5 |
| 8: edge_constrained | +1.32802506e-5 | +1.87868140e-5 |
| 9: free_intercept | +1.98689571e-5 | +2.61620966e-5 |
| 9: edge_constrained | +1.52247849e-5 | +2.07514981e-5 |

Dwie procedury z n=8 różnią się zatem o 4.04833166e-6 (`B_exec`) i 4.99231650e-6 (`B_sym`) w Xnuc. Monotoniczność powyższych 3,5,8,9 występuje w tej skończonej próbce; nie wnioskujemy jej dla wszystkich n, choć tabela autorów ma 100 wierszy.

## III. C² source-edge jet falsifier

Wprowadzamy z=ln u<=0, u=M/10^9g. Dla alt slope s_alt i original slope s0, definiujemy:

    log(Q(z)/Qedge) = s0*z + (s_alt−s0) F_w(z),
    F_w(z)=0                              dla z>=0,
    F_w(z)=z g(-z/w)                     dla -w<z<0,
    F_w(z)=z                              dla z<=-w,
    g(q)=6q^5−15q^4+10q^3.

Algebra symboliczna SymPy potwierdza ciągłość funkcji i jej pierwszych DWÓCH pochodnych na z=0 i z=−w (`independent_fit_jet_audit_037.py`), więc na brzegu kodowej tabeli narzucamy dokładnie naturalny s0 i 0 krzywizny logQ. Poza warstwą o szerokości w wracamy do alternatywnej potęgi. Dodatnie Q w całym u∈[Mcut/Medge,1] z definicji wykładniczej; 1301×3 węzły to dodatkowa numeryczna kontrola.

EM=50%, alternatywne 8 free-intercept dla pięciu kanałów:

| Model | ΔXnuc exec | ΔXnuc sym | Udział efektu bez C² |
|---|---:|---:|---:|
| C0, brak wyrównania pochodnych | +1.73285823e-5 | +2.37791305e-5 | 100% |
| C², w=0.1 | +1.72839639e-5 | +2.36961757e-5 | 99.74% / 99.65% |
| C², w=0.3 | +1.69546883e-5 | +2.31145151e-5 | 97.84% / 97.21% |
| C², w=0.5 | +1.63708122e-5 | +2.21374444e-5 | 94.47% / 93.10% |

**Odrzucona hipoteza kontrolna:** niemal cała odpowiedź ROT036 nie pochodzi tylko z załamania pierwszej lub drugiej pochodnej ekstrapolowanej emisji na M=10^9g. Test nie identyfikuje, która z funkcji jest fizycznie prawdziwa.

## IV. Nieobjęte kalibracją tła i błędy

`c2_edge_heldout_037.csv`, chi_EM=0 i 1, oba B, w=.3, osobne solve_ivp. ΔXnuc C² względem native:

| chi_EM | B_exec | B_sym |
|---|---:|---:|
| 0.0 | +1.69826040e-5 | +2.31925265e-5 |
| 0.5 | +1.69546883e-5 | +2.31145151e-5 |
| 1.0 | +1.69269893e-5 | +2.30372947e-5 |

`c2_edge_tight_037.csv`: 10× ostrzejsza Radau rtol=3e-10 vs 3e-9 dla chi=.5, 2 map, native/C0/C². Max difference C² ΔXnuc: 1.06e-12 exec, 3.59e-13 sym; to NIE jest matematyczny certyfikat błędu prawdziwego ODE ani źródłowego Yp.

W sumie wykonano 42 integracje 7D active/post: 14 window fits w chi .5, 10 nominal C² incl native/C0, 12 heldout, 6 tight. Każdy model ponownie wykorzystuje 10-component source-supported edge bridge Mech ROT013. Testy replikacji ROT036 native i 8 OLS (różnica poniżej 2e−10), niezależne `lstsq` oraz symbolic C² jets PASS w `INDEPENDENT_AUDIT_037.json`. Współczynniki są warunkowe, a nie autor-native source below table.

## V. Stan naukowy projektu i wybór właścicielski

**Korekta zakresu „original Julia 10D NOT_EXECUTED”:** już nie wolno przypisywać tego stwierdzenia całości NASH. Badacz poinformował 31 X o 74 scan points +5 wariantach źródła na 12 masach w oryginalnym Julia d395183, a Mech-S6 uruchomił go w CI 18 X. W naszym środowisku ROT037 Julia nie jest zainstalowana i oryginalnego 10D nie reexecutowano. Przyjmuję wyniki Badacza jako ważne źródłowe *kandydaty* wymagające audytu spoza rodziny Claude.

Badacz pierwszy wskazał zależność konturu Fig.5 od kanałów p/n, konieczność przeskalowania Yp oraz lewą ścianę zależną od emisji pod 10^9g; później pilot PYTHIA 8.318 sugeruje, że s0~−1.20 jest brzegowym artefaktem tabeli BlackHawk, a jego alternatywny p13 daje źródłowy contour shift od 0.03 do 0.055 dex przy niskich masach. Jego B2 gate nie przeszła i osobna wariacja C nie została uruchomiona. Wszystko `CONDITIONAL_[▷]`, brak PBH bound, REC/ AUD1 nadal niezależni.

Dostępne przekazania: https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1793462544056049 ; https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1793474390538889 ; program MT14 1 XI: https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1793528802666979 . Nie wnioskujemy wspólnej fizycznej teorii z wyników DTC0a/NC/LT. Bramy metodologiczne AUD1/REC pozostają.

**Właścicielska dyspozycja (bez EXEC):** (a) uznać udokumentowaną kodową emisję subedge, ale rozdzielić od fizycznej trafności; (b) przyjąć E5/E5b i p13/PYTHIA jako source-conditional priority do nieślepej kontroli po stronie REC/AUD1, bez włączania do kanonu; (c) nie mnożyć arbitralnych fitów jako substytutu walidacji fragmentacji/greybody/ciężkich bozonów; (d) jako dalszą bramę Front B zachować physical E4 i prawidłowe odtworzenie source-native full contour jako oddzielne obowiązki.

## VI. Reprodukcja i custody

Źródłowy zestaw Mech-S7 ROT035 (włącznie z oboma public/paper S6 raw ZIP, pełnym kodem Mech ROT013 i funkcjami ODE) jest podstawą pakietu tego obrotu. Nowe skrypty `reproduce_extrapolation_fit_controls_037.py`, `c2_edge_extrapolation_gate_037.py`, `independent_fit_jet_audit_037.py`; wyniki CSV/JSON i `INDEPENDENT_AUDIT_037.json`. Pliki ROT036 zachowane bez zmiany liczb. Manifest SHA256 oraz kontrola ZIP są w pakiecie. Brak przypisywania źródłowo preegzekwowanemu modelowi statusu fizycznego.

STOP: `NO_CONTOUR_PBH_CLAIM / NO_SOURCE_VALIDATION_BELOW_TABLE / NO_AUTHOR_NATIVE_RUN_IN_THIS_CONTAINER / NO_STRICT_ODE_CERTIFICATE / REFEREE_PENDING / BW_INGEST_PENDING / NO_CANON / NO_EXEC / NO_NOVELTY`.