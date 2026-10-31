# Thirty milestones for quantum search with noise clocks

[Learning guide](README.md) · [Selected anchor](anchor.md) · [Conceptual bridge](bridge.md) · [Scientific account](../science/README.md)

This map describes the project's understanding targets and their scientific dependencies. The first 14 milestones assemble the quantum-query and renewal-probability foundations. The remaining 16 develop the two matching theorems, the controlled comparison between noise laws, and the meaning of their assumptions. Each phase moves from individual operations and objects toward an integrated account.

The sole educational anchor is Andrew M. Childs, *Lecture Notes on Quantum Algorithms*, **17 April 2025**, available as the [official PDF][childs]. Chapters 19, 21, and 23 provide the main algorithmic route, with Sections 1.1–1.2 supplying state and circuit language. Section links below include PDF page locations. Section 19.1 assumes familiarity with Grover search; the [bridge](bridge.md) supplies the rotation and event-order explanation needed here.

Renewal probability, stationary initialization, and the project's noisy-query proofs are supplied by the canonical scientific pages. The noisy quantum potential is a research-level input from Agarwal, Rao, and Song (ARS), attributed on the [progress-bound page](../science/progress-bound.md#attribution-and-use). A connection to Childs identifies the relevant algorithmic foundation; it does not attribute renewal theory or the ARS theorem to those lecture notes.

## Phase I: background and preliminaries

M01–M14 connect the search interface, coherent dynamics, information lost to noise, and the probability model. The phase ends by specifying the complete resource comparison.

### M01

**The search task and its charged access**

**Central question:** What must an algorithm learn, and what counts as a query, when the input has zero or one marked position?

**Understanding target:** Identify the input promise, the distinction between a marked index and `none`, the requirement of correctness on every permitted input, and the oracle-call resource. Explain why the input is supplied through a query interface rather than a free data-loading operation.

**Dependencies and story role:** None. This establishes the concrete computational task to which every later cost statement refers.

**Conceptual connection:** A search problem becomes a meaningful complexity comparison only after its access operation and required output are specified.

**Source pointers:** Anchor: [Childs §21.1, quantum query complexity][childs-query-model]. Canonical: [search and allowed computation](../science/model.md#search-and-allowed-computation).

### M02

**Quantum states, phases, and measurement**

**Central question:** Why does a coherent superposition contain information that its immediate measurement probabilities do not describe?

**Understanding target:** Distinguish basis states, amplitudes, relative phases, and outcome probabilities. Explain how a known unitary can turn a phase difference into a measurable probability difference, and why a classical mixture with the same initial probabilities need not evolve identically.

**Dependencies and story role:** [M01](#m01). This introduces the local state description needed to understand both coherent search and its disruption.

**Conceptual connection:** The computational benefit and the damage caused by dephasing concern coherence between query indices.

**Source pointers:** Anchor: [Childs §§1.1–1.2, quantum data and circuits][childs-basics]. Canonical: [the query registers](../science/model.md#search-and-allowed-computation); bridge: [states, queries, and notation](bridge.md#states-queries-and-notation).

### M03

**Three uses of one XOR oracle**

**Central question:** How can the same oracle support a phase query, an unchanged dummy state, and exact verification?

**Understanding target:** Explain the roles of the response states $`|-\rangle`$, $`|+\rangle`$, and $`|0\rangle`$. Recognize that the project's $`O_x`$ is the XOR oracle denoted $`\widehat O_x`$ in Childs, and that phase kickback uses this interface without requiring a controlled-oracle primitive.

**Dependencies and story role:** [M01](#m01), [M02](#m02). This fixes the local access operation before algorithms combine it with other gates.

**Conceptual connection:** Useful queries, charged waiting, and verification differ through known register preparation, while sharing one input-access resource.

**Source pointers:** Anchor: [Childs §21.2, quantum queries, equations (21.2)–(21.3)][childs-queries]. Canonical: [the XOR interface](../science/model.md#search-and-allowed-computation) and [the causal query policy](../science/predictable-queries.md#causal-query-policy).

### M04

**Known reflections and input-dependent queries**

**Central question:** Which operation in a Grover iteration supplies information about the unknown input?

**Understanding target:** Separate uniform-state preparation and the diffusion reflection from the oracle phase operation. Explain how preparation, a known reflection, and inverse preparation implement diffusion, and why these known operations require no hidden-data oracle.

**Dependencies and story role:** [M02](#m02), [M03](#m03). This assembles a coherent iteration from its local components.

**Conceptual connection:** Query complexity counts input access while keeping the roles of preparation, workspace, and gates explicit.

**Source pointers:** Anchor: [Childs §19.3, amplitude amplification, printed pp. 88–89][childs-amplification]. Canonical: [other resources and scope](../science/predictable-queries.md#other-resources-and-scope); bridge: [states, queries, and notation](bridge.md#states-queries-and-notation).

### M05

**Grover rotation and saturation**

**Central question:** Why does coherent search initially gain quadratically with the number of queries, yet require a stopping rule?

**Understanding target:** Interpret Grover search as rotation between marked and unmarked directions. Relate the angle $`\theta_N=\arcsin(N^{-1/2})`$ to the success probability $`\sin^2((2k+1)\theta_N)`$, its initial order $`k^2/N`$, and the possibility of overshooting after order $`\sqrt N`$ iterations.

**Dependencies and story role:** [M03](#m03), [M04](#m04). This connects one coherent iteration to the useful duration of a run.

**Conceptual connection:** Grover saturation later determines where the renewal reward must be truncated.

**Source pointers:** Anchor: [Childs §19.1, unstructured search][childs-search], and [§19.3, amplification][childs-amplification]. Canonical: [the Grover run in the causal policy](../science/predictable-queries.md#causal-query-policy); bridge: [a complete event-order example](bridge.md#a-complete-event-order-example).

### M06

**Success probability and certified output**

**Central question:** How can an algorithm have a nonzero failure probability while never accepting an unmarked candidate?

**Understanding target:** Separate candidate generation from a basis-index verification query. Distinguish error averaged over noise and private randomness from a guarantee on every noise history, and retain worst-case correctness over the promised inputs. Explain why verification gives one-sided error for the constructed search algorithms.

**Dependencies and story role:** [M01](#m01), [M03](#m03), [M05](#m05). This connects coherent success probabilities to the required classical output.

**Conceptual connection:** A probabilistic search procedure becomes a correct bounded-error algorithm through explicit acceptance and failure rules.

**Source pointers:** Anchor: [Childs §21.1, query-complexity conventions][childs-query-model], and [§19.3, amplification][childs-amplification]. Canonical: [the error criterion](../science/model.md#search-and-allowed-computation) and [paired-interval verification](../science/renewal-law.md#one-paired-interval-trial).

### M07

**What an optimal query bound must establish**

**Central question:** What separates the cost of one algorithm from a lower bound on every permitted algorithm?

**Understanding target:** Distinguish a constructive upper bound from an all-algorithm converse. Explain why comparing the zero input with singleton inputs already supports the ideal search lower bound, and why observing poor performance of a particular noisy Grover strategy would not establish optimality.

**Dependencies and story role:** [M01](#m01), [M06](#m06). This supplies the logical standard that both project theorems must meet.

**Conceptual connection:** The same search promise supports an algorithm and an adversarial comparison of possible inputs.

**Source pointers:** Anchor: [Childs §23.3, unstructured-search adversary example][childs-search-lower]. Canonical: [the imported progress statement](../science/progress-bound.md#the-imported-progress-statement).

### M08

**The information lost at a flagged query**

**Central question:** What does index dephasing erase, and what does the event flag actually reveal?

**Understanding target:** Read the pinching operation as removal of coherence between different index values. Track the order oracle, pinching, then flag. Distinguish knowledge that an event occurred from access to its hidden index outcome, and distinguish index dephasing from omission of the oracle.

**Dependencies and story role:** [M02](#m02), [M03](#m03). This identifies the local physical action whose timing the project studies.

**Conceptual connection:** A noise model is specified by its action on registers and its accessible information, as well as its event frequency.

**Source pointers:** Anchor connection: [Childs §§1.1–1.2, state and circuit language][childs-basics]. Canonical noisy extension: [index dephasing and its flag](../science/model.md#index-dephasing-and-its-flag); bridge: [what a flagged query does](bridge.md#what-a-flagged-query-does).

### M09

**Protected memory and causal control**

**Central question:** When can logical coherence survive while a physical query advances the noise clock?

**Understanding target:** Explain why dephasing a fixed basis query register leaves a separately stored logical state untouched, including its entanglement with other registers. Describe the role of swaps and past flags, and identify the prohibition on using the current flag before its query occurs.

**Dependencies and story role:** [M04](#m04), [M08](#m08). This joins a local noise channel to the allowed control architecture.

**Conceptual connection:** The location of noise and the availability of protected memory determine which physical calls expose computational coherence.

**Source pointers:** Anchor: [Childs §1.2, quantum circuits][childs-basics], and [§21.2, queries][childs-queries]. Canonical: [protected memory is part of the model](../science/interpretation.md#protected-memory-is-part-of-the-model); bridge: [parking the logical state](bridge.md#parking-the-logical-state).

### M10

**Survival and conditional hazard**

**Central question:** How does surviving previous calls change the probability of an event on the next call?

**Understanding target:** Distinguish a gap probability, its survival function $`S(\ell)`$, and the conditional hazard $`h(a)=1-S(a+2)/S(a+1)`$. Explain why the stationary event frequency and the hazard at an observed age describe different information.

**Dependencies and story role:** [M01](#m01), [M08](#m08). This introduces the local probability object used to choose and bound queries.

**Conceptual connection:** Query decisions use information available before a call, so conditional probabilities enter the resource analysis.

**Source pointers:** Anchor connection: [Childs §21.1, the query-model baseline][childs-query-model]. Canonical probability extension: [the exact renewal convention](../science/model.md#exact-renewal-convention); bridge: [renewal facts needed here](bridge.md#renewal-facts-needed-here).

### M11

**Fresh cycles and stationary ages**

**Central question:** Why is the interval seen at a random stationary starting time different from a newly begun interval?

**Understanding target:** Relate iid fresh gaps to the stationary age law $`\pi(a)=S(a+1)/\mu`$ and event rate $`1/\mu`$. Explain length bias, the hidden initial age, and why a computation cannot initially assume it stands at a renewal boundary.

**Dependencies and story role:** [M10](#m10). This builds the full clock from its local hazard and distinguishes two starting conditions.

**Conceptual connection:** Stationarity fixes the sampling of ages; it does not make the future waiting time an ordinary fresh gap.

**Source pointers:** Anchor connection: [Childs §21.1, defining a query model][childs-query-model]. Canonical renewal extension: [stationary initialization](../science/model.md#exact-renewal-convention); bridge: [renewal facts needed here](bridge.md#renewal-facts-needed-here).

### M12

**Expected work and a deterministic budget**

**Central question:** How can random trial durations produce an algorithm with a fixed worst-case query cap?

**Understanding target:** Distinguish expected cost from a deterministic call budget. Explain how a finite cost expectation bounds deadline failure, how a union bound combines different failure events, and why this combination does not require those events to be independent.

**Dependencies and story role:** [M06](#m06), [M11](#m11). This connects probabilistic operations to the complexity convention used throughout the project.

**Conceptual connection:** Repetition and stopping rules must account for both successful output and the calls needed to reach it.

**Source pointers:** Anchor connection: [Childs §19.3, amplification and success probabilities][childs-amplification], and [§21.1, bounded-query algorithms][childs-query-model]. Canonical finite-budget argument: [deterministic truncation](../science/renewal-law.md#deterministic-truncation).

### M13

**The inherited noisy-query potential**

**Central question:** How can one bound information gained by a noisy query without prescribing the algorithm's query state?

**Understanding target:** Identify the roles of the bounded potential $`0\le\Psi_t\le3`$, its zero initial value, the positive terminal requirement, and the conditional drift involving the active magnitude $`u_t`$ and event probability $`p_t`$. Attribute this machinery to ARS and distinguish it from the ideal adversary method used as an educational foundation.

**Dependencies and story role:** [M07](#m07), [M08](#m08), [M10](#m10). This provides the universal converse ingredient needed after the probability model is specified.

**Conceptual connection:** A bound on conditional information gain allows arbitrary adaptive states and protected workspace inside the lower-bound argument.

**Source pointers:** Anchor: [Childs §§23.1–23.2, quantum adversaries][childs-adversaries]. Canonical research input: [the imported progress statement](../science/progress-bound.md#the-imported-progress-statement) and [attribution](../science/progress-bound.md#attribution-and-use).

### M14

**The complete operational comparison**

**Central question:** Which assumptions must remain fixed for two noisy-search costs to be compared meaningfully?

**Understanding target:** Assemble the promised task, XOR interface, post-query flags, exogenous stationary clock, known fixed law, protected memory, and charged dummy calls. Distinguish a query-driven clock from a wall-clock environment, and keep ideal gate operations separate from the resource counted by the theorem.

**Dependencies and story role:** [M09](#m09), [M11](#m11), [M12](#m12), [M13](#m13). This completes the background phase by integrating its local operations, probability objects, and proof standards.

**Conceptual connection:** The meaning of an advantage depends jointly on access, information, memory, and the clock that measures cost.

**Source pointers:** Anchor: [Childs §§21.1–21.2, query model and oracle interface][childs-query-model]. Canonical: [model and charged resources](../science/model.md#search-and-allowed-computation) and [operational boundaries](../science/interpretation.md#asymptotic-and-operational-boundaries).

## Phase II: narrative and innovation

M15–M20 assemble the truncated-moment law from an interrupted run and a universal converse. M21–M27 establish its reach, its obstruction, and the second matching theorem. M28–M30 integrate the exact comparison, resource accounting, attribution, and limits.

### M15

**The reward from one interrupted run**

**Central question:** How much useful search can an interval contribute when its last query is dephased?

**Understanding target:** Explain why measuring immediately after an event at query $`\ell`$ gives the angle $`(2\ell-1)\theta_N`$, while a clean cap after $`K`$ complete iterations gives $`(2K+1)\theta_N`$. Connect these timings to a success probability bounded below by a constant times $`\min\{\ell^2/N,1\}`$.

**Dependencies and story role:** [M05](#m05), [M06](#m06), [M08](#m08), [M14](#m14). This identifies the local coherent reward from which the first algorithm is built.

**Conceptual connection:** Pinching destroys phase information while preserving the index probabilities sampled at the event.

**Source pointers:** Anchor: [Childs §19.1, search][childs-search], and [§19.3, amplification][childs-amplification]. Canonical: [one paired-interval trial, equations (23)–(25)](../science/renewal-law.md#one-paired-interval-trial); bridge: [event order](bridge.md#a-complete-event-order-example).

### M16

**Independent paired trials with charged durations**

**Central question:** How does an interrupted candidate become a repeatable trial whose entire duration is accounted for?

**Understanding target:** Explain the search-interval and verification-interval pairing, fresh preparation between trials, and mean pair cost $`2\mu`$. Separate independence across fresh trials from possible dependence between success and duration inside one trial. Explain how a predetermined trial count and a deadline yield bounded error.

**Dependencies and story role:** [M12](#m12), [M15](#m15). This turns a local run into a complete algorithm after an observed renewal.

**Conceptual connection:** The success reward and the cycle cost must be combined without granting free waiting or assuming an unjustified independence.

**Source pointers:** Anchor connection: [Childs §19.3, success amplification][childs-amplification]. Canonical: [paired trials](../science/renewal-law.md#one-paired-interval-trial) and [deterministic truncation](../science/renewal-law.md#deterministic-truncation).

### M17

**Starting inside a stationary interval**

**Central question:** How can a fixed-budget algorithm reach a fresh renewal when the initial residual waiting time has infinite mean?

**Understanding target:** Interpret the residual tail $`\Pr(F>w)=\mu^{-1}\sum_{\ell>w}S(\ell)`$ and distinguish a finite fixed-error quantile from a finite expectation. Explain the charged startup timeout, its failure event, and the renewal independence available after the first observed flag.

**Dependencies and story role:** [M11](#m11), [M12](#m12), [M16](#m16). This places the paired-trial algorithm into the actual stationary initial condition.

**Conceptual connection:** An infinite mean waiting time can coexist with a finite timeout that fails only with a prescribed constant probability.

**Source pointers:** Anchor connection: [Childs §21.1, fixed query cost and error][childs-query-model]. Canonical startup argument: [reaching the first observed renewal](../science/renewal-law.md#reaching-the-first-observed-renewal).

### M18

**The truncated second moment as a search resource**

**Central question:** Why does the search reward depend on a truncated second moment rather than only the mean gap?

**Understanding target:** Relate $`M_R=\mathbb E\min\{L^2,R^2\}`$ to quadratic coherent growth and saturation at $`R\asymp\sqrt N`$. Interpret its tail-sum identity and explain how a reward of order $`M_R/N`$ per trial produces an upper cost of order $`\mu N/M_R`$.

**Dependencies and story role:** [M10](#m10), [M15](#m15), [M16](#m16). This identifies the scalar quantity that summarizes the first algorithm's useful coherence.

**Conceptual connection:** A gap's contribution is governed by useful coherent evolution before saturation, while its full duration still enters the cost.

**Source pointers:** Anchor: [Childs §19.3, amplification][childs-amplification]. Canonical: [truncated-moment identities](../science/renewal-law.md#the-truncated-moment-resource-law) and [trial success and cost](../science/renewal-law.md#one-paired-interval-trial).

### M19

**The stopped converse and the initial crossing**

**Central question:** Why must a lower bound treat rare old intervals separately, including one already in progress when the algorithm starts?

**Understanding target:** Explain how the global hazard bound controls potential growth below age $`R`$, and how boundedness of $`\Psi`$ permits stopping the analysis before older ages. Identify both the initial old-age probability and later upward crossings. Retain unconditional terminal correctness when initial age is revealed for the lower bound.

**Dependencies and story role:** [M11](#m11), [M13](#m13), [M14](#m14), [M18](#m18). This supplies the first theorem's all-algorithm converse and its stationary boundary correction.

**Conceptual connection:** A rare initial interval can dominate an unrestricted average without giving a typical fixed-budget algorithm that much opportunity.

**Source pointers:** Anchor connection: [Childs §23.2, adversary reasoning][childs-adversary-method]. Canonical: [initial-age conditioning](../science/progress-bound.md#why-the-initial-age-conditioning-is-valid), [the stopped proof](../science/renewal-law.md#lower-bound-by-stopping-before-old-ages), and [the crossing bound](../science/renewal-law.md#the-crossing-bound).

### M20

**The matched renewal resource theorem**

**Central question:** Under which precise conditions does the truncated moment determine the optimal search cost?

**Understanding target:** Combine the fixed-budget construction and stopped converse into $`Q_\epsilon(N;L)=\Theta(\mu N/M_{\lceil\sqrt N\rceil})`$. Distinguish the upper bound's finite-mean assumption from the lower bound's global condition $`h(a)\ge c/(a+1)`$. Preserve the fixed-law, fixed-error quantifiers and the law-dependent asymptotic onset.

**Dependencies and story role:** [M16](#m16), [M17](#m17), [M18](#m18), [M19](#m19). This integrates the first mechanism into a complete optimality statement.

**Conceptual connection:** A resource formula becomes a characterization only when its construction and universal converse share the same operational assumptions.

**Source pointers:** Anchor: [Childs §21.1, query complexity][childs-query-model], and [§23.3, matching search converse][childs-search-lower]. Canonical: [Theorem 1](../science/renewal-law.md#theorem-1-stationary-renewal-search) and [its boundary](../science/renewal-law.md#consequences-and-boundary).

### M21

**The power-law search regimes**

**Central question:** What search costs can occur under one fixed stationary law with a positive mean event rate?

**Understanding target:** Connect $`S(\ell)=\ell^{-\alpha}`$, $`\alpha>1`$, to the regimes $`N^{\alpha/2}`$, $`N/\log N`$, and $`N`$. Explain the role of the truncated moment at $`\alpha=2`$, and retain the hazard condition when interpreting finite second moment as linear search cost.

**Dependencies and story role:** [M20](#m20). This turns the first theorem into an explicit range of algorithmic behaviors.

**Conceptual connection:** A fixed average noise rate does not specify the lengths of usable coherent runs.

**Source pointers:** Anchor: [Childs §19.1, the ideal search baseline][childs-search]. Canonical: [smooth power-law gaps](../science/examples.md#smooth-power-law-gaps) and [finite-second-moment laws within the hazard class](../science/examples.md#finite-second-moment-laws-within-the-hazard-class).

### M22

**The finite-mean logarithmic boundary**

**Central question:** How close to Grover scaling can the regular-hazard theorem get while the stationary event rate stays positive?

**Understanding target:** Explain why the exact law $`S_p(\ell)=[\ell(1+\log\ell)^p]^{-1}`$, $`p>1`$, satisfies the global hazard condition and yields $`\Theta(\sqrt N(\log N)^p)`$ cost. Retain its infinite mean stationary residual, finite startup quantiles, and nonuniform constants as $`p\downarrow1`$.

**Dependencies and story role:** [M17](#m17), [M19](#m19), [M20](#m20). This shows why the stationary-start and stopped-bound details matter at the edge of the theorem's finite-mean regime.

**Conceptual connection:** Near-quadratic asymptotic query improvement can coexist with a large law-dependent startup requirement.

**Source pointers:** Anchor: [Childs §19.1, Grover scaling][childs-search]. Canonical: [the logarithmic boundary example](../science/examples.md#a-finite-mean-logarithmic-boundary).

### M23

**One guaranteed clean slot changes the conclusion**

**Central question:** Why can one guaranteed clean slot at a finite age defeat a conclusion based only on the eventual tail?

**Understanding target:** Explain the redistribution of the length-two mass that preserves the mean and all survival probabilities from length four onward, while creating a zero hazard at age one. Connect that known clean slot and protected memory to accumulation of ideal Grover queries across many cycles.

**Dependencies and story role:** [M09](#m09), [M11](#m11), [M20](#m20), [M21](#m21). This identifies a concrete obstruction to weakening the first theorem's global hazard hypothesis.

**Conceptual connection:** A condition on every reachable age can control computational access even when it affects only a finite part of a probability law.

**Source pointers:** Anchor: [Childs §§21.1–21.2, allowed oracle access][childs-query-model]. Canonical: [one forbidden gap](../science/comparisons.md#one-forbidden-gap) and [its implication](../science/comparisons.md#lower-bound-and-implication).

### M24

**Positive alternating hazards with the same tail exponent**

**Central question:** Can useful timing structure remain when every possible gap has positive probability?

**Understanding target:** Describe the even-age hazards of order $`a^{-\beta}`$ and odd-age hazards asymptotic to $`2\alpha/a`$, with $`\beta>\max\{1,\alpha-1\}`$. Explain why the gap survival still has a positive coefficient times $`\ell^{-\alpha}`$, and why the low-risk ages do not amount to guaranteed clean calls.

**Dependencies and story role:** [M10](#m10), [M11](#m11), [M21](#m21), [M23](#m23). This begins the second theorem with a fully positive clock rather than the zero-hazard obstruction.

**Conceptual connection:** The same asymptotic gap tail can conceal different age-by-age conditional risks.

**Source pointers:** Anchor connection: [Childs §21.1, specifying the oracle model][childs-query-model]. Canonical clock construction: [the alternating-hazard theorem](../science/predictable-queries.md#alternating-hazard-theorem) and [survival asymptotics](../science/predictable-queries.md#survival-asymptotics).

### M25

**Selecting useful queries without advance warning**

**Central question:** How can an algorithm exploit low-risk ages without knowing when the next event will occur?

**Understanding target:** Describe the policy that exposes the logical state only at even ages in $`[A,2A]`$, with $`A\asymp N^{1/(2\beta)}`$. Explain how past flags determine the age counter, how swaps implement active queries, and why all other calls remain charged basis-state dummy queries.

**Dependencies and story role:** [M03](#m03), [M09](#m09), [M14](#m14), [M24](#m24). This converts a statistical pattern into a causal quantum algorithm.

**Conceptual connection:** The algorithm selects the risk to which it exposes its coherent state using information already available before the call.

**Source pointers:** Anchor: [Childs §1.2, circuits][childs-basics], and [§21.2, query transformations][childs-queries]. Canonical: [the causal query policy](../science/predictable-queries.md#causal-query-policy); bridge: [parking the logical state](bridge.md#parking-the-logical-state).

### M26

**Paying for rare opportunities**

**Central question:** Does waiting for low-risk ages still produce an advantage after every intervening call is counted?

**Understanding target:** Connect the conditional error bound over $`\Theta(\sqrt N)`$ active calls to the frequency and capacity of sufficiently long cycles. Explain why cycle length and qualification may be correlated, why the cost argument remains valid, and how startup, deadline, and verification complete a deterministic bounded-error budget.

**Dependencies and story role:** [M12](#m12), [M17](#m17), [M25](#m25). This establishes the complete upper cost of the selective policy.

**Conceptual connection:** Low conditional risk is useful only after its exposure benefit is balanced against the charged time needed to find it.

**Source pointers:** Anchor connection: [Childs §19.3, success probabilities][childs-amplification], and [§21.1, query accounting][childs-query-model]. Canonical: [error on active calls](../science/predictable-queries.md#error-on-active-calls), [charged cost and deadline](../science/predictable-queries.md#charged-cost-and-a-fixed-deadline), and [stationary startup](../science/predictable-queries.md#stationary-startup).

### M27

**The matching converse for predictable queries**

**Central question:** Why can no more elaborate adaptive algorithm beat the selective policy's search exponent?

**Understanding target:** Interpret $`B_N=\mathbb E_\pi\min\{\sqrt N,h(A)^{-1}\}`$ as a capped bound on conditional opportunity. Explain why the even-age contribution dominates in the stated strict parameter regime and yields the matching cost $`\Theta(N^{1/2+(\alpha-1)/(2\beta)})`$, including arbitrary protected memory and adaptive control.

**Dependencies and story role:** [M13](#m13), [M24](#m24), [M25](#m25), [M26](#m26). This integrates the second mechanism into an optimality theorem.

**Conceptual connection:** Bounding available conditional information before averaging prevents an adaptive choice of query state from evading the converse.

**Source pointers:** Anchor: [Childs §§23.1–23.3, adversarial lower bounds][childs-adversaries]. Canonical: [the stationary hazard bound](../science/progress-bound.md#stationary-hazard-bound) and [the alternating-family lower bound](../science/predictable-queries.md#lower-bound-for-adaptive-algorithms).

### M28

**Matching the mean and the leading tail exactly**

**Central question:** How can two clocks retain different optimal search costs after their average rate and asymptotic tail have been matched?

**Understanding target:** Explain how positive mixtures with finite-support laws set a common mean and leading tail coefficient while changing only finite hazard prefixes. Retain full support and the persistence of the two exponents. Distinguish equality of the leading asymptotic tails from equality of the entire survival sequences or of higher finite moments.

**Dependencies and story role:** [M20](#m20), [M23](#m23), [M24](#m24), [M27](#m27). This combines both theorems into the project's controlled comparison.

**Conceptual connection:** Matching coarse noise summaries isolates conditional timing as a resource that those summaries fail to determine.

**Source pointers:** Anchor connection: [Childs §21.1, comparisons within a fixed access model][childs-query-model]. Canonical: [equal-mean and equal-tail laws](../science/comparisons.md#full-support-laws-with-equal-mean-and-tail), [persistence of exponents](../science/comparisons.md#the-search-exponents-persist), and [what is matched](../science/comparisons.md#what-is-matched).

### M29

**The classical comparison and physical resource boundary**

**Central question:** What advantage has been established once access, memory, and the advancing clock are all accounted for?

**Understanding target:** Explain the classical $`\Theta(N)`$ bound in the same flagged oracle model and the quantum algorithms' $`O(\log N)`$ workspace. Account for active, dummy, startup, and verification calls. Distinguish the theorem's oracle cost from gate synthesis and laboratory time, and recognize that equal single-call channels do not specify the multitime process experienced by an adaptive algorithm.

**Dependencies and story role:** [M14](#m14), [M20](#m20), [M27](#m27), [M28](#m28). This interprets the comparison in the complete operational model.

**Conceptual connection:** Quantum improvement here depends on both temporal information and the ability to protect a state between useful calls.

**Source pointers:** Anchor: [Childs §§21.1–21.2, query resources][childs-query-model]. Canonical: [classical search](../science/interpretation.md#classical-search-remains-linear), [protected memory](../science/interpretation.md#protected-memory-is-part-of-the-model), and [operational boundaries](../science/interpretation.md#asymptotic-and-operational-boundaries).

### M30

**The global meaning of the two theorems**

**Central question:** What do the matching results establish about temporal noise, and which conclusions remain outside their scope?

**Understanding target:** Synthesize the regular-hazard moment law and the positive-hazard matched-clock separation, including the finite-variance example with costs $`N`$ and $`N^{3/4}`$. Attribute ideal query foundations to the anchor, noisy converse machinery to ARS, and renewal-specific analysis to this project. Preserve the zero-or-one promise, known fixed law, post-query flags, protected memory, fixed error, and excluded critical alternating-hazard boundary.

**Dependencies and story role:** [M20](#m20), [M22](#m22), [M23](#m23), [M27](#m27), [M28](#m28), [M29](#m29). This completes the narrative phase with the contribution, its proof structure, and its limits as one account.

**Conceptual connection:** Optimal noisy computation depends on the opportunities accessible to an algorithm under a specified information and timing model. The two theorems characterize one broad class and demonstrate why coarse summaries do not characterize every renewal clock.

**Source pointers:** Anchor: [Childs §21.1, model specification][childs-query-model], and [§23.2, lower-bound reasoning][childs-adversary-method]. Canonical: [the finite-variance comparison](../science/comparisons.md#a-finite-variance-example), [scientific contribution and attribution](../science/interpretation.md#scientific-contribution-and-inherited-framework), and [scope of the second theorem](../science/predictable-queries.md#other-resources-and-scope).

[childs]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf
[childs-basics]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=9
[childs-search]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=95
[childs-amplification]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=96
[childs-query-model]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=105
[childs-queries]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=106
[childs-adversaries]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=117
[childs-adversary-method]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=118
[childs-search-lower]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=121
