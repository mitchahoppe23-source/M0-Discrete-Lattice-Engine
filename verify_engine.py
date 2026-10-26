#!/usr/bin/env python3

"""
Discrete Scale-Invariant Numerical Engine (DSNE)
Verification Suite

Author: Mitchell Allen Hoppe
"""

import math


def verify_pell_state(x: int, y: int) -> bool:
    """Verifies strict integer closure for x^2 - 6y^2 = 1."""
    lhs = (x * x) - 6 * (y * y)
    return lhs == 1


def step_scale_forward(x: int, y: int) -> tuple[int, int]:
    """Applies exact integer matrix transformation."""
    x_next = 5 * x + 12 * y
    y_next = 2 * x + 5 * y
    return x_next, y_next
def calculate_derived_metrics(z: int) -> float:
    """Computes derived logarithmic scale metrics."""
    scale_base = 5.0 + 2.0 * math.sqrt(6.0)
    return z * math.log(scale_base)


def run_verification_suite(initial_x: int = 5, initial_y: int = 2, max_steps: int = 5):
    print("=" * 65)
    print("  M=0 DISCRETE LATTICE ENGINE: VERIFICATION SUITE")
    print("=" * 65)
    print("Base Parameters: Scale Invariant ε = 5 - 2√6")
    print(f"Initial State Vector S_1 = ({initial_x}, {initial_y}, Z=1)")
    print("-" * 65)

    x, y = initial_x, initial_y
    all_passed = True

    for z in range(1, max_steps + 1):
        is_valid = verify_pell_state(x, y)
        metric = calculate_derived_metrics(z)

        status = "PASSED (Integer Closure Maintained)" if is_valid else "FAILED"

        if not is_valid:
            all_passed = False

        print(
            f"Step Z={z}: X={x:<12} Y={y:<12} "
            f"Metric={metric:.4f} | Status: {status}"
        )

        x, y = step_scale_forward(x, y)

    print("-" * 65)

    if all_passed:
        print("VERIFICATION RESULT: ALL SCALE TRANSITIONS MAINTAIN INVARIANT CLOSURE.")
    else:
        print("VERIFICATION RESULT: CRITICAL ERROR IN INTEGER CLOSURE.")

    print("=" * 65)


if __name__ == "__main__":
    run_verification_suite()
