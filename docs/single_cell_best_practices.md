# Single-Cell Best-Practice Modes

The corpus uses conservative single-cell defaults: keep raw counts, preserve raw
annotations, record every transformation, and use biological evidence as a gate
rather than as an unchecked relabeling shortcut.

## Corpus Build Modes

Strict public counts mode is the default production path:

```bash
ipsc-corpus download-preprocess \
  --scope public \
  --download-counts \
  --require-counts \
  --validate-biology \
  --build-classifier-dataset \
  --resume \
  --out-dir /data/ipsc_corpus
```

This mode downloads only harmonization-ready counts or H5AD assets, writes
`layers["counts"]`, writes `layers["log1p_norm"]`, rejects non-count-like
matrices when `--require-counts` is set, and excludes failed/quarantined cells
from classifier artifacts by default.

Other useful modes:

```bash
# Inspect planned work without full external download
ipsc-corpus download-preprocess --scope public --dry-run --out-dir /tmp/ipsc_dry

# Revalidate existing harmonized outputs
ipsc-corpus download-preprocess --scope public --validate-only --out-dir /data/ipsc_corpus

# Avoid reference downloads while keeping marker-based biology checks
ipsc-corpus download-preprocess --scope public --no-reference-download --out-dir /data/ipsc_corpus

# Explicit research override; never the default
ipsc-corpus download-preprocess --scope public --allow-quarantined --out-dir /data/ipsc_corpus
```

## Normalization And Layers

The pipeline keeps count-backed data auditable:

```text
layers["counts"]       raw or count-like nonnegative expression
layers["log1p_norm"]   normalized/log1p expression for validation and projection
```

Count checks happen before downstream interpretation. Normalized or fractional
expected-count matrices are not silently treated as strict counts.

## QC Mode

QC is report-first. The pipeline computes and records metrics such as total
counts, detected genes, mitochondrial percentage when available, stress signal,
and doublet-like or mixed-lineage evidence. It does not silently remove cells
unless a rule is explicit, documented, and reproducible.

## Batch And Split Handling

The corpus does not erase batch structure by default. It preserves `dataset_id`,
`sample_id`, `donor_id`, `cell_line_id`, `clone_id`, and `batch_id`, then uses
those fields for validation, clustering evidence, and classifier split leakage
checks. If identifiers are unknown, `split_group_id` falls back conservatively
so unresolved groups do not leak across train, validation, and test.

## Clustering Mode

Clustering is an evidence layer, not biological truth. Per-dataset and
integrated clustering summarize label purity, marker-supported identity,
reference agreement, batch mixing, dataset mixing, donor mixing, and outlier
cells. Cluster evidence can support curation proposals only when it agrees with
metadata, marker modules, and reference projection.

## Gene And Species Mode

Human gene symbols and Ensembl IDs are checked against shared canonical gene
resources. Mouse genes remain species-specific unless a versioned human ortholog
projection is present. Mouse data can be harmonized and audited, but it is not
silently mixed into a human classifier feature space.

## Classifier Preprocessing Modes

`ipsc-corpus train-logstruct` exposes the single-cell preprocessing controls used
for classifier stress tests.

Default profile:

```bash
ipsc-corpus train-logstruct \
  --preprocess-profile sc_best_practices \
  --input-mode auto \
  --hvg-strategy auto \
  --normalize auto \
  --require-counts
```

Important modes:

```text
--preprocess-profile sc_best_practices
    Default. Uses Scanpy-style normalize_total/log1p behavior and records the
    normalization target.

--preprocess-profile legacy
    Compatibility profile. Sets a 10,000 target sum when no target is provided.

--input-mode auto
    Uses a combined expression H5AD when present; otherwise uses per-dataset
    harmonized H5AD files.

--input-mode per_dataset
    Loads per-dataset H5ADs and avoids forcing all data through one large H5AD.

--gene-mode union
    Aligns per-dataset matrices to the union of selected genes.

--gene-mode intersection
    Keeps only genes present across selected datasets.

--hvg-strategy per_dataset_union
    Selects highly variable genes per dataset and unions them for cross-dataset
    training stress tests.

--hvg-strategy global
    Selects highly variable genes after combining the selected data.

--hvg-flavor-counts seurat_v3
    Uses count-layer HVG selection when available.

--hvg-flavor-counts standard
    Saves counts, normalizes/log1p, then runs standard HVG selection.

--normalize auto
    Normalizes only when the matrix is count-like.

--normalize always / --normalize never
    Explicit override for controlled experiments.
```

## Recommended Defaults

Use these unless you have a reason to override them:

```text
Corpus build:        --download-counts --require-counts --validate-biology --resume
Biology:             marker + reference + clustering + timecourse evidence
Classifier data:     PASS + training_eligible + non-quarantined only
Training profile:    --preprocess-profile sc_best_practices
Input mode:          --input-mode auto
HVG strategy:        --hvg-strategy auto
Normalization:       --normalize auto
Quarantine override: off unless --allow-quarantined is explicit
```
