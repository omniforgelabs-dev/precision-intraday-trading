"""
figs_m4.py — Module 4 figures: The 15M Price-Action Entry Model.
Run: python3 figs_m4.py   (writes into ../images/)
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
# 1. The 13-step sequence (flow diagram)
# ---------------------------------------------------------------------------
def f_entry_sequence():
    fig, ax = cl.blank_canvas((13.5, 9.6),
        "Figure 4.1 — The Complete 15M Entry Sequence",
        "Thirteen steps from 4H bias to a qualified trade. Information flows down; the 15M can only veto, never authorise on its own.")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    steps = [
        ("1", "4H directional environment", cl.BLUE, 4),
        ("2", "1H context established", cl.BLUE, 4),
        ("3", "Meaningful 1H/4H location identified", cl.CYAN, 3),
        ("4", "Relevant liquidity identified", cl.CYAN, 3),
        ("5", "Wait: price interacts with the area", cl.MUTED, 2),
        ("6", "Liquidity event / structural reaction observed", cl.ACCENT, 3),
        ("7", "15M price-action confirmation", cl.ACCENT, 3),
        ("8", "15M structure shift / BOS (where applicable)", cl.ACCENT, 3),
        ("9", "Displacement identified (where applicable)", cl.ACCENT, 3),
        ("10", "Structural invalidation point defined", cl.PINK, 3),
        ("11", "Structural target defined", cl.PINK, 3),
        ("12", "Reward-to-risk calculated", cl.PINK, 3),
        ("13", "Trade qualifies — or it does not", cl.UP, 4),
    ]
    n = len(steps)
    y0, y1 = 94, 6
    ys = np.linspace(y0, y1, n)
    for i, ((num, text, col, wsz), y) in enumerate(zip(steps, ys)):
        ax.add_patch(mpatches.Circle((8, y), 2.6, facecolor=col, edgecolor="#0d1420",
                                      lw=1.2, zorder=4))
        ax.text(8, y, num, ha="center", va="center", fontsize=10.5, fontweight="bold",
                color="#0d1420", zorder=5)
        ax.text(15, y, text, ha="left", va="center", fontsize=12.4, color=cl.TXT,
                fontweight="bold" if wsz >= 4 else "normal", zorder=4)
        if i < n - 1:
            ax.plot([8, 8], [y - 2.7, ys[i + 1] + 2.7], color="#33415f", lw=1.6,
                     zorder=1)

    # side brackets grouping the phases
    def bracket(y_top, y_bot, label, col):
        ax.plot([2.2, 1.4, 1.4, 2.2], [y_top, y_top, y_bot, y_bot], color=col, lw=1.6,
                 zorder=2)
        ax.text(0.6, (y_top + y_bot) / 2, label, rotation=90, ha="center", va="center",
                 fontsize=9.6, color=col, fontweight="bold")

    bracket(ys[0] + 2.9, ys[1] - 2.9, "4H/1H", cl.BLUE)
    bracket(ys[2] + 2.9, ys[4] - 2.9, "LOCATION", cl.CYAN)
    bracket(ys[5] + 2.9, ys[8] - 2.9, "15M CONFIRM", cl.ACCENT)
    bracket(ys[9] + 2.9, ys[12] - 2.9, "RISK/DECISION", cl.PINK)

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    cl.save_flat(fig, path("m4_entry_sequence.png"), pad=0.35)


# ---------------------------------------------------------------------------
# 2. Long setup — full worked example, 1H context + 15M execution panel
# ---------------------------------------------------------------------------
def f_long_setup():
    fig, axes = cl.panel_fig(
        "Figure 4.2 — Full Long Sequence (EURUSD, London session)",
        "Left: 1H shows an uptrend pulling back into a demand zone with resting sell-side liquidity below it. Right: 15M confirms with a bullish structure shift, entry on the retest.",
        ncols=2, figsize=(15.8, 6.6))

    # LEFT — 1H, realistic EURUSD scale (~1.0850), pip-sized noise/wick
    ax = axes[0]
    shape = cl.seg((10, 0.0090), (8, -0.0048), (6, 0.0004), (4, -0.0040), (10, 0.0002))
    o, h, l, c = cl.series(seed=41, shape=shape, noise=0.00035, wick=0.00040, start=1.0860)
    cl.candles(ax, o, h, l, c)
    # demand zone: the pullback consolidation, indices 18-27 — edges read off the array
    zlo = float(min(l[18:28]))
    zhi = float(max(h[18:28]))
    cl.zone(ax, 17.5, 27.5, zlo, zhi, cl.UP, label=f"1H demand\n{zlo:.4f}\u2013{zhi:.4f}",
            lblside="left", va="top")
    sweep_low = float(min(l[24:27]))
    cl.hline(ax, sweep_low, cl.DN, label="sell-side liquidity", n=len(o) - 1, side="right", va="bottom")
    cl.label_point(ax, 26, l[26], "sweep + reclaim", cl.ACCENT, dx=3.5, dy=0.0016, fs=8.6, rad=-0.25)
    cl.badge(ax, "1H — CONTEXT & LOCATION", cl.BLUE, loc="tl")
    cl.clean(ax, sub="Uptrend intact: HH/HL structure. Pullback reaches the last 1H demand zone.")
    ax.set_ylim(min(l) - 0.0015, max(h) + 0.0015)

    # RIGHT — 15M zoomed execution window (last part of the pullback + entry)
    ax2 = axes[1]
    shape2 = cl.seg((8, -0.0016), (3, -0.0007), (5, 0.0002), (4, 0.0016), (6, 0.0010))
    o2, h2, l2, c2 = cl.series(seed=42, shape=shape2, noise=0.00028, wick=0.00032, start=1.0872)
    cl.candles(ax2, o2, h2, l2, c2)
    entry_i = 12
    stop_lvl = float(min(l2[9:13]))
    entry_lvl = float(c2[entry_i])
    target_lvl = entry_lvl + (entry_lvl - stop_lvl) * 2.3
    ymax_data = max(float(max(h2)), target_lvl)
    ymin_data = min(float(min(l2)), stop_lvl)
    cl.hline(ax2, entry_lvl, cl.BLUE, label=f"entry {entry_lvl:.4f}", n=len(o2) - 1, side="right", va="bottom")
    cl.hline(ax2, stop_lvl, cl.DN, label=f"stop {stop_lvl:.4f}", n=len(o2) - 1, side="right", va="top")
    cl.hline(ax2, target_lvl, cl.UP, label=f"target {target_lvl:.4f}", n=0, side="left", va="bottom")
    cl.label_point(ax2, 3, h2[3], "MSS: 15M\nhigher low breaks down\nstructure, then reclaims",
                    cl.ACCENT, dx=6.0, dy=0.0006, fs=8.2, ha="left", rad=0.15)
    cl.verdict(ax2, f"R:R \u2248 1:{(target_lvl-entry_lvl)/(entry_lvl-stop_lvl):.1f}  \u2014  qualifies", cl.UP, yy=0.03)
    cl.badge(ax2, "15M — CONFIRMATION & ENTRY", cl.ACCENT, loc="tl")
    cl.clean(ax2, sub="Sweep of the 1H liquidity, bullish 15M close back above the zone, structural stop below the sweep low.")
    ax2.set_ylim(ymin_data - 0.0008, ymax_data + 0.0022)

    cl.save(fig, path("m4_long_setup.png"))


# ---------------------------------------------------------------------------
# 3. Short setup — mirror worked example
# ---------------------------------------------------------------------------
def f_short_setup():
    fig, axes = cl.panel_fig(
        "Figure 4.3 — Full Short Sequence (GBPUSD, NY overlap)",
        "Left: 1H shows a downtrend rallying into a supply zone with resting buy-side liquidity above it. Right: 15M confirms with a bearish structure shift, entry on the retest.",
        ncols=2, figsize=(15.8, 6.6))

    ax = axes[0]
    shape = cl.seg((10, -0.0112), (8, 0.0058), (6, -0.0003), (4, 0.0048), (10, -0.0002))
    o, h, l, c = cl.series(seed=51, shape=shape, noise=0.00045, wick=0.00050, start=1.2680)
    cl.candles(ax, o, h, l, c)
    zlo = float(min(l[18:28]))
    zhi = float(max(h[18:28]))
    cl.zone(ax, 17.5, 27.5, zlo, zhi, cl.DN, label=f"1H supply\n{zlo:.4f}\u2013{zhi:.4f}",
            lblside="left", va="bottom")
    sweep_high = float(max(h[24:27]))
    cl.hline(ax, sweep_high, cl.UP, label="buy-side liquidity", n=0, side="left", va="bottom")
    cl.label_point(ax, 26, h[26], "sweep + reclaim", cl.ACCENT, dx=3.5, dy=-0.0022, fs=8.6, rad=0.25)
    cl.badge(ax, "1H — CONTEXT & LOCATION", cl.BLUE, loc="tl")
    cl.clean(ax, sub="Downtrend intact: LH/LL structure. Rally reaches the last 1H supply zone.")
    ax.set_ylim(min(l) - 0.0018, max(h) + 0.0018)

    ax2 = axes[1]
    shape2 = cl.seg((8, 0.0018), (3, 0.0008), (5, -0.0002), (4, -0.0018), (6, -0.0012))
    o2, h2, l2, c2 = cl.series(seed=52, shape=shape2, noise=0.00032, wick=0.00036, start=1.2668)
    cl.candles(ax2, o2, h2, l2, c2)
    entry_i = 12
    stop_lvl = float(max(h2[9:13]))
    entry_lvl = float(c2[entry_i])
    target_lvl = entry_lvl - (stop_lvl - entry_lvl) * 2.2
    ymax_data = max(float(max(h2)), stop_lvl)
    ymin_data = min(float(min(l2)), target_lvl)
    cl.hline(ax2, entry_lvl, cl.BLUE, label=f"entry {entry_lvl:.4f}", n=len(o2) - 1, side="right", va="top")
    cl.hline(ax2, stop_lvl, cl.DN, label=f"stop {stop_lvl:.4f}", n=len(o2) - 1, side="right", va="bottom")
    cl.hline(ax2, target_lvl, cl.UP, label=f"target {target_lvl:.4f}", n=len(o2) - 1, side="right", va="top")
    cl.label_point(ax2, 3, l2[3], "MSS: 15M\nlower high breaks up\nstructure, then reclaims",
                    cl.ACCENT, dx=6.0, dy=-0.0006, fs=8.2, ha="left", rad=-0.15)
    cl.verdict(ax2, f"R:R \u2248 1:{(entry_lvl-target_lvl)/(stop_lvl-entry_lvl):.1f}  \u2014  qualifies", cl.UP, yy=0.03)
    cl.badge(ax2, "15M — CONFIRMATION & ENTRY", cl.ACCENT, loc="tl")
    cl.clean(ax2, sub="Sweep of the 1H liquidity, bearish 15M close back below the zone, structural stop above the sweep high.")
    ax2.set_ylim(ymin_data - 0.0022, ymax_data + 0.0008)

    cl.save(fig, path("m4_short_setup.png"))


# ---------------------------------------------------------------------------
# 4. Confirmation quality — strong vs weak 15M close
# ---------------------------------------------------------------------------
def f_confirmation_quality():
    fig, axes = cl.panel_fig(
        "Figure 4.4 — Confirmation Quality: Strong Close vs Weak Close",
        "Same location, same liquidity sweep. What differs is how the 15M candle closes relative to its range \u2014 and that difference changes whether step 7 is satisfied.",
        ncols=2, figsize=(15.4, 6.2))

    ax = axes[0]
    shape = cl.seg((10, -0.5), (4, -0.35), (1, 0.62))
    o, h, l, c = cl.series(seed=61, shape=shape, noise=0.04, wick=0.045, start=100.0)
    # force the last candle to close strong near its high
    lastlow = float(l[-1])
    lasthigh = lastlow + 0.85
    o[-1] = lastlow + 0.10
    c[-1] = lasthigh - 0.06
    h[-1] = lasthigh
    l[-1] = lastlow
    cl.candles(ax, o, h, l, c)
    body_pct = (c[-1] - o[-1]) / (h[-1] - l[-1]) * 100
    close_pct_from_high = (h[-1] - c[-1]) / (h[-1] - l[-1]) * 100
    cl.label_point(ax, len(o) - 1, c[-1], f"close in top {100-close_pct_from_high:.0f}%\nof range",
                    cl.UP, dx=-3.6, dy=0.35, fs=8.4, ha="right", rad=-0.2)
    cl.verdict(ax, "STRONG — satisfies step 7", cl.UP, yy=0.03)
    cl.clean(ax, sub=f"Body \u2248 {body_pct:.0f}% of range, wick rejected below, close holds the high. Aggression is visible in the close.")
    ax.set_ylim(min(l) - 0.3, max(h) + 0.6)

    ax2 = axes[1]
    shape2 = cl.seg((10, -0.5), (4, -0.35), (1, 0.08))
    o2, h2, l2, c2 = cl.series(seed=62, shape=shape2, noise=0.04, wick=0.045, start=100.0)
    lastlow2 = float(l2[-1])
    lasthigh2 = lastlow2 + 0.85
    o2[-1] = lastlow2 + 0.30
    c2[-1] = lastlow2 + 0.42
    h2[-1] = lasthigh2
    l2[-1] = lastlow2
    cl.candles(ax2, o2, h2, l2, c2)
    cl.label_point(ax2, len(o2) - 1, c2[-1], "close near\nmid-range", cl.MUTED, dx=-3.6, dy=0.35, fs=8.4, ha="right", rad=-0.2)
    cl.verdict(ax2, "WEAK — does not satisfy step 7", cl.DN, yy=0.03)
    cl.clean(ax2, sub="Same sweep, but the candle closes in the middle of its range with a long upper wick. Indecision, not confirmation.")
    ax2.set_ylim(min(l2) - 0.3, max(h2) + 0.6)

    cl.save(fig, path("m4_confirmation_quality.png"))


# ---------------------------------------------------------------------------
# 5. Invalidation after entry
# ---------------------------------------------------------------------------
def f_invalidation():
    fig, ax = plt.subplots(figsize=(13.6, 7.0))
    shape = cl.seg((6, -0.4), (3, -0.3), (2, 0.5), (5, -0.15), (4, -0.85))
    o, h, l, c = cl.series(seed=71, shape=shape, noise=0.045, wick=0.05, start=100.4)
    cl.candles(ax, o, h, l, c)
    entry_i = 8
    entry_lvl = float(c[entry_i])
    stop_lvl = float(min(l[6:9])) - 0.05
    target_lvl = entry_lvl + (entry_lvl - stop_lvl) * 2.4
    cl.hline(ax, entry_lvl, cl.BLUE, label="entry", n=len(o) - 1, side="right", va="bottom")
    cl.hline(ax, stop_lvl, cl.DN, label="structural stop", n=0, side="left", va="top")
    cl.hline(ax, target_lvl, cl.UP, label="target (never reached)", n=0, side="left", va="top", alpha=0.45)
    cl.label_point(ax, 13, l[13], "structure breaks down\nbefore target \u2014 exit here,\nnot at the stop price",
                    cl.ACCENT, dx=2.5, dy=-0.62, fs=8.6, ha="left", rad=0.2)
    cl.verdict(ax, "Invalidated before the stop was hit — exit on structure, not on price alone", cl.DN, yy=0.03)
    cl.clean(ax, title="Figure 4.5 — Invalidation Is Structural, Not Just a Stop Price",
             sub="The position was correctly entered. A new lower low forms below the entry structure before the stop is touched — the thesis is void even though the stop order has not filled.",
             ts=13.5)
    ax.set_ylim(stop_lvl - 0.55, target_lvl + 0.3)
    cl.save(fig, path("m4_invalidation.png"), rect=(0.012, 0.02, 0.99, 0.86))


# ---------------------------------------------------------------------------
# 6. Stand-aside conditions
# ---------------------------------------------------------------------------
def f_stand_aside():
    fig, ax = plt.subplots(figsize=(13.6, 6.4))
    rng = np.random.RandomState(81)
    shape = cl.seg((30, 0.15))
    o, h, l, c = cl.series(seed=81, shape=shape, noise=0.10, wick=0.11, start=100.0)
    cl.candles(ax, o, h, l, c)
    band_hi = float(np.percentile(h, 82))
    band_lo = float(np.percentile(l, 18))
    cl.zone(ax, -0.5, len(o) - 0.5, band_lo, band_hi, cl.MUTED, label="range, no expansion", lblside="left", alpha=0.10, va="bottom")
    cl.verdict(ax, "No qualifying location, no displacement, no clean liquidity — stand aside", cl.MUTED, yy=0.03)
    cl.clean(ax, title="Figure 4.6 — When the Sequence Correctly Produces No Trade",
             sub="4H and 1H both show a wide, choppy range: no HH/HL or LH/LL structure, no origin zone, no displacement leg to define liquidity. Step 3 and step 4 never resolve, so the sequence ends here.")
    ax.set_ylim(min(l) - 0.3, max(h) + 0.3)
    cl.save(fig, path("m4_stand_aside.png"))


# ---------------------------------------------------------------------------
# 7. Minimum / strengthening / invalidating conditions table (visual card grid)
# ---------------------------------------------------------------------------
def f_condition_grid():
    fig, ax = cl.blank_canvas((13.8, 8.4),
        "Figure 4.7 — Minimum, Strengthening, and Invalidating Conditions",
        "The same 13-step sequence produces different verdicts depending on which conditions are present. None of these lists is exhaustive; all are structural, not a rigid checklist.")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    cols = [
        (3, 32.3, cl.ACCENT, "MINIMUM FOR VALIDITY", [
            "4H direction established\n(Gate 1)",
            "1H location with \u22652\ningredients",
            "Liquidity identified near\nthe location",
            "15M closes confirm the\nreaction",
            "Structural stop and target\nboth exist",
            "Honest R:R \u2265 1:2",
        ]),
        (35.9, 65.2, cl.UP, "STRENGTHENS THE SETUP", [
            "Zone is fresh (first or\nsecond test)",
            "Displacement leg\naccompanies the 15M shift",
            "Liquidity sweep precedes\nthe reaction",
            "4H, 1H, 15M zones are\nnested (\u00a73.8)",
            "Session favours the\ninstrument (\u00a74.9)",
            "R:R comfortably exceeds\n1:2",
        ]),
        (68.8, 97, cl.DN, "INVALIDATES / STAND ASIDE", [
            "4H and 1H direction\ndisagree",
            "Location has 0\u20131 ingredients\n(just a price)",
            "No liquidity nearby to\nreact against",
            "15M closes fail to confirm\n(wicks only)",
            "Structural stop cannot be\nplaced sensibly",
            "Genuine target gives < 1:2",
        ]),
    ]

    for x0, x1, col, title, items in cols:
        ax.add_patch(mpatches.FancyBboxPatch((x0, 4), x1 - x0, 88,
            boxstyle="round,pad=0.6,rounding_size=2.5", facecolor="#131a29",
            edgecolor=col, lw=1.6, zorder=2))
        ax.text((x0 + x1) / 2, 87, title, ha="center", va="top", fontsize=11.3,
                 color=col, fontweight="bold", zorder=3)
        y = 77
        for it in items:
            ax.text(x0 + 2.6, y, "\u2022", color=col, fontsize=13, ha="left", va="top", zorder=3)
            ax.text(x0 + 5.8, y, it, color=cl.TXT, fontsize=9.5, ha="left", va="top",
                     linespacing=1.5, zorder=3)
            y -= 13.0

    cl.save_flat(fig, path("m4_condition_grid.png"), pad=0.35)


# ---------------------------------------------------------------------------
# 8. R:R math — qualifying vs rejected purely on arithmetic
# ---------------------------------------------------------------------------
def f_rr_math():
    fig, axes = cl.panel_fig(
        "Figure 4.8 — Step 12/13 in Practice: Two Identical Setups, One Number Apart",
        "Both trades pass steps 1\u201311 identically. Only the distance to the genuine structural target differs \u2014 and that alone decides step 13.",
        ncols=2, figsize=(15.2, 6.0))

    ax = axes[0]
    entry, stop, target = 100.0, 99.55, 101.53
    risk = entry - stop
    reward = target - entry
    xs = [0, 1, 2]
    ax.plot([0, 2], [stop, stop], color=cl.DN, lw=2, ls="--")
    ax.plot([0, 2], [entry, entry], color=cl.BLUE, lw=2)
    ax.plot([0, 2], [target, target], color=cl.UP, lw=2, ls="--")
    ax.annotate("", xy=(1, entry), xytext=(1, stop),
                arrowprops=dict(arrowstyle="<->", color=cl.DN, lw=1.6))
    ax.annotate("", xy=(1.5, target), xytext=(1.5, entry),
                arrowprops=dict(arrowstyle="<->", color=cl.UP, lw=1.6))
    ax.text(1.05, (entry + stop) / 2, f"risk {risk:.2f}", color=cl.DN, fontsize=9.6, fontweight="bold")
    ax.text(1.55, (entry + target) / 2, f"reward {reward:.2f}", color=cl.UP, fontsize=9.6, fontweight="bold")
    cl.verdict(ax, f"R:R = 1:{reward/risk:.1f} — qualifies", cl.UP, yy=0.03)
    cl.clean(ax, sub=f"Structural stop {risk:.2f} below entry. Genuine next structural level sits {reward:.2f} above.")
    ax.set_xlim(0, 2)
    ax.set_ylim(stop - 0.3, target + 0.3)
    ax.set_xticks([])

    ax2 = axes[1]
    entry2, stop2, target2 = 100.0, 99.55, 100.63
    risk2 = entry2 - stop2
    reward2 = target2 - entry2
    ax2.plot([0, 2], [stop2, stop2], color=cl.DN, lw=2, ls="--")
    ax2.plot([0, 2], [entry2, entry2], color=cl.BLUE, lw=2)
    ax2.plot([0, 2], [target2, target2], color=cl.UP, lw=2, ls="--")
    ax2.annotate("", xy=(1, entry2), xytext=(1, stop2),
                 arrowprops=dict(arrowstyle="<->", color=cl.DN, lw=1.6))
    ax2.annotate("", xy=(1.5, target2), xytext=(1.5, entry2),
                 arrowprops=dict(arrowstyle="<->", color=cl.UP, lw=1.6))
    ax2.text(1.05, (entry2 + stop2) / 2, f"risk {risk2:.2f}", color=cl.DN, fontsize=9.6, fontweight="bold")
    ax2.text(1.55, (entry2 + target2) / 2, f"reward {reward2:.2f}", color=cl.UP, fontsize=9.6, fontweight="bold")
    cl.verdict(ax2, f"R:R = 1:{reward2/risk2:.1f} — rejected, not widened", cl.DN, yy=0.03)
    cl.clean(ax2, sub=f"Same stop distance. The nearest genuine structural level is only {reward2:.2f} away — do not manufacture a farther target.")
    ax2.set_xlim(0, 2)
    ax2.set_ylim(stop2 - 0.3, target - 0.3 + 0.6)
    ax2.set_xticks([])

    cl.save(fig, path("m4_rr_math.png"))


if __name__ == "__main__":
    f_entry_sequence()
    f_long_setup()
    f_short_setup()
    f_confirmation_quality()
    f_invalidation()
    f_stand_aside()
    f_condition_grid()
    f_rr_math()
    print("All Module 4 figures written.")
