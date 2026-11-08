---
artifact_id: IW_MECH_S8_ROT009_WUXU_V3_B5_B11_FULL_SYMBOLIC_DIRAC_SPIN_NORMALIZATION_OWNER_RETURN_001_20261108
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_07 / Mech-S8
created_at: 2026-11-08
exposure: PUBLIC_SAFE
problem_id: P1_FRONTB_WUXU_V3_APPENDIX_B_SOURCE_MANUSCRIPT_CONSISTENCY
result_class: INDEPENDENT_ALL_VARIABLE_SYMBOLIC_DIRAC_TRACE / B5_B11_NORMALIZATION_REPAIR / MATURE_STANDARD_MODEL_ALGEBRA / NONBLIND_CROSS_FAMILY_ACK
sync_state: LOCAL_VERIFIED_GITHUB_PENDING_BW_INGEST
claim_ceiling: V3_MANUSCRIPT_FORMULAS_ONLY / NO_V3_RUN / NO_JCAP_FIG5_IMPACT / NO_PBH_BBN_BOUND / NO_CANON / NO_EXEC_SIGN
---

# Mech-S8 ROT009 — Wu–Xu arXiv v3: (B.5) → (B.11), niezależne pełne wyprowadzenie symboliczne

## A. Aktualność i pierwszeństwo

1. Mech-S8 ROT008 (5 XI): FIRST stwierdził niezgodność arytmetyczną wydrukowanych (B.6) i (B.9), bez rozstrzygania kierunku i normalizacji. Zapis publiczny: https://github.com/wmakiela-tech/Nash-iw-research/blob/0eab7a5c2fb493d128fb42c6c7295e49b9e89494/research/mech-s8/2026-11-05/IW_MECH_S8_ROT008_WUXU_V3_APPENDIX_B6_B9_INTERNAL_ALGEBRA_FALSIFIER_001_20261105.md.
2. **AUD1 ROT029 (6 XI)** sprawdził niezależnie bezpośrednio oryginalny HTML v3 i potwierdził sprzeczność. Slack receipt: https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1793965966436729. Prawidłowy sufit: manuscript inconsistency, nie fizyczny PBH error.
3. **Badacz REVIEW049 (8 XI, 09:15 CET)** FIRST ustalił kierunek, wyprowadzając znak i **nowy factor-32 problem** z (B.5) metodą śladów i spinorów; publiczny commit https://github.com/wmakiela-tech/Nash-iw-research/blob/6d5cf2e69aaa2ba640edb2e137a3c70884c76b77/research/badacz/2026-11-08/IW_BADACZ_WUXU_V3_APPENDIX_B_DIRAC_TRACE_CHECK_REVIEW_049_20261108.md. To **nie** jest odkrycie ani claim pierwszeństwa Mech-S8.
4. **INT9 ROT005 (8 XI, 09:32 CET)** pokazał jedyną poprawkę znaku w rodzinie z jednym wolnym współczynnikiem B.6. Slack: https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1794126755942479.
5. **NOWY wkład Mech-S8 ROT009:** niezależny od skryptów Badacza **pełny symboliczny test wielomianowy dla dowolnych rzeczywistych składowych pędów leptonów i sprzężeń gV/gA oraz dowolnych mn,mp w granicy spoczywających nukleonów**, nie tylko kilka konkretnych par stanów. Dokładna tożsamość `SymPy` i trzy osobne racjonalne kontrole leptonicznie on-shell. Użyta jest jawna reprezentacja 4×4 gamma; kod napisany od zera (nie przeniesiono kodu REVIEW049). **Brak nowego twierdzenia:** standardowy ślad Diraca, źródła i pierwszeństwo osób/autorów zachowane.

## B. Pierwotne źródło i tożsamość

Wu, Xu, *Primordial Black Holes Evaporating before Big Bang Nucleosynthesis*, arXiv:2509.05618 **v3** 6 maja 2026: https://arxiv.org/html/2509.05618v3, Appendix B lines (B.4)–(B.17), szczególnie (B.5),(B.6),(B.7),(B.8),(B.9),(B.11). Ta rewizja **nie** jest automatycznie artykułem JCAP z 17 lutego 2026 ani przypiętym autorskim kodem **v2** Git commit `d395183674cace6c9906a8911bdeb7234ba4040d` z 30 grudnia 2025. Mech-S8 ROT007 sprostował wcześniejszą etykietę v3 dla publicznego kodu v2.

B.5: `L=(GF/sqrt(2)) [pbar gamma^mu(gV-gA gamma5)n][ebar gamma_mu(1-gamma5)nu]`. Z deklarowaną metryką `(+---)`, `gamma5=i gamma0 gamma1 gamma2 gamma3` i mnożeniem `GF²/2` po kwadracie amplitudy otrzymano **pełną sumę po spinach**:

`Σ|M|²/GF² = 32 [ (gV+gA)²(p_n·p_nu)(p_p·p_e) + (gV-gA)²(p_n·p_e)(p_p·p_nu) - (gV²-gA²) mn mp (p_e·p_nu) ]`.

Wyrażenie ma **minus** przed ostatnim członem; wydrukowane (B.6) ma **plus**. W limicie `p_n=(mn,0)`, `p_p=(mp,0)`, ze zmiennymi `E=e0*n0`, `D=ex*nx+ey*ny+ez*nz`, pełne symboliczne wyprowadzenie z tych samych macierzy gamma daje identycznie:

`Σ|M|²/GF² = 32 mn mp [ (gV²+3gA²) E + (gV²-gA²) D ]`.

Nie nałożono do tej tożsamości obostrzenia kinematyki końcowej `p_n=p_p+p_e+p_nu` (limit spoczynkowy w samym artykule pomija odrzut). To **tożsamość tensorowa w przybliżeniu autorów**, a nie obliczenie fizycznego rozpadu z zachowaniem dokładnych wszystkich pędów. Matematyczna tożsamość potwierdzona dla zmiennych symbolicznych, nie tylko na siatce numerycznej.

Wydrukowane (B.9) ma **poprawny kształt w nawiasie**. Wydrukowane (B.6) redukuje się natomiast do `[ (3gV²+gA²)E - (gV²-gA²)D ]`. Pierwszeństwo tej kontroli należy do Mech ROT008/AUD1; orientacja naprawy do Badacz REVIEW049/INT9.

## C. Drugi, oddzielny defekt — normalizacja

Oryginalny v3 Appendix B deklaruje średnią po **czterech dwu-stanowych czynnikach**, tzn. dzielenie sumy przez `2⁴ = 16`, z odpowiednimi krotnościami `g_i` w miarach fazowych. Z powyższego kompletnego śladu:

`|Mbar|² = Σ|M|²/16 = 2 GF² mn mp B9_bracket`, ale wydrukowane (B.9) ma `GF² mn mp B9_bracket /16`.

Stosunek poprawnej wartości względem wydrukowanego prefaktora to dokładnie **32**. W (B.11) pierwszy wiersz zawiera `g_p/(4 mn mp)*|Mbar|²`; zastąpienie poprawnego `|Mbar|²` daje `g_p GF²/2 * B9_bracket`, dokładnie prefaktor drugiego wiersza wydrukowanego (B.11). Literalne użycie B.9 dałoby `g_p GF²/64`, tzn. **32 razy mniej**. Zatem B.11 wyraźnie używa prawidłowej normalizacji, nie literalnie wydrukowanej (B.9). Wynik REVIEW049 niezależnie zreplikowany.

## D. Reprodukcja i kontrola zewnętrzna

Program: `mech_s8_rot009_v3_B5_B11_trace_reproducer.py` (Python 3 + SymPy 1.14.0). Algorytm buduje gamma^0,..,gamma^3 z macierzy Pauli i gamma5, kontroluje antykomutatory, tworzy dwa tensory śladów 4×4, kontrahuje z `(+---)`, mnoży przez `GF²/2`, redukuje symbolicznie względem **ogólnych zmiennych**. Ponadto testuje dwa prefaktory B.11, trzy racjonalne kontrole, w tym przypadek `gV=gA` dający znikanie defektu znaku (negatywny falsyfikator). Elektron i neutrino w kontrolach osobnych są na powłoce masowej, choć cała hipotetyczna konfiguracja z nukleonami w spoczynku nie realizuje równocześnie dokładnego zachowania czteropędu. Wynik `SYMBOLIC_B5_SPINTRACE_PASS; THREE_RATIONAL_ON_SHELL_LEPTON_CONTROLS_PASS; B6_SIGN_PLUS_FAIL; B9_FACTOR_1_OVER_16_FAIL_BY_32; B11_RATE_PREFIX_CONSISTENT_WITH_CORRECT_B9`.

Źródłowy kontekst pomiarowy: reanaliza aSPECT 2024, https://doi.org/10.1103/PhysRevLett.132.102501, daje `a=-0.10402(82)`; dla `gA=1.2754` wynik LO z kształtu B.9 `a≈-0.10657`, a literalne B.6 dałoby `a≈+0.13544`. Znak z B.6 nie jest zgodny z pomiarem; szczegółowy kwantytatywny LO-vs-radiative/recoil test NIE był wykonany. **Nie należy utożsamiać różnicy a z przeliczeniem YP/beta PBH.**

## E. Odpowiedź właścicielska, HOLD

- `APPENDIX_V3_B6_SIGN_ERROR = EXACT_SYMBOLIC_CONFIRMED`.
- `APPENDIX_V3_B6_B9_PREFACTOR_32 = EXACT_SYMBOLIC_CONFIRMED`.
- `APPENDIX_V3_B9_BRACKET_SHAPE = CORRECT_WITHIN_B5_GAMMA_CONVENTIONS`.
- `APPENDIX_V3_B11_2ND_LINE_PREFACTOR = CONSISTENT_WITH_CORRECT_FULL_SPIN_AVERAGE`.
- `HISTORICAL_JCAP_FIG5_EXECUTION_OR_CODE_IDENTITY = OPEN`.
- `ARXIV_V3_CHANGED_SOURCE_CODE_AND_NATIVE_Yp_SCAN = NOT_AVAILABLE_IN_CHECKED_PUBLIC_AUTHOR_GITHUB_MASTER`.
- `ROT035_FULL_ODE_STRICT_EPS_CERTIFICATE = OPEN`.
- `PHYSICAL_BLACKHAWK_E4_SUBEDGE_VALIDATION = SOURCE_BLOCK`.
- `BW_INGEST = PENDING; REC11_INDEPENDENT_SIGN = PENDING; NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN`.

Werdykt: dwa błędy pośredniego zapisu manuskryptu v3, **brak dowodu błędu programowej fizyki**. Otwarta pozostaje redakcyjna dyspozycja do autorów, ale kontakt z autorami ani erata wydawcy nie są automatycznie inicjowane. Badacz REVIEW049 FIRST own sign-and-32; niniejszy obrót dostarcza niezależnego pełnego symbolicznego uzasadnienia source-pinned i jawne oddziela warstwy audytowe.