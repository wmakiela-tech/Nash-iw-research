# IW_NC_LT4_NONMAP_LAYER_AUDIT_005_20261018


<!-- IW_CONFORMANCE_BLOCK v1 (docs/IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md §2.7) -->
```text
artifact_id          : IW_NC_LT4_NONMAP_LAYER_AUDIT_005_20261018
exposure             : PUBLIC_SAFE
canonical_body_path  : research/nc/2026-10-18/IW_NC_LT4_NONMAP_LAYER_AUDIT_005_20261018.md
source_revision      : rozwiazywane przez `git log -- <canonical_body_path>`
bw_event_or_pending  : GITHUB_PENDING_BW_INGEST
claim_ceiling        : NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE / MODEL_AGREEMENT_IS_NOT_PROOF / SEARCH_FAILURE_IS_NOT_NOVELTY
hold                 : BRAK
```

ARTIFACT_ID: IW_NC_LT4_NONMAP_LAYER_AUDIT_005_20261018
KOMÓRKA: NC — zewnętrzna komórka Claude, rola: audytor
OBIEKT: monografia, DRIVE 1cn97_kO65BcJRRWQrvrL9fKlEYBT3PHg6BJItn1Q4FQ, 161 432 znaków, rozdziały 1–7
STATUS: [▷] / EXEC_SIGN = BRAK / NO_CANON / NO_NOVELTY_INFERENCE / SOURCE_FIRST
AUTORSTWO I DECYZJA: LT4. Dokument jest audytem warstwy, nie propozycją redakcyjną.
POPRZEDZA: 004 (prior-art subtraction), DRIVE 1Ih2uvIgG-LITYCU5aVr7YYvbb2x1aUDm
KOD: `witness.py` sha256 4aa74e161e6714b671c666d852ddec3162e54a4bdbb7f750104bc4fb90bbfc1c

---

## 0. Po co ten zwrot — testuję własną hipotezę, nie bronię jej

W 004 postawiłem hipotezę ramową: że realnym produktem monografii nie są twierdzenia, lecz
**atlas tego, co się nie przenosi**. Oparłem ją na policzeniu 53 zdań negatywnych.

Policzenie nie jest audytem. **Non-map jest twierdzeniem matematycznym** — „X nie implikuje Y" —
i wymaga świadka dokładnie tak samo jak twierdzenie pozytywne. Jeżeli warstwa non-mapów jest
w większości nieudowodnionymi przestrogami, moja hipoteza upada, a monografia jest w gorszym,
nie lepszym stanie, niż sugerowało 004. Dlatego ten zwrot atakuje moją własną tezę.

Tej warstwy nikt nigdy nie audytował **jako klasy**: SW sprawdza dowody twierdzeń, INT7 mosty,
MT13 spójność programową, Rec9 kwantyfikatory. Non-mapy przechodziły pojedynczo, przy okazji.

---

## 1. Korekta mojego własnego licznika z 004

Siatka, której użyłem w 004, była za wąska. Szersza, obejmująca także „nie przenosi / nie
zapewnia / nie gwarantuje / nie stanowi / nie daje / nie wyznacza / nie zastępuje / nie musi /
nie cofa / nie rozstrzyga", daje po deduplikacji **96 unikalnych zdań negatywnych**, nie 53.

Podaję obie liczby z ich siatkami, bo różnica jest metodologiczna, nie merytoryczna: 53 to dolne
oszacowanie, 96 górne. Nagłówkowa liczba w 004 była zaniżona i tak ją należy czytać.

---

## 2. Klasyfikacja wszystkich 96

Kategorie, rozłączne:

| kat. | znaczenie | liczba |
|---|---|---|
| **W** | ma świadka — jawna konstrukcja albo kontrprzykład przy zdaniu lub obok | **44** |
| **D** | wyprowadzalne — wynika natychmiast z twierdzenia udowodnionego w tekście | **10** |
| **T** | typowanie — uwaga o poprawności typu, definicji, kalibracji; prawdziwa z typowania, nie wymaga świadka | **15** |
| **S** | samoograniczenie — tekst ogranicza zasięg własnego wyniku („ten przykład nie dowodzi…") | **9** |
| **A** | **stwierdzone bez świadka** — matematyczna nieimplikacja bez konstrukcji i bez wyprowadzenia | **12** |
| **P** | programowe — zapis, co przyszłe twierdzenie musi wyszczególnić (problemy otwarte) | **5** |
| — | częściowe (rozdzielenie trzech warunków A/B/C, świadek tylko dla części par) | 1 |

Razem 96.

**Odczyt: 54 z 96 (56%) ma świadka albo wyprowadzenie. 24 (25%) to typowanie, samoograniczenia
i zapisy programowe, które świadka nie potrzebują. 12 (12,5%) to realne dziury.**

Warstwa non-mapów jest więc w większości udowodniona, a nie przestrzegawcza. To **wzmacnia**
hipotezę z 004 — ale dopiero po §3, bo deklaracja świadka to nie to samo co działający świadek.

---

## 3. Czy świadkowie działają — próbka dziesięciu, policzona niezależnie

Wziąłem dziesięciu świadków z pięciu rozdziałów i policzyłem każdego od zera, porównując
z wartością, którą podaje tekst. **Dziesięć na dziesięć przechodzi.**

| świadek | co twierdzi tekst | moja wartość |
|---|---|---|
| R1 §3, defekt kompresji | `c(ST)=2`, `c(TS)=1` przy `c(S)=c(T)=1` | 2 i 1; tożsamość `PSQTJ = c(ST)−c(S)c(T) = 1` |
| R1 Kontrprz. 1 | `BC=0`, `BDC=1`, `K(t)=t` | 0, 1; `K(0.5)=0.500000`, `K(1)=1.000000`, `K(2)=2.000000` |
| R1 Kontrprz. 3 | wszystkie `τBD^kC=0`, `τABC≠0`, `τx(t)=1+t³/6+O(t⁶)` | momenty `0.000000e+00` dla k=0..3; `τABC=1`; przy t=0.1 odchyłka od `1+t³/6` wynosi `1.39e-09` |
| R2 Przykł. 2.4 | `ω(δ)=(4δ)^{1/3}` dokładnie | zmierzone 0.584800 / 0.928300 / 1.259900 / 1.587400 / 2.000000 wobec wzoru 0.584804 / 0.928318 / 1.259921 / 1.587401 / 2.000000 |
| R2 §2.3 | `[0,2π)→S¹` ciągła bijekcja, `τ̄` nieciągła w 1 | `τ̄(y_n) → 6.283085` przy `τ̄(1)=0` |
| R3 §3.9 | stany Bella, te same marginesy, po CNOT `\|+⟩⟨+\|` i `\|−⟩⟨−\|` | marginesy A przed: oba `I/2`; po CNOT `⟨+\|ρ_A\|+⟩ = 1.000000` dla Φ⁺ i `⟨−\|ρ_A\|−⟩ = 1.000000` dla Φ⁻ |
| R5 Tw. 5.2 | `Φ₂ = id`, `Φ₁∘Φ₁ = Φ₁ ≠ id` | `Φ₁(ρ₀) = I/2`, `Φ₂(ρ₀) = ρ₀`, `Φ₁(Φ₁(ρ₀)) = I/2` |
| R5 Tw. 5.6 | transpozycja: wartość własna `−1/2` operatora Choi | widmo `[−0.5, 0.5, 0.5, 0.5]` |
| R6 Tw. 6.5 | iloraz `e^{r(T−h)}`, „przekracza czynnik 54" | `54.598150` zmierzone, `e⁴ = 54.598150` — zgodność do sześciu cyfr |
| R7 Przykł. 7.3 | `M(π)=0`, `q(π,1)=−2` | `M(π)=1.2e-16`, `q(π,1)=−2.000000000` |

**JEDEN Z TYCH TESTÓW BYŁ POCZĄTKOWO MÓJ BŁĘDNY, NIE TEKSTU.** Przy świadku z R3 §3.9 policzyłem
marginał **B** zamiast **A** i dostałem dla obu stanów Bella to samo `|0⟩⟨0|`, co wyglądało na
porażkę świadka monografii. Zatrzymało mnie to, że wynik był zdegenerowany: `⟨+|ρ|+⟩ = ⟨−|ρ|−⟩ =
0.5` dla obu, czyli test nie rozróżniał niczego, a teza była ostra. Po przeliczeniu właściwego
marginału świadek wychodzi dokładnie. `origin_failure_mode: WRONG_SUBSYSTEM_TRACED_OUT`.
Zapisuję, bo o włos nie zgłosiłem fałszywego defektu, i bo złapała to nie reguła, tylko
podejrzliwość wobec zdegenerowanej liczby.

---

## 4. Dwanaście dziur — i to, że nie są rozrzucone losowo

To jest wynik tego zwrotu. Lista, a potem wzorzec.

**(a) Świadek istnieje u gospodarza, tekst go nie cytuje — 3 pozycje.**
1. §5.2: „Założenie o stałym `σ_E` jest istotne" — gdy przygotowanie środowiska jest skorelowane
   z wejściem, redukcja nie musi być CP. To **dojrzała literatura** (niecałkowita dodatniość
   dynamiki zredukowanej przy początkowych korelacjach układ–środowisko; Pechukas, Shaji–Sudarshan
   i kontynuacje). Zakres mojej weryfikacji: potwierdziłem wyszukiwaniem, że to ustalony obszar
   literatury; nie otworzyłem pojedynczej pracy i nie przypisuję konkretnego twierdzenia.
2. §3.6: „w nieskończonym wymiarze sama minimalność przybliżona nie zapewnia ograniczonego
   izomorfizmu z ograniczoną odwrotnością" — nieskończeniewymiarowa teoria realizacji zna tę
   przeszkodę. **Nie szukałem**; zgłaszam jako kandydata do odnalezienia gospodarza, nie jako
   ustalenie.
3. §3.10: „równość zbiorów możliwych trajektorii nie musi oznaczać równości praw na historiach" —
   rozkłady o wspólnym nośniku i różnych wagach. Świadek jednolinijkowy, nie podany. **Nie szukałem.**

**(b) Świadek istnieje w zwrotach projektu, ale nie w manuskrypcie — 1 pozycja.**
4. §7.8: „splatanie rachunku funkcyjnego nie daje splatania różniczek i dziedzin — pierwsze nie
   daje drugiego". INT7 przeanalizował dokładnie ten rozdział kontraktów (transport spektralny
   kontra łańcuchowy) i wymaga obu osobno. W manuskrypcie zdanie stoi bez świadka. To jest
   **najtańsza do zamknięcia pozycja z całej dwunastki** — materiał istnieje, trzeba go wciągnąć.

**(c) Bez znanego mi świadka — 8 pozycji.**
5. §1.7: redukcja jądra przez `(D, C, τB)` „nie oznacza jeszcze minimalności całej zamkniętej
   odpowiedzi `x₀ ↦ τx(t)`, w której uczestniczy także `A`".
6. §1.10: „Nie wystarczy domagać się analityczności tylko dla `t > 0`" — podany jest powód
   (potrzebna jednoznaczność rozwinięcia w zerze), nie ma świadka.
7. §2.8: „Losowa redukcja informacji i fizyczna eliminacja sektora Hilberta nie są tym samym
   działaniem."
8. §2.9: „Równoważność realizacji minimalnych z dokładnością do podobieństwa nie jest tożsamością
   wewnętrznej zmiennej fizycznej."
9. §3.5: „Równość odpowiedzi nie wyznacza automatycznie mikroskopowych współrzędnych stanów
   ukrytych." (bliźniacze z 8)
10. §4.7: „nie wynika stąd, że skompresowane reprezentacje grupowe lub kwantowe supermapy
    posiadają analogiczną homotopię" — powód podany (brak zadeklarowanego różniczkowania),
    świadka brak.
11. §5.10: „Nierówność praw dla dwóch instrumentów nie jest dowodem nieokreślonej przyczynowości."
12. §7.2: półgrupa `V_t` — „Nie wynika stąd jej ciągłość, całkowita dodatniość ani równoważność
    procesów z interwencjami." To **trzy** nieimplikacje w jednym zdaniu, żadna nie ma świadka.

**WZORZEC.** Osiem z dwunastu dziur leży dokładnie na granicy, którą projekt sam pilnuje
firewallem `COMMON MATHEMATICS != COMMON PHYSICAL MECHANISM`:
- przejście matematyka → interpretacja fizyczna: pozycje 7, 8, 9, 11 (cztery);
- przejście skończony → nieskończony wymiar: pozycje 2, 6 (dwie);
- przejście jeden formalizm → inny (kompleksy łańcuchowe → supermapy; półgrupa → proces
  z interwencjami): pozycje 10, 12 (dwie).

Pozostałe cztery (1, 3, 4, 5) są wewnątrzmatematyczne i w zasięgu jednego kontrprzykładu.

**Czyli: atlas jest solidny tam, gdzie jest matematyczny, i cienki dokładnie tam, gdzie
przekracza reżim.** To nie jest przypadek — to miejsce, w którym świadka najtrudniej
skonstruować, bo trzeba najpierw otypować obie strony. I to jest dokładnie ta granica, której
pilnowanie monografia deklaruje jako swoją oś.

---

## 5. Co z tego wynika dla decyzji ramowej z 004 §6

Hipoteza „atlas granic" **przetrwała test**, ale w postaci ostrzejszej i mniej wygodnej, niż ją
postawiłem:

- Warstwa non-mapów jest w 56% udowodniona albo wyprowadzona, a próbka świadków wychodzi
  10/10. To nie jest zbiór przestróg — to zbiór twierdzeń negatywnych z konstrukcjami.
- Ale atlas **ma dwanaście dziur, osiem z nich na granicach reżimu**, czyli dokładnie tam, gdzie
  byłby najcenniejszy. Atlas, który jest kompletny w środku i dziurawy na brzegach, jest
  atlasem o odwróconej wartości.
- Wniosek operacyjny jest więc odwrotny do „ogłośmy ramę i gotowe": **jeżeli rama ma brzmieć
  „atlas granic przenoszenia", to warunkiem jest zamknięcie tych dwunastu, a nie ich
  przemilczenie.** Dwanaście świadków to praca policzalna i skończona — znacznie mniejsza niż
  dopisanie ośmiu nowych twierdzeń hierarchii B, których i tak nie da się dopisać (każde
  elementarne trafia do A).

Nadal nie rozstrzygam ramy. Dostarczam teraz drugą liczbę: przy ramie twierdzeniowej brakuje
nieokreślonej liczby wyników, przy ramie atlasowej brakuje **dwunastu konkretnych świadków**,
z czego jeden jest już napisany w zwrocie INT7 i trzy mają gospodarzy do odnalezienia.

---

## 6. Czego nie zrobiłem i gdzie spodziewam się sporu

1. **Klasyfikacja 96 pozycji jest moja i jest sądem.** Granica W/D jest ostra, granica T/A nie.
   Jeżeli ktoś przesunie pięć pozycji z T do A, dziur jest siedemnaście, nie dwanaście, a wniosek
   z §5 wzmacnia się. Jeżeli przesunie pięć z A do T, jest siedem i wniosek słabnie. **Spodziewam
   się sporu dokładnie na tej granicy i uważam go za potrzebny.**
2. **Sprawdziłem dziesięciu świadków z czterdziestu czterech.** Próbka była dobrana pod
   sprawdzalność (zamknięte wzory, małe wymiary), a nie losowo — więc nie jest to oszacowanie
   odsetka poprawnych świadków w całej warstwie. Trzydziestu czterech nie sprawdziłem.
3. **Dla ośmiu z dwunastu dziur nie szukałem gospodarza w literaturze.** Mówię „bez znanego mi
   świadka", nie „bez świadka". `SEARCH FAILURE != NOVELTY` i tym bardziej nie oznacza braku.
4. Nie oceniałem, czy poszczególne non-mapy są *potrzebne* — tylko czy są udowodnione. Non-map
   udowodniony, lecz trywialny, jest nadal balastem redakcyjnym i to jest osąd LT4.
5. Nie dotykałem niczego opartego na moich wynikach J3 — nadal `[▷]`, w audycie zewnętrznym.

KOD: `witness.py`, dziesięć bloków, bez tekstu interpretacyjnego w `print`; tabele osobno,
odczyty dopisane po fakcie.

---

KONIEC. Status [▷]. EXEC_SIGN brak. Audyt klasyfikacji z §2 i §4 obowiązkowy per ANTI-SELF-SEALING.
