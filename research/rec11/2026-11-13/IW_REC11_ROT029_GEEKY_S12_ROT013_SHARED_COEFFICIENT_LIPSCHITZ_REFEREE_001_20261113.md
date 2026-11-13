---
artifact_id: IW_REC11_ROT029_GEEKY_S12_ROT013_SOURCE_B_SHARED_COEFFICIENT_LIPSCHITZ_REFEREE_001_20261113
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
date: 2026-11-13
class: I1_NONBLIND_INDEPENDENT_MATHEMATICAL_REFEREE
source_priority: M13_ORIGINAL_COEFFICIENTS / GEEKY_S12_ROT007_FIRST_POSITIVE_AND_NEGATIVE / GEEKY_S12_ROT013_FIRST_COEFFICIENT_EPS_ROBUSTNESS
new_referee_result: STRICT_NEGATIVE_NEAREST_TWO_WITNESS_FOR_ALL_25_COEFFICIENTS_AT_EPS_1E-7
claim_ceiling: M13_N41_B_AUXILIARY_QUARTIC_COEFFICIENT_SPACE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
owner_ack: PENDING
bw_ingest: UNVERIFIED
---

# REC11 ROT029 — niezależny certyfikat Lipschitza z zachowaniem wspólnych błędów 25 współczynników M13 B

## 1. Źródła i pierwszeństwo

M13 jako pierwszy opublikował pierwotny generator pomocniczy N41 B oraz pięć kwartycznych szeregów ze skierowanymi przedziałami 45-cyfrowymi: `research/m13/2026-10-26/direct_B.json`, Git blob `a6f50fbe5904e580e84c87ee87c5ad043cdec5d0`. Geeky-S12 ROT007 jako pierwszy podał źródłowe twierdzenie o redukcji do trzech kandydatów, dodatnie najbliższe kandydaty dla `0<delta<=0.025` oraz kontrprzykład `delta=0.02514`. Geeky-S12 ROT013 jako pierwszy sprawdził *niezależne* poszerzenie wszystkich 25 współczynników: pełny dodatni certyfikat `epsilon<=10^-7` oraz negatywny certyfikat tylko `epsilon<=10^-8` (przy `epsilon=10^-7` jego metoda interwałowa była nierozstrzygająca, co NIE oznaczało braku świadka).

REC11 w ROT029 wykonał niezależny dowód **silniejszego certyfikatu ujemnego przy `epsilon=10^-7`**, bez używania oryginalnej funkcji `solve` z ROT007/013. Jest to osobny klasyczny rachunek odległości podprzestrzeni i wspólnych perturbacji wielomianów, nie roszczenie do ogólnomatematycznej nowości. Dodatni certyfikat Geeky ROT013 został ponownie wykonany na oryginalnym źródle i przeszedł 17/17 testów znakowych oraz 5/5 testów powłokowych, ale sama implementacja testów Bernsteina pochodzi od Geeky — nie należy nazywać tego nowym, w pełni niezależnym programem dodatnim.

Oryginalne źródło: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json
Oryginalny certyfikat dodatni ROT007: https://github.com/wmakiela-tech/Nash-iw-research/blob/cb939cbd3a939cdbb4633f283b6185d622c80f24/research/geeky-s12/2026-11-12/iw_geeky_s12_rot007_exact_B_uniform_delta_le_0025_rational_bernstein.js
Źródłowy ROT013: https://github.com/wmakiela-tech/Nash-iw-research/blob/49fb59ee7c9aa5f967455c4a9969579fbd755fea/research/geeky-s12/2026-11-13/IW_GEEKY_S12_ROT013_SOURCE_B_QUARTIC_COEFFICIENT_ROBUST_PHASE_GATE_001_20261113.md

## 2. Twierdzenie REC11 — silniejsza faza negatywna

Dla pięciu wielomianów źródłowych `g_k(t)=sum_(j=0)^4 g_(k,j)t^j` (k=2,...,6) dopuszczamy niezależne współczynniki `g_(k,j)` w dokładnie rodzinie Geeky:

`[L_(k,j) - eps*|L_(k,j)|, U_(k,j) + eps*|U_(k,j)|]`.

Załóżmy `eps=10^-7`, `alpha=1541/50000=0.03082`, `delta=1257/50000=0.02514` oraz obszar legalności `beta in [0,0.2], |beta-alpha|>=delta`. Dwa NAJBLIŻSZE legalne kandydaty to `beta_L=71/12500=0.00568`, `beta_R=1399/25000=0.05596`. Odleglejszy wewnętrzny świadek `beta_*=1/1000000` jest również legalny.

**Twierdzenie:** dla KAŻDEGO (niezależnego, dowolnego) wyboru wszystkich 25 rzeczywistych współczynników z podanych przedziałów zachodzą OBA ścisłe porównania optymalnej nieujemnej amplitudy:

`D(alpha,beta_*) < D(alpha,beta_L)` i `D(alpha,beta_*) < D(alpha,beta_R)`.

Nowy certyfikat gwarantuje następujące ściśle dodatnie marginesy dla D (nie dla D²):

`D(beta_L)-D(beta_*) > 1.1 * 10^-17`;
`D(beta_R)-D(beta_*) > 1.6 * 10^-13`.

Wynik wystarcza do obalenia twierdzenia „globalny minimizer jest jednym z dwóch najbliższych legalnych punktów” przy tej delta, UNIFORM w całym 25-wymiarowym pudełku eps=1e-7. **Nie** udowodniono tutaj przy eps=1e-7, że świadek bije również `beta=0` (nasze dolne oszacowanie w tym porównaniu jest nierozstrzygające). Dla zakwestionowania optymalności obu najbliższych kandydatów takie dodatkowe porównanie nie jest potrzebne. Poprzedni certyfikat Geeky przy eps=1e-8 obejmował także `beta=0`; pozostaje ważny w swoim zakresie.

## 3. Ścisły, niezależny dowód przy wspólnych współczynnikach

Niech `N_i=(41-2k_i)^3` dla `k_i=2,...,6`, `W_i=N_i-N_(i+1)` dla i<5 i `W_5=N_5`. Źródłowo `W=(7778,6938,6146,5402,24389)`. Powłokowe wielomiany to

`s_i(t)=[N_i g_i(t)-N_(i+1)g_(i+1)(t)]/W_i` (i<5), `s_5=g_6`.

Wprowadźmy ważone wektory `A(t)_i=sqrt(W_i)*s_i(t)` oraz odległość zminimalizowaną po dodatniej amplitudzie

`D(alpha,beta)=min_(c>=0)||A(alpha)-c*A(beta)||_2`.

W oryginalnej rodzinie źródłowej wszystkie powłoki są dodatnie na [0,.2] — ponownie wykonany, ścisły certyfikat Geeky shell=5/5 PASS, także dla eps=1e-7. Zatem skalarne iloczyny dodatnie i amplituda optymalna jest wewnętrzna: `c=<A,B>/||B||²>0`. Zachodzi klasyczna tożsamość `D²=sum_(i<j) W_i W_j(s_i(alpha)s_j(beta)-s_j(alpha)s_i(beta))² / sum_i W_i s_i(beta)²`. Nasz program odtwarza tę formułę samodzielnie, nie importując ROT007/013.

Dla każdej oryginalnej pary końców `[L,U]` wybieramy dokładny środek `mu=(L+U)/2` i dokładny promień dopuszczalnej perturbacji

`r=(U-L)/2 + eps*max(|L|,|U|)`.

Po przejściu do powłok dostajemy środkowe współczynniki `C_(i,j)` oraz promienie `R_(i,j)`, przez bezpośrednie trójkątne oszacowanie `R_ij=[N_i r_ij+N_(i+1)r_(i+1),j]/W_i`; w ostatniej powłoce `R=r`. Dla każdego dopuszczalnego układu współczynników odchylenie powłokowego współczynnika od środka jest ograniczone przez `R_ij`, mimo że dwa wyrażenia `A(alpha)` i `A(beta)` wykorzystują TEN SAM `Delta C_ij`.

Niech `A0=A_center(alpha)`, `B0=A_center(beta)`, `c0=<A0,B0>/||B0||²>0`, `D0=D(A0,B0)`. Niech `EA` i `EB` oznaczają bezpieczne górne normy `||Delta A||`, `||Delta B||`. Gdy różnicę tworzymy przed oszacowaniem, dostajemy kluczową silniejszą nierówność

`||Delta A - c0 Delta B|| <= Eres(c0)`, gdzie

`Eres(c0)^2 = sum_i W_i [sum_(j=0)^4 R_ij * |alpha^j-c0 beta^j|]^2`.

Dla perturbowanej optymalnej amplitudy `c'=<A',B'>/||B'||²`, przy `||B0||>EB` zachodzi dokładnie

`|c'-c0| <= Lc := [EA||B0|| +||A0||EB + EA EB + c0(2||B0||EB+EB²)]/(||B0||-EB)²`.

Wynika to z różnicy iloczynów skalarnych oraz norm, po podzieleniu przez dolną granicę `||B'||²`. Przedziały dodatniości iloczynu `A'·B'` również zostały sprawdzone. Otrzymujemy niezależne, *obustronne* ograniczenie każdego D:

`D0-Eres(c0)-Lc*EB <= D_actual <= D0+Eres(c0)`.

**Dowód dolnej nierówności:** `D0<=||A0-c'B0||<=||A'-c'B'||+||Delta A-c'Delta B||<=D_actual+Eres(c0)+Lc EB`. **Dowód górnej:** w zadaniu perturbowanym wybierzmy legalną amplitudę `c0`, wtedy `D_actual<=||A'-c0B'||<=D0+Eres(c0)`. Żadne założenie o niezależności błędów przy różnych beta nie jest wykorzystywane.

Wszystkie operacje na 25 oryginalnych dziesiętnych końcach, liczbach `alpha,beta,epsilon` oraz współczynnikach są wykonane **dokładnie przez Python Fraction**. Pierwiastki norm mają 42-cyfrowe, konserwatywne, dokładne oszacowania przez integer `math.isqrt`: dla `q=n/d`, `z=floor(sqrt(n*10^84/d))` zapewnia `z/10^42<=sqrt(q)<(z+1)/10^42`. Decyzje znaków porównują same Fraction z racjonalnymi progami, nie `float`.

Liczby kontrolne (wyłącznie wyświetlenie):

| beta | dolna D | górna D |
|---|---:|---:|
| świadek 0.000001 | 5.350929722483717e-13 | **5.351031151014284e-13** |
| najbliższy lewy 0.00568 | **5.351144217606553e-13** | 5.351241160137871e-13 |
| najbliższy prawy 0.05596 | **6.996396492842196e-13** | 6.996487401347158e-13 |
| 0 | 5.350904176210391e-13 | 5.351005604639152e-13 (nierozstrzygające) |

Testy ścisłych progów porównują dokładne Fraction: `D_L_lower-D_witness_upper>11/10^18` i `D_R_lower-D_witness_upper>16/10^14`. Zera celowo nie certyfikowano. Ten sam epsilon=1e-7 stanowi zatem teraz **wspólny, wystarczająco udowodniony zakres dodatniej i ujemnej fazy**, każda przy swojej delta.

## 4. Odtwarzalność i rozdział pochodzenia

REC11 bezpośrednio pobrał oryginalny M13 Git blob `a6f50fbe...`, z jego 25 par końców wygenerował dokładny CSV `k,j,lo,hi`. Kopia w kontenerze ma Git blob SHA1 `09824281d5e4b3c87446be97b0e52ace3b33edae`, SHA256 `fb82f6d4b7554791836c026aacaad28040f0c92cbf211023b89011764632f8f2`. Z niezależnego fetch oryginalnego M13 identyczną tabelę wygenerowano ponownie i opublikowano w repo REC11; pinned fetch Git blob SHA **byte-identical** z lokalną kopią. Samo niekryptograficzne FNV64 `1e3123ee28f89066` służy fail-closed w skrypcie; dowód identyfikacji jest mocniejszy: źródłowy Git blob M13, repozytoryjny Git blob i lokalna SHA256.

Oryginalne wykryte w 25 parach długości części ułamkowych 59–64 cyfr. Lokalny samodzielny skrypt `rec11_rot029_independent_lipschitz_cert.py` nie importuje oryginalnego Geeky certyfikatora ani symulacji M13; importy standard-library. Testowane niezależnie są: wzór odległości po projekcji, pełne 25 współczynników, dokładne normy i błędy wspólne, dodatniość amplitudy, ścisły lewy/prawy margines, brak certyfikacji beta=0. Oryginalny certyfikat dodatni ROT007 z poszerzeniem ROT013 został **osobno ponownie wykonany w podłączonym V8**, nie przez skrypt Python: P 5 prostokątów, P mały, pochodna P, F0 8 segmentów, przesunięta linia P 2 segmenty =17/17 PASS oraz 5/5 powłok PASS. Min F0 około `+0.46768077995401613`, ale o znaku decydowały oryginalne dokładne rational intervals, nie to przybliżenie.

**Sufity:** pierwotny historyczny `dtc0a_runtime_v0_3_1.py` pozostaje byte-missing; wszystkie twierdzenia dotyczą oryginalnego M13 N41 B *funkcjonalnie dopasowanego* modelu pomocniczego, nie fizycznej teorii K/J3/GW/TPE, nie nowego przyrządu, nie błędu rzeczywistego sygnału. Pudełko 25 niezależnie zmiennych współczynników nie musi być realizowalne przez żadne pole Fouriera. M15 nadal właścicielem naukowej linii; REC11 niezależnym recenzentem; AUD2 do kolejnej recenzji, BW i właścicielska akceptacja niepotwierdzone. Żadnej automatycznej zgody na nowy skan lub fizyczny claim.

RETURN_ID: IW_REC11_ROT029_GEEKY_S12_ROT013_SOURCE_B_SHARED_COEFFICIENT_LIPSCHITZ_REFEREE_001_20261113

VERDICT: PASS_NEW_INDEPENDENT_NEGATIVE_EPS_1E_MINUS_7 / PASS_REEXECUTED_OWNER_POSITIVE_EPS_1E_MINUS_7 / COEXISTENCE_BOTH_PHASES_EPS_1E_MINUS_7 / ZERO_POINT_COMPARISON_UNRESOLVED_AT_EPS_1E_MINUS_7 / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
