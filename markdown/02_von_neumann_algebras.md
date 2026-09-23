# Sec. II: Introduction to von Neumann Algebras

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
