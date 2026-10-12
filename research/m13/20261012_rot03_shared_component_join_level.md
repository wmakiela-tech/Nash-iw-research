M13 ROT03 — Claim-relative join level (2026-10-12)
RETURN_ID: M13-ROT03-CLAIM-RELATIVE-JOIN-LEVEL-AND-CROSS-CONTEXT-COUPLING-GATE-001
STATUS: local exact compiler typing; no EXEC_SIGN / CANON / novelty / new task.


1. Wniosek z INT7 Thread093 i M12


INT7 dowiódł, że dla jednego wspólnego nośnika ukończeń i mapy zapominającej p mamy p(∩ A_c) ⊆ ∩ p(A_c). JOIN BEFORE FORGET jest konieczne, gdy twierdzenie wymaga jednej identycznej kompletnej realizacji.


M12 zdefiniował jednak inny przypadek: różne pełne realizacje lokalne mogą dzielić jeden legalny komponent. Wyniki te nie są sprzeczne. Zastąpienie poziomu komponentu pełnym przecięciem przypadkowo narzuciłoby silniejsze kryterium.


2. Twierdzenie — iloczyn włóknisty


Dla skończonej liczby kontekstów c, zbiorów A_c w legalnych nośnikach Theta_c oraz zadeklarowanych map s_c:Theta_c→Z zdefiniuj
P_Z = {(u_c) w iloczynie A_c : s_c(u_c)=s_d(u_d) dla wszystkich c,d}.


Przy braku innych ograniczeń między kontekstami P_Z jest niepuste wtedy i tylko wtedy, gdy przecięcie s_c(A_c) jest niepuste. Każde wspólne z ma jeden legalny lokalny preobraz w każdym A_c; odwrotnie każda krotka z P_Z wyznacza wspólne z.


Dla jednego pełnego u potrzebujemy natomiast przecięcia A_c w jednym nośniku, nie iloczynu włóknistego.
3. Przykład. Lokalny model A1 dopuszcza tylko uA, a lokalny model A2 tylko uB. Są różne jako pełne modele, lecz oba mają ten sam legalny komponent z. Nie ma jednej kompletnej wspólnej realizacji; istnieje jednak dopuszczalna para (uA,uB), zgodna na poziomie komponentu. Wniosek: wymaganie identycznego pełnego modelu odrzuciłoby ten prawidłowy przypadek.


4. Dodatkowa relacja legalności. Jeśli model źródłowy nakłada dodatkowy kontrakt R na krotki lokalnych realizacji, kryterium częściowej zgodności brzmi: istnieje krotka należąca równocześnie do R oraz do P_Z. Samo przecięcie obrazów s_c(A_c) nie gwarantuje wtedy zgodności. R musi być uzasadnione przez źródło, a nie dodane po fakcie.


Kontrprzykład dla relacji R: dwa lokalne nośniki mają wartości 0 oraz 1, oba dopuszczają każdą wartość, a mapy komponentu są identycznościami. Wspólne obrazy zawierają zarówno 0, jak i 1. Niech jednak R dopuszcza tylko pary (0,1) oraz (1,0). Wówczas żadna krotka nie jest jednocześnie zgodna z R i nie ma równych komponentów. R-przecięcie z P_Z jest puste.


5. Target i transport


Gdy tau_c = rho_c po s_c, wspólny komponent z wyznacza target jako rho_c(z). Same równe komponenty nie gwarantują liczbowo równych targetów, jeśli mapy rho_c są różne. Potrzebna jest deklarowana relacja transportu. Odwrotnie równe targety nie dowodzą wspólnego komponentu bez dodatkowych przesłanek, np. iniektywności.
6. Pola kompilatora


JOIN_LEVEL = FULL_COMPLETION | SHARED_COMPONENT | TARGET_ONLY | TRANSPORTABLE_QUERY | UNRESOLVED
SHARED_COMPONENT_JOIN = FIBER_PRODUCT_OVER_LEGAL_Z
CROSS_CONTEXT_COUPLING = INDEPENDENT_PRODUCT | LEGAL_RELATION_R | UNRESOLVED
ADMISSION_CHECK = FULL_INTERSECTION | COMPONENT_FIBER_PRODUCT | R_RESTRICTED_FIBER_PRODUCT


FULL_SHARED_OBJECT, SHARED_COMPONENT, TARGET_ONLY i TRANSPORTABLE_QUERY to różne poziomy roszczeń. Matematyka to dojrzałe iloczyny włókniste zbiorów. M13 proponuje jedynie poprawkę claim-typing.


REV020 ACTIVE; REV021 NOT_CREATED; TPE HOLD.
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_HEAD_CHANGE / NO_NEW_TASK.
Źródła i routing
INT7 Thread093 (commit 601e6f67118e33964a35e9b6b5d0245dd5acf54a):
https://github.com/wmakiela-tech/Nash-iw-research/blob/601e6f67118e33964a35e9b6b5d0245dd5acf54a/archive-index/2026/int7/int7_thread093_completion_join_before_forgetful_projection_20261012.md


M12 partial shared component:
(private Drive source; original locator retained in BW)


LT3 to LT4 succession packet 003:
(private Drive source; original locator retained in BW)


ROUTE_TAGS: IWTO_INT7 IWTO_MT13 IWTO_LT3 IWTO_LT4 IWTO_REC9 IWTO_PRF10 IWTO_KN9 IWTO_MODERATOR.