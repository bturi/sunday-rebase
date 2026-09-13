# The Sunday Rebase

A personal AI weekly that lives entirely in this repo.

- issues/           one HTML file per issue; the newest one is also the template
                    and the dedupe state for the next build
- SOURCES.md        what the routine polls
- STYLE.md          structure slots and writing rules
- ROUTINE.md        the prompt for the Claude Code Routine
- build.py          derives the site from issues/: copies the issues, writes
                    issues/index.json (the list behind the issue picker in
                    the dateline), index.html (redirect to the newest issue),
                    archive.html (back-issue list) and the icons
- tests/            unit tests for build.py, check.py and promote.py:
                    python3 -m unittest discover -s tests
- favicon.svg, favicon.png, apple-touch-icon.png
                    the tab and home-screen icon; the SVG is the source
- .github/workflows/deploy.yml
                    on every push to main: runs the tests, runs build.py,
                    deploys the result to GitHub Pages
- .github/workflows/promote.yml, promote.py
                    on a push to a claude/ branch: if it adds exactly one
                    valid new issue and nothing else, fast-forwards main and
                    dispatches the deploy; a push that does not touch issues/
                    ends with nothing to promote; anything in between fails
                    loudly and waits for a pull request

Flow: Routine pushes a new issue file to its branch -> promote moves it to
main -> the Action deploys -> the paper is at
https://YOURNAME.github.io/REPONAME/ with an archive of every back issue.
No servers, no buckets, no secrets: Pages hosts, the built-in token deploys.

## Setup (once, ~20 minutes)

1. Create a GitHub repo and push this folder. Public is free; Pages on a
   private repo needs a paid GitHub plan.
2. Repo Settings > Pages > Source: GitHub Actions. Then run the
   "Deploy the paper" workflow once from the Actions tab (or just push);
   issue 1 goes live.
   Optional: a custom domain in the same Pages settings (this paper is at
   https://sundayrebase.com). Once the certificate shows as approved, turn
   on "Enforce HTTPS" there, or the old github.io link lands on plain http.
3. In Claude Code on the web (code.claude.com), create a Routine:
   connect this repo, paste ROUTINE.md as the prompt, schedule weekly,
   Sunday 07:00, Europe/Budapest.

Bookmark the Pages URL on your phone. Done.

## Notes

- The routine only ever writes issues/YYYY-MM-DD.html and pushes. It never
  touches index.html, the archive or issues/index.json; the Action derives
  those from the folder, so a half-finished run cannot break the front door.
- Pages caches every file for ten minutes, so right after a deploy the front
  door can still point at the previous issue. Each issue page therefore
  fetches a fresh issues/index.json and, if a newer issue exists, hops to it
  when the reader came through the front door or shows an "Issue N is out"
  line above the ticker otherwise.
- Local preview with a working issue picker: python3 build.py _site, then
  python3 -m http.server --directory _site and open /issues/ in a browser.
- One run per week sits far inside Routine plan limits (5/day on Pro).
- Manual run: open the repo in Claude Code and paste ROUTINE.md.
- Rename the paper later: edit the name lines in STYLE.md and the masthead
  block in the newest issue; the next issue carries it forward.
- If GitHub ever deprecates an action version, bump the @vN pins in
  deploy.yml; nothing else depends on them.
