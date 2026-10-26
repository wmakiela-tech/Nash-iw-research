# IW/NASH — DAX-S7 — obrót 58 (2026-10-26)

## Niezależny falsyfikator termodynamiczny: równanie chłodzenia Wu–Xu i wynik słabych przemian neutronów przy β=0

**Status:** `SOURCE_EQUATION_PORT / SOURCE_TABLE_BLOB_VERIFIED / GRID_CONVERGENCE_PASS / CONDITIONAL_THERMODYNAMIC_COMPARATOR / NO_FULL_JULIA / NO_EXEC / NO_CANON`.

**Funkcja:** DAX-S7, niezależna kontrola warunków falsyfikacji w linii IW/NASH; materiał nie ustanawia kanonu LT/NCDG, fizycznych ograniczeń PBH ani nowości naukowej.

### 1. Hipoteza i motywacja

Obroty 54–57 wykazały w numerycznym modelu kontrolnym większą wrażliwość udziału neutronów na definicję gęstości barionowej niż na brak członu ekspansyjnego `−3Hn_h` w równaniach hadronów. Ten test nie zakłada, że tamte efekty wyczerpują listę błędów systematycznych: sprawdza osobno, **bez PBH i bez hadronów**, czy wybór prawa chłodzenia zmienia uzyskiwane `X_n(T_nuc)` na skali istotnej dla deklarowanej precyzji obserwabla.

### 2. Źródło i typy twierdzeń

**Bezpośrednio ze źródła:** `Fenyutanchan/Primordial-Black-Hole`, `arXiv-2509.05618/main-scan.jl`: 

```julia
d_log_ρ_SM_dη = -4 + d_ln_N_ρ_d_ln_T / (3 + d_ln_N_s_d_ln_T) - d_m_PBH_dt * n_PBH / (H * ρ_SM)
dXₙ_dt_SM = -Γₙ_SM * (Xₙ - (1 - Xₙ) * exp(-x))
dXₙ_dt_decay = -Xₙ / τ_n
Γₙ_SM = (255 / τ_n) * (12 + 6 * x + x^2) / x^5
```

W tym obrocie `β=0`, więc człon wtrysku energii PBH znika. Wartości `g_ρ(T)`, `g_s(T)`, pochodne oraz interpolację logarytmiczną odtworzono bezpośrednio z pliku źródłowego:

- https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/main-scan.jl
- https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/data/ext/N_around_m_e.csv
- Git blob SHA danych: `93f2494f026c5d0587ea40fe08bb938dd9d01fa8` (1000 punktów).

**Wyprowadzenie algebraiczne (nie źródłowe twierdzenie autorów):** oznaczmy `r=dln g_ρ/dln T`, `s=dln g_s/dln T`. Wówczas:

\[
C_{\mathrm{source}}=\frac{d\ln\rho}{d\ln a}=-4+\frac{r}{3+s},\qquad
\frac{d\ln T}{d\ln a}=\frac{C_{\mathrm{source}}}{4+r}.
\]

Dla termodynamicznego układu z zachowaniem entropii współporuszającej, `g_s(T) T^3 a^3 = const`, wynika zamiast tego:

\[
C_{\mathrm{ad}}=-\frac{3(4+r)}{3+s},\qquad
\frac{d\ln T}{d\ln a}=-\frac{3}{3+s}.
\]

**Ograniczenie:** `C_ad` jest kontrfaktycznym **wariantem kontrolnym**; konieczne jest osobne ustalenie, czy tablice i równania Wu–Xu reprezentują właściwy całkowity układ entropii, zwłaszcza podczas odsprzęgania neutrin. Różnica algebraiczna nie jest automatycznie błędem pełnej fizyki.

### 3. Niezależny układ kontrolny

Odtworzono przy `β=0`:

\[
\frac{dX_n}{dt}=-\frac{255}{\tau_n}\frac{12+6x+x^2}{x^5}\left[X_n-(1-X_n)e^{-x}\right]-\frac{X_n}{\tau_n},\quad
x=Q/T,\quad \tau_n=878.4\,\mathrm{s}.
\]

Ekspansja: `H(T)=0.20658852676118475 * sqrt(g_ρ(T)) * T_MeV² s⁻¹`. Warunek początkowy przy `T=10 MeV`: `X_n=[1+exp(Q/T)]⁻¹` (równowaga słaba). Końcowa temperatura: `T_nuc=0.07818527068831995 MeV`. Od T=10 MeV do `T_nuc` dokładne węzły oryginalnej tablicy termodynamicznej wyznaczają **747** przedziałów. Każdy podzielono na 4, 8, 16 albo 32 podkroki RK4 po `ln T`. Węzły traktowano jednostronnie, aby uniknąć zmieszania skoków pochodnej interpolacji logarytmicznej. Jawne RK4 przy 1–2 podkrokach na przedział jest niestabilne ze względu na sztywność przemian słabych w wysokiej temperaturze; takich wyników nie używano.

**Ważne:** czas liczony *od osiągnięcia 10 MeV*, nie od momentu powstania PBH. Nie ma modelu hadronów ani pełnego BBN, więc obliczona `Yp` jest wyłącznie przepuszczeniem `X_n` przez dwie mapy algebraiczne.

### 4. Wyniki o kontrolowanej zbieżności

| Podkroki/przedział | `X_n` kod Wu–Xu | `X_n` adiabatyczne | Różnica `ΔX_n` |
|---:|---:|---:|---:|
| 4 | 0.109032531073 | 0.110249533111 | +0.001217002038 |
| 8 | 0.109032531073 | 0.110249533111 | +0.001217002038 |
| 16 | 0.109032531073 | 0.110249533111 | +0.001217002038 |
| 32 | 0.109032531073 | 0.110249533111 | +0.001217002038 |

**Ostateczne wartości kontrolne przy 32 podkrokach:**

| Obserwabla/test | Source cooling | Adiabatic comparator | Delta |
|---|---:|---:|---:|
| `X_n(T_nuc)` | 0.109032531073 | 0.110249533111 | +0.001217002038 |
| `Y_{p,code}=2X_n/(1−X_n)` | 0.244750868860 | 0.247821242503 | +0.003070373643 |
| `Y_{p,mass}≈2X_n` | 0.218065062146 | 0.220499066222 | +0.002434004076 |
| `Δt(10MeV→T_nuc)` | 214.960142800 s | 208.856755183 s | −6.103387617 s |

Różnica `ΔY_{p,code}/0.003≈1.02346` jednostki obserwacyjnej niepewności użytej w dotychczasowym audycie. To **wrażliwość predykcji modelowej**, a nie zmierzony błąd obfitości helu.

### 5. Niezależny niezmiennik: współporuszająca entropia

Przy wspólnej interpretacji `g_s` jako entropicznych stopni swobody układu, `S_com∝g_s(T)T³a³`. Zintegrowanie źródłowego `C_source` przy β=0 z oryginalnymi tablicami daje warunkowo:

\[
\frac{S_{\mathrm{com}}(T_{\mathrm{nuc}})}{S_{\mathrm{com}}(10\,\mathrm{MeV})}\simeq 1.14678.
\]

Jest to około **+14.68%** odchylenia od zachowania entropii dla wspólnego układu adiabatycznego, choć źródłowe równanie nie zawiera w tym porównaniu zewnętrznego wtrysku PBH. Dla wariantu adiabatycznego wyrażenie jest tożsamościowo równe 1. **Nie wolno zamieniać tej kontroli w twierdzenie o fizycznej niekonserwacji bez udowodnienia zgodności definicji `g_s` z całkowitą entropią sektorów modelu.**

### 6. Niezależność od warunku wysokotemperaturowego

Powtórzenie z równowagowym początkiem przy temperaturach 2, 5 i 10 MeV daje przy 16 podkrokach (source vs comparator):

- 2 MeV: `0.109031659707` vs `0.110248650880`;
- 5 MeV: `0.109032531073` vs `0.110249533111`;
- 10 MeV: `0.109032531073` vs `0.110249533111`.

Efekt źródło–komparator utrzymuje się do ~`10⁻⁸`, bez podatności na dobór początku 2–10 MeV.

### 7. Hierarchia z poprzednimi falsyfikatorami

- **Obrót 53:** różne mapy obserwabla `Y_p` i odmienne obszary akceptacji; to *niezależny* problem definicji obserwabla.
- **Obroty 54–55:** przy `β=3×10⁻¹⁹` korekta baryonowa zmienia `X_n` o około `−0.002572` w modelu z hadronami.
- **Obroty 56–57:** dla tego samego scenariusza brakujący `−3H n_h` powodował około `−1.2×10⁻⁸` w `X_n` w modelu kontrolnym.
- **Obrót 58:** przy **β=0**, alternatywny adiabatyczny model chłodzenia przesuwa `X_n` o `+0.001217`.

**Nie dodajemy powyższych liczb**: dotyczą różnie zdefiniowanych eksperymentów, a równoczesna integracja wszystkich wariantów jeszcze nie nastąpiła. Rzeczywiste ograniczenia PBH nie zostały tutaj wyznaczone.

### 8. Zapis, odtwarzalność i negatywna wiedza

Artefakty: pełny raport Markdown, skrypt Python, CSV z 4 poziomami zbieżności, JSON z manifestem i granicą twierdzeń. Skrypt samodzielnie czyta oryginalną tabelę, wymaga jej niezmienionego Git blob SHA oraz sprawdza odtwarzalność liczbową; posiada test syntetycznego przypadku ze stałym `g_ρ=g_s`. Test lokalny syntetyczny (`--selftest`) oraz kontrola składni: **PASS**. Obliczenia na **rzeczywistym pełnym pliku źródłowym** wykonano niezależnym integratorem JavaScript, do którego tabela została pobrana przez konektor GitHub; lokalny Python ze źródłowym plikiem 1000 wierszy **nie został wykonany**, gdyż pliku nie dało się pobrać do środowiska wykonawczego z sieci. To jawnie ogranicza poziom walidacji odtwarzalności.

**Werdykt:** `THERMODYNAMIC_BACKGROUND_SENSITIVITY_QUANTIFIED / WEAK_ONLY_GRID_PASS / ENTROPY_CONDITIONAL / SOURCE_MATCHED_JULIA_NOT_RUN / NO_EXEC / NO_CANON`.

**Następny falsyfikator (gotowy do przekazania):** porównać `C_source` i `C_ad` w pełnym solverze Julia najpierw dla β=0, następnie w jednym *source-matched* skanie β przy równoczesnej kontroli `n_B a³`, z oddzielnym opisem sektorów i transportu neutrin. Każde twierdzenie o obfitości fizycznej wymaga zewnętrznie zweryfikowanego modelu BBN/definicji Yp i zgody Moderatora na zmianę statusu.
