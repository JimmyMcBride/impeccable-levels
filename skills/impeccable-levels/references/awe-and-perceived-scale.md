# Awe and perceived scale in a compact graybox

Treat awe as an **experience hypothesis**, not an automatic consequence of height, fog or polygon count. These Impeccable Levels procedures are original proposals informed by the [research ledger](sources-design.md). They require player-camera tests and human responses.

## Separate three budgets

- **Playable space:** the footprint, vertical range, routes and interactions the player can actually use.
- **Scenic space:** visible masses that communicate surroundings but do not require full playable interiors or collision.
- **Attention:** which relationships the player can understand at a given moment.

Label scenic geometry explicitly. A distant arch can imply a continent-spanning structure without requiring a continent of traversal. It must not accidentally promise a jump, ledge or destination the game cannot support. Keep known future destinations spatially consistent.

The [metrics discussion](sources-design.md#s2--metrics) distinguishes perceived scale from literal real-world dimensions. This is not permission to use arbitrary proportions: preserve coherent local interaction sizes and test the result in motion.

## Make the scale readable

| Design problem | Graybox experiment | Evidence and failure check |
|---|---|---|
| Monument looks like a normal building | Place a familiar-sized doorway, landing or person marker beside its major mass | Can ordinary views communicate the size relationship? Enlarging every reference removes the comparison. |
| Distant world looks flat | Arrange overlapping foreground, middle-distance and background masses with visible separation | Walk laterally and forward; inspect changing overlap/parallax. A single attractive screenshot is insufficient. |
| Everything competes for attention | Give the important silhouette clear negative space; simplify neighboring masses | Does the focal relationship survive normal camera positions? Avoid deleting useful gameplay features solely for framing. |
| World feels immediately exhausted | Obscure part of its extent with terrain or architecture; imply plausible continuation | Does the route still communicate local possibilities? An invisible-wall maze does not create satisfying mystery. |
| Huge space feels empty | Reduce mandatory walking and relocate activity nearer the view; preserve distant scale layers | Compare route effort, decisions and human response. Large quiet spaces are valid when intentional. |
| Vista has no payoff | Connect it to an identifiable destination, relationship, question or later discovery | Ask what the player understood or wanted to investigate, without announcing the intended emotion. |

## Design the approach, not only the hero frame

For a reveal-centered brief, mark several ordinary player poses: initial hint, approach, strongest view and departure. At each, record the visible target, foreground obstruction, scale reference and next action. Keep the actual camera/FOV and aspect ratio. Do not move only the screenshot camera until the level appears successful.

Place the best observation opportunity where stopping is possible without falling or receiving unavoidable damage. Test entering from alternate directions, looking away, backing up and taking the return route. A free-camera player cannot be assumed to watch a scripted composition. [S6](sources-design.md#s6--composition) emphasizes spatial organization across viewpoints; [S7](sources-design.md#s7--spatial-cinematography) supports thinking about environment, movement and attention together.

Do not mandate a narrow passage before every vista. Grandeur can also emerge from sustained exposure, gradual understanding, small habitation beneath old infrastructure, or returning high above a familiar place.

## Use illusion honestly and cheaply

Prototype skyline pieces as simple silhouettes before modeling distant buildings. Use only enough depth to test the visible relationship. Keep scenic proxies separately grouped so art replacement cannot accidentally change a playable route.

Forced perspective is a candidate experiment for controlled viewing regions, not a default technique for free-roaming levels. Test its failure from side views, height changes and permitted camera motion. If the distortion becomes obvious, use real separation and occlusion instead. Never fix the illusion by silently changing player controls.

Lighting, atmosphere and sound can contribute later, or appear as minimal placeholders when essential to the hypothesis. First run a readable neutral pass to expose geometry problems. Then compare the intended treatment. Do not equate “works without any atmosphere” with a universal artistic requirement.

## Test changed understanding, not just size

[S11](sources-design.md#s11--awe-as-an-appraisal-framework) proposes perceived vastness and a need to revise existing understanding as central to awe. This is a conceptual framework, not a tested level recipe. [S12](sources-design.md#s12--awe-in-immersive-vr) found higher reported awe in three immersive environments than a neutral one, but no significant between-condition difference in accommodation. It does not isolate reveal design or establish desktop-graybox effects.

Our additional experiment: let a later view connect a familiar local space to a larger whole. A modest passage might become recognizable as one buttress of the structure now overhead. Use actual coherent geometry, not a visual trick that contradicts the return journey. A beautiful sustained vista remains valid; not every place needs a twist.

Before building, record:

- **Initial interpretation:** what might the player think this place is?
- **New relationship:** what later becomes visible about its extent, function, age or their location within it?
- **Recognition cue:** which already encountered shape or route makes the connection legible?
- **Local action:** where can the player stop safely, and what can they do next?

Compare a scale-only vista with the relationship-revealing variant under matched controller, camera, lighting, playable footprint and route conditions. Record unavoidable differences. Ask first what caught attention and what changed in the player's understanding. Then ask separately about perceived scale and feelings, including awe, curiosity, fear or confusion. Understanding a relationship is evidence of comprehension, not proof of awe. Preserve clear movement affordances even when the world's history remains mysterious.

## Completion question

Can this compact graybox offer both an enjoyable local journey and the impression of a larger coherent world? Record observations, not “awe achieved.” Note what still depends on art, audio or human testing, and protect the established silhouettes, viewpoints, scale anchors and route clearances during replacement.
