# Godot module evidence ledger

Checked 2026-11-01. These are official engine documentation or implementation sources. The module uses Godot **4.5** as its pinned documentation baseline, not as a claim about the user's installed engine. The CSG tutorial carries an outdated-content notice. Check the target minor version locally and prefer version-matched class references for APIs. No engine execution was performed for this module.

The practical arrangements, recipes and review procedures are Impeccable Levels' own recommendations. API statements below are documented facts, not proof that a particular assembled level works.

## G1 — CSG prototyping and processing order

[Prototyping levels with CSG, Godot 4.5](https://docs.godotengine.org/en/4.5/tutorials/3d/csg_tools.html)

Establishes CSG's prototyping role, tree-order operations and the recommendation to keep geometry simple and unrelated assemblies in separate trees. The tutorial carries a version-update warning; use class references for API details.

## G2 — Root output, collision and baking

[CSGShape3D, Godot 4.5](https://docs.godotengine.org/en/4.5/classes/class_csgshape3d.html)

Documents root-only baking, deferred mesh updates and static collision that remains active when hidden. `snap` is deprecated and has no effect; editor transform snapping is a different feature. Do not use this property as a boolean tolerance control.

## G3 — Combining operations

[CSGCombiner3D, Godot 4.5](https://docs.godotengine.org/en/4.5/classes/class_csgcombiner3d.html)

Explains grouped operation results. A nested combiner remains part of its parent CSG calculation; organization is not automatic runtime isolation.

## G4 — Dimensions and update costs

[CSGBox3D, Godot 4.5](https://docs.godotengine.org/en/4.5/classes/class_csgbox3d.html)

Documents `size` and warns about CSG creation and moving nodes within CSG trees. Preferring explicit dimensions and plain meshes for non-boolean proxies is the module's workflow recommendation.

## G5 — Custom mesh validity

[CSGMesh3D, Godot 4.5](https://docs.godotengine.org/en/4.5/classes/class_csgmesh3d.html)

Requires manifold solids and excludes unsuitable open primitives such as planes. This constrains cutter selection, not the appearance of an entire graybox.

## G6 — Extruded profiles

[CSGPolygon3D, Godot 4.5](https://docs.godotengine.org/en/4.5/classes/class_csgpolygon3d.html)

Documents depth, spin and path modes. Depth follows local negative Z; intersecting polygon edges prevent triangulation. The module's ramp/arch recipes are proposed applications.

## G7 — Cylinder controls

[CSGCylinder3D, Godot 4.5](https://docs.godotengine.org/en/4.5/classes/class_csgcylinder3d.html)

Documents radius, height and side count. Choose tessellation for the test view and profile performance; do not treat a particular side count as a universal optimum.

## G8 — Moving-body alternative

[AnimatableBody3D, Godot 4.5](https://docs.godotengine.org/en/4.5/classes/class_animatablebody3d.html)

Describes manually moved bodies suited to platforms and doors, with physics synchronization. This supports separating moving drawbridge behavior from static CSG prototyping, not a complete drawbridge implementation.

## G9 — Effective CSG collision root

[CSG implementation, Godot master](https://github.com/godotengine/godot/blob/master/modules/csg/csg_shape.cpp)

The inspected `set_use_collision` implementation creates the body only when inside the tree and at a CSG root. This source is unpinned; confirm behavior on the target version rather than treating the development branch as a release guarantee.
