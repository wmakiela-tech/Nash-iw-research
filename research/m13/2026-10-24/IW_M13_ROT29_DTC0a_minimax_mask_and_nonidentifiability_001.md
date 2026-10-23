# IW / M13 — ROT29: optymalna stabilność korekty maskowanego RMS i niskopasmowy kontrprzykład identyfikowalności

**RETURN_ID:** `M13-ROT29-DTC0A-MASKED-NORM-MINIMAX-AND-FIVE-MASK-NONIDENTIFIABILITY-001_20261024`  
**LINEAGE:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**DATE:** 2026-10-24  
**PROBLEM_ID:** `P3_DTC0A_TT_MASK_COMMUTATION_AND_LOCAL_RMS_TYPING_001`  
**CLASS:** ostra elementarna geometria liniowej ekstrapolacji momentów, źródłowa ocena dziewięciu przypadków N41 i konstruktywny nonmap dla pięciu maskowanych RMS; **nie** historyczna alternatywna trajektoria K.  
**CLAIM CEILING:** `EXACT_FINITE_ALGEBRA / FROZEN_45_VALUE_CSV_POSTPROCESS / HELPER_NATIVE_SYNTHETIC_TENSOR_CONTROL / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / TPE HOLD`.

## 0. Currentness i rzeczywista różnica wobec ROT28

ROT18/27: maska ze stałym indeksem k przesuwa fizyczną dziedzinę i generuje błąd RMS rzędu N^-1. ROT23–26: zachowany generator `deepseek_python_20260627_a87249.py` funkcjonalnie odtworzył 99 zamrożonych norm; w tej rodzinie istnieje niezerowa dokładna granica KA, mimo KC/KB ->0. ROT28 **już** podał dwumaskową ekstrapolację k=2,3, przeliczył wszystkie k=2..6 przy N41 i wymienił kombinację k=2,4,6 o normie wag L1=7; nie zgłasza się tych faktów jako nowych. Aktualne równoległe wyniki INT8, XH-S4, PRF11 i Geeky-S11 dotyczą symboli pochodnej, niezamknięcia TT Liego, częstotliwości i właściwej domeny; nie są zastępowane obecnym raportem.

**Nowy wkład ROT29:** (i) ścisły certyfikat **optymalności minimaksowej** wagi L1=7 w klasie wszystkich liniowych korekt k2..6 kasujących dwa rzędy geometrii; (ii) pełna ewaluacja dokładność–odporność na 9 historycznych przypadkach; (iii) jawne konstruktywne twierdzenie: **pięć maskowanych norm nie identyfikuje nawet globalnego RMS dwóch dodatnich gładkich niskopasmowych gęstości energii**. To istotnie ogranicza interpretację estymatorów ROT28.

## 1. Warunki aproksymacji i ostry dualny limit szumu

Dla jednego niezmienionego tensora w N41 (lub w jednorodnie regularnej rodzinie N) oznaczmy `g_k=R_k^2`, przy `R_k=rms_norm(T_N,k)`. Z rachunku sum brzegowych na okresowej siatce przy stałym k i kontrolowanych pochodnych:

`g_k(N)=g_0(N)+a_N k/N+(b_N k+c_N k²)/N²+O(N^-3)`.

W konsekwencji liniowa korekta `g_hat_0=Σ_{k=2}^6 w_k g_k` usuwa wszystkie składniki geometrii pierwszego i drugiego rzędu (w tym `b_N k/N²`), jeśli

`Σw_k=1`, `Σk w_k=0`, `Σk² w_k=0`.  (ROT29.1)

Ten kontrakt wymaga tych samych N, α, pól, stencilu, `P_TT` i normy — nie wolno mieszać siatek. Dodatnie kwadraty RMS **nie zapewniają** dodatniości ekstrapolowanego `g_hat_0`; pierwiastek wolno brać tylko gdy wynik ≥0.

Dla nieznanych zaburzeń **kwadratów norm** `|δg_k|≤ε` zachodzi `|δg_hat_0|≤ε Σ|w_k|`. To limit deterministyczny bez założenia niezależności błędów. Najmniejsza możliwa wartość `Σ|w_k|` przy ROT29.1 jest dokładnie **7**.

**Dowód ostrości.** Weź `q(k)=(k−4)²/2−1`. W pięciu punktach k2..6 jego wartości to `(+1, −1/2, −1, −1/2, +1)`, zatem `|q(k)|≤1`. Ponieważ q ma stopień 2, każde rozwiązanie ROT29.1 spełnia `Σw_k q(k)=q(0)=7`. Stąd `7≤Σ|w_k|`. Wagi `w_2=3,w_4=−3,w_6=1`, pozostałe zero, spełniają ROT29.1 i osiągają L1=7. QED. Jest to klasyczny dualny certyfikat zadania liniowego Chebysheva, bez roszczenia nowości.

Dla samej korekty pierwszego rzędu (dwa warunki) analogiczny wielomian `q_1(k)=(4−k)/2` daje ostry dolny limit **2**, osiągany przez `w_2=3/2,w_6=−1/2`; jego większy błąd systematyczny na danych N41 nie narusza tego dowodu odporności.

**Inny model błędu.** Przy **niezależnych, homoskedastycznych** zakłóceniach kwadratów norm minimalizuje się `Σw²`, a nie `Σ|w|`. Rozwiązanie wszystkich pięciu masek to `w=(3,−2/5,−9/5,−6/5,7/5)`, z `L2²=79/5`, `L1=39/5=7.8`. Porównywana waga minimaksowa ma `L2²=19`. Jednak maski są zagnieżdżone i ich błędy pomiarowe mogą być silnie skorelowane: brak wiarygodnej empirycznej macierzy kowariancji, więc niezależne szumy nie są uprawnionym opisem rzeczywistych danych DTC0a.

## 2. Zamrożone dane historyczne, wynikowa granica accuracy–robustness

Źródło: `dtc0a_mask_sensitivity_N41_v0_3_1.csv`, **15 rekordów**, trzy RMS w wierszu, razem **45 liczb**. Porównano je z wartościami maskowymi wcześniejszego pełnego rekonstruktora ROT28 (zgodność względna lepsza niż `3·10^-14`); pełnosieciowe RMS 9 przypadków pochodzi z **wykonanego uprzednio** rzadkiego rachunku Fouriera zapisanego w `IW_M13_ROT28_mask_extrapolation_and_shells_20261023.json`, a nie z nowego historycznego runtime.

| Korekta dla `g=R²` | Rząd geometryczny | Średni błąd absolutny RMS (9 przypadków) | Najgorszy błąd absolutny RMS | Najgorsze L1 w błędach `g_k` |
|:--|:--:|--:|--:|--:|
| `g_3` bez korekty | O(N^-1) | 8.8953% | 18.5080% | 1 |
| `3g_2−2g_3` (ROT28) | O(N^-2) | 1.9969% | 4.9641% | 5 |
| `(3/2)g_2−(1/2)g_6` (minimax rząd 1) | O(N^-2) | 4.5213% | 11.0821% | 2 |
| `3g_2−3g_4+g_6` (**minimax rząd 2**) | O(N^-3) | **1.1242%** | **2.6724%** | **7** |
| `6g_2−8g_3+3g_4` | O(N^-3) | 0.8237% | 1.1393% | 17 |
| `10g_2−20g_3+15g_4−4g_5` | O(N^-4) | 0.8808% | 2.3880% | 49 |
| `15g_2−40g_3+45g_4−24g_5+5g_6` | O(N^-5) | 0.7141% | 1.3257% | 129 |

Powyższe rzędy są asymptotyczne dla pól gładkich o kontrolowanych pochodnych i dla k stałych. Dla N41 wiodący brak może być mniejszy niż składniki wyższego rzędu, dlatego **nie** wolno wybierać najlepszego algorytmu wyłącznie z ostatniej kolumny ani twierdzić, że minimaksowe k246 ma najmniejszy błąd w każdym z dziewięciu wierszy. W danych N41 każda z sześciu korekt tabeli poprawia błąd względem surowego k3 we wszystkich 9/9 przypadkach, ale to świadectwo konkretnej rodziny, nie twierdzenie uniwersalne.

**Przykład deterministycznego stresu.** Dla N41, α=.05, KA niezakłócony błąd k246 to `+0.82868%` RMS. Jeżeli każda z jego trzech potrzebnych wartości **kwadratu normy** może być niezależnie od pozostałych przesunięta w pesymistycznie dobranym kierunku o `0.005*g0`, otrzymujemy dodatni błąd RMS `+2.5496%` (g0 to rzeczywista pełna norma squared służąca wyłącznie do wielkości testowego błędu). Dla k234 ta sama nierównomierna perturbacja może zwiększyć błąd z `+0.4471%` do `+4.5926%`. To syntetyczny, deterministyczny stress test, nie oszacowanie faktycznych błędów CSV.

## 3. Twierdzenie ROT29.2 — pięć masek nie wyznacza globalnej normy nawet dla niskopasmowej energii

Wykażemy silniejszy negatywny wynik niż prosta utrata informacji spoza maski: dwa **wszędzie dodatnie**, analityczne, realne pola gęstości energii mogą mieć pasmo Fouriera `|m_x|≤5, m_y=m_z=0`, identyczne **wszystkie pięć maskowanych norm** i różne pełnosieciowe normy przy N41.

Niech `N=41`, `θ=2π/41`, `c=20` oraz dla indeksu siatki j:

`t_j=cos(θ(j−c))`, `t_k=cos(θ(c−k))`, k=2,3,4,5.

Zdefiniuj wielomian 4. stopnia `H(t)=∏_{k=2}^5(t−t_k)`. Dla `j=6,..,34` mamy `t_j>t_5`, stąd `H(t_j)>0`. Wyznacz dokładnie określoną (algebraiczną) liczbę

`λ=(Σ_{j=6}^{34} H(t_j)t_j)/(Σ_{j=6}^{34}H(t_j))`.

Niech `V_j=H(t_j)(t_j−λ)` i `C=max_{0≤j<41}|V_j|`. Jest to rzeczywisty wielomian 5. stopnia zmiennej `cos(θ(j−20))`, a więc wielomian trygonometryczny o harmonicznych najwyżej 5. Z definicji λ suma V po wewnętrznej masce k6 wynosi zero. Ponadto pary indeksów usuwanych kolejno przy k=2→3, 3→4, 4→5, 5→6 to `(k,40−k)`; oba mają `t_j=t_k`, więc `V_j=0`. Stąd **suma V wynosi zero na każdym z pięciu zagnieżdżonych obszarów k2..6**.

Jednak `Σ_{j=0}^{40}V_j < 0`: poza maską k2 pozostają cztery indeksy `(0,1,39,40)` z `t_j<t_2`, na których `H(t_j)>0`, a `t_j−λ<0`, zatem wszystkie cztery wkłady są ściśle ujemne. To dowód bez przybliżeń zmiennoprzecinkowych.

Weź `F_±(j)=1±(1/2)V_j/C` i rozszerz na całą siatkę 3D przez niezależność od y,z. Oba są dodatnie (`F_±≥1/2`), gładkie i o wspomnianym pasmie Fourier, mają jednakowe średnie **równe 1** na każdej masce k2..6, a różne średnie na całym torusie. Rzeczywiste symetryczne pola tensorowe `T_±,xx=√(6F_±)`, pozostałe składowe zero, mają dokładnie `rms_norm(T_±,k)=1` dla k=2..6, lecz różne `rms_norm(T_±,0)`; same tensory T_± są gładkie, ale nie przypisujemy im nieuzasadnionej skończonej szerokości widmowej (skończenie pasmowa jest ich **gęstość energii**).

**Bezpośredni test retained helper (odd-N=41):** `rms_norm` niezmienionego `deepseek_python_20260627_a87249.py` daje dla pięciu masek pary równe 1 z różnicą ≤`2.23·10^-16`, ale na pełnej siatce `0.999987687579952` wobec `1.000012312268454`, różnica `2.4624688502·10^-5`. Ilustracja zmiennoprzecinkowa potwierdza dokładną konstrukcję analityczną; nie jest historycznym tensorowym K_A ani koniecznym modelem fizycznym.

**Wniosek identyfikowalności:** żaden operator zależny wyłącznie od pięciu maskowanych RMS nie może dokładnie odzyskać pełnej normy dla całej powyższej klasy bez dodatkowego modelu pola. To samo dotyczy ekstrapolacji wszelkiego rzędu. **Nie** przeczy to funkcjonalnej rekonstrukcji pełnych tensorów konkretnych generatorów w ROT23–27: tam używano więcej informacji (pełna struktura źródła i operatorów), nie tylko pięciu norm.

## 4. Provenance, replikacja, ograniczenia

- Zachowany historyczny CSV SHA256: `4dc228e1edab9fefc219118b5ba465b817d86a934cfee4d5ae563657e3bd5f91`; 15×3 normy zachowane bez zmian.
- Poprzedni pełnosieciowy referent ROT28: `IW_M13_ROT28_mask_extrapolation_and_shells_20261023.json` (SHA256 `f1bef51408899fe00286b25a291865fce846a11d32bd3a8f552066553439d1b5`). To dane obliczone numerycznie, nie niezależny od projektu pomiar fizyczny.
- Retained helper do tensorowego RMS: `deepseek_python_20260627_a87249.py`, SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`.
- Skrypt `verify_m13_rot29.py` weryfikuje **dokładnie wymierne** momenty wag i certyfikaty dualne, 9 źródłowych wierszy eksperymentalnych, kontrprzykład dodatnich gęstości niskopasmowych, a także wywołania *niezmienionej* funkcji `rms_norm` na dwóch syntetycznych rzeczywistych polach. Pełny 9×8 ledger estymatorów w JSON.
- Historyczny oryginalny `dtc0a_runtime_v0_3_1.py` z deklarowanym hashem `2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084` wciąż niedostępny. Bez byte-exact źródła, niezależnego referee, identyfikacji fizycznego modelu czy przyjęcia przez ownera nie ma awansu interpretacji.

**Decyzja:** `PASS_EXACT_MINIMAX_L1 / PASS_9_CASE_FROZEN_EVALUATION / PASS_HELPER_NATIVE_ABSTRACT_NONMAP / HOLD_GENERAL_FULL_GRID_IDENTIFICATION / NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / TPE HOLD`.

**ROUTE_TAGS:** `IWTO_MT13 IWTO_KN11 IWTO_INT8 IWTO_XH_S4 IWTO_REC10 IWTO_LT5 IWTO_SW IWTO_MODERATOR`.