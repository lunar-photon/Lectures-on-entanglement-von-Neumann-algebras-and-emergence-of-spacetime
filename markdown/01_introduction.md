# Chapter 1: Introduction and Motivations

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
