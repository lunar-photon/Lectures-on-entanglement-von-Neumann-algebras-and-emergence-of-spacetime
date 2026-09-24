#!/usr/bin/env python3
"""Figure 1.2 (fig:qubit_entropy): single-pair entanglement entropy.

For |phi_theta> = cos(theta)|0>_R|0>_L + sin(theta)|1>_R|1>_L, theta in (0, pi/4],
    s_1(theta) = -cos^2(theta) log cos^2(theta) - sin^2(theta) log sin^2(theta)
in nats (natural log), matching chapters/01_introduction.tex.
Peak: s_1(pi/4) = log 2 ~ 0.6931 (Bell pair).

Usage (from companion_v2/):  python fig_sources/fig_qubit_entropy.py
Writes figs/fig_qubit_entropy.pdf.  Included at width=0.75\\textwidth of a
6.5in text block, i.e. ~4.9in, so the figure is drawn at 4.9in (scale 1:1).
"""
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent.parent / "figs" / "fig_qubit_entropy.pdf"

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["cmr10"],          # Computer Modern (bundled with matplotlib)
    "mathtext.fontset": "cm",
    "axes.formatter.use_mathtext": True,
    "axes.unicode_minus": False,
    "font.size": 10,
    "axes.labelsize": 11,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "pdf.fonttype": 42,
})


def s1(theta):
    """Single-pair von Neumann entropy in nats; s1(0) = 0 by continuity."""
    c2, s2 = np.cos(theta) ** 2, np.sin(theta) ** 2
    with np.errstate(divide="ignore", invalid="ignore"):
        t1 = np.where(c2 > 0, -c2 * np.log(c2), 0.0)
        t2 = np.where(s2 > 0, -s2 * np.log(s2), 0.0)
    return t1 + t2


theta = np.linspace(0.0, np.pi / 4, 800)
S = s1(theta)
LOG2 = np.log(2.0)

# Numerical check: peak equals log 2 at theta = pi/4.
peak = float(s1(np.pi / 4))
assert abs(peak - LOG2) < 1e-12, peak
assert abs(S.max() - LOG2) < 1e-12 and np.isclose(theta[S.argmax()], np.pi / 4)
print(f"peak s1(pi/4) = {peak:.6f} nats, log 2 = {LOG2:.6f}")

BLUE = "#1f5fa8"
RED = "#b8322a"
GREY = "0.45"

fig, ax = plt.subplots(figsize=(4.9, 3.0))

# log 2 guide
ax.axhline(LOG2, color=GREY, lw=0.9, ls=(0, (4, 3)), zorder=1)

ax.plot(theta, S, color=BLUE, lw=2.0, zorder=2)

# Maximum: Bell state (explained in the caption; no in-figure text)
ax.plot([np.pi / 4], [LOG2], "o", color=RED, ms=6, zorder=4, clip_on=False)
# theta -> 0: product-state limit (open endpoint, since theta in (0, pi/4])
ax.plot([0.0], [0.0], "o", mfc="white", mec=BLUE, mew=1.3, ms=5.5,
        zorder=4, clip_on=False)

# Axes
ax.set_xlim(0.0, np.pi / 4)
ax.set_ylim(0.0, 0.78)
ax.set_xticks([0, np.pi / 16, np.pi / 8, 3 * np.pi / 16, np.pi / 4])
ax.set_xticklabels([r"$0$", r"$\pi/16$", r"$\pi/8$", r"$3\pi/16$", r"$\pi/4$"])
ax.set_yticks([0.0, 0.2, 0.4, LOG2])
ax.set_yticklabels([r"$0$", r"$0.2$", r"$0.4$", r"$\log 2$"])
ax.set_xlabel(r"$\theta$")
ax.set_ylabel(r"$s_1(\theta)$  [nats]")

for side in ("top", "right"):
    ax.spines[side].set_visible(False)
ax.tick_params(direction="out", length=3.5)

fig.tight_layout(pad=0.3)
OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT, bbox_inches="tight", pad_inches=0.03)
print(f"wrote {OUT}")
