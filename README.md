# Impeccable Levels

**Give an AI agent better level-design judgment before committing to production art.**

Impeccable Levels is an engine-agnostic guidance skill for planning, building, reviewing and improving playable 3D grayboxes. It is for an agent that already knows how to work in your game engine—not a replacement construction framework.

Its particular focus is enjoyable local play, exploration, camera-aware composition, and **making compact spaces feel like part of a much grander world**. An optional Godot CSG module covers efficient editable prototyping. Other engines can add their own guidance modules.

## Start here

Read [the skill](skills/impeccable-levels/SKILL.md). Install the **entire** `skills/impeccable-levels` folder using your agent host's supported skill-installation method; the referenced resources are part of the skill. Do not copy only `SKILL.md`.

You can also use it without automatic skill discovery: place this project where your agent can read it, then ask:

> Read `skills/impeccable-levels/SKILL.md` and follow its relevant references. Inspect our existing controller and camera. Design and build a compact graybox that makes the surrounding world feel immense. Use the Godot CSG module if applicable. Preserve existing authored work, test from ordinary player views, and keep production assets out until the layout is reviewed.

If your host recognizes the skill, invoke `impeccable-levels` through that host's normal skill mechanism. The skill does not register slash commands, run an editor plugin, or supply an autonomous playtester.

## What it changes

- Start with player actions and intended experience, rather than a list of objects.
- Sketch routes, spatial dimensions and changing views separately, then cross-check them.
- Separate **playable geometry**, **boundaries**, and **scenic proxies**.
- Build perceived scale through familiar anchors, depth, silhouette, occlusion, negative space and discovery—not automatically through longer walking distances.
- Diagnose misleading action cues from player attempts; distinguish chosen exploration from disorientation.
- Tell environmental stories through related spatial evidence, including ordinary use and peaceful change—not just ruined props.
- Test whether a later view changes understanding of a familiar place; keep comprehension and reported awe separate.
- Treat player-camera comfort, progression state, and geometry as constraints to test.
- Keep grayboxes cheap to revise; preserve approved spatial relationships when swapping assets.
- Report evidence and uncertainty honestly. A plan, screenshot or navmesh cannot certify fun, awe or physical traversal.

## Contents

| Resource | Purpose |
|---|---|
| [Core skill](skills/impeccable-levels/SKILL.md) | Task routing and decision workflow |
| [Design principles](skills/impeccable-levels/references/design-principles.md) | Player experience, choice, encounters and first repairs |
| [Awe and perceived scale](skills/impeccable-levels/references/awe-and-perceived-scale.md) | Grand worlds within compact playable footprints |
| [Player guidance](skills/impeccable-levels/references/player-guidance.md) | Mistaken-action diagnostics, free-camera reveals and accessibility-aware comparisons |
| [Environmental storytelling](skills/impeccable-levels/references/environmental-storytelling.md) | Cause, use and history through graybox relationships |
| [Spatial patterns](skills/impeccable-levels/references/spatial-patterns.md) | Conditional recipes with verification and tradeoffs |
| [Graybox handoff](skills/impeccable-levels/references/graybox-and-handoff.md) | Iteration and safe transition to production assets |
| [Godot CSG module](skills/impeccable-levels/modules/godot-csg/guide.md) | Local assemblies, booleans, collision, baking and performance |
| [Evaluation](skills/impeccable-levels/references/evaluation.md) | Technical gates, human playtests and fair comparisons |
| [Benchmark briefs](skills/impeccable-levels/assets/benchmarks/briefs.md) | Four fantasy scenarios and a contrasting transfer case |
| [Worked example](skills/impeccable-levels/assets/examples/compact-sanctuary.md) | A plan-only compact sanctuary with explicit geometry and view hypotheses |
| [Revision experiments](skills/impeccable-levels/assets/examples/graybox-experiments.md) | Original aqueduct and conservatory before/change/test exercises |

## Add an engine module

Follow the [module contract](skills/impeccable-levels/references/engine-modules.md). Add a local guide, optional recipes and a small metadata descriptor under the skill's `modules/` directory. Register the module in the routing documentation. Keep design principles in the core and engine-specific construction advice in the module.

The bundled Godot guidance uses official **4.5 documentation as a pinned baseline**, with explicit target-version checks. It is documentation-reviewed, not runtime-tested compatibility certification.

## Validation

Python 3.9+ is needed only for package checks, not for reading or using the design guidance:

```sh
python3 skills/impeccable-levels/scripts/check_package.py
python3 -B -m unittest discover -s skills/impeccable-levels/scripts -p 'test_check_package.py' -v
```

These tests check package links and module metadata. They do **not** measure level quality. See [validation scope](docs/validation.md) for the release's evidence and limitations.

## Research and status

Version **0.2.0** deepens guidance with targeted reads of David Shaver's published slides/speaker notes and Smith/Worch's environmental-storytelling materials, plus a conceptual awe framework and an empirical VR study. The [design source ledger](skills/impeccable-levels/references/sources-design.md) and [Godot evidence ledger](skills/impeccable-levels/references/sources-godot.md) distinguish inspected source material from our original heuristics. Linked sources are not bundled. Inspection depth is explicit: selected full-text sections, abstracts and session overviews are not interchangeable. VR results do not validate a particular desktop-graybox reveal formula.

No claim of consistent improvement over a baseline agent is made yet. That requires repeated controlled trials and human playtesting of actual levels. Contributions should improve concrete agent decisions and show their evidence; see [contributing](CONTRIBUTING.md).

Inspired by the idea behind [Impeccable](https://github.com/pbakaus/impeccable), but independent and unaffiliated. No upstream skill text or code was copied.

## License

Original material is available under the [MIT license](LICENSE). Third-party linked references retain their own terms.
