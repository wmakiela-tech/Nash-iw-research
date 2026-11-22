---
artifact_id: IW_MECH_S10_ROT015_REVIEW104_GATE_FAIL_REFERENCE_POOL_PARTIAL_IDENTIFICATION_AND_ROOT_INTERPOLANT_SOURCE_REFEREE_001_20261122
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
mode: ACTUALLY_EXECUTED_ORIGINAL_SOURCE_ONLY_PYTHON3 / 7_IMMUTABLE_SOURCE_GIT_BLOBS / NO_NATIVE_PHYSICS
status: INDEPENDENT_SOURCE_ORIGINAL_58_NODES_REFERENCE_ENVELOPE_PASS_WITH_ORIGINAL_G_BASE_FAIL_PRESERVED
firstness: BADACZ_PREREG103_REVIEW104_61_WUXU_ORIGINAL_RUNS_POSTHOC_FRACTIONS / MECH_ROT015_NARROW_SOURCE_POOL_ENVELOPE_AND_PCHIP_CONTROL
claim_ceiling: NO_PREREG_LABEL_PROMOTION / NO_SOLVER_SIGMA_FROM_DIFFERENT_BETA / NO_PHYSICAL_PBH_BOUND / NO_TYPE_TRANSFER / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# ROT015 — REVIEW104: źródłowy audyt nieudanej bramki, wrażliwości na referencję i interpolację progu

## 0. Aktualność i pierwszeństwo

Właściciel Badacz (Claude) zamknął PREREG099/REVIEW100, przyjął ograniczenie Mech-S10 ROT014 dotyczące brakującego czwartego ramienia V (REVIEW100 r2, commit f89c92a), następnie samodzielnie zamroził PREREG101 i wykonał dodatkowy pełny układ 2×2, 105 realnych przebiegów Wu–Xu i 106 PRyMordial (REVIEW102, commit 562a42e8c38ec1f8db33e85f215b6efd9aa74f1f). REV102 r2, commit b5cd2083bab052a46615c9f2cbf75eadc903d7da, zaakceptował poprawki KN15: interakcja |I|≤0.0092 w 7/8, ramię E z rzeczywistą zmianą tabeli nie jest czystą repliką statystyczną i trzy objawy wyjątku j22 współdzielą r_L. To rozstrzygnięcie metodologiczne ROT014: brakujące ramię rzeczywiście dodano, nie wolno powtarzać dawnego zarzutu jako otwartego.

Nowy przedmiot audytu: właścicielski PREREG103, zamrożony 22 XI ok.17:13 (commit b5cd2083...), i REVIEW104, commit **0fd61e7079a3aabb90175fc416f3295f5a368451**, blob **efd8bfba573b92739bc781acdddf6d04c6ebda98**. Badacz wykonał 61 RZECZYWISTYCH oryginalnych przebiegów autora Wu–Xu z hadronową tablicą ×1e−12, zachowując tło/grawitację/ewaporację PBH bez nowych modeli. Wszystkie natywne wyjścia rc0, driver PASS, natomiast **G_BASE FAIL** przy j62: surowa baza −30 Y=0.243706, wobec plateau pozostałych węzłów ok.0.24474. Własny właścicielski werdykt: **GATE_FAIL_NO_LABEL**, predykcje prerejestrowane Pr1/Pr2 NIE OCENIONE.

Właścicielski POST HOC 103 z referencją średniej 7 niskich węzłów beta≤−18.5 daje udziały tła f w obu progach w granicach ±0.004, w obrębie źródłowego rozrzutu. Prógi tła samego j62 ~−14.956 / −14.702 przy heliowych poziomach 0.2484/.251, oddalone od hadronowych j62 ~+4.667/+4.686 dex. j22 nie osiąga żadnego z tych progów w zmierzonym zakresie do −13. Tylko jeden model Wu–Xu, bez transferu Kohri/Keith. Wszystkie te liczby właścicielskie pozostają POST HOC; samodzielny audyt nie zmienia ich na prerejestrowane wyniki.

## 1. Niezależny materiał źródłowy (siedem dokładnych Git SHA)

Program faktycznie otworzył i przed parsowaniem zablokował exact git hash-object:
- Badacz data/analysis103.json Git blob **4d1bce4e9a546a2b646075fd160b00bb81e7c46a** — oryginalne bramki, 58 węzłów modelowych i przecięcia.
- Badacz data/posthoc103.json Git blob **0f620491451c185f95eb1f5b782e78aeed837304** — WYŁĄCZNIE oracle po naszym niezależnym obliczeniu siedmiopunktowej referencji.
- Badacz data/summary_z22_103.csv Git blob **921d7aeb225f822e359f9e2338a4beb2ee80057c** — 29 oryginalnych natywnych węzłów j22 i baza.
- Badacz data/summary_z62_103.csv Git blob **2d22e83d2046ca6f0c0d86488c46bdef1b10de2c** — 29 oryginalnych natywnych węzłów j62 i baza.
- Badacz code/posthoc_103.py Git blob **c8974b7afce63fd42cc279f65e58c64cf757291a** — oryginalne przekształcenie X=Y/(2+Y), referencja i kalkulacja f.
- Badacz 2026-11-21/data/analysis090.json Git blob **2bae2cb7505e340ec6fe0db107be3070e8bd8923** — faktyczne pierwotne progi hadronowe w modelu code Wu–Xu z oryginalnych analiz (j22 i j62).
- Badacz 2026-11-21/data/summary_orig_083.csv Git blob **f7ea90eb3202933e9f52336315c1f36b3d40b019** — rzeczywiste kontrolne poziomy bazy autorów o22_base/o62_base w mianowniku f.

Surowe 58 punktów źródłowych CSV z kontrolą ID są identyczne z węzłami i Y w pochodnym analysis103.json. Wszystkie oryginalne 7/7 blob gates przeszły; nie użyto właścicielskiego posthoc f jako wejścia obliczeń. Własne wzory odtwarzają z dokładnością double właścicielskie Yref, Yz i f w 7-punktowym oknie dla obu mas i obu progów. Bramka G_BASE i puste predykcje z original analysis103.json osobno egzekwowane jako niezmienne.

## 2. Rozdzielone estymandy: frakcja tła to wybór referencji, nie uniwersalna stała

Oryginalna definicja Badacza:
  X(Y)=Y/(2+Y).
  f(j,t;x_ref) = [X(Y_z(j, beta_had(j,t)))−X(Y_ref)] /
                 [X(t)−X(Y_orig,083,base(j))].
Przy beta_had odczytanym z 090 PYBH code dla docelowego t=.251 lub .2484, Yz wyznaczono liniową interpolacją oryginalnych natywnych 103 węzłów, a dla zadanego zbioru referencji dopuszczono każdy pojedynczy oryginalny Y_ref na niskich wartościach beta (a nie tylko ich średnią). Mianownik pozostaje dokładnie właścicielskim mianownikiem. Nie dobierano nowego modelu fizycznego.

Testy naprzemienne:
- rdzeń OWNER window: 7 natywnych węzłów różnego beta od −20 do −18.5 (co .25).
- rozszerzone okno: 13 natywnych węzłów różnego beta od −20 do −17 (co .25); stopnie pośrednie co .25 od −19.5 do −17, wszystkie zapisane w wynikowym JSON.
- dla każdego zbioru obliczono właścicielski średni f, ale także ścisły arytmetyczny przedział między użyciem MIN i MAX oryginalnego Yref z tego zbioru; f jest monotoniczne w referencji, więc to dokładne ograniczenie WSZYSTKICH dozwolonych pojedynczych węzłów w tym konkretnym, jawnym skończonym zbiorze. Nie jest to matematyczny przedział wartości fizycznej z nieobserwowanego continuum, a tym bardziej przedział ufności.

Wyniki maksymalnego |f| spośród obu progów Yp i każdego rzeczywistego referencyjnego węzła:

| selekcja węzłów | j22 | j62 |
| --- | ---: | ---: |
| log10beta ≤−18.5, 7 węzłów | **0.01608289489633133** | **0.006895468369530106** |
| log10beta ≤−17.0, 13 węzłów | **0.01608289489633133** | **0.030329577655671205** |

Globalny max 7-node pool =1.6083%, max 13-node pool=3.0330%. Wynik NIE jest 95% CI: alternatywna, nieprzetestowana rzeczywista referencja może dawać co innego. Przyjęty w prereg warunek |f|<0.1 zostałby spełniony w tych dwóch jawnych rodzinach alternatyw POST HOC, ale PREREG103 ZOSTAJE GATE_FAIL i nie wolno uznać predykcji Pr2 za PASS. Stan jest tylko SOURCE_ROBUST_CONDITIONAL_REFERENCE_POOL, a nie FIZYCZNE ZATWIERDZENIE.

Wartości średnie w rozszerzonych oknach także pozostają niewielkie (szczegółowy 8-cutoff ×2-mass ×2-target JSON); ważniejszy jest arytmetycznie maksymalny skrajny wybór referencji. Najbardziej niekorzystny pojedynczy węzeł j62 to ok. −17.25, co nie jest odseparowaną, czysto bazową próbką.

## 3. Druga kontrola: odwracanie punktu przecięcia przy nieregularnej siatce

Dla oryginalnego j62 zestaw próg t=.2484 należy do sąsiedztwa węzłów (−15,−14.75), zaś próg .251 do (−14.75,−14.5). Niezależnie wykonano interpolację:
- liniową, dokładnie zgodną z właścicielem, wynik przy .2484 **−14.956075098079873**, przy .251 **−14.702405428618874**;
- PCHIP (własna implementacja Fritsch–Butland, shape preserving) na tych SAMYCH 29 natywnych punktach, odpowiednio **−14.946311198765152**, **−14.690896147150966**.
- Różnica PCHIP − linear odpowiednio **+0.009763899314721769 dex** i **+0.01150928146790875 dex**, wobec odstępu ~4.67–4.69 dex od właścicielskiego hadronowego progu. To jest tylko test geometrii interpolantu, nie zagwarantowana górna granica błędu prawdziwego modelu continuum między punktami co .25 dex.

Dla j22 w dwóch poziomach wszystkie 29 oryginalnych Y_z pozostają poniżej .2484 i .251, nie ma więc ani przecięcia liniowego, ani PCHIP w analizowanej próbce; **brak przecięcia w zakresie siatki**, nie logiczna niemożliwość poza nim.

## 4. Trzecia kontrola: siedem różnych beta nie jest siedmioma replikacjami solwera

Badacz w posthoc103.py wylicza SD(Yref) w 7 różnych niskich beta i nazywa względny wariant f_noise_1sd. Ten SD jest matematycznie poprawny jako ROZRZUT SIEDMIU RÓŻNYCH WARTOŚCI PARAMETRU beta. Nie mierzy on osobno stochastycznego ani deterministycznego błędu solvera PRZY IDENTYCZNYM fizycznym wejściu; w jego wartości mieszają się ewentualny niewielki dryft prawdziwego modelu z beta, nieliniowość, interpolacja i błąd numeryczny. Poprawna nazwa epistemiczna: DESCRIPTIVE_CROSS_BETA_LOW_NODE_SD, nie SOLVER_NOISE_1SIGMA.

Dodatkowe czysto opisowe zestandaryzowanie anomalii dwóch baz beta=1e−30 względem średniej i SD siedmiu pozostałych (różne beta!) daje:
  j22: +5.422697076852807 SD across beta nodes;
  j62: −71.05719778217986 SD across beta nodes.
To NIE są statystyczne z-score z i.i.d. próbek ani p-values i nie są miarą „71σ błędu solvera”. Dokładnie pokazują jednak, dlaczego jednopunktowa baza j62 nie może być bez kontroli podstawiona do obliczenia f. Niezmienny oryginalny status G_BASE FAIL.

## 5. Co rzeczywiście można orzec i czego nie

PASS source-only: 58/58 prawdziwych natywnych węzłów przepisanych z oryginalnych CSV; 4/4 owner-seven-reference values f odtworzone; wszystkie źródłowe SHA; dokładne maksymalne 7-node i 13-node pule referencyjne; 2 PCHIP kontra 2 linear porównania progów. Ten wąski niezależny test wspiera opisowy właścicielski kierunek: w faktycznie próbkowanych niskich beta i zadanej definicji frakcji f udział tła jest bliski zeru.

NO-GO: nie zmieniono statusu GATE_FAIL_NO_LABEL i NIE ocenia się prerejestrowanych Pr1/Pr2. Nie uzyskano fizycznego ograniczenia wpływu tła PBH, nie zweryfikowano krzywizny między punktami ani innych modeli Kohri/Keith; aktualny TYPE_TRANSFER_HOLD wciąż obowiązuje. Nie wykazano ilościowego udziału różnic Wu–Xu vs Kohri/Keith 0.5–2.2 dex, nawet jeśli w modelu Wu–Xu oryginalny sygnał hadronowy dominuje na badanych poziomach. „Szum” siedmiu różnych beta nie jest czystym sigma solwera. Właściwy prospektywny test wymaga wielopunktowego poziomu referencyjnego zamrożonego PRZED uruchomieniem skrajnych danych, oraz powtórzeń identycznego parametru, jeśli potrzebny jest estymator szumu.

## 6. Faktyczne wykonanie, reprodukcja, integralność i dispatch

Niezależny oryginalny Python3 stdlib:
research/mech-s10/2026-11-22/code/mech_s10_rot015_review104_reference_envelope_and_gate_preservation_referee.py
commit **ae3e7000f55423d9e5382071e3fce146893e0641**, original blob **c68ac5f3c8fe7844bffac3e9d7ff456df9745621**, readback source PASS.

Jedyny uruchomiony source-only GitHub Actions workflow:
commit **d4859abfe03e92f42b38a2f58b161a385a9a1f45**, run **45045654624**, job actual **COMPLETED SUCCESS**:
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/45045654624

Artefakt GHA: ID **14763611057**, rzeczywiście pobrany ZIP **5414 bytes**, SHA256 **fcacfb7bebdec76227e5b7067f753a8f500a5e7952b0e401e4364efba79fb2e8**, identyczny z provider digest, ZIP CRC PASS, SHA256 manifest original **5/5 PASS** (prefiks katalogu runnera rot015/ zachowany w manifest, ZIP spłaszcza nazwy). Źródłowy result JSON SHA256 **0034faf91ab0d79ff7b507c5ea68b54097c2568040144d2e6a4ba39f775e8008**. STDERR empty. Wszystkie 7 git hashes źródeł sprawdzone runtime before calculations.

Dane właściciela 61 oryginalnych przebiegów są odczytane tylko, nie były przez Mech powtarzane. Żadnych nowych Julia, PRyMordial, Herwig, PYTHIA, BlackHawk, mechanizmów fizycznych, żadnej migracji statusu.

FINAL:
ROT015_OWNER_REVIEW104_G_BASE_FAIL_PRESERVED /
7_OF_7_GIT_INPUT_SHA_PASS /
58_OF_58_NATIVE_BETA_DATA_NODES_PASS /
POSTHOC_4_OF_4_OWNER_SEVEN_NODE_F_REPLAY_EXACT /
ORIGINAL_REFERENCE_NODE_ENVELOPE_7_MAX_0P016083_13_MAX_0P030330 /
INTERPOLANT_LOCAL_SHIFT_0P0098_TO_0P0115_DEX /
DIFFERENT_BETA_NODE_SD_NOT_SOLVER_NOISE /
NO_TYPE_TRANSFER / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
