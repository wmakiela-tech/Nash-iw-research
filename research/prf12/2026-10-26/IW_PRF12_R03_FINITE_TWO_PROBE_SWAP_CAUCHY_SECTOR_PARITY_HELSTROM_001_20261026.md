---
artifact_id: IW_PRF12_R03_FINITE_TWO_PROBE_SWAP_CAUCHY_SECTOR_PARITY_HELSTROM_001_20261026
created_at: 2026-10-26
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
problem_id: PRF12_R02_FIXED_OMEGA_FIXED_KAPPA_FINITE_N
exposure: PUBLIC
canonical_body_path: research/prf12/2026-10-26/IW_PRF12_R03_FINITE_TWO_PROBE_SWAP_CAUCHY_SECTOR_PARITY_HELSTROM_001_20261026.md
sync_state: GITHUB_PENDING_BW_INGEST
status: SOURCE_TYPED_LOCAL_PROOF_AND_FINITE_NUMERIC_CONTROL / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_DEVICE / NO_GLOBAL_MULTISLOT_OPTIMUM / NO_FIXED_KAPPA_ASYMPTOTIC_RECOVERY / NO_FULL_SUCCESSION_ZIP_READBACK
function: SCIENCE_FIRST / FOUNDATION_FIRST / TWO_SURFACE_PRIOR_ART / NEGATIVE_KNOWLEDGE / FALSIFIER_FIRST
---

# PRF12 R03 — Two-probe exact Helstrom statistic, source-active Cauchy noise and finite-resource falsifier

**Data:** 26 października 2026. **Komórka:** PRF12. **Zakres:** zamrożony syntetyczny model n=2, jeden SWAP o skończonym czasie trwania, źródło A = stała w całym eksperymencie ξ~Cauchy(0,γ), źródło B = niezależne przyrosty Cauchy–Lévy i semigrupa Lindblada. **Stan:** lokalny dowód, odtwarzalne obliczenia, bez niezależnej recenzji.

## 0. Źródła i odejmowanie dojrzałego gospodarza

PRF11 R29–R35 ustanowił oryginalne porównanie dwóch procesów źródłowych, testy wieloslotowe i warunki dla starzejącej się pamięci. Szczególnie PRF11 R35: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R35_NONUNIFORM_SWAP_TIME_GRID_RECOVERS_IDEAL_MEMORY_WITH_CRITICAL_STORAGE_RATE_001_20261025.md

PRF12 R01 ustanowił abstrakcyjne bramki zegara i błędów SWAP:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R01_CLOCK_BUDGET_GATE_ERRORS_AND_TWO_TIER_SCHEDULE_001_20261026.md

PRF12 R02 wprowadził dwa źródłowo odrębne modele szumu podczas skończenie długiej bramki, w tym dokładny Hamiltonian SWAP i zachowawcze oszacowania:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R02_FINITE_DURATION_SWAP_CAUCHY_ACTIVE_PULSES_AND_RESOURCE_GATE_001_20261026.md

**Zewnętrzne gospodarze:**
- Zambon, Soares-Pinto (2024), Relations between Markovian and non-Markovian correlations in multitime quantum processes, PRA 109, 062401, https://doi.org/10.1103/PhysRevA.109.062401.
- White, Jurcevic, Hill, Modi (2025), Unifying Non-Markovian Characterization with an Efficient and Self-Consistent Framework, Physical Review X, https://d3ccyth396mz21.cloudfront.net/publications/unifying-non-markovian-characterization-with-an-efficient-and-self-consistent-framework .
- Butler i in. (2024), Optimizing Performance of Quantum Operations with Non-Markovian Decoherence: The Tortoise or the Hare?, PRL 132, 060401, https://doi.org/10.1103/PhysRevLett.132.060401 .
- Nelson, Barnes, Exact quantum speed limits for quantum gates from space curve geometry, Phys. Rev. A accepted 15.10.2026, https://doi.org/10.1103/28zn-ch8y .
- Quantum speed limits from symmetries in quantum control (2026), https://doi.org/10.1088/1751-8121/ae3f68 .

Diagonalizacja qubitu, norma Helstroma, analityczna całka Cauchy, symetria parzystości, ogólna teoria kwantowych procesów i bounded-Hamiltonian gates mają ugruntowaną literaturę. R03 nie rości nowości lub pierwszeństwa publikacyjnego.

## 1. Zamrożony kontrakt dwóch kubitów

S jest aktywnym kubitem systemu; M świeżym kubitem pamięci. Oba startują w |+,+>. Ustal stałe fizyczne: T>0, γ>0, Ω>0, κ≥0 i czas bramki τ=π/(2Ω)<T. Pozostały czas wolny F=T−τ rozdziel pomiędzy Δ1=pF i Δ2=(1−p)F, 0<p<1. W kolejności: swobodna ekspozycja S przez Δ1, jedyny impuls H0=Ω SWAP_(S,M) przez τ, swobodna ekspozycja S przez Δ2. Po impulsie pamięć M dekoheruje z widocznością r=exp(−κΔ2). Podczas impulsu źródło nadal działa na S.

Hipoteza A: warunkowy generator H_A(t)=H0(t)+ξ Z_S/2 dla JEDNEGO ξ~Cauchy(0,γ) ukrytego przez cały przebieg. Uśrednij po ξ po całej unitarnej ewolucji, a nie pomiędzy krokami.

Hipoteza B: generator L_B(t)(ρ)=−i[H0(t),ρ]+γ/2(Z_SρZ_S−ρ), odpowiadający uśrednionym niezależnym przyrostom Cauchy–Lévy we wszystkich trzech segmentach.

Kryterium TV_H=(1/2)||ρ_A−ρ_B||_1; przy równych priorach P_success=(1+TV_H)/2. Bez SWAP lub jakiejkolwiek innej interwencji pojedynczy kubit daje dokładnie TV=0, ponieważ obie hipotezy mają tę samą jednoczasową semigrupę dephasing. Nie należy utożsamiać tego z optimum dowolnego 1-slot testera PRF11 R30.

## 2. Lemat R03.1: precyzyjny nośnik różnicy stanów

W bazie 00,01,10,11 mamy D=ρ_A−ρ_B i

 D = c(|01><10| + |10><01|),  c∈R.                   (R03.1)

**Dowód source-typed.** Operator SWAP oraz fazowy generator na S zachowują całkowitą liczbę wzbudzeń N=0,1,2. Przestrzeń operatorowa rozpada się na sektory (N_bra,N_ket). Na sektorach (0,1),(0,2),(1,2) generator ukrytej ξ zawiera −iξ Q, gdzie Q=(Z_S,left−Z_S,right)/2 ma WYŁĄCZNIE wartości własne 0 lub +1. Na sektorach sprzężonych (1,0),(2,0),(2,1) Q ma tylko 0 albo −1; na (0,0),(2,2) jest zerem. Pozostały sektor (1,1) ma Q o przeciwnych znakach i wymaga osobnego potraktowania.

Dla Q≥0 operatorowy propagator warunkowy jest holomorficzny i ograniczony dla Im ξ≤0 (dla kompleksowego ξ składnik Im ξ Q jest dyssypatywny, a pozostały generator jest antyhermitowski względem normy Hilberta–Schmidta). Całkowanie po prawie Cauchy(0,γ) jest w tym sektorze dokładną wartością analitycznego propagatora w ξ=−iγ. Dostajemy generator L0−γ Q. Analogicznie Q≤0 używa górnej półpłaszczyzny i ξ=+iγ, dając L0−γ|Q|. Generator niezależnych przyrostów B ma właśnie L0−γ|Q|, ponieważ lokalne γ/2(Ad_Z−I) na tych sektorach jest −γ|Q|. Zatem A=B we wszystkich sektorach poza (1,1). Podstawę analytic-continuation i dobór półpłaszczyzny należy sprawdzić niezależnie; to nie jest ogólna tożsamość procesów A/B.

Na jednowzbudzeniowym sektorze o bazie 01,10 stan początkowy wynosi (I+σ_x)/4, a Hamiltonian jest Ωσ_x+ξσ_z/2 podczas bramki oraz ξσ_z/2 w przerwach. Przy zamianie ξ→−ξ generatory są sprzężone przez σ_x, a symetryczna Cauchy gwarantuje, że średnia A komutuje z σ_x. Ta sama symetria zachodzi dla semigrupy B. Całkowity ślad tego sektora jest identyczny (1/2), więc D wewnątrz sektora jest wyłącznie wielokrotnością σ_x (rzeczywista różnica koherencji). Poimpulsowe Z_M dephasing w obu hipotezach zachowuje sektor i mnoży c przez exp(−κΔ2). Dowodzi (R03.1) dla tego konkretnego źródła/sterowania. □

Nie wolno przenosić wniosku na H0 nie zachowujący wzbudzeń, niesymetryczną inicjalizację ani szum, który różnie działa bezpośrednio na pamięć.

## 3. Twierdzenie R03.2: parzystość lokalnych X jest dokładnie Helstrom-optimal

Z (R03.1) widmo D jest {+c,−c,0,0}, zatem TV_H=|c|. Optymalne efekty można skonstruować w rozpiętości wektorów Bell (|01>±|10>)/sqrt(2), ale nie wymagają splątanego aparatu pomiarowego.

Zmierz osobno X na S i M, zachowaj pełne dwa wyniki. Oblicz ich parzystość, z efektem P_even=(I+X⊗X)/2. Dla tej konkretnej D:

 Tr(P_even D) = c,
 TV_X_parity = |c| = TV_H.                              (R03.2)

Z kolei postprocesor OR zachowujący jedynie zdarzenie „co najmniej jeden minus” odpowiada efektowi I−|++><++|. Jego kontrast ma moduł |c|/2:

 TV_X_OR = TV_H/2.                                       (R03.3)

W n=2 lokalny pełny odczyt X i klasyczne parity wystarczają, ale OR odrzuca dokładnie połowę tego świadectwa. NIE przeczy to asymptotycznej wystarczalności OR w odmiennych założeniach R35.

## 4. Dokładny benchmark bez źródła podczas bramki i próg harmonogramu

Kontrola referencyjna: to SAMO n=2, T, τ, p i aging, lecz A/B source jest wyłączone TYLKO podczas idealnej bramki SWAP. Nie wolno mylić z rzeczywistym aktywnym pulse testem R03.

 c_ref = exp(−κΔ2)/4 × [exp(−γ|Δ1−Δ2|)−exp(−γ(Δ1+Δ2))].      (R03.4)

Ta formuła jest dokładną różnicą macierzy ρA/ρB z PRF11 R35 po podstawieniu d1,d2 i r. Czas źródłowy tego benchmarku wynosi F=T−τ, nie T.

Maksymalizacja c_ref po p, dla stałych γ,κ,F, daje:

 kcrit=2γ/[1−exp(−γ F)]
 p_ref_star=1/2 dla κ≤kcrit
 p_ref_star=1−log[κ/(κ−2γ)]/(2γF) dla κ>kcrit.            (R03.5)

Dowód: lewa strona p≤1/2 jest monotonicznie rosnąca. Przy x=1−p∈[0,1/2] funkcja jest exp(−γF)/4 × [exp((2γ−κ)Fx)−exp(−κFx)]; warunek zerowej pochodnej wraz z bramką x≤1/2 daje (R03.5).

Dla T=1,γ=1,Ω=8,τ=π/16≈0.19634954,F≈0.80365046:

| fixed κ | p_ref_star | exact TV_ref optimum | exact TV_ref at p=1/2 |
|---:|---:|---:|---:|
| 0.3 | 0.500000 | 0.122396341 | 0.122396341 |
| 3 | 0.500000 | 0.041360915 | 0.041360915 |
| 5 | 0.682184 | 0.020806830 | 0.018516938 |
| 10 | 0.861169 | 0.009168726 | 0.002483229 |

Nierówny czas ekspozycji może być korzystny przy dużym κ, nawet dla stałego Ω i stałego κ. To dokładnie optimum benchmarku, NIE optimum problemu z aktywnym źródłem w impulsie.

## 5. Prawdziwe aktywne źródła podczas bramki — obliczenia kontrolne

B liczono za pomocą dokładnej w tym modelu eksponenty 16×16 generatora Lindblada podczas impulsu, nie przez fałszywy quasi-static Cauchy. A liczono jako średnią po warunkowej 4×4 unitarnej ewolucji z *tym samym* ξ w obu wolnych okresach i impulsie; w sektorze jednego wzbudzenia użyto jawnej 2×2 eksponenty Ωσ_x+ξσ_z/2.

Prawa Cauchy'ego nie traktowano naiwnie przez E|ξ|. Całkowano na [-X,X] metodą trapezową, brakującą masę ogonową m_X=(2/π)atan(γ/X) zastąpiono dowolnym dodatnim stanem normalizującym. Ze względu na dodatniość obu podmian:
 ||ρ_A(true)−ρ_A(truncated+fill)||_1≤2m_X, więc błąd TV_H ≤m_X niezależnie od charakteru ogona. Nie jest to certyfikat dokładności samej skończonoprzedziałowej kwadratury; krok .2 porównano z .1.

Dla X=100000, γ=1: m_X≈0.0000063662. Wyniki dla T=1,γ=1,Ω=8:

| κ | p | TV_H aktywne ≈ TV_X parity | TV_X OR |
|---:|---:|---:|---:|
| 0.3 | 0.500000 | 0.125316837 | 0.062661421 |
| 5 | 0.500000 | 0.018958771 | 0.009481190 |
| 5 | 0.682184 | 0.026685903 | 0.013344987 |
| 5 | 0.800000 | 0.028379845 | 0.014192227 |
| 5 | 0.900000 | około 0.02703 | około 0.01352 |

Dla κ=0.3,p=.5 porównanie kwadratury X=100000, krok ξ .2 vs .1 daje TV równe do wydrukowanej dokładności, różnica ~3×10^−15; po zastąpieniu ogona w pozostałych elementach D poza parami (01,10),(10,01) maksimum ~2×10^−6, zgodne z analitycznym zerem i błędem ogona.

**Istotny falsyfikator transportu optimum.** Dla κ=5 p_ref_star≈.682184 z innego problemu źródłowego daje TV_active≈0.026686, ale p=.8 daje TV_active≈0.028380. Różnica ~0.001694 zdecydowanie przekracza zadeklarowany błąd ogona. Zatem optimum source-off-in-pulse nie musi być optymalne source-active. p=.8 NIE jest certyfikowanym globalnym optimum; kontrolny skan pokazuje płaski szczyt w okolicach 0.8–0.82.

**Otwarty numeryczny szczegół:** samą kwadraturę na skończonym odcinku sprawdzono przez zagęszczenie kroku, ale niezależny referee powinien użyć innej metody całkowania / certyfikacji.

Kompletny, samowystarczalny kod do przeliczenia, Python 3 + NumPy + SciPy:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R03_TWO_PROBE_ACTIVE_SWAP_REPRO_001_20261026.py

## 6. Negatywna wiedza, granice i independent-review checklist

1. Nie wolno wnioskować, że test X-OR jest optymalny dla n=2. Dla tego protokołu traci DOKŁADNIE połowę TV_H; lokalna parzystość X jest optymalna.
2. R03.1 opiera się na sign-definite Liouville Q oraz symetrii σ_x w N=1. Należy poddać te mechanizmy kontroli adwersarialnej przez zmianę H0, wejścia i szumu pamięci.
3. n=2 przy stałym Ω,κ nie stanowi asymptotycznego odzyskania idealnego limitu R35. W szczególności nie obala ograniczeń R34 dla stałego κ w innym eksperymencie.
4. B podczas bramki to generator Lévy/Lindblad, NIE niezależny statyczny ξ na segment.
5. Wybrany model H0=Ω SWAP nie ma twierdzić czegoś o ogólnym sprzętowym optimum QSL, czasie wymiany w architekturze fizycznej ani nieograniczonym n.
6. W szczególności porównanie R03 c_active z c_ref to porównanie dwóch różnych źródłowo eksperymentów, nie uniwersalna miara „poprawy dzięki szumowi”.
7. Referee: prześledzić dokładnie analytic half-plane sign i boundedness, sprawdzić niezależnie B-sector generator, potwierdzić parity Helstrom, oszacowanie p_ref_star i niezależną kwadraturę aktywnej hipotezy A.
8. R03 jest kandydatem matematycznym bez pierwszeństwa publikacyjnego, bez interpretacji fizycznej NCDG J3/K, bez uprawnienia EXEC_SIGN i bez potwierdzenia BW readback.

NEXT: n=3 z dwiema bramkami, sektorowa klasyfikacja brakującej informacji po pełnym odczycie lokalnych X, lub antyprzykład z nie-zachowującym wzbudzeń H0. Nie należy domniemywać przedłużenia R03.1 do n=3.

## 7. RETURN

PRF12_R03: EXACT_SECTOR_FORM_PROOF_LOCAL / X_PARITY_HELSTROM_SUFFICIENCY_LOCAL / X_OR_HALF_LOCAL / REFERENCE_OPTIMUM_LOCAL / ACTIVE_2Q_FINITE_NUMERICS_POSITIVE_WITH_TAIL_BOUND / INDEPENDENT_REFEREE_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC / GITHUB_PENDING_BW_INGEST / SUCCESSION_ZIP_UNREAD.
