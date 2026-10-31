# Search at predictable low-risk ages

[Science guide](README.md) · [Repository](../README.md)

A fixed stationary noise law can support coherent search across many renewal cycles. The algorithm stores its logical state in protected workspace and exposes that state to the oracle only at ages with a sufficiently small conditional event probability. Calls at other ages still advance the clock and are charged.

Throughout, use the oracle, error criterion, stationary initialization, and resource conventions in the [model](model.md). The initial age is hidden, flags arrive after their calls, and the input has zero or one marked index. The gap law is fixed independently of $`N`$. Write $`S(\ell)=\Pr(L\ge\ell)`$, $`\mu=\mathbb E L`$, and $`\pi(a)=S(a+1)/\mu`$ as in that model.

## Alternating-hazard theorem

Fix

```math
\alpha>1,\qquad
\beta>\max\{1,\alpha-1\},\qquad
0<c_L<\tfrac12.
```

Define the hazard at every nonnegative integer age by

```math
h(a)=
\begin{cases}
c_L(a+2)^{-\beta},&a\text{ even},\\[2pt]
\min\{\tfrac12,\,2\alpha/(a+2)\},&a\text{ odd}.
\end{cases}
```

The survival probabilities are

```math
S(1)=1,\qquad
S(\ell)=\prod_{a=0}^{\ell-2}(1-h(a)).
```

**Theorem 2.** For every fixed $`0<\epsilon<1/2`$, the optimal deterministic query cap for error at most $`\epsilon`$ is

```math
Q_\epsilon(N;L)=
\Theta_{\alpha,\beta,c_L,\epsilon}
\left(N^{\,1/2+(\alpha-1)/(2\beta)}\right).
```

The lower bound permits arbitrary adaptive algorithms, arbitrary protected quantum memory, and even free revelation of the initial age. The upper bound has the initial age hidden and counts every active, dummy, startup, and verification call.

The law has positive probability at every positive integer gap length and satisfies

```math
S(\ell)\sim C\ell^{-\alpha}
\quad\text{for some }C>0.
```

Its mean is finite, and its gap variance is finite exactly when $`\alpha>2`$. For example, $`\alpha=3`$ and $`\beta=4`$ give $`\Theta(N^{3/4})`$ search with finite gap variance and a stationary event rate that is positive and independent of $`N`$.

### Survival asymptotics

Every hazard is strictly between zero and one. The sum of the even-age hazards converges because $`\beta>1`$. Beyond a finite prefix, the odd-age hazards equal $`2\alpha/(a+2)`$, and

```math
2\alpha
\sum_{\substack{0\le a\le\ell-2\\a\text{ odd}}}
\frac1{a+2}
=\alpha\log\ell+C_0+o(1).
```

The sum of squared hazards also converges. Using
$`\log(1-h)=-h+O(h^2)`$ beyond a finite prefix shows that

```math
\log S(\ell)+\alpha\log\ell
```

converges to a finite real number. This proves the positive asymptotic coefficient. Since $`S(\ell)\to0`$, the gap probabilities sum to one; since each hazard is positive, every gap has positive probability.

The discrete tail-sum formula now gives $`\mathbb E L<\infty`$. More generally, for every $`r>0`$, $`\mathbb E L^r`$ is finite exactly when $`r<\alpha`$.

## Lower bound for adaptive algorithms

Use the [stationary hazard bound (P)](progress-bound.md#stationary-hazard-bound). Its relevant quantity is

```math
B_N=\sum_{a\ge0}\pi(a)
\min\{\sqrt N,h(a)^{-1}\}.
```

Put $`K=\sqrt N`$ and $`U=K^{1/\beta}`$. Apart from a fixed finite prefix,
$`\pi(a)\asymp(a+1)^{-\alpha}`$. On even ages,
$`h(a)^{-1}=c_L^{-1}(a+2)^\beta`$. Their contribution is therefore

```math
\begin{aligned}
\sum_{a\text{ even}}\pi(a)\min\{K,h(a)^{-1}\}
&\asymp
\sum_{\substack{a\le U\\a\text{ even}}}
 (a+1)^{\beta-\alpha}
+K\sum_{\substack{a>U\\a\text{ even}}}
 (a+1)^{-\alpha}\\
&\asymp
U^{\beta-\alpha+1}+KU^{1-\alpha}\\
&\asymp K^{\,1-(\alpha-1)/\beta}.
\end{aligned}
```

The assumption $`\beta>\alpha-1`$ ensures
$`\beta-\alpha+1>0`$. The odd-age contribution has order at most

```math
\begin{cases}
K^{2-\alpha},&1<\alpha<2,\\
\log K,&\alpha=2,\\
1,&\alpha>2.
\end{cases}
```

It is smaller than the even-age contribution. When $`1<\alpha<2`$, the difference between the two power exponents is
$`(\alpha-1)(1-1/\beta)>0`$; the other cases follow because
$`1-(\alpha-1)/\beta>0`$. Thus

```math
B_N\asymp K^{\,1-(\alpha-1)/\beta}.
```

Bound (P) gives $`T=\Omega_\epsilon(N/B_N)`$, which is the claimed lower bound. The source inequality and its application with the initial-age register are established in [the progress-bound proof](progress-bound.md); no restriction to restarted Grover algorithms is made here.

## Causal query policy

It suffices to describe sufficiently large $`N`$. A classical scan handles the finitely many smaller sizes with a law- and error-dependent constant.

Let

```math
\vartheta_N=\arcsin(N^{-1/2}),\qquad
M=\operatorname{round}
\left(\frac{\pi}{4\vartheta_N}-\frac12\right).
```

The [ordinary Grover rotation](../references/related-work.md#earlier-noisy-search-algorithms-and-lower-bounds) has marked-state amplitude
$`\sin((2M+1)\vartheta_N)`$ after $`M`$ iterations. Rounding gives
$`|(2M+1)\vartheta_N-\pi/2|\le\vartheta_N`$, so its failure probability is at most $`1/N`$. In particular, $`M=\Theta(\sqrt N)`$.

Fix $`\eta=\epsilon/5`$, and choose

```math
A=\max\left\{
2,\,
\left\lceil(c_LM/\eta)^{1/\beta}\right\rceil
\right\}.
```

After the first observed flag, the age is known. Use this policy:

1. Prepare the uniform logical search state in a protected register $`S`$. Keep the physical query index $`I`$ in a fixed basis state $`|j\rangle`$ when it is not being used for search.
2. A call is active when its pre-query age is even and lies in $`[A,2A]`$, until $`M`$ active calls have been made. Swap $`S`$ into $`I`$, set the answer qubit to $`|-\rangle`$, apply one ordinary XOR query, apply the known Grover diffusion, and swap the logical state back into $`S`$.
3. At every other age, make a charged dummy query on $`|j\rangle|+\rangle`$. The XOR oracle and any index pinching both leave this state unchanged. The stored logical state is untouched.
4. After $`M`$ active calls, measure $`S`$. Use one further charged query on the measured basis index with answer $`|0\rangle`$ to verify the candidate. Output the index if verification returns one; otherwise output `none`.

Known single-qubit gates switch the answer between $`|+\rangle`$ and $`|-\rangle`$. This does not require a controlled-oracle primitive. The policy can continue after an active flag; those histories count as possible failures. The choice of an active call uses only information available before that call.

## Error on active calls

At every active call, the conditional event probability is at most

```math
h(A_t)\le c_LA^{-\beta}\le\eta/M.
```

Let $`\tau_j`$ be the physical time of the $`j`$th active call under the policy without a deadline. The event $`\{\tau_j=t\}`$ is measurable before call $`t`$. These times are almost surely finite, as follows from the productive-cycle argument below. Hence

```math
\Pr(Z_{\tau_j}=1)
=\sum_t\mathbb E
\left[\mathbf1_{\{\tau_j=t\}}h(A_t)\right]
\le\eta/M.
```

A union bound gives probability at most $`\eta`$ that any of the first $`M`$ active calls is dephased. Independence of these events is unnecessary. If none is dephased, the logical register undergoes exactly $`M`$ ideal Grover iterations, with identity operations on that register between active calls.

## Charged cost and a fixed deadline

Immediately after an observed flag, let $`L_1,L_2,\ldots`$ be the fresh iid cycle lengths. A cycle with

```math
L_j\ge2A+2
```

contains every even-age slot in $`[A,2A]`$ before its terminal event. It supplies

```math
e_A=\lfloor A/2\rfloor+1\ge A/2
```

active slots if they are still needed. Such a cycle has probability

```math
q_A=S(2A+2)\asymp A^{-\alpha}.
```

Qualification is used only to analyze the cost. The algorithm never receives advance knowledge of a cycle length.

Put $`r=\lceil M/e_A\rceil`$, and let $`J`$ be the number of cycles required to encounter $`r`$ qualifying ones. Then $`\mathbb E J=r/q_A`$. Let $`W`$ be the number of physical calls, measured from this renewal boundary, needed to complete the $`M`$th active call. Pathwise,
$`W\le\sum_{j=1}^J L_j`$. Moreover,

```math
\begin{aligned}
\mathbb E\sum_{j=1}^J L_j
&=\sum_{j\ge1}
\mathbb E\!\left[L_j\mathbf1_{\{J\ge j\}}\right]\\
&=\mu\sum_{j\ge1}\Pr(J\ge j)\\
&=\mu r/q_A.
\end{aligned}
```

The event $`\{J\ge j\}`$ depends only on earlier cycles, so it is independent of $`L_j`$. Nonnegativity justifies exchanging expectation and the sum. This argument allows a cycle's length and qualification to be correlated.

It follows that

```math
\mathbb E W
\le C\mu\left(MA^{\alpha-1}+A^\alpha\right)
=O\left(M^{1+(\alpha-1)/\beta}\right).
```

The last equality uses $`\beta>1`$, so $`A=o(M)`$. Choose a deterministic deadline

```math
B=\left\lceil\frac{\mu r}{\eta q_A}\right\rceil,
```

or any known constant upper bound of the same order. Markov's inequality gives
$`\Pr(W>B)\le\eta`$. If $`M`$ active calls have not been completed by the deadline, output `none`. Reserve one further call for verification. The bound counts all dummy calls, including those in unsuccessful cycles.

## Stationary startup

Let $`R`$ be the number of calls until the first flag from the hidden stationary initial age. The renewal identity is

```math
\Pr(R>t)=\frac1\mu\sum_{\ell\ge t+1}S(\ell).
```

The right side tends to zero because $`\mu<\infty`$, even when $`\mathbb E R=\infty`$. Choose a fixed integer $`T_0`$, depending only on the law and $`\eta`$, such that
$`\Pr(R>T_0)\le\eta`$. Issue charged basis dummy calls until the first flag or this timeout. On timeout, output `none`. Otherwise start the causal policy immediately after that flag, with fresh iid cycles.

The total deterministic query cap is

```math
T_0+B+1.
```

For a marked input, failure is contained in the union of startup failure, a dephased active call, deadline failure, and ideal Grover failure. For $`N\ge1/\eta`$, their total probability is at most $`4\eta<\epsilon`$. This union bound does not require the events to be independent. On the zero input, verification never accepts, so the output is always correct.

Since $`T_0`$ is independent of $`N`$ and
$`M=\Theta(\sqrt N)`$, the cap has the order asserted in the theorem.

## Finite-prefix changes

The exponent is unchanged if a fixed finite prefix of the hazard sequence is replaced by other hazards strictly between zero and one, while the later hazards remain those of the stated construction.

Such a change multiplies the eventual survival sequence by a positive constant. The contribution of the changed prefix to $`B_N`$ is $`O(1)`$, since its hazards remain positive. The lower-bound asymptotics therefore persist. For the upper bound, choose the active window above the changed prefix; this affects only fixed constants and finitely many small values of $`N`$.

This observation is used in the [equal-mean and equal-tail construction](comparisons.md#full-support-laws-with-equal-mean-and-tail).

## Other resources and scope

The policy uses two $`O(\log N)`$-qubit index registers, an answer qubit, and standard state-preparation and diffusion ancillas. Total quantum space is $`O(\log N)`$. The uniform state is independent of the input and is prepared with known gates. Diffusion uses that preparation, a known zero-state reflection, and the inverse of the known preparation. For power-of-two $`N`$, the preparation consists of Hadamards; for general $`N`$, known rotations suffice.

The age counter may saturate at $`2A+1`$ until the next flag. All counters use $`O(\log N)`$ bits, and the output contains one index and the distinction between that index and `none`. The state preparations, answer-state changes, swaps, diffusion, measurements, and classical counter updates are known input-independent operations. They require no data-loading or QRAM oracle. The complexity theorem counts oracle calls, with the separate implementation limits stated in the [resource interpretation](interpretation.md); it does not assert an optimal gate count or physical running time. Efficiently computable fixed parameters, including rational choices of $`\alpha,\beta,c_L`$, suffice.

The result uses the protected memory, post-query flags, and query-driven clock specified in the [model](model.md). It assumes a known fixed noise law and proves the zero-or-one marked-item promise. It does not establish a corresponding theorem for unknown-law learning, unflagged noise, noise on all memory, a wall-clock bath, or several marked items.

The parameter condition is $`\beta>\max\{1,\alpha-1\}`$. At the excluded boundary $`\beta=\alpha-1>1`$, the same stationary hazard estimate gives $`\Omega(N/\log N)`$, while this single-window policy gives only $`O(N)`$. A matching critical-boundary theorem is not asserted.
