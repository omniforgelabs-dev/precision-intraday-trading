"""
figs_m11.py — Module 11 figures: The Final Rulebook.
Run: python3 figs_m11.py   (writes into ../images/)
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import chartlib as cl

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "images")
os.makedirs(OUT, exist_ok=True)


def path(name):
    return os.path.join(OUT, name)


# ---------------------------------------------------------------------------
# 1. Core principles — the non-negotiables
# ---------------------------------------------------------------------------
def f_core_principles():
    fig, ax = cl.blank_canvas((13.8, 9.2),
        "Figure 11.1 — Six Non-Negotiable Core Principles",
        "Every rule in this module is a specific application of one of these six statements. When a rule is unclear in the moment, return here first.")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    principles = [
        ("1", "Direction is set on the 4H, refined on the 1H,\nexecuted on the 15M — never the reverse", cl.BLUE),
        ("2", "A completed 15M candle close is the only\nform of confirmation this system accepts", cl.CYAN),
        ("3", "Stops and targets are structural, read from\nprice — never arbitrary distances or manufactured", cl.UP),
        ("4", "No trade clears the sequence below a 1:2\nreward-to-risk ratio, without exception", cl.ACCENT),
        ("5", "Position size is solved backward from a fixed\nrisk percentage and the stop distance \u2014\nnever chosen first", cl.PURP),
        ("6", "Standing aside is a valid, frequent, and often\ncorrect outcome of running the sequence", cl.PINK),
    ]
    cols = 2
    bw, bh = 44, 26
    gx, gy = 4, 4
    for i, (num, text, col) in enumerate(principles):
        r, c = divmod(i, cols)
        x0 = 4 + c * (bw + gx)
        y0 = 82 - r * (bh + gy)
        ax.add_patch(mpatches.FancyBboxPatch((x0, y0 - bh), bw, bh, boxstyle="round,pad=0.6,rounding_size=2.5",
            facecolor="#131a29", edgecolor=col, lw=1.6, zorder=2))
        ax.text(x0 + 3, y0 - 4, num, fontsize=17, color=col, fontweight="bold", zorder=3)
        ax.text(x0 + 11, y0 - 5, text, fontsize=9.4, color=cl.TXT, va="top", ha="left", linespacing=1.55, zorder=3)

    cl.save_flat(fig, path("m11_core_principles.png"), pad=0.35)


# ---------------------------------------------------------------------------
# 2. Full rule map by category
# ---------------------------------------------------------------------------
def f_rule_map():
    fig, ax = cl.blank_canvas((14.2, 9.6),
        "Figure 11.2 — The Complete Rule Map, by Category",
        "Sixteen rule categories, grouped into five functional clusters. Every category is covered in \u00a711.2's tables in the text.")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    groups = [
        (1, 20, cl.BLUE, "DIRECTION\n& CONTEXT", ["Core principles", "4H rules", "1H rules", "15M rules"]),
        (22, 39, cl.CYAN, "STRUCTURE\n& LIQUIDITY", ["S&R rules", "Liquidity rules"]),
        (41, 62, cl.UP, "EXECUTION", ["Entry rules", "Stop rules", "Take-profit rules", "R:R rules", "Management rules"]),
        (64, 81, cl.ACCENT, "PROTECTION", ["No-trade rules", "Risk rules", "News/event rules", "Correlation rules"]),
        (83, 99, cl.PINK, "DISCIPLINE", ["Psychology rules", "Trade-review rules"]),
    ]
    for x0, x1, col, title, items in groups:
        ax.add_patch(mpatches.FancyBboxPatch((x0, 6), x1 - x0, 82, boxstyle="round,pad=0.5,rounding_size=2.2",
            facecolor="#131a29", edgecolor=col, lw=1.6, zorder=2))
        ax.text((x0 + x1) / 2, 84.5, title, ha="center", va="top", fontsize=9.6, color=col,
                 fontweight="bold", zorder=3, linespacing=1.3)
        y = 72
        for it in items:
            ax.text((x0 + x1) / 2, y, "\u2022 " + it, ha="center", va="top", fontsize=8.3, color=cl.TXT, zorder=3)
            y -= 11.5

    ax.text(1, 1.5, "Every category maps to specific, checkable conditions \u2014 none of them require a judgement call made under time pressure.",
            fontsize=9.0, color=cl.MUTED, ha="left", va="bottom")
    cl.save_flat(fig, path("m11_rule_map.png"), pad=0.35)


# ---------------------------------------------------------------------------
# 3. Pre-trade checklist
# ---------------------------------------------------------------------------
def f_pretrade_checklist():
    fig, ax = cl.blank_canvas((12.6, 9.6),
        "Figure 11.3 — Pre-Trade Checklist",
        "Run through top to bottom before every entry. Any single \u2018no\u2019 means stand aside \u2014 the checklist does not get partial credit.")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    items = [
        "4H direction is clear and unconflicted (Gate 1)",
        "1H location qualifies: \u22652 of origin / liquidity / flip present",
        "S&R zone is built from real price behaviour, not a thin line",
        "Zone is not excessively tested \u2014 potency intact (\u00a73.7)",
        "Relevant liquidity has been identified and mapped",
        "No major scheduled news due before or during the trade window",
        "15M has produced a completed, closed confirmation candle",
        "Entry, structural stop, and structural target are all defined",
        "R:R at these levels is \u22651:2, calculated \u2014 not estimated",
        "Position size is calculated from account balance, risk %, and stop distance",
        "This position does not create correlated over-concentration with any open trade",
        "None of the 16 stand-aside conditions (Module 8, Fig 8.1) are present",
        "I am taking this size because the checklist passed \u2014 not to chase or to recover a loss",
    ]
    y = 84
    step = 76.0 / (len(items) - 1)
    for it in items:
        ax.add_patch(mpatches.Rectangle((2, y - 2.6), 3.4, 3.4, facecolor="none", edgecolor=cl.UP, lw=1.6, zorder=3))
        ax.text(7.5, y, it, fontsize=9.3, color=cl.TXT, ha="left", va="center", zorder=3)
        y -= step

    cl.save_flat(fig, path("m11_pretrade_checklist.png"), pad=0.35)


# ---------------------------------------------------------------------------
# 4. Post-trade review checklist
# ---------------------------------------------------------------------------
def f_posttrade_checklist():
    fig, ax = cl.blank_canvas((12.6, 9.6),
        "Figure 11.4 — Post-Trade Review Checklist",
        "Complete for every closed trade, win or loss, before the next one is taken. This is where recurring mistakes get caught.")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    items = [
        "Entry, stop, target, R:R, and size were all recorded before the trade closed",
        "Was every pre-trade checklist item genuinely satisfied, or was one skipped?",
        "Did management follow the five-question loop (Module 7, \u00a77.2), or was there a deviation?",
        "If stopped out: did the structural invalidation actually occur, or was the stop hit on noise?",
        "If target reached: was the exit at the planned level, or moved for any reason?",
        "If closed early: was there a genuine reversal signal, or was it impatience or fear?",
        "Was this a strategy failure, an execution failure, or a correctly-priced loss? (\u00a711.5)",
        "Is this trade part of a recurring pattern in the journal, or an isolated event?",
        "What, if anything, will be done differently on the next qualifying setup?",
    ]
    y = 82
    step = 70.0 / (len(items) - 1)
    for it in items:
        ax.add_patch(mpatches.Rectangle((2, y - 2.6), 3.4, 3.4, facecolor="none", edgecolor=cl.CYAN, lw=1.6, zorder=3))
        ax.text(7.5, y, it, fontsize=9.1, color=cl.TXT, ha="left", va="center", zorder=3)
        y -= step

    ax.text(2, 4, "A completed review takes minutes. Skipping it is how the same mistake repeats for months unnoticed.",
            fontsize=9.0, color=cl.MUTED, ha="left", va="bottom")
    cl.save_flat(fig, path("m11_posttrade_checklist.png"), pad=0.35)


# ---------------------------------------------------------------------------
# 5. Testing and deployment pipeline
# ---------------------------------------------------------------------------
def f_testing_pipeline():
    fig, ax = cl.blank_canvas((13.8, 8.0),
        "Figure 11.5 — Backtesting \u2192 Forward Testing \u2192 Demo \u2192 Live, With Journaling Throughout",
        "Each stage exists to catch a different category of problem before it costs real capital. None of them may be skipped to reach live trading faster.")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    stages = [
        ("BACKTEST", cl.BLUE, "Manually review historical charts,\napplying the full sequence with\nhindsight excluded from the decision.\nTests whether the rules produce\nqualifying setups often enough to matter."),
        ("FORWARD TEST", cl.CYAN, "Apply the sequence to live,\nunfolding price with no capital\nat risk. Tests whether the rules\ncan be followed in real time,\nwithout hindsight."),
        ("DEMO EXECUTION", cl.UP, "Place real orders on a demo\naccount at real position sizes.\nTests execution mechanics,\nplatform behaviour, and\nemotional response to live P&L swings."),
        ("LIVE", cl.ACCENT, "Trade real capital at the size\ndetermined by \u00a79.1, only after\nthe prior three stages show\nconsistent rule-following,\nnot consistent profit."),
    ]
    bw = 21.5
    for i, (name, col, desc) in enumerate(stages):
        x0 = 2 + i * (bw + 2.3)
        ax.add_patch(mpatches.FancyBboxPatch((x0, 30), bw, 48, boxstyle="round,pad=0.5,rounding_size=2",
            facecolor="#131a29", edgecolor=col, lw=1.7, zorder=3))
        ax.text(x0 + bw / 2, 74, name, ha="center", va="top", fontsize=10.6, color=col, fontweight="bold", zorder=4)
        ax.text(x0 + bw / 2, 65, desc, ha="center", va="top", fontsize=8.3, color=cl.TXT, linespacing=1.5, zorder=4)
        if i < len(stages) - 1:
            ax.annotate("", xy=(x0 + bw + 2.1, 54), xytext=(x0 + bw + 0.3, 54),
                        arrowprops=dict(arrowstyle="-|>", color=cl.MUTED, lw=2.0))

    ax.add_patch(mpatches.FancyBboxPatch((2, 6), 96, 18, boxstyle="round,pad=0.5,rounding_size=2",
        facecolor="#0d1420", edgecolor=cl.PINK, lw=1.5, zorder=2))
    ax.text(50, 21, "JOURNALING runs underneath every stage \u2014 every trade, real or simulated, is logged with entry, stop,",
            ha="center", va="top", fontsize=9.4, color=cl.PINK, fontweight="bold", zorder=4)
    ax.text(50, 13.5, "target, R:R, and the post-trade review (Fig 11.4). Without a journal, none of these stages can be evaluated honestly.",
            ha="center", va="top", fontsize=9.0, color=cl.TXT, zorder=4)

    cl.save_flat(fig, path("m11_testing_pipeline.png"), pad=0.35)


# ---------------------------------------------------------------------------
# 6. Strategy failure vs execution failure
# ---------------------------------------------------------------------------
def f_failure_types():
    fig, ax = cl.blank_canvas((13.8, 8.6),
        "Figure 11.6 — Distinguishing Strategy Failure From Execution Failure",
        "The journal answers this question for every loss. Confusing the two leads to abandoning a sound method, or persisting with a genuinely flawed one.")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    ax.add_patch(mpatches.FancyBboxPatch((3, 44), 44, 42, boxstyle="round,pad=0.7,rounding_size=2.5",
        facecolor="#131a29", edgecolor=cl.DN, lw=1.6, zorder=2))
    ax.text(25, 82.5, "EXECUTION FAILURE", ha="center", va="top", fontsize=12.4, color=cl.DN, fontweight="bold", zorder=3)
    for i, t in enumerate([
        "The rules were not actually followed \u2014\nchecklist skipped, chased entry, moved stop",
        "The written sequence would have produced\na different outcome if it had been followed",
        "Correct response: retrain the specific\ndiscipline that slipped, not the rules themselves",
    ]):
        ax.text(6, 73 - i * 12, "\u2022 " + t, fontsize=9.0, color=cl.TXT, ha="left", va="top", linespacing=1.5, zorder=3)

    ax.add_patch(mpatches.FancyBboxPatch((53, 44), 44, 42, boxstyle="round,pad=0.7,rounding_size=2.5",
        facecolor="#131a29", edgecolor=cl.ACCENT, lw=1.6, zorder=2))
    ax.text(75, 82.5, "STRATEGY FAILURE", ha="center", va="top", fontsize=12.4, color=cl.ACCENT, fontweight="bold", zorder=3)
    for i, t in enumerate([
        "The rules were followed exactly, checklist\npassed, and the trade still lost",
        "This is expected behaviour, not a flaw \u2014\nModule 1's expectancy math assumes real losses",
        "Correct response: nothing changes after\none loss; patterns are judged over many trades",
    ]):
        ax.text(56, 73 - i * 12, "\u2022 " + t, fontsize=9.0, color=cl.TXT, ha="left", va="top", linespacing=1.5, zorder=3)

    ax.add_patch(mpatches.FancyBboxPatch((3, 4), 94, 34, boxstyle="round,pad=0.6,rounding_size=2.2",
        facecolor="#0d1420", edgecolor=cl.CYAN, lw=1.5, zorder=2))
    ax.text(50, 34.5, "The single diagnostic question:", ha="center", va="top", fontsize=10.4, color=cl.CYAN, fontweight="bold", zorder=3)
    ax.text(50, 25.5, "\u201cWas the pre-trade checklist genuinely satisfied and management followed exactly as written?\u201d",
            ha="center", va="top", fontsize=9.6, color=cl.TXT, fontweight="bold", zorder=3)
    ax.text(50, 16.5, "Yes, and it still lost \u2192 strategy-consistent loss, expected and acceptable.", ha="center", va="top",
            fontsize=8.8, color=cl.ACCENT, zorder=3)
    ax.text(50, 10.5, "No, a rule was skipped or bent \u2192 execution failure \u2014 review discipline, not the method.", ha="center", va="top",
            fontsize=8.8, color=cl.DN, zorder=3)

    cl.save_flat(fig, path("m11_failure_types.png"), pad=0.35)


# ---------------------------------------------------------------------------
# 7. Reviewing winners vs reviewing losers
# ---------------------------------------------------------------------------
def f_review_winners_losers():
    fig, ax = cl.blank_canvas((13.8, 8.8),
        "Figure 11.7 — Reviewing Winners and Losers Equally",
        "A journal that only examines losses misses the recurring mistakes hiding inside wins \u2014 including luck disguised as skill.")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    ax.add_patch(mpatches.FancyBboxPatch((3, 38), 44, 48, boxstyle="round,pad=0.7,rounding_size=2.5",
        facecolor="#131a29", edgecolor=cl.UP, lw=1.6, zorder=2))
    ax.text(25, 83, "REVIEWING WINNERS", ha="center", va="top", fontsize=11.8, color=cl.UP, fontweight="bold", zorder=3)
    for i, t in enumerate([
        "Did every checklist item genuinely pass, or\ndid a shortcut happen to work out this time?",
        "Was the R:R at entry really \u22651:2, or was\nthe target manufactured and got lucky?",
        "Was management by the rules, or did an\nundisciplined hold happen to pay off?",
        "A win that breaks the rules teaches\nnothing except that luck exists",
    ]):
        ax.text(6, 74 - i * 10.2, "\u2022 " + t, fontsize=8.7, color=cl.TXT, ha="left", va="top", linespacing=1.5, zorder=3)

    ax.add_patch(mpatches.FancyBboxPatch((53, 38), 44, 48, boxstyle="round,pad=0.7,rounding_size=2.5",
        facecolor="#131a29", edgecolor=cl.DN, lw=1.6, zorder=2))
    ax.text(75, 83, "REVIEWING LOSERS", ha="center", va="top", fontsize=11.8, color=cl.DN, fontweight="bold", zorder=3)
    for i, t in enumerate([
        "Was this a strategy failure or an\nexecution failure? (Fig 11.6)",
        "Does this loss share a specific\ncondition with other recent losses?",
        "Was the stop placed at genuine\ninvalidation, or was it too tight for the setup?",
        "A loss that follows every rule exactly\nis data, not a mistake to fix",
    ]):
        ax.text(56, 74 - i * 10.2, "\u2022 " + t, fontsize=8.7, color=cl.TXT, ha="left", va="top", linespacing=1.5, zorder=3)


    ax.add_patch(mpatches.FancyBboxPatch((3, 4), 94, 30, boxstyle="round,pad=0.6,rounding_size=2.2",
        facecolor="#0d1420", edgecolor=cl.PURP, lw=1.5, zorder=2))
    ax.text(50, 30.5, "IDENTIFYING RECURRING MISTAKES", ha="center", va="top", fontsize=10.2, color=cl.PURP, fontweight="bold", zorder=3)
    ax.text(50, 21.5, "A single loss is noise. The same specific rule violation appearing across three or more journal entries", ha="center", va="top",
            fontsize=8.8, color=cl.TXT, zorder=3)
    ax.text(50, 14.5, "\u2014 chasing, moving stops, oversizing after a loss \u2014 is a pattern, and patterns are what the review process exists to surface.", ha="center", va="top",
            fontsize=8.8, color=cl.TXT, zorder=3)

    cl.save_flat(fig, path("m11_review_winners_losers.png"), pad=0.35)


if __name__ == "__main__":
    f_core_principles()
    f_rule_map()
    f_pretrade_checklist()
    f_posttrade_checklist()
    f_testing_pipeline()
    f_failure_types()
    f_review_winners_losers()
    print("All Module 11 figures written.")
