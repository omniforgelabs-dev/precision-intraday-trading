# Elite Precision Intraday Trading — Price Action & Structure System

A self-contained, offline-first static course website teaching a rules-based,
price-action-only intraday trading methodology across the 4H → 1H → 15M
timeframe hierarchy. No indicators, no scalping, no automated signals.

## What this is

An 11-module course, each module a single self-contained HTML file with
base64-embedded chart images, click-to-reveal quizzes with unique per-option
feedback, and full worked examples for readers who cannot ask a follow-up
question. Built for distribution and for GitHub Pages hosting.

- `index.html` — landing page / table of contents
- `module-01.html` … `module-11.html` — the course modules
- `images/` — chart PNGs referenced by the build (also embedded as base64
  directly into each module's HTML, so the HTML files work completely
  standalone)
- `src/` — the Python build tooling (`chartlib.py`, `sitegen.py`, `make.py`,
  `figs_mNN.py`, `content_mNN.py`)

## Course modules

1. Precision Intraday Trading Philosophy
2. Reading Market Structure
3. Mapping High-Quality Support & Resistance
4. The 15M Price-Action Entry Model
5. 15M Candlestick Triggers & Price Psychology
6. Complete Trade Execution Blueprint
7. Fast Intraday Trade Management
8. When Not to Trade
9. Risk Management
10. Complete Trades (long & short, full worked examples)
11. The Rulebook

## Building from source

```bash
cd src
python3 figs_mNN.py     # regenerate charts for a module into ../images/
python3 make.py         # rebuild every module-NN.html + index.html
```

`make.py` only rebuilds a module if `content_mNN.py` exists in `src/`; it
skips (and leaves untouched) any module whose content module hasn't been
written yet.

## Disclaimer

This course is educational only. All charts are illustrative/synthetic and
do not represent real market data. Nothing in this material constitutes
financial advice, and no trading approach — including the one taught here —
guarantees profit or eliminates risk of loss.
