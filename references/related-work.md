# Prior work and the contribution of noise clocks

Machine-readable entries for the citation keys below are in [bibliography.bib](bibliography.bib).

This project studies zero-or-one marked-item search when a perfect bit query is followed by complete dephasing of its index register at the events of an external stationary renewal process. An event flag becomes available after the affected query. Every call advances the noise clock and is charged, including calls made while the logical search state is stored in protected workspace. These conventions specify the information and timing resources available to the algorithm.

The first main result concerns a fixed gap distribution with finite mean $\mu$, survival function $S(\ell)=\Pr(L\geq\ell)$, and a global lower bound $h(a)\geq c/(a+1)$ on its conditional event hazard at every reachable age. For fixed error below $1/2$, its optimal query cost is

$$
Q(N)=\Theta\!\left(
 \frac{\mu N}{\mathbb E\min\{L^2,N\}}
\right).
$$

Constants can depend on the fixed noise law and the error target. A second result shows why the hazard assumption matters: two full-support renewal laws can have exactly the same mean and asymptotic power-law tail, including its leading coefficient, and nevertheless yield different optimal search exponents. Thus the moment formula describes a specified regularity class; it is not a characterization of all renewal noise.

## The quantum lower-bound machinery is inherited

Agarwal, Rao and Song [ARS] already formulate arbitrary algorithm-independent correlated schedules, with index dephasing after the query and flags revealed afterward. Their Section 6 supplies the applicable quantum converse. In the search specialization, Lemmas 6.7–6.8 provide a bounded potential, a constant terminal separation, and conditional drift

$$
\mathbb E[\Delta\Psi_t\mid\mathcal F_{t-1}]
\leq \frac{12}{N}+\frac{12u_t}{\sqrt N}
     -2p_t u_t^2,\qquad 0\leq u_t\leq1.
$$

Their framework already identifies predictable conditional rates as the relevant schedule information and warns against using only hindsight coherent-run lengths. It treats a time-dependent independent-noise search example and explicitly leaves applications to temporal-memory processes open.

We use this inequality with $p_t=h(A_t)$. The new analysis stops the potential before an old-age excursion, controls the stationary initial interval and subsequent threshold crossings, and matches the resulting bound with a causal renewal algorithm. The alternating-hazard construction instead combines a capped drift estimate with selective coherent queries across multiple renewal cycles. We do not claim a new quantum adversary framework or the original observation that predictability matters.

## Earlier noisy-search algorithms and lower bounds

Regev and Schiff [RS] establish the loss of quantum search speedup under independent oracle omissions. An omitted query and a query followed by index dephasing are different operations, so that theorem does not directly supply the converse used here.

Rosmanis [Ros] proves a lower bound of order $\max\{Np,\sqrt N\}$ for independent noisy queries, including dephasing with error flags. This establishes the important independent-noise comparison: constant independent dephasing destroys the asymptotic quadratic search advantage even when the algorithm learns that an error occurred. The present noise law is temporally correlated and stationary, with parameters fixed as $N$ grows.

Vrana, Reeb, Reitzner and Wolf [VRRW] develop noisy-search algorithms built from finite Grover runs, measurement, verification and repetition, including algorithms that do not require the noise strength as input. Their principal lower bounds concern collective depolarizing noise. The finite-run search subroutine and check-and-repeat architecture are established ingredients. Here the trial durations are constrained by an external renewal clock, and converting renewal rewards into a fixed worst-case query budget requires explicit treatment of charged dummy calls and the initial stationary residual interval.

The ordinary Grover rotation [Grover], its quadratic success growth before saturation, and the noiseless search lower bound [BBBV] are standard. The contribution is the optimal allocation of coherent search under the stated temporal noise, including the converse against arbitrary adaptive algorithms and protected ancillary memory.

## Renewal measurements and temporal noise have older physical antecedents

Romanelli [Rom] studies quantum walks interrupted by measurements with Lévy-distributed waiting times. The resulting anomalous spreading is analyzed through truncated waiting-time moments. This is a direct antecedent of the physical mechanism in which rare long intervals preserve substantial coherent evolution despite recurring measurements. The observable there is spatial spreading of a specified walk, rather than optimal oracle-search complexity.

Romanelli, Auyuanet and Donangelo [RAD] analyze a resonant search model with measurements at arbitrary intervals. Their Section 4 gives a product expression for the resulting two-level dynamics. It establishes that the placement of measurements can alter search dynamics; it does not establish the stationary renewal resource law or a lower bound over all permitted search algorithms.

Vacchini [Vac] develops quantum renewal processes with completely positive evolution interrupted by jumps at general waiting times. This supplies broader open-system context for renewal clocks. The probability identities used here, including stationary age bias, renewal rewards and finite-horizon stopping, belong to classical renewal theory.

Temporal-memory search has also been studied under other noise actions. Mandal and collaborators [Mandal] analyze specified Grover dynamics under local unitary errors with memory. King and collaborators [King] optimize monitored continuous-time search with deliberately chosen resetting and account for measurement implementation time. These are relevant comparisons, but their noisy operations, accessible information and time conventions differ from the externally imposed query-index dephasing considered here.

## Relation to the companion Markov-omission result

The public *Quantum Search Memory Laws* account [Memory] determines optimal costs for an unobserved symmetric two-state Markov process that either applies or omits the oracle. It distinguishes actual calls from elapsed oracle slots and proves the bounds using a recurrence that retains both hidden memory states. Its paired-process comparison also shows that equal single-call noise channels can have different computational effects.

The common scientific theme is therefore already established: temporal structure can change search complexity while a one-call marginal fails to specify the computational resource. The present work addresses a different operation and information contract. Events irreversibly dephase the index, flags reveal past events, and every advancing clock tick costs a query. At a fixed positive noise density, the regular-hazard theorem gives a range of asymptotic speedups determined by a truncated gap moment. The positive alternating-hazard family then demonstrates that even equal mean, asymptotic tail and moment-finiteness profile can fail to determine the optimal cost.

The Markov-omission theorem is not used as a proof input. Its hidden-state recurrence does not become the renewal dephasing potential through a change of parameters: an omitted oracle and an index measurement act differently on the algorithm's joint state.

## What the two theorems establish together

For a smooth power-law survival $S(\ell)\asymp\ell^{-\alpha}$, with the stated global hazard condition, the resource formula yields $N^{\alpha/2}$ for $1<\alpha<2$, $N/\log N$ at $\alpha=2$, and $N$ for $\alpha>2$. The stopped argument also treats the finite-mean boundary $S(\ell)\asymp[\ell(\log\ell)^p]^{-1}$, $p>1$, giving $\sqrt N(\log N)^p$.

For alternating hazards of orders $a^{-\beta}$ and $2\alpha/a$, with $\beta>\max\{1,\alpha-1\}$, the gap survival still has exponent $\alpha$, while the optimal cost becomes

$$
Q(N)=\Theta\!\left(N^{\,1/2+(\alpha-1)/(2\beta)}\right).
$$

Positive mixtures with finite-support distributions make the smooth and alternating laws have a common mean $\mu_*$ and a common tail coefficient $c_*>0$:

$$
\mathbb E L_s=\mathbb E L_a=\mu_*,
\qquad
\Pr(L_s\geq\ell)\sim\Pr(L_a\geq\ell)\sim c_*\ell^{-\alpha}.
$$

The mixture changes only a finite prefix of each hazard sequence. Both laws retain full support and their proved search exponents. They therefore have exactly the same stationary event rate $1/\mu_*$, the same isolated single-call marginal including its flag, and the same moment-finiteness thresholds.

For example, $\alpha=3,\beta=4$ gives such a matched pair with costs $N$ and $N^{3/4}$, although both gap distributions have finite variance. Every finite-age hazard is positive. The faster algorithm accumulates useful coherent queries at low-risk ages while protecting the state during other charged calls; it receives no advance warning of the next event. Equality of the leading asymptotic tail is not equality of the entire survival sequence or of the numerical values of higher finite moments.

These conclusions concern the stated oracle interface. Protected memory, ideal controls, post-query flags and a query-driven clock are substantive assumptions. They do not imply the same behavior for noise acting continuously on all memory, or for a fixed finite cutoff of the heavy tail.

## References

- **[Grover]** Lov K. Grover, *A fast quantum mechanical algorithm for database search*, Proceedings of the 28th Annual ACM Symposium on Theory of Computing, pp. 212–219 (1996); arXiv:quant-ph/9605043v3. [Primary preprint](https://arxiv.org/abs/quant-ph/9605043).
- **[BBBV]** Charles H. Bennett, Ethan Bernstein, Gilles Brassard and Umesh Vazirani, *Strengths and Weaknesses of Quantum Computing*, SIAM Journal on Computing **26**(5), 1510–1523 (1997); arXiv:quant-ph/9701001. [Primary preprint](https://arxiv.org/abs/quant-ph/9701001).
- **[RS]** Oded Regev and Liron Schiff, *Impossibility of a Quantum Speed-up with a Faulty Oracle*, ICALP 2008; archival preprint arXiv:1202.1027. [Primary preprint](https://arxiv.org/abs/1202.1027).
- **[ARS]** Mehil Agarwal, Shravas Rao and Fang Song, *Noisy Quantum Query Complexity via Fractional Block Sensitivity*, arXiv:2610.00506v2, revised 2 October 2026. [Primary full text](https://arxiv.org/html/2610.00506v2). See Sections 1.2–1.3 and 6, especially Lemmas 6.7–6.8.
- **[Ros]** Ansis Rosmanis, *Quantum Search with Noisy Oracle*, arXiv:2309.14944v1, 2023. [Primary preprint](https://arxiv.org/abs/2309.14944).
- **[VRRW]** Péter Vrana, David Reeb, Daniel Reitzner and Michael M. Wolf, *Fault-ignorant Quantum Search*, New Journal of Physics **16**, 073033 (2014); arXiv:1307.0771v2. [Primary full text](https://arxiv.org/html/1307.0771v2). See Section II and Appendix B for the algorithm and noise-model distinctions.
- **[Rom]** Alejandro Romanelli, *Measurements in the Lévy quantum walk*, Physical Review A **76**, 054306 (2007); arXiv:0710.1320. [Primary preprint](https://arxiv.org/abs/0710.1320).
- **[RAD]** A. Romanelli, A. Auyuanet and R. Donangelo, *Quantum search algorithm as an open system*, arXiv:quant-ph/0508142v3, revised 19 September 2006. [Primary full text](https://arxiv.org/pdf/quant-ph/0508142).
- **[Vac]** Bassano Vacchini, *Quantum renewal processes*, Scientific Reports **10**, 5592 (2020); arXiv:1906.00693. [Published article](https://www.nature.com/articles/s41598-020-62260-z).
- **[Mandal]** S. P. Mandal, A. Ghoshal, C. Srivastava and U. Sen, *Invariance of success probability in Grover's quantum search under local noise with memory*, Physical Review A **107**, 022427 (2023); arXiv:2112.02640v4. [Primary full text](https://arxiv.org/html/2112.02640v4).
- **[King]** Emma C. King, Sayan Roy, Francesco Mattiotti, Maximilian Kiefer-Emmanouilidis, Markus Bläser and Giovanna Morigi, *Time complexity of a monitored quantum search with resetting*, arXiv:2601.20560v1, 2026. [Primary preprint](https://arxiv.org/abs/2601.20560).
- **[Memory]** *Quantum Search Memory Laws*, public scientific account, revision 55e1d5d34a23e5af0ed1a89628868a4f2e3f0455 (18 October 2026). [Model](https://github.com/GoGoKo699/Quantum-Search-Memory-Laws/blob/55e1d5d34a23e5af0ed1a89628868a4f2e3f0455/science/model.md), [authoritative lower bounds](https://github.com/GoGoKo699/Quantum-Search-Memory-Laws/blob/55e1d5d34a23e5af0ed1a89628868a4f2e3f0455/science/lower-bounds.md), and [paired-process comparison](https://github.com/GoGoKo699/Quantum-Search-Memory-Laws/blob/55e1d5d34a23e5af0ed1a89628868a4f2e3f0455/science/paired-comparison.md).
