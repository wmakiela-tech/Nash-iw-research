---
artifact_id: IW_MECH_S10_ROT021_WUXU_ORIGINAL_LOGLOG_SUBGRID_EXTRAPOLATION_AND_BOUNDARY_CONDITION_NUMBER_SOURCE_REFEREE_001_20261122
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
status: ORIGINAL_AUTHOR_5_GIT_SHA_PASS / ORIGINAL_OWNER_5_GIT_SHA_PASS / SOURCE_ONLY_EXTRAPOLATION_IDENTIFIED_AND_216X_CONDITIONED
owner_firstness: BADACZ_090_099_109_ORIGINAL_PHYSICS / MECH_ROT020_FIRST_MASS_ENERGY_BUDGET
claim_ceiling: AUTHOR_PUBLIC_COMMIT_VERIFIED_BUT_OWNER_LOCAL_GIT_CHECKOUT_NOT_VERIFIED / NO_NATIVE_RESULTS_OF_109 / NO_HADRON_PHYSICAL_SUBGRID_CERTIFICATION / NO_BBN_Yp_OR_BETA_ROOT_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# Mech-S10 ROT021 — kod Wu–Xu w rzeczywistości ekstrapoluje hadronowe szybkości poniżej 10^9 g

## 1. Pytanie z ROT020 i stan własności

Mech ROT019 pierwszy rzeczywiście wczytał 100×100 oryginalnych danych widm pierwotnych BlackHawk, a ROT020 wyprowadził warunkowy energetyczny budżet całego malejącego PBH i wskazał brak tabulowanych węzłów dla M<10^9 g. ROT021 rozstrzyga węższe nowe pytanie: co faktycznie robi publiczny kod autorów Wu–Xu z pięcioma szybkościami hadronowymi poniżej pierwszego wiersza, jaka jest struktura ODE i jak czuły jest operator numeryczny na dwa pierwsze wiersze.

Najpóźniejsza odczytana oryginalna zmiana Badacza: PREREG109 DEV2 commit aebc6e1c6307b78ee7837071b40036ccbbbbc9e7. Brak opublikowanego owner REVIEW110 i analysis109.json w momencie sprawdzenia. Nie ma potwierdzonej akceptacji ROT020. Zmiana ta nie obejmuje nowego fizycznego Herwig/BlackHawk/PRyMordial/Wu–Xu runu. Prawdziwa własność tabel i historycznych wyników pozostaje po stronie Badacza i autorów Wu–Xu.

## 2. Pierwotne oryginalne źródła naprawdę otwarte i kontrolowane

W odrębnym jednorazowym GitHub Actions Python3 pobrał z oryginalnego publicznego commitu autora Wu–Xu:
https://github.com/Fenyutanchan/Primordial-Black-Hole/tree/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618

Pięć autentycznych plików autora, z dokładnym Git blob hash-object 5/5:
- tool_script-hadrons_from_PBH.jl: cc73432910f872d526113ce59b6204f38d0766a9;
- main-scan.jl: b368ba55d5a493f7bc185909730f7fe5691f10d6;
- data/out/hadrons_from_PBH.dat: 06d0883a27b108692720422294ba2baacd381a64;
- tool_script-parameters.jl: 0d7198ff3557bdbd5753000bb07a7a7405cc24f5;
- Project.toml: 6297eb1682da77bbbfa87307795b655c677f98c4.

Pięć właścicielskich kontroli z publicznego repo Nash-iw-research, też dokładne Git blob hash 5/5:
- original Badacz 099 Sa table: 3aac28554204e6b6951a7472773535ad3c8613ea;
- original Badacz rate_dump_081.jl wrapper: 4b415a6ddd7d102ad03194af75aa1fb9203c11fb;
- Mech-S6 apply_wuxu_charge_pair_source_map.py: 4d1f2be94510c576e4f48752911f88ede8b50474;
- original Badacz PREREG109: 4cb85ea4b112780d588884361c4d076952d58dfa;
- original Badacz run109_dev2.sh: 38c2b8ba2d21826893eff5198adb6353a6eb5a57.

Prawdziwy oryginalny author hadrons_from_PBH.dat ma SHA256 25411c26cb24b08058be6dffe01e3c6cc668c91de963438a91c4aac0a38199df, dokładnie ten sam, który Badacz kontroluje w oryginalnym run109_dev2.sh. Zatem oryginalny plik tablicy author-to-owner ma niezależnie sprawdzoną zgodność bajtową. Ograniczenie: nie mieliśmy dostępu do katalogu właściciela /home/claude/fenyutanchan/primordial-black-hole i nie zweryfikowaliśmy SHA jego lokalnej kopii main-scan.jl oraz tool_script-hadrons_from_PBH.jl. Nie wolno twierdzić, że lokalne source 109 z całą pewnością jest identyczne z publicznym commitem bez dodatkowej kontroli, chociaż wrapper faktycznie ładuje tę klasę plików.

Pakiet zawiera pełne oryginalne bajty pięciu plików autora, nie tylko ich streszczenia, oraz przeliczone źródłowe JSON.

## 3. Jawny kod numeryczny zamyka pytanie o operator poniżej siatki

Autentyczny tool_script-hadrons_from_PBH.jl wczytuje plik 100×5 hadronów i konstruuje osobno pięć:
  LinearInterpolation(log.(rate_h), log.(mass); extrapolation=ExtrapolationType.Linear, cache_parameters=true).
Funkcje dN_over_dt_pi/K/K0L/proton/neutron zwracają exp z interpolatora dla log(m_PBH). Używany jest DataInterpolations.jl, zgodnie z oryginalnym Project.toml. Wynika z tego dla M<M0 (M0=10^9 g) dokładny operator z dwóch pierwszych dodatnich wierszy:
  R_h(M) = R_h(M0) × (M/M0)^{a_h},
  a_h = ln[R_h(M1)/R_h(M0)] / ln(M1/M0),
  M1=1.0873877705847254×10^9 g.

W opublikowanym main-scan.jl ten plik jest bezpośrednio include; w evolution_system! źródła do gęstości hadronów mają formę R_h(m_PBH)×n_PBH, przy EWOLUUJĄCEJ masie, bez kontroli dolnej tabularnej granicy M0. Nie ma w tych pięciu funkcjach clamp/rate=0 przy M<M0. To jest rzeczywista EKSTRAPOLACJA potęgowa poza tablicę, nie koniec źródła.

Autor ma OSOBNĄ bramkę wyparowania: PBH_evaporated_flag po osiągnięciu progu m_stop, co zeruje n_PBH. Magic domyślnie używa log_m_PBH_evaporated_ratio=20, próg równy max(M_init×exp(-20), m_Planck). Badacz rate_dump_081.jl woła magic(m,beta; hadrons_output_flag=true) bez override progu. Mech-S6 patch zmienia cztery pierwotne przypisania agregatów hadronowych przez mnożenie 0.5 i pozostawia K0L, bez zmiany pięciu interpolatorów. To potwierdzono ze źródłami, nie z symulacji.

Dla j22 M_init=6.316227669701322e9g, warunkowy stop to 13.01871554155 g; dla j62 M_init=1.8023351397102734e11g, 371.4889602062g. To bardzo małe masy względem 10^9g: 7.88543 i 6.43005 dekad poza tablicą. Słowo WARUNKOWY jest kluczowe: nie wykonano integracji, więc nie stwierdzono, że natywne M(t) faktycznie osiąga Mstop w oknie interesującym BBN. Źródłowo wiadomo, co kod przewiduje jeżeli je osiągnie.

## 4. Prawdziwe nachylenia z dwóch ISTNIEJĄCYCH tablic

Niezależnie odczytano oryginalną tablicę autora Wu–Xu oraz oryginalną tablicę Badacza 099 Sa; obie mają te same pierwsze dwie masy M0/M1, ale różne pięć szybkości. Wszystkie są dodatnie.

| Hadron | wykładnik a_h autor Wu–Xu | wykładnik a_h właściciel Sa |
| --- | ---: | ---: |
| piony naładowane | -1.20048562561 | -1.10550920942 |
| kaony naładowane | -1.19665135050 | -1.08880849556 |
| K0L | -1.19680484135 | -1.08988589320 |
| protony | -1.20429142854 | -1.09919598492 |
| neutrony | -1.20476306398 | -1.10071724853 |

Dla dwóch REALNYCH tablic stosunek ekstrapolowanych funkcji R_Sa/R_author też został obliczony bez solvera:

| Gatunek | M=10^9g faktyczny wiersz | M=13.0187g ekstrap j22, WARUNKOWY | M=371.489g ekstrap j62, WARUNKOWY |
| --- | ---: | ---: | ---: |
| pi± | 0.695875 | 0.124051 | 0.170541 |
| K± | 0.465157 | 0.065647 | 0.094225 |
| K0L | 0.457606 | 0.065673 | 0.093972 |
| proton | 0.497291 | 0.073771 | 0.104916 |
| neutron | 0.486351 | 0.073537 | 0.104215 |

To nie jest nowe Sc 109, które jeszcze nie zostało opublikowane. Różnice przedłużenia źródła pomiędzy dwiema rzeczywistymi, ALE RÓŻNYMI fizycznymi tablicami mogą zmieniać się silnie poza siatką; nie jest to dowód jakiegokolwiek rzeczywistego błędu solvera.

W Sa na warunkowym progu j22 źródłowe same rate R_h wzrastają od wartości w M0 o 3.85–5.22×10^8, a na j62 o 1.00–1.28×10^7. To NIE jest integralna liczba hadronów na PBH: przy M(t) maleje czas ewolucji, działa czynnik n_PBH oraz sieć rozpadów i reakcji jądrowych. Nie wolno przenosić wzrostu natężenia do wzrostu helium.

## 5. Ścisłe uwarunkowanie małej zmiany pierwszych dwóch wierszy

Dla każdej pary dodatnich tablic A/B z jednakową siatką M0/M1:
  lambda(M) = ln(M/M0)/ln(M1/M0);
  ln[R_B(M)/R_A(M)] =
      [1-lambda(M)] ln[R_B(M0)/R_A(M0)]
      +lambda(M) ln[R_B(M1)/R_A(M1)].
To dokładna tożsamość algebraiczna powyższego operatora log-linear, nie statystyczna przybliżona propagacja błędów.

Na WARUNKOWYCH progach wyparowania:
  lambda(j22)= -216.72536166490113,
  lambda(j62)= -176.72536166490113.
Lokalne uwarunkowanie logarytmu ekstrapolowanego rate na logarytm jednej brzegowej wartości wynosi więc około 217 i 177.

SYNTHETYCZNY świadek: zwiększ wyłącznie drugi, nie pierwszy wiersz R(M1) o +0.1%. Pod tą operacją przy zmienionym operatorze końcowe ekstrapolowane R_B/R_A = 0.80523826 (j22; minus 19.48%) i 0.83808391 (j62; minus 16.19%). Przy zwiększeniu wyłącznie R(M0) o +0.1% odpowiednie R_B/R_A = 1.24311033 i 1.19439115. To konstrukcyjne badanie uwarunkowania, NIE źródłowo wykryta zmiana 0.1% w Sc, nie fizyczne σ, nie wynik Yp i nie granica na beta.

Właścicielska Sc nie została jeszcze do tych obliczeń dostarczona. Jeśli istnieje choć niewielka różnica nachylenia dwóch pierwszych rzeczywistych wierszy nowej Sc względem Sa, operator może ją silnie amplifikować poza siatką — o ile fizyczna ścieżka PBH dochodzi do tak małych mas i wpływa na sieć BBN. Siła w efekcie końcowym pozostaje niepoznana.

## 6. Uściślenie ROT020 i rekomendacja falsyfikacyjna

Rozstrzygnięte: brak tablicy M<10^9 g to NIE brak zdefiniowania numerycznego źródła autorów. Publiczny kod Wu–Xu definiuje ekstrapolację log-log LINEAR, aktywną do osobnego progu masy wyparowania. Nie jest to jednak kalibracja fizyczna w nieobserwowanym reżimie.

Nie rozstrzygnięte: czy lokalna źródłowa kopia kodu Badacza ma identyczne SHA jak obecny publiczny commit; czy M(t) w natywnym oknie j22/j62 osiąga bardzo małe masy; jak realna tabela Sc zmienia dwa wiersze; jaka jest kondycja przekształcenia tych pięciu szybkości w BBN Yp i następnie root beta.

Ważna niezamienność: H_M z ROT020 dotyczy interpolacji udziału energii pierwotnego top q(M) w ORYGINALNYCH 14 kanałach BlackHawk, natomiast obecny main-scan interpoluje/ekstrapoluje pięć końcowych HADRONOWYCH źródeł z gotowej tablicy. Sam dowód jednej metody nie daje dowodu H_M dla innego estymandu.

Najwęższy dalszy test owner bez nowych solvers: porównać realne pierwsze dwa wiersze Sa i kiedy już istnieje Sc; obliczyć dokładne lambda i różnice ekstrapolowanych source rates w masach, które mają udokumentowany zasięg w oryginalnych M(t), a nie w hipotetycznym końcu. Jeśli brak źródłowych mas, owner powinien dodać w odrębnej prerejestracji diagnostykę M(t) i gotowych hadronic rates; bez automatycznego zamykania fizycznego label ambiguity.

## 7. Rzeczywista reprodukcja i custody

Publiczny oryginalny niezależny Python3 stdlib:
 research/mech-s10/2026-11-22/code/mech_s10_rot021_wuxu_original_loglog_subgrid_extrapolation_condition_number.py
 Git commit **23664dda35063f382e001971fe279b4960c40b6b**, Git blob **3ee920a8b8fcce1ac17aa158086302543471996b**.

Jednorazowy faktyczny GHA:
 https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/45068362455
 workflow commit **22c0dc2a836a1a88eedb9b639e5a86caa53860fd**,
 job COMPLETED SUCCESS.
Pięć źródeł autora pobranych po przypiętym Git commit i 5/5 zweryfikowanych blob SHA; pięć źródeł owner 5/5 SHA, literalna kontrola owner wrapper i source patch, algebra 5×2 tabel i symbolicznego perturbacyjnego 0.1%.

Faktycznie pobrany oryginalny artifact ID **14771999016**, ZIP **18205 B**, SHA256 **87c4235409cd32d188370c7194cb09667473f1b362f66b18eb6ff4cca9a009d4**, weryfikacja niezależnym sha256 BITY IDENTYCZNE z provider; CRC PASS; manifest dziesięciu oryginalnych plików 10/10 SHA256 PASS, stderr pusty. JSON zawiera pełną strukturę wyniku i dane obu tablic, a ZIP autentyczne oryginalne pliki autora z pinned commit.

FINAL:
ROT021_OFFICIAL_ORIGINAL_AUTHOR_5_SHA_PASS /
OWNER_5_SHA_PASS /
AUTHOR_HADRONIC_RATE_LOGLOG_LINEAR_EXTRAP_CONFIRM /
EXACT_BOUNDARY_2_POINT_CONDITION_NUMBER_216P725_AND_176P725 /
ACTUAL_TWO_PREEXISTING_TABLES_RATE_CONTRAST_PASS /
NO_LOCAL_OWNER_CODE_SHA /
NO_SC_109_NATIVE_RESULTS /
NO_PHYSICS_RERUN / NO_Yp_BETA_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
