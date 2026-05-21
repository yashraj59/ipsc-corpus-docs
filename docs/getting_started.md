# Getting Started

## Install

```bash
git clone https://github.com/yashraj59/ipsc-corpus-kit.git
cd ipsc-corpus-kit
pip install -e ".[dev,biology]"
ipsc-corpus doctor
```

`doctor` checks Python and the core runtime libraries, including `anndata`,
`h5py`, `numpy`, `pandas`, `pyarrow`, `requests`, `scanpy`, `scipy`, `tqdm`,
`yaml`, and the required registry files.

## Build The Registry

```bash
ipsc-corpus build-registry
```

This rebuilds registry CSVs and the public source-link audit from durable
registry/link files. It also refreshes the development-stage audit, including
`development_stage`, `development_stage_ontology_term_id`, and
`development_stage_harmonized`. It should be run before a full corpus build.

## Build The Public Corpus

For normal users, this is the main command:

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

On a new server with no cache, the first run downloads public assets once. Later
runs reuse verified files under `/data/ipsc_corpus/downloads` when `--resume` is
enabled. Use `--force` only when you intentionally want to redownload.

## Normal Users Versus Maintainers

Most users should run `download-preprocess`. The `iterate` command is for
maintainers and coding agents changing parsers, registry rules, validation, or
curation logic. The promoted corpus was created through `iterate`, so users can
rebuild it with the simpler command above.

## Quick Smoke Test

Use this when checking an installation without full downloads:

```bash
ipsc-corpus download-preprocess \
  --scope public \
  --max-datasets 2 \
  --download-counts \
  --require-counts \
  --validate-biology \
  --build-classifier-dataset \
  --dry-run \
  --out-dir /tmp/ipsc_corpus_smoke
```
