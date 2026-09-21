"""
make.py — builds the Precision Intraday Trading static site.

Run from src/:  python3 make.py
Writes ../module-NN.html for every module with a content_mNN module present,
plus ../index.html. Auto-skips modules whose content_mNN.py doesn't exist yet.
"""
import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sitegen

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(ROOT, ".."))

MODULES = [
    {"num": "01", "slug": "module-01", "short": "Philosophy",
     "title": "Precision Intraday Trading Philosophy",
     "kicker": "Module 01 of 11",
     "h1": "Module 1 \u2014 Precision Intraday Trading Philosophy",
     "sub": "What precision means, why this is not scalping, the timeframe "
            "hierarchy, and probability-based thinking.",
     "card": "What precision means, why this is not scalping, the timeframe "
             "hierarchy, and probability-based thinking."},
    {"num": "02", "slug": "module-02", "short": "Market Structure",
     "title": "Reading Market Structure",
     "kicker": "Module 02 of 11",
     "h1": "Module 2 \u2014 Reading Market Structure",
     "sub": "Swings, HH/HL/LH/LL, BOS, MSS, and displacement \u2014 how to "
            "read structure on 4H, 1H and 15M.",
     "card": "Swings, HH/HL/LH/LL, BOS, MSS, and displacement \u2014 how to "
             "read structure on 4H, 1H and 15M."},
    {"num": "03", "slug": "module-03", "short": "Support & Resistance",
     "title": "Mapping High-Quality Support & Resistance",
     "kicker": "Module 03 of 11",
     "h1": "Module 3 \u2014 Mapping High-Quality Support & Resistance",
     "sub": "Zones not lines. Supply and demand, fresh versus tested, flip "
            "zones, liquidity around obvious levels, and how false "
            "breakouts happen.",
     "card": "Building real zones from price behaviour, ranking them, and "
             "understanding the liquidity that pools around them."},
    {"num": "04", "slug": "module-04", "short": "The 15M Entry Model",
     "title": "The 15M Price-Action Entry Model",
     "kicker": "Module 04 of 11",
     "h1": "Module 4 \u2014 The 15M Price-Action Entry Model",
     "sub": "The complete entry sequence from 4H bias to filled order, in "
            "both long and short form, with the minimum conditions for "
            "validity, the conditions that strengthen a setup, and the "
            "conditions that force you to stand aside.",
     "card": "The complete entry sequence \u2014 minimum conditions, "
             "strengthening conditions, and invalidation."},
    {"num": "05", "slug": "module-05", "short": "Candlestick Triggers",
     "title": "15M Candlestick Triggers & Price Psychology",
     "kicker": "Module 05 of 11",
     "h1": "Module 5 \u2014 15M Candlestick Triggers & Price Psychology",
     "sub": "What each candle represents, where it is meaningful, and what "
            "invalidates it. Never as isolated signals.",
     "card": "What each candle represents, where it is meaningful, and what "
             "invalidates it. Never as isolated signals."},
    {"num": "06", "slug": "module-06", "short": "Execution Blueprint",
     "title": "Complete Trade Execution Blueprint",
     "kicker": "Module 06 of 11",
     "h1": "Module 6 \u2014 Complete Trade Execution Blueprint",
     "sub": "The full execution process end to end, including the stop and "
            "target rules that govern everything.",
     "card": "The full execution process end to end, including the stop and "
             "target rules that govern everything."},
    {"num": "07", "slug": "module-07", "short": "Trade Management",
     "title": "Fast Intraday Trade Management",
     "kicker": "Module 07 of 11",
     "h1": "Module 7 \u2014 Fast Intraday Trade Management",
     "sub": "Managing a live position without turning the system into "
            "scalping. Never manage by the clock.",
     "card": "Managing a live position without turning the system into "
             "scalping. Never manage by the clock."},
    {"num": "08", "slug": "module-08", "short": "When NOT to Trade",
     "title": "When Not to Trade",
     "kicker": "Module 08 of 11",
     "h1": "Module 8 \u2014 When Not to Trade",
     "sub": "The conditions that make standing aside correct, and the "
            "psychology that makes it hard.",
     "card": "The conditions that make standing aside correct, and the "
             "psychology that makes it hard."},
    {"num": "09", "slug": "module-09", "short": "Risk Management",
     "title": "Prop-Firm Risk Management",
     "kicker": "Module 09 of 11",
     "h1": "Module 9 \u2014 Prop-Firm Risk Management",
     "sub": "Sizing maths, loss limits, correlation exposure, and capital "
            "preservation under prop-firm constraints.",
     "card": "Sizing maths, loss limits, correlation exposure, and capital "
             "preservation under prop-firm constraints."},
    {"num": "10", "slug": "module-10", "short": "Complete Trades",
     "title": "Complete Hypothetical Trades",
     "kicker": "Module 10 of 11",
     "h1": "Module 10 \u2014 Complete Hypothetical Trades",
     "sub": "Two full worked trades from environment to exit, including "
            "what would have invalidated each.",
     "card": "Two full worked trades from environment to exit, including "
             "what would have invalidated each."},
    {"num": "11", "slug": "module-11", "short": "The Rulebook",
     "title": "Final Precision Intraday Rulebook",
     "kicker": "Module 11 of 11",
     "h1": "Module 11 \u2014 Final Precision Intraday Rulebook",
     "sub": "The complete rulebook, checklists, and the testing and review "
            "protocol.",
     "card": "The complete rulebook, checklists, and the testing and review "
             "protocol."},
]


def index_page():
    modgrid_items = ""
    for m in MODULES:
        modgrid_items += (
            f'<a class="modcard" href="{m["slug"]}.html" data-modkey="{m["slug"]}">'
            f'<span class="tick">\u2713</span><span class="mnum">Module {m["num"]}</span>'
            f'<h3>{m["title"]}</h3><p>{m["card"]}</p></a>'
        )

    body = f"""
<section class="hero">
<h1>Elite Precision Intraday Trading</h1>
<p class="lede">A complete eleven-module course in price action, market
structure, liquidity and structural risk management. No indicators, no
signals, no scalping \u2014 a disciplined framework for reading the 4-hour
environment, locating opportunity on the 1-hour, and executing on the
15-minute chart.</p>
<div class="pills">
<span class="pill">Pure price action</span>
<span class="pill">Market structure</span>
<span class="pill">Supply &amp; demand</span>
<span class="pill">Liquidity &amp; sweeps</span>
<span class="pill">BOS \u00b7 MSS \u00b7 Displacement</span>
<span class="pill">Structural risk management</span>
<span class="pill no">No indicators</span>
<span class="pill no">No scalping</span>
</div>
<p style="margin-top:30px"><a class="startbtn" href="module-01.html">Start
Module 1 \u2192</a><button class="resetbtn" id="resetprog">Reset
progress</button></p>
</section>

<div class="notice">
<h4>How to use this course</h4>
<p>Work through the modules in order. Each one builds on the last, and several
carry practical exercises whose output is used in the next module.</p>
<p>Throughout you will find <strong>check-your-understanding questions</strong>.
Click any option and you get a written response to <em>that specific
choice</em> \u2014 why it fails, or why it works \u2014 plus the full explanation of the
correct answer. There are no wrong turns; every option teaches something.</p>
<p>Your progress is saved in this browser. Completed modules show a green
tick.</p>
</div>

<h2><span class="num">Contents</span>The eleven modules</h2>
<div class="modgrid">{modgrid_items}</div>

<h2><span class="num">Before you begin</span>What this course is, and is not</h2>
<div class="split">
<div class="half good"><h5>What it is</h5><p>A structural framework for
intraday decision-making. It teaches you where to look, what constitutes
evidence, where risk is defined, and \u2014 most importantly \u2014 when to do
nothing.</p></div>
<div class="half bad"><h5>What it is not</h5><p>A signal service, a set of
guaranteed setups, or a promise of profitability. No method removes
uncertainty. This one aims to make your uncertainty measurable and your risk
defined.</p></div>
</div>
<p>The language throughout is deliberately probabilistic. You will not read
\u201cthis always works.\u201d You will read \u201chigher-probability,\u201d \u201cvalid setup,\u201d
\u201cfavourable conditions.\u201d That is not hedging \u2014 certainty language causes
oversizing and refusal to exit, and the vocabulary shapes the behaviour.</p>
"""
    return sitegen.page(
        slug="index",
        title="Precision Intraday Trading \u2014 Price Action & Structure System",
        kicker="", h1="", sub="",
        body_html=body,
        is_index=True,
        modlabel="11-module course",
    )


def build():
    toc = [{"slug": m["slug"], "num": m["num"], "short": m["short"]} for m in MODULES]
    sitegen.set_toc(toc)

    built = 0
    for i, m in enumerate(MODULES):
        modname = f"content_{m['slug'].replace('module-', 'm').lstrip('0') or 'm0'}"
        # normalise: module-04 -> content_m4 ; but we used content_m1/m2/m3 previously
        num_int = int(m["num"])
        modname = f"content_m{num_int}"
        path = os.path.join(ROOT, f"{modname}.py")
        if not os.path.exists(path):
            print(f"\u2026 module-{m['num']} \u2014 content module not written yet, skipping")
            continue

        mod = importlib.import_module(modname)
        importlib.reload(mod)
        body_html = mod.build()

        prev = None
        nxt = None
        if i > 0:
            p = MODULES[i - 1]
            prev = {"slug": p["slug"], "title": f"Module {p['num']} \u2014 {p['short']}"}
        if i < len(MODULES) - 1:
            n = MODULES[i + 1]
            nxt = {"slug": n["slug"], "title": f"Module {n['num']} \u2014 {n['short']}"}

        html = sitegen.page(
            slug=m["slug"],
            title=f"Module {m['num']} \u2014 {m['title']}",
            kicker=m["kicker"],
            h1=m["h1"],
            sub=m["sub"],
            body_html=body_html,
            prev=prev,
            nxt=nxt,
            is_index=False,
        )
        out_path = os.path.join(OUT, f"{m['slug']}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        size_kb = os.path.getsize(out_path) / 1024
        print(f"\u2713 module-{m['num']} \u2014 {out_path}  ({size_kb:.0f} KB)")
        built += 1

    idx_html = index_page()
    idx_path = os.path.join(OUT, "index.html")
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(idx_html)
    print(f"\u2713 index \u2014 {idx_path}")
    print(f"Built {built} module pages + index")


if __name__ == "__main__":
    build()
