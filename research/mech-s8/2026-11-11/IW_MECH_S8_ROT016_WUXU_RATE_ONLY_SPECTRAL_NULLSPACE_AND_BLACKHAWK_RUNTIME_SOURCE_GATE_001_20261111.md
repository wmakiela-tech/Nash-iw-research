---
artifact_id: IW_MECH_S8_ROT016_WUXU_RATE_ONLY_SPECTRAL_NULLSPACE_AND_BLACKHAWK_RUNTIME_SOURCE_GATE_001_20261111
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_07 / Mech-S8
created_at: 2026-11-11
exposure: PUBLIC
claim_ceiling: SOURCE_PINNED_STATIC_CUSTODY / EXACT_RATE_ONLY_MODEL_NULLSPACE / NO_REAL_SECONDARY_SPECTRUM / NO_PHYSICAL_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# Mech-S8 ROT016 — Luka odtwarzalności środowiska BlackHawk i dokładne jądro redukcji widm do szybkości całkowitych

## 0. Aktualność i pierwszeństwo

Autorzy Wu–Xu pierwsi opisali w §4.1 [arXiv:2509.05618v3](https://arxiv.org/html/2509.05618v3) zarówno limit `Emax_init=100000.` GeV, jak i *celową* integrację energii wtórnych hadronów w równaniu (4.2), **uzasadnioną założeniem o szybkim hamowaniu i termalizacji**. Nie przypisujemy odkrycia tych założeń Mech-S8. ROT015 sprostował, że `set_BlackHawk_energy_spectrum!` ustawia siatkę energii cząstek pierwotnych, a nie bezpośrednio siatkę wtórnych hadronów. Badacz REVIEW050 FIRST uruchomił natywny wrażliwościowy test pasmowy; Badacz REVIEW054 FIRST wykonał też jednoczesny przebieg C×2+D×2. REC11 ROT013 FIRST wyznaczył ostry próg globalnej zgodności alternatywy źródłowej z indywidualnymi nominalnymi błędami dopasowania `0.858974879...`, ściślej niż starszy świadek Mech-S8 ROT013 `0.860765...`. REC11 ROT012 i AUD1 ROT035 FIRST potwierdzili awarię założenia jednej odpowiedzi afinicznej w trzech natywnych punktach `k=0,1,2`.

**Własny nowy zakres ROT016:** (i) bezpośredni audyt kompletności *zamrożonego publicznego drzewa Git* autorów względem rzeczywistego importu i wykonania BlackHawk; (ii) dokładne źródłowe jądro operatora `widmo(E,M) -> 5 szybkości liczbowych(M)` wykazane na oryginalnym wierszu danych (nie na zastępczym modelu termicznym). To jest wynik o strukturze informacji w kodzie, **nie korekta fizyczna do PBH**.

## 1. Źródło pierwotne i brama wykonawcza

**Repo autorów:** `Fenyutanchan/Primordial-Black-Hole`, COMMIT `d395183674cace6c9906a8911bdeb7234ba4040d` (2025-12-30, v2 — nie arXiv v3). Kompletny GitHub API `git/trees/{commit}?recursive=1` zwrócił 101 wpisów, `truncated=false`. Dodatkowo odczytano zawartość konkretnych plików, nie tylko ich nazw.

| Komponent | Oryginalny plik i informacja | Status w dokładnym drzewie |
|---|---|---|
| Ścieżka wykonawcza BlackHawk | `tool_script-directories.jl`, blob `8c54632...`: `BlackHawk_directory = .../external_code/BlackHawk_v2.3` | **Katalog nieobecny** |
| Wrapper Julia | `tool_script-BlackHawk_extension.jl`, blob `16c5cb6f...`: `cd(BlackHawk_directory); run(./BlackHawk_inst.x ...)` | **Nie ma wskazanego pliku wykonywalnego w drzewie** |
| Odrębny patch źródłowy | `external_code/BlackHawk_v2.3-hack/` | **Obecny, ale ma tylko 2 pliki główne C oraz `src/include.h`** |
| Funkcje potrzebne do linkowania | `BlackHawk_inst.c` wywołuje `read_hadronization_tables`, `hadronize_instantaneous`, `integrate_initial_energies_instantaneous` itd. | Brak odpowiednich definicji źródłowych `.c` w tym drzewie |
| Tabele hadronizacji użyte przez wskazany runtime | Poddrzewo `BlackHawk_v2.3` | Nie ma katalogu ani tabel; nie wiadomo, jaka kompletna instalacja była na maszynie autorów |
| Notebook i końcowa tabela | `valid_hadrons_from_BlackHawk.ipynb` blob `8a10396a`; `data/out/hadrons_from_PBH.dat` blob `06d0883a` | Oba obecne; tabelę zapisano jako **pięć kolumn szybkości całkowitych** i masę |

**Rozstrzygnięcie:** samo publiczne drzewo z przypiętego commitu nie jest zamkniętym, wykonywalnym środowiskiem generującym widma BlackHawk. To **nie jest** dowód, że autorzy takiego środowiska nie mieli lub że wyniki były błędne. Może ono wymagać instalacji pełnego, zewnętrznego BlackHawk i tabel ze znaną wersją. Oddzielnie zamrożony `BlackHawk_v2.3-hack` nie zastępuje katalogu używanego przez funkcję `run_BlackHawk_inst` w Julia.

**Wersjonowanie PYTHIA:** w zagnieżdżonym archiwum `arXiv-2509.05618v1/PYTHIA8_table_scripts/` są receptury `table_up.jl` i `table_gluon.jl`. Pierwsza deklaruje `E_initial=[5,10^5]` GeV, 100 węzłów, `E_final=[0.1,10^5]` GeV, 10 000 węzłów, 10^5 zdarzeń na energię. Dla gluonu dolne wejście jest 1000 GeV. Są to **skrypty historycznego v1**, a nie poświadczenie bajtowej tożsamości tabel użytych w wykonaniu v2. W katalogu głównym `arXiv-2509.05618/PYTHIA8_table_scripts/` brak analogicznego zestawu. Wcześniejsze utożsamienie konfiguracji `Emax=100TeV` z obserwowanym maksimum wtórnej siatki w rzeczywistym v2 nadal jest niedozwolone.

**Pierwszeństwo tekstu artykułu:** Wu–Xu w §4.1 explicite opisują ograniczenie partonowe 100 TeV oraz stosowanie ekstrapolacji analitycznej dla `M<10^9g`. Wykonawczy kod v2 `tool_script-hadrons_from_PBH.jl` używa log-liniowej ekstrapolacji 100-punktowej tabeli; odrębna niezgodność z deklarowanym asymptotycznym wykładnikiem 1.3 była wcześniej zauważona przez ROT003 i nie jest tu przedstawiana jako nowe odkrycie.

## 2. Dokładna struktura wejścia do oryginalnego ODE

Oryginalne źródło `main-scan.jl`, blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`: w liniach 103–107 pięć funkcji `dN_over_dt_* (m_PBH)` wchodzi jako źródło produkcji hadronów, mnożone przez `n_PBH`. W liniach 90–94 oddziaływania `n↔p` zawierają liczebności `n_π±`, `n_K`, `n_pbar`, `n_nbar` i `σv_h(T_SM)`; nie występuje zależny od energii hadronu stan `n_h(E)` ani energio-rozdzielczy kernel interakcji. W liniach 109–128 rozpad i rozpraszanie też używają liczebności całkowitych.

Niech `S_h(M,E) ≥ 0` oznacza dowolne matematyczne wtórne widmo odpowiadające grupie h, a

\[
R_h(M)=\int S_h(M,E)\,dE.
\]

Jeżeli dwie rodziny mają **takie same pięć funkcji** `R_h(M)` dla wszystkich mas objętych ewolucją i wszystkie inne warunki solvera są te same, wektorowe pole prawej strony oryginalnego ODE jest dokładnie takie samo; jego rozwiązanie, `X_n`, otrzymane `Y_P` i kontury są więc identyczne (w zakresie jednoznaczności rozwiązania oraz tych samych ustawień solvera). **To dokładna, formalna nieodróżnialność modelu RATE_ONLY**, a nie twierdzenie, że fizyka ignoruje energię.

W szczególności nawet bardzo dokładne powtórzenie oryginalnego skanu i wszystkich perturbacji C/D, bez zmiany interfejsu `R_h`, nie waliduje fizycznej energiozależności hadronizacji ani założenia termalizacji. Kontrole Badacza `REVIEW050/054` testują istotny efekt **czasowego** profilu źródła liczb hadronów, lecz nie odtwarzają zintegrowanego rozkładu energii.

## 3. Jawny, nieujemny i ciągły świadek matematyczny

Dla `a>0` definiuję ciągłą, trójkątną gęstość energii `h_a(E)`:

\[
h_a(E)=\begin{cases}
4(E-a),&a\leq E\leq a+1/2,\\
4(a+1-E),&a+1/2\leq E\leq a+1,\\
0,&\text{poza tym zakresem.}
\end{cases}
\]

Dokładny rachunek: `∫h_a dE = 1`, `∫E h_a dE = a+1/2`. Rozważam `S_{h,L}(M,E)=R_h(M)h_1(E)` i `S_{h,H}(M,E)=R_h(M)h_100(E)`. Obydwa hipotetyczne widma są nieujemne, ciągłe i mają **identyczne całki liczby hadronów** dla każdej masy. Średnia energia wynosi odpowiednio 1.5 i 100.5 GeV, a pierwszy moment różni się dokładnie **67-krotnie**. Takie widma są *niezależnymi matematycznymi możliwościami* w przestrzeni funkcji z ustaloną całką; nie wykazano, że oba mogą powstać w prawdziwym programie PYTHIA lub z tej samej emisji Hawkinga.

Do kontroli pięciu grup użyłem rzeczywistego **pierwszego wiersza** (M = `5.609588603804452e32` GeV, odpowiadającego ~`1e9 g`) z publicznego `hadrons_from_PBH.dat`, Git blob `06d0883a27b108692720422294ba2baacd381a64`. Pięć odczytanych wartości w jednostkach naturalnych tabeli: `489105.5126008581`, `59105.93631247951`, `29086.774913348447`, `34849.08026691193`, `34656.17773724596`.

Test w `mech_s8_rot016_rate_compression_exact_witness.py` wykorzystuje `fractions.Fraction`, więc każda z dziesięciu całek liczbowych i dziesięciu momentów jest obliczona **dokładnie**: PASS, pięć dodatnich grup, wspólny stosunek momentu 67. Nie użyto rozkładu Bosego/Fermiego z ROT015, żadnej biblioteki BlackHawk, modelu kolizji ani kodu Julia.

To jest **kontrprzykład wobec twierdzenia**, że poprawność widm energii można wydedukować z samej tabeli pięciu szybkości i zgodności skanu. NIE jest to kontrprzykład wobec hipotezy fizycznej Wu–Xu o szybkiej termalizacji (ta wymaga zewnętrznych czasów hamowania, opóźnień oraz interakcji) i NIE obala wyników Y_P.

## 4. Dlaczego problem E4 pozostaje otwarty

Dwie odrębne bramki:

1. **Source provenance:** pozyskać bajtowo identyfikowalną, kompletną instalację `BlackHawk_v2.3` rzeczywiście użytą w notebooku, wersję i hash PYTHIA BBN tables/greybody, pliki `instantaneous_primary_spectra.txt` i `instantaneous_secondary_spectra.txt` dla mas, zapis rzeczywistej siatki energii oraz metodę postępowania poza zakresem tablic (zwłaszcza `M<10^9g`). Fragmenty źródłowego C i same agregaty nie wystarczają.
2. **Physical target sufficiency:** oryginalna hipoteza natychmiastowego/efektywnego wytracenia energii hadronów wymaga niezależnego porównania czasów zatrzymania, rozpadu i reakcji (zależnych od energii i temperatury plazmy); potem należy zdecydować, czy interfejs `R_h(M)` wystarcza dla docelowego obserwabla. W przeciwnym wypadku rozbudować kernel transportu zależny od energii.

**Nie ustanawiam nowych obowiązków dla innych komórek.** Nie polecam ponawiać już wykonanego przez Badacza testu jednoczesnego C×2+D×2. Wyniki Badacza REVIEW057 dotyczące końcowej fazy `M≳10^10g` są odrębną, nową bramką czasową; mają pierwszeństwo nad niniejszymi konstrukcjami i wymagają oceny właścicielskiej, nie automatycznego włączenia do naszego schematu.

## 5. Werdykt i granice

- `ORIGINAL_GIT_COMMIT_DIRECTORY_INCOMPLETE_FOR_STANDALONE_BLACKHAWK_INST_REPLAY` — źródłowo potwierdzone, dotyczy **tylko tego publicznego drzewa**.
- `ODE_RATE_ONLY_SPECTRAL_KERNEL` — **dokładna tożsamość algebraiczna** w zadanym interfejsie oryginalnego `main-scan.jl`.
- `EXACT_FRACTION_WITNESS` — pięć grup źródłowych z rzeczywistego wiersza danych; 10 całek liczb i energii; PASS.
- `E4_SOURCE_BLOCK / SOURCE_RUNTIME_AND_ENERGY_KERNEL_MISSING / NO_PHYSICAL_Y_P_OR_BETA_BOUND / NO_CANON / NO_EXEC_SIGN / BW_PENDING`.

Załącznik: dokładnie przypięty manifest odczytu drzewa źródłowego, reproduktor Python 3 stdlib i ścisły JSON. ZIP zawiera sumy SHA-256; odtworzenie z rozpakowanego pakietu musi dać bajtowo identyczny JSON.
