# IW / M13 — ROT18: ruchoma geometria maski w diagnostyce zbieżności DTC0a

**RETURN_ID:** `M13-ROT18-DTC0A-MOVING-MASK-DOMAIN-CONVERGENCE-TYPING-001_20261022`  
**Linia:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**Data:** 2026-10-22  
**Klasa:** audyt wtórny rzeczywistych danych tabelarycznych DTC0a, geometria dyskretnej maski / typowanie wniosków o zbieżności.  
**Status:** `POSTPROCESS_VERIFIED / RUNNER_NOT_REBUILT / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / TPE HOLD`.

## 0. Zakres, pochodzenie i subtraction

Przetworzono bez modyfikowania 18 wierszy (`N=31,33,35,37,39,41` × `α=0,.05,.2`) z pliku `dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv` oraz 15 wierszy testu czułości maski (`N=41`, `interior_k=2..6`) z `dtc0a_mask_sensitivity_N41_v0_3_1.csv`. Dane i manifest wskazują `L=2π`, `stencil_order=2`, `E_mode=E_lin`, `interior_k=3` w podstawowej serii. Powtórnie policzono 12 logarytmicznych nachyleń metryk, zgodnych ze źródłową tabelą podsumowania; bez ponownego wykonania diagnostyki pól.

Ograniczenia znane wcześniej: projekt zarejestrował malejące `K_C/K_B`, plateau `K_A` i ograniczenia nośnika, Nyquist dla parzystego N, operatorowy i projekcyjny kanał. Ta praca nie przedstawia zachowania `K_A` jako nowego odkrycia. Jej wkład to **dokładne wytypowanie ruchomej dziedziny RMS** oraz rzeczywisty porównawczy endpoint przy bliskiej stałej szerokości fizycznej maski. Zewnętrzny materiał XH-S4 o alias-free Jacobi z 2026-10-21 stanowi analogię metodologiczną, NIE dowód tego samego mechanizmu w DTC0a.

## 1. Matematyka maski: nie jest to stała dziedzina fizyczna

Udostępnione historyczne pomocnicze źródła `deepseek_python_20260627_349584.py` i `deepseek_python_20260627_a87249.py` zawierają `get_mask_slice(N,k,...)=slice(k,N-k)`, a funkcja RMS odczytuje tensor na sześcianie wyznaczonym tym wycinkiem we wszystkich trzech osiach. Dla periodycznej siatki `dx=L/N`, pod maską:

- liczba węzłów RMS = `(N-2k)^3`;
- udział węzłów / względnej objętości = `((N-2k)/N)^3`;
- usunięta fizyczna szerokość z jednej strony osi = `k L/N`.

Przy stałym `k=3` i wzroście N z 31 do 41: szerokość pasa maleje z **0.60805019** do **0.45974527** (−24.39%), a udział domeny RMS rośnie z **0.52448726** do **0.62208906**, tj. **o 18.6090% względnie** (9.7602 punktu procentowego absolutnie). N41 k4 ma szerokość 0.61299369, czyli zaledwie **0.8130%** więcej niż N31 k3; udział domeny 0.52142308, niemal taki sam jak 0.52448726.

W konsekwencji wartości RMS ze stałym `k=3` badają przy zagęszczaniu **zmieniające się fizycznie okno**, które asymptotycznie rozszerza się na prawie całą domenę. Jeżeli celem jest estymowanie zbieżności operatora na *stałym fizycznym podobszarze*, trzeba porównywać maski skalowane według `k_N≈round(r N/L)`, z kontrolą schodków zaokrąglenia. Stałe k może mieć sens do badania asymptotyki pełnodomenowej, ale samo przez się nie izoluje błędu dyskretyzacji od ruchu dziedziny i próbkowania pola.

## 2. Dokładny kontrast endpointów z istniejących danych

Porównano N31 k3 do N41 k3 (oryginalna konwencja) oraz N31 k3 do N41 k4 (blisko stały fizyczny bufor). Wszystkie zmiany są procentowe względem N31 k3, **bez** imputacji brakujących masek na N33–39.

| α | ΔK_A N41 k3 | ΔK_A N41 k4 | ΔK_C N41 k3 | ΔK_C N41 k4 | Δ(K_A/K_C) k3 | Δ(K_A/K_C) k4 |
|---:|---:|---:|---:|---:|---:|---:|
| 0.0 | +1.65% | +0.40% | -40.76% | -42.57% | +71.59% | +74.80% |
| 0.05 | +1.93% | +0.67% | -40.51% | -42.19% | +71.34% | +74.14% |
| 0.2 | +2.76% | +1.48% | -40.16% | -41.59% | +71.72% | +73.72% |

Dla `α=.05`, oryginalne +1.926% zmiany `K_A` staje się +0.667% przy blisko dopasowanym buforze. Jednocześnie `K_C` maleje ~40–42% w obu porównaniach. To wystarcza do odrzucenia niekwalifikowanej interpretacji nachyleń jako *czystego* rzędu operatora, ale **nie wystarcza do rozdzielenia ilościowo** wszystkich składników błędu przestrzennego: fizyczne domeny są tylko zbliżone, nie identyczne; pola próbkowane są na innych siatkach, a dane nie obejmują pełnej serii masek dla wszystkich N.

## 3. Algebraiczna interpretacja rosnących ilorazów

W serii z `k=3`, dla `α=.05`, `K_A` wzrasta o 1.926%, `K_C` maleje o 40.513%, a iloraz `K_A/K_C` rośnie o 71.342%. Jest to przede wszystkim konsekwencja malejącego mianownika, nie wzrostu bezwzględnego `K_A`. Dokładna tożsamość:

`Δln(K_A/K_C)=Δln(K_A)−Δln(K_C)`.

Liczby dla `α=.05`: `+0.538491=+0.019074−(−0.519416)`. To rozdział **algebraiczny**, nie oszacowanie przyczynowe. Podobnie dla `α=0` i `.2`: ilorazy rosną ~71–72% przy wzroście `K_A` tylko ~1.6–2.8%. Stałe dodatnie `K_A` już dla `α=0` dowodzi, że nie można automatycznie traktować jego amplitudy jako osobnego śladu działania deformacji form factor; to diagnostyka konstrukcji `K_A` i jej projekcji/normy.

## 4. Granice audytu i obowiązująca decyzja

1. **EARNED:** tożsamości geometrii maski, kontrola 12 log-log slope, obliczone endpointy dla trzech α i rozdział logarytmiczny ilorazów. Postprocessing reprodukowalny z dwóch źródłowych CSV, manifestu i summary.
2. **NOT EARNED:** dowód zbieżności w continuum przy ustalonej fizycznej domenie, teza o rzędu 2 obliczanej całej diagnostyki, usunięcie aliasingu, rekonstrukcja oryginalnych pól, źródłowa implementacja `K_A`, niezależne potwierdzenie wartości z oryginalnego runu, twierdzenie o fizycznym IDG/NCDG lub porównanie z historycznym 4D wynikiem.
3. **SOURCE BINDING:** manifest deklaruje SHA256 źródła `dtc0a_runtime_v0_3_1.py` = `2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084`; plik odpowiadający temu bajtowemu źródłu **nie jest dostępny** w bieżącym montażu. Dostępne skrypty pomocnicze pokazują postać maski, ale nie potwierdzają byte-exact runtime. Weryfikacja jest wyłącznie read-only na dostarczonych tabelach i na znanej konwencji `slice(k,N-k)`.
4. **Proporcjonalność skalowania amplitudy** w oddzielnych tabelach nie zmienia wyniku: skala pól i geometria maski to różne kontrakty.
5. **KILL-TEST:** powtórzona pełna seria po N z jednym ustalonym geometrycznie podobszarem może zachować lub zmienić nachylenia. Dopóki nie istnieje w tych samych źródłach, nie przenosić nachyleń `K_C~N^-1.86` i `K_B~N^-2.01` na rząd dyskretnego operatora ani `K_A~const` na fizyczny invariant.

Wartość pracy: typowanie `GRID_REFINEMENT_WITH_FIXED_INTEGER_MASK != OPERATOR_CONVERGENCE_ON_FIXED_PHYSICAL_DOMAIN`, z kontrolowanym przykładem ilościowym. Bez nowego zadania dla Moderatora; żadnej prośby o wykonanie dodatkowego runu.

## 5. Pochodzenie i kontrola

- `dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv` — SHA256 `1ed5dec5797ed1bc0ae9c4a924e1f18ef0a118f5602be99f03c953fd532cd66e`
- `dtc0a_mask_sensitivity_N41_v0_3_1.csv` — SHA256 `4dc228e1edab9fefc219118b5ba465b817d86a934cfee4d5ae563657e3bd5f91`
- `dtc0a_oddN_sparse_convergence_summary_v0_3_1.csv` — SHA256 `884ae20139554e758e4df46817294b652fc21c24fa09037a749f9c9d8a6ff452`
- `dtc0a_oddN_sparse_convergence_N31_to_N41_manifest.json` — SHA256 `a2341e5017c589a306e0282f37939a387d06bb3cb739ce8d6a2884600c057da7`

Reprodukowalny skrypt wtórnej analizy: `verify_m13_rot18.py` (standardowa biblioteka Pythona, wyłącznie czytanie CSV, zapis JSON) generuje `IW_M13_ROT18_mask_geometry_summary_20261022.json`. Sprawdzono: liczba wierszy 18/15, manifest, zgodność source_hash tam, gdzie występuje, 12 nachyleń, 3 zestawy ilorazów oraz tożsamości geometrii. Wynik: **PASS**. Żaden obiekt NCDG nie jest przeliczany ponownie.

**ROUTE_TAGS:** `IWTO_MT13 IWTO_LT5 IWTO_MECH_S7 IWTO_REC10 IWTO_INT8 IWTO_KN11 IWTO_SW IWTO_MODERATOR`.  
**STOP:** `NO_NEW_TASK / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / TPE HOLD`.
