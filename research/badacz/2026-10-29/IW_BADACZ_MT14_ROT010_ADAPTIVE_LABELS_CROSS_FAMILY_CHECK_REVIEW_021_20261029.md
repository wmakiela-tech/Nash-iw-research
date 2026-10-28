---
artifact_id: IW_BADACZ_MT14_ROT010_ADAPTIVE_LABELS_CROSS_FAMILY_CHECK_REVIEW_021_20261029
exposure: PUBLIC
claim_ceiling: CROSS_FAMILY_CHECK_[▷] / PROOFS_VERIFIED_LINE_BY_LINE / EXACT_CONTROLS_REPRODUCED_INDEPENDENTLY / ADDENDUM_[▷]_MATURE_HOSTS_BAIRE_BORSUK_ULAM / NOT_A_REFEREE_VERDICT / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_CLAIM
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-29
origin_cell: BADACZ (wątek Claude)
document_type: REVIEW
result_class: RESULT
task_id: BADACZ-GPT-INDEPENDENT-REVIEW-005
selection: PREREG_018, pozycja 3 (research/badacz/2026-10-29/IW_BADACZ_REVIEW_TARGET_SELECTION_PREREG_018_20261029.md, commit a6535f1)
target: research/mt14/2026-10-28/iw_mt14_rot010_adaptive_finite_label_identifiability_and_sharp_information_budget_001.md (autor MT14)
code: research/badacz/2026-10-29/code/mt14_rot010_adaptive_label_check.py (sha256 cd08253a6a264cf33440beb0673e94b0459b795905ead9031de7809dfee4c27d)
output_sha256: 7d735433aff49748ba629512c77f671dfad9d2a9c3e63a7dcf43a7ffe019c467 (mt14_rot010_adaptive_label_check.json)
---

# Recenzja międzyrodzinowa MT14 ROT010: skończone etykiety adaptacyjne a identyfikacja źródła

**Status:** `[▷]`. Sprawdzenie przez Claude'a wyniku komórki GPT. Nie jest to werdykt REC10/SW.
Kod napisałem z publicznego tekstu, bez archiwum autora.

## Wynik

1. **Wszystkie cztery twierdzenia są poprawne.** Dowody sprawdziłem krok po kroku.
   - T010.1: niezmienniczość obszaru po dopisaniu zer.
   - T010.2: przypadki `x₈ ≠ 0` i `x₈ = 0`.
   - T010.3: pokrycie odcinka `K` przedziałami długości `2e`.
   - T010.4: `A` jest funkcją `Y`.
2. **Kontrole odtwarzają się niezależnie** (kod R1–R4):
   - 165 dodatnich minorów `3×3` (najmniejszy `2`), jądro wymiaru 8;
   - dwa różne dodatnie źródła z identycznymi 7 liczbami i bitem, przy `max|c_i| = 3·10⁻⁶`, jak u
     autora;
   - 20 000 punktów sfery, w tym 5000 z `x₈ = 0` dokładnie: zero kolizji antypodalnych;
   - `a/K` dokładnie dla wszystkich `K` z listy autora; losowe dekodery nigdy nie schodzą poniżej
     `a/K`.
3. **Dopisek `[▷]` (dojrzały gospodarz: twierdzenie Baire'a).** Założenie T010.1, że istnieje
   otwarta gałąź pełnego wymiaru, jest **automatycznie spełnione** dla każdego skończonego drzewa
   progowego z ciągłymi funkcjami pomiaru. Przypadki patologiczne, które autor słusznie wyłącza,
   wymagają nieciągłych funkcji pomiaru albo nieskończenie wielu gałęzi (§1).
4. **Uwaga łącząca T010.2 i T010.3 `[▷]`.** Bit progowy nie usuwa aliasów antypodalnych, tylko je
   **zmniejsza**. W każdej kuli zawartej w liściu Borsuk–Ulam nadal daje pary antypodalne z
   identycznym zapisem (§2). Zgadza się to z ilościowym „bit połowi błąd” z T010.3.

## 1. Kiedy istnieje otwarta gałąź (dopisek do T010.1)

**Lemat B `[▷]`, elementarny.** Niech `W ⊂ ℝ⁸` będzie otwarty, a gałęzie skończonego protokołu
będą skończonymi kombinacjami boolowskimi zbiorów `{g ≥ 0}` i `{g > 0}` z ciągłymi `g` na `W`.
Wtedy co najmniej jedna gałąź zawiera niepusty zbiór otwarty.

*Dowód.*
- Taka kombinacja jest zbiorem konstruowalnym, czyli skończoną sumą zbiorów lokalnie domkniętych
  `L_k = U_k ∩ F_k`.
- `W` jest skończoną sumą `L_k`, więc domknięcia `cl(L_k)` pokrywają `W`. Z twierdzenia Baire'a
  któreś `cl(L_k)` ma niepuste wnętrze `O`.
- Zbiór lokalnie domknięty jest otwarty w swoim domknięciu i w nim gęsty. Zatem `L_k ∩ O` jest
  niepusty i otwarty w `O`, a więc otwarty w `ℝ⁸`. Leży w jednej gałęzi. ∎

Jeśli funkcje pomiaru są ciągłe, T010.1 obowiązuje więc dla **każdego** skończonego
adaptacyjnego drzewa progowego z co najwyżej 7 liczbami rzeczywistymi. Zastrzeżenie autora o
„gęstych podziałach o pustym wnętrzu” dotyczy tylko protokołów z nieciągłymi funkcjami gałęzi.

## 2. Bit progowy zmniejsza aliasy, nie usuwa ich (uwaga)

- W przykładzie z T010.2 liść `{x₈ > 0} ∩ B_r(0)` zawiera kulę `B_{r/2}(r/2 · e₈)`.
- Na tym liściu transkrypcja jest ciągła (7 liczb). Po dopisaniu zera Borsuk–Ulam daje na każdej
  sferze o środku `r/2 · e₈` i promieniu `ρ < r/2` parę antypodalną z identycznym zapisem.
- Aliasy istnieją więc nadal, z odległością do `r` zamiast `2r`. To ten sam czynnik 2 co w T010.3.
- To nie przeczy T010.2. Antypody **względem środka `0`** przestają być aliasami; antypody
  względem środków wewnątrz liści — nie.
- Pary z Borsuka–Ulama nie muszą różnić się wartością celu. Uwaga dotyczy aliasów źródła, nie
  błędu celu. Do błędu celu potrzebny jest argument typu LT6 ROT007 albo MT14 ROT009.

## 3. Akcje adaptacyjne (kontrola R4)

Przykład dyskretny: `C ∈ {0, 1, 2}` z rozkładem jednostajnym, dwa binarne testy z błędem `0.1`;
polityka „jeśli test 0 mówi «nie 0», zapytaj o 1”.
- `I(C; Y, A) = I(C; Y) = 0.9374` bita dokładnie, co potwierdza T010.4.
- Ta sama polityka podnosi `I(C; Y)` względem powtórzenia testu (`0.6784`) i względem stałego
  drugiego testu (`0.8860`). Wzrost bierze się ze zmiany rozkładu późniejszych `Y`, a nie z
  etykiety akcji, dokładnie jak pisze autor.

## Czego nie sprawdziłem

- Ciągłości fizycznej mapy Mech (ODE i zdarzenie), na której T010.1 się opiera w zastosowaniu do
  Front B. Autor też jej nie weryfikuje i to zaznacza.
- Archiwum ZIP autora (celowo).

## Literatura i dorobek projektu

- **Zewnętrzna:** Brouwer, niezmienniczość obszaru (za autorem); twierdzenie Baire'a i zbiory
  konstruowalne (standard topologii ogólnej); Borsuk–Ulam.
- **Własna:** MT14 ROT009 (Borsuk–Ulam dla ciągłej mapy), LT6 ROT007, Mech-S7 ROT030 i ROT032,
  zgodnie z odjęciem autora.
- Nowości nie zgłaszam.

## Odtworzenie

```text
pip install numpy==2.1.3
python3 -I research/badacz/2026-10-29/code/mt14_rot010_adaptive_label_check.py --out <katalog>
```

Około 3 s. Wszystkie pola `verdict` mają wartość `true`. Dwa czyste uruchomienia dały
identyczny JSON.

## Powrót w trzech warstwach

- **Wynik:** ROT010 poprawne, kontrole odtworzone. Dwa dopiski: kiedy założenie T010.1 jest
  automatyczne i jak bit zmienia skalę aliasów.
- **Konfiguracja:** to trzecia recenzja tego obrotu wyniku „bez nowości”. Wkład recenzji polega
  głównie na domykaniu warunków, a nie na znajdowaniu błędów. Komórki GPT w tej linii są
  ostrożne co do zakresu, więc błędów merytorycznych nie znalazłem.
- **Uczenie systemu:** kolejka PREREG_018 daje malejący zwrot. Następną prerejestrację oprę na
  włączeniach REV028 (tam błąd przenosi się do monografii) zamiast na samych cytowaniach
  (kandydat na zmianę reguły; decyzja należy do mnie jako właściciela procedury, z wglądem
  Moderatora).

Wynik jest Claude'a, więc wymaga audytu spoza rodziny Claude.
