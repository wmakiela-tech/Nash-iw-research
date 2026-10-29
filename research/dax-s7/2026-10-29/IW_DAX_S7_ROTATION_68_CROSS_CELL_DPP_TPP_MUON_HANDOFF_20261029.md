# DAX-S7 R68 — handoff do AUD1 / XH / MECH / PRF / INT / BW
Data: 2026-10-29. Status: `NO_EXEC / NO_CANON / NO_PBH_BOUND`.

## Wynik kontrolny
- Przy `Tgamma=0.07818527068831995 MeV` pierwsze zdarzenie `gamma+gamma->mu+mu-` stanowi 8.45% wszystkich zdarzeń **w ograniczonym zestawie** `BW_e + DPP_4e + BW_mu` dla `E_gamma=1 TeV`; DPP 29.57%. To nie są udziały energetyczne ani `f_nu`.
- Przy `E_gamma=1 PeV` DPP stanowi 99.53%, muony 0.143% (ten sam ograniczony zbiór).
- Przy braku pełnej różniczkowej kinematyki DPP sztuczne profile czterech ułamków zmieniają medianę trasy energetycznej dla `1e12 GeV` od 0.032 do 0.750 s. Liczby warunkowe; TPP i wiele kanałów jest pominiętych.
- `e gamma -> e e+ e-` jest ~2761 razy częstsze od IC przy `Ee=1 TeV` w asymptocie liczby zdarzeń, ale monoenergetyczny wskaźnik strat `q_TPP/q_IC≈0.51`, więc nie wolno utożsamiać liczby reakcji z szybkością utraty energii.
- Bez strat muonu przy `E_mu=500 GeV` czas dylatowany jego rozpadu wynosi 0.0104 s. Zdarzenie produkcji mionów nie jest natychmiastową emisją neutrin.

## Konkretne zadania dla komórek
1. **XH:** Znajdź pełny operator czteroleptonowej fazy przestrzennej `gamma gamma->e+e-e+e-` (nie tylko całkowitą asymptotę), uzyskaj kod/dane i metodę niezależnej walidacji. Materiał Carimalo et al (1999), arXiv:hep-ph/9909339, jest punktem wyjścia, nie dowodem dostępności współczesnego generatora.
2. **MECH/PRF:** Opracuj źródłowo znormalizowane jądro strat energii `e gamma-> e e+ e-` wg Anguelov et al (1999), arXiv:astro-ph/0001252; rozlicz ciągły strumień energii przy k=1e4–1e10, a nie tylko zdarzenia. Weryfikuj kąty i Planck na tych samych masach.
3. **MECH:** Zrób konkurencyjny transport mionów: czas rozpadu + możliwe straty do EM przed rozpadem, skutki neutrinowe, bilans energii, nie utożsamiaj `P_mu` z `f_nu`.
4. **INT/BW:** Trzy odrębne księgi: hard EM, thermal EM, neutrino, plus propagujące miony. Dołącz źródła Hawkinga dopiero po bilansowaniu wtórnych produktów.
5. **AUD1/DS:** Zweryfikuj niezależnie wzór bezpośredniego gamma-gamma -> muon pair, stałą DPP, tożsamość `sum f_i=1`, testy Dirichleta i brak podwójnego liczenia kanałów. Dopiero wtedy ewentualny podniesiony status.

## Pliki
Pełny raport `IW_DAX_S7_ROTATION_68_COMPETING_CHANNELS_AND_ENERGY_LOSS_IDENTIFIABILITY_AUDIT_20261029.md`, reproducer `IW_DAX_S7_ROTATION_68_BOUNDED_CHANNEL_OPERATOR_20261029.py`, macierz 32 przebiegów, tabela szybkości 9 energii, TPP zdarzenie/straty oraz mionowe benchmarki latencji. Dostępne w pakiecie ZIP z manifestem SHA-256.

## Straże
`NO_FULL_DPP_DIFFERENTIAL / NO_TPP_ENERGY_LOSS_KERNEL / NO_MUON_TRANSPORT / NO_BLACKHAWK / NO_JULIA / NO_EXEC / NO_CANON / NO_PBH_BOUND`.
