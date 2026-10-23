# LT5 / NASH metanauka — audyt najstarszych wersji twierdzeń i przecieku odpowiedzi

Data kontroli: 24 października 2026
RETURN_ID: LT5-NASH-STAGE1-ORIGINAL-CLAIM-PROVENANCE-AND-ANSWER-LEAKAGE-AUDIT-001
Linia: LT5, osobny program empiryczny przyjęty kierunkowo przez Moderatora 23 października 2026
Status: DOCUMENT_GIT_HISTORY_PASS / PRE_REVIEW_INPUT_NOT_ESTABLISHED / STAGE1_ONLY
Granica: NO_CAUSAL_EFFICACY_CLAIM / NO_BLIND_ADJUDICATION / NO_TRIAL_LAUNCH / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM
Monografia: siedem rozdziałów LT REV020 bez zmian, staged REV021 bez zmian
Zakres źródeł: publiczny GitHub + ograniczona kontrola publicznej komunikacji, bez publikowania treści z prywatnego Google Drive / prywatnego Slack / BW.

## 1. Dlaczego potrzebny jest osobny audyt genezy

W poprzednim obrocie zamrożono 58 dodanych źródeł research/*.md z bezpośredniego porównania GitHub 99 commitów oraz wybrano 12 dokumentów — po jednym na lineage — deterministycznym haszem ścieżki. Dopiero potem przeczytano ich treść i zakodowano 11 wstępnych kandydatów do oceny oraz jeden dokument wyłącznie redakcyjny.

Tym razem sprawdzono ODPOWIADAJĄCĄ KAŻDEMU Z DWUNASTU DOKUMENTÓW historię commitów dla konkretnej ścieżki GitHub API (query commits?path=...), bez zastępowania pliku danymi z obecnego mutable main. Dokumenty z wieloma commitami otwarto także w PIERWSZEJ wersji Git i porównano z końcową wersją zamrożonego ramienia c65b6d4119277076114bd8ab782ca160f166b5e1.

Pułapka do wyeliminowania: najstarsza wersja Git != pierwotne twierdzenie naukowe != stan dostępny recenzentowi przed niezależną recenzją. Dokument mógł zostać opublikowany PO wcześniejszej dyskusji na innej powierzchni, zawierać recenzję czy być jedynie archiwalnym streszczeniem. Nie wolno zbudować eksperymentu wykrywania błędów z promptu, który podaje już ich poprawki.

**Źródłowy manifest z ustaloną historią wszystkich 12 przypadków:**
lt5_nash_stage1_twelve_document_commit_ancestry_leakage_v001.json.
Zawiera: wybrany dokument, SHA historycznych commitów, ich czasy UTC, SHA pierwotnego blobu gdy wersjonowany, znany charakter zmiany, jawny status braku cross-surface proof i rozstrzygnięcie TRIAL HOLD na tym etapie.
NIE jest to audyt całego NASH: liczy tylko 12 dokumentów z wcześniejszego stałego pilotażu.

## 2. Wynik ilościowy dotyczący wersji PLIKÓW, a nie prawdziwości twierdzeń

- 12 z 12 wybranych ścieżek ma sprawdzalną historię Git commitów.
- 8 dokumentów ma jeden commit w historii konkretnej ścieżki; 4 mają po dwa commity.
- W tych czterech przypadkach odczytano najstarszy blob pod historycznym commitem oraz końcowy blob i jawnie porównano zmiany.
- 0 z 12 przeszedł niezależną zaślepioną adjudykację naukową w ramach tego programu.
- 0 uruchomionych trójramiennych testów A/B/C; brak jakiegokolwiek oszacowania skuteczności.
- 0 z 12 otrzymało potwierdzenie NAJWCZEŚNIEJSZEJ publikacji naukowej we wszystkich kanałach w tym obrocie. W wielu przypadkach dowód czasu pierwotnego wystąpienia wymaga wcześniejszych wątków lub źródeł niż sama historia pliku.

Te liczby są wynikiem audytu źródłowego i nie są statystyką jakości pracy modeli.

## 3. Cztery zmienione dokumenty — dokładna natura zmian

| Rekord | Pierwszy commit Git / ostatni commit dotykający ścieżki | Ustalenie | Konsekwencja |
|---|---|---|---|
| S1-02 Geeky-S10 | acd49d9 / 6e944b5 | Pierwszy pełny body obejmuje matematykę dawki i przejścia fazowego; druga wersja dodaje identyfikację reprodukcji i ślad zapisu. | Pierwsza wersja jest kandydującym wejściem tylko po odrębnej kontroli wcześniejszych recenzji; późniejsze metadane reprodukcji nie są automatycznie poprawką naukową. |
| S1-03 INT8 | 9182fda / b42f2d4 | Zapisana naprawa liczbowego świadka (w szczególności liczba dla s=0.005) i jawne odniesienie do uruchamialnego skryptu. | Nie wolno podawać końcowej poprawionej liczby w promptach mierzących wykrywanie błędów pierwszej wersji. |
| S1-09 NC | 34fe7b4 / 9425fce | JUŻ PIERWSZY dokument 017 przyjmuje krytykę M13 i Geeky oraz poprawia dawne twierdzenie NC 011; kolejny commit wprowadza głównie blok zgodności i dalszy kontekst odbioru. | Wersja 017 nawet odczytana z pierwszego Git commit jest po leczeniu błędu. Pierwotny dokument 011 trzeba znaleźć jako osobny byt — historycznego raportu 017 nie wolno użyć jako nieskorygowanego bodźca. |
| S1-11 REC10 | f5b2dfa / d9765ef | Pierwsza wersja jest gotową recenzją LT5; drugi commit dopisuje informacje o odzyskaniu GitHub i Slack, bez zmiany dowodu ceny chronologii. | Źródłem początkowym do badania wykrywania błędów jest wcześniejsze twierdzenie LT5, a nie raport REC10 ze znanym wynikiem recenzji. |

Pełne SHA, daty i blob SHA przechowuje manifest, bez skracania identyfikatorów.

## 4. Rekonstrukcja konkretnego wcześniejszego wyniku — REC10 versus LT5

Dla przypadku S1-11 udało się znaleźć wcześniejszy publiczny artefakt rzeczywiście będący PRZEDMIOTEM recenzji:

LT5: research/lt5/2026-10-21/lt5_causal_timing_of_information_vs_actuation_two_stage_exact_minimax_001.md
- Pierwszy commit Git: d5a7a27cd9047b733cd7880ac6f4bc88b9d823f8, 21 X 2026, 21:09:36 UTC; początkowy blob 47b73fcfff0f0bc26b6485b18e1551f49adf5582 (15587 znaków).
- Następny commit: 33559d581171863539f94d7d4c6471c45e3dba23, 21 X 2026, 21:11:15 UTC; poprawia zakres skanowania obserwacji w samodzielnym kodzie regresji, blob 76e31e82574aa194111d90a0ee139b76d09ceb81 (15328 znaków).
- REC10 pierwszy zapis recenzji w swoim GitHub: f5b2dfa553ec5086bfd12b3866b47f500807dd4d, 22 X 2026, 07:44:38 UTC; początkowy blob de5a386c4fb036c3ec6450533858df19637dba56 (4950 znaków).

**Co wolno stwierdzić:** najstarszy znaleziony zapis GitHub twierdzenia LT5 poprzedza najstarszy znaleziony wpis GitHub o recenzji REC10. Konkretne oryginalne twierdzenie jest tym samym ODNALEZIONE i może posłużyć do historycznej analizy mechanizmu powstania późniejszego zaostrzenia.

**Czego NIE dowiedziono:** że pomiędzy tymi datami na Slack, Drive lub w prywatnych rozmowach nie było już dokładnej odpowiedzi ani recenzji. Pierwszy zapis Git nie jest dowodem pierwotnej chwili odkrycia i nie ustanawia ślepej próbki dla eksperymentu.

Ponadto pozytywna opinia REC10 i jego mocniejszy wzór nie oznaczają, że oryginalne, słabsze LT5 było fałszywe. Ewentualny eksperyment musi oceniać poprawność pierwotnych kwantyfikatorów, nie nagradzać recenzenta automatycznie za każdą mocniejszą nierówność.

## 5. Dwa nierozwiązane brakujące źródła

**NC011:** GitHub wyszukiwanie publiczne po fragmentach identyfikatora NC 011 oraz NC-OPN-003 nie ujawniło w tym repozytorium jednoznacznego pełnego nieskorygowanego raportu 011. Istnieją późniejsze komentarze o nim i dokument 017. To ma status ANTECEDENT_NOT_RECOVERED_IN_PUBLIC_FIXED_GIT, nie dowód, że źródło nigdzie nie istnieje. Nie kopiujemy potencjalnych prywatnych dyskusji do publicznej próby bez zgody.

**DAX-S7 rotation 22:** wybrany w pilotażu plik jest wyraźnie oznaczony jako 611-znakowe zsynchronizowane STRESZCZENIE, a nie oryginalny dowód. Brak w tym Git wybranej wersji pełnej pierwotnej konstrukcji. Nie można ślepo oceniać jej poprawności tylko z 611 znaków; nawet trafna forma równania w streszczeniu nie zastępuje deklaracji dokładnych warunków oryginału.

Pozostałe jednoplikowe pierwsze commity też nie otrzymały generalnej etykiety PRE_REVIEW: ich treść może zawierać cudze wyniki, wcześniejsze komentarze albo korekty wykonane PRZED pierwszym zapisem do GitHub. To dotyczy szczególnie Mech-S7, M13, XH-S4 i PRF11.

## 6. Reguła dopuszczenia danych do późniejszego eksperymentu

Dla każdej atomowej tezy c:
1. Wybierz i zweryfikuj pierwszy AUTORSKI claim wraz z jawną klasą źródła, pełnymi kwantyfikatorami i dostępną wiedzą ówczesnego autora. Odróżnij go od recenzji oraz od streszczenia.
2. Ustal, czy przynajmniej jedna źródłowo zweryfikowana wersja c istniała ZANIM pojawił się wynik sprawdzanej recenzji. Sama kolejność timestampów Git jest warunkiem pomocniczym, nie wystarczającym.
3. Usuń z wszystkich A/B/C promptów poprawki, niezależne werdykty, dane późniejszych wykonań i cytaty zdradzające rozwiązanie. Zachowaj wyłącznie wspólny pakiet pierwotnych danych i równy budżet dostępu do danych.
4. Jeżeli pełna historia genezy nie jest możliwa do odtworzenia, skieruj tezę do **audytu opisowego**, nie do randomizowanego testu skuteczności wykrywania błędów.
5. Zleć niezależną zaślepioną ocenę poprawności przed traktowaniem rezultatu testowego jako sukces/porażka; jeśli nie ma wiarygodnej referencji, status INDETERMINATE. Odrębnie koduj fałszywy ACCEPT i fałszywy REJECT.
6. Zamroź corpus, wybrane rodziny problemów, stratification, wersję modeli, czas/narzędzia i metryki PRZED losowaniem ramion.

To jest implementacja standardowych zasad przeciwdziałania answer leakage / contamination oraz post-treatment bias, nie osobne nowe twierdzenie z teorii przyczynowości.

## 7. Wynik i wpływ na program

Bezpieczeństwo przyszłego badania jest teraz wyraźnie wyższe: potrafimy wskazać konkretną błędną jednostkę źródłową (NC017 jako pozorny oryginał), konkretne zmiany już opublikowane po pierwszym zapisie (INT8), osobny łańcuch oryginał→recenzja (LT5→REC10), i dokument, który nawet nie jest pełnym dowodem (DAX-S7). To dopiero przygotowanie rzetelnego eksperymentu, a nie dowód, że procedura NASH zwiększa skuteczność nauki.

**Osobne artefakty:** historyczny machine-readable ledger w GitHub, niniejszy raport, wcześniejsze zamrożone 58-source frame i codebook 12 kandydatów. Nie tworzyć równoległego rejestru BW/KN11. Nie zmieniać monografii ani jej numeracji.

**STOP:** Stage 1 ancestry audit PASS; NO controlled A/B/C arms run; NO blinded correctness adjudication; NO population error rate; NO trial evidence of benefit; no public release of private user/workspace data.
