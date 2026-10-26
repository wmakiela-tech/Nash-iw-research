# IW/NASH — DAX-S7 — obrót 59 — audyt kontraktu papier ↔ kod: rozdzielenie neutrin, entropia i chłodzenie

**Data:** 2026-10-26  
**Status:** `PAPER_CODE_ENTROPY_CONTRACT_MISMATCH / LOW_T_NEUTRINO_CONTENT_CONFIRMED / SOURCE_GRID_QUADRATURE_PASS / FULL_JULIA_NOT_RUN / NO_EXEC / NO_CANON`  
**Komórka:** DAX-S7, niezależna walidacja ograniczeń wnioskowania naukowego. Bez ustanawiania kanonu, bez interpretacji granic PBH.

## 1. Rozstrzygnięcie otwartego pytania z obrotu 58

**Nowe źródło rozstrzygające:** najnowszy tekst publikacji Wu–Xu, *Primordial black holes evaporating before Big Bang nucleosynthesis*, `arXiv:2509.05618v3`, rozdział 2.1, **równanie (2.7)**, jawnie przyjmuje

`g_{*s}(T_gamma) * a^3 * T_gamma^3 = const.`

Dodatek A, **(A.1)–(A.3)**, oddziela sektory elektromagnetyczny i neutrinowy, zakłada `T_nu a=const` po odsprzęgnięciu oraz wyznacza `T_gamma(a)` na podstawie zachowania *całkowitej* entropii współporuszającej. Tablica używana przez kod jest zgodna z obecnością neutrin chłodniejszych od fotonów. Tym samym hipoteza, że nieznana konwencja `g_*` wyjaśnia różnicę między `C_source` i `C_ad`, jest w omawianym wariancie β=0 **sfalsyfikowana jako wyjaśnienie wewnątrz danego opracowania**: warunek adiabatyczny nie jest zewnętrzną dowolną konwencją, lecz jawnym równaniem autorów.

Źródła pierwotne:

1. Tekst v3: https://arxiv.org/html/2509.05618v3 — (2.7), (A.1)–(A.3) i (5.1).
2. Julia: https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/main-scan.jl — `d_log_ρ_SM_dη` (okolice linii 85), `Yₚ` (okolice linii 206–211).
3. Definicja interpolatorów `Nᵨ` i `Nₛ`: https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/tool_script-N_relativistic_species.jl.
4. Dane: https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/data/ext/N_around_m_e.csv (1000 wierszy).

Sprawdzone Git blob SHA odpowiednio: `main-scan.jl`: `b368ba55d5a493f7bc185909730f7fe5691f10d6`; `tool_script-N_relativistic_species.jl`: `0437c032bdc4bafca6cb634c0db4cd2c46fb7efc`; `N_around_m_e.csv`: `93f2494f026c5d0587ea40fe08bb938dd9d01fa8`.

## 2. Test składu tablicy: neutrina są obecne

Dla najniższego wiersza `T=0.01400298972685787 MeV` tablica ma

`g_rho=3.3654513231275924`, `g_s=3.9120400850273933`.

Oczekiwany po anihilacji elektronów sektor elektromagnetyczny ma około 2 stopnie swobody. Pozostałe wkłady są zgodne z trzema smakami bezmasowych neutrin (`(7/8)*6=5.25`) przy ich innej temperaturze. Niezależne odtworzenie stosunku temperatur z energii i entropii daje:

`( (g_rho-2)/5.25 )^(1/4) = 0.7141332097688913`,

`( (g_s-2)/5.25 )^(1/3) = 0.7141332097688571`.

Wzajemna zgodność ~`3.4e-14`. Przybliżenie natychmiastowego odsprzęgnięcia daje `(4/11)^(1/3)=0.7137658555036082`. **To bezpośredni falsyfikator alternatywy „tablice pomijają neutrina”** w rozważanej części zakresu. Jego interpretacja jako pełnego `N_eff` wymaga bardziej złożonego transportu neutrin; wyliczenie `N_eff_like=3.00618` jest jedynie pomocniczą parametryzacją niskotemperaturowych wkładów.

## 3. Dokładna rozbieżność równania chłodzenia

Oznaczmy `r=dln(g_rho)/dln(T_gamma)` oraz `s=dln(g_s)/dln(T_gamma)`. W publicznym `main-scan.jl`, bez PBH (`β=0`), kod narzuca:

`C_source = dlnρ_SM/dln a = -4 + r/(3+s)`.

Natomiast z jawnego w papierze warunku (2.7), przy tej samej tablicy i `ρ_SM=(π²/30) g_rho T_gamma^4`, wynika:

`C_paper = -3(4+r)/(3+s)`.

Stąd tożsamości algebraiczne:

`C_source - C_paper = 4(r-s)/(3+s)`,

`(dln S_com/dln a)_source = 4(r-s)/(4+r)`,

`S_com = (2π²/45) g_s T_gamma³ a³`.

Różnica znika przy stałych stopniach swobody lub `r=s`, ale występuje przy anihilacji `e⁺e⁻`. Przy `T_nuc` źródłowe tablice dają `r=0.44011773575892355`, `s=0.3590581309288281`, `C_source-C_paper=0.09652658771663658` i `dln S_com/dln a=0.07302473461662871`. Nie jest to artefakt źle dobranej definicji `g_s`: równanie (2.7) autorów jednoznacznie podaje odpowiedni niezmiennik dla β=0.

## 4. Ilościowe rozstrzygnięcie: od 10 MeV w dół

Otrzymano przez całkowanie oryginalnej tablicy 1000 punktów (od `~0.014` do `10 MeV`), w przedziałach logarytmicznych jej natywnych węzłów. Normalizacja: `a(10 MeV)=1`, `T_nu(10 MeV)=T_gamma(10 MeV)`. Źródłowe `C_source` całkowano metodą Simpsona z 1–64 podkrokami na przedział tablicowy; `C_paper` kontrolowano zarówno numerycznie, jak i dokładną postacią `ln(a/a10)=ln(10/T)+(1/3)ln[g_s(10)/g_s(T)]`.

| T [MeV] | `S_com(T)/S_com(10MeV)` — kod | `Tν/Tγ` z `a_source` + (A.3) | `Tν/Tγ` z papieru (A.1)/(2.7) |
|---:|---:|---:|---:|
| 1.0 | 1.000210032 | 0.994051886 | 0.994121476 |
| 0.5 | 1.002594782 | 0.976400920 | 0.977244707 |
| 0.2 | 1.033425440 | 0.879154040 | 0.888842255 |
| 0.1 | 1.117062776 | 0.735711403 | 0.763366939 |
| **0.0781852706883** | **1.146781633** | **0.700776834** | **0.733511025** |
| 0.0140029897269 | 1.170117673 | 0.677540286 | 0.713967269 |

Wniosek w punkcie BBN: kod przy β=0 narusza papierowy warunek entropii o **+14.67816334%** pomiędzy 10 MeV a `T_nuc`. W połączeniu z podanym w (A.3) `T_nu a=const` daje **~4.46267% niższy** stosunek `T_nu/T_gamma` niż papierowa (A.1). Na najniższej temperaturze tablicy różnica wynosi ~5.102%, podczas gdy sama tablica jawnie koduje neutrina z `T_nu/T_gamma≈0.714133`.

**Granica twierdzenia:** wartości `Tν/Tγ z a_source` są testem *konsekwencji jednoczesnego wymagania* źródłowego równania chłodzenia i papierowej (A.3); Julia `main-scan.jl` nie integruje oddzielnego równania `Tν(t)` w rozważanym podukładzie. Nie opisujemy tych wartości jako „rzeczywistych prognoz kodu dla neutrin”.

### Zbieżność

Dla `T_nuc`, przy 1, 2, 4, 8, 16, 32 i 64 podkrokach na źródłową komórkę, `ln(a_nuc/a_10)` pozostaje w zakresie `[5.206824893535384, 5.206824893536117]`, czyli stabilność ~`7.4e-13`. Niepewność kwadratury jest zdecydowanie mniejsza od ustalonej niespójności algebraicznej. Równoważny `S_com(Tnuc)/S_com(10 MeV)=1.1467816334078` jest stabilny do ~`3e-12`.

## 5. Ważna niezależna kontrola: wzór na hel i poziom ufności

Odnaleziono kolejną jawną niezgodność **między aktualnym tekstem arXiv v3 a publicznym kodem**:

- Papier, **równanie (5.1)**: `Y_P ≈ 2 X_n(T_nuc)`.
- `main-scan.jl` w bloku `Yₚ`: `2 * Xₙ_nuc / (1 - Xₙ_nuc)`.
- Papier, opis rysunku 5 i sekcja 5: granica **2σ** dla `Y_P=0.245±0.003`, tzn. `Y_P>0.251`. W części wcześniejszych raportów DAX posługiwano się kontrolą 3σ. **Nie wolno mieszać wyników przy 2σ z wcześniejszymi przedziałami przy 3σ.**

To jest dodatkowe potwierdzenie znanego z obrotów 29–33 i 53 problemu źródło–obserwabla, a nie nowa prognoza fizyczna. Nie zweryfikowano, czy kod z obecnej gałęzi jest dokładnie wersją użytą do ostatecznej figury w publikacji, ani czy osobna sieć BBN kompensowała tę różnicę. Nie deklarujemy korekty granic PBH.

## 6. Negatywna wiedza, granice i następny falsyfikator

Potwierdzona **wewnętrzna niespójność kontraktu** dotyczy przypadku **β=0**, przy ustalonych tablicach i założeniach z tekstu: nie wymaga modelowania wtrysku energii PBH. Nie dowodzi jednak, że dowolna dwusektorowa ewolucja z wtryskiem PBH musi spełniać `S_com=const`. Po rozdzieleniu neutrin na dwa sektory i uruchomieniu źródła energia/emisja PBH musi być jawnie dzielona na oba sektory, a odpowiednia entropia może wzrastać.

**Priorytet audytu:** w pełnym, oryginalnym Julia uruchomić β=0 i rejestrować `g_s(T_gamma)T_gamma³a³`, `T_gamma(t)` oraz `X_n(Tnuc)`, porównać dokładnie z opublikowanym (2.7) i danymi niezależnej kwadratury. Następnie, *dopiero po* zweryfikowaniu zgodności przy β=0, wyodrębnić sektor elektromagnetyczny i neutrinowy dla β>0 (oddzielne bilanse wtrysku) i przetestować poprawki w obserwablu z artykułu. Szczególnie sprawdzić rolę `η_B(T)` i zależność gęstości celów od zachowania liczby barionów.

**Wykonanie:** źródłową tabelę 1000 wierszy pobrano przez konektor GitHub i policzono niezależną kwadraturą JavaScript; zapisano CSV pełnych punktów diagnostycznych, CSV zbieżności i manifest JSON. Lokalny reproducer Python ma zabezpieczenie dokładnego Git blob SHA wejścia i przeszedł `--selftest` z syntetycznym stałym `g`. W tej sesji wejściowej tabeli nie udało się pobrać do kontenera z powodu ograniczenia dostępu sieciowego, więc **lokalny Python z kompletnymi 1000 źródłowymi wierszami nie został wykonany**. Wyniki numeryczne pochodzą z obliczeń na pełnej tabeli w wywołaniach konektora.

**Werdykt:** `SOURCE_PAPER_EQUATION_CONTRACT_MISMATCH / NEUTRINO_CONTENT_IN_SOURCE_TABLE_CONFIRMED / β0_ENTROPY_FALSIFIER_PASS / FULL_JULIA_PENDING / NO_PBH_CONSTRAINT / NO_EXEC / NO_CANON`.
