# Routine prompt: weekly issue of The Sunday Rebase

You are producing this week's issue of The Sunday Rebase, a personal AI weekly
in this repo.

Steps:

1. Read STYLE.md, SOURCES.md and the newest file in issues/. That newest file is
   both the template (copy its HTML structure and CSS exactly) and the dedupe
   state (its linked URLs must not reappear).
2. Fetch every source in SOURCES.md: use the feed URL where given, autodiscover
   the RSS/Atom feed from the site URL otherwise, fetch and diff where marked
   "page". Collect items published since the previous issue's date. Skip
   anything whose URL is already linked in the previous issue.
3. Select and group per STYLE.md. Collapse duplicates into story packages.
   Decide the lead, the section leads, rivers, Also lines, four figures, tables
   if the numbers changed, the And finally item, and the full wire.
4. Fill the template: new content in the same slots. Update the issue number
   (previous plus one), all dates, the read-time estimate, wire counts, the
   colophon source table with kept counts, quiet sources and the filtered count.
5. Self-check before saving, fix and re-check until all pass:
   - zero em-dash characters in the file
   - at most one quote per source, each under 15 words
   - every story and wire item has an outbound link
   - HTML tags balanced, file opens as valid HTML
   - no item asserts anything not present in the fetched material
6. Save as issues/YYYY-MM-DD.html using today's date. Commit it with the
   message "issue N: YYYY-MM-DD" and push. Do not touch index.html or
   archive.html; the deploy workflow generates them from the issues folder.

Failure behaviour: an unreachable or empty source is listed as quiet in the
colophon; never guess its content. If the whole week yields fewer than 8 items,
publish the short issue and say so in the colophon. If pushing fails, retry once,
then stop and leave the working tree committed locally.
