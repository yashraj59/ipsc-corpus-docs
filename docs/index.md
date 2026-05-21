# iPSC Corpus Kit

```{image} _static/ipsc-corpus-kit-logo.png
:alt: iPSC Corpus Kit logo
:width: 260px
:align: center
```

iPSC Corpus Kit is a reproducible, agentically curated corpus factory for public
iPSC, reprogramming, pluripotency, embryo-model, and lineage-drift single-cell
datasets. The corpus was built through an iterative development loop where
agents discovered public sources, audited downloadability and licensing,
downloaded count-ready data, harmonized metadata and gene symbols, ran technical
and biological validation, learned durable curation rules, revalidated
improvements, and promoted only passing versions.

The result is not a one-off merged dataset. It is a clone-ready pipeline that
preserves raw annotations, applies versioned harmonization and curation rules,
quarantines contradictory data, and produces validated corpus and
classifier-ready artifacts from reproducible evidence.

```{image} _static/agentic-corpus-factory-overview.png
:alt: Agentic iterative corpus factory overview
```

## Current Public Corpus

The promoted public run (`iter_014`, 2026-05-20) produced 55 supported public
datasets, 19 audited skipped rows, 6,191,582 harmonized cells, 418,420
classifier-eligible cells, 11 classifier labels, 100% technical/obs/var
validation pass rates, and zero open high-severity failures.

```{toctree}
:maxdepth: 2
:caption: User Guide

getting_started
cli_reference
validation_and_curation
outputs_and_reports
troubleshooting
```

```{toctree}
:maxdepth: 2
:caption: Corpus Factory Method

corpus_factory
custom_corpus_playbook
agentic_prompts
prompts/codex
prompts/claude_code
prompts/agent_roles
```
