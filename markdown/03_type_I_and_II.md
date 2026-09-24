# Chapter 3: Type I and II Algebras and Entanglement

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
