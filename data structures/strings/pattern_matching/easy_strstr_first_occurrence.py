"""=============================================================================
EASY (Pattern Matching): Find First Occurrence (strStr)
=============================================================================

Given two strings `haystack` and `needle`, return the index of the first
occurrence of `needle` in `haystack`, or -1 if `needle` is not part of
`haystack`.

Examples:
    haystack = "sadbutsad", needle = "sad" -> 0
    haystack = "leetcode", needle = "leeto" -> -1

Constraints (assume):
    - 0 <= len(haystack), len(needle) <= 200_000

Target:
    - Time:  O(n*m) is accepted for EASY, but try to keep it clean.
    - Space: O(1)

Extra challenge:
    - Implement KMP for O(n+m) (not required here).

-----------------------------------------------------------------------------
YOUR TASK
-----------------------------------------------------------------------------
Implement `find_first_occurrence(haystack: str, needle: str) -> int`.
"""

from __future__ import annotations


def find_first_occurrence(haystack: str, needle: str) -> int:
    """Return the first index of needle in haystack, else -1.

    Naive O(n * m) sliding match — sufficient for the EASY level.
    See medium_kmp_search.py for the O(n + m) KMP solution.

    Time:  O(n * m)  where n = len(haystack), m = len(needle)
    Space: O(1)
    """

    # Convention: an empty needle is always found at position 0.
    if not needle:
        return 0

    n, m = len(haystack), len(needle)
    # Only need to check starting positions where a full match can fit.
    for i in range(n - m + 1):
        if haystack[i : i + m] == needle:
            return i

    return -1


def _run_samples() -> None:
    assert find_first_occurrence("sadbutsad", "sad") == 0
    assert find_first_occurrence("leetcode", "leeto") == -1

    # Edge cases
    assert find_first_occurrence("", "") == 0
    assert find_first_occurrence("abc", "") == 0
    assert find_first_occurrence("", "a") == -1
    assert find_first_occurrence("aaaaa", "bba") == -1


if __name__ == "__main__":
    _run_samples()
    print("All sample tests passed.")
