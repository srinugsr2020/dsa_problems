"""=============================================================================
MEDIUM (Backtracking): Letter Combinations of a Phone Number
=============================================================================

Given a string containing digits from 2-9, return all possible letter
combinations that the number could represent (like a phone keypad).

Mapping (standard phone keypad):
    2 -> "abc"   3 -> "def"   4 -> "ghi"   5 -> "jkl"
    6 -> "mno"   7 -> "pqrs"  8 -> "tuv"   9 -> "wxyz"

Examples:
    digits = "23"  ->  ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    digits = ""    ->  []
    digits = "2"   ->  ["a","b","c"]

Constraints:
    - 0 <= len(digits) <= 4
    - digits[i] is in '2'..'9'

Target:
    - Time:  O(4^n)   where n = len(digits), at most 4 letters per digit
    - Space: O(n)     recursion depth

Hints:
    - Map each digit to its letters
    - Backtrack: for each digit pick one letter, recurse on the rest

-----------------------------------------------------------------------------
YOUR TASK
-----------------------------------------------------------------------------
Implement `letter_combinations(digits: str) -> list[str]`.
"""

from __future__ import annotations

# Phone keypad mapping
_KEYPAD: dict[str, str] = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


def letter_combinations(digits: str) -> list[str]:
    """Return all letter combinations for the given digit string."""

    if not digits:
        return []

    result: list[str] = []

    def _backtrack(index: int, current: list[str]) -> None:
        # Base case: built a full-length combination
        if index == len(digits):
            result.append("".join(current))
            return

        # Try each letter mapped to the current digit
        for letter in _KEYPAD[digits[index]]:
            current.append(letter)
            _backtrack(index + 1, current)
            current.pop()  # backtrack

    _backtrack(0, [])
    return result


def _run_samples() -> None:
    assert letter_combinations("23") == [
        "ad", "ae", "af",
        "bd", "be", "bf",
        "cd", "ce", "cf",
    ]
    assert letter_combinations("") == []
    assert letter_combinations("2") == ["a", "b", "c"]
    assert letter_combinations("79") == [
        "pw", "px", "py", "pz",
        "qw", "qx", "qy", "qz",
        "rw", "rx", "ry", "rz",
        "sw", "sx", "sy", "sz",
    ]


if __name__ == "__main__":
    _run_samples()
    print("All sample tests passed.")
