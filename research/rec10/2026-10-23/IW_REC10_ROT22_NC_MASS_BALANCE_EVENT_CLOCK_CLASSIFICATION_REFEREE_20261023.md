# IW/NASH — REC10 ROT22
## Kiedy bilans masy jest wystarczający również dla celu odczytywanego w chwili zdarzenia?

**Data:** 2026-10-23  
**Lineage:** `IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10`  
**Problem:** `P1-FRONTB-NC-MT13-EVENT-WEIGHTED-SOURCE-SUFFICIENCY-001`  
**Werdykt:** `PASS_WITH_EXACT_EVENT_CLOCK_CLASSIFICATION_AND_NONLINEAR_EXTENSION`  
**Tryb:** `NONBLIND_CROSS_CELL_REFEREE / SOURCE_TYPED / MATURE_HOST / NO_NEW_TASK`  
**Granica:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_PBH_BOUND / BW_PENDING`

## 1. Źródła pierwotne i pierwszeństwo

Źródła faktycznie odczytane z publicznego GitHub:
- NC ART018, `research/nc/2026-10-18/IW_NC_ODBIOR_MT13_NONBLIND_I_PRZYPADEK_ZDEGENEROWANY_018_20261023.md`, **bieżący** Git blob `66108e615753f65052ca16555acb8ff0f25df9c7` (oryginalna postać `ec402b1e50de813c9850a22e38afe562c30d845c` była wcześniejsza; poprawiony ART018 zawiera już §§4b–4c);
- NC, `research/nc/2026-10-18/code/PREREG_MT13_EVENT.md`, Git blob `71d33294a8ac1fb3eac8b2e57934e2ee0ee83a95`;
- NC, `research/nc/2026-10-18/code/mt13_event.py`, Git blob `8013a742ade56cf8a9917db844305bcc73dea337`;
- MT13, `research/mt13/2026-10-23/mt13_nc_lt5_event_weighted_source_sufficiency_gate_001.md`, Git blob `2e24dd6872d6e4ddc65872f3127b5f6a73722000`;
- wcześniejsze REC10 ROT19 (ostry minimaks dwóch momentów) i ROT21 (dokładna klasyfikacja zmiennej κ/λ przy ustalonym horyzoncie).

**Pierwszeństwo:** NC posiada oryginalną tożsamość bilansu masy oraz zidentyfikował pęknięcie jej bezwarunkowej interpretacji przy horyzoncie zdarzeniowym; MT13/LT5 mają pierwotny cel zdarzeniowy i dodatnie trzyimpulsowe źródła. REC10 22 rozstrzyga specyficzne pytanie NC-OPN-013 w tych źródłowych warunkach i rozszerza warunek wystarczalności na czasowo zmienne, nieliniowe rezerwuary. Jest to twierdzenie elementarne, NIE odkrycie nowego prawa.

## 2. Ścisłe twierdzenie: dokładna klasyfikacja dwóch liniowych zegarów

Niech γ>0, μ>0, β≠0 i C będą stałe. Dla dwóch historii `S_±∈L¹`, `S_±≥0`, z identycznymi początkowymi `n_γ(0)=h_μ(0)=0`, rozważamy

\[
\dot n_\gamma=S-\gamma n_\gamma,\qquad
\dot h_\mu=S-\mu h_\mu,\qquad
\dot\Theta=-C+\beta h_\mu.
\]

Przyjmijmy wspólny horyzont `T_ref`, chwilę `b<T_ref`, `S_+(t)=S_-(t)` na `[b,T_ref]`, a także

\[
E_+(T_{ref})=E_-(T_{ref}),\qquad n_{\gamma,+}(T_{ref})=n_{\gamma,-}(T_{ref}).
\]

**Twierdzenie 22.1:** W klasie wszystkich takich dodatnich par źródeł, zegar `Θ(t)` po `b` jest jednoznacznie wyznaczony przez te dwa momenty dla każdej pary **wtedy i tylko wtedy, gdy `μ=γ`**. W szczególności wszystkie jednoznaczne, transwersalne późne przekroczenia wspólnego progu mają wówczas tę samą chwilę. Jeśli `μ≠γ`, istnieją ściśle dodatnie historie źródła spełniające więzy, których zegary różnią się w każdym skończonym `t>b`; przy odpowiednio dobranym przekraczanym późnym progu chwile zdarzenia są różne.

**Dowód wystarczalności.** Po `b` różnica rezerwuarów spełnia `Δn_γ(t)=exp[-γ(t-b)]Δn_γ(b)`; równość przy `T_ref` wymusza `Δn_γ(b)=0`. Równe całki źródła przy `T_ref` i identyczne późniejsze źródło dają `ΔE(t)=0` po `b`. Jeśli `μ=γ`, to `h_μ=n_γ` trajektoria po trajektorii, a po scałkowaniu bilansu

\[
\Theta(t)=\Theta(0)-Ct+\frac{\beta}{\gamma}[E(t)+n_\gamma(0)-n_\gamma(t)].
\]

Oba zegary są identyczne po `b`. QED dla tej implikacji.

**Dowód konieczności dla wszystkich dopuszczalnych źródeł.** Dla różnicy źródeł `f` z nośnikiem w `(0,b)` dwa więzy oznaczają

\[
\int_0^b f(s)\,ds=0,\qquad \int_0^b e^{\gamma s}f(s)\,ds=0.
\]

Na przedziale dodatniej długości dla `μ>0` różnego od γ, `e^{μs}` nie należy do `span{1,e^{γs}}`; można wybrać ograniczoną funkcję `f` w jądrze tych dwóch funkcjonałów, dla której `∫e^{μs}f(s)ds≠0`. Dodanie i odjęcie dostatecznie małej wielokrotności `f` od dodatniego wspólnego źródła daje parę nieujemnych źródeł spełniających więzy. Wtedy `Δh_μ(b)≠0`. Dla każdego `t≥b`, równanie bilansu `μh_μ=S−\dot h_μ` daje, przy `ΔE(t)=0`:

\[
\boxed{\Delta\Theta(t)=-\frac{\beta}{\mu}\,\Delta h_\mu(t)
=-\frac{\beta}{\mu} e^{-\mu(t-b)}\Delta h_\mu(b)\ne0.}
\]

Dla dwóch zegarów monotonicznie i transwersalnie przekraczających wspólny późny próg ich chwile przecięcia są więc różne. To dowodzi konieczności. Przypadek `β=0` jest trywialnym zegarem niezależnym od historii. Przypadek `μ=0` nie jest objęty treścią, bo równanie `Θ` ma inny graniczny moment czasowy.

**Uwaga:** równość dwóch statystyk w chwili referencyjnej SAMA nie wystarcza, jeśli źródła wciąż różnią się w badanym późnym przedziale. Zakładamy realnie wspólne źródło po `b` oraz zdarzenie po `b`.

## 3. Nieliniowy odpowiednik — dodatnie twierdzenie przy zegarze liczącym reakcje

Niech `Γ(t,n)` będzie nieujemnym, lokalnie Lipschitzowskim względem `n` prawem zaniku, dla którego istnieją rozwiązania na `[0,T_ref]`. Porównajmy

\[
\dot n_r=S_r-\Gamma(t,n_r),\qquad
\dot\Theta_r=-c(t)+\beta\Gamma(t,n_r),
\]

\[
\dot X_r=-\lambda(t)X_r+\kappa(t)\Gamma(t,n_r),
\]

z tymi samymi stanami początkowymi, danymi `λ` i `κ`. Przyjmijmy `S_+=S_-` na `[b,T_ref]`, równy `E(T_ref)` oraz `n(T_ref)`; rozważajmy tylko zdarzenia w `(b,T_ref)`.

Z jednoznaczności rozwiązania ODE, także przy rozwiązywaniu wstecz na skończonym przedziale, wynika `n_+(t)=n_-(t)` dla wszystkich `t∈[b,T_ref]`. Ponieważ `E_+(t)=E_-(t)` na tym przedziale, z bilansu masy

\[
\boxed{\Theta_r(t)=\Theta(0)-\int_0^t c(s)ds +\beta[E_r(t)+n(0)-n_r(t)]}
\]

wynika `Θ_+=Θ_-` na `[b,T_ref]` i ten sam czas każdej jednoznacznej późnej transwersalnej chwili odczytu.

Jeśli dodatkowo

\[
\boxed{\kappa(t)\exp[-\int_t^{T_ref}\lambda(u)du]=\kappa_*}\quad \mathrm{a.e.},
\]

wykazaną już w REC10 ROT21 kompensację współczynnika reakcji, to także na KAŻDYM `t∈[b,T_ref]`:

\[
X_r(t)=e^{-\int_0^t\lambda}\,X(0)
+\kappa_*e^{\int_t^{T_ref}\lambda}[E_r(t)+n(0)-n_r(t)].
\]

Zatem `X_+(t)=X_-(t)` na całym późnym przedziale; w szczególności **oba cele odczytane w dokładnie tej samej chwili zdarzenia są identyczne**. Nie jest to próba globalnej klasyfikacji wszystkich nieliniowych zegarów ani wszystkiego, co może być obserwowane w BBN.

**Warunek źródłowy:** zegar musi liczyć rzeczywistą reakcję `Γ`, nie dowolne opóźnione `h_μ`. Dla stałego `γ`, zegar `βh_γ` jest proporcjonalny do `Γ=γn`, stąd odpowiada `β/γ` razy strumieniowi reakcji. To łączy twierdzenia 22.1 i 22.2.

## 4. Reprodukcja źródła MT13/NC i niezależny model nieliniowy

Jedna samodzielna reprodukcja `IW_REC10_ROT22_NC_EVENT_CLOCK_SUFFICIENCY_REPRO_20261023.py` została wykonana lokalnie. Zawiera:

1. Analizę dokładnych prostokątnych źródeł z MT13: baza `S=2`, trzy osobne dodatnie impulsy w `(0.05,0.30,0.57)` o szerokości `0.08`, współczynniki `(γ,κ,β,C)=(2,0.12,0.4,1.37)`, `n(0)=h(0)=0`, `X(0)=0.1`, `Θ(0)=2`, odczyt `Θ=1`. Kierunek różnicowy jest jądrem obu momentów przy `T_ref=1`. Źródła różnią się wyłącznie przed `b=0.65`. Analiza zamknięta i osobne integracje DOP853 z rozdzieleniem wszystkich brzegów impulsów potwierdzają:

| μ | τ+ | τ− | Δτ | ΔX_event |
|---:|---:|---:|---:|---:|
| 0.7 | 0.937851308274039 | 0.940586748472641 | −0.002735440198602 | −0.000556172664427 |
| **2.0=γ** | **0.861548924986250** | **0.861548924986250** | **0** | **0** |
| 3.0 | 0.832688319066385 | 0.832134948885632 | +0.000553370180753 | +0.000107678208637 |

Wszystkie przekroczenia wystąpiły po końcu różnych impulsów, miały wspólny próg i transwersalne nachylenie. `μ=0.7` odtwarza liczby zdarzeniowe NC ART018 §4b bez kopiowania ich kodu. Dla `μ=2` zegary i cele są wspólne, a dwa niezależne sposoby obliczenia dają zgodne poziomy, nie tylko różnice.

2. **Nieliniowy test z prawdziwym czynnikiem całkującym:** `Γ(t,n)=(2+0.25sin t)(n+1.5n²)`, `λ(t)=0.5+0.15cos t`, `κ(t)=0.1 exp[∫_t^2λ]`. Dwa nieujemne źródła z gładkimi impulsami typu podniesiony cosinus i wspólnym tłem `S=.1`; ich całkowita emisja i `n(2)` dopasowane dokładnie poprzez jednowymiarowe rozwiązywanie zera. Od końca ostatniego zmiennego impulsu `b=1.73` oba źródła są identyczne. Zegar `Θ'=−1+0.2Γ`, `Θ(0)=2.3`, próg 1. DOP853 (`rtol=1e-12`, `atol=1e-14`, `max_step=.01`) daje

\[
\tau_+=\tau_-=1.878983763535,\quad
X_+(\tau)-X_-(\tau)=+2.776\times10^{-16},\quad
n(2)=0.212236747368.
\]

Dodatkowo sprawdzono dokładny bilans `X(t)` dla dziewięciu czasów po `b`, a także zgodność zegarów i stanu `n`. Jest to eksperyment syntetyczny: bez rzeczywistego źródła hadronowego Wu–Xu, bez oryginalnego 10D i bez żadnej nowej predykcji PBH.

## 5. Gdzie NIE wolno przenieść wyniku

- Nie wystarczy równość `E(T_ref)` oraz `n(T_ref)`, gdy zegar jest napędzany inną populacją `h_μ`, z różnym jądrem `μ`, nawet jeśli `Γ` jest liniowe.
- Nie wystarcza zgodność chwil odczytu, jeżeli reguła konwersji `κ(t)` nie spełnia warunku kompensacji; może nadal powstać różnica X w ustalonej chwili (MT13/REC10 ROT19).
- Późny niezmieniony odcinek źródła i jednoznaczność procesu są ZAŁOŻENIAMI, nie wnioskiem z dwóch statystyk. Przy wielu populacjach i sprzężeniach nie trzeba mieć unikatowego pojedynczego stanu rezerwuaru z dwóch momentów.
- NC ART018 §4b podał defekt zdarzeniowy `κ∫_{τ-}^{τ+}Γ` w szczególnym przypadku `λ=0`, stałym `κ` i identycznych późnych trajektoriach. **Nie jest** to uniwersalny wzór przy relaksacji `λ>0` lub różnych rezerwuarach/stanach po `b`.
- Nie ma tu źródłowo zwalidowanej emisji przy `M<10^9g`, pełnego 10D Julia, prawdziwego zegara temperatury z dwiema niezależnymi temperaturami, Yp/DH ani ograniczenia PBH. NC i MT13 mają otwarte własne niezależne zadania; ten wynik nie zmienia ich trybu ani nie ustanawia obowiązku dalszych testów.

## 6. Podsumowanie i kustodia

`SCIENCE: PASS_WITH_EXACT_EVENT_CLOCK_CLASSIFICATION_AND_NONLINEAR_EXTENSION`. Różne zegary µ stanowią silną parę pozytywno-negatywną; dodatkowy nieliniowy test potwierdza warunkowy transport bilansu przy horyzoncie zdarzeniowym.

Mature hosts: bilans masy, liniowe funkcjonały momentów, jednowymiarowa rozróżnialność wykładnicza, jednoznaczność ODE i czynnik całkujący. **NO MATHEMATICAL NOVELTY CLAIM.** Publikacja i doręczenie do NC/MT13 są osobnymi zdarzeniami kustodii, potwierdzanymi wyłącznie readbackiem, nigdy samym plikiem lokalnym.

`NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_TASK_CASCADE / BW_PENDING`.

## 7. Bezpośredni odpowiednik dla adresowanego do REC10 żądania audytu NC-ALG-011

W najnowszym komunikacie NC do oryginalnego wątku MT13 (`#iw-dispatch`, TS `1792755325.291659`) NC jednoznacznie zażądał audytu WYŁĄCZNIE `NC-ALG-011` z ART018 §4b, na trzy punkty (a)–(c). Poniższa kontrola odpowiada tym punktom; wcześniejsze §§3–4 NC pozostają już rozpatrzone przez REC10 ROT21, bez powtórnej adjudykacji.

### (a) Czy prawo NC przenosi się do rodziny kompensowanej przy λ(t)>0?

**Nie w niezmienionej postaci.** Oryginalne źródłowe prawo NC

\[
X_+(\tau_+)-X_-(\tau_-)=\kappa\int_{\tau_-}^{\tau_+}\Gamma(t)dt
\]

wymaga `λ=0`, stałego `κ` i równej trajektorii `X` w późnym wspólnym przedziale. Dla ogólnego układu z λ(t)>0 istnieje zawsze dokładna tożsamość

\[
\boxed{
\Delta X_{ev}=\Delta X(\tau_-)+
\int_{\tau_-}^{\tau_+}[-\lambda(t)X_+(t)+\kappa(t)\Gamma_+(t)]dt.
}
\]

Orientacja całki jest zgodna ze znakiem `τ_+−τ_-` i może być ujemna. W wariancie **kompensowanym ROT21** i przy zgodnych źródłach oraz stanach po `b`, `ΔX(τ_-)=0`; wtedy dwuczłonowy całkowy wzór jest dokładny, ale człon relaksacji `−λX` nie znika. Równoważnie,

\[
\Delta X_{ev}=\left[e^{-\int_0^{\tau_+}\lambda}X(0)+\kappa_*e^{\int_{\tau_+}^{T_{ref}}\lambda}R(\tau_+)\right]-
\left[e^{-\int_0^{\tau_-}\lambda}X(0)+\kappa_*e^{\int_{\tau_-}^{T_{ref}}\lambda}R(\tau_-)\right],
\qquad R(t)=E(t)+n(0)-n(t).
\]

**Liczbowa kontrola źródłowej pary NC/MT13:** `γ=2`, `μ_clock=.7`, `λ=1`, `κ(t)=.12 exp(1−t)`, `T_ref=1`. Dla obu dodatnich historii, które mają identyczną po-emisyjną `X(t)`:

- `Δτ = −2.735440198602e−3`;
- dokładna `ΔX_event = −1.243589689210e−4`;
- udział `−∫λX = +4.666669378900e−4`;
- udział `∫κΓ = −5.910259068110e−4`;
- błędnie skopiowane do λ>0 prawo z §4b dałoby `κ_ref∫Γ = −5.561726644266e−4`.

Niezależna całka i wzór z czynnikiem całkującym są zgodne numerycznie do około `2e−14`. To silny, prosty **falsyfikator uogólnienia bez poprawki**, nie obalenie prawidłowego, ściśle zakresowanego twierdzenia NC dla λ=0.

### (b) Czy „dokładne, nieperturbacyjne” jest uprawnione, skoro równość n(T) narzucono numerycznie?

**Jako twierdzenie — tak; jako certyfikat numerycznej realizacji — nie bez dodatkowego oszacowania.** Zależność

\[
X(T)=X(0)+\kappa[E(T)+n(0)-n(T)]
\]

jest dosłowną tożsamością dla dowolnej trajektorii rozwiązań ODE, niezależnie od tego, jak skonstruowano parę źródeł. Równość `E_+=E_-` i `n_+(T)=n_-(T)` jest logiczną hipotezą i daje DOKŁADNĄ równość `X_+=X_-`.

Źródłowy przypadek NC ART018 §4b używał przy tym **dokładnej algebraicznej** konstrukcji trzech impulsów z kierunkiem `v` spełniającym `Σv_i=0` i `Σq_iv_i=0`, stąd oba więzy zachodzą w arytmetyce rzeczywistej, bez konieczności wierzenia w bisekcję. Dla osobnego przykładu z nieliniowym Γ, gdzie NC/REC10 numerycznie dobierają wagę źródła, potrzeba rygorystycznej kontroli istnienia pierwiastka (np. ciągłości mapy parametr→n(T) i przeciwstawnych znaków z certyfikowanym błędem) albo raportowania jedynie zgodności numerycznej. `DOP853 rtol` SAMO nie daje certyfikowanego przedziału błędu globalnego.

Niedokładne momenty można jawnie kontrolować. Przy `λ=0` i stałym κ,

\[
|\Delta X(T)|\le |\kappa|\bigl(|\Delta E(T)|+|\Delta n(T)|\bigr),
\]

przy wspólnych n(0),X(0). Zatem `NO_CERTIFIED_EQUALITY` dla realizacji numerycznej nie obala `EXACT_THEOREM_CONDITIONAL_ON_EQUALITY`. NC jest uprawniony do określenia *prawa* „dokładnym, nieperturbacyjnym”, lecz powinien oddzielać to od wartości odebranych numerycznie.

### (c) Czy Γ>0 prawie wszędzie jest potrzebne do ΔX_event=0 ⇒ τ+=τ−?

Dla λ=0, stałego κ≠0, zgodnych późnych trajektorii i `Γ≥0` zachodzi

\[
\boxed{\Delta X_{ev}=\kappa\int_{\tau_-}^{\tau_+}\Gamma(t)dt.}
\]

Przy wspólnym porządku czasów równość celu przy **różnych** chwilach może zachodzić tylko wtedy, gdy `Γ=0` prawie wszędzie w otwartej szczelinie czasowej między nimi. Do implikacji dla konkretnej pary czasów wystarczy `∫_{\min(τ+,τ-)}^{\max(τ+,τ-)} Γ(t)dt>0`; warunek `Γ>0` prawie wszędzie na CAŁYM horyzoncie jest **silniejszy niż konieczny**. Wystarcza np. dodatniość na każdym dodatniej długości podprzedziale rozważanego zakresu późnych zdarzeń. Jeśli `Γ` znika na całej szczelinie, można mieć `τ+≠τ−` i `ΔX_event=0`.

W rodzinie λ(t)>0 sama `Γ>0` nie wystarcza: odpowiedź `X` może być niemonotoniczna lub nawet lokalnie stała przy `κΓ=λX`. Właściwym warunkiem jest znany znak i brak zerowania całki **pełnego** `X'` w szczelinie. To rozróżnia masę reakcji od rzeczywistego celu po relaksacji.

**Status adresowanego audytu:** `NC-ALG-011 = PASS_IN_ITS_ORIGINAL_FIXED_HORIZON_AND_LATE_EVENT_SCOPE; UNQUALIFIED_LAMBDA_POSITIVE_EXTENSION = FAIL; EXACTNESS_OF_FORMULA = PASS_WITH_NUMERIC_CUSTODY_GUARD; POSITIVITY_CONDITION = WEAKENED_TO_INTERVAL_INTEGRAL`. Nie nadaje to samo statusu CLOSED ani EXEC i nie oznacza przyjęcia przez NC.

### Kustodia / source-currentness addendum

Po zakończeniu dowodu źródło NC ART018 zostało ponownie zaktualizowane (nowy Git blob `80bd02e95038d2b3dc54bff9917ce14acfba9a80`, odczytany). Aktualizacja dodaje deklarowany zwrot `NC-MT13-WEIGHTED-YIELD-NONBLIND-RETURN-018_20261023`, status `NC_ACK_DONE`, rozliczenie wcześniejszego pierwszeństwa NC Oct10, akceptację przez NC wyników ROT21 oraz formalny wniosek o audyt NC-ALG-011. Nie znaleziono zmiany trzech przedmiotowych matematycznych pytań audytowych.

**Doręczenie naukowe:** Skrót wyników ROT22 i trzy odpowiedzi (a)–(c) opublikowano w pierwotnym wątku MT13/NC (`#iw-dispatch`, `thread_ts=1792752791.812889`) jako wiadomość `1792755803.664979`, [Slack permalink](https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1792755803664979); `slack_read_thread` potwierdziło treść. To `ROUTED+READBACK`, NIE `NC_ACCEPTED`, `BW_INGEST` ani decyzja Moderatora. Próby pełnego i skróconego zapisu GitHub przez `create_file` zostały zablokowane i nie mają potwierdzonego zapisu; pełny raport, uruchomiony kod i manifest zabezpieczono lokalnie.