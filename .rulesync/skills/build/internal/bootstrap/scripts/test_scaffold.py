#!/usr/bin/env python3
import json
from pathlib import Path
import tempfile
import unittest
from scaffold import scaffold, SKILL


def state(profile, design="selected"):
    return {"schema_version": 1, "profile": profile, "brief_agreed": True,
            "design": {"status": design, "selected_ids": ["A"], "override_reason": None}}


class ScaffoldTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.documents = self.root / "decisions"
        self.documents.mkdir()
        (self.documents / "BRIEF.md").write_text("User agreed: submit an issue and see the saved issue.")
        (self.documents / "DESIGN.md").write_text("User selected option A: compact issue list with persistent navigation.")

    def test_profiles_and_decisions(self):
        for profile, expected in [("api", {"api"}), ("web", {"web"}), ("fullstack", {"api", "web"})]:
            with self.subTest(profile=profile):
                original = state(profile)
                original["decisions"] = {"language": "typescript-strict"}
                result = scaffold(self.root / profile, "sample", profile, original, self.documents)
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

    def test_missing_or_placeholder_agreed_documents_fail_before_creation(self):
        original_brief = (self.documents / "BRIEF.md").read_text()
        for invalid in [None, "   ", (SKILL / "assets/documents/BRIEF.md").read_text()]:
            with self.subTest(brief=repr(invalid)[:30]):
                brief = self.documents / "BRIEF.md"
                if invalid is None:
                    brief.unlink()
                else:
                    brief.write_text(invalid)
                with self.assertRaises(ValueError):
                    scaffold(self.root / "missing-parent/project", "sample", "api", state("api"), self.documents)
                self.assertFalse((self.root / "missing-parent").exists())
        (self.documents / "BRIEF.md").write_text(original_brief)
        (self.documents / "DESIGN.md").unlink()
        with self.assertRaises(ValueError):
            scaffold(self.root / "web", "sample", "web", state("web"), self.documents)
        self.assertFalse((self.root / "web").exists())

    def test_explicit_design_override_can_omit_design_document(self):
        (self.documents / "DESIGN.md").unlink()
        original = state("web", "user_override")
        original["design"]["override_reason"] = "User delegated design selection and waived the board"
        result = scaffold(self.root / "delegated", "sample", "web", original, self.documents)
        saved = json.loads((result / "docs/onboarding/state.json").read_text())
        self.assertEqual(saved["design"], original["design"])
        self.assertEqual((result / "docs/onboarding/BRIEF.md").read_text(), (self.documents / "BRIEF.md").read_text())

    def test_api_without_visual_scope_records_design_as_not_applicable(self):
        (self.documents / "DESIGN.md").unlink()
        result = scaffold(self.root / "api", "sample", "api", state("api", "not_applicable"), self.documents)
        design = (result / "docs/onboarding/DESIGN.md").read_text()
        self.assertIn("Visual design: not applicable", design)
        saved = json.loads((result / "docs/onboarding/state.json").read_text())
        self.assertEqual(saved["next_action"], "Implement the first real API journey")

        supplied = "API documentation examples use the parent project's approved visual system."
        (self.documents / "DESIGN.md").write_text(supplied)
        other = scaffold(self.root / "api-with-context", "sample", "api", state("api"), self.documents)
        self.assertEqual((other / "docs/onboarding/DESIGN.md").read_text(), supplied)

    def test_landing_review_is_carried_only_when_supplied(self):
        result = scaffold(self.root / "api-scope", "sample", "api", state("api"), self.documents)
        self.assertFalse((result / "docs/onboarding/LANDING-REVIEW.md").exists())
        review = "Selected landing direction A; mobile motion review pending."
        (self.documents / "LANDING-REVIEW.md").write_text(review)
        result = scaffold(self.root / "landing", "sample", "web", state("web"), self.documents)
        self.assertEqual((result / "docs/onboarding/LANDING-REVIEW.md").read_text(), review)

    def test_brand_is_optional_but_supplied_identity_survives(self):
        result = scaffold(self.root / "api-no-brand", "sample", "api", state("api"), self.documents)
        self.assertFalse((result / "docs/onboarding/BRAND.md").exists())
        brand = "Approved display name: Тиха Хвиля. Preserve the supplied mark."
        (self.documents / "BRAND.md").write_text(brand)
        original = state("web")
        original["brand"] = {"display_name": "Тиха Хвиля", "status": "user_approved"}
        result = scaffold(self.root / "branded", "tykha-khvylia", "web", original, self.documents)
        self.assertEqual((result / "docs/onboarding/BRAND.md").read_text(), brand)
        saved = json.loads((result / "docs/onboarding/state.json").read_text())
        self.assertEqual(saved["brand"], original["brand"])
        self.assertEqual(json.loads((result / "package.json").read_text())["name"], "tykha-khvylia")

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
        scaffold(self.root / "api", "sample", "api", state("api", "not_applicable"), self.documents)

    def test_explicit_override_requires_reason(self):
        original = state("web", "user_override")
        with self.assertRaises(ValueError):
            scaffold(self.root / "bad", "sample", "web", original, self.documents)
        original["design"]["override_reason"] = "User supplied the already approved design"
        scaffold(self.root / "good", "sample", "web", original, self.documents)

    def test_brief_profile_name_validated_before_writing(self):
        invalid = state("api")
        invalid["brief_agreed"] = False
        for name, profile, value in [("sample", "api", invalid), ("sample", "web", state("api")), ("../bad", "api", state("api"))]:
            with self.assertRaises(ValueError):
                scaffold(self.root / "no-write", name, profile, value)
        self.assertFalse((self.root / "no-write").exists())


if __name__ == "__main__":
    unittest.main()
