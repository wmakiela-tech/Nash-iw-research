---
artifact_id: IW_GEEKY_S12_ROT012_INDEPENDENT_PYTHON_BERNSTEIN_AND_FRACTION_WITNESS_AUDIT_001_20261112
cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
date: 2026-11-12
exposure: PUBLIC
status: SAME_CELL_INDEPENDENT_CODEPATH_AUTHOR_SELF_AUDIT_PASS / REC11_AUD1_EXTERNAL_REFEREE_PENDING / M14_OWNER_ADOPTION_PENDING
source: M13_N41_FUNCTIONALLY_MATCHED_AUXILIARY_B_FIVE_MASKS_ONE_POSITIVE_GAIN
sync: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT012 — audyt źródłowy innymi implementacjami: 17 testów Bernsteina, 5 powłok, 5 ścisłych porównań wymiernych

## Wynik

ROT011 wykonał bajtowo niezmieniony oryginalny pomocniczy kod M13 i odtworzył źródłowe 25 przedziałów kwartycznych B. ROT012 bada INNY fragment łańcucha: matematyczny certyfikator ROT007, a nie generator wejściowy.

Wykonałem DWIE zupełnie nowe ścieżki obliczeniowe w Pythonie. Żadna nie uruchamia ani nie importuje oryginalnego JavaScript BigInt kodu ROT007. To niezależność kodu w obrębie tej samej komórki, NIE niezależna osobowa recenzja REC11/AUD1.

Ścieżka A: Python3, mpmath.iv 1.3.0, 70 cyfr, nowa rzadka dwuwymiarowa algebra wielomianów (a^i b^j), oddzielne przekształcenia do bazy Bernsteina, źródłowe skierowane granice oryginalnego M13. 17/17 ścisłych znaków dodatnich oraz 5/5 ścisłych dodatniości pięciu powłok: PASS. Zachowano dokładnie wszystkie źródłowe regiony i kwantyfikatory ROT007.

Ścieżka B: Python3 stdlib fractions.Fraction, oddzielna klasa skierowanego przedziału wymiernego, Horner dla powłok i suma kwadratów wyznaczników Grama. ZERO Float64 w decyzjach znaków, ZERO mpmath i ZERO JS. Pięć ścisłych nierówności świadków dla konkretnego alpha=.03082, delta=.02514: PASS.

Źródło pierwsze M13: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json
Original immutable M13 Git blob SHA1 a6f50fbe5904e580e84c87ee87c5ad043cdec5d0.
Oryginalny dowód Geeky ROT007 FIRST: https://github.com/wmakiela-tech/Nash-iw-research/blob/402ead39de6839ea1db50c0420d6d4f037213b41/research/geeky-s12/2026-11-12/IW_GEEKY_S12_ROT007_M13_B_THREE_CANDIDATE_REDUCTION_AND_NARROW_THRESHOLD_BRACKET_001_20261112.md
Oryginalny BigInt pozytywny certyfikator ROT007: https://github.com/wmakiela-tech/Nash-iw-research/blob/cb939cbd3a939cdbb4633f283b6185d622c80f24/research/geeky-s12/2026-11-12/iw_geeky_s12_rot007_exact_B_uniform_delta_le_0025_rational_bernstein.js

## 17 testów — niezależnie obliczone dolne granice

Wagi powłok dokładnie W=(7778,6938,6146,5402,24389); wszystkie sygnały powłokowe w obliczeniach skaluje się przez 10^12. Z wielomianów stopnia 4 wyznaczono niezależnie parami Q_ij(a,b) jako algebraiczny iloraz antysymetrycznej różnicy przez a-b, R_ij(b) jako s'_i(b)s_j(b)-s_i(b)s'_j(b), następnie P=2 SUM_i<j wi wj Q_ij R_ij. Nie wykorzystano współczynników polinomu P z kodu JS.

Source P, pięć prostokątów (a,b):
- [0,.1] x [.008,.020]: +6817.9921478471815
- [0,.1] x [.020,.105]: +14508.510376279692
- [0,.1] x [.105,.200]: +1317636.7138938764
- [.1,.2] x [.008,.020]: +2776.2777890533757
- [.1,.2] x [.020,.200]: +179369.80345567147

Dodatnie kontrole niewielkiego beta:
- P for a in [0,.028], b in [0,.008]: +310.21019948274386.
- partial_b P for a in [.028,.2], b in [0,.008]: +38348.39646897166.

Osiem segmentów F0(a), delta=.025, a-knots (.028,.03,.032,.033,.035,.04,.05,.1,.2):
+1.0372508111102976; +.7341345112667048; +2.7138745452810373; +7.654278560167522; +32.440423812103816; +269.38736547190854; +2967.9821869606; +1145626.1474003564.

Dwa segmenty P(a,a-.025), a in [.028,.03] and [.03,.033]:
+1687.9594888238569; +3234.134838870772.

Pięć dodatnich dolnych ograniczeń powłok w skali 10^12:
+.009861818352395727; +.013090462972866413; +.018239007511768848; +.024583138646238557; +.033356545541269086.

Wszystkie 22 decyzje znaków używają bezpośrednio skierowanych granic mpmath.iv przy 70 dps. Numery Float64 są wyłącznie zaokrąglonym odczytem wyników. Wszystkie wartości pokrywają się z autorowym kodem ROT007 w granicach zaokrąglenia prezentacyjnego.

Dodatkowy niezależny test obliczył p(a,b), q(b), H=2 p_b q - p q_b osobną ścieżką algebraiczną. Każdy interwał współczynnika wielomianowego H-(a-b)P zawiera zero, z maksymalnym bezwzględnym końcem interwału około 3.621e-26. Ważne: samo zawieranie zera NIE jest dowodem tożsamości symbolicznej; tę zapewnia rachunek wedge quotient podany w ROT007. Wynik tej kontroli jest testem spójności dwóch sposobów wyprowadzenia.

## Wymierny falsyfikator: nie tylko punkt dalszy, lecz brzeg beta=0

Parametry oryginalnego ROT007:
- alpha=1541/50000=.03082
- delta=1257/50000=.02514
- beta*=1/1000000=.000001, legalny dalszy punkt
- betaL=71/12500=.00568, najbliższy lewy
- betaR=1399/25000=.05596, najbliższy prawy.

D^2 z pierwotnych nieskalowanych współczynników pomnożone przez 10^24 (wartości wyświetlane przybliżone):
- beta=0: 0.28632718240805416
- beta*=.000001: 0.28632991635915184
- betaL=.00568: 0.28635263194909905
- betaR=.05596: 0.48950199921011717.

Nowa, oddzielna implementacja wyłącznie w dokładnych Fraction potwierdziła następujące źródłowo wymierne dodatnie D^2 gaps (znowu razy 10^24):
- D^2(betaL)-D^2(beta*) > 0.000022715589947220624
- D^2(betaR)-D^2(beta*) > 0.20317208285096536
- D^2(beta*)-D^2(beta0) > 0.000002733951097639832
- D^2(betaL)-D^2(beta0) > 0.000025449541044860457
- D^2(betaR)-D^2(beta0) > 0.20317481680206298.

Wszystkie NIERÓWNOŚCI ścisłe sprawdzono porównując dokładne ułamki wymierne końców skierowanych przedziałów, nie zaokrąglone wartości. W szczególności beta=0 jest lepszy od obu najbliższych legalnych punktów. W połączeniu z obowiązującą źródłową redukcją ROT007.1 do trzech kandydatów beta={0,a-delta,a+delta} daje to **WARUNKOWO GLOBALNY ARGMIN beta=0** dla tego ustalonego (alpha,delta). To konkretyzuje wcześniejsze ROT007, które poprawnie nie przypisywało globalnej minimalności wewnętrznemu beta*=.000001. Nie jest to nowy uniwersalny dowód formalny ani niezależny werdykt człowieka.

## Reprodukcyjny pakiet lokalny i granice zaufania

Pakiet aktualnej rozmowy: Geeky_S12_ROT012_independent_sign_and_witness_audit.zip,
SHA256 dcf9553a7490054f4e638cd9f78536ef394c6ca6194d7df67715a8028d1ba28c,
13036 bajtów, 9/9 członków SHA256 i porównanie bajtowe PASS, ZIP CRC PASS.

Zawiera rzeczywiście wykonane źródła:
- rot012_independent_mpiv_audit.py SHA256 1996e9dff662e498ff7b2688f953298d7a083a02ec731ab0261a1d28c777fbf9
- rot012_independent_fraction_witness.py SHA256 ead662993d43f259ae577a8770a62edea80f21f6fd99ada60220c16533c00d9b
- original direct_B.json M13, Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0
- rot012_results.json, rot012_exact_witness_results.json, README, logs i manifest SHA256.

Wystarczy uruchomić z katalogu rozpakowania Python3:
python rot012_independent_mpiv_audit.py
python rot012_independent_fraction_witness.py
Pierwszy wymaga mpmath1.3.0, drugi tylko stdlib. Każdy kod odrzuca błędny Git blob źródłowy. Kod w ZIP jest lokalnym artefaktem, nie twierdzimy o publicznej kopii źródeł Python na GitHub.

## Custody i dalsze ograniczenia

As-of 12 listopada późnym wieczorem, brak sprawdzonej autorytatywnej niezależnej recenzji matematycznej REC11/AUD1 ROT007, brak formalnej decyzji adopcyjnej M14 i brak BW ingest KN13. Przegląd KN13 ROT018 klasyfikował ROT007 jako SOURCE READ, NIE jako independent interval referee. Ten ROT012 potwierdza odporność wyników na inne implementacje w tej samej komórce, ale NIE spełnia wymogu niezależności osobowej REC11/AUD1.

Domeną pozostaje M13 pomocnicza rodzina Fourier TT N41 / pięć masek / jedna wspólna dodatnia amplituda energii, NIE byte-missing historic dtc0a_runtime_v0_3_1.py ani fizyczny NASH/J3/K/TPE. Pierwszeństwo generatora i źródła zachowuje M13. ROT012 nie twierdzi o nowości matematycznej, fizycznej, CANON lub EXEC.

STOP dalszych skanów progu delta. NEXT GATE: niezależny referee trójpunktowej redukcji i dowodu źródłowych znaków na oryginalnym source table.

FINAL: 17_INTERVAL_BERNSTEIN_CROSSCODE_PASS / 5_SHELL_POSITIVITY_PASS / 5_FRACTION_STRICT_SIGN_PASS / BETA0_CONDITIONAL_GLOBAL_ARGMIN_AT_FIXED_WITNESS / INDEPENDENT_REFEREE_PENDING / OWNER_PENDING / BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
