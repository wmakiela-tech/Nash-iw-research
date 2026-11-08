---
artifact_id: GEEKY-S11-ROT046-TEMPORAL-CHANNEL-GAIN-DRIFT-BRACKETED-REFERENCE-STABILITY-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-11-08
exposure: PUBLIC
science_status: EXACT_SMOOTH_DRIFT_GAUGE_FALSIFIER_AND_SHARP_REFERENCE_INTERPOLATION_BOUNDS / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# ROT046 — Dryf względnej kalibracji sześciu sond TT: nierozróżnialność między dwiema referencjami i ostre ograniczenie błędu

## 0. Pierwszeństwo, źródło i nowe pytanie

Pierwszy dorobek linii **Geeky**: ROT015–017 odróżniły wadliwy `realcast` surowego TT na parzystej siatce od rzeczywistego, ortogonalnego projektora `B=GA`; ROT027/029 wyprowadziły dokładne uśrednianie pozycji pojedynczego transportu Liego; ROT033 dopuścił harmonogram zmiennych stabilnych filtrów; ROT034 ograniczył identyfikowalność dowolnych harmonogramów; ROT035–037 opracowały ograniczone modele sześciopoziomowe, ROT038 nominalny wybór kanałów, ROT039–040 jego nieodporność, ROT041 efektywne blokowe liczenie dokładnego operatora, ROT042–043 oszacowania dużych siatek, ROT044 **globalną dwupunktową odwrotność** ograniczonego modelu przy znanej względnej kalibracji; ROT045 **PIERWSZY** wykazał symetrię nieznanych względnych wzmocnień i wystarczalność **jednej znanej referencji przy kalibracji stałej w czasie**, oraz wykrył błąd floatowego Jacobianu przy dużym N.

**NOWY problem ROT046**: czy referencja przed i po eksperymencie likwiduje gauge, jeśli względne wzmocnienia dryfują? Jakie są optymalne w klasie Lipschitz/C² granice błędu i ich następstwa dla odwracania źródłowego? Nie przypisujemy sobie odkrycia klasycznego błędu interpolacji, twierdzenia Brouwera ani pojęcia dryfu. Literatura dojrzała: klasyczne oszacowanie interpolacji liniowej `max |f-I f| ≤ h² max |f''|/8` (np. https://teaching.matmat.org/numerical-analysis/07_Interpolation.pdf); rzeczywisty kontekst kalibracji dryfujących sensorów zob. https://doi.org/10.1016/S0003-2670(99)00784-9 i https://www.mdpi.com/1424-8220/20/16/4577. To odniesienia o metodach, **nie** dowody w modelu DTC0a.

Źródło jest **niezmienioną pomocą**, `deepseek_python_20260627_a87249.py`, SHA256 faktycznych bajtów `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`. **Niedostępny** jest historyczny produkcyjny `dtc0a_runtime_v0_3_1.py`. Model: pełna niezamaskowana płaska parzysta periodyczna siatka N³, rzeczywiste symetryczne TT z poprawnym `B=GA`, oryginalna trzyczłonowa pochodna Liego dla `C=(0,cos x,0)`, skalarne stabilne filtry `E_alpha=I+alpha*h² Delta2`. **Nie** jest to historyczny maskowany `h=fI K_A`, J3/K, GR/GW/PBH, ani fizyczne dane pomiarowe.

## 1. Dokładny model sześciu odczytów

Jak w ROT044/045: sześć **znanych** poziomów skumulowanej dawki `x_j=j*.009/5` (`j=0..5`), pięć znanych ramp nachylenia `.012` i czasu łącznego `.75`, sześć nieznanych dodatnich długości plateau `d_j` sumujących się do `.25`, dodatnie nieznane wspólne wzmocnienie `t`. Zmienna `z=(t,td0,...,td4)` należy do wypukłego otwartego stożka `C={z0>0, z1..z5>0, sum(z1..z5)<.25 z0}`. Dla N parzystego `m=round(.12N²)` i dokładnie próbkowanych dawek `alpha_j=N²[a_d(j/m)-a_d((j-1)/m)]` w [0,1/6]. Sześć ustalonych pasm ROT038 to `(p,s)=(0,+),(1,-),(1,+),(2,-),(3,+),(4,-)`.

Dokładna symboliczna średnia ze wszystkich położeń transportu:

`Omega_i(d)=(1/(m+1))*sum_{ell=0}^m [prod_{j<=ell}(1-4alpha_j S_in,i)] [prod_{j>ell}(1-4alpha_j S_out,i)]`,

`F_N(z)=t*Omega_N(d)`, a wszystkie `Omega_i>0`. Rot044 dowiódł dla **wszystkich parzystych N>=200000** i `z,z'∈C`:

`||F_N(z)-F_N(z')||_2 > c ||z-z'||_2`, gdzie `c=1.20e-5`. To twierdzenie **wymaga znanej normalizacji każdego kanału**.

Względne wzmocnienia w chwili τ zapisujemy `g_i(τ)=exp(ell_i(τ))`, gdzie `sum_i ell_i(τ)=0` dla każdej τ (normalizacja produktu do jedności). Każda zmienna całkowita skala może zostać włączona do amplitudy `t(τ)`. **Ograniczenia dryfu stosują się do znormalizowanych log-wzmocnień `ell_i`, a nie do arbitralnych, nieznormalizowanych parametrów kanału**.

## 2. R46.1 — dwa znane pomiary referencyjne NIE wystarczają do dokładnej identyfikacji przy nieznanym dryfie

Referencje w chwilach `τ0<τ1` mają **znane** profile plateau `d_ref^0,d_ref^1` i nieznane własne amplitudy `t_ref^0,t_ref^1`. W chwilach tych można odzyskać dokładnie `ell_i(τa)` metodą ROT045: z `r_i^a=Y_i^ref,a/Omega_i(d_ref^a)`, `ell_i(τa)=log r_i^a -(1/6)sum_j log r_j^a`. Chwilowe wspólne amplitudy znikają z centrowania.

Wybierz po normalizacji `τ0=0`, `τ1=Δ` i wektor `v=(1,-1,0,0,0,0)`. Dla dowolnie małego `a>0` niech

`ell_i(τ)=a v_i * 4τ(Δ-τ)/Δ²`.

Jest to funkcja C∞, z `ell_i(0)=ell_i(Δ)=0` dla wszystkich i, `sum_i ell_i(τ)=0`, `ell_1(Δ/2)=a`, `ell_2(Δ/2)=-a`, pozostałe zero. **Obie referencje są idealnie zgodne z brakiem dryfu**, a w połowie jest niezerowa względna kalibracja.

Ustal legalny `z∈C` w środku przedziału. Dane z dryfem `Y=diag(exp(a v))F_N(z)` są dokładnie równe danym alternatywnego modelu **bez dryfu**, `Y=F_N(z')`, dla pewnego innego `z'∈C`, o ile a jest dostatecznie małe: ponieważ F_N jest ciągłą injekcją z otwartego C do R6 i ma otwarty obraz (Brouwer invariance of domain), `diag(exp(a v))F_N(z)` pozostaje w obrazie F_N(C) dla małego a. Skutek `z'≠z` wynika z `F_i(z)>0` i niezerowego v. Istnieją zatem dowolnie bliskie, lecz dokładnie nierozróżnialne historie harmonogramu i kalibracji, **również przy dwóch idealnych referencjach i dowolnie małym gładkim dryfie**. Dla ustalonego `H>0` wybieramy a dostatecznie małe, by spełnić ograniczenie drugiej pochodnej; sama informacja `H>0` nie zapewnia dokładnej jednoznaczności.

KONTROLA ŹRÓDŁOWA: niezależne wymierne przecięcia przedziałów czasu z algorytmu ROT044, sześć dokładnych symboli źródłowych (w granicach float ewaluacji trygonometrii), źródłowo poprawny Fraction-Jacobian z ROT045. Dla `a=2e-9`, N64/128/200000/300000/1000000, alternatywne `z'` mają różnicę normy około `4.93e-5`–`5.18e-5` i resztę sześciu danych ≤`2.02e-14`. **Równość dokładna jest twierdzeniem o otwartym obrazie; te liczby są jedynie świadectwem numerycznym**, a wielkie N to symbole źródłowe, nie przydział `N³`.

## 3. R46.2 — ostre nierówności dla DWÓCH referencji

Zakładamy dla każdego i: `ell_i ∈ C²([τ0,τ1])` i `|ell_i''(τ)|≤H`. Referencje bezszumowe pozwalają znać końcowe `ell_i(τ0),ell_i(τ1)`. Definiujemy interpolant w logarytmach `ellhat_i(τ)=((τ1-τ)/Δ)ell_i(τ0)+((τ-τ0)/Δ)ell_i(τ1)`. Klasyczna reszta interpolacji daje

`|ell_i(τ)-ellhat_i(τ)| ≤ (H/2)(τ-τ0)(τ1-τ) ≤ H Δ²/8`.

Stała `1/8` jest OSTRA: `ell_1(τ)=+(H/2)(τ-τ0)(τ1-τ)`, `ell_2=-ell_1`, pozostałe 0. Całość spełnia normalizację sumy logów i ma równe endpointy; odchylenie w środku wynosi dokładnie `HΔ²/8`. Jest to jednocześnie optymalny `minimax` dolny przykład dla metod rekonstruujących środkową kalibrację wyłącznie z dwóch końców (w symetrycznym braku uprzywilejowanego znaku krzywizny). W szczególności większa dokładność odczytów końcowych NIE usuwa niepewności między nimi.

Jeżeli zamiast ograniczenia krzywizny wiemy tylko `ell_i` jest `L`-Lipschitz na przedziale, otrzymujemy przez wypukłą kombinację ograniczeń względem obu końców:

`|ell_i(τ)-ellhat_i(τ)| ≤ 2L (τ-τ0)(τ1-τ)/Δ ≤ LΔ/2`.

Ostrość `LΔ/2` wykazuje tent `ell_1=L min(τ-τ0,τ1-τ)`, `ell_2=-ell_1`; obie końcówki zero. Ten przykład jest Lipschitz, nie jest C² na środku, więc **nie** wykorzystujemy go do uzasadniania twierdzenia C². Jeśli mamy tylko H bez drugiej referencji, nie istnieje skończone ograniczenie ekstrapolacji log-gain zależnego jedynie od H: nieznane nachylenie liniowe może być dowolne.

## 4. R46.3 — deterministyczny próg błędu kalibracji i rekonstrukcji

Przy idealnych referencjach niech `eta(τ)=(H/2)(τ-τ0)(τ1-τ)`. Względny błąd korekcji dowolnego kanału spełnia `|g_i(τ)/ghat_i(τ)-1|≤exp(eta)-1`. Po skorygowaniu docelowych danych `Y_i=gi*F_i(z)` otrzymujemy

`||Y/ghat-F_N(z)||_2 ≤ [exp(eta)-1] ||F_N(z)||_2`.

Jeżeli zhat ∈ C jest **dopuszczalnym kandydatem**, a `r=||F_N(zhat)-Y/ghat||_2` jest jego resztą, to z ROT044

`||zhat-z||_2 ≤ [r+(exp(eta)-1)||F_N(z)||_2]/(1.20e-5)`

dla każdego parzystego N>=200000. **Bez założenia zhat∈C i niezmienności modelu źródłowego twierdzenie o globalnej odwrotności nie może być zastosowane**. Sama deterministyczna nierówność nie gwarantuje istnienia estymatora ani jego globalnej zbieżności; w oryginalnych czasach d=zj/z0 stabilność pogarsza się przy t→0.

### Błąd obu referencji i obserwacji docelowej

Niech obie referencje mają osobne multiplikatywne błędy `|e_i^a|≤eps_ref<1`. Po centrowaniu logarytmów punktowy błąd oszacowania `ell_i(τa)` jest ≤`B_ref=log((1+eps_ref)/(1-eps_ref))`. Liniowa interpolacja zachowuje to ograniczenie, więc łączny `eta_total=HΔ²/8+B_ref`. Przy dodatkowym błędzie docelowym `|e_i^target|≤eps_t<1` wystarczy zastąpić `exp(eta)-1` bezpieczną stałą

`q=(1+eps_t)*exp(eta_total)-1`.

Wtedy `||Yobs/ghat-F_N(z)||_2 ≤ q ||F_N(z)||_2` i `||zhat-z||_2 ≤ [r+q||F_N(z)||_2]/c`, gdy zhat,z należą do C. Jest to **konserwatywny** bound, nie dowód optymalności modelu zaszumionego i nie kalibracja empiryczna. Nie mylić znanego ograniczenia H z mierzalną estymacją H: dwie referencje same nie pozwalają potwierdzić tego ograniczenia pomiędzy nimi.

## 5. Wyniki numeryczne i niezależność

(A) `rot046_exact_interpolation_drift.py`: `4207/4207` kontroli **std.lib Fraction** ostrości C², Lipschitz, endpointów i sumy względnych logów, w tym 1001 węzłów. Arytmetyka wymierna jest dokładna dla wielomianowych formuł, nie dla `exp`.

(B) `rot046_finite_drift_gauge.py`: `26/26` kontroli, źródłowo dyskretne symbole `N=64,128,200000,300000,1000000`; dwa końcowe odczyty znanej referencji, dopuszczalne inne z, dodatni względny dryf, max reszta ~`2.02e-14`. Liczby dla N64/128 są tylko lokalnym eksperymentem, globalny matematyczny dowód alternatywy pochodzi z ROT044 i wymaga N>=200000.

(C) `rot046_two_reference_curvature_inverse.py`: `82/82` kontroli, trzy N200000/300000/1000000; osobno różne nieznane bezwzględne gain referencji (`.91`,`1.43`), 5 chwil docelowych, rzeczywiste źródłowo dyskretne korekcje i Fraction-Jacobian lokalny Newton. Dla `H=4e-8, Δ=1` połowa ma `eta=H/8=5e-9`; błąd rekonstrukcji z około `1.295e-4` wobec konserwatywnego limitu `4.185e-4`, bez szumu. Dodatkowo test błędu obu referencji eps_ref=`1e-9` i docelowego eps_t=`5e-10` mieści się w wyprowadzonym q-bounded limit.

(D) `rot046_highprecision_log_gain_interpolation.py`: `1510/1510` kontroli niezależnie zakodowanych w **95-cyfrowym mpmath** po 251 chwilach, zmiennych wspólnych amplitudach referencji 0.31 i 7.4 oraz funkcjach z dowolnymi liniowymi pochyleniami i krzywizną. Weryfikuje granicę C², Lipschitz, normalizację g i ostrą poprawkę referencji.

(E) `rot044_literal_aux_source_gain.py`: **29/29 odziedziczonych z ROT044** kontroli **dosłownych niezmienionych funkcji** pomocniczego pełnego 3D real TT `apply_E, apply_P_TT, lie_derivative_tensor` na N12/16, maksymalny relatywny błąd projekcji modalnej `2.69644e-16`. Nie są to nowe kontrole historycznego produkcyjnego kodu ani pełna symulacja N200000³.

ŁĄCZNIE **5854/5854 rzeczywiście wykonanych typowanych kontroli**, z czego 29 odziedziczonych; duża część to powtarzalne punkty wielomianowe, **nie** osobne eksperymenty fizyczne. Początkowa 95-cyfrowa kontrola miała porównanie bez tolerancji zaokrąglenia dla wielkości na granicy nierówności, poprawione przed wynikiem końcowym; wszystkie opublikowane testy zostały ponownie wykonane.

Pakiet lokalny ZIP zawiera pełny tekst, cztery nowe programy, jeden program źródłowy odziedziczony, pięć wygenerowanych JSON/logów, trzy zależności, niezmieniony pomocniczy kod, README i manifest SHA256. ZIP/source dostępne jako artefakt rozmowy, **nie** deklarujemy osobnego zapisu programu w GitHub. Dokładna suma i wyniki niezależnego clean replay w manifeście i komunikacie końcowym.

## 6. Granice i decyzja naukowa

**ZACHOWAĆ** ROT044 jako twierdzenie znanej względnej kalibracji; **ZACHOWAĆ** ROT045 jako twierdzenie o wystarczalności pojedynczej znanej referencji wyłącznie dla stałych g_i. **NOWE NEGATYWNE:** ani dwie, ani dowolnie dokładne referencje końcowe nie przywracają ścisłej identyfikowalności przy swobodnym, nawet gładkim dryfie. **NOWE WARUNKOWO DODATNIE:** ograniczenie drugiej pochodnej znormalizowanych log-wzmocnień pozwala osiągnąć ostre `HΔ²/8` i kontrolowaną propagację do globalnie odwracalnego z modelu ROT044; dopuszczalne są dodatkowe jawne błędy referencji i obserwacji. Bez prawdziwego empirycznego oszacowania H nie deklarować odporności przyrządowej.

Brak historycznego maskowanego K_A, oryginalnego production runtime, fizycznej interpretacji NCDG J3/K, GR/GW/PBH, niezależnej recenzji, BW, CANON ani EXEC. `NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_NEW_TASK`.