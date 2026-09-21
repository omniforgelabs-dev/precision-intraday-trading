"""
figs_m8.py — Module 8 figures: When NOT to Trade.
Run: python3 figs_m8.py   (writes into ../images/)
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
# 1. Comprehensive stand-aside grid
# ---------------------------------------------------------------------------
def f_stand_aside_grid():
    fig, ax = cl.blank_canvas((13.8, 9.6),
        "Figure 8.1 — Sixteen Reasons the Sequence Never Reaches a Trade",
        "None of these require judgement calls under pressure. Each one is a specific, nameable condition from earlier modules failing to hold.")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    cols = [
        (2, 32, cl.MUTED, "MARKET CONDITION", [
            "Chop \u2014 no directional\nHH/HL or LH/LL",
            "Low-quality range \u2014\nno expansion, no edges",
            "Poor 4H/1H structure \u2014\nno clean swings to read",
            "Conflicting HTF context \u2014\n4H and 1H disagree",
            "Abnormal market behaviour \u2014\nerratic, non-structural moves",
        ]),
        (35, 65, cl.CYAN, "LOCATION & CONFIRMATION", [
            "Weak/unclear S&R \u2014\nno real reaction history",
            "Excessively tested zone \u2014\npotency exhausted (\u00a73.7)",
            "Poor liquidity \u2014 nothing\nresting nearby to react to",
            "Weak 15M confirmation \u2014\nclose mid-range, no conviction",
            "Unclear invalidation \u2014\nno sensible place for a stop",
        ]),
        (68, 98, cl.PINK, "EXECUTION & RISK", [
            "Late entry / chasing \u2014\nmove already extended",
            "Poor R:R \u2014 genuine target\ngives less than 1:2",
            "Excessive spread/slippage \u2014\ncost erodes the edge",
            "Unusual volatility \u2014 ranges\nfar outside the normal",
            "Major scheduled news \u2014\noutcome is not price action",
            "Correlated over-concentration \u2014\nsame risk, multiple tickets",
        ]),
    ]

    for x0, x1, col, title, items in cols:
        ax.add_patch(mpatches.FancyBboxPatch((x0, 4), x1 - x0, 88,
            boxstyle="round,pad=0.6,rounding_size=2.5", facecolor="#131a29",
            edgecolor=col, lw=1.6, zorder=2))
        ax.text((x0 + x1) / 2, 88.5, title, ha="center", va="top", fontsize=10.6,
                 color=col, fontweight="bold", zorder=3)
        y = 78
        step = 68.0 / (len(items) - 1) if len(items) > 1 else 0
        for it in items:
            ax.text(x0 + 2.0, y, "\u2022", color=col, fontsize=12, ha="left", va="top", zorder=3)
            ax.text(x0 + 4.6, y, it, color=cl.TXT, fontsize=8.5, ha="left", va="top",
                     linespacing=1.5, zorder=3)
            y -= step

    ax.text(2, -3.5, "Any single item on this list is sufficient on its own to end the sequence \u2014 they do not need to occur together.",
            fontsize=9.2, color=cl.MUTED, ha="left", va="bottom")
    ax.set_ylim(-8, 100)
    cl.save_flat(fig, path("m8_stand_aside_grid.png"), pad=0.35)



# ---------------------------------------------------------------------------
# 2. Chop vs clean trend
# ---------------------------------------------------------------------------
def f_chop_vs_trend():
    fig, axes = cl.panel_fig(
        "Figure 8.2 — Chop vs a Readable Trend",
        "Same instrument, same number of bars. Left: no directional structure exists to trade with. Right: clean HH/HL structure the entry model can actually use.",
        ncols=2, figsize=(15.6, 6.4))

    ax = axes[0]
    shape = cl.seg((5, 0.0018), (5, -0.0020), (5, 0.0014), (5, -0.0022), (5, 0.0020), (5, -0.0016))
    o, h, l, c = cl.series(seed=811, shape=shape, noise=0.00030, wick=0.00034, start=1.0870)
    cl.candles(ax, o, h, l, c)
    band_hi = float(np.percentile(h, 85))
    band_lo = float(np.percentile(l, 15))
    cl.zone(ax, -0.5, len(o) - 0.5, band_lo, band_hi, cl.MUTED, label="no HH/HL or LH/LL \u2014 pure range",
            lblside="left", alpha=0.10, va="top")
    cl.verdict(ax, "Chop \u2014 4H/1H structure is unreadable, stand aside", cl.MUTED, yy=0.03)
    cl.clean(ax, sub="Price oscillates without ever printing a clean sequence of higher highs/lows or lower highs/lows.")
    ax.set_ylim(min(l) - 0.0012, max(h) + 0.0016)

    ax2 = axes[1]
    shape2 = cl.seg((5, 0.0026), (3, -0.0008), (5, 0.0030), (3, -0.0010), (5, 0.0032), (3, -0.0008))
    o2, h2, l2, c2 = cl.series(seed=812, shape=shape2, noise=0.00028, wick=0.00032, start=1.0850)
    cl.candles(ax2, o2, h2, l2, c2)
    cl.swing_marks(ax2, [(4, "L", "HL"), (7, "H", "HH"), (12, "L", "HL"), (15, "H", "HH"), (20, "L", "HL"), (23, "H", "HH")],
                    h2, l2, col_hi=cl.UP, col_lo=cl.BLUE, dy_hi=0.0009, dy_lo=0.0009, fs=8.0)
    cl.verdict(ax2, "Readable trend \u2014 HH/HL structure supports a directional bias", cl.UP, yy=0.03)
    cl.clean(ax2, sub="Each pullback holds above the prior higher low. Structure is unambiguous.")
    ax2.set_ylim(min(l2) - 0.0016, max(h2) + 0.0016)

    cl.save(fig, path("m8_chop_vs_trend.png"))


# ---------------------------------------------------------------------------
# 3. Conflicting HTF context vs aligned
# ---------------------------------------------------------------------------
def f_conflicting_context():
    fig, axes = cl.panel_fig(
        "Figure 8.3 — Conflicting HTF Context vs Aligned Context",
        "Left: the 4H is bullish but the 1H is printing a clean downtrend against it \u2014 no coherent directional bias exists yet. Right: 4H and 1H agree, giving a single readable direction.",
        ncols=2, figsize=(15.6, 6.4))

    ax = axes[0]
    shape = cl.seg((6, 0.0030), (5, -0.0034), (4, 0.0006), (5, -0.0030), (4, 0.0004), (5, -0.0026))
    o, h, l, c = cl.series(seed=821, shape=shape, noise=0.00030, wick=0.00034, start=1.0860)
    cl.candles(ax, o, h, l, c)
    cl.badge(ax, "1H: LH/LL \u2014 down", cl.DN, loc="tl")
    cl.badge(ax, "4H bias: up", cl.UP, loc="tr")
    cl.verdict(ax, "Conflict \u2014 no coherent direction, stand aside", cl.MUTED, yy=0.03)
    cl.clean(ax, sub="1H prints lower highs/lows while the 4H remains bullish.")
    ax.set_ylim(min(l) - 0.0012, max(h) + 0.0014)

    ax2 = axes[1]
    shape2 = cl.seg((6, 0.0028), (4, -0.0008), (6, 0.0032), (4, -0.0010), (6, 0.0034))
    o2, h2, l2, c2 = cl.series(seed=822, shape=shape2, noise=0.00028, wick=0.00032, start=1.0850)
    cl.candles(ax2, o2, h2, l2, c2)
    cl.badge(ax2, "1H: HH/HL \u2014 up", cl.UP, loc="tl")
    cl.badge(ax2, "4H bias: up", cl.UP, loc="tr")
    cl.verdict(ax2, "Aligned \u2014 4H and 1H agree on direction", cl.UP, yy=0.03)
    cl.clean(ax2, sub="1H prints its own higher highs/lows inside the 4H uptrend.")
    ax2.set_ylim(min(l2) - 0.0012, max(h2) + 0.0014)


    cl.save(fig, path("m8_conflicting_context.png"))


# ---------------------------------------------------------------------------
# 4. Excessively tested zone vs fresh zone
# ---------------------------------------------------------------------------
def f_overtested_zone():
    fig, axes = cl.panel_fig(
        "Figure 8.4 — Excessively Tested Zone vs Fresh Zone",
        "Same type of demand zone. Left: five prior reactions have already consumed the resting orders there \u2014 the zone's reliability is exhausted. Right: an untested zone still holds its original liquidity.",
        ncols=2, figsize=(15.6, 6.4))

    ax = axes[0]
    shape = cl.seg((3, -0.0006), (2, 0.0022), (3, -0.0006), (2, 0.0018), (3, -0.0006), (2, 0.0014),
                    (3, -0.0006), (2, 0.0010), (3, -0.0006), (2, 0.0007), (5, 0.0004))
    o, h, l, c = cl.series(seed=831, shape=shape, noise=0.00016, wick=0.00018, start=1.0840)
    cl.candles(ax, o, h, l, c)
    zlo = float(min(l[:5])) - 0.00015
    zhi = float(max(h[:5])) + 0.00010
    cl.zone(ax, -0.5, len(o) - 0.5, zlo, zhi, cl.DN, label="same zone, 5th test", lblside="left", va="top")
    cl.verdict(ax, "Excessively tested \u2014 each reaction is weaker, treat as low-quality", cl.DN, yy=0.03)
    cl.clean(ax, sub="Five separate reactions off the same level, each producing a smaller bounce than the last (\u00a73.7).")
    ax.set_ylim(zlo - 0.0006, max(h) + 0.0010)

    ax2 = axes[1]
    shape2 = cl.seg((14, -0.0058), (10, 0.0048))
    o2, h2, l2, c2 = cl.series(seed=832, shape=shape2, noise=0.00024, wick=0.00028, start=1.0870)
    cl.candles(ax2, o2, h2, l2, c2)
    zlo2 = float(min(l2[11:16]))
    zhi2 = float(max(h2[11:16]))
    cl.zone(ax2, 10.5, 16.5, zlo2, zhi2, cl.UP, label="fresh demand \u2014 1st test", lblside="left", va="top")
    cl.verdict(ax2, "Fresh \u2014 first test, full original liquidity likely still resting", cl.UP, yy=0.03)
    cl.clean(ax2, sub="Origin of a displacement leg, never revisited since \u2014 the zone's first test carries the most weight.")
    ax2.set_ylim(zlo2 - 0.0012, max(h2) + 0.0012)

    cl.save(fig, path("m8_overtested_zone.png"))


# ---------------------------------------------------------------------------
# 5. Late entry / chasing vs structural entry
# ---------------------------------------------------------------------------
def f_late_entry_chase():
    fig, axes = cl.panel_fig(
        "Figure 8.5 — Chasing an Extended Move vs a Structural Entry",
        "Same uptrend. Left: entry is taken far from any structure, after the move has already run, purely to avoid missing it. Right: entry waits for a pullback into the last valid structure.",
        ncols=2, figsize=(15.6, 6.4))

    ax = axes[0]
    shape = cl.seg((6, 0.0006), (4, 0.0040), (10, 0.0058))
    o, h, l, c = cl.series(seed=841, shape=shape, noise=0.00026, wick=0.00030, start=1.0850)
    cl.candles(ax, o, h, l, c)
    chase_i = len(o) - 2
    chase_lvl = float(c[chase_i])
    origin_lvl = float(min(l[:6]))
    cl.hline(ax, chase_lvl, cl.DN, label=f"chased entry {chase_lvl:.4f}", n=0, side="left", va="bottom")
    cl.label_point(ax, chase_i, h[chase_i], "no nearby structure\nto place a sensible stop\nor measure real risk",
                    cl.DN, dx=-4.2, dy=0.0012, fs=8.3, ha="right", rad=-0.2)
    cl.verdict(ax, "Chasing \u2014 no structure at this price to invalidate against", cl.DN, yy=0.03)
    cl.clean(ax, sub=f"Move has run {(chase_lvl-origin_lvl)*10000:.0f} pips from its origin with no pullback; entering here has no defensible stop location.")
    ax.set_ylim(min(l) - 0.0010, max(h) + 0.0020)

    ax2 = axes[1]
    shape2 = cl.seg((6, 0.0006), (4, 0.0038), (5, -0.0018), (8, 0.0052))
    o2, h2, l2, c2 = cl.series(seed=842, shape=shape2, noise=0.00026, wick=0.00030, start=1.0850)
    cl.candles(ax2, o2, h2, l2, c2)
    entry_i = 11
    entry_lvl = float(c2[entry_i])
    stop_lvl = float(min(l2[9:12]))
    cl.hline(ax2, entry_lvl, cl.BLUE, label=f"entry {entry_lvl:.4f}", n=len(o2) - 1, side="right", va="bottom")
    cl.hline(ax2, stop_lvl, cl.DN, label=f"stop {stop_lvl:.4f}", n=len(o2) - 1, side="right", va="top")
    cl.verdict(ax2, "Structural \u2014 entry has a defensible, nearby invalidation point", cl.UP, yy=0.03)
    cl.clean(ax2, sub="Entry waits for the pullback into the most recent higher low before continuation resumes.")
    ax2.set_ylim(stop_lvl - 0.0010, max(h2) + 0.0018)

    cl.save(fig, path("m8_late_entry_chase.png"))


# ---------------------------------------------------------------------------
# 6. Poor R:R vs manufactured R:R
# ---------------------------------------------------------------------------
def f_poor_rr():
    fig, axes = cl.panel_fig(
        "Figure 8.6 — Genuinely Poor R:R vs a Manufactured Target",
        "Left: the nearest real structure gives less than 1:2 \u2014 rejected. Right: the target is stretched past real structure to force the ratio above 1:2 \u2014 also rejected.",
        ncols=2, figsize=(15.6, 6.2))

    ax = axes[0]
    entry, stop = 100.0, 99.62
    real_target = 100.62
    x = np.arange(6)
    ax.plot([0, 5], [entry, entry], color=cl.BLUE, lw=1.6, ls="--")
    ax.plot([0, 5], [stop, stop], color=cl.DN, lw=1.6, ls="--")
    ax.plot([0, 5], [real_target, real_target], color=cl.UP, lw=1.6, ls="--")
    ax.text(5.05, entry, f"entry {entry:.2f}", color=cl.BLUE, fontsize=9, va="center", fontweight="bold")
    ax.text(5.05, stop, f"stop {stop:.2f}", color=cl.DN, fontsize=9, va="center", fontweight="bold")
    ax.text(5.05, real_target, f"nearest real structure {real_target:.2f}", color=cl.UP, fontsize=9, va="center", fontweight="bold")
    rr1 = (real_target - entry) / (entry - stop)
    cl.verdict(ax, f"R:R \u2248 1:{rr1:.1f} \u2014 below the 1:2 minimum, reject", cl.DN, yy=0.05)
    ax.set_xlim(-0.5, 8.5)
    ax.set_ylim(stop - 0.42, real_target + 0.35)
    ax.set_xticks([])
    cl.clean(ax, sub="The nearest opposing structure sits too close to entry.")

    ax2 = axes[1]
    manufactured_target = 100.90
    ax2.plot([0, 5], [entry, entry], color=cl.BLUE, lw=1.6, ls="--")
    ax2.plot([0, 5], [stop, stop], color=cl.DN, lw=1.6, ls="--")
    ax2.plot([0, 5], [real_target, real_target], color=cl.MUTED, lw=1.3, ls=":")
    ax2.plot([0, 5], [manufactured_target, manufactured_target], color=cl.ACCENT, lw=1.6, ls="--")
    ax2.text(5.05, entry, f"entry {entry:.2f}", color=cl.BLUE, fontsize=9, va="center", fontweight="bold")
    ax2.text(5.05, stop, f"stop {stop:.2f}", color=cl.DN, fontsize=9, va="center", fontweight="bold")
    ax2.text(5.05, real_target, "real structure ends here", color=cl.MUTED, fontsize=8.6, va="center")
    ax2.text(5.05, manufactured_target, f"manufactured target {manufactured_target:.2f}", color=cl.ACCENT, fontsize=9, va="center", fontweight="bold")
    rr2 = (manufactured_target - entry) / (entry - stop)
    cl.verdict(ax2, f"R:R \u2248 1:{rr2:.1f} on paper \u2014 target has no structural basis, reject", cl.ACCENT, yy=0.05)
    ax2.set_xlim(-0.5, 9.0)
    ax2.set_ylim(stop - 0.42, manufactured_target + 0.35)
    ax2.set_xticks([])
    cl.clean(ax2, sub="Stretching the target past real structure to flatter the arithmetic (\u00a76.3).")

    cl.save(fig, path("m8_poor_rr.png"))


# ---------------------------------------------------------------------------
# 7. Unusual volatility / scheduled news
# ---------------------------------------------------------------------------
def f_volatility_news():
    fig, ax = plt.subplots(figsize=(13.6, 6.6))
    shape = cl.seg((10, 0.0010), (1, 0.0140), (1, -0.0180), (1, 0.0110), (8, 0.0006))
    o, h, l, c = cl.series(seed=851, shape=shape, noise=0.00030, wick=0.00034, start=1.0850)
    news_i = 10
    o[news_i] = c[news_i - 1]
    h[news_i] = float(o[news_i]) + 0.0090
    l[news_i] = float(o[news_i]) - 0.0020
    c[news_i] = float(o[news_i]) + 0.0075
    o[news_i + 1] = c[news_i]
    h[news_i + 1] = float(o[news_i + 1]) + 0.0025
    l[news_i + 1] = float(o[news_i + 1]) - 0.0160
    c[news_i + 1] = float(o[news_i + 1]) - 0.0130
    cl.candles(ax, o, h, l, c)
    ax.axvline(news_i - 0.5, color=cl.ACCENT, lw=1.6, ls="--", alpha=0.85)
    ax.text(news_i - 0.5, float(max(h)) + 0.0035, "scheduled news release", fontsize=9.4, color=cl.ACCENT,
            ha="center", va="bottom", fontweight="bold")
    cl.label_point(ax, news_i + 3, h[news_i + 3], "range on this single candle is\n6\u20138x the session's normal 15M range \u2014\nthis is not price action, it's an event outcome",
                    cl.DN, dx=1.5, dy=0.0028, fs=8.4, ha="left", rad=-0.2)
    cl.verdict(ax, "Unusual volatility around scheduled news \u2014 stand aside until it settles", cl.DN, yy=0.03)
    cl.clean(ax, title="Figure 8.7 — Major Scheduled News and Unusual Volatility",
             sub="Normal 15M ranges in this session run 8\u201312 pips. The two candles bracketing the release each exceed 70 pips in a single bar \u2014 structure, stops, and targets built on this data are unreliable.",
             ts=13.5)
    ax.set_ylim(min(l) - 0.0022, max(h) + 0.0075)
    cl.save(fig, path("m8_volatility_news.png"), rect=(0.012, 0.02, 0.99, 0.86))


# ---------------------------------------------------------------------------
# 8. Psychology matrix: no trade vs fear, and the four named biases
# ---------------------------------------------------------------------------
def f_psychology_matrix():
    fig, ax = cl.blank_canvas((13.8, 9.4),
        "Figure 8.8 — \u201cNo Trade Exists\u201d vs \u201cI Am Afraid of a Valid Trade\u201d",
        "The sequence from Modules 4\u20136 is what tells the two apart \u2014 never how the trade feels in the moment.")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    ax.add_patch(mpatches.FancyBboxPatch((3, 52), 44, 37, boxstyle="round,pad=0.7,rounding_size=2.5",
        facecolor="#131a29", edgecolor=cl.MUTED, lw=1.6, zorder=2))
    ax.text(25, 86.5, "NO TRADE EXISTS", ha="center", va="top", fontsize=12.2, color=cl.MUTED, fontweight="bold", zorder=3)
    for i, t in enumerate([
        "One or more of the 16 stand-aside\nconditions (Fig. 8.1) is actually present",
        "The 13-step sequence (Module 4)\ngenuinely fails to complete",
        "Correct action: do nothing \u2014 no\nposition, no partial size, no waiting to jump in",
    ]):
        ax.text(6, 77.5 - i * 10.8, "\u2022 " + t, fontsize=9.0, color=cl.TXT, ha="left", va="top", linespacing=1.5, zorder=3)

    ax.add_patch(mpatches.FancyBboxPatch((53, 52), 44, 37, boxstyle="round,pad=0.7,rounding_size=2.5",
        facecolor="#131a29", edgecolor=cl.ACCENT, lw=1.6, zorder=2))
    ax.text(75, 86.5, "AFRAID OF A VALID TRADE", ha="center", va="top", fontsize=12.2, color=cl.ACCENT, fontweight="bold", zorder=3)
    for i, t in enumerate([
        "Every step of the 13-step sequence\nhas genuinely completed, R:R \u2265 1:2",
        "Hesitation comes from a recent loss,\naccount size, or fear of being wrong",
        "Correct action: take the trade at the\ndefined size \u2014 the setup didn't change, the feeling did",
    ]):
        ax.text(56, 77.5 - i * 10.8, "\u2022 " + t, fontsize=9.0, color=cl.TXT, ha="left", va="top", linespacing=1.5, zorder=3)

    biases = [
        ("FOMO", cl.DN, "Entering late/oversized because\na move is happening without you"),
        ("Revenge trading", cl.PINK, "Re-entering immediately after a loss\nto \u201cwin it back,\u201d ignoring the sequence"),
        ("Overtrading", cl.PURP, "Taking setups below the minimum\nconditions just to stay active"),
        ("Confirmation bias", cl.CYAN, "Reading ambiguous structure as\nsupporting a view already held"),
    ]
    bw = 22.5
    for i, (name, col, desc) in enumerate(biases):
        x0 = 3 + i * (bw + 1.3)
        ax.add_patch(mpatches.FancyBboxPatch((x0, 4), bw, 40, boxstyle="round,pad=0.5,rounding_size=2",
            facecolor="#0d1420", edgecolor=col, lw=1.4, zorder=2))
        ax.text(x0 + bw / 2, 41.5, name, ha="center", va="top", fontsize=10.4, color=col, fontweight="bold", zorder=3)
        ax.text(x0 + bw / 2, 33, desc, ha="center", va="top", fontsize=8.5, color=cl.TXT, linespacing=1.5, zorder=3)
        ax.text(x0 + bw / 2, 16, "Countermeasure:\nthe written sequence\nis the only permission\nto enter or exit", ha="center", va="top",
                fontsize=7.6, color=cl.MUTED, linespacing=1.35, zorder=3)

    cl.save_flat(fig, path("m8_psychology_matrix.png"), pad=0.35)


if __name__ == "__main__":
    f_stand_aside_grid()
    f_chop_vs_trend()
    f_conflicting_context()
    f_overtested_zone()
    f_late_entry_chase()
    f_poor_rr()
    f_volatility_news()
    f_psychology_matrix()
    print("All Module 8 figures written.")
