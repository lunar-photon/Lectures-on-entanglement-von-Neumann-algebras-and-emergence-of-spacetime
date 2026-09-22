# Sec. X: Conclusions & Discussions

# Sec.~X: Conclusions and discussions

## Sec.~X.A: summary

The paper's own summary is short enough, and important enough, to walk through point by point rather than
just gesture at — each bullet below is one of the paper's own, restated with the companion-section number
where it was actually built, so you can trace any one of them back to its full derivation.


- In the $G_N\to0$ limit, a general bulk subregion is defined by a boundary operator algebra —
typically one with no direct boundary geometric description at all — carrying an emergent type
$\mathrm{III}_1$ structure, sourced by the infinite long-range entanglement that only appears in the strict
large-$N$ limit (Secs.~VI—VII of this companion). This machinery is not restricted to the strict Einstein
($\lambda\to\infty$) limit; it extends, with modification, into the stringy regime (Sec.~VIII.D).
- Bulk causal structure is encoded in boundary *emph* structure — not merely boundary
causality (which only forces spacelike-separated operators to commute), but the richer, timelike commutant
structure that subregion-subalgebra duality inherits from the bulk. Quantitative tools like the causal depth
parameter $T(t)$ (Sec.~VIII.A) make this a checkable, numerical diagnostic of horizons and global causal
structure, and these tools too extend into the stringy regime.
- Modular flow, and its refinement half-sided modular flow, characterize the emergence of time itself in
the bulk — resolving the meeting-behind-the-horizon puzzle via emergent Kruskal time (Sec.~VIII.B), and
motivating a sharpened, algebraic version of the ER$=$EPR proposal (Sec.~VIII.C).
- Large-$N$ boundary algebras split cleanly into two kinds, worth keeping distinct in your own head going
forward: an **entanglement wedge algebra** $X$ is, by definition, the large-$N$ limit of a genuine
finite-$N$ algebra $B$ — it always admits a finite-$N$ ancestor. A **causal wedge algebra** $Y$, by
contrast, is intrinsically a large-$N$, semiclassical construct, built directly from single-trace operators via
the extrapolate dictionary, with no finite-$N$ definition of its own. Neither is guaranteed to have a bulk
geometric meaning once you leave the strict Einstein regime — and, importantly, both constructions apply
just as well to non-gravitational systems entangled with a holographic partner (Sec.~VII.B.3), with no need
for the non-gravitational side to have its own large-$N$ parameter at all.
- Simple operator-algebraic toy models — static observers (Sec.~IX.A—D), dynamical observers
(Sec.~IX.E), and exactly-solvable JT gravity (Sec.~IX.F) — turn this machinery into concrete physics: the
physical origin of generalized gravitational entropy for black holes, de~Sitter space, and general regions;
the emergence of a cosmological horizon as an observer's mass is taken to infinity; and, in JT gravity, a
complete, finite-$G_N$ example where the operator algebra of quantum gravity is known in exact closed form,
even though the Hilbert space itself does not factorize.


## Sec.~X.B: the mathematical structure of quantum gravity, and the full-circle answer to where we
started

This closing section is more speculative than the rest of the paper, and it is worth reading slowly, because
it reaches back and answers, at the deepest level the paper attempts, the very question this companion opened
with in Sec.~I: *emph*

### Why quantum gravity cannot have one single Hilbert space

Ordinary quantum mechanics treats the Hilbert space as fundamental: states are density operators living in it,
observables are operators acting on it. The paper argues this cannot be the right starting point for quantum
gravity, for a very concrete reason. It's widely believed that no physical process in quantum gravity can
change a spacetime's *emph* structure — there's no physical process that takes a state of type IIB
string theory on $\text{AdS}_5\times S^5$ to a state on $\text{AdS}_3\times S^3\times K3$, or to either of
these from ten-dimensional flat Minkowski space. Since a genuine physical process is exactly what it means
for two states to live in the same Hilbert space (you can always in principle evolve from one to the other),
**each of these asymptotic backgrounds must correspond to a genuinely separate Hilbert space** — and
this is not a conjecture, it's already visible directly in the existing dictionary: AdS$_5\times S^5$ is dual to
a four-dimensional CFT with its own Hilbert space, AdS$_3\times S^3\times K3$ to a two-dimensional CFT with a
completely different one, and nothing maps a state of one to a state of the other. Yet all of these are
supposed to be different vacua of the very same underlying theory — type IIB string theory. **Without
one single, global Hilbert space to hold all of these together, what mathematical object is left to call ``the
theory''?**

### The resolution you've already met, twice

This is exactly the same shape of question that opened Sec.~I of this companion — and the resolution is
precisely the demotion of the Hilbert space you already worked through in detail back in Sec.~II.B.3,
applied now at the grandest possible scale. Look first at a much smaller-scale version of the exact same
puzzle, already familiar from ordinary QFT in curved spacetime: a free scalar field in flat Minkowski
space can be quantized using ordinary Minkowski time, *emph* using Rindler time (Sec.~IV.D.1) — both are
perfectly physically sensible choices, describing different physical situations (an inertial vs.\ an
accelerated observer), and yet they produce genuinely, unitarily *emph* Hilbert spaces. You could
declare these to be two different theories, but that's clearly the wrong instinct — there's an obvious sense
in which it's the same free scalar field theory, just quantized around two different reference states.
**Algebraic QFT resolves this by defining the theory as a pair $(\Alg,\Sscr)$ — an algebra $\Alg$ of
field operators, together with a space $\Sscr$ of allowed states (in the abstract, linear-functional sense of
Sec.~II.B.3, not vectors in any particular Hilbert space) — and letting the Hilbert space be a
*emph* Minkowski quantization and Rindler quantization are simply two
different GNS representations of the very same underlying algebra $\Alg$ — genuinely different Hilbert
spaces, but manifestly the same theory, because the algebra never changed.

**The proposal here is to do exactly this, one level up, for the whole of quantum gravity.** Postulate
that a quantum-gravity theory at finite $G_N$ is specified by a single abstract $*$-algebra $\Alg$ (not tied to
any particular asymptotic structure) together with some allowed collection of states on it. Different
asymptotic structures — AdS$_5\times S^5$, AdS$_3\times S^3\times K3$, flat space, de~Sitter — simply
correspond to *emph* $\omega$ on this one algebra, each producing its own GNS Hilbert space
$\HH_\omega$ via exactly the Sec.~II.D construction, with the corresponding boundary CFT (where one is known)
simply *emph* that GNS representation. Concretely: $\omega_{\text{AdS}_5\times S^5}$ is the state whose
GNS Hilbert space is that of $\mathcal N=4$ super-Yang-Mills; $\omega_{\text{AdS}_3\times S^3\times K3}$ is
the state whose GNS space is the dual two-dimensional CFT's; and, in principle, flat space and de~Sitter
correspond to further states of the same underlying algebra $A_{\text{IIB}}$, even though an explicit boundary
description for those cases isn't yet known.


> [!NOTE] **Physics Connection: Levels of Algebraic Emergence**
> This is, symbol for symbol, the exact same logical move made twice already in this companion, and it's worth
> seeing all three levels lined up side by side, because each one is a strictly more drastic version of the
> same idea:
> 
- **Sec.~II.B.3 / Slavnov**: an ordinary quantum *emph* $\omega$ (or $\rho$, or $\ket\psi$) is
> not fundamental — it's a derived bookkeeping device (an ensemble average, in Slavnov's language) built on
> top of the more primitive pairing of algebra and individual measurement outcome.
>
- **Sec.~II.D / the Minkowski—Rindler example just above**: the *emph* is not
> fundamental — a single algebra $\Alg$ can produce many inequivalent Hilbert spaces, one per choice of
> reference state, via GNS.
>
- **Here**: even the question "which spacetime background am I in" is not fundamental data fed
> into the theory — it, too, is just a choice of state on one underlying algebra, with the entire geometric
> structure of a spacetime (AdS, flat space, de~Sitter, and everything this whole companion built on top of
> that — causal structure, horizons, entropy) emerging as a *emph* of that choice, not an
> ingredient of it.
>

> Nothing about the mathematics changed between these three instances — it is the identical GNS construction,
> applied at the level of an individual measurement, then at the level of an ordinary quantum system, then at
> the level of an entire spacetime background. What changed is only how much structure you're willing to
> regard as emergent rather than fundamental — and the arc of this whole paper has been to push that boundary
> further out, one section at a time.


At present, there is no known background-independent definition of the algebra $A_{\text{IIB}}$ itself, nor a
full characterization of which states are allowed — string field theory is flagged as a plausible route
toward one, since for any fixed background state it already supplies both the Hilbert space and the
background-dependent algebra, with its equations of motion available to help identify further consistent
states systematically. The paper closes by framing the entire algebraic program of these lecture notes —
subregion-subalgebra duality, modular time, the crossed product, generalized entropy from observer dressing
— as a first, concrete step toward exactly this larger goal: a formulation of quantum gravity in which
asymptotic structure, the cosmological constant, the Hilbert space, and the very number of degrees of freedom
are not fixed ingredients handed to the theory in advance, but *emph* of
a single, more primitive algebraic structure — precisely the shape of the argument this whole companion has
been unpacking, one worked example at a time, since the very first page of Sec.~I.

\subsection*{On the two appendices}

The paper closes with two short technical appendices, useful as reference but not adding new conceptual
content beyond what this companion has already covered in the main text: **Appendix A** works through
two further finite-dimensional examples of infinite entanglement coexisting with a factorizable Hilbert
space (fine-tuned counterexamples to the general expectation, flagged already in a footnote back in Sec.~II.A
of this companion, that infinite entanglement generically prevents factorization); **Appendix B** carries
out the explicit computation, cited but not reproduced in Sec.~V.B above, solving the KMS relation to derive
$\widehat\Delta=\Delta_\Psi$ for the crossed-product algebra. Both are worth consulting directly in the
original paper if you want to see those specific calculations in full, but neither changes anything about the
conceptual picture this companion has built.

\bigskip
\noindent This closes the companion. Every section of Liu's paper, from the opening motivation through the
speculative closing remarks on the mathematical structure of quantum gravity, has now been walked through —
with every definition built up from scratch, every worked example computed with actual numbers, and every
question you wrote in the margin of your own copy answered directly at the point where it came up. The
question of what replaces the wavefunction, and why, turns out to be the same question the paper itself is
asking about spacetime by its very last page: which parts of the familiar picture are fundamental, and which
are just the most convenient representation of something deeper.
