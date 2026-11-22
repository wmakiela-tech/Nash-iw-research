---
artifact_id: IW_MECH_S10_ROT022_OWNER_REVIEW110_TRUE_TOP_ENDPOINT_POSTHOC_SOURCE_REPLAY_AND_WUXU_SUBGRID_EXTRAP_AMPLIFICATION_001_20261122
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
class: INDEPENDENT_ORIGINAL_SOURCE_ONLY_REFEREE / POSTHOC_109B_FIVE_ORACLE_REPLICATION / WUXU_ACTUAL_SUBGRID_INTERPOLATION_CONDITION
status: ACTUAL_ORIGINAL_10000_NODE_PRIMARY_SOURCE / ORIGINAL_HERWIG71_TOP_MC / ORIGINAL_Sc / FIVE_POSTHOC_ORACLES_EXACT / EXTRAPOLATION_AMPLIFICATION
owner_firstness: BADACZ_PREREG109_REVIEW110_R2_AND_FIVE_POSTHOC_SENSITIVITY_VARIANTS / MECH_ROT021_OFFICIAL_WUXU_LOGLOG_SOURCE_INTERPOLATION_FIRST
claim_ceiling: NO_ACTUAL_NATIVE_M_OF_T_AVAILABLE / NO_NEW_NATIVE_PHYSICS / NO_BBN_Yp_OR_BETA_ROOT_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# Mech-S10 ROT022 — 0.011 dex w zakresie tablicy Sc nie ogranicza ekstrapolowanej szybkości hadronowej poniżej 10^9 g

## 1. Zmiana stanu właścicielskiego, firstness i rodzaj wyniku

W porównaniu z ROT021 Badacz **opublikował rzeczywiste wyniki PREREG109 w REVIEW110**, następnie REVIEW110 r2 i nową PREREG112 (22 XI 2026):
- commit 1a7f80ad8c33736897a31d38e407e8562c7ea385: REVIEW110; owner natywne Julia 3 procesy, PRyMordial 54/54, GATE 6/6; szew oryginalnych Herwig7.1.5 48/48, Pr1–Pr3 PASS, G_MC z jawnym wyłączeniem top/E100000 = 29/30; Sc bliska gałęzi Sb j22, a nie Sa;
- commit 2bf0b18938e1567ea20428c1e9b55f5a845e4463: REVIEW110 r2 naprawa błędnie odjętego d_ctrl od residuum odniesionego już do L; nowa zamrożona PREREG112, która rozdziela rocznik generatora i obróbkę tablic;
- REVIEW106 r2 Badacza przyjmuje korektę Mech-S10 ROT017: 0.009689 dex ≈ 2.256%, nie 1%; REVIEW110 §4 Badacza wprost przyjmuje wcześniejszą obserwację ROT018, że G_MC PASS 29/30 NIE jest kompletnym pomiarem 30/30 i Sc jest warunkowa względem top-hi-clip.

Nie wolno nadal twierdzić, że PREREG109 pozostała bez wyników. Odrębna wyszukiwarka commitów wyłącznie z przedrostkiem research(badacz) NIE wychwytywała nowych, rzeczywistych commitów Badacz B1: użyto szerszego wyszukiwania REVIEW_110 i odczytano źródła najnowszego commitu. To jest ważna korekta custody, nie zmiana fizyki.

**Firstness:** Wszystkie oryginalne wykonania natywne, tablica Sc, warianty top ×0, ×0.5, ×2, ×3 i slope oraz wynik wrażliwości dla 0..28 wierszy są od Badacza REVIEW110, nie nowe Mech. Mech ROT021 wcześniej odczytał i oryginalnie przypiął publiczny kod Wu–Xu log-log extrapolation. **Nowy ROT022** łączy ten dokładny operator ze źródłowo odtworzonymi rzeczywistymi wariantami TOP oraz wyprowadza poza zakresem tabeli ich deterministyczny wpływ na rate_h(M). Bez nowych fizycznych solverów.

## 2. Oryginalne źródła, faktyczny odczyt, zamrożone obiekty

Niezależny source-only Python3 w GitHub Actions:
- ponownie otworzył oryginalny 100×100×14 skompresowany BlackHawk primary_spectra_090.tsv.gz (pierwotny Git blob e2079be0b6dfab12a743c09e6937f1d2383d3a57) przez zamrożony SHA-checker Mech ROT019 blob 5d12bfe84eb95a5fdd2f91011e2211a284c178ea;
- przeprowadził jego wszystkie siedem źródłowych SHA guards, 10000 faktycznych węzłów, przeliczenie 100 mas oraz pochodnej kolumny Phi_top;
- sprawdził dodatkowych siedem oryginalnych owner source Git blob SHA:
  * mc109/herwig71_top.json 58e48b22ad58bb50d4b4729efc5f30696c3d865b: 2 rzeczywiste, dobre węzły MC top przy E=50000,70710.678; E=100000 FAILED (rc_run=-6);
  * hadrons_109_Sc.dat 2cc859a1a44a1b8fafa479f6c844a76bd2db5afe;
  * hadrons_099_Sa.dat 3aac28554204e6b6951a7472773535ad3c8613ea;
  * posthoc109b.json d47a8bfee70ed7d1ad0b2b606330f41fe0433b9c;
  * posthoc_109b.py 3545fdb65510f95bef6980b2970f9a4f5417f2e1;
  * REVIEW110 r2 c818f071d7473ab0752d2e6329aa8388cba8f745;
  * fold_090.py 3392d1d088a4bdae869ecdc70bcd2081861ecf37;
- pobrał i zweryfikował jeszcze oryginalny oficjalny blob autorski tool_script-hadrons_from_PBH.jl = cc73432910f872d526113ce59b6204f38d0766a9 z author commit d395183674cace6c9906a8911bdeb7234ba4040d. Oryginalny autor definiuje pięć LinearInterpolation(log(rate),log(mass); extrapolation=Linear).

Kontrole dotyczą autentycznych bajtów z repo, a nie tylko streszczeń. Lokalny kod wykonywany przez właściciela pod /home/claude/fenyutanchan wciąż nie był niezależnie zweryfikowany na tożsamość Git SHA, ale opublikowany kod źródłowy autorów i właścicielskie tablice są rzeczywiście przeczytane.

## 3. Ścisłe odtworzenie pięciu oryginalnych post hoc wariantów Badacza

Najwyższa dobra energia top MC E_last=70710.67811865475 GeV. Dla każdego z pięciu hadronów w prawdziwym herwig71_top.json najnowsza krotność per PRIMARY wynosi 0.5 × średnia per pair ze źródłowego MC (Herwig sqrt(s)=2E).

Całka faktycznego TOP high segmentu:
  T_h(M_j)=HBAR/BIN_HW × trapezoid_E [Phi_top(E,M_j) × n_top,h(E_last) × 1_(E>E_last)].
Rzeczywisty owner Sc_j,h w pliku podaje źródłową szybkość w jednostkach GeV, a zatem T_h/Sc_h jest udziałem tego jednego segmentu w tablicy. Dla k∈{0,0.5,2,3} rzeczywisty source-only wariant właścicielski:
  Sc_{k,h}(M_j)=Sc_h(M_j)+(k−1)T_h(M_j).
Dla slope TOP skrypt bierze rzeczywisty exponent nachylenia z dwóch dostępnych węzłów MC 50000→70710 i zastępuje tylko segment E>E_last; reszta tablicy Sc pozostaje niezmieniona.

Wszystkie 100 mas × 5 hadronów zostały wyliczone z rzeczywistych danych w sposób niezależny od kodu posthoc109b.py. Następnie ODTWORZONO oryginalne maksima |log10(Sc_k/Sc)| na wierszach j=0..28: pięć oryginalnych wartości przeszło kontrolę z błędem numerycznym ≤9.6e−17 dex. Maximum udziału top segmentu 0.012946579376600301 oryginalnego Badacza odtworzono jako 0.012946579376600303 (różnica ≈1.7e−18). Zgodność 5/5 jest niezależnym materialnym source-I1; oryginalne pomiary i firstness należą do Badacza.

| Post hoc Badacza | max |Δ log10 Sc|, rzeczywiste masy j0..j28 |
| --- | ---: |
| top segment ×0 | 0.005659342108340782 dex |
| ×0.5 | 0.002820452675908654 dex |
| ×2 | 0.005586542207547937 dex |
| ×3 | 0.011102133699749604 dex |
| kontynuacja nachylenia TOP MC | 0.00016791383622046674 dex |

GATE 5/5 original-posthoc-oracle EXACT; nie było żadnego ponownego Herwig/BBN run. To poprawny i zachowany **wniosek oryginalny**, ale jego dziedziną są właśnie 29 oryginalnych wierszy, NIE całe M(t).

## 4. Nowy operatorowy kontrast: ten sam wariant poza zakresem masy

W publicznym oryginalnym Wu–Xu funkcja przy M<M0=1e9g jest deterministycznym log-log LINEAR extrapolation ze źródłowych wierszy 0 i 1:
  log R_k(M) = (1−lambda) log R_k(M0)+lambda log R_k(M1),
  lambda=ln(M/M0)/ln(M1/M0).
Tożsamość dla dowolnego owner Sc_k względem owner Sc:
  log10[R_k(M)/R_Sc(M)] =
    (1−lambda) log10[Sc_k(M0)/Sc(M0)]
      +lambda log10[Sc_k(M1)/Sc(M1)].
Nie jest to nowa fizyka i nie korzysta z sintetycznej zmiany liczb; źródłowe Sc_k(M0,M1) wyliczono z pięciu prawdziwych owner wariantów post hoc.

W pierwszych dwóch wierszach oryginalnego Sc udział wysokiego top dla pięciu hadronów wynosi:
 - j0 M=1e9g: od 0.0119849 do 0.0129466 (1.20–1.295%);
 - j1 M≈1.087388e9g: od 0.00793497 do 0.00856621 (0.793–0.857%).
Jest to wystarczająca, NAPRAWDĘ OBSERWOWANA różnica KIERUNKOWEGO NACHYLENIA w dwóch brzegowych wierszach, aby przy kontynuacji loglog rosła różnica Sc_alt/Sc w malejącej masie.

**Ważne konkretne świadectwa** (max po pięciu gatunkach, wartości rzeczywistych tabel plus autorski operator):
| TOP wariant post hoc | max abs Δ log10 szybkości w j0..j28 | M=1e8g (poza siatką) | M=1e6g (poza siatką) | przy domyślnym hipotetycznym progu j22 13.02g |
| --- | ---: | ---: | ---: | ---: |
| ×0 | 0.00566 | 0.05851 | 0.16422 | 0.42243 |
| ×0.5 | 0.00282 | 0.02910 | 0.08167 | 0.21008 |
| ×2 | 0.00559 | 0.05732 | 0.16077 | 0.41349 |
| ×3 | 0.01110 | 0.11347 | 0.31821 | **0.81833** |
| slope z dwóch węzłów MC | 0.000168 | 0.00173 | 0.00487 | 0.01252 |

Dla post hoc ×3 przy j22 hipotetycznej masie końcowej 13g, source-rate ratio Sc_3/Sc wynosi od **5.725 do 6.582** (w zależności od hadronu); przy hipotetycznym progu j62 371g największe |Δ log10|=0.66934 dex i ratio 4.167–4.670. Sc_0 (cały high top wyzerowany) w tym samym j22 stop daje między 0.378 a 0.407 razy bazowa Sc. To ekstremalne **formalne** ekstrapolacje, nie pomiary fizycznej hadronizacji przy M=13g.

Na przykład dla ×3 już przy masie PBH około (6.20–6.54)×10^8g pięć ekstrapolowanych źródeł przekracza |Δ log10|=0.03 dex, chociaż we wszystkich 29 historycznych wierszach było ≤0.0111 dex. Próg 0.03 ma znaczenie tylko jako porównywana wartość numeryczna; jest tolerancją szumu pojedynczego root BADACZ, nie wyliczoną tolerancją RATE ani kwantylowym CI.

Dodatkowo **rzeczywista Sc/Sa** w oryginalnym najniższym wierszu różni się tylko o +1.8…+2.85%, ale w hipotetycznym j22 Mstop po tym SAMYM algorytmie loglog różni się 3.94–5.28-krotnie. Jest to osobny rzeczywisty kontrast dwóch różnych tablic; nie należy mieszać z niepewnością missing top, ale ilustruje tę samą kondycję brzegową.

## 5. Co wolno stwierdzić, a co pozostaje otwarte

**PASS i zachować:** właścicielski wynik 6/6 GATE, 48/48 SEAM, Pr1–Pr3 PASS, Sc≈Sb w j22, 29/30 G_MC z jawnym wyłączeniem. Oryginalna analiza posthoc109b 0.0111 dex w wierszach j0..28 jest POPRAWNA; Mech uzyskał pięć dokładnych oracle źródłowych.

**SCOPE_CORRECTION_REQUIRED:** nie wolno opisywać 0.0111 dex jako górnej granicy NA CAŁE źródło hadronowe R_h(M(t)) Wu–Xu, a tym bardziej jako automatycznego dowodu wpływu na native root poniżej 0.03 dex. Prawdziwy kod ekstrapoluje obwiednię pierwszych dwóch wierszy i może znacznie powiększyć source-rate contrast dla małego M. To wykazano na RZECZYWISTYCH source-variantach owner, bez jakichkolwiek nowych fizycznych założeń poza tym samym operatorem kodu.

**Nie dowodzi to owner paper error, fizycznego PBH bound ani root instability:** Ekstrapolacja nie jest fizycznie zweryfikowanym modelem hadronizacji przy 13g; nie mamy wystawionych czasów M(t), czy i kiedy PBH osiąga m<1e9g, ile energii/hadronów deponuje w efektywnym oknie BBN, ani rozwiązania wrażliwości Yp. Wariant ×3 był przez owner oznaczony jako post hoc ekstremalny, NIE realistyczny 1σ. Zmiana szybkości w Mstop nawet o 0.818dex NIE implikuje przesunięcia beta root o 0.818dex. Czasowy i nuklearny operator jest niezweryfikowany w tej rotacji.

**Rekomendacja źródłowa:** W REVIEW110 doprecyzować zdanie z §4 jako „0.0111dex max w wierszach j0–j28, przed natywną ekstrapolacją poniżej M=1e9g, bez ilościowego bound na root”. Jeżeli Badacz uzna fizyczną wrażliwość za ważną, następnym owner źródłowym zadaniem jest porównać realne zachowane masowe trajektorie M(t) i przejścia poniżej m0, a następnie zaplanować JEDEN prerejestrowany BBN sensitivity run dla wybranych alternatyw k przy rzeczywistej, zaobserwowanej masie; wyłącznie za właściwą autoryzacją. Nie jest wymagana kolejna ogólna seria generatorów bez danych o dynamice M(t).

## 6. Faktyczne wykonanie, custody i negatywna wiedza

Niezależny Python3 (stdlib):
 research/mech-s10/2026-11-22/code/mech_s10_rot022_owner109_true_top_segment_extrapolated_hadronic_source_referee.py
 original commit **5b075b6a3f5d8d6093334af93f33f82cd1afaf3e**, Git blob **9feb8c6c7858405387f7d3e66b2abcbfe7cb220f**.

Wykonany rzeczywiście jeden source-only GitHub Actions:
 https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/45069337167
 workflow commit **ec7f8c37d1c6a9fecff3ef98b7c61a93ff3659cb**,
 SUCCESS, 7 dodatkowych oryginalnych Git SHA owner, reader 7 starszych SHA, publiczny Wu–Xu Git blob, 10000 realnych oryginalnych rekordów, 100 wierszy Sc, 2 rzeczywiste+1 nieudane MC top, exact owner five POSTHOC109b oracles.

Original artifact id **14771929108**, rzeczywiście pobrane archiwum ZIP **7952 bytes**, SHA256 **7c73f51a023e0fdd5a590a3a905a48baada224ca1931bf85e1f1a61a96221195** identyczny z provider, ZIP CRC PASS, oryginalny SHA256_MANIFEST 5/5 PASS (prefiks rot022/ z manifestu mapowany na spłaszczone nazwy ZIP), STDERR pusty; JSON pełny 100×5 pięciu wariantów w warunkowych granicach i 5/5 oracles **21498 bytes** SHA256 **dc4bb93dc02dd4a96836292ca484bdbce79dc12e31145359b9c51aa8237fadbe**. Żadne Herwig/BlackHawk/Julia/PRyMordial ani nowe natywne obliczenia fizyczne nie zostały wykonane.

FINAL:
ROT022_TRUE_OWNER_REVIEW110_CURRENTNESS /
ORIGINAL_10000_SOURCE_GZIP_CHECK /
OWNER_MC_TOP_2_REAL_1_FAILED /
OWNER_5_POSTHOC_SENSITIVITY_ORACLES_EXACT /
IN_TABLE_0P011102_DEX_PASS /
REAL_SOURCE_LOGLOG_SUBGRID_AMPLIFICATION_UP_TO_0P8183_DEX_AT_HYPOTHETICAL_J22_STOP /
NO_NATIVE_Yp_OR_BETA_ROOT_BOUND /
NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
