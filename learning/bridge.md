# From Grover search to noise clocks

[Selected anchor](anchor.md) · [Thirty-milestone map](milestones.md) · [Scientific guide](../science/README.md)

This bridge connects Childs's ideal-query foundations to the repository's actual noise model. The channel and renewal explanations below are supplied locally. The universal noisy-progress inequality is a primary research dependency, identified explicitly where it enters.

## The computational task

Imagine a test device for $`N`$ numbered positions. There is either no marked position or one marked position. A classical call tests one position and returns its bit. A quantum call can act on a superposition of positions, allowing a sequence of queries and known reflections to concentrate probability on the mark.

The device's query port occasionally dephases the position register. It reports that an event occurred only after the call. The device always performs the requested oracle operation first. Its noise is therefore different from an oracle that occasionally does nothing.

The question is how many **physical calls** are necessary to find the mark, or correctly report its absence, when the times of these events are correlated. A query made merely to advance the clock still costs one. Waiting without calling the device does not advance this clock.

The input is $`x\in\{0^N,e_1,\ldots,e_N\}`$, where $`e_j`$ has its only 1 at position $`j`$. The required output is $`j`$ on that input and 0 on $`0^N`$; pseudocode writes the latter as `none`. The quantity $`Q_\epsilon(N;L)`$ is the smallest deterministic query cap achieving error at most $`\epsilon`$ on every allowed input, averaged over the noise and the algorithm's randomness. The noise law $`L`$ and $`0<\epsilon<1/2`$ are fixed as $`N`$ grows.

A basis-state test remains exact under this noise, so classical scanning costs $`N`$ queries. Input-independent flags cannot reveal an unqueried mark, giving the matching classical order $`\Theta(N)`$. The [resource comparison](../science/interpretation.md#classical-search-remains-linear) proves this in the same oracle model.

## States, queries and notation

A register is a quantum system used to hold information. A pure index state has the form $`\lvert\psi\rangle=\sum_i a_i\lvert i\rangle`$, with $`\sum_i|a_i|^2=1`$; measuring its index returns $`i`$ with probability $`|a_i|^2`$. A density matrix $`\rho`$ also describes mixed states and correlations with other registers. For a pure state, $`\rho=\lvert\psi\rangle\langle\psi\rvert`$. A unitary gate $`U`$ acts by $`\rho\mapsto U\rho U^\dagger`$, where the dagger denotes the conjugate transpose.

The register labels $`\mathsf I`$, $`\mathsf S`$ and $`\mathsf B`$ below denote the physical query index, protected logical index and answer qubit. The function $`S(\ell)`$ denotes a probability; it is not the logical register.

| Notation | Meaning |
|---|---|
| $`N,x,\epsilon`$ | Number of positions, unknown input string and allowed error. |
| $`O_x`$ | One ordinary XOR oracle call. |
| $`Z_t`$ | Event flag returned after physical call $`t`$. |
| $`L,S(\ell),\mu`$ | Gap length, survival probability $`\Pr(L\ge\ell)`$, and mean gap $`\mathbb E L`$. |
| $`A_t,h(a),\pi(a)`$ | Pre-query age, conditional next-call event probability, and stationary age distribution. |
| $`R,M_R`$ | Cutoff $`\lceil\sqrt N\rceil`$ and truncated moment $`\mathbb E\min\{L^2,R^2\}`$. |
| $`\Psi_t,u_t`$ | Proof variables for quantum progress; neither is the renewal age. |
| $`\alpha,\beta`$ | Gap-tail exponent and low-risk hazard exponent in the alternating construction. |

Here $`\Pr`$ means probability and $`\mathbb E`$ means expectation. The statement $`f(N)=\Theta(g(N))`$ means upper and lower bounds by positive constant multiples for sufficiently large $`N`$. These constants may depend on the fixed law and error. The notation $`f\asymp g`$ also means comparison up to constants; $`f\sim g`$ is stronger and means their ratio tends to one.

### Correspondence with Childs

In [Section 21.2, equation (21.2)](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=106), Childs writes the bit oracle as $`\widehat O_x`$; the repository calls that same operation $`O_x`$:

```math
O_x\lvert i,b\rangle=\lvert i,b\oplus x_i\rangle.
```

The symbol $`\oplus`$ means addition modulo two. Childs's equation (21.3) calls the answer-Hadamard conjugate the phase oracle. Here its needed action follows directly by preparing the answer in $`\lvert-\rangle=(\lvert0\rangle-\lvert1\rangle)/\sqrt2`$:

```math
O_x\lvert i,-\rangle=(-1)^{x_i}\lvert i,-\rangle.
```

Thus one physical XOR call supplies a phase flip on the marked component. We introduce no separate controlled-oracle resource. Childs's input length $`n`$ in Chapter 21 is $`N`$ here, not the number of qubits in an index register. His marked set $`M`$ in Chapter 19 is a set; the $`M`$ used for the active-call count in the [predictability proof](../science/predictable-queries.md) is an integer.

For one mark $`j`$, let

```math
\lvert s\rangle=\frac1{\sqrt N}\sum_{i=1}^N\lvert i\rangle,
\qquad
D=2\lvert s\rangle\langle s\rvert-I,
\qquad
\theta_N=\arcsin(N^{-1/2}).
```

The state $`\lvert s\rangle`$ and reflection $`D`$ use known gates and contain no loaded input data. A Grover iteration is a phase query followed by $`D`$. In the plane spanned by the marked state and the uniform unmarked state, each iteration rotates the state by $`2\theta_N`$. Starting at angle $`\theta_N`$, after $`m`$ complete ideal iterations the success probability is

```math
p_m=\sin^2((2m+1)\theta_N).
```

This explains both the initial quadratic growth with $`m`$ and saturation near $`m\asymp\sqrt N`$. The project uses only the zero-or-one-mark promise.

## What a flagged query does

Let $`P_i=\lvert i\rangle\langle i\rvert_{\mathsf I}\otimes I_{\rm rest}`$. Complete index dephasing, also called pinching, is

```math
\Delta_{\mathsf I}(\rho)=\sum_{i=1}^N P_i\rho P_i.
```

It removes off-diagonal blocks between different query indices while preserving the probabilities of those indices. It acts only on the query index; it does not dephase every workspace register.

The order of one call is

```math
\rho\longmapsto O_x\rho O_x^\dagger
\longmapsto
\begin{cases}
O_x\rho O_x^\dagger,&Z_t=0,\\
\Delta_{\mathsf I}(O_x\rho O_x^\dagger),&Z_t=1.
\end{cases}
```

Then the algorithm receives $`Z_t`$ and chooses its next operation. The flag reveals whether dephasing occurred, not the inaccessible index outcome associated with that dephasing. It cannot warn the algorithm before the same call.

The clock is **exogenous**: it is generated without knowing the input or the algorithm's choices. A decision can depend on earlier flags, so the algorithm's state and the clock history can be correlated. The decision cannot feed back into future event probabilities. Once the noise history and initial age are fixed, measurements of the algorithm and hidden index records supply no additional influence on the next hazard. This is the condition used in the [exact model](../science/model.md#index-dephasing-and-its-flag).

## A complete event-order example

Take three positions, with position 3 marked. Start just after a renewal with the uniform state. For this calculation, consider the event sequence $`Z_1=0,Z_2=1`$. The algorithm sees each flag only after its call.

After the first unflagged phase query and diffusion, the index state is

```math
\frac1{3\sqrt3}
\begin{pmatrix}-1\\-1\\5\end{pmatrix}.
```

The second oracle flips the marked amplitude. The subsequent event removes index coherence, leaving the index density matrix

```math
\rho_{\rm flag}=\frac1{27}
\begin{pmatrix}
1&0&0\\
0&1&0\\
0&0&25
\end{pmatrix}.
```

The answer qubit remains $`\lvert-\rangle`$ and has been suppressed in these expressions. Measuring the index immediately gives the marked candidate with probability $`25/27`$.

The timing matters. If diffusion is inserted after this pinching and before the measurement, the marked probability becomes

```math
\frac49\left(\frac1{27}+\frac1{27}\right)
+\frac19\frac{25}{27}
=\frac{11}{81}.
```

That calculation uses the squared entries in the marked row of $`D`$: two entries have square $`4/9`$ and the diagonal entry has square $`1/9`$.

A third, charged call verifies the measured candidate: put that basis index in $`\mathsf I`$ and $`\lvert0\rangle`$ in the answer. The answer becomes its oracle bit. Pinching a definite index does not change it, so verification is exact even if the third call is flagged.

This is a small channel-order example, not the large-$`N`$ capped search algorithm. The [density-matrix verification](../verification/README.md#what-is-checked) checks this example and the general formulas independently. In the paired-interval proof, an event on call $`\ell`$ leaves $`\ell-1`$ complete Grover iterations before the final phase query. Measuring before diffusion gives $`\sin^2((2\ell-1)\theta_N)`$.

## Parking the logical state

A second strategy preserves coherent progress across different renewal cycles. Store the logical state in $`\mathsf S`$, and expose it to the physical query port only on selected calls.

| Call type | Physical index and answer | Effect on the logical state | Query cost |
|---|---|---|---:|
| Active | Swap the logical index into $`\mathsf I`$; answer $`\lvert-\rangle`$. | An unflagged call followed by diffusion performs one Grover iteration; an event can corrupt it. | 1 |
| Dummy | Fixed basis index $`\lvert j\rangle`$; answer $`\lvert+\rangle`$. | Both the XOR action and index pinching leave these port registers unchanged; the logical state stays in $`\mathsf S`$. | 1 |
| Verification | Measured candidate index; answer $`\lvert0\rangle`$. | Returns its exact oracle bit. | 1 |

Here $`\lvert+\rangle=(\lvert0\rangle+\lvert1\rangle)/\sqrt2`$ is unchanged by a bit flip. Its use does not assume that the dummy index is unmarked. The basis index is also essential: a neutral answer alone would not protect a superposition held in the physical index from pinching.

Swaps and answer-state changes are known gates. They do not call an inverse or controlled oracle. Protected memory is a supplied feature of this model; the algorithm does not construct a noise-free memory from a bath affecting every register.

The paired-interval strategy measures its candidate when a search call is flagged. The protected-memory strategy instead makes the probability of any flagged active call small and proves correctness on the complementary event. These are two different uses of the same interface.

## Renewal facts needed here

A **renewal** is a flagged event. A gap $`L`$ counts all calls after one event up to and including the next. Fresh complete gaps are independent copies of the same known distribution.

If the next gap is $`\ell`$, its calls have pre-query ages $`0,1,\ldots,\ell-1`$; the last call is flagged. Let $`S(\ell)=\Pr(L\ge\ell)`$. Counting the integer levels reached by $`L`$ gives

```math
\mu=\mathbb E L=\sum_{\ell\ge1}S(\ell).
```

At age $`a`$, survival up to that age is already known. The risk on the next call is therefore

```math
h(a)=\Pr(L=a+1\mid L\ge a+1)
=1-\frac{S(a+2)}{S(a+1)}.
```

This **hazard** differs from the average event rate. It asks about the next call given the elapsed age.

Stationary initialization describes observing the clock at an arbitrary call index, rather than starting immediately after an event. Each complete cycle visits age $`a`$ once precisely when $`L\ge a+1`$. Normalizing by the mean cycle length gives

```math
\pi(a)=\frac{S(a+1)}{\mu}.
```

The [model](../science/model.md#exact-renewal-convention) checks stationarity directly. The reset probability is

```math
\sum_{a\ge0}\pi(a)h(a)
=\frac1\mu\sum_{a\ge0}
\bigl(S(a+1)-S(a+2)\bigr)
=\frac1\mu.
```

The initial containing gap is length-biased: a longer gap contains more possible observation times. Its age is initially hidden. Once a flag is observed, subsequent ages can be counted exactly.

Let $`F`$ be the number of calls until the first flag. Averaging the conditional survival probability over $`\pi`$ gives

```math
\Pr(F>w)=\frac1\mu\sum_{\ell>w}S(\ell).
```

Finite $`\mu`$ makes this tail tend to zero, even when $`\mathbb E F`$ is infinite. For a fixed error allowance, choose a finite timeout with sufficiently small tail probability and spend charged dummy calls until the first flag or that timeout. This is a quantile guarantee, not a finite-mean-residual argument. The timeout can be large and depends on the fixed law.

## The first theorem: a truncated moment

The [renewal theorem](../science/renewal-law.md#theorem-1-stationary-renewal-search) assumes $`\mu<\infty`$ and

```math
h(a)\ge \frac{c}{a+1}
```

for one positive constant $`c`$ at **every reachable age**. With $`R=\lceil\sqrt N\rceil`$ and $`M_R=\mathbb E\min\{L^2,R^2\}`$, it proves

```math
Q_\epsilon(N;L)=\Theta\!\left(\frac{\mu N}{M_R}\right).
```

The square reflects Grover's initial probability growth. The cutoff reflects saturation: an interval much longer than $`\sqrt N`$ cannot provide a success probability larger than one.

The upper algorithm pairs fresh intervals. It searches during the first, stopping at its flag or a cap of order $`\sqrt N`$. It verifies the candidate during the second and uses charged dummy calls to reach that interval's end. A pair has mean cost $`2\mu`$ and success probability at least a constant multiple of $`M_R/N`$. Roughly $`N/M_R`$ independent pairs therefore suffice for a fixed success target.

To obtain a deterministic budget, the proof fixes the number of trials and bounds the probability that their total cost exceeds a sufficiently large multiple of its expectation. It combines this deadline failure with startup and search failure using a union bound. A trial's cost and reward may be correlated. The [complete upper proof](../science/renewal-law.md#upper-bound-with-a-deterministic-call-budget) needs only finite mean; the hazard condition enters the matching lower bound.

The moment is computed by the elementary identity

```math
M_R=\sum_{\ell=1}^R(2\ell-1)S(\ell),
```

because $`k^2=\sum_{\ell=1}^k(2\ell-1)`$. For the fully specified smooth law $`S(\ell)=\ell^{-\alpha}`$, this gives:

| Fixed exponent | Optimal quantum queries |
|---|---:|
| $`1<\alpha<2`$ | $`\Theta(N^{\alpha/2})`$ |
| $`\alpha=2`$ | $`\Theta(N/\log N)`$ |
| $`\alpha>2`$ | $`\Theta(N)`$ |

The [examples](../science/examples.md) also give the fixed finite-mean law $`S(\ell)=1/[\ell(1+\log\ell)^p]`$, $`p>1`$, whose cost is $`\Theta(\sqrt N(\log N)^p)`$. This result retains the cost of stationary startup.

## The research-level lower-bound input

Childs's Chapter 23 introduces the ideal-query method of comparing how distinguishable different inputs become. The noisy converse used here is the separate result of **Agarwal–Rao–Song (ARS)**, [Sections 5–6 and Lemmas 6.7–6.8](https://arxiv.org/html/2610.00506v2).

ARS supplies a bounded progress potential $`0\le\Psi_t\le3`$, initially zero, and a fixed positive terminal requirement $`\mathbb E\Psi_T\ge\gamma_\epsilon`$. Before call $`t`$, its conditional increment satisfies

```math
\mathbb E[\Psi_t-\Psi_{t-1}\mid\mathcal F_{t-1}]
\le \frac{12}{N}+\frac{12u_t}{\sqrt N}-2p_tu_t^2,
\qquad 0\le u_t\le1.
```

The symbol $`\mathcal F_{t-1}`$ denotes the information available before the call, and $`p_t`$ is its conditional event probability. The positive terms permit progress; the negative term limits an active component when dephasing is likely. The potential and $`u_t`$ are proof variables, not observables the algorithm is asked to estimate.

For the lower bound, the proof can reveal the initial age, making the algorithm stronger. Then $`p_t=h(A_t)`$. The [mapping proof](../science/progress-bound.md#why-the-initial-age-conditioning-is-valid) conditions the local inequality correctly while applying terminal correctness to the unconditional state. Correctness averaged over ages does not imply correctness at each separate age.

The first theorem stops the **analysis** before the age reaches $`R`$. Before that threshold, completing the square and using the harmonic hazard bound control progress by a constant times $`(A_t+1)/N`$. Averaging over stationary ages below $`R`$ produces the truncated sum in $`M_R`$.

The discarded event must include an already old initial interval. If $`\tau_R`$ is the first pre-query time with age at least $`R`$, and $`r_R=\Pr(A_1\ge R)`$, then

```math
\Pr(\tau_R\le T)
\le r_R+\frac{(T-1)S(R+1)}{\mu}.
```

A first crossing from below must pass through age exactly $`R`$. The potential is bounded, so discarding these histories loses at most three times their probability. Combining the stopped progress and crossing estimates gives

```math
\gamma_\epsilon
\le 3r_R+(15+18/c)\frac{TM_R}{\mu N}.
```

Since $`r_R\to0`$, the required lower bound follows for sufficiently large $`N`$. Stopping is finite proof bookkeeping; it does not create a new algorithm required to be correct on stopped histories. The [stopped proof](../science/renewal-law.md#lower-bound-by-stopping-before-old-ages) is what handles rare old initial intervals sharply.

ARS already supplies the general correlated-noise model, potential and predictable-rate principle. The project adds the renewal estimates, stationary-initialization application and matching constructions. The [attribution account](../references/related-work.md) records this distinction.

## The second theorem: predictable low-risk ages

The harmonic hazard condition limits how safe a particular old age can become. The second theorem deliberately permits much safer ages.

Fix $`\alpha>1`$, $`\beta>\max\{1,\alpha-1\}`$ and $`0<c_L<1/2`$. Set

```math
h(a)=
\begin{cases}
c_L(a+2)^{-\beta},&a\text{ even},\\
\min\{1/2,\,2\alpha/(a+2)\},&a\text{ odd}.
\end{cases}
```

Every hazard is positive. The odd-age harmonic sum determines the tail exponent, while the even-age hazards have a convergent sum. The [survival calculation](../science/predictable-queries.md#survival-asymptotics) gives $`S(\ell)\sim C\ell^{-\alpha}`$ for a positive $`C`$.

The algorithm needs $`M=\Theta(\sqrt N)`$ ideal Grover calls. Choose a sufficiently large constant in $`A=\Theta(M^{1/\beta})`$. Use the logical state only at even ages in $`[A,2A]`$ and park it during all other charged calls. Each active call then has conditional event probability at most a chosen small constant divided by $`M`$. A union bound makes the chance of any corrupted active call small; independence of active errors is unnecessary.

A cycle of length at least $`2A+2`$ supplies order $`A`$ active slots and has probability of order $`A^{-\alpha}`$. Obtaining $`M`$ active slots has expected cost at most a constant times $`\mu M A^{\alpha-1}`$ physical calls. The proof converts this upper bound into a deterministic deadline and includes the first-flag timeout and final verification. It never reveals the future cycle length.

For the converse, the conditional progress inequality yields the [stationary hazard bound](../science/progress-bound.md#stationary-hazard-bound) in terms of

```math
B_N=\sum_{a\ge0}\pi(a)
\min\{\sqrt N,h(a)^{-1}\},
\qquad
Q_\epsilon(N;L)\ge\frac{\gamma_\epsilon N}{30B_N}.
```

The even-age sum changes regime near $`a\asymp N^{1/(2\beta)}`$. Its evaluation matches the algorithm and proves [Theorem 2](../science/predictable-queries.md#alternating-hazard-theorem):

```math
Q_\epsilon(N;L)
=\Theta\!\left(N^{1/2+(\alpha-1)/(2\beta)}\right).
```

The converse includes every adaptive algorithm allowed by the model, not just the displayed parking policy.

## Equal mean and tail, different costs

The smooth and alternating laws can be matched more closely than their exponent. Write their means as $`\mu_i`$ and tail coefficients as $`C_i>0`$, for $`i\in\{s,a\}`$. Choose $`0<c_*<\min_i C_i`$ and $`\lambda_i=c_*/C_i`$.

To set a common mean, choose

```math
\mu_*>\max_i\{\lambda_i\mu_i+1-\lambda_i\},
\qquad
m_i=\frac{\mu_*-\lambda_i\mu_i}{1-\lambda_i}>1.
```

Take an integer $`R_0>\max_i m_i`$ and a two-point distribution $`\nu_i`$ with

```math
\nu_i(R_0)=\frac{m_i-1}{R_0-1},
\qquad
\nu_i(1)=\frac{R_0-m_i}{R_0-1}.
```

These probabilities are positive and give mean $`m_i`$. The mixture $`\widetilde P_i=\lambda_iP_i+(1-\lambda_i)\nu_i`$ has mean exactly $`\mu_*`$. Above $`R_0`$, its survival is just $`\lambda_iS_i(\ell)`$, so both asymptotic tails are $`c_*\ell^{-\alpha}`$.

The common survival multiplier cancels in each eventual hazard ratio. Only finitely many hazards change, and all remain positive. The [finite-prefix proofs](../science/comparisons.md#the-search-exponents-persist) preserve both complexity results.

For $`\alpha=3,\beta=4`$, the resulting two clocks have the same positive stationary event rate, the same asymptotic survival coefficient and exponent, full support and finite gap variance. Yet

```math
Q_\epsilon(N;\widetilde L_s)=\Theta(N),
\qquad
Q_\epsilon(N;\widetilde L_a)=\Theta(N^{3/4}).
```

Their higher finite moments need not have equal numerical values, and their full survival sequences need not coincide. The comparison fixes the average risk and leading tail while allowing different conditional risks at individual ages. Past flags make those ages usable for scheduling.

## Reading the result with its assumptions

The [model](../science/model.md) supplies a perfect XOR operation, index-only pinching, post-query event flags, ideal controls and protected workspace. The clock advances on calls. Every startup, active, dummy and verification call is counted; input-independent state preparation loads no hidden data. The output is a classical index or `none`.

The laws are fixed and known, the input has zero or one mark, and the error target is fixed. Constants and the asymptotic onset may depend on the law. The results do not supply a gate-count or physical wall-clock theorem, noise-law learning, or a matching theorem when all memory is noisy or flags are absent. The alternating theorem uses the strict condition $`\beta>\max\{1,\alpha-1\}`$; its excluded critical boundary is not solved here.

The [verification record](../verification/README.md) checks finite channels, parking and renewal identities. Analytical proofs establish asymptotic optimality. The [milestone map](milestones.md) connects these local objects and proof steps into the complete scientific argument, while the [science guide](../science/README.md) provides the specialist route.
