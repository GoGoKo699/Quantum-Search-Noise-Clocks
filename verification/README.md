# Scientific model checks

[Repository](../README.md) · [Scientific account](../science/README.md)

These checks address concrete implementation and indexing risks in the mathematical model. They support the analytical arguments; they are not proofs of asymptotic query complexity or all-algorithm lower bounds.

## Run

From the repository root, using Python 3.12 or a compatible environment:

```sh
python -m pip install -r verification/requirements.txt
python verification/check_models.py
```

The script writes `verification/results.json`. Use `--output PATH` to choose another destination. NumPy is the only third-party dependency. The committed output records the actual interpreter and NumPy versions, deterministic seed, numerical tolerance, and SHA-256 hash of the executed script. Timestamps and floating-point roundoff can differ on a rerun.

## What is checked

**Flag timing in full density matrices.** The index and answer registers evolve under an explicit XOR permutation, diffusion, and the pinching channel. The check covers each possible mark in small power-of-two and non-power-of-two dimensions through a full Grover oscillation. A terminal event on query $\ell$, followed immediately by measurement, gives $\sin^2((2\ell-1)\theta_N)$. A clean cap after $K$ complete iterations gives $\sin^2((2K+1)\theta_N)$. The complete density matrices, not only the marked probabilities, are compared. A control calculation applies diffusion after pinching and demonstrates why the measurement order matters.

**Protected-memory parking.** The reference, logical memory, query index, and answer registers are all retained. A seeded local unitary rotates one half of a maximally entangled reference-memory state. The logical state is swapped into the query register only for useful Grover calls; dummy queries use a basis index and the answer state $|+\rangle$. Every flag pattern on the inactive calls is checked against the ideal logical channel. The reference tests preservation of entanglement, not merely one unentangled state. A deliberately dephased useful query produces a nonzero trace-distance control, showing that the check does not silently treat every event as harmless.

**Exact renewal identities and the initial straddling interval.** Rational arithmetic verifies the stationary age distribution, truncated-second-moment identity, and age-crossing bound for a distribution positive on each gap length 1, 2, 3, and 4. All thresholds through one beyond its maximum gap and horizons through twice that gap are enumerated. An explicit two-call case shows that counting only fresh intervals would miss a positive crossing probability from the initially straddling interval.

**Finite-size moment illustrations.** Deterministic sums show the behavior of $M_R$ for three Pareto tails and the logarithmic finite-mean boundary example. These are labeled illustrations in the output. They neither simulate a full large quantum algorithm nor establish the asymptotic theorem.

The channel checks use complex128 arithmetic with tolerance $2\times10^{-12}$; the finite-support renewal checks use exact fractions. No Monte Carlo success estimate is used.

## Recorded run

The committed run used CPython 3.12.14 and NumPy 2.3.5, with seed 20261031.

| Quantity | Observed result |
| --- | ---: |
| Maximum Grover probability error | $1.89\times10^{-15}$ |
| Maximum full Grover density-matrix error, Frobenius norm | $2.41\times10^{-15}$ |
| Maximum parked-channel trace distance from the ideal joint state | $2.05\times10^{-16}$ |
| Trace distance after deliberately dephasing a useful query | $0.6666666666666683$, agreeing with $2/3$ |

The flag-timing control is substantial: at $N=3$, an event on the second query gives marked probability $25/27$ when the index is measured immediately, but approximately 0.135802 when diffusion is applied after pinching first.

For gap probabilities $(1/2,1/6,1/6,1/6)$, threshold $R=2$, and horizon $T=2$, exact enumeration gives crossing probability $5/12$. Its components are the initial old-age probability $1/4$ and an initially straddling contribution $1/6$. The corrected upward-crossing bound equals $5/12$ in this case.
