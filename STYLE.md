# The Sunday Rebase: structure and writing rules

Name: The Sunday Rebase. Schedule: 0 7 * * 0, Europe/Budapest.
Tagline: What the people building AI said this week.

## Structure (fill the previous issue's HTML exactly; slots only, no layout changes)

- Ticker: one line, the top story.
- Band 1, front: one lead package (headline, standfirst of 2-4 sentences, byline,
  3-5 related links with source domains) plus three secondaries (one per topic,
  one sentence each) and four figures of the week.
- Band 2: Models, Agents & tooling, Security as three columns. Each section:
  one lead package (headline, standfirst, 2-4 related links), up to three river
  entries (linked headline, one line, meta), one trailing Also line.
- Band 3: Money & compute (may carry one data table) beside Opinion
  (3-5 columns, author first).
- Band 4: Audio (0-1 episode), Back pages (2-3 worth re-reading), And finally
  (one light item).
- Wire: every kept item, grouped by day, newest first, collapsed by default.
- Colophon: how it was made, the sources table with kept counts, quiet sources,
  the keys line, and the footer with the cron entry.
- At most two data tables per issue. A leaderboard or spend table only when the
  numbers changed.

## Writing rules (hard)

- No em-dash characters anywhere.
- No "not X but Y" constructions, no padded triplets, no hype adjectives.
- Standfirsts up to 4 short sentences; everything else at most 2.
- At most one direct quote per source per issue, always under 15 words, in quotes.
- Summaries are original wording; never reproduce paragraphs.
- Every story, brief and wire item links out to its source.
- Dates as "Sat 29"; the covered window in the dateline; numbers exact, no rounding
  up for drama.

## Selection rules

- Practitioners over press; primary sources over aggregators.
- A lab announcement earns a story only if it changes what a builder can do;
  regional expansion, education programmes and hiring posts are filtered and the
  filtered count noted in the colophon.
- Duplicates across sources collapse into one package; the extra sources become
  related links.
- Window: since the previous issue date, minus anything already linked there.
- If a claim cannot be verified from the fetched material, the item is dropped.
  Nothing is invented. Ever.
