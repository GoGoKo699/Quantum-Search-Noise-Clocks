# Learning Quantum Search Noise Clocks

[Repository overview](../README.md) · [Scientific account](../science/README.md)

Imagine searching a list with a quantum device whose query register is occasionally dephased. A flag reports each event after the query. The intervals between events matter, but so does the conditional risk of the next event at the age the clock has reached. Protected memory makes that distinction operational: a search state can remain stored during a risky call and take part in a later, safer call. Every call still costs one query.

The learning route develops the two questions answered by the science. When does a truncated second moment of the event spacing determine optimal search cost? How can two clocks with equal mean spacing and the same leading survival tail nevertheless yield different search exponents?

## One anchor and a bridge

The educational anchor is **Andrew M. Childs, *Lecture Notes on Quantum Algorithms*, 17 April 2025**. The [anchor guide](anchor.md) identifies the relevant sections. Its role is to supply the quantum-query and Grover foundations needed for this project, with focused reading rather than an entire-book prerequisite.

The [source-to-project bridge](bridge.md) translates notation, explains the physical query register and protected logical state, and supplies the renewal-clock ideas that the anchor does not develop. It also identifies the research-level progress inequality imported from Agarwal, Rao and Song. That ingredient remains an explicitly cited proof dependency.

## Thirty understanding targets

The [milestone map](milestones.md) contains exactly **M01–M30**. Each entry states a central question, an understanding target, dependencies, a conceptual connection and source pointers. The allocation follows this project's combination of quantum algorithms and renewal timing:

| Phase | Milestones | Development |
|---|---|---|
| Background and preliminaries | M01–M14 | From individual queries and noise events to the complete adaptive search and stationary-clock framework. |
| Narrative and innovation | M15–M30 | From the proof ingredients and causal scheduling mechanisms to the two optimal-cost results, matched comparisons and their scope. |

The map is independent of a reader's assessment history. It provides global understanding of the contribution; specialist calculations and full proofs have their authoritative homes in [science](../science/README.md).

## Choose a reading route

| Aim | Route |
|---|---|
| Understand the mechanism first | Read the [bridge](bridge.md), then [predictable useful queries](../science/predictable-queries.md) and [matched comparisons](../science/comparisons.md). |
| Build the framework in order | Use [M01–M14](milestones.md), then follow the narrative phase and its prerequisite links. |
| Inspect the complete proofs | Start with the [model](../science/model.md), [imported progress bound](../science/progress-bound.md), and the two theorem pages in the [science guide](../science/README.md). |
| Check a concrete implementation detail | Run the [channel and renewal checks](../verification/README.md), then compare their bounded conclusions with the analytical proofs. |

Keep the model's conditions attached to each explanation: zero or one marked item, a fixed known law, flags after queries, noise on the physical index only, protected memory, and a clock advanced by every physical call. The distinction between matching a mean and leading tail and matching an entire stochastic process is central to the final synthesis.
