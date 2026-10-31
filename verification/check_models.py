#!/usr/bin/env python3
"""Independent small-system checks for the renewal-search model.

The channel calculations use complete density matrices, explicit XOR oracles,
and computational-basis pinching. They do not simulate the scalar proof as a
substitute for quantum dynamics. Rational renewal calculations are exact.
Finite-size moment diagnostics illustrate proved asymptotics; they are not
evidence of an all-algorithm lower bound.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import sys

import numpy as np


SEED = 20261031
TOLERANCE = 2e-12


def pure_density(vector: np.ndarray) -> np.ndarray:
    return np.outer(vector, vector.conj())


def conjugate(unitary: np.ndarray, rho: np.ndarray) -> np.ndarray:
    return unitary @ rho @ unitary.conj().T


def xor_oracle(n: int, marked: int) -> np.ndarray:
    """Explicit |i,b> -> |i,b xor [i=marked]> permutation matrix."""
    oracle = np.zeros((2 * n, 2 * n), dtype=complex)
    for index in range(n):
        for answer in range(2):
            source = 2 * index + answer
            target = 2 * index + (answer ^ (index == marked))
            oracle[target, source] = 1.0
    return oracle


def pinch_register(
    rho: np.ndarray, dimensions: tuple[int, ...], register: int
) -> np.ndarray:
    """Sum_i P_i rho P_i, retaining coherences inside every index block."""
    labels = np.indices(dimensions)[register].reshape(-1)
    return rho * (labels[:, None] == labels[None, :])


def swap_registers(
    dimensions: tuple[int, ...], first: int, second: int
) -> np.ndarray:
    if dimensions[first] != dimensions[second]:
        raise ValueError("The swapped registers must have equal dimensions.")
    size = math.prod(dimensions)
    unitary = np.zeros((size, size), dtype=complex)
    for coordinate in itertools.product(*(range(d) for d in dimensions)):
        target = list(coordinate)
        target[first], target[second] = target[second], target[first]
        unitary[
            np.ravel_multi_index(tuple(target), dimensions),
            np.ravel_multi_index(coordinate, dimensions),
        ] = 1.0
    return unitary


def trace_distance(first: np.ndarray, second: np.ndarray) -> float:
    difference = first - second
    difference = (difference + difference.conj().T) / 2
    return float(np.abs(np.linalg.eigvalsh(difference)).sum() / 2)


def density_health(rho: np.ndarray) -> dict[str, float]:
    return {
        "trace_error": float(abs(np.trace(rho) - 1)),
        "hermiticity_error": float(np.linalg.norm(rho - rho.conj().T)),
        "minimum_eigenvalue": float(np.linalg.eigvalsh(rho).min()),
    }


def assert_close(value: float, label: str, tolerance: float = TOLERANCE) -> None:
    if not math.isfinite(value) or value > tolerance:
        raise AssertionError(f"{label}: {value:.17g} exceeds {tolerance:.17g}")


def grover_channel_checks() -> dict:
    """Check event/cap formulas through one complete Grover oscillation."""
    minus = np.array([1, -1], dtype=complex) / math.sqrt(2)
    answer_density = pure_density(minus)
    records = []
    global_maximum_probability_error = 0.0
    global_maximum_state_error = 0.0
    timing_control = {"probability_difference": 0.0}

    # N=2 is the smallest nontrivial case; 8 is a power of two; 3 and 17
    # exercise genuine N-dimensional diffusion without a power-of-two shortcut.
    for n in (2, 3, 8, 17):
        theta = math.asin(1 / math.sqrt(n))
        last_query = math.ceil(math.pi / (2 * theta))
        uniform = np.ones(n, dtype=complex) / math.sqrt(n)
        diffusion = 2 * pure_density(uniform) - np.eye(n)
        full_diffusion = np.kron(diffusion, np.eye(2))
        initial = pure_density(np.kron(uniform, minus))
        errors = {"event_probability": 0.0, "clean_cap_probability": 0.0,
                  "event_density_frobenius": 0.0,
                  "clean_density_frobenius": 0.0}
        largest_trace_error = 0.0
        smallest_eigenvalue = 0.0

        # Every possible mark is checked, which also detects index-order errors.
        for marked in range(n):
            oracle = xor_oracle(n, marked)
            rho = initial.copy()
            for ell in range(1, last_query + 1):
                queried = conjugate(oracle, rho)
                flagged = pinch_register(queried, (n, 2), register=0)
                actual_event = float(np.trace(
                    flagged[2 * marked:2 * marked + 2,
                            2 * marked:2 * marked + 2]
                ).real)
                expected_event = math.sin((2 * ell - 1) * theta) ** 2
                probabilities = np.full(n, (1 - expected_event) / (n - 1))
                probabilities[marked] = expected_event
                expected_flagged = np.kron(np.diag(probabilities), answer_density)
                errors["event_probability"] = max(
                    errors["event_probability"], abs(actual_event - expected_event))
                errors["event_density_frobenius"] = max(
                    errors["event_density_frobenius"],
                    float(np.linalg.norm(flagged - expected_flagged)))

                # Diagnostic control: diffusing a flagged state can change the
                # sampling probability. Correct scheduling measures first.
                wrongly_diffused = conjugate(full_diffusion, flagged)
                wrong_probability = float(np.trace(
                    wrongly_diffused[2 * marked:2 * marked + 2,
                                     2 * marked:2 * marked + 2]
                ).real)
                timing_difference = abs(wrong_probability - actual_event)
                if timing_difference > timing_control["probability_difference"]:
                    timing_control = {
                        "n": n, "marked_index_zero_based": marked,
                        "event_query": ell,
                        "correct_measure_before_diffusion": actual_event,
                        "incorrect_diffuse_then_measure": wrong_probability,
                        "probability_difference": timing_difference,
                    }

                # Follow the clean branch to the next full Grover iteration.
                rho = conjugate(full_diffusion, queried)
                actual_clean = float(np.trace(
                    rho[2 * marked:2 * marked + 2,
                        2 * marked:2 * marked + 2]
                ).real)
                angle = (2 * ell + 1) * theta
                expected_clean = math.sin(angle) ** 2
                expected_vector = np.full(
                    n, math.cos(angle) / math.sqrt(n - 1), dtype=complex)
                expected_vector[marked] = math.sin(angle)
                expected_rho = pure_density(np.kron(expected_vector, minus))
                errors["clean_cap_probability"] = max(
                    errors["clean_cap_probability"], abs(actual_clean - expected_clean))
                errors["clean_density_frobenius"] = max(
                    errors["clean_density_frobenius"],
                    float(np.linalg.norm(rho - expected_rho)))
                for state in (rho, flagged):
                    health = density_health(state)
                    largest_trace_error = max(largest_trace_error, health["trace_error"])
                    smallest_eigenvalue = min(smallest_eigenvalue,
                                             health["minimum_eigenvalue"])
                    assert_close(health["hermiticity_error"], "Grover Hermiticity")

        for label, error in errors.items():
            assert_close(error, f"Grover N={n}: {label}")
        assert_close(largest_trace_error, "Grover trace preservation")
        assert_close(-smallest_eigenvalue, "Grover positivity")
        global_maximum_probability_error = max(
            global_maximum_probability_error, errors["event_probability"],
            errors["clean_cap_probability"])
        global_maximum_state_error = max(
            global_maximum_state_error, errors["event_density_frobenius"],
            errors["clean_density_frobenius"])
        records.append({
            "n": n, "mark_selection": "all marked positions",
            "query_range": [1, last_query],
            "event_formula": "sin((2*ell-1)*asin(1/sqrt(N)))**2",
            "clean_cap_formula": "sin((2*K+1)*asin(1/sqrt(N)))**2",
            "maximum_absolute_errors": errors,
            "largest_trace_error": largest_trace_error,
            "smallest_density_eigenvalue": smallest_eigenvalue,
        })

    if timing_control["probability_difference"] < 0.1:
        raise AssertionError("The flag-timing diagnostic did not distinguish the orderings.")
    return {
        "status": "passed", "registers": ["index", "answer"],
        "maximum_probability_error": global_maximum_probability_error,
        "maximum_density_frobenius_error": global_maximum_state_error,
        "finite_models": records,
        "flag_timing_control": timing_control,
    }


def parking_channel_checks() -> dict:
    """Check an entire parked computation on a maximally entangled probe."""
    d = 3
    marked = 1
    dimensions = (d, d, d, 2)  # reference, protected memory, query index, answer
    rng = np.random.default_rng(SEED)
    matrix = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    unitary, triangular = np.linalg.qr(matrix)
    diagonal = np.diag(triangular)
    unitary = unitary @ np.diag(diagonal.conj() / np.abs(diagonal))
    maximally_entangled = np.eye(d, dtype=complex).reshape(-1) / math.sqrt(d)
    logical_reference = np.kron(np.eye(d), unitary) @ maximally_entangled
    logical_density = pure_density(logical_reference)
    basis_dummy = np.zeros(d, dtype=complex)
    basis_dummy[0] = 1
    plus = np.array([1, 1], dtype=complex) / math.sqrt(2)
    dummy_density = pure_density(np.kron(basis_dummy, plus))
    initial = np.kron(logical_density, dummy_density)

    swap = swap_registers(dimensions, 1, 2)
    oracle = np.kron(np.eye(d * d), xor_oracle(d, marked))
    toggle_answer = np.kron(np.eye(d ** 3), np.diag([1, -1]))
    uniform = np.ones(d, dtype=complex) / math.sqrt(d)
    diffusion = 2 * pure_density(uniform) - np.eye(d)
    query_diffusion = np.kron(np.eye(d * d), np.kron(diffusion, np.eye(2)))
    phase_oracle = np.eye(d, dtype=complex)
    phase_oracle[marked, marked] = -1
    logical_iteration = np.kron(np.eye(d), diffusion @ phase_oracle)
    ideal_logical = conjugate(logical_iteration,
                              conjugate(logical_iteration, logical_density))
    ideal = np.kron(ideal_logical, dummy_density)

    def run(flags: tuple[int, ...], active_fault: bool = False) -> np.ndarray:
        state = initial.copy()
        inactive_slot = 0
        active_slot = 0
        # One parked call before, two between, and one after the useful calls.
        for kind in ("dummy", "useful", "dummy", "dummy", "useful", "dummy"):
            if kind == "dummy":
                state = conjugate(oracle, state)
                if flags[inactive_slot]:
                    state = pinch_register(state, dimensions, register=2)
                inactive_slot += 1
            else:
                state = conjugate(toggle_answer, state)  # |+> -> |->
                state = conjugate(swap, state)
                state = conjugate(oracle, state)
                if active_fault and active_slot == 0:
                    state = pinch_register(state, dimensions, register=2)
                state = conjugate(query_diffusion, state)
                state = conjugate(swap, state)
                state = conjugate(toggle_answer, state)  # restore dummy |+>
                active_slot += 1
        return state

    # The probe is a local-unitary image of a maximally entangled state, so
    # matching its output checks the full logical channel in this dimension.
    distances = []
    for flags in itertools.product((0, 1), repeat=4):
        final = run(flags)
        distance = trace_distance(final, ideal)
        distances.append(distance)
        assert_close(distance, f"Parking channel, inactive flags={flags}")
        health = density_health(final)
        assert_close(health["trace_error"], "Parking trace preservation")
        assert_close(health["hermiticity_error"], "Parking Hermiticity")
        assert_close(-health["minimum_eigenvalue"], "Parking positivity")

    once = pinch_register(conjugate(oracle, initial), dimensions, register=2)
    single_dummy_distance = trace_distance(once, initial)
    assert_close(single_dummy_distance, "Single parked dummy channel")
    active_fault_state = run((1, 1, 1, 1), active_fault=True)
    active_fault_distance = trace_distance(active_fault_state, ideal)
    expected_active_fault_distance = 1 - 1 / d
    assert_close(abs(active_fault_distance - expected_active_fault_distance),
                 "Active dephasing diagnostic")
    return {
        "status": "passed",
        "registers": ["reference", "protected_memory", "query_index", "answer"],
        "dimensions": list(dimensions),
        "input": "seeded local-unitary image of a maximally entangled reference-memory state",
        "sequence": ["dummy", "useful", "dummy", "dummy", "useful", "dummy"],
        "inactive_flags": "every binary pattern on the four dummy calls",
        "useful_query_noise": "zero for the identity-channel comparison",
        "single_dummy_joint_trace_distance": single_dummy_distance,
        "maximum_joint_trace_distance_from_ideal": max(distances),
        "active_fault_control": {
            "description": "dephase the first useful query; dephase every dummy call",
            "joint_trace_distance_from_ideal": active_fault_distance,
            "expected_distance": expected_active_fault_distance,
        },
    }


def fraction_record(value: Fraction) -> dict[str, str | float]:
    return {"exact": str(value), "decimal": float(value)}


def renewal_enumeration() -> dict:
    """Use rational arithmetic throughout a finite-support Markov chain."""
    probabilities = {1: Fraction(1, 2), 2: Fraction(1, 6),
                     3: Fraction(1, 6), 4: Fraction(1, 6)}
    largest_gap = max(probabilities)
    survival = lambda ell: sum(
        (probability for length, probability in probabilities.items() if length >= ell),
        Fraction(0))
    mean = sum((length * probability for length, probability in probabilities.items()),
               Fraction(0))
    stationary = {age: survival(age + 1) / mean for age in range(largest_gap)}
    hazard = {age: probabilities[age + 1] / survival(age + 1)
              for age in stationary}
    updated = {age: Fraction(0) for age in stationary}
    for age, probability in stationary.items():
        updated[0] += probability * hazard[age]
        if hazard[age] != 1:
            updated[age + 1] += probability * (1 - hazard[age])
    assert updated == stationary
    assert sum((stationary[age] * hazard[age] for age in stationary),
               Fraction(0)) == 1 / mean

    moments = []
    for threshold in range(1, largest_gap + 2):
        direct = sum((probability * min(length ** 2, threshold ** 2)
                      for length, probability in probabilities.items()), Fraction(0))
        tail_sum = sum(((2 * ell - 1) * survival(ell)
                        for ell in range(1, threshold + 1)), Fraction(0))
        occupation_sum = sum((ell * survival(ell)
                              for ell in range(1, threshold + 1)), Fraction(0))
        assert direct == tail_sum
        assert occupation_sum <= direct
        assert threshold ** 2 * survival(threshold + 1) <= direct
        assert direct <= threshold * mean
        moments.append({"threshold": threshold,
                        "direct_truncated_second_moment": fraction_record(direct),
                        "tail_sum_identity": fraction_record(tail_sum)})

    def hit_probability(threshold: int, horizon: int) -> Fraction:
        # States enumerate exact weighted histories after coalescing identical
        # (current pre-query age, threshold-hit indicator) pairs.
        states = {(age, age >= threshold): probability
                  for age, probability in stationary.items()}
        for _ in range(1, horizon):
            next_states: dict[tuple[int, bool], Fraction] = {}
            for (age, hit), probability in states.items():
                for next_age, transition_probability in (
                    (0, hazard[age]), (age + 1, 1 - hazard[age])):
                    if transition_probability == 0:
                        continue
                    key = (next_age, hit or next_age >= threshold)
                    next_states[key] = next_states.get(key, Fraction(0)) \
                        + probability * transition_probability
            states = next_states
        return sum((probability for (_, hit), probability in states.items() if hit),
                   Fraction(0))

    crossings = []
    for threshold in range(1, largest_gap + 2):
        initial_tail = sum((probability for age, probability in stationary.items()
                            if age >= threshold), Fraction(0))
        mass_at_threshold = stationary.get(threshold, Fraction(0))
        for horizon in range(1, 2 * largest_gap + 1):
            exact = hit_probability(threshold, horizon)
            bound = initial_tail + (horizon - 1) * mass_at_threshold
            assert exact <= bound
            crossings.append({"threshold": threshold, "horizon": horizon,
                              "exact_hit_probability": fraction_record(exact),
                              "upward_crossing_bound": fraction_record(bound)})

    initial_old_probability = sum((probability for age, probability in stationary.items()
                                   if age >= 2), Fraction(0))
    initially_straddling_crossing = stationary[1] * (1 - hazard[1])
    two_call_hit_probability = hit_probability(2, 2)
    assert two_call_hit_probability == initial_old_probability + initially_straddling_crossing
    assert initially_straddling_crossing > 0
    return {
        "status": "passed_exact_rational_arithmetic",
        "gap_probabilities": {str(k): str(v) for k, v in probabilities.items()},
        "mean_gap": fraction_record(mean),
        "stationary_age_probabilities": {str(k): str(v) for k, v in stationary.items()},
        "hazards": {str(k): str(v) for k, v in hazard.items()},
        "stationarity_exact": True,
        "moments": moments,
        "crossing_enumeration": crossings,
        "initially_straddling_witness": {
            "threshold": 2, "horizon": 2,
            "initial_old_age_probability": fraction_record(initial_old_probability),
            "crossing_from_initial_age_one_without_an_event":
                fraction_record(initially_straddling_crossing),
            "true_crossing_probability": fraction_record(two_call_hit_probability),
            "corrected_bound_is_tight": True,
            "interpretation": "Counting only new renewal intervals misses the positive straddling contribution.",
        },
    }


def moment_diagnostics() -> dict:
    """Deterministic moment sums, explicitly not query-complexity experiments."""
    records = []
    for threshold in (16, 64, 256, 1024, 4096, 16384, 65536):
        ell = np.arange(1, threshold + 1, dtype=float)
        increment = 2 * ell - 1
        pareto_15 = float(np.sum(increment * ell ** (-1.5)))
        pareto_2 = float(np.sum(increment * ell ** (-2.0)))
        pareto_3 = float(np.sum(increment * ell ** (-3.0)))
        boundary = float(np.sum(increment / (ell * (1 + np.log(ell)) ** 2)))
        records.append({
            "threshold_R": threshold,
            "N_if_R_equals_sqrt_N": threshold ** 2,
            "pareto_alpha_1_5": {
                "M_R": pareto_15,
                "M_R_over_sqrt_R_limit_4": pareto_15 / math.sqrt(threshold),
            },
            "pareto_alpha_2": {
                "M_R": pareto_2,
                "M_R_over_log_R_limit_2": pareto_2 / math.log(threshold),
            },
            "pareto_alpha_3": {"M_R_converges_to_finite_constant": pareto_3},
            "logarithmic_boundary_p_2": {
                "M_R": boundary,
                "M_R_times_log_R_squared_over_R_limit_2":
                    boundary * math.log(threshold) ** 2 / threshold,
            },
        })
    return {
        "role": "illustration_only",
        "method": "finite deterministic evaluation of sum_(ell=1)^R (2ell-1) S(ell)",
        "limitation": "These sums do not prove any asymptotic law or any quantum lower bound.",
        "records": records,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().with_name("results.json"))
    arguments = parser.parse_args()
    source = Path(__file__).resolve()
    results = {
        "schema_version": 1,
        "status": "passed",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "seed": SEED,
        "floating_point_tolerance": TOLERANCE,
        "environment": {
            "python_version": platform.python_version(),
            "python_implementation": platform.python_implementation(),
            "numpy_version": np.__version__,
            "platform": platform.platform(),
            "python_executable": sys.executable,
        },
        "check_models_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "grover_channels": grover_channel_checks(),
        "protected_memory_channels": parking_channel_checks(),
        "renewal_exact_checks": renewal_enumeration(),
        "finite_size_moment_diagnostics": moment_diagnostics(),
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(json.dumps(results, indent=2, sort_keys=True,
                                           allow_nan=False) + "\n", encoding="utf-8")
    print(f"All model checks passed. Results: {arguments.output}")
    print("Maximum Grover probability error:",
          results["grover_channels"]["maximum_probability_error"])
    print("Maximum parked-channel trace distance:",
          results["protected_memory_channels"]["maximum_joint_trace_distance_from_ideal"])
    print("Active-slot dephasing control trace distance:",
          results["protected_memory_channels"]["active_fault_control"]
          ["joint_trace_distance_from_ideal"])


if __name__ == "__main__":
    main()
