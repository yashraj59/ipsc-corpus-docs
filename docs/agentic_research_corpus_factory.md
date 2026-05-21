# Agentic Research Corpus Factory

The **Agentic Research Corpus Factory** is a human-supervised workflow for
building scientific corpora through repeatable agent loops instead of one-off
manual curation.

The method is:

```text
discover -> audit -> download/cache -> harmonize -> validate
-> diagnose -> learn -> improve durable rules -> revalidate
-> compare scorecards -> promote best
```

Agents do the repetitive work: source discovery, link auditing, parser fixes,
metadata harmonization, validation, report generation, and regression checks.
Human supervision stays in the places where scientific judgment matters:
license interpretation, biological plausibility, curation approval, and final
promotion.

## Human Supervision

The iPSC Corpus Kit was built with an interactive human-supervised loop. The
human supervisor repeatedly asked the agent system what it had learned, what it
had improved, and how those improvements changed validation evidence. When a
claim looked wrong, the supervisor redirected the system toward source evidence,
tests, or stricter validation instead of accepting generated output at face
value.

This matters because the goal is not autonomous annotation. The goal is an
auditable process where agents propose and implement durable improvements while
humans guide ambiguous scientific decisions.

## Agent Roles

The workflow uses specialized responsibilities:

| Role | Responsibility |
|---|---|
| Coordinator | Integrates work, runs tests, compares scorecards, and owns promotion. |
| Source auditor | Resolves exact public links, accessions, and skip evidence. |
| License auditor | Checks usage constraints, attribution, and commercial eligibility. |
| Parser/harmonizer | Adds supported source parsers while preserving raw metadata. |
| Technical validator | Blocks invalid files, malformed AnnData, bad counts, and schema failures. |
| Domain validator | Checks biological or domain-specific consistency with evidence stacks. |
| Curation learner | Turns repeated high-confidence lessons into durable rules. |
| Classifier reviewer | Ensures model artifacts exclude failed or quarantined data by default. |
| Regression reviewer | Rejects changes with new high-severity regressions. |
| Documentation agent | Records what changed, what was learned, and how to rerun it. |
| Human supervisor | Reviews claims, guides corrections, and approves scientific promotion. |

## Promotion Scorecard

The scorecard is the promotion gate. Agents can discover and improve the corpus,
but an iteration is promoted only when the evidence supports it.

Promotion requires:

- tests pass
- required reports are written
- technical validation passes
- biological contradictions are quarantined by default
- classifier artifacts exclude failed and quarantined cells by default
- no new high-severity regressions appear
- documentation reflects changed behavior

## Case Study: iPSC Corpus Kit

The promoted public run, `iter_014` from 2026-05-20, is the reference case
study for the method.

| Metric | Promoted `iter_014` |
|---|---:|
| Supported public datasets processed | 55 |
| Audited skipped rows | 19 |
| Cached source assets reused | 111 |
| Harmonized cells | 6,191,582 |
| Technical validation pass rate | 100% |
| Obs-schema validation pass rate | 100% |
| Var-name validation pass rate | 100% |
| Classifier-eligible cells | 418,420 |
| Classifier labels | 11 |
| Open high-severity failures | 0 |

The promoted run did not hide failures. Skipped rows remained visible in
`skipped_manifest.csv`, biological contradictions remained visible in
`quarantine_manifest.csv`, and learning notes were recorded in `agent_state/`.

## Why This Generalizes

The iPSC implementation is one domain-specific instance. To reuse the method for
another research problem, swap in the domain pieces:

- source registry and source resolvers
- source parsers
- metadata schema and vocabulary
- technical validators
- domain-specific evidence checks
- curation rules
- report schemas
- scorecard and promotion gates

The transferable idea is that a corpus is not finished when data downloads. It
is ready when source evidence, validation, human-reviewed curation, and
promotion decisions are reproducible.

## Related Pages

- {doc}`corpus_factory`
- {doc}`agentic_prompts`
- {doc}`prompts/agent_roles`
- {doc}`outputs_and_reports`
- {doc}`validation_and_curation`
