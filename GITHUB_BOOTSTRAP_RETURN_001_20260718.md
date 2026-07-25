# NASH–IW GitHub Bootstrap Return

```yaml
packet_id: "NASH_IW_GITHUB_BOOTSTRAP_001_20260718"
status: "LOCAL_VALIDATED / READY_FOR_GITHUB_COMMIT / NOT_COMMITTED"
target_repository: "wmakiela-tech/Nash-iw-research"
target_branch: "bootstrap/repository-structure"
target_pr_state: "DRAFT"
canon_merge: false
exec_sign: false
claim_upgrade: false
```

## USAGE_INSTRUCTION

```yaml
purpose: >
  Utworzyć minimalną, testowalną infrastrukturę repozytorium NASH/IW.
primary_recipient: "MGPT / GitHub repository administrator"
exact_next_step: >
  Po przywróceniu konektora utworzyć branch bootstrap/repository-structure,
  wgrać pliki z pakietu i otworzyć draft pull request z treścią
  BOOTSTRAP_PR_BODY.md.
order_dependency: "po potwierdzeniu prywatności repozytorium"
moderator_action_required: false
consequence_if_unused: >
  Repozytorium pozostanie bez CI, szablonów, walidatora manifestów i
  kontroli claim boundary.
```

## Zakres

Pakiet zawiera governance, Pythonowy walidator manifestów SHA-256, CLI,
testy jednostkowe, JSON Schema, workflow GitHub Actions, szablon PR,
formularz research gate oraz indeksowanie artefaktów zewnętrznych.

## Wyniki lokalne

```yaml
unit_tests: PASS
compileall: PASS
manifest_validation: PASS
NCDG_runtime: NOT_INCLUDED
adjusted_transport: NOT_INCLUDED
```

## Granica

Zielony CI nie nadaje EXEC_SIGN, nie wykonuje canon merge i nie podnosi
statusu twierdzeń naukowych.
