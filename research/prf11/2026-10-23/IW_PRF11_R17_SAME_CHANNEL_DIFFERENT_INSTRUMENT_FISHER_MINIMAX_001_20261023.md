---
artifact_id: IW_PRF11_R17_SAME_CHANNEL_DIFFERENT_INSTRUMENT_FISHER_MINIMAX_001_20261023
created_at: 2026-10-23
as_of: 2026-10-23
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_10 / PRF11
function: FOUNDATION_FIRST / OTHERS_FIRST / MATURE_HOST_SUBTRACTION / EXACT_TYPE_SEPARATOR
document_type: REPORT
exposure: PUBLIC_SAFE
status: EXACT_CONDITIONAL_DERIVATION / INDEPENDENT_REFEREE_PENDING
primary_location: research/prf11/2026-10-23/IW_PRF11_R17_SAME_CHANNEL_DIFFERENT_INSTRUMENT_FISHER_MINIMAX_001_20261023.md
cross_surface_sync: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_CANON / NO_EXEC / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE
---

# PRF11 — obrót 17: ten sam kanał kwantowy, dwa instrumenty i dwie różne ilości informacji

## 0. Wyniki innych komórek i reguły projektu — najpierw stan osiągnięć

**Aktualny program MT13 zaakceptowany przez Moderatora 22.10.2026:** P2 obejmuje spójność Living Theory, odjęcie dojrzałych gospodarzy matematycznych oraz współpracę LT5, PRF11, Geeky-S10 i INT8. Obowiązuje autonomia komórek i reguła „jeden problem — jeden stan”; `PUBLICATION != BW_INGEST != REFEREE_PASS != OWNER_ADOPTION != CANON/EXEC`. Źródło: komunikat `MT13-NASH-RESEARCH-STATE-PRIORITIES-AUTONOMY-001_20261022` w `#iw-dispatch`.

**LT5 — 22 października:** Klasyczny reset składowej wektora `Q_s=I-s ee^T` nie jest ogólnie prawidłowym kanałem CPTP, gdy potraktować cały wektor jak wektor Blocha kubitu. LT5 udowodnił brak całkowitej dodatniości, dokładną odległość diamentową `s/2` od zbioru CPTP dla naiwnego unitalnego podniesienia oraz wskazał prawidłowy instrument Lüdersa `E_±=(I±s σ_x)/2` z nie-selektywnym kanałem `(r_x,r_y,r_z)→(r_x,k r_y,k r_z)`, gdzie `k=√(1-s²)`. **Cała ta konstrukcja i rozróżnienie kanału od instrumentu są osiągnięciem LT5**, nie PRF11.
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/2026-10-22/lt5_bloch_reset_noncp_exact_diamond_distance_and_instrument_nonmap_001.md

**Geeky-S10 i MT13 — 21–22 października:** W różnych klasycznych modelach szum może, lub nie może, wejść do bieżącego resetu, zmieniając warunkową czułość statystyczną; pod pewnymi kontraktami możliwe są zupełnie różne asymptotyki Fishera. Nie wolno przenosić ich bezpośrednio na kubit bez prawidłowego instrumentu i prawa wyników.
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s10/2026-10-22/geeky_s10_heterogeneous_mixed_noise_reset_common_storage_phase_001.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/2026-10-21/mt13_mixed_noise_reset_innovations_threshold_001.md

**XH-S4 — 22 października, pytanie Q6:** należy odróżnić całkowitą quantum Fisher information od klasycznej Fisher information faktycznie dostępnej przez określony słownik pomiarów oraz od straty konkretnego celu. R17 wybiera wąską, rozstrzygalną instancję tego pytania, bez ogłaszania ogólnego wyniku o QFI.
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s4/2026-10-22/IW_XH_S4_OCTOBER_RESEARCH_QUESTIONS_LINKS_AND_DISCRIMINATORS_012_20261022.md

**PRF11 R13–R16:** warunkowe klasyczne eksperymenty Gaussian/Le Cam przy jednym przygotowaniu, idealnym lub mieszanym resecie oraz różnych modelach korelacji. To odrębne nośniki praw i inne funkcje celu. R16 zapisano na Drive z odczytem kontrolnym, lecz zapis do GitHub był BLOCKED; brak potwierdzonej niezależnej recenzji R16.
https://drive.google.com/file/d/1IohMUya1yAgXJV8VLCxyjujW_4zxQkl0/view

## 1. Co rozstrzyga istniejąca teoria, a co pozostaje jako projektowe porównanie

Instument `{J_a}` to rodzina całkowicie dodatnich operacji, których suma jest CPTP. Instrument określa zarazem warunkowy stan **i** rozkład zarejestrowanego wyniku; sam nie-selektywny kanał `Λ=Σ_a J_a` nie określa rozkładu zapisów. To dawna teoria Daviesa–Lewisa, Choi, Ozawy i Lüdersa. Wielokrotne pomiary nieostrego obserwabla również mają dojrzałą teorię: Haapasalo, Heinosaari i Kuramochi (2016) udowodnili, że iterowane binarne nieostre pomiary Lüdersa w granicy mogą odzyskać ostry pomiar odpowiadający temu samemu obserwablowi. Ich twierdzenia o tym, że sekwencyjne pomiary niosą coraz więcej informacji, NIE należy ogłaszać ponownie.

Projektowe pytanie R17 po odjęciu prior art:

> W tej SAMEJ rodzinie stanów kubitu i przy tym SAMYM nie-selektywnym kanale ze źródła LT5, jak dalece mogą się różnić eksperymenty obserwatora i jakie są dokładne ograniczenia dostępnej informacji oraz błędu celu przy powtarzaniu pomiaru na jednej kopii?

To jest sprawdzalny przykład łączący LT5 z pytaniem XH Q6; nie pretenduje do nowego twierdzenia ogólnego.

## 2. Jedna rodzina stanów i dwa legalne instrumenty o identycznym kanale

Macierze Pauliego oznaczamy X=σ_x, Y=σ_y, Z=σ_z. Dla `|θ|<1/√2` rozważmy jedną przygotowaną kopię kubitu

`ρ_θ = [I + θ X + θ Y]/2`.

Dla siły `0<s<1`, `k=√(1-s²)`.

**Instrument A: nieostry pomiar Lüdersa σ_x.** Efekty `E_a=(I+a s X)/2`, a∈{+1,-1}; mapy selektywne `J_a^L(ρ)=√E_a ρ √E_a`. To poprawny instrument, ponieważ `E_a≥0` i `Σ E_a=I`. Kanał nie-selektywny:

`Λ_s(ρ_r)= ρ_(r_x, k r_y, k r_z)`.

Wyniki a mają `P_θ(a)=(1+a s θ)/2`; FI pojedynczego zapisu:

`I_L,1(θ)=s²/(1-s²θ²)`.

**Instrument B: flagowana losowa operacja unitarna.** Niech `p=(1+k)/2`. Mapy `J_0^U(ρ)=p ρ`, `J_1^U(ρ)=(1-p)XρX`. Są CP, ich suma jest CPTP. Wyniki 0,1 mają prawdopodobieństwa `p,1-p` niezależne od ρ i θ, stąd `I_U,1(θ)=0`. Jednocześnie na całym zbiorze stanów kubitu:

`Σ J_a^U(ρ)=pρ+(1-p)XρX = Λ_s(ρ) =Σ J_a^L(ρ)`.

Otrzymaliśmy dokładnie TEN SAM kanał nie-selektywny na dowolnym kubicie, lecz inne rozkłady zapisanych wyników. Dotyczy to wyłącznie dostępu do **klasycznego zapisu instrumentu**, bez dodatkowego pomiaru końcowego pozostałego kubitu. Jeśli końcowy kubit również jest dostępny, „brak informacji w etykiecie losowej operacji” nie jest brakiem całej informacji w układzie.

Powtarzanie N razy każdego z instrumentów, bez dodatkowych unitarnych rotacji, sterowania i interwencji, nadal daje tę samą średnią ewolucję stanu `Λ_s^N`, ale rekord random-unitary jest parametrowo niezależny i ma FI=0 dla KAŻDEGO N. Rekord Lüdersa nie.

## 3. Dokładna faktoryzacja procesu Lüdersa: jeden projektor σ_x jako gospodarz Blackwella

Wszystkie efekty `E_a` oraz pierwiastki `√E_a` komutują z `X`. Dla N kolejnych pomiarów na JEDNEJ kopii, pełny efekt sekwencji wyników `y=(y_1,...,y_N)` jest `∏_{j=1}^N E_(y_j)`; zatem

`P_θ(y) = [(1+θ)/2] L_+(y)+[(1-θ)/2] L_-(y)`, gdzie

`L_A(y)=∏_{j=1}^N (1+s A y_j)/2`, A=±1.

To dokładny eksperyment klasyczny generowany przez hipotetyczny *formalny* wynik jednorazowego ostrego pomiaru σ_x, `P_θ(A)= (1+θ A)/2`, po którym działa parametrowo niezależny kanał `A→Y^N`. Zmienna A jest pomocniczym zapisem faktoryzacji statystycznej POVM, nie postulowanym ukrytym bytem ontologicznym ani fizyczną wcześniejszą interwencją.

Stąd:
- `δ(E_sharp-X,E_L,N)=0`: sekwencję Lüdersa symuluje się klasycznie z wyniku ostrego σ_x.
- Wszystkie procedury estymacyjne i decyzyjne na Y^N są garblingiem jednego ostrego wyniku A.
- Dla `|θ|<1`, na mocy klasycznej monotoniczności FI:

`I_L,N(θ) ≤ I_sharp-X(θ)=1/(1-θ²)`.

Ta górna granica NIE rośnie z N. Jednej kopii nie można przekształcić w N niezależnych kopii przez powtarzanie jednego komutatywnego instrumentu.

**Dokładne FI skończonej sekwencji.** Przy `s∈(0,1)` i `m_0(y)=tanh(atanh(s) Σ_j y_j)` mamy

`P_θ(y)=P_0(y)[1+θ m_0(y)]`,
`∂_θ log P_θ(y)=m_0(y)/(1+θ m_0(y))`,
`I_L,N(θ)=E_θ[m_0(Y)^2/(1+θ m_0(Y))²]`.

Statystyka wystarczająca dla tego modelu to liczba dodatnich wyników (lub suma Σ y_j). Powyższe FI daje się obliczać dokładnie z N+1 wyrazów dwumianowych bez symulacji kwantowej wszystkich 2^N gałęzi.

## 4. Asymptotyka liczby i siły słabych pomiarów

**N s²→∞ (odzyskanie ostrego σ_x).** Warunkowo względem A, wyniki y_j są i.i.d. ±1 ze średnią s A. Większościowy estymator `Â=sign(Σ_j y_j)` (arbitralna parametrowo niezależna reguła rozstrzygania remisu) ma błąd `P(Â≠A |A) ≤ exp(-N s²/2)` z Hoeffdinga. Zatem

`δ(E_L,N,E_sharp-X) ≤ exp(-N s²/2)` i `Δ(E_L,N,E_sharp-X) ≤ exp(-N s²/2)`,

jednostajnie po θ. Przy N s²→∞ dwie rodziny eksperymentów stają się równoważne Blackwellowi/Le Cam w granicy. Co ważne, odzyskujemy **dokładnie ostry σ_x**, a nie pełną informację kwantową o całym stanie.

**N s²→0 (zanik całego eksperymentu).** Niech Q_N będzie N niezależnych uczciwych monet, niezależnych od θ. Warunkowa dystrybucja L_A ma

`KL(L_A||Q_N)=N g(s)`, gdzie
`g(s)=[(1+s) ln(1+s)+(1-s) ln(1-s)]/2 =s²/2+O(s^4)`.

Wypukłość KL zapewnia `KL(P_θ||Q_N)≤N g(s)` jednostajnie po θ, a Pinsker

`Δ(E_L,N,E_Q) ≤ sup_θ TV(P_θ,Q_N) ≤ sqrt(N g(s)/2)→0`.

Dla N s² rzędu 1 istnieje nierzadko nietrywialny statystyczny zakres pośredni; nie utożsamia się go ani z dokładnym projekcyjnym pomiarem σ_x, ani z brakiem informacji. To znany mechanizm wielokrotnych nieostrych pomiarów, nie nowy wynik NASH.

## 5. Całkowita informacja kwantowa, dostępna informacja klasyczna i minimalna strata celu

Dla `ρ_θ=(I+θX+θY)/2`, `|θ|<1/√2`, wzór na QFI kubitu

`F_Q(θ)=|∂_θ r|²+ (r·∂_θ r)²/(1-|r|²)`

daje **dokładnie** `F_Q(θ)=2/(1-2θ²)`. Ponieważ stany ρ_θ komutują dla różnych θ (kierunek Blocha jest stały), jednorazowy pomiar `σ_n=(X+Y)/√2` osiąga tę QFI. Sama rodzina pomiarów σ_x jest ograniczona przez

`I_L,N(θ) ≤ 1/(1-θ²) < 2/(1-2θ²) = F_Q(θ)`.

W θ=0 luka wynosi czynnik 2; dla ogólnego θ w dopuszczalnym przedziale nie znika. Także idealnie odtworzony projektor σ_x nie jest optymalnym przyrządem dla tej rodziny stanów. Pomiar `σ_n` daje inny legalny słownik dostępnych operacji; nie wolno przyznawać go aparaturze σ_x automatycznie.

**Dokładne ograniczenie decyzji, nie tylko FI.** Dla θ w przedziale [-R,R], `0<R<1/√2`, strata `(θhat-θ)²`. Przy JEDNYM idealnym wyniku `A∈±1` o prawie `P_θ(A)=(1+Aθ)/2` mamy minimaks

`J_sharp-X(R)=R²(1-R²)`.

Dowód: estymator `θhat(A)=R² A` ma błąd w punkcie θ równy `R^4+(1-2R²)θ²`, maksymalny na ±R, gdzie równa się `R²-R^4`. Przy równych wagach na dwóch parametrach ±R optymalny estymator Bayesa jest dokładnie `R² A`, a jego ryzyko wynosi `R²-R^4`, więc jest to również dolna granica minimaksowa. QED.

Cała sekwencja Lüdersa jest garblingiem tego A, stąd dla każdego N

`J_L,N(R) ≥ R²(1-R²)>0`.

Gdy Ns²→∞, zastosowanie estymatora `R² Â` z majority rule osiąga asymptotycznie `R²(1-R²)` (różnica ryzyka co najwyżej wielokrotność `R² exp(-Ns²/2)`). Bez danych minimaks wynosi R². Tak więc powtarzanie pomiarów na jednej kopii ma dokładnie ograniczoną korzyść w tym zadaniu: może odzyskać jakość jednego pomiaru σ_x, lecz nie sprowadza błędu do zera.

Dla N kolejnych niezależnych KOPII ρ_θ lub po legalnej zmianie słownika przyrządów sytuacja jest inna. W niniejszym twierdzeniu zasób to JEDNA kopia, jeden komutatywny instrument, brak rotacji i dostępu do końcowego kubitu poza zapisami.

## 6. Reprodukcja obliczeniowa — niezależna od dowodu

Dołączony kod `reproduce_r17_qubit_instrument.py` wykonuje:
- bezpośrednie kontrole macierzowe instrumentu Lüdersa i losowo-unitarnego (identyczny wynik kanału dla 4 sił i 3 parametrów);
- sumowanie sekwencyjnych CP operacji dla wszystkich 2^N wyników N=1,2,3,4 i porównanie z faktoryzacją Pθ(y) poprzez A;
- dokładne, numerycznie stabilne Fisher z dwumianowej statystyki wystarczającej, bez symulacji Monte Carlo;
- porównanie dostępnego FI z QFI oraz wartości dokładnego minimaksu.

`python reproduce_r17_qubit_instrument.py` (wymaga NumPy i SciPy): `CHANNEL_IDENTITY_AND_SEQUENCE_CARRIER: PASS`.

Przykład `s=0.2`, `θ=0.25`:

| N | FI zapisu Lüdersa | FI losowej operacji | QFI jednego stanu początkowego |
|---:|---:|---:|---:|
| 1 | 0.040100250627 | 0 | 2.285714285714 |
| 2 | 0.077640910788 | 0 | 2.285714285714 |
| 5 | 0.177758082051 | 0 | 2.285714285714 |
| 25 | 0.586407340396 | 0 | 2.285714285714 |
| 100 | 0.995290981830 | 0 | 2.285714285714 |
| 500 | 1.066656020428 | 0 | 2.285714285714 |

Limit FI projektora σ_x to `1/(1-0.25²)=1.066666666667`, a nie QFI 2.285714285714. Dla R=0.5 minimaks projektu σ_x wynosi 0.1875, wobec 0.25 bez jakiejkolwiek obserwacji. Żadne z tych liczb nie jest wynikiem fizycznego eksperymentu.

## 7. Dojrzałe źródła i rzeczywiste odjęcie prior art

1. E. B. Davies, J. T. Lewis, *An Operational Approach to Quantum Probability*, Communications in Mathematical Physics **17** (1970), 239–260, DOI 10.1007/BF01647093. Oryginalny gospodarz teorii instrumentów; sprawdzono metadane publikacji, nie pełną lekturę dowodów.
2. E. Haapasalo, T. Heinosaari, Y. Kuramochi, *Saturation of Repeated Quantum Measurements*, Journal of Physics A **49** (2016), 33LT01, DOI 10.1088/1751-8113/49/33/33LT01, https://arxiv.org/abs/1603.04271. **Bezpośredni dojrzały gospodarz** sukcesywnej nieostrej informacji i granicznego ostrego pomiaru; zweryfikowano artykuł w bazie instytucjonalnej i jego streszczenie; nie ogłaszać odzyskania pomiaru ostrego jako nowości.
3. T. Bullock, T. Heinosaari, *Quantum State Discrimination via Repeated Measurements and the Rule of Three*, Quantum Studies: Mathematics and Foundations (2020), DOI 10.1007/s40509-020-00233-7. Pierwotny artykuł w pełnym HTML wydawcy; zawiera jawne operatory efektów kolejnych pomiarów i badanie rozpoznawania stanów.
4. F. A. Pollock et al., *Operational Markov Condition for Quantum Processes* / teoria instrumentów wieloczasowych — kontekst strukturalny; bliższa formalizacja instrumentów w *Quantum Stochastic Processes and Quantum non-Markovian Phenomena*, PRX Quantum **2**, 030201 (2021), DOI 10.1103/PRXQuantum.2.030201. Pełny artykuł HTML z definicjami CP instrumentów i POVM przeglądnięty w zakresie relacji instrument–kanał–wynik.
5. Wzór na QFI kubitu, np. *Quantum Fisher and Skew Information for Unruh Accelerated Dirac Qubit*, European Physical Journal C (2016), DOI 10.1140/epjc/s10052-016-4290-7 (oryginalny tekst HTML, jawny wzór zależny od wektora Blocha). To gospodarz FORMUŁY, a nie źródło nowej teorii metrologii.
6. Ruskai, Szarek, Werner, *An Analysis of Completely-Positive Trace-Preserving Maps on M2*, Linear Algebra Appl. **347** (2002), DOI 10.1016/S0024-3795(01)00547-X, oryginalny host geometrii CPTP, użyty także przez LT5.

Wyszukiwanie publiczne 23.10.2026: `Lüders repeated unsharp qubit`; `saturation of repeated quantum measurements 2016`; `same nonselective quantum channel different instrument outcome probabilities`; `quantum Fisher qubit Bloch vector formula`; `Davies Lewis quantum instrument`; `single qubit repeated unsharp measurements Diósi`. To TARGETED HOST CHECK, nie kompletny systematyczny przegląd teorii kwantowych eksperymentów.

**Odjęcie nowości:** wszystkie użyte zasady są znane: instrumenty CPTP, dephasing/random unitary, działanie POVM, monotoniczność FI/Blackwell, Hoeffding, Pinsker, QFI i dwupunktowy minimaks. R17 jest odtwarzalną syntezą i precyzyjną odpowiedzią na lokalne rozróżnienie LT5/XH Q6. Nie jest nowym twierdzeniem matematycznym ani prawem fizycznym.

## 8. Granice i wynik operacyjny

EARNED:
- dwa dokładne poprawne CP instrumenty o **identycznej nie-selektywnej Λ_s** i dramatycznie różnej informacji w ich rekordach (0 wobec dodatniego FI);
- dokładna faktoryzacja danych sekwencji Lüdersa jako garbling jednego pomiaru σ_x i granica Fishera;
- dokładny minimaks strat dla idealnego σ_x i jego konsekwencja dla powtórzeń;
- wyraźne rozróżnienie QFI stanu od FI dostępnego tylko przez określony słownik odczytu;
- reprodukcja macierzowa i numeryczna.

NOT EARNED:
- twierdzenie o zachowaniu informacji dla dowolnych instrumentów albo dowolnych niekomutatywnych polityk z feedbackiem;
- zbieżność fizycznego urządzenia w nieskończonej liczbie strzałów w skończonym czasie;
- prawo kosztów zasobów, zasilania, energetyki, pasma czy rzeczywistej realizacji aparatu;
- uznanie pełnej QFI za dostępną w danej aparaturze;
- identyfikacja klasycznych przybliżeń NC/DTC/PBH z tym kubitem;
- recenzja właścicielska, integracja BW, kanon, EXEC lub odkrycie nowej fizyki.

**Werdykt:** `CHANNEL_EQUALS != INSTRUMENT_EQUALS != OBSERVATION_LAW_EQUALS`; `ONE_COPY_MULTISHOT != MANY_FRESH_COPIES`; `QFI != ACCESSIBLE_CLASSICAL_FI != TARGET_MINIMAX`. Wynik pełni funkcję bariery błędnych transferów do Żywej Teorii; autorstwo i decyzja o ewentualnym wykorzystaniu należą do LT5. Bez tworzenia nowego frontu lub obowiązku dla innych komórek.

`EXACT_CONDITIONAL_CLASSICAL_QUANTUM_EXPERIMENT_MAP / MATURE_HOST_ABSORBED / NO_CANON / NO_EXEC / NO_NOVELTY_CLAIM / BW_INGEST_PENDING`.