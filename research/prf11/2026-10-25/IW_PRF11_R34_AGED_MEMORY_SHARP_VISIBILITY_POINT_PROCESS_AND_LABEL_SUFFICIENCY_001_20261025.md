---
artifact_id: IW_PRF11_R34_AGED_MEMORY_SHARP_VISIBILITY_POINT_PROCESS_AND_LABEL_SUFFICIENCY_001_20261025
created_at: 2026-10-25
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_10 / PRF11
problem_id: LT4_CH7_MULTI_SLOT_PROCESS_REALISTIC_AGED_MEMORY_VISIBILITY_AND_CLASSICAL_HISTORY_SUFFICIENCY
exposure: PUBLIC_SAFE
canonical_body_path: research/prf11/2026-10-25/IW_PRF11_R34_AGED_MEMORY_SHARP_VISIBILITY_POINT_PROCESS_AND_LABEL_SUFFICIENCY_001_20261025.md
bw_event_or_pending: GITHUB_PENDING_BW_INGEST
status: SOURCE_TYPED_ANALYTICAL_PROOF_AND_INDEPENDENT_FINITE_CONTROL_PASS / REFEREE_PENDING
function: SCIENCE_FIRST / OTHERS_FIRST / ERROR_AS_DATA / EXPLICIT_QUANTIFIER / MATURE_HOST_SUBTRACTION / FALSIFIER_FIRST
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE / NO_PHYSICAL_DEVICE_CALIBRATION / NO_UNRESTRICTED_MULTISLOT_OPTIMUM / NO_NEW_OWNER_TASK
---

# PRF11 R34 — pamięć o wieku próbek: ostra skala utraty rozróżnialności, granica niejednorodnego procesu Poissona i informacja w etykietach

**Data:** 25.10.2026. **Właściciel funkcji:** PRF11, monografia LT5/REV021 pozostaje pod osobnym autorstwem. **Klasa wyniku:** jawny matematyczny model procesów kwantowych ze *stałym harmonogramem próbek i SWAP*; nie jest to kalibracja urządzenia, weryfikacja grawitacji ani nowy mechanizm kwantowy.

## 0. Źródła najpierw; czego NIE przedstawiamy ponownie jako odkrycia

1. **PRF11 R29**: statyczna raz na doświadczenie częstość `ξ ~ Cauchy(0,γ)` kontra niezależne przyrosty Cauchy–Lévy dają jednakowe wszystkie jednoczasowe kanały CPTP, ale różne odpowiedzi na instrumenty. [Pierwotny pełny raport](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-24/IW_PRF11_R29_CONTINUOUS_SEMIGROUP_PROCESS_ECHO_AND_QUOTIENT_CONTRACT_001_20261024.md).
2. **PRF11 R30**: globalne optimum testera z JEDNĄ pośrednią interwencją, dowolnym instrumentem system+pamięć: `D_1^ideal(T)=1−exp(−γT)`. [Źródło](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-24/IW_PRF11_R30_FULL_ONE_SLOT_TESTER_NORM_CAUCHY_PROCESS_MEMORY_001_20261024.md).
3. **PRF11 R31**: stała seria `n` równych ekspozycji i `n−1` idealnych SWAP, idealnie chroniona pamięć oraz świadek wieloslotowy. **PRF11 R32**: `P_sym` jest optymalny wśród dowolnych KOŃCOWYCH POVM dla tej *konkretnej idealnej serii*, limit `2(1−exp(−a/2))`. [R31](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R31_MULTISLOT_SYMMETRY_MEMORY_PROCESS_NONMAP_001_20261025.md), [R32](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R32_ALL_N_HELSTROM_SYMMETRY_AND_WEAK_NOISE_SAMPLE_COMPLEXITY_001_20261025.md).
4. **PRF11 R33**, [raport](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R33_NOISY_MULTISLOT_POISSON_LIMIT_AND_MEMORY_VISIBILITY_GATE_001_20261025.md): JEDNA wspólna intensywność dekoherencji `r_n` aplikowana do KAŻDEGO z `n` kubitów końcowych. Wyliczył zanik dla `n(1−r_n)→∞` oraz skalę `r_n=exp(−b/n)`: dwie liczby Poissona, bo próbki są wymienne. **R34 zmienia właśnie tę kluczową przesłankę.** Nie wolno przenosić stąd wystarczalności samego licznika `K`.
5. **REC10 ROT32**: niezależny referee R31 `PASS_WITH_ALL_PARAMETER_HELSTROM_EXTENSION`; dowiódł `P_sym` przy `n=4` i wszystkie `q`, próg idealnej przewagi `a>2ln(7/3)`. [Źródło](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/rec10/2026-10-25/IW_REC10_ROT32_PRF11_FOURPROBE_SHARP_THRESHOLD_HELSTROM_REFEREE_20261025.md). Nie jest recenzją nowych R33/R34.
6. **Literatura dojrzała (prior-art subtraction):** Le Cam (1960), *An approximation theorem for the Poisson binomial distribution*, Pacific J. Math. **10**, 1181–1197, https://msp.org/pjm/1960/10-4/pjm-v10-n4-p11-p.pdf; Barbour–Brown (1992), *Stein's method and point process approximation*, Stochastic Processes and their Applications **43**, 9–31, DOI https://doi.org/10.1016/0304-4149(92)90073-Y; Ruzankin (2016), *On the rate of Poisson process approximation to a Bernoulli process*, J. Applied Probability, https://www.cambridge.org/core/journals/journal-of-applied-probability/article/on-the-rate-of-poisson-process-approximation-to-a-bernoulli-process/4D3EEA9382A6C8BF556519CF62AFA120. Źródła potwierdzają MATEMATYCZNYCH gospodarzy (aproksymacja oznakowanych rzadkich zdarzeń), nie źródłową realizację NASH z kubitami i szumem Cauchy'ego. Helstrom, Fuchs–van de Graaf, kowariancje/CPTP oraz statystyka procesów są wcześniejszą matematyką. Brak certyfikatu priorytetu R34.

## 1. Kontrakt zasobu: dokładnie różne okresy przechowywania

Ustal `a=γT>0`, całkowity czas `T>0`, `n≥2`, `Δ=T/n`, `q_n=e^(−a/n)`. System S w przedziale `j=1,...,n` podlega temu samemu modelowi fazowemu z R29. Po zakończeniu przedziału `j<n`, idealny SWAP przenosi już naświetlony stan do osobnego kubitu pamięci; kubit ten podlega aż do końca doświadczenia zwykłej NIEZALEŻNEJ dekoherencji fazowej ze stałą szybkością `κ_n≥0`. Ostatnia próbka `j=n` nie wymaga późniejszego przechowywania. Wszystkie pozostałe operacje SWAP są idealne i natychmiastowe. Model nie dodaje pamięci szumu podczas samej ekspozycji ani błędów SWAP; te luki są jawne i nie są równoznaczne z fizycznym urządzeniem.

Współczynnik widoczności próbki `j`:

```
c_n=κ_n T;   r_(n,j)=exp[-κ_n(T−j Δ)]=exp[-c_n(n−j)/n];
q_n=exp(−a/n),   j=1,...,n.                                   (34.1)
```

Ostatnia próbka ma `r_(n,n)=1`, najstarsza `r_(n,1)=exp[−c_n(n−1)/n]`.

Dla słów `x,y ∈ {0,1}^n`, `d_H(x,y)=# {j:x_j≠y_j}`, `|x|=Σ x_j`, stany końcowe mają DOKŁADNIE elementy

```
ρ_A(x,y)=2^(−n) exp[−(a/n) ||x|−|y||] ∏_{j:x_j≠y_j} r_(n,j),
ρ_B(x,y)=2^(−n) exp[−(a/n) d_H(x,y)]  ∏_{j:x_j≠y_j} r_(n,j).  (34.2)
```

To pełne legalne macierze gęstości; `A` to jedna wspólna `ξ` Cauchy'ego na całe doświadczenie, `B` to niezależne przyrosty. Każda pamięć ulega TYM SAMYM kanałom w obu hipotezach. W formie produktowej, przy `σ_(r,θ)=[I+r(cosθ X+sinθ Y)]/2`, `σ_r=σ_(r,0)` i `θ~Cauchy(0,a/n)`:

```
ρ_A=E_θ ⊗_(j=1)^n σ_(r_j,θ),
ρ_B=⊗_(j=1)^n σ_(r_j q_n),
τ_n =⊗_(j=1)^n σ_(r_j).                                    (34.3)
```

`τ_n` to stan REFERENCYJNY, nie dodatkowa hipoteza fizyczna. Mamy `ρ_B` oraz `τ_n` komutujące w lokalnych bazach X; `ρ_A` może być niekomutujący. Twierdzenia R34 dotyczą **maksimum po końcowych wspólnych POVM** dla tego zamrożonego systemu/protokołu, nie maksimum po wszystkich innych sterowaniach wieloslotowych.

## 2. Lemma R34.1: niezależnie od czasów życia, wspólna Cauchy faza staje się niewidoczna w normie śladowej

Dla dowolnego ciągu `0≤r_j≤1`, równych wspólnych faz `θ`, kwadrat wierności qubitów jest

```
F(σ_(r_j,θ),σ_(r_j,0))=1−r_j² sin²(θ/2).
```

Dzięki multiplikatywności wierności i nierówności Fuchsa–van de Graafa, dla każdej wartości θ:

```
|| ⊗σ_(r_j,θ) −⊗σ_(r_j,0)||_1
  ≤2 sqrt[1−∏_j(1−r_j² sin²(θ/2))]
  ≤ min{2, sqrt(n)|θ|}.
```

Po uśrednieniu θ z rozkładu Cauchy'ego o skali `a/n`, NIGDY nie używamy nieistniejącej wartości `E|θ|`. Dokładne całkowanie funkcji `min(2,√n|θ|)` daje, przy `z=a/√n`:

```
||ρ_A−τ_n||_1 ≤ ε_A(a,n)
   := (z/π) log(1+4/z²) +(4/π) arctan(z/2)
    = O_a(log n/sqrt(n)) →0.                               (34.4)
```

Jest to UNI-FORM względem całej heterogenicznej pamięci `r_j`. Nie wynika stąd, że `ρ_A` jest dokładnie `τ_n` w skończonym eksperymencie ani że źródłowy szum Cauchy stał się Markowowski. Wynika tylko asymptotyczna nierozróżnialność tego konkretnego wyjścia przy skali kąta `a/n`.

## 3. Twierdzenie R34.2: ostry warunek zaniku pełnej informacji kwantowej

Zdefiniuj **łączny wskaźnik obciążenia pamięci** `h_n=n c_n=n κ_n T`. Jeśli

```
h_n→∞  (przy stałym a>0),
```

to

```
||ρ_A^(n)−ρ_B^(n)||_1 →0.                              (34.5)
```

Oznacza to brak asymptotycznej przewagi dla KAŻDEGO, także splątanego, pomiaru końcowego. W szczególności dotyczy każdej stałej `κ>0,T>0`, dla której `c_n=κT>0` i `h_n` rośnie liniowo z liczbą próbek. Konkluzja nie dotyczy sterowania pośredniego innego niż opisany SWAP.

**Dowód (eliminacja wcześniejszej pozornej luki logarytmicznej).** Komutujące stany `σ_(r q),σ_r` mają kwadrat wierności spełniający dla `r<1` standardową nierówność Hellingera/χ²

```
1−F(σ_r,σ_(rq)) ≤ r²(1−q)²/(1−r²).
```

Numeruj próbki w odwrotnej kolejności według ich wieku `k=n−j=0,...,n−1`, tak że `r_k=e^(−c_n k/n)`. Przy `k>=1`:

```
r_k²/(1−r_k²)=1/(exp(2c_n k/n)−1) ≤ n/(2c_n k).
```

Dla dowolnego `1≤m≤n`, oddziel `m` NAJMŁODSZYCH próbek `k=0,...,m−1` od starszych. Na młodszych zwykłe teleskopowanie różnic stanów daje

```
||τ_young−ρ_B,young||_1 ≤Σ_(k<m) r_k(1−q_n) ≤ a m/n.
```

Na starszych wierność iloczynów i nierówność `1−∏F_j ≤Σ(1−F_j)` dają

```
||τ_old−ρ_B,old||_1
 ≤2(1−q_n) sqrt[ Σ_(k=m)^(n−1) 1/(exp(2c_n k/n)−1)]
 ≤2a sqrt[ (Σ_(k=m)^(n−1) 1/k)/(2n c_n)].
```

Zatem dla `h_n=n c_n≥1` wybierz `m_n=ceil(n/sqrt(h_n))`, ograniczone do `[1,n]`. Mamy `m_n/n≤1/sqrt(h_n)+1/n` i `Σ_(k=m_n)^(n−1)1/k≤(log h_n)/2+1`, ponieważ `m_n≥n/sqrt(h_n)`. Dostajemy jawną, w pełni kwantową nierówność

```
||ρ_A−ρ_B||_1
 ≤ε_A(a,n)+a(1/sqrt(h_n)+1/n)
   +2a sqrt[(1+(log h_n)/2)/(2 h_n)].                     (34.6)
```

Wszystkie trzy człony zanikają, gdy `n→∞` i `h_n→∞`, niezależnie od tego, jak powoli `h_n` rośnie. **Nie potrzeba silniejszego `h_n/log n→∞`** wynikającego z naiwnego sumowania wszystkich odwrotności `1−r_k`. Rzadkie niemal idealne młode próbki usuwa się osobno; tracą łącznie najwyżej `am_n/n`. Dowód obejmuje pełną przestrzeń końcową `2^n`, a nie jedynie określony pomiar X.

## 4. Twierdzenie R34.3: graniczny eksperyment to NIEJEDNORODNY proces Poissona na wieku próbek

Jeśli `h_n=n κ_n T→β∈[0,∞)` i `a>0` jest stałe, zdefiniuj dwie niezależne, klasyczne **miary praw procesów Poissona** na przestrzeni konfiguracji punktów w `[0,1]`, o intensywnościach

```
λ_A(u)= β u/2,
λ_B(u)= (β u+a)/2.                                       (34.7)
```

Punkt `u=0` odpowiada ostatniej, najmłodszej próbce; `u=1` najstarszej. Niech `Π_A,Π_B` oznaczają pełne konfiguracje tych procesów, z ZACHOWANYMI położeniami/etykietami punktów. Wtedy

```
lim_(n→∞) ||ρ_A^(n)−ρ_B^(n)||_1
     = 2 TV(Law(Π_A),Law(Π_B)).                            (34.8)
```

Prawa strona jest ściśle dodatnia dla `a>0` i skończonego `β`. Co więcej, jej optimum w granicy osiąga się przez **LOKALNE pomiary każdego kubitu w bazie X** z ZACHOWANIEM etykiety próbki `k` i dowolny klasyczny test na pełnej konfiguracji ujemnych wyników. W ogólności nie wystarcza samo zliczenie `K`.

**Dowód: krok quantum→commuting.** R34.1 daje `||ρ_A−τ_n||_1→0` bez dodatkowych warunków na `β`. Z drugiej strony `ρ_B=⊗σ_(r_k q_n)`, `τ_n=⊗σ_(r_k)` komutują i diagonalizują się wspólną bazą X. Ich śladowa odległość wynosi dokładnie `2 TV` *pełnych oznakowanych sekwencji* niezależnych wyników Bernoulliego

```
p_(A,k)=(1−exp(−h_n k/n²))/2,
p_(B,k)=(1−exp[−a/n−h_n k/n²])/2,
     k=0,...,n−1.                                         (34.9)
```

Ponieważ `||ρ_A−τ_n||_1→0`, różnica między pełną normą Helstroma a tą klasyczną `2TV` zanika. Wniosek o asymptotycznej optymalności lokalnego odczytu ma TEN SAM błąd górny; nie wymaga założenia o diagonalności skończonego `ρ_A`.

**Dowód: krok Bernoulli→oznaczony PPP, NIE tylko liczba punktów.** Dla `h_n→β`, `p_(H,k)=λ_H(k/n)/n+O(1/n²)+o(1/n)` z dokładną definicją źródłową (34.9). Stwórz na każdym przedziale wieku `I_k=[k/n,(k+1)/n)` odrębny jednorodny proces Poissona o stałej intensywności `n p_(H,k)`. Jego oczekiwana liczba punktów w komórce to `p_(H,k)=O(1/n)`. Prawdopodobieństwo DWÓCH lub więcej punktów w dowolnej komórce ogranicza suma `O(Σp_k²)=O(1/n)`. Po sprowadzeniu każdej komórki do wskaźnika `0/1`, odległość całkowitego wahania od niezależnych Bernoullich jest `O(Σp_k²)`. Gdy każda komórka ma najwyżej jeden punkt, jego położenie jest jednostajnie rozłożone w I_k w OBU hipotezach; dodanie takich etykiet wewnątrz komórki nie zmienia TV. Wreszcie skokowe intensywności `u→n p_(H,k)` zbiegają w `L¹[0,1]` do `λ_H(u)`; wzajemna TV procesów Poissona jest ograniczona prawdopodobieństwem niedopasowania w standardowym sprzężeniu/superpozycji, nie większym niż całka `L¹` różnicy intensywności. Stąd pełne TV oznakowanych sekwencji dąży do `TV(Π_A,Π_B)`, bez nieuprawnionego usuwania etykiet. QED.

**Dokładny znacznik log-likelihood.** Dla β>0 oba PPP mają skończone intensywności `μ_A=β/4`, `μ_B=β/4+a/2`. Dla konfiguracji `ω={u_1,...,u_m}` bez punktu dokładnie w 0 (zdarzenie prawdopodobieństwa jeden), iloraz wiarygodności wynosi

```
L(ω)= dP_B/dP_A(ω)
     = exp(−a/2) ∏_(u∈ω)(1+a/(β u)).                      (34.10)
```

Optymalny test końcowy deklaruje B, gdy `L(ω)>1`. **Nie jest to funkcja samego `m=|ω|`**, bo każdy punkt niesie informację o swoim wieku `u`. Przy β=0, Π_A jest pusty a Π_B jest jednorodny PPP z `μ_B=a/2`; tylko w tym szczególnym przypadku TV=`1−e^(−a/2)`.

**Poprawny wariant dla nieustalonego h_n.** Jeżeli `h_n` jest jedynie ograniczony, każda podsekwencja z `h_n→β` ma własną granicę `2TV(Π_A^β,Π_B^β)`; bez konwergencji `h_n` nie twierdzimy o jednej granicy. Ponieważ test "zero punktów vs jakikolwiek punkt" daje co najmniej `e^(−β/4)(1−e^(−a/2))`, **`liminf_(n→∞) ||ρ_A−ρ_B||_1 >0` wtedy i tylko wtedy, gdy `h_n` jest ostatecznie ograniczony**. Kierunek przeciwny wynika z R34.2 wzdłuż podsekwencji `h_n→∞`. To jest w tym zamrożonym modelu ostre kryterium **utrzymania dodatniej rozróżnialności** dla dowolnej serii `κ_n`.

## 5. Twierdzenie R34.4 — jawny nieciąg logiczny: liczba zdarzeń NIE jest statystyką dostateczną

Po zapomnieniu etykiet wieku obserwujemy wyłącznie `K=|ω|`. Wtedy

```
K_A~Pois(β/4),  K_B~Pois(β/4+a/2).                      (34.11)
```

To są dokładnie dwie rozkłady R33 po zamianie `b=β/2`; jednak R33 miał **wymienne** próbki i tam K był dostateczny. W R34 uzyskujemy wyłącznie bezpieczną nierówność

```
TV(Π_A,Π_B) >= TV(Pois(β/4),Pois(β/4+a/2)),             (34.12)
```

z nierównością ŚCISŁĄ dla wielu parametrów. Co ważne, można ją poświadczyć **analitycznie na zdarzeniu dokładnie jednego punktu**.

Dla β>0 różnica nieznormalizowanych gęstości konfiguracji z JEDNYM zdarzeniem o wieku u (prawo B minus A) jest

```
Δ_1(u)=e^(−β/4)/2 [A−B u],
A=a e^(−a/2),   B=β(1−e^(−a/2)).                         (34.13)
```

Gdy `u_*=A/B∈(0,1)`, znak zmienia się wewnątrz tej samej klasy zdarzeń `K=1`. Zatem licznik K gubi informację i pełne TV jest ściśle większe. Ostry, jawny DODATNI przyrost **tylko z podziału tej klasy** ma wartość

```
G_1(a,β) = min{e^(−β/4) A²/(4B),
               e^(−β/4) B(1−u_*)²/4} >0.                (34.14)
```

Wynika to z `1/2 (∫|Δ_1|−|∫Δ_1|) = min(positive mass,negative mass)`. Inne liczby zdarzeń mogą dać dalszą korzyść.

**Ważny kontrprzykład dla błędnego transferu progu R33.** Weź `a=4 ln 2`, i `β=2.3726585437041354...` uzyskane przez *pooled count only* równość z idealnym `D_1`: `2TV(Pois(β/4),Pois(β/4+a/2))=1−e^(−a)=15/16`. Tu `u_*≈0.3895192771`, `G_1≈0.03729806462`. Zatem źródłowo, bez symulacji, mamy

```
2TV(Π_A,Π_B)
 >= 15/16+2(0.03729806462...) >15/16.                (34.15)
```

**Czyli β=2 bcrit_R33 NIE jest ostrym progiem R34.** Ten β pozostaje wystarczającą bazą licznikową: poniżej niego sam licznik już daje przewagę, a przy tym β etykiety zapewniają jeszcze przewagę. Nie deklarujemy nieobliczonego dokładnego `βcrit_full`; istniejące narzędzia klasycznego testowania konfiguracji mogą go wyznaczyć. To R34 jest istotnym samosprostowaniem pierwszej hipotezy badawczej — nie pominięto go przy publikacji.

Dla `a=4ln2, β=1.5` mamy `u_*≈0.6161308272`, `G_1≈0.02848384240`: również tam etykiety są matematycznie istotne. Z kolei gdy `e^(−a/2)(1+a/β)>1`, nawet pojedynczy punkt w NAJMNIEJ korzystnym wieku przemawia za B; dla tak małego β test "jakikolwiek punkt" może być optymalny. Nie twierdzimy, że każda heterogeniczna seria musi mieć ścisłą lukę przy wszystkich parametrach.

## 6. Kontrole wykonane, nie zastępują dowodów

**Nowy, odrębny kod** `reproduce_prf11_r34.py` (NumPy/SciPy; bez importowania PRF/NC/REC/MT) wykonany po historycznym odczytaniu R29–R33 i najnowszego REC10. Są to kontrole NIEZAŚLEPIONE. Zamrożone lokalne JSON `prf11_r34_results.json` zawiera:

1. **42 pełne kwantowe** kontrole macierzy gęstości dla `n=2,...,8` × `c=0,.01,.05,.1,.2,.5`, `a=4ln2`, wraz z niezależnym tensorowym odtworzeniem `ρ_B`, dodatniością, śladem, idealnym `c=0` i dolną granicą X POVM. Skończone c zostały wybrane jako kontrola skuteczności i strat — nie jako kalibracja pamięci fizycznej.
2. **Skończony świadek utraty przewagi**: `n=4,a=4ln2`, idealny jednoslotowy próg `15/16`. W naszym konkretnym wariancie heterogenicznego szumu, pełna numeryczna norma `||ρ_A−ρ_B||_1` przekracza próg przy `c=.1` (`≈.9712180667`), ale spada poniżej przy `c=.2` (`≈.8959345331`). Numeryczne miejsce przecięcia `c≈0.14352520526552`. Ciągłość jest ścisła; monotoniczna nierosnąca zależność od c wynika z dalszej kompozycji kanałów CPTP. NIE twierdzimy o certyfikacji interwałowej liczby dziesiętnej ani o fizycznym krytycznym lifetimie.
3. **12 bezpośrednich, pełnych rozkładów klasycznych z zachowaniem etykiet** dla `n=8,12,16,20`, trzech par `(a,β)`. Dla `a=4ln2,β=1.5` przy n=20 mamy `TV_labeled≈0.5314211 > TV_count≈0.5142612`. Dla `a=4ln2,β=2.3726585438` przy n=20: `0.4906250 >0.4376673`. To jest 2^n KLASYCZNYCH wartości, a nie `2^n` macierzy diagonalizowanych dla n=20.
4. **7 wartości β do procesu Poissona z samą liczbą zdarzeń** i trzy poziomy `n=100,1000,10000`; **WYRAŹNIE OZNACZONE JAKO DOLNE GRANICE**, nie pełne limity R34. Dojrzała aproksymacja sum niezależnych Bernoulli jest standardowym Le Cam; pełny limit wymaga także znaczników.
5. **6 pomocniczych progów licznikowych**, równych `2 bcrit_R33(a)`. Ich status w R34 to tylko wystarczający dolny budżet; w danych JSON znajduje się także `G_1(a,β)` sprawdzające, czy w tym punkcie na pewno NIE jest progiem optymalnym.
6. **12 dużych n analitycznych oszacowań** zaniku z (34.6), nie żadne `2^1000000` diagonalizacje.

**Error-as-data, zachowane w rozróżnieniu kod/teoria:** W pierwszej wersji skryptu suma wag bitowych była `uint` i odejmowanie w module dawało przepełnienie: kontrola PSD FAIL, kod naprawiono (`int64`). Następnie test masy Poisson-binomial w podwójnej precyzji miał nieodpowiednio jednostronne wymaganie `1−sum(p)>=0`, choć roundoff dawał `−5.5e−13`: zmieniono wyłącznie tolerancję do `|1−sum p|<1e−8`. Najważniejsza samokorekta jest MATEMATYCZNA: pierwotnie przyjęto błędnie, że `K` pozostaje dostateczne przy heterogenicznych `r_j`; odrzucono ją PRZED zapisem raportu, dowiedziono (34.13–14), a implementację rozdzielono na `TV_labelled` i `TV_count_only`. Żaden z tych błędnych przebiegów nie jest nazywany PASS, a źródłowych skryptów R33/REC10 nie modyfikowano.

Do uruchomienia i niezależnego odtworzenia wystarczają Python 3, NumPy i SciPy, bez prywatnych runtime oryginalnego NCDG/DTC. W pakiecie ZIP znajdują się pełny raport, kod, JSON, README oraz manifest SHA-256; wykonanie w czystym katalogu jest osobnym testem custody i nie stanowi dowodu nowości naukowej.

## 7. Zastosowanie logiczne i STOP

- **SOURCE R33 equal endpoint visibility** ≠ **R34 różne czasy życia próbek**. W R34 lokalne etykiety wieku są częścią danych i nie mogą zostać automatycznie uśrednione.
- **Lokalne X z pełnymi etykietami jest asymptotycznie optymalne** w *tym* modelu; **sam licznik K jest nieoptymalny** w części zakresu. Nie jest ogólnym dowodem, że lokalne pomiary są optymalne dla wszystkich procesów kwantowych.
- **Dodatnia przewaga dla n skończonego** jest zgodna z **zanikiem dla n→∞ przy stałym κ>0**. Optymalna praktyczna liczba próbek musi uwzględniać czas życia pamięci, koszt SWAP i dopuszczalny błąd — żadnej kalibracji tych zasobów nie przeprowadzono.
- **Procesowa pamięć ξ per run** ≠ reset środowiska przy SWAP. Reset uczyniłby A=B i unieważnił świadek, a nie wzmocnił wniosek.
- **Ostre kryterium `nκ_nT`** jest własnością właśnie wybranego harmonogramu, Hamilonianu fazowego, źródłowych modeli i ochrony qubitów. Nie przenosi się na arbitralne procesy, modele Lindblada z błędami bramek ani wszystkie strategie testerów wieloslotowych.
- **Brak** wyników o realnym kubicie, sprzęcie, kwantowej grawitacji, NCDG K/J3, DTC0a, PBH/BBN, ani nowych zjawisk matematycznych o potwierdzonym pierwszeństwie. Odłożone są niezależne REC10/NC referee i autorska decyzja LT5 o integracji. BW ingestion niepotwierdzony; brak EXEC_SIGN.

**Status:** `MATHEMATICAL_SOURCE_TYPED_PROOF_PASS / FINITE_MATRIX_AND_LABELED_POISSON_CONTROLS_PASS / NEW_THEOREM_EXTERNAL_REFEREE_PENDING / GITHUB_PENDING_BW_INGEST / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE / NO_NEW_TASK`.
