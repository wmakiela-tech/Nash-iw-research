# IW / M13 — ROT19: ranga dowodowa kontroli DTC0a, jednorodność amplitudy i kontrast klasy pól

**RETURN_ID:** `M13-ROT19-DTC0A-SCALING-TEST-RANK-AND-FIELD-CLASS-EVIDENCE-GATE-001_20261023`  
**CELL:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**DATE:** 2026-10-23  
**CLASS:** frozen-CSV controls audit + exact structural homogeneity proof from retained helper code; **not** runtime reconstruction or independent physics validation.  
**STATUS:** `POSTPROCESS_VERIFIED / EXACT_HELPER_CODE_HOMOGENEITY / FIELD_CLASS_CONFOUNDING_OPEN / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_TASK / TPE HOLD`.

## A. Stan wiedzy / subtraction-first

ROT18 rozdzielił ruch fizycznej domeny RMS pod stałym `interior_k` od deklarowanego rzędu różnicowania. Wcześniejsze testy znały zarówno plateau `K_A`, jak i zależność od projekcji `P_TT`; ich nie odkrywam ponownie. ROT19 sprawdza **ortogonalny względem ROT18 typ ograniczenia interpretacji**: wiele „pass” na skalowaniu amplitudy jest matematycznie wymuszone jednorodnością konstrukcji, podczas gdy zmiana klasy pól nie jest równoważna skalowaniu amplitudy. Dane pochodzą z zamrożonych plików z czerwca 2026, a projektowa aktualność komórek i claim ceilings zostały sprawdzone poprzez Slack w bieżącym obrocie. M13 nie przejmuje roli MT13/MECH-S7/REC10 ani prawa do EXEC.

## B. Źródła i deklarowany kontrakt

Źródłowe tabele:

1. `dtc0a_amplitude_scaling_N31_alpha005_v0_3_1.csv` — **14 wierszy**: 5 h-scale, 5 C-scale, 4 combined-scale; stałe `N=31`, `alpha=0.05`, `interior_k=3`.
2. `dtc0a_field_class_control_custom_gaussian_N31_v0_3_1.csv` — **4 wiersze**, z czego jedna referencja trygonometryczna, trzy niestandardowe periodyczne Gaussy `sigma=0.5,1,2`; komentarz źródłowy: `custom field class in runner; not DS exact provenance`.
3. `dtc0a_swap_fields_alpha005_N31_v0_3_1.csv` — 3 wiersze testu zamiany generatorów.
4. `dtc0a_E_operator_control_N31_v0_3_1.csv` — 1 wiersz porównania `Identity` i `E_lin` przy `alpha=0`.
5. `dtc0a_stencil_order_claim_audit_v0_3_1.csv` — 3 oczekiwane `NotImplementedError` dla `order=4`.
6. `dtc0a_F0_F4_noA_calibration_n10_N31_v0_3_1.csv` — 6 etykiet kalibracyjnych, po 10 replikacji według tabeli.
7. `dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv` — tylko do pomocniczego porównania `alpha=0` z `alpha>0`, NIE nowy run.

`dtc0a_mask_and_scaling_checks_v0_3_1_manifest.json` wiąże wyniki z **deklarowanym**, lecz obecnie nieudostępnionym bajtowo źródłem `dtc0a_runtime_v0_3_1.py`, `SHA256=2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084`. Dostępny skrypt pomocniczy `deepseek_python_20260627_a87249.py` ma **inny hash**, nie może być podmieniony jako tożsamy oryginalny runtime. W tym obrocie nie uruchomiono pipeline'u pól.

## C. Twierdzenie strukturalne: wymuszony kierunek 1D w skalowaniu

W udostępnionym skrypcie pomocniczym `apply_E(h)` i `apply_P_TT(h)` są liniowe w tensorze przy ustalonych parametrach, `lie_derivative_tensor(C,h)` jest liniowe osobno w `C` i `h`, a `lie_bracket(C1,C2)` jest dwuliniowy oraz antysymetryczny. `compute_K_C` jest kombinacją `T(C1,T(C2,h)) - T(C2,T(C1,h)) - T([C1,C2],h)`, `K_B=P_TT(K_C)`, natomiast `K_A` wykorzystuje zagnieżdżone projektowane `T`. Dla wspólnego mnożnika obu generatorów `s` i mnożnika tensora `t`, przy NIEZMIENIONYCH `N,alpha,dx,E_mode,P_TT`:

`K_j(s C1, s C2, t h) = s^2 t K_j(C1,C2,h)` dla `j=A,B,C`.

Wynik jest algebraicznie exact w tej klasie kodu; dla norm RMS `||K_j'||/||K_j||=|s|^2|t|` (dla niezerowego mianownika). Stąd trzy wektory metryk `v=(K_C_RMS,K_B_RMS,K_A_RMS)` mierzone na kolejnych przebiegach skalowania **muszą być proporcjonalne** do jednego wektora bazowego. Macierz `14×3` ma z założeń rząd co najwyżej 1. To jest własność projektowanego testu, nie empirycznie odkryta korelacja.

W **14/14 źródłowych wierszach** dla dodatnich `s,t` zachodzi dokładnie do zapisanej precyzji `v(s,t)=s^2 t v(1,1)`; największa odchyłka względna i dryf ilorazów wynoszą **0,0** przy obliczeniach na sparsowanych wartościach binarnych. Ilorazy pozostają:

- `K_C/K_B=4.8097988476`,
- `K_A/K_C=17.6440737464`,
- `K_A/K_B=84.8644455725`.

**Claim typing:** 14 pozytywnych przypadków potwierdza spójność jednorodności i poprawne raportowanie. Nie jest to 14 niezależnych kierunków pobudzenia, niezależna walidacja źródła `P_TT`, ani nowy dowód continuum zbieżności. Użyteczny test niezależności wymagałby perturbacji **geometrii/polaryzacji/widma** pól lub niezależnego modelu źródłowego, a nie kolejnych wartości tego samego parametru skalowania.

## D. Kontrast klasy pól — odrębna informacja, ale bez identyfikacji przyczyny

Przy `N=31`, `alpha=0.05`, `interior_k=3`:

| Pole | `K_C/trig` | `K_B/trig` | `K_A/trig` | `K_A/K_C` | `(K_A/K_C)/(trig)` |
|---|---:|---:|---:|---:|---:|
| trig reference | 1.000000 | 1.000000 | 1.000000 | 17.644074 | 1.000000 |
| periodic Gaussian, sigma=0.5 | 0.468062 | 0.652044 | 0.030412 | 1.146408 | 0.064974 |
| periodic Gaussian, sigma=1.0 | 0.263226 | 0.270546 | 0.096160 | 6.445654 | 0.365316 |
| periodic Gaussian, sigma=2.0 | 0.198299 | 0.077260 | 0.060259 | 5.361632 | 0.303877 |

Różnice `K_A/K_C` **nie mogą** wynikać wyłącznie z jednego wspólnego przeskalowania generatorów i tensora, gdyż takie skalowanie zachowuje iloraz dokładnie. To wyklucza prostą **hipotezę wspólnego mnożnika** jako kompletne wyjaśnienie tych tabel, ale nie rozróżnia zmian widma, przestrzennego profilu, TT i domeny projekcji. Gaussy są `custom`, bez źródłowej rekonstrukcji DS. Nie twierdzić, że różnica dowodzi form-factor physics.

Dodatkowy kontekst źródłowy: w podstawowych tabelach `K_A_RMS` już przy `alpha=0` ma wartość `3.7885297593e-5` na `N=31`. Przy `alpha=0.05`, `K_C` rośnie względnie o `39.31%`, `K_B` o `47.86%`, a `K_A` maleje o `0.6275%` względem tego samego `N,alpha=0`. Te liczby są algebraicznym kontrastem, nie pomiarem efektu fizycznego i NIE rozdzielają `E_mode` od innych składników konstrukcji.

## E. Które dodatnie kontrole są strukturalne?

- **Swap C1↔C2**: normy bazowe i po zamianie są takie same, a `rms_of_sum=0`, `max_abs_sum=0` dla wszystkich trzech `K`. W podanym pomocniczym kodzie jest to konieczna antysymetria całego wyrażenia, ponieważ `[C2,C1]=-[C1,C2]`; należy traktować jako test kodu, nie trzy niezależne świadectwa fizyki.
- **`E_lin` przy `alpha=0` ≡ `Identity`**: w pomocniczej implementacji `E_lin(h)=h+alpha*dx^2*Δ_discrete(h)`, stąd zgodność jest algebraicznie wymuszona. Źródłowa tabela: sześć różnic RMS/max tensor = 0. Nie dowodzi nic o działaniu niezerowego `alpha` w continuum.
- **Kalibracja `F1`/`F4_C`**: tabele podają dokładnie takie same `mean=5.1337055496e-6` i `std=2.36254374895e-8` przy `n_repeats=10`. Pomocniczy kod wywołuje w obu przypadkach to samo `compute_K_C` z `Identity` i `h_perturbed`; to duplikat tej samej procedury w ramach tej rekonstrukcji, nie dwa niezależne eksperymenty. Wartości `F4_B` nie są identyczne i nie są tutaj redukowane do `F1`.
- **Stencil czwartego rzędu**: `derivative_order4`, `compute_K_C_order4` i `run_pipeline_order4` wszystkie mają status `ERROR_EXPECTED / NotImplementedError`. To jawna **nieobecność porównania 2-vs-4**, a nie negatywny test rzeczywiście uruchomionego schematu rzędu 4.

## F. Wniosek integracyjny i negative knowledge

**EARNED:** warunkowy dowód jednorodności `s^2 t` z dostępnego skryptu pomocniczego, dokładny przegląd 14/4/3/1/3/6 wierszy CSV, oddzielenie zdegenerowanych kontroli amplitudy od zmiany klasy pól, wykazanie nietożsamości `E_lin(alpha=0)` i porównania `E_lin(alpha!=0)` jako dwóch niezależnych testów, audyt etykiet `order4`.

**NOT EARNED:** dowód wektora residualu w oryginalnym bajtowo runtime, niezależna replikacja generatorów gaussowskich, identyfikacja kanału fizycznego, izolowanie wpływu TT od widma, podwyższenie statusu `K_A`, 4. rząd zbieżności, continuum physical observable, `GO_SEN_CHECK`, `EXEC_SIGN`, historyczne 4D `0.522`.

**Minimalny bezpieczny wpis:**

`SCALAR_AMPLITUDE_PASS_FAMILY (14 rows) => ALGEBRAIC_EQUIVARIANCE_CONTROL, NOT 14 INDEPENDENT SCIENTIFIC REPLICATIONS. GAUSSIAN_FIELD_CLASS changes K_A/K_C by factors 0.065..0.365 (relative to trig) and defeats common-scaling explanation, BUT FIELD_SPECTRUM/POLARIZATION/ORIGIN NOT CONTROLLED. ORDER4=NOT_IMPLEMENTED. F1_F4C_DUPLICATE_CONTRACT.`

**Źródła i weryfikowalność:** pełne hashe SHA256 siedmiu wejść zapisano w `IW_M13_ROT19_evidence_rank_summary_20261023.json`, skrypt standardowej biblioteki `verify_m13_rot19.py` czyta tylko zamrożone pliki, weryfikuje wiersze, proporcjonalności i kontrolne tożsamości, wypisuje `PASS`. Wszelkie wnioski o przyczynach zmian Gaussów oraz tym, jaki fizyczny model miały reprezentować, pozostają otwarte.

**ROUTE_TAGS:** `IWTO_MT13 IWTO_MECH_S7 IWTO_LT5 IWTO_INT8 IWTO_REC10 IWTO_KN11 IWTO_SW IWTO_MODERATOR`.  
**STOP:** `NO_NEW_TASK / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / TPE HOLD`.
