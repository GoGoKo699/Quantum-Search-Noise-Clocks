# Equal means and tails can yield different search costs

[Science guide](README.md) · [Repository](../README.md)

The [renewal resource law](renewal-law.md) assumes a lower bound on the hazard at every reachable age. The examples below explain why that condition is substantive. They use the same [stationary flagged-dephasing model](model.md), the same zero-or-one marked-item promise, and a fixed noise law independent of $`N`$.

The first comparison preserves the entire eventual survival sequence and the mean, but introduces one guaranteed clean slot. The second keeps every gap probability positive and matches both the mean and the asymptotic tail coefficient. Its optimal search exponents still differ.

## One forbidden gap

Fix $`\alpha>1`$. Start with the smooth Pareto law

```math
p_\ell=\ell^{-\alpha}-(\ell+1)^{-\alpha},
\qquad \ell\ge1.
```

Define a new law by changing only three masses:

```math
p'_1=p_1+\tfrac12p_2,\qquad
p'_2=0,\qquad
p'_3=p_3+\tfrac12p_2,\qquad
p'_\ell=p_\ell\quad(\ell\ge4).
```

Normalization is preserved. The mean is exactly unchanged, since the removed mass at length two is split equally between lengths one and three. If $`S'(\ell)=\Pr(L'\ge\ell)`$, then

```math
S'(\ell)=S(\ell)=\ell^{-\alpha}
\qquad\text{for every }\ell\ge4.
```

The two laws have the same stationary event rate, tail exponent, tail coefficient, and moment-finiteness thresholds. However,
$`h'(1)=0`$: after the first call of a cycle is unflagged, its second call is guaranteed to be clean.

**Proposition.** For every fixed $`0<\epsilon<1/2`$, the modified law has

```math
Q_\epsilon(N;L')=\Theta_{\alpha,\epsilon}(\sqrt N)
```

with a hidden stationary initial age and a deterministic cap counting all calls.

### Causal algorithm and cost

Set $`\eta=\epsilon/5`$. Use the [stationary first-flag startup](predictable-queries.md#stationary-startup), with a fixed charged timeout $`T_0`$ whose failure probability is at most $`\eta`$.

After the first observed flag, keep the logical search state in protected workspace. Issue a dummy query at age zero. If it is flagged, a new cycle starts. If it is unflagged, use the next call, at age one, for one ideal Grover iteration. That call is clean because $`L'\ne2`$. Park the logical state and use dummy calls for the remainder of the cycle.

Accumulate

```math
M=\operatorname{round}
\left(\frac{\pi}{4\arcsin(N^{-1/2})}-\frac12\right)
=\Theta(\sqrt N)
```

active calls. Then measure the logical register and verify the candidate with one charged basis query. Verification is exact despite index dephasing. Output the candidate if it is marked; otherwise output `none`. The known swaps, state preparation, and answer states are those of the [causal query policy](predictable-queries.md#causal-query-policy).

A cycle supplies one active call precisely when $`L'\ge3`$. Its fixed positive probability is

```math
q=\Pr(L'\ge3)=S(3)+\tfrac12p_2>0.
```

Let $`J`$ count cycles until $`M`$ eligible cycles have occurred. Then
$`\mathbb E J=M/q`$. Since $`\{J\ge j\}`$ depends only on earlier cycles,

```math
\mathbb E\sum_{j=1}^J L'_j
=\sum_{j\ge1}
\mathbb E\!\left[L'_j\mathbf1_{\{J\ge j\}}\right]
=\mu\sum_{j\ge1}\Pr(J\ge j)
=\frac{\mu M}{q}.
```

Choose a deadline

```math
B=\left\lceil\frac{\mu M}{\eta q}\right\rceil
```

for completing the $`M`$th active call, and output `none` if it is missed. Markov's inequality bounds deadline failure by $`\eta`$. The total cap, including startup and verification, is $`T_0+B+1=O(\sqrt N)`$. All active calls are clean. For sufficiently large $`N`$, the ideal Grover failure is at most $`1/N\le\eta`$, so the total failure probability is at most $`3\eta<\epsilon`$. A classical scan handles finitely many smaller sizes. The zero input is always answered correctly.

### Lower bound and implication

The [stationary hazard bound (P)](progress-bound.md#stationary-hazard-bound), with $`h^{-1}=+\infty`$ at a zero hazard, has $`B_N\le\sqrt N`$. It therefore gives $`\Omega_\epsilon(\sqrt N)`$ for every adaptive algorithm, proving the proposition.

For every age $`a\ge3`$, the modified hazard agrees exactly with the original smooth hazard. Thus even the eventual relation $`h(a)\sim\alpha/a`$ is insufficient to extend the renewal resource theorem to all finite prefixes. One reachable finite age with a guaranteed clean slot permits coherent progress across many cycles, because the logical state can be protected on all intervening calls.

## Full-support laws with equal mean and tail

Fix

```math
\alpha>1,\qquad
\beta>\max\{1,\alpha-1\},\qquad
0<c_L<\tfrac12.
```

Let $`P_s`$ be the smooth Pareto law and $`P_a`$ the [alternating-hazard law](predictable-queries.md#alternating-hazard-theorem). Both have positive mass at every positive integer. Write their finite means as $`\mu_i`$ and their positive tail coefficients as $`C_i`$, so

```math
S_i(\ell)\sim C_i\ell^{-\alpha},
\qquad i\in\{s,a\},
```

with $`C_s=1`$.

Choose any

```math
0<c_*<\min\{C_s,C_a\},
\qquad
\lambda_i=c_*/C_i\in(0,1).
```

Choose a common target mean satisfying

```math
\mu_*>
\max_{i\in\{s,a\}}
\{\lambda_i\mu_i+1-\lambda_i\},
```

and define

```math
m_i=\frac{\mu_*-\lambda_i\mu_i}{1-\lambda_i}>1.
```

Choose an integer $`R_0>\max\{m_s,m_a\}`$. On the two gap lengths
$`\{1,R_0\}`$, define

```math
\nu_i(R_0)=\frac{m_i-1}{R_0-1},
\qquad
\nu_i(1)=\frac{R_0-m_i}{R_0-1}.
```

These are strictly positive probabilities with mean $`m_i`$. Set

```math
\widetilde P_i
=\lambda_iP_i+(1-\lambda_i)\nu_i.
```

Let $`\widetilde L_i`$ have law $`\widetilde P_i`$.

Both laws retain full support, because $`\lambda_i>0`$ and $`P_i`$ has full support. Their means are exactly

```math
\mathbb E_{\widetilde P_i}L
=\lambda_i\mu_i+(1-\lambda_i)m_i
=\mu_*.
```

For every $`\ell>R_0`$,

```math
\widetilde S_i(\ell)=\lambda_iS_i(\ell).
```

Their tails therefore have the same asymptotic coefficient:

```math
\widetilde S_s(\ell)\sim
\widetilde S_a(\ell)\sim
c_*\ell^{-\alpha}.
```

Their stationary event rates are both $`1/\mu_*`$. For every age $`a\ge R_0`$, the two survival factors in the hazard ratio have the same multiplier $`\lambda_i`$, so

```math
\widetilde h_i(a)=h_i(a).
```

Only a finite prefix of each hazard sequence has changed, and every changed hazard remains strictly between zero and one.

### The search exponents persist

The [finite-prefix argument](predictable-queries.md#finite-prefix-changes) preserves the alternating law's optimal cost:

```math
Q_\epsilon(N;\widetilde L_a)
=\Theta\left(
N^{\,1/2+(\alpha-1)/(2\beta)}
\right).
```

For the smooth law, its unchanged eventual hazard is comparable to $`1/(a+1)`$. Every hazard in its changed finite prefix is positive. Taking the minimum over that prefix and an eventual lower bound gives a constant $`c>0`$ such that

```math
\widetilde h_s(a)\ge\frac{c}{a+1}
\qquad\text{for every }a\ge0.
```

The [renewal resource theorem](renewal-law.md) applies. Its truncated second moment has the orders computed in the [power-law examples](examples.md), yielding

```math
Q_\epsilon(N;\widetilde L_s)=
\begin{cases}
\Theta(N^{\alpha/2}),&1<\alpha<2,\\
\Theta(N/\log N),&\alpha=2,\\
\Theta(N),&\alpha>2.
\end{cases}
```

All constants may depend on the fixed laws and on $`\epsilon`$. Both costs are deterministic query caps with stationary hidden-age startup and all oracle calls charged.

For $`1<\alpha<2`$, the difference between the two power exponents is
$`(\alpha-1)(1-1/\beta)/2>0`$. At $`\alpha=2`$, the alternating exponent is strictly below one, so it also beats $`N/\log N`$. For $`\alpha>2`$, the condition $`\beta>\alpha-1`$ again makes the alternating exponent strictly below one.

### A finite-variance example

Choose $`\alpha=3`$, $`\beta=4`$, and, for example, $`c_L=1/4`$. The construction produces two full-support stationary laws with

```math
\mathbb E\widetilde L_s=\mathbb E\widetilde L_a=\mu_*,
\qquad
\Pr(\widetilde L_s\ge\ell)\sim
\Pr(\widetilde L_a\ge\ell)\sim c_*\ell^{-3},
```

but

```math
Q_\epsilon(N;\widetilde L_s)=\Theta(N),
\qquad
Q_\epsilon(N;\widetilde L_a)=\Theta(N^{3/4}).
```

Both gap distributions have finite variance. Their positive stationary event rate is identical, and no finite age has zero hazard. The faster policy uses small conditional hazards at suitable ages while storing its logical state during other charged calls.

## What is matched

The full-support pair has exactly equal means and asymptotically equal survival tails, including the leading coefficient. It consequently has the same thresholds for finiteness of moments. It need not have equal numerical values of higher finite moments, and its entire eventual survival sequences need not coincide.

The one-forbidden-gap comparison does preserve the entire survival sequence from length four onward. Its changed probabilities create one zero hazard. Together, the two constructions separate the roles of the gap tail and the conditional event hazard under the [specified information and memory resources](model.md).

The full-support comparison uses only the strict power regime
$`\beta>\max\{1,\alpha-1\}`$. It does not rely on a matching theorem at the excluded critical boundary. These examples establish no claims for unflagged noise, unprotected memory, several marked items, or a different physical clock.
