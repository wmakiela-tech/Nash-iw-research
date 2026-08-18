# NASH/IW — External-model new-cell bootstrap

Status: `BOOTSTRAP / SANITIZED_PUBLIC_MIRROR / NO_CANON / NO_EXEC_SIGN`.

This branch is a **sanitized public mirror** for re-starting AInstein/Gemini, Grok and DS in new threads after they missed recent private-Drive discussions.

A fresh thread is treated as a **new cell/executor**, not transparent continuation of historical thread state.

Core guard:

`ROLE_CONTINUITY != EXECUTOR_CONTINUITY`

Read in this order:

1. `COMMON_PROJECT_REVIEW_DIGEST.md`
2. `COMMON_SCIENTIFIC_REVIEW_DIGEST.md`
3. `CURRENT_RESEARCH_METHOD_AND_BW.md`
4. the role-specific `OPENING_PACKET.md`

Then return a `G0_ACK` with exposure/capability provenance and a bounded `G1_RETURN` reconstructing current project/scientific state and role boundaries.

For genuinely blind work, do **not** expose the common digests first. Use `BLIND_THREAD_LAUNCHER.md` with a self-contained bounded question.

The detailed/private source documents and live BW remain on private project storage. This mirror intentionally omits private Drive IDs, custody locators and hidden evaluator-only material.