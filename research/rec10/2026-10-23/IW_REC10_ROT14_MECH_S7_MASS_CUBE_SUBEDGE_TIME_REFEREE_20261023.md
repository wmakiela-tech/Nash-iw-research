# IW/NASH — REC10 ROT14
## Niezależna kontrola prawa sześcianu masy PBH i okna końcowego Wu–Xu

**Data:** 2026-10-23  
**Komórka:** `IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10`  
**Werdykt:** `PASS_WITH_QUANTITATIVE_STRENGTHENING / SOURCE_TYPED`  
**Status:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_PBH_BOUND / NO_NEW_TASK`.

## Źródła i granice odtworzenia

Odczytano pełny raport źródłowy `research/mech-s7/2026-10-23/mech_s7_frontb_exact_mass_cube_and_subedge_fluence_gate_004.md`, blob `e20a2e2d527863e08992e1879275d1b0d50f85db`, oraz przypięte publiczne pliki źródłowe `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`:

- `arXiv-2509.05618/main-scan.jl`, blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`;
- `arXiv-2509.05618/tool_script-parameters.jl`, blob `0d7198ff3557bdbd5753000bb07a7a7405cc24f5`;
- `arXiv-2509.05618/tool_script-N_relativistic_species.jl`, blob `0437c032bdc4bafca6cb634c0db4cd2c46fb7efc`.

Wykonano samodzielne przeliczenie analityczne z **opublikowanych przez Mech-S7 liczb** i skontrolowano semantykę kodu Julia. **Nie** pobrano ponownie oryginalnych ZIP z trajektoriami, nie wykonywano historycznego solvera 10D Julii ani nie sprawdzano niezależnie ich sum kontrolnych; zweryfikowano tylko arytmetykę jego raportu i zgodność z pinowanym kodem.

## 1. Źródłowo legalna tożsamość

W oryginalnym `main-scan.jl` przed odcięciem parowania:

`d_m_PBH_dt = -N_PBH * NU.m_Pl^4 / m_PBH^2`, a `d_log_m_PBH_dη = d_m_PBH_dt/(H*m_PBH)` wraz z `d_log_t_dη = 1/(H*t)`.

Podstawienie reguły łańcuchowej dowodzi niezależnie od parametryzacji przez `η=log(a)`:

`dM/dt=-C/M²`, a więc `M³(t)+3C(t-t_i)=M_i³`.

Źródłowe `tool_script-parameters.jl` definiuje `N_BH=(27/4) N_rho/(30720π)`. Tablice `N_rho` przy wysokiej temperaturze korzystają z `ExtrapolationType.Constant`, a zadeklarowane temperatury PBH w badanym przedziale mas przekraczają górny punkt tablic. Stąd w tej **konkretnej** wersji modelu stałe `N_BH` i `Γ=3C` są spójne z kodem, przed odcięciem i przy zachowaniu jednostek naturalnych.

Wartość źródłowa `Γ = 4.207579833788249×10^27 g³/s`. W tym raporcie jej liczbową wartość potraktowano jako wynik Mech-S7 po konwersji stałych SI; odtworzono niezależnie dalsze przekształcenia w gramach i sekundach.

## 2. Niezależny przelicznik zamrożonych punktów

Przy `M_i=6×10^9 g`, zaniedbywalnym wobec sekund `t_i`, `M_ex(t)=(M_i³−Γ t)^(1/3)`.

| Mapa | t ostatniego aktywnego zapisu [s] | M zapisane [10⁹ g] | M wynikające z tożsamości [10⁹ g] | Rozbieżność | Przesunięcie czasu [s] |
|---|---:|---:|---:|---:|---:|
| B_exec | 49.961898627 | 1.836633086 | 1.794771130 | +2.33243981% | +0.0984049269 |
| B_sym | 49.959279260 | 1.835347300 | 1.795910890 | +2.19590015% | +0.0926952764 |

Definicja `Δt_equiv=[M_saved³−M_exact(t_saved)³]/Γ` jest **dokładną miarą reszty sześciennej**, nie rzeczywistym zdarzeniem przesunięcia czasu ani korektą rozwiązanego stanu. Zgodność z liczbami Mech-S7: `PASS`.

## 3. Wzmocnienie: znaczenie reszty czasu względem całego podprogowego okna

Dla `M_edge=10^9 g` i nominalnego `M_cut=12.3669217346 g`, źródłowe prawo daje:

- `t_edge=51.09825802317032 s`;
- `t_cut=51.33592433955715 s`;
- `W=t_cut−t_edge=0.23766631638683577 s`.

**Nowy dokładny bezwymiarowy wskaźnik diagnostyczny** `χ=Δt_equiv/W` przy ostatnich aktywnych zapisach:

- `χ_exec=0.4140466` (**41.40%** okna);
- `χ_sym=0.3900228` (**39.00%** okna).

To porównuje wielkość istniejącej reszty równania masy z długością całej podprogowej fazy. **Nie jest ekstrapolacją błędu czasowego do tego okna**: nie dowiedziono, że `Δt_equiv` utrzymuje się, rośnie albo maleje po ostatnim zapisanym punkcie. Nie należy utożsamiać tego wskaźnika z błędem `X_n`, `Y_p`, całki hadronowej ani prawdopodobieństwa wykluczenia PBH.

## 4. Ograniczona kontrola zintegrowanej emisji

Dla zadeklarowanych lokalnych ekstrapolacji `Q_public∝M^{s_h}`, `Q_paper∝M^{-1.3}` i masowego `dt/dM=−M²/C`, przy wspólnej normalizacji źródła na `M_edge`, dokładny stosunek liczby wyemitowanych cząstek od `M_edge` do `M_cut` wynosi:

`R_h=((3+s_h)/1.7)*(1-u_cut^1.7)/(1-u_cut^(3+s_h))`, `u_cut=M_cut/M_edge`.

Po użyciu **zaokrąglonych** wykładników gatunkowych z raportu Mech-S7 otrzymano:

- pion: `+5.8537647%` (źródło `+5.853787%`);
- kaon naładowany: `+6.0793529%` (źródło `+6.079332%`);
- K0L: `+6.0702941%` (źródło `+6.070303%`);
- proton / antyproton: `+5.6299412%` (źródło `+5.629916%`);
- neutron / antyneutron: `+5.6021765%` (źródło `+5.602173%`).

Rozbieżności poniżej `0.000026` punktu procentowego są zgodne z utratą cyfr źródłowych wykładników podczas ich prezentacji; nie obalają raportowanych dokładniejszych stosunków. **Liczba wyemitowanych cząstek nie jest odpowiedzią `X_n`**: potrzebne są straty hadronowe, transfer między kanałami, reakcje i ich konwolucja po czasie.

## 5. Ocena przypisania błędu

`PASS`: wyprowadzona tożsamość dla masy, konwersja `t_edge`/`t_cut` z przyjętym Γ, wykrycie niespójności masy z czasem w czterech relacjonowanych komórkach, rozróżnienie przyszłej podprogowej emisji od historycznych punktów zapisu.

`CONDITIONAL`: rzeczywisty problem solvera/wartości archiwalnych wymaga odczytu surowych plików i kontroli kodu wykonawczego. Źródłowy błąd równania masy jest poważnym **testem koniecznym** poprawności numerycznej, nie ilościowym dolnym ograniczeniem błędu innej zmiennej.

`HOLD`: nie wyprowadzono certyfikowanego błędu globalnego w terminalnym `X_n(T_nuc)`; nie odtworzono oryginalnego `Y_p/D/H`, produkcyjnego `2×2`, genealogii publikacyjnej ani fizycznego PBH-bound. Końcowa regularizacja odcięcia i źródłowo legalna hadronizacja dla `M<10⁹ g` pozostają odrębnymi warunkami.

Mature host: integracja równania `dM/dt=-C/M²`, reszta zachowanej funkcji, kontrola błędów numerycznych i analiza skali; `NO_NOVELTY`. Odpowiedzialność naukowa za źródło pozostaje po stronie Mech-S7, autorytet EXEC po stronie Moderatora. Bez nowych zadań i automatycznego awansu do BW.

**Custody na chwilę utworzenia pliku:** lokalny artefakt rozmowy, readback PASS; GitHub i Slack wymagają osobnego sprawdzenia przed deklaracją sukcesu.