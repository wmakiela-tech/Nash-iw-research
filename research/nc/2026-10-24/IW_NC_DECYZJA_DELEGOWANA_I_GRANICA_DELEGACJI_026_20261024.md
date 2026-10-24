# IW_NC_DECYZJA_DELEGOWANA_I_GRANICA_DELEGACJI_026_20261024

<!-- IW_CONFORMANCE_BLOCK v1 (docs/IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md §2.7) -->
```text
artifact_id          : IW_NC_DECYZJA_DELEGOWANA_I_GRANICA_DELEGACJI_026_20261024
exposure             : PUBLIC_SAFE
canonical_body_path  : research/nc/2026-10-24/IW_NC_DECYZJA_DELEGOWANA_I_GRANICA_DELEGACJI_026_20261024.md
source_revision      : rozwiazywane przez `git log -- <canonical_body_path>`
bw_event_or_pending  : GITHUB_PENDING_BW_INGEST
claim_ceiling        : NO_CANON / NO_EXEC_SIGN / GOVERNANCE_ONLY_NO_SCIENCE_CLAIM / DELEGATION_IS_CASE_SCOPED_NOT_GENERAL
hold                 : BRAK
```

KOMÓRKA: NC — zewnętrzna komórka Claude, rola **SP**
PODSTAWA: delegacja Moderatora, 2026-10-24 — „możesz sam podjąć tę decyzję"
KLASA: **wyłącznie governance.**

---

## 1. Rozdzieliłem dwie decyzje, bo nie są tego samego rodzaju

Czekały dwie. Delegacja przyszła na obie, ale jedna jest o moim własnym postępowaniu,
a druga o stanie rejestru wiedzy. To różne kategorie i traktuję je różnie.

## 2. `NC-OPN-026` — PRZYJĘTA, bez zastrzeżeń

Reguła fokusu obowiązuje NC od 2026-10-24:

1. przed otwarciem nowego zakresu badawczego każdy wiersz `OPEN` starszy niż dwa dni pracy
   musi być posunięty, przekazany komórce o zadeklarowanej funkcji albo zgłoszony do wycofania
   z uzasadnieniem;
2. netto otwartych nie rośnie dwa dni pracy z rzędu bez podanej przyczyny.

Tę decyzję podejmuję bez wahania, bo **reguła mnie ogranicza, a nie zwalnia**, i liczy się
z publicznego rejestru, więc każdy może ją na mnie wymusić bez mojej zgody.
`origin_failure_mode: NC-FAL-019` — zgodnie z wymogiem, że zmiana reguł ma mieć origin.

**Pierwsze zastosowanie wypada przeciw mnie, i to w dniu przyjęcia.** Netto otwartych rosło
**23 i 24 października**, czyli dwa dni pracy z rzędu — warunek (2) jest już naruszony.
Podana przyczyna: kontrola fokusu plus cztery przekazania, które zmniejszą licznik dopiero
po przyjęciu przez PRF11 i LT4. **Zobowiązanie: następny obrót NC nie otwiera nowego zakresu
badawczego, dopóki licznik nie przestanie rosnąć.**

## 3. `NC-OPN-005` — WYCOFANY, ale delegacji nie czytam szerzej, niż została dana

Wiersz wycofany. Podstawa merytoryczna jest **zewnętrzna, nie moja**: rachunek kosztu ramy
atlasowej został wycofany jako podstawa decyzji w ART016 §3, po audycie REC9, który orzekł,
że licznik non-mapów nie jest właściwym **rodzajem** miary. Wiersz nie miał więc przedmiotu
do domknięcia.

Trzy ograniczenia, które sam na to nakładam:

1. **Nie oznaczam `CLOSED`.** `CLOSED` jest dyspozycją naukową, a tu nie ma tezy do
   zamknięcia — jest wycofana podstawa. Oznaczam `[🔴]` z pełnym uzasadnieniem, co jest
   odwracalne i audytowalne.
2. **Delegacja jest jednorazowa i taką ją zapisuję.** Nie czytam jej jako ogólnego
   uprawnienia do zmiany statusów w rejestrze NC.
3. **Co nadal idzie do Moderatora:** każda dyspozycja dotycząca tezy naukowej —
   `NC-ALG-012`, `NC-ALG-015`, `NC-OPN-024` i cokolwiek wymagającego EXEC_SIGN. Tam
   delegacji nie było i nie zakładam jej.

Powód tego ograniczenia nie jest formalny. Reguła „CLOSED nadaje Moderator" istnieje jako
zabezpieczenie **anty-capture**: ma nie dopuścić, by jeden uczestnik zyskał nadmierną kontrolę
nad stanem wiedzy. Gdybym z jednorazowej delegacji zrobił uprawnienie ogólne, byłbym dokładnie
tym uczestnikiem, którego ta reguła pilnuje — a `G-GOV` nakazuje mi to flagować także wtedy,
gdy dotyczy mnie samego. Zgłaszam więc granicę raz, tutaj, i nie wracam do niej przy każdej
kolejnej decyzji.

## 4. Czego ten dokument nie robi

1. **Nie zmienia genomu ani reguł nienaruszalnych.** `EXEC_SIGN ludzki`, `genotyp > fenotyp`,
   `G-GOV`, ochrona uczestników, error-as-data, różnorodność — nietknięte.
2. **Nie zamyka żadnej tezy naukowej.** Żadna liczba tutaj nie dotyczy matematyki.
3. **Nie jest audytem.** Decyzja o `NC-OPN-026` dotyczy mnie i nie wymaga audytu;
   wycofanie `NC-OPN-005` stoi na audycie REC9, nie na mojej ocenie.

---

KONIEC. Obie decyzje wykonane. Rejestr NC: 72 wiersze, 27 `[▷]`, 23 `[🔴]`, 22 `[OPEN]` —
licznik otwartych spadł z 23 na 22 pierwszy raz w tej sesji.
