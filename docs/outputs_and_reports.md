# Outputs And Reports

Each run writes machine-readable manifests and human-readable summaries under
the selected `--out-dir`. Iterative runs write under `runs/iter_XXX/`.

## Core Reports

```text
download_manifest.csv
skipped_manifest.csv
harmonization_manifest.csv
validation_dataset_summary.csv
obs_schema_audit.csv
var_name_audit.csv
```

`download_manifest.csv` records URL, local path, status, SHA-256, file size,
retry count, parser, source kind, and license status.

`skipped_manifest.csv` records controlled-access, permission-required,
raw-read-only, non-scRNA, wrong-accession, unsupported-layout, no-count/H5AD,
license-excluded, and download-failed rows with evidence.

`validation_dataset_summary.csv` is the main per-dataset gate report. It records
technical status, biological status, inclusion status, failure or quarantine
reason, unknown annotation rate, mapped gene fraction, count-likeness, schema
status, var-name status, and training-eligible cells.

## Biology Reports

```text
marker_module_summary.csv
reference_projection_summary.csv
annotation_confusion_matrix.csv
timecourse_consistency_audit.csv
clustering_validation_summary.csv
clustering_label_confusion.csv
clustering_outlier_cells.csv
curation_proposals.csv
curation_applied.csv
quarantine_manifest.csv
```

These reports record the biological evidence stack: marker coverage and signed
scores, reference agreement, source-label confusion, timecourse progression,
cluster-label agreement, batch mixing, curation proposals, applied rules, and
quarantine decisions.

## Classifier Reports

```text
classifier_manifest.json
classifier_train_obs.csv
classifier_val_obs.csv
classifier_test_obs.csv
```

Classifier outputs include only cells that are technical PASS, biological PASS,
not quarantined, `training_eligible == true`, sufficiently labeled, and
license-compatible. Splits are group-aware to avoid leakage across dataset,
donor, cell line, clone, sample, or batch where those identifiers are available.

## Iteration Reports

```text
iteration_scorecard.json
iteration_summary.md
code_commit.txt
registry_snapshot.yaml
command_manifest.json
```

The scorecard tracks supported rows, audited skips, pass rates, quarantine rate,
unknown annotation rate, gene mapping, clustering agreement, classifier
eligibility, regressions, test status, documentation status, and promotion
candidacy.
