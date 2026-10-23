# IW/NASH — DAX-S7, obrót 35
## Źródłowa weryfikacja reszty adiabatycznej w tablicy Wu–Xu
**Data:** 2026-10-23
**Status:** SOURCE-TABLE QUANTIFIED / LOCAL DERIVATIVE TEST / NO FULL ODE / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE

### Pochodzenie danych
Repozytorium Fenyutanchan/Primordial-Black-Hole, arXiv-2509.05618/data/ext/N_around_m_e.csv (1000 wierszy, temperatura 0.01400299–10.00000000 MeV). Funkcje Nᵨ(T) i Nₛ(T) w tool_script-N_relativistic_species.jl używają dla T <= 10 MeV oddzielnych interpolacji liniowych po log(T/MeV) kolumn odpowiednio 2 i 3. W każdym otwartym przedziale pomiędzy węzłami obliczono dokładne nachylenia interpolacji, a następnie logarytmiczne pochodne w środku geometrycznym przedziału.

### Równania
Oznaczenia r=dln(g_rho)/dlnT, s=dln(g_s)/dlnT. Kod bez iniekcji PBH: C_code=-4+r/(3+s). Warunek zachowania entropii s_ent*a^3=const: C_ad=-3(4+r)/(3+s). Różnica Delta=C_code-C_ad=4(r-s)/(3+s). Reszta produkcji entropii współporuszającej według kodu: dln(s_ent*a^3)/dlna=4(r-s)/(4+r). Są to tożsamości termodynamiczne, nie nowe twierdzenia.

### Wyniki numeryczne z tablicy
| T [MeV] | r | s | Delta | |Delta/C_ad| |
|---:|---:|---:|---:|---:|
| 0.09973 | 0.717911 | 0.599810 | 0.131230 | 3.3377% |
| 0.30044 | 0.350177 | 0.318562 | 0.038106 | 0.9690% |
| 0.50025 | 0.140417 | 0.132253 | 0.010425 | 0.2629% |
| 1.00242 | 0.036163 | 0.035271 | 0.001175 | 0.0295% |
| 0.11114 | 0.792294 | 0.668864 | 0.134571 | 3.4341% |

Maksimum |Delta| w 999 przedziałach: ~0.134571 przy T~0.11114 MeV. Przy 0.03 MeV Delta~ -0.00004163. Występują przedziały z niezerową resztą, więc warunek r=s nie zachodzi w użytej tablicy.

### Ograniczenia
To lokalny audyt pochodnych interpolacji, bez uruchamiania Julia ODE, bez propagacji do T(a), X_n ani Yp. Względna różnica 3.43% dotyczy pochodnej dln rho/dln a, nie 3.43% błędu temperatury czy helu. Przy PBH iniekcji wymagane osobne, spójne wyprowadzenie członu źródłowego. Przy dokładnej implementacji należy zweryfikować pochodne ForwardDiff na węzłach i interpolację odwrotną rho->T; próbki w środku przedziałów unikają nieciągłości pochodnych. Żaden wniosek o granicach PBH ani nowości fizycznej.

### Falsyfikator
Zastąpić człon chłodzenia adiabatycznym w SBBN-only przy niezmienionych tablicach i solverze; porównać T(a), X_n(T_nuc) i trzy mapowania Yp. Dopiero później pełne PBH i wyniki publikacji. Dodatkowo porównać źródłowy model termodynamiczny z niezależnym równaniem zachowania energii, ponieważ nie można automatycznie przyjmować, że założenie adiabatyczności wyczerpuje model.
