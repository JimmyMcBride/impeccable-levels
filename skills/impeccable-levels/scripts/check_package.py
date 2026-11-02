#!/usr/bin/env python3
"""Check skill packaging only; never evaluate levels or execute engine code."""

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


def confined_target(root, base, value):
    """Resolve a relative package file, rejecting escapes and absolute paths."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError("expected a nonempty relative path")
    parsed = urlsplit(value)
    if parsed.scheme or parsed.netloc or parsed.query:
        raise ValueError("expected a package path, not a URL")
    raw_path = unquote(parsed.path)
    if not raw_path or Path(raw_path).is_absolute() or "\\" in raw_path:
        raise ValueError("expected a nonempty relative POSIX path")
    target = (base / raw_path).resolve()
    if not target.is_relative_to(root):
        raise ValueError("path escapes the skill package")
    if not target.is_file():
        raise ValueError("target file is missing")
    return target


def check_package(path):
    root = Path(path).resolve()
    errors = []
    checks = 0
    if not root.is_dir():
        return {"ok": False, "checks": 1, "errors": ["skill directory is missing"]}

    def error(file, message):
        label = str(file.relative_to(root))
        errors.append(f"{label}: {message}")

    main = root / "SKILL.md"
    checks += 1
    if not main.is_file():
        error(main, "missing SKILL.md")
    elif not main.is_symlink():
        content = main.read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|$)", content, re.S)
        if not frontmatter:
            error(main, "missing YAML frontmatter")
        else:
            # The package uses two single-line YAML fields. The official skill
            # validator remains responsible for full YAML validation.
            fields = {}
            for line in frontmatter.group(1).splitlines():
                key, separator, value = line.partition(":")
                if not separator or key in fields:
                    error(main, "invalid or duplicate frontmatter field")
                fields[key] = value.strip()
            if set(fields) != {"name", "description"}:
                error(main, "frontmatter must contain only name and description")
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", fields.get("name", "")):
                error(main, "invalid skill name")
            if not fields.get("description"):
                error(main, "empty description")
        if len(content.splitlines()) >= 500:
            error(main, "keep the core under 500 lines")

    files = sorted(root.rglob("*"))
    for file in files:
        if file.is_symlink():
            error(file, "symlinks are not allowed in this portable package")
            continue
        if not file.is_file() or file.suffix != ".md":
            continue
        # Ignore illustrative code blocks when checking Markdown links.
        content = file.read_text(encoding="utf-8")
        content = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", content, flags=re.M | re.S)
        for match in re.finditer(r"\[[^\]]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)", content):
            target = match.group(1)
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            checks += 1
            try:
                confined_target(root, file.parent, target)
            except ValueError as exc:
                error(file, f"bad link {target!r}: {exc}")

    ids = set()
    for manifest in sorted(root.glob("modules/*/module.json")):
        checks += 1
        if manifest.is_symlink():
            continue
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
        except (ValueError, OSError) as exc:
            error(manifest, f"invalid JSON: {exc}")
            continue
        if not isinstance(data, dict):
            error(manifest, "descriptor must be an object")
            continue
        expected = {"contract_version", "id", "engine_family", "purpose", "entrypoint", "references", "compatibility"}
        if set(data) != expected:
            error(manifest, "descriptor fields differ from the documented contract")
        for key in ("contract_version", "id", "engine_family", "purpose", "entrypoint"):
            if not isinstance(data.get(key), str) or not data[key].strip():
                error(manifest, f"{key} must be a nonempty string")
        if data.get("contract_version") != "1.0":
            error(manifest, "unsupported module contract version")
        module_id = data.get("id")
        if isinstance(module_id, str):
            if module_id in ids:
                error(manifest, "duplicate module id")
            ids.add(module_id)
            if module_id != manifest.parent.name:
                error(manifest, "module id must match its directory")
        refs = data.get("references")
        if not isinstance(refs, list) or not all(isinstance(v, str) for v in refs):
            error(manifest, "references must be an array of strings")
            refs = []
        for link in [data.get("entrypoint")] + refs:
            checks += 1
            try:
                confined_target(root, manifest.parent, link)
            except ValueError as exc:
                error(manifest, f"bad resource {link!r}: {exc}")
        compatibility = data.get("compatibility")
        if not isinstance(compatibility, dict):
            error(manifest, "compatibility must be an object")
            continue
        for key in ("applies_to", "documentation_baseline", "notes"):
            if not isinstance(compatibility.get(key), str) or not compatibility[key].strip():
                error(manifest, f"compatibility.{key} must be a nonempty string")
        if type(compatibility.get("runtime_tested")) is not bool:
            error(manifest, "compatibility.runtime_tested must be boolean")

    return {
        "ok": not errors,
        "checks": checks,
        "errors": errors,
        "scope": "Package integrity only. No engine, playability, fun, or awe test performed."
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    result = check_package(args.path)
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
