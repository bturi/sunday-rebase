# The Sunday Rebase

A personal AI weekly. Every file in `issues/` is one published edition. The
newest one is both the template (copy its HTML skeleton exactly) and the
memory (its links define what "already printed" means). This is not an app:
no build step, no dependencies beyond Python 3 for `check.py`.

## Before writing an issue

1. Read `STYLE.md` (structure, voice, hard rules) and `SOURCES.md` (what to
   poll). They are the single source of truth; do not restate their rules
   here or anywhere else.
2. Read the newest file in `issues/` for the skeleton and the dedupe set.
3. The weekly procedure is `ROUTINE.md`.

## Invariants

- Only ever write `issues/YYYY-MM-DD.html`. Never edit `index.html`,
  `archive.html`, `issues/index.json`, past issues or `.github/`. The deploy
  workflow runs `build.py`, which derives the front door, the archive and
  the issue list behind the dateline's issue picker from the folder.
- Nothing invented. Every fact and every link comes from a page actually
  fetched in this run. A source you could not reach is reported as quiet in
  the colophon, never filled in from memory.
- `python3 check.py issues/<file>` must pass before committing. It enforces
  the mechanical rules (dashes, quote length, tag balance, links, dedupe,
  wire count, title). Fix the issue; do not weaken the checker.
- Commit message: `issue N: YYYY-MM-DD`. Push to `main`.

## Development

Whenever code is written or changed in this repo (`check.py`, the deploy
workflow, any future script), it is done test-driven and clean, no exceptions:

- TDD: write the failing test first, make it pass with the smallest change,
  then refactor. No production code without a test that demanded it. The
  whole suite (`python3 -m unittest discover -s tests`) runs green before
  every commit.
- Clean code: small functions that do one thing, names that say what they
  mean, no duplication, no dead or commented-out code. If a function needs a
  comment to explain what it does, rename or split it instead.
- One focused change per commit. Do not refactor unrelated code on the way.

## Design changes

If asked to change the look, edit the CSS or skeleton of the newest issue
only; the next issue inherits it. Keep the name in its five strings (title,
masthead pre, masthead text, aria-label, colophon end line) so a rename
stays a one-pass job. Keep the issue picker markup in the dateline (the
`issue-menu` span with its button and list); its script fills the list from
`issues/index.json`. The icons live at the repo root: `favicon.svg` is the
source, the two PNGs are rendered from it.

## Voice, in one line

Plain words, a person talking. No consultant jargon, no em-dashes, no
"not X but Y". The full guidance is in `STYLE.md`.
