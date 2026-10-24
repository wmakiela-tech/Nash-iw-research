# LT5 — ROT19: dokładny promień informacji na klasie dopuszczalnej i niestabilność odwracania bez kalibracji amplitudy

**RETURN_ID:** LT5-REV021-ROT19-ADMISSIBLE_CLASS_MINIMAX_RADIUS_PROJECTIVE_NOISE_INTERVAL_SOURCE_GATE-001_20261024
**Date:** 2026-10-24
**Author:** LT5, Żywa Teoria NASH
**State:** MATHEMATICAL_PROOF / LOCAL_2000_NUMERIC_CONTROLS_PASS / NATIVE_WORKING_REV021_EDITED / REFEREE_PENDING / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.

**Natywna robocza REV021:** https://docs.google.com/document/d/15b-8uK2DZVScU6k-K6eesL8d8nt777-UmalEUb5U-zE/edit
**Oryginalna REV020 nietknięta:** https://docs.google.com/document/d/1cn97_kO65BcJRRWQrvrL9fKlEYBT3PHg6BJItn1Q4FQ/edit

## 1. Nauka innych komórek i dojrzały gospodarz

KN11 24 X podał kryterium dopuszczalnych różnic: dla liniowych obserwacji L i celu T na rzeczywistym nośniku V, jednoznaczność T na A względem L zachodzi wtedy i tylko wtedy, gdy T znika na (A−A)∩ker L. Odmienny NC ART030 dotyczy zawężenia rzeczywistej klasy profilów reakcji, a nie zaprzeczenia kryterium MT13 na całej L1.
https://github.com/wmakiela-tech/Nash-iw-research/blob/6f873189653bc030b8d171f4fbecf9067ac7cebb/research/kn11/2026-10-24/iw_kn11_rot20261024_restricted_difference_sufficiency_projective_noise_and_negative_source_scope_001.md

MT13 24 X uzyskał dokładny próg rozróżnienia przy jednym nieznanym dodatnim wspólnym wzmocnieniu i błędzie bezwzględnym, uzupełniony testem reszty trzeciego kanału. To nie jest nowy wynik LT5.
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/2026-10-24/mt13_xh_q88_m13_rot32_projective_noise_calibration_overidentification_001.md

M13 ROT033 rzeczywiście poszerzył ROT032: ujemność współczynników Bernsteina i dodatniość RMS są TERAZ objęte zewnętrznie zaokrąglonymi przedziałami liczonymi z trygonometrycznych formuł ZACHOWANEGO HELPERA, nie tylko ze spisanych wielomianów dziesiętnych. Wszystkie 10 źródłowych konfiguracji PASS; minimalne modułowe pochodne log(A/C) >= 0.8648869093985175. Nie odzyskano bajtowo oryginalnego historycznego dtc0a_runtime_v0_3_1.py.
https://github.com/wmakiela-tech/Nash-iw-research/blob/ed6e8857e63b47786b58acfeb589135c1128e08d/research/m13/2026-10-24/IW_M13_ROT33_DTC0a_directed_interval_Bernstein_monotonicity_001.md

Geeky-S11 ROT010 dowiódł niestabilności szachownicowej symetrii TT dla arbitralnie małej domieszki standardowego schematu w rodzinie czwartego rzędu. Autor źródła wykonał 200 kontroli FFT, nie LT5.
https://github.com/wmakiela-tech/Nash-iw-research/blob/e9df6b00387eb64e52b7a3a8e43b5467abbff5f7/research/geeky-s11/2026-10-24/geeky_s11_rot010_mixed_stencil_nyquist_ghost_instability_001.md

LT5 rozwija matematykę rosnącej informacji w znanej klasie **optimal recovery / information-based complexity**, bez przypisywania pierwszeństwa: Micchelli i Rivlin; Ettehad i Foucart, SIAM/ASA UQ, DOI 10.1137/20M1328476; Milanese i Vicino (1993), DOI 10.1006/jcom.1993.1028. Bez hipotez o dowolnym nowym prawie fizycznym.
https://epubs.siam.org/doi/10.1137/20M1328476
https://usiena-air.unisi.it/handle/11365/8938

## 2. Dokładny skalarno-celowy promień informacji dla dowolnej klasy A

Niech A będzie niepustym, niekoniecznie wypukłym ani liniowym zbiorem dopuszczalnych źródeł. Niech L:A→W będzie dowolną mapą obserwacji do rzeczywistej przestrzeni unormowanej W, T:A→R będzie ograniczonym rzeczywistym celem, a dopuszczalny szum addytywny spełnia ||e||≤eta. Estymator phi jest dowolną funkcją rzeczywistą obserwacji y=L(a)+e. Wtedy:

R*(eta) = inf_phi sup_(a∈A, ||e||≤eta) |T(a)−phi(L(a)+e)|
       = (1/2) sup_{a,b∈A; ||L(a)−L(b)||≤2eta} |T(a)−T(b)|.   (R19.1)

Dowód: dla każdego możliwego y włókno A_y={a∈A:||L(a)−y||≤eta} definiuje zbiór możliwych wartości T(A_y). Estymator równy środkowi przedziału od inf T(A_y) do sup T(A_y) ma najmniejszy możliwy lokalny błąd, równy połowie średnicy celu. Gdy a,b należą do tego samego A_y, nierówność trójkąta daje ||L(a)−L(b)||≤2eta. Odwrotnie, dla dowolnej takiej pary y=[L(a)+L(b)]/2 należy jednocześnie do obu kul o promieniu eta. Zatem supremum warunkowych średnic i supremum po parach są równe. Nie trzeba zwartego A ani osiągania supremum. Dla y z pustym włóknem estymator jest arbitralny. QED.

Ograniczenia: RZECZYWISTY cel skalarny, normowa centralna kula addytywnego błędu, dowolny dopuszczalny estymator; nie jest to wynik o ryzyku Bayesowskim, wariancji Gaussa ani o dowolnym celu wektorowym. Dla równobocznego trójkąta wektorowych celów połowa średnicy jest mniejsza od promienia Czebyszewa.

Przy eta=0 otrzymujemy dokładnie wystarczalność celu: L(a)=L(b) => T(a)=T(b). Dla liniowych L,T na A⊂V jest to zapis KN11 dotyczący (A−A)∩ker L. Dla symetrycznej euklidesowej kuli A={||a||≤R}, liniowego L=Ca i T=m^T a, każda para (a,b) redukuje się do v=(a−b)/2 z ||v||≤R, ||Cv||≤eta; odwrotnie para (+v,−v) zawsze istnieje. Stąd dokładnie PIERWSZA postać pierwotnego Twierdzenia 7.9 Żywej Teorii:
R* = max_{||v||≤R, ||Cv||≤eta} |m^T v|.
Nie przenosić jego drugiej dualnej formuły ani optymalności liniowego estymatora na dowolne niekonweksyjne A.

## 3. Ścisły kontrprzykład amplitudowy

Model A={(alpha,s):0≤alpha≤1,s>0}, L(alpha,s)=s(1,1+alpha), T(alpha,s)=alpha. Przy eta=0 pierwszy kanał równy s>0, a ratio drugiego do pierwszego =1+alpha, więc odwrócenie parametru jest dokładne; R*(0)=0.

Jednakże dla KAŻDEGO eta>0 i KAŻDEGO alpha można dobrać tak małe dodatnie s, że ||s(1,1+alpha)||≤eta. Wówczas TEN SAM odczyt y=0 jest zgodny z pełnym przedziałem alpha∈[0,1]. Dokładne ryzyko wynosi R*(eta)=1/2, bo górną granicę osiąga estymator alpha_hat=1/2. Jest to nieciągłość jednostajnego ryzyka dla eta zbliżającego się do zera, mimo doskonałej identyfikowalności bez szumu. Zbieżność źródła do zera jest skrajnym falsyfikatorem zapewnień o odporności. Nie zaprzecza M13 ROT033 przy osobnym modelu błędu WZGLĘDNEGO i wspólnej kalibracji.

W modelu MT13 y=s f(alpha)+e, dla ustalonego prawdziwego s0 oraz alternatywnej s1>0 i f0,f1∈R² o dodatnich składowych minimalna odległość po dopasowaniu s1 wynosi
d=s0 sqrt(||f0||²−(f0·f1)²/||f1||²)=s0 |det(f0,f1)|/||f1||.
Kule błędu eta są rozłączne dokładnie przy d>2eta. Jeśli s0 może zaniknąć, żaden jednostajny dodatni próg eta nie chroni wszystkich wartości alpha. Jeśli oba kanały mają OSOBNE nieznane wzmocnienia, nawet zerowy błąd nie usuwa degeneracji. Właściwie zaprojektowany trzeci kanał może badać niezgodność źródłowego modelu po profilowaniu alpha,s przez residual >eta, co jest innym kontraktem.

Dla M13 helpera ROT033 przy niezależnych WZGLĘDNYCH mnożnikach w obu odczytach z tolerancją eps<1, legalnym wspólnym gain s i zawężeniu alpha∈[0,.2] otrzymujemy osobno:
|alpha_hat−alpha|≤log[(1+eps)/(1−eps)]/0.8648869093985175.
Dla eps=.005 jest to 0.011562301644. Błędy ABSOLUTNE skali N-independent prowadzą do uwarunkowania Θ(N²) w ROT032. Brak fizycznie skalibrowanego rozkładu szumu i legalności wspólnej amplitudy wyklucza wniosek obserwacyjny o realnym K_A, GR lub astronomii.

## 4. Niezależne kontrole rachunkowe LT5

Niezależnie wykonany Python/NumPy z seed 20261024:
- niekonweksyjna siedmiopunktowa klasa A, 12 dozwolonych par przy eta=.11; połówka największej różnicy celu=1.2, a bezpośrednia maksymalna średnica obserwowanych włókien /2 też 1.2.
- 1D kulowy szczególny przypadek oryginalnego Twierdzenia 7.9: R=2, c=1.5, m=2, eta=.3, ryzyko .4.
- tysiąc wartości alpha∈[0,1], s dodatnie i dowolnie małe, wspólne y=0 legalne przy eta=10^-6.
- 2000 losowych par dodatnich wektorów źródła i s0; min odległość profilowana vs formuła wyznacznikowa, maksymalny absolutny błąd w double ~2.84217e−14; wspólny odczyt w środku przy eta=d/2.
- ilustracja trójkąta wektorowego o boku 2 i promieniu 2/sqrt(3)>1.
- arytmetyczna kontrola nowej względnej granicy M13: 0.011562301644197274.
Wszystkie ograniczone kontrole PASS. Nie zastępują ogólnego dowodu, recenzji innej komórki, automatycznego dowodu prawdy źródłowych operatorów lub fizycznej aparatury.

Weryfikowalny kod LT5:
https://github.com/wmakiela-tech/Nash-iw-research/blob/8db91966553111f9a65b7d299945a23c1caed3a0/research/lt5/2026-10-24/reproduce_lt5_rot19_admissible_class_information_radius.py

## 5. Faktyczna integracja i integralność żywej monografii

W natywnej roboczej REV021 dodano §7.5d z Twierdzeniem 7.9a, pełnym dowodem, związkiem z wcześniejszym 7.9, kontrprzykładem braku dolnego s i pytaniem badawczym 7-P5. W §4.11e usunięto przestarzałe zastrzeżenie źródłowe wobec M13 i dodano prawdziwy, uwarunkowany status ROT033. W istniejącym §4.11d dodano wymaganą niestabilność mieszania stencilów z ROT010; jego dodatnia/ujemna klasa TT pozostaje dopasowana do własnego symbolu i generator zależy od N. Zaktualizowano wstępną notę REV021 o §7.5d.

Bezpośredni Google Docs READBACK:
- REV020 oryginał 1763 akapity / 156790 UTF16 znaków; niezmieniony.
- REV021 robocza 2058 akapitów / 214896 UTF16 znaków; wszystkie 1763 oryginalne akapity dosłownie i w zachowanej kolejności; 7 głównych rozdziałów.
- dokładnie jeden nagłówek §7.5d HEADING_2, dotychczasowe §4.11d/e nadal jednoznaczne HEADING_2; stare zdanie o braku certyfikatu przedziałowego już nie występuje; Geeky ROT010 obecny, frontnote zawiera §7.5d.
- Weryfikacja dotyczy TEKSTU i struktury akapitów, nie układu stron PDF ani ewentualnej recenzji niezależnej.

## 6. Otwarte pytania i STOP

Pierwszy nowy test decyzyjny dla rzeczywistego źródła musi deklarować dopuszczalny zbiór A, minimalną amplitudę, strukturę wzmocnień, miarę błędu i typ obserwabli. Należy wyliczyć źródłowo właściwą średnicę docelowych włókien, a nie tylko potwierdzić, że parametry można bez szumu odwrócić. Pytanie 7-P5 dotyczy najtańszego legalnego projektu kanałów, który zapewni wyznaczony promień minimaksowy i niezależne falsyfikatory złej rodziny źródeł.

Status: ścisła matematyka klasycznego optimal recovery i priorytety komórek zachowane; nie ma nowej fizyki, K/J3, ekskluzywnego twierdzenia matematycznego, wyroku dla PBH, historii produkcyjnej DTC ani zatwierdzenia publikacji.

**DISPOSITION:** NEW_NATIVE_CH7_THEOREM_BRIDGE_PASS / M13_DIRECTED_INTERVAL_SOURCE_STATUS_CORRECTED / GEEKY_GHOST_INSTABILITY_INTEGRATED / INDEPENDENT_SPOTCHECK_PASS / REV021_PRESERVED / REFEREE_PENDING / NO_CANON_NO_EXEC_NO_NOVELTY_NO_PHYSICAL_UPGRADE.
