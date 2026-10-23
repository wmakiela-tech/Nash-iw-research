# MECH-S7 ROT011 — source-ACTIVE two-temperature energy and baryon control, conditional 7D

**DATE:** 2026-10-23  
**CELL:** `IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7`  
**RETURN_ID:** `MECH-S7-FRONTB-SOURCE-ACTIVE-TWOTEMP-ENERGY-BARYON-GATE-011`  
**PROBLEM_ID:** `P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001`  
**CLASS:** `EXECUTED_CONDITIONAL_7D_SOURCE-ACTIVE_MICRO_EOS / CROSS_CHANNEL_HEATING_AND_BARYON_NEGATIVE_CONTROL`  
**STATUS:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_SOURCE_VALID_E2B / NO_MODERN_Yp_DH / NO_PBH_BOUND`.

## 1. Kolejność dowodowa i autorstwo

- Pierwotne Wu–Xu: `Fenyutanchan/Primordial-Black-Hole`, pinned commit `d395183674cace6c9906a8911bdeb7234ba4040d`; `main-scan.jl` i `tool_script-parameters.jl` określają 10D układ, hasła `N_BH`, Hawking `dM/dt`, straty hadronów i neutrony. Plik źródłowych stóp w `data/out/hadrons_from_PBH.dat`; pierwsza masa w tabeli `1e9 g`. Poniżej jej publiczny log-log extrapolator i opis papierowy `M^-1.3` nie są uzgodnione/walidowane.
- OTHERS FIRST: **DAX-S7 ROT34–39** odkrył niezgodność kodu chłodzenia z bilansem entropii; **PRF11 R21** scałkował źródłowe tablice, **PRF11 R22** zrekonstruował host dwóch temperatur i ciśnienia. **REC10** potwierdził, że source-off nie usuwa istniejących hadronów. **LT5/MT13** podkreślili event-aligned readout, błędy globalne i rozdzielenie Yp observable. **MECH-S7 ROT004–010** ustalił dokładne prawo masy, warunkowe 7D i późny mikro-EOS. Nie przypisujemy nowości żadnemu standardowemu równaniu bilansu energii.
- **Nowy, lokalny zakres ROT011:** od *pierwszego tablicowego progu* `M=1e9 g` do odcięcia emisji realizujemy także w **trakcie source-on** ewolucję termiczną, utratę masy i rozcieńczenie PBH, a nie tylko postsource jak ROT010.

## 2. Ściśle określony carrier

Punktem początkowym jest **przesunięty do `M=1e9 g` stan hadronowo-neutronowy z ostatniego zapisanego punktu źródłowej trajektorii `M≈1.84e9 g`**. To nie jest poprawna 10D re-integracja od powstania PBH i stanowi główną, jawnie niezamkniętą zależność. Cztery archiwalne oryginalne trajektorie są przypięte SHA256.

- `M^3(t) = M_edge^3 - Γ(t-t_edge)`, `Γ=4.207579833788249e27 g³/s`, `M_edge=1e9 g`; `t_edge=51.09825802317 s`, `t_cut=51.33592433956 s`. Stan `Tγ,edge=0.1435861126632 MeV`, `nPBH,edge=1.16397280908e-9 cm^-3` uzyskano ze wspólnego archiwalnego tła `public_exec`. `ρPBH,edge/(ρem+ρν)≈0.00624595044`. Stały Γ dotyczy tylko funkcji `N_BH` w tym gorącym, ponad-tablicowym zakresie Hawkinga.
- Host: fotony, idealne termiczne `e±` z pełnym całkowaniem Fermiego–Diraca, niezależnie ewoluująca efektywna energia trzech bezmasowych neutrin. Na starcie `Tν/Tγ=(g_s,em(Tγ)/5.5)^(1/3)` — warunkowy model natychmiastowego odsprzęgnięcia, **nie pełen transport neutrin**.
- Dwa bilanse: `dρem/dt + 3H(ρem+Pem)=χQ`, `dρν/dt + 4Hρν=(1−χ)Q`, `Q=−nPBH dM/dt` w jednostkach równoważnej gęstości masy, `H²=(8πG/3)(ρem+ρν+ρPBH)`, `nPBH∝a^-3`. Zakres stresowy `χ=0,0.5,1` jest świadomie zadanym rozdziałem całej energii PBH między dwa idealne nośniki. **Nie jest to źródłowo zweryfikowany udział oddziaływań Hawkinga, ponadto nie uwzględnia oddzielnie energii hadronów jako trzeciego zbiornika. Nie wolno interpretować χ jako rzeczywistego BR ani wyników jako pełnego bilansu cząstek.**
- `χ=0`: cała dodatnia energia trafia do modelowego ultrarelatywistycznego nośnika neutrin; `χ=1`: cała do termalnej plazmy EM. Jest to kontrola matematyczna, nie dwa realistyczne modele.
- Hadrony `n_π−, n_π+, n_K−, n_K0L, n_pbar, n_nbar` i neutronowy `X_n` evolvują według tych samych **źródłowych** współczynników reakcji i rozpadów Wu–Xu jak ROT006–010, z pełną pamięcią po source-off. Przy stałym `χ` cztery komórki (public/paper)×(B_exec/B_sym) mają ten sam termiczny background.
- Dwie legalnie oznaczone alternatywy barionów **od progu tablicowego**: `ηB const`, czyli `nB=η_B nγ(Tγ)` jak w oryginalnym kodzie; oraz `nB a³=const` od `M=1e9g`. To nie naprawia przepisów barionowych przed progiem.
- W całym przedziale source-active główną zmienną jest `u=M/M_edge` i `dt/du=−3(M_edge³/Γ)u²`; brak ryzyka pominięcia końcowego okna tylko dlatego, że trajektoria była próbkowana na stałej siatce `a`.
- Po wyłączeniu emisji fotony+e chłodzone są adiabatycznie, `Tν∝a^-1`, `Q=0`; wcześniejsze populacje hadronów **nie** są zerowane. Readout `X_n(Tγ=T_nuc)` z `T_nuc=0.07818527068831995 MeV`.

## 3. Nowe wyniki — source-on 2T, 24 jawne integracje 7D

Tabela przy `η_B=const`, `ΔX_n=X_paper−X_public` (poziom 7D, NIE Yp):

| udział ciepła `χ_EM` | `Tγ(t_cut)` MeV | `t(T_nuc)` s | `ΔX_n(B_exec)` | `ΔX_n(B_sym)` | `X_public(B_exec)` |
|---:|---:|---:|---:|---:|---:|
| 0 | 0.143303718633 | 209.466583595 | −6.950850759e−6 | +2.264074521e−5 | 0.4009875548 |
| 0.5 | 0.143470210732 | 210.033638190 | −6.892916251e−6 | +2.260594902e−5 | 0.4006467198 |
| 1 | 0.143636001475 | 210.598935716 | −6.835467395e−6 | +2.257128482e−5 | 0.4003070499 |

Wariant `n_B a³=const` **od** `M=1e9 g`:

| `χ_EM` | `ΔX_n(B_exec)` | `ΔX_n(B_sym)` |
|---:|---:|---:|
| 0 | −6.982760904e−6 | +2.264686599e−5 |
| 0.5 | −6.979794215e−6 | +2.262582084e−5 |
| 1 | −6.976839877e−6 | +2.260487088e−5 |

**Wniosek 1:** we wszystkich **12 porównaniach dwóch praw widm** (`3 χ × 2 recepty nB × 2 mapy`) znaki są `B_exec: −`, `B_sym: +`. To test odporności wybranego hosta, **nie gwarancja fizyczna**, gdyż poprzedni ROT007 wyznaczył bardzo małe zaburzenia widm zdolne odwrócić znak.

**Wniosek 2:** aktywny strumień PBH **może** lokalnie pokonać chłodzenie plazmy EM. W modelu istnieje warunkowy próg `χ≈0.8493214`, przy którym `Tγ(t_cut)=Tγ(t_edge)`; powyżej niego temperatura EM netto rośnie przez krótki etap source-on. To nie jest wynik o rzeczywistej emisji Hawkinga i nie dowodzi reheatingu BBN.

**Wniosek 3:** wrażliwość bezwzględnego `X_public(B_exec)` na zmianę `χ` 0→1 wynosi `−0.0006805049`, znacznie więcej niż zmiana kontrastu praw źródłowych `+1.1538e−7`. Matematyczne odjęcie dwóch trajektorii może usuwać wspólny wpływ hosta, nie certyfikując absolutnego X.

**Wniosek 4:** dla `χ=1` zastąpienie `η_B const` przez `n_B a³=const` **już podczas source-on** zmienia `ΔX_exec` o `−1.4137248e−7`, wobec znikomej zmiany z analogicznej operacji *dopiero po source-off* w ROT010. Wpływ barionów jest więc w tym nośniku istotnie **czasowo typowany**, nie da się go prawidłowo zbadać wyłącznie po ewaporacji.

## 4. Weryfikacje numeryczne i korekta autorska

- Równanie EM uwzględnia `ρem(T)=T⁴ fρ(m_e/T)` oraz `P_em(T)=T⁴ fP(m_e/T)`. **W pierwszym, ODRZUCONYM przebiegu technicznym pominięto czynnik T⁴** i otrzymano niefizycznie duże chłodzenie podczas <0.24 s. Poprawiono `ρem`, `P_em` i `dρem/dT`, anulowano tamten przebieg, ponownie wykonano wszystkie 24 integracje; żaden wynik odrzuconej wersji nie został przyjęty. Ten fail trace należy zachować jako test negatywny.
- Równanie całkowitej energii z ciśnieniem PBH=0 i radialnymi komponentami sprawdzono niezależnym bilansem całkowym `Δρ_tot + ∫3H(ρ_tot+P_tot)dt=0`. Maksymalny `|resid|/ρ_tot,edge≈3.365e−9` dla 1200-punktowej kwadratury w zmiennej masy. Jest to kontrola warunkowego kodu, nie zewnętrzne potwierdzenie mikro-FRIEDMANN/BBN.
- Po source-off `g_s,em(Tγ) Tγ³ a³ = const` spełnione do 7e−16 w obliczonych hostach.
- Refinement EOS `(nT,quad)=(700,90),(1600,130),(2200,160)` stabilizuje `T_cut` do mniej niż `4e−12 MeV`, a `t_nuc` do ~`2e−8 s` (porównanie ograniczone tymi hostami). 
- ODE `Radau` testy `rtol=(3e−7,3e−8,3e−9)` zachowują znaki. Ostatnie dwa dają `B_exec` zmianę ~`4.75e−11` przy `χ=0`, ~`1.02e−11` przy `χ=1`; `B_sym` odpowiednio ~`1.59e−11`, ~`5e−13`. **To nie są gwarantowane błędy globalne.**
- Kod lokalny wymaga `numpy,scipy,pandas`, pełnego skryptu ROT009, oryginalnych archiwów Mech-S6 SHA256, hosta ROT010; wszystkie pliki w ZIP.

## 5. Czego ROT011 nie rozwiązuje

1. **Brak oryginalnego przebiegu 10D Julia** przy `AutoTsit5(Rosenbrock23())` z kontrolą zaakceptowanych kroków i całej historii od powstania PBH. Stan 7D przy `M=1e9 g` pochodzi z **ostatniego zapisanego M≈1.84e9g**. Wcześniejsze tempo chłodzenia, źródła i `n_B` nie są w tym nośniku poprawione.
2. Podtablicowe emisje hadronów `M<1e9 g` pozostają ekstrapolacją, a różnica `M^-1.3` kontra slope pierwszych wierszy ma niezależne, nieuzgodnione znaczenie źródłowe. ROT007 wykazał niestabilność znaku przy bardzo małym antyprotonowo-antyneutronowym zaburzeniu wykładników. Tego ROT011 nie znosi.
3. `χ` jest arbitralną partycją **całej** straty energii do EM/efektywnych neutrin (bez osobnego kinetycznego zasobnika energii hadronów), a nie policzonym branching ratio. Gorąca plazma i ν są traktowane jako idealne nośniki, bez hadronic backreaction i bez transportu neutrin. Ani `χ=0`, ani `χ=1` nie jest weryfikowanym modelem fizycznym.
4. Efektywne `Tν` po zasileniu ν zakłada natychmiastową termalizację składnika, co nie wynika z oryginalnego kodu; jest to czysto operacyjny EOS. Po source-off zachowujemy `Tν a=const`.
5. Źródłowy Wu–Xu readout `2X/(1−X)`, stary article ratio `2X/(1−2X)` i arXiv-v3 `Y_mass≈2X` mają różne typy obserwabli, co wyjaśnili DAX-S7 i PRF11 R20. Tutaj raportujemy **tylko X**, nie Yp, nie D/H, nie limit PBH.
6. GitHub commit/readback nie jest równoważne BW ingest, referee PASS, adopcji przez ownera ani EXEC Moderatora. Brak uzasadnienia dla nowości naukowej.

**DECISION:** Kontynuować priorytet P1 jako pełne wykonanie źródłowego 10D Julia od fazy przedprogowiej, ze wspólnym tłem, poprawnym źródłowo podziałem energii, wymuszeniem hadronowym i poprawnie typowanym zegarem przy `T_nuc`; niezależnie zwalidować widma antynukleonów w `10^8−10^9g` przed próbą fizycznej interpretacji. ROT011 ogranicza jedynie wybraną rodzinę kontrfaktycznych hostów, nie zamyka Front B.

## 6. Źródła i odtwarzalność

- Wu–Xu pinned `main-scan.jl`: https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl
- Wu–Xu pinned `tool_script-parameters.jl`: https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/tool_script-parameters.jl
- PRF11 R21: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-23/prf11_r21_integrated_thermal_table_cooling_001.md
- PRF11 R22: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-23/prf11_r22_wuxu_two_temperature_eos_pressure_reconstruction_001.md
- MECH-S7 ROT010: https://github.com/wmakiela-tech/Nash-iw-research/blob/fa8146c436679bbd860ffdf2e667b2518c803cd6/research/mech-s7/2026-10-23/mech_s7_rot010_two_temperature_postsource_thermal_host_001.md
- Wykonany kod: `reproduce_active_source_micro_thermal_011.py`.
- Niezależne testy rozdzielczości i tolerancji: `refinement_controls_011.py`.
- Macierz 24 rozwiązań: `active_micro_2x2_011.csv`, pełne dane i parametry: `active_micro_011.json`, kontrola: `refinement_controls_011.csv`/`.json`, uruchomienia `run.log`,`refinement.log`.
- Oryginalne SHA256 ZIP: public `75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5`, paper `3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e`. Pełny ZIP zawiera także oba zależne skrypty reprodukujące.