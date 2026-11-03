---
artifact_id: IW_MECH_S8_ROT006_WUXU_SUBEDGE_HADRON_NUMBER_WEIGHTING_AND_ROT035_CUSTODY_BLOCK_001_20261103
created_at: 2026-11-03
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_07 / Mech-S8
exposure: PUBLIC_SAFE
sync_state: LOCAL_VALIDATED__GITHUB_PENDING_BW_INGEST
claim_ceiling: SOURCE_TYPED_CONDITIONAL_HADRON_COUNT_ACCOUNTING / NO_PHYSICAL_E4_ADMISSION / NO_ROT035_STRICT_ODE_CERTIFICATE / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
---

# ROT006 — audyt ważenia liczby hadronów w prawie podkrawędziowym Wu–Xu

## Wynik i pierwszeństwo

Pierwszeństwo: Wu–Xu są właścicielami fizyki i oryginalnego modelu; Badacz REVIEW038 (native zero subedge) i REVIEW042 (porównanie p≈1,20, pilotaż p≈1,30), jego nota do Mech-S8 z 2 XI 20:51 (ważenie **liczby** hadronów, nie energii), MT14 ROT025 (source-native zegar utraty masy i przejścia T_H=100 TeV), INT9 ROT001 (brak przeniesienia total emission → Y_P) mają pierwszeństwo odpowiednich wątków. ROT006 nie zgłasza odkrycia, a jedynie rozdziela 20% różnicy chwilowej od integracji czasu w tych *samych* warunkowych prawach źródła.

**Kontrolowane nowo policzone wartości:** po kalibracji obu źródeł przy Mcrit=10^9g, całkowita formalna liczba hadronów ze strefy M<10^9g w modelu p=1,30 jest większa o 5,60–6,08% względem p≈1,20 z `main-scan.jl`. Wynik jest źródłowo-warunkowy i NIE jest tolerancją fizyczną Wu–Xu, zmianą `Y_P`, D/H ani beta/χ²=4.

## Tożsamość metody

Oryginalny kod Wu–Xu `Fenyutanchan/Primordial-Black-Hole` commit `d395183674cace6c9906a8911bdeb7234ba4040d`, tabela `arXiv-2509.05618/data/out/hadrons_from_PBH.dat` Git blob `06d0883a27b108692720422294ba2baacd381a64`, pierwsze DWA wiersze ponownie odczytane 3 XI przez GitHub; `tool_script-hadrons_from_PBH.jl` Git blob `cc73432910f872d526113ce59b6204f38d0766a9` stosuje `LinearInterpolation(log rates, log masses; extrapolation=ExtrapolationType.Linear)`; `main-scan.jl` blob `b368ba55d5a493f7bc185909730f7fe5691f10d6` importuje tę funkcję. Artykuł JCAP 02 (2026) 063, §4.1 i (4.5) opisuje prawo `T_H^1.3` poniżej `10^9g`. Publiczna ścieżka Fig5 odtworzona w ROT004, historyczna identyczność wykonania nadal OPEN.

Dla każdego z 5 kanałów `R_j(M) = R_{0,j}(Mcrit/M)^{p_j}` w kodzie (j: agregaty π±, K±, K0L, p+pbar, n+nbar), a w deklarowanym prawie paper `p=1.3`. Kalibracja R0 jest jednakowa na granicy. Z pierwotnych dwóch wierszy: p = 1.200485626, 1.196651351, 1.196804841, 1.204291429, 1.204763064.

Dla *warunkowego* źródłowego prawa zegara MT14 `dM/dt=-K/M^2`, `K>0` stałe, liczba wyemitowanych hadronów od Mcrit do formalnego Mf wynosi

\[
N_j(p;M_f) = \frac{R_{0,j} M_{crit}^3}{K}\,
\frac{1-(M_f/M_{crit})^{3-p}}{3-p},\qquad p<3.
\]

To elementarna całka `R dt` i wymaga TYLKO tego modelu. W szczególności dla formalnego Mf→0:

\[
\frac{N_{paper}}{N_{scan}} = \frac{3-p_{scan}}{3-1.3};\qquad
\frac{N_{scan}}{N_{paper}}=\frac{3-1.3}{3-p_{scan}}.
\]

Nie ma tutaj wartości K ani skal źródłowych: skracają się w ilorazach. Formalne Mf→0 jest limitowaniem przepisu źródłowego, nie fizyczną ważnością generatora dla dowolnie małej masy czy certyfikatem masy końcowej.

## Tabela kontroli

| Kanał | p w kodzie | scan/paper w chwili T_H=100TeV | paper więcej liczby z całego subedge niż scan | scan/paper liczby przed progiem 100TeV | udział liczby po przekroczeniu progu w scan |
|---|---:|---:|---:|---:|---:|
| π± | 1.200486 | 0.79964 | +5.854% | 0.94894 | 1.754% |
| K± | 1.196651 | 0.79278 | +6.079% | 0.94707 | 1.739% |
| K0L | 1.196805 | 0.79305 | +6.070% | 0.94715 | 1.739% |
| p+pbar | 1.204291 | 0.80650 | +5.630% | 0.95081 | 1.769% |
| n+nbar | 1.204763 | 0.80736 | +5.602% | 0.95104 | 1.771% |

`M(T_H=100TeV)=1.057261195158e8g` pochodzi z ROT002 i niezależnego MT14 ROT025; jest **progiem temperatury**, nie chwilą pojawienia się pierwszego kwantu 100 TeV. Liczba po progu w modelu papierowym p=1,3 = 2,19336% dla wszystkich pięciu kanałów, w modelu scan 1,739–1,771% (Badacz NOTE wcześniej wykazał ten typ ważenia). Nie należy traktować żadnej z tych liczb jako całki o zweryfikowanym pokryciu fragmentacji ponad 100 TeV; w obu metodach dalsze przedłużenie jest niewalidowane.

**Ważne:** 20–21% różnicy *chwilowej* przy 10^8g (ROT003) zostaje po ważeniu źródłowym odpowiednio zredukowane do około 5–6% w formalnej całce **liczby**. Brak jednak nierówności na odpowiedź `Y_P`: dodatnie całkowite tempa nie implikują monotonicznego celu neutron/proton, ponieważ kanały z przeciwnymi reakcjami i historia temperatury mają inne wagi. Brak tu nieliniowej kinetyki, reżimu źródła ani nierówności z certyfikowanym błędem fizycznym.

## Weryfikacja i ograniczenia

- Python 3 stdlib, dwie liczbowe pary wierszy źródła z wcześniej odczytanego niezmiennego Git blob, plus opcja `--table` do kontroli pełnego pliku i jego SHA Git; bez dostarczonego pełnego pliku tryb `PINNED_VERBATIM_FIRST_TWO_ROWS_ONLY`, nie `FULL_TABLE_VERIFIED`.
- Zamknięta całka sprawdzona niezależnie: **złożony Simpson** z transformacją `x=t^4`, 4096 paneli, błąd porównania < 1.1e-14 dla 5 kanałów. Dodatkowa niezależna kwadratura SciPy `quad` wykonana jednorazowo w sesji, największy błąd ≈1.1e-16, nie jest wymagana do publicznego reproduktora.
- Wyliczone ilorazy nie zależą od globalnej normalizacji źródła. Nie ma niezależnej walidacji source→charge→reaction, greybody, heavy channels, BlackHawk v2.3 BBN table, ani błędu Julia10D.
- Priorytet właściciela: **rzeczywista, czasowa odpowiedź n/p na odtworzone spektrum hadronowe**, nie kolejne globalne ∆rate ani perturbacje ×0/×2.

## Zaległość Mech-S7 ROT035 — rzeczywisty stan custody

Archiwum ROT035 (195 elementów wg oryginalnego zwrotu Mech-S7) nie jest zamontowane w tej rozmowie. Bounded search nazwy/ROT035/Mech-S7 w Google Drive, Project/Library i lokalnym `/mnt/data` nie odnalazł oryginalnego ZIP; wyniki Drive dotyczyły przede wszystkim referencji Living Theory, nie kodu Mech. Publiczny raport Mech-S7 ROT035 na GitHub zawiera współrzędne końcowe, korekty matematyczne, wyniki warunkowego 7D, lecz nie dostarcza pełnego programu/byte-identycznych trajektorii w ZIP. **Nie da się uczciwie certyfikować epsilon_ODE z samej wartości różnicy tolerancji.** Dotychczasowe progi ROT005 pozostają warunkami koniecznymi dla numerycznego awansu. NO claim of audit acceptance or `BW_ING`.

### Dyspozycja

`ROT006_CONDITIONAL_SOURCE_NUMBER_GATE=EXECUTED; ROT035_ARCHIVE_CUSTODY=NOT_LOCATED_IN_CHECKED_SURFACES; ROT035_STRICT_ENDPOINT_CERT=OPEN; E4_SOURCE_BLOCK; FIG5_HISTORIC_CODE_HASH_OPEN; NO_PBH_BOUND; NO_CANON; NO_EXEC_SIGN; GITHUB_PENDING_BW_INGEST`.