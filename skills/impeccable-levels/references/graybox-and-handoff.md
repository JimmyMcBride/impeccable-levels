# Graybox before expensive commitments

Use this original workflow with the craft evidence in [the design source ledger](sources-design.md). The point of a graybox is to make important changes affordable, not to produce a finished environment in gray materials.

## What must exist early

- The actual controller and camera, or a clearly labeled provisional stand-in.
- Main-route floor surfaces, boundaries, doors and height transitions at useful scale.
- The masses that change orientation, shelter, exposure and sightlines.
- Simple placeholders for interactions, encounters and scenic landmarks.
- A familiar scale anchor near important views: a person, ordinary doorway, railing or repeated structural unit.

Keep a few flat materials or values to distinguish roles; pair color with naming, shape or labels. Keep visible gameplay boundaries consistent with collision. Use enough lighting to evaluate legibility, plus any lighting explicitly necessary to a hypothesis. Also inspect a neutral-lighting pass so atmosphere does not conceal bad geometry.

## Build for a reversible experiment

Group by spatial purpose: entry passage, court, bridge, stair assembly, landmark and distant silhouettes. Use stable names and sensible local origins. Keep playable geometry separate from scenic proxies. Maintain simple editable source assemblies even when you create baked previews.

Do not add tiny bevels, brick courses, ornate roofs or detailed foliage to solve problems of route choice, silhouette or scale. If a detail matters mechanically, prototype its envelope: a cover box, camera obstruction or doorway clearance. If it matters only aesthetically, defer it.

Reuse measured modules where appropriate but allow intentional variation. Repetition can convey scale; it can also erase orientation. Keep a distinctive local cue at similar-looking junctions rather than adding arbitrary decoration everywhere.

## Run three passes

**Movement pass:** traverse required and optional paths in relevant states; check spawn, turns, steps, slopes, seams, headroom, landings and return routes. Test actual camera collision separately from body collision. Use relevant enemy/cart envelopes, not just the player capsule.

**Perception pass:** capture approach, junction, reveal and return viewpoints. Check what attracts attention, what is hidden, and where the next possible action is legible. Move through the sequence; a single screenshot is insufficient. Deliberately look away from the intended focal point to test recovery.

**Experience pass:** observe people pursuing the task without a narrated tour. Compare their actions and explanations against the hypothesis. Preserve surprises and contradictory evidence. Use [evaluation](evaluation.md), not an aggregate score.

## Art-pass decision, not a false guarantee

Before a human approves replacement, record:

| Preserve | Why |
|---|---|
| Walkable widths, floor elevations, transition lengths and collision envelopes | Art must not silently change movement or camera clearance |
| Entrances, interaction sockets, encounter boundaries and gate states | Gameplay logic depends on them |
| Landmark silhouette and position | Orientation and recognition depend on the mass, not the mesh name |
| Occluder edges, view openings and negative space | A larger asset can destroy a reveal or crowd the composition |
| Scenic/playable distinction | Decorative edges must not advertise false paths |
| Review viewpoints and test routes | Re-test the same questions after replacement |

Mark uncertain elements as unresolved rather than freezing them as approved. Swap one representative assembly first. Compare asset bounds, collision and screen-space silhouette, then repeat the affected controller/camera tests. Keep the old graybox recoverable. Final art can introduce new readability, performance and accessibility problems; graybox approval does not eliminate the need for later testing.

## Common failure → smaller correction

- **The whole level looks equally important:** remove or subordinate competing masses before adding more landmarks.
- **The map feels empty:** inspect the purpose and duration of its travel before adding filler props.
- **The courtyard looks good only from above:** inspect actual entry and return views; move masses to frame useful views.
- **Every design change is expensive:** split large coupled assemblies and defer detail.
- **Asset replacement changes the route:** restore the approved collision/clearance contract or seek explicit approval for a redesign.
