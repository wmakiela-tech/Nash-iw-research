# IW/NASH — REC10 ROT07
## Dokładna wartość ograniczenia wynikającego z chronologii pomiaru i sterowania

**Data:** 21 października 2026  
**Komórka:** `IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10`  
**Funkcja:** `STRESS / TYPE / HARDEN`  
**Werdykt:** `PASS_WITH_EXACT_SHARPENING / MATURE_HOST`  
**Autorytet:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_TASK`

### Materiał źródłowy i aktualność

Zbadano pełny dokument LT5:
`research/lt5/2026-10-21/lt5_causal_timing_of_information_vs_actuation_two_stage_exact_minimax_001.md`.

[Źródło LT5 w GitHub](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/2026-10-21/lt5_causal_timing_of_information_vs_actuation_two_stage_exact_minimax_001.md).

Odczytany SHA blobu: `76e31e82574aa194111d90a0ee139b76d09ceb81`.

Przeprowadzono przegląd późniejszych komunikatów `#iw-dispatch` i `#iw-alerts`, jak również najnowszych commitów naukowych projektu. Równoległe rezultaty Geeky-S10, PRF11 oraz XH-S4 zachowują odrębne warunki źródłowe i nie zmieniają poniższego twierdzenia LT5.

### 1. Zamrożone twierdzenie LT5

Nieznany stan skalarny \(y\in[\ell,h]\). Wcześniejsza decyzja \(u_0\), podejmowana przed pomiarem, spełnia \(|u_0|\leq B_0\). Następnie:

\[
b=s(y-u_0)+\eta,\qquad |\eta|\leq\delta,\quad s>0.
\]

Po obserwacji regulator może wybrać \(u_1(b)\) z \(|u_1|\leq B_1\). Wartość końcowego błędu minimaksowego:

\[
J_{\mathrm{two}}=\inf_{|u_0|\leq B_0}\inf_{u_1(\cdot)}
\sup_{y\in[\ell,h],\,|\eta|\leq\delta}|y-u_0-u_1(b)|.
\]

Definicje:

\[
w=\frac{h-\ell}{2},\quad c=\frac{h+\ell}{2},\quad
e=\min(w,\delta/s).
\]

LT5 wyprowadza:

\[
J_{\mathrm{two}}=\max\{e,\ w+(|c|-B_0)_+-B_1\}.
\]

**Werdykt dla formuły, polityk i dowodu LT5: PASS.** Ograniczenie przyczynowe jest respektowane; w szczególności niewykorzystany wczesny budżet nie jest dostępny podczas późniejszej decyzji.

### 2. Nowe dokładne zaostrzenie: cena chronologii

Alternatywny, wyraźnie **inny** model dysponuje całą nominalną zdolnością \(B_0+B_1\) dopiero po pomiarze:

\[
J_{\mathrm{late}}=\max\{e,\ w+|c|-B_0-B_1\}.
\]

Wtedy dla wszystkich dopuszczalnych parametrów zachodzi dokładnie

\[
\boxed{\quad
J_{\mathrm{two}}-J_{\mathrm{late}}
=
\min\{(B_0-|c|)_+,\ (w-B_1-e)_+\}.
\quad}
\]

**Dowód.** Gdy \(B_0\leq|c|\), drugi składnik maksimum obu wzorów jest taki sam, a różnica wynosi zero. Gdy \(B_0>|c|\), oznaczmy \(q=B_0-|c|>0\) i \(a=w-B_1\). Wówczas

\[
J_{\mathrm{two}}=\max(e,a),\qquad
J_{\mathrm{late}}=\max(e,a-q).
\]

Tożsamość elementarna

\[
\max(e,a)-\max(e,a-q)=\min\{q,(a-e)_+\}
\]

daje tezę. Nie zakładano, że \(a\) lub drugi składnik maksimum są dodatnie. \(\square\)

Wzór stanowi ilościowe uzupełnienie warunku ścisłej nierówności z §3 LT5. Nie jest nową rodziną twierdzeń.

### 3. Kontrole rozdzielające

**Świadek z doskonałą informacją końcową:** \(I=[-1,1]\), \(s=1\), \(\delta=0\), \(B_0=1\), \(B_1=0\). Mamy \(w=1,c=0,e=0\). Wartość \(J_{\mathrm{two}}=1\), ale \(J_{\mathrm{late}}=0\). Nowy wzór daje dokładnie \(\min(1,1)=1\).

**Świadek zaszumiony LT5:** \(I=[-0{,}8,1{,}2]\), \(s=1\), \(\delta=0{,}05\), \(B_0=0{,}7\), \(B_1=0{,}4\). Tutaj \(w=1,c=0{,}2,e=0{,}05\), a zatem:

\[
J_{\mathrm{two}}-J_{\mathrm{late}}
=\min(0{,}5,0{,}55)=0{,}5
=0{,}6-0{,}1.
\]

**Kontrola numeryczna:** 50 000 deterministycznie generowanych zestawów parametrów (generator NumPy `default_rng(21)`); maksimum rozbieżności między różnicą obu wartości i wzorem zamkniętym wyniosło \(8{,}881784197\cdot10^{-16}\). Test jest kontrolą rachunkową, nie zastępuje powyższego dowodu.

### 4. Dokładne ograniczenie zastosowania

- **Zdolność obserwacji końcowej nie oznacza dostępności sterowania po obserwacji.**
- Budżet \(B_0\) nie jest automatycznie przenoszalny: \(J_{\mathrm{late}}\) to osobna, kontrfaktyczna klasa polityk.
- Wcześniejsza decyzja przesuwa środek przedziału, ale nie usuwa niepewności co do \(y\).
- Nie uogólniać wzoru na wielowymiarowe cele, dynamikę z nieznanymi portami, korelowany szum, adaptacyjne pomiary ze zmianą operatora stanu czy pomiar kwantowy.
- Odniesienie do wcześniejszych prac o robust output-feedback / set-membership information states jest uzasadnione źródłowo przez LT5, ale nie stanowi wyczerpującego audytu pierwszeństwa.

### 5. Dyspozycja i custody

`LT5_TWO_STAGE_THEOREM = PASS`  
`REC10_EXACT_CHRONOLOGY_PREMIUM = PASS`  
`PRIOR_ART = MATURE_CLASSICAL_HOST`  
`EDITORIAL_OPTION = ONE_EXACT_EQUATION_FOR_LT5`  
`NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_NEW_TASK`  
`STABLE_STOP` dla tej konkretnej formuły do czasu zmiany kontraktu źródłowego.

**Custody:** raport utworzono jako załącznik do tej rozmowy i zweryfikowano odczytem pliku. Zapis GitHub i przekazanie Slack zostały odrzucone przez zabezpieczenia narzędzi; nie przypisuje się im statusu sukcesu. Wcześniejszy raport ROT06 pozostaje lokalnie zapisany i również nie ma potwierdzonego doręczenia przez te kanały. `BW_INGESTION / OWNER_ACCEPTANCE = NOT_VERIFIED`.

---

### Aktualizacja custody / recovery — 2026-10-22

Historyczne oznaczenia `GitHub_write: BLOCKED` i `Slack_delivery: BLOCKED` w oryginalnym raporcie dotyczą nieudanych prób z 21.10.2026 i pozostają zachowane jako ślad audytowy. **Ponowiony zapis: GitHub WRITE+EXACT READBACK PASS**, commit: `f5b2dfa553ec5086bfd12b3866b47f500807dd4d`. **Ponowione doręczenie: Slack SENT+SEARCH READBACK PASS**, wiadomość: https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1792655163759049. Nie stwierdzono BW ingestion, niezależnej akceptacji właściciela, CANON ani EXEC_SIGN.
