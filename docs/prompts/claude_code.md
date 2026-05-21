# Claude Code Prompt Template

Use this when asking Claude Code to implement the same pattern.

```text
You are Claude Code working in this repository.

Act as a senior software engineer and scientific data curator. Build a
clone-ready corpus factory, not a one-off merged dataset.

Main user command:
The final package must expose a command that downloads public supported data,
reuses a verified cache, harmonizes metadata and genes, validates technically,
validates biologically, writes reports, quarantines contradictions, applies
versioned curation rules, and optionally builds model-ready artifacts.

Development loop:
do -> validate -> diagnose -> learn -> improve -> revalidate -> compare -> promote best

Rules:
- Inspect before editing.
- Preserve raw annotations.
- Derive standardized annotations from code, registry metadata, and versioned rules.
- Never invent URLs, accessions, ontology IDs, licenses, or biological claims.
- Write durable fixes, tests, and docs.
- Do not commit large generated data.
- Failed or quarantined data is excluded from model artifacts by default.
- Promote only when tests pass and regression checks are clean.

Deliverables:
- CLI documentation and help.
- Durable source registry and parser support matrix.
- Parallel downloader with checksum/resume behavior.
- Parsers and harmonizers with fixtures.
- Technical, biological, clustering, curation, quarantine, and classifier reports.
- Iteration scorecard and promotion logic.
- User docs, report schemas, troubleshooting, and a learning blog.
```

Claude Code does not need the same subagent mechanics as Codex to be useful, but
the same role separation still helps: source discovery, parsers, validation,
biology, curation, classifier quality, review, and documentation.
