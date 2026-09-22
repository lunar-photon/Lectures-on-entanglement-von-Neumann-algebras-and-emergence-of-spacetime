# Sec. I: Introduction and Motivations

# Sec.~I: Introduction and Motivations

## What problem is this paper actually solving?

Before any equation, it helps to say in plain words what question this whole 119-page paper is an answer to,
because the paper itself takes a few pages of fairly compressed language to say it, and it's easy to lose the
forest for the trees once the algebra starts.

Here is the question. Ordinary physics — both classical and quantum — treats spacetime as a fixed stage:
space and time are given in advance, with a definite geometry (flat, or curved according to some metric),
and physics happens *emph* that stage. General relativity already complicates this a little, because the
geometry itself is dynamical (matter tells spacetime how to curve, spacetime tells matter how to move), but
even there, at any given moment you can ask "what is the metric right here" and get a sharp, well-defined
answer. Quantum gravity is the attempt to quantize this whole picture — and the moment you do, the metric
itself becomes an operator, subject to quantum fluctuations, and the question ``what is the geometry right
here'' stops having a sharp answer in the same way that "where exactly is the electron" stops having a
sharp answer once you quantize a particle's position. Geometric concepts like ``this point is to the future
of that point,'' or "this region is causally connected to that region," or ``this is a local, self-contained
patch of space'' — all of these are only sharply defined in the classical limit, which physicists write as
$G_N\to0$ ($G_N$ is Newton's gravitational constant; turning it off turns off quantum-gravitational effects
and leaves you with an ordinary, fixed classical geometry).

So here is the actual research question the paper poses: suppose you are handed a complete quantum theory of
gravity at some finite, nonzero $G_N$ — no classical geometry assumed, no metric given in advance, nothing
geometric built in from the start. As you dial $G_N\to0$, familiar geometric structures (a well-defined
notion of "here," of causal order, of a local region) are supposed to emerge. **What, physically and
mathematically, is doing the emerging?** What is it about the underlying quantum theory that produces
spacetime geometry as $G_N\to0$, and what role, if any, does quantum entanglement play?

This is not an idle question. The clearest place it can be asked precisely is the AdS/CFT correspondence,
where a theory of quantum gravity living in a $(d{+}1)$-dimensional *emph* spacetime (AdS,
a spacetime with constant negative curvature, chosen because it has a well-defined boundary at infinity) is
conjectured to be completely equivalent to an ordinary, non-gravitational quantum field theory — a
*emph* (CFT) — living on that $d$-dimensional boundary. On the CFT side, there is a
parameter $N$ that counts the number of independent field degrees of freedom (originally, for the gauge
theories where this was first understood, $N$ was literally the number of colors of an $SU(N)$ gauge group).
The AdS/CFT dictionary says $G_N$ on the gravity side maps to a positive power of $1/N$ on the CFT side, so
$G_N\to0$ (classical, geometric gravity) is exactly the same limit as $N\to\infty$ on the boundary. The
question above becomes concrete and answerable: *emph*

The Ryu—Takayanagi proposal (2006) was the first strong hint at the answer: it conjectures a formula tying
the entanglement entropy of a boundary region to the area of a certain minimal surface in the bulk — literally
an equation relating an entanglement measure to a geometric quantity. If entanglement entropy and bulk area
are related this tightly, entanglement itself must be doing real structural work in building the bulk
geometry, not just decorating it. That is the motivating intuition. The rest of the paper is the attempt to
make this intuition completely precise, and the tool that does it turns out to be a piece of 1930s
mathematics — von Neumann algebras — that was originally developed for a completely different reason (putting
ordinary quantum mechanics on a rigorous footing), and has only recently been recognized as exactly the right
language for this question.

## Why the ordinary quantum-mechanical definition of "subsystem" isn't good enough

To see why a new mathematical tool is needed at all, you have to see precisely where the old one breaks. The
old tool is the one from every quantum mechanics course: given a system built out of two pieces, $R$ and $L$
(read them as "right" and "left," or "region" and its complement — any bipartition), the Hilbert space of
the whole system factors as a tensor product,

$$

\HH = \HH_R\otimes\HH_L .

$$

Concretely, if $\HH_R$ has orthonormal basis $\{\ket i_R\}$ and $\HH_L$ has orthonormal basis
$\{\ket a_L\}$, then $\HH_R\otimes\HH_L$ is spanned by all the pairs $\ket i_R\ket a_L$, and a general state of
the joint system is a sum $\ket\Psi = \sum_{ia} c_{ia}\ket i_R\ket a_L$ for some array of complex numbers
$c_{ia}$ (Liu's eq.~1.1, written with a continuous or more general index set — the idea is identical). This
state is called **entangled** exactly when the array $c_{ia}$ cannot be written as a simple product
$c_{ia}=\psi_i\chi_a$ for two smaller arrays $\psi_i,\chi_a$ — i.e., when it doesn't factor into ``something
about $R$'' times "something about $L$."

Everything about entanglement that you already know — the reduced density matrix
$\rho_R\equiv\Tr_L\ket\Psi\!\bra\Psi$ (tracing out, i.e., summing over, the $L$ degrees of freedom), the
entanglement entropy $S_R=-\Tr_R(\rho_R\log\rho_R)$, the R\'enyi entropies, the relative entropy — every one
of these formulas (Liu's eqs.~2.2—2.4) is built directly on top of the tensor factorization
$\HH=\HH_R\otimes\HH_L$. If that factorization doesn't exist, none of these formulas can even be written down,
because there is no $\HH_L$ to trace over and no well-defined "$R$-part" of the state to extract. The whole
apparatus of entanglement entropy that you learned collapses at the first step, not because it gives a wrong
answer, but because it has no answer to give.

The paper's central claim — the one that everything else builds on — is that this factorization genuinely
fails to exist, not as some exotic mathematical pathology, but in exactly the situations that matter most:
gauge theories, many-body systems in a thermodynamic (infinite-volume or infinite-$N$) limit, quantum field
theories cut into two regions by a surface, and — the case this paper cares about most — the large-$N$ limit
of a holographic boundary theory. Section~II.A of the paper (and this companion's next section) works through
three concrete examples of exactly how and why it fails. It is worth working through the second of these three
examples slowly and completely here, in Sec.~I, because it is the single example every later section in the
paper keeps coming back to.

## The example that carries the whole paper: infinitely many entangled qubit pairs

Take a single pair of qubits, one belonging to $R$ and one to $L$, prepared in the state

$$

\ket{\phi_\theta} = \cos\theta\,\ket0_R\ket0_L + \sin\theta\,\ket1_R\ket1_L , \qquad \theta\in(0,\pi/4] .

$$

This is completely standard material: it's a partially entangled pair (maximally entangled exactly at
$\theta=\pi/4$, where the coefficients become equal, $\tfrac1{\sqrt2}$ each — this is a Bell pair). You could
build this in a lab tomorrow with two photons or two trapped ions. Nothing about a single pair is
mysterious.

To see the reduced density matrix explicitly, write out the full $4\times4$ density operator for the pure pair:

$$

\ket{\phi_\theta}\bra{\phi_\theta} = \cos^2\theta\ket{00}\bra{00} + \cos\theta\sin\theta\ket{00}\bra{11} + \sin\theta\cos\theta\ket{11}\bra{00} + \sin^2\theta\ket{11}\bra{11} .

$$

Now take the partial trace over subsystem $L$ by summing over the orthonormal basis $\{\ket0_L, \ket1_L\}$:
\begin{align*}
\rho_R &\equiv \Tr_L\ket{\phi_\theta}\bra{\phi_\theta} = {}_L\braket{0|\phi_\theta}\bra{\phi_\theta}0\rangle_L + {}_L\braket{1|\phi_\theta}\bra{\phi_\theta}1\rangle_L \\
&= \cos^2\theta\,\ket0_R\bra0_R + \sin^2\theta\,\ket1_R\bra1_R = \begin{pmatrix} \cos^2\theta & 0 \\ 0 & \sin^2\theta \end{pmatrix} .
\end{align*}
Because $\rho_R$ is already diagonal, its operator logarithm is obtained by taking the logarithm of each eigenvalue along the diagonal:

$$

\log\rho_R = \begin{pmatrix} \log(\cos^2\theta) & 0 \\ 0 & \log(\sin^2\theta) \end{pmatrix} .

$$

The single-pair von Neumann entanglement entropy follows immediately by evaluating the trace:
\begin{align*}
s_1(\theta) &= -\Tr_R(\rho_R\log\rho_R) = -\left[ \cos^2\theta\log(\cos^2\theta) + \sin^2\theta\log(\sin^2\theta) \right] .
\end{align*}
Evaluating at key points:

- For the maximally entangled Bell pair at $\theta=\pi/4$, $\cos^2(\pi/4)=\sin^2(\pi/4)=1/2$, yielding

$$

s_1(\pi/4) = -\left[ \tfrac12\log(\tfrac12) + \tfrac12\log(\tfrac12) \right] = \log 2 \approx 0.693147\text{ nats} \quad (= 1\text{ bit}).

$$

- In the weakly entangled limit $\theta \to 0$, with $\sin^2\theta \approx \theta^2$ and $\cos^2\theta \approx 1 - \theta^2$:

$$

s_1(\theta) \approx -(1-\theta^2)\log(1-\theta^2) - \theta^2\log(\theta^2) \approx \theta^2(1 - 2\log\theta) \to 0 .

$$



Now take $N$ independent copies of this pair — $N$ separate two-qubit systems, each prepared the same way —
and glue them together into one big state:

$$

\ket{\Phi_\theta} = \ket{\phi_\theta}_1\otimes\ket{\phi_\theta}_2\otimes\cdots\otimes\ket{\phi_\theta}_N .

$$

Group all the $R$-qubits together into "the $R$ system" and all the $L$-qubits into "the $L$ system." At
any finite $N$, this is still completely mundane: $\HH_R=(\mathbb C^2)^{\otimes N}$ is a $2^N$-dimensional
Hilbert space, $\HH=\HH_R\otimes\HH_L$ obviously factors (it's built by construction as a tensor product), and
the total reduced density operator is the $N$-fold tensor product $\rho_R^{(N)} = \rho_R^{\otimes N}$. By the additivity of von Neumann entropy across independent tensor products ($S(\rho_1 \otimes \rho_2) = S(\rho_1) + S(\rho_2)$), the $N$-pair total is exactly

$$

S_R^{(N)} = N\, s_1(\theta) .

$$

At $\theta=\pi/4$, $s_1(\pi/4)=\log2\approx0.693$. So for $N=1$, $S_R=0.693$; for $N=10$, $S_R=6.93$; for
$N=1000$, $S_R=693$. There is nothing subtle about any single one of these numbers — you could verify each
one by direct computation. The interesting physics only shows up once you ask what happens as
$N\to\infty$ while insisting on staying inside the set of states a real, finite-energy experiment could
actually reach.

### Restricting to finite energy

Suppose a Hamiltonian $H=H_R+H_L$ assigns an energy cost to flipping any given pair away from its ground
state — concretely, Liu takes $H_R=H_L=f\sum_{i=1}^N Z_i$ (footnote~4 of the paper), where $Z_i$ is the Pauli
$Z$ operator on the $i$-th spin, $Z=\ket0\bra0-\ket1\bra1$, and $f>0$ is some fixed energy scale. On a single pair in state $\ket{\phi_\theta}$, the expectation value of the single-site Pauli operator is

$$

\braket{\phi_\theta|Z_R|\phi_\theta} = \cos^2\theta\braket{0|Z|0} + \sin^2\theta\braket{1|Z|1} = \cos^2\theta - \sin^2\theta = \cos(2\theta) .

$$

Applying a spin-flip operator $X_i = \ket0\bra1 + \ket1\bra0$ to site $i$ exchanges $\ket0 \leftrightarrow \ket1$, replacing $Z_i$ with $-Z_i$ and incurring an energy cost of

$$

\Delta E_i = \braket{\Phi_\theta | X_i (f Z_i) X_i | \Phi_\theta} - \braket{\Phi_\theta | f Z_i | \Phi_\theta} = 2f \cos(2\theta) > 0 .

$$

A **finite-energy state** built on top of the reference state $\ket{\Phi_\theta}$ is one you reach by flipping only a finite number $k < \infty$ of the $N$ spins, with total excitation energy $\Delta E = 2k f \cos(2\theta) < \infty$. Flipping infinitely many spins costs $\Delta E \to \infty$, and no physical experiment supplies infinite energy.

Here is the key computation, which is worth actually doing rather than just asserting. Suppose you want to
fully disentangle $R$ from $L$ — to end up in some product state $\ket\psi_R\otimes\ket\chi_L$ with zero
entanglement entropy — starting from $\ket{\Phi_\theta}$. Because entanglement entropy is additive over the
$N$ independent pairs, and each pair individually carries entropy $s_1(\theta)>0$, disentangling requires
individually addressing (in the limiting case, individually flipping) every single one of the $N$ pairs. There
is no shortcut: you cannot remove the entanglement of pair number $573{,}241$ without doing something to pair
number $573{,}241$ specifically. As $N\to\infty$, the number of pairs you'd need to touch goes to infinity,
and so — since each one costs a fixed, nonzero amount of energy to address — does the energy required. This is
the precise content of Liu's statement (i) on p.~9: *emph* A margin note in one copy of the
paper clarifies exactly what "unentangling" means operationally here: it is *emph* — not something mysterious, just an ordinary (if very large) quantum operation, which happens to
be unavailable at finite energy in this limit.

Three consequences follow, and it is worth listing them separately because they are logically distinct facts,
not restatements of one another.


1. **Every finite-energy state has infinite entanglement.** Take any state you can reach from
$\ket{\Phi_\theta}$ by flipping finitely many spins. It still has all but finitely many of its $N$ pairs
sitting in the original entangled configuration, so its total entanglement entropy is still (a finite
correction away from) $N\,s_1(\theta)\to\infty$. There is no unentangled, or even weakly entangled, state
anywhere in the finite-energy sector — every physically reachable state is maximally, infinitely entangled
across $R|L$.
2. **The Hilbert space itself refuses to factor.** A tensor factorization $\HH=\HH_R\otimes\HH_L$ is,
among other things, a promise that unentangled product states $\ket\psi_R\otimes\ket\chi_L$ exist inside
$\HH$ — they're the simplest vectors you can write down once you have the factorization. If every
finite-energy state is infinitely entangled, no such product state can be a finite-energy state, so the
finite-energy Hilbert space $\HH_{\Phi_\theta}$ (built by completing the span of all finite-energy excitations
of $\ket{\Phi_\theta}$) simply does not contain any vectors that look like $\ket\psi_R\otimes\ket\chi_L$. Since
that is exactly what a tensor factorization requires, $\HH_{\Phi_\theta}$ cannot be written as
$\HH_R\otimes\HH_L$ for any sensible choice of $\HH_R,\HH_L$. This isn't a failure to find the right
factorization — the paper's stronger claim, which takes some sitting with, is that $\HH_{\Phi_\theta}$ is not
even a *emph* Hilbert space (one with a countable basis) in the strict $N\to\infty$ limit; it's a
much larger, less tame object, and the usual tools of quantum mechanics (which all assume separability) don't
apply to it directly at all.
3. **Different values of $\theta$ live in different worlds.** Compare $\ket{\Phi_{\theta}}$ and
$\ket{\Phi_{\theta'}}$ for $\theta\ne\theta'$. As $N\to\infty$, the amount of entanglement (hence, by the same
energy argument, the amount of energy) separating these two states diverges. They are not close to each other,
and no finite-energy operation connects one to the other. In the strict limit, they are best thought of as
two entirely separate theories that happen to share a Hamiltonian's functional form, rather than two states of
one single theory.


If you want to see the size of these numbers directly rather than just the qualitative trend, here is the
$\theta=\pi/4$ case computed explicitly at a few values of $N$ (each entry is exact, not approximate — it
follows immediately from additivity of entropy over the $N$ independent, identical pairs):


\begin{tabular}{ccccc}
\toprule
$N$ & $1$ & $10$ & $100$ & $10{,}000$ \\
\midrule
$\dim\HH_R^{(N)}=2^N$ & $2$ & $1024$ & $\approx1.3\times10^{30}$ & astronomically large \\
$S_R^{(N)}=N\log2$ & $0.693$ & $6.93$ & $69.3$ & $6931$ \\
\bottomrule
\end{tabular}

There is nothing hidden in this table — every entry is just $N\log2$, computed directly — but seeing the
entropy grow without bound while the dimension of $\HH_R^{(N)}$ explodes is the concrete picture behind the
abstract statement "$\HH_{\Phi_\theta}$ is not separable."

## The other two examples, more briefly

The paper gives two more examples (Liu's Ex.~1 and Ex.~3, Sec.~II.A), and it's worth knowing what they are
even in outline, because they come back later — the third one especially, since it's the one that actually
applies to quantum field theory and, ultimately, to AdS/CFT.

**Ex.~1: lattice gauge theory.** A gauge theory (like electromagnetism, or the strong force) has more
mathematical variables than physical degrees of freedom — you write down a field $U_{ij}$ living on each link
of a lattice, but many different configurations of $U_{ij}$ describe the exact same physics, related by
*emph* $U_{ij}\to V_iU_{ij}V_j^\dagger$. Physical states are required to be invariant
under these transformations. This requirement — not infinite entanglement, a completely different mechanism —
also breaks the naive tensor factorization $\HH=\HH_R\otimes\HH_L$, because the gauge-invariant states don't,
in general, sit inside a product of an $R$-Hilbert-space and an $L$-Hilbert-space; gauge invariance ties the
two together. This example is flagged explicitly as structurally different from the other two, and it comes
back in Sec.~III.C as a comparatively mild complication (it just adds a classical label — which
gauge/superselection sector you're in — on top of an otherwise ordinary tensor-product story), rather than the
deep, qualitative break that Ex.~2 and Ex.~3 represent.

**Ex.~3: a quantum field theory cut in half.** Take a relativistic quantum field theory (a scalar field,
say) and split space into two halves, $R=\{x>0\}$ and $L=\{x<0\}$. A quantum field has infinitely many degrees
of freedom packed into any interval of space, however small — informally, a value (or a mode) at every point.
Right at the cutting surface $x=0$, there are infinitely many field degrees of freedom on the $R$ side pressed
arbitrarily close to infinitely many on the $L$ side, all coupled to their immediate neighbors, and this
produces infinite entanglement across the cut in *emph* finite-energy state — including the vacuum, the
lowest-energy state there is. This is the field-theory version of exactly the mechanism in Ex.~2 (infinitely
many independent contributions to the entanglement, each one small but adding up to an infinite total), and it
shows up concretely as a divergence: computing the entanglement entropy of the region $R$ with a short-distance
cutoff $\epsilon$ (imagine putting the theory on a lattice with spacing $\epsilon$, which makes everything
finite and well-defined, then asking what happens as $\epsilon\to0$) gives

$$

S_R(\epsilon) = b\,\frac{\mathrm{Area}(\partial R)}{\epsilon^{d-2}} + \cdots, \qquad \epsilon\to0,

$$

(Liu's eq.~2.7) where $\partial R$ is the surface separating $R$ from $L$, $d$ is the spacetime dimension, and
$b$ is some positive, theory-dependent constant. The entropy diverges as the cutoff is removed, and it diverges
in a very specific way — proportional to the *emph* of the cutting surface, not its volume. This
"area-law divergence" is one of the most robust, model-independent facts in quantum field theory (it shows
up in essentially every explicit calculation, from free fields to interacting ones), and this paper's claim is
that it is the direct field-theoretic shadow of exactly the same Hilbert-space-non-factorization phenomenon
as the spin-pair example above — made completely precise later, in Sec.~IV.D, using the language of von
Neumann algebra types.

## The fix: define a subsystem by what you can *emph*}

Here is the resolution the paper proposes, and it is worth sitting with how simple the idea actually is
before any formalism gets attached to it. Instead of defining a subsystem $R$ by declaring a factorization
$\HH=\HH_R\otimes\HH_L$ up front, define it operationally: *emph* Concretely, that observer has access to some collection of operators
$\M\subset B(\HH)$ (the set of all bounded operators on the full Hilbert space $\HH$) — every self-adjoint
combination of things their apparatus can measure, and every unitary transformation their apparatus can
apply. Nothing about this definition requires $\HH$ to factor into anything. It only requires that you can
say, of any given operator, whether or not it belongs to the observer's toolkit.

This reframing costs nothing in the ordinary case (when $\HH=\HH_R\otimes\HH_L$ genuinely does exist, the
natural choice $\M=B(\HH_R)\otimes\id_L$ — every operator acting only on $R$ — recovers exactly the familiar
picture, as you'll see made precise in the next section), and it costs nothing in the broken case either,
because "the set of operators an $R$-observer can apply" is a perfectly sensible, well-defined thing to talk
about even when there's no factorization for it to come from. You lose nothing and gain a definition that
survives exactly the cases where the old one dies.

Naming what kind of mathematical object $\M$ should be — closed under sums, products, and the operation of
taking a Hermitian conjugate, plus some notion of being closed under limits — is precisely what a
**von Neumann algebra** is, and pinning down exactly which notion of "limit" is the right one (there
turn out to be two inequivalent choices, and the difference matters enormously) is the entire content of the
next section, Sec.~II.

This is, historically, not a new invention grafted onto quantum mechanics from outside. In the late 1920s and
early 1930s, John von Neumann — one of the people who built the mathematical foundations of quantum mechanics
in the first place, the same person behind the "Dirac—von Neumann axioms" you may have seen stated in
Sakurai — worked out, together with Francis Murray, a complete classification of exactly these kinds of
operator algebras. For decades this classification lived mostly inside pure mathematics. The claim of this
paper (built on work going back to Rehren in the 1990s, and developed intensively since roughly 2021 by
Leutheusser, Liu, and others) is that this same 1930s classification, when applied to the algebra $\M$ of an
observer's accessible operators, is *emph* a classification of how entangled that observer's
subsystem is with everything they cannot access — turning an abstract piece of 1930s functional analysis into
a working tool for 2020s quantum gravity.

## Two organizing claims, and how seriously to take them at this stage

The paper states its two central claims very early (its eq.~1.3 and the paragraph after it), and it is useful
to know, right at this stage, exactly how much has been established when you first read them, versus how much
is being promised for later. Restated:


*emph* $\;\longleftrightarrow\;$ *emph*


and, going beyond this broad classification, finer tools from the same theory (modular theory, covered in
Sec.~IV, and the crossed product, covered in Sec.~V) are claimed to give access to much sharper entanglement
information than the broad type alone.

At the point in the paper where these claims first appear, they are *emph*, not yet demonstrated. Don't
mistake the double-headed arrow above for a formal theorem with a name and a citation — it isn't one. It's a
dictionary that gets built up, entry by entry, over Secs.~III and IV: each von Neumann algebra type (I, then
II, then the various subtypes of III) is matched, on specific worked examples, to a specific qualitative
pattern of entanglement between a subsystem and its complement. By the time you finish Sec.~IV you will have
seen this correspondence demonstrated concretely enough, on examples you can check by hand, that the arrow in
eq.~1.3 will feel earned rather than asserted. That is exactly the arc this companion follows too — the
promise made here in Sec.~I is redeemed piece by piece, not all at once.

Similarly, the deeper claim that entanglement structure is what *emph* bulk spacetime geometry — the
subregion-subalgebra duality that gives this paper its title — is motivated here by pointing at the
Ryu—Takayanagi formula and the broader "entanglement builds geometry" literature (Van~Raamsdonk
[VanRaamsdonk], Maldacena—Susskind [MaldacenaSusskind]), but the actual mechanism — *emph* a
boundary algebra of a specific type turns out to be identical, not just related, to a bulk causal region's
algebra of observables — isn't built until Sec.~VII. Reading Sec.~I as ``a map of where we're going and why
people believe it's worth going there,'' rather than as a self-contained argument, is the right way to read
it; that's genuinely all a paper's introduction can do.

## Sec.~I.A: the plan of the article, translated

The paper's own plan (p.~6) splits its ten sections into two halves. It's worth restating in a way that says
*emph* the split falls where it does, since the reason is itself informative about how the argument is
built.

**Secs.~II—V: the mathematics, with no gravity or holography anywhere in sight.** This half is pure
operator-algebra theory, developed using only ordinary, finite-dimensional-friendly quantum mechanics
examples (mostly the entangled-spin-pair system from above). Sec.~II lays down what a von Neumann algebra is
and how they're classified. Secs.~III and IV show, type by type, how that classification tracks entanglement
structure — Sec.~III handles the "easy" types (I and II, where a density matrix and an entropy can still be
defined), and Sec.~IV handles type III, which cannot be tamed by a density matrix at all and needs an entirely
new tool (Tomita—Takesaki modular theory) to say anything quantitative about it. Sec.~V introduces the
*emph*, a construction that takes a type III algebra and, by literally attaching an auxiliary
quantum clock to it, produces a new, better-behaved type II algebra out of it — a purely algebraic trick at
this stage, with no physical motivation given yet, but one that turns out (starting in Sec.~IX) to be exactly
what a real physical observer, carrying a real physical clock, is doing to gravitational observables.

**Secs.~VI—IX: applying all of that machinery to quantum gravity.** Sec.~VI sets up the large-$N$
algebraic formulation of AdS/CFT itself. Sec.~VII introduces subregion-subalgebra duality — the paper's
central physics claim, that a bulk spacetime region and a specific boundary operator algebra are literally the
same object, described in two languages — and uses it to reformulate entanglement-wedge and causal-wedge
reconstruction (ideas you may already have encountered in AdS/CFT courses) in this new algebraic language.
Sec.~VIII shows how bulk causal structure, horizons, and even the question of whether two disconnected
boundary theories are joined by a wormhole, can all be read directly off the type and commutant structure of
boundary algebras, with no bulk metric assumed anywhere. Sec.~IX builds simple, fully solvable toy models
(observers with real physical clocks, crossed by the modular group exactly as in Sec.~V) that reproduce black
hole and de~Sitter entropy from nothing but this operator-algebraic machinery.

## Sec.~I.B: conventions and notation, explained rather than just listed

This short subsection (p.~8 of the paper) is easy to skim past, but every single item in it gets used, without
further comment, dozens of times later — so it's worth actually understanding each one now rather than
looking it up under pressure in Sec.~VII.


- **Large $N$ vs.\ finite $N$.** "Large-$N$" (equivalently $G_N\to0$) means doing a perturbative
expansion in powers of $1/N$ — you can keep more than just the very first (leading) term, but you're still
fundamentally treating $1/N$ as a small parameter you expand in, the same way you'd do ordinary perturbation
theory in quantum mechanics. "Finite $N$" (finite $G_N$) means the opposite: treating $N$ (or $G_N$) as an
honest, fixed number, with no expansion at all — the genuinely nonperturbative, full quantum-gravity regime.
Most of this paper works at large $N$; finite-$N$ questions are the hardest open problems, touched on mainly
in Secs.~VII.F and IX.D.
- **$\HH$, $B(\HH)$, and boundedness.** $\HH$ is a Hilbert space (a complex vector space with an
inner product, complete under the norm that inner product defines — the same notion you already know from
ordinary quantum mechanics, just possibly infinite-dimensional). $B(\HH)$ is the set of *emph*
operators on $\HH$: an operator $A$ is bounded if there's some finite number $c$ such that $\|A\ket\psi\|\le
c\|\ket\psi\|$ for every vector $\ket\psi\in\HH$ — informally, $A$ never stretches a vector's length by more
than a fixed factor, no matter which vector you feed it. Ordinary finite matrices are automatically bounded.
Some familiar quantum-mechanical operators are *emph* bounded — position $\hat x$ and momentum $\hat p$ on
a particle on a line, for instance, can make $\|A\ket\psi\|/\|\ket\psi\|$ as large as you like by choosing
$\ket\psi$ spread out far enough, or oscillating fast enough. The paper sidesteps this by simply restricting
attention to bounded operators throughout, and noting that in field theory any operator you actually care
about can be suitably smeared/regularized to become bounded (e.g., $e^{i\hat x}$ is bounded even though
$\hat x$ itself is not). This restriction is not a loss of generality worth worrying about; it's a standard
technical convenience that lets the norm-based definitions below (Sec.~II.B.1) work cleanly.
- **$\id$** is the identity operator — "do nothing."
- **$\widetilde J^\pm(Y)$: causal future and past.** For a region $Y$ in a spacetime, $\widetilde
J^+(Y)$ is the set of every point that can be reached from some point of $Y$ by a future-directed causal
curve — a path that never moves faster than light and always moves forward in time. Physically: everything $Y$
could possibly send a signal to, given unlimited time. $\widetilde J^-(Y)$ is the mirror image: everything
that could have sent a signal to some point of $Y$. (The tilde signals that these are computed in the
*emph* of the spacetime — a technical device, standard in the AdS/CFT literature, that
adds a boundary "at infinity" so that causal curves reaching arbitrarily far away are still tracked
properly; you can safely picture ordinary causal future/past for now and revisit the tilde once conformal
compactification actually matters, starting around Sec.~VI.)
- **Causal complement (single prime) and causal completion (double prime), on a spacetime region.**
The causal complement $Y'$ of a region $Y$ is everything that is spacelike separated from all of $Y$ — every
point that cannot send or receive a signal to or from any point of $Y$ within the time available; loosely,
"everything $Y$ has absolutely no causal influence on, in either direction." The causal completion $Y''$ is
the double complement, $(Y')'$ — and (this is a genuinely important geometric fact, not just a notational
curiosity) $Y''$ is generally *emph* than $Y$ itself: it's the largest region that has exactly the same
causal future and past as $Y$ does. A single point on a Cauchy slice, for instance, has a causal completion
equal to the single point itself (nothing to add), but a spatial region $R$ on a Cauchy slice has a causal
completion equal to its entire *emph* (defined next) — a genuinely bigger set, extending
into the past and future. This double-prime notation for spacetime regions is deliberately built to echo the
double-prime notation for operator commutants ($\M''$) that you'll meet in the very next section, and the
paper is relying on that echo: causal completion of a region and double-commutant closure of an algebra turn
out, once subregion-subalgebra duality is established in Sec.~VII, to be two faces of the same fact.
- **$\bar R$, complement of a spatial region; $\hat R$, domain of dependence.** If $R$ is a subregion
of a single spatial slice (a snapshot of space at one moment), $\bar R$ is just its ordinary set-complement on
that slice — everything on the same slice that isn't in $R$. $\hat R$, the domain of dependence, is a genuinely
spacetime notion built from $R$: it's every spacetime point $p$ such that *emph* causal curve through
$p$ — no matter which direction it goes, as long as it never exceeds the speed of light — must cross $R$. This
is exactly the region whose entire future *emph* past history is completely determined by data specified
on $R$ alone, which is why it's called the domain of *emph*: physics inside $\hat R$ depends only on
initial data given on $R$. For $R$ a full spatial slice, $\hat R$ is the entire spacetime. For $R$ a proper
subregion, $\hat R$ is a diamond-shaped region (a *emph*) sitting above and below $R$, bounded
by the light rays that just barely graze the edge of $R$. This shape shows up constantly from Sec.~VI onward;
it's worth actually picturing it once here.
- **$\subset$ always means *emph* A small notational point that matters: whenever
you see $\M_1\subset\M_2$ in this paper, it means $\M_1$ is strictly smaller than $\M_2$ (not equal to it) —
not the more permissive convention (allowing equality) some other texts use for the same symbol.


With this vocabulary in hand — bounded operators, causal future/past, causal complement and completion,
domain of dependence — you have everything you need to read the rest of the paper's geometric statements
literally, rather than by pattern-matching to what looks familiar. The next section builds the algebraic
machinery ($C^*$ and von Neumann algebras, states, projections, the type classification, and the GNS
construction that produces a Hilbert space from an algebra) that this section's discussion has been building
toward.
