---
artifact_id: IW_GEEKY_S12_ROT005_M13_B_FIXED_DELTA001_GLOBAL_NEAREST_ENDPOINT_BERNSTEIN_CERTIFICATE_001_20261112
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
date: 2026-11-12
exposure: PUBLIC
result_class: SOURCE_TYPED_EXACT_GLOBAL_FIXED_DELTA_POSITIVE_CLOSURE / PRIOR_ART_AND_NEGATIVE_KNOWLEDGE_PRESERVING
science_status: AUTHOR_EXACT_RATIONAL_INTERVAL_CERTIFICATE_AND_PINNED_CODE_REEXEC_PASS / REFEREE_PENDING / OWNER_ADOPTION_PENDING
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: M13_FROZEN_FUNCTIONALLY_MATCHED_N41_B_SOURCE_COEFFICIENTS_ONLY / DELTA_EXACT_1_100 / NO_HISTORIC_PRODUCER / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT005 — dokładny certyfikat minimum globalnego pięciu masek w kanale B przy delta=0,01

## 0. Rozstrzygnięcie w jednym twierdzeniu

Dla pięciomaskowego profilu kanału B źródłowo dopasowanego generatora pomocniczego DTC0a w rozdzielczości N=41, z jedną wspólną dodatnią amplitudą energii i z wagami rozłącznych powłok M13, przy dokładnie ustalonej separacji delta=1/100 zachodzi:

Dla każdego alpha∈[0,1/5] globalny minimizator profilowanego D_B²(alpha,beta) na zbiorze
{beta∈[0,1/5]: |beta-alpha|≥1/100}
należy do zbioru NAJBLIŻSZYCH dopuszczalnych alternatyw:
{alpha-1/100,alpha+1/100}∩[0,1/5].

W szczególności żadna dalej położona beta nie poprawia ścisłego minimum wyznaczonego przez legalną najbliższą granicę; przy równości po obu stronach oba punkty są minimizatorami. Dowód ma zakres kwantyfikatorów ALL-alpha, ale dokładnie JEDNA DELTA=0,01.

Jest to mocne rozstrzygnięcie osobnego przypadku B pozostawionego OPEN przez M13 ROT39/ROT40, a NIE sprzeczność z Geeky-S12 ROT004, który obalił uniwersalną zasadę dla INNEJ delta=0,035. Różnica kwantyfikatorów jest nośna: FIXED DELTA POSITIVE / ALL DELTA FALSE.

## 1. Pierwszeństwo, źródło i dojrzały host

Oryginalna praca M13 ROT32–40:
- ROT32/33: źródłowa geometria parametru, widma i maski;
- ROT35: algebra rozłącznych powłok i kowariancji;
- ROT37/38: certyfikowane punkty źródłowe;
- ROT39: dokładne porównanie TYLKO beta=alpha±0,01 i jedna zmiana strony dla kanału B przy alpha_B≈0,03265254963589545;
- ROT40: źródłowy dwuwymiarowy dowód radialny dla kanałów A/C przy każdej delta, ale faktyczny brak monotoniczności radialnej B i wyraźny HOLD w kwestii jego minimum globalnego.

Oryginalne raporty M13:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-25/IW_M13_ROT39_full5_nearest_alternative_side_switch_001.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/27188018c1dbbcee81d391ceb8ba5c55237cff7e/research/m13/2026-10-26/IW_M13_ROT40_universal_AC_radial_mask_global_argmin_001.md

Geeky-S12 ROT004 FIRST wystawił ścisły kontrprzykład dla B i delta=0,035, alpha=0,039; beta=0,001 leży dalej niż oba najbliższe legalne punkty, a ma niższą odległość niż oba. Ten kontrprzykład jest RETAINED:
https://github.com/wmakiela-tech/Nash-iw-research/blob/a8f0497a8bff36d4d63b1cd8fa90f326e0673380/research/geeky-s12/2026-11-11/IW_GEEKY_S12_ROT004_M13_SOURCE_B_NON_NEAREST_GLOBAL_MINIMIZER_FALSIFIER_001_20261111.md

Źródłowa liczba danych dla ROT005: oryginalny publiczny plik M13 direct_B.json, Git blob SHA-1 a6f50fbe5904e580e84c87ee87c5ad043cdec5d0, 25 współczynników kwartyk z rzeczywistymi skierowanymi końcami przedziałów:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json

Dane dotyczą N=41, C1=(0,05sin x,0,05cos y,0), C2=(0,04cos z,0,0,04sin x), ambientowego czystośladowego h=0,1sin x cos y I, drugiego centralnego stencilu, filtru E_lin oraz płaskiego projektora Fourier TT. To są WSPÓŁCZYNNIKI MODELU FUNKCJONALNIE DOPASOWANEGO, nie brakującego bajtowo historycznego dtc0a_runtime_v0_3_1.py. Nie regenerowano 45-cyfrowej oryginalnej analizy Fourier M13; wykonano nowy dokładny dowód z jej zamrożonych przedziałów.

Matematyczny host: klasyczna geometria projekcji na prostą przy jednym dodatnim wzmocnieniu, identyczność Gram/wedge, pochodna ilorazu i dokładna dodatniość wielomianu przez współczynniki Bernsteina. No mathematical novelty asserted.

## 2. Właściwa funkcja i faktoryzacja pochodnej

Pięć masek k=2..6 ma n_k=(41-2k)^3 voxeli oraz wagi powłok:
w=(7778,6938,6146,5402,24389).

Niech g_k(t)=RMS_mask(K_B(t))². Są to wielomiany stopnia co najwyżej 4 z dokładnymi przedziałami współczynników. Niech s_i(t) będą średnimi energiami rozłącznych powłok:
s_i(t)=[n_i*g_i(t)-n_(i+1)*g_(i+1)(t)]/w_i dla i=2..5 oraz s_6(t)=g_6(t).

Dla a=s(alpha), b=s(beta), W=diag(w), p=<a,b>_W, q=<b,b>_W:
D_B²(alpha,beta)=min_{u>0} ||a-u*b||_W²
                =||a||_W²-p²/q
                =N(alpha,beta)/q(beta),
N(alpha,beta)=SUM_(i<j) w_i*w_j*(a_i*b_j-a_j*b_i)^2.

**Dodatniość wejścia:** pięć oryginalnych wielomianów s_i jest ściśle dodatnich na [0,0,2]. Udowodniono to ponownie przez dokładne dolne współczynniki Bernsteina na całym przedziale, bez próbkowania. W konsekwencji q>0 i p>0; optimum wspólnego dodatniego wzmocnienia ma legalną wartość u=p/q>0.

Pochodna:
partial_beta D_B²= -(p/q²)*H,
H=2*(partial_beta p)*q-p*(partial_beta q).
Dla każdego profilu wielomianowego H(alpha,alpha)=0. Zatem istnieje wielomian P z dokładną tożsamością
H=(alpha-beta)*P.

ROT005 buduje P wprost z par składowych:
Q_ij(alpha,beta)=[s_i(alpha)s_j(beta)-s_j(alpha)s_i(beta)]/(alpha-beta)
oraz R_ij(beta)=s_i'(beta)s_j(beta)-s_i(beta)s_j'(beta).

Tożsamość:
P(alpha,beta)=2*SUM_(i<j) w_i*w_j*Q_ij(alpha,beta)*R_ij(beta).

Dzielenie przez alpha-beta nie jest obliczeniem numerycznym; Q_ij powstaje z antysymetrycznych par monomów a^m b^n-a^n b^m, z dokładnym wzorem sumy geometrycznej. Dlatego P ma stopień najwyżej 3 w alpha i 9 w beta; wszystkie operacje są wymierne.

Gdy P>0:
- po LEWEJ stronie beta<alpha pochodna D² jest UJEMNA (im bliżej alpha, tym lepiej);
- po PRAWEJ beta>alpha pochodna D² jest DODATNIA.

## 3. Sześć dodatnich certyfikatów na oryginalnych przedziałach

Każdy dziesiętny koniec skierowanego przedziału M13 został odczytany jako dokładny ułamek o liczniku i mianowniku BigInt; użyto działań przedziałowych z uwzględnieniem znaków, rozwiązań dodatnich mianowników i dokładnej transformacji do bazy Bernsteina. Podane niżej liczby są jedynie czytelnymi przybliżeniami DODATNICH dolnych granic; znaki ustalono bez float.

Wszystkie wielomiany s_i są dodatnie na [0,0,2]. Dla pozostałych wielomianów uzyskano:

| Test | Dokładna dziedzina | Dolna granica współczynnika Bernsteina (przybliżenie) |
|---|---|---:|
| P, prostokąt 1 | alpha∈[0,0,1], beta∈[0,01,0,105] | +2150,933367 |
| P, prostokąt 2 | alpha∈[0,0,1], beta∈[0,105,0,2] | +1317636,713894 |
| P, prostokąt 3 | alpha∈[0,1,0,2], beta∈[0,01,0,2] | +30311,100082 |
| P, mała beta | alpha∈[0,0,028], beta∈[0,0,01] | +310,210199 |
| partial_beta P, mała beta | alpha∈[0,028,0,2], beta∈[0,0,01] | +38348,396469 |
| F0, jedna zmienna | alpha∈[0,028,0,2] | +244,727006 |

Wszystkie sześć testów: EXACT RATIONAL INTERVAL BERNSTEIN PASS. Pierwsze trzy prostokąty dokładnie pokrywają [0,0,2]×[0,01,0,2]. Liczby na tej tablicy używają normalizacji wejściowych energii powłok przez pomnożenie przez 10^12, wyłącznie dla wygody arytmetyki; nie są błędami eksperymentalnymi ani fizycznymi progami.

Dodatkowe pięć certyfikatów dodatniości energii powłok na [0,0,2] ma dolne granice (po wejściowej normalizacji) odpowiednio:
0,009861818352; 0,013090462973; 0,018239007512; 0,024583138646; 0,033356545541.

## 4. Dlaczego dokładnie te znaki wystarczają na CAŁĄ dziedzinę

Podział alpha przy a_c=7/250=0,028.

**Przypadek I: alpha≤0,028.**
Dla beta∈[0,0,01] P>0 (test 4); dla beta∈[0,01,0,2] P>0 (testy 1–3). Zatem P>0 na CAŁYM możliwym zakresie beta. D² ściśle maleje w kierunku alpha z lewej i ściśle rośnie na prawo. Wszelkie alternatywy odległe co najmniej delta=0,01 są nie lepsze niż najbliższe dopuszczalne beta=alpha±0,01.

**Przypadek II: alpha≥0,028.**
Dla beta≥0,01 analogiczna radialna monotoniczność wynika z testów 1–3. Trzeba sprawdzić TYLKO mały wyjątkowy fragment beta∈[0,0,01].

Test 5 mówi, że partial_beta P>0 dla alpha≥0,028 i beta∈[0,0,01]. Ponieważ w tym obszarze beta<alpha, a znak pochodnej D² to znak MINUS P, przejście znaku P może być wyłącznie z MINUS na PLUS. Zatem D² w tym fragmencie może mieć najwyżej jedno **MAKSIMUM**, lecz żadnego wewnętrznego minimum. Jego minimum na domkniętym przedziale musi leżeć w beta=0 albo beta=0,01.

Porównanie beta=0,01 z najbliższą LEWĄ alternatywą beta_L=alpha-0,01:
dla alpha≥0,028 zachodzi beta_L≥0,018>0,01, więc radialna monotoniczność w beta≥0,01 daje
D²(alpha,0,01)>D²(alpha,alpha-0,01).

Pozostaje beta=0. Niech q(t)=||s(t)||_W² i N(alpha,beta) oznacza numerator wedge z §2. Niech
F0(alpha)=N(alpha,0)*q(alpha-0,01)-N(alpha,alpha-0,01)*q(0).
To JEDNOWYMIAROWY wielomian stopnia co najwyżej 16, z dokładnym dzieleniem różnicowym do obliczenia N(alpha,alpha-0,01) bez odejmowania zbliżonych wartości. Test 6 dowodzi F0>0 na alpha∈[0,028,0,2]. Ponieważ oba mianowniki q są dodatnie,
D²(alpha,0)>D²(alpha,alpha-0,01).

Obydwa końce [0,0,01] są więc ściśle GORSZE niż beta_L; każdy punkt wewnętrzny także, bo D² nie może tam mieć minimum. Poza tym fragmentem monotoniczność daje najbliższe punkty po obu stronach. Razem dowodzi to globalnego twierdzenia dla każdego alpha.

## 5. Konsekwencja do M13 ROT39 — pełna mapa globalnej strony B

M13 ROT39 FIRST certyfikował porównanie dwóch najbliższych punktów dla kanału B i delta=0,01, wraz z jedynym pierwiastkiem przełącznika:

alpha_B≈0,03265254963589545,
z dokładną wymierną izolacją podaną w M13 ROT39.

DOPIERO ROT005 dowodzi, że TO PORÓWNANIE jest wystarczające dla minimum globalnego. Kombinacja dwóch osobnych wyników, bez przepisywania pierwszeństwa M13, daje:

- alpha∈[0,0,01): jedyna najbliższa dopuszczalna strona PRAWA;
- alpha∈[0,01,alpha_B): strona LEWA jest globalnie bliższą alternatywą;
- alpha=alpha_B: obie strony równoważne;
- alpha∈(alpha_B,0,19]: strona PRAWA jest globalnie bliższa;
- alpha∈(0,19,0,2]: jedyna najbliższa dopuszczalna strona LEWA.

To jest mapa geometrii hipotetycznego źródłowego PROFILU, nie zmierzona mapa czułości fizycznej. Sam globalny certyfikat ROT005 nie przenosi automatycznie dowodu M13 ROT39 na inny generator.

## 6. Kod, reprodukcja, kontroli i granice wnioskowania

PUBLIC kod stdlib Node.js, zamrożony na ORYGINALNYM source-Git-blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0 (SHA-1 Git blob sprawdzany przed odczytem):
https://github.com/wmakiela-tech/Nash-iw-research/blob/0e2fe52e64d382df2c9ec1fa93ebe0a00d6fd8c2/research/geeky-s12/2026-11-12/iw_geeky_s12_rot005_exact_B_delta001_interval_bernstein_certifier.js

Uruchomienie z Node >=18:
node iw_geeky_s12_rot005_exact_B_delta001_interval_bernstein_certifier.js
albo offline z drugim argumentem będącym dokładnym oryginalnym direct_B.json.

Kod oblicza wszystkie dziewięć (sześć głównych + pięć powłok, łącznie jedenaście) decyzji znaku matematycznie na ułamkach wymiernych; aproksymacje numeryczne wylicza wyłącznie do wypisania człowiekowi. W rzeczywistym autorskim wykonaniu wszystkie znaki PASS. Po GitHub WRITE wykonano odczyt identycznej zawartości źródłowej (PASS), a następnie PONOWNIE WYKONANO publiczny fragment funkcji certificate po pobraniu dokładnych bajtów opublikowanego pliku i ponownym pobraniu wejścia M13 — wszystkie znaki PASS i te same wyniki. Nie twierdzimy, że wykonano całą Node osłonę sieciową po pobraniu; jej funkcja dowodowa została jednak faktycznie ponownie wykonana z opublikowanych bajtów.

PUBLIC maszynowo czytelne wyniki, readback PASS:
https://github.com/wmakiela-tech/Nash-iw-research/blob/15007ac901fe61f251de70ef3ab78c5e3670b676/research/geeky-s12/2026-11-12/IW_GEEKY_S12_ROT005_M13_B_DELTA001_CERTIFICATE_RESULTS_001_20261112.json

**NIE ZMIENIAMY:**
1. M13 A/C wszystkie-delta PASS; B wszystkie-delta FAIL na mocy ROT004;
2. B dokładnie delta=0,01 ma DOWÓD pozytywny z niniejszego raportu, a nie tylko gęsty skan;
3. Oryginalny producent historyczny dtc0a_runtime_v0_3_1.py nie został odzyskany w postaci byte-exact. Zgodność pochodzenia współczynników M13 jest wejściem warunkowym;
4. Użyte źródło jest syntetyczną klasą modelu pomocniczego ze stałym nieznanym współczynnikiem energii; pięć masek nie jest zbiorem niezależnych pomiarów RMS, a żadna rzeczywista kowariancja szumu nie jest przyjęta jako pomiar;
5. Nie wynika nowy K/J3, teoria grawitacji, wynik NCDG, pomiar Eöt-Wash, fizyczna interpretacja, kanon czy wykonanie eksperymentu;
6. Matematyka: klasyczne dokładne wielomiany/transformacje Bernsteina. NO_NOVELTY;
7. Niezależny referee i M14 owner adoption wymagają osobnych działań/werdyktów. POSTED i source-local RUN nie są I3 akceptacją.

**RECOMMENDED BOUNDED REVIEW:** REC11 lub AUD1 niezależnie pobiera trzy PINNED publiczne bajty źródłowe (M13 direct_B, ROT005 code/results) i sprawdza definicje Q_ij,R_ij,P, wyjątkowy monotoniczny znak beta i ścisły cert F0. M14 następnie może zmienić status dziedziczonego szczególnego pytania B delta=.01 z OPEN do matematycznie rozstrzygniętego (jeśli audyt przyjęty). Nie jest to dyspozycja wykonawcza dla pozostałych komórek.

## 7. Status i przechowywanie

Full-body public GitHub report, reproducible public code and result JSON are separate artifacts with exact pinned readback. Source firstness M13 retained. Cross-surface BW owner KN13 ingest pending; Slack message when delivered is transport only; independent referee and M14 science owner adoption pending. No new task cascade, no protected private science bytes copied into public.

FINAL:
B_DELTA_0P01_ALL_ALPHA_NEAREST_ENDPOINT_PASS_EXACT_RATIONAL_INTERVAL_CERTIFICATE /
B_ALL_DELTA_FAIL_ROT004_RETAINED /
M13_ROT39_SIDE_SWITCH_NOW_GLOBAL_CONDITIONAL_COROLLARY /
SOURCE_M13_FROZEN_FUNCTIONAL_COEFFICIENTS_ONLY /
HISTORIC_PRODUCER_HOLD /
REFEREE_PENDING / OWNER_ADOPTION_PENDING / BW_PENDING /
NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
