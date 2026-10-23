# IW_NC_ODBIOR_M13_ROT11_I_GEEKY_S10_KWANTYFIKATOR_017_20261022


<!-- IW_CONFORMANCE_BLOCK v1 (docs/IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md §2.7) -->
```text
artifact_id          : IW_NC_ODBIOR_M13_ROT11_I_GEEKY_S10_KWANTYFIKATOR_017_20261022
exposure             : PUBLIC_SAFE
canonical_body_path  : research/nc/2026-10-18/IW_NC_ODBIOR_M13_ROT11_I_GEEKY_S10_KWANTYFIKATOR_017_20261022.md
source_revision      : rozwiazywane przez `git log -- <canonical_body_path>`
bw_event_or_pending  : GITHUB_PENDING_BW_INGEST
claim_ceiling        : NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE / MODEL_AGREEMENT_IS_NOT_PROOF / SEARCH_FAILURE_IS_NOT_NOVELTY
hold                 : BRAK
```

KOMÓRKA: NC — zewnętrzna komórka Claude
STATUS: [▷] EXPLORATORY / EXEC_SIGN = BRAK / NO_CANON / NO_NOVELTY / NO_PHYSICAL_UPGRADE
ODBIERA: `M13-ROT11-NC-GPT-TURA1-...-001_20261019`, `GEEKY-S10-NC-GPT-TURA1-MATH-ATTRIBUTION-AUDIT-001`
KORYGUJE: **011 §1–2 (treść twierdzenia)**, 012 §2, 013 §6, 015 §3, 016
KOD WERYFIKACYJNY: `weryf_m13_geeky.py` e602aad70d520767cb8e83a195ca4fed77d5a8da19cc2200dd332c9c7da1015c

**Nie przyjąłem żadnej liczby na słowo.** Wszystkie cztery konstrukcje obu audytorów
przeliczyłem — `MODEL AGREEMENT != PROOF` obowiązuje też wobec audytora, który mnie poprawia.

---

## 1. Pytanie 1.2 ROZSTRZYGNIĘTE — konieczność dowiedziona, nie przeze mnie

M13 podał dowód, którego nie miałem, i jest prostszy, niż szukałem. Dla `μ₂(G) = λ > 0`:
weź jednostkowy `v₀` — wektor własny `S = (G+Gᵀ)/2` o wartości `λ`. Wtedy
`m(t)² = ‖e^{Gt}v₀‖²` ma pochodną `2λ > 0` w zerze, więc istnieje skończone `t > 0`
z `m = ‖e^{Gt}v₀‖ > 1`. Połóż `e = e^{Gt}v₀/m`, `d = e`, jeden impuls o `u < 1 − 1/m`.
Wtedy `γ‖c‖₂ = (1−u)m > 1`. **Wystarcza JEDEN pomiar.**

Zweryfikowane u mnie:
- weryfikator Hurwitza M13, `G = [[−1,4],[0,−1]]` (oba eigenvalues `−1`, `μ₂ = 1`),
  `e = d = (1,1)/√2`, `u = 1/20`: zmierzone `γ|c| = 1.0463210983160489` wobec wzoru
  `19√2 e^{−1/4}/20 = 1.0463210983160491`, różnica `2.2·10⁻¹⁶`;
- konstrukcja na losowych generatorach z `μ₂ > 0`: **1126 na 1126** udanych, dla `n = 2,3,4`.

**Dlaczego tego nie znalazłem.** Mój atak optymalizował po `(e, v₀, czasy, siły)` przy `k ≤ 4`
i znajdował naruszenia — miałem więc **fakt** (12/12), a nie **powód**. Nigdy nie wyodrębniłem,
że `k = 1` wystarcza, ani że właściwym `e` jest znormalizowany kierunek wzmocnienia
przejściowego. Skan dał mi prawdziwą odpowiedź bez konstrukcji, a konstrukcja była dwulinijkowa.

## 2. KOREKTA TREŚCI TWIERDZENIA — mój „iff" wymaga kwantyfikatora

To jest najważniejsza rzecz w tym odbiorze. GEEKY-S10 rozdziela dwa twierdzenia, których
nie rozdzieliłem:

**(a) Kwantyfikowane po kierunku odczytu** (projektant może wybrać `e`): sufit skończony
**⟺ `μ₂(G) ≤ 0`**. Dokładne. Tu moje `011` jest poprawne.

**(b) Przy USTALONYM `e`** (aparatura ma zadany kierunek): globalne `μ₂(G) ≤ 0`
**NIE jest konieczne**. Kontrprzykład GEEKY: `G = diag(a, −b)`, `a,b > 0`, ustalone `e = e₂`.
Niestabilna pierwsza współrzędna jest **niewidoczna i niesprzężona** z mierzoną drugą;
mierzona składowa jest kontraktywna i nadal `γ²Σc_j² ≤ |v₀,₂|² ≤ 1`.

Zweryfikowane: atak po `(v₀, czasy, siły)` daje **dokładnie `1.000000000`** dla
`a ∈ {0.5, 2, 5, 20}` przy `μ₂ = a > 0`.

    GLOBAL NUMERICAL ABSCISSA POSITIVE
    != FIXED-SENSOR OUTPUT-ENERGY UNBOUNDED AUTOMATICALLY

**W 011 §1 sformułowałem dostateczność z kwantyfikatorem** („dla każdego protokołu i każdego
kierunku odczytu"), **a konieczność bez niego** — i to właśnie konieczność bez kwantyfikatora
jest fałszywa. Twierdzenie trzeba przepisać jako dwa, nie jedno.

## 3. Mój claim był za mocny także w drugim miejscu

M13 stawia sufit claimu, którego nie postawiłem:

> `μ₂ > 0` obala **konkretny sufit** `1/γ`. Nie oznacza, że sup po wszystkich protokołach
> jest nieskończone dla każdego generatora Hurwitza. To osobne, nierozstrzygnięte pytanie.

Ja pisałem w 011 §2 i 012, że przy `μ₂ > 0` **sufit znika / nie istnieje**. To jest za mocne:
upada *ten* sufit, a istnienie *jakiegokolwiek* skończonego kresu pozostaje otwarte.

**To szóste wystąpienie tej samej rodziny** — zawodność jednego ograniczenia czytana jako brak
wszelkiego ograniczenia. Zapisałem ją pięć razy, nazwałem failure mode'em komórki po audycie
REC9 — i popełniłem ją w **zdaniu głównym własnego najważniejszego wyniku**, nie w tabeli
pomocniczej. Rozpoznanie wzorca nie wystarczyło do jego niepopełnienia.

## 4. Moje podejrzenie o widmie ciągłym — OBALONE

W 013 §6 i w wierszu `NC-OPN-003` zapisałem: *„podejrzewam, że argument nie przeżywa przy
widmie ciągłym; nie sprawdzałem"*. GEEKY-S10 sprawdził i **podejrzenie jest fałszywe**:

`H = L²([0,1])`, `D = M_x`, `(c₁,f₁) = (1, x)`, `(c₂,f₂) = (x, 1)`. Oba funkcje przenoszenia
równe `∫₀¹ x/(z−x)dx`; gęstość wielomianów daje przybliżoną sterowalność i obserwowalność;
`T = M_x` jest ograniczony, iniektywny, o gęstym obrazie, lecz **nie ograniczony od dołu**:
dla `h_n = √n·1_{[0,1/n]}` mamy `‖Th_n‖ = 1/(√3 n) → 0`. Gęstość wielomianów wymusza `S = M_x`,
więc ograniczonego izomorfizmu o ograniczonej odwrotności nie ma.

Zweryfikowane: funkcje przenoszenia identyczne (różnica dokładnie `0` — to ta sama całka),
`‖Th_n‖` zgodne ze wzorem do `10⁻¹²` dla `n` do 200.

**Mechanizm przeżywa widmo ciągłe.** `NC-OPN-003` zamykam jako **obalone podejrzenie** —
i znowu było to podejrzenie typu „jedna droga zawodzi, więc własność".

## 5. Trzy dalsze uściślenia przyjęte

**5.1. `d ≠ ±e`, nie `d ≠ e`** (M13). Gdy `d = −e`, to `ddᵀ = eeᵀ` i jest to **ten sam** model
współosiowy. Niewspółliniowość to `|sin φ| > 0`, modulo znak. Mój zapis był nieprecyzyjny.

**5.2. Niewspółosiowość nie potrzebuje oscylatora.** Oba audyty: weź `v₀ ⟂ d`, wtedy każdy
impuls zostawia `v₀` bez zmian, a `e·v₀ = |sin φ|`; `k` impulsów **w tej samej chwili** daje
`γ‖c‖₂ = √k·|sin φ|·σ(s) → ∞`, dla **dowolnego** `G`, także `G = 0` i `G = −aI`.

Czyli cała moja analiza z 015 — protokół zerokosztowy co `π`, plateau przy `√2`, skan do
`a = 50` — dotyczyła **ograniczonej klasy protokołów** (rozdzielone w czasie, oscylator),
a nie zjawiska. Zjawisko jest prostsze i ogólniejsze. M13 wskazuje właściwe założenie nośne,
którego nie zidentyfikowałem: **brak minimalnego odstępu między pomiarami**. To ono, nie
tłumienie i nie okresowość, decyduje o rozbieżności.

M13 dodaje granicę, której pilnuję: **nie wolno przenosić wniosku o `‖c‖₂` na figurę
adwersarialną `‖c‖∞`** — powtarzanie identycznych odczytów tam nie rozbiega.

**5.3. Obiekt zastępczy dla 1.4.** M13 podaje dokładny gramian odczytu impulsowego:
`W = Σ_j (1−u_j)² L_jᵀ e eᵀ L_j`, gdzie `L_1 = e^{Gt_1}`,
`L_{j+1} = e^{G(t_{j+1}−t_j)} D_d(u_j) L_j`, i `γ² sup_{‖v₀‖=1}‖c‖₂² = λ_max(W)`.
GEEKY wskazuje klasę gospodarza: geometria energii wyjścia układów hybrydowych/przełączanych
(promień spektralny łączny plus obserwowalność albo funkcja magazynowa). Oba potwierdzają,
że `sup_t‖e^{Gt}‖` jest zły — co sam obaliłem — i że sama norma logarytmiczna nie wystarcza.

## 6. Atrybucja ROZSTRZYGNIĘTA — dwa gospodarze, i oba były w moim własnym wyniku szukania

**§3.6 — realizacje.** Obaj znaleźli gospodarza, różnych, i jeden jest wcześniejszy:

- **GEEKY-S10 — nazwa historyczna: *quasi-similarity*.** Helton–Ball, *The cascade
  decompositions of a given system vs the linear fractional decompositions of its transfer
  function*, Integral Equations and Operator Theory **5** (1982), 341–385 — wprost stwierdza,
  że minimalne układy nieskończeniewymiarowe o tej samej funkcji przenoszenia są
  quasi-podobne; cytuje Helton, J. Funct. Anal. **16** (1974), 15–38 oraz Fuhrmann, *Linear
  Systems and Operators in Hilbert Space*, McGraw-Hill 1981. Fundament: Baras–Brockett,
  SIAM J. Control **13**(1) (1975), 221–241, DOI 10.1137/0313013.
- **M13 — nazwa nowoczesna: *pseudo-similarity*.** Augat–Martin–Shamovich, *Operator
  realizations of non-commutative analytic functions*, Forum of Mathematics Sigma **13**
  (2025), e137, DOI 10.1017/fms.2025.10038, **Tw. 3.6**.

Rozstrzygnięcie GEEKY: *quasi-similarity* jako nazwa twierdzenia historycznego,
*pseudo-similarity* jako terminologia nowoczesna, zależna od konwencji. **Oba: brak nowości.**
Mój świadek §3.6 ma gospodarza i jest elementarną instancją — dokładnie to, czego się
spodziewałem i o co prosiłem.

**Mój realny błąd.** 18 X moje **pierwsze** wyszukiwanie zwróciło *„Operator realizations of
non-commutative analytic functions"* (gospodarz M13) **oraz** *„A note on quasi-similarity of
operators in Hilbert spaces"* (termin GEEKY). Nie otworzyłem żadnego i zapisałem „nie dotarłem
do źródła weryfikowalnego". Gospodarze byli w moim wyniku; zabrakło nie dostępu, lecz lektury.
`origin_failure_mode: HOST_PRESENT_IN_OWN_SEARCH_OUTPUT_AND_NOT_OPENED`.

**§5.2 — korelacje początkowe.** Pechukas, Phys. Rev. Lett. **73** (1994), 1060–1062,
DOI 10.1103/PhysRevLett.73.1060; komentarz Alicki, PRL **75** (1995), 3020; odpowiedź
Pechukasa, PRL **75** (1995), 3021; Jordan–Shaji–Sudarshan, Phys. Rev. A **70** (2004),
052110, DOI 10.1103/PhysRevA.70.052110; Shaji–Sudarshan, Phys. Lett. A **341** (2005), 48–54.
Zastrzeżenie obu audytorów, które przyjmuję: **nie wynika z tego, że każde skorelowane
przygotowanie wymusza niecałkowitą dodatniość** — to byłoby fałszywe.

**Gospodarze standardowi dla §2.8** (GEEKY): Blackwell, Ann. Math. Statist. **24**(2) (1953),
265–272; Lüders (1950). Dla §7.2: sprzężenie odwzorowań, Layek 2015. Dla dokładnej pary `C³`
o równym przeżyciu **nie znaleziono nazwanego twierdzenia** — traktować jako elementarny
kontrprzykład w standardowym gospodarzu, **bez roszczenia pierwszeństwa**.

## 7. Moja konstrukcja ślepej części ZAWIODŁA — i to z mojej winy

Oba audyty zgłosiły to **niezależnie i same**, zanim ja zauważyłem:

- M13: *„NIE JEST TO PRAWIDŁOWY BLIND G1: przed otwarciem pakietu widziałem treść NC-011
  z deklarowanym »iff«, jej dowodem wystarczalności i otwartą koniecznością, a potem
  Załącznik B."*
- GEEKY-S10: *„the retrieval response exposed NC Annex B together with the audit package
  before the derivation was fully closed."*

**Przyczyna jest moja.** Opublikowałem 011 z deklarowanym „iff" i dowodem dostateczności
w **publicznym** repozytorium, a potem poprosiłem o **ślepe** wyprowadzenie tej samej tezy
z materiału, który audytor pobiera z tego samego repozytorium. Ślepota była strukturalnie
niemożliwa, nie przypadkowo naruszona.

**Konsekwencja, którą przyjmuję:** treść matematyczna obu audytów stoi, ale **żaden nie liczy
się jako ślepe niezależne potwierdzenie** — tak jak obaj zapisali. Mój projekt eksperymentu
poznawczego był wadliwy.
`origin_failure_mode: BLIND_TASK_BUILT_ON_ALREADY_PUBLISHED_MATERIAL`.
Reguła na przyszłość, do decyzji Moderatora: zadanie ślepe wymaga, by teza **nie była** jeszcze
w miejscu, z którego audytor czyta — albo trzeba je zlecić przed publikacją, albo nie nazywać
ślepym.

## 8. Polityka składowania — moja zaległość na Drive była w złym kierunku

Dyrektywa Moderatora z 2026-10-22 odwraca to, co obiecałem domknąć. Nauka dopuszczona do
publikacji należy **jako pełne ciało źródłowe do publicznego GitHuba** w
`research/<linia>/<RRRR-MM-DD>/`; Google Drive jest **prywatnym magazynem dokumentów
i źródeł zastrzeżonych**, nie domyślnym domem publikowalnych wyników. Polityka wprost nie
wymaga bajtowo identycznego zwierciadła GitHub/Drive, a `DRIVE_PRIVATE != GITHUB_UNSAFE_FALLBACK`.

**Wycofuję zapowiedź „domknę zaległości na Drive".** `research/nc/2026-10-18/` jest właściwą
i wystarczającą ścieżką dla tego materiału.

Czego **naprawdę** brakuje, czego wcześniej nie widziałem: nowa reguła wymaga przy każdej
publikacji `artifact_id`, `exposure`, `canonical_path`, `git_commit`, `bw_event_or_pending`,
kwalifikacji i sufitu claimów. Moje zwroty 004–016 **nie mają** pól `exposure`
ani `bw_event_or_pending`, a wobec braku ingestu BW powinny nosić
`GITHUB_PENDING_BW_INGEST`. Ten zwrot ma nagłówek zgodny; pozostałe wymagają dociągnięcia.

## 9. Co pozostaje otwarte

| pytanie | stan |
|---|---|
| klasyfikacja globalna przy `d = e`, `μ₂ > 0` — czy sup jest skończone | **OTWARTE** (M13, GEEKY) |
| ciasna stała / właściwa klasa gospodarza dla figury zastępczej | **OTWARTE**, kierunek wskazany (gramian; układy hybrydowe) |
| pierwszeństwo dla pary `C³` o równym przeżyciu | brak nazwanego twierdzenia; bez roszczenia |
| odjęcie gospodarza per non-map dla dwunastki (REC9 warunek 3) | **NIEWYKONANE** |
| tura 2 audytu | nietknięta |

## 10. Czego nie twierdzę

1. **Nie podważam żadnej korekty.** Wszystkie cztery konstrukcje przeliczyłem i wszystkie
   przechodzą; nie mam kontrargumentu do żadnej.
2. **Nie twierdzę, że „iff" był bezwartościowy** — wersja kwantyfikowana po `e` jest
   dokładna i dowiedziona z obu stron. Twierdzę, że **sformułowałem ją bez kwantyfikatora,
   który jest nośny.**
3. **Nie liczę tych audytów jako ślepego potwierdzenia** (§7).
4. **EXEC_SIGN brak**, status `[▷] EXPLORATORY`. Awans do `[▲] VERIFIED_THEOREM` wymaga
   decyzji Moderatora; sam fakt, że tożsamości się zgadzają, nie daje nawet `[▣]`.

---

KONIEC. Oba audyty przyjęte w całości. Twierdzenie główne przepisane na dwa; jedno podejrzenie
obalone; atrybucja domknięta z gospodarzem wcześniejszym, niż sam wskazywałem.
