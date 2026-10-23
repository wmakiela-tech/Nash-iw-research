# IW / M13 — ROT25: ilościowy rozdział źródła śladowego, przecieku kompresji TT i rzeczywistego residualu na historycznie dopasowanej rodzinie DTC0a

**RETURN_ID:** `M13-ROT25-DTC0A-FUNCTIONALLY-REPLAYED-TRACE-SECTOR-AND-PROJECTOR-INSERTION-LEDGER-001_20261023`  
**CELL:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**DATA:** 2026-10-23  
**PROBLEM_ID:** `P3_DTC0A_TT_MASK_COMMUTATION_AND_LOCAL_RMS_TYPING_001` / część programu `P3_DTC0A` (bez tworzenia nowego węzła właścicielskiego)  
**KLASA:** `EXACT_FINITE_OPERATOR_IDENTITY / 18_SOURCE-MATCHING_FUNCTIONAL_REPLAY / REAL_FIELD_LEAKAGE_QUANTIFICATION / MATURE_HOST / NO_NOVELTY`  
**STATUS:** `HELPER_FUNCTIONAL_REPLAY_PASS / DIRECT_NATIVE_TENSOR_CHECK_PASS / ORIGINAL_RUNNER_BYTE_EXACT_MISSING / REFEREE_PENDING / NO_CANON / NO_EXEC_SIGN / TPE HOLD`.

## 0. Currentness, subtraction i rozgraniczenie autorstwa

Dane M13 ROT23 odtworzyły 99/99 historycznych norm DTC0a na podstawie oryginalnego zachowanego helpera `deepseek_python_20260627_a87249.py` (nie tożsamego bajtowo z deklarowanym runtime v0.3.1). ROT24 odtworzył współczynniki tensorowe `U,V,W` dla 18 prób skanu alpha. ROT21–22 dowiodły możliwości i ostrego limitu przecieku przez maskę przestrzenną. **Te obserwacje nie były jeszcze pełnym wyliczeniem źródła dużego K_A w konkretnym dopasowanym polu.**

**Pierwszeństwo innych komórek, bez zawłaszczenia:** XH-S4 ROT018/ROT019 pierwszy wykazał dokładną tożsamość `K_A-K_B` z bloków `P L_i Q L_j` i rozróżnił pełną domenę `Sym²` od właściwego TT-restricted `K_A(P h)`. XH-S4 ROT019 zidentyfikował tworzenie TT przez *strain* przy śladowym `h=fI` i wykonał przekrojowe kontrole na N17/N31 oraz pochodnych spektralnych; Geeky-S10 badał osobno blokową geometrię kompresji, INT8 błąd symbolu różnicowego i dyskretnego Leibniza. To są istniejące ustalenia. **Przyrost ROT25 jest węższy i źródłowo liczbowy:** pełne rozliczenie amplitudy dwóch członów przecieku i ich interferencji dla **18 z 18** historycznie dopasowanych pól (6 siatek i 3 alpha), razem z niezmodyfikowanym natywnym wywołaniem kontrolnym.

Źródło XH-S4:
https://github.com/wmakiela-tech/Nash-iw-research/blob/c1cee5ba11727266a7f7052e470931f6d9213f44/research/xh-s4/2026-10-23/IW_XH_S4_DTC0A_TT_DOMAIN_SPECTRAL_DERIVATIVE_AND_COMMUTATOR_HOST_AUDIT_019_20261023.md

## 1. Dokładne twierdzenie operatorowe i prawidłowa domena

Dla zachowanego `order=2`, `E_alpha=I+alpha*S_N`, `L_i = Lie_{C_i} \circ E_alpha`, `L_b=Lie_{[C_1,C_2]} \circ E_alpha`, P = pełny fourierowski projektor TT, Q=I-P:

```
K_C(h) = (L1 L2 - L2 L1 - Lb) h
K_B(h) = P K_C(h)
K_A(h) = (P L1 P L2 - P L2 P L1 - P Lb) h

D(h) := K_A(h) - K_B(h)
     = P L2 Q L1 h - P L1 Q L2 h
     =: D_plus + D_minus.
```

Dowód: odjęcie `P[L1L2-L2L1-Lb]` od wzoru z pośrednim P i zastąpienie `P-I=-Q`; wyrazy z `L_b` dokładnie się redukują. To **tożsamość skończeniewymiarowa**, a nie nowa dynamika. Dla otrzymanych tensorów pełnych, obcięcie ich maską RMS (`interior_k=3`) następuje dopiero na końcu. Tożsamość obowiązuje także po tym obcięciu.

**Typ celu (XH-S4):** wejściowe `h=f(x,y)I`, z `f=.1sin(x)cos(y)`, należy do `ker(P)` dla każdej badanej nieparzystej siatki. Dlatego `K_A(P h)=0` do błędu numerycznego; surowego `K_A(h)` **nie wolno** przedstawiać jako reprezentacyjnej wady na wejściowej podprzestrzeni TT. Wyjściowy `K_A(h)` może być tensorowo TT i niezerowy, ponieważ działanie `L_i` na tensor śladowy nie zachowuje `ker(P)`.

Dla `g=E_alpha f` oraz pochodnej centralnej `D_i` zachodzi **dokładnie na tej siatce**:

```
Lie_C (g I)_ij = (C·D g) δ_ij + g (D_i C_j + D_j C_i).
P Lie_C E_alpha(f I) = P[ g (D_i C_j + D_j C_i) ].
```

Pierwszy człon (adwekcja skalara) znika po TT; *strain* stanowi pełne źródło pierwszego nietrywialnego etapu. Nie wynika stąd fizyczna tożsamość krzywizny przestrzeni ani gauge-invariant propagacja grawitacyjna.

## 2. Wynik liczbowy na 18 historycznie dopasowanych konfiguracjach

Pełne pola `C_1,C_2,h` są generowane na każdej siatce przez `deepseek_python_20260627_a87249.py`; następnie wykonano **od początku** L, E, P, K_C, K_B, K_A oraz obie strony wzoru na D. W każdej próbie `N=31,33,35,37,39,41`; `alpha=0,.05,.2`; `L=2π`; maska k=3. Wszystkie 54 historyczne normy (3 na każdą konfigurację) są odtworzone z maksimum relatywnego błędu **4.441e-16**. Największy błąd równości `K_A=K_B+D` po maskowaniu: **8.749e-16**. Błąd pierwszego etapu *strain* względem natywnego Lie+P: **2.423e-15**. Natywne, niezmodyfikowane `compute_K_A_out` z pętlami FFT zostało dodatkowo wywołane dla N31, alpha=.05 i porównane jako CAŁY TENSOR: relatywny błąd **6.026e-16**.

Najważniejsze zakresy **nie są procentowym rozdziałem energii**:

- `||D||_RMS / ||K_A||_RMS = 0.974349..1.001156` (**97.43–100.12%**): człon wstawienia TT odpowiada za niemal całą normę K_A w tej rodzinie.
- `||K_B||_RMS / ||K_A||_RMS = 0.004360..0.036134` (**0.44–3.61%**): pełny projektowany residual komutatorowy jest normowo mały wobec K_A.
- Dwa składniki `D_plus`, `D_minus` mają osobno normy rzędu **84–87%** i **65–67%** normy K_A; ich cosinus jest ujemny (`-0.164880..-0.152043`), więc występuje częściowe znoszenie.
- `||P h||_full/||h||_full = 8.813e-17..1.866e-16`: wejście jest numerycznie czystym śladem; nie jest samym sobie TT.

| N | α | ∥K_A∥ RMS | ∥K_B∥/∥K_A∥ | ∥D∥/∥K_A∥ | ∥D_+∥/∥K_A∥ | ∥D_-∥/∥K_A∥ | cos(D₊,D₋) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 31 | 0.00 | 3.78852976e-05 | 0.007919 | 1.001156 | 0.869075 | 0.660551 | -0.164880 |
| 31 | 0.05 | 3.76475685e-05 | 0.011783 | 0.994548 | 0.862141 | 0.657935 | -0.164871 |
| 31 | 0.20 | 3.69472353e-05 | 0.036134 | 0.974349 | 0.840955 | 0.649864 | -0.164840 |
| 33 | 0.00 | 3.80213530e-05 | 0.006926 | 1.001023 | 0.866278 | 0.661749 | -0.162495 |
| 33 | 0.05 | 3.78114539e-05 | 0.010352 | 0.995176 | 0.860153 | 0.659423 | -0.162487 |
| 33 | 0.20 | 3.71917393e-05 | 0.031865 | 0.977346 | 0.841481 | 0.652272 | -0.162463 |
| 35 | 0.00 | 3.81529710e-05 | 0.006106 | 1.000915 | 0.863485 | 0.662764 | -0.159913 |
| 35 | 0.05 | 3.79662572e-05 | 0.009161 | 0.995706 | 0.858037 | 0.660683 | -0.159907 |
| 35 | 0.20 | 3.74139751e-05 | 0.028292 | 0.979851 | 0.841462 | 0.654300 | -0.159888 |
| 37 | 0.00 | 3.82785052e-05 | 0.005423 | 1.000826 | 0.860757 | 0.663639 | -0.157264 |
| 37 | 0.05 | 3.81113131e-05 | 0.008160 | 0.996156 | 0.855882 | 0.661765 | -0.157259 |
| 37 | 0.20 | 3.76160018e-05 | 0.025276 | 0.981966 | 0.841073 | 0.656033 | -0.157244 |
| 39 | 0.00 | 3.83972253e-05 | 0.004849 | 1.000750 | 0.858132 | 0.664403 | -0.154628 |
| 39 | 0.05 | 3.82466265e-05 | 0.007312 | 0.996541 | 0.853745 | 0.662707 | -0.154624 |
| 39 | 0.20 | 3.77998818e-05 | 0.022709 | 0.983767 | 0.840436 | 0.657531 | -0.154612 |
| 41 | 0.00 | 3.85089370e-05 | 0.004360 | 1.000685 | 0.855630 | 0.665077 | -0.152057 |
| 41 | 0.05 | 3.83725630e-05 | 0.006588 | 0.996872 | 0.851662 | 0.663535 | -0.152053 |
| 41 | 0.20 | 3.79675572e-05 | 0.020508 | 0.985314 | 0.839638 | 0.658838 | -0.152043 |

**Konkretny przykład N31, alpha=.05:** `||K_A||=3.764756853e-5`, `||K_B||=4.436200376e-7`, `||D||=3.744230361e-5`. Zatem duży `K_A` jest w tym źródłowym przykładzie prawie całkowicie wrażliwy na umieszczenie pośredniej projekcji P w złożeniu operatorów, nie na sam `P K_C`. Współczynnik `||D||/||K_A||` jest porównaniem norm dwóch wektorów, a NIE eksperymentalnie odizolowanym przyczynowym procentem wpływu.

## 3. Dlaczego to wyjaśnia plateau, ale nie wyjaśnia fizyki

W analizowanej rodzinie, gdy N rośnie, `K_B` maleje w przybliżeniu jak oczekiwano dla różnicowania drugiego rzędu, natomiast duży wkład `D` związany ze **stałym, nielokalnym projektorem na tle euklidesowym** pozostaje rozmiaru ok. `3.6–3.9e-5`. To nadaje obserwowanemu niemal stałemu `K_A` konkretną, źródłowo obliczoną interpretację: jest to w dominującej części *projection-insertion residual* na polu wejściowym czysto śladowym, w którym TT pojawia się pod wpływem odkształcenia Liego. Bezpośredni kontrolny wynik XH-S4 z pochodnymi FFT (alpha=0, N31: `K_C≈1.6e-18`, `K_A≈3.84e-5`) wspiera odrębność tego toru od samego błędu stencil order2; tego testu XH-S4 NIE przypisujemy M13.

**Nie uzyskano:** normy operatorowej niezależnej od siatki lub gwarancji granicy kontinuum, identyfikacji gauge-invariant TT radiative observable, fizycznego niezmiennika `K_A`, identyfikacji J3/K ani dowodu „nowej fizyki”. Właściwa TT-domena `h=Ph` wymaga osobnej oceny; XH-S4 już pokazał niezerowy residual dla pewnego `h_TT` i nie wolno mylić go z zerem `K_A(P(fI))`.

W szczególności `D` jest ogólną tożsamością z wcześniejszego XH-S4, a niniejsza praca wnosi nowe **pełne 18/18 ilościowe pozycje** na rodzinie dopasowanej do starej tabeli; nie udaje niezależnej fizycznej replikacji.

## 4. Walidacja, pochodzenie, STOP

- Source helper matching historical RMS: `deepseek_python_20260627_a87249.py` SHA-256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`.
- Frozen source CSV: `dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv` SHA-256 `1ed5dec5797ed1bc0ae9c4a924e1f18ef0a118f5602be99f03c953fd532cd66e`.
- Reproducer ROT25: `verify_m13_rot25.py` SHA-256 `c91082840bdbbeba1381d884a81599fb26ed8e55568fb9599c08566629b7cdec`.
- Machine data: `IW_M13_ROT25_trace_to_TT_insertion_summary_20261023.json` SHA-256 `3ded076db8d702a598fbee5089685d4258e1eb8984d2d6c0acc97bc549f8123b`.
- Techniczny log: `IW_M13_ROT25_execution_log_20261023.txt`.
- Historia nieobecnego oryginalnego runnera: `dtc0a_runtime_v0_3_1.py` deklarowany SHA-256 `2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084`, **nie został odtworzony bajtowo**; dopasowanie outputu nie oznacza tożsamości kodu.

**PASS:** pełny przebieg 18/18; zgodność 54 norm; tensorowa tożsamość operatorowa 18/18; źródło strain→TT 18/18; bezpośredni natywny source call 1/1.  
**HOLD:** niezależny REC10/SW referee niepotwierdzony; KN11/BW ingestion niepotwierdzony; zero awansu physical/EXEC.  
**OWNER ROUTING:** `IWTO_MT13 IWTO_KN11 IWTO_INT8 IWTO_XH_S4 IWTO_REC10 IWTO_LT5 IWTO_SW IWTO_MODERATOR`.  
**STOP:** `NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / TPE HOLD`.