# Godot CSG grayboxing module

Use this module only for Godot construction. Keep design decisions in the engine-agnostic skill. This module adds guidance to an agent that already edits Godot scenes; it installs no editor plugin or runtime.

**Documentation baseline:** Godot 4.5 class references, checked 2026-11-01. The CSG tutorial carries an outdated-content warning; prefer version-matched class help for API details. Verify the project's exact minor version before using APIs. Recipes are documentation-reviewed, **not engine-tested**. Sources: [Godot evidence ledger](../../references/sources-godot.md).

## Build the experiment first

1. Inspect the existing controller, camera, scene conventions and unit scale. Record body clearance, slope/step behavior, camera reach and protected nodes. Do not replace the project's controller to make the layout pass.
2. Define the question each assembly answers: route readability, arena maneuvering room, gate scale, reveal timing or connection feasibility. Keep an object only if it helps answer that question.
3. Start with floors, wall masses, ramps, major openings, landmark silhouettes and human-scale markers. Use a small neutral material palette; pair semantic colors with names or labels.
4. Put independent assemblies below ordinary `Node3D` organizational parents. Use a local `CSGCombiner3D` only where its children must participate in the same boolean result. A combiner encapsulates its children's operations; nested combiners are not independent performance islands. [G3]
5. Prefer dimension properties such as `CSGBox3D.size` and cylinder height/radius for readable, editable measurements. Keep transforms easy to reason about. This is a workflow convention, not a claim that scaling is forbidden. [G4, G7]
6. Traverse the result with the real controller after each meaningful change. Save player-camera viewpoints at the entrance, decisions, reveal and return route; compare consistent FOV and aspect ratio.

## Spend boolean work deliberately

CSG evaluates child operations in tree order. Keep the solid before its intended cutters and inspect the actual result after reordering. Separate unrelated objects into distinct CSG roots; use boolean operations only where they change the needed shape. [G1]

Godot documents significant CPU costs for CSG creation and movement inside another CSG tree. Avoid animated cuts and per-frame reconstruction. Plain `MeshInstance3D` primitives are suitable for masses that need no booleans. [G4]

For this workflow, keep a courtyard's enclosure, an arch and a distant tower independently editable. Do not union a whole level merely to tidy the scene tree. Start with coarse circular silhouettes; add segments only when the gameplay view needs them. Profile edit latency, scene startup and traversal on the actual target—there is no universal safe CSG node count.

When a cut looks wrong, isolate the assembly, check operation order and transforms, and extend the cutter through the solid rather than ending exactly on its face. The last suggestion is a robustness heuristic, not a guaranteed cure. Imported `CSGMesh3D` inputs must be manifold; an open plane is not a solid cutter. [G5]

Use editor grid/transform snapping for placement. Do not treat the deprecated `CSGShape3D.snap` property as a boolean tolerance knob; it has no effect in the documented version. For flat prototypes that do not use normal/height maps, consider disabling `calculate_tangents` on the root and measure whether the change matters. [G2]

## Collision is a separate test

Configure collision on the effective CSG root, not every boolean operand. The implementation creates the collision body only for a root shape. [G9] CSG collision acts as a static body; hiding the node does **not** disable its collision. [G2]

Keep scenic proxies non-colliding. When swapping a source assembly for a baked result, explicitly disable/remove its active source collision to avoid duplicate or invisible blockers. Test floor seams, door thresholds, ceiling edges, ramp transitions and camera sweeps. A visible opening or navigation path is not proof that the actual controller fits.

Use the project's moving-body setup for a working drawbridge. `AnimatableBody3D` is documented for moving platforms and doors; animated CSG geometry is not the default solution. [G8]

## Bake selectively; preserve the editable source

Godot 4.5 exposes `bake_static_mesh()` and `bake_collision_shape()` on CSG roots. Verify `is_root_shape()`. Updates are deferred: wait a process frame after relevant edits before reading the result, then confirm the baked resource contains geometry, not merely that a resource exists. Baking a non-root can yield empty output. [G2]

Bake a stable assembly only when it helps an actual performance or delivery need. Keep an editable source scene separate from its active baked instance. Record the source revision, transforms, materials and collision policy. Do not bake away uncertainty during the design pass.

Before an art swap, preserve the tested openings, floor heights, camera envelope, collision intent, landmark silhouette and reveal viewpoints. Re-test the replacement: a decorative buttress can destroy a proven path or sightline. Keep the graybox as a reference until the replacement is accepted.
