"""
figs_m5.py — Module 5 figures: 15M Candlestick Triggers & Price Psychology.
Run: python3 figs_m5.py   (writes into ../images/)
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
# 1. Candle anatomy — body vs wick, the vocabulary
# ---------------------------------------------------------------------------
def f_anatomy():
    fig, axes = plt.subplots(1, 3, figsize=(15.6, 7.6))
    fig.subplots_adjust(top=0.74, bottom=0.20, wspace=0.55)
    cl.suptitle(fig, "Figure 5.1 — Candle Anatomy: What Body and Wick Actually Record",
                "Three candles with identical range, different body-to-wick relationships. The body records where aggression won; the wicks record where it was rejected.",
                y=0.965)

    specs = [
        ("Strong body\n(momentum)", 100.0, 100.85, 99.92, 100.80, cl.UP, None),
        ("Small body, long wicks\n(indecision)", 100.0, 100.85, 99.92, 100.10, cl.MUTED, None),
        ("Pin bar\n(rejection)", 100.55, 100.85, 99.92, 100.50, cl.PINK, None),
    ]
    notes_tmpl = [
        "Body \u2248 {pct:.0f}% of range.\nBuyers controlled the\ncandle almost start to finish.",
        "Body \u2248 {pct:.0f}% of range.\nPrice travelled the full range\nbut gave almost all of it back.",
        "Body \u2248 {pct:.0f}% of range near\nthe top. The long lower wick\nshows a level defended hard.",
    ]
    for ax, (title, o, h, l, c, col, _), note_tmpl in zip(axes, specs, notes_tmpl):
        pct = abs(c - o) / (h - l) * 100
        note = note_tmpl.format(pct=pct)
        ax.set_xlim(-1, 1)
        x = 0
        ax.plot([x, x], [l, h], color=col, lw=2.2, zorder=3)
        bh, bl = max(o, c), min(o, c)
        ax.add_patch(mpatches.Rectangle((x - 0.28, bl), 0.56, bh - bl, facecolor=col,
                                         edgecolor=col, lw=1, zorder=4))
        ax.annotate("high", xy=(x, h), xytext=(0.42, h), fontsize=8.6, color=cl.MUTED, va="center")
        ax.annotate("low", xy=(x, l), xytext=(0.42, l), fontsize=8.6, color=cl.MUTED, va="center")
        ax.annotate("open" if o < c else "close", xy=(x, o), xytext=(-0.85, o), fontsize=8.2, color=cl.TXT, va="center", ha="left")
        ax.annotate("close" if o < c else "open", xy=(x, c), xytext=(-0.85, c), fontsize=8.2, color=cl.TXT, va="center", ha="left")
        ax.set_title(title, fontsize=11.2, color=col, fontweight="bold", pad=14, linespacing=1.4)
        ax.text(0.5, -0.20, note, transform=ax.transAxes, fontsize=8.6, color=cl.MUTED,
                 ha="center", va="top", linespacing=1.5)
        ax.set_ylim(l - 0.15, h + 0.15)
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.set_facecolor(cl.PANEL)

    fig.savefig(path("m5_anatomy.png"), dpi=150, facecolor=cl.BG)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 2. Rejection / pin bar at a graded zone
# ---------------------------------------------------------------------------
def f_rejection_pin():
    fig, axes = cl.panel_fig(
        "Figure 5.2 — The Same Pin Bar, Two Locations",
        "Left: a long lower wick at a fresh 1H demand zone with liquidity beneath it \u2014 the wick has a mechanism. Right: an identical-looking wick in the middle of a range with no location behind it.",
        ncols=2, figsize=(15.2, 6.0))

    ax = axes[0]
    shape = cl.seg((10, -0.0035), (3, -0.0004))
    o, h, l, c = cl.series(seed=91, shape=shape, noise=0.00030, wick=0.00028, start=1.0870)
    lo = float(l[-1]) - 0.00055
    hi = float(h[-1])
    o[-1] = hi - 0.00010
    c[-1] = hi - 0.00005
    l[-1] = lo
    h[-1] = hi
    cl.candles(ax, o, h, l, c)
    zlo, zhi = lo - 0.00015, float(max(h[6:11]))
    cl.zone(ax, 5.5, len(o) - 0.5, zlo, zhi, cl.UP, label=f"1H demand\n{zlo:.4f}\u2013{zhi:.4f}", lblside="left", va="bottom")
    body_pct = abs(c[-1] - o[-1]) / (h[-1] - l[-1]) * 100
    cl.label_point(ax, len(o) - 1, h[-1], f"pin bar,\nbody \u2248 {body_pct:.0f}% of range", cl.PINK, dx=-3.5, dy=0.00025, fs=8.6, ha="right", rad=0.2)
    cl.verdict(ax, "Meaningful — location + liquidity + rejection", cl.UP, yy=0.03)
    cl.clean(ax, sub="Wick sweeps beneath a graded demand zone and closes back inside it with conviction.")
    ax.set_ylim(lo - 0.00055, zhi + 0.00060)

    ax2 = axes[1]
    shape2 = cl.seg((14, 0.0002))
    o2, h2, l2, c2 = cl.series(seed=92, shape=shape2, noise=0.00035, wick=0.00030, start=1.0870)
    lo2 = float(l2[-1]) - 0.00050
    hi2 = float(h2[-1])
    o2[-1] = hi2 - 0.00012
    c2[-1] = hi2 - 0.00006
    l2[-1] = lo2
    h2[-1] = hi2
    cl.candles(ax2, o2, h2, l2, c2)
    band_hi = float(np.percentile(h2, 78))
    band_lo = float(np.percentile(l2, 22))
    cl.zone(ax2, -0.5, len(o2) - 0.5, band_lo, band_hi, cl.MUTED, label="mid-range, no location", lblside="left", alpha=0.08, va="top")
    cl.label_point(ax2, len(o2) - 1, hi2, "same shape,\nno mechanism", cl.MUTED, dx=-3.5, dy=0.00045, fs=8.6, ha="right", rad=0.2)
    cl.verdict(ax2, "Meaningless — no location, no liquidity to react to", cl.DN, yy=0.03)
    cl.clean(ax2, sub="Same wick shape, but nothing structural sits beneath it \u2014 no zone, no swept liquidity.")
    ax2.set_ylim(lo2 - 0.00055, hi2 + 0.00085)

    cl.save(fig, path("m5_rejection_pin.png"))


# ---------------------------------------------------------------------------
# 3. Engulfing pattern — with and without structural support
# ---------------------------------------------------------------------------
def f_engulfing():
    fig, axes = cl.panel_fig(
        "Figure 5.3 — Engulfing Candles: Structure Decides Whether It Matters",
        "Left: a bullish engulfing candle at a tested demand zone after a sweep. Right: the identical shape mid-range with nothing beneath it.",
        ncols=2, figsize=(15.8, 6.2))

    ax = axes[0]
    shape = cl.seg((9, -0.0032), (2, -0.0006))
    o, h, l, c = cl.series(seed=101, shape=shape, noise=0.00028, wick=0.00026, start=1.2650)
    prev_lo, prev_hi = float(l[-2]), float(h[-2])
    o[-2] = prev_hi - 0.00015
    c[-2] = prev_hi - 0.00060
    l[-2] = prev_hi - 0.00075
    h[-2] = prev_hi
    eng_lo = float(l[-2]) - 0.00020
    o[-1] = eng_lo + 0.00015
    c[-1] = float(h[-2]) + 0.00030
    l[-1] = eng_lo
    h[-1] = c[-1] + 0.00010
    cl.candles(ax, o, h, l, c)
    zlo = eng_lo - 0.00010
    zhi = float(max(h[5:9]))
    cl.zone(ax, 4.5, len(o) - 0.5, zlo, zhi, cl.UP, label=f"1H demand\n{zlo:.4f}\u2013{zhi:.4f}", lblside="left", va="bottom")
    cl.label_point(ax, len(o) - 1, h[-1], "engulfing candle\nfully overtakes prior range", cl.ACCENT, dx=-6.5, dy=0.00050, fs=8.4, ha="right", rad=0.2)
    cl.verdict(ax, "Meaningful — engulfs the sweep candle at a graded zone", cl.UP, yy=0.03)
    cl.clean(ax, sub="The engulfed candle is the sweep itself; the engulfing candle is the reclaim.")
    top_needed = max(float(max(h)), zhi) + 0.00120
    ax.set_ylim(zlo - 0.00030, top_needed)

    ax2 = axes[1]
    shape2 = cl.seg((11, 0.0003))
    o2, h2, l2, c2 = cl.series(seed=102, shape=shape2, noise=0.00032, wick=0.00028, start=1.2650)
    prev_lo2, prev_hi2 = float(l2[-2]), float(h2[-2])
    o2[-2] = prev_hi2 - 0.00012
    c2[-2] = prev_hi2 - 0.00055
    l2[-2] = prev_hi2 - 0.00068
    h2[-2] = prev_hi2
    eng_lo2 = float(l2[-2]) - 0.00018
    o2[-1] = eng_lo2 + 0.00012
    c2[-1] = float(h2[-2]) + 0.00025
    l2[-1] = eng_lo2
    h2[-1] = c2[-1] + 0.00008
    cl.candles(ax2, o2, h2, l2, c2)
    band_hi = float(np.percentile(h2[:-2], 75))
    band_lo = float(np.percentile(l2[:-2], 25))
    cl.zone(ax2, -0.5, len(o2) - 2.5, band_lo, band_hi, cl.MUTED, label="mid-range, no zone", lblside="left", alpha=0.08, va="top")
    cl.label_point(ax2, len(o2) - 1, h2[-1], "same pattern,\nno location beneath it", cl.MUTED, dx=-6.5, dy=0.00045, fs=8.4, ha="right", rad=0.2)
    cl.verdict(ax2, "Meaningless — engulfing shape, no location or liquidity", cl.DN, yy=0.03)
    cl.clean(ax2, sub="Identical two-candle shape, but nothing was swept and no zone supports it.")
    ax2.set_ylim(band_lo - 0.00030, h2[-1] + 0.00060)

    cl.save(fig, path("m5_engulfing.png"))


# ---------------------------------------------------------------------------
# 4. Momentum / expansion candle vs drifting indecision
# ---------------------------------------------------------------------------
def f_momentum():
    fig, axes = cl.panel_fig(
        "Figure 5.4 — Momentum Candle vs Drift",
        "Same net distance travelled over five candles. Left: one expansion candle does most of the work. Right: the same distance covered by a slow overlapping grind.",
        ncols=2, figsize=(15.4, 6.2))

    ax = axes[0]
    o = np.array([100.00, 100.05, 100.10, 100.95, 101.02])
    c = np.array([100.05, 100.10, 100.95, 101.00, 101.08])
    h = c + np.array([0.04, 0.05, 0.06, 0.05, 0.05])
    l = o - np.array([0.05, 0.04, 0.04, 0.06, 0.05])
    cl.candles(ax, o, h, l, c)
    body_pct = (c[2] - o[2]) / (h[2] - l[2]) * 100
    cl.label_point(ax, 2, h[2], f"expansion candle,\nbody \u2248 {body_pct:.0f}% of range,\nlittle overlap with neighbours", cl.ACCENT, dx=-1.0, dy=0.28, fs=8.4, ha="right", rad=0.2)
    cl.verdict(ax, "Momentum — displacement test passes (Module 2)", cl.UP, yy=0.03)
    cl.clean(ax, sub="One candle contributes most of the five-candle move, with minimal overlap into the range of its neighbours.")
    ax.set_ylim(l.min() - 0.15, h.max() + 0.45)

    ax2 = axes[1]
    o2 = np.array([100.00, 100.08, 99.98, 100.15, 100.20])
    c2 = np.array([100.08, 99.98, 100.15, 100.10, 100.30])
    h2 = np.maximum(o2, c2) + 0.10
    l2 = np.minimum(o2, c2) - 0.10
    cl.candles(ax2, o2, h2, l2, c2)
    cl.label_point(ax2, 2, h2[2], "overlapping ranges,\nno candle stands out", cl.MUTED, dx=1.0, dy=0.28, fs=8.4, ha="left", rad=0.2)
    cl.verdict(ax2, "Drift — displacement test fails, net move is the same", cl.DN, yy=0.03)
    cl.clean(ax2, sub="Five candles overlap heavily; the same net distance is covered without any single candle showing force.")
    ax2.set_ylim(l2.min() - 0.30, h2.max() + 0.45)

    cl.save(fig, path("m5_momentum.png"))


# ---------------------------------------------------------------------------
# 5. Inside bar — compression, and both resolution directions
# ---------------------------------------------------------------------------
def f_inside_bar():
    fig, ax = plt.subplots(figsize=(13.4, 6.4))
    shape = cl.seg((6, 0.0055), (3, 0.0003), (1, -0.0002), (1, 0.0001), (5, 0.0038))
    o, h, l, c = cl.series(seed=111, shape=shape, noise=0.00022, wick=0.00020, start=1.0870)
    mother_hi = float(h[8])
    mother_lo = float(l[8])
    # force candles 9 and 10 to sit fully inside candle 8's range (inside bars)
    for i in (9, 10):
        span = mother_hi - mother_lo
        o[i] = mother_lo + span * 0.35
        c[i] = mother_lo + span * 0.55
        h[i] = mother_lo + span * 0.62
        l[i] = mother_lo + span * 0.28
    cl.candles(ax, o, h, l, c)
    cl.zone(ax, 7.6, 10.5, mother_lo, mother_hi, cl.CYAN, label=None)
    ax.text(9.05, mother_lo - 0.00035, "mother bar range", fontsize=8.4, color=cl.CYAN,
             ha="center", va="top", fontweight="bold")
    cl.label_point(ax, 9.5, mother_hi, "two inside bars:\nrange compresses\nbefore expansion", cl.CYAN, dx=-3.6, dy=0.0038, fs=8.6, ha="left", rad=-0.2)
    cl.label_point(ax, 13.2, h[13], "expansion resolves\nthe compression upward", cl.UP, dx=2.6, dy=0.0022, fs=8.6, ha="left", rad=0.2)
    cl.clean(ax, title="Figure 5.5 — Inside Bars: Compression Before Expansion",
             sub="Two consecutive candles trade fully within the range of the candle before them (the \u201cmother bar\u201d). Range compresses, then resolves with an expansion candle.",
             ts=13.5)
    ax.set_ylim(min(l) - 0.0006, max(h) + 0.0022)
    cl.save(fig, path("m5_inside_bar.png"), rect=(0.012, 0.02, 0.99, 0.86))


# ---------------------------------------------------------------------------
# 6. Failed breakout candle
# ---------------------------------------------------------------------------
def f_failed_breakout():
    fig, ax = plt.subplots(figsize=(13.4, 6.4))
    shape = cl.seg((10, 0.0010), (1, 0.0006), (5, -0.0028))
    o, h, l, c = cl.series(seed=121, shape=shape, noise=0.00022, wick=0.00020, start=1.0860)
    level = float(max(h[:10]))
    # force candle 10 to wick above the level but close back beneath it (failed breakout)
    o[10] = level - 0.00025
    c[10] = level - 0.00040
    h[10] = level + 0.00055
    l[10] = level - 0.00070
    # cap every later candle's high well below the failed-breakout wick, so that
    # single crafted wick remains the clear extreme of the whole move
    cap = h[10] - 0.00015
    for i in range(11, len(o)):
        if h[i] > cap:
            over = h[i] - cap
            o[i] -= over
            c[i] -= over
            h[i] -= over
            l[i] -= over
    cl.candles(ax, o, h, l, c)
    cl.hline(ax, level, cl.ACCENT, label="prior structural high", n=0, side="left", va="bottom")
    cl.label_point(ax, 10, h[10], "wicks above the level,\ncloses back beneath it \u2014\nno acceptance", cl.DN, dx=1.5, dy=0.0012, fs=8.6, ha="left", rad=0.2)
    cl.verdict(ax, "Failed breakout \u2014 the wick is the signal, not the level breaking", cl.DN, yy=0.03)
    cl.clean(ax, title="Figure 5.6 — The Failed Breakout Candle",
             sub="Price wicks through a well-known structural level, attracting breakout buyers, then closes back beneath it within the same candle. The break failed to gain acceptance.",
             ts=13.5)
    ax.set_ylim(min(l) - 0.0015, h[10] + 0.0018)
    cl.save(fig, path("m5_failed_breakout.png"), rect=(0.012, 0.02, 0.99, 0.86))


# ---------------------------------------------------------------------------
# 7. Context dependence — same candle shape, three different verdicts
# ---------------------------------------------------------------------------
def f_context_dependence():
    fig, ax = cl.blank_canvas((13.6, 7.6),
        "Figure 5.7 — One Candle Shape, Three Verdicts",
        "The same bullish pin bar means something different depending on what sits beneath it. The candle itself never changes; the surrounding structure decides its reliability.")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    rows = [
        (78, cl.UP, "AT A FRESH, GRADED DEMAND ZONE\nwith swept liquidity beneath it",
         "High reliability. Location + liquidity + rejection all agree \u2014 this is what step 6/7 of Module 4's sequence looks for."),
        (48, cl.ACCENT, "AT A THIRD-TOUCH, PARTIALLY DEPLETED ZONE\n(Module 3, \u00a73.4)",
         "Reduced reliability. The pin bar is real, but the zone has already absorbed two prior reactions \u2014 treat it as weaker evidence, not disqualifying evidence."),
        (18, cl.DN, "IN THE MIDDLE OF A RANGE\nwith no zone, no liquidity, no structure",
         "No reliability. The candle looks identical, but there is no mechanism for it to mean anything \u2014 Module 4 \u00a74.6's stand-aside conditions apply."),
    ]
    for y, col, title, body in rows:
        ax.add_patch(mpatches.FancyBboxPatch((4, y - 12), 20, 20,
            boxstyle="round,pad=0.5,rounding_size=2", facecolor="#131a29", edgecolor=col, lw=1.6, zorder=2))
        # simple pin-bar glyph
        cx, cy = 14, y
        ax.plot([cx, cx], [cy - 8, cy + 8], color=col, lw=2.4, zorder=3)
        ax.add_patch(mpatches.Rectangle((cx - 2.2, cy + 3), 4.4, 4, facecolor=col, edgecolor=col, zorder=4))
        ax.text(32, y + 9, title, fontsize=10.6, color=col, fontweight="bold", ha="left", va="center")
        ax.text(32, y - 6, body, fontsize=9.6, color=cl.TXT, ha="left", va="center", wrap=True)

    cl.save_flat(fig, path("m5_context_dependence.png"), pad=0.35)


# ---------------------------------------------------------------------------
# 8. Compression-to-expansion sequence (full mini-story)
# ---------------------------------------------------------------------------
def f_compression_expansion():
    fig, ax = plt.subplots(figsize=(13.6, 6.4))
    shape = cl.seg((8, -0.0035), (6, 0.0002), (1, 0.0004))
    o, h, l, c = cl.series(seed=131, shape=shape, noise=0.00016, wick=0.00014, start=1.0870)
    # force candles 8-13 into a tightening range (compression)
    base_lo, base_hi = float(l[7]), float(h[7])
    mid = (base_lo + base_hi) / 2
    for k, i in enumerate(range(8, 14)):
        shrink = 1 - k * 0.13
        span = (base_hi - base_lo) * shrink * 0.5
        o[i] = mid - span * 0.3
        c[i] = mid + span * 0.3
        h[i] = mid + span * 0.55
        l[i] = mid - span * 0.55
    # expansion candle breaks out
    exp_i = 14
    o[exp_i] = mid + span * 0.2
    c[exp_i] = mid + span * 2.6
    h[exp_i] = c[exp_i] + 0.00012
    l[exp_i] = o[exp_i] - 0.00010
    cl.candles(ax, o, h, l, c)
    cl.zone(ax, 7.5, 13.5, mid - span * 0.6, mid + span * 0.6, cl.CYAN, label="compression:\nrange tightens candle by candle", lblside="left", va="top")
    cl.label_point(ax, exp_i, h[exp_i], "expansion candle\nresolves the compression", cl.UP, dx=-3.5, dy=0.0010, fs=8.6, ha="right", rad=-0.2)
    cl.clean(ax, title="Figure 5.8 — Compression Before Expansion",
             sub="A visibly shrinking range over several candles \u2014 each one's high-low span smaller than the last \u2014 frequently precedes a displacement leg. The compression does not predict direction on its own.",
             ts=13.5)
    ax.set_ylim(min(l) - 0.0012, max(h) + 0.0022)
    cl.save(fig, path("m5_compression_expansion.png"), rect=(0.012, 0.02, 0.99, 0.86))


if __name__ == "__main__":
    f_anatomy()
    f_rejection_pin()
    f_engulfing()
    f_momentum()
    f_inside_bar()
    f_failed_breakout()
    f_context_dependence()
    f_compression_expansion()
    print("All Module 5 figures written.")
