# IW / M13 — ROT26: rzadki rachunek Fouriera, dokładna niezerowa granica źródłowego K_A i niezależny readback 54 norm

**RETURN_ID:** `M13-ROT26-DTC0A-SPARSE-FOURIER-EXACT-SOURCE-FAMILY-LIMIT-AND-SPECTRAL-SUPPORT-001_20261023`  
**LINEAGE:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**DATA:** 2026-10-23  
**CLASS:** samodzielna implementacja skończonej algebry modów Fouriera + dokładna arytmetyka wymierna w granicy + 54/54 źródłowych norm + porównanie pełnego tensora ze źródłowym helperem.  
**STATUS:** `FOURIER_REPLAY_PASS / EXACT_RATIONAL_SOURCE_FAMILY_LIMIT / NOT_ORIGINAL_BYTE_EXACT_RUNTIME / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / TPE HOLD`.

## 0. Stan uprzedni / zasada „others first”

* M13 ROT18–25: problem ruchomej maski, jednorodność, nieidentyfikowalność z 3 RMS, nonmap maskowanego TT, ostry ogólny limit przecieku 1/2, funkcjonalne odtworzenie 99/99 norm, współczynniki α², ilościowy bilans wstawionej projekcji.
* XH-S4 ROT019: pierwotny h=fI jest czysto śladowy, nie stanowi wejścia TT; w próbie z różniczkowaniem spektralnym i α=0 KC znika, lecz KA pozostaje niezerowy. To jest uprzednie rozdzielenie błędu stencil od wstawionej projekcji.
* INT8 ROT014: niezależny jawny racjonalny przykład *niezerowego K_A na rzeczywistym wejściu TT* w modelu ciągłym; obecne obliczenie nie jest pierwszym twierdzeniem o niezamykaniu komutatora projektowanego.
* INT8 ROT015: dokładny warunek bezaliasingowości historycznych pól dla pierwotnego spektralnego KC; autorstwo pierwszego pozytywnego certyfikatu dla tej konfiguracji należy do INT8.
* INT8 ROT016, Geeky-S10 oraz XH-S4: osobne wyniki o normach operatorowych, kompresji i nielokalności. Nie zastępujemy ich.

**Nowa różnica ROT26:** niezależny rachunek *całych* trzech residuali K_A, K_B, K_C bez siatkowego składania operatorów, pełny profil nośnika 18 przypadków i **dokładna wymierna wartość granicy RMS globalnego K_A dla dokładnie historycznych generatorów**. Wcześniejsze wyniki nie podały takiej ilościowej wartości dla tej konkretnej rodziny.

## 1. Źródło i definicje — bez podmieniania runtime

Zachowany wariant funkcjonalnie zgodny `deepseek_python_20260627_a87249.py`, SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`. Oryginalny `dtc0a_runtime_v0_3_1.py`, deklarowany SHA256 `2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084`, nadal nieudostępniony bajtowo. Odczyt `dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv`, SHA256 `1ed5dec5797ed1bc0ae9c4a924e1f18ef0a118f5602be99f03c953fd532cd66e`.

Dla torusa o długości L=2π:

- C₁=(0.05 sin x, 0.05 cos y, 0),
- C₂=(0.04 cos z, 0, 0.04 sin x),
- h=0.1 sin x cos y · I.

Ścisłe znaki, komponenty i amplitudy wynikają z podanego helpera. Rozwinięcie Fouriera `f(x)=Σ_m f̂(m)e^{i m·x}` przechowuje tylko niezerowe m∈Z³; współczynniki h, C są racjonalnymi wielokrotnościami 1 lub i.

Słownik modów implementuje osobno:

- centralną pochodną: `D_i exp(i m·x) = i sin(m_i dx)/dx exp(i m·x)`;
- E_lin: `E_α(m)=1+2α Σ_i(cos(m_i dx)−1)`;
- pochodną Liego tensora kowariantnego i dyskretny nawias generatorów jako dokładne sploty słowników modów;
- `P_TT(m)` z symbolem `I−m mᵀ/|m|²` dla m≠0 i trybem bezśladowym dla m=0.

W tym kroku **nie używa się siatki ani FFT** do konstruowania operatorów lub do uzyskania ich współczynników. Synteza odwrotną FFT pojawia się wyłącznie przy porównaniu maskowanej normy RMS z historycznymi danymi (wymaga takiego samego wycinka indeksów jak w CSV). `sympy.Rational` w osobnym skrypcie wyznacza granicę niezależnie od NumPy.

## 2. Ścisłe ograniczenie nośnika i liczbowa pełna walidacja

W dowolnym z trzech torów K, przy dwukrotnym działaniu operatorów generatorowych, wszystkie powstające częstotliwości należą do sumy nośników h, C₁, C₂. W tym źródle oznacza to

`|m_x|≤3`, `|m_y|≤2`, `|m_z|≤1`.

Filtr E, stencile i P_TT są mnożnikami Fouriera — nie poszerzają nośnika. Dla nieparzystych N≥7 cała ta rodzina jest reprezentowana bez zawijania częstości podczas zagnieżdżonych splotów, zatem dotyczy to każdej zamrożonej siatki 31..41. Wyliczony **K_A ma 32 aktywne mody** dla wszystkich 18 konfiguracji (N razy α); graniczny K_A ma również dokładnie 32 aktywne mody. K_B dla α=0 ma osiem aktywnych modów; dla α=.05,.2 ma po 28.

W pełni niezależne źródłowo wartości trzech RMS w 18 konfiguracjach (54 liczby) zostały odtworzone; największa względna różnica do danych CSV to **1.721e-14**. Kontrola całego tensora K_A (N31, α=.05) z bezpośrednim wywołaniem niezmienionego `compute_K_A_out` dała względną normę różnicy **1.310e-15**. To jest ścisła walidacja konkretnej alternatywnej semantyki helpera, lecz nie dowód byte-exact w odniesieniu do nieobecnego runtime.

## 3. Dokładna matematyczna granica źródłowego K_A

Przy stałym α i dowolnym ustalonym modzie `m`:

`sin(m_i dx)/dx → m_i`, `E_α(m)=1+2αΣ(cos(m_i dx)−1)→1` wraz z N→∞.

Cały rachunek odbywa się na **ustalonej skończonej** liczbie modów, więc granica przechodzi przez wszystkie sumy i multiplikatory TT. W przypadku α=0 otrzymujemy bezpośrednio operator z dokładnymi pochodnymi spektralnymi; dla dowolnego stałego α otrzymujemy **ten sam operator graniczny**. Nie wolno bez dodatkowych założeń przenosić tego wniosku na pole zawierające mody rosnące razem z N ani na inne E skalowane w odmienny sposób.

Symboliczny kod na liczbach wymiernych daje dokładnie

`||K_A^(∞)||_RMS,full² = 5917501 / 3499200000000000`,

`||K_A^(∞)||_RMS,full = sqrt(5917501/3499200000000000) = 4.1122999754697787e−5`.

Jeden z modów przedstawia następujący **dokładny niezerowy certyfikat**:

`K̂_A^(∞)(0,1,1) = (17/1440000) [[-2,0,0],[0,1,-1],[0,-1,1]]`.

Cztery mody `(0,±1,±1)` przenoszą **dokładnie** `2601000 / 5917501 = 43.9543651957%` całkowitej energii Fouriera K_A. Sumowanie modułów energii przebiega w pełnej przestrzeni symetrycznych tensorów z normą Frobeniusa (9 komponentów, równoważnie offdiagonal ×2), z mianownikiem 6 w definicji RMS. Nie jest to frakcja w dziedzinie **maskowanej**, gdzie mody nie są ortogonalne.

Dla α ustalonego i N→∞, K_C oraz K_B dążą do zera na tym samym pełnym nośniku, bo w granicznym różniczkowaniu spektralnym zachodzi klasyczna reprezentacja Liego; `P_TT K_C=0`. Dokładny skrypt wymierny i numeryczny rejestrują normy graniczne tych kanałów poniżej poziomu 3e−20 dla rachunku zmiennoprzecinkowego, nie interpretując tego poziomu jako fizycznego błędu.

## 4. Maska: skąd bierze się dodatkowa zmiana RMS podczas zagęszczania

Dla k=3 i α=.05 (wszystkie wiersze zgodne z pierwotnym CSV):

| N | RMS globalny K_A | RMS maskowany K_A | maskowany/globalny | energia 4 modów globalnie |
|---:|---:|---:|---:|---:|
| 31 | 4.0316888194e-05 | 3.7647568532e-05 | 0.933792 | 44.1609% |
| 33 | 4.0410842343e-05 | 3.7811453905e-05 | 0.935676 | 44.1366% |
| 35 | 4.0489315911e-05 | 3.7966257188e-05 | 0.937686 | 44.1164% |
| 37 | 4.0555525089e-05 | 3.8111313059e-05 | 0.939732 | 44.0994% |
| 39 | 4.0611893805e-05 | 3.8246626504e-05 | 0.941759 | 44.0849% |
| 41 | 4.0660276474e-05 | 3.8372562954e-05 | 0.943736 | 44.0725% |

Na N31 maskowana norma stanowi ok. 93.38% pełnej, na N41 ok. 94.37%. Przy stałym k fizyczna szerokość wyłączonego pasa wynosi `k·2π/N` i zanika, podczas gdy pola są jednostajnie gładkie, ograniczone i skończenie pasmowe. Stąd różnica między normą pełną a maskowaną zanika wraz z N; maskowana RMS z zamrożoną konwencją k=3 ma tę samą granicę co globalna. To rozstrzyga asymptotyczny limit **tej jednej** regularnej rodziny, a nie problem ogólnej estymacji rzędu operatora z ROT18.

Na tym samym źródle weryfikacja bezsiatkowych współczynników K_A dla N101, α=.2 daje `4.097670996197095e−5` globalnie, a dla N1001 `4.112150768818637e−5`. To wyliczenia z rzadkich słowników modów, bez tworzenia tablic 1001³. Nie są historycznymi wynikami DTC0a.

## 5. Prawidłowy typ wniosku

**EARNED:** konkretna bezaliasingowa i dokładnie policzalna rodzina widmowa, zgodność 54/54 RMS z CSV, niezależny bezsiatkowy rachunek operatorowy, symbolicznie dokładny iloraz wymierny dla normy granicznej, limit maskowany=globalny przy stałym k, cztery mody niosą ~43.95% globalnej energii.

**NOT EARNED:** ogólne zbieganie K_A na całej przestrzeni tensorowej, zachowanie fizycznego obserwabla w GR/NCDG, stwierdzenie o polu w podprzestrzeni TT (oryginalne h to czysty ślad), awans J3/K, oryginalny runtime v0.3.1 byte-exact, nowość klasycznej algebry Fourier/Lie/TT, niezależny referee/KN11 BW ingest, `GO_SEN_CHECK` lub `EXEC_SIGN`.

**PROBLEM_ID:** `P3_DTC0A_TT_MASK_COMMUTATION_AND_LOCAL_RMS_TYPING_001` (dalsza ilościowa analiza tego samego źródła, bez tworzenia nowego drzewa zadań).  
**Mature hosts:** klasyczne szeregi Fouriera i Parseval; standardowe rachunki reprezentacji Liego na gładkich tensorach; kompresja ortogonalnymi projektorami; INT8 ROT014/015 jako bezpośredni priorytet projektowy.  
**ROUTE_TAGS:** `IWTO_MT13 IWTO_KN11 IWTO_INT8 IWTO_XH_S4 IWTO_REC10 IWTO_LT5 IWTO_SW IWTO_MODERATOR`.  
**STOP:** `NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / TPE HOLD`.

## 6. Reprodukowalność i identyfikatory plików

- `verify_m13_rot26.py`: bezsiatkowy rachunek sparse FFT coefficient dictionaries, NumPy; SHA256 `b58d55227c2da54b51868d57d613bad7deb9bacc4d58badcd49db75e2da741b2`.
- `verify_m13_rot26_exact.py`: niezależny symboliczny dokładny rachunek SymPy; SHA256 `afdb0d8a60222769474333b84aa81f9ce952758e7b64d5a06c4fdb80ea8401c3`.
- `IW_M13_ROT26_sparse_fourier_spectrum_20261023.json`: 18 pełnych rekordów i normy, nośniki i dominanty; SHA256 `72fb185d30e6a86631c5532e8f7d60bb5ee73f576d86545748daec963c517206`.
- `deepseek_python_20260627_a87249.py`: tylko kontrola bezpośredniego historycznie dopasowanego helpera, SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`.
- `dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv`: historyczne 54 normy, SHA256 `1ed5dec5797ed1bc0ae9c4a924e1f18ef0a118f5602be99f03c953fd532cd66e`.

Publikacja raportu nie implikuje pobrania do BW ani akceptacji naukowej przez właściciela.