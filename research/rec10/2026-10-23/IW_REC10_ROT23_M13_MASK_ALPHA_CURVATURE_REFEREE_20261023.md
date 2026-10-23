# IW/NASH — REC10 ROT23
## Audyt M13 ROT27: ścisły współczynnik maski, estymator dwóch siatek i różnica kwadratowa filtru α

**Data:** 2026-10-23  
**Komórka:** `IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10`  
**Problem:** `P3_DTC0A_TT_MASK_COMMUTATION_AND_LOCAL_RMS_TYPING_001`  
**Werdykt:** `PASS_WITH_PARAMETER_DIFFERENCE_STRENGTHENING`  
**Klasa:** `SOURCE_TYPED_MATURE_ANALYTIC_ASYMPTOTICS / INDEPENDENT_RATIONAL_AND_CSV_REPRODUCTION`  
**Granica upoważnienia:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_J3_K_INVARIANT / NO_NEW_TASK`.

## 1. Materiał pierwotny i granice dowodowe

1. M13 ROT27, `research/m13/2026-10-23/IW_M13_ROT27_mask_vs_stencil_exact_asymptotics_001.md`, odczytany Git blob `71c130f9f73ca73033bffbef8142b56696f229ee`.
2. Przekazany historyczny CSV `dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv`, SHA256 `1ed5dec5797ed1bc0ae9c4a924e1f18ef0a118f5602be99f03c953fd532cd66e`: 18 wierszy dla N=31,33,35,37,39,41 i α=0,.05,.2.
3. Dostępny zachowany wariant źródłowego helpera `deepseek_python_20260627_a87249.py`, SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`, bezpośrednio skontrolowane definicje `apply_E`, `apply_T`, `compute_K_A_out`, `rms_norm` i trzech pól testowych.
4. Deklarowany historyczny produkcyjny `dtc0a_runtime_v0_3_1.py` o SHA256 `2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084` pozostaje bajtowo **niedostępny**. Odtworzenie współczynników źródłowego helpera NIE jest odtworzeniem oryginalnego wykonania.

**Odjęcie wcześniejszych osiągnięć:** M13 jest pierwotnym autorem dokładnego współczynnika maski i wielomianów α dla zanikania kanałów K_B, K_C. W ROT23 REC10 weryfikuje te liczby i dodaje (i) dwusiatkowy estymator usuwający maskę oraz (ii) niezależny test *drugiej różnicy α*, dla której można udowodnić skalowanie O(N⁻⁴), inaczej niż dla surowych RMS. Nie ma twierdzenia o matematycznej nowości.

## 2. Niezależne sprawdzenie twierdzenia M13

Dla rodziny `C1=(.05sin x,.05cos y,0)`, `C2=(.04cos z,0,.04sin x)` i h=.1sin x cos y I, stałej indeksowej maski `k=3` oraz RMS pola `||K_A||²_F/6`, M13 podał dokładne wartości pełnej energii G i trzech średnich powierzchniowych S_j:

```
G  = 5917501/3499200000000000
Sx = 761233367/314928000000000000
Sy = 1409179/656100000000000
Sz = 123982963/62985600000000000
```

Ich niezależna arytmetyka wymierna daje

\[
A=\sqrt G=4.11229997546977870875\cdot 10^{-5},
\quad b=3\frac{3G-S_x-S_y-S_z}{G}
=\boxed{-\frac{229914416}{88762515}}=-2.5902197115527878\ldots
\]

Ponieważ `S_j/G = (1.42934467138, 1.27006676185, 1.16399513729)`, każdy odcinany pas brzegowy ma ponadprzeciętną energię. Zatem przy **stałym α**

\[
R_N(\alpha):=\operatorname{RMS}_{\rm mask}K_A(N,\alpha)
=A\left(1+\frac bN\right)+O_\alpha(N^{-2}).\tag{23.1}
\]

Dowód w M13 ROT27 jest poprawnie ograniczony do skończonych modów bez aliasingu, stałej maski w liczbie węzłów i ustalonego α. Niezależne sprawdzenie arytmetyki `G,S_j` daje **PASS**. Źródłowo historyczne `R_N` odczytano z CSV, nie wygenerowano ponownie starym nieobecnym runnerem.

## 3. NOWY estymator dwóch rozdzielczości: usunięcie 1/N bez znajomości b

Jeżeli dla ustalonego α zachodzi pełne rozwinięcie skończonych modów

\[
R_N(\alpha)=A+\frac{bA}{N}+\frac{c(\alpha)}{N^2}+O_\alpha(N^{-3}),
\]

wówczas dla **dowolnych** nieparzystych N<M o porównywalnej skali (M/N ograniczone i odsunięte od 1) definiujemy

\[
\widehat A_{N,M}(\alpha)=\frac{M R_M(\alpha)-N R_N(\alpha)}{M-N}.
\]

Ścisła algebra daje

\[
\boxed{\widehat A_{N,M}(\alpha)=A-\frac{c(\alpha)}{MN}+O_\alpha(N^{-3}).}\tag{23.2}
\]

Estymator usuwa wiodącą maskową poprawkę `1/N` **bez wprowadzania dokładnego b do algorytmu**. Dla historycznych N=31,41 obliczenia z CSV dają:

| α | oryginalny R_41 | estymator (31,41) | błąd estymatora względem dokładnego A |
|---:|---:|---:|---:|
| 0 | 3.850893700760329e−5 | 4.044221919409512e−5 | −1.65547% |
| .05 | 3.837256295424907e−5 | 4.062004566296200e−5 | −1.22305% |
| .20 | 3.796755716372291e−5 | 4.113055507156207e−5 | +0.01837% |

**NEGATIVE KNOWLEDGE:** przypadkowo bardzo trafny wynik przy α=.20 nie jest świadectwem małego błędu dla każdego α. Zgodnie z warunkowym wzorem (23.2) pozostają poprawki zależne od α, a N31–41 są umiarkowanymi siatkami. Estymator nie jest certyfikatem dokładności oryginalnego kodu ani ciągłej fizyki.

## 4. NOWE twierdzenie: druga różnica parametru α jest rzędu N⁻⁴

To druga, odrębna kontrola, której nie uzyskujemy ze zwykłego nachylenia surowych RMS. Dla zachowanego helpera `E_{α,h}=I+α h²Δ_h` jest dokładnie liniowe w α. W `compute_K_A_out` występują co najwyżej **dwa** zastosowania `apply_T(C,F)=Lie_C(E_{α,h}F)`, a `P` jest niezależne od α. Zatem pole tensorowe `K_A(N,α)` jest wielomianem w α stopnia najwyżej dwa.

Na tej JEDNEJ skończeniepasmowej rodzinie źródeł przy N→∞, z `h=2π/N`, dla α na dowolnym ustalonym zwartym przedziale I mamy jednolicie

\[
\partial_\alpha K_A(N,\alpha)=O_I(h^2),
\quad \partial_\alpha^2 K_A(N,\alpha)=O_I(h^4),
\quad R_N(\alpha)\to A>0.
\]

Suma po masce jest liniowa w kwadracie normy pola; maska NIE zależy od α. Różniczkując `R=\sqrt{\langle K,K\rangle_{\rm mask}}`, przy R oddzielonym od zera otrzymujemy

\[
\partial_\alpha^2R_N=
\frac{\langle\partial_\alpha K,\partial_\alpha K\rangle+\langle K,\partial_\alpha^2K\rangle}{R_N}
-\frac{\langle K,\partial_\alpha K\rangle^2}{R_N^3}
=O_I(h^4).
\]

Nie potrzeba tutaj znać b ani obliczać dokładnego współczynnika kwadratowego. Dla trzech ustalonych α0<α1<α2 zastosujmy twierdzenie o wartości średniej do sąsiednich ilorazów różnicowych. Otrzymujemy

\[
D_N=\frac{R_N(\alpha_2)-R_N(\alpha_1)}{\alpha_2-\alpha_1}
-\frac{R_N(\alpha_1)-R_N(\alpha_0)}{\alpha_1-\alpha_0},
\quad
\boxed{|D_N|\le(\alpha_2-\alpha_0)\sup_{\alpha\in I}|R_N''(\alpha)|=O_I(N^{-4}).}\tag{23.3}
\]

Jest to **test krzywizny α**, a nie pomiar błędu siatki per se. Także gdy `K_A` jako pole ma niezerową granicę i maska wnosi 1/N, kombinacja (23.3) eliminuje te wspólne składniki i część pierwszej poprawki operatora zależnej liniowo od α.

**Independent historical data check** dla (α0,α1,α2)=(0,.05,.2):

| N | D_N | N⁴ D_N |
|--:|--:|--:|
| 31 | 8.569271634479e−8 | 0.079139023091 |
| 33 | 6.655164783098e−8 | 0.078924996747 |
| 35 | 5.239458956883e−8 | 0.078624630972 |
| 37 | 4.176741034712e−8 | 0.078278851544 |
| 39 | 3.367875129427e−8 | 0.077913804073 |
| 41 | 2.744246357676e−8 | 0.077545843319 |

Zmienność `N⁴D_N` na całej szóstce to około 2.06%, podczas gdy samo `D_N` spada trzykrotnie. To **zgodność danych z dowodem skali**, nie estymator dokładnej stałej granicznej: sześć N nie wystarcza do numerycznego certyfikowania asymptotycznego współczynnika.

## 5. Reprodukcja i zakres źródłowy

Program `IW_REC10_ROT23_DTC0A_MASK_ALPHA_DIFFERENCE_REPRO_20261023.py` korzysta wyłącznie ze standardowej biblioteki Pythona i z **niezmienionej kopii** przekazanego pierwotnie pliku CSV. Sprawdza SHA256 danych, dokładną arytmetykę `Fraction(G,S_j)`, wszystkie 18 odczytów RMS, kontrolę poprawki maskowej, trzy estymatory dwóch siatek, sześć wartości D_N oraz ich skalowanie przez N⁴. Wykonanie: **PASS**.

**Typy źródeł:** CSV to historyczna warstwa obserwacji liczbowych; dostępny helper to weryfikator matematyczny; produkcyjny runner nie jest dostępny bajtowo. Żadnego oryginalnego wielkiego przebiegu N=10001 ani oryginalnego runtime'u v0.3.1 nie wykonano w tym obrocie.

## 6. Prior art, ograniczenia i dyspozycja

Obie nowe techniki są standardowe w analizie numerycznej: dwusiatkowe usunięcie członu brzegowego jest odmianą ekstrapolacji Richardsona, a kasowanie współczynnika liniowego parametru przez jego drugą różnicę jest elementarną analizą parametryczną. To NIE jest nowa ogólna teoria operatorów, dowód równoważności J3/K ani fizycznego niezmiennika.

Wynik M13 ROT27: **PASS w dokładnym nośniku matematycznym**. Nowa kontrola REC10 ROT23: **PASS** jako źródłowo przypisany test `1/N` kontra `N^-2` i `N^-4` dla stałego α oraz historycznych pól.

Nie wolno przenosić wzorów na maskę o stałej *fizycznej* grubości, α(N) rosnące z N, dowolne niegładkie pola, zmieniającą się metrykę Yorka, stałe obszary fizyczne, ani z nich wnioskować o fizycznym K_A, J3 czy K.

**Owner:** M13 (dane i źródłowa rodzina DTC), XH-S4 (metryczne P_g), LT5/INT8/PRF11 (teoria), KN11 (BW), Moderator (EXEC). `SOURCE_REVIEW != OWNER_ADOPTION != BW_INGEST != EXEC`.

`NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_TASK / BW_PENDING`.