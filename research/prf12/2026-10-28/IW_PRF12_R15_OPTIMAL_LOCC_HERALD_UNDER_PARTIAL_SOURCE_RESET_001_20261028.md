---
artifact_id: IW_PRF12_R15_OPTIMAL_LOCC_HERALD_UNDER_PARTIAL_SOURCE_RESET_001_20261028
created_at: 2026-10-28
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
problem_id: PRF12_R14_HIDDEN_SOURCE_LIFETIME_RESET_AND_LOCAL_HERALD
exposure: PUBLIC
canonical_body_path: research/prf12/2026-10-28/IW_PRF12_R15_OPTIMAL_LOCC_HERALD_UNDER_PARTIAL_SOURCE_RESET_001_20261028.md
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_SEP_AND_LOCC_OPTIMAL_UNAMBIGUOUS_B_HERALD_FOR_ARBITRARY_KNOWN_RESET_PARTITION / EXACT_GLOBAL_BENCHMARK / INDEPENDENT_MATRIX_REPRO_PASS / REFEREE_PENDING
claim_ceiling: NO_SINGLE_BLOCK_MINIMUM_ERROR_LOCC_CLOSURE_GAP / NO_UNKNOWN_PARTITION_OPTIMALITY / NO_FINITE_SOURCE_ACTIVE_SWAPS / NO_HARDWARE_CERTIFICATION / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN
function: SCIENCE_FIRST / SOURCE_TYPED / NEGATIVE_KNOWLEDGE_PRESERVING / FALSIFIER_FIRST
---

# PRF12 R15 — Dokładne optimum LOCC/SEP bezbłędnego świadectwa B przy częściowym resetowaniu wspólnej częstotliwości Cauchy'ego

**Właściciel:** PRF12; 28.10.2026. **Wynik:** jawne, osiągalne optimum jednostronnego, bezbłędnego rozpoznawania B dla *dowolnego, z góry ustalonego podziału przebiegów na grupy ze wspólnym ξ*. Wykorzystuje wyłącznie pomiary symetrii pomiędzy przebiegami w obrębie każdego z trzech oddzielnych laboratoriów i komunikację klasyczną. Optymalność obejmuje WSZYSTKIE dodatnie efekty SEPAROWALNE, z dowolną liczbą rozdrobnionych wyników i rund, a nie tylko wybraną rodzinę lokalnych pomiarów. Nie jest to pierwotny problem minimum-error LOCC pojedynczego bloku z R09.

## 0. Scientific source map and external host subtraction

**Pierwszy właściciel źródła:** PRF11 R35, globalnie zamrożona statyczna częstotliwość ξ~Cauchy(0,γ) (A), kontra niezależne symetryczne przyrosty Cauchy–Lévy (B), końcowe stany idealnego protokołu SWAP. Pierwszy właściciel wyniku o ścisłym wpływie resetowania: PRF12 R14, https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-28/IW_PRF12_R14_SOURCE_RESET_AND_UNAMBIGUOUS_LOCC_AUDIT_001_20261028.md . R13 pomocnicza para P/2-vs-Q/4 i odrębny problem domknięcia LOCC; R09 wycofał nieuprawniony wniosek R07 dla binary coarse-graining. Nie przenosić R15 na ten problem.

**Dojrzała teoria zewnętrzna, BEZ roszczenia nowości:** Barnett, Chefles, Jex, *Comparison of two unknown pure quantum states*, Phys. Lett. A 307, 189–195 (2003), DOI https://doi.org/10.1016/S0375-9601(02)01602-X; Kleinmann, Kampermann, Bruß, *Unambiguous discrimination of mixed quantum states: Optimal solution and case study*, Phys. Rev. A 81, 020304(R) (2010), DOI https://doi.org/10.1103/PhysRevA.81.020304; Feng, Duan, Ying, *Unambiguous discrimination between quantum mixed states*, Phys. Rev. A 70, 012308 (2004), DOI https://doi.org/10.1103/PhysRevA.70.012308. Antysymetryczne testy, Schur–Weyl, podprzestrzenie całkowicie symetryczne, a także kryterium nośnika dla rozróżniania bezbłędnego są standardowymi metodami. Źródłowo specyficzna algebra R15 NIE ustanawia pierwszeństwa publikacyjnego.

## 1. Freeze of source AND operational contract

Jedna realizacja składa się z r≥1 przebiegów. Każdy przebieg zaczyna się od nowych trzech kubitów |+>³, obejmuje trzy równe ekspozycje Δ=T/3 oddzielone DWOMA idealnymi chwilowymi SWAP, bez starzenia przechowywanych kubitów (κ=0) i bez szumu w bramkach. Końcowo każde z trzech oddzielnych laboratoriów L1,L2,L3 posiada JEDEN kubit z każdego przebiegu. Laboratorium może przechowywać i wspólnie mierzyć swoje r lokalnych kubitów, lecz laboratoria nie wymieniają kubitów, nie dzielą splątania ani nie dysponują nielokalnymi bramkami. Komunikacja klasyczna jest dowolna.

Przebiegi podzielono na **znane, rozłączne grupy resetowania** G_1,...,G_g, o długościach m_1,...,m_g≥1 i Σ m_j=r. W hipotezie A każda grupa ma JEDNO wspólne ξ_j~Cauchy(0,γ) używane dla WSZYSTKICH trzech ekspozycji i WSZYSTKICH m_j przebiegów tej grupy. Wartości ξ_j są niezależnie losowane między grupami. W hipotezie B wszystkie przyrosty między ekspozycjami i przebiegami są niezależne. Nie wolno reinterpretować A jako „nowe ξ w każdym przebiegu”, chyba że wszystkie m_j=1.

Parametry: q=γΔ>0, x=e^(−q)∈(0,1), ρ_1=(I+xX)/2, p_+=(1+x)/2, p_-=(1−x)/2. Pod B stan wyjścia wszystkich 3r kubitów to ρ_1^{⊗3r}. Warunkowy na ξ_j stan A w jednej grupie to |u(z_j)>^{⊗3m_j}, gdzie |u(z)>=(|0>+z|1>)/sqrt2, z=e^(−i ξ_jΔ). Rozkład z_j ma pełny dodatni nośnik na okręgu; każdy z g niezależnych parametrów może być traktowany jako niezależny punkt okręgu.

**Cel:** jednostronne *unambiguous B*: efekt 0≤E_B≤I spełniający Tr(E_B ρ_A)=0; maksymalizujemy warunkowe Tr(E_B ρ_B). Inconclusive jest dozwolone. Prawdopodobieństwa poniżej są WARUNKOWE NA B, bez czynnika prior P(B). To NIE jest optymalność błędu Helstroma ani pełna dwustronna unambiguous discrimination.

## 2. Theorem R15.1 — exactly optimal THREE-LAB LOCC = SEP for arbitrary known reset grouping

Niech Sym^n(C²) będzie (n+1)-wymiarową podprzestrzenią permutacyjnie symetryczną n kubitów, a Π_n jej projektorem. Definiujemy podprzestrzeń JEDNEGO laboratorium i projektor:

  V_G = ⊗_{j=1}^g Sym^{m_j}(C²),   Π_V = ⊗_{j=1}^g Π_{m_j}.

Niech

  h_m(q)=Σ_{k=0}^m p_+^{m-k}p_-^k
        =(p_+^{m+1}−p_-^{m+1})/(p_+−p_-), q>0.

**Twierdzenie** (przy kontrakcie §1):

  **P_B-only^{LOCC,max}(G) = P_B-only^{SEP,max}(G)
  = 1−(∏_{j=1}^g h_{m_j}(q))³.**                      (R15.1)

Osiągnięcie: każdy z trzech uczestników mierzy lokalnie {Π_V,I−Π_V} na SWOICH kubitach, a następnie komunikuje 1 bit „niesymetryczny wynik lokalny?”. Wspólna decyzja „B” pada wtedy i tylko wtedy, gdy przynajmniej jeden uczestnik uzyska I−Π_V. Efektem pozytywnym B jest

  R = I−Π_V⊗Π_V⊗Π_V

(w przestrzennym porządku L1,L2,L3). R jest separowalnym efektem POVM, bo powstaje przez sumowanie siedmiu ortogonalnych PRODUKTOWYCH efektów pomiaru lokalnego; jego dopełnienie jest produktowe. Pod A każdy lokalny ciąg kubitów z grupy G_j ma postać |u(z_j)>^{⊗m_j}, zatem należy do Sym^{m_j}; R nigdy nie klika. Pod B każde laboratorium ma ρ_1^{⊗r}, a

 Tr(Π_{m_j} ρ_1^{⊗m_j})=h_{m_j}(q)

— wystarczy zdiagonalizować ρ_1 w lokalnej bazie X i policzyć znormalizowane Dicke states X-weight k, każdy o prawdopodobieństwie p_+^{m_j−k}p_-^k. Niezależność laboratoriów pod B daje formułę (R15.1).

**Optymalność względem WSZYSTKICH SEP:** A ma nośnik dokładnie

  S_A(G)=⊗_{j=1}^g Sym^{3m_j}(C²)

(grupujemy tu kwanty z TRZECH laboratoriów w kolejności zgodnej z grupami). Sprawdzenie nośnika: ciągłe rodziny |u(z_j)>^{⊗3m_j} rozpinają przestrzenie Sym^{3m_j}, bo jednomiany z_j^k, k=0...3m_j są niezależne na okręgu, a miara A jest na nim ściśle dodatnia.

Rozważ dowolny niezerowy wektor produktowy między LABORATORIAMI |a>_1⊗|b>_2⊗|c>_3. Jego skalarne nakrycie na każdy czysty wektor orbitalny A (z_1,...,z_g) ma postać

  f_a(z_1,...,z_g) f_b(z_1,...,z_g) f_c(z_1,...,z_g)

razy niezerowy czynnik normalizacyjny. Każdy f jest wielomianem wielowymiarowym o stopniu ≤m_j względem z_j. f_a jest identycznie zerowy wtedy i tylko wtedy, gdy |a> jest ortogonalny do V_G (współczynniki jednomianów to nakrycia na niezależne podprzestrzenie Dickego). Pierścień C[z_1,...,z_g] jest dziedziną całkowitości, a wielomian znikający na całym wielotorusie musi być zerowy. Ponieważ produkt wielomianów ma znikać identycznie przy zerowym false A, CO NAJMNIEJ jeden z f_a,f_b,f_c jest identycznie zero. Zatem każdy dopuszczalny produktowy ket świadczący bezbłędnie B ma co najmniej JEDEN lokalny czynnik w V_G^⊥ i cały taki wektor należy do Ran(R).

Każdy dodatni efekt SEP ma dekompozycję na nieujemne produkty rank-one. Z zerowej wartości Tr(E_Bρ_A), dodatniości i dodatniej gęstości A na orbitalnym nośniku wynika, że KAŻDY nietrywialny składnik musi być ortogonalny do S_A(G), zatem ma support w Ran(R). Stąd E_B=R E_B R, a ponieważ 0≤E_B≤I, zachodzi operatorowa nierówność E_B≤R. Wobec tego Tr(E_Bρ_B)≤Tr(Rρ_B), dokładnie równe wartości osiągniętej lokalnie powyżej. QED.

Argument obejmuje dowolnie wiele rozdrobnionych efektów SEPAROWALNYCH, nie zakłada wyniku dwóch zsumowanych efektów i nie powtarza błędu coarse-graining z R07/R09. Uzasadnia także górne ograniczenie dla całego LOCC oraz jego domknięcia przy ustalonym SKOŃCZONYM r, lecz tylko dla jednostronnego zdarzenia unambiguous B i tego modelu grup.

## 3. Theorem R15.2 — unrestricted GLOBAL one-sided benchmark, strict SEP gap

Optymalny GLOBALNY event B to projektor na dopełnienie dokładnego support A: E_B^global=I−Π_{S_A(G)}. Pod B produkt ρ_1^{⊗3r} daje

  **P_B-only^{GLOBAL,max}(G)=1−∏_{j=1}^g h_{3m_j}(q).**  (R15.2)

Ponieważ Sym^{3m_j}(C²) jest WŁAŚCIWĄ podprzestrzenią Sym^{m_j}(C²)⊗³ dla każdego m_j≥1, całe S_A(G) jest właściwą podprzestrzenią V_G^{⊗3}. Dla q>0 stan B jest pełnego rzędu, więc

  **P_GLOBAL^max−P_SEP^max
     =(∏_j h_{m_j})³−∏_j h_{3m_j}>0**          (R15.3)

przy KAŻDYM skończonym niepustym podziale G. To jest dokładna dodatnia luka dla *unambiguous B* GLOBAL kontra LOCC/SEP, niezależna od liczby rozdrobnionych wyników LOCC. Nie stanowi dodatniej luki Helstroma dla minimum-error na jednej kopii.

## 4. Source lifetime law: merging reset groups strictly increases local B-only power

Jeśli z G tworzymy G' przez MERGE dwóch grup o długościach m,n≥1, wówczas Sym^{m+n}⊊Sym^m⊗Sym^n, a ρ_1 ma pełny rząd dla q>0. Stąd h_{m+n}(q)<h_m(q)h_n(q); wprost (R15.1) daje

  P_LOCC,max(G') > P_LOCC,max(G).

Większa trwałość wspólnej ξ czyni A silniej ograniczonym strukturalnie; B łatwiej bezbłędnie odróżnić testem wspólnej symetrii. Ten wniosek dotyczy **znanej grupy resetowania**. Jeśli położenie resetu jest nieznane, wyznaczenie optymalnego pomiaru uśrednionego po takiej niepewności jest ODRĘBNYM problemem, nieprzeprowadzonym tutaj.

Kontrakty graniczne: wszystkie m_j=1 → h_1=1 → zero bezbłędnego separowalnego B zdarzenia przy każdej SKOŃCZONEJ liczbie niezależnych resetów (R14). Jedna grupa m=r≥2 → p_LOCC=1−h_r³>0. Gdy r→∞, przy JEDNYM wspólnym ξ i q>0, p_+<1, h_r→0, więc p_LOCC→1. Jest to *many-copy with persistent ξ* limit, NIE *many-round on ONE copy* LOCC closure.

## 5. Exact two-run and numerical examples

Dla m=2 oraz jednej wspólnej ξ:

  h_2=(3+x²)/4,
  P_LOCC,B-only=1−[(3+x²)/4]³
                =(1−x²)(x⁴+10x²+37)/64,
  h_6=(x⁶+21x⁴+35x²+7)/64,
  P_GLOBAL,B-only=(1−x²)(x²+3)(x²+19)/64,
  **P_GLOBAL−P_LOCC=(1−x²)(5+3x²)/16>0.**

At q=1/3 (x=0.716531310574):

| Known reset groups m_j | P_LOCC/SEP B-only | P_GLOBAL B-only |
|---|---:|---:|
| [1] | 0 | 0.243291440484 |
| [2] | 0.322344191560 | 0.521242588284 |
| [3] | 0.566702743165 | 0.697321090645 |
| [4] | 0.725551752298 | 0.808641671490 |
| [6] | 0.890264655544 | 0.923514735545 |
| [1,1,1,1] | 0 | 0.672120256938 |
| [2,1,1] | 0.322344191560 | 0.725859750657 |
| [2,2] | 0.540782605288 | 0.770791340727 |
| [3,1] | 0.566702743165 | 0.770960278506 |

**Operational reading:** For [2] at q=1/3 each of three labs performs one local SWAP antisymmetric test on its own two qubits; declare B if ANY lab sees antisymmetric. Conditional false-B-under-A is exactly zero. Detection B per 2-run macro-experiment ~32.23% instead of ~12.16% from a SINGLE lab in R14. With N independent repetitions of such 2-run macro-experiments under B, no herald appears with probability (1−0.322344...)^N; N=8 gives ≥95% chance of at least one unambiguous B certificate. The independence of such macro-experiments is an EXTRA resource/contract; there is no finite-m false positive even without it, but this N estimate uses independence under B.

## 6. Reproducibility and falsifiers

Independent Python 3/NumPy source: `IW_PRF12_R15_RESET_PARTITION_SEP_OPTIMAL_HERALD_REPRO_001_20261028.py` in this same directory. It constructs Dicke-subspace projectors from computational basis, builds ρ_1^{⊗m}, independently traces local and global support projectors and verifies orbit-invariance of all local symmetry tests. Tests q=.05,1/3,1,3 and nine partitions (36 independent fixtures, including a full global 2^(3r) matrix where 3r≤9); max discrepancy under machine precision. Prints the full q=1/3 table and eight-macro-experiment 95% check. The POLYNOMIAL integral-domain proof is analytic; random/finite matrix tests are not presented as proof of all SEP outcomes.

**Referee gates:** (i) verify independent wrapped Cauchy phases have full support on each group circle; (ii) prove the multivariate polynomial f_a=0 iff local vector lies in V_G^⊥, including possible entanglement WITHIN each lab across distinct groups; (iii) confirm E_B≤R for arbitrary positive SEP effect, regardless of classical coarse-graining; (iv) verify strict h_{m+n}<h_m h_n for q>0; (v) check global/SEP gap with correct 3-lab tensor ordering; (vi) avoid claiming unknown reset grouping, finite gate, fixed κ, hardware or single-copy LOCC closure success; (vii) check literature novelty separately before external claim.

**Negative knowledge:** unambiguous B-only ≠ two-sided unambiguous ≠ minimum-error Helstrom. Fixed source A lifetime across several runs ≠ independently re-drawn hidden ξ per run. Copies ≠ rounds. Mathematically separable optimum achieved by LOCC here, but this is not a general SEP=LOCC statement. No BW ingestion readback; independent referee pending; no publication priority, canon or EXEC_SIGN.

## 7. RETURN

PRF12_R15 / SOURCE_RESET_PARTITION_TYPED / EXACT_OPTIMAL_B_ONLY_LOCC_EQUALS_SEP / ARBITRARY_REFINED_SEPARABLE_EFFECTS_COVERED / EXACT_GLOBAL_B_ONLY_BENCHMARK / STRICT_GLOBAL_VS_LOCC_UNAMBIGUOUS_GAP / EXPLICIT_SOURCE_LIFETIME_MONOTONICITY / 36_MATRIX_FIXTURES_PASS / REFEREE_PENDING / NO_CANON / NO_EXEC / NO_NOVELTY / NO_SINGLE_BLOCK_MINERROR_LOCC_CLOSURE_CLAIM / GITHUB_PENDING_BW_INGEST.