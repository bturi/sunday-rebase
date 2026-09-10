"""Derive the published site from the issues folder.

Run by the deploy workflow: copies every issue, writes issues/index.json
(the list the in-page issue picker reads), the front-door redirect, the
archive page, and the icons. Nothing here touches the issues themselves.
"""
import html
import json
import re
import shutil
import sys
from pathlib import Path

ISSUE_FILE = re.compile(r"^\d{4}-\d{2}-\d{2}\.html$")
LEAD_HEADLINE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S)
TAG = re.compile(r"<[^>]+>")
ICONS = ("favicon.svg", "favicon.png", "apple-touch-icon.png")
ICON_LINKS = ('<link rel="icon" href="favicon.png" sizes="32x32" type="image/png">'
              '<link rel="icon" href="favicon.svg" type="image/svg+xml">'
              '<link rel="apple-touch-icon" href="apple-touch-icon.png">')


def extract_lead(page):
    """The lead headline as plain text, or an empty string."""
    match = LEAD_HEADLINE.search(page)
    if not match:
        return ""
    return " ".join(html.unescape(TAG.sub("", match.group(1))).split())


def list_issues(issues_dir):
    """Every issue file, oldest first, numbered from one."""
    files = sorted(p for p in issues_dir.iterdir() if ISSUE_FILE.match(p.name))
    return [
        {"n": n, "date": p.stem, "file": p.name, "lead": extract_lead(p.read_text(encoding="utf-8"))}
        for n, p in enumerate(files, 1)
    ]


def manifest(issues):
    return {"issues": list(reversed(issues))}


def index_html(latest):
    """The front door: sends the reader to the newest issue before anything is painted.

    The script runs while the head is parsed, so the browser never draws this
    page; the meta refresh covers readers without script, and the links only
    fade in if neither redirect happened.
    """
    target = f"issues/{latest['file']}"
    return (
        '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<meta name="theme-color" content="#F6F4EE">'
        f"<title>The Sunday Rebase</title>{ICON_LINKS}"
        f'<script>location.replace("{target}")</script>'
        f'<meta http-equiv="refresh" content="0; url={target}">'
        "<style>html{background:#F6F4EE}body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;"
        "font:16px/1.7 system-ui,sans-serif;color:#1C1D2A}a{color:#2B5BD7}"
        "p{opacity:0;animation:show .3s 1.5s forwards}@keyframes show{to{opacity:1}}</style></head>"
        f'<body><p><a href="{target}">Latest issue</a> · <a href="archive.html">Archive</a></p></body></html>\n'
    )


def archive_html(issues):
    rows = "".join(
        f'<li><a href="issues/{i["file"]}">Issue {i["n"]} · {i["date"]}</a>'
        f'<span>{html.escape(i["lead"])}</span></li>'
        for i in reversed(issues)
    )
    return (
        '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        f"<title>The Sunday Rebase · archive</title>{ICON_LINKS}"
        "<style>body{font:16px/1.7 system-ui;max-width:640px;margin:40px auto;padding:0 20px;color:#1C1D2A;background:#F6F4EE}"
        "a{color:#2B5BD7}ul{list-style:none;padding:0}li{padding:10px 0;border-top:1px solid #DAD6CB}"
        "li span{display:block;color:#6B7088;font-size:14px}</style></head>"
        f"<body><h1>The Sunday Rebase</h1><p>Back issues, newest first.</p><ul>{rows}</ul></body></html>\n"
    )


def build(root, out):
    issues = list_issues(root / "issues")
    (out / "issues").mkdir(parents=True, exist_ok=True)
    for issue in issues:
        shutil.copy(root / "issues" / issue["file"], out / "issues" / issue["file"])
    (out / "issues" / "index.json").write_text(json.dumps(manifest(issues), indent=1), encoding="utf-8")
    (out / "index.html").write_text(index_html(issues[-1]), encoding="utf-8")
    (out / "archive.html").write_text(archive_html(issues), encoding="utf-8")
    for icon in ICONS:
        if (root / icon).exists():
            shutil.copy(root / icon, out / icon)


if __name__ == "__main__":
    build(Path(__file__).resolve().parent, Path(sys.argv[1] if len(sys.argv) > 1 else "_site"))
