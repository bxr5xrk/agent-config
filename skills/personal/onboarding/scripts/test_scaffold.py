#!/usr/bin/env python3
import json
from pathlib import Path
import tempfile
import unittest
from scaffold import scaffold


def state(profile, design="selected"):
    return {"schema_version": 1, "profile": profile, "brief_agreed": True,
            "onboarding_track": {"value": "product_brand", "reason": "New commercial product"},
            "brand": {"status": "approved", "approved_name": "Sample", "override_reason": None},
            "design": {"status": design, "selected_ids": ["A"], "override_reason": None}}


class ScaffoldTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def test_profiles_and_decisions(self):
        for profile, expected in [("api", {"api"}), ("web", {"web"}), ("fullstack", {"api", "web"})]:
            with self.subTest(profile=profile):
                original = state(profile)
                original["decisions"] = {"language": "typescript-strict"}
                result = scaffold(self.root / profile, "sample", profile, original)
                self.assertEqual({p.name for p in (result / "apps").iterdir()}, expected)
                saved = json.loads((result / "docs/onboarding/state.json").read_text())
                self.assertEqual(saved["decisions"], original["decisions"])
                self.assertNotIn("phase", original)

    def test_agreed_documents_are_carried_instead_of_replaced(self):
        source = self.root / "discovery"
        source.mkdir()
        (source / "BRIEF.md").write_text("Agreed product and actual first journey")
        result = scaffold(self.root / "project", "sample", "api", state("api"), source)
        self.assertEqual((result / "docs/onboarding/BRIEF.md").read_text(), "Agreed product and actual first journey")

    def test_no_overwrite_even_empty_or_dangling_symlink(self):
        for name in ["empty", "populated", "link"]:
            dest = self.root / name
            if name == "link":
                dest.symlink_to(self.root / "missing")
            else:
                dest.mkdir()
                if name == "populated":
                    (dest / "user.txt").write_text("keep")
            with self.assertRaises(FileExistsError):
                scaffold(dest, "sample", "api", state("api"))
        self.assertEqual((self.root / "populated/user.txt").read_text(), "keep")

    def test_visual_choice_required_for_web_but_not_api(self):
        with self.assertRaises(ValueError):
            scaffold(self.root / "web", "sample", "web", state("web", "pending"))
        self.assertFalse((self.root / "web").exists())
        scaffold(self.root / "api", "sample", "api", state("api", "not_applicable"))

    def test_lightweight_site_skips_brand_and_visual_gates(self):
        original = state("web", "pending")
        original["onboarding_track"] = {
            "value": "lightweight_site", "reason": "Small informational site with known content"}
        original["brand"]["status"] = "pending"
        result = scaffold(self.root / "lightweight", "sample", "web", original)
        self.assertFalse((result / "docs/onboarding/BRAND.md").exists())
        self.assertIn("BRIEF.md/DESIGN.md", (result / "docs/onboarding/STARTER.md").read_text())

    def test_web_track_requires_a_recorded_reason(self):
        original = state("web")
        original["onboarding_track"] = {"value": "lightweight_site", "reason": None}
        with self.assertRaises(ValueError):
            scaffold(self.root / "web-track", "sample", "web", original)
        self.assertFalse((self.root / "web-track").exists())

    def test_brand_foundation_required_for_new_web_state(self):
        original = state("web")
        original["brand"]["status"] = "pending"
        with self.assertRaises(ValueError):
            scaffold(self.root / "web", "sample", "web", original)
        self.assertFalse((self.root / "web").exists())

    def test_brand_override_requires_reason(self):
        original = state("web")
        original["brand"] = {"status": "user_override", "approved_name": None, "override_reason": None}
        with self.assertRaises(ValueError):
            scaffold(self.root / "bad-brand", "sample", "web", original)
        original["brand"]["override_reason"] = "User supplied an approved external brand system"
        scaffold(self.root / "good-brand", "sample", "web", original)

    def test_explicit_override_requires_reason(self):
        original = state("web", "user_override")
        with self.assertRaises(ValueError):
            scaffold(self.root / "bad", "sample", "web", original)
        original["design"]["override_reason"] = "User supplied the already approved design"
        scaffold(self.root / "good", "sample", "web", original)

    def test_brief_profile_name_validated_before_writing(self):
        invalid = state("api")
        invalid["brief_agreed"] = False
        for name, profile, value in [("sample", "api", invalid), ("sample", "web", state("api")), ("../bad", "api", state("api"))]:
            with self.assertRaises(ValueError):
                scaffold(self.root / "no-write", name, profile, value)
        self.assertFalse((self.root / "no-write").exists())


if __name__ == "__main__":
    unittest.main()
