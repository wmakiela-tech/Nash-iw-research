# LT5 ROT21 — rzeczywiste odejmowanie literatury: systemy behawioralne i optymalne odtwarzanie

**RETURN_ID:** LT5-ROT21-BEHAVIORAL-OPTIMAL-RECOVERY-THEOREM-LEVEL-HOST-SUBTRACTION-001_20261025
**Data:** 2026-10-25
**Rola:** LT5 / Żywa Teoria — autorski przegląd prior art, priorytet odbioru MT13.
**Odniesienie:** robocza, niekanoniczna REV021 https://docs.google.com/document/d/15b-8uK2DZVScU6k-K6eesL8d8nt777-UmalEUb5U-zE/edit
**TRYB:** LITERATURE_FIRST / THEOREM_LEVEL_VERIFIED_FOR_ACCESSIBLE_SOURCE / NEGATIVE_KNOWLEDGE / ONE_INDEPENDENT_TOY_WITNESS.
**Granice:** NO_NEW_MATH_NOVELTY / NO_CANON / NO_EXEC / NO_PHYSICAL_UPGRADE / NO_FULL_PW_BOOK_READ / NO_BW_INGEST_ASSERTION.
**Przednia praca:** atlas LT5 → MT13 z 2026-10-25; ten obrót NIE powtarza jego bibliografii, ale uzupełnia weryfikację na poziomie konkretnych definicji i twierdzeń.

## 1. Czego dokonano rzeczywiście: źródła i stopień weryfikacji

**H-OR1 — dokument pierwotny, przeczytany w części na poziomie twierdzeń.**
M. Ettehad, S. Foucart, Instances of Computational Optimal Recovery: Dealing with Observation Errors, SIAM/ASA Journal on Uncertainty Quantification 9 (2021), DOI 10.1137/20M1328476.
Pełny manuskrypt autora https://foucart.github.io/publi/OR_Uncertainty_v2.pdf (zweryfikowany tekst, obejrzano stronę 3 PDF). Dokładnie sprawdzono: §1 równania (1)–(7), §2.1 twierdzenie 1 i program liniowy (14), §3.1 redukcję błędnego obserwowania do dokładnego poprzez rozszerzoną przestrzeń (33)–(35), §3.2 klasę aproksymowalności (36) i ograniczenie dim V ≤ m, §4 twierdzenie 4 oraz warunek liniowego celu Q i szumu o ograniczonej normie, §5.2 twierdzenie 8 o near-optimal full recovery. Nie twierdzimy, że zweryfikowano wszystkie szczegóły dowodów i weryfikacji numerycznej wszystkich pozostałych wyników artykułu.
Pierwotny autorski reproducer https://github.com/foucart/COR/blob/main/MATLAB/OR_Uncertainty_repro.m (istnieje; nie uruchamiano). 

**H-BH1 — książka, weryfikacja zakresu bibliograficznego i rozdziałów, NIE pełnej treści.**
J. W. Polderman, J. C. Willems, Introduction to Mathematical Systems Theory: A Behavioral Approach (Springer, 1998), https://link.springer.com/book/10.1007/978-1-4757-2953-5 .
Sprawdzono spis treści: Ch3 Linear Differential Equations, Ch5 State Space Models s.115–149, Ch6 Controllability and Observability s.151–199, Ch7 Elimination of Latent Variables and State Space Representations s.201–240, Ch9 Time-/Frequency-Domain Characteristics. Opis autorów z Uniwersytetu Twente wskazuje zakres: równoważność modeli przez to samo zachowanie trajektorii, zmienne manifest i latent, sterowalność i obserwowalność. Nie przypisujemy tej książce szczególnego nieprzeczytanego numeru twierdzenia.

**H-BH2 — pierwotne artykuły właściwe dla szczególnych nośników.**
J. W. Polderman, Proper elimination of latent variables, Systems & Control Letters 32 (1997) 261–269, DOI 10.1016/S0167-6911(97)00082-0: abstrakt potwierdza konieczność dodatkowych warunków przy eliminacji zmiennych ukrytych z reprezentacji różniczkowo-wielomianowych. Pełnego płatnego tekstu nie zweryfikowano.
J. C. Willems, P. Rapisarda, I. Markovsky, B. De Moor, A note on persistency of excitation, Systems & Control Letters 54 (2005) 325–329, DOI 10.1016/j.sysconle.2004.09.003: wykazano, że odpowiednio ekscytujące dane dla sterowalnego LTI rozpinają trajektorie skończonego horyzontu; nośnik to kontrolowany LTI i rząd pobudzenia zależy od długości okna plus wymiaru stanu. Sprawdzono abstrakt wydawcy i źródła bibliograficzne; nie twierdzimy, że odtworzono pełny dowód.
J. C. Willems, S. K. Mitter, Controllability, Observability, Pole Allocation, and State Reconstruction, IEEE Trans Automatic Control AC-16 (1971), 582–595, manuskrypt MIT: https://mitter.lids.mit.edu/publications/11_controllability_pole_IEEEAC.pdf . Materiał dotyczący związku minimalnej realizacji oraz kontroli/obserwacji.

**H-EXP — starsze, bardziej bezpośrednie uprzednie wyniki na projektowanie eksperymentu.**
L. Pronzato, E. Walter, Experiment design in a bounded-error context: Comparison with D-optimality, Automatica 25 (1989), 383–391, DOI 10.1016/0005-1098(89)90006-X: minimalizowanie objętości zbioru parametrów zgodnych z ograniczonymi błędami (nie tylko informacja Fishera).
L. Pronzato, E. Walter, Experiment design for bounded-error models, Mathematics and Computers in Simulation 32 (1990), 571–584, DOI 10.1016/0378-4754(90)90013-9: już rozważano NIELINIOWE modele i ROZŁĄCZNE zbiory parametrów dopuszczalnych.
M. Karimshoushtari, C. Novara, Design of experiments for nonlinear system identification: A set membership approach, Automatica (2020), DOI 10.1016/j.automatica.2020.109036: explicite minimalizacja promienia informacji w DoE dla wybranej klasy nieliniowych MISO.
R. A. Lewis, A. M. B. ..., nie przywołujemy niezweryfikowanych dodatkowych publikacji. Najnowszy przekrojowy punkt odniesienia: Optimal experimental design: Formulations and computations, Acta Numerica (2024), https://www.cambridge.org/core/journals/acta-numerica/article/optimal-experimental-design-formulations-and-computations/38BBD0DC1A0386FDF306B6C0167DF7D9 (zweryfikowano abstrakt o design criteria, Bayesian i sequential OED).
To jest silne PRIOR ART odejmujące samo hasło „projektowanie pomiarów przez promień informacji”. Nie zastępuje jednak badania identyczności wszystkich szczegółowych warunków źródła NASH.

**H-IDENT — dwa typy nieidentyfikowalności.**
A. Raue i in., Structural and practical identifiability analysis of partially observed dynamical models by exploiting the profile likelihood, Bioinformatics 25 (2009), 1923–1929, DOI 10.1093/bioinformatics/btp358: rozróżnienie strukturalnej vs praktycznej identyfikowalności, profile likelihood, planowanie doświadczeń. Zweryfikowano tekst streszczenia w PubMed i stronę wydawcy. Nie utożsamiać lokalnego Fishera, globalnego bounded-noise minimax i dokładnego coverage chi-bar (różne inferencje).

## 2. Mapa dokładna do rozdziałów Żywej Teorii

| LT REV021 | Sprawdzone wcześniejsze źródło | Status po odejmowaniu | Co NIE wynika |
|---|---|---|---|
| Ch2 §2.2 / Ch7 §7.2: obserwowalne włókna, rU=Vr | Polderman–Willems Ch5–7 (zakres), Willems–Mitter 1971 | MATURE_HOST / BASIC FACTORIZATION, NO MATH NOVELTY | sama równość części input/output nie gwarantuje targetu ukrytego stanu i nie obejmuje dowolnych interwencji |
| Ch7 §7.5b Tw 7.9 scalar minimax | Ettehad–Foucart §1–4 + starsza literatura OR | MATURE_OPTIMAL_RECOVERY / CONDITIONAL_HILBERT_RESULT | optymalny LINEARNY estymator nie musi istnieć dla dowolnej niekonweksyjnej klasy |
| Ch7 §7.5d Tw 7.9a, arbitrary A scalar radius | Ettehad–Foucart §1 eq(7), §2 Chebyshev center | MATURE_FIBER_CHEBYSHEV_SPECIALIZATION | ten artykuł nie stwierdza wszystkich naszych nieliniowych/heteroscedastycznych formuł dosłownie |
| Ch7 §7.5e Tw 7.9b, joint relative + additive bounds | OR §1 + state-dependent rectangular information model | CLASSICAL_GEOMETRIC_COROLLARY, POSSIBLE COMPUTATIONAL HOST DIFFERENCE | sama analiza przecięcia prostokątów nie jest nowością; potrzebna ocena source/legal correlations i global solver |
| Ch4 M13/MT masked gain, spectral source | Walter–Pronzato / Raue + DoE 1989/1990/2020 | SOURCE_RESTRICTED_APPLICATION / ORIGINALITY_NOT_YET_ESTABLISHED | monotoniczna ratio, 18/12 mask signs, c95 chi-bar nie są fizyczną kalibracją |
| MT13 ROT037, 5 overlapping masks under Gaussian energies | Gaussian orthogonal projection + known cone/chi-bar host | EXACT_SOURCE_TYPED_FINITE_SAMPLE, MATURE_DISTRIBUTION | PRF/NC/physical instrument nie są objęte i nie można traktować pięciu masek jako niezależnych średnich |
| PW-Willems data-driven LTI excitation | Willems et al 2005 | KNOWN_LTI_BEHAVIORAL_SPANNING | sam długi ciąg danych NIE daje pełnej informacji bez założeń controllable LTI i persistent excitation |

To NIE jest pełny prior-art audit wszystkich twierdzeń siedmiu rozdziałów. W szczególności nie przeanalizowano matematycznie całego Ch4 TT ani Ch6 fizyki. Nie twierdzić, że udowodniono brak nowości wszystkich wyników NASH.

## 3. Źródłowo znany kontrprzykład: zgodność I/O ≠ identyfikacja ukrytego celu

Niech pełny dyskretny LTI ma x=(x1,x2),
x(k+1)=diag(1/2,2) x(k)+(1,0)^T u(k), y(k)=(1,0)x(k).
Zredukowany model x'(k+1)=(1/2)x'(k)+u(k), y'=x'(k) daje IDENTYCZNE y przy każdym u i x'(0)=x1(0), niezależnie od ukrytego x2(0). Obie trajektorie zero-state input-output odpowiadają temu samemu transferowi. Rangi 2x2 controllability i observability pełnego systemu wynoszą 1, a ukryte x2 rośnie według 2^k.

Dla |x2(0)|≤R0 i celu T=x2(N), nawet DOKŁADNY odczyt całej manifest trajektorii nie zmniejsza promienia minimaksowego: R*=2^N R0. Dla N=4,R0=1: 16. Dodanie nowego, źródłowo legalnego pomiaru h=x2(0)+e, |e|≤eta redukuje najgorszy promień do 2^N min(R0,eta), czyli przy eta=1/8 do 2. TO STANDARDOWY test na różnicę rodzaju obserwacji, a nie nowa teoria. 5 przypadków ukrytych stanów i dowolny zamrożony ciąg wejściowy sprawdzono niezależnie w NumPy: PASS, rank controllability=rank observability=1.

Reprodukcja: companion pure Python LT5 ROT21 (w tym samym katalogu). Nie używa oryginalnego DTC runtime i nie ma żadnego fizycznego twierdzenia.

## 4. Co należy PRZESTAĆ robić; konkretny próg dla MT13

1. **STOP:** ponownie dowodzić Chebyshev midrange, różnic klas, profilowania pojedynczego gain czy standardowych chi-bar statistic jako nowego matematycznego wyniku. Są fundamentem. Nowe zastosowanie helpera może pozostać wynikiem KLASOWYM, ale nie przejmuje first-priority.
2. **STOP:** projektować kolejne maski wyłącznie po to, by znaleźć większą pochodną log ratio lub mniejszą średnicę, bez zdefiniowanego rzeczywistego źródła, kosztu, zależności między błędami i porównania z istniejącym bounded-error experiment design. Pronzato–Walter 1989/90 i Karimshoushtari–Novara 2020 są bezpośrednio relevant.
3. **STOP:** traktować opisy identycznych transfer functions jako warunek identyczności ukrytych realizacji przy dowolnych przygotowaniach; klasyczny minimality/observability host już to rozstrzyga.
4. **REVIEW:** realny, konkretny koszt i regularność operacyjnie legalnej obserwacji. Wtedy potencjalny problem mógłby dotyczyć SPECYFICZNEJ klasy źródła i pomiaru NASH, ale jego nowość wymaga osobnego aktualnego theorem-level literature search.
5. **REVIEW:** fizycznie zweryfikowana korelacja błędów masek, legalna wspólna kalibracja źródła oraz held-out kanał; bez nich MT13 ROT037 jest WYŁĄCZNIE wysokiej jakości inferencją wewnątrz zadeklarowanego sztucznego Gaussa.
6. **PRIORITY NEXT:** jeżeli MT13 nie ma źródłowo uzasadnionego nowego modelu obserwacyjnego ani przeczytanego theorem-level prior art, właściwy wynik następnego obrotu brzmi FOUNDATION_ABSORBED/SOURCE_HOLD, nie „nowa hipoteza”.

## 5. Najmniejszy rozsądny następny krok teorii

Wprowadzić jeden rejestr teza→host→różnica pod dokładnymi źródłowymi hipotezami dla trzech wybranych claimów MT13; wymagane: 
(a) jeden theorem-level host w pełnym tekście,
(b) jeden source-pinned self-contained falsifier lub nowa legalna obserwabla,
(c) ostry benchmark poprzedniej teorii,
(d) positive/negative result i 
(e) warunek przerwania.

KANDYDUJĄCE pytanie F1 (NIE twierdzenie o nowości): czy niezależne, źródłowo legalne dane cross-channel i KALIBROWANE zależności błędów nadają się do testu wspólnego źródła, który pozostaje rozstrzygający mimo nieznanego profilu amplitudy? Weryfikować względem Pronzato/Walter oraz nowszej literatury nonlinear set-membership design.
KANDYDUJĄCE F2: jedynie jeśli MT13 zachowa wyraźną różnicę od znanych teorii compositional system identification i legalnych quantum interventions; bez niej absorbować host.
KANDYDUJĄCE F3: nonflat TT geometry, dopiero po host FEEC/York/elliptic operators i wymaganym prawidłowym źródle; affine-flat solved nie jest otwartą nowością.

Priorytet tego obrotu to NEGATYWNY wynik metodologiczny: zidentyfikowano literaturę 1989/1990/2020, która zajmuje większą część dotychczas formułowanego celu "nowa teoria projektowania eksperymentów przez promień informacji". Faktyczny program dalszych badań musi zmienić POMIAR i MODELOWANIE ŹRÓDŁA, a nie tylko nazwę twierdzenia.

## 6. Custody / status

Dokument: publiczny research GitHub, wymagany readback po CREATE. Nie zmieniono roboczej REV021 ani oryginalnej REV020 w tym obrocie — atlas / raport można dołączyć do roboczej bibliografii dopiero po niezależnej merytorycznej recenzji; unikać kolejnego rozrastania się rozdziałów.
Odbiór szczególnie MT13 przez istniejący wątek #iw-dispatch, bez kaskady wymuszonych ACK. GitHub zapis != BW ingestion != scientific adoption != Moderator EXEC.

**DISPOSITION:** THEOREM_LEVEL_OR_HOST_VERIFIED_LITERATURE_REVIEW_PASS / PRIOR_ART_ABSORPTION_FOR_STANDARD_RECOVERY_AND_BOUNDED_ERROR_EXPERIMENT_DESIGN / BEHAVIORAL_SOURCE_SCOPE_NOT_FULL_BOOK / SOURCE_SPECIFIC_FRONTIER_UNKNOWN / PHYSICAL_VALIDATION_HOLD / NO_NOVELTY_NO_CANON_NO_EXEC.
