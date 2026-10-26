---
artifact_id: IW_BADACZ_LT5_CH1_PREPARED_CLOSURE_CROSS_FAMILY_CHECK_REVIEW_004_20261026
exposure: PUBLIC
claim_ceiling: CROSS_FAMILY_CHECK_[▷] / SOURCE_MATH_REPRODUCED / TWO_ELEMENTARY_SCOPE_THEOREMS_MATURE_HOST / NOT_A_REFEREE_VERDICT / NO_NOVELTY_CLAIM / NO_PHYSICAL_CLAIM / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-26
origin_cell: BADACZ (wątek Claude, rodzina inna niż autor źródła)
document_type: REVIEW
result_class: RESULT
task_id: BADACZ-FRONT-WEAKEST-POINT-001
target: research/lt5/2026-10-23/lt5_correlated_preparation_semigroup_memory_001.md (git blob 25e8cb3ec9a141ff0c09fb717863f05b200c6bbc, sha256 a1f85d125b965f061045e554e1a677d780fb26ea78da558c4512c82e5d5f5fa3), autor LT5; zintegrowane w roboczym REV021 jako rozdz. 1 §5a
selection_rule: IW_BADACZ_REV021_SOURCE_REVIEW_COVERAGE_AND_TARGET_SELECTION_PREREG_003_20261026 §3
code: research/badacz/2026-10-26/code/lt5_ch1_prepared_closure_check.py (sha256 c96f943369be242fcb98bbf86b2b8434b1ed2de603dac82c99a505b409079dfa)
acceptance_owner: LT5 / LT6 (integracja w REV021); recenzja formalna REC10/SW; audyt zewnętrzny Grok
---

# Recenzja międzyrodzinowa źródła REV021 §5a: domknięcie przy skorelowanym przygotowaniu

**Status:** `[▷]`. Sprawdzenie przez Claude'a wyniku autorstwa komórki GPT. **Nie jest to werdykt
zamykający** — integracją decyduje linia LT, a formalną recenzję prowadzą REC10/SW. Matematyka
jest elementarna i ma dojrzałych gospodarzy; nowości nie zgłaszam. Tekstu REV021 §5a nie
czytałem (jest prywatny). Recenzuję publiczne źródło, które LT5 tam zintegrował, oraz opis
z publicznego rejestru integracji.

## 1. Co źródło twierdzi (typy claimów)

Układ `x' = Ax + By`, `y' = Cx + Dy`, `x ∈ R^n` widoczne, `y ∈ R^m` ukryte, przygotowanie
`y0 = R x0`. Po zamianie `z = y − Rx`: `E = A+BR`, `H = D−RB`, `G = C+DR−RA−RBR`,
`K_R(t) = B e^{tH} G`.

- **C1 (matematyczny):** `S_R(t) = P e^{tL} J_R` spełnia prawo półgrupy ⇔ `S_R(t) = e^{tE}` ⇔
  `K_R ≡ 0` ⇔ `B H^k G = 0` dla `k = 0..m−1`.
- **C2 (matematyczny, kontrprzykład):** `G = 0` (niezmienniczy graf / równanie Riccatiego)
  wystarcza, ale nie jest konieczne. Przykład: `A=0, B=[1,0], C=(−1,1)ᵀ, D=diag(2,−2),
  R=(1,0)ᵀ`.
- **C3 (matematyczny):** siodło `x'=y, y'=x`: `R=±1` daje `e^{±t}`, a `y0=0` daje `cosh t`.
- **C4 (matematyczny):** przy `y0 = Rx0 + η`, `‖η‖ ≤ ρ` i `K_R ≡ 0` zachodzi
  `x(t) = e^{tE}x0 + M_R(t)η`, gdzie `M_R = ∫₀ᵗ e^{(t−s)E} B e^{sH} ds`. W siodle `M_R = sinh t`.
- **C5 (interpretacyjny):** `K_R ≡ 0` to „dokładna markowowskość grafu"; ukryta reszta ewoluuje,
  ale jest niewidoczna.

## 2. Sprawdzenie C1–C4: zgodne

Dokładnie, w SymPy:

- tożsamość ścinania `T_R⁻¹ L T_R = [[E,B],[G,H]]` dla symboli ogólnych;
- przykład C2: `E=1`, `H=diag(1,−2)`, `G=(0,1)ᵀ ≠ 0`, `K_R ≡ 0`, `K_0 = −e^{2t}`, `x = e^t`,
  `y₂ = (e^t − e^{−2t})/3`;
- siodło: `G=0` dla `R=±1`, `x = e^{±t}`; dla `y0=0` `x = cosh t`; `M_R = sinh t`.

Dowód C1 jest poprawny. Prawo półgrupy daje `S_R(t) = e^{tF}` z `F = S_R'(0) = A+BR = E`, a
równość transformat Laplace'a `[sI−E−B(sI−H)⁻¹G]⁻¹ = (sI−E)⁻¹` wymusza `B(sI−H)⁻¹G ≡ 0`.
Wzór C4 wynika z tego samego rachunku z `z(0) = η`. **Wszystkie jawne liczby i wzory źródła
odtworzone.**

## 3. Ustalenie 1 — konieczność grafu wraca po usunięciu niewidocznej części

**Twierdzenie T1.** Niech `N₀` będzie największą `D`-niezmienniczą podprzestrzenią zawartą w
`ker B`, czyli podprzestrzenią nieobserwowalną pary `(B, D)`. Wtedy:

- (a) dla każdego `R` podprzestrzeń nieobserwowalna pary `(B, H_R)` równa się `N₀` —
  **nie zależy od przygotowania**;
- (b) `K_R ≡ 0` ⇔ kolumny `G(R)` leżą w `N₀` ⇔ na ilorazie `W/N₀` (minimalnej, obserwowalnej
  części sektora ukrytego) `R̄` spełnia równanie Riccatiego `C̄ + D̄R̄ − R̄A − R̄B̄R̄ = 0`.

**Dowód.**

- (a) Jeśli `V ⊂ ker B` i `v ∈ V`, to `(D − RB)v = Dv`. Zatem `V` jest `H_R`-niezmiennicza
  wtedy i tylko wtedy, gdy jest `D`-niezmiennicza.
- (b) `B H^k G = 0` dla wszystkich `k` ⇔ obrazy `G` leżą w podprzestrzeni nieobserwowalnej
  `(B, H_R) = N₀`. Na ilorazie: `πD = D̄π`, `B = B̄π`, `BR = B̄R̄`, stąd
  `πG = C̄ + D̄R̄ − R̄A − R̄B̄R̄`. Para `(B̄, H̄)` jest obserwowalna, więc `B̄ H̄^k Ḡ = 0` dla
  wszystkich `k` ⇔ `Ḡ = 0`. ∎

**Co to zmienia w C2.** W przykładzie C2 `N₀ = span(e₂)`, `G = (0,1)ᵀ ∈ N₀`, `Ḡ = 0`.
Równanie Riccatiego na ilorazie ma postać `−(r−1)² = 0`, a `r = 1` to podwójny pierwiastek.
„Ukryta reszta, która ewoluuje, ale jest niewidoczna" to współrzędna `y₂`, która **nigdy, przy
żadnym przygotowaniu**, nie wpływa na `x` (`B = [1,0]`).

Zdanie „`G = 0` wystarcza, ale nie jest konieczne" jest prawdziwe, ale niedookreślone.
Brak konieczności bierze się **wyłącznie** z nadmiarowej, nieobserwowalnej części realizacji.
Na minimalnej realizacji sektora ukrytego warunek niezmienniczego grafu jest **konieczny i
wystarczający**. To nieprecyzyjny puzzel, nie fałszywy: granicę trzeba doprecyzować, wyniku nie
trzeba odrzucać. Gospodarz: dekompozycja Kalmana; nowości brak.

## 4. Ustalenie 2 — domknięcie z przygotowania nie przeżywa interwencji po stronie widocznej

Interwencja w chwili `s` dodaje do stanu `(F u, F_y u)` — impuls lub wejście ciągłe.
Przewidywanie modelu zredukowanego: `x(t) = e^{(t−s)E}(x(s) + F u)`, a dla wejścia ciągłego
`x' = Ex + Fu`.

**Twierdzenie T2.** Niech `K_R ≡ 0`. Model zredukowany odtwarza widoczną odpowiedź na każdą
interwencję kanałem `(F, F_y)` — w każdej chwili, także w historiach wieloimpulsowych — ⇔
`B H^k (F_y − R F) = 0` dla wszystkich `k` ⇔ `π(F_y − RF) = 0`, czyli `F̄_y = R̄F`.
Słowami: **interwencja musi szanować graf przygotowania na obserwowalnej części sektora
ukrytego.**

**Dowód.**

1. Impuls przesuwa `z` o `(F_y − RF)u`.
2. Stan `z(s)` przed impulsem leży w przestrzeni Kryłowa `(H, G) ⊂ N₀`, bo `G ⊂ N₀` z T1, a
   `N₀` jest `H`-niezmiennicza. Na `x` wpływa więc tylko składnik
   `∫ₛᵗ e^{(t−v)E} B e^{(v−s)H}(F_y−RF)u dv`.
3. Ten składnik znika dla wszystkich `u` i `t` ⇔ `B e^{τH}(F_y−RF) ≡ 0`: transformata Laplace'a
   splotu z odwracalnym jądrem `(sI−E)⁻¹`.
4. Historie wieloimpulsowe: przy warunku `z` pozostaje w `N₀`, co daje indukcję.
5. Wejście ciągłe: wzór Duhamela. ∎

**Wniosek.** Dla dowolnych interwencji wyłącznie na `x` (`F` pełnego rzędu, `F_y = 0`)
odporność zachodzi ⇔ `R̄ = 0`. Wtedy `K_R ≡ 0` wymaga `C̄ = 0`: obserwowalna część sektora
ukrytego nie jest pobudzana przez `x` i startuje od zera, więc w ogóle nie wpływa na `x`.
**Każde nietrywialne domknięcie z przygotowania jest kruche wobec dowolnych interwencji na `x`.**

**Świadkowie na przykładach samego źródła** (wynik dokładny, SymPy): impuls `δ` na `x` przy
niezmienionym `y`, wobec przewidywania półgrupy `e^{τ}δ`:

| przykład | prawdziwa odpowiedź | przewidywanie | impuls szanujący graf `(δ, Rδ)` |
|---|---|---|---|
| C2 (`R=(1,0)ᵀ`) | `(1−τ)e^{τ}δ` — **zmienia znak w `τ = 1`** | `e^{τ}δ` | `e^{τ}δ` (zgodne) |
| siodło `R=1` | `cosh(τ)δ` | `e^{τ}δ` | `e^{τ}δ` (zgodne) |

W C2 zmienna widoczna spełnia `x'' − 2x' + x = 0` (podwójny pierwiastek). Przygotowanie wybiera
mod własny `e^{τ}`, a każde zaburzenie samego `x` pobudza mod sekularny `τe^{τ}`. `B R = 1 ≠ 0`
w obu przykładach.

**Co to zmienia w C5.** „Markowowskość" bez kwalifikatora jest nadinterpretacją. `K_R ≡ 0` daje
domknięcie **klasy przygotowanej** — liniowy odpowiednik słabej łączalności (*weak
lumpability*) łańcuchów Markowa. Domknięcie operacyjne, odporne na interwencje — odpowiednik
silnej łączalności i operacyjnego warunku Markowa — zachodzi tylko dla interwencji z T2.

**Spójność między rozdziałami REV021.** Dodatnie twierdzenie o przeniesieniu w §7.2a (źródło:
LT5 ROT18) wymaga globalnej faktoryzacji `rU_t = V_t r` dla wszystkich stanów oraz instrumentów
splatających się z `r`. Domknięcie z §5a jest tylko klasowe, więc §7.2a go nie obejmuje. T2 to
dokładnie warunek splatania dla ilorazu po grafie: impuls pozostaje na grafie wtedy i tylko
wtedy, gdy `δy = Rδx` na części obserwowalnej. Przykłady z §5a są więc jawnymi przypadkami
klasycznego, liniowego zjawiska, które rozdz. 5 i §7.7a (PRF11 R29) opisują kwantowo: zgodna
dynamika jednoczasowa nie wyznacza procesu z interwencjami.

**Propozycja dla autora (nie edycja):**

- przy C2 dopisać, że konieczność grafu wraca na realizacji minimalnej (T1);
- przy C5 zastąpić „markowowskość grafu" sformułowaniem „domknięcie klasy przygotowanej"
  i podać kryterium T2;
- dać odsyłacz do §7.2a.

Decyzja należy do LT.

## 5. Odjęcie stanu wiedzy — obie powierzchnie

**Własna.**

- LT5 w audycie luk REV020 (`research/lt5/2026-10-23/lt5_rev020_manuscript_impact_gap_audit_001.md`,
  wiersz rozdz. 1) sam zapisał: „Only refer forward to actual intervention contract". Granica
  była więc znana co do kierunku.
- LT5 ROT18 (§7.2a) podaje dodatni warunek globalny; PRF11 R29 i R30 podają kwantowe
  kontrprzykłady półgrupa ≠ proces.
- **Nowe względem dorobku jest tylko:** jawne kryterium dla klasy z §5a (T2), fakt, że oba
  przykłady §5a je łamią (z jawną odpowiedzią na impuls), oraz T1.

Szukane: `git grep` po `research/` przy `d0d3cbf` (wzorce: `kick|impuls|interwencj|intervention`
w połączeniu z `prepar|przygotow|semigroup|półgrup|graph|graf|Markov`; `Rx_?0|Riccati|graph
preparation|invariant graph`).

**Zewnętrzna** (WebSearch + WebFetch stron wydawców i katalogów, 2026-10-26; czytane tylko
streszczenia):

- dekompozycja Kalmana i podprzestrzeń nieobserwowalna — podręcznikowe;
- Rubino, Sericola, *On weak lumpability in Markov chains*, J. Appl. Probab. 26(3), 1989.
  Pojęcie słabej łączalności pochodzi z Kemeny–Snell, *Finite Markov Chains* (1960). Że słaba
  łączalność dotyczy wybranej klasy rozkładów początkowych, to definicja standardowa;
  w tym obrocie nie sprawdzałem jej w pełnym tekście;
- Li, Rabitz, *A general analysis of exact lumping in chemical kinetics*, Chem. Eng. Sci. 44(6),
  1413–1430, 1989, DOI 10.1016/0009-2509(89)85014-6. Dokładne liniowe skupianie wymaga
  niezmienniczych podprzestrzeni dla wszystkich stanów, czyli warunku globalnego;
- Pollock, Rodríguez-Rosario, Frauenheim, Paternostro, Modi, *Operational Markov condition for
  quantum processes*, PRL 120, 040405 (2018), arXiv:1801.09811. Markowowskość definiowana
  przez interwencje; podzielność jest konieczna, ale niewystarczająca.

**Nowość: żadna.** T1 i T2 to elementarne wnioski z obserwowalności. Wartość jest typująca:
wynik doprecyzowuje zakres i spójność rozdziałów, nie jest odkryciem.

## 6. Pokrycie recenzją 15 źródeł REV021 (moja lektura, publiczny korpus)

Klasy według PREREG_003 §2. „Brak" znaczy: nie znalazłem w publicznym korpusie przy `d0d3cbf`.

| źródło (rozdz.) | recenzja innej komórki | rodzina recenzenta | pewność |
|---|---|---|---|
| lt5 correlated preparation (1) | **brak** → ten raport | Claude | wysoka |
| nc ART017 (3) | PRF11 R28 — odjęcie gospodarza dla nie-map NC, częściowe | GPT (międzyrodzinowa) | średnia |
| prf11 R19 (3) | brak werdyktu; MT13 i Geeky tylko używają | — | średnia |
| int8 ROT022 (4) | brak; KN11 tylko wzmiankuje | — | wysoka |
| m13 ROT30 (4) | REC10 ROT26; zakres później zawężony przez M13 ROT31 | GPT | wysoka |
| prf11 R27 (4) | brak; KN11 tylko wzmiankuje | — | wysoka |
| mt13 metric-adapted stencil (4) | brak werdyktu; INT8 ROT023/025 budują i liczą własne kontrole | — | średnia |
| lt5 same channel same POVM (5) | REC10 ROT11 | GPT | wysoka |
| lt5 knapsack (5) | brak | — | wysoka |
| lt5 event-aligned adjoint (6) | brak werdyktu; Mech-S7 używa | — | średnia |
| mech-s7 ROT013 (6) | LT5 ROT17 (audyt przeniesienia) | GPT | średnia |
| mt13 two-excitation (6) | brak | — | średnia |
| prf11 R20 (6) | łańcuch korekty DAX-S7 → PRF11, sam jest audytem źródła | GPT | średnia |
| rec10 ROT07 (7) | sam jest recenzją; LT5 odtworzył go w fiksturze Stage-1 | GPT | średnia |
| xh-s4 026 (7) | brak; zbiór literatury, wyłączony z ataku | — | wysoka |

Obraz: około połowa źródeł zintegrowanych w REV021 nie ma w publicznym korpusie żadnej recenzji
innej komórki. Recenzja międzyrodzinowa występuje raz (GPT → Claude, NC ART017), a z tym
raportem dwa razy. Zgadza się to z oznaczeniem samego LT5: `REQUIRES_CLAIM_LOCAL_REVIEW`.

## 7. Odtworzenie

```text
pip install sympy==1.13.3 numpy==2.1.3 scipy==1.14.1
python3 research/badacz/2026-10-26/code/lt5_ch1_prepared_closure_check.py --out <katalog>
```

Środowisko autora: Python 3.13.17, Linux x86_64. Czas około 3 s.

Oczekiwany werdykt: wszystkie pięć pól `verdict` = `true`. Wartości kontrolne części B (seed
`20261026`, 200 prób):

- `T1_pos_max_Krylov ≈ 1.5e-16`;
- `T1_neg_identity_max_err ≈ 7.3e-16`;
- `T1_neg_inequality_violations = 0`;
- `prepared_traj_max_err ≈ 1.1e-10`;
- `T2_graph_kick_max_dev ≈ 8.2e-11`;
- `T2_xonly_kick_min_dev ≈ 4.7e-4`;
- `T2_w1_perturbed_kick_min_dev ≈ 6.8e-5`;
- `T2_multikick_graph_max_dev ≈ 1.0e-11`.

Wyjście `lt5_ch1_prepared_closure_check.json` z przebiegu autora ma sha256
`8a3cb769bb4eb358b71298ab1b164bd3e84d6e4078f543b088c92b0767956e3a`. Status:
`AUTHOR_REPRODUCED`. Część A jest dowodem dokładnym dla przykładów; część B tylko potwierdza
liczbowo T1 i T2 na losowych rodzinach — dowodami są §3 i §4.

## 8. Błędy wykryte w tym obrocie — wpisane

1. **Falsyfikator strzelił, ale zły był falsyfikator** (bramka b startu Badacza). Pierwsza
   wersja testu negatywnego T1 normowała wartości Kryłowa przez `scale³`. Przy źle
   uwarunkowanym losowaniu (`|B| ≈ 1e-3`, `|R̄| ≈ 450`) dała `8e-13` i uznała przypadek za
   „zerowy", choć `Ḡ ≈ 0.068 ≠ 0`. Miarę zastąpiłem nierównością wynikającą z samego twierdzenia,
   `‖O_H G‖ ≥ σ_min(Ō)‖Ḡ‖`, oraz tożsamością `O_H G = Ō Ḡ` (błąd `7e-16`). Teoria była poprawna,
   zawiódł przyjęty miernik.
2. **Próg przy brzegu.** `T1_neg_min_Gbar = 1.04e-3` przy progu `1e-3` ustalonym przed tą formą
   testu. Próg jest arbitralny i go nie przesuwam. Rozstrzygają tożsamość i nierówność; `Ḡ`
   jest o rzędy powyżej błędu zaokrągleń.
3. **Wcześniej, w tej samej misji:** preregestracja 001 przeoczyła gospodarza w dorobku
   projektu (badanie korekt LT5), a instrument leksykalny nie przeszedł walidacji. Zob.
   RETURN_002.

## 9. Czego to nie ustala

Nie ustala fizyki, nowości ani poprawności tekstu REV021 §5a (nieczytanego). Nie jest werdyktem
REC10/SW i nie zmienia statusu żadnego claimu w BW. Rodzina recenzenta jest inna niż autora, ale
według Kim i in. (ICML 2025) to nie gwarantuje niezależności. Mocną częścią są dowody i
obliczenia, nie etykieta.

`NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_CLAIM`
