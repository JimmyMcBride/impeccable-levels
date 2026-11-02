# Worked example: an occupied sliver of a vast sanctuary

**Status: original, plan-only design hypothesis. No scene, collision, camera or human response has been tested.** Numbers are authored example inputs, not recommended universal dimensions. This illustrates how the skill changes decisions; it is not a template every level should copy.

## Brief and choice

Build a short third-person exploration graybox. Let the player enter an ancient sanctuary, investigate a side alcove and reach an upper lookout. Inspire curiosity and perceived scale within a compact traversable footprint. Use no final art, required jumping, forced camera cut or fog-dependent trick.

Compare two concepts: an open courtyard showing everything immediately, or a sheltered approach crossing a small part of a much larger ruin. Choose the latter for this brief because it supports discovery while exposing a limited amount of playable geometry. The former could be better for a busy quest hub.

Example controller assumptions: 1.8 m height, 0.4 m collision radius, no jump, 32-degree maximum walkable slope, 2.5 m third-person boom. Confirm actual project settings before construction. Widths below are first-pass hypotheses, not clearance certifications.

## Spatial sketch

Use meters, Y up, horizontal X/Z. Bounds below are floor extents, not mesh-center transforms. All required travel remains inside X=0..56, Z=2..40, with playable floors Y=0..3.

| Space | X bounds | Z bounds | Floor Y | Purpose / connection |
|---|---|---|---|---|
| Arrival | 0..10 | 2..6 | 0 | Ordinary doorway and scale anchor; enters approach |
| Approach | 10..20 | 2..8 | 0 | Offset boundary masses hide the full chasm; joins terrace |
| Terrace | 20..28 | 4..12 | 0 | Safe stopping place; bridge begins at its far edge |
| Bridge | 24..28 | 12..30 | 0 | Crosses exposed gap to lower hall |
| Lower hall | 18..34 | 30..40 | 0 | Recognizable destination, side investigation and ramp access |
| Alcove | 34..42 | 34..40 | 0 | Optional evidence of the place's old function; returns to hall |
| Ramp | 34..46 | 30..34 | 0→3 along +X | 3 m rise over 12 m horizontal run, about 14 degrees; verify seams and camera |
| Upper lookout | 46..56 | 28..38 | 3 | Looks back across the bridge and recognizes the traversed fragment |

Return by the same supported route. Do not invent a drop or shortcut this brief does not require. A later shortcut would need its own purpose, spatial connection and state test.

Add boundary walls only after maintaining all shared openings and clear widths. Keep the alcove and ramp separated where their floor heights differ. The table establishes intended adjacency, not a certified collision solution.

## Perceived world, not extra errands

Place coarse inaccessible buttresses across and below the crossing, a distant broken arcade and one dominant sanctuary silhouette beyond the playable bounds. Their role is visual context. Use barriers and discontinuities to avoid promising a walkable route onto them. Give the bridge ordinary human-scale rail supports; do not enlarge every reference object along with the sanctuary.

The deep void uses a simple distant floor/background, not a playable abyss. Avoid detailed CSG constructions for unseen interiors. Use silhouettes and overlap before atmospheric effects.

## View sequence

| View | Test from the normal controller | Hypothesis / risk |
|---|---|---|
| Approach | Near a human-scale doorway; only the top of the far structure is visible | Partial information may invite curiosity; do not hide the local exit |
| Terrace | Foreground railing, bridge in middle distance, distant supports and sanctuary | Depth and scale contrast may feel grand; a small far silhouette may instead look insignificant |
| Bridge | Moving view with shifting foreground occlusion | The world should remain convincing beyond one exact pose; camera collision must not obscure the route |
| Lookout | Bridge and arrival visible as small but recognizable features | Recognition may convey progress and a larger system; clutter could destroy that understanding |

## Build and test

First build floors, ramp and controller-scale references. Verify every shared edge and return route. Add only the boundary masses that frame the view, then the distant silhouettes. In Godot, use independent local CSG assemblies for editable playable structures and simple non-colliding mesh proxies for background massing where appropriate.

If the terrace feels flat, first compare depth overlap and the relationship between the familiar anchor and landmark; do not immediately lengthen the bridge. If players pursue an inaccessible arcade, change the route cues or boundary language rather than adding an invisible wall to an inviting path.

Record traversal and matched player-camera captures. Ask new players where they wanted to go and what gave them a sense of scale. Only afterward decide whether to retain the approach, change the silhouette, or reconsider the concept. Before art replacement, preserve the openings, ramp profile, bridge width, foreground anchors and reviewed sightlines.
