# The Agentic Corpus Factory

The core loop is:

```text
do -> validate -> diagnose -> learn -> improve -> revalidate -> compare -> promote best
```

This loop turns a corpus from a static spreadsheet into a reproducible system.
Every lesson must become durable code, registry data, curation rules, tests, or
documentation. Generated outputs are evidence, not the source of truth.

## What The Agents Did

The development loop used specialized responsibilities:

- Source agents resolved exact public links and audited skips.
- Parser agents implemented supported public layouts.
- Validation agents converted repeated failures into hard tests.
- Biology agents added marker, reference, clustering, timecourse, and quarantine evidence.
- Curation agents learned durable annotation rules while preserving raw labels.
- Classifier agents enforced eligibility and split-leakage gates.
- Reviewer agents compared scorecards and rejected regressions.
- Documentation/blog agents recorded what changed and why.

## Promotion Rules

An iteration is promoted only when tests pass, no new high-severity regressions
appear, technical and biological pass rates improve or remain stable, unknown
annotation rates are justified, reports are complete, and classifier artifacts
exclude weak, failed, or quarantined data by default.

## Cache Principle

The loop should not redownload data every iteration. Downloads are cached under
`<out-dir>/downloads`, verified with file size and SHA-256 sidecars, and reused
with `--resume`. Iterations re-run harmonization and validation against cached
assets unless `--force` is explicit.

## Why This Matters

Large biological corpora change as links are audited, parsers improve, metadata
edge cases are discovered, and biological contradictions are resolved. The
factory approach records those improvements as reproducible rules instead of
private manual knowledge.
