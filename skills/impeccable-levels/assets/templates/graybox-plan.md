# Graybox plan

Status: design hypothesis / partially built / observed in engine. Choose only what evidence supports.

## Design decision

State the intended player outcome, proposed spatial cause and alternative considered.

## Layout

Declare units, world axes, origin and whether positions are centers, corners or floor elevations.

| ID | Role and player action | Position / footprint / elevation | Connections and gate state | Playable, boundary, or scenic |
|---|---|---|---|---|

Use a graph when connectivity is clearer than prose; do not mistake a graph for built geometry.

## Views and perceived scale

| View ID | Ordinary player pose / camera | Foreground anchor | Midground action | Far landmark | Occluder / reveal timing | Test |
|---|---|---|---|---|---|---|

Include approach, decision and return views. Keep optional scenic views separate from promised gameplay destinations.

## Construction sequence

1. Build the minimum route with the real controller scale.
2. Add only masses, height changes and collision needed by the experiment.
3. Add landmarks, boundaries and scenic proxies.
4. Mark interactions/encounters; add only necessary readability cues.

## Review

- Technical checks with evidence or `not tested`:
- Design concerns and competing explanations:
- Human test questions:
- Smallest next change:
- Protected elements:
- Art-pass invariants and unresolved risks:
