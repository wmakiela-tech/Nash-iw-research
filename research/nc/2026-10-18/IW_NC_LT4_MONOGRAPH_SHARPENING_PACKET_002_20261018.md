# IW_NC_LT4_MONOGRAPH_SHARPENING_PACKET_002_20261018

<!-- IW_CONFORMANCE_BLOCK v1 (docs/IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md §2.7) -->
```text
artifact_id          : IW_NC_LT4_MONOGRAPH_SHARPENING_PACKET_002_20261018
exposure             : PUBLIC_SAFE
canonical_body_path  : research/nc/2026-10-18/IW_NC_LT4_MONOGRAPH_SHARPENING_PACKET_002_20261018.md
source_surface       : GOOGLE_DRIVE (1D1RcNtP1OK24z_rTOIfmPohV0LhfONZ0)
source_revision      : rozwiazywane przez `git log -- <canonical_body_path>`
bw_event_or_pending  : GITHUB_PENDING_BW_INGEST
claim_ceiling        : NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_FROM_ANALOGY / SOURCE_FIRST / SUBTRACTION_FIRST
hold                 : BRAK
mirror_note          : PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
```

> **Ścieżka publiczna nadana 2026-10-23 decyzją Moderatora** (`NC-OPN-015`, ART019 §2).
> Treść merytoryczna jest zapisem z 2026-10-18 i **nie była retuszowana**. Jeden prywatny
> lokator Drive zredagowano zgodnie z routing §4 („Do not publish restricted provider URLs
> to public GitHub"); precedens: mirror `MT13-ROTATION09-...-001`.
>
> **BANER WERDYKTÓW ZEWNĘTRZNYCH.** Ten pakiet był audytowany trzykrotnie 2026-10-18 i ma
> pięć niekorzystnych werdyktów, zarejestrowanych jako `NC-FAL-011` … `NC-FAL-014`
> i `NC-OPN-014` (ART019 §3). Czytać razem z nimi. W szczególności: zdanie z §A.2
> o „oszacowaniu malejącym" przy `mu < 0` jest **odrzucone** (INT7 §4); zdanie z §A.6
> o kinetyce rozdz. 6 jest **odrzucone** (INT7 §8.3 + M13 ROT09); nierówność (7.3′) z §B.2
> jest **odrzucona** (REC9 §B3); odczyt `mu` jako wzrostu asymptotycznego jest **odrzucony**
> (INT7 §5); banachowskie typowanie §A.2 wymaga naprawy (REC9 i INT7 zgodnie) — co §C.2
> tego pakietu **samo zgłasza**. Werdykty nie są tu wmontowane w treść, żeby zapis
> pozostał tym, czym był w chwili audytu.

---

RETURN_ID: NC-LT4-MONOGRAPH-SHARPENING-PACKET-002
FROM_CELL: NC (external independent Claude cell)
TO: **LT4 (właściciel, autorstwo)**, MODERATOR, REC9, INT7, MT13, PRF11, SCOPE8
DATE: 2026-10-18 (CEST)
ZADANIE: Moderator — analizy, obliczenia, wyszukiwania w literaturze, porównania, aby
monografia głębiej analizowała temat i dawała wkład naukowy.
BUDUJE NA: `IW_NC_LT4_MONOGRAPH_AUDIT_001_20261018` (Drive `[PRIVATE_DRIVE_LOCATOR_REDACTED]`)
`NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_FROM_ANALOGY / SOURCE_FIRST / SUBTRACTION_FIRST` · `[▷]`

**Proponuję matematykę, nie prozę.** Twierdzenia, dowody, zweryfikowane liczby i
referencje. Sformułowania redakcyjne i decyzja o włączeniu należą do LT4.

**Dwa zaostrzenia, oba typu A/B z hierarchii planu, oba na twierdzeniach, które rozdział
już ma.** Żadne nie jest nową fizyką. Każde nazywa dokładnie, **która hipoteza lub
konkluzja staje się ostrzejsza** — czego plan wymaga w punkcie B.

---

## A. ZAOSTRZENIE TW. 7.3 / WZORU (7.1): STAŁA LIPSCHITZA → NORMA LOGARYTMICZNA

### A.1 Co jest nie tak ze wzorem (7.1) w obecnej postaci

Wzór (7.1) używa stałej Lipschitza `L(t)` funkcji `g`. Ta stała jest **dwustronna**:
mierzy, jak szybko `g` może rozsuwać *dowolne* dwa punkty. Błąd `e(t)=r(x(t))−y(t)` żyje
jednak w konkretnym kierunku, a Grönwall potrzebuje tylko **jednostronnego** oszacowania
`⟨e, g(r(x))−g(y)⟩ ≤ μ‖e‖²`.

Właściwym obiektem jest **norma logarytmiczna** (jednostronna stała Lipschitza, stała
Dahlquista)
```
mu(G) = lim_{eps->0+} ( ||I + eps G|| - 1 ) / eps ,
```
w przypadku euklidesowym `mu(G) = lambda_max( (G+G^T)/2 )`. Zachodzi zawsze
`-||G|| <= mu(G) <= ||G||`, a **`mu` może być ujemna**, czego `L` nie może.

### A.2 Proponowana postać twierdzenia

> **Twierdzenie 7.3′.** Przy założeniach Tw. 7.3, z `L(t)` zastąpioną mierzalną
> `mu(t)` spełniającą jednostronny warunek
> `⟨g(u,t)−g(v,t), u−v⟩ <= mu(t)‖u−v‖²` na odcinku łączącym `r(x(t))` i `y(t)`:
> ```
> ||e(T)|| <= exp(int_{t0}^T mu) ||e(t0)||
>           + int_{t0}^T exp(int_s^T mu(u) du) eps(s) ds .        (7.1')
> ```
> Ponieważ `mu(t) <= L(t)` punktowo, (7.1′) jest **nigdy nie gorsze** od (7.1), a przy
> `mu < 0` daje oszacowanie **malejące**, podczas gdy (7.1) rośnie wykładniczo.

Dowód jest ten sam co w rozdziale — nierówność Grönwalla z czynnikiem całkującym — z tą
jedną zmianą, że krok `‖g(r(x))−g(y)‖ <= L‖e‖` zastępuje się jednostronnym
`d/dt ‖e‖ <= mu‖e‖ + eps`.

> **ERRATA 2026-10-23 (INT7 §4, `REJECT_AS_STATED`, rejestr `NC-FAL-012`).** Ostatnie
> zdanie jest fałszywe dla **pełnego** ograniczenia z wymuszeniem. Przy stałym `eps > 0`,
> `e(t0) = 0` i `mu = −a < 0` ograniczenie wynosi `(eps/a)(1 − exp(−a(T−t0)))`, czyli
> **rośnie** od zera do plateau `eps/a`. Maleje wkład błędu początkowego, waga starszego
> wymuszenia i propagator jako funkcja opóźnienia — nie ograniczenie całkowite. Poprawne
> sformułowanie: „`mu < 0` daje propagację kontraktywną; trwałe wymuszenie daje ograniczoną
> splotową odpowiedź, która może rosnąć do skończonego plateau". Tabela §A.5 tego pakietu
> ma dokładnie to zachowanie.

### A.3 Dlaczego to jest OSTRE, a nie tylko lepsze

`mu` jest **najmniejszą** stałą, dla której `‖e^{Gt}‖ <= e^{θt}` zachodzi dla wszystkich
`t >= 0`; równoważnie
`mu(G) = min{ θ : ||e^{Gt}|| <= e^{θt} dla wszystkich t>=0 }` (Higham, odwołując się do
dowodu w Hinrichsen–Pritchard 2005). Żadna stała w tej roli nie może być mniejsza.

> **ERRATA 2026-10-23 (INT7 §5, `REJECT_IF_INFERRED`, rejestr `NC-FAL-014`).** Zdanie jest
> poprawne **wyłącznie przy jawnym kontrakcie prefaktora jednostkowego**. `mu(G)` nie jest
> oszacowaniem wzrostu asymptotycznego, gdy dopuszczalne są oszacowania `M exp(omega t)`
> z `M > 1`. Separator INT7: `G = [[−1,100],[0,−1]]` ma odciętą widmową `−1`, czyli jest
> asymptotycznie stabilny, a `mu_2 = 49 > 0`.

### A.4 Sprawdzone na WŁASNYM przykładzie rozdziału (§7.3)

Układ `ẋ = (−x₀, x₂, 0)`, `r(a,b,h)=(a,b)`, `g(y)=(−y₀,0)`, `T=2`, `e(t₀)=0`.
Tu `L = ‖Jg‖ = 1,000000`, natomiast `mu = λ_max((Jg+Jgᵀ)/2) = 0,000000`.

| h₀ | ‖e(T)‖ faktyczne | granica z `L` | iloraz | granica z `mu` | iloraz |
|---|---|---|---|---|---|
| 0,3 | 0,600000000 | 1,916717 | 3,195 | 0,600000000 | **1,00000** |
| 1,0 | 2,000000000 | 6,389056 | 3,195 | 2,000000000 | **1,00000** |
| 3,0 | 6,000000000 | 19,167168 | 3,195 | 6,000000000 | **1,00000** |
| 10,0 | 20,000000000 | 63,890561 | 3,195 | 20,000000000 | **1,00000** |

**Z normą logarytmiczną oszacowanie jest OSIĄGANE** na przykładzie, który rozdział sam
podaje. Ze stałą Lipschitza jest luźne o dokładnie `(e²−1)/2 = 3,1945`.

*(INT7 §6: `PASS_EXACT`, potwierdzone niezależnie.)*

### A.5 Przypadek, w którym (7.1) jest JAKOŚCIOWO zła

`g(y) = diag(−3,−2)·y`, redukcja gubi ukryty stan tak jak w §7.3. Tu `L = 3,0000` (dodatnia,
granica rośnie jak `e^{3T}`), ale `mu = −2,0000` (ujemna, granica maleje).

| T | ‖e(T)‖ faktyczne | granica z `L` | granica z `mu` | granica-L / faktyczne |
|---|---|---|---|---|
| 1,0 | 0,432332358 | 6,3618 | 0,432332361 | 14,7 |
| 3,0 | 0,498760624 | 2 700,6949 | 0,498760647 | 5 414,8 |
| 6,0 | 0,499996928 | 21 886 665,2792 | 0,499997022 | **43 773 599,5** |

Błąd faktyczny **saturuje** na `0,5`; granica Lipschitza przeszacowuje go przy `T=6` o
czynnik `4,4·10⁷`, granica logarytmiczna trafia w siedem cyfr. Dla dyssypatywnej dynamiki
zredukowanej — czyli typowego przypadku kinetycznego — (7.1) jest nad długim horyzontem
bezużyteczne, a (7.1′) ostre.

*(INT7 §7: `PASS_WITH_WORDING_REPAIR` — tabela jest poprawna, ale sama pokazuje, że
granica z `mu` **rośnie** do `1/2`, a nie maleje; patrz errata w §A.2.)*

### A.6 KONSEKWENCJA MIĘDZYROZDZIAŁOWA — to jest priorytet 3 planu

Plan żąda: *„rozwinąć wspólne problemy tak, aby rezultaty z różnych rozdziałów rzeczywiście
działały na tej samej legalnie określonej klasie modeli; jeżeli brak takiej klasy, zapisać
wyraźny non-map."*

`mu` **jest** taką klasą, i to nie przez analogię, a przez tożsamość obiektu:

- **Rozdział 1** (gospodarz Engel–Nagel, półgrupy): `mu(G)` jest dokładnie oszacowaniem
  wzrostu półgrupy, `‖e^{tG}‖ <= e^{mu(G)t}`. Sprawdzone w 9/9 przypadkach losowych dla
  `n = 3,5,8` i `t = 0,5 / 2 / 6`: nierówność zachodzi, a granica Lipschitza jest luźna
  do `9,6·10²³` przy `n=8, t=6`.
- **Rozdział 6** (redukcja kinetyczna, §6.11 granica zamknięcia quasi-stacjonarnego):
  kinetyka jest dyssypatywna, więc `mu < 0` i to jest dokładnie reżim z §A.5.
- **Rozdział 7** (§7.5, wierność trajektorii): wzór (7.1′).

Trzy rozdziały, jedna stała, jedna nierówność, **legalnie określona klasa: dynamika
zredukowana z zadeklarowaną normą logarytmiczną generatora.** To jest wspólny nośnik, nie
zestawienie podobnie brzmiących równań.

> **ERRATA 2026-10-23, dwie, obie na §A.6.**
>
> 1. **Rozdział 1 — zawężenie (INT7 §8.2, `PASS_BOUNDED_SUBCLASS_ONLY`).** Dla ograniczonych
>    generatorów liniowych w zadeklarowanej normie zdanie jest legalne. Rozdział 1 zawiera
>    jednak **nieograniczone generatory C₀**, w tym przykład translacji z §10. Dla nich
>    elementarnego wzoru dla operatorów ograniczonych nie wolno importować bez twierdzenia
>    o dyssypatywności / quasi-kontraktywności i kontroli dziedziny.
>    `LOG_NORM JAKO JEDEN WZÓR DLA WSZYSTKICH GENERATORÓW C₀ ROZDZ. 1 = NIEUSTALONE.`
> 2. **Rozdział 6 — odrzucone (INT7 §8.3 + M13 ROT09, rejestr `NC-FAL-013`).** Zdanie
>    „kinetyka jest dyssypatywna, więc `mu < 0`" jest odrzucone. Rozdział 6 zawiera
>    `D_h(X_n,T,n_B,…)` zależne od stanu, sprzężone sieci obfitości i ogólne jakobiany
>    sieczne §6.9; nic w rozdziale nie dowodzi ujemnej normy logarytmicznej **pełnego
>    sprzężonego** jakobianu we wspólnej normie, a stabilny liniowo jakobian nie musi mieć
>    ujemnej `mu`, bo niesamosprzężony wzrost przejściowy może dać `mu > 0`. Poprawne
>    sformułowanie: „dla tych modeli i obszarów kinetycznych, w których zadeklarowany
>    jakobian ma **certyfikowaną** ujemną normę logarytmiczną w wybranej normie…".
>
> W konsekwencji teza §A.6 o wspólnej klasie jest **warunkowa na kontrakcie normy
> i dziedziny** (INT7 §9: `SAME SYMBOL mu != SAME MODEL CLASS`), a nie ustalona.

### A.7 Odejmowanie prior-artu — to jest materiał GOSPODARZA, nie nasz

Norma logarytmiczna: **Dahlquist (1958)**, rozprawa doktorska, KTH Stockholm; niezależnie
**Lozinskii (1958)**. Nowoczesne opracowanie: **G. Söderlind, „The logarithmic norm.
History and modern theory", BIT Numerical Mathematics 46(3):631–652 (2006),
DOI 10.1007/s10543-006-0069-9** (zweryfikowane w rejestrze Lund University i scite.ai).
Dowód `‖e^{At}‖ <= e^{mu(A)t}` i minimalność `mu`: Hinrichsen & Pritchard,
*Mathematical Systems Theory I*, Springer (2005).

**Typ A w hierarchii planu: zaimportowane, nie nasze.** Wkładem jest wyłącznie (i) import
do wzoru (7.1), (ii) pokazanie, że granica staje się **osiągana na przykładzie rozdziału**,
(iii) wskazanie, że w reżimie dyssypatywnym różnica jest jakościowa, a nie ilościowa, oraz
(iv) §A.6 jako wspólny nośnik trzech rozdziałów. Nic z tego nie jest nową matematyką.

*(INT7 §11: proweniencja bibliograficzna **nie była** niezależnie weryfikowana w tamtym
obrocie; `NO_NOVELTY_INFERENCE`.)*

---

## B. ZAOSTRZENIE TW. 7.4: Z WARUNKU WYSTARCZAJĄCEGO DO RÓWNOWAŻNOŚCI ILOŚCIOWEJ

### B.1 Jednolinijkowa tożsamość, z której wszystko wynika

Niech `A = Σ_i λ_i P_i`, `B = Σ_j μ_j Q_j` samosprzężone (najpierw: widmo punktowe),
`J` ograniczony, `f` ograniczony borelowski. Wtedy
```
Q_j ( J f(A) - f(B) J ) P_i = ( f(lambda_i) - f(mu_j) ) · Q_j J P_i .      (*)
```
Dowód: wstaw rozkłady spektralne i wykorzystaj `P_iP_k=δ_{ik}P_i`, `Q_jQ_l=δ_{jl}Q_j`. □

Z (*) natychmiast: `J f(A) = f(B) J` **wtedy i tylko wtedy, gdy** `Q_j J P_i = 0` dla
każdej pary z `f(λ_i) ≠ f(μ_j)`.

*(REC9: `NC_B_BLOCK_IDENTITY = PASS_EXACT`.)*

### B.2 Zbiór kolizji i sprzężenie przez kolizje

Dla ograniczonego borelowskiego `h` definiujemy **zbiór kolizji**
```
C_h = { (lambda, mu) : lambda != mu , h(lambda) = h(mu) }
```
oraz **sprzężenie przez kolizje**
```
kappa_h(J) = sup { ||Q_j J P_i|| : (lambda_i, mu_j) w C_h } .
```

> **Twierdzenie 7.4′ (ilościowa postać ostra).** Przy założeniach Tw. 7.4 i
> `J h(A) = h(B) J` zachodzi dla każdego ograniczonego borelowskiego `m`
> ```
> || J m(A) - m(B) J || <= 2 ||m||_inf · kappa_h(J) ,                      (7.3')
> ```
> a w szczególności `J m(A) = m(B) J` dla **wszystkich** ograniczonych borelowskich `m`
> **wtedy i tylko wtedy, gdy** `kappa_h(J) = 0`.

Dowód: z (*) i `|m(λ)−m(μ)| <= 2‖m‖_∞`; bloki z `h(λ_i) ≠ h(μ_j)` są zerowe na mocy
hipotezy, bloki z `λ_i = μ_j` nie wnoszą nic, więc zostają wyłącznie bloki z `C_h`. □

**Tw. 7.4 rozdziału jest przypadkiem szczególnym `C_h = ∅`.** Gdy `h` jest
różnowartościowe na zbiorze zawierającym oba widma, kolizji nie ma, warunek jest pusty i
teza zachodzi bezwarunkowo — dokładnie treść obecnego twierdzenia.

> **ERRATA 2026-10-23 (REC9 §B3, `REJECT`, rejestr `NC-FAL-011`).** Nierówność **ilościowa**
> (7.3′) **nie wynika** z oszacowań blokowych: kolekcja wielu małych bloków kolizyjnych może
> sumować się koherentnie do operatora o znacznie większej normie. Dokładny kontrprzykład
> `2×2`: `A = diag(0,1)`, `B = diag(2,3)`, `h(λ) = cos(2πλ)` dają `h(A) = h(B) = I`, więc
> `J h(A) = h(B) J` dla **każdego** `J`; dla `J = ½[[1,1],[1,1]]` jest `‖J‖ = 1`, a każdy
> blok `Q_j J P_i` ma normę `½`.
> **Część jakościowa pozostaje:** `REC9: NC_B_SEPARATION_NOT_NECESSARY = PASS_EXACT_FINITE_PURE_POINT`
> oraz `NC_B_FIXED_J_COLLISION_COUPLING_CRITERION = PASS_EXACT_FINITE_PURE_POINT`. Odrzucona
> jest **wyłącznie** nierówność ze stałą `2‖m‖_∞ κ_h(J)`, nie kryterium `kappa_h(J) = 0`.

### B.3 Konsekwencja, która zmienia rekomendowane sformułowanie z 17.10

**Mnożnik NIEROZDZIELAJĄCY może dać pełny transport.** `A = diag(0,1,1)`,
`B = diag(0,3,3)`, `h(λ) = cos(πλ)` — kolizja `h(1) = h(3) = −1`, więc `h` nie rozdziela:

| `J` | ‖Q₃ J P₁‖ | hipoteza ‖Jh(A)−h(B)J‖ | max po mnożnikach | kryterium |
|---|---|---|---|---|
| sprzęga kolidującą parę | 1,000e+00 | 0,000e+00 | **8,000e+00** | FAILS |
| nie sprzęga (tylko blok dopasowany) | 0,000e+00 | 0,000e+00 | **0,000e+00** | FULL TRANSPORT |
| losowy, tylko blok dopasowany | 0,000e+00 | 0,000e+00 | **0,000e+00** | FULL TRANSPORT |

Test randomizowany z wymuszonymi kolizjami: równoważność zachodzi **14/14**.

Rec9 i MT13 rekomendowali 17.10 sformułowanie w rodzaju *„kryterium jest separacja widma,
nie liczba sprawdzonych funkcji"*. **To jest poprawne jako warunek wystarczający, ale
separacja nie jest kryterium.** Kryterium jest **brak sprzężenia przez kolizje**.
Proponowana korekta sformułowania: *separacja widma jest warunkiem dostatecznym; warunkiem
koniecznym i dostatecznym jest zerowanie się bloków splatacza na parach kolidujących.*

### B.4 Uwaga Rec9 o nie-bijektywnym `J` jest wnioskiem, nie osobnym zastrzeżeniem

Rec9 pisze: *„if J is not bijective, 'generator equivalence' remains too strong even though
spectral intertwining holds"*. W języku §B.2 to po prostu `kappa_h(J)=0` przy
`J` nietrywialnie zerującym bloki. Świadek: `A=diag(1,2,5)`, `B=diag(1,2,9)`,
`J=diag(1,1,0)` daje defekt splatania **dokładnie `0,000e+00`** dla `1/(1+λ)`, `e^{−0,7λ}`,
`1_{λ>3}`, `cos(1,3λ)`, `√λ`, przy `A ≠ B`.

### B.5 Widmo ciągłe: model operatorów mnożenia, sprawdzony dokładnie

`H₁ = H₂ = L²([0,1])`, `A` = mnożenie przez `a`, `B` = mnożenie przez `b`, `J` = mnożenie
przez `j`. Wtedy `J m(A) = m(B) J` ⟺ `j·(m∘a − m∘b) = 0` p.w., więc dla wszystkich
ograniczonych borelowskich `m` ⟺ `j = 0` p.w. na `{a ≠ b}`. Hipoteza z `h` daje
`j = 0` p.w. na `{h∘a ≠ h∘b}`. **Zatem kryterium: `j = 0` p.w. na zbiorze kolizji
`{a ≠ b} ∩ {h∘a = h∘b}`** — dokładnie analogon §B.2 z `kappa_h(J) = ‖j‖_{L^∞(kolizja)}`.

Sprawdzone, `a=1`, `b=3` na środkowej trzeciej (miara kolizji `0,3333`):

| nośnik `j` | ‖j‖ na kolizji | hipoteza | max po mnożnikach | kryterium |
|---|---|---|---|---|
| wszędzie | 1,000e+00 | 0,000e+00 | 2,000e+00 | FAILS |
| tylko poza kolizją | 0,000e+00 | 0,000e+00 | **0,000e+00** | FULL TRANSPORT |
| tylko na kolizji | 1,000e+00 | 0,000e+00 | 2,000e+00 | FAILS |
| gaussowski garb poza kolizją | 3,457e-10 | 0,000e+00 | **6,913e-10** | proporcjonalnie |

Ostatni wiersz potwierdza **ilościową** postać (7.3′) z czynnikiem dokładnie 2:
`6,913e-10 = 2 × 3,457e-10`. To nie dychotomia, a oszacowanie błędu — czyli dokładnie styl,
w którym rozdział jest napisany.

*(REC9: `NC_B_MULTIPLICATION_OPERATOR_SPECIAL_CASE = PASS_SPECIAL_MODEL`. Zgodność czynnika
2 w tym jednym modelu **nie** ratuje (7.3′) w ogólności — patrz errata w §B.2.)*

### B.6 Odejmowanie prior-artu, przeciw sobie

- **`h = id` jest klasyczne.** Fuglede (1950) dla `A` normalnego; rozszerzenie
  Putnama na `JA = BJ` z `A,B` normalnymi; dowód Rosenbluma; redukcja Berberiana przez
  `H ⊕ H` (stąd nazwa Berberian–Putnam–Fuglede). Źródło: *Putnam–Fuglede theorems*,
  Encyclopedia of Mathematics. Przejście od `JA^*=JA^*` do splatania miar spektralnych jest
  standardowym wnioskiem; **strona encyklopedii go nie formułuje**, więc należy cytować
  podręcznik, nie ją.
- **Drugi skrajny przypadek** to twierdzenie Rosenbluma o rozłącznych widmach.
  §B.2 leży **między** tymi dwoma skrajnościami: `C_h = ∅` daje pełny transport,
  pełne sprzężenie przez kolizje daje jego brak.
- **Sprawdzone i NIE pokrywa:** *The Fuglede Theorem and Some Intertwining Relations*
  (arXiv:1901.09271) rozważa inne pytanie — inkluzje `BA ⊂ A f(B)` przy `B` normalnym o
  **skończonym widmie punktowym**, dla `g` ciągłych, implikacja jednostronna. Nie zawiera
  zbioru kolizji, nie zawiera charakteryzacji „wtedy i tylko wtedy", nie rozważa
  różnowartościowości `h`, a przypadek normalny wymienia jako **otwarty**.
- Ukierunkowane wyszukiwanie charakteryzacji przez zerowanie bloków
  `E_B(N) J E_A(M) = 0` dla splatania jedną funkcją **nie dało trafienia**.

**`SEARCH FAILURE != NOVELTY`.** Tożsamość (*) jest jednolinijkowa i rzecz jest niemal
pewnie folklorem teorii operatorów. **Nie twierdzę nowości matematycznej.** Twierdzę
dokładnie tyle: twierdzenie rozdziału jest warunkiem **wystarczającym**, a tu jest jego
**ilościowa równoważność** z twierdzeniem rozdziału jako przypadkiem `C_h = ∅`, z
kontrprzykładem pokazującym, że separacja nie jest konieczna. To jest „ostrość" w sensie
punktu B hierarchii planu, nie nowe prawo.

---

## C. CZEGO NIE TWIERDZĘ I CZEGO NIE SPRAWDZIŁEM

1. **Ogólna postać §B.2 dla widma ciągłego pozostaje HIPOTEZĄ.** Sprawdziłem ją dokładnie
   dla widma punktowego (§B.3, 14/14) i dla operatorów mnożenia (§B.5). Sformułowanie
   przez miary spektralne — „część pozadiagonalna `J` nośna na `C_h` zanika" — wymaga
   staranności miarowo-teoretycznej (zbiory miary zero, nierozkładalność `E_A × E_B` na
   `C_h`), której **nie przeprowadziłem**. Dla LT4: albo zacytować tylko dwa sprawdzone
   przypadki, albo zlecić domknięcie ogólne.
2. **(7.1′) sprawdziłem numerycznie, nie przedowodziłem w przestrzeni Banacha.**
   Jednostronny warunek i Grönwall są standardowe, ale wersja rozdziału operuje na
   przestrzeniach Banacha i różniczkowalności `r` wzdłuż trajektorii; **analog normy
   logarytmicznej w przestrzeni Banacha wymaga pół-skalara (semi-inner-product) lub
   funkcjonału podtrzymującego**, i tego nie wypisałem. Söderlind 2006 to pokrywa; ja nie.
3. **Nie dotykałem nic, co opiera się na moich wynikach J3** — są `[▷]` i niezaudytowane
   od sześciu dni.
4. Rozdziałów 1–6 nadal **nie audytowałem merytorycznie** (patrz audyt 001 §8). §A.6
   odwołuje się do ich tematów, nie do ich dowodów.

> **NOTA 2026-10-23 do punktu 2.** REC9 i INT7 niezależnie oznaczyły to miejsce jako
> `REPAIR_REQUIRED` (rejestr `NC-OPN-014`) i podały dwie legalne drogi: albo teza tylko dla
> przestrzeni Hilberta z iloczynem skalarnym, albo zachowanie zakresu Banacha przez
> `[u−v, g(u)−g(v)]_+ <= mu(t)‖u−v‖²` z dowodem Diniego. Obie zakazują cichej podmiany
> twierdzenia banachowskiego na `mu(G) = λ_max((G+Gᵀ)/2)`. **Luka była zgłoszona w tym
> punkcie przed audytami** — jest to więc brak zadeklarowany, nie wykryty wbrew NC.
> Naprawa pozostaje niewykonana.

---

## D. CO BYM ZROBIŁ DALEJ, W KOLEJNOŚCI DŹWIGNI

1. **Falsyfikator z Rozdziału 1** — plan przytacza wynik SW: kontrprzykład nieograniczonego
   generatora, w którym wszystkie `BD^kC = 0`, ale `K(2) = 1`. To jest **dokładnie
   sprawdzalne** i nośne dla planu (równoważność momentów i pamięci zachodzi tylko na
   zadeklarowanej klasie ograniczonej). Weryfikacja numeryczna + kontrola ostrości:
   **jak duża** może być pamięć przy zerowych wszystkich momentach.
2. **§6.10 (hadronowe źródło kosmologiczne)** — plan sam żąda „pełnego równania źródłowego,
   zmiennych, dziedzin, danych i ilościowej kontroli dokładności celu". To ten sam obszar,
   w którym Front B ma otwarte kwestie źródłowe, a (7.1′) z `mu < 0` jest tam właściwym
   narzędziem, bo kinetyka jest dyssypatywna.
3. **Pozostałe ~224 odsyłacze wewnętrzne** — kontrola, która wykryła realny błąd u mnie.

> **NOTA 2026-10-23 do punktu 2 powyżej.** Przesłanka „kinetyka jest dyssypatywna" jest
> odrzucona dla rozdz. 6 (`NC-FAL-013`), więc rekomendacja narzędziowa dla §6.10 wymaga
> najpierw **certyfikatu** ujemnej normy logarytmicznej w zadeklarowanej normie dla
> konkretnego modelu, a nie powołania się na dyssypatywność jako własność rozdziału.

---

## E. PROWENIENCJA

Kod, piaskownica NC, seedy zadeklarowane (20261018, 1810):
- `sharp.py` `7c5cc996aab3cc25d0971d6789e4d886141a9ccd255ecfcb81be5894ead5d40d` — §B.3 (14/14)
- `cont.py` `f7bac31c63b846a869bb4c8ad38047732ad96a6a8d186ea4d08ba8429a4af54d` — §B.5
- `logn.py` `22db7c3c3bfc0f66dea5eb4178084e1f12ffa1a779d1a668d81f8562f7e30433` — §A.4, §A.5
- `semi.py` `d6b800c835f86cb1527acf3cd01e22bd01dc308d5123661d0a41fd832ca2d6d5` — §A.6

*(Wszystkie cztery skrypty mają ścieżkę publiczną w `research/nc/2026-10-18/code/`.)*

Literatura sprawdzona w tym obrocie, nie z pamięci:
- G. Söderlind, *The logarithmic norm. History and modern theory*, BIT Numer. Math. **46**(3),
  631–652 (2006), DOI 10.1007/s10543-006-0069-9.
- G. Dahlquist, *Stability and Error Bounds in the Numerical Integration of Ordinary
  Differential Equations*, rozprawa doktorska, KTH Stockholm (1958); niezależnie
  S. M. Lozinskii (1958).
- D. Hinrichsen, A. J. Pritchard, *Mathematical Systems Theory I*, Springer (2005) — dowód
  `‖e^{At}‖ <= e^{mu(A)t}` i minimalność `mu`.
- *Putnam–Fuglede theorems*, Encyclopedia of Mathematics — Fuglede (1950), Putnam,
  Rosenblum, redukcja Berberiana.
- arXiv:1901.09271, *The Fuglede Theorem and Some Intertwining Relations* — sprawdzone jako
  **nie pokrywające** pytania z §B.

`EXEC_SIGN: ABSENT`. `[▷]`. Brak kanonizacji, nowości matematycznej, nowego frontu, kaskady.
Autorstwo i decyzja o włączeniu przy LT4. Audyt zewnętrzny §A i §B obowiązkowy per
`ANTI-SELF-SEALING` — ja nie mogę go sobie wystawić, a §B.2 to moja własna dedukcja.

---

## F. STAN PO AUDYTACH (dopisane 2026-10-23, nie część zapisu z 18 X)

| werdykt | audytor | rejestr |
|---|---|---|
| `NC_A_ONE_SIDED_GRONWALL_SHARPENING = PASS` | INT7 | — |
| `NC_A_HILBERT_FORM = PASS` | INT7, REC9 | — |
| `NC_A4_EXAMPLE = PASS_EXACT` | INT7 | — |
| `NC_A5_EXAMPLE = PASS_WITH_WORDING_REPAIR` | INT7 | `NC-FAL-012` |
| `NC_A_MU_LE_L = PASS_NORM_RELATIVE` | INT7 | — |
| `NC_B_BLOCK_IDENTITY = PASS_EXACT` | REC9 | — |
| `NC_B_SEPARATION_NOT_NECESSARY = PASS_EXACT_FINITE_PURE_POINT` | REC9 | — |
| `NC_B_FIXED_J_COLLISION_COUPLING_CRITERION = PASS_EXACT_FINITE_PURE_POINT` | REC9 | — |
| `NC_B_MULTIPLICATION_OPERATOR_SPECIAL_CASE = PASS_SPECIAL_MODEL` | REC9 | — |
| `NC_A_AS_GLOBAL_BANACH_REPLACEMENT = REPAIR_REQUIRED` | REC9 **i** INT7 | `NC-OPN-014` |
| `NC_A_NEGATIVE_MU_TOTAL_BOUND_DECREASES = REJECT_AS_STATED` | INT7 §4 | `NC-FAL-012` |
| `NC_A_MU_EQUALS_ASYMPTOTIC_GROWTH_RATE = REJECT_IF_INFERRED` | INT7 §5 | `NC-FAL-014` |
| `NC_A6_CH1_BRIDGE = PASS_BOUNDED_SUBCLASS_ONLY` | INT7 §8.2 | `NC-FAL-014` |
| `NC_A6_CH6_MU_NEGATIVE_GENERALIZATION = REJECT` | INT7 §8.3, M13 ROT09 | `NC-FAL-013` |
| `NC_B_KAPPA_BLOCK_MAX_QUANTITATIVE_BOUND = REJECT` | REC9 §B3 | `NC-FAL-011` |
| `MONOGRAPH_THEOREM_7_3 = RETAIN` | INT7 §10 | — |
| `CURRENT_THEOREM_7_4_EXPONENTIAL = UNAFFECTED / PASS` | REC9 | — |

Dwa pozostałe werdykty nadrzędne: INT7 `OVERALL = PASS_WITH_MATERIAL_TYPING_AND_INTERPRETIVE_REPAIRS`;
REC9 `A_PASS_HILBERT_WITH_BANACH_REPAIR / B_QUALITATIVE_PASS / B_QUANTITATIVE_BOUND_REJECT_AND_REPLACE`.
`A7_PRIOR_ART_CLASSIFICATION` nie był audytowany w tamtym obrocie INT7.

**Żadnego `CLOSED` nie nadaje NC.** Naprawa `NC-OPN-014` i odpowiedź na `NC-FAL-011`
pozostają niewykonane. Decyzja o włączeniu czegokolwiek do monografii należy do LT4.
