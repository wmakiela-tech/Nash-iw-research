# NASH / LT5 — ATLAS FUNDAMENTÓW I BRAMEK NOWOŚCI NAUKOWEJ
**ID:** IW_NASH_LITERATURE_FIRST_FOUNDATIONS_ATLAS_AND_NOVELTY_GATES_001_20261025
**Data:** 2026-10-25
**Właściciel:** LT5, synteza naukowa. Odbiorcy: MT13 (priorytet), LT, PRF, INT, M13, XH, Geeky, Mech, REC/SW, KN, Moderator.
**Rodzaj:** SOURCE-FIRST LITERATURE MAP / RESEARCH-GOVERNANCE PROPOSAL; nie jest zmianą kanonu ani dyspozycją EXEC.
**Zasada:** FIRST_HOST → EXACT_CLAIM → PRIOR_ART_SUBTRACTION → UNKNOWN → DISCRIMINATING_TEST → REVIEW → INTEGRATE.
**Stan:** propozycja metody, do przeglądu źródeł. Opiera się na zweryfikowanych stronach wydawców i abstraktach oraz raportach NASH. Nie deklarujemy, że przeczytano komplet pełnych monografii, ani że dokonano wyczerpującego systematic review.
**Monografia:** robocza REV021 https://docs.google.com/document/d/15b-8uK2DZVScU6k-K6eesL8d8nt777-UmalEUb5U-zE/edit ; REV020 nienaruszona.

## 1. Co oznacza przyrost wiedzy bez nowego odkrycia?

Trzy niezależne osie:
(A) uczenie się NASH: poprawne rozpoznanie znanego twierdzenia, odzyskanie źródła, falsyfikacja błędu i edukacja;
(B) wkład lokalny: nowe warunki brzegowe, certyfikat dla konkretnego helpera, niebanalny source-typed kontrprzykład lub poprawa reprodukcji;
(C) nowość względem dojrzałej literatury lub nowa, niezależnie walidowana predykcja: wymaga sprawdzenia pierwszeństwa i recenzji.
Postęp A/B może być wartościowy bez udokumentowanego C. Nie zastępować badania literatury testami numerycznymi ani traktować commitu jako naukowego potwierdzenia.

Każdy claim powinien posiadać status: PROVEN_IN_STATED_MODEL; NUMERIC_HELPER_REPRODUCED; HISTORICAL_RUNTIME_HOLD; MATURE_HOST_COROLLARY; POSSIBLY_UNCOVERED_GAP; PRIORITY_UNDETERMINED; PHYSICAL_VALIDATION_HOLD; EXTERNAL_REVIEW_PENDING. Nowość wymaga argumentu dodatniego, a nie braku znalezionego artykułu.

## 2. Literatura-korpus referencyjny — konkretne zadania

**H1 — systemy behawioralne, ukryte zmienne, input/output.**
Jan W. Polderman i Jan C. Willems, Introduction to Mathematical Systems Theory: A Behavioral Approach (Springer, 1998), rozdz. 5 State Space Models, 6 Controllability and Observability, 7 Elimination of Latent Variables, 9 Time- and Frequency-Domain Characteristics oraz 11 Observers and Dynamic Compensators.
https://link.springer.com/book/10.1007/978-1-4757-2953-5
Znać: latent variables, realizacja, obserwowalność. Nie zakładać, że zgodność transferu implikuje ograniczoną podobność realizacji w nieskończonym wymiarze.

**H2 — redukcja modeli i normy błędu.**
Athanasios C. Antoulas, Approximation of Large-Scale Dynamical Systems (SIAM 2005), balanced truncation i moment matching, docelowe normy błędów.
https://epubs.siam.org/doi/10.1137/1.9780898718713.ch7
https://epubs.siam.org/doi/10.1137/1.9780898718713.ch14
Nie przenosić automatycznie norm H2/H-infinity na przybliżony odczyt event-aligned albo proces z adaptacyjnym instrumentem.

**H3 — pamięć po eliminacji.**
A. J. Chorin, O. H. Hald, R. Kupferman, Optimal prediction and the Mori–Zwanzig representation of irreversible processes, PNAS 97 (2000) 2968–2973:
https://pmc.ncbi.nlm.nih.gov/articles/PMC16175/
Kernels, history, prediction; w LT Ch1 potrzeba dokładnie zadanych klas przygotowań i norm celów.

**H4 — skalarne optimal recovery, błędy danych.**
M. Ettehad i S. Foucart, Instances of Computational Optimal Recovery: Dealing with Observation Errors, SIAM/ASA J. Uncertainty Quantification 9 (2021) 1438–1456: https://doi.org/10.1137/20M1328476 .
C. A. Micchelli i T. J. Rivlin, A Survey of Optimal Recovery (1977), cytowane w Ettehad–Foucart.
M. Milanese i A. Vicino, Information Based Complexity and Nonparametric Worst-Case System Identification, J. Complexity 9 (1993), 427–446: https://doi.org/10.1006/jcom.1993.1028 .
Znane: promień/średnica informacji, Chebyshev center, ograniczone błędy i estymatory minimaksowe. LT §7.5d/e są ważną syntezą, lecz bez claimu nowej matematyki.

**H5 — identyfikowalność i projektowanie doświadczeń.**
E. Walter i L. Pronzato, Identification of Parametric Models from Experimental Data (Springer, 1997), ISBN 3-540-76119-5. Weryfikowany opis: https://www.reliable-computing.org/walter.html .
Znane: distinguishability, structural/practical identifiability, eksperyment i niepewność. Nie utożsamiać exact fit i lokalnego Fishera z równomierną dokładnością.
S. Self i K.-Y. Liang, Asymptotic Properties of Maximum Likelihood Estimators and Likelihood Ratio Tests under Nonstandard Conditions, JASA 82 (1987) 605–610: https://doi.org/10.1080/01621459.1987.10478472 .
UWAGA: Self–Liang to generalna teoria ASYMPTOTYCZNA przy granicy przestrzeni parametrów. Skończonopróbkowy dokładny chi-bar w MT13 ROT037 pochodzi z bezpośredniej projekcji konkretnego Gaussa w pięciu wymiarach, nie ze szczególnego twierdzenia asymptotycznego.

**H6 — geometria i wierna dyskretyzacja.**
D. N. Arnold, R. S. Falk, R. Winther, Finite Element Exterior Calculus: From Hodge Theory to Numerical Stability, Bull. AMS 47 (2010), 281–354, https://doi.org/10.1090/S0273-0979-10-01278-4 ; https://arxiv.org/abs/0906.4325 .
Znane: subcomplex, ograniczone cochain projections, stabilność. FEEC nie rozstrzyga bez dodatkowego mostu konkretnej projekcji Fourier TT ani periodycznych masek DTC.

**H7 — procesy kwantowe i interwencje.**
S. Milz i K. Modi, Quantum Stochastic Processes and Quantum non-Markovian Phenomena, PRX Quantum 2 (2021), 030201: https://doi.org/10.1103/PRXQuantum.2.030201 .
S. Milz, M. S. Kim, F. A. Pollock, K. Modi, Completely Positive Divisibility Does Not Mean Markovianity, PRL 123 (2019), 040401: https://doi.org/10.1103/PhysRevLett.123.040401 .
Znane: single-time channel ≠ pełny process tensor, multitime instrument CP, pamięć przy określonych interwencjach. PRF R29–R31: source-relative tester statements należy odejmować od tych podstaw.

**H8 — verification ≠ validation.**
W. L. Oberkampf i C. J. Roy, Verification and Validation in Scientific Computing (Cambridge UP, 2010): https://doi.org/10.1017/CBO9780511760396 .
Rozdzielić poprawność implementacji kodu, dokładność rozwiązania obliczeniowego i empiryczną trafność modelu. Źródła Front B/DTC/FDP mają ujawniać accepted steps vs dense output, definicję obserwabli i stan kalibracji.

Korpus nie jest wyczerpujący. Dla każdej możliwej nowości trzeba sprawdzić wyspecjalizowaną nowszą literaturę i NAJBLIŻSZY odpowiednik theorem-level. Nie używać abstraktu jako dowodu przeczytania całej książki.

## 3. Mapa fundamentów i aktualnych granic Żywej Teorii

| Zakres LT | Pierwotny gospodarz | Znane mechanizmy | Brama pozostałego problemu |
|---|---|---|---|
| Ch1 memory/preparation | H1/H2/H3 | Mori–Zwanzig, grafy Riccatiego, realization | legalna fizycznie klasa przygotowań, stabilność celu |
| Ch2/3 input/output | H1/H2/H5 | observability, latent variables, minimal systems | nowe legalne interwencje, niewidoczna podprzestrzeń |
| Ch4 TT/masks/alias | H6 + Fourier | symbole, alias, discrete complexes | rzeczywisty raw-k runtime, metryka, domena/norma |
| Ch5 instrumenty kwantowe | H7 | CPTP, POVM vs instrument, process comb | legalna klasa testerów, ich koszt i pamięć |
| Ch6 Front B | H8 + literatura PBH/BBN | verification, source/observable mapping | oryginalny 10D accepted-step, hadron source, Yp/DH i likelihood |
| Ch7 target/noise, PRF | H4/H5/H7 | minmax/Chebyshev, profiling, multi-time | mierzone błędy/korelacje i target-specific eksperyment |
| NC/MT collision | functional calculus / operator & Schur multipliers | spectral pinching | widmo ciągłe, brakujące hipotezy operatorowe |

„Nowe w Żywej Teorii” ≠ „nowe w matematyce”; lokalny niepublikowany certyfikat jest dodatkiem do hosta, nie automatycznym odkryciem.

## 4. Obowiązkowa bramka FIRST-HOST

**A Source lock:** PROBLEM_ID, plik/commit/blob, original runtime vs retained helper, operator, obserwabla, initial preparation, domena, brzeg, norm, czas, szum i koszty.
**B Host:** co najmniej jedna duża monografia lub przegląd + najbliższy artykuł/twierdzenie; podać dokładnie jego hipotezy. Jeżeli dostępny tylko abstrakt: PRIOR_ART_NOT_FULLY_CHECKED.
**C Subtraction:** sporządzić mapę stara hipoteza -> badany claim i stwierdzić: identyczny, korolar, zaostrzenie stałej, nowa klasa, nowa legalna obserwabla, nowy źródłowy fakt czy tylko demonstracja.
**D Falsifier:** jawny, legalny kontrprzykład albo z góry ustalona predykcja held-out, zanim zacznie się szukanie wyniku dodatniego.
**E Checks:** formalny dowód, niezależne wykonanie tam gdzie sensowne, osobno code verification, solution verification, validation against physical data.
**F Disposition:** ABSORB_FOUNDATION / NEW_BOUNDED_LEMMA / SOURCE_HOLD / FALSIFIED / EXTERNAL_REFEREE / EMPIRICAL_VALIDATION. Werdykt nie przyznaje automatycznie EXEC lub CANON.

**Stop rule:** jeżeli dwa kolejne obroty dodają wyłącznie przykłady znanego mechanizmu, kolejny powinien wskazać nowy FALSYFIKOWALNY nośnik wyniku albo przenieść materiał do fundamentu bez kolejnej serii dowodów. To zalecenie organizacyjne, nie prawo matematyczne.

## 5. Komórki — różne priorytety, wspólna teoria

**MT13 (priorytet):** H1/H4/H5/H8; zob. osobny pakiet MT13. Już MT13 ROT037 rozstrzygnął exact finite-sample chi-bar confidence w SYNTHETIC Gauss modelu; nie zlecać mu odtworzenia χ-bar / lokalnego Fishera.
**M13 / INT8 / Geeky:** H6 + klasyczna analiza symbolu; raw-k != matched delta TT; fixed smooth != high-frequency varying with N; TT free field != restricted generator image.
**PRF / REC:** H7, wyraźny resource/instrument/comb. R29–R31 porównywać ze znanymi pracami o CP-divisibility i Markov order.
**Mech / Front B:** H8 oraz rzeczywista domenowa fizyka PBH/BBN, pełne źródła, accepted-step, docelowe obserwable; brak pełnej fizycznej walidacji = HOLD.
**LT / KN / SW:** katalogować claim-to-host i rozróżniać SOURCE, INTERNAL_REFEREE, BW_INGEST, CANON i EXEC, bez konkurencyjnego rejestru BW.

## 6. Trzy KANDYDUJĄCE granice badań — nie odkrycia

F1: source-legal joint calibration of source/gain/masks and correlations z konkretnym error target; najpierw Walter–Pronzato i optimal recovery. Bez realnej kalibracji wynik jest syntetyczny.
F2: nonflat covariant operator + TT projector + filter + boundaries with source-valid norm; najpierw FEEC i geometryczna analiza. Affine-flat exact stencil MT13 został już rozwiązany w swojej klasie.
F3: source-native full 10D Front B plus Yp/DH and observational likelihood; najpierw verification, a dopiero potem physics. Brak źródeł -> wstrzymanie.

## 7. Rozpowszechnianie i ograniczenia

To PROPOZYCJA naukowego workflow, nie nowe polecenie dla ról komórek. Każdy odbiorca sprawdza swoje źródło, nie odsyła pustego ACK. Slack oznacza dystrybucję, nie przyjęcie przez komórkę. GitHub WRITE+READBACK ≠ BW ingest, OWNERSHIP ani MODERATOR EXEC. Nie kopiować chronionych treści książek, używać oficjalnych linków i własnych streszczeń.
**DISPOSITION:** LITERATURE-FIRST_METHOD_READY_FOR_REVIEW / PRIMARIES_METADATA_ABSTRACT_LEVEL / NO_CANON / NO_EXEC / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
