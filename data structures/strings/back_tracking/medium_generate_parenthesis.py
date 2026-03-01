"""=============================================================================
MEDIUM (Backtracking): Generate Parentheses
=============================================================================

Given n pairs of parentheses, generate all combinations of well-formed
(valid) parentheses.

Examples:
    n = 1  ->  ["()"]
    n = 2  ->  ["(())", "()()"]
    n = 3  ->  ["((()))", "(()())", "(())()", "()(())", "()()()"]

Constraints:
    - 1 <= n <= 8

Target:
    - Time:  O(4^n / sqrt(n))   (Catalan number)
    - Space: O(n)               (recursion depth)

Hints:
    - At each step, you can add '(' if open_count < n
    - You can add ')' if close_count < open_count
    - Backtrack when the current string reaches length 2*n

-----------------------------------------------------------------------------
YOUR TASK
-----------------------------------------------------------------------------
Implement `generate_parentheses(n: int) -> list[str]`.
"""

from __future__ import annotations


def generate_parentheses(n: int) -> list[str]:
    """Return all valid combinations of n pairs of parentheses."""

    result: list[str] = []

    def _backtrack(current: list[str], open_count: int, close_count: int) -> None:
        # Base case: we've placed all 2*n characters
        if len(current) == 2 * n:
            result.append("".join(current))
            return

        # Choice 1: place '(' if we haven't used all n opens
        if open_count < n:
            current.append("(")
            _backtrack(current, open_count + 1, close_count)
            current.pop()  # backtrack

        # Choice 2: place ')' if it won't create an invalid prefix
        if close_count < open_count:
            current.append(")")
            _backtrack(current, open_count, close_count + 1)
            current.pop()  # backtrack

    _backtrack([], 0, 0)
    return result


def _run_samples() -> None:
    assert generate_parentheses(1) == ["()"]
    assert generate_parentheses(2) == ["(())", "()()"]
    assert generate_parentheses(3) == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()",
    ]
    # n = 0 edge case
    assert generate_parentheses(0) == [""]


if __name__ == "__main__":
    _run_samples()
    print("All sample tests passed.")
