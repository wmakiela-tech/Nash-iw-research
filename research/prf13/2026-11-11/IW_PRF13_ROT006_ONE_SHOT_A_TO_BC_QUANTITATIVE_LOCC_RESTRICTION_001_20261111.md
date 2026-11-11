---
artifact_id: IW_PRF13_ROT006_ONE_SHOT_A_TO_BC_QUANTITATIVE_LOCC_RESTRICTION_001_20261111
created_at: 2026-11-11
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_12 / PRF13
source_type: SOURCE_NATIVE_EXACT_8X8_THREE_QUBIT_AND_RATIONAL_ROOT_ISOLATION_THEOREM
exposure: PUBLIC
sync_state: LOCAL_ARCHIVE_PENDING_GITHUB_AND_BW
status: EXACT_RATIONAL_16_VERTEX_PROOF / INDEPENDENT_8X8_AUDIT / EXTERNAL_REFEREE_PENDING
claim_ceiling: NO_UNRESTRICTED_LOCC_CLOSURE_GAP / NO_GLOBAL_LOCC_OPTIMUM / NO_HARDWARE / NO_PHYSICAL_SWAP_EXTENSION / NO_NOVELTY_INFERENCE / NO_CANON / NO_EXEC_SIGN
---

# PRF13 ROT006 — Ilościowa luka Helstrom–LOCC dla pomiaru jednoetapowego A→BC w trójkubitowym modelu Cauchy–Lévy

**Data:** 11 XI 2026. **Werdykt wewnętrzny:** dokładnie weryfikowalny, warunkowy wynik matematyczny dla nowej ograniczonej klasy pomiarów. Potrzebna niezależna recenzja. Bez eskalacji do twierdzenia o pełnym LOCC.

## 0. Pierwotny problem, status wcześniejszych prac i odejmowanie literatury

Punkt wyjścia: PRF11 R35 (jeden statyczny ukryty Cauchy ξ dla trzech ekspozycji kontra niezależne przyrosty Cauchy–Lévy), PRF12 R04–R05 (dokładny trójkubitowy stan końcowy i separowalny pomiar Helstroma), R06 (lokalny finite-round no-go), R08 (osiągalny adaptacyjny protokół trójstronny), R09 (KRYTYCZNA KOREKTA: wycofanie R07 dodatniej luki dla domknięcia pełnego LOCC), R10 i R12 (ograniczenia drobnoziarnistych pomiarów produktowych). W szczególności R09 zakazuje wnioskowania o full LOCC z argumentu zbudowanego wyłącznie dla dwóch zagregowanych efektów E_A/E_B. Obecny ROT006 **nie** używa tego argumentu.

Dokładne materiały źródłowe:
- https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R04_THREE_PROBE_FINITE_SWAP_EXACT_X_READOUT_GAP_AND_SECTOR_DECOMPOSITION_001_20261026.md
- https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R08_EXACT_ADAPTIVE_LOCC_WITNESS_AND_DELTA_UPPER_BRACKET_001_20261026.md
- https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R09_COARSE_GRAINING_COHEN_THEOREM_AUDIT_AND_CORRECTED_CLAIM_CEILING_001_20261026.md
- https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-27/IW_PRF12_R12_RANKONE_RIGIDITY_PRODUCT_EFFECT_MINIMALITY_AND_EQUATORIAL_LOCC_001_20261027.md

Literatura zewnętrzna (metody dojrzałe, nie dowód nowości): Cohen, *Local approximation of multipartite quantum measurements*, Phys. Rev. A 105, 022207 (2022), https://doi.org/10.1103/PhysRevA.105.022207 ; Cohen, *Local approximation for perfect discrimination of quantum states*, Phys. Rev. A 107, 012401 (2023), wraz z erratą; Cohen, *Asymptotic implementation of multipartite quantum channels and other quantum instruments*, arXiv:2310.05362 (preprint); Kleinmann–Kampermann–Bruß, Phys. Rev. A 84, 042326 (2011); podstawy: Helstrom (1976). Nowy, jeszcze nierecenzowany kontekst badawczy: Steven Abel, *Complete Certificates for LOCC State Discrimination and the Exact Domino Value*, SSRN 7573038 (wersja X 2026), https://ssrn.com/abstract=7573038. Te prace NIE są przesłanką techniczną poniższego dowodu; brak claimu pierwszeństwa.

## 1. Zamrożony model i cel

Trzy fizyczne kubity przygotowane w |+>^⊗3, idealnie chwilowe przełączenia SWAP, trzy jednakowe ekspozycje T/3, zerowe starzenie pamięci κ=0. Hipoteza A: wspólne statyczne ξ~Cauchy(0,γ). Hipoteza B: niezależne inkrementy symetrycznego procesu Cauchy–Lévy. Nie ma dodatkowych pomocniczych zasobów splątanych ani przekazu kwantowego między laboratoriami.

Niech q=γT/3>0, x=e^(−q), b=1−x²>0, a=xb. Różnica stanów końcowych D=ρ_A−ρ_B jest w 8D:

    D_{u,v}=(x^|Σ_j(u_j−v_j)| − x^Σ_j|u_j−v_j|)/8,
    u,v ∈{0,1}³.

Równoważne rozwinięcie Pauliego (oznaczenia X_j,Y_j w trzech laboratoriach):

    D=(b/16) Σ_{j<k}(X_jX_k+Y_jY_k)
      +(xb/32)(3X_1X_2X_3+X_1Y_2Y_3+Y_1X_2Y_3+Y_1Y_2X_3).

Tr D=0, ‖D‖_1=b, a optimum globalnego pomiaru wynosi TV_Hel=b/2. Kod odtwarza D z OBU niezależnych wzorów, jego widmo i normę śladową w arytmetyce dokładnej.

**Nowa klasa C_1→23:** Alice wykonuje dowolną ogólną lokalną operację pomiarową, ogłasza jej wynik klasyczny, a następnie jej kubit nie jest ponownie używany kwantowo. Bob i Charlie mogą WSPÓLNIE (w jednej abstrakcyjnej koalicji) zastosować dowolny optymalny POVM na swoich dwóch kubitach zależny od wiadomości Alice; dopuszcza się ich wspólny pomiar kwantowy, co jest silniejsze od faktycznego protokołu tylko-LOCC między nimi. Alice może użyć dowolnego POVM, dowolnych lokalnych ancilli niepowiązanych splątaniem, dowolnej liczby etykiet pomiarowych (także rozkładu ciągłego). Z racji symetrii trzech qubitów identyczne ograniczenie dotyczy dowolnego pierwszego laboratorium. Nie dopuszcza się wieloturowego powrotu Alicji do pomiarów.

## 2. Dokładna redukcja pierwszego pomiaru do dysku Blocha

Każdy lokalny efekt E≥0 na qubicie Alice można spektralnie rozłożyć na efekty rzędu jeden; ujawnienie etykiety rozdrobnienia nie może zaszkodzić późniejszemu testowi BC (własność trójkąta normy śladowej). Zatem wystarcza dowolna rodzina

    E_k=t_k |r_k><r_k|,
    t_k≥0, ‖r_k‖₂=1,
    Σ_k t_k=2, Σ_k t_k r_k=0.

Zdefiniuj λ_k=t_k/2, czyli Σλ_k=1 i Σλ_k r_k=0. Zależne od wyniku k warunkowe **nieunormowane** różnice stanów BC są

    D_k = Tr_A[(E_k⊗I_4)D] = t_k b T_x(r_k),

przy czym w bazie Pauli BC

    T_x(r) = [X_BX_C+Y_BY_C +r_x(X_B+X_C)+r_y(Y_B+Y_C)]/16
      + x[r_x(3X_BX_C+Y_BY_C)+r_y(X_BY_C+Y_BX_C)]/32.

Wskaźnik r_z nie występuje. Operator T_x(r) jest Hermitowski i liniowo zależy od r_x,r_y, a dla ustalonego r również od x. Po ogłoszeniu k Bob i Charlie wybierają najlepszy binarny pomiar stanu podpisanego D_k. Ponieważ ΣTr(D_k)=TrD=0, poprawnie znormalizowana globalna odległość wynikowych rozkładów dla danej procedury wynosi dokładnie

    TV(A→BC;{E_k})= (1/2)Σ_k ‖D_k‖₁
                    = b Σ_k λ_k ‖T_x(r_k)‖₁.

Kluczowe: nie wstawiam tutaj samego ‖Tr_A D‖₁ ani nie utożsamiam dwóch zbiorczych efektów z drobnoziarnistymi liśćmi LOCC.

## 3. Lemat ROT006.1 — weryfikowalna globalna majoranta afiniczna

**Lemat.** Dla każdej rzeczywistej pary (r_x,r_y) w dysku jednostkowym i każdego x∈[7/10,3/4] zachodzi

    ‖T_x(r)‖₁ ≤ 12/25 + (11/100)r_x.                     (6.1)

**Dowód.** Dysk jednostkowy jest zawarty w wypukłym, ośmiowierzchołkowym zbiorze

    O = {|r_x|≤1, |r_y|≤1, |r_x|+|r_y|≤17/12},

ponieważ |r_x|+|r_y|≤√2≤17/12 (nierówność sprawdzona dokładnie po podniesieniu stron dodatnich do kwadratu). Wierzchołki O to (±1,±5/12) i (±5/12,±1). Dla każdego ustalonego x funkcja

    f_x(r)=‖T_x(r)‖₁−(11/100)r_x

jest wypukła, gdyż norma śladowa macierzy afinicznej jest wypukła. Jej maksimum na O jest zatem osiągane w jednym z wymienionych ośmiu wierzchołków. Ponadto T_x(r) zależy afinicznie od x, więc przy każdym wierzchołku f_x(r) jest wypukła również względem x: maksima na [7/10,3/4] kontrolują obie jego końcówki. Wystarczy 16 testów.

**Dokładny certyfikat, bez arytmetyki zmiennoprzecinkowej w dowodzie:** dla każdego z 16 parametrycznych operatorów Hermitowskich 4×4 o współczynnikach w Q[i] zbudowano wielomian charakterystyczny w Q[z]. Wszystkie cztery rzeczywiste pierwiastki, z krotnościami, izolowano przedziałami o dokładnych wymiernych końcach i szerokości ≤10^-7. Suma największych modułów końców przedziałów jest wymierną górną granicą ‖T_x(r)‖₁. Maksymalna górna granica f_x spośród wszystkich przypadków jest dokładnie

    244884636201 / 513477478400 = 0.4769140741363429...,

co jest ściśle mniejsze od 12/25=0.48. Wszystkie 16 nierówności sprawdza skrypt z SymPy 1.14.0; same porównania są wymierne. Dowodzi to (6.1) na całym dysku i całym przedziale x. QED.

## 4. Twierdzenie ROT006.2 — dodatnia luka dla C_1→23

**Twierdzenie.** Przy kontrakcie z §1, dla x=e^-q∈[7/10,3/4], dowolnej liczby etykiet POVM Alice oraz dowolnego wspólnego odczytu BC po pomiarze Alice,

    TV_{C_1→23}(q) ≤ (12/25)(1−e^(−2q)),
    TV_Hel(q)−TV_{C_1→23}(q) ≥ (1−e^(−2q))/50 >0.     (6.2)

**Dowód.** Wstaw (6.1) do wzoru z §2. Barycentryczny warunek kompletności Alice zapewnia Σ_kλ_k r_{kx}=0. Dlatego

    TV≤b Σ_k λ_k[(12/25)+(11/100)r_{kx}]
       =(12/25)b.

Z R04/R12 TV_Hel=b/2, więc luka jest co najmniej (1/2−12/25)b=b/50>0. Dla POVM z ciągłym alfabetem ten sam dowód działa po zastąpieniu sum przez całki względem miary pozytywnej, z zerowym barycentrum Blocha. Symetria D pod permutacjami trzech miejsc umożliwia dowolny wybór pierwszego laboratorium. QED.

**Przypadek q=1/3:** x=e^(-1/3)≈0.7165313105737893 należy do [0.7,0.75]. Zatem:

    TV_Hel ≈0.243291440483704,
    TV_{C_1→23} ≤0.233559782864356,
    delta_{C_1→23} ≥0.009731657619348.

Jako dolny świadek osiągalności wewnątrz tej klasy R08 daje TV≈0.198464903476238 (Alice X → Bob X/Y → Charlie lokalny Helstrom). Zatem dla q=1/3:

    0.198464903476238 ≤ sup_{C_1→23} TV ≤ 0.233559782864356.

Nie twierdzimy, że którakolwiek z tych granic jest ostra. Dla x=7/10 luka ≥51/5000=0.0102, dla x=3/4 ≥7/800=0.00875 (wszystko dokładnie wymierne).

## 5. Falsyfikatory / antysamopotwierdzanie / granice

1. **NIE FULL LOCC.** Protokół Alice→Bob→Alice→Charlie z ponownym udziałem kwantowym Alice nie należy do C_1→23. Nie wolno przenosić (6.2) na wszystkie protokoły skończone ani na domknięcie asymptotyczne. R09 pełna luka nadal otwarta.
2. **NIE SEP.** R05/R11/R12 dają drobnoziarniste SEP-POVM osiągające dokładnie Helstroma. W tej pracy nie orzekamy implementowalności tego POVM za pomocą protokołu z §1; zresztą (6.2) wyklucza ją dla q z badanego zakresu.
3. **NIE OGÓLNE Q.** D(q) ma formę R04 wyłącznie dla 3 równych idealnych ekspozycji SWAP i κ=0. Nie wnioskujemy o skończonych bramkach, rozpadzie pamięci, innych źródłach, niejednakowych odstępach ani pełnej normie tensora procesu.
4. **Brak współdzielonego splątania/komunikacji kwantowej.** Gdy Alice może przesłać swój qubit do BC lub użyć zasobów teleportacyjnych, twierdzenie nie obowiązuje.
5. **Zakres x.** Majoranta (6.1) została certyfikowana tylko na [7/10,3/4]; poza nim status UNKNOWN. Nie jest to globalny wynik dla wszystkich q>0.
6. **Nie nowość i nie fizyka.** Brak danych urządzenia, niezależnej recenzji, claimu oryginalności, przyjęcia do BW/LT i prawdziwych sensorów.
7. **Falsyfikator kodu.** Wystarczy jeden punkt (x,r) w dopuszczalnym regionie naruszający (6.1), błąd w reprodukcji 8×8 D lub w tożsamości śladowej na BC, aby odrzucić certyfikat. Wskazane przypadki przetestowano wymiernie i niezależnie numerycznie.

## 6. Reprodukcja, środowisko, ścieżki

- `rot006_exact.py`: Python 3 + SymPy 1.14.0; dokładna arytmetyka Q[i], izolacja 16 zestawów pierwiastków charakterystycznych, globalna nierówność wymierna, niezależne 8×8 odtworzenie D oraz spektrum. Wynik: `EXACT_RATIONAL_ALL_16_CERTIFIED: PASS` i `INDEPENDENT_8X8_SOURCE_D_AND_PAULI_EXPANSION: PASS`.
- `rot006_independent_audit.py`: Python 3 + NumPy 2.3.5; niezależne źródłowe 8×8, kwantowy ślad częściowy, 2500 losowych projektorów i 2500 losowych rodzin lokalnych POVM na każde z x∈{.7,e^-1/3,.75}; nie wykryto naruszeń, R08 witness odtworzony. **Sampling jest wyłącznie diagnostyczny i nie dowodzi twierdzenia**.
- `rot006_exact_stdout.txt` i `rot006_independent_stdout.txt`: bezpośrednie logi wykonania; manifest JSON odróżnia proof checks od numerycznych fixtures. Katalog/pakiet źródłowy archiwizuje komplet bajtów i sum SHA256.

**Science route:** rezultat jest publiczny i przeznaczony do `research/prf13/2026-11-11/`, lecz dopiero potwierdzony zapis GitHub i BW-qualifier uprawniają do statusu ingest/receipt. Referee: najlepiej AUD1 / REC11, niezależny krytyczny test definicji C_1→23 i wzoru na TV. Jeśli GitHub writeback nie jest możliwy, lokalny pakiet to `SOURCE_NOT_DELIVERED`, nie publikacja.

**RETURN:** PRF13_ROT006 / EXACT_RATIONAL_OCTAGON_CHARPOLY_INTERVAL_CERTIFICATE / THREE_Q_END_STATE_A_TO_BC_ONE_WAY_CUT_STRICT_GAP_FOR_X_IN_7_10_TO_3_4 / NONREVISITING_FIRST_PARTY_ONLY / WITNESS_R08_RETAINED / FULL_LOCC_CLOSURE_OPEN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / REFEREE_PENDING.
