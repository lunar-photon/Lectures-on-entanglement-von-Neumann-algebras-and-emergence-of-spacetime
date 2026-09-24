#!/usr/bin/env python3
"""Figure fig:spin_chain_typeIII: the Bell-pair chain at theta = pi/6.

State: |Phi_theta> = (x)_{k=1}^N (cos th |00> + sin th |11>)_k.

(a) S_R^{(N)} = N s_1(theta), s_1 = -c^2 log c^2 - s^2 log s^2 (nats),
    for N = 1..40.  s_1(pi/6) = 0.5623 nats.
(b) Modular operator Delta = rho_R (x) rho_L^{-1} at N = 12.  Its eigenvectors
    are |i>_R|j>_L with eigenvalue p_i/p_j = lambda^{k_i - k_j}, where k_i is
    the number of 1s in the string i and lambda = tan^2 theta.  The eigenvalue
    lambda^n therefore occurs with multiplicity sum_k C(N,k) C(N,k-n)
    = C(2N, N+n) (Vandermonde).  Bars show the fraction C(2N,N+n)/4^N.
    Checked against brute-force diagonalisation at small N.

Usage (from companion_v2/):  python fig_sources/fig_spin_chain_typeIII.py
Writes figs/fig_spin_chain_typeIII.pdf.  Included at 0.78\\textwidth (~5.1 in).
"""
from math import comb
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent.parent / "figs" / "fig_spin_chain_typeIII.pdf"

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["cmr10"],
    "mathtext.fontset": "cm",
    "axes.formatter.use_mathtext": True,
    "axes.unicode_minus": False,
    "font.size": 9,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "pdf.fonttype": 42,
})

BLUE = "#2b6cb0"
GOLD = "#b7791f"

TH = np.pi / 6
LAM = np.tan(TH) ** 2
C2, S2 = np.cos(TH) ** 2, np.sin(TH) ** 2
s1 = -C2 * np.log(C2) - S2 * np.log(S2)

# ---- (a) entropy of N pairs --------------------------------------------------
Ns = np.arange(1, 41)
S = Ns * s1

# ---- (b) spectrum of the modular operator at N = 12 ---------------------------
N = 12
ns = np.arange(-N, N + 1)
frac = np.array([comb(2 * N, N + n) for n in ns], float) / 4 ** N
assert abs(frac.sum() - 1) < 1e-12


def brute(Nsmall):
    p = np.array([C2, S2])
    pR = p
    for _ in range(Nsmall - 1):
        pR = np.kron(pR, p)
    ev = np.outer(pR, 1 / pR).ravel()           # eigenvalues of rho_R (x) rho_L^{-1}
    nn = np.rint(np.log(ev) / np.log(LAM)).astype(int)
    assert np.allclose(ev, LAM ** nn)
    counts = np.array([(nn == n).sum() for n in range(-Nsmall, Nsmall + 1)])
    ref = np.array([comb(2 * Nsmall, Nsmall + n) for n in range(-Nsmall, Nsmall + 1)])
    assert (counts == ref).all()


for m in (1, 2, 3, 5):
    brute(m)
print(f"s1(pi/6) = {s1:.4f} nats, lambda = {LAM:.4f}; multiplicities verified")

fig, (a, b) = plt.subplots(1, 2, figsize=(5.1, 2.05),
                           gridspec_kw=dict(width_ratios=[1, 1.15]))

a.plot(Ns, S, "o", ms=2.6, color=BLUE, mew=0)
a.plot(Ns, S, "-", lw=0.8, color=BLUE, alpha=0.6)
a.set_xlim(0, 41)
a.set_ylim(0, None)
a.set_xticks([0, 10, 20, 30, 40])
a.set_xlabel(r"$N$")
a.set_ylabel(r"$S_R^{(N)}$")

logev = ns * np.log(LAM)
b.vlines(logev, 0, frac, color=GOLD, lw=1.1)
b.plot(logev, frac, "o", ms=2.8, color=GOLD, mew=0)
b.set_ylim(0, frac.max() * 1.1)
tick_n = [-10, -5, 0, 5, 10]
b.set_xticks([n * np.log(LAM) for n in tick_n])
b.set_xticklabels([r"$1$" if n == 0 else rf"$\lambda^{{{n}}}$" for n in tick_n])
b.set_xlabel(r"eigenvalue of $\Delta_{\Phi_\theta}$")
b.set_yticks([0, 0.05, 0.1, 0.15])
b.set_yticklabels([r"$0$", r"$0.05$", r"$0.1$", r"$0.15$"])

for ax, letter in ((a, "(a)"), (b, "(b)")):
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction="out", length=3)
    ax.text(-0.02, 1.04, letter, transform=ax.transAxes, ha="right", va="bottom")

fig.tight_layout(pad=0.3, w_pad=1.2)
OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT, bbox_inches="tight", pad_inches=0.03)
print(f"wrote {OUT}")
