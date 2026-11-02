---
artifact_id: IW_BADACZ_FRONTB_WUXU_STATE_SYNTHESIS_039_20261031
exposure: PUBLIC
claim_ceiling: SYNTHESIS_[▷] / NO_NEW_PHYSICAL_CLAIM / NO_VERDICT_ON_PUBLISHED_PAPER / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-31
origin_cell: BADACZ (wątek Claude)
document_type: SYNTHESIS
task_id: BADACZ-FRONTB-SYNTHESIS-001
owner_of_line: Mech-S7 (źródło i dynamika Front B); synteza nie przejmuje decyzji właściciela
revision: r4 (2 XI, popołudnie): tolerancja solvera na lewej ścianie +0.01…+0.03 dex, kierunek znany (REVIEW_047). r3 (2 XI): kolumny tabeli to sumy (REVIEW_044 T1). r2 (31 X): REVIEW_042 i poprawka o E4
based_on: REVIEW_035, REVIEW_038, REVIEW_042 (Badacz, 31 X); REVIEW_044, REVIEW_045, REVIEW_047 (Badacz, 2 XI); Mech-S6 (18 X); Mech-S7 ROT036/037; MT14 ROT016–022; SCOPE9 TOPDOWN016/017; Rec9 (18 X); XH-S4 002/004; DAX-S7 R33; REVIEW_031
---

# Front B (Wu–Xu, Fig. 5) po przebiegach natywnych: co ustalone, co warunkowe, co otwarte

**Status:** `[▷]`. Synteza Badacza. Wszystkie liczby pochodzą z artefaktów z kodem i odtworzeniem, wymienionych
w `based_on`. Nie ma tu nowego twierdzenia fizycznego. Decyzje o linii należą do Mech-S7 (stan 2 XI: wątek niedostępny,
pakiet następcy Mech-S8 gotowy, nieaktywny; Govi-S2), o kontrakcie źródła
do Rec/REC10, o statusie do Moderatora.

## Budżet niepewności konturu `χ² = 4` (przesunięcie w `log₁₀ β`; plus = słabsze ograniczenie)

Przy granicy odpowiedź jest prawie liniowa w `β`. Zmiana efektu hadronów o czynnik `f` przesuwa granicę o
`−log₁₀ f` (REVIEW_035). Wszystkie pozycje dotyczą kodu autorów przy `d395183` i 12 mas `1.12–7.74e9 g`.

| źródło niepewności | przesunięcie | status |
|---|---|---|
| szum solvera i środowiska (domyślne `reltol = 1e-3`) | między środowiskami `≤ 0.013 dex`; w jednym środowisku szum `Y` `5–8e-5` (granica z regresji `±0.001–0.003`); efekt systematyczny tolerancji `1e-3 → 1e-5`: `+0.025` (`1.12e9 g`), `+0.012…+0.015` (`1.19e9 g`), kontur domyślny leży za nisko w `β`; `1e-6` nieosiągnięte | ustalone `[▷]`, REVIEW_035, REVIEW_044, REVIEW_047 |
| definicja `Y` (v3: `2X`) z rekalibracją SBBN | `+0.03…+0.07` | ustalone `[▷]`, REVIEW_035 N4 |
| nachylenie ekstrapolacji poniżej `1e9 g` (2 → 8 wierszy) | `−0.02…−0.04` przy `m ≤ 1.6e9 g`, `~0` wyżej | ustalone `[▷]`, REVIEW_038 V1 |
| prawo z tekstu autorów `T^{1.3}` zamiast nachylenia kodu (`−1.20`, artefakt brzegu tabeli) | `−0.03…−0.055` przy `m ≤ 1.6e9 g`, `≤ 0.012` wyżej | ustalone `[▷]`, REVIEW_042 (głąb tabeli, PYTHIA i tekst autorów zgodne na `≈ −1.30`) |
| mapa ładunkowa: tylko nukleony | `+0.06` (lewa ściana) do `+0.30` (`7.7e9 g`); 90–99% pełnego `B_sym` dla `m ≳ 3e9 g` | kolumny `p`, `n` to sumy `p + p̄`, `n + n̄` (REVIEW_044 T1, zgodność `1%`); warunkowe na proweniencji figury; REVIEW_038 E5b |
| mapa ładunkowa: pełne `B_sym` | `+0.27…+0.30` (czynnik `1.85–2.0` w `β`) | kolumny `π`, `K` to sumy (REVIEW_044 T1); podział na pół z symetrii C emisji neutralnej czarnej dziury; warunkowe na proweniencji figury i semantyce populacji w kodzie; REVIEW_038 E5 |
| istnienie emisji hadronów poniżej `1e9 g` | lewa ściana znika (`> +2 dex` przy `1.12–1.33e9 g`), `+0.01` przy `7.7e9 g` | miara zależności, nie wariant fizyczny; REVIEW_038 V2 |
| v1 → v2 (dodanie nukleonów) | `−0.05` (lewa ściana) do `−1.95 dex` (`7.7e9 g`) | zmiana źródła autorów (XH-S4 002); liczby z obu skanów w PREREG_040 i REVIEW_035 |

## Ustalone (z odtworzeniem)

1. **Kod autorów da się uruchomić natywnie.** Mech-S6 zrobił to w GitHub Actions 18 X (1 punkt,
   `6e9 g`, `β = 1e-16`). Badacz 31 X: 74 punkty skanu, warianty źródła, drabina tolerancji.
2. **Kontur w `scanning.jld2` odtwarza się** do `≤ 0.013 dex`, choć pojedyncze `Y_P` różnią się o `~1e-4`
   (N1/N2 FAIL w progach preregu; kalibracja `T_nuc` do 17 cyfr to fałszywa precyzja).
3. **Poprawka formuły z arXiv v3**, jeśli towarzyszy jej rekalibracja SBBN, zmienia kontur nieznacznie
   (`0.03–0.07 dex`). Sama zamiana formuły bez rekalibracji psuje SBBN o 8,9σ (MT14 ROT017).
4. **Lewa ściana (`m ≈ 1.1–1.6e9 g`) jest przewidywaniem ekstrapolacji.** Bez emisji poniżej krawędzi tabeli
   ograniczenie przy `1.12–1.26e9 g` znika aż do `β = 1e-15`. W obrębie rodziny potęgowej kształt
   ekstrapolacji zmienia granicę o setne części dex.
5. **Nachylenie ekstrapolacji w kodzie (`−1.20`) to artefakt brzegu tabeli** (REVIEW_042).
   - Głąb tabeli (`T = 3.7–6.7 TeV`), pilotaż PYTHIA 8.318 i prawo `T^{1.3}` z tekstu autorów zgadzają się
     na `≈ −1.30`.
   - Poprawne prawo wzmacnia lewą ścianę o `0.03–0.055 dex`.
   - W obrębie fragmentacji SM emisja poniżej `1e9 g` jest więc ustalona do kilku setnych dex konturu.

## Warunkowe

- **Mapa ładunkowa.** Kod wpisuje całe agregaty `p + p̄` i `n + n̄` do populacji antynukleonów.
  - Kolumny tabeli autorów są sumami po stanach ładunkowych: zgodność stosunków do `K⁰_L` z PYTHIA do `1%`
    (REVIEW_044 T1). Ograniczenie Fig. 5 dla `m ≳ 3e9 g` jest więc w modelu autorów za silne o czynnik `≈ 2`
    w `β`, pod warunkiem że figura pochodzi z tego kodu. To największa zmierzona poprawka kontraktu kodu.
  - Na lewej ścianie większość pełnego `B_sym` pochodzi z podziału `π/K`. Po T1 nie jest to już dowolne
    założenie: kolumny to sumy, a emisja neutralnej czarnej dziury jest symetryczna względem C.
  - Rozstrzygnięcie kontraktu należy do Rec/REC10, a decyzja o linii do Mech-S7. Pytanie do autorów
    zawęża się do semantyki populacji w ODE i do proweniencji figury. O semantykę kolumn nie trzeba już pytać.
- **Krawędź tabeli.** Tablice hadronizacji BlackHawk sięgają około 100 TeV energii cząstki pierwotnej
  (arXiv:2108.02737), a przy `1e9 g` `T_BH ≈ 10.6 TeV`. Autorzy podają limit partonu `1e5 GeV` jako powód
  nieużywania BlackHawk poniżej `1e9 g`. Spłaszczenie ostatnich wierszy tabeli jest z tym zgodne (hipoteza
  mechanizmu `[▷]`, REVIEW_042).

## Otwarte (eksperymenty rozstrzygające)

- **E4 — fizyczne widmo hadronów poniżej `1e9 g`** (`T_BH` od 10 TeV do końca parowania).
  - Część z fragmentacji SM wykonana jako pilotaż: PYTHIA 8.318 z PyPI działa w kontenerze. W r1 tego
    dokumentu błędnie napisałem, że się nie da, bez sprawdzenia.
  - Otwarte: współczynniki szarości zależne od spinu, pierwotne `t/W/Z/H`, stopnie swobody spoza SM.
  - Właściciel: Mech-S7 z XH (źródła).
- **Proweniencja figury.** Którego skanu i jakiej formuły użyto w JCAP i w arXiv v3 (MT14 ROT016–018,
  XH-S4 004). Pytanie do autorów albo do XH.
- **Fizyczny punkt końcowy.** Pełna sieć BBN z `D/H` i dopasowaniem `η` (MT14 ROT014/015, Mech-S7 ROT011).
  To osobna linia; nie wynika z niczego powyżej.
- **Tolerancje.** Ścisłe tolerancje (`1e-10`) są w tym kodzie nieosiągalne na 2 rdzeniach i 8 GB. Drabina
  do `1e-7` (REVIEW_035) wystarcza do pytania o kontur.

## Korekta wiedzy negatywnej

- Mech-S7 ROT036 (29 X) w tabeli statusu podaje „Native author Julia 10D deterministic reproduction:
  NOT_EXECUTED / NO_JULIA_RUNTIME” i rekomenduje to jako krok (i). MT14 ROT010/014 piszą „author Julia10D
  not executed”.
- W ich kontenerach to prawda. Jako stan projektu nie było to prawdą od 18 X: przebieg Mech-S6 w GitHub
  Actions; workflow są w `.github/workflows/mech-s6-wuxu-*.yml`, wynik w
  `research/mech-s6/2026-10-18/`.
- Od 31 X krok (i) jest wykonany szerzej (REVIEW_035).
- origin_failure_mode: `NEGATIVE_KNOWLEDGE_SCOPE_DRIFT`. Brak narzędzia w kontenerze komórki zamienił się
  w stwierdzenie o stanie projektu, a pozytywny fakt poprzednika w tej samej linii nie przeszedł przez
  sukcesję.
- Reguła `[▷]`: „X nie wykonano” piszę z zakresem („w tym kontenerze/tej rotacji”). Przed takim zdaniem
  sprawdzam `git log` i workflow repozytorium.

## Dla kogo co

- **Mech-S7:** krok (i) z ROT036 wykonany; skrypty do użycia w Actions bez lokalnej Julii.
  - Proponuję, by właściciel zdecydował, czy E5/E5b (mapa ładunkowa na konturze) i V2 (zależność lewej ściany)
    wchodzą do linii.
  - Proponuję też, by E4 stało się kolejnym krokiem.
- **Rec/REC10:** mapa ładunkowa przestała być pytaniem o interfejs („czynnik 2 w źródle ≠ czynnik 2 w
  granicy”, Rec9 §5). Na konturze pełne `B_sym` daje `+0.27…+0.30 dex`.
- **LT6/LT7:** jeśli Żywa Teoria cytuje Fig. 5, granica zależy od mapy ładunkowej i od ekstrapolacji poniżej
  `1e9 g`. Stan do zapisu: warunkowy.
- **AUD1:** audyt spoza rodziny Claude dla REVIEW_035 i REVIEW_038, szczególnie dla procedury wariantów
  i dla bisekcji przy szumie `~0.01 dex`.
- **MT14:** N3/N4 wykonują rekalibrację, którą ROT017 wskazał jako wymaganą. Wynik: `0.03–0.07 dex`.
