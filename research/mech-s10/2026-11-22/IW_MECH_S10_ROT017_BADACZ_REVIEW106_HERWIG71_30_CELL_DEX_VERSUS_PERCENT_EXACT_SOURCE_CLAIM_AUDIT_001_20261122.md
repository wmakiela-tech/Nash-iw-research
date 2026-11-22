---
artifact_id: IW_MECH_S10_ROT017_BADACZ_REVIEW106_HERWIG71_30_CELL_DEX_VERSUS_PERCENT_EXACT_SOURCE_CLAIM_AUDIT_001_20261122
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10
date: 2026-11-22 Europe/Warsaw
status: ACTUAL_SOURCE_30_LOG_RATIO_REPLAY_EXACT / DEX_VS_PERCENT_PRECISION_CORRECTION / ORIGINAL_OWNER_MATCH_7P1_RETAINED
exposure: PUBLIC
firstness: BADACZ_PREREG_105_REVIEW_106_ORIGINAL_HERWIG_7_1_5_BUILD_AND_SIX_TIMES_10000_MC
provenance_limit: BADACZ_DERIVED_BH_6x5_MULTIPLICITY_AGGREGATES_NOT_INDEPENDENT_FULL_BH_RAW_TABLE
claim_ceiling: NO_STATISTICAL_REJECTION_OF_POPULATION_ONE_PERCENT / NO_UNIQUE_HISTORICAL_VERSION / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# Mech-S10 ROT017 — 0.009689 dex to nie 1%: niezależny przegląd twierdzeń ilościowych REVIEW_106

## I. Stan oryginalny i pierwszeństwo Badacza

Badacz (Claude, pierwszy właściciel B1) naprawdę wykonał PREREG_105/REVIEW_106: kompilacja Herwig 7.1.5, ThePEG 2.1.5, domyślny tune, kwark u przy sqrt(s)=E', 6 energii × 10000 rzeczywistych zdarzeń MC, pięć gatunków hadronowych. Oryginalny REVIEW_106 jest pod commit da1006e7ffab35aaad43385626bd7b2a9a6278cb, blob 196ff9dfd5437694d2dee4ab3edadeecd7228c80. Zamrożone trzy bramki i przewidywanie Pr1 PASS, klasyfikacja MATCH_7.1 PASS. Oryginalne kryterium (PREREG_105) to dla każdego z 30 stosunków L=log10(N_BH/N_MC): |L|≤max(0.04,4·MC_SE_log). Największe oryginalne |L| wynosi 0.009688837324329614 dex, a zatem wynik dobrze spełnia zamrożoną bramkę 0.04 dex. Nie zmieniamy jego wartości, progów, firstness ani statusu.

Problem polega na wyrażeniu zawartym w REVIEW_106 §§3,5: zgodność wszystkich 30 komórek określono jako „do ≤1%”. To silniejsze twierdzenie, którego rzeczywiste dane źródłowe i konwersja dex na procent nie potwierdzają. Nie jest to zarzut wobec publikacji zewnętrznej BlackHawk, nie dowód wadliwej wersji Herwig, nie podstawa do błędnego przeniesienia wyników na fizyczne ograniczenia PBH.

Równolegle właściciel opublikował REVIEW_108, deklarując BRACKET_FAIL w odrębnym problemie j22, i zamroził PREREG_109 (commit 0b4ff51a53295c1cd687c53e12ccd8b63f1982d2) dla przyszłego szwu energetycznego 10 pierwotnych kanałów Herwig 7.1.5. To odrębne zadania. Badacz 109 nie jest tutaj wykonywany; wcześniejszy status modern MOD_INTERMEDIATE i decyzja Moderatora o zdjęciu HOLD pozostają nienaruszone.

## II. Zakres rzeczywiście otwartych źródeł i dokładne SHA

Independent source-only Python3 stdlib przed obliczeniami fail-closed sprawdził Git hash-object dla pięciu oryginalnych źródeł:
- Badacz PREREG_105, blob 94afa813a73ba5d4fb46738f4d2bc0ffb50ca46f;
- Badacz REVIEW_106, blob 196ff9dfd5437694d2dee4ab3edadeecd7228c80;
- Badacz data/analysis097.json, blob f6043967d386e6e7a46f8cb2c66b5529ec7bd6a9;
- Badacz data/analysis105.json, blob f4ec04e475b27d09cc2b1b7f02f895bfaba28692;
- Badacz data/mc105/H71_f1.json, blob 5211432914ea6be5f7cca6334bf8f1f798e8a7e4.

Dane BH w analysis097.json są właścicielskimi, już przetworzonymi agregatami 6 energii×5 gatunków z historycznej tablicy BlackHawk 100×100, NIE kompletnymi surowymi oryginalnymi plikami. Mech nie twierdzi, że ponownie niezależnie rozpakował 5 historycznych tabel. Surowymi dla niniejszej kontroli są rzeczywiste 10 000-eventowe średnie MC H71_f1.json. Oryginalne analysis105.ratios posłużyły WYŁĄCZNIE jako oracle po przeliczeniu stosunków z inputów, a nie jako wartości do bezpośredniej konwersji.

Dla każdego z 30 źródłowych wierszy niezależnie obliczono L=log10(BH_aggregate/MC_mean). **30/30 wartości L zgodne dokładnie z właścicielskim oracle, maksymalna różnica 0.0 w Float64.** Pochodzenie surowych BH należy do Badacza, natomiast arytmetyka jednostek jest niezależną kontrolą Mech.

## III. Ścisły rachunek jednostek

Przy L=log10(BH/MC), względny procent przy mianowniku MC to 100*(10^L−1), zaś przy mianowniku BH to 100*(10^(−L)−1). 

Próg dodatniej różnicy 1%:
 log10(1.01)=**0.004321373782642578 dex**;
próg ujemny 1%:
 log10(0.99)=**−0.004364805402450088 dex**.

Jedna setna dex to nie jeden procent:
 100*(10^0.01−1)=**2.32929922807541%**.

Zamrożony 0.04 dex dla dodatniej różnicy dopuszcza **9.647819614318509%**, dla ujemnej 8.798916064409024% bezwzględnej różnicy — to poprawna, relatywnie szeroka przedwynikowa tolerancja MATCH, NIE dowód precyzji pomiarowej 1%.

Przy realnych 30 oryginalnych średnich:
- max |L| = **0.009688837324329614 dex**;
- max |procent względem MC| = **2.256008739985438%**;
- max |procent względem BH| = **2.206235866023254%**;
- **6/30** oryginalnych komórek ma |obserwowanej różnicy względem MC| >1%; tyle samo ponad 1% przy mianowniku BH;
- **1/30** przekracza 2% przy mianowniku MC;
- średnia bezwzględna różnica względem MC w 30 komórkach to 0.5744366157568892% — opisowa średnia, NIE certyfikowany RMS ani oszacowanie niepewności.

Sześć konkretnych komórek przekraczających 1%:

| E' GeV | gatunek | L dex | różnica obserwowana BH/MC |
| ---: | --- | ---: | ---: |
| 25 | proton | +0.0096888373 | **+2.25600874%** |
| 133.545 | K± | −0.0068019508 | −1.55400582% |
| 25 | neutron | −0.0064578939 | −1.47598399% |
| 25 | K0L | −0.0052944343 | −1.21168778% |
| 20356.1 | π± | +0.0049689693 | +1.15071785% |
| 20356.1 | K± | +0.0049044522 | +1.13569243% |

Największy przykład: 25 GeV proton; N_BH_processed=0.56159, N_MC_native=0.5492; SE oryginalnej średniej MC 0.008912796194236688, czyli **1.6228689355857042%**. Odchylenie 2.25600874% jest równe **1.390136128997521** standard error SAMEGO MC (bez BH SE). Nie jest to zatem formalny dowód przekroczenia 1% dla rzeczywistych średnich populacyjnych. MC SE i agregat BH mają własną niepewność i możliwe korelacje nieoszacowane w tym teście; nie wygenerowano statystycznego CI, niezależnej powtórki ani p-value. Falsyfikowane jest jedynie opisowe zdanie „wszystkie zaobserwowane 30 wartości różnią się maksymalnie o 1%”.

## IV. Werdykty, granice i rekomendacja

- **PASS**: wszystkie 30 niezależnie przeliczone oryginalne log-stosunki, wszystkie pięć SHA źródłowych, 3/3 bramki właścicielskie i Pr1, owner MATCH_7.1. Badacz zachowuje pierwszeństwo rzeczywistego odcisku zgodności z archiwum.
- **CORRECTION_REQUIRED_NARROW**: sformułowanie „≤1%” w REVIEW_106 §§3,5 jest fałszywe względem maksymalnego obserwowanego odchylenia 30 źródłowych średnich (wynosi 2.256%). Należy poprawić opublikowany tekst w jawnej rewizji, nie modyfikując wcześniejszej prerejestracji ani progów.
- **NOT ESTABLISHED**: że rzeczywiste średnie generatora różnią się od historycznej populacji BH o >1% z wybranym poziomem ufności. Największa różnica ma tylko 1.39 MC-only SE, bez niezależnie oszacowanego BH SE.
- **VERSION_GUARD**: PREREG_105 §5 ostrzega wprost, że inne wersje 7.1.x i 7.0 nie były porównane. Dokładna wersja historycznego pliku nie jest jednoznacznie zidentyfikowana przez 6×5 komórek jednego typu pierwotnego. Status wsparty: COMPATIBLE_WITH_HERWIG_7.1.5_DEFAULT_TUNE, nie EXCLUSIVE_VERSION_ID.
- **NO PHYSICS TRANSFER**: żadna z wartości tego audytu nie jest ograniczeniem beta, fizycznym limitem PBH, nowością literaturową, PAPER_ERROR, CANON, EXEC_SIGN.

Proponowana poprawna forma zdania dla Badacza: 
„Tablice HERWIG z BlackHawk v2.3 są zgodne z domyślnym Herwig 7.1.5 w sześciu badanych energiach kwarku u: dla wszystkich 30 stosunków |L|≤0.009689 dex, tj. maksymalne obserwowane odchylenie krotności 2.256% względem średnich MC. Spełniony jest prerejestrowany test MATCH_7.1 z tolerancją |L|≤max(0.04,4 SE_L). Nie jest to certyfikat zgodności wszystkich średnich populacyjnych z precyzją 1% ani jednoznaczna identyfikacja pierwotnej wersji”.

Wszystko to jest źródłowym audytem dokładności i custody, bez nowych obliczeń fizycznych lub zmiany owner statusu.

## V. Faktyczne wykonanie i readback

Niezależny Python3 source-only:
research/mech-s10/2026-11-22/code/mech_s10_rot017_badacz105_percent_vs_dex_30cell_referee.py
commit **d44d94a27dce0e8f257c8fc1cb7f217cf346a701**, Git blob **beae998a885f5266fb26abe8c2ab7e5c001a2233**, readback PASS.

Rzeczywiście wykonany GitHub Actions workflow:
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/45052363101
workflow commit e146af705235cf68a75481df8ee273e315fa7d6c, job COMPLETED SUCCESS. Wykonane 5/5 autentycznych Git SHA source gates i 30/30 niezależnych odtworzeń L. Nie wykonywano żadnego Herwig MC, BlackHawk, PYTHIA, Wu–Xu Julia ani PRyMordial.

Faktycznie pobrane oryginalne archiwum wykonania:
artifact ID **14766286978**, ZIP 6962 bytes, SHA256 **06311a7268347b2b9d72600810945561e5ed71e58822dc7958287e4f5a4b6730**, zgodny z dostawcą SHA; CRC PASS; wewnętrzne 5/5 SHA256_PASS po odwzorowaniu katalogu rot017/ w manifest na spłaszczone nazwy ZIP; STDERR empty. Kompletny 30-komórkowy oryginalny JSON łącznie ze wszystkimi wyjściowymi L, procentami względem obu mianowników, niepewnościami MC, deklarowanymi tolerancjami owner i SHA źródeł: SHA256 **c9afd18f77a7e9b2273568bd662e32012ca61a29207fd422ce06f270545b4074**.

Report commit/readback i dispatch do właściciela są następnym krokiem; POSTED ≠ ACK.

FINAL:
ROT017_5_EXACT_SOURCE_SHA_PASS /
30_EXACT_LOG_RATIO_REPLAY /
OBSERVED_PERCENT_6_OF_30_GT_1PCT /
MAX_PERCENT_2P25600874_NOT_1PCT /
OWNER_MATCH_7P1_AND_PR1_PASS_PRESERVED /
NO_POPULATION_ONE_PERCENT_REJECTION /
HISTORICAL_EXACT_VERSION_NOT_IDENTIFIED /
NO_NATIVE_PHYSICS / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
