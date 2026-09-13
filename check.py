"""Mechanical checks run on an issue before commit: dashes, quote length,
tag balance, links, dedupe, wire count, title. See CLAUDE.md and ROUTINE.md.
"""
import argparse
import re
import sys
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

EM_DASH = "—"
VOID_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}
QUOTE_RE = re.compile(r"<q>(.*?)</q>", re.S)
HREF_RE = re.compile(r'<a\b[^>]*\bhref="([^"]+)"')
TAG_RE = re.compile(r"<[^>]+>")
STORY_RE = re.compile(r"<article\b[^>]*\bdata-story\b[^>]*>(.*?)</article>", re.S)
WIRE_ROW_RE = re.compile(r'<li class="row[^"]*"[^>]*>(.*?)</li>', re.S)
WIRE_COUNT_RE = re.compile(r"\[show (\d+) items\]")
TITLE_RE = re.compile(
    r"The Sunday Rebase · Issue (\d+) · (\d{1,2} \w+ \d{4})"
)
MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]


def find_em_dashes(text):
    """1-based line numbers containing an em dash."""
    return [n for n, line in enumerate(text.splitlines(), 1) if EM_DASH in line]


def overlong_quotes(html_text, limit=15):
    """Quote text (tags stripped) for every <q> at or over the word limit."""
    overlong = []
    for raw in QUOTE_RE.findall(html_text):
        plain = " ".join(TAG_RE.sub("", raw).split())
        if len(plain.split()) >= limit:
            overlong.append(plain)
    return overlong


class TagBalanceChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID_TAGS:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1] != tag:
            self.errors.append(f"unexpected closing tag </{tag}>")
        else:
            self.stack.pop()


def tag_balance_errors(html_text):
    checker = TagBalanceChecker()
    checker.feed(html_text)
    errors = list(checker.errors)
    if checker.stack:
        errors.append(f"unclosed tag(s): {', '.join(checker.stack)}")
    return errors


def extract_hrefs(html_text):
    return HREF_RE.findall(html_text)


def extract_external_hrefs(html_text):
    """Outbound source links only: skips same-page anchors and site-relative paths."""
    return [href for href in extract_hrefs(html_text) if href.startswith(("http://", "https://"))]


def items_missing_links(html_text):
    missing = []
    for n, block in enumerate(STORY_RE.findall(html_text), 1):
        if not HREF_RE.search(block):
            missing.append(f"story {n} has no outbound link")
    for n, block in enumerate(WIRE_ROW_RE.findall(html_text), 1):
        if not HREF_RE.search(block):
            missing.append(f"wire row {n} has no outbound link")
    return missing


def wire_count_mismatches(html_text):
    actual = len(WIRE_ROW_RE.findall(html_text))
    claims = [int(m) for m in WIRE_COUNT_RE.findall(html_text)]
    if not claims:
        return ["no wire item count found"]
    return [
        f"wire count says {claim}, found {actual} rows"
        for claim in claims if claim != actual
    ]


def previous_issue_path(current_path):
    """The issue immediately before current_path by date, or None if it is the first."""
    issues_dir = current_path.parent
    earlier = sorted(
        p.stem for p in issues_dir.glob("*.html")
        if re.match(r"^\d{4}-\d{2}-\d{2}$", p.stem) and p.stem < current_path.stem
    )
    if not earlier:
        return None
    return issues_dir / f"{earlier[-1]}.html"


def reused_links(current_html, previous_html):
    reused = set(extract_external_hrefs(current_html)) & set(extract_external_hrefs(previous_html))
    return sorted(reused)


def title_errors(html_text, file_path, previous_html_text=None):
    errors = []
    match = TITLE_RE.search(html_text)
    if not match:
        return ["title does not match the expected 'Issue N · D Month YYYY' format"]

    number, title_date = match.groups()
    filename_date = date.fromisoformat(file_path.stem)
    expected_date = f"{filename_date.day} {MONTHS[filename_date.month - 1]} {filename_date.year}"
    if title_date != expected_date:
        errors.append(f"title date {title_date!r} does not match filename date {expected_date!r}")

    if previous_html_text is not None:
        previous_match = TITLE_RE.search(previous_html_text)
        if previous_match:
            expected_number = int(previous_match.group(1)) + 1
            if int(number) != expected_number:
                errors.append(f"issue number {number} is not previous issue's number plus one ({expected_number})")

    return errors


def check(file_path):
    """All mechanical errors found in the issue at file_path, or an empty list."""
    html_text = file_path.read_text(encoding="utf-8")
    errors = []

    dashes = find_em_dashes(html_text)
    if dashes:
        errors.append(f"em dash found on line(s): {', '.join(map(str, dashes))}")

    for quote in overlong_quotes(html_text):
        errors.append(f"quote is 15 words or more: {quote!r}")

    errors.extend(tag_balance_errors(html_text))
    errors.extend(items_missing_links(html_text))
    errors.extend(wire_count_mismatches(html_text))

    previous_path = previous_issue_path(file_path)
    previous_html_text = previous_path.read_text(encoding="utf-8") if previous_path else None
    if previous_html_text is not None:
        for url in reused_links(html_text, previous_html_text):
            errors.append(f"link already used in the previous issue: {url}")

    errors.extend(title_errors(html_text, file_path, previous_html_text))

    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    args = parser.parse_args(argv)

    errors = check(args.file)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
