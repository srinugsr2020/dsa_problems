"""=============================================================================
MEDIUM (Dynamic Programming): Longest Palindromic Substring
=============================================================================

Given a string s, return the longest substring that is a palindrome.

Examples:
    s = "babad"  ->  "bab"  (or "aba" — both valid)
    s = "cbbd"   ->  "bb"
    s = "a"      ->  "a"

Constraints:
    - 1 <= len(s) <= 1000

Target (expand-around-centre approach):
    - Time:  O(n^2)
    - Space: O(1)

Hints:
    - A palindrome mirrors around its centre
    - Centres can be between characters (even-length) or on characters (odd)
    - Expand outward while characters match

-----------------------------------------------------------------------------
YOUR TASK
-----------------------------------------------------------------------------
Implement `longest_palindrome(s: str) -> str`.
"""

from __future__ import annotations


def longest_palindrome(s: str) -> str:
    """Return the longest palindromic substring of s."""

    if len(s) <= 1:
        return s

    start = 0
    max_len = 1

    def _expand(left: int, right: int) -> None:
        """Expand around centre and update best result."""
        nonlocal start, max_len
        while left >= 0 and right < len(s) and s[left] == s[right]:
            length = right - left + 1
            if length > max_len:
                start = left
                max_len = length
            left -= 1
            right += 1

    for i in range(len(s)):
        # Odd-length palindromes (single char centre)
        _expand(i, i)
        # Even-length palindromes (gap centre)
        _expand(i, i + 1)

    return s[start : start + max_len]


def _run_samples() -> None:
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") in ("a", "c")
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("aacabdkacaa") == "aca"
    assert longest_palindrome("") == ""


if __name__ == "__main__":
    _run_samples()
    print("All sample tests passed.")
