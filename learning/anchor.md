# Selected educational anchor

[Repository](../README.md) · [Learning bridge](bridge.md) · [Thirty-milestone map](milestones.md)

The selected anchor is **Andrew M. Childs, *Lecture Notes on Quantum Algorithms*, 17 April 2025**.

- [Official author page](https://www.cs.umd.edu/~amchilds/qa/)
- [Official PDF](https://www.cs.umd.edu/~amchilds/qa/qa.pdf)

The date is printed on the inspected PDF's cover. The document has 191 PDF pages. Links below use the PDF viewer's page count; printed page numbers are listed separately.

## Relevant passages

| Passage | Printed pages | Connection to this project |
|---|---:|---|
| [Sections 1.1–1.2: Quantum data; Quantum circuits](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=9) | 1 | State vectors, tensor-product registers, gates and measurement. |
| [Section 19.1: Unstructured search](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=95) | 87 | Search task and the two-reflection picture. |
| [Section 19.3: Amplitude amplification and quantum counting](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=96) | 88–89 | Amplification as a general algorithmic idea. |
| [Sections 21.1–21.2: Quantum query complexity; Quantum queries](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=105) | 97–98 | Query budgets, auxiliary registers, bit and phase oracle conventions. |
| [Sections 23.1–23.2: Quantum adversaries; The adversary method](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=117) | 109–113 | Bounding progress across all permitted algorithms. |
| [Section 23.3: Example: Unstructured search](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=121) | 113 | The zero-versus-singleton input family and ideal search optimality. |

These passages are entry points to the corresponding parts of the [bridge](bridge.md), rather than a requirement to read the complete notes. Section 19.1 assumes familiarity with Grover's algorithm; the bridge supplies the specific rotation and event ordering used here.

## What the bridge supplies

The bridge develops the project's density-matrix channel, hidden measurement outcome, post-query flag, protected logical register, renewal age, conditional hazard and stationary startup. It then connects those objects to the two canonical theorems and the equal-mean, equal-asymptotic-tail comparison.

The noisy all-algorithm converse is a separate **research dependency**: Agarwal–Rao–Song, *Noisy Quantum Query Complexity via Fractional Block Sensitivity*, [arXiv:2610.00506v2](https://arxiv.org/html/2610.00506v2). Its potential is imported and mapped to this model in [the progress-bound account](../science/progress-bound.md). Childs provides the ideal-query foundation; the research paper supplies the noisy inequality; the project supplies the renewal estimates and matching algorithms.

Use the [milestone map](milestones.md) for the project's conceptual order and the [science guide](../science/README.md) for direct access to exact statements and proofs. This page links the educational source; no copy of the notes is distributed here.
