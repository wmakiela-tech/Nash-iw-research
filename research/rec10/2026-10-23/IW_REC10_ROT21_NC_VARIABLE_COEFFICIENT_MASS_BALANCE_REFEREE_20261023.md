# IW/NASH — REC10 ROT21
## Zmienny współczynnik konwersji kompensujący relaksację: pełna klasyfikacja liniowa i nieliniowy bilans masy

**Data:** 2026-10-23  
**Komórka:** `IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10`  
**Status:** `PASS_WITH_EXACT_CLASSIFICATION_AND_NONLINEAR_EXTENSION`  
**Zakres:** klasyczny rezerwuar z jednym kanałem i ustalonym czasem końcowym, **bez fizycznego transferu PBH/BBN**  
**Epistemic ceiling:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / BW_PENDING`

## 1. Źródła, autorstwo i subtrakcja wcześniejszych wyników

Sprawdzono oryginały:
- NC/Claude, `research/nc/2026-10-18/IW_NC_ODBIOR_MT13_NONBLIND_I_PRZYPADEK_ZDEGENEROWANY_018_20261023.md`; bezpośrednio odczytany Git blob `ec402b1e50de813c9850a22e38afe562c30d845c`.
- MT13, `research/mt13/2026-10-23/mt13_nc_active_research_weighted_yield_sufficiency_001.md`, blob `65b4076c9670e7588009ad971de93a84d2b2795e`.
- LT5/MT13 — dokładna wrażliwość celu z czasem zdarzenia w `mt13_nc_lt5_event_weighted_source_sufficiency_gate_001.md` (odrębny problem, nie zastępowany obecnym twierdzeniem).

**MT13** wcześniej wykazał, że dla liniowego modelu z ograniczonymi współczynnikami emisja całkowita `E` i końcowy rezerwuar `n(T)` wystarczają do wyznaczenia `X(T)` dla wszystkich nieujemnych historii wtedy i tylko wtedy, gdy jądro celu `w` leży w `span{1,q}`.

**NC ART018**, świadomie oznaczony `NONBLIND`, samodzielnie skontrolował liczby MT13, wykazał, że przy stałych `γ>0, κ≠0, λ≥0` zachodzi to dokładnie dla `λ=0` (nie także `λ=γ`), oraz udowodnił trwałość wniosku przy dowolnym nieliniowym zaniku `Γ(t,n)`, jeżeli `κ` jest stałe, a `λ=0`. NC pozostawił otwarte pytania `NC-OPN-011` (współczynniki zmienne) i `NC-OPN-012` (zmienna `κ(t)` przy `λ=0`).

**REC10 ROT21:** dokładny warunek konieczny i wystarczający w modelu liniowym przy zmiennych współczynnikach oraz nieliniowe rozszerzenie z relaksacją `λ(t)>0` przy odpowiednio skompensowanej `κ(t)`. Jest to elementary integrating-factor / mass-balance host; brak roszczenia do nowości.

## 2. Twierdzenie 21.1 — dokładna klasyfikacja liniowa

Niech `T>0`, `γ(t)>0` niemal wszędzie, `γ,λ` będą nieujemne i ograniczone, a `κ` ograniczone; wszystkie są mierzalne. Rozważmy

\[
\dot n=S(t)-\gamma(t)n,\qquad
\dot X=-\lambda(t)X+\kappa(t)\gamma(t)n,
\]

z tymi samymi początkowymi `n(0),X(0)` dla porównywanych źródeł `S≥0` z `L¹`.

Wprowadźmy

\[
q(s)=\exp\left(-\int_s^T\gamma(u)\,du\right),\quad
a(t)=\kappa(t)\exp\left(-\int_t^T\lambda(u)\,du\right).
\]

**Twierdzenie.** Poniższe warunki są równoważne:

(A) Dla każdych nieujemnych `S_1,S_2`, równe `∫S` i równe `n(T)` implikują równe `X(T)`.

(B) `w∈span{1,q}` prawie wszędzie, gdzie

\[
w(s)=\int_s^T a(t)\gamma(t)
 \exp\left(-\int_s^t\gamma(u)\,du\right)\,dt.
\]

(C) `a(t)=a_*` prawie wszędzie na `[0,T]`, tzn.

\[
\boxed{\kappa(t)e^{-\int_t^T\lambda}=a_*}.
\]

Wówczas

\[
w(s)=a_*(1-q(s)).
\]

**Dowód.** (A)⇔(B) pochodzi z poprawnego twierdzenia MT13 (dualność liniowych momentów). Różniczkując bezpośrednio wzór na `w` w sensie funkcji absolutnie ciągłych, otrzymujemy

\[
w'(s)=\gamma(s)\,[w(s)-a(s)],\qquad
q'(s)=\gamma(s)q(s),\qquad w(T)=0,\ q(T)=1.
\]

Jeśli `w(s)=A+B q(s)` prawie wszędzie, ciągłość wymusza równość wszędzie; warunek brzegowy daje `B=-A`. Porównanie pochodnych daje

\[
-A\gamma q=\gamma(A-Aq-a(s))
\quad\Longrightarrow\quad \gamma(s)\bigl(a(s)-A\bigr)=0
\]

prawie wszędzie. Ponieważ `γ>0` p.w., `a=A` p.w. To (B)⇒(C). Jeśli `a=a_*`, podstawienie i całkowanie funkcji przeżycia daje `w=a_*(1-q)`, czyli (C)⇒(B). QED.

**Granice kwantyfikatora:** jeśli `γ` zanika na zbiorze dodatniej miary, konieczna jest stałość `a` jedynie na aktywnym zbiorze `{γ>0}`. Jeśli `κ=0`, warunek obejmuje trywialny zerowy cel. Warunek dotyczy wybranego modelu liniowego i wszystkich dopuszczalnych źródeł, nie identyfikacji rzeczywistego hadronowego źródła.

**Przykład dodatniej relaksacji:** wybierz dowolne `λ(t)≥0`, w tym dodatnie, i ustaw
\[
\boxed{\kappa(t)=a_*\exp\left(\int_t^T\lambda(u)\,du\right).}
\]
Wtedy (C) zachodzi dokładnie, choć `λ` nie jest zerowe. Nie przeczy to NC ART018: tam `κ` było STAŁE.

## 3. Twierdzenie 21.2 — bilans nieliniowego rezerwuaru

Niech `Γ(t,n)` będzie dowolnym nieliniowym, nieujemnym prawem reakcji, dla którego równania mają rozwiązania na `[0,T]`:

\[
\dot n=S-\Gamma(t,n),\qquad
\dot X=-\lambda(t)X+\kappa(t)\Gamma(t,n).
\]

Jeżeli `a(t)=κ(t)exp(-∫_t^T λ)=a_*`, to DOKŁADNIE:

\[
\boxed{
X(T)=e^{-\int_0^T\lambda}\,X(0)
+a_*\Bigl(\int_0^T S(t)\,dt+n(0)-n(T)\Bigr).
}
\]

**Dowód.** Integrating factor for `X` gives `X(T)=exp(-∫λ)X0+∫ a(t)Γ(t,n(t))dt`; under `a≡a_*`, the final term equals `a_*∫Γ`. Integrate `n'=S-Γ` to get `∫Γ=E+n0-nT`. QED.

Ta tożsamość zachowuje nawet sprzężenie nieliniowe w `Γ` i nie wymaga liniowości mapy `S↦n(T)`. **To twierdzenie wystarczające, nie konieczno-wystarczająca klasyfikacja wszystkich możliwych nieliniowych modeli.**

## 4. Stabilność przy niedoskonałej kompensacji

Dla dwóch historii ze wspólnym `E,n(0),n(T)` i `Γ_±≥0` niech wspólna całka reakcji wynosi `R=E+n(0)-n(T)≥0`. Definiując `a(t)=κ(t)exp(-∫_t^T λ)` i dowolną stałą `c`,

\[
|\Delta X(T)| =\left|\int(a(t)-c)(\Gamma_+-\Gamma_-)dt\right|
\le2R\|a-c\|_\infty.
\]

Minimalizacja po `c` daje bezpieczny warunkowy certyfikat

\[
\boxed{
|\Delta X(T)|\le
R\Bigl(\operatorname{ess\,sup}a-\operatorname{ess\,inf}a\Bigr)
}
\]

dla ograniczonego rzeczywistego `a`. To **granica wystarczająca**, nie ostre optimum po ograniczonej przez ODE klasie trajektorii. Nie jest też fizycznym przedziałem niepewności.

## 5. Niezależne dodatnie źródła i nieliniowy test ODE

Wybierz:
`T=2`, `γ(t)=2+0.25sin t`, `λ(t)=0.5+0.15cos t`,
`Γ(t,n)=γ(t)(n+β n²)`, `β∈{0,1.5}`,
`a_*=0.1`, `κ_comp(t)=a_*exp(0.5(2-t)+0.15(sin2-sin t))`,
`n(0)=0`, `X(0)=0.1`.

Emisja: stałe dodatnie tło `0.1` plus trzy rozłączne, nieujemne, klasy C¹, znormalizowane do całki 1 impulsy typu podniesiony cosinus. Dla `S+` wagi (0.7,1.4,0.9); dla `S-` wagi (1.4,w,1.6−w), gdzie `w` wyznaczono przez bisekcję/brentq dla równości `n+(T)=n-(T)` w ODE. Wszystkie wagi są dodatnie, obie emisje dokładnie `E=3.2`. Wersja `β=1.5` ma `w=0.6752450898102651`.

Bez korzystania ze wzoru na `X(T)` w integratorze, rozwiązano oba układy 2D metodą DOP853, `rtol=3e-12`, `atol=3e-14`, dwa maksymalne kroki. Następnie wartość `X(T)` obliczona bezpośrednio została porównana z zamkniętym bilansem.

| β | n(T) obu | \(\Delta X_{\mathrm{comp}}(T)\), `max_step=.02` | \(\Delta X_{\kappa\equiv0.1}(T)\) |
|---:|---:|---:|---:|
| 0 | 0.480819927166 | −1.315e−11 | +0.010671350379 |
| 1.5 | 0.212236747372 | +1.923e−12 | +0.012850901162 |

Różnice w scenariuszu kompensowanym są na poziomie błędu numerycznego, a przy identycznych źródłach i jedynie stałym `κ` istotnie różne. Dwa kroki czasowe potwierdziły kontrolę. Test **nie** jest dowodem równości (tę zapewnia algebra); jest falsyfikatorem błędów implementacji.

**Kod:** `IW_REC10_ROT21_NC_VARIABLE_COEFFICIENT_NONLINEAR_COMPENSATION_REPRO_20261023.py`, niezależny SciPy/NumPy.

## 6. Decyzja naukowa i nonmap

- `NC-OPN-011` otrzymuje warunkową **pełną klasyfikację w liniowym modelu z γ(t)>0 p.w.** Istnieją przypadki `λ(t)>0`, jeśli `κ(t)` jest odpowiednio dobrane.
- `NC-OPN-012` — przy `λ=0` zmienne `κ(t)` dają dostateczność wtedy i tylko wtedy, gdy `κ` jest stałe na aktywnym zbiorze w modelu LINIOWYM. Przy dowolnym nieliniowym `Γ` stałe efektywne `a` pozostaje wystarczające; ogólna konieczność dla wszystkich nieliniowych Γ nie została udowodniona.
- `NC-OPN-010` (pełna klasyfikacja dowolnych nieliniowych Γ przy λ>0) pozostaje otwarte poza rodziną wykazaną tutaj. Nie wolno przypisywać NC tego wyniku: REC10 znał cały pakiet NC ART018, zatem jest to `NONBLIND_INDEPENDENT_FOLLOWUP`, nie osłonięta predykcja.
- `κ(t)` dobrane do `λ(t)` jest **zaprojektowaną konstrukcją**, nie obserwacją fizycznej stałości hadronowego udziału reakcji i nie uprawnia do transferu na sześć hadronów, zależne od X sprzężenia, source-table PBH, rzeczywisty cel przy zdarzeniu \(T=T_{\mathrm{nuc}}\), Yp/DH, teorię grawitacji ani DTC0a.

**Prior art:** integrating factors, compartment mass balance, time-varying linear systems and finite-dimensional sufficient moment rank. Standard mathematics; no novelty claim.

**Final:** `PASS_WITH_EXACT_CLASSIFICATION_AND_NONLINEAR_EXTENSION / MATURE_HOST / NONBLIND / NO_NEW_TASK_CASCADE / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / BW_PENDING`.