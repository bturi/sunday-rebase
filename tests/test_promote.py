"""Tests for promote.py, the guard that decides whether a routine push may be
fast-forwarded onto main."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import promote  # noqa: E402


class ParseNameStatus(unittest.TestCase):
    def test_reads_status_and_path_per_line(self):
        text = "A\tissues/2026-09-13.html\nM\tcheck.py\n"
        self.assertEqual(
            promote.parse_name_status(text),
            [("A", "issues/2026-09-13.html"), ("M", "check.py")],
        )

    def test_ignores_blank_lines(self):
        self.assertEqual(promote.parse_name_status("\n\n"), [])


class AddedIssue(unittest.TestCase):
    def test_returns_the_single_new_issue(self):
        changes = [("A", "issues/2026-09-13.html")]
        self.assertEqual(promote.added_issue(changes), "issues/2026-09-13.html")

    def test_returns_none_when_no_issue_was_added(self):
        self.assertIsNone(promote.added_issue([("M", "check.py")]))


class PromotionErrors(unittest.TestCase):
    def test_passes_exactly_one_new_issue(self):
        self.assertEqual(promote.promotion_errors([("A", "issues/2026-09-13.html")]), [])

    def test_flags_no_new_issue(self):
        errors = promote.promotion_errors([])
        self.assertEqual(errors, ["expected exactly one new issue, found 0"])

    def test_flags_two_new_issues(self):
        changes = [("A", "issues/2026-09-13.html"), ("A", "issues/2026-09-14.html")]
        self.assertEqual(promote.promotion_errors(changes), ["expected exactly one new issue, found 2"])

    def test_flags_any_other_change(self):
        changes = [("A", "issues/2026-09-13.html"), ("M", "index.html"), ("D", "STYLE.md")]
        self.assertEqual(
            promote.promotion_errors(changes),
            ["unexpected change: M index.html", "unexpected change: D STYLE.md"],
        )

    def test_flags_added_file_that_is_not_a_dated_issue(self):
        changes = [("A", "issues/draft.html")]
        self.assertEqual(
            promote.promotion_errors(changes),
            ["expected exactly one new issue, found 0", "unexpected change: A issues/draft.html"],
        )

    def test_flags_modified_issue(self):
        changes = [("A", "issues/2026-09-13.html"), ("M", "issues/2026-09-09.html")]
        self.assertEqual(
            promote.promotion_errors(changes),
            ["unexpected change: M issues/2026-09-09.html"],
        )


if __name__ == "__main__":
    unittest.main()
