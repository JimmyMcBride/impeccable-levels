# A small, repeatable design loop

This is an original Impeccable Levels workflow. Treat it as a practical hypothesis about better agent behavior; use the [source ledger](sources-design.md) for the underlying craft references.

## Brief before objects

Turn “make an impressive village” into a player task, an intended feeling, and a bounded experiment. For example: reach the host, discover the garden, and perceive the village as one inhabited part of a larger valley. The number of buildings is a construction constraint, not the experience.

Separate hard requirements, flexible choices, assumptions and protected work. If a request is review-only, inspect and report; do not edit the scene. If an improvement is authorized, keep the patch scoped to the agreed target.

## Sketch before committing

For a new level, make two cheap alternatives only when their tradeoffs differ: a central square with peripheral paths versus a terraced street with an elevated square, for example. Compare daily route convenience, orientation, camera access, useful sightlines and build effort. Do not make alternatives that differ only cosmetically.

Keep three records distinct:

- **Route graph:** spaces and directed connections; annotate doors, one-way drops, return paths and activation states.
- **Spatial plan:** footprint, elevations, actual widths, vertical connections and reference-scale objects.
- **View sequence:** what is visible at approach, decision, reveal and return positions.

A graph can hide an impossible staircase. A top-down plan can hide camera obstruction. A hero image can hide bad connectivity. Cross-check all three before expensive construction.

For dimensioned plans, perform a **spatial-accounting pass** before calling them buildable. Declare whether every extent is clear floor, mesh bounds, or the full assembly including walls and guards. Reserve those margins explicitly inside a hard footprint. For each ramp/stair connection, list the actual endpoint position, floor elevation, landing extent and opening; resolve overlaps where a flat upper floor would cover a still-rising surface. Ensure a promised turning area is represented by geometry, not just prose. Join gate barriers continuously so a small step from an adjacent route cannot bypass progression. These are plan-consistency checks; controller and camera tests remain necessary.

## Build a question, not a finished level

State the most consequential uncertainty and build the smallest test that can resolve it. If the uncertainty is whether a crossing feels exposed but navigable, build that crossing with its approach, depth context and camera. Do not first construct every room beyond it.

Keep production and scenic complexity low. A labeled box can stand for an interaction. A coarse tower silhouette can establish a destination. A giant decorative boolean assembly cannot prove a good route.

Use the actual controller early. Derive width from the player/vehicle envelope plus the intended interaction and camera needs, then test. Collision clearance and comfortable play are different requirements. If the game has no jump, connect every required height change by a supported means rather than introducing a jump implicitly.

## Review behavior and views separately

First verify what the player can do. Then inspect what the player can understand and feel. Record where observations were made and in which state. Check both approach and return; a turn may frame an entrance well while hiding the exit.

Ask for a short neutral playtest when possible. Avoid explaining the intended surprise before observation. Route deviations can be exploration, confusion or experimentation; ask afterward instead of assuming failure or success.

For each suspected problem, name competing explanations. A missed doorway might be hidden by geometry, indistinguishable from scenery, blocked by the camera, or irrelevant to the player's current goal. Make the smallest experiment that distinguishes these causes.

## Change one related cause at a time

Prefer moving a landmark, opening a view, shortening a redundant approach or making a return recognizable over adding entire regions. Keep the original reference views. Preserve fixed entrances, routes and authored features unless the user authorizes changing them.

After editing, re-test affected connections and camera paths, not only the location in the screenshot. Compare using the same FOV, lighting and player position. Do not manufacture improvement by selecting a different flattering view.

## Decide when to stop

Stop when the planned question has enough evidence for the next human decision, the agreed iteration budget is used, or a missing capability blocks meaningful evaluation. A provisional plan with clear uncertainties is preferable to claiming that unperformed tests passed.

Use [evaluation](evaluation.md) to report findings and [graybox handoff](graybox-and-handoff.md) before production assets. Keep the core skill useful with plain language and existing tools; do not require a new planning service or schema to use it.
