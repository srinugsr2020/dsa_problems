"""Phone Letter Combinations

Problem:
Expand a short string of digits 2 through 9 into all strings formed by choosing
one letter for each digit. Use keypad order. No digits returns an empty list.

Examples:
- "23" returns ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
- "" returns [].

Approaches:
- Baseline: Expand one prefix layer at a time.
- Python / standard library: Use itertools.product.
- Optimized: Reuse a path buffer.
"""

from __future__ import annotations

from itertools import product


KEYPAD = dict(zip("23456789", ("abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz")))


def baseline(digits: str) -> list[str]:
    if not digits:
        return []
    prefixes = [""]
    for digit in digits:
        prefixes = [prefix + char for prefix in prefixes for char in KEYPAD[digit]]
    return prefixes


def python_product(digits: str) -> list[str]:
    if not digits:
        return []
    return ["".join(chars) for chars in product(*(KEYPAD[digit] for digit in digits))]


def optimized(digits: str) -> list[str]:
    if not digits:
        return []
    answer = []
    path = [""] * len(digits)

    def visit(index: int) -> None:
        if index == len(digits):
            answer.append("".join(path))
            return
        for char in KEYPAD[digits[index]]:
            path[index] = char
            visit(index + 1)

    visit(0)
    return answer


if __name__ == "__main__":
    for combinations in baseline, python_product, optimized:
        assert combinations("") == []
        assert combinations("3") == ["d", "e", "f"]
        assert combinations("22") == ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]
        expanded = combinations("79")
        assert len(expanded) == len(set(expanded)) == 16
        assert expanded[0] == "pw" and expanded[-1] == "sz"
