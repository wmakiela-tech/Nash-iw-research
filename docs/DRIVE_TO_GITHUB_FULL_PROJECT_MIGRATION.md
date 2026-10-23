# NASH/IW — Drive → GitHub: migracja całego archiwum projektu

## DECYZJA MODERATORA — NASH-PRIV KANONICZNE (2026-10-23)

**Nadrzędna aktualizacja:** Moderator wybrał `wmakiela-tech/Nash-Priv` na **kanoniczny** prywatny cel pełnego archiwum NASH/IW. `Nash-prv` pozostaje niekanoniczne, a wspomnienia o nieistniejącym `Nash-iw-private`, `PRIVATE_REPO_NOT_CONNECTED` i `CANONICAL_PRIVATE_ARCHIVE_UNDECIDED` niżej są wyłącznie historycznym stanem wcześniejszego audytu.

Pełny public-safe status i obowiązujące bramki: [decyzja docelowego archiwum](CANONICAL_PRIVATE_ARCHIVE_DECISION_20261023.md). Zapis decyzji i source-byte pilot znajdują się w prywatnym `Nash-Priv` z pełnym readbackiem.

**Aktualizacja BW:** wcześniejsza 12-event luka XSC po ING-0037 została zamknięta przez KN11. Przy aktualniejszym sprawdzeniu były już `REGISTRY ING-20261023-0137 / XSC-0320`; to nadal stan `AS_OF`, wymagający ponownego live read. BW funkcjonuje na Google Sheets. Repo wybrane ≠ arkusz przeniesiony ≠ zgodność zachowania backendu wykazana.

**Dalsze HOLD:** pełna migracja, usuwanie Drive, zmiana backendu BW, brak niezależnej kopii — wszystko wymaga odrębnych dowodów i warunków opisanych niżej. Oryginałów Drive nie usuwać.

---


## AKTUALIZACJA DOCELOWEGO GITHUB PRIVATE — 2026-10-23

**Nowy stan z bezpośredniego odczytu GitHub (pierwszeństwo nad sekcją 7 i pierwotnym statusem):** integracja obsługuje dwa repozytoria **PRIVATE** `wmakiela-tech/Nash-Priv` (niepuste; trwałe pakiety sukcesyjne) i `wmakiela-tech/Nash-prv` (puste) oraz publiczne `wmakiela-tech/Nash-iw-research`. Użytkownik ma `admin/push/pull` do obu PRIVATE. Wymyślona wcześniej nazwa `wmakiela-tech/Nash-iw-private` **nie istnieje** w podłączonym zbiorze i nie jest wymagana. `Nash-Priv` jest sprawdzonym prywatnym nośnikiem sukcesyjnym, co **nie** oznacza automatycznego wyboru kanonicznego docelowego repo dla BW i całego archiwum.

Status: `PRIVATE_REPO_CONNECTION_VERIFIED / CANONICAL_PRIVATE_ARCHIVE_UNDECIDED / MASS_MIGRATION_NOT_EXECUTED / DRIVE_ORIGINALS_RETAINED`. Żaden proces nie może traktować tego faktu jako uprawnienia do publicznego fallbacku ani destrukcyjnego usuwania z Drive.

**BW live różni się od historycznych punktów głowicy:** `REGISTRY` `ING-20261023-0037` wiersz1448 `COMMITTED/PASS`, `CROSS_SURFACE_CUSTODY` ostatnie `XSC-0210` wiersz211 do `ING-0025`, a skumulowany README tylko `ING-0025` / row1436. Dwanaście najnowszych pełnych zdarzeń REGISTRY `ING-0026..0037` nie ma potwierdzonej następnej mapy XSC. Jest to `SOURCE_CUSTODY_CURRENTNESS_RECONCILIATION_REQUIRED`, a nie dowód utraty science, nowatorstwa czy przyjęcia. SYSS nie zastępuje KN/BW w właścicielskiej semantycznej kwalifikacji.

**Brama wykonania:** przed dużym przenoszeniem prywatnego korpusu należy ustalić właścicielski kanoniczny private target oraz mechanizm działającego BW; test sukcesji już potwierdził odczyt/zapis prywatnego Git, nie migrację źródeł i danych. Stare opisy `PRIVATE_REPO_NOT_CONNECTED` niżej stanowią historyczny stan pierwszego audytu, nie obecne twierdzenie.

---


**Decyzja Moderatora:** 2026-10-22 — przenieść projekt NASH/IW z przeciążonego Google Drive na GitHub.  
**Status wykonania:** `MIGRATION_PREPARED / PRIVATE_REPOSITORY_NOT_YET_CONNECTED / SOURCE_NOT_DELETED`.  
**Właściciel zadania systemowego:** SYSS / opiekunowie architektury archiwum; kwalifikację naukową nadal kontroluje BW/KN i odpowiednie komórki.  
**Zakres:** prywatne i publiczne dokumenty NASH/IW, wyniki badań, BW, pakiety sukcesyjne, źródła odzyskane ze Slacka, kod, dane i archiwa. Nie obejmuje przypadkowych plików osobistych ani odrębnej kampanii RPG.

## 1. Warunek bezpieczeństwa: dwa repozytoria, nie jedno publiczne

| Docelowa powierzchnia | Co zawiera |
| --- | --- |
| `wmakiela-tech/Nash-iw-research` — **PUBLIC** / istniejące | Pełne zatwierdzone do upublicznienia teksty naukowe, wyniki negatywne, publiczne recenzje, kod, dane/manifesty reprodukcyjne i publiczne instrukcje `docs/`. Zachowuje istniejącą historię. |
| `wmakiela-tech/Nash-iw-private` — **PRIVATE** / docelowe, wymagane utworzenie i podłączenie | Prywatne wyniki i surowe źródła, robocze monografie i książki, pełne pakiety sukcesyjne, prywatny BW, oryginalne materiały ze Slacka, prywatne dane/kod, wrażliwe oceny/governance i odrębny rejestr migracji. |
| Google Drive — **źródło migracji / późniejszy okres przejściowy** | Wyłącznie dane jeszcze nieskopiowane lub czasowo blokowane; po zweryfikowaniu migracji i odrębnej kopii zapasowej można je zakwalifikować do usuwania. |

**Krytyczne:** istniejące repozytorium publiczne nie może być użyte jako magazyn prywatnych dokumentów, nawet na ukrytej gałęzi, pod nieoczywistą nazwą czy w historii później „usuniętej”. Prywatne repo musi zostać utworzone z widocznością `private`, dostępem ograniczonym do uczestników z rzeczywistą potrzebą i aktywną możliwością zapisu przez GitHub connector. Do chwili jego dostępności żadna prywatna treść nie może być publicznie „migrowana zastępczo”.

## 2. Dokładna struktura nowego repozytorium prywatnego

```text
Nash-iw-private/
  README.md                         # prywatny indeks, źródła i uprawnienia
  registry/
    bw/
      schemas/                       # opis typów, słowników, constraints
      snapshots/YYYY-MM-DD/          # XLSX fidelity backup + CSV/JSON views
      events/YYYY/MM/                # append-only ING events (.jsonl)
      currentness/                   # indeks efektywnego stanu i provenance
      cross-surface/                 # prywatne powiązania i oryginalne Drive IDs
      audit/                         # snapshot counts, collisions and integrity
  science-private/
    front-b-pbh-bbn/<YYYY-MM-DD>/
    h8r-tpe-qrf-combs/<YYYY-MM-DD>/
    edu1-ai-empirical/<YYYY-MM-DD>/
    formal-theory/<YYYY-MM-DD>/
    referee-prior-art/<YYYY-MM-DD>/
  succession/
    <lineage>/<YYYY-MM-DD>/<artifact-id>/
  books/
    living-theory/
    living-book/
    monographs/
  reproduction-private/
    <lineage>/<YYYY-MM-DD>/
  slack-source/
    <lineage>/<YYYY-MM-DD>/<original-message-id>/
  system-private/
  holds/
  migration/
    source-inventory.jsonl           # prywatny; nigdy do publicznego repo
    file-mapping.jsonl               # oryginalny Drive ID → docelowa ścieżka
    integrity-report.json            # liczniki i checksumy po migracji
    exceptions.jsonl                 # BLOCKED / LOST_FORMAT / UNVERIFIED
  .gitattributes                     # LFS tylko dla faktycznych dużych obiektów
```

**Nie twórz osobnego repozytorium dla każdej komórki** ani nie kopiuj tej samej pracy do wielu katalogów. Tożsamość wyznacza `artifact_id`, nie nazwa transportu. Dotychczasowe prywatne Drive foldery mogą być mapowane bezpośrednio: sukcesja → `succession/`; źródła tematyczne → `science-private/`; monografie → `books/`; pakiety ZIP/JSON → `reproduction-private/`; odzyskane wiadomości → `slack-source/`; system → `system-private/`; HOLD → `holds/`.

## 3. Inwentaryzacja przed importem (nie tylko najnowsze 100 plików)

1. Pobierz **wszystkie strony** list plików Google Drive w zidentyfikowanych obszarach NASH/IW, w tym root, uznane foldery operacyjne BW, archiwa lineage i zamrożone pakiety. Nie mieszaj plików Warhammera/osobistych ani nie traktuj jednej strony API jako pełnego korpusu.
2. Zapisz **prywatny** wiersz na każdy oryginalny identyfikator pliku: `drive_id`, `parent_id`, `title`, `mimeType`, `size`, `modifiedTime`, `sharing`, `artifact_id`, `source_revision`, `exposure`, `target_repo`, `target_path`, `export_format`, `migration_status`.
3. Rozpoznaj duplikaty wyłącznie przez tożsamość naukową i wersję, **nie** przez podobny tytuł; oba różne pliki mogą zawierać różną argumentację albo aktualizacje. Nie usuwaj wstecznie historycznych błędów i prób nieudanych.
4. Ustal realne rozmiary i możliwości konwersji, szczególnie dużych ZIP/PDF/wideo, rodzimych Docs/Sheets/Slides, komentarzy i załączników. Narzędzie aktualnie nie udostępnia użytkownikowego `storageQuota`; rzeczywiste zużycie trzeba sprawdzić w `drive.google.com/drive/quota`.

**Wstępny odczyt 2026-10-22:** jedno `NASH/IW` publiczne repozytorium GitHub jest podłączone, rozmiar GitHub API około 1,9 MiB; prywatne nie jest podłączone. Google Drive root zawiera **co najmniej 600** plików dokumentowych, a paginacja nie była zakończona. Próbka 500 pozycji z root wykazała tylko około **4,8 MB metadanych rozmiaru**; bez pełnego `storageQuota` nie ma podstaw, aby uznać ją za główną przyczynę przepełnienia Dysku. Są też już uporządkowane poddrzewa, inne istniejące archiwa i różne źródła prywatne. Żadna z tych liczb nie oznacza pełnej inwentaryzacji.

## 4. Konwersja z zachowaniem znaczenia i metadanych

- **Dokumenty Google:** kanoniczna czytelna wersja `.md` dla wyszukiwania i recenzji; dla tabel, równań, przypisów, ilustracji i układu — dołącz wierne `.docx` lub `.pdf`, gdy Markdown nie jest równoważny. Nie uznawaj ekstrakcji fragmentarycznej za pełną migrację. Zachowaj tytuł, źródłowy `Drive ID` i rozróżnienie edycja vs oryginał w prywatnym manifeście.
- **Arkusz BW:** zachowaj `.xlsx` z formułami/arkuszami jako snapshot **oraz** wersjonowany eksport wartości w `CSV/JSON` i dziennik `ING events` w `JSONL`. Zweryfikuj liczbę wierszy, arkuszy, oryginalne ING i korekty, typy pól, formuły, właścicielską semantykę `COMMITTED/PASS`, `superseded_by`, niezmienniki i mapy `CROSS_SURFACE_CUSTODY`. `XLSX` nie jest automatycznie działającym zastępnikiem Google Sheets. Wymagany osobny proces zapisu/odczytu BW na GitHub oraz kontrola konfliktów.
- **Kod/dane/ZIP:** zachowaj pełne bajty, podpisy i SHA-256; małe teksty jako zwykłe Git; większe binaria do Git LFS, jeśli plan i workflow na to pozwalają. Nie zapisuj obiektu LFS wyłącznie jako lokalnego pointera bez faktycznego uploadu obiektu.
- **Slack:** zachowaj pełny science-bearing body, `channel`, `thread_ts`, `message_ts`, autor-identyfikator, `RETURN_ID` i drogę do BW. Nie zastępuj archiwum jedynie linkiem do Slacka ani nie twórz fikcyjnego `RECEIPT`.
- **Historia wersji Google Docs:** eksport bieżącego pliku nie eksportuje wiernie całej historii edycji. Dla krytycznych dokumentów zachowaj dostępne migawki/rewizje i oddzielny rekord o niewyeksportowanych metadanych; **nie deklaruj** `FULL_HISTORY_TRANSFERRED` bez realnego dowodu.

## 5. Prawidłowy handshake i obowiązek kontroli

Dla każdego docelowego artefaktu:

```text
SOURCE_IDENTIFIED
  -> EXPORT_FULL_BODY
  -> CLASSIFY_PRIVATE_OR_PUBLIC
  -> WRITE_GITHUB_CORRECT_REPO_AND_PATH
  -> READBACK_EXACT_COMMIT/BYTES
  -> MANIFEST_ORIGINAL_ID + SHA256 + TARGET_COMMIT
  -> VERIFY_BW_EVENT + CLAIM_CEILING + SUPERSESSION
  -> MIGRATED_VERIFIED
```

Statusy błędów: `ACCESS_BLOCKED`, `SOURCE_ONLY_SLACK`, `FORMAT_LOSS`, `LFS_OBJECT_MISSING`, `BW_RECONCILIATION_REQUIRED`, `MIGRATION_PARTIAL`, `NOT_YET_EXPORTED`. **W razie błędu pozostaw oryginał, nie raportuj sukcesu i nie obchodź zabezpieczeń.**

### Warunki przed odzyskaniem miejsca na Dysku Google

1. Każdy wskazany do usunięcia element ma status `MIGRATED_VERIFIED` z porównanym hashem albo integralnością semantyczną dokumentu i źródłowym Google ID.
2. W prywatnym repo potwierdzono pełny BW (dane, struktura i działający nowy zapis), aktualne odnośniki innych komórek i zgodność ze stanem naukowym.
3. Osobna niezależna kopia zapasowa istnieje poza jednym repozytorium GitHub (np. lokalny zaszyfrowany backup); sam Git i Git LFS nie zastępują backupu.
4. Ustalono docelowy sposób współpracy i uprawnienia do prywatnego repo; zmiana linków Drive na GitHub nie tworzy nowych zdarzeń naukowych.
5. Dopiero po zaakceptowaniu protokołu migracji można usuwać **wyłącznie jednoznacznie wskazane zweryfikowane oryginały**. Nie używać masowego kosza, `delete_file` ani czyszczenia kosza na zasadzie samego podobieństwa nazw.

## 6. Techniczne ograniczenia GitHub

- GitHub wymusza limit **100 MiB** na pojedynczy zwykły Git blob; większe wymagają Git LFS lub innego prawidłowego obiektu, zależnie od uprawnień i planu.
- GitHub rekomenduje repozytoria o rozsądnym rozmiarze (aktualna rekomendowana górna granica rozmiaru danych Git około **10 GB**). Nie przenoś wielkich binarnych archiwów do zwykłej historii Git.
- Nie da się bezpiecznie utrzymać tajnych danych w publicznym repo przez chwilowe dodanie i późniejsze usunięcie commitu: historia może pozostać pobieralna.
- Zespół potrzebuje dostępu do **prywatnego** repo; GitHub App podłączona wyłącznie do publicznego nie zobaczy tego archiwum.
- Końcową aktualność nauki nadal wyznaczają kwalifikacja i właściciele BW, nie nazwa pliku ani numer commitu.

## 7. Historyczny punkt zatrzymania — 2026-10-22 (superseded by live 2026-10-23 status)

**Nie można rozpocząć bezpiecznej migracji private→private bez dostępnego prywatnego repo.** Podłączona integracja GitHub udostępnia obecnie tylko `wmakiela-tech/Nash-iw-research` (PUBLIC); nie oferuje w tym środowisku akcji tworzenia repozytorium. Wymagany jest repozytorium `wmakiela-tech/Nash-iw-private` utworzone jako `Private` i dodane do uprawnień integracji GitHub. Po tym kroku można wykonywać etapowe, sprawdzane transfery prywatnych źródeł i BW. Do tego czasu archiwum źródłowe pozostaje nienaruszone, z wyraźnym statusem `NOT_YET_MIGRATED`.

**Zasada nadrzędna:** `NO_PUBLIC_FALLBACK_FOR_PRIVATE_CORPUS` / `COPY_VERIFIED_BEFORE_DELETE` / `FORMATTING_LOSS != SUCCESS` / `BW_SNAPSHOT != WORKING_BW_BACKEND`.
