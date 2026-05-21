# Essential Agentic Prompts

This section provides reusable prompt patterns for building a corpus factory
with Codex, Claude Code, or another coding agent. Use these as starting points
and replace the domain-specific pieces.

## Minimal Corpus Factory Prompt

```text
You are working in a scientific corpus repository.

Goal:
Build a clone-ready corpus pipeline where a user can install the package and run
one command to download public supported data, harmonize it, validate it,
quarantine failures, and write model-ready artifacts.

Loop:
do -> validate -> diagnose -> learn -> improve -> revalidate -> compare -> promote best

Rules:
- Preserve raw source annotations.
- Do not invent source links, ontology IDs, accession mappings, or biological claims.
- Do not commit large downloaded data.
- Encode learned fixes in durable code/config/rules, not generated outputs.
- Failed or quarantined data is excluded from model artifacts by default.
- Add tests and docs for every behavior change.
- Promote only when tests pass and no new high-severity regressions appear.
```

## Source Discovery Prompt

```text
Find exact public source links for every public registry row.
Check official repositories first: GEO/NCBI, BioStudies/ArrayExpress,
CELLxGENE, Zenodo, Figshare, institutional portals, and publication supplements.

For each row, classify it as supported counts/H5AD, controlled access,
permission required, raw reads only, non-target modality, wrong accession,
unsupported layout, duplicate/superseries parent, or public but parser missing.

Do not invent links. Write durable source-link records with evidence, checked
timestamp, parser name, source kind, skip reason, and direct download URLs.
```

## Biological Validation Prompt

```text
Implement biological validation as an evidence stack, not marker scores alone.
Combine signed marker modules, anti-lineage rules, stress/confounder checks,
reference projection, label confusion, timecourse consistency, clustering,
sample/donor/batch metadata, and classifier agreement as supporting evidence.

Generate curation proposals only when evidence agrees across independent
signals. Preserve raw annotations. Quarantine high-confidence contradictions.
Do not silently relabel ambiguous biology.
```

## Documentation Agent Prompt

```text
Keep a running blog and docs notes while implementation proceeds.
Record what was learned, what changed, which reports were added, what failures
were resolved, what remains open, and how a fresh user should run the corpus.
Every new command, report, parser, validation rule, curation rule, and output
schema must be documented.
```

See the Codex and Claude Code pages for complete operational prompts.
