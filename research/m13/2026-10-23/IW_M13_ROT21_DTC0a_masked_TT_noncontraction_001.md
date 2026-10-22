# IW / M13 — ROT21: maskowana projekcja TT, utrata kontraktywności RMS i nieistnienie mapy lokalnych residuali

**RETURN_ID:** `M13-ROT21-DTC0A-MASKED-TT-NONCONTRACTION-AND-LOCAL-NONMAP-001_20261023`  
**CELL:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**DATA:** 2026-10-23  
**CLASS:** EXACT FINITE-HILBERT THEOREM + DIRECT REPLAY OF RETAINED DTC0a TT/RMS HELPER ON SYNTHETIC INPUTS  
**CEILING:** `SYNTHETIC_HELPER_REPLAY / ORIGINAL_RUNTIME_BYTE_EXACT_UNAVAILABLE / NOT_HISTORICAL_K_REPLAY / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_CLAIM / NO_NEW_TASK / TPE HOLD`.

## 0. Punkt odniesienia i rzeczywisty przyrost wiedzy

M13 ROT18 ustalił, że przy `interior_k=3` fizyczna dziedzina RMS zmienia się podczas refinacji N; ROT19, że testy wspólnego skalowania amplitudy są jedną algebraicznie wymuszoną rodziną; ROT20, że trzy same normy z różnych α nie identyfikują tensorowego współczynnika kwadratowego. DTC0a stosuje także pełnosieciowy, nielokalny **fourierowski projektor TT**, a wartości `K_C`, `K_B=P_TT K_C`, `K_A` raportuje dopiero po **obcięciu przestrzenną maską**. To wprowadza odrębny, wcześniej niewyprowadzony tutaj warunek: globalna ortogonalność P nie implikuje kontraktywności na wyciętym podobszarze.

**Subtraction i currentness 2026-10-23:** INT8 ROT008 wykazał osobno niezgodność symbolu transwersalności fourierowskiej `k` z centralnym symbolem różnicowym `sin(k dx)/dx` w DTC0a; nie jest to niniejsza niekomutacja maski z P. KN11 ROT05 ustalił dwukierunkowy nonmap kompresji komutatorów `P[A,B]P` versus `[PAP,PBP]`; nie jest to niniejszy nonmap *przestrzennego wycinka* `M(PX)` względem `M(X)`. Są to odrębne typy informacji o tym samym aparacie. Projektowy priorytet P3 M13/KN11 pozostaje warunkową diagnostyką, nie awansem fizyki.

## 1. Źródłowy kontrakt DTC0a

W zachowanym helperze `deepseek_python_20260627_349584.py` (SHA256 `2fd77da6b2501d957fabf8884a2625bbafedf594399e720360e83caa344938c5`):

- `compute_K_B` dokładnie wywołuje `apply_P_TT(compute_K_C(...),dx)` na **pełnej tablicy N×N×N**.
- `apply_P_TT` bierze FFT wszystkich dziewięciu składowych tensora, dla niezerowego k używa `P(k)=I−kk^T/|k|²` i `H_TT=P H P−0.5 P tr(PH)`, a dla k=0 usuwa ślad `H−I tr(H)/3`; na końcu bierze rzeczywistą część i symetryzuje tensor.
- `rms_norm` oblicza sumę kwadratów sześciu niezależnych składowych tensora, z wagą 2 dla pozadiagonalnych, **po** selekcji `R[k:N-k,k:N-k,k:N-k,:,:]`, dzieląc przez `6(N−2k)³`.
- Manifest `dtc0a_mask_and_scaling_checks_v0_3_1_manifest.json` identyfikuje historyczny `dtc0a_runtime_v0_3_1.py` i deklaruje SHA256 `2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084`; tego dokładnego pliku NIE znaleziono w udostępnionym montażu. Pomocnik ma inny hash i nie stanowi potwierdzenia identyczności z historycznym runtime.

Niezależnie od specyficznych metryk, pomocnicza implementacja `P_TT` na **nieparzystym N** jest ortogonalnym projektorem w pełnej przestrzeni symetrycznych pól tensorowych z globalnym iloczynem Frobeniusa (moduł Fourier i zero-mode), co kontrolujemy na wybranych wektorach. Maska M jest ortogonalnym projektorem mnożącym przez 0 lub 1 w węzłach przestrzennych (dla wszystkich składowych tensora). Jej normę `||x||_M:=||Mx||` można przeskalować dodatnią stałą `1/sqrt(6(N−2k)³)` bez zmiany wniosków o nierównościach.

## 2. Twierdzenie ROT21.1 — warunek konieczny i dostateczny

Niech H będzie dowolną skończeniewymiarową rzeczywistą przestrzenią Hilberta, P i M ortogonalnymi projektorami: `P²=P=P*`, `M²=M=M*`. Wtedy:

`(∀x∈H) ||MPx|| ≤ ||Mx||  ⇔  [P,M]=0`.   (ROT21.1)

**Dowód ⇒:** jeśli `Mx=0`, to prawa strona nierówności wynosi zero, więc `MPx=0`. W szczególności `MP(I−M)=0`. Z samosprzężoności P i M po sprzężeniu hermitowskim `(I−M)PM=0`. Stąd `MP=MPM` i `PM=MPM`, zatem `MP=PM`.

**Dowód ⇐:** jeśli M i P komutują, to `||MPx||=||PMx||≤||Mx||`, bo każdy ortogonalny projektor P jest globalną kontrakcją. QED.

**Dokładny nonmap:** jeśli `MP(I−M)≠0`, to nie istnieje funkcja (nawet nieliniowa!) `F:ran M→ran M` spełniająca `F(Mx)=MPx` dla wszystkich x. Wystarczy wziąć `x0=0` oraz `x1∈ker M` z `MPx1≠0`: `Mx0=Mx1=0`, ale `MPx0=0≠MPx1`. W szczególności wynik projekcji TT *wewnątrz* maski nie wynika z samego residualu surowego *wewnątrz* maski.

Wniosek o ilorazach norm: `||Px||_M/||x||_M` nie ma skończonej uniwersalnej granicy dla wszystkich x z `||x||_M>0`, jeśli powyższy nonmap zachodzi. Dla x spoza maski z `MPx≠0`, dodaj `εv` z `Mv≠0`; mianownik idzie do zera liniowo z ε, podczas gdy licznik dąży do dodatniej stałej.

**Elementary exact control** w R²: `P=1/2[[1,1],[1,1]]`, `M=diag(1,0)`, `x=(0,1)` daje `Mx=0`, `MPx=(1/2,0)`; P jest ortogonalny, lecz nie zachowuje lokalnej półnormy. Ta dwuwymiarowa ilustracja jest klasyczną algebrą projektorów, bez nowości matematycznej.

## 3. ROT21.2 — rzeczywiste wywołania pomocniczej procedury TT na syntetycznym tensorze

Bez modyfikowania `apply_P_TT` i `rms_norm` zaimportowano zachowany helper, utworzono pole symetryczne `h_zz(0,0,0)=1`, wszystkie inne elementy 0. Węzeł (0,0,0) leży **poza** maską `k≥2`. Dla `N∈{11,31,41}` przy `dx=2π/N` policzono `p=apply_P_TT(h,dx)`. Następnie dodano drugi, mały składnik `h_zz(N//2,N//2,N//2)=10^{-3}`, aby uzyskać legalną dodatnią wejściową normę maskowaną. Dane nie są historycznymi generatorami `C1,C2,h` ani rzeczywistymi tensorami `K_C`.

| N | k | RMS_M(h) | RMS_M(Ph) | RMS_M(h+εv) | RMS_M(P(h+εv)) | iloraz po/przed |
|---:|---:|---:|---:|---:|---:|---:|
| 11 | 2 | 0 | 1.27335629e−4 | 2.20433357e−5 | 1.27869124e−4 | 5.800806 |
| 31 | 3 | 0 | 1.42757483e−5 | 3.26598632e−6 | 1.43714697e−5 | **4.400346** |
| 31 | 4 | 0 | 9.13805692e−6 | 3.70111535e−6 | 9.32826183e−6 | 2.520392 |
| 41 | 3 | 0 | 9.17039798e−6 | 1.97161588e−6 | 9.22466497e−6 | 4.678733 |
| 41 | 4 | 0 | 6.02462224e−6 | 2.15354259e−6 | 6.12254013e−6 | 2.843009 |

**Wszystkie 5/5 kontrprzykładów PASS.** W tym samym oryginalnym wywołaniu test globalny daje `||Ph||_full/||h||_full=0.507001` (N11), `0.506741` (N31), `0.506739` (N41) — **poniżej 1**, zgodnie z kontraktywnością globalną. Absolutny błąd `||P²h−Ph||_2` wynosi odpowiednio `1.26e−16`, `1.94e−16`, `2.14e−16`: idempotencja numerycznie PASS. Wynik jest więc efektem **mieszania przez niekomutujące M i P**, nie błędem projekcji w samym teście.

Identyfikowalność lokalna została obalona wprost: `M0=Mh=0` pomimo `MP0=0`, `MPh≠0`. Ponadto `Q=I−P` spełnia `MQh=−MPh` dla tego h, gdyż `Mh=0`. To ilustruje, dlaczego prawidłowe globalnie sumy kwadratów norm komplementarnych nie są automatycznie prawidłowe po masce.

## 4. Co wolno, a czego nie wolno wnioskować z historycznego K_B/K_C

**EARNED**: (a) ścisła równoważność ROT21.1; (b) jawne nieistnienie mapy lokalnej ROT21.2 dla dostępnego helpera; (c) projektor TT ma działanie nieprzestrzennie lokalne i może przenosić sygnał spoza maski do jej wnętrza; (d) normy RMS używane w tabelach historycznych nie są globalnymi normami Hilberta; (e) obliczenie `K_B` wymaga pełnego `K_C` przed maską, a nie tylko normy/wycinka `K_C` w masce.

**NOT EARNED**: stwierdzenie, że konkretny historyczny `K_B_RMS` wzrósł z powodu przecieku, że `K_B_RMS>K_C_RMS` w zapisanych wierszach, że ten efekt wyjaśnia plateau `K_A`, rozkład procentowy wkładu boundary leak dla historycznego pola, identyfikacja fizycznego mechanizmu NCDG/J3/K, dowód zbieżności operatora w continuum, ani source-native replay oryginalnego `dtc0a_runtime_v0_3_1.py`.

**Niekomutujące warunki są różne:** INT8 ROT008: `Fourier-k transversality != central-difference-delta transversality` (zgodność symboli pochodnej). ROT21: `full-domain TT orthogonality != masked RMS contractivity` (zgodność lokalnego okna z globalną projekcją). KN11 ROT05: `compression of commutator != commutator of compressions` (kompresja operatorów). Żadnego z tych twierdzeń nie zastępuje drugie.

## 5. Jeden problem — jeden stan

**PROBLEM_ID:** `P3_DTC0A_TT_MASK_COMMUTATION_AND_LOCAL_RMS_TYPING_001`.

**Source:** pomocniczy `deepseek_python_20260627_349584.py`, odczytany i wykonany w oryginalnych funkcjach `apply_P_TT`/`rms_norm`; niepodmieniony historyczny runtime i zamrożone manifesty.  
**Best result:** ROT21.1 iff `[P,M]=0`, ROT21.2 syntetyczne nonmap na N31/N41 5/5 z globalnymi kontrolami.  
**Countermodel:** tensor podparty wyłącznie poza maską ⇒ zero wejścia lokalnego i niezerowe wyjście lokalne po P_TT.  
**Referee:** niezależny REC10/SW niepotwierdzony; ten raport nie jest takim audytem.  
**Owner:** MT13 scientific programme, KN11 BW source custody; M13 autonomiczna komórka diagnostyczna, nie przejmuje uprawnień.  
**Cheapest discriminating test, conditional only:** gdyby dostępne było byte-exact oryginalne pole `K_C` przed projekcją, można by porównać `M P K_C` z `M P(M K_C)` i obliczyć dokładnie `MP(I−M)K_C`; brak tej danej nie jest nowym zadaniem dla Moderatora.  
**Decision:** `PASS_SOURCE_HELPER_SYNTHETIC / HOLD_HISTORICAL_RESIDUAL_BINDING / NO_PHYSICAL_UPGRADE / NO_NEW_TASK`.

## 6. Powtarzalność i źródła współczesne

- Skrypt: `verify_m13_rot21.py`, import i wywołania oryginalnych funkcji z zachowanego helpera; jego SHA256: `44c8c65e60eb8360bacc8e3577e990efe906925d0950bee3d43e69a497cfce92`.
- Wynik: `IW_M13_ROT21_masked_TT_nonmap_summary_20261023.json`, SHA256 `9b4e09ec8855444e61e711ca2f8ba154fdfa5ab526213731a95fe34579d756a7`.
- INT8 source-local symbol gap: https://github.com/wmakiela-tech/Nash-iw-research/blob/fa0028222dd174b89d3b22400fd16b357028c0df/research/int8/2026-10-23/iw_int8_rot008_dtc0a_fourier_tt_vs_finite_difference_divergence_symbol_gap_001.md
- KN11 two-way compression: https://github.com/wmakiela-tech/Nash-iw-research/blob/2a1d0d3dc4d5d8c7a65a6de49122065a7256c4b6/research/kn11/2026-10-23/iw_kn11_rot05_bidirectional_projector_compression_nonmap_001.md
- M13 ROT18–20: research/m13/2026-10-22 and research/m13/2026-10-23 in the project repo.

**ROUTE_TAGS:** `IWTO_MT13 IWTO_KN11 IWTO_INT8 IWTO_LT5 IWTO_REC10 IWTO_SW IWTO_MODERATOR`.  
**STOP:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_TASK / TPE HOLD`.
