# Entanglement, Operator Algebras, and the Emergence of Spacetime: A First Introduction for Physicists

**arXiv:2510.07017**

---



---

# Introduction and motivations

## What problem are these notes about?

Before any equations, it helps to say in plain words what question this subject answers. Once the algebra
starts, it is easy to lose sight of the goal.

Here is the question. Ordinary physics, classical and quantum, treats spacetime as a fixed stage. Space and
time are given in advance, with a definite geometry (flat, or curved according to some metric), and physics
happens *emph* that stage. General relativity complicates this a little, because the geometry itself is
dynamical: matter tells spacetime how to curve, and spacetime tells matter how to move. Even so, at any moment
you can ask "what is the metric right here?" and get a sharp answer.

Quantum gravity is the attempt to quantize this whole picture. Once you do that, the metric itself becomes an
operator with quantum fluctuations. The question "what is the geometry right here?" then stops having a
sharp answer, in the same way that "where exactly is the electron?" stops having a sharp answer once a
particle's position is quantized. Geometric statements such as ``this point lies to the future of that
point,'' "this region is causally connected to that region," or ``this is a local, self-contained patch of
space'' are sharply defined only in the classical limit. Physicists write this limit as $G_N\to0$, where
$G_N$ is Newton's gravitational constant. Turning $G_N$ off turns off quantum-gravitational effects and leaves
an ordinary, fixed classical geometry.

So the research question is this. Suppose you are handed a complete quantum theory of gravity at some finite,
nonzero $G_N$. No classical geometry is assumed, no metric is given in advance, and nothing geometric is built
in from the start. As you dial $G_N\to0$, familiar geometric structures are supposed to emerge: a
well-defined notion of "here," a causal order, a notion of a local region. **What, physically and
mathematically, is doing the emerging?** What feature of the underlying quantum theory produces spacetime
geometry as $G_N\to0$? And what role, if any, does quantum entanglement play?

The clearest setting in which this question can be asked precisely is the AdS/CFT correspondence. There, a
theory of quantum gravity in a $(d{+}1)$-dimensional *emph* spacetime is conjectured to be
completely equivalent to an ordinary, non-gravitational quantum field theory living on the $d$-dimensional
boundary of that spacetime. Anti-de Sitter space (AdS) is a spacetime of constant negative curvature. It is
chosen because it has a well-defined boundary at infinity. The boundary theory is a *emph* (CFT).

On the CFT side there is a parameter $N$ that counts the number of independent field degrees of freedom. In
the gauge theories where the correspondence was first understood, $N$ is the number of colors of an $SU(N)$
gauge group. The AdS/CFT dictionary relates $G_N$ on the gravity side to a positive power of $1/N$ on the CFT
side. So $G_N\to0$ (classical, geometric gravity) is the same limit as $N\to\infty$ on the boundary. The
question above then becomes concrete: *emph*

The Ryu—Takayanagi proposal~[RT] gave the first strong hint of the answer. It is a formula that relates
the entanglement entropy of a boundary region to the area of a certain minimal surface in the bulk. It is
literally an equation between a measure of entanglement and a geometric quantity. If entanglement entropy and
bulk area are this closely tied, then entanglement is likely doing real structural work in building the bulk
geometry, rather than merely decorating it. That is the motivating intuition.

These notes develop the tools that make this intuition precise. The approach follows a research program
developed by Leutheusser, Liu, and collaborators~[Liu2025]. The key tool is a piece of mathematics from
the 1930s: von Neumann algebras. They were originally developed for a different purpose, namely putting
ordinary quantum mechanics on a rigorous footing. Only recently have they been recognized as the right
language for this question.

\begin{table}[t]
\centering
\footnotesize
\begin{tabularx}{\textwidth}{@{}l >{\raggedright\arraybackslash}p{4.8cm} >{\raggedright\arraybackslash}X@{}}
\toprule
**Symbol / Structure** & **Mathematical Definition** & **Physical Interpretation / Role** \\
\midrule
$\HH$ & Global Hilbert space of states & Total state space of the system \\
$B(\HH)$ & Bounded linear operators on $\HH$ & All bounded operations and observables \\
$\M \subset B(\HH)$ & von Neumann algebra ($\M = \M''$) & Observables accessible to a local subregion or observer \\
$\M'$ & Commutant: $\{B : [B,A]=0\ \forall A \in \M\}$ & Observables of the causal complement, or of the complementary subsystem \\
$\mathcal{Z}(\M) = \M \cap \M'$ & Center of the algebra & Classical superselection labels (trivial, $\mathbb{C}\id$, for a factor) \\
$\omega: \M \to \mathbb{C}$ & State (positive linear functional, $\omega(\id)=1$) & Expectation values, $\omega(A) = \langle A \rangle$ \\
$(\pi_\omega, \HH_\omega, \ket{\Omega_\omega})$ & GNS representation & Hilbert space built directly from the state $\omega$ \\
$\ket\Psi \in \HH$ & Cyclic ($\M\ket\Psi$ dense) and separating (no nonzero $A\in\M$ has $A\ket\Psi=0$) vector & Typical entangled state, such as the vacuum of a quantum field theory \\
$S_\Psi$ & Tomita antilinear operator: $S_\Psi A\ket\Psi = A^\dagger\ket\Psi$ & State-dependent modular involution \\
$J_\Psi$ & Modular conjugation ($J_\Psi \M J_\Psi = \M'$) & Antilinear reflection mapping the algebra to its commutant (for a Rindler wedge, a CPT-type reflection) \\
$\Delta_\Psi = S_\Psi^\dagger S_\Psi$ & Modular operator (positive, self-adjoint) & Encodes the entanglement of $\ket\Psi$ (equals $\rho_R\otimes\rho_L^{-1}$ in type I) \\
$h_\Psi \equiv -\log\Delta_\Psi$ & Modular Hamiltonian & Generator of the intrinsic time flow of the subsystem (for a Rindler wedge, $2\pi$ times the boost generator) \\
$\sigma_t^\Psi(A) = \Delta_\Psi^{it} A \Delta_\Psi^{-it}$ & Modular flow (one-parameter group of automorphisms) & Intrinsic time evolution; the state is thermal (KMS) with respect to it \\
$\widehat\M = \M \rtimes_\sigma \mathbb{R}$ & Crossed product algebra, with clock space $L^2(\mathbb{R})$ & Gravitationally dressed algebra that includes an observer's energy or clock \\
$\tau$ & Semifinite trace on $\widehat\M$ ($\tau(AB)=\tau(BA)$) & Renormalized trace that gives well-defined density matrices \\
$S_{\rm gen}$ & Generalized entropy: $\frac{\langle \hat A\rangle}{4G_N} + S_{\rm bulk}$ & Finite gravitational entropy in semiclassical gravity \\
$\mathcal{A}_{\rm CFT}$ & Boundary single-trace algebra ($N\to\infty$) & Generalized free fields on the holographic boundary \\
$\mathcal{A}_{\rm bulk}(b_A)$ & Bulk algebra in the entanglement wedge $b_A$ & Local semiclassical bulk quantum fields dual to a boundary region \\
\bottomrule
\end{tabularx}
\caption{Summary of the core notation, algebraic structures, and physical interpretations used throughout these notes.}
\label{tab:notation_summary}
\end{table}

\begin{figure}[htbp]
\centering
\includegraphics[width=0.92\textwidth]{figs/fig_roadmap.pdf}
\caption{From tensor factors to subalgebras. On the left, a subsystem is a tensor factor of $\HH = \HH_R \otimes \HH_L$, as in standard quantum mechanics. On the right, a subsystem is an algebra of operators $\M$ inside $B(\HH)$, together with its commutant $\M'$, the operators that commute with all of $\M$. The upper arrow is the generalization; the lower arrow says that type I algebras are the special case in which the tensor-product picture on the left is recovered.}
\label{fig:roadmap}
\end{figure}

## From wavefunctions to density matrices to algebraic states

To see why the algebraic framework is natural, follow how the idea of a "quantum state" changes as we move
from undergraduate quantum mechanics to open systems, quantum field theory, and quantum gravity.


1. **Level 0: the pure wavefunction $\psi(x) = \braket{x|\Psi**$.}
In textbook quantum mechanics, the basic object is a state vector $\ket\Psi \in \HH$. It evolves according to
the Schr\"odinger equation. Probabilities come from the Born rule, $P(x) = |\psi(x)|^2$. This description
assumes a *emph*, in which an experimenter can in principle measure any operator on
the whole system.
2. **Level 1: the density matrix $\rho(x, x')$ and the Wigner function.**
When a system interacts with an unobserved environment or a thermal bath, pure states are replaced by
density operators, $\rho = \sum_k p_k \ket{\psi_k}\bra{\psi_k}$. In the position basis the density operator
becomes a function of two positions, $\rho(x, x') = \braket{x|\rho|x'}$. It is useful to change to the
following variables (called Keldysh variables in the study of open systems):

$$

x_c \equiv \frac{x + x'}{2} \quad \text{(midpoint)}, \qquad
x_q \equiv x - x' \quad \text{(separation)}.

$$

The diagonal $x_q = 0$ gives the classical probability distribution, $P(x_c) = \rho(x_c, x_c)$. Nonzero
$x_q$ records the off-diagonal elements, which carry quantum interference. Fourier transforming in $x_q$
gives the **Wigner quasi-probability distribution** on phase space (we set $\hbar=1$):

$$

W(x_c, p) = \frac{1}{2\pi}\int_{-\infty}^\infty \dd x_q\, e^{-i p x_q}\,
\rho\!\left(x_c + \tfrac{x_q}{2},\, x_c - \tfrac{x_q}{2}\right) .

$$

Here $p$ is the momentum conjugate to $x_q$, and the factor $1/(2\pi)$ makes $\int\dd x_c\,\dd p\,W=1$. The
Wigner function is a bridge between classical statistical physics and quantum mechanics. But the density
matrix of a subsystem is obtained by tracing out an environment, so this whole level still presumes that the
global Hilbert space factorizes as $\HH = \HH_{\rm system} \otimes \HH_{\rm environment}$.
3. **Level 2: observers have limited access.**
In realistic situations, no observer can measure everything. An observer has a limited apparatus, or is
confined to a spatial subregion $R$, and can only measure a restricted set of observables $\M$. Describing
such an observer's situation with global pure states gives useless answers. For example, the relative entropy
$D(\rho\|\sigma) = \Tr(\rho\log\rho - \rho\log\sigma)$ between two *emph* global pure states is
always $+\infty$. The reason is that $\log\sigma$ equals $-\infty$ on every direction orthogonal to the state
vector of $\sigma$, and $\rho$ has weight in such a direction. So the global relative entropy cannot tell two
nearly identical pure states apart from two very different ones. What the observer actually needs is a
relative entropy of the two states *emph* $\M$, which is typically finite and informative. In
quantum field theory there is a further problem: as this chapter shows, a region does not even have a reduced
density matrix to put into this formula.
4. **Level 3: the algebraic state $\omega: \M \to \mathbb{C**$.}
In algebraic quantum mechanics (developed by von Neumann, Haag, and many others), we drop the assumption that
a fixed global Hilbert space is fundamental. The primary physical object is the **algebra of accessible
observables**, $\M$. A **state** $\omega$ is simply a positive linear functional that assigns
expectation values to operators:

$$

\omega(A) = \langle A \rangle_\omega, \qquad \omega(\id) = 1, \quad \omega(A^\dagger A) \ge 0 \quad \forall A \in \M.

$$

The Hilbert space $\HH_\omega$ and the state vector $\ket{\Omega_\omega}$ are not postulated in advance.
They are **constructed** from the state $\omega$ by the Gelfand—Naimark—Segal (GNS) construction of
Chapter~2, in such a way that

$$

\omega(A) = \braket{\Omega_\omega | \pi_\omega(A) | \Omega_\omega} .

$$



\begin{keyresult}
**The conceptual takeaway:** The wavefunction $\psi(x)$ is not the fundamental container of physical
reality. It is one particular GNS representation of an algebraic state $\omega$ on a type I algebra. In the
thermodynamic limit (infinitely many degrees of freedom), for local subregions in quantum field theory, and
for semiclassical black holes, the tensor factorization of the Hilbert space breaks down. The algebraic state
$\omega$, however, remains well defined.
\end{keyresult}

## Why the ordinary quantum-mechanical definition of "subsystem" isn't good enough

To see why a new mathematical tool is needed, we first have to see exactly where the old one breaks. The old
tool is the one from every quantum mechanics course. Take a system built from two pieces, $R$ and $L$. Read
them as "right" and "left," or as "region" and "its complement"; any split into two parts will do. The
Hilbert space of the whole system is then a tensor product,

$$

\HH = \HH_R\otimes\HH_L .

$$

Concretely, suppose $\HH_R$ has orthonormal basis $\{\ket i_R\}$ and $\HH_L$ has orthonormal basis
$\{\ket a_L\}$. Then $\HH_R\otimes\HH_L$ is spanned by all the pairs $\ket i_R\ket a_L$. A general state of
the joint system is a sum $\ket\Psi = \sum_{ia} c_{ia}\ket i_R\ket a_L$ for some array of complex numbers
$c_{ia}$. (The same idea works with continuous or more general index sets.) The state is called
**entangled** exactly when the array $c_{ia}$ cannot be written as a product $c_{ia}=\psi_i\chi_a$ of
two smaller arrays $\psi_i$ and $\chi_a$. In words: an entangled state does not split into ``something about
$R$'' times "something about $L$."

Everything you already know about entanglement is built directly on the tensor factorization
$\HH=\HH_R\otimes\HH_L$. This includes the reduced density matrix $\rho_R\equiv\Tr_L\ket\Psi\!\bra\Psi$
(obtained by tracing out, that is, summing over, the $L$ degrees of freedom), the entanglement entropy
$S_R=-\Tr_R(\rho_R\log\rho_R)$, the R\'enyi entropies, and the relative entropy. If the factorization does not
exist, none of these formulas can even be written down. There is no $\HH_L$ to trace over, and no
well-defined "$R$-part" of the state to extract. The familiar machinery of entanglement entropy fails at
the first step. It does not give a wrong answer; it gives no answer at all.

The central claim, on which the rest of these notes build, is that this factorization really does fail to
exist. This is not an exotic mathematical pathology. It happens in exactly the situations that matter most:
gauge theories; many-body systems in a thermodynamic limit (infinite volume or infinite $N$); quantum field
theories cut into two regions by a surface; and, the case these notes care about most, the large-$N$ limit of
a holographic boundary theory. Three concrete examples show how and why it fails. The first one, infinitely
many entangled qubit pairs, is worked through slowly and completely here, because later chapters keep
returning to it.

## The central example: infinitely many entangled qubit pairs

Take a single pair of qubits, one belonging to $R$ and one to $L$, prepared in the state

$$

\ket{\phi_\theta} = \cos\theta\,\ket0_R\ket0_L + \sin\theta\,\ket1_R\ket1_L , \qquad \theta\in(0,\pi/4] .

$$

This is completely standard. It is a partially entangled pair. It is maximally entangled exactly at
$\theta=\pi/4$, where both coefficients equal $\tfrac1{\sqrt2}$; this is a Bell pair. Such a state can be
prepared in a laboratory with two photons or two trapped ions. Nothing about a single pair is mysterious.

To find the reduced density matrix explicitly, first write out the full $4\times4$ density operator of the
pure pair:
\begin{multline*}
\ket{\phi_\theta}\bra{\phi_\theta} = \cos^2\theta\ket{00}\bra{00} + \cos\theta\sin\theta\ket{00}\bra{11} \\
+ \sin\theta\cos\theta\ket{11}\bra{00} + \sin^2\theta\ket{11}\bra{11} .
\end{multline*}
Now take the partial trace over subsystem $L$, summing over the orthonormal basis $\{\ket0_L, \ket1_L\}$:
\begin{align}
\rho_R \equiv \Tr_L\ket{\phi_\theta}\bra{\phi_\theta}
&\eqstep{1} {}_L\braket{0|\phi_\theta}\bra{\phi_\theta}0\rangle_L + {}_L\braket{1|\phi_\theta}\bra{\phi_\theta}1\rangle_L \notag\\
&\eqstep{2} \cos^2\theta\,\ket0_R\bra0_R + \sin^2\theta\,\ket1_R\bra1_R
\ \eqstep{3}\ \begin{pmatrix} \cos^2\theta & 0 \\ 0 & \sin^2\theta \end{pmatrix} . \notag
\end{align}
**(1)** This is the definition of the partial trace: sandwich between the basis vectors of $L$ and sum.\quad
**(2)** ${}_L\braket{0|\phi_\theta}=\cos\theta\ket0_R$ and ${}_L\braket{1|\phi_\theta}=\sin\theta\ket1_R$.
The cross terms $\ket{00}\bra{11}$ and $\ket{11}\bra{00}$ drop out because $\braket{0|1}_L=0$.\quad
**(3)** Write the result as a matrix in the basis $\ket0_R,\ket1_R$.

Because $\rho_R$ is already diagonal, its operator logarithm is found by taking the logarithm of each diagonal
entry:

$$

\log\rho_R = \begin{pmatrix} \log(\cos^2\theta) & 0 \\ 0 & \log(\sin^2\theta) \end{pmatrix} .

$$

The von Neumann entanglement entropy of a single pair then follows by taking the trace:

$$

s_1(\theta) = -\Tr_R(\rho_R\log\rho_R)
= -\left[ \cos^2\theta\log(\cos^2\theta) + \sin^2\theta\log(\sin^2\theta) \right] .

$$

Two special cases are useful.

- For the maximally entangled Bell pair at $\theta=\pi/4$, we have $\cos^2(\pi/4)=\sin^2(\pi/4)=1/2$,
so

$$

s_1(\pi/4) = -\left[ \tfrac12\log(\tfrac12) + \tfrac12\log(\tfrac12) \right]
= \log 2 \approx 0.693147\text{ nats} \quad (= 1\text{ bit}).

$$

- In the weakly entangled limit $\theta \to 0$:
\begin{align}
s_1(\theta) &\eqstep{1} -(1-\theta^2)\log(1-\theta^2) - \theta^2\log(\theta^2) + O(\theta^4\log\theta) \notag\\
&\eqstep{2} \theta^2 - 2\theta^2\log\theta + O(\theta^4\log\theta)
\ =\ \theta^2(1 - 2\log\theta) + O(\theta^4\log\theta) \ \to\ 0 . \notag
\end{align}
**(1)** Substitute $\cos^2\theta=1-\theta^2+O(\theta^4)$ and $\sin^2\theta=\theta^2+O(\theta^4)$.
The neglected $O(\theta^4)$ corrections change the result only at order $\theta^4\log\theta$.\quad
**(2)** Expand $\log(1-\theta^2)=-\theta^2+O(\theta^4)$ in the first term, and use
$\log\theta^2=2\log\theta$ in the second. The limit is zero because $\theta^2\log\theta\to0$.


Now take $N$ independent copies of this pair. That is, take $N$ separate two-qubit systems, each prepared in
the same way, and combine them into one big state:

$$

\ket{\Phi_\theta} = \ket{\phi_\theta}_1\otimes\ket{\phi_\theta}_2\otimes\cdots\otimes\ket{\phi_\theta}_N .

$$

Group all the $R$-qubits together into "the $R$ system" and all the $L$-qubits into "the $L$ system." At
any finite $N$, this is still completely ordinary. The space $\HH_R=(\mathbb C^2)^{\otimes N}$ is a
$2^N$-dimensional Hilbert space. The full space $\HH=\HH_R\otimes\HH_L$ factorizes, because it was built as a
tensor product. The reduced density operator of $R$ is the $N$-fold tensor product,
$\rho_R^{(N)} = \rho_R^{\otimes N}$. The von Neumann entropy is additive over tensor products,
$S(\rho_1 \otimes \rho_2) = S(\rho_1) + S(\rho_2)$. So the total entropy of the $N$ pairs is exactly

$$

S_R^{(N)} = N\, s_1(\theta) .

$$

At $\theta=\pi/4$, $s_1(\pi/4)=\log2\approx0.693$. So for $N=1$, $S_R=0.693$; for $N=10$, $S_R=6.93$; for
$N=1000$, $S_R=693$. Nothing is subtle about any one of these numbers, and each can be checked by direct
computation. New physics appears only when we ask what happens as $N\to\infty$, while staying
inside the set of states that a real experiment with finite energy could reach.

### Restricting to finite energy

To talk about energy we need a Hamiltonian. Choose one for which $\ket{\Phi_\theta}$ is the ground state:

$$

H = f\sum_{i=1}^N \big(\id - P_i\big), \qquad P_i \equiv \ket{\phi_\theta}\bra{\phi_\theta}_i ,

$$

where $P_i$ is the projector onto the state $\ket{\phi_\theta}$ of the $i$-th pair and $f>0$ is a fixed energy
scale. Each term $f(\id-P_i)$ has eigenvalues $0$ and $f$. So $H\ge0$, and $\ket{\Phi_\theta}$, which has
$P_i=1$ for every pair, is the ground state, with energy $0$. This Hamiltonian couples each $R$-qubit to its
$L$-partner. Some coupling of this kind is unavoidable: a Hamiltonian of the form $H_R+H_L$, with no
interaction between $R$ and $L$, always has an unentangled ground state.

Flipping a single spin costs a fixed amount of energy. Apply the spin-flip operator
$X = \ket0\bra1 + \ket1\bra0$ to the $R$-qubit of pair $i$. It sends
$\ket{\phi_\theta}$ to $\cos\theta\ket1_R\ket0_L + \sin\theta\ket0_R\ket1_L$, which is orthogonal to
$\ket{\phi_\theta}$. So the flipped pair has $P_i=0$, and the energy rises by exactly $f$. Flipping spins in
$k$ different pairs costs $kf$.

A **finite-energy state** built on the reference state $\ket{\Phi_\theta}$ is one obtained by acting on
only a finite number $k$ of the pairs, for example by flipping finitely many spins. Such a state differs from
$\ket{\Phi_\theta}$ only on those $k$ pairs, and its energy is at most $kf$. Changing infinitely many pairs
costs infinite energy, and no physical experiment supplies infinite energy.

Now comes the key computation. Suppose you want to disentangle $R$ from $L$ completely, that is, to reach
some product state $\ket\psi_R\otimes\ket\chi_L$ with zero entanglement entropy. Here $\ket\psi_R$ may be any
state of all $N$ of the $R$-qubits, not necessarily a product over pairs, and similarly for $\ket\chi_L$.
The energy of any such state is bounded below:
\begin{align}
\braket{\psi_R\chi_L|H|\psi_R\chi_L}
&\eqstep{1} f\sum_{i=1}^N\Big(1-\braket{\phi_\theta|\rho_i|\phi_\theta}\Big) \notag\\
&\geqstep{2} f\sum_{i=1}^N\big(1-\cos^2\theta\big) \ =\ N f\sin^2\theta .
\label{eq:qubit_product_energy}
\end{align}
**(1)** Here $\rho_i$ is the reduced density matrix of pair $i$ in the state
$\ket\psi_R\ket\chi_L$. The expectation value of $P_i$ depends only on $\rho_i$.\quad
**(2)** Because the global state is a product across $R|L$, $\rho_i=\rho_{R_i}\otimes\rho_{L_i}$, which is
a mixture of two-qubit product states $\ket a\ket b$. For each of these,
$|\braket{\phi_\theta|a\,b}| = |\cos\theta\, a_0b_0+\sin\theta\, a_1b_1| \le \cos\theta\,(|a_0||b_0|+|a_1||b_1|)
\le\cos\theta$. The first inequality uses $\sin\theta\le\cos\theta$ for $\theta\le\pi/4$; the second is the
Cauchy—Schwarz inequality for unit vectors. So $\braket{\phi_\theta|\rho_i|\phi_\theta}\le\cos^2\theta$.

So every unentangled state costs at least $N f\sin^2\theta$. There is no shortcut. You cannot remove the
entanglement of pair number $573{,}241$ without doing something to pair number $573{,}241$ specifically, and
each pair you touch costs a fixed, nonzero amount of energy. As $N\to\infty$, this cost diverges:
*emph* "Unentangling" has a concrete operational meaning here. It means applying some joint
operation to $R$ and $L$ that turns the state into a product of an $R$-state and an $L$-state. That is an
ordinary (if very large) quantum operation. It simply cannot be done with finite energy in this limit.

Three distinct consequences follow.


1. **Every finite-energy state has infinite entanglement.** Take any state obtained from
$\ket{\Phi_\theta}$ by acting on $k$ pairs. The other $N-k$ pairs are untouched. They remain in the state
$\ket{\phi_\theta}$, unentangled with the first $k$ pairs. By additivity, the entanglement entropy of such a
state is at least $(N-k)\,s_1(\theta)$, which tends to infinity as $N\to\infty$. So there is no unentangled,
or even weakly entangled, state anywhere in the finite-energy sector. Every physically reachable state is
infinitely entangled across the split between $R$ and $L$.
2. **The Hilbert space itself does not factorize.** Suppose a tensor factorization
$\HH=\HH_R\otimes\HH_L$ existed, with the $R$-operators acting on the first factor and the $L$-operators on
the second. Then product states $\ket\psi_R\otimes\ket\chi_L$ would exist. They are the simplest vectors you
can write down once you have the factorization. But by \eqref{eq:qubit_product_energy}, no product state is
a finite-energy state. Consider the finite-energy Hilbert space $\HH_{\Phi_\theta}$. It is built by taking all
finite-energy excitations of $\ket{\Phi_\theta}$ and completing their span. It contains no vectors of the form
$\ket\psi_R\otimes\ket\chi_L$. So $\HH_{\Phi_\theta}$ cannot be written as $\HH_R\otimes\HH_L$ in a way that
matches how the $R$- and $L$-operators act. This is not a failure to find the right factorization; no such
factorization exists. (As an abstract vector space, any infinite-dimensional separable Hilbert space can be
written as some tensor product. The point is that no such splitting is compatible with the operators that the
$R$- and $L$-observers can actually apply.)

There is also a stronger statement, which we quote without proof. Consider the full space obtained from the
$N$-pair system as $N\to\infty$, before restricting to finite energy. It is not even a *emph*
Hilbert space (one with a countable basis). It is a much larger and less tame object, and most of the usual
tools of quantum mechanics, which assume separability, do not apply to it directly. Restricting to
finite-energy excitations is exactly what picks out a well-behaved separable space $\HH_{\Phi_\theta}$ from
it.
3. **Different values of $\theta$ live in different worlds.** Compare $\ket{\Phi_{\theta}}$ and
$\ket{\Phi_{\theta'}}$ for $\theta\ne\theta'$. They differ on every one of the $N$ pairs, so no operation
acting on finitely many pairs turns one into the other. Their overlap is
$\braket{\Phi_\theta|\Phi_{\theta'}} = \cos^N(\theta-\theta')$, which goes to zero as $N\to\infty$. Their
entanglement entropies differ by $N\,|s_1(\theta)-s_1(\theta')|$, which diverges. In the strict limit, the
finite-energy spaces $\HH_{\Phi_\theta}$ and $\HH_{\Phi_{\theta'}}$ are best thought of as two separate
Hilbert spaces, rather than as two states in one Hilbert space. (In the language of Chapter~2, they carry
inequivalent representations of the same algebra of operators.)


To see the size of these numbers directly, here is the $\theta=\pi/4$ case at a few values of $N$. Each entry
follows exactly from additivity of entropy over the $N$ identical pairs, and is shown rounded:


\begin{tabular}{ccccc}
\toprule
$N$ & $1$ & $10$ & $100$ & $10{,}000$ \\
\midrule
$\dim\HH_R^{(N)}=2^N$ & $2$ & $1024$ & $\approx1.3\times10^{30}$ & astronomically large \\
$S_R^{(N)}=N\log2$ & $0.693$ & $6.93$ & $69.3$ & $6931$ \\
\bottomrule
\end{tabular}

Every entropy entry is just $N\log2$. Seeing the entropy grow without bound while the dimension of
$\HH_R^{(N)}$ explodes gives a concrete picture of the abstract statement that no factorized Hilbert space
survives the limit.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.75\textwidth]{figs/fig_qubit_entropy.pdf}
\caption{The single-pair entanglement entropy $s_1(\theta) = -\cos^2\theta\log(\cos^2\theta) - \sin^2\theta\log(\sin^2\theta)$ for $\theta \in (0, \pi/4]$. The red dot is the maximally entangled Bell state at $\theta = \pi/4$, where $s_1 = \log 2 \approx 0.693$ (dashed line). The open circle marks the product-state limit $\theta \to 0$, where the entropy goes smoothly to zero. For $N$ pairs the total entropy is $S_R^{(N)} = N s_1(\theta)$, which tends to infinity as $N \to \infty$.}
\label{fig:qubit_entropy}
\end{figure}

## Two more examples, more briefly

Two more examples come back later, so here they are in outline. The second matters most, because it applies
to quantum field theory and, ultimately, to AdS/CFT.

**Lattice gauge theory.** A gauge theory (such as electromagnetism, or the theory of the strong force)
has more mathematical variables than physical degrees of freedom. You write down a variable $U_{ij}$ on each
link of a lattice. But many different configurations of the $U_{ij}$ describe exactly the same physics. They
are related by *emph*, $U_{ij}\to V_iU_{ij}V_j^\dagger$. Physical states are required to
be invariant under these transformations. This requirement also breaks the naive tensor factorization
$\HH=\HH_R\otimes\HH_L$, by a mechanism quite different from infinite entanglement. The gauge-invariant states
do not, in general, lie in a product of an $R$-Hilbert space and an $L$-Hilbert space, because gauge
invariance ties the two sides together. This example comes back in Chapter~3 as a comparatively mild
complication. It adds a classical label (which gauge or superselection sector you are in) on top of an
otherwise ordinary tensor-product structure. It is not the deep, qualitative breakdown seen in the spin-pair
chain and in field theory.

**A quantum field theory cut in half.** Take a relativistic quantum field theory, say a scalar field, and
split space into two halves, $R=\{x>0\}$ and $L=\{x<0\}$. A quantum field has infinitely many degrees of
freedom in any interval of space, however small; informally, it has a value (or a mode) at every point. Near
the cutting surface $x=0$, infinitely many field degrees of freedom on the $R$ side sit arbitrarily close to
infinitely many on the $L$ side. Each is coupled to its neighbors. This produces infinite entanglement across
the cut in *emph* finite-energy state, including the vacuum, the lowest-energy state of all.

This is the field-theory version of the mechanism in the spin-pair chain: infinitely many separate
contributions to the entanglement, each small, adding up to an infinite total. It shows up as a divergence.
Compute the entanglement entropy of the region $R$ with a short-distance cutoff $\epsilon$. (Imagine putting
the theory on a lattice with spacing $\epsilon$. This makes everything finite, and we then ask what happens
as $\epsilon\to0$.) For $d\ge3$ spacetime dimensions the result is

$$

S_R(\epsilon) = b\,\frac{\mathrm{Area}(\partial R)}{\epsilon^{d-2}} + \cdots, \qquad \epsilon\to0.

$$

Here $\partial R$ is the surface separating $R$ from $L$, and $b$ is a positive constant that depends on the
theory and on how the cutoff is imposed. (In $d=2$ the divergence is logarithmic instead.) The entropy
diverges as the cutoff is removed. It diverges in a specific way: in proportion to the *emph* of the
cutting surface, not the volume of the region. This "area-law divergence" is one of the most robust facts
in quantum field theory. It appears in essentially every explicit calculation, for free and interacting
fields alike. It is the field-theory counterpart of the non-factorization seen in the spin-pair example. The
next section gives an explicit energy argument for it, and Chapter~4 states it precisely in the language of
von Neumann algebra types.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.75\textwidth]{figs/fig_area_law.pdf}
\caption{Why entanglement across a cut scales with its area. (a) A slice of space is replaced by a lattice of spacing $\epsilon$, and the region $R$ (shaded) is separated from $L$ by the surface $\partial R$. The red links are the nearest-neighbour couplings that cross $\partial R$; each one entangles a short-distance mode of $R$ with one of $L$. (b) Halving the spacing to $\epsilon/2$ doubles the number of red links, so the entropy grows as $\mathrm{Area}(\partial R)/\epsilon^{d-2}$ and diverges as $\epsilon \to 0$.}
\label{fig:area_law}
\end{figure}

## Explicit derivation: why the continuum QFT Hilbert space cannot factorize
\label{sec:qft_nonfactorization_derivation}

The claim that $\HH \ne \HH_R \otimes \HH_L$ in continuum quantum field theory underlies everything that
follows. This section shows where it comes from, using nothing more advanced than coupled harmonic
oscillators. The argument below is a physical estimate, not a proof. It shows that an unentangled state
across the cut would cost an energy that diverges as the cutoff is removed. The rigorous version of the
statement is quoted at the end of the section.

### 1. The Hamiltonian and the gradient coupling across the cut

Consider a free, real scalar field $\phi(t, \vec x)$ of mass $m$ in $d$ spacetime dimensions, that is, in
$d-1$ spatial dimensions. On a slice of constant time, the Hamiltonian is
\begin{equation}
H = \int \dd^{d-1}x \left[ \frac{1}{2}\pi(\vec x)^2 + \frac{1}{2}\big(\vec\nabla\phi(\vec x)\big)^2
+ \frac{1}{2}m^2\phi(\vec x)^2 \right].
\label{eq:scalar_hamiltonian_continuum}
\end{equation}
Here $\pi(\vec x)$ is the canonical momentum field, with $[\phi(\vec x), \pi(\vec y)] = i\delta^{(d-1)}(\vec x - \vec y)$.

Divide space into two halves along the plane $x = 0$:

$$

R = \{ (x, \vec x_\perp) : x > 0 \}, \qquad L = \{ (x, \vec x_\perp) : x < 0 \}.

$$

Here $\vec x_\perp = (x^2, \dots, x^{d-1})$ are the $d-2$ spatial coordinates along the dividing surface
$\partial R$. This surface is called the *emph*.

To focus on the physics near the cut, we treat the two kinds of directions differently. We put the
perpendicular direction $x$ on a lattice with spacing $\epsilon$. We Fourier transform the transverse
coordinates $\vec x_\perp$ into transverse momenta $\vec k_\perp$:

$$

\phi(x, \vec x_\perp) = \int \frac{\dd^{d-2}k_\perp}{(2\pi)^{d-2}} \, \widetilde\phi(x, \vec k_\perp) \, e^{i \vec k_\perp \cdot \vec x_\perp} .

$$

The Hamiltonian is quadratic, so different transverse momenta do not mix. For each $\vec k_\perp$, the
Hamiltonian becomes an independent one-dimensional chain of coupled harmonic oscillators. The transverse
gradient $|\vec k_\perp|^2$ adds to the mass term, giving the effective mass
\begin{equation}
M^2 \equiv m^2 + |\vec k_\perp|^2 .
\label{eq:effective_mass_transverse}
\end{equation}
(Strictly, the Fourier modes are complex, with $\widetilde\phi(x,-\vec k_\perp)=\widetilde\phi(x,\vec k_\perp)^*$.
We treat each mode as a real oscillator. This simplification does not affect the energy estimates below.)
On the lattice, the field becomes a set of site variables $\phi_j \equiv \widetilde\phi(j\epsilon, \vec
k_\perp)$ with conjugate momenta $\pi_j$. Sites $j = \dots, -2, -1$ lie in $L$, and sites $j = 0, 1, 2, \dots$
lie in $R$.

The gradient in the direction perpendicular to the cut is replaced by a finite difference:
\begin{equation}
\int \dd x \, \frac{1}{2}\left(\frac{\partial\phi}{\partial x}\right)^2 \;\longrightarrow\;
\sum_j \frac{\epsilon}{2} \left( \frac{\phi_{j+1} - \phi_j}{\epsilon} \right)^2
= \sum_j \frac{1}{2\epsilon} (\phi_{j+1} - \phi_j)^2 .
\label{eq:lattice_gradient_sum}
\end{equation}
The lattice momenta obey $[\phi_j,\pi_k]=i\delta_{jk}/\epsilon$, because the delta function becomes
$\delta_{jk}/\epsilon$ on the lattice. It is convenient to rescale to canonical variables,
$\phi_j\to\sqrt\epsilon\,\phi_j$ and $\pi_j\to\sqrt\epsilon\,\pi_j$, which obey $[\phi_j,\pi_k]=i\delta_{jk}$.
In these variables the chain Hamiltonian for one transverse mode is
\begin{equation}
H_{\vec k_\perp} = \sum_j \left[ \frac12\pi_j^2 + \frac12 M^2\phi_j^2 + \frac{1}{2\epsilon^2}(\phi_{j+1}-\phi_j)^2 \right] .
\label{eq:lattice_chain_hamiltonian}
\end{equation}
One link in this sum straddles the cut. It connects site $j = -1$ (the closest site in $L$) to site $j = 0$
(the closest site in $R$):
\begin{equation}
H_{\rm cut} = \frac{1}{2\epsilon^2} (\phi_0 - \phi_{-1})^2 = \frac{1}{2\epsilon^2} (\phi_R - \phi_L)^2 ,
\label{eq:h_cut_interaction}
\end{equation}
where we write $\phi_R \equiv \phi_0$ and $\phi_L \equiv \phi_{-1}$ for short. This single term is the only
coupling between $R$ and $L$ for this mode.

### 2. Two oscillators across the cut

To see the mechanism as simply as possible, keep only the two sites next to the cut, and drop their links to
the rest of the chain. This is a crude truncation, but it keeps the essential feature: two oscillators, one on
each side, coupled by $H_{\rm cut}$. (A numerical check of the full chain is given below.) The Hamiltonian of
the two oscillators is
\begin{equation}
H_{\rm pair} = \frac{1}{2}\pi_R^2 + \frac{1}{2}\pi_L^2 + \frac{1}{2}M^2(\phi_R^2 + \phi_L^2)
+ \frac{1}{2\epsilon^2}(\phi_R - \phi_L)^2 .
\label{eq:pair_hamiltonian}
\end{equation}

This system is quadratic, so it can be solved exactly using normal-mode coordinates:
\begin{equation}
\phi_+ \equiv \frac{\phi_R + \phi_L}{\sqrt{2}}, \qquad \phi_- \equiv \frac{\phi_R - \phi_L}{\sqrt{2}} ,
\label{eq:normal_mode_coords}
\end{equation}
with $\pi_\pm$ defined in the same way. This change of variables is a rotation, so
$\phi_R^2+\phi_L^2=\phi_+^2+\phi_-^2$ and $\pi_R^2+\pi_L^2=\pi_+^2+\pi_-^2$, while the coupling term becomes
$(\phi_R-\phi_L)^2/(2\epsilon^2)=\phi_-^2/\epsilon^2$. The Hamiltonian therefore separates into two
independent harmonic oscillators:
\begin{equation}
H_{\rm pair} = \left( \frac{1}{2}\pi_+^2 + \frac{1}{2}\omega_+^2 \phi_+^2 \right)
+ \left( \frac{1}{2}\pi_-^2 + \frac{1}{2}\omega_-^2 \phi_-^2 \right),
\label{eq:decoupled_pair_hamiltonian}
\end{equation}
with normal-mode frequencies
\begin{align}
\omega_+ &= M = \sqrt{m^2 + |\vec k_\perp|^2}, \label{eq:omega_plus} \\
\omega_- &= \sqrt{M^2 + \frac{2}{\epsilon^2}} = \sqrt{m^2 + |\vec k_\perp|^2 + \frac{2}{\epsilon^2}}
\notag\\
&\approx \frac{\sqrt{2}}{\epsilon} \quad \text{as } \epsilon \to 0 . \label{eq:omega_minus}
\end{align}
The "sum" mode $\phi_+$ feels only the mass. The "difference" mode $\phi_-$ is stretched by the stiff
link across the cut, so its frequency is very high.

### 3. The vacuum: neighbours across the cut move together

The ground state of \eqref{eq:decoupled_pair_hamiltonian} is a product of two Gaussian ground states in the
normal coordinates:
\begin{equation}
\Psi_0(\phi_+, \phi_-) = \left( \frac{\omega_+ \omega_-}{\pi^2} \right)^{1/4}
\exp\left[ -\frac{1}{2}\omega_+\phi_+^2 - \frac{1}{2}\omega_-\phi_-^2 \right] .
\label{eq:ground_state_normal}
\end{equation}
Its energy is the sum of the two zero-point energies,
\begin{equation}
E_{\rm vac} = \tfrac12(\omega_+ + \omega_-) .
\label{eq:pair_vacuum_energy}
\end{equation}
Transforming back to the local fields $\phi_R, \phi_L$ using \eqref{eq:normal_mode_coords} gives
\begin{align}
\Psi_0(\phi_R, \phi_L) = \left( \frac{\omega_+ \omega_-}{\pi^2} \right)^{1/4}
\exp\Big[ &-\frac{1}{4}(\omega_+ + \omega_-)(\phi_R^2 + \phi_L^2) \notag\\
&- \frac{1}{2}(\omega_+ - \omega_-)\phi_R \phi_L \Big] .
\label{eq:ground_state_physical}
\end{align}
The exponent contains the cross term $\frac{1}{2}(\omega_- - \omega_+)\phi_R \phi_L$. Because of this term,
the wavefunction is not a product of a function of $\phi_R$ and a function of $\phi_L$: the vacuum is
entangled across the cut. The entanglement is strong when $\omega_- \approx \sqrt{2}/\epsilon \gg \omega_+$.

A good way to see how strong it is: compute the correlations. Using
$\braket{\phi_\pm^2}=1/(2\omega_\pm)$ and $\phi_{R,L}=(\phi_+\pm\phi_-)/\sqrt2$,

$$

\braket{\phi_R^2}_\Omega = \frac14\left(\frac1{\omega_+}+\frac1{\omega_-}\right), \qquad
\braket{\phi_R\phi_L}_\Omega = \frac14\left(\frac1{\omega_+}-\frac1{\omega_-}\right).

$$

The correlation coefficient $\braket{\phi_R\phi_L}/\braket{\phi_R^2} = (\omega_- -
\omega_+)/(\omega_-+\omega_+)$ tends to $1$ as $\epsilon\to0$. The two neighbouring field values fluctuate
by large amounts, of order $1/\sqrt{M}$, but they fluctuate almost exactly together. In the vacuum
$\ket\Omega$ this has two consequences.

- The difference between the two sides is small:
\begin{align}
\braket{\Omega | (\phi_R - \phi_L)^2 | \Omega}
&\eqstep{1} 2 \braket{\Omega | \phi_-^2 | \Omega}
\ \eqstep{2}\ \frac{2}{2\omega_-} = \frac{1}{\omega_-}
\ \eqstep{3}\ \frac{\epsilon}{\sqrt{2}} + O(\epsilon^3) .
\label{eq:vacuum_diff_exp}
\end{align}
**(1)** $\phi_R-\phi_L=\sqrt2\,\phi_-$, from the normal-mode definition.\quad
**(2)** A harmonic-oscillator ground state of frequency $\omega$ has $\braket{\phi^2}=1/(2\omega)$.\quad
**(3)** Expand $1/\omega_-=(\epsilon/\sqrt2)(1+M^2\epsilon^2/2)^{-1/2}$ for small $\epsilon$.
- The energy stored in the link across the cut is therefore
\begin{equation}
\braket{\Omega | H_{\rm cut} | \Omega} = \frac{1}{2\epsilon^2} \braket{\Omega | (\phi_R - \phi_L)^2 | \Omega}
= \frac{1}{2\epsilon^2} \frac{1}{\omega_-} \approx \frac{1}{2\sqrt{2}\,\epsilon} .
\label{eq:vacuum_cut_energy}
\end{equation}
This is part of the zero-point energy of the vacuum. The vacuum has it anyway, and the energies of other
states are measured relative to the vacuum energy \eqref{eq:pair_vacuum_energy}.


### 4. The energy cost of an unentangled state

Now suppose, for the sake of argument, that the Hilbert space did factorize across the cut:

$$

\HH \stackrel{?}{=} \HH_L \otimes \HH_R .

$$

Then the Hilbert space would contain unentangled product states,
\begin{equation}
\ket{\Psi_{\rm prod}} = \ket{\psi_L} \otimes \ket{\chi_R} \in \HH ,
\label{eq:hypothetical_product_state}
\end{equation}
with $\ket{\psi_L} \in \HH_L$ and $\ket{\chi_R} \in \HH_R$. How much energy would such a state have?

In a product state, the expectation value of a product of an $L$-operator and an $R$-operator factorizes:
\begin{equation}
\braket{\Psi_{\rm prod} | \phi_R \phi_L | \Psi_{\rm prod}} = \braket{\chi_R | \phi_R | \chi_R} \braket{\psi_L | \phi_L | \psi_L} .
\label{eq:product_state_covariance_zero}
\end{equation}
In other words, the fluctuations of $\phi_R$ and $\phi_L$ are completely uncorrelated. For the difference of
the two fields this gives
\begin{align}
\braket{\Psi_{\rm prod} | (\phi_R - \phi_L)^2 | \Psi_{\rm prod}}
&\eqstep{1} \braket{\phi_R^2}_{\chi_R} + \braket{\phi_L^2}_{\psi_L} - 2\braket{\phi_R}_{\chi_R}\braket{\phi_L}_{\psi_L} \notag \\
&\eqstep{2} (\Delta\phi_R)^2 + (\Delta\phi_L)^2 + \big(\braket{\phi_R}-\braket{\phi_L}\big)^2 .
\label{eq:prod_diff_squared}
\end{align}
**(1)** Expand the square and factorize the cross term using \eqref{eq:product_state_covariance_zero}.\quad
**(2)** Write $\braket{\phi^2}=(\Delta\phi)^2+\braket{\phi}^2$, where $(\Delta\phi)^2$ is the variance,
and collect the mean values into a square.

This shows the difficulty. In the vacuum, $\phi_R-\phi_L$ is kept small because the two sides move together.
In a product state they cannot move together, so the only way to keep $\phi_R-\phi_L$ small is to make each
variance $(\Delta\phi_R)^2$ and $(\Delta\phi_L)^2$ small separately. But by the uncertainty principle,
$\Delta\phi\,\Delta\pi\ge\tfrac12$, so squeezing the field fluctuations increases the momentum fluctuations
and hence the kinetic energy. The product state must pay one way or the other.

We can find the exact minimum. Define the frequency

$$

\Omega_\epsilon \equiv \sqrt{M^2 + \frac{1}{\epsilon^2}}

$$

and the single-site Hamiltonians $h_R = \tfrac12\pi_R^2+\tfrac12\Omega_\epsilon^2\phi_R^2$ and $h_L =
\tfrac12\pi_L^2+\tfrac12\Omega_\epsilon^2\phi_L^2$. Write $a=\braket{\phi_R}$ and $b=\braket{\phi_L}$. Then,
for any product state,
\begin{align}
\braket{H_{\rm pair}}_{\rm prod}
&\eqstep{1} \braket{h_R}_{\chi_R} + \braket{h_L}_{\psi_L} - \frac{ab}{\epsilon^2} \notag\\
&\geqstep{2} \Big(\tfrac12\Omega_\epsilon + \tfrac12\Omega_\epsilon^2a^2\Big)
+ \Big(\tfrac12\Omega_\epsilon + \tfrac12\Omega_\epsilon^2b^2\Big) - \frac{ab}{\epsilon^2} \notag\\
&\geqstep{3} \Omega_\epsilon + \frac12\Big(\Omega_\epsilon^2-\frac1{\epsilon^2}\Big)(a^2+b^2) \notag\\
&\eqstep{4} \Omega_\epsilon + \frac12 M^2(a^2+b^2) \ \ge\ \Omega_\epsilon .
\label{eq:prod_fluctuation_lower_bound}
\end{align}
**(1)** Expand $(\phi_R-\phi_L)^2$ in \eqref{eq:pair_hamiltonian}. The $\phi_R^2$ and $\phi_L^2$ pieces
raise $M^2$ to $\Omega_\epsilon^2$. The cross term factorizes by \eqref{eq:product_state_covariance_zero}.\quad
**(2)** Shift $\phi_R$ and $\pi_R$ by their mean values. Then $\braket{h_R}$ splits into
$\tfrac12\braket{\pi_R}^2+\tfrac12\Omega_\epsilon^2a^2$ plus the energy of a state with zero mean field and
momentum. That last energy is at least the ground-state energy $\tfrac12\Omega_\epsilon$ of an oscillator of
frequency $\Omega_\epsilon$. Finally drop $\tfrac12\braket{\pi_R}^2\ge0$. The same holds for $h_L$.\quad
**(3)** Use $ab\le\tfrac12(a^2+b^2)$.\quad
**(4)** $\Omega_\epsilon^2-1/\epsilon^2=M^2$.

The bound is reached by the product of the ground states of $h_R$ and $h_L$. It also holds for mixed
product states $\rho_R\otimes\rho_L$, since these are mixtures of pure product states. In that best product
state, each field is squeezed to a small spread, of order $\epsilon$, instead of the large vacuum spread of
order $1/M$:
\begin{equation}
\braket{\phi_R^2}_{\rm prod,\,best} = \frac{1}{2\Omega_\epsilon} \approx \frac{\epsilon}{2},
\qquad\text{compared with}\qquad
\braket{\phi_R^2}_\Omega = \frac14\left(\frac1{\omega_+}+\frac1{\omega_-}\right) \approx \frac{1}{4M} .
\label{eq:hcut_prod_divergence}
\end{equation}

Subtracting the vacuum energy \eqref{eq:pair_vacuum_energy} gives the minimum extra energy needed to remove
the entanglement of this one transverse mode across the cut:
\begin{align}
\Delta E_{\rm cut}(\vec k_\perp) &\equiv \min_{\rm prod}\braket{H_{\rm pair}} - E_{\rm vac}
= \Omega_\epsilon - \tfrac12(\omega_+ + \omega_-) \notag\\
&= \frac1\epsilon\left[\sqrt{1+u^2} - \tfrac12\Big(u + \sqrt{u^2+2}\Big)\right],
\qquad u \equiv M\epsilon .
\label{eq:delta_e_single_mode}
\end{align}
This is strictly positive. Indeed, $\Omega_\epsilon$ is the square root of the average of $\omega_+^2=M^2$ and
$\omega_-^2=M^2+2/\epsilon^2$, while $\tfrac12(\omega_++\omega_-)$ is the average of their square roots. The
square root is strictly concave, so the second is always smaller. For $u\to0$ (a transverse mode much
lighter than the cutoff), the bracket equals $1-1/\sqrt2\approx0.29$. At $u=1$ it equals
$\sqrt2-\tfrac12(1+\sqrt3)\approx0.048$, and a quick numerical check shows it decreases steadily in between.
So every transverse mode with $M\lesssim1/\epsilon$ costs an energy of order $1/\epsilon$.

**Check on the full chain.** The two-site truncation is crude, so we checked the result numerically on
the full chain \eqref{eq:lattice_chain_hamiltonian}. Because the Hamiltonian is quadratic, the minimum energy
over product states can be computed exactly: it is the sum of the ground-state energies of the two half-chains,
with the cut link replaced by the on-site terms $\phi_R^2/(2\epsilon^2)$ and $\phi_L^2/(2\epsilon^2)$. For a
chain of 800 sites, the extra energy over the vacuum comes out as about $0.14/\epsilon$ for $M=0$ and
about $0.030/\epsilon$ for $M=1/\epsilon$. These are roughly half to two-thirds of the two-site values, with the same
$1/\epsilon$ scaling. So the truncation changes the numerical constant but not the conclusion.

### 5. Summing over the entangling surface

To remove the entanglement across the whole surface $\partial R$, every transverse mode must be disentangled.
The energy is a sum over transverse modes, and in a product state across the cut, the reduced state of each
mode is itself a (possibly mixed) product state. So the bound \eqref{eq:delta_e_single_mode} applies to every
mode separately. The number of transverse modes per unit area, with momenta in $\dd^{d-2}k_\perp$, is
$\dd^{d-2}k_\perp/(2\pi)^{d-2}$. We keep the modes with $|\vec k_\perp| \le 1/\epsilon$, the same cutoff as
in the perpendicular direction, and assume the mass is small compared with the cutoff, $m\epsilon\ll1$. Let
$c_{\min}>0$ be the smallest value of the bracket in \eqref{eq:delta_e_single_mode} over this range of $u$;
it is about $0.048$. Then
\begin{align}
\Delta E_{\rm prod} &\eqstep{1} \mathrm{Area}(\partial R) \int_{|\vec k_\perp| \le 1/\epsilon}
\frac{\dd^{d-2}k_\perp}{(2\pi)^{d-2}} \, \Delta E_{\rm cut}(\vec k_\perp) \notag \\
&\geqstep{2} \mathrm{Area}(\partial R)\, \frac{c_{\min}}{\epsilon}
\int_{|\vec k_\perp| \le 1/\epsilon} \frac{\dd^{d-2}k_\perp}{(2\pi)^{d-2}} \notag\\
&\eqstep{3} \mathrm{Area}(\partial R)\, \frac{c_{\min}}{\epsilon}\,
\frac{V_{d-2}}{(2\pi)^{d-2}}\,\frac{1}{\epsilon^{d-2}} .
\label{eq:total_prod_energy_integral}
\end{align}
**(1)** The transverse modes are independent, so their minimum excitation energies add.\quad
**(2)** Each mode costs at least $c_{\min}/\epsilon$, by \eqref{eq:delta_e_single_mode}.\quad
**(3)** The integral is the volume of a ball of radius $1/\epsilon$ in $d-2$ dimensions, divided by
$(2\pi)^{d-2}$. Here $V_{d-2}$ is the volume of the unit ball in $d-2$ dimensions (with $V_0=1$).

Collecting the constants into $C = c_{\min}V_{d-2}/(2\pi)^{d-2}$ gives the main result of this section.
\begin{keyresult}
\begin{equation}
\Delta E_{\rm prod} \ge C \cdot \frac{\mathrm{Area}(\partial R)}{\epsilon^{d-1}} \;\xrightarrow{\;\epsilon \to 0\;} \; +\infty ,
\label{eq:product_state_energy_divergence}
\end{equation}
where $C > 0$ is a positive constant of order one that depends on the dimension (and, through the full-chain
correction, on the details of the lattice).
\end{keyresult}
The scaling has a simple interpretation. Disentangling the two sides costs an energy density of order the
cutoff scale, $1/\epsilon^{d}$, in a layer of thickness $\epsilon$ around the entangling surface.

Here is what \eqref{eq:product_state_energy_divergence} shows, and what it does not show.

1. **An infinite energy barrier.** The energy needed to disentangle a region $R$ from its
complement $L$ grows like $\epsilon^{-(d-1)}$ and diverges in the continuum limit. A product state would need
to break the correlations between neighbouring field values at every point of $\partial R$, and this costs an
energy of order the cutoff scale per mode.
2. **No product state has finite energy.** The physical Hilbert space of a continuum field theory, the
vacuum sector, is built from finite-energy excitations of the vacuum. (Mathematically, it is the Fock space,
or the GNS space of the vacuum.) Since $\Delta E_{\rm prod} = +\infty$, no product state across the cut is
one of these finite-energy states.
3. **Failure of factorization.** A tensor product $\HH_L \otimes \HH_R$ is, by definition, spanned by
product vectors $\ket{\psi_L}\ket{\chi_R}$. The energy estimate therefore makes the following statement
very plausible:
\begin{equation}
\boxed{\HH \ne \HH_L \otimes \HH_R \quad \text{in any continuum relativistic quantum field theory.}}
\label{eq:non_factorization_conclusion}
\end{equation}
Here the factorization is meant in the physical sense: the $L$-fields act on the first factor and the
$R$-fields on the second. The energy argument alone is not a proof, because it only rules out product states
of finite energy. The rigorous statement is a theorem of algebraic quantum field theory, which we quote here
and discuss in Chapter~4: the algebra of observables of a region like $R$ is a von Neumann algebra of type
$\mathrm{III}_1$, and an algebra of type III can never be of the form $B(\HH_R)\otimes\id$ for any tensor
factorization.


### 6. The algebraic version: type $\mathrm{III}_1$ and the split property

The energy divergence has a precise algebraic counterpart, which we quote without proof.

- Suppose two spatial regions $R_1$ and $R_2$ are separated by a **finite buffer** of width
$\delta > 0$, so that $\text{dist}(R_1, R_2) = \delta$. Then the gradient energy across the gap is controlled
by $\delta$ rather than by the cutoff $\epsilon$. In this case a state that is unentangled between $R_1$ and
$R_2$ *emph* be prepared. Heuristically, the estimate above with $\epsilon$ replaced by $\delta$ suggests
that its energy cost is finite but grows without bound as $\delta\to0$. The algebraic statement is the
**split property** of quantum field theory (established under mild assumptions by Buchholz,
Doplicher, Longo, Wichmann, and others). It says that there is an intermediate type I factor $\mathcal{N}$
with $\M(R_1) \subset \mathcal{N} \subset \M(R_2)'$. Because $\mathcal N$ is a type I factor, it provides a tensor factorization
$\HH=\HH_1\otimes\HH_2$ with $\mathcal N=B(\HH_1)\otimes\id$. The operators of $R_1$ act on the first factor,
and those of $R_2$ act on the second.
- As the buffer shrinks to zero ($\delta \to 0$, so that the regions touch along a common boundary), this
intermediate type I factor ceases to exist, and the estimated energy cost diverges. What remains is the
algebra $\M(R)$ of the region itself, which is not type I or type II. It is a **type $\mathrm{III**_1$
factor}, the most strongly entangled type in the classification (Chapter~4).


## The fix: define a subsystem by what you can *emph*, not by how you'd *emph*

The way out is simple to state before any formalism is attached to it. Do not define a subsystem $R$ by
declaring a factorization $\HH=\HH_R\otimes\HH_L$ in advance. Instead, define it operationally: *emph* Concretely, that observer has access to
some collection of operators $\M\subset B(\HH)$, where $B(\HH)$ is the set of all bounded operators on the
full Hilbert space $\HH$. The collection $\M$ contains every self-adjoint combination of things the
observer's apparatus can measure, and every unitary transformation it can apply. This definition does not
require $\HH$ to factorize. It only requires that you can say, of any given operator, whether or not it
belongs to the observer's toolkit.

This reframing costs nothing in the ordinary case. When $\HH=\HH_R\otimes\HH_L$ does exist, the natural
choice is $\M=B(\HH_R)\otimes\id_L$, the set of every operator acting only on $R$. This recovers the familiar
picture exactly, as Chapter~2 makes precise. The reframing also works in the broken case, because ``the set
of operators an $R$-observer can apply'' is a perfectly sensible notion even when there is no factorization
for it to come from. You lose nothing, and you gain a definition that survives exactly where the old one
fails.

What kind of mathematical object should $\M$ be? It should contain the identity, and be closed under sums,
products, and taking the Hermitian conjugate. It should also be closed under some notion of limit. An object
with these properties is a **von Neumann algebra**. There are two main candidate notions of "limit,"
which turn out to be inequivalent, and the difference between them matters a great deal. Pinning down the
right one is the subject of Chapter~2.

Historically, this is not a new invention grafted onto quantum mechanics from outside. John von Neumann was
one of the people who built the mathematical foundations of quantum mechanics in the first place. He
introduced these algebras in 1929, and in a series of papers from 1936 to 1943 he and Francis Murray
classified them into types. For decades this classification lived mostly inside pure mathematics. The modern
insight builds on work going back to Rehren around 2000, and has been developed intensively since about
2021 by Leutheusser, Liu, Witten, and others~[Liu2025]. It is that this same classification, applied to
the algebra $\M$ of an observer's accessible operators, tracks how entangled that observer's subsystem is with
everything the observer cannot access. In this way a piece of abstract functional analysis from the 1930s
becomes a working tool for quantum gravity.

## Two organizing claims

Two claims organize everything that follows. The first is:


*emph* $\;\longleftrightarrow\;$ *emph*


The second is that finer tools from the same theory give much sharper information about entanglement than the
broad type alone. These tools are modular theory (Chapter~4) and the crossed product (Chapter~5).

At this point these claims are *emph*, not yet demonstrated. The double-headed arrow above is not a
formal theorem with a name and a citation. It is a dictionary, built up entry by entry over Chapters~3
and~4. Each von Neumann algebra type (I, then II, then the subtypes of III) is matched, on specific worked
examples, to a specific qualitative pattern of entanglement between a subsystem and its complement. By the
end of Chapter~4 the correspondence will have been shown concretely, on examples you can check by hand.

Similarly, this chapter only motivates the deeper claim that entanglement structure is what *emph*
bulk spacetime geometry. The motivation comes from the Ryu—Takayanagi formula and from the broader
"entanglement builds geometry" literature (Van~Raamsdonk~[VanRaamsdonk],
Maldacena—Susskind~[MaldacenaSusskind]). The actual mechanism is subregion-subalgebra duality: the
statement that a boundary algebra of a specific type is identical to, not merely related to, the algebra of
observables of a bulk causal region. That mechanism is developed in Chapter~7. This chapter is a map of where
we are going and why we are going there.

## Plan of the notes

The notes split into two halves. Where the split falls says something about how the argument is built.

**Chapters~2—5: the mathematics, with no gravity or holography.** This half is pure operator-algebra
theory. It is developed using only examples from ordinary quantum mechanics, mostly the entangled spin-pair
system above, which are simple enough to work out by hand. Chapter~2 explains what a von Neumann algebra is
and how such algebras are classified. It also shows how to build a Hilbert space from an algebra and a state
(the GNS construction). Chapters~3 and~4 show, type by type, how the classification tracks entanglement
structure. Chapter~3 treats the "easy" types, I and II, for which a density matrix and an entropy can still
be defined. Chapter~4 treats type III, for which no density matrix exists at all. Saying anything quantitative
about type III needs a new tool, Tomita—Takesaki modular theory. Chapter~5 introduces the *emph*. This construction takes a type III algebra, attaches an auxiliary quantum clock to it, and produces
a new, better-behaved algebra of type II. At that stage it is a purely algebraic device. In Chapter~9 it turns
out to describe what a physical observer carrying a physical clock does to gravitational observables.

**Chapters~6—10: applying the machinery to quantum gravity.** Chapter~6 sets up the large-$N$
algebraic formulation of AdS/CFT. Chapter~7 introduces subregion-subalgebra duality, the central physics
claim: a bulk spacetime region and a specific boundary operator algebra are the same object, described in two
languages. It uses this duality to restate entanglement-wedge and causal-wedge reconstruction (ideas you may
have met in AdS/CFT courses) in algebraic language. Chapter~8 shows how bulk causal structure and horizons can
be read off from the type and commutant structure of boundary algebras, with no bulk metric assumed. The same
tools even decide whether two disconnected boundary theories are joined by a wormhole. Chapter~9 builds
simple, solvable toy models of observers with physical clocks, using the crossed product of Chapter~5. These
models reproduce the generalized entropy of black holes and of de~Sitter space (up to an additive constant)
from the operator-algebraic machinery alone. Chapter~10 summarizes, and discusses what all this suggests
about the mathematical structure of quantum gravity.

## Conventions and notation

Each item below is used many times later without further comment. So each one is explained here rather than
just listed.


- **Large $N$ versus finite $N$.** "Large $N$" (equivalently $G_N\to0$) means working in a
perturbative expansion in powers of $1/N$. You may keep more than the leading term, but $1/N$ is still
treated as a small expansion parameter, just as in ordinary perturbation theory in quantum mechanics.
"Finite $N$" (finite $G_N$) means the opposite. It means treating $N$ (or $G_N$) as a fixed number, with no
expansion at all. This is the nonperturbative regime of full quantum gravity. Most of these notes work at large
$N$. Finite-$N$ questions are the hardest open problems, and they are discussed mainly at the ends of
Chapters~7 and~9.
- **$\HH$, $B(\HH)$, and boundedness.** $\HH$ is a Hilbert space: a complex vector space with an
inner product, complete in the norm defined by that inner product. This is the same notion you know from
ordinary quantum mechanics, except that it may be infinite-dimensional. $B(\HH)$ is the set of
*emph* operators on $\HH$. An operator $A$ is bounded if there is some finite number $c$ such that
$\|A\ket\psi\|\le c\|\ket\psi\|$ for every vector $\ket\psi\in\HH$. Informally, $A$ never stretches the length
of a vector by more than a fixed factor, whatever vector you feed it. Finite matrices are automatically
bounded.

Some familiar operators are *emph* bounded. Position $\hat x$ and momentum $\hat p$ for a particle on a
line are examples. The ratio $\|\hat x\ket\psi\|/\|\ket\psi\|$ can be made as large as you like by choosing
$\ket\psi$ concentrated far from the origin. Similarly, $\|\hat p\ket\psi\|/\|\ket\psi\|$ can be made large
by choosing $\ket\psi$ that oscillates rapidly. We avoid this issue by working with bounded operators
throughout. For an unbounded observable, one uses its bounded functions instead. For example, $e^{i\hat x}$ is
bounded even though $\hat x$ is not. In field theory one uses bounded functions of smeared fields in the same
way. No physical information is lost, because an unbounded observable is determined by its bounded functions
(for instance, by its spectral projections). This convention lets the norm-based definitions of Chapter~2
work cleanly.
- **$\id$** is the identity operator: "do nothing."
- **$\widetilde J^\pm(Y)$: causal future and past.** For a region $Y$ of a spacetime,
$\widetilde J^+(Y)$ is the set of all points that can be reached from some point of $Y$ by a future-directed
causal curve. A causal curve is a path that never moves faster than light. Physically, $\widetilde J^+(Y)$ is
everything that $Y$ could send a signal to, given unlimited time. $\widetilde J^-(Y)$ is the mirror image:
everything that could have sent a signal to some point of $Y$.

The tilde means that these sets are computed in the *emph* of the spacetime. This is a
technical device, standard in AdS/CFT, that adds a boundary "at infinity," so that causal curves reaching
arbitrarily far away are still tracked properly. For now you can picture the ordinary causal future and past.
The tilde starts to matter when the conformal completion appears, in Chapter~6.
- **Causal complement (single prime) and causal completion (double prime) of a spacetime region.**
The causal complement $Y'$ of a region $Y$ is the set of all points spacelike separated from every point of
$Y$. These are the points that can neither send a signal to, nor receive a signal from, any point of $Y$.
Loosely, $Y'$ is "everything that $Y$ has no causal contact with, in either direction."

The causal completion $Y''$ is the double complement, $(Y')'$. In general $Y''$ is *emph* than $Y$.
This is a real geometric fact, not a notational curiosity. $Y''$ is the largest region that has the same
causal complement as $Y$. For instance, the causal completion of a single point is just that point, so
nothing is added. But the causal completion of a spatial region $R$ on a Cauchy slice is its entire
*emph* (defined next). This is a bigger set, which extends into the past and the future.

The double-prime notation for spacetime regions deliberately echoes the double-prime notation for commutants
of operator algebras ($\M''$), met in Chapter~2. Once subregion-subalgebra duality is established in
Chapter~7, the causal completion of a region and the double commutant of an algebra turn out to be two faces
of the same fact.
- **$\bar R$, complement of a spatial region; $\hat R$, domain of dependence.** Let $R$ be a
subregion of a single spatial slice (a snapshot of space at one moment). Then $\bar R$ is its ordinary
set-complement on that slice: everything on the same slice that is not in $R$. The domain of dependence
$\hat R$ is a spacetime region built from $R$. It is the set of spacetime points $p$ such that *emph*
causal curve through $p$, extended as far as it can go in both directions, must cross $R$. Physics inside
$\hat R$ is completely determined by initial data given on $R$ alone. That is why it is called the domain of
*emph*. If $R$ is a full spatial slice, $\hat R$ is the entire spacetime. If $R$ is a proper
subregion, $\hat R$ is a diamond-shaped region, called a *emph*. It sits above and below $R$
and is bounded by the light rays that just graze the edge of $R$. This shape appears constantly from
Chapter~6 onward.
- **$\subset$ always means *emph* Whenever you see $\M_1\subset\M_2$ in these notes,
it means that $\M_1$ is strictly smaller than $\M_2$. Some other texts use the same symbol with the more
permissive meaning that allows equality; these notes do not.


With this vocabulary in hand (bounded operators, causal future and past, causal complement and completion,
domain of dependence), you can read the geometric statements of later chapters literally, rather than by
matching them to what looks familiar. Chapter~2 now builds the algebraic machinery that this chapter has been
pointing toward: $C^*$ and von Neumann algebras, states, projections, the type classification, and the GNS
construction that produces a Hilbert space from an algebra and a state.



---

# Introduction to von Neumann algebras

Chapter~1 ended with a proposal. A subsystem should be defined not by splitting the Hilbert space, but by
the collection of operators that an observer confined to the subsystem can use. This chapter makes that
proposal precise. By the end of it you will know what kind of mathematical object $\M$ must be, how such
objects are sorted into types, and how a Hilbert space can be *emph* from an algebra and a state
instead of being assumed at the start. Most definitions below come with a worked example that uses actual
numbers, often small matrices you can multiply out by hand. The definitions are abstract on first reading,
and watching them act on something small is the quickest way to make them concrete.

## Systems with an infinite amount of entanglement (recap)

Chapter~1 gave three examples: the chain of $N$ Bell pairs, lattice gauge theory, and a quantum field theory
cut in half. They motivate everything in this chapter. The lesson drawn from them was this: a subsystem
should be defined by *emph*, not by how the Hilbert space happens
to split. This chapter turns that idea into a mathematical definition.

## Von Neumann algebras as subsystems

### Setting the stage: what a Hilbert space and an operator are, restated carefully

The new definition is a statement *emph* Hilbert spaces and operators. So we first state exactly what
those are. Vague pictures of "vectors" and "operators" are not precise enough for what follows.

A Hilbert space $\HH$ is a vector space over the complex numbers with two extra properties. First, it has an
inner product $\braket{\cdot|\cdot}$. This is a rule that assigns a complex number $\braket{\xi|\eta}$ to each
pair of vectors. It is linear in the second argument and conjugate-linear in the first, and it satisfies
$\braket{\xi|\xi}\ge0$, with equality only for the zero vector. Second, it is complete. A *emph* is a sequence of vectors whose terms get arbitrarily close to each other, so that it "ought to"
converge. Completeness says that every Cauchy sequence really does converge to some vector in $\HH$. For a
spin-$\tfrac12$ particle, $\HH=\mathbb C^2$. Its vectors are pairs of complex numbers $(c_1,c_2)$, usually
written $c_1\ket0+c_2\ket1$. The inner product is the dot product with complex conjugation,
$\braket{\xi|\eta}=\xi_1^*\eta_1+\xi_2^*\eta_2$. A von Neumann algebra needs nothing more exotic than this.
The infinite-dimensional case (a quantum field, say) uses exactly the same definitions, with infinitely many
components instead of two.

An operator $A$ on $\HH$ is a rule that turns vectors into vectors, $A:\HH\to\HH$, and is linear:
$A(c_1\ket{\xi_1}+c_2\ket{\xi_2})=c_1 A\ket{\xi_1}+c_2A\ket{\xi_2}$. On $\mathbb C^2$, every linear operator is
a $2\times2$ matrix, and $A\ket\xi$ is ordinary matrix-vector multiplication. The **Hermitian
conjugate** (or adjoint) $A^\dagger$ of $A$ is the unique operator with
$\braket{\xi|A\eta}=\braket{A^\dagger\xi|\eta}$ for all $\xi,\eta$. For a finite matrix, this is the familiar
rule "transpose and complex-conjugate every entry." $A$ is **self-adjoint** (or Hermitian) if
$A=A^\dagger$. Self-adjoint operators are the ones that represent physical observables, because their
eigenvalues are real numbers, the kind of number a measurement can return. $B(\HH)$ denotes the set of
*emph* bounded operators on $\HH$. Boundedness was defined in Chapter~1. Informally, a bounded operator
does not stretch the length of any vector by more than some fixed factor.

### The new definition of subsystem

Here is the definition, with every piece spelled out. Suppose you have access to only some subset of
operators, $\M\subset B(\HH)$. This is not everything. It is only what your apparatus, in your location, with
your capabilities, can measure or apply. Let $\ket\Psi\in\HH$ be a state of the full system. Using only $\M$,
you can do two things:

- compute expectation values $\braket{\Psi|A|\Psi}$ for $A\in\M$, which predict the average reading of a
measurement of $A$ over many repetitions;
- act on the state, producing $B\ket\Psi$ for $B\in\M$, which changes the system by an operation you have
access to.

Whatever $\M$ is, it should be closed under three operations, because an observer with access to $\M$ can
already do each of them. If you can measure or apply $A$ and $B$, you can measure or apply $A+B$ (do both and
add the results) and $AB$ (do one after the other). You can also multiply by complex numbers. And if $A$ is
available, so is $A^\dagger$. For a self-adjoint $A$ this is automatic, since $A^\dagger=A$. In general it
says that your toolkit is closed under taking adjoints. A set closed under sums, products, and adjoints is
called a **$*$-subalgebra** of $B(\HH)$. The $*$ refers to the adjoint, which mathematics texts often
write as $A^*$ instead of $A^\dagger$. In these notes every $*$-subalgebra is also taken to contain the identity
operator $\id$, which is the operation "do nothing."

This alone is not quite enough. We also want $\M$ to be *emph*: if some operator can be approximated
arbitrarily well by elements of $\M$, it should count as an element of $\M$ too. Otherwise the set of things
you have access to would have artificial gaps. Here the story becomes subtle. There are two different,
inequivalent ways to make "approximated arbitrarily well" precise, and the choice between them matters a
great deal. The next section explains both.

With this notion of subsystem in hand, the **complement** of $\M$ is defined to be its commutant,

$$

\M' = \{B\in B(\HH) : BA=AB\ \ \forall A\in\M\} .

$$

One misreading of this definition is common enough to address right away. $\M'$ is *emph* the set of
operators that commute *emph*. It is the set of operators that *emph* commute with
*emph* element of $\M$. Two operators inside $\M'$ can fail to commute with each other. In fact, when
$\M'$ is a rich enough algebra (the usual case), it contains non-commuting pairs, just as $\M$ does. What
$\M'$ guarantees is only this: acting with anything in $\M'$ produces no interference with any measurement
made using $\M$. That is the operational meaning of "complement of a subsystem" here. It is not ``the other
half of a tensor factorization you could point to.'' It is ``everything that, as a matter of algebra, cannot
disturb what $\M$ measures.'' A fuller treatment, with the functional-analysis machinery spelled out, is given
in W.~Thirring's *emph*. Nothing beyond what is given here is needed for the rest
of these notes.


> [!NOTE] **Physics Connection: Spacelike Commutativity**
> You already know one instance of this idea from relativistic field theory. It is the cleanest bridge from
> the abstract definition to something you can compute. For a free scalar field $\phi$, the commutator of the
> field at two spacetime points is a fixed function times the identity operator, so it does not depend on the
> state:
> 
$$

> [\phi(x),\phi(y)] = i\Delta(x-y) .
> 
$$

> Here $\Delta$, the Pauli—Jordan function, is given by an integral over the on-shell momenta of the field. A
> standard textbook fact is that $\Delta(x-y)=0$ whenever $x-y$ is spacelike. The reason uses two properties of
> $\Delta$. First, $\Delta$ is Lorentz invariant: $\Delta(\Lambda z)=\Delta(z)$ for every proper orthochronous
> Lorentz transformation $\Lambda$. Second, $\Delta$ is odd, $\Delta(-z)=-\Delta(z)$, because the commutator is
> antisymmetric, $[\phi(x),\phi(y)]=-[\phi(y),\phi(x)]$. Now let $z$ be a spacelike vector in $3+1$ dimensions.
> Then there is a proper orthochronous Lorentz transformation with $\Lambda z=-z$. (Boost to a frame in which
> $z$ has no time component, rotate by $180^\circ$ about an axis perpendicular to $z$, and boost back.) Hence
> $\Delta(z)=\Delta(-z)=-\Delta(z)$, so $\Delta(z)=0$. For a timelike $z$ no such $\Lambda$ exists, because these
> transformations never exchange past and future. This is why microcausality, the statement that field
> operators at spacelike separation commute, comes out of the free-field construction automatically instead
> of being imposed as an extra axiom.
> 
> Now translate this into the language of this chapter. Let $\M(O)$ be the algebra generated by field
> operators smeared over a spacetime region $O$. Let $O'$ be its causal complement, the set of points
> spacelike separated from all of $O$. The vanishing of $\Delta$ at spacelike separation says exactly that
> $\M(O')\subseteq\M(O)'$. This is the *emph* axiom for the local algebras of a relativistic field
> theory, stated in general in Chapter~4. So in a relativistic field theory, every operator localized
> spacelike to $O$ lies in the commutant $\M(O)'$.
> 
> The abstract definition of $\M'$ adds one thing to this familiar fact. The commutant is defined by a purely
> algebraic condition, "commutes with everything in $\M$," which never mentions spacetime. Nothing in the
> definition forces every such operator to be localized in $O'$. In general, $\M(O)'$ can be strictly larger
> than $\M(O')$. When the two are equal, the theory is said to satisfy *emph* for the region $O$
> (Chapter~4). Haag duality holds in many standard cases but not in all, and whether it holds depends on the
> theory, the region, and the representation. So "commutes with $\M$" is a more general notion than ``is
> spacelike separated from $O$.'' Chapter~8 uses exactly this extra room: there, bulk causal structure is read
> off from boundary commutants that are larger than boundary causality alone would require.


## Basic properties: $C^*$ vs.\ von Neumann algebras, and the double commutant theorem

### Two notions of "the limit of a sequence of operators"

Take a sequence of operators $A_1,A_2,A_3,\dots$ in $\M$, and ask whether it converges to some operator $A$.
For ordinary numbers, "converges" has one obvious meaning. For operators there are several natural
meanings, and they are genuinely different.

**Norm convergence.** Every bounded operator has a norm, $\|A\|$. It is the smallest number such that
$\|A\ket\psi\|\le\|A\|\,\|\ket\psi\|$ for every vector $\ket\psi$: the "maximum stretch factor" of
Chapter~1. The norm satisfies the identity
\begin{equation}
\|A^\dagger A\|=\|A\|^2 .
\label{eq:Cstar-identity}
\end{equation}
It is easy to check on a simple case. Take $A=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}$ acting on
$\mathbb C^2$. Then $A^\dagger A = \begin{psmallmatrix}0&0\\0&1\end{psmallmatrix}$, whose largest eigenvalue
is $1$, so $\|A^\dagger A\|=1$. The norm $\|A\|$ is the largest singular value of $A$, which is also $1$. So
$\|A^\dagger A\|=1=1^2=\|A\|^2$, as the identity requires. A sequence $A_n$ **converges in norm** to $A$
if $\|A_n-A\|\to0$. This says that the largest possible discrepancy between $A_n\ket\psi$ and $A\ket\psi$,
taken over *emph* unit vectors $\ket\psi$ at once, shrinks to zero. It is a strong, uniform statement.

**Strong convergence.** $A_n$ **converges strongly** to $A$ if $\|(A_n-A)\ket\psi\|\to0$ for each
fixed vector $\ket\psi$. Each vector is tested separately, so the rate of convergence may differ from one
vector to another.

**Weak convergence.** $A_n$ **converges weakly** to $A$ if $\braket{\xi|A_n|\eta}\to
\braket{\xi|A|\eta}$ for every fixed pair of vectors $\ket\xi,\ket\eta$. This asks only that individual
matrix elements converge, one pair of vectors at a time. It is the weakest of the three demands.

Each notion implies the next one. If $\|A_n-A\|\to0$, then $\|(A_n-A)\ket\psi\|\le\|A_n-A\|\,\|\ket\psi\|\to0$,
so norm convergence implies strong convergence. And $|\braket{\xi|(A_n-A)|\eta}|\le\|\ket\xi\|\,
\|(A_n-A)\ket\eta\|$ by the Cauchy—Schwarz inequality, so strong convergence implies weak convergence. In
finite dimensions the three notions coincide completely. This is why the distinction never comes up in an
ordinary quantum mechanics course. In infinite dimensions they differ, and the gap between them is where
infinite-dimensional phenomena (quantum field theory, the $N\to\infty$ limit) live. The next example shows
the difference.


> [!EXAMPLE] **Worked Example:**
> Let
> $\HH = \ell^2(\mathbb N)$ be the infinite-dimensional Hilbert space of square-summable sequences, with
> standard orthonormal basis $\{\ket 1, \ket 2, \ket 3, \dots\}$. Consider the sequence of rank-one projections
> 
$$

> P_n \equiv \ket n\bra n .
> 
$$

> We test the convergence of $P_n$ as $n\to\infty$ in each of the three senses.
> 
1. **Weak convergence: $P_n \to 0$ weakly.** Take any two vectors
> $\ket\xi = \sum_{k=1}^\infty c_k\ket k$ and $\ket\eta = \sum_{k=1}^\infty d_k\ket k$, with
> $\sum |c_k|^2 < \infty$ and $\sum |d_k|^2 < \infty$. The matrix element is
> 
$$

> \braket{\xi|P_n|\eta} = \braket{\xi|n}\braket{n|\eta} = c_n^* d_n .
> 
$$

> The Cauchy—Schwarz inequality for series gives
> $\sum_{n=1}^\infty |c_n d_n| \le \sqrt{\sum |c_n|^2}\sqrt{\sum |d_n|^2} < \infty$. The terms of a convergent
> series tend to zero, so $c_n^* d_n\to0$. Hence $\braket{\xi|P_n|\eta} \to 0$ for *emph* pair of vectors,
> and $P_n$ converges weakly to the zero operator.
> 
>
2. **Strong convergence: $P_n \to 0$ strongly.** For a fixed vector $\ket\psi = \sum c_k\ket k$ we
> compute
> 
$$

> \|P_n\ket\psi\|^2 = \|\ket n\braket{n|\psi}\|^2 = |c_n|^2 \to 0 \quad \text{as } n\to\infty .
> 
$$

> The limit is zero because $|c_n|^2$ are the terms of the convergent series $\sum_k|c_k|^2$. Hence $P_n$
> converges strongly to $0$.
> 
>
3. **Norm convergence: $P_n$ does not converge in norm.** The operator norm takes the largest stretch
> over all unit vectors at once. The largest stretch is reached at $\ket\psi=\ket n$:
> 
$$

> \|P_n - 0\| = \sup_{\|\psi\|=1} \|P_n\ket\psi\| = \|P_n\ket n\| = \|\ket n\| = 1 .
> 
$$

> So $\|P_n - 0\| = 1$ for every $n$, and this never shrinks. Hence $P_n$ does *emph* converge to $0$ in
> norm. It does not converge in norm to anything else either. For $n\ne m$ the operator $P_n-P_m$ has
> eigenvalues $+1$ and $-1$, so $\|P_n-P_m\|=1$, and the sequence is not even a Cauchy sequence in norm.
>

> This is the standard example to keep in mind. Every matrix element settles down to zero, but the operator as
> a whole never becomes small in norm.


A $*$-subalgebra $\M$ that is complete under norm convergence is called a **$C^*$-algebra**. Here
"complete" means that every norm-convergent sequence in $\M$ has its limit back in $\M$. A $*$-subalgebra
that is complete under weak convergence is called a **von Neumann algebra**. (Strictly speaking, the
weak closure is defined with nets rather than sequences. Sequences give the right intuition, and nothing in
these notes depends on the difference.) Every von Neumann algebra is automatically a $C^*$-algebra. To see
this, suppose $A_n\in\M$ and $A_n\to A$ in norm. Then $A_n\to A$ weakly as well, so if $\M$ is weakly closed,
$A\in\M$. Weak closure is the stronger requirement, because it asks $\M$ to contain the limits of more
sequences. So von Neumann algebras are the more complete, more restrictive notion.

Which notion is the right one for a physical subsystem? Weak convergence, for a simple reason. What a
laboratory measures is a matrix element $\braket{\xi|A|\eta}$: an expectation value, or more generally a
transition amplitude. Weak convergence says exactly that each of these measurable numbers settles down. So
von Neumann algebras, and not the less complete $C^*$-algebras, capture ``the set of operators whose physical
predictions are under control.'' That is why they are the main tool in the rest of these notes.

There is one more difference between the two notions, and it matters for everything that follows. A
$C^*$-algebra can be defined abstractly, with no Hilbert space anywhere. It is a vector space with a product,
an adjoint, and a norm that satisfies the identity~\eqref{eq:Cstar-identity}, and it is complete in that
norm. You could specify one by its multiplication table and its norm, much as you specify a finite group by
its multiplication table, without saying what vectors it acts on. The definition of a von Neumann algebra
given above cannot be stated this way. Its completeness condition, weak convergence, is phrased in terms of
vectors $\ket\xi,\ket\eta$ in a specific $\HH$. (Mathematicians do have an abstract characterization of von
Neumann algebras, due to Sakai, but it is less direct and is not needed here.) This gap is exactly what the
GNS construction, worked through later in this chapter, is designed to close. Starting from nothing but an
abstract $C^*$-algebra and a state on it, GNS builds the missing Hilbert space. Only then can you ask whether
the algebra, represented on that Hilbert space, is also weakly closed.

### The double commutant theorem

Checking weak closure directly means verifying that *emph* weakly convergent sequence in $\M$ has its
limit in $\M$. That sounds like infinitely many checks. Von Neumann's double commutant theorem replaces this
topological chore with an algebraic check. For a $*$-subalgebra $\M\subset B(\HH)$ that contains the
identity,

$$

\M = \M'' \iff \M \text{ is weakly closed (a von Neumann algebra).}

$$

Here $\M''\equiv(\M')'$ is the commutant of the commutant. Read the logic slowly. You take the complement of
your subsystem, $\M'$: everything that cannot disturb $\M$. Then you take the complement of *emph*,
$\M''$: everything that cannot disturb anything in $\M'$. The theorem says that doing this twice brings you
back exactly to where you started, provided $\M$ was already a von Neumann algebra. If $\M$ is only a
$*$-subalgebra (closed under sums, products, and adjoints, but not weakly closed), then $\M''$ is in general
strictly larger than $\M$. It is the *emph* von Neumann algebra containing $\M$: $\M$ together with
every operator that can be approximated weakly by elements of $\M$. This is not an obvious fact. It is a real
theorem, and its proof uses the geometry of Hilbert space. Its value is that a purely algebraic operation
(take the commutant twice) carries out a topological completion (weak closure) for you, with no limits in
the definition at all.


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
> To find $\M'$, look for every $4\times4$ matrix $X$ that commutes with all the $\sigma_i\otimes\id_L$. Use the
> basis $\ket{00},\ket{01},\ket{10},\ket{11}$, where the first digit belongs to $R$ and the second to $L$. Rather
> than solving sixteen equations one by one, write $X$ as four $2\times2$ blocks:
> 
$$

> X = \begin{pmatrix} X_{11} & X_{12} \\ X_{21} & X_{22} \end{pmatrix}, \qquad X_{ij} \in M_2(\mathbb C) .
> 
$$

> In this basis $\sigma_z\otimes\id_L=\begin{psmallmatrix}\id_2&0\\0&-\id_2\end{psmallmatrix}$ and
> $\sigma_x\otimes\id_L=\begin{psmallmatrix}0&\id_2\\\id_2&0\end{psmallmatrix}$. Since $\sigma_x$ and $\sigma_z$
> generate all $2\times2$ matrices (their product is $\sigma_x\sigma_z=-i\sigma_y$), it is enough to commute $X$
> with these two. First,
> \begin{align}
> [\sigma_z\otimes\id_L,\, X]
> &\eqstep{1} \begin{pmatrix} X_{11} & X_{12} \\ -X_{21} & -X_{22} \end{pmatrix}
> - \begin{pmatrix} X_{11} & -X_{12} \\ X_{21} & -X_{22} \end{pmatrix}
> \eqstep{2} \begin{pmatrix} 0 & 2X_{12} \\ -2X_{21} & 0 \end{pmatrix} .
> \notag
> \end{align}
> **(1)** multiplying by $\sigma_z\otimes\id_L$ on the left flips the sign of the bottom row of blocks;
> multiplying on the right flips the sign of the right column of blocks.\quad
> **(2)** subtract block by block.
> 
> Setting this to zero forces $X_{12}=X_{21}=0$, so $X$ is block-diagonal. Next, for block-diagonal $X$,
> \begin{align}
> [\sigma_x\otimes\id_L,\, X]
> &\eqstep{1} \begin{pmatrix} 0 & X_{22} \\ X_{11} & 0 \end{pmatrix}
> - \begin{pmatrix} 0 & X_{11} \\ X_{22} & 0 \end{pmatrix}
> \eqstep{2} \begin{pmatrix} 0 & X_{22}-X_{11} \\ X_{11}-X_{22} & 0 \end{pmatrix} .
> \notag
> \end{align}
> **(1)** multiplying by $\sigma_x\otimes\id_L$ on the left swaps the two rows of blocks; multiplying on
> the right swaps the two columns of blocks.\quad
> **(2)** subtract block by block.
> 
> Setting this to zero forces $X_{22}=X_{11}$. Call this common block $B$. Every $X$ that commutes with $\M$
> therefore has the form
> 
$$

> X = \begin{pmatrix} B & 0 \\ 0 & B \end{pmatrix} = \id_R \otimes B , \qquad B \in M_2(\mathbb C) .
> 
$$

> Since $B$ is an arbitrary $2\times2$ matrix, $\M' = \id_R \otimes B(\HH_L)$. The commutant of ``everything
> $R$ can do'' is "everything $L$ can do".
> 
> Now compute the second commutant $\M''=(\M')'$. An operator
> $Y=\begin{psmallmatrix} Y_{11} & Y_{12} \\ Y_{21} & Y_{22} \end{psmallmatrix}$ in $\M''$ must commute with
> every $\id_R\otimes B=\begin{psmallmatrix} B & 0 \\ 0 & B \end{psmallmatrix}$. Multiplying out, this says
> $Y_{ij}B=BY_{ij}$ for each block and for every $2\times2$ matrix $B$. The only $2\times2$ matrices that commute
> with every $2\times2$ matrix are multiples of the identity. (Commuting with
> $\begin{psmallmatrix}1&0\\0&0\end{psmallmatrix}$ removes the off-diagonal entries, and commuting with
> $\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}$ makes the two diagonal entries equal.) So
> $Y_{ij}=a_{ij}\id_2$, and
> 
$$

> Y = \begin{pmatrix} a_{11}\id_2 & a_{12}\id_2 \\ a_{21}\id_2 & a_{22}\id_2 \end{pmatrix}
> = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} \otimes \id_L \in \M .
> 
$$

> Every such $Y$ lies in $\M$, and every element of $\M$ has this form, so $\M''=\M$. All three algebras are
> 4-dimensional, and the double commutant theorem holds here by direct calculation.
> 
> A second example shows what happens when $\M$ is *emph* simply "all operators on one tensor factor."
> It also previews the notion of a *emph*, defined just below. Take the same $\HH=\mathbb C^4$, but now
> ignore any tensor-product structure. Let $\M$ be spanned by the two matrices $P_1=\mathrm{diag}(1,1,0,0)$ and
> $P_2=\mathrm{diag}(0,0,1,1)$. This is the algebra of an observer who can only tell whether the system is in
> "block one" or "block two," and nothing finer. Solving the same kind of linear system shows that $\M'$ is
> 8-dimensional. It consists of every operator that acts as an arbitrary $2\times2$ block within each of the
> two sectors, without mixing them: two independent $2\times2$ complex matrices, so $4+4=8$ complex
> parameters. The second commutant $\M''$ comes out to be exactly $\M$ again, which is 2-dimensional. Something
> happens here that did not happen in the first example: $\M\subset\M'$. Both $P_1$ and $P_2$ commute with
> *emph* in the block-diagonal algebra $\M'$. So $\M$ is small enough to commute with its own
> complement. Whenever this happens, $\M$ has a nontrivial *emph*, and that has a physical meaning. $\M$
> does not describe one indivisible subsystem. It describes a classical label (which block you are in),
> possibly with further subsystems inside each block. The discussion of the center below comes back to this
> example.


\begin{quote}
**Where the entangled subsystem lives.** Putting the last two subsections together: a subsystem is a von
Neumann algebra $\M\subset B(\HH)$, and its complement is the commutant $\M'$. In this framework, bipartite
entanglement is a statement about the pair $(\M,\M')$, not about a tensor factorization. When a factorization
$\HH=\HH_R\otimes\HH_L$ does exist, the choice $\M=B(\HH_R)\otimes\id_L$ gives back exactly the familiar
story. That is the first worked example above. Chapter~3 calls this special case a *emph*.
\end{quote}

Several further facts about commutants are used freely later, so we collect them here. Let $\Alg$ be any
$*$-subalgebra, not necessarily weakly closed.

- $\Alg'=\Alg'''$. The commutant of $\Alg$ is already a von Neumann algebra: a short argument shows
$\Alg'=(\Alg')''$ directly.
- $\M\equiv\Alg''$ is the smallest von Neumann algebra containing $\Alg$, and it has the same commutant
as $\Alg$: $\M'=\Alg'''=\Alg'$.
- For two von Neumann algebras $\M_1,\M_2$, the **join** $\M_1\vee\M_2\equiv(\M_1\cup\M_2)''$ is the
smallest von Neumann algebra containing both. The **meet** $\M_1\wedge\M_2\equiv\M_1\cap\M_2$ is their
intersection. The intersection is already a von Neumann algebra, so no double commutant is needed on that
side.
- These satisfy a De~Morgan-type duality, $(\M_1\vee\M_2)'=\M_1'\wedge\M_2'$. Joining two algebras and
then taking the complement gives the same result as taking each complement first and then intersecting. (The
left side is $(\M_1\cup\M_2)'''=(\M_1\cup\M_2)'$, and an operator commutes with everything in
$\M_1\cup\M_2$ exactly when it commutes with $\M_1$ and with $\M_2$.)


The **center** of $\M$ is $Z(\M)\equiv\M\cap\M'$. It consists of the operators that commute with
everything in $\M$ *emph* with everything in $\M'$. In the second worked example above, $\M\subset\M'$,
so $Z(\M)=\M$: the center is as large as it can possibly be. At the other extreme, $\M$ is called a
**factor** (or is said to be **primary**) if its center is as small as possible,
$Z(\M)=\mathbb C\,\id$, containing only multiples of the identity. The first worked example,
$\M=B(\HH_R)\otimes\id_L$, is a factor. Indeed, an operator that has both the form $A\otimes\id_L$ and the
form $\id_R\otimes B$ must be a multiple of the identity, as a direct comparison of the two forms shows. A
general von Neumann algebra can always be decomposed into a direct sum, or more generally a direct integral,
of factors. So the classification of von Neumann algebras reduces to classifying factors, plus bookkeeping
for the classical labels carried by the center. For this reason, from here on and for almost all of the
notes, we restrict attention to factors.

## Weights and states

### The definitions

A **linear functional** $\omega$ on $\M$ is a rule that assigns a complex number $\omega(A)$ to every
$A\in\M$ and respects addition and multiplication by numbers: $\omega(aA+bB)=a\,\omega(A)+b\,\omega(B)$. It is
**positive** if $\omega(A^\dagger A)\ge0$ for every $A$. This is a natural requirement. The operator
$A^\dagger A$ plays the role of $|A|^2$: it is always a non-negative operator, the operator analogue of a
squared magnitude, so it should never be assigned a negative number. A positive functional is automatically
compatible with the adjoint, $\omega(A^\dagger)=\omega(A)^*$. (This follows from positivity applied to
$(\id+A)^\dagger(\id+A)$ and $(\id+iA)^\dagger(\id+iA)$.) We use this property freely. In these notes a positive
linear functional is called a **weight**. (In the mathematical literature a weight is also allowed to
take the value $+\infty$ on some positive elements, as the ordinary trace does on $B(\HH)$ when $\HH$ is
infinite-dimensional. Traces of this kind appear in Chapter~3.) A weight is a **state** if it is also
normalized, $\omega(\id)=1$. It is a **trace** if $\omega(AB)=\omega(BA)$. This is the cyclic property of
the ordinary matrix trace, $\Tr(AB)=\Tr(BA)$. Positivity and linearity together give a useful inequality for
free. It is the direct analogue of the Cauchy—Schwarz inequality you know from vector inner products:
\begin{equation}
|\omega(A^\dagger B)|^2\le\omega(A^\dagger A)\,\omega(B^\dagger B) .
\label{eq:CS-omega}
\end{equation}

A state $\omega$ is one rule doing one thing: it assigns a single number, $\omega(A)$, to each $A\in\M$. What
that number means depends only on which operator you feed it, not on any change to $\omega$ itself. Feed it
a general observable $A$, and $\omega(A)$ is the expectation value of $A$. Feed it a projection $P_I$
instead, and $\omega(P_I)$ is a probability. Here $P_I$ is the spectral projection onto some range $I$ of
possible outcomes, defined later in this chapter. Positivity and normalization already force
$0\le\omega(P_I)\le1$, because both $P_I=P_I^\dagger P_I$ and $\id-P_I=(\id-P_I)^\dagger(\id-P_I)$ are of the
form $X^\dagger X$. Linearity gives $\omega(P_{I_1})+\omega(P_{I_2})=\omega(P_{I_1\cup I_2})$ for disjoint
ranges. It is the same formula and the same $\omega$ in both cases. The two readings, expectation value and
probability, come entirely from what sits inside the parentheses.

None of these definitions mentions a Hilbert space, a vector, or a density operator. This is the reason for
introducing weights and states this way, rather than going straight to a density matrix. $\omega$ is defined
only as a number assigned to each element of the algebra $\M$. A standard result, stated here without proof,
connects this back to density matrices. Call a state *emph* if it is continuous in a suitable weak
sense; these are the physically sensible states. Every normal state $\omega$ on $\M\subset B(\HH)$ can be
written as $\omega(A)=\Tr(\rho A)$ for some density operator $\rho$ on $\HH$. This $\rho$ acts on all of
$\HH$. It need not belong to $\M$, and in general it is not unique. So the density operator is a consequence
of the definition of $\omega$, not an input to it. $\omega$ is **faithful** if $\omega(A^\dagger A)=0$
forces $A=0$: nothing nonzero is invisible to it. $\omega$ is **pure** if it cannot be written as a
nontrivial mixture $\omega=\lambda\omega_1+(1-\lambda)\omega_2$ of two different states, with $0<\lambda<1$. If
it can, $\omega$ is said to **dominate** $\lambda\omega_1$ and $(1-\lambda)\omega_2$, since
$\omega-\lambda\omega_1$ and $\omega-(1-\lambda)\omega_2$ are still positive.

### What happens to the wavefunction once the algebra is taken as primary

These definitions look innocent. But they demote the wavefunction from a fundamental object to a derived
one, so we unpack them slowly.

An ordinary quantum-mechanical state is a vector $\ket\psi$ or, more generally, a density matrix $\rho$.
Both of these live in, or act on, a Hilbert space. You cannot even write down $\ket\psi$ without first having
$\HH$. The definition of $\omega$ needs none of that. It is a number assigned to each algebra element, and
the algebra $\M$ can be specified abstractly, as a $C^*$-algebra, with no Hilbert space in the definition.
This is more than a cosmetic change. It changes which object is treated as fundamental. In the ordinary
picture, you start with $\HH$, pick a vector $\ket\psi\in\HH$, and compute $\braket{\psi|A|\psi}$ for
whatever operators you like. In the algebraic picture, you start with the algebra $\M$ (what can be measured
or done) and a state $\omega$ on it (an expected outcome for every element of $\M$). Only afterward, if you
want one, do you build a Hilbert space and a vector that reproduce $\omega$. That construction is the GNS
construction, covered in full later in this chapter. The vector it produces is not fundamental data. It is a
derived bookkeeping device, specific to the state $\omega$ you started with. A different state can produce a
different Hilbert space that is physically inequivalent to the first.

The linearity of $\omega$, $\omega(A+B)=\omega(A)+\omega(B)$, also tells you something. It says that $\omega$
describes an *emph* over many repetitions, not a single outcome on one system. A single measurement
of $A+B$ on one system does not obviously split into "the result you would have got for $A$" plus ``the
result you would have got for $B$.'' In general you cannot even measure $A$ and $B$ together unless they
commute. But the *emph* of $A+B$ over a large ensemble of identically prepared systems does split
this way, simply because averaging is linear. So $\omega$ (equivalently the density matrix $\rho$, or in the
pure case the vector $\ket\psi$) is best read as a statement about an ensemble, not about one individual
system.

The statistical algebraic approach of Slavnov~[Slavnov2001] takes this one level deeper. It also
addresses the obvious next question: what, then, describes one individual system? Slavnov starts from
something more primitive than $\omega$. It is a functional $\varphi(\hat A)$ that returns the number a single
measurement of $\hat A$, on this particular system, would read out. It is not defined linearly on the whole
algebra. It is defined on one maximal set of *emph* observables at a time, that is,
observables that commute and so can be measured jointly. There is no averaging in this definition: $\varphi$
is a record of one concrete measurement outcome. The key point is this. Measuring one observable can disturb
your ability to measure another one that does not commute with it. So no experiment can pin down $\varphi$
completely. An experiment can only tell you that $\varphi$ belongs to an *emph* of
functionals that all agree with your data on the compatible set of observables $\{Q\}$ you chose to measure.
Slavnov proposes that this equivalence class, and not $\varphi$ itself, is what a conventional ``quantum
state'' $\Psi_Q$ is. On this view a quantum state is not a container of hidden, definite properties. It is a
precise record of how much you could possibly know, given that measuring one thing costs you the ability to
measure something incompatible with it.

On this view, one idea accounts for several facts that otherwise look like separate puzzles:


- **Why quantum probability is not "we just don't know the hidden variable yet."** The same
individual $\varphi$ can belong to the class $\Psi_Q=\{\varphi\}_Q$ or to a different class
$\Psi_P=\{\varphi\}_P$. Which one depends on which compatible set, $\{Q\}$ or $\{P\}$, the experimenter chooses
to measure. So the "quantum state" assigned to the system depends on an experimental choice made after the
system was prepared. Slavnov identifies this as the root of the Einstein—Podolsky—Rosen puzzle. On his
account, the EPR puzzle is not an additional strange feature of quantum mechanics. It is the same fact seen
from another angle.
- **Why $\rho$, not $\ket\psi$, is what enters every physical prediction.** $\rho$ (equivalently
$\omega$) is, by construction, one step of ensemble averaging removed from an individual $\varphi$. Textbooks
such as Sakurai's replace $\ket\psi$ by $\rho=\ket\psi\bra\psi$ as the basic object, so that pure and mixed
states are handled in the same way. That is the first half of this demotion. The algebraic framework of these
notes completes it: it replaces $\rho$, which needs a Hilbert space to be written as a matrix, with $\omega$,
which does not.
- **Why a Hilbert space appears at all, and in what sense it comes second.** Slavnov states this
directly: *emph* The primary elements are the algebra of observables and the state, both tied directly to
experiment. The state can be taken in Slavnov's individual sense $\varphi$, or in the ensemble sense $\omega$
used throughout these notes. The Hilbert space, its vectors, and the operators acting on them are all built
afterward, mechanically, by the GNS construction applied to $\omega$.


To state the conclusion of this viewpoint plainly, in one place: the wavefunction is not a physical entity
that stores values the way a hard drive stores bits. It is the name for an equivalence class of individual
measurement records. The records in one class cannot be told apart, because no experiment could distinguish
them, given what was actually chosen to be measured. The algebra, which says what is measurable and how
measurements combine, is the primary, observer-independent structure. The wavefunction depends on a choice
of what you decided to look at. This is an interpretation, not a theorem, and the mathematics in the rest of
the notes do not depend on adopting it. What the rest of the notes do use is the weaker statement: the
algebra and the state come first, and the Hilbert space is built from them.

## $C^*$ and von Neumann algebras generated by a single operator

This section is short. Given the two definitions ($C^*$-algebra and von Neumann algebra) from earlier in this
chapter, it is self-contained. It gives the concrete reason why projections, the subject of the next
section, live in von Neumann algebras and generally not in the smaller $C^*$-algebras.

Take one bounded, self-adjoint operator $\mathcal O$. What is the smallest $C^*$-algebra containing it,
$\Alg(\mathcal O)$, and the smallest von Neumann algebra containing it, $\M(\mathcal O)$? Both contain every
polynomial $\sum_n c_n\mathcal O^n$ in $\mathcal O$, since polynomials are made by repeated multiplication and
addition. Each must then be completed, in its own sense of limit, to become a full $C^*$-algebra or von
Neumann algebra.

The **spectrum** $\sigma(\mathcal O)$ of $\mathcal O$ is the set of numbers $\kappa$ for which
$\mathcal O-\kappa\id$ is not invertible. For a finite Hermitian matrix, the spectrum is its set of
eigenvalues: the numbers a measurement of $\mathcal O$ can return. A standard fact of functional analysis
(stated here without proof) is that $\Alg(\mathcal O)$ is isomorphic to the algebra of *emph*
functions on $\sigma(\mathcal O)$. Every element of $\Alg(\mathcal O)$ can be written as $f(\mathcal O)$ for a
continuous function $f$, and every such $f(\mathcal O)$ lies in $\Alg(\mathcal O)$. A simple example makes
this plausible. Let $\mathcal O$ be a finite Hermitian matrix with distinct eigenvalues
$\kappa_1,\dots,\kappa_n$. Applying a polynomial, or any function, to $\mathcal O$ means applying it to each
eigenvalue and leaving the eigenvectors alone. So specifying $f(\mathcal O)$ is the same as specifying the $n$
numbers $f(\kappa_1),\dots,f(\kappa_n)$, that is, a function on the finite set $\{\kappa_1,\dots,\kappa_n\}$.
On a finite set every function is continuous, so this example cannot yet show the distinction that matters
below. It does show the general shape of the isomorphism.


> [!NOTE] **Physics Connection: Eigenvalues vs.\ Eigenvectors**
> The definition of $\sigma(\mathcal O)$ never mentions an eigenvector or a Hilbert space. A number $\lambda$
> lies in $\sigma(\mathcal O)$ because $\mathcal O-\lambda\id$ has no inverse inside the algebra. So eigenvalues
> do not need to be demoted, as the vacuum vector $\ket\Omega$ will be in the GNS construction later in this
> chapter. They are already an algebra-level notion, fixed before any state or representation is chosen. What
> is demoted is the eigen*emph*. An eigenvector lives in whatever Hilbert space GNS builds for a given
> $\omega$, so it appears only once $\omega$ is chosen.
> 
> Check this on the number operator $N=a^\dagger a$ of the harmonic oscillator. (Strictly, $N$ is unbounded, so
> it is not an element of a $C^*$-algebra. The argument below uses only the commutation relation and
> positivity, so this does not matter.) We show that the possible eigenvalues of $N$ are fixed by
> $[a,a^\dagger]=1$ together with positivity, in every representation at once. Suppose $Nv=\lambda v$ for some
> nonzero vector $v$, in any representation of the algebra on a Hilbert space. First, $\lambda\ge0$:
> \begin{align}
> \lambda\,\|v\|^2
> &\eqstep{1} \braket{v|Nv} \notag\\
> &\eqstep{2} \braket{av|av} = \|av\|^2 \ \ge\ 0 . \notag
> \end{align}
> **(1)** $Nv=\lambda v$ by hypothesis.\quad
> **(2)** $N=a^\dagger a$ and the definition of the adjoint.
> 
> Next, lower with $a$:
> \begin{align}
> N(av)
> &\eqstep{1} \big(aN+[N,a]\big)v \notag\\
> &\eqstep{2} a(\lambda v) + (-a)v \notag\\
> &\eqstep{3} (\lambda-1)(av) . \notag
> \end{align}
> **(1)** $Na=aN+[N,a]$, the definition of the commutator.\quad
> **(2)** $Nv=\lambda v$ by hypothesis, and $[N,a]=[a^\dagger a,a]=[a^\dagger,a]\,a=-a$ from $[a,a^\dagger]=1$.\quad
> **(3)** collect the two terms, both proportional to $av$.
> 
> So $av$ is either zero or an eigenvector with eigenvalue $\lambda-1$. Repeating, $a^kv$ is either zero or an
> eigenvector with eigenvalue $\lambda-k$. Every eigenvalue is $\ge0$, so the vectors $a^kv$ cannot all be
> nonzero. Let $k$ be the last index with $a^kv\ne0$. Then $a(a^kv)=0$, so $N(a^kv)=a^\dagger a(a^kv)=0$, and
> the eigenvalue $\lambda-k$ must be $0$. Hence $\lambda=k\in\{0,1,2,\dots\}$. The same computation with
> $[N,a^\dagger]=a^\dagger$ gives $N(a^\dagger v)=(\lambda+1)(a^\dagger v)$. Here $a^\dagger v$ is never zero:
> $a^\dagger v=0$ would give $aa^\dagger v=(N+1)v=0$, so $\lambda=-1$, which contradicts $\lambda\ge0$. So once
> one eigenvalue occurs, all of $0,1,2,\dots$ occur. These are the quantized levels of the oscillator. They
> follow from the multiplication table of the algebra and positivity, whichever Hilbert space the operators
> act on. Choosing a state $\omega$ and running GNS only decides which eigenvectors appear, and with what
> weights. It never changes the spectrum itself.


$\M(\mathcal O)$, by contrast, is isomorphic to an algebra of *emph* functions on $\sigma(\mathcal O)$
that need not be continuous. (Precisely: bounded measurable functions, where two functions count as equal if
they differ only on a set that the spectral measure of $\mathcal O$ does not see.) Every continuous function
on the compact set $\sigma(\mathcal O)$ is bounded, so $\Alg(\mathcal O)\subset\M(\mathcal O)$. This fits with
von Neumann algebras being the larger, more complete objects. The difference becomes concrete and important
when $\sigma(\mathcal O)$ is a continuum, such as an interval of real numbers, rather than a finite set of
isolated points. This happens when $\mathcal O$ has continuous spectrum, which is the generic case in field
theory and in the $N\to\infty$ limits these notes are about. On a continuum, the **indicator function** of a
subset $I\subset\sigma(\mathcal O)$,

$$

f_I(\kappa) = \begin{cases} 1 & \kappa\in I \\ 0 & \kappa\notin I \end{cases} ,

$$

is bounded, since it only takes the values $0$ and $1$. But it is discontinuous wherever $I$ has an edge
inside the continuum. The corresponding operator $P_I\equiv f_I(\mathcal O)$ is a **spectral
projection**. For a matrix, it projects onto the span of the eigenvectors whose eigenvalues lie in $I$. In
general, it is the operator that answers the yes/no question ``does a measurement of $\mathcal O$ give a value
in the range $I$?'' Indicator functions are generically discontinuous on a continuum, so spectral projections
generically lie in $\M(\mathcal O)$ but not in $\Alg(\mathcal O)$. This is the concrete, checkable reason why
von Neumann algebras, and not merely $C^*$-algebras, are the right setting for the classification in the next
two sections. That classification is built entirely out of projections, and a $C^*$-algebra generally does
not contain the sharp yes/no measurement operators it needs.

## Projections

### Definitions, and what they mean physically

A **projection** is a self-adjoint operator $P$ with $P^2=P$. Applying it twice does nothing more than
applying it once. This is the algebraic signature of ``select a subspace and discard everything orthogonal to
it,'' which is what a sharp yes/no measurement does. The spectral theorem writes any self-adjoint operator in
terms of its spectral projections, as discussed in the previous section. As a result, every element of a von
Neumann algebra is a norm limit of finite linear combinations of projections in the algebra. This is why the
classification that follows can be phrased entirely in terms of projections, with nothing lost.


> [!NOTE] **Physics Connection: Probabilities from Projections**
> The section on weights and states noted that $\omega(P_I)$ reads as a probability because $P_I$ is a
> projection. Here is where that fact comes from. The previous section fixed the possible outcomes of measuring
> $\mathcal O$ as its spectrum $\sigma(\mathcal O)$. This is an algebra-level fact, decided before any state is
> chosen. For a range $I\subset\sigma(\mathcal O)$, the spectral projection $P_I$, built from $\mathcal O$ by
> the indicator-function construction, is itself an element of the von Neumann algebra. The Born rule of
> ordinary quantum mechanics gives the probability of an outcome in $I$ as $\braket{\psi|P_I|\psi}$. The
> algebraic version replaces $\ket\psi$ by $\omega$, so the probability is $\omega(P_I)$. The probability of an
> outcome is therefore not a second thing that $\omega$ supplies on top of expectation values. It is $\omega$
> evaluated on one particular algebra element, the spectral projection for that outcome, by the same rule
> $\omega$ uses for everything else.



> [!EXAMPLE] **Worked Example:**
> Let
> $A = \sigma_x + \sigma_z = \begin{psmallmatrix} 1 & 1 \\ 1 & -1 \end{psmallmatrix}$, an observable on
> $\mathbb C^2$. We construct its spectral projections explicitly and use them to compute probabilities.
> 
1. **Eigenvalues.** The characteristic equation is $\det(A - \lambda\id) = \lambda^2 - 2 = 0$, so
> the eigenvalues are $\lambda_\pm = \pm\sqrt{2}$.
>
2. **Spectral projections by Lagrange interpolation.** Let a $2\times2$ Hermitian matrix $A$ have
> distinct eigenvalues $\lambda_1, \lambda_2$. The projection onto the eigenspace of $\lambda_1$ is
> $P_1 = (A - \lambda_2\id)/(\lambda_1 - \lambda_2)$. The reason is that the polynomial
> $f(x)=(x-\lambda_2)/(\lambda_1-\lambda_2)$ equals $1$ at $\lambda_1$ and $0$ at $\lambda_2$, so $f(A)$ is the
> indicator function of $\{\lambda_1\}$ applied to $A$. For our $A$ this gives
> \begin{align}
> P_+ &= \frac{A + \sqrt2\,\id}{\sqrt2 + \sqrt2}
> = \frac{1}{2\sqrt2}\begin{pmatrix} 1+\sqrt2 & 1 \\ 1 & \sqrt2-1 \end{pmatrix} , \notag\\
> P_- &= \frac{A - \sqrt2\,\id}{-\sqrt2 - \sqrt2}
> = \frac{1}{2\sqrt2}\begin{pmatrix} \sqrt2-1 & -1 \\ -1 & \sqrt2+1 \end{pmatrix} . \notag
> \end{align}
>
3. **Checking the projection properties.**
> 


>
8. **Born-rule probabilities.** Suppose the system is in the state
> $\ket\psi = \ket0 = \begin{psmallmatrix} 1 \\ 0 \end{psmallmatrix}$. The probabilities of the two outcomes are
> \begin{align}
> \operatorname{Prob}(+\sqrt2) &= \braket{0|P_+|0} = \frac{1+\sqrt2}{2\sqrt2}
> = \frac12 + \frac{1}{2\sqrt2} \approx 0.853553 , \notag\\
> \operatorname{Prob}(-\sqrt2) &= \braket{0|P_-|0} = \frac{\sqrt2-1}{2\sqrt2}
> = \frac12 - \frac{1}{2\sqrt2} \approx 0.146447 . \notag
> \end{align}
> They add up to exactly $1$, as they must, since $P_++P_-=\id$. The expectation value is
> \begin{align}
> \braket{A}
> &\eqstep{1} (+\sqrt2)\operatorname{Prob}(+\sqrt2) + (-\sqrt2)\operatorname{Prob}(-\sqrt2) \notag\\
> &\eqstep{2} \sqrt2\Big(\frac12 + \frac{1}{2\sqrt2}\Big) - \sqrt2\Big(\frac12 - \frac{1}{2\sqrt2}\Big) \notag\\
> &\eqstep{3} 2\cdot\frac{\sqrt2}{2\sqrt2} = 1 \notag\\
> &\eqstep{4} \braket{0|\sigma_x+\sigma_z|0} . \notag
> \end{align}
> **(1)** take $\braket{0|\cdot|0}$ of the spectral decomposition $A=\sqrt2\,P_+-\sqrt2\,P_-$.\quad
> **(2)** insert the two probabilities just computed.\quad
> **(3)** the two $\sqrt2\cdot\tfrac12$ terms cancel, and the two remaining terms are equal.\quad
> **(4)** $\braket{0|\sigma_x|0}=0$ and $\braket{0|\sigma_z|0}=1$.
> 
> Numerically, $\sqrt2\,(0.853553-0.146447)=\sqrt2\,(0.707107)=1.000000$.
>

> The example shows how spectral projections break an observable into exact, mutually orthogonal yes/no
> questions. Each question has a probability, here $\braket{0|P|0}$, and the expectation value is recovered by
> weighting each outcome by its probability.


There is an exact correspondence between projections in $B(\HH)$ and closed subspaces of $\HH$. A projection
$P$ picks out the subspace $P\HH$, which consists of everything you get by applying $P$ to vectors in $\HH$.
Conversely, every closed subspace has a unique projection onto it. If $P\in\M$, the subspace $P\HH$ is said to
"belong to $\M$." Physically, it is a subspace that an observer with access to $\M$ can single out by a
measurement. The largest projection is the identity $\id$ (the whole space). Projections are partially
ordered: $P\le Q$ means $PQ=P$, or equivalently $P\HH\subseteq Q\HH$, so the subspace of $P$ sits entirely
inside the subspace of $Q$.

Two projections $P,Q\in\M$ are called **Murray—von Neumann equivalent**, written $P\sim Q$, if there is
a **partial isometry** $V\in\M$ with $P=V^\dagger V$ and $Q=VV^\dagger$. A partial isometry is an operator
that maps its input subspace onto its output subspace without stretching or shrinking lengths. So the
condition says that $V$ maps the subspace $P\HH$ isometrically (preserving lengths) onto the subspace
$Q\HH$, and that $V$ itself is available inside $\M$. This is the algebra-relative version of ``these two
subspaces have the same size.'' It is not the ordinary linear-algebra notion of dimension, which looks only
at the subspace itself. It is tied to what an observer with access to $\M$ can actually do to compare one
subspace with another.


> [!EXAMPLE] **Worked Example:**
> Return to $\M=B(\HH_R)\otimes\id_L$ on $\HH=\mathbb C^2\otimes\mathbb C^2$ from the
> double-commutant example above. Let $P=\ket0_R\!\bra0_R\otimes\id_L$ and $Q=\ket1_R\!\bra1_R\otimes\id_L$.
> Each is a rank-2 projection on the full 4-dimensional $\HH$. It picks out a 2-dimensional subspace: the
> $R$-qubit is fixed to $\ket0$ or to $\ket1$, and the $L$-qubit can be anything. The operator
> $V=\ket1_R\!\bra0_R\otimes\id_L$ is in $\M$, since it has the form $A\otimes\id_L$ with $A=\ket1\bra0$.
> Direct matrix multiplication gives $V^\dagger V=\ket0_R\!\bra0_R\otimes\id_L=P$ and
> $VV^\dagger=\ket1_R\!\bra1_R\otimes\id_L=Q$. So $P\sim Q$, through a partial isometry that lies entirely
> inside $\M$. This captures the intuitive fact that "the $R$-qubit is $\ket0$" and ``the $R$-qubit is
> $\ket1$'' are subspaces of the same size, related by a flip that an $R$-observer can actually perform.


A nonzero projection $P\in\M$ is called **finite** if it is *emph* equivalent to any strictly smaller
projection $Q<P$ in $\M$. It is called **infinite** if it is equivalent to some strictly smaller
projection $Q<P$ in $\M$. This definition takes some getting used to, because it does *emph* match the
linear-algebra notion of "finite-dimensional." The following example shows the difference. The useful
intuition turns out to be that the smallest projections pick out one copy of an irreducible representation.

Take $\M=B(\HH_1)\otimes\id_2$ on $\HH=\HH_1\otimes\HH_2$, where $\HH_2$ is *emph*-dimensional. Let
$P=\ket\psi\bra\psi\otimes\id_2$ for a single unit vector $\ket\psi\in\HH_1$. As a subspace of the full
Hilbert space, $P\HH$ is infinite-dimensional: it is a whole copy of $\HH_2$. Yet $P$ is a *emph*
projection of the algebra $\M$. There is no strictly smaller projection in $\M$ equivalent to it, because
$\M$ contains no nonzero projection strictly below $P$ at all. Inside $\M\cong B(\HH_1)$, the projection $P$
corresponds to a rank-one projection on $\HH_1$, the smallest nonzero rank there is. Here is the precise form
of the irreducible-representation intuition. As an *emph*, forgetting the Hilbert space it
acts on, $\M$ is isomorphic to $B(\HH_1)$. That is a single copy of the algebra of all operators on $\HH_1$,
and it acts irreducibly on $\HH_1$. The factor $\HH_2$ in $\HH=\HH_1\otimes\HH_2$ only counts *emph* of this irreducible representation sit side by side in the big Hilbert space: one copy for each basis
vector of $\HH_2$. The projection $P=\ket\psi\bra\psi\otimes\id_2$ picks out one direction *emph* the
irreducible representation, and it does so in every one of the infinitely many copies at once. That is why
$P$ is as small as $\M$ can make anything (finite, and in fact minimal, in the algebra) while being
infinite-dimensional as a subspace of $\HH$. Finiteness in this algebra-relative sense is a statement about
the irreducible representation, not about the dimension of the ambient Hilbert space. Keeping this
distinction in mind is what makes the type classification in the next section make sense, rather than look
like a strange use of the word "finite."

A projection $P$ is called **minimal** in $\M$ if it is nonzero and $\M$ contains no nonzero projection
strictly smaller than $P$. This is the algebra-relative notion of ``as small as a measurement outcome can
be.'' Every minimal projection is finite, since there is nothing smaller for it to be equivalent to. The
converse fails: a projection can be finite without being minimal. For example, in $\M=B(\mathbb C^3)$ every
projection is finite, because equivalent projections have equal rank. But $\mathrm{diag}(1,1,0)$ is not
minimal, since $\mathrm{diag}(1,0,0)$ lies strictly below it. More strikingly, an algebra can have no minimal
projections at all while still having plenty of finite ones. This possibility is the heart of the
classification in the next section.

Now apply these definitions to the largest projection, $P=\id$. For a von Neumann *emph* $\M$, the
identity is either finite or infinite, and this one question sorts factors into two coarse classes. If $\id$
is finite, then every projection in $\M$ is also finite (this can be shown from the definitions; we omit the
proof), and $\M$ is called a **finite von Neumann factor**. If $\id$ is infinite, $\M$ is called an
**infinite von Neumann factor**. In that case, when $\HH$ is separable, any two infinite projections in
$\M$ are equivalent to each other, so in particular every infinite projection is equivalent to the identity
itself (also stated without proof).

## Classification of von Neumann factors

### Building a dimension function out of nothing but $\sim$ and $\le$

Here is the payoff of the last two sections. Using only the equivalence relation $P\sim Q$ and the ordering
$P\le Q$, one can prove the following theorem (a standard result, stated here without proof). Every von
Neumann factor $\M$ has a **dimension function** $d$. It assigns a number $d(P)\in[0,\infty]$ to each
projection $P\in\M$, and it has three properties:

- $d(P)=d(Q)$ if and only if $P\sim Q$;
- $d(P+Q)=d(P)+d(Q)$ whenever $P$ and $Q$ are orthogonal, $PQ=0$;
- $d(P)<\infty$ if and only if $P$ is finite.

These properties fix $d$ up to an overall constant that you are free to rescale. In words: equivalent
subspaces get the same size, sizes add, and finite projections get finite sizes. Additivity also makes $d$
respect the ordering. If $P\le Q$, then $Q-P$ is a projection orthogonal to $P$, so
$d(Q)=d(P)+d(Q-P)\ge d(P)$. The inequality is strict when $P<Q$ and $P$ is finite, because $d(Q-P)>0$ for the
nonzero projection $Q-P$. These are exactly the properties you would want from anything worth calling a
"size." The function $d$ can also be packaged as a **trace**, $\tr(P)\equiv d(P)$, extended from
projections to other elements of $\M$ by linearity, using the fact that every self-adjoint operator is built
from its spectral projections. When $d(\id)=\infty$, this $\tr$ is finite only on part of $\M$, just as the
ordinary trace on an infinite-dimensional Hilbert space is finite only for trace-class operators. This $\tr$
plays the role of the ordinary matrix trace, generalized to an abstract algebra with no particular Hilbert
space singled out.

Why is the ordinary formula "dimension $=\Tr P$" not the right notion here? Here $\Tr$ is the ordinary
Hilbert-space trace, the sum of diagonal entries. The answer shows why an algebra-relative $d(P)$ is needed
at all. Take again $P=\ket\psi\bra\psi\otimes\id_2$ on $\HH_1\otimes\HH_2$ with $\HH_2$ infinite-dimensional,
the same example as above. The Hilbert-space trace $\Tr P$ is infinite, because $P\HH$ is an
infinite-dimensional subspace of $\HH$. But from the point of view of the algebra $\M\cong B(\HH_1)$, the
projection $P$ is the smallest nonzero thing there is: rank one, within $\HH_1$. The ordinary trace $\Tr$
sees the raw size of the ambient Hilbert space, and for describing what $\M$ can distinguish it gives the
wrong answer. The algebra-relative $d(P)$, normalized so that $d(P)=1$ for this minimal $P$, correctly reports
"this is the smallest measurable unit $\M$ has access to," however large the corresponding subspace of $\HH$
is. This is the concrete sense in which $\tr$ is a *emph* trace. It strips away the part of $\HH$
that $\M$ never had access to, and it reports only the size that $\M$ itself can distinguish.

### The three types

The whole classification now follows from one question: what values can $d(P)$ take, as $P$ ranges over all
the projections in $\M$?


- **Type I: $\M$ has minimal projections.** Normalize $d$ so that a minimal projection has $d=1$.
You are always free to rescale $d$ by an overall constant, so this is only a choice of units, like choosing
what counts as one unit of length. Every projection is then a sum of mutually orthogonal minimal
projections, and it can be shown that $d(P)$ is a nonnegative integer or $\infty$ for every $P$. This is the
familiar notion of dimension, now derived from the algebra instead of assumed. If $n=d(\id)$ is finite, $\M$
is called type $\mathrm I_n$. If $d(\id)=\infty$, so that there is no upper bound on the number of mutually
orthogonal minimal projections, $\M$ is type $\mathrm I_\infty$. For an ordinary separable Hilbert space
$\HH$, the algebra $B(\HH)$ itself is type $\mathrm I_n$ if $\HH$ is $n$-dimensional, and type
$\mathrm I_\infty$ if $\HH$ is infinite-dimensional with a countable basis. In this case $\tr$ is the ordinary
matrix trace $\Tr_\HH$, with no renormalization needed, because there is no part of $\HH$ that the algebra
fails to see.

The most important fact tying this back to ordinary quantum mechanics is the following. $\M$ is a type I
factor *emph* there is a Hilbert space factorization $\HH=\HH_R\otimes\HH_L$ with

$$

\M=B(\HH_R)\otimes\id_L, \qquad \tr=\Tr_{\HH_R}, \qquad \M'=\id_R\otimes B(\HH_L) .

$$

This result closes the type classification, and Chapter~3 uses it constantly. Many books state it without
proof. The proof is short enough to give here, and it shows exactly how minimal projections build a tensor
product.

\begin{keyresult}[: Derivation of the Type I Factorization Theorem]
**Theorem:** A von Neumann algebra $\M \subseteq B(\HH)$ is a type I factor if and only if there exists a
unitary isomorphism $U: \HH \xrightarrow{\sim} \HH_R \otimes \HH_L$ such that

$$

U \M U^\dagger = B(\HH_R) \otimes \id_L, \qquad U \M' U^\dagger = \id_R \otimes B(\HH_L) .

$$

**Proof ($\implies$):**

1. **Minimal projection and orthogonal resolution.**
By the definition of type I, $\M$ contains a minimal projection $P \in \M$. Because $P$ is minimal, the
compressed algebra $P\M P$ contains only multiples of $P$:

$$

P \M P = \mathbb{C} P .

$$

(The reason: $P\M P$ is a von Neumann algebra on $P\HH$ whose only projections are $0$ and $P$, and a von
Neumann algebra is generated by its projections.) Since $\M$ is a factor, its center is trivial,
$\mathcal{Z}(\M) \equiv \M \cap \M' = \mathbb{C}\id$. So the central support of $P$ (the smallest central
projection above $P$) is $c(P) = \id$. By the comparison theorem for projections in a factor, any two minimal
projections are Murray—von Neumann equivalent. By Zorn's lemma, we can choose a maximal family
$\{P_i\}_{i \in I}$ of mutually orthogonal minimal projections, each equivalent to $P$. Maximality together
with $c(P)=\id$ implies that their sum is the identity on $\HH$:

$$

\sum_{i \in I} P_i = \id_\HH, \qquad P_i P_j = \delta_{ij} P_i .

$$

2. **Equivalence through partial isometries.**
Fix a base index $0 \in I$ with $P_0 \equiv P$. Since $P_i \sim P$, there are partial isometries $V_i \in \M$
with

$$

V_i^\dagger V_i = P, \qquad V_i V_i^\dagger = P_i \qquad (\text{with } V_0 \equiv P).

$$

So $V_i$ maps the base subspace $P\HH$ isometrically onto the orthogonal subspace $P_i\HH$.
3. **Construction of the unitary $U$.**
Define two Hilbert spaces:

$$

\HH_R \equiv \ell^2(I) \quad \text{with orthonormal basis } \{\ket{i}\}_{i \in I}, \qquad \HH_L \equiv P\HH .

$$

Define the linear map $U: \HH \to \HH_R \otimes \HH_L$ by its action on any vector $\ket\psi \in \HH$:

$$

U \ket\psi \equiv \sum_{i \in I} \ket{i} \otimes \big(V_i^\dagger \ket\psi\big) .

$$

Each $V_i^\dagger \ket\psi = P V_i^\dagger \ket\psi$ lies in $P\HH = \HH_L$, so this is well defined. We check
that $U$ is an isometry:
\begin{align}
\|U\ket\psi\|^2 = \sum_{i \in I} \|V_i^\dagger \ket\psi\|^2
&\eqstep{1} \sum_{i \in I} \braket{\psi | V_i V_i^\dagger | \psi} \notag\\
&\eqstep{2} \sum_{i \in I} \braket{\psi | P_i | \psi}
\ \eqstep{3}\ \Braket{\psi \Big| \sum_{i \in I} P_i \Big| \psi}
\ \eqstep{4}\ \braket{\psi|\psi} . \notag
\end{align}
**(1)** $\|v\|^2=\braket{v|v}$ applied to $v=V_i^\dagger\ket\psi$, using $(V_i^\dagger)^\dagger=V_i$.\quad
**(2)** the partial isometry relation $V_iV_i^\dagger=P_i$ from Step~2 above.\quad
**(3)** linearity of the inner product, pulling the sum through $\braket{\psi|\cdot|\psi}$.\quad
**(4)** the resolution of the identity, $\sum_i P_i=\id_\HH$, established in Step~1.

The adjoint map $U^\dagger: \HH_R \otimes \HH_L \to \HH$ acts on elementary basis tensors as

$$

U^\dagger \big(\ket{i} \otimes \ket{\phi_L}\big) = V_i \ket{\phi_L}, \qquad \ket{\phi_L} \in P\HH .

$$

Computing $U U^\dagger$ on basis vectors:
\begin{align}
U U^\dagger \big(\ket{j} \otimes \ket{\phi_L}\big)
&\eqstep{1} U \big(V_j \ket{\phi_L}\big) \notag\\
&\eqstep{2} \sum_{i \in I} \ket{i} \otimes \big(V_i^\dagger V_j \ket{\phi_L}\big)
\ \eqstep{3}\ \ket{j} \otimes \big(P \ket{\phi_L}\big) = \ket{j} \otimes \ket{\phi_L} . \notag
\end{align}
**(1)** the definition of $U^\dagger$ on the basis tensor $\ket j\otimes\ket{\phi_L}$.\quad
**(2)** the definition of $U$ applied to the vector $V_j\ket{\phi_L}$.\quad
**(3)** $V_i^\dagger V_j = V_i^\dagger P_i P_j V_j = \delta_{ij} P$, so only the $i=j$ term in the sum
survives, and $P\ket{\phi_L}=\ket{\phi_L}$ since $\ket{\phi_L}\in P\HH$.

So $U$ is an isometry with $UU^\dagger=\id$, which means $U$ is unitary.
4. **Action on the algebra $\M$.**
Let $A \in \M$ be any element. Compute $U A U^\dagger$ on $\ket{j} \otimes \ket{\phi_L}$:
\begin{align}
U A U^\dagger \big(\ket{j} \otimes \ket{\phi_L}\big)
&\eqstep{1} U \big(A V_j \ket{\phi_L}\big) \notag\\
&\eqstep{2} \sum_{i \in I} \ket{i} \otimes \big(V_i^\dagger A V_j \ket{\phi_L}\big) . \notag
\end{align}
**(1)** the definition of $U^\dagger$ on basis tensors, then applying $A$.\quad
**(2)** the definition of $U$ applied to the vector $AV_j\ket{\phi_L}$.

The key object is the operator $V_i^\dagger A V_j$. It lies in $P\M P$:

$$

V_i^\dagger A V_j = (P V_i^\dagger) A (V_j P) = P \big(V_i^\dagger A V_j\big) P \in P \M P .

$$

Because $P$ is minimal, $P \M P = \mathbb{C} P$. Therefore $V_i^\dagger A V_j$ is a multiple of $P$:

$$

V_i^\dagger A V_j = a_{ij} P \quad \text{for some number } a_{ij} \in \mathbb{C} .

$$

Acting on $\ket{\phi_L} \in P\HH$, this gives $V_i^\dagger A V_j \ket{\phi_L} = a_{ij} \ket{\phi_L}$. Thus
\begin{align}
U A U^\dagger \big(\ket{j} \otimes \ket{\phi_L}\big)
&\eqstep{1} \sum_{i \in I} a_{ij} \ket{i} \otimes \ket{\phi_L} \notag\\
&\eqstep{2} \Big(\sum_{i,k \in I} a_{ik} \ket{i}\bra{k} \otimes \id_L \Big) \big(\ket{j} \otimes \ket{\phi_L}\big) . \notag
\end{align}
**(1)** $V_i^\dagger AV_j\ket{\phi_L}=a_{ij}\ket{\phi_L}$, just shown.\quad
**(2)** $\braket{k|j}=\delta_{kj}$ picks out exactly the $k=j$ column of the matrix $(a_{ik})$.

So every operator in $\M$ acts trivially on $\HH_L$ and as a matrix on $\HH_R$. Conversely, every rank-one
operator $\ket{i}\bra{j}\otimes\id_L$ comes from an element of $\M$: a computation like the one above gives
$U V_i V_j^\dagger U^\dagger = \ket{i}\bra{j}\otimes\id_L$, and $V_iV_j^\dagger\in\M$. Linear combinations of
these operators are weakly dense in $B(\HH_R)\otimes\id_L$, and $\M$ is weakly closed. Thus
$U \M U^\dagger = B(\HH_R) \otimes \id_L$.
5. **The commutant and the trace.**
Conjugating by the unitary $U$ and using the previous step:
\begin{align}
U \M' U^\dagger
&\eqstep{1} (U \M U^\dagger)' \notag\\
&\eqstep{2} \big(B(\HH_R) \otimes \id_L\big)'
\ \eqstep{3}\ \id_R \otimes B(\HH_L) . \notag
\end{align}
**(1)** $B$ commutes with every element of $\M$ exactly when $UBU^\dagger$ commutes with every element of
$U\M U^\dagger$, since $U^\dagger U=\id$.\quad
**(2)** $U\M U^\dagger=B(\HH_R)\otimes\id_L$ from Step~4.\quad
**(3)** the commutant of "all operators on one tensor factor" is "all operators on the other," as
in the first double-commutant example earlier in this chapter.

The trace $\tr$ on $\M$, normalized so that minimal projections have trace $1$, corresponds under $U$ to the
standard trace $\Tr_{\HH_R}$ on $B(\HH_R)$.
6. **Proof ($\impliedby$).**
Suppose $\M \cong B(\HH_R) \otimes \id_L$. Its center is $\mathbb C\id$ (as in the first double-commutant
example), so $\M$ is a factor. Take any one-dimensional projection $p = \ket{i}\bra{i}$ on $\HH_R$. Then
$P = p \otimes \id_L \in \M$. For any $A = a \otimes \id_L \in \M$:
\begin{align}
P A P
&\eqstep{1} (p a p) \otimes \id_L \notag\\
&\eqstep{2} \braket{i|a|i}\, (p \otimes \id_L)
\ \eqstep{3}\ \braket{i|a|i}\, P \ \in\ \mathbb{C} P . \notag
\end{align}
**(1)** multiplying tensor products factor by factor, with $\id_L^3=\id_L$.\quad
**(2)** $pap=\ket i\braket{i|a|i}\bra i=\braket{i|a|i}\,p$.\quad
**(3)** the definition $P=p\otimes\id_L$.

So every projection in $\M$ below $P$ is a multiple of $P$, hence $0$ or $P$. This means $P$ is minimal in
$\M$, and $\M$ is a type I factor. $\blacksquare$

\end{keyresult}

So the statement "the algebra describing this subsystem is type I" is the precise, general form of the
statement "the ordinary tensor-product picture of textbooks such as Griffiths and Sakurai applies here."
Every worked example given so far in this chapter, including the two-qubit examples above, is type I by
construction. Types II and III, described next, are what becomes possible when this is no longer true.
- **Type II: $\M$ has finite projections but no minimal ones.** This is a genuinely new possibility,
and it sounds strange at first. The finite/infinite distinction still works, and finite projections can be
compared in size using $d$. But there is no smallest nonzero size: below any nonzero projection there is
always a strictly smaller nonzero one. The values of $d$ are then forced to fill out a continuous range. Here
is the idea. In a type II factor, any finite projection $P$ can be split into two orthogonal pieces that are
equivalent to each other, $P=P_1+P_2$ with $P_1\sim P_2$ (stated without proof). Additivity then gives
$d(P_1)=d(P_2)=\tfrac12d(P)$. Repeating the split gives projections with $d=2^{-k}d(P)$ for every $k$, so $d$
takes arbitrarily small positive values. Adding such pieces gives every dyadic fraction of $d(P)$, and one can
show that every value in between is reached as well. So a von Neumann algebra can assign a *emph*, not only an integer, as the "dimension" of a subspace. Nothing like this happens in ordinary
finite-dimensional linear algebra, where dimension is a whole number obtained by counting basis vectors.
There are two subtypes, depending on whether $d(\id)$ is finite. In type $\mathrm{II}_1$ the identity has
finite dimension. We normalize $d(\id)=\tr(\id)=1$, so that $d(P)\in(0,1]$ for every nonzero projection: the
trace is normalized exactly like a probability. In type $\mathrm{II}_\infty$ we have $d(\id)=\infty$, so
$d(P)\in(0,\infty]$, and there is no natural normalization. Chapter~3 constructs a type $\mathrm{II}_1$ factor
by hand, from the $N\to\infty$ Bell-pair chain of Chapter~1. There, "real-valued dimension" stops being
abstract and can be watched in a specific family of projections.
- **Type III: every nonzero projection is infinite.** This is the most extreme case. The
finite/infinite distinction has no content, because no projection except zero is finite. Formally,
$d(P)=\infty$ for every nonzero $P$. So there is no useful dimension function, and hence no (normal,
semifinite) trace on $\M$ at all. This looks like a mathematical dead end. How could one talk about
entanglement in an algebra with no density matrix, when density matrices are defined using a trace?
Chapter~4 meets exactly this obstacle and overcomes it with a different tool, Tomita—Takesaki modular
theory; that chapter is the technical heart of the notes. Type III is also the type that is physically
generic. The algebras of local regions in relativistic quantum field theory, and the boundary subalgebras of
holography in the strict large-$N$ limit, are both type III (in fact type $\mathrm{III}_1$, as later chapters
explain). This is not an exotic corner case. It is the everyday situation once you leave the world of
finitely many qubits.


Types II and III can sound, on first exposure, like unphysical mathematical curiosities. They are not. The
entangled spin chain of Chapter~1 already produces both, explicitly and by direct construction, and
Chapter~3 works through that construction completely.

## "Emergent" Hilbert space and von Neumann algebra: the GNS construction

### Why this construction is needed

Here is the gap again, now that every piece needed to close it is in hand. The completeness condition of a
von Neumann algebra (weak convergence) is stated in terms of matrix elements $\braket{\xi|A_n|\eta}$, so it
assumes that a Hilbert space already exists. The completeness condition of a $C^*$-algebra (norm
convergence) does not. It needs only an abstract norm with $\|A^\dagger A\|=\|A\|^2$. So you can specify a
$C^*$-algebra $\Alg$ abstractly, with no Hilbert space anywhere. Suppose you are also given a state $\omega$
on $\Alg$, in the sense defined earlier in this chapter: a positive, normalized linear functional, which needs
nothing beyond the algebra itself to define. Can a Hilbert space be *emph*, rather than assumed, in
which $\omega$ is represented by an ordinary vector? The Gelfand—Naimark—Segal (GNS) construction says yes,
always. It does so by an explicit, mechanical recipe.

### The construction, built up in stages

**Stage 1: treat algebra elements as candidate vectors.** This is the conceptual leap, so here it is in
words before the formulas. An element $C\in\Alg$ is reinterpreted as standing for ``the state you would get
by applying the operation $C$ to a fixed reference configuration.'' Two elements $C_1,C_2$ should count as
the *emph* state if no measurement, computed with $\omega$, could ever tell them apart.

**Stage 2: use $\omega$ to build an inner product on $\Alg$ itself.** For any $A,B\in\Alg$, define

$$

\braket{A|B} \equiv \omega(A^\dagger B) .

$$

Check that this deserves to be called an inner product. It is positive, $\braket{A|A}=\omega(A^\dagger A)\ge0$,
directly from the positivity of $\omega$. And it has the correct conjugate symmetry:
\begin{align}
\braket{B|A}=\omega(B^\dagger A)
&\eqstep{1} \omega\big((A^\dagger B)^\dagger\big) \notag\\
&\eqstep{2} \omega(A^\dagger B)^*
\ \eqstep{3}\ \braket{A|B}^* . \notag
\end{align}
**(1)** $(A^\dagger B)^\dagger=B^\dagger A$.\quad
**(2)** $\omega(X^\dagger)=\omega(X)^*$, which holds for every positive functional (see the definitions
of weights and states).\quad
**(3)** the definition $\braket{A|B}\equiv\omega(A^\dagger B)$.

Both required properties hold, using nothing but the definition of $\omega$.

**Stage 3: handle "zero-length" elements.** There may be nonzero $X\in\Alg$ with
$\omega(X^\dagger X)=0$. These are algebra elements that $\omega$ cannot see at all. Call the set of all such
$X$ the null space $\mathcal J$. The Cauchy—Schwarz inequality~\eqref{eq:CS-omega} shows that $\mathcal J$
is a linear subspace. A short computation shows more: if $X\in\mathcal J$ and $A\in\Alg$ is any element, then
$AX\in\mathcal J$ too. The proof is again an application of the Cauchy—Schwarz inequality:
\begin{align}
0 \ \le\ \omega\big((AX)^\dagger(AX)\big)
&\eqstep{1} \omega(X^\dagger A^\dagger AX) \notag \\
&\leqstep{2} \omega(X^\dagger X)^{1/2}\,\omega\big((A^\dagger AX)^\dagger A^\dagger AX\big)^{1/2}
\ \eqstep{3}\ 0 . \notag
\end{align}
**(1)** regroup $(AX)^\dagger(AX)=X^\dagger A^\dagger AX$.\quad
**(2)** the Cauchy—Schwarz inequality for states,
$|\omega(A^\dagger B)|^2\le\omega(A^\dagger A)\,\omega(B^\dagger B)$, with $A$ replaced by $X$ and $B$
replaced by $A^\dagger AX$. This is the only inequality in the chain.\quad
**(3)** $\omega(X^\dagger X)=0$ because $X\in\mathcal J$, so the upper bound is exactly $0$ whatever the
second factor is.

So $\omega\big((AX)^\dagger(AX)\big)=0$, which means $AX\in\mathcal J$. In the language of algebra,
$\mathcal J$ is a *emph*. This computation does real work. It guarantees that quotienting out the
null elements in Stage~4 is consistent: multiplying by $A$ never turns a zero-length vector into a vector of
nonzero length.

**Stage 4: quotient and complete.** Declare $A$ and $A+X$ equivalent whenever $X\in\mathcal J$: algebra
elements that differ only by something $\omega$ cannot see count as the same vector. Let $[A]$ denote the
equivalence class of $A$. The inner product of Stage~2 does not depend on the choice of representative,
because $|\omega(X^\dagger B)|^2\le\omega(X^\dagger X)\,\omega(B^\dagger B)=0$ for $X\in\mathcal J$. On the
quotient space $\Alg/\mathcal J$ the inner product is positive definite: by construction, no nonzero vector
has zero length. Completing this space, by filling in the limits of Cauchy sequences just as the rational
numbers are completed to the real numbers, gives a Hilbert space, called $\HH_\omega$.

**Stage 5: define the representation.** The algebra acts on $\HH_\omega$ by left multiplication:

$$

\pi_\omega(A)\ket{[C]} \equiv \ket{[AC]} .

$$

This is well defined. If $C$ is replaced by $C+X$ with $X\in\mathcal J$, then $AC$ changes by $AX$, which is
also in $\mathcal J$ by Stage~3. It respects the multiplication of the algebra,
$\pi_\omega(A)\pi_\omega(B)=\pi_\omega(AB)$. Indeed, applying $\pi_\omega(B)$ and then $\pi_\omega(A)$ to $[C]$
gives $[A(BC)]=[(AB)C]$, which is $\pi_\omega(AB)$ applied to $[C]$. For a $C^*$-algebra, one also has
$\|\pi_\omega(A)[C]\|\le\|A\|\,\|[C]\|$, so each $\pi_\omega(A)$ is bounded and extends to the completion
$\HH_\omega$.

**Stage 6: identify the special vector.** The equivalence class of the identity element, $[\id]$, gets
its own name, $\ket\Omega\equiv\ket{[\id]}$. Two facts follow at once from the definitions above:

$$

\pi_\omega(A)\ket\Omega = \ket{[A\cdot\id]} = \ket{[A]}, \qquad\qquad
\omega(A) = \braket{\Omega|\pi_\omega(A)|\Omega} .

$$

The second follows from the first together with the definition of the inner product:
$\braket{\Omega|\pi_\omega(A)|\Omega} = \braket{[\id]|[A]} = \omega(\id^\dagger A)=\omega(A)$. So in the Hilbert
space just built, the vector $\ket\Omega$ reproduces the abstract state $\omega$ exactly, through the ordinary
formula $\braket{\Omega|A|\Omega}$ from undergraduate quantum mechanics. This is the purpose of the
construction. You gave it an abstract algebra and a number-valued rule $\omega$. It gave back a Hilbert space
and a vector inside it, and the usual formula for expectation values holds by construction, not by
assumption.


> [!NOTE] **Physics Connection: Origin of the Vacuum $\ket0$**
> $\ket\Omega$ is not found somewhere outside this construction. It *emph* the identity element of the
> algebra, $\id\in\Alg$, renamed once the inner product has been put on $\Alg$ in Stage~2. A vector and the
> Hilbert space it lives in are made in the same step, from the same two ingredients, $\Alg$ and $\omega$.
> Neither exists before the other.
> 
> The construction also explains why $a$ annihilates $\ket\Omega$ for the oscillator ground state, without
> using $\ket0$ as an input to define $\omega$. Start from one algebraic condition, $\omega(a^\dagger a)=0$,
> together with positivity, $\omega(A^\dagger A)\ge0$ for every $A\in\Alg$, and normalization,
> $\omega(\id)=1$. For any element $Y$, the Cauchy—Schwarz inequality~\eqref{eq:CS-omega} gives
> $|\omega(Ya)|^2\le\omega(YY^\dagger)\,\omega(a^\dagger a)=0$. So $\omega(Ya)=0$ for every $Y$, and taking
> adjoints, $\omega(a^\dagger Y)=\omega(Y^\dagger a)^*=0$ as well. In particular $\omega(a)=\omega(a^\dagger)=0$.
> Using $[a,a^\dagger]=1$, every monomial in $a$ and $a^\dagger$ can be rewritten as a combination of
> normal-ordered monomials $(a^\dagger)^ma^n$. Those with $m+n>0$ either end in $a$ or begin with $a^\dagger$,
> so $\omega$ gives them zero. Only the constant term survives, and $\omega(\id)=1$ fixes its value. So the one
> condition $\omega(a^\dagger a)=0$ determines $\omega$ completely. The oscillator box below uses the same
> bookkeeping to show $\braket{0|a^n(a^\dagger)^n|0}=n!$. Here it is read as *emph* $\omega$ from the
> multiplication table of the algebra, not as evaluating a bra-ket that already existed.
> 
> Now apply Stage~3 to this $\omega$. The null ideal is $\mathcal J=\{X:\omega(X^\dagger X)=0\}$, and
> $a\in\mathcal J$, because $\omega(a^\dagger a)=0$. Stage~4 quotients by exactly this $\mathcal J$, so every
> element of $\mathcal J$ becomes the zero vector. So $[a]=0$, and $\pi_\omega(a)\ket\Omega=\ket{[a]}=0$. The
> vacuum being annihilated by $a$ is not a separate fact about the world that $\omega$ happened to match. It is
> what $[a]=0$ means, once $\mathcal J$ is fixed by the one number $\omega(a^\dagger a)$.
> 
> This is the general answer to where the vacuum and its Hilbert space come from. The vector space is not
> searched for among candidates that already reproduce $\omega$. It *emph* $\Alg/\mathcal J$, completed. Its
> points are exactly as fine as $\omega$ can distinguish, and no finer: two algebra elements become the same
> vector exactly when $\omega$ assigns their difference zero length. Quotienting throws out the redundancy.
> Completing, by filling in the limits of Cauchy sequences, turns this inner-product space into a Hilbert space
> in the sense of Chapter~1.
> 
> In a field theory, $\omega$ is fixed in the same way, only more concretely, by a Euclidean path integral:
> 
$$

> \omega\big(O(x_1)\cdots O(x_n)\big) = \frac1Z\int\mathcal D\phi\;O(x_1)\cdots O(x_n)\,e^{-S[\phi]} .
> 
$$

> This formula computes every Euclidean correlator directly (Lorentzian correlators follow by analytic
> continuation), and no Hilbert space, vector, or bra-ket appears in it. The CFT vacuum of Chapter~6 and the
> JT-gravity states $\ket\beta$ of Chapter~9 are both defined this way. Canonical quantization, with its $\ket0$
> and its Fock space, is the GNS representation built afterward from these correlators. Chapter~10 applies the
> same idea to string theory. There, different asymptotic vacua are proposed to be different states $\omega$ on
> one shared, background-independent algebra $\Alg_{\text{IIB}}$. Each has its own path-integral (or
> correlator) definition that needs no Hilbert space. Each one's "$\ket0$" is simply $[\id]$ inside the GNS
> space of *emph* $\omega$. It is never a single object shared across backgrounds. This is why
> the resulting Hilbert spaces can be mutually inequivalent.


The set $\{\pi_\omega(A)\ket\Omega : A\in\Alg\}$ is dense in $\HH_\omega$. This is automatic, because
$\HH_\omega$ was built as the completion of the set of classes $[A]=\pi_\omega(A)\ket\Omega$, so every vector
in $\HH_\omega$ can be approximated arbitrarily well by some $\pi_\omega(A)\ket\Omega$. A vector with this
property is called **cyclic**: every state can be reached from $\ket\Omega$ using only the algebra. This
is the same structure as the familiar construction of the harmonic-oscillator Hilbert space, by acting
repeatedly on the vacuum $\ket0$ with creation operators. The only difference is that here it is a theorem,
derived from the algebra and the state, rather than a separate postulate about how the Hilbert space is
built.


> [!NOTE] **Physics Connection: GNS and Oscillator Fock Space**
> The oscillator shows that GNS is the same calculation as the Fock-space construction you already know, run
> in the opposite direction. We compute the same quantities in two ways and compare the answers.
> 
> **The ordinary way.** Start with a Hilbert space spanned by orthonormal vectors
> $\ket0,\ket1,\ket2,\dots$, and define two operators by $a^\dagger\ket n=\sqrt{n+1}\,\ket{n+1}$ and
> $a\ket n=\sqrt n\,\ket{n-1}$. Then $[a,a^\dagger]=1$, $a\ket0=0$, and $(a^\dagger)^m\ket0=\sqrt{m!}\,\ket m$.
> Consequently
> 
$$

> \braket{0|a^n(a^\dagger)^m|0}=\sqrt{n!\,m!}\,\braket{n|m}=n!\,\delta_{nm} .
> 
$$

> Here the Hilbert space comes first, and the operators are defined on it.
> 
> **The GNS way.** Now forget the Hilbert space. Let $\Alg$ be the $*$-algebra generated by $1,a,a^\dagger$
> with only the relation $[a,a^\dagger]=1$. Its elements are polynomials in $a$ and $a^\dagger$. Let $\omega$
> be the state fixed by the single condition $\omega(a^\dagger a)=0$, as in the previous box. Since $a$ and
> $a^\dagger$ are unbounded, $\Alg$ is a $*$-algebra but not a $C^*$-algebra. The GNS steps still go through,
> with $\pi_\omega(a)$ and $\pi_\omega(a^\dagger)$ defined on the dense subspace of finite combinations of the
> classes $[(a^\dagger)^n]$. Follow the recipe.
> 
> The Stage~2 inner product on $\Alg$ is $\braket{(a^\dagger)^n\,|\,(a^\dagger)^m}\equiv
> \omega\big(a^n(a^\dagger)^m\big)$. First, it vanishes for $n\ne m$. Write $N=a^\dagger a$. The previous box
> showed $\omega(a^\dagger Y)=0$ and $\omega(Ya)=0$ for every $Y$, so $\omega(NX)=\omega(XN)=0$ for every $X$.
> Also $[N,a^n(a^\dagger)^m]=(m-n)\,a^n(a^\dagger)^m$, because $[N,a]=-a$ and $[N,a^\dagger]=a^\dagger$. Hence
> 
$$

> (m-n)\,\omega\big(a^n(a^\dagger)^m\big)=\omega(Na^n(a^\dagger)^m)-\omega(a^n(a^\dagger)^mN)=0 ,
> 
$$

> so $\omega\big(a^n(a^\dagger)^m\big)=0$ unless $n=m$. For $n=m$, write $\omega(X)$ as $\braket{0|X|0}$, as the
> ordinary way would; the computation uses only the algebra and $\omega(Ya)=0$. It is one recursive step:
> \begin{align}
> \braket{0|a^n(a^\dagger)^n|0}
> &\eqstep{1} \braket{0|a^{n-1}\big[a,(a^\dagger)^n\big]|0} + \braket{0|a^{n-1}(a^\dagger)^na|0} \notag\\
> &\eqstep{2} n\,\braket{0|a^{n-1}(a^\dagger)^{n-1}|0} + 0 . \notag
> \end{align}
> **(1)** split $a\,(a^\dagger)^n=[a,(a^\dagger)^n]+(a^\dagger)^n a$ and distribute.\quad
> **(2)** the oscillator identity $[a,(a^\dagger)^n]=n(a^\dagger)^{n-1}$; the second term has the form
> $\omega(Ya)$, which is zero.
> 
> This is a recursion, $\braket{0|a^n(a^\dagger)^n|0}=n\,\braket{0|a^{n-1}(a^\dagger)^{n-1}|0}$, with base case
> $\omega(\id)=1$ at $n=0$. Its solution is $n!$. (For example, $n=1$ gives $1\cdot1=1=1!$ and $n=2$ gives
> $2\cdot1=2=2!$.) So the classes $[(a^\dagger)^n]$ are orthogonal, with squared norm $n!$. Normalizing gives
> $\ket n\equiv[(a^\dagger)^n]/\sqrt{n!}$. The representation acts by $\pi_\omega(a^\dagger)[(a^\dagger)^n]=
> [(a^\dagger)^{n+1}]$, which after normalization is $\pi_\omega(a^\dagger)\ket n=\sqrt{n+1}\,\ket{n+1}$. Also
> $\pi_\omega(a)[(a^\dagger)^n]=[a(a^\dagger)^n]=n\,[(a^\dagger)^{n-1}]$ (System~3 of the next box shows this),
> which after normalization is $\pi_\omega(a)\ket n=\sqrt n\,\ket{n-1}$. The cyclic vector $\ket\Omega=[\id]$ is
> $\ket0$, and $\pi_\omega(a)\ket\Omega=[a]=0$.
> 
> **Comparison.** The two computations give the same answers:
> 
> \small
> \begin{tabular}{@{}lll@{}}
> \toprule
> & The ordinary way & The GNS way \\
> \midrule
> Inner products & $\braket{0|a^n(a^\dagger)^m|0}=n!\,\delta_{nm}$ & $\omega\big(a^n(a^\dagger)^m\big)=n!\,\delta_{nm}$ \\
> Basis & $\ket n=(a^\dagger)^n\ket0/\sqrt{n!}$ & $\ket n=[(a^\dagger)^n]/\sqrt{n!}$ \\
> Raising & $a^\dagger\ket n=\sqrt{n+1}\,\ket{n+1}$ & $\pi_\omega(a^\dagger)\ket n=\sqrt{n+1}\,\ket{n+1}$ \\
> Lowering & $a\ket n=\sqrt n\,\ket{n-1}$ & $\pi_\omega(a)\ket n=\sqrt n\,\ket{n-1}$ \\
> Ground state & $a\ket0=0$ & $\pi_\omega(a)\ket\Omega=[a]=0$ \\
> \bottomrule
> \end{tabular}
> 
> The map $\ket n\mapsto[(a^\dagger)^n]/\sqrt{n!}$ is a unitary between the two Hilbert spaces, and it carries
> $a$ and $a^\dagger$ of the ordinary way to $\pi_\omega(a)$ and $\pi_\omega(a^\dagger)$. So the two routes give
> the same Hilbert space, the same basis, the same matrix elements, and the same ground state. These are exact
> equalities, not approximations.
> 
> Nothing here is new physics. It is the Fock-space construction from a first course on the harmonic
> oscillator, run backward. What differs is only the direction of the logic. In the ordinary way you are handed
> $\HH=L^2(\mathbb R)$ (or an abstract countable basis) first, and $a,a^\dagger$ are defined as operators on
> it. In the GNS way the only inputs are the relation $[a,a^\dagger]=1$ and the state $\omega$ (equivalently,
> "the vacuum is annihilated by $a$"). The whole Fock space, every $\ket n$ and every matrix element, is an
> output. This is the sense in which the section on weights and states called the Hilbert space derived rather
> than fundamental. For the oscillator nothing about the physics changes, because this $\omega$ produces the
> usual Fock space. (For one degree of freedom this is no accident: by the Stone—von Neumann theorem, the
> usual representation is, up to unitary equivalence, the only well-behaved irreducible one.) The cases that matter later
> are those in which a different state produces an *emph* Hilbert space from the same
> algebra. Examples are the $N$-Bell-pair chain, treated at the end of this chapter and in Chapters~3 and~4,
> and the different asymptotic vacua of quantum gravity in Chapter~10.


\begin{workedexamplebox}[: Concrete GNS Construction for Three Physical Systems]
To make the six-stage recipe fully mechanical, we now build the GNS Hilbert space, inner product, null ideal,
representation, and cyclic vector explicitly for three basic physical systems. In each case we also compare
the result with the answer ordinary quantum mechanics gives.


1. **System 1: a pure state of a single qubit ($\Alg = M_2(\mathbb{C**)$).}



9. **System 2: a mixed (thermal) state on $M_2(\mathbb{C**)$, and the thermofield double.}



16. **System 3: the bosonic oscillator (canonical commutation relation) and Fock space.**




\end{workedexamplebox}

Finally, the von Neumann algebra associated with all of this is the double commutant of the
representation,
\begin{equation}
\M\equiv\pi_\omega(\Alg)'' .
\label{eq:GNS-vN}
\end{equation}
This uses the double-commutant machinery from earlier in this chapter to promote the $C^*$-algebra
$\pi_\omega(\Alg)$, which is norm-closed but not necessarily weakly closed, to the von Neumann algebra it
generates.

### Two structural facts, and what they mean

The GNS triple $(\HH_\omega,\pi_\omega,\ket\Omega)$ is unique up to unitary equivalence. Any two
constructions that start from the same $\omega$ give the "same" Hilbert space, possibly described in a
different basis. We state this without proof. It is reassuring, because it means the construction does not
depend on any arbitrary choice made along the way.

Two further properties of $\omega$ translate directly into properties of the representation it produces:


- $\pi_\omega$ is **irreducible** if and only if $\omega$ is a **pure** state. Irreducible
means $\pi_\omega(\Alg)''=B(\HH_\omega)$: the representation generates *emph* bounded operator on
$\HH_\omega$, leaving nothing outside its reach.
- If $\omega$ is **faithful**, then $\ket\Omega$ is **separating** for $\pi_\omega(\Alg)$.
Separating means that $\pi_\omega(A)\ket\Omega=0$ forces $\pi_\omega(A)=0$: no nonzero operator in the algebra
annihilates the reference vector. (Indeed, $\pi_\omega(A)\ket\Omega=[A]=0$ means $\omega(A^\dagger A)=0$, so
$A=0$.) Conversely, if $\ket\Omega$ is separating, then $\omega$ is faithful on the represented algebra
$\pi_\omega(\Alg)$.


The combination *emph* deserves attention now, although its full importance appears
only in Chapter~4. Cyclic says that the algebra reaches every vector, starting from $\ket\Omega$. Separating
says that different elements of the algebra act differently on $\ket\Omega$, so nothing nonzero is wasted.
The two notions are linked: a vector is cyclic for $\M$ if and only if it is separating for $\M'$ (a standard
fact). So a vector that is cyclic and separating for $\M$ is also cyclic and separating for $\M'$. In the
finite-dimensional examples of this chapter, this happens exactly when $\ket\Omega$ is entangled between the
two tensor factors with full Schmidt rank on both sides. This property is the foundation of Tomita—Takesaki
modular theory, the subject of Chapter~4.

### The worked example, done completely with numbers

We now work one standard example all the way through with numbers, rather than leaving it symbolic. It is
the most important computation in this chapter to see in full.

Let $\Alg=M_3(\mathbb C)$, the algebra of all $3\times3$ complex matrices, and take

$$

\rho = \begin{pmatrix}0.6&0&0\\0&0.4&0\\0&0&0\end{pmatrix} , \qquad \omega(A)\equiv\Tr(\rho A).

$$

First check that $\omega$ is a state in the sense defined earlier. It is linear, because the trace and matrix
multiplication are linear. It is positive: since $\rho$ is diagonal,
$\Tr(\rho A^\dagger A)=\sum_j\rho_{jj}(A^\dagger A)_{jj}=\sum_j\rho_{jj}\sum_k|A_{kj}|^2\ge0$. It is normalized:
$\Tr(\rho\,\id_3)=\Tr\rho=0.6+0.4+0=1$. The matrix $\rho$ has rank $2$, not $3$. It ignores the third basis
direction completely, so $\omega$ is *emph* faithful. For example, $e_{33}\ne0$ but
$\omega(e_{33}^\dagger e_{33})=\rho_{33}=0$. This property will show up directly in the construction.

Now follow the recipe, exactly as for System~2 above. The GNS inner product is
\begin{align}
\braket{A|B} = \Tr(\rho A^\dagger B)
&\eqstep{1} \sum_{j=1}^3 \rho_{jj}\,(A^\dagger B)_{jj} \notag\\
&\eqstep{2} 0.6\sum_{k=1}^3 A_{k1}^*B_{k1} + 0.4\sum_{k=1}^3 A_{k2}^*B_{k2} . \notag
\end{align}
**(1)** $\rho$ is diagonal.\quad
**(2)** $(A^\dagger B)_{jj}=\sum_k A_{kj}^*B_{kj}$, and $\rho_{33}=0$ removes the $j=3$ term.

So only the first two columns of a matrix matter. The null space $\mathcal J$ consists of the matrices whose
first two columns vanish, with the third column arbitrary. It is 3-dimensional, so the quotient
$\Alg/\mathcal J$ has dimension $9-3=6$. An orthonormal basis is
$\ket k_R\ket j_L\equiv[e_{kj}]/\sqrt{\rho_{jj}}$, for $k=1,2,3$ and $j=1,2$. Left multiplication,
$[Ae_{kj}]=\sum_lA_{lk}[e_{lj}]$, acts only on the row label $k$, so $\pi_\omega(A)=A\otimes\id_2$. The cyclic
vector is $[\id_3]=[e_{11}]+[e_{22}]+[e_{33}]=[e_{11}]+[e_{22}]$, since $e_{33}\in\mathcal J$. Altogether,
$\HH_\omega\cong\mathbb C^3\otimes\mathbb C^2$ is 6-dimensional: $3$ (the size of the matrices) times $2$ (the
rank of $\rho$). The cyclic vector and the representation are

$$

\ket\Omega=\sqrt{0.6}\,\ket1_R\ket1_L+\sqrt{0.4}\,\ket2_R\ket2_L ,
\qquad
\pi_\omega(A)=A\otimes\id_2 .

$$

We also checked this numerically. For several random complex $3\times3$ matrices $A,B$, we compared
$\omega(A)=\Tr(\rho A)$ with $\braket{\Omega|\pi_\omega(A)|\Omega}$, and the GNS inner product
$\braket{A|B}=\Tr(\rho A^\dagger B)$ with $\braket{\Omega|\pi_\omega(A)^\dagger\pi_\omega(B)|\Omega}$. In every
trial the two sides agreed to about one part in $10^{16}$, the rounding error of ordinary double-precision
arithmetic. The failure of faithfulness is also visible: $\pi_\omega(e_{13})\ket\Omega=0$ although
$e_{13}\ne0$. So $\ket\Omega$ is cyclic but not separating, as the second structural fact leads us to expect.

Recognize what this is. $\ket\Omega$ is the **purification** of $\rho$, familiar from quantum
information. Purification is the standard way to write a mixed state $\rho$ on a small Hilbert space as a
pure state on a larger one, by introducing an auxiliary system (here the $L$ factor) entangled with the
original. The GNS construction produces this purification automatically, with no separate step of ``now
introduce an auxiliary system.'' The auxiliary factor $\HH_L$ appears inside $\Alg/\mathcal J$ as the column
label of the matrix $[A]$. Its dimension is the rank of $\rho$, because $\mathcal J$ removes exactly the
columns on which $\rho$ vanishes.

Two variations of the same example show the two structural facts at work, on numbers you can check directly:

- Take $\rho=\mathrm{diag}(1,0,0)$ instead, which has rank $1$ and is a pure state. Then $\HH_\omega$
reduces to a single copy of $\mathbb C^3$: the $L$ factor becomes 1-dimensional and drops out. The
representation $\pi_\omega$ is irreducible, consistent with the first structural fact, since $\omega$ is now
pure.
- Take $\rho=\tfrac13\id_3$ instead, which has full rank $3$ and is maximally mixed. Then
$\HH_\omega=\mathbb C^3\otimes\mathbb C^3$, and $\ket\Omega=\tfrac1{\sqrt3}\sum_{a=1}^3\ket a_R\ket a_L$ is both
cyclic *emph* separating. This is consistent with the second structural fact, since this $\omega$ is
faithful: $\omega(A^\dagger A)=\tfrac13\Tr(A^\dagger A)>0$ for every nonzero $A$. This maximally mixed state, with
its maximally entangled reference vector, is the $3$-dimensional analogue of the Bell pair at $\theta=\pi/4$
from Chapter~1. It is the same structure, one size larger.


## Emergent von Neumann algebras of the entangled spin example

This closing section does one thing. It takes the GNS machinery just built and applies it explicitly to the
$N\to\infty$ Bell-pair chain of Chapter~1. This turns the informal description given there (``the
finite-energy excitations form some Hilbert space $\HH_{\Phi_\theta}$'') into an actual construction, with an
actual algebra and an actual state.

Define the algebra of **finite-energy operations**, $\Alg$. It is generated by operators of the form

$$

O = \alpha_1\otimes\alpha_2\otimes\cdots\otimes\alpha_n\otimes\cdots ,
\qquad \text{all but finitely many of the } \alpha_i \text{ equal to } \id_2\otimes\id_2 .

$$

So $O$ acts on only finitely many of the infinitely many spin pairs, and does nothing (the identity) to every
pair beyond some finite point. This restriction is not arbitrary. It is the algebraic form of the statement
that $O$ corresponds to a process reachable with finite energy. Recall from Chapter~1 that flipping
infinitely many spins costs infinite energy. An operator that acts nontrivially on infinitely many pairs at
once is exactly what a finite-energy process could never do. In the $N\to\infty$ limit, $O$ inherits a
well-defined norm from the finite-$N$ operators it is built from. Completing $\Alg$ in that norm makes it a
$C^*$-algebra. It is defined abstractly, with no particular Hilbert space singled out yet.

The reference state $\ket{\Phi_\theta}$, the infinite chain of Bell-like pairs from Chapter~1, defines a state
$\omega_\theta$ on this algebra in the obvious way:

$$

\omega_\theta(O) = \braket{\Phi_\theta|O|\Phi_\theta} .

$$

This makes sense because $O$ touches only finitely many pairs, so the expectation value uses only finitely
much of the state. No infinite sum or ill-defined limit is hidden in this definition.

Now apply the GNS construction of the previous section, exactly as given, to $(\Alg,\omega_\theta)$. It
produces a Hilbert space $\HH_{\Phi_\theta}$. This *emph* the space of finite-energy excitations described
informally in Chapter~1, now obtained as a mathematical construction rather than a descriptive placeholder.
Heuristically, and this is Stage~1 of the GNS recipe applied to this case, $\HH_{\Phi_\theta}$ is the completion
of the set of states reachable from $\ket{\Phi_\theta}$ by flipping a finite number of spins. That was
exactly the informal description in Chapter~1. In this representation, the von Neumann algebra you get
(the double commutant~\eqref{eq:GNS-vN}) is all of $B(\HH_{\Phi_\theta})$, every bounded operator on this
emergent Hilbert space. The reason is the first structural fact: $\ket{\Phi_\theta}$ is a pure state of the
whole chain, so the representation is irreducible.

Now suppose, as in Chapter~1, that you have access only to the $R$-half of the spin system. Let $\M_R$ be the
subalgebra of $B(\HH_{\Phi_\theta})$ consisting of operators that act only on the $R$-spins, completed under
weak convergence *emph* $\HH_{\Phi_\theta}$. It is a von Neumann algebra. Its
*emph* (I, II, or III, depending on $\theta$) is the subject of Chapters~3 and~4. Define $\M_L$ in the
same way for the $L$-spins. Operations on the $L$-spins commute with operations on the $R$-spins, because they
act on physically distinct degrees of freedom. This shows directly that $\M_L\subseteq\M_R'$. In fact the two
are equal, $\M_L=\M_R'$. This equality is a theorem about infinite tensor products of this kind, which we
state without proof. So the $L$-algebra is exactly the commutant of the $R$-algebra. This is the
"complement of a subsystem" picture from the start of this chapter, now realized concretely.

One further point removes an apparent asymmetry. This example is completely symmetric between $R$ and $L$:
nothing distinguishes them, and the construction could equally well have started from $\M_L$. It turns out
that the same Hilbert space $\HH_{\Phi_\theta}$ can be rebuilt using *emph* the $R$-algebra, with no
reference to $L$ at all. Concretely, redo the GNS construction using $\Alg_R$ (finite-energy operations on
the $R$-spins only) and the state $\omega_\theta(A)=\braket{\Phi_\theta|A|\Phi_\theta}$ restricted to
$A\in\Alg_R$. This restricted $\omega_\theta$ is a *emph* state of $\Alg_R$, because each pair's
reduced density matrix, $\mathrm{diag}(\cos^2\theta,\sin^2\theta)$, has full rank for $\theta\in(0,\pi/4]$. On
the full algebra $\Alg$, by contrast, $\omega_\theta$ is not faithful. For example, the projection
$\id-\ket{\phi_\theta}\bra{\phi_\theta}$ on a single pair is nonzero, but $\omega_\theta$ gives it zero. So
faithfulness is a property of a state *emph* a specific algebra, not a property of the state
alone. The GNS Hilbert space built from $(\Alg_R,\omega_\theta)$ is the same $\HH_{\Phi_\theta}$ as before,
because $\ket{\Phi_\theta}$ is cyclic for $\M_R$ (stated here without proof for the infinite chain).

The intuition is clearest for a single pair. Acting on $\ket{\phi_\theta}$ with operators on the right spin
alone already produces every vector in the pair's four-dimensional space $\mathbb C^2\otimes\mathbb C^2$.
Indeed,

$$

(A\otimes\id)\ket{\phi_\theta}=\cos\theta\,\big(A\ket0\big)\ket0+\sin\theta\,\big(A\ket1\big)\ket1 ,

$$

and as $A$ ranges over all $2\times2$ matrices, this covers all of $\mathbb C^2\otimes\mathbb C^2$ when
$\cos\theta$ and $\sin\theta$ are both nonzero. (We confirmed numerically that the four vectors
$(e_{ij}\otimes\id)\ket{\phi_\theta}$ are linearly independent.) So operators on the right spin reach
everything that operators on the left spin, or on both spins together, can reach. For the whole chain, the
same statement is that $\ket{\Phi_\theta}$ is cyclic for $\M_R$. This mirrors, on a much larger scale, the
point made earlier about minimal projections and irreducible representations. $\M_R$, as an abstract
algebra, already contains everything needed to rebuild the Hilbert space; $\HH_L$ only ever tracked
multiplicity. In this symmetric example, $R$ alone generates the same Hilbert space that $R$ and $L$ together
do.

With $\HH_{\Phi_\theta}$, $\M_R$, and $\M_L=\M_R'$ now built explicitly rather than only described, the stage is
set for the question that occupies the next two chapters. For different values of $\theta$, what
*emph*, in the precise sense of the classification above, is $\M_R$? Chapter~3 answers this by explicit
computation for $\theta=\pi/4$, where the answer is type $\mathrm{II}_1$. It also sets up the general case
$\theta\ne\pi/4$, which is type III and is completed in Chapter~4.



---

# Von Neumann algebras and entanglement: type I and II

Chapter~2 built the basic tools: algebras, states, projections, the type classification, and the GNS
construction. There the focus was on the algebra $\M$ itself, sitting inside some larger $B(\HH)$. This
chapter adds a specific physical state $\ket\Psi$ and asks the question the whole framework was built to
answer. Given $\Psi$, what does the *emph* of $\M$ tell us about how $\Psi$ entangles the subsystem
described by $\M$ with everything outside it?

We treat type I and type II here. Both types have a trace. Because of that, we can still define a density
operator and an entropy by a direct generalization of the formulas you already know. Type III has no trace at
all. It needs a different tool, and it is the subject of Chapter~4.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.88\textwidth]{figs/fig_type_chart.pdf}
\caption{The types of von Neumann factors, told apart by the values that the dimension function $d(P)$ takes on projections (one row per type, dots and bars marking the allowed values). Types $\mathrm{I}_n$ and $\mathrm{I}_\infty$ take only whole-number values, because they have minimal projections (projections onto single rays). Types $\mathrm{II}_1$ and $\mathrm{II}_\infty$ have no minimal projections but have a trace, finite or infinite, so $d(P)$ fills the interval $[0,1]$ or $[0,\infty]$. Type III has no trace, and every nonzero projection is infinite, so only $0$ and $\infty$ occur.}
\label{fig:type_chart}
\end{figure}

\begin{table}[htbp]
\centering
\footnotesize
\begin{tabularx}{\textwidth}{@{}l >{\raggedright\arraybackslash}p{2.3cm} >{\raggedright\arraybackslash}p{1.9cm}
>{\raggedright\arraybackslash}p{2.4cm} >{\raggedright\arraybackslash}X >{\raggedright\arraybackslash}p{2.7cm}@{}}
\toprule
**Factor** & **Values of $d(P)$** & **Trace** & **Density operator** &
**Example** & **Entropy** \\
\midrule
$\mathrm{I}_n$ & $\{0, 1, \dots, n\}$ & yes, finite & $\rho_R = \Tr_L\ket\Psi\bra\Psi$ &
$n$-level system; qubits & ordinary, $S \ge 0$ \\
$\mathrm{I}_\infty$ & $\{0, 1, 2, \dots, \infty\}$ & yes, semifinite & $\rho_R = \Tr_L\ket\Psi\bra\Psi$ &
harmonic oscillator; Fock space & ordinary, $S \ge 0$ \\
$\mathrm{II}_1$ & $[0, 1]$ & yes, finite, $\tr(\id)=1$ & $\rho_\M$ from eq.~\eqref{eq:rhoM-def} &
infinite chain of Bell pairs at $\theta=\pi/4$ & $S_\M \le 0$; minus a relative entropy \\
$\mathrm{II}_\infty$ & $[0, \infty]$ & yes, semifinite & exists (Chapter~5) &
crossed product $\M \rtimes \mathbb{R}$ & defined up to a constant; $S_{\rm gen}$ (Chapter~5) \\
$\mathrm{III}_0$ & $\{0, \infty\}$ & none & none & few physical examples & relative entropy only \\
$\mathrm{III}_\lambda$ & $\{0, \infty\}$ & none & none & spin chain with $\tan^2\theta = \lambda$ &
relative entropy only \\
$\mathrm{III}_1$ & $\{0, \infty\}$ & none & none & QFT subregion; Rindler wedge &
relative entropy only; crossed product gives $\mathrm{II}_\infty$ \\
\bottomrule
\end{tabularx}
\caption{The factor types and how each one handles density operators and entropy.}
\label{tab:factor_taxonomy}
\end{table}

## Density operators for type I and II algebras

We start with the central new formula of this chapter. Suppose the full system is in a state
$\ket\Psi\in\HH$. Let $\M$ be a von Neumann algebra with a trace $\tr$. By the type classification of
Chapter~2, this means $\M$ is type I or type II. Define $\rho_\M$ to be the operator in $\M$ that satisfies
\begin{equation}
\tr(A\rho_\M) = \braket{\Psi|A|\Psi} \qquad \text{for every } A\in\M .
\label{eq:rhoM-def}
\end{equation}
This equation has exactly one solution $\rho_\M$, and that solution is positive. We quote this result without
proof. It is a noncommutative version of the Radon—Nikodym theorem, and it needs two conditions: the trace must
be faithful and normal, and the state must be normal. Both hold in every example of this chapter. The
normalization is automatic: setting $A=\id$ gives $\tr\rho_\M=\braket{\Psi|\Psi}=1$. So $\rho_\M$ deserves
the name "density operator."

One point is essential. The operator $\rho_\M$ is required to lie in $\M$ itself, not merely in $B(\HH)$. We
solve eq.~\eqref{eq:rhoM-def} *emph* the algebra. (If $\rho_\M$ is unbounded, the precise statement is
that $\rho_\M$ is *emph* with $\M$: all of its spectral projections lie in $\M$.)

Once we have $\rho_\M$, we define the entanglement entropy in the expected way:
\begin{equation}
S_\M \equiv -\tr(\rho_\M\log\rho_\M) .
\label{eq:SM-def}
\end{equation}
This has the same form as the ordinary formula $S_R=-\Tr(\rho_R\log\rho_R)$. Two things have been replaced.
The algebra's own trace $\tr$ from Chapter~2, which may be renormalized, stands in for the ordinary
Hilbert-space trace. And $\rho_\M$ stands in for the ordinary reduced density matrix.

Compare this with the formula you already know, the partial trace $\rho_R=\Tr_L\ket\Psi\!\bra\Psi$. That formula
needs the complement $L$ to be given explicitly, as a separate tensor factor that you can trace over. In other
words, to build an object that describes the part of the world you *emph* access, you must know about the
part you *emph* access. Equation~\eqref{eq:rhoM-def} needs nothing of the sort. It uses only the trace of
$\M$ and the expectation values of operators in $\M$.

This raises an obvious question. If only $\M$ enters the definition, in what sense does $\rho_\M$ capture
entanglement with the outside world? The answer depends on the *emph* of $\M$. Working it out type by type
is the content of the rest of this chapter and of Chapter~4.

## Type I algebras

### The type I factor case: nothing is lost

When $\M$ is a type I *emph*, Chapter~2 showed that

$$

\HH=\HH_R\otimes\HH_L, \qquad \M=B(\HH_R)\otimes\id_L, \qquad \M'=\id_R\otimes B(\HH_L) ,

$$

and the trace is $\tr(a\otimes\id_L)=\Tr_{\HH_R}(a)$. Let $\rho_R=\Tr_{\HH_L}\ket\Psi\bra\Psi$ be the ordinary
reduced density matrix. For any $A=a\otimes\id_L$ in $\M$,
\begin{align}
\braket{\Psi|a\otimes\id_L|\Psi}
&\eqstep{1} \Tr_{\HH}\big((a\otimes\id_L)\ket\Psi\bra\Psi\big) \notag\\
&\eqstep{2} \Tr_{\HH_R}\big(a\,\Tr_{\HH_L}\ket\Psi\bra\Psi\big)
\ \eqstep{3}\ \Tr_{\HH_R}(a\rho_R) \notag\\
&\eqstep{4} \tr\big((a\otimes\id_L)(\rho_R\otimes\id_L)\big) . \notag
\end{align}
**(1)** an expectation value is the trace of the operator times the projector $\ket\Psi\bra\Psi$.\quad
**(2)** do the trace over $\HH_L$ first; the operator $a$ does not act on $\HH_L$, so it comes out of that
partial trace.\quad
**(3)** definition of $\rho_R$.\quad
**(4)** $(a\otimes\id_L)(\rho_R\otimes\id_L)=a\rho_R\otimes\id_L$, and $\tr$ of this is $\Tr_{\HH_R}(a\rho_R)$.

Comparing with the defining equation~\eqref{eq:rhoM-def}, we read off $\rho_\M=\rho_R\otimes\id_L$. This is the
ordinary reduced density matrix, written as an element of $\M$. The new definition, which uses only the algebra,
and the old one, which uses a partial trace, give *emph* the same operator whenever a type I
factorization is available. Nothing is lost by switching definitions. It follows that $S_\M=S_R$.

Two remarks follow. They are the seeds of everything that happens once type I is no longer available.

1. The two recipes are conceptually different, even though they agree here. The partial-trace recipe needs
the full global state $\ket\Psi$, including the part in $\HH_L$ that an observer on $R$ cannot access.
Equation~\eqref{eq:rhoM-def} needs only expectation values of operators in $\M$. An observer on $R$ could, in
principle, collect those data. So in the type I case, all of the entanglement information was already contained
in the internal data of $\M$. The tensor-product recipe was a roundabout way of getting the same answer, and it
is the recipe that breaks once no factorization exists.
2. Here $\tr$ equals the ordinary $\Tr_{\HH_R}$, which counts basis states of an honest Hilbert space
$\HH_R$. So $S_\M=S_R$ keeps its usual statistical meaning: roughly, the logarithm of the number of
effectively occupied states. This meaning, too, becomes much more delicate once we leave type I.


### General type I: a nontrivial center, and where lattice gauge theory fits

Now suppose $\M$ is type I but *emph* a factor. Then it has a nontrivial center. (Recall the
block-diagonal example with projections $P_1,P_2$ in Chapter~2.) The Hilbert space splits into a direct sum of
sectors, one for each value $\alpha$ of the central label. This label is classical: every operator in $\M$
commutes with it. We have

$$

\HH=\bigoplus_\alpha\HH_\alpha, \quad \HH_\alpha=\HH_{R\alpha}\otimes\HH_{L\alpha}, \qquad
\M=\bigoplus_\alpha\big(B(\HH_{R\alpha})\otimes\id_{L\alpha}\big) .

$$

Within each sector, the tensor-product story of the factor case holds exactly. The sectors sit side by side and
never mix. Every operator in $\M$ is block diagonal, so it never sends a state in sector $\alpha$ to a state in
a different sector $\alpha'$. A general element of $\M$ has the form $A=\bigoplus_\alpha(a_\alpha\otimes
\id_{L\alpha})$, and the trace is built sector by sector:

$$

\tr A=\sum_\alpha\Tr_{\HH_{R\alpha}}a_\alpha .

$$


A general density matrix $\rho$ on $\HH$ can have blocks that connect different sectors. Operators in $\M$
cannot detect those off-diagonal blocks, because they are block diagonal. So only the diagonal blocks matter,
and we write them as $p_\alpha\rho_\alpha$. Here $p_\alpha$ is the classical probability of being in sector
$\alpha$, and $\rho_\alpha$ is a normalized density matrix within that sector. Let
$\rho_{R\alpha}=\Tr_{\HH_{L\alpha}}\rho_\alpha$ be the ordinary reduced density matrix within sector $\alpha$.
For $A\in\M$,
\begin{align}
\Tr_\HH(\rho A)
&\eqstep{1} \sum_\alpha p_\alpha\Tr_{\HH_\alpha}\big(\rho_\alpha(a_\alpha\otimes\id_{L\alpha})\big)
\ \eqstep{2}\ \sum_\alpha p_\alpha\Tr_{\HH_{R\alpha}}(\rho_{R\alpha}a_\alpha) \notag\\
&\eqstep{3} \tr\Big(A\,\bigoplus_\alpha p_\alpha(\rho_{R\alpha}\otimes\id_{L\alpha})\Big) . \notag
\end{align}
**(1)** $A$ is block diagonal, so only the diagonal blocks $p_\alpha\rho_\alpha$ of $\rho$
contribute.\quad
**(2)** the type I factor computation above, done inside each sector.\quad
**(3)** the sector-by-sector formula for $\tr$.

Comparing with eq.~\eqref{eq:rhoM-def} gives

$$

\rho_\M=\bigoplus_\alpha p_\alpha(\rho_{R\alpha}\otimes\id_{L\alpha}) .

$$

Now put this into eq.~\eqref{eq:SM-def}. Let $S_\alpha=-\Tr_{\HH_{R\alpha}}(\rho_{R\alpha}\log\rho_{R\alpha})$ be
the ordinary entanglement entropy within sector $\alpha$. Then
\begin{align}
S_\M
&\eqstep{1} -\sum_\alpha\Tr_{\HH_{R\alpha}}\big(p_\alpha\rho_{R\alpha}\log(p_\alpha\rho_{R\alpha})\big) \notag\\
&\eqstep{2} -\sum_\alpha p_\alpha\Tr_{\HH_{R\alpha}}\big(\rho_{R\alpha}(\log p_\alpha+\log\rho_{R\alpha})\big)
\notag\\
&\eqstep{3} -\sum_\alpha p_\alpha\log p_\alpha \;+\; \sum_\alpha p_\alpha S_\alpha .
\label{eq:SM-center}
\end{align}
**(1)** $\rho_\M$ is block diagonal, so $\log\rho_\M$ is computed block by block, and $\tr$ is the sum of
the traces of the $R$ parts.\quad
**(2)** $\log(cX)=\log c\,\id+\log X$ for a number $c>0$.\quad
**(3)** $\Tr_{\HH_{R\alpha}}\rho_{R\alpha}=1$, and the definition of $S_\alpha$.

The entropy splits into two recognizable pieces. The first is the classical (Shannon) entropy of *emph*. The second is the probability-weighted average of the quantum entanglement entropy
*emph* each sector. Nothing here is conceptually new. It is what you would compute by hand if someone
told you: ``the system is in configuration A with probability $p_A$, entangled by an amount $S_A$, or in
configuration B with probability $p_B$, entangled by an amount $S_B$, and you don't know which.'' The new point
is that this result comes directly out of the single formula~\eqref{eq:rhoM-def}. We do not have to reason it
out from scratch each time.

\begin{workedexamplebox}[: Superselection sectors in a two-site lattice gauge model]
Consider a toy lattice with two sites, $x_1$ and $x_2$, joined by one gauge link that crosses the cut between
them. Let the electric flux on the link take the values $q \in \{0, 1\}$. By Gauss's law, this flux can be
measured from either side of the cut, so it commutes with every gauge-invariant operator on each side. It is
therefore central, and it labels the sectors. The physical Hilbert space splits into two sectors:

$$

\HH_{\text{phys}} = \HH_{q=0} \oplus \HH_{q=1}
= (\HH_{R,0}\otimes\HH_{L,0}) \oplus (\HH_{R,1}\otimes\HH_{L,1}) .

$$

Suppose the state is a mixture of the two sectors,

$$

\rho = p_0\,\rho_0 \oplus p_1\,\rho_1 , \qquad p_0 = 0.8, \quad p_1 = 0.2 .

$$

In sector $q=0$, take the two sites to be in a Bell state, so $\rho_{R,0} = \operatorname{diag}(1/2, 1/2)$
and $S_0 = \log 2 \approx 0.6931$. In sector $q=1$, take them to be in a product state, so $S_1 = 0$.
We evaluate eq.~\eqref{eq:SM-center} one piece at a time (all logarithms are natural, so entropies are in
nats).

1. **Classical Shannon entropy of the flux label:**
\begin{align*}
H(p) &= -p_0\log p_0 - p_1\log p_1 = -0.8\log 0.8 - 0.2\log 0.2 \\
&\approx 0.1785 + 0.3219 = 0.5004 .
\end{align*}
2. **Average entanglement within the sectors:**

$$

\sum_\alpha p_\alpha S_\alpha = 0.8 \times \log 2 + 0.2 \times 0 \approx 0.5545 .

$$

3. **Total entropy of the algebra:**

$$

S_\M = H(p) + \sum_\alpha p_\alpha S_\alpha \approx 0.5004 + 0.5545 = 1.0549 .

$$


One formula captures both the classical uncertainty in the flux and the genuine quantum entanglement. It does
not need the Hilbert space to factorize across the cut.
\end{workedexamplebox}

This is exactly the situation of the lattice gauge theory example of Chapter~1. On a finite lattice, the algebra
of gauge-invariant local operators is type I. It still has minimal projections, and it still counts states in
the ordinary way, sector by sector. But it is not a factor. Gauge invariance imposes a classical superselection
label, such as the electric flux through the boundary. The single formula~\eqref{eq:rhoM-def} handles all of
this at once. A type I factor is the special case with a trivial center: only one sector, with $p_\alpha=1$.
So even at this early and mostly familiar stage, the algebraic language is already unifying cases that
otherwise need separate treatment.

## Type II algebras

This is where something genuinely new happens. The clearest way to see it is to build a type $\mathrm{II}_1$
factor by hand, out of the infinite Bell-pair chain of Chapter~2. We do every step of the construction below.
It is the first place in these notes where we can watch a new kind of mathematical object being built. The only
raw material is an infinite chain of ordinary qubits.

### Building a trace at $\theta=\pi/4$

Recall the Bell-pair chain from Chapter~2. The algebra $\Alg_R$ consists of finite-energy operations on the
right-hand spins, meaning operators that act on only finitely many of them. The state is
$\omega_\theta(A)=\braket{\Phi_\theta|A|\Phi_\theta}$, where $\ket{\Phi_\theta}$ is the infinite product of
pairs $\cos\theta\ket{00}+\sin\theta\ket{11}$. The von Neumann algebra $\M\equiv\M_R$ is built from $\Alg_R$
and $\omega_\theta$ by the GNS construction. Now fix $\theta=\pi/4$, so that every pair is maximally
entangled, and *emph*
\begin{equation}
\tr A \equiv \braket{\Phi_{\pi/4}|A|\Phi_{\pi/4}} , \qquad A\in\M .
\label{eq:typeII-trace}
\end{equation}
In notation, this is just the expectation value $\omega_{\pi/4}(A)$ from Chapter~2. The claim is that at
$\theta=\pi/4$, and only there, this expectation value *emph* has the cyclic property $\tr(AB)=\tr(BA)$
that defines a trace (Chapter~2). The rest of this section rests on this single fact, so we verify it.

**Step 1: a single pair.** Take one spin pair at $\theta=\pi/4$, in the state
$\ket{\phi_{\pi/4}}=\tfrac1{\sqrt2}(\ket{00}+\ket{11})$. Let
$a = \begin{psmallmatrix} a_{00} & a_{01} \\ a_{10} & a_{11} \end{psmallmatrix}$ be any operator on the right
spin alone, acting on the pair as $a\otimes\id_L$. We compute its expectation value by expanding the state:
\begin{align}
\braket{\phi_{\pi/4}|a\otimes\id_L|\phi_{\pi/4}}
&\eqstep{1} \frac{1}{2}\left(\bra{00}+\bra{11}\right)(a\otimes\id_L)\left(\ket{00}+\ket{11}\right) \notag\\
&\eqstep{2} \frac{1}{2}\Big( \braket{00|a\otimes\id|00} + \braket{00|a\otimes\id|11} \notag\\
&\qquad\quad + \braket{11|a\otimes\id|00} + \braket{11|a\otimes\id|11} \Big) \notag\\
&\eqstep{3} \frac{1}{2}\left( a_{00}\braket{0|0}_L + a_{01}\braket{0|1}_L + a_{10}\braket{1|0}_L
+ a_{11}\braket{1|1}_L \right) \notag\\
&\eqstep{4} \frac{1}{2}\left( a_{00} + a_{11} \right) \ \eqstep{5}\ \frac{1}{2}\Tr_2(a) .
\label{eq:typeII-single-pair}
\end{align}
**(1)** substitute $\ket{\phi_{\pi/4}}=\frac1{\sqrt2}(\ket{00}+\ket{11})$ on both sides.\quad
**(2)** expand the product of two two-term sums into four terms.\quad
**(3)** $a\otimes\id_L$ acts only on the first (right) qubit, so each term factorizes into a matrix
element of $a$ times an inner product on $L$.\quad
**(4)** $\braket{0|0}_L=\braket{1|1}_L=1$ and $\braket{0|1}_L=\braket{1|0}_L=0$, so the cross terms
vanish.\quad
**(5)** $a_{00}+a_{11}$ is the ordinary matrix trace $\Tr_2(a)$.

Here $\Tr_2$ is the ordinary $2\times2$ matrix trace. So in a single maximally entangled pair, the expectation
value of any operator on one side is exactly one half of its ordinary trace. The coefficient $\tfrac12$ is
$1/\dim(\HH_2)$ for a single qubit. It will come back when we compute the dimensions of projections below.

**Step 2: many pairs.** A typical element of $\Alg_R$ is a product $A=a_1\otimes a_2\otimes\cdots$, where
only finitely many of the $a_i$ differ from the identity. Say $a_{i_1},\dots, a_{i_k}$ are the nontrivial ones.
General elements of $\Alg_R$ are finite sums of such products, and general elements of $\M_R$ are limits of
these sums. Since $\ket{\Phi_{\pi/4}}$ is a product over pairs,
\begin{align}
\braket{\Phi_{\pi/4}|A|\Phi_{\pi/4}}
&\eqstep{1} \prod_{i}\braket{\phi_{\pi/4}|a_i\otimes\id_L|\phi_{\pi/4}} \notag\\
&\eqstep{2} \frac{1}{2^k}\,\Tr_2(a_{i_1})\cdots\Tr_2(a_{i_k}) .
\label{eq:typeII-many-pairs}
\end{align}
**(1)** both $A$ and $\ket{\Phi_{\pi/4}}$ are products over pairs, so the expectation value is a product of
single-pair expectation values.\quad
**(2)** each touched pair gives $\tfrac12\Tr_2(a_{i_s})$ by eq.~\eqref{eq:typeII-single-pair}; each
untouched pair gives $\tfrac12\Tr_2(\id_2)=1$.

So the expectation value in the infinite chain reduces to a product of ordinary $2\times2$ traces, with one
factor of $\tfrac12$ for each of the $k$ pairs that $A$ actually touches.

**Step 3: cyclicity.** Take two product operators $A=\bigotimes_i a_i$ and $B=\bigotimes_i b_i$. Choose $n$
large enough that both act trivially beyond pair $n$. Then $AB=\bigotimes_i(a_ib_i)$, and
\begin{align}
\tr(AB)
&\eqstep{1} \prod_{i=1}^n \tfrac12\Tr_2(a_ib_i)
\ \eqstep{2}\ \prod_{i=1}^n \tfrac12\Tr_2(b_ia_i)
\ \eqstep{3}\ \tr(BA) . \notag
\end{align}
**(1)** eq.~\eqref{eq:typeII-many-pairs} applied to the product operator $AB$; pairs where $a_ib_i=\id_2$
contribute $1$.\quad
**(2)** the ordinary matrix trace is cyclic, $\Tr_2(a_ib_i)=\Tr_2(b_ia_i)$, pair by pair.\quad
**(3)** step (1) read backwards, for the product operator $BA$.

Both sides are linear in $A$ and in $B$, so cyclicity extends to finite sums of products, that is, to all of
$\Alg_R$. It then extends to all of $\M_R$ by continuity. For fixed $A$, both $B\mapsto\tr(AB)$ and
$B\mapsto\tr(BA)$ are continuous under the weak limits that build $\M_R$ out of $\Alg_R$, because a vector
expectation value is weakly continuous. So we may first take limits in $B$ and then, by the same argument,
in $A$. This establishes eq.~\eqref{eq:typeII-trace} as a genuine trace on $\M$.

This is exactly where $\theta=\pi/4$ earns its special status. For a general angle, Step~1 gives
$\braket{\phi_\theta|a\otimes\id_L|\phi_\theta}=\cos^2\theta\,a_{00}+\sin^2\theta\,a_{11}$. This is a weighted
sum, not a multiple of the trace, and cyclicity fails. A concrete check: take
$a=\ket0\!\bra1$ and $b=\ket1\!\bra0$, so that $ab=\ket0\!\bra0$ and $ba=\ket1\!\bra1$. Then

$$

\omega_\theta(ab)=\cos^2\theta , \qquad \omega_\theta(ba)=\sin^2\theta ,

$$

and these are equal only at $\theta=\pi/4$. So the state $\omega_\theta$ is not a trace when $\theta\ne\pi/4$.

More is true: for $\theta\neq\pi/4$ the algebra $\M_R$ admits no normalized trace of *emph* kind. This can
be proved directly, using the average magnetization of many spins and the law of large numbers.

\begin{keyresult}[: No normalized trace away from $\theta=\pi/4$]
**Theorem.** Let $\Alg_R = \bigotimes_{k=1}^\infty M_2(\mathbb{C})$ be the algebra of the right-hand spins,
generated by operators that act on finitely many sites. Let
$\ket{\Phi_\theta} = \bigotimes_{k=1}^\infty (\cos\theta\ket{00} + \sin\theta\ket{11})_k$ with
$\theta \in (0, \pi/2)$, and let $\M_R \equiv \pi_\theta(\Alg_R)'' \subseteq B(\HH_\theta)$ be the von Neumann
algebra given by the GNS construction. If $\theta \ne \pi/4$, then **there is no normal tracial state on
$\M_R$**.

**Proof.**

1. **A trace vanishes on each $\sigma_z$.**
Suppose, to reach a contradiction, that there is a normal tracial state $\tau: \M_R \to \mathbb{C}$ with
$\tau(\id) = 1$. Being a trace means $\tau(AB) = \tau(BA)$ for all $A, B \in \M_R$. Equivalently, $\tau([A,
B]) = 0$ for every commutator. At any single site $k$, the Pauli operators $\sigma_x^{(k)}, \sigma_y^{(k)},
\sigma_z^{(k)}$ lie in $\Alg_R \subset \M_R$. They obey $[\sigma_x, \sigma_y] = 2i\sigma_z$, so

$$

\sigma_z^{(k)} = \frac{1}{2i}\big[\sigma_x^{(k)}, \, \sigma_y^{(k)}\big] .

$$

Applying $\tau$ gives
\begin{align}
\tau\big(\sigma_z^{(k)}\big) \eqstep{1} \frac{1}{2i}\tau\big([\sigma_x^{(k)}, \, \sigma_y^{(k)}]\big)
\eqstep{2} 0 \qquad \text{for all } k \ge 1 . \notag
\end{align}
**(1)** substitute the commutator identity and pull the constant $\tfrac1{2i}$ out by linearity of
$\tau$.\quad
**(2)** a trace vanishes on every commutator.
2. **A trace vanishes on the average magnetization.**
Define the average magnetization of the first $N$ sites,

$$

M_N \equiv \frac{1}{N}\sum_{k=1}^N \sigma_z^{(k)} \in \M_R .

$$

Then
\begin{align}
\tau(M_N) \eqstep{1} \frac{1}{N}\sum_{k=1}^N \tau\big(\sigma_z^{(k)}\big) \eqstep{2} 0
\qquad \text{for all } N \ge 1 . \notag
\end{align}
**(1)** linearity of $\tau$.\quad
**(2)** every term vanishes by item~1.
3. **In the GNS state, the magnetization settles to a fixed value.**
Now look at $M_N$ in the GNS reference vector $\ket{\Omega_\theta} \equiv \ket{\Phi_\theta}$. For a single
pair,
\begin{align}
\braket{\phi_\theta | \sigma_z\otimes\id_L | \phi_\theta}
\eqstep{1} \cos^2\theta \braket{0|\sigma_z|0} + \sin^2\theta \braket{1|\sigma_z|1}
\eqstep{2} \cos^2\theta - \sin^2\theta
\eqstep{3} \cos(2\theta) . \notag
\end{align}
**(1)** $\sigma_z$ is diagonal, so the cross terms between $\ket{00}$ and $\ket{11}$ vanish. What remains
are the two diagonal terms, weighted by $\cos^2\theta$ and $\sin^2\theta$.\quad
**(2)** $\braket{0|\sigma_z|0}=+1$ and $\braket{1|\sigma_z|1}=-1$.\quad
**(3)** the double-angle identity.

So the average magnetization has expectation value

$$

\braket{\Omega_\theta | M_N | \Omega_\theta} = \frac{1}{N}\sum_{k=1}^N \cos(2\theta) = \cos(2\theta) .

$$

Write $c\equiv\cos(2\theta)$. The state $\ket{\Phi_\theta}$ is a product over pairs, so the fluctuations at
different sites $k \ne j$ are uncorrelated. At the same site, $(\sigma_z^{(k)})^2=\id$. Together these give

$$

\Braket{\Omega_\theta \Big| \big(\sigma_z^{(k)} - c\big)\big(\sigma_z^{(j)} - c\big) \Big| \Omega_\theta}
= \delta_{kj}\big(1 - c^2\big) = \delta_{kj}\sin^2(2\theta) .

$$

The variance of $M_N$ in the GNS vector is then
\begin{align}
\big\| \big(M_N - c\,\id\big)\ket{\Omega_\theta} \big\|^2
\eqstep{1} \frac{1}{N^2}\sum_{k,j=1}^N \delta_{kj}\sin^2(2\theta)
\eqstep{2} \frac{\sin^2(2\theta)}{N} \xrightarrow{N\to\infty} 0 . \notag
\end{align}
**(1)** write $M_N-c\,\id=\frac1N\sum_k(\sigma_z^{(k)}-c)$, expand the squared norm into a double sum, and
use the correlation formula just derived.\quad
**(2)** the Kronecker delta leaves $N$ equal terms.

This is the law of large numbers for $N$ independent spins. The average of many independent measurements of
$\sigma_z$ settles to its mean $c$, with fluctuations of order $1/\sqrt N$.
4. **From one vector to all vectors.**
We now show that $M_N\to c\,\id$ on *emph* vector, not only on $\ket{\Omega_\theta}$. Take any $A'$ in
the commutant $\M_R'$. Since $A'$ commutes with $M_N\in\M_R$,
\begin{align}
\big\|(M_N - c\,\id)A'\ket{\Omega_\theta}\big\|
\eqstep{1} \big\|A'(M_N - c\,\id)\ket{\Omega_\theta}\big\|
\leqstep{2} \|A'\|\,\big\|(M_N - c\,\id)\ket{\Omega_\theta}\big\| \xrightarrow{N\to\infty} 0 . \notag
\end{align}
**(1)** $A'$ commutes with $M_N$.\quad
**(2)** the operator-norm bound $\|A'v\|\le\|A'\|\,\|v\|$.

For $\theta\in(0,\pi/2)$ every pair has both Schmidt coefficients nonzero, so $\ket{\Omega_\theta}$ is
separating for $\M_R$ (Chapter~2). A vector is separating for $\M_R$ exactly when it is cyclic for $\M_R'$, so
the vectors $A'\ket{\Omega_\theta}$ are dense in $\HH_\theta$. The operators $M_N-c\,\id$ are uniformly
bounded, $\|M_N-c\,\id\|\le2$, so convergence on a dense set implies convergence on every vector. Hence $M_N$
converges in the strong operator topology to a multiple of the identity:

$$

\mathrm{s\text{-}}\lim_{N\to\infty} M_N = \cos(2\theta)\,\id .

$$

5. **The contradiction.**
A normal state is continuous under strong limits of uniformly bounded sequences. (On bounded sets, strong
convergence implies weak convergence, and a normal state is weakly continuous there.) Combining this with the
result $\tau(M_N)=0$ of item~2 gives two evaluations of the same limit:
\begin{align}
0 = \lim_{N\to\infty}\tau(M_N)
&\eqstep{1} \tau\Big(\mathrm{s\text{-}}\lim_{N\to\infty} M_N\Big) \notag\\
&\eqstep{2} \tau\big(\cos(2\theta)\id\big)
\ \eqstep{3}\ \cos(2\theta)\,\tau(\id)
\ \eqstep{4}\ \cos(2\theta) . \notag
\end{align}
**(1)** normality of $\tau$, applied to the bounded sequence $M_N$ and its strong limit from
item~4.\quad
**(2)** substitute the limit $\mathrm{s\text{-}}\lim M_N=\cos(2\theta)\id$.\quad
**(3)** linearity of $\tau$.\quad
**(4)** normalization, $\tau(\id)=1$.

So $\cos(2\theta)=0$. But for $\theta \in (0, \pi/2)$ with $\theta\ne\pi/4$ we have $\cos(2\theta)\ne0$. This
is a contradiction, so no normal tracial state $\tau$ exists on $\M_R$. $\blacksquare$

\end{keyresult}

Two comments on what this theorem does and does not show. First, at $\theta=\pi/4$ the argument gives no
contradiction: $\cos(2\theta)=0$, so $M_N\to0$, which agrees with $\tr(M_N)=0$. Second, the theorem rules out a
*emph* trace, that is, types $\mathrm{II}_1$ and $\mathrm{I}_n$ with finite $n$. It does not by
itself rule out an infinite (semifinite) trace, as in types $\mathrm{I}_\infty$ and $\mathrm{II}_\infty$.
Excluding those as well takes more work. The full result, due to Powers (1967), is that for $\theta\ne\pi/4$ the
algebra $\M_R$ is a type $\mathrm{III}_\lambda$ factor with $\lambda=\tan^2\theta$ (for $\theta<\pi/4$).
Chapter~4 derives this from the spectrum of the modular operator.

### No minimal projection, and dimensions that are real numbers

We now have a genuine trace, so $\M_R$ at $\theta=\pi/4$ is type I or type II. Which one? We use one fact that
we quote without proof: $\M_R$ is a factor, meaning that its center contains only multiples of the identity.
Now consider projections
built by forcing some finite set of spins to be spin-up and leaving the rest alone:

$$

\id \equiv \id_2\otimes\id_2\otimes\cdots, \qquad
P_1 = \id_2\otimes P_\uparrow\otimes\id_2\otimes\cdots, \qquad
P_2 = P_\uparrow\otimes\id_2\otimes P_\uparrow\otimes\id_2\otimes\cdots .

$$

Here $P_\uparrow=\begin{psmallmatrix}1&0\\0&0\end{psmallmatrix}$ is the projector onto spin-up for a single
qubit. In general, we can choose *emph* finite set of spins and replace their identity factors with
$P_\uparrow$.

**Dimensions.** We use the trace normalized so that $d(\id)=\tr(\id)=1$. This holds automatically, since
$\tr(\id)=\braket{\Phi_{\pi/4}|\Phi_{\pi/4}}=1$. By eq.~\eqref{eq:typeII-many-pairs}, and using
$\Tr_2(P_\uparrow)=1$,

$$

d(P_1)=\tr(P_1)=\tfrac12\Tr_2(P_\uparrow)=\tfrac12 , \qquad
d(P_2)=\tr(P_2)=\tfrac1{2^2}\Tr_2(P_\uparrow)\Tr_2(P_\uparrow)=\tfrac14 .

$$

In general, a projection that fixes $k$ spins has dimension exactly $2^{-k}$. This is positive for every finite
$k$, so every such projection is nonzero. Fixing one more spin halves the dimension, and this never reaches zero
at any finite step.

**No minimal projection.** Take any nonzero projection $P$ of this fixed-spin form. It fixes only finitely
many spins, so we can pick one more spin that $P$ leaves alone and fix it too. This gives a new projection
$\widetilde P$ with $\widetilde P<P$, and $\widetilde P$ is still nonzero, since $\tr(\widetilde P)=\tfrac12
\tr(P)>0$. So no projection of this form is minimal.

That argument covers only the fixed-spin projections. To rule out minimal projections of every kind, we use the
trace. Suppose $\M_R$ had a minimal projection $E$. Then $\M_R$ would be a type I factor, and two standard facts
about type I factors apply. All minimal projections are equivalent, so they all have the same trace $t$. Every
nonzero projection contains a minimal one. The trace is faithful, because $\ket{\Phi_{\pi/4}}$ is separating,
so $t=\tr(E)>0$. Now pick $k$ so large that $2^{-k}<t$, and take any projection $P$ that fixes $k$ spins. It
contains some minimal projection $E'\le P$, so $t=\tr(E')\le\tr(P)=2^{-k}<t$. This is a contradiction. So
$\M_R$ has no minimal projections, and by the type classification of Chapter~2 it is not type I.

**Every dimension in $[0,1]$.** Here something appears that has no counterpart in finite-dimensional
linear algebra. In ordinary quantum mechanics, the dimension of a subspace is a whole number, found by counting
basis vectors. There is no subspace of dimension $1/\pi=0.3183\ldots$. In $\M_R$ there is. Let
$P_\downarrow=\id_2-P_\uparrow$, and define projections that act on the first $n$ spins as

$$

Q_n = \underbrace{P_\downarrow\otimes\cdots\otimes P_\downarrow}_{n-1}\otimes P_\uparrow\otimes\id_2\otimes\cdots ,
\qquad \tr(Q_n)=2^{-n} .

$$

Any two of them are orthogonal: for $n<m$, the spin at site $n$ is up in $Q_n$ and down in $Q_m$. Now take any
number $x\in[0,1]$ with binary digits $x=\sum_n b_n2^{-n}$, $b_n\in\{0,1\}$. The partial sums of
$\sum_n b_nQ_n$ are projections in $\M_R$, and they converge strongly. Since $\M_R$ is closed under such limits,
the limit $P_x=\sum_n b_nQ_n$ is a projection in $\M_R$. The trace is a vector expectation value, so it adds up
over orthogonal projections, and

$$

d(P_x)=\sum_n b_n\tr(Q_n)=\sum_n b_n2^{-n}=x .

$$

So $d(P)$ takes every real value in $[0,1]$.

This continuous range of dimensions, together with the absence of minimal projections, is the defining signature
of type $\mathrm{II}_1$ (Chapter~2). Finite projections exist and can be compared in size, but there is no
smallest unit of dimension, only a continuum that can be refined forever. Since $\M_R$ is a factor, we
conclude: at $\theta=\pi/4$, $\M=\M_R$ is a type $\mathrm{II}_1$ factor. It is the first
genuinely new object in these notes, and we built it from nothing more than an infinite chain of ordinary
spin-$\tfrac12$ qubits.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.78\textwidth]{figs/fig_spin_chain_typeIII.pdf}
\caption{The Bell-pair chain at a generic angle, here $\theta=\pi/6$. (a) The entanglement entropy of $N$ pairs, in nats, grows linearly in $N$, so it diverges as $N\to\infty$ and no factorized $\HH_R$ survives the limit. (b) At $N=12$, the eigenvalues of the modular operator $\Delta_{\Phi_\theta}$ are the powers $\lambda^n$ with $\lambda=\tan^2\theta$, evenly spaced on a logarithmic axis; bar heights give the fraction of all $4^N$ eigenvalues equal to each power. As $N\to\infty$ this becomes the geometric ladder of a type $\mathrm{III}_\lambda$ factor (Chapter~4). At $\theta=\pi/4$, $\lambda=1$ and the whole ladder collapses to the single eigenvalue $1$ of the type $\mathrm{II}_1$ factor of this chapter.}
\label{fig:spin_chain_typeIII}
\end{figure}

### Interpreting $\rho_\M$ and $S_\M$: an entropy that can be negative

With the type $\mathrm{II}_1$ trace~\eqref{eq:typeII-trace}, we can use eq.~\eqref{eq:rhoM-def} to compute
$\rho_\M$, and eq.~\eqref{eq:SM-def} to compute $S_\M$, for many states. The results have a surprising feature
that looks at first like a mistake. So we work it out with actual numbers.

Take a state $\ket\Psi$ that equals $\ket{\Phi_{\pi/4}}$ everywhere except on a finite number $k$ of pairs,
labelled $i_1,\dots,i_k$. Those pairs are instead prepared in other pure two-qubit states $\ket{\eta_{i_s}}$.
Let $\rho_i$ be the ordinary reduced density matrix of pair $i$ on its right qubit. For the unchanged pairs,
$\rho_i=\tfrac12\id_2$. We claim that
\begin{equation}
\rho_\M(\Psi) = 2\rho_1\otimes2\rho_2\otimes\cdots\otimes2\rho_n\otimes\cdots ,
\label{eq:typeII-rhoM}
\end{equation}
where $2\rho_i=\id_2$ for every pair not among $i_1,\dots,i_k$. To check the claim, take any product operator
$A=\bigotimes_ia_i$. Then $A\rho_\M=\bigotimes_i(a_i\,2\rho_i)$, and
\begin{align}
\tr(A\rho_\M)
&\eqstep{1} \prod_i\tfrac12\Tr_2(a_i\,2\rho_i)
\ \eqstep{2}\ \prod_i\Tr_2(a_i\rho_i) \notag\\
&\eqstep{3} \prod_i\braket{\eta_i|a_i\otimes\id_L|\eta_i}
\ \eqstep{4}\ \braket{\Psi|A|\Psi} . \notag
\end{align}
**(1)** eq.~\eqref{eq:typeII-many-pairs}; only finitely many factors differ from $\id_2$.\quad
**(2)** the $\tfrac12$ cancels the $2$.\quad
**(3)** the ordinary partial-trace formula in each pair, with $\ket{\eta_i}=\ket{\phi_{\pi/4}}$ for the
unchanged pairs.\quad
**(4)** $\ket\Psi$ is a product over pairs.

By linearity and continuity, the same holds for every $A\in\M$, so eq.~\eqref{eq:typeII-rhoM} solves
eq.~\eqref{eq:rhoM-def}. The factor of $2$ comes directly from the $\tfrac12$ in
eq.~\eqref{eq:typeII-single-pair}. As a check, set $\Psi=\Phi_{\pi/4}$. Then every factor is $\id_2$ and
$\rho_\M(\Phi_{\pi/4})=\id$. This must be so, because $\tr(A\cdot\id)=\tr(A)=\braket{\Phi_{\pi/4}|A|\Phi_{\pi/4}}$
by the definition of $\tr$. The state that defines the trace has the identity as its density operator.

Now put eq.~\eqref{eq:typeII-rhoM} into the entropy formula~\eqref{eq:SM-def}. The logarithm of a tensor
product is the sum of the logarithms of the factors, and $\log(2\rho_i)=\log\id_2=0$ for every unchanged pair.
Therefore
\begin{align}
S_\M(\Psi) = -\tr(\rho_\M\log\rho_\M)
&\eqstep{1} -\sum_{s=1}^k \tfrac12\Tr_2\big(2\rho_{i_s}\log(2\rho_{i_s})\big) \notag\\
&\eqstep{2} -\sum_{s=1}^k \Big[\Tr_2(\rho_{i_s}\log\rho_{i_s}) + \log2\,\Tr_2\rho_{i_s}\Big] \notag\\
&\eqstep{3} \sum_{s=1}^k S_2(\rho_{i_s}) - k\log2 .
\label{eq:typeII-entropy}
\end{align}
**(1)** only the $k$ changed pairs contribute to $\log\rho_\M$. For each one, the trace factorizes pair by
pair as in eq.~\eqref{eq:typeII-many-pairs}. The pair itself gives $\tfrac12\Tr_2$, and every other factor gives
$\tfrac12\Tr_2(2\rho_j)=\Tr_2\rho_j=1$.\quad
**(2)** $\log(2\rho)=\log2\,\id_2+\log\rho$, and the $\tfrac12$ cancels the $2$.\quad
**(3)** $\Tr_2\rho_{i_s}=1$, and $S_2(\rho)\equiv-\Tr_2(\rho\log\rho)$ is the ordinary single-qubit
entropy.

Here $S_2(\rho_{i_s})$ is the ordinary entanglement entropy of the single changed pair $i_s$. It lies between
$0$ and $\log2$.

\begin{workedexamplebox}[: One changed pair at angle $\phi=0.3$]
Take $k=1$. Let the changed pair be prepared at angle $\phi=0.3$ instead of $\pi/4\approx0.785$, so
$\ket{\eta_{i_1}}=\cos(0.3)\ket{00}+\sin(0.3)\ket{11}$. This pair is less than maximally entangled. Its reduced
density matrix and the corresponding factor of $\rho_\M$ are

$$

\rho_{i_1}=\begin{pmatrix}\cos^2 0.3&0\\0&\sin^2 0.3\end{pmatrix}
\approx\begin{pmatrix}0.9127&0\\0&0.0873\end{pmatrix} , \qquad
2\rho_{i_1}\approx\begin{pmatrix}1.8253&0\\0&0.1747\end{pmatrix} .

$$

**Directly from $\rho_\M$.** Only this one factor of $\rho_\M$ differs from $\id_2$, so
\begin{align*}
S_\M(\Psi) &= -\tfrac12\Tr_2\big(2\rho_{i_1}\log(2\rho_{i_1})\big)
= -\tfrac12\big(1.8253\log1.8253+0.1747\log0.1747\big) \\
&\approx -0.5492+0.1524 = -0.3968 .
\end{align*}
**From eq.~\eqref{eq:typeII-entropy**.} The ordinary entropy of the pair is
$S_2(\rho_{i_1})=-0.9127\log0.9127-0.0873\log0.0873\approx0.2963$, and $\log2\approx0.6931$, so

$$

S_\M(\Psi) \approx 0.2963 - 0.6931 = -0.3968 .

$$

**From ordinary quantum mechanics.** The ordinary relative entropy of the qubit state $\rho_{i_1}$ with
respect to the maximally mixed state $\tfrac12\id_2$ is

$$

S\big(\rho_{i_1}\,\big\|\,\tfrac12\id_2\big)=\Tr_2\rho_{i_1}\big(\log\rho_{i_1}-\log\tfrac12\id_2\big)
=\log2-S_2(\rho_{i_1})\approx0.3968 .

$$

All three numbers agree to four decimals (we checked them numerically). So $S_\M(\Psi)$ is a genuinely
*emph* number, and it equals minus an ordinary relative entropy of one qubit.
\end{workedexamplebox}

The negative sign is not an accident of the angle chosen. The ordinary two-level entropy is at most $\log2$,
with equality only for a maximally entangled pair. So every term in the sum in eq.~\eqref{eq:typeII-entropy}
obeys $S_2(\rho_{i_s})-\log2\le0$. Hence $S_\M(\Psi)\le0$ for *emph* state built this way. Equality holds
only when every changed pair is still maximally entangled.

At first sight this is alarming. The operator $\rho_\M$ is a genuine density operator: it is positive and
$\tr\rho_\M=1$. Yet $-\tr(\rho_\M\log\rho_\M)$ is negative. For an ordinary finite-dimensional density matrix
this can never happen, since $-\Tr(\rho\log\rho)\ge0$, with equality only for a pure state. There is no
contradiction, and the resolution is simple. Here $\tr$ is *emph* the ordinary matrix trace that counts basis
states one at a time. We built it from expectation values in the maximally entangled reference state
$\ket{\Phi_{\pi/4}}$. In a type II algebra there is no minimal projection to serve as "one state." So $\tr$
never had the counting interpretation that makes the ordinary entropy non-negative.

What eq.~\eqref{eq:typeII-entropy} actually computes is minus a *emph* entropy:

$$

S_\M(\Psi) = -S_\M(\Psi\,\|\,\Phi_{\pi/4}) .

$$

Here $S(\rho\|\sigma)=\tr\rho(\log\rho-\log\sigma)$ is the relative entropy of quantum information theory
(mentioned in Chapter~1), applied with $\rho=\rho_\M(\Psi)$ and $\sigma=\rho_\M(\Phi_{\pi/4})=\id$. Since
$\log\id=0$, the identity follows at once from eq.~\eqref{eq:SM-def}. It holds for every state that has a
density operator, not only for the simple states used above. That the right-hand side agrees with the general
definition of relative entropy in a von Neumann algebra is a standard result, which we quote without proof.

Relative entropy measures how distinguishable a state is from a chosen reference state. It always obeys
$S(\rho\|\sigma)\ge0$, so $-S(\rho\|\sigma)\le0$. This matches what we just computed. So in a type II algebra,
$S_\M$ should not be read as "how many microstates the state occupies." That reading only makes sense when
there is a minimal projection to count from. Instead, $S_\M$ is **a signed distance from the maximally
entangled reference state that defines the trace**. It is a relative quantity, not an absolute one.

This is the first place in the notes where relative entropy, rather than entropy itself, turns out to be the more
fundamental and more robust object. A suitable generalization of relative entropy (due to Araki) survives
through type III (Chapter~4) and into the holographic applications that begin in Chapter~6. Ordinary entropy,
as we have just seen, already changes its meaning at type II.


> [!NOTE] **Physics Connection: Negative relative entropy in qubits**
> Is a negative "entropy" a sensible thing for a theory to produce? Ordinary finite-dimensional quantum
> mechanics already contains the same phenomenon in disguise. Take a $d$-dimensional quantum system, and compute
> the relative entropy of any state $\rho$ with respect to the maximally mixed state $\sigma=\id/d$:
> \begin{align}
> S(\rho\|\sigma) \eqstep{1} \Tr\rho\big(\log\rho - \log(\id/d)\big) \eqstep{2} -S(\rho) + \log d . \notag
> \end{align}
> **(1)** the definition of relative entropy, with $\sigma=\id/d$.\quad
> **(2)** $\log(\id/d)=-\log d\,\id$ and $\Tr\rho=1$; here $S(\rho)\equiv-\Tr(\rho\log\rho)$ is the ordinary
> von Neumann entropy.
> 
> The entropy never exceeds its maximally mixed value, $S(\rho)\le\log d$, so $S(\rho\|\sigma)\ge0$, as a relative
> entropy must be. Now flip the sign: $-S(\rho\|\sigma)=S(\rho)-\log d$. For a qubit ($d=2$) in the state
> $\rho=\mathrm{diag}(0.9,0.1)$, we get $S(\rho)\approx0.325$ and $\log2\approx0.693$, so
> $-S(\rho\|\sigma)\approx-0.368$. This is a negative number, obtained from an ordinary qubit entropy minus a
> constant.
> 
> This is exactly the mechanism behind eq.~\eqref{eq:typeII-entropy}, with the constant written out. In a type II
> algebra, $S_\M$ is built the same way: an ordinary-looking entropy, shifted down by the baseline set by the
> maximally entangled reference state. In finite dimensions the baseline is the finite number $\log d$. In the
> type $\mathrm{II}_1$ Bell-pair algebra the same baseline is present, but it has been absorbed into the
> definition of $\tr$, which was built from the maximally entangled state $\ket{\Phi_{\pi/4}}$. It is no longer a
> separate $\log d$ that we subtract by hand.
> 
> The arithmetic of entropy has not changed. Subtracting a constant from an ordinary entropy could always give a
> negative number. What is new in the type II case is that the algebra offers no other baseline. With no minimal
> projection there is no "$d$" to normalize against. Moreover, a type $\mathrm{II}_1$ factor has exactly one
> normalized trace. So the reference state is not a free choice: it is fixed by the algebra.


### Changing infinitely many pairs: the law of large numbers

Equation~\eqref{eq:typeII-entropy} says that each changed pair lowers $S_\M$ by $\log2-S_2(\rho_i)\ge0$. What
happens if we keep changing more and more pairs? Let $\Psi_N$ be the state in which the first $N$ pairs are at
angle $\phi$ and all the others are at $\pi/4$. Then

$$

S_\M(\Psi_N) = -N\big[\log2-S_2(\phi)\big] .

$$

For $\phi=0.3$ the deficit per pair is $0.3968$, so after $N=100$ pairs $S_\M\approx-39.68$. As $N\to\infty$,
$S_\M(\Psi_N)\to-\infty$. The limiting state is the chain $\Phi_\phi$ with every pair at angle $\phi$, and it
has no density operator at all with respect to this trace. The law of large numbers shows why.

**Where the state lives.** By eq.~\eqref{eq:typeII-rhoM}, $\rho_\M(\Psi_N)=(2\rho_\phi)^{\otimes
N}\otimes\id\otimes\cdots$, where $\rho_\phi=\mathrm{diag}(\cos^2\phi,\sin^2\phi)$. On a configuration in which
$m$ of the first $N$ right spins are up, this operator has the eigenvalue

$$

2^N\cos^{2m}\phi\,\sin^{2(N-m)}\phi .

$$

In the state $\Psi_N$, each of the first $N$ right spins is up with probability $\cos^2\phi$, independently. By
the law of large numbers, $m/N\to\cos^2\phi$. So the eigenvalue that the state typically sees is
\begin{align}
2^N\cos^{2m}\phi\,\sin^{2(N-m)}\phi
&\eqstep{1} \exp\Big\{N\big[\log2+\cos^2\phi\log\cos^2\phi+\sin^2\phi\log\sin^2\phi\big]\Big\} \notag\\
&\eqstep{2} e^{N[\log2-S_2(\phi)]} \xrightarrow{N\to\infty}\infty . \notag
\end{align}
**(1)** take the logarithm and set $m=N\cos^2\phi$.\quad
**(2)** $S_2(\phi)=-\cos^2\phi\log\cos^2\phi-\sin^2\phi\log\sin^2\phi$.

**Where the trace lives.** Under the trace, each spin is up with probability $\tfrac12$, so the trace
concentrates on configurations with $m/N\to\tfrac12$. The configurations where $\Psi_N$ lives, with $m\approx
N\cos^2\phi$, number roughly $e^{NS_2(\phi)}$, and each has trace weight $2^{-N}$. Their total trace is
therefore about $e^{-N[\log2-S_2(\phi)]}\to0$. As $N$ grows, the state piles up on a set of vanishing trace,
with a density that grows without bound. In the limit, the density would have to be infinite on a set of trace
zero, and no operator can do that.

**The sharp version.** This is the same law of large numbers that drives the theorem above. Apply item~3
of its proof at $\theta=\pi/4$. The variance is $1/N$, so $M_N\to0$ strongly on the $\pi/4$ Hilbert space.
Suppose $\Phi_\phi$ had a density operator $\rho$ in $\M_R$. The state $A\mapsto\tr(A\rho)$ would then be
normal, and so $\tr(\rho M_N)\to0$. But $\braket{\Phi_\phi|M_N|\Phi_\phi}=\cos(2\phi)$ for every $N$, which is
nonzero unless $\phi=\pi/4$. So $\Phi_\phi$ is not a normal state of the $\pi/4$ algebra. It is not described by
any vector or density matrix in the Hilbert space $\HH_{\Phi_{\pi/4}}$. The density operator of
eq.~\eqref{eq:rhoM-def} exists for states that differ from $\Phi_{\pi/4}$ on finitely many pairs, or by
changes that die off fast enough along the chain. It does not exist for a change of fixed size repeated on
infinitely many pairs.

### Type $\mathrm{II}_\infty$

For a type $\mathrm{II}_\infty$ factor, the same interpretation of $\rho_\M$ and $S_\M$ carries over, with one
difference. In the $\mathrm{II}_1$ case the condition $d(\id)=1$ fixes the normalization of the trace. In the
$\mathrm{II}_\infty$ case $\tr(\id)=\infty$, so there is no such condition. The trace is unique only up to a
positive constant, $\tr'=c\,\tr$. Rescaling the trace changes the density operator to $\rho'=\rho/c$, since
$\tr'(A\rho/c)=\tr(A\rho)$. The entropy then shifts by a constant:
\begin{align}
S'=-\tr'(\rho'\log\rho')
&\eqstep{1} -c\,\tr\Big(\frac{\rho}{c}\big(\log\rho-\log c\,\id\big)\Big) \notag\\
&\eqstep{2} -\tr(\rho\log\rho)+\log c\,\tr\rho
\ \eqstep{3}\ S+\log c . \notag
\end{align}
**(1)** substitute $\tr'=c\,\tr$ and $\rho'=\rho/c$, and use $\log(\rho/c)=\log\rho-\log c\,\id$.\quad
**(2)** the factors $c$ and $1/c$ cancel.\quad
**(3)** $\tr\rho=1$.

So in type $\mathrm{II}_\infty$, the entropy is defined only up to an additive constant that is the same for
every state. Entropy differences between states are unambiguous. This is exactly the situation we will meet in
the crossed product of Chapter~5.

## Summary

We can now combine the type I and type II results into one statement, before Chapter~4 introduces type III. The
*emph* of the algebra $\M$ that describes a subsystem determines, independently of the state, what
*emph* of entanglement every state of the full system can have.


- **Type I factor.** A genuine tensor factorization $\HH=\HH_R\otimes\HH_L$ exists. Unentangled
product states exist, and every state is built from them by superposition or mixing. This is the ordinary
textbook picture of quantum mechanics, and $\rho_\M$ is the ordinary reduced density matrix.
- **Type I with a center.** The Hilbert space splits into superselection sectors. The entropy is the
classical Shannon entropy of the sector label plus the average entanglement within the sectors,
eq.~\eqref{eq:SM-center}. Lattice gauge theory is an example.
- **Type II factor.** There are no minimal projections. A standard result says that a normal pure state
on $\M$ exists only if $\M$ has a minimal projection. So no state of the full system restricts to a pure state
on $\M$. There is no unentangled reference state anywhere. In this sense *emph* state of the full system
is entangled across $(\M,\M')$. There is no "ground floor" of zero entanglement to compare against. There is
only the maximally entangled reference state that defines the trace, and the entropy~\eqref{eq:SM-def} is
measured relative to it. In type $\mathrm{II}_1$ this entropy is minus a relative entropy and is never positive.
In type $\mathrm{II}_\infty$ it is defined up to a state-independent constant.


In type III, not even a trace exists, so eqs.~\eqref{eq:rhoM-def} and~\eqref{eq:SM-def} cannot be written down
at all. Type III is the subject of the next chapter. It is not an exotic corner case. It is the type that governs
local regions of relativistic quantum field theory, and holographic boundary subalgebras in the strict large-$N$
limit. These are the central objects of these notes.



---

# Von Neumann algebras and entanglement: type III

This chapter is the technical heart of the notes. A type III algebra has no trace. So the density operator
$\rho_\M$ and the entropy $S_\M$ of Chapter~3 cannot even be defined. Type III is not a rare special case,
though. It is the type of the algebra of a local region in a relativistic quantum field theory. As Chapter~7
will show, it is also the type of the holographic boundary algebras in the strict large-$N$ limit. To say
anything about entanglement in these settings, we need a different tool. That tool is
**Tomita—Takesaki modular theory**. Its core physical idea fits in one sentence, before any formalism:
*emph* Seen from inside one half, entanglement looks like heat. This chapter makes that one
idea precise.

## Emergent times from entanglement — modular flows

### Starting from something you already understand: the type I case, retold

To motivate the general construction, go back to an ordinary type I bipartite pure state $\ket\Psi$. Assume
that its reduced density matrix $\rho_R$ is full-rank. "Full-rank" means invertible: every eigenvalue is
strictly positive, so $\rho_R^{-1}$ exists. This will matter in a moment. Instead of studying the entropy $S_R$
directly, we package the same information in a different way. Write

$$

\rho_R = e^{-K_R}, \qquad K_R\equiv-\log\rho_R .

$$

The operator $K_R$ is called the **entanglement Hamiltonian**. It satisfies $K_R\ge0$, because the
eigenvalues of $\rho_R$ lie in $(0,1]$, so their negative logarithms are all $\ge0$. The full set of
eigenvalues of $K_R$ is called the *emph*. It carries more information than the entropy
$S_R$, and more than any finite list of R\'enyi entropies. Each of those numbers is one particular weighted sum
over the spectrum, while the spectrum itself is the unsummed data. This is why condensed-matter physicists
study entanglement spectra directly, and not only the single number $S_R$. It has proved to be a very useful
diagnostic.

Now use $K_R$ to generate a flow:
\begin{equation}
A(s) = e^{iK_Rs}Ae^{-iK_Rs} \in B(\HH_R), \qquad A\in B(\HH_R) .
\label{eq:modflow-typeI}
\end{equation}
This has the same form as ordinary Heisenberg time evolution, $A(t)=e^{iHt}Ae^{-iHt}$. Here $K_R$ plays the
role of the Hamiltonian and $s$ plays the role of time. The flow is called **modular flow**, and $s$ is
called **modular time**. The key physical claim is the following. An observer confined to $R$, who uses
$s$ as their time, should see their system in thermal equilibrium. The reason is simple. By construction,
$\rho_R=e^{-K_R}$ is an ordinary Gibbs density matrix for the "Hamiltonian" $K_R$, at the dimensionless
inverse temperature $\beta=1$. In precise terms, correlation functions of modular-flowed operators satisfy the
**Kubo—Martin—Schwinger (KMS) condition**. This condition is the mathematical signature of thermal
equilibrium. It is spelled out precisely below.

The same construction works on the $L$ side, with $K_L=-\log\rho_L$. To treat both sides at once, define
\begin{equation}
\Delta_\Psi \equiv \rho_R\otimes\rho_L^{-1}, \qquad -\log\Delta_\Psi = K_R - K_L ,
\label{eq:Delta-typeI}
\end{equation}
and let the modular flow act on operators of *emph* side:

$$

\begin{aligned}
\sigma_s(A) &\equiv \Delta_\Psi^{-is}A\Delta_\Psi^{is}\in B(\HH_R), &\qquad& A\in B(\HH_R), \\
\sigma_s(A') &\equiv \Delta_\Psi^{-is}A'\Delta_\Psi^{is}\in B(\HH_L), && A'\in B(\HH_L) .
\end{aligned}

$$

Here, as usual, an operator $A$ on $\HH_R$ stands for $A\otimes\id_L$, and an operator $A'$ on $\HH_L$ stands
for $\id_R\otimes A'$. Let us check that this reduces to the one-sided flow \eqref{eq:modflow-typeI} for
$A\in B(\HH_R)$:
\begin{align}
\Delta_\Psi^{-is}(A\otimes\id_L)\Delta_\Psi^{is}
&\eqstep{1} (\rho_R^{-is}\otimes\rho_L^{is})(A\otimes\id_L)(\rho_R^{is}\otimes\rho_L^{-is}) \notag\\
&\eqstep{2} \rho_R^{-is}A\rho_R^{is}\otimes\rho_L^{is}\rho_L^{-is}
\ \eqstep{3}\ \rho_R^{-is}A\rho_R^{is}\otimes\id_L . \notag
\end{align}
**(1)** a power of a tensor product of positive operators is the tensor product of the powers.\quad
**(2)** operators on different tensor factors multiply factor by factor.\quad
**(3)** $\rho_L^{is}\rho_L^{-is}=\id_L$.
Since $\rho_R^{-is}=e^{iK_Rs}$, this is exactly \eqref{eq:modflow-typeI}. So the single joint object
$\Delta_\Psi$ reproduces the one-sided flow on each side. The operator $\Delta_\Psi$ is called the
**modular operator**.


> [!EXAMPLE] **Worked Example:**
> Take the two-qubit state
> $\ket{\phi_\theta}=\cos\theta\ket{00}+\sin\theta\ket{11}$ from Chapter~1, with $0<\theta<\pi/2$ so that both
> coefficients are nonzero. In each basis vector $\ket{ab}$, the first label refers to the $R$ qubit and the
> second to the $L$ qubit. Then $\rho_R=\rho_L=\mathrm{diag}(\cos^2\theta,\sin^2\theta)$. In the basis
> $\ket{00},\ket{01},\ket{10},\ket{11}$, the modular operator $\Delta_\Psi=\rho_R\otimes\rho_L^{-1}$ is the
> diagonal matrix
> 
$$

> \Delta_\Psi = \begin{pmatrix} 1&0&0&0\\ 0&\cot^2\theta&0&0\\
> 0&0&\tan^2\theta&0\\0&0&0&1\end{pmatrix}
> = \operatorname{diag}\left(1, \; \cot^2\theta, \; \tan^2\theta, \; 1\right) .
> 
$$

> For example, the $\ket{01}$ entry is $\cos^2\theta/\sin^2\theta=\cot^2\theta$. The eigenvalues are $1$
> (twice, on $\ket{00}$ and $\ket{11}$), $\lambda\equiv\tan^2\theta$ (on $\ket{10}$), and
> $\lambda^{-1}=\cot^2\theta$ (on $\ket{01}$).
> 
> Now let us build three more objects from first principles, using only the algebra and the state. They are the
> Tomita operator $S_\Psi$, its adjoint $F_\Psi \equiv S_\Psi^\dagger$, and the modular conjugation $J_\Psi$.
> (Remark~(c) after the Tomita—Takesaki theorem below defines them in general.) We will see that $\Delta_\Psi$
> comes out of them.
> 
1. **Action of the algebra on $\ket{\phi_\theta**$.} Any operator $A \in B(\HH_R)$ is a $2\times2$
> matrix $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$. Acting on $\ket{\phi_\theta}$ it gives
> 
$$

> (A\otimes\id_L)\ket{\phi_\theta} = a\cos\theta\ket{00} + b\sin\theta\ket{01} + c\cos\theta\ket{10}
> + d\sin\theta\ket{11} .
> 
$$

> Now take an arbitrary vector $\ket x = x_{00}\ket{00} + x_{01}\ket{01} + x_{10}\ket{10} + x_{11}\ket{11}$.
> Matching coefficients shows that $\ket x=(A\otimes\id_L)\ket{\phi_\theta}$ for exactly one $A$, namely
> $a = x_{00}/\cos\theta$, $b = x_{01}/\sin\theta$, $c = x_{10}/\cos\theta$, $d = x_{11}/\sin\theta$.
> 
>
2. **The Tomita operator $S_\Psi$.** It is defined by
> $S_\Psi(A\otimes\id_L)\ket{\phi_\theta} = (A^\dagger\otimes\id_L)\ket{\phi_\theta}$. It is antilinear, which
> means $S_\Psi(z\ket x)=z^*S_\Psi\ket x$ for a complex number $z$. Since
> $A^\dagger = \begin{pmatrix} a^* & c^* \\ b^* & d^* \end{pmatrix}$, we have
> 
$$

> (A^\dagger\otimes\id_L)\ket{\phi_\theta} = a^*\cos\theta\ket{00} + c^*\sin\theta\ket{01}
> + b^*\cos\theta\ket{10} + d^*\sin\theta\ket{11} .
> 
$$

> Now substitute the expressions for $a,b,c,d$ in terms of the $x_{ij}$:
> \begin{align}
> S_\Psi \begin{pmatrix} x_{00} \\ x_{01} \\ x_{10} \\ x_{11} \end{pmatrix}
> \eqstep{1} \begin{pmatrix} x_{00}^* \\ \frac{\sin\theta}{\cos\theta} x_{10}^* \\
> \frac{\cos\theta}{\sin\theta} x_{01}^* \\ x_{11}^* \end{pmatrix}
> \eqstep{2} \begin{pmatrix} x_{00}^* \\ \tan\theta\, x_{10}^* \\ \cot\theta\, x_{01}^* \\ x_{11}^*
> \end{pmatrix} . \notag
> \end{align}
> **(1)** insert $a^*=x_{00}^*/\cos\theta$, $c^*=x_{10}^*/\cos\theta$, $b^*=x_{01}^*/\sin\theta$ and
> $d^*=x_{11}^*/\sin\theta$ into the four coefficients $a^*\cos\theta$, $c^*\sin\theta$, $b^*\cos\theta$ and
> $d^*\sin\theta$. The angles are real, so conjugation does not affect them.\quad
> **(2)** $\sin\theta/\cos\theta=\tan\theta$ and $\cos\theta/\sin\theta=\cot\theta$.
> Applying $S_\Psi$ twice gives back the original vector. For example, the second slot becomes
> $\tan\theta\,(\cot\theta\,x_{01}^*)^*=x_{01}$. So $S_\Psi^2 = \id$. Also $S_\Psi\ket{\phi_\theta} =
> \ket{\phi_\theta}$, because $\ket{\phi_\theta}$ is $(A\otimes\id_L)\ket{\phi_\theta}$ with $A=\id$, and
> $\id^\dagger=\id$.
> 
>
3. **The adjoint operator $F_\Psi \equiv S_\Psi^\dagger$.** For an antilinear operator, the adjoint is
> defined by $\braket{y|S_\Psi x} = \braket{x|F_\Psi y}$ for all vectors $\ket x,\ket y$. Writing out both
> sides in components and comparing gives
> 
$$

> F_\Psi \begin{pmatrix} y_{00} \\ y_{01} \\ y_{10} \\ y_{11} \end{pmatrix}
> = \begin{pmatrix} y_{00}^* \\ \cot\theta\, y_{10}^* \\ \tan\theta\, y_{01}^* \\ y_{11}^* \end{pmatrix} .
> 
$$

> 
>
4. **The modular operator $\Delta_\Psi = F_\Psi S_\Psi$.** Multiply the two operators:
> \begin{align}
> \Delta_\Psi \begin{pmatrix} x_{00} \\ x_{01} \\ x_{10} \\ x_{11} \end{pmatrix}
> \eqstep{1} F_\Psi \begin{pmatrix} x_{00}^* \\ \tan\theta\, x_{10}^* \\ \cot\theta\, x_{01}^* \\ x_{11}^*
> \end{pmatrix}
> \eqstep{2} \begin{pmatrix} x_{00} \\ \cot^2\theta\, x_{01} \\ \tan^2\theta\, x_{10} \\ x_{11} \end{pmatrix} .
> \notag
> \end{align}
> **(1)** apply $S_\Psi$ first, using the formula from item~2.\quad
> **(2)** apply $F_\Psi$ from item~3 to the vector
> $(y_{00},y_{01},y_{10},y_{11})=(x_{00}^*,\tan\theta\,x_{10}^*,\cot\theta\,x_{01}^*,x_{11}^*)$. The second slot
> becomes $\cot\theta\,y_{10}^*=\cot\theta\cdot\cot\theta\,x_{01}$. The third becomes
> $\tan\theta\,y_{01}^*=\tan\theta\cdot\tan\theta\,x_{10}$. The two complex conjugations cancel.
> 
> This is exactly the diagonal matrix found at the start,
> 
$$

> \Delta_\Psi = \operatorname{diag}(1, \cot^2\theta, \tan^2\theta, 1) .
> 
$$

> So the modular operator can be obtained from the Tomita operator alone, as
> $\Delta_\Psi=S_\Psi^\dagger S_\Psi$.
> 
>
5. **The modular conjugation $J_\Psi = S_\Psi \Delta_\Psi^{-1/2**$.} The positive square root of
> $\Delta_\Psi$ is
> 
$$

> \Delta_\Psi^{1/2} = \operatorname{diag}(1, \cot\theta, \tan\theta, 1) .
> 
$$

> Apply $S_\Psi$ to $\Delta_\Psi^{-1/2}\ket x$:
> \begin{align}
> J_\Psi \begin{pmatrix} x_{00} \\ x_{01} \\ x_{10} \\ x_{11} \end{pmatrix}
> \eqstep{1} S_\Psi \begin{pmatrix} x_{00} \\ \tan\theta\, x_{01} \\ \cot\theta\, x_{10} \\ x_{11}
> \end{pmatrix}
> \eqstep{2} \begin{pmatrix} x_{00}^* \\ x_{10}^* \\ x_{01}^* \\ x_{11}^* \end{pmatrix} . \notag
> \end{align}
> **(1)** $\Delta_\Psi^{-1/2}=\operatorname{diag}(1,\tan\theta,\cot\theta,1)$, the inverse of the square
> root just written.\quad
> **(2)** apply $S_\Psi$. The second slot becomes $\tan\theta\cdot(\cot\theta\,x_{10})^*=x_{10}^*$. The
> third becomes $\cot\theta\cdot(\tan\theta\,x_{01})^*=x_{01}^*$.
> So $J_\Psi$ conjugates every component and then exchanges $\ket{01} \leftrightarrow \ket{10}$. That exchange
> is the SWAP of the two qubits. $J_\Psi$ is antiunitary and satisfies $J_\Psi^2 = \id$. It also satisfies
> $J_\Psi \Delta_\Psi J_\Psi = \Delta_\Psi^{-1}$, because the swap exchanges the two diagonal entries
> $\cot^2\theta$ and $\tan^2\theta$.
> 
>
6. **Exact modular flow on Pauli matrices.** The modular flow of an observable $A \in B(\HH_R)$ is
> $\sigma_s(A) = \Delta_\Psi^{-is} (A\otimes\id_L) \Delta_\Psi^{is}$.
> 


> So on the qubit $R$, modular flow is an exact rotation of the Bloch sphere about the $z$-axis. The rotation
> angle is $-\alpha=2s\log\cot\theta$, so the angular frequency is the constant $2\log\cot\theta$. It is
> positive for $0<\theta<\pi/4$.
>



Two facts about $\Delta_\Psi$ deserve to be stated plainly. They are the two facts that carry over, unchanged
in spirit, to the fully general (type III) theory below.


1. $\Delta_\Psi\ket\Psi=\ket\Psi$, and also $\Delta_\Psi^{-1}\ket\Psi=\ket\Psi$. Equivalently,
$(K_R-K_L)\ket\Psi=0$. To see this in general, write the Schmidt decomposition
$\ket\Psi=\sum_n\sqrt{\lambda_n}\ket n_R\ket n_L$. Each term $\ket n_R\ket n_L$ is an eigenvector of $K_R$
with eigenvalue $-\log\lambda_n$, and of $K_L$ with the same eigenvalue, so $K_R-K_L$ annihilates it. In the
worked example, $\ket\Psi=\ket{\phi_\theta}=\cos\theta\ket{00}+\sin\theta\ket{11}$ is built entirely out of
the two eigenvectors of $\Delta_\Psi$ with eigenvalue $1$, so $\Delta_\Psi$ fixes it. Physically, modular flow
is an emergent, internal time evolution under which the state itself never changes. It still acts nontrivially
on operators in $R$ and in $L$. This fact is also the operator version of the elementary statement $S_R=S_L$
for a pure global state (Chapter~1). By the Schmidt decomposition, $\rho_R$ and $\rho_L$ have the same nonzero
eigenvalues, so $K_R$ and $K_L$ have the same spectrum. The equation $(K_R-K_L)\ket\Psi=0$ expresses this
symmetry as an operator statement.
2. Correlators of modular-flowed operators satisfy the KMS condition, which is made precise just below. This
is the mathematical signature of thermal equilibrium at $\beta=1$. An observer with access only to $R$ (or only
to $L$), who uses modular time as their clock, sees a thermal state.


### The swap operator $J_\Psi$

A third object will appear again and again, so it pays to build it explicitly now. Requiring both $\rho_R$ and
$\rho_L$ to be full-rank forces $\dim\HH_R=\dim\HH_L$. The reason is short. The number of nonzero Schmidt
coefficients of $\ket\Psi$ equals the rank of $\rho_R$, and it also equals the rank of $\rho_L$. If $\rho_R$ is
full-rank, this number is $\dim\HH_R$. If $\rho_L$ is full-rank, it is $\dim\HH_L$. So the two dimensions must
be equal. Because the dimensions match, we can build an explicit **swap operator**. Write the Schmidt
decomposition $\ket\Psi=\sum_n\sqrt{\lambda_n}\ket n_R\ket n_L$. Expand a general vector in the same Schmidt
basis, $\ket\phi=\sum_{mn}\phi_{mn}\ket m_R\ket n_L$. Define

$$

J_\Psi\ket\phi = \sum_{m,n}\phi_{mn}^*\ket n_R\ket m_L .

$$

This operator swaps the labels $R\leftrightarrow L$ *emph* complex-conjugates every coefficient. For the
two-qubit example it is exactly the $J_\Psi$ found in item~5 above. $J_\Psi$ is **antiunitary**: because
of the complex conjugation it is a different kind of map from an ordinary unitary, and it needs its own name.
It satisfies $J_\Psi^2=\id$, since swapping twice and conjugating twice gives back the starting vector. A
direct check shows $J_\Psi(A\otimes\id_L)J_\Psi=\id_R\otimes\bar A$, where $\bar A$ is the matrix of $A$ in
the Schmidt basis with every entry complex-conjugated. So conjugating an operator in $\M=B(\HH_R)\otimes\id_L$
by $J_\Psi$ produces an operator in $\M'=\id_R\otimes B(\HH_L)$. In other words, $J_\Psi$ exchanges the
subsystem with its complement at the level of operators, not just of vectors. It is called the
**modular conjugation operator**.

### The key limitation, and the reformulation that removes it

Everything above required $\rho_R$ and $\rho_L$ to be full-rank. This is a real restriction. Among other
things, it forces $\dim\HH_R=\dim\HH_L$, which already rules out many ordinary type I examples. It also says
nothing about type II, where there is no factorization $\HH_R\otimes\HH_L$ and the density operators of
Chapter~3 are of a different kind, or about type III, where there is no density operator at all. The strategy
now is to restate "$\rho_R$ and $\rho_L$ are full-rank" in a way that never mentions $\rho_R$ or $\rho_L$.
Then the condition can survive in a setting where those objects do not exist.

The restatement uses the two properties singled out at the end of Chapter~2's discussion of the GNS
construction: **cyclic** and **separating**. Recall the definitions. The vector $\ket\Psi$ is cyclic
with respect to $\M$ if $\{A\ket\Psi : A\in\M\}$ is dense in $\HH$. In words, the algebra can reach
essentially every vector, starting from $\ket\Psi$. The vector $\ket\Psi$ is separating with respect to $\M$
if $A\ket\Psi=0$ forces $A=0$. In words, no nonzero operator in $\M$ annihilates $\ket\Psi$. A short exercise
with the Schmidt decomposition shows two things. First, $\ket\Psi$ is cyclic for $\M=B(\HH_R)\otimes\id_L$
exactly when $\rho_L$ is full-rank. Second, $\ket\Psi$ is cyclic for the commutant $\M'=\id_R\otimes B(\HH_L)$
exactly when $\rho_R$ is full-rank. So "$\rho_R$ and $\rho_L$ are both full-rank" is *emph* to "$\ket\Psi$ is cyclic with respect to both $\M$ and $\M'$."

A further simplification is available. For any von Neumann algebra, $\ket\Psi$ is cyclic with respect to $\M'$
if and only if it is separating with respect to $\M$. (Cyclic for the complement is the same as separating
for the algebra itself.) So we never need to look at the two algebras separately. The whole condition becomes a
single statement about $\M$ alone: **$\ket\Psi$ is cyclic and separating with respect to $\M$.** This is
an important step in the logic. It shows once more that the relevant facts about bipartite entanglement can be
stated using the algebra of one side only, with no reference to the complement.

### The Tomita—Takesaki theorem, stated in full

Here is the theorem. It holds for *emph* von Neumann algebra $\M$ with a cyclic and separating vector
$\ket\Psi$. Its statement never mentions a trace, a density matrix, or a tensor factorization. This is exactly
why it survives into type III.


1. There is a positive operator $\Delta_\Psi$, still called the *emph*, that leaves
$\ket\Psi$ invariant: $\Delta_\Psi\ket\Psi=\ket\Psi$. The operator $K_\Psi\equiv-\log\Delta_\Psi$ generates an
automorphism of $\M$ (a map from $\M$ to itself that respects all of the algebra structure), and separately an
automorphism of $\M'$:
\begin{equation}
\sigma_s(A) \equiv \Delta_\Psi^{-is}A\Delta_\Psi^{is}\in\M\ \ \forall A\in\M,
\qquad
\sigma_s(A') \equiv \Delta_\Psi^{-is}A'\Delta_\Psi^{is}\in\M'\ \ \forall A'\in\M' .
\label{eq:modflow-auto}
\end{equation}
So at every modular time $s$, the flow stays inside the algebra it started in. This holds for $\M$ and for
$\M'$ separately.
2. There is an antiunitary **modular conjugation** $J_\Psi$. It satisfies $J_\Psi\ket\Psi=\ket\Psi$,
$J_\Psi=J_\Psi^{-1}=J_\Psi^\dagger$, $J_\Psi\Delta_\Psi J_\Psi=\Delta_\Psi^{-1}$, and
$J_\Psi\M J_\Psi=\M'$, $J_\Psi\M'J_\Psi=\M$. So $J_\Psi$ swaps $\M$ and $\M'$. This is the role the explicit
swap operator played in the type I example above, now established as a general fact.
3. There is a technical analyticity statement. It is included for completeness and is not needed for the
physics that follows. As a function of $s$, the vector $\Delta_\Psi^{-is}A\ket\Psi$ extends to complex values
of $s$ in the strip $0<\Im s<\tfrac12$. On the upper edge of that strip it satisfies
$\Delta_\Psi^{-i(t+i/2)}A\ket\Psi=\Delta_\Psi^{-it}J_\Psi A^\dagger\ket\Psi$.
4. Consider correlation functions of modular-flowed operators, $f_{AB}(s)\equiv\braket{\Psi|\sigma_s(A)B|\Psi}$.
They extend to analytic functions in the strip $-1<\Im s<0$, of width $1$, and satisfy the **KMS
relation**
\begin{equation}
f_{AB}(s) = f_{BA}(-s-i) .
\label{eq:kms}
\end{equation}
This is the precise mathematical statement of "looks thermal at $\beta=1$." It is the same
periodicity-in-imaginary-time relation that an ordinary thermal correlator $\Tr(e^{-\beta H}A(t)B)$ satisfies,
here with $\beta=1$. For an ordinary thermal state, the relation comes from the cyclic property of the trace
$\Tr(e^{-\beta H}\cdots)$. The KMS relation encodes that property without needing $e^{-\beta H}$ to exist as a
trace-class operator. That is exactly what is needed once there is no trace at all, as in type III.



> [!NOTE] **Physics Connection: KMS Condition in Thermal QFT**
> You have almost certainly met the KMS relation already, perhaps not by that name, in a course on
> finite-temperature quantum mechanics or statistical field theory. Before trusting it for a type III algebra with
> no Hamiltonian at all, let us check the same relation on an ordinary example. Take a two-level system,
> $H=\omega\ket1\!\bra1 = \begin{pmatrix} 0 & 0 \\ 0 & \omega \end{pmatrix}$, in the thermal (Gibbs) state
> 
$$

> \rho = \frac{e^{-\beta H}}{Z} = \frac{1}{1 + e^{-\beta\omega}}
> \begin{pmatrix} 1 & 0 \\ 0 & e^{-\beta\omega} \end{pmatrix} .
> 
$$

> The computation below in fact works for any Hamiltonian on a finite-dimensional space. For two operators
> $A, B$, define $f_{AB}(t) \equiv \Tr(\rho A(t) B)$, where $A(t) = e^{iHt} A e^{-iHt}$. Write
> $B(s)\equiv e^{iHs}Be^{-iHs}$ for the same flow applied to $B$. Substituting the imaginary time $s=-i\beta$
> gives $B(-i\beta)=e^{\beta H}Be^{-\beta H}$, an analytic continuation of the flow to imaginary time. Then:
> \begin{align}
> f_{AB}(t) &= \Tr\!\left( \frac{e^{-\beta H}}{Z}\, e^{iHt} A e^{-iHt} B \right) \notag\\
> &\eqstep{1} \Tr\!\left( B \, \frac{e^{-\beta H}}{Z}\, e^{iHt} A e^{-iHt} \right) \notag\\
> &\eqstep{2} \Tr\!\left( \frac{e^{-\beta H}}{Z} \left[ e^{\beta H} B e^{-\beta H} \right] e^{iHt} A e^{-iHt}
> \right) \notag\\
> &\eqstep{3} \Tr\big( \rho \, B(-i\beta) \, A(t) \big) \notag\\
> &\eqstep{4} \Tr\big( \rho \, e^{-iHt} B(-i\beta) e^{iHt} \, A \big) \notag\\
> &\eqstep{5} \Tr\big( \rho \, B(-t - i\beta) \, A \big) \ =\ f_{BA}(-t - i\beta) . \notag
> \end{align}
> **(1)** cyclicity of the ordinary matrix trace, moving $B$ to the front.\quad
> **(2)** insert $\id=e^{-\beta H}e^{\beta H}$ in front of $B$. This changes nothing, since it is the
> identity, but it sets up the next step.\quad
> **(3)** $e^{-\beta H}/Z=\rho$, the bracket is $B(-i\beta)$, and $e^{iHt}Ae^{-iHt}=A(t)$ by definition.\quad
> **(4)** cyclicity again: move the factor $e^{-iHt}$ at the right end of $A(t)$ around to the front, then
> use that $\rho$ commutes with $e^{-iHt}$ (both are functions of $H$).\quad
> **(5)** the group property of the flow, $e^{-iHt}B(-i\beta)e^{iHt}=B(-t-i\beta)$: flowing by $-i\beta$ and
> then by $-t$ is the same as flowing by $-t-i\beta$. The last equality is the definition of $f_{BA}$.
> 
> This algebraic proof uses only the cyclicity of the trace and the group property of the flow. It shows why
> thermal correlators are periodic in imaginary time, with period $\beta$. Tomita—Takesaki theory takes this
> exact property as the definition of a thermal state at $\beta=1$. It needs no trace and no Hamiltonian.
> 
> So what changed between this ordinary example and the general Tomita—Takesaki statement? Only this. Here the
> flow generating $A(t)$ came from an honest Hamiltonian $H$, and $\rho$ was a normalizable density matrix that you
> could write down as a finite matrix. In the general theorem, neither needs to exist. The flow $\sigma_s$ can be
> generated by no Hamiltonian that lives in $\M$. This is exactly the defining property of type III, given by the
> inner-automorphism criterion \eqref{eq:inner-criterion} below. There may also be no $\rho$ from which to build
> a trace. The KMS relation \eqref{eq:kms} survives all of this unchanged. It was never really a statement about
> $H$ or $\rho$ separately. It is a statement about the correlator $f_{AB}$ alone. That is why the general theory
> takes the KMS relation, rather than the Hamiltonian or the density matrix, as the basic object.


Read physically, the theorem says the following. *emph* operator algebra with a cyclic and separating
reference vector comes with a canonical, built-in notion of time flow. Under this flow, the reference state
looks exactly thermal at inverse temperature $1$. This holds whether or not $\M$ has a trace. So the type I
story above is not being generalized by analogy. It is included as the special case in which the canonical
flow is generated by an honest Hamiltonian $K_R$ that lives inside $\M$ itself.

Several remarks complete the theorem:

- [(a)] Physically: given $\M$ and a cyclic and separating $\ket\Psi$, there is an emergent time evolution,
internal to $\M$ (or to $\M'$), that leaves $\ket\Psi$ fixed. Relative to this time, an observer confined to
$\M$ (or to $\M'$) feels a temperature $1/\beta=1$.
- [(b)] For type I, the cyclic and separating condition was a real restriction, since it forced
$\dim\HH_R=\dim\HH_L$. For the type III situations that matter most in these notes, namely quantum field theory
and statistical mechanics in the thermodynamic limit, the condition holds very widely. You will see this
explicitly later in this chapter, in the $N\to\infty$ entangled-spin construction and in the Reeh—Schlieder
theorem.
- [(c)] The theorem is usually *emph*, not just stated, by first defining an antilinear
**Tomita operator** $S_\Psi$ directly from $\M$ and $\ket\Psi$:

$$

S_\Psi A\ket\Psi = A^\dagger\ket\Psi\ \ (A\in\M), \qquad
S_\Psi^2=\id, \qquad S_\Psi\ket\Psi=\ket\Psi .

$$

Its adjoint $F_\Psi=S_\Psi^\dagger$ does the same job for the commutant:

$$

F_\Psi A'\ket\Psi = A'^\dagger\ket\Psi\ \ (A'\in\M') .

$$

(In the two-qubit worked example one can check directly that it is $F_\Psi$, not $S_\Psi$, that acts this way
on vectors $A'\ket\Psi$; the two operators differ unless $\theta=\pi/4$.) The operator $S_\Psi$ is well
defined precisely because $\ket\Psi$ is separating. If $A\ket\Psi=B\ket\Psi$, then $(A-B)\ket\Psi=0$, so
$A=B$, and therefore $A^\dagger\ket\Psi=B^\dagger\ket\Psi$. This is the same role the separating property played
in the GNS construction of Chapter~2. One then takes the **polar decomposition**
$S_\Psi=J_\Psi\Delta_\Psi^{1/2}$, with $\Delta_\Psi=S_\Psi^\dagger S_\Psi$. This is the operator analogue of
writing a complex number as $z=e^{i\phi}|z|$: an antiunitary "phase" $J_\Psi$ times a positive "modulus"
$\Delta_\Psi^{1/2}$. Every statement of the theorem is then derived from this one definition. The derivation is
a technical piece of functional analysis and is not reproduced here. What matters is that the whole
construction starts from this one simple map.
- [(d)] There is a converse, which is used to *emph* the modular operator in physical examples,
including the Rindler-wedge computation later in this chapter. Suppose you find a one-parameter group of
unitaries that leaves $\ket\Psi$ invariant, maps $\M$ to itself in the sense of \eqref{eq:modflow-auto}, and
whose flow satisfies the KMS relation \eqref{eq:kms}. Then it *emph* the modular flow $\Delta_\Psi^{-is}$
for $\ket\Psi$. Only one flow has these properties. So finding one by any means is enough, whether by a
physical argument, a symmetry, or a guess that is later checked.
- [(e)] If $\M$ is type II, the density operators $\rho_\M\in\M$ and $\rho_{\M'}\in\M'$ of Chapter~3 exist.
Then $\Delta_\Psi$ can still be built as in \eqref{eq:Delta-typeI}, with $\rho_\M,\rho_{\M'}$ in place of
$\rho_R,\rho_L$. The tensor product is replaced by an ordinary product of these two commuting operators,
$\Delta_\Psi=\rho_\M\rho_{\M'}^{-1}$. If $\ket\Psi$ is the tracial state itself (so
$\rho_\M=\rho_{\M'}=\id$), then $\Delta_\Psi=\id$. This matches the worked example above at $\theta=\pi/4$.
- [(f)] If $\M$ is type III, $\Delta_\Psi$ cannot be split into a piece from $\M$ and a piece from $\M'$ at
all, because there is no $\rho_\M$. $\Delta_\Psi$ still exists, by the theorem above, but it is now a single
joint object with no factorized description.


Finally, one lemma does real work starting in Chapter~7. It is the mechanism that lets entanglement-wedge
reconstruction go strictly beyond causal-wedge reconstruction.

\begin{quote}
**Lemma (an "ergodic" property of modular flow).** Let $\N\subset\mathcal X$ be two von Neumann
algebras, and let $\ket\Psi$ be cyclic and separating for both. Apply the modular flow $\sigma_s$ of the
*emph* algebra $\mathcal X$ to the *emph* algebra $\N$. The result regenerates all of
$\mathcal X$: $\{\sigma_s(A):A\in\N, s\in\mathbb R\}''=\mathcal X$.
\end{quote}
In words: flow a small piece of an algebra in modular time, using the larger algebra's own modular clock, and
you sweep out the entire larger algebra. This may sound too strong to be true. It follows from a theorem of
Takesaki. That theorem says that a subalgebra of $\mathcal X$ that is mapped into itself by the modular flow
of $\mathcal X$, and for which $\ket\Psi$ is still cyclic, must be all of $\mathcal X$. The algebra generated by
all the $\sigma_s(A)$ is such a subalgebra. It contains $\N$, so $\ket\Psi$ is cyclic for it.

## Classification of type III factors

### Telling type III apart from type I and II, using modular flow alone

Here is a clean, checkable criterion. It was met briefly in Chapter~2's discussion of inner automorphisms, and
it is now established as the actual dividing line between the types:
\begin{equation}
\sigma_s \text{ is an inner automorphism of } \M \text{ for *emph* } s\in\mathbb R
\qquad \iff \qquad \M \text{ is type I or type II} .
\label{eq:inner-criterion}
\end{equation}
Here $\sigma_s$ is an **inner automorphism** if there is a unitary $U_s$ that belongs to $\M$ itself (not
just some unitary on $\HH$) and implements the flow: $\sigma_s(A)=U_sAU_s^\dagger$. For type I, this holds with
$U_s=\rho_R^{-is}=e^{iK_Rs}$. For type II it holds with the analogous operator built from $\rho_\M$. This is
the ordinary type I story from earlier in this chapter, now described as "the flow is inner." Now read
\eqref{eq:inner-criterion} in the other direction. **For a type III algebra, there must be *emph* This gives a
practical definition of type III: modular time flows, but no clock that generates the flow can be found inside
the algebra being flowed.

### State-independence: relating the flows of different reference vectors

The modular operator $\Delta_\Psi$, and hence the flow $\sigma_s^\Psi$, depends on the choice of the cyclic and
separating reference vector $\ket\Psi$. A different choice $\ket\Omega$ gives a different $\Delta_\Omega$ and a
different flow $\sigma_s^\Omega$. A reassuring theorem, due to Connes, says that these flows are never wildly
unrelated. There is a family of unitaries $u_{\Psi\Omega}(s)\in\M$, one for each $s$, relating the two:
\begin{equation}
\sigma_s^\Psi(A) = u_{\Psi\Omega}(s)\,\sigma_s^\Omega(A)\,u_{\Psi\Omega}(s)^\dagger, \qquad \forall A\in\M .
\label{eq:cocycle}
\end{equation}
So modular flows for different reference states differ only by an inner automorphism, never by anything more
drastic. These unitaries also obey a chain rule through a third vector $\Phi$,
$u_{\Psi\Omega}(t)u_{\Omega\Phi}(t)=u_{\Psi\Phi}(t)$. This is what one wants if "relating two flows" is to be
a consistent notion.

This result lets us define two **state-independent** invariants of the algebra $\M$ itself. They are sets
of numbers that depend only on $\M$, not on the reference vector used to compute them. That is exactly why they
are useful for *emph* algebras rather than states. The first is

$$

T(\M) \equiv \{t\in\mathbb R : \sigma_t^\Psi \text{ is inner on } \M\} .

$$

It does not depend on $\Psi$, by \eqref{eq:cocycle}: composing with an inner automorphism does not change
whether a map is inner. The second is
\begin{equation}
S(\M) \equiv \bigcap_\Psi \sigma(\Delta_\Psi) \subset \mathbb R_{\ge0} ,
\label{eq:connes-S}
\end{equation}
where $\sigma(\Delta_\Psi)$ denotes the spectrum of $\Delta_\Psi$. It is the intersection, over *emph*
cyclic and separating reference vector, of the spectrum of the corresponding modular operator. Whatever
survives this intersection is a property of $\M$ alone. These are **Connes' two fundamental invariants**.
By \eqref{eq:inner-criterion}, $T(\M)=\mathbb R$ for type I and type II, since every modular time is inner.
For type III, $T(\M)$ is a proper subgroup of $\mathbb R$. (For the type III examples below it is a discrete
set.) For type I or type II, $S(\M)=\{1\}$. The reason is that there is a tracial reference for which
$\Delta=\id$, whose spectrum is the single point $\{1\}$. For the $\mathrm{I}_\infty$ and $\mathrm{II}_\infty$
cases the trace is not a normalizable state. The precise definition of $S(\M)$ therefore takes the
intersection over a slightly larger class of reference functionals (called weights), which includes the trace.

For a type III factor, Connes proved that $S(\M)$ with the point $0$ removed is a closed multiplicative
subgroup of $\mathbb R_{>0}$. This is a hard theorem and is not re-derived here. The closed subgroups of
$\mathbb R_{>0}$ are $\{1\}$, the powers $\lambda^{\mathbb Z}$ of a single number, and all of $\mathbb R_{>0}$.
So there are exactly three possibilities, and no others:
\begin{gather}
\text{Type III}_0:\ S(\M)=\{0,1\}, \qquad
\text{Type III}_\lambda:\ S(\M)=\{0\}\cup\{\lambda^n : n\in\mathbb Z\},\ \lambda\in(0,1), \notag\\
\text{Type III}_1:\ S(\M)=\mathbb R_{\ge0} .
\label{eq:typeIII-classes}
\end{gather}
This is as fine as the classification gets. Every physically relevant type III algebra in the rest of these notes
is one of these three.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.95\textwidth]{figs/fig_connes_spectrum.pdf}
\caption{Connes' invariant $S(\M)$ for each kind of factor, drawn as a set of points on the half-line
$\mathbb R_{\ge0}$ (dashed guides mark $0$ and $1$). Types I and II give the single point $1$, and type
$\mathrm{III}_0$ gives the two points $0$ and $1$. Type $\mathrm{III}_\lambda$ gives $0$ together with every
integer power of $\lambda$ (drawn for $\lambda=1/2$), and these powers pile up at $0$. Type $\mathrm{III}_1$
fills the whole half-line.}
\label{fig:connes_spectrum}
\end{figure}

The unitaries $u_{\Psi\Omega}(s)$ have further technical properties. They satisfy a so-called cocycle
identity. Conversely, any family of unitaries satisfying that identity comes from some other reference state
(more precisely, from a weight). These facts serve later as machinery rather than as physical content, so they
are only mentioned here.

## The entangled spin example revisited

We can now compute $S(\M_\theta)$ and $T(\M_\theta)$ explicitly, by hand, for the algebra
$\M_\theta\equiv\M_R(\theta)$ of the infinite chain of entangled spin pairs from Chapter~2. We will find that
different values of $\theta$ give different type $\mathrm{III}_\lambda$ subtypes.

### Setting up the finite-$N$ computation

At finite $N$, the algebra of the $R$ system is an ordinary type I algebra. The reduced density matrices are
$N$-fold tensor products of the single-pair result from Chapter~1:

$$

\rho_R(\Phi_\theta) = \rho_r(\phi_\theta)^{\otimes N}, \qquad
\rho_r(\phi_\theta) = \begin{pmatrix}\cos^2\theta&0\\0&\sin^2\theta\end{pmatrix}.

$$

The same holds for $\rho_L$, since each pair is symmetric between $R$ and $L$. For $\theta\in(0,\pi/4)$ both
are strictly positive (full rank, since every diagonal entry is nonzero). So $\ket{\Phi_\theta}$ is cyclic and
separating with respect to the $R$-algebra at every finite $N$, and the modular operator can be built directly
from \eqref{eq:Delta-typeI}:
\begin{align}
\Delta_{\Phi_\theta} = \rho_R(\Phi_\theta)\otimes\rho_L(\Phi_\theta)^{-1} \eqstep{1} \delta_\theta^{\otimes N},
\qquad \delta_\theta \equiv \rho_r(\phi_\theta)\otimes\rho_l(\phi_\theta)^{-1} . \notag
\end{align}
**(1)** $\rho_R$ and $\rho_L^{-1}$ are both $N$-fold tensor products. Regroup the factors pair by pair,
with the $i$-th $r$ factor next to the $i$-th $l$ factor. The whole operator is then the $N$-fold tensor power
of the single-pair operator $\delta_\theta$.

The single-pair operator $\delta_\theta$ is exactly the modular operator of the two-qubit worked example
earlier in this chapter. Its eigenvalues were computed there: $1$ (twice), $\lambda$ and $\lambda^{-1}$, with
$\lambda=\tan^2\theta$. The $N$ pairs are independent, identical copies. So the eigenvalues of the full
$\Delta_{\Phi_\theta}$ are all possible products,
\begin{equation}
\bigotimes_{i=1}^N(1,\lambda,\lambda^{-1}) = \prod_{i=1}^N\lambda^{\alpha_i}, \qquad \alpha_i\in\{0,1,-1\} .
\label{eq:powers-eigs}
\end{equation}
Each of the $N$ pairs independently contributes a factor $1$, $\lambda$ or $\lambda^{-1}$ to the product, and
every combination of choices appears as an eigenvalue.

### Taking $N\to\infty$, and reading off the type

The eigenvalue \eqref{eq:powers-eigs} depends only on the exponent $n=\sum_i\alpha_i$, where each term is $0$
or $\pm1$. As $N\to\infty$, every integer $n$ becomes achievable, each with a growing multiplicity. So the
eigenvalues are the numbers $\lambda^n$ with $n\in\mathbb Z$, and the spectrum is
\begin{equation}
\sigma(\Delta_{\Phi_\theta}) = \{0\}\cup\{\lambda^n : n\in\mathbb Z\} .
\label{eq:powers-spec}
\end{equation}
The point $\{0\}$ appears because the spectrum is a closed set. Since $0<\lambda<1$, the eigenvalues $\lambda^n$
come arbitrarily close to zero as $n\to+\infty$ (choose more and more $\alpha_i=+1$). The eigenvalue $0$
itself is never reached. It is a limit point, and the spectrum includes all its limit points. The keyresult
below makes this infinite-$N$ statement precise.

\begin{keyresult}[: Spectral Derivation of the Connes Invariant for the Powers Factor]
**Goal:** Show that for the infinite entangled spin chain $\M_\theta$ with $\theta \in (0, \pi/4)$ and
$\lambda = \tan^2\theta$,

$$

\begin{aligned}
\mathrm{Spec}(\Delta_{\Phi_\theta}) &= \{0\} \cup \{\lambda^n : n \in \mathbb{Z}\}, \\
S(\M_\theta) \equiv \bigcap_{\Psi} \mathrm{Spec}(\Delta_\Psi) &= \{0\} \cup \lambda^{\mathbb{Z}} .
\end{aligned}

$$

Steps 1 and 2 are a complete computation of the first line. Step 3 is a sketch of the second line, which rests
on a theorem quoted from the literature.

**Derivation:**

1. **Action on the local GNS basis.**
The GNS Hilbert space $\HH_\theta$ is the completion of the span of local excitations of $\ket{\Phi_\theta}$:

$$

\ket{\Psi_{\{a_k\}}} \equiv \big(a_1 \otimes a_2 \otimes \cdots \otimes a_m \otimes \id \otimes \cdots\big)
\ket{\Phi_\theta} .

$$

Expand each single-site $2\times2$ matrix in the standard basis $\{e_{00}, e_{01}, e_{10}, e_{11}\}$, where
$e_{ij} \equiv \ket{i}\bra{j}$. Use the Tomita operator $S_\phi (a\ket\phi) = a^\dagger\ket\phi$ on a single
pair $\ket\phi = \cos\theta\ket{00} + \sin\theta\ket{11}$:
\begin{align}
S_\phi (e_{00}\ket\phi) = S_\phi (\cos\theta\ket{00}) &\eqstep{1} e_{00}^\dagger\ket\phi \eqstep{2}
e_{00}\ket\phi = \cos\theta\ket{00} , \notag\\
S_\phi (e_{11}\ket\phi) = S_\phi (\sin\theta\ket{11}) &\eqstep{1} e_{11}^\dagger\ket\phi \eqstep{2}
e_{11}\ket\phi = \sin\theta\ket{11} , \notag\\
S_\phi (e_{01}\ket\phi) = S_\phi (\sin\theta\ket{01}) &\eqstep{1} e_{01}^\dagger\ket\phi \eqstep{2}
e_{10}\ket\phi = \cos\theta\ket{10} , \notag\\
S_\phi (e_{10}\ket\phi) = S_\phi (\cos\theta\ket{10}) &\eqstep{1} e_{10}^\dagger\ket\phi \eqstep{2}
e_{01}\ket\phi = \sin\theta\ket{01} . \notag
\end{align}
**(1)** the defining property of the Tomita operator, $S_\phi(a\ket\phi)=a^\dagger\ket\phi$.\quad
**(2)** $e_{00}$ and $e_{11}$ are Hermitian, while $e_{01}^\dagger=e_{10}$ and $e_{10}^\dagger=e_{01}$.

$S_\phi$ is antilinear and the angles are real. So the last two lines say $S_\phi\ket{01}=\cot\theta\ket{10}$
and $S_\phi\ket{10}=\tan\theta\ket{01}$. This is exactly the $4\times4$ Tomita operator found in the worked
example earlier in this chapter. Computing the adjoint $S_\phi^\dagger$ and the modular operator
$\delta_\theta = S_\phi^\dagger S_\phi = \rho_r \otimes \rho_l^{-1}$ on this basis gives four exact
eigenvectors:

$$

\delta_\theta (e_{00}\ket\phi) = 1 \cdot (e_{00}\ket\phi), \qquad
\delta_\theta (e_{11}\ket\phi) = 1 \cdot (e_{11}\ket\phi),

$$


$$

\begin{aligned}
\delta_\theta (e_{10}\ket\phi) &= \tan^2\theta \cdot (e_{10}\ket\phi) = \lambda \cdot (e_{10}\ket\phi), \\
\delta_\theta (e_{01}\ket\phi) &= \cot^2\theta \cdot (e_{01}\ket\phi) = \lambda^{-1} \cdot (e_{01}\ket\phi) .
\end{aligned}

$$

2. **Eigenvalue spectrum on the infinite chain.**
Consider a product excitation $\ket\Psi$ in which $n_+$ sites carry the factor $e_{10}$, $n_-$ sites carry
$e_{01}$, and all other sites carry $e_{00}$, $e_{11}$ or $\id$. The modular operator acts site by site, so

$$

\Delta_{\Phi_\theta} \ket{\Psi} = \lambda^{n_+ - n_-} \ket{\Psi} = \lambda^n \ket{\Psi},
\qquad n = n_+ - n_- \in \mathbb{Z} .

$$

The numbers $n_+$ and $n_-$ can be any non-negative integers. So the set of eigenvalues is exactly the
geometric progression $\{\lambda^n : n \in \mathbb{Z}\}$. These eigenvectors span a dense subspace of
$\HH_\theta$, so the spectrum is the closure of this set. Since $\lambda \in (0, 1)$, we have
$\lambda^n \to 0$ as $n \to +\infty$. So $0$ is an accumulation point and belongs to the spectrum:

$$

\mathrm{Spec}(\Delta_{\Phi_\theta}) = \{0\} \cup \{\lambda^n : n \in \mathbb{Z}\} .

$$

3. **Independence of the reference state (sketch).**
Why does the intersection over all states not shrink this set? Let $\ket\Psi$ be any other cyclic and
separating vector. By Connes' theorem \eqref{eq:cocycle}, the two modular flows are related by unitaries
$u_t\in\M_\theta$:

$$

\sigma_t^\Psi(A) = u_t \,\sigma_t^{\Phi_\theta}(A)\, u_t^\dagger .

$$

The algebra $\M_\theta$ is an infinite tensor product of finite type I factors (an "ITPFI" factor; this
particular one is called a Powers factor). Any normal state on it can be approximated in norm by states that
differ from $\Phi_\theta$ only on finitely many sites $1, \dots, K$. On the infinite tail $k > K$, such a state
is identical to $\Phi_\theta$. Heuristically, its modular operator then factorizes as

$$

\Delta_\Psi \approx \Delta_{\Psi,\text{local}} \otimes \bigotimes_{k=K+1}^\infty \delta_\theta^{(k)} ,

$$

and the infinite tail still produces all the eigenvalues $\lambda^n$. The precise version is a theorem.
Araki and Woods defined an invariant of such infinite tensor products, the asymptotic ratio set, that is built
only from the tail of the chain. Connes later showed that it equals $S(\M)$ for these algebras. For the Powers
factor it equals $\{0\}\cup\lambda^{\mathbb Z}$. Hence

$$

S(\M_\theta) \equiv \bigcap_{\Psi} \mathrm{Spec}(\Delta_\Psi) = \{0\} \cup \{\lambda^n : n \in \mathbb{Z}\}
= \{0\} \cup \lambda^{\mathbb{Z}} .

$$

Comparing with Connes' classification, $\M_\theta$ is a **type $\mathrm{III**_\lambda$} factor with
$\lambda = \tan^2\theta$. $\blacksquare$

\end{keyresult}

The spectrum \eqref{eq:powers-spec} belongs to *emph* reference vector, $\ket{\Phi_\theta}$. The
Connes invariant $S(\M_\theta)$ needs the intersection over *emph* cyclic and separating reference
vector, as in \eqref{eq:connes-S}. The Araki—Woods—Connes result quoted in step~3 says that for this example
the intersection is the same set \eqref{eq:powers-spec}. Now compare with the three-way classification
\eqref{eq:typeIII-classes}. The set $\{0\}\cup\{\lambda^n\}$ with $\lambda=\tan^2\theta\in(0,1)$ is exactly the
signature of **type $\mathrm{III**_\lambda$}. **So $\M_\theta$ is type $\mathrm{III**_{\tan^2\theta}$,
for every $\theta\in(0,\pi/4)$.} Different entangling angles produce different, inequivalent von Neumann
algebras.

The other Connes invariant, $T(\M_\theta)$, can also be read off from \eqref{eq:powers-eigs}. The operator
$\Delta_{\Phi_\theta}^{it}$ equals $1$ exactly when $\lambda^{int}=1$ for every eigenvalue at once, that is,
when $t\log\lambda\in2\pi\mathbb Z$. At those times the flow does nothing, so it is trivially inner,
implemented by the identity. This holds at every finite $N$, and hence also in the $N\to\infty$ limit. One can
show that no other values of $t$ give an inner flow; this part is quoted, not proved here. The result is

$$

T(\M_\theta) = \left\{\frac{2\pi n}{\log\lambda} : n\in\mathbb Z\right\}, \qquad \lambda=\tan^2\theta .

$$

This is a discrete proper subgroup of $\mathbb R$. It is not all of $\mathbb R$, as the type III criterion
\eqref{eq:inner-criterion} requires.

### The endpoints, and how to reach $\mathrm{III}_0$ and $\mathrm{III}_1$ too

Two special values of $\theta$ need to be reconciled with all this. At $\theta=\pi/4$, Chapter~3 already showed
that the algebra is type $\mathrm{II}_1$, not type III. Indeed $\lambda=\tan^2(\pi/4)=1$ here. This sits just
outside the range $\lambda\in(0,1)$ of type $\mathrm{III}_\lambda$, consistent with this being a different type,
one that has a trace and is easier to handle (Chapter~3). At $\theta=0$, the two spins in each pair are not
entangled at all. The $N\to\infty$ construction then never leaves ordinary type I, because there is no
entanglement to produce anything new.

Can type $\mathrm{III}_0$ and type $\mathrm{III}_1$ be reached from a variant of the same family? Yes. Seeing
how shows that the classification is sensitive to fine details of *emph* the infinite limit is taken, not
just to a single overall parameter. Instead of using the same $\theta$ for every pair, give the $i$-th pair its
own angle $\theta_i$. Then $\lambda_i=\tan^2\theta_i$ can vary from pair to pair. The eigenvalue formula
\eqref{eq:powers-eigs} becomes $\prod_i\lambda_i^{\alpha_i}$. What happens in the $N\to\infty$ limit now depends
on the *emph* of the whole sequence $\{\lambda_i\}$, not on any single number. Araki and
Woods worked out the answer. Stated roughly, it is as follows. If every $\lambda_i$ equals the same
$\lambda\in(0,1)$, one gets type $\mathrm{III}_\lambda$; this is the case just worked out. If $\lambda_i\to0$
fast enough that $\sum_i\lambda_i$ is finite, one gets an ordinary type $\mathrm{I}_\infty$ algebra. The
entanglement dies off so quickly that nothing new happens in the limit. If $\lambda_i\to0$ more slowly, one
gets a type III algebra, and type $\mathrm{III}_0$ can arise this way. Finally, sequences that do not settle
down to a single value typically give type $\mathrm{III}_1$, the "most chaotic" member of the family. A
simple example is a sequence that keeps returning to two values whose logarithms have an irrational ratio.

There is a second way to build type $\mathrm{III}_1$ directly. It will return, in a quite different physical
form, when the Rindler wedge is discussed in the next section. Instead of qubits, use pairs of *emph*
(three-level systems, such as spin-$1$) in an entangled state. The single-pair reduced density matrix is then a
$3\times3$ diagonal matrix, $\rho_r=\tfrac{1}{1+\lambda+\tilde\lambda}\,\mathrm{diag}(1,\lambda,\tilde\lambda)$,
with two independent parameters $\lambda,\tilde\lambda>0$. The single-pair modular eigenvalues are the ratios of
these entries. So in the $N\to\infty$ limit the modular eigenvalues are all products $\lambda^n\tilde\lambda^m$
with integers $n,m$. Suppose the ratio $\log\lambda/\log\tilde\lambda$ is irrational, which is the generic
case. Then these products are dense in all of $\mathbb R_{\ge0}$, so $\sigma(\Delta_\Psi)=\mathbb R_{\ge0}$. By
the same Araki—Woods—Connes argument, $S(\M)=\mathbb R_{\ge0}$, which is type $\mathrm{III}_1$ again. This
time the result comes not from varying $\theta_i$ from pair to pair, but from two incommensurate
"frequencies," $\log\lambda$ and $\log\tilde\lambda$, built into a single repeated building block.

## Local algebras in a relativistic quantum field theory

### The Rindler wedge, and why the modular flow is a boost

Now return to the third example of Chapter~1. There, a relativistic quantum field theory in
$1{+}1$-dimensional Minkowski space, with coordinates $(t,x)$, was cut in half at the surface $x=0$. Chapter~1
showed that the vacuum state $\ket\Omega$ has infinite entanglement across this cut, so no tensor factorization
exists. In the language now available, we describe this entanglement through the algebra $\M_R$ of operators
localized in the right region $R=\{x>0\}$.

One geometric fact is used constantly from here on, so we state it explicitly. In a relativistic theory, time
evolution is causal: nothing propagates faster than light. So $\M_R$, built from operators localized at $x>0$ at
a single instant, is the same as the algebra of operators localized anywhere in the *emph*
$\widehat R$ of that region (the notion from Chapter~1). For the half-line $x>0$, the domain of dependence is
the **right Rindler wedge**, $\{(t,x): x>|t|\}$. It is everything that data on the initial slice $x>0$
determines completely, both to the future and to the past. Causality alone gives $\M_L\subseteq\M_R'$: operators
in the left wedge commute with those in the right wedge. For wedges the stronger statement
$\M_R' = \M_L = \M_{\widehat L}$ also holds. The commutant is exactly the algebra of the causally complementary
(left) wedge, with no gap between them. This equality is known as wedge duality, and it follows from the
Bisognano—Wichmann theorem discussed below.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.82\textwidth]{figs/fig_rindler.pdf}
\caption{The Rindler wedges. The light cone through the origin (dot) splits Minkowski spacetime into the right
wedge $R$ ($x>|t|$, blue), the left wedge $L$ ($x<-|t|$, gold), the future $F$ and the past $P$. The curves are
the hyperbolae $x^2-t^2=\rho^2$ (the bar marks $\rho$ for one of them), worldlines of uniformly accelerated
observers with proper acceleration $a=1/\rho$ and proper time $\tau=\rho\eta$, where $\eta$ is the boost
parameter. The red arrows show which way a boost that increases $\eta$ moves points: toward the future in $R$ and
toward the past in $L$.}
\label{fig:rindler}
\end{figure}

The **Reeh—Schlieder theorem**, stated here and sketched below, says the following. In a relativistic
quantum field theory, act on the vacuum $\ket\Omega$ with operators localized in *emph* open spacetime
region, however small. The resulting set of states is dense in the entire Hilbert space.

\begin{keyresult}[: Derivation of the Reeh—Schlieder Theorem]
**Theorem:** Let $\mathcal{O} \subset \mathbb{R}^{1,d-1}$ be a nonempty open region in Minkowski
spacetime. Let $\M(\mathcal{O})$ be the local von Neumann algebra generated by fields smeared with test
functions supported in $\mathcal{O}$. In any relativistic QFT satisfying the Wightman axioms:

1. $\ket\Omega$ is **cyclic** for $\M(\mathcal{O})$: $\overline{\M(\mathcal{O})\ket\Omega} = \HH$.
2. If the causal complement of $\mathcal O$ contains a nonempty open region (as it does for any bounded
region, and for a wedge), then $\ket\Omega$ is also **separating** for $\M(\mathcal{O})$:
$A\ket\Omega = 0 \implies A = 0$ for all $A \in \M(\mathcal{O})$.


**Proof sketch** (treating the fields as if they were defined at points, a standard shortcut):

1. **Orthogonality hypothesis.**
To prove cyclicity, suppose some state $\ket\chi \in \HH$ is orthogonal to $\M(\mathcal{O})\ket\Omega$:

$$

\braket{\chi | A | \Omega} = 0 \qquad \text{for all } A \in \M(\mathcal{O}) .

$$

Consider field states $\phi(x_1)\cdots\phi(x_n)\ket\Omega$ with all points $x_j$ in $\mathcal O$. Use
translation covariance, $\phi(x) = e^{i P_\mu x^\mu} \phi(0) e^{-i P_\mu x^\mu}$, and translation invariance of
the vacuum, $P_\mu\ket\Omega = 0$. Define the function

$$

F(x_1, \dots, x_n) \equiv \braket{\chi | \phi(x_1)\phi(x_2)\cdots\phi(x_n)|\Omega} .

$$

2. **Relativistic spectrum condition and analyticity.**
Change to the difference coordinates $\xi_j \equiv x_j - x_{j+1}$ ($j = 1, \dots, n-1$). Inserting the
translation formula and using $e^{-iP\cdot x_n}\ket\Omega=\ket\Omega$ gives

$$

F = \Braket{\chi \Big| e^{iP\cdot x_1}\phi(0) e^{-i P \cdot \xi_1} \phi(0) e^{-i P \cdot \xi_2}
\cdots e^{-i P \cdot \xi_{n-1}} \phi(0) \Big| \Omega} .

$$

By the relativistic spectrum condition, the joint spectrum of the energy-momentum operator
$P^\mu = (H, \vec P)$ lies in the closed forward lightcone:

$$

\mathrm{Spec}(P^\mu) \subseteq \bar V^+ = \{p^\mu : p^0 \ge |\vec p|\} .

$$

Now continue the differences into the complex domain:

$$

\xi_j \longrightarrow \zeta_j = \xi_j - i \eta_j, \qquad \eta_j \in V^+ \quad (\eta_j^0 > |\vec \eta_j|) .

$$

On a state with four-momentum $p \in \bar V^+$, the exponent becomes

$$

-i p \cdot (\xi_j - i \eta_j) = -i p \cdot \xi_j - p \cdot \eta_j .

$$

For $p \in \bar V^+$ and $\eta_j \in V^+$, the Lorentzian inner product
$p \cdot \eta_j = p^0 \eta_j^0 - \vec p \cdot \vec\eta_j$ is non-negative (and strictly positive unless
$p=0$). So the factor $e^{-p \cdot \eta_j}$ is at most $1$. It damps high momenta, which keeps the operator
product bounded and makes it depend holomorphically on the $\zeta_j$. The same argument applies to $x_1$,
continued to $x_1+i\eta_0$ with $\eta_0\in V^+$. Therefore $F$ is holomorphic in a tube domain $\mathcal T$:
the set of complex arguments whose imaginary parts lie in these forward cones.
3. **Edge-of-the-wedge theorem and global vanishing.**
By assumption, the boundary value $F(x_1, \dots, x_n)$ vanishes when all $x_j \in \mathcal{O}$. The set of
such real points is a nonempty open set. The edge-of-the-wedge theorem is a many-variable version of the
Schwarz reflection principle. Together with the identity theorem for holomorphic functions, it implies the
following: a function holomorphic in a tube domain whose boundary values vanish on a real open set must vanish
*emph* on the whole tube:

$$

F \equiv 0 \qquad \text{on } \mathcal{T} .

$$

Taking the boundary limit back to real arguments gives

$$

\braket{\chi | \phi(x_1)\phi(x_2)\cdots\phi(x_n)|\Omega} = 0 \qquad
\text{for *emph*} \ x_1, \dots, x_n \in \mathbb{R}^{1,d-1} .

$$

4. **Conclusion of cyclicity.**
By the Wightman axioms, polynomials in fields smeared over all of spacetime, acting on $\ket\Omega$, give a
dense subspace of $\HH$. The vector $\ket\chi$ is orthogonal to this dense subspace, so $\ket\chi = 0$. Thus
$\overline{\M(\mathcal{O})\ket\Omega} = \HH$, and $\ket\Omega$ is **cyclic**.
5. **Separating property.**
Suppose $A \in \M(\mathcal{O})$ satisfies $A\ket\Omega = 0$. Choose a nonempty open region $\mathcal{O}'$ in
the causal (spacelike) complement of $\mathcal{O}$. By microcausality, $[A, B'] = 0$ for all
$B' \in \M(\mathcal{O}')$. Therefore

$$

A \big(B'\ket\Omega\big) = B' \big(A\ket\Omega\big) = B'(0) = 0 .

$$

By the cyclicity of step~4, applied to $\mathcal O'$, vectors of the form $B'\ket\Omega$ are dense in $\HH$.
A bounded operator that vanishes on a dense subspace is zero, so $A = 0$. Hence $\ket\Omega$ is
**separating** for $\M(\mathcal{O})$. $\blacksquare$

\end{keyresult}

Apply this to the two wedges. It shows that $\ket\Omega$ is cyclic with respect to both $\M_R$ and $\M_L$.
Since $\M_L\subseteq\M_R'$, it is also cyclic for $\M_R'$. By the cyclic—separating duality established
earlier in this chapter, $\ket\Omega$ is therefore cyclic *emph* separating with respect to $\M_R$ alone. So
Tomita—Takesaki theory applies directly, with no further assumption.

Now comes a striking physical fact. It is found using the uniqueness remark~(d) after the Tomita—Takesaki
theorem: find *emph* flow with the right properties that satisfies the KMS condition, and it must be
*emph* modular flow. The result is that the modular operator for $\M_R$ in the vacuum state is
\begin{equation}
K_\Omega \equiv -\log\Delta_\Omega = 2\pi K ,
\label{eq:bw}
\end{equation}
where $K$ is the ordinary **boost generator**. This is the operator that generates Lorentz boosts in
special relativity. It is a geometric symmetry of Minkowski space, and nothing about its definition is abstract
or algebraic. This result is the **Bisognano—Wichmann theorem**. To justify \eqref{eq:bw}, two things must
be checked. (i) The flow generated by $K$ maps $\M_R$ to itself and leaves $\ket\Omega$ invariant. This is
immediate: a boost maps the Rindler wedge $\widehat R$ to itself, and the vacuum is Lorentz invariant. (ii)
Correlators of boosted operators satisfy the KMS relation with $\beta=2\pi$.

\begin{workedexamplebox}[: Verification of the Bisognano—Wichmann KMS Condition]
**Goal:** Show, by a Euclidean path-integral argument, that the boost flow
$\alpha_\eta(A) = e^{i K \eta} A e^{-i K \eta}$ satisfies the KMS condition at $\beta = 2\pi$ for any
operators $A, B \in \M_R$:

$$

\braket{\Omega | A\,\alpha_{i 2\pi}(B) | \Omega} = \braket{\Omega | B A | \Omega} .

$$

Here $\alpha_{i2\pi}(B)=e^{-2\pi K}Be^{2\pi K}$ is the flow continued to the imaginary parameter
$\eta=2\pi i$.

**Calculation:**

1. **Rindler coordinates and Euclidean rotation.**
The right Rindler wedge $\widehat R = \{(t,x) : x > |t|\}$ is described by a proper distance $\rho > 0$ and a
boost parameter $\eta \in \mathbb{R}$:

$$

t = \rho \sinh\eta, \qquad x = \rho \cosh\eta .

$$

A boost by parameter $s$ shifts $\eta \to \eta + s$. Now rotate to Euclidean signature by setting
$t_E \equiv -i t$ and $\eta_E \equiv -i \eta$, so that $t=it_E$ and $\eta=i\eta_E$. Since
$\sinh(i\eta_E)=i\sin\eta_E$ and $\cosh(i\eta_E)=\cos\eta_E$, this gives

$$

t_E = \rho \sin\eta_E, \qquad x = \rho \cos\eta_E .

$$

The Euclidean version of the Minkowski metric is

$$

ds_E^2 = dt_E^2 + dx^2 + dx_\perp^2 = d\rho^2 + \rho^2 d\eta_E^2 + dx_\perp^2 ,

$$

where $dx_\perp^2$ collects the transverse directions, if there are any. In the $(\rho, \eta_E)$ plane these are
standard polar coordinates: $\rho$ is the radius and $\eta_E$ is the polar angle.
2. **Regularity and Euclidean $2\pi$-periodicity.**
The point $\rho = 0$ is the Euclidean image of the horizon. For the plane to be smooth there, with no conical
singularity, the Euclidean angle must have period $2\pi$:

$$

\eta_E \sim \eta_E + 2\pi .

$$

In terms of the Lorentzian boost parameter $\eta = i \eta_E$, the full turn $\eta_E\to\eta_E+2\pi$ is an
imaginary shift of the rapidity:

$$

\eta \longrightarrow \eta + 2\pi i .

$$

Geometrically, rotating $\eta_E$ by $\pi$ maps $(t_E, x) \to (-t_E, -x)$. This sends an operator in the right
wedge $R$ to the left wedge $L$. Rotating by $2\pi$ goes once around the point $\rho = 0$ and returns to the
right wedge.
3. **Path integral and operator ordering.**
In the Euclidean path integral that prepares the vacuum $\ket\Omega$, flowing an operator by the imaginary
boost parameter $i\vartheta$ moves its insertion to the Euclidean angle $\eta_E=\vartheta$. So for
$0<\vartheta<2\pi$, the correlator is a path integral with $A$ inserted at angle $0$ and $B$ at angle
$\vartheta$. The path integral orders operators by their angle:

$$

\begin{aligned}
&\braket{\Omega | A \, e^{-\vartheta K} B e^{\vartheta K} | \Omega} \\
&\qquad = \braket{\Omega | \mathcal{T}_{\eta_E} \big[ A(\eta_E{=}0)\, B(\eta_E{=}\vartheta) \big] | \Omega} ,
\qquad 0<\vartheta<2\pi .
\end{aligned}

$$

The right side is a single smooth function of the angle $\vartheta$, because in the Euclidean plane no angle is
special. As $\vartheta\to0$, the insertion of $B$ approaches $A$ from one side, and the ordered product becomes
$AB$. As $\vartheta\to2\pi$, it approaches the same point from the other side, and the ordering puts $B$ to the
left of $A$:

$$

\lim_{\vartheta\to2\pi}\mathcal{T}_{\eta_E} \big[ A(0)\, B(\vartheta) \big] = B\,A .

$$

Therefore

$$

\Braket{\Omega \Big| A \big( e^{-2\pi K} B e^{2\pi K} \big) \Big| \Omega} = \braket{\Omega | B A | \Omega} .

$$

This is the KMS relation with inverse temperature $\beta = 2\pi$ with respect to the boost parameter $\eta$.
The argument treats the path integral formally, so it is a heuristic. The rigorous statement, for any QFT
satisfying the Wightman axioms, is the Bisognano—Wichmann theorem. Given the KMS property, and property (i)
above, the uniqueness remark~(d) identifies the modular operator as $\Delta_\Omega = e^{-2\pi K}$.
$\blacksquare$

\end{workedexamplebox}

The physical meaning of condition (ii) is the **Unruh effect**. The geometry deserves to be spelled out,
because "a Rindler observer" is not just a figure of speech. Write the Minkowski metric as
$ds^2=-dt^2+dx^2=-\rho^2d\eta^2+d\rho^2$. In these Rindler coordinates, $\rho$ plays the role of a radius and
$\eta$ the role of a boost angle. A trajectory of constant $\rho$ is a hyperbola in the $(t,x)$ plane. It is the
worldline of an observer with constant proper acceleration $a=1/\rho$. Along it, the boost parameter $\eta$ is
proportional to the observer's own proper time: $d\tau=\rho\,d\eta$. Condition (ii) says that observers who use
$\eta$ as their clock, which means exactly these uniformly accelerated observers, see the Minkowski vacuum as a
thermal bath. For an inertial observer the vacuum contains no particles at all. The accelerated observers see
the temperature

$$

T_\rho = \frac{1}{2\pi\rho} = \frac{a}{2\pi} .

$$

This is Unruh's 1976 result. Here it appears as a direct consequence of Tomita—Takesaki theory applied to the
vacuum of a relativistic field. The factor $2\pi$ in \eqref{eq:bw} converts the universal, dimensionless modular
temperature $\beta=1$ into this physical temperature, once $\eta$ is converted to the accelerated observer's own
proper time $\tau$.


> [!NOTE] **Physics Connection: a finite-matrix version of the Unruh effect, from quantum optics**
> The field-theory argument above is rigorous but abstract. It involves every mode of the field, an honest boost,
> and a full QFT vacuum. The same thermality already appears in a finite, checkable calculation, using a toy
> model that every quantum-optics course covers: a two-mode squeezed state. Take two copies of a single
> harmonic-oscillator mode, labelled $R$ and $L$, and build
> 
$$

> \ket{\mathrm{TFD}_x} = \sqrt{1-x^2}\sum_{n=0}^\infty x^n\,\ket n_R\ket n_L , \qquad x\in(0,1) .
> 
$$

> This is the standard two-mode squeezed vacuum. It is already in Schmidt form, with probabilities
> $p_n=(1-x^2)x^{2n}$. We truncated at $40$ Fock levels and computed
> $\rho_R=\Tr_L\ket{\mathrm{TFD}_x}\bra{\mathrm{TFD}_x}$ numerically at $x=0.6$. The off-diagonal entries vanish,
> as they must, since the state is already diagonal in the Fock basis. The trace $\Tr\rho_R$ equals $1$ to
> machine precision (the truncation error is $x^{80}\approx 2\times10^{-18}$). The diagonal entries match
> $p_n=(1-x^2)x^{2n}$ to machine precision for every $n$. Now compare this with an ordinary Gibbs state:
> 
$$

> p_n = (1-x^2)x^{2n} \ \eqstep{1}\ (1-e^{-\beta\omega})e^{-n\beta\omega} .
> 
$$

> **(1)** set $x^2\equiv e^{-\beta\omega}$. The right side is the Boltzmann distribution of a single mode
> of frequency $\omega$ at inverse temperature $\beta$.
> 
> At $x=0.6$ this gives $\beta\omega=-\log(x^2)\approx1.022$. **The observer with access only to mode $R$
> looks at a pure, zero-entropy global state and measures an exactly thermal distribution.** No approximation or
> large-$N$ limit is involved. It is just the ordinary partial trace, applied to a state that happens to be
> diagonal. This is more than an analogy to the Rindler-wedge argument above. It is the same calculation with the
> geometry stripped away. In free field theory, rewriting the Minkowski vacuum in Rindler modes produces exactly
> this two-mode squeezed form, mode by mode. The squeezing parameter is tied to the proper acceleration $a$ by
> $x=e^{-\pi\omega/a}$, so $\beta=2\pi/a$. Summing this thermal spectrum over every field mode is the full
> field-theoretic Unruh calculation.


\begin{figure}[htbp]
\centering
\includegraphics[width=0.78\textwidth]{figs/fig_unruh.pdf}
\caption{The Bisognano—Wichmann theorem and the Unruh effect. (a) The Euclidean plane $(x,t_E)$: the $t=0$
slice is the horizontal axis, split at the horizon point $\rho=0$ (dot) into the half-lines $R$ (blue) and $L$
(gold), and the Euclidean boost angle $\eta_E$ (red) turns about that point, carrying $R$ onto $L$ after a half
turn and back after a full turn of $2\pi$, the periodicity behind the KMS condition at $\beta=2\pi$. (b) The resulting Unruh
temperature $T=1/(2\pi x)$ seen by the accelerated observer passing through the point $x$ of $R$ at $t=0$; it
diverges at the horizon and falls off far from it.}
\label{fig:unruh}
\end{figure}

The boost generator $K$ has continuous spectrum covering the whole real line, $(-\infty,\infty)$. (The only
eigenvector is the vacuum, with eigenvalue $0$.) Boosts form a noncompact group: there are boosts of
arbitrarily large rapidity, and no smallest nonzero one. So $\Delta_\Omega=e^{-2\pi K}$ has spectrum
$\mathbb R_{\ge0}$. One can show that $S(\M_R)$ equals this spectrum. By the classification
\eqref{eq:typeIII-classes}, **$\M_R$ is type $\mathrm{III**_1$}. The modular conjugation $J_\Omega$ also has
a geometric meaning. It is $CRT$: charge conjugation, combined with a reflection of the $x$ direction and time
reversal. So the CPT symmetry of relativistic quantum field theory shows up as part of the modular structure of
the vacuum, built from nothing but the algebra and the state.

This whole story extends at once to higher spacetime dimensions. Any transverse directions just come along
unchanged, since the boost acts only in the $t$-$x$ plane. More importantly, it extends in part to a
*emph* open region $O$ on a Cauchy slice, not just to a half-space. Reeh—Schlieder guarantees that
$\ket\Omega$ is still cyclic and separating for $\M_O$, so Tomita—Takesaki theory applies. In general the
modular operator can no longer be written in closed form. It depends on the precise theory and on the precise
shape of $O$. Still, a scale-invariance argument pins down its type. The argument needs the theory to have a
scale-invariant fixed point at short distances, which is believed to be true of essentially every interacting
quantum field theory. Very close to the boundary $\Sigma_O$ of the region $O$, the boundary looks like a flat
plane. So locally the geometry cannot be told apart from the Rindler wedge just worked out, and

$$

-\log\Delta_\Omega \approx 2\pi K, \qquad \text{very close to } \Sigma_O ,

$$

with $K$ now the boost that locally leaves $\Sigma_O$ fixed. This forces the same continuous spectrum
$\mathbb R_{\ge0}$, and hence type $\mathrm{III}_1$ again. As stated, this is a heuristic. It can be made
rigorous under a technical assumption about the short-distance (scaling) limit of the theory. **So the
type $\mathrm{III**_1$ nature of local algebras in a relativistic quantum field theory can be traced to the local
Rindler structure near any entangling surface, and that structure comes from relativistic causality.} This is
the precise sense in which "the causal structure of a relativistic QFT requires type $\mathrm{III}_1$."
Correspondingly, a *emph*-relativistic field theory, with no light-cone structure to force this local
Rindler behavior, need not have type $\mathrm{III}_1$ local algebras at all.

### The split property

Chapter~1 gave a heuristic picture: non-factorization and type III structure come from infinite entanglement
among short-distance degrees of freedom right at the boundary of a region. This picture can be made precise.
The precise version also resolves what could look like a contradiction. How can two regions be infinitely
entangled (type III, no factorization) and yet, intuitively, "mostly independent" away from their shared
boundary?

Separate $R$ and $L$ by a small but nonzero buffer distance $\epsilon_b$. There is then a thin strip
$I_\epsilon$ of "no man's land" between them. The **split property** states that there *emph* a
genuine tensor factorization $\HH=\HH_1\otimes\HH_2$, with

$$

\begin{aligned}
\M_R &\subset B(\HH_1)\otimes\id_{\HH_2} \subset \M_L' = \M_{R_\epsilon}, \\
\M_L &\subset \id_{\HH_1}\otimes B(\HH_2) \subset \M_R' = \M_{L_\epsilon} ,
\end{aligned}

$$

where $R_\epsilon\equiv R\cup I_\epsilon$, and similarly for $L_\epsilon$. So a type I factor,
$B(\HH_1)\otimes\id_{\HH_2}$, sits between the two type $\mathrm{III}_1$ algebras $\M_R$ and $\M_{R_\epsilon}$.
This has real physical content. Once $R$ and $L$ are separated by *emph* nonzero distance, however small,
they *emph* be completely disentangled. There are honest product states with respect to the factors
$\HH_1,\HH_2$, and on them $\M_R$ and $\M_L$ act independently. In other words, the entanglement obstruction of
Chapter~1 is a short-distance effect localized at the boundary. It disappears as soon as the two regions are
separated by any finite gap. More generally, take two regions $O_1\subset O_2$ whose boundaries do not touch
(the closure of $O_1$ lies inside the interior of $O_2$). The split property then guarantees a type I factor
$\N$ with $\M_{O_1}\subset\N\subset\M_{O_2}$. A type I "buffer" can always be inserted, as long as there is
some geometric gap to put it in.

The split property is not an extra assumption pulled from nowhere. It can be shown to follow from a technical
condition called the *emph*. This is a statement about how quickly the number of available
states of the theory grows with energy. It is believed to hold for any "reasonable" relativistic QFT. Given
the split property, one can further show that $\M_O$, for an open region $O$, is not only type
$\mathrm{III}_1$ but also **hyperfinite**. This means it can be built as the weak closure of an increasing
sequence of ordinary finite-dimensional matrix algebras. That is exactly the kind of construction used
throughout these notes: bigger and bigger, but always finite, matrices, taken to a limit. A deep uniqueness
theorem then applies: up to isomorphism, there is only *emph* hyperfinite type $\mathrm{III}_1$ factor. The
consequence is striking. **The local algebra of any region in any "reasonable" relativistic QFT (free or
interacting, weakly or strongly coupled, in any spacetime dimension) is abstractly isomorphic to the local
algebra of any other region in any other such theory.** Different theories are not distinguished by what their
local algebras *emph*, since abstractly these are all the same object. They are distinguished by how the
algebras sit relative to one another: which operators are shared between overlapping regions, how correlators
between distant regions behave, and so on. This statement is surprising, and it is given here at full strength
for a reason. It shows clearly how much structure the type classification captures. It also shows how much it
deliberately does *emph* capture: the dynamics, which lives entirely in the relations between algebras, not
in the abstract type of any single algebra.

Two further consequences follow. The first comes with a short proof. The second is one of the more startling
facts in the whole subject.

**Strong local preparability.** Take the split setup just described, with regions $R$ and $L$ separated by
a buffer $I_\epsilon$. In a general state $\omega$, operators in $R$ and in $L$ are correlated:
$\omega(AB)\ne\omega(A)\omega(B)$ for $A\in\M_R$, $B\in\M_L$. Nothing is surprising there. The startling claim is
the following. There is an operation $W$, supported only in the slightly larger region $R_\epsilon$ ($R$ plus
the thin buffer strip), that turns $\omega$ into a *emph* state $\omega_W$ with three properties. (i) There
is *emph* correlation at all between $\M_R$ and $\M_L$. (ii) On $\M_R$, the new state equals an arbitrarily
chosen target state $\phi$. (iii) On $\M_L$, the new state is the same as the original $\omega$. This sounds
nearly impossible. It says you can locally erase all correlation with a distant system and, at the same time,
re-prepare your own region in any state you like, without touching the distant system. Yet it follows in a few
lines from the split property and the type III structure.

Here is the argument. By the split property, $\M_R\subset B(\HH_1)\otimes\id_{\HH_2}$. So there is a vector
$\ket\xi\in\HH_1$ that represents the target state, $\phi(A)=\braket{\xi|A|\xi}$. (This step is justified more
carefully in the section on the natural cone at the end of this chapter.) The projection
$P_\xi=\ket\xi\bra\xi\otimes\id_{\HH_2}$ lies in $\M_{R_\epsilon}$. Since $\M_{R_\epsilon}$ is type III,
*emph* nonzero projection in it is equivalent to the identity. This is Chapter~2's discussion of finite
and infinite projections pushed to its extreme: in type III nothing is finite, so every projection is as "big"
as the whole algebra. So there is an isometry $W\in\M_{R_\epsilon}$ with $WW^\dagger=P_\xi$ and
$W^\dagger W=\id$. Define $\omega_W(X)\equiv\omega(W^\dagger XW)$. Because $W\in\M_{R_\epsilon}\subset\M_L'$,
it commutes with everything in $\M_L$. So for $B\in\M_L$,
\begin{align}
\omega_W(B)\equiv\omega(W^\dagger BW) \eqstep{1} \omega(W^\dagger W B) \eqstep{2} \omega(B) . \notag
\end{align}
**(1)** $W$ commutes with $B$, because $W\in\M_L'$.\quad
**(2)** $W^\dagger W=\id$.

So the $L$ side is untouched, as claimed. For the $R$ side, we use the relation $P_\xi AP_\xi=\phi(A)P_\xi$,
which follows at once from $\ket\xi$ representing $\phi$. For $A\in\M_R$ it gives
\begin{align}
W^\dagger AW &\eqstep{1} W^\dagger (WW^\dagger)A(WW^\dagger)W \notag\\
&\eqstep{2} W^\dagger P_\xi AP_\xi W
\eqstep{3} \phi(A)\,W^\dagger P_\xi W
\eqstep{4} \phi(A)\,\id . \notag
\end{align}
**(1)** $W^\dagger W=\id$ implies $W^\dagger=W^\dagger WW^\dagger$ and $W=WW^\dagger W$.\quad
**(2)** $WW^\dagger=P_\xi$.\quad
**(3)** $P_\xi AP_\xi=\phi(A)P_\xi$.\quad
**(4)** $W^\dagger P_\xi W=W^\dagger WW^\dagger W=\id$.

Combining the two results gives the factorized, re-prepared state. For $A\in\M_R$ and $B\in\M_L$,
\begin{align}
\omega_W(AB)\equiv\omega(W^\dagger ABW) \eqstep{1} \omega(W^\dagger AW\,B) \eqstep{2} \phi(A)\,\omega(B) .
\notag
\end{align}
**(1)** $W$ commutes with $B\in\M_L$, so $BW=WB$.\quad
**(2)** $W^\dagger AW=\phi(A)\id$, from the chain just above.

**The Connes—St\o rmer transitivity theorem.** For a type $\mathrm{III}_1$ factor, *emph* two states
$\phi$ and $\omega$ can be connected to arbitrary precision $\epsilon>0$ by a unitary $W$ *emph*: $\|\phi-\omega_W\|<\epsilon$. In words, every state can be prepared locally, to arbitrary
accuracy, starting from any other state. This is such a strong form of ergodicity that it is fair to call the
state space *emph*. No state is structurally special or hard to reach from another. This is in
sharp contrast with a type I factor $B(\HH)$. There, unitary conjugation $\rho\to U\rho U^\dagger$ preserves the
eigenvalues of the density matrix, so a pure state can never be brought close to a mixed one. With a
nontrivial center it is worse still: different superselection sectors are, by definition, unreachable from one
another by anything in the algebra.

### The collection of algebras $\{\M(O)\}$, and Haag duality

One more structural point returns directly in Chapter~7. Consider the full collection of local algebras
$\{\M(O)\}$, one for every open spacetime region $O$. It is expected to satisfy several basic consistency
relations. Each one is an algebraic translation of an ordinary physical principle.

- **Isotony**, $\M(O_1)\subseteq\M(O_2)$ for $O_1\subseteq O_2$. A bigger region gives access to at
least as many operations as a smaller region inside it. This is almost a definition.
- **The time-slice axiom**, $\M(O)=\M(\widehat O)$. The equations of motion are causal. So operators
anywhere in the domain of dependence $\widehat O$ can be rewritten, using time evolution, in terms of operators
in $O$ itself. Knowing the algebra on a single Cauchy slice therefore determines it everywhere.
- **Locality (commutativity)**, $\M(O')\subseteq\M(O)'$. Operators in the causal complement $O'$
(spacelike separated from all of $O$) commute with everything in $\M(O)$. This is the operator-algebra form of
ordinary microcausality.

When the last relation holds with *emph*, $\M(O')=\M(O)'$, it is called **Haag duality**. This
is strictly stronger. It says that *emph* operator commuting with $\M(O)$ already comes from the causal
complement, with nothing extra hiding elsewhere. Haag duality is not automatic. It can fail for topologically
nontrivial regions. It is expected to hold quite generally for the vacuum sector of an ordinary relativistic QFT
on topologically simple regions. Two further relations complete the package. The first is
**additivity**, $\M(O_1\cup O_2)=\M(O_1)\vee\M(O_2)$: no "extra," genuinely nonlocal operators hide in a
union beyond those built from the pieces. The second is the **intersection property**,
$\M(O_1\cap O_2)=\M(O_1)\cap\M(O_2)$. It can be derived from Haag duality and additivity by taking commutants,
in cases where the causal complement of $O_1\cap O_2$ is the union of $O_1'$ and $O_2'$. A theory that
satisfies all of these relations for every region (not just topologically trivial ones) is called
"complete." It helps to know these relations in outline, not for their own sake, but because Chapter~7 builds
subregion-subalgebra duality on exactly this dictionary, translated to the boundary theory of AdS/CFT.

## Emergent times from subalgebras — half-sided modular inclusion

This section introduces a second, distinct notion of emergent time. It does not come from the modular flow of a
single algebra. It comes from the relationship between an algebra and a carefully chosen subalgebra of it. It
is special to type $\mathrm{III}_1$ algebras. It is also the mechanism, taken up again in Chapters~7 and~8, that
lets a single band of boundary time generate the entire interior of an emergent black-hole horizon.

### A new, positive "Hamiltonian" $G$

Let $\M$ be a von Neumann algebra with a cyclic and separating vector $\ket\Omega$. Its modular data are
$\Delta_\M=e^{-K_\M}$ and $J_\M$, as in the Tomita—Takesaki theorem. Now suppose $\N\subset\M$ is a
subalgebra, and $\ket\Omega$ is *emph* cyclic for $\N$. It is then automatically separating for $\N$ too:
it is separating for the bigger algebra $\M$, and $\N\subset\M$. So $\N$ has its own modular data,
$\Delta_\N=e^{-K_\N}$ and $J_\N$, with respect to the same $\ket\Omega$.

Here is the first new structural fact, with the reason it holds. Because $\N\subset\M$, the Tomita operator
$S_\M$ (built from $\M$ and $\ket\Omega$) is an extension of $S_\N$ (built from $\N$ and the same
$\ket\Omega$). That is, $S_\M$ agrees with $S_\N$ wherever $S_\N$ is defined, but it is also defined on the
larger set $\M\ket\Omega\supseteq\N\ket\Omega$. There is a general fact about unbounded operators: if $X$
extends $Y$, then $X^\dagger X\le Y^\dagger Y$ as quadratic forms. The two forms agree wherever both are
defined. The form of $X^\dagger X$ is defined on more vectors, and in this ordering that makes it the smaller
one. Applied to $\Delta_\M=S_\M^\dagger S_\M$ and $\Delta_\N=S_\N^\dagger S_\N$, this gives
$\Delta_\M\le\Delta_\N$. The logarithm preserves inequalities between positive operators, so
$\log\Delta_\M\le\log\Delta_\N$, which means $K_\M\ge K_\N$. Define
\begin{equation}
G \equiv \frac{1}{2\pi}(K_\M-K_\N) \ \ge 0, \qquad G\ket\Omega=0 .
\label{eq:G-def}
\end{equation}
The factor $2\pi$ is a normalization chosen for convenience later. The equation $G\ket\Omega=0$ holds because
$K_\M$ and $K_\N$ each annihilate $\ket\Omega$. This is the invariance $\Delta\ket\Omega=\ket\Omega$ from the
Tomita—Takesaki theorem, applied to each algebra. $G$ is a positive operator, so it deserves to be called a
Hamiltonian. The flow $e^{iGs}$ that it generates is a legitimate new notion of "time." It is distinct from
the modular flows of both $\M$ and $\N$, and it also leaves the reference vector $\ket\Omega$ fixed.

### The half-sided modular inclusion condition, and what it buys you

Everything so far works for *emph* subalgebra $\N\subset\M$ that shares a cyclic and separating vector with
$\M$. Much more follows if $\N$ satisfies one additional, geometric-looking condition, called
**half-sided modular inclusion**:
\begin{equation}
\N_t \equiv \Delta_\M^{-it}\N\Delta_\M^{it} \subset \N, \qquad \text{for every } t\le0 .
\label{eq:hsmi}
\end{equation}
In words: flowing $\N$ by $\M$'s *emph* modular flow, for negative modular time, always shrinks $\N$ or
leaves it the same. It never grows it. When this holds, a theorem of Wiesbrock, building on earlier work of
Borchers, gives three consequences at once. We quote it without proof. None of the three is assumed; all are
derived from \eqref{eq:hsmi} alone.


1. $K_\M$, $K_\N$ and $G$ satisfy the commutation relations

$$

[K_\M,K_\N] = -4\pi^2i\,G , \qquad [K_\M,G] = 2\pi i\,G ,

$$

together with a companion relation for the modular conjugations. Since $K_\N=K_\M-2\pi G$, these are the
commutation relations of the dilations and translations of a line. They form a two-dimensional subalgebra of
the M\"obius algebra, which is the global conformal symmetry of a line. So a recognizable piece of conformal
symmetry is produced from nothing but one algebraic inclusion condition on two von Neumann algebras.
2. The flow generated by $G$ maps $\M$ into itself for one whole half of the time axis:
$e^{iGs}\M e^{-iGs}\subset\M$ for $s\le0$. In particular, $\N=e^{-iG}\M e^{iG}$. So $\N$ is exactly the image
of $\M$ under one unit of this new time translation generated by $G$. Running $G$ continuously gives a nested,
continuously parametrized family of algebras $e^{-iGu}\M e^{iGu}$ for $u\ge0$. For $0\le u_1<u_2$ they satisfy

$$

e^{-iGu_2}\M e^{iGu_2}\ \subset\ e^{-iGu_1}\M e^{iGu_1}\ \subset\ \M ,

$$

with $u=0$ giving $\M$ itself and $u=1$ giving $\N$. This is a new time translation, distinct from $\M$'s own
modular flow. It acts by relating the algebra to smaller and smaller copies of itself.
3. **$\M$ must be type $\mathrm{III**_1$} (as long as $\N\ne\M$). Half-sided modular inclusion is not
just a convenient technical condition. Its existence forces the ambient algebra to be the "most chaotic" type
identified earlier in this chapter.

The proof of this theorem builds several further objects along the way. They include the unitaries
$D(t)=\Delta_\M^{-it}\Delta_\N^{it}$ and $V=J_\M J_\N$, and a chain of nested algebras built by repeatedly
conjugating with $V$. These are used to *emph* the theorem and to show that this half-sided inclusion
structure, once it exists, is unique. They are careful pieces of functional analysis. They are named here so
that the notation is not a surprise in the research literature. The three numbered consequences above are the
physical content that matters for everything that follows.

### The concrete example: light-cone translations in the Rindler wedge

Here is a worked example that turns the abstract theorem into something you can picture. Use light-cone
coordinates $x^\pm=x^0\pm x^1$, so that the right Rindler wedge $\widehat R$ from earlier in this chapter is
$\{x^+>0,\,x^-<0\}$. Take $\M$ to be the algebra of $\widehat R$. Let $\N$ be the algebra of the smaller region
$\{x^+>0,\,x^-<-1\}$. This is a wedge nested strictly inside $\widehat R$, with its tip moved by one unit along
the $x^-$ direction, to the point $(x^+,x^-)=(0,-1)$. Now flow $\N$ using $K_\M=2\pi K$ (the boost generator,
\eqref{eq:bw}). A boost acts on light-cone coordinates by a simple rescaling. With the sign convention in which
the modular flow moves the right wedge forward in time, the flow $e^{iK_\M t}=e^{2\pi iKt}$ is a boost by
$\eta=2\pi t$ that acts as $x^\pm\to e^{\pm2\pi t}x^\pm$. It turns the defining condition $x^-<-1$ into
$x^-<-e^{-2\pi t}$. So

$$

\N_t \equiv e^{iK_\M t}\N e^{-iK_\M t} = \text{algebra of the region } \{x^+>0,\,x^-<-e^{-2\pi t}\} .

$$

For $t<0$ we have $e^{-2\pi t}>1$. So this region is *emph* than the original one, since it requires
$x^-$ to be even more negative. This is exactly $\N_t\subset\N$ for $t<0$, the half-sided modular inclusion
condition. Here it is checked directly on an explicit geometric example, not just asserted.

Identifying $G$ here takes a short computation with the ordinary Poincar\'e algebra of special relativity.
Write $P^\pm=\tfrac12(P^0\pm P^1)$ for the light-cone components of the energy-momentum operator. The boost
generator and the momentum satisfy $[K,P^\pm]=\pm iP^\pm$. This is the statement that a boost rescales energy
and momentum in the same way that it rescales light-cone coordinates. The region of $\N$ is the region of $\M$
translated so that its tip moves from the origin to $(x^+,x^-)=(0,-1)$. So $K_\N$ is $K_\M$ conjugated by this
translation, which is the unitary $e^{-iP^+}$:
\begin{align}
K_\N = e^{-iP^+}K_\M\,e^{iP^+} \eqstep{1} K_\M - i\,[P^+,K_\M] \eqstep{2} K_\M - 2\pi P^+ . \notag
\end{align}
**(1)** expand $e^{-iP^+}K_\M e^{iP^+}=K_\M-i[P^+,K_\M]+\dots$; the higher terms vanish, because
$[P^+,K_\M]$ is proportional to $P^+$, which commutes with $P^+$.\quad
**(2)** $[P^+,K_\M]=-2\pi[K,P^+]=-2\pi iP^+$.

Then the definition \eqref{eq:G-def}, $G=\tfrac1{2\pi}(K_\M-K_\N)$, gives

$$

G = P^+ .

$$

**So in this example, the abstract "positive Hamiltonian" $G$ is just the ordinary light-cone momentum
operator $P^+$. The new "time flow" it generates is just ordinary translation in the $x^-$ direction.** It is
positive, as it must be: $P^+\ge0$ by the spectrum condition. The general statements~1 and~2 above (the
commutation relations and the half-sided translation structure) can be checked directly on this example with
ordinary special-relativistic kinematics. For instance, $[K_\M,G]=2\pi[K,P^+]=2\pi iG$. Statement~3 agrees with
the type $\mathrm{III}_1$ result for the Rindler wedge found earlier. This is the mechanism that Chapter~8
reuses to show that a single band of *emph* time in AdS/CFT can generate the entire interior of an
emergent black-hole horizon. There, the interior is built by exactly this kind of half-sided modular inclusion
light-cone translation, with $G$ playing the role of a positive bulk momentum.

One further variant is the mirror image. Take $\N$ to be the region $\{x^+>1,\,x^-<0\}$, shifted along $x^+$
instead of $x^-$. This gives a half-sided inclusion on the *emph* half of the time axis,
$\N_t\subset\N$ for $t\ge0$. The commutation relations have the opposite sign, and the translation generator is
$G=P^-$ instead of $P^+$.

## Relative modular flows and relative entropy

This section extends two familiar objects, the relative entropy $S(\rho\|\sigma)$ of Chapter~1 and the
Tomita operator $S_\Psi$ of this chapter, to a setting with *emph* states $\ket\Psi$ and $\ket\Omega$,
both cyclic and separating for the same $\M$. The aim is a relative entropy that still makes sense when $\M$
is type III, where the ordinary entropy $S_\M$ cannot be defined at all (Chapter~3).

The **relative Tomita operator** is defined like the ordinary one, except that it maps between the two
vectors:

$$

S_{\Psi\Omega}A\ket\Omega = A^\dagger\ket\Psi\ \ (A\in\M), \qquad
F_{\Psi\Omega}A'\ket\Omega = A'^\dagger\ket\Psi\ \ (A'\in\M') ,

$$

with $F_{\Psi\Omega}=S_{\Psi\Omega}^\dagger$, exactly as $S_\Psi$ and $F_\Psi$ act on $\M$ and $\M'$ in the
single-state case.
Its polar decomposition $S_{\Psi\Omega}=J_{\Psi\Omega}\Delta_{\Psi\Omega}^{1/2}$ defines the
**relative modular operator** $\Delta_{\Psi\Omega}\ge0$ and the **relative modular conjugation**
$J_{\Psi\Omega}$. When $\Psi=\Omega$ these are the ordinary $\Delta_\Psi$ and $J_\Psi$. For the type I case
$\M=B(\HH_1)\otimes\id$, the same calculation that gave $\Delta_\Psi=\rho_R\otimes\rho_L^{-1}$ at the start of
this chapter now gives

$$

\Delta_{\Psi\Omega}=\rho_\Psi\otimes\rho_\Omega'^{-1} ,

$$

the density matrix of $\Psi$ on the $\M$ side and the inverse density matrix of $\Omega$ on the commutant
side. (Here $\rho_\Psi$ and $\rho'_\Psi$ are the reduced density matrices of $\Psi$ on $\HH_1$ and $\HH_2$,
the $\rho_R$ and $\rho_L$ of the opening example.) The relative modular operator lets one convert correlation functions in one state into correlation
functions in the other. For $A,B\in\M$,
\begin{align}
\braket{\Psi|AB|\Psi}
&\eqstep{1} \big\langle A^\dagger\Psi\,\big|\,B\Psi\big\rangle
\eqstep{2} \big\langle S_{\Psi\Omega}A\Omega\,\big|\,S_{\Psi\Omega}B^\dagger\Omega\big\rangle \notag\\
&\eqstep{3} \big\langle \Delta_{\Psi\Omega}^{1/2}B^\dagger\Omega\,\big|\,\Delta_{\Psi\Omega}^{1/2}A\Omega\big\rangle
\eqstep{4} \braket{\Omega|B\,\Delta_{\Psi\Omega}\,A|\Omega} .
\label{eq:twostate-kms}
\end{align}
**(1)** move $A$ to the left as $A^\dagger$.\quad
**(2)** the definition of $S_{\Psi\Omega}$, used twice: $A^\dagger\Psi=S_{\Psi\Omega}A\Omega$ and
$B\Psi=S_{\Psi\Omega}B^\dagger\Omega$.\quad
**(3)** $S_{\Psi\Omega}=J_{\Psi\Omega}\Delta_{\Psi\Omega}^{1/2}$, and the antiunitary $J$ satisfies
$\braket{J\xi|J\eta}=\braket{\eta|\xi}$, which swaps the two slots.\quad
**(4)** $\Delta_{\Psi\Omega}^{1/2}$ is self-adjoint, and $(B^\dagger)^\dagger=B$.

This is the two-state version of the KMS relation. For two random states of a pair of qutrits it was checked
numerically, with $\Delta_{\Psi\Omega}=\rho_\Psi\otimes\rho_\Omega'^{-1}$ and random $A,B$: both sides agree to
fifteen digits.

Two further facts are quoted without proof. On $\M$, the flow generated by $\Delta_{\Psi\Omega}$ is the same
as the flow generated by the ordinary $\Delta_\Psi$, and on $\M'$ it is the same as the flow generated by
$\Delta_\Omega$. And the unitary $u_{\Omega\Psi}(s)\equiv\Delta_{\Omega\Phi}^{-is}\Delta_{\Psi\Phi}^{is}$,
built with the help of a third state $\ket\Phi$ but independent of which $\Phi$ is used, is the explicit
unitary in $\M$ that relates $\sigma_s^\Psi$ to $\sigma_s^\Omega$ in \eqref{eq:cocycle}.

### Relative entropy for type III, and a proof that it is positive

For a type III algebra no entropy can be assigned to a single state. A **relative** entropy between two
states can be, using the relative modular operator:
\begin{equation}
S_\M(\Psi\|\Omega) \equiv -\braket{\Psi|\log\Delta_{\Omega\Psi}|\Psi} .
\label{eq:araki-relent}
\end{equation}
In the type I case this reduces to the familiar formula:
\begin{align}
-\braket{\Psi|\log\Delta_{\Omega\Psi}|\Psi}
&\eqstep{1} -\braket{\Psi|\log\rho_\Omega\otimes\id|\Psi} + \braket{\Psi|\id\otimes\log\rho_\Psi'|\Psi}
\notag\\
&\eqstep{2} -\tr(\rho_\Psi\log\rho_\Omega) + \tr(\rho'_\Psi\log\rho'_\Psi)
\eqstep{3} \tr(\rho_\Psi\log\rho_\Psi) - \tr(\rho_\Psi\log\rho_\Omega) .
\notag
\end{align}
**(1)** $\Delta_{\Omega\Psi}=\rho_\Omega\otimes\rho_\Psi'^{-1}$, and the logarithm of a tensor product
of commuting positive factors is the sum of the logarithms.\quad
**(2)** the expectation value of an operator acting on one factor is its trace against that factor's
reduced density matrix.\quad
**(3)** for a pure state $\ket\Psi$, $\rho_\Psi$ and $\rho'_\Psi$ have the same nonzero eigenvalues
(Schmidt decomposition), so $\tr(\rho'_\Psi\log\rho'_\Psi)=\tr(\rho_\Psi\log\rho_\Psi)$.

This is the relative entropy of Chapter~1. For the same random qutrit states, the left side of the chain and
the familiar formula both give $2.10961$, agreeing to thirteen digits. The definition \eqref{eq:araki-relent}
never uses a trace, however, so it carries over unchanged to type III.

Positivity takes only a few lines. The inequality $\log x\le x-1$ holds for every positive real $x$, with
equality only at $x=1$. (The function $f(x)=x-1-\log x$ has $f(1)=0$ and $f'(x)=1-1/x$, which is negative for
$x<1$ and positive for $x>1$, so $x=1$ is its unique minimum.) Then
\begin{align}
-\braket{\Psi|\log\Delta_{\Omega\Psi}|\Psi}
&\geqstep{1} \braket{\Psi|\,\id-\Delta_{\Omega\Psi}\,|\Psi} \notag\\
&\eqstep{2} \braket{\Psi|\Psi} - \braket{\Omega|\Omega}
\ \eqstep{3}\ 0 . \notag
\end{align}
**(1)** $\log x\le x-1$, applied to the spectrum of the positive operator $\Delta_{\Omega\Psi}$ and then
averaged in the state $\ket\Psi$.\quad
**(2)** the two-state KMS relation \eqref{eq:twostate-kms} with $\Psi$ and $\Omega$ exchanged and
$A=B=\id$ gives $\braket{\Psi|\Delta_{\Omega\Psi}|\Psi}=\braket{\Omega|\Omega}$ (numerically $0.99999\ldots$
for the qutrit example).\quad
**(3)** both states are normalized.

So $S_\M(\Psi\|\Omega)\ge0$ for every type of algebra. Chapter~3 found that the ordinary entropy $S_\M$ of a
type II algebra can be negative. Relative entropy does not have this problem, because it measures how
distinguishable $\Psi$ is from a fixed reference state $\Omega$. It never needs an absolute zero of entropy,
which type II and type III algebras do not have.

## A canonical purification: the natural cone

This last section answers a natural question about purifications. Given a state $\omega$ on $\M$, is there a
*emph* vector $\ket\xi\in\HH$ with $\omega(A)=\braket{\xi|A|\xi}$?

In general many vectors do the job. For $\M=B(\HH_1)\otimes\id_{\HH_2}$, any vector in $\HH_1\otimes\HH_2$ whose
reduced density matrix on $\HH_1$ is the right one works, and ordinary quantum mechanics gives no reason to
prefer one of them. Suppose, however, that $\HH$ contains *emph* cyclic and separating vector for $\M$.
The pair $(\M,\HH)$ is then said to be in **standard form**. This holds, for instance, for $\M=\M_O$ with
$O$ an open region in the vacuum sector of a relativistic QFT (by Reeh—Schlieder), and for any GNS
representation built from a faithful state (Chapter~2). In standard form there is a canonical choice.

Fix a cyclic and separating reference vector $\ket\Omega$. The **natural cone** $P_\Omega$ is the closure
of the set $\{A\,j_\Omega(A)\ket\Omega : A\in\M\}$, where $j_\Omega(A)\equiv J_\Omega AJ_\Omega$. An
equivalent description is the closure of $\{\Delta_\Omega^{1/4}A^\dagger A\ket\Omega : A\in\M\}$. Every normal
state $\omega$ on $\M$ has exactly one representative vector in $P_\Omega$, and that vector is the canonical
purification. It depends on the choice of $\Omega$: a different reference vector gives a different cone.

For two qubits the cone is easy to see. Take $\M=B(\mathbb C^2)\otimes\id$ and the reference vector
$\ket\Omega=\tfrac1{\sqrt2}(\ket{00}+\ket{11})$. Write a vector as $\ket\xi=\sum_{ia}\xi_{ia}\ket{i}\ket{a}$,
that is, as a $2\times2$ matrix $\xi$. For this $\Omega$, $J_\Omega$ acts by $\xi\mapsto\xi^\dagger$, and
$A\,j_\Omega(A)\ket\Omega$ corresponds to the matrix $A A^\dagger/\sqrt2$, which is positive semidefinite. The
natural cone is therefore the set of positive semidefinite $2\times2$ matrices. A state with density matrix
$\rho$ on the first qubit is represented by every $\xi$ with $\xi\xi^\dagger=\rho$, but only one of these is
positive, namely $\xi=\sqrt\rho$. The canonical purification is
$\ket{\xi_\rho}=\sum_{ia}(\sqrt\rho)_{ia}\ket i\ket a$, the familiar "square-root" purification of ordinary
quantum information. The inner product of two such vectors is $\tr(\sqrt{\rho}\sqrt{\sigma})$, which is real
and non-negative.

Vectors in the natural cone have several further properties, quoted here without proof. The inner product of
any two vectors in $P_\Omega$ is real and non-negative, as in the two-qubit example. Vectors fixed by $J_\Omega$ can be decomposed into cone vectors. The
distance between two cone vectors is bounded by the distance between the states they represent. Two different
cyclic and separating vectors in the same natural cone have the same $J$ and the same cone. A cyclic and
separating vector outside the cone can be moved into it by an explicit unitary. Every automorphism of $\M$ can
be implemented by a unitary that preserves the cone. The physics in the rest of these notes uses only the
existence and uniqueness of the canonical purification and the positivity of inner products.

\bigskip
\noindent With this, the tools for entanglement are in place for every type of von Neumann algebra: I, II, and
III. Chapter~5 takes up the problem noted in remark (f) after the Tomita—Takesaki theorem. A type III algebra
has no trace and so no entropy of its own, which is a serious problem if the goal is to compute a black-hole
entropy. The **crossed product** fixes this. It attaches an extra quantum system, a clock, to a type III
algebra and turns it into a type II algebra, which does have a trace.



---

# The crossed product by the modular group

Chapter~4 ended with a problem. A type III algebra has no trace. Without a trace there is no density operator,
and without a density operator there is no entropy. This is true even for the weaker, ``relative to a
reference'' kind of entropy that worked for type II in Chapter~3. Suppose the goal is to compute something like
a black-hole entropy using only operator algebras. Then this is a real obstruction, not a technicality.

The **crossed product** is the construction that removes the obstruction. It does not get around the
no-trace theorem. Instead, it builds a *emph* algebra out of the original type III algebra.
This larger algebra always turns out to be type II, and a type II algebra does have a trace. The construction
is mechanical and completely general. It comes back, almost unchanged, in Chapter~9, where it is the physical
mechanism behind gravitational entropy.

One limitation should be stated at the start. It explains why this chapter has no qubit model of the whole
construction. Every finite-dimensional von Neumann algebra is type I. The reason is simple. In finite
dimensions every projection has finite rank. So a nonzero projection of smallest rank in the algebra cannot be
split any further, and an algebra with such minimal projections is type I (Chapter~2). As a result, no finite
matrix example can show the passage from type III to type II itself. That passage happens only in infinite
dimensions. What small, explicit examples *emph* check is each individual step: the dressing condition, the
commutator identities, the trace formula and its cyclicity, and the shape of the entropy formula. These steps
are checked explicitly below. (The cyclicity of a type II trace was already checked on Bell-pair matrices in
Chapter~3.)

## Crossed products in general

The general construction does not mention modular theory at all. The modular case used in these notes is one
special instance. Suppose a group $G$ acts on a von Neumann algebra $\M$ by unitaries,
$\alpha_g(A)=U_gAU_g^\dagger$. Think of $\alpha$ as a family of symmetries of $\M$, labelled by the group
elements $g$. Given the triple $(\M,G,\alpha)$, there is a standard way to build a *emph* von Neumann
algebra, called the **crossed product** and written $\widehat\M\equiv\M\rtimes_\alpha G$. It acts on the
enlarged Hilbert space $\widehat\HH=\HH\otimes L^2(G)$. The second factor $L^2(G)$ consists of square-integrable
functions on $G$. One can think of it as an extra quantum system whose configuration space is the group $G$
itself.

In these notes the group is $G=\mathbb R$, with generator $K$ and action
\begin{equation}
\alpha_t(A)=e^{iKt}Ae^{-iKt} .
\label{eq:cp-action}
\end{equation}
Then $\widehat\HH=\HH\otimes L^2(\mathbb R)$. The extra system is simply a quantum particle on a line.

From now on, take $K=-\log\Delta_\Psi$. This is the *emph* generator of $\M$ itself, built from some
cyclic and separating vector $\ket\Psi$. With this choice, \eqref{eq:cp-action} is exactly the modular flow
$\sigma_t$ built in Chapter~4.

The main result of this chapter is proved step by step below. If $\M$ is type III, the crossed product
$\widehat\M$ is **always type II**, whichever type III subtype $\M$ started as. This makes the tools of
Chapter~3 (density operators and entropy) available at once, applied to $\widehat\M$ instead of $\M$. A second
fact is justified at the end of the next section. The algebra $\widehat\M$ depends only on $\M$, not on which
reference state $\ket\Psi$ was used to build the modular flow. So the construction is *emph* to $\M$.
It is not an artifact of an arbitrary choice. In Chapter~9 the same construction explains black-hole and
de~Sitter entropy. There, the clock position $\hat q$ introduced below becomes the energy of a physical
observer.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.88\textwidth]{figs/fig_crossed.pdf}
\caption{The crossed product. A type $\mathrm{III}_1$ algebra $\M$, which has no trace, comes with its
modular flow $\sigma_s$ (red arrow). Adding a clock, a particle on a line with position $\hat q$ and Hilbert
space $L^2(\mathbb R)$ (a wavepacket is sketched), and combining the two produces the larger algebra
$\widehat\M$. It is type $\mathrm{II}_\infty$ and does have a trace.}
\label{fig:crossed_product}
\end{figure}

## Construction of $\widehat\M$

Attach a genuine one-dimensional quantum system to the original system. This is a particle on a line, with
position $\hat q$ and momentum $\hat p$ obeying the ordinary canonical commutation relation $[\hat q,\hat p]=i$.
We call it the **clock**. The enlarged Hilbert space is $\HH\otimes L^2(\mathbb R)$. Define the single
operator
\begin{equation}
C \equiv K+\hat q ,
\label{eq:cp-constraint}
\end{equation}
and let $\widehat\M$ be the set of all operators in $\M\otimes B(L^2(\mathbb R))$ that commute with $C$. In
symbols, $a\in\widehat\M$ if and only if $[a,C]=0$.

Why is this the right condition? It is not obvious at first sight. The operator $C$ generates two translations
at once. The piece $K$ generates the modular flow. The piece $\hat q$ generates translations of the clock's
momentum. So $e^{iCs}$ shifts both by the same amount. Asking for invariance under $C$ therefore says that only
the *emph* reading, "clock minus modular time," matters, and neither one matters on its own.
Mathematically this is the same as the familiar idea that only relative positions matter, never the choice of
an origin for the coordinates. In the applications of Chapter~9, $\hat q$ is an observer's own energy and
$\hat p$ is the observer's proper time. There the invariance condition becomes the statement that physical
observables must be diffeomorphism-invariant: they cannot depend on an arbitrary choice of where to put the
zero of a clock.


> [!NOTE] **Physics Connection: this is the same trick as separating center-of-mass motion**
> You have already solved a version of this problem in a first mechanics course, in the two-body problem. Two
> particles have positions $x_1,x_2$ and momenta $p_1,p_2$. Their total momentum $P\equiv p_1+p_2$ generates a
> *emph* translation of both particles, $e^{iPs}$. This is the same job that $C=K+\hat q$ does here:
> it generates modular-time flow and clock translation together.
> 
> Suppose the Hamiltonian depends only on the relative coordinate $x_{\rm rel}\equiv x_1-x_2$. This is
> translation invariance: nothing picks out an absolute position. Then the useful, physically meaningful
> variables are the ones that are unchanged by the combined shift. These are the relative coordinate itself and
> the total momentum $P$. Check the elementary commutator directly:
> \begin{align}
> [x_{\rm rel},P] = [x_1-x_2,\,p_1+p_2]
> &\eqstep{1} [x_1,p_1] - [x_2,p_2]
> \ \eqstep{2}\ i - i = 0 . \notag
> \end{align}
> **(1)** expand the commutator term by term. The cross terms $[x_1,p_2]$ and $[x_2,p_1]$ vanish because the
> two particles are independent degrees of freedom.\quad
> **(2)** the canonical commutator $[x_j,p_j]=i$ for each particle separately.
> 
> So $x_{\rm rel}$ commutes with the generator of the shift that we want the physics to ignore. Below, the
> dressed operator $\widehat A=e^{iK\hat p}Ae^{-iK\hat p}$ plays exactly this role for $C$. The phrase ``translate
> both particles'' is replaced by "translate modular time and the clock together."
> 
> The center-of-mass coordinate $X_{\rm cm}$ behaves differently. It does *emph* commute with $P$. Instead
> $[X_{\rm cm},P]=i$, the ordinary canonical commutator. It plays the role that $\hat q$ would play if you forgot
> to dress it: an absolute reference that the physics was never supposed to depend on.
> 
> None of the mathematics here is new. The only new features are these. The "coordinate" being made relative
> is modular time, not ordinary position. And the "other particle" is the modular generator $K$, not a second
> physical body.


Two families of operators obviously satisfy $[a,C]=0$, and together they generate all of $\widehat\M$.

The first family is built from $\hat q$ itself. It commutes with $C=K+\hat q$, because $[\hat q,\hat q]=0$ and
$\hat q$ acts on a different tensor factor than $K$. So every bounded function of $\hat q$ belongs to
$\widehat\M$. An example is the unitary $e^{-i\hat qs}$.

The second family is the nontrivial one. An ordinary element $A\in\M$ does *emph* commute with $C$ by
itself. The reason is that $[A,K]\ne0$ in general; this is exactly what it means for $K$ to generate a
nontrivial flow on $A$. But a specific *emph* version of $A$ does commute with $C$:
\begin{equation}
[e^{iK\hat p}Ae^{-iK\hat p},\,C] = 0, \qquad A\in\M .
\label{eq:cp-dressed}
\end{equation}
This identity follows from the canonical commutation relations alone. Here is the calculation. Write
$\widehat A \equiv e^{iK\hat p}(A\otimes\id)e^{-iK\hat p}$. Because $[\hat q,\hat p]=i$, the position operator
acts on functions of $\hat p$ like a derivative:
$[\hat q, f(\hat p)] = i f'(\hat p)$. Apply this to the two exponentials. Since $K$ acts on $\HH$ and $\hat p$
acts on the clock, $K$ can be treated as a constant when differentiating with respect to $p$:
\begin{align}
[\hat q, \, e^{iK\hat p}] &\eqstep{a} i(iK)\,e^{iK\hat p} = -K e^{iK\hat p}, \notag\\
[\hat q, \, e^{-iK\hat p}] &\eqstep{b} i(-iK)\,e^{-iK\hat p} = K e^{-iK\hat p} . \notag
\end{align}
**(a)** $[\hat q,f(\hat p)]=if'(\hat p)$ with $f(p)=e^{iKp}$, so $f'(p)=iKe^{iKp}$.\quad
**(b)** the same rule with $f(p)=e^{-iKp}$, so $f'(p)=-iKe^{-iKp}$.

Now compute the commutator $[\hat q, \widehat A]$ with the product rule for commutators:
\begin{align}
[\hat q, \, \widehat A]
&\eqstep{1} [\hat q, \, e^{iK\hat p}](A\otimes\id)e^{-iK\hat p} + e^{iK\hat p}(A\otimes\id)[\hat q, \, e^{-iK\hat p}] \notag\\
&\eqstep{2} -K e^{iK\hat p}(A\otimes\id)e^{-iK\hat p} + e^{iK\hat p}(A\otimes\id) e^{-iK\hat p} K \notag\\
&\eqstep{3} -K \widehat A + \widehat A K \ =\ -[K, \, \widehat A] . \notag
\end{align}
**(1)** the product rule $[\hat q,XYZ]=[\hat q,X]YZ+X[\hat q,Y]Z+XY[\hat q,Z]$, with the middle term zero
because $[\hat q,A\otimes\id]=0$.\quad
**(2)** substitute (a) and (b). In the second term, $K e^{-iK\hat p}=e^{-iK\hat p}K$, because $K$ commutes
with any function of $K$ and $\hat p$.\quad
**(3)** both terms contain $e^{iK\hat p}(A\otimes\id)e^{-iK\hat p}=\widehat A$, by definition.

Now take the commutator with the full constraint $C = K + \hat q$:
\begin{align}
[C, \, \widehat A] = [K + \hat q, \, \widehat A]
&\eqstep{4} [K, \, \widehat A] + [\hat q, \, \widehat A]
\ \eqstep{5}\ [K, \, \widehat A] - [K, \, \widehat A] \ =\ 0 . \notag
\end{align}
**(4)** the commutator is linear in each slot, so it splits over the sum $K+\hat q$.\quad
**(5)** substitute $[\hat q,\widehat A]=-[K,\widehat A]$ from step (3).

The dressing by the clock momentum $\hat p$ exactly cancels the failure of $A$ to commute with $K$. So
$\widehat A$ is exactly invariant under $C$. The crossed product is therefore
\begin{equation}
\widehat\M = \big\{e^{iK\hat p}Ae^{-iK\hat p},\ e^{-i\hat qs} \ \big|\ A\in\M,\ s\in\mathbb R\big\}'' ,
\label{eq:cp-generators}
\end{equation}
the von Neumann algebra generated by the two families. A general element has the schematic form
$\widehat A=\int ds\,A(\hat p;s)\,e^{-i\hat qs}$. Here $A(\hat p;s)\equiv e^{iK\hat p}A(s)e^{-iK\hat p}$, built
from an operator-valued function $A(s)\in\M$. Since $\hat p$ is now an operator, $A(\hat p;s)$ is an operator
that depends on another operator, not on a fixed number. In the applications of Chapter~9, where $\hat p$ is an
observer's time, this means the operator is evaluated at a time that is itself quantum.

There is a second, equivalent description of the same algebra. It comes from the unitary change of frame
$U=e^{-iK\hat p}$, which maps $\widehat\M\to U\widehat\M U^\dagger$ and $C\to UCU^\dagger$. The same derivative
rule as in (a) gives $U\hat qU^\dagger=\hat q-K$, so $C\to\hat q$ and $e^{-i\hat qs}\to e^{i(K-\hat q)s}$. The
dressed operator $\widehat A$ goes back to the undressed $A$. This second form is more convenient for almost
everything that follows:
\begin{equation}
\begin{gathered}
\widehat\M = \big\{A,\ e^{i(K-\hat q)s} \ \big|\ A\in\M,\ s\in\mathbb R\big\}'', \\
\widehat A = \int ds\, A(s)\,e^{is(K-\hat q)}, \qquad A(s)\in\M .
\end{gathered}
\label{eq:cp-frame2}
\end{equation}
In this frame, ordinary (undressed) elements of $\M$ sit directly inside $\widehat\M$. All the dressing has
been moved into the clock-dependent generator $K-\hat q$. In this frame, $e^{i\hat qs}$ commutes with every
$A\in\M$, because they act on different factors. It also commutes with every $e^{i(K-\hat q)s'}$, because
$[K,\hat q]=0$. So $e^{i\hat qs}$ belongs to the commutant $\widehat\M'$. (This matches the constraint: in this
frame $C$ has become $\hat q$, and everything in $\widehat\M$ commutes with it.)

## $\widehat\M$ is always type II

### Finding the modular operator of $\widehat\M$

Now set $K=-\log\Delta_\Psi$, the modular generator of $\M$. Work in the frame \eqref{eq:cp-frame2} and take the
reference vector
\begin{equation}
\ket{\widehat\Psi} = \ket\Psi\otimes\ket{p=0} .
\label{eq:cp-refvector}
\end{equation}
The clock is in a state of definite momentum, so it is completely spread out in position. This vector cannot be
normalized: it is a plane wave. Strictly speaking it defines a *emph* rather than a state. This technical
point does not change any conclusion below. The vector $\ket{\widehat\Psi}$ is cyclic and separating for
$\widehat\M$ (a standard fact that we quote), so Tomita—Takesaki theory applies. The modular operator
$\widehat\Delta$ can then be found from the KMS relation that characterizes it,
\begin{equation}
\braket{\widehat\Psi|\widehat A\widehat B|\widehat\Psi}=\braket{\widehat\Psi|\widehat B\,\widehat\Delta\,
\widehat A|\widehat\Psi} ,
\label{eq:cp-kms}
\end{equation}
or, equivalently, from the Tomita operator $\widehat S$. The calculation below shows a clean cancellation.

\begin{keyresult}[: Derivation of the Crossed Product Modular Operator $\widehat\Delta$]
**Goal:** On $\widehat\HH = \HH \otimes L^2(\mathbb{R})$ with reference vector $\ket{\widehat\Psi} = \ket\Psi \otimes \ket{p=0}$, find the Tomita operator $\widehat S$ and show that the modular operator is

$$

\widehat\Delta \equiv \widehat S^\dagger \widehat S = \Delta_\Psi \otimes \id = \Delta_\Psi .

$$

**Derivation:**

1. **A general operator acting on the reference vector.**
In the frame \eqref{eq:cp-frame2}, a general operator $\widehat A \in \widehat\M$ has the form

$$

\widehat A = \int_{-\infty}^\infty ds \, A(s) \, e^{is(K - \hat q)}, \qquad A(s) \in \M .

$$

Act with $\widehat A$ on $\ket{\widehat\Psi} = \ket\Psi \otimes \ket{p=0}$. Two facts are needed. First, $K = -\log\Delta_\Psi$ and $\Delta_\Psi\ket\Psi = \ket\Psi$, so the modular Hamiltonian annihilates the state: $K\ket\Psi = 0$, and therefore $e^{is K}\ket\Psi = \ket\Psi$. Second, on the clock $\hat q = i\partial_p$ in the momentum representation, so $e^{-is\hat q}$ shifts the clock momentum:

$$

e^{-is\hat q}\ket{p=0} = \ket{p = -s} .

$$

Since $K$ and $\hat q$ act on different factors, they commute, and
\begin{align}
e^{is(K - \hat q)}\ket{\widehat\Psi}
&\eqstep{1} \big(e^{is K}\ket\Psi\big) \otimes \big(e^{-is\hat q}\ket{p=0}\big)
\ \eqstep{2}\ \ket\Psi \otimes \ket{p = -s} . \notag
\end{align}
**(1)** $[K,\hat q]=0$, so the exponential factorizes into a piece acting on $\HH$ and a piece acting on
the clock.\quad
**(2)** $e^{isK}\ket\Psi=\ket\Psi$ and $e^{-is\hat q}\ket{p=0}=\ket{p=-s}$, both shown just above.

Now multiply by $A(s) \in \M$ and integrate:
\begin{align}
\widehat A \ket{\widehat\Psi}
&\eqstep{3} \int_{-\infty}^\infty ds \, A(s)\ket\Psi \otimes \ket{p = -s}
\ \eqstep{4}\ \int_{-\infty}^\infty dp \, A(-p)\ket\Psi \otimes \ket{p} . \notag
\end{align}
**(3)** substitute the result of steps (1)—(2) inside the $s$ integral.\quad
**(4)** change the integration variable to $p=-s$. The sign from $dp=-ds$ cancels the sign from swapping
the limits.

So the clock momentum $p$ labels the different pieces $A(s)$ of the operator: the component at clock momentum
$p$ is $A(-p)\ket\Psi$.
2. **The adjoint $\widehat A^\dagger$ acting on the reference vector.**
The adjoint is

$$

\widehat A^\dagger = \int_{-\infty}^\infty ds \, e^{-is(K - \hat q)} A(s)^\dagger .

$$

Insert $\id=e^{is(K-\hat q)}e^{-is(K-\hat q)}$ to the right of $A(s)^\dagger$:

$$

\widehat A^\dagger = \int_{-\infty}^\infty ds \, \Big( e^{-is(K - \hat q)} A(s)^\dagger e^{is(K - \hat q)} \Big) e^{-is(K - \hat q)} .

$$

Since $[\hat q, A(s)^\dagger] = 0$, the conjugation in brackets is just the modular flow of the original algebra $\M$:
\begin{align}
e^{-is(K - \hat q)} A(s)^\dagger e^{is(K - \hat q)}
&\eqstep{5} e^{-is K} A(s)^\dagger e^{is K}
\ \eqstep{6}\ \Delta_\Psi^{is} A(s)^\dagger \Delta_\Psi^{-is} \equiv \alpha_{-s}\big(A(s)^\dagger\big) . \notag
\end{align}
**(5)** $\hat q$ commutes with $A(s)^\dagger$ and with $K$, so the $\hat q$ exponentials cancel against each
other.\quad
**(6)** $K=-\log\Delta_\Psi$, so $e^{-isK}=\Delta_\Psi^{is}$.

The last factor $e^{-is(K-\hat q)}$ acts on $\ket{\widehat\Psi}$ as in step (2), with $s\to-s$, and gives $\ket\Psi\otimes\ket{p=s}$. Hence

$$

\widehat A^\dagger \ket{\widehat\Psi} = \int_{-\infty}^\infty ds \, \alpha_{-s}\big(A(s)^\dagger\big)\ket\Psi \otimes \ket{p = s} .

$$

Now use $\Delta_\Psi^{-is}\ket\Psi = \ket\Psi$ and the definition of the Tomita operator, $S_\Psi A\ket\Psi = A^\dagger\ket\Psi$:

$$

\alpha_{-s}\big(A(s)^\dagger\big)\ket\Psi = \Delta_\Psi^{is} A(s)^\dagger\ket\Psi = \Delta_\Psi^{is} S_\Psi A(s)\ket\Psi .

$$

3. **The Tomita operator $\widehat S$.**
The Tomita operator of $\widehat\M$ is defined by $\widehat S(\widehat A\ket{\widehat\Psi}) = \widehat A^\dagger\ket{\widehat\Psi}$. Compare the two results. The input has the vector $A(s)\ket\Psi$ at clock momentum $p=-s$. The output has the vector $\Delta_\Psi^{is}S_\Psi A(s)\ket\Psi$ at clock momentum $p=+s$. Three things happen. The clock momentum is reflected, $p\to-p$; call this reflection $\mathcal{P}_p \ket{p} \equiv \ket{-p}$. The $\HH$ part is acted on by $S_\Psi$. Finally, the component at clock momentum $p$ is multiplied by $\Delta_\Psi^{ip}$. So

$$

\widehat S = \Delta_\Psi^{i\hat p}\,\big(S_\Psi \otimes \mathcal{P}_p\big) ,

$$

where $\Delta_\Psi^{i\hat p}=e^{-iK\hat p}$ is a unitary operator. (One can check that $S_\Psi$ commutes with $\Delta_\Psi^{is}$ for real $s$, so the order of $S_\Psi$ and $\Delta_\Psi^{ip}$ at fixed $p$ does not matter.)
4. **Cancellation in the modular operator.**
Now evaluate the modular operator $\widehat\Delta \equiv \widehat S^\dagger \widehat S$:
\begin{align}
\widehat\Delta
&\eqstep{7} \big(S_\Psi^\dagger \otimes \mathcal{P}_p^\dagger\big)\,\Delta_\Psi^{-i\hat p}\,\Delta_\Psi^{i\hat p}\,\big(S_\Psi \otimes \mathcal{P}_p\big) \notag\\
&\eqstep{8} \big(S_\Psi^\dagger S_\Psi\big) \otimes \big(\mathcal{P}_p^\dagger \mathcal{P}_p\big)
\ \eqstep{9}\ \Delta_\Psi \otimes \id_{L^2(\mathbb{R})} = \Delta_\Psi . \qquad \blacksquare \notag
\end{align}
**(7)** the adjoint of a product reverses the order, and $(\Delta_\Psi^{i\hat p})^\dagger=\Delta_\Psi^{-i\hat p}$.\quad
**(8)** the unitary factor cancels, $\Delta_\Psi^{-i\hat p}\Delta_\Psi^{i\hat p}=\id$; then products of tensor products multiply factor by factor.\quad
**(9)** $S_\Psi^\dagger S_\Psi=\Delta_\Psi$ is the definition of the modular operator, and the reflection
$\mathcal P_p$ is unitary, $\mathcal P_p^\dagger\mathcal P_p=\id_{L^2(\mathbb R)}$.

\end{keyresult}

The answer is very simple, given how much machinery went into building $\widehat\M$:
\begin{equation}
\widehat\Delta = \Delta_\Psi .
\label{eq:cp-modop}
\end{equation}
**In this reference vector, the modular operator of the new algebra is the same operator as the modular
operator of the original algebra.** Nothing new had to be invented. The crossed product inherits its modular
structure directly from $\M$.

### Why this forces type II

The key algebraic step is short. Start from $\widehat\Delta=e^{-K}$ and split the exponential:
\begin{equation}
\widehat\Delta = e^{-K} = e^{-(K-\hat q)}e^{-\hat q} \equiv \rho\rho'^{-1}, \qquad
\rho\equiv e^{-(K-\hat q)}, \quad \rho'\equiv e^{\hat q} .
\label{eq:cp-factorization}
\end{equation}
Splitting the exponential is allowed because $K$ and $\hat q$ commute. Hence

$$

\widehat\Delta^{-is} = e^{i(K-\hat q)s}\,e^{i\hat qs} .

$$

Now compare the two factors on the right with the descriptions of $\widehat\M$ and its commutant. The factor
$e^{i(K-\hat q)s}$ is a unitary inside $\widehat\M$ itself; it is one of the generators in
\eqref{eq:cp-frame2}. The factor $e^{i\hat qs}$ is a unitary inside the commutant $\widehat\M'$. **So
$\widehat\Delta^{-is**$ is a unitary in $\widehat\M$ times a unitary in $\widehat\M'$.}

When we conjugate an element of $\widehat\M$ by $\widehat\Delta^{-is}$, the factor in $\widehat\M'$ commutes
with it and drops out. So the modular flow of $\widehat\M$ is implemented by a unitary that lies inside
$\widehat\M$. This is the definition of an *emph* automorphism. By the criterion
\eqref{eq:inner-criterion} of Chapter~4, the modular flow is inner for *emph* $s$ if and only if the
algebra is type I or type II, never type III. **So $\widehat\M$ cannot be type III**, whatever $\M$ was.
No explicit trace was needed for this step. It followed only from identifying the modular operator and checking
the inner-automorphism criterion.

It remains to rule out type I. Here is an intuitive reason, which is not a proof. Attaching a clock and
imposing an invariance condition does not create a tensor factorization of $\widehat\HH=\HH\otimes
L^2(\mathbb R)$ adapted to $\widehat\M$. The obstruction that made $\M$ type III is still present.

A sharper argument works when $\widehat\M$ is a factor, which is the case when $\M$ is type $\mathrm{III}_1$.
Shift the clock by conjugating with $e^{i\hat ps}$, which sends $\hat q\to\hat q+s$. This maps $\widehat\M$ to
itself: each $A\in\M$ is unchanged, and $e^{i(K-\hat q)t}$ only picks up a phase $e^{-ist}$. Using the trace
\eqref{eq:cp-trace} constructed in the next subsection, together with $e^{-i\hat ps}\ket{p=0}=\ket{p=0}$, one
finds that this shift multiplies the trace by $e^{s}$. In a type I factor $B(\mathcal K)$ every automorphism has
the form $X\to VXV^\dagger$ with $V$ unitary, and such a map never changes the trace. So a type I factor has no
automorphism that rescales its trace, and $\widehat\M$ cannot be type I. **By elimination, $\widehat\M$ is
type II.** For a type $\mathrm{III}_1$ factor $\M$, the crossed product is a type $\mathrm{II}_\infty$ factor.
For the other type III subtypes, $\widehat\M$ is still type II but has a nontrivial center. That last statement
is a standard theorem of Takesaki that we quote without proof.

### Building the trace explicitly, and checking cyclicity by hand

We now know *emph* a trace exists. It is useful to write one down and check that it works. Define
\begin{equation}
\tr\widehat A \equiv \braket{\widehat\Psi|\widehat A\,\rho^{-1}|\widehat\Psi} ,
\label{eq:cp-trace}
\end{equation}
with $\rho=e^{-(K-\hat q)}$ from \eqref{eq:cp-factorization}. The motivation is as follows. If a trace exists,
expectation values in the reference vector should have the form $\braket{A}=\tr(A\rho)$ for some density
operator $\rho$. So to recover the trace from an expectation value, one removes $\rho$ by multiplying with
$\rho^{-1}$.

Cyclicity means $\tr(\widehat A\widehat B)=\tr(\widehat B\widehat A)$. It follows from nothing more than the
KMS relation \eqref{eq:cp-kms}. In the chain below, $\braket{\cdots}$ is shorthand for
$\braket{\widehat\Psi|\cdots|\widehat\Psi}$:
\begin{align}
\tr(\widehat A\widehat B) = \braket{\widehat A\widehat B\rho^{-1}}
&\eqstep{1} \braket{\widehat B\rho^{-1}\widehat\Delta\,\widehat A} \notag\\
&\eqstep{2} \braket{\widehat B\rho'^{-1}\widehat A}
\ \eqstep{3}\ \braket{\widehat B\widehat A\rho'^{-1}}
\ \eqstep{4}\ \tr(\widehat B\widehat A) . \notag
\end{align}
**(1)** the KMS relation \eqref{eq:cp-kms}, with $\widehat A$ as the first operator and $\widehat B\rho^{-1}$
as the second. This is allowed because $\rho^{-1}=e^{K-\hat q}$ is built from a generator of $\widehat\M$.\quad
**(2)** $\rho^{-1}\widehat\Delta=\rho^{-1}\rho\rho'^{-1}=\rho'^{-1}$, directly from the factorization
$\widehat\Delta=\rho\rho'^{-1}$.\quad
**(3)** $\rho'^{-1}=e^{-\hat q}$ is built from the commutant $\widehat\M'$. So it commutes with $\widehat A\in
\widehat\M$ and can be moved to the far right.\quad
**(4)** since $K\ket\Psi=0$, we have $\rho^{-1}\ket{\widehat\Psi}=e^{K-\hat q}\ket{\widehat\Psi}=e^{-\hat q}
\ket{\widehat\Psi}=\rho'^{-1}\ket{\widehat\Psi}$. So $\braket{\widehat B\widehat A\rho'^{-1}}=
\braket{\widehat B\widehat A\rho^{-1}}$, which is the definition \eqref{eq:cp-trace} of $\tr(\widehat B\widehat
A)$.

Every step is either a definition or something already established. No new assumption enters. (The
manipulations are formal, since $\rho^{-1}$ is unbounded and $\ket{\widehat\Psi}$ is not normalizable, but they
can be made precise.) The same mechanism appeared in a much more concrete setting in Chapter~3. There the trace
on the infinite chain of maximally entangled Bell pairs was checked to be cyclic by explicit $2\times2$ matrix
computation. In both cases the consistency conditions of a specific reference state force cyclicity. Here the
argument is written in the general language of modular theory, which also works for type III, rather than
worked out on small matrices.

### Type $\mathrm{II}_\infty$, or type $\mathrm{II}_1$ if the clock's energy is bounded below

Evaluate the trace \eqref{eq:cp-trace} on the identity. Since $K\ket\Psi=0$, only the clock factor $e^{-\hat q}$
acts nontrivially. A plane wave has $|\braket{q|p=0}|^2=1/2\pi$ at every $q$, so

$$

\tr(\id) = \braket{p=0|e^{-\hat q}|p=0} = \frac{1}{2\pi}\int_{-\infty}^\infty dq\,e^{-q} = \infty .

$$

The trace of the identity diverges. So, by the classification of Chapter~2, $\widehat\M$ is type
$\mathrm{II}_\infty$.

The divergence comes from the range of the clock variable. In the construction above, the clock's
"energy" $\hat q$ is like the position $x$, or the momentum $p$, of a particle on a line. Its spectrum is the
whole real line, and the weight $e^{-q}$ blows up as $q\to-\infty$. That is what gives type
$\mathrm{II}_\infty$.

There is a simple, physically motivated fix, used again in Chapter~9. Require the clock's energy to be bounded
below, $q\ge0$. This says that a real observer's energy cannot be negative, which is a reasonable requirement
for any physical clock. For example, an observer whose energy is a kinetic energy $p^2/2m\ge0$ has possible
energies filling the half-line $[0,\infty)$, not the whole line.

To impose this, insert a projector. In the frame \eqref{eq:cp-generators}, the operator $\hat q$ itself
belongs to $\widehat\M$, and the projector is $\Pi=\theta(\hat q)$. Here $\theta$ is the step function, equal to
$1$ for $q\ge0$ and $0$ for $q<0$. Define $\widehat\M_+\equiv\Pi\widehat\M\Pi$. In that frame it acts on the
smaller Hilbert space $\HH\otimes L^2(\mathbb R_{>0})$. In the frame \eqref{eq:cp-frame2}, where the trace formula
is written, the same projector reads $\Pi=\theta(\hat q-K)$. This is a function of the generator $K-\hat q$, so
it lies in $\widehat\M$, and it acts on $\ket{\widehat\Psi}$ as $\theta(\hat q)$ because $K\ket\Psi=0$. The
identity element of $\widehat\M_+$ is $\Pi$, and
\begin{align}
\tr_{\widehat\M_+}(\id)
&\eqstep{1} \tr_{\widehat\M}(\Pi)
\ \eqstep{2}\ \frac{1}{2\pi}\int_{-\infty}^\infty dq\,e^{-q}\theta(q)
\ \eqstep{3}\ \frac{1}{2\pi}\int_0^\infty dq\,e^{-q} = \frac{1}{2\pi} . \notag
\end{align}
**(1)** the identity of $\widehat\M_+$ is the projector $\Pi$, viewed as an element of $\widehat\M$.\quad
**(2)** the trace formula \eqref{eq:cp-trace}; acting on $\ket{\widehat\Psi}$, the projector inserts the
factor $\theta(q)$ into the clock integral.\quad
**(3)** $\theta(q)$ cuts the integration range down to $q\ge0$.

The result is finite. A trace is only defined up to an overall positive constant, so multiplying it by $2\pi$
normalizes it to $\tr(\id)=1$. **So restricting the observer's clock to positive energy is exactly the
algebraic step that turns type $\mathrm{II**_\infty$ into type $\mathrm{II}_1$.}

The same condition decides whether an ordinary Gibbs state exists. A partition function $Z=\Tr\,e^{-\beta H}$
can converge only if $H$ is bounded below. For the harmonic oscillator, with energies $\omega(n+\tfrac12)$ for
$n\ge0$, the geometric sum converges. For a Hamiltonian whose spectrum runs down to $-\infty$, the weights
$e^{-\beta E}$ grow without bound and $Z=\infty$. An example is a particle in a linear potential $V=-Fx$ on the
whole line: its spectrum is all of $\mathbb R$. The two integrals $\int_0^\infty e^{-q}\,dq$ (finite) and
$\int_{-\infty}^\infty e^{-q}\,dq$ (infinite) express the same fact for the clock, whose "energy" is $\hat q$.

One caution about the analogy. Being bounded below is necessary for a finite $Z$, but it is not sufficient. A
free particle on the whole line has $p^2/2m\ge0$, yet its thermal $Z$ is infinite, because the infinite volume
gives infinitely many states in any energy window. The clock trace has no such volume factor: it weights each
value of $q$ with the flat measure $dq/2\pi$. So for the clock, the lower bound on the spectrum is the only
thing that matters.

This fork has real physical consequences. Black-hole entropy (type $\mathrm{II}_\infty$) and de~Sitter entropy
(type $\mathrm{II}_1$) sit on opposite sides of it, as Chapter~9 shows.

### The crossed product does not depend on the reference state

The construction used a specific cyclic and separating vector $\ket\Psi$ to define the modular generator $K$.
Choosing a different vector $\ket\Phi$ gives only a *emph* algebra,

$$

\widehat\M_\Phi = u'_{\Phi\Psi}(\hat p)\,\widehat\M_\Psi\,u_{\Phi\Psi}'^\dagger(\hat p) .

$$

Here $u'_{\Phi\Psi}$ is the intertwining unitary of relative modular theory (Chapter~4). It relates the
modular flows of the two states. In the formula above, its flow parameter is replaced by the clock momentum
operator $\hat p$. The computation that proves this is a direct but somewhat long manipulation of the relative
modular identities of Chapter~4, and we do not reproduce it. What matters is the conclusion: up to unitary
equivalence, $\widehat\M$ is an *emph* invariant of $\M$ alone.

## Density operator for $\widehat\M$ in a general semiclassical state

With a trace in hand, the tools of Chapter~3 become available for $\widehat\M$. In particular, a density
operator $\rho_{\widehat\M}$ for a state is defined by $\tr(A\rho_{\widehat\M})=\braket{\text{state}|A|
\text{state}}$ for all $A\in\widehat\M$. Consider the physically motivated class of states
\begin{equation}
\ket{\widehat\Phi}=\ket\Phi\otimes\ket g ,
\label{eq:cp-semiclassical}
\end{equation}
where $\ket g$ is a fixed clock wavefunction. It is normalized, $\int dq\,|g(q)|^2=1$, and nonzero everywhere.

Solving the defining equation for the density operator is a longer computation. It uses the two-state KMS
relation of relative modular theory (Chapter~4) twice. It also uses the explicit form
$\braket{q|e^{-iK\hat p}|g}=g(q-K)$, which describes how the clock wavefunction changes between the two frames
\eqref{eq:cp-generators} and \eqref{eq:cp-frame2}. Once the KMS relation is accepted, the rest is mostly
bookkeeping, and we do not reproduce it. The result is clean [CLPW]:
\begin{equation}
\rho_{\widehat\Phi} = 2\pi\, g(\hat q-K)\,e^{\hat q}\,\Delta_{\Phi\Psi}\, g^*(\hat q-K) .
\label{eq:cp-density}
\end{equation}
This expression is written in the frame \eqref{eq:cp-frame2}, the same frame as the trace
\eqref{eq:cp-trace}. (There, $\hat q-K$ is minus the generator $K-\hat q$, so functions of it lie in
$\widehat\M$.) The expression in the other frame follows by conjugating with $U^\dagger$. It is an explicit
operator with three ingredients: the clock wavefunction $g$; the factor $e^{\hat q}$, which comes from the
normalization of the trace; and the relative modular operator $\Delta_{\Phi\Psi}$ of Chapter~4, which compares
the state of interest $\Phi$ with the reference $\Psi$ used to build the crossed product. The factor $2\pi$
matches the $1/2\pi$ in the plane-wave normalization used for the trace.

## Entanglement entropy for $\widehat\M$ in a general semiclassical state

### The final formula, and why it has exactly the shape it does

Insert $\rho_{\widehat\Phi}$ into the ordinary entropy formula, $S_{\widehat\M}=-\tr(\rho_{\widehat\Phi}\log
\rho_{\widehat\Phi})$. Then specialize to a **semiclassical** clock wavefunction. This means one that
varies slowly, with $g'(q)\propto\epsilon$ for a small parameter $\epsilon$, and we work to leading order in
$\epsilon$. The expansion has three steps. First, expand $-\log\rho_{\widehat\Phi}$ using the relative-modular
identity $K_{\Phi\Psi}=K_\Phi+K-K_{\Psi\Phi}$ of Chapter~4. Second, evaluate the resulting expectation value
term by term, using $K_\Phi\ket\Phi=0$. Third, recognize the surviving piece as the relative entropy of
Chapter~4. The result, due to Chandrasekaran, Longo, Penington and Witten [CLPW], is
\begin{equation}
\begin{gathered}
S_{\widehat\M}(\widehat\Phi) = -S_\M(\Phi\|\Psi) - \bar q + S_o, \\
\bar q = \int dq\,q\,|g(q)|^2, \qquad S_o = -\int dq\,|g(q)|^2\log|g(q)|^2 .
\end{gathered}
\label{eq:cp-entropy}
\end{equation}
Here $\bar q$ is the mean clock reading in the probability distribution $|g(q)|^2$. The quantity $S_o$ is the
ordinary (differential) Shannon entropy of that same distribution. Both depend only on the shape of the clock
wavefunction $g$, not on the state $\Phi$. (The formula holds up to an additive constant, which depends on how
the trace is normalized.)

**Up to terms fixed entirely by the clock, the entropy of the type II crossed-product algebra is minus
the type III relative entropy of the original algebra $\M$.** This closes the loop opened in Chapter~4. There,
relative entropy was introduced as the one entropy-like quantity that survives in type III, where ordinary
entropy does not. Now it turns out to *emph* an ordinary entropy, of a different and larger algebra built by
attaching a clock.

\begin{workedexamplebox}[: the clock terms of the entropy formula, from a Gaussian clock]
The clock terms $-\bar q+S_o$ in \eqref{eq:cp-entropy} can be checked on a fully explicit example. Take
$\Phi=\Psi$, so the relative-entropy term is zero. Then look only at the operators in $\widehat\M$ that are
functions of $X\equiv\hat q-K$ (in the frame \eqref{eq:cp-frame2}). These form a commutative subalgebra, so
this is a toy calculation on a subalgebra, not the full entropy of $\widehat\M$. It does check where the clock
terms come from.

*emph* Since $K\ket\Psi=0$, a function $f(X)$ acts on $\ket{\widehat\Psi}$ as
$f(\hat q)$. With $|\braket{q|p=0}|^2=1/2\pi$, the trace \eqref{eq:cp-trace} becomes

$$

\tr f(X) = \frac{1}{2\pi}\int dq\,e^{-q}f(q) .

$$

*emph* For $\Phi=\Psi$ we have $\Delta_{\Phi\Psi}=\Delta_\Psi=e^{-K}$, and
\eqref{eq:cp-density} reduces to $\rho(X)=2\pi\,|g(X)|^2e^{X}$. Check that it reproduces the state:
\begin{align}
\tr\big(\rho(X)f(X)\big)
&\eqstep{1} \frac{1}{2\pi}\int dq\,e^{-q}\,2\pi|g(q)|^2e^{q}f(q)
\ \eqstep{2}\ \int dq\,|g(q)|^2f(q) . \notag
\end{align}
**(1)** the trace formula just derived, applied to the function $\rho f$.\quad
**(2)** the factors $2\pi$ and $e^{\pm q}$ cancel.

The right side is the expectation value of $f(X)$ in $\ket\Psi\otimes\ket g$, because $X$ acts on that vector
as $\hat q$ and the clock distribution is $|g(q)|^2$. With $f=1$ this also gives $\tr\rho=1$.

*emph*
\begin{align}
-\tr(\rho\log\rho)
&\eqstep{3} -\int dq\,|g(q)|^2\big(\log 2\pi+\log|g(q)|^2+q\big) \notag\\
&\eqstep{4} -\bar q + S_o - \log 2\pi . \notag
\end{align}
**(3)** apply step (2) with $f=\log\rho=\log2\pi+\log|g|^2+X$.\quad
**(4)** $\int|g|^2=1$, and the definitions of $\bar q$ and $S_o$ in \eqref{eq:cp-entropy}.

The constant $-\log2\pi$ disappears if the trace is rescaled by $2\pi$. So the clock terms have exactly the
shape $-\bar q+S_o$.

*emph* Take a Gaussian clock distribution of width $\sigma$ centered at $\bar q_0$,
$|g(q)|^2=\frac{1}{\sqrt{2\pi}\sigma}\exp\!\big(-(q-\bar q_0)^2/2\sigma^2\big)$. Then $\bar q=\bar q_0$ and
$S_o=\tfrac12\log(2\pi e\sigma^2)$, so

$$

-\tr(\rho\log\rho) = -\bar q_0 + \tfrac12\log(2\pi e\sigma^2) - \log 2\pi .

$$

We checked this numerically by doing the $q$ integrals directly (for $\bar q_0=0.4$, $\sigma=0.8$), and also
checked $\tr\rho=1$. This example tests the clock terms only. The relative-entropy term, which needs
$\Phi\ne\Psi$ and the full non-commutative algebra, is not tested by it.
\end{workedexamplebox}

\bigskip
\noindent This completes the operator-algebra toolkit of Chapters~2—5. A type III algebra has no trace and no
entropy of its own. But it can always be crossed with its own modular group to produce a type II algebra that
has both. And the entropy of that type II algebra is the relative entropy of the original algebra, in disguise.
Chapter~6 applies all of these tools (the type classification, modular theory, and the crossed product) to the
large-$N$ limit of the AdS/CFT correspondence.



---

# AdS/CFT in the large-$N$ limit: an algebraic formulation

Chapters~2—5 developed their tools on their own terms. They used nothing more exotic than qubits, matrix
algebras, and (in Chapter~4) an ordinary free quantum field. This chapter applies all of those tools (the type
classification, the GNS construction, modular theory, and the crossed product) to the physical system these notes
are aiming at. That system is the AdS/CFT correspondence, in the limit $N\to\infty$, or equivalently $G_N\to0$,
where bulk spacetime is supposed to emerge.

## General description

### The dictionary, restated precisely

AdS/CFT is a conjecture. It says that quantum gravity on $(d{+}1)$-dimensional anti-de~Sitter space (AdS) is
completely equivalent to an ordinary conformal field theory (CFT), without gravity, living on the
$d$-dimensional boundary of that space. The standard example is type IIB string theory on
$\text{AdS}_5\times S^5$, which is dual to $\mathcal N=4$ super-Yang-Mills theory with gauge group $SU(N)$.

The core entries of the dictionary are these.

- The two theories share the same Hilbert space, $\HH_{\text{bulk}}=\HH_{\text{CFT}}\equiv\HH$.
- The classical-gravity limit $G_N\to0$ is the same as the large-$N$ limit of the boundary gauge theory.
- The limit $\alpha'\to0$ is the same as the limit of infinite 't~Hooft coupling, $\lambda\to\infty$, in the
boundary theory. Here $\alpha'$ sets the string length, so $\alpha'\to0$ switches off stringy corrections.
- Elementary bulk fields correspond to **single-trace operators**. These are boundary operators built as
a single trace over color indices, $\Tr(\cdots)$.
- A classical bulk geometry $\phi_c$ corresponds to a specific boundary state $\ket\Psi$, called a
**semiclassical state**.


The precise map from bulk fields to boundary operators is the **extrapolate dictionary**:
\begin{equation}
O(x) = \lim_{r\to\infty} r^\Delta\,\phi(r,x) .
\label{eq:ads-extrapolate}
\end{equation}
In words: take a bulk field $\phi$ and evaluate it at radial coordinate $r$ and boundary point $x$. Multiply by
$r^\Delta$, where $\Delta$ is the conformal dimension of the operator, a number fixed by the mass of the field.
Then send $r\to\infty$, which moves the point out to the AdS boundary. What survives this limit is the
corresponding boundary operator $O(x)$.

This equation is not just a convenient definition. In some holographic theories an independent definition of
$O(x)$ already exists, such as $\Tr(\cdots)$ in super-Yang-Mills. There, \eqref{eq:ads-extrapolate} is a derived
fact. In more general holographic systems no such independent definition is available. There,
\eqref{eq:ads-extrapolate} *emph* taken as the definition of what counts as a single-trace operator.

A semiclassical state $\ket\Psi$ is one with a well-defined $N\to\infty$ limit. This means it can be built as
the limit of a sequence of states $\{\ket{\Psi_N}\}$, one for each finite-$N$ theory. This chapter works out two
examples. The first is the vacuum $\ket\Omega$, dual to empty AdS. The second is the thermofield double
$\ket{\Psi_\beta}$, which at high enough temperature is dual to an eternal black hole. A third example is a
single-sided black hole formed by collapse. It is generally harder to write down explicitly.

### Building the boundary operator algebra with GNS, and why it can be bigger than expected

Here the tools of Chapters~2 and~4 are used directly. Say that an operator $A$ has a well-defined large-$N$
limit in the state $\ket\Psi$ if two things hold. First, $A$ is the limit of some sequence of finite-$N$
operators $\{A_N\}$, with corresponding states $\{\ket{\Psi_N}\}$. Second, the expectation values converge to
something finite:

$$

\lim_{N\to\infty}\braket{\Psi_N|A_N|\Psi_N}<\infty .

$$

This is the same kind of finite-energy restriction met for the infinite chain of Bell pairs in Chapters~1
and~2, now applied to a real gauge theory. Call the collection of all such operators $\Alg_\Psi$. One subset is
present for every semiclassical state:

$$

\Sscr \equiv \text{the } *\text{-algebra generated by single-trace operators} \subseteq \Alg_\Psi .

$$

The inclusion need not be an equality. The set $\Alg_\Psi$ may contain *emph* operators than those built
from single-trace operators, and which extra operators survive can depend on the state $\Psi$. This point is
easy to skip on a first reading. But the fact that the inclusion can be strict turns out to be exactly what
allows a description of a black-hole *emph*. This is discussed in the section on general black holes
below.

Assume that $\Alg_\Psi$ is closed under products, so it is a $*$-algebra. Assume also that it is completed in
the norm it inherits, so it is a $C^*$-algebra, exactly the kind of object studied in Chapter~2. Then
expectation values in $\ket\Psi$ define a state $\omega_\Psi$ on $\Alg_\Psi$. The GNS construction of Chapter~2
applies directly. It gives a GNS Hilbert space $\HH_\Psi^{\text{GNS}}$ built from $(\Alg_\Psi,\omega_\Psi)$,
together with a representation $\pi_\Psi(\Alg_\Psi)$. This Hilbert space is, quite literally, ``the space of
small excitations around $\ket\Psi$.'' It is the same construction that Chapter~2 carried out by hand on qubits.

Suppose the bulk geometry dual to $\Psi$ is smooth and $\Psi$ is pure. Then $\omega_\Psi$ is expected to be a
pure state on $\Alg_\Psi$. Chapter~2 showed that a pure state gives an irreducible GNS representation. So
\begin{equation}
B(\HH_\Psi^{\text{GNS}})=\pi_\Psi(\Alg_\Psi)'' .
\label{eq:ads-irreducible}
\end{equation}
This can fail if the dual geometry has a singularity that can be reached on some Cauchy slice. We return to
this in the discussion of firewalls later in this chapter. Write

$$

Y\equiv(\pi_\Psi(\Sscr))'', \qquad Y_O\equiv(\pi_\Psi(\Sscr_O))''

$$

for the von Neumann algebra generated by single-trace operators alone, and for its restriction to a boundary
region $O$. The algebra $Y$ may be strictly smaller than $\pi_\Psi(\Alg_\Psi)''$.

### Matching this to an ordinary bulk Fock space

On the gravity side, expand every bulk field around its classical background:
$\phi=\phi_c+\kappa\delta\phi$, with $\kappa=\sqrt{8\pi G_N}$. This gives an action
$S[\phi_c]+S_2[\delta\phi]+S_{\text{int}}[\delta\phi]$, with $S_{\text{int}}=\kappa S_3+\kappa^2S_4+\cdots$. At
leading order, $\kappa\to0$, only the quadratic piece $S_2$ survives. It describes an ordinary free quantum field
$\delta\phi$ on the fixed background $\phi_c$. Quantizing it in the standard way, with some vacuum
$\ket0_{\phi_c}$, gives a Fock space $\HH_\Psi^{\text{Fock}}$.

We now have two Hilbert spaces. One is built from the boundary algebra by GNS. The other is built from the bulk
field theory by ordinary quantization. For the AdS/CFT duality to hold, they must agree:
\begin{equation}
\HH_\Psi^{\text{Fock}} = \HH_\Psi^{\text{GNS}} .
\label{eq:ads-fock-gns}
\end{equation}
This requires the GNS representation to have exactly the structure of a Fock space. In other words, the
boundary theory must be Gaussian at large $N$: all correlators must factorize into products of two-point
functions. This property is called "large-$N$ factorization." It follows from 't~Hooft's planar scaling, as
the following sketch shows.

\begin{keyresult}[: Sketch of the large-$N$ generalized free field and its CCR algebra]
**Goal:** Explain why, in a large-$N$ $SU(N)$ gauge theory with fixed 't~Hooft coupling $\lambda = g_{YM}^2 N$:

1. Connected correlators of $n$ single-trace operators scale as $\braket{\mathcal{O}_1 \cdots \mathcal{O}_n}_{\text{conn}} \sim N^{2-n}$.
2. Commutators of single-trace operators become $c$-numbers: $[\mathcal{O}_A, \mathcal{O}_B] = c_{AB}\id + O(1/N)$.
3. The resulting boundary algebra is a CCR algebra, whose GNS space is a free Fock space $\HH_\Psi^{\text{Fock}}$.

This is a standard diagrammatic argument, not a rigorous proof.

**Derivation sketch:**

1. **The 't~Hooft topological expansion.**
Consider an adjoint matrix field theory with action $S = \frac{N}{\lambda}\int d^d x \Tr\big[\frac{1}{2}(\partial\Phi)^2 + V(\Phi)\big]$. So the propagator carries a factor $g_{YM}^2=\lambda/N$ and each interaction vertex a factor $1/g_{YM}^2=N/\lambda$. In 't~Hooft's double-line notation, a vacuum Feynman graph with $V$ vertices, $E$ edges (propagators), and $F$ closed index loops scales as
\begin{align}
(g_{YM}^2)^{E-V} N^F
&\eqstep{1} \lambda^{E-V} N^{V - E + F}
\ \eqstep{2}\ \lambda^{E-V} N^\chi
\ \eqstep{3}\ \lambda^{E-V} N^{2 - 2g} . \notag
\end{align}
**(1)** substitute $g_{YM}^2=\lambda/N$, so $(g_{YM}^2)^{E-V}=\lambda^{E-V}N^{-(E-V)}$.\quad
**(2)** $\chi\equiv V-E+F$ is the Euler characteristic of the surface on which the double-line graph can be
drawn.\quad
**(3)** for a closed orientable surface of genus $g$, $\chi=2-2g$.

The leading diagrams are planar, with the topology of a sphere ($g = 0$, $\chi = 2$). They contribute at order $N^2$.
2. **Scaling of connected correlators.**
Define the single-trace operators, with their vacuum value subtracted,

$$

\mathcal{O}_i(x) \equiv \Tr\big(\Phi^{k_i}(x)\big) - \Braket{\Tr\big(\Phi^{k_i}(x)\big)} .

$$

Now consider a connected correlator $\braket{\mathcal{O}_1(x_1) \cdots \mathcal{O}_n(x_n)}_{\text{conn}}$. Treat each operator insertion as an extra vertex of the graph, so the graph has $V_{\rm int}$ interaction vertices and $n$ insertions. An interaction vertex carries a factor $N/\lambda$ from the action. An insertion carries no such factor. Therefore
\begin{align}
\Big(\frac N\lambda\Big)^{V_{\rm int}}\Big(\frac\lambda N\Big)^{E}N^F
&\eqstep{4} \lambda^{E-V_{\rm int}}\,N^{(V_{\rm int}+n)-E+F}\,N^{-n} \notag\\
&\eqstep{5} \lambda^{E-V_{\rm int}}\,N^{\chi-n}
\ \eqstep{6}\ \lambda^{E-V_{\rm int}}\,N^{2-n} . \notag
\end{align}
**(4)** collect the powers of $N$, and add and subtract $n$ in the exponent.\quad
**(5)** counting the insertions as vertices, the Euler characteristic is $\chi=(V_{\rm int}+n)-E+F$.\quad
**(6)** a connected planar graph has $\chi=2$.

So

$$

\Braket{\mathcal{O}_1(x_1) \cdots \mathcal{O}_n(x_n)}_{\text{conn}} \sim N^{2-n} .

$$

In terms of canonically normalized fields $\varphi=\Phi/g_{YM}$, the same operators are
$\mathcal O_i=(\lambda/N)^{k_i/2}\Tr\varphi^{k_i}$ minus its mean. For $k_i=2$ this is $\lambda\,N^{-1}\Tr\varphi^2$, the normalization used in the worked example later in this chapter. The leading powers of $N$ are:



6. **Wick's theorem and Gaussian factorization.**
All connected correlators with $n \ge 3$ vanish as $N \to \infty$. By the cumulant expansion, every higher correlation function then splits into a sum of products of two-point functions:

$$

\lim_{N\to\infty} \Braket{\mathcal{O}_1(x_1) \cdots \mathcal{O}_{2m}(x_{2m})} = \sum_{\text{pairings } \pi} \prod_{(i, j) \in \pi} \Braket{\mathcal{O}_i(x_i)\mathcal{O}_j(x_j)} .

$$

Correlators with an odd number of operators vanish. A field with this property is called a **generalized free field** (GFF).
7. **Commutators become $c$-numbers.**
Now look at the commutator $[\mathcal{O}_A(x), \mathcal{O}_B(y)]$. Its expectation value is a number,

$$

c_{AB}(x, y) \equiv \Braket{[\mathcal{O}_A(x), \mathcal{O}_B(y)]} \sim O(1) .

$$

The quantum fluctuation of the commutator around this number is controlled by connected four-point functions:

$$

\begin{split}
\Big\| \big([\mathcal{O}_A(x), \mathcal{O}_B(y)] - c_{AB}(x, y)\id\big)\ket\Omega \Big\|^2
&\sim \Braket{\mathcal{O}_A\mathcal{O}_B\mathcal{O}_A\mathcal{O}_B}_{\text{conn}} \\
&\sim N^{2-4} = \frac{1}{N^2} \xrightarrow{N\to\infty} 0 .
\end{split}

$$

The fluctuations vanish as $N \to \infty$, so in the limit the commutator is a $c$-number:

$$

[\mathcal{O}_A(x), \, \mathcal{O}_B(y)] = c_{AB}(x, y)\,\id .

$$

8. **A bulk Fock space appears.**
A commutator that is a $c$-number is the canonical commutation relation (CCR) of a free quantum field. The GNS representation of this CCR algebra, built on the cyclic vector $\ket1_\Psi$, is a multi-particle Fock space:

$$

\HH_\Psi^{\text{GNS}} = \overline{\mathrm{span}\big\{\mathcal{O}_{i_1} \cdots \mathcal{O}_{i_k}\ket1_\Psi\big\}} \cong \HH_\Psi^{\text{Fock}} .

$$

The boundary single-trace operators act as creation and annihilation operators for the free bulk fluctuations $\delta\phi$. This is the content of \eqref{eq:ads-fock-gns}.

\end{keyresult}

It is then natural to identify the two vacua, $\ket0_{\phi_c}=\ket1_\Psi$. Here $\ket1_\Psi$ is the GNS vector
that corresponds to the identity operator. It is the same object that was called $\ket\Omega$ throughout
Chapter~2.

### Disjoint sectors: no single Hilbert space survives $N\to\infty$

This consequence is the large-$N$ version of the obstruction met in Chapter~1. Different semiclassical states
correspond to different classical bulk geometries. Their energies typically differ by an amount of order
$1/G_N$. This is an ordinary classical-gravity energy difference, and it diverges as $G_N\to0$. By contrast,
states *emph* a single $\HH_\Psi^{\text{GNS}}$ differ from $\Psi$ only by energies of order $G_N^0$,
which is the size of an ordinary quantum fluctuation and stays finite. So the GNS Hilbert spaces
$\HH_{\Psi_1}$ and $\HH_{\Psi_2}$, built around two different classical geometries, cannot overlap at any finite
order in perturbation theory in $G_N$.

There is a further, more subtle point. Two semiclassical states with the *emph* energy can still lie in
different GNS sectors. This happens if they are separated by an infinite entanglement barrier, exactly the
mechanism of Chapter~1.

**So in the large-$N$ limit there is no longer one single Hilbert space for the theory. The space of
states splits into disjoint sectors, one for each semiclassical background.** Each sector has its own GNS Hilbert
space and its own emergent operator algebra. This mirrors the $N\to\infty$ behavior of the entangled spin chain
with different angles $\theta$ in Chapter~2. There, different values of $\theta$ gave disjoint sectors. Here,
different classical geometries give disjoint sectors, for the same underlying reason.


> [!NOTE] **Physics Connection: this is an ordinary superselection rule**
> "Disjoint GNS sectors that no operator connects" already has a name in elementary quantum mechanics:
> **superselection**. You already know one example. No physical operator connects a state of one total
> electric charge to a state of a different total charge. So a superposition such as
> $\ket{\psi}=\alpha\ket{Q{=}0}+\beta\ket{Q{=}1}$ can never be distinguished from the corresponding mixture by any
> observable. The reason is that every physical operator $O$ must conserve charge, $[O,\hat Q]=0$.
> 
> This is exactly a block-diagonal condition. Check it on a toy two-level charge operator
> $\hat Q=\begin{psmallmatrix}0&0\\0&1\end{psmallmatrix}$. Write a general operator as $O=\begin{psmallmatrix}a&b\\c&d
> \end{psmallmatrix}$. Then
> 
$$

> [O,\hat Q] = \begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}0&0\\0&1\end{pmatrix}
> -\begin{pmatrix}0&0\\0&1\end{pmatrix}\begin{pmatrix}a&b\\c&d\end{pmatrix}
> = \begin{pmatrix}0&b\\-c&0\end{pmatrix} .
> 
$$

> Requiring this to vanish gives $b=c=0$. So $O$ must be block-diagonal in the charge sectors, and no
> charge-conserving operator can have a nonzero matrix element between them.
> 
> Different semiclassical vacua behave in the same way. The role of the conserved charge is played by an energy
> or entanglement difference that diverges as $N\to\infty$ (Chapter~1). It forces every operator that survives the
> large-$N$ limit to have vanishing matrix elements between sectors. The mechanism that produces the split is
> different: a conserved quantity in one case, an infinite barrier in the other. But the resulting structure is
> the same superselection structure you already know: disjoint sectors, no operator that crosses between them,
> and a separate Hilbert space for each sector.


### Why boundary time slices carry independent algebras

One more structural fact explains something that would otherwise look paradoxical. At finite $N$, the algebra
of operators on one Cauchy slice determines the algebra everywhere. This is the time-slice axiom of Chapter~4:
ordinary time evolution lets you reconstruct operators at any other time from data on one slice. In the strict
$N\to\infty$ limit this is no longer true. The boundary theory becomes a **generalized free field**. Such a
field is Gaussian and is specified completely by its two-point function. It has *emph* equation of motion
that governs its time evolution. As a result, algebras built on different Cauchy slices become inequivalent.

The reason lies in how the boundary Hamiltonian scales with $N$. The stress tensor has the schematic form
$T^{\mu\nu}=N\Tr(\cdots)$. It has an overall factor of $N$ relative to the normalized single-trace operators.
So the ordinary boundary Hamiltonian $H=\int d^{d-1}x\,T^{00}$ has no finite $N\to\infty$ limit in any sector:
it diverges. The *emph* versions $\widehat T^{\mu\nu}\equiv T^{\mu\nu}/N$ and $\widehat H\equiv H/N$ do
survive the limit. But they generate only an infinitesimally slow flow,
$i[\widehat H,O(x)]=\tfrac1N\partial_tO(x)$. A full time translation of single-trace operators needs the
unrescaled $H$, and that operator does not exist in the limit. **Ordinary time translation, generated by
the integral of a local density over one Cauchy slice, does not survive the large-$N$ limit.**

This does not contradict the fact that semiclassical states such as the vacuum clearly have time-translation
symmetry. Within a given sector there is a genuine time-translation operator $\hat h_\Psi$ satisfying
\begin{equation}
i[\hat h_\Psi,O(x)]=\partial_tO(x) .
\label{eq:ads-htrans}
\end{equation}
But $\hat h_\Psi$ cannot be written as the integral of a local operator over a single time slice, the way $H$
was. The next section, on the vacuum sector, makes this explicit and constructs $\hat h_\Omega$. The same thing
happens for any global symmetry, not only time translation. We return to it in the section on $1/N$
corrections, for an internal $U(1)$ charge.

## The vacuum sector

In the vacuum sector every part of the general story can be made explicit and checked. The reason is that here
both sides of the duality are known in closed form. The vacuum $\ket\Omega$ is dual to empty global AdS, with
bulk vacuum $\ket0_{\text{AdS}}\in\HH_{\text{AdS}}^{\text{Fock}}$. A bulk field has the ordinary mode expansion
\begin{equation}
\phi(X)=\sum_k\big(u_k(X)a_k+u_k^*(X)a_k^\dagger\big), \qquad a_k\ket0_{\text{AdS}}=0 ,
\label{eq:ads-bulkmodes}
\end{equation}
and $\HH_{\text{AdS}}^{\text{Fock}}$ is built by acting with creation operators $a_k^\dagger$ on the vacuum, just
as for any ordinary Fock space.

On the boundary, vacuum correlators of single-trace operators have the standard large-$N$ scaling:
$\braket{O}=0$, $\braket{O_1O_2}_c\sim O(N^0)$, and $\braket{O_1\cdots O_n}_c\sim N^{2-n}$. So at leading order
every higher correlator factorizes into a sum of products of two-point functions. This is exactly the Gaussian,
generalized-free-field structure that \eqref{eq:ads-fock-gns} requires. Each single-trace operator behaves like
a generalized free field, so $\HH_\Omega^{\text{GNS}}$ has the required Fock-space structure. In fact

$$

B(\HH_\Omega^{\text{GNS}})=(\pi_\Omega(\Sscr))'' .

$$

This means that $\omega_\Omega$ is a *emph* state with respect to $\Sscr$, and $\Sscr=\Alg_\Omega$. In the
vacuum sector, single-trace operators are all there is. Nothing extra survives the large-$N$ limit.

### Worked calculation: matrix Wick contractions and large-$N$ factorization

To see how large-$N$ factorization produces a free Fock algebra from a matrix theory, work out the index
contractions for an $N\times N$ hermitian matrix field $M_{ij}(x)$ with Gaussian propagator

$$

\braket{M_{ij}(x) M_{kl}(y)}_0 = \delta_{il}\delta_{jk} G(x,y) .

$$

Here $G(x,y)$ is a scalar two-point function. Define the gauge-invariant, normalized single-trace operator

$$

\mathcal{O}(x) \equiv \frac{1}{N} \Tr\big(M(x)^2\big) = \frac{1}{N} \sum_{i,j=1}^N M_{ij}(x) M_{ji}(x) ,

$$

understood as normal-ordered. This means contractions between the two $M$'s inside the same $\mathcal O$ are
left out. Equivalently, the vacuum value $\braket{\mathcal O}_0=N\,G(x,x)$ has been subtracted. The two-point
correlator is

$$

\braket{\mathcal{O}(x)\mathcal{O}(y)}_0 = \frac{1}{N^2}\sum_{i,j,k,l=1}^N \braket{M_{ij}(x) M_{ji}(x) M_{kl}(y) M_{lk}(y)}_0 .

$$

By Wick's theorem, there are two ways to contract each $M(x)$ with an $M(y)$:

1. Contract $M_{ij}(x)$ with $M_{kl}(y)$, and $M_{ji}(x)$ with $M_{lk}(y)$:
\begin{align}
\braket{M_{ij}(x)M_{kl}(y)}_0 \braket{M_{ji}(x)M_{lk}(y)}_0
&\eqstep{1} (\delta_{il}\delta_{jk} G(x,y))(\delta_{jk}\delta_{il} G(x,y))
\ \eqstep{2}\ \delta_{il}\delta_{jk} G(x,y)^2 . \notag
\end{align}
**(1)** the Gaussian propagator, applied to each contracted pair.\quad
**(2)** a Kronecker delta squared equals itself, $\delta_{il}\delta_{il}=\delta_{il}$.

Summing over all four indices gives

$$

\sum_{i,j,k,l} \delta_{il}\delta_{jk} = \sum_{i,j=1}^N 1 = N^2 .

$$

2. Contract $M_{ij}(x)$ with $M_{lk}(y)$, and $M_{ji}(x)$ with $M_{kl}(y)$:
\begin{align}
\braket{M_{ij}(x)M_{lk}(y)}_0 \braket{M_{ji}(x)M_{kl}(y)}_0
&\eqstep{3} (\delta_{ik}\delta_{jl} G(x,y))(\delta_{jl}\delta_{ik} G(x,y))
\ \eqstep{4}\ \delta_{ik}\delta_{jl} G(x,y)^2 . \notag
\end{align}
**(3)** the Gaussian propagator again, with the indices of the second contraction pattern.\quad
**(4)** a Kronecker delta squared equals itself.

Summing over the indices again gives $\sum_{i,j} 1 = N^2$.

Now multiply by the normalization $\frac{1}{N^2}$:

$$

\braket{\mathcal{O}(x)\mathcal{O}(y)}_0 = \frac{1}{N^2}\Big(N^2 G(x,y)^2 + N^2 G(x,y)^2\Big) = 2\,G(x,y)^2 \sim O(N^0) .

$$


Next consider the four-point function
$\braket{\mathcal{O}(x_1)\mathcal{O}(x_2)\mathcal{O}(x_3)\mathcal{O}(x_4)}_0$. Its contractions fall into two
classes.

- **Disconnected contractions.** These contract the single traces in pairs, for example
$\mathcal{O}_1$ with $\mathcal{O}_2$ and $\mathcal{O}_3$ with $\mathcal{O}_4$:

$$

\braket{\mathcal{O}(x_1)\mathcal{O}(x_2)}_0 \braket{\mathcal{O}(x_3)\mathcal{O}(x_4)}_0 = \big(2 G(x_1,x_2)^2\big)\big(2 G(x_3,x_4)^2\big) \sim O(N^0) .

$$

There are three such pairings: $(12)(34)$, $(13)(24)$, and $(14)(23)$.
- **Connected contractions.** These link all four operators in a single ring, for example
$M(x_1) \to M(x_2) \to M(x_3) \to M(x_4) \to M(x_1)$. In double-line notation the ring has two closed index
loops, one running around its inside and one around its outside. That gives two free index sums and a factor
$N^2$. With four normalization factors of $1/N$, the connected four-point function scales as

$$

\braket{\mathcal{O}(x_1)\mathcal{O}(x_2)\mathcal{O}(x_3)\mathcal{O}(x_4)}_c \sim \frac{1}{N^4} \times N^2 = \frac{1}{N^2} \to 0 .

$$

This agrees with the general planar scaling $\braket{\mathcal{O}_1\cdots\mathcal{O}_n}_c \sim N^{2-n}$ at
$n=4$. The same scaling holds when planar gauge interactions are switched on, at fixed 't~Hooft coupling
$\lambda = g_{\text{YM}}^2 N$.

As a check at coincident points, with $G=1$: here $\Tr M^2$ is a sum of independent squared Gaussian entries,
and adding up their cumulants gives exactly $\braket{\mathcal O^2}_0=2$ and a fourth cumulant $48/N^2$. A Monte
Carlo sample of random Hermitian matrices reproduces the variance $2$.

So at strictly $N\to\infty$,

$$

\begin{split}
\braket{\mathcal{O}(x_1)\mathcal{O}(x_2)\mathcal{O}(x_3)\mathcal{O}(x_4)}_0
={}& \braket{\mathcal{O}_1\mathcal{O}_2}_0\braket{\mathcal{O}_3\mathcal{O}_4}_0
+ \braket{\mathcal{O}_1\mathcal{O}_3}_0\braket{\mathcal{O}_2\mathcal{O}_4}_0 \\
&+ \braket{\mathcal{O}_1\mathcal{O}_4}_0\braket{\mathcal{O}_2\mathcal{O}_3}_0 + O(1/N^2) .
\end{split}

$$

Connected $n$-point correlators vanish for all $n \ge 3$. So the single-trace operators obey Wick's theorem
exactly in the limit, and they generate a generalized-free-field Fock space $\HH_\Omega^{\text{GNS}}$.

The match between bulk and boundary mode expansions can be made explicit. Expand a single-trace operator
directly on the GNS Hilbert space:

$$

\pi_\Omega(O(x))=\sum_k\big(v_k(x)b_k+v_k^*(x)b_k^\dagger\big), \qquad b_k\ket1_\Omega=0 .

$$

Match the boundary mode functions to the boundary limits of the bulk ones:

$$

v_k(x)=\lim_{r\to\infty}r^\Delta u_k(X) .

$$

The extrapolate dictionary \eqref{eq:ads-extrapolate} then forces the mode operators to be the same,
$a_k=b_k$. This establishes \eqref{eq:ads-fock-gns} explicitly in this one solvable case. Written in position
space, the identification becomes
\begin{equation}
\phi(X) = \int d^dx\,K(X;x)\,\pi_\Omega(O(x)) .
\label{eq:ads-hkll}
\end{equation}
This is the **global HKLL construction**, named after Hamilton, Kabat, Lifschytz and Lowe. The kernel $K$ is
explicit, and it reconstructs the bulk field everywhere in AdS from boundary single-trace operators.

### Worked derivation: the HKLL smearing kernel in \texorpdfstring{$\text{AdS}_3$}{AdS3}

To make the HKLL kernel $K(X;x)$ concrete, consider a free massless scalar field $\phi(z,t,x)$ in Poincaré
$\text{AdS}_3$ with metric

$$

ds^2 = \frac{R^2}{z^2}\big(dz^2 - dt^2 + dx^2\big), \qquad z > 0 .

$$

The boundary is at $z=0$. For $m^2=0$ the conformal dimension is $\Delta = 2$. The bulk Klein—Gordon equation
$(\Box - m^2)\phi = 0$, multiplied through by $R^2/z^2$, reads

$$

z\, \partial_z \left(\frac{1}{z}\partial_z \phi\right) - \partial_t^2 \phi + \partial_x^2 \phi
= \partial_z^2 \phi - \frac{1}{z}\partial_z \phi - \partial_t^2 \phi + \partial_x^2 \phi = 0 .

$$

The second form follows from the product rule applied to $\partial_z(z^{-1}\partial_z\phi)$.

Go to Fourier space, with boundary momentum $(\omega, k)$ chosen timelike, $\omega^2 - k^2 \equiv q^2 > 0$. For
$\phi(z,t,x) = f(z) e^{-i\omega t + ikx}$ the mode equation is

$$

f''(z) - \frac{1}{z} f'(z) + q^2 f(z) = 0 .

$$

Setting $f(z) = z\, g(z)$ turns this into Bessel's equation of order 1 for $g(z)$. The solution that is regular
in the interior is $J_1$:

$$

g''(z) + \frac{1}{z} g'(z) + \left(q^2 - \frac{1}{z^2}\right)g(z) = 0 \implies f(z) = C\, z J_1(q z) .

$$

Near the boundary, $z \to 0$, we have $J_1(qz) \approx \frac{qz}{2}$, so $f(z) \approx C \frac{q}{2} z^2$. The
extrapolate dictionary (in Poincaré coordinates, $z^{-\Delta}$ plays the role of $r^{\Delta}$) requires
$\lim_{z\to 0} z^{-2} \phi(z,t,x) = \mathcal{O}(t,x) = e^{-i\omega t + ikx}$. This fixes $C = \frac{2}{q}$. Hence

$$

\phi(z,t,x) = \frac{2 z}{q} J_1(q z)\, \mathcal{O}(t,x) .

$$


Now go back to position space. The result is a smearing of $\mathcal O$ over a disk of radius $z$, with one of
the boundary coordinates continued to imaginary values:
\begin{equation*}
\phi(z,t,x) = \frac{1}{\pi} \int_{t'^2 + y'^2 < z^2} dt'\, dy' \, \mathcal{O}\big(t + t',\, x + i y'\big) .
\end{equation*}
To check it, insert $\mathcal O(t,x)=e^{-i\omega t+ikx}$:
\begin{align}
&\frac{1}{\pi} \int_{t'^2 + y'^2 < z^2} dt'\,dy'\, e^{-i\omega(t+t')+ik(x+iy')} \notag\\
&\qquad\eqstep{1} \frac{e^{-i\omega t+ikx}}{\pi}\int_{t'^2 + y'^2 < z^2} dt'\,dy'\,e^{-i\omega t'-ky'} \notag\\
&\qquad\eqstep{2} \frac{e^{-i\omega t+ikx}}{\pi}\cdot\frac{2\pi z\,J_1(qz)}{q}
\ \eqstep{3}\ \frac{2z}{q}J_1(qz)\,\mathcal O(t,x) . \notag
\end{align}
**(1)** pull the factor that does not depend on $t',y'$ out of the integral.\quad
**(2)** the disk integral $\int_{|u|<z}d^2u\,e^{ia\cdot u}=2\pi z J_1(|a|z)/|a|$, continued to
$a=(-\omega,ik)$, for which $a\cdot a=\omega^2-k^2=q^2$.\quad
**(3)** $e^{-i\omega t+ikx}=\mathcal O(t,x)$.

We also checked step (2) numerically for sample values of $z,\omega,k$. The contour can be rotated back to
real boundary coordinates. The smearing region then becomes the set of boundary points spacelike-separated from
the bulk point, which is not compact, and the real-space kernel needs more care; we do not need its explicit
form.

The disk formula has a clear physical meaning. To evaluate the local bulk operator $\phi(z,t,x)$ at radial
depth $z$, one must integrate the boundary operator $\mathcal{O}$ over a region of size $z$. The deeper the
operator sits in the bulk (the larger $z$), the larger the boundary region needed to reconstruct it. This is a
direct example of the holographic UV/IR relation.

A further fact follows from the representation theory of the boundary conformal group. In global AdS the
single-particle energy levels are evenly spaced: in units of $1/R$ they are $\Delta+2n+l$, so successive radial
excitations are spaced by $2$. From this one can show the following result, which we state without proof:
\begin{equation}
B(\HH_\Omega^{\text{GNS}}) = Y_{I_w}, \qquad w\ge\pi R .
\label{eq:ads-timeband}
\end{equation}
Here $I_w$ is a boundary time band of width $w$. **The entire operator content of the bulk vacuum
sector, meaning every bulk field everywhere in AdS, is already generated by boundary operators smeared over a
time band of width $\pi R$.** You do not need the whole boundary history, or an infinite band. A band of width
$\pi R$ is already enough to reconstruct the entire bulk. This width is half of $2\pi R$, the time after which
every single-particle mode returns to itself up to an overall phase. This
is the clearest and most concrete preview of subregion-subalgebra duality, which Chapter~7 develops as a
general principle.

Finally, the vacuum-sector time-translation operator $\hat h_\Omega$ from the previous section can be written
down explicitly. It is the bulk energy integral over a Cauchy slice, schematically

$$

\hat h_\Omega=\int d\rho\,d^{d-1}\Omega\,\rho^{d-1} T_{tt} ,

$$

with the appropriate metric factors. Here $T_{tt}$ is the bulk stress tensor, which is quadratic in $\phi$ at
this order. Substitute the mode expansion \eqref{eq:ads-bulkmodes} and use $a_k=b_k$. This turns $\hat h_\Omega$
into a specific quadratic expression in boundary single-trace operators, which is an operator satisfying
\eqref{eq:ads-htrans}. Consistent with \eqref{eq:ads-timeband}, this expression involves integrating boundary
operators over a time band of width $\pi R$, not a single instant.

## The thermofield double state

### Setup, and the Hawking—Page transition

Take two copies of the boundary CFT, $\text{CFT}_R$ and $\text{CFT}_L$. At finite $N$, build the
**thermofield double** (TFD) state
\begin{equation}
\ket{\Psi_\beta} = \frac{1}{\sqrt{Z_\beta}}\sum_n e^{-\beta E_n/2}\ket n_R\ket{\Theta n}_L, \qquad
Z_\beta=\sum_n e^{-\beta E_n} .
\label{eq:ads-tfd}
\end{equation}
Here $\Theta$ is the CRT operator (charge conjugation, reflection, and time reversal). It is needed to match
energy eigenstates correctly across the two copies. Tracing out $L$ gives the ordinary thermal density matrix
$\rho_\beta=\tfrac1{Z_\beta}e^{-\beta H_R}$ on $R$.

This is the finite-dimensional worked example of Chapter~4, now applied to a field theory. The algebra
$B(\HH_R)$ is type I, $\ket{\Psi_\beta}$ is cyclic and separating for it, and the modular operator is
\begin{equation}
-\log\Delta_\beta=\beta(H_R-H_L) .
\label{eq:ads-tfd-modular}
\end{equation}
This is the formula $\Delta_\Psi=\rho_R\otimes\rho_L^{-1}$ from Chapter~4, with $\rho_R=e^{-\beta H_R}/Z_\beta$
and $\rho_L=e^{-\beta H_L}/Z_\beta$. The factors of $Z_\beta$ cancel in the logarithm.

In the large-$N$ limit this system has a first-order phase transition at the **Hawking—Page
temperature** $T_{\text{HP}}$. The free energy jumps in its scaling with $N$: it is of order $N^0$ below
$T_{\text{HP}}$ and of order $N^2$ above it. The dual bulk geometry jumps at the same point. Below
$T_{\text{HP}}$ it is *emph*, a thermal gas of particles in ordinary global AdS with no black hole.
Above $T_{\text{HP}}$ it is an *emph*.

**Below $T_{\text{HP**}$.} The energies that contribute to the sum in \eqref{eq:ads-tfd} stay of order
$N^0$, because higher energies are suppressed by the Boltzmann factor. So in the large-$N$ limit these states lie
inside the vacuum-sector GNS Hilbert spaces $\HH_\Omega^R$ and $\HH_\Omega^L$ built in the previous section. The
GNS Hilbert space built from $\ket{\Psi_\beta}$ factorizes, $\HH_{\Psi_\beta}^{\text{GNS}}=
\HH_\Omega^R\otimes\HH_\Omega^L$. Correspondingly $Y_R=B(\HH_\Omega^R)$ and $Y_L=B(\HH_\Omega^L)$. **So
$Y_R$ remains type I.** The bulk dual is two separate copies of global AdS, with no geometric connection between
them. The only link between them is the entanglement carried by the TFD state. The bulk geometry is
disconnected.

**Above $T_{\text{HP**}$.} Now the thermal ensemble is dominated by states of energy of order $N^2$. The
finite-$N$ sum \eqref{eq:ads-tfd} has no sensible limit as $N\to\infty$: neither the energies nor the
eigenstates converge. In fact the one-point function of a single-trace operator in this state *emph*,
$\braket{\Psi_\beta|O|\Psi_\beta}\sim O(N)$. The fix is to use "renormalized," mean-subtracted operators
$\widehat O\equiv O-\braket{\Psi_\beta|O|\Psi_\beta}$. Their connected correlators have sensible large-$N$
limits of order $N^0$, and they again obey large-$N$ factorization. This produces a good GNS Hilbert space with
a Fock-space structure. The resulting algebras $Y_R\equiv(\pi_{\Psi_\beta}(\Sscr_\beta^{(R)}))''$ satisfy
$Y_R'=Y_L$.

But now the entanglement between $\text{CFT}_R$ and $\text{CFT}_L$ has jumped to order $N^2$. Because of this,
it has been argued that **$Y_R$ becomes type $\mathrm{III**_1$}, and $\HH_{\Psi_\beta}^{\text{GNS}}$ no
longer factorizes into separate $R$ and $L$ pieces. On the gravity side this matches the eternal black-hole
geometry (Fig.~\ref{fig:penrose}). The algebras $Y_R,Y_L$ are identified with the bulk exterior algebras
$\widetilde\M_R,\widetilde\M_L$. These are type $\mathrm{III}_1$ for a simple reason: they are algebras of
subregions in an ordinary continuum quantum field theory, which is the local-algebra story of Chapter~4.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.72\textwidth]{figs/fig_penrose.pdf}
\caption{Penrose diagram of the two-sided eternal AdS black hole, dual to the thermofield double state $\ket{\Psi_\beta}$. The exterior regions $R$ (blue) and $L$ (gold) end on the AdS boundaries where $\mathrm{CFT}_R$ and $\mathrm{CFT}_L$ live, and are cut off from the interior regions $F$ and $P$ by the event horizons (dashed red), which cross at the bifurcation point (black dot). The wavy lines are the future and past singularities, and the gray horizontal line is the $t=0$ slice, which runs from one boundary to the other through the Einstein—Rosen bridge.}
\label{fig:penrose}
\end{figure}

### Two puzzles, and how algebra resolves the first of them

The $T>T_{\text{HP}}$ phase is identified with an eternal black hole, and this identification passes every
quantitative check. Even so, before the algebraic reformulation it carried two conceptual puzzles. Both are
long-standing and well known in holography.

**The factorization puzzle.** The boundary theory clearly factorizes as $\text{CFT}_R\otimes
\text{CFT}_L$. It is just two separate, non-interacting copies of the same CFT. But the bulk black hole is a
single, *emph* spacetime. There are bulk operators, such as a Wilson line stretching from the left
boundary through the interior to the right boundary (Fig.~\ref{fig:penrose}), that do not seem to split into an
operator in $B(\HH_R)$ times an operator in $B(\HH_L)$. How can a connected bulk object correspond to anything
in a boundary tensor product that is clearly disconnected?

**The meeting-behind-the-horizon puzzle.** There is no interaction at all between $\text{CFT}_R$ and
$\text{CFT}_L$: the total Hamiltonian is simply $H_R+H_L$, with no cross term. Yet bulk degrees of freedom that
start separately in the $R$ and $L$ exterior regions can cross the horizon and interact with each other in the
interior. How can two boundary theories that are disconnected, both causally and dynamically, produce bulk
physics that is connected once you look behind the horizon?

The algebraic picture resolves the *emph* puzzle directly. Once $N\to\infty$ is taken seriously,
"$B(\HH_R)$" is the wrong object to compare with the bulk exterior algebra. The actual large-$N$ limit of the
algebra is $Y_R$. It is type $\mathrm{III}_1$, not type I, precisely because of the order-$N^2$ entanglement
between $R$ and $L$. For a type $\mathrm{III}_1$ algebra and its commutant, there is no tensor product structure
$Y_R\otimes Y_L$ inside $B(\HH^{\text{GNS}})$ of the kind an ordinary tensor product would give. So nothing
prevents the presence of operators (such as the boundary counterpart of that Wilson line) that are not products
of an $R$-piece and an $L$-piece. The apparent contradiction came from using type I tensor-product intuition in
a regime where the algebra has already become type $\mathrm{III}_1$.

The second puzzle, meeting behind the horizon, needs more tools. It needs the emergent commutant and the
half-sided modular inclusion structure of Chapter~4. It is taken up in Chapter~8, where the bulk causal
structure of the eternal black hole is built directly from boundary algebra data.

Three further remarks prepare the ground for algebraic ER$=$EPR in Chapter~8.

First, the whole qualitative conclusion here (disconnected bulk geometry below $T_{\text{HP}}$, connected black
hole above it) could in principle have been *emph* just from watching $Y_R$ jump from type I to type
$\mathrm{III}_1$. No independent knowledge of the bulk geometry is needed.

Second, for $T>T_{\text{HP}}$ different temperatures $\beta$ lie in different, non-overlapping GNS sectors.
Their entanglement entropies differ by an amount of order $N^2$, which is an infinite barrier in the strict
limit (the mechanism of Chapter~1 again). Below $T_{\text{HP}}$, by contrast, every $\beta$ shares one common GNS
Hilbert space, and the different TFD states are just different vectors inside it.

Third, the ordinary Hamiltonians $H_R,H_L$ do not survive the large-$N$ limit as elements of the algebra. So
\eqref{eq:ads-tfd-modular} stops holding literally. But the modular operator $\Delta_\beta$ itself *emph*
survive, and it still generates boundary time translation in opposite directions on the two sides. Below
$T_{\text{HP}}$ it splits into an $R$ part and an $L$ part, $-\log\Delta_\beta=\beta(\hat h_R-\hat h_L)$, where
$\hat h$ is the vacuum-sector time-translation operator of the previous section. Above $T_{\text{HP}}$ it does
not split at all. This tracks the transition from type I to type $\mathrm{III}_1$ exactly.

## General black holes

The thermofield double is special. It has an exact bifurcate horizon: the future and past horizons meet at a
single surface in a perfectly symmetric way. A more generic two-sided semiclassical state $\ket\Psi$ is dual to
a "long" black hole. Such a black hole has a genuine interior region $I$ that separates $R$ and $L$, and its
horizons do not meet at a single bifurcation surface.

This case shows the subtlety noted at the start of this chapter: the inclusion $\Sscr\subseteq\Alg_\Psi$ can
now be *emph*. The renormalized single-trace algebras still reproduce the bulk exterior algebras,
$Y_R=\widetilde\M_R$ and $Y_L=\widetilde\M_L$. But $R$ and $L$ together no longer cover a full Cauchy slice. The
interior region $I$ is missing. Bulk operators in $I$ must still correspond to *emph* boundary operators
that survive the large-$N$ limit, since they belong to the same physical bulk field as the exterior operators,
only evaluated at a different place. But they are not single-trace operators. They must belong to
$\Alg_\Psi\setminus\Sscr$.

Chapter~7 identifies exactly what these extra operators are. They are generated from single-trace operators by
*emph*. This mechanism was previewed by the ergodic lemma of Chapter~4: a modular flow, run long
enough, generates a whole larger algebra starting from a smaller subalgebra.

The same phenomenon (extra, non-single-trace operators needed for a black-hole interior) also occurs for a
"long" one-sided black hole. A one-sided black hole formed by ordinary gravitational collapse, with matter
falling in from empty space, is different. This contrast matters in Chapter~7. There, $\Alg_\Psi=\Sscr$
exactly: single-trace operators are already everything, and nothing extra is needed.

## A diagnostic of firewalls in generic highly excited states

Now consider a completely generic, highly excited state $\ket\Psi$ with energy $E_\Psi\sim O(N^2)$. We do not
assume that it was prepared to have a nice bulk dual. It is just an arbitrary state of that energy. The
boundary theory at such energies is expected to be chaotic. A typical state of that energy should then look
thermal to any probe made of single-trace operators, to leading order in $1/N$:
\begin{equation}
\braket{\Psi|O|\Psi}\approx\braket{O}_\beta, \qquad \braket{\Psi|O_1\cdots O_n|\Psi}\approx\braket{O_1\cdots
O_n}_\beta ,
\label{eq:ads-thermal}
\end{equation}
with $\beta$ fixed by matching the energy, $E_\Psi=E_\beta$. This is the familiar statement, in the spirit of
the eigenstate thermalization hypothesis, that a single generic high-energy state reproduces thermal
correlators. It says that, as far as single-trace operators can tell, $\Psi$ has a smooth black-hole exterior.
But does it also have a smooth *emph*, a genuine continuation of the geometry behind the horizon? Or
does the interior simply fail to exist? The second possibility is called a **firewall**.

The previous section already gave the criterion needed to answer this. A smooth interior requires operators
that survive the large-$N$ limit *emph* single-trace operators, that is, $\Sscr\subsetneq\Alg_\Psi$. This
gives a clean, checkable diagnostic. **Suppose a generic highly excited state satisfies the thermal
condition \eqref{eq:ads-thermal** and *emph* has $\Alg_\Psi=\Sscr$, so that no operators beyond single-trace
ones survive the limit. Then its bulk dual has a firewall.} In this case $\omega_\Psi$ is a *emph* state on
$\Alg_\Psi$. This violates the purity condition \eqref{eq:ads-irreducible} assumed earlier for the "nice"
semiclassical case.

For two-sided generic states there is an analogous statement with one more condition. The correlations between
the two sides must vanish, $\braket{\Psi|O_RO_L|\Psi}_c\to0$ as $N\to\infty$. This is consistent with there
being no smooth, connected bridge between the two boundaries in that case.

## Perturbative $1/N$ corrections

### Corrections to bulk reconstruction

Everything so far worked at strictly leading order in $G_N$, or equivalently in $1/N$. Including subleading
orders makes the bulk field theory interacting: the terms $\kappa S_3+\kappa^2S_4+\cdots$ in the bulk action
switch back on. Correspondingly, the boundary theory develops nonzero connected three-point and higher
functions, suppressed by powers of $1/N$.

One direct consequence is that the HKLL formula \eqref{eq:ads-hkll}, exact at leading order, gets corrected.
Take the simplest case of a cubic self-interaction $\phi^3$ and solve the interacting bulk equation of motion
perturbatively in $\kappa$. (We do not reproduce this computation.) The result is a series of extra terms in the
bulk-to-boundary map:

$$

\begin{split}
\phi(X) ={}& \int d^dx\,K(X;x)\,O^{(0)}(x) \\
&+ \kappa\int d^dx_1\,d^dx_2\,K(X;x_1,x_2)\,O^{(0)}(x_1)O^{(0)}(x_2) + \cdots
\end{split}

$$

The leading-order reconstruction picks up multi-trace corrections, with one extra factor of a single-trace
operator for each order in $1/N$. These corrections underlie the topic of ``$1/N$ corrections to bulk
locality,'' a substantial research area of its own. We do not need to track every term here.

The structural point that matters for everything downstream is this. To any finite order in the $1/N$
expansion, the *emph* of each algebra discussed above is expected to stay the same as at leading order.
The heuristic reason is that the spectrum of the modular operator is controlled by its zeroth-order piece. On
this picture, perturbation theory in $1/N$ does not change an algebra's type; only the strict $N\to\infty$ limit
can do that.

### Conserved charges, and where gravitational dressing first appears

The second new feature matters more conceptually, for everything from Chapter~9 onward. Suppose the boundary
CFT has a global $U(1)$ symmetry. Its conserved charge must be rescaled, $\widehat Q\equiv Q/N$, in exactly the
way $\widehat H=H/N$ was, because the current itself scales as $N\Tr(\cdots)$. For a single-trace operator of
unit charge, with the convention $[Q,O(x)]=O(x)$,
\begin{equation}
[\widehat Q,O(x)]=\tfrac1N O(x) .
\label{eq:ads-charge}
\end{equation}
So the action of the rescaled charge is suppressed by $1/N$, exactly as in the time-translation story earlier
in this chapter. Within a given sector there is again a genuine large-$N$ operator $\hat q$ that generates the
full rotation, $[\hat q,O(x)]=O(x)$. Like $\hat h_\Omega$ before it, $\hat q$ cannot be written as the integral of
a local density over a single time slice.

The bulk dual of this boundary global $U(1)$ symmetry is a bulk $U(1)$ *emph* symmetry. Here something new
and physically important appears once $1/N$ corrections are included. Translate the suppressed commutator
\eqref{eq:ads-charge} to the bulk with the extrapolate dictionary. It forces the bulk gauge field strength and a
charged bulk scalar to have a *emph*. This is an explicit violation of
naive bulk microcausality, order by order in $1/N$.

The violation comes directly from the bulk Gauss-law constraint. The equation of motion
$\nabla_MF^{MN}=\kappa J^N$ ties the electric field on a Cauchy slice to the charges on that same slice, because
Gauss's law is intrinsically nonlocal. The resolution comes back as the central mechanism of Chapter~9. A bulk
charged field $\phi(z,x)$ is not gauge invariant on its own. To build a gauge-invariant operator, one attaches a
**Wilson line** that runs from the boundary to the point:
\begin{equation}
\Phi(z,x) = e^{-i\kappa V}\phi(z,x), \qquad V=\int_0^z dz'\,A_z(z',x) .
\label{eq:ads-dressed}
\end{equation}
This is a **dressed observable**. The Wilson line is nonlocal: it depends on the gauge field along a whole
path, not just at one point. This nonlocality produces the nonlocal commutation relations directly, and nothing
mysterious is left over.

### Worked calculation: Gauss's law and the dressed operator commutator

To see this mechanism explicitly in canonical quantization, consider the bulk gauge field
$A_M = (A_t, A_z, A_x)$ on a constant-time Cauchy slice, in the gauge $A_t = 0$. We suppress the factors of the
AdS metric; they do not affect the structure of the argument. The momentum conjugate to $A_z(z,x)$ is the
electric field $E^z(z,x) = F^{zt}(z,x) = \partial_t A_z - \partial_z A_t$. The canonical commutation relation is

$$

\big[A_z(z',x'),\, F^{zt}(z'',x'')\big] = i\,\delta(z'-z'')\,\delta(x'-x'') .

$$

The field $F^{xt}$ is conjugate to $A_x$, so it commutes with $A_z$.

In the quantum theory, Gauss's law is a constraint on physical operators. Define the Gauss operator

$$

G(z'',x'') \equiv \partial_{z''} F^{zt}(z'',x'') + \partial_{x''} F^{xt}(z'',x'') - \kappa\, J^t(z'',x'') .

$$

A physical, gauge-invariant operator must commute with $G$ at every point. Take $\phi(z,x)$ to create one unit
of charge at $(z,x)$, so that $[J^t(z'',x''),\phi(z,x)]=\delta(z''-z)\,\delta(x''-x)\,\phi(z,x)$.

The naive, undressed field fails this test. It commutes with the gauge field, $[\phi(z,x), F^{Mt}] = 0$, so only
the charge term contributes:
$[G(z'',x''),\phi(z,x)]=-\kappa\,\delta(z''-z)\,\delta(x''-x)\,\phi(z,x)\ne0$. So $\phi$ is not gauge invariant.

Now compute with the dressed operator $\Phi(z,x) = e^{-i\kappa V(z,x)}\phi(z,x)$, where
$V(z,x) = \int_0^z dz' A_z(z',x)$. First, the commutator with the electric field:
\begin{align}
\big[\Phi(z,x),\, F^{zt}(z'',x'')\big]
&\eqstep{1} \Big[e^{-i\kappa \int_0^z dz' A_z(z',x)},\, F^{zt}(z'',x'')\Big]\,\phi(z,x) \notag\\
&\eqstep{2} -i\kappa \left(\int_0^z dz' \big[A_z(z',x),\, F^{zt}(z'',x'')\big]\right) \Phi(z,x) \notag\\
&\eqstep{3} -i\kappa \left(\int_0^z dz' \, i\,\delta(z'-z'')\,\delta(x-x'')\right) \Phi(z,x) \notag\\
&\eqstep{4} \kappa\,\theta(z - z'')\,\delta(x - x'')\,\Phi(z,x) . \notag
\end{align}
**(1)** move $\phi(z,x)$ out of the commutator. It commutes with $F^{zt}$, so only the Wilson-line factor
has to be commuted.\quad
**(2)** $[V,F^{zt}]$ is a $c$-number, so $[e^{-i\kappa V},F^{zt}]=-i\kappa[V,F^{zt}]\,e^{-i\kappa V}$
exactly. Then recombine $e^{-i\kappa V}\phi=\Phi$.\quad
**(3)** substitute the canonical commutator $[A_z(z',x),F^{zt}(z'',x'')]=i\delta(z'-z'')\delta(x-x'')$.\quad
**(4)** $(-i)(i)=1$. The $\delta(z'-z'')$ collapses the $z'$ integral. The result is $1$ if $0<z''<z$ and $0$
if $z''>z$, which is the step function $\theta(z-z'')$.

Next, differentiate with respect to $z''$:
\begin{align}
\partial_{z''} \big[\Phi(z,x),\, F^{zt}(z'',x'')\big]
&\eqstep{5} \kappa\, \frac{d}{dz''}\theta(z - z'')\;\delta(x - x'')\,\Phi(z,x) \notag\\
&\eqstep{6} -\kappa\,\delta(z'' - z)\,\delta(x'' - x)\,\Phi(z,x) . \notag
\end{align}
**(5)** differentiate the result of step (4). Only the step function depends on $z''$.\quad
**(6)** $\frac{d}{dz''}\theta(z-z'')=-\delta(z''-z)$, the derivative of a step function.

Finally, assemble the Gauss operator:
\begin{align}
[G(z'',x''),\Phi(z,x)]
&\eqstep{7} -\partial_{z''}\big[\Phi(z,x),F^{zt}(z'',x'')\big] - \kappa\big[J^t(z'',x''),\Phi(z,x)\big] \notag\\
&\eqstep{8} \kappa\,\delta(z''-z)\,\delta(x''-x)\,\Phi(z,x) \notag\\
&\qquad - \kappa\,\delta(z''-z)\,\delta(x''-x)\,\Phi(z,x) \ =\ 0 . \notag
\end{align}
**(7)** $[\partial F,\Phi]=-\partial[\Phi,F]$. The $F^{xt}$ term drops out because $\Phi$ contains only
$A_z$ and $\phi$, both of which commute with $F^{xt}$.\quad
**(8)** use step (6) for the first term. For the second, $J^t$ commutes with the gauge field, so
$[J^t,\Phi]=e^{-i\kappa V}[J^t,\phi]=\delta\,\Phi$.

So Gauss's law holds identically as an operator statement for the dressed field. The price is visible in step
(4). For every point $z''<z$ along the string that runs from the boundary to the insertion point, the
commutator with the electric field is nonzero, even though that point is spacelike-separated from $(z,x)$. The
nonlocal string of the Wilson line is the physical cost of gauge invariance.

The same story holds for spacetime symmetries in place of an internal $U(1)$. To make a bulk operator
diffeomorphism-invariant, one must dress it to the boundary with a *emph* Wilson line.
Equivalently, one can work in a specific gauge and solve the constraint directly, as in the Gauss-law
calculation above. This dressing produces an analogous $1/N$ correction to the rescaled Hamiltonian,
$\widehat H=\widehat H^{(0)}+\tfrac1N\hat h_\Omega+\cdots$. **This is the first appearance, in perturbation
theory, of the mechanism that Chapter~9 turns into an exact, nonperturbative construction.** Dressing an operator
gravitationally to a physical reference is what makes it a genuine, gauge-invariant, physical observable. Here
the reference is a Wilson line; in Chapter~9 it is an observer's own clock, through the crossed product of
Chapter~5. The dressing is not optional decoration. It is forced by the bulk Gauss-law constraint that any
theory with gravity or gauge fields must satisfy.

\bigskip
\noindent The large-$N$ algebraic structure of AdS/CFT is now in place: semiclassical states as GNS sectors,
single-trace algebras $Y_O$, a change of algebra type that tracks the Hawking—Page transition, and
gravitational dressing already visible in perturbation theory. Chapter~7 assembles all of this into the central
physical claim of these notes, **subregion-subalgebra duality**. This is the statement that a bulk causal
region is identical, not merely related, to a specific emergent boundary operator subalgebra.



---

# Subregion-subalgebra duality

Chapters 2—6 built the tools for the idea of this chapter. The claim is simple to state, and its
consequences are large: **in the strict large-$N$ limit, an arbitrary bulk spacetime region is not
merely *emph* one.} This is not an approximation,
and there is no correction term to add at this order. The algebra of the bulk region and the boundary
algebra are the same mathematical object, described in two different languages.

## General formulation

### Where the identification comes from

Chapter 6 identified two Hilbert spaces. The first is the bulk Fock space. It is built by ordinary
quantization of small fluctuations around a classical background. The second is the boundary GNS Hilbert
space. It is built, through the GNS construction, from the algebra of boundary operators that survive the
large-$N$ limit. Since these are the same Hilbert space, the algebras of all bounded operators on them are
also the same:
\begin{equation}
B(\HH_\Psi^{\text{Fock}}) = B(\HH_\Psi^{\text{GNS}}) .
\label{eq:full_algebra_identity}
\end{equation}
This equation hides a small surprise. $B(\HH_\Psi^{\text{Fock}})$ is naturally built from data on a single
bulk Cauchy slice, because canonical quantization only needs one moment of time. $B(\HH_\Psi^{\text{GNS}})$
is built from operators on the entire boundary spacetime, or, by the time-band result of Chapter 6, at least
on a finite time band. These look like objects of different sizes. They are reconciled by the fact that the
bulk has one more spatial dimension than the boundary. The data of this extra dimension, spread over one
bulk Cauchy slice, is matched by a stretch of boundary *emph*, not boundary space. This is a first hint
of a general phenomenon that Chapter 8 develops in full: boundary time and bulk radial position are closely
linked.

At the free (quadratic) level, different bulk fields do not interact. So both the Hilbert space and its
operator algebra split into independent tensor factors, one for each field species $i$:
$\HH_\Psi^{\text{GNS}}=\bigotimes_i\HH_{\Psi,i}^{\text{GNS}}$, with $\HH_{\Psi,i}^{\text{Fock}}=
\HH_{\Psi,i}^{\text{GNS}}$ for each field separately. Nothing conceptually new happens here. It is
bookkeeping: the identification holds field by field, not just for the whole theory at once.

### The duality, stated precisely

Equation \eqref{eq:full_algebra_identity} is an identity between entire operator algebras. So it must also
hold subalgebra by subalgebra. Take any open bulk subregion $b$ of a Cauchy slice. It has a bulk operator
algebra $\widetilde\M_b \subset B(\HH_\Psi^{\text{Fock}})$. (Throughout this chapter, bulk algebras carry a
tilde, to keep them visually distinct from boundary algebras.) By \eqref{eq:full_algebra_identity}, this is
also a subalgebra of $B(\HH_\Psi^{\text{GNS}})$. When we view it as a boundary algebra we call it $\M_b$:
\begin{equation}
\widetilde\M_b = \M_b .
\label{eq:subregion_subalgebra}
\end{equation}
Read this as a literal equality, not as an analogy or a matching of some properties. There is one algebra,
with two descriptions.

Chapter 4 explained how an algebra, together with a state, encodes causal structure, entanglement, and
modular flow. Since $\M_b=\widetilde\M_b$, **the boundary algebra $\M_b$ already encodes the
corresponding structure of the bulk region $b$**. For example, the modular operator of $\widetilde\M_b$
describes how $b$ is entangled with its complement. It is exactly the modular operator of $\M_b$, and that
can be computed from boundary data alone. **This is why a bulk region can be fully "reconstructed"
from the corresponding boundary algebra.** This statement is subregion-subalgebra duality. You have already
met two special cases of it in Chapter 6. The identifications $\widetilde\M_R=Y_R$ and $\widetilde\M_L=Y_L$
of the two black-hole exteriors in the thermofield double are exactly \eqref{eq:subregion_subalgebra}, with
$b$ taken to be the whole right or the whole left exterior region.

At this order the bulk theory is effectively a free quantum field theory, and $\widetilde\M_b$ is one of its
local algebras. So $\widetilde\M_b$ has every structural property of such algebras found in Chapter 4. By
\eqref{eq:subregion_subalgebra}, the boundary algebra $\M_b$ has the same properties:

1. **Reeh—Schlieder**: the bulk "vacuum" $\ket0_{\phi_c}$ is cyclic and separating for
$\widetilde\M_b$. Chapter 6 identified this vacuum with the boundary GNS vacuum, $\ket0_{\phi_c}=\ket1_\Psi$.
So $\ket1_\Psi$ is cyclic and separating for $\M_b$ too.
2. **Causality**: $\widetilde\M_b=\widetilde\M_{\widehat b}$, where $\widehat b$ is the domain of
dependence of $b$. In words, the algebra of a region equals the algebra of its full domain of dependence
(the time-slice axiom of Chapter 4). So $\M_b$ reconstructs the whole of $\widehat b$, not only $b$ itself.
3. **Type $\mathrm{III**_1$}: every local algebra of a continuum quantum field theory is type
$\mathrm{III}_1$ (Chapter 4). So $\widetilde\M_b$ is type $\mathrm{III}_1$, and $\M_b$ must be too.
4. **Additivity** for topologically trivial regions: $\widetilde\M_{b_1\cup b_2}=\widetilde\M_{b_1}
\vee\widetilde\M_{b_2}$.
5. **Haag duality**: $\widetilde\M_{b'}=\widetilde\M_b'$, where $b'$ is the bulk causal complement of
$b$ on its Cauchy slice.

Each of these bulk statements becomes a checkable statement about boundary algebras once it is translated
through \eqref{eq:subregion_subalgebra}. The worked examples in the rest of this chapter all come from such
translations.

## Entanglement wedge reconstruction, algebraically

### Defining the boundary algebra $X_A$ properly

Take a boundary spatial region $A$ on a constant-time Cauchy slice. Its **Ryu—Takayanagi (RT) surface**
$\gamma_A$ is the bulk surface of minimal area anchored on $\partial A$. The bulk region $b_A$ lying between
$A$ and $\gamma_A$ is the bulk region dual to $A$. The **entanglement wedge** $\widehat b_A$ is the bulk
domain of dependence of $b_A$ (Figure~\ref{fig:rt_entanglement_wedge}). We write $X_A$ for the boundary
algebra that subregion-subalgebra duality assigns to $b_A$:
\begin{align}
X_A \equiv \M_{b_A} &\eqstep{1} \widetilde\M_{b_A} \eqstep{2} \widetilde\M_{\widehat b_A} ,
\label{eq:XA_def}
\end{align}
**(1)** subregion-subalgebra duality \eqref{eq:subregion_subalgebra} for the region $b=b_A$.\quad
**(2)** the causality property: a bulk region's algebra equals that of its domain of dependence.

So $X_A\subset B(\HH_\Psi^{\text{GNS}})$ is the boundary algebra dual to the entanglement wedge of $A$.
Entanglement wedge reconstruction is usually stated as: physics inside $\widehat b_A$ can be fully recovered
from $A$ alone. Equation \eqref{eq:XA_def} restates this as a literal identity between algebras.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.82\textwidth]{figs/fig_rt.pdf}
\caption{(a) A constant-time slice of AdS drawn as a disk, whose edge is the boundary: the Ryu—Takayanagi surface $\gamma_A$ (blue) is the minimal curve anchored at the endpoints of the boundary region $A$ (red), $b_A$ (gold) is the bulk region between them, and $\bar A$ is the rest of the boundary. The entropy of $A$ is $S(A)=\mathrm{Area}(\gamma_A)/4G_N+S_{\rm bulk}(b_A)=S_{\rm gen}(b_A)$. (b) A side view, with time running upward, cut through the middle of $A$: the entanglement wedge $\widehat b_A$ (gold), bounded by light rays, is the domain of dependence of $b_A$; it meets the boundary along $\widehat A$ (red), and its tip on the $t=0$ slice (dashed) is $\gamma_A$ (blue dot).}
\label{fig:rt_entanglement_wedge}
\end{figure}

The boundary construction of $X_A$ needs some care. It is used many times below, so here it is in detail.
At finite $N$ there is an ordinary von Neumann algebra $B_A^{(N)}$ of operators localized in $A$. It
satisfies $B_A^{(N)}=B_{\widehat A}^{(N)}$, where $\widehat A$ is the boundary domain of dependence of $A$.
This is the ordinary time-slice axiom. As $N\to\infty$, many operators in $B_A^{(N)}$ have no sensible limit
and drop out. The right object is built from the operators that do survive the limit in the state $\Psi$:

$$

X_A \equiv \pi_\Psi\Big(\lim_{N\to\infty,\Psi}B_A^{(N)}\Big)'' = X_{\widehat A} .

$$

Here $\pi_\Psi$ is the GNS representation. The double commutant plays the same role as in the GNS discussion
of Chapter 2: it makes the result a genuine von Neumann algebra. The equality with $X_{\widehat A}$ holds
because the finite-$N$ time-slice axiom survives the limit. The content of entanglement wedge reconstruction
is that this boundary-defined algebra equals the bulk algebra in \eqref{eq:XA_def}.

A second algebra is easier to construct. The algebra $Y_{\widehat A}$ is generated by single-trace operators
restricted to $\widehat A$. It is the single-trace algebra $Y_O$ of Chapter 6, taken for the region
$\widehat A$. Single-trace operators in any region survive the large-$N$ limit by construction, so
\begin{equation}
Y_{\widehat A} \subseteq X_A .
\label{eq:YA_in_XA}
\end{equation}
The rest of this section studies this inclusion: what $Y_{\widehat A}$ describes in the bulk, and what else
$X_A$ contains.

### Causal wedge reconstruction: the "easy" part of $X_A$

Causal wedge reconstruction is also known as HKLL reconstruction (after Hamilton, Kabat, Lifschytz, and
Lowe). It concerns the **causal wedge**

$$

C_{\widehat A}\equiv \widetilde J^+(\widehat A)\cap\widetilde J^-(\widehat A) ,

$$

where $\widetilde J^\pm$ denote the bulk causal future and past. So $C_{\widehat A}$ is the set of bulk points
that can both receive signals from $\widehat A$ and send signals to $\widehat A$. Causal wedge reconstruction
states that bulk fields in $C_{\widehat A}$ can be written directly as single-trace operators smeared over
$\widehat A$:
\begin{equation}
\Phi(X) = \int d^dx\,K_A^{(C)}(X;x)\,\pi_\Psi(O(x)), \qquad X\in C_{\widehat A},\ x\in\widehat A .
\label{eq:HKLL_region}
\end{equation}
Here $K_A^{(C)}$ is an explicit kernel. In general it is a distribution rather than a smooth function. This
is the HKLL construction of Chapter 6, now applied to a general region instead of the whole boundary.
Algebraically, it says

$$

\widetilde\M_{C_{\widehat A}} = Y_{\widehat A} .

$$

For $A$ equal to a full boundary, this is the black-hole exterior identification of Chapter 6.

The causal wedge always lies inside the entanglement wedge, $C_{\widehat A}\subseteq\widehat b_A$. This is a
standard geometric fact. It says that causal reconstruction is always more conservative than
entanglement-based reconstruction. Combine this fact with the definition \eqref{eq:XA_def} and with
$\widetilde\M_{C_{\widehat A}}=Y_{\widehat A}$. The inclusion \eqref{eq:YA_in_XA} then follows at once: it is
the algebraic image of the geometric inclusion $C_{\widehat A}\subseteq\widehat b_A$.

### Where the rest of $X_A$ comes from: modular flow, made explicit

The double-commutant definition fixes $X_A$ abstractly. It does not say which operators $X_A$ contains
beyond $Y_{\widehat A}$. On the gravity side, the entanglement wedge is generically strictly larger than the
causal wedge. Equality holds only in special, highly symmetric cases. So generically
$Y_{\widehat A}\subsetneq X_A$.

Here the ergodic lemma of Chapter 4 does real work. The lemma concerns two von Neumann algebras
$\N\subset\mathcal X$ and a vector that is cyclic and separating for both. It says that the modular flow of
the larger algebra $\mathcal X$, applied to the smaller algebra $\N$, generates all of $\mathcal X$.

We apply it with $\mathcal X=X_A$. Since $b_A$ is a genuine bulk local region, $\ket1_\Psi$ is cyclic and
separating for $X_A=\widetilde\M_{b_A}$. Call the corresponding modular operator $\Delta_{X_A}$. By
\eqref{eq:subregion_subalgebra}, it equals the bulk modular operator $\widetilde\Delta_{b_A}$. For the smaller
algebra we take $Y_A^\epsilon$. This is the algebra of single-trace operators smeared within a thin time band
of width $\epsilon$ around $A$. Picture a thin strip of boundary spacetime hugging the region $A$. Its causal
wedge is a thin open bulk region next to $A$, so by the Reeh—Schlieder property $\ket1_\Psi$ is still cyclic
and separating for $Y_A^\epsilon$. The lemma then says that modular flow of the *emph* algebra $X_A$
regenerates all of $X_A$ from this thin sliver:

$$

X_A = \Big\{\, \Delta_{X_A}^{-is}\,O_\epsilon(\vec x)\,\Delta_{X_A}^{is} \ :\ \vec x\in A,\ s\in\mathbb R
\,\Big\}'' .

$$

Here $O_\epsilon(\vec x)$ is a single-trace operator smeared over the thin band near the point $\vec x$.
**The extra operators in $X_A$, beyond single-trace operators smeared over $\widehat A$, are
single-trace operators carried along by modular flow.**

Write $O(s;\vec x)\equiv\Delta_{X_A}^{-is}\,O_\epsilon(\vec x)\,\Delta_{X_A}^{is}$ for these modular-flowed
operators. At the free-field level of the large-$N$ limit the state is Gaussian. The modular flow of a
Gaussian state maps each smeared field to another field that is again linear in the original fields. A bulk
field is itself linear in the fields. So a bulk field anywhere in the entanglement wedge, not only in the
causal wedge, can be written as

$$

\Phi(X) = \int_{-\infty}^\infty ds\int d\vec x\,K_A^{(E)}(X;s,\vec x)\,O(s;\vec x), \qquad X\in\widehat b_A .

$$

This is the entanglement-wedge generalization of the HKLL formula \eqref{eq:HKLL_region}. Formulas of this
type were first proposed on other grounds. Here their existence follows directly from modular theory. The
kernel $K_A^{(E)}$ is in general not known in closed form.

A related result, the **JLMS relation** (Jafferis, Lewkowycz, Maldacena, and Suh, 2015), connects
boundary and bulk modular flow at large but finite $N$. In the strict large-$N$ limit it reduces to the
statement $\Delta_{X_A}=\widetilde\Delta_{b_A}$ used above. The JLMS relation is often quoted without
derivation. The box below shows how it fits together with two other holographic results.

\begin{keyresult}[: The JLMS relation and modular flow]
**Statement (JLMS).** Let $A$ be a boundary spatial region, with entanglement wedge $b_A$ bounded by the
RT surface $\gamma_A$. Work on the code subspace, the space of semiclassical states around a fixed
background. Let $\sigma$ be a reference state in it, and write the modular Hamiltonians with density matrices
(at large but finite $N$, with a short-distance cutoff where needed):

$$

H_A \equiv -\log\sigma_A , \qquad H_{\text{bulk}} \equiv -\log\sigma_{b_A} .

$$


1. The boundary and bulk modular Hamiltonians obey an operator identity on the code subspace,

$$

H_A = \frac{\hat A[\gamma_A]}{4G_N} + H_{\text{bulk}} + \mathcal{O}(G_N) ,

$$

where $\hat A[\gamma_A]$ is the area operator of the RT surface. (The area term is understood to include the
local terms on $\gamma_A$, such as counterterms, that also appear in the FLM formula below.)
2. For any bulk operator $\Phi \in \widetilde\M_{b_A}$ in the entanglement wedge,

$$

\Delta_A^{-is}\,\Phi\,\Delta_A^{is} = \widetilde\Delta_{b_A}^{-is}\,\Phi\,\widetilde\Delta_{b_A}^{is} .

$$

In words, boundary modular flow acts on every entanglement-wedge operator exactly as bulk modular flow does.


**How the pieces fit.** The argument below takes two inputs: the equality of bulk and boundary relative
entropies (step 1), and the FLM formula (step 3). JLMS originally argued in the other direction. They started
from FLM, derived the modular Hamiltonian identity, and then obtained the equality of relative entropies.
Given FLM, the two statements are equivalent at this order. So the argument shows how the pieces fit
together. It is not a derivation from first principles.

1. **Relative entropy equality.**
Let $\sigma$ be a reference background state, such as the global vacuum or the thermofield double. Let $\rho$
be any nearby excited state in the code subspace. The input is that the relative entropy of the boundary
region $A$ equals that of the bulk entanglement wedge $b_A$, up to small corrections:

$$

D(\rho_A \| \sigma_A) = D(\rho_{\text{bulk}} \| \sigma_{\text{bulk}}) + \mathcal{O}(G_N) .

$$

2. **Relative entropy in terms of modular Hamiltonians.**
For any two density matrices, with $H^\sigma\equiv-\log\sigma$,
\begin{align}
D(\rho\|\sigma) &\eqstep{1} \Tr(\rho\log\rho) - \Tr(\rho\log\sigma) \notag\\
&\eqstep{2} -S(\rho) + \Braket{H^\sigma}_\rho . \notag
\end{align}
**(1)** the definition of relative entropy.\quad
**(2)** $S(\rho)=-\Tr(\rho\log\rho)$, and $-\log\sigma=H^\sigma$.

Applied to the boundary state and to the bulk state in the entanglement wedge, this gives
\begin{align*}
D(\rho_A \| \sigma_A) &= -S(\rho_A) + \Braket{H_A}_\rho , \\
D(\rho_{\text{bulk}} \| \sigma_{\text{bulk}}) &= -S(\rho_{\text{bulk}}) + \Braket{H_{\text{bulk}}}_\rho .
\end{align*}
3. **The FLM formula.**
The Faulkner—Lewkowycz—Maldacena (FLM) formula is the quantum-corrected RT formula. It says that the
boundary entanglement entropy equals the bulk generalized entropy, at leading and first subleading order:

$$

S(\rho_A) = \Braket{\frac{\hat A[\gamma_A]}{4G_N}}_\rho + S(\rho_{\text{bulk}}) + \mathcal{O}(G_N) .

$$

4. **Cancellation of the bulk entropy.**
Start from the boundary relative entropy and use steps 2, 3, and 1 in turn:
\begin{align}
D(\rho_A \| \sigma_A)
&\eqstep{1} -S(\rho_A) + \Braket{H_A}_\rho \notag\\
&\eqstep{2} -\Braket{\frac{\hat A[\gamma_A]}{4G_N}}_\rho - S(\rho_{\text{bulk}}) + \Braket{H_A}_\rho
  + \mathcal O(G_N) \notag\\
&\eqstep{3} -S(\rho_{\text{bulk}}) + \Braket{H_{\text{bulk}}}_\rho + \mathcal O(G_N) . \notag
\end{align}
**(1)** step 2 applied to the boundary state.\quad
**(2)** insert the FLM formula of step 3 for $S(\rho_A)$.\quad
**(3)** the relative entropy equality of step 1, with the bulk relative entropy written out using
step 2.

The bulk entropy $S(\rho_{\text{bulk}})$ appears on both sides of the last equality, so it cancels.
Rearranging what is left gives

$$

\Braket{H_A}_\rho = \Braket{\frac{\hat A[\gamma_A]}{4G_N} + H_{\text{bulk}}}_\rho + \mathcal O(G_N) .

$$

5. **From expectation values to an operator identity.**
This equality holds for *emph* state $\rho$ in the code subspace. The expectation values of a Hermitian
operator in all density matrices supported on a subspace determine that operator's restriction to the
subspace. So the two operators agree on the code subspace:

$$

H_A = \frac{\hat A[\gamma_A]}{4G_N} + H_{\text{bulk}} + \mathcal{O}(G_N) .

$$

6. **Action on bulk operators.**
Let $\Phi \in \widetilde\M_{b_A}$ be an operator localized in the interior of the entanglement wedge. The RT
surface $\gamma_A = \partial b_A$ is the edge of the wedge, so it is spacelike separated from $\Phi$. At
leading order the area operator therefore commutes with $\Phi$:

$$

\left[\frac{\hat A[\gamma_A]}{4G_N}, \, \Phi\right] = 0 .

$$

Now compute the commutator of $\Phi$ with the boundary modular Hamiltonian:
\begin{align}
[H_A, \, \Phi] &\eqstep{1} \left[\frac{\hat A[\gamma_A]}{4G_N} + H_{\text{bulk}}, \, \Phi\right]
\eqstep{2} [H_{\text{bulk}}, \, \Phi] . \notag
\end{align}
**(1)** the operator identity of step 5, at leading order.\quad
**(2)** the commutator is linear, and the area term commutes with $\Phi$.

The operator $[H_{\text{bulk}},\Phi]$ again lies in $\widetilde\M_{b_A}$, so the same step applies to it.
Hence all nested commutators agree, $[H_A,[H_A,\dots[H_A,\Phi]]]=[H_{\text{bulk}},[H_{\text{bulk}},\dots
[H_{\text{bulk}},\Phi]]]$. Summing the exponential series of nested commutators then gives, formally,

$$

e^{is H_A}\, \Phi\, e^{-is H_A} = e^{is H_{\text{bulk}}}\, \Phi\, e^{-is H_{\text{bulk}}} .

$$

Finally, the full modular operator is $\Delta_A=\sigma_A\otimes\sigma_{\bar A}^{-1}$. Its $\sigma_{\bar A}$
factor commutes with $\Phi$, so $\Delta_A^{-is}\Phi\Delta_A^{is}=\sigma_A^{-is}\Phi\sigma_A^{is}
=e^{isH_A}\Phi e^{-isH_A}$. The same holds in the bulk. Therefore

$$

\Delta_A^{-is}\,\Phi\,\Delta_A^{is} = \widetilde\Delta_{b_A}^{-is}\,\Phi\,\widetilde\Delta_{b_A}^{is} .
\qquad \blacksquare

$$


\end{keyresult}

When is the causal-wedge piece already everything, so that $X_A=Y_{\widehat A}$? This happens exactly when the
bulk modular flow of $b_A$ acts *emph*. That means it acts as a pointwise coordinate
transformation, like the Rindler-wedge boost of Chapter 4. A flow of this kind maps operators localized in
$\widehat A$ to operators that are still localized in $\widehat A$, so it generates nothing new. This happens
for a half-space or a spherical region in the vacuum, and for the full boundary in the thermofield double.
These are exactly the cases already worked out explicitly. In them $X_A=Y_{\widehat A}$ and
$\widehat b_A=C_{\widehat A}$ hold exactly. In general, though, modular flow is *emph* geometric, and the
inclusion \eqref{eq:YA_in_XA} is strict.


> [!NOTE] **Physics Connection: Modular Flow and Operator Generation**
> **You have already met a finite-dimensional version of this object in Chapter 4.** There, the modular
> flow of a single entangled pair, $\sigma_s(A)=\rho_R^{-is}A\rho_R^{is}$, was an ordinary unitary conjugation.
> You worked it out explicitly on a $4\times4$ matrix. Here the same object, the modular flow of a boundary
> algebra, does something with no finite-dimensional analogue. Starting from a small algebra, it generates
> operators that were not in that algebra, and in fact the whole larger algebra. This is possible only because
> the algebras involved are infinite-dimensional (here, type $\mathrm{III}_1$).
> 
> In finite dimensions the ergodic lemma has no content. Suppose $\N\subset\M$ act on a finite-dimensional
> Hilbert space $\HH$, and a vector $\ket\Omega$ is cyclic for $\N$ and separating for $\M$. Because
> $\ket\Omega$ is separating for $\M$, the map $x\mapsto x\ket\Omega$ is injective on $\M$, so
> $\dim\M\le\dim\HH$. Because $\ket\Omega$ is cyclic for $\N$, the vectors $x\ket\Omega$ with $x\in\N$ fill all
> of $\HH$, so $\dim\N\ge\dim\HH$. Together these give $\dim\N\ge\dim\M$, and so $\N=\M$. In finite dimensions
> a proper subalgebra can never share such a vector with the larger algebra. There is nothing left for
> modular flow to fill in.
> 
> In infinite dimensions the situation is different. By the Reeh—Schlieder property, a small subalgebra, such
> as the thin sliver above, can have the same cyclic and separating vector as the larger algebra. Modular flow
> can then sweep out the entire larger algebra from the sliver. This is the "ergodic" lemma of Chapter 4, now
> doing physical work: it builds an entire entanglement wedge, or a black-hole interior, out of a thin sliver of
> boundary time. The definition of modular flow has not changed. What changed is that infinite dimensions let it
> do something a finite matrix conjugation cannot.


### Two logically distinct sources of type $\mathrm{III}_1$

Both $X_A$ and $Y_{\widehat A}$ are type $\mathrm{III}_1$. This property can have two different physical
origins, and it helps to keep them apart.

The first origin is the one met in Chapter 4. For a continuum quantum field theory at finite $N$, the local
algebra $B_A^{(N)}$ is already type $\mathrm{III}_1$. The cause is the infinite amount of *emph*-range
entanglement across the boundary $\partial A$. In the bulk, this matches the fact that the RT surface reaches
the AdS boundary, which is at infinite proper distance.

To isolate the second origin, put the boundary theory on a lattice. Then at any finite $N$ the algebra
$B_A^{(N)}$ is type I: it is an algebra of finite matrices, with minimal projections. Yet $X_A$ and
$Y_{\widehat A}$, defined through the large-$N$ limit, are *emph* type $\mathrm{III}_1$. So their type
$\mathrm{III}_1$ property does not come from the type of $B_A^{(N)}$ before the limit. It comes from an
infinite amount of *emph*-range entanglement between $A$ and its complement, which appears only in the
strict $N\to\infty$ limit. In the bulk, this matches the infinite short-range entanglement of bulk fields
across the RT surface $\gamma_A$ (or, for $Y_{\widehat A}$, across the edge $\chi_{\widehat A}$ of the causal
wedge).

So two independent mechanisms produce the same type of algebra, at two different stages of the same
construction: finite $N$, and the strict $N\to\infty$ limit.

The same picture gives an algebraic way to locate the RT surface. Near $\gamma_A$, bulk modular flow acts as a
local boost. This is the local-Rindler argument of Chapter 4, applied at the RT surface. The surface
$\gamma_A$ is the fixed ("invariant") set of that boost. By the JLMS relation, boundary modular flow acts on
wedge operators as bulk modular flow does. So **the RT surface can be characterized, without assuming a
bulk metric, as the asymptotic fixed-point set of the boundary modular flow**. This gives an algebraic
restatement of the procedure for finding the RT surface.

### Extended gravitational systems: algebra without any geometry to point to

The entanglement-wedge and causal-wedge story extends beyond geometric boundary regions. Replace $A$ by
*emph* von Neumann subalgebra $\M$ of the boundary theory. Then define $X_\M$ by the direct analogue of the
double-commutant definition of $X_A$. This definition makes sense even when there is no bulk geometric
picture at all.

One can go further. Couple a gravitational sector $B$ (which has its own boundary dual) to an ordinary
non-gravitational sector $R$. For example, $R$ could be radiation that has already escaped to infinity. For
any subsystem $Q$ of the combined system $B\cup R$, define two algebras:

- the entanglement wedge algebra $X_Q\equiv\lim_{G_N\to0,\Psi}B_Q$, whether or not it has a geometric
meaning;
- the causal wedge algebra $Y_Q$, the algebra of $Q$'s ordinary low-energy effective description.

This abstraction is exactly what the evaporating-black-hole discussion later in this chapter needs. There,
$Q$ will be the emitted Hawking radiation.

## Quantum informational aspects of entanglement wedge reconstruction

### Superadditivity, and its boundary origin

**Entanglement wedge nesting** is a standard geometric fact, which follows from the extremality of RT
surfaces. For boundary regions $A_1\subseteq A_2$, the entanglement wedges satisfy
$\widehat b_{A_1}\subseteq\widehat b_{A_2}$. Algebraically this is just $X_{A_1}\subseteq X_{A_2}$, which
follows immediately from $A_1\subseteq A_2$ and the definition of $X_A$.

Nesting has a direct geometric consequence. For two regions $A_1,A_2$ on one Cauchy slice,

$$

b_{A_1}\cup b_{A_2} \subseteq b_{A_1\cup A_2}, \qquad b_{A_1\cap A_2}\subseteq b_{A_1}\cap b_{A_2} .

$$

This is a consequence of nesting, not an extra assumption. In words, the entanglement wedge of a union is at
least as big as the union of the entanglement wedges, and generically it is strictly bigger. This is
**superadditivity of entanglement wedges**. Two AdS$_3$ examples make it concrete: two overlapping
boundary intervals, and two disjoint intervals placed close together. In both cases the RT surface of the
union "jumps" and encloses visibly more bulk than the two pieces do separately. Translated through the
definition \eqref{eq:XA_def}, superadditivity becomes a statement purely about boundary algebras:
\begin{equation}
X_{A_1}\vee X_{A_2} \subseteq X_{A_1\cup A_2}, \qquad X_{A_1\cap A_2}\subseteq X_{A_1}\wedge X_{A_2} .
\label{eq:superadditivity_alg}
\end{equation}

Compare this with the additivity axiom of Chapter 4 for an ordinary relativistic quantum field theory at
finite $N$. For topologically trivial regions, that axiom says $B_{A_1}^{(N)}\vee B_{A_2}^{(N)}
=B_{A_1\cup A_2}^{(N)}$. **For the inclusions \eqref{eq:superadditivity_alg** to be strict, ordinary
additivity has to fail in the strict large-$N$ limit.} One can show that it does fail in the two AdS$_3$
examples above. The argument uses a classic result of Araki. It identifies $X_{A_1}\vee X_{A_2}$ concretely as
the algebra of single-trace operators in a specific larger causal region. That algebra is strictly smaller
than $X_{A_1\cup A_2}$. (We quote this computation without reproducing it.) **Superadditivity of
entanglement wedges is the bulk geometric image of the failure of additivity for boundary algebras in the
strict large-$N$ limit.** Algebras of local regions are then no longer "locally generated" in the way the
algebras of an ordinary finite-$N$ quantum field theory are.

Haag duality, by contrast, survives. Assume it holds for the bulk algebras, $\widetilde\M_{b'}=
\widetilde\M_b'$. For a pure global state, $A$ and its complement $\bar A$ share the same RT surface. So
$b_{\bar A}$ is the bulk complement $b_A'$. Then Haag duality holds in the large-$N$ limit:

$$

X_{A}' = X_{\bar A} .

$$

The single-trace algebra $Y_{\widehat A}$ behaves in the opposite way. It is additive by construction, but in
general it does *emph* satisfy Haag duality.

### Quantum error correction, made precise

Entanglement wedge reconstruction has long been interpreted in the language of quantum error correction.
All the information in $b_A$ can be recovered from boundary data on $A$ alone. So this information is
protected against "erasing" the complementary region $\bar A$ entirely. Superadditivity makes this more
precise and checkable.

Take an operator $\Phi(X)$ at a point $X$ in a bulk region $b$. Suppose $b$ lies in the *emph*
of the entanglement wedges of two different boundary regions $A$ and $\widetilde A$, but outside the
entanglement wedge of $A\cap\widetilde A$. Picture two overlapping boundary intervals. Their wedges overlap
in a bulk region that reaches deeper than the wedge of their small common piece. Now use the HKLL-type formula
\eqref{eq:HKLL_region}. For concreteness, take a case in the vacuum sector (GNS representation $\pi_\Omega$)
where the causal and entanglement wedges coincide for both $A$ and $\widetilde A$. Then
\begin{equation}
\Phi(X) = \pi_\Omega(O_A(X)) = \pi_\Omega(O_{\widetilde A}(X)) .
\label{eq:double_reconstruction}
\end{equation}
Here $O_A(X)$ and $O_{\widetilde A}(X)$ are two *emph* boundary operators. They are built from
different single-trace data, smeared over $A$ and over $\widetilde A$ respectively. Yet they coincide once
represented on the GNS Hilbert space. In fact there is an infinite family of such reconstructions, one for
every boundary region whose entanglement wedge contains $b$.

**So a bulk degree of freedom $\Phi(X)$ in $b$ cannot be assigned to any one boundary region. It is
encoded collectively and redundantly across the boundary system. This is the defining feature of a quantum
error-correcting code.** This redundancy follows from superadditivity \eqref{eq:superadditivity_alg}. It is not
an extra postulate added to the holographic dictionary.

### Worked calculation: a three-qubit toy code

To see this redundancy in elementary matrix algebra, we work through a small toy code with three qubits. It is
a simplified cousin of the three-qutrit code of Almheiri, Dong, and Harlow, which is the standard example. The
qubit version is not perfect, as we will see, but it already shows the key mechanism.

Let the bulk logical state be a single qubit at the center of the disk:

$$

\ket{\psi}_L = \alpha \ket{0}_L + \beta \ket{1}_L, \qquad |\alpha|^2 + |\beta|^2 = 1 .

$$

The boundary consists of three physical qubits $A, B, C$. The encoding isometry
$V: \mathbb{C}^2 \to (\mathbb{C}^2)^{\otimes 3}$ is defined by

$$

\ket{0}_L \mapsto \frac{1}{\sqrt{2}}\big(\ket{000} + \ket{111}\big), \qquad
\ket{1}_L \mapsto \frac{1}{\sqrt{2}}\big(\ket{100} + \ket{011}\big) .

$$

The four basis states that appear are distinct, so the two code states are orthonormal and $V$ is an
isometry. The encoded boundary state is
\begin{align*}
\ket{\Psi(\alpha,\beta)}
&= \frac{\alpha}{\sqrt{2}}\big(\ket{000}_{ABC} + \ket{111}_{ABC}\big) \\
&\quad + \frac{\beta}{\sqrt{2}}\big(\ket{100}_{ABC} + \ket{011}_{ABC}\big) .
\end{align*}

**A single qubit.** Compute the reduced density matrix of qubit $C$ by tracing out qubits $A$ and $B$:

$$

\rho_C = \Tr_{AB}\big(\ket{\Psi}\bra{\Psi}\big) = \sum_{a,b \in \{0,1\}} \braket{ab|\Psi}\braket{\Psi|ab} .

$$

Here $\braket{ab|\Psi}$ is a (unnormalized) state of qubit $C$. The four overlaps with the basis states of
$AB$ are
\begin{align*}
\braket{00|\Psi} &= \tfrac{\alpha}{\sqrt{2}}\ket{0}_C , &
\braket{00|\Psi}\braket{\Psi|00} &= \tfrac{|\alpha|^2}{2}\ket{0}\bra{0}_C , \\
\braket{10|\Psi} &= \tfrac{\beta}{\sqrt{2}}\ket{0}_C , &
\braket{10|\Psi}\braket{\Psi|10} &= \tfrac{|\beta|^2}{2}\ket{0}\bra{0}_C , \\
\braket{11|\Psi} &= \tfrac{\alpha}{\sqrt{2}}\ket{1}_C , &
\braket{11|\Psi}\braket{\Psi|11} &= \tfrac{|\alpha|^2}{2}\ket{1}\bra{1}_C , \\
\braket{01|\Psi} &= \tfrac{\beta}{\sqrt{2}}\ket{1}_C , &
\braket{01|\Psi}\braket{\Psi|01} &= \tfrac{|\beta|^2}{2}\ket{1}\bra{1}_C .
\end{align*}
Each $AB$ basis state picks out exactly one of the four terms of $\ket\Psi$. Summing:
\begin{align}
\rho_C &\eqstep{1} \left(\frac{|\alpha|^2 + |\beta|^2}{2}\right)\ket{0}\bra{0}_C
+ \left(\frac{|\alpha|^2 + |\beta|^2}{2}\right)\ket{1}\bra{1}_C \notag\\
&\eqstep{2} \frac{1}{2}\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \frac{1}{2}\id_2 . \notag
\end{align}
**(1)** add the four terms of the table, grouping the two that multiply $\ket0\bra0_C$ and the two that
multiply $\ket1\bra1_C$.\quad
**(2)** normalization of the logical state, $|\alpha|^2+|\beta|^2=1$.

So $\rho_C$ is proportional to the identity matrix. It does not depend on the logical amplitudes $\alpha$ and
$\beta$ at all. The same four-overlap computation for qubit $B$ (now tracing out $A$ and $C$) gives the same
answer, $\rho_B=\tfrac12\id_2$. So qubit $B$ alone and qubit $C$ alone each contain **no** information
about the central bulk qubit. Qubit $A$ is different. The same computation gives
$\rho_A=\tfrac12\id_2+\Re(\alpha\beta^*)\,X_A$, which does depend on the logical state. (These three reduced
density matrices were also checked numerically.) Three qubits are too few for a code in which *emph*
single qubit is blind to the logical information. The perfect version of this toy code uses three qutrits
(three-level systems) instead.

**Two qubits.** Now consider reconstructing logical operators on *emph* qubits, a boundary subregion
of size 2.

1. **Logical $Z_L = \ket{0**_L\bra{0} - \ket{1}_L\bra{1}$}.
Define the boundary operator $Z_{AB} \equiv Z_A \otimes Z_B$ acting on region $AB$. Then
\begin{align}
(Z_A \otimes Z_B \otimes \id_C)\ket{0}_L &\eqstep{1} \tfrac{1}{\sqrt{2}}\big( (+1)(+1)\ket{000}
+ (-1)(-1)\ket{111}\big) \notag\\
&\eqstep{2} \ket{0}_L , \notag\\
(Z_A \otimes Z_B \otimes \id_C)\ket{1}_L &\eqstep{1} \tfrac{1}{\sqrt{2}}\big( (-1)(+1)\ket{100}
+ (+1)(-1)\ket{011}\big) \notag\\
&\eqstep{2} -\ket{1}_L . \notag
\end{align}
**(1)** $Z$ gives $+1$ on $\ket0$ and $-1$ on $\ket1$, applied to qubits $A$ and $B$; the identity leaves
qubit $C$ alone.\quad
**(2)** multiply the signs and compare with the encoding of $\ket0_L$ and $\ket1_L$.

Hence $(Z_{AB} \otimes \id_C)\ket{\psi}_L = Z_L\ket{\psi}_L$.
2. **Logical $X_L = \ket{0**_L\bra{1} + \ket{1}_L\bra{0}$}.
Define the boundary operator $X_{AB} \equiv X_A \otimes \id_B$ on region $AB$. (It acts nontrivially only on
qubit $A$.) Then
\begin{align}
(X_A \otimes \id_B \otimes \id_C)\ket{0}_L &\eqstep{1} \tfrac{1}{\sqrt{2}}\big(\ket{100} + \ket{011}\big)
\eqstep{2} \ket{1}_L , \notag\\
(X_A \otimes \id_B \otimes \id_C)\ket{1}_L &\eqstep{1} \tfrac{1}{\sqrt{2}}\big(\ket{000} + \ket{111}\big)
\eqstep{2} \ket{0}_L . \notag
\end{align}
**(1)** $X$ flips qubit $A$, $\ket0\leftrightarrow\ket1$, and leaves $B$ and $C$ alone.\quad
**(2)** compare with the encoding of $\ket1_L$ and $\ket0_L$.

Hence $(X_{AB} \otimes \id_C)\ket{\psi}_L = X_L\ket{\psi}_L$.


The logical $X_L$ can also be reconstructed on the complementary region $BC$, as
$X_{BC} \equiv \id_A \otimes X_B \otimes X_C$:
\begin{align}
(\id_A \otimes X_B \otimes X_C)\ket{0}_L &\eqstep{1} \tfrac{1}{\sqrt{2}}\big(\ket{011} + \ket{100}\big)
\eqstep{2} \ket{1}_L , \notag\\
(\id_A \otimes X_B \otimes X_C)\ket{1}_L &\eqstep{1} \tfrac{1}{\sqrt{2}}\big(\ket{111} + \ket{000}\big)
\eqstep{2} \ket{0}_L . \notag
\end{align}
**(1)** flip qubits $B$ and $C$ in each basis state: $\ket{000}\to\ket{011}$, $\ket{111}\to\ket{100}$,
$\ket{100}\to\ket{111}$, $\ket{011}\to\ket{000}$.\quad
**(2)** compare with the encoding.

Flipping only qubit $B$ would not work: $X_B\ket0_L=\tfrac1{\sqrt2}(\ket{010}+\ket{101})$ lies outside the
code subspace. Both $X_A \otimes \id_B \otimes \id_C$ and $\id_A \otimes X_B \otimes X_C$ act on the code
subspace as the central bulk operator $\Phi(0) = X_L$. Yet they are supported on disjoint, complementary
boundary regions ($A$ versus $BC$). The same kind of redundancy holds for $Z_L$. Repeating the sign computation
above with $Z$ on qubits $A$ and $C$ shows that $Z_A\otimes\id_B\otimes Z_C$ also acts as $Z_L$. So $Z_L$ can
be built on $AB$ or on $AC$.

To summarize: each of the regions $AB$ and $AC$ reconstructs the full logical algebra (both $X_L$ and $Z_L$).
The region $BC$ does not. It reconstructs $X_L$ but not $Z_L$. The reason is that every operator on $BC$
commutes with $X_A$, which acts as $X_L$, so the logical action of any operator on $BC$ must commute with
$X_L$. (A search over all three-qubit Pauli strings confirms this list of reconstructions numerically.) In the
three-qutrit code, by contrast, any two of the three qutrits reconstruct every logical operator. Even in this
imperfect qubit version, the same logical operator lives on several different boundary regions. This is the
algebraic mechanism of holographic error correction.

One caveat about this picture. The "bulk Hilbert space as a code subspace" picture from quantum error
correction is literally meaningful only at finite $N$. The bulk semiclassical Hilbert space, on the other hand,
is only precisely defined at $N=\infty$. So holographic error correction is better understood as a framework
connecting the two regimes. Any finite-$N$ code is necessarily only *emph* isometric, and should
not be read as a literal, exact implementation of the holographic dictionary.


> [!NOTE] **Physics Connection: Redundant Purifications and Code Subspaces**
> The operator $\Phi(X)$ can be written using completely different boundary data (region $A$ or region
> $\widetilde A$), while remaining, in every observable sense, the same operator. This is a large-scale version
> of a fact you already know from ordinary quantum information: **purification is never unique.**
> 
> Take a single mixed qubit, $\rho=\mathrm{diag}(0.7,0.3)$. One purification uses a second qubit as the
> ancilla, $\ket\Psi_1=\sqrt{0.7}\ket{00}+\sqrt{0.3}\ket{11}$. A completely different one uses, say, a 3-level
> ancilla, $\ket\Psi_2=\sqrt{0.7}\ket{0}\ket{a}+\sqrt{0.3}\ket{1}\ket{b}$, for any orthonormal $\ket a,\ket b$ in
> the bigger ancilla space. Trace out the ancilla in either case and you get back the same $\rho$. You can check
> this directly from the definition of the partial trace: the result depends only on the Schmidt coefficients
> $\sqrt{0.7},\sqrt{0.3}$, not on which ancilla states carry them. **No measurement confined to the
> original qubit can tell you which purification, meaning which ancilla entangled in which way, is "really"
> on the other side.** The information is present, but it is not attached to any single, canonical description of
> the environment. It is attached only to the reduced state itself.
> 
> The double reconstruction \eqref{eq:double_reconstruction} works the same way, at the scale of an entire
> holographic boundary instead of one ancilla qubit. The observable content of $\Phi(X)$ on the GNS Hilbert space
> is fixed. But the choice of boundary data used to build it (region $A$ or region $\widetilde A$) is as
> non-unique as the choice of ancilla above. As in the qubit example, no measurement of the reconstructed
> operator itself can tell you which region did the reconstructing. What is new here, with no counterpart in the
> single-qubit example, is the *emph* content of that redundancy. It is not just a bookkeeping fact about
> how $\rho$ can be written as a partial trace. Superadditivity \eqref{eq:superadditivity_alg} ties it to real
> bulk geometry. It turns "purification is not unique" into ``a bulk region is stored redundantly enough to
> survive the erasure of a boundary subregion.'' That is the operational content of a quantum error-correcting
> code.


## An algebraic formulation of entanglement islands

### The island phenomenon, restated algebraically

The **entanglement island** phenomenon is central to modern derivations of the Page curve for an
evaporating black hole. It says the following. After the Page time $t_P$, the black-hole interior stops being
part of the black hole's own entanglement wedge. Instead it becomes part of the entanglement wedge of the
emitted radiation $R$.

Split the full system into the black-hole boundary theory $B$ and the radiation $R$
(Figure~\ref{fig:page_curve_islands}(b)). Before $t_P$, the minimal quantum extremal surface for $B$ is empty.
So $B$'s entanglement wedge is the whole Cauchy slice: the interior $I$ and the exterior $O$ together. After
$t_P$, a new, nontrivial quantum extremal surface $\alpha$ takes over, and $B$'s entanglement wedge shrinks to
the exterior $O$ alone. Algebraically,

$$

X_B = \begin{cases} \widetilde\M_O\vee\widetilde\M_I & t<t_P , \\ \widetilde\M_O & t>t_P . \end{cases}

$$

Since $B\cup R$ is the whole system, once $\widetilde\M_I$ drops out of $X_B$ it must appear in $R$'s
description instead. We use the entanglement-wedge algebra $X_R$ and the causal-wedge algebra $Y_R$ from the
discussion of extended gravitational systems earlier in this chapter. The transfer is then stated precisely as

$$

X_R = \begin{cases} Y_R & t<t_P , \\ Y_R\vee\widetilde\M_I & t>t_P . \end{cases}

$$


\begin{figure}[htbp]
\centering
\includegraphics[width=0.95\textwidth]{figs/fig_page_curve_islands.pdf}
\caption{(a) Entropy of the radiation $R$ against time. Hawking's no-island answer (dashed red after $t_P$) keeps growing and the black hole's area term $A_{\text{BH}}/4G_N$ (dashed blue before $t_P$) keeps shrinking; the true entropy (green) follows the smaller of the two, turning over at the Page time $t_P$. (b) Penrose diagram of a black hole that forms from a collapsing star (gold) and evaporates completely, drawn after~[AHMST]. The dashed red line is the event horizon and the zigzag the singularity; after the evaporation ends, the centre $r=0$ continues straight up. The dotted curve separates the region near the black hole, described by $B$, from the far region where the radiation collects (for an AdS black hole this is the boundary to which the bath is attached). On a Cauchy slice after $t_P$, the quantum extremal surface (red dot) lies just inside the horizon. The island $I$ (green) behind it joins the radiation region $R$ (blue) in the radiation's entanglement wedge, while the exterior $O$ between the red dot and the dotted curve belongs to $B$.}
\label{fig:page_curve_islands}
\end{figure}

This lets you *emph* an island using only data intrinsic to the radiation system, with no reference to
$B$ at all. Define

$$

I_R \equiv Y_R'\cap X_R .

$$

These are the operators in $X_R$ that commute with every operator in $Y_R$. For $t>t_P$, this intersection is
exactly $\widetilde\M_I$. An island exists exactly when the intersection is nontrivial, that is, larger than
the multiples of the identity. In that case there are operators that survive the semiclassical limit but lie
outside $R$'s ordinary low-energy effective description. As with $X_A$ versus $Y_{\widehat A}$ above, these
extra operators are generated from $Y_R$ by the modular flow of $X_R$. It is the same mechanism once more.
The same definition, $I_Q\equiv Y_Q'\cap X_Q$, applies to any subsystem $Q$ of an extended gravitational
system, not just to radiation. An island for $Q$ is whatever survives the semiclassical limit but sits outside
$Q$'s own low-energy description.

Now return to an ordinary boundary region $A$, so that $Y_Q=Y_{\widehat A}$. Then the island algebra $I_A$
consists of the operators in $X_A$ that commute with all of $Y_{\widehat A}$. These are the operators that
modular flow adds to $Y_{\widehat A}$. Geometrically, they belong to the part of the entanglement wedge $b_A$
lying outside the causal wedge. Write $c_{\widehat A}$ for the part of $b_A$ inside the causal wedge. Then
$b_A=c_{\widehat A}\cup i_A$. This is an ordinary geometric decomposition: a causal-wedge part next to the
boundary, plus a deeper leftover piece $i_A$ between the causal wedge and the RT surface. It gives

$$

X_A=Y_{\widehat A}\vee\widetilde\M_{i_A}, \qquad I_A=\widetilde\M_{i_A} .

$$

So, in this language, an island is exactly the piece of an entanglement wedge that causal-wedge (HKLL)
reconstruction alone can never reach.

\begin{keyresult}[: Derivation of the Page Curve from the Quantum Extremal Island Rule]
**The island rule for radiation.** Consider an evaporating black hole coupled to a non-gravitational
radiation reservoir. The entropy of the radiation $R$ at boundary time $t$ is found by extremizing the
generalized entropy over candidate islands $I$, whose boundaries $\partial I$ are quantum extremal surfaces
(QES), and then taking the minimum over the extrema:

$$

S(R) = \min_{\text{QES } I} \operatorname{ext}_I \left[ \frac{\operatorname{Area}(\partial I)}{4G_N}
+ S_{\text{bulk}}(R \cup I) \right] .

$$


**The Page curve in a toy model.** The model below keeps only the features needed to see the shape of the
Page curve.

1. **Evaporating black-hole geometry.**
Let the black hole form at $t = 0$ with initial horizon area $A_0$ and Bekenstein—Hawking entropy
$S_0 = A_0/4G_N$. As it radiates into the reservoir, its horizon area decreases. Let $\Gamma$ be the rate at
which its Bekenstein—Hawking entropy decreases, and take $\Gamma$ constant. (In a real evaporating black hole
the rate changes with time; a constant rate is a simplification.) Then

$$

S_{\text{BH}}(t) \equiv \frac{A_{\text{BH}}(t)}{4G_N} = S_0 - \Gamma t, \qquad t \in [0, t_{\text{evap}}] ,

$$

where $t_{\text{evap}} = S_0/\Gamma$ is the total evaporation time.
2. **Saddle 1: no island ($I = \emptyset$).**
For $I = \emptyset$ there is no boundary, $\partial I = \emptyset$, so $\operatorname{Area}(\partial I) = 0$.
The generalized entropy reduces to the bulk field-theory entropy of the radiation:

$$

S_{\text{no-island}}(R) = S_{\text{bulk}}(R) .

$$

In Hawking's semiclassical calculation, each outgoing quantum $c_k$ in the radiation is entangled with an
infalling partner mode $b_k$ behind the horizon:

$$

\ket{\text{Hawking pair}}_k \approx \frac{1}{\sqrt{2}}\big(\ket{0}_{c_k}\ket{0}_{b_k}
+ \ket{1}_{c_k}\ket{1}_{b_k}\big) .

$$

The reservoir $R$ collects only the outgoing quanta $c_k$. The partners $b_k$ stay behind the horizon. So
tracing them out leaves $R$ in a mixed state, and each new pair adds to its entropy. In the toy model we assume
that the radiation entropy grows at the same rate $\Gamma$ at which the black-hole entropy falls. (For a real
black hole the two rates differ by a factor of order one. This moves the crossing point below, but not the
shape of the curve.) Then

$$

S_{\text{no-island}}(R) = \int_0^t dt' \, \frac{dS_{\text{rad}}}{dt'} = \Gamma t .

$$

This grows without bound as $t$ increases. Eventually it exceeds the Bekenstein—Hawking entropy of the
remaining black hole. But a black hole with entropy $S_{\text{BH}}$ can be entangled with the radiation by at
most $S_{\text{BH}}$. This conflict is the **Hawking information paradox**.
3. **Saddle 2: an island ($I \ne \emptyset$).**
A second, non-empty extremum appears. Its boundary $\partial I$ is a quantum extremal surface located just
inside the event horizon. Its displacement from the horizon vanishes as $G_N\to0$. The region $I$ covers the
black-hole interior behind the horizon. The generalized entropy of this saddle is

$$

S_{\text{island}}(R) = \frac{\operatorname{Area}(\partial I)}{4G_N} + S_{\text{bulk}}(R \cup I) .

$$

Now evaluate the bulk matter entropy $S_{\text{bulk}}(R \cup I)$. The union $R \cup I$ contains *emph* the
outgoing Hawking quanta $c_k \in R$ *emph* their infalling partners $b_k \in I$. Each pair
$\ket{\text{Hawking pair}}_k$ is a pure state, so a pair lying entirely inside $R\cup I$ contributes no entropy.
The infalling and outgoing modes **purify each other**. What remains is the entropy of modes near
$\partial I$. It is of order $G_N^0$ and does not grow like $\Gamma t$:

$$

S_{\text{bulk}}(R \cup I) = \mathcal{O}(G_N^0) .

$$

So the large, steadily growing contribution is absent, and the area term dominates:
\begin{align}
S_{\text{island}}(R) &\eqstep{1} \frac{\operatorname{Area}(\partial I)}{4G_N} + \mathcal{O}(G_N^0)
\overset{(2)}{\approx} \frac{A_{\text{BH}}(t)}{4G_N} \eqstep{3} S_0 - \Gamma t . \notag
\end{align}
**(1)** the bulk term $S_{\text{bulk}}(R\cup I)$ is only $\mathcal O(G_N^0)$, because the Hawking pairs
purify each other.\quad
**(2)** the quantum extremal surface sits just inside the horizon, so its area is the horizon area up to
tiny corrections, and the $\mathcal O(G_N^0)$ term is negligible next to terms of order $1/G_N$.\quad
**(3)** the linear decrease of the horizon area from step 1.
4. **The Page time and the phase transition.**
By the island rule, the entropy is the smaller of the two saddle values:
\begin{align}
S(R) &\eqstep{1} \min\big\{ S_{\text{no-island}}(R), \, S_{\text{island}}(R) \big\}
\eqstep{2} \min\big\{ \Gamma t, \, S_0 - \Gamma t \big\} . \notag
\end{align}
**(1)** the island rule: take the smallest of the extremal values.\quad
**(2)** substitute the two saddle values found in steps 2 and 3.

Setting the two branches equal gives the **Page time** $t_P$:

$$

\Gamma t_P = S_0 - \Gamma t_P \implies t_P = \frac{S_0}{2\Gamma} = \frac{1}{2} t_{\text{evap}} .

$$

Over the lifetime of the black hole, the resulting entropy is

$$

S(R) = \begin{cases}
\Gamma t & t < t_P \quad (\text{no island}), \\
S_0 - \Gamma t = \frac{A_{\text{BH}}(t)}{4G_N} & t > t_P \quad (\text{island } I).
\end{cases}

$$

The early phase, with no island, is the Hawking phase. The late phase, with the interior island $I$, is the
unitary phase.
At $t = t_{\text{evap}}$, $S(R) \to 0$ as the black hole disappears. This is the value unitary evolution
requires: the final radiation is in a pure state.
5. **Algebraic translation.**
For $t < t_P$, the radiation algebra is simply $X_R = Y_R$. For $t > t_P$, the island forms, and
$X_R = Y_R \vee \widetilde\M_I$. The modular flow of $X_R$ then generates the entire interior algebra
$\widetilde\M_I$ from the radiation data alone. In this language, the resolution of the paradox needs no change
to semiclassical effective field theory. What changes at $t_P$ is which algebra the interior operators belong
to. $\blacksquare$

\end{keyresult}

## Boundary description of a bulk causal diamond

This section works through several concrete examples of the duality applied to regions that *emph*. These are purely interior bulk regions, described entirely through the commutant
structure of boundary algebras.

### A diamond in the center of AdS, defined purely algebraically

In the vacuum sector, take a boundary time band $I_w$ of width $w<\pi R$, where $R$ is the AdS radius. Its
causal wedge is a "spherical Rindler region" $W_{\rho_w}$. This is the part of global AdS outside a sphere of
radius $\rho_w=R\tan(\tfrac\pi2-\tfrac w{2R})$ around the center. It is identified with the single-trace
time-band algebra: $\widetilde\M_{W_{\rho_w}}=Y_{I_w}$. (For $w\ge\pi R$, $W_{\rho_w}$ contains an entire Cauchy
slice, and this reduces to the full-boundary statement of Chapter 6.) Now take the *emph* of both
sides, and use Haag duality, $\widetilde\M_{b'}=\widetilde\M_b'$:

$$

\widetilde\M_{D_{\rho_w}} = Y_{I_w}' .

$$

Here $D_{\rho_w}=W_{\rho_w}'$ is a spherical causal diamond centered in global AdS, as far from the boundary as
possible. **The boundary description of this diamond is not geometric at all. It is defined purely
algebraically, as the commutant of a boundary time-band algebra**, with no boundary region of its own to point
to.

As $w\to\pi R$, the time band covers nearly the whole boundary, and the causal wedge $W_{\rho_w}$ covers nearly
the whole bulk. Correspondingly, the diamond $D_{\rho_w}$ shrinks to an arbitrarily small, local patch of nearly
flat spacetime. At every stage it is described by the commutant of an ever-larger boundary time-band algebra.
This is a precise, operator-algebraic version of the holographic **IR/UV relation**: probing longer
boundary time scales (a bigger $Y_{I_w}$) is dual to probing shorter bulk distance scales (a smaller diamond
$D_{\rho_w}$).

### Detecting a horizon from commutant structure alone

Now repeat this in the thermofield-double black hole above the Hawking—Page temperature $T_{\text{HP}}$. Take
$Y_{I_w}^{(R)}$, the algebra of a time band of width $w$ on the right boundary. Its causal wedge is a spherical
wedge region $W_{\rho_w}$ lying strictly inside the right black-hole exterior. *emph*, $W_{\rho_w}$ never covers the entire $t=0$ slice of the exterior region. The horizon is what prevents
this. Algebraically,
\begin{equation}
(Y_{I_w}^{(R)})' \cap Y_R \ne \mathbb{C}\,\id, \qquad \text{for every } w .
\label{eq:horizon_commutant}
\end{equation}
Here $Y_R=\widetilde\M_R$ is the algebra of the whole right exterior, and $\mathbb C\,\id$ denotes the multiples
of the identity. **The existence of a bulk horizon is detected on the boundary by the following fact: no
matter how wide a time band you take, its commutant inside the $R$ algebra never becomes trivial.**

Compare this with the vacuum case just above. There, growing $w$ up to $\pi R$ eventually made the causal wedge
cover an entire Cauchy slice. There was no horizon, and correspondingly the commutant of the time band became
trivial once $w\ge\pi R$. Here, above the Hawking—Page transition, this never happens, for any $w$. This gives a
clean diagnostic, intrinsic to the boundary, that distinguishes a horizon-free geometry (such as empty AdS) from
a black hole. It uses nothing but the way commutants of nested time bands behave as the bands grow.

### A single-sided collapsing black hole, and the emergence of a horizon in real time

The richest example is a black hole formed by collapse. Take $\ket\Psi$ dual to a single-sided black hole
formed by ordinary gravitational collapse: a shell of matter falls inward from the boundary and forms a horizon
at late times. On the boundary side, this corresponds to $\ket\Psi$ thermalizing over time.

Take first an early time band $I_0$, wide enough that its causal wedge already covers a full Cauchy slice. It
gives $Y_{I_0}=B(\HH_{\text{bulk}})$, an ordinary type I algebra. No horizon has formed yet, so nothing blocks
full reconstruction. Next take, at late times well after the collapse, a semi-infinite time band $I_1$. It
reconstructs only the black-hole exterior, $\widetilde\M_R=Y_{I_1}$. Its commutant $Y_{I_1}'$ gives an emergent
"mirror" interior algebra $\widetilde\M_L$. So a *emph* collapse geometry reproduces the same
split structure as the two-sided eternal black hole of the thermofield double:

$$

Y_{I_0}=Y_{I_1}\vee Y_{I_1}'=\widetilde\M_R\vee\widetilde\M_L .

$$


**The type of the time-band algebra changes qualitatively as the system evolves.** It is type I at early
times, before a horizon exists. Once the system has thermalized, it is type $\mathrm{III}_1$ for a time band of
*emph* width, however large, as long as the band's earliest endpoint stays fixed at some late reference time.
**This change of algebra type, tracked purely from boundary data, can serve as an operator-algebraic
definition of horizon formation and thermalization in real time.** This is the idea behind the "causal depth"
diagnostic that Chapter 8 makes precise.

### The general theorem, and its limits

All the examples above shared a convenient special feature. The boundary region considered was exactly the
intersection of its own causal wedge with the boundary. This fails in general: the causal wedge of a boundary
region can meet the boundary in a strictly larger region. Correspondingly, for a generic boundary region $Y$,
the naive single-trace algebra $Y_Y$ is not a von Neumann algebra on its own. Its double commutant can contain
single-trace operators supported on a region strictly larger than $Y$. This is the same phenomenon that lies
behind the failure of additivity in the superadditivity discussion earlier in this chapter.

A precise theorem, which we quote without proof, says exactly when the naive causal-wedge story works. Write

$$

C_Y\equiv (\widetilde J^+[Y]\cap\widetilde J^-[Y])''

$$

for the generalized causal wedge. Here the double prime on a set of points means its bulk causal completion
(the causal complement of the causal complement). Let $B$ denote the boundary manifold. The theorem states:
$Y_Y$ admits standard causal-wedge reconstruction, and is already a von Neumann algebra, if and only if $Y$ is
**causally convex** and $C_Y\cap B=Y$. In that case $Y_Y=\widetilde\M_{C_Y}$ exactly, with commutant
$Y_Y'=\widetilde\M_{C_Y'}$. If $Y$ fails this condition, $Y_Y''$ instead reconstructs the algebra of the larger
region $Y_{\max}\equiv C_Y\cap B$. This gives a clean, general answer to how much bigger the double commutant can
be.

## Generalized entropy and subregion-subalgebra duality at finite $N$

Everything above was stated strictly at $N=\infty$. This closing section asks what survives at finite but large
$N$. There, a bulk subregion can no longer be sharply defined, because spacetime itself fluctuates. The
section gives a significant piece of indirect evidence that the framework nonetheless extends.

Take the thermofield double above $T_{\text{HP}}$. At finite $N$, $B(\HH_R)$ is an ordinary type I algebra,
with a well-defined entanglement entropy $S_R$. At large $N$, $S_R$ should be given by the **generalized
entropy** of the dual black hole,
\begin{equation}
S_{\text{gen}} \equiv \frac{A_{\text{hor}}}{4G_N(\epsilon)} + S_{\text{bulk}}(\epsilon) .
\label{eq:Sgen_cutoff}
\end{equation}
Here $\epsilon$ is a bulk short-distance cutoff, and $G_N(\epsilon)$ is the corresponding bare Newton constant.

At strict $G_N\to0$, $\widetilde\M_R$ is type $\mathrm{III}_1$. So $S_{\text{bulk}}$ is not even defined until
$\widetilde\M_R$ is regularized into a type I algebra $\widetilde\M_R^\epsilon$ using the cutoff $\epsilon$.
The entropy of that regularized algebra has a leading UV divergence,
$S_{\text{bulk}}(\epsilon)=a\,A_{\text{hor}}/\epsilon^{d-1}+\cdots$, where $a$ is a constant that depends on
the field content and on the regulator. This is the familiar area-law divergence of Chapter 4 again. It is
matched by a divergence in the bare coupling $G_N(\epsilon)$ in the first term. Neither term in
\eqref{eq:Sgen_cutoff} is separately finite as $\epsilon\to0$. But there are strong indications, from
independent gravitational calculations, that the two divergences cancel exactly, leaving a finite
$S_{\text{gen}}=\lim_{\epsilon\to0}\big(\tfrac{A_{\text{hor}}}{4G_N(\epsilon)}+S_{\text{bulk}}(\epsilon)\big)$.

### Worked calculation: cancellation of UV divergences in generalized entropy

To see this cancellation explicitly, consider a free, minimally coupled scalar field in $d+1$ spacetime
dimensions. Close to a non-extremal horizon, the metric looks like Rindler space:

$$

ds^2 = -\kappa^2 \rho^2 dt^2 + d\rho^2 + dx_\perp^2 .

$$

Here $\rho$ is the proper distance to the horizon at $\rho = 0$, and $\kappa = 2\pi/\beta$ is the surface
gravity. The coordinates $x_\perp \in \mathbb{R}^{d-1}$ run along the horizon, whose total area is
$A_{\text{hor}} = \int d^{d-1}x_\perp$.

**Choice of regulator.** The coefficient of a power-law divergence depends on how the theory is
regulated. For example, a "brick wall" at proper distance $\epsilon$ from the horizon gives, for $d=3$, a
thermal entropy $A_{\text{hor}}/(360\pi\epsilon^2)$, while the regulator used below gives
$A_{\text{hor}}/(48\pi\epsilon^2)$. A cancellation can only be tested if both terms of \eqref{eq:Sgen_cutoff}
are regulated in the same way. We use a proper-time (heat-kernel) cutoff throughout: every heat-kernel integral
$\int ds$ is restricted to proper times $s\ge\epsilon^2$. This removes the contribution of distances shorter than
about $\epsilon$.

**Bulk entropy.** The entanglement entropy of the region outside the horizon can be computed by the replica
method. One puts the field on a cone of opening angle $2\pi\alpha$ in the $(t,\rho)$ plane (in Euclidean
signature) and uses $S=(1-\alpha\partial_\alpha)\log Z_\alpha$ at $\alpha=1$. The heat kernel on such a
two-dimensional cone contains an $s$-independent term $(1-\alpha^2)/(12\alpha)$; this is a standard result,
quoted here. The operation $(1-\alpha\partial_\alpha)$ at $\alpha=1$ turns this term into $\tfrac16$. The
transverse directions contribute a factor $A_{\text{hor}}(4\pi s)^{-(d-1)/2}$. So, with
$\log Z_\alpha=\tfrac12\int_{\epsilon^2}^\infty\frac{ds}{s}\Tr\,e^{s\Box}$,
\begin{align}
S_{\text{bulk}}(\epsilon)
&\eqstep{1} \frac12\cdot\frac16\,A_{\text{hor}}\int_{\epsilon^2}^\infty \frac{ds}{s}\,(4\pi s)^{-(d-1)/2}
  + S_{\text{bulk}}^{\text{finite}} \notag\\
&\eqstep{2} \frac{c_{d-1}\, A_{\text{hor}}}{\epsilon^{d-1}} + S_{\text{bulk}}^{\text{finite}},
\qquad c_{d-1} = \frac{1}{6(d-1)(4\pi)^{(d-1)/2}} . \notag
\end{align}
**(1)** the replica formula applied to the cone term of the heat kernel, times the transverse factor; the
remaining, cutoff-independent part is collected in $S_{\text{bulk}}^{\text{finite}}$.\quad
**(2)** $\int_{\epsilon^2}^\infty ds\, s^{-(d+1)/2}=\tfrac{2}{d-1}\,\epsilon^{-(d-1)}$.

For $d=3$ this gives $c_2=1/(48\pi)$. On its own, $S_{\text{bulk}}(\epsilon) \to +\infty$ as $\epsilon \to 0$,
as it must for a type $\mathrm{III}_1$ local algebra.

**Renormalization of Newton's constant.** Quantum fluctuations of the same scalar also correct the
gravitational effective action. In Euclidean signature, integrating out the scalar with the same cutoff gives

$$

I_{\text{eff}}[g] = -\frac{1}{16\pi G_N(\epsilon)}\int d^{d+1}x \sqrt{g}\, R + \frac{1}{2}\Tr\log(-\Box) + \dots

$$

For a minimally coupled scalar, the heat-kernel expansion is
$\Tr\,e^{s\Box}=(4\pi s)^{-(d+1)/2}\int d^{d+1}x\sqrt g\,\big(1+\tfrac{s}{6}R+\mathcal O(s^2)\big)$, and
$\tfrac12\Tr\log(-\Box)=-\tfrac12\int_{\epsilon^2}^\infty\frac{ds}{s}\Tr\,e^{s\Box}$. The term proportional to
$R$ has the same form as the Einstein—Hilbert term, so it shifts the coefficient of $\int\sqrt g\,R$:
\begin{align}
\frac{1}{16\pi G_{N,\text{ren}}}
&\eqstep{1} \frac{1}{16\pi G_N(\epsilon)} + \frac{1}{12}(4\pi)^{-(d+1)/2}
  \int_{\epsilon^2}^\infty ds\, s^{-(d+1)/2} \notag\\
&\eqstep{2} \frac{1}{16\pi G_N(\epsilon)} + \frac{c_{d-1}}{4\pi\,\epsilon^{d-1}} . \notag
\end{align}
**(1)** collect the coefficient of $-\int\sqrt g\,R$: the bare term, plus $\tfrac12\cdot\tfrac16$ times the
proper-time integral from the $R$ term of the heat kernel.\quad
**(2)** do the integral as before, and use the definition of $c_{d-1}$.

Multiplying by $4\pi$ gives

$$

\frac{1}{4G_N(\epsilon)} = \frac{1}{4G_{N,\text{ren}}} - \frac{c_{d-1}}{\epsilon^{d-1}} .

$$

For $d=3$ this is the familiar one-loop result $1/G_{N,\text{ren}}=1/G_N(\epsilon)+1/(12\pi\epsilon^2)$ for a
single scalar. (The coefficients $c_{d-1}$ in the entropy and in the coupling were also checked to agree with
a computer-algebra evaluation of the integrals, for several values of $d$.)

**The cancellation.** Now substitute this coupling into the generalized entropy $S_{\text{gen}}(\epsilon)$:
\begin{align}
S_{\text{gen}}(\epsilon) &\eqstep{1} \frac{A_{\text{hor}}}{4G_N(\epsilon)} + S_{\text{bulk}}(\epsilon) \notag\\
&\eqstep{2} \left(\frac{A_{\text{hor}}}{4G_{N,\text{ren}}} - \frac{c_{d-1}\,A_{\text{hor}}}{\epsilon^{d-1}}\right)
+ \left(\frac{c_{d-1}\,A_{\text{hor}}}{\epsilon^{d-1}} + S_{\text{bulk}}^{\text{finite}}\right) \notag\\
&\eqstep{3} \frac{A_{\text{hor}}}{4G_{N,\text{ren}}} + S_{\text{bulk}}^{\text{finite}} . \notag
\end{align}
**(1)** the definition \eqref{eq:Sgen_cutoff} of generalized entropy with cutoff $\epsilon$.\quad
**(2)** insert the renormalized coupling $1/4G_N(\epsilon)=1/4G_{N,\text{ren}}-c_{d-1}/\epsilon^{d-1}$ in the
first term and the replica result for $S_{\text{bulk}}(\epsilon)$ in the second.\quad
**(3)** the two $c_{d-1}A_{\text{hor}}/\epsilon^{d-1}$ terms have opposite signs and cancel.

The cutoff-dependent term $\epsilon^{-(d-1)}$ cancels exactly. Both coefficients come from the same heat-kernel
coefficient $\tfrac16$, which is why they match. So, at one loop and for this field, the generalized entropy
$S_{\text{gen}}$ does not depend on the cutoff, even though its geometric part and its field-theory part are
separately ill-defined without a regulator. For fields with non-minimal curvature couplings, or for gauge fields,
extra contributions localized on the horizon appear, and the matching needs more care. The crossed product of
Chapter 5 gives an operator-algebraic version of the same idea: it produces a type II algebra whose entropy is
finite and agrees with the generalized entropy up to a state-independent constant.

This finiteness is real, if indirect, evidence for the extension this chapter has been building toward. There
should exist a boundary regularization at finite $N$ that produces a type I algebra $Y_R^\epsilon$ with
$\widetilde\M_R^\epsilon=Y_R^\epsilon$. Nobody currently knows how to write this regularization down explicitly
for a general boundary theory. Now push $\epsilon$ down to the Planck length $\ell_p$. There, the clean separation
between the two terms of \eqref{eq:Sgen_cutoff} breaks down, since $1/G_N\sim1/\epsilon^{d-1}$. The natural
expectation is

$$

\widetilde\M_R^\epsilon = Y_R^\epsilon = B(\HH_R), \qquad \epsilon\sim\ell_p .

$$

The conjecture, then, is the following. The emergent, large-$N$, type $\mathrm{III}_1$ algebra $Y_R$ is the
strict $\epsilon\to0$ endpoint of a continuous family of type I algebras at finite $N$. This family reaches all
the way down to the ordinary finite-$N$ algebra $B(\HH_R)$ itself. In this sense subregion-subalgebra duality,
suitably reinterpreted, would survive at finite $N$, not only as a strict $N=\infty$ statement.

\bigskip
\noindent Subregion-subalgebra duality is now established as a general principle. We have worked it through for
the vacuum sector, the eternal and evaporating black holes, and purely algebraic bulk diamonds. Chapter 8 turns
to a further consequence: reading bulk *emph* directly off the type and commutant
structure of boundary algebras. This includes the formation of a horizon and the connectivity of spacetime, and
no bulk metric is assumed anywhere in the argument.



---

# Emergence of bulk geometric concepts

Chapter 7 established that a bulk region *emph* a boundary algebra. This chapter pushes that identification
to its limit: causal structure, the formation of a horizon, and even whether two boundary theories are joined
by a wormhole at all, can each be read directly off the type and commutant structure of boundary algebras —
with no bulk metric assumed anywhere in the argument. This closes the two puzzles raised in Chapter 6
(the factorization puzzle was already resolved there; the meeting-behind-the-horizon puzzle is resolved here,
in the section on Kruskal-like time).

## Algebraic characterization of bulk causal structure

### Why boundary commutants can encode more than boundary causality

Boundary operators separated in a spacelike way automatically commute — ordinary microcausality. But
*emph*-separated boundary operators are not required to commute at all; whether they do depends on
the specific representation, which is fixed by the state's two-point functions. This freedom is not a bug —
it is exactly the room needed for boundary commutant structure to encode something richer than boundary
causality alone: by subregion-subalgebra duality, it encodes bulk causal structure, in one higher dimension.

### The causal depth parameter

Recall from Chapter 6 that in empty AdS, a boundary time band $I_w$ generates the entire algebra,
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
geometry, $T(t)$ is expected to stay finite for all time. For a single-sided eternal black hole
(Figure~\ref{fig:causal_depth}(b)), by contrast, $Y_{I_w}$ has a *emph* commutant for *emph* finite $w$ — no matter
how wide a time band you take, you can never quite reach the full exterior algebra (only in the strict
$w\to\infty$ limit does the commutant become trivial) — so $T(t)=\infty$, for all $t$: **a purely
boundary-intrinsic signature of a horizon, requiring no bulk metric to state.** For a black hole formed by
collapse (the single-sided collapse example of Chapter 7), $T(t)$ starts finite and grows monotonically, diverging only as $t\to\infty$ — the
boundary-side signature of a horizon actually *emph*, in real time, rather than always having been
there.

A two-sided version, $T_R(t)$, is defined the same way but using the *emph* commutant of $Y_{I_w}$
within $Y_R$ (the right boundary's own single-trace algebra) — for the thermofield double below
$T_{\text{HP}}$, this reduces to ordinary empty AdS's $\pi R$; above $T_{\text{HP}}$, it diverges for all
time, exactly reproducing the bifurcating-horizon diagnostic of Chapter 7, the statement that
$(Y_{I_w}^{(R)})'\cap Y_R$ is nontrivial for every $w$, in this new language.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.90\textwidth]{figs/fig_causal_depth.pdf}
\caption{(a) Empty AdS drawn as a strip: the vertical edges are the boundary and the dotted line is the center $r=0$. Light rays (blue lines) from the ends of a boundary time band $I_w$ of width $w=\pi R$ meet at $r=0$, so the region they enclose (shaded) contains the whole $t=0$ slice (dashed), giving causal depth $T=\pi R$. (b) Penrose diagram of the eternal black hole: for a band $I_w$ of any finite width on the right boundary, the region its light rays enclose (shaded) stops short of the horizons (dashed red) and their crossing point, so it never covers the whole exterior $t=0$ slice and $T=\infty$.}
\label{fig:causal_depth}
\end{figure}

### $T$ as a measure of lost determinism

$T$ has a second meaning, and it explains why the whole construction is possible. At finite $N$, knowing the operator algebra on a single Cauchy
slice determines the whole theory (ordinary causal time evolution, the time-slice axiom of Chapter 4). In
the strict large-$N$ limit, this stops being true — there are no equations of motion relating single-trace
operators at different times (Chapter 6) — but the theory isn't completely disconnected across time either:
correlations (encoded in two-point functions) still relate a time band's algebra to the rest of the theory,
just not through equations of motion. $T$ is exactly the minimal width of a band whose algebra is
*emph*, via these correlations rather than dynamics, to recover the whole system. Read this way,
**$T=0$ is full determinism (an honest equation of motion); $T$ finite is a partial, quantifiable loss of
determinism; $T=\infty$, as in a black hole, is a complete loss of determinism — no finite window of boundary
time, however wide, is ever enough.** The emergence of the bulk radial direction is, in this precise sense,
tied to the boundary theory progressively losing determinism as $N\to\infty$.

The precise version of this statement relates $T$ to the *emph* $\rho(\omega)$, the
Fourier transform of the commutator $\braket{\Psi|[O(t),O(0)]|\Psi}$. It connects to an old question of
Kolmogorov's: how long must you watch a fluctuating signal before you can predict all of its future? The
general theorem belongs to harmonic analysis and is quoted rather than proved here. What can be done with
ordinary tools is to see, in two contrasting examples, why a discrete spectrum gives a finite $T$ and a
continuous spectrum does not.

### Worked calculation: spectral functions and the divergence of causal depth

The spectral function is

$$

\rho(\omega) \equiv \int_{-\infty}^\infty dt\, e^{i\omega t}\, \braket{\Psi|\big[O(t),\, O(0)\big]|\Psi} .

$$

It records which frequencies the operator $O$ can put into the system, and with what weight.


1. **Vacuum state $\ket\Omega$ (empty AdS).**
In global $\text{AdS}_{d+1}$ of radius $R$, the modes created by $O$ have the discrete energies
$\omega_n = (\Delta + 2n)/R$, $n=0,1,2,\dots$, exactly like the evenly spaced levels of a harmonic oscillator.
The Wightman function is a sum over these levels,

$$

\braket{\Omega|O(t)O(0)|\Omega} = \sum_{n=0}^\infty c_n\, e^{-i\omega_n t}, \qquad c_n\ge0 ,

$$

and so
\begin{align}
\rho(\omega)
&\eqstep{1} \int dt\, e^{i\omega t} \sum_{n} c_n \big(e^{-i\omega_n t} - e^{i\omega_n t}\big) \notag\\
&\eqstep{2} 2\pi \sum_{n} c_n \Big(\delta(\omega - \omega_n) - \delta(\omega + \omega_n)\Big) .
\label{eq:rho_vacuum_AdS}
\end{align}
**(1)** the commutator is $\braket{O(t)O(0)}-\braket{O(0)O(t)}$, and the second term is the complex
conjugate of the first.\quad
**(2)** $\int dt\, e^{i(\omega-\omega_n)t}=2\pi\,\delta(\omega-\omega_n)$.

The spectrum is a comb of spikes with fixed spacing $2/R$. Now ask: which time bands are wide enough to
separate the modes from one another? A smeared operator $\int dt\, f(t)\,O(t)$ with $f$ supported in a band of
width $w$ picks up mode $n$ with weight $\tilde f(\omega_n)$. On a window of width exactly

$$

w = \frac{2\pi}{\text{spacing}} = \frac{2\pi}{2/R} = \pi R ,

$$

the functions $e^{-i\omega_n t}$ are mutually orthogonal, just as $e^{int}$ are orthogonal on
$[0,2\pi]$ in an ordinary Fourier series. So by choosing $f$ to be one of these exponentials one can switch on
a single mode and nothing else. Every mode operator is then in the band algebra, and the band algebra is the
whole algebra of the vacuum sector. On a shorter window the exponentials overlap and cannot be separated. A
direct numerical check with the first 40 modes confirms this: the overlap (Gram) matrix of the
$e^{-i\omega_n t}$ is exactly the identity on a window of width $\pi R$, while on a window of width $0.9\,\pi R$
its smallest eigenvalue has already dropped to about $6\times10^{-5}$, and at $0.6\,\pi R$ it is zero to
machine precision. The threshold width is $T=\pi R$, exactly the light-crossing value found geometrically.
2. **Thermal state $\ket{\Psi_\beta**$ (black hole).}
Take the thermal two-point function of an operator of dimension $\Delta$ in a one-dimensional thermal
system at inverse temperature $\beta$,

$$

\braket{O(t)O(0)}_\beta = \left(\frac{\pi}{i\beta \sinh\big(\frac{\pi}{\beta}(t - i\epsilon)\big)}\right)^{2\Delta} .

$$

Its Fourier transform and the resulting spectral function are
\begin{align}
G_\beta(\omega) &\equiv \int dt\, e^{i\omega t}\braket{O(t)O(0)}_\beta
= \frac{1}{\Gamma(2\Delta)}\left(\frac{2\pi}{\beta}\right)^{2\Delta-1} e^{\beta\omega/2}
\left|\Gamma\!\left(\Delta+\frac{i\beta\omega}{2\pi}\right)\right|^2 , \notag\\
\rho(\omega) &\eqstep{1} G_\beta(\omega)\big(1-e^{-\beta\omega}\big)
\eqstep{2} \frac{2}{\Gamma(2\Delta)}\left(\frac{2\pi}{\beta}\right)^{2\Delta-1}
\sinh\!\left(\frac{\beta\omega}{2}\right)\left|\Gamma\!\left(\Delta+\frac{i\beta\omega}{2\pi}\right)\right|^2 .
\label{eq:rho_thermal}
\end{align}
**(1)** the KMS condition of Chapter 4: in a thermal state $\braket{O(0)O(t)}$ transforms to
$e^{-\beta\omega}G_\beta(\omega)$.\quad
**(2)** $e^{\beta\omega/2}(1-e^{-\beta\omega})=2\sinh(\beta\omega/2)$.

The formula for $G_\beta(\omega)$ was checked by numerical integration for $\Delta=1,\ 1.5,\ 2.3$ at several
frequencies, agreeing to all twenty digits computed. For $\Delta=1$ it reduces to
$G_\beta(\omega)=2\pi\omega/(1-e^{-\beta\omega})$, which is $2\pi\omega$ times the Bose—Einstein factor, as it
should be for a thermal gas of bosons, and then $\rho(\omega)=2\pi\omega$ exactly.

The decisive difference from the vacuum is the *emph* of $\rho$. At high frequency, Stirling's formula
gives $\rho(\omega)\to\frac{2\pi}{\Gamma(2\Delta)}|\omega|^{2\Delta-1}\operatorname{sgn}\omega$, the same power
law as in the vacuum (the ultraviolet does not know about the temperature; numerically the ratio to this
power law is $1.0247$ at $\beta\omega=20$ and $1.0001$ at $\beta\omega=400$). But unlike the vacuum comb,
$\rho(\omega)$ is a smooth function that is nonzero at *emph* real frequency. There is no spacing between
levels. Using the same reasoning as in the vacuum case, separating frequencies spaced by $\delta\omega$ needs a
window of width $2\pi/\delta\omega$, and a continuous spectrum has $\delta\omega\to0$. No finite band can
single out the individual modes, and the causal depth is $T=\infty$.


The vacuum argument is complete as it stands. The thermal argument shows why no finite band could work by
mode separation. The stronger statement, that the commutant of every finite band is genuinely nontrivial, is
the harmonic-analysis theorem quoted above. Physically, the continuous spectrum is the boundary imprint of the
horizon: a black hole absorbs perturbations at every frequency, and that damping destroys the sharp
recurrences that let a finite window of the vacuum reconstruct everything.

## Emergence of Kruskal-like time, and resolving the meeting-behind-the-horizon puzzle

### Two kinds of bulk time

The eternal AdS black hole geometry has two qualitatively different notions of time. **Schwarzschild
time** is an honest isometry — it maps the $R$ (or $L$) exterior region to itself, never leaving it. This is
exactly the boundary time of the thermofield double: Chapter 6 already established
Schwarzschild time as the modular time of $\widetilde\M_R=Y_R$. **Kruskal time**, by contrast, is not an
isometry at all. It is the time that actually carries a point from the exterior $R$ region across the horizon
into the interior $F$ (future) or $P$ (past) regions (see the Penrose diagram, Figure~\ref{fig:penrose}, in
Chapter 6). The Kruskal null coordinates $U,V$ are exactly the light-cone coordinates $x^\mp$ of the
Rindler-wedge discussion in Chapter 4, since near the horizon the geometry looks locally like flat Rindler
space. Schwarzschild time has an obvious boundary home
(it's just ordinary boundary time evolution); Kruskal time, at first glance, has no boundary home at all —
boundary time simply runs to $\pm\infty$ as you approach the horizon and has nothing left to say about what
happens beyond it.

### Kruskal time from half-sided modular inclusion

Here the half-sided modular inclusion machinery of Chapter 4, introduced there as a purely algebraic
curiosity and worked out on an abstract Rindler-wedge light-cone example, turns out to be *emph* the
tool needed to manufacture Kruskal time out of nothing but boundary data. Take $\M=Y_R$ (the
right boundary's full single-trace algebra, cyclic-separating for $\ket{\Psi_\beta}$), and $\N=Y_-$, the
subalgebra generated by single-trace operators supported on the semi-infinite band $t<0$. By the
time-band duality of Chapter 7, $Y_-$ is dual to a specific bulk wedge region $W_-$ (the part of the right
exterior that can send and receive signals from the half-band $t<0$), itself type
$\mathrm{III}_1$, with $\ket{\Psi_\beta}$ cyclic and separating for it too. Because $Y_R$'s modular flow is
literally boundary time translation, $Y_-$ automatically satisfies exactly the half-sided modular inclusion
condition of Chapter 4. So that machinery applies immediately, producing a genuine positive generator
\begin{equation}
G_+\equiv\tfrac1{2\pi}(K_{Y_R}-K_{Y_-}) ,
\label{eq:Gplus}
\end{equation}
generating a brand-new time flow on $Y_R=\widetilde\M_R$
that leaves $\ket{\Psi_\beta}$ fixed. Repeating with $\N=Y_+$ (the band $t>0$) gives a second, independent
generator $G_-$.

Near the horizon, where, exactly as in the abstract example of Chapter 4, the geometry reduces to flat Rindler
space, these two generators act exactly as null translations in the two light-cone directions,

$$

e^{iG_+s}\phi(X)e^{-iG_+s}=\phi(X_s),\ \ X_s=(U+s,V,x_\perp)\ \ (V\ll1),

$$


$$

e^{iG_-s}\phi(X)e^{-iG_-s}=\phi(X_s),\ \ X_s=(U,V+s,x_\perp)\ \ (U\ll1)

$$

**$G_\pm$, built purely from boundary modular data, literally translate a bulk operator
across the horizon**, and the combinations $p\equiv G_—G_+$, $h\equiv G_++G_-$ generate ordinary
spatial and genuine Kruskal-time translation respectively, right in the near-horizon region.

**This resolves the meeting-behind-the-horizon puzzle of Chapter 6 directly**: the boundary
Hamiltonian $H=H_R+H_L$ genuinely has no term coupling $R$ to $L$ — and yet the entanglement structure of
$\ket{\Psi_\beta}$ itself, purely through the algebraic relationship between $Y_R$ and its subalgebras
$Y_\pm$, generates emergent operators $G_\pm$ that couple the two sides and translate operators from $R$ and
$L$ into causal contact behind the horizon. No interaction term was ever needed in $H$; the coupling is
already latent in how entangled the state is, made manifest only once you build the right algebraic objects
from it.

For the BTZ black hole the full computation reproduces the *emph* causal structure of the black hole
geometry, not just a qualitative picture. Flow an operator, $\Phi(X,s)\equiv e^{iG_+s}\phi(X)e^{-iG_+s}$,
starting at $X=(U_0,V_0,x_\perp)$. For $s$ below the threshold $s_0=-U_0$, $\Phi(X;s)$ stays entirely within
$\widetilde\M_R$. Once $s$ passes $s_0$, operators from $\widetilde\M_L$ suddenly appear in $\Phi(X;s)$: the
flowed point has crossed the horizon. Commutators tell the same story. For two points $X_1\in R$ and
$X_2\in L$, $[\Phi(X_1,s),\phi(X_2)]$ is exactly zero until $s$ passes the threshold $s_{12}=U_2-U_1$, and
nonzero after it. **Sharp causal structure comes out of an evolution built entirely from algebraic
data, with no bulk light cone put in by hand.** The near-horizon part of this computation can be done
explicitly, and that is the content of the next derivation.

### Worked derivation: Kruskal coordinates and horizon crossing in BTZ

The non-rotating BTZ black hole in $\text{AdS}_3$ has metric

$$

ds^2 = -\frac{r^2 - r_+^2}{R^2}\, dt^2 + \frac{R^2}{r^2 - r_+^2}\, dr^2 + \frac{r^2}{R^2}\, d\phi^2 .

$$

The surface gravity at the horizon $r = r_+$ is $\kappa = r_+/R^2$, and the Hawking temperature is
$1/\beta=\kappa/2\pi$. The tortoise coordinate is

$$

r^*(r) \equiv \int \frac{R^2}{r^2 - r_+^2}\, dr = \frac{1}{2\kappa} \log\left(\frac{r - r_+}{r + r_+}\right)
\in (-\infty, 0) ,

$$

and in the right exterior $R$ ($r > r_+$) the Kruskal null coordinates are

$$

U \equiv -e^{-\kappa(t - r^*)}, \qquad V \equiv e^{\kappa(t + r^*)} .

$$

In region $R$ one has $U<0$ and $V>0$. As $r\to r_+$, $r^*\to-\infty$ and $UV=-e^{2\kappa r^*}\to0$. The
future horizon $\mathcal H^+$ is the null surface $U=0$, $V>0$, and the black hole interior $F$ is the region
$U>0$, $V>0$.

First, the modular flow of $Y_R$ in these coordinates. Shifting Schwarzschild time, $t\to t+a$, gives
$U\to e^{-\kappa a}U$ and $V\to e^{\kappa a}V$, so
\begin{align}
K_{Y_R} \eqstep{1} \beta H_R \eqstep{2} \beta\,\kappa\,(V\partial_V - U\partial_U) \eqstep{3}
2\pi\,(V\partial_V - U\partial_U) .
\label{eq:BTZ_boost}
\end{align}
**(1)** Chapter 6: the modular Hamiltonian of $Y_R$ in the thermofield double is $\beta$ times the
right boundary Hamiltonian.\quad
**(2)** $\partial_t=\kappa(V\partial_V-U\partial_U)$, read off from the transformation of $U,V$ under
$t\to t+a$ (checked by finite differences).\quad
**(3)** $\beta=2\pi/\kappa$.

The modular flow is a Lorentz boost in the $(U,V)$ plane: one unit of modular time sends $U\to e^{-2\pi s}U$,
$V\to e^{2\pi s}V$, and it leaves the horizon $U=0$ in place. This is exactly the Rindler boost of Chapter 4.

The half-sided modular generator $G_+=\frac{1}{2\pi}(K_{Y_R}-K_{Y_-})$ acts differently. Near the horizon it
generates a rigid translation along the null direction $U$, normalised so that

$$

\Phi(s) \equiv e^{i G_+ s}\, \phi(U_0, V_0)\, e^{-i G_+ s} = \phi(U_0 + s,\, V_0) .

$$

Follow the coordinate $U(s) = U_0 + s$ of a point that starts in the right exterior, $U_0<0$:

1. For $0 \le s < -U_0$: $U(s) < 0$. The point is still in the right exterior, and
$\Phi(s) \in \widetilde\M_R = Y_R$.
2. At $s = s_0 \equiv -U_0$: $U(s_0) = 0$. The point sits on the future horizon $\mathcal{H}^+$.
3. For $s > -U_0$: $U(s) > 0$ and $V_0 > 0$, so the point is inside the black hole, in region $F$.

Now bring in an operator $\phi(X_L)$ at a point $X_L = (U_L, V_L)$ of the left exterior, where $U_L > 0$ and
$V_L < 0$. Near the horizon the metric is $ds^2\propto-dU\,dV$, so two points are causally connected exactly
when $\Delta U\,\Delta V\ge0$. Here $\Delta V=V_0-V_L>0$, so the condition is $\Delta U=U_0+s-U_L\ge0$. By
microcausality the commutator $[\Phi(s), \phi(X_L)]$ vanishes for $s<U_L-U_0$ and is generically nonzero once
$s\ge U_L-U_0$. This is the threshold $s_{12}$ quoted above, now derived from the geometry.

Near the horizon, then, the generator $G_+$, built from boundary modular data alone, carries a right-exterior
operator into the interior, where it can meet an operator sent in from the left. That is the resolution of
the meeting-behind-the-horizon puzzle, seen in coordinates.

In a suitable large-conformal-weight limit this flow even becomes a genuinely *emph* bulk
transformation, with trajectories running smoothly into the black hole singularity as $s$ approaches a further
critical value. Together with the boost $K$, the generators $G_\pm$ close into an $SL(2,\mathbb R)$ algebra,
the two-dimensional conformal structure already met abstractly in Chapter 4. These two statements are quoted
without proof. A consistency check is immediate, however: below $T_{\text{HP}}$, $Y_R$ is type I, and
half-sided modular inclusion cannot occur for a type I algebra (Chapter 4 showed that it requires type
$\mathrm{III}_1$). This matches the bulk fact that the two boundaries are then disconnected, with no horizon
and nothing to cross.

## Emergent spacetime connectivity: algebraic ER$=$EPR

### Why the naive slogan needs fixing

The naive ER$=$EPR slogan says that any two entangled gravitational systems are connected by some kind of
Einstein—Rosen bridge. Examined carefully, it runs into two problems. **First**: below $T_{\text{HP}}$ in
the thermofield double, $R$ and $L$ are certainly entangled (by an amount of order $G_N^0$), but the bulk dual
is two entirely *emph* copies of AdS (Chapter 6). So "entangled $\Rightarrow$ connected" is
already false as stated, unless one calls this a "quantum wormhole" without any independent definition of
what that means. **Second**, and sharper: even requiring a large, $O(1/G_N)$ amount of entanglement does
not fix it. Consider an evaporating black hole at a time $t<t_P$ before the Page time. The black hole and the
radiation it has already emitted share $O(1/G_N)$ entanglement, yet the two systems are *emph*. The amount of entanglement, at any threshold, is not the right diagnostic.

### The fix: entanglement *emph*, not entanglement *emph*

Two facts established earlier point to the right diagnostic. Chapter 6 showed that a classical
Einstein—Rosen bridge corresponds to $Y_R$ and $Y_L$ both being type $\mathrm{III}_1$. The previous section
showed that type $\mathrm{III}_1$ is what makes half-sided modular inclusion, and hence a causal connection
through the horizon, possible at all. **Algebraic ER$=$EPR** turns this observation into a three-way
classification. Take two entangled systems $R_1$ and $R_2$ in a pure semiclassical state, with bulk dual
$W_{R_1R_2}$ (every part of which touches some boundary) and algebras $\M_{R_1}$, $\M_{R_2}$. Then:

- $W_{R_1R_2}$ is **disconnected** $\iff$ $\M_{R_1}$ and $\M_{R_2}$ are both type I.
- $W_{R_1R_2}$ has a **classical** wormhole $\iff$ $\M_{R_1}$ and $\M_{R_2}$ are both type
$\mathrm{III}_1$ *emph* $W_{R_1R_2}$ is classical.
- $W_{R_1R_2}$ has a **quantum** wormhole $\iff$ $W_{R_1R_2}$ is **quantum volatile** and
$\M_{R_1}$, $\M_{R_2}$ are not type I.

A bulk spacetime is **quantum volatile** when it fails to become classical in the $G_N\to0$ limit even
though that limit is being taken. Concretely, either diffeomorphism-invariant fluctuations do not die away as
$G_N\to0$, or some geometric quantity (a length, an area, a volume) grows like $G_N^{-a}$ instead of staying
finite. The standard example is the evaporating black hole before the Page time. The interior connecting the
black hole to its radiation has a *emph* of order $1/G_N$, which diverges as $G_N\to0$. That is
why it counts as quantum volatile rather than as an ordinary classical wormhole, even though the entanglement
supporting it is large.


> [!NOTE] **Physics Connection: why "structure," not "amount," already matters in ordinary quantum information**
> The classification uses the *emph* of $\M_{R_1}$ and $\M_{R_2}$, not the amount of entanglement. The same
> distinction already appears for three qubits. Compare the GHZ state
> $\ket{\rm GHZ}=\tfrac1{\sqrt2}(\ket{000}+\ket{111})$ with the W state
> $\ket{\rm W}=\tfrac1{\sqrt3}(\ket{001}+\ket{010}+\ket{100})$. Trace out qubit $C$ from each. In the basis
> $\ket{00},\ket{01},\ket{10},\ket{11}$ the remaining two-qubit states are
> 
$$

> \rho^{\rm GHZ}_{AB} = \begin{pmatrix}\tfrac12&0&0&0\\0&0&0&0\\0&0&0&0\\0&0&0&\tfrac12\end{pmatrix}, \qquad
> \rho^{\rm W}_{AB} = \begin{pmatrix}\tfrac13&0&0&0\\0&\tfrac13&\tfrac13&0\\0&\tfrac13&\tfrac13&0\\0&0&0&0\end{pmatrix} .
> 
$$

> Apply the Peres—Horodecki test: transpose the $B$ index and look for a negative eigenvalue. For
> $\rho^{\rm GHZ}_{AB}$ the eigenvalues after partial transpose are $\{0,0,\tfrac12,\tfrac12\}$, all non-negative,
> so **no entanglement is left** between $A$ and $B$. For $\rho^{\rm W}_{AB}$ they are
> $\{\tfrac{1-\sqrt5}{6},\tfrac13,\tfrac13,\tfrac{1+\sqrt5}{6}\}\approx\{-0.206,\,0.333,\,0.333,\,0.539\}$. One is
> negative, so **$A$ and $B$ are still entangled** after $C$ is gone.
> 
> By the simplest measure, GHZ is the *emph* entangled of the two. The entropy of one qubit against the
> other two is $1$ bit for GHZ and $0.918$ bits for W. Yet removing a qubit destroys all remaining entanglement
> in GHZ and not in W. The difference lies in how the entanglement is arranged. GHZ puts all of its correlation
> into a three-way correlation with nothing left for any pair, while W spreads it out so that every pair keeps
> some. Algebraic ER$=$EPR applies the same idea to gravitational systems. Type I, type $\mathrm{III}_1$, and
> quantum volatile describe how entanglement is organised between $\M_{R_1}$ and $\M_{R_2}$. Two systems with
> comparable entanglement entropy can land in different classes, just as $\rho^{\rm GHZ}_{AB}$ and
> $\rho^{\rm W}_{AB}$ do.


This resolves both problems. Below $T_{\text{HP}}$, both boundary algebras are type I, and algebraic
ER$=$EPR correctly reports *emph* wormhole of either kind. For the evaporating black hole before the Page
time, the entanglement wedge connecting the black hole and the radiation is quantum volatile (its interior
length is of order $1/G_N$), so the connection is a *emph* wormhole rather than either "no wormhole"
or an ordinary classical one. After the Page time the entanglement wedge becomes classical, and it connects to
the radiation through a classical wormhole anchored at the quantum extremal surface. A refinement of the causal
depth of the first section, the *emph* depth, built from modular rather than ordinary time bands,
sharpens the distinction further. The boundary algebra is type $\mathrm{III}_1$ in both regimes, but the
modular depth is finite before the Page time and infinite after it.

The whole classification assumes the strict $\alpha'\to0$ (large 't~Hooft coupling) limit, in which the bulk
has ordinary geometry. In the stringy regime, taken up next, type $\mathrm{III}_1$ alone is no longer enough
to guarantee connectivity.

## Stringy geometry and stringy black holes

Everything so far assumed the bulk is described by ordinary Einstein gravity coupled to matter, which is valid
in the double limit $N\to\infty$, $\lambda\to\infty$ ('t~Hooft coupling large, equivalently $\alpha'\to0$). At
finite $\lambda$, that is, at finite string tension, an infinite tower of massive string modes appears. The
notion of a sharp bulk causal region, built throughout this chapter from field-theory causal wedges and RT
surfaces, becomes delicate, because strings are extended objects and interact non-locally on the string scale.
The dictionary between bulk causal structure and boundary commutants must therefore be modified.

Boundary operator algebras can still be used in this regime. They still probe causal structure, and they still
define an analogue of a horizon. The half-sided modular inclusion mechanism behind Kruskal time also carries
over to a stringy black hole. The main new lesson is negative: once stringy effects are included, type
$\mathrm{III}_1$ structure alone no longer guarantees connectivity, and the algebraic ER$=$EPR classification
needs an extra ingredient. This part of the subject is still being developed, and the details are not needed
for anything that follows. The central chain of ideas, from algebra to type of entanglement to emergent
spacetime, stands without it.

\bigskip
\noindent Bulk causal structure, horizon formation, and spacetime connectivity have now all been read directly
off boundary algebra data. Chapter 9 turns to a different kind of question. Rather than analysing an existing
holographic theory, it builds simple, fully solvable *emph* of quantum gravity directly out of
operator algebras. The crossed product of Chapter 5 returns there, no longer as an abstract construction but
as the mechanism by which an observer's own clock produces the Bekenstein—Hawking area term and the
de~Sitter entropy.



---

# Algebraic approaches to  quantum-gravity regimes

Chapters~6—8 analyzed an existing structure — AdS/CFT — using the machinery built in Chapters~2—5. This
chapter does something different and, in a sense, more ambitious: it builds simple, completely solvable
*emph* of quantum gravity directly out of operator algebras, with the crossed product of Chapter~5
appearing not as an abstract mathematical device but as the literal, physical mechanism that turns a quantum
field theory's type $\mathrm{III}_1$ algebra into the finite, well-defined entropy of a black hole or of
de~Sitter space. This is the payoff the whole crossed-product construction was built for.

## A model of gravitational dressing from observers

### Setting up the constraint

Start with an ordinary quantum field theory on Hilbert space $\HH_Q$, and let $\M$ be the algebra of some
region, $\M'$ its commutant, both type $\mathrm{III}_1$, with a cyclic-separating reference $\ket\Psi$ and
modular Hamiltonian $K$ generating the usual internal time flow on $\M$ and $\M'$ (Chapter~4).

Now attach two observers, $R$ and $L$, each with their own Hamiltonian $\hat q_R,\hat q_L$ and conjugate
clock-reading operators $\hat p_R,\hat p_L$ (with clock-reading eigenstates $\ket\tau_R,\ket\tau_L$). Demand
the *emph* system — field theory plus both observers — be invariant under translations generated by

$$

H = K + \hat q_R - \hat q_L .

$$

This is a toy **Hamiltonian constraint**, built to mimic the way general relativity's own Hamiltonian
constraint works: there is no external clock, only relative readings between subsystems, exactly the way
diffeomorphism invariance in gravity means only relational data (not absolute time) is physical.

The naive way to build gauge-invariant states — projecting with $\Pi\equiv\int_{-\infty}^\infty dt\,e^{-iHt}$
— fails, because $\Pi^2\propto\Pi\int dt$ diverges: the projector is not normalizable, the same obstruction met
(and resolved) in Chapter~5. The fix is to define physical states as *emph* $[\psi]$ under
$\Pi\ket{\psi_1}=\Pi\ket{\psi_2}$ (states related by the gauge flow $e^{iHt}$ count as the same physical
state), with inner product $(\psi|\phi)\equiv\braket{\psi|\Pi|\phi}$, which depends only on the equivalence
classes, as can be checked directly.

### Gauge-fixing, and two equivalent presentations

Any state can be gauge-fixed by pinning the $L$-observer's clock to a specific reading $\tau$: expanding a
general state in the joint clock-reading$\times$field basis, one shows explicitly that $\ket\psi\sim
\ket\tau_L\otimes\ket{\psi_\tau}_{RQ}$ for $\ket{\psi_\tau}_{RQ}\equiv{}_L\!\bra\tau\Pi\ket\psi$, and this map
from the physical (gauge-invariant) Hilbert space to $\HH_R\otimes\HH_Q$ is an honest isometry, checked
directly from the definitions. In this gauge, $\hat q_L$ is no longer an independent dynamical variable — the
constraint $H=0$ solves it as a composite operator, $\hat q_L=\hat q_R+K$. Symmetrically, gauge-fixing the
$R$-observer's clock instead gives $\hat q_R=\hat q_L-K$. These are two different, but physically equivalent,
ways of describing exactly the same gauge-invariant physics.

### Dressed operators, and the crossed product falls out automatically

A gauge-invariant (physical) operator must commute with $H$. Starting from $A\in\M$ (or $A'\in\M'$), the
gauge-invariant, "dressed" version — literally the operator $A$, tagged with the $R$-observer's clock
reading $\tau$ — is built by integrating over the gauge group,

$$

\widehat A_R(\tau) \equiv \int dt\,e^{iHt}\big(\ket\tau\!\bra\tau_R\otimes A\big)e^{-iHt}
= e^{iK\hat p_R}A(-\tau)e^{-iK\hat p_R} ,

$$

with the mirror construction $\widehat A'_L(\tau)$ for $A'\in\M'$, and by construction
$[\widehat A_R(\tau),H]=0$. The clock reading $\tau$ appearing in $\widehat A_R(\tau)$ is now a *emph*, not a classical coordinate: in a generic state (not an eigenstate of $\hat p_R$), it genuinely
fluctuates. **The dressed operators live in a quantum spacetime.** The algebra generated by all such
dressed operators, together with clock translations, is

$$

\widehat\M \equiv \big\{\widehat A_R = e^{iK\hat p_R}Ae^{-iK\hat p_R},\ e^{i\hat q_Rs}\ \big|\ A\in\M,\
s\in\mathbb R\big\}'' ,

$$

and this is, symbol for symbol, exactly the crossed-product algebra $\widehat\M$ constructed abstractly in
Chapter~5, with the clock $\hat q$ there identified with the $R$-observer's own Hamiltonian $\hat q_R$ here.

### Worked derivation: solving the relational constraint and dressing operators

To see this constraint solving and dressing algebraically, work out the quantum mechanics of the relational
Hamiltonian constraint:

$$

H = K + \hat q_R - \hat q_L = 0 .

$$

Let the observers' clock variables satisfy the canonical commutation relations $[\hat p_L, \hat q_L] = -i$ and
$[\hat p_R, \hat q_R] = -i$. In the clock-reading representation $\ket{\tau_L}$, the Hamiltonian operator acts
as a differential operator $\hat q_L = i \frac{\partial}{\partial \tau_L}$.

A physical (gauge-invariant) wavefunction $\ket{\Psi_{\text{phys}}}$ must satisfy the Wheeler—DeWitt-like
equation:

$$

H \ket{\Psi_{\text{phys}}} = 0 \implies \left(K + \hat q_R - i \frac{\partial}{\partial \tau_L}\right)
\psi(\tau_L) = 0 .

$$

Integrating this first-order differential equation immediately yields:

$$

\psi(\tau_L) = e^{-i(K + \hat q_R)\tau_L} \psi(0) .

$$

Thus the entire $\tau_L$-dependence is completely determined by the data on the initial slice $\tau_L = 0$.
Choosing the gauge $\tau_L = 0$ provides a faithful, isometric embedding of the physical Hilbert space into
$\HH_R \otimes \HH_Q$:

$$

\ket{\Psi_{\text{phys}}} \longleftrightarrow \ket{\psi(0)}_{RQ} \in \HH_R \otimes \HH_Q .

$$

In this gauge, the $L$-clock momentum is eliminated via the constraint $\hat q_L = K + \hat q_R$.

Now consider dressing an operator $A \in \M$ to make it gauge-invariant under the flow $e^{i H t}$. The
group-averaged operator is:

$$

\widehat A_R(\tau) \equiv \int_{-\infty}^\infty dt\, e^{i H t} \big(\ket\tau\!\bra\tau_R \otimes A\big)
e^{-i H t} .

$$

Evaluate it on the physical gauge slice $\tau_L = 0$:
\begin{align}
\widehat A_R(\tau)
&\eqstep{1} \int_{-\infty}^\infty dt\, e^{i(K + \hat q_R)t} \big(\ket\tau\!\bra\tau_R \otimes A\big)
e^{-i(K + \hat q_R)t} \notag\\
&\eqstep{2} \int_{-\infty}^\infty dt\, \big(\ket{\tau + t}\!\bra{\tau + t}_R\big) \otimes \big(e^{i K t} A
e^{-i K t}\big) . \notag
\end{align}
**(1)** on the slice $\tau_L=0$ the constraint replaces $\hat q_L$ by $K+\hat q_R$, so
$e^{iHt}=e^{i(K+\hat q_R)t}e^{-i\hat q_Lt}$ reduces to $e^{i(K+\hat q_R)t}$ acting on $\HH_R\otimes\HH_Q$.\quad
**(2)** $K$ and $\hat q_R$ act on different factors and commute, so the exponential splits;
$e^{i\hat q_Rt}$ shifts the clock state, $e^{i\hat q_Rt}\ket\tau_R=\ket{\tau+t}_R$, while $e^{iKt}$ flows
$A$ in modular time.

Since the clock momentum operator $\hat p_R$ is diagonal in the clock basis ($\hat p_R \ket\tau_R = \tau
\ket\tau_R$), the $t$-integral collapses once the clock reading is identified with $\hat p_R$: setting
$t = \hat p_R - \tau$ inside the integral gives the closed form

$$

\widehat A_R(\tau) = e^{i K \hat p_R} A(-\tau) e^{-i K \hat p_R} .

$$

Check directly that this dressed operator commutes with the total generator $K + \hat q_R$:
\begin{align}
\big[K + \hat q_R,\, \widehat A_R(\tau)\big]
&\eqstep{3} \big[K,\, \widehat A_R(\tau)\big] + \big[\hat q_R,\, e^{i K \hat p_R} A(-\tau) e^{-i K
\hat p_R}\big] \notag\\
&\eqstep{4} i \frac{\partial}{\partial \tau}\widehat A_R(\tau) - i \frac{\partial}{\partial
\tau}\widehat A_R(\tau) \ =\ 0 . \notag
\end{align}
**(3)** bilinearity of the commutator over the sum $K+\hat q_R$.\quad
**(4)** $[K,\widehat A_R(\tau)]$ is the generator of modular flow acting on $A(-\tau)$, which is
$i\partial_\tau\widehat A_R(\tau)$; the second commutator, evaluated with $[\hat q_R, e^{\pm i K \hat p_R}] =
\mp K e^{\pm i K \hat p_R}$ (from $[\hat q_R, \hat p_R] = i$), gives the same term with the opposite sign.

The operator $\widehat A_R(\tau)$ is genuinely gauge-invariant. The algebra generated by $\{\widehat A_R,
e^{i\hat q_R s}\}$ is identically the crossed-product algebra $\M \rtimes_\sigma \mathbb{R}$.

**Gravitational dressing to a physical observer's clock *emph* — not an analogy, a literal identity, checkable by comparing the two constructions gauge-fixing choice
for gauge-fixing choice: fixing the $L$-observer's clock at $\tau=0$ reproduces exactly the first presentation
of $\widehat\M$ and $\widehat\M'$ in Chapter~5; fixing the $R$-observer's instead reproduces the second
presentation, in which undressed elements of $\M$ sit directly inside $\widehat\M$. And since $K$ here is a
genuine modular Hamiltonian, the theorem of Chapter~5 applies immediately: $\widehat\M$ and $\widehat\M'$ are
type $\mathrm{II}_\infty$, with honest density operators and entropies — no further argument needed, since
it is literally the same construction already proven there.

## Application I: quantum volatile black hole spacetime and its entropy

Apply the model directly to the eternal AdS black hole: $\HH_Q$ is the bulk QFT in the black-hole geometry at
$G_N\to0$, $\ket\Psi$ is the Hartle—Hawking vacuum, $\M=\widetilde\M_R$, $\M'=\widetilde\M_L$, and $K$
generates ordinary Schwarzschild time. With two genuine asymptotic boundaries available, it is natural to
identify the $R,L$ "observers" of the previous section with the two boundaries themselves, and
$\hat q_R,\hat q_L$ with (mean-subtracted) perturbations of the boundary Hamiltonians $H_R,H_L$ around their
background values — concretely, in a microcanonical thermofield double peaked around energy $E_0\sim O(N^2)$
with an $O(N^0)$ spread, $\hat q_R\equiv H_R-\braket{H_R}$.

The crossed-product algebras are type $\mathrm{II}_\infty$ — and this genuinely reflects a change in the
physical spacetime structure. The gauge-invariant, but now quantum, quantity $\hat p_R+\hat p_L$ (the time
separation between the $R$ and $L$ boundaries, represented geometrically by a geodesic running between them)
has $O(1)$ fluctuations as $G_N\to0$ — precisely an example of the **quantum volatile geometry** met in
Chapter~8: **the two boundaries are connected by a genuine quantum wormhole**, not a classical one.

Now the entropy payoff, which closes the loop opened at the start of Chapter~5. For a semiclassical excited
state $\ket{\widehat\Phi}=\ket\Phi\otimes\ket g$ (exactly the construction of Chapter~5), the crossed-product
entropy formula of Chapter~5 gives

$$

S_{\widehat\M_R}^{(\widehat\Phi)} = -S(\Phi\|\Psi) + \text{const} .

$$

Separately — a gravitational computation quoted here rather than re-derived — it has been shown that,
assuming the system relaxes back to the equilibrium state $\ket\Psi$ as $t\to\infty$, this same relative
entropy is exactly (minus, up to an additive constant) the ordinary generalized entropy of the excited state,
$S(\Phi\|\Psi)=-S_{\text{gen}}^{(\Phi)}+\text{const}$. Combining the two:

$$

S_{\widehat\M_R}^{(\widehat\Phi)} = S_{\text{gen}}^{(\Phi)} + \text{const} .

$$

**The type II entropy of the gravitationally dressed algebra literally *emph* Every
algebraic step in this chain — crossed product, type II, its entropy formula — was proved in full generality in
Chapter~5; the only new input is the quoted gravitational identity relating relative entropy to generalized
entropy.

## Application II: de Sitter entropy

### The puzzle

De~Sitter space has no boundary at all — quantum gravity there faces a much deeper "problem of time" than
AdS does, with no asymptotic region to anchor observables to. A static observer (sitting at a pole of the
spatial sphere) only ever accesses a **static patch**, bounded by a cosmological horizon at the de~Sitter
radius $R$ (Fig.~\ref{fig:desitter}). The horizon carries the celebrated Gibbons—Hawking entropy,
$S_{\text{dS}}=A_{\text{hor}}^{(0)}/4G_N$ — but its physical meaning has been debated for decades (does its
exponential count a genuine, finite-dimensional de~Sitter Hilbert space, for instance?), with little concrete
progress.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.82\textwidth]{figs/fig_desitter.pdf}
\caption{(a) Penrose diagram of global de~Sitter space. The left edge is the worldline of a static observer at the north pole $r=0$ (blue arrow); the cosmological horizons (dashed red diagonals) confine everything this observer can ever see to the static patch $R$ (blue), while the patch $L$ (gold) belongs to an observer at the south pole (right edge). The top and bottom edges are future and past infinity $\mathcal I^\pm$, and the gray line is the $t=0$ slice. (b) That slice is a sphere: its northern half (blue) lies in $R$ and ends on the horizon $r=R$ (red equator), which is the black dot in (a).}
\label{fig:desitter}
\end{figure}

The *emph* de~Sitter entropy, $S_{\text{gen}}=A_{\text{hor}}/4G_N+\widetilde S_R$, has a strange
feature that is the opposite of a black hole's behavior: **exciting matter in the static patch
*emph*}$}, because it shrinks the cosmological horizon area faster than it grows the
matter entanglement $\widetilde S_R$. This can be checked completely explicitly: put a black hole of mass
parameter $\mu$ inside the static patch (giving a black-hole horizon at $r_b$ nested inside the cosmological
horizon at $r_c>r_b$), represent $\widetilde S_R$ by the black-hole horizon area itself, and the generalized
entropy comes out to $S_{\text{gen}}=\omega_{d-2}(r_c^{d-2}+r_b^{d-2})/4G_N$, which is *emph* than
$S_{\text{dS}}$ — so $S_{\text{dS}}$ is the maximum possible value of $S_{\text{gen}}$, achieved exactly by
empty de~Sitter.

### Worked calculation: why matter excitations decrease de~Sitter entropy

To see this thermodynamic behavior in detail, consider a four-dimensional Schwarzschild—de~Sitter spacetime
with metric:

$$

ds^2 = -f(r) dt^2 + \frac{dr^2}{f(r)} + r^2 d\Omega_2^2, \qquad f(r) = 1 - \frac{2 G_N M}{r} -
\frac{r^2}{R^2} .

$$


1. **Empty de~Sitter space ($M = 0$)**:
The horizon condition $f(r) = 1 - r^2/R^2 = 0$ gives a single cosmological horizon at $r_c^{(0)} = R$.
The cosmological horizon area is $A_{\text{dS}} = 4\pi R^2$, giving the Gibbons—Hawking entropy:

$$

S_{\text{dS}} = \frac{A_{\text{dS}}}{4 G_N} = \frac{\pi R^2}{G_N} .

$$

2. **Matter excitation: small black hole ($0 < G_N M \ll R$)**:
For a localized excitation of mass $M$, the horizon equation $f(r) = 0$ has two positive roots: a black hole
horizon at $r_b$ and a shifted cosmological horizon at $r_c < R$.
Let $r_c = R(1 - \delta)$ with $\delta \ll 1$. Expanding $f(r_c) = 0$ to first order in $\delta$ and $M$:

$$

1 - \frac{2 G_N M}{R} - (1 - 2\delta) \approx 0 \implies \delta = \frac{G_N M}{R} .

$$

Therefore the cosmological horizon shrinks to $r_c \approx R\left(1 - \frac{G_N M}{R}\right)$.
Its shifted area is:

$$

A_c(M) = 4\pi r_c^2 \approx 4\pi R^2 \left(1 - \frac{2 G_N M}{R}\right) = A_{\text{dS}} - 8\pi G_N M R .

$$

The black hole horizon is at $r_b \approx 2 G_N M$, with area $A_b(M) = 4\pi r_b^2 \approx 16\pi G_N^2 M^2
\sim O(G_N^2 M^2)$.
The total generalized entropy is the sum of both horizon areas:
\begin{align}
S_{\text{gen}}(M) = \frac{A_c(M)}{4 G_N} + \frac{A_b(M)}{4 G_N}
&\eqstep{1} \frac{A_{\text{dS}} - 8\pi G_N M R}{4 G_N} + O(G_N M^2) \notag\\
&\eqstep{2} S_{\text{dS}} - 2\pi M R + O(G_N M^2) . \notag
\end{align}
**(1)** substitute the shifted cosmological area $A_c(M)=A_{\text{dS}}-8\pi G_NMR$, and note that the
black-hole term $A_b/4G_N\approx4\pi G_NM^2$ is second order in $M$.\quad
**(2)** split the fraction: $A_{\text{dS}}/4G_N=S_{\text{dS}}$ and $8\pi G_NMR/4G_N=2\pi MR$.

Here $\beta_{\text{dS}} = 2\pi R$ is the inverse Gibbons—Hawking temperature. Thus, to linear order in
perturbation:

$$

S_{\text{gen}}(M) - S_{\text{dS}} = -\beta_{\text{dS}} M < 0 \quad \text{for all } M > 0 .

$$

Any localized energy excitation inside the static patch strictly **lowers** the generalized entropy.
Consequently, empty de~Sitter ($M = 0$) is the unique state of **maximal entropy**.

### Recognizing the type \texorpdfstring{$\mathrm{II}_1$}{II1} signature

This behavior — a reference state whose entropy can only ever decrease under perturbation — is exactly what
appeared, worked out on an explicit example, in the type $\mathrm{II}_1$ Bell-pair chain of Chapter~3, where
perturbing away from the maximally entangled $\ket{\Phi_{\pi/4}}$ always gives $S_\M(\Psi)\le0$.
**Empty de~Sitter behaves exactly like the maximally entangled reference state of a type
$\mathrm{II**_1$ algebra, with $R$ and $L$ static patches playing the role of the two entangled halves.}

Making this precise uses exactly the observer model above, with one small but crucial modification. Take
$\HH_Q$ to be the QFT Hilbert space on global de~Sitter, $\ket\Psi$ the Bunch—Davies vacuum, $\M,\M'$ the $R$-
and $L$-patch algebras (modular Hamiltonian $K$ = the boost generator of $t$-translations), and $\hat q_R,\hat
q_L$ the Hamiltonians of static observers at the two poles. This reproduces $\widehat\M_R,\widehat\M_L$ exactly
as before — *emph* that now $\hat q_R,\hat q_L$ are required to be **bounded below** (non-negative
eigenvalues — physically, the sensible statement that a real observer's energy cannot be negative). By exactly
the mechanism checked in Chapter~5 (restricting the clock spectrum to $q\ge0$ turns a divergent trace into a
normalized one), $\widehat\M_R,\widehat\M_L$ become type $\mathrm{II}_1$, not type $\mathrm{II}_\infty$. The
type $\mathrm{II}_1$ entropy relative to the maximally entangled reference state
$\ket{\widehat\Psi_T}=e^{-\hat q/2}\otimes\ket0_{\text{BD}}$, with trace $\tr(\cdots)\equiv\braket{
\widehat\Psi_T|\cdots|\widehat\Psi_T}$, is negative exactly the way the Chapter~3 example was, and for the
identical reason: there is no unentangled reference to fall below zero from, only a maximally entangled one to
fall below.

One more consistency check resolves an objection that looks fatal at first glance: if empty de~Sitter is a
maximally entangled state, should it not have infinite temperature (the way a maximally entangled Bell pair
has infinite temperature in the entanglement-Hamiltonian sense)? The resolution: the state
$\ket{\widehat\Psi_T}$ has density operator $\rho=e^{-K}$ on the crossed-product algebra — a thermal state at
*emph* temperature exactly $1$, the universal modular temperature of Tomita—Takesaki theory
(Chapter~4). Converting this dimensionless $\beta=1$ into physical units using the static observer's own
proper time $t$ reproduces exactly the known, finite de~Sitter temperature $T_{\text{dS}}=1/2\pi R$. There is
no contradiction: "maximally entangled" was always a dimensionless, modular-time statement, and the finite
physical temperature only appears once you convert to an observer's physical clock.

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

## Application III: generalized entropy for a local spacetime region

The black hole and de~Sitter examples both had a special simplifying feature: a single reference state existed
whose modular Hamiltonian coincided exactly with an honest geometric (isometric) time flow. A more general
region has no such flow. A standard example is Schwarzschild—de~Sitter: a black hole sitting inside a
de~Sitter universe, so the observer's accessible region is bounded by *emph* horizons at different
temperatures, $r_b<r_c$. With no common temperature, there is no single global geometric modular flow at all.
The construction generalizes cleanly: decompose the region's algebra as $\M_R=\M_c\otimes\M_b$ (cosmological-
and black-hole-horizon factors), choose a state making *emph* factor's modular flow separately geometric,
and introduce two independent pairs of observer Hamiltonians, one for each horizon, with a separate constraint
for each. The resulting type is not what naive analogy would suggest: even with both sets of observer
Hamiltonians bounded below, the algebra comes out type $\mathrm{II}_\infty$, not type $\mathrm{II}_1$ — and its
entropy reproduces exactly the expected sum of both horizon areas plus bulk matter entropy,

$$

S_{\text{gen}}=\frac{A_{\text{cos}}}{4G_N}+\frac{A_{\text{BH}}}{4G_N}+\widetilde S_R .

$$

This shows the crossed-product mechanism is robust and general, not a special property of the two simplest
(black hole, de~Sitter) examples.

## A model of dynamical observers

Every model so far treated the observer's own trajectory as fixed, non-dynamical — only its clock was quantum
mechanical. A more honest model lets the observer itself be a genuine, finite-mass dynamical particle, worked
out for two-dimensional de~Sitter space: promoting the particle's mass to a dynamical variable $Q(\tau)$ with
conjugate $P(\tau)$ and gauging the full de~Sitter isometry group (rather than just time translations)
produces a richer physical Hilbert space, with gauge-invariant, "dressed" field operators $\phi_R$ built by
projecting onto observer-frame matrix elements. A key structural result: the resulting observer algebra
$\Alg_R$ turns out to be a direct integral of type $\mathrm{I}_\infty$ factors — because a genuinely dynamical
observer can change its own trajectory, there is no fixed subregion its dressed operators stay confined to, so
they end up smeared, state-dependently, over an entire Cauchy slice. The static-observer limit of the
de~Sitter discussion above is recovered by sending the observer's mass $\Lambda\to\infty$ — but this limit does
*emph* commute with taking the double commutant: take $\Lambda\to\infty$ first and you recover the emergent
type II algebra (and its Gibbons—Hawking entropy); take the double commutant first and then send
$\Lambda\to\infty$, and you get type I instead. The type II structure — and the cosmological horizon's very
existence as an entropic object — is itself an emergent, order-of-limits-dependent phenomenon.


> [!NOTE] **Physics Connection: bounded-below spectra are why a Gibbs state exists at all**
> The distinction running through Chapter~5 and the de~Sitter discussion above — whether the observer's clock
> spectrum is bounded below decides type $\mathrm{II}_1$ versus type $\mathrm{II}_\infty$ — is exactly the same
> distinction you already navigate every time you write down a partition function. An ordinary Gibbs state
> $\rho=e^{-\beta H}/Z$ only exists as a normalizable density matrix if $Z=\Tr\,e^{-\beta H}$ converges, and
> that convergence is exactly the statement that $H$ is bounded below: for the harmonic oscillator,
> $H=\omega(n+\tfrac12)$ with $n=0,1,2,\dots$, so
> 
$$

> Z=\sum_{n=0}^\infty e^{-\beta\omega(n+1/2)}=\frac{e^{-\beta\omega/2}}{1-e^{-\beta\omega}}
> 
$$

> converges precisely because the sum is bounded below at $n=0$. This is the discrete, everyday version of the
> exact integral check carried out in Chapter~5, $\int_0^\infty dq\,e^{-q}=1$ versus $\int_{-\infty}^\infty
> dq\,e^{-q}=\infty$. A harmonic oscillator or a hydrogen atom has a ground state, and hence a sensible thermal
> state at any temperature, *emph* its spectrum is bounded below; a system whose energy were unbounded
> below would have no normalizable Gibbs state at any temperature. The observer models of this chapter are doing
> nothing more exotic: a physical observer's clock Hamiltonian $\hat q$ is bounded below for the same reason a
> real physical system's energy is — because a real system has a ground state — and it is exactly this ordinary
> fact, not a new gravitational input, that produces the finite trace (type $\mathrm{II}_1$) and hence the
> finite Gibbons—Hawking entropy of the cosmological horizon.


With a large but finite observer mass, the observer's position becomes increasingly uncertain over time: an
initial position uncertainty $1/\Lambda$ grows to $\sim e^{2\pi\tau/\beta_{\text{dS}}}/\Lambda$ after proper
time $\tau$, from the exponential expansion of de~Sitter. This defines a natural **scrambling time**
$\tau_s\equiv\tfrac{\beta_{\text{dS}}}{2\pi}\log\Lambda$, after which the observer has an $O(1)$ chance of
leaving its original static patch. This scrambling shows up concretely in an out-of-time-order correlator (a
standard chaos diagnostic): even though the matter field itself is free and does not directly interact with
the observer, the gravitational constraint couples them nontrivially — inserting an operator along the
observer's worldline physically "kicks" its trajectory, and this recoil produces genuine quantum chaotic
behavior, with a decay rate matching a Lyapunov exponent of $4\pi/\beta_{\text{dS}}$ — twice the universal
chaos bound, matching a mechanism identified independently in other contexts.

## Operator algebras of JT gravity

The chapter closes with a remarkable exact result, in a setting simple enough to solve completely rather than
only perturbatively: **Jackiw—Teitelboim (JT) gravity**, a two-dimensional gravity theory (with a scalar
"dilaton" field $\Phi$) coupled to matter, whose gravitational sector reduces entirely to boundary dynamics
once the dilaton's own equation of motion is solved, forcing the bulk geometry to be locally exact AdS$_2$.
The theory's gauge freedom (the isometry group of AdS$_2$) locks the two boundaries' Hamiltonians together,
$H_L=H_R\equiv H$, reducing the classical phase space to just two variables — equivalently, the boundary
geodesic separation $\ell$ and its conjugate momentum — which can be canonically quantized into a Hilbert space
$L^2(\mathbb R)$, with an (overcomplete) basis of states $\ket\beta$, $\beta\in\mathbb R_{>0}$, built from a
Euclidean path integral. Including matter fields (which do not couple directly to the dilaton), the full
quantum-gravitational Hilbert space becomes $\HH=L^2(\mathbb R)\otimes\HH_{\text{matt}}$, with a basis built
from path integrals with matter insertions on the Euclidean boundary.

This is one of the very few places in the entire subject where "the operator algebra of quantum gravity" is
known in exact, closed form: the full algebra of gauge-invariant JT-gravity observables (built including the
boundary Hamiltonian $H_R$ itself, at genuinely finite $G_N$ — with no crossed product, no auxiliary observer,
and no perturbative expansion needed as an approximation) is **type II**. This result is stated here
without proof. Unlike every earlier example in this chapter, it is not a statement about a semiclassical,
large-$N$ construction dressed onto an auxiliary clock; it is an exact statement about the full
quantum-gravitational theory itself, at finite coupling. It stands as concrete proof of principle that ``the
algebra of quantum gravity,'' at finite $G_N$, is a well-posed and answerable question — not merely a
semiclassical approximation scheme — at least in this simplest of solvable models.

\bigskip
\noindent The concrete applications of this chapter — black hole, de~Sitter, Schwarzschild—de~Sitter,
dynamical observers, and exact JT gravity — are all built from the same single mechanism: gravitational
dressing to a physical observer is the crossed product by the modular group, and it is this, and nothing more
exotic, that converts an intractable type $\mathrm{III}_1$ algebra with no entropy into a genuine type II
algebra whose entropy is exactly the gravitational entropy physicists already knew to expect. Chapter~10
closes with a summary and some more speculative remarks on what all of this might mean for the mathematical
structure of quantum gravity at finite $G_N$.



---

# Conclusions and outlook

## Summary

The main results of these notes fit into five statements. Each one is listed below together with the chapter
where it was built, so any one of them can be traced back to its full derivation.


- In the $G_N\to0$ limit, a general bulk subregion is defined by a boundary operator algebra —
typically one with no direct boundary geometric description at all — carrying an emergent type
$\mathrm{III}_1$ structure, sourced by the infinite long-range entanglement that only appears in the strict
large-$N$ limit (Chapters~6 and~7). This machinery is not restricted to the strict Einstein
($\lambda\to\infty$) limit; it extends, with modification, into the stringy regime (Chapter~8).
- Bulk causal structure is encoded in boundary *emph* structure — not merely boundary
causality (which only forces spacelike-separated operators to commute), but the richer, timelike commutant
structure that subregion-subalgebra duality inherits from the bulk. Quantitative tools like the causal depth
parameter $T(t)$ (Chapter~8) make this a checkable, numerical diagnostic of horizons and global causal
structure, and these tools too extend into the stringy regime.
- Modular flow, and its refinement half-sided modular flow, characterize the emergence of time itself in
the bulk — resolving the meeting-behind-the-horizon puzzle via emergent Kruskal time, and motivating a
sharpened, algebraic version of the ER$=$EPR proposal (both in Chapter~8).
- Large-$N$ boundary algebras split cleanly into two kinds. An **entanglement wedge algebra** $X$ is,
by definition, the large-$N$ limit of a genuine finite-$N$ algebra $B$ — it always admits a finite-$N$
ancestor. A **causal wedge algebra** $Y$, by contrast, is intrinsically a large-$N$, semiclassical
construct, built directly from single-trace operators via the extrapolate dictionary, with no finite-$N$
definition of its own. Neither is guaranteed to have a bulk geometric meaning once you leave the strict
Einstein regime — and both constructions apply just as well to non-gravitational systems entangled with a
holographic partner (Chapter~7), with no need for the non-gravitational side to have its own large-$N$
parameter at all.
- Simple operator-algebraic toy models — static observers, dynamical observers, and exactly solvable JT
gravity (all in Chapter~9) — turn this machinery into concrete physics: the physical origin of generalized
gravitational entropy for black holes, de~Sitter space, and general regions; the emergence of a cosmological
horizon as an observer's mass is taken to infinity; and, in JT gravity, a complete, finite-$G_N$ example where
the operator algebra of quantum gravity is known in exact closed form, even though the Hilbert space itself
does not factorize.


## The mathematical structure of quantum gravity

This final section is more speculative than the rest of the notes. It returns to the question raised in
Chapter~1 — *emph* — and answers it at the largest scale available.

### Why quantum gravity cannot have one single Hilbert space

Ordinary quantum mechanics treats the Hilbert space as fundamental: states are density operators living in it,
observables are operators acting on it. There is a concrete reason why this cannot be the right starting point
for quantum gravity. It is widely believed that no physical process in quantum gravity can change a
spacetime's *emph* structure — there is no physical process that takes a state of type IIB string
theory on $\text{AdS}_5\times S^5$ to a state on $\text{AdS}_3\times S^3\times K3$, or to either of these from
ten-dimensional flat Minkowski space. Since a genuine physical process is exactly what it means for two states
to live in the same Hilbert space (you can always in principle evolve from one to the other), **each of
these asymptotic backgrounds must correspond to a genuinely separate Hilbert space**. This is not a conjecture;
it is already visible directly in the existing dictionary: AdS$_5\times S^5$ is dual to a four-dimensional CFT
with its own Hilbert space, AdS$_3\times S^3\times K3$ to a two-dimensional CFT with a completely different
one, and nothing maps a state of one to a state of the other. Yet all of these are supposed to be different
vacua of the very same underlying theory — type IIB string theory. **Without one single, global Hilbert
space to hold all of these together, what mathematical object is left to call "the theory"?**

### The resolution you have already met, twice

This is exactly the same shape of question that opened Chapter~1, and the resolution is precisely the demotion
of the Hilbert space worked through in detail in Chapter~2, applied now at the grandest possible scale. Look
first at a much smaller-scale version of the same puzzle, already familiar from ordinary QFT in curved
spacetime: a free scalar field in flat Minkowski space can be quantized using ordinary Minkowski time,
*emph* using Rindler time (Chapter~4). Both are perfectly sensible choices, describing different physical
situations (an inertial versus an accelerated observer), and yet they produce genuinely, unitarily
*emph* Hilbert spaces. You could declare these to be two different theories, but that is clearly
the wrong instinct — there is an obvious sense in which it is the same free scalar field theory, just quantized
around two different reference states. **Algebraic QFT resolves this by defining the theory as a pair
$(\Alg,\Sscr)$ — an algebra $\Alg$ of field operators, together with a space $\Sscr$ of allowed states (in the
abstract, linear-functional sense of Chapter~2, not vectors in any particular Hilbert space) — and letting the
Hilbert space be a *emph* Minkowski quantization and Rindler quantization are
simply two different GNS representations of the very same underlying algebra $\Alg$ — genuinely different
Hilbert spaces, but manifestly the same theory, because the algebra never changed.

**The proposal is to do exactly this, one level up, for the whole of quantum gravity.** Postulate that a
quantum-gravity theory at finite $G_N$ is specified by a single abstract $*$-algebra $\Alg$ (not tied to any
particular asymptotic structure) together with some allowed collection of states on it. Different asymptotic
structures — AdS$_5\times S^5$, AdS$_3\times S^3\times K3$, flat space, de~Sitter — simply correspond to
*emph* $\omega$ on this one algebra, each producing its own GNS Hilbert space $\HH_\omega$ via
exactly the construction of Chapter~2, with the corresponding boundary CFT (where one is known) simply
*emph* that GNS representation. Concretely: $\omega_{\text{AdS}_5\times S^5}$ is the state whose GNS
Hilbert space is that of $\mathcal N=4$ super-Yang-Mills; $\omega_{\text{AdS}_3\times S^3\times K3}$ is the
state whose GNS space is the dual two-dimensional CFT's; and, in principle, flat space and de~Sitter correspond
to further states of the same underlying algebra $A_{\text{IIB}}$, even though an explicit boundary description
for those cases is not yet known.


> [!NOTE] **Physics Connection: levels of algebraic emergence**
> This is the same logical move made twice already in these notes. Lined up side by side, the three levels are
> each a strictly more drastic version of the same idea:
> 
- **States (Chapter~2, Slavnov's statistical picture)**: an ordinary quantum *emph* $\omega$
> (or $\rho$, or $\ket\psi$) is not fundamental — it is a derived bookkeeping device (an ensemble average, in
> Slavnov's language) built on top of the more primitive pairing of algebra and individual measurement outcome.
>
- **Hilbert spaces (Chapter~2's GNS construction, and the Minkowski—Rindler example just above)**:
> the *emph* is not fundamental — a single algebra $\Alg$ can produce many inequivalent
> Hilbert spaces, one per choice of reference state, via GNS.
>
- **Spacetime backgrounds (this section)**: even the question "which spacetime background am I in"
> is not fundamental data fed into the theory — it, too, is just a choice of state on one underlying algebra,
> with the entire geometric structure of a spacetime (AdS, flat space, de~Sitter, and everything built on top of
> it in these notes — causal structure, horizons, entropy) emerging as a *emph* of that choice, not an
> ingredient of it.
>

> Nothing about the mathematics changed between these three instances — it is the identical GNS construction,
> applied at the level of an individual measurement, then at the level of an ordinary quantum system, then at
> the level of an entire spacetime background. What changed is only how much structure you are willing to
> regard as emergent rather than fundamental, and each chapter of these notes have pushed that boundary a little
> further out.


At present, there is no known background-independent definition of the algebra $A_{\text{IIB}}$ itself, nor a
full characterization of which states are allowed. String field theory is a plausible route toward one, since
for any fixed background state it already supplies both the Hilbert space and the background-dependent
algebra, with its equations of motion available to help identify further consistent states systematically.
The algebraic program developed in these notes — subregion-subalgebra duality, modular time, the crossed
product, generalized entropy from observer dressing — can be read as a first, concrete step toward exactly
this larger goal: a formulation of quantum gravity in which asymptotic structure, the cosmological constant,
the Hilbert space, and the very number of degrees of freedom are not fixed ingredients handed to the theory in
advance, but *emph* of a single, more primitive algebraic structure.

## Further reading

Two technical computations are not reproduced in these notes; both can be found in~[Liu2025]. The first
consists of further finite-dimensional examples of infinite entanglement coexisting with a factorizable Hilbert
space — fine-tuned counterexamples to the general expectation, discussed in Chapter~2, that infinite
entanglement generically prevents factorization. The second is the explicit solution of the KMS relation that
gives $\widehat\Delta=\Delta_\Psi$ for the crossed-product algebra, the result used without derivation in
Chapter~5. Neither changes the conceptual picture developed here.

\bigskip
\noindent These notes began with a wavefunction and asked what it really is. The answer that emerged, one
worked example at a time, is that the wavefunction, the Hilbert space it lives in, and finally the spacetime
itself are each the most convenient representation of something more primitive: an algebra of observables,
together with a choice of state on it. Which parts of the familiar picture are fundamental, and which are
representations of something deeper, is the same question at every level — for a single spin, for a quantum
field in a Rindler wedge, for a black hole, and for the universe as a whole.
