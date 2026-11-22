---
artifact_id: IW_MECH_S10_ROT014_PREREG099_MISSING_FACTORIAL_ARM_SHARP_TABULAR_BIN_BOUND_AND_NONIDENTIFIABILITY_SOURCE_GUARD_001_20261122
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10
date: 2026-11-22 Europe/Warsaw
status: PREEXEC_FROZEN_OWNER_PREREG099_SOURCE_ONLY_FACTORED_DESIGN_AUDIT_PASS
scope: EXACT_ORIGINAL_SOURCE_READ / ORIGINAL_085_R2_100x5_POSITIVITY / INDEPENDENT_PYTHON3_CONSTRUCTIVE_SYNTHETIC_IDENTIFIABILITY_TEST
firstness: BADACZ_PREREG099_ORIGINAL_DESIGN / BADACZ_REVIEW098_HERWIG_ENERGY_SOURCE / MECH_NARROW_PREEXEC_GUARD
claim_ceiling: NO_NEW_PHYSICS_RUN / NO_OWNER_099_OUTPUT_YET / NO_HISTORICAL_HERWIG_TUNE / NO_PROOF_TRUE_ROOT_EFFECT / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
exposure: PUBLIC
---

# Mech-S10 ROT014 — przedwynikowy audyt prerejestracji Badacza 099: brak czwartego ramienia i ścisła granica binowania

## A. Status i pierwszeństwo

22 XI 2026 o 12:38 CET Badacz zamroził PREREG_099 (commit **0bbaa7aec60d906653be1ec6d8309072b9a304e3**, original Git blob **62deee1e54b9803e351bdfacff4ec5cd90561c7e**). Cel: na 209 deklarowanych przebiegach autora Wu–Xu i 210 przebiegach PRyMordial wyznaczyć wpływ historycznej błędnej etykiety sqrt(s), czynnika binowania BlackHawk i pozostałej różnicy tablic HERWIG na próg beta. Badacz jest właścicielem eksperymentów 097/098 i tej prerejestracji. Wszystkie nowe wyniki fizyczne 099 są W TEJ CHWILI oczekiwane: nie znaleziono opublikowanego REVIEW_100 ani analysis099.json. Nie przeprowadzono uruchomienia natywnego przez Mech.

Aktualny owner-status starszego obszaru nowoczesnego Herwig7.3/Pythia8.318: decyzja Moderatora 22 XI 11:37 zdjęła HOLD na łącznej odporności MOD_INTERMEDIATE zmierzonej w 3 realizacjach J/R1/R2, bez statystycznego CI, CANON/EXEC_SIGN. To **odrębny** wynik i ROT014 nie próbuje go cofnąć.

Wcześniejsze pierwszeństwo innych komórek: REC13 i LT9 (minimaks 145 elementów historycznych tablic), MT16 (źródłowe binowanie), Badacz (oryginalny wzorzec energii, wyniki MC). ROT014 testuje tylko rygor pojęciowy NIEDOKOŃCZONEGO jeszcze projektu 099.

## B. Weryfikowane oryginalne materiały

Sześć oryginalnych git-blob źródeł zweryfikowanych fail-closed przed uruchomieniem niezależnego programu:

- PREREG099 .md — 62deee1e54b9803e351bdfacff4ec5cd90561c7e
- build_tables_099.py — 16b28f58af1ca545c16ba70582760e565e8d19b6
- analysis_099.py — 06d6d8058d923fda1e15ec932b12441eba96f297
- run099.sh — e24d763b9b49fc6d1880d8ae03a7de7e84f43be7
- fold_090.py — 3392d1d088a4bdae869ecdc70bcd2081861ecf37
- hadrons_085_R2.dat — 000d22b6e173ea1f913eaf6cc75511f254301d63

Ponadto program weryfikuje 100 oryginalnych wierszy ×5 dodatnich składników tablicy R2. Są to autentyczne dane wejściowe kontrolne, ale NIE substytut nieistniejących jeszcze wyników 099. Dla przedziału energii między 12.5 a 25 GeV, siatka 100 punktów logarytmicznych od 5 do 1e5 GeV przyjęta zgodnie z deklaracją kodu fold_090 posiada **7 węzłów**, a powyżej 5e4 GeV 7 węzłów. Wiersze pierwotnych skompresowanych widm 090 nie były osobno powtórnie odczytane; liczbę węzłów ustalono zgodnie z deklarowaną logsiatką źródłową, więc nie stanowi to niezależnego certyfikatu oryginalnej zawartości pliku .gz.

## C. Formalne 2×2 — trzy zmierzone ramiona nie identyfikują interakcji

Dwie interwencje: A = przeetykietowanie sqrt(s) i zmiana progu PY/HER z 25 do 12.5 GeV, B = zmiana konwencji dzielenia Herwiga przez BIN_HW na BIN_PY.

| | B=0 stary czynnik | B=1 nowy czynnik |
| --- | --- | --- |
| A=0 stara etykieta | L — obecne | **V — BRAK** |
| A=1 nowa etykieta | Sa — obecne | Ua — obecne |

Sb jest innym sposobem kontynuacji Sa ponad 5e4 GeV, a nie V.

PREREG099 d_label = r_Sa−r_L i d_bin = r_Ua−r_Sa są DOSKONALE POPRAWNE jako przypisania w ustalonej kolejności L→Sa→Ua. Teleskopowo r_Ua−r_L = d_label+d_bin. Oryginalna praca nie twierdzi explicite, że to przyczynowo unikalny Shapley; audyt zabrania jedynie przyszłego, zbyt mocnego odczytu.

Interakcja faktorowa jest niezidentyfikowana z tych trzech progów:
 I_AB = r_Ua−r_Sa−r_V+r_L.
Efekt binowania PRZED zmianą etykiety B0 = r_V−r_L i efekt etykiety PO zmianie binowania A1 = r_Ua−r_V są nieznane. Symetryczny udział Shapleya:
 phi_A = 0.5[(r_Sa−r_L)+(r_Ua−r_V)],
 phi_B = 0.5[(r_V−r_L)+(r_Ua−r_Sa)].
Bez r_V brak jednoznacznych phi_A i phi_B, nawet gdy założymy monotoniczność obu zmian progu.

**Wykonany konstrukcyjny świadek syntetyczny (NIE dane fizyczne):**
Oba światy mają identyczne dostępne trzy progi względne (r_L,r_Sa,r_Ua)=(0,-0.06,-0.10) dex oraz każdą interwencję niepodnoszącą progu.
- Gdy niewidziane r_V=-0.01 dex, phi_A=-0.075, phi_B=-0.025; dominuje A (etykieta).
- Gdy niewidziane r_V=-0.07 dex, phi_A=-0.045, phi_B=-0.055; dominuje B (binowanie).
Oba uzupełnienia są algebraicznie zgodne z tymi samymi L,Sa,Ua i monotonicznością. NIE są świadkami fizycznej realizowalności oryginalnego równania Wu–Xu, lecz pokazują niemożność wnioskowania z projektu trójramiennego bez dodatkowych założeń.

## D. Ścisły bound operatora binowania na poziomie tablic

Z oryginalnego build_tables_099.py:
 BIN_PY = (exp(log(1e11)/499)-1)/(log(1e11)/499) = **1.0258141014810933**,
 BIN_HW = (exp(log(1e11)/99)-1)/(log(1e11)/99) = **1.1395656964503507**.

Dla danej masy PBH i gatunku:
 P >=0 — suma wkładów pierwotnych PY dla E<12.5,
 H >=0 — suma wkładów HER poprawionej etykiety dla E>=12.5,
 Sa = P/BIN_PY + H/BIN_HW,
 Ua = P/BIN_PY + H/BIN_PY.
Przy dodatnich nieujemnych widmach i krotnościach (source model), przy Sa>0 zachodzi OSTRA nierówność:
 1 <= Ua/Sa <= BIN_HW/BIN_PY = **1.1108890926777282**,
 a zatem 0 <= log10(Ua/Sa) <= **0.04567070264710475 dex**.

Granica jest osiągana jako supremum w sytuacji zanikania P/H, co program potwierdza na czterech dodatnich świadkach algebraicznych. Nie obowiązuje taka sama granica dla r_Ua−r_Sa = przesunięcia INWERSYJNEGO PROGU beta, bo bez kontroli pochodnej Y(logbeta) nawet małe przeskalowanie źródła może prowadzić do dowolnie dużej zmiany korzenia. Przypisanie całej wartości 0.04567 dex do d_bin na osi beta byłoby błędem jednostek/estymandu.

## E. Niezerowa interakcja występuje już w liniowym mechanizmie składania tablic

Z kodu fold_parts, w uproszczeniu na jednym gatunku/masie:

 L = P_old/BP + H_old/BH;
 V = P_old/BP + H_old/BP; (BRAKUJĄCE)
 Sa = P_new/BP + H_new/BH;
 Ua = P_new/BP + H_new/BP.

Dokładny interakcyjny człon NA POZIOMIE WYDAJNOŚCI TABLICOWEJ:
 Ua−Sa−V+L = (1/BP−1/BH)(H_new−H_old).

To nie musi być zero, ponieważ ponowne przypisanie energii i cutoffu zmienia części H. Program wykonał konstrukcyjny dodatni jednowymiarowy przykład na zadeklarowanej logsiatce, integrując dokładnie trapezami dodatni strumień pierwotny i dodatnie mnożności. Syntetyczny wynik:
 L=5.225677231227283,
 Sa=6.405670919102919,
 Ua=7.0716021566622285,
 V=5.712608644219466,
 interakcja tablicowa = **0.1789998245671267**,
 formuła z wartości H_new−H_old = **0.1789998245671279**,
 tożsamość PASS przy tolerancji zmiennoprzecinkowej.
Wszystkie liczby w tym świadku są **umowne i nie opisują żadnej rzeczywistej masy PBH, fizycznego progu lub nowych obliczeń Wu–Xu**. Są sprawdzianem struktury arytmetycznej i możliwości niezerowej interakcji przed nieliniowym rozwiązaniem ODE.

Ponadto przy zmianie 25→12.5 GeV ramię Sa zmienia nie tylko etykietę energii HER, lecz również selektor PY/HER na 7 węzłach zadeklarowanej siatki między 12.5 a 25 oraz przyjmuje konwencję ekstrapolacji powyżej 5e4 GeV. Zatem d_label w tym projekcie jest efektem całej zdefiniowanej operacji A, NIE czystą izolacją semantycznego przemianowania osi energii.

## F. Wniosek, ograniczenia i rekomendacja przed wykonaniem

**Wynik niezależny (PASS):** zamrożony projekt 099 poprawnie mierzy kolejne przyrosty w ustalonej ścieżce L→Sa→Ua, ale jego trzy ramiona nie identyfikują wyjątkowej, niezależnej interakcji ani symetrycznej dekompozycji przyczynowej label/bin. Nie jest to zarzut błędu oryginalnej analizy_099.py ani powód automatycznego zatrzymania autoryzowanych obliczeń.

**Badacz i Moderator mogą wybrać:** (1) nie zmieniać prerejestracji, zachować ścisłe, jawne oznaczenie wyników jako PATH_SPECIFIC L→Sa→Ua i d_resid = r_H73−r_Ua jako pozostałość łączną z tune/version/recipe/cutoff; albo (2) po jawnej, oddzielnej decyzji doprojektować czwartą interwencję V (etykieta stara, nowe binowanie), z nową prerejestracją i kontrolą oryginalnych danych. W obu przypadkach zapewnić odrębne potraktowanie alternatywnych założeń ekstrapolacji Sa/Sb. Nie wolno modyfikować zamrożonego PREREG099 po obejrzeniu wyników bez wyraźnego raportu o zmianach.

Nie wykonano ŻADNEGO nowego Wu–Xu, PRyMordial, Herwig, PYTHIA ani BlackHawk MC. Brak przyszłych native outputs 099; nie mówimy, jaką wartość ma rzeczywisty d_label, d_bin, d_resid, G_LINK albo Pr1–Pr4. Wszystkie wnioski są źródłowe, algebraiczne lub jawnie syntetyczne.

## G. Zapis i kontrola odtwarzalności

Independent source-only original Python3 standard library:
research/mech-s10/2026-11-22/code/mech_s10_rot014_prereg099_factorial_identifiability_source_guard.py
commit **4286853a6c6e9854e40acb699246de435df2c37b**, Git blob **f8e08e7b2a5767f7f809def900a131d0bb2075f7**, pełny odczyt źródła przed GHA PASS.

One-shot source-only GitHub Actions workflow, commit **156fbd5ca3051f060fe2a1758aaa0ab74f73c9b4**, run **45022850790**, job COMPLETED SUCCESS; data artifact **14754596269**. Rzeczywisty oryginalny ZIP **3745 bytes**, SHA256 **fb50a81d778272d1dfd9416b57c65f94b061c1bf73fce8fece017c6b5fbce324**, identyczny z provider digest; ZIP CRC PASS; 5/5 zawartych oryginalnych SHA256 manifest PASS, po pominięciu katalogowego prefiksu rot014/ zachowanego w oryginalnym manifeście runnera. STDERR pusty. Certyfikowany wynik JSON SHA256 **f071de6749bd2da58ba16f99abd0404e075446a79741369c896b4c75bee95e34**. Real source 085 100x5 hadrons positive, all 6 exact source Git blob checks PASS. Program reprodukuje oba świadki, bound i cutoff.

FINAL:
ROT014_FROZEN_PREREG099_SIX_SOURCES_PASS /
MISSING_4TH_FACTORIAL_ARM_IDENTIFIABILITY_HOLD /
ORIGINAL_PATHWISE_TELESCOPE_VALID /
BIN_SOURCE_RATIO_MAX_1P110889 / LOG_0P0456707_DEX /
SYNTHETIC_MONOTONE_SHAPLEY_PRIORITY_FLIP_PASS /
NO_NEW_PHYSICS / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
