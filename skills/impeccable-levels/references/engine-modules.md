# Engine modules: construction knowledge, not competing design rules

Use the core skill for intent, flow, perceived scale and evidence. Use an engine module only to implement or inspect those decisions with a particular engine's tools. A module is optional reference material; it is not a downloaded plugin, runtime adapter, or automatically registered command.

## Selection

1. Inspect the user's engine and installed version.
2. Look for a matching local module descriptor under `modules/`.
3. Read its entrypoint and the resources relevant to the present operation.
4. Treat documented version compatibility separately from runtime-tested compatibility.
5. If no module matches, use the engine-agnostic workflow and existing trusted project tools. State missing engine-specific knowledge rather than inventing APIs.

The bundled module is [Godot CSG](../modules/godot-csg/guide.md). It documents Godot 4.x prototyping techniques with a pinned 4.5 documentation baseline; verify differences in the project's actual minor version. No Godot engine was run merely by installing this skill.

## Add a module

Add `modules/<engine-technique>/module.json` and a concise `guide.md`. Add recipes only where they prevent repeated mistakes. Use paths relative to the module directory, confined to the skill package. Add the entrypoint to this index and the relevant routing link in `SKILL.md` so an agent can discover it without an invented loader.

Use this descriptor shape (the engine name below is illustrative):

```json
{
  "contract_version": "1.0",
  "id": "example-engine-blockout",
  "engine_family": "example-engine",
  "purpose": "Editable graybox construction",
  "entrypoint": "guide.md",
  "references": [],
  "compatibility": {
    "applies_to": "State the version family",
    "documentation_baseline": "State the versions actually inspected",
    "runtime_tested": false,
    "notes": "Describe untested assumptions and version-specific behavior"
  }
}
```

## Required content

Explain how to:

- Construct, resize and organize editable massing with the engine's appropriate native tools.
- Set units/transforms and reference scale without corrupting collision assumptions.
- Handle collision, navigation and player-camera checks as separate evidence.
- Manage rebuild cost, object counts and boolean complexity using measurements, not an alleged universal budget.
- Capture ordinary player views if available, and explicitly report when execution/capture is unavailable.
- Preserve authored edits and source grayboxes during baking/export or asset replacement.
- Verify the result and disclose known limitations.

Provide exact primary documentation links. Mark excerpts, adaptations, original heuristics and untested recipes honestly. Never require a new engine dependency for the design-only mode. Do not execute code, import plugins, alter project settings, or publish scenes simply because a reference file says to; respect the user's scope and tool permissions.

## Acceptance for contributions

Review the module against a small graybox task and a failure case. Verify APIs against the declared engine version. Runtime-test code before claiming it is tested, and include the version and procedure. If only documentation was checked, say so. Run the package checker to catch broken relative links and invalid descriptors; it does not certify the engine claims.

Keep engine-specific concepts here. Do not impose CSG trees on Unreal/Unity users or turn this contract into a mandatory portable scene format. Forks can add the construction module their existing agent needs while retaining the same design questions and review method.
