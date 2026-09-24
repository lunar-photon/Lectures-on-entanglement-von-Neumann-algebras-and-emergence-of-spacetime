#!/usr/bin/env python3
"""Figure fig:area_law: why entanglement across a cut scales with the area.

A spatial slice (d-1 = 2 dimensions, so d = 3 and d-2 = 1) is replaced by a
square lattice of spacing eps.  A region R is bounded by a smooth closed curve
dR.  Nearest-neighbour links whose two ends lie on opposite sides of dR are
drawn in red: these are the short-distance couplings that entangle R with L.
Panel (b) halves eps; the number of crossing links roughly doubles, i.e. it
scales as Area(dR)/eps^{d-2} = Length(dR)/eps.

Usage (from companion_v2/):  python fig_sources/fig_area_law.py
Writes figs/fig_area_law.pdf.  Included at 0.75\\textwidth (~4.9 in).
"""
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

OUT = Path(__file__).resolve().parent.parent / "figs" / "fig_area_law.pdf"

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["cmr10"],
    "mathtext.fontset": "cm",
    "axes.unicode_minus": False,
    "axes.formatter.use_mathtext": True,
    "font.size": 10,
    "pdf.fonttype": 42,
})

BLUE = "#2b6cb0"
FILL = "#e3ecf8"
RED = "#c0392b"
GREY = "0.62"

HALF = 1.0            # the drawn window is [-HALF, HALF]^2


def radius(phi):
    """Smooth, slightly irregular boundary dR in polar form."""
    return 0.62 * (1 + 0.10 * np.cos(3 * phi + 0.4) + 0.06 * np.sin(2 * phi))


def inside(x, y):
    return np.hypot(x, y) < radius(np.arctan2(y, x))


def lattice(eps):
    n = int(round(2 * HALF / eps))
    g = -HALF + eps * np.arange(n + 1)
    X, Y = np.meshgrid(g, g, indexing="ij")
    return g, X, Y


def draw(ax, eps, letter):
    g, X, Y = lattice(eps)
    I = inside(X, Y)
    n = len(g)
    grid_lines, cut_links = [], []
    for i in range(n):
        for j in range(n):
            for di, dj in ((1, 0), (0, 1)):
                a, b = i + di, j + dj
                if a >= n or b >= n:
                    continue
                seg = [(X[i, j], Y[i, j]), (X[a, b], Y[a, b])]
                (cut_links if I[i, j] != I[a, b] else grid_lines).append(seg)

    phi = np.linspace(0, 2 * np.pi, 600)
    r = radius(phi)
    ax.fill(r * np.cos(phi), r * np.sin(phi), color=FILL, zorder=0, lw=0)
    ax.add_collection(LineCollection(grid_lines, colors=GREY, lw=0.35, zorder=1))
    ax.add_collection(LineCollection(cut_links, colors=RED, lw=1.5, zorder=3,
                                     capstyle="round"))
    ms = 2.2 if eps > 0.1 else 1.3
    ax.plot(X[~I], Y[~I], "o", ms=ms, color="0.45", mew=0, zorder=2)
    ax.plot(X[I], Y[I], "o", ms=ms, color=BLUE, mew=0, zorder=2)
    ax.plot(r * np.cos(phi), r * np.sin(phi), color=BLUE, lw=1.0, zorder=4)

    # labels
    ax.text(0.0, -0.05, r"$R$", ha="center", va="center", fontsize=12,
            color=BLUE, zorder=6,
            bbox=dict(fc=FILL, ec="none", pad=1.2))
    ax.text(0.80, 0.84, r"$L$", ha="center", va="center", fontsize=12,
            color="0.25", zorder=6,
            bbox=dict(fc="white", ec="none", pad=1.2))
    # label dR at a point on the curve, outside it
    p0 = 2.35
    rb = radius(p0)
    ax.annotate(r"$\partial R$", xy=(rb * np.cos(p0), rb * np.sin(p0)),
                xytext=(-0.88, 0.86), ha="center", va="center", fontsize=10,
                color=BLUE, zorder=6,
                bbox=dict(fc="white", ec="none", pad=1.0),
                arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.6,
                                shrinkA=1, shrinkB=1))
    # eps bracket along the bottom edge, below the lattice
    x0 = g[1]
    yb = -HALF - 0.09
    ax.annotate("", xy=(x0, yb), xytext=(x0 + eps, yb),
                arrowprops=dict(arrowstyle="|-|", color="0.2", lw=0.7,
                                mutation_scale=2.5, shrinkA=0, shrinkB=0))
    ax.text(x0 + eps + 0.05, yb, r"$\epsilon$" if eps > 0.1 else r"$\epsilon/2$",
            ha="left", va="center", fontsize=10, color="0.2")

    ax.text(-HALF - 0.02, HALF + 0.13, letter, ha="left", va="bottom",
            fontsize=10)
    ax.set_xlim(-HALF - 0.06, HALF + 0.06)
    ax.set_ylim(-HALF - 0.2, HALF + 0.24)
    ax.set_aspect("equal")
    ax.axis("off")
    return len(cut_links)


EPS = 0.2
fig, axes = plt.subplots(1, 2, figsize=(4.9, 2.55))
n1 = draw(axes[0], EPS, "(a)")
n2 = draw(axes[1], EPS / 2, "(b)")
print(f"crossing links: eps -> {n1}, eps/2 -> {n2}, ratio {n2 / n1:.2f}")
# Area law in d = 3: number of crossing links ~ Length(dR)/eps, so ratio ~ 2.
assert 1.6 < n2 / n1 < 2.4

fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01, wspace=0.08)
OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT, bbox_inches="tight", pad_inches=0.03)
print(f"wrote {OUT}")
