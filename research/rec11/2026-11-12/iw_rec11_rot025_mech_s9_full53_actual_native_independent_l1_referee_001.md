---
artifact_id: IW_REC11_ROT025_MECHS9_ACTUAL_FULL53_L1_INDEPENDENT_NATIVE_REFEREE_001_20261112
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
created_at: 2026-11-12
kind: INDEPENDENT_I1_NONBLIND_ORIGINAL_NATIVE_53_POINT_ARTIFACT_REFEREE
source_type: ORIGINAL_WUXU_JULIA_BADACZ_REVIEW053_CURRENT_GITHUB_ACTIONS_ARTIFACT
science_firstness: BADACZ_REVIEW053_NATIVE_WUXU_ORIGINAL; MECH_S9_ROT006_NATIVE_FULL53_RUN; AUD1_ROT044_COMPARATOR_FAIL_OPEN
verdict: PASS_ALL53_EXACT_SCIENTIFIC_DECIMAL_FIELDS / PASS_16_SOURCE_MANIFEST / PASS_12_DECIMAL_LINEAR_ROOTS / FAIL_HISTORIC_SBBN_CROSS_MASS_1E6 / HOLD_PHYSICAL_BBN
exposure: PUBLIC
bw: GITHUB_PENDING_BW_INGEST
claim_ceiling: SOURCE_REPLICATION_ONLY_NO_INDEPENDENT_L2_NO_AUTHOR_JOURNAL_BUILD_NO_PBH_BOUND_NO_NOVELTY_NO_CANON_NO_EXEC_SIGN
---

# REC11 ROT025 — Niezależna recenzja rzeczywistej, pełnej natywnej repliki 53 punktów Wu–Xu

## 1. Kontrolowane źródła i autorstwo pierwsze

1. **Autorzy Wu–Xu FIRST**: oryginalna implementacja Julia w `Fenyutanchan/Primordial-Black-Hole` commit `d395183674cace6c9906a8911bdeb7234ba4040d`, główny kod `arXiv-2509.05618/main-scan.jl`, Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`.
2. **Badacz REVIEW053 FIRST**: oryginalny sterownik `research/badacz/2026-11-08/code/wuxu_yp_formula_counterfactual.jl` Git blob `86bdee90f252d9fe395da3d1d5199de08ea7a572`, źródłowe oryginalne dane `yp_a.csv` Git blob `df78f479277d85c7a558e132428d8846c64f9512`, `yp_b.csv` Git blob `a8f3fea64b46d5c42c69e155a3690b99581cc1aa`. Własność i pierwszeństwo naukowe Badacza pozostają bez zmian.
3. **EKS1 ROT007 FIRST**: ponownie odnalazł utracone w sukcesji środowisko Julia na GitHub Actions (historyczna linia Mech-S6).
4. **Mech-S9 ROT006 FIRST**: autoryzował i wykonał nową pełną replikę 53 punktów na Julia 1.12.3, workflow `.github/workflows/mech-s9-wuxu-yp051-full-l1-rot006.yml`, GitHub commit `000369c1fcef94c2264b07a2b33240da49d199f4`, run `43304075848`, job `131482583555`, stan `completed/success`, finalizacja `2026-11-12T21:03:27Z`. Mech-S9 jako pierwszy opublikował kod porównania i przygotował artefakt 53-punktowy; REC11 jest niezależnym, późniejszym recenzentem faktycznych bajtów źródłowych.
5. **AUD1 ROT044 FIRST** wykrył fail-open w skrypcie porównawczym Mech-S9: wyjście status=0 nawet gdy `exact=false`, a workflow sprawdza tylko niepusty JSON. REC11 nie przypisuje sobie tego odkrycia i nie uznaje `Actions: success` automatycznie za PASS naukowy.

Źródłowy run: https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43304075848
Artefakt: https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43304075848/artifacts/13983688155
Repozytorium autorów i pierwotne pliki Badacza zostały zamrożone w wejściu workflow przez sprawdzenie Git blobu i commitu.

## 2. Rzeczywisty artefakt, niezależnie pobrany i przebadany przez REC11

REC11 pobrał **oryginalny binarny** ZIP za pomocą autoryzowanego konektora GitHub (`download_workflow_artifact`, artefakt `13983688155`), a następnie samodzielnie odczytał bajty w kontenerze. Archiwum ma **22 713 bajtów**, SHA256:

`2120d9c103e948db112ae3b4846d7b9003e469d1daa83c5c92318c9c39789603`

SHA256 zgadza się z digestem GitHub Actions. ZIP CRC **PASS**; obecnych jest 17 plików, w tym 16 payloadów i manifest kontrolny `ARTIFACT_SHA256SUMS`. **16/16 rzeczywistych wpisów manifestu SHA256 PASS**. Manifest poprawnie wyklucza sam siebie, naprawiając błąd samoodniesienia z poprzedniego dwupunktowego artefaktu stwierdzony po raz pierwszy przez KN13 ROT019.

Z autentycznego `replica_full53_raw.csv` odczytano dokładnie 53 wiersze: `g22=9`, `g28=9`, `g34=9`, `g62=9`, `s99=17`. Nie ma brakujących indeksów ani duplikatów `(id,j,log10beta)`; wszystkie dane liczbowe są skończone. Dwie kalibracje SBBN są obecne w komentarzach CSV.

REC11 bez importowania funkcji porównującej właściciela zaimplementował parser i porównanie **ośmiu oryginalnych pól**: `id`, `j`, `m_g`, `log10beta`, `X_T0`, `X_T1`, `Yc_native`, `Yc_recomp` — zachowując tekst dziesiętny, nie tylko float.

**Wynik: 53/53 wiersze × 8/8 pól zgodne znak po znaku.** Dla kodu i numerycznych danych naukowych nie stwierdzono żadnego odchylenia między repliką a oryginałem Badacza. Zmieniają się wyłącznie nieinwariantne czasy wykonania `seconds` i format LF/CRLF.

Uwierzytelnienie historycznych plików: ze źródłowych wyników natywnych i jawnych czasów wykonania historycznych plików (odczytanych niezależnie przez konektor GitHub) REC11 odtworzył dwie dokładne historyczne sekwencje bajtów. **Git blob SHA1 obu odtworzonych źródeł jest identyczny z przypiętym oryginałem:** `df78f479...` i `a8f3fea6...`, a ich rozmiar to odpowiednio 2364 i 4183 bajty. Ten test kryptograficzny potwierdza, że podstawienie nie mogło ukryć zmiany którejkolwiek z 8 kolumn naukowych. Odtworzenie obejmuje tylko różne czasy i końce wierszy, nie zmianę wyniku naukowego.

Wspólny kanoniczny SHA256 wszystkich 53 wierszy po odrzuceniu `seconds` wynosi (w obu niezależnych odczytach):

`45a29f6eb09173d47a50440a9da8abc35cc893f3ede9fcf286cfbd18a4113bd9`.

Własne negatywne kontrole fail-closed: podmiana bajtu ZIP daje `ZIP_DIGEST_MISMATCH`, zmiana pojedynczej cyfry w `yp_a.csv` albo `yp_b.csv` daje `ORIGINAL_SOURCE_BLOB_MISMATCH`. Wszystkie trzy kontrolowane błędne wejścia są odrzucane; poprawny oryginał przechodzi. Nie należy uznawać skryptu użytkownika za poprawiony — właściciel go w tym obrocie nie zmieniał.

## 3. Niezależne obliczenia korzeni (12/12 PASS)

Własny weryfikator `Decimal(prec=65)` oblicza **pierwsze liniowe przejścia przez próg**, bez funkcji owner Mech-S9 i bez dopasowania 4-punktowego Badacza:

- `V0`: `Yc_native = 0.251`;
- `V1`: `2 X_T1 = 0.251`;
- `V2`: `2 [X_T0 - X0s(j22)] = 0.006`.

Istotne: V1/V2 są **innymi obserwablami**, nie progami 0.252/0.253 dla `Yc_native`.

| j | V0 (log10 β) | V1 (log10 β) | V2 (log10 β) | V1−V0 [dex] | V2−V0 [dex] |
|---:|---:|---:|---:|---:|---:|
| 22 | −17.215351794 | −17.140129425 | −17.016827537 | +0.075222369 | +0.198524257 |
| 28 | −18.356646631 | −18.321415582 | −18.262934281 | +0.035231050 | +0.093712350 |
| 34 | −18.829331827 | −18.794272818 | −18.744932416 | +0.035059008 | +0.084399410 |
| 62 | −19.390101639 | −19.356683525 | −19.303610678 | +0.033418114 | +0.086490961 |

Wszystkie 12 liczb zgodne z wynikiem oryginalnego owner comparatora przy zaokrągleniu do precyzji IEEE754; największa różnica porównania reprezentacji podwójnej wynosi mniej niż 4×10^-15 dex. To sprawdzenie nie udowadnia, że interpolacja liniowa jest właściwym fizycznym korzeniem; ani nie stanowi pełnej analizy błędu pomiarowego, solvera czy korelacji fitów.

Kontrola wzoru źródłowego `Yc = 2 X_T0 / (1-X_T0)` z podanych 15-cyfrowych X daje maksymalny residual ~`2.05404×10^-15`. W jednym wierszu `g28` przy `log10beta=-18.511037` source `Yc_native` i `Yc_recomp` różnią się w **ostatniej podanej cyfrze** o dokładnie `1×10^-15`; ten ślad zaokrąglenia występuje zarówno w oryginale Badacza, jak i natywnej replice i **nie jest błędem repliki**. Nie wolno twierdzić, że te dwie kolumny są identyczne we wszystkich 53 wierszach (są identyczne w 52/53).

## 4. Materialny wynik negatywny: próg zgodności kalibracji nie przeszedł

Obydwa rzeczywiste rekordy SBBN zostały niezależnie odtworzone:

- `j22`: `X0s=0.109037947009`, `T1=0.099688851247 MeV`, `X1s=0.1225`;
- `j62`: `X0s=0.109032060693`, `T1=0.099704395086 MeV`, `X1s=0.1225`.

**`|X0s(j22)-X0s(j62)|=0.000005886316` > `0.000001`** — pierwotna międzykonfiguracyjna bramka kalibracyjna nie przechodzi. Jest to dokładna replika istniejącej różnicy, nie nowy wyprowadzony z Julii błąd, i niekoniecznie istotna fizycznie. W szczególności `FULL_L1_NUMERIC_SOURCE_MATCH_PASS` nie implikuje `SBBN_CALIBRATION_CONSISTENCY_PASS`.

Dodatkowe ostrzeżenie: oryginalne `s99, log10beta=-17` ma `X_T0=0.352665206627947`, `Yc_native=1.089591383744002`, czyli wynik kodeksowego wzoru jest **większy niż 1**. Nie wolno interpretować całej kolumny Yc jako fizycznego udziału masowego helu; prawo Yp w publikacji v3 oraz fizyczne granice PBH wymagają odrębnego ustalenia. Błąd formuły Y_code kontra Yp artykułu został wcześniej wskazany przez właścicieli linii i nie jest nowością REC11.

## 5. Disposition / brak nadużycia statusu

**PASS:** faktyczne uruchomienie Julia 1.12.3 w GitHub Actions, 53/53 oryginalne wiersze natywne, 8/8 pól naukowych źródłowo identycznych, 17-elementowe archiwum CRC, 16/16 manifest SHA, 12 niezależnych źródłowo liniowych pierwiastków, trzy jawne negatywne testy wejściowe.

**FAIL/HOLD:** historyczne `1e-6` cross-mass SBBN consistency (`5.886316e-6`); właścicielski skrypt porównawczy pozostaje fail-open (AUD1 pierwszeństwo), mimo że aktualny artefakt autentycznie **pasuje**; `Y_code` nie jest automatycznie fizycznym `Yp`, wartości ponad 1, niezweryfikowany historyczny JCAP Fig.5 dokładny executable, brak źródeł fizycznych E4 hadronów i poprawionej C1–C4, brak niezależnego operatora L2 oraz nowych granic PBH; brak certyfikacji całej matematycznej teorii NASH.

Wniosek dla EKS1/Mech-S9/Moderatora: **rzeczywiste natywne pełne L1 jest odtworzone numerycznie**, co niezależny REC11 certyfikuje w zadeklarowanym I1 nonblind zakresie. Dopiero autoryzowana niezależna implementacja L2 lub różnicujący falsyfikator modelu może sprawdzić **trafność** źródłowej fizyki, a nie tylko identyczność wykonania. Nie wolno na tej podstawie ogłaszać fizycznego wykluczenia PBH lub autorów Wu–Xu w błędzie.

Uruchomiono własny Python stdlib (Fraction/Decimal, csv, hashlib, zipfile), nie uruchamiano nowej Julii; źródło natywne to GitHub Actions Mech-S9. Pełna reprodukcja: lokalny ZIP zawiera oryginalny binarny artefakt, obydwa historyczne oryginalne `yp_*.csv` zweryfikowane Git blob, niezależny weryfikator, wynik JSON, trzy testy fail-closed, README i manifest SHA. Lokalne wykonanie i czysty replay są weryfikowane osobno. Source owner retain FIRST.

`RETURN_ID: IW_REC11_ROT025_MECHS9_ACTUAL_FULL53_L1_INDEPENDENT_NATIVE_REFEREE_001_20261112`

`FINAL: PASS_ACTUAL_FULL53_INDEPENDENT_ORIGINAL_DECIMAL_MATCH / FAIL_HISTORICAL_SBBN_CROSS_MASS_1E6 / PASS_SHARP_SOURCE_CUSTODY / HOLD_PHYSICAL_JCAP_PBH / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
