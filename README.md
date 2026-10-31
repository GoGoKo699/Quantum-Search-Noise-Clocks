# Quantum Search Noise Clocks

How does the timing of noise determine the optimal cost of quantum search?

This repository studies a perfect query followed by occasional dephasing of the query-index register. Noise events follow a fixed stationary renewal clock, and their flags become available after each query. Protected quantum memory lets an algorithm decide when to expose its logical state. Every physical call, including synchronization, dummy and verification calls, is counted.

The task has zero or one marked item among $N$ positions. All rates below use a fixed noise law and fixed error $0<\epsilon<1/2$.

## Principal results

Let $L$ be the gap between events, $\mu=\mathbb E L<\infty$, and $h(a)$ the next-call event probability at age $a$.

**A sharp renewal law.** If $h(a)\ge c/(a+1)$ at every reachable age for a fixed $c>0$, then

$$
Q_\epsilon(N;L)=\Theta\!\left(
\frac{\mu N}{\mathbb E\min\{L^2,N\}}
\right).
$$

The [proof](science/renewal-law.md) combines a stopped quantum progress bound with a paired-interval search algorithm. Both bounds use a deterministic query budget and handle stationary initialization even when its residual waiting time has infinite mean.

**Equal rate and tail, different optimal search exponents.** Two full-support renewal clocks can have exactly the same mean gap and leading asymptotic survival tail, yet different search costs. A concrete parameter choice gives

$$
Q_{\rm smooth}(N)=\Theta(N),
\qquad
Q_{\rm alternating}(N)=\Theta(N^{3/4}).
$$

Both clocks have positive noise risk at every age and finite gap variance. Their mean event rate and asymptotic tail coefficient/exponent agree. The algorithm [parks its logical state](science/predictable-queries.md) during risky calls and accumulates Grover queries at predictable low-risk ages. The [matching construction](science/comparisons.md) gives exact equality of the mean and leading tail, without claiming equality of every higher numerical moment.

## Search regimes

| Fixed gap law | Optimal charged quantum queries |
|---|---:|
| Smooth survival $\Pr(L\ge\ell)=\ell^{-\alpha}$, $1<\alpha<2$ | $\Theta(N^{\alpha/2})$ |
| Smooth power law, $\alpha=2$ | $\Theta(N/\log N)$ |
| Smooth power law, $\alpha>2$ | $\Theta(N)$ |
| Survival $1/[\ell(1+\log\ell)^p]$, $p>1$ | $\Theta(\sqrt N(\log N)^p)$ |
| Alternating hazards, $\alpha>1$, $\beta>\max\{1,\alpha-1\}$ | $\Theta(N^{1/2+(\alpha-1)/(2\beta)})$ |

The [examples](science/examples.md) and [alternating theorem](science/predictable-queries.md) specify the complete laws and proofs. The classical cost is $\Theta(N)$ throughout this same oracle model.

## Read and reproduce

- Start with the [scientific guide](science/README.md) and [exact model](science/model.md).
- Go directly to the [resource theorem](science/renewal-law.md), [predictability theorem](science/predictable-queries.md), or [matched comparisons](science/comparisons.md).
- Read the [proof lineage and related work](references/related-work.md); the general correlated-noise model and quantum progress method are due to Agarwal–Rao–Song.
- Run the [scientific checks](verification/README.md):

```bash
python -m pip install -r verification/requirements.txt
python verification/check_models.py --output verification/results.json
```

The numerical checks test exact channel ordering, protected-memory parking, and finite renewal identities. They do not establish asymptotic optimality; that conclusion comes from the analytical proofs.

## Scope

The clock advances per oracle call, the workspace is protected, the flags arrive after each query, and the law is fixed and known. The theorems cover zero-or-one-mark search and fixed error. Constants and asymptotic onset can depend on the law. Results for unflagged noise, noise acting on all memory, unrestricted marked-set size, unknown-law learning, or physical wall-clock cost require separate analysis. See [operational meaning and boundaries](science/interpretation.md).

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
