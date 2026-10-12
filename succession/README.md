# Succession

This directory contains **public-safe succession pointers/manifests**, not private packet bodies by default.

Canonical forward location:

```text
succession/<YYYY>/<lineage>/<pointer>.md
```

A succession pointer may expose:
- stable packet/artifact identity;
- BW ingestion event;
- safe lifecycle/currentness typing;
- supersession relation;
- public-safe guards such as `SUCCESSION != ACTIVATION`.

It must not expose private Drive/Slack locators, protected scientific payloads, or restricted packet content.

Private packet custody and applicability resolve through BW/private project sources.

```text
POINTER_ONLY != PACKET_BODY
SUCCESSION != ACTIVATION
GITHUB_POINTER != DELIVERY
```

See `../docs/STORAGE_AND_SYNC_POLICY.md`.
