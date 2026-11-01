# The Sunday Rebase: structure and writing rules

Name: The Sunday Rebase. Schedule: 0 7 * * 0, Europe/Budapest.
Tagline: What the people building and paying for AI said this week.

## Reader and editor

The reader builds with AI and follows it as an industry. They want the week's
changes across the whole stack, from chips and power up through models and
tools, and who is paying for it on what terms. They are technical, but not a
chip designer or a trader.

The paper is edited like a good trade paper, so it explains how things work.
When a story turns on a mechanism (why rents rose, how a cache leaked, what a
futures contract settles against), the summary says what the mechanism is. A
term outside everyday AI vocabulary gets half a sentence of explanation the
first time it appears. A number comes with the comparison that gives it
meaning: up on what, over which period.

## Structure (fill the previous issue's HTML exactly; slots only, no layout changes)

- Ticker: one line, the top story.
- Band 1, front: one lead package (headline, standfirst of 2-4 sentences, byline,
  3-5 related links with source domains) plus three secondaries (from three
  different sections, one sentence each) and four figures of the week. When
  Compute or Money has a story, at least one secondary or figure comes from it.
- Band 2: Models & research, Agents & tooling, Security as three columns.
- Band 3: Compute, Money and Opinion as three columns.
- Each Band 2 and Band 3 section except Opinion: one lead package (headline,
  standfirst, 2-4 related links), up to three river entries (linked headline,
  one line, meta), one trailing Also line. Opinion: 3-5 columns, author first.
  - Models & research: model releases, benchmarks, papers, training methods
    and algorithms.
  - Compute: chips, memory, networking, data centres, power, and the engines
    that train and serve models (vLLM, SGLang, PyTorch, kernels).
  - Money: capex, compute prices and markets, AI debt and deals, revenue and
    pricing.
- Band 4: Audio (0-1 episode), Back pages (2-3 worth re-reading), And finally
  (one light item).
- Wire: every kept item, grouped by day, newest first, collapsed by default.
- Colophon: how it was made, the sources table with kept counts, quiet,
  overdue and unreachable sources, the keys line, and the footer with the
  cron entry.
- At most two data tables per issue: the leaderboard in Models and GPU rental
  prices in Money, each only when the numbers changed. The price table gives
  the price, the week's change and the change since the start of the month,
  and its caption states the compute futures status, so the next issue has a
  baseline to compare against.

## Writing rules (hard)

- No em-dash characters anywhere.
- No "not X but Y" constructions, no padded triplets, no hype adjectives.
- Standfirsts up to 4 short sentences; everything else at most 2.
- At most one direct quote per source per issue, always under 15 words, in quotes.
- Summaries are original wording; never reproduce paragraphs.
- Every story, brief and wire item links out to its source.
- Dates as "Sat 29"; the covered window in the dateline; numbers exact, no rounding
  up for drama.
- When a source has a stake in its claim (a vendor's own benchmark, an
  appraiser that sells insurance, a deal story resting on one report), say so.

## Selection rules

- Practitioners over press; primary sources over aggregators.
- A lab announcement earns a story only if it changes what a builder can do;
  regional expansion, education programmes and hiring posts are filtered and the
  filtered count noted in the colophon.
- A Compute or Money item earns a story if it changes the cost, supply or
  financing of compute: prices, capacity, power, memory, debt, capex, contracts.
  A bare funding round or a hire goes to the wire.
- Duplicates across sources collapse into one package; the extra sources become
  related links.
- Window: since the previous issue date, minus anything already linked there.
- If a claim cannot be verified from the fetched material, the item is dropped.
  Nothing is invented. Ever.
