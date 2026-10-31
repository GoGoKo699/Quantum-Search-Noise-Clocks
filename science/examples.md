# Noise laws and search regimes

[Science guide](README.md) · [Repository](../README.md)

These examples evaluate the [renewal resource theorem](renewal-law.md) for fully specified fixed laws. The exponents are analytical consequences; the finite-size values in [verification](../verification/README.md) are illustrations.


## Smooth power-law gaps

For a fixed $`\alpha>1`$, define the entire survival function by

```math
S(\ell)=\ell^{-\alpha},\qquad \ell\ge1.
```

Every positive integer gap has positive probability. The mean is $`\mu=\sum_{\ell\ge1}\ell^{-\alpha}<\infty`$, and the conditional hazard is

```math
h(a)=1-\left(\frac{a+1}{a+2}\right)^\alpha
\ge\frac1{a+2}\ge\frac1{2(a+1)}.
```

The global condition of [Theorem 1](renewal-law.md) therefore holds. Its truncated moment has the exact sum and asymptotic orders

```math
M_R=\sum_{\ell=1}^{R}(2\ell-1)\ell^{-\alpha}
\asymp
\begin{cases}
R^{2-\alpha},&1<\alpha<2,\\
\log R,&\alpha=2,\\
1,&\alpha>2.
\end{cases}
```

These estimates follow from integral comparisons for the power sums. Substituting $`R=\lceil\sqrt N\rceil`$ gives

```math
Q_\epsilon(N;L)=
\begin{cases}
\Theta(N^{\alpha/2}),&1<\alpha<2,\\
\Theta(N/\log N),&\alpha=2,\\
\Theta(N),&\alpha>2.
\end{cases}
```

The law is held fixed as $`N`$ grows; its positive mean event rate does not decrease with problem size. A positive average dephasing rate is thus compatible with a sublinear search cost in this model. The quantum state is prepared afresh in each search trial, and all intervening verification and dummy calls are charged.

## Finite-second-moment laws within the hazard class

If $`\mathbb E L^2<\infty`$, monotone convergence gives $`M_R\to\mathbb E L^2`$. Under the global harmonic hazard condition, the optimal cost is consequently $`\Theta(N)`$. The hazard condition remains part of this implication. The [alternating-hazard construction](predictable-queries.md) has finite gap variance for $`\alpha>2`$ and can nevertheless have a smaller search exponent.


## A finite-mean logarithmic boundary

Fix $`p>1`$ and specify the entire survival function, including its small-argument behavior, by

**Equation (31).**

```math
S_p(\ell)=\frac{1}{\ell(1+\log\ell)^p},\qquad \ell\ge1.
```

It starts at one, decreases strictly to zero, and defines positive probability at every integer gap length. The integral test gives $`\mu_p<\infty`$. Its hazard obeys the global bound

**Equation (32).**

```math
\begin{aligned}
h_p(a)
&=1-\frac{a+1}{a+2}
\left(\frac{1+\log(a+1)}{1+\log(a+2)}\right)^p\\
&\ge\frac1{a+2}\ge\frac1{2(a+1)}.
\end{aligned}
```

Thus [Theorem 1](renewal-law.md) applies with $`c=1/2`$, without inferring a hazard asymptotic from a survival-tail asymptotic.

The [truncated-moment identity (5)](renewal-law.md) becomes

**Equation (33).**

```math
M_R=\sum_{\ell=1}^{R}
\frac{2-1/\ell}{(1+\log\ell)^p}
=\Theta_p\!\left(\frac{R}{(\log R)^p}\right).
```

For completeness, the lower estimate follows by retaining $`\ell\in[R/2,R]`$. For the upper estimate, the terms $`\ell\le\sqrt R`$ contribute $`O(\sqrt R)`$, and all later terms sum to at most $`2R/(1+\tfrac12\log R)^p`$. This proves the claimed order directly.

Consequently, for fixed $`p>1`$ and fixed $`\epsilon`$,

**Equation (34).**

```math
\boxed{
Q_\epsilon(N;L_p)
=\Theta_{p,\epsilon}\!\left(\sqrt N(\log N)^p\right).
}
```

This is one fixed, $`N`$-independent, stationary noise law with positive event rate $`1/\mu_p`$. Its stationary residual has infinite mean, but every fixed-error residual quantile is finite. The upper proof uses that quantile, and the lower proof uses $`r_R\to0`$; neither replaces it by a finite residual expectation.

The statement is asymptotic in $`N`$. Its constants and onset are not uniform as $`p\downarrow1`$ or $`\epsilon\downarrow0`$. It does not claim a uniformly small synchronization cost or a procedure for constructing the stationary environment.
