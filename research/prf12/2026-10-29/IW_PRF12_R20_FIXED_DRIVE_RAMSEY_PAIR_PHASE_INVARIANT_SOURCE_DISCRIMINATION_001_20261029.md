---
artifact_id: IW_PRF12_R20_FIXED_DRIVE_RAMSEY_PAIR_PHASE_INVARIANT_SOURCE_DISCRIMINATION_001_20261029
created_at: 2026-10-29
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
problem_id: PRF12_R19_FIXED_OMEGA_MAX_VS_RESET_AGNOSTIC_SOURCE_DISCRIMINATION
exposure: PUBLIC
canonical_body_path: research/prf12/2026-10-29/IW_PRF12_R20_FIXED_DRIVE_RAMSEY_PAIR_PHASE_INVARIANT_SOURCE_DISCRIMINATION_001_20261029.md
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_TWO_SHOT_PHASE_INVARIANT_BERNOULLI_TEST / EXACT_U1_TWIRLED_HELSTROM_INVARIANT_OPTIMALITY / FINITE_SAMPLE_EXACT_BINOMIAL / ANGLE_AND_STORAGE_ROBUSTNESS / NUMPY_SCIPY_REPRO_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_FIXED_OMEGA_FULL_HARDWARE_PROOF / PREPARATION_READOUT_ASSUMED_IDEAL / RESET_WITHIN_PAIR_BREAKS_TEST / NO_ORIGINAL_THREE_PROBE_SINGLE_COPY_LOCC_GAP / NO_UNQUALIFIED_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# PRF12 R20 — Dwa destrukcyjne pomiary Ramsey'ego zamiast silnego echa: niezmienniczość fazowa i rzeczywisty rachunek zasobów

**Data:** 29 października 2026. **Funkcja:** PRF12. **Werdykt:** uzyskano jawny eksperyment kontrolny odróżniający jedno źródło quasi-statyczne od niezależnych przyrostów Lévy'ego przy całkowitym braku *wewnętrznego impulsu refokusującego*. Powtarzalna losowa miara jest niezależna od każdego skrytego ξ i harmonogramu jego resetów MIĘDZY parami. Koszt stanowią dwa przygotowania i dwa destrukcyjne pomiary na parę. Nie wykazano pełnej zgodności z ograniczoną amplitudą podczas przygotowania ani pomiarów; dlatego nie jest to certyfikat **kompletnego** urządzenia z ograniczonym sterowaniem.

## 0. Genealogia, first owner, dojrzały gospodarz

- PRF11 R35: źródło A = pojedynczy statyczny ξ~Cauchy(0,γ), źródło B = przyrosty Cauchy–Lévy o tych samych jednomarginalnych funkcjach charakterystycznych; oryginalna aparatura SWAP: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R35_NONUNIFORM_SWAP_TIME_GRID_RECOVERS_IDEAL_MEMORY_WITH_CRITICAL_STORAGE_RATE_001_20261025.md .
- PRF12 R16: fazowo-niezależny protokół z trzema kubitami, idealnymi SWAP i losowanymi X/Y: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-29/IW_PRF12_R16_RESET_AGNOSTIC_SOURCE_TEST_AND_SEPARATE_LIFETIME_CALIBRATION_001_20261029.md .
- PRF12 R18: pełny model z aktywnymi źródłami podczas SWAP i kontrprzykład dla jednolitej zgodności w ξ: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-29/IW_PRF12_R18_FULL_THREE_QUBIT_ACTIVE_SWAP_DYNAMICS_CAUCHY_TAIL_CERTIFICATE_001_20261029.md .
- PRF12 R19: nowy jednokubitowy protokół echo z jednym aktywnym impulsem X π, gwarancją dla ośmiu przebiegów przy ΩT≈3927, rosnącym Ω_N T=πN³ w konstrukcji asymptotycznej: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-29/IW_PRF12_R19_FINITE_HAHN_ECHO_RESET_ROBUST_CERTIFIED_SOURCE_DISCRIMINATION_001_20261029.md .
- Zewnętrzny dojrzały gospodarz: Hahn 1950, https://doi.org/10.1103/PhysRev.80.580 ; omówienie losowych pomiarów i korelatorów dwukubitowych w przeglądzie *Analysing quantum systems with randomised measurements*, Physics Reports 2024, https://doi.org/10.1016/j.physrep.2024.09.009 ; klasyczna tomografia i purity z losowanych baz: https://www.nature.com/articles/s41534-024-00857-2 . Kompensacja rozstrojenia sekwencjami CORPSE jest rozwinięta w zewnętrznej literaturze, https://pmc.ncbi.nlm.nih.gov/articles/PMC7005697/ . **Nie zgłaszamy nowości metody dwóch prób, randomizowanych osi ani teorii Helstroma.**

## 1. KONTRAKT ŹRÓDŁA — różni się od R19 i R16

Jedna para eksperymentalna j składa się z dwóch następujących po sobie doświadczeń na **jednym ponownie przygotowywanym sensorze**. Każde doświadczenie: idealnie przygotuj |+>, pozwól swobodnie ewoluować Δ>0 pod ξZ/2 (A) albo Cauchy–Lévy generator (γ/2)(Ad_Z−Id) (B), wykonaj destrukcyjny lokalny pomiar X albo Y. Po pierwszym odczycie resetuj **sensor**, nie źródło zewnętrzne.

A: jedna częstotliwość ξ_j jest identyczna podczas OBU odczytów tej samej pary, mimo resetu sensora, φ_j=ξ_j Δ; możliwa dowolna zależność statystyczna ξ_j pomiędzy kolejnymi parami, nawet perfekcyjne utrzymywanie ξ. Zmienne ξ_j NIE muszą być nawet Cauchy — wynik warunkowy nie zależy od ich rozkładu. Założenie krytyczne: brak resetu źródła POMIĘDZY dwiema ekspozycjami wewnątrz tej samej pary; brak wpływu ukrytego procesu na prywatny los baz. Przy znanej stałej fazie początkowej obu preparacji można przyjąć |+> bez utraty ogólności.

B: każdy odczyt widzi niezależny przyrost stacjonarnego symetrycznego procesu Cauchy–Lévy przez czas Δ. Funkcja charakterystyczna exp(−γΔ)=x. Po przygotowaniu stany są niezależne i oba mają ρ_B=(I+x X)/2. Jeżeli B ma istotnie zależne przyrosty pomiędzy dwoma ekspozycjami, wynik zmienia się — nie wolno tego ignorować.

Przyrząd: jednym wspólnym uczciwym bitem wybieramy oś U=X albo U=Y dla obu odczytów pary. Wyniki s1,s2∈{±1}; zachowujemy jeden bit Z=1[s1=s2]. Nie ma SWAP, sterowanego refokusowania, interlaboratoryjnej komunikacji kwantowej ani magazynowania pierwszego kubitu po pomiarze. Operacje przygotowania |+> i odczytu X/Y są w modelu idealne i nie mają przypisanych skończonych czasów ani gwarantowanego Ω_max. Są to jawne, **niezmodelowane** zasoby sterowania, nie oszustwo rachunkowe.

## 2. Twierdzenie R20.1 — niezmienniczy względem ξ bit i jego dokładne prawa

Dla fazy φ=ξΔ mamy |ψ_φ>=(|0>+exp(iφ)|1>)/sqrt(2). Dwa idealnie niezależne przy wspólnym φ wyniki pomiaru X dają korelację E[s1s2|φ,X]=cos²φ, a dla Y E[s1s2|φ,Y]=sin²φ. Ponieważ P(Z=1)=(1+E[s1s2])/2, losowanie X/Y po 1/2 daje bez żadnego uśredniania po ξ:

 p_A:=P(Z=1|A,ξ_j,cała historia)=1/2+[cos²φ_j+sin²φ_j]/4=3/4.   (R20.1)

B ma korelację XX równą x², YY równą zero; stąd

 p_B:=P(Z=1|B)=1/2+x²/4=(2+exp(-2q))/4, q=γΔ.     (R20.2)

Zatem Δp=(1-exp(-2q))/4>0 dla każdego q>0. **Ponieważ** Z_j mają identyczną warunkową dystrybucję Bernoulliego 3/4 dla każdego ξ_j i losowanie baz/preparacja/odczyt są niezależne pomiędzy parami, bezwarunkowa sekwencja Z_j jest iid pod A dla ARBITRALNIE SKORELOWANEJ historii ξ_j. Pod B niezależność przyrostów i przygotowań zapewnia iid Bernoulli p_B. Nie wolno automatycznie przenosić tego na zepsuty zegar, zresetowane źródło wewnątrz pary ani niekontrolowane bazowe błędy względne.

Ogólnie bezwzględny kierunek wybranych baz jest nieistotny: losujemy jedną z dowolnych dwóch **wzajemnie prostopadłych** osi w płaszczyźnie X–Y. Dla nieznanej wspólnej fazy przesuniętej względem obu osi wciąż zachodzi cos²θ+sin²θ=1. Brak absolutnej referencji fazy nie przeszkadza; wymagana jest powtarzalna względna ortogonalność ustawień i ten sam wybór osi dla obu pomiarów danej pary.

## 3. Twierdzenie R20.2 — ścisła optymalność w U(1)-niezmienniczej klasie, nie całego problemu

Efekt odpowiadający decyzji zgodności po wymazaniu etykiety losowanej bazy ma operatorową postać

 E=I_4/2+(X⊗X+Y⊗Y)/4.                                  (R20.3)

Ma widmo (0,1/2,1/2,1); jest pozytywny, dopełnienie też jest pozytywne, a implementacja to prosta mieszanina dwóch **separowalnych pomiarów projektorowych** XX i YY z klasyczną funkcją parzystości. E komutuje ze wspólnym obrotem fazy U(φ)^{⊗2}. Po matematycznym U(1)-twirlingu obu stanów

 ρ_A^twirl=I_4/4+(XX+YY)/8,
 ρ_B^twirl=I_4/4+x²(XX+YY)/8,
 D^twirl=(1−x²)(XX+YY)/8.                                  (R20.4)

D^twirl ma eigenvalues [−(1−x²)/4,0,0,+(1−x²)/4], więc

 TV_Helstrom(ρ_A^twirl,ρ_B^twirl)=(1−x²)/4=Tr(E D^twirl).  (R20.5)

Zatem test osiąga Helstroma dla **dwóch celowo stwirlowanych stanów**, co dowodzi optymalności w klasie binary decision effects niezmienniczych względem wspólnej fazy. NIE jest to pełna granica Helstroma oryginalnej niesymetryzowanej pary przy znanej wspólnej referencji, ani twierdzenie o najbardziej efektywnym protokole z dowolnymi efektami lub adaptacyjnymi metodami.

## 4. Dokładny koszt liczby prób, czasu i informacji Chernoffa

Jedna para = dwa niezależnie przygotowane i zmierzone kubity, łączny czas swobodny T_pair=2Δ=2q/γ. Dla N par N-bitowy rozkład wylosowanego Z jest iid Bernoulli p_A i p_B pod obydwoma hipotezami. Przy równych priorach i 0<p_B<p_A<1 wybieramy A wtedy i tylko wtedy, gdy liczba zgodnych par K≥k, z

 k=ceil(N log[(1−p_B)/(1−p_A)]/[log(p_A/p_B)+log((1−p_B)/(1−p_A))]).

Średni błąd jest dokładnie [BinomCDF(k−1;N,p_A)+BinomSF(k−1;N,p_B)]/2. Błędy warunkowe występują oddzielnie jako obydwa składniki.

Dla q=.5 (czyli γT_pair=1): p_A=.75, p_B=.5919698602928606, Δp=.1580301397071394.
- N=93: średni błąd .0505014261214 (NIE wystarcza).
- N=94: k=64, średni błąd .0494672406058, ale błąd pod A .0507407273528 (>5%).
- N=97: k=66, błąd pod A .0475614169244, pod B .0461343689415: OBA <5%. Dokładny skan N=1..97 potwierdza pierwszy taki N.
- Przy q=.579, N=80: k=54, błąd pod A .049887178375, pod B .049727230084; zużycie N*T_pair=92.64/γ, tylko 160 lokalnych pomiarów. To jawny wygodny punkt, NIE dowód globalnie najkrótszego kalendarza po wszystkich harmonogramach.

Znormalizowana na całkowity czas swobodny liczba Chernoffa wynosi C(q)/(2q), gdzie C(q)=−log min_{0≤s≤1}[p_A^s p_B^{1−s}+(1−p_A)^s(1−p_B)^{1−s}]. Niezależna optymalizacja numeryczna daje q≈.5895129 i C(q)/(2q)≈.0145410. Ten rezultat jest asymptotycznym *względnym* benchmarkiem dla **jednakowych czasów ekspozycji w każdej parze**, nie dowodem globalnej optymalności nad adaptacyjnymi niejednorodnymi harmonogramami ani przy kosztach SPAM. Teorię Chernoffa i różnicę między dawką a liczbą prób stosuje się standardowo.

**Porównanie R16/R19 ma różne zasoby:** R16 w idealnym trójkubitowym SWAP przy γT=1 i zerowym wieku pamięci używał 80 przebiegów i 240 lokalnych odczytów do średniego błędu <5%, ale zawierał dwa SWAP na przebieg. R19 pojedynczy echo pi używał ośmiu przebiegów, lecz certyfikował oba błędy <5% tylko przy ΩT≈3927. R20 dla q=.579 używa 80 par, 160 odczytów, żadnego SWAP ani refokusowania, lecz reset sensora i dwa oddzielne odczyty wymagają sprawnej realizacji. R20 nie dowodzi przewagi w jednakowej cenie fizycznej.

## 5. Twierdzenie R20.3 — rozdzielone źródła, nierówne ekspozycje i znane niedoskonałości

**Negatywny falsyfikator #1: reset ξ WEWNĄTRZ pary.** Jeśli w A dwie ekspozycje dostają niezależnie ξ_1,ξ_2~Cauchy(0,γ), to ich średnie stany wynoszą ρ_x⊗ρ_x, dokładnie jak w B. ŻADEN dwukubitowy efekt nie rozróżnia wtedy stanów bez dodatkowej informacji. R20.1 staje się nieprawdziwe, a test traci kontrast. Nie wolno mylić dowolnego resetowania MIĘDZY parami z niezależnym resetowaniem WEWNĄTRZ nich.

**Negatywny falsyfikator #2: różne czasy ekspozycji.** Przy Δ_1≠Δ_2, wspólne ξ generuje fazy φ_1=ξΔ_1 i φ_2=ξΔ_2; dla idealnie prostopadłych osi

 P_A(Z=1|ξ)=1/2+cos[ξ(Δ_1−Δ_2)]/4.             (R20.6)

Nie jest to stała w ξ. Dla ξ(Δ_1−Δ_2)=π spada aż do .25. Nawet dowolnie mała, lecz NIEZEROWA nierówność czasów może wywołać taki wynik dla dalekiego ξ; nie ma jednostajnej gwarancji wobec nieograniczonej częstotliwości, analogicznie do R18/R19. Dla rozkładu Cauchy efekt ma małe prawdopodobieństwo przy małej nierówności, ale to wymaga odrębnego oszacowania i nie odtwarza R20.1 dokładnie.

**Dopuszczalne tłumienie koherencji i SPAM visibility**: jeżeli podczas obu ekspozycji lokalne, niezależne i fazowo-kowariantne straty zmniejszają długości wektorów Blocha o d_1,d_2∈[0,1], wtedy

 p_A=1/2+d_1d_2/4,
 p_B=1/2+d_1d_2 e^(−2q)/4,
 Δp=d_1d_2(1−e^(−2q))/4.                            (R20.7)

Bezwzględna wspólna rotacja referencji pozostaje niewidoczna. Jeśli druga baza odchyla się od dokładnej prostopadłości o |ε|, warunkowe prawdopodobieństwo pod A może zależeć od fazy, lecz dla KAŻDEJ fazy otrzymujemy

 p_A(ξ)≥1/2+d_1d_2(1−|sin ε|)/4,
 p_B≤1/2+d_1d_2 e^(−2q)(1+|sin ε|)/4.               (R20.8)

Dlatego dodatni znak kontrastu dla wszystkich ξ jest zagwarantowany, gdy

 |sin ε| < [1−e^(−2q)]/[1+e^(−2q)] = tanh(q).       (R20.9)

Dla q=.5, d_1=d_2=1, ε=.02 rad, konserwatywna dolna granica wynosi Δp≥.15119119845. Zakładając niezależność pomiarów warunkowo względem dowolnej historii ξ oraz prywatnych losowań osi, próg w połowie przedziału [p_B^max,p_A^min] i nierówność Hoeffdinga dają oba błędy najwyżej exp(−NΔp²/2), co jest <.05 dla N≥263. To jest ograniczenie konserwatywne, nie dokładne optimum. Sam nierówny czas Δ_1≠Δ_2 NIE należy do tej tolerancji względnego kąta.

**Niezmodelowane zasoby:** realne przygotowania kubitu, obrót baz, odczyt i reset trwają niezerowy czas, mogą działać pod źródłem i wymagają Ω_max. Dodatkowy czas może naruszyć kluczowy kontrakt stałości ξ wewnątrz pary. R20 pokazuje usunięcie WYŁĄCZNIE mocnego impulsu refokusowania i brak potrzeby koherentnej pamięci; nie dowodzi kompletnego ograniczenia amplitudy wszystkich sygnałów sterujących.

## 6. Kontrola R19 pod stałym ograniczeniem mocy — co R20 faktycznie poprawia

Dla ośmiu przebiegów R19, γT_phys=1 i prostokątnego echa τ=π/Ω, konserwatywny certyfikat błędu A używa kwantyla Cauchy i parametru δ. Niezależna minimalizacja tylko tego bezpiecznego oszacowania daje:

| ΩT | τ/T | najlepsza UPPER bound błędu A w R19 (N=8) |
|---:|---:|---:|
| 100 | .031416 | .5408 |
| 1000 | .003142 | .1151 |
| 3000 | .001047 | .05493 |
| 3500 | .000898 | .04953 |
| 3927 | .000800 | .04584 |

Wartość >.05 oznacza wyłącznie brak certyfikatu tą metodą, a nie dowód że taki eksperyment nie może działać. Źródłem nowego zasobu R20 są dwa idealne odczyty z jednakowym ξ w obrębie pary; brak rozbudowanego π echa nie dowodzi możliwości realizacji szybkich pomiarów przy ΩT=100. Dla realnego urządzenia najpierw trzeba zmierzyć/założyć czasy SPAM, dostępne osie, drift zegara i źródła; dopiero potem porównywać całkowity budżet czasu i mocy.

## 7. Odtwarzalność, source typing, niezależny referee

Samodzielny program Python 3 + NumPy + SciPy odtwarza całe twierdzenie, nie importując PRF12 R16-R19: 
IW_PRF12_R20_RAMSEY_PAIR_PHASE_INVARIANT_REPRO_001_20261029.py.

Testy: 307 różnych ukrytych faz × 3 obroty absolutnej bazy; 7 wartości q sprawdzonych przez bezpośrednie produkty macierzy 4×4; dokładna diagonalizacja stwirlowanego D i saturacja granicy Helstroma; pełny rozkład dwumianowy i minimalne N dla celów .05; numeryczne maksimum szybkości Chernoffa na jednostkę czasu; 103 × 100 punktów fazy i referencji w teście niedoskonałej ortogonalności; kontrprzykład różnego czasu ekspozycji ξ(Δ2−Δ1)=π. Tabela porównawcza ograniczenia R19 obliczona osobno.

**Niezależna kontrola nie jest jeszcze niezależną recenzją.** Recenzent ma sprawdzić: dokładne rozdzielenie wspólnej fazy A i przyrostów B podczas *dwóch* kolejnych ekspozycji, warunkową niezależność ponownej preparacji, weryfikację pA bez uśredniania po źródle, U(1) twirling (nie podstawiać go za prawdziwą state tomography), minimalne N i kwalifikację Ω podczas SPAM; nie przenosić R20 na oryginalny trzypróbkowy bezkontrolny pomiar ani single-copy closure LOCC. Literaturowe prior-art randomized measurements i Ramsey purity należy uwzględnić przed jakimkolwiek claimem nowości.

**Werdykt:** EXACT_TWO_SEQUENTIAL_RAMSEY_PHASE_INVARIANCE / NO_ECHO_AND_NO_QUANTUM_MEMORY / U1_INVARIANT_HELSTROM / CONDITIONAL_HISTORY_IID / EXACT_94_97_AND_80_579_RESOURCES / NUMERIC_CHERNOFF_PER_TIME / RESET_WITHIN_PAIR_NO_GO / UNEQUAL_DURATION_FAR_TAIL_FALSIFIER / AXIS_AND_VISIBILITY_CERTIFICATE / FIXED_OMEGA_FOR_PREP_READOUT_UNPROVEN / REFEREE_PENDING / NO_CANON / NO_EXEC / NO_NOVELTY / ORIGINAL_THREE_QUBIT_SINGLE_COPY_LOCC_CLOSURE_OPEN / GITHUB_PENDING_BW_INGEST.
