---
artifact_id: IW_PRF12_R02_FINITE_DURATION_SWAP_CAUCHY_ACTIVE_PULSES_AND_RESOURCE_GATE_001_20261026
created_at: 2026-10-26
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
problem_id: PRF12_R01_FINITE_DURATION_SWAPS_WHILE_SOURCE_ACTIVE
exposure: PUBLIC
canonical_body_path: research/prf12/2026-10-26/IW_PRF12_R02_FINITE_DURATION_SWAP_CAUCHY_ACTIVE_PULSES_AND_RESOURCE_GATE_001_20261026.md
sync_state: GITHUB_PENDING_BW_INGEST
status: SOURCE_TYPED_DERIVATION_LOCAL / EXACT_2Q_PULSE_CONTROLS_PASS / TIMING_GRID_NUMERIC_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_HARDWARE / NO_GLOBAL_OPTIMUM / NO_FIXED_KAPPA_RECOVERY / NO_FULL_HANDOFF_REHYDRATION
function: SCIENCE_FIRST / FOUNDATION_FIRST / INTERNAL_EXTERNAL_PRIOR_ART / NEGATIVE_KNOWLEDGE_PRESERVING / FALSIFIER_FIRST
---

# PRF12 R02 — Skończony czas SWAP przy aktywnym szumie Cauchy'ego: bramka energetyczna, jawny model impulsu i granica Helstroma

**Data:** 26.10.2026. **Właściciel obrotu:** PRF12. **Rodzaj:** matematyczny model syntetyczny i lokalne kontrole skończenie-wymiarowe; bez demonstracji fizycznej. **Główny status:** dowód warunkowy dla jawnego harmonogramu i dwóch zadeklarowanych modeli źródłowych, oczekuje niezależnej recenzji.

## 0. Źródła i odejmowanie dojrzałego gospodarza

**Pierwszeństwo lokalnych rezultatów:**
- PRF11 R29–R35: statyczny jednokrotnie losowany parametr fazy ξ ~ Cauchy(0,γ) przeciw niezależnym przyrostom Cauchy–Lévy; asymptotyczny problem SWAP, warunek pamięci i krytyczny wiek. Kluczowy **PRF11 R35**: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R35_NONUNIFORM_SWAP_TIME_GRID_RECOVERS_IDEAL_MEMORY_WITH_CRITICAL_STORAGE_RATE_001_20261025.md (odczyt SHA Git blob 3d8dda56a401c5fce1d1ab9f0f280c4127a6caf0).
- **PRF12 R01**: abstrakcyjny minimalny odstęp i mechanizm usuwania wieku przez nieliniowy zegar; niezależnie policzone wybrane przykłady; ogólny budżet błędów SWAP w normie diamentowej: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R01_CLOCK_BUDGET_GATE_ERRORS_AND_TWO_TIER_SCHEDULE_001_20261026.md (Git blob 62fca37133c520bec6e6e16014b68e12c08082c6). Ten raport NIE jest powtórzeniem wyniku R01, lecz jawnym wprowadzeniem czasu trwania i szumu *podczas* impulsu.
- PRF11 R34 o ustalonej siatce i różnych czasach magazynowania: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R34_AGED_MEMORY_SHARP_VISIBILITY_POINT_PROCESS_AND_LABEL_SUFFICIENCY_001_20261025.md (odczyt SHA 531ef738cb98ec5438a3c1f2ba555456d968b4c4).

**Wcześniejsza zewnętrzna matematyka:**
- Farmanian i Karimipour, *Quantum speed limits for implementation of unitary transformations*, Phys. Rev. A 110, 042611 (2024), DOI https://doi.org/10.1103/PhysRevA.110.042611 — ograniczenia czasu realizacji unitarnego operatora.
- *The roles of drift and control field constraints upon quantum control speed limits*, New J. Phys. 19 (2017), DOI https://doi.org/10.1088/1367-2630/aa8242 — nierówności Duhamela i kontrola czasu/amplitudy, także przykłady SWAP.
- *Quantum speed limits from symmetries in quantum control*, J. Phys. A (10 lutego 2026), DOI https://doi.org/10.1088/1751-8121/ae3f68 — współczesna, zewnętrzna analiza limitów czasu i symetrii przy bramkach, w tym SWAP w innym układzie.
- *Practical Introduction to Benchmarking and Characterization of Quantum Computers*, PRX Quantum **6**, 030202 (2025), DOI https://doi.org/10.1103/PRXQuantum.6.030202 — zachowawcze sumowanie błędów diamentowych bramek.

To są źródła dla **metod**, nie dowody, że model R02 jest oryginalny. R02 nie rości pierwszeństwa dla Duhamela, limitu prędkości, SWAP, Lévy dephasing ani harmonogramów sterowania.

## 1. Pełny kontrakt mikromodelu

Niech T>0, a=γT>0 i β≥0. Eksperyment obejmuje n≥2 ekspozycji, n−1 SEKWENCYJNYCH, niepokrywających się impulsów SWAP oraz lokalny końcowy odczyt X, ewentualnie dowolne końcowe POVM. n kubitów startuje w stanach |+>. Na aktywnym kubicie systemowym S w wolnych okresach działa:

A: jeden wspólny i NIEOBSERWOWANY ξ~Cauchy(0,γ) przez cały przebieg, H_A,free=ξ Z_S/2;
B: niezależne stacjonarne przyrosty symetrycznego procesu Cauchy–Lévy, z uśrednioną generatorką \(\mathcal D_\gamma(\rho)=\gamma(Z_S\rho Z_S-\rho)/2\).

Dla każdej bramki SWAP na parze (S,M_j) wybieramy **konkretny** Hamiltonian:
\[
H_{0,n}={\pi\over2\tau_n}S_{S,M_j},\qquad
e^{-i\tau_n H_{0,n}}=-iS_{S,M_j}.
\]
Globalna faza -i nie ma znaczenia dla kanału. Jest to przykładowa rodzina impul­sów, NIE twierdzenie, że rzeczywisty sprzęt realizuje dowolny Hamiltonian proporcjonalny do SWAP.

**Podczas bramki źródło wciąż działa na S:**
A: \(H_{A,\rm pulse}=H_{0,n}+\xi Z_S/2\), z TYM SAMYM ξ co w wolnych odstępach;
B: proces markowowski \(\dot\rho=-i[H_{0,n},\rho]+\mathcal D_\gamma(\rho)\), czyli szum Cauchy–Lévy na S również podczas bramki.

Po ukończeniu impulsu j próbka j zostaje w pamięci M_j i do końcowego odczytu podlega niezależnej dekoherencji \(r_j=\exp[-\kappa_n(T-t_j)]\), gdzie \(\kappa_n T=\beta/n\), \(t_j\) to fizyczny koniec impulsu. Stare rejestry pamięci nadal starzeją się podczas kolejnych wolnych ekspozycji i impulsów. Świeżo przydzielone rejestry są przygotowane jako |+>. Brak resetu wymagającego dodatkowego czasu, sprzężenia ξ z elektroniką, błędów krosowych, ograniczeń topologii, odczytu w trakcie eksperymentu i awarii źródła.

**Nie wolno** zastępować procesu B w trakcie bramki niezależnym losowaniem *jednej* fazy na cały impuls bez dowodu: przy niekomutującym SWAP te dwa modele różnią się. W R02 B jest explicite procesem Lévy/semigrupą Lindblada w całym fizycznym czasie.

## 2. Kontrakt czasu i referencyjny idealny protokół

Wybierz n−1 impul­sów o jednakowym \(\tau_n>0\). Ich łączna długość i czas wolnej ekspozycji:
\[
L_n=(n-1)\tau_n<T,\quad F_n=T-L_n,\quad s_n=L_n/T.
\]
Niech \(\Delta_j>0\), j=1..n, \(\sum_j\Delta_j=F_n\). W bloku j<n kubit S najpierw jest swobodnie eksponowany przez \(\Delta_j\), następnie przechodzi przez impuls SWAP długości \(\tau_n\). W ostatnim bloku n występuje tylko wolna ekspozycja \(\Delta_n\). Po bramce j czas fizyczny wynosi
\[
t_j=\sum_{i\le j}\Delta_i+j\tau_n.
\]

**Referencja R:** te same fizyczne okresy i te same końcowe czasy \(t_j\), ale generator źródła jest WYŁĄCZONY na każdym z n−1 impulsów. Bramki pozostają bezbłędne, pamięć starzeje się do T w obu procesach. Referencja ma zatem \(\gamma F_n\), nie \(\gamma T\); jest źródłowo różna od idealnego R35 przy T i tylko w granicy \(L_n/T\to0\) można ją utożsamić z pierwotnym celem.

Znormalizowana wolna siatka \(d_j=\Delta_j/F_n\), \(\sum d_j=1\). Ustal:
\[
E_n=\sum_j d_j^2,\quad
P_n=\prod_j{1+e^{-\gamma F_n d_j}\over2},\quad
z_n=\gamma F_n\sqrt{E_n}.
\]
Niech \(u_j=(T-t_j)/T\) dla j<n oraz \(u_n=0\), i \(A_n^{\rm phys}=n^{-1}\sum_j u_j\).

Referencyjne stany mają **dokładnie** tę samą postać macierzy co w R35 dla ekspozycji \(\Delta_j\) i niezależnych \(r_j=e^{-\beta u_j/n}\). Dowód R35, wykorzystujący \(\sum_j(1-r_j)\le\beta A_n^{\rm phys}\), daje:
\[
2(1-P_n)-\varepsilon(z_n)-2\beta A_n^{\rm phys}
\le D_n^R\le2(1-P_n)+\varepsilon(z_n), \tag{R}
\]
gdzie \(D=\|\rho_A-\rho_B\|_1\) i
\[
\varepsilon(z)={z\over\pi}\ln(1+4/z^2)+{4\over\pi}\arctan(z/2),\quad \varepsilon(0)=0.
\]

## 3. Lemat R02.1: działające źródło podczas SWAP daje jawny błąd końcowy

**A, wspólna statyczna Cauchy.** Warunkowo względem wartości ξ Duhamel daje, przy jednym impulsie:
\[
\|U_{A,\xi}-U_0\|_{\rm op}\le |\xi|\tau_n/2;
\quad \|\operatorname{Ad}_{U_{A,\xi}}-\operatorname{Ad}_{U_0}\|_\diamond\le \min(2,|\xi|\tau_n).
\]
Teleskopując n−1 podstawień kanałów wewnątrz CAŁEGO obwodu przy tej samej ξ, z tymi samymi wolnymi odcinkami i pamięcią, otrzymujemy
\[
\|\rho_A^{\rm active}-\rho_A^R\|_1
 \le \mathbb E_\xi\min(2,|\xi|L_n)
 =\varepsilon(\gamma L_n).\tag{A}
\]
Uśrednienie można wykonać dopiero PO warunkowym teleskopowaniu. Nie istnieje \(\mathbb E|\xi|\), więc zastąpienie prawej strony przez \(\gamma L_n\) bez logarytmu byłoby nielegalne.

**B, niezależne przyrosty Cauchy–Lévy.** Przy generatorze
\(\mathcal D_\gamma=(\gamma/2)(\operatorname{Ad}_{Z_S}-\mathrm{Id})\) mamy \(\|\mathcal D_\gamma\|_\diamond\le\gamma\). Duhamel dla CP semigrupy kontrolowanej i jednostkowego kanału impulsu daje
\[
\|\Phi_{B,\tau_n}-\Phi_{0,\tau_n}\|_\diamond\le\gamma\tau_n.
\]
Ponownie teleskopowanie n−1 bramek przy niezależnych odcinkach procesu daje:
\[
\|\rho_B^{\rm active}-\rho_B^R\|_1\le\gamma L_n.\tag{B}
\]
To rozumowanie wykorzystuje generator **uśrednionego** B i nie zakłada ograniczonych ścieżek Lévy'ego.

**Wniosek (Helstrom):** Jeśli \(D_n^{\rm active}=\|\rho_A^{\rm active}-\rho_B^{\rm active}\|_1\), to
\[
|D_n^{\rm active}-D_n^R|\le
q_n:=\varepsilon(\gamma L_n)+\gamma L_n. \tag{H}
\]
Dla zdarzenia \(K\ge1\) w lokalnym pomiarze X różnica kontrastów prawdopodobieństw względem referencji nie przekracza \(q_n/2\) (dla ustalonego znaku kontrastu). To są **bezpieczne górne ograniczenia**, a nie charakterystyka rzeczywistych błędów konkretnego czujnika.

## 4. Twierdzenie R02.2: granica Helstroma przy skończonych impulsach

Jeżeli ciąg jawnych eksperymentów z §1 spełnia
\[
\gamma L_n\to0,\quad E_n\to0,\quad A_n^{\rm phys}\to0,
\quad\gamma F_n\to\gamma T=a>0,\quad \kappa_nT=\beta/n,
\]
to z (R) i (H):
\[
\boxed{\lim_{n\to\infty}D_n^{\rm active}
=2(1-e^{-a/2}).} \tag{T}
\]
Dodatkowo lokalny pomiar każdej próbki w X i test „co najmniej jeden minus” osiąga granicznie
\(\mathrm{TV}_{\rm OR}=1-e^{-a/2}\). Zatem aktywny szum podczas B-Hamiltonianowego / A-statycznego SWAP nie musi niszczyć limitu w tej **szczególnej, poprawiającej się z n klasie sterowania i pamięci**.

Dowód: \(\max d_j\le\sqrt{E_n}\to0\) i \(F_n\to T\), stąd \(P_n\to e^{-a/2}\). Ograniczenie \(\varepsilon(z_n)\to0\), \(\beta A_n^{\rm phys}\to0\), a także \(q_n\to0\) przez ciągłość ε w 0. Referencyjny test X-OR ma graniczną dostateczność z dowodu R35 i perturbacja zdarzeń jest najwyżej \(q_n/2\).

**Krytycznie:** równość T jest ostateczną odległością **dla zadanej sekwencji n−1 impulsów i końcowego pomiaru**. Nie jest normą procesu po dowolnych kontrolach, kwantowym optimum po wszystkich zegarach, ani twierdzeniem o fizycznym urządzeniu przy niezmienionej amplitudzie sterowania.

## 5. Konstrukcja R02.3: jednoczesne ograniczenie czasu impulsu, źródła i wieku

Wybierz dla n≥16:
\[
m_n=\lceil n^{2/3}\rceil,\quad B_n=\lceil n^{4/3}\rceil,\quad
\tau_n=T/B_n,\quad s_n=(n-1)/B_n,\quad F_n=T(1-s_n),
\]
\[
\delta_n=(n-m_n)/B_n,\quad
d_{\rm early}=(1-\delta_n)/m_n \ (\text{pierwsze } m_n \text{ ekspozycji}),\quad
d_{\rm late}=1/B_n\ (\text{pozostałe }n-m_n).
\]
Suma wszystkich d_j jest dokładnie 1, a n−1 rzeczywistych impulsów mieści się w T. Nie potrzebujemy „nakładania” SWAP na ekspozycję: bramki zajmują OSOBNY czas T, podczas którego źródło nadal działa, zgodnie z §1.

Mamy dokładnie
\[
E_n=(1-\delta_n)^2/m_n+(n-m_n)/B_n^2,
\]
\[
A_n^{\rm grid}=(m_n-1)/(2n)+\delta_n/2,
\]
\[
A_n^{\rm phys}=(1-s_n) A_n^{\rm grid}
+\frac{(n-1)(n-2)}{2nB_n}.
\]
Wynika stąd \(E_n=\Theta(n^{-2/3})\), \(A_n^{\rm phys}=\Theta(n^{-1/3})\), \(s_n=\Theta(n^{-1/3})\). Dla stałych a,β:
\[
|D_n^{\rm active}-2(1-e^{-a/2})|
=O(n^{-1/3}\log n)+O(\beta n^{-1/3}).\tag{RATE}
\]
Rząd RATE jest **rządem konserwatywnego ograniczenia**, nie oszacowaniem ostrej szybkości ani przewagą eksperymentalną.

Sterowanie Hamiltonianem wybranego impulsu wymaga
\[
\Omega_n:=\|H_{0,n}\|_{\rm op}=\pi B_n/(2T)=\Theta(n^{4/3}/T).
\]
Wybrana rodzina protokołów NIE osiąga (T) przy stałym Ω. Jeśli \(\Omega_n\le\Omega\) i implementujemy właśnie \(H=(\pi/2\tau)S\), to
\[
\tau_n\ge\pi/(2\Omega),\quad (n-1)\pi/(2\Omega)<T,\quad
n<1+2\Omega T/\pi.
\]
To skończona liczba dopuszczalnych impulsów dla stałego T,Ω — **dla tej zadeklarowanej realizacji SWAP**, nie nowe twierdzenie o każdej możliwej architekturze procesora.

## 6. Obliczone kontrole i negatywny wynik skończonego budżetu

Poniższa tabela jest wynikiem bezpośredniego podstawienia oraz odrębnego sumowania definicji \(A_n^{\rm phys}=n^{-1}\sum_j (T-t_j)/T\), zgodnego dla sprawdzonych siatek. Przy a=1, β=2:

| n | B_n | L_n/T | E_n | A_grid | A_phys | ε(γL_n) | γL_n |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 64 | 256 | 0.246094 | 0.041992 | 0.210938 | 0.278229 | 0.485311 | 0.246094 |
| 256 | 1626 | 0.156827 | 0.018448 | 0.144238 | 0.199418 | 0.354107 | 0.156827 |
| 1024 | 10322 | 0.099109 | 0.008139 | 0.093978 | 0.134122 | 0.252700 | 0.099109 |
| 4096 | 65536 | 0.062485 | 0.003463 | 0.060425 | 0.087876 | 0.177659 | 0.062485 |

**Kluczowe uczciwe ograniczenie skończonego n:** przy n=4096 mamy \(q_n=0.240144\) w normie śladowej, zatem konserwatywna niepewność kontrastu końcowego testu X-OR wynosi **aż 0.120072 TV**. To jest znacznie więcej niż różnica R01–R35 ok. **0.01808 TV** dla idealnych bramek w innym, bezpulsowym eksperymencie. Dlatego NIE wolno przenosić selektywnej przewagi liczbowej R01 na skończone impulsy jako gwarantowaną przewagę praktyczną. Graniczne (T) przetrwa, lecz finite-n advantage pozostaje otwarty.

**Dodatkowy bezpośredni dwukubitowy check niekomutującego SWAP i Z_S** dla stanu |+0>, γ=1: wykonano egzaktne macierzowe expm generatora Lindblada i Hamiltonianu (4×4/16×16). W poniższych przypadkach \(\|\rho_B^{pulse}-\rho_0^{pulse}\|_1\) jest poniżej γτ:
| τ | bezpośrednia różnica B | granica γτ | różnica A przy ξ=4 | granica |ξ|τ |
|---:|---:|---:|---:|---:|
| 0.01 | 0.00681525 | 0.010000 | 0.02691038 | 0.040000 |
| 0.05 | 0.03354795 | 0.050000 | 0.13441969 | 0.200000 |
| 0.20 | 0.12675803 | 0.200000 | 0.52947685 | 0.800000 |

A to **warunkowa** konkretna ξ=4, nie uśrednienie po Cauchy ani symulacja całego n-probe eksperymentu. Symulacja B jest średnim Markowowskim podczas jednego SWAP; obie służą jedynie do sanity-check lokalnego ograniczenia. Nie ma liczbowo policzonej pełnej macierzy 2^4096.

## 7. Falsyfikatory / granice kompetencji

- F1: ustalone fizyczne Ω i T dają górny limit n dla realizacji §1; nieograniczone n w tym samym sprzęcie jest niedozwolonym ekstrapolowaniem.
- F2: statycznego ξ (A) nie można podmienić średnim Lindblad A; ukryta zależność między impulsami znika w takim nielegalnym uproszczeniu.
- F3: próbkowanie jednej niezależnej fazy na każdy impuls B nie opisuje tego samego niekomutującego jednoczesnego procesu co generator Lévy B.
- F4: Cauchy ma nieskończony moment pierwszego rzędu; bez obcięcia \(\varepsilon(\gamma L)\) nielegalne jest liniowe „średnie |ξ|”.
- F5: stan pamięci podlega aging również podczas późniejszych impulsów; pominięcie składnika \((n-1)(n-2)/(2nB_n)\) zaniża \(A_n^{phys}\).
- F6: przy stałej κ zamiast \(\kappa_n T=\beta/n\) nie ma tego samego twierdzenia (T); R34 zabrania automatycznego „fixed-κ recovery”.
- F7: wynik nie obejmuje krosowych błędów Hamiltonianu, ograniczonego pasma, finite slew, odczytu, błędów inicjalizacji, kontrolnych korelacji z ξ, nieidealnej topologii przełączników, kosztu chłodzenia czy metrologicznej kalibracji.
- F8: w finite n granica q jest luźna; R02 NIE poświadcza przewagi praktycznej nad R35 ani jednej najlepszej siatki.
- F9: wyniki nie są NCDG J3/K, teorią grawitacji, sygnałem urządzenia ani podstawą \`EXEC_SIGN\`.

## 8. Karta review / następny falsyfikator

Do niezależnego review: (a) proof of χ Cauchy-averaged capped-error equality; (b) controlled Lindblad generator for B and diamond contractivity; (c) exact physical aging timing and product state reference; (d) n=4096 q-value and comparison of DIFFERENT model experiments; (e) all quantified prerequisites for T; (f) check that regularization and initial fresh |+> systems don't cost hidden gates.

Dalszy sensowny **negatywny test**: narzucić stałe sprzętowe Ω, κ i niezerowe błędy impulsu, następnie znaleźć skończonon-parametryczny optimum/discrimination upper/lower bounds; nie zasłaniać luki nową tezą o fizycznym optimum. Ewentualnie policzyć pełny n=2..5 aktywny proces A/B bez zastępowania niekomutującej Lévy dephasing przez quasi-static draw w B.

## 9. RETURN

\`PRF12_R02: ANALYTIC_CONDITIONAL_THEOREM_LOCAL / FULL_QUANTUM_ENDPOINT_BOUND_WITH_EXPLICIT_SOURCE_MODEL / 2Q_EXPM_SANITY_PASS / SELECTED_GRID_ARITHMETIC_PASS / PRIOR_ART_SUBTRACTION_DOCUMENTED / REFEREE_PENDING / NOT_CANON / NO_EXEC / NO_NOVELTY / GITHUB_PENDING_BW_INGEST / SUCCESSION_ZIP_UNREAD\`
