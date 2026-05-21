# Codex Prompt Template

Use this when asking Codex to build or refine a corpus factory.

```text
You are Codex working in this repository.

Mission:
Deliver a clone-ready, validated public corpus pipeline. A fresh user should be
able to install the package, build the registry, run one command, and receive
downloaded, harmonized, technically validated, biologically validated, curated,
and model-ready artifacts.

Required loop:
1. Inspect the repo and current evidence.
2. Make durable code/config/rule improvements only.
3. Add or update tests.
4. Update docs whenever behavior changes.
5. Re-run relevant validation.
6. Record findings in agent_state/ or an equivalent state directory.
7. Never silently patch generated outputs.

Hard rules:
- Do not commit downloaded large data.
- Do not overwrite raw source annotations.
- Do not invent source links, ontology IDs, accession mappings, or biological claims.
- Do not include failed or quarantined data in model training by default.
- Technical failures block inclusion.
- Biological contradictions quarantine by default.
- Include quarantined data only with an explicit opt-in flag.
- Iterations must reuse verified download cache unless force redownload is explicit.

Implementation:
- Build or update CLI commands for doctor, registry build, download/preprocess,
  iteration, scoring, comparison, promotion, and classifier artifacts.
- Write manifests for downloads, skips, harmonization, validation, var names,
  obs schema, biology, clustering, curation, quarantine, classifier outputs, and
  iteration scorecards.
- Use parallel download where safe and serial or bounded-memory harmonization for
  large expression files.
- Preserve raw annotations and derive standardized columns reproducibly.
- Promote only when tests pass and no new high-severity regressions appear.

Finish:
Run tests, run a smoke pipeline, commit, push if authentication is available,
and report branch, commit, push status, tested commands, smoke outputs, external
download limitations, and remaining known issues.
```

## Codex Operating Notes

For large tasks, ask Codex to use subagents for independent source discovery,
parser work, validation, biology, classifier quality, review, and docs. Keep the
coordinator responsible for integration and tests.

When the prompt evolves, update the repo's main prompt file and docs so future
agents inherit the same requirements.
