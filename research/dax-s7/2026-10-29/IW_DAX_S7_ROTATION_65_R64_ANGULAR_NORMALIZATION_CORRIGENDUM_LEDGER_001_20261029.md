# IW/NASH — DAX-S7 — obrót 65 — errata kwadratury R64
Data: 2026-10-29. Status: SOURCE_CODE_CORRIGENDUM / NO_CANON / NO_EXEC / NO_PHYSICAL_PBH_BOUND.

## Potwierdzony błąd własnego skryptu audytowego
Historyczne skrypty DAX-S7 R64, **nie kod Wu–Xu**, pomijają czynnik 1/2 w izotropowej średniej kątowej:
`< (1-mu) sigma > = (1/2) integral(mu=-1..1)[(1-mu) sigma(mu) dmu]`.
Po podstawieniu a=1-mu, R64 całkuje `integral(a=0..2) a*sigma(a) da` zamiast połowy tej całki.
Test sigma=const: stara całka=2; poprawna średnia=1.
Dotyczy R64 `IW_DAX_S7_R64_BREIT_WHEELER_MICROPHYSICS_20261026.py` (`PairRate.kappa_s`) i `IW_DAX_S7_R64_KLEIN_NISHINA_MICROPHYSICS_20261026.py` (`KNFirstScatter.collision_rate_s`).
Wniosek: **R64 rates x2 za duże; R64 first scattering times x2 za małe**.
Minimalny patch: `self.w_angle=weights/2` w PairRate; `self.w_ang=weights/2` w KNFirstScatter.

## Niezależny test
Obliczono jądro Jones/Blumenthal-Gould `F(q,Gamma)=2q ln(q)+(1+2q)(1-q)+(Gamma*q)^2*(1-q)/(2*(1+Gamma*q))` oraz jego moment energetyczny w izotropowym widmie Plancka.
Przy N=190 i Tgamma=0.07818527068831995 MeV, dla 13 energii 1..10^12 GeV: maksymalna względna różnica czasu BG i poprawionego KN = 2.758e-6; test granicy Thomsona przy Ee=1GeV,T=1e-9MeV = 0.999972416.
N=190 vs N=260: max relative BW 5.241e-5, KN 2.002e-5, BG 1.868e-5, moment 5.055e-6.

| Energia | BW first, poprawione | IC first, poprawione | Średni E_gamma_out/E_e w jednym IC |
| --- | ---: | ---: | ---: |
| 1 TeV | 1.62945e-10 s | 2.89301e-10 s | 0.90012 |
| 10 TeV | 1.36440e-9 s | 2.46732e-9 s | 0.91481 |
| 100 TeV | 1.17348e-8 s | 2.15088e-8 s | 0.92574 |
| 1 PeV | 1.02942e-7 s | 1.90639e-7 s | 0.93418 |

## Co falsyfikuje i czego nie rozstrzyga
- Wysokoenergetyczny elektron wypromieniowuje w IC wysokoenergetyczny foton; około 90% jego energii przy Ee=1TeV *pozostaje w nietermicznej kaskadzie*. Pierwsze zderzenie NIE równa się pełnej termalizacji.
- Próg t_BW_first=0.05s dla monochromatycznego proxy E_gamma=T_H odpowiada obecnie M_PBH ~12.6355 g, **nie 6.18 g** z R64. Ułamek pozostałej masy względem Mf=9.58288e9g: 1.31855e-9. Nie jest to próg depozycji.
- Warunkowe okna masowe i czasy opóźnienia z R62–64 zostały obliczone niezależnym modelem rezerwuaru i nie korzystają z błędnego mnożnika kątowego. Nie ulegają automatycznej zmianie.
- Nie uruchomiono oryginalnej Julii ani BlackHawk; nie oszacowano pełnej kaskady ani fizycznych granic PBH.

## Źródła i dane
Wu–Xu public code: https://github.com/Fenyutanchan/Primordial-Black-Hole
Kernel BG/Jones: https://doi.org/10.1093/mnras/stac2712
CSV pełnych 13 punktów: `IW_DAX_S7_ROTATION_65_CORRECTED_BW_KN_AND_BG_ENERGY_MOMENTS_20261029.csv` w tym samym katalogu.
Pełny reproducer, audyt, testy zbieżności N120/N190/N260, skrypty źródłowe R64 (niezmienione), progi oraz manifest SHA-256: lokalny `IW_DAX_S7_ROTATION_65_REPRODUCIBLE_PACKET_20261029.zip`.

Werdykt: `R64_X2_ANGULAR_BUG_CONFIRMED / INDEPENDENT_BG_PASS / FIRST_SCATTERING_NOT_DEPOSITION / NO_PHYSICAL_UPGRADE / NO_EXEC / NO_CANON`.
