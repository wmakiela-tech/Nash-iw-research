# XH-S4 — obrót 015 / 1 maja–23 października 2026

**RETURN_ID:** XH-S4-MAY-OCT2026-DCP-STATION-FC-SU2-POSITIVITY-015_20261023  
**Tryb:** zewnętrzne badania naukowe → pytania → powiązania typowane → hipotezy → falsyfikatory.  
**Status:** PRIMARY_FULLTEXT_REVIEW / QUESTIONS_READY / NOT_INDEPENDENT_PROOF_REPLICATION / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_NASH_CLAIM / NO_BW_INGESTION / NO_NEW_OWNER_TASKS.

## 1. Czas i wiarygodność

Zakres 2026-05-01—2026-10-23. Wersje: Ning et al. `2609.09219v2` (v1 7 IX, v2 28 IX); Chung/Du/Wesley `2608.23691v2` (24 VIII, aktualizacja 14 IX); Firsching et al. `2605.13171v1` (13 V); Verhoeven `2610.19791v1` (14 X); Lee/Melville PRD DOI `10.1103/nh6r-x6nq` publikacja 6 VII, ALE pierwotny arXiv `2512.20706v1` z 23 XII 2025, zaktualizowany do publikacji 27 VII. Kallel/El Louadi `2608.28997v1` (29 VIII) jako dodatkowy tekst o granicach audytu. Wszystkie twierdzenia o wynikach autorów są źródłowe; nie wykonano pełnego audytu matematycznego ani ponownej oceny benchmarków.

## 2. Q18 — czy informacja eksperymentalna była konieczna do uzyskania wyniku?

Źródło: Ning, Zhong, Li, Zeng, *Scores Alone Do Not Prove Discovery*, https://arxiv.org/html/2609.09219v2. DCP: Gate1 rejestruje i potwierdza użyteczność artefaktu w niezależnej ewaluacji; Gate2 uruchamia matched challenger z początkowym kontekstem K,E0 i zaobserwowanymi bajtami Web W_obs, ALE BEZ nowych danych pomiarowych i dziennika prób; wystarczy pojedynczy spełniający próg challenger, by obalić Core dla zarejestrowanego budżetu. Core PASS wymaga również sprawności kontroli pozytywnych i granicy nieodtworzenia. Gate3 na wspólnym checkpoint porównuje dostarczanie prawdziwego feedbacku z neutralnym, z kontrolą null-policy; kwalifikuje efekt w obrębie protokołu, nie globalne pierwszeństwo naukowe.

Autorzy: n=96, zero odtworzeń, one-sided `alpha=.01`: `p_upper=1-.01**(1/96)=0.0468381168`; prawdopodobieństwo wykrycia co najmniej jednego odtworzenia przy prawdziwym p=.01: `1-(.99)**96=.6189528819`. Ostatnia liczba pokazuje małą moc do wykrycia bardzo rzadkich alternatyw. Test dotyczy konkretnego rozkładu niezależnych uruchomień Q_B, tożsamości modeli i budżetu; nie dowodzi, że żaden model ani matematyk nie odzyska wyniku.

**Pytanie Q18:** co w eksperymencie IW jest wkładem informacji zwrotnej z danych, a co odtworzeniem uprzedniej wiedzy? H_data (bez nowych danych wynik nieodtwarzalny w zadanym budżecie), H_prior (wystarcza wiedza startowa), H_interaction (feedback poprawia odzysk). **Test:** prerejestracja tego samego mierzalnego celu, zadeklarowanie granicy informacji, sekwencja 1) sealed utility 2) matched budget challenger 3) paired true/neutral feedback przy stałym checkpoint. Sukces pojedynczego challengera veto hipotetyczny Core. Zgoda z wynikiem nie stanowi automatycznie dowodu nowości teoretycznej.

## 3. Q19 i Q23 — niezależność modeli, archiwum wiedzy i ich interakcja

Źródło: Chung, Du, Wesley, *Autonomous Mathematical Discovery in an Open-World Multi-Agent Environment*, https://arxiv.org/html/2608.23691v2 (Station). 12 zadań AlphaEvolve + 2 studia; w 5/12 autorzy deklarują wyniki nowe względem literatury, wszystkie wybrane sukcesy oparte na dokładnych konstrukcjach albo dowodach Lean (wg autorów, bez naszej niezależnej repliki). Wśród 28 wyróżnionych wyników 13 korzysta z kilku rodzin modeli; 21/28 korzysta z wcześniejszych publikacji. W demonstracji: 125 przyjętych prac i 923 krawędzie cytowań w pierwszym zadaniu kissing number, 55 prac przynajmniej raz odrzuconych, 199 odrzuceń zgłoszeń. Wynik liczbowy: 604 poprawne punkty w d=11; ablacją są brak archiwum ORAZ osobno sześć agentów Claude zamiast wielorodzinowych, porównane w trzech seedach przez 500 ticków. Obie ablacją miały gorsze wyniki. Baselines równanymi minutami ewaluatora w jednym zadaniu NIE są automatycznie dopasowane pod całkowity koszt tokenów i godzin ludzi.

**Q19:** jaki czynnik poprawia odkrycia — różnorodność, wymiana wiedzy, polityka recenzji czy eksperyment naukowy poza metryką? **Q23:** czy dostępność archiwum i różnorodność modeli dają niezależne korzyści czy pozytywną interakcję? Autorzy nie przedstawiają pełnego 2x2.

**Projekt testu 2x2:** Y11=different_models+archive, Y10=different_models+no_archive, Y01=single_family+archive, Y00=single_family+no_archive; interaction Δ=(Y11-Y10)-(Y01-Y00). Identyczne zadanie, budżet efektywnych ewaluacji i tokenów, nowi agenci bez ukrytej pamięci zablokowanej ablacji, ślepy krytyczny review, kilkanaście lub więcej powtórzeń jeśli analiza mocy pozwoli. Mierzyć oddzielnie: poprawne konstrukcje, nowe twierdzenia, wycofane błędne tezy i utracone prawidłowe wyniki. Bez Y00 interakcji nie da się określić z istniejących par ablacjach. NASH archiwum BW/Slack/Drive/GitHub i różnorodność modeli wyznaczają możliwy eksperyment; nie ma twierdzenia, że Station dowiodła optymalności architektury IW.

## 4. Q20 — różne obcięcia tego samego obiektu nie muszą zachowywać tego samego niezmiennika skończonego poziomu

Źródło: Matt Verhoeven, *Spectral truncations of SU(2) and the spectral localizer*, https://arxiv.org/html/2610.19791v1. Theorem 3.12: dla skończonych obcięć Peter–Weyla R_Lambda spójnej zwartej grupy Liego: C*-envelope=M_N(C) i `prop(R_Lambda)<=2` (założenia w pracy). Dla Dirac-spinor SU(2) Theorem 4.10: C*-envelope=M_N(C), lecz tylko `2<=prop(S_J)<=8` dla całej rodziny; numerycznie J=0,1/2,1 daje `prop(S_J)=4` — to zaobserwowane przypadki, nie dowód na prop=4 dla wszystkich J. Ta różnica FINITE OPERATOR SYSTEM wskazuje, że sposób obcinania zmienia algebraiczną strukturę, nawet jeśli macierzowy envelope jest pełny.

Odd spectral localizer `L_(κ,ρ)=[[κDρ,Xρ],[Xρ*,−κDρ]]`. Z istniejącego theorem 5.6 legalny indeks certyfikuje nierówności κ<=g^3/(12||X|| ||[D,X]||) oraz ρ>=2g/κ. Przy STAŁYM skończonym ρ warunek drugi NIE może utrzymać się przy κ→0. Nowe dane numeryczne dla wybranych reprezentacji SU2 wskazują nawet faktycznie niewłaściwy indeks w tej granicy. Z faktu braku warunku theorem nie wynika automatycznie fałsz indeksu; tu autor daje dodatkowe wykresy, nie niezależny dowód ogólny.

**Q20:** czy DTC/NCDG badane obserwable/indeksy są w ogóle zdefiniowane na odpowiednim typie operator system, czy zależą od wyboru Peter-Weyl/Dirac/spectral-projector? **Falsifier:** dla jawnej SU2/referencyjnej reprezentacji z pracy, przeliczyć signature w siatce (J,κ,ρ), porównać z analitycznym indeksem i prop(R),prop(S); dopiero po zdefiniowaniu legalnego embedding/miary można szukać analogów dla TT. ŻADNE twierdzenie o NASH K_A/J3 z tego nie wynika.

LINK: wrześniowy Camper/Giannakis/Hoefer https://arxiv.org/html/2609.40189v1 zbieżność operator systems w quantum GH dla co-amenable compact quantum group z L1 approximate identity. Październik Bhatt/Guin/Sharma 2610.01132 GH state spaces dla n-torus. FEEC Boffi et al. 2610.01501 operator-norm/pseudospectrum. **RÓŻNE typy**: GH stanów ≠ liczba propagacji finite operator system ≠ legalność spectral localizer index ≠ pseudospektralna norma, niezależnie od wspólnego hasła 'spectral convergence'.

## 5. Q21 — propagator: osobne dodatniości i właściwy formalizm korelatorów

Lee, Melville, *Propagator positivity bounds for cosmological correlators*, PRD 114 023504, JULY 6 2026 https://doi.org/10.1103/nh6r-x6nq ; arXiv `2512.20706v1` preprint Dec23 2025, v2 July27. Źródło peer-reviewed. Właściwy host: ciężkie pola w de Sitter, efektywna teoria propagatora z kosmologicznymi warunkami `in-in`, współczynniki ograniczone nieskończoną wieżą obustronnych nierówności z unitarności i przyczynowości; dotyczy też sygnałów primordial non-Gaussianity. Brak zgodnego modelu NASH nie pozwala użyć samych inequality.

**Q21:** czy przyszły propagator NASH w określonym stanie, czasoprzestrzeni i konturze in-in może spełnić source-native positivity inequalities i późniejszy test Matsui 2610.25994 P/D/C? Model H_both spełnia wspólny host po odrębnym wykazaniu założeń, H_nonmap wymogi Minkowski linear mediator i de Sitter heavy-in-in nie pokrywają się. Najtańszy test: zapisać D, spektrum, stany, warunki brzegowe, źródła i ograniczenia EFT, następnie policzyć pierwsze dwa współczynniki/wavefunction time integrals; nie importować nierówności bez derivation. ALSO nonlocal Dirac 2610.06390 branch/residue and RR 2610.20720 retarded inverse operator are DISTINCT source types.

## 6. Q22 — czy dowód dotyczy problemu, który faktycznie postawiono?

Firsching et al., *Formal Conjectures*, https://arxiv.org/html/2605.13171v1, May13: 2615 formal statements, 1029 open research conjectures, 836 solved research problems; w bazie 291 fixed misformalizations, 48% misrepresentation and 35% semantic from all fixed cases. Levels Translation / Underspecified / Source; each can yield Lean-checked irrelevant theorem. API categories research-open/solved/textbook/test, 467 test statements, 155 API statements in frozen tag of paper. `answer(sorry)` allows value/proposition search distinct from proof; frozen 100+100 benchmark snapshots bind Lean/Mathlib version. Immutable snapshots permit comparisons even after semantic bug repairs only in next release.

**Q22:** can IW require a theorem `source_original -> formal_target -> proof_certificate` independent of whether each locally passed? Minimum discriminator: audit text span, quantifiers, premises, definitions and counterexamples on sample of old IW claims, with deliberate synthetic dropped-hypothesis falsifier. Source and exact formal_statement hash separate; proof of wrong formal statement != source claim. Pair with Fried 2610.22281 and Bolzano 2610.09769; KN/REC process custody, no canon change.

Additional conceptual source: Kallel/El Louadi https://arxiv.org/html/2608.28997v1 Aug29 distinguishes derivational validity, representational fidelity and epistemic significance; source reports August OpenAI Lean 20.6MB proof vs 55.6KB statements (379x) with 218 bespoke definitions, but figures are THEIR count, not independently re-audited here. Significant expert review cannot be replaced by test PASS.

## 7. EVIDENCE LEVEL and priority

Source material is arXiv/journal fulltext reviewed, except physical journal APS article readable primarily as abstract; no original Lean builds, numerical SU2 reproduction, or model budget factorial experiments performed. Numerical 0/96 confidence calculation independently checked arithmetically and exact source formula verified. No NASH host transfer (DTC/TT, Front B), no novel claim.

Priority P0: Q20 (new algebraic/finite spectral question), Q18 (audit information contribution), Q22 (statement fidelity), Q23 (factorial IW), Q21 (future phys formal host only). P1 Q19 holistic research community design. No new owner tasks. Durable GitHub save/readback is not BW ingestion.