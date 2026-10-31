# What timing information buys

[Science guide](README.md) · [Repository](../README.md)

The two algorithms use temporal structure in different ways. The paired-interval algorithm obtains a reward proportional to the square of a coherent run, up to Grover saturation. The protected-memory algorithm accumulates useful queries across many separate intervals, selecting each query from the conditional risk known before it. Both pay for every call that moves the clock.

## Quantities held equal

The [full-support comparison](comparisons.md) constructs two fixed stationary clocks with exactly the same mean gap, the same positive one-call event probability, and the same leading survival-tail coefficient and exponent. With $\alpha=3$ and $\beta=4$, their optimal costs are $\Theta(N)$ and $\Theta(N^{3/4})$. Both gap laws have finite variance.

Their higher finite moments need not have equal numerical values. Their entire survival sequences are not equal. The distinction lies in the conditional hazard at individual ages, which a past flag makes observable through a classical counter. The [separate clean-slot example](comparisons.md) preserves the entire eventual survival sequence, but permits a zero hazard at one reachable age.

The average single-query channel is the same for the matched pair: stationarity gives event probability $1/\mu$ in both. An adaptive algorithm does not experience independent draws of this average channel. It can correlate its choice to expose the logical state with the age learned from past flags. The lower bounds explicitly allow that adaptation.

## Classical search remains linear

A computational-basis query returns the oracle bit exactly even when the index is dephased, so a classical scan uses $N$ calls. Conversely, the flags are independent of the unknown marked position. On the all-zero input, fix the classical random seed and flag sequence. At most $T$ positions can be inspected in $T$ calls. Changing an unqueried position to the unique mark leaves that transcript unchanged.

Couple each singleton run to the zero-input run using the same random seed and flag sequence. For a uniformly chosen position $J$, the probability that the zero-input run outputs 0 and never queries $J$ is at least $1-\epsilon-T/N$. On that event, the singleton run has the same transcript and incorrectly outputs 0. Averaging over the position, seed, and flags, the singleton error is at most $\epsilon$, so every adaptive classical algorithm needs

$$
T\ge(1-2\epsilon)N.
$$

Thus the classical same-oracle cost is $\Theta(N)$ for every clock considered here. The quantum comparisons include the full synchronization and dummy-query cost.

## Protected memory is part of the model

During an inactive call, the physical query register is a fixed basis state. The logical Grover state remains in a different, protected register. Index dephasing therefore acts on a register carrying no logical coherence. Swaps move the logical state into the query register only for selected active calls. This mechanism relies on the [channel location specified in the model](model.md#index-dephasing-and-its-flag).

The algorithms use $O(\log N)$ qubits: one or two index registers, the answer qubit, and standard preparation and reflection ancillas. The result allows arbitrary workspace in its lower bounds, so these upper bounds do not derive from an imposed memory restriction. Age and query counters can be saturated or bounded by the deterministic horizon and require $O(\log N)$ bits asymptotically for each fixed law and error.

Known-state preparation, swaps and the diffusion reflection require no hidden-data oracle. For a power-of-two search space, standard ideal gate implementations have a polynomial logarithmic gate overhead per useful query; finite-precision synthesis adds its usual precision cost. The theorems count oracle calls and do not claim optimal gate count, fault-tolerant overhead, or laboratory wall-clock time.

## Asymptotic and operational boundaries

The law and target error are fixed before $N$ grows. A stationary residual interval can have infinite mean, so the proofs use a finite residual quantile for startup. This quantile may be large. The lower proof likewise has a law-dependent onset through the stationary age tail. Neither feature supplies a uniform practical speedup across all finite-mean laws.

The clock advances on physical queries. Passive waiting does not advance it, and dummy calls are counted. Past flags are available after each query; the measured index and future flags are inaccessible. All gates and the protected workspace are ideal. Noise that acts on all memory, advances during gates or idle wall-clock time, or lacks the stated flag is a different access model.

The task promises zero or one mark. The upper bounds use that promise to choose Grover run lengths. Multiple-mark search, learning an unknown noise law, sharp error dependence, and the critical alternating-hazard boundary $\beta=\alpha-1>1$ are outside the proved matching results. At that boundary the present estimates give only $\Omega(N/\log N)$ and $O(N)$.

## Scientific contribution and inherited framework

[Agarwal–Rao–Song](../references/related-work.md) already identify predictable conditional noise rates and supply the quantum progress framework for arbitrary exogenous correlated schedules. Earlier measurement and search work also establishes that temporal noise structure can matter. The contribution here is the matched stationary-renewal resource law, its treatment of rare old initial intervals, and the causal full-support constructions with matched rate and asymptotic tail but different optimal search exponents.

The [verification record](../verification/README.md) checks concrete channels, indexing and finite renewal identities. The all-algorithm lower bounds and asymptotic conclusions rest on the mathematical arguments, not on numerical fits.
