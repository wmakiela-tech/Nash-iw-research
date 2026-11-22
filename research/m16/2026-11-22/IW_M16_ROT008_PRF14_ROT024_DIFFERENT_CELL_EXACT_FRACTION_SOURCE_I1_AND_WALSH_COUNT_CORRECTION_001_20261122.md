---
artifact_id: IW_M16_ROT008_PRF14_ROT024_DIFFERENT_CELL_EXACT_FRACTION_SOURCE_I1_AND_WALSH_COUNT_CORRECTION_001_20261122
return_id: IW_M16_ROT008_PRF14_ROT024_DIFFERENT_CELL_16_PAULI_SO3_EXACT_18_CHANNEL_ALIAS_AND_95PC_INTERVAL_POWER_I1_WITH_WALSH_9_VS_10_SOURCE_CORRECTION_001_20261122
origin: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_11 / M16
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
science_type: DIFFERENT_CELL_NONBLIND_PRF14_ROT024_ORIGINAL_SOURCE_I1
status: OWNER_SOURCE_DIRECT_READ / PURE_FRACTION_AND_INTEGER_SQRT_INDEPENDENT_EXECUTION_PASS / REPLAY_BYTE_IDENTICAL / MAIN_THEOREM_PASS / NONMATERIAL_FOURIER_COUNT_CORRECTION
claim_ceiling: NO_HARDWARE / NO_GENERAL_NOVELTY / NO_UNRESTRICTED_PROCESS_TENSOR / NO_CANON / NO_EXEC_SIGN / NO_BW_NATIVE_ING
---

# M16 ROT008 — niezależny audyt źródłowy PRF14 ROT024: identyfikowalność pamięci Pauliego i przeszkoda dwuwierszowa SO(3)

## 0. Decyzja badawcza i bezpośrednie źródła

ROT007 uzasadnił zamrożenie kolejnych syntetycznych wariantów M13 bez rzeczywistego operatora odczytu. M16 ROT008 sprawdza zamiast tego matematycznie źródłowy fizyczny model kwantowego kanału Pauliego z dwóch ogłoszonych eksperymentów UNIT i destrukcyjnego BREAK, obecnie rozwijany przez PRF14 i INT10. Celem jest inna komórka I1, nie przejęcie autorstwa ani arbitralne wznowienie C1. Żaden sprzęt nie został uruchomiony.

Oryginalny kompletny artykuł PRF14 ROT024 przeczytano w pinned GitHub commit 743a65e0e73677a3191bd6acd01df5f3486be7e8, Git blob 7b7a87df05e404e2b8af96755bf946c1fbbabc7f:
https://github.com/wmakiela-tech/Nash-iw-research/blob/743a65e0e73677a3191bd6acd01df5f3486be7e8/research/prf14/2026-11-22/IW_PRF14_ROT024_TWO_ROW_SO3_ORTHOGONALITY_SOURCE_TRANSPORT_FOUR_CHARACTER_95PC_TV_LOWER_AND_PHYSICAL_NO_GO_001_20261122.md

Oryginalny kod PRF14 również przeczytano, ale NIE uruchamiano:
https://github.com/wmakiela-tech/Nash-iw-research/blob/765da45bd9a6f860cb5b2903520bbd933e90c6ba/research/prf14/2026-11-22/code/IW_PRF14_ROT024_TWO_ROW_ORTHOGONALITY_FOUR_CHARACTER_PHYSICAL_COMPACT_REPRO_001_20261122.py
blob 016b35271078e54ed7fbaeab7bb2f957953c2595.

PRF14 ROT023 zachowuje FIRST poprzedni pojedynczy wiersz SO(3), PRF14 ROT024 FIRST dwu-wierszową przeszkodę i konstrukcję 16 fizycznych źródeł, INT10 FIRST własne certyfikaty kalibracji i TV. Nie rościmy pierwszeństwa w ogólnej teorii obrotów, tomografii, pomiarów Bell, prawdopodobieństwa ani testów statystycznych.

## 1. Niezależna reprezentacja, bez importu kodu autora

Zbudowano od podstaw osobny, wykonany rzeczywiście program Python standard library na Fraction, isqrt i Decimal. Cztery bity opisują dwa elementy v,w z F2^2, razem 16 możliwych historii Pauliego. Użyto bitwise parity do trzech znaków Pauli każdego v i w. Model:
p_C(v,w) = [1 + suma_(i różne j) C_ij chi_j(v) chi_i(w)]/16.

Matryca sześciu źródłowych dodatnich składowych to:
C0=[[0,9/100,11/100],[7/100,0,1/10],[8/100,12/100,0]].
Oryginalna fizycznie proper SO(3):
S0=(1/7)*[[2,6,3],[-3,-2,6],[6,-3,2]].
Kontrole dokładnych wymiernych S0*S0^T=I i det S0=+1 PASS.

Unitarny kanał 3x3 obliczono przez dosłowną sumę 16 historii, każda zawiera macierz Pauli sign D_w S D_v, NIE przez podstawienie gotowego wzoru korelacyjnego. Dwie dozwolone procedury: UNIT ma jeden nieznany środkowy S należący do SO(3), BREAK mierzy destrukcyjnie wspólne 16 etykiet historii; p_UNIT i p_BREAK NIE MUSZĄ być jednakowe bez testowanego założenia niezmienności źródła wobec wyboru protokołu.

## 2. PASS: źródła 16-historii, dwie odrębne skale

Łagodna oryginalna para:
p_BREAK=p_(C0), p_UNIT=p_((26/25)C0).
Z nowych wyliczeń Fraction:
min p_BREAK=73/1600;
min p_UNIT=899/20000;
TV=171/40000=.004275.
Suma każdego p jest dokładnie 1, minima >0.

Silniejsza osobna para do statystycznego przykładu:
p_BREAK=p_((7/2)C0), p_UNIT=p_((91/25)C0).
Nowe Fraction:
min p_BREAK=11/3200;
min p_UNIT=43/40000;
TV=1197/80000=.0149625.
Suma każdego p dokładnie 1, minima >0.
Nie mieszano obu wielkości TV. Dozwolono klasyczny 16-etykietowy proces błędów Pauli bez dowodu, że instrument dostępny fizycznie.

### Mała korekta tekstowa: dziesięć versus dziewięć zerowych współczynników

Zrekonstruowano pełną, dokładną 16-elementową transformatę Walsh każdego rozkładu. Bilans jest 1 STAŁY współczynnik normalizacji F00=1, 6 wybranych NIEZEROWYCH współczynników mieszanych i 9 pozostałych NIETRYWIALNYCH równych 0. Zatem literalne sformułowanie oryginału o 10 innych zerowych współczynnikach jest niedokładne: dopełnienie zbioru sześciu współczynników w pełnej 16-wymiarowej transformacie ma 10 elementów, ale jednym z nich jest jednostka, nie zero. W dziewięciu nieaktywnych współczynnikach: 3 marginalne v, 3 marginalne w, 3 diagonalne mieszane. To nie podważa żadnego twierdzenia głównego PRF14.

## 3. PASS: wszystkie sześć słabszych warunków, niepowodzenie wspólnej ortogonalności

Dla pozornego ilorazu x_ij=k S0_ij, k=26/25, dokładnie:
każda suma 2 kwadratów nieprzekątnych elementów każdego z 3 wierszy = 6084/6125 <1;
każda analogiczna suma każdej z 3 kolumn = 6084/6125 <1.

Jednocześnie ortogonalność dwóch pierwszych pełnych wierszy przy niewiadomych przekątnych wymaga:
|x02*x12| <= |x10| sqrt(1-x01^2-x02^2) + |x01| sqrt(1-x10^2-x12^2).

Od zera obliczono 48-cyfrowe wymierne osłony każdego pierwiastka przez integer isqrt. Dokładna dolna osłona lewa-prawa jest ściśle >.2879, informacyjnie .28792260803896597. W pełni wymierny wielomian konieczny:
Q=(W^2-A-B)^2-4AB,
A=x10^2(1-x01^2-x02^2), B=x01^2(1-x10^2-x12^2), W=x02*x12,
wynosi DOKŁADNIE 409983535198224/17951812744140625 >0.
W konsekwencji ilorazy nie pochodzą z jednej fizycznej właściwej macierzy S; wynik PRF14 ROT024 PASS.

## 4. PASS: gwarancja 95% i niezależny wymierny certyfikat mocy

W silnej parze źródeł, przy deklarowanej tolerancji gate δ_gate=.001, błędach całkowitych UNIT e_u=.00145 i BREAK e_c=.003, dla kandydata dolnej odległości źródeł z=.00026 użyto SKRAJNIE NIEKORZYSTNYCH osłon każdego |S_e|:
l_e=(|a0_e|-|Cunit_e|δ_gate-2e_u)_+/(|Cbreak_e|+2e_c+2z),
u_e=min(1,(|a0_e|+|Cunit_e|δ_gate+2e_u)/(|Cbreak_e|-2e_c-2z)),
gdzie a0_e=Cunit_e*S0_e; jeśli mianownik u niedodatni, przyjęto u=1.

Włożenie tych Fraction do koniecznego warunku dwóch wierszy i zastosowanie ścisłych wymiernych górnych granic sqrt przez isqrt dało dolny margines
5.0950015457609176e-5 > 5e-5 >0.
To niezależnie od autora sprawdza istotną dodatnią granicę mocy i nie polega na floating-point porównaniu.

Osobno idealna para bez błędu przy z=.0056 nadal daje margines +.00095957418, przy z=.00563 margines -.0000998577. Jest to strażnik oryginalnej deklaracji o progu około .005627, NIE pełna niezależna certyfikacja wszystkich jego cyfr lub globalnego optimum.

Osiem odchyleń średnich i union bound odtworzono 80-cyfrowym Decimal.ln i exp:
nu=6,826,416 prób KAŻDEGO z 4 ustawień UNIT, nb=11,536,642 prób dla JEDNEGO wspólnego strumienia BREAK.
Łączne N=4nu+nb=38,842,306 uruchomień eksperymentu, breaker wymaga 2nb=23,073,284 pomiarów baz Bella.
8exp(-nu*.0013^2/2)+8exp(-nb*.001^2/2)=.049999986789692...<.05.
Cztery współczynniki Bell obliczane z TEGO SAMEGO zbioru etykiet są skorelowane, lecz union bound nie potrzebuje ich niezależności.
To jest warunkowa, konserwatywna gwarancja modelowa, NIE budżet dostępny na sprzęcie.

## 5. PASS: pełna nierozróżnialność 18/18 przy różnych źródłach

W0: p_UNIT=p_BREAK=p_(7/2 C0), środkowy S0, TV źródłowy 0.
W1: BREAK identyczne; proper S' jest S0 poprzedzonym konstrukcją racjonalnego obrotu Cayleya z t=1/1000, a UNIT ma rozkład z 6 zmienionymi mieszanymi współczynnikami
C'_ij=(7/2)*C0_ij*S0_ij/S'_ij dla i≠j, 9 innych nietrywialnych pozostaje 0.
Użyto niezależnego algorytmu 16 rozkładów Fraction i bezpośredniego obliczenia kanału jako średniej D(w) S D(v).

W1 ma min p_UNIT'=0.00356598491344>0, całkowitą TV(p_UNIT',p_BREAK)=41979/50199950=.000836235892665...>0.
WSZYSTKIE 9 kanałowe współczynniki T(S0,pW0)=T(S',pW1) DOKŁADNIE jako Fractions.
To samo po dodatkowej macierzy fizycznego sterowania D_X: kolejne 9/9, razem 18/18.
BREAK ma 16/16 identyczne etykiety w W0/W1.

Wniosek: nawet udany zerowy test nie dowodzi, że wybór instrumentu nie zmienia źródła, ponieważ zmiana nieznanej bramki może maskować zmianę p. To dotyczy ZADANEJ klasy dwóch osobno ogłaszanych protokołów i nie jest twierdzeniem o dowolnym unified process tensor.

## 6. Wykonanie, reprodukcja, ograniczenia

Nowy niezależny program napisany i wykonany dwukrotnie z Python -I:
lokalny /mnt/data/m16_rot008/m16_rot008_independent_prf24_pauli_so3_fraction_i1.py,
SHA256 d5364df7e4702ff99890457301a27875b95e4d2aad0a55ee00b8fd9ea6637077,
Git blob lokalnego pełnego programu 2cad296d60cb99ea400bb85727190cbbe3d3b883.
Wynik JSON SHA256 b95a2ac2ab1d1921b40389b26ebe53fd8f704ef4e7a61ee5a6057c998cca0256.
Dwa stdout byte identical SHA256 81835720b5909d4b4018f8f80b13864c2bbfb2a4cd3a96f31ff20e9a409c1f42.

Weryfikowano algebraiczne źródła 16 stanów, pełne dwóch kanałów 18 wpisów, normy SO(3), ortogonalność, żądany dodatni margines 95% i koszt próbek. NIE przeprowadzano ponownie 800 losowań ownera, ani oryginalnego pełnego kodu Krausa 2x2 i nie pozyskano urządzenia kwantowego.

Nie ma roszczeń do zewnętrznej nowości ogólnej, potwierdzonej nieklasycznej pamięci kwantowej, fizycznej dostępności niszczącego tester break, uniwersalnego process tensor ani przyjęcia przez CANON.

RECOMMENDATION: DIFFERENT_CELL_SOURCE_I1_PASS dla oryginalnego PRF14 ROT024, z krótką redakcyjną korektą liczby zerowych współczynników Walsh (9 nie 10). Publikacyjnie i strategicznie najważniejsze pozostaje niezależne wykazanie użyteczności testu w realizowalnym interfejsie instrumentalnym, nie dalsze redukcje teoretycznych n.

FINAL: M16_ROT008_PRF14_QUARTIC_I1_PASS / ALL_16_POSITIVE_FRACTION_SOURCE_I1_PASS / EXACT_WALSH_1_PLUS_6_PLUS_9_COUNT_GUARD / 95PC_38842306_MODEL_BUDGET_PASS / 0P000050950_EXACT_POWER_MARGIN_PASS / EXACT_18_OF_18_GAUGE_ALIAS_PASS / NO_HARDWARE / NO_GENERAL_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_BW_NATIVE_WRITE.
