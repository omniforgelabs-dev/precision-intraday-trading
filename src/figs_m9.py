"""
figs_m9.py — Module 9 figures: Prop-Firm Risk Management.
Run: python3 figs_m9.py   (writes into ../images/)
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
# 1. Risk-per-trade sizing across three different stop distances
# ---------------------------------------------------------------------------
def f_sizing_by_stop():
    fig, ax = cl.blank_canvas((13.8, 8.4),
        "Figure 9.1 — Position Size Changes With Stop Distance, Risk Stays Fixed",
        "Same $25,000 account, same 1.00% risk per trade, three different structural stop distances. Dollar risk never changes — only the lot size solves for it.")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    bal = 25000.0
    risk_pct = 0.01
    risk_dollars = bal * risk_pct
    pip_value = 10.0  # USD per pip, 1.0 standard lot

    cases = [
        ("Tight stop \u2014 8 pips", 8.0, cl.UP),
        ("Normal stop \u2014 18 pips", 18.0, cl.CYAN),
        ("Wide stop \u2014 35 pips", 35.0, cl.PINK),
    ]
    col_x = [3, 36, 69]
    for (label, pips, col), x0 in zip(cases, col_x):
        lots = risk_dollars / (pips * pip_value)
        ax.add_patch(mpatches.FancyBboxPatch((x0, 8), 28, 80, boxstyle="round,pad=0.6",
                     facecolor="#0d1420", edgecolor=col, lw=1.4, zorder=2))
        ax.text(x0 + 2, 82, label, fontsize=11.8, color=col, fontweight="bold", zorder=4)
        lines = [
            f"Stop distance: {pips:.0f} pips",
            f"Risk per trade: {risk_pct*100:.2f}%",
            f"= ${risk_dollars:,.2f}",
            "",
            f"Lots = ${risk_dollars:,.0f} \u00f7",
            f"({pips:.0f} \u00d7 ${pip_value:.0f})",
            f"= {lots:.2f} lots",
        ]
        yy = 73
        for ln in lines:
            fw = "bold" if ln.startswith("=") else "normal"
            fs = 10.4 if ln.startswith("=") else 9.4
            ax.text(x0 + 2, yy, ln, fontsize=fs, color=cl.TXT if not ln.startswith("=") else col,
                    fontweight=fw, zorder=4)
            yy -= 8.4

    ax.text(3, 3.5, "The tighter stop allows a larger position for identical dollar risk; the wider stop forces a smaller one. Dollar risk — never lot size — is the fixed input.",
            fontsize=9.0, color=cl.MUTED, ha="left", va="bottom")
    cl.save_flat(fig, path("m9_sizing_by_stop.png"), pad=0.35)


# ---------------------------------------------------------------------------
# 2. Daily loss limit — approaching vs breaching
# ---------------------------------------------------------------------------
def f_daily_loss_limit():
    fig, ax = plt.subplots(figsize=(13.6, 6.6))
    trades = [-0.8, -0.7, +1.6, -0.9, -0.6]
    cum = np.cumsum(trades)
    x = np.arange(1, len(trades) + 1)
    daily_limit = -3.0
    colors = [cl.DN if t < 0 else cl.UP for t in trades]
    ax.bar(x, trades, color=colors, width=0.5, zorder=3)
    ax.plot([0.4, len(trades) + 0.6], [0, 0], color=cl.MUTED, lw=1.0, zorder=2)
    ax.axhline(daily_limit, color=cl.DN, lw=1.8, ls="--", alpha=0.9, zorder=2)
    ax.text(len(trades) + 0.55, daily_limit, f"daily loss limit {daily_limit:.1f}%", color=cl.DN,
            fontsize=9.6, ha="right", va="bottom", fontweight="bold")
    for i, (xi, c) in enumerate(zip(x, cum)):
        ax.text(xi, trades[i] + (0.12 if trades[i] >= 0 else -0.12), f"cum {c:+.1f}%",
                color=cl.TXT, fontsize=8.6, ha="center", va="bottom" if trades[i] >= 0 else "top")
    ax.axvline(4.5, color=cl.ACCENT, lw=1.4, ls=":", alpha=0.8)
    ax.text(4.5, 1.9, "cumulative loss now\nwithin 1 trade's risk\nof the daily limit \u2014\nstop for the day", color=cl.ACCENT,
            fontsize=8.8, ha="center", va="top", fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels([f"Trade {i}" for i in x])
    ax.set_ylabel("Result (% of account)", color=cl.MUTED, fontsize=10)
    cl.clean(ax, title="Figure 9.2 — Respecting a Daily Loss Limit",
             sub="After trade 4, cumulative loss sits at -2.4% \u2014 one more full loss breaches the -3.0% daily limit. Trading stops for the day here.",
             ts=13.5)
    ax.set_ylim(-3.6, 2.4)
    cl.save(fig, path("m9_daily_loss_limit.png"), rect=(0.012, 0.02, 0.99, 0.84))


# ---------------------------------------------------------------------------
# 3. Max drawdown and consecutive-loss risk reduction
# ---------------------------------------------------------------------------
def f_drawdown_reduction():
    fig, axes = cl.panel_fig(
        "Figure 9.3 — Consecutive Losses and Scheduled Risk Reduction",
        "Left: risk per trade stays fixed through a losing streak, drawdown accelerates. Right: the same streak with a pre-defined risk-reduction rule after 3 consecutive losses, drawdown decelerates.",
        ncols=2, figsize=(15.6, 6.4))

    ax = axes[0]
    losses = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    equity = 100 + np.cumsum([0] + losses)
    x = np.arange(len(equity))
    ax.plot(x, equity, color=cl.DN, lw=2.2, marker="o", markersize=5, zorder=3)
    ax.axhline(94, color=cl.ACCENT, lw=1.4, ls="--", alpha=0.8)
    ax.text(len(equity) - 1, 94, "max drawdown limit \u2014 6%", color=cl.ACCENT, fontsize=9, ha="right", va="bottom", fontweight="bold")
    cl.verdict(ax, "Fixed 1.0% risk through the streak \u2014 6 losses reaches the limit", cl.DN, yy=0.05)
    cl.clean(ax, sub="Six consecutive losses at constant risk consume the full drawdown allowance.")
    ax.set_ylim(93, 101)
    ax.set_xticks(x)
    ax.set_xlabel("Trades", color=cl.MUTED, fontsize=9.5)

    ax2 = axes[1]
    risks2 = [-1.0, -1.0, -1.0, -0.5, -0.5, -0.5]
    equity2 = 100 + np.cumsum([0] + risks2)
    x2 = np.arange(len(equity2))
    ax2.plot(x2, equity2, color=cl.UP, lw=2.2, marker="o", markersize=5, zorder=3)
    ax2.axhline(94, color=cl.ACCENT, lw=1.4, ls="--", alpha=0.8)
    ax2.text(len(equity2) - 1, 94, "max drawdown limit \u2014 6%", color=cl.ACCENT, fontsize=9, ha="right", va="bottom", fontweight="bold")
    ax2.axvline(3, color=cl.CYAN, lw=1.3, ls=":", alpha=0.8)
    ax2.text(3, 98.2, "risk halved after\n3 consecutive losses", color=cl.CYAN, fontsize=8.6, ha="center", va="bottom", fontweight="bold")
    cl.verdict(ax2, "Risk reduced to 0.5% after 3 losses \u2014 same streak, smaller drawdown", cl.UP, yy=0.05)
    cl.clean(ax2, sub="A pre-defined rule, not a reactive feeling, cuts risk in half after the third consecutive loss.")
    ax2.set_ylim(93, 101)
    ax2.set_xticks(x2)
    ax2.set_xlabel("Trades", color=cl.MUTED, fontsize=9.5)

    cl.save(fig, path("m9_drawdown_reduction.png"))


# ---------------------------------------------------------------------------
# 4. Max simultaneous exposure and correlation risk
# ---------------------------------------------------------------------------
def f_correlation_exposure():
    fig, ax = cl.blank_canvas((13.8, 8.6),
        "Figure 9.4 — Correlated Exposure Looks Like Diversification, Isn't",
        "Three tickets, each individually risking 1.0% by its own stop-loss math. Together they carry far more than 3.0% of real risk because the underlying driver is shared.")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    tickets = [
        ("EURUSD long", 1.0, cl.UP, 18),
        ("GBPUSD long", 1.0, cl.UP, 50),
        ("EURGBP short", 1.0, cl.DN, 82),
    ]
    for label, risk, col, x0 in tickets:
        ax.add_patch(mpatches.FancyBboxPatch((x0 - 15, 55), 30, 30, boxstyle="round,pad=0.5",
                     facecolor="#0d1420", edgecolor=col, lw=1.4, zorder=2))
        ax.text(x0, 78, label, ha="center", va="top", fontsize=11.5, color=col, fontweight="bold", zorder=4)
        ax.text(x0, 68, f"Individual risk: {risk:.1f}%", ha="center", va="top", fontsize=9.6, color=cl.TXT, zorder=4)
        ax.text(x0, 60, "Looks independent", ha="center", va="top", fontsize=8.8, color=cl.MUTED, zorder=4)

    ax.annotate("", xy=(50, 52), xytext=(18, 52), arrowprops=dict(arrowstyle="-", color=cl.ACCENT, lw=1.4))
    ax.annotate("", xy=(82, 52), xytext=(50, 52), arrowprops=dict(arrowstyle="-", color=cl.ACCENT, lw=1.4))
    ax.text(50, 48, "All three positions actually depend on one underlying view: USD weakness against EUR/GBP.\nA single USD-strength reversal moves all three tickets against the trader at once.",
            ha="center", va="top", fontsize=9.4, color=cl.ACCENT, fontweight="bold", zorder=4)

    ax.add_patch(mpatches.FancyBboxPatch((10, 8), 80, 26, boxstyle="round,pad=0.6",
                 facecolor="#0d1420", edgecolor=cl.DN, lw=1.6, zorder=2))
    ax.text(50, 30, "Nominal risk: 1.0% + 1.0% + 1.0% = 3.0% on paper", ha="center", va="top",
            fontsize=10.4, color=cl.TXT, fontweight="bold", zorder=4)
    ax.text(50, 21, "Real correlated exposure: closer to a single 3.0% USD-direction bet,\nnot three independent 1.0% risks \u2014 treat correlated tickets as one position for sizing purposes",
            ha="center", va="top", fontsize=9.4, color=cl.DN, fontweight="bold", zorder=4)

    cl.save_flat(fig, path("m9_correlation_exposure.png"), pad=0.35)


# ---------------------------------------------------------------------------
# 5. News/event risk sizing
# ---------------------------------------------------------------------------
def f_news_event_risk():
    fig, ax = plt.subplots(figsize=(13.6, 6.4))
    shape = cl.seg((10, 0.0010), (1, 0.0140), (1, -0.0180), (8, 0.0006))
    o, h, l, c = cl.series(seed=91, shape=shape, noise=0.00028, wick=0.00032, start=1.0850)
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
    ax.text(news_i - 0.5, float(max(h)) + 0.0035, "scheduled release \u2014 no open position held through it", fontsize=9.2, color=cl.ACCENT,
            ha="center", va="bottom", fontweight="bold")
    cl.verdict(ax, "Position sizing cannot price this gap risk \u2014 the correct control is exposure, not a bigger stop", cl.DN, yy=0.03)
    cl.clean(ax, title="Figure 9.5 — News/Event Risk Is Not Solved by Position Sizing",
             sub="A stop-loss order does not guarantee this fill price during a scheduled-release gap.",
             ts=13.4)
    ax.set_ylim(min(l) - 0.0018, max(h) + 0.0060)
    cl.save(fig, path("m9_news_event_risk.png"), rect=(0.012, 0.02, 0.99, 0.85))


# ---------------------------------------------------------------------------
# 6. Overtrading / revenge trading equity curve
# ---------------------------------------------------------------------------
def f_overtrading_curve():
    fig, axes = cl.panel_fig(
        "Figure 9.6 — Disciplined Sizing vs Revenge-Driven Overtrading",
        "Same starting equity, same first loss. Left: risk stays at the pre-defined 1.0% regardless of outcome. Right: risk is doubled and tripled after losses to \u201cwin it back,\u201d accelerating the drawdown.",
        ncols=2, figsize=(15.6, 6.2))

    ax = axes[0]
    results1 = [-1.0, -1.0, 2.0, -1.0, 1.8, -1.0]
    eq1 = 100 + np.cumsum([0] + results1)
    x1 = np.arange(len(eq1))
    ax.plot(x1, eq1, color=cl.UP, lw=2.2, marker="o", markersize=5, zorder=3)
    cl.verdict(ax, "Disciplined \u2014 fixed 1.0% risk every trade, drawdown stays bounded", cl.UP, yy=0.05)
    cl.clean(ax, sub="Two losses in a row do not change the size of the third trade.")
    ax.set_xticks(x1)
    ax.set_xlabel("Trades", color=cl.MUTED, fontsize=9.5)

    ax2 = axes[1]
    results2 = [-1.0, -2.0, -4.0, 7.6, -8.0]
    eq2 = 100 + np.cumsum([0] + results2)
    x2 = np.arange(len(eq2))
    ax2.plot(x2, eq2, color=cl.DN, lw=2.2, marker="o", markersize=5, zorder=3)
    cl.verdict(ax2, "Revenge trading \u2014 size doubles after each loss, one bad trade erases the gain", cl.DN, yy=0.05)
    cl.clean(ax2, sub="Risk escalates purely to recover the prior loss faster, not because the setup improved.")
    ax2.set_xticks(x2)
    ax2.set_xlabel("Trades", color=cl.MUTED, fontsize=9.5)

    cl.save(fig, path("m9_overtrading_curve.png"))


# ---------------------------------------------------------------------------
# 7. No universal risk level across prop firms
# ---------------------------------------------------------------------------
def f_no_universal_risk():
    fig, ax = cl.blank_canvas((13.8, 8.2),
        "Figure 9.7 — No Single Risk Percentage Is Universally Appropriate",
        "Three illustrative prop-firm rule sets. Identical 1.0% per-trade risk produces very different outcomes against each firm's own daily and max-drawdown limits.")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    firms = [
        ("Firm A (illustrative)", "Daily loss limit: 4%\nMax drawdown: 8%\nConsecutive-loss buffer: ~4 trades at 1.0%", cl.BLUE),
        ("Firm B (illustrative)", "Daily loss limit: 2%\nMax drawdown: 5%\nConsecutive-loss buffer: ~2 trades at 1.0%", cl.CYAN),
        ("Firm C (illustrative)", "Daily loss limit: 3%, scales with\nequity high-water mark\nConsecutive-loss buffer: varies by day", cl.PINK),
    ]
    col_x = [3, 36, 69]
    for (name, rules, col), x0 in zip(firms, col_x):
        ax.add_patch(mpatches.FancyBboxPatch((x0, 40), 28, 46, boxstyle="round,pad=0.6",
                     facecolor="#0d1420", edgecolor=col, lw=1.4, zorder=2))
        ax.text(x0 + 2, 82, name, fontsize=11.2, color=col, fontweight="bold", zorder=4)
        ax.text(x0 + 2, 73, rules, fontsize=9.0, color=cl.TXT, va="top", linespacing=1.6, zorder=4)
        ax.text(x0 + 2, 44, "Same 1.0% risk/trade\nconsumes this buffer\nat a different rate", fontsize=8.6, color=cl.MUTED, va="bottom", linespacing=1.4, zorder=4)

    ax.add_patch(mpatches.FancyBboxPatch((3, 6), 94, 26, boxstyle="round,pad=0.6",
                 facecolor="#0d1420", edgecolor=cl.ACCENT, lw=1.6, zorder=2))
    ax.text(50, 28, "Firm B's rules leave roughly half the consecutive-loss buffer of Firm A at the identical 1.0% risk setting.",
            ha="center", va="top", fontsize=10.0, color=cl.ACCENT, fontweight="bold", zorder=4)
    ax.text(50, 18, "The correct risk percentage is derived from each specific firm's own daily loss limit and max drawdown rule \u2014\nnever copied from another firm's number or from a generic \u201c1% rule\u201d without checking it against the actual limits in force.",
            ha="center", va="top", fontsize=9.2, color=cl.TXT, linespacing=1.5, zorder=4)

    cl.save_flat(fig, path("m9_no_universal_risk.png"), pad=0.35)


if __name__ == "__main__":
    f_sizing_by_stop()
    f_daily_loss_limit()
    f_drawdown_reduction()
    f_correlation_exposure()
    f_news_event_risk()
    f_overtrading_curve()
    f_no_universal_risk()
    print("All Module 9 figures written.")
