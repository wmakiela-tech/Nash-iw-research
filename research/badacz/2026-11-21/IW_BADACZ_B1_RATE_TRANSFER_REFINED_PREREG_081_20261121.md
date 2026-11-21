---
artifact_id: IW_BADACZ_B1_RATE_TRANSFER_REFINED_PREREG_081_20261121
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), współwłaściciel natywny B1, właściciel T2
created_at: 2026-11-21
document_type: PREREGISTRATION (zamrożona przed jakimkolwiek przebiegiem pomiarowym 081)
authorization: Moderator 21 XI 14:20 „Tak autoryzuję” — odpowiedź na pytanie „Autoryzujesz przygotowanie i uruchomienie PREREG_081?” (przygotowanie + uruchomienie; uruchomienie dopiero po commicie tego dokumentu)
supersedes_design_of: PREREG_079 (wynik GATE_FAIL_NO_LABEL, REVIEW_080, Nash-iw-research@9aa00ea)
claim_ceiling: NUMERYCZNY w modelach / NO_PBH_BOUND / NO_PAPER_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_081: transfer natywnych szybkości z rozdzielonym błyskiem końcowym PBH

## 0. Co się zmienia względem PREREG_079

Pytanie, przypadki, węzły β (`cfg079_{orig,e5}.dat`), ramię sieci (`prym_rate_patch_079.py`, `net_rate_079.py`, `run_net_079.py` bez zmian), definicje ρ, D_code i D_net oraz etykiety pozostają **identyczne z PREREG_079 §0–§2 i §5**.

Zmieniają się trzy rzeczy, wszystkie wynikające z REVIEW_080:

1. **Eksport szybkości (`rate_dump_081.jl`).**
   - W gałęzi `hadrons_output_flag` funkcja `magic` autorów dodatkowo zwraca obiekt rozwiązania ODE. To zmiana wyłącznie wyjścia; wywołanie solve pozostaje nietknięte.
   - Wszystkie eksportowane wielkości liczę z tego rozwiązania na połączonej siatce ln a: 10000 punktów autorów plus 20000 punktów jednorodnych w ln a na przedziale [ln a(i_d − 200), ln a(i_d + 2)], gdzie i_d to ostatni żywy punkt wyjściowy. W oknie śmierci PBH siatka jest więc 100× gęstsza.
   - Gęstości hadronów obcinam tak samo jak `evolution_system!` (log n ≥ −100).
   - Eksportuję tylko punkty z T_SM ≤ 30 MeV, bo PRyMordial startuje od 10 MeV.
2. **Bramki z progami a priori ponad szumem** (reguła z REVIEW_080 §5):
   - **V2_EXACT** (zastępuje V2 różnicowe). W każdym punkcie wywołuję `evolution_system!` autorów dwukrotnie: raz z rzeczywistym stanem, raz z sześcioma log-gęstościami hadronów ustawionymi na −200 (obcięte do e^−100).
     - had_code = (du₄ − du₄^{bez hadronów})·H·X, gdzie H = 1/(t·du₁).
     - Porównuję to z eksportowanym (1−X)r_{p→n} − X·r_{n→p}.
     - Próg: maks. błąd względny ≤ 1e-6 w punktach z |had| > 1e-6·max|had|. Oczekiwany szum to zaokrąglenie Float64, ~1e-15, więc próg leży ≫ 5× ponad szumem.
     - Przebiegi bazowe (β = 1e-30) są wyłączone: ich szybkości ~1e-12 s⁻¹ są porównywalne z podłogą obcięcia e^−100.
   - **V3_NET_ZERO:** próg 1e-5. Zmierzony szum solvera sieci wynosi 6–8e-7 (REVIEW_080), więc margines ≥ 12×; to < 0.2% sygnału.
   - **V6_REFINED (nowa):** w każdym przebiegu zastosowano zagęszczenie (≥ 20000 eksportowanych punktów, i_d > 200).
   - **V1, V4, V5 bez zmian.** V5 (co drugi punkt zmienia ΔY_net o ≤ 1%) działa teraz na siatce połączonej.
3. **Predykcje.** P1 i P3 przenoszę z PREREG_079 bez zmian.
   - **Ujawnienie:** widziałem już liczby opisowe z REVIEW_080 (ρ62 ≈ 0.79, D_net − D_code = −0.013 i +0.060), więc P1 i P3 nie są już niezależnymi testami.
   - Nowe predykcje, wprost poinformowane przez REVIEW_080, testujące moją diagnozę V5:
     - **P4:** po zagęszczeniu rozrzut ρ j22 między 9 węzłami (max/min, oba ramiona) wynosi ≤ 1.04. W REVIEW_080 było to 1.11 i 1.06.
     - **P5:** ρ(j22, orig, w pierwiastku kodu) > 1.10, czyli kierunek „sieć > kod” dla j22 się utrzymuje.

## 1. Zamrożony kod (`research/badacz/2026-11-21/code/`)

| plik | SHA-256 |
|---|---|
| `rate_dump_081.jl` (nowy) | fbbce938b7b798a18500d16d9795acfb958dc66e40ed73e7715fb57a03d0e0ee |
| `analysis_081.py` (z `analysis_079.py`; zmiany oznaczone [081]) | a11b1bab3b4170201ae66cf536983043a69c28a799c97ec3e97ef0cd1a34ba0d |
| `run081.sh` (nowy) | 14ad33e93fe1acb1a8e8e1e950ed5f8251b91bf018653dd6996010ef3cc9e29f |
| `run_net_079.py` (bez zmian) | eb76ab846dbe8ee9b3b748f979fa37882f697a27c433fa813269e110d76d806b |
| `net_rate_079.py` (bez zmian) | 866f90fc75d453751b9d7a1906a3718c44a9337c32f18574a5a1767319fef763 |
| `prym_rate_patch_079.py` (bez zmian) | 93989e68411ff7d641bd780e6d902fa495eaef892bfe954cef13a9c744b7fac1 |
| `cfg079_orig.dat` / `cfg079_e5.dat` (bez zmian) | 50478cee… / d0fe761f… (jak w PREREG_079) |

## 2. Plan i koszt

- 38 wywołań Julii z eksportem (dwie kolejki równolegle) oraz 43 przebiegi sieci.
- Eksport z V2_EXACT oznacza ~22000 punktów × 2 wywołania `evolution_system!` na przebieg. Szacunek łączny: 30–90 min CPU.

## 3. Ujawnienie przed zamrożeniem

- Nowy driver nie był uruchamiany; żadnych przebiegów 081.
- Analiza 081 to analiza 079 z oznaczonymi zmianami bramek i nowymi predykcjami P4 i P5. Liczb z REVIEW_080 nie używam do niczego poza kalibracją progów V3 (szum zmierzony) i sformułowaniem P4/P5 (jawnie oznaczone).
- Usterka techniczna drivera przed uzyskaniem danych to odnotowane odchylenie, bez oglądania wyników.

## 4. Granice i audyt

- Granice jak w PREREG_079 §8.
- I1 zewnętrzne: REC13 lub AUD3.
