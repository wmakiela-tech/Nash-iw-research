# IW/NASH — obowiązująca mapa zapisu i wyszukiwania dokumentów

**Stan:** DIRECT_MODERATOR_ROUTING / 2026-10-22 / dokument operacyjny, bez zmiany statusu naukowego.  
**Zakres:** wszystkie komórki IW/NASH; nowe wyniki, zmiany wyników, sukcesje i odczyt informacji.  
**Zasada nadrzędna:** najpierw rozpoznaj `artifact_id`, klasę udostępnienia i funkcję materiału, a potem **konkretny katalog**. Nie zapisuj nowych materiałów IW w głównym katalogu My Drive ani nie kończ pracy samą wiadomością w Slacku.

## 1. Zapis: dokładnie gdzie trafia dany materiał

| Co zapisujesz? | Kanoniczne miejsce pełnej treści | Dodatkowy obowiązek |
| --- | --- | --- |
| Publiczny wynik naukowy, twierdzenie warunkowe, kontrprzykład, wynik negatywny, próba falsyfikacji, recenzja naukowa dopuszczona do publikacji | GitHub `research/<lineage>/<YYYY-MM-DD>/<stable-artifact-slug>.md` | BW `REGISTRY` (zdarzenie źródłowe, kwalifikacja) i prywatny `CROSS_SURFACE_CUSTODY` (dokładna ścieżka + commit); Slack `#iw-dispatch` tylko do dostarczenia |
| Publiczny kod, testy, odtwarzalne dane i manifest eksperymentu | GitHub istniejąca właściwa gałąź `runtime/<topic>/`, `tests/` lub powiązany katalog `research/<lineage>/<YYYY-MM-DD>/` | W wyniku naukowym odnośnik do kodu, danych i wersji, albo jawny brak odtwarzalności; BW źródło tego samego artefaktu |
| Aktualne publiczne reguły, protokoły, mapa projektu i dokumentacja systemowa | GitHub `docs/` — aktualizuj **istniejący** dokument właścicielski, zamiast tworzyć konkurencyjny | Odsyłacze w `README.md`/`docs/START_HERE_CURRENT.md` tylko dla istotnych zmian |
| Prywatny pakiet sukcesyjny, rehydratacja, przekazanie komórki | Drive `NASH–IW Shared Research Bridge/04_PRIVATE_PROJECT_DOCUMENTS_CURRENT/01_CELL_SUCCESSION_AND_HANDOFF_PACKETS/` | Stabilny ID pliku, identyfikator następcy i bieżący stan, wskazanie aktualnego pakietu; nie publikuj prywatnych treści w GitHub |
| Prywatny oryginał naukowy, recenzja, tekst nieprzeznaczony do publikacji | Drive `.../04_PRIVATE_PROJECT_DOCUMENTS_CURRENT/02_PRIVATE_SCIENTIFIC_SOURCE_AND_REVIEW/` — **wybierz podfolder tematyczny** poniżej | Zapisz źródłowy ID w BW i podaj, czy pełna treść publiczna jest osobno na GitHub |
| Robocza Żywa Teoria / kolejne szkice LT | Drive `.../03_MONOGRAPHS_AND_LIVING_BOOKS/01_LIVING_THEORY_DRAFTS/` | Status `DRAFT`; wcześniejsze wersje nie stają się „obowiązujące” tylko z powodu nazwy lub daty |
| Żywa Książka / piloty edukacyjne | Drive `.../03_MONOGRAPHS_AND_LIVING_BOOKS/03_LIVING_BOOK_AND_EDUCATION/` | Rozdziel wydanie wewnętrzne i materiał publiczny, gdy ten drugi zostanie dopuszczony |
| Monografia techniczna / plan książki / robocza rozprawa | Drive `.../03_MONOGRAPHS_AND_LIVING_BOOKS/` bezpośrednio | Nie twórz nieistniejącego „02” jako założonej lokalizacji; utworzenie takiego folderu było wcześniej blokowane |
| Prywatne pakiety obliczeń, ZIP, JSON, dane, skrypty oraz potwierdzenia wykonania | Drive `.../04_REPRODUCTION_DATA_CODE_PACKAGES/` | Publiczny odpowiednik kodu/danych, jeśli dopuszczony, należy do GitHub; Drive nie jest jedynym końcowym repozytorium reprodukcji publicznej |
| Pełny oryginał naukowej wiadomości odzyskanej ze Slacka | Drive `.../05_SLACK_SOURCE_RECOVERY/` | Zachowaj ID pracy, źródłowy kanał i timestamp, pełny tekst, readback; link w BW; sam Slack nie zastępuje kopii |
| Prywatny systemowy dokument wykonawczy, wewnętrzny audyt uprawnień i governance | Drive `.../06_SYSTEM_OPERATIONS_AND_GOVERNANCE/` | Publiczne reguły aktualizuj równolegle **we właściwym istniejącym** `docs/`, bez udostępniania prywatnych lokalizatorów |
| Materiał bez rozpoznanego celu, źródła lub klasy dostępu | Drive `.../00_TRIAGE_NEW_AND_UNCLASSIFIED/` | Wpisz powód `UNCLASSIFIED`; to bufor, nie pełnoprawny rejestr naukowy |
| Pusta kopia ratunkowa, zablokowany zapis, niezgodna lub podejrzana treść | Drive `.../99_BLOCKED_HOLD_AND_EXCEPTION/` lub pozostawienie oryginału na miejscu, gdy przeniesienie zablokowane | Zapisz `HOLD`, przyczynę i istniejące źródło; **nie obchodź zabezpieczeń** i nie oznaczaj pustej kopii jako odzyskanej |

**Skrót `...` w tabeli** oznacza dokładnie `NASH–IW Shared Research Bridge/04_PRIVATE_PROJECT_DOCUMENTS_CURRENT`. Wszystkie nazwy w tabeli odpowiadają istniejącym, zweryfikowanym folderom. Stary katalog `02_IW_BW_SCIENTIFIC_KNOWLEDGE_BASE_LIVE` i właściwy prywatny skoroszyt BW pozostają na miejscu: nie kopiuj ani nie przenoś BW tylko dla estetyki. Starsze zatwierdzone archiwa, zamrożone kampanie i katalogi właścicieli również pozostają tam, gdzie są.

### 1a. Dokładna podścieżka prywatnego źródła naukowego

Po `02_PRIVATE_SCIENTIFIC_SOURCE_AND_REVIEW/` wybierz **jedną**:

- `01_FRONT_B_PBH_BBN/` — Front B, Wu–Xu, PBH/BBN, kanały fizyczne, residual/source errors.
- `02_H8R_TPE_QRF_AND_COMBS/` — H8R, TPE, QRF, struktury comb, identyfikowalność i przenoszenie celu w tym programie.
- `03_EDU1_AI_AND_EMPIRICAL/` — EDU1, hipotezy dark sector, empiryczne/AI, eksperymenty związane z EDU1.
- `04_OTHER_FORMAL_THEORY_AND_MECHANISMS/` — odrębna teoria formalna, mechanizmy lub matematyka niesprowadzalna do powyższych.
- `05_REFEREE_PRIOR_ART_AND_REVIEWS/` — recenzja, krytyka, niezależny audyt, literatura i prior-art. **Funkcja „recenzja” ma pierwszeństwo przed tematem**, ale metadane powinny wymieniać recenzowany front.

Nie odkładaj nowego, już sklasyfikowanego źródła bezpośrednio w folderze `02`. Nie powielaj go w kilku folderach: użyj BW/odnośnika. `owner/lineage` jest identyfikatorem w tytule/metadanych, nie powodem tworzenia kolejnego zbędnego podfolderu.

## 2. Obowiązkowa procedura w chwili tworzenia i po obrocie

1. **Odszukaj istniejącą tożsamość.** Ustal `artifact_id`/`RETURN_ID`, linię, zakres, wersję i wcześniejszy wpis BW. Rewizja lub nowe miejsce transportu tego samego wyniku nie tworzy automatycznie nowego zdarzenia ING.
2. **Wybierz publikowalność.** `PUBLIC` tylko dla sprawdzonej i dozwolonej pełnej treści; `PRIVATE/RESTRICTED` w Drive; `HOLD` przy prawdziwej blokadzie. Prywatny nośnik źródła nie oznacza automatycznie prywatności jego naukowej treści, ale nie daje też zgody na publikację.
3. **Zapisz do ścieżki z tabeli, nie do My Drive root, Slack ani przypadkowego katalogu ChatGPT.** Zachowaj wszystkie hipotezy, dowody, negatywną wiedzę i granice wniosku. Nie zastępuj pracy samym streszczeniem.
4. **Zweryfikuj odczyt nośnika.** GitHub: dokładna treść i commit; Drive: istniejące ID pliku, właściwy folder, uprawnienia i pełny body readback. Jeśli dostęp blokowany — jawny `PENDING/HOLD`.
5. **Powiąż BW.** Uprawniony właściciel procesu BW rejestruje źródło i kwalifikację w `REGISTRY`, a relację GitHub–Drive w `CROSS_SURFACE_CUSTODY`. Jeśli jeszcze nie zarejestrowano: `GITHUB_PENDING_BW_INGEST` albo `BW_PENDING_GITHUB_PUBLICATION`; brak fikcyjnego `SYNCED`.
6. **Wyślij do właściwego kanału Slack.** Formalny zwrot do `#iw-dispatch`, pilny problem do `#iw-alerts`, dialog do `#iw-live-dialogue`; niezależny `#iw-nc-inbound` pozostaje prywatny. `#iw-start-here` służy wyłącznie nawigacji, a nie wynikom.
7. **Raportuj tylko wynik materialny.** Minimalne potwierdzenie: `artifact_id | exposure | canonical_body_path | source_revision/commit | bw_event_or_pending | claim_ceiling | HOLD`. Nie uruchamiaj osobnego biurokratycznego obrotu wyłącznie w celu zameldowania o zwykłym zapisie.

**Nie wymagamy fizycznej kopii każdej nauki jednocześnie w GitHub i Drive.** Wymagamy pełnego publicznego tekstu w GitHub *dla nauki dopuszczonej do publikacji* oraz odpowiednich prywatnych źródeł/proweniencji i wiązań w BW.

## 3. Procedura wyszukiwania — nie zaczynaj od listy plików

| Pytanie badacza | Pierwsze miejsce sprawdzenia | Następny krok |
| --- | --- | --- |
| „Jaki jest aktualny status/kwalifikacja tej tezy?” | BW — aktualny widok owner-currentness i źródłowe `REGISTRY`, nie sam manifest publiczny | Z `artifact_id` przejdź do właściwego `CROSS_SURFACE_CUSTODY`; sprawdź korekty/supersession |
| „Gdzie jest pełna publiczna praca, twierdzenie, kod?” | BW/XSC lub publiczne `research/<lineage>/...` i kod GitHub | Otwórz ścieżkę i zweryfikowany commit, porównaj z BW, nie tylko wyszukiwarką Slack |
| „Gdzie są prywatne oryginały, recenzje i pakiety?” | BW prywatny locator po `artifact_id`; w Drive folder wg tabeli i wyszukiwanie tytułu/ID | Skontroluj prawa dostępu i bieżącą wersję; nie wnioskuj o aktualności z samej daty modyfikacji |
| „Jaki pakiet musi przeczytać następca?” | Drive `01_CELL_SUCCESSION_AND_HANDOFF_PACKETS/` lub istniejący folder lineage, a także aktualna orientacja właściciela | Ustal obowiązującą wersję pakietu i jego jawne supersession; nie wybieraj ślepo ostatniego alfabetycznie |
| „Gdzie był przekaz, decyzja, odpowiedź?” | Slack `#iw-dispatch` i oryginalny `thread_ts/RETURN_ID` | Sprawdź czy body faktycznie zapisano i przyjęto w BW; `#iw-alerts` tylko do blokad |
| „W Drive nie ma pełnej treści, ale widzę Slack?” | Oryginalny Slack timestamp + BW ING/XSC i rejestr `HOLD` | To **nie** dowodzi braku nauki; źródło może istnieć wyłącznie w Slacku. Nie oznaczaj pustego pliku jako recoverable |

Kolejność wyszukiwania: **`artifact_id` → BW/owner-currentness → kanoniczny body (GitHub/Drive) → commit/readback → oryginalny wątek Slack**. Dla systemowych polityk pierwszym źródłem aktualnej normy jest odpowiednie `docs/`, nie zdublowany historyczny pakiet.

## 4. Wzory adresowania i rozróżnienia

```text
PUBLIC_SCIENCE  -> GitHub: research/<lineage>/<YYYY-MM-DD>/<stable-artifact-slug>.md
PRIVATE_RETURN  -> Drive: .../02_PRIVATE_SCIENTIFIC_SOURCE_AND_REVIEW/<topic-folder>/
PRIVATE_PACKETS -> Drive: .../01_CELL_SUCCESSION_AND_HANDOFF_PACKETS/
LIVING_THEORY  -> Drive: .../03_MONOGRAPHS_AND_LIVING_BOOKS/01_LIVING_THEORY_DRAFTS/
LIVING_BOOK    -> Drive: .../03_MONOGRAPHS_AND_LIVING_BOOKS/03_LIVING_BOOK_AND_EDUCATION/
REPRO_PRIVATE  -> Drive: .../04_REPRODUCTION_DATA_CODE_PACKAGES/
SLACK_RECOVERY -> Drive: .../05_SLACK_SOURCE_RECOVERY/
HOLD           -> Drive: .../99_BLOCKED_HOLD_AND_EXCEPTION/ [jeśli dozwolone]
BW             -> existing operating spreadsheet: REGISTRY + CROSS_SURFACE_CUSTODY
DISPATCH       -> Slack: #iw-dispatch; NAVIGATION -> #iw-start-here
```

**Minimalne metadane:** `artifact_id`, `origin_cell`, `created_at`, `document_type`, `exposure`, `claim_ceiling`, `bw_ingestion_event_id` lub jawne `pending`, `canonical_path`, `source_revision`, `supersedes/superseded_by` gdy dotyczy. `CANON` ani `EXEC_SIGN` nie wynika ze ścieżki, nazwy, ingestu czy commitu.

## 5. Utrzymanie porządku — jeden właściciel miejsca zapisu

- Każdy autor/komórka **sama zapisuje materiał we właściwym folderze** podczas normalnego obrotu; SYSS nie musi ręcznie przenosić każdej nowej pracy.
- Właściciel BW/KN utrzymuje zdarzenia źródłowe i relacje; nie przenoś skoroszytu BW do nowego „ładniejszego” drzewa.
- Komórki systemowe korygują reguły w istniejących kanonicznych plikach `docs/`; aktualizacja samej wiadomości Slack lub prywatnego pakietu nie zmienia publicznej normy.
- Każdy uczestnik czyta tę mapę podczas orientacji i przed pierwszym materialnym zapisem po sukcesji. Nie wymaga to zimnego odtwarzania całej historii.
- Jeśli katalog nie pasuje, oznacz `TRIAGE/HOLD` i podaj uzasadnienie, a nie twórz automatycznie nową gałąź folderów.

**Granice:** `FOLDER != SCIENCE_CURRENTNESS`; `PUBLICATION != SCIENCE_ACCEPTANCE`; `STORAGE != DELIVERY != RECEIPT != BW_COMMIT`; `PRIVATE_URL != PUBLIC_GITHUB_METADATA`.
