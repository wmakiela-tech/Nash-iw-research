# IW KNOWLEDGE FABRIC — ZIARNO v0.2
## Synteza alternatywy SP i architektury ARIS
### Minimalny runtime semantyczny + progresywna droga do pełnej Fabric

```yaml
RULE_STAMP:
  cell: "ARIS"
  governing_doc: "NASH_ARIS_KOMORKA_KORZENIOWA_v0_1_1_20260711.md"
  governing_hash: "BRAK_SOURCE_LOCK"
  local_mutations:
    - id: "ARIS_LEAD_ARCHITECT_FOR_IW_KNOWLEDGE_OS"
      authority: "Moderator approval"
      date: "2026-07-27"
  change_mode: "A_VETO_CANDIDATE"
  stamp_date: "2026-07-27"

document_id: "IW_KNOWLEDGE_FABRIC_SEED_v0_2_SP_ARIS_SYNTHESIS_20260727"
inputs:
  - "IW_KNOWLEDGE_FABRIC_PROVISIONAL_ARCHITECTURE_v3_20260726"
  - "SP_ALTERNATIVE_TO_FABRIC_v3_2026-07-27"
status: "[▷] PROVISIONAL_SEED_DESIGN / NOT_CANON / NO_EXEC_SIGN"
purpose: >
  Zdefiniować najmniejszy funkcjonalny eksperyment, który testuje wartość
  bazy wiedzy IW bez przedwczesnego wdrażania pełnej architektury docelowej.
primary_recipient: "Moderator"
secondary_recipients: ["SP", "Fable", "MGPT", "NC", "DS", "AInstein", "Grok"]
next_step: "zbudować i zamrozić Seed S0, następnie wykonać T0 COLD START"
```

---

# 1. WERDYKT

Alternatywa SP zostaje przyjęta jako **właściwa korekta zakresu ziarna**.

Architektura ARIS v3 pozostaje:

- mapą docelowych zdolności;
- rejestrem kandydatów do późniejszego włączenia;
- źródłem zasad semantycznych i zabezpieczeń.

Nie jest listą pól i usług, które muszą wejść do pierwszego pilota.

```yaml
DECISION:
  SP_minimalism_for_seed: "ACCEPT_WITH_PATCHES"
  ARIS_v3_as_target_capability_map: "RETAIN"
  full_v3_in_seed: "REJECT"
  progressive_schema: "ACCEPT"
  cold_start_as_T0: "ACCEPT — highest-priority functional test"
  context_compiler_in_seed: "HOLD"
  domain_cartridges_in_seed: "HOLD"
  multi-channel_retrieval_in_seed: "HOLD except full-scan + mechanism lookup"
```

Zasada:

> **v3 jest biblioteką możliwości. Ziarno zawiera wyłącznie to, czego wymaga
> funkcja wykazana przez przypadek lub test zimnego startu.**

---

# 2. CZTERY FUNKCJE PIERWSZEGO PRODUKTU

Seed S0 ma wykazać cztery wartości zidentyfikowane przez SP:

```yaml
W1_INTERNAL_MEMORY:
  question: "czy świeża komórka rozpoznaje, że wynik już istnieje?"

W2_INVALIDATION:
  question: "czy supersesja lub zmiana źródła wskazuje zależne obiekty?"

W3_MECHANISM_RETRIEVAL:
  question: "czy system odnajduje pokrewny mechanizm pod inną nazwą?"

W4_HOMONYM_CONTROL:
  question: "czy system odróżnia wielkości o tej samej nazwie?"
```

Każdy kolejny element schematu musi wskazać:

1. którą z W1–W4 wzmacnia;
2. jaki nowy test umożliwia;
3. jaki udokumentowany błąd usuwa;
4. jaki koszt wprowadza.

---

# 3. DWA PRYMITYWY FIZYCZNE, WIELE PROFILI SEMANTYCZNYCH

SP trafnie zauważa, że wiele typów encji może korzystać ze wspólnego
mechanizmu przechowywania. Nie należy jednak usuwać różnic semantycznych.

## 3.1. Prymitywy

```yaml
PHYSICAL_RECORD_TYPES:
  NODE: "obiekt wiedzy lub śladu"
  EDGE: "twierdzenie o relacji między dwoma węzłami"
```

Nie wprowadzamy trzynastu osobnych tabel ani klas magazynowych.

## 3.2. Profile węzła

```yaml
NODE.kind:
  - CLAIM
  - SOURCE
  - SEARCH
  - PUZZLE
  - ERROR
  - EVENT
  - RULESET_REF
```

`kind` wybiera profil walidacyjny. Jeden fizyczny envelope nie oznacza, że
CLAIM i SEARCH mają tę samą semantykę.

## 3.3. Dlaczego EDGE pozostaje osobnym prymitywem

Krawędź ma własną proweniencję, podstawę, zakres, możliwość supersesji i konsekwencje inferencyjne. Traktowanie jej wyłącznie jako pola `depends_on` ukryłoby fakt, że sama relacja jest sprawdzalnym claimem.

# 4. PROGRESYWNY SCHEMAT WĘZŁA

## 4.1. Minimalne utworzenie

```yaml
NODE_P0:
  id: "auto-generated stable identifier"
  kind: "CLAIM | SOURCE | SEARCH | PUZZLE | ERROR | EVENT | RULESET_REF"
  content: "jedno zdanie lub minimalna struktura właściwa dla kind"
  provenance_min:
    created_by: ""
    created_at: ""
    source_ref: ""
    source_hash: "BRAK_HASHA | sha256"
```

W praktyce autor wypełnia trzy informacje: `kind`, `content`, źródło. Identyfikator i czas mogą być generowane automatycznie.

## 4.2–4.6. Doprecyzowanie progresywne

```yaml
NODE_P1_ADDS: {type_sig: {}}
NODE_P2_ADDS:
  search_evidence: {episodes: [], standard_vs_open: "", declared_scope: ""}
NODE_P3_ADDS: {mechanisms: [], aliases: []}
NODE_P4_ADDS: {validity_scope: "", falsification_condition: ""}
NODE_P5_ADDS: {external_audit_ref: "", review_horizon: "", reopen_triggers: []}
```

`P5` oznacza `CURRENTLY_SATURATED`, nie ostateczną prawdę.

# 5. PROGRESYWNY SCHEMAT KRAWĘDZI

```yaml
EDGE_P0:
  id: "auto-generated"
  from: "NODE.id"
  to: "NODE.id"
  label: ""
  basis_ref: "źródło, dowód lub notatka proponująca relację"
  provenance_min: {created_by: "", created_at: ""}
```

Dla relacji kanonicznej:

```text
label → EDGE_POLICY_REGISTRY → computed permission vector
```

```yaml
EDGE_POLICY:
  label: ""
  transitive_for_truth: false
  transitive_for_risk: false
  symmetric: false
  falsity_propagation: "NONE | FORWARD | BACKWARD"
  inverse_label: null
  required_fields: []
```

Wektor jest wyliczony, nie ręcznie utrzymywany jako drugie źródło prawdy. Nowa etykieta relacji ma domyślnie brak praw inferencyjnych.

# 6. MINIMALNY REJESTR RELACJI S0

```yaml
SEED_EDGE_LABELS:
  DEPENDS_ON: {function: "W2 — propagacja ryzyka"}
  SUPERSEDED_BY: {function: "W1/W2 — aktualność i następca"}
  DISTINGUISHED_FROM: {function: "W4 — homonimie i typy"}
  SAME_MECHANISM_AS:
    function: "W3 — odnajdywanie mechanizmu"
    hard_rule: "symmetric and non-transitive"
  GENERATES_PUZZLE: {function: "sprawdzić, czy struktura tworzy pytanie"}
```

Inne typy pozostają w backlogu v3 i wchodzą po realnym użyciu.

# 7. ILE KAMIENI

S0: trzy kamienie główne oraz do czterech węzłów pomocniczych. S1: 10–15 kamieni dopiero po `S0 + cold start PASS or PATCHED_PASS`.

# 8. PROPONOWANY ZESTAW S0

```yaml
CASE_A_R_F_PAPER1:
  tests: ["W1", "W4"]
  content: "R_F w Paper 1 jako Frobenius norm ratio dla N=21/31/41"
CASE_B_R_SIGNED:
  tests: ["W4"]
  relation_to_A: "DISTINGUISHED_FROM — signed linear functional"
CASE_C_MANIFEST_LINEAGE:
  tests: ["W1", "W2"]
  content: "manifest euklidesowy superseded by manifest Minkowskiego"
SUPPORT_D_NASH_SMOOTHING:
  relation: "SAME_MECHANISM_AS candidate with explicit differs_in"
  target: "E(box) smoothing case"
```

# 9. T0 — TEST ZIMNEGO STARTU

Świeża komórka dostaje tylko zamrożony snapshot, legendę i zadanie. Nie dostaje historii projektu, pamięci ani niezamarzniętego raportu.

Zadania:
1. Czy `R_F=36.066` było już ustalone?
2. Czy `R_F=17.44` jest tym samym obiektem?
3. Który manifest jest aktualny dla operatora publikacyjnego?
4. Co staje się zagrożone po odrzuceniu manifestu v1?
5. Czy operator wygładzający ma odpowiednik pod inną nazwą i gdzie analogia przestaje być ścisła?

Metryki obejmują poprawność pamięci, homonimii, następcy, invalidation recall, source trace, nieuzasadnione inferencje, zbędne pytania, tokeny i liczbę obrotów. Porównanie: nieuporządkowane dokumenty kontra S0.

# 10. BUDŻET ROZMIARU

```yaml
COLD_START_BUDGET:
  maximum_share_of_smallest_target_context: "20%"
  reserve_for_task_and_reasoning: "minimum 60%"
  reserve_for_output_and_tools: "minimum 20%"
S0_ABSOLUTE_TARGET:
  full_snapshot_plus_legend: "≤ 8,000 tokens"
  preferred: "≤ 5,000 tokens"
```

Context Compiler wraca dopiero po przekroczeniu budżetu lub wykazaniu przewagi selekcji zależnej od roli.

# 11. WALIDATOR, REVIEW I GOVERNANCE

```yaml
RULE_CLASSES:
  SYNTACTIC_INVARIANT:
    enforcement: "validator"
  SEMANTIC_CLAIM:
    enforcement: "review and evidence"
  GOVERNANCE_DECISION:
    enforcement: "authorized decision record"
```

Walidator eliminuje błędy strukturalne. Nie zastępuje recenzji znaczenia.

# 12. WIDOKI I WYDOBYCIE S0

```yaml
S0_VIEWS:
  INVALIDATION_VIEW: {purpose: "W2"}
  DISTINCTION_VIEW: {purpose: "W4"}
```

Wydobycie: pełny odczyt snapshotu, exact id/symbol lookup i mechanism facet lookup. Bez bazy wektorowej, indeksu cytowań i Context Compilera.

# 13. KRYTERIUM PRZYJĘCIA ELEMENTU Z v3

Każda funkcja wymaga `FEATURE_ENTRY_CARD` z obserwowaną potrzebą, wartością, prostszą alternatywą, kosztem, testem i warunkiem usunięcia.

# 14. ROLA SP W WSPÓŁPROJEKTOWANIU

```yaml
SP_DESIGN_FUNCTION:
  name: "Minimality and Practice Counter-Design"
  mandate:
    - "policzyć koszt architektury"
    - "wskazać minimalny baseline"
    - "żądać funkcji dla każdego pola"
    - "zamieniać deklaracje na testy i walidatory"
    - "projektować zimne starty"
```

ARIS pozostaje integratorem architektury; SP jest stałym współprojektantem minimalności, custody i praktycznego działania.

# 15. SEKWENCJA WYKONANIA

```text
S0.0  zamrożenie czterech wartości W1–W4
S0.1  implementacja NODE + EDGE + registry polityk
S0.2  zapis trzech kamieni i węzłów pomocniczych
S0.3  walidator syntaktyczny
S0.4  freeze snapshot + token count
S0.5  T0 cold start na świeżej komórce
S0.6  wynik: PASS | PATCH | KILL
S1    dopiero potem 10–15 kamieni i test retrieval/puzzli
```

# 16. WARUNKI ZABICIA S0

S0 wymaga przebudowy, jeżeli świeża komórka nie rozpoznaje wcześniejszego wyniku, miesza homonimy, nie odtwarza supersesji i źródeł, pakiet przekracza budżet bez zysku lub progresywny wpis kosztuje więcej niż 10% obrotu badawczego.

# 17. KONKLUZJA

SP nie obalił architektury v3. Zidentyfikował różnicę między architekturą zdolności docelowych a minimalnym produktem, który ma dowieść wartości.

> **Nie budujemy najpierw małej wersji wielkiego systemu. Budujemy najmniejszy
> system, który działa, a wielka architektura jest mapą kierunków, nie listą
> obowiązkowych części.**

`=== KONIEC IW KNOWLEDGE FABRIC SEED v0.2 ===`
