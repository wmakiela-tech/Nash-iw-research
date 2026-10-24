# LT5 — ROT20: mieszany szum, dokładny minimaks celu i nowe wyniki do REV021

**RETURN_ID:** LT5-REV021-ROT20-MIXED-NOISE-ADMISSIBLE-PROJECTIVE-MINIMAX-001_20261024
**Date:** 2026-10-24
**Status:** SOURCE-TYPED MATURE OPTIMAL RECOVERY / ANALYTICAL PROOF / INDEPENDENT LOCAL NUMERIC PASS / NATIVE MANUSCRIPT VERIFIED / EXTERNAL REFEREE PENDING.
**Ceilings:** NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_HISTORICAL_DTC0A_RUNTIME / NO_J3_K_GR_PBH_PHYSICS.

**Natywna robocza REV021, naprawdę zmieniona:** https://docs.google.com/document/d/15b-8uK2DZVScU6k-K6eesL8d8nt777-UmalEUb5U-zE/edit
**Oryginalna REV020, bez zmian:** https://docs.google.com/document/d/1cn97_kO65BcJRRWQrvrL9fKlEYBT3PHg6BJItn1Q4FQ/edit

## 1. Priorytety i pytanie

LT5 ROT19 i dawne Twierdzenie 7.9 zmonografii: dokładny skalarno-celowy promień informacji. KN11: kryterium różnic dopuszczalnych. MT13: pierwszeństwo dokładnej geometrii dwóch promieni źródłowych przy jednym nieznanym wzmocnieniu, progu d>2eta i nadmiarowej kontroli trzecim kanałem. M13 ROT033: ścisłe przedziałowe pochodne źródłowego ilorazu A/C, w HELPERZE bez oryginalnego DTC runtime. M13 ROT034: źródłowa identyfikowalność z dwóch masek JEDNEGO kanału, N41 maski 2..6, 18 monotonicznych par i 12 z certyfikowanym punktem zwrotnym. Geeky-S11 ROT011: iff parzystość stencila i 48D jądro zachowania dla kroku 2. PRF11 R30: dokładna pełna norma testera JEDNEGO punktu interwencji, z pamięcią kwantową. LT5 nie przejmuje ich autorstwa.

Odrębny problem LT5: ustalić dokładne ryzyko celu, jeśli KAŻDY odczyt ma niezależny błąd względny i absolutny, a WSZYSTKIE kanały współdzielą jedno dodatnie wzmocnienie źródła.

## 2. Twierdzenie 7.9b: dokładne prostokąty danych i promień

I=[a,b], f_j:I→(0,∞), s∈[smin,smax], 0<smin<=smax<=∞; y_j=s f_j(alpha)(1+delta_j)+e_j z |delta_j|<=eps_j<1 oraz |e_j|<=eta_j. Błędy DOPUSZCZAJĄ niezależny wybór między odczytami, s jest jedną wspólną liczbą.

Kandydat alpha jest zgodny z y dokładnie wtedy, gdy niepusty jest przedział:

[smin,smax] ∩ intersection_j [
(y_j−eta_j)/(f_j(alpha)(1+eps_j)),
(y_j+eta_j)/(f_j(alpha)(1−eps_j)) ].

Dwie kompletne hipotezy (alpha,s) i (beta,t) mogą dać te SAME dane iff dla KAŻDEGO kanału j:
|s f_j(alpha)−t f_j(beta)| <= eps_j [s f_j(alpha)+t f_j(beta)] + 2eta_j.   (20.1)

Dowód: dopuszczalne dane pierwszej hipotezy tworzą prostokąt o środkach s f_j(alpha) i półszerokościach eps_j*s f_j(alpha)+eta_j. Dwa takie prostokąty mają niepuste przecięcie iff przecięcia wszystkich odpowiadających przedziałów są niepuste — dokładnie (20.1).

Dla DOWOLNEGO estymatora skalarnej alpha optymalne ryzyko minimaksowe jest dokładnie:
R*=1/2 sup{|alpha−beta|: istnieją s,t legalne takie, że (20.1) zachodzi dla wszystkich j}.   (20.2)
Dowód: po danej obserwacji wybrać środek przedziału dopuszczalnych alpha; każda zgodna para wymusza połowę różnicy. Analogicznie dla skalarnego celu T(alpha) stosuje się różnicę jego wartości. Dla REALNEGO WEKTOROWEGO celu ta połowa średnicy NIE jest ogólnym promieniem Czebyszewa. Dla błędów skorelowanych zamiast prostokątów trzeba użyć rzeczywistego wspólnego nośnika niepewności. To dojrzały optimal recovery, bez nowości matematycznej.

## 3. Ścisły pełny przykład

f(alpha)=(1,1+alpha), alpha∈[0,A], wolna wspólna dodatnia amplituda s, BRAK błędu addytywnego, niezależne |delta_j|<=eps<1. Obserwowany ratio y2/y1∈[(1+alpha)(1−eps)/(1+eps), (1+alpha)(1+eps)/(1−eps)]. Oznaczając Q=((1+eps)/(1−eps))², dwie wartości alpha<=beta mogą zostać pomylone iff (1+beta)/(1+alpha)<=Q. Stąd ŚCISŁE globalne ryzyko:
R*=1/2 min[A,(1+A)(1−1/Q)].   (20.3)

Dla eps=.005,A=.2: Q=1.0202015100628767, świadek alpha=.17623821192544797 versus beta=.2 z legalnym wspólnym odczytem, R*=.011880894037276019. Świadek można skonstruować przy s=1/(1−eps),t=1/(1+eps). Dla eps=0: R*=0. Jednak gdy obie współrzędne dopuszczają DOWOLNY dodatni błąd bezwzględny, a s może dowolnie zbliżyć się do zera, wspólny y=0 odpowiada wszystkim alpha i dokładnie R*=A/2=.1. To silny nośnik falsyfikatora kalibracji, nie dane fizyczne.

## 4. Znaczenie konkretnych źródeł NASH

M13 ROT034: na znanym źródłowym N41 i tym samym kanale j=K_C dwie maski k2/k4 mają ścisłą monotoniczność, ale skrajnie słaby konserwatywny odwrotny moduł 0.056593174. Względne eps=.005 daje błąd alpha <=0.176701; przy dwóch różnych kanałach A/C, M13 ROT033 dolne |dlnR/dalpha|>=0.8648869093985175, analogiczny bound <=0.0115623. To DWA INNE wektory odpowiedzi, nie porównanie kosztów realnego sprzętu. Maski mają nakładające się regiony i ich błędy nie są automatycznie niezależne.

Źródło M13 ROT034: https://github.com/wmakiela-tech/Nash-iw-research/blob/d63733b2b70301cda30a3cd5dfd7c3c1b4fe8c3a/research/m13/2026-10-24/IW_M13_ROT34_single_channel_multimask_identifiability_001.md
Źródło MT13: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/2026-10-24/mt13_xh_q88_m13_rot32_projective_noise_calibration_overidentification_001.md

Geeky-S11 ROT011 (inny nośnik): niezerowy skończony centralny D na EVEN N>2R i własny matched Fourier P zachowuje full-checkerboard TT przy E=I iff wszystkie niezerowe przesunięcia r mają tę samą parzystość; dwukrokowy stencil ma 48D jądro zachowania TT wobec 192D jądra D generatorów. Nie jest to fizyczny J3/K ani historical raw-k runtime.
https://github.com/wmakiela-tech/Nash-iw-research/blob/4e000446f239db464f0dff4ba89ebff68adafc27/research/geeky-s11/2026-10-24/geeky_s11_rot011_parity_criterion_and_coarse_sublattice_kernel_001.md

PRF11 R30 (inny nośnik): dla dwóch konkretnych Cauchy dephasing procesów o identycznej jednoczasowej półgrupie oraz pełnej klasie JEDNOSLOTOWYCH instrumentów kubit+tester memory, maksymalna nieznormalizowana norma śladowa z flagami D=exp(−gamma|s−t|)−exp(−gamma(s+t)), optymalny już impuls X bez dodatkowej pamięci. Przy s=t=1,gamma=.7 D=.753403036. Flaga wyniku CP z K0=X/sqrt2,K1=ZX/sqrt2 daje D z flagą i 0 po skasowaniu; nie jest to pełna nieograniczona multitime process norm.
https://github.com/wmakiela-tech/Nash-iw-research/blob/2ca01509d410a0abce479d8f6c90a99480ef493d/research/prf11/2026-10-24/IW_PRF11_R30_FULL_ONE_SLOT_TESTER_NORM_CAUCHY_PROCESS_MEMORY_001_20261024.md

## 5. Przeprowadzone kontrole, edycja i status

Niezależnie w container uruchomiono Python+NumPy:
- 2000 losowych 3-odczytowych par źródeł: kryterium (20.1) porównane z niezależnym przecięciem przedziałów i odtwarzaniem wspólnego gain; PASS.
- Ścisły R*=.011880894037276 i świadek, którego oba źródła dają te same odczyty; PASS.
- Jawny przedział wspólnej amplitudy przy zadanym y; PASS.
- Kontrprzykład dowolnie zanikającej dodatniej amplitudy i błędu bezwzględnego; PASS.
- Arytmetyczna kontrola dwóch różnych względnych boundów M13: .011562301644 oraz .176701227865; PASS.
Kod równoważnej implementacji zachowany w GitHub:
https://github.com/wmakiela-tech/Nash-iw-research/blob/20c8929a1a62c9d2cbf3ebf9ef3d722bde856213/research/lt5/2026-10-24/reproduce_lt5_rot20_mixed_noise_information_radius.py
Dodatkowy lokalny plik wykonany: /mnt/data/reproduce_lt5_rot20_mixed_noise_information_radius.py .

**Natywne zmiany w roboczej REV021:** Ch4 §4.11f M13 mask inversion/Geeky parity; Ch7 §7.5e exact mixed noise theorem and sharp toy; Ch7 §7.7b PRF11 one-slot instrument tester and recorded-flag witness. Wszystkie mają pytania i źródła. Oryginalne REV020 pozostaje bez zmian. Google Docs bezpośredni readback: źródło 1763 akapity i 156790 UTF16 znaków, kopia robocza 2116 akapitów i 226127 znaków; wszystkie 1763 źródłowe akapity dosłownie i w kolejności, siedem głównych rozdziałów. Trzy nowe nagłówki każde dokładnie raz i HEADING_2, treść/źródła obecne, intro uaktualnione. Nie wykonano kontroli drukarskiego układu PDF ani formalnego niezależnego referee.

Następny próg naukowy: rzeczywista wspólna struktura korelacji szumu maski/kanału, skończony koszt pozyskania obserwacji, minimalna legalna amplituda oraz dokładne źródło modelu. Bez tego nie wolno zmienić źródłowego PASS matematyki w decyzję o realnym eksperymencie, nowy invariant J3/K czy fizyczny wynik.

**DISPOSITION:** MATH_EXACT_SCALAR_MINIMAX / INDEPENDENT_SCOPED_CONTROLS_PASS / REV021_NATIVE_EDIT_AND_READBACK_PASS / SOURCE_OWNERSHIP_PRESERVED / REFEREE_PENDING / NO_CANON_NO_EXEC_NO_NOVELTY_NO_PHYSICAL_UPGRADE.
