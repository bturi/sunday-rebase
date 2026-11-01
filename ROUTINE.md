# Routine prompt: weekly issue of The Sunday Rebase

You are producing this week's issue of The Sunday Rebase, a personal AI weekly
in this repo.

Steps:

1. Read STYLE.md, SOURCES.md and the newest file in issues/. That newest file is
   both the template (copy its HTML structure and CSS exactly) and the dedupe
   state (its linked URLs must not reappear).
2. Fetch every source in SOURCES.md the way its line says: the feed URL where
   given, the feed autodiscovered from the site URL where marked so, fetch and
   diff where marked "page". Collect items published since the previous
   issue's date, comparing dates in Europe/Budapest time. Skip anything whose
   URL is already linked in the previous issue.
   - Big full-text feeds can be cut off after a few items. If a feed stops
     before the start of the window, read the rest of the week from the
     source's archive or tag page.
   - On a list page without dates, open each new entry and take its date from
     the entry itself.
   - Data pages (price indices, the CME page, the Epoch tracker) have no items.
     Read their current values and compare them with the values the newest
     issue printed. Print the new values in this issue (the price table, the
     Compute Also line) so next week has a baseline.
   - If a feed fails and its line names a fallback page, read the fallback.
3. Select and group per STYLE.md. Collapse duplicates into story packages.
   Decide the lead, the section leads (Compute and Money included), rivers,
   Also lines, four figures, tables if the numbers changed, the And finally
   item, and the full wire.
4. Fill the template: new content in the same slots. Update the issue number
   (previous plus one) in the title, the dateline button and the colophon end
   line, all dates, the read-time estimate, wire counts, the colophon source
   table with kept counts, and the filtered count. In the colophon, list quiet
   sources (silent within their usual gap) in one line, overdue sources
   (silent past four times their gap) with a note that the entry may need
   fixing, and unreachable sources with the URL tried. The issue picker
   behind the dateline button lists issues from issues/index.json, which the
   deploy workflow writes; nothing in the page needs updating for it.
5. Self-check before saving, fix and re-check until all pass:
   - zero em-dash characters in the file
   - at most one quote per source, each under 15 words
   - every story and wire item has an outbound link
   - HTML tags balanced, file opens as valid HTML
   - no item asserts anything not present in the fetched material
6. Save as issues/YYYY-MM-DD.html using today's date and run
   python3 check.py on it; fix and re-run until it prints OK. Commit only that
   one file, with the message "issue N: YYYY-MM-DD", and push to your own
   claude/ branch, which is the default. Do not push to main and do not open
   or merge anything by hand: the promote workflow fast-forwards main and
   deploys as soon as the push is exactly one new issue file and nothing else.
   Do not touch index.html, archive.html or issues/index.json; the deploy
   workflow generates them from the issues folder.

Failure behaviour: an unreachable or empty source is listed in the colophon;
never guess its content. If the whole week yields fewer than 8 items, publish
the short issue and say so in the colophon. If pushing fails, retry once, then
stop and leave the working tree committed locally.
