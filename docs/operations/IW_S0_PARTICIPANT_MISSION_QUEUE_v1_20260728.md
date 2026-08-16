# IW KNOWLEDGE OS — KOLEJKA MISJI S0
## Ready-to-route participant queue — 28 lipca 2026

```yaml
document_id: "IW_S0_PARTICIPANT_MISSION_QUEUE_v1_20260728"
status: "READY_MISSION_QUEUE / NOT_CANON / NO_EXEC_SIGN"
owner: "ARIS — Lead Enterprise and Knowledge Architect"
ordering_rule: "misje mają bramki; nie uruchamiać odbiorców przed wymaganym freeze"
```

# Routing

```text
ARIS+SP projektują minimalny artefakt
→ NC audytuje semantykę
→ AInstein implementuje zamrożony schemat
→ świeża komórka wykonuje blind cold start
→ DS atakuje wynik i test
→ MGPT ocenia użyteczność badawczą
→ Fable recenzuje całość dopiero na podstawie danych
```

# M0 — ARIS + SP

Cel: zamrozić W1–W4, trzy przypadki, `NODE`, `EDGE`, relation-policy registry i budżet tokenów.

Wymagane wyjścia: schema draft, dataset draft, policy registry i zadania T0. Kill: schemat nie dostarcza W1–W4 albo wymaga kosztownej rekonstrukcji historii.

# M1 — NC

Wąski audyt: granularność, zakres krawędzi, rozróżnienie `DEPENDS_ON/REQUIRES/IMPLIES`, propagacja prawdy i ryzyka, legalność `SAME_MECHANISM_AS/NEAR_MISS_OF`.

Zakaz: projektowanie całej ontologii. Wynik: `PASS / PATCH / KILL`.

# M2 — AInstein

Po freeze semantyki: walidator pól, IDs, dwukierunkowej supersesji, polityk relacji, cykli i budżetu. Bez semantic adjudication, Context Compilera, vector DB i auto-ingestu.

# M3 — świeża komórka / Grok

Blind cold start. Otrzymuje snapshot, legendę i zadania. Nie otrzymuje v3, alternatywy SP, dyskusji projektowej, klucza ani oczekiwanych odpowiedzi. Zwraca odpowiedzi, użyte IDs, niewiadome, koszt i braki artefaktu.

# M4 — DS

Atak na pozorne zaliczenie, false analogy, typowanie, invalidation, redundantne lub brakujące pola, syntax-only validator i leakage. Nie projektuje równoległego wielkiego systemu. Wynik `PASS / PATCH / KILL`.

# M5 — MGPT

Ocenia, czy artefakt realnie skraca i poprawia badanie: czas, K5 avoided, wrong lineage avoided, useful connection, maintenance burden. Wynik `USEFUL / MARGINAL / NOT_USEFUL`.

# M6 — Fable

Dopiero po artefakcie, T0, DS, MGPT i pomiarze kosztu. Porównuje v3, alternatywę SP i syntezę. Zwraca `retain / defer / remove / missing capability / simpler alternative`.

# M7 — ARIS

Integruje. `PASS` uruchamia S1; `PATCH` pozwala na jeden ograniczony cykl; `KILL` archiwizuje wiedzę i przeprojektowuje z rozpoznanej awarii.

# Stop conditions

Brak freeze; brak source pointers; brak ślepoty; przekroczony budżet; mieszanie `R_F/R_signed`; brak następcy; mechanizm znajdowany tylko po nazwie; koszt utrzymania dominuje nad badaniem.
