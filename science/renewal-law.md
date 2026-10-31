# The truncated-moment resource law

[Science guide](README.md) · [Repository](../README.md)

A long interval can support a longer coherent Grover run, but its contribution saturates once it reaches order $`\sqrt N`$. Under a global lower bound on the conditional hazard, this truncated second moment determines the optimal search cost. The statement uses the [model and renewal convention](model.md) and the [ARS progress lemma](progress-bound.md).

For an integer $`R\ge1`$, define

**Equation (4).**

```math
M_R=\mathbb E[\min\{L^2,R^2\}],
\qquad
r_R=\frac1\mu\sum_{\ell=R+1}^{\infty}S(\ell).
```

Here $`r_R=\Pr(A_1\ge R)`$ and $`r_R\to0`$. The elementary identities and inequalities used below are

**Equation (5).**

```math
M_R=\sum_{\ell=1}^{R}(2\ell-1)S(\ell),
\quad
\sum_{\ell=1}^{R}\ell S(\ell)\le M_R,
\quad
R^2S(R+1)\le M_R,
\quad
M_R\le R\mu.
```

The first identity follows by telescoping the square of $`\min(L,R)`$; the others follow termwise or directly from the definition.

### Theorem 1: stationary renewal search

Suppose the fixed gap law has finite mean and, for some $`c>0`$, satisfies

**Equation (6).**

```math
h(a)\ge\frac{c}{a+1}
\quad\text{at every reachable age }a.
```

For every fixed $`\epsilon\in(0,1/2)`$, with $`R=\lceil\sqrt N\rceil`$,

**Equation (7).**

```math
\boxed{
Q_\epsilon(N;L)
=\Theta_{\epsilon,L,c}\!\left(\frac{\mu N}{M_R}\right).
}
```

The upper bound requires only $`\mu<\infty`$, not (6). The lower bound holds even if the initial age is revealed. Both bounds concern a deterministic query budget and unrestricted adaptive algorithms in the stated model.

The asymptotic constants and the threshold in $`N`$ may depend on the fixed law. A quantitative version of the lower bound is

**Equation (8).**

```math
T\ge
\frac{\mu N}{(15+18/c)M_R}
\bigl(\gamma_\epsilon-3r_R\bigr)_+,
\qquad
\gamma_\epsilon=
\frac{\left(1-2\sqrt{\epsilon(1-\epsilon)}\right)^2}{36}.
```

The upper bound below has the explicit form

**Equation (9).**

```math
T\le w_{\epsilon/3}
+\left\lceil\frac{6\mu}{\epsilon}
\left\lceil\frac{N}{bM_R}\log\frac3\epsilon\right\rceil\right\rceil,
\qquad b=\frac{1}{64\pi^2},
```

for $`N\ge64`$, where $`w_\eta`$ is any positive integer satisfying
$`\mu^{-1}\sum_{\ell>w_\eta}S(\ell)\le\eta`$.

## Lower bound by stopping before old ages

Fix a $`T`$-query algorithm with error at most $`\epsilon`$. Give it the initial age if desired, and use the [augmented filtration](progress-bound.md#why-the-initial-age-conditioning-is-valid). Throughout, the stochastic process describes the original algorithm run to horizon $`T`$; stopping is an analytical device, not a new purportedly correct algorithm.

Let

**Equation (14).**

```math
\tau_R=\inf\{t\ge1:A_t\ge R\},
\qquad
\sigma=\min\{T,\tau_R-1\},
```

with $`\tau_R=\infty`$ if the set is empty. The event $`\{t<\tau_R\}`$ is known before query $`t`$: it only asks whether a pre-query age at or before $`t`$ has reached $`R`$. Thus the finite identity

**Equation (15).**

```math
\Psi_\sigma-\Psi_0
=\sum_{t=1}^{T}\mathbf1_{\{t<\tau_R\}}
(\Psi_t-\Psi_{t-1})
```

can be averaged using [the local progress inequality (11)](progress-bound.md). No optional-stopping theorem or unbounded stopping-time limit is needed.

For $`h>0`$, completing the square in the active magnitude $`u`$ gives

```math
\frac{12u}{\sqrt N}-2hu^2\le\frac{18}{Nh}.
```

By (6), before the stop the conditional drift is at most

**Equation (16).**

```math
\frac{12}{N}+\frac{18}{Nh(A_t)}
\le C_c\frac{A_t+1}{N},
\qquad C_c=12+18/c.
```

Dropping the condition that no earlier age crossed the threshold can only increase this nonnegative bound. Stationarity then yields

**Equation (17).**

```math
\begin{aligned}
\mathbb E\Psi_\sigma
&\le\frac{C_c}{N}\sum_{t=1}^{T}
\mathbb E[(A_t+1)\mathbf1_{\{A_t<R\}}]\\
&=\frac{C_cT}{\mu N}\sum_{\ell=1}^{R}\ell S(\ell)
\le\frac{C_cTM_R}{\mu N}.
\end{aligned}
```

This step already optimizes out the algorithm-dependent active magnitude. Correlation between the query state and the age therefore causes no replacement of a conditional expectation by an unjustified independent one.

### The crossing bound

If $`A_1<R`$, the first entrance into $`[R,\infty)`$ must occur at age exactly $`R`$, because the age only increases by one or resets to zero. Hence

```math
\{\tau_R\le T\}
\subseteq\{A_1\ge R\}\cup
\bigcup_{t=2}^{T}\{A_t=R\},
```

and therefore

**Equation (18).**

```math
\Pr(\tau_R\le T)
\le r_R+\frac{(T-1)S(R+1)}{\mu}.
```

This includes an upward crossing inside the initially straddling renewal interval. Counting only fresh long gaps starting after time zero would not establish (18).

On $`\{\tau_R>T\}`$, the stopped and terminal potentials agree. On its complement, both lie in $`[0,3]`$. The [terminal progress bound (10)](progress-bound.md) and equation (18) imply

**Equation (19).**

```math
\mathbb E\Psi_\sigma
\ge\gamma_\epsilon
-3r_R-\frac{3(T-1)S(R+1)}{\mu}.
```

Combining (17) and (19), and using
$`NS(R+1)\le R^2S(R+1)\le M_R`$, gives

**Equation (20).**

```math
\gamma_\epsilon
\le3r_R+(C_c+3)\frac{TM_R}{\mu N}.
```

This proves the explicit bound (8). Since $`r_R\to0`$, for all sufficiently large $`N`$,

**Equation (21).**

```math
T\ge\frac{\gamma_\epsilon}{2(15+18/c)}
\frac{\mu N}{M_R}.
```

The threshold depends on the stationary age tail. This dependence is not uniform over all finite-mean gap laws.

## Upper bound with a deterministic call budget

The proof has three components: a bounded-time synchronization step, an iid sequence of paired-interval trials, and a deterministic truncation of their total cost. Correlation between a trial's success and its duration is allowed throughout.

### Reaching the first observed renewal

Let $`F=\min\{t\ge1:Z_t=1\}`$. Conditional on $`A_1=a`$,

```math
\Pr(F>w\mid A_1=a)
=\frac{S(a+w+1)}{S(a+1)}.
```

Averaging against the [stationary age law (3)](model.md#exact-renewal-convention) gives the exact residual tail

**Equation (22).**

```math
\Pr(F>w)=\frac1\mu\sum_{\ell=w+1}^{\infty}S(\ell).
```

Because $`\mu<\infty`$, choose a fixed integer $`w_{\epsilon/3}`$ making this at most $`\epsilon/3`$. Issue charged dummy calls until the first event, aborting and outputting 0 if the timeout is reached without one. This costs at most $`w_{\epsilon/3}`$ queries. Following the first event, all complete gaps are iid copies of $`L`$, independent of the initial waiting period.

The mean of $`F`$ is not required to be finite. The timeout is a fixed law-dependent quantile, not a bound on its expectation.

### One paired-interval trial

Assume $`N\ge64`$, let

```math
\theta_N=\arcsin(1/\sqrt N),
\qquad K=\lfloor\sqrt N/8\rfloor\ge1.
```

Starting immediately after an event, use the next two complete intervals as one trial.

**Search interval.** Prepare the uniform index state and the answer qubit $`|-\rangle`$. For each query, apply the phase query using the XOR oracle. If the returned flag is 1, immediately measure the index, before applying diffusion. If the flag is 0, apply diffusion. After $`K`$ such complete Grover iterations, measure the index and store the candidate. If this cap was reached before the interval ended, use dummy calls until its terminal event.

**Verification interval.** At its first query, put the stored candidate in the index register and the answer qubit in $`|0\rangle`$, make one XOR query, and measure the answer. A basis-index query is unaffected by index pinching, so verification is exact even if this interval has length one. Retain any verified mark, then make dummy calls until the interval's terminal event.

On an interval of length $`\ell\le K`$, precisely $`\ell-1`$ full Grover iterations precede the flagged oracle call. That last oracle changes phases but not index probabilities; subsequent pinching also preserves these probabilities. The candidate is therefore marked with probability

**Equation (23).**

```math
q_N(\ell)=\sin^2((2\ell-1)\theta_N),\qquad \ell\le K.
```

If $`\ell>K`$, the first $`K`$ calls were unflagged, so the probability is

**Equation (24).**

```math
q_N(\ell)=\sin^2((2K+1)\theta_N),\qquad \ell>K.
```

At $`\ell=K`$, equation (23), not (24), applies. This distinction accounts for the missing final diffusion at a flagged query.

All angles in (23)–(24) lie in $`[0,\pi/2]`$. The inequalities
$`\theta_N\ge1/\sqrt N`$, $`\theta_N\le2/\sqrt N`$,
$`K\ge\sqrt N/16`$, and $`\sin y\ge2y/\pi`$ on this range give

**Equation (25).**

```math
q_N(\ell)\ge c_0\min\{\ell^2/N,1\},
\qquad c_0=\frac1{16\pi^2}.
```

For $`\ell\le K`$, one can use the stronger coefficient $`4/\pi^2`$ in front of $`\ell^2/N`$; for $`\ell>K`$, the angle is at least $`1/8`$, giving the stated uniform constant.

Because $`R^2\le4N`$,

```math
\mathbb E\min\{L^2/N,1\}
\ge\frac{M_R}{R^2}\ge\frac{M_R}{4N}.
```

Thus a trial succeeds with probability at least

**Equation (26).**

```math
\beta_N=b\frac{M_R}{N},\qquad b=\frac1{64\pi^2}.
```

Its total cost is $`L_{2k-1}+L_{2k}`$, of mean $`2\mu`$. Verification is already included in that cost. On the zero input no trial ever verifies a mark.

### Deterministic truncation

Consider a predetermined number

**Equation (27).**

```math
m=\left\lceil\beta_N^{-1}\log\frac3\epsilon\right\rceil
```

of trials. The algorithm can retain a found mark and still continue its planned trials, or one can define this continuation only for analysis. Fresh gap pairs and freshly prepared search registers give independent trial rewards for each fixed input. Therefore, on a unique-mark input, the probability that none succeeds is at most

**Equation (28).**

```math
(1-\beta_N)^m\le e^{-\beta_Nm}\le\epsilon/3.
```

Let $`C_m=\sum_{k=1}^{2m}L_k`$. Its expectation is $`2\mu m`$. Impose a post-synchronization budget

```math
B=\left\lceil6\mu m/\epsilon\right\rceil.
```

Markov's inequality gives

**Equation (29).**

```math
\Pr(C_m>B)\le\epsilon/3.
```

If the hard budget is reached, return a previously verified mark if one exists, and otherwise return 0. On the joint event that synchronization succeeds, all planned trials fit, and at least one trial succeeds, the output is correct. The union bound using (22), (28), and (29) gives error at most $`\epsilon`$. It does not assume that trial cost and reward are independent. On input $`0^N`$, the output is always correct.

The worst-case number of calls is at most $`w_{\epsilon/3}+B`$, establishing (9). Since $`M_R\le R\mu`$,

**Equation (30).**

```math
\frac{\mu N}{M_R}\ge\frac NR\ge\frac12\sqrt N.
```

The initial quantile and ceiling terms can therefore be absorbed into a fixed-law asymptotic constant. This proves the upper half of (7) and completes Theorem 1.

## Consequences and boundary

Replacing $`R^2=\lceil\sqrt N\rceil^2`$ by $`N`$ changes the truncated moment by at most a constant factor. The familiar form is therefore $`Q_\epsilon(N;L)=\Theta(\mu N/\mathbb E\min\{L^2,N\})`$. The [power-law and logarithmic examples](examples.md) evaluate it explicitly. The condition on $`h(a)`$ is global: the [comparisons](comparisons.md) show why an eventual tail asymptotic, or a finite gap variance alone, cannot replace it. Constants and the onset in $`N`$ depend on the fixed law and fixed error.

The result assumes the law is known for choosing the synchronization timeout, the number of trials, and the total query budget. The Grover cap $`K=\lfloor\sqrt N/8\rfloor`$ depends on $`N`$ alone. The theorem does not establish optimal noise-law learning, optimal error dependence, or a result uniform over noise laws that vary with $`N`$.
