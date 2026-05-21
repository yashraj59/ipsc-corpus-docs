# CLI Reference

The command name is `ipsc-corpus`.

## Top-Level Commands

```text
parse-petropoulos            Parse Petropoulos/Lanner download HTML.
build-registry               Build registry, license audit, summaries, and attribution docs.
preview-metadata             Build metadata-only H5AD preview from metadata tables.
harmonize                    Legacy download/preprocess/harmonize command.
download-preprocess          Download, preprocess, harmonize, validate, and write reports.
iterate                      Run the self-improving corpus factory loop.
score-iteration              Score a completed iteration directory.
compare-iterations           Compare two iteration scorecards.
promote-best                 Promote a valid iteration as the best output.
build-classifier-dataset     Build classifier metadata/artifacts.
train-logstruct              Stress-test LogStruct on classifier labels and expression.
doctor                       Check runtime dependencies and registry readability.
paths                        Print resolved project/script paths.
```

## `doctor`

```bash
ipsc-corpus doctor [--out-dir /path/to/out]
```

Use before long runs. It verifies package importability, dependencies, registry
files, and optional output-directory access.

## `build-registry`

```bash
ipsc-corpus build-registry
```

Rebuilds generated registry files from durable source files. Do not hand-edit
generated CSVs; update durable registry inputs or source-link overrides instead.

## `download-preprocess`

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

Important options:

```text
--scope public                   Use public registry rows.
--registry PATH                  Override registry input path.
--out-dir PATH                   Required output/cache directory.
--download-counts                Download expression assets.
--require-counts                 Require count-like matrices.
--validate-biology               Run biological validation.
--no-validate-biology            Disable biological validation.
--build-classifier-dataset       Write classifier manifests/splits.
--max-datasets N                 Limit datasets for smoke/debug runs.
--download-workers N             Parallel download workers; default is 4.
--harmonize-workers N            Harmonization workers; default is conservative.
--validate-only                  Validate existing harmonized outputs.
--allow-quarantined              Explicitly include quarantined data.
--write-combined-expression-h5ad Write combined expression H5AD.
--no-reference-download          Skip external reference downloads.
--force                          Redownload/rebuild instead of reusing cache.
--resume / --no-resume           Reuse verified cache; enabled for normal runs.
--dry-run                        Plan/report without large external work.
```

## `iterate`

```bash
ipsc-corpus iterate \
  --scope public \
  --download-counts \
  --require-counts \
  --validate-biology \
  --build-classifier-dataset \
  --max-iterations 20 \
  --promote-best \
  --out-dir /data/ipsc_corpus
```

Use `iterate` when developing the corpus factory itself. It snapshots registry
state, runs the pipeline, scores the iteration, compares it to the previous best,
and promotes only if tests and validation gates hold.

Additional options:

```text
--iteration-id iter_001     Reuse or name a specific iteration directory.
--promote-best              Promote a passing candidate.
--no-run-tests              Skip test execution inside the loop.
```

## Iteration Utilities

```bash
ipsc-corpus score-iteration --run-dir /data/ipsc_corpus/runs/iter_014 --tests-passed
ipsc-corpus compare-iterations --old /path/to/old --new /path/to/new
ipsc-corpus promote-best --run-dir /data/ipsc_corpus/runs/iter_014
```

Use these to inspect completed runs without redownloading data.

## `train-logstruct`

```bash
ipsc-corpus train-logstruct \
  --input-mode auto \
  --preprocess-profile sc_best_practices \
  --hvg-strategy auto \
  --normalize auto \
  --require-counts
```

This command stress-tests classifier-ready outputs. It supports combined or
per-dataset H5AD input, union or intersection gene alignment, global or
per-dataset HVG selection, explicit normalization controls, group-aware splits,
repeated runs, CUDA device assignment, and dry-run preprocessing checks. See
{doc}`single_cell_best_practices` for the mode matrix.
