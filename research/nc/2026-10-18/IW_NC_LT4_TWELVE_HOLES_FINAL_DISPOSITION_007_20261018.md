# IW_NC_LT4_TWELVE_HOLES_FINAL_DISPOSITION_007_20261018

ARTIFACT_ID: IW_NC_LT4_TWELVE_HOLES_FINAL_DISPOSITION_007_20261018
KOMÓRKA: NC — zewnętrzna komórka Claude
OBIEKT: monografia, DRIVE 1cn97_kO65BcJRRWQrvrL9fKlEYBT3PHg6BJItn1Q4FQ
POPRZEDZAJĄ: 005 (audyt warstwy, DRIVE 1q9csyp4dBTYoZiA9kNmBL-lr0O7iFghB), 006 (cztery świadki, DRIVE 17ASIUR8CxH6rWo2UPD8EuSO6E3fMez_1)
STATUS: [▷] / EXEC_SIGN = BRAK / NO_CANON / NO_NOVELTY
KOD: `twin.py` sha256 bbe9464dbf5fd00ccaadc795b601425b341d334a82887ff472e9f3c62b387f3b
AUTORSTWO I DECYZJA: LT4. **AUDYT ZEWNĘTRZNY OBOWIĄZKOWY** — świadek z §1 jest mój.

---

## 0. Wynik główny: z dwunastu dziur tylko sześć wymagało nowej matematyki

Audyt 005 znalazł dwanaście non-mapów bez świadka. Po przepracowaniu każdego z osobna okazuje
się, że **lista była przeszacowana jako zadanie matematyczne**:

| dyspozycja | ile |
|---|---|
| zamknięte świadkiem, który skonstruowałem (006 + §1 poniżej) | **6** |
| świadek **już jest w manuskrypcie**, w innym rozdziale — brakuje odsyłacza | **3** |
| gospodarz w literaturze — brakuje cytowania, nie dowodu | **1** |
| **nie jest non-mapem** — uwaga o typowaniu źle sklasyfikowana | **1** |
| nadal otwarte | **2** |

Czyli realny deficyt matematyczny warstwy non-mapów to **dwie pozycje**, a nie dwanaście.
Reszta to praca redakcyjna: odsyłacze, jedno cytowanie, jedno przeredagowanie.

**To koryguje mój własny wniosek z 005 na korzyść monografii.** Pisałem tam, że atlas jest
„dziurawy na brzegach". Jest raczej **rozproszony**: świadkowie istnieją, ale leżą w innych
rozdziałach niż zdania, które uzasadniają, więc czytelnik ich nie znajduje. To defekt złożenia,
nie dowodu — i naprawia się go inaczej i taniej.

---

## 1. Nowy świadek: §2.9 i §3.5 (bliźniacza para, jeden świadek)

**Zdanie monografii.** §2.9: „Równoważność realizacji minimalnych z dokładnością do podobieństwa
nie jest tożsamością wewnętrznej zmiennej fizycznej." §3.5: „Równość odpowiedzi nie wyznacza
automatycznie mikroskopowych współrzędnych stanów ukrytych." Tekst sam podaje właściwy warunek
zgodności — `s₂∘S = s₁` — ale nie pokazuje, że bywa niespełnialny.

**Konstrukcja.** `D₁ = diag(−1,−2)`, `C₁ = (1,1)ᵀ`, `B₁ = (1,1)`; `T = [[1,1],[0,1]]`;
`D₂ = TD₁T^{-1}`, `C₂ = TC₁`, `B₂ = B₁T^{-1}`. Obserwabla ukryta zadana **tym samym wzorem**
w obu układach współrzędnych: `s(y) = y₁`.

**Te same dane zewnętrzne w każdej chwili.** `K(t) = Be^{tD}C`:

| t | 0 | 0.25 | 0.5 | 1.0 | 2.0 | 4.0 |
|---|---|---|---|---|---|---|
| `K₁` | 2.000000000000000 | 1.385331442784038 | 0.974410100884076 | 0.503214724408055 | 0.153650922125347 | 0.018651101516637 |
| różnica | 0 | 0 | 0 | `4.4e-16` | 0 | 0 |

**Obie realizacje minimalne**: rangi osiągalności i obserwowalności równe 2 dla obu.

**A zmienna ukryta ewoluuje inaczej.** Odpowiedź na impuls jednostkowy, `y(0) = C`:

| t | `s(y₁(t))` real. 1 | `s(y₂(t))` real. 2 | różnica |
|---|---|---|---|
| 0.00 | 1.000000000000000 | 2.000000000000000 | 1.000000 |
| 0.25 | 0.778800783071405 | 1.385331442784038 | 0.606531 |
| 1.00 | 0.367879441171442 | 0.503214724408055 | 0.135335 |
| 4.00 | 0.018315638888734 | 0.018651101516637 | 0.000335 |

**I nie da się tego naprawić innym podobieństwem.** Układ równań `SD₁ = D₂S`, `SC₁ = C₂`,
`B₁ = B₂S` ma **rank 4 przy 4 niewiadomych**, czyli rozwiązanie **jednoznaczne**: `S = T`
z dokładnością `6.7e-16`, residuum `9.7e-16`. Zatem jedyne dostępne podobieństwo daje
`s₂∘S = (1,1) ≠ (1,0) = s₁`, z defektem dokładnie `1.000000`.

**Teza świadka.** Istnieją dwie minimalne realizacje tej samej funkcji przenoszenia,
nierozróżnialne z zewnątrz w każdej chwili, w których „pierwsza współrzędna ukryta" ma różne
trajektorie — a ponieważ podobieństwo między realizacjami minimalnymi jest **jednoznaczne**,
nie istnieje wybór `S`, który by to uzgodnił. Dokładnie to twierdzą §2.9 i §3.5, i dokładnie
w tej postaci, którą tekst sam zapowiada warunkiem `s₂∘S = s₁`.

Jednoznaczność podobieństwa jest klasyczna (teoria realizacji Kalmana) — **NO_NOVELTY**; wkładem
jest tylko złożenie jej z obserwablą ukrytą w jeden świadek.

---

## 2. Trzy pozycje: świadek już jest w manuskrypcie, brakuje odsyłacza

**§5.10 — „Nierówność praw dla dwóch instrumentów nie jest dowodem nieokreślonej przyczynowości."**
Potrzebny świadek: układ o **określonym** porządku przyczynowym, którego prawa dwuinstrumentowe
są różne. Tw. 5.3 i §5.5a konstruują dokładnie to — dwa modele `Φ_t(ρ) = Tr_E[U_t(ρ⊗σ_E)U_t*]`,
czyli obwody **sekwencyjne**, a więc o ustalonym porządku, dające różne prawdopodobieństwa dla
tego samego legalnego instrumentu dwuczasowego. Świadek leży pięć sekcji wcześniej w tym samym
rozdziale. **Odsyłacz, nie matematyka.**

**§7.2 — „Nie wynika stąd jej ciągłość, całkowita dodatniość ani równoważność procesów
z interwencjami."** To **trzy** zdania w jednym i rozpadają się różnie:
- *równoważność procesów* — świadkiem jest Tw. 5.3, jak wyżej. Odsyłacz.
- *całkowita dodatniość* — `V_t` działa na `Y₀ = r(X)`, zbiorze bez zadeklarowanej struktury
  systemu operatorowego. Pojęcie CP **nie jest tam zdefiniowane**, więc nie ma czego obalać.
  To uwaga o typowaniu, nie non-map. Przeredagować.
- *ciągłość* — **konstruowalne mechanizmem z §2.3** (faktoryzacja przez redukcję, która jest
  ciągłą bijekcją, lecz nie jest odwzorowaniem ilorazowym), ale **nie skonstruowałem go**.
  Potrzeba ciągłego `U_t` i takiej redukcji jednocześnie, a przykład `[0,2π) → S¹` z §2.3
  dotyczy `τ̄`, nie `V_t`, więc nie przenosi się wprost. **Zgłaszam jako konstruowalne,
  nie jako zrobione.**

**§2.8 → patrz §4**, nie udało mi się jej domknąć odsyłaczem; zostaje otwarta.

---

## 3. Jedna pozycja do przeredagowania, nie do udowodnienia

**§4.7 — „nie wynika stąd, że skompresowane reprezentacje grupowe lub kwantowe supermapy
posiadają analogiczną homotopię".** Tekst sam podaje powód: „tam brakuje zadeklarowanego
różniczkowania i odpowiedniej tożsamości". To jest rozstrzygające — tożsamości homotopii
`T_s − T_u = dK + Kd` **nie da się nawet zapisać** bez `d`. Zdanie nie jest nieimplikacją
matematyczną wymagającą świadka; jest stwierdzeniem, że równanie jest źle otypowane w drugim
formalizmie.

Rekomendacja: przenieść z rejestru non-mapów do uwag o typowaniu i przeformułować
z „nie wynika stąd, że…" na „tożsamości (4.12) nie można sformułować dla…, ponieważ nie ma
zadeklarowanego różniczkowania". Różnica jest merytoryczna: pierwsza wersja obiecuje
kontrprzykład, którego nie ma i nie może być.

---

## 4. Dwie pozycje nadal otwarte

**§2.8 — „Losowa redukcja informacji i fizyczna eliminacja sektora Hilberta nie są tym samym
działaniem."** Szukałem świadka w manuskrypcie. Najbliższy to uwaga z rozdziału 1 §8: „Mapa
`ρ ↦ VρV*` jest całkowicie dodatnia, lecz na ogół **zmniejsza ślad**", podczas gdy jądro
Markowa ślad zachowuje. **To jednak nie jest ten sam obiekt**: §2.8 mówi o garblingu
w sensie Blackwella wobec eliminacji sektora Hilberta, a rozdział 1 o kompresji amplitud
wobec śladu częściowego. Nie wolno ich utożsamić — a gdybym to zrobił, popełniłbym dokładnie
ten błąd, który ten non-map ostrzega. **Zostaje otwarte**; potrzebny świadek rozdzielający
garbling od eliminacji sektora dla konkretnej obserwabli.

**§3.6 — „w nieskończonym wymiarze sama minimalność przybliżona nie zapewnia ograniczonego
izomorfizmu z ograniczoną odwrotnością".** To jedyna pozycja, dla której sądzę, że gospodarz
istnieje w nieskończeniewymiarowej teorii realizacji, ale **nie szukałem**. Nie przypisuję
nikomu wyniku, którego nie sprawdziłem.

---

## 5. Zaktualizowany bilans decyzji ramowej

W 005 podałem, że rama atlasowa kosztuje „dwanaście świadków". Po tym zwrocie:

- **sześć świadków już jest** (cztery w 006, dwa — jako jeden — tutaj);
- **cztery pozycje to praca redakcyjna**: trzy odsyłacze wewnątrz manuskryptu, jedno cytowanie
  literatury (§5.2), jedno przeredagowanie (§4.7) — plus jeden świadek konstruowalny, którego
  nie zbudowałem (§7.2 ciągłość);
- **dwie pozycje otwarte** (§2.8, §3.6).

Koszt ramy atlasowej spadł więc z „dwunastu nowych wyników" do **„dwóch otwartych pozycji plus
kilka godzin redakcji"**. To zmienia porównanie z 004 §6 jakościowo, nie ilościowo: przy ramie
twierdzeniowej brakuje nieokreślonej liczby wyników hierarchii B, których nie da się dopisać,
bo każde nowe twierdzenie elementarne trafia do A. Przy ramie atlasowej brakuje **dwóch**.

Decyzja nadal należy do Moderatora i LT4. Dostarczam trzecią i ostatnią liczbę.

---

## 6. Czego nie twierdzę

1. **Nowości matematycznej — nigdzie.** Jednoznaczność podobieństwa realizacji minimalnych jest
   klasyczna.
2. **§7.2 (ciągłość) nazwałem konstruowalnym, ale nie skonstruowałem.** Mechanizm z §2.3 dotyczy
   `τ̄`, nie `V_t`, i przeniesienie wymaga osobnego przykładu. Zapisuję jako niezrobione.
3. **Dyspozycja „świadek jest w innym rozdziale" to mój osąd o tym, że świadek jest adekwatny.**
   Dla §5.10 i §7.2 (równoważność procesów) uważam odsyłacz do Tw. 5.3 za trafny, ale to wymaga
   potwierdzenia przez kogoś, kto zna §5.5a lepiej ode mnie.
4. **§3.6 — nie szukałem literatury.** „Sądzę, że gospodarz istnieje" nie jest ustaleniem.
5. **Nie przeklasyfikowałem całej warstwy ponownie.** Przepracowałem dwanaście pozycji z listy
   A; pozostałych 84 nie ruszałem, a granica T/A nadal jest sporna (005 §6).
6. Nie dotykałem niczego opartego na moich wynikach J3 — nadal `[▷]`, w audycie zewnętrznym.

---

KONIEC. Status [▷]. EXEC_SIGN brak.
