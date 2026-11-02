# Graybox benchmark briefs

Contents: [Shared conditions](#shared-conditions), [Village](#a--festival-village), [Forest](#b--forest-dungeon), [Castle](#c--castle-and-drawbridge), [Gothic dungeon](#d--vertical-gothic-dungeon), [Transfer case](#e--orbital-maintenance-deck-transfer-case), [Scoring discipline](#scoring-discipline).

These are original Impeccable Levels evaluation fixtures. All sizes, counts and budgets below are deliberately chosen **test inputs**, not universal rules of good design. Do not put the acceptance notes into a generation prompt unless the same notes are given to both conditions.

## Shared conditions

- Evaluate a spatial plan when no engine is available; otherwise use the same runnable starting project for both conditions. Do not silently compare a plan with a playable level.
- Use the existing project controller and camera. For a new benchmark project, agree a reference controller first, including body size, speed, step/slope/jump behavior and camera limits. Keep it fixed for the paired runs.
- Use neutral graybox materials, a familiar player-size marker, simple lighting and readable silhouettes. No production art, cinematic camera override, music, fog-dependent concealment or presentation-only decorations in the primary comparison.
- Supply the same construction tools to both conditions. Set the same total generation budget and allow one review/revision pass. Record actual time, token/tool cost and unavailable capabilities.
- Separate the traversable footprint from scenic proxies. Backdrops may imply a wider world but may not create hidden gameplay areas or evade the playable-area limit.
- Preserve the brief's external entrances/exits and approved constraints during revision. Capture ordinary player views on approach, at decisions and on return.
- Ask for a compact annotated layout, route/connection explanation, dimensions derived from the controller, intended experiences, construction priorities, and a test plan. Require a runnable graybox only when the test environment supports it.
- Run the first pass without waypoint arrows. If guidance is necessary for the intended audience, compare an accessible guidance configuration too; do not equate withholding help with good design.

## A — Festival village

### Generation brief

Design a welcoming fantasy village for a third-person exploration game. The player arrives for a festival, visits a noticeboard, finds the host and can investigate an optional garden. The village should feel like a lived-in corner of a much larger region. Make one view inspire wonder without making the village inconvenient to traverse.

### Constraints and budget

- Keep the playable area within an 80 m by 70 m rectangle.
- Provide one public entrance/exit, one festival square, six building masses, the noticeboard, the host location and one optional garden.
- Only the host building needs a playable interior. Keep all other buildings as readable graybox masses.
- Include a recognizable landmark and a distant-world layer; neither requires a large traversable extension.
- Keep vendor/activity placement accessible from the square. No combat, jumping challenge or mandatory maze.

### Acceptance observations

- Can a first-time player infer where the festival is and recover orientation after visiting the garden?
- Are everyday routes short and purposeful while the surroundings imply life beyond the footprint?
- Does the wonder moment retain a human scale anchor and a clear next action?
- Does the village avoid both a featureless parking-lot square and arbitrary winding streets?
- Can the intended composition be explained using geometry and camera views, without relying on final art?

## B — Forest dungeon

### Generation brief

Design a compact forest ruin where curiosity gradually becomes unease. The player investigates an ancient shrine, passes through two encounter spaces and reaches a guardian arena. Include optional discoveries and a shortcut that makes the return journey feel newly understood. Suggest an ancient forest larger than the playable route.

### Constraints and budget

- Keep traversable geometry within 110 m by 90 m, excluding clearly non-playable backdrop masses.
- Provide one start, the shrine, two ordinary encounter spaces, one guardian arena and two optional discovery areas.
- Include one unlockable returning shortcut; place its activation on the accessible side of the intended progression.
- Use an existing controller's normal movement. Do not add new climbing, flying or swimming mechanics.
- Prototype encounter boundaries and sightlines; do not invent tested enemy behavior if the starting project has none.

### Acceptance observations

- Is progression possible without accessing the locked shortcut first?
- Do the optional discoveries offer different information, views or tactical opportunities rather than duplicate dead ends?
- Does the shortcut materially change the return route, and can the player recognize where it reconnects?
- Does the shrine help orientation without every part of the dungeon being visible at once?
- Do pauses and changes of enclosure support the requested emotional progression without adding empty distance?

## C — Castle and drawbridge

### Generation brief

Design an imposing medieval-inspired castle approach and outer court. The player and a supply cart enter across a moat using a drawbridge and pass a guarded gate. Make a compact fortress feel monumental and functionally credible. The result is a gameplay prototype, not a structurally certified building.

### Constraints and budget

- Keep the playable approach and castle court within 120 m by 100 m.
- Supply a cart envelope and turning requirements as explicit benchmark inputs before generation; use the same values in both conditions.
- Include a moat, drawbridge span, gate passage, outer court, keep entrance and one accessible defensive overlook.
- Test or describe both bridge-open and bridge-closed states. Reserve the bridge's swept volume and avoid blocking the gate mechanism with scenery.
- Keep distant towers and outer fortifications non-playable unless needed by the required route.
- Include one human-scale reference near the gate and a service route from the gate to the court.

### Acceptance observations

- Does the lowered bridge actually span the moat, with usable approach/departure and stated cart clearance?
- Can the cart turn and proceed through the gate under the declared envelope? A path centerline alone is insufficient evidence.
- Does the raised bridge have a plausible reserved motion envelope, with its collision state handled explicitly?
- Do walls, entrances, overlooks and service circulation communicate a defensible, used place?
- Does grandeur come from hierarchy, approach and contrast rather than uniformly oversized doors and empty courts?

## D — Vertical gothic dungeon

### Generation brief

Design an ancient sanctuary built around a deep chasm. The player crosses an occupied sliver of an immense ruin: an arrival passage, a reveal, a hazardous crossing, a resting place and a final chamber. Make the world feel older and larger than what can be reached. Preserve reliable navigation and player-camera comfort.

### Constraints and budget

- Keep the playable horizontal footprint within 75 m by 75 m and its total elevation range within 18 m.
- Include three connected playable elevations, one optional overlook and a return connection that exposes a previously seen space from another angle.
- Keep stairs/ramps within the actual controller's limits; no unexplained elevators or new traversal abilities.
- Use the chasm and distant structures as scenic depth, not as an excuse for an unbounded playable map.
- Include a safe place to stop and observe the major reveal. Do not require stopping in an active damage zone.
- No required hidden ledge drops; clearly distinguish scenic ledges from intended walkable routes.

### Acceptance observations

- Is the vertical route understandable from player height, including its return connections?
- Do changing viewpoints create new understanding rather than repetitive views of the same backdrop?
- Can players infer depth and monumental scale using ordinary reference sizes and overlapping geometry?
- Does the path still work when players turn the camera away from the intended hero framing?
- Does a complete traversal support the reveal sequence without forcing a camera cut or excessive walking?

## E — Orbital maintenance deck (transfer case)

### Generation brief

Design a first-person, non-combat maintenance level inside a vast orbital structure. The player restores power at two substations and returns to an observation control room. Make the industrial world feel enormous, but keep the player's task compact and legible. Wonder should come from discovering how the place fits together, not fantasy architecture or a mandatory dramatic reveal pattern.

### Constraints and budget

- Keep the traversable deck within 45 m by 35 m; use at most two playable elevations.
- Provide two order-independent substation routes, one control room and a short return route after both tasks.
- No jumps, weapon mechanics, enemies or locked key hunt. Mark task states with redundant shape/text/position cues rather than color alone.
- Include a view of a non-playable large structure that helps explain the facility's purpose.
- Keep utilitarian proportions near the player; scenery must not suggest a required route into inaccessible machinery.

### Acceptance observations

- Do both task orders work, and does completion make the return route clear?
- Does the agent adapt to first-person readability and the absence of combat instead of importing fantasy-dungeon formulas?
- Does the background help the player understand the installation without obscuring local tasks?
- Can the small footprint convey a larger system without excessive travel or a changed FOV used to manufacture scale?

Reserve E from worked examples and skill-tuning trials when testing transfer. Because this fixture is published, it is not permanently secret: create unpublished variations before a formal held-out study, and keep those variations out of authoring context.

## Scoring discipline

Use [the evaluation procedure](../../references/evaluation.md). Separate hard failures, evidence coverage and human judgments. Record untested claims; do not convert them into passes.

Do not rate a design higher merely for adding space, encounters, branches or visual clutter. Compare fulfillment of each brief, tradeoffs, rework cost and player observations. Report all paired attempts, including failed runs. Small plan-only smoke tests can validate instruction usefulness, not prove that the resulting game is fun or awe-inspiring.
