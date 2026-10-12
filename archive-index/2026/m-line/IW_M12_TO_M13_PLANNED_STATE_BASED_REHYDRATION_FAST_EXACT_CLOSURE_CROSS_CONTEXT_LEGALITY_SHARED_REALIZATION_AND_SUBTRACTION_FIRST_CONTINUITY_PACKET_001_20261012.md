---
artifact_id: M12-TO-M13-SUCCESSION-PACKET-READY-001
bw_ingestion_event_id: ING-20261012-0018
archive_mode: POINTER_ONLY
sync_state: SYNCED
legacy_full_body_commit: 7c925d17f9ddd28a0baff6487716e6772d384cd9
---

# M12 → M13 succession packet — public pointer

The full packet is retained in immutable Git history at commit `7c925d17f9ddd28a0baff6487716e6772d384cd9` and in private project custody.

Current public HEAD keeps only the safe identity/currentness pointer:

- BW event: `ING-20261012-0018`
- packet readiness did not itself establish activation;
- later M13 activation is a separate event;
- no private provider coordinates are published.

```text
SUCCESSION_PACKET_READY != ACTIVATION
POINTER_ONLY != PRIVATE_PACKET_BODY
HISTORICAL_FULL_BODY -> IMMUTABLE_GIT_HISTORY
```
