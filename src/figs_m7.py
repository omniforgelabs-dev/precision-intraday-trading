"""
figs_m7.py — Module 7 figures: Fast Intraday Trade Management.
Run: python3 figs_m7.py   (writes into ../images/)
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
# 1. Management decision tree
# ---------------------------------------------------------------------------
def f_management_tree():
    fig, ax = cl.blank_canvas((13.6, 9.4),
        "Figure 7.1 — The Trade Management Decision Tree",
        "Asked continuously while a trade is open, not on a timer. The same five questions apply whether the trade is 8 minutes old or 80.")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    boxes = [
        ("Has price structurally\ninvalidated the thesis?", 88, cl.DN, "YES \u2192 exit now, regardless of elapsed time or stop distance"),
        ("Is the move still showing\nmomentum in your favour?", 70, cl.ACCENT, "YES \u2192 leave the trade alone; do not tighten out of impatience"),
        ("Has price reached a level that\njustifies partial profit or breakeven?", 52, cl.CYAN, "YES \u2192 apply the specific rule for that level (\u00a77.2\u2013\u00a77.4)"),
        ("Is momentum fading without\nstructural failure yet?", 34, cl.PURP, "MAYBE \u2192 tighten the stop to the newest structure, don't force an exit"),
        ("Has a genuine reversal signal\nappeared against the position?", 16, cl.BLUE, "YES \u2192 exit or reduce; a reversal signal outranks unrealized profit target"),
    ]
    for text, y, col, note in boxes:
        ax.add_patch(mpatches.FancyBboxPatch((4, y - 6), 34, 11, boxstyle="round,pad=0.6",
                     facecolor="#0d1420", edgecolor=col, lw=1.5, zorder=3))
        ax.text(21, y - 0.5, text, ha="center", va="center", fontsize=10.2, color=cl.TXT,
                fontweight="bold", zorder=4)
        ax.text(41, y - 0.5, note, ha="left", va="center", fontsize=9.6, color=col, zorder=4)

    ax.text(4, 4, "None of these five questions reference a clock. \u201cHow long has this been open\u201d is never one of the five.",
            fontsize=9.4, color=cl.MUTED, ha="left", va="bottom")
    cl.save_flat(fig, path("m7_management_tree.png"), pad=0.35)


# ---------------------------------------------------------------------------
# 2. Leave alone vs premature tightening
# ---------------------------------------------------------------------------
def f_leave_alone():
    fig, axes = cl.panel_fig(
        "Figure 7.2 — Leaving a Winning Trade Alone vs Premature Tightening",
        "Same trade, same move. Left: stop stays at the original structural level while the move develops. Right: stop is dragged up on every green candle and gets clipped by a normal pullback.",
        ncols=2, figsize=(15.8, 6.6))

    ax = axes[0]
    shape = cl.seg((6, -0.0008), (5, 0.0038), (4, -0.0012), (6, 0.0046), (4, -0.0010), (5, 0.0052))
    o, h, l, c = cl.series(seed=221, shape=shape, noise=0.00024, wick=0.00026, start=1.0850)
    cl.candles(ax, o, h, l, c)
    entry_i = 5
    entry_lvl = float(c[entry_i])
    stop_lvl = float(min(l[2:6])) - 0.00015
    cl.hline(ax, entry_lvl, cl.BLUE, label=f"entry {entry_lvl:.4f}", n=len(o) - 1, side="right", va="bottom")
    cl.hline(ax, stop_lvl, cl.DN, label=f"stop {stop_lvl:.4f} (unchanged)", n=len(o) - 1, side="right", va="top")
    cl.label_point(ax, 20, h[20], "stop stays put \u2014\nmove is given room\nto develop", cl.UP, dx=-3.4, dy=0.0012, fs=8.4, ha="right", rad=-0.2)
    cl.verdict(ax, "Correct \u2014 momentum intact, no structural reason to tighten yet", cl.UP, yy=0.16)
    cl.clean(ax, sub="Stop stays at structure through two pullbacks; neither broke structure.")
    ax.set_ylim(min(l) - 0.0022, max(h) + 0.0018)

    ax2 = axes[1]
    o2, h2, l2, c2 = o.copy(), h.copy(), l.copy(), c.copy()
    cl.candles(ax2, o2, h2, l2, c2)
    entry_lvl2 = entry_lvl
    # dragged stop follows price up aggressively, tight enough that the second pullback (idx ~19-21) clips it
    dragged_stop = float(min(l2[16:19])) + 0.00020
    cl.hline(ax2, entry_lvl2, cl.BLUE, label=f"entry {entry_lvl2:.4f}", n=len(o2) - 1, side="right", va="bottom")
    cl.hline(ax2, dragged_stop, cl.DN, label=f"stop {dragged_stop:.4f} (dragged up)", n=0, side="left", va="top")
    stop_hit_i = 20
    cl.label_point(ax2, stop_hit_i, l2[stop_hit_i], "normal pullback clips\nthe over-tight stop", cl.DN, dx=1.6, dy=-0.0020, fs=8.4, ha="left", rad=-0.2)
    cl.verdict(ax2, "Premature \u2014 stopped out by ordinary noise, move continues without the trade", cl.DN, yy=0.16)
    cl.clean(ax2, sub="Stop dragged up out of impatience; a routine pullback removes the position.")
    ax2.set_ylim(min(l2) - 0.0022, max(h2) + 0.0018)

    cl.save(fig, path("m7_leave_alone.png"))


# ---------------------------------------------------------------------------
# 3. Breakeven — when justified vs when premature
# ---------------------------------------------------------------------------
def f_breakeven():
    fig, axes = cl.panel_fig(
        "Figure 7.3 — Breakeven: Structural Justification vs Premature Move",
        "Left: price prints a fresh swing beyond entry, so moving the stop to breakeven locks in structure that now exists. Right: breakeven is moved on a small, early wiggle with no new structure to justify it.",
        ncols=2, figsize=(15.8, 6.6))

    ax = axes[0]
    shape = cl.seg((6, -0.0006), (5, 0.0040), (4, -0.0010))
    o, h, l, c = cl.series(seed=231, shape=shape, noise=0.00022, wick=0.00024, start=1.0850)
    cl.candles(ax, o, h, l, c)
    entry_i = 5
    entry_lvl = float(c[entry_i])
    new_swing_low = float(min(l[9:13]))
    cl.hline(ax, entry_lvl, cl.BLUE, label=f"entry/new stop {entry_lvl:.4f}", n=len(o) - 1, side="right", va="bottom")
    cl.label_point(ax, 10, new_swing_low, "new higher-low prints\nabove entry \u2014 structure\nnow supports breakeven", cl.UP, dx=2.4, dy=-0.0016, fs=8.3, ha="left", rad=-0.2)
    cl.verdict(ax, "Justified \u2014 a genuine new swing formed above entry", cl.UP, yy=0.03)
    cl.clean(ax, sub="A fresh higher-low forms above entry before the stop moves \u2014 breakeven reflects real structure.")
    ax.set_ylim(min(l) - 0.0016, max(h) + 0.0014)

    ax2 = axes[1]
    shape2 = cl.seg((6, -0.0006), (2, 0.0010), (3, -0.0004))
    o2, h2, l2, c2 = cl.series(seed=232, shape=shape2, noise=0.00022, wick=0.00024, start=1.0850)
    cl.candles(ax2, o2, h2, l2, c2)
    entry_lvl2 = float(c2[entry_i])
    cl.hline(ax2, entry_lvl2, cl.BLUE, label=f"entry/stop moved here {entry_lvl2:.4f}", n=len(o2) - 1, side="right", va="bottom")
    wiggle_i = 7
    cl.label_point(ax2, wiggle_i, h2[wiggle_i], "small early wiggle \u2014\nno new structure,\njust nerves", cl.DN, dx=-2.0, dy=0.0016, fs=8.3, ha="right", rad=0.2)
    fail_i = 9
    cl.label_point(ax2, fail_i, l2[fail_i], "normal retrace stops\nout a trade that had\nno structural problem", cl.DN, dx=1.2, dy=-0.0016, fs=8.3, ha="left", rad=-0.2)
    cl.verdict(ax2, "Premature \u2014 breakeven moved on a wiggle, not on new structure", cl.DN, yy=0.03)
    cl.clean(ax2, sub="Breakeven moved after a small early bounce with no new swing point \u2014 a normal retrace then stops it out.")
    ax2.set_ylim(min(l2) - 0.0016, max(h2) + 0.0014)

    cl.save(fig, path("m7_breakeven.png"))


# ---------------------------------------------------------------------------
# 4. Partial profit-taking at structure
# ---------------------------------------------------------------------------
def f_partial_profit():
    fig, ax = plt.subplots(figsize=(13.8, 6.8))
    shape = cl.seg((6, -0.0006), (6, 0.0052), (4, -0.0008), (8, 0.0060))
    o, h, l, c = cl.series(seed=241, shape=shape, noise=0.00026, wick=0.00028, start=1.0850)
    cl.candles(ax, o, h, l, c)
    entry_i = 5
    entry_lvl = float(c[entry_i])
    stop_lvl = float(min(l[2:6])) - 0.00015
    interim_structure = float(max(h[8:12]))
    final_target = float(max(h[18:24]))
    cl.hline(ax, entry_lvl, cl.BLUE, label=f"entry {entry_lvl:.4f}", n=0, side="left", va="bottom")
    cl.hline(ax, stop_lvl, cl.DN, label=f"stop {stop_lvl:.4f}", n=0, side="left", va="top")
    cl.hline(ax, interim_structure, cl.ACCENT, label=f"interim structure {interim_structure:.4f} \u2014 partial here", n=len(o) - 1, side="right", va="bottom")
    cl.hline(ax, final_target, cl.UP, label=f"final structural target {final_target:.4f}", n=len(o) - 1, side="right", va="top")
    cl.label_point(ax, 10, interim_structure, "first meaningful\nopposing structure:\ntake partial size off", cl.ACCENT, dx=-2.5, dy=0.0016, fs=8.3, ha="right", rad=0.2)
    cl.verdict(ax, "Partial at genuine interim structure, remainder still targets the original structural level", cl.UP, yy=0.03)
    cl.clean(ax, title="Figure 7.4 — Partial Profit-Taking at Genuine Interim Structure",
             sub="A portion of the position is closed at the first real opposing structure the move reaches on the way to the final target. This is not the same as taking a small, arbitrary profit early.",
             ts=13.4)
    ax.set_ylim(min(l) - 0.0014, max(h) + 0.0018)
    cl.save(fig, path("m7_partial_profit.png"), rect=(0.012, 0.02, 0.99, 0.86))


# ---------------------------------------------------------------------------
# 5. Momentum loss vs structural failure
# ---------------------------------------------------------------------------
def f_momentum_vs_failure():
    fig, axes = cl.panel_fig(
        "Figure 7.5 — Momentum Loss vs Structural Failure",
        "Both show the trade stalling. Only one requires an exit. The difference is whether a structural point the thesis depends on has actually broken.",
        ncols=2, figsize=(15.6, 6.4))

    ax = axes[0]
    shape = cl.seg((6, -0.0006), (5, 0.0038), (10, 0.0004))
    o, h, l, c = cl.series(seed=251, shape=shape, noise=0.00020, wick=0.00022, start=1.0850)
    cl.candles(ax, o, h, l, c)
    entry_i = 5
    entry_lvl = float(c[entry_i])
    last_swing_low = float(min(l[9:14]))
    cl.hline(ax, entry_lvl, cl.BLUE, label=f"entry {entry_lvl:.4f}", n=0, side="left", va="bottom")
    cl.hline(ax, last_swing_low, cl.MUTED, label="last swing low \u2014 still holding", n=0, side="left", va="top")
    cl.label_point(ax, 16, h[16], "candles get smaller,\nprogress stalls \u2014\nbut structure still holds", cl.ACCENT, dx=-3.0, dy=0.0010, fs=8.3, ha="right", rad=-0.2)
    cl.verdict(ax, "Momentum loss only \u2014 tighten the stop, don't exit yet", cl.ACCENT, yy=0.03)
    cl.clean(ax, sub="Momentum fades, but the last swing low the thesis depends on holds.")
    ax.set_ylim(min(l) - 0.0012, max(h) + 0.0018)

    ax2 = axes[1]
    shape2 = cl.seg((6, -0.0006), (5, 0.0038), (5, 0.0002), (4, -0.0040))
    o2, h2, l2, c2 = cl.series(seed=252, shape=shape2, noise=0.00020, wick=0.00022, start=1.0850)
    cl.candles(ax2, o2, h2, l2, c2)
    entry_lvl2 = float(c2[entry_i])
    last_swing_low2 = float(min(l2[9:14]))
    cl.hline(ax2, entry_lvl2, cl.BLUE, label=f"entry {entry_lvl2:.4f}", n=0, side="left", va="bottom")
    cl.hline(ax2, last_swing_low2, cl.DN, label="last swing low \u2014 now broken", n=0, side="left", va="top")
    fail_i = 18
    cl.label_point(ax2, fail_i, c2[fail_i], "15M close breaks\nbelow the swing low\nthe thesis depended on", cl.DN, dx=1.4, dy=-0.0026, fs=8.3, ha="left", rad=-0.2)
    cl.verdict(ax2, "Structural failure \u2014 exit now, don't wait for the stop price", cl.DN, yy=0.03)
    cl.clean(ax2, sub="The same stall, but the swing low the thesis depended on genuinely breaks.")
    ax2.set_ylim(min(l2) - 0.0044, max(h2) + 0.0018)

    cl.save(fig, path("m7_momentum_vs_failure.png"))


# ---------------------------------------------------------------------------
# 6. Reversal signal against an open position
# ---------------------------------------------------------------------------
def f_reversal_signal():
    fig, ax = plt.subplots(figsize=(13.8, 6.8))
    shape = cl.seg((6, -0.0006), (7, 0.0052), (3, 0.0004), (1, -0.0030))
    o, h, l, c = cl.series(seed=261, shape=shape, noise=0.00024, wick=0.00026, start=1.0850)
    entry_i = 5
    entry_lvl = float(c[entry_i])
    # force the last candle to be a strong bearish engulfing against the long
    prior_o, prior_c = float(o[-2]), float(c[-2])
    o[-1] = prior_c + 0.00006
    c[-1] = prior_o - 0.00050
    h[-1] = o[-1] + 0.00008
    l[-1] = c[-1] - 0.00010
    cl.candles(ax, o, h, l, c)
    cl.hline(ax, entry_lvl, cl.BLUE, label=f"entry {entry_lvl:.4f}", n=0, side="left", va="bottom")
    cl.label_point(ax, len(o) - 1, c[-1], "strong bearish engulfing\nprints at the highs \u2014\na genuine reversal signal", cl.DN, dx=-4.0, dy=0.0006, fs=8.4, ha="right", rad=-0.2)
    cl.verdict(ax, "Reduce or exit \u2014 a real reversal signal outranks an unrealized profit target", cl.DN, yy=0.03)
    cl.clean(ax, title="Figure 7.6 — A Genuine Reversal Signal Against an Open Position",
             sub="The position is still profitable and the original stop has not been touched. A qualifying reversal pattern (Module 5) at a meaningful location changes the picture regardless of unrealized P&L.",
             ts=13.4)
    ax.set_ylim(min(l) - 0.0012, max(h) + 0.0014)
    cl.save(fig, path("m7_reversal_signal.png"), rect=(0.012, 0.02, 0.99, 0.86))


# ---------------------------------------------------------------------------
# 7. Structure-based trailing
# ---------------------------------------------------------------------------
def f_trailing():
    fig, ax = plt.subplots(figsize=(13.8, 7.0))
    shape = cl.seg((5, -0.0006), (5, 0.0042), (3, -0.0006), (5, 0.0040), (3, -0.0006), (5, 0.0038))
    o, h, l, c = cl.series(seed=271, shape=shape, noise=0.00022, wick=0.00024, start=1.0850)
    cl.candles(ax, o, h, l, c)
    entry_i = 4
    entry_lvl = float(c[entry_i])
    s1 = float(min(l[7:10])) - 0.00012
    s2 = float(min(l[12:15])) - 0.00012
    s3 = float(min(l[17:20])) - 0.00012
    cl.hline(ax, entry_lvl, cl.BLUE, label=f"entry {entry_lvl:.4f}", n=0, side="left", va="bottom")
    ax.plot([9, 14], [s1, s1], color=cl.ACCENT, lw=1.6, ls="--", alpha=0.9)
    ax.plot([14, 19], [s2, s2], color=cl.ACCENT, lw=1.6, ls="--", alpha=0.9)
    ax.plot([19, len(o) - 1], [s3, s3], color=cl.ACCENT, lw=1.6, ls="--", alpha=0.9)
    ax.text(9, s1 - 0.00008, "stop 1: below swing after leg 1", fontsize=8.2, color=cl.ACCENT, ha="left", va="top", fontweight="bold")
    ax.text(14, s2 - 0.00008, "stop 2: below swing after leg 2", fontsize=8.2, color=cl.ACCENT, ha="left", va="top", fontweight="bold")
    ax.text(19, s3 - 0.00008, "stop 3: below swing after leg 3", fontsize=8.2, color=cl.ACCENT, ha="left", va="top", fontweight="bold")
    cl.verdict(ax, "Each stop moves only when a new swing genuinely forms \u2014 never on elapsed time or a fixed pip trail", cl.UP, yy=0.03)
    cl.clean(ax, title="Figure 7.7 — Structure-Based Trailing",
             sub="The stop steps up behind each new confirmed swing low as the move progresses in legs. It never moves on a timer and never trails by a fixed pip distance disconnected from structure.",
             ts=13.4)
    ax.set_ylim(min(l) - 0.0018, max(h) + 0.0016)
    cl.save(fig, path("m7_trailing.png"), rect=(0.012, 0.02, 0.99, 0.86))


# ---------------------------------------------------------------------------
# 8. Time is descriptive, not a rule — two trades of different duration
# ---------------------------------------------------------------------------
def f_time_not_a_rule():
    fig, axes = cl.panel_fig(
        "Figure 7.8 — Duration Is Descriptive, Not a Rule",
        "Left: force-closed at 60 minutes purely on elapsed time. Right: the same move, held because structure never failed.",
        ncols=2, figsize=(15.8, 6.6))

    ax = axes[0]
    shape = cl.seg((4, -0.0006), (4, 0.0034), (10, 0.0006), (6, 0.0058))
    o, h, l, c = cl.series(seed=281, shape=shape, noise=0.00022, wick=0.00024, start=1.0850)
    cl.candles(ax, o, h, l, c)
    entry_i = 3
    entry_lvl = float(c[entry_i])
    force_close_i = 11  # ~60 minutes at 15M bars from entry
    cl.hline(ax, entry_lvl, cl.BLUE, label=f"entry {entry_lvl:.4f}", n=len(o) - 1, side="right", va="bottom")
    ax.axvline(force_close_i, color=cl.DN, lw=1.6, ls="--", alpha=0.85)
    ax.text(force_close_i, max(h) + 0.0002, "forced close\nat 60 minutes", fontsize=8.4, color=cl.DN, ha="center", va="bottom", fontweight="bold")
    cl.label_point(ax, len(o) - 3, h[-3], "move continues well\nbeyond the clock-based exit \u2014\nleft on the table", cl.MUTED, dx=-3.4, dy=0.0006, fs=8.2, ha="right", rad=-0.2)
    cl.verdict(ax, "Wrong \u2014 exited on a clock while structure was intact", cl.DN, yy=0.03)
    cl.clean(ax, sub="No structural reason to exit at minute 60 \u2014 closed purely on elapsed time.")
    ax.set_ylim(min(l) - 0.0012, max(h) + 0.0024)

    ax2 = axes[1]
    o2, h2, l2, c2 = o.copy(), h.copy(), l.copy(), c.copy()
    cl.candles(ax2, o2, h2, l2, c2)
    entry_lvl2 = entry_lvl
    cl.hline(ax2, entry_lvl2, cl.BLUE, label=f"entry {entry_lvl2:.4f}", n=len(o2) - 1, side="right", va="bottom")
    cl.label_point(ax2, len(o2) - 3, h2[-3], "held to the genuine\nstructural target \u2014\nno clock involved", cl.UP, dx=-3.4, dy=0.0006, fs=8.2, ha="right", rad=-0.2)
    cl.verdict(ax2, "Correct \u2014 structure never failed, trade stayed open past 60 minutes", cl.UP, yy=0.03)
    cl.clean(ax2, sub="Managed by structure alone \u2014 the 10\u201360 minute window is descriptive, never a rule.")
    ax2.set_ylim(min(l2) - 0.0012, max(h2) + 0.0024)

    cl.save(fig, path("m7_time_not_a_rule.png"))


if __name__ == "__main__":
    f_management_tree()
    f_leave_alone()
    f_breakeven()
    f_partial_profit()
    f_momentum_vs_failure()
    f_reversal_signal()
    f_trailing()
    f_time_not_a_rule()
    print("All Module 7 figures written.")
