# DAX-S7 — obrót 36: skumulowana reszta chłodzenia Wu–Xu

**Data:** 2026-10-23  
**Status:** SOURCE-TABLE INTEGRATED / BACKGROUND-ONLY / NO FULL JULIA ODE / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE

## Dane źródłowe
Repozytorium Fenyutanchan/Primordial-Black-Hole, `arXiv-2509.05618/data/ext/N_around_m_e.csv` (1000 punktów od 0,014 do 10 MeV), wczytane przez GitHub connector. `tool_script-N_relativistic_species.jl` interpoluje osobno g_rho i g_s liniowo w log(T). Wartości obliczone z dokładnych liniowych odcinków tablicy; całkowanie Simpsona na każdym odcinku po log(T). Nie uruchomiono Julia.

## Równania
W granicy bez iniekcji PBH: `C_code=dln(rho)/dln(a)=-4+r/(3+s)`, gdzie `r=dln(g_rho)/dln(T)` i `s=dln(g_s)/dln(T)`. Z `rho∝g_rho T^4` wynika `dln(a)/dln(T)=(4+r)/C_code`. Dla zachowania entropii `a_ad(T)=(T0/T)*(g_s(T0)/g_s(T))^(1/3)`. Start `T0=10 MeV`, `a(T0)=1`.

## Wyniki
| T [MeV] | ln(a_code/a_ad) | a_code/a_ad-1 | (s_ent a_code³)/(s_ent(T0))-1 |
|---:|---:|---:|---:|
| 1.00 | 0.00007030 | 0.0070% | 0.0211% |
| 0.50 | 0.00087155 | 0.0872% | 0.2618% |
| 0.30 | 0.00397363 | 0.3982% | 1.1992% |
| 0.10 | 0.03689246 | 3.7581% | 11.703% |
| 0.03 | 0.05236358 | 5.3759% | 17.010% |

W ostatnim wierszu procenty wyliczono z `exp(drift)-1` oraz `exp(3*drift)-1`. Wartości w tabeli przy najbliższym węźle T; nie są precyzyjnie na podanych zaokrąglonych temperaturach. Maksimum drift w pełnej tablicy ~0.052368 przy 0.014 MeV.

## Granice i weryfikacja
Jest to porównanie dwóch trajektorii termodynamicznych T(a), NIE pełna ewolucja t(a), X_n(T), Yp ani skan PBH. Fizyczna interpretacja wymaga kontroli zgodności tablic g*(T), sposobu bilansu energii oraz założeń o adiabatyczności, a dla PBH także członu iniekcji. Rachunek stanowi standardowy test zachowania entropii (host-theory subtraction), nie nową teorię. Falsyfikator: wykonać niezależny solver SBBN na tych samych tabelach, odtworzyć log(a) w podanych temperaturach, sprawdzić zmianę X_n i Yp, a następnie porównać wyniki kodu z publikacją. Bez EXEC nie zmieniać kanonu ani ograniczeń PBH.
