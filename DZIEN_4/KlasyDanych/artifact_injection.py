"""
Self-modifying closure artifact + runtime injector.

This script demonstrates:
1) An "artifact" function that returns a gate() closure capturing f.
2) A runtime injector that finds the captured function object inside gate.__closure__
   and replaces its bytecode (f.__code__) with bytecode of a generated function.

Run:
    python artifact_injection.py
"""

from __future__ import annotations
from typing import Callable, Any


def artifact() -> Callable[[int], Any]:
    """Builds an artifact: a gate() closure that captures a hidden function f()."""

    def f(x: int) -> int:
        return x + 1

    def gate(x: int) -> Any:
        if x == 7:  # "initiation point"
            f.__code__ = (lambda y: f"Ω:{y*y}").__code__
        return f(x)

    return gate


def inject_function(gate_func: Callable[[int], Any], generator: Callable[[], Callable[[int], Any]]) -> None:
    """
    Injects a newly generated function into the artifact at runtime.

    Steps:
    - Traverse gate_func.__closure__ to find a captured callable (the hidden f).
    - Generate a new function via generator().
    - Replace the captured function's bytecode: f.__code__ = new_func.__code__.
    """
    closure = gate_func.__closure__ or ()
    target = None

    for cell in closure:
        obj = cell.cell_contents
        # We intentionally pick the first callable from the closure.
        if callable(obj):
            target = obj
            break

    if target is None:
        raise RuntimeError("No injectable callable found in gate_func.__closure__")

    new_func = generator()

    # Bytecode transplant
    target.__code__ = new_func.__code__


def generator_cube() -> Callable[[int], Any]:
    """Example generator: returns a new function that formats cube values."""
    return lambda x: f"λ:{x**3}"


if __name__ == "__main__":
    g = artifact()

    # original behavior
    print("original:", g(1), g(7), g(2))  # 2  Ω:49  Ω:4

    # create a fresh artifact (so it's not already altered by x==7)
    g2 = artifact()
    print("before injection:", g2(2))  # 3

    inject_function(g2, generator_cube)

    print("after injection:", g2(2), g2(3))  # λ:8  λ:27
