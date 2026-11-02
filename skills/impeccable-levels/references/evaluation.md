# Evaluate the graybox, not the pitch

This is Impeccable Levels' proposed evaluation method, not a validated measure of fun. Use the project's intended experience as the standard. A quiet village, deliberate maze, and readable combat arena need different judgments.

## Separate evidence levels

| Evidence | What it can support | What it cannot establish |
|---|---|---|
| Plan or scene-data inspection | Intended routes, dimensions, authored relationships, hypotheses | Physical traversal, visibility in the running game, emotional response |
| Captured player-camera view | Composition and visibility at the recorded pose and settings | Behavior along the whole route, collision correctness, general player understanding |
| Actual controller traversal | Observed movement and camera behavior on tested routes and states | Every possible route, combat balance, whether discovery is enjoyable |
| Observed human playtest | That participant's choices, confusion, reactions and reported experience | Universal fun, statistical superiority from one session |

Never promote an intention into an observation. Report `not tested` when evidence is absent. A navigation path is not proof that the player controller, camera, or cart can traverse it. A screenshot cannot prove that a reveal works in motion.

## Establish the review conditions

1. Record the brief, scene revision, engine version, player/controller settings, camera/FOV/aspect ratio, and available evidence.
2. List hard requirements, protected authored elements, and intentional exceptions before identifying defects.
3. Name the current design question: for example, "Does this compact approach make the keep feel monumental without adding empty walking?"
4. Review ordinary player views and the return journey, not only an editor flythrough or selected hero shot.
5. Keep a readable neutral-lighting comparison when useful. Add lighting or sound cues when the experiment depends on them. Keep necessary accessibility support active; do not confuse a layout-only diagnostic with an acceptable configuration for every player.

## Technical eligibility

Use `pass`, `fail`, `not tested`, or `not applicable`, each with evidence and scope. Do not award points that compensate for a blocking failure.

- Required destinations are reachable in the intended progression states, with no inaccessible key, self-locking shortcut, or unintended irreversible trap.
- Actual clearances and transitions support the project's controller, camera, enemies and required vehicles; test seams, slopes, steps, doors and landing zones.
- Boundaries communicate where play stops. Scenic proxies do not accidentally invite a traversal mechanic they cannot support.
- Gameplay-critical elements remain readable under the intended camera range and relevant accessibility settings. Do not depend solely on color to distinguish routes or hazards.
- Protected elements, external connections, budget constraints and required mechanics remain intact after revision.
- The graybox remains editable and can be replaced by assets without losing routes, dimensions, sightlines, interaction positions or collision intent.

When an engine is unavailable, limit this gate to plan/data checks and list the engine checks still needed. Do not label the level "playable" on that basis.

## Design questions and observable checks

| Question | Inspect or observe | Avoid mistaking this for success |
|---|---|---|
| Does the player have a reason to act? | A legible destination, curiosity cue, interesting choice, or satisfying movement opportunity | A long list of activities with no meaningful difference |
| Do route choices matter? | What the player can anticipate, trade off and learn; whether branches provide distinct experiences | More junctions or loops automatically being better |
| Does the place invite exploration? | Where attention goes, what is partially revealed, what a detour changes or rewards | Arbitrary dead ends and collectible counts |
| Does the intended grandeur survive movement? | Familiar scale anchors, depth layers, landmark silhouette and changing visibility along the approach | Large dimensions, empty walking or one flattering screenshot |
| Is pacing intentional? | Contrast between exposure/shelter, action/reflection and anticipation/payoff | A mandatory encounter every fixed number of seconds |
| Can the player understand the space? | Recognition of landmarks, useful recovery after a wrong turn, comprehension of vertical connections | Preventing every moment of uncertainty |
| Does the environment support the mechanics? | Movement options, sightlines, camera room and encounter boundaries | Decorative complexity or an unused balcony |

Record each as `supported`, `concern`, or `unresolved`; include the evidence and an alternative explanation. These are review labels, not a summed quality score.

## Run a small human playtest

- Give the objective without explaining the intended route, surprise, or emotional effect. Observe first; avoid coaching.
- Record route taken, attempted interactions, voluntary pauses, backtracks, camera adjustments and places requiring help. A pause can mean wonder, confusion or distraction: ask afterward rather than interpreting it automatically.
- Ask neutral questions: "What stood out?", "Where did you want to go?", "Was anything unclear?", "How large did this place feel?", and "Which moment would you change?"
- Begin with unprompted recall before asking about a particular relationship or history. Record whether understanding emerged spontaneously or only after a targeted question; prompting is not evidence of spontaneous discovery.
- For awe, distinguish feeling scale, surprise, beauty, threat and curiosity. Do not lead with "Did that awesome vista amaze you?"
- Ask what changed in the player's understanding separately from what they felt. A correctly identified spatial relationship is not proof of an emotional response.
- Revisit the main design question. Preserve evidence that contradicts the author's intention. Record familiarity, relevant access needs and sample limitations without collecting unnecessary personal information.

## Report and revise

Before a comparison, write a small experiment card: `question → competing explanations → changed variable → fixed conditions → observations → revision decision`. Decide what evidence would contradict the proposal. Use [player guidance](player-guidance.md) for mistaken actions and [environmental storytelling](environmental-storytelling.md) for interpreted clues.

Keep route, controller/camera, relevant assistance, scene states and exposure conditions comparable. Prefer fresh participants for discoveries; if people see both versions, counterbalance order where practical and disclose learning effects. A stronger explanation after a second visit may reflect familiarity, not a better layout. Report observations and denominators rather than inventing a universal success threshold.

Use one finding per issue:

`Location/state → evidence → player consequence → smallest proposed change → protected constraints → re-test → uncertainty`

Classify severity as `blocker` (breaks a requirement), `important` (undermines the intended experience), or `experiment` (plausible improvement needing comparison). Separate measured defects from taste disagreements.

For example: "At approach_turn, the recorded gameplay view shows the complete tower before the intended reveal. This may flatten anticipation. Test shifting the existing wall inward; keep the walking clearance and external doorway fixed. Repeat approach/return captures and controller traversal. Emotional impact remains untested."

Change one related cluster of causes at a time. Compare before/after from the same poses and settings, then traverse the affected route and connected seams. Revert a regression; do not hide it by changing the review conditions. Stop at the agreed iteration budget and report unresolved questions.

Call a result `plan reviewed`, `graybox checks completed for listed routes`, or `ready for human art-pass decision`, as warranted. Only a human can accept the intended feel and the remaining risks; do not self-certify "fun" or "awe achieved."

## Compare skill versus baseline fairly

1. Freeze briefs, model/version, tools, project/controller, assets, compute/time budget, allowed revisions and evaluation questions before generation. Count skill-reading overhead in the skill condition's total cost.
2. Run baseline and skill conditions in independent fresh contexts with the same brief. Do not leak the skill, expected solution, reviewer diagnosis or the other output to baseline. Pair procedural seeds when controllable; otherwise record that model sampling is uncontrolled.
3. Repeat each condition with multiple independent runs and new brief variants. Retain failures, timeouts and weak outputs; do not select only the best example. Treat familiar development briefs separately from previously unused transfer cases.
4. Give reviewers anonymous artifacts in randomized/counterbalanced order. Hide condition labels and author pitches; standardize camera, lighting, task and explanation length. Use independent players or counterbalance order to limit learning effects.
5. Report hard-constraint failures, technical evidence coverage, player observations, preferences with reasons, disagreements, generation/revision time, and cost separately. Do not collapse them into one "fun score."
6. For early smoke tests, claim only what happened: whether the skill was followed, what concrete decisions changed, and what defects were detected. Text-only agent trials do not demonstrate superior playable levels. Reserve claims of consistent improvement for broader, repeated, blinded human testing.

Use the [benchmark briefs](../assets/benchmarks/briefs.md) as authored test inputs, then write new variants that were not used while revising the skill.
