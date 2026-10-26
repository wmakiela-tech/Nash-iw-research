---
artifact_id: IW_BADACZ_REVIEW_FAMILY_CONCENTRATION_PREREG_001_20261026
exposure: PUBLIC
claim_ceiling: PREREGISTRATION_ONLY / NO_RESULT / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-26
origin_cell: BADACZ (wątek Claude w roli Badacza; linia `badacz` zadeklarowana tym plikiem, nazwa do decyzji Moderatora)
document_type: PROTOCOL
task_id: BADACZ-FRONT-WEAKEST-POINT-001
status: FROZEN_BEFORE_CODE
corpus_pin: wmakiela-tech/Nash-iw-research commit 921360060946b0ed7bdfad2ef5e6b52e2b7e6dd1 (2026-10-26 14:22 CET)
acceptance_owner: Moderator; audyt zewnętrzny: Grok (publiczny GitHub)
---

# Preregestracja: koncentracja recenzji w jednej rodzinie modeli w publicznym korpusie IW

Plik zamrożony **przed** napisaniem i uruchomieniem kodu pomiaru. Zmiana definicji po
zobaczeniu wyników wymaga nowego pliku z jawną listą zmian.

## 1. Pytanie

Moderator zlecił (2026-10-26) przegląd całego frontu i wskazanie, gdzie puzzel trzyma
najsłabiej. Pierwszy krok to tani pomiar: **które wyniki o wysokiej centralności — takie, na
które powołuje się wiele innych linii — nie mają w publicznym korpusie żadnego kontaktu z
dokumentem innej rodziny modeli niż ich autor?**

To operacjonalizacja osi `C_MODEL` i `C_REVIEW` oraz trybu awarii `V5 REVIEW MONOCULTURE`
z EAI-S3 (`ING-20261012-0050`). Typ claimu wyniku: **definicyjno-pomiarowy o korpusie**, nie
naukowy o fizyce ani matematyce. Nie ocenia poprawności żadnego wyniku innej komórki.

## 2. Odjęcie stanu wiedzy — obie powierzchnie, przed kodem

**Własna powierzchnia projektu.**

- EAI-S3 (`research/eai-s3/2026-10-12/eai_s3_verification_bandwidth_epistemic_concentration_anti_self_sealing_001.md`)
  definiuje osie `C_PRODUCER, C_MODEL, C_SOURCE, C_REP, C_REVIEW, BACKLOG, CENTRALITY, BURDEN,
  EXPOSURE_RESERVE` oraz tryby `V1–V6`. **Nie mierzy ich.**
- NC 025 (`research/nc/2026-10-24/IW_NC_KONTROLA_FOKUSU_ZMIERZONA_I_TRIAGE_ZALEGLOSCI_025_20261024.md`)
  mierzy własny fokus NC i udział własnych falsyfikacji (52,4%). Nie mierzy rodzin recenzentów.
- Wyszukiwanie: `grep -rniE "C_REVIEW|C_MODEL|review monoculture|REVIEW_MONOCULTURE|model[- ]famil|rodzin[aąy] model|cross[- ]family|międzyrodzin|same[- ]family|correlated (error|verifier)|skorelowan"`
  po `research/ docs/ templates/` przy commicie z nagłówka oraz Drive `fullText contains`
  (`C_REVIEW`, `REVIEW MONOCULTURE`, `REVIEW_MONOCULTURE`, `C_MODEL`). Trafienia: tylko
  EAI-S3 i dokumenty bez pomiaru. **Nie przeszukano:** prywatnego BW (SEM, GENEALOGY,
  MECHANISM_GRAPH), Nash-Priv, Slacka poza deltą od 2026-10-25 20:00. Brak trafienia ≠ brak
  pomiaru.

**Literatura zewnętrzna** (lokatory i zapytania w §7).

- Kim, Garg, Peng, Garg, *Correlated Errors in Large Language Models*, ICML 2025,
  arXiv:2506.07962. Ponad 350 modeli. Błędy są silnie skorelowane; wspólna architektura i
  dostawca zwiększają korelację; **duże i dokładne modele mają silnie skorelowane błędy
  także przy różnych dostawcach**. Na jednym zbiorze, gdy oba modele się mylą, zgadzają się w
  60% przypadków.
- Goel i in., *Great Models Think Alike and this Undermines AI Oversight*, ICML 2025 (PMLR
  v267), arXiv:2502.04313. Metryka CAPA. Sędziowie LLM faworyzują modele **funkcjonalnie
  podobne**, nie tylko własną rodzinę; błędy upodabniają się wraz ze wzrostem zdolności.
- Panickssery, Bowman, Feng, *LLM Evaluators Recognize and Favor Their Own Generations*,
  NeurIPS 2024, arXiv:2404.13076. Liniowa korelacja zdolności rozpoznania własnego tekstu z
  siłą preferencji własnej.

**Konsekwencja dla pomiaru (wiążąca przy interpretacji).** Rodzina modelu jest wskaźnikiem
**koniecznym, ale niewystarczającym** niezależności. Recenzja międzyrodzinowa (Claude ↔ GPT)
nie certyfikuje niezależności: według Kim i in. duże modele różnych dostawców też mylą się
podobnie. Pomiar może więc wykazać **brak nawet słabej różnorodności**, nie jej obecność jako
niezależność. Niezależność w sensie projektu dają test, wykonanie kodu i kontrprzykład — nie
etykieta rodziny. **Nowość: żadna.** To zastosowanie znanej idei do korpusu projektu.

## 3. Definicje

- **Korpus:** pliki `*.md` w `research/` przy commicie z nagłówka. Pominięte: `README.md`,
  `DISPATCH_LEDGER*`, `CLAIM_ROWS*` oraz ten plik.
- **Linia autora:** drugi człon ścieżki, małymi literami (`research/LT4/…` → `lt4`).
- **Rodzina** (mapa zamrożona, z podstawą):

  | linia | rodzina | podstawa |
  |---|---|---|
  | `nc`, `badacz` | CLAUDE | etykieta transportu „Sent using Claude" (Slack 2026-10-25); ten wątek |
  | `rec10` | GPT | oświadczenie Moderatora 2026-10-26 |
  | `mt13`, `kn11`, `prf11`, `lt5` | GPT | etykieta transportu „Sent using ChatGPT" (Slack 2026-10-25) |
  | wszystkie pozostałe | GPT_ASSUMED | brak bezpośredniego potwierdzenia |

  Etykieta transportu nie dowodzi tożsamości modelu (TRANSPORT ≠ IDENTITY). Błędne przypisanie
  linii nie-GPT do GPT może tylko **zawyżyć** koncentrację. Dla każdego kandydata z rankingu
  wypiszę, czy któraś linia odwołująca się do niego ma rodzinę `GPT_ASSUMED`.
- **Treść modeli zewnętrznych** (Grok, DS/R1, Gemini/AInstein, Bielik) przekazana wewnątrz
  pliku liczy się jako kontakt międzyrodzinowy **tylko** wtedy, gdy ręcznie sprawdzę, że plik
  zawiera werdykt lub kontrprzykład tego modelu dotyczący konkretnego celu. Wynik ręcznego
  sprawdzenia wpisuję do raportu.
- **Aliasy węzła:**
  1. nazwa pliku bez rozszerzenia;
  2. wartości `artifact_id:` i `RETURN_ID:` z pierwszych 3500 znaków;
  3. hash bloba Git pliku przy commicie z nagłówka (pełny oraz pierwsze 12 znaków);
  4. etykieta krótka (komórka, numer obrotu) wyprowadzona z nazwy pliku. W tekście dopasowuję
     ją w wariantach `<KOM> ROT<n>`, `<KOM> R<n>`, `<KOM> rotation <n>`, `<KOM> <nnn>`, bez
     rozróżniania wielkości liter, z normalizacją zer wiodących, separatorem spacja, `-`, `_`
     albo `/`, i z granicą nie-alfanumeryczną po obu stronach (`M13` nie trafia w `MT13`).
- **Etykieta niejednoznaczna:** etykieta krótka wskazująca ponad jeden węzeł. Liczę dwa
  warianty i raportuję oba: **A** — przypisana do wszystkich wskazywanych węzłów; **B** — do
  żadnego. Ranking główny: wariant B, ostrożniejszy wobec fałszywych krawędzi.
- **Krawędź odwołania A→B:** tekst pliku A zawiera alias węzła B, A ≠ B.
- **Centralność B:** liczba różnych linii, innych niż linia B, mających co najmniej jeden plik
  z krawędzią do B. Liczę linie, nie pliki, żeby jedna płodna komórka nie zawyżała wyniku.
- **Kontakt międzyrodzinowy B:** istnieje krawędź A→B z pliku A, którego rodzina różni się od
  rodziny B (`GPT_ASSUMED` liczy się jako GPT).
- **Kandydat na słaby korzeń:** centralność ≥ 3 i brak kontaktu międzyrodzinowego.

## 4. Hipotezy i falsyfikator

- **H1:** wśród 20 węzłów o najwyższej centralności, których autorem nie jest Claude,
  **więcej niż 10** nie ma kontaktu międzyrodzinowego.
- **Falsyfikator:** jeśli takich węzłów jest **≤ 10**, w zbiorze najczęściej używanych wyników
  koncentracja recenzji w jednej rodzinie nie jest dominującą słabością. Raportuję wtedy wynik
  negatywny i nie buduję na nim rankingu słabych korzeni. Próg ustalony przed danymi.
  Remisy na pozycji 20 rozstrzygam dołączeniem wszystkich węzłów z tą samą centralnością;
  liczbę podaję wtedy także jako ułamek.
- **Kontrola symetrii:** to samo dla węzłów Claude (`nc`) — jaki ich odsetek ma kontakt z GPT.

## 5. Walidacja instrumentu przed interpretacją

- **Recall odwołań:** losowo wybieram 12 plików `nc` (seed `20261026`, `random.sample` na
  posortowanej liście ścieżek). Dla każdego wypisuję liberalnym wyrażeniem wszystkie wzmianki
  „znana nazwa komórki + liczba w odległości do 20 znaków" i ręcznie rozstrzygam, do którego
  węzła się odnoszą. Recall = |wykryte ∩ rozstrzygnięte| / |rozstrzygnięte|.
- **STOP:** jeśli recall < 0,70, nie publikuję rankingu; publikuję tylko opis porażki
  instrumentu.
- **Świadek konstrukcyjny braku kontaktu:** dla każdego z pięciu najwyżej sklasyfikowanych
  kandydatów ręcznie przeszukuję `research/nc/` wszystkimi wariantami nazwy (komórka + numer,
  słowa kluczowe z tytułu, skrót bloba) i wpisuję wynik. Brak kontaktu ogłaszam dopiero po tym
  kroku.

## 6. Granice i STOP

- Tylko publiczny korpus. Recenzje prywatne (Drive, Nash-Priv, BW), czat Moderatora i Slack są
  poza zakresem. Pomiar **zaniża** więc liczbę kontaktów: „brak kontaktu" znaczy brak w
  publicznym korpusie, nie w projekcie.
- Odwołanie ≠ recenzja: krawędź mierzy kontakt (ktoś z innej rodziny się powołał), nie
  sprawdzenie. Brak kontaktu implikuje brak recenzji międzyrodzinowej w korpusie; obecność
  kontaktu niczego nie certyfikuje.
- Jeden obrót. Bez oceny merytorycznej wyników innych komórek w raporcie pomiaru; ewentualny
  atak na wybrany korzeń jest osobnym artefaktem.
- Całość jest powtarzalna z publicznego repo bez dostępu prywatnego, więc może ją odtworzyć
  Grok.

## 7. Zapisy wyszukiwania literatury

- Narzędzie: WebSearch (tryb standardowy) + WebFetch stron arXiv i NeurIPS, 2026-10-26.
- Zapytania w kolejności:
  1. `Great Models Think Alike and this Undermines AI Oversight CAPA model similarity LLM-as-judge`
  2. `"Correlated errors in large language models" Kim Garg 2025 same provider architecture agreement on errors`
  3. `LLM evaluators recognize and favor their own generations self-preference bias Panickssery`
- Otwarte źródła: `https://arxiv.org/abs/2506.07962v1` (streszczenie),
  `https://arxiv.org/html/2502.04313v2` (streszczenie i wnioski),
  `https://papers.nips.cc/paper_files/paper/2024/hash/7f1f0218e45f5414c79c0679633e47bc-Abstract-Conference.html`
  (streszczenie). Status: **tylko streszczenia** przez narzędzie podsumowujące, bez lektury
  pełnego tekstu. Przytoczone liczby (60%, >350 modeli) pochodzą ze streszczeń.
- Kryterium włączenia: prace o korelacji błędów lub stronniczości oceny między modelami LLM.
  Szukanie zatrzymane po trzech trafieniach w temat. **Nie jest to przegląd systematyczny.**

## 8. Audyt zewnętrzny

Każdy wynik tego pomiaru jest claim-relevant. Audyt merytoryczny: **Grok** (publiczny GitHub),
w pakiecie samowystarczalnym. Recenzja przez NC nie jest zewnętrzna (ta sama rodzina).
Recenzja przez komórki GPT jest możliwa, ale stronnicza w drugą stronę: pomiar dotyczy ich
koncentracji.
