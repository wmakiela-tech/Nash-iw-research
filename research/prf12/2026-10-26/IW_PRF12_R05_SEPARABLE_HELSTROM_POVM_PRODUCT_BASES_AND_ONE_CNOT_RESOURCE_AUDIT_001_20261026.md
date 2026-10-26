---
artifact_id: IW_PRF12_R05_SEPARABLE_HELSTROM_POVM_PRODUCT_BASES_AND_ONE_CNOT_RESOURCE_AUDIT_001_20261026
created_at: 2026-10-26
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
problem_id: PRF12_R04_MEASUREMENT_RESOURCE_GAP
exposure: PUBLIC
canonical_body_path: research/prf12/2026-10-26/IW_PRF12_R05_SEPARABLE_HELSTROM_POVM_PRODUCT_BASES_AND_ONE_CNOT_RESOURCE_AUDIT_001_20261026.md
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_SEPARABLE_POVM_CONSTRUCTION_LOCAL / FOUR_Q_EXACT_MATRIX_CONTROLS_PASS / FINITE_PULSE_TRANSFER_CHECK / PRODUCT_OPTIMIZATION_NUMERICAL_NOT_CERTIFIED / REFEREE_PENDING
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_HARDWARE / NO_LOCC_IMPLEMENTABILITY_CLAIM / NO_UNRESTRICTED_PROCESS_OPTIMUM / NO_FULL_SUCCESSION_PACKET_READBACK
function: SCIENCE_FIRST / FOUNDATION_FIRST / TWO_SURFACE_PRIOR_ART / NEGATIVE_KNOWLEDGE_PRESERVING / FALSIFIER_FIRST
---

# PRF12 R05 — Helstrom dla trzech próbek poprzez 28-elementowy pomiar separowalny; ograniczenia baz produktowych i pojedynczego CNOT

**Data:** 26.10.2026. **Funkcja:** PRF12 (po aktywacji Moderatora). **Główne odkrycie robocze:** po R04 nie trzeba zakładać, że optimum Helstroma wymaga nieseparowalnych efektów POVM. Dla ściśle wytypowanego idealnego 3-probe Cauchy-vs-Lévy eksperymentu z równymi ekspozycjami można jawnie zbudować separowalny 28-efektowy POVM osiągający dokładnie Helstroma. **Nie** wykazano protokołu LOCC, kosztu sprzętowego ani minimalnej liczby efektów.

## 0. Właściciele/źródła: nie nadpisywać

- PRF11 R29–R35 pozostają właścicielem identyfikowalności wspólnej ukrytej fazy Cauchy i niezależnych przyrostów Cauchy–Lévy. R35: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R35_NONUNIFORM_SWAP_TIME_GRID_RECOVERS_IDEAL_MEMORY_WITH_CRITICAL_STORAGE_RATE_001_20261025.md .
- PRF12 R01: minimum odstępu i harmonogram dwóch klas; https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R01_CLOCK_BUDGET_GATE_ERRORS_AND_TWO_TIER_SCHEDULE_001_20261026.md .
- PRF12 R02: aktywny szum podczas skończenie długiego SWAP; https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R02_FINITE_DURATION_SWAP_CAUCHY_ACTIVE_PULSES_AND_RESOURCE_GATE_001_20261026.md .
- PRF12 R03: n=2, wyjątkowa dokładna wystarczalność lokalnej parzystości X; https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R03_FINITE_TWO_PROBE_SWAP_CAUCHY_SECTOR_PARITY_HELSTROM_001_20261026.md .
- PRF12 R04: ścisły n=3 kontrprzykład dla pełnego lokalnego X; https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R04_THREE_PROBE_FINITE_SWAP_EXACT_X_READOUT_GAP_AND_SECTOR_DECOMPOSITION_001_20261026.md (zweryfikowany blob b9e8a0aae88403ea65584061f5f105a33bd81c1c).

**Zewnętrzna literatura uprzednia** (metody klasyczne, NIE proof of PRF12 priority):
- Helstrom, *Quantum Detection and Estimation Theory* (1976), klasyczne ograniczenie optimum binary state discrimination (standardowo TV=1/2||ρA−ρB||1).
- Bennett et al., *Quantum nonlocality without entanglement*, Phys. Rev. A 59, 1070 (1999), https://doi.org/10.1103/PhysRevA.59.1070 .
- Croke, Barnett, *Difficulty of distinguishing product states locally*, Phys. Rev. A 95, 012337 (2017), https://doi.org/10.1103/PhysRevA.95.012337 .
- S. M. Cohen, *Class of unambiguous state discrimination problems achievable by separable measurements but impossible by local operations and classical communication*, Phys. Rev. A 91, 012321 (2015), https://doi.org/10.1103/PhysRevA.91.012321 . Zwłaszcza: SEP nie implikuje LOCC.
- Bandyopadhyay, Halder, Nathanson, *Optimal resource states for local state discrimination*, Phys. Rev. A 97, 022314 (2018), https://doi.org/10.1103/PhysRevA.97.022314 .
- Zambon, *Process tensor distinguishability measures*, Phys. Rev. A 110, 042210 (2024), https://doi.org/10.1103/PhysRevA.110.042210 . Nie wolno przenieść endpoint POVM na normę procesu.
- A. Imam, S. Manna, *Local marking of locally implementable unitary operations*, Phys. Rev. A 114, 042441, opublikowane 19.10.2026, https://doi.org/10.1103/sx4p-ty2v . Odmienny problem (unitary marking, nie nasze binary mixed-state endpoint), więc tylko currentness scout, nie dowód tej konstrukcji.

**Host subtraction:** twierdzenie Helstroma, separowalne POVM, symetryczne stany Dickego/W, grupowe twirling i ograniczenia LOCC są znaną matematyką. Udział PRF12 R05 jest WYŁĄCZNIE specyficznym, sprawdzonym rozkładem dla wcześniej stworzonego syntetycznego modelu R04. NO NOVELTY claim.

## 1. Zamrożony eksperyment: idealne trzy ekspozycje, brak starzenia

Weź n=3, κ=0, Δ1=Δ2=Δ3=T/3 i q=γT/3>0. Dla q>0, x=e^(−q)∈(0,1), b=1−x², a=xb. PRF12 R04 pokazał, że D=ρA−ρB działa niezerowo tylko na 6-wymiarowej przestrzeni wzbudzeń 1 i 2 i ma blok

 D|_{N=1,2}=1/8 [[b(J3−I3), a I3],[a I3,b(J3−I3)]]

po odpowiednim przyporządkowaniu stanów przez dopełnienie bitowe. Pozostałe |000>,|111> tworzą dokładny kernel D.

Definiujemy stany normalizowane
 |W>=(|001>+|010>+|100>)/sqrt(3),
 |Wbar>=(|110>+|101>+|011>)/sqrt(3),
 P_W=|W><W|, P_Wbar=|Wbar><Wbar|,
 P0=|000><000|+|111><111|,
 P_+=P_W+P_Wbar.

Spektrum dodatnie D składa się z dwóch wartości b(2±x)/8>0 w span(W,Wbar). Pozostałe cztery niezerowe wartości własne są ujemne, a kernel=P0. Wobec tego efektem pozytywnym Helstroma jest P_+, a dowolne dodanie 0≤K≤P0 nie zmienia rozróżnialności.

Dokładne optimum:
 TV_Hel=1/2||D||1=b/2=(1−e^(−2q))/2.                 (1)

## 2. Theorem R05.1: 28 rank-one PRODUCT effects achieve exact binary Helstrom

Zdefiniuj lokalny stan równikowy |+φ>=(|0>+e^(iφ)|1>)/sqrt(2). Niech Φ={0,π/2,π,3π/2} (cztery fazy zabijające wszystkie różnice liczby wzbudzeń w zakresie 1..3), a S3 grupą sześciu permutacji.

**Cztery efekty klasy A+**, dla φ∈Φ:
 E_{φ,+}=(2/3) (|+φ><+φ|)^{⊗3}.

**Dwadzieścia cztery efekty klasy B−**, dla φ∈Φ i π∈S3:
 E_{φ,π,−}=(2/9) ⊗_{j=1}^3 |+(φ+α_{π(j)})><+(φ+α_{π(j)})|,
 gdzie (α1,α2,α3)=(0,2π/3,4π/3).

Każdy efekt jest dodatni, rzędu 1, jawnie iloczynowy. Grupując tylko po oznaczeniu hipotezy, otrzymujemy dokładnie:

 E_+ := Σ_φ E_{φ,+} = P_W+P_Wbar+(1/3)P0,          (2)
 E_- := Σ_{φ,π} E_{φ,π,−} = (I−P_W−P_Wbar)−(1/3)P0
       = P_{std,weight1}+P_{std,weight2}+(2/3)P0.    (3)

Stąd E_++E_-=I, to jest dokładnie normalizowany POVM z 28 dodatnimi produktowymi elementami.

**Dowód.** Globalny twirl fazy zabija coherences pomiędzy różnymi wagami Hamminga. Dla |+φ>^⊗3 waga k ma prawdopodobieństwo C(3,k)/8 i w sektorach k=1 i k=2 daje dokładnie |W> oraz |Wbar>. Po uśrednieniu czterech faz:
 σ_+ = P0/8 + (3/8)(P_W+P_Wbar).
 Mnożąc przez 8/3 dostajemy E_+.

Dla faz względnych 0,2π/3,4π/3 suma amplitud w symetrycznych wektorach W i Wbar znika, ponieważ 1+ω+ω²=0. Permutacyjny twirl rozkłada pozostały ciężar 3/8 każdej wagi 1 i 2 równomiernie na jej dwuwymiarowy ortogonalny sektor standardowy. Dlatego:
 σ_- = P0/8 +(3/16)(P_{std,weight1}+P_{std,weight2}).
 Mnożąc przez 16/3 dostajemy E_−. QED.

Ponieważ D ma dodatni support w span(W,Wbar), ujemny w obu sektorach standardowych, a zerowy na P0:

 Tr(E_+ D)=Tr(P_+ D) = b/2 = TV_Hel.                 (4)

**Zasięg:** wzory (2)–(4) obowiązują dla KAŻDEGO q>0 w tej jednej rodzinie równych idealnych ekspozycji, bez κ. To jest efekt pomiaru rozróżniania stanów na końcu jednego protokołu, nie ogólny process tensor norm.

**Najważniejsza granica:** 28 iloczynowych efektów definiuje pomiar SEP. To NIE jest dowód, że istnieje implementacja za pomocą lokalnych operacji i klasycznej komunikacji, ani że nie potrzeba zasobów splątujących przy rzeczywistej realizacji; SEP ⊃ LOCC w znanej literaturze. Tu status LOCC pozostaje OPEN. Tak samo 28 efektów nie jest minimalną liczbą.

## 3. Exact finite control q=1/3 i test niezależności od q

NumPy kontrola z analitycznie wyprowadzonymi wzorami, bez fitowania parametrów, dla q=.05,1/3,.7,1.4:
- Norm closure: max absolute |E_++E_-−I|=4.4408920985×10^(−16).
- Każdy z 28 efektów jest dodatni semidefinite do dokładności maszyny, rzędu 1.
- Max |E_+−P_W−P_Wbar−P0/3| ≈ 3×10^(−16).
- W każdym q: TV_SEP28=TV_Hel=(1−e^(−2q))/2 do ≤10^(−15) w obliczeniach.

Dla γT=1, q=1/3:

| Readout | TV |
|---|---:|
| pełny Helstrom, dowolny endpoint POVM | 0.243291440484 |
| SEP28: cztery + oraz 24 − efekty iloczynowe | 0.243291440484 |
| pełny pomiar lokalnych X (8 wyników) | 0.189292628451 |
| 1 CNOT + jedna zoptymalizowana rotacja odczytu, ścisły świadek ograniczonej konstrukcji | 0.198464903476 |

W R04 TV X parity=0.130744451 i TV X OR=0.123920403.

## 4. Czy wystarczy zmienić lokalną bazę? Czy pomaga jeden CNOT?

Rozważamy bez adaptacji: dokładnie trzy lokalne ortonormalne rank-1 bazy (po dwa kąty θ_j,φ_j na kubit), wszystkie osiem wyników zachowane i optymalne klasyczne postprocessing. Funkcja celu TV_product(θ,φ)=1/2 Σ_s |Tr(P_s(θ,φ)D)|. Użyto scipy differential_evolution na sześciu kątach, seed 11/19/27; odnaleziono rozwiązania równoważne bazie X:

 TV_product_best_found ≈0.18929262845.                 (5)

To wyłącznie **niecertyfikowane optimum numeryczne**, nie twierdzenie, że wszystkie local product projective measurements są gorsze lub że pełne LOCC jest gorsze od SEP28. Należy też oddzielać produktowe ostre PVM od dowolnych lokalnych POVM/adaptacji.

Drugą rodziną jest JEDEN CNOT (pierwszy kubit kontroluje drugi), następnie pomiar X na kubitach 1 i 3 oraz pomiar w płaszczyźnie XZ o kącie θ≈1.000253724 względem Z na kubicie 2. Zawsze zachowujemy pełne osiem wyników. Dla q=1/3 bez dalszego strojenia innych elementów:

 TV_CNOT_witness=0.198464903476>TV_X.                  (6)

To dokładna ewaluacja jawnej bramki i jawnego zestawu osi; jednak wybrany kąt pochodzi z numerycznego dostrojenia na tym q i nie stanowi globalnie optymalnej implementacji „jednego CNOT”. Przy q=.05, .7, 1.4 ta SAMA jawna ustawiona bramka może być gorsza niż X; nie istnieje twierdzenie o uniwersalnej przewadze CNOT. Dla q=1/3 (6) odzyskuje ~17% luki z R04. UWAGA: CNOT sam z pomiarem wszystkich X bez zmiany osi w ogóle NIE zmienia TV — tylko relabeluje wyniki zgodnie z działaniem CNOT na podgrupę X Pauliego.

## 5. Finite-duration source-active transfer: niezwykle ważny negatywny test

Nie wolno utożsamiać idealnego eksperymentu §1 z R04 active-pulse finite (dwie bramki τ=π/(2Ω), T=1, γ=1, Ω=8, źródło ξ aktywne w A i Lindblad aktywny w B, stały κ). Wybrano TAN SAM tensor E_+ z (2) i odczytano jego kontrast na stanach aktywnych R04 — bez ponownej optymalizacji E_+.

Kontrole NumPy/SciPy względem R04 źródła dla obcięcia Cauchy X=12000, step=.3 (granica wkładu obciętego ogona do pojedynczego TV ≤5.31×10^−5, quadrature step nie jest certyfikowany):

| Free schedule | κ | TV_H active | TV_Xfull active | TV_SEP28_witness active |
|---|---:|---:|---:|---:|
| 1/3,1/3,1/3 | 0.3 | ≈0.181388 | ≈0.146901 | ≈0.178747 |
| 1/3,1/3,1/3 | 5.0 | ≈0.041397 | ≈0.037961 | ≈0.029827 |
| 0.55,0.30,0.15 | 0.3 | ≈0.167205 | ≈0.147232 | ≈0.152912 |
| 0.55,0.30,0.15 | 5.0 | ≈0.046897 | ≈0.041357 | ≈0.036872 |

W słabym aging κ=.3 i równych wolnych ekspozycjach ten dawny idealny SEP28 odzyskuje ok. 92% luki X→Helstrom; lecz w silnym aging κ=5 staje się GORSZY niż proste X. Separowalność POVM nie gwarantuje optymalności pod zmianą źródła i wieku.

Niezależna, lokalna optymalizacja (sześć kątów produktów, differential_evolution seed=42, bez certyfikacji globalności) daje przy κ=5, równych czasach, \(\mathrm{TV}_{product,bestfound}\approx0.040516675\) wobec Hel≈0.041397, czyli > X≈0.037961. Przykładowe kąty (θ,φ) poszczególnych kubitów:
 (1.57101455,1.57078166),
 (0.78832505,1.36812110),
 (1.92853396,4.71237125).

To kontrola istnienia lepszego jawnego produktu w aktywnej konfiguracji, nie theorem global product optimum. Pierwotny, R04-stabilized cutoff=30000 daje trochę inne liczby absolutne w granicach zadeklarowanych ogonów, nie zmieniając ułożenia dla dużych różnic.

**Falsifier:** jeden kanoniczny readout nie jest automatycznie najlepszy w różnych modelach; wybór hardware i odczytu wymaga wspólnie typu źródła, κ, harmonogramu, kosztu i fizycznej implementacji. Nie wolno ogłaszać, że „lokalny X jest optymalny” albo „28 efektów nie potrzebuje splątania”.

## 6. Exact executable custody

Repo scientific paths:
- Self-contained **exact** ideal model with 28 effects, positivity, completeness, comparison X/CNOT and optional non-certified six-angle product search:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R05_SEPARABLE_28_EFFECT_HELSTROM_EXACT_REPRO_001_20261026.py
  Run \`python IW_PRF12_R05_SEPARABLE_28_EFFECT_HELSTROM_EXACT_REPRO_001_20261026.py\`; for costly multiple-seed search add \`--search\`.
- Finite-pulse **active** verification (imports the prior R04 scientific file from same repository directory):
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R05_ACTIVE_FINITE_SWAP_READOUT_CHECK_001_20261026.py
  Run \`python IW_PRF12_R05_ACTIVE_FINITE_SWAP_READOUT_CHECK_001_20261026.py --search\`; R04 dependency is \`IW_PRF12_R04_THREE_PROBE_ACTIVE_SWAP_AND_X_MEASUREMENT_REPRO_001_20261026.py\`. Active default cutoff 30000/step .3; early exploratory table §5 used cutoff 12000/.3.

## 7. Independent referee, destruction criteria, and negative knowledge

1. Derive permutation/global-phase twirls algebraically; check no interference survives phase set Φ, count correct six permutations and four phases, positivity of all 28 elements and completeness. Test all q>0 rather than only q=1/3.
2. Do not confuse separable effects with LOCC implementation. Seek an exact finite-round LOCC protocol OR a no-go/upper bound using known distinguishability results. Neither is established here.
3. Determine whether fewer than 28 product rank-1 effects suffice; 28 is a construction not a lower bound.
4. Repeat six-angle product numerical searches via analytic inequalities/global branch-and-bound before asserting any mathematical optimality. Randomized optimization alone does not make (5) a theorem.
5. For active n=3 confirm source specification under finite SWAP, memory age, heavy-tail integration and gate topology; distinguish κ=.3 from κ=5. Cross-check with an independently developed integration method, not copied R04 quadrature.
6. If a different LOCC/SEP POVM attains Helstrom for source-active parameters, report exact resource assumptions; do not promote a source-off calculation to source-on.
7. Distinguish endpoint Helstrom for fixed evolution from distinguishability norms over ALL process testers, and from experimental feasibility. No quantum hardware measurement is claimed.
8. Preserve negative knowledge from R01–R04 and do not elevate to Nash-IDG gravitational J3/K, LT canon, publication priority, BW synced, or EXEC_SIGN.

**Next science question R06:** characterize SEP-vs-LOCC gap for exact fixed n=3 source pair (could be equality or strict gap), and independent finite-duration SEP POVM optimization under κ>0. Test whether an adaptive local readout can achieve the exact binary effect (2), or whether an entangling operation is genuinely necessary once implementability, rather than abstract separability, becomes the resource.

## 8. Return

PRF12_R05 / EXACT_28_RANKONE_PRODUCT_POVM_FOR_N3_IDEAL / EXACT_SEPARABLE_HELSTROM_SUFFICIENCY / LOCAL_PRODUCT_NUMERIC_NONCERTIFIED / ONE_CNOT_WITNESS_AT_Q_1_3 / ACTIVE_NOISE_RESOURCE_REGIME_REVERSAL / INDEPENDENT_REFEREE_PENDING / NO_LOCC_CLAIM / NO_NOVELTY / NO_CANON / NO_EXEC / GITHUB_PENDING_BW_INGEST / SUCCESSION_ZIP_UNREAD.
