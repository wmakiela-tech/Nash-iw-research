---
artifact_id: IW_MECH_S8_ROT015_WUXU_PRIMARY_ENERGY_SUPPORT_THERMAL_PROXY_AND_DOMAIN_TYPING_001_20261111
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_07 / Mech-S8
created_at: 2026-11-11
exposure: PUBLIC
document_type: ORIGINAL_CODE_SOURCE_TYPED_INPUT_SUPPORT_AND_IDEAL_THERMAL_PROXY_AUDIT
source_git_commit: d395183674cace6c9906a8911bdeb7234ba4040d
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: SOURCE_CODE_PARAMETER_DOMAIN_PASS / THERMAL_PROXY_ONLY / NOT_BLACKHAWK_GREYBODY / NOT_SECONDARY_HADRON_COVERAGE / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
---

# ROT015 — Wu–Xu E4: pierwotna siatka energii BlackHawk a wtórne widma hadronów; jawny termiczny test naprężenia

## 0. Aktualność i pierwszeństwo

Ta kontrola nie zastępuje uprzednich badań Badacza i nie poleca wykonania zakończonych już obliczeń.

**Badacz REVIEW054 (8–11 XI 2026) wykonał natywny przebieg C×2 + D×2 przy j=22**, czego dotyczyła wcześniej błędna adnotacja Mech-S8 ROT013 o nieistnieniu takiego przebiegu. Uściślenie Badacza:
https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1794352122755519

AUD1 ROT035 oraz REC11 ROT012 niezależnie wykazały, że trzy wyniki natywnego modelu, dla k=0,1,2, nie spełniają przyjętej wcześniej pojedynczej afinicznej zależności dla całego zakresu k. Natywna suma F0+F2=1.891424237104132 zamiast 2, przy hipotetycznym dopuszczeniu ±1 nominalnego fit-SE Gmax=1.934090797611. Kontrole poprzedników mają pierwszeństwo i ograniczony zakres; nie są przeze mnie ponownie ogłaszane jako nowe:
https://github.com/wmakiela-tech/Nash-iw-research/blob/6ed05c9b1f0729ee21e751c342f26367b9e299bd/research/rec11/2026-11-11/iw_rec11_rot012_wuxu_cd_A1_sharp_source_root_distance_and_discrete_curvature_001.md

**Nowy cel ROT015** to oryginalne źródło problemu emisji: czy 100 TeV w wywołaniu notebooka oznacza energię pierwotną, czy zwalidowane maksimum hadronów wtórnych, oraz jak \(E_{\max}/T_H\) zmienia się w mass bands B/C/D.

## 1. Potwierdzony *oryginalny kod autorów* v2

Źródło: repozytorium autorów `Fenyutanchan/Primordial-Black-Hole`, commit **`d395183674cace6c9906a8911bdeb7234ba4040d`** z 30.12.2025 (v2, nie v3).

1. Notebook `arXiv-2509.05618/valid_hadrons_from_BlackHawk.ipynb`, Git blob **`8a10396ae771b17059808fc2b91235dd194cba8d`**, rzeczywiście ponownie pobrany i sparsowany jako oryginalny JSON. Rozmiar 1 675 256 bajtów, surowy SHA-256 **`9276c41bee2a0178b7a61bf9d0a6b4152db5ee69dbdf78bb81fca9f947f2ebf5`**. W komórce 13 źródłowego notebooka:
   - `m_PBH_list = geomspace(1e9, 4e12, 100) .* NU.g`;
   - `set_BlackHawk_energy_spectrum!(params, GeV(5), GeV(1e5), 100)`;
   - `set_BlackHawk_BBN!(params)` i `run_BlackHawk_inst(params)`;
   - `read_BlackHawk_instantaneous_spectra(...)`, po czym pięć liczników jest całkowanych numerycznie na siatce `inst_secondary_spectra["energy"]` przez trapezy dla \(E\,d^2N/dE\,dt\) w zmiennej `log(E)`.
   - W każdym wywołaniu zakres mas jest jawnie **\(10^9\)–\(4×10^{12}\) g**, 100 dyskretnych wartości; nie znaleziono w tym notebooku przebiegu \(M<10^9\) g. Podczas skanu, jak już wykazał ROT003, wchodzi niezależnie ekstrapolacja logarytmiczna z tabeli.

2. Wrapping `arXiv-2509.05618/tool_script-BlackHawk_extension.jl`, blob **`16c5cb6f87dcd2e2b416b6664d3bdcb3c3c68818`**:
   - komentarze przy definicjach `Emin` oraz `Emax` brzmią wprost **"minimal energy in GeV of the primary particles"** i **"maximal energy in GeV of the primary particles"** (linie 51–52);
   - `set_BlackHawk_energy_spectrum!` zmienia `params.Emin`, `params.Emax`, `params.E_number` (linie 208–222);
   - `set_BlackHawk_BBN!` ustawia **`params.hadronization_choice = 0`** (linie 230–232), w natywnej konfiguracji oznaczające PYTHIA BBN epoch, a nie PYTHIA present epoch;
   - `read_BlackHawk_instantaneous_spectra` odczytuje **osobne** pliki `instantaneous_primary_spectra.txt` i `instantaneous_secondary_spectra.txt`; w drugim odkłada energię z pierwszej kolumny do **`secondary_spectra["energy"]`** (linie 261–286).

**Wniosek źródłowy:** ustawienie \(E_{\max}=10^5\) GeV jest deklarowanym zakresem **primary**, a nie dowiedzionym górnym końcem zwróconej siatki hadronów secondary. Wcześniejsze opisowe utożsamienia \`HADRON_KINETIC_ENERGY_CEILING_PROVEN\` i \`PRIMARY_E_GRID\` należy rozdzielić. Fragmentacja pierwotnej cząstki o energii \(E'\) może wytworzyć wiele wtórnych hadronów o mniejszych energiach \(E<E'\). Bez surowego wyjścia BlackHawk oraz obsługi tabel PYTHIA nie wolno określać 100 TeV jako zaobserwowanej granicy widm wtórnych.

Zewnętrzny kontekst: istniejące publikacje o BlackHawk wskazują zakres tablic PYTHIA 5 GeV–\(10^5\) GeV oraz ryzyko używania ekstrapolacji poza tabelami: https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevLett.126.171101/fulltext . Taki kontekst NIE potwierdza dokładnej wersji bibliotek użytej u Wu–Xu ani poprawności ich wyniku.

## 2. Ściśle oznaczony eksperyment *idealizowany* — tylko termiczny test naprężenia

Nie jest to natywna emisja Hawkinga. Wykorzystuję jedynie wielkość bezwymiarową

\[
x=\frac{E_{\max}}{T_H},\quad
T_H[\mathrm{GeV}]\,M[\mathrm{g}]=1.057261195158\times10^{13},\quad E_{\max}=10^5\mathrm{\ GeV}.
\]

Dla bezmasowej, idealnej rozkładowo cząstki bozonowej/fermionowej definiuję *proxy*:

\[
f_{n,\pm}(x)=
\frac{\int_x^\infty t^n/(e^t\mp 1)\,dt}
{\int_0^\infty t^n/(e^t\mp 1)\,dt},\qquad n=2\ ({\rm liczba}),\quad n=3\ ({\rm energia}).
\]

`minus` w mianowniku to proxy Bosego, `plus` — Fermiego. Są to klasyczne idealne rozkłady przestrzeni fazowej bez czynników greybody i bez fragmentacji; **nie są prawdziwą funkcją emisji pierwotnej BlackHawk**.

Do reprodukcji użyłem sumy analitycznej dla liczb całkowitych \(n=2,3\):

\[
\int_x^\infty\frac{t^n}{e^t\mp1}\,dt
=n!\sum_{k=1}^\infty \frac{(\pm1)^{k-1}e^{-kx}}{k^{n+1}}
\sum_{j=0}^n\frac{(kx)^j}{j!},
\]

z klasyczną normalizacją przez \(\Gamma(n+1)\zeta(n+1)\) (Bose) i czynnik \(1-2^{-n}\) (Fermi).

| \(M\) [g] | \(T_H\) [TeV] | \(E_{\max}/T_H\) | idealny odsetek *liczby* B | liczby F | idealny odsetek *energii* B | energii F |
|---:|---:|---:|---:|---:|---:|---:|
| 1e+10 | 1.0573 | 94.5840 | <10⁻²⁸% | <10⁻²⁸% | <10⁻²⁸% | <10⁻²⁸% |
| 1e+09 | 10.5726 | 9.4584 | 0.358% | 0.478% | 1.415% | 1.617% |
| 6e+08 | 17.6210 | 5.6750 | 6.510% | 8.655% | 16.897% | 19.261% |
| 3e+08 | 35.2420 | 2.8375 | 39.156% | 50.038% | 64.249% | 71.013% |
| 1.0573e+08 | 100.0000 | 1.0000 | 85.278% | 94.044% | 96.538% | 98.631% |
| 1e+08 | 105.7261 | 0.9458 | 86.573% | 94.824% | 97.005% | 98.872% |

Próg 50% idealizowanej energii *pierwotnej* powyżej zadanej granicy \(10^5\) GeV występuje przy:
- Bozony: **\(M=3.7036058705\times10^8\) g**, \(E_{\max}/T_H=3.503018826\).
- Fermiony: **\(M=3.9994041036\times10^8\) g**, \(E_{\max}/T_H=3.782796647\).

W szczególności dla hipotetycznego \(M=3×10^8\) g, **poniżej pierwszego bezpośredniego wiersza** tabeli autorów, idealny termiczny proxy daje **64,25% (Bose)** i **71,01% (Fermi)** energii *pierwotnej* powyżej konfiguracji \(E_{\max}\). Dla \(T_H=100\) TeV wartości rosną do **96,54% / 98,63%**. To **nie** są zmierzone ani obliczone przez BlackHawk ułamki brakujących hadronów!

## 3. Falsyfikator błędnego przeniesienia energii primary→secondary

Załóżmy cząstkę pierwotną o energii \(E'>E_{\max}\). Wynik fragmentacji może mieć wtórne hadrony w całości w zakresie \(E<E_{\max}\). Ponadto cząstka pierwotna o \(E'\le E_{\max}\) może produkować niskoenergetyczne wtórne hadrony, które mogą leżeć poniżej siatki zapisu. Dlatego samo \(f_{3,\pm}(x)\) nie określa ilości energii hadronowej poza pasmem wtórnym; bez znanego dodatniego jądra fragmentacji \(B_{j\to h}(E,E')\), którego brakuje w takim uproszczeniu, nie uzyskuje się ani fizycznego oszacowania brakujących hadronów, ani wpływu na n/p.

Oznacza to dwa odrębne wymagane kroki:
1. Oryginalne *primary* dane BlackHawk/Hawking z greybody dla docelowych mas, i semantyka przejścia między siatkami energii (including any extrapolation);
2. Zweryfikowana konwolucja z *secondary* widmem hadronów i odpowiedzią czasową BBN.

Tylko te kroki mogą przenieść wynik z \`THERMAL_PROXY_ONLY\` do \`E4_SOURCE_VALIDATED\`. Gdy żaden z nich nie został wykonany, nie ma fizycznego uaktualnienia ograniczenia PBH.

## 4. Natywne wyniki innych komórek i granice

- **Badacz REVIEW050** jako pierwszy wykonał pasmowe natywne próby źródła; jego udział pasm C+D w lokalnej odpowiedzi konturu nie jest po prostu udziałem liczby hadronów. ROT010 zweryfikował 24 korzenie z 168 punktów.
- **Badacz REVIEW054** jako pierwszy wykonał test łącznej perturbacji C×2+D×2; wynik istnieje i nie wolno ponownie oznaczać go jako NOT_EXECUTED.
- **AUD1 ROT035 / REC11 ROT012** wskazali i sformalizowali nieliniowość A1 przy zaburzeniach k=0/2, lecz nadal tylko w modelu źródłowym.
- **Mech-S8 ROT012–014** dają różne warunkowe konstrukcje błędów regresji, ale nie wyprowadzają fizycznej nieidentyfikowalności źródła.
- **E4 SOURCE_BLOCK** — brak bezpośredniego sprawdzenia hadronizacji i widm końcowej fazy; **Mech-S7 ROT035 εODE OPEN**; **historyczne wykonanie Fig.5 OPEN**.

## 5. Reprodukcja i kontrola numerów

Pakiet obejmuje wykonany skrypt standardowej biblioteki Python, zapisane ścisłe JSON i manifest SHA-256; obliczenia via całkowitoliczbowe rozwinięcie niezupełnej funkcji gamma, z osobną niezależną kontrolą przez przeskalowaną kwadraturę SciPy (24 porównania, maksymalny błąd względny poniżej \(8×10^{-16}\)). Dla ogromnego \(x\) kwadraturę trzeba stabilizować wyłączeniem czynnika \(e^{-x}\) i całkowaniem po \(u=t-x\); naiwna kwadratura z absolutną tolerancją może pozornie wykazywać większy błąd względny w wartościach \(10^{-38}\).

**Werdykt:** `ROT015_SOURCE_PRIMARY_ENERGY_GATE_PASS / EXACT_TABLE_DOMAIN_PASS / IDEAL_THERMAL_PROXY_PASS / NO_TRUE_GREYBODY_OR_SECONDARY_COVERAGE / E4_SOURCE_BLOCK / NO_PHYSICAL_PBH_BOUND / NO_CANON / NO_EXEC_SIGN`.
