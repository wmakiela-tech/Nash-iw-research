---
artifact_id: IW_MECH_S10_ROT019_ORIGINAL_BH_10000_NODE_TOP_TAIL_ENERGY_CONSERVATION_BOUNDED_SOURCE_IMPACT_AND_MASS_EVOLUTION_GUARD_001_20261122
date: 2026-11-22 Europe/Warsaw
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10
exposure: PUBLIC
status: ORIGINAL_100x100_RAW_GZIP_INDEPENDENTLY_READ / EXACT_SEVEN_GIT_INPUT_BLOB_SHA_PASS / CONDITIONALLY_RIGOROUS_DISCRETE_HADRON_SOURCE_BOUND
firstness: BADACZ_090_SOURCE_PRIMARY_AND_099_Sa_AND_109_DEV2_OWNER / MECH_ROT018_FOUR_SOURCE_GRID_NODES_FIRST / MECH_ROT019_FIRST_SOURCE_ONLY_MASS_RESOLVED_CONSERVATIVE_TOP_FLUX_BOUND
claim_ceiling: ORIGINAL_100_GRID_TRAPEZOID_ONLY / ENERGY_CONSERVATION_ASSUMPTION / NOT_TIME_INTEGRATED / NO_BETA_ROOT_BOUND / NO_PBH_LIMIT / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# Mech-S10 ROT019 — faktyczny odczyt 10 000 węzłów BlackHawk: warunkowa ścisła granica wpływu brakującego top na źródło hadronowe

## 1. Motywacja, firstness i aktualność

Badacz pierwszy zamroził PREREG109 i jawnie zapisał DEV-1 (natywny Herwig7.1.5 top sqrt(s)=200000 GeV zawiesił się z seed9709) i DEV-2 (top po ponowieniu seed9710 nie powiódł się przez RhoDMatrix); zob. oryginalny commit DEV2 aebc6e1c6307b78ee7837071b40036ccbbbbc9e7 z 22 XI 2026 19:07:58 CET. Oryginalne 10 kanałów MC×3 energie zostało ograniczone w code/analysis_109.py i builderze przez pominięcie top przy Eprimary=100000 GeV; reszta top przy E>70710.678 GeV korzysta z klipu n_top(E_last). Mech ROT018 pierwszy audytował dokładny zakres G_MC 29-of-30 i 4 węzły deklarowanej siatki, wskazując NIEWIADOMĄ wielkość wpływu top na fizyczne progi.

Celem NOWEGO obrotu jest przekroczenie ograniczenia ROT018 „brak odczytu Phi_top”: tutaj niezależny audytor **rzeczywiście rozpakował i odczytał pełne źródłowe 100×100 BlackHawk widmo pierwotne**, oryginalne 100-wierszowe Sa, dopasował dokładne masy do j=0…99 i obliczył ścisłą zachowawczą granicę ORYGINALNEGO, dyskretnego operatora całkowania po energii dla BRAKUJĄCEGO KANAŁU TOP powyżej 70710.678 GeV. Nie wykonano żadnego nowego generowania Herwig, BlackHawk, Julia, PRyMordial, PYTHIA ani alternatywnej fizyki.

Ostatni sprawdzony stan właścicielski pozostaje PREREG109 DEV2 bez opublikowanego natywnego REVIEW110/analysis109.json; nie wymyśla się etykiet Pr1–Pr3. Korekta ROT017 REVIEW106 0.009689dex=2.256% (nie ≤1% obserwowanych komórek) nadal oczekuje owner ACK, ale nie jest przedmiotem nowego eksperymentu.

## 2. Oryginalna baza i pełna kontrola 7 SHA

Niezależny Python3 stdlib, uruchomiony rzeczywiście w czystym GitHub Actions, otworzył ORYGINALNY skompresowany blob zamiast pochodnego materiału:

1. research/badacz/2026-11-21/data/primary_spectra_090.tsv.gz — Git blob **e2079be0b6dfab12a743c09e6937f1d2383d3a57**, fizycznie rozpakowane **10000** wierszy (100 mas×100 energii), zawierające dodatnie/zerowe Phi_top(E,M) i oryginalne 14 kanałów;
2. research/badacz/2026-11-22/data/hadrons_099_Sa.dat — Git blob **3aac28554204e6b6951a7472773535ad3c8613ea**, 100 mas×5 dodatnich oryginalnych źródłowych wydajności hadronów;
3. research/badacz/2026-11-21/code/fold_090.py — blob **3392d1d088a4bdae869ecdc70bcd2081861ecf37** (oryginalny trapez w energii, n per primary, HBAR);
4. research/badacz/2026-11-22/code/build_tables_109.py — blob **fd231901b01602909974f77cdffd2af5053f8de6** (Sc, top high clip, 1/BIN_HW);
5. research/badacz/2026-11-22/code/analysis_109.py — blob **c84d3a32603d96f08c4be4c3e8198772c9bf2e92** (DEV2 top/E100000 exclusion);
6. research/badacz/2026-11-22/code/run109_dev2.sh — blob **38c2b8ba2d21826893eff5198adb6353a6eb5a57** (jawna oryginalna zmiana workflow);
7. Badacz oryginalny PREREG109 markdown — blob **4cb85ea4b112780d588884361c4d076952d58dfa**.

SHA każdego zweryfikowano fail-closed przed parsowaniem. Oryginalne 100 mas źródłowych zgadzają się z masami oryginalnej Sa w jednostkach author m_PBH [GeV], użyto oryginalnego przelicznika 5.609588603804452e23 GeV/g, zaś Sa w jednostkach [GeV] przeliczono na liczbę hadronów na sekundę przez oryginalną HBAR=6.582119569e−25 GeV s. W oryginalnym gzip nagłówek fizyczny „W+-” trzeba mapować zgodnie z oryginalnym fold_090.PCOL wewnętrznie na „Wpm”. Pierwsze uruchomienie ROT019 zakończyło się fail-closed na tej rozbieżności nazwy (FAILED run45056004076, bez raportowania liczb); parser poprawiono mechanicznie jako DEV-1 bez zmiany estymandu, commit6afd075a7e16a67531bf2a993ba3ec217e898247. Drugie, finalne uruchomienie 45056115560 źródła rzeczywiście odczytało i zaliczyło; nie ukryto poprzedniej awarii.

## 3. Niezależne wyprowadzenie zachowawczej GRANICY, a nie oszacowania

Oryginalny generator HERWIG jest wywoływany dla pary przy sqrt(s)=2Eprimary. Krotność na JEDEN kwark pierwotny jest połową krotności hadronów wygenerowanych w całym zdarzeniu e+e−; oryginalny fold_090.PAIR_MC daje 0.5 dla top. Z zachowania energii i dodatniej masy gatunku hadronowego m_h wynika przy idealnie zachowującej energię próbce:
  0 ≤ n_top→h(E) ≤ E/m_h.
Przyjmujemy umyślnie zaniżoną i wspólną wszystkim pięciu gatunkom masę M0=0.1GeV; π±, K±, KL0, proton i neutron są cięższe od 0.1 GeV. Zatem KAŻDA przyszła dodatnia krotność n_true(E) i każda klipowana historyczna wartość n_clip(E)=n(E_last), przy E≥E_last, mieszczą się w [0,E/M0]. Ich RÓŻNICA ma:
  |n_true−n_clip| ≤ E/M0,
niekoniecznie 2E/M0, bo obie wartości leżą w tym samym przedziale.

Właścicielski source-only dyskretny operator hadronowy dla brakującego top:
  S_h(M) = (1/BIN_HW) Σ_trapez_E Phi_top(E,M) n_top→h(E) ,
gdzie BIN_HW=(exp(ln(1e11)/99)−1)/(ln(1e11)/99)=1.1395656964503507.
Przez monotoniczność kwadratury trapezów przy Phi_top≥0 (wykryte i sprawdzone dla pełnych 10000 wartości) dostajemy **ściśle dla tego DISKRETNEGO modelu**:
  |S_h,true(M)−S_h,clip(M)|
   ≤ [1/(M0 BIN_HW)] Σ_trapez_E [Phi_top(E,M) E 1_(E>E_last)] .
Wynik dzielimy przez O R Y G I N A L N E Sa_h(M)/HBAR, otrzymując bezwymiarową górną granicę WZGLĘDNEJ ZMIANY źródła hadronowego w tablicy, dla każdego gatunku i każdej masy. Nie jest to błąd faktyczny, wartość oczekiwana, CI, rzeczywisty artefakt MC ani granica na log10beta/Yp. Wymaga zachowania energii na poziomie zdarzeń i oryginalnej dyskretnej siatki.

Brakujące cztery węzły źródłowej energii są indeksami 96,97,98,99, E>70710.678 GeV; cały oryginalny plik 100×100 odczytano. Dla części mas dodatni bardzo wysoki ogon wynika z surowych widm, dla większych jest dokładnie zerowy w zapisie float (podcięcie/underflow, nie teoretyczne zero w continuum).

## 4. Rzeczywiste wyniki według masy, bez dorabiania efektu fizycznego

Największa dopuszczalna różnica źródła względem oryginalnej Sa spośród pięciu gatunków:

| index j | oryginalna masa PBH [g] | Max_h |Delta S_h|/Sa_h |
| ---: | ---: | ---: |
| 0 | 1.0000000e9 | **2803.388526357862** (bardzo luźny bound) |
| 8 | 1.9546795e9 | 19.9252 |
| 10 | 2.3112368e9 | 2.699458378677222 |
| 12 | 2.7328345e9 | 0.21659723995466068 |
| 14 | 3.2313368e9 | 0.010731717505697435 |
| 15 | 3.5137161e9 | 0.0019068746248365478 |
| 16 | 3.8207719e9 | 0.00029610012119849226 |
| 18 | 4.5177272e9 | 0.000003529447821554388 |
| 22 | 6.3162277e9 | **4.040894307909193e−11** |
| 62 | 1.8023351e11 | **0** (w ORYGINALNEJ dyskretnej siatce) |

W j22: oryginalny surowy całkowy strumień energii top dla E>70710.678 = 9.848338354883738e15 (jednostka źródłowa), podczas gdy całkowity strumień energii wszystkich kanałów na tej masie 1.0684566037726548e31; udział = **9.217349885910068e−16**. W obrębie samego top jest to **7.444604775863932e−15** całego źródłowego strumienia energii top. Na j22 bardzo wysokoenergetyczny top jest rzeczywiście skrajnie stłumiony w ORYGINALNYM widmie. Najgorszy względny hadronowy bound z m0=0.1 wynosi 4.04e−11 (K0L); piony 1.6736874659544137e−12, kaony± 1.951811083617029e−11, protony 3.2134883384208125e−11, neutrony 3.312497538464601e−11. Jest to maksymalna różnica W TABELI źródła na wierszu j22, nie dla całej ewolucji PBH j22.

W j62: w czterech oryginalnych punktach Phi_top(E>70710.678)=0 w zapisie źródłowym, więc górna granica DYSKRETNA jest równa 0. Nie wolno uogólniać na kontinuum ani mówić, że emisja top z PBH j62 jest fizycznie niemożliwa.

W j0: oryginalny top high-energy tail obejmuje **12.565066182842785%** całej energii emitowanej w kanale top oraz **1.5607054684713455%** całej energii pierwotnych kanałów na tej masie; przełożenie przez skrajnie luźną masę minimalną 0.1GeV daje dla K0L limit aż 2803.3885-krotności Sa. To NIE znaczy, że fizyczny błąd ma taką wielkość; oznacza jedynie brak użytecznej małomasowej certyfikacji tą konserwatywną nierównością.

Przy monotoniczności obliczonej (źródłowo sprawdzonej tabeli 100 mas): dla wszystkich mas z INDEKSEM j≥15 (M≥3.5137161e9g) maksymalny bound jest <0.002, a dla j≥16 (M≥3.8207719e9g) <0.0003, przy natywnych węzłach źródłowej masy. Dla j≤10 limity mogą przekraczać 100% i stają się nieinformatywne. Jest to PRZEJŚCIE MIĘDZY MASAMI ŹRÓDŁOWYMI, nie próg istotności dla całego procesu BBN.

## 5. Krytyczna granica: PBH wyparowuje i M(t) przechodzi przez inne wiersze

**Nie wolno przenieść 4.04e−11 dla wyjściowej masy PBH j22 albo 0 dla j62 na całe natywne rozwiązanie Wu–Xu.** Badane modele obejmują zmianę masy czarnej dziury przez promieniowanie Hawkinga i ewaporację. Początkowa masa j22/j62 jest jedynie jednym punktem M(t); w późnym przebiegu M może znacznie się zmniejszyć. Gdy M(t) dociera do ok.1e9–3e9g, surowe widmo top high-energy przestaje być bezwzględnie zaniedbywalne, a powyższy prosty bound bez dodatkowego rozkładu czasu M(t), modyfikacji dynamiki i propagacji źródła przez sieć jądrową może być bardzo szeroki.

To jest zasadnicze kryterium NIEIDENTYFIKOWALNOŚCI wpływu na d_label_c w PREREG109 z samych wierszy Sa i surowych Phi. Znak i rozmiar wpływu na progową beta pozostają UNKNOWN. Wartość mniejsza niż 0.03dex root-jitter albo mała frakcja w późnym czasie nie wynika automatycznie z ograniczenia hadronowego na wyjściowej masie.

Sugerowany JEDYNY dalszy kierunek właścicielski: w oddzielnie zarejestrowanej analizie source-only zbadać rzeczywiste M(t) (jeżeli zachowane oryginalne trajektorie) i wagę czasową przedziału M<3.5e9g podczas integracji BBN; następnie zastosować ten sam deterministyczny source energy bound do time-integrated source. Dopiero po kontroli kondycjonowania Yp względem hadronic source można mówić o zmianie beta root. Mech nie wykonywał żadnego z tych nowo wymagających natywnych obliczeń.

## 6. Wykonanie, uczciwa korekta parsera i custody

Źródłowy Python3 stdlib:
research/mech-s10/2026-11-22/code/mech_s10_rot019_actual_blackhawk_primary_top_tail_energy_conservation_sharp_discrete_bound.py,
finalny Git commit **6afd075a7e16a67531bf2a993ba3ec217e898247**, Git blob **5d12bfe84eb95a5fdd2f91011e2211a284c178ea**.

Pierwsza nieudana kontrola:
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/45056004076
FAIL z powodu autentycznego source gzip header W+- (zamiast skrótu wewnętrznego Wpm); poprawka DEV-1 wyłącznie mapuje nazwę zgodnie z prawdziwym fold_090.PCOL. Nie wywiedziono żadnych liczb z tego nieudanego runu.

Finalny jeden poprawny GitHub Actions source-only:
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/45056115560
workflow commit **2244b99461ebdf4b01fc53ceb53e65f06794e820**, COMPLETED **SUCCESS**. Oryginalny run zip artifact **14767905020** rzeczywiście pobrany i niezależnie skontrolowany:
ZIP **16722 bajtów**, SHA256 **24d4c4bd3fefbb8e12280f87ec372e2df134cc9e54268013b7046eeb5968183b**, identyczny z dostawcą; ZIP CRC PASS; oryginalny SHA256_MANIFEST **5/5 PASS**, STDERR pusty. Oryginalny wynik JSON zawierający **100 mas×5 gatunków**, 10 000 węzłów, siedem exact SHA oryginalnych źródeł, strumienie i granice mas, **93800 bajtów** SHA256 **89006bfda0c6e8329827461060a2609bc59d02e97c6525352c645a9a267cf1e4**. Odczyt JSON, kontrolę ZIP i wewnętrzne 5 SHA faktycznie wykonano. Właściwy status:
SOURCE_PASS_RAW_ORIGINAL_10000_NODES /
CONSERVATIVE_DISCRETE_TOP_TAIL_BOUND_J22_4P04E_MINUS11_J62_ZERO_STORED /
LOW_MASS_SOURCE_UPPER_BOUND_NONINFORMATIVE /
EVOLVING_PBH_MASS_BLOCKS_BETA_ROOT_TRANSFER /
NO_NATIVE_PHYSICS / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
