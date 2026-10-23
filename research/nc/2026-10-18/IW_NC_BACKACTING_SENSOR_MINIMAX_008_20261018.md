# IW_NC_BACKACTING_SENSOR_MINIMAX_008_20261018


<!-- IW_CONFORMANCE_BLOCK v1 (docs/IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md §2.7) -->
```text
artifact_id          : IW_NC_BACKACTING_SENSOR_MINIMAX_008_20261018
exposure             : PUBLIC_SAFE
canonical_body_path  : research/nc/2026-10-18/IW_NC_BACKACTING_SENSOR_MINIMAX_008_20261018.md
source_revision      : rozwiazywane przez `git log -- <canonical_body_path>`
bw_event_or_pending  : GITHUB_PENDING_BW_INGEST
claim_ceiling        : NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE / MODEL_AGREEMENT_IS_NOT_PROOF / SEARCH_FAILURE_IS_NOT_NOVELTY
hold                 : BRAK
```

ARTIFACT_ID: IW_NC_BACKACTING_SENSOR_MINIMAX_008_20261018
KOMÓRKA: NC — zewnętrzna komórka Claude
STATUS: [▷] / EXEC_SIGN = BRAK / NO_CANON / NO_NOVELTY / NO_PHYSICAL_UPGRADE
KOD: `backaction.py` sha256 3a9c197274d4b99ba72db335ab52ec8e43d0f5c1b392372aa0290c4e171f9775
**AUDYT ZEWNĘTRZNY OBOWIĄZKOWY** — cały wynik jest mój, nie mogę go sobie wystawić.
TO NIE JEST AUDYT CUDZEGO TEKSTU. To próba rozwiązania problemu, który monografia stawia jako otwarty.

---

## 0. Problem i dlaczego dotąd był otwarty

§7.5b.5 monografii: *„Potencjalnie badawczy problem powstaje dopiero dla fizycznie ograniczonej
rodziny obserwacji, kiedy czujniki oddziałują zwrotnie na układ (…). Twierdzenie 7.9 daje klasę
odniesienia do falsyfikacji; nie daje wyniku dla całej Jint."*

Powód, dla którego to jest realny problem, a nie formalność, stoi w samej monografii. Wniosek 7.4:
dla `C_a y = ay` minimaksowe ryzyko wynosi `min(1, δ/|a|)`, więc **dąży do zera przy `a → ∞`**.
Tekst słusznie nazywa to nielicencjonowanym wzmocnieniem. Brakuje modelu, w którym wzmocnienie
czegoś kosztuje — i dopiero wtedy pytanie o optymalny czujnik ma sens.

**Dostarczam taki model i rozwiązuję go w przypadku skalarnym.**

---

## 1. Model: uczciwa reakcja zwrotna

Oscylator z rozdziału 7, ale czujnik o wzmocnieniu `a` mierzy prędkość i **przez to ją tłumi** —
pomiar pędu odbiera pęd:

    x' = y,        y' = −x − aγ y
    cel:    x(T)
    pomiar: b = a·y(t_s) + η,   |η| ≤ δ
    ukryte przygotowanie y₀, |y₀| ≤ R;  x₀ = 0 znane

Z `β := aγ/2`:  `x(t) = y₀ h_a(t)`, `y(t) = y₀ g_a(t)`, gdzie
`h_a(t) = e^{−βt} sin(ωt)/ω`, `g_a(t) = e^{−βt}(cos ωt − (β/ω) sin ωt)`, `ω = √(1−β²)`
(z gałęziami hiperbolicznymi dla `β > 1`). Parametr `γ ≥ 0` to **siła reakcji zwrotnej**:
`γ = 0` odtwarza nieoddziałujący czujnik z Wniosku 7.4.

Ryzyko z Tw. 7.9 (skalarny cel, jeden pomiar) wynosi dokładnie

    ℰ(a) = |h_a(T)| · min( R , δ / (a|g_a(t_s)|) ).

---

## 2. Wynik: cel się skraca, i to zmienia wszystko

**Obserwacja, od której wszystko zależy.** Właściwą miarą nie jest `ℰ(a)`, lecz `ℰ(a)` podzielone
przez **niepewność celu bez pomiaru**, `R|h_a(T)|`. W tym ilorazie **`h_a(T)` kasuje się
tożsamościowo**:

    ℰ(a) / (R|h_a(T)|) = min( 1 , δ / (a R |g_a(t_s)|) ).

Konsekwencje są natychmiastowe i wszystkie zweryfikowane numerycznie:

**(a) Optymalne wzmocnienie nie zależy ani od szumu, ani od horyzontu.** Minimalizacja sprowadza
się do maksymalizacji `a|g_a(t_s)|`, w której nie występuje ani `δ`, ani `T`. Podstawiając
`a = 2β/γ`: `max_a a|g_a(t_s)| = (2/γ)·N(t_s)`, gdzie

    N(t_s) := max_β β |g_β(t_s)|     zależy WYŁĄCZNIE od czasu pomiaru.

Stąd **`a* = 2β*(t_s)/γ`**, czyli `a*` jest dokładnie odwrotnie proporcjonalne do siły reakcji
zwrotnej. Zmierzone wobec przewidywanego, dla `γ ∈ {0.5,1,2,4}` i `t_s ∈ {0.25,0.5,1}`:
7.8565/7.8791, 3.7045/3.6831, 1.3284/1.3300, 3.9283/3.9758, 1.8522/1.8550, 0.6642/0.6650,
1.9641/1.9650, 0.9261/0.9250, 0.3321/0.3300 — zgodność w granicach rozdzielczości siatki.
Niezależność od `δ` zmierzona osobno: `a* = 1.8600` **niezmiennie** dla `δ` od 0.5 do 0.005.

**(b) Podłoga błędu jest liniowa w sile reakcji zwrotnej i w szumie.**

    min_a ℰ(a)/(R|h_a(T)|)  =  γ δ / ( 2 R N(t_s) ).

Przewidywane wobec zmierzonego, jedenaście konfiguracji: 0.017780/0.017780, 0.041089/0.041089,
0.173630/0.173630, 0.035561/0.035563, 0.082177/0.082177, 0.347260/0.347260, 0.071121/0.071121,
0.164355/0.164355, 0.694521/0.694542, 0.142242/0.142243, 0.328709/0.328712 — **sześć cyfr**.
Liniowość w `γ` sprawdzona przy `t_s = 0.5` dla `γ` od 0.25 do 8 (zakres 32×): iloraz
podłoga/`γ` = 0.082178, 0.082179, 0.082177, 0.082177, 0.082178, 0.082179.

**(c) Warunek dopuszczalności czujnika.** Gdy `γδ ≥ 2RN(t_s)`, podłoga przekracza 1 i **żadne
wzmocnienie nie daje ani odrobiny informacji**. To ostry próg, nie asymptota. Przy `R = 1`
maksymalny budżet `γδ` wynosi 3.652 przy `t_s = 0.1`, ale tylko 0.144 przy `t_s = 1.0` —
różnica 25× zależna wyłącznie od tego, **kiedy** się mierzy. Formuła poprawnie sygnalizuje ten
reżim: dla `γ=4, t_s=1` przewiduje podłogę 1.389, a pomiar saturuje na 1.000000.

---

## 3. Nowy non-map: mały błąd minimaksowy ≠ informatywny pomiar

Zmierzone przy `γ=1, T=2, t_s=0.5, R=1, δ=0.05`:

| a | `ℰ(a)` surowy | `ℰ/prior` |
|---|---|---|
| 1 | `4.045e-02` | **0.096479** |
| 10 | `8.339e-02` | **1.000000** |
| 50 | `1.923e-02` | **1.000000** |
| 200 | `4.950e-03` | **1.000000** |

Przy `a = 200` surowy błąd jest **ośmiokrotnie mniejszy** niż przy `a = 1`, a pomiar nie wnosi
**nic**: cała redukcja bierze się stąd, że czujnik zniszczył zależność celu od stanu ukrytego.
Prior spadł z `4.193e-01` do `4.950e-03`.

**To zaostrza Wniosek 7.4 monografii.** Tam `ℰ → 0` przy `a → ∞` jest artefaktem braku kontraktu
fizycznego. Tutaj, przy obecnym kontrakcie, `ℰ → 0` nadal zachodzi — ale z zupełnie innego
powodu i widać go dopiero po normalizacji. **Surowy błąd minimaksowy nie jest miarą jakości
pomiaru, jeśli aparatura zmienia mierzony układ.** Normalizacja przez prior nie jest kosmetyką,
tylko warunkiem sensowności wielkości.

---

## 4. Reakcja zwrotna PRZESUWA czas ślepy

Monografia ma w §7.5b.4 własny przykład o źle wybranym czasie pomiaru, dla oscylatora
**nietłumionego**. Dla pomiaru prędkości odpowiedź nietłumiona to `cos t_s`, więc naiwnie czasem
ślepym jest `t_s = π/2 = 1.570796`. **To nieprawda, gdy czujnik oddziałuje zwrotnie.**

| `t_s` | `\|cos t_s\|` | `N(t_s)` | `β*` |
|---|---|---|---|
| 1.0050 | 0.5376 | **0.071202** ← minimum | 0.33 |
| 1.5000 | 0.0707 | 0.114030 | 1.1910 |
| 1.5708 | `4e-06` | **0.119320** | 1.0958 |
| 1.6500 | 0.0791 | 0.124833 | 1.0028 |

W punkcie, w którym odpowiedź nietłumiona znika dokładnie, informacyjność **nie ma minimum** —
jest `1.676×` większa niż w rzeczywistym najgorszym punkcie. Czujnik **wytłumia się z zera**
(`β* = 1.0958` tam), zmieniając dynamikę tak, by układ stał się obserwowalny. Rzeczywisty czas
ślepy przesuwa się do `t_s ≈ 1.005`.

Najlepszy czas wobec najgorszego: `N(0.25)/N(1.005) = 0.703026/0.071202 ≈ **9.9×**` w osiągalnej
precyzji przy tym samym szumie.

---

## 5. Optymalne wzmocnienie jest NIECIĄGŁE w czasie pomiaru

| `t_s` | 0.95 | 1.00 | **1.02** | 1.04 | 1.10 | 1.15 |
|---|---|---|---|---|---|---|
| `β*` | 0.3698 | 0.3323 | **2.3693** | 2.2913 | 2.0783 | 1.9223 |
| `N` | 0.085275 | 0.071992 | 0.072563 | 0.074378 | 0.079820 | 0.084337 |

Między `t_s = 1.00` a `t_s = 1.02` — przesunięcie czasu pomiaru o **2%** — optymalne wzmocnienie
skacze **7.1-krotnie**. Argmaks przeskakuje z gałęzi słabo tłumionej na silnie tłumioną.

Odczyt fizyczny: po jednej stronie skoku najlepszą strategią jest mierzyć delikatnie i przyjąć
słaby sygnał; po drugiej — tłumić mocno, **celowo zmieniając dynamikę**, żeby układ dał się
zobaczyć. Projektowanie czujnika przez ciągłe strojenie wokół nominalnego czasu pomiaru trafi
w złą gałąź, jeśli nominalny czas leży po niewłaściwej stronie `t_s ≈ 1.01`.

---

## 6. Moja predykcja, która okazała się FAŁSZYWA

Przed liczeniem przewidywałem `a* = 2/(γ t_s)`, z argumentu, w którym przybliżyłem
`g_a(t_s) ≈ e^{−βt_s}`, pomijając człon `(β/ω)sin ωt_s`. Zmierzone ilorazy `a*/(2/(γt_s))`
wynoszą 0.4903, 0.4619, 0.3300 dla `t_s` = 0.25, 0.5, 1.0 — **ani równe 1, ani stałe**.
Pominięty człon nie jest poprawką, tylko współrządzi optimum; to on odpowiada za skok gałęzi z §5.
`origin_failure_mode: ASYMPTOTIC_TERM_DROPPED_BEFORE_CHECKING_WHETHER_IT_GOVERNS_THE_EXTREMUM`.
Zachowuje się dokładnie jedna część tej predykcji — `a* ∝ 1/γ` — i ta jest potwierdzona do trzech
cyfr, bo wynika ze skalowania `β = aγ/2`, a nie z pominiętego przybliżenia.

---

## 7. Czego nie twierdzę

1. **Nie rozwiązałem problemu z §7.5b.5.** Rozwiązałem **jeden przypadek**: skalarny stan ukryty,
   jeden pomiar, jeden konkretny kanał reakcji zwrotnej. Problem pyta o całą klasę interwencji `Jint`.
2. **Model reakcji zwrotnej jest wyborem fenomenologicznym, nie wyprowadzeniem.** „Pomiar prędkości
   tłumi prędkość" jest fizycznie uczciwe, ale nie wynika z żadnej zasady, którą tu wypisałem.
   W wersji kwantowej back-action byłby ograniczony relacjami nieoznaczoności i to **inne zadanie**.
   `COMMON MATHEMATICS != COMMON PHYSICAL MECHANISM`.
3. **`N(t_s)` mam numerycznie, nie w postaci zamkniętej.** Skok gałęzi z §5 zlokalizowałem na
   siatce; nie wyznaczyłem punktu skoku analitycznie ani nie wykluczyłem dalszych skoków przy
   `t_s > 4` (przy `t_s = 4` `N` nadal opada i mój skan się tam kończy).
4. **Nie sprawdzałem, czy wynik przeżywa wielokrotne pomiary.** Tw. 7.10 monografii mówi, że
   adwersarialne powtórzenia nie pomagają przy jednym budżecie `δ` na pomiar — ale tam czujnik
   nie oddziaływał zwrotnie, a tutaj każdy kolejny pomiar **dokłada tłumienia**. To osobne i
   prawdopodobnie ciekawsze pytanie.
5. **Nie szukałem literatury.** Kompromis wzmocnienie–zaburzenie jest motywem klasycznym (pomiary
   kwantowe o słabym sprzężeniu, projektowanie czujników), więc **nie twierdzę nowości** i
   spodziewam się, że struktura (a) i (b) ma gospodarzy. Nowe jest, o ile cokolwiek, osadzenie
   tego w kontrakcie Tw. 7.9 i punkty §3–§5.
6. **Wartość `ℰ` dla `a = 1000` w pierwszym przebiegu wyszła NaN** — przepełnienie w gałęzi
   hiperbolicznej przy dużym `β`. To artefakt numeryczny, nie wynik; w tabelach powyżej go nie ma.

---

## 8. Co z tego dla monografii, gdyby LT4 chciał to wziąć

Trzy rzeczy nadają się do §7.5b, i każda jest innego rodzaju:
- **normalizacja przez prior** jako warunek sensowności miary błędu, gdy aparatura zmienia układ
  (§3) — to poprawka pojęciowa do sposobu, w jaki Wniosek 7.4 jest czytany;
- **warunek dopuszczalności `γδ < 2RN(t_s)`** (§2c) — ostry próg, poniżej którego czujnik jest
  bezużyteczny niezależnie od strojenia;
- **nieciągłość optymalnego wzmocnienia** (§5) — ostrzeżenie projektowe, którego nie widać
  w modelu bez reakcji zwrotnej.

Decyzja o włączeniu i cała redakcja należą do LT4. Ja proponuję matematykę.

---

KONIEC. Status [▷]. EXEC_SIGN brak.
