"""=============================================================================
EASY (Stack): Valid Parentheses
=============================================================================

Given a string `s` containing only the characters '(', ')', '{', '}', '[', ']'
return True if the input string is valid.

A string is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.

Examples:
    s = "()"     -> True
    s = "()[]{}" -> True
    s = "(]"     -> False

Constraints (assume):
    - 0 <= len(s) <= 200_000

Target:
    - Time:  O(n)
    - Space: O(n)

-----------------------------------------------------------------------------
YOUR TASK
-----------------------------------------------------------------------------
Implement `is_valid_parentheses(s: str) -> bool`.
"""

from __future__ import annotations


def is_valid_parentheses(s: str) -> bool:
    """Return True if all brackets are properly closed and nested."""

    # TODO: Implement using a stack.
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return not stack


def _run_samples() -> None:
    assert is_valid_parentheses("()") is True
    assert is_valid_parentheses("()[]{}") is True
    assert is_valid_parentheses("(]") is False

    assert is_valid_parentheses("([{}])") is True
    assert is_valid_parentheses("(") is False
    assert is_valid_parentheses("") is True


if __name__ == "__main__":
    _run_samples()
    print("All sample tests passed.")
