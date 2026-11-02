# Graybox recipes for Godot

These are original construction experiments, not universal dimensions or tested scene generators. Derive sizes from the project's player, camera, mechanics and brief. Use the [CSG guide](guide.md) for version checks, performance and collision. Review results from ordinary gameplay views before adding detail.

## 1. Courtyard: choose proportion before decoration

**Question:** Does the space support its activity while establishing a clear next destination?

- Start with a floor slab and separate wall/building masses. Leave real gaps for entrances instead of subtracting every opening from one giant solid.
- Place an ordinary door or player-height marker near the dominant structure. Reserve clear working space for combat, circulation or gathering before adding stalls or pillars.
- Vary enclosure and one meaningful elevation rather than distributing objects evenly. Keep the required route readable after the player turns around.
- **Check:** Walk all approaches, turn the camera beside walls, and compare the focal structure against the human-scale anchor. If the court feels empty, test compression or a useful activity zone before increasing decoration.

## 2. Gate or arch: give the opening a job

**Question:** Does the threshold communicate scale, frame a destination and allow traversal?

- First test two side piers and a lintel as separate masses. If an arched silhouette matters, use a local wall assembly with a rectangular opening plus a rounded or polygonal upper cutter.
- A cylinder-based cutter needs its axis aligned through the wall; a custom profile can use `CSGPolygon3D` depth extrusion. Draw the profile in local XY without self-intersection; depth mode extrudes along local negative Z. [G6]
- Make cutter depth exceed wall thickness. Keep the walking/camera aperture separate from the decorative arch envelope.
- **Check:** Traverse both ways and stop under the arch. Verify that the lintel does not force an unacceptable camera collision and that the destination remains legible. A grand façade does not require an equally oversized everyday doorway.

## 3. Stairs or ramp: test the actual movement policy

**Question:** Can the player change elevation comfortably while understanding the route?

- Represent a simple ramp with an extruded triangular profile, or build a short stair flight from repeated boxes. Add landings wherever turning, pausing or a camera change needs room.
- For a rise `H` and positive horizontal run `R`, calculate slope as `atan(H / R)`; convert radians to degrees if that is how the controller expresses its limit. Leave a justified project-specific margin and test the transitions.
- For explicit steps, choose riser height from the controller's supported stepping behavior. Do not assume a capsule automatically climbs every small step.
- A smooth collision ramp under visual stairs is an optional controller strategy, not a free fix. Keep it independently editable, document the mismatch, and test foot placement, sliding, ledge behavior and camera motion. Avoid simultaneous stair and ramp collisions.
- **Check:** Ascend, descend, stop, turn and approach diagonally. Geometry alone cannot certify movement quality.

## 4. Drawbridge: reserve motion before implementing it

**Question:** Can the lowered span carry the intended traffic and can the mechanism move unobstructed?

- Begin with a flat bridge proxy, abutments, moat gap and gate. Mark the hinge and full raised/lowered swept volume.
- Use explicit cart width, height, length and turning requirements; trace its whole envelope through approach, bridge, gate and departure—not just a centerline.
- A static CSG proxy can compare the two endpoint compositions. A working bridge needs proper moving-body collision and state tests; follow the project's `AnimatableBody3D` or other established setup. [G8]
- If CSG remains as a visual child, disable its `use_collision` and use the moving body's own collision shape. Do not leave a hidden static CSG collider alongside the moving bridge. [G2]
- **Check:** The lowered span reaches both banks, the raised span misses the gate, and no scenery occupies the swept volume. Inspect player/cart behavior during motion if motion is implemented. Label unimplemented motion as untested.

## 5. Chasm and distant ruin: build perceived scale cheaply

**Question:** Does a small playable route feel embedded in a much larger place?

- Build only the reachable shelf, safe overlook, crossing and far landing as gameplay geometry. Use separate low-detail masses for distant walls, broken bridges and towers.
- Establish near framing, a middle-distance crossing and a distant silhouette. Include a familiar-scale feature near the player; do not make every object monumental.
- Use plain mesh proxies where no boolean edit is needed. Keep backdrop collision off and prevent their shapes from falsely advertising reachable paths.
- **Check:** Approach, sidestep, look back and change camera yaw. The depth should survive parallax and ordinary movement without fog hiding a broken illusion. If forced-perspective proxies fail outside a narrow viewpoint, constrain the view honestly or revise the arrangement.

For every recipe, retain the smallest geometry that supports the test. Replace it with production assets only after the route, camera and intended experience have earned the next pass.
