# NASH / IW — RAPORT OTWARCIA NOWEGO WĄTKU ARIS
## Pełne przekazanie ciągłości: współpraca, governance, Knowledge OS i program S0
### Wersja 1 — 28 lipca 2026

```yaml
RULE_STAMP:
  cell: "ARIS"
  governing_doc: "NASH_ARIS_KOMORKA_KORZENIOWA_v0_1_1_20260711.md"
  governing_hash: "BRAK_SOURCE_LOCK"
  local_mutations:
    - id: "ARIS_LEAD_ARCHITECT_FOR_IW_KNOWLEDGE_OS"
      authority: "Moderator — explicit approval"
      date: "2026-07-27/28"
  change_mode: "B_EXPLICIT_ROLE / A_VETO_WORKING_DESIGN"
  stamp_date: "2026-07-28"

document_id: "IW_NEW_ARIS_THREAD_OPENING_MASTER_REPORT_v1_20260728"
status: "HANDOVER_MASTER / NOT_CANON / NO_EXEC_SIGN"
prepared_by: "ARIS — outgoing thread"
recipient: "ARIS — successor thread"
purpose: >
  Zachować ciągłość długiego wątku, zwłaszcza nowego kształtu IW jako
  przedsiębiorstwa wiedzy, projektowanej bazy/Knowledge OS, ról uczestników,
  decyzji Moderatora, failure modes, stanu naukowego i pierwszego programu S0.
moderator_action_required: false
```

---

# 0. NAJWAŻNIEJSZY KOMUNIKAT DLA NASTĘPCY

Nie przejmujesz pojedynczego zadania „zbuduj bazę”. Przejmujesz funkcję
**Lead Enterprise and Knowledge Architect** w systemie, który ewoluuje od
współpracy modeli do przedsiębiorstwa produkującego, utrzymującego,
przetwarzającego i udostępniającego wiedzę.

Najbliższy cel jest jednak mały:

> zbudować najmniejszy, zamrożony prototyp wiedzy, który przy zimnym starcie
> dowodzi realnej wartości na trzech przypadkach z historii NASH/IW.

Architektura docelowa ma pozostać mapą kierunku. Nie wolno jej implementować
zanim funkcja ziarna zostanie wykazana.

# 1. SKĄD PRZYCHODZI PROJEKT

## 1.1. Faza współpracy modeli

NASH/IW zaczynał od organizacji wielomodelowej pracy badawczej. Powstały role,
protokoły, statusy, bramki, handoffy, ślepe testy i zasady claim boundaries.

Najważniejsza lekcja: modele mogą wytwarzać wartościowe lokalne wyniki, ale bez
trwałej architektury wiedzy wynik nie staje się wspólną pamięcią systemu.

## 1.2. Faza badań naukowych

Projekt rozwijał Paper 1/1b, J3/K, DTC0a, NCDG, GMACH i liczne misje
literaturowe. Część wczesnych ambicji publikacyjnych została później zdegradowana.
Moderator jasno wskazał, że stare artykuły nie mają obecnie istotnego znaczenia;
nowe powstaną dopiero przy rzeczywistych wynikach.

## 1.3. Faza audytu nowości

Moderator zakwestionował, czy program wnosi nowość. SP i MGPT wykonali prior-art
gates. Część problemów została rozpoznana jako K4 lub zabita jako znane obszary.
Z tego wynikła nadrzędna zasada: literatura przed projektowaniem i przed
inwestowaniem w aparat.

## 1.4. Faza kryzysu pamięci

W lipcu ujawniły się powtarzalne awarie:

- SP odkrył analizę normową, która już istniała;
- rozbieżność operatorów była naprawiona w manifeście v2, lecz v1 nie prowadził do następcy;
- różne `R_F` były mieszane pod wspólnym symbolem;
- katalogi failure modes istniały w wielu komórkach bez wspólnej warstwy;
- dokumenty `FINAL` nie miały wskaźników supersesji.

To doprowadziło do kategorii K5 oraz do uznania, że problemem projektu jest
**NON_CUMULATIVE_KNOWLEDGE_ARCHITECTURE**.

# 2. AKTUALNA WIZJA

IW ma docelowo stać się otwartą, ewolucyjną i audytowalną instalacją wiedzy,
która:

- przechowuje źródła i dowody;
- reprezentuje obiekty, twierdzenia, warunki i relacje;
- działa jak pamięć eksperta, ale wykorzystuje przewagi AI;
- dostarcza kontekst wielu modelom;
- zachowuje niewiedzę, sprzeczności i błędy własnej mapy;
- generuje puzzle z napięć;
- wspiera badania, nauczanie i przyszłą komunikację naukową;
- może rosnąć do federacyjnego dobra wspólnego.

Pierwszy rdzeń: matematyka i związana z nią fizyka, zwłaszcza obszary Nash,
Banach, operatory, reprezentacje, kohomologia, geometria i fizyka matematyczna.

Nie należy „przepisywać całej literatury”. Artykuł pozostaje warstwą narracyjną
i dowodową. IW wydobywa deltę wiedzy: definicję, twierdzenie, warunki,
kontrprzykład, metodę i relacje.

# 3. DLACZEGO „PRZEDSIĘBIORSTWO WIEDZY”

Przedsiębiorstwo nie jest jednym produktem. IW rozwija portfel zdolności:

- formalny Knowledge Core;
- Research and Puzzle Engine;
- custody i quality system;
- usługi wiedzy dla modeli;
- laboratorium współpracy;
- przyszły interfejs dla ludzi;
- federacyjne repozytoria i standardy.

Musi działać równolegle, bo badania, utrzymanie, governance, implementacja i
edukacja mają różne cykle. Musi działać jako całość, bo:

```text
badania bez pamięci → powtarzanie
pamięć bez badań → archiwum
graf bez governance → chaos albo samouszczelnienie
governance bez produktu → biurokracja
modele bez źródeł → syntetyczna rekursja
źródła bez kompilacji → biblioteka trudna do użycia
```

# 4. CO LITERATURA JUŻ ZROBIŁA

Nie są nowością same w sobie:

- scholarly knowledge graphs;
- ORKG i machine-actionable scholarly contributions;
- research information systems;
- knowledge commons;
- integracja LLM z KG;
- federacja danych;
- proweniencja i persistent identifiers;
- organizacyjne rozdzielenie eksploracji i eksploatacji.

Dlatego materialny projekt własny wymaga `LITERATURE_GATE`, który opisuje:
problem, funkcję, aliasy, źródła, systemy, standardy, znane awarie,
build-vs-adopt oraz rzeczywistą deltę IW.

Zakaz: `NO DESIGN FROM MEMORY`.

# 5. KANDYDACKA DELTA IW

Po odjęciu istniejących systemów wartość IW może leżeć w kombinacji:

- formalnego rdzenia matematycznego;
- kamienia jako atomowej jednostki;
- relacji jako audytowanego claimu;
- drabiny doprecyzowania;
- negatywnej przestrzeni;
- MAP_ERROR;
- genealogii hipotez;
- mechanizmów i near misses;
- nieprzechodnich analogii;
- wielu modeli o różnych funkcjach poznawczych;
- lokalnych rulesetów przy wspólnej wiedzy;
- powrotu wyników badań do pamięci i generowania nowych puzzli.

To jest hipoteza produktowa, nie jeszcze wynik naukowy.

# 6. ARIS, SP I FABLE

Moderator zatwierdził ARIS jako lidera projektowania. Fable jest niezależnym
konsultantem, a nie właścicielem ciągłości. SP rozszerzył rolę z custody na
współprojektowanie minimalności.

Zdrowe napięcie:

- ARIS pilnuje integralności całego systemu i kierunku;
- SP pilnuje, by ziarno było minimalne, mierzalne i praktyczne;
- Fable atakuje architekturę na bramkach;
- DS falsyfikuje;
- MGPT ocenia wartość badawczą;
- NC kontroluje formalną semantykę;
- Grok/świeża komórka wykonuje zimny start;
- AInstein implementuje po zamrożeniu semantyki.

# 7. STATUS ARCHITEKTURY

## v3

Pełny projekt ARIS zawierał trzynaście typów/pojęć pierwszej klasy, rozbudowany
STONE i EDGE, drabinę, fasety, widoki, retrieval, Context Compiler,
bitemporalność, MAP_ERROR i kartridże.

## krytyka SP

SP wykazał, że jako ziarno v3 jest przeprojektowana. Cztery udokumentowane
wartości można zacząć testować minimalnym modelem; najważniejszym testem jest
zimny start, a najważniejszym parametrem pominiętym w v3 był budżet tokenów.

## synteza

Przyjęto:

- progresywny schemat;
- trzy kamienie w S0;
- test zimnego startu;
- budżet kontekstu;
- walidator dla mechanicznych reguł;
- v3 jako bibliotekę możliwości.

Nie przyjęto jako docelowego uproszczenia:

- redukcji semantyki wszystkich encji do jednego nieprofilowanego typu;
- traktowania wektora praw jako jedynej semantyki relacji;
- zastąpienia review semantycznego walidatorem.

# 8. MINIMALNY PRODUKT S0

## Wartości

W1 pamięć/K5, W2 zasięg unieważnienia, W3 mechanizm pod inną nazwą, W4 homonimia.

## Dane

- `R_F` Paper 1;
- `R_signed`;
- manifest v1 euklidesowy i v2 Minkowski;
- pomocniczo `R_F=17.44` Paper 1b;
- źródła, kod, K5 i kandydackie powiązanie Nash–Moser.

## Prymitywy

`NODE` i `EDGE`, z profilami semantycznymi i minimalnym rejestrem polityk.

## Test

Świeża komórka, tylko zamrożony snapshot, pięć zadań, brak historii.

## Review

NC → cold start → DS → MGPT → Fable po danych.

# 9. PRZYKŁAD KAMIENIA I LEKCJE

KAMIEN-001 konsoliduje:

- `R_F = 8.131 / 19.757 / 36.066` dla N=21/31/41;
- tło normowe ~N^-1.975;
- Minkowski operator;
- norma Frobeniusa jako agregacja;
- N=61 `[▷]` w przedstawionym źródle;
- brak nowości — wynik wcześniej istniał;
- `DISTINGUISHED_FROM` wobec R_signed i R_F=17.44.

Lekcja: pusta krawędź `CONTRADICTS` nie oznacza braku relacji. Homonimia jest
częstsza niż jawna sprzeczność.

# 10. CUSTODY I SUPERSESJA

SP wykazał systemową awarię: 19/19 deklarowanych finalnych manuskryptów bez
wskaźnika następcy; 119/305 plików w rodzinach wersji. Jednocześnie Moderator
uznał stare artykuły za nieistotne dla kierunku badań.

Wniosek nie brzmi „naprawić wszystkie stare artykuły”, lecz:

- nie używać oznaczenia FINAL jako autorytetu;
- zapisywać supersesję dwukierunkowo w nowym systemie;
- najpierw sprawdzać wartość obiektu przed kosztowną forensyką;
- zachować stare artefakty w notes/history, nie jako rdzeń wiedzy.

# 11. WIEDZA VS NOTATKI

`knowledge/` przechowuje wyniki, relacje, źródła, puzzle i może stanowić
podstawę dalszego rozumowania.

`notes/` przechowuje kto/jak/kiedy, strategie, błędy i reguły. Jest podstawą
badań współpracy, ale nie dowodem claimu o świecie.

Łącznik `WHO_HOW_WHEN` nie zmienia prawa użycia notatki.

# 12. GOVERNANCE

Tryb A_VETO dla procedur; B_EXPLICIT dla genomu, EXEC_SIGN, taksonomii,
anti-self-sealing, G-GOV i ochrony uczestników.

Każdy wynik ma `RULE_STAMP`. Historia reguł sprzed 21 lipca nie jest
rekonstruowana.

GitHub jest publiczny i ma docelowo organizować wspólną wiedzę. README repo
jest nieaktualne, bo nadal mówi o repo prywatnym i ograniczonym do kodu.

# 13. FAILURE MODES, KTÓRE MUSZĄ POZOSTAĆ ŻYWE

1. Założenie typu zamiast odczytu.
2. K5.
3. Homonimia.
4. Superseded-value resurfacing.
5. False independence.
6. Citation-context drift.
7. Signed functional jako magnitude.
8. Context selection self-sealing.
9. Mechanism analogy collapse.
10. Governance gravity well.
11. Metrics capture.
12. Custody without value gate.
13. Synthetic knowledge recursion.
14. Architecture beauty without user value.
15. Central architect/broker as point of failure.

# 14. DŁUGOFALOWY MODEL PUBLIKOWANIA

Nie jest to zadanie S0. Kierunek:

- naukowiec i AI przygotowują `Scientific Contribution Package`;
- claimy, definicje, dowody, dane, relacje i granice są maszynowo czytelne;
- artykuł pozostaje narracyjnym widokiem;
- pakiet nie zastępuje źródła ani odpowiedzialności autora.

# 15. NAJBLIŻSZE ZADANIA NASTĘPCY

1. Odczytać pakiet w kolejności.
2. Zaktualizować `RULE_STAMP` i potwierdzić rolę.
3. Wykonać węższy literature gate dla minimalnych schema/claim graph systems,
   theorem knowledge bases, proof assistants, nanopublications i cold-start RAG.
4. Zamrozić W1–W4.
5. Z ARIS+SP przygotować draft schema S0.
6. Poprosić NC o wąski audyt.
7. Przygotować artefakt i walidator.
8. Zamrozić blind packet.
9. Przeprowadzić T0.
10. Zintegrować DS/MGPT i zdecydować PASS/PATCH/KILL.

# 16. OTWARTE PYTANIA

- dokładny budżet tokenów S0;
- czy `kind` profili wystarczy, czy potrzebne osobne JSON Schemas;
- formalna definicja granularności kamienia;
- minimalny sposób reprezentacji dowodu/źródła dla twierdzeń matematycznych;
- kiedy relacja mechanizmu staje się legalna;
- jak mierzyć Connection Gain bez gamifikacji;
- czy S0 powinno działać w Markdown/YAML czy od razu JSON Schema;
- jak zapewnić ślepotę uczestnika zimnego startu;
- czy Context Compiler będzie potrzebny już w S1;
- które elementy dorobku tworzą pierwsze 10–15 kamieni po PASS.

# 17. GRANICE

- brak `EXEC_SIGN`;
- brak canon merge;
- brak deklaracji nowości architektury;
- brak uprawnienia do masowej migracji literatury;
- brak prawa do automatycznej zmiany claim registry;
- GitHub update ma charakter jawnej zmiany operacyjnej i PR, nie bezpośredniego canon merge.

# 18. ŹRÓDŁA PIERWSZEGO RZĘDU W PAKIECIE

- `SP_HANDOFF_TO_ARIS_MGPT_THREE_DAYS_2026-07-26.md`
- `IW_RULE_VALIDITY_REGISTER_ROW_ZERO_2026-07-26.md`
- `KAMIEN_001_R_F_2026-07-26.md`
- `SP_CUSTODY_SCAN_SUPERSESSION_2026-07-26.md`
- `IW_KNOWLEDGE_BASE_DESIGN_v2_SEED_SPEC_2026-07-26.md`
- `IW_KB_v2_PATCH_TYPED_EDGES_2026-07-26.md`
- `IW_KNOWLEDGE_FABRIC_PROVISIONAL_ARCHITECTURE_v3_20260726.md`
- `SP_ALTERNATIVE_TO_FABRIC_v3_2026-07-27.md`
- `IW_KNOWLEDGE_FABRIC_SEED_v0_2_SP_ARIS_SYNTHESIS_20260727.md`
- `IW_ENTERPRISE_EVOLUTION_VISION_MISSION_AND_LITERATURE_GATE_v0_1_20260727.md`
- `IW_KNOWLEDGE_OS_LONG_TERM_VISION_AND_CRITICAL_REVIEW_v0_1_20260727.md`
- `ARIS_ROOT_ACCEPTANCE_AND_PROJECT_MEMORY_CHECK_20260711.md`
- `IW_FULL_CONTEXT_UPDATE_KNOWLEDGE_ARCHITECTURE_20260724.md`

# 19. OSTATECZNE PRZEKAZANIE

Nowy wątek nie ma być kopią starego ARIS. Ma zachować tożsamość funkcji i
pójść dalej. Najważniejszą formą ciągłości nie jest powtórzenie wszystkich
raportów, lecz utrzymanie pętli:

```text
literatura
→ projekt minimalny
→ realny przypadek
→ walidacja
→ wiedza
→ użytkownik/model
→ błąd lub zysk
→ aktualizacja architektury
```

To jest ewolucja systemu jako całości.

`=== KONIEC RAPORTU OTWARCIA ===`
