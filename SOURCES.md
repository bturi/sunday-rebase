# Sources

Every line gives a URL, how to read it and how often the source usually posts.
"feed" means read that RSS/Atom URL. "page" means fetch the page and compare it
with what the newest issue already printed. "autodiscover" means find the feed
from the site URL. New entries always name the feed or page explicitly: sites
move, and autodiscovery kept SemiAnalysis on a feed that froze in September
2025. Poll everything, then select per STYLE.md.

Cadence words: daily, several a week, weekly, fortnightly, monthly, rare,
event. A source silent within its usual gap is quiet. One silent for more than
four times its gap is overdue, which usually means a broken entry.

## Tier 1: practitioners (the core)
- https://simonwillison.net/               autodiscover · daily · the backbone
- https://lucumr.pocoo.org/                autodiscover · fortnightly · Armin Ronacher
- https://thezvi.substack.com/             autodiscover · several a week · Zvi, AI #N roundups
- https://jack-clark.net/                  autodiscover · weekly · Import AI
- https://www.interconnects.ai/            autodiscover · weekly · Nathan Lambert
- https://www.oneusefulthing.org/          autodiscover · fortnightly · Ethan Mollick
- https://magazine.sebastianraschka.com/   autodiscover · monthly · Ahead of AI
- https://www.latent.space/                autodiscover · several a week · swyx and Alessio
- https://hamel.dev/                       autodiscover · monthly · evals
- https://eugeneyan.com/                   autodiscover · monthly · production ML
- https://www.dbreunig.com/                autodiscover · fortnightly · Drew Breunig

## Labs and trackers
- https://openai.com/news/rss.xml          feed · daily
- https://www.anthropic.com/news           page · several a week · no official RSS: fetch and diff
- https://deepmind.google/discover/blog/   autodiscover · weekly
- https://huggingface.co/blog/feed.xml     feed · daily
- https://artificialanalysis.ai/leaderboards/models   page · weekly · for the index table

## Chips and systems
- https://newsletter.semianalysis.com/feed   feed · several a week · SemiAnalysis: chips, data centres, power. Mostly paid; summarise the free opening. If the feed fails, read the page https://newsletter.semianalysis.com/archive
- https://chipsandcheese.com/feed          feed · weekly · measured chip and memory architecture; keep what bears on AI hardware
- https://www.viksnewsletter.com/feed      feed · several a week · Vik's Newsletter: interconnect, optics, HBM, power. If the feed fails, read the page https://www.viksnewsletter.com/archive
- https://semiengineering.com/feed         feed · daily · Semiconductor Engineering. Start with Friday's Chip Industry Week In Review; skip posts marked SPONSOR BLOG

## Data centres and power
- https://www.latitudemedia.com/feed/      feed · daily · Latitude Media: data-centre power, grid, onsite generation
- https://www.utilitydive.com/feeds/news/  feed · daily · Utility Dive: keep data-centre, large-load, transmission and generation-deal items
- https://www.powermag.com/category/data-centers/   page · several a week · POWER: plant-level detail and federal loans
- https://epoch.ai/data/data-centers?view=table   page · weekly · Epoch AI's data-centre tracker: compare site count and total GW with the newest issue
- https://epoch.ai/latest                  page · several a week · Epoch AI research and data insights; keep what fits a section

## Engines and research
- https://vllm.ai/blog/rss.xml             feed · several a week · vLLM. Fold "Day 0 support" posts into one line
- https://lmsys.org/                       page · weekly · LMSYS: SGLang and Miles. Shows only the three newest posts
- https://www.sglang.io/blog               page · weekly · SGLang project blog
- https://developer.nvidia.com/blog/tag/inference-performance   page · weekly · NVIDIA's inference work (TensorRT, Dynamo); benchmarks are vendor claims
- https://huggingface.co/api/daily_papers?week={ISO week of the covered week, e.g. 2026-W44}&limit=100   page · weekly · papers ranked by upvotes; take the top few
- https://thinkingmachines.ai/blog         page · rare · Thinking Machines
- https://pypi.org/rss/project/vllm/releases.xml   feed · fortnightly · same pattern for sglang, torch and triton. Stable versions only, one line in Compute

## Compute markets and money
- https://www.silicondata.com/products/silicon-index/h100   page · daily · Silicon Data's H100 rental index, which CME plans to settle futures on. Compute the week's change from the daily table: the "(7D)" label has shown the change since the start of the month
- https://www.silicondata.com/products/silicon-index/b200   page · daily · the B200 index, same rule
- https://getdeploying.com/gpu-price-index   page · weekly · median on-demand list prices across providers
- https://www.cmegroup.com/markets/energy/power/compute-futures.html   page · event · CME compute futures; report when the status line changes
- https://www.silicondata.com/blog         page · monthly · index commentary and hedging
- https://platformonomics.com/feed/        feed · weekly · Platformonomics: hyperscaler capex. If the feed fails, read the page https://platformonomics.com/tag/capex/
- https://ramp.com/authors/ara-kharazian   page · monthly · Ramp AI Index: what businesses pay for AI. The list has no dates; open new entries for theirs
- https://www.amcompute.com/blog           page · several a week · American Compute: GPU depreciation, resale, loan risk. It sells residual value insurance; say so. Skip how-to posts

## Audio
- https://www.dwarkesh.com/                autodiscover · fortnightly · include only with a transcript or detailed notes

## Rules of the road
- General press (Bloomberg, CNBC, FT, Reuters) is not polled; it enters when a
  listed source relays it. The trade press listed above is the exception,
  because chip and power news rarely reaches practitioner blogs.
- X and Discord are not polled.
- Quiet, overdue and unreachable sources are listed in the colophon.
- Cap: at most 12 kept items from any single source per issue.
