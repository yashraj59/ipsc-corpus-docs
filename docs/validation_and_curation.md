# Validation And Curation

## Technical Validation

Technical validation runs before biological interpretation. It checks file
integrity, AnnData shape, unique obs and var names, count-likeness, required
layers, metadata alignment, standardized vocabularies, gene mapping, QC fields,
and classifier eligibility gates.

Required layers:

```text
layers["counts"]       nonnegative count-like expression
layers["log1p_norm"]   normalized expression for validation/projection
```

## Obs Harmonization

Raw source annotations are preserved. Standardized columns are derived from
parsers, registry metadata, shared vocabularies, and versioned curation rules.
Important columns include `dataset_id`, `source_accession`, `source_annotation`,
`cell_type_coarse`, `cell_type_fine`, `qc_label`,
`development_stage`, `development_stage_ontology_term_id`,
`development_stage_harmonized`,
`reprogramming_stage_harmonized`, `biological_validation_status`,
`technical_validation_status`, `training_eligible`, and `split_group_id`.

Unknown values are allowed when they are true unknowns, but unknown rates are
reported and weak labels are excluded from classifier training by default.

## Development Stage Harmonization

Development stage is tracked separately from in-vitro differentiation or
reprogramming state. Parsers preserve raw source stage text in
`development_stage`, preserve ontology IDs in
`development_stage_ontology_term_id` when supplied, and derive
`development_stage_harmonized` from versioned code and vocabulary.

The harmonized vocabulary includes embryo stages such as
`preimplantation_embryo`, `cleavage`, `morula`, `blastocyst`, `gastrulation`,
and `postimplantation_embryo`, plus `fetal`, `neonatal`, `pediatric`, `adult`,
`aged_adult`, `organoid_or_in_vitro_stage`, and `in_vitro_pluripotent`.
`ipsc-corpus audit-development-stage` validates the registry-wide mapping and
uses publication or PubMed hints only when title evidence matches the registry
record.

## Gene Symbols And Species

Human symbols and Ensembl IDs are validated against shared canonical gene
resources in `data_registry/shared`. Mouse genes are kept species-specific unless
a durable ortholog projection is available. Mouse rows without a versioned human
ortholog projection can be harmonized and reported, but are not silently mixed
into the human classifier feature space.

## Biological Evidence Stack

Biological validation combines:

- signed marker modules and anti-markers
- stress, mitochondrial, ribosomal, and cell-cycle confounders
- reference projection
- source-label versus standardized-label confusion
- timecourse consistency
- per-dataset and integrated clustering
- sample, donor, cell-line, clone, and batch metadata
- classifier agreement as supporting evidence only

Marker scores and clustering are not treated as sole truth. Relabeling requires
agreement across metadata, marker evidence, reference evidence, and validation
context. Ambiguous cases produce warnings or quarantine.

## Quarantine

Technical failures block inclusion. Biological contradictions quarantine by
default. Quarantined data remains auditable but is excluded from combined outputs
and classifier artifacts unless `--allow-quarantined` is explicitly set.

Common quarantine reasons include clean iPSC labels with fibroblast-dominant
profiles, weak unknown-heavy annotation, unsupported embryo-like labels,
stress-dominant identity, reversed timecourses, or high-confidence reference and
marker disagreement.

## Curation Learning

Validation produces `curation_proposals.csv`. Accepted rules are written to
`data_registry/curation_rules.yaml` and applied reproducibly in later runs.
Accepted rules must preserve raw annotations and should have regression tests.
