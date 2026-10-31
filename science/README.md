# Scientific account

[Repository overview](../README.md)

A noise clock supplies two kinds of information: a distribution of time between events and a conditional risk after a particular observed history. This project determines optimal search cost for a broad renewal class and constructs clocks for which the conditional timing pattern changes that cost despite matching the mean and leading tail.

## Reading route

| Page | Scientific purpose |
|---|---|
| [Model and charged resources](model.md) | Zero-or-one-mark task, XOR oracle, index-only dephasing, post-query flags, stationarity and protected workspace. |
| [Quantum progress bound](progress-bound.md) | Exact imported ARS inequalities, initial-age hypothesis mapping, and the capped stationary hazard lower bound. |
| [Truncated-moment resource law](renewal-law.md) | Theorem 1, stopped lower bound and paired-interval upper with a hard query cap. |
| [Noise laws and regimes](examples.md) | Smooth power-law phase diagram, finite-variance implication with its hazard condition, and the logarithmic boundary example. |
| [Predictable useful queries](predictable-queries.md) | Full-support alternating-hazard theorem, causal protected-memory algorithm and matching lower bound. |
| [Matched comparisons](comparisons.md) | Exact mean/tail matching and the finite-prefix clean-slot obstruction. |
| [Operational meaning](interpretation.md) | Classical cost, memory and implementation resources, asymptotic onset, and the limits of the access model. |

The [related-work account](../references/related-work.md) states the proof lineage and the difference from the closest sources. [Verification](../verification/README.md) gives runnable channel and renewal checks with their actual outputs.

The [learning route](../learning/README.md) connects Childs's ideal-search foundations to these pages through one source bridge and a project-defined map of 30 milestones.

## Logical dependencies

The common model fixes the meaning of all query counts. The ARS local potential and terminal separation give two converse routes: a stopped occupation estimate for the global harmonic-hazard class, and a capped inverse-hazard estimate for the alternating family. Independent paired-interval trials match the first route. Coherent state parking and predictable active slots match the second. Finite-prefix probability mixtures then equalize the mean and leading tail without changing either asymptotic exponent.

Each proof has one authoritative page. Equation numbers within a proof refer to that page unless a link names the source page. Equations (1)–(3) define the common clock in the model, and equations (10)–(12) state and map the inherited quantum progress bound.
