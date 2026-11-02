"""Regression tests for packaging validation, not tests of level-design quality."""

import json
import tempfile
import unittest
from pathlib import Path

from check_package import check_package


class PackageChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.main = self.root / "SKILL.md"
        self.main.write_text("---\nname: test-skill\ndescription: A test\n---\n# Test\n", encoding="utf-8")

    def test_minimal_valid_package(self):
        self.assertTrue(check_package(self.root)["ok"])

    def test_missing_main(self):
        self.main.unlink()
        self.assertFalse(check_package(self.root)["ok"])

    def test_missing_link(self):
        with self.main.open("a", encoding="utf-8") as stream:
            stream.write("[Missing](absent.md)\n")
        self.assertFalse(check_package(self.root)["ok"])

    def test_existing_relative_link(self):
        (self.root / "guide.md").write_text("# Guide\n", encoding="utf-8")
        with self.main.open("a", encoding="utf-8") as stream:
            stream.write("[Guide](guide.md#section)\n")
        self.assertTrue(check_package(self.root)["ok"])

    def test_escape_rejected(self):
        with self.main.open("a", encoding="utf-8") as stream:
            stream.write("[Escape](../outside.md)\n")
        self.assertFalse(check_package(self.root)["ok"])

    def test_absolute_link_rejected(self):
        with self.main.open("a", encoding="utf-8") as stream:
            stream.write("[Absolute](/etc/passwd)\n")
        self.assertFalse(check_package(self.root)["ok"])

    def test_external_links_not_fetched(self):
        with self.main.open("a", encoding="utf-8") as stream:
            stream.write("[Source](https://example.com)\n[Section](#heading)\n")
        self.assertTrue(check_package(self.root)["ok"])

    def test_fenced_examples_ignored(self):
        with self.main.open("a", encoding="utf-8") as stream:
            stream.write("```markdown\n[Illustration](unwritten.md)\n```\n")
        self.assertTrue(check_package(self.root)["ok"])

    def test_symlink_rejected(self):
        (self.root / "link.md").symlink_to(self.main)
        self.assertFalse(check_package(self.root)["ok"])

    def make_module(self):
        directory = self.root / "modules" / "test-module"
        directory.mkdir(parents=True)
        (directory / "guide.md").write_text("# Module\n", encoding="utf-8")
        data = {
            "contract_version": "1.0", "id": "test-module",
            "engine_family": "test", "purpose": "Test", "entrypoint": "guide.md",
            "references": [], "compatibility": {
                "applies_to": "1.x", "documentation_baseline": "1.0",
                "runtime_tested": False, "notes": "Documentation only"
            }
        }
        path = directory / "module.json"
        path.write_text(json.dumps(data), encoding="utf-8")
        return path, data

    def test_valid_module(self):
        self.make_module()
        self.assertTrue(check_package(self.root)["ok"])

    def test_module_missing_guide(self):
        path, data = self.make_module()
        data["entrypoint"] = "missing.md"
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertFalse(check_package(self.root)["ok"])

    def test_module_invalid_json(self):
        path, _ = self.make_module()
        path.write_text("{", encoding="utf-8")
        self.assertFalse(check_package(self.root)["ok"])

    def test_module_wrong_id(self):
        path, data = self.make_module()
        data["id"] = "different"
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertFalse(check_package(self.root)["ok"])

    def test_runtime_flag_must_be_boolean(self):
        path, data = self.make_module()
        data["compatibility"]["runtime_tested"] = "yes"
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertFalse(check_package(self.root)["ok"])


if __name__ == "__main__":
    unittest.main()
