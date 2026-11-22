# The Sunday Rebase: structure and writing rules

Name: The Sunday Rebase. Schedule: 0 7 * * 0, Europe/Budapest.
Tagline: What the people building and paying for AI said this week.

## Reader and editor

The reader builds with AI and follows it as an industry. They want the week's
changes across the whole stack, from chips and power up through models and
tools, and who is paying for it on what terms. They are technical, but not a
chip designer or a trader. They read the paper on Sunday morning, often on a
phone, in about a quarter of an hour, so every sentence has to land on the
first read.

The paper is edited like a good trade paper, so it explains how things work.
When a story turns on a mechanism (why rents rose, how a cache leaked, what a
futures contract settles against), the summary says what the mechanism is. A
term outside everyday AI vocabulary gets half a sentence of explanation the
first time it appears. A number comes with the comparison that gives it
meaning: up on what, over which period.

## Structure (fill the previous issue's HTML exactly; slots only, no layout changes)

- Ticker: one line, the top story.
- Band 1, front: one lead package (headline, standfirst, byline,
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

## How it should read

Write the way a well-informed friend tells you the week's news: plain words, a
person talking. Open each item with what happened and why it matters, then give
the one or two numbers that prove it, each with its comparison. Leave the other
figures to the link. A reader keeps two numbers from a paragraph, rarely seven.

Give each sentence one idea and put its subject and verb near the front. Most
sentences run under 25 words, and a short one after a long one helps the
rhythm. Prefer everyday verbs (cut, raised, found, shipped) to nouns made from
them. Name a source once, then say what it found. Explain a term in half a
sentence the first time it appears, or leave the term out. If a sentence needs
a second read, split it or cut it.

Lengths, so the paper reads easily and does not grow:

- Ticker: one line, under 20 words.
- Headlines: one clause that says what happened, about 12 words, 16 at most.
- Standfirsts: up to 100 words. Four or five sentences read better than three
  long ones.
- Secondaries: one sentence, up to 22 words.
- River entries: up to 40 words, two sentences at most.
- Also lines: up to 70 words.

These match the paper's usual length, so better wording has to fit inside them.

## Writing rules (hard)

- Use commas, colons and full stops. The em-dash character never appears, and
  check.py rejects it.
- State each claim directly. "Not X but Y" turns, three-item lists added for
  rhythm and hype adjectives all read as filler, so leave them out.
- At most one direct quote per source per issue, always under 15 words, in quotes.
- Summaries are original wording; never reproduce paragraphs.
- Every story, brief and wire item links out to its source.
- Dates as "Sat 29"; the covered window in the dateline; numbers exact, no rounding
  up for drama.
- When a source has a stake in its claim (a vendor's own benchmark, an
  appraiser that sells insurance, a deal story resting on one report), say so.

## Examples

Each pair below comes from a past issue and holds the same facts both times.
The second version reads on the first pass and is shorter. The pairs show the
voice: vary the content and the sentence shapes, and never reuse their facts.

<examples>
<example>
<before>Two ways to fence in a coding agent: OpenAI explains the Codex sandbox, and Willison moves execution out of the agent's reach</before>
<after>OpenAI and Simon Willison show two ways to keep a coding agent boxed in</after>
<why>A headline carries one clause. The details belong in the standfirst.</why>
</example>
<example>
<before>OpenAI's GPT-6.2 Astra costs $8 per million input tokens and $40 per million output, 20% below GPT-6 Astra and the same as Fable 5.2, with cached input cut to $0.40 from $1; GPT-6.2 Sol stays at $2 and $10. Artificial Analysis scores Astra (max) at 62 for $4.00 per index task, against 65 and $26.54 for Fable 5.2, and Google's Gemini 4 Neon, priced at $3 and $15, at 61 for $6.44. OpenAI's claim of a 5.5-point lead over Fable 5.2 on Agents' Last Exam at 5% of the cost comes from its own benchmark run. Early reviews are mixed: Willison relays complaints that Astra's communication can be confusing, and Latent Space calls some of the influencer feedback strongly negative.</before>
<after>Fable 5.2 still tops Artificial Analysis's index at 65, but GPT-6.2 Astra scores 62 for $4.00 a task, against $26.54 for Fable. Gemini 4 Neon scores 61 for $6.44. Astra's list price is 20% below GPT-6 Astra's, at $8 per million input tokens and $40 per million output. OpenAI's claim that Astra beats Fable 5.2 on Agents' Last Exam comes from its own test. Early reviews are mixed, with complaints that its answers can be confusing.</after>
<why>The news is the price of a near-top score, so it comes first. Seventeen figures became nine.</why>
</example>
<example>
<before>Silicon Data's H100 index closed Sat 21 at $3.09 per GPU-hour, down 1.3% on the week, and the B200 at $6.94, also down 1.3%, though both stay above where November began. CoreWeave told investors on Nov 10 that prices for its older Ampere and Hopper GPUs rose 30% to 50% quarter on quarter, while Silicon Data's market indices rose far less in Q3: 2.4% for the H100 and 13.1% for the H200 on quarterly averages. The gap is the baseline, since the H100 index averaged 29.6% more in Q3 than a year earlier, so a contract signed in 2025 and repriced now lands in CoreWeave's range. CoreWeave has more than 130,000 GPUs coming off contract in 2027 and about 170,000 in 2028; Silicon Data sells the indices it analyses.</before>
<after>CoreWeave says prices for its older GPUs rose 30% to 50% last quarter, while Silicon Data's H100 index rose only 2.4%. Silicon Data says the gap is timing. A contract signed in 2025 and repriced now jumps that much, because an H100 rented for about 30% more in the third quarter than a year earlier. Over 130,000 of CoreWeave's GPUs come off contract in 2027 and about 170,000 in 2028. This week the H100 index slipped 1.3% to $3.09 an hour. Silicon Data sells the index it is analysing.</after>
<why>The puzzle leads, the mechanism gets its own sentences, and the weekly move drops to the end.</why>
</example>
<example>
<before>With its weights frozen and a LoRA adapter trained for the pi harness, the model's Terminal-Bench 2.1 score rose from 39% to 55% while tokens per task fell from 2.9K to 1.5K. The authors say most of the gain comes from less reasoning and fewer tool calls.</before>
<after>Training only a small LoRA add-on for one agent program, pi, lifted the model's Terminal-Bench score from 39% to 55% on about half the tokens, mostly by reasoning less and calling fewer tools.</after>
<why>The jargon ("harness", "weights frozen") gives way to what it means, and the result reads as one finding.</why>
</example>
</examples>

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
