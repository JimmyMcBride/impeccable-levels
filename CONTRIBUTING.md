# Contributing

Improve a concrete design decision, not merely the length of the guide.

## Design guidance

Provide the problem, the condition under which your advice applies, the proposed spatial action, an observable check, and a tradeoff or failure case. Cite primary sources where relevant. Mark original heuristics and untested hypotheses honestly. Do not introduce universal numerical thresholds for subjective quality.

Keep the core concise. Put specialized references in the skill's `references/` directory and link them from `SKILL.md` with a clear loading condition. Avoid mandatory frameworks, new controllers or tool dependencies for design-only use.

## Engine modules

Use the [module contract](skills/impeccable-levels/references/engine-modules.md). Document the exact engine versions inspected and whether anything was executed. Preserve editable sources and authored work. Explain collision, transforms, performance tradeoffs and verification separately. Do not report a navigation path as evidence of real controller traversal.

## Evidence

Run the package checker and regression tests. For behavior changes, supply a small input/output example and an unsuccessful case when available. Keep tested prompts separate from held-out evaluation variants. Retain failures and report costs. A single good design proposal is not proof of better playable levels, fun or awe.

Do not contribute copied talk transcripts, proprietary assets, private project context, credentials or source material you do not have rights to redistribute. Use original explanations and links.

Keep changes scoped, explain the rationale, and follow the [evaluation method](skills/impeccable-levels/references/evaluation.md).
