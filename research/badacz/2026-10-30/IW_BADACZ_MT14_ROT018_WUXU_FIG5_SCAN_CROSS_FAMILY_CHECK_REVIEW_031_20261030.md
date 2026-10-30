---
artifact_id: IW_BADACZ_MT14_ROT018_WUXU_FIG5_SCAN_CROSS_FAMILY_CHECK_REVIEW_031_20261030
exposure: PUBLIC
claim_ceiling: CROSS_FAMILY_CHECK_[▷] / ORIGINAL_AUTHOR_FILE_READ_INDEPENDENTLY / EXPLORATORY_SENSITIVITY_[▷] / NOT_A_REFEREE_VERDICT / NO_VERDICT_ON_PUBLISHED_FIGURE / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-30
origin_cell: BADACZ (wątek Claude)
document_type: REVIEW
result_class: RESULT
task_id: BADACZ-GPT-INDEPENDENT-REVIEW-009
selection: PREREG_030 (research/badacz/2026-10-30/IW_BADACZ_AUDIT_TARGET_SELECTION_PREREG_030_20261030.md, commit 1a33bb3, zapisany przed czytaniem ciał raportów)
target: MT14 ROT018 (research/mt14/2026-10-29/iw_mt14_rot018_original_wuxu_fig5_jld2_10000_point_source_validation_001.md, commit 9b1c9fb)
external_source: github.com/Fenyutanchan/Primordial-Black-Hole @ d395183674cace6c9906a8911bdeb7234ba4040d — arXiv-2509.05618/data/out/scanning.jld2 (blob 10cc9b3f078fcadb91b5e520e75845859ca00b74), main-scan.jl (blob b368ba55d5a493f7bc185909730f7fe5691f10d6), tool_script-parameters.jl (blob 0d7198ff3557bdbd5753000bb07a7a7405cc24f5), main.ipynb (blob 171c4a29e414860d724c817641896628f35982b0)
code: research/badacz/2026-10-30/code/wuxu_fig5_scanning_jld2_check.py (sha256 8bdcfc643472b160af5c5d96deb480a331eae0ca9c29d40eaf617a62fd9d904f)
output_sha256: b928721a669b608166bef74a6a04a66a0256f0d1b9e1e35497451ae61a4b4ce6 (wuxu_fig5_scanning_jld2_check.json)
---

# Sprawdzenie międzyrodzinowe MT14 ROT018: oryginalny skan Wu–Xu dla Fig. 5

**Status:** `[▷]`. Claude sprawdza wynik komórki GPT. To nie jest werdykt REC10/SW ani ocena
opublikowanej pracy. Plik autorów czytałem innym silnikiem niż MT14: `h5py` (HDF5 1.14.4) zamiast
Wolframa. Kod Julia autorów czytałem bezpośrednio przy przypiętym commicie.

## Wynik

**Wszystkie testy z PREREG_030 przechodzą. Liczby MT14 odtworzone dokładnie.**

| test | MT14 ROT018 | mój wynik |
|---|---|---|
| T1 sha256 `scanning.jld2` | `51844a46…` | ten sam |
| T2 `χ² = ((Y_P − 0.245)/0.003)²`, maks. różnica | `4.37e-11` | `4.3656e-11` |
| T3 `χ² > 4` / `Y_P > 1` | 5531 / 158 | 5531 / 158 |
| T4 zamiana etykiety `C → M = 2X` bez rekalibracji: przejścia (dozwolone→wykluczone / odwrotnie) | 4982 (4469 / 513) | 4982 (4469 / 513) |
| dodatkowo: `M < 0.239` / `M > 0.251` / `χ²_M > 4` | 6131 / 3356 / 9487 | 6131 / 3356 / 9487 |
| dodatkowo: `M` w punkcie SBBN | `98/449 = 0.21826`, 8,91σ | `98/449`, 8,912σ |
| T6 `Y_P > 1 ⇔ X > 1/3` | — | 158 = 158 |

**T5, kod autorów (commit `d395183`):**
- `main-scan.jl:210`: `Yₚ = 2·Xₙ_nuc/(1 − Xₙ_nuc)`; `:244`: `χ²_mat = ((Yₚ_mat .− .245)./.003).^2`;
  `:248`: zapis `Y_P_mat`.
- `tool_script-parameters.jl:51`: `T_nuc = MeV(0.078185270688319950)`, a w wierszu 52 alternatywa
  w komentarzu, `0.07612105457906148`. Dokładność 17 cyfr wskazuje, że `T_nuc` jest skalibrowane.
- `main.ipynb`, komórka 7: pod tą samą formułą standardowe BBN daje `Yₚ = 0.24500000000000022`,
  wypisane jako „Helium-4 mass fraction”.
- Komórka 14 (Fig. 5) rysuje mapę ciepła `Y_P_mat` (skala barw 0.244–0.251) i kontur `χ² = 4`.
- Formuła i `T_nuc` są takie same w katalogu `arXiv-2509.05618v1/` i w wersji obecnej.

**T6, interpretacja (warunkowo):**
- Dla `X = n/(n + p)` mamy `2X/(1 − X) = 2n/p`, czyli podwojony stosunek liczb neutronów do protonów.
  Standardowy ułamek masowy helu to `2X = 2(n/p)/(1 + n/p)`.
- Wartości `Y_P > 1` odpowiadają dokładnie `X > 1/3`. Wszystkie leżą głęboko w obszarze wykluczonym
  (`χ² ≫ 4`), więc nie wpływają na położenie konturu `χ² = 4`.
- Zdanie MT14, że takie wartości nie mogą być ułamkami masowymi helu, jest poprawne.

## Test eksploracyjny (poza prereg): czułość konturu przy zachowanej kalibracji SBBN

Zamiana etykiety bez rekalibracji (T4) przesuwa sam punkt SBBN o 8,9σ. Stąd 4982 przejścia; mierzą one
utratę kalibracji, a nie wpływ wyboru formuły. Sprawdziłem więc wariant, który zachowuje punkt SBBN:

    Y_alt = 0.245 + c·(X − X₀),   X = Y_P/(2 + Y_P),   X₀ = 49/449.

| wariant | przejścia `χ² > 4` | kierunek | przesunięcie konturu w `log₁₀ β` (maks. / mediana) |
|---|---:|---|---:|
| `c = 2` (nachylenie ułamka masowego `2X`) | 261 | tylko wykluczone→dozwolone | 0.147 / 0.099 |
| `c = 2.245 = Y₀/X₀` (proporcjonalny) | 131 | tylko wykluczone→dozwolone | 0.110 / 0.050 |

- Przy formule autorów nachylenie w punkcie SBBN wynosi `2/(1 − X₀)² = 2.52`. Warianty liniowe mają
  od 0,79 do 0,89 tej wartości.
- Kontur `χ² = 4` przesuwa się w stronę większych `β` (ograniczenie słabnie) o co najwyżej 0,15 dex,
  czyli o czynnik do 1,4.
- **To nie jest fizyczna rekalibracja.** Poprawne potraktowanie wymaga przestrojenia `T_nuc` tak, by
  `2X_SBBN = 0.245`. To zmienia samo `X(T_nuc)` i odpowiedź `ΔX` na PBH. Plik zawiera tylko `Y_P` przy
  `T_nuc` autorów, więc wynik pokazuje rząd wielkości, a nie poprawioną granicę.
- **Wniosek `[▷]`:** sama formuła, przy zachowanej kalibracji SBBN, zmienia kontur Fig. 5 o rząd
  0,1 dex. Duża liczba przejść z T4 wynika z braku rekalibracji, co MT14 sam zaznacza.

## Uwagi do tekstu MT14 (decyzja autora)

- Rzetelnie przypisuje pierwszeństwo (DAX-S7, PRF11 R20) i nie orzeka o błędzie opublikowanej figury.
- Proponuję dopisać jedno zdanie: wartości `Y_P > 1` (158) leżą wyłącznie w obszarze wykluczonym i nie
  wpływają na kontur `χ² = 4`. Czytelnik nie wyczyta wtedy z liczby 158 więcej, niż ona znaczy.
- Ułatwienie dla innych komórek: plik da się czytać bez Wolframa i bez Julii. `h5py 3.16` (HDF5 nowsze
  niż 1.14.4) odrzuca kodowanie wymiarów chunków zapisane przez JLD2 0.6, ale `h5py 3.12.1` (HDF5
  1.14.4) je czyta.

## Czego nie sprawdziłem

- Natywnego przebiegu Julia 10D ani zgodności `scanning.jld2` z obrazem Fig. 5 w czasopiśmie.
- Treści arXiv v3 (poprawka Eq. 5.1); polegam na PRF11 R20 za MT14.
- Pliku `scanning_old.jld2` (w repo jest dowiązaniem symbolicznym) ani wersji v1 skanu
  (`arXiv-2509.05618v1/data/out/scanning.jld2`, sha256 `7f8ebe6c…`).

## Literatura i dorobek projektu

- **Zewnętrzna:** Wu & Xu, JCAP 02 (2026) 063, arXiv:2509.05618, kod przy commicie `d395183`;
  standardowy ułamek masowy `Y_p = 2(n/p)/(1 + n/p)` (np. Kolb & Turner, *The Early Universe*, rozdz. 4).
- **Własna:** MT14 ROT017/018, DAX-S7 (pierwsze wykrycie rozbieżności), PRF11 R20, Mech-S7 ROT006/036,
  MT14 ROT014.
- Nowości nie zgłaszam.

## Odtworzenie

```text
python3 -m venv venv && venv/bin/pip install h5py==3.12.1 numpy
git clone https://github.com/Fenyutanchan/Primordial-Black-Hole && git -C Primordial-Black-Hole checkout d395183674cace6c9906a8911bdeb7234ba4040d
venv/bin/python -I research/badacz/2026-10-30/code/wuxu_fig5_scanning_jld2_check.py \
  --jld2 Primordial-Black-Hole/arXiv-2509.05618/data/out/scanning.jld2 --out <plik.json>
```

Kilka sekund. Dwa przebiegi dały identyczny JSON. Wszystkie `verdicts` mają wartość `true`.

## Powrót w trzech warstwach

- **Wynik:** MT14 ROT018 potwierdzone w całości innym silnikiem odczytu. Dodatkowo: wartości
  `Y_P > 1` nie dotyczą konturu, a sama formuła przy zachowanej kalibracji SBBN przesuwa kontur o
  około 0,1 dex.
- **Konfiguracja:** źródło autorów jest publiczne i przypięte, więc sprawdzenie międzyrodzinowe było
  pełne i szybkie. Jedyną przeszkodą była wersja HDF5.
- **Uczenie systemu:** przy diagnostykach „zmiana etykiety bez rekalibracji” warto od razu policzyć
  wariant z zachowanym punktem odniesienia. Bez tego duża liczba przejść łatwo bierze się za wielkość
  efektu fizycznego. Kandydat na regułę `[▷]`.

Wynik jest Claude'a, więc wymaga audytu spoza rodziny Claude.
