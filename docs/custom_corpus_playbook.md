# Build Your Own Corpus Factory

The iPSC workflow generalizes to other biological and scientific corpora. Keep
the loop, replace the domain evidence.

## 1. Define Scope

Write the biological or scientific boundary clearly:

```text
Corpus: public single-cell atlas of disease X.
Include: scRNA count matrices and public H5AD files.
Exclude: controlled access, raw reads only, bulk RNA-seq, unsupported modality.
Default model artifacts: PASS and non-quarantined data only.
```

## 2. Create Durable Registries

Use versioned files for source links, parser support, standardized
vocabularies, marker/reference assets, and curation rules. Every generated CSV
must be reproducible from those durable files.

## 3. Assign Agent Roles

Use separate agents for source discovery, parser implementation, technical
validation, biological validation, curation learning, classifier quality,
review/regression, and documentation. Agents should write durable files and
tests, not only chat summaries.

## 4. Validate Before Learning

Never learn curation rules from broken matrices. First pass technical gates:
file integrity, matrix shape, count-likeness, metadata alignment, schema,
var-name uniqueness, gene mapping, and raw annotation preservation.

## 5. Build A Domain Evidence Stack

For another domain, replace iPSC marker modules with relevant pathways,
phenotypes, reference labels, ontologies, timecourse expectations, or physical
constraints. Keep the same principle: no single evidence source silently
rewrites labels.

## 6. Promote Only Stable Improvements

Compare scorecards. Promote only when tests pass, no high-severity regressions
appear, and the new run improves or preserves technical/biological quality.

## 7. Publish User And Maintainer Paths

Give users one normal command. Keep iterative refinement as a maintainer/agent
workflow. Users should not need to rediscover links or manually patch metadata.
