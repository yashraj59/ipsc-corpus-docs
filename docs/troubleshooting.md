# Troubleshooting

## `doctor` Fails

Reinstall with biology and development extras:

```bash
pip install -e ".[dev,biology]"
ipsc-corpus doctor
```

If `scanpy` or plotting dependencies are unavailable, technical validation can
still run, but biology and clustering features may degrade.

## Downloads Are Slow

Use the default parallel downloader first:

```bash
ipsc-corpus download-preprocess --download-workers 4 --resume --out-dir /data/ipsc_corpus
```

Keep `/data/ipsc_corpus/downloads` mounted across runs. Do not use `--force`
unless you need to redownload.

## A Dataset Is Skipped

Check `skipped_manifest.csv`. Skips are expected for controlled access,
permission-required, raw-read-only, non-scRNA, wrong-accession,
unsupported-layout, no-count/H5AD, and license-excluded rows.

## A Dataset Is Quarantined

Check `quarantine_manifest.csv`, `marker_module_summary.csv`,
`reference_projection_summary.csv`, and clustering reports. Quarantine means the
data remains auditable but is excluded from combined/classifier outputs by
default because technical or biological evidence was not safe enough.

## Classifier Cell Counts Look Lower Than Total Cells

Classifier artifacts are intentionally stricter than the corpus. They exclude
failed, quarantined, weak-label, unknown-label, license-incompatible, and
leakage-risk cells by default.

## Full Run Is Too Large For A Laptop

Run a dry smoke test locally and use a server for the full corpus:

```bash
ipsc-corpus download-preprocess --scope public --max-datasets 2 --dry-run --out-dir /tmp/ipsc_smoke
```

For production, use a persistent output directory with enough disk space for
downloads, harmonized H5ADs, reports, and classifier outputs.
