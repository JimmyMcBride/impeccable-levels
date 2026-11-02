---
name: impeccable-levels
description: Plan, build, critique, and improve intentional 3D level grayboxes before production art. Use for level design, grayboxing/greyboxing, blockouts/whiteboxes, player flow, exploration, encounters, wayfinding, camera-aware composition, awe, or making compact worlds feel grand. Includes optional Godot 4 CSG guidance; keep the design core engine-agnostic. Not a general engine-programming or final environment-art skill.
---

# Impeccable Levels

Version 0.1.0 — research-backed guidance; behavioral smoke tests are not proof of superior playable levels.

Design a playable experience, not a collection of objects. Make the next spatial decision concrete, reversible, and testable.

**Scope:** guidance for an agent that already has construction tools. Do not introduce a level-generation framework, mandatory JSON scene format, new controller, or engine adapter unless the user separately requests one. This package does not install editor commands or provide autonomous playtesting.

## Start with the right mode

Treat these as conversational modes, not executable commands.

| Request | Do | Read next |
|---|---|---|
| Plan a level | Turn the brief into routes, spaces, views, and experiments | [Design principles](references/design-principles.md), [workflow](references/workflow.md) |
| Build a graybox | Use existing project tooling; construct the smallest useful playable test | [Graybox and handoff](references/graybox-and-handoff.md), applicable engine module |
| Review a level | Inspect available artifacts; report findings without changing them | [Evaluation](references/evaluation.md), one relevant design reference |
| Improve a level | Make authorized, targeted changes; preserve protected work | [Workflow](references/workflow.md), [evaluation](references/evaluation.md) |
| Make it feel grand / inspire awe | Design perception and the approach before adding area | [Awe and perceived scale](references/awe-and-perceived-scale.md) |
| Prepare for art replacement | Record the approved spatial relationships and remaining risks | [Graybox and handoff](references/graybox-and-handoff.md) |

Load only the references relevant to the current decision. Use [spatial patterns](references/spatial-patterns.md) when choosing route structure and [archetypes](references/archetypes.md) when the genre or place type changes. Patterns are options, not a checklist to impose on every level.

## 1. Establish the experience and constraints

Inspect the actual brief, current scene, controller, camera, and project conventions before assuming missing facts. Record:

- The player's verbs, immediate purpose, intended audience, and desired experience. Ask what the player should *do*, *notice*, and *feel*; these are different requirements.
- Footprint, traversal/time budget, entrances/exits, required activities, optional content, and inaccessible scenery.
- Body/collision dimensions, movement speed, step/slope/jump rules, relevant enemy/vehicle envelopes, camera type/offset/FOV/collision behavior, and aspect ratio.
- Approved geometry, locked connections, existing art, and any work that must not change.
- Available evidence and tools: plan only, scene inspection, screenshots, running controller, or human playtest.

Ask only questions whose answers materially change the design. If measurements cannot be inspected, label assumptions and use reversible prototypes. Never present invented metrics as project facts. Do not expand the game mechanics to rescue a layout.

Use the [brief template](assets/templates/design-brief.md) when a durable brief is helpful. Do not force the template on a quick critique.

## 2. Make a spatial hypothesis

Write one sentence linking a spatial decision to a player outcome. Example: “A sheltered turn with a familiar doorway will frame the remote observatory, making the arrival feel monumental while keeping the local route compact.” Label the outcome a hypothesis until tested.

For new layouts, compare two inexpensive route/massing sketches when there is a meaningful choice. Choose based on the brief and explain the tradeoff, not an invented total quality score. For existing layouts, prefer a local repair over redesigning the whole place.

Describe:

1. Required progression, branches, one-way links, gates and the states that unlock them.
2. What each important space lets the player decide, practice, discover, anticipate, or recover from.
3. Where destinations are visible, hidden, foreshadowed and recognized on return.
4. The actual player-camera viewpoints that test the composition.
5. Which masses are **playable**, **spatial boundaries**, or **scenic proxies**. Keep scenic scale separate from traversal distance.

Use an annotated plan, spatial table, or simple graph. Include coordinates/elevations and dimensions when needed to build reliably; declare units, axes and origin. A written connection is not proof that geometry connects.

Before construction, reconcile clear widths with wall/guard thickness, footprint limits, ramp endpoints, landing planes and closed-gate barriers. Do not promise turning space that the plan has not reserved. Follow the spatial-accounting pass in the workflow.

For each built connection, match the departure and arrival positions/elevations, reserve an actual opening, and account for the transition's run and landing. Trace required objective orders and gate states; do not let a convenient diagram hide a gap, a key behind its own lock, or a final route reachable too early.

## 3. Graybox in decision order

Construct in this order unless the project's experiment requires another:

1. Controller-scale reference, ground, entrance, exit and main route.
2. Major volumes, elevation transitions and necessary collision.
3. Landmarks, occluders, voids, and distant massing for the intended views.
4. Encounter/activity envelopes, interaction markers and optional routes.
5. Minimal value/lighting cues that the experiment actually requires.

Keep silhouettes and dimensions useful, materials simple and edits cheap. Do not decorate a weak layout or model details that do not answer a current design question. Grayboxing may use coarse terrain, primitives, CSG, temporary meshes, or existing placeholders; it is not a requirement to build everything from cubes or booleans.

For Godot CSG, read [the module guide](modules/godot-csg/guide.md) before engine-specific advice and [recipes](modules/godot-csg/recipes.md) when relevant. Verify the installed Godot minor version. Other engines use their own module or the agent's existing tools; do not apply Godot-specific constraints globally.

## 4. Review from the player, then repair

Walk or request traversal of the actual route and return route with the actual controller/camera. Test decisions, seams, corners, thresholds, height changes and gate states. Capture ordinary player views, not just a flattering editor flythrough. Keep camera/FOV and comparison conditions fixed between revisions unless changing the camera is the explicit experiment.

Use [evaluation](references/evaluation.md). Keep these judgments separate:

- **Technical:** pass / fail / not tested / not applicable, with scope and evidence.
- **Design:** supported / concern / unresolved, with the intended player consequence.
- **Human response:** observed behavior and participant feedback, never inferred automatically from a pause or screenshot.

A navigation path does not prove physics traversal. A screenshot does not prove a moving reveal. Neither proves fun or awe. If the engine is unavailable, perform plan-level review and state exactly what remains untested.

For each important finding, give `location/state → evidence → player consequence → smallest change → protected constraints → re-test`. Recommend a few prioritized changes rather than unbounded polishing. Apply only changes authorized by the request. Preserve unrelated work; keep before/after evidence and a recoverable revision. Stop at the agreed budget and disclose unresolved issues.

## 5. Hand off the spatial contract

Before replacing grayboxes with art, record approved widths, heights, collision boundaries, route connections, gameplay sockets, landmark silhouettes, reveal occluders and camera viewpoints. Distinguish approved elements from unresolved hypotheses. Retest a representative asset replacement before replacing the entire level; asset bounds and decoration can change both movement and views.

Present a concise result: what was designed/changed, why it supports the brief, evidence collected, assumptions, and the next high-value test. Do not label a plan “playtested,” or a scene “fun,” merely because files were generated.

## Non-negotiable design habits

- Design meaningful action and curiosity, not mandatory combat, constant branching, or constant spectacle.
- Make grandeur through contrast, depth, silhouette, anchors and discovery; do not default to oversized empty maps.
- Maintain the player's trust about what is reachable. Do not advertise an inaccessible scenic ledge with the same cues as a required path.
- Use readable geometry and redundant cues; do not rely solely on color, darkness, tiny details, or forced camera movement.
- Allow purposeful uncertainty, but provide recovery appropriate to the audience. A maze and a quest hub have different clarity goals.
- Tie numbers to measured project metrics or explicitly authored experiments. There is no universal corridor width, branch count, pacing interval, “awe ratio,” or CSG-node budget.
- Treat AI failure patterns as review hypotheses, not claims about every model. Make concrete observations about the current artifact.

## Further resources

- [Worked compact sanctuary plan](assets/examples/compact-sanctuary.md): original design hypothesis, not an engine-tested level.
- [Graybox plan template](assets/templates/graybox-plan.md) and [review template](assets/templates/review-report.md).
- [Benchmark briefs](assets/benchmarks/briefs.md): authored tests, not genre prescriptions; use independent contexts and retain failures.
- [Engine-module contract](references/engine-modules.md) and [module metadata](modules/godot-csg/module.json): extend the engine guidance without changing the core.
- [Design source ledger](references/sources-design.md) and [Godot source ledger](references/sources-godot.md): distinguish source evidence from original synthesis.

Run `python3 scripts/check_package.py` from this skill directory to check package integrity. This checks documents and module metadata, **not level quality or engine behavior**.
