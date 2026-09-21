"""
figs_m6.py — Module 6 figures: Complete Trade Execution Blueprint.
Run: python3 figs_m6.py   (writes into ../images/)
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
# 1. The execution chain (flow diagram)
# ---------------------------------------------------------------------------
def f_execution_chain():
    fig, ax = cl.blank_canvas((13.5, 9.8),
        "Figure 6.1 — The Complete Execution Blueprint",
        "Eleven links. Each one only makes sense given the one before it. A break anywhere in the chain means no trade, not a smaller trade.")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    steps = [
        ("1", "4H analysis", cl.BLUE, 4),
        ("2", "1H context", cl.BLUE, 4),
        ("3", "Key S&R / supply / demand", cl.CYAN, 3),
        ("4", "Liquidity location", cl.CYAN, 3),
        ("5", "15M price interaction", cl.MUTED, 2),
        ("6", "15M confirmation", cl.ACCENT, 4),
        ("7", "Entry", cl.ACCENT, 4),
        ("8", "Structural stop", cl.PINK, 3),
        ("9", "Structural target", cl.PINK, 3),
        ("10", "Trade management", cl.PURP, 3),
        ("11", "Exit", cl.UP, 4),
    ]
    n = len(steps)
    y0, y1 = 94, 6
    ys = np.linspace(y0, y1, n)
    for i, ((num, text, col, wsz), y) in enumerate(zip(steps, ys)):
        ax.add_patch(mpatches.Circle((8, y), 2.6, facecolor=col, edgecolor="#0d1420",
                                      lw=1.2, zorder=4))
        ax.text(8, y, num, ha="center", va="center", fontsize=10.5, fontweight="bold",
                color="#0d1420", zorder=5)
        ax.text(15, y, text, ha="left", va="center", fontsize=12.6, color=cl.TXT,
                fontweight="bold" if wsz >= 4 else "normal", zorder=4)
        if i < n - 1:
            ax.plot([8, 8], [y - 2.7, ys[i + 1] + 2.7], color="#33415f", lw=1.6, zorder=1)

    def bracket(y_top, y_bot, label, col):
        ax.plot([2.2, 1.4, 1.4, 2.2], [y_top, y_top, y_bot, y_bot], color=col, lw=1.6, zorder=2)
        ax.text(0.6, (y_top + y_bot) / 2, label, rotation=90, ha="center", va="center",
                 fontsize=9.4, color=col, fontweight="bold")

    bracket(ys[0] + 2.9, ys[1] - 2.9, "4H/1H", cl.BLUE)
    bracket(ys[2] + 2.9, ys[3] - 2.9, "LOCATION", cl.CYAN)
    bracket(ys[4] + 2.9, ys[6] - 2.9, "15M EXECUTE", cl.ACCENT)
    bracket(ys[7] + 2.9, ys[8] - 2.9, "RISK", cl.PINK)
    bracket(ys[9] + 2.9, ys[10] - 2.9, "MANAGE/EXIT", cl.UP)

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    cl.save_flat(fig, path("m6_execution_chain.png"), pad=0.35)


# ---------------------------------------------------------------------------
# 2. Structural stop vs arbitrary stop
# ---------------------------------------------------------------------------
def f_stop_logic():
    fig, axes = cl.panel_fig(
        "Figure 6.2 — Structural Stop vs Arbitrary Stop",
        "Same entry, same account. Left: the stop sits beyond the structural point that invalidates the thesis. Right: the stop is chosen only to hit a target risk percentage, ignoring structure.",
        ncols=2, figsize=(15.6, 6.4))

    ax = axes[0]
    shape = cl.seg((10, -0.0060), (5, -0.0006), (6, 0.0034), (5, 0.0006))
    o, h, l, c = cl.series(seed=161, shape=shape, noise=0.00030, wick=0.00034, start=1.0910)
    cl.candles(ax, o, h, l, c)
    entry_i = 15
    entry_lvl = float(c[entry_i])
    sweep_low = float(min(l[9:16]))
    stop_lvl = sweep_low - 0.00018
    target_lvl = entry_lvl + (entry_lvl - stop_lvl) * 2.6
    cl.hline(ax, entry_lvl, cl.BLUE, label=f"entry {entry_lvl:.4f}", n=len(o) - 1, side="right", va="bottom")
    cl.hline(ax, stop_lvl, cl.DN, label=f"stop {stop_lvl:.4f}", n=len(o) - 1, side="right", va="top")
    cl.label_point(ax, 10, sweep_low, "beyond the swing low\nthat the thesis depends on", cl.DN, dx=2.2, dy=-0.0022, fs=8.3, ha="left", rad=-0.2)
    risk_pips = (entry_lvl - stop_lvl) * 10000
    cl.verdict(ax, f"Stop set by structure — {risk_pips:.0f} pips, wherever that lands", cl.UP, yy=0.04)
    cl.badge(ax, "STRUCTURAL STOP", cl.UP, loc="tr")
    cl.clean(ax, sub="Stop sits below the swing low the long thesis depends on.")
    ax.set_ylim(min(l) - 0.0040, max(h) + 0.0012)

    ax2 = axes[1]
    o2, h2, l2, c2 = o.copy(), h.copy(), l.copy(), c.copy()
    cl.candles(ax2, o2, h2, l2, c2)
    entry_lvl2 = float(c2[entry_i])
    arbitrary_stop = entry_lvl2 - 0.00040   # picked to "hit" a round pip risk, ignores the swing low
    cl.hline(ax2, entry_lvl2, cl.BLUE, label=f"entry {entry_lvl2:.4f}", n=len(o2) - 1, side="right", va="bottom")
    cl.hline(ax2, arbitrary_stop, cl.DN, label=f"stop {arbitrary_stop:.4f} (4 pips)", n=len(o2) - 1, side="right", va="top")
    cl.label_point(ax2, 10, sweep_low, "swing low sits\nbelow this stop —\nignored", cl.DN, dx=2.2, dy=-0.0022, fs=8.3, ha="left", rad=-0.2)
    cl.verdict(ax2, "Stop chosen to look like \u201clow risk\u201d — sits inside normal noise", cl.DN, yy=0.04)
    cl.badge(ax2, "ARBITRARY STOP", cl.DN, loc="tr")
    cl.clean(ax2, sub="4 pips, picked to feel comfortable \u2014 sits inside ordinary 15M noise.")
    ax2.set_ylim(min(l2) - 0.0040, max(h2) + 0.0012)

    fig.text(0.5, 0.015,
              "The right-hand stop ignores the swing low the thesis depends on \u2014 a normal retrace would stop it out for no structural reason.",
              fontsize=9.0, color=cl.MUTED, ha="center", va="bottom")
    cl.save(fig, path("m6_stop_logic.png"), rect=(0.012, 0.07, 0.99, 0.86))


# ---------------------------------------------------------------------------
# 3. Structural target vs manufactured target, the 1:2 gate
# ---------------------------------------------------------------------------
def f_target_logic():
    fig, axes = cl.panel_fig(
        "Figure 6.3 — Structural Target vs Manufactured Target",
        "The target must be the nearest genuine opposing structure. Stretching a target further to force a better ratio is not allowed, even when the arithmetic looks attractive.",
        ncols=2, figsize=(15.6, 6.4))

    ax = axes[0]
    shape = cl.seg((8, 0.0006), (4, 0.0044), (6, -0.0004), (5, 0.0058), (5, 0.0004))
    o, h, l, c = cl.series(seed=171, shape=shape, noise=0.00030, wick=0.00034, start=1.2620)
    cl.candles(ax, o, h, l, c)
    entry_i = 3
    entry_lvl = float(c[entry_i])
    stop_lvl = float(min(l[0:entry_i + 1])) - 0.00018
    # genuine opposing structure: the prior swing high before this leg started
    genuine_target = float(max(h[13:18]))
    rr = (genuine_target - entry_lvl) / (entry_lvl - stop_lvl)
    cl.hline(ax, entry_lvl, cl.BLUE, label=f"entry {entry_lvl:.4f}", n=len(o) - 1, side="right", va="bottom")
    cl.hline(ax, stop_lvl, cl.DN, label=f"stop {stop_lvl:.4f}", n=len(o) - 1, side="right", va="top")
    cl.hline(ax, genuine_target, cl.UP, label=f"target {genuine_target:.4f}", n=0, side="left", va="bottom")
    cl.label_point(ax, 15, genuine_target, "prior opposing\nswing high", cl.UP, dx=-4.0, dy=0.0020, fs=8.3, ha="right", rad=0.2)
    cl.verdict(ax, f"R:R \u2248 1:{rr:.1f} — genuine structure, qualifies", cl.UP, yy=0.10)
    cl.badge(ax, "STRUCTURAL TARGET", cl.UP, loc="tl")
    cl.clean(ax, sub="Target is the nearest real opposing structure \u2014 a prior swing high.")
    ax.set_ylim(min(l) - 0.0040, max(h) + 0.0020)

    ax2 = axes[1]
    o2, h2, l2, c2 = o.copy(), h.copy(), l.copy(), c.copy()
    cl.candles(ax2, o2, h2, l2, c2)
    entry_lvl2 = entry_lvl
    stop_lvl2 = stop_lvl
    manufactured_target = entry_lvl2 + (entry_lvl2 - stop_lvl2) * 4.5   # placed past all real structure
    rr2 = (manufactured_target - entry_lvl2) / (entry_lvl2 - stop_lvl2)
    cl.hline(ax2, entry_lvl2, cl.BLUE, label=f"entry {entry_lvl2:.4f}", n=0, side="left", va="bottom")
    cl.hline(ax2, stop_lvl2, cl.DN, label=f"stop {stop_lvl2:.4f}", n=0, side="left", va="top")
    cl.hline(ax2, genuine_target, cl.MUTED, label=None)
    cl.hline(ax2, manufactured_target, cl.DN, label=None)
    ax2.text(len(o2) - 1, genuine_target - 0.00035, "nearest real structure (unused)",
             fontsize=8.2, color=cl.MUTED, ha="right", va="top", fontweight="bold")
    ax2.text(len(o2) - 1, manufactured_target + 0.00012, f"target {manufactured_target:.4f} (empty air)",
             fontsize=8.2, color=cl.DN, ha="right", va="bottom", fontweight="bold")
    ymax2 = max(float(max(h2)), manufactured_target)
    cl.label_point(ax2, 8, manufactured_target, "no structure here \u2014\nchosen only to force 1:4.5", cl.DN, dx=1.5, dy=0.0010, fs=8.3, ha="left", rad=0.15)
    cl.verdict(ax2, f"R:R \u2248 1:{rr2:.1f} on paper \u2014 invalid, target is manufactured", cl.DN, yy=0.10)
    cl.badge(ax2, "MANUFACTURED TARGET", cl.DN, loc="tl")
    cl.clean(ax2, sub="No genuine opposing structure exists near this price \u2014 use the target on the left.")
    ax2.set_ylim(min(l2) - 0.0040, ymax2 + 0.0022)

    fig.text(0.5, 0.015,
              "Both stops are identical. Only the target differs \u2014 one uses the nearest real structure, the other stretches past it to manufacture a better-looking ratio.",
              fontsize=9.0, color=cl.MUTED, ha="center", va="bottom")
    cl.save(fig, path("m6_target_logic.png"), rect=(0.012, 0.07, 0.99, 0.86))


# ---------------------------------------------------------------------------
# 4. Position sizing worked math (two account sizes, same setup)
# ---------------------------------------------------------------------------
def f_position_sizing():
    fig, ax = cl.blank_canvas((13.8, 8.2),
        "Figure 6.4 — Position Sizing From a Structural Stop",
        "Same EURUSD setup, same 22-pip structural stop, two account sizes. Position size is solved backward from risk — never chosen first.")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    entry = 1.09120
    stop = 1.08900
    pips_risk = round((entry - stop) * 10000, 1)
    pip_value_standard_lot = 10.0  # USD per pip, 1.0 standard lot, USD-quote pair approx.

    accounts = [
        ("$10,000 account", 10000, 0.01, cl.BLUE),
        ("$50,000 account", 50000, 0.0075, cl.CYAN),
    ]

    col_x = [8, 52]
    for (label, bal, risk_pct, col), x0 in zip(accounts, col_x):
        risk_dollars = bal * risk_pct
        lots = risk_dollars / (pips_risk * pip_value_standard_lot)
        y = 82
        ax.add_patch(mpatches.FancyBboxPatch((x0, 8), 40, 78, boxstyle="round,pad=0.6",
                     facecolor="#0d1420", edgecolor=col, lw=1.4, zorder=2))
        ax.text(x0 + 2, y, label, fontsize=13.5, color=col, fontweight="bold", zorder=4)
        lines = [
            f"Account balance: ${bal:,.0f}",
            f"Risk per trade: {risk_pct*100:.2f}%  =  ${risk_dollars:,.2f}",
            f"Entry: {entry:.5f}",
            f"Structural stop: {stop:.5f}",
            f"Stop distance: {pips_risk:.1f} pips",
            f"Pip value (1.0 lot): ${pip_value_standard_lot:.2f}/pip",
            "",
            f"Position size = ${risk_dollars:,.2f} \u00f7 ({pips_risk:.1f} \u00d7 ${pip_value_standard_lot:.2f})",
            f"= {lots:.2f} standard lots",
        ]
        yy = y - 8
        for ln in lines:
            fw = "bold" if ln.startswith("= ") else "normal"
            fs = 10.6 if ln.startswith("= ") else 9.6
            ax.text(x0 + 2, yy, ln, fontsize=fs, color=cl.TXT if not ln.startswith("=") else col,
                    fontweight=fw, zorder=4)
            yy -= 6.6

    ax.text(8, 4, "The stop distance and entry never change with account size. Only the position size changes to keep dollar risk fixed. "
                   "A prop firm's own drawdown rules can require a lower risk-per-trade than shown here — never assume a single percentage is appropriate everywhere.",
            fontsize=9.0, color=cl.MUTED, ha="left", va="bottom")
    cl.save_flat(fig, path("m6_position_sizing.png"), pad=0.35)


# ---------------------------------------------------------------------------
# 5. R:R calculation — qualifying vs rejected, different instrument to M4
# ---------------------------------------------------------------------------
def f_rr_calc():
    fig, axes = cl.panel_fig(
        "Figure 6.5 — Reward-to-Risk as a Pass/Fail Gate",
        "Same stop distance, same instrument. Only the genuine distance to the nearest opposing structure differs \u2014 and that alone decides pass or fail.",
        ncols=2, figsize=(15.8, 6.4))

    ax = axes[0]
    shape = cl.seg((10, -0.42), (6, 0.05), (8, 0.98))
    o, h, l, c = cl.series(seed=181, shape=shape, noise=0.045, wick=0.05, start=17800.0)
    cl.candles(ax, o, h, l, c)
    entry_i = 15
    entry_lvl = float(c[entry_i])
    stop_lvl = float(min(l[9:16])) - 0.6
    target_lvl = entry_lvl + (entry_lvl - stop_lvl) * 2.9
    rr = (target_lvl - entry_lvl) / (entry_lvl - stop_lvl)
    cl.hline(ax, entry_lvl, cl.BLUE, label=f"entry {entry_lvl:.1f}", n=len(o) - 1, side="right", va="bottom")
    cl.hline(ax, stop_lvl, cl.DN, label=f"stop {stop_lvl:.1f}", n=len(o) - 1, side="right", va="top")
    cl.hline(ax, target_lvl, cl.UP, label=f"target {target_lvl:.1f}", n=0, side="left", va="bottom")
    cl.verdict(ax, f"R:R \u2248 1:{rr:.1f} \u2014 clears the 1:2 minimum", cl.UP, yy=0.03)
    cl.badge(ax, "QUALIFIES", cl.UP, loc="tl")
    cl.clean(ax, sub="NQ, NY session \u2014 target sits well beyond the 1:2 minimum.")
    ax.ticklabel_format(axis="y", useOffset=False, style="plain")
    ax.set_ylim(min(l) - 1.2, max(h) + 1.6)

    ax2 = axes[1]
    shape2 = cl.seg((10, -0.42), (6, 0.05), (8, 0.30))
    o2, h2, l2, c2 = cl.series(seed=182, shape=shape2, noise=0.045, wick=0.05, start=17800.0)
    cl.candles(ax2, o2, h2, l2, c2)
    entry_lvl2 = float(c2[entry_i])
    stop_lvl2 = stop_lvl
    target_lvl2 = float(max(h2[13:19]))  # a real but nearby prior high — genuine, but close
    rr2 = (target_lvl2 - entry_lvl2) / (entry_lvl2 - stop_lvl2)
    cl.hline(ax2, entry_lvl2, cl.BLUE, label=None)
    cl.hline(ax2, stop_lvl2, cl.DN, label=f"stop {stop_lvl2:.1f}", n=len(o2) - 1, side="right", va="top")
    cl.hline(ax2, target_lvl2, cl.UP, label=None)
    ax2.text(0, entry_lvl2 - 0.35, f"entry {entry_lvl2:.1f}", fontsize=8.6, color=cl.BLUE,
              ha="left", va="top", fontweight="bold")
    ax2.text(len(o2) - 1, target_lvl2 + 0.30, f"target {target_lvl2:.1f} (too close)", fontsize=8.6,
              color=cl.UP, ha="right", va="bottom", fontweight="bold")
    cl.verdict(ax2, f"R:R \u2248 1:{rr2:.1f} \u2014 below the 1:2 minimum, reject", cl.DN, yy=0.03)
    cl.badge(ax2, "REJECTED", cl.DN, loc="tl")
    cl.clean(ax2, sub="Same stop distance \u2014 nearest genuine structure sits too close. Stand aside.")
    ax2.ticklabel_format(axis="y", useOffset=False, style="plain")
    ax2.set_ylim(min(l2) - 1.2, max(h2) + 1.6)

    cl.save(fig, path("m6_rr_calc.png"))


# ---------------------------------------------------------------------------
# 6. Trade cancellation — setup invalidated before confirmation completes
# ---------------------------------------------------------------------------
def f_cancellation():
    fig, ax = plt.subplots(figsize=(13.6, 6.6))
    shape = cl.seg((9, -0.0006), (4, 0.0002), (3, -0.0034), (5, -0.0004))
    o, h, l, c = cl.series(seed=191, shape=shape, noise=0.00026, wick=0.00030, start=1.0845)
    cl.candles(ax, o, h, l, c)
    zlo = float(min(l[7:11]))
    zhi = float(max(h[7:11]))
    cl.zone(ax, 6.5, 10.5, zlo, zhi, cl.UP, label=None)
    ax.text(6.5, zhi + 0.00055, "1H demand \u2014 waiting for\n15M confirmation", fontsize=8.5, color=cl.UP,
            ha="left", va="bottom", fontweight="bold")
    fail_i = 13
    cl.label_point(ax, fail_i, l[fail_i], "15M closes below the zone\nbefore confirmation ever appeared", cl.DN, dx=2.6, dy=-0.0006, fs=8.6, ha="left", rad=-0.2)
    cl.verdict(ax, "Setup cancelled — the zone failed before an entry was ever taken", cl.DN, yy=0.03)
    cl.clean(ax, title="Figure 6.6 — Trade Cancellation Before Entry",
             sub="Price interacted with the zone (step 5) but never produced step 6 confirmation \u2014 it closed straight through instead. The setup is cancelled, not managed.",
             ts=13.4)
    ax.set_ylim(min(l) - 0.0012, max(h) + 0.0026)
    cl.save(fig, path("m6_cancellation.png"), rect=(0.012, 0.02, 0.99, 0.86))


# ---------------------------------------------------------------------------
# 7. Price moves without confirmation — do not chase
# ---------------------------------------------------------------------------
def f_no_chase():
    fig, ax = plt.subplots(figsize=(13.6, 6.6))
    shape = cl.seg((9, -0.0006), (3, 0.0003), (7, 0.0062))
    o, h, l, c = cl.series(seed=201, shape=shape, noise=0.00026, wick=0.00028, start=1.0845)
    cl.candles(ax, o, h, l, c)
    zlo = float(min(l[7:11]))
    zhi = float(max(h[7:11]))
    cl.zone(ax, 6.5, 10.5, zlo, zhi, cl.UP, label="1H demand", lblside="left", va="bottom")
    cl.label_point(ax, 11, l[11], "price only wicks the\nedge of the zone,\nnever confirms", cl.MUTED, dx=1.0, dy=-0.0028, fs=8.3, ha="left", rad=-0.15)
    cl.label_point(ax, 15, h[15], "then runs without you \u2014\nno 15M confirmation was ever given", cl.ACCENT, dx=-3.6, dy=0.0012, fs=8.3, ha="right", rad=0.2)
    cl.verdict(ax, "Correct response: no trade \u2014 the move is not evidence you were wrong to wait", cl.UP, yy=0.03)
    cl.clean(ax, title="Figure 6.7 — Price Runs Without Confirmation",
             sub="Step 6 (15M confirmation) never happened before price moved. Entering here means entering on hope \u2014 chasing recreates every risk the sequence exists to remove.",
             ts=13.4)
    ax.set_ylim(min(l) - 0.0040, max(h) + 0.0020)
    cl.save(fig, path("m6_no_chase.png"), rect=(0.012, 0.02, 0.99, 0.86))


# ---------------------------------------------------------------------------
# 8. Re-entry — valid pullback re-entry vs a chase re-entry
# ---------------------------------------------------------------------------
def f_reentry():
    fig, axes = cl.panel_fig(
        "Figure 6.8 — Re-Entry: Valid Pullback vs Chase",
        "The original entry was missed. Left: price returns to the same zone and re-confirms. Right: price is chased mid-leg, far from any zone.",
        ncols=2, figsize=(15.8, 6.6))

    ax = axes[0]
    shape = cl.seg((8, -0.0006), (4, 0.0038), (5, -0.0034), (5, 0.0044))
    o, h, l, c = cl.series(seed=211, shape=shape, noise=0.00026, wick=0.00030, start=1.0845)
    cl.candles(ax, o, h, l, c)
    zlo = float(min(l[10:14]))
    zhi = float(max(h[10:14]))
    cl.zone(ax, 9.5, 21, zlo, zhi, cl.UP, label="same 1H demand, re-tested", lblside="left", va="bottom")
    reentry_i = 17
    cl.label_point(ax, reentry_i, c[reentry_i], "second 15M confirmation\nat the same zone", cl.UP, dx=1.0, dy=0.0040, fs=8.3, ha="left", rad=0.2)
    cl.verdict(ax, "Valid re-entry \u2014 the zone itself produced a fresh confirmation", cl.UP, yy=0.03)
    cl.clean(ax, sub="Same zone, new independent confirmation \u2014 a fresh signal, not a chase.")
    ax.set_ylim(min(l) - 0.0034, max(h) + 0.0016)

    ax2 = axes[1]
    shape2 = cl.seg((8, -0.0006), (4, 0.0038), (10, 0.0058))
    o2, h2, l2, c2 = cl.series(seed=212, shape=shape2, noise=0.00026, wick=0.00030, start=1.0845)
    cl.candles(ax2, o2, h2, l2, c2)
    zlo2 = float(min(l2[10:14]))
    zhi2 = float(max(h2[10:14]))
    cl.zone(ax2, 9.5, 13.5, zlo2, zhi2, cl.UP, label="original zone \u2014 far below now", lblside="left", va="top")
    chase_i = 19
    cl.label_point(ax2, chase_i, c2[chase_i], "entered mid-leg,\nno zone, no fresh\nconfirmation here", cl.DN, dx=-2.4, dy=0.0018, fs=8.3, ha="right", rad=-0.2)
    cl.verdict(ax2, "Chase \u2014 no structure supports an entry at this price", cl.DN, yy=0.03)
    cl.clean(ax2, sub="Well past the original zone \u2014 no stop reference, no fresh confirmation. This is FOMO, delayed.")
    ax2.set_ylim(min(l2) - 0.0034, max(h2) + 0.0016)

    cl.save(fig, path("m6_reentry.png"))


if __name__ == "__main__":
    f_execution_chain()
    f_stop_logic()
    f_target_logic()
    f_position_sizing()
    f_rr_calc()
    f_cancellation()
    f_no_chase()
    f_reentry()
    print("All Module 6 figures written.")
