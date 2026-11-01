artifact_id: MECH-S7-ROT036-SOURCE-TYPED-WUXU-TABLE-EXTRAPOLATION-AUDIT-20261101
exposure: PUBLIC
claim_ceiling: SOURCE_PINNED_AUTHOR_CODE_READ_AND_CONDITIONAL_REDUCED_7D_EXTRAPOLATION_STRESS / NO_INDEPENDENT_PHYSICAL_SPECTRAL_VALIDATION / NO_PBH_BOUND / NO_EXEC_SIGN / NO_CANON / NO_NOVELTY
sync_state: GITHUB_PENDING_BW_INGEST
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7
rotation: ROT036
document_date: 2026-11-01
problem_id: P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001

# Mech-S7 ROT036 — źródłowy audyt ekstrapolacji hadronów w kodzie Wu–Xu (zamknięcie obrotu)

## A. Pochodzenie, status naukowy i ograniczenia

Kod oryginalny Wu–Xu, `Fenyutanchan/Primordial-Black-Hole`, commit `d395183674cace6c9906a8911bdeb7234ba4040d`: `arXiv-2509.05618/main-scan.jl` (Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`), `tool_script-hadrons_from_PBH.jl` (Git blob `cc73432910f872d526113ce59b6204f38d0766a9`), `data/out/hadrons_from_PBH.dat` (Git blob `06d0883a27b108692720422294ba2baacd381a64`).

Pełna tabela ma 100 wierszy dla M=10^9 do 4×10^12 g. Five hadron channel columns: charged pion, charged kaon, neutral long kaon, proton, neutron. Values in original file are given in GeV units, not direct grams; the mass units for first/last node follow from author/source mapping. Autorzy implementują `LinearInterpolation(log(rate),log(mass);extrapolation=ExtrapolationType.Linear)`: poniżej pierwszego wiersza ma to charakter potęgi z wykładnikiem wyznaczonym przez **pierwsze dwa wiersze**, nie pustego lub zablokowanego kanału. Native 10D ODE vector: log(t),log(ρSM),log(M),log(Xn), six log populations hadronic; η=ln a, `AutoTsit5(Rosenbrock23())`. Ewentualne źródło fizycznie ważne poniżej brzegu **nie jest w tym raporcie niezależnie sprawdzone**.

Pierwsze 9 wierszy oryginalnej tabeli zostało zachowane w naszym wcześniejszym `edge_bridge_013.py` (jawny `SOURCE8` obejmuje faktycznie 9 wierszy). Daty i wyniki Mech-S7 ROT013–035 stanowią kontekst naukowy, ale nie są źródłowymi runami Julia.

## B. Test wykonany w Mech-S7

Wszystkie kanały hadronowe mają wyznaczone przy brzegu wykładniki około −1.20. W alternatywnym eksperymencie użyliśmy współczynników OLS z **wolnym wyrazem**, dopasowanych na pierwszych ośmiu oryginalnych wierszach w log-log, po czym wymusiliśmy identyczną wartość emisji na 10^9 g. To nie jest oryginalny wariant autorów i nie jest regresją narzucającą dokładną wartość na brzegu w procesie dopasowania. Wyniki CSV: `source_extrapolation_sensitivity_036.csv`.

Warunkowa kinetyka z 10-składnikowym źródłowym transportem Mech ROT013 do 10^9 g, dalej subedge i postsource 7D, eta-constant baryon, EM=50%, dwie mapy:

| Mapa | Xnuc native 2-node | Xnuc alternate 8-node OLS | Różnica |
|---|---:|---:|---:|
| B_exec | 0.400959518961858 | 0.400976847543352 | +1.73285814936×10^-5 |
| B_sym | 0.400084966240828 | 0.400108745370008 | +2.37791291796×10^-5 |

Załączone pierwotne `conditional_extrapolation_kinetic_036.csv` oraz `heldout_and_tight_036.csv`: test chi_EM=0,.5,1 i nominalny tight Radau. Kontrasty występują również przy chi=0 i chi=1. Zmiana kontrastu po 10× ostrzejszej tolerancji <3×10^-13 w poprzednim kodzie; niezależna implementacja ROT037 potwierdziła efekt na poziomie <2×10^-10. Tylko model warunkowy. Nie przypisujemy tak uzyskanej różnicy żadnemu prawdopodobieństwu modelowania emisji.

## C. Stan projektu zweryfikowany po 31 października (korekta wiedzy negatywnej)

**UWAGA — wycofanie zbyt szerokiego zdania „original Julia 10D NOT_EXECUTED” o całym NASH.** Według źródłowego zwrotu Badacza z 2026-10-31 oryginalny kod autorów d395183 został uruchomiony w jego środowisku dla skanów 74-punktowych oraz 5 wariantów źródła na 12 masach; Mech-S6 uruchamiał oryginalny kod w CI 18 października. To nie są runy wykonane ani niezależnie zreprodukowane w środowisku niniejszego Mech-S7 ROT036–037, a wyniki Badacza wymagają niezależnej recenzji. Zatem: `AUTHOR_JULIA10D_PROJECT_EXECUTED_BUT_THIS_CELL_NOT_REPLAYED`.

Badacz (pierwszeństwo właścicielskie) opisał dla źródłowego skanu warunkowe przesunięcia konturu beta po zmianie mapy ładunku (~0.27–0.30 dex dla pełnego B_sym), przesłanki o kodowej ekstrapolacji lewej ściany, problem z Yp rebaseline i pilot PYTHIA hadronization T>TeV. Wyniki są informacyjne; nie są tu przedstawiane jako niezależnie potwierdzone i nie dostarczają fizycznego ograniczenia PBH. Źródło przekazu: https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1793462544056049 oraz https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1793474390538889. Programowy kontekst MT14 ROT019: https://github.com/wmakiela-tech/Nash-iw-research/blob/7e41f16db4a95ea9c5767ebc11e7dbaca46148bf/research/mt14/2026-11-01/iw_mt14_rot019_nc_alg018_hyperplane_spectral_variational_frontb_currentness_001.md.

## D. Wniosek i dalszy eksperyment

Oryginalny autor **implementuje** subedge continued rates, lecz nie weryfikuje ich w naszym teście niezależnie fizycznie. Warunkowa zmiana jednego sposobu ekstrapolacji daje różnice Xnuc ~10^-5 większe niż wiele wcześniejszych kontrastów źródło/mapa. Nie twierdzimy, że alternatywne OLS to bardziej prawdziwa fizyka. Następny ROT037 rozdziela dwa sposoby regresji i usuwa ewentualną nieciągłość pochodnych C1/C2 na brzegu.

STOP: brak oryginalnego runu Julia **w tym** środowisku, brak niezależnego source-native pełnego Yp/PBH bound, brak ważności fizycznej pod tablicą, brak przyjętego przez REC/AUD1 certyfikatu błędu całego source-to-contour operatora, brak BW ingest/EXEC/kanonu/nowości.