---
artifact_id: IW_BADACZ_XH_S5_ROT013_014_FRAME_DEPENDENCE_CROSS_FAMILY_CHECK_REVIEW_033_20261030
exposure: PUBLIC
claim_ceiling: CROSS_FAMILY_CHECK_[▷] / SOURCE_DEFINITIONS_READ / CONSTRUCTIVE_REMARK_[▷]_TRANSFORMATION_LAW / NOT_A_REFEREE_VERDICT / NO_VERDICT_ON_PUBLISHED_PAPER / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_CLAIM
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-30
origin_cell: BADACZ (wątek Claude)
document_type: REVIEW
result_class: RESULT
task_id: BADACZ-GPT-INDEPENDENT-REVIEW-010
selection: cel drugi z PREREG_030 (1a33bb3); testy ustalone w PREREG_032 (research/badacz/2026-10-30/IW_BADACZ_AUDIT_TESTS_PREREG_032_XH_S5_ROT013_014_20261030.md, commit f61b1ed), przed czytaniem ciał raportów
targets: XH-S5 ROT013 (research/xh-s5/2026-10-29/iw_xh_s5_rot013_prd2026_eq28_eq31_local_lorentz_frame_countercontrol_001.md, commit df5cdb2); XH-S5 ROT014 (research/xh-s5/2026-10-29/iw_xh_s5_rot014_temporally_compact_local_lorentz_unbounded_raw_reconnection_rate_001.md, commit 4da0c8e)
external_source: L. Comisso, F. A. Asenjo, „Reconnection of Gravitational Fields”, Phys. Rev. D 114, 084095 (2026), arXiv:2609.25241 (PDF czytany 30 X)
code: research/badacz/2026-10-30/code/xh_s5_rot013_014_frame_dependence_check.py (sha256 ab2ed2d60857b10a48efd560256630255674ed45782dc01fe5bcc79be9131191)
output_sha256: 5e37a8aae1ce2c011fa25481633c2392fa4dc90d7927586529a65c4fee61ae74 (xh_s5_rot013_014_frame_dependence_check.json)
---

# Sprawdzenie międzyrodzinowe XH-S5 ROT013/014: zależność diagnostyk rekoneksji od reperu

**Status:** `[▷]`. Claude sprawdza wyniki komórki GPT. To nie jest werdykt REC10/SW ani ocena
opublikowanej pracy.

## Wynik

1. **Matematyka XH odtworzona dokładnie (X1–X4).**
   - Oba korepery, kontrolny i aktywny, dają płaską metrykę `diag(−1, 1, 1, 1)`.
   - Dla reperu aktywnego `F¹ = dA¹` w `t = 0` w początku układu ma `F_ty = 2/5` i `F_xz = 7/10`.
     Wyznacznik `49/625`, rząd 4, jądro zerowe.
   - Reper kontrolny jest idealny: `i_u F¹ = 0`.
   - `∫ f = 1.2069003224378765`, a całka typu Eq. 31 wzdłuż `x = z = 0` wynosi `(2/5)·C = 0.48276…`.
   - ROT014: reper z `α = κ h(t) f(y)` pokrywa się z kontrolnym wszędzie tam, gdzie `h = 0`, a w `t = 0`
     daje `F_ty = κ f(y)`. Całka `|κ| C` nie jest więc ograniczona.
2. **X5, definicje w źródle (czytane w PDF arXiv:2609.25241): kontrprzykład trafia w faktyczną
   konstrukcję autorów.**
   - Eq. 3: `F^α̂_μν = ∂_μ A^α̂_ν − ∂_ν A^α̂_μ`. Reper traktowany jest jako „gravitational vector
     potential”, bez połączenia spinowego w `F`.
   - Praca nie mówi o niezmienniczości lokalnego Lorentza ani o regule wyboru reperu. Wymaga tylko reperu
     **dostosowanego** do kongruencji (`A^α̂_μ u^μ = δ^α̂_0`). Oba repery XH są dostosowane
     (`e⁰ = dt`, `u = ∂_t`).
   - Autorzy sami piszą, że Eq. 12 można czytać jako warunek propagacji reperu dostosowanego.
3. **X6, atrybucje.** XH-S5 nie przypisuje autorom niczego ponad tekst. Poprawnie oddaje ich rozróżnienie
   między lokalną nieidealnością a zmianą łączności płatów pola. Zaznacza też, czego nie dowodzi
   (separator Eq. 30, topologia, fizyka).
   - Jedno doprecyzowanie: ROT014 pisze, że prawdziwe obalenie wymagałoby wykazania, że dopuszczalne
     repery źródła obejmują te obroty. W klasie, którą źródło **jawnie** podaje (repery dostosowane, bez
     dodatkowej reguły), obejmują.
4. **Uwaga konstruktywna `[▷]`: skąd bierze się zależność od reperu i jaka minimalna reguła ją usuwa** (§1).

## 1. Prawo transformacji i minimalna reguła wyboru reperu

Dla reperu dostosowanego `i_u A^b = δ^b_0`. Stąd tożsamość, sprawdzona dokładnie w kodzie:

    R^a := i_u dA^a = L_u A^a.

Eq. 12 (`R = 0`) mówi więc, że reper jest **transportowany Liego** wzdłuż `u`, zgodnie z uwagą autorów.

Niech `A′ = Λ A` będzie czysto przestrzennym obrotem (`Λ^a_0 = δ^a_0`). Z `d(ΛA) = dΛ ∧ A + Λ dA`
oraz `dΛ^a_0 = 0`:

    R′^a = Λ^a_b R^b + u(Λ^a_b) A^b.

Kod sprawdza to prawo na 50 cyfrach w 10 losowych punktach dla dwóch pól `α(t, x, y, z)`; reszta
wynosi `≤ 6e-160`.

- **Wniosek 1.** Zależność od reperu bierze się wyłącznie z obrotu triady **wzdłuż** `u` (`u(Λ) ≠ 0`).
  Obrót zależny od położenia, ale stały wzdłuż `u`, daje `R′ = Λ R`. Reper idealny pozostaje wtedy
  idealny; dokładny test EXTRA3 dla dowolnego `α(x, y, z)` to potwierdza.
- **Wniosek 2.** Oba przykłady XH (ROT013: `α = 0.4 t f(y)`, ROT014: `α = κ t f(t) f(y)`) używają triad
  obracających się w czasie. Przy regule, która ustala obrót triady wzdłuż `u`, wszystkie dopuszczalne
  repery różnią się o `Λ` z `u(Λ) = 0`. Wtedy:
  - `R` z Eq. 22 transformuje się kowariantnie (`R′ = ΛR`), więc warunek idealności Eq. 12 nie zależy
    od reperu;
  - przykłady XH przestają być dopuszczalne;
  - w płaskiej czasoprzestrzeni z `u = ∂_t` wszystko jest idealne, czyli fałszywych pozytywów nie ma.
  - **Zastrzeżenie:** Eq. 28 (`R = F ζ` z gładkim `w = u − ζ ≠ 0`) zawiera pełne `F`. Przy statycznym, ale
    zależnym od położenia `Λ(x)` mamy `F′ = ΛF + dΛ ∧ A`. Niezależność Eq. 28 od reperu nie wynika więc
    z samego prawa dla `R` i zostaje otwarta.
  Naturalnym kandydatem na taką regułę są repery nierotujące (transport Fermiego–Walkera).
- **Wniosek 3 (ograniczenie).** Nawet przy takiej regule `R′ = ΛR` miesza składowe `α̂`. Całka Eq. 31
  liczona osobno dla każdej składowej zależy więc od statycznego `Λ(x)` zmieniającego się wzdłuż krzywej.
  Niezmienniczą wersją byłaby np. całka normy `|R|` albo maksimum po kierunkach w przestrzeni wewnętrznej.
- **Propozycja dla pytania recenzenckiego XH:** zapytać autorów, czy repery dostosowane mają być
  nierotujące (Fermi–Walker) albo w inny sposób mieć ustalony obrót wzdłuż `u`. Jeśli tak, kontrprzykłady
  XH nie mają zastosowania do Eq. 12, 22 i 28, a pozostaje pytanie o składowe Eq. 31. Jeśli nie, potrzebna
  jest inna reguła albo diagnostyka niezmiennicza.
- Nie sprawdzałem, co `R` mierzy przy reperach Fermiego–Walkera w czasoprzestrzeni zakrzywionej.
  Oczekuję związku z kinematyką kongruencji (`∇u`), ale to hipoteza `[▷]`, niesprawdzona.

## Czego nie sprawdziłem

- Wersji opublikowanej w PRD; czytałem PDF arXiv. Komórki ROT012 ani wcześniejszej pracy PRL 136,
  161401 (2026).
- Odwzorowania końców linii pola z ROT014 (całkowanie ODE), poza faktem, że po wyjściu z nośnika czasowego
  reper wraca do kontrolnego.
- Eq. 30 (separator) i topologii płatów pola.

## Literatura i dorobek projektu

- **Zewnętrzna:**
  - Comisso & Asenjo (2026), Eq. 2–5, 12, 22, 26–28, 30, 31;
  - lokalna transformacja Lorentza korepera i teleparalelizm kowariantny (Krššák & Pereira,
    EPJC 75:519, 2015, za XH);
  - transport Fermiego–Walkera (np. Misner, Thorne, Wheeler, *Gravitation*, §6.5).
- **Własna:** XH-S5 ROT012–014; moje doc 016 §1 (ukryte podobieństwo jako „cechowanie” obserwacji: ta sama
  lekcja, czyli świadectwo ma być niezmiennikiem albo mieć cechowanie ustalone przez źródło).
- Nowości nie zgłaszam.

## Odtworzenie

```text
pip install sympy==1.13.3 mpmath==1.3.0
python3 -I research/badacz/2026-10-30/code/xh_s5_rot013_014_frame_dependence_check.py --out <plik.json>
```

Kilka minut, głównie przez symboliczne `simplify`. Dwa przebiegi dały identyczny JSON. Wszystkie
`verdicts` mają wartość `true`.

## Moje błędy po drodze

- Pierwsza wersja testu tożsamości `i_u dA = L_u A` była tautologiczna, bo sprawdzała samą definicję
  `F`. Zastąpiłem ją testem dostosowania reperu (`A^a_t = δ^a_0`) i równości `i_u dA^a = ∂_t A^a`.
- Symboliczne sprawdzenie prawa transformacji z abstrakcyjnym `α(t, x, y, z)` zwróciło `false`, bo
  `simplify` nie domknął tożsamości trygonometrycznej. Numerycznie różnica wynosiła `2e-16`. Zastąpiłem
  je dokładną ewaluacją na 50 cyfrach dla dwóch konkretnych pól i podaję resztę jawnie.

## Powrót w trzech warstwach

- **Wynik:** matematyka XH-S5 ROT013/014 jest poprawna i trafia w faktyczną konstrukcję źródła.
  Zależność od reperu ma prostą przyczynę: obrót triady wzdłuż `u`. Usuwa ją reguła ustalająca ten obrót,
  np. Fermi–Walker; wtedy przykłady XH przestają być dopuszczalne.
- **Konfiguracja:** źródło w arXiv było dostępne, więc kluczowy test X5 (z czego zbudowane są równania
  autorów) dał się rozstrzygnąć tekstem, a nie domysłem.
- **Uczenie systemu:** przy kontrprzykładzie „zależność od cechowania” od razu wyprowadzam prawo
  transformacji. Wskazuje ono, która reguła wyboru cechowania usuwa problem; to przekształca falsyfikator
  w konkretne pytanie do autorów. Kandydat na regułę `[▷]`.

Wynik jest Claude'a, więc wymaga audytu spoza rodziny Claude.
