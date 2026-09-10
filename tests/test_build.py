"""Tests for build.py, the deploy step that derives the site from issues/."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import build  # noqa: E402

PAGE = (
    "<!DOCTYPE html><html><head><title>The Sunday Rebase</title></head>"
    '<body><article class="lead"><h1>{lead}</h1></article></body></html>'
)


def make_issue(folder, date, lead):
    (folder / f"{date}.html").write_text(PAGE.format(lead=lead), encoding="utf-8")


class ListIssues(unittest.TestCase):
    def test_numbers_issue_files_oldest_first_from_one(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            make_issue(folder, "2026-09-09", "Second")
            make_issue(folder, "2026-08-30", "First")
            (folder / "notes.txt").write_text("ignored", encoding="utf-8")
            issues = build.list_issues(folder)
            self.assertEqual(
                [(i["n"], i["date"], i["file"], i["lead"]) for i in issues],
                [(1, "2026-08-30", "2026-08-30.html", "First"),
                 (2, "2026-09-09", "2026-09-09.html", "Second")],
            )


class ExtractLead(unittest.TestCase):
    def test_strips_tags_entities_and_whitespace(self):
        page = ('<article class="lead"><h1>Everyone shipped\n  at once. '
                "<em>Fable &amp; Astra</em> split the crown.</h1></article>")
        self.assertEqual(build.extract_lead(page),
                         "Everyone shipped at once. Fable & Astra split the crown.")

    def test_missing_headline_gives_empty_string(self):
        self.assertEqual(build.extract_lead("<p>no headline</p>"), "")


class Manifest(unittest.TestCase):
    def test_lists_issues_newest_first(self):
        issues = [
            {"n": 1, "date": "2026-08-30", "file": "2026-08-30.html", "lead": "a"},
            {"n": 2, "date": "2026-09-09", "file": "2026-09-09.html", "lead": "b"},
        ]
        self.assertEqual([i["n"] for i in build.manifest(issues)["issues"]], [2, 1])


class Build(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "repo"
        (self.root / "issues").mkdir(parents=True)
        make_issue(self.root / "issues", "2026-08-30", "First lead")
        make_issue(self.root / "issues", "2026-09-09", "Second lead")
        (self.root / "favicon.svg").write_text("<svg/>", encoding="utf-8")
        self.out = Path(self.tmp.name) / "_site"
        build.build(self.root, self.out)

    def tearDown(self):
        self.tmp.cleanup()

    def test_copies_every_issue(self):
        self.assertTrue((self.out / "issues" / "2026-08-30.html").exists())
        self.assertTrue((self.out / "issues" / "2026-09-09.html").exists())

    def test_writes_manifest_next_to_the_issues_newest_first(self):
        data = json.loads((self.out / "issues" / "index.json").read_text(encoding="utf-8"))
        self.assertEqual(
            data["issues"],
            [{"n": 2, "date": "2026-09-09", "file": "2026-09-09.html", "lead": "Second lead"},
             {"n": 1, "date": "2026-08-30", "file": "2026-08-30.html", "lead": "First lead"}],
        )

    def test_index_redirects_to_the_newest_issue(self):
        index = (self.out / "index.html").read_text(encoding="utf-8")
        self.assertIn('url=issues/2026-09-09.html', index)
        self.assertIn('href="favicon.svg"', index)

    def test_index_redirects_before_first_paint_and_keeps_a_fallback(self):
        index = (self.out / "index.html").read_text(encoding="utf-8")
        head, body = index.split("<body", 1)
        self.assertIn('location.replace("issues/2026-09-09.html")', head)
        self.assertIn('href="issues/2026-09-09.html"', body)
        self.assertIn('href="archive.html"', body)
        self.assertIn("animation", head)  # fallback links stay invisible until the redirect had its chance

    def test_archive_lists_every_issue_newest_first(self):
        archive = (self.out / "archive.html").read_text(encoding="utf-8")
        newest = archive.index("issues/2026-09-09.html")
        oldest = archive.index("issues/2026-08-30.html")
        self.assertLess(newest, oldest)
        self.assertIn("Second lead", archive)
        self.assertIn('href="favicon.svg"', archive)

    def test_copies_the_icons_that_exist_and_skips_the_rest(self):
        self.assertTrue((self.out / "favicon.svg").exists())
        self.assertFalse((self.out / "favicon.png").exists())


if __name__ == "__main__":
    unittest.main()
