---
artifact_id: IW_REC11_ROT035_GEEKY_S12_ROT019_NATIVE_FIELD_SCALAR_PROJECTIVE_REFEREE_001_20261113
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
date: 2026-11-13
classification: I1_NONBLIND_DIRECT_ORIGINAL_M13_SOURCE_AND_RATIONAL_INTERVAL_REFEREE
original_owner: GEEKY_S12_ROT019_NATIVE_FIELD_SCALAR_RANK_1_FIRST
result: PASS_SCOPED_ORIGINAL_NATIVE_FIELD_AMPLITUDE_RANK / NEW_SOURCE_BOX_PROJECTIVE_SEPARATION_CERTIFICATE
claim_ceiling: SOURCE_QUARTIC_AUXILIARY_ONLY / NO_HISTORICAL_RUNTIME_IDENTITY / NO_FIELD_SHAPE_PERTURBATION_REALIZABILITY / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
bw_receipt: UNVERIFIED
---

# REC11 ROT035 — źródłowy audyt Geeky-S12 ROT019 i certyfikat niezatartej odległości projekcyjnej

## 1. Pierwszeństwo, źródło i ograniczenia

**M13 FIRST** — publiczny, zachowany operator ROT33 M13 z funkcjami `source()`, `bracket()`, `lie()`, `proj()`, `calc()` i `tensor_polys()`, Git blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679`, ścieżka `research/m13/2026-10-24/verify_m13_rot33_interval.py`, oraz 25 oryginalnych skierowanych przedziałów współczynników B w `research/m13/2026-10-26/direct_B.json`, Git blob `a6f50fbe5904e580e84c87ee87c5ad043cdec5d0` (repo `wmakiela-tech/Nash-iw-research`). Oba pliki odczytano bezpośrednio i sprawdzono w ROT035. Z oryginalnego JSON odtworzono token po tokenie 25 wierszy CSV: FNV64 `1e3123ee28f89066`, byte SHA256 `fb82f6d4b7554791836c026aacaad28040f0c92cbf211023b89011764632f8f2`. Wersja historycznego `dtc0a_runtime_v0_3_1.py` nadal nie ma dowodu tożsamości bajtowej.

**Geeky-S12 ROT019 FIRST** zauważył i zweryfikował w rzeczywistym operatorze M13, że trzy hipotetyczne amplitudy całych pól `C1,C2,h` dają wyłącznie wspólne skalowanie energii pięciu powłok i nie są parametrami pięciu niezależnych wzmocnień; pierwotnie też wykonał oryginalny operator N41. Git blob raportu właściciela `eb63ea908686eb2f739013637aefac6c2d820c76`. **REC11** nie przypisuje sobie jego pierwszeństwa ani ponownego wykonania pełnego operatora. REC11 niezależnie audytuje algebrę na bezpośrednim źródle, wprowadza nowy **ścisły ilościowy certyfikat dla całej klasy 25 współczynników** i oddzielny certyfikat niezerowej prędkości kształtu przy zmianie `alpha`.

## 2. Zrekonstruowana algebra operatora

Kod źródłowy M13 w `calc` definiuje `C1,C2,h=source()`; wywołuje dwuliniowy nawias `bracket(C1,C2)`, dwa składniki zagnieżdżonych Lie `L(C1,L(C2,h))`, `L(C2,L(C1,h))` i składnik `L([C1,C2],h)`. Operator `em(...,alpha)`, projekcja TT i sumowanie są liniowe. Każdy wyraz B ma dokładnie jeden czynnik `C1`, jeden `C2` i jeden `h`. Stąd dla **hipotetycznych całopolowych** amplitud λ1, λ2, μ >0:

`B_alpha(λ1*C1,λ2*C2,μ*h) = (λ1*λ2*μ) B_alpha(C1,C2,h)`.

Wszystkie pierwotne średnie norm kwadratowych i energie rozłącznych powłok `s_i(alpha)` skaluje jeden wspólny `g²=(λ1λ2μ)²`. Pięć razy trzy pochodne amplitudowe `∂s_i/∂logλ_j=2s_i` mają macierz rzędu dokładnie **jeden** w punktach, gdzie `s_i>0`. Po podzieleniu przez jedną wspólną amplitudę pozostaje **zero** kierunków projekcyjnych wytwarzanych przez same trzy amplitudy. Przeciwnie, pięć wolnych niezależnych modyfikatorów `1+eta_i` po usunięciu wspólnej skali daje do czterech kierunków kształtu. To jest rozróżnienie **modelu sztucznego z pięcioma kalibracjami** od rzeczywistego zestawu gałek pierwotnego operatora M13, a nie stwierdzenie, że rzeczywiste niezależne kanały czujnika są niemożliwe.

## 3. Nowe twierdzenie REC11 — globalnie odporna rozróżnialność projekcyjna

Ustalono oryginalne N=41, `alpha=1/20=.05`, `beta=3/40=.075`, maski k=2..6, objętości `Nk=(41-2k)^3` i wagi rozłącznych powłok `W=(7778,6938,6146,5402,24389)`. Pięć kwartycznych energii powłok otrzymujemy bez zmiany źródła przez

`si(t)=(Nk*gk(t)-N(k+1)*g(k+1)(t))/Wi` dla i=1..4; `s5(t)=g6(t)`.

Każda z 25 skierowanych współczynnikowych par `[lo,hi]` jest niezależnie poszerzona o `epsilon*max(abs(lo),abs(hi))`, epsilon=1/10000000. Dla dowolnego **jednego i tego samego** doboru 25 współczynników zarówno przy alpha, jak i beta, ustawiamy `a_i=s_i(alpha)` i `b_i=s_i(beta)`. Wszystkie dziesięć energii ma **ścisłe dodatnie dolne oszacowanie** przedziałowe. Względny, niezależny od globalnej skali kwadrat błędu po dopasowaniu dowolnej dodatniej amplitudy:

`R² := min_(c>0) SUM_i Wi*(a_i-c*b_i)^2 / SUM_i Wi*a_i^2`.

Iloczyn skalarny `SUM Wi*a_i*b_i` jest dodatni, więc optimum osiąga `c0=(SUM Wi*a_i*b_i)/(SUM Wi*b_i²)`. Tożsamość Lagrange'a:

`R² = 1-(SUM Wi*a_i*b_i)^2/((SUM Wi*a_i²)*(SUM Wi*b_i²))`

`   = [SUM_(i<j) Wi*Wj*(a_i*b_j-a_j*b_i)^2]/[(SUM Wi*a_i²)*(SUM Wi*b_i²)]`.

**Dokładny Fraction interval proof** z zachowaniem wspólnych współczynników źródła daje dla każdej z 25 niezależnych współczynnikowych perturbacji:

`0.00297325437023945 < R² < 0.00297362237660917`

(zachowano zaokrąglone w kierunku konserwatywnym ogólnodostępne granice `0.00297325 < R² < 0.00297363`). Co najmniej jeden składnik licznika (powłoki 1 i 5) sam daje `R² > 0.00097351`. Wszystkie **10/10** różnic `a_i*b_j-a_j*b_i`, i<j, ma ściśle **ujemny** przedział wymierny, więc nie występuje znoszenie we wzorze sumy kwadratów. W punkcie środkowym `R²=0.002973438369067976`, `R=0.054529243246793514` (5.4529243%).

Wymiar bezwzględny zależy od skali i dlatego **nie** podaje się uniwersalnej dolnej granicy bezwzględnej straty dla amplitud mogących dążyć do zera. Wielkość R jest *projekcyjna*, niezmiennicza nawet przy osobnych dodatnich całopolowych skalach w dwóch pomiarach. To odpowiada właściwemu twierdzeniu rozróżnialności mimo nieznanego całkowitego wzmocnienia.

## 4. Nowy lokalny certyfikat kształtu alpha

Niech `s'(alpha)` oznacza pochodną pięciu kwartycznych energii względem alpha. Dokładny kwadrat prędkości kierunku w pięciowymiarowej przestrzeni ważonej to

`G(alpha)=[SUM_(i<j) Wi*Wj*(s_i'(alpha)*s_j(alpha)-s_j'(alpha)*s_i(alpha))²]/[SUM_i Wi*s_i(alpha)²]²`.

Przy `alpha=.05` całe 25-wymiarowe pudełko oryginalnych danych spełnia ściśle:

`7.86347145 < G(.05) < 7.86390760`.

Ponadto skierowany minor `H45=s4'(.05)*s5(.05)-s4(.05)*s5'(.05)` jest ściśle dodatni w całym pudełku, `1.6527e-26 < H45 < 1.6528e-26`. Właściciel wcześniej pokazał dodatniość minora na środkowych współczynnikach; obecny certyfikat obejmuje **wszystkie 25** niezależnie poszerzonych przedziałów. Oznacza to lokalną niezerową zmianę projekcyjnego kształtu przy zmianie alfa, której nie może zasymulować wspólna amplituda całych pól. Nie jest to wniosek o rzeczywistej czułości instrumentu.

## 5. Niezależna weryfikacja i falsyfikowalność

1. **Pierwsza, samodzielna implementacja Python standard-library Fraction** (`rec11_rot035_native_projective.py`) bada dokładne źródłowe przedziały, dodatniość dziesięciu energii, 10/10 znaków klinów, ścisły globalny przedział R², co najmniej jeden klin i dodatnie G. Decyzje znakowe i przedziałowe bez `float64`; `float` wyłącznie do wyświetlania dziesiętnych oszacowań.
2. **Druga napisana oddzielnie implementacja Decimal80** (`independent_decimal_geometry.py`) wyznacza R² dwiema różnymi formułami — Gram/Cauchy i sumą dziesięciu klinów — z błędem porównania mniejszym od 1e−68. Sprawdza 120 deterministycznych, legalnych punktów pudełka (kontrola punktowa, **nie** dowód ciągły) oraz różne zestawy trzech niezależnych hipotetycznych amplitud po stronie alpha i beta; bezwzględny błąd wyniku R² pod ich zmianą to 3e−80 (zaokrąglenie Decimal80), podczas gdy algebra gwarantuje równość dokładną.
3. **Osiem testów negatywnych**: cztery celowe mutacje oryginalnego pliku CSV × dwa niezależne wejściowe weryfikatory, w tym podmiana cyfry, usunięcie końcowego LF, zamiana wierszy i nagłówka. 8/8 FAIL-CLOSED **przed** obliczeniami naukowymi, wymuszonym SHA źródła.
4. Oryginalne 25 par przedziałów sprawdzone przez bezpośredni odczyt `direct_B.json` Git blob `a6f50fbe...`; rekonstrukcja 25 wierszy, 3377 bajtów, FNV64 `1e3123ee28f89066`, SHA256 CSV `fb82f6d4...` PASS. Bezpośredni kod M13 oryginalny odczytany Git blob `c6377cf...`; nie wykonano na nowo pełnego operatora M13/N41 w REC035. Jego wcześniejsze wykonanie należy do Geeky ROT019.

## 6. Negatywna wiedza i granice naukowe

**PASS**: Twierdzenie Geeky ROT019 o jednorodności oryginalnego operatora w trzech całopolowych amplitudach oraz o braku natywnego wektora pięciu niezależnych kalibracji jest źródłowo i algebraicznie poprawne. Nowy wynik REC035 daje ilościową dolną i górną granicę nieusuwalnego przez amplitudę błędu projekcyjnego, i lokalny przedział dodatniej prędkości kształtu dla wszystkich 25 oryginalnych przedziałów. **NIE twierdzimy**, że 25 niezależnych perturbacji współczynników jest realizowalne przez źródłowy proces, a pięć hipotetycznych kalibracji jest fizycznie niemożliwych. Istnieją inne możliwe deformacje kształtu `C1,C2,h`, zmiany operatora, maskowania i pomiarów; nie są przedmiotem obecnego kontraktu i mogą generować nowe kierunki. Dane historycznego oryginalnego `dtc0a_runtime_v0_3_1.py` nadal nie są odtworzone bajtowo, nie wykonano zewnętrznego ślepego I3, ani żadnego eksperymentu fizycznego. Wynik nie dowodzi nowości nad dojrzałą klasyczną teorią przestrzeni projekcyjnej / najmniejszych kwadratów.

Wersja testowa pięciu wolnych wzmocnień pozwala przy kappa około 6.627% uzyskać idealne dopasowanie w tym modelu, jednak **nie należy** importować tego zerowego ryzyka jako twierdzenia o oryginalnym operatorze M13 bez odrębnego mechanizmu pięciu realnych skalowań powłokowych. Brak modyfikacji kodu właścicieli, brak samoczynnego wdrożenia do BW, brak statusu CANON/EXEC_SIGN lub automatycznych kolejnych uruchomień.

**RETURN_ID:** `IW_REC11_ROT035_GEEKY_S12_ROT019_NATIVE_FIELD_SCALAR_PROJECTIVE_REFEREE_001_20261113`

**STATUS:** `PASS_GEEKY_ROT019_SCOPED / PASS_NEW_SOURCEBOX_PROJECTIVE_R2_CERT / PASS_NEW_SOURCEBOX_LOCAL_SHAPE_METRIC / HOLD_NATIVE_SHAPE_REALIZABILITY / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.

---

## Reproducibility receipt

Actual local ZIP `IW_REC11_ROT035_GEEKY_NATIVE_FIELD_SCALAR_PROJECTIVE_BOX_CERT_REPRO_001_20261113.zip`: size 16,159 bytes, SHA256 `41b9cfd3191acb2db234e3ecfce00acd18c3e6d32e711e720052564fff2292e3`; CRC PASS; 9/9 payload SHA256 PASS; three clean isolated JSON replays byte-identical; 8/8 source-mutation controls FAIL CLOSED. ZIP is conversation-local, not GitHub-hosted. This published source-typed receipt differs from the Polish REPORT.md inside ZIP by the receipt paragraph and does not claim byte identity.

RETURN_ID: `IW_REC11_ROT035_GEEKY_S12_ROT019_NATIVE_FIELD_SCALAR_PROJECTIVE_REFEREE_001_20261113`.
