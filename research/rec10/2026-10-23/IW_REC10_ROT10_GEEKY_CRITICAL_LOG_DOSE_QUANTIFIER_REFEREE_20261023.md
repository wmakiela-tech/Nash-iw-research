# REC10 ROT10 — krytyczny budżet logarytmiczny: naprawa kwantyfikatora Geeky-S10

**Data:** 2026-10-23  
**Funkcja:** niezależny referee / STRESS / TYPE / HARDEN  
**Status:** `PASS_WITH_MATERIAL_CORRECTION / REPAIR_REQUIRED_SECTION_6`  
**Autorytet:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE`  
**Custody:** lokalny dokument; próby zapisu GitHub i wysłania do Slack BLOCKED. Brak BW ingest i potwierdzonej akceptacji właściciela.

## Źródło i zakres

Źródło właściciela, odczytane w GitHub:
`research/geeky-s10/2026-10-23/geeky_s10_oblique_mixed_reset_exact_dose_phase_001.md`, blob `8c152b690547b1fe2bfa1a63f15cb9cd5510aeba`.

Przedmiotem recenzji jest §6 i relacja do §5.5. Pozostałe źródłowe dokładne wzory i zakres klasycznego modelu nie są awansowane do fizyki.

## Wynik pozytywny: dokładna energia i współczynnik krytyczny

Ustalono `q>1`, `κ∈(0,1]`, `s→0`, `r=κs`, liczbę par `M_s` i dawkę `B_s=2M_s s`. Źródłowa dodatnia macierz pary ma wartość własną Perrona:

`λ_+(r)=1+(q−1)r+O(r²)`.

Energia współczynników obserwacji, przy jednostkowym wektorze Perrona, wynosi dokładnie:

`E_M=s² A_r(λ_+^(2M)−1)/(λ_+²−1)`, gdzie `A_r→1`.

Oznaczmy `a=(q−1)κ` i `c_*=1/a`. Jeśli `B_s=O(log(1/s))`, to

`2M log(λ_+) = aB_s+O(sB_s)=aB_s+o(1)`

oraz `λ_+²−1=2as(1+O(s))`. Ponieważ `aB_s→∞` dla dawki logarytmicznej, uzyskujemy dokładną asymptotykę:

`E_M = [s/(2a)] exp(aB_s)(1+o(1))`.

Próg `c_*` podany przez autora jest prawidłowy jako próg zerowania/rozbieżności dla `B_s=c log(1/s)+o(log(1/s))` z `c≠c_*`.

## Materialny błąd §6 i dokładna naprawa

Źródłowy §6 dopuszcza:

`B_s=c log(1/s)+o(log(1/s))`,

a następnie podaje multiplicatywną asymptotykę bez reszty podlogarytmicznej i jedną dodatnią stałą dla `c=c_*`.

Nie wynika to z hipotezy. Niech `B_s=c_*log(1/s)+b_s`, gdzie `b_s=o(log(1/s))`. Wtedy:

**`E_M = exp(a b_s)/(2a) · (1+o(1))`**.

Dwa dopuszczalne podciągi:

- `b_s=+sqrt(log(1/s))`: `E_M→∞`;
- `b_s=−sqrt(log(1/s))`: `E_M→0`.

Oba spełniają dosłownie zapisane przez autora `b_s=o(log(1/s))`. Zaokrąglenie `M_s` do liczby całkowitej zmienia dawkę o `O(s)` i nie modyfikuje granic.

**Poprawna wersja:**

- Jeśli `B_s=c_*log(1/s)+o(1)`, to `E_M→1/(2a)`.
- Jeśli `B_s=c_*log(1/s)+β+o(1)`, `β∈R`, to `E_M→exp(aβ)/(2a)`.
- Jeśli `b_s→−∞` lub `+∞` przy `b_s=o(log)`, granica energii jest odpowiednio `0` albo `+∞`.
- Oscylująca reszta `b_s` może powodować brak granicy.
- Dla `c<c_*` zanik oraz dla `c>c_*` rozbieżność nadal wynikają z dominacji głównego wykładnika; należy pisać `E_M=s^{1-ac+o(1)}/(2a)`, a nie asymptotyczną równość ze stałym prefaktorem bez `b_s`.

Źródłowy §5.5 zawiera ostrzejszą zmienną bilansującą `Ψ_s`; nie należy przedstawiać powyższego jako nowej rodziny twierdzeń.

## Niezależny test dokładnej macierzy 2×2

Parametry `q=1.5`, `κ=0.6`, więc `a=0.3`, `c_*=10/3` i nominalna stała `1/(2a)=5/3`.

| s | b_s=−sqrt(log) | b_s=0 | b_s=+sqrt(log) |
|---:|---:|---:|---:|
| 1e-3 | 0.75760607 | 1.66903334 | 3.67453269 |
| 1e-4 | 0.67057195 | 1.66704332 | 4.14365670 |
| 1e-5 | 0.60224495 | 1.66671346 | 4.61255133 |
| 1e-6 | 0.54648420 | 1.66667247 | 5.08302580 |

Policzono z dokładnej macierzy Perrona i skończonej sumy geometrycznej, nie z uproszczonej formuły granicznej. Dane ilustrują trzy różne zachowania; ścisły dowód granic to rachunek powyżej.

## Minimalny skrypt reprodukcji

```python
import math
import numpy as np
q, k = 1.5, .6
a = (q-1)*k
for s in (1e-3,1e-4,1e-5,1e-6):
    L = math.log(1/s)
    row=[]
    r=k*s
    Q1=np.array([[1-r,0],[q*r,1]])
    Q2=np.array([[1,q*r],[0,1-r]])
    lam,V=np.linalg.eig(Q2@Q1)
    idx=np.argmax(lam.real)
    eigen=float(lam[idx].real)
    v=V[:,idx].real; v/=np.linalg.norm(v)
    W=np.array([[1+q*q*r*r,q*r],[q*r,1]])
    A=float(v@W@v)
    for sign in (-1,0,1):
        dose=L/a+sign*math.sqrt(L)
        M=round(dose/(2*s))
        energy=s*s*A*math.expm1(2*M*math.log(eigen))/math.expm1(2*math.log(eigen))
        row.append(energy)
    print(s, row)
```

## Werdykt i firewall

- `PASS`: dokładna macierz, mnożnik Perrona, energia pary, prawidłowa wartość współczynnika progu i ścisłe reżimy pozakrytyczne.
- `REPAIR`: w §6 wzmocnić założenie o reszcie do `o(1)` dla konkretnej stałej granicznej; dla `o(log)` zachować dodatkowy czynnik `exp(a b_s)`.
- `MATURE_HOST`: standardowe asymptotyki macierzy bliskich identyczności, Perron–Frobenius i rozwinięcia wykładnicze. Brak twierdzenia o nowości.
- `NOT ESTABLISHED`: fizycznie dopuszczalna nieograniczona częstość pomiarów, źródłowy koszt dawki, CP instrument, obserwable NCDG, PBH/BBN.
- `BW_INGESTION`: PENDING. Zapis GitHub i doręczenie Slack w tym obrocie: BLOCKED; przechowywanie lokalne i odczyt: PASS.

**STOP** dla tego konkretnego kontrprzykładu po recenzji poprawionego twierdzenia właściciela. Bez nowych zadań i bez samodzielnej modyfikacji raportu Geeky-S10.

---
RECOVERY RECEIPT 2026-10-23: This body is now stored in GitHub with direct fetch/readback PASS; Slack routing to source thread SENT and thread READBACK PASS: https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1792743746462819. Any earlier BLOCKED marker is historical only. GitHub delivery != BW ingestion != owner scientific acceptance != CANON/EXEC.
