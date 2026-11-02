# v0.1.0 validation scope

Checked 2026-11-01.

## Completed

- Skill-format validation using the authoring workflow's validator.
- 52 package-integrity checks, with no reported errors.
- 14 package-checker regression tests, all passing. They cover missing files, broken relative links, path escapes, symlinks, malformed module data and compatibility flags.
- Documentation review of the Godot CSG guidance against pinned 4.5 class references. The review strengthened checks for empty baked resources and explicitly separated moving-body collision from static CSG collision.
- Independent review of two plan-only graybox proposals. Both had useful decisions and unresolved construction details; one exposed conflicting width conventions, a ramp/landing overlap, and turning-space promises not represented in geometry. This led to an explicit spatial-accounting pass in the skill. It did not establish superiority of the skill condition.
- A fresh-context review using the skill detected a circular key/door dependency, stairs above the supplied step limit, a ramp above the supplied slope limit, hidden static CSG collision, misleading scenic route cues, and invalid screenshot-only evidence of grandeur. It preserved the distinction between nominal body fit and untested camera comfort. This is a bounded smoke test, not a human gameplay study.

## Not established

- No Godot scene or CSG recipe was executed as part of this release's package validation.
- No controller traversal, navigation bake, screenshot capture, performance benchmark or combat simulation is claimed.
- No human study of fun, awe, perceived scale or wayfinding was performed.
- No statistically supported improvement over a baseline agent is claimed.

The [evaluation procedure](../skills/impeccable-levels/references/evaluation.md) describes the next evidence to collect. Use the same project, controller, camera, tool access and total budget for baseline and skill conditions. Review ordinary player views and actual traversal, retain failures, and use neutral human observations. Package tests cannot substitute for those experiments.
