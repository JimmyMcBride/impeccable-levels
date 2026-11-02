# Design research and provenance

Research checked 2026-11-01. Links identify original papers, practitioner-authored documentation and official conference session records. Summaries below are deliberately brief. No talk transcript, images or slides are redistributed. The procedural cards elsewhere are **original Impeccable Levels hypotheses**, not validated psychological laws or quotations from these sources.

## S1 — MDA

Robin Hunicke, Marc LeBlanc and Robert Zubek, *MDA: A Formal Approach to Game Design and Game Research* (2004). [Original paper](https://users.cs.northwestern.edu/~hunicke/MDA.pdf). **Inspected:** paper text.

Distinguishes implementation, behavior during play and intended player experience; argues for more specific vocabulary than undifferentiated “fun.” Use it to articulate an experience hypothesis and relate spatial decisions to observable play. It does not establish a formula that guarantees enjoyment.

## S2 — Metrics

The Level Design Book, [Metrics](https://book.leveldesignbook.com/process/blockout/metrics). **Inspected:** chapter text.

Separates measured player/physics properties from designer-chosen building guidelines. Discusses the gap between literal world dimensions and perceived scale. Use project metrics and playtests rather than importing real-world sizes or numerical rules as universal truths.

## S3 — Wayfinding

The Level Design Book, [Wayfinding](https://book.leveldesignbook.com/process/blockout/wayfinding). **Inspected:** chapter text.

Distinguishes orientation from navigation, emphasizes mental maps and player agency, and challenges the assumption that players always want the intended critical path. Use landmarks and information to support chosen exploration, not to pretend that attention can be reliably controlled.

## S4 — Environmental storytelling

Harvey Smith and Matthias Worch, GDC 2010, [What Happened Here? Environmental Storytelling](https://www.gdcvault.com/play/1012647/What-Happened-Here-Environmental). **Inspected:** official session overview, not full video.

The overview describes environments as information players interpret, with implied history and systems that reflect player agency. This supports testing whether spatial evidence communicates a plausible history. Specific graybox implementations in this skill are our proposals, not a detailed extraction of the talk.

## S5 — Blockout

The Level Design Book, [Blockout](https://book.leveldesignbook.com/process/blockout). **Inspected:** chapter text.

Presents rough geometry as a way to test and cheaply revise foundational shapes before polished art. Identifies massing, metrics, wayfinding and playtesting as relevant considerations. Use grayboxes to investigate play, not merely to preview final aesthetics.

## S6 — Composition

The Level Design Book, [Composition](https://book.leveldesignbook.com/process/blockout/massing/composition). **Inspected:** chapter text.

Distinguishes overall three-dimensional organization from a specific two-dimensional shot. Warns against overvaluing a single camera composition. Use hierarchy and contrast, then inspect multiple ordinary player viewpoints. This is a useful counterweight to treating every level as a cinematic corridor.

## S7 — Spatial cinematography

Miriam Bellard, GDC 2019, [Environment Design as Spatial Cinematography: Theory and Practice](https://www.gdcvault.com/play/1025736/Environment-Design-as-Spatial-Cinematography). **Inspected:** official session overview, not full video.

The overview connects environment design, player movement, attention and the onscreen experience when players control the camera. Use this as motivation for testing the sequence of views along an approach. Do not attribute the skill's specific reveal procedures or scale ratios to Bellard.

## S8 — Invisible Intuition

David Shaver and Robert Yang, GDC 2018, [Invisible Intuition: Blockmesh and Lighting Tips to Guide Players and Set the Mood](https://www.gdcvault.com/play/1025360/Level-Design-Workshop-Invisible-Intuition). **Inspected:** official session overview, not full presentation/slides.

The overview explicitly connects early blockmesh iteration, flow, playtest feedback and lighting-based readability. Use that scope to justify testing navigation and mood before final assets. Avoid asserting individual techniques or talk demonstrations not inspected here.

## S9 — Playtesting

The Level Design Book, [Playtesting](https://book.leveldesignbook.com/process/blockout/playtesting). **Inspected:** chapter text.

Distinguishes self-testing, expert critique and public/blind playtests. Observed behavior can reveal problems an author misses. The skill's evidence labels, controlled comparisons and reporting format are its own evaluation protocol; a text review is not a substitute for someone playing.

## S10 — Modular construction

Joel Burgess and Nate Purkeypile, GDC 2013, [Skyrim's Modular Approach to Level Design](https://www.gamedeveloper.com/design/skyrim-s-modular-approach-to-level-design). **Inspected:** practitioner-authored article adapting their talk.

Describes modular kits as reusable systems rather than unrelated pieces, with production benefits and constraints. Use early agreement on connection dimensions and replacement boundaries. This is a case study, not evidence that all levels need the same kit or grid.

## Research boundaries

- No source here demonstrates that this skill consistently outperforms a baseline agent.
- No formula here predicts awe, ideal corridor width, universal encounter spacing or an optimal number of loops.
- “Common defects” are diagnostic candidates, not measured prevalence claims about AI-generated levels.
- When sources emphasize different approaches, preserve the tradeoff: cinematic attention and free exploration are not interchangeable goals.
- Refresh engine facts through the engine module's source ledger; these design references do not establish engine behavior.

## Inspiration and reuse

The project concept is inspired by [Impeccable](https://github.com/pbakaus/impeccable), the frontend-design skill. This is an independent level-design project, not an official module or endorsement. No upstream skill text or code was copied. The [MIT license](../LICENSE) applies to this package's original material; linked third-party works retain their own terms and are not bundled.
