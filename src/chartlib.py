"""
chartlib.py — shared dark-theme charting library for Precision Intraday Trading.
Rebuilt after the original build/ directory was lost to the workspace
snapshot exclusion list (that dirname is now "src", never "build").

Palette: BG #0f1420, PANEL #131a29, UP #26a69a, DN #ef5350, ACCENT #ffb300,
BLUE #4fa3ff, PURP #b07cff, PINK #ff7ab8, CYAN #4fd1e0, GRID #23304a,
MUTED #8c9bb5, TXT #e8edf7.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

BG = "#0f1420"
PANEL = "#131a29"
UP = "#26a69a"
DN = "#ef5350"
ACCENT = "#ffb300"
BLUE = "#4fa3ff"
PURP = "#b07cff"
PINK = "#ff7ab8"
CYAN = "#4fd1e0"
GRID = "#23304a"
MUTED = "#8c9bb5"
TXT = "#e8edf7"

plt.rcParams.update({
    "figure.facecolor": BG,
    "axes.facecolor": PANEL,
    "savefig.facecolor": BG,
    "text.color": TXT,
    "axes.edgecolor": GRID,
    "axes.labelcolor": MUTED,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "font.size": 11,
    "font.family": "DejaVu Sans",
})


# ---------------------------------------------------------------------------
# synthetic candle series
# ---------------------------------------------------------------------------
def series(seed, shape, noise=0.05, wick=0.06, start=100.0):
    """
    Deterministic synthetic OHLC series driven by a shape array (cumulative
    drift per bar) plus small per-bar jitter and wicks.

    shape: 1D array of cumulative drift already walked out (e.g. from seg()).
    noise, wick: ABSOLUTE price-unit magnitudes (not fractions of price) —
    keep them the same small scale as the per-bar moves in `shape` (typically
    0.03-0.12 for a synthetic instrument trading near `start`).
    """
    rng = np.random.RandomState(seed)
    n = len(shape)
    drift = np.asarray(shape, dtype=float)
    jitter = rng.normal(0, noise, n)
    close = start + drift + jitter
    open_ = np.empty(n)
    open_[0] = start
    open_[1:] = close[:-1]
    body_hi = np.maximum(open_, close)
    body_lo = np.minimum(open_, close)
    rng2 = np.random.RandomState(seed + 1)
    up_wick = np.abs(rng2.normal(0, wick, n))
    dn_wick = np.abs(rng2.normal(0, wick, n))
    high = body_hi + up_wick
    low = body_lo - dn_wick
    return open_, high, low, close


def seg(*legs):
    """
    Build a cumulative-drift shape array from (bars, total_move, kind) legs.
    kind is unused directionally (sign comes from total_move); kept for
    readability at call sites, e.g. seg((10,+2.0,'up'),(5,-0.5,'pullback')).
    Returns a 1D numpy array suitable for series(shape=...).
    """
    out = []
    level = 0.0
    for leg in legs:
        bars, move = leg[0], leg[1]
        bars = int(bars)
        if bars <= 0:
            continue
        step = np.linspace(level, level + move, bars + 1)[1:]
        out.append(step)
        level = level + move
    if not out:
        return np.zeros(1)
    return np.concatenate(out)


# ---------------------------------------------------------------------------
# drawing primitives
# ---------------------------------------------------------------------------
def candles(ax, o, h, l, c, width=0.62, lw=1.05, alpha=1.0):
    n = len(o)
    x = np.arange(n)
    up = c >= o
    for i in range(n):
        col = UP if up[i] else DN
        ax.plot([x[i], x[i]], [l[i], h[i]], color=col, lw=lw, alpha=alpha,
                solid_capstyle="round", zorder=3)
        bh = max(o[i], c[i])
        bl = min(o[i], c[i])
        if bh == bl:
            bh = bl + (h[i] - l[i]) * 0.01 + 1e-6
        rect_h = bh - bl
        ax.add_patch(
            matplotlib.patches.Rectangle(
                (x[i] - width / 2, bl), width, rect_h,
                facecolor=col, edgecolor=col, lw=0.6, alpha=alpha, zorder=4,
            )
        )
    ax.set_xlim(-1, n)


import matplotlib.patches  # noqa: E402  (used by candles())


def clean(ax, title=None, sub=None, ts=12.3):
    ax.grid(True, color=GRID, lw=0.6, alpha=0.55, zorder=0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_color(GRID)
    ax.tick_params(labelsize=9.5)
    if title:
        ax.set_title(title, fontsize=ts, color=TXT, fontweight="bold",
                      loc="left", pad=10)
    if sub:
        ax.text(0.0, 1.0, sub, transform=ax.transAxes, fontsize=9.3,
                 color=MUTED, va="bottom", ha="left",
                 transform_rotates_text=False)


def suptitle(fig, title, sub=None, x=0.048, y=0.982):
    fig.text(x, y, title, fontsize=15.5, color=TXT, fontweight="bold",
              ha="left", va="top")
    if sub:
        fig.text(x, y - 0.045, sub, fontsize=10.6, color=MUTED,
                  ha="left", va="top")


def zone(ax, x0, x1, lo, hi, col, label=None, alpha=0.14, ls="--",
         lblside="left", fs=8.2, va="bottom"):
    ax.add_patch(
        matplotlib.patches.Rectangle(
            (x0, lo), x1 - x0, hi - lo, facecolor=col, edgecolor=col,
            lw=1.1, ls=ls, alpha=alpha, zorder=1,
        )
    )
    ax.plot([x0, x1], [hi, hi], color=col, lw=1.0, ls=ls, alpha=0.75, zorder=2)
    ax.plot([x0, x1], [lo, lo], color=col, lw=1.0, ls=ls, alpha=0.75, zorder=2)
    if label:
        lx = x0 if lblside == "left" else x1
        ha = "left" if lblside == "left" else "right"
        ly = hi if va == "bottom" else lo
        ax.text(lx, ly, label, fontsize=fs, color=col, ha=ha, va=va,
                fontweight="bold", zorder=5)


def hline(ax, y, col, label=None, n=None, ls="--", lw=1.3, side="right",
          fs=8.6, va="bottom", alpha=0.85):
    ax.axhline(y, color=col, lw=lw, ls=ls, alpha=alpha, zorder=2)
    if label and n is not None:
        x = n if side == "right" else 0
        ha = "right" if side == "right" else "left"
        ax.text(x, y, label, fontsize=fs, color=col, ha=ha, va=va,
                 fontweight="bold", zorder=5)


def label_point(ax, x, y, text, col, dx, dy, fs=9.0, ha="left", arrow=True, rad=0.2):
    if arrow:
        ax.annotate(
            text, xy=(x, y), xytext=(x + dx, y + dy),
            fontsize=fs, color=col, ha=ha, fontweight="bold", zorder=6,
            arrowprops=dict(arrowstyle="-", color=col, lw=1.0,
                             connectionstyle=f"arc3,rad={rad}", alpha=0.85),
        )
    else:
        ax.text(x + dx, y + dy, text, fontsize=fs, color=col, ha=ha,
                 fontweight="bold", zorder=6)


def verdict(ax, text, col, bgc=None, yy=0.05):
    bgc = bgc or "#0d1420"
    ax.text(0.5, yy, text, transform=ax.transAxes, fontsize=11.5,
             color=col, ha="center", va="bottom", fontweight="bold",
             bbox=dict(boxstyle="round,pad=0.45", facecolor=bgc,
                       edgecolor=col, lw=1.3), zorder=8)


def badge(ax, text, col, loc="tl"):
    positions = {
        "tl": (0.015, 0.965, "left", "top"),
        "tr": (0.985, 0.965, "right", "top"),
        "bl": (0.015, 0.035, "left", "bottom"),
        "br": (0.985, 0.035, "right", "bottom"),
    }
    x, y, ha, va = positions.get(loc, positions["tl"])
    ax.text(x, y, text, transform=ax.transAxes, fontsize=9.2, color=col,
             ha=ha, va=va, fontweight="bold",
             bbox=dict(boxstyle="round,pad=0.35", facecolor="#0d1420",
                       edgecolor=col, lw=1.0, alpha=0.92), zorder=9)


def swing_marks(ax, idx_labels, h, l, col_hi=ACCENT, col_lo=BLUE,
                 dy_hi=1.0, dy_lo=1.0, fs=8.6):
    """
    idx_labels: list of (index, 'H'|'L', text)
    """
    for idx, kind, text in idx_labels:
        if kind == "H":
            ax.scatter([idx], [h[idx]], color=col_hi, s=26, zorder=6,
                       edgecolor="#0d1420", lw=0.8)
            ax.text(idx, h[idx] + dy_hi, text, fontsize=fs, color=col_hi,
                     ha="center", va="bottom", fontweight="bold", zorder=6)
        else:
            ax.scatter([idx], [l[idx]], color=col_lo, s=26, zorder=6,
                       edgecolor="#0d1420", lw=0.8)
            ax.text(idx, l[idx] - dy_lo, text, fontsize=fs, color=col_lo,
                     ha="center", va="top", fontweight="bold", zorder=6)


# ---------------------------------------------------------------------------
# figure/canvas helpers
# ---------------------------------------------------------------------------
def panel_fig(title, sub, ncols=2, figsize=(15.4, 6.3)):
    fig, axes = plt.subplots(1, ncols, figsize=figsize)
    if ncols == 1:
        axes = [axes]
    suptitle(fig, title, sub)
    return fig, axes


def blank_canvas(figsize, title, sub):
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_facecolor(PANEL)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    suptitle(fig, title, sub)
    return fig, ax


def save(fig, path, rect=(0.012, 0.02, 0.99, 0.895), tight=True, dpi=150):
    if tight:
        try:
            fig.tight_layout(rect=rect)
        except Exception:
            pass
    fig.savefig(path, dpi=dpi, facecolor=BG)
    plt.close(fig)


def save_flat(fig, path, pad=0.3, dpi=150):
    fig.savefig(path, dpi=dpi, facecolor=BG, bbox_inches="tight", pad_inches=pad)
    plt.close(fig)
