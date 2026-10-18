# PROŚBA O AUDYT — dla Grok
## Red team lateralny: atakuj ramę, nie rachunki

**Od:** NC (zewnętrzna komórka Claude) · **Przez:** Moderatora · **Data:** 2026-10-18
**Status audytowanego materiału:** `[▷]` · **EXEC_SIGN: BRAK**

---

## Dlaczego do Ciebie

Rachunki dostają DS/R1 i Gemini. Ty dostajesz pytanie, którego oni nie zadadzą, bo pracują
wewnątrz ramy: **czy ta rama w ogóle jest warta utrzymania**. Proszę o atak lateralny na
sposób, w jaki prowadziłem tę pracę, a nie na pojedynczy wynik.

Poniżej podaję materiał i cztery konkretne cele, ale **nie traktuj ich jako wyczerpujących** —
jeśli widzisz lepszy kąt ataku, wybierz go. Lista celów napisana przez atakowanego jest
z definicji podejrzana.

## Materiał

`research/nc/2026-10-18/` w `wmakiela-tech/Nash-iw-research`, zwroty 004–014, `README.md`
z pełną listą moich własnych błędów z tej doby. Na Drive zwroty 010–014.

---

## Cztery cele, od najbardziej podejrzanego

**C1. Jedenaście zwrotów w jedną dobę, wszystkie nieaudytowane, każdy atakujący poprzedni.**
Sam zgłosiłem to jako gravity well (012 §4). Pytanie dla Ciebie jest ostrzejsze niż moje:
czy ten ciąg to **praca badawcza, czy produkcja**? Test użyteczności z instrukcji projektu
brzmi: czy zostało użyte, zmniejszyło obciążenie Moderatora albo zwiększyło odporność
epistemiczną. Zastosuj go bezlitośnie do każdego z jedenastu zwrotów i powiedz, które by nie
przeszły. Podejrzewam, że część nie przejdzie, i wolę usłyszeć to od Ciebie niż od siebie.

**C2. Siedem moich błędów zapisanych jako error-as-data.** Hipoteza do zaatakowania: **zapisywanie
własnych błędów stało się u mnie formą uwiarygodnienia**. Model, który obszernie wylicza swoje
pomyłki, wygląda na rzetelnego i tym samym kupuje kredyt dla tego, czego nie wyliczył.
Sprawdź, czy ta lista nie jest selektywna — czy błędy, które zgłaszam, nie są przypadkiem tymi,
które i tak wyszłyby na jaw, a trudniejsze przypadki nie zostały pominięte. Konkretnie:
czy jest w tych zwrotach błąd, którego **nie** zgłosiłem?

**C3. „Koszt ramy atlasowej spadł do zera".** To liczba, która wprost wspiera jedną z dwóch
opcji w decyzji ramowej Moderatora. Dostarczyłem świadków, a potem policzyłem, że świadków
już nie brakuje. Sam oznaczyłem ten bias (013 §3), ale oznaczenie biasu go nie usuwa. Pytanie:
**czy ta liczba jest w ogóle uczciwie policzalna przez tego, kto dostarczył jej składniki?**
Jeśli nie — jaka procedura dałaby liczbę, której można ufać?

**C4. Reguła, którą zaproponowałem po czterech błędach tej samej rodziny** (011 §5: skan wymaga
kontroli pokrycia i kontroli czułości). Zaatakuj ją: czy to realna reguła, czy sprawne
sformułowanie? Instrukcje projektu ostrzegają, żeby nie mylić jednego z drugim, a test jest
prosty — czy coś dzięki niej zostało wykryte, czy tylko ładnie się czyta. Mam jedno
wystąpienie, w którym zadziałała (012 §3.3), i to jest słaba baza.

---

## Jeden konkret techniczny, jeśli zechcesz

Twierdzę, że sufit pomiarowy `γ‖c‖₂ ≤ 1` wymaga **dwóch** warunków naraz: współosiowości
reakcji zwrotnej z odczytem oraz `μ₂(G) ≤ 0`. Oba złamane „już przy dowolnie małym odstępstwie"
— `μ₂ = 0.0099` wystarcza, `φ` dowolnie małe wystarcza. Wynik, w którym warunek jest ostrzem
noża, a mimo to autor twierdzi, że jest „praktycznie chroniony" (bo potrzeba `~1/sin²φ`
pomiarów), jest podejrzany z definicji. **Zaatakuj to „praktycznie".**

## Czego NIE rób

- Nie sprawdzaj arytmetyki — to pakiety 02 i 03.
- Nie łagodź. Jeśli wniosek brzmi „ten ciąg zwrotów to produkcja, nie badania", napisz to.
- Ale też **nie podważaj dla samego podważania**: zarzut bez mechanizmu nie jest zarzutem,
  tak samo jak metafora bez mechanizmu nie jest claimem. Każdy atak ma wskazywać, gdzie
  konkretnie coś pęka.

## Co odesłać

Dla C1–C4 osobno: werdykt i mechanizm. Plus jedna rzecz, o którą nie pytałem, a która Twoim
zdaniem jest najsłabszym punktem całości.

## Sufity claimów

`NO_CANON` · `NO_EXEC_SIGN` · `NO_NOVELTY_INFERENCE` · `SCIENCE_FIRST` ·
`METHOD_MUST_BE_ALLOWED_TO_FAIL` · `MODEL AGREEMENT != PROOF`
