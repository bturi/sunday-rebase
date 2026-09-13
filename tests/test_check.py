"""Tests for check.py, the mechanical checker run on an issue before commit."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import check  # noqa: E402


class FindEmDashes(unittest.TestCase):
    def test_flags_line_with_em_dash(self):
        text = "clean line\nbroken — line\n"
        self.assertEqual(check.find_em_dashes(text), [2])

    def test_passes_text_with_no_em_dash(self):
        self.assertEqual(check.find_em_dashes("all clean, no dashes here\n"), [])


class OverlongQuotes(unittest.TestCase):
    def test_flags_quote_of_15_words_or_more(self):
        long_quote = "<q>" + " ".join(["word"] * 15) + "</q>"
        self.assertEqual(check.overlong_quotes(long_quote), [" ".join(["word"] * 15)])

    def test_allows_quote_under_15_words(self):
        short_quote = "<q>" + " ".join(["word"] * 14) + "</q>"
        self.assertEqual(check.overlong_quotes(short_quote), [])


class TagBalanceErrors(unittest.TestCase):
    def test_flags_unclosed_tag(self):
        errors = check.tag_balance_errors("<article><h3>title</h3>")
        self.assertTrue(any("article" in e for e in errors))

    def test_passes_balanced_html_with_void_tags(self):
        html = '<article><h3>title</h3><br><img src="x.png"><p>ok</p></article>'
        self.assertEqual(check.tag_balance_errors(html), [])

    def test_flags_mismatched_closing_tag(self):
        errors = check.tag_balance_errors("<p><em>text</p></em>")
        self.assertTrue(errors)


class ItemsMissingLinks(unittest.TestCase):
    def test_flags_story_without_outbound_link(self):
        html = '<article data-story><h3>No link here</h3></article>'
        self.assertEqual(check.items_missing_links(html), ["story 1 has no outbound link"])

    def test_passes_story_with_outbound_link(self):
        html = '<article data-story><h3><a href="https://example.com">t</a></h3></article>'
        self.assertEqual(check.items_missing_links(html), [])

    def test_flags_wire_row_without_outbound_link(self):
        html = '<li class="row c-tools" data-cat="tools"><span>no link</span></li>'
        self.assertEqual(check.items_missing_links(html), ["wire row 1 has no outbound link"])


class WireCountMismatches(unittest.TestCase):
    def test_flags_button_count_not_matching_row_count(self):
        html = (
            '<button id="wireToggle">[show 2 items]</button>'
            '<li class="row c-tools"><a href="https://example.com">a</a></li>'
        )
        self.assertEqual(
            check.wire_count_mismatches(html),
            ["wire count says 2, found 1 rows"],
        )

    def test_passes_when_every_claim_matches_row_count(self):
        html = (
            '<button id="wireToggle">[show 1 items]</button>'
            '<li class="row c-tools"><a href="https://example.com">a</a></li>'
            "<script>wireBtn.textContent='[show 1 items]';</script>"
        )
        self.assertEqual(check.wire_count_mismatches(html), [])


class ReusedLinks(unittest.TestCase):
    def test_flags_link_reused_from_previous_issue(self):
        current = '<a href="https://example.com/a">a</a>'
        previous = '<a href="https://example.com/a">a</a>'
        self.assertEqual(check.reused_links(current, previous), ["https://example.com/a"])

    def test_passes_when_no_links_overlap(self):
        current = '<a href="https://example.com/new">a</a>'
        previous = '<a href="https://example.com/old">a</a>'
        self.assertEqual(check.reused_links(current, previous), [])


class PreviousIssuePath(unittest.TestCase):
    def test_finds_the_issue_immediately_before_by_date(self):
        with tempfile.TemporaryDirectory() as tmp:
            issues = Path(tmp)
            (issues / "2026-08-30.html").write_text("old", encoding="utf-8")
            (issues / "2026-09-09.html").write_text("mid", encoding="utf-8")
            current = issues / "2026-09-13.html"
            current.write_text("new", encoding="utf-8")
            self.assertEqual(check.previous_issue_path(current), issues / "2026-09-09.html")

    def test_returns_none_for_the_first_issue(self):
        with tempfile.TemporaryDirectory() as tmp:
            issues = Path(tmp)
            current = issues / "2026-08-30.html"
            current.write_text("new", encoding="utf-8")
            self.assertIsNone(check.previous_issue_path(current))


class TitleErrors(unittest.TestCase):
    def test_flags_title_date_not_matching_filename(self):
        html = "<title>The Sunday Rebase · Issue 3 · 10 September 2026</title>"
        errors = check.title_errors(html, Path("issues/2026-09-13.html"))
        self.assertTrue(any("date" in e for e in errors))

    def test_passes_title_date_matching_filename(self):
        html = "<title>The Sunday Rebase · Issue 3 · 13 September 2026</title>"
        errors = check.title_errors(html, Path("issues/2026-09-13.html"))
        self.assertEqual(errors, [])

    def test_flags_issue_number_not_previous_plus_one(self):
        html = "<title>The Sunday Rebase · Issue 4 · 13 September 2026</title>"
        previous_html = "<title>The Sunday Rebase · Issue 2 · 9 September 2026</title>"
        errors = check.title_errors(html, Path("issues/2026-09-13.html"), previous_html)
        self.assertTrue(any("issue number" in e for e in errors))

    def test_passes_issue_number_that_is_previous_plus_one(self):
        html = "<title>The Sunday Rebase · Issue 3 · 13 September 2026</title>"
        previous_html = "<title>The Sunday Rebase · Issue 2 · 9 September 2026</title>"
        errors = check.title_errors(html, Path("issues/2026-09-13.html"), previous_html)
        self.assertEqual(errors, [])


class CheckIntegration(unittest.TestCase):
    def test_check_collects_errors_from_a_broken_issue(self):
        with tempfile.TemporaryDirectory() as tmp:
            issues = Path(tmp)
            (issues / "2026-09-09.html").write_text(
                "<title>The Sunday Rebase · Issue 2 · 9 September 2026</title>",
                encoding="utf-8",
            )
            broken = issues / "2026-09-13.html"
            broken.write_text(
                "<title>The Sunday Rebase · Issue 3 · 13 September 2026</title>"
                "<p>bad — dash</p>"
                '<article data-story><h3>no link</h3></article>',
                encoding="utf-8",
            )
            errors = check.check(broken)
            self.assertTrue(any("em dash" in e for e in errors))
            self.assertTrue(any("outbound link" in e for e in errors))

    def test_check_passes_a_clean_issue(self):
        with tempfile.TemporaryDirectory() as tmp:
            issues = Path(tmp)
            (issues / "2026-09-09.html").write_text(
                "<title>The Sunday Rebase · Issue 2 · 9 September 2026</title>"
                '<a href="https://example.com/old">old</a>',
                encoding="utf-8",
            )
            clean = issues / "2026-09-13.html"
            clean.write_text(
                "<title>The Sunday Rebase · Issue 3 · 13 September 2026</title>"
                '<article data-story><h3><a href="https://example.com/new">new</a></h3></article>'
                '<button id="wireToggle">[show 1 items]</button>'
                '<li class="row c-tools"><a href="https://example.com/wire">w</a></li>'
                "<script>wireBtn.textContent='[show 1 items]';</script>",
                encoding="utf-8",
            )
            self.assertEqual(check.check(clean), [])


if __name__ == "__main__":
    unittest.main()
