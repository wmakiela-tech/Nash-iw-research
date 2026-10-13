# NASH/IW — Private Drive document organization and Slack navigation

**Status:** FORWARD_STORAGE_ROUTING_ACTIVE / BOUNDED_2026-10-13_CLEANUP_PASS  
**Date:** 2026-10-13  
**Owner function:** SYSS4 / systems and cross-surface custody.  
**Authority ceiling:** navigation/custody only; no scientific adoption, CANON, or EXEC_SIGN.

## Purpose and safety boundary

The Moderator requested project-document organization with clear role separation:

- **GitHub:** complete scientific work that has been explicitly classified safe for public release, with code/fixtures/reproduction where legal and possible.
- **Private Google Drive:** project-private documents, restricted originals, manuscripts, lineage/succession packets and nonpublic source custody.
- **BW:** original source identity, committed ING event, qualified status/currentness, private source, public Git path and immutable commit.
- **Slack:** current messages, return routing, live dialogue and alert transport. Slack threads must be searchable as science-bearing source records if they were the only full copy.

**Organization must not rewrite the history of scientific evidence.** A Drive move preserves the same file ID and must not become a duplicated BW scientific event; moving a file does not by itself establish a new science claim or public-release permission. Do not move BW registry or established historical succession folders just to normalize presentation.

## Drive — where new private documents go

The already existing project root `NASH–IW Shared Research Bridge` has current-applicable documents, architecture, BW/knowledge and governance/handoffs trees. These original locations remain intact.

A new sibling subtree under the existing root is:

`04_PRIVATE_PROJECT_DOCUMENTS_CURRENT/`

| Folder | Intended document class |
|---|---|
| `00_TRIAGE_NEW_AND_UNCLASSIFIED/` | Temporary intake for files without verified identity/exposure; no acceptance implied |
| `01_CELL_SUCCESSION_AND_HANDOFF_PACKETS/` | Planned/emergency succession, cell role, recipient handoff packets |
| `02_PRIVATE_SCIENTIFIC_SOURCE_AND_REVIEW/` | Private source originals and reviews, including originals whose public-safe scientific bodies live in GitHub |
| `03_MONOGRAPHS_AND_LIVING_BOOKS/` | Draft books, literature foundation maps, living-book educational documents and monograph editorial material |
| `04_REPRODUCTION_DATA_CODE_PACKAGES/` | Restricted or internal code, JSON/ZIP bundles, checks, receipts and data not yet classified for public GitHub |
| `05_SLACK_SOURCE_RECOVERY/` | Complete science messages independently restored from Slack, with original timestamp and source identity |
| `06_SYSTEM_OPERATIONS_AND_GOVERNANCE/` | Internal system review, architecture, governance and operations (not replacements for controlling policy) |
| `99_BLOCKED_HOLD_AND_EXCEPTION/` | Empty shells, denied writes and unresolved custody conflicts, explicitly *not* validated source bodies |

Place each document by **function and exposure class**, not simply by submitting cell or upload date. Names are searchable; stable artifact IDs control identity. Within a major folder, lineages may be subdivided in future only when actual density requires it. Do not create a new folder for every rotation.

### Migration and readback requirements

1. Identify the source file and its current parent using Google metadata.
2. Confirm the destination folder and access/sharing semantics. When uncertain, classify `HOLD`.
3. Move with `addParents` for target and `removeParents` for the exactly verified old parent, preserving the same ID.
4. Read back the parent, file ID, and availability. Do not copy documents just to change location.
5. The location change does **not** alter BW scientific lifecycle, original source event, or public GitHub commit.
6. Preserve older established lineage/frozen archives and shared-drive permissions. No indiscriminate destructive reorganization.

### Bounded migration evidence

The 2026-10-13 first live cleaning pass moved and independently verified **56** owner-only My Drive root files, with the same IDs: 8 succession packets, 20 source/reviews, 8 books, 8 code/data/reproduction artifacts, 9 source-recovery documents, 2 systems/governance documents, and 1 explicitly blocked/empty recovery shell. The latter was placed in `99_BLOCKED_HOLD_AND_EXCEPTION`; this **does not** resolve its source-copy failure. No assertion is made that all project files or history were exhaustively migrated. Existing BW / governance / historical-campaign trees were not moved.

## Slack — source, alert and dispatch routing

Only one lightweight navigation channel was added; the existing four IW channels were left intact. Do **not** mass-forward existing science threads into a new channel: it severs native message identity, sender context, thread provenance and receipt semantics.

| Channel | Role |
|---|---|
| `#iw-start-here` | Stable navigation/index, not an additional scientific task inbox |
| `#iw-dispatch` | Formal cross-cell routing, scientific-return notices, receipts and actionable handoffs; preserve original return thread |
| `#iw-alerts` | Material critical/high risk signals, blocks and authorized global decisions |
| `#iw-live-dialogue` | Small bounded model-to-model sessions; explicit `FROM_CELL` / participant identity |
| `#iw-nc-inbound` | Existing independent private NC inbound; never change its visibility as an organization shortcut |

Slack Canvas could not be created on the current plan (`not_supported_free_team`). A durable `#iw-start-here` index message and a cross-reference from `#iw-dispatch` were created instead. The public-safe rules are in this file; private Drive folder locators and document IDs are **not** included in the public repository.

## Scientific return filing rule

```text
PUBLIC_SCIENCE -> COMPLETE_GITHUB_RESEARCH_BODY
PRIVATE_SOURCE_OR_PACKET -> GOOGLE_DRIVE_PRIVATE_DOCUMENT
RESULT_STATUS_AND_SOURCE_PROVENANCE -> BW_ING + CROSS_SURFACE_CUSTODY
SLACK -> ORIGINAL_MESSAGE_TRANSPORT_AND_THREAD_SEARCH
```

For a public-safe work result, create one complete canonical science body in GitHub and link the **same original artifact identity** to BW. An ordinary private Drive original may be retained for provenance, but the project should not treat a GitHub `POINTER_ONLY` file as completed publication. Public/private release eligibility is determined from actual content and access rules, not by folder name.

**Exceptions:** The prior `INT7 Thread076` document shell is empty due to a provider safeguard, even though the original Slack science return and BW event remain. Its placement in the exception folder marks this fact and does not bypass or retry a blocked provider operation. Old public GitHub commit revisions with private-provider coordinates also remain a separate security hold; Drive moves cannot erase historical public Git records.

## Triggered maintenance, not ritual

At a relevant new upload, Slack-only scientific body, failed write, source mismatch, or search failure, classify only the affected source and file it correctly. Future folder audits may sample accumulated unclassified source documents, using stable IDs and restrictions; they are not a mandatory prerequisite for scientific work.

**Non-collapse:** `FILE_MOVED != SCIENCE_RECLASSIFIED`; `MESSAGE_POSTED != BODY_SAVED`; `FULL_BODY_RECOVERED != ACCEPTED`; `INDEX_EXISTS != ALL_PROJECT_HISTORY_AUDITED`.
