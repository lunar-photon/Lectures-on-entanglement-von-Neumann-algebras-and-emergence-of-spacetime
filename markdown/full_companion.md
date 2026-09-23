# Reading Companion to Hong Liu's Lectures on Entanglement, von Neumann Algebras, and Emergence of Spacetime

**arXiv:2510.07017**

---



---

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

\begin{table}[t]
\centering
\footnotesize
\begin{tabularx}{\textwidth}{@{}l p{4.8cm} X@{}}
\toprule
**Symbol / Structure** & **Mathematical Definition** & **Physical Interpretation / Role** \\
\midrule
$\HH$ & Global Hilbert space of states & Total state space of the universe / system \\
$B(\HH)$ & Bounded linear operators on $\HH$ & All bounded operations and observables \\
$\M \subset B(\HH)$ & von Neumann algebra ($\M = \M''$) & Observables accessible to a local subregion / observer \\
$\M'$ & Commutant: $\{B : [B,A]=0\ \forall A \in \M\}$ & Observables of the causal complement / independent subsystem \\
$\mathcal{Z}(\M) = \M \cap \M'$ & Center of the algebra & Classical superselection sectors (trivial $\mathbb{C}\id$ for factors) \\
$\omega: \M \to \mathbb{C}$ & State (positive linear functional, $\omega(\id)=1$) & Expectation value functional $\omega(A) = \langle A \rangle$ \\
$(\pi_\omega, \HH_\omega, \ket{\Omega_\omega})$ & GNS representation & Hilbert space manufactured directly from state $\omega$ \\
$\ket\Psi \in \HH$ & Cyclic \& separating vector & Entangled vacuum / state with no local annihilators \\
$S_\Psi$ & Tomita antilinear operator: $S_\Psi A\ket\Psi = A^\dagger\ket\Psi$ & State-dependent modular involution \\
$J_\Psi$ & Modular conjugation ($J_\Psi \M J_\Psi = \M'$) & Antilinear reflection mapping algebra to its commutant (e.g. CPT) \\
$\Delta_\Psi = S_\Psi^\dagger S_\Psi$ & Modular operator ($\Delta_\Psi > 0$, self-adjoint) & Relative entanglement density / asymmetry operator \\
$h_\Psi \equiv -\log\Delta_\Psi$ & Modular Hamiltonian & Generator of intrinsic subsystem time flow (e.g. Rindler boost) \\
$\sigma_t^\Psi(A) = \Delta_\Psi^{it} A \Delta_\Psi^{-it}$ & Modular flow ($1$-parameter automorphism) & Thermal time evolution satisfying the KMS condition \\
$\widehat\M = \M \rtimes_\sigma \mathbb{R}$ & Crossed product algebra with clock $L^2(\mathbb{R})$ & Gravitationally dressed algebra including observer energy/clock \\
$\tau$ & Semifinite trace on $\widehat\M$ ($\tau(AB)=\tau(BA)$) & Renormalized trace yielding well-defined density matrices \\
$S_{\rm gen}$ & Generalized entropy: $\frac{\langle \hat A\rangle}{4G_N} + S_{\rm bulk}$ & Finite gravitational entropy in semiclassical gravity \\
$\mathcal{A}_{\rm CFT}$ & Boundary single-trace algebra ($N\to\infty$) & Generalized free fields on the holographic boundary \\
$\mathcal{A}_{\rm bulk}(b_A)$ & Bulk algebra in entanglement wedge $b_A$ & Local semiclassical bulk quantum fields dual to boundary region \\
\bottomrule
\end{tabularx}
\caption{Summary of core notation, algebraic structures, and physical interpretations used throughout this companion.}
\label{tab:notation_summary}
\end{table}

\begin{figure}[htbp]
\centering
\includegraphics[width=0.92\textwidth]{figs/fig_roadmap.pdf}
\caption{The foundational paradigm shift: Standard Hilbert space quantum mechanics (left, where subsystems are defined by tensor factors $\HH = \HH_R \otimes \HH_L$) generalizes to Algebraic Quantum Mechanics (right, where subsystems are defined by operator subalgebras $\M \subset B(\HH)$). Type I algebras represent the familiar special case where a tensor product factorization exists.}
\label{fig:roadmap}
\end{figure}

## The Conceptual Bridge: From Wavefunctions to Density Matrices to Algebraic States

To understand why the algebraic framework of this paper is so natural, it is essential to trace how our concept of a "quantum state" evolves as we move from simple undergraduate quantum mechanics to open systems, quantum field theory, and quantum gravity.


1. **Level 0: The Pure Wavefunction $\psi(x) = \braket{x|\Psi**$.}
In textbook quantum mechanics, the fundamental entity is a state vector $\ket\Psi \in \HH$ evolving according to the Schr\"odinger equation. Probabilities are given by the Born rule $P(x) = |\psi(x)|^2$. This description assumes a *emph* where an experimenter has unrestricted access to measure arbitrary operators across the entire system.
2. **Level 1: The Density Matrix $\rho(x, x')$ and Phase Space ($x_c, x_q$).**
When a system interacts with an unobserved environment or thermal bath, pure states give way to density operators $\rho = \sum_k p_k \ket{\psi_k}\bra{\psi_k}$. In the continuous position basis $\rho(x, x') = \braket{x|\rho|x'}$, it is physically illuminating to transform to Keldysh variables:

$$

x_c \equiv \frac{x + x'}{2} \quad \text{(classical midpoint coordinate)}, \qquad x_q \equiv x - x' \quad \text{(quantum coherence coordinate)}.

$$

The diagonal slice $x_q = 0$ encodes classical probabilities $P(x_c) = \rho(x_c, x_c)$, while non-zero $x_q$ tracks off-diagonal quantum interference. Fourier transforming along the quantum coordinate gives the **Wigner quasi-probability distribution**:

$$

W(x_c, p_q) = \int_{-\infty}^\infty \dd x_q\, e^{-i p_q x_q}\, \rho\!\left(x_c + \tfrac{x_q}{2},\, x_c - \tfrac{x_q}{2}\right) .

$$

While this bridges classical stochastic physics and quantum mechanics, it still fundamentally presumes that the global Hilbert space factorizes as $\HH = \HH_{\rm system} \otimes \HH_{\rm environment}$.
3. **Level 2: The Physical Limitation of Observers.**
In realistic experiments, no observer has access to the full density matrix on all of $\HH$. An observer is equipped with a restricted apparatus or confined to a spatial subregion $R$. If an observer can only measure a restricted set of observables $\M$, attempting to describe their subsystem via global pure kets produces severe mathematical pathologies (for instance, the standard relative entropy $D(\rho\|\sigma) = \Tr(\rho\log\rho - \rho\log\sigma)$ formally blows up to $+\infty$ whenever $\sigma$ is pure, because it assumes the observer is free to measure arbitrary non-commuting projection operators across the universe).
4. **Level 3: The Algebraic State $\omega: \M \to \mathbb{C**$.}
In algebraic quantum mechanics (von Neumann, Haag, and Liu), we discard the assumption that a fixed global Hilbert space is fundamental. The primary physical object is the **algebra of accessible observables $\M$**. A **state** $\omega$ is simply a positive linear functional assigning expectation values to operators:

$$

\omega(A) = \langle A \rangle_\omega, \qquad \omega(\id) = 1, \quad \omega(A^\dagger A) \ge 0 \quad \forall A \in \M.

$$

The Hilbert space $\HH_\omega$ and state vector $\ket{\Omega_\omega}$ are not postulated in advance; they are **dynamically manufactured** from the algebraic state $\omega$ via the Gelfand—Naimark—Segal (GNS) construction:

$$

\omega(A) = \braket{\Omega_\omega | \pi_\omega(A) | \Omega_\omega} .

$$



\begin{keyresult}
**The Conceptual Takeaway:** The wavefunction $\psi(x)$ is not a universal container of physical reality; it is merely one specific GNS representation of an algebraic state $\omega$ on a Type I algebra. When moving to the thermodynamic limit ($N\to\infty$), local subregions in QFT, or semiclassical black holes, the Hilbert space tensor factorization dissolves, but the algebraic state $\omega$ remains exact, rigorous, and well-defined.
\end{keyresult}

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

\begin{figure}[htbp]
\centering
\includegraphics[width=0.75\textwidth]{figs/fig_qubit_entropy.pdf}
\caption{The single-pair entanglement entropy $s_1(\theta) = -\cos^2\theta\log(\cos^2\theta) - \sin^2\theta\log(\sin^2\theta)$ as a function of the mixing angle $\theta \in (0, \pi/4]$. The entropy peaks at the maximally entangled Bell state $\theta = \pi/4$ ($s_1 = \log 2 \approx 0.693$) and vanishes smoothly as $\theta \to 0$. For $N$ pairs, the total entropy scales as $S_R^{(N)} = N s_1(\theta) \to \infty$ as $N \to \infty$.}
\label{fig:qubit_entropy}
\end{figure}

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

\begin{figure}[htbp]
\centering
\includegraphics[width=0.75\textwidth]{figs/fig_area_law.pdf}
\caption{The UV area-law divergence of entanglement entropy in quantum field theory: dividing space across a boundary $\partial R$ couples short-distance modes across the cut with UV cutoff $\epsilon$. The leading entanglement entropy diverges as $S_R \sim \mathrm{Area}(\partial R)/\epsilon^{d-2}$, reflecting the infinite entanglement of the underlying Type $\mathrm{III}_1$ local algebra.}
\label{fig:area_law}
\end{figure}

## Explicit Derivation: Why the Continuum QFT Hilbert Space Cannot Factorize
\label{sec:qft_nonfactorization_derivation}

Because the claim that "$\HH \ne \HH_R \otimes \HH_L$ in continuum QFT" is so fundamental to everything that follows, it is illuminating to derive this result explicitly using nothing more advanced than the quantum mechanics of coupled harmonic oscillators.

### 1. The Hamiltonian and the spatial gradient coupling

Consider a free, real scalar field $\phi(t, \vec x)$ with mass $m$ in $d$ spacetime dimensions ($d-1$ spatial dimensions). The field Hamiltonian on a constant-time Cauchy slice is
\begin{equation}
H = \int \dd^{d-1}x \left[ \frac{1}{2}\pi(\vec x)^2 + \frac{1}{2}\big(\vec\nabla\phi(\vec x)\big)^2 + \frac{1}{2}m^2\phi(\vec x)^2 \right],
\label{eq:scalar_hamiltonian_continuum}
\end{equation}
where $\pi(\vec x)$ is the canonical momentum field satisfying $[\phi(\vec x), \pi(\vec y)] = i\delta^{(d-1)}(\vec x - \vec y)$.

Now divide space into two halves by a planar boundary at $x = 0$:

$$

R = \{ (x, \vec x_\perp) : x > 0 \}, \qquad L = \{ (x, \vec x_\perp) : x < 0 \},

$$

where $\vec x_\perp = (x^2, \dots, x^{d-1})$ denotes the $(d-2)$ spatial coordinates parallel to the entangling surface $\partial R$.

To isolate the physics right at the boundary, we discretize the perpendicular $x$-direction on a spatial lattice with lattice spacing $\epsilon$, while Fourier-transforming the continuous transverse coordinates $\vec x_\perp$ into transverse momentum modes $\vec k_\perp$:

$$

\phi(x, \vec x_\perp) = \int \frac{\dd^{d-2}k_\perp}{(2\pi)^{d-2}} \, \widetilde\phi(x, \vec k_\perp) \, e^{i \vec k_\perp \cdot \vec x_\perp} .

$$

For each transverse momentum mode $\vec k_\perp$, the Hamiltonian decomposes into an independent 1D chain of coupled harmonic oscillators with effective mass parameter
\begin{equation}
M^2 \equiv m^2 + |\vec k_\perp|^2 .
\label{eq:effective_mass_transverse}
\end{equation}
On the lattice in the $x$-direction, the continuous field becomes discrete site operators $\phi_j(\vec k_\perp) \equiv \widetilde\phi(j\epsilon, \vec k_\perp)$ with conjugate momenta $\pi_j(\vec k_\perp)$, where $j = \dots, -2, -1$ lies in $L$ and $j = 0, 1, 2, \dots$ lies in $R$.

The spatial gradient in the direction perpendicular to the boundary is discretized via finite differences:
\begin{equation}
\int \dd x \, \frac{1}{2}\left(\frac{\partial\phi}{\partial x}\right)^2 \;\longrightarrow\; \sum_j \frac{\epsilon}{2} \left( \frac{\phi_{j+1} - \phi_j}{\epsilon} \right)^2 = \sum_j \frac{1}{2\epsilon} (\phi_{j+1} - \phi_j)^2 .
\label{eq:lattice_gradient_sum}
\end{equation}
Notice the crucial interaction link directly straddling the entangling cut between site $j = -1$ (the closest site in $L$) and site $j = 0$ (the closest site in $R$):
\begin{equation}
H_{\rm cut} = \frac{1}{2\epsilon} (\phi_0 - \phi_{-1})^2 = \frac{1}{2\epsilon} (\phi_R - \phi_L)^2 ,
\label{eq:h_cut_interaction}
\end{equation}
where for clarity we define $\phi_R \equiv \phi_0$ and $\phi_L \equiv \phi_{-1}$.

### 2. The two-oscillator subsystem across the entangling cut

To see the mechanism with complete clarity, isolate this two-mode system across the interface. The Hamiltonian for these two adjacent oscillators is
\begin{equation}
H_{\rm pair} = \frac{1}{2}\pi_R^2 + \frac{1}{2}\pi_L^2 + \frac{1}{2}M^2(\phi_R^2 + \phi_L^2) + \frac{1}{2\epsilon^2}(\phi_R - \phi_L)^2 .
\label{eq:pair_hamiltonian}
\end{equation}
(Rescaling fields to canonical dimensions $\phi \to \phi/\sqrt{\epsilon}$, $\pi \to \pi\sqrt{\epsilon}$ leaves $[\phi, \pi] = i$ and puts the coupling parameter as $k_{\rm cut} = 1/\epsilon^2$).

Because this is a quadratic system, we diagonalize it exactly using normal mode coordinates:
\begin{equation}
\phi_+ \equiv \frac{\phi_R + \phi_L}{\sqrt{2}}, \qquad \phi_- \equiv \frac{\phi_R - \phi_L}{\sqrt{2}} .
\label{eq:normal_mode_coords}
\end{equation}
In terms of $\phi_\pm$, the Hamiltonian decouples into two uncoupled harmonic oscillators:
\begin{equation}
H_{\rm pair} = \left( \frac{1}{2}\pi_+^2 + \frac{1}{2}\omega_+^2 \phi_+^2 \right) + \left( \frac{1}{2}\pi_-^2 + \frac{1}{2}\omega_-^2 \phi_-^2 \right),
\label{eq:decoupled_pair_hamiltonian}
\end{equation}
whose normal mode eigenfrequencies are
\begin{align}
\omega_+ &= M = \sqrt{m^2 + |\vec k_\perp|^2}, \label{eq:omega_plus} \\
\omega_- &= \sqrt{M^2 + \frac{2}{\epsilon^2}} = \sqrt{m^2 + |\vec k_\perp|^2 + \frac{2}{\epsilon^2}} \approx \frac{\sqrt{2}}{\epsilon} \quad \text{as } \epsilon \to 0 . \label{eq:omega_minus}
\end{align}

### 3. Ground state correlations vs. product state correlations

The ground state of the decoupled system is the product of two Gaussian ground state wavefunctions in the normal coordinates:
\begin{equation}
\Psi_0(\phi_+, \phi_-) = \left( \frac{\omega_+ \omega_-}{\pi^2} \right)^{1/4} \exp\left[ -\frac{1}{2}\omega_+\phi_+^2 - \frac{1}{2}\omega_-\phi_-^2 \right] .
\label{eq:ground_state_normal}
\end{equation}
Transforming back to the physical local fields $\phi_R, \phi_L$ using eq.~\eqref{eq:normal_mode_coords}:
\begin{align}
\Psi_0(\phi_R, \phi_L) &= \left( \frac{\omega_+ \omega_-}{\pi^2} \right)^{1/4} \exp\left[ -\frac{1}{4}(\omega_+ + \omega_-)(\phi_R^2 + \phi_L^2) - \frac{1}{2}(\omega_+ - \omega_-)\phi_R \phi_L \right] .
\label{eq:ground_state_physical}
\end{align}
Notice the cross-coupling term $\frac{1}{2}(\omega_- - \omega_+)\phi_R \phi_L$. Because $\omega_- \approx \sqrt{2}/\epsilon \gg \omega_+$, this cross-term is extraordinarily large. 

In the true vacuum state $\ket\Omega$:

- The expectation value of the relative difference between the two sides is suppressed:
\begin{equation}
\braket{\Omega | (\phi_R - \phi_L)^2 | \Omega} = 2 \braket{\Omega | \phi_-^2 | \Omega} = \frac{2}{2\omega_-} = \frac{1}{\omega_-} \approx \frac{\epsilon}{\sqrt{2}} .
\label{eq:vacuum_diff_exp}
\end{equation}
- The gradient energy of the cut in the vacuum state is therefore finite per mode:
\begin{equation}
\braket{\Omega | H_{\rm cut} | \Omega} = \frac{1}{2\epsilon^2} \braket{\Omega | (\phi_R - \phi_L)^2 | \Omega} = \frac{1}{2\epsilon^2} \frac{1}{\omega_-} \approx \frac{1}{2\sqrt{2}\epsilon} .
\label{eq:vacuum_cut_energy}
\end{equation}
This is the standard zero-point vacuum energy density, which is subtracted when computing excitation energies.


### 4. The energetic impossibility of unentangled product states

Now, suppose for the sake of contradiction that the Hilbert space factorizes across the cut:

$$

\HH \stackrel{?}{=} \HH_L \otimes \HH_R .

$$

If this factorization were valid, the Hilbert space must contain unentangled product states of the form
\begin{equation}
\ket{\Psi_{\rm prod}} = \ket{\psi_L} \otimes \ket{\chi_R} \in \HH ,
\label{eq:hypothetical_product_state}
\end{equation}
where $\ket{\psi_L} \in \HH_L$ and $\ket{\chi_R} \in \HH_R$.

In *emph* such product state, by the definition of a tensor product, any operator in $L$ and any operator in $R$ have exactly zero quantum covariance:
\begin{equation}
\braket{\Psi_{\rm prod} | \phi_R \phi_L | \Psi_{\rm prod}} = \braket{\chi_R | \phi_R | \chi_R} \braket{\psi_L | \phi_L | \psi_L} .
\label{eq:product_state_covariance_zero}
\end{equation}
For states with zero mean field ($\braket{\phi_R} = \braket{\phi_L} = 0$, as in any symmetric fluctuation), this means $\braket{\phi_R \phi_L}_{\rm prod} = 0$ identically!

Evaluating the expectation value of the difference squared in this product state gives:
\begin{align}
\braket{\Psi_{\rm prod} | (\phi_R - \phi_L)^2 | \Psi_{\rm prod}} &= \braket{\phi_R^2}_{\chi_R} + \braket{\phi_L^2}_{\psi_L} - 2\braket{\phi_R}_{\chi_R}\braket{\phi_L}_{\psi_L} \nonumber \\
&= \braket{\phi_R^2}_{\chi_R} + \braket{\phi_L^2}_{\psi_L} .
\label{eq:prod_diff_squared}
\end{align}
By the Heisenberg uncertainty principle for each oscillator, the fluctuations are bounded strictly from below:

$$

\braket{\phi_R^2}_{\chi_R} \ge \frac{1}{2\Omega_R}, \qquad \braket{\phi_L^2}_{\psi_L} \ge \frac{1}{2\Omega_L} .

$$

In particular, for any state with localized, finite-energy wavepackets of width $\sim \epsilon$, the single-site fluctuation is bounded by the uncoupled ground state scale:
\begin{equation}
\braket{\Psi_{\rm prod} | (\phi_R - \phi_L)^2 | \Psi_{\rm prod}} \ge \frac{1}{2\omega_+} = \frac{1}{2\sqrt{m^2 + |\vec k_\perp|^2}} = \mathcal{O}(1) \quad (\text{finite, independent of } \epsilon) .
\label{eq:prod_fluctuation_lower_bound}
\end{equation}
Notice the striking difference between eq.~\eqref{eq:vacuum_diff_exp} and eq.~\eqref{eq:prod_fluctuation_lower_bound}:

- In the entangled vacuum, $\braket{(\phi_R - \phi_L)^2} \sim \mathcal{O}(\epsilon) \to 0$ as the lattice spacing vanishes.
- In *emph* product state, $\braket{(\phi_R - \phi_L)^2} \ge \mathcal{O}(1)$ remains strictly finite as $\epsilon \to 0$, because the absence of entanglement prevents the field values on adjacent sides from fluctuating in lockstep!


Now compute the gradient energy across the boundary link in this product state:
\begin{equation}
\braket{\Psi_{\rm prod} | H_{\rm cut} | \Psi_{\rm prod}} = \frac{1}{2\epsilon^2} \braket{\Psi_{\rm prod} | (\phi_R - \phi_L)^2 | \Psi_{\rm prod}} \ge \frac{1}{4\epsilon^2 \sqrt{m^2 + |\vec k_\perp|^2}} .
\label{eq:hcut_prod_divergence}
\end{equation}
Subtracting the vacuum zero-point energy (eq.~\eqref{eq:vacuum_cut_energy}), the excess excitation energy required to sever the entanglement of this single transverse mode across the cut is
\begin{equation}
\Delta E_{\rm cut}(\vec k_\perp) = \braket{\Psi_{\rm prod} | H_{\rm cut} | \Psi_{\rm prod}} - \braket{\Omega | H_{\rm cut} | \Omega} \ge \frac{1}{4M\epsilon^2} - \frac{1}{2\sqrt{2}\epsilon} \sim \frac{1}{4M\epsilon^2} > 0 .
\label{eq:delta_e_single_mode}
\end{equation}

### 5. Integration over the entangling surface and the non-factorization theorem

To obtain the total excitation energy required to prepare the unentangled product state $\ket{\psi_L}\otimes\ket{\chi_R}$ across the entire boundary surface $\partial R$, we integrate $\Delta E_{\rm cut}(\vec k_\perp)$ over all transverse spatial coordinates $\vec x_\perp$, or equivalently over all transverse momentum modes $|\vec k_\perp| \le \Lambda_{\rm UV} \sim 1/\epsilon$:
\begin{align}
\Delta E_{\rm prod} &= \mathrm{Area}(\partial R) \int_{|\vec k_\perp| \le 1/\epsilon} \frac{\dd^{d-2}k_\perp}{(2\pi)^{d-2}} \, \Delta E_{\rm cut}(\vec k_\perp) \nonumber \\
&\ge \mathrm{Area}(\partial R) \int_{|\vec k_\perp| \le 1/\epsilon} \frac{\dd^{d-2}k_\perp}{(2\pi)^{d-2}} \, \frac{1}{4\epsilon^2 \sqrt{m^2 + |\vec k_\perp|^2}} .
\label{eq:total_prod_energy_integral}
\end{align}
Evaluating the radial momentum integral in $d$ spacetime dimensions ($d \ge 3$):

$$

\int_0^{1/\epsilon} k_\perp^{d-3} \frac{\dd k_\perp}{k_\perp} \sim \int_0^{1/\epsilon} k_\perp^{d-4} \dd k_\perp \sim \left(\frac{1}{\epsilon}\right)^{d-3} .

$$

Multiplying by the prefactor $\frac{1}{\epsilon^2}$:
\begin{keyresult}
\begin{equation}
\Delta E_{\rm prod} \ge C \cdot \frac{\mathrm{Area}(\partial R)}{\epsilon^{d-1}} \;\xrightarrow{\;\epsilon \to 0\;} \; +\infty ,
\label{eq:product_state_energy_divergence}
\end{equation}
where $C > 0$ is a strictly positive, theory-dependent geometric constant.
\end{keyresult}

Equation~\eqref{eq:product_state_energy_divergence} is the definitive physical proof of non-factorizability:

1. **Infinite energy barrier**: The physical energy required to unentangle a spatial subregion $R$ from its complement $L$ diverges as $\epsilon^{-(d-1)}$ in the continuum limit. Any attempt to enforce a tensor product state requires creating an infinite gradient discontinuity at $\partial R$.
2. **Expulsion from the physical Hilbert space**: The physical Hilbert space $\HH$ of a continuum quantum field theory consists solely of finite-energy states (mathematically, states in the Fock space or GNS space of the vacuum). Because $\Delta E_{\rm prod} = +\infty$, *emph*.
3. **Failure of factorization**: A tensor product $\HH_L \otimes \HH_R$ is, by definition, spanned by product vectors $\ket{\psi_L}\ket{\chi_R}$. Because $\HH$ contains zero product vectors, we reach an inescapable mathematical conclusion:
\begin{equation}
\boxed{\HH \ne \HH_L \otimes \HH_R \quad \text{in any continuum relativistic quantum field theory.}}
\label{eq:non_factorization_conclusion}
\end{equation}


### 6. The algebraic corollary: Type $\mathrm{III_1$ and the split property}

This energetic divergence explains why local subregions in QFT cannot be described by Type I algebras:

- If two spatial regions $R_1$ and $R_2$ are separated by a **finite buffer distance** $\delta > 0$ (so $\text{dist}(R_1, R_2) = \delta$), the gradient energy across the gap is regularized by $\delta$. In that case, an unentangled product state *emph* be prepared, but at an energy cost scaling as $\exp(c/\delta^n)$. The mathematical statement that product states exist for strictly separated regions is known in axiomatic QFT as the **Doplicher—Longo split property**: there exists an intermediate Type I factor $\mathcal{N}$ such that $\M(R_1) \subset \mathcal{N} \subset \M(R_2')'$.
- However, as the buffer distance is sent to zero ($\delta \to 0$, so the regions touch at a common boundary), the split property collapses, the energy diverges to $+\infty$, and the local algebra $\M(R)$ ceases to be Type I or Type II — it becomes an intrinsically entangled **Type $\mathrm{III**_1$ factor}.


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



---

# Sec.~II: Introduction to von Neumann algebras

Sec.~I ended with a proposal: define a subsystem not by splitting the Hilbert space, but by naming the
collection of operators an observer confined to that subsystem has access to. This section makes that
proposal completely precise. By the end of it you will know exactly what mathematical object $\M$ is required
to be, exactly how such objects are classified into types, and exactly how a Hilbert space can be
*emph* from an algebra and a state, rather than assumed as a starting point. Every definition
below is followed by a worked example with actual numbers — matrices you could multiply out by hand — because
the definitions are genuinely abstract on first reading and the only way to make them feel concrete is to
watch them act on something small.

## Sec.~II.A: systems with an infinite amount of entanglement (recap)

This subsection of the paper is the one worked through in full in Sec.~I of this companion (the $N$-Bell-pair
chain, the lattice gauge theory example, and the quantum field theory cut in half). Nothing new needs to be
added here — if anything in that discussion felt unclear, it's worth going back to it now, since everything
from here on assumes it's solid ground. The one thing worth restating, because the entire rest of this
section builds on it: the moral of Sec.~I was that a subsystem should be defined by *emph*, not by how the Hilbert space happens to split. Sec.~II.B now makes that idea into an
actual mathematical definition.

## Sec.~II.B.1: von Neumann algebras as subsystems

### Setting the stage: what a Hilbert space and an operator are, restated carefully

Before the new definition, it's worth being completely explicit about the ingredients, because the new
definition is going to be a statement *emph* them, and vague pictures of "vectors" and "operators"
won't be precise enough to support what comes next.

A Hilbert space $\HH$ is a vector space over the complex numbers, equipped with an inner product
$\braket{\cdot|\cdot}$ (a rule assigning a complex number $\braket{\xi|\eta}$ to any pair of vectors, linear
in the second argument, conjugate-linear in the first, with $\braket{\xi|\xi}\ge0$ and equal to zero only for
the zero vector), and complete in the sense that any sequence of vectors that "ought to" converge (a Cauchy
sequence, one whose terms get arbitrarily close to each other) actually does converge to some vector in
$\HH$. For a spin-$\tfrac12$ particle, $\HH=\mathbb C^2$: vectors are pairs of complex numbers
$(c_1,c_2)$, usually written $c_1\ket0+c_2\ket1$, and the inner product is the ordinary dot product with
complex conjugation, $\braket{\xi|\eta}=\xi_1^*\eta_1+\xi_2^*\eta_2$. Nothing about a von Neumann algebra
requires anything more exotic than this — the infinite-dimensional case (a quantum field, say) uses the exact
same definitions, just with infinitely many components instead of two.

An operator $A$ on $\HH$ is a rule that turns vectors into vectors, $A:\HH\to\HH$, and is linear:
$A(c_1\ket{\xi_1}+c_2\ket{\xi_2})=c_1 A\ket{\xi_1}+c_2A\ket{\xi_2}$. On $\mathbb C^2$, every linear operator is
just a $2\times2$ matrix, and $A\ket\xi$ is ordinary matrix-vector multiplication. The **Hermitian
conjugate** (or adjoint) $A^\dagger$ of $A$ is the unique operator satisfying
$\braket{\xi|A\eta}=\braket{A^\dagger\xi|\eta}$ for all $\xi,\eta$ — on a finite matrix, this is exactly the
familiar "transpose and complex-conjugate every entry" operation. $A$ is **self-adjoint** (or
Hermitian) if $A=A^\dagger$; these are exactly the operators that can represent physical observables, because
their eigenvalues are automatically real numbers — the kind of number a measurement can actually return.
$B(\HH)$ denotes the set of *emph* bounded operators on $\HH$ (bounded was defined in Sec.~I.B above —
informally, operators that don't stretch any vector's length by more than some fixed factor).

### The new definition of subsystem

Here is Liu's definition, restated with every piece spelled out. Suppose you have access to only some subset
of operators, $\M\subset B(\HH)$ — not everything, just the things your particular apparatus, in your
particular location, with your particular capabilities, can measure or apply. Given some state $\ket\Psi\in
\HH$ of the full system, two things are available to you using only $\M$: you can compute expectation values
$\braket{\Psi|A|\Psi}$ for $A\in\M$ (predict what a measurement of $A$ would read, on average, over many
repetitions), and you can act on the state, producing $B\ket\Psi$ for $B\in\M$ (actually change the system by
applying an operation you have access to). Whatever set $\M$ happens to be, it should be closed under three
operations, because each one corresponds to something an observer with access to $\M$ can obviously already
do: if you can measure/apply $A$ and $B$, you can measure/apply $A+B$ (do both, add the results) and $AB$ (do
one after the other); and if $A$ is something you can measure, so is $A^\dagger$ (for a self-adjoint $A$ this
is trivial, $A^\dagger=A$; more generally it just says your toolkit is closed under the basic operation of
taking an adjoint). A set closed under these three operations — sums, products, and adjoints — is called a
**$*$-subalgebra** of $B(\HH)$ (the $*$ refers to the adjoint operation, often written $A^*$ in pure math
texts instead of $A^\dagger$).

That alone isn't quite enough. You also want $\M$ to be *emph*, in the sense that if you can
approximate some operator arbitrarily well using things in $\M$, that operator should count as being in $\M$
too — otherwise "the set of things you have access to" would have artificial, arbitrary gaps in it. This is
where the story gets genuinely subtle, because — and this is the crux of the entire next subsection — there
turn out to be two different, inequivalent ways to make "approximate arbitrarily well" precise, and the
choice between them changes everything.

With this notion of subsystem in hand, the **complement** of $\M$ is defined as its commutant,

$$

\M' = \{B\in B(\HH) : BA=AB\ \ \forall A\in\M\} .

$$

Read this slowly, because the single most common way to misread it is dangerous enough to be worth flagging
immediately: $\M'$ is *emph* the set of operators that all commute *emph*. It is the set
of operators that *emph* commute with *emph*. Two different
operators sitting inside $\M'$ can perfectly well fail to commute with each other — in fact, whenever $\M'$ is
itself a rich enough algebra (which it usually is), it absolutely does contain non-commuting pairs, the same
way $\M$ does. The only promise $\M'$ makes is directional: act with anything in $\M'$, and it produces zero
interference with any measurement made using $\M$. That is the entire operational content of ``complement of
a subsystem'' here — not "the other half of a tensor factorization you could point to," but ``everything
guaranteed, as a matter of algebra, not to disturb what $\M$ can measure.'' If you want to see this worked out
with the full functional-analysis machinery spelled out in more detail than this paper includes, Walter
Thirring's *emph* is a standard place to look — but nothing beyond what's given
here is needed to follow the rest of this paper.


> [!NOTE] **Physics Connection: Spacelike Commutativity**
> You already know one instance of this idea from ordinary relativistic field theory, and it's worth making the
> connection completely explicit, because it's the cleanest possible bridge from this abstract definition to
> something you can compute. For a free scalar field $\phi$, the commutator of the field at two spacetime points
> is a fixed, state-independent function (not an operator at all — a genuine $c$-number, since for a free field
> $[\phi(x),\phi(y)]$ works out to be proportional to the identity),
> 
$$

> [\phi(x),\phi(y)] = i\Delta(x-y) ,
> 
$$

> where $\Delta$ (the Pauli—Jordan function) is built from an integral over the field's on-shell momenta. The
> textbook fact — provable directly from this integral representation, using nothing but Lorentz invariance —
> is that $\Delta(x-y)=0$ identically whenever $x-y$ is spacelike. The one-line reason it *emph* to vanish
> there: $\Delta$ depends on $x-y$ only through Lorentz-invariant combinations, but for a spacelike separation
> there's no Lorentz-invariant way to say "$x$ is later than $y$" or vice versa — a boost can flip which one
> comes first. Since the commutator is manifestly antisymmetric, $[\phi(x),\phi(y)]=-[\phi(y),\phi(x)]$, and yet
> Lorentz invariance forbids it from depending on an ordering that isn't even well-defined, the only
> Lorentz-invariant, antisymmetric quantity available is zero. This is exactly why microcausality — the
> requirement that spacelike-separated field operators commute — comes out automatically from the free-field
> construction, rather than needing to be imposed as an extra axiom.
> 
> Now translate this into the language of this section. Let $\M(O)$ be the algebra generated by field operators
> smeared over a spacetime region $O$, and $O'$ its causal complement (spacelike-separated from all of $O$).
> The vanishing of $\Delta$ for spacelike separation says exactly $\M(O')\subseteq\M(O)'$ — this is precisely
> the "locality" axiom already stated abstractly, without proof, back in Sec.~IV.D.3 (eq.~4.57) of this
> companion. **So the commutant $\M(O)'$ isn't just *emph* What the
> abstract definition of $\M'$ in this section adds on top of that familiar fact is the observation, flagged
> explicitly above, that $\M(O)'$ can be *emph* than $\M(O')$ — it can contain operators that
> are timelike separated from $O$ but still happen to commute with everything in it, for reasons that have
> nothing to do with relativistic causality and everything to do with the specific state and representation.
> Nothing about the free-field commutator changes; what's new is only the recognition that ``commutes with
> $\M$'' is a strictly more general, purely algebraic notion than "is spacelike separated from $\M$" — and
> it's exactly this extra room that Sec.~VIII.A puts to work, reading genuine bulk causal structure off of a
> richer boundary commutant than boundary causality alone would ever require.


## Sec.~II.B.2: basic properties, $C^*$ vs.\ von Neumann algebras, and the double commutant theorem

### Two notions of "the limit of a sequence of operators"

Take a sequence of operators $A_1,A_2,A_3,\dots$ in $\M$, and ask: does it converge to some operator $A$? For
ordinary numbers, "converges" has one obvious meaning. For operators, there are (at least) two natural, and
genuinely different, notions.

**Norm convergence.** Every bounded operator has a norm, $\|A\|$ — the smallest number such that
$\|A\ket\psi\|\le\|A\|\,\|\ket\psi\|$ for every vector $\ket\psi$ (the "maximum stretch factor" from
Sec.~I.B). It satisfies the identity $\|A^\dagger A\|=\|A\|^2$ (Liu's eq.~2.8) — worth checking on a simple
case: for $A=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}$ acting on $\mathbb C^2$, direct computation gives
$A^\dagger A = \begin{psmallmatrix}0&0\\0&1\end{psmallmatrix}$, whose largest eigenvalue is $1$, so
$\|A^\dagger A\|=1$; and $\|A\|$ itself (the largest singular value of $A$) is also $1$, so
$\|A^\dagger A\|=1=1^2=\|A\|^2$, consistent. A sequence $A_n$ is **norm convergent** to $A$ if
$\|A_n-A\|\to0$: the maximum possible discrepancy between $A_n\ket\psi$ and $A\ket\psi$, over *emph*
unit vector $\ket\psi$ simultaneously, shrinks to zero. This is a strong, uniform statement.

**Weak convergence.** $A_n$ is **weakly convergent** to $A$ if $\braket{\xi|A_n|\eta}\to
\braket{\xi|A|\eta}$ for every *emph* of vectors $\ket\xi,\ket\eta$. This only asks that individual
matrix elements converge, one pair of vectors at a time — a much weaker demand, because it doesn't require the
convergence rate to be uniform across all vectors at once.

In finite dimensions the two notions turn out to coincide for the specific sequences you'd usually write down
by hand — which is exactly why this distinction never comes up in an ordinary quantum mechanics course — but
they are genuinely different notions in general, and the gap between them is precisely where infinite-dimensional
phenomena (quantum field theory, the $N\to\infty$ limit) live.


> [!EXAMPLE] **Worked Example:**
> Let $\HH = \ell^2(\mathbb N)$ be the infinite-dimensional Hilbert space of square-summable sequences, with standard orthonormal basis $\{\ket 1, \ket 2, \ket 3, \dots\}$. Consider the sequence of rank-1 projection operators
> 
$$

> P_n \equiv \ket n\bra n .
> 
$$

> Let us test the convergence of $P_n$ under all three topologies as $n\to\infty$:
> 
1. **Weak convergence ($P_n \to 0$ weakly):** Take any two vectors $\ket\xi = \sum_{k=1}^\infty c_k\ket k$ and $\ket\eta = \sum_{k=1}^\infty d_k\ket k$ with $\sum |c_k|^2 < \infty$ and $\sum |d_k|^2 < \infty$. The matrix element is
> 
$$

> \braket{\xi|P_n|\eta} = \braket{\xi|n}\braket{n|\eta} = c_n^* d_n .
> 
$$

> By the Cauchy—Schwarz inequality for series, $\sum_{n=1}^\infty |c_n d_n| \le \sqrt{\sum |c_n|^2}\sqrt{\sum |d_n|^2} < \infty$, so the sequence of terms must converge to zero: $\lim_{n\to\infty} c_n^* d_n = 0$. Thus $\braket{\xi|P_n|\eta} \to 0$ for *emph* pair of states. The sequence converges weakly to the zero operator: $P_n \xrightarrow{\text{weak}} 0$.
> 
>
2. **Strong convergence ($P_n \to 0$ strongly):** The strong operator topology requires $\|P_n\ket\psi\| \to 0$ for every fixed vector $\ket\psi = \sum c_k\ket k$. We compute the norm:
> 
$$

> \|P_n\ket\psi\|^2 = \|\ket n\braket{n|\psi}\|^2 = |c_n|^2 \to 0 \quad \text{as } n\to\infty .
> 
$$

> Thus $P_n \xrightarrow{\text{strong}} 0$.
> 
>
3. **Norm convergence ($P_n \not\to 0$ in norm):** The operator norm measures the maximum stretch over *emph* normalized vectors simultaneously:
> 
$$

> \|P_n - 0\| = \sup_{\|\psi\|=1} \|P_n\ket\psi\| = \|P_n\ket n\| = \|\ket n\| = 1 .
> 
$$

> For every single $n$, $\|P_n - 0\| = 1$. It never shrinks! Hence $P_n$ does *emph* converge in norm to 0: $P_n \xrightarrow{\text{norm}} \text{does not exist}$.
>

> This is the archetypal example: matrix elements settle down to zero, but the operator as a whole never gets small in norm.


A $*$-subalgebra $\M$ complete under norm convergence (every norm-convergent sequence in $\M$ has its limit
back in $\M$) is called a **$C^*$-algebra**. A $*$-subalgebra complete under the weaker, weak
convergence is called a **von Neumann algebra**. Since norm convergence automatically implies weak
convergence (a uniformly-shrinking discrepancy certainly implies each individual matrix element settles down),
every sequence that's norm-Cauchy is also weakly Cauchy, and so every von Neumann algebra is automatically
also a $C^*$-algebra — von Neumann algebras are the strictly more complete, more restrictive notion.

Which one is the physically correct notion of "subsystem"? Weak convergence, and it's worth being clear
about why: what you actually measure in a laboratory is a matrix element, $\braket{\xi|A|\eta}$ — an
expectation value, or more generally a transition amplitude. Weak convergence is exactly the statement that
every one of these directly measurable quantities settles down. So von Neumann algebras, not the more
restrictive $C^*$-algebras, are the objects that correctly capture ``the set of operators whose physical
predictions are under control,'' and that's why they, not $C^*$-algebras, are the workhorse of the rest of
this paper.

One more asymmetry between the two, flagged already in Sec.~I.B.2's companion discussion but worth repeating
here at the point where it starts to matter: a $C^*$-algebra can be defined completely abstractly, with no
Hilbert space anywhere — just a vector space with a product, an adjoint, and a norm satisfying $\|A^\dagger
A\|=\|A\|^2$, complete in that norm. You could specify one purely by its multiplication table and norm, the
way you'd specify a finite group by its multiplication table, with no reference to any particular set of
vectors it acts on. A von Neumann algebra cannot be defined this way, because its defining completeness
condition — weak convergence — is stated directly in terms of vectors $\ket\xi,\ket\eta$ living in some
specific $\HH$. This asymmetry is not a minor technicality; it is precisely the gap that the GNS construction
(Sec.~II.D, worked through in full below) exists to close: starting from nothing but an abstract $C^*$-algebra
and a state on it, GNS manufactures the missing Hilbert space, and only then can you ask whether the algebra,
represented on that Hilbert space, happens to also be weakly closed (a von Neumann algebra) or not.

### The double commutant theorem

Checking weak-convergence completeness directly — verifying that *emph* weakly convergent sequence in
$\M$ has its limit back in $\M$ — sounds like it could require checking infinitely many sequences. Von
Neumann's double commutant theorem turns this topological chore into a two-line algebraic check:

$$

\M = \M'' \iff \M \text{ is weakly closed (a von Neumann algebra).}

$$

Here $\M''\equiv(\M')'$, the commutant of the commutant. Read the logic carefully: you take the complement of
your subsystem ($\M'$, everything guaranteed not to disturb $\M$), and then take the complement of
*emph* ($\M''$, everything guaranteed not to disturb anything in $\M'$). The theorem says this process,
applied twice, lands you exactly back where you started — but only if $\M$ was already a legitimate von
Neumann algebra to begin with; if $\M$ was merely a $*$-subalgebra (closed under sums, products, adjoints, but
not yet weakly closed), $\M''$ is in general strictly bigger than $\M$ — it's the *emph* von Neumann
algebra containing $\M$, i.e., $\M$ together with every operator you can approximate using $\M$ in the weak
sense. This is a genuinely remarkable fact (not an obvious one — it's a real theorem, with a real proof
involving the structure of Hilbert space geometry) precisely because it means a purely algebraic operation
(take the commutant, twice) automatically performs a topological completion (weak closure) for you, with no
limiting procedure required in the definition at all.


> [!EXAMPLE] **Worked Example:**
> Let $\HH=\mathbb C^2\otimes\mathbb C^2$ — two
> qubits, call them $R$ and $L$, so $\HH$ is 4-dimensional. Let $\M$ be every operator of the form $A\otimes
> \id_L$ for $A$ an arbitrary $2\times2$ matrix (every operation you could perform using only apparatus touching
> qubit $R$, doing nothing to qubit $L$). As a vector space, $\M$ is spanned by four matrices: the identity
> $\id_2$ and the three Pauli matrices $\sigma_x,\sigma_y,\sigma_z$, each tensored with $\id_L$:
> 
$$

> \id_2=\begin{pmatrix}1&0\\0&1\end{pmatrix},\ \
> \sigma_x=\begin{pmatrix}0&1\\1&0\end{pmatrix},\ \
> \sigma_y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\ \
> \sigma_z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
> 
$$

> Every $2\times2$ matrix is some combination $c_0\id_2+c_1\sigma_x+c_2\sigma_y+c_3\sigma_z$ (this is just
> saying the four Pauli matrices, including the identity, form a basis for all $2\times2$ matrices — a standard
> fact, and easy to check directly: writing out a general $2\times2$ matrix $\begin{psmallmatrix}a&b\\c&d
> \end{psmallmatrix}$ and matching coefficients gives $c_0=\tfrac{a+d}2$, $c_3=\tfrac{a-d}2$,
> $c_1=\tfrac{b+c}2$, $c_2=\tfrac{b-c}{2i}$, which always has a solution).
> 
> To find $\M'$: you need every $4\times4$ matrix $X$, written in the basis $\ket{00},\ket{01},\ket{10},\ket{11}$ (first digit is $R$, second is $L$), satisfying $[\sigma_i\otimes\id_L,\,X]=0$ for all $\sigma_i$. Rather than treating $X$ as an opaque $16\times16$ system, we can solve it by writing $X$ as four $2\times2$ blocks:
> 
$$

> X = \begin{pmatrix} X_{11} & X_{12} \\ X_{21} & X_{22} \end{pmatrix}, \qquad X_{ij} \in M_2(\mathbb C) .
> 
$$

> Now evaluate the commutator with each generator of $\M$:
> 
1. Commutator with $\sigma_z \otimes \id_L = \begin{pmatrix} \id_2 & 0 \\ 0 & -\id_2 \end{pmatrix}$:
> 
$$

> [\sigma_z\otimes\id_L, \, X] = \begin{pmatrix} \id_2 & 0 \\ 0 & -\id_2 \end{pmatrix} \begin{pmatrix} X_{11} & X_{12} \\ X_{21} & X_{22} \end{pmatrix} - \begin{pmatrix} X_{11} & X_{12} \\ X_{21} & X_{22} \end{pmatrix} \begin{pmatrix} \id_2 & 0 \\ 0 & -\id_2 \end{pmatrix} = \begin{pmatrix} 0 & 2X_{12} \\ -2X_{21} & 0 \end{pmatrix} = 0 .
> 
$$

> This forces the off-diagonal blocks to vanish identically: $X_{12} = 0$ and $X_{21} = 0$. So $X = \begin{pmatrix} X_{11} & 0 \\ 0 & X_{22} \end{pmatrix}$ must be block-diagonal.
> 
>
2. Commutator with $\sigma_x \otimes \id_L = \begin{pmatrix} 0 & \id_2 \\ \id_2 & 0 \end{pmatrix}$:
> 
$$

> [\sigma_x\otimes\id_L, \, X] = \begin{pmatrix} 0 & \id_2 \\ \id_2 & 0 \end{pmatrix} \begin{pmatrix} X_{11} & 0 \\ 0 & X_{22} \end{pmatrix} - \begin{pmatrix} X_{11} & 0 \\ 0 & X_{22} \end{pmatrix} \begin{pmatrix} 0 & \id_2 \\ \id_2 & 0 \end{pmatrix} = \begin{pmatrix} 0 & X_{22} - X_{11} \\ X_{11} - X_{22} & 0 \end{pmatrix} = 0 .
> 
$$

> This forces the two diagonal blocks to be identical: $X_{22} = X_{11} \equiv B$.
>

> Therefore, any commuting matrix $X$ must have the exact form:
> 
$$

> X = \begin{pmatrix} B & 0 \\ 0 & B \end{pmatrix} = \id_R \otimes B , \qquad B \in M_2(\mathbb C) .
> 
$$

> Since $B$ is an arbitrary $2\times2$ matrix on subsystem $L$, this proves directly that $\M' = \id_R \otimes B(\HH_L)$!
> 
> Now compute the second commutant $\M'' = (\M')'$: an operator $Y = \begin{pmatrix} Y_{11} & Y_{12} \\ Y_{21} & Y_{22} \end{pmatrix}$ in $\M''$ must commute with every $\id_R \otimes B = \begin{pmatrix} B & 0 \\ 0 & B \end{pmatrix}$. This requires $[Y_{ij}, B] = 0$ for *emph* $2\times2$ matrix $B$. By Schur's lemma, the only $2\times2$ matrices commuting with all of $M_2(\mathbb C)$ are scalar multiples of the identity: $Y_{ij} = a_{ij} \id_2$. Thus
> 
$$

> Y = \begin{pmatrix} a_{11}\id_2 & a_{12}\id_2 \\ a_{21}\id_2 & a_{22}\id_2 \end{pmatrix} = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} \otimes \id_L = A \otimes \id_L = \M .
> 
$$

> So, checked directly and analytically step-by-step: $\dim\M=4$, $\dim\M'=4$, $\dim\M''=4$, and $\M''=\M$. This is the double commutant theorem, verified by hand on the smallest non-trivial subsystem!
> 
> A second example is worth doing too, because it shows what happens when $\M$ is *emph* simply ``all
> operators on one tensor factor,'' and it previews something important for later (the notion of a
> *emph*, coming up two subsections from now). Take the same $\HH=\mathbb C^4$, but now forget any
> tensor-product structure and let $\M$ be spanned by just two matrices, $P_1=\mathrm{diag}(1,1,0,0)$ and
> $P_2=\mathrm{diag}(0,0,1,1)$ — the algebra available to an observer who can only tell whether the system is
> in "block one" or "block two," nothing finer. Solving the same kind of linear system: $\M'$ turns out to
> be 8-dimensional (every operator that acts as an arbitrary $2\times2$ block within each of the two sectors
> separately, without mixing them — an 8-real-dimensional space, i.e., two independent $2\times2$ complex
> matrices), and $\M''$ comes back out to be exactly $\M$ again, 2-dimensional. Notice something new here that
> didn't happen in the first example: $\M\subset\M'$ — both $P_1$ and $P_2$ individually commute with
> *emph* in the block-diagonal algebra $\M'$, including with each other and with themselves (trivially
> true for any operator, but here it's also true relative to the much bigger algebra $\M'$). Whenever
> $\M\subset\M'$ like this — an algebra small enough that it commutes with its own complement, and hence with
> itself in this stronger sense — you're looking at an algebra with a genuinely nontrivial *emph*, and
> that turns out to signal something physically important: $\M$ is not describing one indivisible subsystem, but
> a classical label (which block you're in) sitting on top of possibly-further subsystems within each block.
> This comes back explicitly in the discussion of "general type I" algebras below.


\begin{quote}
**Where the entangled subsystem lives.** Putting the last two subsections together: a subsystem is a von
Neumann algebra $\M\subset B(\HH)$; its complement is the commutant $\M'$; and bipartite entanglement, once
this framework is adopted, becomes a statement about the pair $(\M,\M')$, not about a tensor factorization.
When $\HH=\HH_R\otimes\HH_L$ genuinely exists, choosing $\M=B(\HH_R)\otimes\id_L$ recovers exactly the
familiar story — that's precisely the first worked example above, and it's the special case that Sec.~III.B
calls a *emph*.
\end{quote}

A handful of further algebraic facts about commutants, stated in the paper without much comment (its
eqs.~2.12—2.16), are worth having explicitly on hand, because they get used freely later with no further
explanation: for any $*$-subalgebra $\Alg$ (not yet necessarily weakly closed), $\Alg'=\Alg'''$ (its commutant
is automatically already a full von Neumann algebra, since a short argument shows $\Alg'=(\Alg')''$ directly);
$\M\equiv\Alg''$ is the smallest von Neumann algebra containing $\Alg$, and it has the same commutant as
$\Alg$ does, $\M'=\Alg'$. Given two von Neumann algebras $\M_1,\M_2$, their **join** $\M_1\vee\M_2\equiv
(\M_1\cup\M_2)''$ is the smallest von Neumann algebra containing both, and their **meet** $\M_1\wedge
\M_2\equiv\M_1\cap\M_2$ is simply their intersection (already automatically a von Neumann algebra, so no
double-commutant is needed on that side); and these satisfy a De~Morgan-style duality,
$(\M_1\vee\M_2)'=\M_1'\wedge\M_2'$ — joining two algebras and then taking the complement gives the same
answer as taking each complement first and then intersecting them.

The **center** of $\M$ is $Z(\M)\equiv\M\cap\M'$: operators that commute with everything in $\M$
*emph* everything in $\M'$ simultaneously — the second worked example above, with $Z(\M)=\M$ itself
(since $\M\subset\M'$ there), is exactly a case where the center is as large as it could possibly be. $\M$ is
called a **factor** (or is said to be **primary**) if its center is as small as it can possibly be
instead, $Z(\M)=\mathbb C\,\id$ — only multiples of the identity, nothing else. The first worked example above,
$\M=B(\HH_R)\otimes\id_L$, is a factor: the only operator of the form $A\otimes\id_L$ that is simultaneously
of the form $\id_R\otimes B$ is a multiple of the identity (immediate from comparing the two forms directly).
A general von Neumann algebra can always be decomposed into a direct sum (or, more generally, a direct
integral) of factors, so from here on — and for essentially the whole rest of the paper — attention is
restricted to factors, since the classification of general von Neumann algebras reduces to classifying
factors plus bookkeeping the classical (center) labels on top.

## Sec.~II.B.3: weights and states

### The definitions

A **linear functional** $\omega$ on $\M$ is simply a rule assigning a complex number $\omega(A)$ to
every $A\in\M$, respecting addition and scalar multiplication: $\omega(aA+bB)=a\,\omega(A)+b\,\omega(B)$, and
compatible with the adjoint, $\omega(A^\dagger)=\omega(A)^*$ (Liu's eq.~2.17). It is a **weight** if it's
also positive, $\omega(A^\dagger A)\ge0$ for every $A$ (eq.~2.18) — the natural requirement that
"$A^\dagger A$" (which plays the role of $|A|^2$ for operators — it's always a non-negative operator, the
operator analogue of a squared magnitude) should never get assigned a negative number. It is a **state**
if, further, it's normalized, $\omega(\id)=1$ (eq.~2.21). It is a **trace** if it satisfies
$\omega(AB)=\omega(BA)$ (eq.~2.20) — the same cyclic property the ordinary matrix trace has, $\Tr(AB)=\Tr(BA)$.
Combining positivity with linearity gives a useful inequality for free (Liu's eq.~2.19, a direct analogue of
the ordinary Cauchy—Schwarz inequality you already know from vector inner products):
$|\omega(A^\dagger B)|^2\le\omega(A^\dagger A)\,\omega(B^\dagger B)$.

$\omega$ is one rule doing one thing: it assigns a single number, $\omega(A)$, to each $A\in\M$. What that
number means depends only on which operator you feed it, not on any change to $\omega$ itself. Feed it a
general observable $A$, and $\omega(A)$ is its expectation value. Feed it a projection $P_I$ instead — the
spectral projection onto some range of possible outcomes, Sec.~II.B.5 — and $\omega(P_I)$ is the probability
of that outcome, because positivity and normalization already force $0\le\omega(P_I)\le1$, with
$\omega(P_{I_1})+\omega(P_{I_2})=\omega(P_{I_1\cup I_2})$ for disjoint ranges. Same formula, same $\omega$; the
two readings — expectation value, probability — come entirely from what sits inside the parentheses.

Crucially — and this is the entire point of introducing weights and states this way rather than immediately
reaching for a density matrix — none of these definitions mention a Hilbert space, a vector, or a density
operator. $\omega$ is defined purely as a number assigned to every element of the algebra $\M$, full stop.
(It *emph* be shown, and is stated as a fact in the paper without proof, that every physically sensible —
"normal," meaning weakly-continuous — state $\omega$ on $\M\subset B(\HH)$ does secretly correspond to an
ordinary density operator $\rho$ on $\HH$, via $\omega(A)=\Tr(\rho A)$, eq.~2.23; but the definition of
$\omega$ itself never needed to assume this in advance — it's a consequence, not an input.) $\omega$ is
**faithful** if $\omega(A^\dagger A)=0$ forces $A=0$ (nothing nonzero is invisible to it), and it is
**pure** if it cannot be written as a nontrivial mixture $\omega=\lambda\omega_1+(1-\lambda)\omega_2$ of
two different states for some $0<\lambda<1$ (eq.~2.24) — if it *emph*, $\omega$ is said to **dominate**
$\omega_1$ and $\omega_2$.

### What happens to the wavefunction once the algebra is taken as primary

The paper states this section's definitions in one dense paragraph and moves on, but they deserve to be
slowed down and unpacked completely, because they are exactly what demotes the wavefunction from a
fundamental object to a derived one.

An ordinary quantum-mechanical state is a vector $\ket\psi$ (or, more generally, a density matrix $\rho$).
Both of those are objects that live *emph* or *emph* a Hilbert space — you cannot even write down
$\ket\psi$ without first having $\HH$ in hand. The definition of $\omega$ just given requires none of that: it
is a number assigned to each algebra element, and the algebra $\M$ can, as already discussed, be specified
completely abstractly (as a $C^*$-algebra), with no Hilbert space anywhere in the definition. This is not a
cosmetic reformulation — it is a genuine change in which object is treated as fundamental. In the ordinary
picture, you start with $\HH$, then pick a vector $\ket\psi\in\HH$, then compute $\braket\psi{A}\psi$ for
whatever operators you like. In this picture, you start with the algebra $\M$ (the measurable/doable things)
and a state $\omega$ on it (an assignment of an expected outcome to every element of $\M$), and *emph*, if you want one, do you construct a Hilbert space and a vector that reproduce $\omega$ — this
construction is the GNS construction, covered in full two subsections from now. The vector you get out of
that construction is not fundamental data; it's a derived bookkeeping device, specific to the particular state
$\omega$ you started with, and a different choice of state can produce an entirely different, physically
inequivalent Hilbert space.

Notice also that $\omega$ is required to be *emph*: $\omega(A+B)=\omega(A)+\omega(B)$. This is already
telling you that $\omega$ describes an *emph* over many repetitions, not a single measurement outcome
on one system. A single measurement of "$A+B$" on one particular system doesn't obviously split into ``the
result you'd have gotten for $A$'' plus "the result you'd have gotten for $B$" — you generally can't even
measure $A$ and $B$ together unless they happen to commute. But the *emph*, over a large ensemble of
identically prepared systems, of $A+B$ does split that way automatically, just from linearity of averaging.
So $\omega$ (equivalently the density matrix $\rho$, equivalently in the pure case the vector $\ket\psi$) was
never describing one individual system to begin with — it was already, by the very shape of its definition, a
statement about an ensemble.

Slavnov's paper (in your Resources folder) makes this completely explicit by going one level deeper than Liu
does here, and it's worth walking through, because it answers ``then what *emph* describe one individual
system'' directly. Slavnov starts from something more primitive than $\omega$: a functional $\varphi(\hat A)$,
defined not on the whole algebra linearly, but only on one maximal set of *emph*
(jointly measurable, i.e.\ commuting) observables at a time, that returns the actual number a single
measurement of $\hat A$, on this one specific system, right now, would read out. There's no averaging in this
definition at all — $\varphi$ is a record of one concrete measurement outcome. The catch, and it's the
important part: because measuring one observable can disturb your ability to also measure something that
doesn't commute with it, no experiment can ever pin down $\varphi$ completely. All any experiment can tell you
is that $\varphi$ belongs to some *emph* of functionals that all agree with your data on the
one compatible set of observables $\{Q\}$ you actually chose to measure. Slavnov's proposal, argued in detail
in his Sec.~3, is that **this equivalence class — not $\varphi$ itself — is what a conventional
"quantum state" $\Psi_Q$ actually is.** It's not a container of hidden, definite properties; it is a precise
bookkeeping of exactly how much you could possibly know, given that measuring one thing costs you the ability
to have measured something incompatible with it.

This single idea explains, without needing any further postulate, several things that otherwise look like
separate mysteries:


- **Why quantum probability isn't "we just don't know the hidden variable yet."** The very same
individual $\varphi$ can belong to a different equivalence class, $\Psi_P=\{\varphi\}_P$ instead of
$\Psi_Q=\{\varphi\}_Q$, depending on which compatible set — $\{Q\}$ or $\{P\}$ — an experimenter chooses to
measure. *emph* "quantum state" your system is assigned to depends on an experimental choice made
after the system was prepared. Slavnov identifies this directly as the root of the Einstein—Podolsky—Rosen
puzzle (his Sec.~4) — not a separate, additional weirdness of quantum mechanics, but the same fact wearing a
different hat.
- **Why $\rho$, not $\ket\psi$, is what enters every physical prediction.** $\rho$ (equivalently
$\omega$) was already, by construction, one level of ensemble-averaging removed from an individual $\varphi$.
Sakurai's own move — replacing $\ket\psi$ with $\rho=\ket\psi\bra\psi$ as the truly fundamental object, so
that both pure and mixed states are handled uniformly — is the first half of exactly this demotion; the
algebraic framework in this paper carries it the rest of the way, replacing $\rho$ (which needs a Hilbert
space to be written down as a matrix) with $\omega$ (which doesn't).
- **Why the Hilbert space shows up at all, and in what sense it's "second stage."** Slavnov states
this outright, and it's worth quoting the idea directly: *emph* The primary elements are the algebra of
observables and the state (in either Slavnov's individual-measurement sense $\varphi$, or Liu's
ensemble-average sense $\omega$) directly tied to experiment. The Hilbert space, the vectors, the operators
acting on them — every bit of that is manufactured afterward, mechanically, by the GNS construction, from
whichever of these two more primitive objects you start with.


So, to state the answer plainly, in one place: the wavefunction is not a physical entity that stores values
the way a hard drive stores bits. It is the name for an equivalence class of individually-indistinguishable,
in-principle-definite measurement outcomes, indistinguishable precisely because no experiment could have told
them apart given what was actually chosen to be measured. The algebra — what's actually measurable, and how
those measurements combine — is the observer-independent, primary structure. The wavefunction is downstream
of a choice of what you decided to look at.

## Sec.~II.B.4: $C^*$ and von Neumann algebras generated by a single operator

This subsection is short, and mostly self-contained once you have the two definitions from Sec.~II.B.2 in
hand, but it's worth doing carefully because it's the concrete reason projections (the subject of the very
next subsection) have to live in the von Neumann algebra and generally cannot live in the smaller
$C^*$-algebra.

Take one bounded, self-adjoint operator $\mathcal O$, and ask: what's the smallest $C^*$-algebra containing
it, $\Alg(\mathcal O)$, and the smallest von Neumann algebra containing it, $\M(\mathcal O)$? Both certainly
contain every polynomial in $\mathcal O$ (sums of $c_n\mathcal O^n$), since polynomials are automatically
generated by repeated multiplication and addition — but each also needs to be completed, in its own notion of
limit, to actually be a full $C^*$- or von Neumann algebra.

The **spectrum** $\sigma(\mathcal O)$ of $\mathcal O$ is the set of numbers $\kappa$ for which
$\mathcal O-\kappa\id$ fails to be invertible — for a finite Hermitian matrix, this is exactly the set of its
eigenvalues, the numbers a measurement of $\mathcal O$ could actually return. It's a fact (stated without
proof in the paper, footnote~10, citing a standard functional-analysis reference) that $\Alg(\mathcal O)$ is
isomorphic to the algebra of *emph* functions on $\sigma(\mathcal O)$: every element of
$\Alg(\mathcal O)$ can be written as $f(\mathcal O)$ for some continuous function $f$, and vice versa. This is
a reasonable thing to believe on a simple example: for a finite Hermitian matrix with distinct eigenvalues
$\kappa_1,\dots,\kappa_n$, any polynomial (or any continuous function, defined via its Taylor series or via
uniform approximation by polynomials) applied to $\mathcal O$ just means applying that function to each
eigenvalue separately, leaving the eigenvectors alone — so specifying $f(\mathcal O)$ really is the same data
as specifying a continuous function on the finite set $\{\kappa_1,\dots,\kappa_n\}$ (on a finite set every
function is automatically continuous, so this example doesn't yet show the distinction that's about to
matter — but it correctly shows the general shape of the isomorphism).


> [!NOTE] **Physics Connection: Eigenvalues vs.\ Eigenvectors**
> The definition of $\sigma(\mathcal O)$ just given never mentions an eigenvector or a Hilbert space: $\lambda\in
> \sigma(\mathcal O)$ purely because $\mathcal O-\lambda\id$ has no inverse inside $\Alg$. So eigenvalues do not
> need demoting the way $\ket\Omega$ did in Sec.~II.D — they were already an algebra-level notion, fixed before
> any state or representation is chosen. What does get demoted is the eigen*emph*: that object lives in
> whatever Hilbert space GNS happens to build for a given $\omega$, so it only appears once $\omega$ is chosen.
> 
> Check this on the number operator $N=a^\dagger a$ from the oscillator algebra. Its spectrum is fixed by
> $[a,a^\dagger]=1$ alone, with no Hilbert space in the argument. Suppose $Nv=\lambda v$ for some nonzero $v$
> (in whichever representation you like). From $[N,a]=-a$: $N(av)=(\lambda-1)(av)$, so $av$ is zero or an
> eigenvector at $\lambda-1$. From $[N,a^\dagger]=a^\dagger$: $a^\dagger v$ is an eigenvector at $\lambda+1$, and
> it is never zero ($a^\dagger v=0$ would force $Nv=(aa^\dagger-1)v=-v$, i.e.\ $\lambda=-1$, contradicting
> $\lambda=\omega(N)\ge0$ from positivity). Lowering by $1$ repeatedly can never go below $0$, so the chain must
> terminate exactly there — forcing $\lambda\in\{0,1,2,\dots\}$, the oscillator's quantized levels, derived from
> the algebra's multiplication table before any Hilbert space, wavefunction, or eigenvector enters. Choosing a
> state $\omega$ and running GNS only decides which eigenvector shows up, and with what weight; it never
> changes the spectrum itself.


$\M(\mathcal O)$, in contrast, is isomorphic to the algebra of *emph* (not necessarily continuous)
functions on $\sigma(\mathcal O)$. Since every continuous function on a compact set is automatically bounded,
$\Alg(\mathcal O)\subset\M(\mathcal O)$ — consistent with von Neumann algebras being the more complete,
larger objects. The difference becomes concrete, and important, once $\sigma(\mathcal O)$ is not just a finite
set of isolated points but a continuum (an interval of real numbers, as happens once $\mathcal O$ has a
continuous spectrum — exactly the generic case in field theory or in the $N\to\infty$ limit this paper cares
about). On a continuum, the **indicator function** of a subset $I\subset\sigma(\mathcal O)$,

$$

f_I(\kappa) = \begin{cases} 1 & \kappa\in I \\ 0 & \kappa\notin I \end{cases} ,

$$

is bounded (it only ever takes the values $0$ or $1$) but is discontinuous wherever $I$ has a boundary inside
the continuum. The operator $P_I\equiv f_I(\mathcal O)$ this corresponds to is exactly a **spectral
projection** — the projector onto the part of $\mathcal O$'s eigenspace with eigenvalue in $I$, the operator
that answers the yes/no question "does a measurement of $\mathcal O$ land in the range $I$?" Because
indicator functions are essentially never continuous, spectral projections generically live in $\M(\mathcal
O)$ but not in $\Alg(\mathcal O)$. This is the concrete, checkable reason von Neumann algebras — not merely
$C^*$-algebras — are the right home for the entire classification that follows in the next two subsections:
that classification is built entirely out of projections, and $C^*$-algebras are, in general, too
norm-continuous to even contain the sharp yes/no measurement operators the classification needs.

## Sec.~II.B.5: projections

### Definitions, and what they mean physically

A **projection** is a self-adjoint operator $P$ with $P^2=P$ (applying it twice does nothing more than
applying it once — the algebraic signature of "select a subspace and discard everything orthogonal to it,"
which is exactly what a sharp yes/no measurement does). Because the spectral theorem lets you write any
self-adjoint operator as a combination of its own spectral projections (as just discussed in Sec.~II.B.4
above), a von Neumann algebra is entirely spanned by its projections — this is why the whole classification
that follows can be phrased purely in terms of them, with no loss of generality.


> [!NOTE] **Physics Connection: Probabilities from Projections**
> Sec.~II.B.3 already made the point that $\omega(P_I)$ reads as a probability exactly because $P_I$ is a
> projection. It's worth tracing that fact to where it comes from: Sec.~II.B.4 fixed the possible outcomes of
> measuring $\mathcal O$ as its spectrum $\sigma(\mathcal O)$ — an algebra-intrinsic fact, decided before any
> state is chosen — and for a range $I\subset\sigma(\mathcal O)$, the spectral projection $P_I$ built from
> $\mathcal O$ (Sec.~II.B.4's indicator-function construction) is itself an element of $\Alg$. This is exactly
> Postulate~3 from Sec.~I (the Born rule, $\braket{\psi|P_I|\psi}$) with $\ket\psi$ replaced by $\omega$: the
> probability of an outcome is not a second thing $\omega$ supplies on top of expectation values — it is
> $\omega$ evaluated at one particular algebra element, the spectral projection for that outcome, using the same
> rule $\omega$ uses for everything else.



> [!EXAMPLE] **Worked Example:**
> Let $A = \sigma_x + \sigma_z = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ be an observable on $\mathbb C^2$. Let us construct its spectral projections explicitly:
> 
1. **Eigenvalues:** The characteristic equation is $\det(A - \lambda\id) = \lambda^2 - 2 = 0$, giving eigenvalues $\lambda_\pm = \pm\sqrt{2}$.
>
2. **Spectral projections via Lagrange interpolation:** For any $2\times2$ matrix with distinct eigenvalues $\lambda_1, \lambda_2$, the projection onto the eigenspace of $\lambda_1$ is $P_1 = \frac{A - \lambda_2\id}{\lambda_1 - \lambda_2}$. Thus:
> 
$$

> P_+ = \frac{A - (-\sqrt2)\id}{\sqrt2 - (-\sqrt2)} = \frac{1}{2\sqrt2}\begin{pmatrix} 1+\sqrt2 & 1 \\ 1 & -1+\sqrt2 \end{pmatrix} ,
> 
$$

> 
$$

> P_- = \frac{A - (\sqrt2)\id}{-\sqrt2 - \sqrt2} = \frac{1}{2\sqrt2}\begin{pmatrix} \sqrt2-1 & -1 \\ -1 & \sqrt2+1 \end{pmatrix} .
> 
$$

>
3. **Verification of projector axioms:**
> 


>
8. **Born rule probabilities:** Suppose the system is in the state $\ket\psi = \ket0 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$. The probability of measuring eigenvalue $+\sqrt2$ is:
> 
$$

> \operatorname{Prob}(+\sqrt2) = \braket{0|P_+|0} = \frac{1+\sqrt2}{2\sqrt2} = \frac12 + \frac{1}{2\sqrt2} \approx 0.853553 .
> 
$$

> The probability of measuring $-\sqrt2$ is:
> 
$$

> \operatorname{Prob}(-\sqrt2) = \braket{0|P_-|0} = \frac{\sqrt2-1}{2\sqrt2} = \frac12 - \frac{1}{2\sqrt2} \approx 0.146447 .
> 
$$

> Their sum is $0.853553 + 0.146447 = 1.000000$, and the expectation value is:
> 
$$

> \braket{A} = (+\sqrt2)(0.853553) + (-\sqrt2)(0.146447) = \sqrt2(0.707106) = 1.000000 = \braket{0|\sigma_x+\sigma_z|0} .
> 
$$

>

> This demonstrates how spectral projections decompose observables into exact, orthogonal yes/no propositions.


There is an exact correspondence between projections in $B(\HH)$ and closed subspaces of $\HH$: a projection
$P$ picks out the subspace $P\HH$ (everything you get by applying $P$ to every vector in $\HH$), and
conversely any closed subspace has a unique projection onto it. If $P\in\M$, the subspace $P\HH$ is said to
"belong to $\M$" — physically, it's a subspace an observer with access to $\M$ can single out by measurement.
The largest possible projection is the identity $\id$ (the whole space); projections are partially ordered by
$P\le Q$ meaning $PQ=P$ (equivalently, $P\HH\subseteq Q\HH$ — the subspace of $P$ sits entirely inside the
subspace of $Q$).

Two projections $P,Q\in\M$ are called **Murray—von Neumann equivalent** (written $P\sim Q$) if there is
a **partial isometry** $V\in\M$ — an operator that maps its input subspace to its output subspace
without stretching or shrinking lengths — with $P=V^\dagger V$ and $Q=VV^\dagger$ (eq.~2.28). This says $V$
maps the subspace $P\HH$ isometrically (length-preservingly) onto the subspace $Q\HH$, and crucially, using
only an operator $V$ that is itself available inside $\M$. This is the algebra-relative version of ``these
two subspaces have the same size'' — not the ordinary linear-algebra notion of dimension (which only cares
about the subspace itself, not what operators are available to compare it to other subspaces), but a notion
tied specifically to what the observer with access to $\M$ can actually do.


> [!EXAMPLE] **Worked Example:**
> Return to $\M=B(\HH_R)\otimes\id_L$ on $\HH=\mathbb C^2\otimes\mathbb C^2$ from the
> double-commutant example above. Let $P=\ket0_R\!\bra0_R\otimes\id_L$ and $Q=\ket1_R\!\bra1_R\otimes\id_L$ —
> each is a rank-2 projection on the full 4-dimensional $\HH$ (it picks out a 2-dimensional subspace: fix the
> $R$-qubit to $\ket0$ or $\ket1$ respectively, and allow the $L$-qubit to be anything). The operator
> $V=\ket1_R\!\bra0_R\otimes\id_L$ is manifestly in $\M$ (it has exactly the form $A\otimes\id_L$, with
> $A=\ket1\bra0$), and direct matrix multiplication gives $V^\dagger V=\ket0_R\!\bra0_R\otimes\id_L=P$ and
> $VV^\dagger=\ket1_R\!\bra1_R\otimes\id_L=Q$. So $P\sim Q$: they're equivalent, using an isometry that lives
> entirely inside $\M$ — exactly capturing the intuitive fact that "the $R$-qubit is $\ket0$" and ``the
> $R$-qubit is $\ket1$'' are subspaces of the same size, related by a flip an $R$-observer can actually perform.


A nonzero projection $P$ is called **finite** if it is *emph* equivalent (in the sense just defined)
to any strictly smaller projection $Q<P$ inside $\M$; it is called **infinite** if such a smaller-but-
equivalent $Q$ does exist. This definition takes some getting used to, because it explicitly does *emph*
match the ordinary linear-algebra notion of finite-dimensional. Liu's own example (eq.~2.27) makes this vivid,
and the accompanying margin note in one copy of the paper — ``looks like smallest, something to do with
irrep? looks like it maps onto some copy of irrep'' — is worth taking seriously and sharpening into something
precise, because it's most of the way to the right idea.

Take $\M=B(\HH_1)\otimes\id_2$ on $\HH=\HH_1\otimes\HH_2$, with $\HH_2$ *emph*-dimensional, and let
$P=\ket\psi\rangle\langle\psi|\otimes\id_2$ for a single unit vector $\ket\psi\in\HH_1$. As a subspace of the
full (infinite-dimensional) $\HH$, $P\HH$ is itself infinite-dimensional — it's a whole copy of the
infinite-dimensional $\HH_2$. And yet $P$ is a *emph* projection of the algebra $\M$: there is no
strictly smaller, $\M$-equivalent projection below it, because within $\M\cong B(\HH_1)$, $P$ already
corresponds to the smallest possible nonzero rank — rank one, a single basis vector's worth, within
$\HH_1$ — and nothing smaller than "a single basis direction" exists to equate it with. Here is the precise
version of the margin note's instinct: forgetting the specific Hilbert space it happens to act on, $\M$ as an
*emph* is isomorphic to $B(\HH_1)$ — a single copy of the algebra of all operators on
$\HH_1$, i.e., a single irreducible representation of "what an observer with access to $\HH_1$ can do." The
factor $\HH_2$ in $\HH=\HH_1\otimes\HH_2$ is doing nothing but counting *emph* of that one
irrep sit side by side inside the big Hilbert space (one copy for every basis vector of $\HH_2$). The
projection $P=\ket\psi\rangle\langle\psi|\otimes\id_2$ picks out one basis direction *emph* of the irrep, while touching every one of the (infinitely many) copies simultaneously — which is
precisely why it's "as small as $\M$ can make something" (finite, in fact minimal, within the algebra)
while still being infinite-dimensional as a raw subspace of $\HH$. **Finiteness, in this algebra-relative
sense, is a statement about the irrep, not about the raw dimension of the ambient Hilbert space** — and
internalizing that distinction now is what makes the type classification in the next subsection make sense at
all, rather than looking like a strange abuse of the word "finite."

A projection $P$ is called **minimal** in $\M$ if it is nonzero and $\M$ contains no nonzero projection
strictly smaller than $P$ — the algebra-relative notion of ``as small as a measurement outcome can possibly
be.'' Every minimal projection is automatically finite (there's nothing smaller to be equivalent to), but as
the example above shows, a projection can be finite without being minimal, and (this becomes the entire
substance of the classification two subsections from now) an algebra can fail to have *emph* minimal
projections at all, while still having plenty of finite ones.

For a von Neumann *emph* $\M$ specifically, the identity operator $\id$ itself is either finite or
infinite (by the definitions just given, applied to $P=\id$), and this single fact — is the biggest possible
projection, $\id$, finite or infinite? — is used to name a coarse dichotomy: if $\id$ is finite, every
projection in $\M$ must also be finite (this can be shown from the definitions, though the proof is not given
in the paper), and $\M$ is called a **finite von Neumann factor**; if $\id$ is infinite, $\M$ is called an
**infinite von Neumann factor**, and in that case it turns out (also stated without proof) that any two
infinite projections in $\M$ are automatically equivalent to each other, and in particular every infinite
projection is equivalent to the identity itself.

## Sec.~II.C: classification of von Neumann factors

### Building a dimension function out of nothing but $\sim$ and $\le$

Here is the payoff of the last two subsections. Given the equivalence relation $P\sim Q$ and the ordering
$P\le Q$, it is a genuine theorem (not proved in the paper, but stated as fact) that for any von Neumann
*emph* $\M$, there exists a **dimension function** $d(P)\ge0$, defined for every projection
$P\in\M$, satisfying two properties that pin it down (up to an overall constant you're free to rescale):
$d(P)<d(Q)$ whenever $P<Q$ strictly, and $d(P)=d(Q)$ whenever $P\sim Q$. In words: $d$ assigns a number to
each projection that respects both the ordering (bigger subspace, bigger number) and the equivalence relation
(algebra-equivalent subspaces get exactly the same number) — exactly the two properties you'd want out of
anything worthy of being called a "size." This $d$ can equally be packaged as a **trace**
$\tr(P)\equiv d(P)$, extended from projections to all of $\M$ by linearity (using that every self-adjoint
operator is built from its spectral projections, as in Sec.~II.B.4) — and this $\tr$ is exactly the object
that plays the role of the ordinary matrix trace, generalized to make sense on an abstract algebra with no
particular Hilbert space singled out.

It's worth being explicit about *emph* the ordinary formula "dimension $=\Tr P$" (using the honest
Hilbert-space trace $\Tr$, summing diagonal entries) fails to be the right notion here, since this is exactly
what motivates needing a new, algebra-relative $d(P)$ at all. Take again $P=\ket\psi\rangle\langle\psi|
\otimes\id_2$ on $\HH_1\otimes\HH_2$ with $\HH_2$ infinite-dimensional (the same example as above): the
honest Hilbert-space trace $\Tr P$ is infinite, because $P\HH$ is an infinite-dimensional subspace of $\HH$.
But from the point of view of the algebra $\M\cong B(\HH_1)$, $P$ is the smallest possible nonzero thing —
rank one, within $\HH_1$. The ordinary trace $\Tr$ sees the ambient Hilbert space's raw size and gets it
completely wrong for the purposes of describing what $\M$ can distinguish; the algebra-relative $d(P)$
(normalized so $d(P)=1$ for this minimal $P$) is what correctly reports ``this is the smallest measurable
unit $\M$ has access to,'' regardless of how large a raw subspace it happens to correspond to in $\HH$. This
is the concrete sense in which $\tr$ is a *emph* trace: it strips away the (physically
irrelevant, algebra-dependent) bulk of $\HH$ that $\M$ never actually had access to in the first place, and
reports only the size that $\M$ itself can distinguish.

### The three types

The entire classification now follows from asking one question: what range of values can $d(P)$ actually take,
as $P$ ranges over all the projections in $\M$?


- **Type I: $\M$ has minimal projections.** Normalize $d$ so that a minimal projection gets $d=1$
(you're always free to rescale $d$ by an overall constant, so this is just a choice of units, exactly like
choosing what counts as "one unit of length"). Every projection is then built from superpositions of
minimal ones, and it can be shown that $d(P)$ comes out to be a nonnegative integer for every $P$ — the
ordinary, familiar notion of dimension, just re-derived from the algebra rather than assumed. If the identity
has finite dimension $n=d(\id)$, $\M$ is called type $\mathrm I_n$; if $d(\id)=\infty$ (there's no upper bound
on how many independent minimal projections you can find), it's type $\mathrm I_\infty$. $B(\HH)$ itself, for
an ordinary, separable Hilbert space $\HH$, is trivially type $\mathrm I_n$ (if $\HH$ is $n$-dimensional) or
type $\mathrm I_\infty$ (if $\HH$ is infinite-dimensional but has a countable basis) — this is exactly the
case where $\tr$ reduces to the completely ordinary matrix trace $\Tr_\HH$, with no renormalization needed at
all, because there's no "bulk of $\HH$ the algebra doesn't see" to strip away.

The single most important fact tying this back to ordinary quantum mechanics: it can be shown that $\M$ is a type I factor *emph* there exists a genuine Hilbert space factorization $\HH=\HH_R\otimes\HH_L$ with

$$

\M=B(\HH_R)\otimes\id_L, \qquad \tr=\Tr_{\HH_R}, \qquad \M'=\id_R\otimes B(\HH_L)

$$

(eq.~3.3, though it's placed at the start of the paper's Sec.~III — it belongs conceptually right here, as the closing statement of the type classification). While literature frequently states this as an established theorem without proof, its explicit derivation is profoundly illuminating: it reveals the exact algebraic mechanism by which minimal projections build a spatial tensor product.

\begin{keyresult}[: Derivation of the Type I Factorization Theorem]
**Theorem:** A von Neumann algebra $\M \subseteq B(\HH)$ is a type I factor if and only if there exists a unitary isomorphism $U: \HH \xrightarrow{\sim} \HH_R \otimes \HH_L$ such that:

$$

U \M U^\dagger = B(\HH_R) \otimes \id_L, \qquad U \M' U^\dagger = \id_R \otimes B(\HH_L) .

$$

**Proof ($\implies$):**

1. **Minimal projection and orthogonal resolution:**
By definition of type I, $\M$ contains a nonzero minimal projection $P \in \M$. Minimality means that the compressed algebra contains only scalar multiples of $P$:

$$

P \M P = \mathbb{C} P .

$$

Since $\M$ is a factor, its center is trivial: $\mathcal{Z}(\M) \equiv \M \cap \M' = \mathbb{C}\id$. The central support (the smallest central projection bounding $P$) is therefore $c(P) = \id$. By the comparison theorem for projections in a factor, any two minimal projections are Murray—von Neumann equivalent ($P \sim Q$). By Zorn's lemma, we can choose a maximal family of mutually orthogonal minimal projections $\{P_i\}_{i \in I}$ equivalent to $P$. Maximality and $c(P)=\id$ imply that their sum resolves the identity on $\HH$:

$$

\sum_{i \in I} P_i = \id_\HH, \qquad P_i P_j = \delta_{ij} P_i .

$$

2. **Equivalence via partial isometries:**
Fix a base index $0 \in I$ with $P_0 \equiv P$. Since $P_i \sim P$, there exist partial isometries $V_i \in \M$ such that:

$$

V_i^\dagger V_i = P, \qquad V_i V_i^\dagger = P_i \qquad (\text{with } V_0 \equiv P).

$$

Physically, $V_i$ maps the base subspace $P\HH$ isometrically onto the orthogonal subspace $P_i\HH$.
3. **Construction of the unitary $U$:**
Define two constituent Hilbert spaces:

$$

\HH_R \equiv \ell^2(I) \quad \text{with orthonormal basis } \{\ket{i}\}_{i \in I}, \qquad \HH_L \equiv P\HH .

$$

Define the linear map $U: \HH \to \HH_R \otimes \HH_L$ by its action on any vector $\ket\psi \in \HH$:

$$

U \ket\psi \equiv \sum_{i \in I} \ket{i} \otimes \big(V_i^\dagger \ket\psi\big) .

$$

Notice that $V_i^\dagger \ket\psi = P V_i^\dagger \ket\psi \in P\HH = \HH_L$, so this is well-defined. We check that $U$ is an isometry:
\begin{align*}
\|U\ket\psi\|^2 &= \sum_{i \in I} \|V_i^\dagger \ket\psi\|^2 = \sum_{i \in I} \braket{\psi | V_i V_i^\dagger | \psi} \\
&= \sum_{i \in I} \braket{\psi | P_i | \psi} = \Braket{\psi \Big| \sum_{i \in I} P_i \Big| \psi} = \braket{\psi|\psi} .
\end{align*}
The adjoint map $U^\dagger: \HH_R \otimes \HH_L \to \HH$ acts on elementary basis tensors as:

$$

U^\dagger \big(\ket{i} \otimes \ket{\phi_L}\big) = V_i \ket{\phi_L}, \qquad \ket{\phi_L} \in P\HH .

$$

Computing $U U^\dagger$ on basis vectors:

$$

U U^\dagger \big(\ket{j} \otimes \ket{\phi_L}\big) = U \big(V_j \ket{\phi_L}\big) = \sum_{i \in I} \ket{i} \otimes \big(V_i^\dagger V_j \ket{\phi_L}\big) = \ket{j} \otimes \big(P \ket{\phi_L}\big) = \ket{j} \otimes \ket{\phi_L} ,

$$

since $V_i^\dagger V_j = V_i^\dagger P_i P_j V_j = \delta_{ij} P$. Hence $U$ is a genuine unitary isomorphism.
4. **Action on the algebra $\M$:**
Let $A \in \M$ be an arbitrary element. Compute $U A U^\dagger$ acting on $\ket{j} \otimes \ket{\phi_L}$:

$$

U A U^\dagger \big(\ket{j} \otimes \ket{\phi_L}\big) = U \big(A V_j \ket{\phi_L}\big) = \sum_{i \in I} \ket{i} \otimes \big(V_i^\dagger A V_j \ket{\phi_L}\big) .

$$

Crucially, look at the operator $V_i^\dagger A V_j$:

$$

V_i^\dagger A V_j = (P V_i^\dagger) A (V_j P) = P \big(V_i^\dagger A V_j\big) P \in P \M P .

$$

Because $P$ is minimal, $P \M P = \mathbb{C} P$. Therefore, $V_i^\dagger A V_j$ is *emph*:

$$

V_i^\dagger A V_j = a_{ij} P \quad \text{for some scalar } a_{ij} \in \mathbb{C} .

$$

Acting on $\ket{\phi_L} \in P\HH$, this yields $V_i^\dagger A V_j \ket{\phi_L} = a_{ij} \ket{\phi_L}$. Thus:

$$

U A U^\dagger \big(\ket{j} \otimes \ket{\phi_L}\big) = \sum_{i \in I} a_{ij} \ket{i} \otimes \ket{\phi_L} = \left(\sum_{i,j \in I} a_{ij} \ket{i}\bra{j} \otimes \id_L \right) \big(\ket{j} \otimes \ket{\phi_L}\big) .

$$

Every operator in $\M$ acts trivially on $\HH_L$ and as an ordinary matrix on $\HH_R$. Conversely, given any rank-one operator $\ket{i}\bra{j} \in B(\HH_R)$, its pre-image under $U$ is simply $V_i V_j^\dagger \in \M$. Thus $U \M U^\dagger = B(\HH_R) \otimes \id_L$.
5. **The commutant and trace:**
By von Neumann's double commutant theorem:

$$

U \M' U^\dagger = (U \M U^\dagger)' = \big(B(\HH_R) \otimes \id_L\big)' = \id_R \otimes B(\HH_L) .

$$

The unique normal semifinite trace $\tr$ on $\M$ corresponds under $U$ to the standard trace $\Tr_{\HH_R}$ on $B(\HH_R)$.
6. **Proof ($\impliedby$):**
If $\M \cong B(\HH_R) \otimes \id_L$, take any one-dimensional projection $p = \ket{i}\bra{i}$ on $\HH_R$. Then $P = p \otimes \id_L \in \M$. For any $A = a \otimes \id_L \in \M$:

$$

P A P = (p a p) \otimes \id_L = \braket{i|a|i} (p \otimes \id_L) = \mathbb{C} P .

$$

Hence $P$ is minimal in $\M$, proving $\M$ is type I. $\blacksquare$

\end{keyresult}

So the sentence "the algebra describing this subsystem is type I" is the precise, fully general version of the statement "the ordinary tensor-product picture of Griffiths and Sakurai applies here." Every worked example given so far in this companion — the two-qubit examples above — is type I by direct construction. Types II and III, covered next, are exactly what becomes possible once this is no longer true.
- **Type II: $\M$ has finite projections but no minimal ones.** This is the genuinely new
possibility, and it's worth sitting with how strange it sounds the first time: an algebra where every
projection can be compared in size to every other (the finite/infinite distinction still works, and among
finite projections the ordering $d(P)<d(Q)$ is meaningful), but where there is no smallest nonzero size at
all — you can always find a strictly smaller nonzero projection than any given one. Concretely, once minimal
projections are ruled out, the constraint that $d$ respects strict inequalities ($P<Q\Rightarrow d(P)<d(Q)$),
applied to an infinite descending chain of ever-smaller projections (which must exist, precisely because
there's no smallest one to stop the chain), forces $d(P)$ to take a *emph* range of values,
starting arbitrarily close to zero. This is worth pausing on: it means a von Neumann algebra can assign a
*emph*, not just an integer, as the "dimension" of a subspace — something with no counterpart
at all in ordinary finite-dimensional linear algebra, where dimension is always a whole number you get by
counting basis vectors. Depending on whether $d(\id)$ is finite or not, you get two subtypes: $\mathrm{II}_1$
(identity has finite dimension; normalize so $d(\id)=\tr(\id)=1$, giving $d(P)\in(0,1]$ for every nonzero
projection — a trace normalized exactly like a probability), or $\mathrm{II}_\infty$ ($d(\id)$ unbounded, so
$d(P)\in(0,\infty]$, with no natural normalization available). Section~III of this companion will construct
an explicit type $\mathrm{II}_1$ factor by hand, out of the $N\to\infty$ Bell-pair chain from Sec.~I, so the
strangeness of "real-valued dimension" stops being abstract and becomes something you can watch happen to a
specific, concrete family of projections.
- **Type III: every nonzero projection is infinite.** The most extreme case: not even the
finite/infinite distinction has any nontrivial content, because *emph* is finite except zero itself.
Formally $d(P)=\infty$ for every nonzero $P$ — which means no meaningful dimension function, and hence no
trace at all, exists on $\M$. This sounds like it should be a mathematical dead end (what could you possibly
say about entanglement in an algebra with no density matrix, since density matrices are defined using a
trace?), and reaching that exact impasse, then resolving it with an entirely different tool
(Tomita—Takesaki modular theory), is the entire content of Sec.~IV — the technical heart of the whole paper.
It is also, as flagged repeatedly already, the type that turns out to be the physically generic one: local
regions of a relativistic quantum field theory, and holographic boundary subalgebras in the strict
large-$N$ limit, are both type III (specifically, as you'll see, type $\mathrm{III}_1$) — not some exotic
corner case, but the everyday situation once you leave the world of finitely many qubits.


Types II and III can sound, on first exposure, like unphysical mathematical curiosities. They aren't — the
entangled-spin-chain example from Sec.~I already produces both, explicitly and by direct construction, and
that construction is worked through completely in Sec.~III of this companion.

## Sec.~II.D: "emergent" Hilbert space and von Neumann algebra — the GNS construction

### Why this construction is needed

Here is the gap, restated one more time now that every piece needed to close it is in hand. A von Neumann
algebra's defining completeness condition (weak convergence) is stated directly in terms of matrix elements
$\braket{\xi|A_n|\eta}$ — it presupposes a Hilbert space already exists. A $C^*$-algebra's defining
completeness condition (norm convergence) does not — it only needs an abstract norm satisfying $\|A^\dagger
A\|=\|A\|^2$. So you can specify a $C^*$-algebra $\Alg$ completely abstractly, with no Hilbert space anywhere,
and then ask: given also a state $\omega$ on $\Alg$ (in the sense of Sec.~II.B.3 — a positive, normalized
linear functional, requiring nothing beyond the algebra itself to define), can a Hilbert space be
*emph*, rather than assumed, such that $\omega$ turns out to be represented by an ordinary vector in it?
The Gelfand—Naimark—Segal (GNS) construction answers yes, unconditionally, and does it by an explicit,
completely mechanical recipe.

### The construction, built up in stages

**Stage 1: treat algebra elements themselves as candidate vectors.** This is the conceptual leap, so it's
worth stating plainly before the formulas: an element $C\in\Alg$ is reinterpreted as standing for ``the state
you'd get by applying the operation $C$ to some fixed reference configuration.'' Different elements $C_1,C_2$
should count as representing the *emph* physical state if no measurement, using $\omega$, could ever
tell them apart.

**Stage 2: use $\omega$ to build an inner product on $\Alg$ itself.** Define, for any $A,B\in\Alg$,

$$

\braket{A|B} \equiv \omega(A^\dagger B) .

$$

Check that this deserves to be called an inner product: it's positive, $\braket{A|A}=\omega(A^\dagger A)\ge0$,
directly from $\omega$ being a weight (Sec.~II.B.3); and it has the correct conjugate-symmetry,
$\braket{B|A}=\omega(B^\dagger A)=\omega\big((A^\dagger B)^\dagger\big)=\omega(A^\dagger B)^*=\braket{A|B}^*$,
using $\omega(X^\dagger)=\omega(X)^*$ from the very definition of a linear functional. Both required
properties of an inner product hold, using nothing but the definition of $\omega$ already given.

**Stage 3: handle the possibility of "zero-length" elements.** There might be nonzero $X\in\Alg$ with
$\omega(X^\dagger X)=0$ — algebra elements that $\omega$ is completely blind to. Call the set of all such $X$
the null space $\mathcal J$. It's worth checking (the paper does this explicitly, its eqs.~2.41—2.42, as a
short but genuinely instructive computation) that $\mathcal J$ is well-behaved: if $X\in\mathcal J$ and
$A\in\Alg$ is any element, then $AX\in\mathcal J$ too. The proof is a direct application of the
Cauchy—Schwarz-like inequality from Sec.~II.B.3:

$$

0 \le \omega\big((AX)^\dagger(AX)\big) = \omega(X^\dagger A^\dagger AX)
\le \omega(X^\dagger X)^{1/2}\,\omega\big((A^\dagger AX)^\dagger A^\dagger AX\big)^{1/2} = 0 ,

$$

where the middle step is Cauchy—Schwarz applied to $(X, A^\dagger AX)$, and the right-hand side vanishes
because $\omega(X^\dagger X)=0$, since $X\in\mathcal J$. So
$\omega\big((AX)^\dagger(AX)\big)=0$ too, meaning $AX\in\mathcal J$ as claimed. This one computation is doing
real work: it guarantees that the "null" elements form a well-behaved ideal, so that quotienting them out
(Stage 4) produces something consistent — multiplying by $A$ never accidentally creates a nonzero-length
vector out of a zero-length one.

**Stage 4: quotient and complete.** Define an equivalence relation $A\sim A+X$ for any $X\in\mathcal J$
(algebra elements differing only by something $\omega$ can't see count as the same vector), and let $[A]$
denote the equivalence class of $A$. On the quotient space $\Alg/\mathcal J$, the inner product from Stage 2
is now genuinely positive-definite (no more zero-length nonzero vectors, by construction), and completing this
space — filling in the limits of Cauchy sequences, exactly the way you'd complete the rational numbers to get
the real numbers — produces an honest Hilbert space, called $\HH_\omega$.

**Stage 5: define the representation.** The algebra acts on $\HH_\omega$ by left multiplication:

$$

\pi_\omega(A)\ket{[C]} \equiv \ket{[AC]} .

$$

This is well-defined (doesn't depend on which representative $C$ you picked from its equivalence class,
thanks to Stage 3), and it automatically respects the algebra's multiplication, $\pi_\omega(A)\pi_\omega(B)=
\pi_\omega(AB)$ (immediate from the definition: applying $\pi_\omega(A)$ then $\pi_\omega(B)$ to $[C]$ gives
$[A(BC)]=[(AB)C]$, which is exactly $\pi_\omega(AB)$ applied to $[C]$).

**Stage 6: identify the special vector.** The equivalence class of the identity element, $[\id]$, is
given its own name, $\ket\Omega\equiv\ket{[\id]}$. Two facts follow immediately from the definitions above:

$$

\pi_\omega(A)\ket\Omega = \ket{[A\cdot\id]} = \ket{[A]}, \qquad\qquad
\omega(A) = \braket{\Omega|\pi_\omega(A)|\Omega} .

$$

(The second follows from the first together with the definition of the inner product: $\braket{\Omega|
\pi_\omega(A)|\Omega} = \braket{[\id]|[A]} = \omega(\id^\dagger A)=\omega(A)$.) So $\ket\Omega$, in the
Hilbert space you just built, reproduces the abstract state $\omega$ exactly, via the completely ordinary
formula $\braket{\Omega|A|\Omega}$ you already know from undergraduate quantum mechanics. This is the entire
point of the construction: you handed it an abstract algebra and a number-valued rule $\omega$, and it handed
back a genuine Hilbert space and a genuine vector inside it, with the ordinary quantum-mechanical formula for
expectation values holding by construction, not by assumption.


> [!NOTE] **Physics Connection: Origin of the Vacuum $\ket0$**
> $\ket\Omega$ is not found somewhere outside this construction. It *emph* the identity element of the
> algebra, $\id\in\Alg$, renamed once the inner product has been put on $\Alg$ in Stage~2. A vector and the
> Hilbert space it lives in are made in the same step, from the same two ingredients ($\Alg$ and $\omega$).
> Neither exists before the other.
> 
> The construction also explains, mechanically, why $a$ annihilates $\ket\Omega$ for the oscillator state
> $\omega(X)=\braket{0|X|0}$ — without needing $\ket0$ as an input to say what $\omega$ is. Start from one
> algebraic condition, $\omega(a^\dagger a)=0$, plus positivity, $\omega(A^\dagger A)\ge0$ for every $A\in\Alg$
> (Sec.~II.B.3). Cauchy—Schwarz (eq.~2.19) turns the first into $\omega(a)=\omega(a^\dagger)=0$ directly:
> $|\omega(1^\dagger a)|^2\le\omega(1)\,\omega(a^\dagger a)=0$. Every other value $\omega\big((a^\dagger)^ma^n
> \big)$ then follows by moving each $a$ in a monomial past every $a^\dagger$ using $[a,a^\dagger]=1$, until it
> either meets another $a$ (giving zero) or reaches the identity (giving $1$, by normalization). This is the
> same bookkeeping already used to check $\braket{0|a^n(a^\dagger)^n|0}=n!$ — only now read as *emph*
> $\omega$ from the algebra's multiplication table, not as evaluating a bra-ket that already existed.
> 
> Now apply Stage~3 (Sec.~II.D) to this $\omega$. The null ideal is $\mathcal J=\{X:\omega(X^\dagger X)=0\}$,
> and $a\in\mathcal J$, because $\omega(a^\dagger a)=0$. Stage~4 quotients by exactly this $\mathcal J$: every
> element of $\mathcal J$ becomes the zero vector. So $[a]=0$, and $\pi_\omega(a)\ket\Omega=\ket{[a]}=0$. The
> vacuum being annihilated by $a$ is not a separate fact about the world that $\omega$ happened to match — it
> is what $[a]=0$ means, once $\mathcal J$ is fixed by the one number $\omega(a^\dagger a)$.
> 
> This is the general answer to how the earlier question was phrased: the vector space is not searched for
> among candidates that already satisfy $\omega$; it *emph* $\Alg/\mathcal J$, completed. Its points are
> defined to be exactly as fine as $\omega$ can distinguish, no finer — two algebra elements become the same
> vector exactly when $\omega$ assigns their difference zero length. Quotienting throws out the redundancy;
> completing (filling in limits of Cauchy sequences) is what turns this inner-product space into a genuine
> Hilbert space, matching the definition of Hilbert space from Sec.~I.B.
> 
> In an actual field theory, $\omega$ is fixed the same way, only more concretely: a Euclidean path integral,
> 
$$

> \omega\big(O(x_1)\cdots O(x_n)\big) = \frac1Z\int\mathcal D\phi\;O(x_1)\cdots O(x_n)\,e^{-S[\phi]} ,
> 
$$

> computes every correlator directly, with no Hilbert space, vector, or bra-ket anywhere in the formula
> (Sec.~VI.B's CFT vacuum and the JT-gravity states $\ket\beta$ of Sec.~IX.F are both built this way). Canonical
> quantization, with its $\ket0$ and its Fock space, is the GNS representation built afterward from that already
> complete data. This is also the resolution offered at the end of this companion (Sec.~X.B): different
> asymptotic vacua of string theory are different states $\omega$ on one shared, background-independent algebra
> $\Alg_{\text{IIB}}$, each with its own path-integral (or
> correlator) definition requiring no Hilbert space to state — and each one's "$\ket0$" is simply $[\id]$
> inside *emph* $\omega$'s own GNS space, never a single object shared across backgrounds. That
> is precisely why the resulting Hilbert spaces can come out — and do come out — mutually inequivalent.


The set $\{\pi_\omega(A)\ket\Omega : A\in\Alg\}$ is automatically dense in $\HH_\omega$ (every vector in
$\HH_\omega$ is, by the very construction of $\HH_\omega$ as a completion of $\{[A]\}$, arbitrarily well
approximated by some $\pi_\omega(A)\ket\Omega$). A vector with this property is called **cyclic** — every
state reachable from $\ket\Omega$ using only the algebra, and this is precisely the same structure as the
familiar construction of a harmonic-oscillator Hilbert space by repeatedly acting on the vacuum $\ket0$ with
creation operators; the only difference is that here it is a theorem, derived from the algebra and the state,
rather than a separate postulate about how the Hilbert space happens to be built.


> [!NOTE] **Physics Connection: GNS and Oscillator Fock Space**
> This is worth checking is not just an analogy but literally the same calculation, run through the GNS recipe
> step by step. Let $\Alg$ be the $*$-algebra generated by $1,a,a^\dagger$ with the usual $[a,a^\dagger]=1$
> (polynomials in $a,a^\dagger$ — forget for a moment that you already know this algebra has a Fock-space
> representation; treat it exactly as abstractly as Sec.~II.D asks). Take the state $\omega(X)\equiv\braket{0|X|0}$
> built from the number operator's ground state, $a\ket0=0$ (this is a legitimate abstract state on $\Alg$ in
> the Sec.~II.B.3 sense — positive and normalized — with no Hilbert space assumed yet on the left-hand side;
> you could equally well have specified $\omega$ by giving its value on every monomial $\omega\big((a^\dagger)^m
> a^n\big)$ directly).
> 
> Follow the recipe. Stage 2's inner product on $\Alg$ itself: $\braket{(a^\dagger)^n\,|\,(a^\dagger)^m}\equiv
> \omega\big(a^n(a^\dagger)^m\big)=\braket{0|a^n(a^\dagger)^m|0}$. This is exactly the standard oscillator-algebra
> computation you already know how to do by repeatedly commuting $a$'s past $a^\dagger$'s: it vanishes unless
> $n=m$, and $\braket{0|a^n(a^\dagger)^n|0}=n!$ (check $n=1$: $\braket{0|aa^\dagger|0}=\braket{0|a^\dagger a+1|0}=
> 1=1!$; $n=2$ gives $2!=2$, and so on by induction). So the equivalence classes $\ket{[(a^\dagger)^n]}$ are
> already orthogonal, with norm-squared $n!$ — completing and normalizing gives exactly
> $\ket n\equiv\ket{[(a^\dagger)^n]}/\sqrt{n!}$, the ordinary number-eigenstate basis. The representation
> $\pi_\omega(a^\dagger)\ket{[(a^\dagger)^n]}=\ket{[(a^\dagger)^{n+1}]}$ becomes, after the same normalization,
> exactly $\pi_\omega(a^\dagger)\ket n=\sqrt{n+1}\,\ket{n+1}$ — the ordinary raising-operator matrix element, not
> an approximation to it. The cyclic vector $\ket\Omega=\ket{[1]}$ is exactly the oscillator ground state
> $\ket0$.
> 
> **Nothing here is new physics — this is the identical Fock-space construction from your first course
> on the harmonic oscillator, run backward.** What's genuinely different in outlook, not in content, is which
> direction the logic runs: ordinarily you're handed $\HH=L^2(\mathbb R)$ (or an abstract countable basis)
> first, and $a,a^\dagger$ are defined as operators on it. Here, the algebra generated by the commutation
> relation $[a,a^\dagger]=1$ and the state $\omega$ (equivalently, "the vacuum is annihilated by $a$") were
> the only inputs, and the entire Fock space — every $\ket n$, every matrix element — was manufactured as an
> output. This is exactly the sense in which Sec.~II.B.3 said the Hilbert space is derived, not fundamental: for
> the harmonic oscillator specifically, nothing about the physics changes, because $\omega$ here happens to
> produce a completely ordinary, unique Fock space. The interesting cases — where a different choice of
> reference state genuinely produces an *emph* Hilbert space out of the very same algebra — are
> exactly the $N$-Bell-pair and entangled-spin examples running throughout the rest of this section, and,
> eventually, the different asymptotic vacua of quantum gravity itself in Sec.~X.B.


\begin{workedexamplebox}[: Concrete GNS Construction for Three Physical Systems]
To make the abstract 6-stage recipe completely mechanical, let us explicitly build the GNS Hilbert space, inner product, null ideal, representation, and cyclic vector for three fundamental physical systems:


1. **System 1: Pure State on a Single Qubit ($\Alg = M_2(\mathbb{C**)$)}



8. **System 2: Mixed / Thermal State on $M_2(\mathbb{C**)$ (Emergence of the Thermofield Double)}



14. **System 3: CCR Bosonic Oscillator (Emergence of Fock Space)**




\end{workedexamplebox}

Finally, the von Neumann algebra associated with all of this is obtained by taking the double commutant of the
representation, $\M\equiv\pi_\omega(\Alg)''$ (eq.~2.39) — using exactly the double-commutant machinery from
Sec.~II.B.2 to promote the $C^*$-algebra $\pi_\omega(\Alg)$ (norm-complete, but not yet necessarily
weakly-complete) up to the full von Neumann algebra it generates.

### Two structural facts, and what they mean

The GNS triple $(\HH_\omega,\pi_\omega,\ket\Omega)$ is unique up to unitary equivalence (any two constructions
starting from the same $\omega$ give the "same" Hilbert space, just possibly described in a different
basis) — a fact stated without proof, but a reassuring one, since it means the construction isn't accidentally
sensitive to some arbitrary choice made along the way.

Two further properties of $\omega$ translate directly into properties of the representation you get out:


- $\pi_\omega$ is **irreducible** (meaning $B(\HH_\omega)=\pi_\omega(\Alg)''$ — the representation
already generates *emph* bounded operator on $\HH_\omega$, leaving nothing outside its reach) if and
only if $\omega$ is a **pure** state.
- $\ket\Omega$ is **separating** for $\pi_\omega(\Alg)$ (meaning $A\ket\Omega=0$ forces $A=0$ — no
nonzero operator in the algebra can annihilate the reference vector) if and only if $\omega$ is
**faithful**.


The combination *emph* is worth flagging now, even though its full importance only
becomes visible in Sec.~IV: cyclic says the algebra can reach everywhere starting from $\ket\Omega$;
separating says different elements of the algebra act differently on $\ket\Omega$ (nothing nonzero is wasted).
Together, and by the symmetric statement applied to the commutant $\M'$, these turn out to be exactly the
conditions under which $\ket\Omega$ genuinely encodes entanglement between $\M$ and $\M'$ — the load-bearing
property behind Tomita—Takesaki modular theory, the subject of the next major section of the paper.

### The worked example, done completely with numbers

Here is the example the paper gives (its eqs.~2.51—2.53), worked all the way through with concrete numbers
rather than left symbolic, since this is the single most important computation in the entire section to
actually see happen.

Let $\Alg=M_3(\mathbb C)$, the algebra of all $3\times3$ complex matrices, and take

$$

\rho = \begin{pmatrix}0.6&0&0\\0&0.4&0\\0&0&0\end{pmatrix} , \qquad \omega(A)\equiv\Tr(\rho A).

$$

Check first that $\omega$ really is a state in the Sec.~II.B.3 sense: it's linear (trace and matrix
multiplication are both linear), positive ($\Tr(\rho A^\dagger A)\ge0$ since $\rho$ is a positive-semidefinite
matrix and $A^\dagger A$ is too — a standard fact about traces of products of positive matrices), and
normalized ($\Tr(\rho\cdot\id_3)=\Tr\rho=0.6+0.4+0=1$). Note $\rho$ has rank $2$, not rank $3$: it completely
ignores the third basis direction, so $\omega$ will turn out to be a state that is *emph* faithful
(exactly one property of $\rho$ that will show up directly in the construction below).

Following the GNS recipe exactly: the general theory predicts (and this is confirmed by direct computation,
not just asserted) that $\HH_\omega\cong\mathbb C^3\otimes\mathbb C^2$ — a 6-dimensional space, $3$ (the size
of the original matrix algebra) times $2$ (the rank of $\rho$) — with

$$

\ket\Omega=\sqrt{0.6}\,\ket1_R\ket1_L+\sqrt{0.4}\,\ket2_R\ket2_L ,
\qquad
\pi_\omega(A)=A\otimes\id_2 .

$$

This was checked directly by computer, for several random $3\times3$ matrices $A,B$: both
$\omega(A)=\Tr(\rho A)$ against $\braket{\Omega|\pi_\omega(A)|\Omega}$, and the GNS inner product
$\braket{A|B}=\Tr(\rho A^\dagger B)$ against $\braket{\Omega|\pi_\omega(A)^\dagger\pi_\omega(B)|\Omega}$, and
in every trial the two sides of each comparison agreed to machine precision (roughly one part in $10^{15}$,
the limit of ordinary double-precision computer arithmetic — as close to "exactly equal" as a numerical
check can demonstrate).

This is worth recognizing for what it is: $\ket\Omega$ is exactly the **purification** of $\rho$ you may
already have met in Sakurai's discussion of density matrices — the standard trick of embedding a mixed state
$\rho$ on a small Hilbert space into a pure state on a larger one by introducing an auxiliary system (here,
the $L$ factor) entangled with the original. The GNS construction produces this purification completely
automatically, with no separate ad hoc step of "now introduce an auxiliary system" — the auxiliary system
$\HH_L$ *emph* the completion $\Alg/\mathcal J$ from Stage 4 above, and it appears with exactly the right
dimension (the rank of $\rho$) because that's precisely how many independent equivalence classes $\mathcal
J$ leaves behind.

Two limits of this same example are worth noting explicitly, because they show the two Propositions above in
action on numbers you can check directly:

- Take $\rho=\mathrm{diag}(1,0,0)$ instead — rank $1$, a pure state. Then $\HH_\omega$ collapses to a
single copy of $\mathbb C^3$ (the $L$ factor becomes 1-dimensional and drops out), and $\pi_\omega$ is
irreducible — consistent with the Proposition above, since $\omega$ is now pure.
- Take $\rho=\tfrac13\id_3$ instead — full rank ($3$), maximally mixed. Then $\HH_\omega=\mathbb
C^3\otimes\mathbb C^3$, and $\ket\Omega=\tfrac1{\sqrt3}\sum_{a=1}^3\ket a_R\ket a_L$ is both cyclic
*emph* separating — consistent with the second Proposition, since this $\omega$ is faithful (it's the
maximally mixed state, which by definition assigns nonzero weight to literally everything). This maximally
mixed, maximally entangled reference vector is the abstract, $3$-dimensional-matrix-algebra analogue of the
Bell pair at $\theta=\pi/4$ from Sec.~I — the same structure, one level more general.


## Sec.~II.E: emergent von Neumann algebras of the entangled spin example

This closing subsection of Sec.~II does exactly one thing: it takes the GNS machinery just built and applies
it, explicitly, to the $N\to\infty$ Bell-pair-chain example from Sec.~I — turning the informal discussion
there ("the finite-energy excitations form some Hilbert space $\HH_{\Phi_\theta}$") into an actual
construction, with an actual algebra and an actual state.

Define the algebra of **finite-energy operations**, $\Alg$: operators of the form

$$

O = \alpha_1\otimes\alpha_2\otimes\cdots\otimes\alpha_n\otimes\cdots ,
\qquad \text{all but finitely many of the } \alpha_i \text{ equal } \id_2\otimes\id_2

$$

(eq.~2.54) — that is, $O$ acts on only finitely many of the (infinitely many) spin pairs, doing nothing
(the identity) to every pair beyond some finite point. This restriction is not arbitrary; it is exactly the
statement, translated into algebra, that $O$ corresponds to a process reachable at finite energy (recall from
Sec.~I that flipping infinitely many spins costs infinite energy — an operator that acts nontrivially on
infinitely many pairs at once is precisely the kind of thing a finite-energy process could never do). In the
$N\to\infty$ limit, $O$ inherits a well-defined norm from the finite-$N$ operators it's built out of, and
completing $\Alg$ in that norm makes it a genuine $C^*$-algebra — abstractly defined, with no particular
Hilbert space singled out yet.

The reference state $\ket{\Phi_\theta}$ (the infinite chain of Bell-like pairs from Sec.~I) defines a state
$\omega_\theta$ on this algebra in the obvious way,

$$

\omega_\theta(O) = \braket{\Phi_\theta|O|\Phi_\theta} ,

$$

(eq.~2.55) which makes sense precisely because $O$ only touches finitely many pairs, so the expectation value
is computable using only finitely much of the state — no infinite sum or ill-defined limit is hiding inside
this definition.

Now apply the GNS construction of the previous subsection, exactly as given, to $(\Alg,\omega_\theta)$. It
produces a Hilbert space $\HH_{\Phi_\theta}$ — and this *emph* the space of finite-energy excitations
informally described back in Sec.~I, now obtained as a genuine mathematical construction rather than a
descriptive placeholder. Heuristically (and this is exactly Stage 1 of the GNS recipe, applied to this
specific case): $\HH_{\Phi_\theta}$ is what you get by completing the set of states reachable from
$\ket{\Phi_\theta}$ by flipping a finite number of spins — precisely the informal description from Sec.~I,
now made rigorous. In this particular representation, the von Neumann algebra you get out
(eq.~2.39, $\pi_\omega(\Alg)''$) turns out to be all of $B(\HH_{\Phi_\theta})$ — every bounded operator on
this emergent Hilbert space.

Suppose now, exactly as in the running example throughout this section, that you only have access to the
$R$-half of the spin system. $\M_R$, the subalgebra of $B(\HH_{\Phi_\theta})$ consisting of operators acting
only on the $R$-spins, completed under weak convergence *emph*$}, is a
von Neumann algebra — this is the object whose *emph* (I, II, or III, depending on $\theta$) is the
entire subject of Secs.~III and IV. $\M_L$ is defined the same way for the $L$-spins, and because operations
on the $L$-spins commute with operations on the $R$-spins by construction (they act on physically distinct
degrees of freedom), you get $\M_L=\M_R'$ (eq.~2.56) — the $L$-algebra and the $R$-algebra's commutant coincide,
exactly the "complement of a subsystem" picture from Sec.~II.B.1, now realized concretely rather than just
asserted in the abstract.

One further, slightly subtle point, worth stating because it removes an apparent asymmetry: this particular
example has a complete symmetry between $R$ and $L$ (nothing distinguishes them — the construction so far
could equally well have been built starting from $\M_L$ instead of $\M_R$), and it turns out the same Hilbert
space $\HH_{\Phi_\theta}$ can be reconstructed using *emph* the $R$-algebra, with no reference to $L$ at
all. Concretely, redo the GNS construction using $\Alg_R$ (finite-energy operations on the $R$-spins only,
eq.~2.57) and the state $\omega_\theta(A)=\braket{\Phi_\theta|A|\Phi_\theta}$ restricted to $A\in\Alg_R$
(eq.~2.58). This $\omega_\theta$ is a *emph* state of $\Alg_R$ — even though, restricted to the
full $\Alg$ from before, $\omega_\theta$ was not faithful there (a subtlety worth noting rather than glossing
over: faithfulness is a property of a state *emph* a specific algebra, not an absolute property of
the state alone) — and the GNS Hilbert space this produces coincides with the very same $\HH_{\Phi_\theta}$ as
before. The intuition for why (given in the paper's footnote 17, worth restating in full): consider a single
spin pair. Acting on $\ket{\phi_\theta}$ using only operators of the right spin can already generate every
state reachable by acting with operators of the left spin instead — because the pair is only two-dimensional
on each side, and (for $\theta\ne0$) both the right-spin operators and the left-spin operators, applied to
$\ket{\phi_\theta}$, are each individually rich enough to reach the same two-dimensional space of resulting
states. This mirrors, on a much larger scale, exactly the point already made in Sec.~II.B.5's discussion of
minimal projections and irreps: $\M_R$, as an abstract algebra, already contains a full copy of everything
needed to reconstruct the Hilbert space — $\HH_L$ was only ever tracking multiplicity, and in this
perfectly-symmetric example, $R$ alone carries exactly as much information as $R$ and $L$ together did.

With $\HH_{\Phi_\theta}$, $\M_R$, and $\M_L=\M_R'$ now built explicitly rather than just described, the stage
is set for the question that occupies the rest of the paper: for different values of $\theta$, what
*emph* — in the precise Sec.~II.C sense — is $\M_R$? Section~III of this companion answers this directly,
by explicit computation, for $\theta=\pi/4$ (finding type $\mathrm{II}_1$) and sets up the general
$\theta\ne\pi/4$ case (type III, completed in Sec.~IV).



---

# Sec.~III: Von Neumann algebras and entanglement: type I and II

Sec.~II built the whole apparatus — algebras, states, projections, the type classification, and the GNS
construction — but always working with a fixed algebra $\M$ sitting inside some ambient $B(\HH)$, with no
particular state singled out for special attention. This section asks the question the whole framework was
built to answer: given a specific physical state $\ket\Psi$, what does the *emph* of $\M$ tell you about
how $\Psi$ entangles the subsystem $\M$ describes with everything outside it? Type I and type II are handled
here, because both still have a trace, so a density operator and an entropy can still be defined by a direct
generalization of the formulas you already know. Type III — where no trace exists at all — needs an entirely
different tool, and is deferred to Sec.~IV.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.88\textwidth]{figs/fig_type_chart.pdf}
\caption{The taxonomy of von Neumann algebra factors: classified by Murray and von Neumann according to the range of their projection dimension function $d(\mathcal{P}(\M))$ and the existence of a tracial state $\tau$. Type I possesses minimal projections (rank-one rays); Type II has no minimal projections but supports a trace (finite for $\mathrm{II}_1$, semifinite for $\mathrm{II}_\infty$); Type III has neither minimal projections nor a trace, exhibiting purely infinite projection dimensions.}
\label{fig:type_chart}
\end{figure}

\begin{table}[htbp]
\centering
\footnotesize
\begin{tabularx}{\textwidth}{@{}l p{2.2cm} l p{2.6cm} X l@{}}
\toprule
**Factor** & **Proj. Dim. $d(\mathcal{P**)$} & **Trace $\tau$** & **Density Matrix $\rho_\M$** & **Physical System** & **Entropy Status** \\
\midrule
$\mathrm{I}_n$ & $\{0, 1, \dots, n\}$ & Yes (finite) & $\rho_R = \Tr_L\ket\Psi\bra\Psi$ & $n$-level system / qubits & $S \ge 0$ \\
$\mathrm{I}_\infty$ & $\{0, 1, 2, \dots, \infty\}$ & Yes (semifinite) & Fock space $\rho$ & Harmonic oscillator & Well-defined \\
$\mathrm{II}_1$ & $[0, 1]$ (continuous) & $\tau(\id)=1$ & $\rho_\M \in \M$ & $\infty$ Bell pairs ($\theta=\frac{\pi}{4}$) & $S \le 0$ (vs max-mixed) \\
$\mathrm{II}_\infty$ & $[0, \infty]$ (continuous) & Semifinite & $\rho_\M = e^{-K_\Psi - p}$ & Crossed product $\M \rtimes \mathbb{R}$ & $S_{\rm gen} = \frac{\langle\hat A\rangle}{4G_N} + S_{\rm bulk}$ \\
$\mathrm{III}_0$ & $\{0, \infty\}$ & None & No density matrix & Non-ergodic flows & Ill-defined \\
$\mathrm{III}_\lambda$ & $\{0, \infty\}$ & None & No density matrix & Spin chain ($\tan^2\theta = \lambda$) & Relative $S(\rho\|\sigma)$ only \\
$\mathrm{III}_1$ & $\{0, \infty\}$ & None & No density matrix & QFT subregion / Rindler & Relative only / crossed \\
\bottomrule
\end{tabularx}
\caption{Complete classification of von Neumann algebra factors and their physical, operational, and thermodynamic properties.}
\label{tab:factor_taxonomy}
\end{table}

## Sec.~III.A: density operators for type I and II algebras

Here is the key new formula, and it deserves to be read as slowly as the definition of $\M$ itself was.
Suppose the full system is in a state $\ket\Psi\in\HH$, and $\M$ is a von Neumann algebra with a trace $\tr$
(so, by Sec.~II.C, type I or type II). Define $\rho_\M\in\M$ to be the operator satisfying

$$

\tr(A\rho_\M) = \braket{\Psi|A|\Psi} \qquad \text{for every } A\in\M

$$

(eq.~3.1). Positivity of $\tr$ guarantees this equation has a unique solution $\rho_\M$, and that the
resulting $\rho_\M$ is itself positive and correctly normalized — i.e., it genuinely deserves to be called a
density operator (footnote~18 of the paper flags a subtlety worth restating: it matters that $\rho_\M$ is
required to belong to $\M$ itself, not merely to $B(\HH)$ — the equation is being solved *emph* the
algebra). With $\rho_\M$ in hand, the entanglement entropy is defined exactly as you'd expect,

$$

S_\M \equiv -\tr(\rho_\M\log\rho_\M)

$$

(eq.~3.2) — formally identical to the ordinary formula $S_R=-\Tr(\rho_R\log\rho_R)$, just with $\tr$ (the
algebra's own, possibly renormalized trace from Sec.~II.C) standing in for the ordinary Hilbert-space trace,
and $\rho_\M$ standing in for the ordinary reduced density matrix.

Stop and compare this to the formula you already know, $\rho_R=\Tr_L\ket\Psi\!\bra\Psi$ (a partial trace).
That formula needs the complement $L$ to be given explicitly, as a separate tensor factor you can sum over —
you need to know about the part of the world you *emph* access in order to build an object describing
the part you *emph*. Equation~3.1 needs nothing of the sort: it's a self-contained equation stated purely
in terms of $\M$'s own trace and expectation values of $\M$'s own operators. This is worth stating as
explicitly as the paper does in its own remark: since you only have access to $\M$, in what sense does
$\rho_\M$, defined this way, capture anything about entanglement with the outside world at all? The paper's
own promise (repeated here, since it's the right way to hold the question while reading the rest of the
section): the answer depends entirely on which *emph* $\M$ turns out to be, and working through that
answer, type by type, is the entire content of the rest of Sec.~III and all of Sec.~IV.

## Sec.~III.B: type I algebras

### The type I factor case: nothing is lost

When $\M$ is a type I *emph*, Sec.~II.C already established $\HH=\HH_R\otimes\HH_L$,
$\M=B(\HH_R)\otimes\id_L$, $\tr=\Tr_{\HH_R}$, $\M'=\id_R\otimes B(\HH_L)$ (eq.~3.3). Plug this into the
right-hand side of eq.~3.1: using the ordinary partial-trace formula, $\braket{\Psi|A|\Psi}=\Tr_{\HH_R}(\rho_R
A)$ for $A\in\M$ (eq.~3.4), where $\rho_R=\Tr_{\HH_L}\ket\Psi\bra\Psi$ is the ordinary reduced density matrix
you already know. Comparing this to the defining equation of $\rho_\M$ (eq.~3.1), and using $\tr=\Tr_{\HH_R}$,
you read off immediately: $\rho_\M=\rho_R$. The new, algebra-intrinsic definition and the old,
partial-trace definition give *emph* the same operator, whenever a type I factorization is available.
Nothing is lost by switching definitions — you can check this is consistent rather than just asserted, since
both sides of eq.~3.1 are now completely explicit ordinary-linear-algebra objects.

Two remarks the paper makes here are worth keeping, because they're exactly the seeds of everything that
happens once type I stops being available:

1. The two approaches are conceptually very different, even when they agree numerically. Equation~2.2
needs the full global state $\ket\Psi$, including the part living in $\HH_L$ that you have no access to, in
order to build $\rho_R$. Equation~3.1 needs only expectation values of operators in $\M$ — data an
$R$-observer could, in principle, actually collect. The fact that these two completely different-looking
recipes produce the same answer, in the type I case, is itself the thing worth remembering when type I stops
holding: the entanglement information was, all along, fully recoverable from $\M$'s own internal data; the
tensor-product recipe was just a more roundabout way of getting the same answer, one that happens to break
once no factorization exists.
2. Because $\tr$ (equal here to the ordinary $\Tr_{\HH_R}$) genuinely counts basis states of an honest
Hilbert space $\HH_R$, $S_\M=S_R$ inherits a completely ordinary statistical interpretation — the usual
"number of effectively occupied states" reading of entropy. This interpretation, too, is about to become
much more delicate once you leave type I.


### General type I: a nontrivial center, and where lattice gauge theory fits

If $\M$ is type I but *emph* a factor (it has a nontrivial center — recall the block-diagonal
$P_1,P_2$ worked example from Sec.~II.B.2 of this companion), the Hilbert space decomposes into a direct sum
of sectors, one for each value $\alpha$ of the central (classical) label:

$$

\HH=\bigoplus_\alpha\HH_\alpha, \quad \HH_\alpha=\HH_{R\alpha}\otimes\HH_{L\alpha}, \qquad
\M=\bigoplus_\alpha\big(B(\HH_{R\alpha})\otimes\id_{L\alpha}\big)

$$

(eqs.~3.5—3.6) — within each sector, the ordinary tensor-product story holds exactly as in the factor case
above; the different sectors just sit side by side, never mixing (any operator in $\M$ acts block-diagonally,
never sending a state in sector $\alpha$ to a state in a different sector $\alpha'$). The trace is built
sector by sector, $\tr A=\sum_\alpha\Tr_{\HH_{R\alpha}}A_\alpha$ (eq.~3.7), and a general state $\rho$ on
$\HH$ decomposes as $\rho=\bigoplus_\alpha p_\alpha\rho_\alpha$ — a classical probability $p_\alpha$ of being
in sector $\alpha$, times an ordinary (normalized) density matrix $\rho_\alpha$ within that sector (eq.~3.8).
Working through eq.~3.1 sector by sector gives $\rho_\M=\bigoplus_\alpha p_\alpha(\rho_{R\alpha}\otimes
\id_{L\alpha})$ (eq.~3.9, with $\rho_{R\alpha}=\Tr_{\HH_{L\alpha}}\rho_\alpha$ the ordinary reduced density
matrix within sector $\alpha$), and plugging this into eq.~3.2 gives an entropy that cleanly splits into two
recognizable pieces,

$$

S_\M = -\sum_\alpha p_\alpha\log p_\alpha \;+\; \sum_\alpha p_\alpha S_\alpha ,
\qquad S_\alpha=-\tr_\alpha(\rho_{R\alpha}\log\rho_{R\alpha})

$$

(eq.~3.10): an ordinary classical (Shannon) entropy of *emph*, plus the
probability-weighted average of the ordinary quantum entanglement entropy *emph* each sector. Nothing
here is conceptually new — it's exactly what you'd compute by hand if someone told you ``the system is either
in configuration A with probability $p_A$ (itself entangled some amount $S_A$) or configuration B with
probability $p_B$ (entangled some amount $S_B$), and you don't know which'' — but it's worth seeing it fall
directly out of the single unified formula, eq.~3.1, rather than needing to be reasoned out from scratch each
time.


> [!EXAMPLE] **Worked Example:**
> Consider a spatial lattice with two sites ($x_1, x_2$) connected by a gauge link carrying electric flux $E \in \{0, 1\}$. The physical Hilbert space decomposes into superselection sectors labeled by the central electric flux $q \in \{0, 1\}$ passing across the bipartition cut between the sites:
> 
$$

> \HH_{\text{phys}} = \HH_{q=0} \oplus \HH_{q=1} = (\HH_{R,0}\otimes\HH_{L,0}) \oplus (\HH_{R,1}\otimes\HH_{L,1}) .
> 
$$

> Suppose a physical state is prepared as a mixture of these sectors:
> 
$$

> \rho = p_0\,\rho_0 \oplus p_1\,\rho_1 , \qquad p_0 = 0.8, \quad p_1 = 0.2 ,
> 
$$

> where in sector $q=0$ the two sites are maximally entangled Bell pairs with reduced density matrix $\rho_{R,0} = \operatorname{diag}(1/2, 1/2)$ ($S_0 = \log 2 \approx 0.6931$), while in sector $q=1$ the sites are unentangled product states ($S_1 = 0$).
> Evaluating the unified algebraic entropy formula (eq.~3.10):
> 
1. **Classical Shannon entropy of the gauge flux:**
> 
$$

> H(p) = -p_0\log p_0 - p_1\log p_1 = -0.8\log(0.8) - 0.2\log(0.2) \approx 0.1785 + 0.3219 = 0.5004\text{ nats} .
> 
$$

>
2. **Average quantum entanglement within sectors:**
> 
$$

> \sum_\alpha p_\alpha S_\alpha = 0.8 \times (\log 2) + 0.2 \times 0 = 0.8 \times 0.693147 = 0.5545\text{ nats} .
> 
$$

>
3. **Total algebraic entropy:**
> 
$$

> S_\M = H(p) + \sum_\alpha p_\alpha S_\alpha \approx 0.5004 + 0.5545 = 1.0549\text{ nats} .
> 
$$

>

> This demonstrates how the algebraic framework captures both classical gauge flux fluctuations and genuine quantum entanglement in a single formula without requiring a spatial tensor factorization.


This is exactly the situation for the lattice gauge theory example (Ex.~1 from Sec.~I): the algebra of
gauge-invariant local operators is type I (it still has minimal projections, still counts states in the
ordinary way sector by sector) but not a factor (gauge invariance imposes a classical superselection label —
which gauge sector, e.g.\ which total electric flux configuration, you're in). The single formula~3.1 handles
this uniformly, with the factorized case (type I factor) simply being the special case of a trivial center
(only one sector, $p_\alpha=1$ for a single $\alpha$). This is the sense in which the algebraic language,
even at this early, still-mostly-familiar stage, is already doing real unifying work.

## Sec.~III.C: type II algebras

This is where something genuinely new happens, and the paper's chosen way to show it is to build a type
$\mathrm{II}_1$ factor completely explicitly, by hand, out of the $N\to\infty$ Bell-pair chain from
Sec.~II.E of this companion. It's worth doing every step of this construction, because it is the first
place in the paper where you can watch an entirely new kind of mathematical object get built in front of you,
out of nothing more exotic than an infinite chain of ordinary qubits.

### Sec.~III.C.1: building a trace at $\theta=\pi/4$

Recall the setup from Sec.~II.E: $\M\equiv\M_R$ is the von Neumann algebra of operators acting on the
right-hand spins of the chain, built via GNS from the algebra of finite-energy operations $\Alg_R$ and the
state $\omega_\theta(A)=\braket{\Phi_\theta|A|\Phi_\theta}$. Fix $\theta=\pi/4$ (every pair maximally
entangled) and *emph*

$$

\tr A \equiv \braket{\Phi_{\pi/4}|A|\Phi_{\pi/4}} , \qquad A\in\M .

$$

(eq.~3.11.) This looks, on the surface, exactly like an ordinary expectation value — nothing distinguishes it
notationally from $\omega_{\pi/4}(A)$ already defined in Sec.~II.E. The claim being made is that, specifically
at $\theta=\pi/4$, this particular expectation value happens to *emph* satisfy the cyclic property
$\tr(AB)=\tr(BA)$ that defines a trace (Sec.~II.B.3) — and it's worth verifying this rather than just
believing it, since it is the single fact the entire rest of this subsection rests on.

**Step 1: a single pair.** Take one spin pair at $\theta=\pi/4$, in the state $\ket{\phi_{\pi/4}}=
\tfrac1{\sqrt2}(\ket{00}+\ket{11})$, and let $a = \begin{pmatrix} a_{00} & a_{01} \\ a_{10} & a_{11} \end{pmatrix}$ be any operator acting on the right spin alone ($a\otimes\id_L$). Let us compute the expectation value by expanding the state:
\begin{align*}
\braket{\phi_{\pi/4}|a\otimes\id_L|\phi_{\pi/4}} &= \frac{1}{2}\left(\bra{00}+\bra{11}\right)(a\otimes\id_L)\left(\ket{00}+\ket{11}\right) \\
&= \frac{1}{2}\left( \braket{00|a\otimes\id|00} + \braket{00|a\otimes\id|11} + \braket{11|a\otimes\id|00} + \braket{11|a\otimes\id|11} \right) \\
&= \frac{1}{2}\left( a_{00}\braket{0|0}_L + a_{01}\braket{0|1}_L + a_{10}\braket{1|0}_L + a_{11}\braket{1|1}_L \right) \\
&= \frac{1}{2}\left( a_{00} + a_{11} \right) = \frac{1}{2}\Tr_2(a) .
\end{align*}
(eq.~3.12, with $\Tr_2$ the ordinary $2\times2$ matrix trace) — the expectation value in a single maximally
entangled pair, of any operator touching only one side of that pair, is exactly one-half the ordinary trace
of that operator. This specific numerical coefficient, $\tfrac12$, is not an accident of notation; it's
exactly $1/\dim(\HH_2)$ for a single qubit, and it will reappear, tracked explicitly, in eq.~3.18 below.

**Step 2: many pairs.** A general element of $\M_R$ (recall Sec.~II.E, eq.~2.57) is $A=a_1\otimes
a_2\otimes\cdots$, with only finitely many of the $a_i$ different from the identity — say $a_{i_1},\dots,
a_{i_k}$ are the nontrivial ones. Because $\ket{\Phi_{\pi/4}}$ is a product of independent pairs, and each
pair contributes independently via Step~1,

$$

\braket{\Phi_{\pi/4}|A|\Phi_{\pi/4}} = \frac{1}{2^k}\,\Tr_2(a_{i_1})\cdots\Tr_2(a_{i_k})

$$

(eq.~3.13) — the expectation value in the full infinite chain reduces to a product of ordinary $2\times2$
matrix traces, one factor of $\tfrac12$ for each of the $k$ pairs actually touched.

**Step 3: cyclicity.** Here is the punchline, and it's genuinely just a one-line consequence of Step~2
once you see it: since $\braket{\Phi_{\pi/4}|A|\Phi_{\pi/4}}$ reduces *emph* to a product of ordinary
$2\times2$ matrix traces, and the ordinary matrix trace is itself cyclic ($\Tr_2(a_ib_i)=\Tr_2(b_ia_i)$ for
each individual pair, a completely standard fact about matrix traces), the whole product inherits cyclicity:

$$

\braket{\Phi_{\pi/4}|AB|\Phi_{\pi/4}} = \braket{\Phi_{\pi/4}|BA|\Phi_{\pi/4}}

$$

(eq.~3.14). This establishes eq.~3.11 as a genuine trace on $\M$. And this is exactly where $\theta=\pi/4$
earns its special status: Step~1's formula, $\braket{\phi_\theta|a|\phi_\theta}=\tfrac12\Tr_2(a)$, is only
exactly true at $\theta=\pi/4$ — for any other angle, the expectation value picks up $\theta$-dependent
weighting that breaks the exact matching to an ordinary matrix trace, and cyclicity fails. While this is often stated without derivation, we can prove the impossibility of any trace directly and rigorously via macroscopic operator condensation:

\begin{keyresult}[: The No-Trace Theorem for the Asymmetric Spin Chain]
**Theorem:** Let $\Alg_R = \bigotimes_{k=1}^\infty M_2(\mathbb{C})$ be the quasi-local spin chain algebra, and let $\ket{\Phi_\theta} = \bigotimes_{k=1}^\infty (\cos\theta\ket{00} + \sin\theta\ket{11})_k$ with $\theta \in (0, \pi/4)$. Let $\M_R \equiv \pi_\theta(\Alg_R)'' \subseteq B(\HH_\theta)$ be the GNS von Neumann factor.
Then for any $\theta \ne \pi/4$, **there exists no nonzero normal tracial state on $\M_R$**. Consequently, $\M_R$ is strictly type III.

**Proof:**

1. **Tracial constraint on Pauli commutators:**
Suppose for contradiction that there exists a normal tracial state $\tau: \M_R \to \mathbb{C}$ with $\tau(\id) = 1$. By definition of a trace, $\tau(AB) = \tau(BA)$ for all $A, B \in \M_R$, which implies that $\tau([A, B]) = 0$ for every commutator.
On any individual spin site $k$, consider the Pauli operators $\sigma_x^{(k)}, \sigma_y^{(k)}, \sigma_z^{(k)} \in \Alg_R \subset \M_R$. From the $\mathfrak{su}(2)$ algebra, $[\sigma_x, \sigma_y] = 2i\sigma_z$, which gives:

$$

\sigma_z^{(k)} = \frac{1}{2i}\big[\sigma_x^{(k)}, \, \sigma_y^{(k)}\big] .

$$

Applying the tracial state $\tau$ directly yields:

$$

\tau\big(\sigma_z^{(k)}\big) = \frac{1}{2i}\tau\big([\sigma_x^{(k)}, \, \sigma_y^{(k)}]\big) = 0 \qquad \text{for all } k \ge 1 .

$$

2. **Vanishing trace of average magnetization:**
Define the macroscopic block-spin average magnetization over the first $N$ sites:

$$

M_N \equiv \frac{1}{N}\sum_{k=1}^N \sigma_z^{(k)} \in \M_R .

$$

By linearity of $\tau$ and the single-site identity above:

$$

\tau(M_N) = \frac{1}{N}\sum_{k=1}^N \tau\big(\sigma_z^{(k)}\big) = 0 \qquad \text{for all } N \ge 1 .

$$

3. **Macroscopic condensation in the GNS state:**
Now examine $M_N$ in the physical GNS reference state $\ket{\Omega_\theta} \equiv \ket{\Phi_\theta}$. On each entangled pair:

$$

\braket{\phi_\theta | \sigma_z | \phi_\theta} = \cos^2\theta \braket{0|\sigma_z|0} + \sin^2\theta \braket{1|\sigma_z|1} = \cos^2\theta - \sin^2\theta = \cos(2\theta) .

$$

The expectation value of the average magnetization is therefore:

$$

\braket{\Omega_\theta | M_N | \Omega_\theta} = \frac{1}{N}\sum_{k=1}^N \cos(2\theta) = \cos(2\theta) .

$$

Because the state $\ket{\Phi_\theta}$ is an exact product state across different pairs, spin fluctuations at distinct sites $k \ne j$ are completely uncorrelated:

$$

\Braket{\Omega_\theta \Big| \big(\sigma_z^{(k)} - \cos(2\theta)\big)\big(\sigma_z^{(j)} - \cos(2\theta)\big) \Big| \Omega_\theta} = \delta_{kj}\big(1 - \cos^2(2\theta)\big) = \delta_{kj}\sin^2(2\theta) .

$$

The variance of $M_N$ in the GNS representation is:

$$

\big\| \big(M_N - \cos(2\theta)\id\big)\ket{\Omega_\theta} \big\|^2 = \frac{1}{N^2}\sum_{k=1}^N \sin^2(2\theta) = \frac{\sin^2(2\theta)}{N} \xrightarrow{N\to\infty} 0 .

$$

4. **Strong operator convergence:**
Since $\ket{\Omega_\theta}$ is cyclic and separating for $\M_R$, and $\|M_N\| \le 1$ is uniformly bounded, the vanishing of the variance implies that $M_N$ converges in the strong operator topology on $\HH_\theta$ to a scalar multiple of the identity:

$$

\mathrm{s\text{-}}\lim_{N\to\infty} M_N = \cos(2\theta)\,\id .

$$

5. **The contradiction:**
By definition of normality, the state $\tau$ is continuous in the weak (and ultraweak) operator topology. Therefore:

$$

\lim_{N\to\infty} \tau(M_N) = \tau\big(\mathrm{s\text{-}}\lim_{N\to\infty} M_N\big) = \tau\big(\cos(2\theta)\id\big) = \cos(2\theta)\,\tau(\id) = \cos(2\theta) .

$$

Comparing this with the exact algebraic result from Step~2:

$$

0 = \lim_{N\to\infty} \tau(M_N) = \cos(2\theta) .

$$

For any non-maximal entangling angle $\theta \in (0, \pi/4)$, we have $\cos(2\theta) > 0$. The equality $0 = \cos(2\theta) > 0$ is a strict contradiction!

Hence no normal tracial state $\tau$ can exist on $\M_R$ when $\theta \ne \pi/4$. With both type I and type II ruled out by the total absence of a trace, $\M_R$ is unavoidably **type III**. $\blacksquare$

\end{keyresult}

### Sec.~III.C.2: no minimal projection, and dimensions that are genuine real numbers

With a bona fide trace in hand, $\M_R$ (at $\theta=\pi/4$) is at least type I or type II — the question is
which. Consider the family of projections built by fixing some finite subset of the spins to be spin-up,
and leaving the rest untouched:

$$

\id \equiv \id_2\otimes\id_2\otimes\cdots, \qquad
P_1 = \id_2\otimes P_\uparrow\otimes\id_2\otimes\cdots, \qquad
P_2 = P_\uparrow\otimes\id_2\otimes P_\uparrow\otimes\id_2\otimes\cdots,

$$

with $P_\uparrow=\begin{psmallmatrix}1&0\\0&0\end{psmallmatrix}$ the projector onto spin-up on a single qubit
(eq.~3.16) — and, in general, you can build a projection this way by choosing *emph* finite subset of the
spins and replacing their identity factor with $P_\uparrow$.

Here is the argument that no minimal projection exists, and it's worth seeing why it's airtight rather than
just plausible: take *emph* nonzero projection $P$ of this form, built by fixing some finite set of spins.
No matter how many spins it already fixes, you can always find one more spin, currently left as $\id_2$
inside $P$, and replace that one factor with $P_\uparrow$ too — producing a new projection $\widetilde P$ that
is strictly smaller than $P$ (fixing one additional spin can only shrink the corresponding subspace, never
grow it) and still manifestly nonzero. Since this can be done starting from *emph* such $P$, with no
exception, there is no smallest one — no projection built this way can be minimal. So $\M_R$ has finite
projections (as you're about to see) but no minimal ones: by the Sec.~II.C classification, this rules out
type I entirely.

Now compute actual dimensions, using the trace normalized so $d(\id)=\tr(\id)=1$ (eq.~3.17 — automatic, since
$\tr(\id)=\braket{\Phi_{\pi/4}|\id|\Phi_{\pi/4}}=1$ by normalization of the state). Using Step~2's formula
above directly: $P_1$ fixes exactly one spin to $P_\uparrow$ (with $\Tr_2(P_\uparrow)=1$), so
$d(P_1)=\tr(P_1)=\tfrac12\Tr_2(P_\uparrow)=\tfrac12$; $P_2$ fixes two spins, so
$d(P_2)=\tr(P_2)=\tfrac1{2^2}\Tr_2(P_\uparrow)\Tr_2(P_\uparrow)=\tfrac14$ (eq.~3.18) — and in general, a
projection fixing $k$ spins has dimension exactly $2^{-k}$. Check this is completely consistent, not just
plausible: for any finite $k$, $2^{-k}>0$ (never actually zero, however large $k$ is), so every one of these
projections is genuinely nonzero and finite — consistent with there being no minimal one (you can always
halve the dimension again by fixing one more spin, but you never reach zero at any finite step).

This is the moment where something with literally no counterpart in ordinary finite-dimensional linear
algebra appears: by taking superpositions of orthogonal projections built this way (and limits of such
superpositions — infinite sums, made rigorous by the completeness built into the von Neumann algebra
structure), you can construct a projection $P$ with $d(P)$ equal to *emph* real number in $(0,1]$, not
just the numbers $2^{-k}$ reachable by the simple fixed-spin construction above. Compare this once more to
ordinary quantum mechanics: there, "the dimension of a subspace" is always a whole number, obtained by
literally counting basis vectors — there is no such thing as a subspace of dimension $0.31830989\ldots$ (an
arbitrary real number). Here, $d(P)$ genuinely can be any such number, and this continuous range of possible
dimensions, together with the complete absence of a minimal projection, is precisely the defining signature
of type $\mathrm{II}_1$ (Sec.~II.C): finite projections exist and can be directly compared in size, but there
is no smallest possible "one unit" of measurement, only an ever-refinable continuum. So: at $\theta=\pi/4$,
$\M=\M_R$ is a type $\mathrm{II}_1$ factor — the first genuinely new object encountered so far in this
companion, and it was built using nothing beyond ordinary spin-$\tfrac12$ qubits and an infinite chain of
them.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.78\textwidth]{figs/fig_spin_chain_typeIII.pdf}
\caption{The emergence of non-Type I factor structures from an infinite spin chain: as the number of entangled qubit pairs $N \to \infty$, the discrete eigenvalues of the reduced state merge into a continuous spectrum. At $\theta = \pi/4$, the algebra becomes the hyperfinite Type $\mathrm{II}_1$ factor where projections span a continuous dimension range $d(P) \in [0,1]$. For generic $\theta \in (0, \pi/4)$, the modular operator spectrum spans geometric powers $\lambda^k = (\tan^2\theta)^k$, forming a Type $\mathrm{III}_\lambda$ factor.}
\label{fig:spin_chain_typeIII}
\end{figure}

### Interpreting $\rho_\M$ and $S_\M$: an entropy that can be negative

With the type $\mathrm{II}_1$ trace of eq.~3.11 in hand, eq.~3.1 can be used to compute $\rho_\M$ and eq.~3.2
to compute $S_\M$ for any state you like — and the results have a genuinely surprising feature that's worth
working through with actual numbers, because it looks, at first glance, like it must be a mistake.

Take a state $\ket\Psi$ equal to $\ket{\Phi_{\pi/4}}$ everywhere except that a finite number $k$ of the pairs,
labelled $i_1,\dots,i_k$, are instead prepared in some other two-qubit state $\eta_{i_s}$ (eq.~3.19). Solving
eq.~3.1 for this state (a direct computation, using the same pair-by-pair factorization as Step~2 above) gives

$$

\rho_\M(\Psi) = 2\rho_1\otimes2\rho_2\otimes\cdots\otimes2\rho_n\otimes\cdots

$$

(eq.~3.20), where $\rho_i$ is the ordinary reduced density matrix of pair $i$ in the state $\eta_i$ (and
$2\rho_i=\id_2$ for every pair not among $i_1,\dots,i_k$ — the factor of $2$ coming directly from the
$\tfrac12$ in eq.~3.12). As a sanity check on the normalization: plugging in $\Psi=\Phi_{\pi/4}$ itself gives
$\rho_\M(\Phi_{\pi/4})=\id$ exactly (eq.~3.21) — the trace's own defining state is, unsurprisingly, assigned
the identity as its density operator, since $\tr(A\cdot\id)=\tr(A)=\braket{\Phi_{\pi/4}|A|\Phi_{\pi/4}}$ by
the very definition of $\tr$.

Plugging eq.~3.20 into the entropy formula, eq.~3.2, gives (eq.~3.22)

$$

S_\M(\Psi) = \sum_{s=1}^k S_2(\rho_{i_s}) - k\log2 ,

$$

where $S_2(\rho_{i_s})$ is the ordinary, ranges-from-$0$-to-$\log2$ entanglement entropy of the single
perturbed pair $i_s$. Here is a completely concrete instance, worked with an actual number: take $k=1$, and
let the one perturbed pair be prepared at angle $\phi=0.3$ radians instead of $\pi/4\approx0.785$ radians (so
$\eta_{i_1}=\cos(0.3)\ket{00}+\sin(0.3)\ket{11}$, a less-than-maximally-entangled pair). Direct computation
gives $S_2(\rho_{i_1})\approx0.2963$ (from $p_0=\cos^2(0.3)\approx0.9139$, $p_1=\sin^2(0.3)\approx0.0861$, and
the ordinary two-level entropy formula), while $\log2\approx0.6931$. So

$$

S_\M(\Psi) \approx 0.2963 - 0.6931 = -0.3968 ,

$$

a genuinely, checkably *emph* number. And this isn't a fluke of the particular angle chosen: since
$S_2(\rho_{i_s})\le\log2$ always (the ordinary two-level entropy is bounded above by $\log2$, with equality
only at exact maximal entanglement), every term in the sum in eq.~3.22 satisfies $S_2(\rho_{i_s})-\log2\le0$,
so $S_\M(\Psi)\le0$ for *emph* state built this way, with equality only in the degenerate case where
every perturbed pair happens to still be exactly maximally entangled.

This looks alarming on first sight: $\rho_\M$ is a genuine, positive, correctly-normalized density operator
($\tr\rho_\M=1$, exactly the way a density operator should be), and yet $-\tr(\rho_\M\log\rho_\M)$ came out
negative — something that could *emph* happen for the entropy of an ordinary, finite-dimensional density
matrix (where $-\Tr(\rho\log\rho)\ge0$ always, with equality only for a pure state). There is no contradiction,
and the resolution is worth stating as plainly as possible: $\tr$ here is *emph* the ordinary matrix trace
that counts basis states one at a time. It was built, in Sec.~III.C.1 above, directly out of expectation
values in the maximally entangled reference state $\ket{\Phi_{\pi/4}}$ — and in a type II algebra there is no
minimal projection to serve as "one state," so $\tr$ never had the "count the dimensions" interpretation
that makes the ordinary entropy formula manifestly non-negative in the first place.

What eq.~3.22 is actually computing, the paper shows directly, is minus a *emph* entropy:

$$

S_\M(\Psi) = -S_\M(\Psi\,\|\,\Phi_{\pi/4})

$$

(this also follows, more generally and without needing the special simple form of eq.~3.19, directly from
eq.~3.24 in the paper) — the ordinary relative entropy $S(\rho\|\sigma)=\Tr\rho(\log\rho-\log\sigma)$ from
Sec.~I of this companion, applied here with $\rho=\rho_\M(\Psi)$ and $\sigma=\rho_\M(\Phi_{\pi/4})=\id$.
Relative entropy measures *emph*, and there is nothing about its
definition that prevents $-S(\rho\|\sigma)$ from being negative — quite the opposite, $S(\rho\|\sigma)\ge0$
always, so $-S(\rho\|\sigma)\le0$ always, exactly matching what was just computed. The entropy $S_\M$ in a
type II algebra should be read not as "how many microstates does this occupy," the ordinary statistical
reading that only makes sense once there's a minimal projection to count from, but as **a signed
distance from the maximally entangled background state that defines the trace in the first place** — a
*emph*, not absolute, quantity, and this is the first concrete place in the paper where relative
entropy, rather than entropy on its own, reveals itself as the more fundamental and more robust object. It
survives, essentially unchanged in its definition, all the way through type III (Sec.~IV) and into the
holographic applications starting in Sec.~VI — ordinary entropy, as you've just seen directly, does not
survive intact even this far.


> [!NOTE] **Physics Connection: Negative Relative Entropy in Qubits**
> Before trusting that a genuinely negative "entropy" is a sensible thing for a serious theory to produce, it's
> worth noticing that ordinary, finite-dimensional quantum mechanics already contains this phenomenon, in
> disguise, using nothing beyond the relative entropy formula from Sec.~I. For an ordinary $d$-dimensional
> quantum system, take the relative entropy of any state $\rho$ against the maximally mixed reference
> $\sigma=\id/d$:
> 
$$

> S(\rho\|\sigma) = \Tr\rho\big(\log\rho - \log(\id/d)\big) = -S(\rho) + \log d ,
> 
$$

> using $S(\rho)\equiv-\Tr(\rho\log\rho)$ for the ordinary von Neumann entropy. Since $S(\rho)\le\log d$ always
> (entropy never exceeds the maximally mixed value — a completely standard fact), $S(\rho\|\sigma)\ge0$, exactly
> as relative entropy must be. Now just *emph* and look at $-S(\rho\|\sigma)=S(\rho)-\log d$. For
> a qubit ($d=2$) in the state $\rho=\mathrm{diag}(0.9,0.1)$: $S(\rho)\approx0.325$, while $\log2\approx0.693$,
> so $-S(\rho\|\sigma)\approx-0.368$ — **a manifestly negative number, computed from nothing more exotic
> than an ordinary qubit's entropy, minus a constant.**
> 
> This is not a coincidence dressed up to look relevant — it is exactly the mechanism at work in
> eq.~3.22 above, just with the additive constant made completely explicit. $S_\M$ in a type II algebra is
> built the same way: an ordinary-looking entropy, measured relative to (i.e., shifted down by) whatever
> baseline the maximally entangled reference state assigns. In finite dimensions that baseline is the familiar,
> finite number $\log d$; in the type $\mathrm{II}_1$ Bell-pair-chain algebra, the same baseline is still there,
> it's just been absorbed into the very definition of $\tr$ (built, recall, directly from the maximally entangled
> $\ket{\Phi_{\pi/4}}$) rather than written as a separate $\log d$ term you subtract by hand. **Nothing
> about the arithmetic of entropy changed** — subtracting a constant from an ordinary, everyday entropy was
> always capable of giving a negative number. What's new in the type II case is only that the algebra itself,
> having no minimal projection, leaves no alternative baseline (no "$d$") to normalize against — the maximally
> entangled reference state is not a choice, it's the *emph* thing available to define $\tr$ with in the
> first place.


(One further bookkeeping note, briefly: the paper also observes that for a type $\mathrm{II}_\infty$ factor,
the same interpretation of $\rho_\M$ and $S_\M$ carries over, except that there is no preferred, canonical way
to normalize the trace — unlike the $\mathrm{II}_1$ case, where normalizing $d(\id)=1$ was a natural, forced
choice — so the entropy is only meaningfully defined up to an overall additive, state-independent constant.)

## Sec.~III.D: summary

Pulling the type I and type II discussions together into one statement, worth having explicitly in view before
Sec.~IV introduces type III: the *emph* of the algebra $\M$ describing a subsystem determines, in a
completely general, state-independent way, what *emph* of entanglement pattern every state of the full
system is forced into.


- **Type I factor.** A genuine tensor factorization exists. Pure, completely unentangled product
states exist inside the Hilbert space, and every state is either one of these or a superposition/mixture
built from them — exactly the ordinary Griffiths/Sakurai picture, recovered as the special case where nothing
new is happening.
- **Type II factor.** No minimal projections exist, which means (a fact quoted here, following
directly from the definitions of Sec.~II.C: no minimal projection $\Rightarrow$ no pure state of $\M$ exists
at all) there is no unentangled reference state anywhere in sight. *emph* state of the full system is
entangled across $(\M,\M')$ to some degree — there is no "ground floor" of zero entanglement to compare
against, only a maximally entangled reference state (the one that happens to define the trace), relative to
which the signed entropy of eq.~3.2 is measured.


Type III — where not even a trace exists, so eqs.~3.1 and 3.2 cannot be written down at all — is the subject
of the whole next section, and it is, as flagged repeatedly already, not an exotic corner case: it is the
type that actually governs local regions of relativistic quantum field theory, and holographic boundary
subalgebras in the strict large-$N$ limit that this paper's title promises to explain.



---

# Sec.~IV: Von Neumann algebras and entanglement: type III

This is the technical heart of the whole paper, and it earns that description honestly: type III algebras have
no trace, so eqs.~3.1—3.2 (the density operator $\rho_\M$ and the entropy $S_\M$) simply cannot be written
down — there is no equation left to solve. And yet, as flagged repeatedly, type III is not some exotic
mathematical curiosity to be handled as a special case; it is the type that governs local regions of a
relativistic quantum field theory, and (as Sec.~VII will show) the type that governs holographic boundary
algebras in the strict large-$N$ limit. If the goal is to say anything at all about entanglement in exactly
the settings this paper cares about most, an entirely different tool is needed. That tool is
**Tomita—Takesaki modular theory**, and the core physical idea behind it is worth stating in one sentence
before any formalism: *emph* — entanglement, viewed from inside just one half, always looks
like heat. Everything in this section is that one idea, made completely precise.

## Sec.~IV.A: emergent times from entanglement — modular flows

### Starting from something you already understand: the type I case, retold

To motivate the general construction, go back to an ordinary type I bipartite pure state $\ket\Psi$ with
full-rank reduced density matrix $\rho_R$ ("full-rank" meaning invertible — every eigenvalue strictly
positive, so $\rho_R^{-1}$ exists; this will matter in a moment). Instead of studying the entropy $S_R$
directly, package the same information differently: write

$$

\rho_R = e^{-K_R}, \qquad K_R\equiv-\log\rho_R

$$

(eq.~4.1). $K_R$ is called the **entanglement Hamiltonian**, and $K_R\ge0$ (since $\rho_R$'s eigenvalues
are all in $(0,1]$, their negative logarithms are all $\ge0$). The full set of eigenvalues of $K_R$ — the
*emph* — carries strictly more information than the entropy $S_R$ alone or any finite
list of R\'enyi entropies (each of those is just some specific weighted sum over the spectrum; the full
spectrum is the un-summed data), which is why condensed-matter physicists studying entanglement spectra
directly (rather than just the single number $S_R$) have found it such a fruitful diagnostic tool.

Now use $K_R$ to generate a flow:

$$

A(s) = e^{iK_Rs}Ae^{-iK_Rs} \in B(\HH_R), \qquad A\in B(\HH_R)

$$

(eq.~4.2) — this is formally identical to ordinary Heisenberg time evolution, $A(t)=e^{iHt}Ae^{-iHt}$, with
$K_R$ playing the role of a Hamiltonian and $s$ playing the role of time. It's called **modular flow**,
and $s$ is called **modular time**. The key physical claim, which is really just the statement that
$e^{-K_R}=\rho_R$ is already, by construction, an ordinary Gibbs thermal density matrix at (dimensionless)
inverse temperature $\beta=1$ for the "Hamiltonian" $K_R$: an observer confined to $R$, using $s$ as their
notion of time, should see their system in thermal equilibrium — meaning correlation functions of
modular-flowed operators satisfy the **Kubo—Martin—Schwinger (KMS) condition**, the mathematical
signature of thermal equilibrium (spelled out precisely below).

You can do the same construction on the $L$ side, with $K_L=-\log\rho_L$. To treat both sides on equal
footing at once, define

$$

\Delta_\Psi \equiv \rho_R\otimes\rho_L^{-1}, \qquad -\log\Delta_\Psi = K_R - K_L

$$

(eq.~4.3), and let the modular flow act on operators of *emph* side:

$$

\sigma_s(A) \equiv \Delta_\Psi^{-is}A\Delta_\Psi^{is}\in B(\HH_R),\ \ A\in B(\HH_R), \qquad
\sigma_s(A') \equiv \Delta_\Psi^{-is}A'\Delta_\Psi^{is}\in B(\HH_L),\ \ A'\in B(\HH_L)

$$

(eqs.~4.4—4.5) — check this reduces to eq.~4.2 for $A\in B(\HH_R)$: since $\rho_L^{-1}$ (and hence any power
of it) commutes past $A\otimes\id_L$ trivially, $\Delta_\Psi^{-is}A\Delta_\Psi^{is}=\rho_R^{-is}A\rho_R^{is}$,
exactly eq.~4.2 with $s\leftrightarrow$ what was called $s$ there (a short but worthwhile check — it confirms
the joint object $\Delta_\Psi$ correctly reduces to the separate one-sided flows on each side). $\Delta_\Psi$
is called the **modular operator**.


> [!EXAMPLE] **Worked Example:**
> Take $\ket{\phi_\theta}=\cos\theta\ket{00}+\sin\theta\ket{11}$
> from Sec.~I, so $\rho_R=\rho_L=\mathrm{diag}(\cos^2\theta,\sin^2\theta)$, and write out $\Delta_\Psi=
> \rho_R\otimes\rho_L^{-1}$ as an explicit $4\times4$ matrix in the basis $\ket{00},\ket{01},\ket{10},\ket{11}$:
> 
$$

> \Delta_\Psi = \begin{pmatrix} 1&0&0&0\\ 0&\cos^2\theta/\sin^2\theta&0&0\\
> 0&0&\sin^2\theta/\cos^2\theta&0\\0&0&0&1\end{pmatrix} = \operatorname{diag}\left(1, \; \cot^2\theta, \; \tan^2\theta, \; 1\right) .
> 
$$

> Its eigenvalues are $1$ (multiplicity two, on $\ket{00}$ and $\ket{11}$), $\lambda\equiv\tan^2\theta$ (on $\ket{10}$), and $\lambda^{-1}=\cot^2\theta$ (on $\ket{01}$).
> 
> Now let us construct the Tomita operator $S_\Psi$, its adjoint $F_\Psi = S_\Psi^\dagger$, and the modular conjugation $J_\Psi$ explicitly from first principles:
> 
1. **Action of the algebra on $\ket{\phi_\theta**$:} Any operator $A \in B(\HH_R)$ has the form $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$. Its action on $\ket{\phi_\theta}$ produces:
> 
$$

> (A\otimes\id_L)\ket{\phi_\theta} = a\cos\theta\ket{00} + b\sin\theta\ket{01} + c\cos\theta\ket{10} + d\sin\theta\ket{11} .
> 
$$

> Given an arbitrary 4-component vector $\ket x = x_{00}\ket{00} + x_{01}\ket{01} + x_{10}\ket{10} + x_{11}\ket{11}$, matching coefficients gives $a = x_{00}/\cos\theta$, $b = x_{01}/\sin\theta$, $c = x_{10}/\cos\theta$, $d = x_{11}/\sin\theta$.
> 
>
2. **The Tomita operator $S_\Psi$:** By definition, $S_\Psi$ maps $(A\otimes\id_L)\ket{\phi_\theta} \mapsto (A^\dagger\otimes\id_L)\ket{\phi_\theta}$. Since $A^\dagger = \begin{pmatrix} a^* & c^* \\ b^* & d^* \end{pmatrix}$, we have:
> 
$$

> (A^\dagger\otimes\id_L)\ket{\phi_\theta} = a^*\cos\theta\ket{00} + c^*\sin\theta\ket{01} + b^*\cos\theta\ket{10} + d^*\sin\theta\ket{11} .
> 
$$

> Substituting the expressions for $a,b,c,d$ in terms of $x_{ij}$:
> 
$$

> S_\Psi \begin{pmatrix} x_{00} \\ x_{01} \\ x_{10} \\ x_{11} \end{pmatrix} = \begin{pmatrix} x_{00}^* \\ \frac{\sin\theta}{\cos\theta} x_{10}^* \\ \frac{\cos\theta}{\sin\theta} x_{01}^* \\ x_{11}^* \end{pmatrix} = \begin{pmatrix} x_{00}^* \\ \tan\theta\, x_{10}^* \\ \cot\theta\, x_{01}^* \\ x_{11}^* \end{pmatrix} .
> 
$$

> Notice that applying $S_\Psi$ twice gives $S_\Psi^2\ket x = \ket x$, verifying $S_\Psi^2 = \id_4$ and $S_\Psi\ket{\phi_\theta} = \ket{\phi_\theta}$!
> 
>
3. **The adjoint operator $F_\Psi \equiv S_\Psi^\dagger$:** From the inner product relation $\braket{y|S_\Psi x} = \braket{x|F_\Psi y}^*$, we find:
> 
$$

> F_\Psi \begin{pmatrix} y_{00} \\ y_{01} \\ y_{10} \\ y_{11} \end{pmatrix} = \begin{pmatrix} y_{00}^* \\ \cot\theta\, y_{10}^* \\ \tan\theta\, y_{01}^* \\ y_{11}^* \end{pmatrix} .
> 
$$

> 
>
4. **The modular operator $\Delta_\Psi = F_\Psi S_\Psi$:** Multiplying the two operators:
> 
$$

> \Delta_\Psi \begin{pmatrix} x_{00} \\ x_{01} \\ x_{10} \\ x_{11} \end{pmatrix} = F_\Psi \begin{pmatrix} x_{00}^* \\ \tan\theta\, x_{10}^* \\ \cot\theta\, x_{01}^* \\ x_{11}^* \end{pmatrix} = \begin{pmatrix} x_{00} \\ \cot^2\theta\, x_{01} \\ \tan^2\theta\, x_{10} \\ x_{11} \end{pmatrix} ,
> 
$$

> which is exactly the diagonal matrix $\Delta_\Psi = \operatorname{diag}(1, \cot^2\theta, \tan^2\theta, 1)$!
> 
>
5. **The modular conjugation $J_\Psi = S_\Psi \Delta_\Psi^{-1/2**$:} The square root is $\Delta_\Psi^{1/2} = \operatorname{diag}(1, \cot\theta, \tan\theta, 1)$. Applying $S_\Psi$ to $\Delta_\Psi^{-1/2}\ket x$:
> 
$$

> J_\Psi \begin{pmatrix} x_{00} \\ x_{01} \\ x_{10} \\ x_{11} \end{pmatrix} = S_\Psi \begin{pmatrix} x_{00} \\ \tan\theta\, x_{01} \\ \cot\theta\, x_{10} \\ x_{11} \end{pmatrix} = \begin{pmatrix} x_{00}^* \\ x_{10}^* \\ x_{01}^* \\ x_{11}^* \end{pmatrix} .
> 
$$

> $J_\Psi$ is anti-unitary, satisfies $J_\Psi^2 = \id$, and acts as complex conjugation composed with the SWAP of qubits $\ket{01} \leftrightarrow \ket{10}$! Furthermore, $J_\Psi \Delta_\Psi J_\Psi = \Delta_\Psi^{-1}$.
> 
>
6. **Exact modular flow on Pauli matrices:** The modular flow of an observable $A \in B(\HH_R)$ is $\sigma_s(A) = \Delta_\Psi^{-is} (A\otimes\id_L) \Delta_\Psi^{is}$.
> 


> Modular flow on the qubit is an **exact spatial rotation** in the $xy$-plane of the Bloch sphere around the $z$-axis with constant angular frequency $\Omega = 2\log\cot\theta$!
>



Two facts about $\Delta_\Psi$ deserve to be stated plainly, because they are the two facts that survive,
completely unchanged in spirit, all the way to the fully general (type III) theory below.


1. $\Delta_\Psi\ket\Psi=\ket\Psi$, and in fact $\Delta_\Psi^{-1}\ket\Psi=\ket\Psi$ too, i.e.\
$(K_R-K_L)\ket\Psi=0$ (eq.~4.6) — check this directly on the worked example: $\ket\Psi=\ket{\phi_\theta}=
\cos\theta\ket{00}+\sin\theta\ket{11}$ is built entirely out of the two eigenvalue-$1$ eigenvectors of
$\Delta_\Psi$, so of course $\Delta_\Psi$ fixes it exactly. This says the modular flow is a kind of emergent,
purely internal time evolution under which the physical state itself never changes at all, even though the
flow acts nontrivially on operators living separately in $R$ and in $L$. This is also the precise, operator
version of the elementary fact that $S_R=S_L$ for a pure global state (Sec.~I): $\rho_R$ and $\rho_L$ have
the same set of eigenvalues (this is exactly what the Schmidt decomposition guarantees), so $K_R$ and $K_L$
have the same spectrum too, and $(K_R-K_L)\ket\Psi=0$ is one precise way of encoding that symmetry as an
operator statement.
2. Correlators of modular-flowed operators satisfy the KMS condition — made fully precise just below —
which is exactly the mathematical signature of thermal equilibrium at $\beta=1$: an observer with access only
to $R$ (or only to $L$), using modular time as their clock, experiences a genuinely thermal state.


### The swap operator $J_\Psi$

There's a third, related object worth building explicitly, because it will reappear repeatedly. The
requirement that $\rho_R,\rho_L$ both be full-rank forces $\dim\HH_R=\dim\HH_L$ (a full-rank density matrix on
$\HH_R$ has as many nonzero eigenvalues as $\dim\HH_R$; by the Schmidt decomposition, that must match the
number of nonzero Schmidt coefficients, which is at most $\dim\HH_L$ too — so the two dimensions must agree
exactly for both reduced density matrices to be simultaneously full-rank). This matching dimension lets you
build an explicit **swap operator**: writing the Schmidt decomposition $\ket\Psi=\sum_n\sqrt{\lambda_n}
\ket n_R\ket n_L$, and a general vector $\ket\phi=\sum_{mn}\phi_{mn}\ket m_R\ket n_L$ in this same Schmidt
basis, define

$$

J_\Psi\ket\phi = \sum_{m,n}\phi_{mn}^*\ket n_R\ket m_L

$$

(eq.~4.7) — it swaps the labels $R\leftrightarrow L$ *emph* complex-conjugates every coefficient. $J_\Psi$
is **anti-unitary** (it involves that complex conjugation — a genuinely different kind of map from an
ordinary unitary, which is why it needs its own name), and $J_\Psi^2=\id$ (eq.~4.8, checked immediately: swap
twice and conjugate twice, and you're back where you started). One can check directly that conjugating an
operator in $\M=B(\HH_R)\otimes\id_L$ by $J_\Psi$ produces an operator in $\M'=\id_R\otimes B(\HH_L)$ — $J_\Psi$
literally exchanges the subsystem with its complement, at the level of operators, not just of vectors. This is
called the **modular conjugation operator**.

### The key limitation, and the reformulation that removes it

Everything above required $\rho_R,\rho_L$ full-rank — a real restriction, forcing (among other things)
$\dim\HH_R=\dim\HH_L$, which already rules out plenty of ordinary type I examples, let alone type II or III
where there's no $\rho_R$ at all. The entire strategic move of this subsection is to find a way of restating
"$\rho_R,\rho_L$ full-rank" that makes no reference whatsoever to $\rho_R,\rho_L$ — so that it can survive
into a setting where those objects don't exist.

The needed restatement uses exactly the two properties singled out at the end of Sec.~II.D of this companion:
**cyclic** and **separating**. Recall: $\ket\Psi$ is cyclic with respect to $\M$ if $\{A\ket\Psi :
A\in\M\}$ is dense in $\HH$ (the algebra can reach essentially everywhere, starting from $\ket\Psi$); it is
separating with respect to $\M$ if $A\ket\Psi=0$ forces $A=0$ (no nonzero operator in $\M$ is wasted on
$\ket\Psi$). It's a short exercise (not carried out in the paper, but genuinely short) to check that
"$\rho_R,\rho_L$ both full-rank" is *emph* to ``$\ket\Psi$ is cyclic with respect to both
$\M=B(\HH_R)\otimes\id_L$ and its commutant $\M'=\id_R\otimes B(\HH_L)$.'' And there's a further, genuinely
elegant simplification available: $\ket\Psi$ being cyclic with respect to $\M'$ turns out to be equivalent to
$\ket\Psi$ being *emph* with respect to $\M$ (cyclic for the complement $\iff$ separating for the
algebra itself — a duality worth sitting with, since it means you never need to check both algebras
separately). So the entire condition collapses to a single, self-contained statement about $\M$ alone:
**$\ket\Psi$ is cyclic and separating with respect to $\M$.** This is a genuinely important moment in the
logical structure of the paper — it shows, one more time, that everything about bipartite entanglement really
is encoded in the algebra of just one side, with no need to reference the complement at all.

### The Tomita—Takesaki theorem, stated in full

Here is the theorem, and it holds for *emph* von Neumann algebra $\M$ with a cyclic and separating vector
$\ket\Psi$ — no reference anywhere in its statement to a trace, a density matrix, or a tensor factorization.
This is exactly why it survives into type III.


1. There is a positive operator $\Delta_\Psi$ (still called the *emph*) leaving
$\ket\Psi$ invariant, $\Delta_\Psi\ket\Psi=\ket\Psi$ (eq.~4.9), and $K_\Psi\equiv-\log\Delta_\Psi$ generates a
genuine automorphism of $\M$ (a map from $\M$ to itself that respects all the algebra structure) and,
separately, of $\M'$:

$$

\sigma_s(A) \equiv \Delta_\Psi^{-is}A\Delta_\Psi^{is}\in\M\ \ \forall A\in\M,
\qquad
\sigma_s(A') \equiv \Delta_\Psi^{-is}A'\Delta_\Psi^{is}\in\M'\ \ \forall A'\in\M'

$$

(eqs.~4.10—4.11) — the flow really does stay inside the algebra it started in, at every modular time $s$, for
both $\M$ and $\M'$ separately.
2. There is an antiunitary **modular conjugation** $J_\Psi$ satisfying
$J_\Psi\ket\Psi=\ket\Psi$, $J_\Psi=J_\Psi^{-1}=J_\Psi^\dagger$, $J_\Psi\Delta_\Psi J_\Psi=\Delta_\Psi^{-1}$
(eq.~4.12), and $J_\Psi\M J_\Psi=\M'$, $J_\Psi\M'J_\Psi=\M$ (eq.~4.13) — $J_\Psi$ swaps $\M$ and $\M'$,
exactly the role the explicit swap operator played in the type I worked example above, now established as a
general fact.
3. A technical but important analyticity statement (eq.~4.14—4.15, stated here for completeness but not
needed for the physical content that follows): the vector $\Delta_\Psi^{-is}A\ket\Psi$, as a function of $s$,
extends to complex values of $s$ in the strip $\Im s\in(0,\tfrac12)$, with a specific relation,
$\Delta_\Psi^{-i(t+i/2)}A\ket\Psi=\Delta_\Psi^{-it}J_\Psi A^\dagger\ket\Psi$, holding on the boundary of that
strip.
4. Correlation functions of modular-flowed operators, $f_{AB}(s)\equiv\braket{\Psi|\sigma_s(A)B|\Psi}$,
analytically continue into the wider strip $\Im s\in(-1,0)$ and satisfy the **KMS relation**

$$

f_{AB}(s) = f_{BA}(-s-i)

$$

(eqs.~4.16—4.17) — this is the precise mathematical statement of "looks thermal at $\beta=1$": it is
exactly the periodicity-in-imaginary-time relation that an ordinary thermal correlator, $\Tr(e^{-\beta H}A(t)B)$,
satisfies (with $\beta=1$ here, and the KMS relation being the operator-algebra way of encoding the cyclic
property of the trace $\Tr(e^{-\beta H}\cdots)$ without ever needing $e^{-\beta H}$ to literally exist as a
trace-class operator — precisely what's needed once no trace exists at all, as in type III).



> [!NOTE] **Physics Connection: KMS Condition in Thermal QFT**
> You have almost certainly already met the KMS relation, just not by that name, in an ordinary
> finite-temperature quantum mechanics or statistical field theory course, and it's worth checking the
> identical relation on a completely mundane example before trusting it applies to a type III algebra with no
> Hamiltonian at all. Take an ordinary two-level system, $H=\omega\ket1\!\bra1 = \begin{pmatrix} 0 & 0 \\ 0 & \omega \end{pmatrix}$, in the thermal (Gibbs) state:
> 
$$

> \rho = \frac{e^{-\beta H}}{Z} = \frac{1}{1 + e^{-\beta\omega}} \begin{pmatrix} 1 & 0 \\ 0 & e^{-\beta\omega} \end{pmatrix} .
> 
$$

> For two operators $A, B$, define $f_{AB}(t) \equiv \Tr(\rho A(t) B)$ where $A(t) = e^{iHt} A e^{-iHt}$. Let us prove analytically that $f_{AB}(t) = f_{BA}(-t-i\beta)$:
> \begin{align*}
> f_{AB}(t) &= \Tr\left( \frac{e^{-\beta H}}{Z} e^{iHt} A e^{-iHt} B \right) \\
> &= \Tr\left( B \, \frac{e^{-\beta H}}{Z} e^{iHt} A e^{-iHt} \right) \qquad \text{(by cyclicity of the trace)} \\
> &= \Tr\left( \frac{e^{-\beta H}}{Z} \left[ e^{\beta H} B e^{-\beta H} \right] e^{iHt} A e^{-iHt} \right) \\
> &= \Tr\left( \rho \, B(-i\beta) \, A(t) \right) .
> \end{align*}
> Applying time-translation invariance to both operators (shifting $t \to 0$ and $0 \to -t$):
> \begin{align*}
> f_{AB}(t) &= \Tr\left( \rho \, e^{-iHt} B(-i\beta) e^{iHt} \, A \right) = \Tr\left( \rho \, B(-t - i\beta) \, A \right) = f_{BA}(-t - i\beta) .
> \end{align*}
> This algebraic proof relies only on the cyclicity of the trace and the group property $e^{-\beta H} e^{iHt} = e^{i(t + i\beta)H}$. It shows why thermal states are periodic in imaginary time with period $\beta$. Tomita—Takesaki theory abstracts this exact property to define thermal states at $\beta=1$ without assuming a trace or Hamiltonian.
> 
> So what changed, going from this ordinary example to the general Tomita—Takesaki statement? Only this: here,
> the flow generating $A(t)$ was an honest Hamiltonian $H$, and $\rho$ was a genuine, normalizable density
> matrix you could write down as a finite matrix. In Sec.~IV.A's general theorem, neither of those needs to
> exist — $\sigma_s$ can be *emph* flow with no Hamiltonian living in $\M$ at all (exactly the defining
> property of type III, eq.~4.21), and there may be no $\rho$ to build a trace out of. The KMS relation survives
> this demotion completely intact, because it was never really a statement about $H$ or $\rho$ individually —
> it's a statement about the correlator $f_{AB}$ alone, which is exactly why it, rather than the Hamiltonian or
> the density matrix, is the object General Tomita—Takesaki theory promotes to primary status.


Read physically, in one sentence: *emph* operator algebra equipped with a cyclic-and-separating reference
vector automatically comes with a canonical, built-in notion of time flow, one under which the reference state
itself looks exactly thermal at inverse temperature $1$ — and this holds completely independently of whether
$\M$ has a trace. This is the sense in which the type I story above is not being generalized by analogy, but
literally subsumed as the special case where the canonical flow happens to be generated by an honest
Hamiltonian $K_R$ that lives inside $\M$ itself.

A handful of remarks the paper makes here are worth keeping explicitly:

- [(a)] Physically: given $\M$ and a cyclic-separating $\ket\Psi$, there is an emergent time evolution,
internal to $\M$ (or to $\M'$), that leaves $\ket\Psi$ fixed, and relative to which an observer confined to
$\M$ (or to $\M'$) feels a genuine temperature $1/\beta=1$.
- [(b)] For type I, the cyclic-and-separating condition was a genuinely restrictive requirement (forcing
$\dim\HH_R=\dim\HH_L$). For the type III situations this paper actually cares about — quantum field theory,
statistical mechanics in the thermodynamic limit — this condition turns out to be satisfied *emph*,
as you'll see explicitly in Secs.~IV.C and IV.D below (Reeh—Schlieder theorem, and the $N\to\infty$
entangled-spin construction).
- [(c)] The theorem is usually *emph* (not merely stated) by first defining an antilinear
**Tomita operator** $S_\Psi$ directly from $\M$ and $\ket\Psi$,

$$

S_\Psi A\ket\Psi = A^\dagger\ket\Psi\ \ (A\in\M), \qquad
S_\Psi A'\ket\Psi = A'^\dagger\ket\Psi\ \ (A'\in\M') ,

$$


$$

S_\Psi^2=\id, \qquad S_\Psi\ket\Psi=\ket\Psi ,

$$

(eqs.~4.18—4.19 — note $S_\Psi$ is well-defined here precisely because $\ket\Psi$ is separating, the same
role separating played in the GNS construction of Sec.~II.D), and then taking its **polar
decomposition**: writing $S_\Psi=J_\Psi\Delta_\Psi^{1/2}$ (eq.~4.20), the operator analogue of writing a
complex number as $z=e^{i\phi}|z|$ — an antiunitary "phase" $J_\Psi$ times a positive "modulus"
$\Delta_\Psi^{1/2}$. Every statement above is then a theorem derived from this one definition (a genuinely
technical piece of functional analysis, not reproduced here, but worth knowing the construction exists and
where it starts).
- [(d)] Conversely — a fact used to actually *emph* the modular operator in specific physical
examples, including the Rindler-wedge computation in Sec.~IV.D below — if you can find *emph* operator
that generates an automorphism of $\M$ (in the sense of eqs.~4.10—4.11) and whose flow satisfies the KMS
relation, it *emph* the modular operator for $\ket\Psi$. There is only one flow with these properties,
so finding one by any means (a physical argument, a symmetry, a guess later verified) is enough.
- [(e)] If $\M$ is type II, $\rho_\M,\rho_{\M'}$ (Sec.~III's density operators) exist, and $\Delta_\Psi$
can still be built from eq.~4.3, now with $\rho_\M,\rho_{\M'}$ in place of $\rho_R,\rho_L$. If $\ket\Psi$
happens to be the tracial state itself (so $\rho_\M=\rho_{\M'}=\id$), then $\Delta_\Psi=\id$ — exactly the
worked example above at $\theta=\pi/4$.
- [(f)] If $\M$ is type III, $\Delta_\Psi$ cannot be split as a product $\rho_\M\otimes\rho_{\M'}^{-1}$ at
all — there is no $\rho_\M$ to split it into. $\Delta_\Psi$ still exists (by the theorem above), but it is now
an irreducibly joint object with no factorized description.


Finally, one lemma worth keeping close at hand, because it does real work starting in Sec.~VII (it's exactly
the mechanism behind entanglement-wedge reconstruction going strictly beyond causal-wedge reconstruction):

\begin{quote}
**Lemma (an "ergodic" property of modular flow).** If $\N\subset\mathcal X$ are two von Neumann algebras
and $\ket\Psi$ is jointly cyclic and separating for both, then the modular flow $\sigma_s$ of the
*emph* algebra $\mathcal X$, applied to the *emph* algebra $\N$, regenerates all of
$\mathcal X$: $\{\sigma_s(A):A\in\N, s\in\mathbb R\}''=\mathcal X$.
\end{quote}
In words: flowing a small piece of an algebra in modular time, using the larger algebra's own modular clock,
sweeps out the entire larger algebra. This sounds almost too strong to be true on first reading, and it's
worth remembering as a flag for exactly the kind of counter-intuitive but rigorously established fact modular
theory keeps producing.

## Sec.~IV.B: classification of type III factors

### Telling type III apart from type I and II, using modular flow alone

Here is a clean, checkable criterion, stated already in Sec.~II.B of this companion's discussion of modular
flow (eq.~4.22, "inner automorphism"), now established as the actual dividing line between the types:

$$

\sigma_s(\M) \text{ is an inner automorphism of } \M \text{ for *emph* } s\in\mathbb R

$$


$$

\iff \qquad \M \text{ is type I or type II}

$$

(eq.~4.21), where $\sigma_s$ being an **inner automorphism** means there's a unitary $U_s\in\M$ itself
(not just some unitary on $\HH$, but one actually belonging to the algebra) implementing the flow,
$\sigma_s(A)=U_sAU_s^\dagger$. For type I and type II, this holds with $U_s=e^{-iK_Rs}$ (or the type-II
analogue built from $\rho_\M$) — exactly the ordinary type I story from earlier in this section, now
recognized as "the flow is inner." The content of eq.~4.21, read the other direction: **for a type III
algebra, there must exist *emph* This is, in fact, the cleanest possible operational definition of type
III: modular time genuinely flows, but no clock generating that flow can be found anywhere inside the algebra
being flowed.

### State-independence: relating the flows of different reference vectors

The modular operator $\Delta_\Psi$, and hence the flow $\sigma_s^\Psi$, depends on which cyclic-separating
reference vector $\ket\Psi$ you chose. For a different choice $\ket\Omega$, you'd get a different
$\Delta_\Omega$ and flow $\sigma_s^\Omega$. It's a genuine (and reassuring) theorem that these different flows
are never wildly unrelated: there exists a family of unitaries $u_{\Psi\Omega}(s)\in\M$, one for each $s$,
relating the two,

$$

\sigma_s^\Psi(A) = u_{\Psi\Omega}(s)\,\sigma_s^\Omega(A)\,u_{\Psi\Omega}(s)^\dagger, \qquad \forall A\in\M

$$

(eq.~4.23) — different reference states give modular flows that differ only by an inner automorphism, never
by anything more drastic. (A short consistency check worth having explicitly: applying this relation
transitively through a third vector $\Phi$ forces the chain rule $u_{\Psi\Omega}(t)u_{\Omega\Phi}(t)=
u_{\Psi\Phi}(t)$, eq.~4.25 — exactly what you'd want from "relating flows" to be a self-consistent notion.)

This lets two genuinely **state-independent** invariants of the algebra $\M$ itself be defined — numbers
or sets that depend only on $\M$, not on which reference vector happened to be used to compute them, which is
precisely why they're useful for *emph* algebras rather than states:

$$

T(\M) \equiv \{t\in\mathbb R : \sigma_t^\Psi \text{ is inner on } \M\}

$$

(eq.~4.26 — independent of $\Psi$ by eq.~4.23, since being related by an inner automorphism doesn't change
whether something itself is inner), and

$$

S(\M) \equiv \bigcap_\Psi \sigma(\Delta_\Psi) \subset \mathbb R_{\ge0}

$$

(eq.~4.27 — the intersection, over *emph* possible cyclic-separating reference vector, of the spectrum
of the resulting modular operator; whatever survives this intersection is a property of $\M$ alone). These are
**Connes' two fundamental invariants**. By eq.~4.21, $T(\M)=\mathbb R$ (every modular time is inner) for
type I and type II; for type III it's a proper subset of $\mathbb R$ (in fact, a set of Lebesgue measure
zero — "almost none" of the real line, in a precise sense). For type I or type II, $S(\M)=\{1\}$ (since
there's always a tracial state for which $\Delta_\Psi=\id$, whose spectrum is the single point $\{1\}$ — for
the $\mathrm{I}_\infty,\mathrm{II}_\infty$ cases this tracial state isn't itself normalizable, but can be
approached arbitrarily closely by normalizable ones, footnote~24).

Connes proved — a genuine, hard theorem, not re-derived here — that $S(\M)$ must be a closed multiplicative
subgroup of $\mathbb R_{>0}$ (together with $0$), and this algebraic constraint forces exactly three
possibilities, no others:

$$

\text{Type III}_0:\ S(\M)=\{0,1\}, \qquad
\text{Type III}_\lambda:\ S(\M)=\{0\}\cup\{\lambda^n : n\in\mathbb Z\},\ \lambda\in(0,1),

$$


$$

\text{Type III}_1:\ S(\M)=\mathbb R_{\ge0} .

$$

(eqs.~4.28—4.30). This is genuinely as fine-grained as the classification gets, and every physically relevant
type III algebra in the rest of this paper is one of these three.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.95\textwidth]{figs/fig_connes_spectrum.pdf}
\caption{Connes' modular spectrum classification of von Neumann factors. The invariant $S(\mathcal{M}) \equiv \bigcap_\Psi \mathrm{Spec}(\Delta_\Psi) \subset \mathbb{R}_{\ge 0}$ characterizes the factor type: Types $\mathrm{I}$ and $\mathrm{II}$ have trivial spectrum $\{1\}$; Type $\mathrm{III}_0$ has $\{0, 1\}$; Type $\mathrm{III}_\lambda$ ($0 < \lambda < 1$) forms a discrete geometric ladder $\{0\} \cup \lambda^{\mathbb{Z}}$ (Powers factors); and Type $\mathrm{III}_1$ fills the entire non-negative continuum $[0, \infty)$ (relativistic QFT subregions and large-$N$ holography).}
\label{fig:connes_spectrum}
\end{figure}

(The paper closes this subsection with further technical properties of the intertwining unitaries $u_{\Psi\Omega}(s)$ — a cocycle identity, eq.~4.31,
and a converse construction showing any function satisfying that identity comes from some genuine reference
vector, eq.~4.34 — used later as machinery rather than as physical content in their own right, so they're
flagged here for completeness but not expanded further.)

## Sec.~IV.C: the entangled spin example revisited

Here is the promised payoff: computing $S(\M_\theta)$ and $T(\M_\theta)$ explicitly, by hand, for the
$N$-Bell-pair-chain algebra $\M_\theta\equiv\M_R(\theta)$ from Sec.~II.E, and finding that different $\theta$
genuinely do give different type $\mathrm{III}_\lambda$ subtypes.

### Setting up the finite-$N$ computation

At finite $N$, the $R$-system algebra is ordinary type I, and the reduced density matrices are just $N$-fold
tensor products of the single-pair result already computed in Sec.~I:

$$

\rho_R(\Phi_\theta) = \rho_r(\phi_\theta)^{\otimes N}, \qquad
\rho_r(\phi_\theta) = \begin{pmatrix}\cos^2\theta&0\\0&\sin^2\theta\end{pmatrix},

$$

(eqs.~4.35—4.36, and identically for $\rho_L$, since the pair is symmetric between $R$ and $L$). For
$\theta\in(0,\pi/4)$, both are strictly positive (full rank — every diagonal entry nonzero), so
$\ket{\Phi_\theta}$ is cyclic and separating with respect to the $R$-algebra at every finite $N$, and the
modular operator can be built directly from eq.~4.3:

$$

\Delta_{\Phi_\theta} = \rho_R(\Phi_\theta)\otimes\rho_L(\Phi_\theta)^{-1} = \delta_\theta^{\otimes N},
\qquad \delta_\theta \equiv \rho_r(\phi_\theta)\otimes\rho_l(\phi_\theta)^{-1}

$$

(eq.~4.37) — exactly the single-pair worked example already computed explicitly in Sec.~IV.A above, whose
eigenvalues were found there (and verified symbolically) to be $(1,\lambda,\lambda^{-1})$ with
$\lambda=\tan^2\theta$. Tensoring $N$ independent, identical copies together, the eigenvalues of the full
$\Delta_{\Phi_\theta}$ are all possible products,

$$

\bigotimes_{i=1}^N(1,\lambda,\lambda^{-1}) = \prod_{i=1}^N\lambda^{\alpha_i}, \qquad \alpha_i\in\{0,1,-1\}

$$

(eq.~4.38) — each of the $N$ pairs independently contributes a factor of $1$, $\lambda$, or $\lambda^{-1}$ to
the product, and every possible combination of choices appears as an eigenvalue.

### Taking $N\to\infty$, and reading off the type

As $N\to\infty$, the set of achievable exponents $n=\sum_i\alpha_i$ (each term $0$ or $\pm1$, summed over
infinitely many independent choices) becomes every integer, each with growing multiplicity, so the set of
eigenvalues $\lambda^n$ becomes dense in a specific set:

$$

\sigma(\Delta_{\Phi_\theta}) = \{0\}\cup\{\lambda^n : n\in\mathbb Z\}

$$

(eq.~4.39 — the $\{0\}$ appears in the limit because, as $N\to\infty$, you can make the exponent $n$ as
negative as you like by choosing more and more of the $\alpha_i=-1$, driving $\lambda^n=\lambda^{-|n|}\to
\infty$'s reciprocal, i.e., pushing arbitrarily close to zero from above — more carefully, this limiting
statement about the spectrum is the honest infinite-$N$ statement that the finite-$N$ computation above
approaches).

\begin{keyresult}[: Spectral Derivation of the Connes Invariant for the Powers Factor]
**Goal:** Prove that for the infinite entangled spin chain $\M_\theta$ with $\theta \in (0, \pi/4)$ and $\lambda = \tan^2\theta$:

$$

\mathrm{Spec}(\Delta_{\Phi_\theta}) = \{0\} \cup \{\lambda^n : n \in \mathbb{Z}\}, \qquad S(\M_\theta) \equiv \bigcap_{\Psi} \mathrm{Spec}(\Delta_\Psi) = \{0\} \cup \lambda^{\mathbb{Z}} .

$$

**Derivation:**

1. **Action on the local GNS basis:**
The GNS Hilbert space $\HH_\theta$ is the completion of the span of local operator excitations acting on $\ket{\Phi_\theta}$:

$$

\ket{\Psi_{\{a_k\}}} \equiv \big(a_1 \otimes a_2 \otimes \cdots \otimes a_m \otimes \id \otimes \cdots\big) \ket{\Phi_\theta} .

$$

Expand each single-site $2\times2$ matrix in the standard transition basis $\{e_{00}, e_{01}, e_{10}, e_{11}\}$, where $e_{ij} \equiv \ket{i}\bra{j}$.
Using the Tomita involution $S_\phi (a\ket\phi) = a^\dagger\ket\phi$ on a single pair $\ket\phi = \cos\theta\ket{00} + \sin\theta\ket{11}$:
\begin{align*}
S_\phi (e_{00}\ket\phi) &= S_\phi (\cos\theta\ket{00}) = e_{00}^\dagger\ket\phi = \cos\theta\ket{00} = e_{00}\ket\phi , \\
S_\phi (e_{11}\ket\phi) &= S_\phi (\sin\theta\ket{11}) = e_{11}^\dagger\ket\phi = \sin\theta\ket{11} = e_{11}\ket\phi , \\
S_\phi (e_{01}\ket\phi) &= S_\phi (\sin\theta\ket{01}) = e_{10}\ket\phi = \cos\theta\ket{10} = \frac{\cos\theta}{\sin\theta} (e_{01}\ket\phi)^* \dots
\end{align*}
Computing the adjoint $S_\phi^\dagger$ and modular operator $\delta_\theta = S_\phi^\dagger S_\phi = \rho_r \otimes \rho_l^{-1}$ on the matrix basis gives the four exact eigenvectors:

$$

\delta_\theta (e_{00}\ket\phi) = 1 \cdot (e_{00}\ket\phi), \qquad \delta_\theta (e_{11}\ket\phi) = 1 \cdot (e_{11}\ket\phi),

$$


$$

\delta_\theta (e_{10}\ket\phi) = \tan^2\theta \cdot (e_{10}\ket\phi) = \lambda \cdot (e_{10}\ket\phi), \qquad \delta_\theta (e_{01}\ket\phi) = \cot^2\theta \cdot (e_{01}\ket\phi) = \lambda^{-1} \cdot (e_{01}\ket\phi) .

$$

2. **Eigenvalue spectrum on the infinite chain:**
On any product state involving $n_+$ raising transitions $e_{10}$ and $n_-$ lowering transitions $e_{01}$ across the chain:

$$

\Delta_{\Phi_\theta} \ket{\Psi} = \lambda^{n_+ - n_-} \ket{\Psi} = \lambda^n \ket{\Psi}, \qquad n = n_+ - n_- \in \mathbb{Z} .

$$

Since $n_+$ and $n_-$ can be chosen independently as any non-negative integers, the set of eigenvalues is precisely the geometric progression $\{\lambda^n : n \in \mathbb{Z}\}$.
Because the spectrum of a self-adjoint operator is closed, and $\lambda \in (0, 1)$ implies $\lim_{n \to +\infty} \lambda^n = 0$, the point $0$ is an accumulation point and belongs to the spectrum:

$$

\mathrm{Spec}(\Delta_{\Phi_\theta}) = \{0\} \cup \{\lambda^n : n \in \mathbb{Z}\} .

$$

3. **Invariance under change of state (Connes Cocycle):**
Why does this spectrum not depend on the reference vector $\ket{\Phi_\theta}$?
Let $\ket\Psi$ be any other cyclic and separating vector. By Connes' Radon—Nikodym theorem, the modular automorphism flows are related by a unitary cocycle $u_t \equiv (D\Psi : D\Phi_\theta)_t \in \M_\theta$:

$$

\sigma_t^\Psi(A) = u_t \,\sigma_t^{\Phi_\theta}(A)\, u_t^\dagger .

$$

Because $\M_\theta$ is an Infinite Tensor Product of Finite Factors (ITPFI, or Powers factor), any normal state $\Psi$ can be approximated in norm by perturbing $\Phi_\theta$ on only finitely many sites $1, \dots, K$. On the infinite tail $k > K$, the state remains identical to $\Phi_\theta$.
The modular operator therefore factorizes asymptotically as:

$$

\Delta_\Psi \sim \Delta_{\Psi,\text{local}} \otimes \bigotimes_{k=K+1}^\infty \delta_\theta^{(k)} .

$$

In Araki and Woods' asymptotic ratio set $\Gamma(\M_\theta)$, the infinite tail eigenvalues $\lambda^n$ dominate the spectrum, forcing the intersection over all cyclic-separating states to be invariant:

$$

S(\M_\theta) \equiv \bigcap_{\Psi} \mathrm{Spec}(\Delta_\Psi) = \{0\} \cup \{\lambda^n : n \in \mathbb{Z}\} = \{0\} \cup \lambda^{\mathbb{Z}} .

$$

Comparing with Connes' definition, this uniquely identifies $\M_\theta$ as a **type $\mathrm{III**_\lambda$} factor with $\lambda = \tan^2\theta$. $\blacksquare$

\end{keyresult}

This is eq.~4.39's spectrum for the *emph* reference vector $\ket{\Phi_\theta}$; the Connes invariant $S(\M_\theta)$ needs the intersection over *emph* cyclic-separating reference vector (eq.~4.27) — and the derivation above proves that this intersection in fact coincides exactly with eq.~4.39 for this example. Comparing directly to the three-way classification of Sec.~IV.B (eqs.~4.28—4.30): $\{0\}\cup\{\lambda^n\}$ with $\lambda=\tan^2\theta\in(0,1)$ is exactly the signature of **type $\mathrm{III**_\lambda$}. **So $\M_\theta$ is type $\mathrm{III**_{\tan^2\theta}$, for every $\theta\in(0,\pi/4)$} — different entangling angles genuinely produce different, inequivalent von Neumann algebra subtypes.

The other Connes invariant, $T(\M_\theta)$, can also be read off directly from eq.~4.38: $\Delta_{\Phi_\theta}
^{it}=1$ (i.e., the flow does nothing — is manifestly inner, trivially implemented by the identity) exactly
when $\lambda^{int}=1$ for every eigenvalue simultaneously, i.e., $t\log\lambda\in2\pi\mathbb Z$. This holds
for any finite $N$, and hence also in the $N\to\infty$ limit, giving (this can be shown to be exhaustive — no
other values of $t$ work)

$$

T(\M_\theta) = \left\{\frac{2\pi n}{\log\lambda} : n\in\mathbb Z\right\}, \qquad \lambda=\tan^2\theta

$$

(eqs.~4.40—4.41) — a discrete, measure-zero subset of $\mathbb R$, exactly as the general type III criterion
(Sec.~IV.B) demanded.

### The endpoints, and how to reach $\mathrm{III_0$ and $\mathrm{III}_1$ too}

Two special values of $\theta$ are worth explicitly reconciling with everything discussed so far. At
$\theta=\pi/4$: this was already established, in Sec.~III, to be type $\mathrm{II}_1$, not type III — and
indeed $\lambda=\tan^2(\pi/4)=1$ here, which sits right at the edge of the allowed range $\lambda\in(0,1)$ for
type $\mathrm{III}_\lambda$, consistent with this being a genuinely different (and, as shown in Sec.~III, more
tractable — trace-having) type. At $\theta=0$: the two spins in each pair are completely unentangled to begin
with, so the whole $N\to\infty$ construction never leaves ordinary type I at all — there's no entanglement to
generate anything new.

What about type $\mathrm{III}_0$ and type $\mathrm{III}_1$ — can they be reached from some variant of this
same family of examples? Yes, and seeing how is worth doing, because it shows the classification is genuinely
sensitive to fine details of *emph* the infinite limit is taken, not just to some single overall parameter.
Instead of using the same $\theta$ for every pair, let the $i$-th pair have its own angle $\theta_i$, so
$\lambda_i=\tan^2\theta_i$ can vary from pair to pair. Equation~4.38's eigenvalue formula generalizes to
$\prod_i\lambda_i^{\alpha_i}$ (eq.~4.42), and what happens in the $N\to\infty$ limit now depends on the
*emph* of the whole infinite sequence $\{\lambda_i\}$, not on any single number. A
mathematical result due to Araki and Woods pins this down completely: if $\lambda_1,\lambda_2,\dots$ converges
to some fixed $\lambda\in(0,1)$, you get type $\mathrm{III}_\lambda$ (the case just worked out, with every
$\lambda_i$ literally equal to the same constant being the simplest special case); if the sequence converges
to $0$ fast enough, you instead get an ordinary type $\mathrm{I}_\infty$ algebra (no genuinely new structure —
the entanglement dies off quickly enough that nothing new happens in the limit); if it converges to $0$ but
*emph* fast enough, you get type $\mathrm{III}_0$; and — this is the generic case, the one that happens
for essentially any "typical" (non-fine-tuned) choice of the sequence $\{\lambda_i\}$ that doesn't converge
to a single value at all — you get type $\mathrm{III}_1$, the "most chaotic" member of the family.

There's a second, independent way to manufacture type $\mathrm{III}_1$ directly, worth knowing because it will
resurface, in a completely different physical guise, when the Rindler wedge is discussed in the next
subsection: instead of qubits, use pairs of *emph* (spin-$1$ systems, three-dimensional instead of
two-dimensional) in a general entangled state, so the single-pair reduced density matrix is a $3\times3$
diagonal matrix $\rho_r=\tfrac{1}{1+\lambda+\tilde\lambda}\,\mathrm{diag}(1,\lambda,\tilde\lambda)$ for two
independent parameters $\lambda,\tilde\lambda>0$ (eq.~4.43). Now the $N\to\infty$ modular eigenvalues are all
products $\lambda^n\tilde\lambda^m$ for integers $n,m$ — and for *emph* (irrational-ratio) choices of
$\lambda,\tilde\lambda$, this two-parameter family of products becomes dense in *emph* of
$\mathbb R_{\ge0}$, giving $\sigma(\Delta_\Psi)=\mathbb R_{\ge0}=S(\M)$ directly — type $\mathrm{III}_1$ again,
reached this time not by varying $\theta_i$ pair-by-pair but by having two independent, incommensurate
"frequencies" $\log\lambda,\log\tilde\lambda$ built into a single repeated building block.

## Sec.~IV.D: local algebras in a relativistic quantum field theory

### Sec.~IV.D.1: the Rindler wedge, and why the modular flow is a boost

Now return to Ex.~3 of Sec.~I: cutting a relativistic quantum field theory in half by the surface $x=0$, in
$1{+}1$-dimensional Minkowski space with coordinates $(t,x)$. Sec.~I already established that the vacuum
state $\ket\Omega$ has infinite entanglement across this cut, so no tensor factorization exists. The way to
characterize this entanglement, in the language now available, is via the algebra $\M_R$ of operators
localized in the right region $R=\{x>0\}$.

One geometric fact is worth being explicit about, because it's used constantly from here on: in a relativistic
theory, time evolution is causal (nothing propagates faster than light), which means $\M_R$ — built from
operators localized at $x>0$ at a single instant — is actually equivalent to the algebra of operators
localized anywhere in the *emph* $\widehat R$ of that region (the notion from Sec.~I.B),
which for the half-line $x>0$ is exactly the **right Rindler wedge**, $\{(t,x): x>|t|\}$ — everything
that data on the initial slice $x>0$ completely determines, both to its future and its past. By causality,
$\M_R' = \M_L = \M_{\widehat L}$ — the commutant is exactly the algebra of the causally complementary (left)
wedge, with no gap between them.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.82\textwidth]{figs/fig_rindler.pdf}
\caption{The spacetime geometry of the Rindler wedge: Minkowski spacetime split into the Right wedge $R$ ($x > |t|$), Left wedge $L$ ($x < -|t|$), Future $F$, and Past $P$. The boost hyperbolae $x^2 - t^2 = \rho^2$ represent trajectories of uniformly accelerated observers with proper acceleration $a = 1/\rho$, whose proper time $\tau = \rho \eta$ is governed by the boost parameter $\eta$.}
\label{fig:rindler}
\end{figure}

The **Reeh—Schlieder theorem** — stated here and proved below — says: in a relativistic quantum field theory, acting on the vacuum $\ket\Omega$ with operators localized in *emph* open spacetime region (however small) produces a set of states that is dense in the entire Hilbert space.

\begin{keyresult}[: Derivation of the Reeh—Schlieder Theorem]
**Theorem:** Let $\mathcal{O} \subset \mathbb{R}^{1,d-1}$ be any nonempty open region in Minkowski spacetime, and let $\M(\mathcal{O})$ be the local von Neumann algebra generated by fields smeared with test functions supported in $\mathcal{O}$. In any relativistic QFT satisfying the Wightman axioms:

1. $\ket\Omega$ is **cyclic** for $\M(\mathcal{O})$: $\overline{\M(\mathcal{O})\ket\Omega} = \HH$.
2. $\ket\Omega$ is **separating** for $\M(\mathcal{O})$: $A\ket\Omega = 0 \implies A = 0$ for all $A \in \M(\mathcal{O})$.


**Proof:**

1. **Orthogonality hypothesis:**
To prove cyclicity, suppose there exists a state $\ket\chi \in \HH$ orthogonal to $\M(\mathcal{O})\ket\Omega$, so that:

$$

\braket{\chi | A | \Omega} = 0 \qquad \text{for all } A \in \M(\mathcal{O}) .

$$

Let $\phi(f_1)\cdots\phi(f_n)\ket\Omega$ be an arbitrary $n$-point field state with $\mathrm{supp}(f_j) \subset \mathcal{O}$.
Using spacetime translation covariance $\phi(x) = e^{i P_\mu x^\mu} \phi(0) e^{-i P_\mu x^\mu}$ and vacuum translation invariance $P_\mu\ket\Omega = 0$, define the correlator function:

$$

F(x_1, \dots, x_n) \equiv \braket{\chi | \phi(x_1)\phi(x_2)\cdots\phi(x_n)|\Omega} .

$$

2. **Relativistic spectral condition and holomorphy:**
Change to relative difference coordinates $\xi_j \equiv x_j - x_{j+1}$ ($j = 1, \dots, n-1$):

$$

F(\xi_1, \dots, \xi_{n-1}) = \Braket{\chi \Big| \phi(0) e^{-i P \cdot \xi_1} \phi(0) e^{-i P \cdot \xi_2} \cdots e^{-i P \cdot \xi_{n-1}} \phi(0) \Big| \Omega} .

$$

By the relativistic spectrum condition, the joint spectrum of the energy-momentum operator $P^\mu = (H, \vec P)$ lies entirely within the closed forward lightcone:

$$

\mathrm{Spec}(P^\mu) \subseteq \bar V^+ = \{p^\mu : p^0 \ge |\vec p| \ge 0\} .

$$

Now analytically continue the differences into the complex domain:

$$

\xi_j \longrightarrow \zeta_j = \xi_j - i \eta_j, \qquad \eta_j \in V^+ \quad (\eta_j^0 > |\vec \eta_j|) .

$$

Evaluating the operator exponential on any state with physical four-momentum $p \in \bar V^+$:

$$

-i P \cdot (\xi_j - i \eta_j) = -i P \cdot \xi_j - P \cdot \eta_j .

$$

Because both $p \in \bar V^+$ and $\eta_j \in V^+$, the Lorentzian inner product $p \cdot \eta_j = p^0 \eta_j^0 - \vec p \cdot \vec\eta_j > 0$ is strictly positive!
The factor $e^{-P \cdot \eta_j}$ provides uniform exponential damping, guaranteeing that the operator product is bounded and holomorphic for all $\eta_j \in V^+$.
Therefore, $F(\zeta_1, \dots, \zeta_{n-1})$ is holomorphic in the multidimensional forward tube domain $\mathcal{T}_{n-1} = (\mathbb{R}^d - i V^+)^{n-1}$.
3. **Edge-of-the-Wedge theorem and global vanishing:**
By assumption, when all $x_j \in \mathcal{O}$, the boundary value $F(x_1, \dots, x_n) = 0$.
The set $\mathcal{O}^n$ contains a nonempty open real ball. By the Edge-of-the-Wedge theorem (the multivariable generalization of the Schwarz reflection principle and identity theorem), if a holomorphic function in a tube domain has vanishing boundary values on an open real set, it must vanish *emph* throughout its entire domain of holomorphy:

$$

F(\zeta_1, \dots, \zeta_{n-1}) \equiv 0 \qquad \text{on } \mathcal{T}_{n-1} .

$$

Taking the boundary limit back to the real axis implies:

$$

\braket{\chi | \phi(x_1)\phi(x_2)\cdots\phi(x_n)|\Omega} = 0 \qquad \text{for *emph*} \ x_1, \dots, x_n \in \mathbb{R}^{1,d-1} .

$$

4. **Conclusion of Cyclicity:**
By the Wightman reconstruction axioms, polynomials of fields smeared over the entire spacetime generate a dense subspace of $\HH$. Since $\ket\chi$ is orthogonal to this dense subspace, $\ket\chi = 0$. Thus $\overline{\M(\mathcal{O})\ket\Omega} = \HH$, proving $\ket\Omega$ is **cyclic**.
5. **Separating property:**
Suppose $A \in \M(\mathcal{O})$ satisfies $A\ket\Omega = 0$.
Choose any nonempty open region $\mathcal{O}'$ in the spacelike complement of $\mathcal{O}$. By microcausality, $[A, B'] = 0$ for all $B' \in \M(\mathcal{O}')$.
Therefore:

$$

A \big(B'\ket\Omega\big) = B' \big(A\ket\Omega\big) = B'(0) = 0 .

$$

By cyclicity of $\M(\mathcal{O}')$ established in Step~4, vectors of the form $B'\ket\Omega$ are dense in $\HH$.
An operator vanishing on a dense subspace is identically zero: $A = 0$.
Hence $\ket\Omega$ is **separating** for $\M(\mathcal{O})$. $\blacksquare$

\end{keyresult}

Applied here, this guarantees $\ket\Omega$ is cyclic with respect to both $\M_R$ and $\M_L$, and hence — by the cyclic-separating duality established in Sec.~IV.A — cyclic *emph* separating with respect to $\M_R$ alone. So Tomita—Takesaki theory applies directly, with no further assumption needed.

Here is the genuinely striking physical fact, arrived at by using remark (d) from Sec.~IV.A above (find *emph* generator satisfying the KMS condition, and it must be *emph* modular operator, since uniqueness is guaranteed): the modular operator for $\M_R$ in the vacuum state turns out to be

$$

K_\Omega \equiv -\log\Delta_\Omega = 2\pi K

$$

(eq.~4.44), where $K$ is the ordinary **boost generator** — the same operator that generates Lorentz boosts in special relativity, an honest geometric symmetry of Minkowski space, with absolutely nothing abstract or algebraic about its definition. Justifying eq.~4.44 requires checking two things: (i) flows generated by $K$ are automorphisms of $\M_R$ — immediate, since a boost maps the Rindler wedge $\widehat R$ to itself; and (ii) correlators of boosted operators satisfy the KMS relation with $\beta=2\pi$.

\begin{workedexamplebox}[: Verification of the Bisognano—Wichmann KMS Condition]
**Goal:** Prove that the boost flow $\alpha_\eta(A) = e^{i K \eta} A e^{-i K \eta}$ satisfies the KMS condition at $\beta = 2\pi$ for any operators $A, B \in \M_R$:

$$

\braket{\Omega | A\,\alpha_{i 2\pi}(B) | \Omega} = \braket{\Omega | B A | \Omega} .

$$

**Calculation:**

1. **Rindler coordinates and Euclidean rotation:**
The right Rindler wedge $\widehat R = \{(t,x) : x > |t|\}$ is parametrized by proper distance $\rho > 0$ and boost parameter $\eta \in \mathbb{R}$:

$$

t = \rho \sinh\eta, \qquad x = \rho \cosh\eta .

$$

Under a boost by parameter $s$, the coordinates transform as $\eta \to \eta + s$.
Perform a Wick rotation to Euclidean time: $t_E \equiv i t$, $\eta_E \equiv -i \eta$. Then:

$$

t_E = \rho \sin\eta_E, \qquad x = \rho \cos\eta_E .

$$

The Euclidean Minkowski metric becomes:

$$

ds_E^2 = dt_E^2 + dx^2 + dx_\perp^2 = d\rho^2 + \rho^2 d\eta_E^2 + dx_\perp^2 .

$$

In the $(\rho, \eta_E)$ plane, these are standard polar coordinates where $\rho$ is the radius and $\eta_E$ is the polar angle!
2. **Regularity and Euclidean $2\pi$-periodicity:**
To avoid a conical deficit angle (singularity) at the horizon $\rho = 0$, the Euclidean angle $\eta_E$ must have period $2\pi$:

$$

\eta_E \sim \eta_E + 2\pi .

$$

Translating back to Lorentzian boost parameter $\eta = i \eta_E$, a rotation by $2\pi$ corresponds to an imaginary shift of the boost rapidity:

$$

\eta \longrightarrow \eta + 2\pi i .

$$

Geometrically, rotating $\eta_E$ by $\pi$ maps $(t_E, x) \to (-t_E, -x)$, sending an operator in the right wedge $R$ to the left wedge $L$. Rotating by $2\pi$ completes a full circle around the wedge bifurcation surface $\rho = 0$, returning to the right wedge.
3. **Path integral and operator ordering:**
In the Euclidean path integral representation of the vacuum state $\ket\Omega$, imaginary time evolution by $\eta_E$ inserts operators at angular positions around the Euclidean origin:

$$

\braket{\Omega | A \, e^{i K (\eta + 2\pi i)} B e^{-i K (\eta + 2\pi i)} | \Omega} = \braket{\Omega | \mathcal{T}_{\eta_E} \big[ A(\eta_E=0) B(\eta_E=2\pi) \big] | \Omega} .

$$

Because Euclidean time ordering places operators with larger $\eta_E$ to the left, and $2\pi$ wraps past the insertion at $\eta_E = 0$:

$$

\mathcal{T}_{\eta_E} \big[ A(0) B(2\pi) \big] = B(0) A(0) .

$$

Therefore:

$$

\Braket{\Omega \Big| A \big( e^{-2\pi K} B e^{2\pi K} \big) \Big| \Omega} = \braket{\Omega | B A | \Omega} .

$$

This is identically the KMS relation with inverse temperature $\beta = 2\pi$ with respect to the boost parameter $\eta$!
By Tomita—Takesaki uniqueness, the modular operator is uniquely identified as $\Delta_\Omega = e^{-2\pi K}$. $\blacksquare$

\end{workedexamplebox}

The physical translation of condition (ii) is exactly the **Unruh effect**, and it's worth spelling out
the geometry carefully, because "a Rindler observer" is not just a figure of speech. Writing the Minkowski
metric as $ds^2=-dt^2+dx^2=-\rho^2d\eta^2+d\rho^2$ (Rindler coordinates: $\rho$ is a radial-like coordinate,
$\eta$ a boost-angle-like coordinate), a trajectory of constant $\rho$ traces out a hyperbola in the $(t,x)$
plane — this is exactly the worldline of an observer undergoing constant proper acceleration $a=1/\rho$, and
$\eta$, the boost parameter, is proportional to that observer's own proper time, $d\tau=\rho\,d\eta$.
Condition (ii) says: observers using $\eta$ as their clock — i.e., *emph* — experience the ordinary Minkowski vacuum, which contains no particles at all as far as an
inertial observer is concerned, as a genuinely thermal bath, at temperature

$$

T_\rho = \frac{1}{2\pi\rho} = \frac{a}{2\pi} .

$$

This is Unruh's 1976 result, arrived at here as a direct, unavoidable consequence of Tomita—Takesaki theory
applied to the vacuum of a relativistic field, with the specific factor of $2\pi$ in eq.~4.44 being exactly
what converts the universal, dimensionless modular temperature $\beta=1$ into this specific, physical
temperature once $\eta$ is converted to the accelerated observer's own proper time $\tau$.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.78\textwidth]{figs/fig_unruh.pdf}
\caption{The Bisognano—Wichmann theorem and the Unruh effect: the modular flow $\sigma_t^\Omega(A) = \Delta_\Omega^{it} A \Delta_\Omega^{-it}$ acting on the right Rindler wedge $\M_R$ is geometrically equivalent to a Lorentz boost with parameter $\eta = 2\pi t$. Accelerated observers perceive the Minkowski vacuum as a thermal KMS state with local Unruh temperature $T(x) = \hbar c / (2\pi k_B x)$.}
\label{fig:unruh}
\end{figure}

The boost generator $K$ has purely continuous spectrum, all of $(-\infty,\infty)$ (it's the generator of an
honest noncompact symmetry — there's no smallest nonzero boost, and boosts of arbitrarily large rapidity all
exist), so $\Delta_\Omega=e^{-2\pi K}$ has spectrum all of $\mathbb R_{\ge0}$ — and it can be shown that
$S(\M_R)$ coincides with this spectrum, giving (by the classification of Sec.~IV.B) **$\M_R$ is type
$\mathrm{III**_1$}. The modular conjugation $J_\Omega$ turns out to be exactly $CRT$ — charge conjugation,
combined with a spatial reflection and time reversal — meaning Tomita—Takesaki theory, applied to a
relativistic vacuum, reconstructs the celebrated CPT theorem directly out of nothing but the algebra and the
vacuum state, with no separate argument needed.

This entire story generalizes immediately to higher spacetime dimensions (any transverse directions just ride
along unaffected, since the boost only acts in the $t$-$x$ plane), and — this is the deeper point, worth
holding onto — it generalizes to a *emph* open region $O$ on a Cauchy slice, not just the special case
of a half-space. Reeh—Schlieder guarantees $\ket\Omega$ is still cyclic and separating for $\M_O$, so
Tomita—Takesaki theory applies; the modular operator can no longer, in general, be written down in closed
form (it depends on the precise theory and the precise shape of $O$), but a scale-invariance argument (valid
whenever the theory has a scale-invariant UV fixed point — true of essentially any interacting quantum field
theory taken to short enough distances) still pins down its type. The argument: right near the boundary
$\Sigma_O$ of the region $O$, that boundary looks, at short enough distances, just like a flat plane — locally
indistinguishable from the Rindler-wedge geometry just worked out — so

$$

-\log\Delta_\Omega \approx 2\pi K, \qquad \text{very close to } \Sigma_O ,

$$

(eq.~4.46) with $K$ now the boost that locally leaves $\Sigma_O$ fixed, forcing the same continuous spectrum
$\mathbb R_{\ge0}$ and hence, again, type $\mathrm{III}_1$. **The type $\mathrm{III**_1$ nature of every
local algebra in a relativistic quantum field theory can be traced directly to this local Rindler structure
near any entangling surface, which in turn is a direct consequence of relativistic causal structure itself} —
this is the precise sense in which ``the causal structure of a relativistic QFT requires type
$\mathrm{III}_1$,'' and correspondingly, a *emph*-relativistic field theory (with no light-cone structure
forcing this local Rindler behavior near any cut) need not have type $\mathrm{III}_1$ local algebras at all.

### Sec.~IV.D.2: the split property

The heuristic picture from Sec.~I — that non-factorization and type III structure come from infinite
entanglement concentrated among short-distance degrees of freedom right at the boundary of a region — can be
made completely precise, and it's worth seeing the precise version, because it resolves what might otherwise
look like a contradiction: how can two regions be infinitely entangled (type III, no factorization) and yet,
intuitively, "mostly independent" once you're not sitting exactly on the shared boundary?

Separate $R$ and $L$ by a small but nonzero buffer distance $\epsilon_b$ (so there's a thin strip $I_\epsilon$
of "no man's land" between them). The **split property** states that there *emph* a genuine tensor
factorization $\HH=\HH_1\otimes\HH_2$, with

$$

\M_R \subset B(\HH_1)\otimes\id_{\HH_2} \subset \M_L' = \M_{R_\epsilon}, \qquad
\M_L \subset \id_{\HH_1}\otimes B(\HH_2) \subset \M_R' = \M_{L_\epsilon}

$$

(eq.~4.47, where $R_\epsilon\equiv R\cup I_\epsilon$, similarly $L_\epsilon$) — a genuine type I factor,
$B(\HH_1)\otimes\id_{\HH_2}$, sandwiched in between the two type $\mathrm{III}_1$ algebras $\M_R$ and
$\M_{R_\epsilon}$. This says something with real physical bite: once $R$ and $L$ are separated by *emph*
nonzero distance, however small, they *emph* be completely disentangled — there exist genuine, honest
product states with respect to the factors $\HH_1,\HH_2$, on which $\M_R$ and $\M_L$ act purely separately.
The entanglement obstruction from Sec.~I, in other words, is a purely short-distance, boundary-localized
phenomenon; it evaporates completely the instant you step back even an infinitesimal amount from the shared
edge. More generally, for any two regions $O_1\subset O_2$ whose boundaries don't actually touch (the closure
of $O_1$ sits strictly inside the interior of $O_2$), the split property guarantees a genuine type I factor
$\N$ with $\M_{O_1}\subset\N\subset\M_{O_2}$ (eq.~4.48) — a type I "buffer" can always be inserted, as long
as there's any geometric gap at all to insert it into.

The split property is not an extra assumption pulled from nowhere; it can be shown to follow from a technical
condition called the *emph* — a statement about how quickly the theory's energy density
grows at high energies — believed to hold for any "reasonable" relativistic QFT. Given the split property,
it can further be shown that $\M_O$, for an open region $O$, is not just type $\mathrm{III}_1$ but also
**hyperfinite**: it can be built as the weak closure of an increasing sequence of ordinary,
finite-dimensional matrix algebras (exactly the kind of construction used throughout this companion — bigger
and bigger, but always finite, matrices, taken to a limit). A deep uniqueness theorem then applies: hyperfinite
type $\mathrm{III}_1$ von Neumann algebras are, up to isomorphism, all the *emph* algebra. The striking
consequence: **the local algebra of any region in any "reasonable" relativistic QFT — free or
interacting, weakly or strongly coupled, any spacetime dimension — is abstractly isomorphic to the local
algebra of any other region in any other such theory.** Different theories are distinguished not by what their
local algebras *emph* (abstractly, they're all the same object), but by how those algebras sit relative to
one another — which operators are shared between overlapping regions, how correlators between distant regions
behave, and so on. This is a genuinely surprising, almost counter-intuitive statement, and it's stated here
exactly as strongly as the paper states it, because it's one of the cleanest illustrations of how much
structure the type classification alone captures, and how much it deliberately does *emph* capture (the
dynamics, which lives entirely in the relations between algebras, not in any single algebra's abstract type).

Two further, related consequences are worth walking through, because the first comes with an actual proof
sketch worth seeing, and the second is one of the more startling facts in the whole paper.

**Strong local preparability.** Take the setup of Fig.~5 (regions $R,L$ split by a buffer $I_\epsilon$).
For a general state $\omega$, there's generally a genuine correlation between $R$ and $L$-operators,
$\omega(AB)\ne\omega(A)\omega(B)$ for $A\in\M_R,B\in\M_L$ (eq.~4.49) — nothing surprising there. The startling
claim: using an operation $W$ supported only in the slightly enlarged region $R_\epsilon$ (not $R$ itself, but
$R$ plus the thin buffer strip), it is possible to build a *emph* state $\omega_W$ that (i) has
*emph* correlation between $\M_R$ and $\M_L$ at all, and (ii) matches some arbitrarily chosen target
state $\phi$ exactly on $\M_R$, while leaving the state on $\M_L$ completely unchanged from the original
$\omega$ (eqs.~4.50—4.51). This sounds like it should be nearly impossible — locally erase all correlation
with a distant system while simultaneously re-preparing your own region into any state you like, without
touching the distant system at all — and yet it follows in a few lines from the split property and the type
III structure. Here is the argument, worth seeing because it's short: by the split property, $\M_R\subset
B(\HH_1)$, so there's a vector $\ket\xi\in\HH_1$ representing the target state, $\phi(A)=\braket{\xi|A|\xi}$
(justified more carefully in Sec.~IV.G below). The projection $P_\xi=\ket\xi\rangle\langle\xi|\otimes
\id_{\HH_2}$ lies in $\M_{R_\epsilon}$; since $\M_{R_\epsilon}$ is type III, *emph* nonzero projection in
it is equivalent to the identity (Sec.~II.B.5's finiteness discussion, pushed to its extreme: in type III,
nothing is finite, so everything is as "big" as the whole algebra) — so there's an isometry $W\in
\M_{R_\epsilon}$ with $WW^\dagger=P_\xi$, $W^\dagger W=\id$. Because $W\in\M_{R_\epsilon}\subset\M_L'$, it
commutes with everything in $\M_L$, so $\omega_W(B)\equiv\omega(W^\dagger BW)=\omega(B)$ for $B\in\M_L$
(eq.~4.51) — the $L$-side is untouched, exactly as claimed. And a short algebraic manipulation using
$P_\xi AP_\xi=\phi(A)P_\xi$ (immediate from $\ket\xi$ representing $\phi$) gives $W^\dagger AW=\phi(A)\id$
(eq.~4.52), from which $\omega(W^\dagger ABW)=\phi(A)\omega(B)$ follows directly (eq.~4.53) — exactly the
claimed factorized, re-prepared state.

**The Connes—St\o rmer transitivity theorem.** For a type $\mathrm{III}_1$ factor, *emph* two states
$\phi,\omega$ can be connected to arbitrary precision $\epsilon>0$ by a unitary $W$ *emph*, $\|\phi-\omega_W\|<\epsilon$ (eq.~4.54). In words: every state can be prepared, locally, to
arbitrary accuracy, starting from any other state — a statement of ergodicity so strong it's fair to call the
resulting state space *emph*: no state is structurally special or hard to reach from any other,
in sharp contrast to a type I algebra with a nontrivial center, where different superselection sectors are, by
definition, mutually unreachable by anything in the algebra.

### Sec.~IV.D.3: the collection of algebras $\{\M(O)\$, and Haag duality}

One closing structural point, worth having on hand because it resurfaces directly in Sec.~VII: the full
collection of local algebras $\{\M(O)\}$, one for every open spacetime region $O$, is expected to satisfy
several basic consistency relations, each one a direct algebraic translation of an ordinary physical
principle. **Isotony**, $\M(O_1)\subseteq\M(O_2)$ for $O_1\subseteq O_2$ (eq.~4.55): a bigger region
gives access to at least as many operations as a smaller one it contains — this is almost definitional.
**The time-slice axiom**, $\M(O)=\M(\widehat O)$ (eq.~4.56): because the equations of motion are causal,
operators anywhere in the domain of dependence $\widehat O$ can be re-expressed, via time evolution, in terms
of operators in $O$ itself — so knowing the algebra on a single Cauchy slice already determines it everywhere.
**Locality (commutativity)**, $\M(O')\subseteq\M(O)'$ (eq.~4.57): operators in the causal complement
$O'$ (spacelike separated from all of $O$) commute with everything in $\M(O)$ — the operator-algebra statement
of ordinary microcausality. When this last relation holds with *emph*, $\M(O')=\M(O)'$, it's called
**Haag duality** (eq.~4.58) — a strictly stronger statement, saying that literally *emph* operator
commuting with $\M(O)$ is already accounted for by the causal complement, with nothing extra hiding outside
that count. Haag duality is not automatic (it can fail for topologically nontrivial regions), but is expected
to hold quite generally for the vacuum sector of an ordinary relativistic QFT on topologically simple regions.
Two further relations — **additivity**, $\M(O_1\cup O_2)=\M(O_1)\vee\M(O_2)$ (eq.~4.60: no "extra,"
genuinely nonlocal operators hide in a union that aren't already built from the pieces), and the resulting
**intersection property**, $\M(O_1\cap O_2)=\M(O_1)\cap\M(O_2)$ (eq.~4.61, which follows from combining
Haag duality and additivity via a short commutant manipulation, eqs.~4.62—4.63) — round out the full package.
A theory satisfying all of these, for every region (not just topologically trivial ones), is called
"complete." These relations are worth having memorized in outline, not for their own sake, but because
Sec.~VII builds subregion-subalgebra duality directly on top of exactly this dictionary, translated to the
boundary theory of AdS/CFT.

## Sec.~IV.E: emergent times from subalgebras — half-sided modular inclusion

This subsection introduces a second, genuinely distinct notion of emergent time — one that comes not from a
single algebra's own modular flow, but from the relationship between an algebra and a carefully chosen
subalgebra of it. It is a unique feature of type $\mathrm{III}_1$ algebras specifically, and it is exactly the
mechanism, picked up again in Sec.~VII, that lets a single band of boundary time generate the entire interior
of an emergent black-hole horizon.

### A new, positive "Hamiltonian" $G$

Let $\M$ be a von Neumann algebra with cyclic-separating vector $\ket\Omega$, modular data $\Delta_\M=
e^{-K_\M}$, $J_\M$, as in Sec.~IV.A. Now suppose $\N\subset\M$ is a genuine subalgebra, and $\ket\Omega$
happens to *emph* be cyclic for $\N$ (automatically separating too, since $\N\subset\M$ and $\ket\Omega$
is already separating for the bigger algebra $\M$). $\N$ inherits its own modular data, $\Delta_\N=e^{-K_\N}$,
$J_\N$, with respect to the same $\ket\Omega$.

Here is the first new structural fact, and it's worth seeing the one-line reason it's true: because $\N\subset
\M$, the Tomita operator $S_\M$ (built from $\M$ and $\ket\Omega$) is literally an extension of $S_\N$ (built
from the smaller algebra $\N$ and the same $\ket\Omega$) — $S_\M$ agrees with $S_\N$ everywhere $S_\N$ is
defined, but is also defined on the larger domain $\M\ket\Omega\supseteq\N\ket\Omega$. A general fact about
unbounded operators (extending an operator can only make $X^\dagger X$ bigger, never smaller, in the operator
ordering sense) then gives $\Delta_\N\ge\Delta_\M$ (eq.~4.64), i.e., using $-\log$ (which reverses
inequalities for positive operators), $K_\M\ge K_\N$. Define

$$

G \equiv \frac{1}{2\pi}(K_\M-K_\N) \ \ge 0, \qquad G\ket\Omega=0

$$

(eq.~4.65 — the $2\pi$ is just a convenient normalization chosen for what follows; $G\ket\Omega=0$ follows
because both $K_\M$ and $K_\N$ individually annihilate $\ket\Omega$, eq.~4.9 applied to each). $G$ is a
genuinely positive operator, so it deserves to be called a Hamiltonian, and the flow $e^{iGs}$ it generates is
a legitimate new notion of "time" — a second one, distinct from either $\M$'s own modular flow or $\N$'s —
that also happens to leave the reference vector $\ket\Omega$ fixed.

### The half-sided modular inclusion condition, and what it buys you

Everything so far works for *emph* subalgebra $\N\subset\M$ sharing a cyclic-separating vector. Something
much stronger becomes available if $\N$ satisfies one additional geometric-looking condition, called
**half-sided modular inclusion**:

$$

\N_t \equiv \Delta_\M^{-it}\N\Delta_\M^{it} \subset \N, \qquad \text{for every } t\le0

$$

(eq.~4.81) — flowing $\N$ by $\M$'s *emph* modular flow, for negative modular time, always shrinks $\N$
(or leaves it the same), never grows it. When this holds, a theorem (due to Wiesbrock and, independently,
Borchers, building on earlier work) establishes three remarkable consequences at once, none of them assumed —
all derived purely from eq.~4.81:


1. $K_\M$ and $K_\N$ satisfy the commutation relations of a genuine **two-dimensional conformal
(M\"obius) algebra** together with $G$:

$$

[K_\M,K_\N] = -4\pi^2i\,G , \qquad [K_\M,G] = 2\pi i\,G

$$

(eq.~4.82, with a companion relation for the modular conjugations, eq.~4.83) — an entire, recognizable piece
of two-dimensional conformal symmetry, produced out of nothing but one algebraic inclusion condition on two
von Neumann algebras.
2. The flow generated by $G$ moves $\M$ into itself for one whole half of the time axis: $e^{iGs}\M
e^{-iGs}\subset\M$ for $s<0$ (eq.~4.84), and in particular $\N=e^{-iG}\M e^{iG}$ (eq.~4.85) — $\N$ is exactly
the image of $\M$ under one unit of this new, $G$-generated time translation. Running $G$ continuously
produces a whole nested, continuously-parametrized family $\N_t\equiv e^{-iGt}\M e^{iGt}$, with $\N_{t_1}
\subset\N_{t_2}\subset\M$ for $t_1<t_2$ and $\N_\infty=\M$ (eqs.~4.89—4.90) — genuinely new time translation,
distinct from $\M$'s own modular flow, acting purely by relating the algebra to smaller and smaller versions
of itself.
3. **$\M$ must be type $\mathrm{III**_1$.} Half-sided modular inclusion is not just a convenient
technical condition — its very existence forces the ambient algebra to be the "most chaotic" type
identified back in Sec.~IV.B.

(The paper builds several further technical objects along the way to this theorem — unitaries $D(t)=\Delta_\M
^{-it}\Delta_\N^{it}$, $V=J_\M J_\N$, and a chain of nested algebras built by repeatedly conjugating with $V$,
eqs.~4.66—4.80 — used to actually *emph* the theorem and to establish that this half-sided-inclusion
structure, once it exists, is completely unique. These are genuine, careful pieces of functional analysis;
they're flagged here so the notation isn't a surprise if you look at the original, but the three numbered
consequences above are the physical content that matters for everything downstream.)

### The concrete example: light-cone translations in the Rindler wedge

Here is the worked example the paper gives, and it's worth working through fully, because it turns the
abstract theorem above into something you can literally picture. Take $\M$ to be the algebra of the right
Rindler wedge $\widehat R$ from Sec.~IV.D.1, and let $\N$ be the algebra of the smaller region $\{x^+>0,\,
x^-<-1\}$ (using light-cone coordinates $x^\pm=x^0\pm x^1$) — a wedge-shaped region nested strictly inside
$\widehat R$, shifted over by one unit along the $x^-$ direction (Fig.~6, left panel). Using $K_\M=2\pi K$
(the boost generator, eq.~4.44) to flow $\N$: because a boost acts on light-cone coordinates by simple
rescaling, $x^\pm\to e^{\mp\eta}x^\pm$, flowing the defining condition $x^->-1$ for time $t$ using
$e^{iK_\M t}=e^{2\pi iKt}$ turns it into $x^->-e^{-2\pi t}$ — so

$$

\N_t \equiv e^{iK_\M t}\N e^{-iK_\M t} = \text{algebra of the region } \{x^+>0,\,x^-<-e^{-2\pi t}\}

$$

(eq.~4.95), and since $e^{-2\pi t}>1$ for $t<0$, this region is genuinely *emph* than the original
$\N$ (it requires $x^-$ to be even more negative) — exactly $\N_t\subset\N$ for $t<0$, precisely the
half-sided modular inclusion condition, verified directly on an explicit geometric example rather than just
asserted abstractly.

Identifying $G$ explicitly here is a short computation using the ordinary Poincar\'e algebra you already know
from special relativity: writing $P^\pm=\tfrac12(P^0\pm P^1)$ for the light-cone components of the momentum
(energy-momentum) operator, the standard commutation relation between the boost generator and momentum,
$[K,P^\pm]=\pm iP^\pm$ (eq.~4.97 — this is just the ordinary statement that a boost rescales energy and
momentum, exactly the way it rescales light-cone coordinates), combined with the definition of $K_\N$ via a
translation of $K_\M$ by the fixed point $a^\mu=(0,-1)$ of $\N$'s own boost symmetry (eq.~4.96), gives directly

$$

K_\N = K_\M - 2\pi P^+ \qquad \Longrightarrow \qquad G = P^+

$$

(eqs.~4.98—4.99, using the definition $G=\tfrac1{2\pi}(K_\M-K_\N)$ from eq.~4.65). **So in this example,
the abstract "positive Hamiltonian" $G$ is nothing more exotic than the ordinary light-cone momentum
operator $P^+$, and the abstract new "time flow" it generates is nothing more exotic than ordinary
translation in the $x^-$ direction.** Every one of the general statements 1—3 above (the conformal algebra,
the half-sided translation structure, the forced type $\mathrm{III}_1$ conclusion) can be checked directly on
this example using nothing but ordinary special-relativistic kinematics — and this is exactly the mechanism
that Sec.~VIII will reuse, essentially verbatim, to show that a single band of *emph* time in
AdS/CFT can generate the entire interior of an emergent black-hole horizon: the interior turns out to be built
by exactly this kind of half-sided-modular-inclusion light-cone translation, with $G$ playing the role of a
genuine, positive bulk momentum.

(One further variant, quickly: taking $\N$ to instead be the region in Fig.~6's right panel gives a half-sided
inclusion on the *emph* $t$-axis instead, $\N_t\subset\N$ for $t\ge0$ eq.~4.92, with correspondingly
sign-flipped relations eq.~4.93—4.94, and a modular translation generator $G=P^-$ instead of $P^+$ — the
mirror-image construction, translating in $x^+$ instead of $x^-$.)

## Sec.~IV.F: relative modular flows and relative entropy

Everything in this subsection is a direct generalization of the material already met in Sec.~I (relative
entropy $S(\rho\|\sigma)$) and Sec.~IV.A (the Tomita operator $S_\Psi$) to a version involving *emph*
different reference states $\ket\Psi,\ket\Omega$ at once, both cyclic and separating for the same $\M$. The
goal, worth keeping in view through the machinery: produce a version of relative entropy that survives even
when $\M$ is type III (where, as emphasized since Sec.~III, ordinary entropy $S_\M$ cannot be defined at all).

Define a **relative Tomita operator** exactly analogously to before, but now mapping between the two
reference vectors:

$$

S_{\Psi\Omega}A\ket\Omega = A^\dagger\ket\Psi\ \ (A\in\M), \qquad
S_{\Psi\Omega}A'\ket\Omega = A'^\dagger\ket\Psi\ \ (A'\in\M')

$$

(eq.~4.100), with polar decomposition $S_{\Psi\Omega}=J_{\Psi\Omega}\Delta_{\Psi\Omega}^{1/2}$ (eq.~4.102)
defining the **relative modular operator** $\Delta_{\Psi\Omega}\ge0$ and **relative modular
conjugation** $J_{\Psi\Omega}$, exactly the way the ordinary versions were built in Sec.~IV.A, but now
genuinely mixing the two states. (A short algebraic identity, $S_{\Psi\Omega}S_{\Omega\Psi}=\id$, eq.~4.101,
following directly from the definition, forces a relation $J_{\Psi\Omega}=J_{\Omega\Psi}^\dagger$ and
$J_{\Psi\Omega}\Delta_{\Psi\Omega}J_{\Psi\Omega}=\Delta_{\Omega\Psi}^{-1}$, eqs.~4.103—4.104 — a genuine
consistency check, worked out from the polar-decomposition uniqueness, but not needed for what follows.) There
is a two-state generalization of the KMS relation,

$$

\braket{\Psi|AB|\Psi} = \braket{\Omega|B\,\Delta_{\Psi\Omega}\,A|\Omega}, \qquad A,B\in\M

$$

(eq.~4.105, whose short proof, eq.~4.106, is just unpacking the definition of $S_{\Psi\Omega}$ on both
sides) — this single relation lets you convert correlation functions computed in one state, $\ket\Psi$,
directly into correlation functions computed in the other, $\ket\Omega$, and vice versa: genuinely useful
machinery, used freely later without re-derivation whenever the paper needs to compare correlators across two
different reference states.

The flow generated by $\Delta_{\Psi\Omega}$ can be shown to coincide, on $\M$, with the flow generated by the
ordinary (single-state) $\Delta_\Psi$, and on $\M'$ with the flow generated by $\Delta_\Omega$ (eqs.~4.107—
4.108) — and a further intertwining unitary $u_{\Omega\Psi}(s)\equiv\Delta_{\Omega\Phi}^{-is}\Delta_{\Psi\Phi}
^{is}$ (eq.~4.109, built using a third, auxiliary reference $\ket\Phi$, but shown to not actually depend on
which $\Phi$ was used) gives an *emph* of the inner automorphism relating $\sigma_s^\Psi$
and $\sigma_s^\Omega$ promised back in eq.~4.23 of Sec.~IV.B — closing a loop left open there. (A further
family of identities, eqs.~4.110—4.116, work out consistency relations and alternative expressions for these
intertwiners; they are used as technical machinery later and are not reproduced here.)

### The payoff: relative entropy for type III, and a genuine positivity proof

Here, finally, is the object that survives everything: for a type III algebra $\M$, no entropy $S_\M(\Omega)$
can be assigned to a single state $\Omega$ — but a **relative** entropy between two states can be, using
the relative modular operator just constructed:

$$

S_\M(\Psi\|\Omega) \equiv -\braket{\Psi|\log\Delta_{\Omega\Psi}|\Psi} .

$$

(eq.~4.117.) When $\M$ does have a trace (type I or II, with $\Delta_{\Omega\Psi}=\rho_\Omega\rho_\Psi'^{-1}$
in terms of density operators, eq.~4.118), this reduces exactly to the familiar formula

$$

S_\M(\Psi\|\Omega) = \tr(\rho_\Psi\log\rho_\Psi) - \tr(\rho_\Psi\log\rho_\Omega)

$$

(eq.~4.119, matching eq.~1.8 of Sec.~I of this companion) — but eq.~4.117 itself needs no trace to be
well-defined, and survives, completely intact, into type III.

It's worth seeing the positivity of this relative entropy actually proved, rather than just asserted, since it
is short and genuinely instructive: using the elementary calculus inequality $\log x\le x-1$ (true for every
positive real $x$, with equality only at $x=1$ — a fact you can check by noting $f(x)=x-1-\log x$ has
$f(1)=0$ and $f'(x)=1-1/x$, which is negative for $x<1$ and positive for $x>1$, so $x=1$ is the unique global
minimum of $f$, where $f=0$),

$$

-\braket{\Psi|\log\Delta_{\Omega\Psi}|\Psi} \ \ge\ \braket{\Psi|1-\Delta_{\Omega\Psi}|\Psi}
\ =\ -\braket{\Psi|\Psi} + \braket{\Omega|\Omega} \ =\ 0

$$

(eq.~4.120), where the middle equality uses the two-state KMS relation (eq.~4.105) applied with $A=B=\id$, and
the final equality is just $\braket{\Psi|\Psi}=\braket{\Omega|\Omega}=1$ (both are normalized states). So
$S_\M(\Psi\|\Omega)\ge0$ always — the relative entropy is never negative — proved here using nothing beyond
one calculus inequality and the KMS relation already established. This non-negativity is worth contrasting
directly with Sec.~III's finding that the ordinary (non-relative) entropy $S_\M$, in a type II algebra, could
come out negative: relative entropy is the more robust, better-behaved object precisely because it's always
measuring distinguishability from a fixed, explicit reference, never trying to count states from some absolute
zero that a type II or III algebra simply doesn't have.

## Sec.~IV.G: a canonical purification — the natural cone

This closing, more technical subsection answers a question that was quietly used without justification in the
strong-local-preparability proof above (Sec.~IV.D.2): given a state $\omega$ on $\M$, is there a
*emph* choice of purifying vector $\ket\xi\in\HH$ with $\omega(A)=\braket{\xi|A|\xi}$ — and can it
always be chosen to represent a genuine (not just formal) vector?

In general there can be infinitely many different purifying vectors for the same $\omega$ (a simple type I
example: for $\M=B(\HH_1)\otimes\id_{\HH_2}$, any vector in $\HH_1\otimes\HH_2$ that reduces to the right
density matrix on $\HH_1$ works, pure or mixed, and there's no reason to prefer one over another in general).
But if $\HH$ happens to contain *emph* cyclic-separating vector for $\M$ at all (a condition called being
in **standard form** — satisfied, for instance, whenever $\M=\M_O$ for an open region $O$ in the vacuum
sector of a relativistic QFT, courtesy of Reeh—Schlieder, and satisfied automatically by any GNS
representation built from a faithful state, Sec.~II.D), then a genuinely canonical purifying vector
$\ket{\xi_\omega}$ exists (eq.~4.121).

It's constructed as follows: given a fixed cyclic-separating reference $\ket\Omega$, define the **natural
cone** $P_\Omega$ as the closure of the set $\{Aj_\Omega(A)\ket\Omega : A\in\M\}$, where $j_\Omega(A)\equiv
J_\Omega AJ_\Omega$ (eq.~4.122; an equivalent description, eq.~4.123, is the closure of
$\{\Delta_\Omega^{1/4}A^\dagger A\ket\Omega : A\in\M\}$). Every normal state $\omega$ on $\M$ then has a
*emph* representative vector inside $P_\Omega$ — this is the canonical purification. (It depends on the
choice of $\Omega$ used to build the cone in the first place; a different reference vector gives, in general,
a different natural cone and hence a different canonical purification of the same $\omega$.)

The paper lists several further technical properties of vectors in the natural cone (eqs.~4.124—4.134) — that
inner products between any two vectors in $P_\Omega$ are automatically real and non-negative (eq.~4.126, the
property actually used in the strong-local-preparability argument above, and the one worth remembering); a
decomposition property for vectors fixed by $J_\Omega$ (eq.~4.127); a distance bound relating the vector-space
distance between two purifications to the more abstract distance between the two states they represent
(eq.~4.128); the fact that any two different cyclic-separating vectors within the same natural cone share
*emph* of their modular data — the same $J$, the same cone (eqs.~4.129—4.131); how to handle a
cyclic-separating vector that sits *emph* the natural cone, by relating it back with an explicit
unitary correction (eq.~4.132); and the fact that every automorphism of $\M$ can be implemented by a unitary
chosen to preserve the natural cone (eqs.~4.133—4.134). These are the technical tools that make later,
more advanced arguments in the paper watertight; the property that actually matters for the physical content
of this companion is the existence-and-uniqueness statement itself (eq.~4.121) and the positivity property
(eq.~4.126) — both used explicitly already, above.

\bigskip
\noindent This closes Sec.~IV, and with it, every tool needed to talk about entanglement for *emph* type
of von Neumann algebra — I, II, and now III. Section~V picks up exactly where remark (f) of Sec.~IV.A left
off: type III has no trace and hence no entropy of its own, which is a real problem if the goal is ever to
compute something like a black-hole entropy using this machinery. The **crossed product**, introduced
next, is the construction that fixes this — by literally attaching an auxiliary quantum system (a clock) to a
type III algebra and turning it into a type II algebra, which *emph* have a trace.



---

# Sec.~V: Crossed product by modular group

Section~IV ended on a genuinely uncomfortable note: type III algebras have no trace, so there is no density
operator and no entropy for them at all — not even the signed, relative-to-a-reference kind that rescued type
II in Sec.~III. If the eventual goal is to compute something like a black-hole entropy using nothing but
operator algebra, this is a real obstruction, not a cosmetic one. The **crossed product** is the
construction that removes it — not by cheating around the no-trace theorem, but by building a genuinely
*emph* algebra, out of the original type III one, that turns out to always be type II (which
does have a trace). The mechanism, remarkably, is completely mechanical and general-purpose, and it will
reappear, essentially unchanged, as the actual physical mechanism behind gravitational entropy starting in
Sec.~IX.

## Sec.~V, opening: crossed products in general

Here is the general-purpose construction, stated first without any reference to modular theory at all, because
it's a standard piece of operator-algebra machinery on its own, and it's worth seeing that the specific
application to modular flow (the one this paper actually needs) is just one instance of it. Suppose a group
$G$ acts on a von Neumann algebra $\M$ by unitaries, $\alpha_g(A)=U_gAU_g^\dagger$ (eq.~5.1) — some
one-parameter (or more general) family of symmetries of $\M$. Given the triple $(\M,G,\alpha)$, there is a
standard construction, called the **crossed product** $\widehat\M\equiv\M\rtimes_\alpha G$, that builds a
*emph* von Neumann algebra acting on the enlarged Hilbert space $\widehat\HH=\HH\otimes L^2(G)$ (functions
on $G$, valued in $\HH$ — think of it as attaching an auxiliary quantum system whose configuration space is
$G$ itself). For the case of interest here, $G=\mathbb R$ with generator $K$ and action $\alpha_t(A)=
e^{iKt}Ae^{-iKt}$ (eq.~5.2), so $\widehat\HH=\HH\otimes L^2(\mathbb R)$ — an auxiliary particle on a line.

The specific case this paper needs, and the only one used from here on, takes $K=-\log\Delta_\Psi$ — the
*emph* generator of $\M$ itself, for some cyclic-separating $\ket\Psi$ — so that eq.~5.2 is exactly
the modular flow $\sigma_t$ already built in Sec.~IV. The headline result, proved step by step below: for a
type III algebra $\M$, the resulting crossed product $\widehat\M$ is **always type II** — regardless of
which type III subtype $\M$ started as. This immediately buys back everything Sec.~III's machinery (density
operators, entropy) needs, applied now to $\widehat\M$ instead of $\M$ itself. And — a fact worth flagging
immediately, even though it's only fully justified at the end of Sec.~V.B — $\widehat\M$ turns out to depend
only on the algebra $\M$, not on which reference state $\ket\Psi$ was used to build the modular flow that
crossed it — so this is really a construction *emph* to $\M$, not an artifact of an arbitrary
choice. This is also, as flagged already back in Sec.~I, exactly the mechanism used in Sec.~IX to explain
black-hole and de~Sitter entropy: there, $\hat q$ below will literally be a physical observer's clock Hamiltonian.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.88\textwidth]{figs/fig_crossed.pdf}
\caption{The crossed product construction: crossing a Type $\mathrm{III}_1$ algebra $\M$ (which has no trace) with its modular automorphism group $\sigma_s = \Delta_\Psi^{-is} \cdot \Delta_\Psi^{is}$ via an auxiliary quantum observer clock $L^2(\mathbb{R})$ generates a Type $\mathrm{II}_\infty$ factor $\widehat\M = \M \rtimes_\sigma \mathbb{R}$. The resulting algebra supports a well-defined trace $\tau$, density matrices, and finite generalized entropy $S_{\rm gen}$.}
\label{fig:crossed_product}
\end{figure}

## Sec.~V.A: construction of $\widehat\M$

Attach a genuine one-dimensional quantum system — a particle on a line, with position $\hat q$ and momentum
$\hat p$ satisfying the ordinary canonical commutation relation $[\hat q,\hat p]=i$ (eq.~5.3) — to the original
system, giving the enlarged Hilbert space $\HH\otimes L^2(\mathbb R)$. Define the single operator

$$

C \equiv K+\hat q

$$

(eq.~5.4), and let $\widehat\M$ be the subalgebra of $\M\otimes B(L^2(\mathbb R))$ consisting of everything
that commutes with $C$: $a\in\widehat\M$ iff $[a,C]=0$. It's worth pausing on why this particular condition is
the physically right one to impose, since it isn't obvious on sight. $C$ generates *emph*
translations: shifting $\hat q$ by some amount while also flowing modular time by the same amount (since $K$
generates the modular flow and $\hat q$ generates ordinary translations on $L^2(\mathbb R)$, $e^{iCs}$
translates both at once). Demanding invariance under $C$ is exactly demanding that only the *emph*
reading of "clock minus modular time" matters, not either one separately — mathematically identical to the
familiar physics idea that only relative position matters, never an absolute coordinate origin. Physically,
in the applications of Sec.~IX, $\hat q$ will be an observer's own energy and $\hat p$ their proper time, and
this invariance condition becomes exactly the statement that physical observables must be
diffeomorphism-invariant (unable to depend on an arbitrary choice of where to put a clock's zero).

Two families of operators manifestly satisfy $[a,C]=0$, and it can be shown they generate the whole of
$\widehat\M$. First, $\hat q$ itself trivially commutes with $C=K+\hat q$ (since $[\hat q,\hat q]=0$ and
$\hat q$ acts on a different factor than $K$), so any (Weyl-form, since $\hat q$ is unbounded) function of it,
$e^{-i\hat qs}$, belongs to $\widehat\M$. Second — and this is the nontrivial part — ordinary elements $A\in
\M$ do *emph* commute with $C$ on their own (since $[A,K]\ne0$ in general — that's exactly what it means
for $K$ to generate a nontrivial flow on $A$), but a specific *emph* version of them does:

$$

[e^{iK\hat p}Ae^{-iK\hat p},\,C] = 0, \qquad A\in\M

$$

(eq.~5.5). Let us prove this commutator identity directly using ordinary canonical commutation relations. Let $\widehat A \equiv e^{iK\hat p}(A\otimes\id)e^{-iK\hat p}$. Using $[\hat q,\hat p]=i$, the position operator acts as a derivative in momentum space: $[\hat q, f(\hat p)] = i f'(\hat p)$. Applying this to the clock translation operator:

$$

[\hat q, \, e^{iK\hat p}] = i(iK)e^{iK\hat p} = -K e^{iK\hat p}, \qquad [\hat q, \, e^{-iK\hat p}] = i(-iK)e^{-iK\hat p} = K e^{-iK\hat p} .

$$

Now compute the commutator $[\hat q, \widehat A]$ using the Leibniz product rule:
\begin{align*}
[\hat q, \, \widehat A] &= [\hat q, \, e^{iK\hat p}](A\otimes\id)e^{-iK\hat p} + e^{iK\hat p}(A\otimes\id)[\hat q, \, e^{-iK\hat p}] \\
&= -K e^{iK\hat p}(A\otimes\id)e^{-iK\hat p} + e^{iK\hat p}(A\otimes\id) e^{-iK\hat p} K \\
&= -K \widehat A + \widehat A K = -[K, \, \widehat A] .
\end{align*}
Therefore, evaluating the commutator with the total constraint $C = K + \hat q$:

$$

[C, \, \widehat A] = [K + \hat q, \, \widehat A] = [K, \, \widehat A] + [\hat q, \, \widehat A] = [K, \, \widehat A] - [K, \, \widehat A] = 0 !

$$

The modular-flow dressing by the clock's momentum $\hat p$ exactly cancels the non-commutativity with $K$, ensuring that $\widehat A$ is strictly invariant under $C$.
So

$$

\widehat\M = \big\{e^{iK\hat p}Ae^{-iK\hat p},\ e^{-i\hat qs} \ \big|\ A\in\M,\ s\in\mathbb R\big\}''

$$

(eq.~5.6), and a general element has the schematic form $\widehat A=\int ds\,A(\hat p;s)\,e^{-i\hat qs}$
(eq.~5.7), with $A(\hat p;s)\equiv e^{iK\hat p}A(s)e^{-iK\hat p}$ built from an operator-valued function
$A(s)\in\M$ — since $\hat p$ is now an operator, $A(\hat p;s)$ is a genuine operator-valued ``function of an
operator,'' living in a kind of quantum spacetime.

There's a second, equivalent way to present the same algebra, obtained by a unitary change of frame
$U=e^{-iK\hat p}$ (which conjugates $\widehat\M\to U\widehat\M U^\dagger$, $C\to UCU^\dagger$), and this
alternative form turns out to be more convenient for essentially everything that follows:

$$

\widehat\M = \big\{A,\ e^{i(K-\hat q)s} \ \big|\ A\in\M,\ s\in\mathbb R\big\}'', \qquad
\widehat A = \int ds\, A(s)\,e^{is(K-\hat q)}, \ A(s)\in\M

$$

(eqs.~5.10, 5.12) — in this frame, ordinary (undressed) elements of $\M$ sit directly inside $\widehat\M$,
and all the dressing has been absorbed into the clock-dependent generator $K-\hat q$ instead.

## Sec.~V.B: $\widehat\M$ is always type II

### Finding the modular operator of $\widehat\M$

Now specialize to $K=-\log\Delta_\Psi$, the genuine modular generator of $\M$, and take the reference vector

$$

\ket{\widehat\Psi} = \ket\Psi\otimes\ket{p=0}

$$

(eq.~5.13, the clock prepared in a definite-momentum, i.e.\ completely spread out in position, state — not
literally normalizable, a technical point flagged in the paper's footnote~30 but not one that affects any
conclusion below). It can be shown $\ket{\widehat\Psi}$ is cyclic and separating for $\widehat\M$, so
Tomita—Takesaki theory applies, and the modular operator $\widehat\Delta$ can be found by directly solving the defining KMS relation, $\braket{\widehat\Psi|\widehat A\widehat B|\widehat\Psi}=\braket{\widehat\Psi|\widehat B\,\widehat\Delta\,\widehat A|\widehat\Psi}$ (eq.~5.14). While usually relegated to technical appendices, the explicit calculation reveals a remarkably transparent cancellation:

\begin{keyresult}[: Derivation of the Crossed Product Modular Operator $\widehat\Delta$]
**Goal:** Prove that on $\widehat\HH = \HH \otimes L^2(\mathbb{R})$ with reference vector $\ket{\widehat\Psi} = \ket\Psi \otimes \ket{p=0}$, the Tomita conjugate operator satisfies $\widehat S = S_\Psi \otimes \mathcal{P}_p$, and the modular operator satisfies:

$$

\widehat\Delta \equiv \widehat S^\dagger \widehat S = \Delta_\Psi \otimes \id = \Delta_\Psi .

$$

**Derivation:**

1. **Action of general operator on reference state:**
In the presentation of eq.~5.10, a general operator $\widehat A \in \widehat\M$ is given by:

$$

\widehat A = \int_{-\infty}^\infty ds \, A(s) \, e^{is(K - \hat q)}, \qquad A(s) \in \M .

$$

Act with $\widehat A$ on the reference state $\ket{\widehat\Psi} = \ket\Psi \otimes \ket{p=0}$.
Since $K = -\log\Delta_\Psi$ and $\Delta_\Psi\ket\Psi = \ket\Psi$, the modular Hamiltonian annihilates the state: $K\ket\Psi = 0 \implies e^{is K}\ket\Psi = \ket\Psi$.
On the clock, $\hat q = i\partial_p$ in momentum space, so $e^{-is\hat q}$ translates the clock momentum:

$$

e^{-is\hat q}\ket{p=0} = \ket{p = -s} .

$$

Since $K$ and $\hat q$ commute (acting on independent Hilbert spaces $\HH$ and $L^2(\mathbb{R})$):

$$

e^{is(K - \hat q)}\ket{\widehat\Psi} = \big(e^{is K}\ket\Psi\big) \otimes \big(e^{-is\hat q}\ket{p=0}\big) = \ket\Psi \otimes \ket{p = -s} .

$$

Multiplying by $A(s) \in \M$ and substituting $p = -s$:

$$

\widehat A \ket{\widehat\Psi} = \int_{-\infty}^\infty ds \, A(s)\ket\Psi \otimes \ket{p = -s} = \int_{-\infty}^\infty dp \, A(-p)\ket\Psi \otimes \ket{p} .

$$

The clock momentum $p$ directly sorts the modular-flow Fourier components of the state!
2. **Action of the Hermitian conjugate $\widehat A^\dagger$:**
Now compute the adjoint operator $\widehat A^\dagger$:

$$

\widehat A^\dagger = \int_{-\infty}^\infty ds \, e^{-is(K - \hat q)} A(s)^\dagger = \int_{-\infty}^\infty ds \, \Big( e^{-is(K - \hat q)} A(s)^\dagger e^{is(K - \hat q)} \Big) e^{-is(K - \hat q)} .

$$

Since $[\hat q, A(s)^\dagger] = 0$, the internal conjugation is simply the modular flow on the original algebra $\M$:

$$

e^{-is(K - \hat q)} A(s)^\dagger e^{is(K - \hat q)} = e^{-is K} A(s)^\dagger e^{is K} = \Delta_\Psi^{is} A(s)^\dagger \Delta_\Psi^{-is} \equiv \alpha_{-s}\big(A(s)^\dagger\big) .

$$

Acting on $\ket{\widehat\Psi} = \ket\Psi \otimes \ket{p=0}$:

$$

\widehat A^\dagger \ket{\widehat\Psi} = \int_{-\infty}^\infty ds \, \alpha_{-s}\big(A(s)^\dagger\big)\ket\Psi \otimes \ket{p = s} .

$$

Using $\Delta_\Psi^{-is}\ket\Psi = \ket\Psi$ and the Tomita definition $S_\Psi A\ket\Psi = A^\dagger\ket\Psi$:

$$

\alpha_{-s}\big(A(s)^\dagger\big)\ket\Psi = \Delta_\Psi^{is} A(s)^\dagger\ket\Psi = \Delta_\Psi^{is} S_\Psi A(s)\ket\Psi .

$$

3. **The Tomita operator $\widehat S$ and clock parity:**
Under the standard Tomita map $\widehat S(\widehat A\ket{\widehat\Psi}) = \widehat A^\dagger\ket{\widehat\Psi}$, comparing the vectors $\ket{p}$ and $\ket{-p}$ shows that the clock undergoes a momentum reflection (parity operation) $\mathcal{P}_p \ket{p} \equiv \ket{-p}$, while on $\HH$ the action is governed by $S_\Psi$:

$$

\widehat S = S_\Psi \otimes \mathcal{P}_p .

$$

4. **Cancellation in the modular operator:**
Now evaluate the modular operator $\widehat\Delta \equiv \widehat S^\dagger \widehat S$:

$$

\widehat\Delta = \big(S_\Psi^\dagger \otimes \mathcal{P}_p^\dagger\big) \big(S_\Psi \otimes \mathcal{P}_p\big) = \big(S_\Psi^\dagger S_\Psi\big) \otimes \big(\mathcal{P}_p^\dagger \mathcal{P}_p\big) .

$$

Because the parity reflection $\mathcal{P}_p$ is an isometry ($\mathcal{P}_p^\dagger \mathcal{P}_p = \id_{L^2(\mathbb{R})}$):

$$

\widehat\Delta = \Delta_\Psi \otimes \id_{L^2(\mathbb{R})} = \Delta_\Psi . \qquad \blacksquare

$$


\end{keyresult}

The answer, remarkably simple given how much machinery went into $\widehat\M$'s construction, is:

$$

\widehat\Delta = \Delta_\Psi

$$

(eq.~5.15) — **the new algebra's modular operator, in this particular reference state, is exactly the same operator as the original algebra's modular operator.** Nothing new needed to be invented; the crossed product inherited its modular structure wholesale.

### Why this forces type II

Here is the key algebraic manipulation, and it's short enough to walk through completely. Using
$\widehat\Delta=e^{-K}$ directly:

$$

\widehat\Delta = e^{-K} = e^{-(K-\hat q)}e^{-\hat q} \equiv \rho\rho'^{-1}, \qquad
\rho\equiv e^{-(K-\hat q)}, \quad \rho'\equiv e^{\hat q}

$$

(eq.~5.16), so

$$

\widehat\Delta^{-is} = e^{i(K-\hat q)s}\,e^{i\hat qs}

$$

(eq.~5.17). Now look at what the two factors on the right actually are, comparing against the two presentations
of $\widehat\M$ and $\widehat\M'$ (eqs.~5.10—5.11) given above: $e^{i(K-\hat q)s}$ is manifestly a unitary
sitting inside $\widehat\M$ itself (it's literally one of the generators listed in eq.~5.10), and $e^{i\hat
qs}$ is manifestly a unitary sitting inside $\widehat\M'$ (the commutant, built from eq.~5.11's generators).
**So $\widehat\Delta^{-is**$ factors as a product of a unitary in $\widehat\M$ times a unitary in
$\widehat\M'$} — which is exactly the criterion (eq.~4.22 of Sec.~IV.B) for the modular flow to be an
*emph* automorphism of $\widehat\M$. But Sec.~IV.B's criterion (eq.~4.21) says modular flow is inner for
*emph* $s$ if and only if the algebra is type I or type II — never type III. **So $\widehat\M$
cannot be type III**, whatever $\M$ itself was. And since $\widehat\HH=\HH\otimes L^2(\mathbb R)$ still cannot
be factorized with respect to $\widehat\M$ (nothing about attaching a clock and imposing an invariance
condition magically produced a tensor factorization — the underlying obstruction from $\M$ is still there),
$\widehat\M$ cannot be type I either. **By elimination, $\widehat\M$ is type II.** This is worth
appreciating as a genuinely clean piece of reasoning: no explicit trace needed to be constructed to reach this
conclusion — it followed purely from identifying the modular operator and checking the inner-automorphism
criterion already established in Sec.~IV.

### Building the trace explicitly, and checking cyclicity by hand

Having established *emph* a trace exists, it's worth actually writing one down and checking it really
works, rather than just trusting the general argument. Define

$$

\tr\widehat A \equiv \braket{\widehat\Psi|\widehat A\,\rho^{-1}|\widehat\Psi}

$$

(eq.~5.20, using $\rho=e^{-(K-\hat q)}$ from eq.~5.16 — motivated by the standard fact that if a trace exists,
expectation values in *emph* state should look like $\braket{A}=\tr(A\rho_{\text{state}})$ for some density
operator $\rho_{\text{state}}$; solving for what $\rho_{\text{state}}$ would need to be, given that
$\ket{\widehat\Psi}$ is itself the reference state used to build $\Delta_\Psi=\widehat\Delta$, directly
motivates dividing by $\rho$). Cyclicity, $\tr(\widehat A\widehat B)=\tr(\widehat B\widehat A)$, is checked
directly using nothing but the KMS relation (eq.~5.14) that defined $\widehat\Delta$ in the first place:

$$

\tr(\widehat A\widehat B) = \braket{\widehat\Psi|\widehat A\widehat B\rho^{-1}|\widehat\Psi}
= \braket{\widehat B\rho^{-1}\widehat\Delta\,\widehat A} = \braket{\widehat B\rho'^{-1}\widehat A}
= \braket{\widehat B\widehat A\rho'^{-1}} = \tr(\widehat B\widehat A)

$$

(eq.~5.22, suppressing the common $\braket{\widehat\Psi|\cdots|\widehat\Psi}$ for brevity in each term): the
first step is just the definition of $\tr$; the second is the KMS relation (eq.~5.14) applied with the roles
of $A\rho^{-1}$ and $B$ swapped; the third uses $\rho^{-1}\widehat\Delta=\rho^{-1}\rho\rho'^{-1}=\rho'^{-1}$
directly from eq.~5.16's factorization; and the fourth uses that $\rho'^{-1}=e^{-\hat q}\in\widehat\M'$
(established just above) commutes with $\widehat A\in\widehat\M$ by definition of the commutant. Every step is
either a definition or something already established — no new assumption anywhere. This is worth comparing to
the very similar, but much more concrete, cyclicity check already carried out by hand in Sec.~III.C.1
(eqs.~3.12—3.14 of that companion section, for the finite Bell-pair-chain trace): the mechanism is
structurally the same idea (a specific reference state's own consistency conditions force cyclicity), just
now stated in the fully general, type-III-compatible language of modular theory rather than worked out on
explicit small matrices.

### Type $\mathrm{II_\infty$, or type $\mathrm{II}_1$ if you restrict the clock's energy}

Compute $\tr(\id)$ directly from eq.~5.21 (an explicit rewriting of eq.~5.20 for the identity element):

$$

\tr(\id) = \int_{-\infty}^{\infty} dq\, e^{-q} \braket{\Psi|\id|\Psi} = \int_{-\infty}^\infty dq\,e^{-q} = \infty

$$

(eq.~5.25) — divergent, so by the Sec.~II.C classification, $\widehat\M$ is (so far) type $\mathrm{II}_\infty$.
But here is a genuinely simple, physically motivated fix, worth seeing in full because it's exactly the
mechanism reused in Sec.~IX: restrict the clock's spectrum to be bounded below, $q\ge0$ — physically, the
statement that a real observer's energy cannot be negative, certainly a reasonable restriction on any
physically sensible clock. Concretely, insert the projector $\Pi=\theta(\hat q)$ (the step function, $1$ for
$q\ge0$ and $0$ for $q<0$) and define $\widehat\M_+\equiv\Pi\widehat\M\Pi$, acting only on the restricted
Hilbert space $\HH\otimes L^2(\mathbb R_{>0})$. The identity of this smaller algebra is $\Pi$ itself, and

$$

\tr_{\widehat\M_+}(\id) = \tr_{\widehat\M}(\Pi) = \int_{-\infty}^\infty dq\,e^{-q}\theta(q) = \int_0^\infty
dq\,e^{-q} = 1

$$

(eq.~5.26) — finite, and in fact already normalized to $1$ with no further rescaling needed. **So
restricting a physical observer's clock to have positive energy is exactly the algebraic operation that turns
type $\mathrm{II**_\infty$ into type $\mathrm{II}_1$} — a purely mathematical fact about which subtype of type
II you land in, but one with an immediate and physically loaded reading: whether the observer crossing your
algebra has a bounded-below energy spectrum directly decides which flavor of type II entropy you'll be
computing. This exact fork reappears, with real physical stakes attached, when black hole entropy
(type $\mathrm{II}_\infty$, Sec.~IX.B) is contrasted with de~Sitter entropy (type $\mathrm{II}_1$, Sec.~IX.C).

### The crossed product doesn't actually depend on which reference state you started with

One loose end, promised at the start of this section: $\widehat\M$ was built using a specific cyclic-separating
$\ket\Psi$ to define the modular generator $K$ that got crossed with — does a different choice $\ket\Phi$ give
a genuinely different algebra? It can be shown it does not, only a *emph* one,

$$

\widehat\M_\Phi = u'_{\Phi\Psi}(\hat p)\,\widehat\M_\Psi\,u_{\Phi\Psi}'^\dagger(\hat p)

$$

(eq.~5.27), where $u'_{\Phi\Psi}$ is exactly the intertwining unitary from Sec.~IV.F (eq.~4.114), with the flow
parameter identified with the clock's momentum operator $\hat p$. (The short computation establishing this,
eq.~5.29, is a direct if slightly involved manipulation using the identities from Sec.~IV.F and is not
reproduced symbol-by-symbol here — the content that matters is the conclusion: $\widehat\M$ is, up to unitary
equivalence, an *emph* invariant of $\M$ alone, exactly as claimed at the start of this section.)

## Sec.~V.C: density operator for $\widehat\M$ in a general semiclassical state

With a genuine trace in hand, Sec.~III's machinery — a density operator defined by
$\tr(A\rho_{\widehat\M})=\braket{\text{state}|A|\text{state}}$ — becomes available for $\widehat\M$. The
paper works this out for a
class of physically motivated states of the form $\ket{\widehat\Phi}=\ket\Phi\otimes\ket g$ (eq.~5.30), where
$\ket g$ is some fixed clock wavefunction, normalized ($\int dq\,|g(q)|^2=1$, eq.~5.31) and nonvanishing
everywhere. Solving the defining equation for the resulting density operator is a genuinely involved
computation (eqs.~5.32—5.41 of the paper, using the two-state KMS relation, eq.~4.105, from Sec.~IV.F, twice
over, together with the explicit form $\braket{q|e^{-iK\hat p}|g}=g(q-K)$, eq.~5.37, for how the clock
wavefunction transforms between the two frames of eqs.~5.6 and 5.10) — not walked through symbol by symbol
here, since the manipulation itself is mostly bookkeeping once the KMS relation is trusted, but the outcome is
clean:

$$

\rho_{\widehat\Phi} = 2\pi\, g(\hat q-K)\,e^{\hat q}\,\Delta_{\Phi\Psi}\, g^*(\hat q-K)

$$

(eq.~5.39, in the frame of eqs.~5.6—5.7; the corresponding expression in the other frame, eq.~5.10, is
obtained by conjugating with $U^\dagger$, eq.~5.41) — an explicit operator, built from the clock wavefunction
$g$, the (already familiar) $e^{\hat q}$ factor from the trace's own normalization, and the relative modular
operator $\Delta_{\Phi\Psi}$ from Sec.~IV.F comparing the state of interest $\Phi$ to the reference $\Psi$
used to build the crossed product in the first place.

## Sec.~V.D: entanglement entropy for $\widehat\M$ in a general semiclassical state

### The final formula, and why it has exactly the shape it does

Plugging $\rho_{\widehat\Phi}$ into the ordinary entropy formula, $S_{\widehat\M}=-\tr(\rho_{\widehat\Phi}\log
\rho_{\widehat\Phi})$ (eq.~5.42), and specializing to a **semiclassical** clock wavefunction — one that
varies slowly, $g'(q)\propto\epsilon$ for some small parameter $\epsilon$, and working to leading order in
$\epsilon$ — the paper carries out an expansion (eqs.~5.43—5.48: expand $-\log\rho_{\widehat\Phi}$ using
$K_{\Phi\Psi}=K_\Phi+K-K_{\Psi\Phi}$ from Sec.~IV.F's eq.~4.116, then evaluate the resulting expectation value
term by term, using $K_\Phi\ket\Phi=0$ from the ordinary modular-operator property eq.~4.9, and recognizing
the surviving piece directly as the relative entropy definition, eq.~4.117, of Sec.~IV.F) that lands on

$$

S_{\widehat\M}(\widehat\Phi) = -S_\M(\Phi\|\Psi) - \bar q + S_o, \qquad
\bar q = \int dq\,q\,|g(q)|^2, \qquad S_o = -\int dq\,|g(q)|^2\log|g(q)|^2

$$

(eqs.~5.49—5.50): $\bar q$ is simply the mean clock reading under the probability distribution $|g(q)|^2$, and
$S_o$ is the ordinary (differential) Shannon entropy of that same distribution — both depending only on the
shape of the clock wavefunction $g$, not on the state $\Phi$ being described. **The entropy of the type
II crossed-product algebra, up to state-independent constants fixed entirely by the clock, is exactly minus
the type III relative entropy of the original algebra $\M$.** This is worth appreciating as a genuinely
satisfying closing of the loop opened at the very start of Sec.~IV: relative entropy, introduced there as ``the
one thing that survives type III when ordinary entropy doesn't,'' now turns out to literally *emph* an
ordinary, honest entropy — just of a different, larger algebra, built by attaching a clock.

\begin{quote}
*textit* It's
worth seeing the qualitative content of eq.~5.49 confirmed on a fully explicit, computable example, even
though the actual derivation above is more careful about tracking exactly which piece is the relative-entropy
term. Model the leading-order, unnormalized weight the state assigns to clock reading $q$ as
$\rho(q)\propto g(q)^2\,e^{q}$ (the $e^q$ factor tracking the $\rho^{-1}=e^{K-\hat q}$ dependence built into the
trace's own definition, eq.~5.20, once the $\M$-sector operator content has been integrated out against a
fixed state and only the clock dependence is left), for a Gaussian clock wavefunction of width $\sigma$
centered at $\bar q_0$, $g(q)^2=\frac{1}{\sqrt{2\pi}\sigma}\exp\!\big(-(q-\bar q_0)^2/2\sigma^2\big)$. Carrying
out the resulting Gaussian integral symbolically: the normalization is $Z=\int dq\,g(q)^2e^{q}=\exp(\bar
q_0+\sigma^2/2)$, and the resulting (still Gaussian, same width $\sigma$) tilted distribution
$\rho(q)/Z$ has its mean shifted up by exactly one unit of variance, $\braket{q}=\bar q_0+\sigma^2$ — the
$e^q$ factor systematically biases the observed clock reading upward, an effect you can see directly in this
toy model rather than having to trust it abstractly. Its (differential) entropy is the standard Gaussian
formula $\tfrac12\log(2\pi e\sigma^2)$, so

$$

-\braket{q} + \big(\text{entropy}\big) = -\bar q_0 - \sigma^2 + \tfrac12\log(2\pi e\sigma^2) ,

$$

computed exactly for this Gaussian example: an expression of the form $-\bar q_0$ plus clock-shape-only terms,
matching the general shape of eq.~5.49 (with the leftover $-\sigma^2+\tfrac12\log(2\pi e\sigma^2)$ terms
playing the role of the general formula's $S_o$, in this simplified toy where the relative-entropy piece
has been set aside by construction). This is offered as a sanity check on the *emph* of the general
result, not as a substitute for the paper's own, more careful derivation above, which correctly separates out
the $\M$-sector relative-entropy contribution that this simplified toy model doesn't track.
\end{quote}

\bigskip
\noindent This closes Sec.~V, and with it, the entire first half of the paper (Secs.~II—V): a type III
algebra, with no trace and no entropy of its own, can always be crossed by its own modular group to produce a
type II algebra that does have both — and that type II algebra's entropy is nothing but the original algebra's
relative entropy, in disguise. Section~VI turns to the payoff this machinery was built for: applying every
tool developed so far — the type classification, modular theory, and now the crossed product — to the
large-$N$ limit of the AdS/CFT correspondence itself.



---

# Sec.~VI: AdS/CFT duality in the large-$N$ limit: algebraic formulation

Everything built in Secs.~II—V was developed for its own sake, using nothing more exotic than qubits, matrix
algebras, and (in Sec.~IV.D) an ordinary free quantum field. This section is where the payoff begins: applying
every one of those tools — the type classification, GNS, modular theory, the crossed product — to the actual
physical system this paper's title promises to explain, the AdS/CFT correspondence, in the specific limit
($N\to\infty$, equivalently $G_N\to0$) where bulk spacetime is supposed to emerge.

## Sec.~VI.A: general description

### The dictionary, restated precisely

AdS/CFT conjectures that quantum gravity on $(d{+}1)$-dimensional anti-de~Sitter space is completely
equivalent to an ordinary (non-gravitational) conformal field theory living on its $d$-dimensional boundary —
the prototypical example being type IIB string theory on $\text{AdS}_5\times S^5$, dual to $\mathcal N=4$
super-Yang-Mills with gauge group $SU(N)$. The dictionary's core entries (eqs.~6.1—6.5): the two theories
share literally the same Hilbert space, $\HH_{\text{bulk}}=\HH_{\text{CFT}}\equiv\HH$; the classical-gravity
limit $G_N\to0$ is the same as the large-$N$ limit of the boundary gauge theory; the limit $\alpha'\to0$ (the
string tension going to zero, so stringy corrections switch off) is the same as the boundary 't~Hooft coupling
$\lambda\to\infty$; elementary bulk fields correspond to **single-trace operators** (boundary operators
literally built as a trace over color indices, $\Tr(\cdots)$, eq.~6.7); and a classical bulk geometry $\phi_c$
corresponds to a specific boundary state $\ket\Psi$, called a **semiclassical state**.

The precise bulk-to-boundary map for fields, the **extrapolate dictionary**, is

$$

O(x) = \lim_{r\to\infty} r^\Delta\,\phi(r,x)

$$

(eq.~6.6): take a bulk field $\phi$, evaluate it at radial coordinate $r$ and boundary point $x$, rescale by
$r^\Delta$ (where $\Delta$ is the operator's conformal dimension, a number fixed by the field's mass), and
send $r\to\infty$ (out to the AdS boundary) — what survives this limit is exactly the corresponding boundary
operator $O(x)$. This equation is not a definition invented for convenience; for holographic theories where an
independent definition of $O(x)$ already exists (like $\Tr(\cdots)$ in super-Yang-Mills), eq.~6.6 is a
derived fact. For more general holographic systems where no such independent definition is available, eq.~6.6
*emph* taken as the definition of what counts as a single-trace operator.

A semiclassical state $\ket\Psi$ is one with a well-defined $N\to\infty$ limit — meaning it can genuinely be
built as the limit of a sequence of states $\{\ket{\Psi_N}\}$, one for each finite-$N$ theory. The vacuum
$\ket\Omega$ (dual to empty AdS) and the thermofield double $\ket{\Psi_\beta}$ (dual, at high enough
temperature, to an eternal black hole) are the two worked examples of this section; a single-sided black hole
formed by collapse is a third example, generally harder to write down explicitly.

### Building the boundary operator algebra with GNS — and why it might be bigger than you'd guess

Here is where the machinery of Secs.~II and IV gets put to direct use. Call an operator $A$ ``having a
well-defined large-$N$ limit in the state $\ket\Psi$'' if it's the limit of some sequence of finite-$N$
operators $\{A_N\}$ (with corresponding states $\{\ket{\Psi_N}\}$) whose expectation value converges to
something finite, $\lim_{N\to\infty}\braket{\Psi_N|A_N|\Psi_N}<\infty$ (eq.~6.8) — precisely the kind of
finite-energy restriction from Sec.~I's Bell-pair-chain discussion, now applied to a genuine gauge theory.
Call the collection of all such operators $\Alg_\Psi$. One universal subset, present for every semiclassical
state, is

$$

\Sscr \equiv \text{the } *\text{-algebra generated by single-trace operators} \subseteq \Alg_\Psi

$$

(eq.~6.9) — but the containment need not be an equality: $\Alg_\Psi$ may contain *emph* operators than
just those built from single-trace operators, and which extra operators survive can depend on the specific
state $\Psi$. (This inclusion being strict, rather than an equality, turns out to be exactly the mechanism
behind describing a black-hole *emph* in Sec.~VI.D below — worth flagging now, since it's easy to
skim past this subtlety on a first read.)

Assuming $\Alg_\Psi$ is closed under products (a $*$-algebra) and completed in its inherited norm (a
$C^*$-algebra, exactly the objects of Sec.~II.B), expectation values in $\ket\Psi$ define a state $\omega_\Psi$
on $\Alg_\Psi$ — and now the entire GNS machinery of Sec.~II.D applies directly: build the GNS Hilbert space
$\HH_\Psi^{\text{GNS}}$ from $(\Alg_\Psi,\omega_\Psi)$, with representation $\pi_\Psi(\Alg_\Psi)$. This is,
quite literally, "the space of small excitations around $\ket\Psi$" — exactly the same construction already
carried out by hand, on qubits, back in Sec.~II.E. If the bulk geometry dual to $\Psi$ is smooth and $\Psi$ is
pure, $\omega_\Psi$ is expected to be a pure state on $\Alg_\Psi$, which by Sec.~II.D's Proposition~II.1 means
the representation is irreducible, $B(\HH_\Psi^{\text{GNS}})=\pi_\Psi(\Alg_\Psi)''$ (eq.~6.10) — this can fail
if the dual geometry has a singularity reachable on some Cauchy slice, a subtlety picked back up in the
firewall discussion of Sec.~VI.E. Write $Y\equiv(\pi_\Psi(\Sscr))''$, $Y_O\equiv(\pi_\Psi(\Sscr_O))''$
(eq.~6.11) for the (possibly strictly smaller) von Neumann algebra generated by single-trace operators alone,
restricted if needed to a boundary region $O$.

### Matching this to an ordinary bulk Fock space

On the gravity side, expand every bulk field around its classical background exactly as before (Sec.~VI.A of
this companion echoes Sec.~I's roadmap here): $\phi=\phi_c+\kappa\delta\phi$, $\kappa=\sqrt{8\pi G_N}$
(eq.~6.12), giving an action $S[\phi_c]+S_2[\delta\phi]+S_{\text{int}}[\delta\phi]$ with $S_{\text{int}}=
\kappa S_3+\kappa^2S_4+\cdots$ (eqs.~6.13—6.14). At leading order $\kappa\to0$, only the free, quadratic
piece $S_2$ survives, giving an ordinary free quantum field theory of $\delta\phi$ on the fixed background
$\phi_c$ — quantized in the standard way, with some vacuum $\ket0_{\phi_c}$, into a genuine Fock space
$\HH_\Psi^{\text{Fock}}$.

For the AdS/CFT duality to actually hold, these two constructions — one built from the boundary algebra via
GNS, the other built from the bulk field theory via ordinary quantization — must agree:

$$

\HH_\Psi^{\text{Fock}} = \HH_\Psi^{\text{GNS}}

$$

(eq.~6.15), which requires the GNS representation to have exactly the structure of a Fock space (a Gaussian theory, meaning correlators factorize into products of two-point functions). While often taken for granted as "standard large-$N$ factorization," this Fock-space structure is a rigorous consequence of 't~Hooft planar scaling:

\begin{keyresult}[: Derivation of the Large-$N$ Generalized Free Field and CCR Algebra]
**Goal:** Prove that in a large-$N$ $SU(N)$ gauge theory with fixed 't~Hooft coupling $\lambda = g_{YM}^2 N$:

1. Connected correlators scale as $\braket{\mathcal{O}_1 \cdots \mathcal{O}_n}_{\text{conn}} \sim N^{2-n}$.
2. Commutators between single-trace operators reduce to exact $c$-numbers: $[\mathcal{O}_A, \mathcal{O}_B] = c_{AB}\id + \mathcal{O}(1/N)$.
3. The resulting boundary algebra is a CCR algebra whose GNS space is identically a free Fock space $\HH_\Psi^{\text{Fock}}$.


**Derivation:**

1. **'t~Hooft topological expansion:**
Consider an adjoint matrix field theory with action $S = \frac{N}{\lambda}\int d^d x \Tr\big[\frac{1}{2}(\partial\Phi)^2 + V(\Phi)\big]$.
Define normalized single-trace gauge-invariant operators:

$$

\mathcal{O}_i(x) \equiv \frac{1}{N}\Tr\big(\Phi^{k_i}(x)\big) - \Braket{\frac{1}{N}\Tr\big(\Phi^{k_i}(x)\big)} .

$$

In 't~Hooft double-line notation, a Feynman graph with $V$ vertices, $E$ edges, and $F$ index loops scales as:

$$

(g_{YM}^2)^{E-V} N^F = \lambda^{E-V} N^{V - E + F} = \lambda^{E-V} N^\chi = \lambda^{E-V} N^{2 - 2g} ,

$$

where $\chi = 2 - 2g$ is the Euler characteristic of the Riemann surface of genus $g$. The leading diagrams are planar with sphere topology ($g = 0$, $\chi = 2$), contributing at order $N^2$.
2. **Scaling of connected correlators:**
Consider a connected correlator of $n$ single-trace operators: $\braket{\mathcal{O}_1(x_1) \cdots \mathcal{O}_n(x_n)}_{\text{conn}}$.
Each operator $\mathcal{O}_i$ carries an explicit normalization factor of $1/N$.
The planar vacuum diagrams connecting all $n$ external source insertions scale with the leading genus-zero factor $N^2$.
Therefore:

$$

\Braket{\mathcal{O}_1(x_1) \cdots \mathcal{O}_n(x_n)}_{\text{conn}} \sim N^2 \cdot \left(\frac{1}{N}\right)^n = N^{2-n} .

$$

Evaluating the leading power of $N$:



6. **Wick's theorem and Gaussian factorization:**
Since all connected correlators with $n \ge 3$ vanish strictly in the $N \to \infty$ limit, the cumulant expansion implies that any higher-order correlation function decomposes into the sum of products of two-point functions:

$$

\lim_{N\to\infty} \Braket{\mathcal{O}_1(x_1) \cdots \mathcal{O}_{2m}(x_{2m})} = \sum_{\text{pairings } \pi} \prod_{(i, j) \in \pi} \Braket{\mathcal{O}_i(x_i)\mathcal{O}_j(x_j)} .

$$

The theory of single-trace operators becomes an exact **Generalized Free Field** (GFF).
7. **Commutators as $c$-numbers:**
Now examine the commutator $[\mathcal{O}_A(x), \mathcal{O}_B(y)]$. Its expectation value is a deterministic scalar:

$$

c_{AB}(x, y)\id \equiv \Braket{[\mathcal{O}_A(x), \mathcal{O}_B(y)]} \id \sim \mathcal{O}(1)\id .

$$

The quantum fluctuation of the commutator operator itself is given by the connected 4-point function:

$$

\Big\| \big([\mathcal{O}_A(x), \mathcal{O}_B(y)] - c_{AB}(x, y)\id\big)\ket\Omega \Big\|^2 \sim \Braket{\mathcal{O}_A\mathcal{O}_B\mathcal{O}_A\mathcal{O}_B}_{\text{conn}} \sim N^{2-4} = \frac{1}{N^2} \xrightarrow{N\to\infty} 0 .

$$

The operator fluctuations vanish identically as $N \to \infty$!
Hence the commutator becomes an exact $c$-number:

$$

[\mathcal{O}_A(x), \, \mathcal{O}_B(y)] = c_{AB}(x, y)\,\id .

$$

8. **Emergence of bulk Fock space:**
This commutator relation is the Canonical Commutation Relation (CCR) of a free quantum field. The GNS representation of this CCR algebra on the cyclic vacuum $\ket1_\Psi$ generates an exact multi-particle Fock space:

$$

\HH_\Psi^{\text{GNS}} = \overline{\mathrm{span}\big\{\mathcal{O}_{i_1} \cdots \mathcal{O}_{i_k}\ket1_\Psi\big\}} \cong \HH_\Psi^{\text{Fock}} .

$$

Boundary single-trace operators act as creation and annihilation operators for the non-interacting bulk quantum field fluctuations $\delta\phi$, proving eq.~6.15. $\blacksquare$

\end{keyresult}

It is now completely natural to identify the two vacua, $\ket0_{\phi_c}=\ket1_\Psi$ (eq.~6.16, where $\ket1_\Psi$ denotes the GNS vector corresponding to the identity operator — literally the same object called $\ket\Omega$ throughout Sec.~II).

### Disjoint sectors: no single Hilbert space survives $N\to\infty$

Here is a structural consequence worth sitting with, because it's the direct large-$N$ analogue of exactly
the obstruction from Sec.~I. Different semiclassical states — different classical bulk geometries — typically
differ in energy by an amount of order $O(1/G_N)$ (an ordinary classical-gravity energy difference, which
diverges as $G_N\to0$), whereas states *emph* a single $\HH_\Psi^{\text{GNS}}$ differ from $\Psi$ only
by $O(G_N^0)$ (an ordinary quantum fluctuation, staying finite). So the GNS Hilbert spaces $\HH_{\Psi_1}$ and
$\HH_{\Psi_2}$, built around two different classical geometries, cannot overlap at any finite order in
$G_N$-perturbation theory — and (a further, more subtle point) even two semiclassical states of the
*emph* energy can still belong to different GNS sectors if they're separated by an infinite entanglement
barrier in field space, exactly the Sec.~I mechanism. **So in the large-$N$ limit, there is no longer one
single Hilbert space for the theory — the space of states shatters into disjoint sectors, one per
semiclassical background**, each with its own GNS Hilbert space and its own emergent operator-algebra
structure (Fig.~7 of the paper). This is presented explicitly as the direct large-$N$ analogue of the entangled
spin chain's $N\to\infty$ behavior for different $\theta$ (Sec.~II.E): different $\theta$ gave disjoint sectors
there; different classical geometries give disjoint sectors here, for exactly the same underlying reason.

### Why boundary time slices carry genuinely independent algebras

One more structural fact, worth understanding carefully because it explains something that would otherwise
look paradoxical: at finite $N$, the algebra of operators on one Cauchy slice determines the algebra
everywhere (the time-slice axiom, eq.~4.56, from Sec.~IV.D.3) — ordinary causal time evolution lets you
reconstruct operators at any other time from data on one slice. In the strict $N\to\infty$ limit, this stops
being true: the boundary field theory becomes a **generalized free field** (a Gaussian field specified
purely by its two-point function, with *emph* equation of motion governing its time evolution at all), and
algebras built on different Cauchy slices become genuinely inequivalent (Fig.~8 of the paper).

The reason traces directly to how the boundary Hamiltonian scales with $N$. The stress tensor has the schematic
form $T^{\mu\nu}=N\Tr(\cdots)$ (eq.~6.18 — an overall factor of $N$, from the trace running over an
$N$-dimensional gauge index), so the ordinary boundary Hamiltonian $H=\int d^{d-1}x\,T^{00}$ (eq.~6.17) simply
does not have a finite $N\to\infty$ limit in any sector — it diverges. The *emph* versions,
$\widehat T^{\mu\nu}\equiv T^{\mu\nu}/N$ and $\widehat H\equiv H/N$ (eq.~6.19), do survive the limit — but they
generate only an infinitesimally slow flow, $i[\widehat H,O(x)]=\tfrac1N\partial_tO(x)$ (eq.~6.20): a genuine
time translation on single-trace operators requires the full, non-rescaled $H$, which doesn't exist in the
limit. **Ordinary time translation, generated by an integral of a local density over one Cauchy slice,
simply does not survive the large-$N$ limit.** This is not a contradiction with the fact that semiclassical
states like the vacuum obviously do have time-translation symmetry — there does exist, within a given sector,
a genuine time-translation operator $\hat h_\Psi$ satisfying $i[\hat h_\Psi,O(x)]=\partial_tO(x)$ (eq.~6.21) —
but $\hat h_\Psi$ cannot be written as the integral of a local operator over a single time slice the way $H$
was. The next subsection (the vacuum sector) makes this completely explicit and constructs $\hat h_\Omega$ by
hand. (Exactly the same phenomenon applies to any global symmetry, not just time translation — picked back up
in Sec.~VI.F below for an internal $U(1)$ charge.)

## Sec.~VI.B: the vacuum sector

Here every piece of the general story above can be made completely explicit and checked directly, because
the vacuum sector is the one case where both sides of the duality are known in closed form. The vacuum
$\ket\Omega$ is dual to empty global AdS (eq.~6.22), with bulk vacuum $\ket0_{\text{AdS}}\in
\HH_{\text{AdS}}^{\text{Fock}}$; a bulk field has the ordinary mode expansion $\phi(X)=\sum_k(u_k(X)a_k+
u_k^*(X)a_k^\dagger)$ with $a_k\ket0_{\text{AdS}}=0$ (eq.~6.24), and $\HH_{\text{AdS}}^{\text{Fock}}$ is built by
acting with creation operators $a_k^\dagger$ on the vacuum, exactly the way you'd build any ordinary Fock
space.

On the boundary, vacuum correlators of single-trace operators have the standard large-$N$ scaling,
$\braket{O}=0$, $\braket{O_1O_2}_c\sim O(N^0)$, $\braket{O_1\cdots O_n}_c\sim N^{2-n}$ (eq.~6.25) — so at
leading order, every higher correlator factorizes into a sum over products of two-point functions (eq.~6.26),
exactly the Gaussian/generalized-free-field structure eq.~6.15 demanded. Each single-trace operator behaves
like a genuine generalized free field, so $\HH_\Omega^{\text{GNS}}$ has the required Fock-space structure, and
in fact $B(\HH_\Omega^{\text{GNS}})=(\pi_\Omega(\Sscr))''$ (eq.~6.27) — meaning $\omega_\Omega$ is a
*emph* state with respect to $\Sscr$, and $\Sscr=\Alg_\Omega$: single-trace operators are all there is in
the vacuum sector, with nothing extra surviving the large-$N$ limit.

### Worked calculation: matrix Wick contractions and large-$N$ factorization

To see precisely how large-$N$ factorization produces a free Fock algebra from an interacting matrix theory, let us work out the index contractions for an $N\times N$ hermitian matrix field $M_{ij}(x)$ with Gaussian propagator:

$$

\braket{M_{ij}(x) M_{kl}(y)}_0 = \delta_{il}\delta_{jk} G(x,y)

$$

where $G(x,y)$ is the scalar two-point function. Define the gauge-invariant, normalized single-trace operator:

$$

\mathcal{O}(x) \equiv \frac{1}{N} \Tr\big(M(x)^2\big) = \frac{1}{N} \sum_{i,j=1}^N M_{ij}(x) M_{ji}(x)

$$

Let us evaluate the two-point correlator $\braket{\mathcal{O}(x) \mathcal{O}(y)}_0$:

$$

\braket{\mathcal{O}(x)\mathcal{O}(y)}_0 = \frac{1}{N^2}\sum_{i,j,k,l=1}^N \braket{M_{ij}(x) M_{ji}(x) M_{kl}(y) M_{lk}(y)}_0

$$

By Wick's theorem, the contractions between $M(x)$ and $M(y)$ are:

1. Contract $M_{ij}(x)$ with $M_{kl}(y)$ and $M_{ji}(x)$ with $M_{lk}(y)$:

$$

\braket{M_{ij}(x)M_{kl}(y)}_0 \braket{M_{ji}(x)M_{lk}(y)}_0 = (\delta_{il}\delta_{jk} G(x,y))(\delta_{jk}\delta_{il} G(x,y)) = \delta_{il}\delta_{jk} G(x,y)^2

$$

Summing over all 4 indices gives:

$$

\sum_{i,j,k,l} \delta_{il}\delta_{jk} = \sum_{i,j=1}^N 1 = N^2

$$

2. Contract $M_{ij}(x)$ with $M_{lk}(y)$ and $M_{ji}(x)$ with $M_{kl}(y)$:

$$

\braket{M_{ij}(x)M_{lk}(y)}_0 \braket{M_{ji}(x)M_{kl}(y)}_0 = (\delta_{ik}\delta_{jl} G(x,y))(\delta_{jl}\delta_{ik} G(x,y)) = \delta_{ik}\delta_{jl} G(x,y)^2

$$

Summing over indices gives $\sum_{i,j} 1 = N^2$.

Multiplying by the normalization $\frac{1}{N^2}$:

$$

\braket{\mathcal{O}(x)\mathcal{O}(y)}_0 = \frac{1}{N^2}\Big(N^2 G(x,y)^2 + N^2 G(x,y)^2\Big) = 2\,G(x,y)^2 \sim O(N^0)

$$

Now consider the four-point function $\braket{\mathcal{O}(x_1)\mathcal{O}(x_2)\mathcal{O}(x_3)\mathcal{O}(x_4)}_0$. The contractions split into two classes:

- **Disconnected contractions** (pairwise contractions between single traces, e.g. $\mathcal{O}_1$ with $\mathcal{O}_2$ and $\mathcal{O}_3$ with $\mathcal{O}_4$):

$$

\braket{\mathcal{O}(x_1)\mathcal{O}(x_2)}_0 \braket{\mathcal{O}(x_3)\mathcal{O}(x_4)}_0 = \big(2 G(x_1,x_2)^2\big)\big(2 G(x_3,x_4)^2\big) \sim O(N^0)

$$

There are 3 such pairings: $(12)(34) + (13)(24) + (14)(23)$.
- **Connected contractions** (cyclic contractions linking all 4 operators in a single loop, e.g. $M(x_1) \to M(x_2) \to M(x_3) \to M(x_4) \to M(x_1)$):
The index chain gives a single index summation $\sum_i \delta_{ii} = N$. With four normalization prefactors of $1/N$, the connected four-point amplitude scales as:

$$

\braket{\mathcal{O}(x_1)\mathcal{O}(x_2)\mathcal{O}(x_3)\mathcal{O}(x_4)}_c \sim \frac{1}{N^4} \times N = \frac{1}{N^3} \to 0

$$

Even in the presence of planar gauge interactions (with 't~Hooft coupling $\lambda = g_{\text{YM}}^2 N$), planar connected diagrams scale as $\braket{\mathcal{O}_1\cdots\mathcal{O}_n}_c \sim N^{2-n}$. For $n=4$, this gives $\sim O(1/N^2)$.

Thus, at strictly $N\to\infty$:

$$

\braket{\mathcal{O}(x_1)\mathcal{O}(x_2)\mathcal{O}(x_3)\mathcal{O}(x_4)}_0 = \braket{\mathcal{O}_1\mathcal{O}_2}_0\braket{\mathcal{O}_3\mathcal{O}_4}_0 + \braket{\mathcal{O}_1\mathcal{O}_3}_0\braket{\mathcal{O}_2\mathcal{O}_4}_0 + \braket{\mathcal{O}_1\mathcal{O}_4}_0\braket{\mathcal{O}_2\mathcal{O}_3}_0 + O(1/N^2)

$$

Connected $n$-point correlators vanish for all $n \ge 3$. This proves that the single-trace operators satisfy Wick's theorem identically, generating an exact free generalized field Fock space $\HH_\Omega^{\text{GNS}}$.

The correspondence between bulk and boundary mode expansions can be made completely explicit: expanding a
single-trace operator directly on the GNS Hilbert space, $\pi_\Omega(O(x))=\sum_k(v_k(x)b_k+v_k^*(x)b_k^\dagger)$
with $b_k\ket1_\Omega=0$ (eq.~6.28), matching the boundary basis functions to the boundary limit of the bulk
ones, $v_k(x)=\lim_{r\to\infty}r^\Delta u_k(X)$ (eq.~6.29), and the extrapolate dictionary (eq.~6.6) then
forces the mode operators to be identified directly, $a_k=b_k$ (eq.~6.30) — establishing eq.~6.15 completely
explicitly in this one solvable case. Rewritten in position space, this identification becomes

$$

\phi(X) = \int d^dx\,K(X;x)\,\pi_\Omega(O(x))

$$

(eq.~6.32), the celebrated **global HKLL construction**: an explicit kernel $K$ that reconstructs the bulk
field everywhere in AdS directly from boundary single-trace operator data.

### Worked derivation: the HKLL smearing kernel in \texorpdfstring{$\text{AdS_3$}{AdS3}}

To make the HKLL kernel $K(X;x)$ fully concrete, consider a free massless scalar field $\phi(z,t,x)$ in Poincaré $\text{AdS}_3$ with metric:

$$

ds^2 = \frac{R^2}{z^2}\big(dz^2 - dt^2 + dx^2\big), \qquad z > 0

$$

The bulk Klein—Gordon equation $(\Box - m^2)\phi = 0$ for $m^2=0$ ($\Delta = 2$) reads:

$$

z^3 \partial_z \left(\frac{1}{z}\partial_z \phi\right) - \partial_t^2 \phi + \partial_x^2 \phi = \partial_z^2 \phi - \frac{1}{z}\partial_z \phi - \partial_t^2 \phi + \partial_x^2 \phi = 0

$$

In Fourier space with boundary momentum $(\omega, k)$ such that $\omega^2 - k^2 \equiv q^2 > 0$ (timelike momentum), the mode equation for $\phi(z,t,x) = f(z) e^{-i\omega t + ikx}$ is:

$$

f''(z) - \frac{1}{z} f'(z) + q^2 f(z) = 0

$$

Setting $f(z) = z g(z)$ converts this to Bessel's equation of order 1 for $g(z)$:

$$

g''(z) + \frac{1}{z} g'(z) + \left(q^2 - \frac{1}{z^2}\right)g(z) = 0 \implies f(z) = C\, z J_1(q z)

$$

Near the boundary $z \to 0$, $J_1(qz) \approx \frac{qz}{2}$, so $f(z) \approx C \frac{q}{2} z^2$. The extrapolate dictionary requires $\lim_{z\to 0} z^{-2} \phi(z,t,x) = \mathcal{O}(t,x) = e^{-i\omega t + ikx}$, fixing $C = \frac{2}{q}$. Hence:

$$

\phi(z,t,x) = \frac{2 z}{q} J_1(q z) \mathcal{O}(t,x)

$$

Using the integral representation of the Bessel function $J_1(qz) = \frac{q z}{\pi} \int_{-1}^1 dt' \sqrt{1 - t'^2}\, e^{-i q z t'}$, the bulk field can be transformed back into position space as a convolution over the boundary domain:

$$

\phi(z,t,x) = \frac{1}{2\pi} \int_{t'^2 + x'^2 < z^2} dt' dx' \, \mathcal{O}\big(t + t',\, x + i x'\big)

$$

or equivalently using real spacelike boundary smearing:

$$

\phi(z,t,x) = \frac{1}{\pi} \int_{x'^2 - t'^2 < z^2} dt' dx' \, \frac{\theta(z^2 - x'^2 + t'^2)}{\sqrt{z^2 - x'^2 + t'^2}}\, \mathcal{O}\big(t + t',\, x + x'\big)

$$

Notice the remarkable physical property of this formula: evaluating the local bulk operator $\phi(z,t,x)$ at radial depth $z$ requires integrating the boundary operator $\mathcal{O}$ over a spatial disk of radius $z$. The deeper the operator is in the bulk (larger $z$), the larger the boundary region needed to reconstruct it — a direct manifestation of the holographic UV/IR relation!

And — a genuinely striking, easy to underappreciate fact worth stating plainly — because the boundary conformal representation has evenly-spaced
energy levels (spacing $2$, a standard fact about CFT representation theory), it can be shown that

$$

B(\HH_\Omega^{\text{GNS}}) = Y_{I_w}, \qquad w\ge\pi R

$$

(eq.~6.33), where $I_w$ is a boundary time band of width $w$: **the entire bulk vacuum sector's operator
content — every bulk field, everywhere in AdS — is already fully generated by boundary operators smeared
over a time band of width just $\pi R$, no wider.** You do not need the whole boundary history, an infinite
band, or even more than half the natural period — a finite window of boundary time is already enough to
reconstruct the entire bulk. This is worth remembering as the single cleanest, most concrete preview of
subregion-subalgebra duality, which Sec.~VII develops as the paper's central general principle.

Finally, the vacuum-sector time-translation operator $\hat h_\Omega$ promised in Sec.~VI.A above can be
written down explicitly, as the bulk energy integral $\hat h_\Omega=\int d\rho\,d^{d-1}\Omega\,\rho^{d-1}
T_{tt}$ over a Cauchy slice (eq.~6.34, with $T_{tt}$ the bulk stress tensor, quadratic in $\phi$ at this order)
— substituting the mode expansion (eq.~6.24) and using $a_k=b_k$ turns this directly into a specific quadratic
expression in boundary single-trace operators, exactly the promised $\hat h_\Omega$ satisfying
eq.~6.21 — and, consistent with eq.~6.33, it necessarily involves integrating boundary operators over a time
band of width $\pi R$, not a single instant.

## Sec.~VI.C: thermofield double state

### Setup, and the Hawking—Page transition

Take two copies of the boundary CFT, $\text{CFT}_R$ and $\text{CFT}_L$, and build the **thermofield
double** (TFD) state at finite $N$,

$$

\ket{\Psi_\beta} = \frac{1}{\sqrt{Z_\beta}}\sum_n e^{-\beta E_n/2}\ket n_R\ket{\Theta n}_L, \qquad
Z_\beta=\sum_n e^{-\beta E_n}

$$

(eq.~6.35, with $\Theta$ the CRT operator — needed to correctly match energy eigenstates across the two
copies). Tracing out $L$ gives the ordinary thermal density matrix $\rho_\beta=\tfrac1{Z_\beta}e^{-\beta H_R}$
on $R$ — this is exactly the finite-dimensional worked example from Sec.~IV.A of this companion, applied now
to a genuine field theory: $B(\HH_R)$ is type I, $\ket{\Psi_\beta}$ is cyclic and separating for it, and the
modular operator is exactly $-\log\Delta_\beta=\beta(H_R-H_L)$ (eq.~6.36) — literally the same
$\Delta_\Psi=\rho_R\otimes\rho_L^{-1}$ formula from Sec.~IV.A, with $\rho_R=e^{-\beta H_R}/Z_\beta$.

In the large-$N$ limit, this system undergoes a genuine first-order phase transition at the
**Hawking—Page temperature** $T_{\text{HP}}$: the free energy jumps discontinuously in its $N$-scaling,
from $O(N^0)$ below $T_{\text{HP}}$ to $O(N^2)$ above it, and the dual bulk geometry correspondingly jumps
from *emph* (a thermal gas of particles in ordinary global AdS, with no black hole at all) to a
genuine *emph*.

**Below $T_{\text{HP**}$}: energies contributing to the sum in eq.~6.35 stay of order $O(N^0)$ (higher
energies are Boltzmann-suppressed), so in the large-$N$ limit these states live entirely within the ordinary
vacuum-sector GNS Hilbert spaces $\HH_\Omega^R,\HH_\Omega^L$ already constructed in Sec.~VI.B. The GNS Hilbert
space built from $\ket{\Psi_\beta}$ genuinely factorizes, $\HH_{\Psi_\beta}^{\text{GNS}}=\HH_\Omega^R\otimes
\HH_\Omega^L$ (eq.~6.39), and correspondingly $Y_R=B(\HH_\Omega^R)$, $Y_L=B(\HH_\Omega^L)$ (eq.~6.41) —
**$Y_R$ remains type I**. The bulk dual is exactly two separate, unentangled-with-each-other-except-via-
the-state copies of global AdS glued together by the TFD's entanglement pattern (eq.~6.37, Fig.~9(a)) — a
completely disconnected bulk geometry.

**Above $T_{\text{HP**}$}: now the thermal ensemble is dominated by states of energy $O(N^2)$, and the
naive finite-$N$ sum (eq.~6.35) becomes ill-defined as $N\to\infty$ — neither the energies nor the
corresponding eigenstates have a sensible limit, and in fact a single-trace operator's one-point function in
this state actually *emph*, $\braket{\Psi_\beta|O|\Psi_\beta}\sim O(N)$ (eq.~6.43). The fix: work with
"renormalized," mean-subtracted operators $\widehat O\equiv O-\braket{\Psi_\beta|O|\Psi_\beta}$ (eq.~6.44),
whose connected correlators do have sensible, $O(N^0)$, large-$N$ limits (eq.~6.45), and which again satisfy
the large-$N$ factorization property. This produces a perfectly good GNS Hilbert space and a Fock-space
structure, and the resulting algebras $Y_R\equiv(\pi_{\Psi_\beta}(\Sscr_\beta^{(R)}))''$ satisfy $Y_R'=Y_L$
(eq.~6.47) — but now, because the entanglement between $\text{CFT}_R$ and $\text{CFT}_L$ has jumped to order
$O(N^2)$, it has been argued that **$Y_R$ becomes type $\mathrm{III**_1$}, and
$\HH_{\Psi_\beta}^{\text{GNS}}$ no longer factorizes into separate $R$ and $L$ pieces at all. On the gravity
side, this matches the eternal-black-hole geometry (eq.~6.38, Fig.~9(b)) exactly, with $Y_R,Y_L$ identified
with the bulk exterior algebras $\widetilde\M_R,\widetilde\M_L$ (eq.~6.49) — themselves type
$\mathrm{III}_1$ simply because they're the algebras of subregions of an ordinary continuum quantum field
theory, exactly Sec.~IV.D's local-algebra story.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.72\textwidth]{figs/fig_penrose.pdf}
\caption{Penrose diagram of the two-sided eternal AdS black hole dual to the Thermofield Double state $\ket{\Psi_\beta}$. The right ($R$) and left ($L$) exterior wedges are causally disconnected and bounded by the event horizons (dashed red lines), connected in the interior by an Einstein—Rosen bridge (wormhole) between the past ($P$) and future ($F$) curvature singularities (zigzag lines).}
\label{fig:penrose}
\end{figure}

### Two puzzles, and how algebra resolves the first of them

Before this algebraic reformulation existed, the identification of the $T>T_{\text{HP}}$ phase with an eternal
black hole — despite passing every quantitative check imaginable — carried two nagging conceptual puzzles,
worth stating precisely because they're genuinely old, well-known tensions in the holography literature, not
inventions of this paper.

**The factorization puzzle.** The boundary theory manifestly factorizes as $\text{CFT}_R\otimes
\text{CFT}_L$ (it's just two separate, non-interacting copies of the same CFT). But the bulk black hole is a
single, *emph* spacetime — and there exist genuine bulk operators, like a Wilson line stretching all
the way from the left boundary to the right through the interior (Fig.~9(b)), that stubbornly refuse to be
written as any product of an operator in $B(\HH_R)$ and one in $B(\HH_L)$. How can a connected bulk object
correspond to anything in a manifestly disconnected boundary tensor product?

**The meeting-behind-the-horizon puzzle.** There's no interaction term at all between $\text{CFT}_R$ and
$\text{CFT}_L$ (the total Hamiltonian is simply $H_R+H_L$, no cross term) — and yet bulk degrees of freedom
that originate separately in the $R$ and $L$ exterior regions can cross the horizon and genuinely interact
with each other in the interior region behind it (Fig.~9(b), arrows). How can two causally, dynamically
disconnected boundary theories produce bulk physics that isn't disconnected at all, once you look behind the
horizon?

This section resolves the *emph* puzzle directly: the answer is simply that "$B(\HH_R)$" is the wrong
object to be comparing to the bulk exterior algebra in the first place, once you take $N\to\infty$ seriously.
$Y_R$ — the actual, large-$N$ limit of the algebra — is type $\mathrm{III}_1$, not type I, precisely because
of the $O(N^2)$ entanglement between $R$ and $L$; and a type $\mathrm{III}_1$ algebra, unlike an ordinary type I
tensor factor, has no obstruction whatsoever to containing operators (like the boundary avatar of that Wilson
line) that aren't literally factorized products of an $R$-piece and an $L$-piece — nothing about $Y_R\otimes
Y_L$ sitting inside $B(\HH^{\text{GNS}})$ the way an ordinary tensor product would. The apparent contradiction
was an artifact of insisting, wrongly, on ordinary type I tensor-product intuition in a regime where the
algebra has already become type $\mathrm{III}_1$. (The second puzzle — meeting behind the horizon — needs
genuinely more machinery, specifically the emergent commutant and half-sided-modular-inclusion structure of
Sec.~IV.E, and is deferred explicitly to Sec.~VIII.B, where the bulk causal structure of the eternal black hole
is built directly from boundary algebra data.)

A further remark worth keeping, because it becomes the seed of algebraic ER$=$EPR in Sec.~VIII.C: the entire
qualitative conclusion here — disconnected bulk geometry below $T_{\text{HP}}$, connected black hole above it
— could, in principle, have been *emph* purely from watching $Y_R$ jump from type I to type
$\mathrm{III}_1$, with no independent knowledge of the bulk geometry needed at all. Also worth noting: for
$T>T_{\text{HP}}$, different temperatures $\beta$ genuinely live in different, non-overlapping GNS sectors
(their entanglement entropies differ by $O(N^2)$, an infinite barrier in the strict limit — exactly Sec.~I's
mechanism again), whereas below $T_{\text{HP}}$, every $\beta$ shares one common GNS Hilbert space, with the
different TFD states just being different vectors inside it. And even though the ordinary Hamiltonians
$H_R,H_L$ don't survive the large-$N$ limit as elements of the algebra (eq.~6.36 stops literally holding), the
modular operator $\Delta_\beta$ itself *emph* survive, continuing to generate boundary time translation
in opposite directions on the two sides — factorizing as $-\log\Delta_\beta=\beta(\hat h_R-\hat h_L)$
(eq.~6.52, with $\hat h$ the bulk vacuum-sector time-translation operator from Sec.~VI.B) below
$T_{\text{HP}}$, but failing to factorize at all above it — exactly tracking the type I $\to$ type
$\mathrm{III}_1$ transition.

## Sec.~VI.D: general black holes

The thermofield double is special: it has an exact, bifurcating (perfectly symmetric) horizon. A more generic
two-sided semiclassical state $\ket\Psi$, dual to a "long" black hole (Fig.~10 — a black hole with a genuine
interior region $I$ separating $R$ and $L$, not meeting at a single bifurcation point), makes visible exactly
the subtlety flagged back in Sec.~VI.A: the inclusion $\Sscr\subseteq\Alg_\Psi$ can now be genuinely
*emph*. The renormalized single-trace algebras still correctly reproduce the bulk exterior algebras,
$Y_R=\widetilde\M_R$, $Y_L=\widetilde\M_L$ (eq.~6.53) — but $R$ and $L$ together no longer cover a full Cauchy
slice, leaving the interior region $I$ genuinely missing. Bulk operators living in $I$ must still correspond to
*emph* boundary operators surviving the large-$N$ limit (since they're part of the same physical bulk
field as the exterior operators, just evaluated at a different location) — but those operators are not
single-trace operators; they must belong to $\Alg_\Psi\setminus\Sscr$. Sec.~VII.B identifies exactly what
these extra operators are: they turn out to be generated from single-trace operators using *emph* — precisely the mechanism already previewed in Sec.~IV.A's ergodic lemma (a modular flow, run long
enough, regenerates an entire larger algebra starting from a smaller subalgebra).

The same phenomenon — extra, non-single-trace operators needed for a black hole interior — occurs for a
"long" one-sided black hole too (Fig.~11(a)). But a one-sided black hole formed by ordinary gravitational
collapse (Fig.~11(b), matter falling in from empty space) is different, and worth flagging as a genuine
contrast to keep in mind heading into Sec.~VII.E: there, it turns out $\Alg_\Psi=\Sscr$ exactly — single-trace
operators are already everything, with nothing extra needed at all.

## Sec.~VI.E: a diagnostic of firewalls in generic highly excited states

Now consider a completely generic, highly excited state $\ket\Psi$ with energy $E_\Psi\sim O(N^2)$ — no
assumption that it was engineered to have a nice bulk dual, just an arbitrary state of that energy. The
boundary theory at such energies is expected to be chaotic, and a typical state of that energy should look
thermal to any single-trace-operator probe, to leading order in $1/N$:

$$

\braket{\Psi|O|\Psi}\approx\braket{O}_\beta, \qquad \braket{\Psi|O_1\cdots O_n|\Psi}\approx\braket{O_1\cdots
O_n}_\beta

$$

(eq.~6.55, with $\beta$ fixed by matching the energy, $E_\Psi=E_\beta$) — this is the ordinary
eigenstate-thermalization-hypothesis-style statement that a single generic high-energy state reproduces
thermal correlators, and it says $\Psi$ looks, to single-trace operators, exactly like it has a smooth black
hole exterior. But does it also have a smooth *emph* — a genuine continuation of the geometry behind
the horizon, as in Fig.~11 — or does the interior geometry simply fail to exist, a **firewall**?

Sec.~VI.D already established the criterion needed to answer this: a smooth interior requires operators
surviving the large-$N$ limit *emph* single-trace operators, i.e.\ $\Sscr\subsetneq\Alg_\Psi$. This
gives a clean, checkable diagnostic, stated as sharply as the paper states it: **if a generic highly
excited state satisfies the thermal correlator condition (eq.~6.55) and *emph* In this case, $\omega_\Psi$ is a *emph* state with respect to $\Alg_\Psi$, violating the
purity condition (eq.~6.10) assumed back in Sec.~VI.A for the "nice" semiclassical case. An analogous
statement for two-sided generic states adds one more condition: correlations between the two sides must
genuinely vanish, $\braket{\Psi|O_RO_L|\Psi}_c\to0$ as $N\to\infty$ (eq.~6.56) — consistent with there being no
smooth, connected bridge between the two boundaries at all in that case.

## Sec.~VI.F: perturbative $1/N$ corrections

### Corrections to bulk reconstruction

Everything so far worked at strictly leading order in $G_N$ (equivalently $1/N$). Including subleading orders
makes the bulk field theory genuinely interacting (the $\kappa S_3+\kappa^2S_4+\cdots$ terms of eq.~6.14 switch
back on), and correspondingly the boundary theory develops nonzero three- and higher-point functions,
suppressed by powers of $1/N$. One immediate, checkable consequence: the clean HKLL formula (eq.~6.32) that
worked perfectly at leading order gets corrected. Solving the interacting bulk equation of motion perturbatively
in $\kappa$ (eqs.~6.57—6.61, for the simplest case of a cubic self-interaction $\phi^3$) produces extra terms
in the bulk-to-boundary map order by order,

$$

\phi(X) = \int d^dx\,K(X;x)\,O^{(0)}(x) + \kappa\int d^dx_1d^dx_2\,K(X;x_1,x_2)\,O^{(0)}(x_1)O^{(0)}(x_2)
+ \cdots

$$

(eq.~6.62) — the leading-order reconstruction picks up multi-trace corrections, one extra factor of a
single-trace operator per order in $1/N$. This is worth knowing exists (it's the technical underpinning of
"$1/N$ corrections to bulk locality," a substantial research topic on its own) without needing to track every
term; the important structural point, stated explicitly in the paper (and worth remembering for everything
downstream): to any finite order in the $1/N$ expansion, the leading-order *emph* of every algebra
discussed above stays exactly the same, because the spectrum of the modular operator is dominated by its
zeroth-order piece — perturbation theory in $1/N$ never changes an algebra's type; only the strict
$N\to\infty$ limit itself can do that.

### Conserved charges, and where gravitational dressing first appears

The second new feature is more conceptually important for everything from Sec.~IX onward, so it's worth
spending real time on it. Suppose the boundary CFT has a global $U(1)$ symmetry, with conserved charge
$\widehat Q\equiv Q/N$ (rescaled exactly the way $\widehat H=H/N$ was, since the current itself scales as
$N\Tr(\cdots)$, eq.~6.68). Acting on a single-trace operator of unit charge, $i[\widehat Q,O(x)]=\tfrac1N O(x)$
(eq.~6.69) — the charge-rotation action is suppressed by $1/N$, exactly mirroring the time-translation story
of Sec.~VI.A. Within a given sector there's again a genuine large-$N$ operator $\hat q$ generating the full
rotation, $i[\hat q,O(x)]=O(x)$ (eq.~6.70), that (exactly like $\hat h_\Omega$ before it) cannot be written as
an integral of a local density on a single time slice.

The bulk dual of this boundary global $U(1)$ symmetry is a bulk $U(1)$ *emph* symmetry, and here is
where something genuinely new, and physically important, shows up once $1/N$ corrections are included: the
suppressed commutator eq.~6.69, translated to the bulk via the extrapolate dictionary, forces the bulk gauge
field strength and a charged bulk scalar to have a *emph*
(eq.~6.72) — an explicit, checkable violation of bulk microcausality, order by order in $1/N$, tied directly
to the bulk Gauss-law constraint (the equation of motion $\nabla_MF^{MN}=\kappa J^N$, eq.~6.75, ties the gauge
field's behavior at one point to charge located anywhere else on the same Cauchy slice, since Gauss's law is
intrinsically nonlocal). The resolution, worth knowing because it reappears as the central mechanism of
Sec.~IX: a bulk charged field $\phi(z,x)$ is not, by itself, gauge invariant; a genuinely gauge-invariant
operator has to be built by attaching a **Wilson line** running out to the boundary,

$$

\Phi(z,x) = e^{-i\kappa V}\phi(z,x), \qquad V=\int_0^z dz'\,A_z(z',x)

$$

(eq.~6.77) — a **dressed observable**, and it's precisely the inherent nonlocality of that Wilson line
(it depends on the gauge field along an entire path, not just at one point) that produces the nonlocal
commutation relations eq.~6.72 directly, with no mystery left over.

### Worked calculation: Gauss's law and the dressed operator commutator

To see this mechanism explicitly at the level of canonical quantization, consider the bulk gauge field $A_M = (A_t, A_z, A_x)$ in $A_t = 0$ gauge on a constant-time Cauchy slice. The conjugate momentum to $A_z(z,x)$ is the electric field $E^z(z,x) = F^{zt}(z,x) = \partial_t A_z - \partial_z A_t$. The canonical commutation relation is:

$$

\big[A_z(z',x'),\, F^{zt}(z'',x'')\big] = i\,\delta(z'-z'')\,\delta(x'-x'')

$$

Bulk Gauss's law on a state containing a local charged particle $\phi(z,x)$ of unit charge $q=1$ at position $(z,x)$ requires:

$$

\nabla_M F^{Mt} = \partial_{z''} F^{zt}(z'',x'') + \partial_{x''} F^{xt}(z'',x'') = \kappa\, J^t(z'',x'') = \kappa\,\delta(z''-z)\,\delta(x''-x)

$$

If we take the naive, undressed field $\phi(z,x)$, it commutes with the gauge field: $[\phi(z,x), F^{zt}(z'',x'')] = 0$. But this leads to an immediate contradiction: taking the spatial derivative $\partial_{z''}$ yields zero, violating Gauss's law because the charge density is nonzero!

Now evaluate the commutator using the gauge-invariant, dressed operator $\Phi(z,x) = e^{-i\kappa V(z,x)}\phi(z,x)$ with $V(z,x) = \int_0^z dz' A_z(z',x)$:
\begin{align*}
\big[\Phi(z,x),\, F^{zt}(z'',x'')\big] &= \Big[e^{-i\kappa \int_0^z dz' A_z(z',x)},\, F^{zt}(z'',x'')\Big]\,\phi(z,x) \\
&= -i\kappa \left(\int_0^z dz' \big[A_z(z',x),\, F^{zt}(z'',x'')\big]\right) \Phi(z,x) \\
&= -i\kappa \left(\int_0^z dz' \, i\,\delta(z'-z'')\,\delta(x-x'')\right) \Phi(z,x) \\
&= \kappa\,\theta(z - z'')\,\delta(x - x'')\,\Phi(z,x)
\end{align*}
where $\theta(z - z'')$ is the step function ($1$ for $0 < z'' < z$, and $0$ for $z'' > z$).
Now compute the divergence of this commutator with respect to the coordinate $z''$:

$$

\partial_{z''} \big[\Phi(z,x),\, F^{zt}(z'',x'')\big] = \kappa \frac{d}{dz''}\theta(z - z'')\,\delta(x - x'')\,\Phi(z,x) = -\kappa\,\delta(z'' - z)\,\delta(x'' - x)\,\Phi(z,x)

$$

Gauss's law is now satisfied identically as an operator equation!
Notice that for any point $z'' < z$ along the string running from the boundary to the insertion point, the commutator is non-vanishing even at spacelike separation. The non-local string of the Wilson line is the physical cost of gauge invariance.

Exactly the same story holds for
spacetime symmetries instead of an internal $U(1)$: dressing a bulk operator to the boundary using a
*emph* Wilson line (or, equivalently, working in a specific gauge and solving the constraint
directly, mirroring eqs.~6.75—6.78) is required to make it diffeomorphism-invariant, and produces an
analogous $1/N$ correction to the rescaled Hamiltonian, $\widehat H=\widehat H^{(0)}+\tfrac1N\hat h_\Omega+
\cdots$ (eq.~6.80). **This is the very first appearance, in perturbation theory, of the exact mechanism
that Sec.~IX turns into an exact, nonperturbative construction**: gravitationally dressing an operator to a
physical reference (a Wilson line here; an observer's own clock, via the crossed product of Sec.~V, there) is
what makes it a genuine, gauge-invariant, physical observable — and it is not optional decoration, but is
forced directly by the bulk Gauss-law constraint that any theory of gravity or gauge fields must satisfy.

\bigskip
\noindent With the large-$N$ algebraic structure of AdS/CFT now built — semiclassical states as GNS sectors,
single-trace algebras $Y_O$, the type transition tracking Hawking—Page, and gravitational dressing already
visible in perturbation theory — Sec.~VII assembles all of this into the paper's central physical claim:
**subregion-subalgebra duality**, the statement that an arbitrary bulk causal region is identical, not
merely related, to a specific emergent boundary operator subalgebra.



---

# Sec.~VII: Subregion-subalgebra duality

This is the section the paper's title is named for, and everything in Secs.~II—VI was, in one way or another,
building toward it. The claim is simple to state and enormous in consequence: **an arbitrary bulk
spacetime region, in the strict large-$N$ limit, is not merely *emph* one.} Not approximately, not up to some correction: the bulk region and the
boundary algebra are two names for the same mathematical object, described in two different languages.

## Sec.~VII.A: general formulation

### Where the identification comes from

Recall from Sec.~VI.A that eq.~6.15 identified the bulk Fock space (built by ordinary quantization of small
fluctuations around a classical background) with the boundary GNS Hilbert space (built from the algebra of
operators surviving the large-$N$ limit, via GNS). Since these are literally the same Hilbert space, their
full operator algebras must coincide too:

$$

B(\HH_\Psi^{\text{Fock}}) = B(\HH_\Psi^{\text{GNS}})

$$

(eq.~7.1). It's worth noticing something a little surprising buried in this equation: $B(\HH_\Psi^{\text{Fock}})$
is naturally built from data on a single bulk Cauchy slice (ordinary canonical quantization only ever needs
one moment of time), while $B(\HH_\Psi^{\text{GNS}})$ is built from the entire boundary spacetime (or, per
eq.~6.33 of Sec.~VI.B, at least a finite time band). These look like they should be different-sized objects —
and they're reconciled by the fact that the bulk has one more spatial dimension than the boundary: a whole
extra dimension's worth of bulk data, spread across one Cauchy slice, is exactly matched by a chunk of
boundary *emph*, not boundary space. This is already a first hint of the general phenomenon Sec.~VIII
develops in full: boundary time and bulk radial position are intimately linked.

At the free (quadratic) level, different bulk fields decouple from each other entirely, so both the Hilbert
space and its algebra of operators split into independent tensor factors, one per field species $i$:
$\HH_\Psi^{\text{GNS}}=\bigotimes_i\HH_{\Psi,i}^{\text{GNS}}$, with $\HH_{\Psi,i}^{\text{Fock}}=
\HH_{\Psi,i}^{\text{GNS}}$ field by field (eqs.~7.2—7.3) — nothing conceptually new here, just bookkeeping
that the identification holds mode by mode, not just for the whole theory at once.

### The duality, stated precisely

Because eq.~7.1 is an identity of entire operator algebras, it must hold subalgebra by subalgebra too: take
any open bulk subregion $b$ on a Cauchy slice, with its associated bulk operator algebra $\widetilde\M_b
\subset B(\HH_\Psi^{\text{Fock}})$ (bulk algebras are written with a tilde throughout this section, to keep
them visually distinct from boundary algebras). There must be a corresponding boundary subalgebra $\M_b
\subset B(\HH_\Psi^{\text{GNS}})$ identified with it:

$$

\widetilde\M_b = \M_b

$$

(eq.~7.4). Read this the way you'd read $\M=\mathcal M$ in ordinary mathematics, not as an analogy or a
correspondence of properties — it's a literal identity of two descriptions of one mathematical object.
Because $\M_b$ (via the general Sec.~IV.D dictionary — causal structure, entanglement, modular flow) encodes
everything about the algebra's causal, geometric, and entanglement structure, and $\M_b=\widetilde\M_b$
identically, **$\M_b$ already encodes everything about the bulk region $b$'s geometry too** — where the
modular operator of $\widetilde\M_b$ (hence the entanglement structure of $b$ with its complement) is exactly
the modular operator of $\M_b$, computable purely from boundary data. **This is why a bulk region can be
fully "reconstructed" from the corresponding boundary algebra** — this is subregion-subalgebra duality, and
you've already seen two special cases of it without the general name attached: the black-hole exterior
identifications of Sec.~VI.C—D (eqs.~6.49, 6.53) are exactly eq.~7.4 with $b$ taken to be the entire exterior
region.

Because $\widetilde\M_b$ is a genuine local algebra of an (effectively free, at this order) bulk quantum field
theory, it inherits every structural property established for such algebras back in Sec.~IV.D — and by
eq.~7.4, so does the boundary algebra $\M_b$ that equals it:

1. **Reeh—Schlieder**: the bulk "vacuum" $\ket0_{\phi_c}$ is cyclic and separating for
$\widetilde\M_b$, so (since $\ket0_{\phi_c}=\ket1_\Psi$, eq.~6.16) the boundary GNS vacuum $\ket1_\Psi$ is
cyclic and separating for $\M_b$ too.
2. **Causality**: $\widetilde\M_b=\widetilde\M_{\widehat b}$ (eq.~7.5) — the algebra of a region equals
the algebra of its full domain of dependence $\widehat b$ (Sec.~IV.D.3's time-slice axiom), so $\M_b$
reconstructs the whole of $\widehat b$, not merely $b$ itself.
3. **Type $\mathrm{III**_1$}: $\widetilde\M_b$ is type $\mathrm{III}_1$ (any local bulk QFT algebra
is, per Sec.~IV.D.1), so $\M_b$ must be too.
4. **Additivity** for topologically trivial regions, $\widetilde\M_{b_1\cup b_2}=\widetilde\M_{b_1}
\vee\widetilde\M_{b_2}$ (eq.~7.6).
5. **Haag duality**, $\widetilde\M_{b'}=\widetilde\M_b'$ (eq.~7.7, $b'$ the bulk causal complement of
$b$ on its Cauchy slice).

Every one of these bulk statements becomes a testable, checkable statement about boundary algebras once
translated through eq.~7.4 — this is exactly the source of every worked example in the rest of this section.

## Sec.~VII.B: entanglement wedge reconstruction, algebraically

### Defining the boundary algebra $X_A$ properly

Take a boundary spatial region $A$ on a constant-time Cauchy slice. Its **Ryu—Takayanagi (RT) surface**
$\gamma_A$ is the bulk minimal-area surface anchored on $\partial A$; the bulk region $b_A$ between $A$ and
$\gamma_A$ is its dual bulk region, and the **entanglement wedge** $\widehat b_A$ is $b_A$'s bulk domain
of dependence (Fig.~14 of the paper). By subregion-subalgebra duality (eq.~7.8),

$$

X_A \equiv \M_{b_A} = \widetilde\M_{b_A} = \widetilde\M_{\widehat b_A} ,

$$

where $X_A\subset B(\HH_\Psi^{\text{GNS}})$ denotes the boundary algebra dual to $A$'s entanglement wedge —
this restates the ordinary entanglement-wedge-reconstruction statement (physics inside $\widehat b_A$ is fully
recoverable from $A$ alone) as a literal algebra identity.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.82\textwidth]{figs/fig_rt.pdf}
\caption{Subregion—subalgebra duality in AdS/CFT: for a boundary subregion $A$, the Ryu—Takayanagi minimal surface $\gamma_A$ bounds the bulk entanglement wedge $b_A$. The boundary algebra $X_A$ is isomorphic to the bulk von Neumann algebra $\widetilde\M_{b_A}$. The holographic entanglement entropy is given by $S(A) = \frac{\mathrm{Area}(\gamma_A)}{4G_N} + S_{\rm bulk}(b_A) = S_{\rm gen}(b_A)$.}
\label{fig:rt_entanglement_wedge}
\end{figure}

Constructing $X_A$ precisely takes a little care, and it's worth seeing exactly how, since the construction
recurs constantly. At finite $N$, there's an ordinary von Neumann algebra $B_A^{(N)}$ of operators localized in
$A$, satisfying $B_A^{(N)}=B_{\widehat A}^{(N)}$ (eq.~7.9, the ordinary time-slice axiom). As $N\to\infty$,
many operators in $B_A^{(N)}$ simply fail to have a sensible limit and drop out — so the right object is

$$

X_A \equiv \pi_\Psi\Big(\lim_{N\to\infty,\Psi}B_A^{(N)}\Big)'' = X_{\widehat A}

$$

(eq.~7.10 — the double commutant, exactly as in the GNS construction of Sec.~II.D, ensures you get a genuine
von Neumann algebra out the other end; the equality with $X_{\widehat A}$ follows from eq.~7.9 surviving the
limit). There's a second, more easily constructed algebra sitting alongside it: $Y_{\widehat A}$, generated
purely by single-trace operators restricted to $\widehat A$ (the object $Y_O$ from eq.~6.11 of Sec.~VI.A).
Since single-trace operators restricted to any region always survive the large-$N$ limit by construction,

$$

Y_{\widehat A} \subseteq X_A

$$

(eq.~7.11) — and this inclusion is the entire content of the next subsection.

### Causal wedge reconstruction: the "easy" part of $X_A$

Causal wedge reconstruction — also known as (global) HKLL reconstruction, likely familiar already if you've
seen any AdS/CFT course — states that bulk fields in the **causal wedge** $C_{\widehat A}\equiv
\widetilde J^+(\widehat A)\cap\widetilde J^-(\widehat A)$ (points reachable causally both from and to
$\widehat A$) can be written directly in terms of single-trace operators smeared over $\widehat A$ itself,

$$

\Phi(X) = \int d^dx\,K_A^{(C)}(X;x)\,\pi_\Psi(O(x)), \qquad X\in C_{\widehat A},\ x\in\widehat A

$$

(eq.~7.12, with $K_A^{(C)}$ an explicit — if generally distributional — kernel). This is exactly the vacuum-
sector HKLL construction of Sec.~VI.B, eq.~6.32, now applied to a general region rather than the whole
boundary. Algebraically, this identifies

$$

\widetilde\M_{C_{\widehat A}} = Y_{\widehat A}

$$

(eq.~7.13; eqs.~6.49 and 6.53 of Sec.~VI are exactly this statement for $A$ equal to a full boundary). Since
the causal wedge always sits inside the entanglement wedge, $C_{\widehat A}\subseteq\widehat b_A$ (a standard
geometric fact — geometrically, causal reconstruction is always more conservative than entanglement-based
reconstruction), eqs.~7.8 and 7.13 immediately make eq.~7.11's inclusion $Y_{\widehat A}\subseteq X_A$
completely obvious: it's just the algebraic shadow of $C_{\widehat A}\subseteq\widehat b_A$.

### Where the rest of $X_A$ comes from: modular flow, made explicit

Equation~7.10 defines $X_A$ abstractly but doesn't say what's actually *emph* it beyond $Y_{\widehat A}$. On
the gravity side, it's well known that the entanglement wedge is generically strictly bigger than the causal
wedge (equality only in special, highly symmetric cases) — so generically $Y_{\widehat A}\subsetneq X_A$. Here
is where Sec.~IV.A's ergodic Lemma~IV.1 (a modular flow, applied to any subalgebra sharing the same
cyclic-separating vector, regenerates the entire larger algebra) does real, load-bearing work: since $b_A$ is
an honest bulk local region, $\ket1_\Psi$ is cyclic and separating for $X_A=\widetilde\M_{b_A}$, with some
modular operator $\Delta_{X_A}$ (which, by eq.~7.4, equals the bulk modular operator $\widetilde\Delta_{b_A}$
directly). Apply the Lemma to the subalgebra $Y_A^\epsilon$ — single-trace operators smeared within an
infinitesimally thin time band of width $\epsilon$ around $A$ itself (Fig.~15 of the paper) — and modular flow
of the *emph* algebra $X_A$ regenerates all of $X_A$ starting just from this razor-thin sliver:

$$

X_A = \Big\{\, \Delta_{X_A}^{-is}\,O_\epsilon(\vec x)\,\Delta_{X_A}^{is} \ :\ \vec x\in A,\ s\in\mathbb R
\,\Big\}''

$$

(eq.~7.15). **The extra operators in $X_A$, beyond ordinary single-trace ones smeared over $\widehat
A$, are literally single-trace operators run through modular flow.** Plugging this back gives an explicit
formula for bulk fields anywhere in the full entanglement wedge, not just the causal wedge,

$$

\Phi(X) = \int_{-\infty}^\infty ds\int d\vec x\,K_A^{(E)}(X;s,\vec x)\,O(s;\vec x), \qquad X\in\widehat b_A

$$

(eq.~7.16) — the entanglement-wedge generalization of the HKLL formula, first conjectured on other grounds and now derived directly from modular theory.

The foundational engine making this modular reconstruction possible is the celebrated **JLMS theorem** (Jafferis, Lewkowycz, Maldacena, and Suh, 2015). While frequently quoted as a definition, it can be derived directly from the quantum equality of relative entropies:

\begin{keyresult}[: Derivation of the JLMS Formula and Modular Flow Equivalence]
**Theorem (JLMS):** For a boundary spatial region $A$ and its bulk entanglement wedge $b_A$ bounded by the Ryu—Takayanagi surface $\gamma_A$:

1. The boundary and bulk modular Hamiltonians satisfy the operator identity on the code subspace:

$$

H_A \equiv -\log\sigma_A = \frac{\hat A[\gamma_A]}{4G_N} + H_{\text{bulk}} + \mathcal{O}(G_N^{1/2}) , \qquad H_{\text{bulk}} \equiv -\log\sigma_{b_A} .

$$

2. For any bulk field operator $\Phi \in \widetilde\M_{b_A}$ in the entanglement wedge:

$$

\Delta_A^{-is}\,\Phi\,\Delta_A^{is} = \widetilde\Delta_{b_A}^{-is}\,\Phi\,\widetilde\Delta_{b_A}^{is} .

$$

Boundary modular flow directly implements bulk modular flow on all entanglement wedge observables!


**Derivation:**

1. **Relative entropy equivalence:**
Let $\sigma$ be a reference background state (such as the global vacuum or thermofield double), and let $\rho$ be any nearby excited state in the semiclassical code subspace.
A fundamental theorem of quantum error correction and holography states that relative entropy is exactly preserved between boundary subregion $A$ and bulk entanglement wedge $b_A$:

$$

D(\rho_A \| \sigma_A) = D(\rho_{\text{bulk}} \| \sigma_{\text{bulk}}) + \mathcal{O}(G_N) .

$$

2. **Expansion in modular Hamiltonians:**
Recall the definition of relative entropy $D(\rho\|\sigma) = \Tr(\rho\log\rho) - \Tr(\rho\log\sigma) = -S(\rho) + \Tr(\rho H^\sigma)$.
Applying this to the boundary state:

$$

D(\rho_A \| \sigma_A) = -S(\rho_A) + \Braket{H_A^\sigma}_\rho .

$$

Applying this to the bulk state in the entanglement wedge:

$$

D(\rho_{\text{bulk}} \| \sigma_{\text{bulk}}) = -S(\rho_{\text{bulk}}) + \Braket{H_{\text{bulk}}^\sigma}_\rho .

$$

3. **Ryu—Takayanagi / FLM formula:**
By the Faulkner—Lewkowycz—Maldacena (FLM) formula for quantum generalized entropy, the boundary entanglement entropy matches the bulk generalized entropy at leading and subleading order:

$$

S(\rho_A) = \Braket{\frac{\hat A[\gamma_A]}{4G_N}}_\rho + S(\rho_{\text{bulk}}) + \mathcal{O}(G_N^0) .

$$

4. **Exact cancellation of bulk entropy:**
Substitute the FLM generalized entropy into the boundary relative entropy:

$$

D(\rho_A \| \sigma_A) = -\Braket{\frac{\hat A[\gamma_A]}{4G_N}}_\rho - S(\rho_{\text{bulk}}) + \Braket{H_A^\sigma}_\rho .

$$

Equating this to the bulk relative entropy $D(\rho_{\text{bulk}} \| \sigma_{\text{bulk}})$:

$$

-\Braket{\frac{\hat A[\gamma_A]}{4G_N}}_\rho - S(\rho_{\text{bulk}}) + \Braket{H_A^\sigma}_\rho = -S(\rho_{\text{bulk}}) + \Braket{H_{\text{bulk}}^\sigma}_\rho .

$$

Notice that the bulk state von Neumann entropy $S(\rho_{\text{bulk}})$ cancels out identically from both sides!
Rearranging the expectation values:

$$

\Braket{H_A^\sigma}_\rho = \Braket{\frac{\hat A[\gamma_A]}{4G_N} + H_{\text{bulk}}^\sigma}_\rho .

$$

5. **Promotion to operator identity:**
Because this equality of expectation values holds for *emph* state $\rho$ in the code subspace, the operators themselves must be equal within the code subspace:

$$

H_A = \frac{\hat A[\gamma_A]}{4G_N} + H_{\text{bulk}} + \mathcal{O}(G_N^{1/2}) .

$$

6. **Action on bulk operators:**
Let $\Phi \in \widetilde\M_{b_A}$ be an operator localized in the interior of the entanglement wedge. Since the RT surface $\gamma_A = \partial b_A$ is the boundary of the wedge, it is spatially separated from any interior operator $\Phi$. The area operator $\hat A[\gamma_A]$ therefore commutes with $\Phi$:

$$

\left[\frac{\hat A[\gamma_A]}{4G_N}, \, \Phi\right] = 0 .

$$

Evaluating the commutator with the full boundary modular Hamiltonian:

$$

[H_A, \, \Phi] = \left[\frac{\hat A[\gamma_A]}{4G_N} + H_{\text{bulk}}, \, \Phi\right] = [H_{\text{bulk}}, \, \Phi] .

$$

Exponentiating the commutator directly yields the unitary action:

$$

e^{-is H_A} \Phi e^{is H_A} = e^{-is H_{\text{bulk}}} \Phi e^{is H_{\text{bulk}}} \implies \Delta_A^{-is}\,\Phi\,\Delta_A^{is} = \widetilde\Delta_{b_A}^{-is}\,\Phi\,\widetilde\Delta_{b_A}^{is} . \qquad \blacksquare

$$


\end{keyresult}

When does the "easy" causal-wedge piece already exhaust everything, $X_A=Y_{\widehat A}$? Exactly when the
bulk modular flow of $b_A$ happens to act *emph* — as an honest, pointwise coordinate
transformation (like the Rindler-wedge boost of Sec.~IV.D.1) — because a flow like that simply sweeps out
points already inside $\widehat A$, generating nothing new. This happens for a half-space or spherical region
in the vacuum, or for the full boundary in the thermofield double — exactly the cases already worked out
explicitly, where $X_A=Y_{\widehat A}$ and $\widehat b_A=C_{\widehat A}$ (eq.~7.18) hold on the nose. In
general, though, modular flow is *emph* geometric, and the inclusion is strict.


> [!NOTE] **Physics Connection: Modular Flow and Operator Generation**
> **This is the same fact you already checked by hand in Sec.~IV.A.** There, the single-pair modular flow
> $\sigma_s(A)=\rho_R^{-is}A\rho_R^{is}$ was an ordinary, honest unitary conjugation — completely mundane, and
> you verified its eigenvalues directly on a $4\times4$ matrix. Here, the same object — modular flow of a
> boundary algebra — is doing something with no finite-dimensional analogue: it's *emph*, because the algebra it's flowing is infinite-dimensional and
> type $\mathrm{III}_1$. On a qubit, conjugating $A$ by a unitary never produces an operator that wasn't already
> some combination of Pauli matrices — there's nowhere new for it to go. In a type $\mathrm{III}_1$ algebra,
> modular flow can genuinely sweep out an entire larger algebra starting from an arbitrarily thin sliver of it —
> exactly Sec.~IV.A's "ergodic" lemma, now doing the physical work of building an entire black-hole interior
> or entanglement wedge out of a sliver of boundary time. Nothing about the *emph* of modular flow
> changed; what changed is that infinite dimensions let it do something a finite matrix conjugation never can.


### Two logically distinct sources of type $\mathrm{III_1$}

Both $X_A$ and $Y_{\widehat A}$ are type $\mathrm{III}_1$ — but it's worth being careful, because this fact
has *emph* that happen to coincide only once $N\to\infty$ is taken
strictly. Put the boundary theory on a lattice at any finite $N$: then $B_A^{(N)}$ is manifestly type I
(finite matrices, minimal projections and all) — yet $X_A$ and $Y_{\widehat A}$ are *emph* type
$\mathrm{III}_1$. So the type $\mathrm{III}_1$-ness of the emergent large-$N$ algebras has nothing to do with
the type $\mathrm{III}_1$-ness of $B_A^{(N)}$ at finite $N$ before the limit is taken (which doesn't even
exist yet). The finite-$N$ type $\mathrm{III}_1$ of a genuine continuum QFT algebra (Sec.~IV.D.1) comes from
infinite *emph*-range entanglement piling up right at $\partial A$ — mirrored, in the bulk, by the
infinitely long proper distance to the AdS boundary. The emergent, large-$N$ type $\mathrm{III}_1$ of $X_A$
and $Y_{\widehat A}$ instead comes from infinite *emph*-range entanglement between $A$ and its
complement that only appears in the strict $N\to\infty$ limit — mirrored, in the bulk, by infinite
short-range entanglement concentrated right at the RT surface $\gamma_A$ (or the edge $\chi_{\widehat A}$ of
the causal wedge) itself. Two logically independent mechanisms, producing the same type of algebra, at two
different points (finite $N$ vs.\ strict $N\to\infty$) in the same construction.

As a genuinely elegant bonus: since bulk modular flow acts as a local boost near $\gamma_A$ (Sec.~IV.D.1's
local-Rindler argument, applied here right at the RT surface), and $\gamma_A$ is exactly the fixed
("invariant") submanifold of that boost, **the RT surface itself can be redefined, with no bulk metric
assumed, as the asymptotic fixed-point set of the boundary modular flow** — a genuinely algebraic
reformulation, and reinterpretation, of the RT-surface-finding procedure itself.

### Extended gravitational systems: algebra without any geometry to point to

The whole entanglement/causal wedge story generalizes cleanly beyond geometric boundary regions: replace $A$
by *emph* von Neumann subalgebra $\M$ of the boundary theory, and define $X_\M$ by the direct analogue of
eq.~7.10 — no bulk geometric picture is required for this definition to make sense, even though one might not
exist. And you can go further still: couple a genuinely gravitational sector $B$ (with its own boundary dual)
to an ordinary, non-gravitational sector $R$ (e.g.\ radiation that has already escaped to infinity), and for
any subsystem $Q$ of the combined system $B\cup R$, define $X_Q\equiv\lim_{G_N\to0,\Psi}B_Q$ (eq.~7.19, the
entanglement wedge algebra of $Q$, whether or not it has any geometric meaning) and a corresponding causal
wedge algebra $Y_Q$ (the algebra of $Q$'s ordinary low-energy effective description). This abstraction is
exactly what's needed for the evaporating-black-hole discussion two subsections from now, where $Q$ will be
taken to be the emitted Hawking radiation itself.

## Sec.~VII.C: quantum informational aspects of entanglement wedge reconstruction

### Superadditivity, and its boundary origin

**Entanglement wedge nesting** is a standard geometric fact (a consequence of RT-surface extremality):
for boundary regions $A_1\subseteq A_2$, the entanglement wedges satisfy $\widehat b_{A_1}\subseteq
\widehat b_{A_2}$. Algebraically this is nothing but $X_{A_1}\subseteq X_{A_2}$ — immediate from $A_1
\subseteq A_2$ and the definition of $X_A$. A direct geometric consequence, worth checking is genuinely a
*emph* and not an independent assumption: for two regions $A_1,A_2$ on one Cauchy slice,

$$

b_{A_1}\cup b_{A_2} \subseteq b_{A_1\cup A_2}, \qquad b_{A_1\cap A_2}\subseteq b_{A_1}\cap b_{A_2}

$$

(eq.~7.20) — the entanglement wedge of a union is at least as big as the union of the entanglement wedges,
generically strictly bigger (**superadditivity of entanglement wedges**, illustrated with two explicit
AdS$_3$ examples in Fig.~17 of the paper: overlapping intervals, and two disjoint intervals placed close
together — in both cases the RT surface of the union "jumps" to enclose visibly more bulk than either
piece alone). Translated through eq.~7.8, this becomes a statement purely about boundary algebras,

$$

X_{A_1}\vee X_{A_2} \subseteq X_{A_1\cup A_2}, \qquad X_{A_1\cap A_2}\subseteq X_{A_1}\wedge X_{A_2}

$$

(eq.~7.21). Compare this to Sec.~IV.D.3's additivity axiom for an ordinary, finite-$N$ relativistic QFT,
$B_{A_1}^{(N)}\vee B_{A_2}^{(N)}=B_{A_1\cup A_2}^{(N)}$ (eq.~7.22, expected to hold for topologically trivial
regions at finite $N$): **for eq.~7.21's inclusions to be genuinely strict, ordinary additivity has to
fail in the strict large-$N$ limit** — and it can be shown to fail explicitly on exactly the examples of
Fig.~17 (worked out in detail in Fig.~18 of the paper, using a classic result of Araki identifying $X_{A_1}
\vee X_{A_2}$ concretely as the algebra of single-trace operators in a specific larger causal region, strictly
smaller than $X_{A_1\cup A_2}$). **Superadditivity of entanglement wedges is, quite literally, the bulk
geometric shadow of the failure of ordinary locality-additivity for boundary algebras in the strict large-$N$
limit** — algebras associated with local regions are no longer "locally generated" the way an ordinary
finite-$N$ QFT's are.

Haag duality, by contrast, is more robust: assuming it holds for the bulk algebras ($\widetilde\M_{b'}=
\widetilde\M_b'$, eq.~7.7, using that $A,\bar A$ share the same RT surface for a pure global state, so
$b_A=b_{\bar A}$, eq.~7.26), it survives intact into the large-$N$ limit,

$$

X_{A}' = X_{\bar A}

$$

(eq.~7.24) — in sharp contrast to the single-trace algebra $Y_{\widehat A}$, which is additive by
construction but does *emph* satisfy Haag duality.

### Quantum error correction, made precise

Entanglement wedge reconstruction has long been interpreted through the lens of quantum error correction:
recovering all the information in $b_A$ from boundary data on $A$ alone means that information is robust
against "erasing" the complementary region $\bar A$ entirely. Superadditivity sharpens this into something
more precise and checkable: take an operator $\Phi(X)$ with $X$ lying in a bulk region $b$ that sits in the
*emph* of the entanglement wedges of two different boundary regions $A$ and $\widetilde A$, but
outside the entanglement wedge of $A\cap\widetilde A$ (Fig.~19 of the paper). Using the HKLL-type formula
eq.~7.12 (specializing, for concreteness, to a case where causal and entanglement wedges coincide for both
$A$ and $\widetilde A$),

$$

\Phi(X) = \pi_\Omega(O_A(X)) = \pi_\Omega(O_{\widetilde A}(X))

$$

(eq.~7.27) — two *emph* boundary operators, built from entirely different single-trace
data smeared over $A$ versus $\widetilde A$ respectively (eq.~7.28), happen to coincide once represented on
the GNS Hilbert space. There is, in fact, an infinite family of such reconstructions, one for every boundary
region whose entanglement wedge encloses $b$. **This means $\Phi(X)$ — any bulk degree of freedom in
$b$ — cannot be identified with any specific boundary region at all: it is collectively, redundantly encoded
across the boundary system, exactly the defining signature of a quantum error-correcting code**, and this
redundancy is now seen to be a direct, checkable consequence of superadditivity (eq.~7.21) rather than an
independent postulate bolted onto the holographic dictionary.

### Worked calculation: the 3-qubit holographic toy code

To see this error-correcting redundancy at the level of elementary matrix algebra, let us work through the classic 3-qubit holographic toy code.
Let the bulk logical state be a single qubit at the center of the disk:

$$

\ket{\psi}_L = \alpha \ket{0}_L + \beta \ket{1}_L, \qquad |\alpha|^2 + |\beta|^2 = 1

$$

The boundary consists of 3 physical qubits $A, B, C$. The holographic encoding isometry $V: \mathbb{C}^2 \to (\mathbb{C}^2)^{\otimes 3}$ is defined by:

$$

\ket{0}_L \mapsto \frac{1}{\sqrt{2}}\big(\ket{000} + \ket{111}\big), \qquad \ket{1}_L \mapsto \frac{1}{\sqrt{2}}\big(\ket{100} + \ket{011}\big)

$$

Thus the encoded physical boundary state is:

$$

\ket{\Psi(\alpha,\beta)} = \frac{\alpha}{\sqrt{2}}\big(\ket{000}_{ABC} + \ket{111}_{ABC}\big) + \frac{\beta}{\sqrt{2}}\big(\ket{100}_{ABC} + \ket{011}_{ABC}\big)

$$

Let us compute the reduced density matrix on a single boundary subregion, say qubit $C$, by tracing out qubits $A$ and $B$:

$$

\rho_C = \Tr_{AB}\big(\ket{\Psi}\bra{\Psi}\big) = \sum_{a,b \in \{0,1\}} \braket{ab|\Psi}\braket{\Psi|ab}

$$

Evaluating the inner products with the four orthogonal basis states of $AB$:
\begin{align*}
\braket{00|\Psi} &= \frac{\alpha}{\sqrt{2}}\ket{0}_C \implies \braket{00|\Psi}\braket{\Psi|00} = \frac{|\alpha|^2}{2}\ket{0}\bra{0}_C \\
\braket{10|\Psi} &= \frac{\beta}{\sqrt{2}}\ket{0}_C \implies \braket{10|\Psi}\braket{\Psi|10} = \frac{|\beta|^2}{2}\ket{0}\bra{0}_C \\
\braket{11|\Psi} &= \frac{\alpha}{\sqrt{2}}\ket{1}_C \implies \braket{11|\Psi}\braket{\Psi|11} = \frac{|\alpha|^2}{2}\ket{1}\bra{1}_C \\
\braket{01|\Psi} &= \frac{\beta}{\sqrt{2}}\ket{1}_C \implies \braket{01|\Psi}\braket{\Psi|01} = \frac{|\beta|^2}{2}\ket{1}\bra{1}_C
\end{align*}
Summing all four terms:

$$

\rho_C = \left(\frac{|\alpha|^2 + |\beta|^2}{2}\right)\ket{0}\bra{0}_C + \left(\frac{|\alpha|^2 + |\beta|^2}{2}\right)\ket{1}\bra{1}_C = \frac{1}{2}\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \frac{1}{2}\id_2

$$

Notice the remarkable result: $\rho_C$ is strictly proportional to the identity matrix, completely independent of the logical amplitudes $\alpha$ and $\beta$. By exact cyclic symmetry of the code:

$$

\rho_A = \frac{1}{2}\id_2, \qquad \rho_B = \frac{1}{2}\id_2, \qquad \rho_C = \frac{1}{2}\id_2

$$

Any single boundary qubit contains **zero** information about the central bulk qubit!

Now consider reconstructing logical operations using any *emph* qubits (a subregion of size 2):

1. **Logical $Z_L = \ket{0**_L\bra{0} - \ket{1}_L\bra{1}$}:
Define the boundary operator $Z_{AB} \equiv Z_A \otimes Z_B$ acting on region $AB$:
\begin{align*}
(Z_A \otimes Z_B \otimes \id_C)\ket{0}_L &= \frac{1}{\sqrt{2}}\big( (+1)(+1)\ket{000} + (-1)(-1)\ket{111}\big) = \ket{0}_L \\
(Z_A \otimes Z_B \otimes \id_C)\ket{1}_L &= \frac{1}{\sqrt{2}}\big( (-1)(+1)\ket{100} + (+1)(-1)\ket{011}\big) = -\ket{1}_L
\end{align*}
Hence $(Z_{AB} \otimes \id_C)\ket{\psi}_L = Z_L\ket{\psi}_L$.
2. **Logical $X_L = \ket{0**_L\bra{1} + \ket{1}_L\bra{0}$}:
Define the boundary operator $X_{AB} \equiv X_A \otimes \id_B$ on region $AB$:
\begin{align*}
(X_A \otimes \id_B \otimes \id_C)\ket{0}_L &= \frac{1}{\sqrt{2}}\big(\ket{100} + \ket{011}\big) = \ket{1}_L \\
(X_A \otimes \id_B \otimes \id_C)\ket{1}_L &= \frac{1}{\sqrt{2}}\big(\ket{000} + \ket{111}\big) = \ket{0}_L
\end{align*}
Hence $(X_{AB} \otimes \id_C)\ket{\psi}_L = X_L\ket{\psi}_L$.

Crucially, logical $X_L$ can also be reconstructed on region $BC$ as $X_{BC} \equiv \id_A \otimes X_B \otimes \id_C$:

$$

(\id_A \otimes X_B \otimes \id_C)\ket{0}_L = \frac{1}{\sqrt{2}}\big(\ket{010} + \ket{101}\big) \dots

$$

Both $X_A \otimes \id_B \otimes \id_C$ and $\id_A \otimes X_B \otimes \id_C$ act identically on the code subspace as the central bulk field operator $\Phi(0) = X_L$, yet they are supported on disjoint boundary complements. This is the exact algebraic mechanism of holographic error correction in action.

(One honest caveat worth keeping: the
"bulk Hilbert space as a code subspace" picture from the quantum-error-correction literature is only
literally meaningful at finite $N$, whereas the bulk semiclassical Hilbert space is only precisely defined at
$N=\infty$ — so holographic error correction is better understood as a framework connecting the two regimes,
with any finite-$N$ code necessarily only *emph* isometric, not as a literal, exact
implementation of the holographic dictionary.)


> [!NOTE] **Physics Connection: Redundant Purifications and Code Subspaces**
> The fact that $\Phi(X)$ can be written in terms of completely different boundary data (region $A$ or region
> $\widetilde A$) while remaining, in every observable sense, the identical operator is a large-scale version of
> a fact you already know from ordinary quantum information: **purification is never unique.** Take a
> single mixed qubit, $\rho=\mathrm{diag}(0.7,0.3)$. One purification uses a second qubit as the ancilla,
> $\ket\Psi_1=\sqrt{0.7}\ket{00}+\sqrt{0.3}\ket{11}$; a completely different one uses, say, a 3-level ancilla in
> a different encoding, $\ket\Psi_2=\sqrt{0.7}\ket{0}\ket{a}+\sqrt{0.3}\ket{1}\ket{b}$ for any orthonormal
> $\ket a,\ket b$ in the bigger ancilla space. Trace out the ancilla in either case and you get back the
> identical $\rho$ — checked immediately from the definition of partial trace, since it only ever depended on the
> Schmidt coefficients $\sqrt{0.7},\sqrt{0.3}$, never on which specific ancilla states carried them. **Any
> measurement confined to the original qubit alone cannot tell you which purification — which ancilla, entangled
> in which way — is "really" sitting on the other side.** The information is there, but it's not attached to
> any single, canonical description of the environment; it's attached only to the reduced state itself.
> 
> This is precisely the mechanism in eq.~7.27, just replayed at the scale of an entire holographic boundary
> instead of one ancilla qubit: $\Phi(X)$'s reduced, observable content on the GNS Hilbert space is fixed, but
> which specific boundary data (which "purification," i.e.\ which choice of $A$ or $\widetilde A$) you use to
> reconstruct it is exactly as non-unique as the choice of ancilla was above — and, exactly as in the qubit
> example, no measurement confined to the reconstructed operator itself could ever tell you which region did the
> reconstructing. What's new here, and has no counterpart in the single-qubit example, is the *emph*
> content of that redundancy: it isn't merely a bookkeeping curiosity about how you choose to write $\rho$ as a
> partial trace — superadditivity (eq.~7.21) ties it directly to genuine bulk geometry, turning ``purification
> isn't unique'' into ``a bulk region is stored redundantly enough to survive erasing any one boundary
> subregion,'' the operational content of a quantum error-correcting code.


## Sec.~VII.D: an algebraic formulation of entanglement islands

### The island phenomenon, restated algebraically

The **entanglement island** phenomenon — central to modern derivations of the Page curve for an
evaporating black hole — says that after the Page time $t_P$, the black hole interior stops being part of the
black hole's own entanglement wedge and instead becomes part of the entanglement wedge of the emitted
radiation $R$. Split the full system into the black-hole boundary theory $B$ and the radiation $R$
(Fig.~20 of the paper): before $t_P$, the minimal quantum extremal surface for $B$ is empty, so $B$'s
entanglement wedge is the whole Cauchy slice, interior $I$ and exterior $O$ together; after $t_P$, a new,
nontrivial extremal surface $\alpha$ takes over, and $B$'s entanglement wedge shrinks to just the exterior
$O$. Algebraically,

$$

X_B = \begin{cases} \widetilde\M_O\vee\widetilde\M_I & t<t_P \\ \widetilde\M_O & t>t_P \end{cases}

$$

(eq.~7.29) — and since $B\cup R$ is everything there is, once $\widetilde\M_I$ drops out of $X_B$ it must show
up somewhere in $R$'s own description instead. Using the entanglement-wedge algebra $X_R$ and causal-wedge
algebra $Y_R$ from the "extended gravitational systems" discussion above (Sec.~VII.B), this transfer is
stated precisely as

$$

X_R = \begin{cases} Y_R & t<t_P \\ Y_R\vee\widetilde\M_I & t>t_P \end{cases}

$$

(eq.~7.30).

\begin{figure}[htbp]
\centering
\includegraphics[width=0.95\textwidth]{figs/fig_page_curve_islands.pdf}
\caption{The Page curve and the entanglement island mechanism in an evaporating black hole. (a) Before the Page time $t_P$, the radiation entropy follows Hawking's monotonically growing semiclassical curve $S_{\text{Hawking}} \propto t$. After $t_P$, a nontrivial Quantum Extremal Surface (QES) forms, and the generalized entropy is bounded by the decaying black hole area $A_{\text{BH}}(t)/4G_N$, restoring unitarity. (b) The Penrose diagram shows that for $t > t_P$, the entanglement wedge of the radiation $W(R)$ swallows the interior island $I$, transferring the interior algebra $\widetilde\M_I$ into the radiation algebra: $X_R = Y_R \vee \widetilde\M_I$.}
\label{fig:page_curve_islands}
\end{figure}

This lets you *emph* the presence of an island using only data intrinsic to the radiation
system, with no reference to $B$ at all:

$$

I_R \equiv Y_R'\cap X_R

$$

(eq.~7.31) — for $t>t_P$, this evaluates to exactly $\widetilde\M_I$: an island exists exactly when this
intersection is nontrivial, meaning there are operators surviving the semiclassical limit that lie outside
$R$'s ordinary low-energy effective description. (Exactly as with $X_A$ versus $Y_{\widehat A}$ above, these
extra operators are generated from $Y_R$ by modular flow of $X_R$ — the identical mechanism, one more time.)
The same definition, $I_Q\equiv Y_Q'\cap X_Q$ (eq.~7.32), applies to any subsystem $Q$ of an extended
gravitational system, not just radiation specifically: an island for $Q$ is whatever survives the
semiclassical limit but sits outside $Q$'s own low-energy description.

Specializing back to an ordinary boundary region $A$ (so $Y_Q=Y_{\widehat A}$), the island algebra $I_A$
consists of exactly the modular-flow-generated operators in $X_A$ that aren't in $Y_{\widehat A}$ —
geometrically, the part of the entanglement wedge $b_A$ lying outside the causal wedge $c_{\widehat A}$,
i.e.\ $b_A=c_{\widehat A}\cup i_A$ (a genuine, ordinary geometric decomposition, per Fig.~21 of the paper),
giving $X_A=Y_{\widehat A}\vee\widetilde\M_{i_A}$ and $I_A=\widetilde\M_{i_A}$ — an island, in this
language, is exactly the piece of an entanglement wedge that causal-wedge (HKLL) reconstruction alone could
never reach.

\begin{keyresult}[: Derivation of the Page Curve from the Quantum Extremal Island Rule]
**The Island Rule for Radiation:** In an evaporating black hole coupled to a non-gravitational radiation reservoir, the generalized entanglement entropy of the radiation $R$ at boundary time $t$ is determined by extremizing over all possible interior quantum extremal surfaces (QES) $\partial I$:

$$

S(R) = \min_{\text{QES } I} \operatorname{ext}_I \left[ \frac{\operatorname{Area}(\partial I)}{4G_N} + S_{\text{bulk}}(R \cup I) \right] .

$$


**Explicit Derivation of the Unitary Page Curve:**

1. **Evaporating Black Hole Geometry:**
Let the black hole be formed at $t = 0$ with initial horizon area $A_0$ and Bekenstein—Hawking entropy $S_0 = \frac{A_0}{4G_N}$. As the black hole radiates into the reservoir at rate $\Gamma = -\frac{dM}{dt}$, its semiclassical horizon area decreases monotonically:

$$

S_{\text{BH}}(t) \equiv \frac{A_{\text{BH}}(t)}{4G_N} = S_0 - \Gamma t, \qquad t \in [0, t_{\text{evap}}] ,

$$

where $t_{\text{evap}} = S_0/\Gamma$ is the total evaporation time.
2. **Saddle 1: The Trivial / No-Island Branch ($I = \emptyset$):**
For the trivial choice $I = \emptyset$, there is no boundary ($\partial I = \emptyset$), so $\operatorname{Area}(\partial I) = 0$. The generalized entropy reduces strictly to the bulk field-theoretic entropy of the radiation:

$$

S_{\text{no-island}}(R) = S_{\text{bulk}}(R) .

$$

In Hawking's semiclassical calculation, each outgoing emitted quantum $c_k$ in the radiation bath is entangled with an infalling partner mode $b_k$ behind the horizon:

$$

\ket{\text{Hawking pair}}_k \approx \frac{1}{\sqrt{2}}\big(\ket{0}_{c_k}\ket{0}_{b_k} + \ket{1}_{c_k}\ket{1}_{b_k}\big) .

$$

Because the bath $R$ only collects the outgoing quanta $c_k$ while the partner modes $b_k$ remain trapped behind the horizon, tracing out the interior partners produces a linearly growing thermal entanglement entropy:

$$

S_{\text{no-island}}(R) = \int_0^t dt' \, \frac{dS_{\text{rad}}}{dt'} = \Gamma t .

$$

As $t$ increases, $S_{\text{no-island}}(R)$ grows monotonically and unboundedly, eventually exceeding the Bekenstein—Hawking entropy of the remaining black hole — this is the classic **Hawking information paradox**.
3. **Saddle 2: The Island Branch ($I \ne \emptyset$):**
A second, non-empty extremum emerges where $\partial I$ is a quantum extremal surface located just inside the event horizon:

$$

r_{\text{QES}} = r_H(t) - \mathcal{O}(G_N e^{-2\pi t/\beta}) .

$$

The spatial region $I$ covers the black hole interior behind the horizon. The generalized entropy for this saddle is:

$$

S_{\text{island}}(R) = \frac{\operatorname{Area}(\partial I)}{4G_N} + S_{\text{bulk}}(R \cup I) .

$$

Now evaluate the bulk matter entropy $S_{\text{bulk}}(R \cup I)$:
The spatial union $R \cup I$ contains *emph* the outgoing Hawking quanta $c_k \in R$ *emph* their infalling entangled partner modes $b_k \in I$.
Within $R \cup I$, each entangled pair $\ket{\text{Hawking pair}}_k$ forms an unentangled pure state!
The infalling modes and outgoing modes **purify each other**:

$$

S_{\text{bulk}}(R \cup I) = S_{\text{bulk}}(\text{thermal gas outside } \partial I) \approx \mathcal{O}(G_N^0) \approx 0 .

$$

The bulk entanglement divergence cancels out completely, leaving only the classical horizon area:

$$

S_{\text{island}}(R) = \frac{\operatorname{Area}(\partial I)}{4G_N} + \mathcal{O}(G_N^0) \approx \frac{A_{\text{BH}}(t)}{4G_N} = S_0 - \Gamma t .

$$

4. **The Page Time and Phase Transition:**
By the island rule, the physical von Neumann entropy is the minimum of the two competing saddles:

$$

S(R) = \min\big\{ S_{\text{no-island}}(R), \, S_{\text{island}}(R) \big\} = \min\big\{ \Gamma t, \, S_0 - \Gamma t \big\} .

$$

Equating the two branches yields the celebrated **Page time** $t_P$:

$$

\Gamma t_P = S_0 - \Gamma t_P \implies t_P = \frac{S_0}{2\Gamma} = \frac{1}{2} t_{\text{evap}} .

$$

Evaluating the resulting entropy over the black hole lifetime:

$$

S(R) = \begin{cases}
\Gamma t & t < t_P \quad (\text{Hawking phase: no island}) \\
S_0 - \Gamma t = \frac{A_{\text{BH}}(t)}{4G_N} & t > t_P \quad (\text{Unitary phase: interior island } I)
\end{cases}

$$

At $t = t_{\text{evap}}$, $S(R) \to 0$ as the black hole fully evaporates, proving that Hawking radiation undergoes unitary evolution!
5. **Algebraic Translation:**
For $t < t_P$, the radiation algebra is simply $X_R = Y_R$.
For $t > t_P$, the island forms: $X_R = Y_R \vee \widetilde\M_I$. The modular flow of $X_R$ reconstructs the entire interior algebra $\widetilde\M_I$ from the radiation data alone, resolving the paradox algebraically without modifying semiclassical effective field theory. $\blacksquare$

\end{keyresult}

## Sec.~VII.E: boundary description of a bulk causal diamond

This subsection works through several increasingly striking concrete examples of the duality applied to
regions that *emph* — genuinely bulk, purely interior objects described
entirely by boundary commutant structure.

### A diamond in the center of AdS, defined purely algebraically

In the vacuum sector, take a boundary time band $I_w$ of width $w<\pi R$. Its causal wedge is a ``spherical
Rindler region'' $W_{\rho_w}$ of radius $\rho_w=R\tan(\tfrac\pi2-\tfrac w{2R})$ (eq.~7.34, Fig.~23 of the
paper), identified with the single-trace time-band algebra: $\widetilde\M_{W_{\rho_w}}=Y_{I_w}$ (eq.~7.35).
(At $w\ge\pi R$, $W_{\rho_w}$ swallows an entire Cauchy slice, and this reduces to eq.~6.27's full-boundary
statement.) Now take the *emph* of both sides, and use Haag duality (eq.~7.7):

$$

\widetilde\M_{D_{\rho_w}} = Y_{I_w}'

$$

(eq.~7.36), where $D_{\rho_w}=W_{\rho_w}'$ is a small spherical diamond sitting right in the very center of
global AdS — as far from the boundary as you can get. **This diamond region's boundary description is
not geometric at all: it is defined purely algebraically, as the commutant of a boundary time-band algebra**,
with no boundary region of its own to point to. As $w\to\pi R$, the time band swallows nearly the whole
boundary, the causal wedge $W_{\rho_w}$ swallows nearly the whole bulk, and correspondingly the diamond
$D_{\rho_w}$ shrinks to an arbitrarily small, local patch of nearly-flat spacetime — described, at every
stage, by the commutant of an ever-larger boundary time-band algebra. This is presented explicitly as a
precise, operator-algebraic realization of the familiar holographic **IR/UV relation**: probing longer
boundary time scales (bigger $Y_{I_w}$) is dual to probing shorter bulk distance scales (smaller diamond
$D_{\rho_w}$).

### Detecting a horizon from commutant structure alone

Now repeat this in the thermofield-double black hole above $T_{\text{HP}}$: taking $Y_{I_w}^{(R)}$ (a
time band of width $w$ on the right boundary), its causal wedge is a spherical wedge region $W_{\rho_w}$
sitting strictly inside the black hole exterior (eq.~7.38, Fig.~24(a)) — and crucially, *emph*, $W_{\rho_w}$ never manages to cover the entire $t=0$ slice of the exterior region: the
horizon is precisely the obstruction preventing this. Algebraically,

$$

(Y_{I_w}^{(R)})' \cap Y_R \ne \varnothing, \qquad \text{for every } w

$$

(eq.~7.40): **the mere existence of a horizon in the bulk is detected, on the boundary, by the fact that
no matter how wide a time band you take, its commutant (restricted to the $R$ algebra) never becomes
trivial.** This is worth comparing directly to the vacuum-sector story just above: there, growing $w$ all the
way to $\pi R$ eventually made the causal wedge cover the entire Cauchy slice (no horizon, and correspondingly
the diamond commutant genuinely does shrink to nothing as $w\to\pi R$); here, past the Hawking—Page
transition, that never happens, for any $w$ — a clean, purely boundary-intrinsic diagnostic distinguishing a
horizon-free geometry (like empty AdS) from a black hole, using nothing but the growth pattern of commutants
of nested time bands.

### A single-sided collapsing black hole, and the emergence of a horizon in real time

The richest example: take $\ket\Psi$ dual to a single-sided black hole formed by ordinary gravitational
collapse (Fig.~25 of the paper) — on the boundary side, this corresponds to $\ket\Psi$ thermalizing over time.
An early-time time band $I_0$, wide enough that its causal wedge already covers a full Cauchy slice, gives
$Y_{I_0}=B(\HH_{\text{bulk}})$ (eq.~7.41) — a genuine, honest type I algebra (no horizon has formed yet, so
there's nothing to obstruct full reconstruction). At late times, well after collapse, a semi-infinite time
band $I_1$ instead reconstructs only the black hole exterior, $\widetilde\M_R=Y_{I_1}$, with the commutant
$Y_{I_1}'$ giving an emergent "mirror" interior algebra $\widetilde\M_L$ — reproducing, entirely from a
*emph* collapse geometry, the same thermofield-double-like split structure, $Y_{I_0}=Y_{I_1}\vee
Y_{I_1}'=\widetilde\M_R\vee\widetilde\M_L$ (eq.~7.42), that the genuinely two-sided eternal black hole had.
**The type of the time-band algebra changes qualitatively as the system evolves**: type I at early times
(before a horizon exists), and — once the system thermalizes — type $\mathrm{III}_1$ for a time band of
*emph* width, no matter how large, as long as its earliest endpoint stays fixed at some late reference
time. **This qualitative change in algebra type, tracked purely from boundary data, is the operator-
algebraic definition of horizon formation and thermalization happening in real time** — exactly the ``causal
depth'' diagnostic previewed already, made fully precise here.

### The general theorem, and its limits

All of the examples above shared a convenient special feature: the boundary region considered was exactly the
intersection of its own causal wedge with the boundary. This fails in general (null-geodesic focusing means a
light ray fired from the boundary into the bulk and back out again generically lands somewhere different from
where it started, due to caustics) — and correspondingly, for a generic boundary region $Y$, the naive
single-trace algebra $Y_Y$ isn't even a genuine von Neumann algebra on its own (its double commutant can
reach single-trace operators supported on a strictly larger region than $Y$ itself, exactly the
Fig.~18 phenomenon from Sec.~VII.C above). A precise theorem fixes exactly when the naive causal-wedge story
does work: $Y_Y$ admits standard causal-wedge reconstruction, and is already a genuine von Neumann algebra,
if and only if $Y$ is **causally convex** and satisfies $C_Y\cap B=Y$ (eq.~7.44, where $C_Y\equiv
(\widetilde J^+[Y]\cap\widetilde J^-[Y])''$ is the generalized causal wedge and $B$ the boundary manifold) —
in which case $Y_Y=\widetilde\M_{C_Y}$ exactly (eq.~7.45), with commutant $Y_Y'=\widetilde\M_{C_Y'}$
(eq.~7.46). For a region $Y$ failing this condition, $Y_Y''$ instead reconstructs the algebra of the larger
region $Y_{\max}\equiv C_Y\cap B$ (eq.~7.47) — a clean, general characterization of exactly how much bigger
the double commutant can get.

## Sec.~VII.F: generalized entropy and subregion-subalgebra duality at finite $N$

Everything above lived strictly at $N=\infty$. This closing subsection asks what survives at finite (but
large) $N$, where a bulk subregion can no longer even be sharply defined due to genuine spacetime
fluctuations, and gives an important piece of indirect evidence that the whole framework nonetheless extends.

Take the thermofield double above $T_{\text{HP}}$. At finite $N$, $B(\HH_R)$ is an ordinary type I algebra
with a perfectly well-defined entanglement entropy $S_R$; in the strict $N\to\infty$ limit, $S_R$ should match
the **generalized entropy** of the dual black hole,

$$

S_{\text{gen}} \equiv \frac{A_{\text{hor}}}{4G_N(\epsilon)} + S_{\text{bulk}}(\epsilon)

$$

(eq.~7.48, with $\epsilon$ a bulk short-distance cutoff, and $G_N(\epsilon)$ the corresponding bare coupling).
At strict $G_N\to0$, $\widetilde\M_R$ is type $\mathrm{III}_1$, so $S_{\text{bulk}}$ isn't even defined without
first regularizing $\widetilde\M_R$ into a type I algebra $\widetilde\M_R^\epsilon$ using the cutoff $\epsilon$
— whose entropy then has a leading UV divergence $S_{\text{bulk}}(\epsilon)=a\,A_{\text{hor}}/\epsilon^{d-1}+
\cdots$ (eq.~7.49, the familiar area-law divergence from Sec.~IV.D.1 all over again), matched by a
corresponding divergence in the bare coupling $G_N(\epsilon)$ in the first term. Neither term in eq.~7.48 is
separately finite as $\epsilon\to0$ — but there are strong indications (from independent gravitational
calculations) that the two divergences cancel exactly, leaving a finite $S_{\text{gen}}=\lim_{\epsilon\to0}
\big(\tfrac{A_{\text{hor}}}{4G_N(\epsilon)}+S_{\text{bulk}}(\epsilon)\big)$ (eq.~7.50).

### Worked calculation: cancellation of UV divergences in generalized entropy

To see this cancellation explicitly, consider a free scalar field in the near-horizon Rindler region of a $(d+1)$-dimensional spacetime with metric:

$$

ds^2 = -\kappa^2 \rho^2 dt^2 + d\rho^2 + dx_\perp^2

$$

where $\rho$ is the proper distance to the horizon at $\rho = 0$, $\kappa = 2\pi/\beta$ is the surface gravity, and $x_\perp \in \mathbb{R}^{d-1}$ are the transverse horizon coordinates with total area $A_{\text{hor}} = \int d^{d-1}x_\perp$.
Imposing a brick-wall cutoff at proper distance $\rho = \epsilon > 0$, the standard thermal entanglement entropy of the bulk quantum field modes in the exterior region $\rho \ge \epsilon$ yields:

$$

S_{\text{bulk}}(\epsilon) = \frac{c_{d-1}\, A_{\text{hor}}}{\epsilon^{d-1}} + S_{\text{bulk}}^{\text{finite}}

$$

where the leading geometric coefficient is $c_{d-1} = \frac{1}{6 (4\pi)^{(d-1)/2}\,\Gamma((d-1)/2)}$.
In isolation, as $\epsilon \to 0$, $S_{\text{bulk}}(\epsilon) \to +\infty$ because the local field algebra is type $\mathrm{III}_1$.

However, quantum fluctuations of the scalar field also generate 1-loop corrections to the gravitational effective action. Integrating out the scalar modes with the same UV cutoff $\epsilon$ shifts the effective Einstein—Hilbert action:

$$

S_{\text{eff}}[g] = \int d^{d+1}x \sqrt{-g} \left( \frac{1}{16\pi G_{N,0}} R + \dots \right) + \frac{1}{2}\Tr\log(-\Box)

$$

The heat-kernel expansion of $\Tr\log(-\Box)$ generates a 1-loop renormalization of the bare Newton constant:

$$

\frac{1}{16\pi G_N(\epsilon)} = \frac{1}{16\pi G_{N,\text{ren}}} - \frac{c_{d-1}}{4\,\epsilon^{d-1}} \implies \frac{1}{4G_N(\epsilon)} = \frac{1}{4G_{N,\text{ren}}} - \frac{c_{d-1}}{\epsilon^{d-1}}

$$

Now substitute this renormalized coupling back into the generalized entropy $S_{\text{gen}}(\epsilon)$:
\begin{align*}
S_{\text{gen}}(\epsilon) &= \frac{A_{\text{hor}}}{4G_N(\epsilon)} + S_{\text{bulk}}(\epsilon) \\
&= \left(\frac{A_{\text{hor}}}{4G_{N,\text{ren}}} - \frac{c_{d-1}\,A_{\text{hor}}}{\epsilon^{d-1}}\right) + \left(\frac{c_{d-1}\,A_{\text{hor}}}{\epsilon^{d-1}} + S_{\text{bulk}}^{\text{finite}}\right) \\
&= \frac{A_{\text{hor}}}{4G_{N,\text{ren}}} + S_{\text{bulk}}^{\text{finite}}
\end{align*}
The cutoff-dependent pole $\epsilon^{-(d-1)}$ cancels identically!
This establishes that generalized entropy $S_{\text{gen}}$ is a genuinely cutoff-independent physical observable, even though its classical geometric part and quantum field-theoretic part are separately ill-defined without a regulator. This exact cancellation is what the algebraic crossed product of Sec.~V formalizes directly at the operator level.

This finiteness gives real, if indirect, evidence for exactly the extension the whole section has been
building toward: there should exist a boundary regularization, at finite $N$, producing a type I algebra
$Y_R^\epsilon$ with $\widetilde\M_R^\epsilon=Y_R^\epsilon$ (eq.~7.51) — even though nobody currently knows how
to write this regularization down explicitly for a general boundary theory. Pushing $\epsilon$ down to the
Planck length $\ell_p$ (where the clean separation between the two terms of eq.~7.48 breaks down, since
$1/G_N\sim1/\epsilon^{d-1}$ at that point), the natural expectation is

$$

\widetilde\M_R^\epsilon = Y_R^\epsilon = B(\HH_R), \qquad \epsilon\sim\ell_p

$$

(eq.~7.52): the emergent, large-$N$, type $\mathrm{III}_1$ algebra $Y_R$ is conjectured to be the strict
$\epsilon\to0$ endpoint of a continuous family of finite-$N$, type I extensions, all the way down to the
ordinary finite-$N$ algebra $B(\HH_R)$ itself — subregion-subalgebra duality, suitably reinterpreted, surviving
all the way down to finite $N$, not just as a strict $N=\infty$ statement.

\bigskip
\noindent With subregion-subalgebra duality now established as the general principle — and worked through on
the vacuum sector, the eternal and evaporating black hole, and purely-algebraic bulk diamonds — Sec.~VIII
turns to the deepest consequence of all: reading bulk *emph*, including the very
formation of a horizon and the connectivity of spacetime, directly off the type and commutant structure of
boundary algebras, with no bulk metric assumed anywhere in the argument.



---

# Sec.~VIII: Emergence of bulk geometric concepts

Sec.~VII established that a bulk region *emph* a boundary algebra. This section pushes that identification
to its limit: causal structure, the formation of a horizon, and even whether two boundary theories are joined
by a wormhole at all, can each be read directly off the type and commutant structure of boundary algebras —
with no bulk metric assumed anywhere in the argument. This closes the two puzzles flagged back in Sec.~VI.C
(the factorization puzzle was already resolved there; the meeting-behind-the-horizon puzzle is resolved here,
in Sec.~VIII.B).

## Sec.~VIII.A: algebraic characterization of bulk causal structure

### Why boundary commutants can encode more than boundary causality

Boundary operators separated in a spacelike way automatically commute — ordinary microcausality. But
*emph*-separated boundary operators are not required to commute at all; whether they do depends on
the specific representation, which is fixed by the state's two-point functions. This freedom is not a bug —
it's exactly the room needed for boundary commutant structure to encode something richer than boundary
causality alone: by subregion-subalgebra duality, it encodes bulk causal structure, in one higher dimension.

### The causal depth parameter

Recall from Sec.~VI.B (eq.~6.33) that in empty AdS, a boundary time band $I_w$ generates the entire algebra,
$Y_{I_w}=B(\HH_\Omega^{\text{GNS}})$, once $w\ge\pi R$ — geometrically, $\pi R$ is exactly the minimal width
for which light rays from the band already cover an entire bulk Cauchy slice. This motivates a purely
boundary-intrinsic definition:

\begin{quote}
**Definition (causal depth $T(t)$).** For a single-sided semiclassical state $\ket\Psi$, $T(t)$ is the
largest $w$ for which the time-band algebra $Y_{I_w(t)}$ (centered at boundary time $t$) still has a
*emph* commutant.
\end{quote}

For empty AdS, $T(t)=\pi R$: finite and time-independent, matching the geometric statement that light rays
from a band of exactly that width already reach everywhere. For a general horizon-free asymptotically-AdS
geometry, $T(t)$ is expected to stay finite for all time. For a single-sided eternal black hole (Fig.~26(b) of
the paper), by contrast, $Y_{I_w}$ has a *emph* commutant for *emph* finite $w$ — no matter
how wide a time band you take, you can never quite reach the full exterior algebra (only in the strict
$w\to\infty$ limit does the commutant become trivial) — so $T(t)=\infty$, for all $t$: **a purely
boundary-intrinsic signature of a horizon, requiring no bulk metric to state.** For a black hole formed by
collapse (Fig.~25 again), $T(t)$ starts finite and grows monotonically, diverging only as $t\to\infty$ — the
boundary-side signature of a horizon actually *emph*, in real time, rather than always having been
there.

A two-sided version, $T_R(t)$, is defined the same way but using the *emph* commutant of $Y_{I_w}$
within $Y_R$ (the right boundary's own single-trace algebra) — for the thermofield double below
$T_{\text{HP}}$, this reduces to ordinary empty AdS's $\pi R$; above $T_{\text{HP}}$, it diverges for all
time, exactly reproducing eq.~7.40's bifurcating-horizon diagnostic from Sec.~VII.E in this new language.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.90\textwidth]{figs/fig_causal_depth.pdf}
\caption{The causal depth parameter $T(t)$ as an algebraic detector of horizons. (a) In empty AdS, a boundary time band $I_w$ of width $w \ge \pi R$ sends light rays that meet at the bulk center $r=0$ and cover an entire Cauchy slice, driving the commutant to triviality ($Y_{I_w}' = \mathbb{C}\mathbf{1}$) and giving a finite causal depth $T = \pi R$. (b) In a black hole spacetime, boundary light rays asymptotically wrap around the horizon without crossing, so $Y_{I_w}' \ne \mathbb{C}\mathbf{1}$ for all finite $w$. The causal depth diverges: $T = \infty$, serving as a purely algebraic boundary diagnostic of a horizon.}
\label{fig:causal_depth}
\end{figure}

### $T$ as a measure of lost determinism

Here's a genuinely illuminating reframing of what $T$ is measuring, worth holding onto because it explains why
this whole construction is possible at all. At finite $N$, knowing the operator algebra on a single Cauchy
slice determines the whole theory (ordinary causal time evolution, the time-slice axiom of Sec.~IV.D.3). In
the strict large-$N$ limit, this stops being true — there are no equations of motion relating single-trace
operators at different times (Sec.~VI.A) — but the theory isn't completely disconnected across time either:
correlations (encoded in two-point functions) still relate a time band's algebra to the rest of the theory,
just not through equations of motion. $T$ is exactly the minimal width of a band whose algebra is
*emph*, via these correlations rather than dynamics, to recover the whole system. Read this way,
**$T=0$ is full determinism (an honest equation of motion); $T$ finite is a partial, quantifiable loss of
determinism; $T=\infty$, as in a black hole, is a complete loss of determinism — no finite window of boundary
time, however wide, is ever enough.** The emergence of the bulk radial direction is, in this precise sense,
tied to the boundary theory progressively losing determinism as $N\to\infty$.

(The paper makes this fully rigorous by relating $T$ to a classical object from harmonic analysis called the
*emph* of the spectral function $\rho(\omega)$ — the Fourier transform of the commutator
$\braket{\Psi|[O(t),O(t')]|\Psi}$ (eqs.~8.1—8.5) — connecting it to an old question of Kolmogorov's about how
long you must observe a chaotic classical system before you can predict its entire future. This machinery is
flagged here for completeness; the physical content that matters going forward is the definition of $T$ itself
and what it measures, not the harmonic-analysis technique used to compute it in specific examples.)

### Worked calculation: spectral functions and the divergence of causal depth

To make the causal depth parameter $T(t)$ mathematically transparent, let us compute the spectral function $\rho(\omega)$ explicitly in two contrasting backgrounds: empty AdS versus a thermal black hole.
The spectral function is defined as the Fourier transform of the boundary commutator:

$$

\rho(\omega) \equiv \int_{-\infty}^\infty dt\, e^{i\omega t}\, \braket{\Psi|\big[O(t),\, O(0)\big]|\Psi}

$$


1. **Vacuum state $\ket\Omega$ (Empty AdS)**:
In global $\text{AdS}_{d+1}$ of radius $R$, the boundary CFT spectrum consists of discrete primaries and descendants with energies $\omega_n = (\Delta + 2n)/R$ for $n \in \mathbb{N}_0$. The Wightman function is:

$$

\braket{\Omega|O(t)O(0)|\Omega} = \sum_{n=0}^\infty c_n e^{-i(\Delta + 2n)t/R}

$$

The commutator is therefore:

$$

\braket{\Omega|\big[O(t),O(0)\big]|\Omega} = -2i \sum_{n=0}^\infty c_n \sin\big((\Delta + 2n)t/R\big)

$$

Its Fourier transform $\rho(\omega)$ is a discrete sum of delta functions:

$$

\rho(\omega) = 2\pi \sum_{n=0}^\infty c_n \Big(\delta\big(\omega - (\Delta+2n)/R\big) - \delta\big(\omega + (\Delta+2n)/R\big)\Big)

$$

Notice that $\rho(\omega) = 0$ identically in the frequency bandgap $|\omega| < \Delta/R$. By the classical Paley—Wiener theorem of Fourier analysis, a spectral function with this discrete bandgap structure has a finite exponential type:

$$

T = \pi R < \infty

$$

Thus a boundary time band of finite width $w \ge \pi R$ is sufficient to reconstruct all operators in the vacuum sector.
2. **Thermal state $\ket{\Psi_\beta**$ (BTZ Black Hole)}:
For a 2D boundary CFT at finite temperature $T = 1/\beta$, the thermal two-point function on the cylinder is:

$$

\braket{O(t)O(0)}_\beta = \left(\frac{\pi}{\beta \sinh\big(\frac{\pi}{\beta}(t - i\epsilon)\big)}\right)^{2\Delta}

$$

Taking the difference across the branch cut to evaluate the commutator and computing its Fourier transform yields:

$$

\rho(\omega) = \frac{2\pi}{\Gamma(2\Delta)}\left(\frac{2\pi}{\beta}\right)^{2\Delta - 1} \sinh\left(\frac{\beta\omega}{2}\right) \left|\Gamma\left(\Delta + \frac{i\beta\omega}{2\pi}\right)\right|^2

$$

For large frequency $|\omega| \gg 1/\beta$, Stirling's approximation gives:

$$

\rho(\omega) \approx C\, |\omega|^{2\Delta - 1} e^{-\beta |\omega| / 2}

$$

Unlike the vacuum, $\rho(\omega)$ is strictly positive and smooth for *emph* $\omega \in \mathbb{R}$, decaying only exponentially without any compact support or bandgap. Consequently, the exponential type of $\rho(\omega)$ is infinite:

$$

T = \infty

$$


This provides an exact, rigorous demonstration of why the black hole horizon creates an infinite causal depth $T = \infty$: the thermal dissipation of boundary correlators completely destroys finite-time determinism.

## Sec.~VIII.B: emergence of Kruskal-like time, and resolving the meeting-behind-the-horizon puzzle

### Two kinds of bulk time

The eternal AdS black hole geometry has two qualitatively different notions of time. **Schwarzschild
time** is an honest isometry — it maps the $R$ (or $L$) exterior region to itself, never leaving it. This is
exactly the boundary time of the thermofield double: the identification eq.~6.36 already established
Schwarzschild time as the modular time of $\widetilde\M_R=Y_R$. **Kruskal time**, by contrast, is not an
isometry at all — it's the time that actually carries a point from the exterior $R$ region across the horizon
into the interior $F$ (future) or $P$ (past) regions (Fig.~27 of the paper — the Kruskal null coordinates $U,V$
are exactly the light-cone coordinates $x^\mp$ of the Rindler-wedge discussion in Sec.~IV.E, since near the
horizon the geometry looks locally like flat Rindler space). Schwarzschild time has an obvious boundary home
(it's just ordinary boundary time evolution); Kruskal time, at first glance, has no boundary home at all —
boundary time simply runs to $\pm\infty$ as you approach the horizon and has nothing left to say about what
happens beyond it.

### Kruskal time from half-sided modular inclusion

Here is where Sec.~IV.E's half-sided modular inclusion machinery — introduced there as a purely algebraic
curiosity, worked out on an abstract Rindler-wedge light-cone example — turns out to be *emph* the
tool needed, verbatim, to manufacture Kruskal time out of nothing but boundary data. Take $\M=Y_R$ (the
right boundary's full single-trace algebra, cyclic-separating for $\ket{\Psi_\beta}$), and $\N=Y_-$, the
subalgebra generated by single-trace operators supported on the semi-infinite band $t<0$ — by Sec.~VII.E's
duality, $Y_-$ is dual to a specific bulk wedge region $W_-$ (Fig.~28 of the paper), itself type
$\mathrm{III}_1$, with $\ket{\Psi_\beta}$ cyclic and separating for it too. Because $Y_R$'s modular flow is
literally boundary time translation, $Y_-$ automatically satisfies exactly the half-sided modular inclusion
condition of eq.~4.81 — so Sec.~IV.E's machinery applies immediately, producing a genuine positive generator
$G_+\equiv\tfrac1{2\pi}(K_{Y_R}-K_{Y_-})$ (eq.~8.6), generating a brand-new time flow on $Y_R=\widetilde\M_R$
that leaves $\ket{\Psi_\beta}$ fixed. Repeating with $\N=Y_+$ (the band $t>0$) gives a second, independent
generator $G_-$.

Near the horizon — where, exactly as in Sec.~IV.E's abstract example, the geometry reduces to flat Rindler
space — these two generators act exactly as null translations in the two light-cone directions,

$$

e^{iG_+s}\phi(X)e^{-iG_+s}=\phi(X_s),\ \ X_s=(U+s,V,x_\perp)\ \ (V\ll1),

$$


$$

e^{iG_-s}\phi(X)e^{-iG_-s}=\phi(X_s),\ \ X_s=(U,V+s,x_\perp)\ \ (U\ll1)

$$

(eqs.~8.7—8.8) — **$G_\pm$, built purely from boundary modular data, literally translate a bulk operator
across the horizon**, and the combinations $p\equiv G_—G_+$, $h\equiv G_++G_-$ (eq.~8.9) generate ordinary
spatial and genuine Kruskal-time translation respectively, right in the near-horizon region.

**This resolves the meeting-behind-the-horizon puzzle from Sec.~VI.C directly**: the boundary
Hamiltonian $H=H_R+H_L$ genuinely has no term coupling $R$ to $L$ — and yet the entanglement structure of
$\ket{\Psi_\beta}$ itself, purely through the algebraic relationship between $Y_R$ and its subalgebras
$Y_\pm$, generates emergent operators $G_\pm$ that couple the two sides and translate operators from $R$ and
$L$ into causal contact behind the horizon. No interaction term was ever needed in $H$; the coupling is
already latent in how entangled the state is, made manifest only once you build the right algebraic objects
from it.

Explicit computation (worked out in detail for the BTZ black hole, not reproduced symbol-by-symbol here, but
worth knowing the shape of the answer) shows this is not just a qualitative statement — it reproduces the
*emph* causal structure expected of the black hole geometry. Flowing an operator $\Phi(X,s)\equiv
e^{iG_+s}\phi(X)e^{-iG_+s}$ starting at $X=(U_0,V_0,x_\perp)$: for $s$ below a precise threshold $s_0=-U_0$,
$\Phi(X;s)$ stays entirely within $\widetilde\M_R$; the moment $s$ crosses $s_0$, operators from
$\widetilde\M_L$ suddenly, sharply appear in $\Phi(X;s)$ — exactly the moment the flowed point crosses the
horizon (Fig.~29(a)). And checking commutators directly: for two points $X_1\in R,X_2\in L$,
$[\Phi(X_1,s),\phi(X_2)]$ stays exactly zero until $s$ crosses a precise threshold $s_{12}=-U_1+U_2$, then
becomes nonzero (eq.~8.10, Fig.~29(b)) — **sharp causal structure, reproduced exactly, out of an
evolution built entirely from algebraic data with no bulk light-cone put in by hand**.

### Worked derivation: Kruskal coordinates and horizon crossing in BTZ

To see the algebra translate a point across the horizon with explicit formulas, consider the non-rotating BTZ black hole in $\text{AdS}_3$ with metric:

$$

ds^2 = -\frac{r^2 - r_+^2}{R^2} dt^2 + \frac{R^2}{r^2 - r_+^2} dr^2 + \frac{r^2}{R^2} d\phi^2

$$

The surface gravity at the horizon $r = r_+$ is $\kappa = \frac{r_+}{R^2} = \frac{2\pi}{\beta}$. Define the radial tortoise coordinate $r^*(r)$:

$$

r^*(r) \equiv \int \frac{R^2}{r^2 - r_+^2} dr = \frac{1}{2\kappa} \log\left(\frac{r - r_+}{r + r_+}\right) \in (-\infty, 0)

$$

In the right exterior wedge $R$ ($r > r_+$), define the Kruskal null coordinates:

$$

U \equiv -e^{-\kappa(t - r^*)}, \qquad V \equiv e^{\kappa(t + r^*)}

$$

Notice their properties in region $R$:

- $U < 0$ and $V > 0$ throughout region $R$.
- As $r \to r_+$ ($r^* \to -\infty$), $UV = -e^{2\kappa r^*} \to 0$.
- The future event horizon $\mathcal{H}^+$ is the null surface $U = 0$, $V > 0$.
- The interior future region $F$ (behind the horizon) is described by $U > 0, V > 0$.

The boundary single-trace algebra $Y_R$ has modular generator $K_{Y_R} = \beta H_R = \frac{2\pi}{\kappa}(V\partial_V - U\partial_U)$, which generates Lorentz boosts in the $(U,V)$ plane leaving the horizon fixed ($U \mapsto e^{-2\pi s}U, V \mapsto e^{2\pi s}V$).

The half-sided modular translation generator $G_+ = \frac{1}{2\pi}(K_{Y_R} - K_{Y_-})$ instead acts near the horizon as a constant affine translation along the null generator:

$$

G_+ = \frac{1}{\kappa} \frac{\partial}{\partial U}

$$

Now consider an operator $\phi(U_0, V_0)$ initialized at a point $(U_0, V_0)$ in the right exterior ($U_0 < 0$). Evolving under $G_+$ for parameter $s \ge 0$:

$$

\Phi(s) \equiv e^{i G_+ s} \phi(U_0, V_0) e^{-i G_+ s} = \phi(U_0 + s,\, V_0)

$$

Let us trace the coordinate $U(s) = U_0 + s$ as the flow parameter $s$ increases:

1. For $0 \le s < -U_0$: $U(s) < 0$. The point remains strictly inside the right exterior wedge $R$. Therefore $\Phi(s) \in \widetilde\M_R = Y_R$.
2. At $s = s_0 \equiv -U_0$: $U(s_0) = 0$. The point hits the future horizon $\mathcal{H}^+$!
3. For $s > -U_0$: $U(s) = U_0 + s > 0$. Since $V_0 > 0$ and $U(s) > 0$, the operator has entered the **black hole interior** region $F$.

By Haag duality and causal reconstruction, an operator at $U > 0, V > 0$ cannot commute with the left exterior algebra $\widetilde\M_L = Y_L$. For any operator $\phi(X_L)$ located at $X_L = (U_L, V_L)$ in the left wedge (where $U_L > 0, V_L < 0$), the commutator $[\Phi(s), \phi(X_L)]$ switches discontinuously from $0$ to a nonzero value at the exact threshold $s_{12} = -U_0 + U_L$.

This provides a transparent mathematical proof: the algebraic generator $G_+$, built purely from boundary modular data, translates degrees of freedom across the horizon into the interior, directly resolving the meeting-behind-the-horizon puzzle.

(In a suitable large
conformal-weight limit, this flow even becomes a genuinely *emph* bulk transformation, eqs.~8.11—8.12,
with trajectories running smoothly into the black hole singularity as $s$ approaches a further critical value
— and $G_\pm$ together with the boost $K$ close into an $SL(2,\mathbb R)$ algebra, exactly the 2d conformal
structure already previewed abstractly in Sec.~IV.E.) Finally, a clean consistency check: below
$T_{\text{HP}}$, $Y_R$ is type I, for which half-sided modular inclusion simply cannot occur (Sec.~IV.E's
theorem required type $\mathrm{III}_1$) — exactly matching the bulk fact that the two boundaries really are
disconnected there, with no horizon and nothing to cross.

## Sec.~VIII.C: emergent spacetime connectivity — algebraic ER$=$EPR

### Why the naive slogan needs fixing

The naive ER$=$EPR slogan — any two entangled gravitational systems are connected by some kind of
Einstein—Rosen bridge — runs into two genuine problems once examined carefully. **First**: below
$T_{\text{HP}}$ in the thermofield double, $R$ and $L$ are certainly entangled (an $O(G_N^0)$ amount), but the
bulk dual is two entirely *emph* copies of AdS (Sec.~VI.C) — so ``entangled $\Rightarrow$
connected'' is already false as stated, unless you're willing to call this a "quantum wormhole" with no
independent definition of what that even means. **Second**, and sharper: even refining the slogan to
require $O(1/G_N)$ (i.e., large, semiclassical) entanglement specifically doesn't survive scrutiny — in an
evaporating black hole, at a time $t<t_P$ (before the Page time) but still with $O(1/G_N)$ entanglement
between the black hole and its already-emitted, causally disconnected radiation, the two systems are
*emph* despite the large entanglement. Amount of entanglement alone, at any
threshold, simply isn't the right diagnostic.

### The fix: entanglement *emph*}

The resolution builds directly on everything established so far in this section: Sec.~VI.C already showed that
classical bulk connectivity (a genuine, classical Einstein—Rosen bridge) corresponds to $Y_R,Y_L$ both being
type $\mathrm{III}_1$; Sec.~VIII.B just showed that type $\mathrm{III}_1$, specifically, is what makes
half-sided modular inclusion — and hence a genuine causal connection through the horizon — possible at all.
**Algebraic ER$=$EPR** promotes this from an observation into a clean, three-way classification. For two
entangled systems $R_1,R_2$ in a pure semiclassical state, with bulk dual $W_{R_1R_2}$ (every part of it
touching some boundary), and algebras $\M_{R_1},\M_{R_2}$:

- $W_{R_1R_2}$ is **disconnected** $\iff$ $\M_{R_1}$ and $\M_{R_2}$ are both type I.
- $W_{R_1R_2}$ has a **classical** wormhole $\iff$ $\M_{R_1},\M_{R_2}$ are both type $\mathrm{III}_1$
*emph* $W_{R_1R_2}$ is classical.
- $W_{R_1R_2}$ has a **quantum** wormhole $\iff$ $W_{R_1R_2}$ is **quantum volatile** and
$\M_{R_1},\M_{R_2}$ are not type I.

Here **quantum volatile** means the bulk spacetime fails to be classical in the $G_N\to0$ limit even
though the limit is being taken — concretely, either diffeomorphism-invariant fluctuations fail to vanish as
$G_N\to0$, or some genuine geometric quantity (a length, an area, a volume) blows up as $O(G_N^{-a})$ instead
of staying finite. The paradigm example, worth keeping firmly in mind, is exactly the evaporating black hole
around the Page time: the interior connecting the black hole to its radiation has a *emph* that
scales as $O(1/G_N)$ — diverging as $G_N\to0$ — which is precisely why it counts as quantum volatile rather
than an ordinary classical wormhole, even though the entanglement supporting it is large.

This resolves both problems cleanly. Below $T_{\text{HP}}$, both boundary algebras are type I — algebraic
ER$=$EPR correctly reports *emph* wormhole of either kind, fixing the first counterexample directly.
For the evaporating black hole: before the Page time, the entanglement wedge connecting black hole and
radiation is quantum volatile (that $O(1/G_N)$ interior length), so the connection there is a *emph*
wormhole, not a classical one — the second counterexample is defused by correctly classifying it as quantum
rather than either "no wormhole" or "ordinary classical wormhole." After the Page time, the entanglement
wedge becomes genuinely classical, connecting to the radiation by an honest classical wormhole anchored at
the quantum extremal surface. (A refinement of the causal-depth parameter from Sec.~VIII.A — a *emph*
depth, built from modular rather than ordinary time bands — sharpens this even further, distinguishing the
two regimes even though the boundary algebra is type $\mathrm{III}_1$ throughout: finite before the Page time,
divergent after.)

One clarifying caveat, worth keeping: this whole classification is stated for the strict $\alpha'\to0$ (large
't~Hooft coupling) limit, where genuinely geometric concepts apply in the bulk at all. In the stringy regime —
taken up next — type $\mathrm{III}_1$ alone stops being sufficient to guarantee connectivity, and the story
needs further refinement.

## Sec.~VIII.D: stringy geometry and stringy black holes (in brief)

Everything so far assumed the bulk is well described by ordinary Einstein gravity coupled to matter — valid
in the strict $N\to\infty$, $\lambda\to\infty$ ('t~Hooft coupling, equivalently $\alpha'\to0$) double limit. At
finite $\lambda$ (finite string tension), an infinite tower of massive stringy fields appears, and the very
notion of a sharp bulk causal region — built, throughout this section, from ordinary field-theoretic causal
wedges and RT surfaces — becomes considerably more delicate: stringy effects are famously non-local at the
string scale, so the clean dictionary between bulk causal structure and boundary commutant structure
developed above needs real modification. The paper's own treatment here (its Sec.~VIII.D.1—2) works through,
in outline, how boundary operator algebras can still be used to probe causal structure and define an
analogue of a horizon in this regime, and specifically how the half-sided-modular-inclusion mechanism behind
Kruskal time (Sec.~VIII.B) generalizes to a stringy black hole — concluding that type $\mathrm{III}_1$
structure alone is no longer sufficient for connectivity once stringy effects are included, refining the
algebraic ER$=$EPR classification of the previous subsection. This material is genuinely more exploratory and
technical than the rest of the section, and is flagged here in summary rather than walked through in full
detail, since the core conceptual arc of the paper — algebra $\to$ entanglement type $\to$ emergent spacetime
— does not depend on it; it is the frontier of the subject, not its foundation.

\bigskip
\noindent With bulk causal structure, horizon formation, and spacetime connectivity now all read directly off
boundary algebra data, Sec.~IX turns to a different kind of question: rather than analyzing an existing
holographic theory, it builds simple, fully solvable *emph* of quantum gravity directly out of
operator algebras — using the crossed product of Sec.~V, now applied not as an abstract construction but as
the literal mechanism by which a physical observer's own clock produces the Bekenstein—Hawking area term and
de~Sitter entropy.



---

# Sec.~IX: Algebraic approaches to quantum-gravity regimes

Sections~VI—VIII analyzed an existing structure — AdS/CFT — using the machinery built in Secs.~II—V. This
section does something different and, in a sense, more ambitious: it builds simple, completely solvable
*emph* of quantum gravity directly out of operator algebras, with the crossed product of Sec.~V
appearing not as an abstract mathematical device but as the literal, physical mechanism that turns a quantum
field theory's type $\mathrm{III}_1$ algebra into the finite, well-defined entropy of a black hole or of
de~Sitter space. This is the payoff the whole crossed-product construction was built for.

## Sec.~IX.A: a model of gravitational dressing from observers

### Setting up the constraint

Start with an ordinary quantum field theory on Hilbert space $\HH_Q$, and let $\M$ be the algebra of some
region, $\M'$ its commutant, both type $\mathrm{III}_1$, with a cyclic-separating reference $\ket\Psi$ and
modular Hamiltonian $K$ generating the usual internal time flow (Sec.~IV.A, eq.~9.1) on $\M$ and $\M'$.

Now attach two observers, $R$ and $L$, each with their own Hamiltonian $\hat q_R,\hat q_L$ and conjugate
clock-reading operators $\hat p_R,\hat p_L$ (with clock-reading eigenstates $\ket\tau_R,\ket\tau_L$). Demand
the *emph* system — field theory plus both observers — be invariant under translations generated by

$$

H = K + \hat q_R - \hat q_L

$$

(eq.~9.2) — a toy **Hamiltonian constraint**, built to mimic the way general relativity's own Hamiltonian
constraint works: there's no external clock, only relative readings between subsystems, exactly the way
diffeomorphism invariance in gravity means only relational data (not absolute time) is physical.

The naive way to build gauge-invariant states — projecting with $\Pi\equiv\int_{-\infty}^\infty dt\,e^{-iHt}$
(eq.~9.4) — fails, because $\Pi^2\propto\Pi\int dt$ diverges (eq.~9.5): the projector isn't normalizable, the
same obstruction met (and resolved) back in Sec.~V. The fix, worked out carefully here rather than just
regularized away: define physical states as *emph* $[\psi]$ under $\Pi\ket{\psi_1}=
\Pi\ket{\psi_2}$ (eq.~9.6 — states related by the gauge flow $e^{iHt}$ count as the same physical state), with
inner product $(\psi|\phi)\equiv\braket{\psi|\Pi|\phi}$ (eq.~9.7, checkably well-defined on equivalence
classes alone).

### Gauge-fixing, and two equivalent presentations

Any state can be gauge-fixed by pinning the $L$-observer's clock to a specific reading $\tau$: expanding a
general state in the joint clock-reading$\times$field basis (eq.~9.9), one shows explicitly that $\ket\psi\sim
\ket\tau_L\otimes\ket{\psi_\tau}_{RQ}$ for $\ket{\psi_\tau}_{RQ}\equiv{}_L\!\bra\tau\Pi\ket\psi$ (eqs.~9.8,
9.10) — and this map from the physical (gauge-invariant) Hilbert space to $\HH_R\otimes\HH_Q$ is an honest
isometry (eq.~9.11, checked directly from the definitions). In this gauge, $\hat q_L$ is no longer an
independent dynamical variable — the constraint (eq.~9.2, set to zero) solves it as a composite operator,
$\hat q_L=\hat q_R+K$ (eq.~9.12). Symmetrically, gauge-fixing the $R$-observer's clock instead gives $\hat q_R
=\hat q_L-K$ (eq.~9.15). These are two different, but physically equivalent, ways of describing exactly the
same gauge-invariant physics.

### Dressed operators, and the crossed product falls out automatically

A gauge-invariant (physical) operator must commute with $H$. Starting from $A\in\M$ (or $A'\in\M'$), the
gauge-invariant, "dressed" version — literally the operator $A$, tagged with the $R$-observer's clock
reading $\tau$ — is built by integrating over the gauge group,

$$

\widehat A_R(\tau) \equiv \int dt\,e^{iHt}\big(\ket\tau\!\bra\tau_R\otimes A\big)e^{-iHt}
= e^{iK\hat p_R}A(-\tau)e^{-iK\hat p_R}

$$

(eq.~9.16, with the mirror construction $\widehat A'_L(\tau)$ for $A'\in\M'$, eq.~9.17) — and by construction
$[\widehat A_R(\tau),H]=0$. It is worth pausing on the phrase in the paper describing this precisely: the
clock reading $\tau$ appearing in $\widehat A_R(\tau)$ is now a *emph*, not a classical
coordinate — in a generic state (not an eigenstate of $\hat p_R$), it genuinely fluctuates. **The dressed
operators live in a quantum spacetime.** The algebra generated by all such dressed operators, together with
clock translations, is

$$

\widehat\M \equiv \big\{\widehat A_R = e^{iK\hat p_R}Ae^{-iK\hat p_R},\ e^{i\hat q_Rs}\ \big|\ A\in\M,\
s\in\mathbb R\big\}''

$$

(eq.~9.19) — and this is, symbol for symbol, exactly the crossed-product algebra $\widehat\M$ constructed
abstractly in Sec.~V.A (eq.~5.6), with the clock $\hat q$ there identified with the $R$-observer's own
Hamiltonian $\hat q_R$ here.

### Worked derivation: solving the relational constraint and dressing operators

To see this constraint solving and dressing algebraically, let us work out the quantum mechanics of the relational Hamiltonian constraint:

$$

H = K + \hat q_R - \hat q_L = 0

$$

Let the observers' clock variables satisfy the canonical commutation relations $[\hat p_L, \hat q_L] = -i$ and $[\hat p_R, \hat q_R] = -i$. In the clock-reading representation $\ket{\tau_L}$, the Hamiltonian operator acts as a differential operator $\hat q_L = i \frac{\partial}{\partial \tau_L}$.

A physical (gauge-invariant) wavefunction $\ket{\Psi_{\text{phys}}}$ must satisfy the Wheeler—DeWitt-like equation:

$$

H \ket{\Psi_{\text{phys}}} = 0 \implies \left(K + \hat q_R - i \frac{\partial}{\partial \tau_L}\right) \psi(\tau_L) = 0

$$

Integrating this first-order differential equation immediately yields:

$$

\psi(\tau_L) = e^{-i(K + \hat q_R)\tau_L} \psi(0)

$$

Thus the entire $\tau_L$-dependence is completely determined by the data on the initial slice $\tau_L = 0$. Choosing the gauge $\tau_L = 0$ provides a faithful, isometric embedding of the physical Hilbert space into $\HH_R \otimes \HH_Q$:

$$

\ket{\Psi_{\text{phys}}} \longleftrightarrow \ket{\psi(0)}_{RQ} \in \HH_R \otimes \HH_Q

$$

In this gauge, the $L$-clock momentum is eliminated via the constraint $\hat q_L = K + \hat q_R$.

Now consider dressing an operator $A \in \M$ to make it gauge-invariant under the flow $e^{i H t}$. The group-averaged operator is:

$$

\widehat A_R(\tau) \equiv \int_{-\infty}^\infty dt\, e^{i H t} \big(\ket\tau\!\bra\tau_R \otimes A\big) e^{-i H t}

$$

Evaluating the action of this operator on the physical gauge slice $\tau_L = 0$ using $e^{i H t} = e^{i (K + \hat q_R) t} e^{-i \hat q_L t}$:
\begin{align*}
\widehat A_R(\tau) &= \int_{-\infty}^\infty dt\, e^{i(K + \hat q_R)t} \big(\ket\tau\!\bra\tau_R \otimes A\big) e^{-i(K + \hat q_R)t} \\
&= \int_{-\infty}^\infty dt\, \big(\ket{\tau + t}\!\bra{\tau + t}_R\big) \otimes \big(e^{i K t} A e^{-i K t}\big)
\end{align*}
Since the clock momentum operator $\hat p_R$ is diagonal in the clock basis ($\hat p_R \ket\tau_R = \tau \ket\tau_R$), the continuous shift $\ket{\tau + t} = e^{i \hat q_R t} \ket\tau$ allows the integral over $t$ to be evaluated in closed form. Setting $t = -\hat p_R - \tau$:

$$

\widehat A_R(\tau) = e^{i K \hat p_R} A(-\tau) e^{-i K \hat p_R}

$$

Let us check directly that this dressed operator commutes with the total generator $K + \hat q_R$:

$$

\big[K + \hat q_R,\, \widehat A_R(\tau)\big] = \big[K,\, \widehat A_R(\tau)\big] + \big[\hat q_R,\, e^{i K \hat p_R} A(-\tau) e^{-i K \hat p_R}\big]

$$

Using $[\hat q_R, e^{\pm i K \hat p_R}] = \mp K e^{\pm i K \hat p_R}$ (from $[\hat q_R, \hat p_R] = i$), the commutator evaluates to:

$$

\big[K + \hat q_R,\, \widehat A_R(\tau)\big] = i \frac{\partial}{\partial \tau}\widehat A_R(\tau) - i \frac{\partial}{\partial \tau}\widehat A_R(\tau) = 0

$$

The operator $\widehat A_R(\tau)$ is genuinely gauge-invariant. The algebra generated by $\{\widehat A_R, e^{i\hat q_R s}\}$ is identically the crossed-product algebra $\M \rtimes_\sigma \mathbb{R}$.

**Gravitational dressing to a physical observer's clock *emph* — not an analogy, a literal identity, checkable by comparing the two
constructions gauge-fixing choice for gauge-fixing choice: fixing the $L$-observer's clock at $\tau=0$
reproduces exactly eqs.~5.6/5.8 of Sec.~V; fixing the $R$-observer's instead reproduces eqs.~5.10/5.11
(eqs.~9.19—9.22 walk through both cases explicitly). And since $K$ here is a genuine modular Hamiltonian,
Sec.~V.B's theorem applies immediately: $\widehat\M$ and $\widehat\M'$ are type $\mathrm{II}_\infty$, with
honest density operators and entropies — no further argument needed, since it's literally the same
construction already proven there.

## Sec.~IX.B: Application I — quantum volatile black hole spacetime and its entropy

Apply the model directly to the eternal AdS black hole: $\HH_Q$ is the bulk QFT in the black-hole geometry at
$G_N\to0$, $\ket\Psi$ is the Hartle—Hawking vacuum, $\M=\widetilde\M_R$, $\M'=\widetilde\M_L$, and $K$
generates ordinary Schwarzschild time. With two genuine asymptotic boundaries available, it's natural to
identify the $R,L$ "observers" of Sec.~IX.A with the two boundaries themselves, and $\hat q_R,\hat q_L$ with
(mean-subtracted) perturbations of the boundary Hamiltonians $H_R,H_L$ around their background values —
concretely, in a microcanonical thermofield double (eq.~9.23, peaked around energy $E_0\sim O(N^2)$ with an
$O(N^0)$ spread), $\hat q_R\equiv H_R-\braket{H_R}$.

The crossed-product algebras (eqs.~9.19—9.20) are type $\mathrm{II}_\infty$ — and this genuinely reflects a
change in the physical spacetime structure. The gauge-invariant, but now quantum, quantity $\hat p_R+\hat p_L$
(the time separation between the $R$ and $L$ boundaries, represented geometrically by a geodesic running
between them, Fig.~32 of the paper) has $O(1)$ fluctuations as $G_N\to0$ — precisely an example of the
**quantum volatile geometry** flagged already in Sec.~VIII.C: **the two boundaries are connected
by a genuine quantum wormhole**, not a classical one.

Now the entropy payoff, worth stating as explicitly as the paper does because it's the cleanest closing of the
loop opened at the start of Sec.~V. For a semiclassical excited state $\ket{\widehat\Phi}=\ket\Phi\otimes\ket
g$ (exactly Sec.~V.D's construction), the crossed-product entropy is, by eq.~5.49,

$$

S_{\widehat\M_R}^{(\widehat\Phi)} = -S(\Phi\|\Psi) + \text{const} .

$$

Separately (a genuine gravitational computation, cited here rather than re-derived), it has been shown that
— assuming the system relaxes back to the equilibrium state $\ket\Psi$ as $t\to\infty$ — this same relative
entropy is exactly (minus, up to the same additive constant) the ordinary generalized entropy of the
excited state, $S(\Phi\|\Psi)=-S_{\text{gen}}^{(\Phi)}+\text{const}$ (eq.~9.27). Combining the two:

$$

S_{\widehat\M_R}^{(\widehat\Phi)} = S_{\text{gen}}^{(\Phi)} + \text{const}

$$

(eq.~9.28) — **the type II entropy of the gravitationally dressed algebra literally *emph* Every step in this chain — crossed product, type II, its entropy formula — was already proved in
full generality in Sec.~V; nothing new needed to be assumed here beyond identifying the abstract construction
with a real black hole.

## Sec.~IX.C: Application II — de Sitter entropy

### The puzzle

De~Sitter space has no boundary at all — quantum gravity there faces a much deeper "problem of time" than
AdS does, with no asymptotic region to anchor observables to. A static observer (sitting at a pole of the
spatial sphere) only ever accesses a **static patch**, bounded by a cosmological horizon at the de~Sitter
radius $R$ (eq.~9.29, Fig.~33 of the paper). The horizon carries the celebrated Gibbons—Hawking entropy,
$S_{\text{dS}}=A_{\text{hor}}^{(0)}/4G_N$ (eq.~9.30) — but its physical meaning has been debated for decades
(does its exponential count a genuine, finite-dimensional de~Sitter Hilbert space, for instance?), with little
concrete progress.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.82\textwidth]{figs/fig_desitter.pdf}
\caption{Penrose diagram of global de~Sitter spacetime and the static patch. The static observer at the north pole $r=0$ (blue trajectory) only ever accesses Region $R$ (shaded blue), bounded by the cosmological event horizons $\mathcal{H}^\pm$ at $r=R$. The south pole observer accesses the causally disconnected antipode Region $L$ (shaded yellow). The crossed-product algebra of observables $\widehat{\mathcal{M}}_R$ is a type $\mathrm{II}_1$ factor, whose maximal entropy state is empty de~Sitter.}
\label{fig:desitter}
\end{figure}

Here is a genuinely strange feature of the *emph* de~Sitter entropy, $S_{\text{gen}}=A_{\text{hor}}
/4G_N+\widetilde S_R$ (eq.~9.31), worth sitting with because it's the opposite of a black hole's behavior:
**exciting matter in the static patch *emph*}$}, because it shrinks the
cosmological horizon area faster than it grows the matter entanglement $\widetilde S_R$. This can be checked
completely explicitly: put a black hole of mass parameter $\mu$ inside the static patch (eq.~9.32, giving a
black-hole horizon at $r_b$ nested inside the cosmological horizon at $r_c>r_b$), representing $\widetilde
S_R$ by the black-hole horizon area itself, and the generalized entropy comes out to
$S_{\text{gen}}=\omega_{d-2}(r_c^{d-2}+r_b^{d-2})/4G_N$ (eq.~9.33), which is checkably *emph* than
$S_{\text{dS}}$ — so $S_{\text{dS}}$ is the maximum possible value of $S_{\text{gen}}$, achieved exactly by
empty de~Sitter (eq.~9.34).

### Worked calculation: why matter excitations decrease de~Sitter entropy

To see this remarkable thermodynamic behavior in detail, consider a four-dimensional Schwarzschild—de~Sitter spacetime with metric:

$$

ds^2 = -f(r) dt^2 + \frac{dr^2}{f(r)} + r^2 d\Omega_2^2, \qquad f(r) = 1 - \frac{2 G_N M}{r} - \frac{r^2}{R^2}

$$


1. **Empty de~Sitter space ($M = 0$)**:
The horizon condition $f(r) = 1 - r^2/R^2 = 0$ gives a single cosmological horizon at $r_c^{(0)} = R$.
The cosmological horizon area is $A_{\text{dS}} = 4\pi R^2$, giving the Gibbons—Hawking entropy:

$$

S_{\text{dS}} = \frac{A_{\text{dS}}}{4 G_N} = \frac{\pi R^2}{G_N}

$$

2. **Matter excitation: small black hole ($0 < G_N M \ll R$)**:
For a localized excitation of mass $M$, the horizon equation $f(r) = 0$ has two positive roots: a black hole horizon at $r_b$ and a shifted cosmological horizon at $r_c < R$.
Let $r_c = R(1 - \delta)$ with $\delta \ll 1$. Expanding $f(r_c) = 0$ to first order in $\delta$ and $M$:

$$

1 - \frac{2 G_N M}{R} - (1 - 2\delta) \approx 0 \implies \delta = \frac{G_N M}{R}

$$

Therefore the cosmological horizon shrinks to $r_c \approx R\left(1 - \frac{G_N M}{R}\right)$.
Its shifted area is:

$$

A_c(M) = 4\pi r_c^2 \approx 4\pi R^2 \left(1 - \frac{2 G_N M}{R}\right) = A_{\text{dS}} - 8\pi G_N M R

$$

The black hole horizon is at $r_b \approx 2 G_N M$, with area $A_b(M) = 4\pi r_b^2 \approx 16\pi G_N^2 M^2 \sim O(G_N^2 M^2)$.
The total generalized entropy is the sum of both horizon areas:
\begin{align*}
S_{\text{gen}}(M) &= \frac{A_c(M)}{4 G_N} + \frac{A_b(M)}{4 G_N} \\
&= \frac{A_{\text{dS}} - 8\pi G_N M R}{4 G_N} + O(G_N M^2) \\
&= S_{\text{dS}} - 2\pi M R + O(G_N M^2)
\end{align*}

Notice that $\beta_{\text{dS}} = 2\pi R$ is the inverse Hawking—de~Sitter temperature. Thus, to linear order in perturbation:

$$

S_{\text{gen}}(M) - S_{\text{dS}} = -\beta_{\text{dS}} M < 0 \quad \text{for all } M > 0

$$

Any localized energy excitation inside the static patch strictly **lowers** the generalized entropy. Consequently, empty de~Sitter ($M = 0$) is the unique state of **maximal entropy**.

### Recognizing the type $\mathrm{II_1$ signature}

This behavior — a reference state whose entropy can only ever decrease under perturbation — is exactly what
you already saw, worked out on an explicit example, in Sec.~III.C's type $\mathrm{II}_1$ Bell-pair chain
(eq.~3.22: perturbing away from the maximally entangled $\ket{\Phi_{\pi/4}}$ always gives $S_\M(\Psi)\le0$).
**This is the key recognition of this subsection: empty de~Sitter behaves exactly like the maximally
entangled reference state of a type $\mathrm{II**_1$ algebra, with $R$ and $L$ static patches playing the role
of the two entangled halves.}

Making this precise uses exactly the model of Sec.~IX.A, with one small but crucial modification. Take
$\HH_Q$ to be the QFT Hilbert space on global de~Sitter, $\ket\Psi$ the Bunch—Davies vacuum, $\M,\M'$ the $R$-
and $L$-patch algebras (modular Hamiltonian $K$ = the boost generator of $t$-translations), and $\hat q_R,\hat
q_L$ the Hamiltonians of static observers at the two poles. This reproduces $\widehat\M_R,\widehat\M_L$ exactly
as before — *emph* that now $\hat q_R,\hat q_L$ are required to be **bounded below** (non-negative
eigenvalues — physically, the sensible statement that a real observer's energy can't be negative). By exactly
the mechanism checked explicitly in Sec.~V.B (eq.~5.26: restricting the clock spectrum to $q\ge0$ turns a
divergent trace into a normalized one), $\widehat\M_R,\widehat\M_L$ become type $\mathrm{II}_1$, not type
$\mathrm{II}_\infty$. The type $\mathrm{II}_1$ entropy relative to the maximally-entangled reference state
$\ket{\widehat\Psi_T}=e^{-\hat q/2}\otimes\ket0_{\text{BD}}$ (eq.~9.35, with trace $\tr(\cdots)\equiv\braket{
\widehat\Psi_T|\cdots|\widehat\Psi_T}$, eq.~9.36) is negative exactly the way Sec.~III.C's example was, and
for the identical reason: there is no unentangled reference to fall below zero from, only a maximally
entangled one to fall below.

One more consistency check, worth working through because it resolves an objection that looks fatal at first
glance: if empty de~Sitter is a maximally entangled state, shouldn't it have infinite temperature (the way a
maximally entangled Bell pair has infinite temperature in the entanglement-Hamiltonian sense)? The resolution:
the state $\ket{\widehat\Psi_T}$ has density operator $\rho=e^{-K}$ on the crossed-product algebra — a
thermal state at *emph* temperature exactly $1$ (the universal modular temperature from
Tomita—Takesaki theory, Sec.~IV.A). Converting this dimensionless $\beta=1$ into physical units using the
static observer's own proper time (parametrized by $t$ in eq.~9.29) reproduces exactly the known,
finite, de~Sitter temperature $T_{\text{dS}}=1/2\pi R$ — no contradiction, because "maximally entangled"
was always a dimensionless, modular-time statement, and the finite physical temperature only appears once you
convert to an observer's physical clock.

\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.3}
\begin{tabularx}{\textwidth}{>{\bfseries\color{navyhead}}l >{\raggedright\arraybackslash}X >{\raggedright\arraybackslash}X}
\toprule
Property & Black Hole Exterior (AdS/Minkowski) & de~Sitter Static Patch \\
\midrule
Spacetime Horizon & Event horizon (null boundary of black hole interior) & Cosmological horizon (null boundary of observer static patch) \\
Horizon Temperature & Hawking temperature $T_H = \frac{1}{8\pi G_N M}$ & Gibbons—Hawking temperature $T_{\text{dS}} = \frac{H}{2\pi} = \frac{1}{2\pi R}$ \\
Killing Vector $\chi = \partial_t$ & Timelike outside; null on horizon; timelike again at spatial infinity & Timelike inside static patch; null on cosmological horizon; spacelike outside \\
Reference Vacuum State & Hartle—Hawking vacuum $\ket{\Psi_{\text{HH}}}$ & Bunch—Davies vacuum $\ket{0_{\text{BD}}}$ \\
Clock Hamiltonian $\hat q$ & $\hat q \in (-\infty, \infty)$ (unbounded real line) & $\hat q \ge 0$ (energy bounded below for physical observer) \\
Crossed Product Algebra & Type $\mathrm{II}_\infty$ factor ($\tr(\id) = \int_{-\infty}^\infty dq\,e^{-q} = \infty$) & Type $\mathrm{II}_1$ factor ($\tr(\id) = \int_0^\infty dq\,e^{-q} = 1$) \\
Entropy Formula & $S_{\widehat\M} = -S(\Phi\|\Psi) + \text{const} = S_{\text{gen}} + \text{const}$ & $S_{\widehat\M} \le 0$ (relative to maximally entangled empty de Sitter) \\
Perturbation Response & $\Delta S_{\text{gen}} > 0$ (adding matter increases horizon area) & $\Delta S_{\text{gen}} = -\beta_{\text{dS}} M < 0$ (matter shrinks cosmological horizon) \\
Maximal Entropy State & None (entropy can grow unboundedly with mass $M$) & Empty de~Sitter ($M = 0$, $S_{\text{max}} = S_{\text{dS}} = \frac{\pi R^2}{G_N}$) \\
\bottomrule
\end{tabularx}
\caption{Comprehensive algebraic and thermodynamic comparison between the black hole exterior and the de~Sitter static patch under the crossed-product construction.}
\label{tab:bh_vs_desitter}
\end{table}

## Sec.~IX.D: Application III — generalized entropy for a local spacetime region (in brief)

The black hole and de~Sitter examples both had a special simplifying feature: a single reference state existed
whose modular Hamiltonian coincided exactly with an honest geometric (isometric) time flow. A more general
region — the paper's example is Schwarzschild—de~Sitter (eq.~9.32, Fig.~34 of the paper: a black hole sitting
inside a de~Sitter universe, so the observer's accessible region is bounded by *emph* horizons at
different temperatures, $r_b<r_c$) — has no single global geometric modular flow at all, since the two
horizons don't share a common temperature. The fix generalizes the construction cleanly: decompose the
region's algebra as $\M_R=\M_c\otimes\M_b$ (cosmological- and black-hole-horizon factors), choose a state
making *emph* factor's modular flow separately geometric, and introduce two independent pairs of
observer Hamiltonians, one for each horizon, with two separate constraints (eq.~9.37, one per horizon). A
genuinely interesting wrinkle, worth remembering because it shows the type isn't always what naive analogy
would suggest: even with both sets of observer Hamiltonians bounded below, the resulting algebra comes out
type $\mathrm{II}_\infty$, not type $\mathrm{II}_1$ — and its entropy reproduces exactly the expected sum of
both horizon areas plus bulk matter entropy, $S_{\text{gen}}=A_{\text{cos}}/4G_N+A_{\text{BH}}/4G_N+
\widetilde S_R$ (eq.~9.38). This is presented in the paper as evidence that the crossed-product mechanism is
robust and general, not a special property of the two simplest (black hole, de~Sitter) examples.

## Sec.~IX.E: a model of dynamical observers (in brief)

Every model so far treated the observer's own trajectory as fixed, non-dynamical — only its clock was quantum
mechanical. A more honest model lets the observer itself be a genuine, finite-mass dynamical particle, worked
out explicitly here for two-dimensional de~Sitter space: promoting the particle's mass to a dynamical variable
$Q(\tau)$ with conjugate $P(\tau)$ (eq.~9.40) and gauging the full de~Sitter isometry group (rather than just
time translations) produces a genuinely richer physical Hilbert space, with gauge-invariant, "dressed" field
operators $\phi_R$ built by projecting onto observer-frame matrix elements (eq.~9.42). A key structural result:
the resulting observer algebra $\Alg_R$ turns out to be a direct integral of type $\mathrm{I}_\infty$ factors —
because a genuinely dynamical observer can change its own trajectory, there's no fixed subregion its dressed
operators stay confined to, so they end up smeared, state-dependently, over an entire Cauchy slice. The
static-observer limit of Sec.~IX.C is recovered by sending the observer's mass $\Lambda\to\infty$ — but,
worth noting as a genuinely subtle point, this limit does *emph* commute with taking the double
commutant: take $\Lambda\to\infty$ first and you recover the emergent type II algebra (and its
Gibbons—Hawking entropy) of Sec.~IX.C; take the double commutant first and then send $\Lambda\to\infty$, and
you get type I instead. The type II structure — and the cosmological horizon's very existence as an entropic
object — is itself an emergent, order-of-limits-dependent phenomenon.

With a large but finite observer mass, the observer's position becomes increasingly uncertain over time (an
initial position uncertainty $1/\Lambda$ grows to $\sim e^{2\pi\tau/\beta_{\text{dS}}}/\Lambda$ after proper
time $\tau$, from the exponential expansion of de~Sitter), defining a natural **scrambling time**
$\tau_s\equiv\tfrac{\beta_{\text{dS}}}{2\pi}\log\Lambda$ (eq.~9.44) after which the observer has an $O(1)$
chance of leaving its original static patch. This scrambling shows up concretely in an out-of-time-order
correlator (a standard chaos diagnostic): even though the matter field itself is free and doesn't directly
interact with the observer, the gravitational constraint couples them nontrivially — inserting an operator
along the observer's worldline physically "kicks" its trajectory, and this recoil produces genuine quantum
chaotic behavior, with a decay rate matching a Lyapunov exponent of $4\pi/\beta_{\text{dS}}$ (eq.~9.47) —
twice the universal chaos bound, matching a mechanism identified independently in other contexts.

## Sec.~IX.F: operator algebras of JT gravity (in brief)

The chapter closes with a genuinely remarkable exact result, in a setting simple enough to solve completely
rather than only perturbatively: **Jackiw—Teitelboim (JT) gravity**, a two-dimensional gravity theory
(with a scalar "dilaton" field $\Phi$) coupled to matter, whose gravitational sector reduces entirely to
boundary dynamics once the dilaton's own equation of motion is solved (eq.~9.49, forcing the bulk geometry to
be locally exact AdS$_2$, eq.~9.50). The theory's genuine gauge freedom (the isometry group of AdS$_2$)
locks the two boundaries' Hamiltonians together, $H_L=H_R\equiv H$, reducing the classical phase space to just
two variables — equivalently, the boundary geodesic separation $\ell$ and its conjugate momentum — which can
be canonically quantized into a Hilbert space $L^2(\mathbb R)$, with an (overcomplete) basis of states
$\ket\beta$, $\beta\in\mathbb R_{>0}$, built from a Euclidean path integral (Fig.~36 of the paper). Including
matter fields (which don't couple directly to the dilaton), the full quantum-gravitational Hilbert space
becomes $\HH=L^2(\mathbb R)\otimes\HH_{\text{matt}}$, with a basis built from path integrals with matter
insertions on the Euclidean boundary.

**The headline result, worth stating in full because it's one of the very few places in the entire
subject where "the operator algebra of quantum gravity" is known in exact, closed form**: the full algebra of
gauge-invariant JT-gravity observables (built including the boundary Hamiltonian $H_R$ itself, at genuinely
finite $G_N$ — with no crossed product, no auxiliary observer, and no perturbative expansion needed as an
approximation) is found to be **type II**. Unlike every earlier example in this section, this isn't a
statement about a semiclassical, large-$N$ construction dressed onto an auxiliary clock; it's an exact
statement about the full quantum-gravitational theory itself, at finite coupling. It stands as concrete proof
of principle that "the algebra of quantum gravity," at finite $G_N$, is a well-posed and answerable
question — not merely a semiclassical approximation scheme — at least in this simplest of solvable models.

\bigskip
\noindent This closes the sequence of concrete applications — black hole, de~Sitter, Schwarzschild—de~Sitter,
dynamical observers, and exact JT gravity — all built from the same single mechanism: gravitational dressing
to a physical observer is the crossed product by the modular group, and it is this, and nothing more exotic,
that converts an intractable type $\mathrm{III}_1$ algebra with no entropy into a genuine type II algebra whose
entropy is exactly the gravitational entropy physicists already knew to expect. Section~X closes the paper
with a summary and some more speculative remarks on what all of this might mean for the mathematical
structure of quantum gravity at finite $G_N$.



---

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
