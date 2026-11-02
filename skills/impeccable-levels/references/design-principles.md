# Design decisions that change play

Use these **Impeccable Levels heuristics** to turn a brief into experiments. They are an original synthesis, not a universal recipe or a demonstrated guarantee of fun. The [source ledger](sources-design.md) distinguishes inspected literature from our proposed procedures.

## Define the experience before the objects

Replace “make a fun village” with a player-facing hypothesis: “Arriving players recognize the gathering place, choose a tempting detour, and return without losing their bearings.” Name the supported actions, the anticipated decisions, and the experience to investigate. Discovery, mastery, comfort, suspense and spectacle are different goals; do not optimize every level for combat or surprise. This follows the experience-oriented distinction in [S1](sources-design.md#s1--mda).

For every major space, answer: **What can the player do here, what information do they have, and what changes afterward?** Quiet contemplation is a valid purpose. An object count is not a purpose.

## Work from the actual player

Read the controller and camera settings before choosing dimensions. If unavailable, name assumptions and build a calibration room first. Separate measured physics limits from chosen comfort margins; do not turn a maximum jump or slope into the normal route requirement. Compare ordinary passage, combat turn, overhead obstruction and elevation transition using the existing controller. Different actors may need different clearances. [S2](sources-design.md#s2--metrics) supports this distinction; the calibration procedure is ours.

Reserve camera volume as well as body volume. Test turning, backing into corners and approaching diagonally. A passage that fits a capsule may still be unpleasant with a following camera.

## Offer information and worthwhile choices

At a junction, decide what the player can infer about each option: purpose, risk, destination, cost or curiosity. Different routes should support different experiences, not merely duplicate distance. Allow deliberate uncertainty where appropriate, but provide a way to recover orientation. Recognizable landmarks and spatial relationships help; do not assume a painted line controls a player's attention. Players may intentionally investigate the apparent wrong route. See [S3](sources-design.md#s3--wayfinding).

Make secrets understandable in retrospect. A glimpse, anomalous shape or alternate view can invite investigation; an unmarked arbitrary wall tests exhaustive searching instead. Which is appropriate depends on the intended audience and game.

## Design encounters as spatial problems

Start with existing verbs and opponent behaviors. Reserve room for the actual dodge, attack, retreat, line-of-sight and recovery needs. Give important obstacles a role, such as separating approaches or breaking a dangerous sightline. Test whether each placement creates a useful decision or merely obstructs movement. A valid navmesh is insufficient: prototype the encounter if systems exist; otherwise label combat suitability untested.

## Give journeys contrast and consequences

Sketch changes in action, enclosure, exposure, knowledge and safety along the route. Where a sequence is monotonous, change the relevant condition before adding more content. A spacious resting point may serve pacing better than another encounter. Do not require a crescendo, loop, vista or battle in every level.

Give buildings and ruins plausible functions at the game's abstraction level. Use access, circulation, blocked passages and structural relationships to suggest use or history. Let players infer a cause from evidence instead of treating arbitrary debris as storytelling. [S4](sources-design.md#s4--environmental-storytelling) provides the narrative basis; these graybox translations are our proposals.

## Common defects and first repairs

| Observed concern | First experiment | Re-check |
|---|---|---|
| Impressive view, awkward movement | Reposition the viewing space without narrowing circulation | Approach, departure and off-axis cameras |
| Featureless oversized room | Establish distinct functions and massing; reduce unused travel | Actual choices and traversal time |
| Every room has the same rhythm | Vary one meaningful condition | Whole-route experience |
| Many confusing branches | Make destinations or consequences distinguishable | Unprompted route choices |
| Shortcut adds no value | Compare before/after return routes | Recognition and meaningful saved travel |
| Decorative height | Give elevation a view, route or gameplay purpose—or remove it | Accessible transitions and camera |
| Beautiful pitch, no evidence | Build the smallest testable section | Observed behavior, not prose quality |

Keep experiments inexpensive. The blockout exists so fundamental decisions can change before detailed assets become commitments ([S5](sources-design.md#s5--blockout)). Never confuse a coherent explanation with a successful playtest.
