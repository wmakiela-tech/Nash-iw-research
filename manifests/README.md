# Manifests

Store small machine-readable custody and reproduction manifests here. A manifest is evidence of integrity and provenance, not automatic scientific authorization.

For load-bearing computational or empirical work:

- follow [the current work and reproducibility protocol](../docs/WORK_AND_REPRODUCIBILITY_PROTOCOL.md);
- start from [the reproduction-manifest template](../templates/IW_RESEARCH_REPRODUCTION_MANIFEST_TEMPLATE.json);
- validate against [the reproduction-manifest schema](../schemas/research-reproduction-manifest.schema.json);
- preserve exact code/environment/commands, inputs and outputs with checksums, parameters/seeds/tolerances, controls, failures and reproduction status.

General custody manifests may continue to use the lighter existing artifact schema where full scientific reproduction is not applicable.

```text
MANIFEST_VALID != SCIENTIFIC_VALIDATION
RESULT_REPORTED != RESULT_REGENERABLE
```
