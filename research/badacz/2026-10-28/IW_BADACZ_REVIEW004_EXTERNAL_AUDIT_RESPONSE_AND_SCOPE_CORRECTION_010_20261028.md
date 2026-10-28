---
artifact_id: IW_BADACZ_REVIEW004_EXTERNAL_AUDIT_RESPONSE_AND_SCOPE_CORRECTION_010_20261028
exposure: PUBLIC
claim_ceiling: EXTERNAL_AUDIT_RECORD / SCOPE_CORRECTION_OF_INTERPRETIVE_CLAIMS / T2_MATH_STATUS_UNCHANGED_[▷] / ADAPTIVE_INPUT_PROPOSITION_[▷] / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-28
origin_cell: BADACZ (wątek Claude)
document_type: CORRECTION
result_class: RESULT
task_id: BADACZ-FRONT-WEAKEST-POINT-001
corrects: research/badacz/2026-10-26/IW_BADACZ_LT5_CH1_PREPARED_CLOSURE_CROSS_FAMILY_CHECK_REVIEW_004_20261026.md (commit 3c76fe7) — tylko dwa zdania interpretacyjne w §4; matematyka bez zmian
audit_source: Grok (rodzina xAI), odpowiedź na PAKIET_GROK_BADACZ_001 poz. 1, przekazana przez Moderatora 2026-10-28; Grok nie uruchamiał kodu
code: research/badacz/2026-10-28/code/review004_grok_audit_followup_check.py (sha256 80601c4c5b234bc2de677759862e7172bd82382ed12ade94102ae4cd97c3e3a1)
output_sha256: 012f6874951370430a0c5434b2e015af84b4eda6d74d98f55a5772e93ef952fe (review004_grok_audit_followup_check.json)
---

# Odpowiedź na audyt zewnętrzny T2 (Grok) i korekta zakresu REVIEW_004

**Status:**
- Matematyka T2 pozostaje `[▷]`. Brak trafienia w audycie zewnętrznym zwiększa pokrycie, ale nie
  jest dowodem; status podnosi tylko Moderator.
- Dwa zdania interpretacyjne z REVIEW_004 §4 zostają **skorygowane** (§2 niżej).

## 1. Punkty audytu — każdy sprawdziłem sam

| punkt Groka | moje sprawdzenie | skutek |
|---|---|---|
| iff T2 (`K_R ≡ 0`: model zredukowany dokładny ⇔ `B Hᵏ(F_y − RF) = 0` ∀k ⇔ `π(F_y − RF) = 0`): brak kontrprzykładu i brak luki | zgodne z REVIEW_004 | bez zmian |
| model „impuls na samo `x`” jest uczciwy w klasie liniowej | zgodne | bez zmian |
| teza „każde nietrywialne domknięcie jest kruche wobec dowolnych impulsów na `x`” zależy od algebry dopuszczalnych interwencji | **przyjęte**: jeśli kontrakt instrumentów wymusza `F̄_y = R̄F`, kruchość jest pusta | korekta K1 |
| „pełny rząd `F`” jest nośny | **przyjęte**. Założenie było w zdaniu poprzedzającym, ale wytłuszczone podsumowanie je zgubiło. Dokładny świadek A2: `R = [1, 0]`, `G = 0`; impuls `F = e₂ ∈ ker R̄` jest nieszkodliwy, `F = e₁` łamie domknięcie | korekta K1 |
| analogia z operacyjnym warunkiem Markowa (Pollock i in.) jest częściowa: tam dozwolone są instrumenty adaptacyjne | **przyjęte częściowo**. W obrębie zadanych kanałów T2 obejmuje także wejścia adaptacyjne (Propozycja A, §3). Analogia pozostaje częściowa z innego powodu: Pollock dopuszcza instrumenty stochastyczne z oddziaływaniem zwrotnym pomiaru oraz kanały spoza algebry | korekta K2 |
| przeoczony gospodarz: niezmienniczość sterowana, odsprzęganie zakłóceń | **przyjęte, przeoczyłem go** (§4) | dopisany gospodarz |

Drobna uwaga do audytu: Li–Rabitz nie było w pakiecie, było w REVIEW_004 §5. Grok miał link do
obu plików, więc nie zmienia to niczego.

## 2. Skorygowane brzmienie (zastępuje dwa zdania REVIEW_004 §4)

**K1** (zamiast „Każde nietrywialne domknięcie z przygotowania jest kruche wobec dowolnych
interwencji na `x`”):

> Jeśli algebra dopuszczalnych interwencji zawiera impulsy wyłącznie na `x` (`F_y = 0`) o pełnym
> obrazie w `x`, to każde domknięcie z przygotowania, które jest nietrywialne na obserwowalnym
> ilorazie (`R̄ ≠ 0`), jest na nie kruche. Przy niepełnym obrazie `F` odporne są dokładnie impulsy
> z `R̄F = 0`. Jeśli kontrakt instrumentów wymusza `F̄_y = R̄F` (por. §7.2a, instrumenty splatające
> się z redukcją), kruchość jest pusta.

**K2** (zamiast „Domknięcie operacyjne, odporne na interwencje — odpowiednik silnej łączalności i
operacyjnego warunku Markowa — zachodzi tylko dla interwencji z T2”):

> T2 jest warunkiem dokładności modelu zredukowanego **dla zadanej algebry kanałów**
> `(F_i, F_{y,i})` i obejmuje także wejścia adaptacyjne w tych kanałach (Propozycja A). Związek z
> operacyjnym warunkiem Markowa Pollocka i in. to **analogia**: tamten warunek obejmuje instrumenty
> stochastyczne z oddziaływaniem zwrotnym pomiaru, których ten deterministyczny model liniowy nie
> zawiera.

## 3. Propozycja A `[▷]`: wejścia adaptacyjne

**Założenia.** `K_R ≡ 0`, przygotowanie `y(0) = Rx(0)` i kanały `(F_i, F_{y,i})`, przez które
wchodzą wejścia `u_i`. Wejścia mogą być impulsami albo sygnałem ciągłym. Mogą zależeć w dowolny
sposób od historii, także od ukrytego `y` i od losowania.

**Teza.** Model zredukowany `x' = Ex + Σ F_i u_i` jest dokładny dla wszystkich takich protokołów
⇔ `B Hᵏ(F_{y,i} − RF_i) = 0` dla wszystkich `k` i `i`.

**Dowód.**
- `z = y − Rx` spełnia `z' = Gx + Hz + Σ(F_{y,i} − RF_i)u_i`, `z(0) = 0`.
- Z `K_R ≡ 0` mamy `im G ⊂ N₀` (T1).
- Z warunku `im(F_{y,i} − RF_i) ⊂ N₀`, a `N₀` jest `H`-niezmiennicza. Stąd `z(t) ∈ N₀` dla
  każdego `t`, **niezależnie od wartości `u`**, więc i od sposobu ich wyboru. Zatem `Bz ≡ 0`.
- Konieczność: protokoły otwarte są szczególnym przypadkiem adaptacyjnych; stosujemy T2. ∎

Wniosek dla typowania: luka między interwencjami otwartymi a adaptacyjnymi, wskazana przez Groka,
nie istnieje w obrębie zadanych kanałów. Istnieje poza nimi.

**Sprawdzenie** (seed `20261028`):

| test | wynik |
|---|---|
| siodło `x' = y`, `y' = x`, `R = 1`, sprzężenie `u = kx` (SymPy, dokładnie) | kanał `(1,1)`: różnica `≡ 0`; kanał `(1,0)`: przy `k = 1/2`, `t = 1` różnica `−0.5482` |
| 60 losowych układów z nietrywialnym `N₀`, `K_R ≡ 0` (`max|B e^{sH} G| ≤ 1e-9`), kanały spełniające T2 z **niezerowym** przesunięciem w `N₀` (60/60) | błąd modelu zredukowanego: sprzężenie od `x` `≤ 8.5e-11`, sprzężenie od ukrytego `y` (odtworzony sygnał) `≤ 2.4e-11`, adaptacyjne impulsy `≤ 3.6e-12` |
| te same układy, kanały łamiące T2 | błąd `≥ 2.5e-3` we wszystkich trzech trybach |

## 4. Przeoczony gospodarz

Warunek T2 to dokładnie przypadek bez sterowania z klasycznego problemu odsprzęgania zakłóceń.
Zaburzenie `(F_y − RF)u` wchodzi do podukładu `z`, który wpływa na `x` przez `Bz`. Odsprzęgnięcie
⇔ obraz kanału zaburzenia leży w maksymalnej `H`-niezmienniczej podprzestrzeni `ker B`, czyli w
`N₀`. Przy sterowaniu odpowiednikiem jest maksymalna `(A,B)`-niezmiennicza podprzestrzeń w
`ker C`.

Źródła (rekordy sprawdzone; twierdzenie DDP widziane w notatkach wykładowych KTH, rozdz. 3,
Tw. 3.1):
- Basile, Marro, *Controlled and conditioned invariant subspaces in linear system theory*,
  J. Optim. Theory Appl. 3(5), 306–315 (1969), DOI 10.1007/BF00931370;
- Wonham, *Linear Multivariable Control: A Geometric Approach*, Springer, ISBN 978-0-387-96071-5
  (wydania nie zweryfikowałem).

**Dlaczego to przeoczyłem:** szukałem w słownictwie łańcuchów Markowa i skupiania (lumpability,
weak/strong), a nie w słownictwie geometrycznej teorii sterowania.

## 5. Monografia — bez potrzeby edycji

REV023, rozdz. 1 §9–§10 (tekst rozdz. 1 bez zmian w REV024–025) sformułował wynik ostrożniej niż
moja REVIEW_004:
- „warunek splatania konkretnego instrumentu z redukcją”;
- „na ogół NIE jest zamknięta”;
- „analogią na poziomie pytania o dozwolone interwencje, nie identycznością mechanizmów”.

Nadmiar zakresu był tylko w mojej recenzji. Opcjonalnie dla LT, decyzja autora:
1. „na ogół” można zastąpić warunkiem dokładnym. Przy impulsach na `x` o pełnym obrazie
   domknięcie jest odporne ⇔ `R̄ = 0`, co przy `K_R ≡ 0` wymusza `C̄ = 0`.
2. Do źródeł §9 można dopisać gospodarza z §4.

## Odtworzenie

```text
pip install numpy==2.1.3 scipy==1.14.1 sympy==1.13.3
python3 research/badacz/2026-10-28/code/review004_grok_audit_followup_check.py --out <katalog>
```

Około 15 s. Wszystkie pola `verdict` mają wartość `true`. Dwa czyste uruchomienia dały identyczny
JSON.

## Uczenie systemu

`origin_failure_mode`: **CONDITIONAL_RESULT_SUMMARIZED_UNCONDITIONALLY**.
- Co się stało: wytłuszczone podsumowanie zgubiło przesłanki, które stały w zdaniu wyżej (pełny
  rząd `F`) albo nie stały nigdzie (dopuszczalność interwencji).
- Reguła: każde zdanie interpretacyjne niesie własne przesłanki albo jawny odsyłacz do nich.
- Reguła dla odjęcia stanu wiedzy: twierdzenia o układach liniowych przeszukuję też w słownictwie
  geometrycznej teorii sterowania.

Audyt spoza rodzin GPT i Claude wykrył błąd typowania, którego nie wykryłem ja. Komórka GPT (LT)
przy integracji typowała wynik ostrożniej ode mnie.

`NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM`. Propozycja A to mój wynik `[▷]`; wymaga
zewnętrznego sprawdzenia (Grok albo REC10).
