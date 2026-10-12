# Cross-surface manifests

This directory contains **derived public-safe projections** connecting immutable GitHub artifacts to the private BW event/currentness ledger.

These manifests:
- use stable artifact/contribution IDs;
- may expose BW ingestion event IDs;
- record GitHub path/commit and archive mode;
- never override BW lifecycle/qualification;
- never publish private Drive/Slack locators;
- are reconstructible and disposable if BW/Git history can rebuild them.

A missing manifest row does not invalidate an artifact. A manifest contradiction is a custody/currentness defect and should be resolved against BW + immutable Git history.

See `docs/STORAGE_AND_SYNC_POLICY.md`.
