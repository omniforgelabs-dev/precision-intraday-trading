"""
figs_m10.py — Module 10 figures: Complete Hypothetical Trade (long + short).
Run: python3 figs_m10.py   (writes into ../images/)
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


# ===========================================================================
# LONG EXAMPLE — EURUSD, London session
# ===========================================================================

def f_long_context():
    fig, axes = cl.panel_fig(
        "Figure 10.1 — Long Trade, Step 1\u20134: 4H Environment and 1H Location (EURUSD, London)",
        "Left: 4H shows a clean uptrend (HH/HL) establishing directional bias. Right: 1H pulls back into the last demand zone with resting sell-side liquidity below it.",
        ncols=2, figsize=(15.8, 6.6))

    ax = axes[0]
    shape = cl.seg((8, 0.0090), (6, -0.0030), (8, 0.0100), (6, -0.0028), (8, 0.0110))
    o, h, l, c = cl.series(seed=1001, shape=shape, noise=0.00050, wick=0.00060, start=1.0780)
    cl.candles(ax, o, h, l, c)
    cl.swing_marks(ax, [(5, "L", "HL"), (13, "H", "HH"), (19, "L", "HL"), (27, "H", "HH")],
                    h, l, col_hi=cl.UP, col_lo=cl.BLUE, dy_hi=0.0016, dy_lo=0.0016, fs=8.6)
    cl.badge(ax, "4H \u2014 DIRECTIONAL ENVIRONMENT", cl.BLUE, loc="tl")
    cl.verdict(ax, "Gate 1: 4H direction = LONG only", cl.UP, yy=0.04)
    cl.clean(ax, sub="Clean HH/HL sequence across the visible 4H structure \u2014 direction is unambiguous.")
    ax.set_ylim(min(l) - 0.0020, max(h) + 0.0020)

    ax2 = axes[1]
    shape2 = cl.seg((10, 0.0095), (8, -0.0052), (6, 0.0004), (4, -0.0044), (10, 0.0004))
    o2, h2, l2, c2 = cl.series(seed=1002, shape=shape2, noise=0.00035, wick=0.00040, start=1.0855)
    cl.candles(ax2, o2, h2, l2, c2)
    zlo = float(min(l2[18:28]))
    zhi = float(max(h2[18:28]))
    cl.zone(ax2, 17.5, 27.5, zlo, zhi, cl.UP, label=f"1H demand\n{zlo:.4f}\u2013{zhi:.4f}",
            lblside="left", va="top")
    sweep_low = float(min(l2[24:27]))
    cl.hline(ax2, sweep_low, cl.DN, label="sell-side liquidity", n=len(o2) - 1, side="right", va="bottom")
    cl.badge(ax2, "1H \u2014 CONTEXT & LOCATION", cl.CYAN, loc="tl")
    cl.verdict(ax2, "Location has 3 ingredients: origin + liquidity + flip \u2014 qualifies", cl.UP, yy=0.04)
    cl.clean(ax2, sub="Pullback reaches the last 1H demand zone; resting liquidity sits just below it.")
    ax2.set_ylim(min(l2) - 0.0018, max(h2) + 0.0018)

    cl.save(fig, path("m10_long_context.png"))


def f_long_execution():
    fig, axes = cl.panel_fig(
        "Figure 10.2 — Long Trade, Step 5\u201312: 15M Interaction, Confirmation, Entry",
        "Left: price sweeps the resting liquidity and interacts with the zone. Right: 15M bullish structure shift confirms; entry, structural stop, and structural target are all defined from price behaviour.",
        ncols=2, figsize=(15.8, 6.4))

    ax = axes[0]
    shape = cl.seg((10, -0.0020), (4, -0.0010), (3, 0.0006), (5, 0.0004))
    o, h, l, c = cl.series(seed=1003, shape=shape, noise=0.00022, wick=0.00026, start=1.0868)
    cl.candles(ax, o, h, l, c)
    sweep_i = 11
    sweep_low = float(min(l[9:13]))
    cl.hline(ax, sweep_low, cl.DN, label="sell-side liquidity swept", n=0, side="left", va="top")
    cl.label_point(ax, sweep_i, l[sweep_i], "liquidity event:\nsweep below the level,\nimmediate reclaim", cl.ACCENT, dx=3.0, dy=-0.0018, fs=8.4, ha="left", rad=-0.2)
    cl.badge(ax, "STEP 5\u20136 \u2014 INTERACTION & EVENT", cl.MUTED, loc="tl")
    cl.clean(ax, sub="Price interacts with the 1H zone and sweeps the resting liquidity below it before reclaiming.")
    ax.set_ylim(min(l) - 0.0012, max(h) + 0.0014)

    ax2 = axes[1]
    shape2 = cl.seg((8, -0.0016), (3, -0.0007), (5, 0.0002), (4, 0.0016), (6, 0.0022))
    o2, h2, l2, c2 = cl.series(seed=1004, shape=shape2, noise=0.00028, wick=0.00032, start=1.0872)
    cl.candles(ax2, o2, h2, l2, c2)
    entry_i = 12
    stop_lvl = float(min(l2[9:13]))
    entry_lvl = float(c2[entry_i])
    target_lvl = entry_lvl + (entry_lvl - stop_lvl) * 2.4
    rr = (target_lvl - entry_lvl) / (entry_lvl - stop_lvl)
    ymax_data = max(float(max(h2)), target_lvl)
    ymin_data = min(float(min(l2)), stop_lvl)
    cl.hline(ax2, entry_lvl, cl.BLUE, label=f"entry {entry_lvl:.4f}", n=len(o2) - 1, side="right", va="bottom")
    cl.hline(ax2, stop_lvl, cl.DN, label=f"stop {stop_lvl:.4f}", n=len(o2) - 1, side="right", va="top")
    cl.hline(ax2, target_lvl, cl.UP, label=f"target {target_lvl:.4f}", n=0, side="left", va="bottom")
    cl.label_point(ax2, 3, h2[3], "MSS: 15M higher\nlow breaks down,\nthen reclaims", cl.ACCENT, dx=5.0, dy=0.0006, fs=8.2, ha="left", rad=0.15)
    cl.verdict(ax2, f"R:R \u2248 1:{rr:.1f} \u2014 qualifies (\u22651:2)", cl.UP, yy=0.03)
    cl.badge(ax2, "STEP 7\u201312 \u2014 CONFIRM, ENTER, STOP, TARGET", cl.ACCENT, loc="tl")
    cl.clean(ax2, sub="Bullish 15M close reclaims the sweep low; stop sits beyond the sweep, target at the next 1H opposing structure.")
    ax2.set_ylim(ymin_data - 0.0010, ymax_data + 0.0022)

    cl.save(fig, path("m10_long_execution.png"))
    return dict(entry=entry_lvl, stop=stop_lvl, target=target_lvl, rr=rr)


def f_long_management():
    fig, ax = plt.subplots(figsize=(13.8, 6.8))
    shape = cl.seg((3, 0.0004), (5, 0.0022), (4, -0.0009), (5, 0.0024), (4, -0.0008), (6, 0.0026))
    o, h, l, c = cl.series(seed=1005, shape=shape, noise=0.00020, wick=0.00022, start=1.0872)
    cl.candles(ax, o, h, l, c)
    entry_i = 2
    entry_lvl = float(c[entry_i])
    stop1 = float(min(l[0:3])) - 0.00015
    swing1 = float(min(l[6:9]))
    swing2 = float(min(l[15:18]))
    target_lvl = entry_lvl + (entry_lvl - stop1) * 2.4

    cl.hline(ax, entry_lvl, cl.BLUE, label=f"entry {entry_lvl:.4f}", n=0, side="left", va="bottom")
    cl.hline(ax, stop1, cl.DN, label=f"initial stop {stop1:.4f}", n=0, side="left", va="bottom")
    ax.plot([8, 17], [swing1, swing1], color=cl.ACCENT, lw=1.5, ls="--")
    ax.text(8.2, swing1 - 0.00020, f"stop trailed to {swing1:.4f} after leg 1 confirms", color=cl.ACCENT, fontsize=8.2, va="top", ha="left", fontweight="bold")
    ax.plot([17, len(o) - 1], [swing2, swing2], color=cl.ACCENT, lw=1.5, ls="--")
    ax.text(17.2, swing2 - 0.00020, f"stop trailed to {swing2:.4f} after leg 2 confirms", color=cl.ACCENT, fontsize=8.2, va="top", ha="left", fontweight="bold")
    cl.hline(ax, target_lvl, cl.UP, label=f"target {target_lvl:.4f} \u2014 reached", n=len(o) - 1, side="right", va="bottom")

    cl.verdict(ax, "Momentum intact \u2014 left alone, then trailed behind each new confirmed swing \u2014 exits at target", cl.UP, yy=0.03)
    cl.clean(ax, title="Figure 10.3 — Long Trade, Management Through Exit",
             sub="Neither pullback breaks the newest confirmed structure, so the stop is trailed (\u00a77.7), not tightened on the wiggle. Price reaches the target.",
             ts=13.4)
    ax.set_ylim(min(float(min(l)), stop1) - 0.0022, max(float(max(h)), target_lvl) + 0.0020)
    cl.save(fig, path("m10_long_management.png"), rect=(0.012, 0.02, 0.99, 0.855))


# ===========================================================================
# SHORT EXAMPLE — NQ (Nasdaq-100 futures), NY cash session
# ===========================================================================

def f_short_context():
    fig, axes = cl.panel_fig(
        "Figure 10.4 — Short Trade, Step 1\u20134: 4H Environment and 1H Location (NQ, NY session)",
        "Left: 4H shows a clean downtrend (LH/LL) establishing directional bias. Right: 1H rallies into the last supply zone with resting buy-side liquidity above it.",
        ncols=2, figsize=(15.8, 6.6))

    ax = axes[0]
    shape = cl.seg((8, -95), (6, 32), (8, -105), (6, 30), (8, -110))
    o, h, l, c = cl.series(seed=1011, shape=shape, noise=5.5, wick=6.5, start=18420.0)
    cl.candles(ax, o, h, l, c)
    cl.swing_marks(ax, [(5, "H", "LH"), (13, "L", "LL"), (19, "H", "LH"), (27, "L", "LL")],
                    h, l, col_hi=cl.UP, col_lo=cl.DN, dy_hi=18, dy_lo=18, fs=8.6)
    cl.badge(ax, "4H \u2014 DIRECTIONAL ENVIRONMENT", cl.BLUE, loc="tl")
    cl.verdict(ax, "Gate 1: 4H direction = SHORT only", cl.DN, yy=0.04)
    cl.clean(ax, sub="Clean LH/LL sequence across the visible 4H structure \u2014 direction is unambiguous.")
    ax.ticklabel_format(axis="y", useOffset=False, style="plain")
    ax.set_ylim(min(l) - 30, max(h) + 30)

    ax2 = axes[1]
    shape2 = cl.seg((10, -102), (8, 58), (6, -3), (4, 46), (10, -3))
    o2, h2, l2, c2 = cl.series(seed=1012, shape=shape2, noise=4.5, wick=5.0, start=18250.0)
    cl.candles(ax2, o2, h2, l2, c2)
    zlo = float(min(l2[18:28]))
    zhi = float(max(h2[18:28]))
    cl.zone(ax2, 17.5, 27.5, zlo, zhi, cl.DN, label=f"1H supply\n{zlo:.0f}\u2013{zhi:.0f}",
            lblside="left", va="bottom")
    sweep_high = float(max(h2[24:27]))
    cl.hline(ax2, sweep_high, cl.UP, label="buy-side liquidity", n=0, side="left", va="bottom")
    cl.badge(ax2, "1H \u2014 CONTEXT & LOCATION", cl.CYAN, loc="tl")
    cl.verdict(ax2, "Location has 3 ingredients: origin + liquidity + flip \u2014 qualifies", cl.DN, yy=0.04)
    cl.clean(ax2, sub="Rally reaches the last 1H supply zone; resting liquidity sits just above it.")
    ax2.ticklabel_format(axis="y", useOffset=False, style="plain")
    ax2.set_ylim(min(l2) - 25, max(h2) + 25)

    cl.save(fig, path("m10_short_context.png"))


def f_short_execution():
    fig, axes = cl.panel_fig(
        "Figure 10.5 — Short Trade, Step 5\u201312: 15M Interaction, Confirmation, Entry",
        "Left: price sweeps the resting liquidity above the supply zone. Right: 15M bearish structure shift confirms; entry, structural stop, and structural target are all defined from price behaviour.",
        ncols=2, figsize=(15.8, 6.4))

    ax = axes[0]
    shape = cl.seg((10, 18), (4, 9), (3, -6), (5, -4))
    o, h, l, c = cl.series(seed=1013, shape=shape, noise=3.4, wick=4.0, start=18300.0)
    cl.candles(ax, o, h, l, c)
    sweep_i = 11
    sweep_high = float(max(h[9:13]))
    cl.hline(ax, sweep_high, cl.UP, label="buy-side liquidity swept", n=0, side="left", va="bottom")
    cl.label_point(ax, sweep_i, h[sweep_i], "liquidity event:\nsweep above the level,\nimmediate reclaim", cl.ACCENT, dx=3.0, dy=16, fs=8.4, ha="left", rad=0.2)
    cl.badge(ax, "STEP 5\u20136 \u2014 INTERACTION & EVENT", cl.MUTED, loc="tl")
    cl.clean(ax, sub="Price interacts with the 1H zone and sweeps the resting liquidity above it before reclaiming.")
    ax.ticklabel_format(axis="y", useOffset=False, style="plain")
    ax.set_ylim(min(l) - 14, max(h) + 14)

    ax2 = axes[1]
    shape2 = cl.seg((8, 16), (3, 7), (5, -2), (4, -18), (6, -25))
    o2, h2, l2, c2 = cl.series(seed=1014, shape=shape2, noise=3.6, wick=4.2, start=18280.0)
    cl.candles(ax2, o2, h2, l2, c2)
    entry_i = 12
    stop_lvl = float(max(h2[9:13]))
    entry_lvl = float(c2[entry_i])
    target_lvl = entry_lvl - (stop_lvl - entry_lvl) * 2.3
    rr = (entry_lvl - target_lvl) / (stop_lvl - entry_lvl)
    ymax_data = max(float(max(h2)), stop_lvl)
    ymin_data = min(float(min(l2)), target_lvl)
    cl.hline(ax2, entry_lvl, cl.BLUE, label=f"entry {entry_lvl:.0f}", n=len(o2) - 1, side="right", va="top")
    cl.hline(ax2, stop_lvl, cl.DN, label=f"stop {stop_lvl:.0f}", n=len(o2) - 1, side="right", va="bottom")
    cl.hline(ax2, target_lvl, cl.UP, label=f"target {target_lvl:.0f}", n=len(o2) - 1, side="right", va="top")
    cl.label_point(ax2, 3, l2[3], "MSS: 15M lower\nhigh breaks up,\nthen reclaims", cl.ACCENT, dx=5.0, dy=-8, fs=8.2, ha="left", rad=-0.15)
    cl.verdict(ax2, f"R:R \u2248 1:{rr:.1f} \u2014 qualifies (\u22651:2)", cl.DN, yy=0.03)
    cl.badge(ax2, "STEP 7\u201312 \u2014 CONFIRM, ENTER, STOP, TARGET", cl.ACCENT, loc="tl")
    cl.clean(ax2, sub="Bearish 15M close reclaims the sweep high; stop sits beyond the sweep, target at the next 1H opposing structure.")
    ax2.ticklabel_format(axis="y", useOffset=False, style="plain")
    ax2.set_ylim(ymin_data - 14, ymax_data + 16)

    cl.save(fig, path("m10_short_execution.png"))
    return dict(entry=entry_lvl, stop=stop_lvl, target=target_lvl, rr=rr)


def f_short_management():
    fig, ax = plt.subplots(figsize=(13.8, 6.8))
    shape = cl.seg((3, -3), (5, -20), (4, 6), (5, -24), (4, 6), (6, -28))
    o, h, l, c = cl.series(seed=1015, shape=shape, noise=2.6, wick=2.9, start=18280.0)
    cl.candles(ax, o, h, l, c)
    entry_i = 2
    entry_lvl = float(c[entry_i])
    stop1 = float(max(h[0:3])) + 1.2
    swing1 = float(max(h[6:9]))
    swing2 = float(max(h[15:18]))
    target_lvl = entry_lvl - (stop1 - entry_lvl) * 2.3

    cl.hline(ax, entry_lvl, cl.BLUE, label=f"entry {entry_lvl:.0f}", n=len(o) - 1, side="right", va="bottom")
    cl.hline(ax, stop1, cl.DN, label=f"initial stop {stop1:.0f}", n=0, side="left", va="bottom")
    ax.plot([8, 17], [swing1, swing1], color=cl.ACCENT, lw=1.5, ls="--")
    ax.text(8.2, swing1 + 0.6, f"stop trailed to {swing1:.0f} after leg 1 confirms", color=cl.ACCENT, fontsize=8.2, va="bottom", ha="left", fontweight="bold")
    ax.plot([17, len(o) - 1], [swing2, swing2], color=cl.ACCENT, lw=1.5, ls="--")
    ax.text(17.2, swing2 + 0.6, f"stop trailed to {swing2:.0f} after leg 2 confirms", color=cl.ACCENT, fontsize=8.2, va="bottom", ha="left", fontweight="bold")
    cl.hline(ax, target_lvl, cl.UP, label=f"target {target_lvl:.0f} \u2014 reached", n=len(o) - 1, side="right", va="top")

    cl.verdict(ax, "Momentum intact \u2014 left alone, then trailed behind each new confirmed swing \u2014 exits at target", cl.DN, yy=0.04)
    cl.clean(ax, title="Figure 10.6 — Short Trade, Management Through Exit",
             sub="Neither pullback breaks the newest confirmed structure, so the stop is trailed (\u00a77.7), not tightened on the wiggle. Price reaches the target.",
             ts=13.4)
    ax.ticklabel_format(axis="y", useOffset=False, style="plain")
    ax.set_ylim(min(float(min(l)), target_lvl) - 3, max(float(max(h)), stop1) + 4)
    cl.save(fig, path("m10_short_management.png"), rect=(0.012, 0.02, 0.99, 0.855))


# ===========================================================================
# Shared closing figures
# ===========================================================================

def f_invalidation_comparison():
    fig, axes = cl.panel_fig(
        "Figure 10.7 — What Would Have Invalidated Each Trade",
        "Neither invalidation occurred in the worked examples above \u2014 both show the specific structural break that would have ended the trade early, exactly as Module 4 (\u00a74.10) and Module 7 (\u00a77.5) define it.",
        ncols=2, figsize=(15.6, 6.2))

    ax = axes[0]
    shape = cl.seg((3, 0.0004), (5, 0.0010), (4, -0.0038))
    o, h, l, c = cl.series(seed=1021, shape=shape, noise=0.00022, wick=0.00024, start=1.0872)
    cl.candles(ax, o, h, l, c)
    entry_lvl = float(c[2])
    invalidation_lvl = float(min(l[0:3])) - 0.00015
    cl.hline(ax, entry_lvl, cl.BLUE, label=f"entry {entry_lvl:.4f}", n=0, side="left", va="bottom")
    cl.hline(ax, invalidation_lvl, cl.DN, label="structural invalidation", n=0, side="left", va="top")
    cl.verdict(ax, "Long: a 15M close below the sweep low would have invalidated the thesis", cl.DN, yy=0.10)
    cl.clean(ax, sub="Hypothetical \u2014 shown for illustration, not what actually occurred in Figure 10.3.")
    ax.set_ylim(invalidation_lvl - 0.0026, max(h) + 0.0012)

    ax2 = axes[1]
    shape2 = cl.seg((3, -3), (5, -12), (4, 42))
    o2, h2, l2, c2 = cl.series(seed=1022, shape=shape2, noise=3.2, wick=3.6, start=18280.0)
    cl.candles(ax2, o2, h2, l2, c2)
    entry_lvl2 = float(c2[2])
    invalidation_lvl2 = float(max(h2[0:3])) + 1.2
    cl.hline(ax2, entry_lvl2, cl.BLUE, label=f"entry {entry_lvl2:.0f}", n=0, side="left", va="top")
    cl.hline(ax2, invalidation_lvl2, cl.UP, label="structural invalidation", n=0, side="left", va="bottom")
    cl.verdict(ax2, "Short: a 15M close above the sweep high would have invalidated the thesis", cl.UP, yy=0.05)
    cl.clean(ax2, sub="Hypothetical \u2014 shown for illustration, not what actually occurred in Figure 10.6.")
    ax2.ticklabel_format(axis="y", useOffset=False, style="plain")
    ax2.set_ylim(min(l2) - 10, invalidation_lvl2 + 22)

    cl.save(fig, path("m10_invalidation_comparison.png"))


def f_final_results_summary(long_data, short_data):
    fig, ax = cl.blank_canvas((13.8, 8.8),
        "Figure 10.8 — Final Result Summary, Both Trades",
        "Illustrative outcomes only \u2014 a properly qualified setup can still lose (Module 1); these results demonstrate the mechanics, not a guarantee.")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    long_rr = long_data["rr"]
    short_rr = short_data["rr"]
    bal = 20000.0
    risk_pct = 0.0075
    risk_dollars = bal * risk_pct

    cols = [
        ("LONG \u2014 EURUSD, London", cl.UP, [
            f"Entry: {long_data['entry']:.4f}    Stop: {long_data['stop']:.4f}    Target: {long_data['target']:.4f}",
            f"R:R \u2248 1:{long_rr:.1f}  (qualifies, \u22651:2)",
            f"Account: USD {bal:,.0f}   Risk: {risk_pct*100:.2f}% = USD {risk_dollars:,.2f}",
            f"Result: target reached \u2014 gain \u2248 +{long_rr:.1f}R = USD {risk_dollars*long_rr:,.2f}",
            "Management: left alone through 2 pullbacks, stop trailed",
            "behind each new confirmed swing (\u00a77.7), no time-based exit",
        ]),
        ("SHORT \u2014 NQ, NY session", cl.DN, [
            f"Entry: {short_data['entry']:.0f}    Stop: {short_data['stop']:.0f}    Target: {short_data['target']:.0f}",
            f"R:R \u2248 1:{short_rr:.1f}  (qualifies, \u22651:2)",
            f"Account: USD {bal:,.0f}   Risk: {risk_pct*100:.2f}% = USD {risk_dollars:,.2f}",
            f"Result: target reached \u2014 gain \u2248 +{short_rr:.1f}R = USD {risk_dollars*short_rr:,.2f}",
            "Management: left alone through 2 pullbacks, stop trailed",
            "behind each new confirmed swing (\u00a77.7), no time-based exit",
        ]),
    ]
    y0 = [52, 52]
    for (title, col, lines), x0 in zip(cols, [3, 52]):
        ax.add_patch(mpatches.FancyBboxPatch((x0, 40), 45, 46, boxstyle="round,pad=0.6",
                     facecolor="#0d1420", edgecolor=col, lw=1.5, zorder=2))
        ax.text(x0 + 2.5, 82, title, fontsize=13.0, color=col, fontweight="bold", zorder=4)
        yy = 73
        for ln in lines:
            fw = "bold" if ln.startswith("Result") else "normal"
            ax.text(x0 + 2.5, yy, ln, fontsize=8.9, color=cl.TXT, fontweight=fw, zorder=4)
            yy -= 6.2

    ax.add_patch(mpatches.FancyBboxPatch((3, 6), 94, 28, boxstyle="round,pad=0.6",
                 facecolor="#0d1420", edgecolor=cl.ACCENT, lw=1.6, zorder=2))
    ax.text(50, 28, "Both trades were sized independently from account balance and structural stop distance (Module 9, \u00a79.1) \u2014",
            ha="center", va="top", fontsize=9.6, color=cl.TXT, zorder=4)
    ax.text(50, 21, "position size never determined direction or entry, and neither trade's target was manufactured to hit a number (Module 6, \u00a76.3).",
            ha="center", va="top", fontsize=9.6, color=cl.TXT, zorder=4)
    ax.text(50, 12, "A structurally qualified trade is a well-defined, risk-controlled opportunity \u2014 never a certainty. See Module 1's probability framework.",
            ha="center", va="top", fontsize=9.2, color=cl.ACCENT, fontweight="bold", zorder=4)

    cl.save_flat(fig, path("m10_final_results_summary.png"), pad=0.35)


if __name__ == "__main__":
    f_long_context()
    long_data = f_long_execution()
    f_long_management()
    f_short_context()
    short_data = f_short_execution()
    f_short_management()
    f_invalidation_comparison()
    f_final_results_summary(long_data, short_data)
    print("All Module 10 figures written.")
