---
artifact_id: IW_MECH_S10_ROT020_ORIGINAL_10000_NODE_PBH_MASS_PATH_MISSING_TOP_ENERGY_BUDGET_CONDITIONAL_INTERPOLATION_ENVELOPE_AND_SUBGRID_NO_GO_001_20261122
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
class: ORIGINAL_RAW_100x100_BLACKHAWK_SOURCE_ONLY_MASS_BUDGET_REFEREE
status: SOURCE_7_EXACT_GIT_BLOBS_PASS / MASS_INTERPOLATION_CONDITIONAL_ENERGY_BUDGET / UNKNOWN_BELOW_1E9g_DOMINATES
owner_firstness: BADACZ_ORIGINAL_090_BLACKHAWK_PRIMARY_AND_099_Sa / BADACZ_109_DEV2_EXPLICIT / MECH_ROT019_SOURCE_BOUND_FIRST
claim_ceiling: NO_UNCONDITIONAL_SUBPERCENT_FULL_EVAPORATION / NO_BBN_TIME_WEIGHTING / NO_TRUE_HELIUM_Yp_OR_BETA_ROOT_BOUND / NO_NEW_NATIVE_PHYSICS / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# Mech-S10 ROT020: budżet niezmierzonego kanału top podczas całej zmiany masy PBH — conditional 0.5574% j62, 15.9055% j22, bez twierdzenia o Yp

## 1. Aktualność, przedmiot i firstness

Na początku ROT020 zweryfikowano oryginalne repo Badacza: najnowszy commit badawczy Badacza to **aebc6e1c6307b78ee7837071b40036ccbbbbc9e7** (PREREG109 DEV2, 22 XI 2026 godz. 19:07:58 CET); oryginalnego REVIEW110 lub opublikowanego analysis109.json nie znaleziono. Nie było też potwierdzonego owner ACK dla Mech ROT019. Wszystkie nowe wyniki Badacza, jeśli ukażą się po zamrożeniu niniejszego audytu, wymagają oddzielnej rewizji; nie przypisujemy temu obrotowi dostępu do nieistniejących danych.

Przypomnienie faktów właścicielskich: Badacz pierwszy zamroził PREREG109 i jawnie opublikował DEV1/DEV2 przy niepowodzeniu Herwig 7.1.5 top Eprim100000 GeV (sqrt(s)=2e5 GeV; seed9709 hang, seed9710 RhoDMatrix). DEV2 wyklucza tę energię z oryginalnej bramki G_MC i przedłuża ostatnią dobrą krotność top z Eprim70710.678 GeV jako płaski clip. Mech ROT018 pierwszy formalnie wykazał, że G_MC może przejść mimo brakującej jednej z 30 planowanych komórek. Mech ROT019 pierwszy rzeczywiście odczytał 100×100 oryginalnych surowych widm BlackHawk i wyprowadził ścisłą warunkową górną granicę udziału TOP TAIL w dyskretnym źródle hadronowym dla KAŻDEJ stałej masy; w j22 maksymalny bound na pojedynczy gatunek hadronu w pierwotnym wierszu jest 4.04e-11, j62 stored zero. ROT019 wyraźnie zabronił przenoszenia tego wyniku z początkowego M_init na całe M(t).

ROT020 podejmuje inne pytanie: ile energii całego przebiegu możliwie pochodzi z NIEZMIERZONEGO odcinka top Eprim>70710.678 przy malejącej masie PBH, gdy znamy historyczny spektralny surowy zakres M=1e9…4e12 g, ale nie mamy danych dla M<1e9g? Jest to audyt **energetyczny** i **warunkowy**, nie nowe obliczenie natywnego BBN. Dwie niewiadome są jawnie oddzielone: (I) pomiędzy 100 węzłami masy konieczne założenie regularności interpolacji; (II) poniżej dolnej masy widma nie mamy ŻADNYCH węzłów, więc stosujemy wyłącznie bilans pozostałej energii spoczynkowej.

## 2. Dokładne pierwotne wejście, bez pliku wynikowego z ROT019 jako materiału danych

Nie odczytywano wyłącznie zarchiwizowanego JSON ROT019: nowy niezależny skrypt ROT020 **ponownie rozpakował i przeliczył oryginalny** research/badacz/2026-11-21/data/primary_spectra_090.tsv.gz (Git blob e2079be0b6dfab12a743c09e6937f1d2383d3a57), 10000 pierwotnych węzłów źródłowych, masy m_g i 14 nieujemnych kanałów widma. Ponownie odczytano research/badacz/2026-11-22/data/hadrons_099_Sa.dat (blob 3aac28554204e6b6951a7472773535ad3c8613ea) oraz zweryfikowano dokładność dopasowania wszystkich 100 źródłowych mas. Nazwa oryginalnej kolumny W+- mapowana na wewnętrzny Wpm zgodnie z oryginalnym code/fold_090.py (blob 3392d1d088a4bdae869ecdc70bcd2081861ecf37).

Dodatkowe oryginalne SHA, faktycznie gated:
- owner builder109 code/build_tables_109.py blob fd231901b01602909974f77cdffd2af5053f8de6;
- owner DEV2 code/analysis_109.py blob c84d3a32603d96f08c4be4c3e8198772c9bf2e92;
- owner run109_dev2.sh blob 38c2b8ba2d21826893eff5198adb6353a6eb5a57;
- oryginalny PREREG109 blob 4cb85ea4b112780d588884361c4d076952d58dfa.

Kod ROT020 używa oryginalnej funkcji parsera źródeł ROT019 **z zamrożonego blob 5d12bfe84eb95a5fdd2f91011e2211a284c178ea**, sprawdzając SHA tego kodu i wewnętrzne 7 SHA pierwotnych źródeł fail-closed przed przetwarzaniem. Rzeczywisty ZIP GHA pokazuje 10000 faktycznie rozpakowanych węzłów przy każdorazowym ponownym wykonaniu. Nie ma kopii z wynikowego JSON ROT019 użytej jako dane wejściowe.

## 3. Nowy estymand: udział energii potencjalnie związanej z top w budżecie MASOWYM PBH, a nie hadronic count/Yp

Dla źródłowej masy M_i obliczono bezpośrednio z 100 energii:
  N_i = trapezoid_E { E·Phi_top(E,M_i)·1_(E>70710.678GeV) };
  D_i = trapezoid_E { E·Σ_(c∈14 oryginalnych kanałów) Phi_c(E,M_i) };
  q_i = N_i/D_i.

Dodatnie surowe Phi_c, brak podwójnego liczenia 14 kanałów, poprawne energy-flux units są założeniami fizycznej interpretacji. Ponieważ all-channel denominator D_i jest dodatnią CZĘŚCIĄ całkowitego promieniowania PBH, udział niezmierzonego TOP-Ehigh w pełnym bilansie masy nie jest większy niż q_i, **o ile** pominięte kanały promieniowania wnoszą tylko dodatknią energię i żaden z 14 kanałów nie jest liczony wielokrotnie. To źródłowa miara q_14, nie energia zrzucana do BBN po hadronizacji. q_i nie jest krotnością hadronów ani zmianą Sa_h.

Dla PBH wyłącznie wyparowującego, bez akrecji, utrata masy dM przekłada się przez bilans spoczynkowy na wypromieniowaną energię dE=−c²dM. Zatem, jeśli q(M) jest poprawnym ograniczeniem udziału brakującego kanału w całkowitej chwilowej mocy, energia tego kanału w całym przebiegu od M_init do końca ma ograniczenie:
  E_top_missing/(M_init c²) ≤ (1/M_init)∫_0^M_init q(M)dM.
Gdy PBH przestaje wyparowywać przed osiągnięciem M=0, dodatniość pozwala nadal użyć formalnego całego przedziału jako (konserwatywnego) ograniczenia; nie znaczy to, że cały przedział został faktycznie fizycznie zrealizowany w oknie BBN.

Oryginalny zakres danych to M∈[M_min,4e12 g], gdzie **M_min=1.0e9g**. Poniżej M_min żadnych rzeczywistych źródłowych węzłów NIE MA. Można bez innych danych założyć wyłącznie 0≤q≤1, co daje:
  (1/M_init)∫_0^M_min q(M)dM ≤ M_min/M_init.
Jest to BEZWARUNKOWY wobec nieznanej szczegółowej krotności top budżet energii **tego niezarejestrowanego przedziału masy** (warunek Hawking-only mass loss pozostaje). Nie jest to dolne ograniczenie rzeczywistego top i nie dowodzi dodatniego wkładu. Dla j22 wynosi 0.15832234876474735, dla j62 0.005548357672040676.

**Niebezpieczne przejście przez przedziały 100 mas:** 100 zaobserwowanych q_i stanowi tylko dyskretne próbki; nie ma matematycznego dowodu, że q(M) pomiędzy sąsiednimi masami nie wzrasta dowolnie blisko 1. Bez dodatkowego H_M z surowego źródła jedyny uniwersalny bound na CAŁY przedział 0..M_init to banalne 100% początkowej energii, NIE poniższe dokładne wartości. To jest główna granica epistemiczna.

## 4. Jawny i falsyfikowalny warunek H_M: kontrola obwiedni po masie

Wprowadza się założenie oznaczone H_M:
  Dla każdego M∈[M_i,M_(i+1)],
  0≤q(M)≤max(q_i,q_(i+1)).
Jest ono automatyczne, jeśli nieujemny strumień N i dodatni strumień D są interpolowane WSPÓLNIE liniowo po masie: ich iloraz ma postać dodatniej kombinacji obu końcowych q. Także przy dodatnich N,D, gdy obie wielkości interpoluje się wspólnie w log, q jest geometryczną interpolacją wartości końcowych. Ale NIE sprawdzono tutaj, czy rzeczywisty natywny kod Wu–Xu używa takiej reguły dla strumieni/top albo czy nie ma wewnątrz przedziału fizycznego piku. Nie przypisuje się H_M STATUSU DOWODU FIZYCZNEGO. 100 oryginalnych q_i jest malejących na ZAOBSERWOWANEJ siatce, co wspiera, ale nie rozstrzyga H_M między węzłami.

Przy H_M, dodatnim bilansie Hawkinga i założeniach typowania mocy:
 B_HM(j)= [ M_min + Σ_(i=0..j-1) (M_(i+1)-M_i) max(q_i,q_(i+1)) ] / M_j
jest poprawną WARUNKOWĄ górną granicą udziału masowej energii początkowej przypisanej do potencjalnie niezbadanego top high. To nierówność obwiedniowa; składnik M_min jest celowo maksymalnie pesymistyczny q≤1 i dotyczy CAŁEJ nieobserwowanej fazy M<1e9g.

Odrębnie obliczono scenariusz liniowej interpolacji SAMEGO q_i po masie (trapezoidal sum w M), który daje mniejszą liczbową wartość, ale NIE jest granicą przy H_M i NIE jest obserwacją czasu rzeczywistego. Odmienna słabsza globalna hipoteza q(M)≤q(M_min)=0.015607 dla wszystkich M≥M_min daje jeszcze luźniejszą obwiednię, lecz także nie wynika wyłącznie z węzłów.

## 5. Wyniki z autentycznych 100 mas/10 000 węzłów

Przebieg q_i na autentycznej siatce maleje od:
  q(M=1e9g)=0.015607054684713455,
  q(j22, M=6.316227669701322e9g)=9.217349885910068e−16,
  q(j62, M=1.8023351397102734e11g)=0 (dokładnie zerowy w FLOAT oryginalnego dyskretnego źródła, nie teoretyczne continuum zero).
Przyjmuje wartości 0 dla 43 górnych mas, co może wynikać z ograniczeń reprezentacji / tablicy i nie dowodzi zerowej fizycznej emisji.

| Estymand | j22: M_init=6.31622767e9g | j62: M_init=1.80233514e11g |
| --- | ---: | ---: |
| q w M_init — statyczny ułamek w oryginalnej tablicy | 9.21735e−16 | 0 zapisane |
| Niezbadana faza M<1e9: do Mmin/Minit energii początkowej | 0.15832234876474735 | 0.005548357672040676 |
| W PRZEDZIAŁACH ZBADANYCH M≥1e9: scenariusz liniowej interpolacji q — NIE BOUND | 0.0006035363721316124 | 0.00002115074521568673 |
| W ZBADANYCH PRZEDZIAŁACH: górna obwiednia H_M | **0.0007322484998443729** | **0.00002566142186274145** |
| Cały przebieg: GÓRNA GRANICA wyłącznie przy H_M i bilansie energii | **0.15905459726459173 (15.90546%)** | **0.0055740190939034175 (0.557402%)** |
| Bardziej luźne H_global, q(M)≤q(Mmin) powyżej minimum | 0.1714584578944771 | 0.021068818835156242 |
| Bez założenia interpolacyjnego na niezmierzone przedziały | **1.0 (100%)** | **1.0 (100%)** |

Dla obu początkowych mas składnik górnej obwiedni z OBSERWOWANEGO odcinka ma TĘ SAMĄ równoważną masę energetyczną (q zasklepia się przy większych masach):
   ∫_(1e9..M_init) q_upper(M)dM = **4625048.235814 g**,
a całkowity dopuszczony wkład wraz z nieznanym końcowym etapem jest ≤**1004625048.235814 g** równoważnika energii. To nie znaczy, że tyle top wyemitowano: 1e9g jest całym, maksymalnie konserwatywnym i NIE ZAOBSERWOWANYM końcowym budżetem.

Iloraz niewiadomego M<1e9g do zbadanej obwiedni masowej wynosi **216.213961** w j22 i j62. Jest to nowy, ilościowy priorytet jakości: piętrzenie dokładności górnej energii w istniejących 100 węzłach daje ograniczony wzrost identyfikowalności, dopóki końcowe M<1e9g pozostaje nieudokumentowane.

Bardzo ważny kontrast: w ROT019 j22 początkowy SOURCE-hadron bound wynosił 4.04e−11, co brzmiało skrajnie mało. ROT020 pokazuje, że nawet czysto ENERGETYCZNY pełny przebieg może mieć LUŹNY bound 15.9% z powodu braku masowej siatki poniżej 1e9g, a nie z powodu tego, że początkowy top jest duży. To nie jest sprzeczność: porównywane są różne estymandy i zakresy.

## 6. Negatywna wiedza: czego te procenty NIE mierzą

1. Wartości 15.905% i 0.5574% są maksymalnymi możliwymi udziałami ENERGII początkowego PBH przy H_M, a NIE wartościami rzeczywiście emitowanymi w brakującym top i NIE błędami aktualnej tablicy Sc.
2. Dzielenie przez całkowitą początkową energię PBH NIE jest dzieleniem przez fizyczną energię zdeponowaną w hadronicznym oknie BBN; efektywne rozkłady czasu oraz masy, wydajność fragmentacji top i odpowiedź sieci jądrowej są nadal nieoznaczone.
3. Ułamek 0.5574% NIE jest limitem zmiany helium Yp o 0.5574%, ani limitem β o 0.005574 dex, ani dowodem poniżej-prerejestrowanej root noise.
4. H_M nie jest niezależnie zweryfikowaną własnością modelu Wu–Xu między węzłami masy; bez H_M nie ma nietrywialnej górnej granicy na całą ścieżkę z samych dyskretnych punktów. Surowe źródło nie obejmuje M<1e9g.
5. Nie wykonano natywnego REVIEW110 ani żadnego dodatkowego H71/BlackHawk/Julia/PRyMordial solvera; status własnego źródła Badacza pozostaje PREREG109 DEV2.
6. Starsze owner MOD_INTERMEDIATE dla modern-generator problemu jest osobną decyzją Moderatora, NIE jest tutaj otwierane ani zawieszane.

**Jedna uzasadniona rekomendacja:** najpierw zweryfikować, jak autorski native Wu–Xu interpoluje hadronowe tablice po masie i co dzieje się po zejściu M(t)<1e9g (czy klipuje, ekstrapoluje, kończy injection), a dopiero potem testować deklarację, że brakujący top/E100000 nie ma znaczenia dla native beta root. W przypadku braku zachowanych natywnych trajektorii nie należy twierdzić, że ostatni krok został zweryfikowany. Ten audyt wskazuje precyzyjną kolejność źródłowej falsyfikacji, bez wykonywania nowej fizyki.

## 7. Real execution, SHA custody, dispatch readiness

Pełna oryginalna Python3 stdlib:
 research/mech-s10/2026-11-22/code/mech_s10_rot020_raw_primary_mass_budget_missing_below_grid_conditional_energy_fraction.py
 commit **f1380adf88d790ea85fd4b110eeaa19bb600de33**, Git blob **34d90cc6221427844c1079b653dbce011d6c1e1a**.
Oryginalny source-reader ROT019 Git blob 5d12bfe84eb95a5fdd2f91011e2211a284c178ea jest sprawdzony przed importem; wewnętrznie sprawdza 7 dokładnych oryginalnych Git SHA plików, otwiera oryginalny gzip i oryginalne Sa. Żadne dane ROT019-JSON nie są używane do obliczeń. Cały nowy JSON zawiera 100 surowych q_i i siedem reprezentatywnych masowych przedziałów B_HM, bez przemilczanych wartości.

Wykonany jeden nieinteraktywny GitHub Actions source-only:
 https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/45063044425
workflow commit **f56236f3d895a41b4e68de2398e884ec5811f18c**, job COMPLETED SUCCESS, 10000 original source rows and 100 source masses replayed; output 7 SHAs source gated, no native physics.

Rzeczywiście pobrano artifact **14770431684**: ZIP **9292 bytes**, SHA256 **ebe83abd00316e18cf749574f2b6da612bc7a74223f8ed51bcd4297ee860ca18**, identyczny z provider digest; ZIP CRC PASS; oryginalny SHA256_MANIFEST **5/5 PASS**, STDERR EMPTY. JSON oryginalny wynik źródłowy SHA256 **ca16ba26b6cd2b8d58c1c898e935c8b7bf4a6df0b10fdd0dd6175749c2920f6c**.
Nie wykonano GitHub Actions nowych solverów fizycznych, żadnych eksperymentów Julia, Herwig7.1.5, BlackHawk, Pythia, PRyMordial.

FINAL:
ROT020_SOURCE_7_GIT_BLOBS_PASS /
ACTUAL_GZIP_10000_NODES_RECOMPUTED /
Q_MASS_GRID_MONOTONE_SAMPLED_ONLY /
FULL_EVAPORATION_ENERGY_FRACTION_HM_CONDITIONAL_J22_0P15905_J62_0P005574 /
MASS_BELOW_1E9_UNKNOWN_BUDGET_DOMINATES_BY_216X /
WITHOUT_HM_ONLY_TRIVIAL_UNCONDITIONAL_100PCT /
NO_Yp_OR_BETA_ROOT_BOUND / NO_NATIVE_PHYSICS / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
