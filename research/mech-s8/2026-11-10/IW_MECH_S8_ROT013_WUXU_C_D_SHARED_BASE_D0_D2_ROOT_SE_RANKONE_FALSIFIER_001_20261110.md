---
artifact_id: IW_MECH_S8_ROT013_WUXU_C_D_SHARED_BASE_D0_D2_ROOT_SE_RANKONE_FALSIFIER_001_20261110
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_07 / Mech-S8
date: 2026-11-10
exposure: PUBLIC
document_type: INDEPENDENT_CONDITIONAL_SOURCE_MODEL_ROOT_LEVEL_FALSIFIER
result_class: EXECUTED_STD_LIB_REPRODUCTION / BOUNDED_EXISTENTIAL_ROOT_LEVEL_WITNESS
source_commit: 11eeb1c37c21f19b2510e3bba5ae50169cbd5d79
source_git_blob: 1df29aff025755f9042628ec85752178b991d398
sync_state: LOCAL_REPRO_VERIFIED / GITHUB_PENDING_BW_INGEST
claim_ceiling: MODEL_INTERNAL_HYPOTHETICAL_FIT_SE_ROOT_BOX / NOT_PHYSICAL_UNCERTAINTY / NOT_JULIA_DOUBLE_BAND / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
---

# Mech-S8 ROT013 — Wspólna baza, kontrole D×0/D×2 i dokładny kontrprzykład rzędu 1 na poziomie położeń konturu

## Streszczenie naukowe i relacja do pierwszeństwa

Wu–Xu (arXiv:2509.05618, kod autorów v2) są właścicielami modelu; **Badacz PREREG048/REVIEW050 (8 XI 2026)** wykonał natywne uruchomienia czterech pasm odpowiedzi w kodzie Julia Wu–Xu. **Mech-S8 ROT012 (10 XI)** jako pierwszy przedstawił SVD i konstrukcję rzędu 1 w *niezależnej per-współczynnik warunkowej ramce ±1 nominalny fit-SE*. **INT9 ROT008 (10 XI)** niezależnie potwierdził ROT012 oraz wykazał, że brak stabilnego rozdzielenia C/D **nie unieważnia** warunkowego przewidywania dla ich łącznej poprawki.

Nowy przyrost ROT013 jest węższy, ale ostrzejszy: poprzednie współczynniki C i D dzieliły **ten sam wynik bazowy** przy ustalonym `j`, a pasmo D miało niezależne przebiegi `D×2` i `D×0`. Poprzedni kontrprzykład nie wymuszał kompatybilności źródłowej tych czterech dopasowanych położeń konturu naraz. W ROT013 konstruuję **jedną i tę samą bazę β dla C/D**, jeden współczynnik D spełniający obie transformacje `D×2` i `D×0`, oraz *wspólny* stosunek dla czterech wartości masy początkowej.

## Oryginalne źródło oraz wejścia

Original pinned owner artifact:
- [Badacz REVIEW050 full report](https://github.com/wmakiela-tech/Nash-iw-research/blob/11eeb1c37c21f19b2510e3bba5ae50169cbd5d79/research/badacz/2026-11-08/IW_BADACZ_WUXU_BAND_RESOLVED_HADRON_RESPONSE_KERNEL_REVIEW_050_20261108.md)
- [Original JSON model fit diagnostics](https://github.com/wmakiela-tech/Nash-iw-research/blob/11eeb1c37c21f19b2510e3bba5ae50169cbd5d79/research/badacz/2026-11-08/data/kernel_analysis.json), Git blob `1df29aff025755f9042628ec85752178b991d398`

Z oryginalnych `configs` odczytałem położenie `root` i jego nominalny `se` z regresji liniowej (po siedem wartości `Y_C` na konfigurację), dla czterech wierszy `j∈{22,28,34,62}`, przy odpowiedziach `base_j`, `C2_j`, `D2_j`, `D0_j`. Otrzymujemy **16 źródłowych położeń**. Nie traktuję `se` jako statystycznie niezależnych ani jako gwarantowanych, rygorystycznych przedziałów błędów rzeczywistego modelu.

## Równania testu

Niech \(b_j\) oznacza bazowy `log10 β` dla `Y_C=0.251`; \(c_j\) wynik przy `C×2`, \(d^{(2)}_j\) przy `D×2`, a \(d^{(0)}_j\) przy `D×0`.

Pod źródłowo typowanym, warunkowym założeniem odpowiedzi afinicznej w mnożniku emisji:

\[
s_C(j)=10^{b_j-c_j}-1,\qquad
s_D^{(2)}(j)=10^{b_j-d^{(2)}_j}-1,\qquad
s_D^{(0)}(j)=1-10^{b_j-d^{(0)}_j}.
\]

Test negatywny, którego wcześniej brakowało, wymaga jednocześnie:

\[
\boxed{s_D^{(2)}(j)=s_D^{(0)}(j)=q\,s_C(j)} \quad
\text{dla wszystkich }j,\qquad q=0.210.
\]

**Jawna konstrukcja:** dla każdego wiersza \(j\) wybieram poprawki \(b'_j=b_j+x_j u_{b,j}\), \(c'_j=c_j+y_j u_{c,j}\). Następnie z ich *wspólnej bazy* definiuję \(s'_C(j)=10^{b'_j-c'_j}-1\), \(s'_D(j)=0.210\,s'_C(j)\) i wyznaczam jednoznacznie:

\[
d^{(2)\prime}_j=b'_j-\log_{10}(1+s'_D(j)),\qquad
d^{(0)\prime}_j=b'_j-\log_{10}(1-s'_D(j)).
\]

Jest to konstrukcja algebraiczna, nie optymalizacja dopasowania do oryginalnego `Y_C(t)` i nie nowy przebieg Julia.

## Przeprowadzony test

Wystarczają następujące **jawne, nieoptymalizowane** poprawki \(x,y\):

- `j=22`: \((x,y)=(-0.075,-0.860)\);
- `j=28`: \((x,y)=(-0.565,+0.860)\);
- `j=34`: \((x,y)=(+0.218,-0.218)\);
- `j=62`: \((x,y)=(+0.429,+0.429)\).

Wyniki skryptu (wartości w nominalnych **osobnych SE położeń root**):

| j | baza | C×2 | D×2 | D×0 | największe |z| | modelowy Δ(C+D) pierwotny [dex] | modelowy Δ(C+D) kontrmodel [dex] |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 22 | -0.075 | -0.860 | +0.855015 | -0.860765 | 0.860765 | -0.148985 | -0.149007 |
| 28 | -0.565 | +0.860 | -0.859500 | +0.859212 | 0.860000 | -0.068572 | -0.065050 |
| 34 | +0.218 | -0.218 | -0.107109 | -0.217234 | 0.218000 | -0.035783 | -0.037454 |
| 62 | +0.429 | +0.429 | -0.427524 | -0.152660 | 0.429000 | -0.003663 | -0.005307 |

**16/16 przesunięć mniejszych od 0.900 nominalnego SE**; faktyczne maksimum:

\[
\max_{j,X\in\{b,c,d2,d0\}}
\frac{|X'_j-X_j|}{u_{X,j}}
=\mathbf{0.860765078038}<0.900.
\]

W tym samym czasie alternatywa ma rząd 1 w wymiarze C/D z definicji, bo \(s'_D(j)=0.210\,s'_C(j)\) dla każdego `j`, oraz **oba znaki zaburzenia `D×0`/`D×2` mają ten sam współczynnik**. Sprawdzono numerycznie tożsamości przeliczeń `s_D` z obu korzeni (reszty poniżej 1e−12).

Największa odnotowana różnica prognozy *w warunkowym łącznym surogacie* między danymi pierwotnymi a alternatywą wynosi około 0.003523 dex (`j=28`), co jest zgodne z kierunkiem wcześniejszego wyniku INT9 ROT008: **możliwa słaba identyfikacja rozdziału i jednocześnie użyteczna agregacja**. Nie sprawdza to rzeczywistej addytywności solvera przy wspólnej zmianie źródła.

## Interpretacja i negatywna wiedza

**Potwierdzone:** kontrprzykład rzędu 1 dla dwupasmowej mapy C/D nadal istnieje, jeśli wymagamy wspólnej bazy i spójnych dwóch przeciwstawnych perturbacji emisji D, w *hipotetycznej prostokątnej ramce położeń root* zbudowanej z **indywidualnych nominalnych SE dopasowania**. To mocniejszy test niż ROT012; wyklucza naprawę problemu samym algebraicznym utożsamieniem bazy albo dołożeniem istniejącej kontroli `D×0`.

**NIE potwierdzono:**
1. Wartości `se` nie są rygorystycznymi przedziałami błędów, nie wyznaczają wspólnego przedziału ufności, nie muszą odpowiadać niezależnym zmianom próbek wejściowych czy natywnego solvera. Konstrukcja pokazuje tylko istnienie w zadeklarowanym modelu tolerancji korzeni, a nie realną niedookreśloność fizyki Wu–Xu.
2. Warunkowa liniowość \(10^{-\Delta}\) przy `D×0/D×2` to założenie mapy źródła, nie twierdzenie o dokładnym natywnym Jacobianie; brak testu równoczesnego `C×2+D×2` w oryginalnym solverze.
3. Rząd 1 został skonstruowany przez zmianę estymat w obrębie nominalnych SE; nominalna macierz właściciela nie jest dokładnie rzędu 1.
4. Nie rozstrzyga to walidacji prawdziwych widm w BlackHawk/PYTHIA, przejścia poniżej \(10^9\) g, naładowanych par czy historycznego pochodzenia Fig. 5.
5. Status ścisłego błędu ODE dla Mech-S7 ROT035 pozostaje OPEN; nie przenosi się certyfikatów między różnymi trajektoriami.

## Wniosek operacyjny i procedura falsyfikacji

Najtańszy **test addytywności** (po decyzji właściciela i w dostępnym natywnym środowisku) to *jeden* przebieg `j22` z jednoczesnym `C×2+D×2`, porównany z wcześniej zapisanymi wartościami \(\Delta_{joint,model}\approx-0.148985\) dex; przejście nie rozdziela C/D, tylko testuje założenie surogatu. Dopiero niezależny, widmowo sprawdzony model emisji dla mas \(10^9\), \(3\times10^8\), \(10^8\) g oraz drugi obserwabl o odmiennym jądrze odpowiedzi mogą uzasadniać wnioskowanie oddzielne.

**Stan:** `ROT013 EXECUTED_ROOT_LEVEL_WITNESS_PASS / INVERSE_C_D_STABLE_SPLIT_UNPROVEN / CONDITIONAL_AGGREGATE_FORWARD_AVAILABLE / E4_SOURCE_BLOCK / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN / BW_PENDING`.

## Reprodukcja

Dołączony skrypt \`mech_s8_rot013_shared_root_rank1_reproducer.py\` działa z biblioteki standardowej Python i zawiera dokładne transkrypcje 16 par `(root, se)` z przypiętego JSON Badacza. Zapisuje deterministyczny wynik \`mech_s8_rot013_shared_root_witness.json\`, bez `Infinity`/`NaN`. Manifest podaje sumy SHA-256 rzeczywistych plików; archiwum ZIP zweryfikowano przez CRC, porównanie bajtowe i uruchomienie kodu po wypakowaniu.