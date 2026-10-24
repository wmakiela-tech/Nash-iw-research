# IW / M13 — ROT34: identyfikowalność parametru DTC0a z dwóch masek jednego kanału i ścisły test odporności

**RETURN_ID:** `M13-ROT34-DTC0A-SOURCE-MATCHED-SINGLE-CHANNEL-MULTIMASK-PROJECTIVE-IDENTIFIABILITY-001_20261024`  
**PROBLEM_ID:** `P3_DTC0A_TT_MASK_COMMUTATION_AND_LOCAL_RMS_TYPING_001`  
**DATE:** 2026-10-24  
**CELL:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**CLASS:** `SOURCE-OPERATOR DIRECTED INTERVAL / MASK-RATIO PROJECTIVE IDENTIFIABILITY / HISTORICAL DATA REPLAY / BOUNDED NOISE COUNTERCONTROL`  
**GATES:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / TPE HOLD / NO_NEW_TASK`

## 1. Dlaczego wykonano obrót; subtraction

- ROT29–31: bez znajomości konkretnego generatora nawet pięć maskowanych norm RMS nie identyfikuje normy pełnej siatki, w tym przy rzeczywistych 3D polach TT o paśmie 1. Te twierdzenia pozostają ważne.
- ROT32: **dwa różne kanały** (A,C) i jeden wspólny dodatni gain pozwalają odwrócić `alpha` na [0,0.2] dla zadeklarowanego źródła; wykazano zwrot A/B, uwarunkowanie `N²` wobec absolutnego błędu.
- ROT33: bezpośredni *source formula interval certificate* dla A/C, już nie tylko dla wielomianów zaokrąglonych dziesiętnie.
- MT13 z 2026-10-24 (`MT13-XH-Q88-M13-ROT32-PROJECTIVE-QUOTIENT-NOISE-DISCRIMINATOR-001`): matematyczna geometria nieznanego gain, ostre projektowe odległości i overidentification trzecim kanałem to **wcześniejszy dorobek MT13**. Nie przypisujemy go M13/ROT34.
- Geeky-S11, INT8, PRF11 i XH-S4: odrębne twierdzenia o stencilach, projektorach TT, nielokalności i geometrii. ROT34 nie przypisuje im nowych twierdzeń o fizyce.

**Nowy test:** Czy *dwa pomiary tego samego kanału na różnie szerokich maskach* zastępują dwa kanały? Które pary masek są odwracalne, które mają punkt zwrotny? Czy po odwróceniu istnieje użyteczna certyfikowana odporność na szum?

## 2. Źródło, domena i model

Utrzymujemy zamrożone pola generatorów

```
C1 = (0.05*sin x, 0.05*cos y, 0)
C2 = (0.04*cos z, 0, 0.04*sin x)
h  = 0.1*sin x*cos y * I
```

oraz N=41, L=2*pi, centralny stencil rzędu drugiego, `E_lin=I+alpha*dx²Delta_N`, spektralny projektor Fourier-TT i maski `k=2,3,4,5,6`. Dla kanału j i maski k oznaczamy

\[
 g_{j,k}(\alpha)=\operatorname{RMS}_{j,k}(\alpha)^2,
\quad R_{j;k_1,k_2}(\alpha)=\sqrt{g_{j,k_1}(\alpha)/g_{j,k_2}(\alpha)}.
\]

Dane obserwowane mają postać `y_k=s*sqrt(g_j,k(alpha))` dla **jednego wspólnego nieznanego gain s>0 na obie maski**, stałego N, źródła, konfiguracji filtrów i skali RMS. Stąd `y_k1/y_k2=R` usuwa gain. Jeśli R jest ściśle monotoniczna w alpha∈[0,.2], odzyskujemy alpha i następnie s. Przy oddzielnych nieznanych gain na każdą maskę identyfikacja się nie utrzymuje; należy jawnie określić model kalibracyjny.

**Ważne:** surowe h jest czystym śladem, więc ambient K_A(h) nie jest Lie-komutatorem ograniczonym od początku do domeny TT. Fizyczny K/J3/TPE ani continuum nie są wnioskiem.

## 3. Certyfikat znaków i jego zakres

Dla każdej pary masek `k1<k2` i trzech kanałów liczymy z rzadkiego modelu modowego U,V,W, a następnie kwartyki `g1, g2` z zachowaniem **arytmetyki przedziałowej** (`mpmath.iv`, 45 cyfr), obejmującej źródłową trygonometrię stencilu, filtr E, Fourier-TT i skończoną sumę okna. Tworzymy

\[
 p(\alpha)=g_1'(\alpha)g_2(\alpha)-g_1(\alpha)g_2'(\alpha).
\]

Bernsteinowskie przedziałowe współczynniki `p` w całym `[0,1/5]` dają znaki `UP` (wszystkie ściśle dodatnie) i `DOWN` (wszystkie ściśle ujemne). Dolne granice wszystkich współczynników Bernsteina `g1,g2` są dodatnie. Dla pozostałych przypadków bezpośrednie przedziałowe wartości `p(0)` i `p(1/5)` mają przeciwne ściśle rozdzielone znaki. Z ciągłości funkcji i twierdzenia Darboux wynikają punkty zwrotne, a więc brak globalnej iniektywności `R`.

**Wynik całej klasyfikacji — 30/30 rozstrzygniętych par:**

| Kanał | Ściśle rosnących | Ściśle malejących | Certyfikowane punkty zwrotne |
|---|---:|---:|---:|
| K_A | 10 | 0 | 0 |
| K_B | 1 | 0 | 9 |
| K_C | 1 | 6 | 3 |
| **Łącznie** | **12** | **6** | **12** |

Wszystkie **12 punktów zwrotnych** mają **przeciwne znaki pochodnej na końcach przedziału**, a nie są tylko nierozstrzygniętymi znakami współczynników Bernsteina.

## 4. Konkretne pary i certyfikaty czułości

Dla monotonicznych par podzielono przedział alpha na 80 fragmentów. Przedziałowe obliczenie Hornerem `p/(2g1*g2)` na każdym podprzedziale daje dodatnią dolną granicę na `|d log R/dalpha|` (nie tylko niezerowość pochodnej):

| Para | Monotoniczność | Dolna certyfikowana czułość | Łączna zmiana `log R` od 0 do 0.2 | Gwarancja `|delta alpha|`, eps=.005 |
|---|---|---:|---:|---:|
| A:2/3 | wzrost | 0.000869734 | +0.000181560 | 11.4979 (bezużyteczne ponad zakresem) |
| A:2/6 | wzrost | 0.003011839 | +0.000615674 | 3.3203 (bezużyteczne ponad zakresem) |
| B:2/3 | zwrot | — | — | brak globalnej gwarancji |
| B:5/6 | wzrost | 0.012994969 | +0.030873469 | 0.7695 (ponad zakresem) |
| C:2/3 | spadek | 0.035473406 | −0.015488005 | 0.2819 (ponad zakresem) |
| **C:2/4** | **spadek** | **0.056593174** | **−0.022223247** | **0.17670** |

`C:2/4` jest najlepszą monotoniczną parą w ocenianym zestawie według tej **konserwatywnej, certyfikowanej dolnej granicy czułości**. Nie jest bezwarunkowo optymalna dla nieznanej macierzy kowariancji błędu. Są to maski N41 w jednym określonym modelu źródłowym; pięć masek nie zostało potraktowanych jako niezależne próby pomiarowe.

Przy względnych błędach `y_k -> y_k(1+eta_k)`, `|eta_k|<=eps`, zachodzi

\[
 |\widehat\alpha-\alpha| \le \frac{\log\bigl((1+\epsilon)/(1-\epsilon)\bigr)}{c},\quad c\le \inf_\alpha |d\log R/d\alpha|,
\]

gdzie wynik należy obciąć do rzeczywistego przedziału długości 0.2. Dla `eps=.005` i `C:2/4` dostajemy 0.176701..., podczas gdy ROT33 daje 0.011562... przy dwóch **różnych kanałach A,C**. Mniejsza korelacja masek ani taka sama precyzja eksperymentalna nie zostały założone.

## 5. Jawna demonstracja utraty rozróżnialności przy szumie

Metoda ostrego minimalnego dopasowania z jednym gain jest standardową geometrią dwóch dodatnich wektorów odczytów (przyznany priorytet MT13). Niech obserwacja pochodzi z alpha=.05, s=1 i niech model alternatywny ma alpha=.10. Po wyborze najlepszego skalowania alternatywnego `s'=2/(t1+t2)`, gdzie `ti=RMS_ki(.10)/RMS_ki(.05)`, najmniejszy maksymalny bezwzględny błąd **względny** odczytów to `epsilon* = |t1-t2|/(t1+t2)`.

| Para | Najlepszy wspólny `s'` | Najmniejszy maks. błąd względny |
|---|---:|---:|
| A:2/6 | 1.0035802 | 0.007736% |
| B:5/6 | 0.6241224 | 0.445395% |
| C:2/4 | 0.7548260 | 0.346694% |
| C:2/3 | 0.7556095 | 0.243257% |

Wszystkie cztery różne parametry alpha=.05 i .10 **mogą zostać pomylone** przy dopuszczonym błędzie ±0.5% każdego maskowanego odczytu i wolnym wspólnym gain. Dowód jest konstruktywny: wspólne `s'` i oba błędy zostały zapisane w maszynowym JSON. To nie jest szum zaobserwowany w realnym eksperymencie.

## 6. Niezależne źródłowe kontrole, limitation, bez nowych twierdzeń o fizyce

1. 30/30 przedziałowo certyfikowanych par; 18 monotonicznych, 12 z podpisanym punktem zwrotnym, wszystkie domknięte bez sampling-only weryfikacji. 45/45 zamrożonych odczytów `N41 × k2..6 × alpha0,.05,.2 × A,B,C` odpowiada generowanemu źródłowemu modelowi, max wzgl. różnica `2.89e-15`.
2. **Niezmieniony** `deepseek_python_20260627_a87249.py`: off-grid `alpha=.113`, N41, k2/k4, A/C: **4/4 PASS**, maks. różnica wobec prognozy quartic ROT32 `1.56e-15`.
3. Osobny skrypt analizuje profilowanie gain wyłącznie na utrwalonych wielomianach ROT32; nie jest niezależną walidacją produkcyjnego runtime. Brak niezależnej kalibracji instrumentalnej lub danych zewnętrznych.
4. Warunkowość ścisłości: `mpmath.iv` przy poprawnych wzorach stencilu i projekcji. Certyfikat nie jest formalnym dowodem w proof assistant; nie odtwarza bajtowo historycznego `dtc0a_runtime_v0_3_1.py` (deklarowany SHA256 `2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084`). Alternatywny, funkcjonalnie dopasowany helper SHA256 `23b0ec865263c5688682425af9d4c1f9dcb9f1d582a0f2f33d99c642c176f801` pozostaje użytym źródłem.
5. Nie mieszamy iniektywności alpha dla znanego C1,C2,h z nieidentyfikowalnością dowolnych TT z ROT31. Nie ma automatycznej stabilności przy błędach absolutnych N→infinity, rozdzielonych gainach ani nieznanym stencilu. Brak wykazanego fizycznego GR/GW/J3/K/TPE endpointu.
6. Brak niezależnej recenzji, potwierdzonej integracji BW, podpisu owner/EXEC, nowości fizycznej lub dodatkowego zadania moderatora.

## 7. Odtwarzalność

Samodzielny `verify_m13_rot34_interval.py` (`mpmath.iv`) generuje plik `IW_M13_ROT34_one_channel_mask_ratio_certificates_20261024.json`, czytając zaimportowane źródłowe funkcje `verify_m13_rot33_interval.py` i historyczny plik maski. `verify_m13_rot34_native.py` wykorzystuje niezmieniony helper i wcześniej archiwalne współczynniki ROT32. `verify_m13_rot34_noise.py` jest odrębną kontrolą kinematyki gain/noise z pliku JSON ROT32. ZIP zawiera pełne zależności, frozen CSV, źródłowy helper, raport i sumy SHA256; można go rozpakować do pustego katalogu i wykonać trzy programy bez dostępu do wcześniejszego wątku.