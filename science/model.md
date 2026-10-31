# Model and charged resources

[Science guide](README.md) · [Repository](../README.md)

The noise channel and flag timing follow [Agarwal–Rao–Song, Section 6.1](https://arxiv.org/html/2610.00506v2). The additional assumption is a stationary renewal law for the event sequence. All results concern the same operational model below.

### Search and allowed computation

The unknown input belongs to

```math
\mathcal X_N=\{0^N,e_1,\ldots,e_N\}.
```

An algorithm must output 0 on input $`0^N`$, and output $`j`$ on input $`e_j`$, with probability at least $`1-\epsilon`$ for each input, where $`0<\epsilon<1/2`$. Probabilities average over the noise and the algorithm's randomness. Let $`Q_\epsilon(N;L)`$ denote the smallest worst-case number of oracle calls that achieves this task in the noise model defined below.

One call first applies the standard XOR oracle

```math
O_x|i,b\rangle=|i,b\oplus x_i\rangle,
\qquad i\in[N],\quad b\in\{0,1\}.
```

The algorithm may use arbitrary input-independent gates, measurements, resets, classical control, and auxiliary quantum memory between calls. Auxiliary memory is noiseless in this model. Every call, including a call made on a fixed basis index solely to advance the clock, costs one query. Free gates or physical waiting do not advance the noise clock.

The resource statement concerns oracle calls. Uniform-state preparation and the diffusion reflection use known transformations on the index register; no data-loading or QRAM oracle is supplied. The output is a classical index; the distinguished output 0 means no marked item and is written `none` in algorithm pseudocode. No gate-count, wall-clock, or physical implementation theorem is asserted. The renewal law is fixed and known to the algorithm; learning an unknown noise law is outside the statement.

Algorithms that halt early can be padded to a deterministic horizon with dummy queries on a separate basis-state query register, while preserving their stored output. Thus a fixed horizon can be used for the lower bound without restricting worst-case bounded-query algorithms.

### Index dephasing and its flag

At query $`t`$, an exogenous bit $`Z_t`$ determines the channel

```math
\mathcal O_{x,Z_t}(\rho)=
\begin{cases}
O_x\rho O_x^\dagger,&Z_t=0,\\
\Delta_I(O_x\rho O_x^\dagger),&Z_t=1,
\end{cases}
\qquad
\Delta_I(\rho)=\sum_{i=1}^N P_i\rho P_i,
\quad P_i=|i\rangle\langle i|_I\otimes I.
```

Only after this channel acts does the algorithm receive the classical flag $`Z_t`$. The index outcome implicit in $`\Delta_I`$ is inaccessible. An event therefore cannot be anticipated from its own flag and cannot be undone by retrying an omitted oracle call: the oracle has acted and the queried index has been pinched.

The initial age and all renewal draws are generated independently of the unknown input and the algorithm's initial state and private randomness. The algorithm's actions can correlate with past flags, but its actions and outcomes do not feed back into the noise. Conditional on the initial age and past flags, the next event has the prescribed renewal hazard, with no further dependence on past algorithm measurement outcomes, hidden index records, or the current query state.

### Exact renewal convention

Let $`L`$ be a positive-integer random variable with

```math
S(\ell)=\Pr(L\ge\ell),\qquad
\mu=\mathbb E L=\sum_{\ell\ge1}S(\ell)<\infty.
```

After each event, the number of calls up to and including the next event is an independent copy of $`L`$. Let $`A_t`$ be the age immediately before query $`t`$. It evolves as

**Equation (1).**

```math
A_{t+1}=\begin{cases}0,&Z_t=1,\\A_t+1,&Z_t=0.\end{cases}
```

At a reachable age $`a`$, meaning $`S(a+1)>0`$, the hazard is

**Equation (2).**

```math
h(a)=\Pr(L=a+1\mid L\ge a+1)
=1-\frac{S(a+2)}{S(a+1)}.
```

For example, if an event occurs at call $`t_0`$ and the next gap is $`\ell`$, then queries $`t_0+1,\ldots,t_0+\ell`$ have pre-query ages $`0,\ldots,\ell-1`$; the last of them is the next event.

The clock starts in its stationary distribution

**Equation (3).**

```math
\pi(a)=\Pr(A_1=a)=\frac{S(a+1)}{\mu},\qquad a\ge0.
```

This is a probability distribution because $`\mu<\infty`$. It is stationary for (1)–(2): for $`a\ge1`$, its incoming mass is
$`\pi(a-1)(1-h(a-1))=\pi(a)`$, and the incoming reset mass is
$`\sum_a\pi(a)h(a)=1/\mu=\pi(0)`$.

One equivalent initialization samples the containing gap and initial age jointly according to

```math
\Pr(L_\star=\ell,A_1=a)=\frac{\Pr(L=\ell)}{\mu},
\qquad 0\le a<\ell,
```

then uses iid fresh gaps after that gap ends. The initial age is not given to the algorithm. Giving it to the algorithm will nevertheless be permitted in the lower bound. Stationarity is a promise about the supplied noise environment, not a claimed algorithm for preparing a stationary environment.

The mean event rate is $`1/\mu`$. The gap containing the initial query is length-biased; it must not be treated as a fresh iid gap.

Continue to the [quantum progress bound](progress-bound.md), the [renewal resource law](renewal-law.md), or the [classical and implementation resource comparison](interpretation.md).
