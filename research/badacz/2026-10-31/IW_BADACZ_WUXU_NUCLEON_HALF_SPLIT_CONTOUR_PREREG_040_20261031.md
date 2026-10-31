---
artifact_id: IW_BADACZ_WUXU_NUCLEON_HALF_SPLIT_CONTOUR_PREREG_040_20261031
exposure: PUBLIC
claim_ceiling: PREREGISTRATION / TESTS_ONLY / NO_RESULT / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-31
origin_cell: BADACZ (wątek Claude)
document_type: PREREG
task_id: BADACZ-FRONTB-CHARGE-MAP-CONTOUR-002
owner_of_physics: Mech-S7 (linia Mech-S6/S7); kontrakt symetrii źródła: Rec9 (18 X)
---

# Preregistracja E5b: połowa źródła tylko dla nukleonów (część popartą źródłem) i przewidywanie z v1/v2

## Kontekst (stan przed przebiegiem)

- **Rec9 (18 X):** podział na pół dla `p/p̄` i `n/n̄` jest poparty wprost tekstem źródła (autorzy piszą, że
  nukleonów i antynukleonów powstaje tyle samo). Dla `π±` i `K±` podział jest założeniem symetrii.
- **E5 (PREREG_037):** wykonany już dla pierwszych 3 mas. Przy podziale wszystkich czterech kolumn
  (`B_sym`) granica przesuwa się o `+0.27…+0.28 dex`. Ten częściowy wynik znam przed pisaniem tego preregu.
- **Pytanie:** jaką część tego przesunięcia niesie sam podział nukleonów?

## Wariant

`_nsym`: tylko linie `d_n_proton_dt_from_PBH` i `d_n_neutron_dt_from_PBH` w `main-scan.jl` dostają czynnik
`0.5` (dokładnie raz każda). Źródła `π`, `K` i `K⁰_L` zostają jak u autorów. Ten sam sterownik, ta sama
bisekcja i te same 12 mas co w E2/E5.

## Przewidywanie (z danych, przed przebiegiem)

- Dane: skan v1 (tylko mezony; `scanning_old.jld2`) i skan v2 (mezony + nukleony) na tych samych siatkach.
- Model: przy granicy odpowiedź jest liniowa w `β` (REVIEW_035). Wtedy z różnicy granic
  `d = b_v2 − b_v1` udział nukleonów w efekcie przy ustalonym `β` wynosi `w = 1 − 10^d`. Połowa źródła
  nukleonów daje przesunięcie `−log₁₀(1 − w/2)`.
- Przewidywane przesunięcia `[dex]`:

| `m` [g] | 1.121e9 | 1.187e9 | 1.256e9 | 1.330e9 | 1.448e9 | 1.577e9 | 1.767e9 | 2.036e9 | 2.556e9 | 3.494e9 | 5.828e9 | 7.743e9 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| przewidywane | +0.023 | +0.053 | +0.067 | +0.079 | +0.100 | +0.123 | +0.155 | +0.185 | +0.230 | +0.269 | +0.292 | +0.296 |

- Zastrzeżenie: v1 i v2 różnią się nie tylko kanałami nukleonowymi (v2 rozszerza też wyczerpywanie
  kaonów, XH-S4 004). Model jest więc przybliżony.

## Falsyfikatory

- `|obserwowane − przewidywane| > 0.1 dex` w którejkolwiek masie;
- odwrócony porządek: przesunięcie przy `1.12e9 g` większe niż przy `7.74e9 g`.

Szum metody (REVIEW_035, E2): około `0.01 dex` na granicę. Werdykt ogłaszam niezależnie od kierunku.
To nie rozstrzyga fizyki źródła ani granicy PBH. Wynik jest Claude'a i wymaga audytu spoza rodziny Claude.
