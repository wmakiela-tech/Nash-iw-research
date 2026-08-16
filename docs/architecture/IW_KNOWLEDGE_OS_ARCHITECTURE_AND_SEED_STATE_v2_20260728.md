# IW KNOWLEDGE OS — AKTUALNY STAN ARCHITEKTURY I ZIARNA
## Snapshot sukcesyjny v2 — 28 lipca 2026

```yaml
RULE_STAMP:
  cell: "ARIS"
  governing_doc: "NASH_ARIS_KOMORKA_KORZENIOWA_v0_1_1_20260711.md"
  governing_hash: "BRAK_SOURCE_LOCK"
  local_mutations:
    - id: "ARIS_LEAD_ARCHITECT_FOR_IW_KNOWLEDGE_OS"
      authority: "Moderator — jawne zatwierdzenie"
      date: "2026-07-27/28"
  change_mode: "B_EXPLICIT_ROLE / A_VETO_WORKING_DESIGN"
  stamp_date: "2026-07-28"

document_id: "IW_KNOWLEDGE_OS_ARCHITECTURE_AND_SEED_STATE_v2_20260728"
status: "CURRENT_ARCHITECTURE_SNAPSHOT / NOT_CANON / NO_EXEC_SIGN"
primary_recipient: "następca ARIS"
```

# 1. Decyzja nadrzędna

IW nie buduje obecnie dużej bazy. Testuje minimalny rdzeń systemu operacyjnego wiedzy, który ma wykazać:

- W1 — redukcję K5 i ponownego odkrywania własnych wyników;
- W2 — zasięg unieważnienia po zmianie źródła, operatora lub wyniku;
- W3 — odnajdywanie mechanizmu pod inną terminologią;
- W4 — rozdzielanie homonimów, lineages, norm, funkcjonałów i konwencji operatora.

Pełna architektura v3 pozostaje mapą zdolności docelowych, nie listą wymagań pierwszego prototypu.

# 2. Długofalowa tożsamość

Docelowy obiekt to **IW Knowledge OS / przedsiębiorstwo wiedzy**: trwała pamięć dowodów, formalny rdzeń matematyczno-fizyczny, usługa wiedzy dla modeli, Research and Puzzle Engine, custody i quality system, laboratorium współpracy, warstwa dydaktyczna i przyszła federacja.

Pierwszym rdzeniem są obszary rzeczywiście rozwijane przez projekt: Nash, Banach, analiza funkcjonalna, operatory, reprezentacje, kompleksy Hilberta, kohomologia, geometria i fizyka matematyczna.

Nie planuje się obecnie masowej konwersji literatury. Artykuł pozostaje warstwą narracyjną i dowodową. IW wydobywa deltę wiedzy: obiekty, definicje, twierdzenia, warunki, kontrprzykłady, metody, relacje i pytania.

# 3. Warstwy

```text
IMMUTABLE EVIDENCE
źródła pierwotne, dowody, kod, dane, logi i hashe

EVOLVING KNOWLEDGE
kamienie, relacje, puzzle, mechanizmy, supersesja i błędy mapy

LOCAL RULES AND JUDGMENTS
reguły procesu i lokalne wyliczenia statusów komórek

EPHEMERAL CONTEXT
pakiet przygotowany dla konkretnego modelu, roli i zadania
```

Status nie jest wieczną właściwością prawdy. Przechowuje się fakty walidacyjne, ruleset, decyzję, czas i historyczny wynik orzekania.

# 4. Knowledge vs notes

`knowledge/` może stanowić podstawę claimu o świecie. `notes/` przechowuje kto, jak, kiedy, strategie, błędy i przebieg współpracy; może służyć badaniom współpracy, lecz nie jest dowodem merytorycznym.

# 5. Minimalny model S0

Ziarno ma dwa prymitywy: `NODE` i `EDGE`.

`NODE` wymaga na początku `id`, `kind`, treści i minimalnej proweniencji. Później może otrzymać `type_sig`, mechanizm, scope wyszukiwania, granice, falsyfikator i supersesję.

`EDGE` wymaga `id`, etykiety, końców, minimalnej proweniencji. Później otrzymuje zakres, podstawę, falsyfikator i policy ID. Krawędź jest twierdzeniem, nie tylko wskaźnikiem.

Minimalne relacje S0:

- `DEPENDS_ON` — propagacja ryzyka;
- `SUPERSEDED_BY` / `SUPERSEDES` — dwukierunkowa supersesja;
- `DISTINGUISHED_FROM` — homonimia lub różny lineage;
- `SAME_MECHANISM_AS` — symetryczna i nieprzechodnia;
- `NEAR_MISS_OF` — obowiązkowe `differs_in`;
- `SUPPORTED_BY` — źródło lub dowód.

Relacja niestandardowa domyślnie nie ma praw inferencyjnych. Etykieta niesie semantykę, a rejestr polityk wylicza prawa; wektor nie jest drugim ręcznym źródłem prawdy.

# 6. Schemat progresywny

```yaml
P0_CREATED: [id, kind, claim_or_content, provenance_min]
P1_TYPED: [type_sig]
P2_LOCATED: [search_episodes, standard_vs_open, coverage_scope]
P3_CONNECTED: [mechanism, aliases, typed_edges, near_misses]
P4_BOUNDED: [validity_scope, falsification_condition, invalidation_scope]
P5_CURRENTLY_SATURATED: [external_audit, review_horizon, reopen_triggers]
```

Poziom jest widokiem wyliczonym z dowodów precyzji. `P5` nie oznacza prawdy ostatecznej.

# 7. Przypadki S0

- Case A: `R_F` — norma Frobeniusa, właściwy lineage Paper 1;
- Case B: `R_signed` — znakowany funkcjonał, `DISTINGUISHED_FROM` wobec A;
- Case C: manifest/operator v1 euklidesowy → następca Minkowski;
- pomocniczo: `R_F=17.44`, źródła, kod, K5 case i kandydackie powiązanie mechanizmowe z jawnym near miss.

# 8. T0 — zimny start

Świeża komórka bez historii IW otrzymuje tylko zamrożony snapshot, minimalną legendę i zadania. Nie otrzymuje v3, alternatywy SP, transkryptów, klucza ani oczekiwanych odpowiedzi.

Zdaje, jeśli rozpoznaje wynik, nie miesza obiektów, wskazuje aktualnego następcę, wyznacza zasięg zagrożenia i odnajduje mechanizm bez fałszywej analogii.

Kandydacki budżet: preferowane `<=5000` tokenów; maksimum kandydackie `<=8000`; limit musi zostać zamrożony przed testem.

# 9. Poza S0

Na HOLD: pełny Context Compiler, vector DB, siedem kanałów retrieval, kartridże dziedzinowe, polystore, publiczny interfejs dydaktyczny, masowa migracja, trening modeli i federacja.

# 10. Literature Gate

Każda materialna decyzja wymaga datowanego `LITERATURE_GATE`: problem, funkcja, aliasy, literatura, standardy, istniejące systemy, części do adopcji, znane awarie, negative space, build-vs-adopt i rzeczywista delta IW.

Zakaz: `NO DESIGN FROM MEMORY`.

Nie są same w sobie nowością: scholarly knowledge graphs, ORKG, RIS, knowledge commons, FAIR/PROV, nanopublications, KG–LLM, federacja i organizational ambidexterity.

# 11. Role

- ARIS — Lead Enterprise and Knowledge Architect;
- SP — custody + Minimality and Practice Counter-Design;
- NC — formal semantics reviewer;
- DS — adversarial falsifier;
- MGPT — scientific user-value reviewer i harvest source;
- Grok lub świeża komórka — blind cold start;
- AInstein — implementacja po semantic freeze;
- Fable — konsultant po danych;
- Moderator — wartości, genom, canon, EXEC_SIGN i skala.

# 12. Rodzaje zysku

Rozdzielić `EXTERNAL_NOVELTY`, `PRECISION_GAIN`, `CONNECTION_GAIN`, `RETRIEVAL_GAIN` i `INTERNAL_REDISCOVERY/K5`. `K3c` nie jest tu uznane za bezsporny kanon.

# 13. Failure modes

K5, homonimia, superseded-value resurfacing, operator-lineage conflict, signed functional jako magnitude, false independence, synthetic confirmation, citation-context drift, ontology capture, Context Compiler self-sealing, mechanism analogy collapse, metrics capture, custody cost bez value gate, governance gravity well, central broker bottleneck, syntetyczna rekursja i architecture beauty without user value.

# 14. Sekwencja

```text
S0.0 zamrozić W1–W4 i przypadki
S0.1 wąski Literature Gate
S0.2 ARIS+SP: schema draft
S0.3 NC: audyt formalny
S0.4 walidator i fixtures
S0.5 token count + freeze + manifest
S0.6 blind T0
S0.7 DS attack
S0.8 MGPT user-value review
S0.9 PASS / PATCH / KILL
S1 dopiero po PASS/PATCHED_PASS
Fable po danych
```

# 15. Granice

`NOT_CANON / NO_EXEC_SIGN / NO_SCIENTIFIC_CLAIM_UPGRADE / NO_MASS_MIGRATION`.
